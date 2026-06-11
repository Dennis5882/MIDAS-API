# MIDAS API 개요

## 📌 API란?

**API (Application Programming Interface)** 는 두 프로그램이 서로 통신하기 위한 규칙 모음입니다.

### MIDAS API의 특징

- **REST API** - HTTP 프로토콜 기반의 표준 웹 API
- **JSON 형식** - 데이터를 JSON 구조로 주고받음
- **WebSocket 지원** - 실시간 양방향 통신 가능

---

## 🔑 핵심 개념

### 1. REST API (Representational State Transfer)

| 메소드 | 역할 | 예시 |
|--------|------|------|
| **GET** | 데이터 조회 | `/db/PJCF` - 프로젝트 정보 조회 |
| **POST** | 새 데이터 생성 | `/doc/NEW` - 새 프로젝트 생성 |
| **PUT** | 데이터 수정 | `/db/PJCF` - 프로젝트 정보 수정 |
| **DELETE** | 데이터 삭제 | 요소 또는 항목 삭제 |

### 2. JSON (JavaScript Object Notation)

데이터를 구조화된 형식으로 저장합니다.

```json
{
  "project_name": "My Bridge",
  "unit": "m",
  "structure_type": "Steel"
}
```

### 3. WebSocket

실시간 데이터 전송이 필요할 때 사용합니다.

```
ws://your-midas-server.com/ws
```

---

## 🌐 기본 요청/응답 구조

### 요청 (Request)

```
GET /db/PJCF HTTP/1.1
Host: your-midas-server.com
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

### 응답 (Response)

```json
{
  "status": "success",
  "code": 200,
  "data": {
    "project_name": "Bridge Project",
    "unit": "m",
    "created_at": "2026-06-11"
  }
}
```

---

## 📚 주요 엔드포인트 카테고리

### 1. **DOC** - 문서 관리

프로젝트 파일을 조작합니다.

| 엔드포인트 | 메소드 | 기능 |
|-----------|--------|------|
| `/doc/NEW` | POST | 새 프로젝트 생성 |
| `/doc/OPEN` | POST | 프로젝트 열기 |
| `/doc/CLOSE` | POST | 프로젝트 닫기 |
| `/doc/SAVE` | POST | 프로젝트 저장 |
| `/doc/EXPORT` | POST | 프로젝트 내보내기 |

### 2. **DB** - 데이터베이스 조작

프로젝트 내 데이터를 관리합니다.

| 엔드포인트 | 메소드 | 기능 |
|-----------|--------|------|
| `/db/PJCF` | GET/POST/PUT | 프로젝트 정보 |
| `/db/UNIT` | GET/POST/PUT | 단위 설정 |
| `/db/MATL` | GET/POST/PUT | 재료 속성 |
| `/db/GRUP` | GET/POST/PUT | 그룹 정보 |
| `/db/NODE` | GET/POST/PUT/DELETE | 노드 관리 |
| `/db/ELEM` | GET/POST/PUT/DELETE | 요소 관리 |

### 3. **기타 엔드포인트**

- `/view/` - 뷰 설정
- `/structure/` - 구조 형식
- `/property/` - 속성 관리

---

## 🔐 인증 방식

모든 API 요청에는 인증이 필요합니다.

```
Authorization: Bearer YOUR_API_KEY
```

또는

```
X-API-Key: YOUR_API_KEY
```

**Base URL 설정 예시:**

```
https://your-midas-server.com/api/v1
```

---

## ✅ 다음 단계

1. [인증 설정하기](./AUTHENTICATION.md) - API-KEY 설정
2. [5분 시작 가이드](./QUICK-START.md) - 첫 API 호출
3. [엔드포인트 가이드](./ENDPOINTS.md) - 전체 엔드포인트 확인

---

## 📖 참고 자료

- [MIDAS 공식 API 매뉴얼](https://support.midasuser.com/hc/ko/p/gate_api_manual)
- [REST API 개념 학습](https://en.wikipedia.org/wiki/Representational_state_transfer)
- [JSON 형식 이해](https://www.json.org/json-ko.html)
