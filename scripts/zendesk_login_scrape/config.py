"""Edit these per target. Nothing else in this folder should need changes for a new run."""
import os

# --- 대상 ---
TARGET_URL = "https://support.midasuser.com/hc/ko/categories/60103640613785?page=1&tab=all"
# 로그인 전에는 이 문자열들 중 하나가 URL에 포함됨 (로그인 완료 판정 기준)
LOGIN_DOMAIN_MARKERS = ["members.midasuser.com", "zendesk.com/access"]

# --- 출력 경로 ---
HERE = os.path.dirname(os.path.abspath(__file__))
PROFILE_DIR = os.path.join(HERE, "chrome_profile")
OUT_DIR = os.path.join(HERE, "output")
LIST_PAGE_HTML = os.path.join(OUT_DIR, "list_page.html")
LINKS_JSON = os.path.join(OUT_DIR, "links.json")
PAGES_DIR = os.path.join(OUT_DIR, "pages")
PAGES_INDEX_JSON = os.path.join(OUT_DIR, "pages_index.json")
ASSETS_DIR = os.path.join(OUT_DIR, "assets")

# article 링크로 인정할 URL 패턴 (Zendesk 기준). 다른 사이트로 재사용 시 수정.
ARTICLE_HREF_MARKERS = ["/hc/ko/articles/", "/hc/ko/sections/"]

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

for d in (OUT_DIR, PAGES_DIR, ASSETS_DIR):
    os.makedirs(d, exist_ok=True)
