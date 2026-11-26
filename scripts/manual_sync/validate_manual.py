"""Validate docs/manual/*.md and docs/plugin/**/*.md: every ```json block must parse, and
every TOC link must resolve to a real GitHub-generated heading anchor. No AI involved — run
after any AI-assisted patch to catch mistakes before committing.

Exit code 0 -> all clean. Exit code 1 -> problems found (printed to stdout).
"""
import glob
import json
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
TARGET_DIRS = [
    os.path.join(REPO_ROOT, "docs", "manual"),
    os.path.join(REPO_ROOT, "docs", "plugin"),
]


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


def heading_anchors(path, _cache={}):
    if path not in _cache:
        text = re.sub(r"```.*?```", "", open(path, encoding="utf-8").read(), flags=re.S)
        anchors, seen = set(), {}
        for h in re.findall(r"^#{1,6} (.*)$", text, re.MULTILINE):
            a = gh_anchor(h)
            seen[a] = seen.get(a, -1) + 1
            anchors.add(f"{a}-{seen[a]}" if seen[a] else a)
        _cache[path] = anchors
    return _cache[path]


def tracked_markdown():
    """Markdown files in git (local-only folders are not checked); every .md on disk without git."""
    try:
        out = subprocess.run(["git", "ls-files", "*.md"], cwd=REPO_ROOT, capture_output=True,
                             text=True, check=True).stdout.split()
        return [os.path.join(REPO_ROOT, p) for p in out]
    except (OSError, subprocess.CalledProcessError):
        return glob.glob(os.path.join(REPO_ROOT, "**", "*.md"), recursive=True)


def broken_links():
    """Relative links between Markdown files: the target file must exist and, if an anchor is
    given, the heading too. validate_file() only sees links inside one file."""
    bad = []
    for path in tracked_markdown():
        for target in re.findall(r"\]\(([^)\s]+)\)", open(path, encoding="utf-8").read()):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            file_part, _, anchor = target.partition("#")
            dest = os.path.normpath(os.path.join(os.path.dirname(path), file_part))
            if not os.path.exists(dest):
                bad.append((os.path.relpath(path, REPO_ROOT), target, "missing file"))
            elif anchor and dest.endswith(".md") and anchor not in heading_anchors(dest):
                bad.append((os.path.relpath(path, REPO_ROOT), target, "missing anchor"))
    return bad


def main():
    files = []
    for d in TARGET_DIRS:
        files += glob.glob(os.path.join(d, "**", "*.md"), recursive=True)
    files = sorted(set(files), key=lambda p: os.path.relpath(p, REPO_ROOT))
    total_bad = 0
    total_missing = 0
    print(f"{'file':55} {'json':>5} {'bad':>4} {'links':>6} {'miss':>5}")
    for f in files:
        r = validate_file(f)
        total_bad += len(r["bad_json"])
        total_missing += len(r["missing_anchors"])
        flag = " <<<" if r["bad_json"] or r["missing_anchors"] else ""
        rel = os.path.relpath(f, REPO_ROOT)
        print(f"{rel:55} {r['json_blocks']:>5} {len(r['bad_json']):>4} "
              f"{r['toc_links']:>6} {len(r['missing_anchors']):>5}{flag}")
        if r["bad_json"]:
            print("   bad json:", r["bad_json"][:3])
        if r["missing_anchors"]:
            print("   missing anchors:", r["missing_anchors"][:5])

    print()
    print("TOTAL bad json blocks:", total_bad)
    print("TOTAL missing toc anchors:", total_missing)
    links = broken_links()
    for source, target, why in links:
        print(f"   broken link ({why}): {source} -> {target}")
    print("TOTAL broken cross-file links:", len(links))
    sys.exit(1 if (total_bad or total_missing or links) else 0)


if __name__ == "__main__":
    main()
