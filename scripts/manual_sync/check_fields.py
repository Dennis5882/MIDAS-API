"""AI-free field coverage check: is every request key of an official article present in docs/manual?

check_coverage.py only asks whether an article has a section. A section that documents just a
"representative" subset still passes there, so this script compares key by key.

For each article in the "manual" section listing:
  keys      = quoted keys of the specification tables, plus JSON keys of the schema and the request
              examples (response examples are excluded).
  sections  = the docs/manual sections that cover the article: sections linking its id or listed in
              article_map.json; otherwise sections for its Input URI (for shared URIs such as
              post/TABLE, sections containing one of its TABLE_TYPE / CURRENT_MODE values).
  missing   = keys that appear nowhere in those sections.

A key counts as present when its exact name appears as a token, so this measures "mentioned",
not "documented correctly". Treat the result as a list of places to look at.

Exit code 0 -> nothing missing.  Exit code 1 -> missing keys found.
"""
import argparse
import collections
import glob
import html
import json
import os
import re
import sys

from check_coverage import (
    ARTICLE_MAP_PATH,
    ARTICLE_URI_RE,
    ENDPOINT_RE,
    EXCEPTIONS_PATH,
    SECTION_LINE_RE,
    SHARED_URIS,
    TOC_ARTICLE_ID,
    fetch_bodies,
    plain_text,
)

_DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "docs", "manual")
SCHEMA_WORDS = {
    "$schema", "$ref", "type", "properties", "description", "enum", "items", "required", "title",
    "default", "minimum", "maximum", "additionalProperties", "oneOf", "anyOf", "allOf", "const",
    "if", "then", "else", "not", "format", "pattern", "patternProperties", "minItems", "maxItems",
    "minLength", "maxLength", "exclusiveMinimum", "exclusiveMaximum", "minProperties",
    "maxProperties", "definitions", "$defs", "examples", "uniqueItems", "additionalItems",
    "readOnly", "contains", "multipleOf", "dependencies", "unevaluatedProperties", "Argument",
    "Assign",
}
JSON_KEY_RE = re.compile(r'"([A-Za-z_$][A-Za-z0-9_\-]*)"\s*:')
CELL_KEY_RE = re.compile(r'"\s*([A-Za-z_][A-Za-z0-9_\-]*)\s*"')


def article_keys(body):
    """{key: source} where source is "table" or "json"."""
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", body or "", flags=re.S)
    text = plain_text(body)
    start = text.find("Response Examples")
    if start >= 0:
        end = text.find("Specifications", start)
        text = text[:start] + (text[end:] if end >= 0 else "")
    keys = {k: "json" for k in JSON_KEY_RE.findall(text) if k not in SCHEMA_WORDS and not k.startswith("x-")}
    # Specification tables end in  Key | Value Type | Default | Required. Reading only that column
    # keeps quoted enum values from code lists out of the key set.
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", body, re.S):
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)
        if len(cells) < 5:
            continue
        value = html.unescape(re.sub(r"<[^>]+>", " ", cells[-4])).replace("\xa0", " ")
        for key in CELL_KEY_RE.findall(value):
            if key not in SCHEMA_WORDS:
                keys[key] = "table"
    return keys


def load_sections():
    """Every ## / ### block, plus per file the preamble and the shared ("공통") blocks."""
    sections, shared = [], {}
    for path in sorted(glob.glob(os.path.join(_DOCS, "[0-9]*.md"))):
        with open(path, encoding="utf-8") as f:
            lines = f.read().splitlines()
        fenced, heads = False, []
        for n, line in enumerate(lines):
            if line.startswith("```"):
                fenced = not fenced
            elif not fenced:
                m = re.match(r"(#{1,3}) ", line)
                if m:
                    heads.append((n, len(m.group(1))))
        first = next((n for n, level in heads if level > 1), len(lines))
        common = ["\n".join(lines[:first])]
        for i, (n, level) in enumerate(heads):
            if "공통" in lines[n]:
                end = next((m for m, lv in heads[i + 1:] if lv <= level), len(lines))
                common.append("\n".join(lines[n:end]))
        shared[os.path.basename(path)] = "\n".join(common)
        for i, (n, level) in enumerate(heads):
            if level == 1:
                continue
            end = next((m for m, lv in heads[i + 1:] if lv <= level), len(lines))
            block = lines[n:end]
            endpoints = set()
            for line in block:
                if SECTION_LINE_RE.search(line):
                    endpoints |= {re.sub(r"(/\d+)+$", "", e.upper()) for e in ENDPOINT_RE.findall(line)}
            text = "\n".join(block)
            sections.append({
                "file": os.path.basename(path), "path": path, "start": n, "end": end,
                "heading": lines[n], "level": level, "text": text,
                "endpoints": endpoints, "ids": set(re.findall(r"/articles/(\d+)", text)),
            })
    return sections, shared


def mapped_headings():
    """{article id: [(file, section label)]} from article_map.json."""
    with open(ARTICLE_MAP_PATH, encoding="utf-8") as f:
        data = json.load(f)
    out = collections.defaultdict(list)
    for name, entries in data.items():
        if name.startswith("_") or not isinstance(entries, dict):
            continue
        for label, entry in entries.items():
            if isinstance(entry, dict) and entry.get("article_id"):
                out[str(entry["article_id"])].append((name, label))
    return out


def covering(aid, text, sections, mapping):
    hit = [s for s in sections if aid in s["ids"]]
    uris = {u.upper() for u in ARTICLE_URI_RE.findall(text)}
    for name, label in mapping.get(aid, []):
        number = re.match(r"\s*(\d+|[A-H]-\d+)", label)
        if number:
            pattern = re.compile(r"#{2,3} " + re.escape(number.group(1)) + r"[.\s]")
            hit += [s for s in sections if s["file"] == name and pattern.match(s["heading"])]
    own = uris - SHARED_URIS
    by_uri = [s for s in sections if own & s["endpoints"]]
    # the narrowest level that names the endpoint avoids pulling in whole chapter groups
    hit += by_uri
    if uris & SHARED_URIS:
        values = set(re.findall(r'"(?:TABLE_TYPE|CURRENT_MODE|TEXT_TYPE)"\s*:\s*"([^"]+)"', text))
        values -= {"string"}
        hit += [s for s in sections if any(f'"{v}"' in s["text"] for v in values)]
    unique = {(s["file"], s["heading"]): s for s in hit}
    return list(unique.values()), sorted(uris)


def analyze(articles, sections, shared, mapping, skipped):
    """Return (findings, unmatched, checked article count, key count)."""
    findings, unmatched, checked, total = [], [], 0, 0
    for aid, article in sorted(articles.items()):
        if aid == TOC_ARTICLE_ID or aid in skipped:
            continue
        keys = article_keys(article.get("body"))
        if not keys:
            continue
        text = plain_text(article.get("body"))
        found, uris = covering(aid, text, sections, mapping)
        codes = {u.split("/")[-1] for u in uris}
        keys = {k: v for k, v in keys.items() if k.upper() not in codes}
        if not found:
            unmatched.append({"id": aid, "title": article["title"], "uris": uris})
            continue
        checked += 1
        total += len(keys)
        doc = "\n".join(s["text"] for s in found)
        # chapter-wide parameter tables apply to every section of that chapter
        doc += "\n" + "\n".join(shared[name] for name in {s["file"] for s in found})
        tokens = set(re.findall(r"[A-Za-z_$][A-Za-z0-9_\-]*", doc))
        tokens |= {p for t in tokens for p in t.split("-")}
        missing = sorted(k for k in keys if k not in tokens)
        if missing:
            findings.append({
                "id": aid, "title": article["title"], "uris": uris, "keys": len(keys),
                "missing": missing, "missing_in_table": sorted(k for k in missing if keys[k] == "table"),
                "files": sorted({s["file"] for s in found}),
                "sections": [{k: s[k] for k in ("file", "path", "start", "end", "level", "heading")} for s in found],
            })
    return findings, unmatched, checked, total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", help="path to write the findings JSON")
    parser.add_argument("--top", type=int, default=25, help="how many articles to list")
    args = parser.parse_args()

    articles = fetch_bodies()
    sections, shared = load_sections()
    mapping = mapped_headings()
    with open(EXCEPTIONS_PATH, encoding="utf-8") as f:
        skipped = set(json.load(f).get("article_without_section", {}))

    findings, unmatched, checked, total = analyze(articles, sections, shared, mapping, skipped)
    findings.sort(key=lambda x: -len(x["missing"]))
    count = sum(len(x["missing"]) for x in findings)
    print(f"checked articles: {checked}  keys: {total}  unmatched articles: {len(unmatched)}")
    print(f"articles with missing keys: {len(findings)}  missing keys: {count}  "
          f"({count / total:.1%} of keys)" if total else "no keys")
    # Several articles share one schema (e.g. one per country code), so count each gap once per endpoint.
    gaps = {}
    for x in findings:
        group = x["uris"][0] if x["uris"] else x["title"]
        for key in x["missing"]:
            gaps[(group, key)] = gaps.get((group, key), False) or key in x["missing_in_table"]
    by_endpoint = collections.Counter(group for group, _ in gaps)
    print(f"unique gaps (endpoint, key): {len(gaps)}  of which in a specification table: "
          f"{sum(gaps.values())}  endpoints affected: {len(by_endpoint)}")
    print("\nby endpoint:", ", ".join(f"{k} {v}" for k, v in by_endpoint.most_common(12)))
    by_file = collections.Counter()
    for x in findings:
        by_file[x["files"][0]] += len(x["missing"])
    print("\nby chapter (counted per article):", dict(sorted(by_file.items())))
    print(f"\ntop {args.top}:")
    for x in findings[: args.top]:
        print(f"  {len(x['missing']):4d}/{x['keys']:<4d} {x['id']} {x['title'][:55]} {x['missing'][:6]}")
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump({"findings": findings, "unmatched": unmatched}, f, ensure_ascii=False, indent=1)
    sys.exit(1 if findings or unmatched else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
