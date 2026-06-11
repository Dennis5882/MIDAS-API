# 인증 설정 가이드

## 🔑 API-KEY 획득

### 1단계: 서버 접속

MIDAS 서버에 접속하여 API-KEY를 발급받습니다.

```
https://your-midas-server.com/admin
```

### 2단계: API-KEY 발급

관리자 패널에서 API-KEY를 생성합니다.

- 사용자 계정 설정에서 "API 토큰 생성" 클릭
- 또는 MIDAS 지원팀에 요청

---

## 📍 Base URL 설정

### 기본 형식

```
https://your-midas-server.com/api/v1
```

### 로컬 개발 환경

```
http://localhost:8080/api/v1
```

---

## 🔐 인증 방법

모든 요청의 헤더에 인증 정보를 포함해야 합니다.

### 방법 1: Authorization 헤더 (권장)

```
Authorization: Bearer YOUR_API_KEY
```

**예시:**

```bash
curl -H "Authorization: Bearer abc123def456" \
  https://your-midas-server.com/api/v1/db/PJCF
```

### 방법 2: X-API-Key 헤더

```
X-API-Key: YOUR_API_KEY
```

**예시:**

```bash
curl -H "X-API-Key: abc123def456" \
  https://your-midas-server.com/api/v1/db/PJCF
```

---

## 💻 언어별 설정

### Python

```python
import requests

API_KEY = "your-api-key-here"
BASE_URL = "https://your-midas-server.com/api/v1"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 모든 요청에 headers 포함
response = requests.get(f"{BASE_URL}/db/PJCF", headers=headers)
```

### JavaScript (Node.js)

```javascript
const API_KEY = "your-api-key-here";
const BASE_URL = "https://your-midas-server.com/api/v1";

const headers = {
  "Authorization": `Bearer ${API_KEY}`,
  "Content-Type": "application/json"
};

fetch(`${BASE_URL}/db/PJCF`, {
  method: "GET",
  headers: headers
})
.then(response => response.json())
.then(data => console.log(data));
```

### cURL

```bash
#!/bin/bash

API_KEY="your-api-key-here"
BASE_URL="https://your-midas-server.com/api/v1"

curl -X GET "${BASE_URL}/db/PJCF" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json"
```

### Excel VBA

```vb
Sub GetProjectInfo()
    Dim xmlHttp As Object
    Dim API_KEY As String
    Dim BASE_URL As String
    
    Set xmlHttp = CreateObject("MSXML2.XMLHTTP")
    API_KEY = "your-api-key-here"
    BASE_URL = "https://your-midas-server.com/api/v1"
    
    xmlHttp.Open "GET", BASE_URL & "/db/PJCF", False
    xmlHttp.SetRequestHeader "Authorization", "Bearer " & API_KEY
    xmlHttp.SetRequestHeader "Content-Type", "application/json"
    xmlHttp.Send
    
    MsgBox xmlHttp.responseText
End Sub
```

---

## 🛡️ 보안 팁

### ✅ 해야 할 것

- ✅ API-KEY를 `.env` 파일에 저장
- ✅ `.env` 파일을 `.gitignore`에 추가
- ✅ 환경 변수로 관리
- ✅ 정기적으로 API-KEY 재발급

### ❌ 하지 말아야 할 것

- ❌ API-KEY를 코드에 직접 입력
- ❌ GitHub에 API-KEY 업로드
- ❌ 공개 저장소에 API-KEY 노출
- ❌ 여러 개발자가 같은 API-KEY 사용

### 환경변수 설정

**.env 파일 (Git에 추적되지 않음)**

```
MIDAS_API_KEY=your-api-key-here
MIDAS_BASE_URL=https://your-midas-server.com/api/v1
```

**Python에서 사용**

```python
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MIDAS_API_KEY")
BASE_URL = os.getenv("MIDAS_BASE_URL")
```

---

## ⚠️ 인증 오류 해결

### 401 Unauthorized

```
문제: API-KEY가 잘못되었거나 없음
해결: API-KEY를 확인하고 헤더에 올바르게 포함했는지 확인
```

### 403 Forbidden

```
문제: API-KEY는 유효하지만 권한 부족
해결: 사용자 권한을 관리자에게 요청
```

### 400 Bad Request

```
문제: 헤더 형식이 잘못됨
해결: Authorization 헤더 형식을 다시 확인
      "Authorization: Bearer YOUR_KEY" 형식 필수
```

---

## 🧪 인증 테스트

### cURL로 테스트

```bash
curl -X GET "https://your-midas-server.com/api/v1/db/PJCF" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -v
```

응답에 `HTTP/1.1 200 OK`가 나타나면 인증 성공입니다.

### Postman으로 테스트

1. **New Request** 클릭
2. **Headers** 탭으로 이동
3. Key: `Authorization`, Value: `Bearer YOUR_API_KEY` 추가
4. **Send** 클릭
5. 상태 코드 200이 나타나면 성공

---

## 📝 다음 단계

1. [5분 시작 가이드](./QUICK-START.md) - 첫 API 호출해보기
2. [엔드포인트 가이드](./ENDPOINTS.md) - 모든 엔드포인트 확인

---

## 🆘 도움말

- 인증 문제가 발생하면 [공식 지원 사이트](https://support.midasuser.com)에 문의하세요.
