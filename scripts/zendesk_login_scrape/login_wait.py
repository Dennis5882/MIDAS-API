"""Open a real (headed) Chrome window against a dedicated profile, let the user log in
manually, then save the rendered target page once login succeeds. Passwords/cookies are
never handled by this script -- the human logs in inside the visible window.
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config

options = Options()
options.add_argument(f"--user-data-dir={config.PROFILE_DIR}")
options.add_argument("--profile-directory=Default")
options.add_argument("--window-size=1280,900")
options.add_argument("--lang=ko-KR")
# NOTE: do not add --headless here. Cloudflare bot management on this site serves an
# empty shell to headless browsers even with a valid logged-in session.

driver = webdriver.Chrome(options=options)
driver.get(config.TARGET_URL)

print("브라우저 창에서 로그인해 주세요. 로그인 완료를 자동으로 감지합니다 (최대 10분 대기)...")

deadline = time.time() + 600
success = False
while time.time() < deadline:
    time.sleep(3)
    url = driver.current_url
    if not any(marker in url for marker in config.LOGIN_DOMAIN_MARKERS):
        success = True
        break

if success:
    driver.get(config.TARGET_URL)
    time.sleep(3)
    with open(config.LIST_PAGE_HTML, "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"SUCCESS -> {config.LIST_PAGE_HTML}")
else:
    print("TIMEOUT -- 로그인이 감지되지 않았습니다. 다시 실행해 주세요.")

driver.quit()
