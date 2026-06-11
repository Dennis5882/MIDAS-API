# MIDAS NX Open API 개요

## 📌 MIDAS Open API란?

MIDAS는 기존의 로컬 API가 아닌 **웹 기반 Open API**를 채택했습니다.
HTTP로 요청을 보내면 MIDAS NX 제품(Gen NX / Civil NX)의 모델 데이터를 생성·조회·수정할 수 있습니다.

### 특징

- **REST API** - HTTP 프로토콜 기반 표준 웹 API
- **JSON 전용** - 모든 데이터를 JSON으로 주고받음
- **WebSocket 연동** - 서버와 로컬 제품 간 실시간 통신
- **플랫폼/언어 독립** - Python, JavaScript, C#, VBA 등 HTTP 클라이언트라면 무엇이든

---

## 🏗️ 동작 구조 (중요)

MIDAS NX는 애플리케이션과 **직접 통신하지 않습니다.** 클라우드 서버(AWS)가 중계합니다.

```
[내 코드/앱]  ──REST(HTTP)──▶  [MIDAS 서버(AWS)]  ──WebSocket──▶  [로컬 MIDAS Gen NX]
     ▲                                                                   │
     └───────────────────────  결과(JSON)  ◀──────────────────────────────┘
```

1. 클라이언트가 서버에 REST 요청을 보냅니다. (예: `GET /db/node`)
2. 서버가 `MAPI-Key`로 대상 제품을 식별하고, WebSocket으로 연결된 Gen NX에 요청을 전달합니다.
3. Gen NX가 데이터를 서버에 보내고, 서버가 클라이언트에 응답을 되돌려줍니다.

> ⚠️ **MIDAS Gen NX(또는 Civil NX)가 실행 중**이어야 API가 동작합니다.
> 로컬 PC에서 모든 게 일어나는 것처럼 보이지만, 실제로는 서버를 경유합니다.

---

## 🔑 핵심 개념

### 1. HTTP 메서드

| 메서드 | 역할 | 예시 |
|--------|------|------|
| `POST`   | 데이터 생성 | `/db/node` - 노드 생성 |
| `PUT`    | 데이터 수정 | `/db/unit` - 단위 설정 (신규 파일의 필수 데이터는 GET/PUT만) |
| `GET`    | 데이터 조회 | `/db/node` - 노드 조회 |
| `DELETE` | 데이터 삭제 | 항목 삭제 |

### 2. 엔드포인트 분류

- **`/doc/*`** - 문서 라이프사이클 (new, open, save, close)
- **`/db/*`** - 모델 데이터 (node, elem, matl, sect, thik, stld, …)

### 3. 공통 요청 바디 형식

모든 DB 엔드포인트는 `Assign` 래퍼 안에 **항목 ID → 데이터** 형태로 전송합니다.

```json
{
  "Assign": {
    "1": { "X": 0, "Y": 0, "Z": 0 },
    "2": { "X": 0, "Y": 0, "Z": 3.2 }
  }
}
```

---

## 🌐 요청 / 응답 예시

### 요청 (Request)

```
PUT /db/unit HTTP/1.1
Host: moa-engineers.midasit.com:443
MAPI-Key: eyJhbGciOi...
Content-Type: application/json

{ "Assign": { "1": { "DIST": "M", "FORCE": "TONF" } } }
```

### 응답 (Response)

```json
{ "UNIT": { "1": { "DIST": "M", "FORCE": "TONF" } } }
```

---

## 🔐 인증

모든 요청 헤더에 `MAPI-Key`를 포함합니다.

```
MAPI-Key: YOUR_MAPI_KEY
Content-Type: application/json
```

`MAPI-Key`는 MIDAS Gen NX 앱에서 발급하며, 임시 키이므로 언제든 재발급할 수 있습니다.
자세한 내용은 [인증 설정](./AUTHENTICATION.md)을 참고하세요.

---

## ✅ 다음 단계

1. [인증 설정하기](./AUTHENTICATION.md) - MAPI-Key 발급 및 설정
2. [5분 시작 가이드](./QUICK-START.md) - 첫 모델 생성
3. [엔드포인트 가이드](./ENDPOINTS.md) - 전체 엔드포인트와 JSON 스키마

---

## 📖 참고 자료

- [MIDAS API 온라인 매뉴얼](https://support.midasuser.com/hc/en-us/articles/33016922742937-MIDAS-API-Online-Manual)
- [MIDAS CIVIL NX Open API 동작 원리](https://support.midasuser.com/hc/en-us/articles/30212837484441-How-to-work-MIDAS-CIVIL-NX-Open-API)
- [NX Open API JSON Manual](https://support.midasuser.com/hc/en-us/sections/30087500371097-JSON-Manual)
