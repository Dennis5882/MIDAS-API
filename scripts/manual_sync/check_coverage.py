"""AI-free coverage check: does every official article / TOC endpoint have a section in docs/manual?

check_diff.py only looks at articles that *changed*, so an article that was skipped when it was
first documented is never flagged again. This script ignores timestamps and checks everything.

Check A  every article in the "manual" section listing must be represented in docs/manual, by
         (1) its article id (source link or article_map.json), or
         (2) its Input URI having a section, or
         (3) for shared URIs (post/TABLE etc.), one of its TABLE_TYPE values appearing in docs.
Check B  the endpoint table of the official table-of-contents article is compared with
         docs/manual in both directions, and with the Input URI of the article each row links to.

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

import common

TOC_ARTICLE_ID = "33016922742937"  # MIDAS API Online Manual (table of contents)
_HERE = os.path.dirname(os.path.abspath(__file__))
_DOCS = os.path.join(_HERE, "..", "..", "docs", "manual")
EXCEPTIONS_PATH = os.path.join(_HERE, "coverage_exceptions.json")
ARTICLE_MAP_PATH = os.path.join(_HERE, "article_map.json")

_PATH = r"(?:db|doc|ope|view|post|design)/[A-Za-z0-9_\-/]*[A-Za-z0-9_]"
# Not preceded by a letter or '.', so "midasuser.com/..." fragments are not endpoints.
ENDPOINT_RE = re.compile(r"(?<![A-Za-z.])(" + _PATH + r")", re.I)
# "{base url} + db/X", or a bare "Input URI /DESIGN/..." cell with no base-url prefix.
ARTICLE_URI_RE = re.compile(
    r"(?:base\s*url\s*\}?\s*(?:\+\s*)?/?|Input\s*URI\s*/)\s*(" + _PATH + r")", re.I
)
SECTION_LINE_RE = re.compile(r"^#{2,4} |base.?url|\*\*URL\*\*|Input URI", re.I)
TABLE_TYPE_RE = re.compile(r'"TABLE_TYPE"\s*:\s*"([A-Za-z0-9_\-/() .]+)"')
SHARED_URIS = {"POST/TABLE", "POST/TEXT", "VIEW/RESULTGRAPHIC"}


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
    with open(ARTICLE_MAP_PATH, encoding="utf-8") as f:
        mapped = set(re.findall(r'"article_id":\s*"(\d+)"', f.read()))
    linked = set(re.findall(r"/articles/(\d+)", docs_text))
    missing = []
    for aid, article in sorted(articles.items()):
        if aid == TOC_ARTICLE_ID or aid in mapped or aid in linked:
            continue
        text = plain_text(article.get("body"))
        uris = sorted({u.upper() for u in ARTICLE_URI_RE.findall(text)})
        if any(u in sections and u not in SHARED_URIS for u in uris):
            continue
        types = TABLE_TYPE_RE.findall(text)
        if any(f'"{t}"' in docs_text for t in types if t.lower() != "string"):
            continue
        missing.append({"key": aid, "title": article["title"], "uris": uris})
    return missing


def check_toc(articles, sections):
    toc = parse_toc(articles[TOC_ARTICLE_ID]["body"])
    listed = {ep for ep, _ in toc}
    toc_only = [{"key": ep, "articles": ids} for ep, ids in toc if ep not in sections]
    docs_only = [
        {"key": ep, "files": sorted(files)}
        for ep, files in sorted(sections.items())
        # DESIGN/ endpoints are listed per code on separate index articles, not in the TOC.
        if ep not in listed and not ep.startswith("DESIGN/")
    ]
    mismatch = []
    for ep, ids in toc:
        for aid in ids:
            if aid not in articles:
                continue
            uris = {u.upper() for u in ARTICLE_URI_RE.findall(plain_text(articles[aid].get("body")))}
            if uris and ep not in uris:
                mismatch.append({"key": f"{ep}@{aid}", "article_uris": sorted(uris)})
    return len(listed), toc_only, docs_only, mismatch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", help="path to write the findings JSON (optional)")
    args = parser.parse_args()

    articles = fetch_bodies()
    sections, docs_text = load_docs()
    toc_count, toc_only, docs_only, mismatch = check_toc(articles, sections)
    findings = {
        "article_without_section": check_articles(articles, sections, docs_text),
        "toc_only": toc_only,
        "docs_only": docs_only,
        "toc_uri_mismatch": mismatch,
    }
    with open(EXCEPTIONS_PATH, encoding="utf-8") as f:
        exceptions = json.load(f)

    print(f"articles: {len(articles)}  toc endpoints: {toc_count}  docs sections: {len(sections)}")
    unreviewed = 0
    for name, items in findings.items():
        known = exceptions.get(name, {})
        new = [i for i in items if i["key"] not in known]
        stale = sorted(set(known) - {i["key"] for i in items})
        unreviewed += len(new)
        print(f"\n[{name}] total {len(items)}, reviewed {len(items) - len(new)}, NEW {len(new)}")
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
