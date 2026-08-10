# 로그인 필요한 Zendesk 카테고리 스크래핑 (Selenium 성공 사례)

`support.midasuser.com`의 일부 카테고리(예: 회원 전용 "Plugin 사례")는 `manual_sync`가 쓰는
공개 Help Center API(`/api/v2/help_center/...`)로 접근할 수 없다. 이 폴더는 그런 **로그인 필수
카테고리**를 뚫은 실제 성공 사례를 재사용 가능한 스크립트로 정리한 것이다.

## 왜 curl/API로는 안 되는가 (먼저 시도했다가 실패한 방법들)

1. **curl + 브라우저에서 복사한 세션 쿠키** → 계속 로그인 페이지로 302 리다이렉트됨.
   Cloudflare `__cf_bm`이 요청마다 새로 발급되는 걸로 봐서, 세션이 브라우저의 TLS/기기 지문에
   묶여 있어 다른 IP/클라이언트(curl)에서 온 요청은 쿠키 값이 맞아도 신뢰하지 않는 것으로 보임.
2. **Zendesk Help Center REST API + 세션 쿠키** → API는 쿠키를 아예 인정하지 않는다. Basic
   Auth(이메일+비번) 또는 API 토큰만 받는데, 이 사이트는 `members.midasuser.com` 커스텀
   SSO라서 애초에 Zendesk 네이티브 비밀번호 자체가 없다. (참고: `manual_sync`가 성공하는
   이유는 그 카테고리들이 **애초에 로그인이 필요 없는 공개 카테고리**이기 때문 — 이 방법과는
   무관.)
3. **Selenium + headless 모드** → 로그인은 됐지만(쿠키가 프로필에 저장되어 있으므로) 이후
   페이지 요청에서 Cloudflare가 헤드리스를 감지해 빈 셸 페이지만 반환함(`<title>`이 그냥
   도메인명). → **headless 끄고 화면 있는 브라우저로 띄워야 통과**.

## 성공한 방법

**진짜 브라우저(Selenium, headed) + 전용 프로필 디렉터리 + 사람이 화면에서 직접 로그인.**

1. `login_wait.py` 실행 → 전용 `chrome_profile/` 디렉터리로 Chrome이 뜸(headless 아님).
2. 사용자가 그 창에서 평소처럼 로그인(비밀번호를 Claude/스크립트에 절대 넘기지 않음).
3. 스크립트가 URL이 로그인 도메인을 벗어날 때까지 폴링 → 로그인 완료 자동 감지 → 대상
   페이지 HTML을 저장.
4. 이후 스크래핑(`scrape_pages.py`)은 **같은 `chrome_profile/`**을 재사용 — Chrome이 쿠키를
   디스크에 저장해두므로 매번 재로그인할 필요 없음. 단, 이때도 **headless 금지**(위 3번 이유).

## 파일 구성

| 파일 | 역할 |
|---|---|
| `login_wait.py` | 대상 URL로 Chrome을 띄우고, 로그인 완료를 자동 감지해 렌더링된 HTML 저장 |
| `parse_links.py` | 저장된 카테고리/목록 페이지 HTML에서 하위 article 링크(제목+URL) 추출 |
| `scrape_pages.py` | 링크 목록을 순회하며 각 페이지의 제목/본문/영상(iframe·video src) 추출 |
| `download_assets.py` | 추출된 영상 등 첨부 URL을 실제 파일로 다운로드 |

## 로컬 실행 순서

```bash
cd scripts/zendesk_login_scrape

# 1) config.py에서 TARGET_URL, LOGIN_DOMAIN_MARKERS 등을 새 대상에 맞게 수정

# 2) 로그인 대기 + 목록 페이지 저장 (Chrome 창이 뜨면 그 안에서 직접 로그인)
python login_wait.py

# 3) 목록 페이지에서 하위 링크 추출
python parse_links.py

# 4) 각 하위 페이지 스크래핑 (headed 유지, 같은 프로필 재사용)
python scrape_pages.py

# 5) 영상/첨부파일 다운로드
python download_assets.py
```

## 재사용 시 체크리스트

- `config.py`의 `TARGET_URL`, `OUT_DIR`을 새 대상에 맞게 바꾼다.
- `chrome_profile/`은 세션(로그인 상태)이 담긴 디렉터리다. 재사용 가능하지만, 세션 만료 시
  `login_wait.py`를 다시 돌려 재로그인 창을 띄우면 된다. 지우고 새로 시작해도 무방(다시
  로그인하면 됨).
- **절대 하지 말 것**: 비밀번호를 대화창/스크립트에 평문으로 넘기기, 다른 도메인(예: Google
  계정) 쿠키를 잘못 복사해 붙여넣기 — 실제로 한 번 이런 실수가 있었다. 브라우저 쿠키를
  요청할 땐 반드시 **대상 사이트 도메인**의 쿠키인지 확인할 것(`Cookie:` 헤더 값이
  `_help_center_session=...`, `_zendesk_session=...` 같은 이름으로 시작해야 정상).
- headless는 이 사이트(Cloudflare 봇 관리 적용)에서는 쓸 수 없다. 다른 사이트에 재사용할 땐
  headless부터 시도해보고, 빈 페이지/제목만 나오면 headed로 전환.

## 실제 성공 사례

- 2026-08-07: `support.midasuser.com/hc/ko/categories/60103640613785`
  ("API 적용 사례" — Plugin 20종, 로그인 필수) → 문서 20개 + 영상 20개(mp4, 총 1.8GB) 전량
  수집 성공. 결과물: `docs/plugin_cases/`.
