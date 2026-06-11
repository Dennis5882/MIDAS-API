# API 엔드포인트 가이드

MIDAS API의 모든 엔드포인트 참고서입니다. 자세한 내용은 [MIDAS GATE API 공식 매뉴얼](https://support.midasuser.com/hc/ko/p/gate_api_manual)을 참고하세요.

## 기본 정보

### Base URL
```
https://your-midas-server.com/api/v1
```

### 인증 헤더
모든 API 요청에 다음 헤더를 포함해야 합니다:

#### 방법 1: Authorization 헤더 (권장)
```
Authorization: Bearer [발급받은 API 키]
Content-Type: application/json
```

#### 방법 2: X-API-Key 헤더
```
X-API-Key: [발급받은 API 키]
Content-Type: application/json
```

---

## 데이터베이스 조회 엔드포인트

### 1. 프로젝트 정보 조회
- **메서드:** `GET`
- **경로:** `/db/PJCF`
- **설명:** 프로젝트의 전체 정보 조회
- **인증:** 필수
- **응답 예시:**
  ```json
  {
    "status": "success",
    "data": {
      "project_name": "Bridge Project",
      "unit": "m",
      "description": "구조 설계 프로젝트"
    }
  }
  ```

### 2. 단위 정보 조회
- **메서드:** `GET`
- **경로:** `/db/UNIT`
- **설명:** 프로젝트의 단위(Unit) 정보 조회
- **인증:** 필수
- **응답 예시:**
  ```json
  {
    "status": "success",
    "data": {
      "unit": "m",
      "unit_name": "미터"
    }
  }
  ```

### 3. 구조 정보 조회
- **메서드:** `GET`
- **경로:** `/db/STR`
- **설명:** 프로젝트의 구조 정보 조회
- **인증:** 필수
- **쿼리 파라미터:** (선택)
  - `offset`: 페이지 오프셋
  - `limit`: 결과 제한 개수

### 4. 재료 정보 조회
- **메서드:** `GET`
- **경로:** `/db/MAT`
- **설명:** 프로젝트의 재료 정보 조회
- **인증:** 필수

### 5. 속성 정보 조회
- **메서드:** `GET`
- **경로:** `/db/PROP`
- **설명:** 프로젝트의 속성 정보 조회
- **인증:** 필수

---

## 문서 작업 엔드포인트

### 6. 새 프로젝트 생성
- **메서드:** `POST`
- **경로:** `/doc/NEW`
- **설명:** 새로운 프로젝트 생성
- **인증:** 필수
- **Request Body:**
  ```json
  {
    "project_name": "My First Project",
    "unit": "m",
    "description": "Created via API"
  }
  ```
- **응답 예시:**
  ```json
  {
    "status": "success",
    "data": {
      "project_id": "PRJ_001",
      "project_name": "My First Project",
      "created_at": "2024-01-15T10:30:00Z"
    }
  }
  ```

### 7. 프로젝트 수정
- **메서드:** `PUT`
- **경로:** `/doc/UPDATE`
- **설명:** 기존 프로젝트 정보 수정
- **인증:** 필수
- **Request Body:**
  ```json
  {
    "project_id": "PRJ_001",
    "project_name": "Updated Project Name",
    "description": "Updated description"
  }
  ```

### 8. 프로젝트 삭제
- **메서드:** `DELETE`
- **경로:** `/doc/DELETE`
- **설명:** 프로젝트 삭제
- **인증:** 필수
- **Request Body:**
  ```json
  {
    "project_id": "PRJ_001"
  }
  ```

---

## 사용자 관련 엔드포인트

### 9. 로그인
- **메서드:** `POST`
- **경로:** `/user/login`
- **설명:** 사용자 인증 (API-KEY 대신 사용 가능)
- **Request Body:**
  ```json
  {
    "userId": "user_id",
    "password": "password"
  }
  ```
- **응답 예시:**
  ```json
  {
    "status": "success",
    "data": {
      "api_key": "abc123def456xyz789",
      "user_name": "홍길동",
      "expires_at": "2024-12-31T23:59:59Z"
    }
  }
  ```

### 10. 사용자 정보 조회
- **메서드:** `GET`
- **경로:** `/user/info`
- **설명:** 현재 인증된 사용자의 정보 조회
- **인증:** 필수
- **응답 예시:**
  ```json
  {
    "status": "success",
    "data": {
      "user_id": "USER_001",
      "user_name": "홍길동",
      "email": "hong@example.com",
      "role": "admin"
    }
  }
  ```

---

## HTTP 상태 코드

| 코드 | 설명 |
|------|------|
| 200 | 요청 성공 |
| 201 | 리소스 생성 성공 |
| 204 | 요청 성공 (응답 본문 없음) |
| 400 | 잘못된 요청 (필수 파라미터 누락 등) |
| 401 | 인증 실패 (API-KEY 없음 또는 잘못됨) |
| 403 | 접근 거부 (권한 부족) |
| 404 | 리소스 없음 |
| 500 | 서버 오류 |

---

## 에러 응답 예시

### 인증 실패 (401)
```json
{
  "status": "error",
  "code": "UNAUTHORIZED",
  "message": "API-KEY가 유효하지 않습니다."
}
```

### 잘못된 요청 (400)
```json
{
  "status": "error",
  "code": "BAD_REQUEST",
  "message": "필수 파라미터가 누락되었습니다.",
  "details": "project_name은 필수입니다."
}
```

### 리소스 없음 (404)
```json
{
  "status": "error",
  "code": "NOT_FOUND",
  "message": "프로젝트를 찾을 수 없습니다.",
  "details": "project_id: PRJ_INVALID"
}
```

### 서버 오류 (500)
```json
{
  "status": "error",
  "code": "SERVER_ERROR",
  "message": "서버에서 오류가 발생했습니다.",
  "details": "잠시 후 다시 시도해주세요."
}
```

---

## 사용 예시

### cURL
```bash
# 프로젝트 정보 조회
curl -X GET "https://your-midas-server.com/api/v1/db/PJCF" \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json"

# 새 프로젝트 생성
curl -X POST "https://your-midas-server.com/api/v1/doc/NEW" \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "project_name": "My Project",
    "unit": "m",
    "description": "Test Project"
  }'
```

### Python
```python
import requests

API_KEY = "your-api-key"
BASE_URL = "https://your-midas-server.com/api/v1"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 프로젝트 정보 조회
response = requests.get(f"{BASE_URL}/db/PJCF", headers=headers)
print(response.json())

# 새 프로젝트 생성
new_project = {
    "project_name": "My Project",
    "unit": "m",
    "description": "Created via API"
}
response = requests.post(f"{BASE_URL}/doc/NEW", headers=headers, json=new_project)
print(response.json())
```

### JavaScript (Node.js)
```javascript
const API_KEY = "your-api-key";
const BASE_URL = "https://your-midas-server.com/api/v1";

const headers = {
  "Authorization": `Bearer ${API_KEY}`,
  "Content-Type": "application/json"
};

// 프로젝트 정보 조회
fetch(`${BASE_URL}/db/PJCF`, {
  method: "GET",
  headers: headers
})
.then(response => response.json())
.then(data => console.log(data));

// 새 프로젝트 생성
const newProject = {
  "project_name": "My Project",
  "unit": "m",
  "description": "Created via API"
};

fetch(`${BASE_URL}/doc/NEW`, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(newProject)
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## 참고 문서

- [MIDAS GATE API 공식 매뉴얼](https://support.midasuser.com/hc/ko/p/gate_api_manual)
- [MIDAS API 온라인 매뉴얼](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)
- [인증 설정](./AUTHENTICATION.md)
- [5분 시작 가이드](./QUICK-START.md)

---

## 🆘 도움말

- API 관련 문제: [공식 지원 사이트](https://support.midasuser.com)에 문의
- Base URL 확인: MIDAS 서버 관리자에게 문의
- API-KEY 발급: MIDAS 관리자 패널에서 발급받기
