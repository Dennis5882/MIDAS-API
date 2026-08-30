"""Shared helpers for MIDAS API manual sync scripts. No AI calls here — pure HTTP + diff logic."""
import json
import os
import urllib.request

_DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "docs")

BASE = "https://support.midasuser.com/api/v2/help_center/en-us"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# The "Plug-in" Zendesk section (id 35681419399961) does NOT list its member articles via
# sections/{id}/articles.json — that endpoint returns exactly 1 article (the "Plug-in Online
# Manual" landing page). The other 56 articles are just <a href> links inside that landing
# page's body HTML, each living in its own auto-generated section_id that isn't otherwise
# discoverable. So unlike "manual" (real section listing), "plugin" is tracked as an explicit
# article-id allowlist, fetched one by one via articles/{id}.json. If the landing page's own
# updated_at changes, that's the signal to re-scrape it and check whether the link list
# (docs/plugin/INDEX.md) itself needs updating (tool added/removed/renamed).
_PLUGIN_LANDING_ID = "35639730101529"  # Plug-in Online Manual (catalog page)
_PLUGIN_GUIDE_IDS = [
    "35693347852569",   # Introduction to MIDAS Plug-in
    "35694950947353",   # How to use MIDAS Plug-ins
    "44321576105497",   # Guiding for writing Python Code
    "44321750649369",   # A Guide to Creating Plug-in for Developers
]
_PLUGIN_TOOL_IDS = [
    "35651992652441", "60307252076441", "35679369131289", "40709970824729",
    "35656036758937", "35650468767385", "46935970426905", "46857988729753",
    "52564358801049", "35661003551385", "35845551989401", "45536334603161",
    "60341711486361", "45496104876313", "41509743351193", "56841756166681",
    "60340982021529", "35639906272025", "45543036560921", "35649982873625",
    "49393118303897", "45352026157593", "35681919947673", "56728677543321",
    "45354275911321", "40706127836953", "50959239482393", "60469083421593",
    "35649669387289", "45537498601881", "35651585867801", "47130265330841",
    "45548001795865", "35654598923161", "52596776672537", "60470400396953",
    "35649267067545", "45716286965273", "35651417232025", "35658068066841",
    "45545604010521", "35824220762521", "58178248491161", "60317101122329",
    "52808991968665", "40708129121817", "40663607747737", "45306728128921",
    "60315550956825", "52715682940313", "35655721814937", "40645303004697",
    "60848073556633", "60848423734169",
    "60997850893209", "60998764028185",
    "61258768334233", "61259043302041", "61259174909849", "61259225090329",
    "61259382041369", "61486703401753", "61655350763289",
]
# 2026-08-30 폐기됨(공식 사이트에서 삭제, 404 확인) — 더 이상 조회 대상 아님. docs/plugin/INDEX.md
# No.53/54("Floor Load Table Generator"/"Easy Result Table")에 ⚠️ 폐기됨으로 표시, 문서는 보존.
#   "49475987573657", "49504449511705",
PLUGIN_ARTICLE_IDS = [_PLUGIN_LANDING_ID] + _PLUGIN_GUIDE_IDS + _PLUGIN_TOOL_IDS  # 68 ids

# Zendesk resources tracked by this repo. "manual" = JSON Manual section (REST endpoint
# schema reference, docs/manual/*), "plugin" = Plug-in article-id allowlist (GUI-embedded
# automation tools, docs/plugin/*).
SECTIONS = {
    "manual": {
        "mode": "section",
        "id": "30087500371097",
        "manifest": os.path.join(_DOCS_DIR, "manual", ".sync_manifest.json"),
    },
    "plugin": {
        "mode": "id_list",
        "ids": PLUGIN_ARTICLE_IDS,
        "manifest": os.path.join(_DOCS_DIR, "plugin", ".sync_manifest.json"),
    },
}
DEFAULT_SECTION = "manual"

# Backward-compat aliases (old single-section scripts/callers).
SECTION_ID = SECTIONS[DEFAULT_SECTION]["id"]
MANIFEST_PATH = SECTIONS[DEFAULT_SECTION]["manifest"]


def _get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_all_articles(section_id=SECTION_ID):
    """Fetch {id: {title, updated_at, html_url}} for every article in the given section
    (via sections/{id}/articles.json listing — only works for sections that actually list
    their member articles through the API; see PLUGIN_ARTICLE_IDS for the "plugin" exception).
    """
    articles = {}
    page = 1
    while True:
        data = _get_json(f"{BASE}/sections/{section_id}/articles.json?per_page=100&page={page}")
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


def fetch_articles_by_ids(ids):
    """Fetch {id: {title, updated_at, html_url}} one article at a time via the locale-agnostic
    articles/{id}.json endpoint (no /en-us/ prefix — some Plug-in articles, e.g. the Python
    coding guide, only exist under the ko locale and 404 under /en-us/). Used for sections
    (like "plugin") whose member articles aren't listable through the section API.
    """
    articles = {}
    for aid in ids:
        data = _get_json(
            f"https://support.midasuser.com/api/v2/help_center/articles/{aid}.json"
        )
        a = data["article"]
        articles[str(a["id"])] = {
            "title": a["title"],
            "updated_at": a["updated_at"],
            "html_url": a["html_url"],
        }
    return articles


def fetch_section(name):
    """Dispatch to the right fetch strategy based on SECTIONS[name]["mode"]."""
    cfg = SECTIONS[name]
    if cfg["mode"] == "id_list":
        return fetch_articles_by_ids(cfg["ids"])
    return fetch_all_articles(cfg["id"])


def load_manifest(path=MANIFEST_PATH):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f).get("articles", {})


def save_manifest(articles, path=MANIFEST_PATH, section_id=SECTION_ID):
    payload = {"section_id": section_id, "article_count": len(articles), "articles": articles}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
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
