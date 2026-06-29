# 02. DB — Project / View / Structure Endpoints

> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **공식 최종 편집:** 2025.11.04 · **이 파일 동기화:** 2026-06-29  
> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX

---

## 개요

프로젝트 기본 정보, 단위계, 구조 타입, 그룹, 뷰 색상, 스팬·층(Story) 데이터를 다루는 Endpoint들입니다.

**공통 규칙:**
- **요청 바디:** `"Assign"` 키로 시작, 번호 키(ID) → 데이터 구조
- 단위(`/db/UNIT`)·구조타입(`/db/STYP`) 등 신규 파일 필수 데이터는 **`GET` / `PUT`만 동작**
- 그 외 일반 데이터는 `POST / GET / PUT / DELETE` 모두 지원

| No. | Endpoint | 기능 | 메서드 |
|-----|----------|------|--------|
| 1 | [`/db/PJCF`](#1-dbpjcf--project-information) | Project Information | POST, GET, PUT, DELETE |
| 2 | [`/db/UNIT`](#2-dbunit--unit-system) | Unit System | **GET, PUT** |
| 3 | [`/db/STYP`](#3-dbstyp--structure-type) | Structure Type | **GET, PUT** |
| 4 | [`/db/GRUP`](#4-dbgrup--structure-group) | Structure Group | POST, GET, PUT |
| 5 | [`/db/BNGR`](#5-dbbngr--boundary-group) | Boundary Group | POST, GET, PUT |
| 6 | [`/db/LDGR`](#6-dbldgr--load-group) | Load Group | POST, GET, PUT, DELETE |
| 7 | [`/db/TDGR`](#7-dbtdgr--tendon-group) | Tendon Group | POST, GET, PUT, DELETE |
| 8 | [`/db/NPLN`](#8-dbnpln--named-plane) | Named Plane | POST, GET, PUT, DELETE |
| 9 | [`/db/CO_M`](#9-dbco_m--material-color) | Material Color | **GET, PUT** |
| 10 | [`/db/CO_S`](#10-dbco_s--section-color) | Section Color | **GET, PUT** |
| 11 | [`/db/CO_T`](#11-dbco_t--thickness-color) | Thickness Color | **GET, PUT** |
| 12 | [`/db/CO_F`](#12-dbco_f--floor-load-color) | Floor Load Color | **GET, PUT** |
| 13 | [`/db/SPAN`](#13-dbspan--span-information) | Span Information | POST, GET, PUT, DELETE |
| 14 | [`/db/STOR`](#14-dbstor--story-data) | Story Data | POST, GET, PUT, DELETE |

---

## 공통 헬퍼 함수 (Python)

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
```

---

## 1. `/db/PJCF` — Project Information

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/PJCF` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **공식 문서** | [Project Information ↗](https://support.midasuser.com/hc/en-us/articles/35801869341337) |

### JSON Schema

```json
{
  "PJCF": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "PROJECT":  { "description": "ProjectName",   "type": "string" },
      "REVISION": { "description": "RevisionInfo",  "type": "string" },
      "USER":     { "description": "User",           "type": "string" },
      "EMAIL":    { "description": "E-mail",         "type": "string" },
      "ADDRESS":  { "description": "Address",        "type": "string" },
      "TEL":      { "description": "Telephone",      "type": "string" },
      "FAX":      { "description": "Fax",            "type": "string" },
      "CLIENT":   { "description": "Client",         "type": "string" },
      "TITLE":    { "description": "Title",          "type": "string" },
      "ENGINEER": { "description": "ReviewName",     "type": "string" },
      "EDATE":    { "description": "ReviewDate",     "type": "string" },
      "CHECK1":   { "description": "ReviewName",     "type": "string" },
      "CDATE1":   { "description": "ReviewDate",     "type": "string" },
      "CHECK2":   { "description": "ReviewName",     "type": "string" },
      "CDATE2":   { "description": "ReviewDate",     "type": "string" },
      "CHECK3":   { "description": "ReviewName",     "type": "string" },
      "CDATE3":   { "description": "ReviewDate",     "type": "string" },
      "APPROVE":  { "description": "ReviewName",     "type": "string" },
      "ADATE":    { "description": "ReviewDate",     "type": "string" },
      "COMMENT":  { "description": "Comments",       "type": "string" }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "PROJECT":  "Cable",
      "REVISION": "940",
      "USER":     "LJW",
      "EMAIL":    "cle1123",
      "ADDRESS":  "MIDASIT",
      "TEL":      "031789",
      "FAX":      "031789",
      "CLIENT":   "MIDASIT",
      "TITLE":    "CableBridge",
      "ENGINEER": "A",
      "EDATE":    "23.11",
      "CHECK1":   "B",
      "CDATE1":   "24.11",
      "CHECK2":   "C",
      "CDATE2":   "24.12",
      "CHECK3":   "D",
      "CDATE3":   "24.12",
      "APPROVE":  "E",
      "ADATE":    "14.2",
      "COMMENT":  "Good"
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Project Name | `"PROJECT"` | String | - | Optional |
| 2 | Revision Info | `"REVISION"` | String | - | Optional |
| 3 | Username | `"USER"` | String | - | Optional |
| 4 | E-mail | `"EMAIL"` | String | - | Optional |
| 5 | Address | `"ADDRESS"` | String | - | Optional |
| 6 | Telephone Numbers | `"TEL"` | String | - | Optional |
| 7 | Fax Numbers | `"FAX"` | String | - | Optional |
| 8 | Client | `"CLIENT"` | String | - | Optional |
| 9 | Title | `"TITLE"` | String | - | Optional |
| 10 | Engineer (Review Name) | `"ENGINEER"` | String | - | Optional |
| 11 | Engineer Review Date | `"EDATE"` | String | - | Optional |
| 12 | Checker 1 Name | `"CHECK1"` | String | - | Optional |
| 13 | Checker 1 Date | `"CDATE1"` | String | - | Optional |
| 14 | Checker 2 Name | `"CHECK2"` | String | - | Optional |
| 15 | Checker 2 Date | `"CDATE2"` | String | - | Optional |
| 16 | Checker 3 Name | `"CHECK3"` | String | - | Optional |
| 17 | Checker 3 Date | `"CDATE3"` | String | - | Optional |
| 18 | Approver Name | `"APPROVE"` | String | - | Optional |
| 19 | Approver Date | `"ADATE"` | String | - | Optional |
| 20 | Comments | `"COMMENT"` | String | - | Optional |

### Python 예제

```python
# 프로젝트 정보 설정
result = midas_api("POST", "/db/pjcf", {
    "Assign": {
        "1": {
            "PROJECT":  "My Building Project",
            "USER":     "Dennis",
            "CLIENT":   "ABC Corp",
            "TITLE":    "10-Story RC Frame",
            "ENGINEER": "Dennis",
            "EDATE":    "2026-06-29",
            "COMMENT":  "Initial modeling"
        }
    }
})

# 프로젝트 정보 조회
result = midas_api("GET", "/db/pjcf")
print(result)
```

---

## 2. `/db/UNIT` — Unit System

> ⚠️ **신규 파일의 필수 데이터:** `GET` / `PUT`만 동작합니다.

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/UNIT` |
| **Methods** | `GET`, `PUT` |
| **공식 문서** | [Unit System ↗](https://support.midasuser.com/hc/en-us/articles/35802155483801) |

### JSON Schema

```json
{
  "UNIT": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "FORCE":  { "description": "Force",       "type": "string" },
      "DIST":   { "description": "Distance",    "type": "string" },
      "HEAT":   { "description": "Heat",        "type": "string" },
      "TEMPER": { "description": "TemperUnit",  "type": "string" }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "FORCE":  "KN",
      "DIST":   "M",
      "HEAT":   "KJ",
      "TEMPER": "C"
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Force (Mass) · `"N"` / `"KN"` / `"KGF"` / `"TONF"` / `"LBF"` / `"KIPS"` | `"FORCE"` | String | - | Optional |
| 2 | Length · `"M"` / `"CM"` / `"MM"` / `"FT"` / `"IN"` | `"DIST"` | String | - | Optional |
| 3 | Heat · `"CAL"` / `"KCAL"` / `"J"` / `"KJ"` / `"BTU"` | `"HEAT"` | String | - | Optional |
| 4 | Temperature · `"C"` (Celsius) / `"F"` (Fahrenheit) | `"TEMPER"` | String | - | Optional |

#### Force 단위 상세

| 값 | 힘 단위 | 질량 단위 |
|----|---------|----------|
| `"N"` | N | kg |
| `"KN"` | kN | ton |
| `"KGF"` | kgf | kg |
| `"TONF"` | tonf | ton |
| `"LBF"` | lbf | lb |
| `"KIPS"` | kips | kips/g |

#### Length 단위 상세

| 값 | 길이 단위 |
|----|----------|
| `"M"` | m |
| `"CM"` | cm |
| `"MM"` | mm |
| `"FT"` | ft |
| `"IN"` | in |

### Python 예제

```python
# 단위 설정 (SI: kN, m — 한국 건축구조 기준)
result = midas_api("PUT", "/db/unit", {
    "Assign": {
        "1": {
            "FORCE":  "KN",
            "DIST":   "M",
            "HEAT":   "KJ",
            "TEMPER": "C"
        }
    }
})

# 단위 설정 (tonf, m — 대만 RC 설계 기준)
result = midas_api("PUT", "/db/unit", {
    "Assign": {
        "1": {
            "FORCE":  "TONF",
            "DIST":   "M",
            "HEAT":   "KCAL",
            "TEMPER": "C"
        }
    }
})

# 현재 단위 조회
result = midas_api("GET", "/db/unit")
print(result)
```

---

## 3. `/db/STYP` — Structure Type

> ⚠️ **신규 파일의 필수 데이터:** `GET` / `PUT`만 동작합니다.

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/STYP` |
| **Methods** | `GET`, `PUT` |
| **공식 문서** | [Structure Type ↗](https://support.midasuser.com/hc/en-us/articles/35802404495257) |

### JSON Schema

```json
{
  "STYP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "STYP":        { "description": "StructureType",            "type": "integer" },
      "MASS":        { "description": "MassType",                 "type": "integer" },
      "bMASSOFFSET": { "description": "ConsiderOffset",           "type": "boolean" },
      "bSELFWEIGHT": { "description": "ConvertSelfWeight",        "type": "boolean" },
      "SMASS":       { "description": "StructureMassType",        "type": "integer" },
      "GRAV":        { "description": "Gravity",                  "type": "number"  },
      "TEMP":        { "description": "InitialTemperature",       "type": "number"  },
      "bALIGNBEAM":  { "description": "AlignTopofBeamSection",    "type": "boolean" },
      "bALIGNSLAB":  { "description": "AlignTopofSlab(Plate)",    "type": "boolean" },
      "bROTRIGID":   { "description": "ConsideringRotationalRigid","type": "boolean" }
    }
  }
}
```

### Request Examples

**기본 3-D 구조 (자중 변환 없음)**

```json
{
  "Assign": {
    "1": {
      "STYP":        0,
      "MASS":        1,
      "bMASSOFFSET": false,
      "bSELFWEIGHT": false,
      "GRAV":        9.806,
      "TEMP":        0,
      "bALIGNBEAM":  false,
      "bALIGNSLAB":  false,
      "bROTRIGID":   false
    }
  }
}
```

**3-D 구조 (자중 → 질량 변환, 회전 강체 고려)**

```json
{
  "Assign": {
    "1": {
      "STYP":        0,
      "MASS":        2,
      "bMASSOFFSET": false,
      "bSELFWEIGHT": true,
      "SMASS":       2,
      "GRAV":        9.806,
      "TEMP":        0,
      "bALIGNBEAM":  false,
      "bALIGNSLAB":  false,
      "bROTRIGID":   true
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Structure Type · `0`=3-D / `1`=X-Z Plane / `2`=Y-Z Plane / `3`=X-Y Plane / `4`=Constraint RZ | `"STYP"` | Integer | System | Optional |
| 2 | Mass Type · `1`=Lumped Mass / `2`=Consistent Mass | `"MASS"` | Integer | - | Optional |
| 3 | Consider Offset | `"bMASSOFFSET"` | Boolean | - | Optional |
| 4 | Convert Self-Weight to Mass | `"bSELFWEIGHT"` | Boolean | - | Optional |
| 5 | Structure Mass Type (자중→질량 변환 시) | `"SMASS"` | Integer | - | Optional |
| 6 | Gravity Acceleration (m/s²) | `"GRAV"` | Number | System | Optional |
| 7 | Initial Temperature | `"TEMP"` | Number | 0 | Optional |
| 8 | Align Top of Beam Section | `"bALIGNBEAM"` | Boolean | - | Optional |
| 9 | Align Top of Slab (Plate) | `"bALIGNSLAB"` | Boolean | - | Optional |
| 10 | Considering Rotational Rigid | `"bROTRIGID"` | Boolean | - | Optional |

#### Structure Type (`STYP`) 상세

| 값 | 구조 타입 |
|----|----------|
| `0` | 3-D (기본) |
| `1` | X-Z Plane |
| `2` | Y-Z Plane |
| `3` | X-Y Plane |
| `4` | Constraint RZ |

### Python 예제

```python
# 구조 타입 설정 (3-D, Lumped Mass, 자중 변환 없음)
result = midas_api("PUT", "/db/styp", {
    "Assign": {
        "1": {
            "STYP":        0,       # 3-D
            "MASS":        1,       # Lumped Mass
            "bMASSOFFSET": False,
            "bSELFWEIGHT": False,
            "GRAV":        9.806,
            "TEMP":        0,
            "bALIGNBEAM":  False,
            "bALIGNSLAB":  False,
            "bROTRIGID":   False
        }
    }
})

# 현재 구조 타입 조회
result = midas_api("GET", "/db/styp")
print(result)
```

---

## 4. `/db/GRUP` — Structure Group

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/GRUP` |
| **Methods** | `POST`, `GET`, `PUT` |
| **공식 문서** | [Structure Group ↗](https://support.midasuser.com/hc/en-us/articles/35802441712921) |

### JSON Schema

```json
{
  "GRUP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":   { "description": "GroupName",    "type": "string" },
      "P_TYPE": { "description": "PlaneType",    "type": "integer" },
      "N_LIST": {
        "description": "NodeList",
        "type": "array",
        "items": { "type": "integer" }
      },
      "E_LIST": {
        "description": "ElementList",
        "type": "array",
        "items": { "type": "integer" }
      }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "NAME":   "CENTER_",
      "P_TYPE": 0,
      "N_LIST": [1, 2, 3, 4, 5],
      "E_LIST": [1, 2, 3, 4, 5]
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Structure Group Name | `"NAME"` | String | - | **Required** |
| 2 | Plane Type | `"P_TYPE"` | Integer | 0 | Optional |
| 3 | Node List | `"N_LIST"` | Array [Integer] | - | Optional |
| 4 | Element List | `"E_LIST"` | Array [Integer] | - | Optional |

### Python 예제

```python
# 구조 그룹 생성 (노드·요소 포함)
result = midas_api("POST", "/db/grup", {
    "Assign": {
        "1": {
            "NAME":   "Column_Group",
            "P_TYPE": 0,
            "N_LIST": [1, 2, 3, 4],
            "E_LIST": [1, 2, 3, 4]
        },
        "2": {
            "NAME":   "Beam_Group",
            "P_TYPE": 0,
            "N_LIST": [5, 6, 7, 8],
            "E_LIST": [5, 6, 7, 8]
        }
    }
})

# 전체 그룹 조회
result = midas_api("GET", "/db/grup")
print(result)
```

---

## 5. `/db/BNGR` — Boundary Group

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/BNGR` |
| **Methods** | `POST`, `GET`, `PUT` |
| **공식 문서** | [Boundary Group ↗](https://support.midasuser.com/hc/en-us/articles/35804937452313) |

### JSON Schema

```json
{
  "BNGR": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":     { "description": "BoundaryGroupName", "type": "string" },
      "AUTOTYPE": { "description": "AutoType",          "type": "integer" }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": { "NAME": "fix1", "AUTOTYPE": 0 },
    "2": { "NAME": "fix2", "AUTOTYPE": 0 },
    "3": { "NAME": "fix3", "AUTOTYPE": 0 }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Boundary Group Name | `"NAME"` | String | - | **Required** |
| 2 | Auto-generated boundary groups for CR/SH in Composite Section ¹⁾ · `0`=Creep / `1`=Shrinkage | `"AUTOTYPE"` | Integer | Auto | Optional |

> ¹⁾ 합성단면(Composite Section)의 크리프(Creep)/건조수축(Shrinkage) 자동 경계 그룹

### Python 예제

```python
# 경계 그룹 생성
result = midas_api("POST", "/db/bngr", {
    "Assign": {
        "1": { "NAME": "Foundation_BG", "AUTOTYPE": 0 },
        "2": { "NAME": "Stage1_BG",     "AUTOTYPE": 0 }
    }
})
print(result)
```

---

## 6. `/db/LDGR` — Load Group

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/LDGR` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **공식 문서** | [Load Group ↗](https://support.midasuser.com/hc/en-us/articles/35804975346841) |

### JSON Schema

```json
{
  "LDGR": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "LoadGroupName", "type": "string" }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": { "NAME": "SW" },
    "2": { "NAME": "WetConcrete" }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Load Group Name | `"NAME"` | String | - | **Required** |

### Python 예제

```python
# 하중 그룹 생성
result = midas_api("POST", "/db/ldgr", {
    "Assign": {
        "1": { "NAME": "Dead_Load_Group" },
        "2": { "NAME": "Live_Load_Group" },
        "3": { "NAME": "Wind_Load_Group" }
    }
})

# 특정 하중 그룹 삭제
result = midas_api("DELETE", "/db/ldgr", {
    "Assign": { "3": {} }
})
print(result)
```

---

## 7. `/db/TDGR` — Tendon Group

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/TDGR` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **공식 문서** | [Tendon Group ↗](https://support.midasuser.com/hc/en-us/articles/35805198736793) |

### JSON Schema

```json
{
  "TDGR": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "Name", "type": "string" }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": { "NAME": "TGR1" },
    "2": { "NAME": "TGR2" }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Tendon Group Name | `"NAME"` | String | - | **Required** |

### Python 예제

```python
# 텐던 그룹 생성 (PSC 교량 등에서 사용)
result = midas_api("POST", "/db/tdgr", {
    "Assign": {
        "1": { "NAME": "Tendon_Span1" },
        "2": { "NAME": "Tendon_Span2" }
    }
})
print(result)
```

---

## 8. `/db/NPLN` — Named Plane

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/NPLN` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **공식 문서** | [Named Plane ↗](https://support.midasuser.com/hc/en-us/articles/35805287066649) |

### JSON Schema

```json
{
  "NPLN": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "PlaneName", "type": "string" },
      "TYPE": { "description": "PlaneType", "type": "integer" },
      "TOL":  { "description": "Tolerance", "type": "number" },
      "POINT": {
        "description": "Point",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ITEM": {
              "description": "PointItem",
              "type": "array",
              "items": { "type": "number" }
            }
          }
        }
      },
      "COORD": { "description": "Coord", "type": "number" }
    }
  }
}
```

### Request Example

```json
{
  "NPLN": {
    "1": {
      "NAME": "NP11",
      "TYPE": 1,
      "TOL":  1,
      "POINT": [
        { "ITEM": [0,     235,  0] },
        { "ITEM": [0,     9710, 0] },
        { "ITEM": [15250, 9710, 0] }
      ]
    },
    "2": {
      "NAME":  "NP12",
      "TYPE":  2,
      "TOL":   1,
      "COORD": -12000
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Plane Name | `"NAME"` | String | - | **Required** |
| 2 | Plane Type · `1`=3 Points / `2`=X-Y Plane / `3`=X-Z Plane / `4`=Y-Z Plane | `"TYPE"` | Integer | - | **Required** |
| 3 | Tolerance | `"TOL"` | Number | - | Optional |
| 4 | Point Data (TYPE=1 시) · 1st/2nd/3rd 점 좌표 `[X, Y, Z]` | `"POINT"[].ITEM"` | Array [Number] | - | Required (TYPE=1) |
| 5 | Coordinate (TYPE=2,3,4 시) · Z/Y/X 위치 | `"COORD"` | Number | - | Required (TYPE≠1) |

#### Plane Type 상세

| 값 | 타입 | 필요 데이터 |
|----|------|------------|
| `1` | 3 Points | `POINT` (3개 점 좌표) |
| `2` | X-Y Plane | `COORD` (Z 위치) |
| `3` | X-Z Plane | `COORD` (Y 위치) |
| `4` | Y-Z Plane | `COORD` (X 위치) |

### Python 예제

```python
# 3점으로 정의하는 평면
result = midas_api("POST", "/db/npln", {
    "NPLN": {
        "1": {
            "NAME": "FloorPlane_1F",
            "TYPE": 2,       # X-Y Plane
            "TOL":  1,
            "COORD": 0       # Z = 0 (1층 바닥)
        },
        "2": {
            "NAME": "FloorPlane_2F",
            "TYPE": 2,
            "TOL":  1,
            "COORD": 3200    # Z = 3200mm (2층 바닥)
        }
    }
})
print(result)
```

---

## 9. `/db/CO_M` — Material Color

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/CO_M` |
| **Methods** | `GET`, `PUT` |
| **공식 문서** | [Material Color ↗](https://support.midasuser.com/hc/en-us/articles/35805703171353) |

### JSON Schema

```json
{
  "CO_M": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "W_R":    { "description": "WireFrameRed",    "type": "integer" },
      "W_G":    { "description": "WireFrameGreen",  "type": "integer" },
      "W_B":    { "description": "WireFrameBlue",   "type": "integer" },
      "HF_R":   { "description": "HiddenFillRed",   "type": "integer" },
      "HF_G":   { "description": "HiddenFillGreen", "type": "integer" },
      "HF_B":   { "description": "HiddenFillBlue",  "type": "integer" },
      "HE_R":   { "description": "HiddenEdgeRed",   "type": "integer" },
      "HE_G":   { "description": "HiddenEdgeGreen", "type": "integer" },
      "HE_B":   { "description": "HiddenEdgeBlue",  "type": "integer" },
      "bBLEMD": { "description": "OpacityBoolean",  "type": "boolean" },
      "FACT":   { "description": "OpacityValue",    "type": "number"  }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "W_R": 131, "W_G": 131, "W_B": 131,
      "HF_R": 178, "HF_G": 178, "HF_B": 178,
      "HE_R": 131, "HE_G": 131, "HE_B": 131,
      "bBLEMD": false,
      "FACT": 0.5
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Wire Frame Red (0–255) | `"W_R"` | Integer | - | Optional |
| 2 | Wire Frame Green (0–255) | `"W_G"` | Integer | - | Optional |
| 3 | Wire Frame Blue (0–255) | `"W_B"` | Integer | - | Optional |
| 4 | Hidden Fill Red (0–255) | `"HF_R"` | Integer | - | Optional |
| 5 | Hidden Fill Green (0–255) | `"HF_G"` | Integer | - | Optional |
| 6 | Hidden Fill Blue (0–255) | `"HF_B"` | Integer | - | Optional |
| 7 | Hidden Edge Red (0–255) | `"HE_R"` | Integer | - | Optional |
| 8 | Hidden Edge Green (0–255) | `"HE_G"` | Integer | - | Optional |
| 9 | Hidden Edge Blue (0–255) | `"HE_B"` | Integer | - | Optional |
| 10 | Opacity Boolean | `"bBLEMD"` | Boolean | - | Optional |
| 11 | Opacity Value (0.0–1.0) | `"FACT"` | Number | - | Optional |

### Python 예제

```python
# 재료 색상 설정 (재료 ID 1번 = 회색 계열)
result = midas_api("PUT", "/db/co_m", {
    "Assign": {
        "1": {
            "W_R": 131, "W_G": 131, "W_B": 131,
            "HF_R": 178, "HF_G": 178, "HF_B": 178,
            "HE_R": 131, "HE_G": 131, "HE_B": 131,
            "bBLEMD": False,
            "FACT": 0.5
        }
    }
})
print(result)
```

---

## 10. `/db/CO_S` — Section Color

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/CO_S` |
| **Methods** | `GET`, `PUT` |
| **공식 문서** | [Section Color ↗](https://support.midasuser.com/hc/en-us/articles/35805763514393) |

### JSON Schema

```json
{
  "CO_S": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "W_R":    { "description": "WireFrameRed",    "type": "integer" },
      "W_G":    { "description": "WireFrameGreen",  "type": "integer" },
      "W_B":    { "description": "WireFrameBlue",   "type": "integer" },
      "HF_R":   { "description": "HiddenFillRed",   "type": "integer" },
      "HF_G":   { "description": "HiddenFillGreen", "type": "integer" },
      "HF_B":   { "description": "HiddenFillBlue",  "type": "integer" },
      "HE_R":   { "description": "HiddenEdgeRed",   "type": "integer" },
      "HE_G":   { "description": "HiddenEdgeGreen", "type": "integer" },
      "HE_B":   { "description": "HiddenEdgeBlue",  "type": "integer" },
      "bBLEMD": { "description": "OpacityBoolean",  "type": "boolean" },
      "FACT":   { "description": "OpacityValue",    "type": "number"  }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "2": {
      "W_R": 111, "W_G": 142, "W_B": 91,
      "HF_R": 159, "HF_G": 205, "HF_B": 131,
      "HE_R": 111, "HE_G": 142, "HE_B": 91,
      "bBLEMD": false,
      "FACT": 0.5
    }
  }
}
```

### Specifications

CO_M과 동일한 필드 구조 (키 이름 동일). Section ID별 색상 지정.

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1–9 | Wire Frame / Hidden Fill / Hidden Edge RGB (0–255) | `"W_R"` ~ `"HE_B"` | Integer | - | Optional |
| 10 | Opacity Boolean | `"bBLEMD"` | Boolean | - | Optional |
| 11 | Opacity Value (0.0–1.0) | `"FACT"` | Number | - | Optional |

### Python 예제

```python
# 단면 색상 설정 (단면 ID 2번 = 녹색 계열)
result = midas_api("PUT", "/db/co_s", {
    "Assign": {
        "2": {
            "W_R": 111, "W_G": 142, "W_B": 91,
            "HF_R": 159, "HF_G": 205, "HF_B": 131,
            "HE_R": 111, "HE_G": 142, "HE_B": 91,
            "bBLEMD": False,
            "FACT": 0.5
        }
    }
})
print(result)
```

---

## 11. `/db/CO_T` — Thickness Color

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/CO_T` |
| **Methods** | `GET`, `PUT` |
| **공식 문서** | [Thickness Color ↗](https://support.midasuser.com/hc/en-us/articles/35805833925785) |

### JSON Schema

CO_M, CO_S와 동일한 필드 구조.

```json
{
  "CO_T": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "W_R":    { "description": "WireFrameRed",    "type": "integer" },
      "W_G":    { "description": "WireFrameGreen",  "type": "integer" },
      "W_B":    { "description": "WireFrameBlue",   "type": "integer" },
      "HF_R":   { "description": "HiddenFillRed",   "type": "integer" },
      "HF_G":   { "description": "HiddenFillGreen", "type": "integer" },
      "HF_B":   { "description": "HiddenFillBlue",  "type": "integer" },
      "HE_R":   { "description": "HiddenEdgeRed",   "type": "integer" },
      "HE_G":   { "description": "HiddenEdgeGreen", "type": "integer" },
      "HE_B":   { "description": "HiddenEdgeBlue",  "type": "integer" },
      "bBLEMD": { "description": "OpacityBoolean",  "type": "boolean" },
      "FACT":   { "description": "OpacityValue",    "type": "number"  }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "W_R": 111, "W_G": 142, "W_B": 91,
      "HF_R": 159, "HF_G": 205, "HF_B": 131,
      "HE_R": 111, "HE_G": 142, "HE_B": 91,
      "bBLEMD": false,
      "FACT": 0.5
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1–9 | Wire Frame / Hidden Fill / Hidden Edge RGB (0–255) | `"W_R"` ~ `"HE_B"` | Integer | - | Optional |
| 10 | Opacity Boolean | `"bBLEMD"` | Boolean | - | Optional |
| 11 | Opacity Value (0.0–1.0) | `"FACT"` | Number | - | Optional |

### Python 예제

```python
# 두께 색상 설정 (두께 ID 1번)
result = midas_api("PUT", "/db/co_t", {
    "Assign": {
        "1": {
            "W_R": 111, "W_G": 142, "W_B": 91,
            "HF_R": 159, "HF_G": 205, "HF_B": 131,
            "HE_R": 111, "HE_G": 142, "HE_B": 91,
            "bBLEMD": False, "FACT": 0.5
        }
    }
})
print(result)
```

---

## 12. `/db/CO_F` — Floor Load Color

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/CO_F` |
| **Methods** | `GET`, `PUT` |
| **공식 문서** | [Floor Load Color ↗](https://support.midasuser.com/hc/en-us/articles/35805846236441) |

### JSON Schema

```json
{
  "CO_F": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":         { "description": "FloorLoadTypeName", "type": "string"  },
      "WF_R":         { "description": "WireFrame_Red",     "type": "integer" },
      "WF_G":         { "description": "WireFrame_Green",   "type": "integer" },
      "WF_B":         { "description": "WireFrame_Blue",    "type": "integer" },
      "HF_R":         { "description": "HiddenFill_Red",    "type": "integer" },
      "HF_G":         { "description": "HiddenFill_Green",  "type": "integer" },
      "HF_B":         { "description": "HiddenFill_Blue",   "type": "integer" },
      "HE_R":         { "description": "HiddenEdge_Red",    "type": "integer" },
      "HE_G":         { "description": "HiddenEdge_Green",  "type": "integer" },
      "HE_B":         { "description": "HiddenEdge_Blue",   "type": "integer" },
      "OPT_BLEND":    { "description": "Blending",          "type": "boolean" },
      "BLEND_FACTOR": { "description": "BlendingFactor",    "type": "number"  }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "NAME": "FL",
      "WF_R": 166, "WF_G": 202, "WF_B": 240,
      "HF_R": 166, "HF_G": 202, "HF_B": 240,
      "HE_R": 166, "HE_G": 202, "HE_B": 240,
      "OPT_BLEND":    true,
      "BLEND_FACTOR": 0.25
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Floor Load Type Name | `"NAME"` | String | - | **Required** |
| 2 | Wire Frame Red (0–255) | `"WF_R"` | Integer | - | Optional |
| 3 | Wire Frame Green (0–255) | `"WF_G"` | Integer | - | Optional |
| 4 | Wire Frame Blue (0–255) | `"WF_B"` | Integer | - | Optional |
| 5 | Hidden Fill Red (0–255) | `"HF_R"` | Integer | - | Optional |
| 6 | Hidden Fill Green (0–255) | `"HF_G"` | Integer | - | Optional |
| 7 | Hidden Fill Blue (0–255) | `"HF_B"` | Integer | - | Optional |
| 8 | Hidden Edge Red (0–255) | `"HE_R"` | Integer | - | Optional |
| 9 | Hidden Edge Green (0–255) | `"HE_G"` | Integer | - | Optional |
| 10 | Hidden Edge Blue (0–255) | `"HE_B"` | Integer | - | Optional |
| 11 | Blending | `"OPT_BLEND"` | Boolean | - | Optional |
| 12 | Blending Factor (0.0–1.0) | `"BLEND_FACTOR"` | Number | - | Optional |

### Python 예제

```python
# 바닥하중 타입 색상 설정
result = midas_api("PUT", "/db/co_f", {
    "Assign": {
        "1": {
            "NAME": "Residential_Floor",
            "WF_R": 166, "WF_G": 202, "WF_B": 240,
            "HF_R": 166, "HF_G": 202, "HF_B": 240,
            "HE_R": 166, "HE_G": 202, "HE_B": 240,
            "OPT_BLEND": True,
            "BLEND_FACTOR": 0.25
        }
    }
})
print(result)
```

---

## 13. `/db/SPAN` — Span Information

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/SPAN` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **공식 문서** | [Span Information ↗](https://support.midasuser.com/hc/en-us/articles/35805957502233) |

### JSON Schema

```json
{
  "SPAN": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":       { "description": "Name",       "type": "string"  },
      "bEXACTSPAN": { "description": "bExactSpan", "type": "boolean" },
      "DIRECTION":  { "description": "nDirection", "type": "integer" },
      "SECTTYPE":   { "description": "nSectType",  "type": "integer" },
      "SPAN_LIST":  {
        "description": "Span",
        "type": "array",
        "items": { "type": "number" }
      },
      "SPAN_BASE_ITEMS": {
        "description": "SpanBaseItems",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ELEM_KEY": { "description": "Element", "type": "integer" },
            "SUPPORT":  { "description": "Support", "type": "integer" }
          }
        }
      }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "NAME":       "s1",
      "bEXACTSPAN": true,
      "DIRECTION":  0,
      "SECTTYPE":   0,
      "SPAN_LIST":  [2.5, 5, 32.5],
      "SPAN_BASE_ITEMS": [
        { "ELEM_KEY": 1,  "SUPPORT": 1 },
        { "ELEM_KEY": 2,  "SUPPORT": 1 },
        { "ELEM_KEY": 3,  "SUPPORT": 2 },
        { "ELEM_KEY": 4,  "SUPPORT": 0 }
      ]
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Span Name | `"NAME"` | String | - | **Required** |
| 2 | Exact Span Option | `"bEXACTSPAN"` | Boolean | - | **Required** |
| 3 | Inner Direction of Multiple Girders · `0`=(-) Local y / `1`=(+) Local y / `2`=Both / `3`=None | `"DIRECTION"` | Integer | - | **Required** |
| 4 | Assign Elements · `0`=By Selection / `1`=Number | `"SECTTYPE"` | Integer | - | **Required** |
| 5 | Span List (bEXACTSPAN=true 시) | `"SPAN_LIST"` | Array [Number] | - | Required (bEXACTSPAN=true) |
| 6 | Span Base Items (bEXACTSPAN=true 시) · Element Key | `"SPAN_BASE_ITEMS"[].ELEM_KEY"` | Integer | - | Required (bEXACTSPAN=true) |
| 7 | Span Base Items · Support type · `0`=None / `1`=Start / `2`=End | `"SPAN_BASE_ITEMS"[].SUPPORT"` | Integer | - | Required (bEXACTSPAN=true) |

### Python 예제

```python
# 스팬 정보 설정 (교량 등)
result = midas_api("POST", "/db/span", {
    "Assign": {
        "1": {
            "NAME":       "Main_Span",
            "bEXACTSPAN": True,
            "DIRECTION":  0,
            "SECTTYPE":   0,
            "SPAN_LIST":  [40.0, 60.0, 40.0],
            "SPAN_BASE_ITEMS": [
                {"ELEM_KEY": 1, "SUPPORT": 1},
                {"ELEM_KEY": 5, "SUPPORT": 2},
            ]
        }
    }
})
print(result)
```

---

## 14. `/db/STOR` — Story Data

### 기본 정보

| 항목 | 값 |
|------|----|
| **Input URI** | `{base url}/db/STOR` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **공식 문서** | [Story Data ↗](https://support.midasuser.com/hc/en-us/articles/49513466793113) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "STORY_NAME":               { "description": "StoryName",                            "type": "string"  },
      "STORY_LEVEL":              { "description": "StoryLevel",                           "type": "number"  },
      "bFLOOR_DIAPHRAGM":         { "description": "FloorDiaphragm",                      "type": "boolean" },
      "WIND_FLOOR_WIDTH_X":       { "description": "WindFloorWidthX-Dir",                 "type": "number"  },
      "WIND_FLOOR_WIDTH_Y":       { "description": "WindFloorWidthY-Dir",                 "type": "number"  },
      "WIND_CENTER_X":            { "description": "WindFloorCenterXc",                   "type": "number"  },
      "WIND_CENTER_Y":            { "description": "WindFloorCenterYc",                   "type": "number"  },
      "WIND_ECCENT_X":            { "description": "WindEccentricityX-Dir",               "type": "number"  },
      "WIND_ECCENT_Y":            { "description": "WindEccentricityY-Dir",               "type": "number"  },
      "SEIS_ACC_ECCENT_X":        { "description": "SeismicAccidentalEccentricityX-Dir",  "type": "number"  },
      "SEIS_ACC_ECCENT_Y":        { "description": "SeismicAccidentalEccentricityY-Dir",  "type": "number"  },
      "SEIS_INHERENT_ECCENT_X":   { "description": "SeismicInherentEccentricityX-Dir",    "type": "number"  },
      "SEIS_INHERENT_ECCENT_Y":   { "description": "SeismicInherentEccentricityY-Dir",    "type": "number"  },
      "SEIS_TORSIONAL_AMP_FACTOR_X": { "description": "SeismicTorsionalAmpFactorX-Dir",  "type": "number"  },
      "SEIS_TORSIONAL_AMP_FACTOR_Y": { "description": "SeismicTorsionalAmpFactorY-Dir",  "type": "number"  }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "STORY_NAME":               "1F",
      "STORY_LEVEL":              0,
      "bFLOOR_DIAPHRAGM":         false,
      "WIND_FLOOR_WIDTH_X":       36,
      "WIND_FLOOR_WIDTH_Y":       27.6,
      "WIND_CENTER_X":            18,
      "WIND_CENTER_Y":            13.8,
      "WIND_ECCENT_X":            5.4,
      "WIND_ECCENT_Y":            4.14,
      "SEIS_ACC_ECCENT_X":        1.8,
      "SEIS_ACC_ECCENT_Y":        1.38,
      "SEIS_INHERENT_ECCENT_X":   0,
      "SEIS_INHERENT_ECCENT_Y":   0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "2": {
      "STORY_NAME":               "2F",
      "STORY_LEVEL":              5,
      "bFLOOR_DIAPHRAGM":         true,
      "WIND_FLOOR_WIDTH_X":       36,
      "WIND_FLOOR_WIDTH_Y":       29.1,
      "WIND_CENTER_X":            18,
      "WIND_CENTER_Y":            14.55,
      "WIND_ECCENT_X":            5.4,
      "WIND_ECCENT_Y":            4.365,
      "SEIS_ACC_ECCENT_X":        1.8,
      "SEIS_ACC_ECCENT_Y":        1.455,
      "SEIS_INHERENT_ECCENT_X":   0,
      "SEIS_INHERENT_ECCENT_Y":   0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Story Name | `"STORY_NAME"` | String | - | **Required** |
| 2 | Story Height (elevation) | `"STORY_LEVEL"` | Number | - | **Required** |
| 3 | Floor Diaphragm (강성 다이아프램 가정 여부) | `"bFLOOR_DIAPHRAGM"` | Boolean | false | **Required** |
| 4 | Wind Floor Width X-Dir (GCS Y방향 풍하중에 노출되는 X축 폭) | `"WIND_FLOOR_WIDTH_X"` | Number | - | Required |
| 5 | Wind Floor Width Y-Dir (GCS X방향 풍하중에 노출되는 Y축 폭) | `"WIND_FLOOR_WIDTH_Y"` | Number | - | Required |
| 6 | Wind Floor Center Xc | `"WIND_CENTER_X"` | Number | - | Required |
| 7 | Wind Floor Center Yc | `"WIND_CENTER_Y"` | Number | - | Required |
| 8 | Wind Eccentricity X-Dir | `"WIND_ECCENT_X"` | Number | - | Required |
| 9 | Wind Eccentricity Y-Dir | `"WIND_ECCENT_Y"` | Number | - | Required |
| 10 | Seismic Accidental Eccentricity X-Dir | `"SEIS_ACC_ECCENT_X"` | Number | - | Required |
| 11 | Seismic Accidental Eccentricity Y-Dir | `"SEIS_ACC_ECCENT_Y"` | Number | - | Required |
| 12 | Seismic Inherent Eccentricity X-Dir | `"SEIS_INHERENT_ECCENT_X"` | Number | - | Required |
| 13 | Seismic Inherent Eccentricity Y-Dir | `"SEIS_INHERENT_ECCENT_Y"` | Number | - | Required |
| 14 | Seismic Torsional Amplification Factor X-Dir | `"SEIS_TORSIONAL_AMP_FACTOR_X"` | Number | - | Required |
| 15 | Seismic Torsional Amplification Factor Y-Dir | `"SEIS_TORSIONAL_AMP_FACTOR_Y"` | Number | - | Required |

### Python 예제 — 다층 건물 층 데이터 자동 생성

```python
def create_story_data(story_heights: list, floor_width_x: float, floor_width_y: float,
                       eccentricity_ratio: float = 0.05) -> dict:
    """
    다층 건물 층 데이터를 자동 생성합니다.

    Args:
        story_heights  : 각 층의 절대 높이(elevation) 리스트. 예: [0, 4, 8, 12]
        floor_width_x  : 바닥판 X 방향 폭 (m)
        floor_width_y  : 바닥판 Y 방향 폭 (m)
        eccentricity_ratio: 편심률 (기본 5%)

    Returns:
        dict: /db/STOR에 전달할 Assign 딕셔너리
    """
    story_names = ["B1F", "1F"] + [f"{i}F" for i in range(2, len(story_heights))]
    story_names[-1] = "Roof"

    assign = {}
    for i, (name, level) in enumerate(zip(story_names, story_heights), start=1):
        eccent_x = floor_width_x * eccentricity_ratio
        eccent_y = floor_width_y * eccentricity_ratio
        assign[str(i)] = {
            "STORY_NAME":               name,
            "STORY_LEVEL":              level,
            "bFLOOR_DIAPHRAGM":         (i > 1),   # 지상층부터 강성 다이아프램 적용
            "WIND_FLOOR_WIDTH_X":       floor_width_x,
            "WIND_FLOOR_WIDTH_Y":       floor_width_y,
            "WIND_CENTER_X":            floor_width_x / 2,
            "WIND_CENTER_Y":            floor_width_y / 2,
            "WIND_ECCENT_X":            eccent_x,
            "WIND_ECCENT_Y":            eccent_y,
            "SEIS_ACC_ECCENT_X":        eccent_x * 0.333,
            "SEIS_ACC_ECCENT_Y":        eccent_y * 0.333,
            "SEIS_INHERENT_ECCENT_X":   0,
            "SEIS_INHERENT_ECCENT_Y":   0,
            "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
            "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
        }
    return assign


# 10층 건물 (층고 4m), 바닥판 36m × 27.6m
story_heights = [i * 4 for i in range(11)]  # [0, 4, 8, ..., 40]
story_heights[0] = 0  # 1F = GL

assign_data = create_story_data(
    story_heights=story_heights,
    floor_width_x=36.0,
    floor_width_y=27.6
)
result = midas_api("POST", "/db/stor", {"Assign": assign_data})
print(result)
```

---

## 전체 프로젝트 초기 설정 워크플로우

```python
import requests, os

BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

def midas_api(method, endpoint, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    res = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{res.status_code}] {method.upper()} {endpoint}")
    return res.json() if res.text else {}


# ── Step 1: 새 프로젝트 ──────────────────────────────────
midas_api("POST", "/doc/new", {"Argument": {}})

# ── Step 2: 단위 설정 (kN, m) ───────────────────────────
midas_api("PUT", "/db/unit", {
    "Assign": {"1": {"FORCE": "KN", "DIST": "M", "HEAT": "KJ", "TEMPER": "C"}}
})

# ── Step 3: 구조 타입 (3-D, Lumped Mass) ─────────────────
midas_api("PUT", "/db/styp", {
    "Assign": {"1": {
        "STYP": 0, "MASS": 1, "bMASSOFFSET": False,
        "bSELFWEIGHT": False, "GRAV": 9.806, "TEMP": 0,
        "bALIGNBEAM": False, "bALIGNSLAB": False, "bROTRIGID": False
    }}
})

# ── Step 4: 프로젝트 정보 ───────────────────────────────
midas_api("POST", "/db/pjcf", {
    "Assign": {"1": {
        "PROJECT": "10F RC Frame", "USER": "Dennis",
        "CLIENT": "ABC Corp", "TITLE": "Structural Analysis"
    }}
})

# ── Step 5: 층 데이터 (10층 @ 4m) ──────────────────────
story_names = [f"{i}F" for i in range(1, 11)] + ["Roof"]
assign = {}
for i, name in enumerate(story_names, start=1):
    assign[str(i)] = {
        "STORY_NAME": name, "STORY_LEVEL": (i - 1) * 4,
        "bFLOOR_DIAPHRAGM": (i > 1),
        "WIND_FLOOR_WIDTH_X": 36, "WIND_FLOOR_WIDTH_Y": 27.6,
        "WIND_CENTER_X": 18, "WIND_CENTER_Y": 13.8,
        "WIND_ECCENT_X": 1.8, "WIND_ECCENT_Y": 1.38,
        "SEIS_ACC_ECCENT_X": 1.8, "SEIS_ACC_ECCENT_Y": 1.38,
        "SEIS_INHERENT_ECCENT_X": 0, "SEIS_INHERENT_ECCENT_Y": 0,
        "SEIS_TORSIONAL_AMP_FACTOR_X": 1, "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    }
midas_api("POST", "/db/stor", {"Assign": assign})

# ── Step 6: 저장 ─────────────────────────────────────────
midas_api("POST", "/doc/save", {"Argument": {}})
```

---

## 관련 문서

- [INDEX.md](./INDEX.md) — 전체 Endpoint 목차
- [01_DOC.md](./01_DOC.md) — 문서 관리
- [03_DB_Node_Element.md](./03_DB_Node_Element.md) — 노드·요소
- [MIDAS API Online Manual (공식)](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)
