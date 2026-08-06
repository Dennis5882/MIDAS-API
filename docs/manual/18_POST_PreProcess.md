# 18. POST – Pre-Process Tables

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

`POST` 파트는 전처리·후처리 테이블을 추출하는 데 사용됩니다. 이 파트(전처리 테이블)의 모든 엔드포인트는 **공통 URI `{base url}/post/TABLE`** 를 사용하며, `POST` 메서드만 지원합니다. 요청 바디의 `"Argument"` 객체에서 `TABLE_TYPE` 값으로 어떤 테이블을 추출할지 결정합니다.

---

## 공통 사항

### Input URI (전처리 테이블 공통)

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 공통 Request 구조

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "<테이블별 고유 값>",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON"
  }
}
```

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 응답 테이블 제목(Response Table Title) | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 (엔드포인트별 값 상이) | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로(JSON) | `"EXPORT_PATH"` | String | — | Optional |

> **참고:** 일부 테이블(예: `NODALBODYFORCE`가 아닌 `ELEMENTWEIGHT` 등)은 `NODE_ELEMS`로 대상 범위를 지정할 수 있으며, Story 계열 테이블은 `UNIT`·`STYLES`·`COMPONENTS`를 추가로 지원합니다. 상세는 각 절을 참조하세요.

### 공통 Response 구조

모든 응답은 `TABLE_NAME`(요청 시 지정한 이름)을 키로 하며, `FORCE`·`DIST`(단위), `HEAD`(열 이름 배열), `DATA`(행 배열) 구조를 가집니다.

```json
{
  "<TABLE_NAME>": {
    "FORCE": "N",
    "DIST": "m",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."], ["2", "..."]]
  }
}
```

---

## Endpoint(테이블) 목록

| No. | 테이블 | `TABLE_TYPE` | 대상 지정 |
|-----|--------|--------------|-----------|
| 1 | [Element Weight Table](#1-element-weight-table) | `ELEMENTWEIGHT` | `NODE_ELEMS` (3방식) |
| 2 | [Nodal Body Force Table](#2-nodal-body-force-table) | `NODALBODYFORCE` | 전체 |
| 3 | [Mass Summary Table](#3-mass-summary-table) | `MASS_SUMMARY_X/Y/Z` | 전체 |
| 4 | [Load Summary Table](#4-load-summary-table) | `LOAD_SUMMARY_X/Y/Z` | 전체 |
| 5 | [Material Table](#5-material-table) | `MATERIAL` | 전체 |
| 6 | [Section Table](#6-section-table) | `SECTIONALL` 외 9종 | 전체 |
| 7 | [Restraint Supports Table](#7-restraint-supports-table) | `SUPPORTS` | 전체 |
| 8 | [Story Mass Summary Table](#8-story-mass-summary-table) | `STORY_MASS` / `_X/_Y/_Z` | `UNIT`·`STYLES`·`COMPONENTS` |
| 9 | [Story Load Summary Table](#9-story-load-summary-table) | `STORY_LOAD_SUMMARY_X/Y/Z` | 전체 |
| 10 | [Story Weight Table](#10-story-weight-table) | `STORYWEIGHT` | 전체 |

---

## 1. Element Weight Table

> **기능:** 요소별 중량(단위중량·총중량 등)을 추출합니다. `NODE_ELEMS`로 대상 요소를 3가지 방식 중 하나로 지정할 수 있으며, 생략 시 전체 요소가 대상입니다.

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "ElementWeightTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" },
          "NODE_ELEMS": {
            "type": "object",
            "properties": {
              "TO": { "type": "string" },
              "KEYS": { "type": "array", "items": { "type": "integer" } },
              "STRUCTURE_GROUP_NAME": { "type": "string" }
            },
            "anyOf": [
              { "required": ["TO"] },
              { "required": ["KEYS"] },
              { "required": ["STRUCTURE_GROUP_NAME"] },
              { "not": { "required": ["TO", "KEYS", "STRUCTURE_GROUP_NAME"] } }
            ]
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
| 1 | 테이블 이름 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 · `"ELEMENTWEIGHT"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 노드/요소 지정 (아래 3방식 중 하나만 사용) | `"NODE_ELEMS"` | Object | All | Optional |
| 4-1 | 방식1: ID 각각 지정 (예: `[101, 102, 103]`) | `NODE_ELEMS.KEYS` | Array [Integer] | — | Optional |
| 4-2 | 방식2: ID 범위 지정 (예: `"101 to 105"`) | `NODE_ELEMS.TO` | String | — | Optional |
| 4-3 | 방식3: 구조 그룹명 지정 (예: `"SG1"`) | `NODE_ELEMS.STRUCTURE_GROUP_NAME` | String | — | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "ELEMENTWEIGHT",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Elementweight_all_Output.JSON",
    "NODE_ELEMS": { "TO": "1to5" }
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "N",
    "DIST": "m",
    "HEAD": ["Index", "No", "Type", "No", "Name", "No", "Name", "No", "Name", "Type", "Value", "UnitWeight", "TotalWeight"],
    "DATA": [
      ["1", "1", "BEAM", "1", "SS235", "1208", "H300x150x6.5/9", "-", "-", "L", "4.0000", "76980.0000", "1440.4500"],
      ["2", "2", "BEAM", "1", "SS235", "1208", "H300x150x6.5/9", "-", "-", "L", "4.0000", "76980.0000", "1440.4500"],
      ["3", "3", "BEAM", "1", "SS235", "1104", "H300x150x6.5/9", "-", "-", "L", "2.0615", "76980.0000", "742.3910"]
    ]
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

# ── POST: 1~5번 요소의 중량 테이블 추출 ────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "ElemWeight",
        "TABLE_TYPE": "ELEMENTWEIGHT",
        "NODE_ELEMS": {"TO": "1to5"}   # 방식2: 범위 지정
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("ElemWeight", {})
print("HEAD:", table.get("HEAD"))
for row in table.get("DATA", []):
    print(row)

# ── 다른 대상 지정 방식 예시 ───────────────────────────────────────
# 방식1: {"KEYS": [1, 2, 3]}
# 방식3: {"STRUCTURE_GROUP_NAME": "SG1"}
# 생략 시 전체 요소
```

---

## 2. Nodal Body Force Table

> **기능:** 하중케이스별 절점 체적력(Nodal Body Force, FX/FY/FZ)을 추출합니다.

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "NodalBodyForceTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 테이블 이름 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 · `"NODALBODYFORCE"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "NODALBODYFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\NodalBodyForce_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "N",
    "DIST": "m",
    "HEAD": ["Index", "LoadCase", "Node", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "EX", "1", "26.8158", "0.0000", "0.0000"],
      ["2", "EX", "2", "31.0746", "0.0000", "0.0000"],
      ["3", "EX", "3", "86.5800", "0.0000", "0.0000"]
    ]
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

# ── POST: 절점 체적력 테이블 추출 ──────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "NodalBodyForce",
        "TABLE_TYPE": "NODALBODYFORCE"
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("NodalBodyForce", {})
print("HEAD:", table.get("HEAD"))
print(f"총 {len(table.get('DATA', []))}개 행")
```

---

## 3. Mass Summary Table

> **기능:** 절점별 질량 요약(절점질량·하중질량·구조질량·합계)을 X/Y/Z 방향별로 추출합니다.

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "MassSummaryTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 테이블 이름 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 · X방향: `"MASS_SUMMARY_X"` / Y방향: `"MASS_SUMMARY_Y"` / Z방향: `"MASS_SUMMARY_Z"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body (X 방향)**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "MASS_SUMMARY_X",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Mass_Summary_X_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "N",
    "DIST": "m",
    "HEAD": ["Index", "Node", "NodalMass", "LoadToMass", "StructureMass", "Sum"],
    "DATA": [
      ["1", "1", "200.0000", "0.0000", "73.4631", "273.4631"],
      ["2", "2", "200.0000", "0.0000", "116.8933", "316.8933"],
      ["3", "3", "200.0000", "515.4224", "167.5067", "882.9290"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: X/Y/Z 3방향 질량 요약 테이블을 각각 추출 ─────────────────
for direction in ["X", "Y", "Z"]:
    payload = {
        "Argument": {
            "TABLE_NAME": f"Mass_{direction}",
            "TABLE_TYPE": f"MASS_SUMMARY_{direction}"
        }
    }
    resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
    table = resp.json().get(f"Mass_{direction}", {})
    total = sum(float(row[-1]) for row in table.get("DATA", []))
    print(f"{direction}방향 질량 합계: {total:.4f}")
```

---

## 4. Load Summary Table

> **기능:** 하중케이스별 하중 요약(집중·보·바닥·압력·자중·합계)을 X/Y/Z 방향별로 추출합니다.

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "LoadSummaryTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 테이블 이름 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 · X방향: `"LOAD_SUMMARY_X"` / Y방향: `"LOAD_SUMMARY_Y"` / Z방향: `"LOAD_SUMMARY_Z"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body (Z 방향)**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "LOAD_SUMMARY_Z",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Load_Summary_Z_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "N",
    "DIST": "m",
    "HEAD": ["Index", "Load", "Concent", "Beam", "Floor", "Pressure", "SelfWeight", "Sum"],
    "DATA": [
      ["1", "DL", "-9.000e+02", "0.000e+00", "-6.469e+05", "0.000e+00", "-1.005e+05", "-7.483e+05"],
      ["2", "LL", "-7.200e+02", "0.000e+00", "-1.294e+06", "0.000e+00", "0.000e+00", "-1.295e+06"],
      ["9", "DW", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "-1.005e+05", "-1.005e+05"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: Z방향 하중 요약 테이블 추출 ──────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Load_Z",
        "TABLE_TYPE": "LOAD_SUMMARY_Z"
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Load_Z", {})
for row in table.get("DATA", []):
    print(f"  하중케이스 {row[1]}: Sum={row[-1]}")
```

---

## 5. Material Table

> **기능:** 재료 특성 테이블(탄성계수·포아송비·열팽창계수·밀도·질량밀도 등)을 추출합니다.

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "MaterialTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 테이블 이름 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 · `"MATERIAL"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "MATERIAL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Material_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "ID", "Name", "Type", "Standard", "Code", "DB", "UseMassDensity", "Elasticity", "Poisson", "Thermal", "Density", "MassDensity", "Standard2", "Code2", "DB2", "Elasticity2", "Poisson2", "Thermal2", "Density2", "MassDensity2", "PlasticMatl.", "Sp.Heat", "HeatCo.", "MaterialType", "ShearMod._xy", "Elasticity_y", "Thermal_y", "ShearMod._xz", "Poisson_xz", "Elasticity_z", "Thermal_z", "ShearMod._yz", "Poisson_yz"],
    "DATA": [
      ["1", "1", "st", "Concrete", "KSCE-LSD15(RC)", "", "C45", "O", "3.1185e+07", "0.18", "1.0000e-05", "2.4517e+01", "2.5000e+00", "", "", "", "", "", "", "", "", "None", "0.0000", "0.0000", "Isotropic", "0.0000", "0.0000", "0.0000", "0.0000", "0", "0.0000", "0.0000", "0.0000", "0"]
    ]
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

# ── POST: 재료 특성 테이블 추출 ────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Materials",
        "TABLE_TYPE": "MATERIAL"
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Materials", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    mat = dict(zip(head, row))
    print(f"  [{mat['ID']}] {mat['Name']} ({mat['Type']}) E={mat['Elasticity']}")
```

---

## 6. Section Table

> **기능:** 단면 특성 테이블(면적·전단면적·관성모멘트·단면계수·둘레 등)을 추출합니다. `TABLE_TYPE`으로 단면 종류를 선택합니다.

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "SectionTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 테이블 이름 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 (아래 10종 중 하나) | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |

**`TABLE_TYPE` 값 목록**

| 값 | 설명 |
|----|------|
| `"SECTIONALL"` | 전체 단면 |
| `"SECTIONCOMBINED"` | Combined 단면 |
| `"SECTIONCOMPOSITE"` | Composite 단면 |
| `"SECTIONCONSTRUCTION"` | Construction 단면 |
| `"SECTIONDB/USER"` | DB/User 단면 |
| `"SECTIONPSC"` | PSC 단면 |
| `"SECTIONSRC"` | SRC 단면 |
| `"SECTIONSTEELGIRDER"` | Steel Girder 단면 |
| `"SECTIONTAPERED"` | Tapered(변단면) |
| `"SECTIONVALUE"` | Value 단면 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "SECTIONALL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Section_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "ID", "Type", "Shape", "Name", "Area", "Asy", "Asz", "Ixx", "Iyy", "Izz", "Cyp", "Cym", "Czp", "Czm", "Qyb", "Qzb", "Peri.(Out)", "Peri.(In)"],
    "DATA": [
      ["1", "1", "DB/User", "L", "Angle_DB", "0.0002", "0.0001", "0.0001", "0.0000", "0.0000", "0.0000", "0.0216", "0.0084", "0.0086", "0.0214", "0.0002", "0.0002", "0.1200", "0.0000"]
    ]
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

# ── POST: 전체 단면 특성 테이블 추출 ───────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Sections",
        "TABLE_TYPE": "SECTIONALL"
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Sections", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    sect = dict(zip(head, row))
    print(f"  [{sect['ID']}] {sect['Name']} ({sect['Shape']}) Area={sect['Area']}")
```

---

## 7. Restraint Supports Table

> **기능:** 지점 구속 조건 테이블(Dx/Dy/Dz/Rx/Ry/Rz/Rw 구속 여부, 경계 그룹)을 추출합니다.

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "SupportsTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 테이블 이름 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 · `"SUPPORTS"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "SUPPORTS",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Supports_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz", "Rw", "Group"],
    "DATA": [
      ["1", "2", "0", "0", "1", "0", "0", "0", "0", "Default"],
      ["2", "7", "1", "0", "1", "0", "0", "0", "0", "Default"],
      ["3", "9", "1", "0", "1", "0", "0", "0", "0", "Default"]
    ]
  }
}
```

> **참고:** `Dx`~`Rw` 값에서 `1`은 구속(Fixed), `0`은 자유(Free)를 의미합니다.

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 지점 구속 조건 테이블 추출 ───────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Supports",
        "TABLE_TYPE": "SUPPORTS"
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Supports", {})
for row in table.get("DATA", []):
    node, dx, dy, dz = row[1], row[2], row[3], row[4]
    print(f"  Node {node}: Dx={dx} Dy={dy} Dz={dz}")
```

---

## 8. Story Mass Summary Table

> **기능:** 층별 질량 요약을 추출합니다. `STORY_MASS`(방향 합산) 또는 `STORY_MASS_X/Y/Z`(방향별)를 선택하며, `UNIT`·`STYLES`·`COMPONENTS`로 단위·형식·표시 열을 제어할 수 있습니다.

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 테이블 이름 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 · `"STORY_MASS"` / `"STORY_MASS_X"` / `"STORY_MASS_Y"` / `"STORY_MASS_Z"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 응답 단위 설정 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 힘 단위 | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 길이 단위 | `UNIT.DIST` | String | — | Optional |
| 4-3 | └ 열 단위 | `UNIT.HEAT` | String | — | Optional |
| 4-4 | └ 온도 단위 | `UNIT.TEMP` | String | — | Optional |
| 5 | 응답 숫자 형식 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 숫자 형식 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 소수 자릿수 (0~15) | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 결과 테이블 표시 열 | `"COMPONENTS"` | Array [String] | All | Optional |

### Request / Response JSON

**POST Request Body — STORY_MASS (방향 합산)**

```json
{
  "Argument": {
    "TABLE_NAME": "Story Mass",
    "TABLE_TYPE": "STORY_MASS",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "COMPONENTS": ["Story", "Level", "X-DIR", "Y-DIR", "Rotational Mass", "X-Coord", "Y-Coord"]
  }
}
```

**POST Response Body — STORY_MASS**

```json
{
  "Story Mass": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Story", "Level", "X-DIR", "Y-DIR", "Rotational Mass", "X-Coord", "Y-Coord"],
    "DATA": [
      ["1", "Roof", "9.500", "1056.318", "1056.318", "221794.676", "17.930", "14.172"],
      ["2", "2F", "5.500", "1076.719", "1076.719", "226809.725", "18.021", "14.187"],
      ["3", "1F", "0.000", "0.000", "0.000", "0.000", "0.000", "0.000"],
      ["4", "", "Total", "11322.131", "11322.131", "", "", ""]
    ]
  }
}
```

**POST Request Body — STORY_MASS_X (방향별)**

```json
{
  "Argument": {
    "TABLE_NAME": "Story Mass X",
    "TABLE_TYPE": "STORY_MASS_X",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "COMPONENTS": ["Story", "Level", "NodalMass", "LoadToMass", "DiaphragmMass", "StructureMass", "Sum"]
  }
}
```

**POST Response Body — STORY_MASS_X**

```json
{
  "Story Mass X": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Story", "Level", "NodalMass", "LoadToMass", "DiaphragmMass", "StructureMass", "Sum"],
    "DATA": [
      ["1", "Roof", "9.500", "0.000", "541.887", "0.000", "514.431", "1056.318"],
      ["2", "2F", "5.500", "0.000", "541.887", "0.000", "534.832", "1076.719"],
      ["3", "1F", "0.000", "0.000", "0.000", "0.000", "147.850", "147.850"],
      ["4", "", "Total", "0.000", "6047.119", "0.000", "5422.862", "11469.981"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 층 질량 요약(방향 합산) 추출 ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Story Mass",
        "TABLE_TYPE": "STORY_MASS",
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
        "COMPONENTS": ["Story", "Level", "X-DIR", "Y-DIR", "Rotational Mass", "X-Coord", "Y-Coord"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Story Mass", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['Story'] or d['Level']}: X-DIR={d.get('X-DIR')}, Y-DIR={d.get('Y-DIR')}")
```

---

## 9. Story Load Summary Table

> **기능:** 층별·하중케이스별 하중 요약(집중·보·바닥·압력·자중·합계)을 X/Y/Z 방향별로 추출합니다.
>
> ⚠️ **2026-08-05 원문 갱신 반영:** `TABLE_TYPE` enum 값이 `STORY_LOAD_SUMMARY_X/Y/Z`에서
> `STORY_LOAD_X/Y/Z`로 변경됐고(같은 챕터의 `STORY_MASS`/`STORY_MASS_X` 명명 규칙과 통일),
> `UNIT`·`STYLES`·`COMPONENTS`(8번 Story Mass Summary Table과 동일한 구조)와 `LOAD_CASE_NAMES`
> 파라미터가 추가로 노출된다. `LOAD_CASE_NAMES`는 원문 Request 예제에는 있으나 Specifications
> 표에는 없는 상태라(원문 자체의 표/예제 불일치), 이 저장소 관례상 예제를 우선해 반영한다.

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "StoryLoadSummaryTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" },
          "UNIT": { "type": "object" },
          "STYLES": { "type": "object" },
          "COMPONENTS": { "type": "array" },
          "LOAD_CASE_NAMES": { "type": "array" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 테이블 이름 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 · X방향: `"STORY_LOAD_X"` / Y방향: `"STORY_LOAD_Y"` / Z방향: `"STORY_LOAD_Z"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 응답 단위 설정 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 힘 단위 | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 길이 단위 | `UNIT.DIST` | String | — | Optional |
| 4-3 | └ 열 단위 | `UNIT.HEAT` | String | — | Optional |
| 4-4 | └ 온도 단위 | `UNIT.TEMP` | String | — | Optional |
| 5 | 응답 숫자 형식 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 숫자 형식 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 소수 자릿수 (0~15) | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 결과 테이블 표시 열 | `"COMPONENTS"` | Array [String] | All | Optional |
| 7 | 하중케이스 이름 지정(예: `["DL (ST)"]`) ⚠️ 원문 Specifications 표에는 없고 Request 예제에만 등장 | `"LOAD_CASE_NAMES"` | Array [String] | All | Optional |

### Request / Response JSON

**POST Request Body (Z 방향)**

```json
{
  "Argument": {
    "TABLE_NAME": "StoryLoadZ",
    "TABLE_TYPE": "STORY_LOAD_Z",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "COMPONENTS": ["Load", "Story", "Level", "Concent", "Beam", "Floor", "Pressure", "SelfWeight", "Sum"],
    "LOAD_CASE_NAMES": ["DL (ST)"]
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Load", "Story", "Level", "Concent", "Beam", "Floor", "Pressure", "SelfWeight", "Sum"],
    "DATA": [
      ["1", "DL", "Roof", "9.500", "0.000", "-248.400", "-5730.624", "0.000", "-5044.509", "-10358.253"],
      ["2", "DL", "2F", "5.000", "0.000", "-248.400", "-5065.344", "0.000", "-5244.565", "-10558.309"],
      ["3", "DL", "1F", "0.000", "0.000", "0.000", "0.000", "0.000", "-1449.815", "-1449.815"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: X/Y/Z 3방향 층 하중 요약 테이블을 각각 추출 ──────────────
for direction in ["X", "Y", "Z"]:
    payload = {
        "Argument": {
            "TABLE_NAME": f"StoryLoad_{direction}",
            "TABLE_TYPE": f"STORY_LOAD_{direction}",
            "UNIT": {"FORCE": "KN", "DIST": "M"},
            "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
            "COMPONENTS": ["Load", "Story", "Level", "Concent", "Beam", "Floor", "Pressure", "SelfWeight", "Sum"]
        }
    }
    resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
    table = resp.json().get(f"StoryLoad_{direction}", {})
    print(f"{direction}방향: {len(table.get('DATA', []))}개 행")
```

---

## 10. Story Weight Table

> **기능:** 층별 중량을 요소 종류별(트러스·보·멤브레인·판·벽체·솔리드·합계)로 추출합니다.
>
> ⚠️ **2026-08-05 원문 갱신 반영:** `UNIT`·`STYLES`·`COMPONENTS` 파라미터(8번 Story Mass
> Summary Table과 동일한 구조)가 추가로 노출된다. `TABLE_TYPE` 값(`"STORYWEIGHT"`) 자체는
> 변경 없음.

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "StoryWeightTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" },
          "UNIT": { "type": "object" },
          "STYLES": { "type": "object" },
          "COMPONENTS": { "type": "array" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 테이블 이름 (출력 제목) | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 · `"STORYWEIGHT"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로(JSON) | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 응답 단위 설정 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 힘 단위 | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 길이 단위 | `UNIT.DIST` | String | — | Optional |
| 4-3 | └ 열 단위 | `UNIT.HEAT` | String | — | Optional |
| 4-4 | └ 온도 단위 | `UNIT.TEMP` | String | — | Optional |
| 5 | 응답 숫자 형식 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 숫자 형식 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 소수 자릿수 (0~15) | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 결과 테이블 표시 열 | `"COMPONENTS"` | Array [String] | All | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "STORYWEIGHT",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "COMPONENTS": ["Story", "Level", "Truss", "Beam", "Membrane", "Plate", "Wall", "Solid", "Sum"]
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Story", "Level", "Truss", "Beam", "Membrane", "Plate", "Wall", "Solid", "Sum"],
    "DATA": [
      ["1", "Roof", "5.600", "0.000", "56.912", "0.000", "0.000", "104.321", "0.000", "161.233"],
      ["2", "2F", "2.800", "0.000", "70.257", "0.000", "0.000", "208.642", "0.000", "278.898"],
      ["3", "1F", "0.000", "0.000", "13.345", "0.000", "0.000", "104.321", "0.000", "117.666"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 층 중량 테이블 추출 ──────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_TYPE": "STORYWEIGHT",
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
        "COMPONENTS": ["Story", "Level", "Truss", "Beam", "Membrane", "Plate", "Wall", "Solid", "Sum"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Example", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['Story']} (Lv.{d['Level']}): 합계 중량 = {d['Sum']}")
```

---

## End-to-End Workflow

다음은 해석 실행 후 전처리 요약 테이블들을 일괄 추출하는 워크플로우입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

def get_table(table_type, name, extra=None):
    """전처리 테이블 추출 공통 함수"""
    arg = {"TABLE_NAME": name, "TABLE_TYPE": table_type}
    if extra:
        arg.update(extra)
    resp = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    return resp.json().get(name, {})

# ── STEP 1: 재료·단면 확인 ─────────────────────────────────────────
mat = get_table("MATERIAL", "Mat")
print(f"STEP1 재료 {len(mat.get('DATA', []))}종")
sect = get_table("SECTIONALL", "Sect")
print(f"      단면 {len(sect.get('DATA', []))}종")

# ── STEP 2: 지점 구속 조건 확인 ────────────────────────────────────
sup = get_table("SUPPORTS", "Sup")
print(f"STEP2 지점 {len(sup.get('DATA', []))}개")

# ── STEP 3: 질량·하중 요약 (X/Y/Z) ─────────────────────────────────
for d in ["X", "Y", "Z"]:
    m = get_table(f"MASS_SUMMARY_{d}", f"Mass{d}")
    l = get_table(f"LOAD_SUMMARY_{d}", f"Load{d}")
    print(f"STEP3 {d}방향: 질량 {len(m.get('DATA', []))}행, 하중 {len(l.get('DATA', []))}행")

# ── STEP 4: 층별 요약 (질량·하중·중량) ─────────────────────────────
story_mass = get_table("STORY_MASS", "StoryMass",
                        extra={"UNIT": {"FORCE": "KN", "DIST": "M"},
                               "STYLES": {"FORMAT": "Fixed", "PLACE": 3}})
print(f"STEP4 층 질량 {len(story_mass.get('DATA', []))}행")
story_weight = get_table("STORYWEIGHT", "StoryWeight")
print(f"      층 중량 {len(story_weight.get('DATA', []))}행")

# ── STEP 5: 요소 중량 (전체) ───────────────────────────────────────
elem_w = get_table("ELEMENTWEIGHT", "ElemW")
print(f"STEP5 요소 중량 {len(elem_w.get('DATA', []))}행")
```
