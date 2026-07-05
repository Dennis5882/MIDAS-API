"""Build/overwrite docs/manual/.sync_manifest.json from the live Zendesk article list.

Run this once to establish a baseline (or after an AI-assisted update has been applied and
verified), so future check_diff.py runs have something to compare against. No AI involved.
"""
from common import fetch_all_articles, save_manifest


def main():
    articles = fetch_all_articles()
    save_manifest(articles)
    print(f"manifest saved: {len(articles)} articles")


if __name__ == "__main__":
    main()
