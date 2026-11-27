"""AI-free coverage check: does every official article / TOC endpoint have a section in docs/manual?

check_diff.py only looks at articles that *changed*, so an article that was skipped when it was
first documented is never flagged again. This script ignores timestamps and checks everything.

Check A  every article in the "manual" section listing must be represented in docs/manual, by
         (1) its article id (source link or article_map.json), or
         (2) its Input URI having a section, or
         (3) for shared URIs (post/TABLE etc.), one of its TABLE_TYPE values appearing in docs.
Check B  the top-level and design catalog endpoint tables are compared with docs/manual in
         both directions, and with the Input URI of the article each row links to.

Reviewed exceptions live in coverage_exceptions.json (each with a reason) and are listed
separately, so only new findings count.

Exit code 0 -> nothing unreviewed.  Exit code 1 -> unreviewed findings.
"""
import argparse
import glob
import html
import json
import os
import re
import sys
from urllib.error import HTTPError
from urllib.parse import urlsplit

import common

TOC_ARTICLE_ID = "33016922742937"  # MIDAS API Online Manual (table of contents)
_HERE = os.path.dirname(os.path.abspath(__file__))
_DOCS = os.path.join(_HERE, "..", "..", "docs", "manual")
EXCEPTIONS_PATH = os.path.join(_HERE, "coverage_exceptions.json")
ARTICLE_MAP_PATH = os.path.join(_HERE, "article_map.json")

_PATH = r"(?:db|doc|ope|view|post|design|rating)/[A-Za-z0-9_\-/]*[A-Za-z0-9_]"
# Not preceded by a letter or '.', so "midasuser.com/..." fragments are not endpoints.
ENDPOINT_RE = re.compile(r"(?<![A-Za-z.])(" + _PATH + r")", re.I)
# "{base url} + db/X", or a bare "Input URI /DESIGN/..." cell with no base-url prefix.
ARTICLE_URI_RE = re.compile(
    r"(?:base\s*url\s*\}?\s*(?:\+\s*)?/?|Input\s*URI\s*/)\s*(" + _PATH + r")", re.I
)
SECTION_LINE_RE = re.compile(r"^#{2,4} |base.?url|\*\*URL\*\*|Input URI", re.I)
SHARED_URIS = {"POST/TABLE", "POST/TEXT", "VIEW/RESULTGRAPHIC"}
CODE_SELECTORS = {"DESIGN/RC/DRC"}
DESIGN_PATHS = ("DESIGN/", "RATING/")
# The existing KDS 41 and AIK-SRC2K catalogs keep their prior coverage policy.
LEGACY_DESIGN_CATALOGS = {"57678093825049", "57711427405209", "57711471216537"}
VARIANT_RE = re.compile(r'"(TABLE_TYPE|CURRENT_MODE|TEXT_TYPE|DGNCODE)"\s*:\s*"([^"]+)"')


def shared_uri(uri):
    return (uri in SHARED_URIS or uri in CODE_SELECTORS or
            (uri.startswith(DESIGN_PATHS) and uri.endswith("/TABLE")))


def variant_values(text, uri):
    keys = ({"DGNCODE"} if uri in CODE_SELECTORS else
            {"TABLE_TYPE", "CURRENT_MODE", "TEXT_TYPE"} if uri in SHARED_URIS else
            {"TABLE_TYPE", "CURRENT_MODE"})
    return {value for key, value in VARIANT_RE.findall(text) if key in keys and value.lower() != "string"}


def plain_text(body):
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", body or "", flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", " ", body)).replace("\xa0", " ")
    return re.sub(r"\s+", " ", text)


def fetch_bodies():
    """Every manual article with its body: en-us, plus articles that exist in ko only."""
    return common.fetch_section_bodies(common.SECTION_ID)


def parse_toc(body):
    """[(endpoint, [article ids])] from rows whose own cell is an endpoint path."""
    rows = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", body, re.S):
        cells = [plain_text(c).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        for cell in cells:
            # The leading slash is optional: some rows are written "db/XXXX".
            match = re.match(r"/?(" + _PATH + r")", cell, re.I)
            if match:
                rows.append((match.group(1).upper(), re.findall(r"/articles/(\d+)", tr)))
                break
    return rows


def design_catalog_ids(body):
    """Article links in the level-two Design or Design Code section (not in DB/Design)."""
    headings = list(re.finditer(r"<h2\b[^>]*>(.*?)</h2>", body or "", re.I | re.S))
    ids = set()
    for i, heading in enumerate(headings):
        if plain_text(heading[1]).strip().casefold() not in {"design", "design code"}:
            continue
        end = headings[i + 1].start() if i + 1 < len(headings) else len(body)
        for match in re.finditer(r"""<a\b[^>]*\bhref\s*=\s*(["'])(.*?)\1""",
                                 body[heading.end():end], re.I | re.S):
            url = urlsplit(html.unescape(match[2]))
            if url.netloc and (url.scheme not in {"https", "http"} or
                               url.hostname != "support.midasuser.com"):
                continue
            article = re.match(r"/hc/(?:en-us|ko)/articles/(\d+)(?:[-/]|$)", url.path)
            if article:
                ids.add(article[1])
    return ids


def fetch_top_toc_ko():
    url = f"https://support.midasuser.com/api/v2/help_center/ko/articles/{TOC_ARTICLE_ID}.json"
    try:
        return common._get_json(url)["article"]["body"]
    except HTTPError as exc:
        if exc.code != 404:
            raise
        return ""


def design_catalogs(articles, ko_body=None):
    """Collect the deduplicated catalogs, fetching only the missing top-level locale."""
    root = articles[TOC_ARTICLE_ID].get("body")
    ids = design_catalog_ids(root)
    # An archived snapshot predating the Design section has no bridge catalogs to follow.
    if ko_body is None and ids:
        ko_body = fetch_top_toc_ko()
    ids |= design_catalog_ids(ko_body)
    ids -= LEGACY_DESIGN_CATALOGS
    return {aid: parse_toc(articles[aid].get("body")) if aid in articles else None
            for aid in sorted(ids)}


def load_docs():
    sections, full_text = {}, []
    for path in sorted(glob.glob(os.path.join(_DOCS, "[0-9]*.md"))):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        full_text.append(text)
        for line in text.splitlines():
            if SECTION_LINE_RE.search(line):
                for ep in ENDPOINT_RE.findall(line):
                    ep = re.sub(r"(/\d+)+$", "", ep.upper())  # drop record ids ("db/STAG/1")
                    sections.setdefault(ep, set()).add(os.path.basename(path))
    return sections, "\n".join(full_text)


def check_articles(articles, sections, docs_text):
    # Import lazily because check_fields consumes the same URI and discriminator rules.
    import check_fields as cf

    with open(ARTICLE_MAP_PATH, encoding="utf-8") as f:
        mapped = set(re.findall(r'"article_id":\s*"(\d+)"', f.read()))
    linked = set(re.findall(r"/articles/(\d+)", docs_text))
    detail, _ = cf.load_sections()
    missing = []
    for aid, article in sorted(articles.items()):
        if aid == TOC_ARTICLE_ID or aid in mapped or aid in linked:
            continue
        text = plain_text(article.get("body"))
        uris = sorted({u.upper() for u in ARTICLE_URI_RE.findall(text)})
        if any(u in sections and not shared_uri(u) for u in uris):
            continue
        if any(shared_uri(u) for u in uris) and cf.covering(aid, text, detail, {})[0]:
            continue
        missing.append({"key": aid, "title": article["title"], "uris": uris})
    return missing


def check_toc(articles, sections, catalogs=None):
    toc = parse_toc(articles[TOC_ARTICLE_ID]["body"])
    catalog_rows = [(ep, ids, aid) for aid, rows in (catalogs or {}).items()
                    for ep, ids in (rows or [])]
    groups = {}
    for ep, ids, aid in catalog_rows:
        entry = groups.setdefault(ep, {"key": ep, "articles": [], "catalogs": []})
        entry["articles"].extend(i for i in ids if i not in entry["articles"])
        if aid not in entry["catalogs"]:
            entry["catalogs"].append(aid)
    listed = {ep for ep, _ in toc} | set(groups)
    # Unversioned selectors such as DESIGN/RC/DRC are listed individually. They
    # do not put every other RC code family under this catalog's docs-only check.
    catalog_prefixes = {ep.rsplit("/", 1)[0] for ep in groups if ep.count("/") >= 3}
    toc_only = [{"key": ep, "articles": ids} for ep, ids in toc if ep not in sections]
    toc_only.extend(item for ep, item in groups.items() if ep not in sections)
    docs_only = [
        {"key": ep, "files": sorted(files)}
        for ep, files in sorted(sections.items())
        # Other design and rating families may still have their own, untracked catalogs.
        if ep not in listed and
        (not ep.startswith(DESIGN_PATHS) or ep.rsplit("/", 1)[0] in catalog_prefixes)
    ]
    mismatch = []
    for ep, ids in toc:
        for aid in ids:
            if aid not in articles:
                continue
            uris = {u.upper() for u in ARTICLE_URI_RE.findall(plain_text(articles[aid].get("body")))}
            if uris and ep not in uris:
                mismatch.append({"key": f"{ep}@{aid}", "article_uris": sorted(uris)})
    for aid, rows in (catalogs or {}).items():
        if not rows:
            mismatch.append({"key": f"catalog@{aid}", "article_uris": [],
                             "reason": "missing catalog article or endpoint rows"})
    for ep, ids, catalog in catalog_rows:
        if not ids:
            mismatch.append({"key": f"{ep}@catalog:{catalog}", "article_uris": [],
                             "reason": "no article link"})
        for aid in ids:
            body = articles.get(aid, {}).get("body")
            uris = {u.upper() for u in ARTICLE_URI_RE.findall(plain_text(body))}
            item = {"key": f"{ep}@{aid}", "article_uris": sorted(uris), "catalog": catalog}
            if ep not in uris and not any(m["key"] == item["key"] for m in mismatch):
                mismatch.append(item)
    return len(listed), toc_only, docs_only, mismatch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", help="path to write the findings JSON (optional)")
    args = parser.parse_args()

    articles = fetch_bodies()
    sections, docs_text = load_docs()
    catalogs = design_catalogs(articles)
    toc_count, toc_only, docs_only, mismatch = check_toc(articles, sections, catalogs)
    findings = {
        "article_without_section": check_articles(articles, sections, docs_text),
        "toc_only": toc_only,
        "docs_only": docs_only,
        "toc_uri_mismatch": mismatch,
    }
    with open(EXCEPTIONS_PATH, encoding="utf-8") as f:
        exceptions = json.load(f)

    print(f"articles: {len(articles)}  toc endpoints: {toc_count}  docs sections: {len(sections)}")
    if catalogs:
        print(f"design catalogs: {len(catalogs)}  rows: {sum(len(rows or []) for rows in catalogs.values())}")
    reported_articles = {item["key"] for item in findings["article_without_section"]}
    unreviewed = 0
    for name, items in findings.items():
        known = exceptions.get(name, {})
        # The JSON retains the URI-level finding. The console counts an unrepresented
        # bridge endpoint once, under the article(s) that still need writing or review.
        by_article = [i for i in items if name == "toc_only" and i.get("catalogs")
                      and i["articles"] and set(i["articles"]) <= reported_articles]
        new = [i for i in items if i["key"] not in known and i not in by_article]
        active_exceptions = set(known) & articles.keys() if name == "article_without_section" else set(known)
        stale = sorted(active_exceptions - {i["key"] for i in items})
        unreviewed += len(new)
        print(f"\n[{name}] total {len(items)}, reviewed {sum(i['key'] in known for i in items)}, NEW {len(new)}")
        if by_article:
            print(f"  already reported by article: {len(by_article)}")
        for item in new:
            print("  NEW", json.dumps(item, ensure_ascii=False))
        for key in stale:
            print(f"  stale exception (no longer reproduces): {key}")
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(findings, f, ensure_ascii=False, indent=1)
    sys.exit(1 if unreviewed else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
