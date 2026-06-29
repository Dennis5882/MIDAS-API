# 01. DOC — 문서 관리 Endpoints

> **출처:** [MIDAS API Online Manual – DOC](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **공식 최종 편집:** 2025.11.04 · **이 파일 동기화:** 2026-06-29  
> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX

---

## 개요

`/doc/*` Endpoint는 MIDAS NX 파일(문서)의 생성·열기·저장·닫기·가져오기·내보내기·해석 실행을 담당합니다.

**공통 규칙:**
- **HTTP 메서드:** `POST` 전용
- **요청 바디:** `"Argument"` 키로 시작
- 바디가 비어 있는 경우 `{"Argument": {}}` 사용

| No. | Endpoint | 기능 | 바디 타입 |
|-----|----------|------|-----------|
| 1 | [`/doc/NEW`](#1-docnew--new-project) | 새 프로젝트 생성 | Empty Object |
| 2 | [`/doc/OPEN`](#2-docopen--open-project) | 프로젝트 열기 | File Path (String) |
| 3 | [`/doc/CLOSE`](#3-docclose--close-project) | 프로젝트 닫기 | Empty Object |
| 4 | [`/doc/SAVE`](#4-docsave--save) | 저장 | Empty Object |
| 5 | [`/doc/SAVEAS`](#5-docsaveas--save-as) | 다른 이름으로 저장 | File Path (String) |
| 6 | [`/doc/STAGAS`](#6-docstagas--save-current-stage-as) | 현재 스테이지를 다른 이름으로 저장 | Object |
| 7 | [`/doc/IMPORT`](#7-docimport--import-to-json) | JSON 파일 불러오기 | File Path (String) |
| 8 | [`/doc/IMPORTMXT`](#8-docimportmxt--import-to-mctmgt) | MCT/MGT 파일 불러오기 | File Path (String) |
| 9 | [`/doc/EXPORT`](#9-docexport--export-to-json) | JSON 파일로 내보내기 | File Path (String) |
| 10 | [`/doc/EXPORTMXT`](#10-docexportmxt--export-to-mctmgt) | MCT/MGT 파일로 내보내기 | File Path (String) |
| 11 | [`/doc/ANAL`](#11-docnal--perform-analysis) | 해석 실행 | Empty Object / Object |

---

## 공통 헬퍼 함수 (Python)

모든 예제 코드는 아래 헬퍼 함수를 전제로 합니다.

```python
import requests
import os

# .env 또는 환경변수에서 로드 권장
BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

def midas_api(method: str, endpoint: str, body=None):
    """
    MIDAS NX Open API 호출 헬퍼.

    Args:
        method  : HTTP 메서드 문자열 ("POST", "GET", "PUT", "DELETE")
        endpoint: API 경로 (예: "/doc/new")
        body    : 요청 바디 (dict). None이면 빈 바디 전송.

    Returns:
        dict: JSON 응답
    """
    url = BASE_URL + endpoint
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": MAPI_KEY,
    }
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}
```

---

## 1. `/doc/NEW` — New Project

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/NEW` |
| **Method** | `POST` |
| **공식 문서** | [New Project ↗](https://support.midasuser.com/hc/en-us/articles/35994078198681) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/NEW",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "object",
      "properties": {}
    }
  }
}
```

### Request Example

```json
{
  "Argument": {}
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Empty Object | - | - | - | - |

### Python 예제

```python
# 새 프로젝트 생성
result = midas_api("POST", "/doc/new", {"Argument": {}})
print(result)
```

---

## 2. `/doc/OPEN` — Open Project

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/OPEN` |
| **Method** | `POST` |
| **공식 문서** | [Open Project ↗](https://support.midasuser.com/hc/en-us/articles/35994112560793) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/OPEN",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.mcb"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Opened File Path | - | String | - | - |

### Python 예제

```python
# 기존 프로젝트 열기 (절대 경로)
file_path = r"C:\MIDAS\MyProject.mcb"
result = midas_api("POST", "/doc/open", {"Argument": file_path})
print(result)
```

---

## 3. `/doc/CLOSE` — Close Project

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/CLOSE` |
| **Method** | `POST` |
| **공식 문서** | [Close Project ↗](https://support.midasuser.com/hc/en-us/articles/35994162529305) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/CLOSE",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "object",
      "properties": {}
    }
  }
}
```

### Request Example

```json
{
  "Argument": {}
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Empty Object | - | Object | - | - |

### Python 예제

```python
# 현재 열린 프로젝트 닫기
result = midas_api("POST", "/doc/close", {"Argument": {}})
print(result)
```

---

## 4. `/doc/SAVE` — Save

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/SAVE` |
| **Method** | `POST` |
| **공식 문서** | [Save ↗](https://support.midasuser.com/hc/en-us/articles/35994210207513) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/SAVE",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "object",
      "properties": {}
    }
  }
}
```

### Request Example

```json
{
  "Argument": {}
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Empty Object | - | - | - | - |

### Python 예제

```python
# 현재 프로젝트 저장
result = midas_api("POST", "/doc/save", {"Argument": {}})
print(result)
```

---

## 5. `/doc/SAVEAS` — Save As

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/SAVEAS` |
| **Method** | `POST` |
| **공식 문서** | [Save As ↗](https://support.midasuser.com/hc/en-us/articles/35994277012377) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/SAVEAS",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.mcb"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Save File Path | - | String | - | - |

### Python 예제

```python
# 다른 경로에 다른 이름으로 저장
save_path = r"C:\MIDAS\MyProject_v2.mcb"
result = midas_api("POST", "/doc/saveas", {"Argument": save_path})
print(result)
```

---

## 6. `/doc/STAGAS` — Save Current Stage As

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/STAGAS` |
| **Method** | `POST` |
| **공식 문서** | [Save Current Stage As ↗](https://support.midasuser.com/hc/en-us/articles/50707525717401) |

### JSON Schema

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\FASE1.mcb",
    "STAGE_STEP": "Fase1"
  }
}
```

### Request Example

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\FASE1.mcb",
    "STAGE_STEP": "Fase1"
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Save File Path | `"EXPORT_PATH"` | String | - | - |
| 2 | Stage Step Name | `"STAGE_STEP"` | String | - | **Required** |

### Python 예제

```python
# 현재 시공 스테이지를 별도 파일로 저장
result = midas_api("POST", "/doc/stagas", {
    "Argument": {
        "EXPORT_PATH": r"C:\MIDAS\Stage1.mcb",  # 저장 경로 (선택)
        "STAGE_STEP": "Stage1",                  # 스테이지 이름 (필수)
    }
})
print(result)
```

---

## 7. `/doc/IMPORT` — Import to JSON

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/IMPORT` |
| **Method** | `POST` |
| **공식 문서** | [Import to Json ↗](https://support.midasuser.com/hc/en-us/articles/35994338816793) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/IMPORT",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.json"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | JSON File Path | - | String | - | - |

### Python 예제

```python
# JSON 파일을 현재 프로젝트로 불러오기
json_path = r"C:\MIDAS\ModelData.json"
result = midas_api("POST", "/doc/import", {"Argument": json_path})
print(result)
```

---

## 8. `/doc/IMPORTMXT` — Import to mct/mgt

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/IMPORTMXT` |
| **Method** | `POST` |
| **공식 문서** | [Import to mct/mgt ↗](https://support.midasuser.com/hc/en-us/articles/35994365225113) |
| **제품 제한** | Civil NX: `.mct` / Gen NX: `.mgt` |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/IMPORTMXT",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.mct"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | MCT/MGT File Path | - | String | - | - |

> ⚠️ Civil NX는 `.mct`, Gen NX는 `.mgt` 파일 형식을 사용합니다.

### Python 예제

```python
# MCT 파일 불러오기 (Civil NX)
mct_path = r"C:\MIDAS\BridgeModel.mct"
result = midas_api("POST", "/doc/importmxt", {"Argument": mct_path})
print(result)

# MGT 파일 불러오기 (Gen NX)
mgt_path = r"C:\MIDAS\BuildingModel.mgt"
result = midas_api("POST", "/doc/importmxt", {"Argument": mgt_path})
print(result)
```

---

## 9. `/doc/EXPORT` — Export to JSON

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/EXPORT` |
| **Method** | `POST` |
| **공식 문서** | [Export to Json ↗](https://support.midasuser.com/hc/en-us/articles/35994422273305) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/EXPORT",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.json"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | JSON File Path | - | String | - | - |

### Python 예제

```python
# 현재 프로젝트를 JSON 파일로 내보내기
export_path = r"C:\MIDAS\ModelExport.json"
result = midas_api("POST", "/doc/export", {"Argument": export_path})
print(result)
```

---

## 10. `/doc/EXPORTMXT` — Export to mct/mgt

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/EXPORTMXT` |
| **Method** | `POST` |
| **공식 문서** | [Export to mct/mgt ↗](https://support.midasuser.com/hc/en-us/articles/35994462805017) |
| **제품 제한** | Civil NX: `.mct` / Gen NX: `.mgt` |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/EXPORTMXT",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.mct"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | MCT/MGT File Path | - | String | - | - |

> ⚠️ Civil NX는 `.mct`, Gen NX는 `.mgt` 파일 형식을 사용합니다.

### Python 예제

```python
# MCT 파일로 내보내기 (Civil NX)
export_path = r"C:\MIDAS\BridgeExport.mct"
result = midas_api("POST", "/doc/exportmxt", {"Argument": export_path})
print(result)
```

---

## 11. `/doc/ANAL` — Perform Analysis

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/doc/ANAL` |
| **Method** | `POST` |
| **공식 문서** | [Perform Analysis ↗](https://support.midasuser.com/hc/en-us/articles/35685160815897) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/ANAL",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "object",
      "properties": {
        "TYPE": {
          "type": "string"
        }
      }
    }
  }
}
```

### Request Examples

**일반 해석 (Perform Analysis)**
```json
{}
```

**푸시오버 해석 (Pushover Analysis)**
```json
{
  "Argument": {
    "TYPE": "Pushover"
  }
}
```

### Specifications

**Perform Analysis**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Empty Object | - | - | - | - |

**Pushover Analysis**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Input Analysis Type · `"Pushover"` | `"TYPE"` | String | - | **Required** |

### Python 예제

```python
# 일반 선형/비선형 해석 실행
result = midas_api("POST", "/doc/anal", {})
print(result)

# 푸시오버 해석 실행
result = midas_api("POST", "/doc/anal", {
    "Argument": {
        "TYPE": "Pushover"
    }
})
print(result)
```

---

## 전체 워크플로우 예제

일반적인 모델링 자동화 흐름:

```python
import requests
import os

BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

def midas_api(method: str, endpoint: str, body=None):
    url = BASE_URL + endpoint
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": MAPI_KEY,
    }
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}


# ── Step 1: 새 프로젝트 생성 ──────────────────────────────
midas_api("POST", "/doc/new", {"Argument": {}})

# ── Step 2: 모델 데이터 입력 (db/* 엔드포인트 사용) ─────────
# 단위, 재료, 단면, 노드, 요소, 하중 등 설정
# (02_DB_Project_Structure.md ~ 12_DB_Load_Combinations.md 참조)

# ── Step 3: 저장 ─────────────────────────────────────────
midas_api("POST", "/doc/save", {"Argument": {}})

# ── Step 4: 해석 실행 ────────────────────────────────────
midas_api("POST", "/doc/anal", {})

# ── Step 5: 결과 확인 후 다른 이름으로 저장 ──────────────────
midas_api("POST", "/doc/saveas", {"Argument": r"C:\MIDAS\Result_v1.mcb"})

# ── Step 6: 프로젝트 닫기 (선택) ──────────────────────────
midas_api("POST", "/doc/close", {"Argument": {}})
```

---

## HTTP 상태 코드

| 코드 | 설명 | 조치 |
|------|------|------|
| `200` | 요청 성공 | - |
| `400` | 잘못된 요청 (JSON/필드 오류) | 요청 바디 확인 |
| `401` | 인증 실패 | `MAPI-Key` 헤더 값 확인 |
| `403` | 접근 거부 | 키 권한·라이선스 확인 |
| `404` | 경로 오류 | Base URL 및 Endpoint 경로 확인 |
| `500` | 서버 오류 | MIDAS Gen NX 실행 여부 확인 |

> ⚠️ **가장 흔한 오류:** MIDAS Gen NX(또는 Civil NX)가 실행되지 않은 상태에서 API 호출 시 연결 실패 또는 타임아웃 발생.

---

## 관련 문서

- [INDEX.md](./INDEX.md) — 전체 Endpoint 목차
- [02_DB_Project_Structure.md](./02_DB_Project_Structure.md) — 프로젝트·단위 설정
- [MIDAS API Online Manual (공식)](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)
