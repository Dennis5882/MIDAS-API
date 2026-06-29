# 04 DB — Properties

> **Source**: [MIDAS API Online Manual](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **Sync date**: 2026-06-29  
> **Endpoints covered**: `/db/MATL`, `/db/MATL-M1`, `/db/IMFM`, `/db/IMFM-M1`, `/db/TDMF`, `/db/TDMT`, `/db/TDME`, `/db/EDMP`, `/db/TMAT`, `/db/EPMT`, `/db/EPMT-M1`, `/db/SECT`, `/db/THIK`, `/db/TSGR`, `/db/SECF`, `/db/RPSC`, `/db/STRPSSM`, `/db/PSSF`, `/db/VBEM`, `/db/VSEC`, `/db/EWSF`, `/db/IEHC`, `/db/IEHG`, `/db/IEHG-BEAM-M1`, `/db/IEHG-TRUSS-M1`, `/db/IEHG-GL-M1`, `/db/IEHG-PSS-M1`, `/db/FIMP`, `/db/FIBR`, `/db/GRDP`, `/db/ESSF`

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

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "KDS2016",
      "CODE": "KDS2016",
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
            "CODE": "KDS2016",
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

### Specifications (공통 + ACI/KDS)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Material Name | `"NAME"` | String | - | **Required** |
| 2 | Material Type • Code: `"CODE"` • User: `"USER"` | `"TYPE"` | String | - | **Required** |
| 3 (CODE) | Code Name ¹⁾ | `"CODENAME"` | String | - | **Required** |
| 4 (CODE) | Compression Strength | `"STRENGTH"` | Number | - | **Required** |
| 5 (ACI/KDS) | Factor, a | `"A"` | Number | - | **Required** |
| 6 (ACI/KDS) | Factor, b | `"B"` | Number | - | **Required** |
| 5 (CEB-FIP 1990/Ohzagi) | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "TDME_KDS2016",
      "TYPE": "CODE",
      "CODENAME": "KDS2016",
      "STRENGTH": 24000
    }
  }
}
```

### Python 예제

```python
tdme_data = {
    "Assign": {
        "1": {
            "NAME": "CompStr_C24_KDS",
            "TYPE": "CODE",
            "CODENAME": "KDS2016",
            "STRENGTH": 24000
        }
    }
}
midas_api("POST", "/db/TDME", tdme_data)
```

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
      "MOHRCL":     { "description": "Mohr-Coulomb","type": "object" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Plastic Material Name | `"NAME"` | String | - | **Required** |
| 2 | Model Type • `"TR"` (Tresca) • `"VM"` (Von-Mises) • `"MC"` (Mohr-Coulomb) • `"DP"` (Drucker-Prager) • `"MA"` (Masonry) • `"DM"` (Concrete Damage) | `"MODEL_TYPE"` | String | - | **Required** |

#### Tresca / Von-Mises 공통 파라미터 (`"TRESCA"` or `"VMISES"` object)

| Key | Description | Required |
|-----|-------------|----------|
| `"INIT_YIELD_STRESS"` | Initial Uniaxial Yield Stress | **Required** |
| `"OPT_HARDENING"` | Hardening Option (0: Active, 1: Inactive) | Optional |
| `"HARDENING_TYPE"` | `"ISO"` / `"KIN"` / `"MIX"` | Optional |
| `"HARDENING_COEF"` | Hardening Coefficient | Optional |
| `"BACK_STRESS_COEF"` | Back Stress Coefficient (MIX only) | Optional |

#### Mohr-Coulomb 파라미터 (`"MOHRCL"` object)

| Key | Description | Required |
|-----|-------------|----------|
| `"INIT_COHESION"` | Initial Cohesion | **Required** |
| `"INIT_FRIC_ANGLE"` | Initial Friction Angle (deg) | **Required** |
| `"OPT_HARDENING"` | Hardening Option | Optional |

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

---

## 11. `/db/EPMT-M1`

> **Plastic Material (Hyper-S)** — Hyper-S 전용 소성 재료 모델.

- **URL**: `{base url}/db/EPMT-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Plastic Material (Hyper-S) ↗](https://support.midasuser.com/hc/ko/articles/56511025581337)

```python
result = midas_api("GET", "/db/EPMT-M1")
```

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
      "ZDIST":    { "description": "Z axis Symmetric Distance",      "type": "number" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Tapered Group Name | `"NAME"` | String | - | **Required** |
| 2 | Element No. list | `"ELEMLIST"` | Array[Integer] | - | **Required** |
| 3 | Z-axis Section Shape Variation • Linear: `"LINEAR"` • Polynomial: `"POLY"` | `"ZVAR"` | String | - | **Required** |
| 4 | Y-axis Section Shape Variation | `"YVAR"` | String | - | **Required** |
| 5 (POLY only) | Z axis Exponent | `"ZEXP"` | Number | - | **Required** |
| 6 (POLY only) | Z axis Symmetric Plane from i or j | `"ZFROM"` | String | `"i"` | Optional |
| 7 (POLY only) | Z axis Symmetric Plane Distance (m) | `"ZDIST"` | Number | 0 | Optional |

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

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
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

> **Section Manager – Reinforcements** — PSC/RC 단면 철근 배근 데이터를 설정합니다.

- **URL**: `{base url}/db/RPSC`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Reinforcements ↗](https://support.midasuser.com/hc/en-us/articles/35943227821465)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Same Rebar Data at i and j-end (Longitudinal) | `"OPT_MBAR_J"` | Boolean | - | **Required** |
| 2 | Same Shear Rebar Data at i and j-end | `"OPT_SBAR_J"` | Boolean | - | **Required** |
| 3 | Cracked Section | `"OPT_CRACKED"` | Boolean | - | **Required** |
| 4 | Shear Reinforcement Data [i-section, j-section] | `"SBAR_ITEMS"` | Array[Object] | - | **Required** |
| (1) | Diagonal Reinforcement (DR) | `"OPT_DR"` | Boolean | false | Optional |
| (2) | [DR] Pitch | `"DR_PITCH"` | Number | - | Optional |
| (3) | [DR] Angle | `"DR_THETA"` | Number | - | Optional |
| (4) | [DR] Area | `"DR_AW"` | Number | - | Optional |

### Request Body

```json
{
  "Assign": {
    "401": {
      "OPT_MBAR_J": false,
      "OPT_SBAR_J": false,
      "OPT_CRACKED": false,
      "SBAR_ITEMS": [
        { "OPT_DR": false },
        { "OPT_DR": false }
      ]
    }
  }
}
```

---

## 17. `/db/STRPSSM`

> **Section Manager – Stress Points** — 단면 추가 응력 계산 점을 정의합니다.

- **URL**: `{base url}/db/STRPSSM`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Stress Points ↗](https://support.midasuser.com/hc/en-us/articles/35943448721177)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Same Stress Points at i and j-end | `"OPT_SAME_J"` | Boolean | true | Optional |
| 2 | Number of Stress Points (I) | `"POINT_SIZE_1"` | Integer | - | **Required** |
| 3 | Number of Stress Points (J) | `"POINT_SIZE_2"` | Integer | - | **Required** |
| 4 | Stress Point Coordinates (I) | `"POINT1"` | Array[{PY, PZ}] | - | **Required** |
| (1) | Point Y | `"PY"` | Number | - | **Required** |
| (2) | Point Z | `"PZ"` | Number | - | **Required** |
| 5 | Stress Point Coordinates (J) | `"POINT2"` | Array[{PY, PZ}] | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "9003": {
      "OPT_SAME_J": true,
      "POINT_SIZE_1": 2, "POINT_SIZE_2": 2,
      "POINT1": [{"PY": 0.00583, "PZ": 0.00476}, {"PY": -0.00506, "PZ": 0.00097}],
      "POINT2": [{"PY": 0.00583, "PZ": 0.00476}, {"PY": -0.00506, "PZ": 0.00097}]
    }
  }
}
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

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Reference Location for Distributed Hinges • I-End: 0 • Center: 1 • J-End: 2 | `"BEAM_LOC"` | Integer | - | **Required** |
| 2 | Consider Reinforcement Area | `"OPT_ConsiderRebarArea1D"` | Boolean | - | **Required** |
| 3 | Fiber Beam Areas Core • Auto Size: 0 • Equal-Size: 1 | `"FAreaSizeCore"` | Integer | - | **Required** |
| 4 | Number of Divisions (Beam-Column) Ny | `"BeamDivNumNy"` | Integer | - | **Required** |
| 5 | Number of Divisions (Beam-Column) Nz | `"BeamDivNumNz"` | Integer | - | **Required** |
| 6 | Fiber Beam Areas Cover • Auto: 0 • Equal: 1 | `"FAreaSizeCover"` | Integer | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "BEAM_LOC": 1,
      "BeamDivNumNy": 15, "BeamDivNumNz": 20,
      "WallConsOut": false, "WallDivNumZ": 8, "WallDivNumY": 1,
      "dR": 0.4, "WAreaSize": "AUTO",
      "OPT_ConsiderRebarArea1D": false,
      "OPT_ConsiderRebarAreaWall": false,
      "FAreaSizeCore": 1, "FAreaSizeCover": 1,
      "CoverDivNumNy": 3, "CoverDivNumNz": 3
    }
  }
}
```

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

---

## 25. `/db/IEHG-TRUSS-M1`

> **Assign Inelastic Hinges – Truss (Hyper-S)** — Hyper-S 전용 트러스 요소 비선형 힌지 할당.

- **URL**: `{base url}/db/IEHG-TRUSS-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - Truss ↗](https://support.midasuser.com/hc/ko/articles/57668724267545)

```python
result = midas_api("GET", "/db/IEHG-TRUSS-M1")
```

---

## 26. `/db/IEHG-GL-M1`

> **Assign Inelastic Hinges – General Link (Hyper-S)** — Hyper-S 전용 일반 링크 비선형 힌지 할당.

- **URL**: `{base url}/db/IEHG-GL-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - General Link ↗](https://support.midasuser.com/hc/ko/articles/57668691115801)

```python
result = midas_api("GET", "/db/IEHG-GL-M1")
```

---

## 27. `/db/IEHG-PSS-M1`

> **Assign Inelastic Hinges – Point Spring Support (Hyper-S)** — Hyper-S 전용 점 스프링 지지 비선형 힌지 할당.

- **URL**: `{base url}/db/IEHG-PSS-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - Point Spring Support ↗](https://support.midasuser.com/hc/ko/articles/57668755432473)

```python
result = midas_api("GET", "/db/IEHG-PSS-M1")
```

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

#### Concrete — Kent & Park (`"HYS_MODEL": "KPM"`)

| Key | Description |
|-----|-------------|
| `"KENPAR"."FC"` | Concrete Strength (fc') |
| `"KENPAR"."EC0"` | Peak Strain (εc0) |
| `"KENPAR"."K"` | Strength/Strain Factor |
| `"KENPAR"."ECU"` | Ultimate Strain |
| `"KENPAR"."PARTIAL_FACT"` | Partial Safety Factor |

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
          "EC0": 0.002,
          "K": 1.0,
          "ECU": 0.003,
          "PARTIAL_FACT": 1.0
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
                    "FC": 24000,    # 압축강도 (kPa)
                    "EC0": 0.002,   # 최대 변형률
                    "K": 1.0,
                    "ECU": 0.003,
                    "PARTIAL_FACT": 1.0
                }
            }
        }
    }
}
midas_api("POST", "/db/FIMP", fimp_data)
```

---

## 29. `/db/FIBR`

> **Fiber Division of Section** — 단면을 섬유(Fiber)로 분할하고 비선형 재료를 할당합니다.

- **URL**: `{base url}/db/FIBR`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Fiber Division of Section ↗](https://support.midasuser.com/hc/en-us/articles/35944476555801)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Fiber Division Name | `"NAME"` | String | - | **Required** |
| 2 | Assigned Section ID | `"SECT_KEY"` | Integer | - | **Required** |
| 3 | Assign Type | `"ASSIGN_TYPE"` | Integer | - | **Required** |
| 4 | Inelastic Material Properties Name (6 elements) | `"FIMP_NAME"` | Array[String, 6] | - | **Required** |
| 5 | Inelastic Material Properties Color (6 elements) | `"FIMP_COLOR"` | Array[Object, 6] | - | Optional |
| (1) R/G/B | Color components | `"R"` `"G"` `"B"` | Integer | 0 | Optional |
| 6 | Fiber Division Base Data | `"FIBR_BASE"` | Array[Object] | - | **Required** |
| (1) | Base Key | `"FIBR_BASE_KEY"` | Boolean | - | **Required** |

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
      "FIBR_BASE": [{"FIBR_BASE_KEY": true}]
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

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Strain Energy Proportional | `"bExistStrain"` | Boolean | - | **Required** |
| 2 | Damping Ratio Items | `"STRAIN_GROUP_ITEMS"` | Array[Object] | - | **Required** |
| (1) | Damping Ratio Type • Material: `"MATERIAL"` • Structure Group: `"STRUCTURE"` • Boundary: `"BOUNDARY"` | `"GROUP_TYPE"` | String | - | **Required** |
| (2) | Damping Ratio Name | `"GROUP_NAME"` | String | - | **Required** |
| (3) | Damping Ratio | `"DAMPING_RATIO"` | Number | - | **Required** |
| 3 | Calculate Only When Used | `"OPT_CALC_WHEN_USED"` | Boolean | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "bExistStrain": true,
      "STIFF_COEF_DEFAULT": 0.0849,
      "MASS_COEF_DEFAULT": 0.0419,
      "OPT_CALC_WHEN_USED": true,
      "OPT_MASS_PROP_DEFAULT": true,
      "OPT_STIFF_PROP_DEFAULT": true,
      "STRAIN_GROUP_ITEMS": [
        { "GROUP_TYPE": "MATERIAL", "GROUP_NAME": "1", "DAMPING_RATIO": 0.05 }
      ]
    }
  }
}
```

### Python 예제

```python
# 재료 1번 감쇠비 5% 설정
grdp_data = {
    "Assign": {
        "1": {
            "bExistStrain": True,
            "OPT_CALC_WHEN_USED": True,
            "OPT_MASS_PROP_DEFAULT": True,
            "OPT_STIFF_PROP_DEFAULT": True,
            "STIFF_COEF_DEFAULT": 0.0849,
            "MASS_COEF_DEFAULT": 0.0419,
            "STRAIN_GROUP_ITEMS": [
                {"GROUP_TYPE": "MATERIAL", "GROUP_NAME": "1", "DAMPING_RATIO": 0.05}
            ]
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
        "GROUP_NAME": ""
      }]
    }
  }
}
```

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
