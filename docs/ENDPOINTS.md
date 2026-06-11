# API 엔드포인트 가이드

MIDAS API의 모든 엔드포인트 참고서입니다. 자세한 내용은 [MIDAS GATE API 공식 매뉴얼](https://support.midasuser.com/hc/ko/p/gate_api_manual)을 참고하세요.

## 기본 정보

### Base URL
```
https://gate.midasuser.com/api/rest/v1
```

### 인증 헤더
모든 API 요청에 다음 헤더를 포함해야 합니다:

```
X-API-KEY: [발급받은 API 키]
X-USER-ID: [사용자 ID]
Content-Type: application/json
```

---

## 사용자 관련 엔드포인트

### 1. 로그인
- **메서드:** `POST`
- **경로:** `/user-login`
- **설명:** 사용자 인증
- **Request Body:**
  ```json
  {
    "userId": "user_id",
    "password": "password"
  }
  ```

### 2. 사용자 정보 조회
- **메서드:** `GET`
- **경로:** `/users/info`
- **설명:** 현재 사용자의 기본 정보 조회
- **응답:** 사용자 정보 (ID, 이름, 권한 등)

---

## 프로젝트 관련 엔드포인트

### 3. 프로젝트 목록 조회
- **메서드:** `GET`
- **경로:** `/projects`
- **설명:** 사용자가 접근 가능한 프로젝트 목록 조회
- **Query Parameters:**
  - `offset` (선택): 페이지 오프셋
  - `limit` (선택): 결과 제한 개수
- **응답 예시:**
  ```json
  [
    {
      "projectId": "PROJECT_001",
      "projectName": "구조 설계 프로젝트",
      "createdAt": "2024-01-01",
      "status": "active"
    }
  ]
  ```

### 4. 프로젝트 상세 정보 조회
- **메서드:** `GET`
- **경로:** `/projects/{projectId}`
- **설명:** 특정 프로젝트의 상세 정보 조회
- **Path Parameters:**
  - `projectId`: 프로젝트 ID
- **응답:** 프로젝트 상세 정보 (메타데이터, 생성일, 수정일 등)

### 5. 프로젝트 생성
- **메서드:** `POST`
- **경로:** `/projects`
- **설명:** 새로운 프로젝트 생성
- **Request Body:**
  ```json
  {
    "projectName": "새 프로젝트",
    "description": "프로젝트 설명",
    "projectType": "STRUCTURAL"
  }
  ```

### 6. 프로젝트 수정
- **메서드:** `PUT`
- **경로:** `/projects/{projectId}`
- **설명:** 프로젝트 정보 수정
- **Path Parameters:**
  - `projectId`: 프로젝트 ID
- **Request Body:**
  ```json
  {
    "projectName": "수정된 프로젝트명",
    "description": "수정된 설명"
  }
  ```

---

## 도면(문서) 관련 엔드포인트

### 7. 도면 목록 조회
- **메서드:** `GET`
- **경로:** `/projects/{projectId}/drawings`
- **설명:** 프로젝트의 모든 도면(문서) 목록 조회
- **Path Parameters:**
  - `projectId`: 프로젝트 ID
- **응답 예시:**
  ```json
  [
    {
      "drawingId": "DRW_001",
      "drawingName": "기초 도면",
      "createdAt": "2024-01-15",
      "lastModified": "2024-01-20"
    }
  ]
  ```

### 8. 도면 상세 정보 조회
- **메서드:** `GET`
- **경로:** `/projects/{projectId}/drawings/{drawingId}`
- **설명:** 특정 도면의 상세 정보 조회
- **Path Parameters:**
  - `projectId`: 프로젝트 ID
  - `drawingId`: 도면 ID

### 9. 도면 생성
- **메서드:** `POST`
- **경로:** `/projects/{projectId}/drawings`
- **설명:** 새로운 도면(문서) 생성
- **Path Parameters:**
  - `projectId`: 프로젝트 ID
- **Request Body:**
  ```json
  {
    "drawingName": "새 도면",
    "drawingType": "FOUNDATION",
    "description": "기초 도면"
  }
  ```

### 10. 도면 수정
- **메서드:** `PUT`
- **경로:** `/projects/{projectId}/drawings/{drawingId}`
- **설명:** 도면 정보 수정
- **Path Parameters:**
  - `projectId`: 프로젝트 ID
  - `drawingId`: 도면 ID

### 11. 도면 삭제
- **메서드:** `DELETE`
- **경로:** `/projects/{projectId}/drawings/{drawingId}`
- **설명:** 도면 삭제
- **Path Parameters:**
  - `projectId`: 프로젝트 ID
  - `drawingId`: 도면 ID

---

## 데이터베이스 조작 엔드포인트

### 12. 구조 정보 조회
- **메서드:** `GET`
- **경로:** `/projects/{projectId}/structures`
- **설명:** 프로젝트의 구조 정보 조회
- **Path Parameters:**
  - `projectId`: 프로젝트 ID

### 13. 재료 정보 조회
- **메서드:** `GET`
- **경로:** `/projects/{projectId}/materials`
- **설명:** 프로젝트의 재료 정보 조회
- **Path Parameters:**
  - `projectId`: 프로젝트 ID

### 14. 속성 정보 조회
- **메서드:** `GET`
- **경로:** `/projects/{projectId}/properties`
- **설명:** 프로젝트의 속성 정보 조회
- **Path Parameters:**
  - `projectId`: 프로젝트 ID

---

## HTTP 상태 코드

| 코드 | 설명 |
|------|------|
| 200 | 요청 성공 |
| 201 | 리소스 생성 성공 |
| 204 | 요청 성공 (응답 본문 없음) |
| 400 | 잘못된 요청 |
| 401 | 인증 실패 |
| 403 | 접근 거부 |
| 404 | 리소스 없음 |
| 500 | 서버 오류 |

---

## 에러 응답 예시

```json
{
  "error": {
    "code": "ERR_INVALID_PROJECT",
    "message": "프로젝트를 찾을 수 없습니다.",
    "details": "projectId: PROJECT_INVALID"
  }
}
```

---

## 참고 문서

- [MIDAS GATE API 공식 매뉴얼](https://support.midasuser.com/hc/ko/p/gate_api_manual)
- [MIDAS API 온라인 매뉴얼](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)
- [인증 설정](./AUTHENTICATION.md)
- [API 개요](./API-OVERVIEW.md)
