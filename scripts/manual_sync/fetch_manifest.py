"""Build/overwrite the .sync_manifest.json for one or all tracked Zendesk sections
(docs/manual/.sync_manifest.json for "manual", docs/plugin/.sync_manifest.json for "plugin").

Run this once to establish a baseline (or after an AI-assisted update has been applied and
verified), so future check_diff.py runs have something to compare against. No AI involved.
"""
import argparse

from common import SECTIONS, fetch_section, save_manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--section", choices=sorted(SECTIONS), help="section to snapshot (default: all)"
    )
    args = parser.parse_args()

    targets = [args.section] if args.section else sorted(SECTIONS)
    for name in targets:
        cfg = SECTIONS[name]
        articles = fetch_section(name)
        save_manifest(articles, cfg["manifest"], cfg.get("id", name))
        print(f"[{name}] manifest saved: {len(articles)} articles")


if __name__ == "__main__":
    main()
