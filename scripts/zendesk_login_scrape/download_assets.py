"""Download every asset URL collected in pages_index.json (typically demo videos hosted
on the company's own asset/landing domain -- plain GET, no auth needed in practice so
far). Skips files that already exist and are non-empty, so re-runs are cheap.
"""
import json
import os
import re
import urllib.request

import config

with open(config.PAGES_INDEX_JSON, encoding="utf-8") as f:
    pages = json.load(f)

for p in pages:
    for j, url in enumerate(p["assets"], 1):
        slug = re.sub(r"[^a-zA-Z0-9_-]+", "_", p["title"]).strip("_")
        ext = os.path.splitext(url.split("?")[0])[1] or ".bin"
        suffix = "" if len(p["assets"]) == 1 else f"_{j}"
        filename = f"{p['index']:02d}_{slug}{suffix}{ext}"
        dest = os.path.join(config.ASSETS_DIR, filename)

        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            print(f"[{p['index']:02d}] skip (exists): {filename}")
            continue

        # Download to a .part file first and rename only on success, so a connection
        # drop mid-transfer never leaves a truncated file at `dest` that the exists/size
        # check above would mistake for a completed download on the next run.
        part = dest + ".part"
        req = urllib.request.Request(url, headers={"User-Agent": config.USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp, open(part, "wb") as out:
                total = 0
                while True:
                    chunk = resp.read(1024 * 256)
                    if not chunk:
                        break
                    out.write(chunk)
                    total += len(chunk)
            os.replace(part, dest)
            print(f"[{p['index']:02d}] OK  {filename}  ({total/1024/1024:.1f} MB)")
        except Exception as e:
            if os.path.exists(part):
                os.remove(part)
            print(f"[{p['index']:02d}] FAIL {filename}: {e}")
