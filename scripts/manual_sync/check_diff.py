"""Cheap, AI-free check: compare the live MIDAS API Zendesk article list(s) against the
saved manifest(s) and report what's new/changed/removed, per tracked section
("manual" = JSON Manual, "plugin" = Plug-in). Defaults to checking all sections.

Exit code 0  -> no diff in any checked section, nothing to do.
Exit code 1  -> diff found in at least one section; JSON diff is printed to stdout
                (and optionally written to --out) keyed by section name.

Each changed article is annotated with which *locale* moved (see --no-locales to skip).
This matters because the article-level updated_at is the max over all translations, so a
ko-only or ja-only edit flags the article while the en-us body we mirror stays identical.
Without the annotation that pattern reads as a cosmetic bump and gets waved through — see
the "locale_note" field for the verdict on each entry.

This script never calls an LLM. It is meant to run on every scheduled tick; an AI agent
should only be invoked downstream when this exits 1.
"""
import argparse
import json
import sys

from common import (
    SECTIONS,
    SYNC_LOCALE,
    diff_articles,
    fetch_section,
    load_manifest,
    locales_changed_since,
)


def annotate_locales(changed):
    """Tag each changed article with the locale(s) whose body actually moved."""
    for entry in changed:
        try:
            moved, locales = locales_changed_since(entry["id"], entry["old_updated_at"])
        except Exception as exc:  # network hiccup must not break the cheap gate
            entry["locale_note"] = f"lookup failed ({type(exc).__name__}); inspect manually"
            continue
        entry["locales_changed"] = moved
        entry["locales_seen"] = sorted(locales)
        if not moved:
            entry["locale_note"] = "metadata only — no translation body is newer"
        elif SYNC_LOCALE in moved:
            entry["locale_note"] = f"{SYNC_LOCALE} changed — normal review"
        else:
            entry["locale_note"] = (
                f"{'/'.join(moved)} changed but {SYNC_LOCALE} did NOT — our fetched "
                f"body looks identical; open the {'/'.join(moved)} page(s) to compare"
            )
    return changed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--section", choices=sorted(SECTIONS), help="section to check (default: all)"
    )
    parser.add_argument("--out", help="path to write the diff JSON (optional)")
    parser.add_argument(
        "--no-locales",
        action="store_true",
        help="skip the per-locale lookup for changed articles (one extra request each)",
    )
    args = parser.parse_args()

    targets = [args.section] if args.section else sorted(SECTIONS)
    result = {}
    has_diff = False
    for name in targets:
        cfg = SECTIONS[name]
        old = load_manifest(cfg["manifest"])
        new = fetch_section(name)
        diff = diff_articles(old, new)
        if diff["changed"] and not args.no_locales:
            annotate_locales(diff["changed"])
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
