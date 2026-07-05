"""Shared helpers for MIDAS API manual sync scripts. No AI calls here — pure HTTP + diff logic."""
import json
import os
import urllib.request

SECTION_ID = "30087500371097"  # JSON Manual section on MIDAS support Zendesk
LIST_URL = (
    "https://support.midasuser.com/api/v2/help_center/en-us/sections/"
    f"{SECTION_ID}/articles.json?per_page=100&page={{page}}"
)
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
MANIFEST_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "docs", "manual", ".sync_manifest.json"
)


def fetch_all_articles():
    """Fetch {id: {title, updated_at, html_url}} for every article in the JSON Manual section."""
    articles = {}
    page = 1
    while True:
        req = urllib.request.Request(
            LIST_URL.format(page=page), headers={"User-Agent": USER_AGENT}
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        for a in data.get("articles", []):
            articles[str(a["id"])] = {
                "title": a["title"],
                "updated_at": a["updated_at"],
                "html_url": a["html_url"],
            }
        if not data.get("next_page"):
            break
        page += 1
    return articles


def load_manifest():
    if not os.path.exists(MANIFEST_PATH):
        return {}
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f).get("articles", {})


def save_manifest(articles):
    payload = {"section_id": SECTION_ID, "article_count": len(articles), "articles": articles}
    os.makedirs(os.path.dirname(MANIFEST_PATH), exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


def diff_articles(old, new):
    """Pure comparison, no AI. Returns dict with added/removed/changed id lists."""
    old_ids, new_ids = set(old), set(new)
    added = sorted(new_ids - old_ids)
    removed = sorted(old_ids - new_ids)
    changed = sorted(
        i for i in (old_ids & new_ids) if old[i]["updated_at"] != new[i]["updated_at"]
    )
    return {
        "added": [{"id": i, **new[i]} for i in added],
        "removed": [{"id": i, **old[i]} for i in removed],
        "changed": [
            {"id": i, "title": new[i]["title"], "html_url": new[i]["html_url"],
             "old_updated_at": old[i]["updated_at"], "new_updated_at": new[i]["updated_at"]}
            for i in changed
        ],
    }
