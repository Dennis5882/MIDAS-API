# 24. DB – Design (설계 입력)

> **대상 제품:** MIDAS Gen NX · MIDAS Civil NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

이 장은 설계 실행에 앞서 모델에 입력해야 하는 **설계 입력 DB**를 다룹니다. RC/강재 설계 코드, 검토용 철근 입력, 비지지 길이, 설계 부재 배정, 프레임 정의, 세장비 제한, 부재 타입 및 마크 수정, 그리고 보/기둥/벽체/가새의 철근 데이터 수정까지 총 **13개 엔드포인트**를 포함합니다.

> **참고 1 — Load Combination(설계용 하중조합):** Concrete / Steel / SRC / Composite / Seismic Design 하중조합 관련 엔드포인트는 이 장이 아니라 **13장(Load Combinations)** 에서 다룹니다. 이 장은 설계 계산에 필요한 "입력 레코드(input DB)" 를 정의하는 CRUD 엔드포인트만 설명합니다.
>
> **참고 2 — `/db/MEMB` vs `/ope/MEMB`:** 이 장의 `/db/MEMB`(5번)는 설계 부재 배정 정보를 저장·조회하는 **DB 레코드(CRUD)** 입니다. 반면 요소에 대해 부재 배정을 실제로 실행하는 **작업(operation)** 엔드포인트 `/ope/MEMB`는 **15장(OPE)** 에서 다룹니다. 두 엔드포인트는 URI가 비슷하지만 서로 다릅니다.

> **공통 규약 — `"Assign"` 래핑:** POST/PUT 요청은 항상 최상위에 `"Assign"` 객체를 두고, 그 안에서 대상 ID(요소·단면·벽체 ID 등)를 **문자열 키**로 사용하여 각 레코드를 담습니다. GET 응답은 최상위 키가 해당 엔드포인트의 스키마 이름(예: `REBB`, `LTSR`)으로 바뀌어 동일한 구조로 반환됩니다.

---

## Endpoint 목록

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/db/DCON`](#1-dbdcon--rc-design-code-rc-설계-코드) | RC 설계 코드 | POST, GET, PUT, DELETE |
| 2 | [`/db/DSTL`](#2-dbdstl--design-steel-code-강재-설계-코드) | 강재(Steel) 설계 코드 | POST, GET, PUT, DELETE |
| 3 | [`/db/RCHK`](#3-dbrchk--rebar-input-for-checking---beamcolumn-검토용-철근-입력) | 검토용 철근 입력 (Beam/Column) | POST, GET, PUT, DELETE |
| 4 | [`/db/LENG`](#4-dbleng--unbraced-length-비지지-길이) | 비지지 길이 (Unbraced Length) | POST, GET, PUT, DELETE |
| 5 | [`/db/MEMB`](#5-dbmemb--member-assignment-설계-부재-배정) | 설계 부재 배정 (Member Assignment) | POST, GET, PUT, DELETE |
| 6 | [`/db/DCTL`](#6-dbdctl--definition-of-frame-프레임-정의) | 프레임 정의 (Definition of Frame) | POST, GET, PUT, DELETE |
| 7 | [`/db/LTSR`](#7-dbltsr--limiting-slenderness-ratio-세장비-제한) | 세장비 제한 (Limiting Slenderness Ratio) | POST, GET, PUT, DELETE |
| 8 | [`/db/MBTP`](#8-dbmbtp--modify-member-type-부재-타입-수정) | 부재 타입 수정 (Modify Member Type) | POST, GET, PUT, DELETE |
| 9 | [`/db/WMAK`](#9-dbwmak--modify-wall-mark-design-벽체-마크-설계-수정) | 벽체 마크 설계 수정 (Modify Wall Mark) | POST, GET, PUT, DELETE |
| 10 | [`/db/REBB`](#10-dbrebb--modify-beam-rebar-data-보-철근-데이터-수정) | 보 철근 데이터 수정 (Modify Beam Rebar) | POST, GET, PUT, DELETE |
| 11 | [`/db/REBC`](#11-dbrebc--modify-column-rebar-data-기둥-철근-데이터-수정) | 기둥 철근 데이터 수정 (Modify Column Rebar) | **POST** |
| 12 | [`/db/REBW`](#12-dbrebw--modify-wall-rebar-data-벽체-철근-데이터-수정) | 벽체 철근 데이터 수정 (Modify Wall Rebar) | POST, GET, PUT, DELETE |
| 13 | [`/db/REBR`](#13-dbrebr--modify-brace-rebar-data-가새-철근-데이터-수정) | 가새 철근 데이터 수정 (Modify Brace Rebar) | POST, GET, PUT, DELETE |

> ⚠️ **`/db/REBC`(11번)는 POST(생성/설정)만 지원**합니다. 나머지 12개 엔드포인트는 POST · GET · PUT · DELETE 전체(CRUD)를 지원합니다.

---

## 1. `/db/DCON` — RC Design Code (RC 설계 코드)

> **기능:** RC(철근콘크리트) 부재 설계에 사용할 설계 기준(Design Code)을 지정합니다. KDS·KCI·ACI·Eurocode·AASHTO 등 다양한 국가/버전 코드를 문자열로 설정합니다.

### Input URI

```
{base url}/db/DCON
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "DCON": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "DGNCODE": { "description": "Design Code", "type": "string" }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | RC 설계 코드 이름 (아래 표의 문자열 중 하나) | `"DGNCODE"` | String | — | **Required** |

**주요 `DGNCODE` 값 (일부 발췌 — 원문 기준 총 64종):**

| Design Code | DGNCODE |
|-------------|---------|
| KDS 24 14 21 : 2021 | `"KDS 24 14 21 : 2021"` |
| KDS 41 30 : 2018 | `"KDS 41 30 : 2018"` |
| KSCE-LSD15 | `"KSCE-LSD15"` |
| KCI-USD12 | `"KCI-USD12"` |
| KCI-USD07 | `"KCI-USD07"` |
| ACI318-19 / ACI318M-19 | `"ACI318-19"` / `"ACI318M-19"` |
| ACI318-14 / ACI318M-14 | `"ACI318-14"` / `"ACI318M-14"` |
| Eurocode2-2:05 / Eurocode2:04 / Eurocode2 | `"Eurocode2-2:05"` / `"Eurocode2:04"` / `"Eurocode2"` |
| AASHTO-LRFD20(US) | `"AASHTO-LRFD20"` |
| CSA-S6-19 | `"CSA-S6-19"` |
| GB/T50010-10 | `"GB/T50010-10"` |
| IS456:2000 | `"IS456:2000"` |
| NSCP 2015 | `"NSCP 2015"` |
| AREMA-2023 | `"AREMA-2023"` |

> 위 표는 대표 값만 발췌한 것입니다. 이 외에도 KSCE-USD·AIK·BS·IRC·TWN·SNiP·SP 계열 등 다수의 코드가 지원됩니다. 정확한 문자열은 온라인 매뉴얼의 "Available Design Code" 표를 참고하세요.

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "KCI-USD12"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCON": {
    "1": {
      "DGNCODE": "KCI-USD12"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

# 1) RC 설계 코드 설정 (생성/설정)
payload = {
    "Assign": {
        "1": {"DGNCODE": "KCI-USD12"}   # RC 설계 기준
    }
}
res = requests.post(f"{BASE_URL}/db/DCON", headers=HEADERS, json=payload)
print("POST 결과:", res.status_code, res.json())

# 2) 설정된 RC 설계 코드 조회
res = requests.get(f"{BASE_URL}/db/DCON", headers=HEADERS)
print("현재 설계 코드:", res.json())

# 3) 코드 변경 (PUT) / 삭제 (DELETE)
# requests.put(f"{BASE_URL}/db/DCON", headers=HEADERS,
#              json={"Assign": {"1": {"DGNCODE": "ACI318-19"}}})
# requests.delete(f"{BASE_URL}/db/DCON", headers=HEADERS)
```

---

## 2. `/db/DSTL` — Design Steel Code (강재 설계 코드)

> **기능:** 강재(Steel) 부재 설계에 사용할 설계 기준을 지정합니다. KDS·KSSC·AISC·Eurocode3·AASHTO 등을 문자열로 설정합니다.

### Input URI

```
{base url}/db/DSTL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "DGNCODE": { "description": "Design Code", "type": "string" }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 강재 설계 코드 이름 (아래 표의 문자열 중 하나) | `"DGNCODE"` | String | — | **Required** |

**주요 `DGNCODE` 값 (일부 발췌 — 원문 기준 총 66종):**

| Design Code | DGNCODE |
|-------------|---------|
| KDS 41 30 : 2022 | `"KDS 41 30 : 2022"` |
| KDS 24 14 31 : 2018 | `"KDS 24 14 31 : 2018"` |
| KSSC-LSD16 | `"KSSC-LSD16"` |
| KSSC-ASD03 | `"KSSC-ASD03"` |
| AISC(16th)-LRFD22 / AISC(16th)-ASD22 | `"AISC(16th)-LRFD22"` / `"AISC(16th)-ASD22"` |
| AISC(15th)-LRFD16 / AISC(15th)-ASD16 | `"AISC(15th)-LRFD16"` / `"AISC(15th)-ASD16"` |
| AISC-LRFD93 / AISC-ASD89 | `"AISC-LRFD93"` / `"AISC-ASD89"` |
| Eurocode3-2:05 / Eurocode3:05 / Eurocode3 | `"Eurocode3-2:05"` / `"Eurocode3:05"` / `"Eurocode3"` |
| AASHTO-LRFD20(US) | `"AASHTO-LRFD20(US)"` |
| CSA-S6-19 | `"CSA-S6-19"` |
| GB50017-03 | `"GB50017-03"` |
| IS:800-2007 | `"IS:800-2007"` |
| SP 16.13330.2017 | `"SP 16.13330.2017"` |

> 위 표는 대표 값만 발췌한 것입니다. 이 외에도 KSCE·AIK·BS5950·JTJ·TWN·NSCP·Japan Road 계열 등 다수의 코드가 지원됩니다.

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "Eurocode3-2:05"
    }
  }
}
```

**GET Response Body**

```json
{
  "DSTL": {
    "1": {
      "DGNCODE": "Eurocode3-2:05"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

# 강재 설계 코드 설정
payload = {"Assign": {"1": {"DGNCODE": "AISC(16th)-LRFD22"}}}
res = requests.post(f"{BASE_URL}/db/DSTL", headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 조회
print("현재 강재 코드:", requests.get(f"{BASE_URL}/db/DSTL", headers=HEADERS).json())
```

---

## 3. `/db/RCHK` — Rebar Input for Checking - Beam/Column (검토용 철근 입력)

> **기능:** 설계 검토(Checking) 시 사용할 실제 배근 정보를 부재(요소)별로 입력합니다. `MEMBTYPE`에 따라 **BEAM(보)** 또는 **COLUMN(기둥)** 트리 중 하나를 채우며, 주철근 레이어·부철근(전단/비틀림/다발 철근) 정보를 상세히 담습니다.

### Input URI

```
{base url}/db/RCHK
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "RCHK": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "MEMBTYPE": { "description": "MEMBTYPE (BEAM / COLUMN)", "type": "string" },
      "ENVTYPE":  { "description": "Environment Type (crack checking)", "type": "integer" },
      "BEAM": {
        "description": "BEAM (MEMBTYPE == BEAM 일 때)",
        "type": "object",
        "properties": {
          "vMAIN": {
            "description": "Main Rebar Datas [I, M, J]",
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "SECTOR": { "type": "string" },
                "POS_TOP_LAYERS": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "LAYER":     { "type": "integer" },
                      "dD":        { "type": "number" },
                      "BAR_NUM":   { "type": "integer" },
                      "BAR_NAME1": { "type": "string" },
                      "BAR_NAME2": { "type": "string" }
                    }
                  }
                },
                "POS_BOT_LAYERS": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "LAYER":     { "type": "integer" },
                      "dD":        { "type": "number" },
                      "BAR_NUM":   { "type": "integer" },
                      "BAR_NAME1": { "type": "string" },
                      "BAR_NAME2": { "type": "string" }
                    }
                  }
                }
              }
            }
          },
          "vSUB_BAR": {
            "description": "Sub Rebar Data [I, M, J]",
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "SECTOR":          { "type": "string" },
                "dSUB_BARNUM":     { "type": "number" },
                "SUB_BARNAME":     { "type": "string" },
                "dSUB_BARDIST":    { "type": "number" },
                "dSUB_BARANGLE":   { "type": "number" },
                "bTORSIONAL_BAR":  { "type": "boolean" },
                "sTRTORBARNA":     { "type": "string" },
                "dTORBAR_SPACING": { "type": "number" },
                "bBUNDLEDBAR":     { "type": "boolean" },
                "dBUNDLEDBARNUM":  { "type": "number" },
                "LONGIBARNA":      { "type": "string" },
                "dLONGIBARNUM":    { "type": "number" }
              }
            }
          }
        }
      },
      "COLM": {
        "description": "COLM (MEMBTYPE == COLUMN 일 때)",
        "type": "object",
        "properties": {
          "vLAYER": {
            "description": "Main Rebar Layers",
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "INDEX": { "type": "integer" },
                "dDc":   { "type": "number" },
                "vPOSITION": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "POSITION":  { "type": "string" },
                      "BAR_NUM":   { "type": "integer" },
                      "BAR_NAME1": { "type": "string" },
                      "BAR_NAME2": { "type": "string" }
                    }
                  }
                }
              }
            }
          },
          "SUB_BAR": {
            "type": "object",
            "properties": {
              "SUBBAR_NAME":   { "type": "string" },
              "SUBBAR_DIST":   { "type": "number" },
              "SUBBAR_NUM":    { "type": "number" },
              "SUBBAR_NAME_Y": { "type": "string" },
              "SUBBAR_NAME_Z": { "type": "string" },
              "SUBBAR_NUM_Y":  { "type": "number" },
              "SUBBAR_NUM_Z":  { "type": "number" }
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 부재 타입 · 보: `"BEAM"` / 기둥: `"COLUMN"` | `"MEMBTYPE"` | String | — | **Required** |
| 2 | 균열 검토(노출 환경) · Class 1: `0` / Class 2: `1` | `"ENVTYPE"` | Integer | — | **Required** |

**MEMBTYPE == `"BEAM"` 일 때 — `"BEAM"` 객체**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| (1) | 종방향 철근 (구간 [I, J, M] 별 객체 배열) | `"vMAIN"` | Array[Object] | — | **Required** |
| i | 구간 · I단: `"I"` / J단: `"J"` / 중앙: `"M"` | `"SECTOR"` | String | — | **Required** |
| ii | 상단 레이어 정보¹⁾ | `"POS_TOP_LAYERS"` | Array[Object] | — | **Required** |
| iii | 하단 레이어 정보¹⁾ | `"POS_BOT_LAYERS"` | Array[Object] | — | **Required** |
| (2) | 횡방향(전단/비틀림) 철근 (구간 [I, J, M] 별) | `"vSUB_BAR"` | Array[Object] | — | **Required** |
| i | 구간 · `"I"` / `"J"` / `"M"` | `"SECTOR"` | String | — | **Required** |
| ii | 철근 개수 | `"dSUB_BARNUM"` | Integer | — | **Required** |
| iii | 철근 규격 | `"SUB_BARNAME"` | String | — | **Required** |
| iv | 철근 간격 | `"dSUB_BARDIST"` | Number | — | **Required** |
| v | 부재와의 각도 | `"dSUB_BARANGLE"` | Number | — | **Required** |
| vi | 비틀림 철근 사용 여부 | `"bTORSIONAL_BAR"` | Boolean | — | Optional |
| vii | 비틀림 철근 규격 | `"sTRTORBARNA"` | String | — | Optional |
| viii | 비틀림 철근 간격 | `"dTORBAR_SPACING"` | Number | — | Optional |
| ix | 다발철근(Bundled) 사용 여부 | `"bBUNDLEDBAR"` | Boolean | — | Optional |
| x | 다발철근 개수 | `"dBUNDLEDBARNUM"` | Number | — | Optional |
| xi | 종방향 철근 규격 | `"LONGIBARNA"` | String | — | Optional |
| xii | 종방향 철근 개수 | `"dLONGIBARNUM"` | Number | — | Optional |

> ⚠️ 2026-08-26 확인 (article id `35993850335897`): `vi`~`xii`(비틀림·다발·종방향 철근 관련
> 7개 필드)는 공식 JSON Schema에는 존재하지만 공식 Specifications 표에는 전혀 실려 있지
> 않습니다(표가 `dSUB_BARANGLE`에서 바로 `COLM` 객체로 건너뜀). Required 배열 지정도 없어
> Optional로 간주해 기재했습니다.

**MEMBTYPE == `"COLUMN"` 일 때 — `"COLM"` 객체**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| (1) | 종방향 철근 레이어 배열 | `"vLAYER"` | Array[Object] | — | **Required** |
| i | 레이어 인덱스 (1~5) | `"INDEX"` | Integer | — | **Required** |
| ii | 표면~철근중심 피복 거리 | `"dDc"` | Number | — | **Required** |
| iii | 철근 레이어(위치별)²⁾ | `"vPOSITION"` | Array[Object] | — | **Required** |
| (2) | 횡방향 철근 | `"SUB_BAR"` | Object | — | **Required** |
| i | 철근 규격 | `"SUBBAR_NAME"` | String | — | **Required** |
| ii | 철근 간격 | `"SUBBAR_DIST"` | Number | — | **Required** |
| iii | 철근 개수 | `"SUBBAR_NUM"` | Integer | — | **Required** |
| iv | Y방향 철근 규격 | `"SUBBAR_NAME_Y"` | String | — | **Required** |
| v | Z방향 철근 규격 | `"SUBBAR_NAME_Z"` | String | — | **Required** |
| vi | Y방향 철근 개수 | `"SUBBAR_NUM_Y"` | Integer | — | **Required** |
| vii | Z방향 철근 개수 | `"SUBBAR_NUM_Z"` | Integer | — | **Required** |

**¹⁾ 보 철근 레이어 (`POS_TOP_LAYERS` / `POS_BOT_LAYERS` 항목 구조)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| (1) | 레이어 번호 | `"LAYER"` | Integer | — | **Required** |
| (2) | 표면~철근중심 피복 거리 | `"dD"` | Number | — | **Required** |
| (3) | 철근 개수 | `"BAR_NUM"` | Integer | — | **Required** |
| (4) | 철근 규격 1 | `"BAR_NAME1"` | String | — | **Required** |
| (5) | 철근 규격 2 | `"BAR_NAME2"` | String | Blank | Optional |

**²⁾ 기둥 철근 레이어 (`vPOSITION` 항목 구조)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| (1) | 표면 위치 · 원형: `"P1"` / 사각형: `"P1"`, `"P2"` | `"POSITION"` | String | — | **Required** |
| (2) | 철근 개수 | `"BAR_NUM"` | Number | — | **Required** |
| (3) | 철근 규격 1 | `"BAR_NAME1"` | String | — | **Required** |
| (4) | 철근 규격 2 | `"BAR_NAME2"` | String | Blank | Optional |

### Request / Response JSON

**POST / PUT Request Body (기둥 + 보 혼합)**

```json
{
  "Assign": {
    "1": {
      "MEMBTYPE": "COLUMN",
      "ENVTYPE": 0,
      "COLM": {
        "vLAYER": [
          {
            "INDEX": 1,
            "dDc": 0.1,
            "vPOSITION": [
              { "POSITION": "P1", "BAR_NUM": 24, "BAR_NAME1": "#4", "BAR_NAME2": "" }
            ]
          },
          {
            "INDEX": 2,
            "dDc": 0.2,
            "vPOSITION": [
              { "POSITION": "P1", "BAR_NUM": 24, "BAR_NAME1": "#4", "BAR_NAME2": "" }
            ]
          }
        ],
        "SUB_BAR": {
          "SUBBAR_NAME": "#4",
          "SUBBAR_DIST": 0.1,
          "SUBBAR_NUM": 12,
          "SUBBAR_NAME_Y": "#4",
          "SUBBAR_NAME_Z": "#4",
          "SUBBAR_NUM_Y": 12,
          "SUBBAR_NUM_Z": 12
        }
      }
    },
    "2": {
      "MEMBTYPE": "BEAM",
      "ENVTYPE": 1,
      "BEAM": {
        "vMAIN": [
          {
            "SECTOR": "I",
            "POS_TOP_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#5", "BAR_NAME2": "" }
            ],
            "POS_BOT_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#7", "BAR_NAME2": "" }
            ]
          },
          {
            "SECTOR": "M",
            "POS_TOP_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#5", "BAR_NAME2": "" }
            ],
            "POS_BOT_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#7", "BAR_NAME2": "" }
            ]
          },
          {
            "SECTOR": "J",
            "POS_TOP_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#5", "BAR_NAME2": "" }
            ],
            "POS_BOT_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#7", "BAR_NAME2": "" }
            ]
          }
        ],
        "vSUB_BAR": [
          { "SECTOR": "I", "dSUB_BARNUM": 2, "SUB_BARNAME": "#6", "dSUB_BARDIST": 0.1, "dSUB_BARANGLE": 90 },
          { "SECTOR": "M", "dSUB_BARNUM": 2, "SUB_BARNAME": "#6", "dSUB_BARDIST": 0.1, "dSUB_BARANGLE": 90 },
          { "SECTOR": "J", "dSUB_BARNUM": 2, "SUB_BARNAME": "#6", "dSUB_BARDIST": 0.1, "dSUB_BARANGLE": 90 }
        ]
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "RCHK": {
    "1": {
      "MEMBTYPE": "COLUMN",
      "ENVTYPE": 0,
      "COLM": {
        "vLAYER": [
          {
            "INDEX": 1,
            "dDc": 0.1,
            "vPOSITION": [
              { "POSITION": "P1", "BAR_NUM": 24, "BAR_NAME1": "#4", "BAR_NAME2": "" }
            ]
          }
        ],
        "SUB_BAR": {
          "SUBBAR_NAME": "#4",
          "SUBBAR_DIST": 0.1,
          "SUBBAR_NUM": 12,
          "SUBBAR_NAME_Y": "#4",
          "SUBBAR_NAME_Z": "#4",
          "SUBBAR_NUM_Y": 12,
          "SUBBAR_NUM_Z": 12
        }
      }
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

# 요소 2(보)에 검토용 철근 입력
beam_rebar = {
    "Assign": {
        "2": {
            "MEMBTYPE": "BEAM",
            "ENVTYPE": 1,
            "BEAM": {
                "vMAIN": [
                    {
                        "SECTOR": "I",
                        "POS_TOP_LAYERS": [
                            {"LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#5", "BAR_NAME2": ""}
                        ],
                        "POS_BOT_LAYERS": [
                            {"LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#7", "BAR_NAME2": ""}
                        ],
                    }
                ],
                "vSUB_BAR": [
                    {"SECTOR": "I", "dSUB_BARNUM": 2, "SUB_BARNAME": "#6",
                     "dSUB_BARDIST": 0.1, "dSUB_BARANGLE": 90}
                ],
            },
        }
    }
}
res = requests.post(f"{BASE_URL}/db/RCHK", headers=HEADERS, json=beam_rebar)
print("POST:", res.status_code)

# 조회
print(requests.get(f"{BASE_URL}/db/RCHK", headers=HEADERS).json())
```

---

## 4. `/db/LENG` — Unbraced Length (비지지 길이)

> **기능:** 부재의 좌굴 검토에 사용할 비지지 길이(Unbraced Length)를 요소별로 입력합니다. 강축/약축(Ly, Lz), 횡비틀림 좌굴 길이(Lb, Lt)를 지정하거나 코드에 의한 자동 계산을 설정할 수 있습니다.

### Input URI

```
{base url}/db/LENG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "LY":        { "description": "Unbraced Length Ly", "type": "number" },
      "LZ":        { "description": "Unbraced Length Lz", "type": "number" },
      "LB":        { "description": "Laterally Unbraced Length", "type": "number" },
      "bNOTUSE":   { "description": "Do not consider", "type": "boolean" },
      "bAUTOCALC": { "description": "Calculate by Code", "type": "boolean" },
      "LT":        { "description": "Torsional Unbraced Length", "type": "number" }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 비지지 길이 Ly (강축) | `"LY"` | Number | `0` | Optional |
| 2 | 비지지 길이 Lz (약축) | `"LZ"` | Number | `0` | Optional |
| 3 | 횡방향 비지지 길이 Lb | `"LB"` | Number | `0` | Optional |
| 4 | 횡방향 비지지 길이 미고려 | `"bNOTUSE"` | Boolean | `false` | Optional |
| 5 | 코드에 의한 자동 계산 | `"bAUTOCALC"` | Boolean | `false` | Optional |
| 6 | 비틀림 비지지 길이 Lt | `"LT"` | Number | `0` | Optional |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "21": {
      "LY": 9.464111,
      "LZ": 4,
      "LB": 4,
      "bNOTUSE": false,
      "bAUTOCALC": false,
      "LT": 9.464111
    }
  }
}
```

**GET Response Body**

```json
{
  "LENG": {
    "21": {
      "LY": 9.464111,
      "LZ": 4,
      "LB": 4,
      "bNOTUSE": false,
      "bAUTOCALC": false,
      "LT": 9.464111
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

# 요소 21에 비지지 길이 지정
payload = {
    "Assign": {
        "21": {"LY": 9.464111, "LZ": 4, "LB": 4,
               "bNOTUSE": False, "bAUTOCALC": False, "LT": 9.464111}
    }
}
res = requests.post(f"{BASE_URL}/db/LENG", headers=HEADERS, json=payload)
print("POST:", res.status_code)

# 조회 / 삭제
print(requests.get(f"{BASE_URL}/db/LENG", headers=HEADERS).json())
# requests.delete(f"{BASE_URL}/db/LENG", headers=HEADERS)
```

---

## 5. `/db/MEMB` — Member Assignment (설계 부재 배정)

> **기능:** 여러 요소를 하나의 설계 부재(Design Member)로 묶어 배정합니다. `AELEM`에 요소 번호 배열을 넣고, 필요 시 국부좌표 방향을 반전(`bREVERSE`)합니다.
>
> ⚠️ 이것은 **DB 레코드(CRUD)** 입니다. 배정을 실제로 실행하는 작업 엔드포인트 `/ope/MEMB`(15장)와 혼동하지 마세요.

### Input URI

```
{base url}/db/MEMB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "AELEM": {
        "description": "Element Lists",
        "type": "array",
        "items": { "type": "integer" }
      },
      "bREVERSE": {
        "description": "Reverse Local Direction",
        "type": "boolean"
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 설계 부재로 묶을 요소 번호 목록 | `"AELEM"` | Array[Integer] | — | **Required** |
| 2 | 국부좌표 방향 반전 | `"bREVERSE"` | Boolean | `false` | Optional |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "AELEM": [36, 48, 46, 49, 47]
    },
    "2": {
      "AELEM": [32, 43],
      "bREVERSE": true
    }
  }
}
```

**GET Response Body**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [36, 48, 46, 49, 47],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [32, 43],
      "bREVERSE": true
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

# 설계 부재 배정 (2개 부재)
payload = {
    "Assign": {
        "1": {"AELEM": [36, 48, 46, 49, 47]},
        "2": {"AELEM": [32, 43], "bREVERSE": True},
    }
}
res = requests.post(f"{BASE_URL}/db/MEMB", headers=HEADERS, json=payload)
print("POST:", res.status_code)

# 조회
print(requests.get(f"{BASE_URL}/db/MEMB", headers=HEADERS).json())
```

---

## 6. `/db/DCTL` — Definition of Frame (프레임 정의)

> **기능:** 설계 시 프레임의 좌굴 거동(횡구속/비횡구속) 및 유효좌굴길이계수(K) 자동 계산 여부, 설계 평면(Design Type)을 정의합니다.

### Input URI

```
{base url}/db/DCTL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "FRAMEX": { "description": "X-Direction of Frame", "type": "string" },
      "FRAMEY": { "description": "Y-Direction of Frame", "type": "string" },
      "bAUTOKF": { "description": "Auto Calculate Effective Length Factor", "type": "boolean" },
      "DT": { "description": "Design Type", "type": "string" }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 프레임 X방향 · 비횡구속·Sway: `"Unbraced Sway"` / 횡구속·Non-sway: `"Braced Non-sway"` | `"FRAMEX"` | String | `"Braced Non-sway"` | Optional |
| 2 | 프레임 Y방향 · `"Unbraced Sway"` / `"Braced Non-sway"` | `"FRAMEY"` | String | `"Braced Non-sway"` | Optional |
| 3 | 유효좌굴길이계수 자동 계산 | `"bAUTOKF"` | Boolean | `false` | Optional |
| 4 | 설계 타입 · 3-D: `"3D"` / X-Z 평면: `"XZ"` / Y-Z 평면: `"YZ"` / X-Y 평면: `"XY"` | `"DT"` | String | `"3D"` | Optional |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": false,
      "DT": "XY"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCTL": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": false,
      "DT": "XY"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "1": {
            "FRAMEX": "Braced Non-sway",
            "FRAMEY": "Unbraced Sway",
            "bAUTOKF": True,
            "DT": "3D",
        }
    }
}
res = requests.post(f"{BASE_URL}/db/DCTL", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/DCTL", headers=HEADERS).json())
```

---

## 7. `/db/LTSR` — Limiting Slenderness Ratio (세장비 제한)

> **기능:** 부재의 압축/인장 한계 세장비(Limiting Slenderness Ratio)를 요소별로 지정하거나 검토를 생략(`bNOTCHECK`)합니다.

### Input URI

```
{base url}/db/LTSR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "bNOTCHECK": { "description": "Do not check", "type": "boolean" },
      "COMP": { "description": "Compression", "type": "number" },
      "TENS": { "description": "Tension", "type": "number" }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 세장비 검토 생략 | `"bNOTCHECK"` | Boolean | `false` | Optional |
| 2 | 압축 한계 세장비 | `"COMP"` | Number | — | **Required** |
| 3 | 인장 한계 세장비 | `"TENS"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

> 원문 예제는 최상위 키를 `"LTSR"`로 사용했으나, 이 장의 공통 규약(및 다른 엔드포인트)과 동일하게 `"Assign"` 래핑을 사용하는 것을 권장합니다. 아래는 `"Assign"` 형식으로 정리한 예입니다.

```json
{
  "Assign": {
    "602": { "bNOTCHECK": false, "COMP": 150, "TENS": 400 },
    "651": { "bNOTCHECK": false, "COMP": 200, "TENS": 300 },
    "734": { "bNOTCHECK": false, "COMP": 200, "TENS": 300 }
  }
}
```

**GET Response Body**

```json
{
  "LTSR": {
    "602": { "bNOTCHECK": false, "COMP": 150, "TENS": 400 },
    "651": { "bNOTCHECK": false, "COMP": 200, "TENS": 300 },
    "734": { "bNOTCHECK": false, "COMP": 200, "TENS": 300 }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "602": {"bNOTCHECK": False, "COMP": 150, "TENS": 400},
        "651": {"bNOTCHECK": False, "COMP": 200, "TENS": 300},
    }
}
res = requests.post(f"{BASE_URL}/db/LTSR", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/LTSR", headers=HEADERS).json())
```

---

## 8. `/db/MBTP` — Modify Member Type (부재 타입 수정)

> **기능:** 요소의 설계 부재 타입(Column / Beam / Brace)을 지정·변경합니다.

### Input URI

```
{base url}/db/MBTP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "Argument": {
      "type": "object",
      "properties": {
        "TYPE": { "description": "Member Type", "type": "string" }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 부재 타입 · 기둥: `"COLUMN"` / 보: `"BEAM"` / 가새: `"BRACE"` | `"TYPE"` | String | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "160": { "TYPE": "COLUMN" },
    "174": { "TYPE": "COLUMN" },
    "188": { "TYPE": "BEAM" },
    "306": { "TYPE": "BEAM" },
    "376": { "TYPE": "BRACE" },
    "377": { "TYPE": "BRACE" }
  }
}
```

**GET Response Body**

```json
{
  "MBTP": {
    "160": { "TYPE": "COLUMN" },
    "188": { "TYPE": "BEAM" },
    "376": { "TYPE": "BRACE" }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "160": {"TYPE": "COLUMN"},
        "188": {"TYPE": "BEAM"},
        "376": {"TYPE": "BRACE"},
    }
}
res = requests.post(f"{BASE_URL}/db/MBTP", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/MBTP", headers=HEADERS).json())
```

---

## 9. `/db/WMAK` — Modify Wall Mark Design (벽체 마크 설계 수정)

> **기능:** 설계용 벽체 마크(Wall Mark)를 정의합니다. 마크 이름과 해당 마크에 속하는 벽체 ID 목록을 지정합니다.

### Input URI

```
{base url}/db/WMAK
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "WMAK": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "MARKNAME": { "description": "Wall Mark Name", "type": "string" },
      "WID_LIST": {
        "description": "Wall ID List",
        "type": "array",
        "items": { "type": "integer" }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 벽체 마크 이름 | `"MARKNAME"` | String | — | **Required** |
| 2 | 벽체 ID 목록 | `"WID_LIST"` | Array[Integer] | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": { "MARKNAME": "W1", "WID_LIST": [1, 5, 8] },
    "2": { "MARKNAME": "W2", "WID_LIST": [2, 3, 4, 6, 7] },
    "3": { "MARKNAME": "W3", "WID_LIST": [9, 10, 11] }
  }
}
```

**GET Response Body**

```json
{
  "WMAK": {
    "1": { "MARKNAME": "W1", "WID_LIST": [1, 5, 8] },
    "2": { "MARKNAME": "W2", "WID_LIST": [2, 3, 4, 6, 7] }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "1": {"MARKNAME": "W1", "WID_LIST": [1, 5, 8]},
        "2": {"MARKNAME": "W2", "WID_LIST": [2, 3, 4, 6, 7]},
    }
}
res = requests.post(f"{BASE_URL}/db/WMAK", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/WMAK", headers=HEADERS).json())
```

---

## 10. `/db/REBB` — Modify Beam Rebar Data (보 철근 데이터 수정)

> **기능:** 단면(section) 번호별로 콘크리트 보의 철근 데이터를 수정합니다. 각 `ITEMS` 항목은 I·M·J 세 구간(`BAR_SECTOR_I/M/J`)의 상·하단 주철근, 스터럽(전단철근), 표피철근(skin bar) 정보와 피복 거리(`MAIN_BAR_DC_*`)를 포함합니다.

### Input URI

```
{base url}/db/REBB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 실제 스키마는 각 철근 규격 `NAME`에 대해 `D4`~`D57` enum 목록이 반복되어 매우 큽니다. 아래는 의미 있는 구조를 요약한 스키마입니다(규격 enum은 `D4`~`D57`로 축약).

```json
{
  "type": "object",
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "키는 단면 번호 문자열 (예: \"211\")",
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "object",
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "default": false },
                  "ID": { "type": "integer", "description": "Sub Section ID (read only)" },
                  "BAR_SECTOR_I": { "type": "object", "description": "I단 구간 철근" },
                  "BAR_SECTOR_M": { "type": "object", "description": "중앙(M) 구간 철근" },
                  "BAR_SECTOR_J": { "type": "object", "description": "J단 구간 철근" },
                  "MAIN_BAR_DC_TOP": { "type": "number", "description": "상단 피복 dT" },
                  "MAIN_BAR_DC_BOT": { "type": "number", "description": "하단 피복 dB" },
                  "bSAME_SIZE_TOP_BOT": { "type": "boolean" },
                  "bSAME_SIZE_IMJ": { "type": "boolean" },
                  "bSAME_SIZE_LAYER": { "type": "boolean" },
                  "ELEMS": {
                    "type": "object",
                    "description": "CREATE_SUB_SECTION=true 일 때. KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "items": { "type": "integer" } },
                      "TO": { "type": "string" },
                      "STRUCTURE_GROUP_NAME": { "type": "string" }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

각 `BAR_SECTOR_*` 객체(구간별 철근) 구조:

```json
{
  "MAIN_BAR_TOP": {
    "LAYER1": { "NAME": "D19", "NUM": 4 },
    "LAYER2": { "NAME": "D16", "NUM": 2 }
  },
  "MAIN_BAR_BOT": {
    "LAYER1": { "NAME": "D19", "NUM": 4 },
    "LAYER2": { "NAME": "D16", "NUM": 2 }
  },
  "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
  "SKIN_BAR": { "NAME": "D10", "NUM": 2 }
}
```

### 파라미터

**Root / Item 공통**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 단면 번호 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **Required** |
| 1 | 콘크리트 보 철근 항목 (min 1) | `"ITEMS"` | Array[Object] | — | **Required** |
| (1) | 서브 단면 생성 여부 | `"CREATE_SUB_SECTION"` | Boolean | `false` | Optional |
| (2) | I단 구간 철근 | `"BAR_SECTOR_I"` | Object | — | **Required** |
| (3) | 중앙(M) 구간 철근 | `"BAR_SECTOR_M"` | Object | — | **Required** |
| (4) | J단 구간 철근 | `"BAR_SECTOR_J"` | Object | — | **Required** |
| (5) | 상단 피복 거리 dT | `"DT"` (예제에서는 `"MAIN_BAR_DC_TOP"`) | Number | — | **Required** |
| (6) | 하단 피복 거리 dB | `"DB"` (예제에서는 `"MAIN_BAR_DC_BOT"`) | Number | — | **Required** |

**`BAR_SECTOR_I/M/J` 구간 객체 (a~d)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| a | 상단 철근 | `"MAIN_BAR_TOP"` | Object | — | **Required** |
| a→(a) | 레이어1 | `"LAYER1"` | Object | — | **Required** |
| a→(d) | 레이어2 | `"LAYER2"` | Object | — | Optional |
| — | 레이어 내 철근 규격 · `D4`~`D57` | `"NAME"` | String | — | **Required** |
| — | 레이어 내 철근 개수 | `"NUM"` | Integer | — | **Required** |
| b | 하단 철근 | `"MAIN_BAR_BOT"` | Object (LAYER1/LAYER2) | — | **Required** |
| c | 스터럽(전단철근) | `"SHEAR_BAR"` | Object | — | **Required** |
| c→ | 스터럽 규격 · `D4`~`D57` | `"NAME"` | String | — | **Required** |
| c→ | 다리(leg) 개수 | `"LEG"` | Integer | — | **Required** |
| c→ | 스터럽 간격 @ | `"DIST"` | Number | — | **Required** |
| d | 표피철근(skin bar) | `"SKIN_BAR"` | Object | — | Optional |
| d→ | 표피철근 규격 · `D4`~`D57` | `"NAME"` | String | — | **Required** |
| d→ | 표피철근 개수 | `"NUM"` | Integer | — | **Required** |

**`CREATE_SUB_SECTION == true` 일 때**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| (1) | 서브 단면 ID (읽기 전용) | `"ID"` | Integer | — | Optional |
| (2) | 요소 목록 (KEYS / TO / STRUCTURE_GROUP_NAME 중 택1) | `"ELEMS"` | Object | — | **Required** |
| a | 요소 ID 배열 | `"KEYS"` | Array[Integer] | — | Optional |
| b | ID 범위 (예: `"1to160"`) | `"TO"` | String | — | Optional |
| c | 구조 그룹 이름 | `"STRUCTURE_GROUP_NAME"` | String | — | Optional |

> 참고: Request/Response 예제에서는 구간별 상·하단 주철근을 `"vMAIN_BAR_TOP"` / `"vMAIN_BAR_BOT"` **배열**로 표기하고, 피복 거리를 `"MAIN_BAR_DC_TOP"` / `"MAIN_BAR_DC_BOT"`로 표기합니다. 실제 전송 시에는 아래 예제 형식을 그대로 따르는 것이 안전합니다.

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "211": {
      "ITEMS": [
        {
          "ID": 0,
          "BAR_SECTOR_I": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_M": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_J": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "MAIN_BAR_DC_TOP": 0.06999999999999999,
          "MAIN_BAR_DC_BOT": 0.06999999999999999,
          "bSAME_SIZE_TOP_BOT": true,
          "bSAME_SIZE_IMJ": true,
          "bSAME_SIZE_LAYER": true
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "REBB": {
    "211": {
      "ITEMS": [
        {
          "ID": 0,
          "BAR_SECTOR_I": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_M": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_J": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "MAIN_BAR_DC_TOP": 0.06999999999999999,
          "MAIN_BAR_DC_BOT": 0.06999999999999999,
          "bSAME_SIZE_TOP_BOT": true,
          "bSAME_SIZE_IMJ": true,
          "bSAME_SIZE_LAYER": true
        }
      ]
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

# 단면 211의 보 철근 데이터 수정
sector = {
    "vMAIN_BAR_TOP": [],
    "vMAIN_BAR_BOT": [],
    "SHEAR_BAR": {"NAME": "D10", "LEG": 2, "DIST": 0.1},
    "SKIN_BAR_NAME": "",
    "SKIN_BAR_NUM": 2,
}
payload = {
    "Assign": {
        "211": {
            "ITEMS": [
                {
                    "ID": 0,
                    "BAR_SECTOR_I": sector,
                    "BAR_SECTOR_M": sector,
                    "BAR_SECTOR_J": sector,
                    "MAIN_BAR_DC_TOP": 0.07,
                    "MAIN_BAR_DC_BOT": 0.07,
                    "bSAME_SIZE_TOP_BOT": True,
                    "bSAME_SIZE_IMJ": True,
                    "bSAME_SIZE_LAYER": True,
                }
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/db/REBB", headers=HEADERS, json=payload)
print("POST:", res.status_code)

# 조회 (PUT/DELETE도 동일 URI 지원)
print(requests.get(f"{BASE_URL}/db/REBB", headers=HEADERS).json())
# requests.delete(f"{BASE_URL}/db/REBB", headers=HEADERS)
```

---

## 11. `/db/REBC` — Modify Column Rebar Data (기둥 철근 데이터 수정)

> **기능:** 단면 번호별로 콘크리트 기둥의 철근 데이터를 수정합니다. 주철근(`MAIN_BAR`), 단부/중앙부 전단철근(`SHEAR_BAR_END`/`SHEAR_BAR_CEN`), 피복 거리(`DO`), 후프 타입(`HOOP_TYPE`), 후크 타입(`HOOK_TYPE`)을 포함합니다.
>
> ⚠️ **이 엔드포인트는 `POST` 만 지원합니다.** (GET/PUT/DELETE 미지원)

### Input URI

```
{base url}/db/REBC
```

### Active Methods

`POST`

### JSON Schema

> 규격 enum(`D4`~`D57`)은 축약. 실제 스키마에는 각 `NAME`마다 전체 규격 목록이 나열됩니다.

```json
{
  "type": "object",
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "키는 단면 번호 문자열 (예: \"1\")",
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "Concrete column rebar items.",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": ["MAIN_BAR", "SHEAR_BAR_END", "SHEAR_BAR_CEN", "DO"],
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "default": false },
                  "ID": { "type": "integer", "description": "Sub Section ID (read only)" },
                  "ELEMS": {
                    "type": "object",
                    "description": "CREATE_SUB_SECTION=true 일 때. KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "items": { "type": "integer" } },
                      "TO": { "type": "string" },
                      "STRUCTURE_GROUP_NAME": { "type": "string" }
                    }
                  },
                  "MAIN_BAR": {
                    "type": "object",
                    "required": ["NAME", "NUM", "ROW", "USE_CORNER"],
                    "properties": {
                      "NAME": { "type": "string", "description": "Main rebar size (D4~D57)" },
                      "NUM": { "type": "integer", "description": "Total number of rebars" },
                      "ROW": { "type": "integer", "description": "Number of column row for rebar" },
                      "USE_CORNER": { "type": "boolean" },
                      "NAME_CORNER": { "type": "string", "description": "Corner rebar size (USE_CORNER=true 일 때)" }
                    }
                  },
                  "SHEAR_BAR_END": {
                    "type": "object",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "Hoop rebar size (D4~D57)" },
                      "LEG_Y": { "type": "integer", "description": "Number of leg (local Y dir.)" },
                      "LEG_Z": { "type": "integer", "description": "Number of leg (local Z dir.)" },
                      "DIST": { "type": "number", "description": "Distance between rebars" }
                    }
                  },
                  "SHEAR_BAR_CEN": {
                    "type": "object",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "Hoop rebar size (D4~D57)" },
                      "LEG_Y": { "type": "integer" },
                      "LEG_Z": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "DO": { "type": "number", "description": "Distance from concrete face to center of rebar" },
                  "HOOP_TYPE": {
                    "type": "string",
                    "default": "Ties",
                    "oneOf": [
                      { "title": "Ties", "const": "Ties" },
                      { "title": "Spirals", "const": "Spirals" }
                    ]
                  },
                  "HOOK_TYPE": {
                    "type": "integer",
                    "default": 0,
                    "oneOf": [
                      { "title": "90+(135 or 180)", "const": 0 },
                      { "title": "Both(135 or 180)", "const": 1 }
                    ]
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

**Root / Item**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 단면 번호 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **Required** |
| 1 | 콘크리트 기둥 철근 항목 (min 1) | `"ITEMS"` | Array[Object] | — | **Required** |
| (1) | 서브 단면 생성 여부 | `"CREATE_SUB_SECTION"` | Boolean | `false` | Optional |
| (2) | 서브 단면 ID (읽기 전용) | `"ID"` | Integer | — | Optional |
| (3) | 주철근 | `"MAIN_BAR"` | Object | — | **Required** |
| (4) | 단부 전단철근 | `"SHEAR_BAR_END"` | Object | — | **Required** |
| (5) | 중앙부 전단철근 | `"SHEAR_BAR_CEN"` | Object | — | **Required** |
| (6) | 콘크리트면~철근중심 거리 (do) | `"DO"` | Number | — | **Required** |
| (7) | 후프 철근 타입 · `"Ties"` / `"Spirals"` | `"HOOP_TYPE"` | String | `"Ties"` | Optional |
| (8) | 후크 타입 · `0`: 90+(135 or 180) / `1`: Both(135 or 180) | `"HOOK_TYPE"` | Enum(Integer) | `0` | Optional |

**`MAIN_BAR` 객체**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| a | 주철근 규격 · `D4`~`D57` | `"NAME"` | String | — | **Required** |
| b | 철근 총 개수 | `"NUM"` | Integer | — | **Required** |
| c | 열(row) 수 | `"ROW"` | Integer | — | **Required** |
| d | 코너 철근 사용 | `"USE_CORNER"` | Boolean | — | **Required** |
| a' | 코너 철근 규격 (USE_CORNER=true 일 때) | `"NAME_CORNER"` | String | — | **Required** |

**`SHEAR_BAR_END` / `SHEAR_BAR_CEN` 객체 (단부·중앙부 공통 구조)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| a | 후프 철근 규격 · `D4`~`D57` | `"NAME"` | String | — | **Required** |
| b | 다리 개수 (local Y) | `"LEG_Y"` | Integer | — | **Required** |
| c | 다리 개수 (local Z) | `"LEG_Z"` | Integer | — | **Required** |
| d | 철근 간격 @ | `"DIST"` | Number | — | **Required** |

**`CREATE_SUB_SECTION == true` 일 때 — `ELEMS` (KEYS / TO / STRUCTURE_GROUP_NAME 중 택1)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| a | 요소 ID 배열 | `"KEYS"` | Array[Integer] | — | Optional |
| b | ID 범위 (예: `"1to160"`) | `"TO"` | String | — | Optional |
| c | 구조 그룹 이름 | `"STRUCTURE_GROUP_NAME"` | String | — | Optional |

### Request JSON

**POST Request Body**

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_SECTION": false,
          "MAIN_BAR": { "NAME": "D19", "NUM": 8, "ROW": 3, "USE_CORNER": false },
          "SHEAR_BAR_END": { "NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 100 },
          "SHEAR_BAR_CEN": { "NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 200 },
          "DO": 40,
          "HOOP_TYPE": "Ties",
          "HOOK_TYPE": 0
        }
      ]
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

# 단면 1의 기둥 철근 데이터 수정 (REBC는 POST만 지원)
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_SECTION": False,
                    "MAIN_BAR": {"NAME": "D19", "NUM": 8, "ROW": 3, "USE_CORNER": False},
                    "SHEAR_BAR_END": {"NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 100},
                    "SHEAR_BAR_CEN": {"NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 200},
                    "DO": 40,
                    "HOOP_TYPE": "Ties",
                    "HOOK_TYPE": 0,
                }
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/db/REBC", headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# ※ REBC는 POST 전용이므로 GET/PUT/DELETE는 지원하지 않습니다.
```

---

## 12. `/db/REBW` — Modify Wall Rebar Data (벽체 철근 데이터 수정)

> **기능:** 벽체 ID별로 철근 데이터를 수정합니다. 수직/수평 철근, 단부 철근(End Rebar), 경계요소(Boundary Element) 수평 철근, 피복 거리(dw, de), 두께 및 서브 벽체 ID/층(Story) 정보를 포함합니다.

### Input URI

```
{base url}/db/REBW
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 규격 enum(`D4`~`D57`)은 축약.

```json
{
  "type": "object",
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "키는 벽체 ID 문자열 (예: \"1\")",
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "object",
                "properties": {
                  "CREATE_SUB_WALL_ID": { "type": "boolean", "default": false },
                  "SUB_WALL_ID": { "type": "integer", "description": "read only" },
                  "STORY": {
                    "type": "object",
                    "properties": {
                      "FROM": { "type": "string" },
                      "TO": { "type": "string" }
                    }
                  },
                  "VERTICAL_REBAR": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "HORIZONTAL_REBAR": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "USE_END_REBAR": { "type": "boolean", "default": false },
                  "END_REBAR": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "NUM": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "BE_HORIZONTAL_REBAR": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "BOUNDARY_ELEMENT_LENGTH": { "type": "number", "default": 0 },
                  "CONCRETE_FACE_TO_CENTER_OF_REBAR": {
                    "type": "object",
                    "properties": {
                      "DW": { "type": "number" },
                      "DE": { "type": "number" }
                    }
                  },
                  "USE_MODEL_THICKNESS": { "type": "boolean", "default": true },
                  "THICKNESS": { "type": "number", "description": "USE_MODEL_THICKNESS=false 일 때" }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 벽체 ID 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **Required** |
| 1 | 벽체 철근 항목 (min 1) | `"ITEMS"` | Array[Object] | — | **Required** |
| (1) | 서브 벽체 ID 생성 여부 | `"CREATE_SUB_WALL_ID"` | Boolean | `false` | Optional |
| (2) | 수직 철근 | `"VERTICAL_REBAR"` | Object | — | **Required** |
| (2)a | 규격 · `D4`~`D57` | `"NAME"` | String | — | **Required** |
| (2)b | 수직 철근 간격 @ | `"DIST"` | Number | — | **Required** |
| (3) | 수평 철근 | `"HORIZONTAL_REBAR"` | Object (NAME/DIST) | — | **Required** |
| (4) | 단부 철근 사용 여부 | `"USE_END_REBAR"` | Boolean | `false` | Optional |
| (5) | 경계요소 수평 철근 | `"BE_HORIZONTAL_REBAR"` | Object (NAME/DIST) | — | Optional |
| (6) | 경계요소 길이 | `"BOUNDARY_ELEMENT_LENGTH"` | Number | `0` | Optional |
| (7) | 콘크리트면~철근중심 거리 (dw, de) | `"CONCRETE_FACE_TO_CENTER_OF_REBAR"` | Object | — | **Required** |
| (7)a | dw | `"DW"` | Number | — | **Required** |
| (7)b | de | `"DE"` | Number | — | **Required** |
| (8) | 모델 두께 사용 | `"USE_MODEL_THICKNESS"` | Boolean | `true` | Optional |

**`CREATE_SUB_WALL_ID == true` 일 때**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| (1) | 서브 벽체 ID (읽기 전용) | `"SUB_WALL_ID"` | Integer | — | **Required** |
| (2) | 층 범위 | `"STORY"` | Object | — | **Required** |
| (2)a | 시작 층 | `"FROM"` | String | — | **Required** |
| (2)b | 끝 층 | `"TO"` | String | — | **Required** |

**`USE_END_REBAR == true` 일 때 — `END_REBAR`**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| a | 규격 · `D4`~`D57` | `"NAME"` | String | — | **Required** |
| b | 개수 | `"NUM"` | Integer | — | **Required** |
| c | 간격 @ | `"DIST"` | Number | — | **Required** |

**`USE_MODEL_THICKNESS == false` 일 때**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| (1) | 두께 | `"THICKNESS"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_WALL_ID": true,
          "VERTICAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "HORIZONTAL_REBAR": { "NAME": "D16", "DIST": 200 },
          "USE_END_REBAR": true,
          "BE_HORIZONTAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "BOUNDARY_ELEMENT_LENGTH": 222,
          "CONCRETE_FACE_TO_CENTER_OF_REBAR": { "DW": 50, "DE": 50 },
          "USE_MODEL_THICKNESS": false,
          "END_REBAR": { "NAME": "D25", "NUM": 2, "DIST": 150 },
          "THICKNESS": 1000,
          "SUB_WALL_ID": 1,
          "STORY": { "FROM": "2F", "TO": "Roof" }
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "REBW": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_WALL_ID": true,
          "SUB_WALL_ID": 1,
          "STORY": { "FROM": "2F", "TO": "Roof" },
          "VERTICAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "HORIZONTAL_REBAR": { "NAME": "D16", "DIST": 200 },
          "USE_END_REBAR": true,
          "END_REBAR": { "NAME": "D25", "NUM": 2, "DIST": 150 },
          "BE_HORIZONTAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "BOUNDARY_ELEMENT_LENGTH": 222,
          "CONCRETE_FACE_TO_CENTER_OF_REBAR": { "DW": 50, "DE": 50 },
          "USE_MODEL_THICKNESS": false,
          "THICKNESS": 1000
        }
      ]
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_WALL_ID": True,
                    "VERTICAL_REBAR": {"NAME": "D19", "DIST": 222},
                    "HORIZONTAL_REBAR": {"NAME": "D16", "DIST": 200},
                    "USE_END_REBAR": True,
                    "END_REBAR": {"NAME": "D25", "NUM": 2, "DIST": 150},
                    "BE_HORIZONTAL_REBAR": {"NAME": "D19", "DIST": 222},
                    "BOUNDARY_ELEMENT_LENGTH": 222,
                    "CONCRETE_FACE_TO_CENTER_OF_REBAR": {"DW": 50, "DE": 50},
                    "USE_MODEL_THICKNESS": False,
                    "THICKNESS": 1000,
                    "SUB_WALL_ID": 1,
                    "STORY": {"FROM": "2F", "TO": "Roof"},
                }
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/db/REBW", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/REBW", headers=HEADERS).json())
# requests.delete(f"{BASE_URL}/db/REBW", headers=HEADERS)
```

---

## 13. `/db/REBR` — Modify Brace Rebar Data (가새 철근 데이터 수정)

> **기능:** 단면 번호별로 콘크리트 가새(Brace)의 철근 데이터를 수정합니다. 구조는 기둥(REBC)과 유사하나 `USE_CORNER`/`HOOK_TYPE` 없이 주철근(`MAIN_BAR`), 단부/중앙부 전단철근, 피복(`DO`), 후프 타입(`HOOP_TYPE`)으로 구성됩니다.

### Input URI

```
{base url}/db/REBR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 규격 enum(`D4`~`D57`)은 축약.

```json
{
  "type": "object",
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "키는 단면 번호 문자열 (예: \"1\")",
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "object",
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "default": false },
                  "ID": { "type": "integer", "description": "read only" },
                  "ELEMS": {
                    "type": "object",
                    "description": "CREATE_SUB_SECTION=true 일 때. KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "items": { "type": "integer" } },
                      "TO": { "type": "string" },
                      "STRUCTURE_GROUP_NAME": { "type": "string" }
                    }
                  },
                  "MAIN_BAR": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "NUM": { "type": "integer", "description": "min 4" },
                      "ROW": { "type": "integer" }
                    }
                  },
                  "SHEAR_BAR_END": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "LEG_Y": { "type": "integer" },
                      "LEG_Z": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "SHEAR_BAR_CEN": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "LEG_Y": { "type": "integer" },
                      "LEG_Z": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "DO": { "type": "number", "description": "Concrete face to center of rebar" },
                  "HOOP_TYPE": {
                    "type": "string",
                    "default": "Ties",
                    "oneOf": [
                      { "title": "Ties", "const": "Ties" },
                      { "title": "Spirals", "const": "Spirals" }
                    ]
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 단면 번호 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **Required** |
| 1 | 콘크리트 가새 철근 항목 (min 1) | `"ITEMS"` | Array[Object] | — | **Required** |
| (1) | 서브 단면 생성 여부 | `"CREATE_SUB_SECTION"` | Boolean | `false` | Optional |
| (2) | 주철근 | `"MAIN_BAR"` | Object | — | **Required** |
| (2)a | 규격 · `D4`~`D57` | `"NAME"` | String | — | **Required** |
| (2)b | 개수 (min 4) | `"NUM"` | Integer | — | **Required** |
| (2)c | 열(row) 수 | `"ROW"` | Integer | — | **Required** |
| (3) | 단부 전단철근 | `"SHEAR_BAR_END"` | Object | — | **Required** |
| (4) | 중앙부 전단철근 | `"SHEAR_BAR_CEN"` | Object | — | **Required** |
| (5) | 콘크리트면~철근중심 거리 (do) | `"DO"` | Number | — | **Required** |
| (6) | 후프 철근 타입 · `"Ties"` / `"Spirals"` | `"HOOP_TYPE"` | String | `"Ties"` | Optional |

**`SHEAR_BAR_END` / `SHEAR_BAR_CEN` 객체 (공통 구조)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| a | 후프 철근 규격 · `D4`~`D57` | `"NAME"` | String | — | **Required** |
| b | 다리 개수 (local Y) | `"LEG_Y"` | Integer | — | **Required** |
| c | 다리 개수 (local Z) | `"LEG_Z"` | Integer | — | **Required** |
| d | 철근 간격 @ | `"DIST"` | Number | — | **Required** |

**`CREATE_SUB_SECTION == true` 일 때 — `ELEMS` (KEYS / TO / STRUCTURE_GROUP_NAME 중 택1)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| (1) | 서브 단면 ID (읽기 전용) | `"ID"` | Integer | — | Optional |
| a | 요소 ID 배열 | `"KEYS"` | Array[Integer] | — | Optional |
| b | ID 범위 (예: `"1to160"`) | `"TO"` | String | — | Optional |
| c | 구조 그룹 이름 | `"STRUCTURE_GROUP_NAME"` | String | — | Optional |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_SECTION": false,
          "MAIN_BAR": { "NAME": "D22", "NUM": 4, "ROW": 2 },
          "SHEAR_BAR_END": { "NAME": "D7", "LEG_Y": 2, "LEG_Z": 2, "DIST": 300 },
          "SHEAR_BAR_CEN": { "NAME": "D22", "LEG_Y": 3, "LEG_Z": 3, "DIST": 300 },
          "DO": 0.05,
          "HOOP_TYPE": "Spirals"
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "REBR": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_SECTION": false,
          "MAIN_BAR": { "NAME": "D22", "NUM": 4, "ROW": 2 },
          "SHEAR_BAR_END": { "NAME": "D7", "LEG_Y": 2, "LEG_Z": 2, "DIST": 300 },
          "SHEAR_BAR_CEN": { "NAME": "D22", "LEG_Y": 3, "LEG_Z": 3, "DIST": 300 },
          "DO": 0.05,
          "HOOP_TYPE": "Spirals"
        }
      ]
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_SECTION": False,
                    "MAIN_BAR": {"NAME": "D22", "NUM": 4, "ROW": 2},
                    "SHEAR_BAR_END": {"NAME": "D7", "LEG_Y": 2, "LEG_Z": 2, "DIST": 300},
                    "SHEAR_BAR_CEN": {"NAME": "D22", "LEG_Y": 3, "LEG_Z": 3, "DIST": 300},
                    "DO": 0.05,
                    "HOOP_TYPE": "Spirals",
                }
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/db/REBR", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/REBR", headers=HEADERS).json())
# requests.delete(f"{BASE_URL}/db/REBR", headers=HEADERS)
```

---

## End-to-End Workflow

아래 스크립트는 설계 입력 DB를 순서대로 구성하는 전형적인 흐름을 보여줍니다:
**RC 설계 코드 설정(DCON) → 강재 설계 코드 설정(DSTL) → 설계 부재 배정(MEMB) → 비지지 길이 설정(LENG) → 기둥 철근 배정(REBC)** 후, 한 항목을 다시 조회(GET)하여 검증합니다. 마지막에 간단한 CRUD 헬퍼도 포함합니다.

```python
import requests

# ─────────────────────────────────────────────
# 공통 설정
# ─────────────────────────────────────────────
BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (교량: /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}


def api(method, uri, body=None):
    """DB 엔드포인트용 간단 CRUD 헬퍼."""
    url = f"{BASE_URL}{uri}"
    res = requests.request(method, url, headers=HEADERS, json=body)
    print(f"[{method:6}] {uri:12} -> {res.status_code}")
    try:
        return res.json()
    except ValueError:
        return res.text


# ─────────────────────────────────────────────
# 1) RC 설계 코드 설정 (DCON)
# ─────────────────────────────────────────────
api("POST", "/db/DCON", {"Assign": {"1": {"DGNCODE": "KCI-USD12"}}})

# ─────────────────────────────────────────────
# 2) 강재 설계 코드 설정 (DSTL)
# ─────────────────────────────────────────────
api("POST", "/db/DSTL", {"Assign": {"1": {"DGNCODE": "AISC(16th)-LRFD22"}}})

# ─────────────────────────────────────────────
# 3) 설계 부재 배정 (MEMB) — 여러 요소를 하나의 설계 부재로 묶음
#    ※ 실제 배정 '작업'은 /ope/MEMB (15장). 여기서는 DB 레코드 저장.
# ─────────────────────────────────────────────
api("POST", "/db/MEMB", {
    "Assign": {
        "1": {"AELEM": [36, 48, 46, 49, 47]},
        "2": {"AELEM": [32, 43], "bREVERSE": True},
    }
})

# ─────────────────────────────────────────────
# 4) 비지지 길이 설정 (LENG)
# ─────────────────────────────────────────────
api("POST", "/db/LENG", {
    "Assign": {
        "1": {"LY": 9.464111, "LZ": 4, "LB": 4,
              "bNOTUSE": False, "bAUTOCALC": False, "LT": 9.464111}
    }
})

# ─────────────────────────────────────────────
# 5) 기둥 철근 배정 (REBC)
# ─────────────────────────────────────────────
api("POST", "/db/REBC", {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "ID": 0,
                    "vMAIN_BAR": [
                        {"NAME": "D19", "NUM": 8, "ROW": 3, "D0": 0.04,
                         "bUSE_CORNER": False, "NAME_CORNER": "D19"}
                    ],
                    "SHEAR_BAR_END": {"NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 0.1},
                    "SHEAR_BAR_CEN": {"NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 0.2},
                    "HOOP_TYPE": 1,
                    "bSAME_SPACE_END_CEN": False,
                    "NUM_BAR_BC_JOINT": 0,
                }
            ]
        }
    }
})

# ─────────────────────────────────────────────
# 6) 검증: 기둥 철근 레코드를 다시 조회
# ─────────────────────────────────────────────
result = api("GET", "/db/REBC")
print("검증 결과 (REBC):", result)

# ─────────────────────────────────────────────
# (선택) CRUD 예시 — 수정/삭제
# ─────────────────────────────────────────────
# api("PUT",    "/db/DCON", {"Assign": {"1": {"DGNCODE": "ACI318-19"}}})
# api("DELETE", "/db/LENG")
```
