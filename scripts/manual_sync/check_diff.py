"""Cheap, AI-free check: compare the live MIDAS API Zendesk article list(s) against the
saved manifest(s) and report what's new/changed/removed, per tracked section
("manual" = JSON Manual, "plugin" = Plug-in). Defaults to checking all sections.

Exit code 0  -> no diff in any checked section, nothing to do.
Exit code 1  -> diff found in at least one section; JSON diff is printed to stdout
                (and optionally written to --out) keyed by section name.

This script never calls an LLM. It is meant to run on every scheduled tick; an AI agent
should only be invoked downstream when this exits 1.
"""
import argparse
import json
import sys

from common import SECTIONS, fetch_section, load_manifest, diff_articles


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--section", choices=sorted(SECTIONS), help="section to check (default: all)"
    )
    parser.add_argument("--out", help="path to write the diff JSON (optional)")
    args = parser.parse_args()

    targets = [args.section] if args.section else sorted(SECTIONS)
    result = {}
    has_diff = False
    for name in targets:
        cfg = SECTIONS[name]
        old = load_manifest(cfg["manifest"])
        new = fetch_section(name)
        diff = diff_articles(old, new)
        section_has_diff = bool(diff["added"] or diff["removed"] or diff["changed"])
        has_diff = has_diff or section_has_diff
        result[name] = {"has_diff": section_has_diff, "checked": len(new), **diff}

    output = json.dumps(result, ensure_ascii=False, indent=1)
    print(output)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output + "\n")
    sys.exit(1 if has_diff else 0)


if __name__ == "__main__":
    main()
