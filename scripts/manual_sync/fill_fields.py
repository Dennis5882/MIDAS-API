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
from om_parse import md_escape, spec_rows

BLOCK_RE = re.compile(r"\n*<!-- om-fields:\d+ -->.*?<!-- /om-fields -->\n*", re.S)
SKIP_HEAD = re.compile(r"End-to-End|워크플로|Workflow|공통 설정|Table of Contents|목차")
HC = "https://support.midasuser.com/hc/en-us/articles/"


def read(path):
    raw = open(path, "rb").read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def write(path, text, crlf):
    open(path, "wb").write((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))


def strip_blocks():
    for path in sorted(__import__("glob").glob(os.path.join(cf._DOCS, "[0-9]*.md"))):
        text, crlf = read(path)
        new = BLOCK_RE.sub("\n\n", text)
        if new != text:
            write(path, new.rstrip("\n") + "\n", crlf)


def host_section(finding):
    cands = [s for s in finding["sections"] if not SKIP_HEAD.search(s["heading"])] or finding["sections"]
    return min(cands, key=lambda s: (s["level"], s["start"]))


def block(aid, title, missing, rows):
    lines = [f"<!-- om-fields:{aid} -->", f"**OM 원문 추가 필드 — {title} ([{aid}]({HC}{aid}))**", "",
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
    if not args.dry_run:
        strip_blocks()
    articles = fetch_bodies()
    sections, shared = cf.load_sections()
    mapping = cf.mapped_headings()
    skipped = set(json.load(open(EXCEPTIONS_PATH, encoding="utf-8")).get("article_without_section", {}))
    findings, unmatched, _, _ = cf.analyze(articles, sections, shared, mapping, skipped)

    inserts = collections.defaultdict(list)  # (path, line) -> [(article id, text)]
    n_rows = n_rest = 0
    for f in sorted(findings, key=lambda x: x["id"]):
        host = host_section(f)
        rows = spec_rows(articles[f["id"]].get("body"))
        text, rows_used, rest = block(f["id"], f["title"], f["missing"], rows)
        n_rows += rows_used
        n_rest += rest
        inserts[(host["path"], host["end"])].append(text)
    print(f"articles: {len(findings)}  table keys copied: {n_rows}  schema/example-only keys listed: {n_rest}")
    if args.dry_run:
        return
    by_file = collections.defaultdict(list)
    for (path, end), texts in inserts.items():
        by_file[path].append((end, texts))
    for path, items in by_file.items():
        text, crlf = read(path)
        lines = text.split("\n")
        for end, texts in sorted(items, reverse=True):
            pos = min(end, len(lines))
            while pos > 0 and lines[pos - 1].strip() in ("", "---"):
                pos -= 1
            lines[pos:pos] = [""] + "\n\n".join(texts).split("\n") + [""]
        write(path, "\n".join(lines), crlf)
    print("files changed:", len(by_file))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
