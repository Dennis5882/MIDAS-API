"""Extract sub-page links (title + href) from the saved list/category page HTML."""
import json

from bs4 import BeautifulSoup

import config

with open(config.LIST_PAGE_HTML, encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

seen = set()
items = []
for a in soup.select("a[href]"):
    href = a.get("href", "")
    text = a.get_text(strip=True)
    if not text or not any(marker in href for marker in config.ARTICLE_HREF_MARKERS):
        continue
    key = (text, href)
    if key in seen:
        continue
    seen.add(key)
    items.append({"text": text, "href": href})

with open(config.LINKS_JSON, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"{len(items)}개 링크 추출 -> {config.LINKS_JSON}")
for it in items:
    print("-", it["text"], "->", it["href"])
