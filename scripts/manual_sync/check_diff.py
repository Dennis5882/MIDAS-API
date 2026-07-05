"""Cheap, AI-free check: compare the live MIDAS API Zendesk article list against the
saved manifest and report what's new/changed/removed.

Exit code 0  -> no diff, nothing to do.
Exit code 1  -> diff found; JSON diff is printed to stdout (and optionally written to --out).

This script never calls an LLM. It is meant to run on every scheduled tick; an AI agent
should only be invoked downstream when this exits 1.
"""
import argparse
import json
import sys

from common import fetch_all_articles, load_manifest, diff_articles


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", help="path to write the diff JSON (optional)")
    args = parser.parse_args()

    old = load_manifest()
    new = fetch_all_articles()
    diff = diff_articles(old, new)

    has_diff = bool(diff["added"] or diff["removed"] or diff["changed"])

    if not has_diff:
        print(json.dumps({"has_diff": False, "checked": len(new)}, ensure_ascii=False))
        sys.exit(0)

    result = {"has_diff": True, "checked": len(new), **diff}
    output = json.dumps(result, ensure_ascii=False, indent=1)
    print(output)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output + "\n")
    sys.exit(1)


if __name__ == "__main__":
    main()
