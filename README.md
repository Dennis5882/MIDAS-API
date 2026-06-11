# MIDAS-API

MIDAS API를 사용하여 구조 설계 프로젝트를 프로그래밍 방식으로 제어하고 자동화할 수 있습니다.

## 🚀 빠른 시작

- **처음이신가요?** → [5분 시작 가이드](./docs/QUICK-START.md)
- **API 기본을 알고 싶으신가요?** → [API 개요](./docs/API-OVERVIEW.md)
- **엔드포인트를 찾고 있으신가요?** → [엔드포인트 가이드](./docs/ENDPOINTS.md)
- **인증 설정이 필요하신가요?** → [인증 설정](./docs/AUTHENTICATION.md)

## 📚 주요 기능

- **문서 관리** - 프로젝트 생성, 열기, 저장, 내보내기
- **데이터베이스 조작** - 구조 정보, 재료, 속성 등 관리
- **다중 언어 지원** - Python, JavaScript, Excel VBA 등

## 💻 예제 코드

### Python으로 첫 API 호출

```python
import requests

API_KEY = "your-api-key"
BASE_URL = "https://your-midas-server.com/api/v1"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 프로젝트 정보 조회
response = requests.get(
    f"{BASE_URL}/db/PJCF",
    headers=headers
)

print(response.json())
```

더 많은 예제는 [examples/](./examples/) 디렉토리를 참고하세요.

## 🔗 공식 문서

- [MIDAS API 공식 매뉴얼](https://support.midasuser.com/hc/ko/p/gate_api_manual)
- [MIDAS API 온라인 매뉴얼](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)

## 📖 문서 구조

```
docs/
├── API-OVERVIEW.md      # REST API, JSON, WebSocket 기본 개념
├── AUTHENTICATION.md    # Base URL, API-KEY 설정
├── ENDPOINTS.md         # 전체 엔드포인트 가이드
└── QUICK-START.md       # 5분 안에 시작하기

examples/
├── python/              # Python 예제
├── javascript/          # JavaScript 예제
└── curl/                # cURL 예제
```

## ❓ 도움말

문제가 발생했나요?
- Issues 탭에서 질문하기
- [공식 지원 사이트](https://support.midasuser.com) 방문

## 📝 라이선스

MIDAS API 문서는 MIDAS 공식 사이트를 참고합니다.
