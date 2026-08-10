"""Visit every link from links.json (authenticated, same persisted profile) and save
title/body text/asset URLs (iframe or <video> src) for each page. Must stay headed --
see README for why headless gets blocked here.
"""
import json
import os
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import config

with open(config.LINKS_JSON, encoding="utf-8") as f:
    items = json.load(f)

options = Options()
options.add_argument(f"--user-data-dir={config.PROFILE_DIR}")
options.add_argument("--profile-directory=Default")
options.add_argument("--window-size=1280,900")
options.add_argument("--lang=ko-KR")

driver = webdriver.Chrome(options=options)

results = []
failed = []
try:
    for i, item in enumerate(items, 1):
        url = item["href"]
        print(f"[{i}/{len(items)}] {url}")
        try:
            driver.get(url)
            time.sleep(3)
            html = driver.page_source
            if len(html) < 5000:  # likely still loading / interstitial
                time.sleep(3)
                html = driver.page_source

            soup = BeautifulSoup(html, "html.parser")
            title_el = soup.select_one("h1") or soup.title
            title = title_el.get_text(strip=True) if title_el else item["text"]

            body = soup.select_one("div.article-body, div[class*='article-body'], article")
            body_text = body.get_text("\n", strip=True) if body else ""

            assets = []
            for iframe in soup.select("iframe[src]"):
                src = iframe.get("src", "")
                if any(d in src for d in ("youtube.com", "youtu.be", "vimeo.com", "player")):
                    assets.append(src)
            for video_tag in soup.select("video source[src], video[src]"):
                src = video_tag.get("src", "")
                if src:
                    assets.append(src)
            assets = list(dict.fromkeys(assets))

            slug = re.sub(r"[^a-zA-Z0-9_-]+", "_", url.rstrip("/").split("/")[-1])[:80]
            rec = {"index": i, "title": title, "url": url, "assets": assets, "body_chars": len(body_text)}
            results.append(rec)

            with open(os.path.join(config.PAGES_DIR, f"{i:02d}_{slug}.json"), "w", encoding="utf-8") as f:
                json.dump({**rec, "body_text": body_text}, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[{i}/{len(items)}] FAILED: {e}")
            failed.append({"index": i, "url": url, "error": str(e)})
finally:
    driver.quit()

with open(config.PAGES_INDEX_JSON, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nDONE")
for r in results:
    print(f"- [{r['index']:02d}] {r['title']} | assets={len(r['assets'])} | body_chars={r['body_chars']}")
if failed:
    print(f"\n{len(failed)} page(s) failed and were skipped:")
    for f in failed:
        print(f"- [{f['index']:02d}] {f['url']}: {f['error']}")
