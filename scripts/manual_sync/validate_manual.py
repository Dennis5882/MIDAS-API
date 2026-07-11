"""Validate docs/manual/*.md: every ```json block must parse, and every TOC link must
resolve to a real GitHub-generated heading anchor. No AI involved — run after any
AI-assisted patch to catch mistakes before committing.

Exit code 0 -> all clean. Exit code 1 -> problems found (printed to stdout).
"""
import glob
import json
import os
import re
import sys

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
MANUAL_DIR = os.path.join(REPO_ROOT, "docs", "manual")


def gh_anchor(h):
    """Reproduce GitHub's heading-to-anchor algorithm (space-per-hyphen, not collapsed)."""
    h = h.strip().lower()
    h = h.replace("`", "")
    h = re.sub(r"[^\w\s\-가-힣]", "", h)
    h = re.sub(r"\s", "-", h)
    return h


def validate_file(path):
    text = open(path, encoding="utf-8").read()

    blocks = re.findall(r"```json\n(.*?)\n```", text, re.DOTALL)
    bad_snippets = []
    for b in blocks:
        try:
            json.loads(b)
        except Exception as e:
            bad_snippets.append(str(e)[:80])

    headers = re.findall(r"^#{1,6} (.*)$", text, re.MULTILINE)
    anchors = set()
    seen_count = {}
    for h in headers:
        a = gh_anchor(h)
        if a in seen_count:
            seen_count[a] += 1
            a = f"{a}-{seen_count[a]}"
        else:
            seen_count[a] = 0
        anchors.add(a)

    toc_links = re.findall(r"\[.*?\]\(#(.*?)\)", text)
    missing = [l for l in toc_links if l not in anchors]

    return {
        "json_blocks": len(blocks),
        "bad_json": bad_snippets,
        "toc_links": len(toc_links),
        "missing_anchors": missing,
    }


def main():
    files = sorted(glob.glob(os.path.join(MANUAL_DIR, "*.md")), key=os.path.basename)
    total_bad = 0
    total_missing = 0
    print(f"{'file':45} {'json':>5} {'bad':>4} {'links':>6} {'miss':>5}")
    for f in files:
        r = validate_file(f)
        total_bad += len(r["bad_json"])
        total_missing += len(r["missing_anchors"])
        flag = " <<<" if r["bad_json"] or r["missing_anchors"] else ""
        print(f"{os.path.basename(f):45} {r['json_blocks']:>5} {len(r['bad_json']):>4} "
              f"{r['toc_links']:>6} {len(r['missing_anchors']):>5}{flag}")
        if r["bad_json"]:
            print("   bad json:", r["bad_json"][:3])
        if r["missing_anchors"]:
            print("   missing anchors:", r["missing_anchors"][:5])

    print()
    print("TOTAL bad json blocks:", total_bad)
    print("TOTAL missing toc anchors:", total_missing)
    sys.exit(1 if (total_bad or total_missing) else 0)


if __name__ == "__main__":
    main()
