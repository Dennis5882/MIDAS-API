# 12. DB – Analysis Control

해석 제어(Analysis Control) 관련 데이터베이스 API입니다. 메인 제어, P-Delta, 좌굴, 고유치, 수화열, 이동하중, 침하, 비선형, 시공단계, 경계 변경 등 해석 옵션을 정의합니다.

> **Base URL**
> - Civil NX : `https://moa-engineers.midasit.com:443/civil`
> - Gen NX   : `https://moa-engineers.midasit.com:443/gen`
>
> **인증 헤더** : 모든 요청에 `MAPI-Key: <your_api_key>` 헤더를 포함해야 합니다.
>
> **Hyper-S (`-M1`) 엔드포인트** : MIDAS Engineering Core(MEC) 기반의 차세대 솔버용 제어 데이터입니다. 중첩 객체 구조와 `enum` 기반 문자열 값을 사용하며, 일부는 `GET, PUT, DELETE`만 지원합니다(POST 미지원).

---

## 목차

| No. | Endpoint | 설명 | 비고 |
|-----|----------|------|------|
| 1 | [/db/ACTL](#1-dbactl--main-control-data) | Main Control Data | |
| 2 | [/db/ACTL-M1](#2-dbactl-m1--main-control-data-hyper-s) | Main Control Data | Hyper-S |
| 3 | [/db/PDEL](#3-dbpdel--p-delta-analysis-control) | P-Delta Analysis Control | |
| 4 | [/db/BUCK](#4-dbbuck--buckling-analysis-control) | Buckling Analysis Control | |
| 5 | [/db/EIGV](#5-dbeigv--eigenvalue-analysis-control) | Eigenvalue Analysis Control | |
| 6 | [/db/EIGV-M1](#6-dbeigv-m1--eigenvalue-analysis-control-hyper-s) | Eigenvalue Analysis Control | Hyper-S |
| 7 | [/db/HHCT](#7-dbhhct--heat-of-hydration-analysis-control) | Heat of Hydration Analysis Control | |
| 8 | [/db/HHCT-M1](#8-dbhhct-m1--heat-of-hydration-analysis-control-hyper-s) | Heat of Hydration Analysis Control | Hyper-S |
| 9 | [/db/MVCT](#9-dbmvct--moving-load-analysis-control) | Moving Load Analysis Control | |
| 10 | [/db/MVCTch](#10-dbmvctch--moving-load-analysis-control--china) | Moving Load Analysis Control – China | |
| 11 | [/db/MVCTid](#11-dbmvctid--moving-load-analysis-control--india) | Moving Load Analysis Control – India | |
| 12 | [/db/MVCTbs](#12-dbmvctbs--moving-load-analysis-control--bs) | Moving Load Analysis Control – BS | |
| 13 | [/db/MVCTtr](#13-dbmvcttr--moving-load-analysis-control--transverse) | Moving Load Analysis Control – Transverse | |
| 14 | [/db/SMCT](#14-dbsmct--settlement-analysis-control-data) | Settlement Analysis Control Data | |
| 15 | [/db/NLCT](#15-dbnlct--nonlinear-analysis-control-data) | Nonlinear Analysis Control Data | |
| 16 | [/db/NLCT-M1](#16-dbnlct-m1--nonlinear-analysis-control-hyper-s) | Nonlinear Analysis Control | Hyper-S |
| 17 | [/db/STCT](#17-dbstct--construction-stage-analysis-control-data) | Construction Stage Analysis Control Data | |
| 18 | [/db/STCT-M1](#18-dbstct-m1--construction-stage-analysis-control-data-hyper-s) | Construction Stage Analysis Control Data | Hyper-S |
| 19 | [/db/BCCT](#19-dbbcct--boundary-change-assignment) | Boundary Change Assignment | |
| 20 | [/db/BCGD-M1](#20-dbbcgd-m1--define-boundary-combination-hyper-s) | Define Boundary Combination | Hyper-S |
| 21 | [/db/BCGA-M1](#21-dbbcga-m1--assign-boundary-combination-hyper-s) | Assign Boundary Combination | Hyper-S |

---

## 1. /db/ACTL — Main Control Data

해석의 기본 제어 데이터를 정의합니다. 자동 구속, 반복 횟수, 수렴 허용오차 등을 설정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/ACTL` | 메인 제어 데이터 생성 |
| GET | `{base_url}/db/ACTL` | 조회 |
| PUT | `{base_url}/db/ACTL/{id}` | 수정 |
| DELETE | `{base_url}/db/ACTL/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Auto Rotational DOF Constraint for Truss / Plane Stress / Solid Elements | `"ARDC"` | Boolean | false | Optional |
| 2 | Auto Normal Rotation Constraint for Plate Elements | `"ANRC"` | Boolean | false | Optional |
| 3 | Consider Section Stiffness Scale Factor for Stress Calculation | `"CSECF"` | Boolean | false | Optional |
| 4 | Transfer Reactions of Slave Node to the Master Node | `"TRS"` | Boolean | false | Optional |
| 5 | Calculate Equivalent Beam Stresses (Von-Mises and Max-Shear) | `"BMSTRESS"` | Boolean | false | Optional |
| 6 | Consider Reinforcement for Section Stiffness Calculation | `"CRBAR"` | Boolean | false | Optional |
| 7 | Change Local Axis of Tapered Section for Force / Stress Calculation | `"CLATS"` | Boolean | false | Optional |
| 8 | Number of Iterations / Load Case | `"ITER"` | Number | - | Required |
| 9 | Convergence Tolerance | `"TOL"` | Number | - | Required |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "ARDC": true,
      "ANRC": true,
      "ITER": 20,
      "TOL": 0.001,
      "CSECF": false,
      "TRS": true,
      "CRBAR": false,
      "BMSTRESS": false,
      "CLATS": false
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_main_control():
    payload = {
        "Assign": {
            "1": {
                "ARDC": True,      # 트러스/평면응력/솔리드 요소 자동 회전 구속
                "ANRC": True,      # 판 요소 자동 법선 회전 구속
                "ITER": 20,        # 하중케이스당 반복 횟수
                "TOL": 0.001,      # 수렴 허용오차
                "CSECF": False,    # 응력계산 시 단면강성 스케일계수 고려
                "TRS": True,       # 종속절점 반력을 주절점으로 전달
                "CRBAR": False,    # 단면강성 계산 시 철근 고려
                "BMSTRESS": False, # 등가 보 응력 계산
                "CLATS": False     # 변단면 국부축 변경
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/ACTL", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Main Control Data set:", resp.json())

set_main_control()
```

---

## 2. /db/ACTL-M1 — Main Control Data (Hyper-S)

Hyper-S(MEC) 솔버용 메인 제어 데이터입니다. 인장/압축 트러스 요소(Tension/Compression Truss)에 대한 고급 비선형 파라미터(`TCELEM`)를 중첩 객체로 포함합니다.

> **Active Methods**: `GET, PUT, DELETE`(POST 미지원). 원문에 POST가 없는 이유는 설명돼 있지 않다
> — ⚠️ 2026-08-30 확인: 이전에 "기본 레코드가 자동 생성됨"이라는 근거를 달아 뒀으나, 원문 어디에도
> 그런 설명이 없어 근거 없는 추정이었음이 확인돼 삭제한다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| GET | `{base_url}/db/ACTL-M1` | 조회 |
| PUT | `{base_url}/db/ACTL-M1/{id}` | 수정 |
| DELETE | `{base_url}/db/ACTL-M1/{id}` | 삭제 |

### Parameters — 기본 설정

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Auto Rotational DOF Constraint | `"ARCD"` | Boolean | true | Optional |
| 2 | Auto Normal Rotation Constraint | `"ANRC"` | Boolean | true | Optional |
| 3 | Consider Section Stiffness Scale Factor | `"CSECF"` | Boolean | false | Optional |
| 4 | Consider Reinforcement for Section Stiffness | `"CRBAR"` | Boolean | false | Optional |
| 5 | Transfer Reactions to Master Node | `"TRS"` | Boolean | true | Optional |
| 6 | Change Local Axis of Tapered Section | `"CLATS"` | Boolean | false | Optional |
| 7 | Calculate Equivalent Beam Stresses | `"BMSTRESS"` | Boolean | false | Optional |
| 8 | Classical Formula for Solid Element | `"CLFORM"` | Boolean | false | Optional |
| 9 | Beam Section Property Changes (`"CONSTANT"` / `"CHANGE"`) | `"BSCHG"` | String (enum) | "CHANGE" | Optional |
| 10 | Consider Initial Tension for Cable Element | `"CABINIT"` | Boolean | true | Optional |
| 11 | Tension/Compression Truss Element | `"TCELEM"` | Object | - | Optional |

### Parameters — TCELEM 객체 (인장/압축 트러스)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Number of Increments | `"NUMINC"` | Integer | 1 | Optional |
| 2 | Intermediate Output Request (`"EVERY"` / `"LAST"`) | `"INTOUT"` | String (enum) | "LAST" | Optional |
| 3 | Convergence Criteria | `"CONVERGENCE"` | Object | - | Optional |

**CONVERGENCE 객체** — `DISPL`(변위 U) / `LOAD`(하중 P) / `WORK`(일 W) 각각:

| Key | Value Type | Description |
|-----|------------|-------------|
| `"OPT_USE"` | Boolean | 해당 기준 사용 여부 |
| `"VALUE"` | Number | 허용오차 (OPT_USE = true일 때 필수) |

### Request Body (PUT)

```json
{
  "Assign": {
    "1": {
      "ARCD": true,
      "ANRC": true,
      "CSECF": false,
      "CRBAR": false,
      "TRS": true,
      "CLATS": false,
      "BMSTRESS": false,
      "CLFORM": false,
      "BSCHG": "CHANGE",
      "CABINIT": true,
      "TCELEM": {
        "NUMINC": 10,
        "INTOUT": "LAST",
        "CONVERGENCE": {
          "DISPL": { "OPT_USE": true, "VALUE": 0.001 },
          "LOAD":  { "OPT_USE": false },
          "WORK":  { "OPT_USE": false }
        }
      }
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def update_main_control_m1():
    payload = {
        "Assign": {
            "1": {
                "ARCD": True,
                "ANRC": True,
                "CSECF": False,
                "CRBAR": False,
                "TRS": True,
                "CLATS": False,
                "BMSTRESS": False,
                "CLFORM": False,
                "BSCHG": "CHANGE",       # 보 단면 물성 변경 방식
                "CABINIT": True,         # 케이블 초기 장력 고려
                "TCELEM": {              # 인장/압축 트러스 요소 제어
                    "NUMINC": 10,        # 증분 수
                    "INTOUT": "LAST",    # 중간 출력: 마지막만
                    "CONVERGENCE": {
                        "DISPL": {"OPT_USE": True, "VALUE": 0.001},
                        "LOAD":  {"OPT_USE": False},
                        "WORK":  {"OPT_USE": False}
                    }
                }
            }
        }
    }
    # Hyper-S 엔드포인트는 PUT으로 수정
    resp = requests.put(f"{BASE_URL}/db/ACTL-M1/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Main Control (Hyper-S) updated:", resp.json())

update_main_control_m1()
```

---

## 3. /db/PDEL — P-Delta Analysis Control

P-Delta(2차 효과) 해석 제어 데이터를 정의합니다. 반복 횟수, 수렴 허용오차, 대상 하중 케이스를 설정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/PDEL` | P-Delta 제어 생성 |
| GET | `{base_url}/db/PDEL` | 조회 |
| PUT | `{base_url}/db/PDEL/{id}` | 수정 |
| DELETE | `{base_url}/db/PDEL/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Number of Iterations | `"ITER"` | Number | - | Required |
| 2 | Convergence Tolerance | `"TOL"` | Number | 0 | Optional |
| 3 | Load Cases | `"PDEL_CASES"` | Array [Object] | - | Required |
| (1) | Load Case Name | `"LCNAME"` | String | - | Required |
| (2) | Scale Factor | `"FACTOR"` | Number | - | Required |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "ITER": 5,
      "TOL": 1e-05,
      "PDEL_CASES": [
        { "LCNAME": "A", "FACTOR": 1 },
        { "LCNAME": "B", "FACTOR": 1 }
      ]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_pdelta_control():
    payload = {
        "Assign": {
            "1": {
                "ITER": 5,           # 반복 횟수
                "TOL": 1e-05,        # 수렴 허용오차
                "PDEL_CASES": [      # P-Delta 적용 하중 케이스
                    {"LCNAME": "DL", "FACTOR": 1.0},
                    {"LCNAME": "LL", "FACTOR": 1.0}
                ]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/PDEL", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("P-Delta Control set:", resp.json())

set_pdelta_control()
```

---

## 4. /db/BUCK — Buckling Analysis Control

좌굴(Buckling) 해석 제어 데이터를 정의합니다. 모드 수, 하중계수 범위, Sturm Sequence 체크, 좌굴 조합을 설정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/BUCK` | 좌굴 제어 생성 |
| GET | `{base_url}/db/BUCK` | 조회 |
| PUT | `{base_url}/db/BUCK/{id}` | 수정 |
| DELETE | `{base_url}/db/BUCK/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Number of Modes | `"MODE_NUM"` | Integer | - | Required |
| 2 | Load Factor Range Type (Positive Value Only: true / Search: false) | `"OPT_POSITIVE"` | Boolean | false | Optional |
| 3 | Search From (when `OPT_POSITIVE` is false) | `"LOAD_FACTOR_FROM"` | Number | 0 | Optional |
| 4 | Search To (when `OPT_POSITIVE` is false) | `"LOAD_FACTOR_TO"` | Number | 0 | Optional |
| 5 | Check Sturm Sequence | `"OPT_STURM_SEQ"` | Boolean | false | Optional |
| 6 | Frame Geometric Stiffness Option (Consider Axial Only) | `"OPT_CONSIDER_AXIAL_ONLY"` | Boolean | false | Optional |
| 7 | Load Cases (Buckling Combination) | `"ITEMS"` | Array [Object] | - | Required |
| (1) | Load Case Name | `"LCNAME"` | String | - | Required |
| (2) | Scale Factor | `"FACTOR"` | Number | 0 | Optional |
| (3) | Load Type (Variable: 0 / Constant: 1) | `"LOAD_TYPE"` | Integer | 0 | Optional |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "MODE_NUM": 12,
      "OPT_POSITIVE": true,
      "OPT_CONSIDER_AXIAL_ONLY": true,
      "LOAD_FACTOR_FROM": 0,
      "LOAD_FACTOR_TO": 0,
      "OPT_STURM_SEQ": true,
      "ITEMS": [
        { "LCNAME": "A", "FACTOR": 1, "LOAD_TYPE": 0 },
        { "LCNAME": "B", "FACTOR": 1, "LOAD_TYPE": 1 }
      ]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_buckling_control():
    payload = {
        "Assign": {
            "1": {
                "MODE_NUM": 12,                    # 좌굴 모드 수
                "OPT_POSITIVE": True,              # 양수 하중계수만 사용
                "OPT_CONSIDER_AXIAL_ONLY": True,   # 축력만 고려
                "LOAD_FACTOR_FROM": 0,
                "LOAD_FACTOR_TO": 0,
                "OPT_STURM_SEQ": True,             # Sturm Sequence 체크
                "ITEMS": [
                    {"LCNAME": "DL", "FACTOR": 1, "LOAD_TYPE": 1},  # Constant
                    {"LCNAME": "LL", "FACTOR": 1, "LOAD_TYPE": 0}   # Variable
                ]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/BUCK", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Buckling Control set:", resp.json())

set_buckling_control()
```

---

## 5. /db/EIGV — Eigenvalue Analysis Control

고유치(Eigenvalue) 해석 제어 데이터를 정의합니다. 해석 타입(`TYPE`)에 따라 파라미터가 달라집니다: Subspace Iteration(`EIGEN`), Lanczos(`LANCZOS`), Ritz Vectors(`RITZ`).

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/EIGV` | 고유치 제어 생성 |
| GET | `{base_url}/db/EIGV` | 조회 |
| PUT | `{base_url}/db/EIGV/{id}` | 수정 |
| DELETE | `{base_url}/db/EIGV/{id}` | 삭제 |

### Parameters — 공통

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Type of Analysis (Subspace Iteration: `"EIGEN"` / Lanczos: `"LANCZOS"` / Ritz Vectors: `"RITZ"`) | `"TYPE"` | String | - | Required |

### Parameters — Eigen Vectors (Subspace Iteration, `TYPE = "EIGEN"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Number of Frequencies | `"iFREQ"` | Integer | - | Required |
| 3 | Number of Iterations | `"iITER"` | Integer | - | Required |
| 4 | Subspace Dimension | `"iDIM"` | Integer | 0 | Optional |
| 5 | Convergence Tolerance | `"TOL"` | Number | 0 | Optional |

### Parameters — Eigen Vectors (Lanczos, `TYPE = "LANCZOS"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Number of Frequencies | `"iFREQ"` | Integer | - | Required |
| 3 | Frequency Range of Interest | `"bMINMAX"` | Boolean | false | Optional |
| 4 | Search From [cps] (when `bMINMAX` is true, `FRMIN` < `FRMAX`) | `"FRMIN"` | Number | - | Required |
| 5 | Search To [cps] (when `bMINMAX` is true) | `"FRMAX"` | Number | - | Required |
| 6 | Sturm Sequence Check | `"bSTRUM"` | Boolean | false | Optional |

### Parameters — Ritz Vectors (`TYPE = "RITZ"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Include GL-link Force Vectors | `"bINCNL"` | Boolean | false | Optional |
| 3 | Number of Generations for Each GL-link Force | `"iGNUM"` | Integer | - | Required |
| 4 | Load Cases | `"vRITZ"` | Array [Object] | - | Required |
| (1) | Load Case Type (Ground Acc.: `"GROUND"` / General: `"CASE"`) | `"KIND"` | String | - | Required |
| (2) | Load Case Name (`KIND="CASE"`일 때) | `"CASE"` | String | - | Required |
| (3) | Ground Acc. 방향 (`KIND="GROUND"`일 때, `"ACCX"`/`"ACCY"`/`"ACCZ"`) | `"GROUND"` | String | - | Required |
| (4) | Number of Generations | `"iNOG"` | Integer | Blank | Optional |

> ⚠️ **2026-08-25 확인:** 원문 Specifications 표는 (2)번 항목의 Key를 `"CASE"` 하나로만
> 표기해 General/Ground Acc. 두 분기를 뭉뚱그렸지만, JSON Schema는 `CASE`와 `GROUND`를 별개
> 속성으로 선언하고 있고 원문 예제·아래 로컬 예제 모두 Ground Acc. 항목엔 `"GROUND"` 키를 쓴다
> (표가 자기 예제와도 모순). 예제·스키마 우선 원칙에 따라 표를 분리해 정정(아티클 id
> `35989224565273`).

### Request Body — Subspace Iteration

```json
{
  "Assign": {
    "1": {
      "TYPE": "EIGEN",
      "iFREQ": 100,
      "iITER": 20,
      "iDIM": 1,
      "TOL": 1e-10,
      "bMINMAX": false,
      "FRMIN": 0,
      "FRMAX": 1600,
      "bSTRUM": false
    }
  }
}
```

### Request Body — Lanczos

```json
{
  "Assign": {
    "1": {
      "TYPE": "LANCZOS",
      "iFREQ": 100,
      "bMINMAX": false,
      "FRMIN": 0,
      "FRMAX": 0,
      "bSTRUM": false
    }
  }
}
```

> ⚠️ **2026-08-25 확인:** 이전 예제에는 Subspace Iteration(`TYPE="EIGEN"`) 전용 필드인 `iITER`/
> `iDIM`/`TOL`이 잘못 섞여 있었다(위 Lanczos 파라미터 표에도 없는 필드). 원문 Lanczos 예제에
> 없는 필드라 삭제(아티클 id `35989224565273`).

### Request Body — Ritz Vectors

```json
{
  "Assign": {
    "1": {
      "TYPE": "RITZ",
      "bINCNL": false,
      "iGNUM": 1,
      "vRITZ": [
        { "KIND": "GROUND", "GROUND": "ACCX", "iNOG": 30 },
        { "KIND": "GROUND", "GROUND": "ACCY", "iNOG": 30 },
        { "KIND": "GROUND", "GROUND": "ACCZ", "iNOG": 30 }
      ]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# Lanczos 방식 고유치 해석 제어
def set_eigenvalue_lanczos():
    payload = {
        "Assign": {
            "1": {
                "TYPE": "LANCZOS",   # Lanczos 방식
                "iFREQ": 30,         # 고유진동수 개수
                "bMINMAX": True,     # 관심 주파수 범위 사용
                "FRMIN": 0.1,        # 검색 시작 [cps]
                "FRMAX": 50,         # 검색 끝 [cps]
                "bSTRUM": True       # Sturm Sequence 체크
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/EIGV", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Eigenvalue (Lanczos) set:", resp.json())

# Ritz Vector 방식 (지반 가속도 기반)
def set_eigenvalue_ritz():
    payload = {
        "Assign": {
            "1": {
                "TYPE": "RITZ",
                "bINCNL": False,
                "iGNUM": 1,
                "vRITZ": [
                    {"KIND": "GROUND", "GROUND": "ACCX", "iNOG": 30},
                    {"KIND": "GROUND", "GROUND": "ACCY", "iNOG": 30},
                    {"KIND": "GROUND", "GROUND": "ACCZ", "iNOG": 30}
                ]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/EIGV", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Eigenvalue (Ritz) set:", resp.json())

set_eigenvalue_lanczos()
```

---

## 6. /db/EIGV-M1 — Eigenvalue Analysis Control (Hyper-S)

Hyper-S(MEC) 솔버용 고유치 해석 제어입니다. UI의 Subspace Iteration이 MEC에서 Lanczos로 통합되었습니다. 해석 타입은 `LANCZOS` 또는 `RITZ`이며, 중첩 객체(`FREQ_RANGE`, `GLINK_VECTOR`, `RITZ_LOAD`)를 사용합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| GET | `{base_url}/db/EIGV-M1` | 조회 |
| PUT | `{base_url}/db/EIGV-M1/{id}` | 수정 |
| DELETE | `{base_url}/db/EIGV-M1/{id}` | 삭제 |

### Parameters — 공통

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Eigen Vectors (Lanczos: `"LANCZOS"` / Ritz Vectors: `"RITZ"`) | `"ANAL_TYPE"` | String (enum) | - | Required |

### Parameters — Lanczos (`ANAL_TYPE = "LANCZOS"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Number of Frequencies (1~1000) | `"FREQ_NO"` | Integer | - | Required |
| 3 | Frequency range of interest | `"FREQ_RANGE"` | Object | - | Optional |
| (1) | Use Option | `"OPT_USE"` | Boolean | false | Required |
| (2) | Search From (when `OPT_USE` true) | `"FREQ_MIN"` | Number | - | Required |
| (3) | To (when `OPT_USE` true) | `"FREQ_MAX"` | Number | - | Required |
| 4 | Sturm Sequence Check | `"STURM_SEQ"` | Boolean | false | Optional |

### Parameters — Ritz Vectors (`ANAL_TYPE = "RITZ"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Include GL-link Force Vectors | `"GLINK_VECTOR"` | Object | - | Optional |
| (1) | Use Option | `"OPT_USE"` | Boolean | - | Required |
| (2) | Number of Generations (when `OPT_USE` true) | `"GLINK_NUMBER"` | Integer | - | Required |
| 3 | Ritz Load Cases | `"RITZ_LOAD"` | Array [Object] | - | Required |
| (1) | Type (Ground Acc.: `"GROUND"` / Load: `"LOAD"`) | `"TYPE"` | String (enum) | - | Required |
| (2) | Load Name (`"ACCX"`/`"ACCY"`/`"ACCZ"` 또는 하중케이스명) | `"LOAD_NAME"` | String | - | Required |
| (3) | Number of Generations | `"NUM_OF_GEN"` | Integer | - | Required |

### Request Body — Lanczos

```json
{
  "Assign": {
    "1": {
      "ANAL_TYPE": "LANCZOS",
      "FREQ_NO": 30,
      "FREQ_RANGE": {
        "OPT_USE": true,
        "FREQ_MIN": 0.1,
        "FREQ_MAX": 50
      },
      "STURM_SEQ": true
    }
  }
}
```

### Request Body — Ritz Vectors

```json
{
  "Assign": {
    "1": {
      "ANAL_TYPE": "RITZ",
      "GLINK_VECTOR": {
        "OPT_USE": true,
        "GLINK_NUMBER": 3
      },
      "RITZ_LOAD": [
        { "TYPE": "GROUND", "LOAD_NAME": "ACCX", "NUM_OF_GEN": 5 },
        { "TYPE": "GROUND", "LOAD_NAME": "ACCY", "NUM_OF_GEN": 5 },
        { "TYPE": "GROUND", "LOAD_NAME": "ACCZ", "NUM_OF_GEN": 5 },
        { "TYPE": "LOAD", "LOAD_NAME": "DL", "NUM_OF_GEN": 3 },
        { "TYPE": "LOAD", "LOAD_NAME": "LL", "NUM_OF_GEN": 3 }
      ]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def update_eigenvalue_m1_ritz():
    payload = {
        "Assign": {
            "1": {
                "ANAL_TYPE": "RITZ",
                "GLINK_VECTOR": {
                    "OPT_USE": True,
                    "GLINK_NUMBER": 3
                },
                "RITZ_LOAD": [
                    {"TYPE": "GROUND", "LOAD_NAME": "ACCX", "NUM_OF_GEN": 5},
                    {"TYPE": "GROUND", "LOAD_NAME": "ACCY", "NUM_OF_GEN": 5},
                    {"TYPE": "GROUND", "LOAD_NAME": "ACCZ", "NUM_OF_GEN": 5},
                    {"TYPE": "LOAD", "LOAD_NAME": "DL", "NUM_OF_GEN": 3}
                ]
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/EIGV-M1/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Eigenvalue (Hyper-S, Ritz) updated:", resp.json())

update_eigenvalue_m1_ritz()
```

---

## 7. /db/HHCT — Heat of Hydration Analysis Control

수화열(Heat of Hydration) 해석 제어 데이터를 정의합니다. 적분계수, 초기온도, 응력 평가 위치, 크리프·건조수축 옵션을 설정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/HHCT` | 수화열 제어 생성 |
| GET | `{base_url}/db/HHCT` | 조회 |
| PUT | `{base_url}/db/HHCT/{id}` | 수정 |
| DELETE | `{base_url}/db/HHCT/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Final Stage (Last Stage: true / Other Stage: false) | `"FINAL_STAGE"` | Boolean | false | Optional |
| 2 | Construction Stage for Hydration (when `FINAL_STAGE` false) | `"STAGE_NAME"` | String | - | Required |
| 3 | Integration Factor | `"THETA"` | Number | 0 | Optional |
| 4 | Initial Temperature | `"INIT_TEMP"` | Number | 0 | Optional |
| 5 | Element Stress Evaluation (`"CENTER"` / `"GAUSS"` / `"NODAL"`) | `"EVAL"` | String | "CENTER" | Optional |
| 6 | Creep & Shrinkage Option | `"OPT_IS_CREEP_SHRINKAGE"` | Boolean | false | Optional |
| 7 | Creep & Shrinkage 설정 객체 | `"ITEM"` | Object | - | Optional |
| (1) | Type (Creep: `"CREEP"` / Shrinkage: `"SHRINK"` / Both: `"BOTH"`) | `"TYPE"` | String | "CREEP" | Optional |
| (2) | Creep Calculation Method (General: 0 / Effective Modulus: 1) | `"CREEP_CALC_METHOD"` | Integer | 0 | Optional |
| (3) | General Data (when method 0) | `"M_GENERAL"` | Object | - | Optional |
| i | Number of Iterations | `"ITER"` | Integer | 0 | Optional |
| ii | Tolerance | `"TOL"` | Number | 0 | Optional |
| (3) | Effective Modulus Data (when method 1) | `"M_EFF_MOD"` | Object | - | Required |
| i | Phi1 | `"PHI1"` | Number | - | Required |
| ii | Day1 | `"DAY1"` | Integer | - | Required |
| iii | Phi2 | `"PHI2"` | Number | - | Required |
| iv | Day2 | `"DAY2"` | Integer | - | Required |
| 8 | Use Equivalent Age by Time & Temperature | `"OPT_USE_EQUI_AGE"` | Boolean | false | Optional |
| 9 | Include Self-weight Load | `"OPT_INCL_SELF_WEIGHT"` | Boolean | false | Optional |
| 10 | Self-weight Factor | `"SELF_WEIGHT_FACTOR"` | Number | 0 | Optional |

### Request Body — General

```json
{
  "Assign": {
    "1": {
      "FINAL_STAGE": true,
      "STAGE_NAME": "",
      "THETA": 1,
      "INIT_TEMP": 20,
      "EVAL": "GAUSS",
      "OPT_USE_EQUI_AGE": true,
      "OPT_INCL_SELF_WEIGHT": false,
      "SELF_WEIGHT_FACTOR": -1,
      "OPT_IS_CREEP_SHRINKAGE": true,
      "ITEM": {
        "TYPE": "BOTH",
        "CREEP_CALC_METHOD": 0,
        "M_GENERAL": { "ITER": 20, "TOL": 0.001 }
      }
    }
  }
}
```

### Request Body — Effective Modulus

```json
{
  "Assign": {
    "1": {
      "FINAL_STAGE": true,
      "STAGE_NAME": "",
      "THETA": 1,
      "INIT_TEMP": 20,
      "EVAL": "GAUSS",
      "OPT_USE_EQUI_AGE": true,
      "OPT_INCL_SELF_WEIGHT": false,
      "SELF_WEIGHT_FACTOR": -1,
      "OPT_IS_CREEP_SHRINKAGE": true,
      "ITEM": {
        "TYPE": "BOTH",
        "CREEP_CALC_METHOD": 1,
        "M_EFF_MOD": { "PHI1": 0.73, "DAY1": 3, "PHI2": 1, "DAY2": 5 }
      }
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_hydration_control():
    payload = {
        "Assign": {
            "1": {
                "FINAL_STAGE": True,          # 마지막 단계
                "STAGE_NAME": "",
                "THETA": 1,                   # 적분계수
                "INIT_TEMP": 20,              # 초기온도 (°C)
                "EVAL": "GAUSS",              # 응력 평가: Gauss point
                "OPT_USE_EQUI_AGE": True,     # 등가재령 사용
                "OPT_INCL_SELF_WEIGHT": False,
                "SELF_WEIGHT_FACTOR": -1,
                "OPT_IS_CREEP_SHRINKAGE": True,
                "ITEM": {
                    "TYPE": "BOTH",            # 크리프 + 건조수축
                    "CREEP_CALC_METHOD": 0,    # General 방식
                    "M_GENERAL": {"ITER": 20, "TOL": 0.001}
                }
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/HHCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Heat of Hydration Control set:", resp.json())

set_hydration_control()
```

---

## 8. /db/HHCT-M1 — Heat of Hydration Analysis Control (Hyper-S)

Hyper-S(MEC) 솔버용 수화열 해석 제어입니다. 반복 횟수(`ITER`)와 수렴 기준(`CONVERGENCE`) 객체가 추가되었습니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| GET | `{base_url}/db/HHCT-M1` | 조회 |
| PUT | `{base_url}/db/HHCT-M1/{id}` | 수정 |
| DELETE | `{base_url}/db/HHCT-M1/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Final Stage (Last: true / Other: false) | `"FINAL_STAGE"` | Boolean | true | Optional |
| 2 | Stage Name (when `FINAL_STAGE` false) | `"STAGE_NAME"` | String | - | Required |
| 3 | Initial Temperature | `"INIT_TEMP"` | Number | 20 | Optional |
| 4 | Element Stress Evaluation (`"CENTER"`/`"GAUSS"`/`"NODAL"`) | `"EVAL"` | String (enum) | "GAUSS" | Optional |
| 5 | Creep & Shrinkage | `"OPT_IS_CREEP_SHRINKAGE"` | Boolean | true | Optional |
| 6 | Creep & Shrinkage Settings (when option true) | `"ITEM"` | Object | - | Required |
| (1) | Type (`"CREEP"`/`"SHRINKAGE"`/`"BOTH"`) | `"TYPE"` | String (enum) | "BOTH" | Optional |
| (2) | Creep Calculation Method (General: 0 / Effective Modulus: 1) | `"CREEP_CALC_METHOD"` | Integer (enum) | 0 | Optional |
| (3) | Effective Modulus Params (when method 1) | `"M_EFF_MOD"` | Object | - | Required |
| a | phi 1 | `"PHI1"` | Number | - | Required |
| b | day 1 | `"DAY1"` | Integer | - | Required |
| c | phi 2 | `"PHI2"` | Number | - | Required |
| d | day 2 | `"DAY2"` | Integer | - | Required |
| 7 | Use Equivalent Age by Time & Temperature | `"OPT_USE_EQUI_AGE"` | Boolean | true | Optional |
| 8 | Include Selfweight Load | `"OPT_INCL_SELF_WEIGHT"` | Boolean | false | Optional |
| 9 | Self Weight Factor (when option true) | `"SELF_WEIGHT_FACTOR"` | Number | - | Required |
| 10 | Max. No. of Iterations per Increment | `"ITER"` | Integer | 50 | Optional |
| 11 | Convergence Criteria (DISP/LOAD/WORK 중 최소 1개 필수) | `"CONVERGENCE"` | Object | - | Optional |
| (1) | Displacement(U) | `"DISP"` | Object | - | Optional |
| (2) | Load(P) | `"LOAD"` | Object | - | Optional |
| (3) | Work(W) | `"WORK"` | Object | - | Optional |
| a | Use Option | `"OPT_CHECK"` | Boolean | - | Required |
| b | Tolerance (when `OPT_CHECK` true) | `"VALUE"` | Number | - | Required |

### Request Body (PUT)

```json
{
  "Assign": {
    "1": {
      "FINAL_STAGE": false,
      "STAGE_NAME": "Stage 1",
      "INIT_TEMP": 20,
      "EVAL": "GAUSS",
      "OPT_IS_CREEP_SHRINKAGE": true,
      "ITEM": {
        "TYPE": "BOTH",
        "CREEP_CALC_METHOD": 1,
        "M_EFF_MOD": { "PHI1": 1, "DAY1": 3, "PHI2": 2, "DAY2": 28 }
      },
      "OPT_USE_EQUI_AGE": true,
      "OPT_INCL_SELF_WEIGHT": true,
      "SELF_WEIGHT_FACTOR": 1,
      "ITER": 50,
      "CONVERGENCE": {
        "DISP": { "OPT_CHECK": true, "VALUE": 0.001 },
        "LOAD": { "OPT_CHECK": true, "VALUE": 0.001 },
        "WORK": { "OPT_CHECK": true, "VALUE": 0.001 }
      }
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def update_hydration_control_m1():
    payload = {
        "Assign": {
            "1": {
                "FINAL_STAGE": False,
                "STAGE_NAME": "Stage 1",
                "INIT_TEMP": 20,
                "EVAL": "GAUSS",
                "OPT_IS_CREEP_SHRINKAGE": True,
                "ITEM": {
                    "TYPE": "BOTH",
                    "CREEP_CALC_METHOD": 1,             # Effective Modulus
                    "M_EFF_MOD": {"PHI1": 1, "DAY1": 3, "PHI2": 2, "DAY2": 28}
                },
                "OPT_USE_EQUI_AGE": True,
                "OPT_INCL_SELF_WEIGHT": True,
                "SELF_WEIGHT_FACTOR": 1,
                "ITER": 50,                             # 증분당 최대 반복 횟수
                "CONVERGENCE": {                        # 수렴 기준 (최소 1개)
                    "DISP": {"OPT_CHECK": True, "VALUE": 0.001},
                    "LOAD": {"OPT_CHECK": True, "VALUE": 0.001},
                    "WORK": {"OPT_CHECK": True, "VALUE": 0.001}
                }
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/HHCT-M1/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Heat of Hydration (Hyper-S) updated:", resp.json())

update_hydration_control_m1()
```

---

## 9. /db/MVCT — Moving Load Analysis Control

이동하중(Moving Load) 해석 제어 데이터를 정의합니다. 해석 방법, 영향선 생성점, 판/프레임/링크별 결과 옵션, 계산 필터(반력/변위/부재력/링크)를 설정합니다.

> **¹⁾** `METHOD`(Analysis Method)는 MIDAS Civil NX 전용 항목입니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/MVCT` | 이동하중 제어 생성 |
| GET | `{base_url}/db/MVCT` | 조회 |
| PUT | `{base_url}/db/MVCT/{id}` | 수정 |
| DELETE | `{base_url}/db/MVCT/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Analysis Method ¹⁾ (Exact: `"EXACT"` / Pivot: `"PIVOT"` / Quick: `"QUICK"`) | `"METHOD"` | String | "EXACT" | Optional |
| 2 | Load Point Selection (Influence Line Dependent: `"INF"` / All Points: `"ALL"`) | `"POINT"` | String | - | Required |
| 3 | Influence Generating Points (Number/Line Element: 0 / Distance: 1) | `"iIGP"` | Integer | 0 | Optional |
| 4 | Number/Line Element (when `iIGP`=0) | `"iIGPN"` | Integer | - | Required |
| 5 | Distance between Points (when `iIGP`=1) | `"DIST"` | Number | - | Required |
| 6 | Plate Options (Center: `"CENTER"` / Center+Nodal: `"NODAL"`) | `"PLATE"` | String | - | Required |
| 7 | Plate – Stress | `"bSTRCALC"` | Boolean | false | Optional |
| 8 | Plate – Concurrent Force | `"bCONCURRENT"` | Boolean | false | Optional |
| 9 | Frame Options (Normal: `"NORMAL"` / Normal+Concurrent: `"AXIAL"`) | `"FRAME"` | String | - | Required |
| 10 | Frame – Combined Stress | `"bCSTRCALC"` | Boolean | false | Optional |
| 11 | Link – Concurrent Force of Elastic/General Links | `"bCONCLINK"` | Boolean | false | Optional |
| 12 | Filter – Reactions | `"bREAC"` | Boolean | false | Optional |
| 13 | Reactions Option (All: false / Structure Group: true) | `"bRG"` | Boolean | false | Optional |
| 14 | Reactions Group Name (when `bRG` true) | `"RGN"` | String | - | Required |
| 15 | Filter – Displacements | `"bDISP"` | Boolean | false | Optional |
| 16 | Displacements Option (All: false / Structure Group: true) | `"bDG"` | Boolean | false | Optional |
| 17 | Displacements Group Name (when `bDG` true) | `"DGN"` | String | - | Required |
| 18 | Filter – Forces/Moments | `"bFM"` | Boolean | false | Optional |
| 19 | Forces/Moments Option (All: false / Structure Group: true) | `"bFG"` | Boolean | false | Optional |
| 20 | Forces/Moments Group Name (when `bFG` true) | `"FGN"` | String | - | Required |
| 21 | Filter – Elastic/General Link | `"bL"` | Boolean | false | Optional |
| 22 | Link Option (All: false / Boundary Group: true) | `"bLG"` | Boolean | false | Optional |
| 23 | Link Group Name (when `bLG` true) | `"LGN"` | String | - | Required |

> **Russia 코드** 적용 시 추가 파라미터: `MATTYPE`, `BRIDGETYPE`, `AKMATTYPE`, `AKBRIDGETYPE`(Integer), `MINFACTS2`(Number, 최소계수), `MAXV`(Integer, 최대 연속 차량), `INCV`(Integer, 차량 증분), `MAXSPACE`(Number, 열차 최대 간격).

### Request Body — General

```json
{
  "Assign": {
    "1": {
      "METHOD": "EXACT",
      "POINT": "INF",
      "iIGP": 0,
      "iIGPN": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "bCONCURRENT": true,
      "bCONCLINK": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true,
      "bRG": false,
      "RGN": "",
      "bDISP": true,
      "bDG": false,
      "DGN": "",
      "bFM": true,
      "bFG": false,
      "FGN": "",
      "bL": true,
      "bLG": false,
      "LGN": ""
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_moving_load_control():
    payload = {
        "Assign": {
            "1": {
                "METHOD": "EXACT",       # 정밀 해석법
                "POINT": "INF",          # 영향선 종속점
                "iIGP": 0,               # Number/Line Element 방식
                "iIGPN": 3,              # 부재당 분할 수
                "PLATE": "NODAL",        # 판: 중심+절점
                "bSTRCALC": True,        # 판 응력 계산
                "bCONCURRENT": True,     # 판 동시력
                "bCONCLINK": True,       # 링크 동시력
                "FRAME": "AXIAL",        # 프레임: Normal+동시력
                "bCSTRCALC": True,       # 조합 응력
                "bREAC": True,  "bRG": False, "RGN": "",   # 반력 (전체)
                "bDISP": True,  "bDG": False, "DGN": "",   # 변위 (전체)
                "bFM": True,    "bFG": False, "FGN": "",   # 부재력 (전체)
                "bL": True,     "bLG": False, "LGN": ""    # 링크 (전체)
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/MVCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Moving Load Control set:", resp.json())

set_moving_load_control()
```

---

## 10. /db/MVCTch — Moving Load Analysis Control – China

중국 코드(JTG 등) 전용 이동하중 해석 제어입니다. 충격계수(`bIF`), 코드 타입, 고유진동수 방법, 주파수 데이터(`FREQ`), 교량 데이터(`BRIDGE1`) 등을 포함합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/MVCTch` | 생성 |
| GET | `{base_url}/db/MVCTch` | 조회 |
| PUT | `{base_url}/db/MVCTch/{id}` | 수정 |
| DELETE | `{base_url}/db/MVCTch/{id}` | 삭제 |

### Parameters — 기본 (MVCT와 공통 결과 옵션)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Load Point (`"INF"` / `"ALL"`) | `"POINT"` | String | - | Required |
| 2 | Influence Generating Points (0/1) | `"iIGP"` | Integer | 0 | Optional |
| 3 | Number/Line Element (when `iIGP`=0) | `"UNUMT"` | Integer | - | Required |
| 4 | Distance between Points (when `iIGP`=1) | `"DIST"` | Number | - | Required |
| 5 | Plate Options (`"CENTER"` / `"NODAL"`) | `"PLATE"` | String | - | Required |
| 6 | Plate – Stress | `"bSTRCALC"` | Boolean | false | Optional |
| 7 | Frame Options (`"NORMAL"` / `"AXIAL"`) | `"FRAME"` | String | - | Required |
| 8 | Frame – Combined Stress | `"bCSTRCALC"` | Boolean | false | Optional |
| 9 | Filter – Reactions | `"bREAC"` | Boolean | false | Optional |
| 10 | Reactions Option (All/Group) | `"bRG"` | Boolean | false | Optional |
| 11 | Reactions Group Name | `"RGN"` | String | - | Required |
| 12 | Filter – Displacements | `"bDISP"` | Boolean | false | Optional |
| 13 | Displacements Option (All/Group) | `"bDG"` | Boolean | false | Optional |
| 14 | Displacements Group Name | `"DGN"` | String | - | Required |
| 15 | Filter – Forces/Moments | `"bFM"` | Boolean | false | Optional |
| 16 | Forces/Moments Option (All/Group) | `"bFG"` | Boolean | false | Optional |
| 17 | Forces/Moments Group Name | `"FGN"` | String | - | Required |
| 18 | Filter – Elastic/General Links | `"bL"` | Boolean | false | Optional |
| 19 | Links Option (All/Group) | `"bLG"` | Boolean | false | Optional |
| 20 | Links Group Name | `"LGN"` | String | - | Required |

### Parameters — 충격계수 (Impact Factor)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 21 | Impact Factor 사용 | `"bIF"` | Boolean | false | Optional |
| 22 | Code Type (`0`=JTG D60-2015/JTG04 / `1`=Other Codes / `2`=TB 10002-2017 / `3`=Q/CR 9300-2018) | `"iCODETYPE"` | Integer | - | Required |
| 23 | Natural Frequency Method (`iCODETYPE`=0일 때 필수. `0`=User Input / `1`=Simple Beam / `2`=Continuous Beam / `3`=Arch Bridge / `4`=Cable Stayed Bridge / `5`=Suspension Bridge) | `"iNFM"` | Integer | - | Required (조건부) |
| 24 | Span Length (`0`=Span Length by Lane Input / `1`=Loaded Length by Influence Line) | `"iSLCM"` | Integer | - | Required |
| 25 | Vehicle Load Class 사용 | `"bBC"` | Boolean | false | Optional |
| 26 | Vehicle Load Class Type (`0`=Class I / `1`=Class II) | `"iBC"` | Integer | 0 | Required |
| 27 | Frequency Data (`iCODETYPE`=0일 때 필수) | `"FREQ"` | Object | - | Required (조건부) |
| 28 | Bridge Data — Other Codes (`iCODETYPE`=1일 때 필수) | `"BRIDGE1"` | Object | - | Required (조건부) |
| 29 | Bridge Data — TB 10002-2017 / Q·CR 9300-2018 (`iCODETYPE`=2 또는 3일 때 필수) | `"BRIDGE2"` | Object | - | Required (조건부) |

> ⚠️ **2026-08-25 확인:** `iCODETYPE`/`iNFM`/`iSLCM`/`iBC` 4개 필드 모두 원문 Specifications
> 표에 enum 값 목록이 있는데도 이전 문서엔 누락돼 있었고, Required 여부도 실제로는 (조건부)
> Required인데 Optional로 잘못 기재돼 있었다. `BRIDGE2` 객체(TB 10002-2017/Q·CR 9300-2018
> 코드 전용)는 통째로 누락돼 있어 아래에 별도 표로 신규 추가했다(아티클 id `35989644995609`).

**FREQ 객체 주요 키** (교량 형식별 진동수 산정 파라미터):

| Key | 설명 | Key | 설명 |
|-----|------|-----|------|
| `"USER_F"` | f [Hz] | `"SBEM_L"`/`"SBEM_E"`/`"SBEM_IC"`/`"SBEM_MC"` | 단순보 L/E/Ic/mc |
| `"CBEM_A"`/`"CBEM_B"`/`"CBEM_L"`/`"CBEM_E"`/`"CBEM_IC"`/`"CBEM_MC"` | 연속보 a/b/L/E/Ic/mc | `"iARCH_TYPE"` | 아치교 형식 |
| `"ARCH_N"`/`"ARCH_F"`/`"ARCH_L"`/`"ARCH_E"`/`"ARCH_IC"`/`"ARCH_MC"` | 아치교 n/f/L/E/Ic/mc | `"CABL_A"`/`"CABL_L"` | 사장교 a/L |
| `"SUSP_L"`/`"SUSP_E"`/`"SUSP_I"`/`"SUSP_HG"`/`"SUSP_M"` | 현수교 L/E/I/Hg/m | | |

**BRIDGE1 객체 — `"BTYPE"`(Bridge Type: `"RC"` / `"STEEL"` / `"MBRG"`(Old Urban Bridge) /
`"TRAIN"`(Train·Subway))별 필드:**

| Key | 설명 | Value Type |
| --- | --- | --- |
| `"RC_C1L1"`/`"RC_C1F1"`/`"RC_C1L2"`/`"RC_C1F2"` | RC — Case 1 L1/F1/L2/F2 | Number |
| `"RC_bCASE2"` | RC — Case 2 사용 여부 | Boolean (기본 false) |
| `"RC_C2L1"`/`"RC_C2F1"`/`"RC_C2L2"`/`"RC_C2F2"` | RC — Case 2 L1/F1/L2/F2 (`RC_bCASE2`=true 시) | Number |
| `"RC_GROUP"` | RC — 구조 그룹명 | String |
| `"STL_C1V1"`/`"STL_C1V2"` | Steel — Case 1 V1/V2 | Number |
| `"STL_bCASE2"` | Steel — Case 2 사용 여부 | Boolean (기본 false) |
| `"STL_C2V1"`/`"STL_C2V2"` | Steel — Case 2 V1/V2 (`STL_bCASE2`=true 시) | Number |
| `"STL_GROUP"` | Steel — 구조 그룹명 | String |
| `"MBRG_RL1"`/`"MBRG_RF1"`/`"MBRG_RL2"`/`"MBRG_RF2"`/`"MBRG_RF3"`/`"MBRG_RF4"` | Old Urban Bridge — 차로하중 충격계수 L1/F1/L2/F2/F3/F4 | Number |
| `"MBRG_CF1"`/`"MBRG_CF2"`/`"MBRG_CF3"` | Old Urban Bridge — 차량하중 충격계수 F1/F2/F3 | Number |
| `"TRAIN_SUB_TYPE"` | Train — Sub-Type(`"SIMPLE"`/`"COMPOSITE"`/`"RCCONC"`/`"RCARCH"`) | String |
| `"TRAIN_NUMERATOR"`/`"TRAIN_DENOMINATOR"` | Train — Value 1 / Value 2 | Number |
| `"TRAIN_H"` | Train — Surcharge Thickness (`TRAIN_SUB_TYPE="RCCONC"` 전용) | Number |
| `"TRAIN_bCLSL"` | Train — Apply Loaded Span Length (`RCCONC` 전용, `0`=미고려/`1`=고려) | Integer |
| `"TRAIN_LAMBDA"`/`"TRAIN_F"` | Train — Lambda / f (`RCARCH` 전용) | Number |
| `"TRAIN_bALSL"` | Train — Apply Loaded Span Length (`RCARCH` 전용, `0`=미고려/`1`=고려) | Integer |
| `"TRAIN_GROUP"` | Train — 구조 그룹명 | String |

**BRIDGE2 객체** (`iCODETYPE`=2 TB 10002-2017 / 3 Q·CR 9300-2018 전용) — `"BTYPE"`(Bridge Type:
`"RAILWAY"`(Passenger-Freight Mixed Line·Heavy Haul Railway Bridge) / `"RAILBRG"`(High Speed·
Intercity Railway Bridge) / `"RAILCUL"`(High Speed·Intercity Railway Culvert))별 필드:

| Key | 설명 | Value Type |
| --- | --- | --- |
| `"METHOD"` | RAILWAY — Sub-Type(`"SIMPLE"`/`"COMPOSITE"`/`"RCCONC"`/`"RCARCH"`) | String |
| `"SIMPLE_U"`/`"SIMPLE_L"` | RAILWAY(`METHOD="SIMPLE"`) — Value 1/2 | Number |
| `"COMPO_U"`/`"COMPO_L"` | RAILWAY(`METHOD="COMPOSITE"`) — Value 1/2 | Number |
| `"CONC_U"`/`"CONC_L"`/`"CONC_H"` | RAILWAY(`METHOD="RCCONC"`) — Value 1/2, Surcharge Thickness | Number |
| `"ARCH_U"`/`"ARCH_L"`/`"ARCH_LAMBDA"`/`"ARCH_F"` | RAILWAY(`METHOD="RCARCH"`) — Value 1/2, Lambda, f | Number |
| `"bCHECK"` | RAILWAY(`RCCONC`/`RCARCH`) — Apply Loaded Span Length 여부 | Boolean (기본 false) |
| `"GROUP"` | RAILWAY(`RCCONC`/`RCARCH`) — 구조 그룹명 | String |
| `"MU1"`/`"MU2"`/`"MU3"` | RAILBRG·RAILCUL 공통 — mu 산정용 Value 1/2/3 | Number |
| `"bLFAI"` | RAILBRG·RAILCUL 공통 — Apply Loaded Span Length 여부 | Boolean (기본 false) |
| `"LFAI"` | RAILBRG·RAILCUL 공통 — Lfai (`bLFAI`=false 시) | Number |
| `"bCHECK"` | RAILBRG 전용 — Apply Loaded Span Length (`bLFAI`=true 시) | Boolean (기본 false) |
| `"bLENGTH"` | RAILCUL 전용 — Apply Loaded Span Length (`bLFAI`=true 시) | Boolean (기본 false) |
| `"MUR1"`/`"MUR2"`/`"MUR3"` | RAILCUL 전용 — mu Reduction 산정용 Value 1/2/3 | Number |
| `"HC"` | RAILCUL 전용 — Surcharge Thickness | Number |
| `"GROUP"` | RAILBRG·RAILCUL 공통 — 구조 그룹명 | String |

> `BRIDGE2.bCHECK`/`GROUP` 키는 RAILWAY 분기와 RAILBRG 분기가 이름을 공유한다(원문 표에서도
> 동일 Key로 재사용) — `BTYPE`으로 분기를 구분해서 해석할 것.

### Request Body (요약 예시)

```json
{
  "Assign": {
    "1": {
      "POINT": "INF",
      "iIGP": 0,
      "UNUMT": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true, "bRG": false, "RGN": "",
      "bDISP": true, "bDG": false, "DGN": "",
      "bFM": true, "bFG": false, "FGN": "",
      "bL": true, "bLG": false, "LGN": "",
      "bIF": true,
      "iCODETYPE": 0,
      "iNFM": 0,
      "bBC": false,
      "FREQ": {
        "USER_F": 0,
        "SBEM_L": 30, "SBEM_E": 3.0e10, "SBEM_IC": 0.5, "SBEM_MC": 2500
      }
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_moving_load_china():
    payload = {
        "Assign": {
            "1": {
                "POINT": "INF", "iIGP": 0, "UNUMT": 3,
                "PLATE": "NODAL", "bSTRCALC": True,
                "FRAME": "AXIAL", "bCSTRCALC": True,
                "bREAC": True, "bRG": False, "RGN": "",
                "bDISP": True, "bDG": False, "DGN": "",
                "bFM": True,  "bFG": False, "FGN": "",
                "bL": True,   "bLG": False, "LGN": "",
                "bIF": True,           # 충격계수 사용
                "iCODETYPE": 0,        # 코드 타입
                "iNFM": 0,             # 고유진동수 산정법
                "bBC": False,          # 차량하중등급 미사용
                "FREQ": {              # 단순보 진동수 데이터
                    "USER_F": 0,
                    "SBEM_L": 30, "SBEM_E": 3.0e10,
                    "SBEM_IC": 0.5, "SBEM_MC": 2500
                }
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/MVCTch", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Moving Load Control (China) set:", resp.json())

set_moving_load_china()
```

---

## 11. /db/MVCTid — Moving Load Analysis Control – India

인도 코드(IRC/IRS) 전용 이동하중 해석 제어입니다. 충격/CDA 계산용 교량 타입, 철도교 정보(트랙, 침목 폭, 성토 깊이) 등을 포함합니다. 계산 필터 그룹 키는 `*GP` 접미사를 사용합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/MVCTid` | 생성 |
| GET | `{base_url}/db/MVCTid` | 조회 |
| PUT | `{base_url}/db/MVCTid/{id}` | 수정 |
| DELETE | `{base_url}/db/MVCTid/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Influence Generating Points (0/1) | `"iIGP"` | Integer | 0 | Optional |
| 2 | Number/Line Element (when `iIGP`=0) | `"UNUMT"` | Integer | - | Required |
| 3 | Distance between Points (when `iIGP`=1) | `"DIST"` | Number | - | Required |
| 4 | Plate Options (`"CENTER"` / `"NODAL"`) | `"PLATE"` | String | - | Required |
| 5 | Plate – Stress | `"bSTRCALC"` | Boolean | false | Optional |
| 6 | Frame Options (`"NORMAL"` / `"AXIAL"`) | `"FRAME"` | String | - | Required |
| 7 | Frame – Combined Stress | `"bCSTRCALC"` | Boolean | false | Optional |
| 8 | Filter – Reactions | `"bREAC"` | Boolean | false | Optional |
| 9 | Reactions Option (All/Group) | `"bRGP"` | Boolean | false | Optional |
| 10 | Reactions Group Name | `"RGP"` | String | - | Required |
| 11 | Filter – Displacements | `"bDISP"` | Boolean | false | Optional |
| 12 | Displacements Option (All/Group) | `"bDGP"` | Boolean | false | Optional |
| 13 | Displacements Group Name | `"DGP"` | String | - | Required |
| 14 | Filter – Forces/Moments | `"bFM"` | Boolean | false | Optional |
| 15 | Forces/Moments Option (All/Group) | `"bFGP"` | Boolean | false | Optional |
| 16 | Forces/Moments Group Name | `"FGP"` | String | - | Required |
| 17 | Filter – Elastic/General Links | `"bL"` | Boolean | false | Optional |
| 18 | Links Option (All/Group) | `"bLG"` | Boolean | false | Optional |
| 19 | Links Group Name | `"LGP"` | String | - | Required |
| 20 | Bridge Type for Impact/CDA (Steel: 0 / RC: 1) | `"BRIDGE"` | Integer | 0 | Optional |
| 21 | Track (Single: 0 / Double: 1 / Multiple: 2) | `"TRACKS"` | Integer | 0 | Optional |
| 22 | Sleeper Width Type (Type1: 0 / Type2: 1 / User: 2) | `"WIDTHTYPE"` | Integer | 0 | Optional |
| 23 | Sleeper Width for User | `"WIDTH"` | Number | 0 | Optional |
| 24 | Depth of Fill | `"DEPTH"` | Number | 0 | Optional |
| 25 | Maximum Successive Vehicles | `"VHMAX"` | Integer | - | Required |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "iIGP": 0,
      "UNUMT": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true, "bRGP": false, "RGP": "",
      "bDISP": true, "bDGP": false, "DGP": "",
      "bFM": true, "bFGP": false, "FGP": "",
      "bL": true, "bLG": false, "LGP": "",
      "BRIDGE": 0,
      "TRACKS": 0,
      "WIDTHTYPE": 0,
      "WIDTH": 0,
      "DEPTH": 10,
      "VHMAX": 10
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_moving_load_india():
    payload = {
        "Assign": {
            "1": {
                "iIGP": 0, "UNUMT": 3,
                "PLATE": "NODAL", "bSTRCALC": True,
                "FRAME": "AXIAL", "bCSTRCALC": True,
                "bREAC": True, "bRGP": False, "RGP": "",
                "bDISP": True, "bDGP": False, "DGP": "",
                "bFM": True,  "bFGP": False, "FGP": "",
                "bL": True,   "bLG": False, "LGP": "",
                "BRIDGE": 0,        # Steel bridge
                "TRACKS": 0,        # Single track
                "WIDTHTYPE": 0,     # Type 1
                "WIDTH": 0,
                "DEPTH": 10,        # 성토 깊이
                "VHMAX": 10         # 최대 연속 차량 수
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/MVCTid", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Moving Load Control (India) set:", resp.json())

set_moving_load_india()
```

---

## 12. /db/MVCTbs — Moving Load Analysis Control – BS

영국 코드(BS 5400 / BD 37/01 / CS 454) 전용 이동하중 해석 제어입니다. 표준 차로(Notional Lanes) 수를 추가로 지정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/MVCTbs` | 생성 |
| GET | `{base_url}/db/MVCTbs` | 조회 |
| PUT | `{base_url}/db/MVCTbs/{id}` | 수정 |
| DELETE | `{base_url}/db/MVCTbs/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Influence Generating Points (0/1) | `"iIGP"` | Integer | 0 | Optional |
| 2 | Number/Line Element (when `iIGP`=0) | `"UNUMT"` | Integer | - | Required |
| 3 | Distance between Points (when `iIGP`=1) | `"DIST"` | Number | - | Required |
| 4 | Plate Options (`"CENTER"` / `"NODAL"`) | `"PLATE"` | String | - | Required |
| 5 | Plate – Stress | `"bSTRCALC"` | Boolean | false | Optional |
| 6 | Plate – Concurrent Force | `"bCONCURRENT"` | Boolean | false | Optional |
| 7 | Frame Options (`"NORMAL"` / `"AXIAL"`) | `"FRAME"` | String | - | Required |
| 8 | Frame – Combined Stress | `"bCSTRCALC"` | Boolean | false | Optional |
| 9 | Filter – Reactions | `"bREAC"` | Boolean | false | Optional |
| 10 | Reactions Option (All/Group) | `"bRGP"` | Boolean | false | Optional |
| 11 | Reactions Group Name | `"RGP"` | String | - | Required |
| 12 | Filter – Displacements | `"bDISP"` | Boolean | false | Optional |
| 13 | Displacements Option (All/Group) | `"bDGP"` | Boolean | false | Optional |
| 14 | Displacements Group Name | `"DGP"` | String | - | Required |
| 15 | Filter – Forces/Moments | `"bFM"` | Boolean | false | Optional |
| 16 | Forces/Moments Option (All/Group) | `"bFGP"` | Boolean | false | Optional |
| 17 | Forces/Moments Group Name | `"FGP"` | String | - | Required |
| 18 | Filter – Elastic/General Links | `"bL"` | Boolean | false | Optional |
| 19 | Links Option (All/Group) | `"bLG"` | Boolean | false | Optional |
| 20 | Links Group Name | `"LGP"` | String | - | Required |
| 21 | N for HA Lane Factor (BD/37/01) or ALL Model 2 (CS 454) — N < 6: 0 / N ≥ 6: 1 | `"NUMLANE"` | Integer | 0 | Optional |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "iIGP": 0,
      "UNUMT": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "bCONCURRENT": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true, "bRGP": false, "RGP": "",
      "bDISP": true, "bDGP": false, "DGP": "",
      "bFM": true, "bFGP": false, "FGP": "",
      "bL": true, "bLG": false, "LGP": "",
      "NUMLANE": 0
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_moving_load_bs():
    payload = {
        "Assign": {
            "1": {
                "iIGP": 0, "UNUMT": 3,
                "PLATE": "NODAL", "bSTRCALC": True, "bCONCURRENT": True,
                "FRAME": "AXIAL", "bCSTRCALC": True,
                "bREAC": True, "bRGP": False, "RGP": "",
                "bDISP": True, "bDGP": False, "DGP": "",
                "bFM": True,  "bFGP": False, "FGP": "",
                "bL": True,   "bLG": False, "LGP": "",
                "NUMLANE": 0     # N < 6
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/MVCTbs", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Moving Load Control (BS) set:", resp.json())

set_moving_load_bs()
```

---

## 13. /db/MVCTtr — Moving Load Analysis Control – Transverse

횡방향(Transverse) 이동하중 해석 제어입니다. 단위 하중 수, 해석 결과 타입, 결과 옵션(조합응력/반력/변위/부재력)을 설정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/MVCTtr` | 생성 |
| GET | `{base_url}/db/MVCTtr` | 조회 |
| PUT | `{base_url}/db/MVCTtr/{id}` | 수정 |
| DELETE | `{base_url}/db/MVCTtr/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Load Point Selection (Influence Line Dependent: 1 / All Point: 2) | `"LOAD_POINT_SEL"` | Integer | - | Required |
| 2 | Influence Generation Method (Number/Line: 0 / Distance: 1) | `"INFL_GEN_POINT"` | Integer | 0 | Optional |
| 3 | Number/Line Element (when method 0) | `"NUM_UNIT_LOAD"` | Integer | - | Required |
| 4 | Distance between Points (when method 1) | `"DISTANCE"` | Number | - | Required |
| 5 | Analysis Results Type (Normal: 1 / Normal+Concurrent Force/Stress: 2) | `"ANALYSIS_RESULT"` | Integer | - | Required |
| 6 | Combined Stress | `"OPT_COMBINED_STR"` | Boolean | false | Optional |
| 7 | Reactions | `"OPT_REACTIONS"` | Boolean | false | Optional |
| 8 | Displacement | `"OPT_DISPLACEMENTS"` | Boolean | false | Optional |
| 9 | Forces/Moments | `"OPT_FORCE"` | Boolean | false | Optional |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "LOAD_POINT_SEL": 1,
      "INFL_GEN_POINT": 0,
      "NUM_UNIT_LOAD": 3,
      "ANALYSIS_RESULT": 2,
      "OPT_COMBINED_STR": true,
      "OPT_REACTIONS": true,
      "OPT_DISPLACEMENTS": true,
      "OPT_FORCE": false
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_moving_load_transverse():
    payload = {
        "Assign": {
            "1": {
                "LOAD_POINT_SEL": 1,       # 영향선 종속점
                "INFL_GEN_POINT": 0,       # Number/Line Element
                "NUM_UNIT_LOAD": 3,        # 단위하중 분할 수
                "ANALYSIS_RESULT": 2,      # Normal + 동시력/응력
                "OPT_COMBINED_STR": True,  # 조합 응력
                "OPT_REACTIONS": True,     # 반력
                "OPT_DISPLACEMENTS": True, # 변위
                "OPT_FORCE": False         # 부재력/모멘트
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/MVCTtr", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Moving Load Control (Transverse) set:", resp.json())

set_moving_load_transverse()
```

---

## 14. /db/SMCT — Settlement Analysis Control Data

침하(Settlement) 해석 제어 데이터를 정의합니다. 판/링크 요소의 동시력(Concurrent Force) 계산 활성화 여부를 설정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/SMCT` | 생성 |
| GET | `{base_url}/db/SMCT` | 조회 |
| PUT | `{base_url}/db/SMCT/{id}` | 수정 |
| DELETE | `{base_url}/db/SMCT/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Plate Concurrent Force (Active: true / Inactive: false) | `"CONCURRENT_CALC"` | Boolean | false | Optional |
| 2 | Elastic / General Links Concurrent Force (Active: true / Inactive: false) | `"CONCURRENT_LINK"` | Boolean | false | Optional |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "CONCURRENT_CALC": true,
      "CONCURRENT_LINK": false
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_settlement_control():
    payload = {
        "Assign": {
            "1": {
                "CONCURRENT_CALC": True,   # 판 요소 동시력 계산
                "CONCURRENT_LINK": False   # 링크 요소 동시력 계산
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/SMCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Settlement Control set:", resp.json())

set_settlement_control()
```

---

## 15. /db/NLCT — Nonlinear Analysis Control Data

비선형(Nonlinear) 해석 제어 데이터를 정의합니다. 비선형 타입, 반복법(Newton-Raphson/Arc-Length/Displacement-Control)에 따라 하중케이스별 제어 항목(`NEWTON_ITEMS`/`ARCLEN_ITEMS`/`DISPCT_ITEMS`)을 사용합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/NLCT` | 생성 |
| GET | `{base_url}/db/NLCT` | 조회 |
| PUT | `{base_url}/db/NLCT/{id}` | 수정 |
| DELETE | `{base_url}/db/NLCT/{id}` | 삭제 |

### Parameters — 공통

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Nonlinear Type (Geometry: `"GEOM"` / Material: `"MATL"` / Both: `"GEOM+MATL"`) | `"NONLINEAR_TYPE"` | String | "GEOM" | Optional |
| 2 | Iteration Method (Newton-Raphson: `"NEWTON"` / Arc-Length: `"ARC"` / Displacement-Control: `"DISP"`) | `"ITERATION_METHOD"` | String | "NEWTON" | Optional |
| 3 | Energy Norm 사용 | `"OPT_ENERGY_NORM"` | Boolean | false | Optional |
| 4 | Energy Norm | `"ENERGY_NORM"` | Number | - | Required |
| 5 | Displacement Norm 사용 | `"OPT_DISPLACEMENT_NORM"` | Boolean | false | Optional |
| 6 | Displacement Norm | `"DISPLACEMENT_NORM"` | Number | - | Required |
| 7 | Force Norm 사용 | `"OPT_FORCE_NORM"` | Boolean | false | Optional |
| 8 | Force Norm | `"FORCE_NORM"` | Number | - | Required |

### Parameters — Newton-Raphson (`ITERATION_METHOD = "NEWTON"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 9 | Number of Load Steps | `"NUMBER_STEPS"` | Integer | - | Required |
| 10 | Maximum Number of Iterations/Load Step | `"MAX_ITERATIONS"` | Integer | - | Required |
| 11 | Load Case Specific Data | `"NEWTON_ITEMS"` | Array [Object] | - | Required |
| (1) | Iteration Method (`"NEWTON"`) | `"ITERATION_METHOD"` | String | "NEWTON" | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Number of Load Steps | `"NUMBER_STEPS"` | Number | - | Required |
| (4) | Max Iterations/Load Step | `"MAX_ITERATIONS"` | Integer | - | Required |
| (5) | Load Factor (Index: Step) | `"LOAD_FACTORS"` | Array [Number] | 1 | Optional |

### Parameters — Arc-Length (`ITERATION_METHOD = "ARC"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 9 | Number of Load Steps | `"NUMBER_STEPS"` | Integer | - | Required |
| 10 | Maximum Number of Iterations/Load Step | `"MAX_ITERATIONS"` | Integer | - | Required |
| 11 | Initial Force Ratio for Unit Arc-Length | `"INITIAL_FORCE_RATIO_ARC_LEN"` | Number | - | Required |
| 12 | Maximum Displacement Bound | `"MAXIMUM_DISPLACEMENT"` | Number | 0 | Optional |
| 13 | Load Case Specific Data | `"ARCLEN_ITEMS"` | Array [Object] | - | Required |
| (1) | Iteration Method (`"ARC"`) | `"ITERATION_METHOD"` | String | "ARC" | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Initial Force Ratio for Unit Arc-Length | `"INITIAL_FORCE_RATIO_ARC_LEN"` | Number | - | Required |
| (4) | Number of Steps | `"NUMBER_STEPS"` | Number | - | Required |
| (5) | Max Iterations/Increment Step | `"MAX_ITERATIONS"` | Integer | - | Required |
| (6) | Maximum Displacement | `"MAXIMUM_DISPLACEMENT"` | Number | 0 | Optional |

> ⚠️ **2026-08-25 확인:** `MAXIMUM_DISPLACEMENT`(상단 12번, `ARCLEN_ITEMS`(6) 모두)가 원문
> Specifications 표·예제 둘 다 기본값 `0`/Optional인데 이전엔 Required로 잘못 기재돼 있었다
> (아티클 id `35990229420441`).

### Parameters — Displacement-Control (`ITERATION_METHOD = "DISP"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 9 | Number of Steps | `"NUMBER_STEPS"` | Integer | - | Required |
| 10 | Max Iterations/Load Step | `"MAX_ITERATIONS"` | Integer | - | Required |
| 11 | Master Node ID | `"MASTER_NODE"` | Integer | - | Required |
| 12 | Direction (Dx: 0 / Dy: 1 / Dz: 2) | `"DIRECTION"` | Integer | 0 | Optional |
| 13 | Maximum Displacement | `"MAXIMUM_DISPLACEMENT"` | Number | - | Required |
| 14 | Load Case Specific Data | `"DISPCT_ITEMS"` | Array [Object] | - | Required |
| (1) | Iteration Method (`"DISP"`) | `"ITERATION_METHOD"` | String | "DISP" | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Number of Steps | `"NUMBER_STEPS"` | Integer | - | Required |
| (4) | Max Iterations/Load Step | `"MAX_ITERATIONS"` | Number | - | Required |
| (5) | Master Node ID | `"MASTER_NODE"` | Integer | - | Required |
| (6) | Direction (Dx: 0 / Dy: 1 / Dz: 2) | `"DIRECTION"` | Integer | 0 | Optional |
| (7) | Maximum Displacement | `"MAXIMUM_DISPLACEMENT"` | Number | - | Required |
| (8) | Master Node Displacement (Index: Step) | `"LOAD_FACTORS"` | Array [Number] | 1 | Optional |

### Request Body — Newton-Raphson

```json
{
  "Assign": {
    "1": {
      "NONLINEAR_TYPE": "GEOM+MATL",
      "ITERATION_METHOD": "NEWTON",
      "NUMBER_STEPS": 1,
      "MAX_ITERATIONS": 30,
      "OPT_ENERGY_NORM": true,
      "ENERGY_NORM": 0.001,
      "OPT_DISPLACEMENT_NORM": true,
      "DISPLACEMENT_NORM": 0.001,
      "OPT_FORCE_NORM": true,
      "FORCE_NORM": 0.001,
      "NEWTON_ITEMS": [
        {
          "ITERATION_METHOD": "NEWTON",
          "LCNAME": "A",
          "NUMBER_STEPS": 1,
          "MAX_ITERATIONS": 30,
          "LOAD_FACTORS": [1]
        }
      ],
      "DISPCT_ITEMS": [
        {
          "ITERATION_METHOD": "DISP",
          "LCNAME": "B",
          "NUMBER_STEPS": 1,
          "MAX_ITERATIONS": 10,
          "MASTER_NODE": 1,
          "DIRECTION": 0,
          "MAXIMUM_DISPLACEMENT": 0.1,
          "LOAD_FACTORS": [1]
        }
      ]
    }
  }
}
```

### Request Body — Arc-Length

```json
{
  "Assign": {
    "1": {
      "NONLINEAR_TYPE": "GEOM+MATL",
      "ITERATION_METHOD": "ARC",
      "NUMBER_STEPS": 100,
      "MAX_ITERATIONS": 10,
      "INITIAL_FORCE_RATIO_ARC_LEN": 5,
      "MAXIMUM_DISPLACEMENT": 0,
      "OPT_ENERGY_NORM": true,
      "ENERGY_NORM": 0.001,
      "OPT_DISPLACEMENT_NORM": true,
      "DISPLACEMENT_NORM": 0.001,
      "OPT_FORCE_NORM": true,
      "FORCE_NORM": 0.001,
      "ARCLEN_ITEMS": [
        {
          "ITERATION_METHOD": "ARC",
          "LCNAME": "A",
          "INITIAL_FORCE_RATIO_ARC_LEN": 5,
          "NUMBER_STEPS": 100,
          "MAX_ITERATIONS": 10,
          "MAXIMUM_DISPLACEMENT": 1
        }
      ]
    }
  }
}
```

### Request Body — Displacement-Control

```json
{
  "Assign": {
    "1": {
      "NONLINEAR_TYPE": "GEOM+MATL",
      "ITERATION_METHOD": "DISP",
      "NUMBER_STEPS": 1,
      "MAX_ITERATIONS": 10,
      "MASTER_NODE": 1,
      "DIRECTION": 0,
      "MAXIMUM_DISPLACEMENT": 0.1,
      "OPT_ENERGY_NORM": true,
      "ENERGY_NORM": 0.001,
      "OPT_DISPLACEMENT_NORM": true,
      "DISPLACEMENT_NORM": 0.001,
      "OPT_FORCE_NORM": true,
      "FORCE_NORM": 0.001,
      "DISPCT_ITEMS": [
        {
          "ITERATION_METHOD": "DISP",
          "LCNAME": "B",
          "NUMBER_STEPS": 1,
          "MAX_ITERATIONS": 10,
          "MASTER_NODE": 1,
          "DIRECTION": 0,
          "MAXIMUM_DISPLACEMENT": 0.1,
          "LOAD_FACTORS": [1]
        }
      ]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_nonlinear_control_newton():
    payload = {
        "Assign": {
            "1": {
                "NONLINEAR_TYPE": "GEOM+MATL",     # 기하+재료 비선형
                "ITERATION_METHOD": "NEWTON",      # Newton-Raphson
                "NUMBER_STEPS": 1,
                "MAX_ITERATIONS": 30,
                "OPT_ENERGY_NORM": True,  "ENERGY_NORM": 0.001,
                "OPT_DISPLACEMENT_NORM": True, "DISPLACEMENT_NORM": 0.001,
                "OPT_FORCE_NORM": True,   "FORCE_NORM": 0.001,
                "NEWTON_ITEMS": [
                    {
                        "ITERATION_METHOD": "NEWTON",
                        "LCNAME": "PUSH",
                        "NUMBER_STEPS": 10,
                        "MAX_ITERATIONS": 30,
                        "LOAD_FACTORS": [0.1, 0.2, 0.3, 0.4, 0.5,
                                         0.6, 0.7, 0.8, 0.9, 1.0]
                    }
                ]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/NLCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Nonlinear Control (Newton-Raphson) set:", resp.json())

set_nonlinear_control_newton()
```

---

## 16. /db/NLCT-M1 — Nonlinear Analysis Control (Hyper-S)

Hyper-S(MEC) 솔버용 비선형 해석 제어입니다. `LC_SCOPE`로 적용 범위를 지정하고, `LOAD_STEPS`(스텝 모드/출력) 및 `CONV_CRITERIA`(수렴 기준)를 중첩 객체로 사용합니다. 반복법은 Force Control(`FORCE`), Arc Length(`ARC`), Displacement Control(`DISP`)을 지원합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| GET | `{base_url}/db/NLCT-M1` | 조회 |
| PUT | `{base_url}/db/NLCT-M1/{id}` | 수정 |
| DELETE | `{base_url}/db/NLCT-M1/{id}` | 삭제 |

### Parameters — 공통

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Load Case Scope (전체: `"ALL"` / 선택: `"SELECT"`, 기본 `"ALL"`) | `"LC_SCOPE"` | String (enum) | "ALL" | Optional |
| 6 | Load Case Name (`LC_SCOPE="SELECT"`로 신규 생성 시 필수. 기존 항목 수정 시 미지정하면 기존 값 유지) | `"LOAD_CASE"` | String | - | Required (조건부) |
| 2 | Nonlinear Type (`"GEOM"` / `"MATL"` / `"GEOM_MATL"`) | `"NONLINEAR_TYPE"` | String (enum) | - | Required |
| 3 | Iteration Method (Force: `"FORCE"` / Arc Length: `"ARC"` / Displacement: `"DISP"`) | `"ITER_METHOD"` | String (enum) | - | Required |
| 4 | Load Steps 설정 | `"LOAD_STEPS"` | Object | - | Required |
| 5 | Convergence Criteria | `"CONV_CRITERIA"` | Object | - | Required |
| 7 | 고급 설정 (미지정 시 서버 기본값 적용) | `"ADVANCED"` | Object | - | Optional |

> ⚠️ **2026-08-25 확인:** `LOAD_CASE`(6번)가 이전 문서엔 전혀 없었다 — `LC_SCOPE="SELECT"`로
> 신규 항목을 만들 때 필수인 필드다. `ADVANCED`(7번) 객체도 통째로 누락돼 있었다(아티클 id
> `56506850582425`). 원문 JSON Schema에 이례적으로 상세한 구현 주석이 함께 실려 있어 이를
> 근거로 반영했다.

### Parameters — LOAD_STEPS 객체 (`ITER_METHOD`별 사용 필드가 다름)

| Key | Value Type | Default | Description |
| --- | --- | --- | --- |
| `"STEP_MODE"` | String (enum: `"AUTO"`/`"MANUAL"`) | - | 스텝 모드 (Required). `ITER_METHOD="ARC"`일 때는 UI상 `"AUTO"`로 고정 |
| `"NUMBER_STEPS"` | Integer (≥1) | 1 | 스텝 수 (`STEP_MODE="AUTO"`일 때 필수) |
| `"OUTPUT"` | String (enum: `"EVERY"`/`"LAST"`) | "EVERY" | 중간 출력 (`STEP_MODE="AUTO"`일 때 필수) |
| `"MANUAL_STEPS"` | Array [Number] (≥1개) | - | 사용자 정의 스텝 목록 (`STEP_MODE="MANUAL"`일 때) |
| `"MIN_ARC_RATIO"` | Number (>0) | 0.25 | (`ITER_METHOD="ARC"`) 최소 호장 조정 비율 |
| `"MAX_ARC_RATIO"` | Number (>0) | 4.0 | (`ITER_METHOD="ARC"`) 최대 호장 조정 비율 |
| `"MAX_ARC_INCREMENTS"` | Integer (≥1) | 100 | (`ITER_METHOD="ARC"`) 최대 호장 증분 수 |
| `"MASTER_NODE"` | Integer | 0 | (`ITER_METHOD="DISP"`) 주 절점 ID |
| `"MAX_DISP"` | Number (0 금지) | - | (`ITER_METHOD="DISP"`) 최대 변위 — 서버가 0을 채우면 검증 실패하므로 명시적 값 필수 |
| `"DIRECTION"` | String (enum: `"DX"`/`"DY"`/`"DZ"`) | "DX" | (`ITER_METHOD="DISP"`) 방향 |
| `"REF_NODE"` | Object | - | (`ITER_METHOD="DISP"`) 기준(상대) 절점 — 하위 `OPT_USE`(Boolean, Required)/`NODE`(Integer, `OPT_USE=false`시 기본 0) |

### Parameters — CONV_CRITERIA 객체

`DISP`(변위) / `LOAD`(하중) / `WORK`(일) 각각 — 최소 1개는 `OPT_USE=true`:

| Key | Value Type | Default | Description |
| --- | --- | --- | --- |
| `"OPT_USE"` | Boolean | - | 해당 기준 사용 여부 (Required) |
| `"VALUE"` | Number (0 초과 1 이하) | 0.001 | 허용오차 (`OPT_USE=true`일 때 필수) |

### Parameters — ADVANCED 객체 (고급 비선형 설정, 전체 Optional — 미지정 시 서버 기본값 사용)

| Key | Value Type | Default | Description |
| --- | --- | --- | --- |
| `"OPT_USE_DEFAULT"` | Boolean | - | 기본 설정 사용 여부 (Required — true면 아래 필드 모두 미지정 허용) |
| `"STIFF_UPDATE_SCHEME"` | String (enum: `"CUSTOM"`/`"FULL_NEWTON_RAPHSON"`/`"INITIAL_STIFF"`) | - | 강성 갱신 방식 |
| `"ITER_BEFORE_STIFF_UPDATE"` | Integer | - | 강성 갱신 전 반복 횟수 (`CUSTOM`이 아니면 방식별 서버 자동값 적용) |
| `"OPT_TERMINATE_ON_FAILED_CONV"` | Boolean | false | 수렴 실패 시 해석 종료 여부 |
| `"MAX_ITER_PER_INCREMENT"` | Integer | 50 | 증분당 최대 반복 횟수 |
| `"MAX_BISECTION_LEVEL"` | Integer (0~20) | 5 | 최대 이분(Bisection) 단계 |
| `"OPT_SMART_BISECTION"` | Boolean | false | Smart Bisection 사용 여부 |
| `"DIVERGENCE_THRESHOLD"` | Number | 3 | 발산 판정 임계값 |
| `"OPT_ENABLE_LINE_SEARCH"` | Boolean | true | Line Search 사용 여부 |
| `"LINE_SEARCH_OPTION"` | String (enum: `"AUTO"`/`"MANUAL"`) | - | Line Search 방식 |
| `"MAX_LINE_SEARCH_PER_ITER"` | Integer | 4 | 반복당 최대 Line Search 횟수 |
| `"LINE_SEARCH_TOL"` | Number | 0.5 | Line Search 허용오차 |

### Request Body — Force Control

```json
{
  "Assign": {
    "1": {
      "LC_SCOPE": "ALL",
      "NONLINEAR_TYPE": "GEOM",
      "ITER_METHOD": "FORCE",
      "LOAD_STEPS": {
        "STEP_MODE": "AUTO",
        "NUMBER_STEPS": 10,
        "OUTPUT": "EVERY"
      },
      "CONV_CRITERIA": {
        "DISP": { "OPT_USE": true, "VALUE": 0.001 }
      }
    }
  }
}
```

### Request Body — Arc Length

```json
{
  "Assign": {
    "1": {
      "LC_SCOPE": "ALL",
      "NONLINEAR_TYPE": "GEOM_MATL",
      "ITER_METHOD": "ARC",
      "LOAD_STEPS": {
        "STEP_MODE": "AUTO",
        "NUMBER_STEPS": 20,
        "OUTPUT": "LAST",
        "MIN_ARC_RATIO": 0.25,
        "MAX_ARC_RATIO": 4,
        "MAX_ARC_INCREMENTS": 100
      },
      "CONV_CRITERIA": {
        "DISP": { "OPT_USE": true, "VALUE": 0.001 },
        "LOAD": { "OPT_USE": true, "VALUE": 0.001 }
      }
    }
  }
}
```

### Request Body — Displacement Control

```json
{
  "Assign": {
    "1": {
      "LC_SCOPE": "ALL",
      "NONLINEAR_TYPE": "MATL",
      "ITER_METHOD": "DISP",
      "LOAD_STEPS": {
        "STEP_MODE": "AUTO",
        "NUMBER_STEPS": 15,
        "OUTPUT": "EVERY",
        "MASTER_NODE": 101,
        "MAX_DISP": 0.05,
        "DIRECTION": "DX",
        "REF_NODE": { "OPT_USE": false }
      },
      "CONV_CRITERIA": {
        "WORK": { "OPT_USE": true, "VALUE": 0.001 }
      }
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def update_nonlinear_control_m1_arc():
    payload = {
        "Assign": {
            "1": {
                "LC_SCOPE": "ALL",
                "NONLINEAR_TYPE": "GEOM_MATL",
                "ITER_METHOD": "ARC",           # Arc Length 방식
                "LOAD_STEPS": {
                    "STEP_MODE": "AUTO",
                    "NUMBER_STEPS": 20,
                    "OUTPUT": "LAST",
                    "MIN_ARC_RATIO": 0.25,
                    "MAX_ARC_RATIO": 4,
                    "MAX_ARC_INCREMENTS": 100
                },
                "CONV_CRITERIA": {
                    "DISP": {"OPT_USE": True, "VALUE": 0.001},
                    "LOAD": {"OPT_USE": True, "VALUE": 0.001}
                }
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/NLCT-M1/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Nonlinear Control (Hyper-S, Arc) updated:", resp.json())

update_nonlinear_control_m1_arc()
```

---

## 17. /db/STCT — Construction Stage Analysis Control Data

시공단계(Construction Stage) 해석 제어 데이터를 정의합니다. 해석 타입(`iINC_NLA`: 선형/비선형/재료비선형)과 단계 옵션(`iNLA_TYPE`: 독립/누가)에 따라 사용하는 파라미터가 달라집니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/STCT` | 생성 |
| GET | `{base_url}/db/STCT` | 조회 |
| PUT | `{base_url}/db/STCT/{id}` | 수정 |
| DELETE | `{base_url}/db/STCT/{id}` | 삭제 |

### Parameters — 공통 / 핵심

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Final Stage Option (Last: true / Other: false) | `"bLAST_FINAL"` | Boolean | false | Optional |
| 2 | Construction Stage Name (when `bLAST_FINAL` false) | `"FINAL_STAGE"` | String | - | Required |
| 3 | Analysis Type (Linear: 0 / Nonlinear ¹⁾: 1 / Material Nonlinear ¹⁾: 2) | `"iINC_NLA"` | Integer | 0 | Optional |
| 4 | Stage Option (Independent: 0 / Accumulative: 1) | `"iNLA_TYPE"` | Integer | 0 | Optional |

> **¹⁾** 비선형/재료비선형 해석은 MIDAS Civil NX 전용입니다.

### Parameters — Erection Load (C.S. 출력용 사하중 구분)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 6 | Erection Load for Construction Stage | `"vEREC"` | Array [Object] | Empty | Optional |
| (1) | Erection Load Case Name | `"LTYPECC"` | String | - | Required |
| (2) | Load Type for C.S ⁴⁾ | `"EREC"` | String | - | Required |
| (3) | Load Case Name List | `"vLCNAME"` | Array [String] | - | Required |
| 8 | Secondary Dead Load Effect for Grid Model (MIDAS Civil NX JP 버전 전용) | `"bSDLE"` | Boolean | false | Optional |
| 9 | Load Case Name List (Grid Analysis Load, JP 버전 전용) | `"vSDLE"` | Array [String] | - | Required |

> **⁴⁾ `EREC` 값 목록** (Erection Load Type for C.S.): Dead Load: `"D"` / Dead Load of Component
> and Attachments: `"DC"` / Dead Load of Wearing Surfaces and Utilities: `"DW"` / Earth Pressure:
> `"EP"` / Live Load: `"L"` / Wind Load on Structure: `"W"` / Temperature: `"T"` / Temperature
> Gradient: `"TPG"` / Earthquake: `"E"` / Erection Load: `"ER"`.
>
> ⚠️ **2026-08-25 확인:** `bSDLE`/`vSDLE`(9번)와 `EREC`의 값 목록(각주 ⁴⁾)이 이전 문서엔 없었다
> — `bSDLE`/`vSDLE`는 STCT-M1 절엔 이미 있었으나 STCT 본절에는 누락돼 있었다(아티클 id
> `35990281053465`).

### Parameters — Cable-Pretension / Initial Force Control

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 7 | Cable-Pretension Force Type (Internal: `"INTERNAL"` / External: `"EXTERNAL"`) | `"CPFC"` | String | "INTERNAL" | Optional |
| - | External Force Type (대체 여부) | `"bEXT_REPL"` | Boolean | false | Optional |
| 8 | Convert Final Stage Member Forces to Initial Forces for Post C.S | `"bCONV"` | Boolean | false | Optional |
| 9 | Truss (when `bCONV` true) | `"bTRUSS"` | Boolean | false | Optional |
| 10 | Beam (when `bCONV` true) | `"bBEAM"` | Boolean | false | Optional |
| 11 | Change Cable Element to Equivalent Truss for Post C.S. | `"bCHANGE_CABLE"` | Boolean | false | Optional |
| 12 | Apply Initial Member Force to C.S | `"bAPPLY_IMF"` | Boolean | false | Optional |

### Parameters — Initial Displacement / Camber / 기타

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| - | Initial Tangent Displacement 사용 | `"bITD"` | Boolean | false | Optional |
| - | Initial Tangent Displacement Type (All: `"ALL"` / Structure Group: `"GROUP"`) | `"ITD"` | String | "ALL" | Optional |
| - | Structure Group Name (`ITD`="GROUP"일 때) | `"GROUP"` | String | - | Required (조건부) |
| - | Lack-of-Fit Force Control 사용 | `"bLFFC"` | Boolean | false | Optional |
| - | Lack-of-Fit Group Name (`bLFFC`=true일 때) | `"LFFGR"` | String | - | Required (조건부) |
| - | Apply Camber Displacement to C.S. | `"bCAMBER"` | Boolean | false | Optional |
| - | Calculate Concurrent Forces of Frame | `"bCALC_CFF"` | Boolean | false | Optional |
| - | Calculate Output of Each Part of Composite Section | `"bCALC_CSP"` | Boolean | false | Optional |
| - | Self-constrained Forces & Stresses | `"bSELFCONS"` | Boolean | false | Optional |
| - | Save Output of Construction Stage | `"bSAVE_OCS"` | Boolean | false | Optional |
| - | Stress Decrease 사용 / 옵션 / 상수 | `"bSD"` / `"iSDOPT"` / `"SDCONST"` | Boolean / Integer / Number | - | Optional |
| - | Beam Section Property Option (Constant: 0 / Change with Tendon: 1) | `"iBSC"` | Integer | 0 | Optional |

> ⚠️ **2026-08-25 확인:** `iBSC`는 이전 문서에 "Bi-Section Control"(이분법 반복제어)로 잘못
> 라벨링돼 있었으나, 원문 표는 "Beam Section Property Option"(보 단면 물성 변경 방식,
> 0=Constant/1=Change with Tendon)으로 완전히 다른 개념이다 — 이분법 관련 제어는 별도의
> `BSSTEP`/`ADSTEP`(아래 Nonlinear Analysis 절)가 담당한다. `ITD` 기본값도 `-`→`"ALL"`로,
> `GROUP`/`LFFGR`는 각각 조건부 Required로 정정(아티클 id `35990281053465`).

### Parameters — Linear & Independent Stage

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Include P-Delta Effect ²⁾ | `"bINC_PDL"` | Boolean | false | Optional |
| - | Number of Iterations | `"iITER"` | Integer | - | Optional |
| - | Convergence Tolerance | `"TOL"` | Number | - | Optional |

### Parameters — Nonlinear Analysis (`iINC_NLA` = 1 또는 2)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| - | Number of Load Steps | `"iLSTEP"` | Integer | - | Optional |
| - | Maximum Number of Iterations | `"iMAXITER"` | Integer | - | Optional |
| - | Convergence Failure 사용 | `"CF"` | Boolean | false | Optional |
| - | Max Bi-Section Level for a Load Step | `"BSSTEP"` | Integer | - | Optional |
| - | Max Allowable Diverged Steps | `"ADSTEP"` | Integer | - | Optional |
| - | Energy Norm 사용 / 값 | `"bENEG"` / `"EV"` | Boolean / Number | - | Optional |
| - | Displacement Norm 사용 / 값 | `"bDISP"` / `"DV"` | Boolean / Number | - | Optional |
| - | Force Norm 사용 / 값 | `"bFORC"` / `"FV"` | Boolean / Number | - | Optional |
| - | Include Equilibrium Element Nodal Forces | `"bIEMF"` | Boolean | false | Optional |

### Parameters — Time Dependent Effect (누가 단계, `iNLA_TYPE` = 1)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| - | Include Time Dependent Effect | `"bINC_TDE"` | Boolean | false | Optional |
| - | Creep & Shrinkage 사용 | `"bCNS"` | Boolean | false | Optional |
| - | Creep & Shrinkage Type (`"CREEP"`/`"SHRINK"`/`"BOTH"`) | `"TYPE"` | String | - | Optional |
| - | Number of Creep Iterations | `"iITER_CR"` | Integer | - | Optional |
| - | Creep Tolerance | `"TOL_CR"` | Number | 0 | Optional |
| - | Only User's Creep Coefficient | `"bOUCC"` | Boolean | false | Optional |
| - | Internal Time Step for Creep 사용 | `"bITS"` | Boolean | false | Optional |
| - | Internal Time Step for Creep 값 | `"iITS"` | Integer | - | Required |
| - | Auto Time Step Generation for Large Time Gap | `"bATS"` | Boolean | false | Optional |
| - | Time Gap Steps (T>10 / >100 / >1000 / >5000 / >10000) | `"iT10"` / `"iT100"` / `"iT1K"` / `"iT5K"` / `"iT10K"` | Integer | - | Optional |
| - | Tendon Tension Loss Effect (Creep&Shrinkage) | `"bTTLE_CS"` | Boolean | false | Optional |
| - | Consider Re-bar Confinement Effect | `"bRCE"` | Boolean | false | Optional |
| - | Variation of Comp. Strength | `"bVAR"` | Boolean | false | Optional |
| - | Tendon Tension Loss Effect (Elastic Shortening) 사용 / 타입 | `"bTTLE_ES"` / `"iTTLE_ES"` | Boolean / Integer | - | Optional |
| - | Apply Time Dependent Elastic Modulus to Post C.S | `"bAPPLY_ELA"` | Boolean | false | Optional |

> ⚠️ **2026-08-25 확인:** `TOL_CR` 기본값 `-`→`0`, `iITS`는 원문 표에서 `bITS`와 분리된 별도
> 행으로 Required 표기돼 있어(이전엔 `bITS`/`iITS`를 하나로 묶어 `-`/Optional로 잘못 기재) 정정
> (아티클 id `35990281053465`).

### Request Body — Linear Analysis and Independent Stage

```json
{
  "Assign": {
    "1": {
      "bLAST_FINAL": false,
      "FINAL_STAGE": "CS1",
      "iINC_NLA": 0,
      "iNLA_TYPE": 0,
      "bINC_PDL": true,
      "iITER": 30,
      "TOL": 0.01,
      "vEREC": [
        { "LTYPECC": "Erection Load 1", "EREC": "D", "vLCNAME": ["A", "B"] },
        { "LTYPECC": "Erection Load 2", "EREC": "DC", "vLCNAME": ["C"] }
      ],
      "CPFC": "EXTERNAL",
      "bCONV": true,
      "bTRUSS": true,
      "bBEAM": true,
      "bCHANGE_CABLE": true,
      "bAPPLY_IMF": true,
      "bCAMBER": true,
      "bSD": true,
      "iSDOPT": 1,
      "SDCONST": 1,
      "iBSC": 0
    }
  }
}
```

### Request Body — Nonlinear Analysis and Accumulative Stage

```json
{
  "Assign": {
    "1": {
      "bLAST_FINAL": false,
      "FINAL_STAGE": "CS1",
      "iINC_NLA": 1,
      "iNLA_TYPE": 1,
      "iLSTEP": 1,
      "iMAXITER": 30,
      "CF": false,
      "BSSTEP": 5,
      "ADSTEP": 3,
      "bENEG": false, "EV": 0.01,
      "bDISP": true, "DV": 0.01,
      "bFORC": false, "FV": 0.01,
      "bINC_TDE": true,
      "bCNS": true,
      "TYPE": "BOTH",
      "iITER_CR": 5,
      "TOL_CR": 0.01,
      "bTTLE_CS": true,
      "bRCE": false,
      "bVAR": true,
      "bTTLE_ES": true,
      "iTTLE_ES": 0,
      "bAPPLY_ELA": false,
      "bOUCC": false,
      "bITS": false,
      "iITS": 2,
      "bATS": true,
      "iT10": 2, "iT100": 5, "iT1K": 7, "iT5K": 10, "iT10K": 20,
      "CPFC": "EXTERNAL",
      "bEXT_REPL": true,
      "bCONV": true,
      "bTRUSS": true,
      "bBEAM": true,
      "bCHANGE_CABLE": true,
      "bITD": true,
      "ITD": "GROUP",
      "GROUP": "Strt Group 1",
      "bLFFC": true,
      "LFFGR": "Strt Group 1",
      "bCAMBER": true,
      "iBSC": 1,
      "bCALC_CFF": true,
      "bCALC_CSP": true,
      "bSELFCONS": true,
      "bSAVE_OCS": false
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_construction_stage_control():
    payload = {
        "Assign": {
            "1": {
                "bLAST_FINAL": False,
                "FINAL_STAGE": "CS1",   # 대상 시공단계
                "iINC_NLA": 0,          # 선형 해석
                "iNLA_TYPE": 1,         # 누가 단계 (시간의존효과 고려)
                "bINC_PDL": True,
                "iITER": 30,
                "TOL": 0.01,
                "bINC_TDE": True,       # 시간의존효과 포함
                "bCNS": True,           # 크리프 & 건조수축
                "TYPE": "BOTH",
                "iITER_CR": 5,
                "TOL_CR": 0.01,
                "CPFC": "EXTERNAL",     # 케이블 프리텐션: 외력
                "bCONV": True, "bTRUSS": True, "bBEAM": True,
                "bCHANGE_CABLE": True,
                "bCAMBER": True
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/STCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Construction Stage Control set:", resp.json())

set_construction_stage_control()
```

---

## 18. /db/STCT-M1 — Construction Stage Analysis Control Data (Hyper-S)

Hyper-S(MEC) 솔버용 시공단계 해석 제어입니다. 기능별로 중첩 객체(`ANAL_TYPE`, `RESTART_CS_ANAL`, `ERECTION_LOAD`, `TIME_DEP_CONTROL`, `CABLE_CONTROL`, `INITIAL_CONTROL`, `INITIAL_DISP`, `STRESS_DECREASE`)로 재구성되었습니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| GET | `{base_url}/db/STCT-M1` | 조회 |
| PUT | `{base_url}/db/STCT-M1/{id}` | 수정 |
| DELETE | `{base_url}/db/STCT-M1/{id}` | 삭제 |

### Parameters — 최상위

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Final Stage Option (Last: true / Other: false) | `"bLAST_FINAL"` | Boolean | - | Optional |
| 2 | Analysis Type 설정 | `"ANAL_TYPE"` | Object | - | Required |
| 3 | Restart C.S. Analysis 설정 | `"RESTART_CS_ANAL"` | Object | - | Optional |
| 4 | Erection Load 목록 | `"ERECTION_LOAD"` | Array [Object] | - | Optional |
| 5 | Self-weight Dead Load for Erection 사용 / 목록 | `"bSDLE"` / `"vSDLE"` | Boolean / Array [String] | - | Optional |
| 6 | Time Dependent Control | `"TIME_DEP_CONTROL"` | Object | - | Optional |
| 7 | Cable Control | `"CABLE_CONTROL"` | Object | - | Optional |
| 8 | Initial Force Control | `"INITIAL_CONTROL"` | Object | - | Optional |
| 9 | Initial Displacement Control | `"INITIAL_DISP"` | Object | - | Optional |
| 10 | Stress Decrease Control | `"STRESS_DECREASE"` | Object | - | Optional |
| 11 | Beam Section Property Option (Constant: 0 / Change with Tendon: 1) | `"iBSC"` | Integer | 1 | Optional |
| 12 | Frame Output 설정 | `"FRAME_OUTPUT"` | Object | - | Optional |
| 13 | Save Output of Current Stage (Beam/Truss) | `"bSAVE_OCS"` | Boolean | false | Optional |
| 14 | Nonlinear Analysis Control (`iINC_NLA` ≠ 0일 때) | `"NONL_CONTROL"` | Object | - | Optional |

> ⚠️ **2026-08-25 확인:** `iBSC`/`FRAME_OUTPUT`/`bSAVE_OCS`/`NONL_CONTROL` 4개 필드가 통째로
> 누락돼 있었다. 특히 `iBSC`는 레거시 `STCT`(17번 절)와 이름은 같지만 **기본값이 다르다**
> (STCT는 0, STCT-M1은 1)(아티클 id `57053813627673`).

### Parameters — ANAL_TYPE 객체

| Key | Value Type | Description |
|-----|------------|-------------|
| `"iINC_NLA"` | Integer | 해석 타입 (Linear: 0 / Geometric Nonlinear: 1 / Material Nonlinear: 2 / Geometric+Material Nonlinear: 3) |
| `"iNLA_TYPE"` | Integer | 단계 옵션 (Independent: 0 / Accumulative: 1) — `iINC_NLA`=2 또는 3이면 `iNLA_TYPE`=1만 허용 |
| `"bIEMF"` | Boolean | Include Equilibrium Element Nodal Forces (`iINC_NLA`=1 & `iNLA_TYPE`=0일 때만) |
| `"bINC_PDL"` | Boolean | Include P-Delta Effect (`iINC_NLA`=0일 때만) |
| `"bINC_TDE"` | Boolean | Include Time Dependent Effect (`iNLA_TYPE`=1 & `iINC_NLA`∈{0,1}일 때만) |

> ⚠️ **2026-08-25 확인:** `iINC_NLA`에 4번째 값(3 = Geometric+Material Nonlinear 동시 고려)이
> 추가돼 있었고, `bIEMF`가 통째로 누락돼 있었다(아티클 id `57053813627673`).

### Parameters — RESTART_CS_ANAL 객체

| Key | Value Type | Description |
|-----|------------|-------------|
| `"OPT_USE"` | Boolean | Restart 해석 사용 여부 |
| `"RESTART_STAGE"` | Array [String] | Restart 대상 시공단계 목록 |

### Parameters — ERECTION_LOAD 항목

| Key | Value Type | Description |
|-----|------------|-------------|
| `"LTYPECC"` | String | Erection Load Case Name |
| `"EREC"` | String | Load Type for C.S (`"D"`, `"W"`, …) |
| `"vLCNAME"` | Array [String] | Load Case Name List |

### Parameters — TIME_DEP_CONTROL 객체

| Key | Value Type | Description |
|-----|------------|-------------|
| `"CREEP_SHRINKAGE"` | Object | 크리프·건조수축 설정 |
| `"CREEP_SHRINKAGE.OPT_USE"` | Boolean | 사용 여부 |
| `"CREEP_SHRINKAGE.TYPE"` | String | (`"CREEP"`/`"SHRINKAGE"`/`"BOTH"`) |
| `"CREEP_SHRINKAGE.bOUCC"` | Boolean | Only User's Creep Coefficient |
| `"CREEP_SHRINKAGE.INTERNAL_STEP"` | Object | `{ "OPT_USE": bool, "iITS": int }` |
| `"CREEP_SHRINKAGE.AUTO_TIME_STEP"` | Object | `{ "OPT_USE": bool, "iT10","iT100","iT1K","iT5K","iT10K": int }` |
| `"CREEP_SHRINKAGE.bTTLE_CS"` | Boolean | Tendon Tension Loss Effect |
| `"CREEP_SHRINKAGE.bRCE"` | Boolean | Re-bar Confinement Effect |
| `"bVAR"` | Boolean | Variation of Comp. Strength |
| `"bAPPLY_ELA"` | Boolean | Apply Time Dep. Elastic Modulus to Post C.S |
| `"bTTLE_ES"` / `"iTTLE_ES"` | Boolean / Integer | Tendon Tension Loss (Elastic Shortening) / Type |

> ⚠️ **2026-08-25 확인:** `CREEP_SHRINKAGE.TYPE`의 두 번째 enum 값은 레거시 `STCT`(17번 절)의
> `"SHRINK"`와 달리 STCT-M1에서는 **`"SHRINKAGE"`**로 표기된다 — 원문 JSON Schema·Specifications
> 표 양쪽에서 일관되게 확인됨(아티클 id `57053813627673`). 이전 문서는 STCT와 동일하게
> `"SHRINK"`로 잘못 기재돼 있었다.

### Parameters — NONL_CONTROL 객체 (`iINC_NLA` ≠ 0일 때 사용 — 레거시 `NLCT`/`NLCT-M1`에 대응)

| Key | Value Type | Default | Description |
| --- | --- | --- | --- |
| `"iLSTEP"` | Integer (≥1) | - | 증분 스텝 수 |
| `"INTOUT"` | String (enum: `"EVERY"`/`"LAST"`) | "LAST" | 중간 출력 요청 |
| `"ADVANCED"` | Object | - | 고급 설정 — 하위 `USE_DEF_SETTINGS`(Boolean, Required, 기본 true)/`STIFF_UPD_SCHEME`(Integer enum 0=Custom·1=Full Newton-Raphson·2=Initial Stiffness, `USE_DEF_SETTINGS=false`일 때)/`ITER_BEF_UPDATE`(Integer, `STIFF_UPD_SCHEME=0`일 때만)/`TERMINATE_ON_FAIL_CONV`(Boolean)/`MAX_ITER_INCREMENT`(Integer)/`MAX_BISECT_LEVEL`(Integer)/`SMART_BISECT`(Boolean)/`DIVERG_THRESH`(Number)/`ENABLE_LINE_SEARCH`(Boolean, 기본 true)/`LINE_SEARCH`(Object, `ENABLE_LINE_SEARCH=true`일 때 필수 — 하위 `OPT_USE`(Boolean,Required)/`LINE_SEARCH_TYPE`(enum `"AUTO"`/`"USER"`, 기본 AUTO)/`MAX_LN_SRCH_ITER`(Integer, `LINE_SEARCH_TYPE="USER"`일 때)/`LN_SEARCH_TOL`(Number, 〃)) |
| `"DISP"`/`"LOAD"`/`"WORK"` | Object | - | 변위/하중/일 수렴기준 — 각각 하위 `OPT_USE`(Boolean, Required, 기본 false)/`VALUE`(Number >0, `OPT_USE=true`일 때 필수) |

> `ADVANCED`의 Key 이름은 §16 `NLCT-M1`의 `ADVANCED` 객체(`STIFF_UPDATE_SCHEME`/`ITER_BEFORE_STIFF_UPDATE`/…, 문자열 enum)와 유사하지만 **이름과 타입이 다르다**
> (STCT-M1은 `STIFF_UPD_SCHEME`/`ITER_BEF_UPDATE`/… 및 정수 enum, `LINE_SEARCH`도 중첩 객체) —
> 같은 개념이라도 엔드포인트별로 직렬화가 다르므로 혼용하지 말 것(아티클 id `57053813627673`).

### Parameters — 나머지 객체

| Object | Key | Value Type | Description |
|--------|-----|------------|-------------|
| `CABLE_CONTROL` | `"CPFC"` | String | Cable-Pretension Force Type (`"INTERNAL"`/`"EXTERNAL"`) |
| `CABLE_CONTROL` | `"bEXT_REPL"` | Boolean | External Force Replace |
| `INITIAL_CONTROL` | `"bCONV"` | Boolean | Convert Final Stage Forces to Initial Forces |
| `INITIAL_CONTROL` | `"bTRUSS"` / `"bBEAM"` | Boolean | Truss / Beam |
| `INITIAL_CONTROL` | `"bCHANGE_CABLE"` | Boolean | Change Cable to Equivalent Truss |
| `INITIAL_CONTROL` | `"bAPPLY_IMF"` | Boolean | Apply Initial Member Force to C.S |
| `INITIAL_DISP` | `"ITD_CONTROL"` | Object | `{ "OPT_USE", "ITD", "GROUP", "LFFC_OPT_USE", "LFFGR" }` |
| `INITIAL_DISP` | `"bCAMBER"` | Boolean | Apply Camber Displacement |
| `STRESS_DECREASE` | `"OPT_USE"` / `"iSDOPT"` / `"SDCONST"` | Boolean / Integer / Number | Stress Decrease 사용 / 옵션 / 상수 |

### Request Body (PUT)

```json
{
  "Assign": {
    "1": {
      "bLAST_FINAL": true,
      "ANAL_TYPE": {
        "iINC_NLA": 0,
        "iNLA_TYPE": 1,
        "bINC_PDL": true,
        "bINC_TDE": true
      },
      "RESTART_CS_ANAL": {
        "OPT_USE": true,
        "RESTART_STAGE": ["CS1", "CS2"]
      },
      "ERECTION_LOAD": [
        { "LTYPECC": "Erection Dead Load", "EREC": "D", "vLCNAME": ["Self Weight", "Deck Concrete"] },
        { "LTYPECC": "Erection Wind Load", "EREC": "W", "vLCNAME": ["Wind Load"] }
      ],
      "bSDLE": true,
      "vSDLE": ["Grid Dead Load", "Grid Wearing Surface"],
      "TIME_DEP_CONTROL": {
        "CREEP_SHRINKAGE": {
          "OPT_USE": true,
          "TYPE": "BOTH",
          "bOUCC": false,
          "INTERNAL_STEP": { "OPT_USE": true, "iITS": 5 },
          "AUTO_TIME_STEP": {
            "OPT_USE": true,
            "iT10": 2, "iT100": 5, "iT1K": 10, "iT5K": 20, "iT10K": 30
          },
          "bTTLE_CS": true,
          "bRCE": true
        },
        "bVAR": true,
        "bAPPLY_ELA": true,
        "bTTLE_ES": true,
        "iTTLE_ES": 0
      },
      "CABLE_CONTROL": {
        "CPFC": "EXTERNAL",
        "bEXT_REPL": true
      },
      "INITIAL_CONTROL": {
        "bCONV": true,
        "bTRUSS": true,
        "bBEAM": true,
        "bCHANGE_CABLE": true,
        "bAPPLY_IMF": true
      },
      "INITIAL_DISP": {
        "ITD_CONTROL": {
          "OPT_USE": true,
          "ITD": "GROUP",
          "GROUP": "Erected Structure Group",
          "LFFC_OPT_USE": true,
          "LFFGR": "Lack of Fit Group"
        },
        "bCAMBER": true
      },
      "STRESS_DECREASE": {
        "OPT_USE": true,
        "iSDOPT": 1,
        "SDCONST": 1
      },
      "iBSC": 1,
      "FRAME_OUTPUT": {
        "bCALC_CFF": true,
        "bCALC_CSP": true,
        "bSELFCONS": true
      },
      "bSAVE_OCS": true,
      "NONL_CONTROL": {
        "iLSTEP": 10,
        "INTOUT": "EVERY",
        "ADVANCED": {
          "USE_DEF_SETTINGS": false,
          "STIFF_UPD_SCHEME": 0,
          "ITER_BEF_UPDATE": 3,
          "TERMINATE_ON_FAIL_CONV": true,
          "MAX_ITER_INCREMENT": 30,
          "MAX_BISECT_LEVEL": 5,
          "SMART_BISECT": true,
          "DIVERG_THRESH": 10,
          "ENABLE_LINE_SEARCH": true,
          "LINE_SEARCH": {
            "OPT_USE": true,
            "LINE_SEARCH_TYPE": "USER",
            "MAX_LN_SRCH_ITER": 5,
            "LN_SEARCH_TOL": 0.8
          }
        },
        "DISP": { "OPT_USE": true, "VALUE": 0.001 },
        "LOAD": { "OPT_USE": true, "VALUE": 0.001 },
        "WORK": { "OPT_USE": true, "VALUE": 0.000001 }
      }
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def update_construction_stage_control_m1():
    payload = {
        "Assign": {
            "1": {
                "bLAST_FINAL": True,
                "ANAL_TYPE": {
                    "iINC_NLA": 0,       # 선형
                    "iNLA_TYPE": 1,      # 누가 단계
                    "bINC_PDL": True,
                    "bINC_TDE": True     # 시간의존효과
                },
                "ERECTION_LOAD": [
                    {"LTYPECC": "Erection Dead Load", "EREC": "D",
                     "vLCNAME": ["Self Weight", "Deck Concrete"]}
                ],
                "TIME_DEP_CONTROL": {
                    "CREEP_SHRINKAGE": {
                        "OPT_USE": True,
                        "TYPE": "BOTH",
                        "bOUCC": False,
                        "INTERNAL_STEP": {"OPT_USE": True, "iITS": 5},
                        "AUTO_TIME_STEP": {
                            "OPT_USE": True,
                            "iT10": 2, "iT100": 5, "iT1K": 10,
                            "iT5K": 20, "iT10K": 30
                        },
                        "bTTLE_CS": True,
                        "bRCE": True
                    },
                    "bVAR": True,
                    "bAPPLY_ELA": True,
                    "bTTLE_ES": True,
                    "iTTLE_ES": 0
                },
                "CABLE_CONTROL": {"CPFC": "EXTERNAL", "bEXT_REPL": True},
                "INITIAL_CONTROL": {
                    "bCONV": True, "bTRUSS": True, "bBEAM": True,
                    "bCHANGE_CABLE": True, "bAPPLY_IMF": True
                },
                "iBSC": 1,               # Change with Tendon
                "FRAME_OUTPUT": {
                    "bCALC_CFF": True,
                    "bCALC_CSP": True,
                    "bSELFCONS": True
                },
                "bSAVE_OCS": True,
                "NONL_CONTROL": {        # iINC_NLA != 0 일 때 사용 (레거시 NLCT/NLCT-M1 대응)
                    "iLSTEP": 10,
                    "INTOUT": "EVERY",
                    "ADVANCED": {
                        "USE_DEF_SETTINGS": False,
                        "STIFF_UPD_SCHEME": 0,       # Custom
                        "ITER_BEF_UPDATE": 3,
                        "TERMINATE_ON_FAIL_CONV": True,
                        "MAX_ITER_INCREMENT": 30,
                        "MAX_BISECT_LEVEL": 5,
                        "SMART_BISECT": True,
                        "DIVERG_THRESH": 10,
                        "ENABLE_LINE_SEARCH": True,
                        "LINE_SEARCH": {
                            "OPT_USE": True,
                            "LINE_SEARCH_TYPE": "USER",
                            "MAX_LN_SRCH_ITER": 5,
                            "LN_SEARCH_TOL": 0.8
                        }
                    },
                    "DISP": {"OPT_USE": True, "VALUE": 0.001},
                    "LOAD": {"OPT_USE": True, "VALUE": 0.001},
                    "WORK": {"OPT_USE": True, "VALUE": 0.000001}
                }
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/STCT-M1/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Construction Stage Control (Hyper-S) updated:", resp.json())

update_construction_stage_control_m1()
```

---

## 19. /db/BCCT — Boundary Change Assignment

경계 변경(Boundary Change) 할당 데이터를 정의합니다. 어떤 경계 데이터 종류(지점/스프링/링크/강성계수/단부해제 등)를 변경 대상으로 할지 선택하고, 경계 그룹 조합(`vBOUNDARY`)과 해석/하중케이스별 적용(`vLOADANAL`)을 지정합니다.

> `bWSSF`, `bESSF` 등 일부 항목은 Civil NX 또는 Gen NX 전용일 수 있습니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/BCCT` | 생성 |
| GET | `{base_url}/db/BCCT` | 조회 |
| PUT | `{base_url}/db/BCCT/{id}` | 수정 |
| DELETE | `{base_url}/db/BCCT/{id}` | 삭제 |

### Parameters — 데이터 선택 플래그

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Support | `"bSPT"` | Boolean | false | Optional |
| 2 | Point Spring Support | `"bSPR"` | Boolean | false | Optional |
| 3 | General Spring Support | `"bGSPR"` | Boolean | false | Optional |
| 4 | Change General Link Property | `"bCGLINK"` | Boolean | false | Optional |
| 5 | Section Stiffness Scale Factor | `"bSSSF"` | Boolean | false | Optional |
| 6 | Plate Stiffness Scale Factor | `"bPSSF"` | Boolean | false | Optional |
| 7 | Beam End Release | `"bRLS"` | Boolean | false | Optional |
| 8 | Wall Stiffness Scale Factor | `"bWSSF"` | Boolean | false | Optional |
| 9 | Element Stiffness Scale Factor | `"bESSF"` | Boolean | false | Optional |
| 12 | Constrain DOF associated with specified displacements / settlements by boundary group combinations | `"bCDOF"` | Boolean | false | Optional |

### Parameters — Boundary List (`vBOUNDARY`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 10 | Boundary List | `"vBOUNDARY"` | Array [Object] | - | Required |
| (1) | Boundary Group Combination Name | `"BGCNAME"` | String | - | Required |
| (2) | Boundary Group List | `"vBG"` | Array [String] | - | Required |

### Parameters — Load Cases & Analysis List (`vLOADANAL`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 11 | Load Cases & Analysis List | `"vLOADANAL"` | Array [Object] | - | Optional |
| (1) | Load Cases & Analysis Type | `"TYPE"` | String | - | Required |
| (2) | Boundary Group Combination Name | `"BGCNAME"` | String | - | Required |
| (3) | Static Load Case | `"LCNAME"` | String | - | Required |

**`vLOADANAL.TYPE` 값:**

| Value | Description |
|-------|-------------|
| `"ST"` | Static Load Case |
| `"ULAT"` | Unlisted Analysis Types |
| `"THRSEV"` | TH / RS Analysis / Eigenvalue |
| `"THNS"` | TH Nonlinear Static Analysis |
| `"PO"` | Pushover Analysis |
| `"MV"` | Moving Load Analysis |
| `"SM"` | Settlements Analysis |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "bSPT": true,
      "bSPR": true,
      "bGSPR": false,
      "bCGLINK": false,
      "bSSSF": true,
      "bPSSF": false,
      "bRLS": true,
      "bCDOF": false,
      "vBOUNDARY": [
        { "BGCNAME": "BGL1", "vBG": ["BG1", "BG2"] }
      ],
      "vLOADANAL": [
        { "TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC1" },
        { "TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC2" },
        { "TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC3" },
        { "TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC4" }
      ]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_boundary_change():
    payload = {
        "Assign": {
            "1": {
                "bSPT": True,      # 지점
                "bSPR": True,      # 점 스프링
                "bGSPR": False,
                "bCGLINK": False,
                "bSSSF": True,     # 단면강성 스케일계수
                "bPSSF": False,
                "bRLS": True,      # 보 단부해제
                "bCDOF": False,
                "vBOUNDARY": [
                    {"BGCNAME": "BGL1", "vBG": ["BG1", "BG2"]}
                ],
                "vLOADANAL": [
                    {"TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC1"},
                    {"TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC2"}
                ]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/BCCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Boundary Change Assignment set:", resp.json())

set_boundary_change()
```

---

## 20. /db/BCGD-M1 — Define Boundary Combination (Hyper-S)

Hyper-S(MEC) 솔버용 경계 그룹 조합(Boundary Group Combination)을 정의합니다. 조합 이름과 포함할 경계 그룹 목록을 지정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/BCGD-M1` | 경계 조합 생성 |
| GET | `{base_url}/db/BCGD-M1` | 조회 |
| PUT | `{base_url}/db/BCGD-M1/{id}` | 수정 |
| DELETE | `{base_url}/db/BCGD-M1/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Boundary Combination Name (1~20자, 모델 내 유일) | `"BCG_NAME"` | String | - | Required |
| 2 | Boundary Group List (선택한 경계 그룹 이름 배열, 중복 자동 제거) | `"GROUP_LIST"` | Array [String] | - | Required |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "BCG_NAME": "Support_BCG",
      "GROUP_LIST": ["Fixed_Support", "Elastic_Link"]
    },
    "2": {
      "BCG_NAME": "Stage_BCG",
      "GROUP_LIST": ["Stage1_Boundary", "Stage2_Boundary", "Stage3_Boundary"]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def define_boundary_combination():
    payload = {
        "Assign": {
            "1": {
                "BCG_NAME": "Support_BCG",   # 조합 이름 (1~20자)
                "GROUP_LIST": ["Fixed_Support", "Elastic_Link"]
            },
            "2": {
                "BCG_NAME": "Stage_BCG",
                "GROUP_LIST": ["Stage1_Boundary", "Stage2_Boundary", "Stage3_Boundary"]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/BCGD-M1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Boundary Combination defined:", resp.json())

define_boundary_combination()
```

---

## 21. /db/BCGA-M1 — Assign Boundary Combination (Hyper-S)

Hyper-S(MEC) 솔버용 경계 조합 할당 데이터입니다. 해석 타입·하중케이스에 경계 조합(BCGD)을 할당하고(`BC_ASSIGN`), 적용할 경계 변경 항목(`BC_SELECT`)을 지정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/BCGA-M1` | 경계 조합 할당 생성 |
| GET | `{base_url}/db/BCGA-M1` | 조회 |
| PUT | `{base_url}/db/BCGA-M1/{id}` | 수정 |
| DELETE | `{base_url}/db/BCGA-M1/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Assign Boundary Combination to Analyses & Load Cases | `"BC_ASSIGN"` | Array [Object] | - | Required |
| (1) | Analysis Type | `"ANAL_TYPE"` | String (enum) | - | Required |
| (2) | Load Case Name (ANAL_TYPE ∈ {ST, NLTH, PO}일 때 필수) | `"LCNAME"` | String | - | Conditional |
| (3) | Boundary Group Combination Name (빈 문자열 = 변경 없음) | `"BGCNAME"` | String | "" | Optional |
| 2 | Apply to Boundary Change | `"BC_SELECT"` | Array [String (enum)] | - | Required |

**`BC_ASSIGN.ANAL_TYPE` 값 (enum):**

| Value | Description |
|-------|-------------|
| `"ST"` | Static |
| `"MV"` | Moving Load |
| `"SM"` | Settlement |
| `"EIGV"` | Eigenvalue |
| `"RS"` | Response Spectrum |
| `"LTH"` | Linear Time History |
| `"NLTH"` | Nonlinear Time History |
| `"PO"` | Pushover |

> **조건부 필수**: `ANAL_TYPE`이 `ST`, `NLTH`, `PO`이면 `LCNAME`이 필수입니다. 그 외 해석 타입은 단일 집합 해석이므로 `LCNAME`이 불필요합니다.

**`BC_SELECT` 값 (enum) — 적용할 경계 변경 항목:**

| Value | Description | Value | Description |
|-------|-------------|-------|-------------|
| `"SECF"` | Section Stiffness Scale Factor | `"ESSF"` | Element Stiffness Scale Factor |
| `"EWSF"` | (Element) Wall Stiffness Scale Factor | `"PSSF"` | Plate Stiffness Scale Factor |
| `"WSSF"` | Wall Stiffness Scale Factor | `"CONS"` | Constraint |
| `"NSPR"` | Point (Nodal) Spring Support | `"GSPR"` | General Spring Support |
| `"SSPS"` | Surface Spring Support | `"ELNK"` | Elastic Link |
| `"RIGD"` | Rigid Link | `"NLNK"` | Nonlinear Link |
| `"CGLP"` | Change General Link Property | `"FRLS"` | Frame (Beam) End Release |
| `"OFFS"` | Beam Offset | `"PRLS"` | Plate End Release |
| `"MCON"` | Multi-Constraint | | |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "BC_ASSIGN": [
        { "ANAL_TYPE": "ST", "LCNAME": "DL", "BGCNAME": "Support_BCG" },
        { "ANAL_TYPE": "ST", "LCNAME": "LL", "BGCNAME": "Support_BCG" },
        { "ANAL_TYPE": "EIGV", "BGCNAME": "Stage_BCG" }
      ],
      "BC_SELECT": ["SECF", "NSPR", "ELNK", "FRLS"]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def assign_boundary_combination():
    payload = {
        "Assign": {
            "1": {
                "BC_ASSIGN": [
                    # Static 해석: LCNAME 필수
                    {"ANAL_TYPE": "ST", "LCNAME": "DL", "BGCNAME": "Support_BCG"},
                    {"ANAL_TYPE": "ST", "LCNAME": "LL", "BGCNAME": "Support_BCG"},
                    # Eigenvalue: LCNAME 불필요
                    {"ANAL_TYPE": "EIGV", "BGCNAME": "Stage_BCG"}
                ],
                # 적용할 경계 변경 항목
                "BC_SELECT": ["SECF", "NSPR", "ELNK", "FRLS"]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/BCGA-M1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Boundary Combination assigned:", resp.json())

assign_boundary_combination()
```

---

## End-to-End 워크플로우 예제

해석 제어 데이터 설정 전체 흐름: **ACTL → EIGV → PDEL → BUCK → MVCT → NLCT → STCT → BCCT**

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def post(endpoint, payload):
    resp = requests.post(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print(f"[OK] POST {endpoint}")
    return resp.json()

# Step 1: 메인 제어 데이터
post("/db/ACTL", {"Assign": {
    "1": {"ARDC": True, "ANRC": True, "ITER": 20, "TOL": 0.001,
          "CSECF": False, "TRS": True, "CRBAR": False,
          "BMSTRESS": False, "CLATS": False}
}})

# Step 2: 고유치 해석 (Lanczos)
post("/db/EIGV", {"Assign": {
    "1": {"TYPE": "LANCZOS", "iFREQ": 30, "bMINMAX": False,
          "FRMIN": 0, "FRMAX": 0, "bSTRUM": True}
}})

# Step 3: P-Delta 해석
post("/db/PDEL", {"Assign": {
    "1": {"ITER": 5, "TOL": 1e-05,
          "PDEL_CASES": [{"LCNAME": "DL", "FACTOR": 1.0}]}
}})

# Step 4: 좌굴 해석
post("/db/BUCK", {"Assign": {
    "1": {"MODE_NUM": 5, "OPT_POSITIVE": True,
          "OPT_CONSIDER_AXIAL_ONLY": True,
          "LOAD_FACTOR_FROM": 0, "LOAD_FACTOR_TO": 0,
          "OPT_STURM_SEQ": True,
          "ITEMS": [{"LCNAME": "DL", "FACTOR": 1, "LOAD_TYPE": 1}]}
}})

# Step 5: 이동하중 해석 제어
post("/db/MVCT", {"Assign": {
    "1": {"METHOD": "EXACT", "POINT": "INF", "iIGP": 0, "iIGPN": 3,
          "PLATE": "NODAL", "bSTRCALC": True, "bCONCURRENT": True,
          "bCONCLINK": True, "FRAME": "AXIAL", "bCSTRCALC": True,
          "bREAC": True, "bRG": False, "RGN": "",
          "bDISP": True, "bDG": False, "DGN": "",
          "bFM": True, "bFG": False, "FGN": "",
          "bL": True, "bLG": False, "LGN": ""}
}})

# Step 6: 비선형 해석 제어 (Newton-Raphson)
post("/db/NLCT", {"Assign": {
    "1": {"NONLINEAR_TYPE": "GEOM+MATL", "ITERATION_METHOD": "NEWTON",
          "NUMBER_STEPS": 1, "MAX_ITERATIONS": 30,
          "OPT_ENERGY_NORM": True, "ENERGY_NORM": 0.001,
          "OPT_DISPLACEMENT_NORM": True, "DISPLACEMENT_NORM": 0.001,
          "OPT_FORCE_NORM": True, "FORCE_NORM": 0.001,
          "NEWTON_ITEMS": [{"ITERATION_METHOD": "NEWTON", "LCNAME": "DL",
                            "NUMBER_STEPS": 1, "MAX_ITERATIONS": 30,
                            "LOAD_FACTORS": [1]}]}
}})

# Step 7: 시공단계 해석 제어 (선형, 누가)
post("/db/STCT", {"Assign": {
    "1": {"bLAST_FINAL": True, "iINC_NLA": 0, "iNLA_TYPE": 1,
          "bINC_PDL": True, "iITER": 30, "TOL": 0.01,
          "bINC_TDE": True, "bCNS": True, "TYPE": "BOTH",
          "iITER_CR": 5, "TOL_CR": 0.01, "CPFC": "INTERNAL"}
}})

# Step 8: 경계 변경 할당
post("/db/BCCT", {"Assign": {
    "1": {"bSPT": True, "bSPR": True, "bSSSF": True, "bRLS": True,
          "vBOUNDARY": [{"BGCNAME": "BGL1", "vBG": ["BG1", "BG2"]}],
          "vLOADANAL": [{"TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "DL"}]}
}})

print("\nAll Analysis Control settings applied successfully.")
```

---

*다음 파트: [13_DB_Load_Combinations.md](13_DB_Load_Combinations.md)*
