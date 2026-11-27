"""Append the official Specifications rows that docs/manual is missing (additive only).

For every article where check_fields.py finds keys absent from the covering section, this adds a
block at the end of that section:

    <!-- om-fields:ARTICLE_ID -->
    **OM 원문 추가 필드 — Title ([id](url))**
    | No. | 설명 | Key | ... |      <- rows copied verbatim from the official table
    Schema·요청 예제에만 있는 Key: ...
    <!-- /om-fields -->

Existing text is never edited. Blocks carry markers, so a re-run first removes every generated block
and rebuilds it from the current official article (idempotent; keeps the blocks in sync with OM).

  python fill_fields.py            # rewrite docs/manual
  python fill_fields.py --dry-run  # only report
"""
import argparse
import collections
import json
import os
import re
import sys

import check_fields as cf
from check_coverage import EXCEPTIONS_PATH, fetch_bodies
from common import SYNC_LOCALE
from om_parse import md_escape, spec_rows

# a run of adjacent generated blocks is removed as one, so re-runs do not pile up blank lines
BLOCK_RE = re.compile(r"\n*(?:<!-- om-fields:\d+ -->.*?<!-- /om-fields -->\n*)+", re.S)
SKIP_HEAD = re.compile(r"End-to-End|워크플로|Workflow|공통 설정|Table of Contents|목차")
HC = "https://support.midasuser.com/hc/en-us/articles/"


def read(path):
    with open(path, "rb") as f:
        raw = f.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def write(path, text, crlf):
    with open(path, "wb") as f:
        f.write((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))


def strip_blocks():
    """{path: (original text, text without generated blocks, crlf)}; nothing is written."""
    out = {}
    for path in sorted(__import__("glob").glob(os.path.join(cf._DOCS, "[0-9]*.md"))):
        text, crlf = read(path)
        new = BLOCK_RE.sub("\n\n", text)
        out[path] = (text, new.rstrip("\n") + "\n" if new != text else text, crlf)
    return out


def host_section(finding):
    cands = [s for s in finding["sections"] if not SKIP_HEAD.search(s["heading"])] or finding["sections"]
    return min(cands, key=lambda s: (s["level"], s["start"]))


def block(aid, title, url, missing, rows):
    url = re.sub(r"(/articles/\d+).*$", r"\1", url)  # drop the title slug, keep the locale
    lines = [f"<!-- om-fields:{aid} -->", f"**OM 원문 추가 필드 — {title} ([{aid}]({url}))**", "",
             "공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.", ""]
    wanted, seen, used = set(missing), set(), set()
    body = []
    group = None
    for row in rows:
        hit = [k for k in row["keys"] if k in wanted]
        if not hit:
            continue
        used |= set(hit)
        desc = row["desc"]
        if row["group"] and row["group"] != group and not desc.startswith(row["group"]):
            desc = f"[{row['group']}] {desc}".strip()
        group = row["group"]
        key = " / ".join(f'`"{k}"`' for k in row["keys"]) or f"`{row['key_text']}`"
        sig = (row["no"], row["desc"], key)
        if sig in seen:
            continue
        seen.add(sig)
        req = f"**{row['required']}**" if row["required"].lower() == "required" else row["required"]
        body.append(f"| {row['no'] or '-'} | {md_escape(desc)} | {key} | {md_escape(row['type'])} | "
                    f"{md_escape(row['default'])} | {md_escape(req)} |")
    if body:
        lines += ["| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |", "| --- | --- | --- | --- | --- | --- |"] + body + [""]
    rest = sorted(wanted - used)
    if rest:
        lines += ["Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): " + ", ".join(f"`{k}`" for k in rest), ""]
    lines.append("<!-- /om-fields -->")
    return "\n".join(lines), len(used), len(rest)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    articles = fetch_bodies()
    # Strip and rebuild in memory and write once at the end, so a failure leaves docs untouched
    # and --dry-run reports the rows a real run would write.
    docs = strip_blocks()
    sections, shared = cf.load_sections({path: stripped for path, (_, stripped, _) in docs.items()})
    mapping = cf.mapped_headings()
    with open(EXCEPTIONS_PATH, encoding="utf-8") as stream:
        skipped = set(json.load(stream).get("article_without_section", {}))
    findings, unmatched, _, _ = cf.analyze(articles, sections, shared, mapping, skipped)

    inserts = collections.defaultdict(list)  # (path, line) -> [(article id, text)]
    added = collections.defaultdict(set)  # host section -> keys already given a row there
    n_rows = n_rest = 0
    # en-us articles first: a ko-only twin of an en-us article (same endpoint, another id) then only
    # adds the keys its twin did not
    order = sorted(findings, key=lambda x: (articles[x["id"]].get("locale") != SYNC_LOCALE, x["id"]))
    for f in order:
        host = host_section(f)
        art = articles[f["id"]]
        place = (host["path"], host["end"])
        if art.get("locale") == SYNC_LOCALE:
            # different en-us articles may share a section and give the same key another meaning
            # (e.g. TYPE of Tapered DB/User vs Tapered Value): every one keeps its own rows
            missing = f["missing"]
            added[place] |= set(missing)
        else:
            missing = [k for k in f["missing"] if k not in added[place]]
            if not missing:
                continue
            # a second ko-only twin of the same section must not repeat these rows
            added[place] |= set(missing)
        rows = spec_rows(art.get("body"))
        text, rows_used, rest = block(f["id"], f["title"], art.get("html_url") or HC + f["id"], missing, rows)
        n_rows += rows_used
        n_rest += rest
        inserts[(host["path"], host["end"])].append(text)
    print(f"articles: {len(findings)}  table keys copied: {n_rows}  schema/example-only keys listed: {n_rest}")
    if args.dry_run:
        return
    by_file = collections.defaultdict(list)
    for (path, end), texts in inserts.items():
        by_file[path].append((end, texts))
    results = {}
    for path, (original, stripped, crlf) in docs.items():
        lines = stripped.split("\n")
        for end, texts in sorted(by_file.get(path, []), reverse=True):
            pos = min(end, len(lines))
            while pos > 0 and lines[pos - 1].strip() in ("", "---"):
                pos -= 1
            lines[pos:pos] = [""] + "\n\n".join(texts).split("\n") + [""]
        results[path] = "\n".join(lines) if path in by_file else stripped
    changed = [path for path, text in results.items() if text != docs[path][0]]
    for path in changed:
        write(path, results[path], docs[path][2])
    print("files changed:", len(changed))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
