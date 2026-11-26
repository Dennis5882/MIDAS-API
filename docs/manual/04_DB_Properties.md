# 04 DB — Properties

> **Source**: [MIDAS API Online Manual](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **Sync date**: 2026-07-12  
> **Endpoints covered**: `/db/MATL`, `/db/MATL-M1`, `/db/IMFM`, `/db/IMFM-M1`, `/db/TDMF`, `/db/TDMT`, `/db/TDME`, `/db/EDMP`, `/db/TMAT`, `/db/EPMT`, `/db/EPMT-M1`, `/db/SECT`, `/db/THIK`, `/db/TSGR`, `/db/SECF`, `/db/RPSC`, `/db/STRPSSM`, `/db/PSSF`, `/db/VBEM`, `/db/VSEC`, `/db/EWSF`, `/db/IEHC`, `/db/IEHG`, `/db/IEHG-BEAM-M1`, `/db/IEHG-TRUSS-M1`, `/db/IEHG-GL-M1`, `/db/IEHG-PSS-M1`, `/db/FIMP`, `/db/FIBR`, `/db/GRDP`, `/db/ESSF`, `/db/MATD`, `/db/SECV`, `DESIGN/SECT`

---

## Table of Contents

| No. | Endpoint | 기능 | Methods |
|-----|----------|------|---------|
| 1 | [`/db/MATL`](#1-dbmatl) | Material Properties | POST, GET, PUT, DELETE |
| 2 | [`/db/MATL-M1`](#2-dbmatl-m1) | Material Properties (Hyper-S) | POST, GET, PUT, DELETE |
| 3 | [`/db/IMFM`](#3-dbimfm) | Inelastic Material Props for Fiber Model | POST, GET, PUT, DELETE |
| 4 | [`/db/IMFM-M1`](#4-dbimfm-m1) | Inelastic Material Link for Auto Generation (Hyper-S) | POST, GET, PUT, DELETE |
| 5 | [`/db/TDMF`](#5-dbtdmf) | Time Dependent Material – User Defined | POST, GET, PUT, DELETE |
| 6 | [`/db/TDMT`](#6-dbtdmt) | Time Dependent Material – Creep/Shrinkage | POST, GET, PUT, DELETE |
| 7 | [`/db/TDME`](#7-dbtdme) | Time Dependent Material – Compressive Strength | POST, GET, PUT, DELETE |
| 8 | [`/db/EDMP`](#8-dbedmp) | Change Property | POST, GET, PUT, DELETE |
| 9 | [`/db/TMAT`](#9-dbtmat) | Time Dependent Material Link | POST, GET, PUT, DELETE |
| 10 | [`/db/EPMT`](#10-dbepmt) | Plastic Material | POST, GET, PUT, DELETE |
| 11 | [`/db/EPMT-M1`](#11-dbepmt-m1) | Plastic Material (Hyper-S) | POST, GET, PUT, DELETE |
| 12 | [`/db/SECT`](#12-dbsect) | Section Properties | POST, GET, PUT, DELETE |
| 13 | [`/db/THIK`](#13-dbthik) | Thickness | POST, GET, PUT, DELETE |
| 14 | [`/db/TSGR`](#14-dbtsgr) | Tapered Group | POST, GET, PUT, DELETE |
| 15 | [`/db/SECF`](#15-dbsecf) | Section Manager – Stiffness | POST, GET, PUT, DELETE |
| 16 | [`/db/RPSC`](#16-dbrpsc) | Section Manager – Reinforcements | POST, GET, PUT, DELETE |
| 17 | [`/db/STRPSSM`](#17-dbstrpssm) | Section Manager – Stress Points | POST, GET, PUT, DELETE |
| 18 | [`/db/PSSF`](#18-dbpssf) | Section Manager – Plate Stiffness Scale Factor | POST, GET, PUT, DELETE |
| 19 | [`/db/VBEM`](#19-dbvbem) | Virtual Beam | POST, GET, PUT, DELETE |
| 20 | [`/db/VSEC`](#20-dbvsec) | Virtual Section | POST, GET, PUT, DELETE |
| 21 | [`/db/EWSF`](#21-dbewsf) | Effective Width Scale Factor | POST, GET, PUT, DELETE |
| 22 | [`/db/IEHC`](#22-dbiehc) | Inelastic Hinge Control Data | POST, GET, PUT, DELETE |
| 23 | [`/db/IEHG`](#23-dbiehg) | Assign Inelastic Hinge Properties | POST, GET, PUT, DELETE |
| 24 | [`/db/IEHG-BEAM-M1`](#24-dbiehg-beam-m1) | Assign Inelastic Hinges – Beam (Hyper-S) | POST, GET, PUT, DELETE |
| 25 | [`/db/IEHG-TRUSS-M1`](#25-dbiehg-truss-m1) | Assign Inelastic Hinges – Truss (Hyper-S) | POST, GET, PUT, DELETE |
| 26 | [`/db/IEHG-GL-M1`](#26-dbiehg-gl-m1) | Assign Inelastic Hinges – General Link (Hyper-S) | POST, GET, PUT, DELETE |
| 27 | [`/db/IEHG-PSS-M1`](#27-dbiehg-pss-m1) | Assign Inelastic Hinges – Point Spring (Hyper-S) | POST, GET, PUT, DELETE |
| 28 | [`/db/FIMP`](#28-dbfimp) | Inelastic Material Properties | POST, GET, PUT, DELETE |
| 29 | [`/db/FIBR`](#29-dbfibr) | Fiber Division of Section | POST, GET, PUT, DELETE |
| 30 | [`/db/GRDP`](#30-dbgrdp) | Group Damping | POST, GET, PUT, DELETE |
| 31 | [`/db/ESSF`](#31-dbessf) | Element Stiffness Scale Factor | POST, GET, PUT, DELETE |
| 32 | [`/db/MATD`](#32-dbmatd) | Modify Concrete Materials | GET, PUT |
| 33 | [`/db/SECV`](#33-dbsecv) | Virtual Section for Design | POST, GET, PUT, DELETE |
| 34 | [`DESIGN/SECT`](#34-designsect) | Section for Design | POST, GET, PUT, DELETE |

---

## 공통 설정

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY"

def midas_api(method: str, endpoint: str, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}
```

---

## 1. `/db/MATL`

> **Material Properties** — 재료 특성을 정의합니다. DB(표준), Isotropic(등방성), Orthotropic(직교이방성) 3가지 타입을 지원합니다.

- **URL**: `{base url}/db/MATL`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Material Properties ↗](https://support.midasuser.com/hc/en-us/articles/35807411331993)

### JSON Schema

```json
{
  "MATL": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "TYPE":       { "description": "Material Type",    "type": "string" },
      "NAME":       { "description": "Material Name",   "type": "string" },
      "HE_SPEC":    { "description": "Specific Heat",   "type": "number" },
      "HE_COND":    { "description": "Heat Conduction", "type": "number" },
      "PLMT":       { "description": "Plasticity Key",  "type": "integer" },
      "P_NAME":     { "description": "Plasticity Name", "type": "string" },
      "bMASS_DENS": { "description": "Use Mass Density","type": "boolean" },
      "DAMP_RAT":   { "description": "Damping Ratio",   "type": "number" },
      "PARAM":      { "description": "Material Data",   "type": "array" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Material Type • Concrete: `"CONC"` • Steel: `"STEEL"` • SRC: `"SRC"` • Aluminum: `"ALUMINUM"` • User Defined: `"USER"` | `"TYPE"` | String | - | **Required** |
| 2 | Material Name | `"NAME"` | String | - | **Required** |
| 3 | Specific Heat | `"HE_SPEC"` | Number | 0 | Optional |
| 4 | Heat Conduction | `"HE_COND"` | Number | 0 | Optional |
| 5 | Plastic Material No. | `"PLMT"` | Integer | 0 | Optional |
| 6 | Plastic Material Name | `"P_NAME"` | String | Blank | Optional |
| 7 | Use Mass Density | `"bMASS_DENS"` | Boolean | false | Optional |
| 8 | Damping Ratio | `"DAMP_RAT"` | Number | 0 | Optional |
| 9 | Material Parameter | `"PARAM"` | Object | - | **Required** |
| (1) | Material Parameter Type • Standard: 1 • Isotropic: 2 • Orthotropic: 3 | `"P_TYPE"` | Integer | - | **Required** |

#### PARAM — P_TYPE = 1 (Standard / DB)

| Sub-No. | Description | Key | Value Type | Default | Required |
|---------|-------------|-----|------------|---------|----------|
| (2) | Standard Name | `"STANDARD"` | String | - | **Required** |
| (3) | Code Name | `"CODE"` | String | Blank | Optional |
| (4) | DB Name | `"DB"` | String | - | **Required** |
| (5) | Use Young's Modulus (User Option) | `"bELAST"` | Boolean | false | Optional |

#### PARAM — P_TYPE = 2 (Isotropic / User)

| Sub-No. | Description | Key | Value Type | Default | Required |
|---------|-------------|-----|------------|---------|----------|
| (2) | Modulus of Elasticity | `"ELAST"` | Number | - | **Required** |
| (3) | Poisson's Ratio | `"POISN"` | Number | - | **Required** |
| (4) | Thermal Coefficient | `"THERMAL"` | Number | - | **Required** |
| (5) | Weight Density | `"DEN"` | Number | - | **Required** |
| (6) | Mass Density | `"MASS"` | Number | - | **Required** |

#### PARAM — P_TYPE = 3 (Orthotropic / User)

| Sub-No. | Description | Key | Value Type | Default | Required |
|---------|-------------|-----|------------|---------|----------|
| (2) | Modulus of Elasticity (3 values) | `"ELAST_M"` | Array[Number] | - | **Required** |
| (3) | Poisson's Ratio (3 values) | `"POISN_M"` | Array[Number] | - | **Required** |
| (4) | Thermal Coefficient (3 values) | `"THERMAL_M"` | Array[Number] | - | **Required** |
| (5) | Shear Modulus (3 values) | `"SHEAR_M"` | Array[Number] | - | **Required** |
| (6) | Weight Density | `"DEN"` | Number | - | **Required** |
| (7) | Mass Density | `"MASS"` | Number | - | **Required** |

### Request Body 예제

#### Standard DB 재료 (Steel + Concrete)

```json
{
  "Assign": {
    "1": {
      "TYPE": "STEEL",
      "NAME": "DB_Steel",
      "HE_SPEC": 0, "HE_COND": 0,
      "PLMT": 0, "P_NAME": "",
      "bMASS_DENS": false,
      "DAMP_RAT": 0.02,
      "PARAM": [{ "P_TYPE": 1, "STANDARD": "EN05(S)", "CODE": "", "DB": "S450", "bELAST": false }]
    },
    "2": {
      "TYPE": "CONC",
      "NAME": "DB_Conc",
      "HE_SPEC": 0, "HE_COND": 0,
      "PLMT": 0, "P_NAME": "",
      "bMASS_DENS": false,
      "DAMP_RAT": 0.05,
      "PARAM": [{ "P_TYPE": 1, "STANDARD": "KS21(RC)", "CODE": "", "DB": "C24", "bELAST": false }]
    }
  }
}
```

#### Isotropic User 재료

```json
{
  "Assign": {
    "5": {
      "TYPE": "USER",
      "NAME": "User_Steel",
      "HE_SPEC": 0, "HE_COND": 0,
      "PLMT": 0, "P_NAME": "",
      "bMASS_DENS": true,
      "DAMP_RAT": 0,
      "PARAM": [{
        "P_TYPE": 2,
        "ELAST": 205000000,
        "POISN": 0.3,
        "THERMAL": 6.667e-06,
        "DEN": 76.98,
        "MASS": 7.85
      }]
    }
  }
}
```

### Python 예제

```python
# --- GET: 전체 재료 조회 ---
result = midas_api("GET", "/db/MATL")
materials = result.get("MATL", {})
print(f"정의된 재료 수: {len(materials)}")
for mid, m in materials.items():
    print(f"  {mid}: {m['NAME']} ({m['TYPE']})")

# --- POST: DB 재료 생성 (KS 콘크리트 + 강재) ---
matl_data = {
    "Assign": {
        "1": {
            "TYPE": "CONC", "NAME": "C24",
            "bMASS_DENS": False, "DAMP_RAT": 0.05,
            "HE_SPEC": 0, "HE_COND": 0, "PLMT": 0, "P_NAME": "",
            "PARAM": [{"P_TYPE": 1, "STANDARD": "KS21(RC)", "CODE": "", "DB": "C24", "bELAST": False}]
        },
        "2": {
            "TYPE": "STEEL", "NAME": "SS400",
            "bMASS_DENS": False, "DAMP_RAT": 0.02,
            "HE_SPEC": 0, "HE_COND": 0, "PLMT": 0, "P_NAME": "",
            "PARAM": [{"P_TYPE": 1, "STANDARD": "KS21(S)", "CODE": "", "DB": "SS400", "bELAST": False}]
        }
    }
}
midas_api("POST", "/db/MATL", matl_data)

# --- DELETE ---
midas_api("DELETE", "/db/MATL", {"Assign": {"3": None}})
```

---

## 2. `/db/MATL-M1`

> **Material Properties (Hyper-S)** — Hyper-S 솔버 전용 재료 특성 정의.  
> ¹⁾ 동일한 `/db/MATL` 엔드포인트를 사용하나 Hyper-S 전용 파라미터를 추가 지원합니다.

- **URL**: `{base url}/db/MATL-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Material Properties (Hyper-S) ↗](https://support.midasuser.com/hc/ko/articles/56396523438873)

> **Note**: Hyper-S 솔버 전용 엔드포인트입니다. 기본 재료 구조는 `/db/MATL`과 동일하며, Hyper-S 전용 하이퍼엘라스틱(Hyperelastic) 재료 모델을 추가로 지원합니다.

```python
# Hyper-S 재료 조회
result = midas_api("GET", "/db/MATL-M1")
```

<!-- om-fields:56396523438873 -->
**OM 원문 추가 필드 — Material Properties ([56396523438873](https://support.midasuser.com/hc/en-us/articles/56396523438873))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Name | `"MATL_NAME"` | string | - | **Required** |
| 2 | Type of Design · Steel: STEEL · Concrete: CONC · SRC: SRC · User: USER | `"MATL_TYPE"` | string (enum) | - | **Required** |
| 3 | PARAM When MATL_TYPE is "SRC", enter both Concrete and Steel inputs. | `"PARAM"` | array [object] | - | **Required** |
| (1) | Isotropic / Orthotropic · Standard: 0 · Isotropic User Defined: 1 · Orthotropic User Defined: 2 When MATL_TYPE is "SRC", "2" is not available. | `"P_TYPE"` | integer (enum) | - | **Required** |
| (2) | [When P_TYPE = 0] Standard | `"STANDARD"` | string | - | **Required** |
| a | [When P_TYPE = 1] Modulus of Elasticity | `"bELAST"` | number | - | Optional |
| b | Poisson's Ratio | `"POISN"` | number | - | Optional |
| c | Thermal Coefficient | `"THERMAL"` | number | - | Optional |
| d | Weight Density | `"DEN"` | number | - | Optional |
| e | Use Mass Density | `"bMASS_DENS"` | boolean | false | Optional |
| f | [When bMASS_DENS = true] Mass Density | `"MASS"` | number | - | **Required** |
| a | [When P_TYPE = 2] Weight Density | `"DEN"` | number | - | Optional |
| b | Modulus of Elasticity | `"ELAST_M"` | array | - | Optional |
| c | Thermal Coefficient | `"THERMAL_M"` | array | - | Optional |
| d | Shear Modulus | `"SHEAR_M"` | array | - | Optional |
| e | Poisson's Ratio | `"POISN_M"` | array | - | Optional |
| f | Use Mass Density | `"bMASS_DENS"` | boolean | false | Optional |
| g | [When bMASS_DENS = true] Mass Density | `"MASS"` | number | - | **Required** |
| (7) | Plastic Material Name | `"PLASTIC_MATL_NAME"` | string | - | Optional |
| (8) | THERMAL_TRANS | `"THERMAL_TRANS"` | object | - | Optional |
| a | Specific Heat | `"HE_SPEC"` | number | 0 | Optional |
| b | Heat Conduction | `"HE_COND"` | number | 0 | Optional |
| 5 | Damping Ratio | `"DAMP_RAT"` | number | 0 | Optional |

<!-- /om-fields -->


---

## 3. `/db/IMFM`

> **Inelastic Material Properties for Fiber Model** — 섬유 모델(Fiber Model) 비선형 재료 특성을 할당합니다.

- **URL**: `{base url}/db/IMFM`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Inelastic Material Properties for Fiber Model ↗](https://support.midasuser.com/hc/en-us/articles/35807475893401)

### JSON Schema

```json
{
  "IMFM": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "CONC_NAME":          { "description": "Fiber Model Property Name (Concrete)",         "type": "string" },
      "CONFINED_CONC_NAME": { "description": "Fiber Model Property Name (Confined Concrete)","type": "string" },
      "REBAR_NAME":         { "description": "Fiber Model Property Name (Rebar)",            "type": "string" },
      "STEEL_NAME":         { "description": "Fiber Model Property Name (Steel)",            "type": "string" }
    }
  }
}
```

### Specifications

#### Concrete Material

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Inelastic Material of Concrete | `"CONC_NAME"` | String | Blank | Optional |
| 2 | Confined Concrete for Columns | `"CONFINED_CONC_NAME"` | String | Blank | Optional |
| 3 | Inelastic Material of Rebar | `"REBAR_NAME"` | String | Blank | Optional |

#### Steel Material

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Inelastic Material of Steel | `"STEEL_NAME"` | String | Blank | Optional |

### Request Body

```json
{
  "Assign": {
    "1": {
      "CONC_NAME": "Concrete_KP",
      "CONFINED_CONC_NAME": "Confined_KP",
      "REBAR_NAME": "Rebar_Menegotto"
    },
    "2": {
      "STEEL_NAME": "Steel_Bilinear"
    }
  }
}
```

### Python 예제

```python
# 콘크리트 요소에 섬유 모델 재료 할당
imfm_data = {
    "Assign": {
        "3": {
            "CONC_NAME": "Conc_Kent&Park",
            "CONFINED_CONC_NAME": "Confined_Conc",
            "REBAR_NAME": "Rebar_MP"
        }
    }
}
midas_api("POST", "/db/IMFM", imfm_data)
```

---

## 4. `/db/IMFM-M1`

> **Inelastic Material Link for Auto Generation (Hyper-S)** — Hyper-S 전용 비선형 재료 자동 생성 링크.

- **URL**: `{base url}/db/IMFM-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Inelastic Material Link for Auto Generation ↗](https://support.midasuser.com/hc/ko/articles/56375076523929)

```python
result = midas_api("GET", "/db/IMFM-M1")
```

<!-- om-fields:56375076523929 -->
**OM 원문 추가 필드 — Inelastic Material Link for Auto Generation ([56375076523929](https://support.midasuser.com/hc/en-us/articles/56375076523929))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Material Type - Concrete | `"CONCRETE"` | object | - | Optional |
| (1) | Inelastic Material Property - Unconfined Concrete | `"UN_CONC_NAME"` | string | - | **Required** |
| (2) | Inelastic Material Property - Confined Concrete | `"CONF_CONC_NAME"` | string | - | Optional |
| (3) | Inelastic Material Property - Rebar | `"REBAR_NAME"` | string | - | **Required** |
| 2 | Material Type - STEEL | `"STEEL"` | object | - | Optional |
| (1) | Inelastic Material Property - Steel | `"STEEL_NAME"` | string | - | **Required** |

<!-- /om-fields -->


---

## 5. `/db/TDMF`

> **Time Dependent Material – User Defined** — 크리프/건조수축/이완 사용자 정의 함수를 정의합니다.

- **URL**: `{base url}/db/TDMF`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Time Dependent Material Properties - User Defined ↗](https://support.midasuser.com/hc/en-us/articles/35807665049369)

### JSON Schema

```json
{
  "TDMF": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":       { "description": "Material Function Name", "type": "string" },
      "FTYPE":      { "description": "Material Func Type",    "type": "string" },
      "SCALE":      { "description": "Scale Factor",          "type": "number" },
      "CTYPE":      { "description": "Creep Type",            "type": "string" },
      "DESC":       { "description": "Description",           "type": "string" },
      "RELAXATION": { "description": "Relaxation Time",       "type": "integer" },
      "vDAY":       { "description": "Function Data",         "type": "array" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Material Function Name | `"NAME"` | String | - | **Required** |
| 2 | Material Function Type • Creep: `"CREEP"` • Shrinkage Strain: `"SHRINK"` • Relaxation: `"RELAX"` | `"FTYPE"` | String | - | **Required** |
| 3 | Scale Factor | `"SCALE"` | Number | - | **Required** |
| 4 | Description | `"DESC"` | String | Blank | Optional |
| 5 | Function Data (Array of `{DAY, VALUE}`) | `"vDAY"` | Array[Object] | - | **Required** |
| (1) | Time | `"DAY"` | Number | - | **Required** |
| (2) | Value | `"VALUE"` | Number | - | **Required** |
| 6 (Creep only) | Creep Type • Specific Creep: `"SC"` • Creep Function: `"CF"` • Creep Coefficient: `"CC"` | `"CTYPE"` | String | - | **Required** |
| 6 (Relax only) | Relaxation Time • Hour: 0 • Day: 1 | `"RELAXATION"` | Integer | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "CreepFunc_1",
      "FTYPE": "CREEP",
      "CTYPE": "CC",
      "SCALE": 1.0,
      "DESC": "사용자 정의 크리프 함수",
      "vDAY": [
        {"DAY": 28,  "VALUE": 0.5},
        {"DAY": 90,  "VALUE": 1.0},
        {"DAY": 365, "VALUE": 1.5},
        {"DAY": 3650,"VALUE": 2.0}
      ]
    }
  }
}
```

### Python 예제

```python
tdmf_data = {
    "Assign": {
        "1": {
            "NAME": "Shrinkage_User",
            "FTYPE": "SHRINK",
            "SCALE": 1.0,
            "DESC": "건조수축 함수",
            "vDAY": [
                {"DAY": 28,   "VALUE": 0.0001},
                {"DAY": 90,   "VALUE": 0.0002},
                {"DAY": 365,  "VALUE": 0.0003},
                {"DAY": 3650, "VALUE": 0.0004}
            ]
        }
    }
}
midas_api("POST", "/db/TDMF", tdmf_data)
```

<!-- om-fields:35807665049369 -->
**OM 원문 추가 필드 — Time Dependent Material Properties - User Defined ([35807665049369](https://support.midasuser.com/hc/en-us/articles/35807665049369))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `ELAST`

<!-- /om-fields -->


---

## 6. `/db/TDMT`

> **Time Dependent Material – Creep/Shrinkage** — 코드 기반 크리프/건조수축 재료 특성을 정의합니다. CEB-FIP(2010/1990/1978), ACI, KDS 등 다양한 국제/국내 코드를 지원합니다.

- **URL**: `{base url}/db/TDMT`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Time Dependent Material Properties - Creep/Shrinkage ↗](https://support.midasuser.com/hc/en-us/articles/35808006330009)

### JSON Schema

```json
{
  "TDMT": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":       { "description": "Material Name",       "type": "string" },
      "CODE":       { "description": "Code Name",           "type": "string" },
      "STR":        { "description": "Compression Strength","type": "number" },
      "HU":         { "description": "Relative Humidity",  "type": "number" },
      "MSIZE":      { "description": "Notional Size",       "type": "number" },
      "CTYPE":      { "description": "Cement Type",         "type": "string" },
      "AGE":        { "description": "Concrete Age",        "type": "number" },
      "VOL":        { "description": "Volume/Surface Ratio","type": "number" },
      "CMETHOD":    { "description": "Curing Method",       "type": "string" },
      "TYPEOFAFFR": { "description": "Type of Aggregate",   "type": "integer" }
    }
  }
}
```

### Specifications (공통 키 + CEB-FIP)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Time Dependent Material Name | `"NAME"` | String | - | **Required** |
| 2 | Code Name ¹⁾ | `"CODE"` | String | - | **Required** |
| 3 | Compression Strength | `"STR"` | Number | - | **Required** |
| 4 | Relative Humidity (CEB-FIP 2010/1990: 40~99%; 1978: 40~100%) | `"HU"` | Number | - | **Required** |
| 5 (CEB-FIP) | Notional Size of Member | `"MSIZE"` | Number | - | **Required** |
| 6 | Type of Cement ²⁾ | `"CTYPE"` | String | `"RS"` | Optional |
| 7 | Concrete Age | `"AGE"` | Number | - | **Required** |
| 8 (CEB-FIP 2010) | Type of Aggregate • 0: Basalt/dense limestone • 1: Quartzite • 2: Limestone • 3: Sandstone | `"TYPEOFAFFR"` | Integer | 0 | Optional |
| 5 (ACI) | Volume/Surface Ratio | `"VOL"` | Number | - | **Required** |
| 7 (ACI) | Curing Method • Moist: `"MOIST"` • Steam: `"STEAM"` | `"CMETHOD"` | String | `"MOIST"` | Optional |

#### ¹⁾ Code Name 코드표 (`TDMT.CODE`)

| 표시명 | `"CODE"` |
| --- | --- |
| CEB-FIP (2010) | `"CEB_FIP_2010"` |
| CEB-FIP (1990) | `"CEB"` |
| CEB-FIP (1978) | `"CEB_FIP_1978"` |
| ACI | `"ACI"` |
| PCA | `"PCA"` |
| Combined (ACI & PCA) | `"COMBINED"` |
| AASHTO | `"AASHTO"` |
| JAPAN (JSCE2012) | `"JSCE_12"` |
| JAPAN (JSCE2007) | `"JSCE_07"` |
| Japanese Standard | `"JAPAN"` |
| JAPAN (JSCE) | `"JSCE"` |
| INDIA (IRC:112-2020) | `"INDIA_IRC_112_2020"` |
| INDIA (IRC:18-2000) | `"INDIA_IRC_18_2000"` |
| INDIA (IRC:112-2011) | `"INDIA_IRC_112_2011"` |
| European | `"EUROPEAN"` |
| AS 5100.5-2017 Amd 2:2024 | `"AS_2017_AMD_2024"` |
| AS 5100.5-2017 | `"AS_5100_5_2017"` |
| AS 5100.5-2016 | `"AS_5100_5_2016"` |
| AS/RTA 5100.5-2011 | `"AS_RTA_5100_5_2011"` |
| AS 3600-2018 Amd 2:2021 | `"AS_2018_AMD_2021"` |
| AS 3600-2009 | `"AS_3600_2009"` |
| NZ Bridge (SP/M/022 Amd 4:2022) | `"NEWZEALAND_2022"` |
| NZ Bridge (SP/M/022) | `"NEWZEALAND"` |
| Russian | `"RUSSIAN"` |
| Chinese Standard | `"CHINESE"` |
| China (JTG D62-2004) | `"JTG"` |
| China (JTG3362-2018) | `"CHINA_JTG3362_2018"` |
| China (JTG/T D65-06-2015) | `"CHJTG_T_D65_2015"` |
| **KDS-2016** | **`"KDS_2016"`** |
| KCI-USD12 | `"KSI_USD12"` |
| KSCE 2010 | `"KSCE_2010"` |
| Korea Standard | `"KS"` |
| User Defined | `"USER_DEFINED"` |

> ⚠️ **2026-08-25 재확인 보강:** 코드표에 누락돼 있던 5개 항목(`INDIA_IRC_112_2020`,
> `AS_2017_AMD_2024`, `AS_2018_AMD_2021`, `NEWZEALAND_2022`, `CHJTG_T_D65_2015`)을
> 원문(아티클 id `35808006330009`) 대조로 추가했다.
>
> ⚠️ **2026-07-25 정정:** `CODE` 값은 `"KDS2016"`(구분자 없음)이 아니라 **`"KDS_2016"`**(언더스코어)입니다.
> 이전 버전 문서와 아래 예제가 잘못 표기되어 있었습니다. 공식 아티클의 Request Examples
> (`"KDS-2016, KCI-USD12, KSCE 2010, Korea Standard"` 예제)에서 실제 페이로드로 확인했습니다.
> `/db/TDME`(§7)의 동일 계열 필드 `CODENAME`은 이와 달리 `"KDS-2016"`(하이픈)을 쓰므로
> 혼동하지 마십시오 — 두 엔드포인트가 같은 한국 기준에 서로 다른 리터럴을 씁니다.

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "KDS-2016",
      "CODE": "KDS_2016",
      "STR": 24000,
      "HU": 70,
      "MSIZE": 0.2,
      "CTYPE": "RS",
      "AGE": 28
    }
  }
}
```

### Python 예제

```python
# KDS 2016 코드 기반 크리프/수축 정의
tdmt_data = {
    "Assign": {
        "1": {
            "NAME": "Creep_C24_KDS",
            "CODE": "KDS_2016",  # 주의: 언더스코어 표기 (TDME의 CODENAME은 하이픈 "KDS-2016")
            "STR": 24000,        # 압축강도 (kPa)
            "HU": 70,            # 상대습도 (%)
            "MSIZE": 0.2,        # 부재 공칭 크기 (m)
            "CTYPE": "RS",       # 시멘트 종류: 보통
            "AGE": 28            # 타설 재령일 (days)
        }
    }
}
midas_api("POST", "/db/TDMT", tdmt_data)
```

<!-- om-fields:35808006330009 -->
**OM 원문 추가 필드 — Time Dependent Material Properties - Creep/Shrinkage ([35808006330009](https://support.midasuser.com/hc/en-us/articles/35808006330009))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 8 | [ACI] Concrete Compressive Strength Factor a · Range: 0.05 ~ 9.25 | `"CFACTA"` | Number | - | **Required** |
| 9 | Concrete Compressive Strength Factor b · Range: 0.67 ~ 0.98 | `"CFACTB"` | Number | - | **Required** |
| 10 | Material Factored Ultimate Value Type · ACI Code: "CODE" · User: "USER" | `"TYPE"` | String | "CODE" | Optional |
| 11 | [- When the Ultimate Value Type is CODE] Slump | `"SLUMP"` | Number | - | **Required** |
| 12 | Fine Aggregate Percentage | `"FAPERCENT"` | Number | - | **Required** |
| 13 | Air Content | `"AIRCONTENT"` | Number | - | **Required** |
| 14 | Cement Content | `"CEMCONTENT"` | Number | - | **Required** |
| 11 | [- When the Ultimate Value Type is USER] Creep Coefficient · Range: 1.3 ~ 4.15 | `"CREEPCOEFF"` | Number | - | **Required** |
| 12 | Shrinkage Strain · Range: 415 ~ 1070 (E-6) | `"SHRINKSTRAIN"` | Number | - | **Required** |
| 4 | [PCA] Ultimate Shrinkage Strain · Range: 500 ~ 800 (E-6) | `"USS"` | Number | - | **Required** |
| 5 | Ultimate Creep Strain · Range: 3 ~ 5 (1/fc*E-3) | `"UCS"` | Number | - | **Required** |
| 8 | Reinforcement Ratio of Cross Section of Column Segment | `"RR"` | Number | - | **Required** |
| 9 | Modulus of Elasticity of Steel | `"MOD"` | Number | - | **Required** |
| 6 | [Combined (ACI & PCA)] Material Factored Ultimate Creep Strain (E-6) | `"UCS"` | Number | - | **Required** |
| 7 | Volume-Surface Ratio for Creep Strain · ACI Code: "ACI" · PCA: "PCA" | `"VSR1"` | String | "ACI" | Optional |
| 8 | Loading Aged Factor · moist cured ACI Code: "MOIST" · steam cured ACI Code: "STEAM" · PCA: "PCA" | `"LAF"` | String | "MOIST" | Optional |
| 9 | Material Factored Ultimate Shrinkage Strain (E-6) | `"USS"` | Number | - | **Required** |
| 10 | Volume-Surface Ratio for Shrinkage Strain · ACI Code: "ACI" · PCA: "PCA" | `"VSR"` | String | "ACI" | Optional |
| 11 | Progress of Shrinkage with Time · moist cured ACI Code: "MOIST" · steam cured ACI Code: "STEAM" · PCA: "PCA" | `"PST"` | String | "MOIST" | Optional |
| 12 | Reinforced Concrete Effect by PCA | `"bRCE"` | Boolean | false | Optional |
| 13 | Reinforcement Ratio of Cross Section of Column Segment · When the "bRCE" is true | `"RR"` | Number | - | **Required** |
| 14 | Modulus of Elasticity of Steel · When the "bRCE" is true | `"MOD"` | Number | - | **Required** |
| 7 | [AASHTO] Expose to Drying before 5 Days of Curing | `"bEXPOSE"` | Boolean | False | Optional |
| 5 | [JAPAN (JSCE 2012, JSCE 2007, JSCE)] Cement Content · Range: 260 kg/m3 ~ 500 kg/m3 | `"CEMCONTENT"` | Number | - | **Required** |
| 6 | Water Content · Range: 130 kg/m3 ~ 230 kg/m3 | `"WATERCONTENT"` | Number | - | **Required** |
| 9 | [- Only for JAPAN (JSCE 2012)] Impact Factor by Cement Type and Mixture | `"IPFACT"` | Number | - | **Required** |
| 10 | Age of Concrete at the Beginning of Solidification | `"AGESOL"` | Number | - | **Required** |
| 9 | [- Only for JAPAN (JSCE 2007)] Alpha-Factor according to Cement Type · 11 or 15 | `"ALPHAFACT"` | Number | - | **Required** |
| 10 | Autogenous Shrinkage Option | `"bAUTO"` | Boolean | - | **Required** |
| 11 | Gamma-Factor · When the "bAUTO" is true | `"GAMMAFACT"` | Number | - | **Required** |
| 12 | a-Factor · When the "bAUTO" is true | `"AFACT"` | Number | - | **Required** |
| 13 | b-Factor · When the "bAUTO" is true | `"BFACT"` | Number | - | **Required** |
| 14 | General Shrinkage Option | `"bGEN"` | Boolean | - | **Required** |
| 4 | [Japanese Standard] Calculation Method For E · JSCE: "JSCE" · AIJ: "AIJ" | `"CM"` | String | - | **Required** |
| 5 | Relative Humidity Type · Curing Underwater: "CU" · Relative Humidity: "RH" | `"HTYPE"` | String | - | **Required** |
| 7 | Environmental Coefficient | `"LAMBDA"` | Number | - | **Required** |
| 7 | [European] Type of Code · EN 1992-1 (General Structure): 0 · EN 1992-2 (Concrete Bridge): 1 | `"TCODE"` | Integer | 0 | Optional |
| 8 | Silica Fume · When the "TCODE" is 1 | `"bSILICA"` | Boolean | false | Optional |
| 5 | [AS 5100.5-2017, AS 5100.5-2016, AS/RTA 5100.5-2011, AS 3600-2009, NZ Bridge(SP/M/022)] Type of Drying Basic Shrinkage Strain ³⁾ | `"iEPS_DRY"` | Integer | 0 | Optional |
| 6 | Drying Basic Shrinkage Strain ³⁾ | `"EPS_DRY"` | Number | - | **Required** |
| 8 | Relative Humidity Thickness · Only for NZ Bridge (SP/M/022) · Range: 0.20 ~ 0.72 | `"FS"` | Number | - | **Required** |
| 7 | [Russian] Curing Method · Natural cure: 0 · Steam cure: 1 | `"CMETH"` | Integer | 0 | Optional |
| 8 | Fast-Accumulating Creep | `"CREEP"` | Boolean | False | Optional |
| 9 | Concrete Type · Heavy concrete: 0 · Fine-grained concrete: 1 | `"CONCT"` | Integer | 0 | Optional |
| 10 | Water Content | `"W"` | Number | - | **Required** |
| 11 | Maximum Aggregate Size | `"MAXS"` | Number | - | **Required** |
| 12 | Air Content | `"A"` | Number | - | **Required** |
| 13 | Specific Content of the Cement Paste | `"PZ"` | Number | - | **Required** |
| 7 | [- Chinese Standard] Type of Relative Humidity · Curing Underwater: "CU" · Relative Humidity: "RH" | `"HTYPE"` | String | "CU" | Optional |
| 7 | [- China (JTG D62-2004)] Cement Type Coefficient | `"BSC"` | Number | - | **Required** |
| 8 | Amount of Added Fly Ash Alpha · Range : 0 ~ 30 | `"FLYASH"` | Number | - | **Required** |
| 8 | [KDS-2016, KCI-USD12, KSCE 2010, Korea Standard] Weight Density · Only for KDS-2016 | `"DENSITY"` | Number | - | **Required** |
| 3 | [User Defined] Shrinkage Strain Function Name | `"SSFNAME"` | String | - | **Required** |
| 4 | Creep Function · Insert the data as an object | `"vCREEP_AGE"` | Array [Object] | - | **Required** |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `EXPOSURE`, `US`, `iCTYPE`

<!-- /om-fields -->


---

## 7. `/db/TDME`

> **Time Dependent Material – Compressive Strength** — 콘크리트 압축강도의 시간 의존성을 정의합니다.

- **URL**: `{base url}/db/TDME`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Time Dependent Material Properties - Compressive Strength ↗](https://support.midasuser.com/hc/en-us/articles/35808102389401)

### JSON Schema

```json
{
  "TDME": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":     { "description": "Material Name",       "type": "string" },
      "TYPE":     { "description": "Code or User Type",   "type": "string" },
      "CODENAME": { "description": "Code Name",           "type": "string" },
      "STRENGTH": { "description": "Compression Strength","type": "number" },
      "A":        { "description": "Factor A",            "type": "number" },
      "B":        { "description": "Factor B",            "type": "number" },
      "iCTYPE":   { "description": "Cement Type",         "type": "integer" },
      "nAGGRE":   { "description": "Aggregate Type",      "type": "integer" }
    }
  }
}
```

### Specifications

> ⚠️ **2026-08-25 재확인 전면 정정.** 이전 버전은 `A`/`B`(Factor a, b) 그룹을 "ACI/KDS"로
> 묶어 **`KDS-2016`도 A/B 계수를 쓰는 것처럼 잘못 기재**하고 있었다. 원문(아티클 id
> `35808102389401`) 대조 결과 A/B 계수 그룹은 **`ACI`·`Korean Standard`**(CODENAME
> `"Korean Standard"`, 20번 — `KDS-2016`과는 다른 별개 코드)이며, **`KDS-2016`은 실제로는
> `iCTYPE`(Cement Type) + `DENSITY`(Weight Density) 그룹**(`GILBERT AND RANZI`와 동일 구조)에
> 속한다. 한국 사용자가 가장 많이 쓸 코드에서 필수 필드가 틀려 있던 것이라 전체 표를
> 코드 그룹별로 다시 작성했다.

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Material Name | `"NAME"` | String | - | **Required** |
| 2 | Material Type · Code: `"CODE"` / User: `"USER"` | `"TYPE"` | String | - | **Required** |
| 3 (TYPE=CODE) | Code Name ¹⁾ | `"CODENAME"` | String | - | **Required** |
| 4 (TYPE=CODE) | Compression Strength | `"STRENGTH"` | Number | - | **Required** |

공통 4개 필드만으로 끝나는 코드: `INDIA(IRC:18-2000)` · `CEB-FIP(1978)` · `AS 5100.5-2017` ·
`AS 5100.5-2016` · `AS/RTA 5100.5-2011` · `AS 3600-2009`.

#### `ACI`, `Korean Standard` 전용 추가 필드

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Factor, a | `"A"` | Number | - | **Required** |
| 6 | Factor, b | `"B"` | Number | - | **Required** |

#### `CEB-FIP(1990)` · `Ohzagi` · `European` · `INDIA(IRC:112-2011)` · `KCI-USD12` 전용 추가 필드

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |

#### `CEB-FIP(2010)` · `INDIA(IRC:112-2020)` 전용 추가 필드

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |
| 6 | Aggregate Type · Basalt/dense limestone: `0` / Quartzite: `1` / Limestone: `2` / Sandstone: `3` | `"nAGGRE"` | Integer | - | **Required** |

#### `Russian` 전용 추가 필드

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |
| 6 | Curing Method · Natural Cure: `0` / Steam Cure: `1` | `"CMETH"` | Integer | - | **Required** |
| 7 | Concrete Type · Heavy Concrete: `0` / Fine-Grained Concrete: `1` | `"CTYPE"` | Integer | - | **Required** |
| 8 | Maximum Aggregate Size | `"MAXS"` | Number | - | **Required** |
| 9 | Specific Content of the Cement Paste | `"PZ"` | Number | - | **Required** |

> ⚠️ 이 그룹의 `"CTYPE"`(Concrete Type, Integer)는 최상위 `"TYPE"`(Code/User 구분, String)과
> 이름이 겹치지만 다른 필드다. 원문 그대로 옮겼다.

#### `GILBERT AND RANZI`, **`KDS-2016`** 전용 추가 필드

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |
| 6 | Weight Density | `"DENSITY"` | Number | - | **Required** |

#### `Japan (Hydration)` 전용 추가 필드

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Tensile Strength Factor | `"TENS_STRN_FACTOR"` | Number | - | **Required** |
| 6 | Use Concrete Data Option | `"bUSE"` | Boolean | `false` | Optional |
| 7 (bUSE=false) | Factor, a | `"A"` | Number | - | **Required** |
| 8 (bUSE=false) | Factor, b | `"B"` | Number | - | **Required** |
| 9 (bUSE=false) | Factor, d | `"D"` | Number | - | **Required** |
| 7 (bUSE=true) | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |

#### `Japan (Elastic)` 전용 추가 필드

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Elastic Cement Type · Normal Type: `0` / Rapid Type: `1` | `"iECTYPE"` | Integer | - | **Required** |

#### `TYPE = "USER"` (User Defined) 전용 필드

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Scale Factor | `"SCALE"` | Number | - | **Required** |
| 6 | Function Data (Array of `{TIME, COMP, TENS, ELAST}`) | `"SCALE"` | Array [Object] | - | **Required** |
| (1) | Time (day) | `"TIME"` | Number | - | **Required** |
| (2) | Compression Strength | `"COMP"` | Number | - | **Required** |
| (3) | Tensile Strength | `"TENS"` | Number | - | **Required** |
| (4) | Elastic Modulus | `"ELAST"` | Number | - | **Required** |

> ⚠️ 원문 Specifications 표가 "Scale Factor"(Number)와 "Function Data"(Array[Object]) 두
> 필드 모두에 Key `"SCALE"`을 중복 표기하고 있다. 오타로 보이나 실제 키 이름이 무엇인지
> 확인할 예제가 없어 원문 그대로 옮기고 이 주석으로 남긴다.

#### ¹⁾ Code Name 코드표 (`TDME.CODENAME`)

| No. | 표시명 | `"CODENAME"` |
| --- | --- | --- |
| 1 | ACI | `"ACI"` |
| 2 | CEB-FIP (2010) | `"CEB-FIP(2010)"` |
| 3 | CEB-FIP (1990) | `"CEB-FIP(1990)"` |
| 4 | Ohzagi | `"Ohzagi"` |
| 5 | European | `"European"` |
| 6 | INDIA (IRC:18-2000) | `"INDIA(IRC:18-2000)"` |
| 7 | CEB-FIP (1978) | `"CEB-FIP(1978)"` |
| 8 | AS 5100.5-2017 | `"AS 5100.5-2017"` |
| 9 | AS 5100.5-2016 | `"AS 5100.5-2016"` |
| 10 | AS/RTA 5100.5-2011 | `"AS/RTA 5100.5-2011"` |
| 11 | AS 3600-2009 | `"AS 3600-2009"` |
| 12 | INDIA (IRC:112-2011) | `"INDIA(IRC:112-2011)"` |
| 13 | INDIA (IRC:112-2020) | `"INDIA(IRC:112-2020)"` |
| 14 | Russian | `"Russian"` |
| 15 | GILBERT AND RANZI | `"GILBERT AND RANZI"` |
| 16 | Japan (Hydration) | `"Japan(hydration)"` |
| 17 | Japan (Elastic) | `"Japan(elastic)"` |
| 18 | **KDS-2016** | **`"KDS-2016"`** |
| 19 | KCI-USD12 | `"KCI-USD12"` |
| 20 | Korean Standard | `"Korean Standard"` |

> ⚠️ **2026-07-25 정정:** `CODENAME` 값은 `"KDS2016"`(구분자 없음)이 아니라 **`"KDS-2016"`**(하이픈)입니다.
> 이전 버전 문서와 아래 예제가 잘못 표기되어 있었습니다. `/db/TDMT`(§6)의 `CODE` 필드는 같은
> 한국 기준을 언더스코어 표기 `"KDS_2016"`으로 쓰므로, 두 엔드포인트의 표기가 서로 다릅니다 —
> 엔드포인트별로 정확한 리터럴을 확인하십시오.

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "TDME_KDS2016",
      "TYPE": "CODE",
      "CODENAME": "KDS-2016",
      "STRENGTH": 30000,
      "iCTYPE": 1,
      "DENSITY": 230
    }
  }
}
```

> ⚠️ `KDS-2016`은 `STRENGTH`만으로는 완성되지 않는다 — `iCTYPE`(Cement Type)과
> `DENSITY`(Weight Density)가 함께 **Required**다. 위 예제는 원문 Request Example
> (아티클 id `35808102389401`)의 실제 페이로드를 그대로 옮긴 것이다.

### Python 예제

```python
tdme_data = {
    "Assign": {
        "1": {
            "NAME": "CompStr_C24_KDS",
            "TYPE": "CODE",
            "CODENAME": "KDS-2016",  # 주의: 하이픈 표기 (TDMT의 CODE는 언더스코어 "KDS_2016")
            "iCTYPE": 1,   # Cement Type (KDS-2016은 STRENGTH만으로 부족 — iCTYPE/DENSITY 필수)
            "DENSITY": 230,  # Weight Density
            "STRENGTH": 24000
        }
    }
}
midas_api("POST", "/db/TDME", tdme_data)
```

<!-- om-fields:35808102389401 -->
**OM 원문 추가 필드 — Time Dependent Material Properties - Compressive Strength ([35808102389401](https://support.midasuser.com/hc/en-us/articles/35808102389401))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `aDATA`

<!-- /om-fields -->


---

## 8. `/db/EDMP`

> **Change Property** — 요소별 시간 의존 재료 특성(공칭 크기 또는 체적/표면적 비)를 변경합니다.

- **URL**: `{base url}/db/EDMP`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Change Property ↗](https://support.midasuser.com/hc/en-us/articles/35808245801881)

### JSON Schema

```json
{
  "EDMP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "TYPE": { "description": "TYPE",   "type": "string" },
      "H_VS": { "description": "H (VS)", "type": "number" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Change Property Method • Notional Size: `"NSM"` • Volume/Surface Ratio: `"VSR"` | `"TYPE"` | String | - | **Required** |
| 2 | Change Property Value (h for NSM, v/s for VSR) | `"H_VS"` | Number | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "10": { "TYPE": "NSM", "H_VS": 0.10 },
    "20": { "TYPE": "VSR", "H_VS": 0.15 }
  }
}
```

### Python 예제

```python
# 특정 요소들의 공칭 크기 변경
edmp_data = {
    "Assign": {
        "101": {"TYPE": "NSM", "H_VS": 0.20},
        "102": {"TYPE": "NSM", "H_VS": 0.20},
        "103": {"TYPE": "NSM", "H_VS": 0.30}
    }
}
midas_api("POST", "/db/EDMP", edmp_data)
```

---

## 9. `/db/TMAT`

> **Time Dependent Material Link** — 재료에 시간 의존 특성(크리프/건조수축 + 압축강도)을 링크합니다.

- **URL**: `{base url}/db/TMAT`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Time Dependent Material Link ↗](https://support.midasuser.com/hc/en-us/articles/35808280891033)

### JSON Schema

```json
{
  "TMAT": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "TDMT_NAME": { "description": "TDM-TYPE1 (CREEP/SHRINKAGE)", "type": "string" },
      "TDME_NAME": { "description": "TDM-TYPE2 (ELASTICITY)",      "type": "string" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Creep/Shrinkage Name | `"TDMT_NAME"` | String | - | **Required** |
| 2 | Comp. Strength Name | `"TDME_NAME"` | String | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "2": {
      "TDMT_NAME": "KDS2016",
      "TDME_NAME": "KDS2016"
    }
  }
}
```

### Python 예제

```python
# 재료 2번에 시간 의존 특성 링크
tmat_data = {
    "Assign": {
        "2": {
            "TDMT_NAME": "Creep_C24_KDS",   # /db/TDMT에서 정의한 이름
            "TDME_NAME": "CompStr_C24_KDS"  # /db/TDME에서 정의한 이름
        }
    }
}
midas_api("POST", "/db/TMAT", tmat_data)
```

---

## 10. `/db/EPMT`

> **Plastic Material** — 소성 재료 모델을 정의합니다. Tresca, Von-Mises, Mohr-Coulomb, Drucker-Prager, Masonry, Concrete Damage 등 6가지 모델을 지원합니다.

- **URL**: `{base url}/db/EPMT`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Plastic Material ↗](https://support.midasuser.com/hc/en-us/articles/35808376517913)

### JSON Schema

```json
{
  "EPMT": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":       { "description": "Name",       "type": "string" },
      "MODEL_TYPE": { "description": "Model Type", "type": "string" },
      "TRESCA":     { "description": "Tresca",     "type": "object" },
      "VMISES":     { "description": "Von Mises",  "type": "object" },
      "MOHRCL":     { "description": "Mohr-Coulomb","type": "object" },
      "DRUCKER":    { "description": "Drucker-Prager","type": "object" },
      "MASONRY":    { "description": "Masonry",    "type": "object" },
      "CONCDMG":    { "description": "Concrete Damage","type": "object" }
    }
  }
}
```

> ⚠️ **2026-08-25 재확인 보강.** 이전 버전은 `MODEL_TYPE`이 `"DP"`(Drucker-Prager)·`"MA"`
> (Masonry)·`"DM"`(Concrete Damage)일 때 필요한 `DRUCKER`/`MASONRY`/`CONCDMG` 객체 구조가
> 통째로 빠져 있었다. 또 Tresca/Von-Mises/Mohr-Coulomb 공통 파라미터 중 `HARDENING_COEF`가
> 실제로는 **Required**(원문 기준, `OPT_HARDENING`이 기본값 `0`=Activated일 때)인데 이전
> 버전은 Optional로 잘못 기재했었다. 원문(아티클 id `35808376517913`) 재대조로 전면 보강.

### Specifications

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Plastic Material Name | `"NAME"` | String | - | **Required** |
| 2 | Model Type · `"TR"`(Tresca) / `"VM"`(Von-Mises) / `"MC"`(Mohr-Coulomb) / `"DP"`(Drucker-Prager) / `"MA"`(Masonry) / `"DM"`(Concrete Damage) | `"MODEL_TYPE"` | String | - | **Required** |

#### Tresca / Von-Mises 공통 파라미터 (`"TRESCA"` or `"VMISES"` object)

| Key | Description | Default | Required |
| --- | --- | --- | --- |
| `"INIT_YIELD_STRESS"` | Initial Uniaxial Yield Stress | - | **Required** |
| `"OPT_HARDENING"` | Hardening Option · Activated: `0` / Inactivated: `1` | `0` | Optional |
| `"HARDENING_TYPE"` | (`OPT_HARDENING`=0일 때만) `"ISO"` / `"KIN"` / `"MIX"` | `"ISO"` | Optional |
| `"HARDENING_COEF"` | (`OPT_HARDENING`=0일 때) Hardening Coefficient | - | **Required** |
| `"BACK_STRESS_COEF"` | (`HARDENING_TYPE`=`"MIX"`일 때) Back Stress Coefficient | - | **Required** |

#### Mohr-Coulomb / Drucker-Prager 공통 파라미터 (`"MOHRCL"` or `"DRUCKER"` object)

| Key | Description | Default | Required |
| --- | --- | --- | --- |
| `"INIT_COHESION"` | Initial Cohesion | - | **Required** |
| `"INIT_FRIC_ANGLE"` | Initial Friction Angle (deg) | - | **Required** |
| `"OPT_HARDENING"` | Hardening Option · Activated: `0` / Inactivated: `1` | `0` | Optional |
| `"HARDENING_TYPE"` | (`OPT_HARDENING`=0일 때만) `"ISO"` / `"KIN"` / `"MIX"` | `"ISO"` | Optional |
| `"HARDENING_COEF"` | (`OPT_HARDENING`=0일 때) Hardening Coefficient | - | **Required** |
| `"BACK_STRESS_COEF"` | (`HARDENING_TYPE`=`"MIX"`일 때) Back Stress Coefficient | - | **Required** |

#### Masonry 파라미터 (`"MASONRY"` object)

Brick(`"BM"`)·Bed Joint(`"BED_JOINT"`)·Head Joint(`"HEAD_JOINT"`) 3개 재료 object가 각각
아래와 동일한 하위 구조를 가짐(모두 **Required**):

| Key | Description |
| --- | --- |
| `"YOUNG_S_MODULUS"` | Young's Modulus |
| `"POSSIONS_S_RATIO"` | Poisson's Ratio |
| `"TENSION_STRENGTH"` | Tensile Strength |
| `"SOFTENING_PARAMETER"`(BM) / `"HARDENING_PARAM"`(BED_JOINT·HEAD_JOINT) | Stiffness Reduction Factor |

여기에 형상 정보 object `"GEOM"`이 추가로 필요(**Required**):

| Key | Description | Required |
| --- | --- | --- |
| `"BRICK_LENGTH"` | Brick Length | **Required** |
| `"BRICK_HEIGHT"` | Brick Height | **Required** |
| `"THICKNESS_BED"` | Thickness of Bed | **Required** |
| `"THICKNESS_HEAD"` | Thickness of Head | **Required** |
| `"COORD_TYPE"` | Material Coordinate System(수직/수평) · Global-Y/Global-X: `0` / Local-y/Local-z: `-1` / Global-Z/Angle: `-4` | **Required** |
| `"COORD_ANGLE"` | (`COORD_TYPE`=`-4`일 때) Global X축 기준 각도 | **Required** |

#### Concrete Damage 파라미터 (`"CONCDMG"` object)

| Key | Description | Required |
| --- | --- | --- |
| `"DILIATION_ANGLE"` | Dilation Angle | **Required** |
| `"ECCEN"` | Eccentricity | **Required** |
| `"FBO_FCO"` | fbo/fco | **Required** |
| `"K"` | K | **Required** |
| `"VISCOSITY_PARAM"` | Viscosity Parameter | **Required** |
| `"COMP_ITEMS"` | Compressive Behavior — Array of `{INELASTIC_STRAIN, YIELD_STRESS, DAMAGE}` | **Required** |
| `"TENSILE_ITEMS"` | Tensile Behavior — Array of `{INELASTIC_STRAIN, YIELD_STRESS, DAMAGE}` | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "Steel_VonMises",
      "MODEL_TYPE": "VM",
      "VMISES": {
        "INIT_YIELD_STRESS": 235000,
        "OPT_HARDENING": 0,
        "HARDENING_TYPE": "ISO",
        "HARDENING_COEF": 21000
      }
    }
  }
}
```

### Python 예제

```python
epmt_data = {
    "Assign": {
        "1": {
            "NAME": "Steel_VM",
            "MODEL_TYPE": "VM",
            "VMISES": {
                "INIT_YIELD_STRESS": 235000,
                "OPT_HARDENING": 0,
                "HARDENING_TYPE": "ISO",
                "HARDENING_COEF": 21000
            }
        }
    }
}
midas_api("POST", "/db/EPMT", epmt_data)
```

<!-- om-fields:35808376517913 -->
**OM 원문 추가 필드 — Plastic Material ([35808376517913](https://support.midasuser.com/hc/en-us/articles/35808376517913))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `BOND_WRENCH_STRENGTH`, `COMP_STRENGTH`, `FRICTION_ANGLE`, `MICROPL`, `MU`, `PARAM_C`, `PARAM_K`, `V1`, `V2`, `V3`, `V4`, `V5`, `V6`, `V7`

<!-- /om-fields -->


---

## 11. `/db/EPMT-M1`

> **Plastic Material (Hyper-S)** — Hyper-S 전용 소성 재료 모델.

- **URL**: `{base url}/db/EPMT-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Plastic Material (Hyper-S) ↗](https://support.midasuser.com/hc/ko/articles/56511025581337)

```python
result = midas_api("GET", "/db/EPMT-M1")
```

<!-- om-fields:56511025581337 -->
**OM 원문 추가 필드 — Plastic Material ([56511025581337](https://support.midasuser.com/hc/en-us/articles/56511025581337))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 2 | Model · Tresca: 0 · Von Mises: 1 · Mohr-Coulomb: 2 · Drucker-Prager: 3 · Masonry: 4 · Concrete-Damage: 5 | `"MODEL_TYPE"` | integer (enum) | - | **Required** |
| 3 | [When MODEL_TYPE = 0] Tresca parameters | `"TRESCA"` | object | - | **Required** |
| (1) | Initial Uniaxial Yield Stress | `"INIT_YIELD_STRESS"` | number | - | **Required** |
| (2) | Hardening | `"OPT_HARDENING"` | boolean | false | Optional |
| (3) | [When OPT_HARDENING = true] Isotropic / Kinematic / Mixed · Isotropic: 0 · Kinematic: 1 · Mixed: 2 | `"HARDENING_TYPE"` | integer (enum) | - | **Required** |
| (4) | Hardening Coefficient | `"HARDENING_COEF"` | number | - | **Required** |
| (5) | Back Stress Coefficient When HARDENING_TYPE = 2 | `"BACK_STRESS_COEF"` | number | - | **Required** |
| 4 | [When MODEL_TYPE = 1] Von Mises parameters | `"VMISES"` | object | - | **Required** |
| 5 | [When MODEL_TYPE = 2] Mohr-Coulomb parameters | `"MOHRCL"` | object | - | **Required** |
| (1) | Initial Cohesion | `"INIT_COHESION"` | number | - | **Required** |
| (2) | Initial Friction Angle | `"INIT_FRIC_ANGLE"` | number | - | **Required** |
| (3) | Hardening | `"OPT_HARDENING"` | boolean | false | Optional |
| (4) | Back Stress Coefficient When OPT_HARDENING = true, HARDENING_TYPE = 2 | `"BACK_STRESS_COEF"` | number | - | Optional |
| (5) | [When OPT_HARDENING = true] Isotropic / Kinematic / Mixed · Isotropic: 0 | `"HARDENING_TYPE"` | integer (enum) | - | **Required** |
| (6) | Hardening Coefficient | `"HARDENING_COEF"` | number | - | **Required** |
| 6 | [When MODEL_TYPE = 3] Drucker-Prager parameters | `"DRUCKER"` | object | - | **Required** |
| 7 | [When MODEL_TYPE = 4] Masonry parameters | `"MASONRY"` | object | - | **Required** |
| (1) | Brick Material / Properties | `"BM"` | object | - | **Required** |
| (2) | Bed Joint / Properties | `"BED_JOINT"` | object | - | **Required** |
| (3) | Head Joint / Properties | `"HEAD_JOINT"` | object | - | **Required** |
| (4) | Geometry / Properties | `"GEOM"` | object | - | **Required** |
| (5) | Material Coordinate System | `"MAT_COORD"` | object | - | **Required** |
| a | Material Coordinate System / Vertical : Horizontal · Global: 0 · Element Local: 1 · Global-Z : Angle: 2 | `"COORD_TYPE"` | integer (enum) | - | **Required** |
| b | Angle from Global X When COORD_TYPE = 2 | `"COORD_ANGLE"` | number | - | **Required** |
| 8 | [When MODEL_TYPE = 5] Concrete Damage parameters | `"CONCDMG"` | object | - | **Required** |
| (1) | Diliation Angle | `"DILIATION_ANGLE"` | number | - | **Required** |
| (2) | Eccentricity | `"ECCEN"` | number | - | **Required** |
| (3) | fbo/fco | `"FBO_FCO"` | number | - | **Required** |
| (4) | K | `"K"` | number | - | **Required** |
| (5) | Viscosity Parameter | `"VISCOSITY_PARAM"` | number | - | **Required** |
| (6) | Compressive Behavior / Strain-Yield Stress... | `"COMP_ITEMS"` | array [object] | - | **Required** |
| a | Inelastic Strain | `"INELASTIC_STRAIN"` | number | - | **Required** |
| b | Yield Stress | `"YIELD_STRESS"` | number | - | **Required** |
| c | Damage | `"DAMAGE"` | number | - | **Required** |
| (7) | Tensile Behavior / Strain-Yield Stress... | `"TENSILE_ITEMS"` | array [object] | - | **Required** |
| (1) | Brick Material / Properties... | `"BM"` | object | - | **Required** |
| a | Young's Modulus | `"YOUNG_S_MODULUS"` | number | - | **Required** |
| b | Poisson's Ratio | `"POSSIONS_S_RATIO"` | number | - | **Required** |
| c | Stiffness Reduction Factor | `"TENSION_STRENGTH"` | number | - | **Required** |
| d | Comp. Strength, fc | `"STIFF_REDUCTION"` | number | - | **Required** |
| (2) | Bed Joint / Properties... | `"BED_JOINT"` | object | - | **Required** |
| c | Tensile Strength, ft | `"TENSION_STRENGTH"` | number | - | **Required** |
| d | Stiffness Reduction Factor | `"STIFF_REDUCTION"` | number | - | **Required** |
| (3) | Head Joint / Properties... | `"HEAD_JOINT"` | object | - | **Required** |
| (4) | Geometry / Properties... | `"GEOM"` | object | - | **Required** |
| a | Brick Length | `"BRICK_LENGTH"` | number | - | **Required** |
| b | Brick Height | `"BRICK_HEIGHT"` | number | - | **Required** |
| c | Thickness of Bed Joint | `"THICKNESS_BED"` | number | - | **Required** |
| d | Thickness of Head Joint | `"THICKNESS_HEAD"` | number | - | **Required** |

<!-- /om-fields -->


---

## 12. `/db/SECT`

> **Section Properties** — 단면 특성을 정의합니다. `SECTTYPE` 값에 따라 DB/User, Value, SRC, Combined, PSC, Tapered, Composite, Steel Girder 등 다양한 서브타입을 지원합니다.

- **URL**: `{base url}/db/SECT`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Properties - Common ↗](https://support.midasuser.com/hc/en-us/articles/35808653964185)

### SECTTYPE 코드표

| SECTTYPE | 설명 |
|----------|------|
| `"DBUSER"` | DB / User 정의 단면 |
| `"VALUE"` | 직접 값 입력 단면 |
| `"SRC"` | SRC (Steel-Reinforced Concrete) 합성 단면 |
| `"COMBINED"` | 조합 단면 |
| `"PSC"` | PSC (Prestressed Concrete) 단면 |
| `"TAPERED"` | 변단면 (테이퍼) |
| `"COMPOSITE"` | 강-콘크리트 합성 단면 (PSC 또는 Steel) |
| `"SOD"` | 강거더 (Steel Girder) |

### JSON Schema (공통)

```json
{
  "SECT": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "SECTTYPE":   { "description": "Type",        "type": "string" },
      "SECT_NAME":  { "description": "Sect Name",   "type": "string" },
      "SECT_BEFORE":{ "description": "Sect Before", "type": "object",
        "properties": {
          "SHAPE":              { "type": "string" },
          "OFFSET_PT":          { "type": "string" },
          "OFFSET_CENTER":      { "type": "integer" },
          "HORZ_OFFSET_OPT":    { "type": "integer" },
          "VERT_OFFSET_OPT":    { "type": "integer" },
          "USERDEF_OFFSET_YI":  { "type": "number" },
          "USERDEF_OFFSET_ZI":  { "type": "number" },
          "USE_SHEAR_DEFORM":   { "type": "boolean" },
          "USE_WARPING_EFFECT": { "type": "boolean" }
        }
      }
    }
  }
}
```

### 공통 Specifications (모든 SECTTYPE 공통)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Section Data Type | `"SECTTYPE"` | String | - | **Required** |
| 2 | Section Name | `"SECT_NAME"` | String | - | **Required** |
| 3 | Section Data (Before Stage) | `"SECT_BEFORE"` | Object | - | **Required** |
| (1) | Section Shape ²⁾ | `"SHAPE"` | String | - | **Required** |
| (2) | Offset Direction | `"OFFSET_PT"` | String | `"CC"` | Optional |
| (3) | Center Location (0: Centroid, 1: Center of Section) | `"OFFSET_CENTER"` | Integer | 0 | Optional |
| (4) | Horizontal Offset Option (0: Extreme Fiber, 1: User) | `"HORZ_OFFSET_OPT"` | Integer | 0 | Optional |
| (5) | Horizontal Offset Value (I-end) | `"USERDEF_OFFSET_YI"` | Number | 0 | Optional |
| (6) | Horizontal Offset Value (J-end, Tapered only) | `"USERDEF_OFFSET_YJ"` | Number | 0 | Optional |
| (7) | Vertical Offset Option | `"VERT_OFFSET_OPT"` | Integer | 0 | Optional |
| (8) | Vertical Offset Value (I-end) | `"USERDEF_OFFSET_ZI"` | Number | 0 | Optional |
| (9) | Vertical Offset Value (J-end, Tapered only) | `"USERDEF_OFFSET_ZJ"` | Number | 0 | Optional |
| (10) | User Type Offset Reference (0: Centroid, 1: Extreme Fiber) | `"USER_OFFSET_REF"` | Integer | 0 | Optional |
| (11) | Consider Shear Deformation | `"USE_SHEAR_DEFORM"` | Boolean | false | Optional |
| (12) | Consider Warping Effect | `"USE_WARPING_EFFECT"` | Boolean | false | Optional |

#### Offset Direction 코드표

| Code | Position |
|------|----------|
| `"LT"` | Left-Top |
| `"CT"` | Center-Top |
| `"RT"` | Right-Top |
| `"LC"` | Left-Center |
| `"CC"` | Center-Center |
| `"RC"` | Right-Center |
| `"LB"` | Left-Bottom |
| `"CB"` | Center-Bottom |
| `"RB"` | Right-Bottom |

---

### 12-A. SECT — DB/User (`"SECTTYPE": "DBUSER"`)

- **Source**: [Section Properties - DB/User ↗](https://support.midasuser.com/hc/en-us/articles/35809067039513)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| (1) | Data Type • DB: 1 • User: 2 | `"DATATYPE"` | Integer | - | **Required** |
| (2) | Section Specifications | `"SECT_I"` | Object | - | **Required** |
| DB | DB Name | `"DB_NAME"` | String | - | **Required** |
| DB | Section Name of DB | `"SECT_NAME"` | String | - | **Required** |
| User | Dimension of Section | `"vSIZE"` | Array[Number] | - | **Required** |

```json
{
  "Assign": {
    "1": {
      "SECTTYPE": "DBUSER",
      "SECT_NAME": "H300x150",
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
        "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
        "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": true,
        "SHAPE": "H",
        "DATATYPE": 1,
        "SECT_I": { "DB_NAME": "KS21", "SECT_NAME": "H300x150x6.5/9" }
      }
    }
  }
}
```

---

### 12-B. SECT — Value (`"SECTTYPE": "VALUE"`)

- **Source**: [Section Properties - Value ↗](https://support.midasuser.com/hc/en-us/articles/35839753881497)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Calculation Options | `"CALC_OPT"` | Boolean | true | Create Only |
| (1) | Dimension of Section ³⁾ | `"vSIZE"` | Array[Number] | - | **Required** |

```json
{
  "Assign": {
    "101": {
      "SECTTYPE": "VALUE",
      "SECT_NAME": "H_User",
      "CALC_OPT": true,
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
        "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
        "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": true,
        "SHAPE": "H",
        "SECT_I": {
          "vSIZE": [0.30, 0.15, 0.0065, 0.009, 0, 0, 0, 0]
        }
      }
    }
  }
}
```

---

### 12-C. SECT — SRC (`"SECTTYPE": "SRC"`)

- **Source**: [Section Properties - SRC ↗](https://support.midasuser.com/hc/en-us/articles/35845378225689)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| (1) | SRC Type • DB: 1 • User: 2 | `"SRC_TYPE"` | Integer | - | **Required** |
| (3) | E Ratio (Steel/Concrete) | `"MATL_ELAST"` | Number | - | **Required** |
| (4) | Density Ratio | `"MATL_DENS"` | Number | - | **Required** |
| (5) | Poisson's Ratio (Steel) | `"MATL_POIS_S"` | Number | - | **Required** |
| (6) | Poisson's Ratio (Concrete) | `"MATL_POIS_C"` | Number | - | **Required** |
| (7) | Stiffness Reduction Factor (Concrete) | `"MATL_STIF_FACTOR"` | Number | - | **Required** |
| (9) DB | Steel Section (DB/User) | `"SECT_I"` | Object | - | **Required** |
| (10) | Concrete Dimensions | `"SECT_J"` | Object | - | **Required** |

```json
{
  "Assign": {
    "201": {
      "SECTTYPE": "SRC",
      "SECT_NAME": "SRC_H300",
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
        "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
        "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": false,
        "SHAPE": "RBO",
        "SRC_TYPE": 1,
        "MATL_ELAST": 7.69, "MATL_DENS": 2.94,
        "MATL_POIS_S": 0.3, "MATL_POIS_C": 0.18,
        "MATL_STIF_FACTOR": 1.0,
        "SECT_I": { "DB_NAME": "KS21", "SECT_NAME": "B400x400x12" },
        "SECT_J": { "vSIZE": [0.06, 0.065] }
      }
    }
  }
}
```

---

### 12-D. SECT — PSC (`"SECTTYPE": "PSC"`)

- **Source**: [Section Properties - PSC ↗](https://support.midasuser.com/hc/en-us/articles/35851688190105)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| i | Outer-Height array | `"vSIZE_PSC_A"` | Array[Number] | - | **Required** |
| ii | Outer-Breadth array | `"vSIZE_PSC_B"` | Array[Number] | - | **Required** |
| iii | Inner-Height array | `"vSIZE_PSC_C"` | Array[Number] | - | **Required** |
| iv | Inner-Breadth array | `"vSIZE_PSC_D"` | Array[Number] | - | **Required** |
| (6) | Web Thickness Check [i, j] | `"USE_WEB_THICK"` | Array[Boolean] | false | **Required** |

```json
{
  "Assign": {
    "401": {
      "SECTTYPE": "PSC",
      "SECT_NAME": "PSC_I-Girder",
      "SECT_BEFORE": {
        "OFFSET_PT": "CB",
        "HORZ_OFFSET_OPT": 0, "VERT_OFFSET_OPT": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": false,
        "SHAPE": "PSC1",
        "SECT_I": {
          "vSIZE_PSC_A": [0.20, 0.05, 0.10, 0.05, 0.05, 0.20],
          "vSIZE_PSC_B": [0.60, 0.40, 0.20, 0.18, 0.40, 0.60],
          "vSIZE_PSC_C": [0.0],
          "vSIZE_PSC_D": [0.0]
        },
        "USE_WEB_THICK": [false, false]
      }
    }
  }
}
```

---

### 12-E. SECT — Tapered (`"SECTTYPE": "TAPERED"`)

- **Source**: [Section Properties - Tapered - DB/User ↗](https://support.midasuser.com/hc/en-us/articles/35852806893593)

Tapered 단면은 `"SECT_BEFORE"` (I-end)와 함께 `"SECT_AFTER"` (J-end)를 추가로 정의합니다.

```json
{
  "Assign": {
    "501": {
      "SECTTYPE": "TAPERED",
      "SECT_NAME": "Tapered_H",
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0, "USERDEF_OFFSET_YJ": 0,
        "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0, "USERDEF_OFFSET_ZJ": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": false,
        "SHAPE": "H",
        "DATATYPE": 1,
        "SECT_I": { "DB_NAME": "KS21", "SECT_NAME": "H400x200x8/13" },
        "SECT_J": { "DB_NAME": "KS21", "SECT_NAME": "H300x150x6.5/9" }
      }
    }
  }
}
```

---

### 12-F. SECT — Composite / Steel Girder

- **Source**: [Section Properties - Composite - Steel ↗](https://support.midasuser.com/hc/en-us/articles/35939122737689) | [Steel Girder ↗](https://support.midasuser.com/hc/en-us/articles/35939506348697)

```json
{
  "Assign": {
    "701": {
      "SECTTYPE": "COMPOSITE",
      "SECT_NAME": "SteelBox_Comp",
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "HORZ_OFFSET_OPT": 0, "VERT_OFFSET_OPT": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": false,
        "SHAPE": "SOD_BOX"
      }
    }
  }
}
```

### Python 예제 (SECT 전체)

```python
# --- GET: 모든 단면 조회 ---
result = midas_api("GET", "/db/SECT")
sections = result.get("SECT", {})
print(f"정의된 단면 수: {len(sections)}")
for sid, s in sections.items():
    print(f"  {sid}: {s.get('SECT_NAME', '?')} ({s.get('SECTTYPE', '?')})")

# --- POST: H형강 DB 단면 생성 ---
sect_data = {
    "Assign": {
        "1": {
            "SECTTYPE": "DBUSER",
            "SECT_NAME": "H300x150",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",
                "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
                "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
                "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
                "USE_SHEAR_DEFORM": True, "USE_WARPING_EFFECT": True,
                "SHAPE": "H",
                "DATATYPE": 1,
                "SECT_I": {"DB_NAME": "KS21", "SECT_NAME": "H300x150x6.5/9"}
            }
        },
        "2": {
            "SECTTYPE": "DBUSER",
            "SECT_NAME": "H400x200",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",
                "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
                "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
                "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
                "USE_SHEAR_DEFORM": True, "USE_WARPING_EFFECT": True,
                "SHAPE": "H",
                "DATATYPE": 1,
                "SECT_I": {"DB_NAME": "KS21", "SECT_NAME": "H400x200x8/13"}
            }
        }
    }
}
midas_api("POST", "/db/SECT", sect_data)
```

<!-- om-fields:35808653964185 -->
**OM 원문 추가 필드 — Section Properties - Common ([35808653964185](https://support.midasuser.com/hc/en-us/articles/35808653964185))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `TYPE`, `Y_VAR`, `Z_VAR`

<!-- /om-fields -->

<!-- om-fields:35809067039513 -->
**OM 원문 추가 필드 — Section Properties - DB/User ([35809067039513](https://support.midasuser.com/hc/en-us/articles/35809067039513))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| iii. | [GEN Design Feature] Stiffness for Design ²⁾ | `"CF_STIFF_ULS"` | Object | - | Optional |
| (3) | Number of Stiffeners 1 · Box with Stiffener: N1 · Pipe with Stiffener: N | `"CELL_SHAPE"` | Integer | - | **Required** |
| (4) | Number of Stiffeners 2 · Box with Stiffener: N2 | `"CELL_TYPE"` | Integer | - | **Required** |
| 3 | Coating Thickness for Design ²⁾ | `"COAT_THIK"` | Number | 0 | Optional |
| 4 | Type of Forming for Design ²⁾ · Roll Forming: 0 · Other Methods of Forming: 1 | `"FORM_TYPE"` | Integer | 0 | Optional |
| 1 | Stiffness for Design | `"CF_STIFF_ULS"` | Object | - | Optional |
| (1) | Effective Area | `"A_EFF"` | Number | DB | Optional |
| (2) | Net Area | `"A_NET"` | Number | DB | Optional |
| (3) | Moment of Inertia; y-axis | `"LY_EFF"` | Number | DB | Optional |
| (4) | Moment of Inertia; z-axis | `"LZ_EFF"` | Number | DB | Optional |
| (5) | Section modulus; y-axis | `"WY_EFF"` | Number | DB | Optional |
| (6) | Section modulus; z-axis | `"WZ_EFF"` | Number | DB | Optional |
| (7) | Torsional Moment of Inertia | `"LT_EFF"` | Number | DB | Optional |
| (8) | Warping Moment of inertia | `"LW_EFF"` | Number | DB | Optional |
| (9) | Radius of Gyration; y-axis | `"RY_EFF"` | Number | DB | Optional |
| (10) | Radius of Gyration; z-axis | `"RZ_EFF"` | Number | DB | Optional |

<!-- /om-fields -->

<!-- om-fields:35839753881497 -->
**OM 원문 추가 필드 — Section Properties - Value ([35839753881497](https://support.midasuser.com/hc/en-us/articles/35839753881497))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| ii. | Built-Up Section Check · Not Build-Up: 0 · Build-Up: 1 | `"BUILT_FLAG"` | Integer | 1 | Optional |
| iii. | Inside perimeter length of a hollow section ¹⁾ | `"PERIIN"` | Number | 0 | Optional |
| iv. | Total perimeter of the section ¹⁾ | `"PERIOUT"` | Number | 0 | Optional |
| v. | Section Stiffness ¹⁾ ²⁾ | `"STIFF"` | Object | - | Optional |
| (2) | Number of Cell · Only for R-Octagon | `"CELL_SHAPE"` | Integer |  | **Required** |
| 1 | Section Stiffness | `"STIFF"` | Object | - | Optional |
| (1) | Cross section area | `"AREA"` | Number | 0 | Optional |
| (2) | Effective shear area for shear force in the element's local y-direction | `"ASY"` | Number | 0 | Optional |
| (3) | Effective shear area for shear force in the element's local z-direction | `"ASZ"` | Number | 0 | Optional |
| (4) | Torsional constant about the element's local x-axis | `"RXX"` | Number | 0 | Optional |
| (5) | Moment of Inertia about the element's local y-direction | `"RYY"` | Number | 0 | Optional |
| (6) | Moment of Inertia about the element's local z-direction | `"RZZ"` | Number | 0 | Optional |
| (7) | Distance from the section's neutral axis to the extreme fiber of the element in the local (+)y-direction | `"CYP"` | Number | 0 | Optional |
| (8) | Distance from the section's neutral axis to the extreme fiber of the element in the local (-)y-direction | `"CYM"` | Number | 0 | Optional |
| (9) | Distance from the section's neutral axis to the extreme fiber of the element in the local (+)z-direction | `"CZP"` | Number | 0 | Optional |
| (10) | Distance from the section's neutral axis to the extreme fiber of the element in the local (-)z-direction | `"CZM"` | Number | 0 | Optional |
| (11) | Shear coefficient for the shear force applied in the element's local z-direction | `"QYB"` | Number | 0 | Optional |
| (12) | Shear coefficient for the shear force applied in the element's local y-direction | `"QZB"` | Number | 0 | Optional |
| (13) | Distance from the section's neutral axis to the Location 1, 2, 3, 4 · [y1, y2, y3, y4] | `"Y"` | Array [Number] | 0 | Optional |
| (14) | Distance from the section's neutral axis to the Location 1, 2, 3, 4 · [z1, z2, z3, z4] | `"Z"` | Array [Number] | 0 | Optional |
| (15) | Warping Constant | `"Iw"` | Number | 0 | Optional |
| (16) | Warping function · [w1, w2, w3, w4] | `"W"` | Array [Number] | 0 | Optional |
| (17) | Coefficients to be used to calculate twisting and warping moment · [Cxy1, Cxy2, Cxy3, Cxy4] | `"CXY"` | Array [Number] | 0 | Optional |
| (18) | Coefficients to be used to calculate twisting and warping moment · [Cxz1, Cxz2, Cxz3, Cxz4] | `"CXZ"` | Array [Number] | 0 | Optional |
| (19) | Distance between centroid and shear center in the local y directions | `"YS_YC"` | Number | 0 | Optional |
| (20) | Distance between centroid and shear center in the local z directions | `"ZS_ZC"` | Number | 0 | Optional |
| (21) | Polar moment of inertia | `"IP"` | Number | 0 | Optional |
| (1) | Centroidal distance in ECS y-axis | `"YBAR"` | Number | 0 | Optional |
| (2) | Centroidal distance in ECS z-axis | `"ZBAR"` | Number | 0 | Optional |
| (3) | Plastic section modulus about the element local y-direction | `"ZYY"` | Number | 0 | Optional |
| (4) | Plastic section modulus about the element local z-direction | `"ZZZ"` | Number | 0 | Optional |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `IW`

<!-- /om-fields -->

<!-- om-fields:35845378225689 -->
**OM 원문 추가 필드 — Section Properties - SRC ([35845378225689](https://support.midasuser.com/hc/en-us/articles/35845378225689))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (8) | Assign Steel to be the Reference When Calculating Stiffness of a Composite Section | `"MATL_THERMAL"` | Integer | - | Read Only |
| iii. | [DB Section] Section Name of DB · Only for Rect-Cross H and Rec-Combined T | `"SECT_NAME2"` | String | - | **Required** |
| (11) | [User Section] Number of Stiffeners 1 · SRC-Box/Pipe-Stiffener (N1) | `"CELL_SHAPE"` | Integer | - | **Required** |
| (12) | Number of Stiffeners 2 · SRC-Box-Stiffener (N2) | `"CELL_TYPE"` | Integer | - | **Required** |

<!-- /om-fields -->

<!-- om-fields:35851688190105 -->
**OM 원문 추가 필드 — Section Properties - PSC ([35851688190105](https://support.midasuser.com/hc/en-us/articles/35851688190105))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| v. | PSC-nCELL2 · Slab Width v. Others · Index 0 of "vSIZE_PSC_A" | `"SWIDTH"` | Number | - | Optional |
| (2) | Warping Check for I · Auto: true · User: false | `"WARPING_CHK_AUTO_I"` | Boolean | true | Optional |
| (3) | Warping Check for J · Auto: true · User: false | `"WARPING_CHK_AUTO_J"` | Boolean | true | Optional |
| (4) | Warping Check Position for I · [[ y1, y2, y3, y4, y5, y6 ],[ z1, z2, z3, z4, z5, z6 ]] | `"WARPING_CHK_POS_I"` | Array [Array [Number]] | 0 | Optional |
| (5) | Warping Check Position for J · [[ y1, y2, y3, y4, y5, y6 ],[ z1, z2, z3, z4, z5, z6 ]] | `"WARPING_CHK_POS_J"` | Array [Array [Number]] | 0 | Optional |
| (7) | Web Thickness Value for Torsion of I, J · [i, j] | `"WEB_THICK"` | Array [Number] | 0 | Optional |
| (8) | Web Thickness Check for Shear of I, J · [[ti1, ti2, ti3], [tj1, tj2, tj3]] | `"USE_WEB_THICK_SHEAR"` | Array [Array [Boolean] | false | **Required** |
| (9) | Web Thickness Value for Shear of I, J · [[ti1, ti2, ti3], [tj1, tj2, tj3]] | `"WEB_THICK_SHEAR"` | Array [Array [Number]] | 0 | Optional |
| (10) | Symmetry Option | `"USE_SYMMETRIC"` | Boolean | false | Optional |
| (11) | Side Hole Option · Only nCELL2 | `"USE_SMALL_HOLE"` | Boolean | false | Optional |
| (12) | Mesh Size Calculation Option | `"USE_USER_DEF_MESHSIZE"` | Boolean | false | Optional |
| (14) | Stiffness Calculation Option | `"USE_USER_INTPUT_STIFF"` | Boolean | - | Optional |
| (15) | Shape Option 1 ²⁾ | `"PSC_OPT1"` | String | - | **Required** |
| (16) | Shape Option 2 ²⁾ | `"PSC_OPT2"` | Integer | - | **Required** |
| (17) | Joint On/Off ³⁾ | `"JOINT"` | Array [Boolean] | - | **Required** |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `AUTO_SHEAR_CHK_POS`, `SHEAR_CHK`, `USE_AUTO_SHEAR_CHK_POS`

<!-- /om-fields -->

<!-- om-fields:35852806893593 -->
**OM 원문 추가 필드 — Section Properties - Tapered - DB/User ([35852806893593](https://support.midasuser.com/hc/en-us/articles/35852806893593))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | Tapered Type · DB: 1 · User: 2 | `"TYPE"` | Integer | - | **Required** |
| (2) | Y Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Y_VAR"` | Integer | - | **Required** |
| (3) | Z Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Z_VAR"` | Integer | - | **Required** |

<!-- /om-fields -->

<!-- om-fields:35938685208089 -->
**OM 원문 추가 필드 — Section Properties - Tapered - Value ([35938685208089](https://support.midasuser.com/hc/en-us/articles/35938685208089))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | Tapered Type · Value: 3 | `"TYPE"` | Integer | - | **Required** |
| (2) | Y Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Y_VAR"` | Integer | - | **Required** |
| (3) | Z Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Z_VAR"` | Integer | - | **Required** |
| ii. | Inside perimeter length of a hollow section ¹⁾ | `"PERIIN"` | Number | 0 | Optional |
| iii. | Total perimeter of the section ¹⁾ | `"PERIOUT"` | Number | 0 | Optional |
| iv. | Section Stiffness ¹⁾ | `"STIFF"` | Object | - | Optional |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `AREA`, `ASY`, `ASZ`, `CYM`, `CYP`, `CZM`, `CZP`, `QYB`, `QZB`, `RXX`, `RYY`, `RZZ`, `Y`, `YBAR`, `Z`, `ZBAR`, `ZYY`, `ZZZ`

<!-- /om-fields -->

<!-- om-fields:35938998724377 -->
**OM 원문 추가 필드 — Section Properties - Composite - PSC ([35938998724377](https://support.midasuser.com/hc/en-us/articles/35938998724377))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (6) | Ratio of Thermal Expansion Coefficient of Steel and Concrete | `"MATL_THERMAL"` | Number | - | **Required** |
| (7) | Multiple Modulus of Elasticity Options | `"USE_MULTI_ELAST"` | Boolean | false | Optional |
| (8) | Long-term Es/Ec | `"LONGTERM_ESEC"` | Number | 0 | Optional |
| (9) | Shrinkage Es/Ec | `"SHRINK_ESEC"` | Number | 0 | Optional |
| (10) | Shape Option 1 ¹⁾ | `"PSC_OPT1"` | String | - | **Required** |
| (11) | Shape Option 2 ¹⁾ | `"PSC_OPT2"` | Integer | - | **Required** |
| (12) | Joint On/Off ¹⁾ | `"JOINT"` | Array [Boolean] | - | **Required** |
| (1) | Slab Dimensions · [Bc, tc, Hh] | `"SLAB"` | Array [Number] | - | **Required** |

<!-- /om-fields -->

<!-- om-fields:35939122737689 -->
**OM 원문 추가 필드 — Section Properties - Composite - Steel ([35939122737689](https://support.midasuser.com/hc/en-us/articles/35939122737689))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (5) | Ratio of Thermal Expansion Coefficient of Steel and Concrete | `"MATL_THERMAL"` | Number | - | **Required** |
| (6) | Multiple Modulus of Elasticity Options | `"USE_MULTI_ELAST"` | Boolean | false | Optional |
| (7) | Long-term Es/Ec | `"LONGTERM_ESEC"` | Number | 0 | Optional |
| (8) | Shrinkage Es/Ec | `"SHRINK_ESEC"` | Number | 0 | Optional |
| ii. | [Type 1 (Symmetric Section)] Stiffener ²⁾ | `"STIFFENER"` | Object | - | Optional |
| ii. | [Type 2 (Asymmetric Section)] Symmetric Section Auto Calculation | `"USE_SYM_CALC"` | Boolean | false | Optional |
| iii. | Stiffener ³⁾ | `"SODSTIFF"` | Object | - | Optional |
| (1) | [Type 1 (Symmetric Section)] Slab Dimensions · [Bc, tc, Hh] | `"SLAB"` | Array [Number] | - | **Required** |
| 1 | Stiffener | `"STIFFENER"` | Object | - | Optional |
| (1) | Position of Stiffener · Both: 0 · Left: 1 · Right: 2 | `"POSITION"` | Integer | - | - |
| (2) | Reference of d · Top: 0 · Bottom: 1 | `"REFERENCE_OF_D"` | Integer | - | - |
| (3) | Stiffener Array Count · [N Left, N Right, N Bottom, N Top] | `"STIFF_CNT"` | Array [Integer] | - | - |
| (4) | Stiffener Shape · Insert the data as an object | `"STIFF_SHAPE"` | Array [Object] | - | - |
| ii. | Stiffener Shape Type · Flat: 0 · Tee: 1 · U-Rib: 2 | `"SHAPE_TYPE"` | Integer | - | - |
| iii. | Stiffener Size · Flat: [H, B] · Tee: [H, B, tw, tf] · U-Rib: [H, B1, B2, t, R] | `"SIZE"` | Array [Number] | - | - |
| (5) | Stiffener Top/Bottom/Left/Right · Insert the data as an object | `"STIFF_TOP"` / `"STIFF_BOT"` / `"STIFF_LEFT"` / `"STIFF_RIGHT"` | Array [Object] | - | - |
| i. | Stiffener Spacing | `"SPACING"` | Number | - | - |
| iii. | Considering for the Section Property Calculations | `"USE_CALC"` | Boolean | - | - |
| 1 | Stiffener | `"SODSTIFF"` | Object | - | Optional |
| (1) | Number of defined Stiffeners Shape | `"TOSTIFNOS"` | Integer | - | - |
| (2) | Number of defined Stiffeners Positions | `"DECKSTIFFNO"` | Integer | - | - |
| (4) | Stiffener Positions · Insert the data as an object | `"SUB"` | Array [Object] | - | - |
| i. | Deck Positions <strong> · </strong>Steel-Box / Top flange: 0 / Left web: 1 / Right web: 2 / Bottom flange: 3 | `"DECK_POS"` | Integer | - | - |
| ii. | Deck Part · Deck1, Web: 0 · Deck2: 1 · Deck3: 2 | `"DECK_PART"` | Integer | - | - |
| iii. | Reference Positions · Left, Top: 0 · Right, Bottom: 1 | `"REF_POS"` | Integer | - | - |
| iv. | Number of Stiffeners | `"NUM"` | Integer | - | - |
| v. | Deck Name · DECK_POS/DECK_PART: "Deck Name" · Steel Box · Steel-I · Steel-Tub | `"DECK_NAME"` | String | - | - |
| vi. | Number of Stiffeners in a Deck Positions | `"EACHSTIFFNOS"` | Integer | - | - |
| vii. | Stiffeners Data at Positions · Insert the data as an object | `"DATA"` | Array [Object] | - | - |
| - | vii-1. Considering for the section property calculations | `"USE_CALC"` | Boolean | - | - |
| - | vii-2. Stiffener Spacing | `"SPACING"` | Number | - | - |
| - | vii-3. Stiffener Positions · Top flange/Bottom: 1 · Web/Left: 0 · Web/Right: 1 · Web/Both: 2 · Bottom flange/Top: 0 | `"STIF_POS"` | Number | - | - |
| - | vii-4. Stiffener Shape Name | `"SHAPE_NAME"` | String | - | - |
| - | vii-5. Stiffener Name | `"STIF_NAME"` | String | - | - |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `STIFF`

<!-- /om-fields -->

<!-- om-fields:35939506348697 -->
**OM 원문 추가 필드 — Section Properties - Steel Girder ([35939506348697](https://support.midasuser.com/hc/en-us/articles/35939506348697))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| - | Symmetric Section Auto Calculation | `"USE_SYM_CALC"` | Boolean | false | Optional |
| - | Stiffener ²⁾ | `"SODSTIFF"` | Object | - | Optional |
| 1 | Stiffener | `"SODSTIFF"` | Object | - | Optional |
| (1) | Number of defined Stiffeners Shape | `"TOSTIFNOS"` | Integer | - | - |
| (2) | Number of defined Stiffeners Positions | `"DECKSTIFFNO"` | Integer | - | - |
| ii. | Stiffener Shape Type · Flat: 0 · Tee: 1 · U-Rib: 2 | `"SHAPE_TYPE"` | Integer | - | - |
| iii. | Stiffener Size · Flat: [H, B] · Tee: [H, B, tw, tf] · U-Rib: [H, B1, B2, t, R] | `"SIZE"` | Array [Number] | - | - |
| (4) | Stiffener Positions · Insert the data as an object | `"SUB"` | Array [Object] | - | - |
| i. | Deck Positions <strong> · </strong>Steel-Box / Top flange: 0 / Left web: 1 / Right web: 2 / Bottom flange: 3 | `"DECK_POS"` | Integer | - | - |
| ii. | Deck Part · Deck1, Web: 0 · Deck2: 1 · Deck3: 2 | `"DECK_PART"` | Integer | - | - |
| iii. | Reference Positions · Left, Top: 0 · Right, Bottom: 1 | `"REF_POS"` | Integer | - | - |
| iv. | Number of Stiffeners | `"NUM"` | Integer | - | - |
| v. | Deck Name · DECK_POS/DECK_PART: "Deck Name" · Steel Box · Steel-I · Steel-Tub | `"DECK_NAME"` | String | - | - |
| vi. | Number of Stiffeners in a Deck Positions | `"EACHSTIFFNOS"` | Integer | - | - |
| vii. | Stiffeners Data at Positions · Insert the data as an object | `"DATA"` | Array [Object] | - | - |
| - | vii-1. Considering for the section property calculations | `"USE_CALC"` | Boolean | - | - |
| - | vii-2. Stiffener Spacing | `"SPACING"` | Number | - | - |
| - | vii-3. Stiffener Positions · Top flange/Bottom: 1 · Web/Left: 0 · Web/Right: 1 · Web/Both: 2 · Bottom flange/Top: 0 | `"STIF_POS"` | Number | - | - |
| - | vii-4. Stiffener Shape Name | `"SHAPE_NAME"` | String | - | - |
| - | vii-5. Stiffener Name | `"STIF_NAME"` | String | - | - |

<!-- /om-fields -->

<!-- om-fields:35941360898713 -->
**OM 원문 추가 필드 — Section Properties - Tapered - PSC ([35941360898713](https://support.midasuser.com/hc/en-us/articles/35941360898713))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | Tapered Type · PSC: 11 | `"TYPE"` | Integer | - | **Required** |
| (2) | Y Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Y_VAR"` | Integer | - | **Required** |
| (3) | Z Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Z_VAR"` | Integer | - | **Required** |
| v. | PSC-nCELL2 · Slab Width v. Others · Index 0 of "vSIZE_PSC_A" | `"SWIDTH"` | Number | - | Optional |
| (6) | Warping Check for I · Auto: true · User: false | `"WARPING_CHK_AUTO_I"` | Boolean | true | Optional |
| (7) | Warping Check for J · Auto: true · User: false | `"WARPING_CHK_AUTO_J"` | Boolean | true | Optional |
| (8) | Warping Check Position for I · [[ y1, y2, y3, y4, y5, y6 ],[ z1, z2, z3, z4, z5, z6 ]] | `"WARPING_CHK_POS_I"` | Array [Array [Number]] | 0 | Optional |
| (9) | Warping Check Position for J · [[ y1, y2, y3, y4, y5, y6 ],[ z1, z2, z3, z4, z5, z6 ]] | `"WARPING_CHK_POS_J"` | Array [Array [Number]] | 0 | Optional |
| (11) | Web Thickness Value for Torsion of I, J · [i, j] | `"WEB_THICK"` | Array [Number] | 0 | Optional |
| (12) | Web Thickness Check for Shear of I, J · [[ti1, ti2, ti3], [tj1, tj2, tj3]] | `"USE_WEB_THICK_SHEAR"` | Array [Array [Boolean]] | false | **Required** |
| (13) | Web Thickness Value for Shear of I, J · [[ti1, ti2, ti3], [tj1, tj2, tj3]] | `"WEB_THICK_SHEAR"` | Array [Array [Number]] | 0 | Optional |
| (14) | Symmetry Option | `"USE_SYMMETRIC"` | Boolean | false | Optional |
| (15) | Side Hole Option · Only nCELL2 | `"USE_SMALL_HOLE"` | Boolean | false | Optional |
| (16) | Mesh Size Calculation Option | `"USE_USER_DEF_MESHSIZE"` | Boolean | false | Optional |
| (18) | Stiffness Calculation Option | `"USE_USER_INTPUT_STIFF"` | Boolean | - | Optional |
| (19) | Shape Option 1 ¹⁾ | `"PSC_OPT1"` | String | - | **Required** |
| (20) | Shape Option 2 ¹⁾ | `"PSC_OPT2"` | Integer | - | **Required** |
| (21) | Joint On/Off ¹⁾ | `"JOINT"` | Array [Boolean] | - | **Required** |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `AUTO_SHEAR_CHK_POS`, `MESHSIZE`, `SHEAR_CHK`, `USE_AUTO_SHEAR_CHK_POS`

<!-- /om-fields -->

<!-- om-fields:35941514067225 -->
**OM 원문 추가 필드 — Section Properties - Tapered - Composite PSC ([35941514067225](https://support.midasuser.com/hc/en-us/articles/35941514067225))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | Tapered Type · PSC-I: 12 · PSC-T: 13 | `"TYPE"` | Integer | - | **Required** |
| (2) | Y Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Y_VAR"` | Integer | - | **Required** |
| (3) | Z Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Z_VAR"` | Integer | - | **Required** |
| (9) | Ratio of Thermal Expansion Coefficient of Steel and Concrete | `"MATL_THERMAL"` | Number | - | **Required** |
| (10) | Multiple Modulus of Elasticity Options | `"USE_MULTI_ELAST"` | Boolean | false | Optional |
| (11) | Long-term Es/Ec | `"LONGTERM_ESEC"` | Number | 0 | Optional |
| (12) | Shrinkage Es/Ec | `"SHRINK_ESEC"` | Number | 0 | Optional |
| (13) | Shape Option 1 ¹⁾ | `"PSC_OPT1"` | String | - | **Required** |
| (14) | Shape Option 2 ¹⁾ | `"PSC_OPT2"` | Integer | - | **Required** |
| (15) | Joint On/Off ¹⁾ | `"JOINT"` | Array [Boolean] | - | **Required** |
| (1) | Slab Dimensions · [Bc, tc, Hh] | `"SLAB"` | Array [Number] | - | **Required** |
| i. | Built-Up Section · 1 | `"BUILT_FLAG"` | Integer | - | **Required** |
| 4 | Section Specifications - J | `"COMPOSITE_J"` | Object | - | **Required** |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `USE_SYMMETRIC`

<!-- /om-fields -->

<!-- om-fields:35941644806553 -->
**OM 원문 추가 필드 — Section Properties - Tapered - Composite Steel ([35941644806553](https://support.midasuser.com/hc/en-us/articles/35941644806553))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | Tapered Type · Steel-Box: 9 · Steel-I: 10 · Steel-Tub: 16 · Steel-Box: 19 · Steel-I: 20 · Steel-Tub: 21 | `"TYPE"` | Integer | - | **Required** |
| (2) | Y Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Y_VAR"` | Integer | - | **Required** |
| (3) | Z Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Z_VAR"` | Integer | - | **Required** |
| (8) | Ratio of Thermal Expansion Coefficient of Steel and Concrete | `"MATL_THERMAL"` | Number | - | **Required** |
| (9) | Multiple Modulus of Elasticity Options | `"USE_MULTI_ELAST"` | Boolean | false | Optional |
| (10) | Long-term Es/Ec | `"LONGTERM_ESEC"` | Number | 0 | Optional |
| (11) | Shrinkage Es/Ec | `"SHRINK_ESEC"` | Number | 0 | Optional |
| ii. | [Type 1 (Symmetric Section)] Stiffener ¹⁾ | `"STIFFENER"` | Object | - | Optional |
| ii. | [Type 2 (Asymmetric Section)] Symmetric Section Auto Calculation | `"USE_SYM_CALC"` | Boolean | false | Optional |
| iii. | Stiffener ¹⁾ | `"SODSTIFF"` | Object | - | Optional |
| (1) | [Type 1 (Symmetric Section)] Slab Dimensions · [Bc, tc, Hh] | `"SLAB"` | Array [Number] | - | **Required** |
| i. | Built-Up Section · 1 | `"BUILT_FLAG"` | Integer | - | **Required** |
| ii. | Built-Up Section · 1 | `"BUILT_FLAG"` | Integer | - | **Required** |
| 4 | Section Specifications - J | `"COMPOSITE_J"` | Object | - | **Required** |
| (2) | Symmetric Section Auto Calculation | `"USE_SYM_CALC"` | Boolean | false | Optional |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `DATA`, `DECKSTIFFNO`, `DECK_NAME`, `DECK_PART`, `DECK_POS`, `EACHSTIFFNOS`, `NUM`, `POSITION`, `REFERENCE_OF_D`, `REF_POS`, `SHAPE_NAME`, `SHAPE_TYPE`, `SIZE`, `SPACING`, `STIFF`, `STIFF_BOT`, `STIFF_CNT`, `STIFF_LEFT`, `STIFF_RIGHT`, `STIFF_SHAPE`, `STIFF_TOP`, `STIF_NAME`, `STIF_POS`, `SUB`, `TOSTIFNOS`, `USE_CALC`

<!-- /om-fields -->

<!-- om-fields:35941809011225 -->
**OM 원문 추가 필드 — Section Properties - Tapered - Steel Girder ([35941809011225](https://support.midasuser.com/hc/en-us/articles/35941809011225))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | Tapered Type · Steel Box: 17 · Steel I: 18 | `"TYPE"` | Integer | - | **Required** |
| (2) | Y Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Y_VAR"` | Integer | - | **Required** |
| (3) | Z Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Z_VAR"` | Integer | - | **Required** |
| - | Symmetric Section Auto Calculation | `"USE_SYM_CALC"` | Boolean | false | Optional |
| - | Stiffener ¹⁾ | `"SODSTIFF"` | Object | - | Optional |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `DATA`, `DECKSTIFFNO`, `DECK_NAME`, `DECK_PART`, `DECK_POS`, `EACHSTIFFNOS`, `NUM`, `REF_POS`, `SHAPE_NAME`, `SHAPE_TYPE`, `SIZE`, `SPACING`, `STIF_NAME`, `STIF_POS`, `SUB`, `TOSTIFNOS`, `USE_CALC`

<!-- /om-fields -->

<!-- om-fields:39233604772633 -->
**OM 원문 추가 필드 — Section Properties - PSC Value ([39233604772633](https://support.midasuser.com/hc/en-us/articles/39233604772633))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| ii. | Inside perimeter length of a hollow section ¹⁾ | `"PERIIN"` | Number | 0 | Optional |
| iii. | Total perimeter of the section ¹⁾ | `"PERIOUT"` | Number | 0 | Optional |
| iv. | Section Stiffness ¹⁾ | `"STIFF"` | Object | - | Optional |
| vi. | Outer Polygon ²⁾ | `"OUTER_POLYGON"` | Array [Object] | - | **Required** |
| vii. | Inner Polygon ²⁾ · for inner hole | `"INNER_POLYGON"` | Array [Object] | - | Optional |
| (2) | Shear Check | `"SHEAR_CHK"` | Boolean | false | Optional |
| (3) | Position Value for Shear check of I, J · [[Zi1, Zi2, Zi3], [Zj1, Zj2, Zj3]] | `"SHEAR_CHK_POS"` | Array [Array [Number]] | 0 | Optional |
| (4) | Qy Check for Shear of I, J · [[Qi1, Qi2, Qi3], [Qj1, Qj2, Qj3]] | `"USE_AUTO_QY"` | Array [Array [Boolean]] | false | Optional |
| (5) | Qy Value for Shear of I, J · [[Qi1, Qi2, Qi3], [Qj1, Qj2, Qj3]] | `"AUTO_QY"` | Array [Array [Number]] | 0 | Optional |
| (6) | Web Thickness Value for Torsion of I, J · [i, j] | `"WEB_THICK"` | Array [number] | 0 | Optional |
| (7) | Web Thickness Check for Shear of I, J · [[ti1, ti2, ti3], [tj1, tj2, tj3]] | `"USE_WEB_THICK_SHEAR"` | Array [Array [Boolean]] | false | Optional |
| (8) | Web Thickness Value for Shear of I, J · [[ti1, ti2, ti3], [tj1, tj2, tj3]] | `"WEB_THICK_SHEAR"` | Array [Array [Number]] | 0 | Optional |
| 1 | Outer Polygon | `"OUTER_POLYGON"` | Array [Object] | - | **Required** |
| (1) | Vertex Data | `"Vertex"` | Array [Object] | - | **Required** |
| i. | X-Coordinate | `"X"` | Number | - | **Required** |
| ii. | Y-Coordinate | `"Y"` | Number | - | **Required** |
| 2 | Inner Polygon | `"INNER_POLYGON"` | Array [Object] | - | Optional |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `AREA`, `ASY`, `ASZ`, `BUILT_FLAG`, `CXY`, `CXZ`, `CYM`, `CYP`, `CZM`, `CZP`, `IP`, `IW`, `QYB`, `QZB`, `RXX`, `RYY`, `RZZ`, `VERTEX`, `W`, `YBAR`, `YS_YC`, `Z`, `ZBAR`, `ZS_ZC`, `ZYY`, `ZZZ`

<!-- /om-fields -->

<!-- om-fields:39233752695321 -->
**OM 원문 추가 필드 — Section Properties - Tapered - PSC Value ([39233752695321](https://support.midasuser.com/hc/en-us/articles/39233752695321))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | Y Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Y_VAR"` | Integer | - | **Required** |
| (2) | Z Axis Variations · Linear: 1 · Parabolic: 2 · Cubic: 3 | `"Z_VAR"` | Integer | - | **Required** |
| ii. | Inside perimeter length of a hollow section ¹⁾ | `"PERIIN"` | Number | 0 | Optional |
| iii. | Total perimeter of the section ¹⁾ | `"PERIOUT"` | Number | 0 | Optional |
| iv. | Section Stiffness ¹⁾ | `"STIFF"` | Object | - | Optional |
| vi. | Outer Polygon ²⁾ | `"OUTER_POLYGON"` | Array [Object] | - | **Required** |
| vii. | Inner Polygon ²⁾ · for inner hole | `"INNER_POLYGON"` | Array [Object] | - | Optional |
| (5) | Shear Check | `"SHEAR_CHK"` | Boolean | false | Optional |
| (6) | Position Value for Shear check of I, J · [[Zi1, Zi2, Zi3], [Zj1, Zj2, Zj3]] | `"SHEAR_CHK_POS"` | Array [Array [Number]] | 0 | Optional |
| (7) | Qy Check for Shear of I, J · [[Qi1, Qi2, Qi3], [Qj1, Qj2, Qj3]] | `"USE_AUTO_QY"` | Array [Array [Boolean]] | false | Optional |
| (8) | Qy Value for Shear of I, J · [[Qi1, Qi2, Qi3], [Qj1, Qj2, Qj3]] | `"AUTO_QY"` | Array [Array [Number]] | 0 | Optional |
| (9) | Web Thickness Value for Torsion of I, J · [i, j] | `"WEB_THICK"` | Array [number] | 0 | Optional |
| (10) | Web Thickness Check for Shear of I, J · [[ti1, ti2, ti3], [tj1, tj2, tj3]] | `"USE_WEB_THICK_SHEAR"` | Array [Array [Boolean]] | false | Optional |
| (11) | Web Thickness Value for Shear of I, J · [[ti1, ti2, ti3], [tj1, tj2, tj3]] | `"WEB_THICK_SHEAR"` | Array [Array [Number]] | 0 | Optional |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `AREA`, `ASY`, `ASZ`, `BUILT_FLAG`, `CXY`, `CXZ`, `CYM`, `CYP`, `CZM`, `CZP`, `Calc_OPT`, `IP`, `IW`, `QYB`, `QZB`, `RXX`, `RYY`, `RZZ`, `VERTEX`, `W`, `X`, `Y`, `YBAR`, `YS_YC`, `Z`, `ZBAR`, `ZS_ZC`, `ZYY`, `ZZZ`

<!-- /om-fields -->


---

## 13. `/db/THIK`

> **Thickness** — 판(Plate/Wall) 요소의 두께를 정의합니다. Value와 Stiffened(보강판) 4가지 서브타입을 지원합니다.

- **URL**: `{base url}/db/THIK`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Thickness - Value ↗](https://support.midasuser.com/hc/en-us/articles/35942236652697)

### JSON Schema

```json
{
  "THIK": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":   { "description": "Name",       "type": "string" },
      "TYPE":   { "description": "Type",       "type": "string" },
      "STYPE":  { "description": "Sub Type",   "type": "string" },
      "bINOUT": { "description": "Thick Type", "type": "boolean" },
      "T_IN":   { "description": "Thick In",   "type": "number" },
      "T_OUT":  { "description": "Thick Out",  "type": "number" },
      "OFFSET": { "description": "Offset",     "type": "integer" },
      "O_VALUE":{ "description": "Offset Value","type": "number" }
    }
  }
}
```

### Specifications — Value (`"TYPE": "VALUE"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Thickness Name | `"NAME"` | String | - | **Required** |
| 2 | Thickness Type • Value: `"VALUE"` • Stiffened: `"STIFFENED"` | `"TYPE"` | String | - | **Required** |
| 3 | Plane • false: In-plane & Out-of-plane (same) • true: Different I/O values | `"bINOUT"` | Boolean | false | Optional |
| 4 | In-plane Thickness | `"T_IN"` | Number | - | **Required** |
| 5 | Out-of-plane Thickness (when `"bINOUT"` is true) | `"T_OUT"` | Number | - | Required |
| 6 | Plate Offset Option • None: 0 • Thickness Ratio: 1 • Value: 2 | `"OFFSET"` | Integer | 0 | Optional |
| 7 | Local z Direction Offset Value | `"O_VALUE"` | Number | 0 | Optional |

### Specifications — Stiffened DB (`"STYPE": "DB"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Thickness Type | `"TYPE"` | String | - | **Required** |
| 2 | Stiffened Thickness Sub-Type • Value: `"VALUE"` • User: `"USER"` • DB: `"DB"` | `"STYPE"` | String | - | **Required** |
| 3 | Rib Position • `"LOWER"` • `"UPPER"` | `"RIB_POS"` | String | - | **Required** |
| 4 | Defined Stiffener | `"SECTION"` | Object | - | **Required** |
| (1) | Thickness | `"THIKNESS"` | Number | - | **Required** |
| (2) | DB Name | `"DBNAME"` | String | - | **Required** |
| (3) | XZ Section | `"XZ"` | Object | - | **Required** |
| i | Use Rib Attached | `"bRIB"` | Boolean | false | Optional |
| ii | Shape | `"SHAPE"` | String | - | **Required** |
| iii | Section Name | `"NAME"` | String | - | **Required** |
| iv | Rib Spacing Distance | `"DIST"` | Number | - | **Required** |

### Request Body 예제

#### Value 두께

```json
{
  "Assign": {
    "1": {
      "NAME": "T200",
      "TYPE": "VALUE",
      "bINOUT": false,
      "T_IN": 0.20,
      "T_OUT": 0,
      "O_VALUE": 0
    }
  }
}
```

#### Stiffened DB 두께

```json
{
  "Assign": {
    "101": {
      "NAME": "Stiff_DB",
      "TYPE": "STIFFENED",
      "STYPE": "DB",
      "RIB_POS": "LOWER",
      "SECTION": {
        "THIKNESS": 0.012,
        "DBNAME": "KS21",
        "XZ": { "bRIB": true, "SHAPE": "C", "NAME": "C75x40x5/7", "DIST": 0.4 }
      }
    }
  }
}
```

### Python 예제

```python
# --- GET: 두께 전체 조회 ---
result = midas_api("GET", "/db/THIK")
thiks = result.get("THIK", {})
print(f"정의된 두께 수: {len(thiks)}")

# --- POST: Value 두께 생성 ---
thik_data = {
    "Assign": {
        "1": {"NAME": "T150", "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.15, "T_OUT": 0, "O_VALUE": 0},
        "2": {"NAME": "T200", "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.20, "T_OUT": 0, "O_VALUE": 0},
        "3": {"NAME": "T250", "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.25, "T_OUT": 0, "O_VALUE": 0},
    }
}
midas_api("POST", "/db/THIK", thik_data)
```

<!-- om-fields:35942342783769 -->
**OM 원문 추가 필드 — Thickness - Stiffened DB ([35942342783769](https://support.midasuser.com/hc/en-us/articles/35942342783769))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (4) | YZ Section | `"YZ"` | Object | - | **Required** |

<!-- /om-fields -->

<!-- om-fields:35942603029401 -->
**OM 원문 추가 필드 — Thickness - Stiffened User ([35942603029401](https://support.midasuser.com/hc/en-us/articles/35942603029401))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| - | iv) Size | `"SIZE"` | Array [Number] | - | **Required** |
| (3) | YZ Section | `"YZ"` | Object | - | **Required** |

<!-- /om-fields -->

<!-- om-fields:35942739673369 -->
**OM 원문 추가 필드 — Thickness - Stiffened Value ([35942739673369](https://support.midasuser.com/hc/en-us/articles/35942739673369))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | Thickness weight data of plate element | `"WEIGHT"` | Number | - | **Required** |
| v. | Distance from the neutral axis to the extreme fiber of the rib | `"HL"` | Number | - | Optional |
| (3) | YZ SECT | `"YZ"` | Object | - | Optional |
| - | v) Hl: Distance from the neutral axis to the extreme fiber of the rib | `"HL"` | Number | - | Optional |

<!-- /om-fields -->


---

## 14. `/db/TSGR`

> **Tapered Group** — 변단면 그룹을 정의합니다. 선형(Linear) 또는 다항식(Polynomial) 단면 변화를 설정합니다.

- **URL**: `{base url}/db/TSGR`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Tapered Group ↗](https://support.midasuser.com/hc/en-us/articles/35942955627673)

### JSON Schema

```json
{
  "TSGR": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":     { "description": "Group Name",                     "type": "string" },
      "ELEMLIST": { "description": "Element Key List",               "type": "array", "items": {"type": "integer"} },
      "ZVAR":     { "description": "Section shape z-axis variation", "type": "string" },
      "YVAR":     { "description": "Section shape y-axis variation", "type": "string" },
      "ZEXP":     { "description": "Z axis Exponent",                "type": "number" },
      "ZFROM":    { "description": "Z axis Symmetric Plane",         "type": "string" },
      "ZDIST":    { "description": "Z axis Symmetric Distance",      "type": "number" },
      "YEXP":     { "description": "Y axis Exponent",                "type": "number" },
      "YFROM":    { "description": "Y axis Symmetric Plane",         "type": "string" },
      "YDIST":    { "description": "Y axis Symmetric Distance",      "type": "number" }
    }
  }
}
```

### Specifications

> ⚠️ **2026-08-25 재확인 보강:** Y축 다항식 계열 필드(`YEXP`/`YFROM`/`YDIST`)가 누락돼 있어
> Z축과 대칭으로 추가했다(아티클 id `35942955627673`).

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Tapered Group Name | `"NAME"` | String | - | **Required** |
| 2 | Element No. list | `"ELEMLIST"` | Array[Integer] | - | **Required** |
| 3 | Z-axis Section Shape Variation · Linear: `"LINEAR"` / Polynomial: `"POLY"` | `"ZVAR"` | String | - | **Required** |
| 4 | Y-axis Section Shape Variation · Linear: `"LINEAR"` / Polynomial: `"POLY"` | `"YVAR"` | String | - | **Required** |
| 5 (ZVAR=POLY) | Z axis Exponent | `"ZEXP"` | Number | - | **Required** |
| 6 (ZVAR=POLY) | Z axis Symmetric Plane from i or j | `"ZFROM"` | String | `"i"` | Optional |
| 7 (ZVAR=POLY) | Z axis Symmetric Plane Distance (m) | `"ZDIST"` | Number | 0 | Optional |
| 8 (YVAR=POLY) | Y axis Exponent | `"YEXP"` | Number | - | **Required** |
| 9 (YVAR=POLY) | Y axis Symmetric Plane from i or j | `"YFROM"` | String | `"i"` | Optional |
| 10 (YVAR=POLY) | Y axis Symmetric Plane Distance (m) | `"YDIST"` | Number | 0 | Optional |

### Request Body

```json
{
  "Assign": {
    "1": { "NAME": "LinearGroup", "ELEMLIST": [1, 2, 3], "ZVAR": "LINEAR", "YVAR": "LINEAR" },
    "2": { "NAME": "PolyGroup",   "ELEMLIST": [4, 5, 6], "ZVAR": "POLY",   "YVAR": "LINEAR", "ZEXP": 2.0, "ZFROM": "i", "ZDIST": 0 }
  }
}
```

### Python 예제

```python
tsgr_data = {
    "Assign": {
        "1": {
            "NAME": "Haunch_Linear",
            "ELEMLIST": [10, 11, 12, 13],
            "ZVAR": "LINEAR",
            "YVAR": "LINEAR"
        }
    }
}
midas_api("POST", "/db/TSGR", tsgr_data)
```

---

## 15. `/db/SECF`

> **Section Manager – Stiffness** — 단면 강성 수정 계수를 할당합니다. 건설 단계, 지진, 설계 등 각 그룹별 강성 배율을 설정합니다.

- **URL**: `{base url}/db/SECF`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Stiffness ↗](https://support.midasuser.com/hc/en-us/articles/35943174833177)

### Specifications

> ⚠️ **2026-08-25 재확인 보강:** 변단면(Tapered) J단 계수 11개 필드(`W_SF`·`IPART`·`bDiffIJ`·
> `J1`~`J8`)가 통째로 빠져 있었다(아티클 id `35943174833177`). J단 필드는 I단과 이름 규칙이
> 달라 `AREA_SF_J`가 아니라 **`J1`~`J8`**(순서대로 Area/Asy/Asz/Ixx/Iyy/Izz/Weight/Warping)로
> 표기되므로 원문 그대로 옮겼다.

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Stiffness Items (Array of Objects) | `"ITEMS"` | Array[Object] | - | **Required** |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Area Scale Factor (I) | `"AREA_SF"` | Number | 1 | Optional |
| (4) | Asy Scale Factor (I) | `"ASY_SF"` | Number | 1 | Optional |
| (5) | Asz Scale Factor (I) | `"ASZ_SF"` | Number | 1 | Optional |
| (6) | Ixx Scale Factor (I) | `"IXX_SF"` | Number | 1 | Optional |
| (7) | Iyy Scale Factor (I) | `"IYY_SF"` | Number | 1 | Optional |
| (8) | Izz Scale Factor (I) | `"IZZ_SF"` | Number | 1 | Optional |
| (9) | Weight Scale Factor | `"WGT_SF"` | Number | 1 | Optional |
| (10) | Warping Scale Factor (I) | `"W_SF"` | Number | 1 | Optional |
| (11) | Composite Section 적용 시점 · Before만: `1` / After만: `2` / Before+After: `3` | `"IPART"` | Integer | 1 | Optional |
| (12) | Tapered Section — J단 별도 값 사용 여부 | `"bDiffIJ"` | Boolean | `true` | Optional |
| (13) | Area Scale Factor (J, Tapered) | `"J1"` | Number | 1 | Optional |
| (14) | Asy Scale Factor (J) | `"J2"` | Number | 1 | Optional |
| (15) | Asz Scale Factor (J) | `"J3"` | Number | 1 | Optional |
| (16) | Ixx Scale Factor (J) | `"J4"` | Number | 1 | Optional |
| (17) | Iyy Scale Factor (J) | `"J5"` | Number | 1 | Optional |
| (18) | Izz Scale Factor (J) | `"J6"` | Number | 1 | Optional |
| (19) | Weight Scale Factor (J) | `"J7"` | Number | 1 | Optional |
| (20) | Warping Scale Factor (J) | `"J8"` | Number | 1 | Optional |

### Request Body

```json
{
  "Assign": {
    "9001": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Creep716",
        "AREA_SF": 2.61, "ASY_SF": 3.25, "ASZ_SF": 1.09,
        "IXX_SF": 1.39, "IYY_SF": 1.52, "IZZ_SF": 1.0,
        "WGT_SF": 1.0
      }]
    }
  }
}
```

### Python 예제

```python
# 균열 단면 강성 저감 (콘크리트 보: Izz = 0.35)
secf_data = {
    "Assign": {
        "5": {
            "ITEMS": [{
                "ID": 1,
                "GROUP_NAME": "Seismic",
                "AREA_SF": 1.0, "ASY_SF": 1.0, "ASZ_SF": 1.0,
                "IXX_SF": 1.0, "IYY_SF": 0.70, "IZZ_SF": 0.35,
                "WGT_SF": 1.0
            }]
        }
    }
}
midas_api("POST", "/db/SECF", secf_data)
```

---

## 16. `/db/RPSC`

> **Section Manager – Reinforcements** — PSC/RC 단면 철근 배근 데이터를 설정합니다. 키는 단면 ID입니다.

- **URL**: `{base url}/db/RPSC`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Reinforcements ↗](https://support.midasuser.com/hc/en-us/articles/35943227821465)

### ADDITIONAL — 종방향철근 구조 개정 (2026-11-25 공식 반영)

> - 종방향철근이 최상위 `"MBAR_ITEMS"`가 아니라 **`"MBARS"[].MBAR_ITEMS`** 구조입니다.
> - `"OPT_CRACKED"`가 Required → Optional로 바뀌었고 `"CONTRIBUTION_FACTOR"`가 추가됐습니다.
> - `"LBAR_INC_FC"` 타입이 Integer(`0`/`1`) → Boolean입니다.
> - PUT에서 `"MBARS": []`, 또는 `MBAR_ITEMS`가 없는 객체(`{}`, GET 응답 형태)를 보내면 해당 단면의
>   기존 종방향철근이 유지됩니다. 삭제하려면 `{"MBAR_ITEMS": []}`를 보냅니다. 전단철근만 바꿀 때는
>   앞의 세 형태 중 아무것이나 보내면 됩니다.
>
> 공식 문서 기준입니다.

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Same Longitudinal Rebar at I/J | `"OPT_MBAR_J"` | Boolean | - | **Required** |
| 2 | Same Shear Rebar at I/J | `"OPT_SBAR_J"` | Boolean | - | **Required** |
| 3 | Cracked Section Shown only for composite sections. If omitted, the stored value is kept (false for a new record). | `"OPT_CRACKED"` | Boolean | - | Optional |
| 4 | Concrete Contribution Factor Steel composite Type 2 sections only. Applied when OPT_CRACKED is true (otherwise reset to 1). | `"CONTRIBUTION_FACTOR"` | Number | `1` | Optional |
| 5 | Shear Reinforcement Items Constraints: · Items: 1 ~ 2 Index 0: i-section, Index 1: j-section (when OPT_SBAR_J is false) | `"SBAR_ITEMS"` | Array[Object] | - | **Required** |
| 6 | Longitudinal Reinforcement Constraints: · Items: 0 ~ 2 Index 0: i-section, Index 1: j-section (when OPT_MBAR_J is false). On PUT, [] or an object without MBAR_ITEMS ({}, as returned by GET) keeps the existing longitudinal rebar of that section. | `"MBARS"` | Array[Object] | - | **Required** |
| 6.1 | └ Longitudinal Rebar Items Constraints: · Items: min 0 If omitted, the existing rebar of the section is kept (PUT). [] deletes it. | `"MBAR_ITEMS"` | Array[Object] | - | Optional |

#### `SBAR_ITEMS[]` — 전단철근

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | Diagonal Reinforcement | `"OPT_DR"` | Boolean | `false` | Optional |
| (2) | [DR] Pitch (> 0) | `"DR_PITCH"` | Number | - | **Required** (`OPT_DR`) |
| (3) | [DR] Angle | `"DR_THETA"` | Number | `0` | Optional |
| (4) | [DR] Area (> 0) | `"DR_AW"` | Number | - | **Required** (`OPT_DR`) |
| (5) | Steel Bar for Web | `"OPT_SBW"` | Boolean | `false` | Optional |
| (6) | [SBW] Pitch (> 0) | `"SBW_PITCH"` | Number | - | **Required** (`OPT_SBW`) |
| (7) | [SBW] Angle | `"SBW_ANGLE"` | Number | `90` | Optional |
| (8) | [SBW] Area (> 0) | `"SBW_AP"` | Number | - | **Required** (`OPT_SBW`) |
| (9) | [SBW] Pre-force (> 0) | `"SBW_PS"` | Number | - | **Required** (`OPT_SBW`) |
| (10) | [SBW] Shear Reduction Factor (> 0) | `"SBW_FACTOR"` | Number | `1` | Optional |
| (11) | Torsional Reinforcement | `"OPT_TR"` | Boolean | `false` | Optional |
| (12) | [TR] Pitch (> 0) | `"TR_PITCH"` | Number | - | **Required** (`OPT_TR`) |
| (13) | [TR] Area (Web) (> 0) | `"TR_AWT"` | Number | - | **Required** (`OPT_TR`) |
| (14) | [TR] Area (Long.) (> 0) | `"TR_ALT"` | Number | - | **Required** (`OPT_TR`) |
| (15) | Stirrup | `"OPT_SR"` | Boolean | `false` | Optional |
| (16) | [SR] Pitch (> 0) | `"SR_PITCH"` | Number | - | **Required** (`OPT_SR`) |
| (17) | [SR] Area (> 0) | `"SR_AW"` | Number | - | **Required** (`OPT_SR`) |
| (18) | Enclosing Stirrup | `"OPT_LBAR_FLG"` | Boolean | `false` | Optional |
| (19) | Cover Thickness (> 0) | `"LBAR_THICK"` | Number | - | **Required** (`OPT_LBAR_FLG`) |
| (20) | Include Flange/Cantilever | `"LBAR_INC_FC"` | Boolean | `false` | Optional |

#### `MBARS[].MBAR_ITEMS[]` — 종방향철근

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | 6.1.1 Section Positions - I / J · I: "I" · J: "J" | `"IJ"` | String | - | **Required** |
| (2) | 6.1.2 Bar Name Constraints: · Length: min 1 Must be a rebar name of the concrete rebar material code of the model (e.g. D16, #5). Otherwise the request is rejected. | `"NAME"` | String | - | **Required** |
| (3) | 6.1.3 Reference Y · Centroid: "0" · Left: "1" | `"REF_Y"` | Integer | - | **Required** |
| (4) | 6.1.4 Distance from Reference in Y direction | `"Y"` | Number | `0` | Optional |
| (5) | 6.1.5 Reference Z · Top: "0" · Bottom: "1" | `"REF_Z"` | Integer | - | **Required** |
| (6) | 6.1.6 Distance from Reference in Z Direction | `"Z"` | Number | `0` | Optional |
| (7) | 6.1.7 Number of Rebar Constraints: · Value Range: >= 0 | `"NUM"` | Integer | - | **Required** |
| (8) | 6.1.8 Spacing Constraints: · Value Range: >= 0 | `"SPACING"` | Number | `0` | Optional |
| (9) | 6.1.9 Part · 0: "0" · 1: "1" · 2: "2" — Allowed values depend on the section: non-composite 0, 1 or 2; concrete composite 1 or 2; steel composite 2. | `"PART"` | Integer | - | **Required** |

### Request / Response JSON

**종방향철근** — 공식 예제는 I·J단 각 14개이며, 아래는 각 단의 앞 2개만 발췌한 것입니다.

```json
{
  "Assign": {
    "401": {
      "OPT_MBAR_J": false,
      "OPT_SBAR_J": false,
      "OPT_CRACKED": false,
      "SBAR_ITEMS": [
        {
          "OPT_DR": false,
          "OPT_SBW": false,
          "OPT_TR": false,
          "OPT_SR": false,
          "OPT_LBAR_FLG": false
        }
      ],
      "MBARS": [
        {
          "MBAR_ITEMS": [
            {
              "IJ": "I",
              "NAME": "#18",
              "REF_Y": 1,
              "Y": 3.63,
              "REF_Z": 1,
              "Z": 2.148120340131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#18",
              "REF_Y": 0,
              "Y": 0,
              "REF_Z": 0,
              "Z": 0.1,
              "NUM": 2,
              "SPACING": 0.1,
              "PART": 0
            }
          ]
        },
        {
          "MBAR_ITEMS": [
            {
              "IJ": "J",
              "NAME": "#18",
              "REF_Y": 1,
              "Y": 3.63,
              "REF_Z": 1,
              "Z": 2.148120340131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#18",
              "REF_Y": 0,
              "Y": 0,
              "REF_Z": 0,
              "Z": 0.1,
              "NUM": 2,
              "SPACING": 0.1,
              "PART": 0
            }
          ]
        }
      ]
    }
  }
}
```

**전단철근**

```json
{
  "Assign": {
    "1": {
      "OPT_MBAR_J": true,
      "OPT_SBAR_J": false,
      "OPT_CRACKED": false,
      "MBARS": [
        {
          "MBAR_ITEMS": [
            {
              "IJ": "I",
              "NAME": "D16",
              "REF_Y": 1,
              "Y": 610,
              "REF_Z": 0,
              "Z": 250,
              "NUM": 1,
              "SPACING": 0,
              "PART": 1
            }
          ]
        }
      ],
      "SBAR_ITEMS": [
        {
          "OPT_DR": true,
          "DR_PITCH": 100,
          "DR_THETA": 90,
          "DR_AW": 402.2,
          "OPT_SBW": false,
          "OPT_TR": true,
          "TR_PITCH": 150,
          "TR_AWT": 402.2,
          "TR_ALT": 4022,
          "OPT_SR": false,
          "OPT_LBAR_FLG": false
        },
        {
          "OPT_DR": true,
          "DR_PITCH": 100,
          "DR_THETA": 90,
          "DR_AW": 402.2,
          "OPT_SBW": false,
          "OPT_TR": true,
          "TR_PITCH": 150,
          "TR_AWT": 402.2,
          "TR_ALT": 4022,
          "OPT_SR": false,
          "OPT_LBAR_FLG": false
        }
      ]
    }
  }
}
```

### Python 예제

```python
# 전단철근만 변경: "MBARS": [] 는 기존 종방향철근을 유지합니다 (PUT)
rpsc_data = {
    "Assign": {
        "1": {
            "OPT_MBAR_J": True, "OPT_SBAR_J": True,
            "MBARS": [],
            "SBAR_ITEMS": [
                {"OPT_DR": True, "DR_PITCH": 100, "DR_THETA": 90, "DR_AW": 402.2}
            ]
        }
    }
}
midas_api("PUT", "/db/RPSC", rpsc_data)
```

---

## 17. `/db/STRPSSM`

> **Section Manager – Stress Points** — 단면 추가 응력 계산 점을 정의합니다.

- **URL**: `{base url}/db/STRPSSM`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Stress Points ↗](https://support.midasuser.com/hc/en-us/articles/35943448721177)

### ADDITIONAL — 좌표 Key 개정 (2026-11-25 공식 반영)

> 좌표 객체의 Key가 `"PY"`/`"PZ"` → **`"Y"`/`"Z"`**이며, JSON Schema는 그 밖의 Key를 허용하지
> 않습니다(`additionalProperties: false`). 공식 문서 기준입니다.

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Same Additional Stress Points Data at i and j-end When true, POINT1 is also applied to the j-end and POINT2 is ignored. If omitted on PUT, the stored value is kept. | `"OPT_SAME_J"` | Boolean | `true` | Optional |
| 2 | Number of Stress Point for I Stored as the number of items in POINT1; a different value is ignored. | `"POINT_SIZE_1"` | Integer | - | **Required** |
| 3 | Number of Stress Point for J Stored as the number of items in POINT2; a different value is ignored. | `"POINT_SIZE_2"` | Integer | - | **Required** |
| 4 | Stress Point Coordinates for I · Insert the data as an object | `"POINT1"` | Array[Object] | - | **Required** |
| (1) | └ Point Y | `"Y"` | Number | - | **Required** |
| (2) | └ Point Z | `"Z"` | Number | - | **Required** |
| 5 | Stress Point Coordinates for J · Insert the data as an object Used only when OPT_SAME_J is false. | `"POINT2"` | Array[Object] | - | **Required** |
| (1) | └ Point Y | `"Y"` | Number | - | **Required** |
| (2) | └ Point Z | `"Z"` | Number | - | **Required** |

### Request / Response JSON

```json
{
  "Assign": {
    "9003": {
      "OPT_SAME_J": false,
      "POINT_SIZE_1": 2,
      "POINT_SIZE_2": 2,
      "POINT1": [{"Y": 0.00583, "Z": 0.00476}, {"Y": -0.00506, "Z": 0.00097}],
      "POINT2": [
        {"Y": 0.007067356048348719, "Z": 0.005572125828318985},
        {"Y": -0.0059233102292634635, "Z": 0.0011354962297204655}
      ]
    }
  }
}
```

### Python 예제

```python
strpssm_data = {
    "Assign": {
        "9003": {
            "OPT_SAME_J": True,
            "POINT_SIZE_1": 2, "POINT_SIZE_2": 2,
            "POINT1": [{"Y": 0.00583, "Z": 0.00476}, {"Y": -0.00506, "Z": 0.00097}],
            "POINT2": [{"Y": 0.00583, "Z": 0.00476}, {"Y": -0.00506, "Z": 0.00097}]
        }
    }
}
midas_api("POST", "/db/STRPSSM", strpssm_data)
```

---

## 18. `/db/PSSF`

> **Section Manager – Plate Stiffness Scale Factor** — 판 요소 강성 수정 계수를 설정합니다.

- **URL**: `{base url}/db/PSSF`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Plate Stiffness Scale Factor ↗](https://support.midasuser.com/hc/en-us/articles/35943557337753)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Items (Array of Objects) | `"ITEMS"` | Array[Object] | - | **Required** |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Axial Fxx Scale Factor | `"AXIAL_X"` | Number | 1 | Optional |
| (4) | Axial Fyy Scale Factor | `"AXIAL_Y"` | Number | 1 | Optional |
| (5) | Shear Fxy Scale Factor | `"SHEAR"` | Number | 1 | Optional |
| (6) | Bending Mxx Scale Factor | `"OUT_BENDING_X"` | Number | 1 | Optional |
| (7) | Bending Myy Scale Factor | `"OUT_BENDING_Y"` | Number | 1 | Optional |
| (8) | Bending Mxy Scale Factor | `"OUT_TORSION"` | Number | 1 | Optional |
| (9) | Shear Vxx Scale Factor | `"OUT_SHEAR_X"` | Number | 1 | Optional |
| (10) | Shear Vyy Scale Factor | `"OUT_SHEAR_Y"` | Number | 1 | Optional |

### Request Body

```json
{
  "Assign": {
    "12": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service",
        "AXIAL_X": 0.6, "AXIAL_Y": 0.7, "SHEAR": 0.8,
        "OUT_BENDING_X": 0.9, "OUT_BENDING_Y": 1.0,
        "OUT_TORSION": 1.1, "OUT_SHEAR_X": 1.0, "OUT_SHEAR_Y": 1.0
      }]
    }
  }
}
```

---

## 19. `/db/VBEM`

> **Virtual Beam** — 결과력 계산을 위한 가상 보 단면을 정의합니다. 가상 단면 2개로 구성됩니다.

- **URL**: `{base url}/db/VBEM`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Virtual Beam ↗](https://support.midasuser.com/hc/en-us/articles/35943802727065)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Virtual Section 1 | `"VSEC1"` | Integer | - | **Required** |
| 2 | Virtual Section 2 | `"VSEC2"` | Integer | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": { "VSEC1": 1, "VSEC2": 2 }
  }
}
```

---

## 20. `/db/VSEC`

> **Virtual Section** — 결과력 계산용 가상 단면을 정의합니다. 절점 목록과 법선 벡터를 사용합니다.

- **URL**: `{base url}/db/VSEC`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Virtual Section ↗](https://support.midasuser.com/hc/en-us/articles/35943859944729)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Name | `"NAME"` | String | - | **Required** |
| 2 | Centroid Calculation Type | `"CENT_CALC_TYPE"` | Integer | - | **Required** |
| 3 | Centroid X (Global) | `"CEN_PT_X"` | Number | - | **Required** |
| 4 | Centroid Y (Global) | `"CEN_PT_Y"` | Number | - | **Required** |
| 5 | Centroid Z (Global) | `"CEN_PT_Z"` | Number | - | **Required** |
| 6 | Direction Normal Vector (X) | `"NORMAL_X"` | Number | - | **Required** |
| 7 | Direction Normal Vector (Y) | `"NORMAL_Y"` | Number | - | **Required** |
| 8 | Direction Normal Vector (Z) | `"NORMAL_Z"` | Number | - | **Required** |
| 9 | Node List | `"NODE_LIST"` | Integer | - | **Required** |
| 10 | Element List | `"ELEM_LIST"` | Integer | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "Girder_I_Section",
      "CENT_CALC_TYPE": 0,
      "CEN_PT_X": 0, "CEN_PT_Y": 18.0, "CEN_PT_Z": 0.934,
      "NORMAL_X": 1, "NORMAL_Y": 0, "NORMAL_Z": 0,
      "NODE_LIST": [20, 29, 26, 23],
      "ELEM_LIST": [10, 11, 12]
    }
  }
}
```

<!-- om-fields:35943859944729 -->
**OM 원문 추가 필드 — Section Manager - Section for Resultant Forces - Virtual Section ([35943859944729](https://support.midasuser.com/hc/en-us/articles/35943859944729))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `__DESC__`, `__TYPE__`

<!-- /om-fields -->


---

## 21. `/db/EWSF`

> **Effective Width Scale Factor** — 유효 폭 축소 계수를 단면에 할당합니다.

- **URL**: `{base url}/db/EWSF`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Effective Width Scale Factor ↗](https://support.midasuser.com/hc/en-us/articles/35943954272281)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Items (Array of Objects) | `"ITEMS"` | Array[Object] | - | **Required** |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | ly Scale Factor for Sbz (I-End) | `"LYSCALE"` | Number | 1 | **Required** |
| (4) | z_top Scale Factor (I-End) | `"ZTSCALE"` | Number | 1 | **Required** |
| (5) | z_bot Scale Factor (I-End) | `"ZBSCALE"` | Number | 1 | **Required** |
| (6) | J-End Option | `"bJ"` | Boolean | false | **Required** |
| (7) | ly Scale Factor (J-End) | `"LYSCALE_J"` | Number | 1 | Optional |
| (8) | z_top Scale Factor (J-End) | `"ZTSCALE_J"` | Number | 1 | Optional |
| (9) | z_bot Scale Factor (J-End) | `"ZBSCALE_J"` | Number | 1 | Optional |

### Request Body

```json
{
  "Assign": {
    "10": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service",
        "LYSCALE": 0.5, "ZTSCALE": 0.6, "ZBSCALE": 0.7,
        "bJ": true,
        "LYSCALE_J": 0.8, "ZTSCALE_J": 0.9, "ZBSCALE_J": 1.0
      }]
    }
  }
}
```

---

## 22. `/db/IEHC`

> **Inelastic Hinge Control Data** — 비선형 힌지 제어 데이터(섬유 분할 수 등)를 설정합니다.

- **URL**: `{base url}/db/IEHC`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Inelastic Hinge Control Data ↗](https://support.midasuser.com/hc/en-us/articles/35944093809689)

### Specifications

> ⚠️ **2026-08-25 재확인 전면 보강.** Cover(피복) 관련 Beam 필드 2개와 GEN 전용 Wall 관련
> 필드 9개가 통째로 빠져 있었다(아티클 id `35944093809689`). 기존 Request Body 예제도
> `CoverDivNumNy`/`CoverDivNumNz`처럼 원문에 없는 키를 쓰고 있었는데, 실제 키는
> `BeamDivNumNyCover`/`BeamDivNumNzCover`다 — 원문 Examples 그대로 교체했다.

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Reference Location for Distributed Hinges · I-End: `0` / Center: `1` / J-End: `2` | `"BEAM_LOC"` | Integer | - | **Required** |
| 2 | Consider Reinforcement Area | `"OPT_ConsiderRebarArea1D"` | Boolean | - | **Required** |
| 3 | Fiber Beam Areas Core · Auto Size: `0` / Equal-Size: `1` | `"FAreaSizeCore"` | Integer | - | **Required** |
| 4 | Number of Divisions(Beam-Column) — Ny (y-dir) | `"BeamDivNumNy"` | Integer | - | **Required** |
| 5 | Number of Divisions(Beam-Column) — Nz (z-dir) | `"BeamDivNumNz"` | Integer | - | **Required** |
| 6 | Fiber Beam Areas Cover · Auto Size: `0` / Equal-Size: `1` | `"FAreaSizeCover"` | Integer | - | **Required** |
| 7 | Number of divisions(Beam-Column, Cover) — Ny | `"BeamDivNumNyCover"` | Integer | - | **Required** |
| 8 | Number of divisions(Beam-Column, Cover) — Nz | `"BeamDivNumNzCover"` | Integer | - | **Required** |

#### GEN 전용 필드 (Wall/벽체)

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 9 | Consider Out of Plane Nonlinearity of Plate Type | `"WallConsOut"` | Boolean | - | **Required** |
| 10 | Fiber Wall Areas Core | `"WAreaSize"` | Integer | - | **Required** |
| 11 | Number of divisions — z, Core | `"WallDivNumZ"` | Integer | - | **Required** |
| 12 | Number of divisions — y, Core | `"WallDivNumY"` | Integer | - | **Required** |
| 13 | Fiber Wall Areas Cover | `"WAreaSizeCover"` | Integer | - | **Required** |
| 14 | Number of divisions — z, Cover | `"WallDivNumZCover"` | Integer | - | **Required** |
| 15 | Number of divisions — y, Cover | `"WallDivNumYCover"` | Integer | - | **Required** |
| 16 | Wall, Consider Rebar Area | `"OPT_ConsiderRebarAreaWall"` | Boolean | - | **Required** |
| 17 | Shear Spring Location | `"dR"` | Number | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "BEAM_LOC": 1,
      "BeamDivNumNy": 15,
      "BeamDivNumNz": 20,
      "WallConsOut": false,
      "WallDivNumZ": 8,
      "WallDivNumY": 1,
      "dR": 0.4,
      "WAreaSize": "AUTO",
      "OPT_ConsiderRebarArea1D": false,
      "OPT_ConsiderRebarAreaWall": false,
      "FAreaSizeCore": 1,
      "FAreaSizeCover": 1,
      "WAreaSizeCover": 1,
      "BeamDivNumNyCover": 20,
      "BeamDivNumNzCover": 15,
      "WallDivNumZCover": 8,
      "WallDivNumYCover": 1
    }
  }
}
```

> ⚠️ 원문 Specifications 표는 `"WAreaSize"`를 Integer로 명시하지만, 원문 Request Example은
> 문자열 `"AUTO"`를 그대로 전송한다. 이 저장소 관례상 예제가 표보다 우선하므로 예제 값을
> 그대로 옮겼다 — 실제 전송 시 표기(Integer vs `"AUTO"`)에 유의할 것.

---

## 23. `/db/IEHG`

> **Assign Inelastic Hinge Properties** — 비선형 힌지 속성(Inelastic Hinge Property + Fiber Division)을 요소에 할당합니다.

- **URL**: `{base url}/db/IEHG`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinge Properties ↗](https://support.midasuser.com/hc/en-us/articles/35944228031001)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Name of Inelastic Hinge Property | `"PROP_NAME"` | String | - | **Required** |
| 2 | Name of Fiber Division | `"FIBER_NAME"` | String | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "2101": {
      "PROP_NAME": "Fiber_Auto",
      "FIBER_NAME": "B2102_Column12"
    }
  }
}
```

---

## 24. `/db/IEHG-BEAM-M1`

> **Assign Inelastic Hinges – Beam (Hyper-S)** — Hyper-S 전용 보 요소 비선형 힌지 할당.

- **URL**: `{base url}/db/IEHG-BEAM-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - Beam ↗](https://support.midasuser.com/hc/ko/articles/57668691043865)

```python
result = midas_api("GET", "/db/IEHG-BEAM-M1")
```

<!-- om-fields:57656773423385 -->
**OM 원문 추가 필드 — Assign Inelastic Hinges - Beam ([57656773423385](https://support.midasuser.com/hc/en-us/articles/57656773423385))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Inelastic Hinge Property | `"INEL_PROP_NAME"` | string | - | **Required** |

<!-- /om-fields -->


---

## 25. `/db/IEHG-TRUSS-M1`

> **Assign Inelastic Hinges – Truss (Hyper-S)** — Hyper-S 전용 트러스 요소 비선형 힌지 할당.

- **URL**: `{base url}/db/IEHG-TRUSS-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - Truss ↗](https://support.midasuser.com/hc/ko/articles/57668724267545)

```python
result = midas_api("GET", "/db/IEHG-TRUSS-M1")
```

<!-- om-fields:57656796689177 -->
**OM 원문 추가 필드 — Assign Inelastic Hinges - Truss ([57656796689177](https://support.midasuser.com/hc/en-us/articles/57656796689177))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Inelastic Hinge Property | `"INEL_PROP_NAME"` | string | - | **Required** |

<!-- /om-fields -->


---

## 26. `/db/IEHG-GL-M1`

> **Assign Inelastic Hinges – General Link (Hyper-S)** — Hyper-S 전용 일반 링크 비선형 힌지 할당.

- **URL**: `{base url}/db/IEHG-GL-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - General Link ↗](https://support.midasuser.com/hc/ko/articles/57668691115801)

```python
result = midas_api("GET", "/db/IEHG-GL-M1")
```

<!-- om-fields:57656799110937 -->
**OM 원문 추가 필드 — Assign Inelastic Hinges - General Link ([57656799110937](https://support.midasuser.com/hc/en-us/articles/57656799110937))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Inelastic Hinge Property | `"INEL_PROP_NAME"` | string | - | **Required** |

<!-- /om-fields -->


---

## 27. `/db/IEHG-PSS-M1`

> **Assign Inelastic Hinges – Point Spring Support (Hyper-S)** — Hyper-S 전용 점 스프링 지지 비선형 힌지 할당.

- **URL**: `{base url}/db/IEHG-PSS-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - Point Spring Support ↗](https://support.midasuser.com/hc/ko/articles/57668755432473)

```python
result = midas_api("GET", "/db/IEHG-PSS-M1")
```

<!-- om-fields:57656826629657 -->
**OM 원문 추가 필드 — Assign Inelastic Hinges - Point Spring Support ([57656826629657](https://support.midasuser.com/hc/en-us/articles/57656826629657))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Inelastic Hinge Property | `"INEL_PROP_NAME"` | string | - | **Required** |

<!-- /om-fields -->


---

## 28. `/db/FIMP`

> **Inelastic Material Properties** — 섬유 모델 비선형 재료를 정의합니다. 콘크리트(Kent&Park, Mander 등)와 강재(Bilinear, Menegotto-Pinto 등) 다양한 이력 모델을 지원합니다.

- **URL**: `{base url}/db/FIMP`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Inelastic Material Properties ↗](https://support.midasuser.com/hc/en-us/articles/35944335180569)

### JSON Schema

```json
{
  "FIMP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":      { "description": "Name",            "type": "string" },
      "MATL_TYPE": { "description": "Material Type",   "type": "string" },
      "HYS_MODEL": { "description": "Hysteresis Model","type": "string" },
      "CONC":      { "description": "Concrete Model",  "type": "object" },
      "STEEL":     { "description": "Steel Model",     "type": "object" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Material Name | `"NAME"` | String | - | **Required** |
| 2 | Material Type • Concrete: `"CONC"` • Steel: `"STEEL"` | `"MATL_TYPE"` | String | - | **Required** |
| 3 | Hysteresis Model ¹⁾ | `"HYS_MODEL"` | String | - | **Required** |

> ⚠️ FIMP 원문(아티클 id `35944335180569`)은 콘크리트(Kent&Park·Japanese Standard·Mander 등)와
> 강재(Bilinear·Menegotto-Pinto 등) 다수의 이력 모델을 다루는 5900줄 이상의 방대한 문서다.
> 이 저장소는 그중 가장 많이 쓰이는 **Kent & Park 모델만 대표로 상세 기재**하며, 나머지
> 모델은 `MATL_TYPE`/`HYS_MODEL` 조합으로 존재한다는 사실만 남기고 전수 기재하지 않는다.

#### Concrete — Kent & Park (`"HYS_MODEL": "KPM"`)

| Key | Description | Required |
| --- | --- | --- |
| `"KENPAR"."FC"` | Concrete Strength (fc') | **Required** |
| `"KENPAR"."PARTIAL_FACT"` | Partial Safety Factor | **Required** |
| `"KENPAR"."K"` | Strength/Strain Factor | **Required** |
| `"KENPAR"."EC0"` | Peak Strain (εc0) | **Required** |
| `"KENPAR"."EC1_METHOD"` | Hardening Strain Method · Manual: `0` / Calculation: `1` | **Required** |
| `"KENPAR"."EC1"` | Hardening Strain Manual (εc1) | **Required** |
| `"KENPAR"."Z"` | Hardening Strain Calculation (Z) | **Required** |
| `"KENPAR"."ECU"` | Ultimate Strain (εcu) | **Required** |
| `"KENPAR"."STRENGTH_AFTER"` | Strength After Critical Strain · Zero: `0` / Keep: `1` | **Required** |

### Request Body

```json
{
  "Assign": {
    "3": {
      "NAME": "Conc_Kent&Park",
      "MATL_TYPE": "CONC",
      "HYS_MODEL": "KPM",
      "CONC": {
        "KENPAR": {
          "FC": 30000,
          "PARTIAL_FACT": 1.0,
          "K": 1.0,
          "EC0": 0.002,
          "EC1_METHOD": 1,
          "EC1": 0.0035,
          "Z": 100,
          "ECU": 0.003,
          "STRENGTH_AFTER": 0
        }
      }
    }
  }
}
```

### Python 예제

```python
fimp_data = {
    "Assign": {
        "1": {
            "NAME": "Concrete_KP",
            "MATL_TYPE": "CONC",
            "HYS_MODEL": "KPM",
            "CONC": {
                "KENPAR": {
                    "FC": 24000,          # 압축강도 (kPa)
                    "PARTIAL_FACT": 1.0,
                    "K": 1.0,
                    "EC0": 0.002,         # 최대 변형률
                    "EC1_METHOD": 1,      # 0=수동 입력, 1=계산
                    "EC1": 0.0035,
                    "Z": 100,
                    "ECU": 0.003,
                    "STRENGTH_AFTER": 0   # 0=극한변형률 이후 강도 0, 1=강도 유지
                }
            }
        }
    }
}
midas_api("POST", "/db/FIMP", fimp_data)
```

<!-- om-fields:35944335180569 -->
**OM 원문 추가 필드 — Inelastic Material Properties ([35944335180569](https://support.midasuser.com/hc/en-us/articles/35944335180569))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (1) | Japanese Concrete Standard Specification Model | `"JPSTND"` | Object | - | **Required** |
| iii. | Peak Strain (e’peak) | `"EPEAK"` | Number | - | **Required** |
| (1) | Japan Roadway Specification (H.24) Model | `"JP_H24"` | Object | - | **Required** |
| i. | Concrete Elastic Modulus (Ec) | `"EC"` | Number | - | **Required** |
| ii. | Concrete Strength (σck) | `"SIGMA_CK"` | Number | - | **Required** |
| iii. | Rebar Strength (σsy) | `"SIGMA_SY"` | Number | - | **Required** |
| iv. | Strength Factor (α) | `"ALPHA"` | Number | - | **Required** |
| v. | Tensile Strength (σbt) | `"SIGMA_BT"` | Number | - | **Required** |
| vi. | Horizontal Rebar Area (Ah) | `"AH"` | Number | - | **Required** |
| vii. | Spacing (s) | `"S"` | Number | - | **Required** |
| viii. | Depth (d) | `"D"` | Number | - | **Required** |
| ix. | Strain Factor (β) | `"BETA"` | Number | - | **Required** |
| x. | Stiffness After Critical Strain Property · Keep the Stiffness Down: 0 · Assume Stiffness as Zero: 1 | `"STRENGTH_LIMIT"` | Integer | - | **Required** |
| (1) | Japan Roadway Specification (H.14) Model | `"JP_H14"` | Object | - | **Required** |
| i. | Earthquake Type · Type I: 0 · Type II: 1 | `"EARTHQUAKE_TYPE"` | Integer | - | **Required** |
| ii. | Concrete Elastic Modulus (Ec) | `"EC"` | Number | - | **Required** |
| iii. | Concrete Strength (σck) | `"SIGMA_CK"` | Number | - | **Required** |
| iv. | Rebar Strength (σsy) | `"SIGMA_SY"` | Number | - | **Required** |
| v. | Strength Factor (α) | `"ALPHA"` | Number | - | **Required** |
| vi. | Tensile Strength (σbt) | `"SIGMA_BT"` | Number | - | **Required** |
| vii. | Horizontal Rebar Area (Ah) | `"AH"` | Number | - | **Required** |
| viii. | Spacing (s) | `"S"` | Number | - | **Required** |
| ix. | Depth (d) | `"D"` | Number | - | **Required** |
| x. | Strain Factor (β) | `"BETA"` | Number | - | **Required** |
| xi. | Stiffness After Critical Strain Property · Keep the Stiffness Down: 0 · Assume Stiffness as Zero: 1 | `"STRENGTH_LIMIT"` | Integer | - | **Required** |
| (1) | Nagoya Highway Corporation Model | `"NAGOYA"` | Object | - | **Required** |
| i. | Concrete Strength (σck) | `"SIGMA_CK"` | Number | - | **Required** |
| ii. | Peak Compressive Strain (εcc) | `"EPSILON_CC"` | Number | - | **Required** |
| iv. | Ultimate Compressive Strain (εcu) | `"EPSILON_CU"` | Number | - | **Required** |
| v. | Peak Tensile Strain (εt0) | `"EPSILON_T0"` | Number | - | **Required** |
| vi. | Ultimate Tensile Strain (εtu) | `"EPSILON_TU"` | Number | - | **Required** |
| vii. | Zero Tensile Strength Strain (εt1) | `"EPSILON_T1"` | Number | - | **Required** |
| (1) | Trilinear Concrete Model | `"TRILIN"` | Object | - | **Required** |
| i. | Input Method · σ-ε Method: 0 · σ-α Method: 1 | `"INPUT_METHOD"` | Integer | - | **Required** |
| ii. | Concrete Strength · Index 0: σc1 · Index 1: σc2 · Index 2: σc3 | `"SIGMA_Y_ITEMS"` | Array [Number,3] | - | **Required** |
| iii. | Concrete Compressive Strain for σ-ε Method · Index 0: εc1 · Index 1: εc2 · Index 2: εc3 | `"EPSILON_Y_ITEMS"` | Array [Number,3] | - | **Required** |
| iii. | Concrete Compressive Strain for σ-α Method · Index 0: K1 · Index 1: K2/K1 · Index 2: K3/K1 | `"K_ITEMS"` | Array [Number,3] | - | **Required** |
| iv. | Concrete Tensile Strain · Index 0: ε · Index 1: εt1 · Index 2: εtu | `"EPSILON_T_ITEMS"` | Array [Number,3] | - | **Required** |
| v. | Ultimate Compressive Strain | `"EPSILON_CU"` | Number | - | **Required** |
| (1) | China Concrete Code (GB50010-10) | `"CHGB10"` | Object | - | **Required** |
| i. | Peak Concrete Compressive Strength (fc,r) | `"FCR"` | Number | - | **Required** |
| ii. | Peak Concrete Tensile Strength (ft,r) | `"FTR"` | Number | - | **Required** |
| iii. | Peak Concrete Compressive Strain (εc,r) | `"ECR"` | Number | - | Read Only |
| iv. | Peak Concrete Tensile Strain (εt,r) | `"ETR"` | Number | - | Read Only |
| v. | Concrete Modulus | `"EC"` | Number | - | **Required** |
| (1) | China Concrete Code (GB50010-02) | `"CHGB02"` | Object | - | **Required** |
| i. | Peak Concrete Compressive Strength (fc*) | `"FCK"` | Number | - | **Required** |
| ii. | Peak Concrete Tensile Strength (ft*) | `"FTK"` | Number | - | **Required** |
| iii. | Peak Concrete Compressive Strain (εc) | `"EC"` | Number | - | Read Only |
| iv. | Peak Concrete Tensile Strain (εt) | `"ET"` | Number | - | Read Only |
| (1) | Mander Model | `"MANDER"` | Object | - | **Required** |
| i. | Concrete Type · Unconfined Concrete: 0 · Confined Concrete: 1 | `"CONC_TYPE"` | Integer | - | **Required** |
| ii. | Unconfined Concrete Data ²⁾ | `"UCD"` | Object | - | **Required** |
| iii. | Confinement Effectiveness Coefficient ²⁾ | `"KE"` | Object | - | **Required** |
| iv. | Confined Concrete Strength & Strain ²⁾ | `"CCS"` | Object | - | **Required** |
| v. | Section & Rebar Data Input ²⁾ | `"FIELD_2"` | Object | - | **Required** |
| (1) | Menegotto-Pinto Model | `"MENEGO"` | Object | - | **Required** |
| i. | Steel Strength (fy) | `"FY"` | Number | - | **Required** |
| ii. | Steel Elastic Modulus (E) | `"E"` | Number | - | **Required** |
| iii. | Factor (b) | `"B"` | Number | - | **Required** |
| (1) | Bilinear Model | `"BILINE"` | Object | - | **Required** |
| ii. | Steel Elastic Modulus (E1) | `"E1"` | Number | - | **Required** |
| iii. | Elastic Modulus Ratio (E2/E1) | `"E2E1"` | Number | - | **Required** |
| (1) | Asymmetrical Bilinear Steel Model | `"GENBIL"` | Object | - | **Required** |
| i. | Steel Tensile Strength (σy) | `"SIGMA_Y"` | Number | - | **Required** |
| ii. | Steel Compressive Strength (σcy) | `"SIGMA_CY"` | Number | - | **Required** |
| iii. | Compressive Strain | `"EPSILON_1"` | Number | - | **Required** |
| iv. | Tensile Strain | `"EPSILON_2"` | Number | - | **Required** |
| v. | Elastic Modulus · [E1, E2, E3, E4, E5] | `"E_ITEMS"` | Array [Number,5] | - | **Required** |
| (1) | [Trilinear Steel Model] Asymmetrical Bilinear Steel Model | `"TRILIN"` | Object | - | **Required** |
| ii. | Steel Strength · Index 0: σ1y · Index 1: σ2y · Index 2: σ3y · Index 3: σ'1y · Index 4: σ'2y · Index 5: σ'3y | `"SIGMA_Y_ITEMS"` | Array [Number, 6] | - | **Required** |
| iii. | Steel Strain for σ-ε Method · Index 0: ε1y · Index 1: ε2y · Index 2: ε3y | `"EPSILON_Y_ITEMS"` | Array [Number, 3] | - | **Required** |
| iv. | Steel Modulus for σ-α Method · Index 0: K1 · Index 1: K2/K1 · Index 2: K3/K1 | `"K_ITEMS"` | Array [Number, 3] | - | **Required** |
| (1) | Park Model | `"PARKMD"` | Object | - | **Required** |
| i. | Yield Stress of Steel (fy) | `"FY"` | Number | - | **Required** |
| ii. | Ultimate Stress of Steel (fu) | `"FU"` | Number | - | **Required** |
| iii. | Elastic Modulus of Steel (Es) | `"ES"` | Number | - | **Required** |
| iv. | Strain at the Onset of Strain Hardening (σsh) | `"EPSILON_SH"` | Number | - | **Required** |
| v. | Strain at the Steel Rupture (σsu) | `"EPSILON_SU"` | Number | - | **Required** |
| i. | [Japan Roadway Specification Model] Yield Stress of Steel (ρsy) | `"SIGMA_Y"` | Number | - | **Required** |
| ii. | Elastic Modulus of Steel (Es) | `"ES"` | Number | - | **Required** |
| iii. | Permissible Tensile Strain of Reinforcement (εst) | `"EPSILON_ST"` | Number | - | **Required** |
| 1 | Unconfined Concrete Data | `"UCD"` | Object | - | **Required** |
| (1) | Unconfined Concrete Strength - User Input Option | `"OPT_FCO"` | Boolean | false | Optional |
| (2) | Unconfined Concrete Strength (fco') | `"FCO"` | Number | - | **Required** |
| (3) | Unconfined Concrete Strain - User Input Option | `"OPT_EPSILON_CO"` | Boolean | false | Optional |
| (4) | Unconfined Concrete Strain (fco') | `"EPSILON_CO"` | Number | - | **Required** |
| (5) | Yield Strain for Unconfined Concrete - User Input Option | `"OPT_EPSILON_CY"` | Boolean | false | Optional |
| (6) | Yield Strain for Unconfined Concrete (εcy) | `"EPSILON_CY"` | Number | - | **Required** |
| (7) | Spalling Strain for Unconfined Concrete - User Input Option | `"OPT_EPSILON_SP"` | Boolean | false | Optional |
| (8) | Spalling Strain for Unconfined Concrete (εsp) | `"EPSILON_SP"` | Number | - | **Required** |
| (9) | Elastic Modulus of Concrete Type · Mander et al.: 0 · User Input: 1 | `"IDX_EC"` | Integer | - | **Required** |
| (10) | Elastic Modulus of Concrete (Ec) | `"EC"` | Number | - | **Required** |
| (11) | Tensile Strength of Concrete Type · Mander et al.: 0 · User Input: 1 · Neglect Tensile Strength: 2 | `"IDX_FT"` | Integer | - | **Required** |
| (12) | Tensile Strength of Concrete (ft’) | `"FT"` | Number | - | **Required** |
| (13) | Tensile Strain of Concrete (εt) | `"EPSILON_T"` | Number | - | Read Only |
| 2 | Confinement Effectiveness Coefficient | `"KE"` | Object | - | **Required** |
| (1) | Section & Confinement Rebar Type · Rectangular: 0 · Circular-Hoop Confinement Steel: 1 · User Defined: 2 · Circular-Spiral Confinement Steel: 3 | `"SC_REBAR_TYPE"` | Number | - | **Required** |
| (2) | Area of Effective Concrete Core - User Input Option | `"OPT_ACC"` | Boolean | false | Optional |
| (3) | Area of Effective Concrete Core (Acc) | `"ACC"` | Number | - | **Required** |
| (4) | Total Area of Effectively Confined Core Concrete - User Input Option | `"OPT_AE"` | Boolean | false | Optional |
| (5) | Total Area of Effectively Confined Core Concrete (Ae) | `"AE"` | Number | - | **Required** |
| (6) | Confinement Effectiveness Coefficient - User Input Option | `"OPT_KE"` | Boolean | false | Optional |
| (7) | Confinement Effectiveness Coefficient (ke) | `"KE"` | Number | - | **Required** |
| (8) | Effective Lateral Confining Stress on the Concrete - User Input Option | `"OPT_FL"` | Boolean | false | Optional |
| (9) | Effective Lateral Confining Stress on the Concrete (f’l) | `"FL"` | Number | - | **Required** |
| 3 | Confined Concrete Strength & Strain | `"CCS"` | Object | - | **Required** |
| (1) | Strength of Confined Concrete - User Input Option | `"OPT_FCC"` | Boolean | false | Optional |
| (2) | Strength of Confined Concrete (fcc) | `"FCC"` | Number | - | **Required** |
| (3) | Strain for Confined Concrete - User Input Option | `"OPT_EPSILON_CC"` | Boolean | false | Optional |
| (4) | Strain for Confined Concrete (εcc) | `"EPSILON_CC"` | Number | - | **Required** |
| (5) | Yield Strain for Confined Concrete - User Input Option | `"OPT_EPSILON_CY"` | Boolean | false | Optional |
| (6) | Yield Strain for Confined Concrete (εcy) | `"EPSILON_CY"` | Number | - | **Required** |
| (7) | Ultimate Strain for Confined Concrete - Activation Option | `"OPT_ENABLE_EPSILON_CU"` | Boolean | false | Optional |
| (8) | Ratio of the Volume of Transverse Confining - User Input Option | `"USE_RHO_S"` | Boolean | false | Optional |
| (9) | Ratio of the Volume of Transverse Confining (ρs) | `"RHO_S"` | Number | - | **Required** |
| (10) | Steel Material Type · Not Selected: 0 · Inelastic Steel: 2 | `"IDX_STEEL_MATERIAL"` | Integer | - | **Required** |
| (11) | Ultimate Strain for Confined Concretes - User Input Option | `"USE_EPSILON_CU"` | Boolean | false | Optional |
| (12) | Ultimate Strain for Confined Concretes (εcu) | `"EPSILON_CU"` | Number | - | **Required** |
| 4 | Confined Concrete Strength & Strain | `"FIELD_2"` | Object | - | **Required** |
| (1) | Rectangular Section Data - Input Type · User Input: 1 | `"nRectSectAutoorUser"` | Integer | - | **Required** |
| (2) | Concrete Core Dimension to Center Lines of Perimeter Hoop in y-dir (bc) | `"dXdirectionbc"` | Number | - | **Required** |
| (3) | i-th Clear Transverse Spacing Between Adjacent Longitudinal Rebars in y-dir (w’yi) | `"dXdirectionwxi"` | Number | - | **Required** |
| (4) | Number of Transverse Rebar in y-dir(n) | `"nXdirectionn"` | Integer | - | **Required** |
| (5) | Concrete Core Dimension to Center Lines of Perimeter Hoop in z-dir (dc) | `"dYdirectiondc"` | Number | - | **Required** |
| (6) | i-th Clear Transverse Spacing Between Adjacent Longitudinal Rebars in z-dir (w’zj) | `"dYdirectionwyj"` | Number | - | **Required** |
| (7) | Number of Transverse Rebar in z-dir (m) | `"nYdirectionm"` | Integer | - | **Required** |
| (8) | [Rebar Data] Longitudinal Rebar Type · Rebar Number: 0 · Total Area of Rebars: 1 | `"nLongiRebarType"` | Integer | - | **Required** |
| (9) | Number of Longitudinal Rebar | `"nLongiRebarNum"` | Integer | - | **Required** |
| (10) | Rebar Size of Longitudinal Rebar | `"strLongiRebarSize"` | String | - | **Required** |
| (11) | Total Area of Rebars | `"dLongiRebarArea"` | Number | - | **Required** |
| (12) | Longitudinal Reinforcement Ratio - User Input Option | `"bLongiRebarRatio"` | Boolean | false | Optional |
| (13) | Longitudinal Reinforcement Ratio (ρcc) | `"dLongiRebarRatio"` | Number | - | **Required** |
| (14) | General Confinement Rebar Type · Rebar Size: 0 · Rebar Area: 1 | `"nGeneralRebarType"` | Integer | - | **Required** |
| (15) | Rebar Size of Confinement Rebar | `"strGeneralRebarSize"` | String | - | **Required** |
| (16) | Confinement Rebar Area | `"dGeneralRebarArea"` | Number | - | **Required** |
| (17) | Hoops Space (s) | `"dHoopsSpaceS1"` | Number | - | **Required** |
| (18) | Clear Hoops Space (s') | `"dClearHoopsSpaceS2"` | Number | - | **Required** |
| (19) | Confinement Rebar Number y-dir (ny) | `"nGeneralRebarNumX"` | Integer | - | **Required** |
| (20) | Confinement Rebar Number z-dir (nz) | `"nGeneralRebarNumY"` | Integer | - | **Required** |
| (21) | [Rectangular Section - Effective Lateral Confining Stress] Confinement Rebar Yield Strength - User Input Option | `"bRectStrengthfyh"` | Boolean | false | Optional |
| (22) | Confinement Rebar Yield Strength | `"dRectStrengthfyh"` | Number | - | **Required** |
| (23) | Total Area of Confinement Rebars in y-dir - User Input Option | `"bGeneralAsx"` | Boolean | false | Optional |
| (24) | Total Area of Confinement Rebars in y-dir (Asy) | `"dGeneralAsx"` | Number | - | **Required** |
| (25) | Total Area of Confinement Rebars in z-dir - User Input Option | `"bGeneralAsy"` | Boolean | false | Optional |
| (26) | Total Area of Confinement Rebars in z-dir (Asz) | `"dGeneralAsy"` | Number | - | **Required** |
| (27) | Ratio of the Volume of Transverse Confining Steel to the Volume of Confined Concrete Core in y-dir - User Input Option | `"bRectRatiopx"` | Boolean | false | Optional |
| (28) | Ratio of the Volume of Transverse Confining Steel to the Volume of Confined Concrete Core in y-dir (ρy) | `"dRectRatiopx"` | Number | - | **Required** |
| (29) | Ratio of the Volume of Transverse Confining Steel to the Volume of Confined Concrete Core in z-dir - User Input Option | `"bRectRatiopy"` | Boolean | false | Optional |
| (30) | Ratio of the Volume of Transverse Confining Steel to the Volume of Confined Concrete Core in z-dir (ρz) | `"dRectRatiopy"` | Number | - | **Required** |
| (31) | Effective Lateral Confining Stress on the Concrete in the y-dir - User Input Option | `"bRectStressflx"` | Boolean | false | Optional |
| (32) | Effective Lateral Confining Stress on the Concrete in the y-dir (f’ly) | `"dRectStressflx"` | Number | - | **Required** |
| (33) | Effective Lateral Confining Stress on the Concrete in the z-dir - User Input Option | `"bRectStressfly"` | Boolean | false | Optional |
| (34) | Effective Lateral Confining Stress on the Concrete in the z-dir (f’lz) | `"dRectStressfly"` | Number | - | **Required** |
| (35) | Circular Section Data - Input Type · User Input: 1 | `"nCircSectAutoorUser"` | Integer | - | **Required** |
| (36) | Diameter of Spiral | `"dds"` | Number | - | **Required** |
| (35) | [Circular Section - Effective Lateral Confining Stress] Confinement Rebar Yield Strength - User Input Option | `"bCircularStrengthfyh"` | Boolean | false | Optional |
| (36) | Confinement Rebar Yield Strength (fyh) | `"dCircularStrengthfyh"` | Number | - | **Required** |
| (37) | Area of Confinement Rebar - User Input Option | `"bGeneralRebarArea"` | Boolean | false | Optional |
| (38) | Ratio of Volume of Transverse Confining Steel - User Input Option | `"bCircularRatiops"` | Boolean | false | Optional |
| (39) | Ratio of Volume of Transverse Confining Steel (ρs) | `"dCircularRatiops"` | Number | - | **Required** |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `ASSIGN_TYPE`, `A_B_M`, `A_B_P`, `C_M`, `C_P`, `D_M`, `D_P`, `ELASTIC_MODULUS`, `ENRGDS`, `EPSILON_C`, `EU`, `EUY`, `E_M`, `E_P`, `FMR_ITEMS`, `FSTR`, `FYR`, `INPUT_TYPE`, `ITEMS`, `JPROAD`, `OPT_CYCLIC_DEGRATION`, `OPT_STRENGTH_LOSS`, `OPT_SYMMETRIC`, `OPT_TOTAL_STR_LOSS_AT_E`, `OPT_UNLOADING_STIFF_FACTOR`, `OPT_USE_STRENGTH_LOSS`, `OPT_USE_TOTAL_STR_LOSS_AT_E`, `OPT_USE_YIELD_STRAIN`, `SHAPE_OF_CURVE`, `UNLOADING_STIFF_FACTOR`, `YIELD_STRAINS`, `YIELD_STRENGTHS`

<!-- /om-fields -->


---

## 29. `/db/FIBR`

> **Fiber Division of Section** — 단면을 섬유(Fiber)로 분할하고 비선형 재료를 할당합니다.

- **URL**: `{base url}/db/FIBR`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Fiber Division of Section ↗](https://support.midasuser.com/hc/en-us/articles/35944476555801)

### Specifications

> ⚠️ **2026-08-25 재확인 전면 보강.** `FIBR_BASE[]`의 실제 섬유별 속성(REBAR_NAME/AREA/좌표/
> 재료 연결 등) 8개 필드와 상위 레벨의 모니터링 섬유 지정 2개 필드가 통째로 빠져 있었다
> (아티클 id `35944476555801`). 또한 `FIBR_BASE_KEY`는 표에 Boolean으로 적혀 있었으나 원문
> JSON Schema·Request Example 모두 **Integer**(섬유 식별 키 값, 예: `752`)로 다뤄 정정했다.

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Fiber Division Name | `"NAME"` | String | - | **Required** |
| 2 | Assigned Section ID | `"SECT_KEY"` | Integer | - | **Required** |
| 3 | Assign Type | `"ASSIGN_TYPE"` | Integer | - | **Required** |
| 4 | Inelastic Material Properties Name (6 elements) | `"FIMP_NAME"` | Array[String, 6] | - | **Required** |
| 5 | Inelastic Material Properties Color (6 elements) | `"FIMP_COLOR"` | Array[Object, 6] | - | Optional |
| (1) R/G/B | Color components | `"R"` `"G"` `"B"` | Integer | 0 | Optional |
| 6 | Fiber Division Base Data | `"FIBR_BASE"` | Array[Object] | - | **Required** |
| (1) | Fiber Base Key | `"FIBR_BASE_KEY"` | Integer | - | **Required** |
| (2) | Rebar Name | `"REBAR_NAME"` | String | - | **Required** |
| (3) | Area | `"AREA"` | Number | - | **Required** |
| (4) | Center Y | `"CENTER_Y"` | Number | - | **Required** |
| (5) | Center Z | `"CENTER_Z"` | Number | - | **Required** |
| (6) | Fiber Material ID | `"FIBER_MATL_ID"` | Number | - | **Required** |
| (7) | Area Consider Rebar | `"AREA_CONSIDER_REBAR"` | Number | - | **Required** |
| (8) | Is Rebar | `"OPT_IS_REBAR"` | Boolean | - | **Required** |
| (9) | Point Y | `"POINT_Y"` | Array[Number] | - | **Required** |
| (10) | Point Z | `"POINT_Z"` | Array[Number] | - | **Required** |
| 7 | Monitored Fiber Option | `"OPT_MONITORED_FIBER"` | Boolean | - | **Required** |
| 8 | Monitored Fiber | `"MONITORED_FIBER"` | Array[Integer] | - | Require |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "Column_Fiber",
      "SECT_KEY": 11001,
      "ASSIGN_TYPE": 0,
      "FIMP_NAME": [
        "Steel", "Cover Concrete", "Core Conc 1",
        "Core Conc 1", "Core Conc 1", "Core Conc 1"
      ],
      "FIMP_COLOR": [
        {"R": 255, "G": 0, "B": 0},
        {"R": 128, "G": 128, "B": 128},
        {"R": 0, "G": 128, "B": 0},
        {"R": 0, "G": 128, "B": 0},
        {"R": 0, "G": 128, "B": 0},
        {"R": 0, "G": 128, "B": 0}
      ],
      "FIBR_BASE": [
        {
          "FIBR_BASE_KEY": 752,
          "REBAR_NAME": "",
          "AREA": 0.00688072,
          "CENTER_Y": -1.05047e-16,
          "CENTER_Z": 1.06179,
          "FIBER_MATL_ID": 1,
          "AREA_CONSIDER_REBAR": 0,
          "OPT_IS_REBAR": false,
          "POINT_Y": [0.0527429, 0.0527429, -0.0527429, -0.0527429, 0],
          "POINT_Z": [1.08596, 1.029, 1.029, 1.08596, 1.1025]
        }
      ],
      "OPT_MONITORED_FIBER": true,
      "MONITORED_FIBER": [0, 0, 0, 0, 0, 0]
    }
  }
}
```

---

## 30. `/db/GRDP`

> **Group Damping** — 재료 그룹, 구조 그룹, 경계 그룹별 감쇠비를 설정합니다.

- **URL**: `{base url}/db/GRDP`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Group Damping ↗](https://support.midasuser.com/hc/en-us/articles/35944577940633)

### Specifications

> ⚠️ **2026-08-25 재확인 전면 보강.** 이 엔드포인트는 감쇠비 지정 두 가지 방식 —
> **Strain Energy Proportional**(변형에너지 비례, 모드별 감쇠비 계산)과
> **Element Mass & Stiffness Proportional**(Rayleigh 감쇠 계수 직접/모드 기반 산정) — 을
> 함께 다루는데, 이전 버전은 Strain Energy 쪽 일부(3개 필드)만 있고 Element Mass & Stiffness
> Proportional 계열 18개 필드(그룹별 오버라이드용 `GROUP_DAMPING_ITEMS[]`의 13개 하위 필드
> 포함) 전체와 그룹 우선순위 4개 필드가 통째로 빠져 있었다(아티클 id `35944577940633`).

#### Strain Energy Proportional

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Strain Energy Proportional 사용 여부 | `"bExistStrain"` | Boolean | - | **Required** |
| 2 | Damping Ratio Items(재료/구조군/경계군별 감쇠비) | `"STRAIN_GROUP_ITEMS"` | Array[Object] | - | **Required** |
| (1) | Damping Ratio Type · Material: `"MATERIAL"` / Structure Group: `"STRUCTURE"` / Boundary: `"BOUNDARY"` | `"GROUP_TYPE"` | String | - | **Required** |
| (2) | Damping Ratio Name(재료는 ID, 구조군/경계군은 이름) | `"GROUP_NAME"` | String | - | **Required** |
| (3) | Damping Ratio | `"DAMPING_RATIO"` | Number | - | **Required** |
| 3 | Calculate Only When Used | `"OPT_CALC_WHEN_USED"` | Boolean | - | **Required** |
| 4 | Priority: Material Data vs Structure Group · Material: `0` / Structure Group: `1` | `"STRAIN_GROUP_PRIORITY"` | Integer | - | **Required** |
| 5 | Priority between Structure Groups · Smallest: `0` / Largest: `1` | `"STRAIN_VALUE_PRIORITY"` | Integer | - | **Required** |

#### Element Mass & Stiffness Proportional

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 6 | Element Mass & Stiffness Proportional 사용 여부 | `"bExistElement"` | Boolean | - | **Required** |
| 7 | (미지정 요소) Mass Proportional 옵션 | `"OPT_MASS_PROP_DEFAULT"` | Boolean | `false` | Optional |
| 8 | (미지정 요소) Stiffness Proportional 옵션 | `"OPT_STIFF_PROP_DEFAULT"` | Boolean | `false` | Optional |
| 9 | 직접 입력/모드 기반 산정 · Direct: `0` / Calculate from Modal Damping: `1` | `"DIRECT_CALC_MODE_DEFAULT"` | Integer | - | **Required** |
| 10 | Mass Proportional 값 | `"MASS_COEF_DEFAULT"` | Number | - | **Required** |
| 11 | Stiffness Proportional 값 | `"STIFF_COEF_DEFAULT"` | Number | - | **Required** |
| 12 | 계수 산정 기준 · Frequency: `0` / Period: `1` | `"FREQ_PERIOD_MODE_DEFAULT"` | Integer | - | **Required** |
| 13 | Frequency Mode 1 | `"FREQ_MODE_1_DEFAULT"` | Number | - | **Required** |
| 14 | Frequency Mode 2 | `"FREQ_MODE_2_DEFAULT"` | Number | - | **Required** |
| 15 | Period Mode 1 | `"PERIOD_MODE_1_DEFAULT"` | Number | - | **Required** |
| 16 | Period Mode 2 | `"PERIOD_MODE_2_DEFAULT"` | Number | - | **Required** |
| 17 | Damping Ratio Mode 1 | `"DAMPING_MODE_1_DEFAULT"` | Number | - | **Required** |
| 18 | Damping Ratio Mode 2 | `"DAMPING_MODE_2_DEFAULT"` | Number | - | **Required** |
| 19 | 그룹별 Rayleigh 감쇠 오버라이드 | `"GROUP_DAMPING_ITEMS"` | Array[Object] | - | **Required** |
| 20 | Priority: Material Data vs Structure Group(요소 쪽) | `"ELEM_GROUP_PRIORITY"` | Integer | - | **Required** |
| 21 | Priority between Structure Groups(요소 쪽) | `"ELEM_VALUE_PRIORITY"` | Integer | - | **Required** |

`GROUP_DAMPING_ITEMS[]`는 위 7~18번과 동일한 의미의 필드를 그룹 단위로 오버라이드하며,
`"_DEFAULT"` 접미사만 빠진 이름을 쓴다: `GROUP_TYPE`/`GROUP_NAME`(위 `STRAIN_GROUP_ITEMS`와
동일한 3-way 규칙) + `STIFF_COEF`/`OPT_STIFF_PROP`/`MASS_COEF`/`OPT_MASS_PROP`/
`DIRECT_CALC_MODE`/`FREQ_PERIOD_MODE`/`FREQ_MODE_1`/`FREQ_MODE_2`/`PERIOD_MODE_1`/
`PERIOD_MODE_2`/`DAMPING_RATIO_MODE`/`DAMPING_RATIO_MODE_1`/`DAMPING_RATIO_MODE_2`.

### Request Body

```json
{
  "Assign": {
    "1": {
      "STIFF_COEF_DEFAULT": 0.0848826377636192,
      "MASS_COEF_DEFAULT": 0.04188790133333333,
      "OPT_CALC_WHEN_USED": true,
      "OPT_MASS_PROP_DEFAULT": true,
      "OPT_STIFF_PROP_DEFAULT": true,
      "DIRECT_CALC_MODE_DEFAULT": 1,
      "FREQ_PERIOD_MODE_DEFAULT": 0,
      "FREQ_MODE_1_DEFAULT": 0.1,
      "FREQ_MODE_2_DEFAULT": 0.2,
      "PERIOD_MODE_1_DEFAULT": 0,
      "PERIOD_MODE_2_DEFAULT": 0,
      "DAMPING_MODE_1_DEFAULT": 0.06,
      "DAMPING_MODE_2_DEFAULT": 0.07,
      "bExistElement": true,
      "bExistStrain": true,
      "GROUP_DAMPING_ITEMS": [
        {
          "GROUP_TYPE": "MATERIAL", "GROUP_NAME": "1",
          "STIFF_COEF": 0.005787452574792216, "OPT_STIFF_PROP": true,
          "MASS_COEF": 0.06854383854545451, "OPT_MASS_PROP": true,
          "DIRECT_CALC_MODE": 1, "FREQ_PERIOD_MODE": 0,
          "FREQ_MODE_1": 0.5, "FREQ_MODE_2": 0.6,
          "PERIOD_MODE_1": 0, "PERIOD_MODE_2": 0,
          "DAMPING_RATIO_MODE": 0,
          "DAMPING_RATIO_MODE_1": 0.02, "DAMPING_RATIO_MODE_2": 0.02
        }
      ],
      "STRAIN_GROUP_ITEMS": [
        { "GROUP_TYPE": "MATERIAL", "GROUP_NAME": "1", "DAMPING_RATIO": 0.02 }
      ],
      "ELEM_GROUP_PRIORITY": 0,
      "ELEM_VALUE_PRIORITY": 0,
      "STRAIN_GROUP_PRIORITY": 0,
      "STRAIN_VALUE_PRIORITY": 0
    }
  }
}
```

### Python 예제

```python
# 재료 1번 Strain Energy 감쇠비 2% + Rayleigh 계수(Frequency Mode 1/2 = 0.1/0.2Hz) 설정
grdp_data = {
    "Assign": {
        "1": {
            "bExistStrain": True,
            "bExistElement": True,
            "OPT_CALC_WHEN_USED": True,
            "OPT_MASS_PROP_DEFAULT": True,
            "OPT_STIFF_PROP_DEFAULT": True,
            "DIRECT_CALC_MODE_DEFAULT": 1,   # 1=모드 기반 산정
            "FREQ_PERIOD_MODE_DEFAULT": 0,   # 0=Frequency 기준
            "FREQ_MODE_1_DEFAULT": 0.1,
            "FREQ_MODE_2_DEFAULT": 0.2,
            "PERIOD_MODE_1_DEFAULT": 0,
            "PERIOD_MODE_2_DEFAULT": 0,
            "DAMPING_MODE_1_DEFAULT": 0.06,
            "DAMPING_MODE_2_DEFAULT": 0.07,
            "STIFF_COEF_DEFAULT": 0.0849,
            "MASS_COEF_DEFAULT": 0.0419,
            "STRAIN_GROUP_ITEMS": [
                {"GROUP_TYPE": "MATERIAL", "GROUP_NAME": "1", "DAMPING_RATIO": 0.05}
            ],
            "ELEM_GROUP_PRIORITY": 0,
            "ELEM_VALUE_PRIORITY": 0,
            "STRAIN_GROUP_PRIORITY": 0,
            "STRAIN_VALUE_PRIORITY": 0
        }
    }
}
midas_api("POST", "/db/GRDP", grdp_data)
```

---

## 31. `/db/ESSF`

> **Element Stiffness Scale Factor** — 요소별 단면 강성 수정 계수를 직접 할당합니다.

- **URL**: `{base url}/db/ESSF`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Element Stiffness Scale Factor ↗](https://support.midasuser.com/hc/en-us/articles/44613910309401)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Items (Array of Objects) | `"ITEMS"` | Array[Object] | - | **Required** |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Area (Cross-sectional area) | `"AREA_SF"` | Number | 1.0 | Optional |
| (3) | Asy (Shear area, local y) | `"ASY_SF"` | Number | 1.0 | Optional |
| (4) | Asz (Shear area, local z) | `"ASZ_SF"` | Number | 1.0 | Optional |
| (5) | Ixx (Torsional resistance) | `"IXX_SF"` | Number | 1.0 | Optional |
| (6) | Iyy (Moment of Inertia, y-axis) | `"IYY_SF"` | Number | 1.0 | Optional |
| (7) | Izz (Moment of Inertia, z-axis) | `"IZZ_SF"` | Number | 1.0 | Optional |
| (8) | Weight | `"WGT_SF"` | Number | 1.0 | Optional |
| (9) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (10) | Part(합성단면 전용) · Before: `"Before"` / After: `"After"` / All: `"All"` | `"iPart"` | String | `"Before"` | Optional |

### Request Body

```json
{
  "Assign": {
    "1": {
      "ITEMS": [{
        "ID": 1,
        "AREA_SF": 0.5,
        "ASY_SF": 0.6, "ASZ_SF": 0.7,
        "IXX_SF": 0.8, "IYY_SF": 0.8, "IZZ_SF": 0.9,
        "WGT_SF": 0.95,
        "GROUP_NAME": "",
        "iPart": "All"
      }]
    }
  }
}
```

> ⚠️ **2026-08-25 재확인 보강:** 합성단면 전용 필드 `iPart`(Before/After/All)가 누락돼 있어
> 추가했다(아티클 id `44613910309401`).

### Python 예제

```python
# RC 기둥 균열 단면 강성 저감 (ACI 318 기준: Izz = 0.70, Iyy = 0.70)
essf_data = {
    "Assign": {
        "5": {
            "ITEMS": [{
                "ID": 1,
                "AREA_SF": 1.0,
                "ASY_SF": 1.0, "ASZ_SF": 1.0,
                "IXX_SF": 0.20,  # 비틀림 강성 저감
                "IYY_SF": 0.70,  # 균열 단면
                "IZZ_SF": 0.70,
                "WGT_SF": 1.0,
                "GROUP_NAME": ""
            }]
        }
    }
}
midas_api("POST", "/db/ESSF", essf_data)
```

---

## 32. `/db/MATD`

> **Modify Concrete Materials** — 기존 콘크리트 재료(`TYPE:"CONC"`)의 설계값(강도)·철근 등급을 조회·수정합니다. `/db/MATL`과 달리 **GET/PUT만 지원**합니다.

- **URL**: `{base url}/db/MATD`
- **Methods**: `GET`, `PUT`
- **Source**: [Modify Concrete Materials ↗](https://support.midasuser.com/hc/en-us/articles/35993732216985-Modify-Concrete-Materials)

### Specifications

> ✅ **2026-09-06 해결 확인:** 원문 Specifications 표 4번 Key가 `"RABAR_CODENAME"`(E 누락 오타)
> 이던 것이 2026-09-01 원문 갱신으로 `"REBAR_CODENAME"`으로 정정됐다(재확인 시
> `REBAR_CODENAME` 3회·`RABAR_CODENAME` 0회). 우리 문서는 처음부터 정상 표기였다.
>
> ⚠️ **스키마에만 존재하는 필드(설명 근거 없음).** `DATA1.DESIGN` 하위
> `bLAMBDA`/`dLAMBDA`/`bTRANSFER`/`dTRANSFERFCI` 4개 필드는 JSON Schema에만 있고 원문
> Specifications 표·Request Example 어디에도 설명·예시가 없다 — 경량콘크리트 λ계수·프리스트레스
> 전달강도 관련으로 추정되나 필수 여부·기본값 근거가 없어 참고용으로만 표기한다. 여기에 더해
> **2026-09-01 갱신으로 최상위에 3개 필드가 새로 추가**됐는데(아래 표 참고), 이들 역시 스키마에만
> 있고 표·예제에는 없다.
>
> ✅ **원문 JSON Schema 구문 오류 — 2026-10-04 해결 확인.** 2026-09-06에 발견한 `"bSERVCHECK"` 앞
> 쉼표 누락(`..."type": "number" } "bSERVCHECK": {...`)은 원문 갱신(2026-09-28)으로 정정되었다.

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Material Type (Concrete: `"CONC"`) | `"TYPE"` | String | - | **Required** |
| 2 | Material Name | `"NAME"` | String | - | **Required** |
| 3 | Concrete Material Information | `"DATA1"` | Object | - | **Required** |
| 3-(1) | Material Code Name | `"DATA1.CODENAME"` | String | - | **Required** |
| 3-(3) | Material Grade | `"DATA1.CODEMATLNAME"` | String | - | **Required** |
| 3-(4) | Material Design Values | `"DATA1.DESIGN"` | Object | - | **Required** |
| 3-(4)-i | Strength | `"DATA1.DESIGN.C_FC"` | Number | - | GET only |
| 3-(4)-ii | (추정) Lambda 적용 여부 ⚠️표·예제에 근거 없음 | `"DATA1.DESIGN.bLAMBDA"` | Boolean | - | 불명 |
| 3-(4)-iii | (추정) Lambda 값 ⚠️표·예제에 근거 없음 | `"DATA1.DESIGN.dLAMBDA"` | Number | - | 불명 |
| 3-(4)-iv | Strength (Initial) | `"DATA1.DESIGN.C_FCI"` | Number | - | GET only |
| 3-(4)-v | (추정) Transfer 적용 여부 ⚠️표·예제에 근거 없음 | `"DATA1.DESIGN.bTRANSFER"` | Boolean | - | 불명 |
| 3-(4)-vi | (추정) Transfer 시 fci 값 ⚠️표·예제에 근거 없음 | `"DATA1.DESIGN.dTRANSFERFCI"` | Number | - | 불명 |
| 4 | Rebar Code Name | `"REBAR_CODENAME"` | String | - | **Required** |
| 5 | Main Rebar Name | `"MAINREBAR_REBARNAME"` | String | - | **Required** |
| 6 | Sub Rebar Name | `"SUBREBAR_REBARNAME"` | String | Blank | Optional |
| 7 | Main Rebar (fy) | `"MAINREBAR_B_FY"` | Number | 0 | GET only |
| 8 | Sub Rebar (fy) | `"SUBREBAR_B_FY"` | Number | 0 | GET only |
| 9 | Modulus of Elasticity Ratio Input Option | `"bSERVCHECK"` | Boolean | `true` | Optional |
| 10 | Short-Term Ratio of Modulus of Elasticity | `"dSHORTTERM"` | Number | - | Optional |
| 11 | Long-Term Ratio of Modulus of Elasticity | `"dLONGTERM"` | Number | - | Optional |

> `C_FC`·`C_FCI`·`MAINREBAR_B_FY`·`SUBREBAR_B_FY`는 `CODENAME`/`CODEMATLNAME`/`REBAR_CODENAME`에 종속되는 계산값으로, GET 응답에서만 채워지며 PUT 요청 시에는 무시됩니다.
>
> 9~11번(`bSERVCHECK`/`dSHORTTERM`/`dLONGTERM`)은 2026-09-01 원문 갱신으로 JSON Schema 최상위에
> 추가된 뒤, **2026-09-28 원문 갱신으로 Specifications 표에도 행이 추가되었다**(위 표가 원문 표기 그대로).
>
> ✅ **2026-10-04 재확인:** 원문 JSON Schema의 `SUBREBAR_B_FY` 블록 뒤 쉼표 누락(위 2026-09-06 구문 오류)도
> 현재는 정상 쉼표로 고쳐져 있어 이 블록은 유효한 JSON이다.

### Request Body

```json
{
  "Assign": {
    "1": {
      "TYPE": "CONC",
      "NAME": "C16/20",
      "DATA1": {
        "CODENAME": "EN(RC)",
        "CODEMATLNAME": "C16/20",
        "DESIGN": { "C_FC": 16000, "C_FCI": 11200 }
      },
      "REBAR_CODENAME": "EN04(RC)",
      "MAINREBAR_REBARNAME": "ClassB",
      "SUBREBAR_REBARNAME": "ClassC",
      "MAINREBAR_B_FY": 500000,
      "SUBREBAR_B_FY": 600000
    }
  }
}
```

### Python 예제

```python
# 기존 콘크리트 재료(ID=1)의 철근 등급 수정
matd_data = {
    "Assign": {
        "1": {
            "TYPE": "CONC",
            "NAME": "C16/20",
            "DATA1": {
                "CODENAME": "EN(RC)",
                "CODEMATLNAME": "C16/20"
            },
            "REBAR_CODENAME": "EN04(RC)",
            "MAINREBAR_REBARNAME": "ClassB",
            "SUBREBAR_REBARNAME": "ClassC"
        }
    }
}
midas_api("PUT", "/db/MATD/1", matd_data)
```

---

## 33. `/db/SECV`

> **Virtual Section for Design** — 설계용 가상 보(Virtual Beam)에 지정하는 합성 단면을 정의합니다. 키는 기존 가상 보 번호(`/db/VBEM`)와 일치해야 합니다.

- **URL**: `{base url}/db/SECV`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Properties - Virtual Section for Design ↗](https://support.midasuser.com/hc/en-us/articles/64608751935897-Section-Properties-Virtual-Section-for-Design)

> ⚠️ 공식 아티클은 `SECTTYPE`을 `"COMPOSITE"` 한 가지로만 허용하며, `SHAPE`는 `GI`/`CI`/`CT` 3종입니다. `SECT_AFTER.SLAB`은 공식 Specifications 표에 `Array [any]`로 표기되나 JSON Schema는 `[Bc, tc, Hh[, Sg]]` 3~4개 number로 정의하여 스키마 기준으로 적었습니다. `/db/SECT`의 `COMPOSITE`와 필드 구성이 유사하지만 별도 엔드포인트입니다.
>
> ⚠️ 2026-11-26 공식 개정: JSON Schema에서 "`SECT_BEFORE.SHAPE`가 `CI`/`CT`이면 `SECT_AFTER.SLAB`(3~4개)이 필요"하다는 조건(`allOf` / `if`·`then`)이 삭제되었습니다. `SLAB` 자체의 `minItems: 3`·`maxItems: 4`는 그대로이고, Specifications 표는 여전히 `SLAB`을 Required(CI/CT)로 표기하므로 아래 표는 표 기준으로 유지합니다.

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Section Data Type | `"SECTTYPE"` | String | - | **Required** |
| 2 | Section Name Constraints: · Length: min 1 | `"SECT_NAME"` | String | - | **Required** |
| 3 | Section Data - Before | `"SECT_BEFORE"` | Object | - | Optional |
| 3.1 | └ Cardinal Point | `"OFFSET_PT"` | String | - | Optional |
| 3.2 | └ Offset Center | `"OFFSET_CENTER"` | Integer | - | Optional |
| 3.3 | └ User Offset Reference | `"USER_OFFSET_REF"` | Integer | - | Optional |
| 3.4 | └ Horizontal Offset Option | `"HORZ_OFFSET_OPT"` | Integer | - | Optional |
| 3.5 | └ User Offset Y at I | `"USERDEF_OFFSET_YI"` | Number | - | Optional |
| 3.6 | └ User Offset Y at J | `"USERDEF_OFFSET_YJ"` | Number | - | Optional |
| 3.7 | └ Vertical Offset Option | `"VERT_OFFSET_OPT"` | Integer | - | Optional |
| 3.8 | └ User Offset Z at I | `"USERDEF_OFFSET_ZI"` | Number | - | Optional |
| 3.9 | └ User Offset Z at J | `"USERDEF_OFFSET_ZJ"` | Number | - | Optional |
| 3.10 | └ Consider Shear Deformation | `"USE_SHEAR_DEFORM"` | Boolean | false | Optional |
| 3.11 | └ Consider Warping Effect | `"USE_WARPING_EFFECT"` | Boolean | false | Optional |
| 3.12 | └ Hambly Equivalent Section | `"USE_HAMBLY_EQ"` | Boolean | false | Optional |
| 3.13 | └ Girder Shape · Steel Composite I: "GI" · PSC Composite I: "CI" · PSC Composite T: "CT" | `"SHAPE"` | String | - | **Required** (`SECT_BEFORE` 지정 시) |
| 3.14 | └ Section Data Type | `"DATATYPE"` | Integer | - | Optional |
| 3.15 | └ Section Type | `"TYPE"` | Integer | - | Optional |
| 3.16 | └ I-End Girder Section | `"SECT_I"` | Object | - | Optional |
| 3.16.1 | 　　└ 3.16.1 I-End Section Dimensions — GI uses [B1, B2, B3, B4, H, t1, t2, tw]. | `"vSIZE"` | Array[Number] | - | Optional |
| 3.16.2 | 　　└ 3.16.2 PSC Dimensions A | `"vSIZE_PSC_A"` | Array[Number] | - | Optional |
| 3.16.3 | 　　└ 3.16.3 PSC Dimensions B | `"vSIZE_PSC_B"` | Array[Number] | - | Optional |
| 3.16.4 | 　　└ 3.16.4 PSC Dimensions C | `"vSIZE_PSC_C"` | Array[Number] | - | Optional |
| 3.16.5 | 　　└ 3.16.5 PSC Dimensions D | `"vSIZE_PSC_D"` | Array[Number] | - | Optional |
| 3.16.6 | 　　└ 3.16.6 Use Symmetric Calculation | `"USE_SYM_CALC"` | Boolean | - | Optional |
| 3.16.7 | 　　└ 3.16.7 Section Stiffness | `"SODSTIFF"` | Object | - | Optional |
| 3.16.7.1 | 　　　　└ 3.16.7.1 Torsional Stiffness Number | `"TOSTIFNOS"` | Integer | - | Optional |
| 3.16.7.2 | 　　　　└ 3.16.7.2 Deck Stiffness Number | `"DECKSTIFFNO"` | Integer | - | Optional |
| 3.17 | └ J-End Girder Section | `"SECT_J"` | Object | - | Optional |
| 3.17.1 | 　　└ 3.17.1 J-End Section Dimensions | `"vSIZE"` | Array[Number] | - | Optional |
| 3.18 | └ Y Variation | `"Y_VAR"` | Integer | - | Optional |
| 3.19 | └ Z Variation | `"Z_VAR"` | Integer | - | Optional |
| 3.20 | └ Source Section Type | `"SRC_TYPE"` | Integer | - | Optional |
| 3.21 | └ Modulus Ratio, Steel to Concrete | `"MATL_ELAST"` | Number | - | Optional |
| 3.22 | └ Density Ratio, Steel to Concrete | `"MATL_DENS"` | Number | - | Optional |
| 3.23 | └ Poisson's Ratio of Steel | `"MATL_POIS_S"` | Number | - | Optional |
| 3.24 | └ Poisson's Ratio of Concrete | `"MATL_POIS_C"` | Number | - | Optional |
| 3.25 | └ Material Stiffness Factor | `"MATL_STIF_FACTOR"` | Number | - | Optional |
| 3.26 | └ Thermal Expansion Ratio | `"MATL_THERMAL"` | Number | - | Optional |
| 3.27 | └ Stiffness Calculation Option | `"CALC_STIFF_OPT"` | Integer | - | Optional |
| 3.28 | └ Multiple Modulus Options | `"USE_MULTI_ELAST"` | Boolean | false | Optional |
| 3.29 | └ PSC Shape Option 1 | `"PSC_OPT1"` | String | - | Optional |
| 3.30 | └ PSC Shape Option 2 | `"PSC_OPT2"` | String | - | Optional |
| 3.31 | └ Joint Options | `"JOINT"` | Array[Boolean] | - | Optional |
| 3.32 | └ Long-Term Es/Ec | `"LONGTERM_ESEC"` | Number | - | Optional |
| 3.33 | └ Shrinkage Es/Ec | `"SHRINK_ESEC"` | Number | - | Optional |
| 4 | Section Data - After | `"SECT_AFTER"` | Object | - | Optional |
| 4.1 | └ After-Composite Section | `"SECT_I"` | Object | - | Optional |
| 4.1.1 | 　　└ 4.1.1 After-Composite I-End Dimensions — GI uses [Sg, Top, Bot]. | `"vSIZE"` | Array[Number] | - | Optional |
| 4.2 | └ Slab Dimensions Constraints: · Items: 3 ~ 4 [Bc, tc, Hh[, Sg]]; CI/CT requires 3 or 4 values. | `"SLAB"` | Array[Number] | - | **Required** (`CI`/`CT`) |
| 5 | Composite J-End | `"COMPOSITE_J"` | Object | - | Optional |
| 5.1 | └ Base Section Name | `"DB_NAME"` | String | - | Optional |
| 5.2 | └ J-End Section Name | `"SECT_NAME"` | String | - | Optional |
| 5.3 | └ J-End Composite Dimensions | `"vSIZE"` | Array[Number] | - | Optional |

### Request / Response JSON

```json
{
  "Assign": {
    "1": {
      "SECTTYPE": "COMPOSITE",
      "SECT_NAME": "VB_D1",
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
        "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
        "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": false, "USE_HAMBLY_EQ": false,
        "SHAPE": "CI",
        "SECT_I": {
          "vSIZE_PSC_A": [0, 0.1016, 0.127, 0.0508, 0, 1.1684, 0.2286, 0, 0, 0.2032],
          "vSIZE_PSC_B": [0.1016, 0.6096, 0.4318, 0, 0.3302, 0, 0],
          "vSIZE_PSC_C": [0.1016, 0.127, 0.0508, 0, 1.1684, 0.2286, 0, 0, 0.2032],
          "vSIZE_PSC_D": [0.1016, 0.6096, 0.4318, 0, 0.3302, 0, 0]
        },
        "MATL_ELAST": 1.173905142649464, "MATL_DENS": 1,
        "MATL_POIS_S": 0.167, "MATL_POIS_C": 0.167, "MATL_THERMAL": 1,
        "USE_MULTI_ELAST": false, "PSC_OPT1": "", "PSC_OPT2": "",
        "JOINT": [false, true, false, false, false, true, false, false, false]
      },
      "SECT_AFTER": { "SLAB": [2.5, 0.22, 0.0500003333333333, 0] }
    }
  }
}
```

> GET 응답은 최상위 키가 `"SECV"`이고 그 아래는 `Assign`과 동일한 구조입니다.

### Python 예제

```python
# 가상 보 1번에 PSC Composite I 설계용 단면 지정 (사전에 /db/VBEM 으로 가상 보 정의 필요)
secv_data = {
    "Assign": {
        "1": {
            "SECTTYPE": "COMPOSITE", "SECT_NAME": "VB_D1",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC", "SHAPE": "CI",
                "SECT_I": {
                    "vSIZE_PSC_A": [0, 0.1016, 0.127, 0.0508, 0, 1.1684, 0.2286, 0, 0, 0.2032],
                    "vSIZE_PSC_B": [0.1016, 0.6096, 0.4318, 0, 0.3302, 0, 0],
                    "vSIZE_PSC_C": [0.1016, 0.127, 0.0508, 0, 1.1684, 0.2286, 0, 0, 0.2032],
                    "vSIZE_PSC_D": [0.1016, 0.6096, 0.4318, 0, 0.3302, 0, 0]
                },
                "MATL_ELAST": 1.1739, "MATL_DENS": 1,
                "MATL_POIS_S": 0.167, "MATL_POIS_C": 0.167, "MATL_THERMAL": 1
            },
            "SECT_AFTER": {"SLAB": [2.5, 0.22, 0.05, 0]}
        }
    }
}
midas_api("POST", "/db/SECV", secv_data)
```

---

## 34. `DESIGN/SECT`

> **Section for Design** — 설계용 단면을 정의합니다. 키는 단면 ID이며, 각 값의 구조는
> [`/db/SECT`](#12-dbsect)와 같습니다.

- **URL**: `{base url}/DESIGN/SECT`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [DESIGN/SECT : Section for Design ↗](https://support.midasuser.com/hc/en-us/articles/59471991932441)

> ⚠️ 2026-11-26 문서화. 공식 아티클에는 **요청·응답 예제가 없고**, 본문 필드는 `/db/SECT`의 단면 유형별
> 아티클을 참조하도록 되어 있습니다. 아래 예제는 이 장 12절의 DB/User 단면 구조를 옮긴 것이며

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Keyed object (dictionary). Each property name is a section ID string (e.g., "1"). Each value uses the same payload structure as /db/SECT. | `"Assign"` | Object | - | **Required** |
| 1.1 | └ Section Body ([/db/SECT](#12-dbsect)) | (단면 ID) | Object | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "SECTTYPE": "DBUSER",
      "SECT_NAME": "H300x150",
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "USE_SHEAR_DEFORM": true,
        "SHAPE": "H",
        "DATATYPE": 1,
        "SECT_I": {"DB_NAME": "KS21", "SECT_NAME": "H300x150x6.5/9"}
      }
    }
  }
}
```

### Python 예제

```python
# 설계용 단면 조회
midas_api("GET", "/DESIGN/SECT")
```

<!-- om-fields:59471991932441 -->
**OM 원문 추가 필드 — DESIGN/SECT : Section for Design ([59471991932441](https://support.midasuser.com/hc/en-us/articles/59471991932441))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `article`, `label`, `order`, `vSIZE`

<!-- /om-fields -->


---

## 전체 워크플로우 예제 — 재료·단면·두께 자동 설정

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY"

def midas_api(method, endpoint, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}

# ── Step 1: 재료 정의 ─────────────────────────────────────
midas_api("POST", "/db/MATL", {
    "Assign": {
        "1": {
            "TYPE": "CONC", "NAME": "C24",
            "bMASS_DENS": False, "DAMP_RAT": 0.05,
            "HE_SPEC": 0, "HE_COND": 0, "PLMT": 0, "P_NAME": "",
            "PARAM": [{"P_TYPE": 1, "STANDARD": "KS21(RC)", "CODE": "", "DB": "C24", "bELAST": False}]
        },
        "2": {
            "TYPE": "STEEL", "NAME": "SS400",
            "bMASS_DENS": False, "DAMP_RAT": 0.02,
            "HE_SPEC": 0, "HE_COND": 0, "PLMT": 0, "P_NAME": "",
            "PARAM": [{"P_TYPE": 1, "STANDARD": "KS21(S)", "CODE": "", "DB": "SS400", "bELAST": False}]
        }
    }
})

# ── Step 2: 단면 정의 (H형강 DB) ───────────────────────────
midas_api("POST", "/db/SECT", {
    "Assign": {
        "1": {
            "SECTTYPE": "DBUSER", "SECT_NAME": "H300x150",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",
                "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
                "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
                "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
                "USE_SHEAR_DEFORM": True, "USE_WARPING_EFFECT": True,
                "SHAPE": "H", "DATATYPE": 1,
                "SECT_I": {"DB_NAME": "KS21", "SECT_NAME": "H300x150x6.5/9"}
            }
        },
        "2": {
            "SECTTYPE": "DBUSER", "SECT_NAME": "H400x200",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",
                "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
                "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
                "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
                "USE_SHEAR_DEFORM": True, "USE_WARPING_EFFECT": True,
                "SHAPE": "H", "DATATYPE": 1,
                "SECT_I": {"DB_NAME": "KS21", "SECT_NAME": "H400x200x8/13"}
            }
        }
    }
})

# ── Step 3: 두께 정의 (슬래브, 벽체) ──────────────────────
midas_api("POST", "/db/THIK", {
    "Assign": {
        "1": {"NAME": "Slab_200",  "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.20, "T_OUT": 0, "O_VALUE": 0},
        "2": {"NAME": "Wall_250",  "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.25, "T_OUT": 0, "O_VALUE": 0},
        "3": {"NAME": "Slab_150",  "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.15, "T_OUT": 0, "O_VALUE": 0},
    }
})

print("✓ 재료, 단면, 두께 정의 완료")
```

---

*[04_DB_Properties.md] 작성 완료 — 다음 파일 [05_DB_Boundary.md] 진행 준비가 되었습니다.*
