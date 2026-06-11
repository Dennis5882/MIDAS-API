# 5분 안에 시작하기

이 가이드를 따라 5분 안에 첫 MIDAS API 호출을 완성하세요! 🚀

---

## ⚙️ 사전 준비 (1분)

### 필요한 정보

1. **Base URL** - MIDAS 서버 주소
   ```
   https://your-midas-server.com/api/v1
   ```

2. **API-KEY** - 서버 관리자에게 요청
   ```
   abc123def456xyz789
   ```

---

## 🐍 Python으로 시작 (2분)

### 1단계: 필수 라이브러리 설치

```bash
pip install requests
```

### 2단계: 코드 작성

`test_api.py` 파일을 만들고 다음을 입력하세요:

```python
import requests
import json

# 설정
API_KEY = "your-api-key-here"
BASE_URL = "https://your-midas-server.com/api/v1"

# 헤더 준비
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# API 호출 1: 프로젝트 정보 조회 (GET)
print("=" * 50)
print("1️⃣  프로젝트 정보 조회")
print("=" * 50)

response = requests.get(
    f"{BASE_URL}/db/PJCF",
    headers=headers
)

print(f"상태 코드: {response.status_code}")
print(f"응답:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")

# API 호출 2: 새 프로젝트 생성 (POST)
print("\n" + "=" * 50)
print("2️⃣  새 프로젝트 생성")
print("=" * 50)

new_project = {
    "project_name": "My First Project",
    "unit": "m",
    "description": "Created via API"
}

response = requests.post(
    f"{BASE_URL}/doc/NEW",
    headers=headers,
    json=new_project
)

print(f"상태 코드: {response.status_code}")
print(f"응답:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")

# API 호출 3: 단위 정보 조회 (GET)
print("\n" + "=" * 50)
print("3️⃣  단위 정보 조회")
print("=" * 50)

response = requests.get(
    f"{BASE_URL}/db/UNIT",
    headers=headers
)

print(f"상태 코드: {response.status_code}")
print(f"응답:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")
```

### 3단계: 실행

```bash
python test_api.py
```

**성공 시 출력:**

```
==================================================
1️⃣  프로젝트 정보 조회
==================================================
상태 코드: 200
응답:
{
  "status": "success",
  "data": {
    "project_name": "Bridge Project",
    "unit": "m"
  }
}
```

---

## 🌐 cURL로 시작 (2분)

터미널에서 바로 실행할 수 있습니다.

### API 호출 1: 프로젝트 정보 조회

```bash
curl -X GET \
  https://your-midas-server.com/api/v1/db/PJCF \
  -H "Authorization: Bearer your-api-key-here" \
  -H "Content-Type: application/json"
```

### API 호출 2: 새 프로젝트 생성

```bash
curl -X POST \
  https://your-midas-server.com/api/v1/doc/NEW \
  -H "Authorization: Bearer your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{
    "project_name": "My First Project",
    "unit": "m",
    "description": "Created via API"
  }'
```

### API 호출 3: 단위 정보 조회

```bash
curl -X GET \
  https://your-midas-server.com/api/v1/db/UNIT \
  -H "Authorization: Bearer your-api-key-here" \
  -H "Content-Type: application/json"
```

---

## 📮 Postman으로 시작 (2분)

**Postman 다운로드:** https://www.postman.com/downloads/

### 1단계: 새 Request 만들기

1. **+** 버튼 클릭 → **HTTP**
2. 메소드: **GET**
3. URL: `https://your-midas-server.com/api/v1/db/PJCF`

### 2단계: 인증 헤더 추가

1. **Headers** 탭 클릭
2. 다음 두 행 추가:

| Key | Value |
|-----|-------|
| Authorization | Bearer your-api-key-here |
| Content-Type | application/json |

### 3단계: Send 클릭

**성공 시:**
- 상태: `200 OK`
- Body에 JSON 응답 표시

---

## 🎯 이제 뭘 할까?

### ✅ 첫 API 호출 완료!

다음으로 할 수 있는 것들:

| 문서 | 설명 |
|------|------|
| [엔드포인트 가이드](./ENDPOINTS.md) | 모든 사용 가능한 엔드포인트 확인 |
| [인증 설정](./AUTHENTICATION.md) | API-KEY를 안전하게 관리하기 |
| [예제 코드](../examples/) | 더 많은 실제 예제 확인 |

---

## ⚠️ 자주 묻는 질문

### Q: 401 Unauthorized 에러가 나요

**A:** API-KEY가 잘못되었거나 헤더 형식이 잘못됨

```
✅ 올바른 형식: Authorization: Bearer YOUR_API_KEY
❌ 잘못된 형식: Authorization: YOUR_API_KEY
```

### Q: 404 Not Found 에러가 나요

**A:** Base URL이 잘못되었을 가능성

```bash
# 올바른지 확인하기
curl -X GET https://your-midas-server.com/api/v1/db/PJCF \
  -H "Authorization: Bearer your-api-key"
```

### Q: 타임아웃 에러

**A:** 서버가 응답하지 않음. 서버 연결 확인 후 다시 시도

### Q: 어떤 엔드포인트를 사용할 수 있나요?

**A:** [엔드포인트 가이드](./ENDPOINTS.md)를 확인하세요

---

## 💡 팁

- 🔒 **API-KEY는 비밀로!** - 환경 변수에 저장하세요
- 📝 **요청/응답 로그 남기기** - 디버깅에 유용합니다
- 🧪 **Postman으로 먼저 테스트** - 코드 짜기 전에 API가 작동하는지 확인
- 📚 **공식 문서 참고** - [MIDAS API 매뉴얼](https://support.midasuser.com/hc/ko/p/gate_api_manual)

---

## 🚀 다음 단계

1. [모든 엔드포인트 확인하기](./ENDPOINTS.md)
2. [고급 예제 살펴보기](../examples/)
3. [공식 문서 읽기](https://support.midasuser.com/hc/ko/p/gate_api_manual)

---

문제가 있으신가요? 이슈를 등록하거나 공식 지원팀에 문의하세요!
