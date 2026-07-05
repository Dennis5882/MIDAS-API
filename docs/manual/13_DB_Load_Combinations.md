# 13. DB – Load Combinations / Results

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

---

## Endpoint 목록

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/db/LCOM-GEN`](#1-dblcom-gen--load-combinations--general) | 하중조합 – 일반 | POST, GET, PUT, DELETE |
| 2 | [`/db/LCOM-CONC`](#2-dblcom-conc--load-combinations--concrete-design) | 하중조합 – 콘크리트 설계 | POST, GET, PUT, DELETE |
| 3 | [`/db/LCOM-STEEL`](#3-dblcom-steel--load-combinations--steel-design) | 하중조합 – 강재 설계 | POST, GET, PUT, DELETE |
| 4 | [`/db/LCOM-SRC`](#4-dblcom-src--load-combinations--src-design) | 하중조합 – SRC 설계 | POST, GET, PUT, DELETE |
| 5 | [`/db/LCOM-STLCOMP`](#5-dblcom-stlcomp--load-combinations--composite-steel-girder-design) | 하중조합 – 강합성 거더 설계 | POST, GET, PUT, DELETE |
| 6 | [`/db/LCOM-SEISMIC`](#6-dblcom-seismic--load-combinations--seismic-design) | 하중조합 – 내진 설계 | POST, GET, PUT, DELETE |
| 7 | [`/db/CUTL`](#7-dbcutl--cutting-line) | 절단선 (Cutting Line) | POST, GET, PUT, DELETE |
| 8 | [`/db/CLWP`](#8-dbclwp--plate-cutting-line-diagram) | 판 절단선 다이어그램 | POST, GET, PUT, DELETE |

---

## 공통 개념

### `vCOMB` 배열 — ANAL 타입 값

모든 LCOM 계열 엔드포인트의 조합 항목 배열(`vCOMB`)에서 사용하는 해석 타입:

| `ANAL` 값 | 설명 |
|-----------|------|
| `"ST"` | Static Load Case (정적 하중케이스) |
| `"CS"` | Construction Stage Case (시공단계 케이스) |
| `"MV"` | Moving Load Case (이동하중 케이스) |
| `"SM"` | Settlement Case (침하 케이스) |
| `"RS"` | Response Spectrum Case (응답스펙트럼 케이스) |
| `"TH"` | Time History Case (시간이력 케이스) |
| `"CB"` | General Combination (일반 조합) |

### `iTYPE` — 합산 방식

| 값 | 방식 | LCOM-GEN | LCOM-CONC | LCOM-STEEL/SRC/STLCOMP | LCOM-SEISMIC |
|----|------|:--------:|:---------:|:----------------------:|:------------:|
| `0` | Add (가산) | ✔ | ✔ | ✔ | ✔ |
| `1` | Envelope (포락) | ✔ | ✔ | ✔ | ✔ |
| `2` | ABS (절댓값) | ✔ | ✔ | — | — |
| `3` | SRSS | ✔ | ✔ | ✔ | ✔ |

---

## 1. `/db/LCOM-GEN` — Load Combinations – General

> **기능:** 일반 하중조합 정의. 정적·이동·응답스펙트럼·시간이력·시공단계·침하 케이스를 조합하여 구조해석 결과용 하중조합을 생성합니다.

### Input URI

```
{base url}/db/LCOM-GEN
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-GEN": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber", "type": "integer" },
      "NAME":   { "description": "CombinationName",   "type": "string" },
      "ACTIVE": { "description": "ActiveType",         "type": "string" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",         "type": "integer" },
      "DESC":   { "description": "Description",        "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType",  "type": "string" },
            "LCNAME": { "description": "LoadCaseName",  "type": "string" },
            "FACTOR": { "description": "Factor",        "type": "number" }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 조합 번호 (읽기 전용) | `"NO"` | Integer | — | Read Only |
| 2 | 조합 이름 | `"NAME"` | String | — | **Required** |
| 3 | 활성 타입 · `"INACTIVE"` / `"ACTIVE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 합산 방식 · `0`=Add / `1`=Envelope / `2`=ABS / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 5 | 설명 | `"DESC"` | String | `""` | Optional |
| 6 | 결과 타입 (읽기 전용) · `false`=General / `true`=Min/Max/All | `"bCB"` | Boolean | — | Read Only |
| 7 | 조합 항목 배열 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 해석 타입 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 하중케이스명 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 계수 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "LC1",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.2D + 1.0L + 1.0RS",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad",   "FACTOR": 1.2 },
        { "ANAL": "ST", "LCNAME": "LiveLoad",   "FACTOR": 1.0 },
        { "ANAL": "RS", "LCNAME": "SeismicX",   "FACTOR": 1.0 }
      ]
    },
    "2": {
      "NO": 2,
      "NAME": "LC2",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 1,
      "DESC": "Envelope: Dead + Live",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-GEN": {
    "1": {
      "NO": 1,
      "NAME": "LC1",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.2D + 1.0L + 1.0RS",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.2 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.0 },
        { "ANAL": "RS", "LCNAME": "SeismicX", "FACTOR": 1.0 }
      ]
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 일반 하중조합 생성 ──────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "COMB_GEN_1",
            "ACTIVE": "ACTIVE",
            "bCB": False,
            "iTYPE": 0,          # 0=Add
            "DESC": "1.2D + 1.6L",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.2},
                {"ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.6}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-GEN", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 전체 조회 ─────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/LCOM-GEN", headers=HEADERS)
combos = resp.json().get("LCOM-GEN", {})
print(f"일반 하중조합 수: {len(combos)}")
for key, val in combos.items():
    print(f"  [{key}] {val['NAME']} ({val['ACTIVE']}) iTYPE={val['iTYPE']}")

# ── DELETE: 특정 조합 삭제 ─────────────────────────────────────────
resp = requests.delete(f"{BASE_URL}/db/LCOM-GEN", json={"Assign": {"1": {}}}, headers=HEADERS)
print("DELETE:", resp.status_code)
```

---

## 2. `/db/LCOM-CONC` — Load Combinations – Concrete Design

> **기능:** 콘크리트 설계용 하중조합 정의. 강도설계(Strength) / 사용성 설계(Service) 구분이 가능하며, 콘크리트 설계 전용 옵션(`bES`)이 추가됩니다.  
> **적용 제품:** MIDAS Civil NX 전용

### Input URI

```
{base url}/db/LCOM-CONC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-CONC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber",          "type": "integer" },
      "NAME":   { "description": "CombinationName",            "type": "string" },
      "ACTIVE": { "description": "ActiveType",                  "type": "string" },
      "bES":    { "description": "E (Concrete design only)",   "type": "boolean" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",                 "type": "integer" },
      "DESC":   { "description": "Description",                "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType", "type": "string" },
            "LCNAME": { "description": "LoadCaseName", "type": "string" },
            "FACTOR": { "description": "Factor",       "type": "number" }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 조합 번호 (읽기 전용) | `"NO"` | Integer | — | Read Only |
| 2 | 조합 이름 | `"NAME"` | String | — | **Required** |
| 3 | 활성 타입 · `"INACTIVE"` / `"STRENGTH"` / `"SERVICE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 콘크리트 설계 전용 옵션 (E) | `"bES"` | Boolean | `false` | Optional |
| 5 | 합산 방식 · `0`=Add / `1`=Envelope / `2`=ABS / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 6 | 설명 | `"DESC"` | String | `""` | Optional |
| 7 | 결과 타입 (읽기 전용) · `false`=General / `true`=Min/Max/All | `"bCB"` | Boolean | — | Read Only |
| 8 | 조합 항목 배열 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 해석 타입 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 하중케이스명 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 계수 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "cLCB1",
      "ACTIVE": "STRENGTH",
      "bES": false,
      "bCB": true,
      "iTYPE": 0,
      "DESC": "1.25D + 1.5L (Strength)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.25 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.5  }
      ]
    },
    "6": {
      "NO": 6,
      "NAME": "cLCB2",
      "ACTIVE": "SERVICE",
      "bES": false,
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.0D + 1.0L (Service)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-CONC": {
    "1": {
      "NO": 1,
      "NAME": "cLCB1",
      "ACTIVE": "STRENGTH",
      "bES": false,
      "bCB": true,
      "iTYPE": 0,
      "DESC": "1.25D + 1.5L (Strength)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.25 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.5  }
      ]
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 콘크리트 설계용 하중조합 생성 ──────────────────────────
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "CONC_STR_1",
            "ACTIVE": "STRENGTH",     # 강도설계
            "bES": False,
            "bCB": False,
            "iTYPE": 0,               # Add
            "DESC": "KDS 41 20:2022 강도조합",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.25},
                {"ANAL": "ST", "LCNAME": "LiveLoad",  "FACTOR": 1.8},
                {"ANAL": "RS", "LCNAME": "SeismicX",  "FACTOR": 1.0}
            ]
        },
        "2": {
            "NO": 2,
            "NAME": "CONC_SRV_1",
            "ACTIVE": "SERVICE",      # 사용성 설계
            "bES": False,
            "bCB": False,
            "iTYPE": 0,
            "DESC": "KDS 41 20:2022 사용조합",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0},
                {"ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.0}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-CONC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 조합 목록 조회 ────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/LCOM-CONC", headers=HEADERS)
for key, val in resp.json().get("LCOM-CONC", {}).items():
    print(f"  [{key}] {val['NAME']} ({val['ACTIVE']})")
```

---

## 3. `/db/LCOM-STEEL` — Load Combinations – Steel Design

> **기능:** 강재 설계용 하중조합 정의. LCOM-GEN과 구조가 동일하나 ACTIVE 타입이 STRENGTH / SERVICE로 구분되며 ABS 합산 방식은 지원하지 않습니다.

### Input URI

```
{base url}/db/LCOM-STEEL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-STEEL": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber",          "type": "integer" },
      "NAME":   { "description": "CombinationName",            "type": "string" },
      "ACTIVE": { "description": "ActiveType",                  "type": "string" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",                 "type": "integer" },
      "DESC":   { "description": "Description",                "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType", "type": "string" },
            "LCNAME": { "description": "LoadCaseName", "type": "string" },
            "FACTOR": { "description": "Factor",       "type": "number" }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 조합 번호 (읽기 전용) | `"NO"` | Integer | — | Read Only |
| 2 | 조합 이름 | `"NAME"` | String | — | **Required** |
| 3 | 활성 타입 · `"INACTIVE"` / `"STRENGTH"` / `"SERVICE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 합산 방식 · `0`=Add / `1`=Envelope / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 5 | 설명 | `"DESC"` | String | `""` | Optional |
| 6 | 결과 타입 (읽기 전용) · `false`=General / `true`=Min/Max/All | `"bCB"` | Boolean | — | Read Only |
| 7 | 조합 항목 배열 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 해석 타입 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 하중케이스명 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 계수 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "sLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": true,
      "iTYPE": 0,
      "DESC": "1.2D + 1.6L (강도)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.2 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.6 }
      ]
    },
    "2": {
      "NO": 2,
      "NAME": "sLCB2",
      "ACTIVE": "SERVICE",
      "bCB": true,
      "iTYPE": 0,
      "DESC": "1.0D + 1.0L (사용성)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-STEEL": {
    "1": {
      "NO": 1,
      "NAME": "sLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": true,
      "iTYPE": 0,
      "DESC": "1.2D + 1.6L (강도)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.2 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.6 }
      ]
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 강재 설계용 하중조합 생성 ───────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "STEEL_STR_1",
            "ACTIVE": "STRENGTH",
            "bCB": False,
            "iTYPE": 0,            # Add
            "DESC": "KDS 41 30:2022 강도조합",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.2},
                {"ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.6}
            ]
        },
        "2": {
            "NO": 2,
            "NAME": "STEEL_STR_2",
            "ACTIVE": "STRENGTH",
            "bCB": False,
            "iTYPE": 3,            # SRSS
            "DESC": "지진조합 SRSS",
            "vCOMB": [
                {"ANAL": "RS", "LCNAME": "RX", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RY", "FACTOR": 1.0}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-STEEL", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 4. `/db/LCOM-SRC` — Load Combinations – SRC Design

> **기능:** SRC(철골 콘크리트 합성) 설계용 하중조합. 구조는 LCOM-STEEL과 동일합니다.

### Input URI

```
{base url}/db/LCOM-SRC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-SRC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber",          "type": "integer" },
      "NAME":   { "description": "CombinationName",            "type": "string" },
      "ACTIVE": { "description": "ActiveType",                  "type": "string" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",                 "type": "integer" },
      "DESC":   { "description": "Description",                "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType", "type": "string" },
            "LCNAME": { "description": "LoadCaseName", "type": "string" },
            "FACTOR": { "description": "Factor",       "type": "number" }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 조합 번호 (읽기 전용) | `"NO"` | Integer | — | Read Only |
| 2 | 조합 이름 | `"NAME"` | String | — | **Required** |
| 3 | 활성 타입 · `"INACTIVE"` / `"STRENGTH"` / `"SERVICE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 합산 방식 · `0`=Add / `1`=Envelope / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 5 | 설명 | `"DESC"` | String | `""` | Optional |
| 6 | 결과 타입 (읽기 전용) | `"bCB"` | Boolean | — | Read Only |
| 7 | 조합 항목 배열 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 해석 타입 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 하중케이스명 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 계수 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "rLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.4(cD)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.4 }
      ]
    },
    "2": {
      "NO": 2,
      "NAME": "rLCB2",
      "ACTIVE": "SERVICE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "SERV:(cD)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-SRC": {
    "1": {
      "NO": 1,
      "NAME": "rLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.4(cD)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.4 }
      ]
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: SRC 설계용 하중조합 생성 ────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "SRC_STR_1",
            "ACTIVE": "STRENGTH",
            "bCB": False,
            "iTYPE": 0,
            "DESC": "AIK-SRC2K 강도조합",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.4},
                {"ANAL": "ST", "LCNAME": "LiveLoad",  "FACTOR": 1.7}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-SRC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── PUT: 특정 조합 수정 ────────────────────────────────────────────
update_payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "SRC_STR_1_UPD",
            "ACTIVE": "STRENGTH",
            "bCB": False,
            "iTYPE": 0,
            "DESC": "수정된 SRC 강도조합",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.25},
                {"ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.5}
            ]
        }
    }
}
resp = requests.put(f"{BASE_URL}/db/LCOM-SRC", json=update_payload, headers=HEADERS)
print("PUT:", resp.status_code, resp.json())
```

---

## 5. `/db/LCOM-STLCOMP` — Load Combinations – Composite Steel Girder Design

> **기능:** 강합성 거더(Composite Steel Girder) 설계용 하중조합. 구조는 LCOM-STEEL과 동일합니다.  
> **적용 제품:** MIDAS Civil NX 전용 (교량 설계)

### Input URI

```
{base url}/db/LCOM-STLCOMP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-STLCOMP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber",          "type": "integer" },
      "NAME":   { "description": "CombinationName",            "type": "string" },
      "ACTIVE": { "description": "ActiveType",                  "type": "string" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",                 "type": "integer" },
      "DESC":   { "description": "Description",                "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType", "type": "string" },
            "LCNAME": { "description": "LoadCaseName", "type": "string" },
            "FACTOR": { "description": "Factor",       "type": "number" }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 조합 번호 (읽기 전용) | `"NO"` | Integer | — | Read Only |
| 2 | 조합 이름 | `"NAME"` | String | — | **Required** |
| 3 | 활성 타입 · `"INACTIVE"` / `"STRENGTH"` / `"SERVICE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 합산 방식 · `0`=Add / `1`=Envelope / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 5 | 설명 | `"DESC"` | String | `""` | Optional |
| 6 | 결과 타입 (읽기 전용) | `"bCB"` | Boolean | — | Read Only |
| 7 | 조합 항목 배열 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 해석 타입 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 하중케이스명 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 계수 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "scLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.25D + 1.75L",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.25 },
        { "ANAL": "MV", "LCNAME": "LiveLoad", "FACTOR": 1.75 }
      ]
    },
    "2": {
      "NO": 2,
      "NAME": "scLCB2",
      "ACTIVE": "SERVICE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.0D + 1.0L",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "MV", "LCNAME": "LiveLoad", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-STLCOMP": {
    "1": {
      "NO": 1,
      "NAME": "scLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.25D + 1.75L",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.25 },
        { "ANAL": "MV", "LCNAME": "LiveLoad", "FACTOR": 1.75 }
      ]
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 강합성 거더 설계용 하중조합 생성 ────────────────────────
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "COMP_STR_1",
            "ACTIVE": "STRENGTH",
            "bCB": False,
            "iTYPE": 0,
            "DESC": "교량 강도조합 Ⅰ",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.25},
                {"ANAL": "MV", "LCNAME": "TruckLoad", "FACTOR": 1.75}
            ]
        },
        "2": {
            "NO": 2,
            "NAME": "COMP_SRV_1",
            "ACTIVE": "SERVICE",
            "bCB": False,
            "iTYPE": 0,
            "DESC": "교량 사용조합 Ⅱ",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.0},
                {"ANAL": "MV", "LCNAME": "TruckLoad", "FACTOR": 1.0}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-STLCOMP", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 강합성 거더 조합 목록 조회 ──────────────────────────────
resp = requests.get(f"{BASE_URL}/db/LCOM-STLCOMP", headers=HEADERS)
for key, val in resp.json().get("LCOM-STLCOMP", {}).items():
    print(f"  [{key}] {val['NAME']} ({val['ACTIVE']}) iTYPE={val['iTYPE']}")
```

---

## 6. `/db/LCOM-SEISMIC` — Load Combinations – Seismic Design

> **기능:** 내진 설계용 하중조합 정의. ACTIVE 타입은 LCOM-GEN과 동일(INACTIVE/ACTIVE)하며, ABS 합산 방식은 지원하지 않습니다. 응답스펙트럼 케이스를 SRSS 또는 CQC 조합에 활용합니다.

### Input URI

```
{base url}/db/LCOM-SEISMIC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-SEISMIC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber",          "type": "integer" },
      "NAME":   { "description": "CombinationName",            "type": "string" },
      "ACTIVE": { "description": "ActiveType",                  "type": "string" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",                 "type": "integer" },
      "DESC":   { "description": "Description",                "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType", "type": "string" },
            "LCNAME": { "description": "LoadCaseName", "type": "string" },
            "FACTOR": { "description": "Factor",       "type": "number" }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 조합 번호 (읽기 전용) | `"NO"` | Integer | — | Read Only |
| 2 | 조합 이름 | `"NAME"` | String | — | **Required** |
| 3 | 활성 타입 · `"INACTIVE"` / `"ACTIVE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 합산 방식 · `0`=Add / `1`=Envelope / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 5 | 설명 | `"DESC"` | String | `""` | Optional |
| 6 | 결과 타입 (읽기 전용) | `"bCB"` | Boolean | — | Read Only |
| 7 | 조합 항목 배열 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 해석 타입 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 하중케이스명 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 계수 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "S1",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.0D + 1.0RS_X",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "RS", "LCNAME": "RX",       "FACTOR": 1.0 }
      ]
    },
    "2": {
      "NO": 2,
      "NAME": "S2",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 3,
      "DESC": "SRSS: RX + RY",
      "vCOMB": [
        { "ANAL": "RS", "LCNAME": "RX", "FACTOR": 1.0 },
        { "ANAL": "RS", "LCNAME": "RY", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-SEISMIC": {
    "1": {
      "NO": 1,
      "NAME": "S1",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.0D + 1.0RS_X",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "RS", "LCNAME": "RX",       "FACTOR": 1.0 }
      ]
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 내진 설계용 하중조합 생성 ───────────────────────────────
# KDS 17:2022 기준 내진조합: 1.0D ± 1.0RS_X ± 0.3RS_Y
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "SEIS_1",
            "ACTIVE": "ACTIVE",
            "bCB": False,
            "iTYPE": 0,            # Add
            "DESC": "1.0D + 1.0RX + 0.3RY",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RX",       "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RY",       "FACTOR": 0.3}
            ]
        },
        "2": {
            "NO": 2,
            "NAME": "SEIS_2",
            "ACTIVE": "ACTIVE",
            "bCB": False,
            "iTYPE": 3,            # SRSS
            "DESC": "SRSS(RX, RY, RZ)",
            "vCOMB": [
                {"ANAL": "RS", "LCNAME": "RX", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RY", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RZ", "FACTOR": 1.0}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-SEISMIC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 내진 조합 조회 ────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/LCOM-SEISMIC", headers=HEADERS)
seismic_combos = resp.json().get("LCOM-SEISMIC", {})
print(f"내진 하중조합 수: {len(seismic_combos)}")
```

---

## 7. `/db/CUTL` — Cutting Line

> **기능:** 구조 모델의 단면력(Sectional Force) 결과를 추출하기 위한 절단선(Cutting Line)을 정의합니다. 두 점(PT1, PT2)을 지정하여 절단 방향과 위치를 설정합니다.

### Input URI

```
{base url}/db/CUTL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "CUTL": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "Name",         "type": "string"  },
      "DIR":  { "description": "Direction",    "type": "string"  },
      "PT1X": { "description": "Point1X",      "type": "number"  },
      "PT1Y": { "description": "Point1Y",      "type": "number"  },
      "PT1Z": { "description": "Point1Z",      "type": "number"  },
      "PT2X": { "description": "Point2X",      "type": "number"  },
      "PT2Y": { "description": "Point2Y",      "type": "number"  },
      "PT2Z": { "description": "Point2Z",      "type": "number"  },
      "R":    { "description": "ColorRValue",  "type": "integer" },
      "G":    { "description": "ColorGValue",  "type": "integer" },
      "B":    { "description": "ColorBValue",  "type": "integer" },
      "TYPE": { "description": "Type",         "type": "integer" }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 절단선 이름 | `"NAME"` | String | — | **Required** |
| 2 | 방향 · `"NORMAL"` = 법선 방향 / `"DIR"` = 면 내 방향 | `"DIR"` | String | — | **Required** |
| 3 | 점 1 – X 좌표 | `"PT1X"` | Number | — | **Required** |
| 4 | 점 1 – Y 좌표 | `"PT1Y"` | Number | — | **Required** |
| 5 | 점 1 – Z 좌표 | `"PT1Z"` | Number | — | **Required** |
| 6 | 점 2 – X 좌표 | `"PT2X"` | Number | — | **Required** |
| 7 | 점 2 – Y 좌표 | `"PT2Y"` | Number | — | **Required** |
| 8 | 점 2 – Z 좌표 | `"PT2Z"` | Number | — | **Required** |
| 9 | 선 색상 – 빨강(R) 값 (0–255) | `"R"` | Integer | `0` | Optional |
| 10 | 선 색상 – 초록(G) 값 (0–255) | `"G"` | Integer | `0` | Optional |
| 11 | 선 색상 – 파랑(B) 값 (0–255) | `"B"` | Integer | `0` | Optional |
| 12 | 타입 | `"TYPE"` | Integer | `0` | Optional |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NAME": "Cut-Line#1",
      "DIR":  "NORMAL",
      "PT1X": 8.95,
      "PT1Y": 11.0725,
      "PT1Z": 1.205,
      "PT2X": 8.95,
      "PT2Y": -1.0725,
      "PT2Z": 1.205,
      "R": 255,
      "G": 0,
      "B": 0,
      "TYPE": 0
    },
    "2": {
      "NAME": "Cut-Line#2",
      "DIR":  "DIR",
      "PT1X": 0.0,
      "PT1Y": 5.0,
      "PT1Z": 3.0,
      "PT2X": 10.0,
      "PT2Y": 5.0,
      "PT2Z": 3.0,
      "R": 0,
      "G": 0,
      "B": 255,
      "TYPE": 0
    }
  }
}
```

**GET Response Body**

```json
{
  "CUTL": {
    "1": {
      "NAME": "Cut-Line#1",
      "DIR":  "NORMAL",
      "PT1X": 8.95,  "PT1Y": 11.0725, "PT1Z": 1.205,
      "PT2X": 8.95,  "PT2Y": -1.0725, "PT2Z": 1.205,
      "R": 255, "G": 0, "B": 0,
      "TYPE": 0
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 절단선 생성 ──────────────────────────────────────────────
cutting_lines = {
    "1": {
        "NAME": "Section_A-A",
        "DIR":  "NORMAL",        # 법선 방향 절단
        "PT1X": 5.0,  "PT1Y": 0.0,  "PT1Z": 0.0,
        "PT2X": 5.0,  "PT2Y": 10.0, "PT2Z": 0.0,
        "R": 255, "G": 0, "B": 0,   # 빨간색
        "TYPE": 0
    },
    "2": {
        "NAME": "Section_B-B",
        "DIR":  "NORMAL",
        "PT1X": 10.0, "PT1Y": 0.0,  "PT1Z": 0.0,
        "PT2X": 10.0, "PT2Y": 10.0, "PT2Z": 0.0,
        "R": 0, "G": 128, "B": 0,   # 초록색
        "TYPE": 0
    }
}
resp = requests.post(
    f"{BASE_URL}/db/CUTL",
    json={"Assign": cutting_lines},
    headers=HEADERS
)
print("POST:", resp.status_code, resp.json())

# ── GET: 전체 절단선 조회 ──────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/CUTL", headers=HEADERS)
cutlines = resp.json().get("CUTL", {})
print(f"절단선 수: {len(cutlines)}")
for key, val in cutlines.items():
    print(f"  [{key}] {val['NAME']} DIR={val['DIR']}")
    print(f"       PT1=({val['PT1X']}, {val['PT1Y']}, {val['PT1Z']})")
    print(f"       PT2=({val['PT2X']}, {val['PT2Y']}, {val['PT2Z']})")

# ── DELETE: 절단선 삭제 ────────────────────────────────────────────
resp = requests.delete(
    f"{BASE_URL}/db/CUTL",
    json={"Assign": {"1": {}}},
    headers=HEADERS
)
print("DELETE:", resp.status_code)
```

---

## 8. `/db/CLWP` — Plate Cutting Line Diagram

> **기능:** 판(Plate) 요소에 대한 절단선 다이어그램을 정의합니다. CUTL(1D 절단선)과 달리 세 점(PT1, PT2, PT3)으로 면(Plane)을 정의하여 판 요소의 단면력을 추출합니다.

### Input URI

```
{base url}/db/CLWP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "CLWP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "Name",        "type": "string"  },
      "DIR":  { "description": "Direction",   "type": "string"  },
      "PT1X": { "description": "Point1X",     "type": "number"  },
      "PT1Y": { "description": "Point1Y",     "type": "number"  },
      "PT1Z": { "description": "Point1Z",     "type": "number"  },
      "PT2X": { "description": "Point2X",     "type": "number"  },
      "PT2Y": { "description": "Point2Y",     "type": "number"  },
      "PT2Z": { "description": "Point2Z",     "type": "number"  },
      "PT3X": { "description": "Point3X",     "type": "number"  },
      "PT3Y": { "description": "Point3Y",     "type": "number"  },
      "PT3Z": { "description": "Point3Z",     "type": "number"  },
      "R":    { "description": "ColorRValue", "type": "integer" },
      "G":    { "description": "ColorGValue", "type": "integer" },
      "B":    { "description": "ColorBValue", "type": "integer" }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 절단선 이름 | `"NAME"` | String | — | **Required** |
| 2 | 방향 · `"NORMAL"` = 법선 / `"DIR"` = 면 내 / `"PLANE"` = 평면 | `"DIR"` | String | — | **Required** |
| 3 | 점 1 – X 좌표 | `"PT1X"` | Number | — | **Required** |
| 4 | 점 1 – Y 좌표 | `"PT1Y"` | Number | — | **Required** |
| 5 | 점 1 – Z 좌표 | `"PT1Z"` | Number | — | **Required** |
| 6 | 점 2 – X 좌표 | `"PT2X"` | Number | — | **Required** |
| 7 | 점 2 – Y 좌표 | `"PT2Y"` | Number | — | **Required** |
| 8 | 점 2 – Z 좌표 | `"PT2Z"` | Number | — | **Required** |
| 9 | 점 3 – X 좌표 | `"PT3X"` | Number | — | **Required** |
| 10 | 점 3 – Y 좌표 | `"PT3Y"` | Number | — | **Required** |
| 11 | 점 3 – Z 좌표 | `"PT3Z"` | Number | — | **Required** |
| 12 | 선 색상 – 빨강(R) 값 (0–255) | `"R"` | Integer | `0` | Optional |
| 13 | 선 색상 – 초록(G) 값 (0–255) | `"G"` | Integer | `0` | Optional |
| 14 | 선 색상 – 파랑(B) 값 (0–255) | `"B"` | Integer | `0` | Optional |

> **참고 — CUTL vs CLWP 비교:**
>
> | 항목 | CUTL | CLWP |
> |------|------|------|
> | 대상 요소 | 보·트러스·링크 등 1D 요소 | 판(Plate) 요소 |
> | 점 수 | 2점 (PT1, PT2) | 3점 (PT1, PT2, PT3) |
> | DIR 값 | `NORMAL` / `DIR` | `NORMAL` / `DIR` / `PLANE` |
> | `TYPE` 필드 | 있음 | 없음 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NAME": "CL1",
      "DIR":  "PLANE",
      "PT1X": 0,
      "PT1Y": 10710,
      "PT1Z": -1000,
      "PT2X": 0,
      "PT2Y": 10710,
      "PT2Z": 0,
      "PT3X": 0,
      "PT3Y": 9945,
      "PT3Z": 0,
      "R": 0,
      "G": 0,
      "B": 0
    },
    "2": {
      "NAME": "CL2",
      "DIR":  "NORMAL",
      "PT1X": 5.0,
      "PT1Y": 0.0,
      "PT1Z": 0.0,
      "PT2X": 5.0,
      "PT2Y": 10.0,
      "PT2Z": 0.0,
      "PT3X": 5.0,
      "PT3Y": 5.0,
      "PT3Z": 3.0,
      "R": 255,
      "G": 0,
      "B": 0
    }
  }
}
```

**GET Response Body**

```json
{
  "CLWP": {
    "1": {
      "NAME": "CL1",
      "DIR":  "PLANE",
      "PT1X": 0,    "PT1Y": 10710, "PT1Z": -1000,
      "PT2X": 0,    "PT2Y": 10710, "PT2Z": 0,
      "PT3X": 0,    "PT3Y": 9945,  "PT3Z": 0,
      "R": 0, "G": 0, "B": 0
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 판 절단선 다이어그램 생성 ───────────────────────────────
# 3점으로 평면(Plane)을 정의하여 판 요소 단면력 추출 위치 설정
payload = {
    "Assign": {
        "1": {
            "NAME": "PLATE_CUT_1",
            "DIR":  "PLANE",        # 평면 절단
            "PT1X": 0.0,  "PT1Y": 10.0, "PT1Z": -2.0,
            "PT2X": 0.0,  "PT2Y": 10.0, "PT2Z":  0.0,
            "PT3X": 0.0,  "PT3Y":  8.0, "PT3Z":  0.0,
            "R": 255, "G": 165, "B": 0   # 주황색
        },
        "2": {
            "NAME": "PLATE_CUT_2",
            "DIR":  "NORMAL",       # 법선 방향 절단
            "PT1X": 5.0, "PT1Y": 0.0,  "PT1Z": 0.0,
            "PT2X": 5.0, "PT2Y": 10.0, "PT2Z": 0.0,
            "PT3X": 5.0, "PT3Y": 5.0,  "PT3Z": 3.0,
            "R": 0, "G": 0, "B": 200
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/CLWP", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 전체 판 절단선 조회 ───────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/CLWP", headers=HEADERS)
clwp_data = resp.json().get("CLWP", {})
print(f"판 절단선 수: {len(clwp_data)}")
for key, val in clwp_data.items():
    print(f"  [{key}] {val['NAME']} DIR={val['DIR']}")

# ── PUT: 절단선 위치 수정 ──────────────────────────────────────────
update = {
    "Assign": {
        "1": {
            "NAME": "PLATE_CUT_1_UPD",
            "DIR":  "PLANE",
            "PT1X": 0.0,  "PT1Y": 12.0, "PT1Z": -2.0,
            "PT2X": 0.0,  "PT2Y": 12.0, "PT2Z":  0.0,
            "PT3X": 0.0,  "PT3Y": 10.0, "PT3Z":  0.0,
            "R": 255, "G": 0, "B": 0
        }
    }
}
resp = requests.put(f"{BASE_URL}/db/CLWP", json=update, headers=HEADERS)
print("PUT:", resp.status_code, resp.json())
```

---

## End-to-End Workflow

다음은 교량 구조물 설계를 위한 하중조합 전체 설정 워크플로우입니다. 각 설계 코드에 맞는 조합을 순차적으로 정의합니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── STEP 1: 일반 하중조합 (LCOM-GEN) ──────────────────────────────
# 구조해석 결과 확인용 기본 조합
gen_payload = {
    "Assign": {
        "1": {
            "NO": 1, "NAME": "GEN_ULS_1",
            "ACTIVE": "ACTIVE", "bCB": False, "iTYPE": 0,
            "DESC": "ULS: 1.35D + 1.5L",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.35},
                {"ANAL": "MV", "LCNAME": "LiveLoad",  "FACTOR": 1.5}
            ]
        },
        "2": {
            "NO": 2, "NAME": "GEN_SLS_1",
            "ACTIVE": "ACTIVE", "bCB": False, "iTYPE": 0,
            "DESC": "SLS: 1.0D + 1.0L",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0},
                {"ANAL": "MV", "LCNAME": "LiveLoad", "FACTOR": 1.0}
            ]
        }
    }
}
r1 = requests.post(f"{BASE_URL}/db/LCOM-GEN", json=gen_payload, headers=HEADERS)
print(f"STEP1 LCOM-GEN: {r1.status_code}")

# ── STEP 2: 강합성 거더 설계 조합 (LCOM-STLCOMP) ──────────────────
stlcomp_payload = {
    "Assign": {
        "1": {
            "NO": 1, "NAME": "COMP_STR_I",
            "ACTIVE": "STRENGTH", "bCB": False, "iTYPE": 0,
            "DESC": "AASHTO Strength I",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.25},
                {"ANAL": "MV", "LCNAME": "LiveLoad",  "FACTOR": 1.75}
            ]
        },
        "2": {
            "NO": 2, "NAME": "COMP_SRV_I",
            "ACTIVE": "SERVICE", "bCB": False, "iTYPE": 0,
            "DESC": "AASHTO Service I",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0},
                {"ANAL": "MV", "LCNAME": "LiveLoad", "FACTOR": 1.0}
            ]
        }
    }
}
r2 = requests.post(f"{BASE_URL}/db/LCOM-STLCOMP", json=stlcomp_payload, headers=HEADERS)
print(f"STEP2 LCOM-STLCOMP: {r2.status_code}")

# ── STEP 3: 내진 하중조합 (LCOM-SEISMIC) ─────────────────────────
seismic_payload = {
    "Assign": {
        "1": {
            "NO": 1, "NAME": "SEIS_EQ_X",
            "ACTIVE": "ACTIVE", "bCB": False, "iTYPE": 0,
            "DESC": "1.0D + 1.0EQ_X + 0.3EQ_Y",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RX",       "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RY",       "FACTOR": 0.3}
            ]
        },
        "2": {
            "NO": 2, "NAME": "SEIS_SRSS",
            "ACTIVE": "ACTIVE", "bCB": False, "iTYPE": 3,  # SRSS
            "DESC": "SRSS(RX, RY, RZ)",
            "vCOMB": [
                {"ANAL": "RS", "LCNAME": "RX", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RY", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RZ", "FACTOR": 1.0}
            ]
        }
    }
}
r3 = requests.post(f"{BASE_URL}/db/LCOM-SEISMIC", json=seismic_payload, headers=HEADERS)
print(f"STEP3 LCOM-SEISMIC: {r3.status_code}")

# ── STEP 4: 절단선 정의 (CUTL) ────────────────────────────────────
# 교량 주경간 중앙부와 단부 2개소 절단
cutl_payload = {
    "Assign": {
        "1": {
            "NAME": "MidSpan",  "DIR": "NORMAL",
            "PT1X": 50.0, "PT1Y": 0.0,  "PT1Z": 0.0,
            "PT2X": 50.0, "PT2Y": 15.0, "PT2Z": 0.0,
            "R": 255, "G": 0, "B": 0, "TYPE": 0
        },
        "2": {
            "NAME": "QuarterSpan", "DIR": "NORMAL",
            "PT1X": 25.0, "PT1Y": 0.0,  "PT1Z": 0.0,
            "PT2X": 25.0, "PT2Y": 15.0, "PT2Z": 0.0,
            "R": 0, "G": 0, "B": 255, "TYPE": 0
        }
    }
}
r4 = requests.post(f"{BASE_URL}/db/CUTL", json=cutl_payload, headers=HEADERS)
print(f"STEP4 CUTL: {r4.status_code}")

# ── STEP 5: 판 요소 절단선 (CLWP) ────────────────────────────────
# 교량 바닥판(Deck Plate) 절단선 정의
clwp_payload = {
    "Assign": {
        "1": {
            "NAME": "DeckCut_1", "DIR": "PLANE",
            "PT1X": 50.0, "PT1Y": 0.0,  "PT1Z": -0.5,
            "PT2X": 50.0, "PT2Y": 0.0,  "PT2Z":  0.0,
            "PT3X": 50.0, "PT3Y": 15.0, "PT3Z":  0.0,
            "R": 200, "G": 50, "B": 0
        }
    }
}
r5 = requests.post(f"{BASE_URL}/db/CLWP", json=clwp_payload, headers=HEADERS)
print(f"STEP5 CLWP: {r5.status_code}")

# ── 전체 설정 확인 ─────────────────────────────────────────────────
print("\n=== 하중조합 설정 확인 ===")
endpoints = ["LCOM-GEN", "LCOM-STLCOMP", "LCOM-SEISMIC", "CUTL", "CLWP"]
for ep in endpoints:
    r = requests.get(f"{BASE_URL}/db/{ep}", headers=HEADERS)
    data = r.json().get(ep, {})
    print(f"  {ep}: {len(data)}개")
```

---

## LCOM 타입별 비교 요약

| 엔드포인트 | ACTIVE 값 | iTYPE(ABS) | 추가 필드 | 용도 |
|-----------|-----------|:-----------:|----------|------|
| `LCOM-GEN` | INACTIVE / ACTIVE | ✔(2) | — | 일반 해석 결과 |
| `LCOM-CONC` | INACTIVE / STRENGTH / SERVICE | ✔(2) | `bES` | 콘크리트 설계 |
| `LCOM-STEEL` | INACTIVE / STRENGTH / SERVICE | — | — | 강재 설계 |
| `LCOM-SRC` | INACTIVE / STRENGTH / SERVICE | — | — | SRC 합성 설계 |
| `LCOM-STLCOMP` | INACTIVE / STRENGTH / SERVICE | — | — | 강합성 거더 설계 |
| `LCOM-SEISMIC` | INACTIVE / ACTIVE | — | — | 내진 설계 |
