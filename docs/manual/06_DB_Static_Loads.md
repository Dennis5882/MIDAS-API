# DB – Static Loads

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:** `https://moa-engineers.midasit.com:443/gen`  
> **인증:** 모든 요청에 `MAPI-Key: <key>` 헤더 필수  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

---

## 목차

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | [/db/STLD](#1-dbstld--static-load-cases) | Static Load Cases |
| 2 | [/db/BODF](#2-dbbodf--self-weight) | Self-Weight |
| 3 | [/db/CNLD](#3-dbcnld--nodal-loads) | Nodal Loads |
| 4 | [/db/BMLD](#4-dbbmld--beam-loads) | Beam Loads |
| 5 | [/db/SDSP](#5-dbsdsp--specified-displacements-of-support) | Specified Displacements of Support |
| 6 | [/db/NMAS](#6-dbnmas--nodal-masses) | Nodal Masses |
| 7 | [/db/LTOM](#7-dbltom--loads-to-masses) | Loads to Masses |
| 8 | [/db/NBOF](#8-dbnbof--nodal-body-force) | Nodal Body Force |
| 9 | [/db/PSLT](#9-dbpslt--define-pressure-load-type) | Define Pressure Load Type |
| 10 | [/db/PRES](#10-dbpres--assign-pressure-loads) | Assign Pressure Loads |
| 11 | [/db/PNLD](#11-dbpnld--define-plane-load-type) | Define Plane Load Type |
| 12 | [/db/PNLA](#12-dbpnla--assign-plane-loads) | Assign Plane Loads |
| 13 | [/db/FBLD](#13-dbfbld--define-floor-load-type) | Define Floor Load Type |
| 14 | [/db/FBLA](#14-dbfbla--assign-floor-loads) | Assign Floor Loads |
| 15 | [/db/FMLD](#15-dbfmld--finishing-material-loads) | Finishing Material Loads |
| 16 | [/db/POSP](#16-dbposp--parameter-of-soil-properties) | Parameter of Soil Properties |
| 17 | [/db/EPST](#17-dbepst--static-earth-pressure) | Static Earth Pressure |
| 18 | [/db/EPSE](#18-dbepse--seismic-earth-pressure) | Seismic Earth Pressure |
| 19 | [/db/POSL](#19-dbposl--parameter-of-seismic-loads) | Parameter of Seismic Loads |
| 20 | [/db/SWIND](#20-dbswind--static-wind-load) | Static Wind Load (KDS 41-12:2022) |
| 21 | [/db/SSEIS](#21-dbsseis--static-seismic-load) | Static Seismic Load (KDS 41-17-00:2019) |

---

## 공통 Python 헬퍼

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY_HERE"

def midas_api(method: str, endpoint: str, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}
```

---

## 1. /db/STLD — Static Load Cases

> 정적 하중 케이스(Load Case)를 정의합니다. 이후 모든 하중 데이터는 여기서 정의된 `NAME`(load case name)을 참조합니다.

**Input URI:** `{base url}/db/STLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "NAME": "DL",
      "TYPE": "D",
      "DESC": "DeadLoads"
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Ordering Index in GUI | `"NO"` | Integer | - | Read Only |
| 2 | Load Case Name | `"NAME"` | String | - | Required |
| 3 | Load Type ¹⁾ | `"TYPE"` | String | - | Required |
| 4 | Description | `"DESC"` | String | Blank | Optional |

> ¹⁾ Load Type 값 목록 (67종):

| No. | Load Type | Value | No. | Load Type | Value |
|-----|-----------|-------|-----|-----------|-------|
| 1 | User Defined Load | `"USER"` | 2 | Dead Load | `"D"` |
| 3 | Dead Load of Component and Attachments | `"DC"` | 4 | Dead Load of Wearing Surfaces and Utilities | `"DW"` |
| 5 | Down Drag | `"DD"` | 6 | Earth Pressure | `"EP"` |
| 7 | Active Earth Pressure – Native Ground / Non-cohesive | `"EANN"` | 8 | Active Earth Pressure – Native Ground / Cohesive | `"EANC"` |
| 9 | Active Earth Pressure – Made Ground / Non-cohesive | `"EAMN"` | 10 | Active Earth Pressure – Made Ground / Cohesive | `"EAMC"` |
| 11 | Passive Earth Pressure – Native Ground / Non-cohesive | `"EPNN"` | 12 | Passive Earth Pressure – Native Ground / Cohesive | `"EPNC"` |
| 13 | Passive Earth Pressure – Made Ground / Non-cohesive | `"EPMN"` | 14 | Passive Earth Pressure – Made Ground / Cohesive | `"EPMC"` |
| 15 | Horizontal Earth Pressure | `"EH"` | 16 | Vertical Earth Pressure | `"EV"` |
| 17 | Earth Surcharge Load | `"ES"` | 18 | Locked in Erection Stresses | `"EL"` |
| 19 | Live Load Surcharge | `"LS"` | 20 | Trailer or Crawler Induced Surcharge | `"LSC"` |
| 21 | Live Load | `"L"` | 22 | Trailer or Crawler Induced Live Load | `"LC"` |
| 23 | Overload Live Load | `"LP"` | 24 | Live Load Impact | `"IL"` |
| 25 | Overload Live Load Impact | `"ILP"` | 26 | Centrifugal Force | `"CF"` |
| 27 | Braking Load | `"BRK"` | 28 | Longitudinal Force from Live Load | `"BK"` |
| 29 | Crowd Load | `"CRL"` | 30 | Prestress | `"PS"` |
| 31 | Buoyancy | `"B"` | 32 | Ground Water Pressure | `"WP"` |
| 33 | Fluid Pressure | `"FP"` | 34 | Stream Flow Pressure | `"SF"` |
| 35 | Wave Pressure | `"WPR"` | 36 | Wind Load on Structure | `"W"` |
| 37 | Wind Load on Live Load | `"WL"` | 38 | Settlement | `"STL"` |
| 39 | Creep | `"CR"` | 40 | Shrinkage | `"SH"` |
| 41 | Temperature | `"T"` | 42 | Temperature Gradient | `"TPG"` |
| 43 | Collision Load | `"CO"` | 44 | Vehicular Collision Force | `"CT"` |
| 45 | Vessel Collision Force | `"CV"` | 46 | Earthquake | `"E"` |
| 47 | Friction | `"FR"` | 48 | Ice Pressure | `"IP"` |
| 49 | Construction Stage Load | `"CS"` | 50 | Erection Load | `"ER"` |
| 51 | Rib Shortening | `"RS"` | 52 | Grade Effect | `"GE"` |
| 53 | Roof Live Load | `"LR"` | 54 | Snow Load | `"S"` |
| 55 | Rain Load | `"R"` | 56 | Longitudinal Force | `"LF"` |
| 57 | Raking Force | `"RF"` | 58 | Movement of Foundation | `"GD"` |
| 59 | Soil Heaving | `"SHV"` | 60 | Derailment Load | `"DRL"` |
| 61 | Across Wind Load | `"WA"` | 62 | Torsional Wind Load | `"WT"` |
| 63 | Vertical Earthquake | `"EVT"` | 64 | Earthquake Earth Pressure | `"EEP"` |
| 65 | Explosion Load | `"EX"` | 66 | Imperfection Load | `"I"` |
| 67 | Earthquake for Elastic | `"EE"` | | | |

### Python 예제

```python
# 정적 하중 케이스 생성 (POST)
stld_data = {
    "Assign": {
        "1": {"NAME": "DL",   "TYPE": "D",   "DESC": "Dead Load"},
        "2": {"NAME": "LL",   "TYPE": "L",   "DESC": "Live Load"},
        "3": {"NAME": "WX",   "TYPE": "W",   "DESC": "Wind Load X"},
        "4": {"NAME": "EX",   "TYPE": "E",   "DESC": "Earthquake X"},
        "5": {"NAME": "PS",   "TYPE": "PS",  "DESC": "Prestress"},
    }
}
result = midas_api("POST", "/db/STLD", stld_data)

# 전체 조회 (GET)
all_cases = midas_api("GET", "/db/STLD")

# 특정 케이스 수정 (PUT)
update_data = {
    "Assign": {
        "2": {"NAME": "LL",   "TYPE": "L",   "DESC": "Live Load (Revised)"}
    }
}
midas_api("PUT", "/db/STLD", update_data)

# 특정 케이스 삭제 (DELETE)
midas_api("DELETE", "/db/STLD", {"Assign": {"5": {}}})
```

---

## 2. /db/BODF — Self-Weight

> 자중(Self-Weight)을 지정된 하중 케이스에 적용합니다. `FV` 배열은 [X, Y, Z] 방향 자중 계수이며, 보통 `[0, 0, -1]`을 사용합니다.

**Input URI:** `{base url}/db/BODF`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "2": {
      "LCNAME": "D",
      "GROUP_NAME": "",
      "FV": [0, 0, -1]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | - | Required |
| 2 | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| 3 | Self-Weight Factor [X, Y, Z] | `"FV"` | Array \[Number, 3\] | - | Required |

### Python 예제

```python
# 자중 적용 (POST) — 구조그룹 없음, -Z 방향 전체 자중
bodf_data = {
    "Assign": {
        "1": {
            "LCNAME": "DL",      # 하중 케이스명 (STLD에서 정의)
            "GROUP_NAME": "",    # 구조그룹 없음 (전체 구조물)
            "FV": [0, 0, -1]     # X=0, Y=0, Z=-1 (중력 방향)
        }
    }
}
result = midas_api("POST", "/db/BODF", bodf_data)

# 조회
all_bodf = midas_api("GET", "/db/BODF")

# 수정 — 특정 구조그룹에만 적용
update_data = {
    "Assign": {
        "1": {
            "LCNAME": "DL",
            "GROUP_NAME": "MainStructure",
            "FV": [0, 0, -1]
        }
    }
}
midas_api("PUT", "/db/BODF", update_data)

# 삭제
midas_api("DELETE", "/db/BODF", {"Assign": {"1": {}}})
```

---

## 3. /db/CNLD — Nodal Loads

> 노드에 집중 힘/모멘트를 직접 부가합니다. 키(key)는 **노드 번호**입니다.

**Input URI:** `{base url}/db/CNLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "8": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "D",
          "GROUP_NAME": "",
          "FX": 10,
          "FY": 20,
          "FZ": 30,
          "MX": -40,
          "MY": -50,
          "MZ": -60
        }
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Nodal Load items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Nodal Load – FX | `"FX"` | Number | 0 | Optional |
| (5) | Nodal Load – FY | `"FY"` | Number | 0 | Optional |
| (6) | Nodal Load – FZ | `"FZ"` | Number | 0 | Optional |
| (7) | Nodal Load – MX | `"MX"` | Number | 0 | Optional |
| (8) | Nodal Load – MY | `"MY"` | Number | 0 | Optional |
| (9) | Nodal Load – MZ | `"MZ"` | Number | 0 | Optional |

### Python 예제

```python
# 노드 집중하중 부가 (POST)
# 키 = 노드 번호, ITEMS 배열로 여러 하중 케이스 동시 입력 가능
cnld_data = {
    "Assign": {
        "8": {   # 노드 8번
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "LL",   # 활하중 케이스
                    "GROUP_NAME": "",
                    "FX": 0.0,
                    "FY": 0.0,
                    "FZ": -50.0,      # 50 kN (downward)
                    "MX": 0.0,
                    "MY": 0.0,
                    "MZ": 0.0
                }
            ]
        },
        "12": {   # 노드 12번
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "WX",
                    "GROUP_NAME": "",
                    "FX": 100.0,      # X방향 풍하중
                    "FY": 0.0,
                    "FZ": 0.0,
                    "MX": 0.0,
                    "MY": 0.0,
                    "MZ": 0.0
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/CNLD", cnld_data)

# 조회
all_cnld = midas_api("GET", "/db/CNLD")

# 삭제 (노드 8번의 집중하중 삭제)
midas_api("DELETE", "/db/CNLD", {"Assign": {"8": {}}})
```

---

## 4. /db/BMLD — Beam Loads

> 보 요소에 분포하중·집중하중·압력하중 등을 부가합니다. 키(key)는 **요소 번호**입니다.

**Input URI:** `{base url}/db/BMLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조 (균일 분포하중 예시)

```json
{
  "Assign": {
    "115": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "L",
          "GROUP_NAME": "",
          "CMD": "BEAM",
          "TYPE": "UNILOAD",
          "DIRECTION": "GZ",
          "USE_PROJECTION": false,
          "USE_ECCEN": false,
          "D": [0, 1, 0, 0],
          "P": [-50, -50, 0, 0]
        }
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Beam Load items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Load Classification (`"BEAM"` / `"LINE"` / `"TYPICAL"`) | `"CMD"` | String | - | Required |
| (5) | Load Type (`"CONLOAD"` / `"CONMOMENT"` / `"UNILOAD"` / `"UNIMOMENT"` / `"PRESSURE"`) | `"TYPE"` | String | - | Required |
| (6) | Direction (`"LX"` / `"LY"` / `"LZ"` / `"GX"` / `"GY"` / `"GZ"`) | `"DIRECTION"` | String | - | Required |
| (7) | Projection | `"USE_PROJECTION"` | Boolean | false | Optional |
| (8) | Distance [x1, x2, x3, x4] | `"D"` | Array \[Number, 4\] | 0 | Optional |
| (9) | Load [v1, v2, v3, v4] | `"P"` | Array \[Number, 4\] | 0 | Optional |
| (10) | Eccentricity | `"USE_ECCEN"` | Boolean | false | Optional |
| (11) | Eccentricity Type (0=Centroid, 1=Offset) | `"ECCEN_TYPE"` | Integer | 0 | Optional |
| (12) | Eccentricity Direction (`"LY"` / `"LZ"` / `"GX"` / `"GY"` / `"GZ"`) | `"ECCEN_DIR"` | String | - | Required |
| (13) | Distance I-End | `"I_END"` | Number | 0 | Optional |
| (14) | J-End Option | `"USE_J_END"` | Boolean | false | Optional |
| (15) | Distance J-End | `"J_END"` | Number | 0 | Optional |
| (16) | Additional H from Top Option | `"USE_ADDITIONAL"` | Boolean | false | Optional |
| (17) | Distance I-End (additional) | `"ADDITIONAL_I_END"` | Number | 0 | Optional |
| (18) | J-End Option (additional) | `"USE_ADDITIONAL_J_END"` | Boolean | false | Optional |
| (19) | Distance J-End (additional) | `"ADDITIONAL_J_END"` | Number | 0 | Optional |

### Python 예제

```python
# 보 하중 부가 (POST) — 균일 분포하중과 집중하중
bmld_data = {
    "Assign": {
        "115": {   # 요소 115번
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "LL",
                    "GROUP_NAME": "",
                    "CMD": "BEAM",           # 일반 보 요소
                    "TYPE": "UNILOAD",       # 균일 분포하중
                    "DIRECTION": "GZ",       # 전체 좌표계 Z방향
                    "USE_PROJECTION": False,
                    "USE_ECCEN": False,
                    "D": [0, 1, 0, 0],       # 전 길이 구간 [0~1 (비율)]
                    "P": [-30.0, -30.0, 0, 0]  # -30 kN/m 균일
                }
            ]
        },
        "120": {   # 요소 120번 — 집중하중
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "LL",
                    "GROUP_NAME": "",
                    "CMD": "BEAM",
                    "TYPE": "CONLOAD",       # 집중하중
                    "DIRECTION": "GZ",
                    "USE_PROJECTION": False,
                    "USE_ECCEN": False,
                    "D": [0.5, 0, 0, 0],    # 요소 중간 지점 (비율 0.5)
                    "P": [-100.0, 0, 0, 0]  # -100 kN
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/BMLD", bmld_data)

# 조회
all_bmld = midas_api("GET", "/db/BMLD")

# 삭제
midas_api("DELETE", "/db/BMLD", {"Assign": {"115": {}}})
```

---

## 5. /db/SDSP — Specified Displacements of Support

> 지점 강제 변위(Settlement/Prescribed displacement)를 정의합니다. 키(key)는 **노드 번호**입니다.

**Input URI:** `{base url}/db/SDSP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "10": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "LL",
          "GROUP_NAME": "",
          "VALUES": [
            {"OPT_FLAG": true, "DISPLACEMENT": 1.5},
            {"OPT_FLAG": true, "DISPLACEMENT": 1.5},
            {"OPT_FLAG": true, "DISPLACEMENT": 1.5},
            {"OPT_FLAG": true, "DISPLACEMENT": 1.5},
            {"OPT_FLAG": true, "DISPLACEMENT": 0.5},
            {"OPT_FLAG": true, "DISPLACEMENT": 0.5}
          ]
        }
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Specified Displacement items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Displacements (Local) [Dx, Dy, Dz, Rx, Ry, Rz] | `"VALUES"` | Array \[Object, 6\] | Blank | Optional |
| i. | Usage Flag | `"OPT_FLAG"` | Boolean | false | Optional |
| ii. | Displacement Value | `"DISPLACEMENT"` | Real | 0 | Optional |

### Python 예제

```python
# 지점 강제 변위 부가 (POST)
# VALUES 배열: 6개 요소 = [Dx, Dy, Dz, Rx, Ry, Rz]
sdsp_data = {
    "Assign": {
        "10": {   # 노드 10번
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "STL",        # 침하 하중 케이스
                    "GROUP_NAME": "",
                    "VALUES": [
                        {"OPT_FLAG": True,  "DISPLACEMENT": -0.025},  # Dx = -25mm
                        {"OPT_FLAG": False, "DISPLACEMENT": 0.0},      # Dy (미사용)
                        {"OPT_FLAG": True,  "DISPLACEMENT": -0.050},  # Dz = -50mm
                        {"OPT_FLAG": False, "DISPLACEMENT": 0.0},      # Rx (미사용)
                        {"OPT_FLAG": False, "DISPLACEMENT": 0.0},      # Ry (미사용)
                        {"OPT_FLAG": False, "DISPLACEMENT": 0.0},      # Rz (미사용)
                    ]
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/SDSP", sdsp_data)

# 조회
all_sdsp = midas_api("GET", "/db/SDSP")

# 삭제
midas_api("DELETE", "/db/SDSP", {"Assign": {"10": {}}})
```

---

## 6. /db/NMAS — Nodal Masses

> 노드에 집중 질량을 정의합니다. 키(key)는 **노드 번호**입니다.

**Input URI:** `{base url}/db/NMAS`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "mX": 1,
      "mY": 2,
      "mZ": 3,
      "rmX": 4,
      "rmY": 5,
      "rmZ": 6
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Translational Mass – GCS X | `"mX"` | Number | - | Required |
| 2 | Translational Mass – GCS Y | `"mY"` | Number | 0 | Optional |
| 3 | Translational Mass – GCS Z | `"mZ"` | Number | 0 | Optional |
| 4 | Rotational Mass Moment of Inertia – X-axis | `"rmX"` | Number | 0 | Optional |
| 5 | Rotational Mass Moment of Inertia – Y-axis | `"rmY"` | Number | 0 | Optional |
| 6 | Rotational Mass Moment of Inertia – Z-axis | `"rmZ"` | Number | 0 | Optional |

### Python 예제

```python
# 노드 질량 정의 (POST)
nmas_data = {
    "Assign": {
        "1":  {"mX": 500.0, "mY": 500.0, "mZ": 500.0, "rmX": 0.0, "rmY": 0.0, "rmZ": 0.0},
        "5":  {"mX": 750.0, "mY": 750.0, "mZ": 750.0, "rmX": 0.0, "rmY": 0.0, "rmZ": 0.0},
        "10": {"mX": 1000.0, "mY": 1000.0, "mZ": 1000.0,
               "rmX": 250.0, "rmY": 250.0, "rmZ": 500.0},
    }
}
result = midas_api("POST", "/db/NMAS", nmas_data)

# 조회
all_nmas = midas_api("GET", "/db/NMAS")

# 삭제
midas_api("DELETE", "/db/NMAS", {"Assign": {"5": {}}})
```

---

## 7. /db/LTOM — Loads to Masses

> 기존 하중 케이스의 하중을 질량으로 변환하는 설정입니다.

**Input URI:** `{base url}/db/LTOM`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "DIR": "XYZ",
      "bNODAL": true,
      "bBEAM": true,
      "bFLOOR": true,
      "bPRES": true,
      "GRAV": 9.806,
      "vLC": [
        {"LCNAME": "D",  "FACTOR": 1.0},
        {"LCNAME": "L",  "FACTOR": 0.5}
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Mass Direction (`"X"` / `"Y"` / `"Z"` / `"XY"` / `"YZ"` / `"XZ"` / `"XYZ"`) | `"DIR"` | String | - | Required |
| 2 | Nodal Load | `"bNODAL"` | Boolean | false | Optional |
| 3 | Beam Load | `"bBEAM"` | Boolean | false | Optional |
| 4 | Floor Load | `"bFLOOR"` | Boolean | false | Optional |
| 5 | Pressure (Hydrostatic) | `"bPRES"` | Boolean | false | Optional |
| 6 | Gravity Acceleration | `"GRAV"` | Number | 0 | Optional |
| 7 | Load Case List | `"vLC"` | Array \[Object\] | - | Required |
| (1) | Load Case Name | `"LCNAME"` | String | - | Required |
| (2) | Scale Factor | `"FACTOR"` | Number | - | Required |

### Python 예제

```python
# 하중→질량 변환 설정 (POST)
ltom_data = {
    "Assign": {
        "1": {
            "DIR": "XYZ",        # 3방향 변환
            "bNODAL": True,      # 노드 집중하중 포함
            "bBEAM": True,       # 보 하중 포함
            "bFLOOR": True,      # 바닥 하중 포함
            "bPRES": False,      # 수압 제외
            "GRAV": 9.806,       # 중력 가속도 (m/s²)
            "vLC": [
                {"LCNAME": "DL", "FACTOR": 1.0},   # 사하중 100%
                {"LCNAME": "LL", "FACTOR": 0.25},  # 활하중 25%
            ]
        }
    }
}
result = midas_api("POST", "/db/LTOM", ltom_data)

# 조회
all_ltom = midas_api("GET", "/db/LTOM")

# 삭제
midas_api("DELETE", "/db/LTOM", {"Assign": {"1": {}}})
```

---

## 8. /db/NBOF — Nodal Body Force

> 노드 집중 질량·하중→질량·구조 질량으로부터 관성력(체적력)을 산정·부가합니다.

**Input URI:** `{base url}/db/NBOF`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조 (노드 목록 방식)

```json
{
  "Assign": {
    "1": {
      "LCNAME": "E",
      "OPT_USE_GROUP": false,
      "KEY_NODE_ITEMS": [12, 42, 39, 40, 11, 41],
      "OPT_NODAL_MASS": true,
      "OPT_LOAD_TO_MASS": true,
      "OPT_STRUCT_MASS": true,
      "X": 10,
      "Y": 20,
      "Z": 30
    }
  }
}
```

### 요청 바디 구조 (구조그룹 방식)

```json
{
  "Assign": {
    "2": {
      "LCNAME": "E",
      "OPT_USE_GROUP": true,
      "GROUP_NAME": "CrossBeam",
      "OPT_NODAL_MASS": true,
      "OPT_LOAD_TO_MASS": true,
      "OPT_STRUCT_MASS": true,
      "X": 10,
      "Y": 0,
      "Z": 0
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | - | Required |
| 2 | Nodal Mass | `"OPT_NODAL_MASS"` | Boolean | false | Optional |
| 3 | Load to Mass | `"OPT_LOAD_TO_MASS"` | Boolean | false | Optional |
| 4 | Structure Mass | `"OPT_STRUCT_MASS"` | Boolean | false | Optional |
| 5 | X-dir. Force Factor | `"X"` | Number | - | Required |
| 6 | Y-dir. Force Factor | `"Y"` | Number | 0 | Optional |
| 7 | Z-dir. Force Factor | `"Z"` | Number | 0 | Optional |
| 8 | Structure Group Option | `"OPT_USE_GROUP"` | Boolean | false | Optional |
| **OPT_USE_GROUP = true** | | | | | |
| 9 | Structure Group Name | `"GROUP_NAME"` | String | - | - |
| **OPT_USE_GROUP = false** | | | | | |
| 9 | Node No. List | `"KEY_NODE_ITEMS"` | Array \[Integer\] | - | - |

### Python 예제

```python
# 노드 체적력 부가 (POST)
nbof_data = {
    "Assign": {
        "1": {
            "LCNAME": "EX",              # 지진 하중 케이스
            "OPT_USE_GROUP": False,
            "KEY_NODE_ITEMS": [1, 2, 3, 4, 5],  # 적용 노드 목록
            "OPT_NODAL_MASS": True,
            "OPT_LOAD_TO_MASS": True,
            "OPT_STRUCT_MASS": True,
            "X": 1.0,    # X방향 계수 (지진 가속도 계수)
            "Y": 0.0,
            "Z": 0.0
        }
    }
}
result = midas_api("POST", "/db/NBOF", nbof_data)

# 조회
all_nbof = midas_api("GET", "/db/NBOF")

# 삭제
midas_api("DELETE", "/db/NBOF", {"Assign": {"1": {}}})
```

---

## 9. /db/PSLT — Define Pressure Load Type

> 요소 면/엣지에 가해지는 압력 하중 타입을 정의합니다. 이후 `/db/PRES`로 요소에 할당합니다.

**Input URI:** `{base url}/db/PSLT`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조 (Plate Face – Uniform)

```json
{
  "Assign": {
    "1": {
      "NAME": "PlateUniform",
      "DESC": "Plate/PlaneStress(Face)",
      "ELEM_TYPE": "Plate/PlaneStress(Face)",
      "PRESSURE_LOAD_ITEMS": [
        {"LOADCASENAME": "DC", "LOADTYPE": "Uniform", "LOAD_P1": -20},
        {"LOADCASENAME": "DW", "LOADTYPE": "Linear",
         "LOAD_P1": -1, "LOAD_P2": -2, "LOAD_P3": -3, "LOAD_P4": -4}
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Pressure Load Type Name | `"NAME"` | String | - | Required |
| 2 | Description | `"DESC"` | String | - | Required |
| 3 | Element Type | `"ELEM_TYPE"` | String | - | Required |
| 4 | Pressure Load items | `"PRESSURE_LOAD_ITEMS"` | Array \[Object\] | - | Required |
| (1) | Load Case Name | `"CMD"` | String | 0 | Required |
| (2) | Load Type (`"Uniform"` / `"Linear"`) | `"LOADTYPE"` | String | - | Required |
| (3) | Load P1 ¹⁾ | `"LOAD_P1"` | Number | - | Required |
| (4) | Load P2 ¹⁾ | `"LOAD_P2"` | Number | 0 | Optional |
| (5) | Load P3 ¹⁾ | `"LOAD_P3"` | Number | 0 | Optional |
| (6) | Load P4 ¹⁾ | `"LOAD_P4"` | Number | 0 | Optional |

> ¹⁾ Element Type별 P1~P4 사용 가능 여부 (O=사용, -=미사용):

| Element Type | Load Type | P1 | P2 | P3 | P4 |
|---|---|:---:|:---:|:---:|:---:|
| `"Plate/Plane Stress (Face)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | O | O |
| `"Plate/Plane Stress (Edge)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | - | - |
| `"Solid (Face)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | O | O |
| `"Plane Strain (Edge)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | - | - |
| `"Axisymmetric (Edge)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | - | - |
| `"Wall (Edge)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | - | - |

### Python 예제

```python
# 압력 하중 타입 정의 (POST)
pslt_data = {
    "Assign": {
        "1": {
            "NAME": "WaterPressure",
            "DESC": "Hydrostatic water pressure on wall",
            "ELEM_TYPE": "Plate/PlaneStress(Face)",
            "PRESSURE_LOAD_ITEMS": [
                {
                    "LOADCASENAME": "WP",   # Ground Water Pressure 케이스
                    "LOADTYPE": "Uniform",
                    "LOAD_P1": -25.0        # -25 kN/m²
                }
            ]
        },
        "2": {
            "NAME": "EarthPressureWall",
            "DESC": "Linear earth pressure on retaining wall (edge)",
            "ELEM_TYPE": "Plate/PlaneStress(Edge)",
            "PRESSURE_LOAD_ITEMS": [
                {
                    "LOADCASENAME": "EP",
                    "LOADTYPE": "Linear",
                    "LOAD_P1": 0.0,         # 상단 (top) 압력
                    "LOAD_P2": -40.0        # 하단 (bottom) 압력
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/PSLT", pslt_data)

# 조회
all_pslt = midas_api("GET", "/db/PSLT")

# 삭제
midas_api("DELETE", "/db/PSLT", {"Assign": {"2": {}}})
```

---

## 10. /db/PRES — Assign Pressure Loads

> `/db/PSLT`에서 정의한 압력 하중 타입을 실제 요소에 할당합니다. 키(key)는 **요소 번호**입니다.

**Input URI:** `{base url}/db/PRES`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조 (Plate Face)

```json
{
  "Assign": {
    "116": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Element_Type1",
          "GROUP_NAME": "",
          "CMD": "PRES",
          "ELEM_TYPE": "PLATE",
          "FACE_EDGE_TYPE": "FACE",
          "DIRECTION": "LZ",
          "FORCES": [-10, 0, 0, 0, 0]
        }
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Pressure Load items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Command Type (`"PRES"`) | `"CMD"` | String | `"PRES"` | Optional |
| (5) | Element Type (`"PLATE"` / `"SOLID"` / `"PLANE"`) | `"ELEM_TYPE"` | String | `"PLATE"` | Optional |
| (6) | Pressure Type (`"FACE"` / `"EDGE"` / `"PRES"`) | `"FACE_EDGE_TYPE"` | String | - | Required |
| (7) | Direction (`"NORMAL"` / `"LX"` / `"LY"` / `"LZ"` / `"GX"` / `"GY"` / `"GZ"` / `"VECTOR"`) | `"DIRECTION"` | String | `"NORMAL"` | Optional |
| (8) | Vector [X, Y, Z] (if DIRECTION="VECTOR") | `"VECTORS"` | Array \[Number, 3\] | - | Optional |
| (9) | Projection (GX/GY/GZ only) | `"OPT_PROJECTION"` | Boolean | false | Optional |
| (10) | Face/Edge Number (Solid: 1~6, Plate/Plane: 1~4) | `"EDGE_FACE"` | Integer | - | Required |
| **FACE_EDGE_TYPE = "FACE" or "PRES"** | | | | | |
| (11) | Forces [PU,0,0,0,0] or [0,P1,P2,P3,P4] | `"FORCES"` | Array \[Number, 5\] | - | Required |
| **FACE_EDGE_TYPE = "EDGE"** | | | | | |
| (11) | Edge Loads [EPU,0,0] or [0,EP1,EP2] | `"EDGE_LOADS"` | Array \[Number, 3\] | - | Required |

> Direction 지원 매트릭스:

| ELEM_TYPE | FACE_EDGE_TYPE | NORMAL | LX | LY | LZ | GX | GY | GZ | VECTOR |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `"PLATE"` | `"FACE"` | - | O | O | O | O | O | O | O |
| `"PLATE"` | `"EDGE"` | O | O | O | O | O | O | O | O |
| `"SOLID"` | `"PRES"` | O | O | O | O | O | O | O | O |
| `"PLANE"` | `"EDGE"` | O | O | O | O | - | - | - | O |

### Python 예제

```python
# 압력 하중 할당 (POST)
pres_data = {
    "Assign": {
        "116": {   # 요소 116번 (Plate 요소)
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "WP",
                    "GROUP_NAME": "",
                    "CMD": "PRES",
                    "ELEM_TYPE": "PLATE",
                    "FACE_EDGE_TYPE": "FACE",
                    "DIRECTION": "NORMAL",   # 면 법선 방향
                    "EDGE_FACE": 1,
                    "FORCES": [-25.0, 0, 0, 0, 0]  # 균일 -25 kN/m²
                }
            ]
        },
        "320": {   # Solid 요소
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "EP",
                    "GROUP_NAME": "",
                    "CMD": "PRES",
                    "ELEM_TYPE": "SOLID",
                    "FACE_EDGE_TYPE": "PRES",
                    "DIRECTION": "NORMAL",
                    "EDGE_FACE": 1,          # Face #1
                    "FORCES": [0, -10, -30, -30, -10]  # 선형 압력
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/PRES", pres_data)

# 조회
all_pres = midas_api("GET", "/db/PRES")

# 삭제
midas_api("DELETE", "/db/PRES", {"Assign": {"116": {}}})
```

---

## 11. /db/PNLD — Define Plane Load Type

> 평면 하중 타입(점·선·면)을 정의합니다. 이후 `/db/PNLA`로 요소에 할당합니다.

**Input URI:** `{base url}/db/PNLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조 (Point Load)

```json
{
  "Assign": {
    "1": {
      "NAME": "Point_examples",
      "DESC": "API_example",
      "LTYPE": "POINT",
      "POINTLOAD": [
        {"X": 0, "Y": 0, "F": -10},
        {"X": 1, "Y": -1, "F": 10.5}
      ],
      "COPY_X": [5, 5, 5],
      "COPY_Y": [3, 3]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Type Name | `"NAME"` | String | - | Required |
| 2 | Description | `"DESC"` | String | Blank | Optional |
| 3 | Load Type (`"POINT"` / `"LINE"` / `"AREA"`) | `"LTYPE"` | String | - | Required |
| 4 | Copy in X-Direction | `"COPY_X"` | Array \[Number\] | - | Required |
| 5 | Copy in Y-Direction | `"COPY_Y"` | Array \[Number\] | - | Required |
| 6 | Sequence Number (Unique) | `"SEQ"` | Integer | Auto | Optional |
| **LTYPE = "POINT"** | | | | | |
| 7 | Point Loads | `"POINTLOAD"` | Array \[Object\] | - | Required |
| (1) | Point X | `"X"` | Number | 0 | Optional |
| (2) | Point Y | `"Y"` | Number | 0 | Optional |
| (3) | Force | `"F"` | Number | 0 | Optional |
| **LTYPE = "LINE"** | | | | | |
| 7 | Line Loads | `"LINELOAD"` | Object | - | Required |
| (1) | Uniform (true) / Trapezoidal (false) | `"bUNIFORM"` | Boolean | true | Optional |
| (2) | Coordinates of X1, X2 | `"X"` | Array \[Number, 2\] | 0 | Optional |
| (3) | Coordinates of Y1, Y2 | `"Y"` | Array \[Number, 2\] | 0 | Optional |
| (4) | Force (Uniform: [F1] / Trap: [F1, F2]) | `"F"` | Array \[Number, 2\] | 0 | Optional |
| **LTYPE = "AREA"** | | | | | |
| 7 | Area Loads | `"AREALOAD"` | Object | - | Required |
| (1) | Uniform (true) / Trapezoidal (false) | `"bUNIFORM"` | Boolean | false | Optional |
| (2) | 3 Points (true) / 4 Points (false) | `"b3PNT"` | Boolean | false | Optional |
| (3) | Coordinates X1~X4 | `"X"` | Array \[Number, 4\] | 0 | Optional |
| (4) | Coordinates Y1~Y4 | `"Y"` | Array \[Number, 4\] | 0 | Optional |
| (5) | Load (Uniform: [F1] / Trap: [F1,F2,F3,F4]) | `"LOAD"` | Array \[Number, 4\] | 0 | Optional |

### Python 예제

```python
# 평면 하중 타입 정의 (POST) — 균일 면 하중
pnld_data = {
    "Assign": {
        "1": {
            "NAME": "UniformAreaLoad",
            "DESC": "Uniform load on floor area",
            "LTYPE": "AREA",
            "COPY_X": [0],    # 복사 없음
            "COPY_Y": [0],
            "AREALOAD": {
                "bUNIFORM": True,    # 균일 하중
                "b3PNT": False,      # 4점 정의
                "X": [0, 5, 5, 0],  # 가로 5m
                "Y": [0, 0, 4, 4],  # 세로 4m
                "LOAD": [-5.0, -5.0, -5.0, -5.0]  # -5 kN/m²
            }
        },
        "2": {
            "NAME": "LineLoadOnEdge",
            "DESC": "Line load along beam edge",
            "LTYPE": "LINE",
            "COPY_X": [0],
            "COPY_Y": [0],
            "LINELOAD": {
                "bUNIFORM": True,
                "X": [0, 6],     # X: 0~6m
                "Y": [0, 0],     # Y: 고정
                "F": [-10.0]     # -10 kN/m 균일
            }
        }
    }
}
result = midas_api("POST", "/db/PNLD", pnld_data)

# 조회
all_pnld = midas_api("GET", "/db/PNLD")

# 삭제
midas_api("DELETE", "/db/PNLD", {"Assign": {"2": {}}})
```

---

## 12. /db/PNLA — Assign Plane Loads

> `/db/PNLD`에서 정의한 평면 하중 타입을 실제 요소에 좌표계로 할당합니다.

**Input URI:** `{base url}/db/PNLA`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "LCNAME": "AssignPlaneExample",
      "PNLD_KEY": 1,
      "ELEM_TYPE": "PLATE",
      "POINT_ORIGIN": [18, 2, 0],
      "AXIS_X": [19, 2, 0],
      "AXIS_Y": [19, 3, 0],
      "TOL": 0.0009144,
      "SELECT_TYPE": "ON_PLANE",
      "LOAD_DIR": "GLOBAL_Z",
      "PROJECT_TYPE": "NO"
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | - | Required |
| 2 | Load Group Name | `"LOAD_GROUP"` | String | - | Required |
| 3 | Defined Plane Load Key | `"PNLD_KEY"` | Integer | - | Required |
| 4 | Element Type (`"PLATE"` / `"SOLID"`) | `"ELEM_TYPE"` | String | - | Required |
| 5 | First Point / Origin [x, y, z] | `"POINT_ORIGIN"` | Array \[Number, 3\] | - | Required |
| 6 | Second Point / on x-Axis [x, y, z] | `"AXIS_X"` | Array \[Number, 3\] | - | Required |
| 7 | Third Point / on x-y Plane [x, y, z] | `"AXIS_Y"` | Array \[Number, 3\] | - | Required |
| 8 | Tolerance | `"TOL"` | Number | - | Required |
| 9 | Element Selection (`"ON_PLANE"` / `"IN_GROUP"`) | `"SELECT_TYPE"` | String | - | Required |
| 10 | Load Direction (`"NORMAL_PLANE"` / `"NORMAL_ELEM"` / `"GLOBAL_X"` / `"GLOBAL_Y"` / `"GLOBAL_Z"`) | `"LOAD_DIR"` | String | - | Required |
| 11 | Projection Type (`"NO"` / `"LOAD_DIR"` / `"LOAD_PLANE"`) | `"PROJECT_TYPE"` | String | - | Required |
| 12 | Description | `"DESC"` | String | Blank | Optional |
| **ELEM_TYPE = "PLATE"** | | | | | |
| 13 | Node Defining Loading Area | `"bDEFINE_NODE"` | Boolean | false | Optional |
| 14 | Loading Boundary Connecting Node | `"CONNECT_NODE"` | Array \[Integer, 15\] | - | Optional |
| **SELECT_TYPE = "IN_GROUP"** | | | | | |
| 13 | Element Group Name | `"ELEM_GROUP"` | String | - | Optional |
| **SELECT_TYPE = "SOLID"** | | | | | |
| 14 | Solid Face No. (1~6) | `"FACE_NO"` | Integer | - | Optional |

### Python 예제

```python
# 평면 하중 할당 (POST)
pnla_data = {
    "Assign": {
        "1": {
            "LCNAME": "LL",
            "LOAD_GROUP": "LiveLoadGroup",
            "PNLD_KEY": 1,                   # PNLD에서 정의한 키
            "ELEM_TYPE": "PLATE",
            "POINT_ORIGIN": [0.0, 0.0, 3.0], # 하중 평면 원점
            "AXIS_X":       [1.0, 0.0, 3.0], # x축 방향 정의점
            "AXIS_Y":       [1.0, 1.0, 3.0], # x-y 평면 정의점
            "TOL": 0.001,
            "SELECT_TYPE": "ON_PLANE",
            "LOAD_DIR": "GLOBAL_Z",
            "PROJECT_TYPE": "NO",
            "DESC": "3층 바닥 활하중"
        }
    }
}
result = midas_api("POST", "/db/PNLA", pnla_data)

# 조회
all_pnla = midas_api("GET", "/db/PNLA")

# 삭제
midas_api("DELETE", "/db/PNLA", {"Assign": {"1": {}}})
```

---

## 13. /db/FBLD — Define Floor Load Type

> 바닥 하중 타입(Floor Load Type)을 정의합니다. 하중 케이스별 면하중 값을 담습니다.

**Input URI:** `{base url}/db/FBLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "NAME": "Floor_example",
      "DESC": "",
      "ITEM": [
        {"LCNAME": "DC",  "FLOOR_LOAD": 10, "OPT_SUB_BEAM_WEIGHT": true},
        {"LCNAME": "DW",  "FLOOR_LOAD": 20, "OPT_SUB_BEAM_WEIGHT": true}
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Floor Load Type Name | `"NAME"` | String | - | Required |
| 2 | Description | `"DESC"` | String | Blank | Optional |
| 3 | Floor Load items | `"ITEM"` | Array \[Object\] | - | Required |
| (1) | Load Case Name | `"LCNAME"` | String | - | Required |
| (2) | Floor Load (kN/m² or equivalent) | `"FLOOR_LOAD"` | Number | - | Required |
| (3) | Consider Sub Beam Weight | `"OPT_SUB_BEAM_WEIGHT"` | Boolean | false | Optional |

### Python 예제

```python
# 바닥 하중 타입 정의 (POST)
fbld_data = {
    "Assign": {
        "1": {
            "NAME": "TypicalFloor",
            "DESC": "일반 층 사하중 + 활하중",
            "ITEM": [
                {"LCNAME": "DL", "FLOOR_LOAD": 4.0,  "OPT_SUB_BEAM_WEIGHT": True},
                {"LCNAME": "LL", "FLOOR_LOAD": 2.5,  "OPT_SUB_BEAM_WEIGHT": False},
            ]
        },
        "2": {
            "NAME": "RoofFloor",
            "DESC": "옥상 하중",
            "ITEM": [
                {"LCNAME": "DL", "FLOOR_LOAD": 3.5,  "OPT_SUB_BEAM_WEIGHT": True},
                {"LCNAME": "LL", "FLOOR_LOAD": 1.0,  "OPT_SUB_BEAM_WEIGHT": False},
                {"LCNAME": "S",  "FLOOR_LOAD": 0.5,  "OPT_SUB_BEAM_WEIGHT": False},
            ]
        }
    }
}
result = midas_api("POST", "/db/FBLD", fbld_data)

# 조회
all_fbld = midas_api("GET", "/db/FBLD")

# 삭제
midas_api("DELETE", "/db/FBLD", {"Assign": {"2": {}}})
```

---

## 14. /db/FBLA — Assign Floor Loads

> `/db/FBLD`에서 정의한 바닥 하중 타입을 노드로 구성된 영역에 할당합니다.

**Input URI:** `{base url}/db/FBLA`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조 (One-Way 배분)

```json
{
  "Assign": {
    "1": {
      "FLOOR_LOAD_TYPE_NAME": "Floor_example",
      "FLOOR_DIST_TYPE": 1,
      "LOAD_ANGLE": 0,
      "SUB_BEAM_NUM": 2,
      "SUB_BEAM_ANGLE": 90,
      "UNIT_SELF_WEIGHT": 10,
      "DIR": "GZ",
      "OPT_PROJECTION": false,
      "DESC": "",
      "OPT_EXCLUDE_INNER_ELEM_AREA": true,
      "GROUP_NAME": "LoadGroup2",
      "NODES": [508, 509, 511, 510]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Floor Load Type Name | `"FLOOR_LOAD_TYPE_NAME"` | String | - | Required |
| 2 | Distribution Type (1=One Way / 2=Two Way / 3=Polygon-Centroid / 4=Polygon-Length) | `"FLOOR_DIST_TYPE"` | Integer | - | Required |
| 3 | Load Direction (`"LX"` / `"LY"` / `"LZ"` / `"GX"` / `"GY"` / `"GZ"`) | `"DIR"` | String | `"LX"` | Optional |
| 4 | Projection | `"OPT_PROJECTION"` | Boolean | false | Optional |
| 5 | Description | `"DESC"` | String | Blank | Optional |
| 6 | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| 7 | Nodes defining Loading Area | `"NODES"` | Array \[Integer\] | - | Required |
| **FLOOR_DIST_TYPE = 1** | | | | | |
| 8 | Load Angle (A1) | `"LOAD_ANGLE"` | Number | 0 | Optional |
| **FLOOR_DIST_TYPE = 2** | | | | | |
| 8 | Allow Polygon Type Unit Area | `"OPT_ALLOW_POLYGON_TYPE_UNIT_AREA"` | Boolean | false | Optional |
| **FLOOR_DIST_TYPE = 1 or 2** | | | | | |
| 9 | Exclude Inner Element of Area | `"OPT_EXCLUDE_INNER_ELEM_AREA"` | Boolean | false | Optional |
| 10 | No. of Sub Beams | `"SUB_BEAM_NUM"` | Integer | 0 | Optional |
| 11 | Sub-Beam Angle (A2) | `"SUB_BEAM_ANGLE"` | Number | 0 | Optional |
| 12 | Unit Self Weight | `"UNIT_SELF_WEIGHT"` | Number | 0 | Optional |

### Python 예제

```python
# 바닥 하중 할당 (POST)
fbla_data = {
    "Assign": {
        "1": {
            "FLOOR_LOAD_TYPE_NAME": "TypicalFloor",  # FBLD에서 정의한 이름
            "FLOOR_DIST_TYPE": 2,    # Two Way 배분
            "DIR": "GZ",
            "OPT_PROJECTION": False,
            "DESC": "3층 바닥 영역",
            "GROUP_NAME": "FloorLoads",
            "NODES": [101, 102, 103, 104],  # 바닥 영역 노드
            "SUB_BEAM_NUM": 0,
            "UNIT_SELF_WEIGHT": 0.0
        },
        "2": {
            "FLOOR_LOAD_TYPE_NAME": "RoofFloor",
            "FLOOR_DIST_TYPE": 3,    # Polygon-Centroid
            "DIR": "GZ",
            "OPT_PROJECTION": False,
            "DESC": "옥상 영역",
            "GROUP_NAME": "RoofLoads",
            "NODES": [201, 202, 203, 204, 205]
        }
    }
}
result = midas_api("POST", "/db/FBLA", fbla_data)

# 조회
all_fbla = midas_api("GET", "/db/FBLA")

# 삭제
midas_api("DELETE", "/db/FBLA", {"Assign": {"2": {}}})
```

---

## 15. /db/FMLD — Finishing Material Loads

> 기둥/보 요소 주변 마감재 하중(Finishing Material Load)을 정의합니다. 키(key)는 **요소 번호**입니다.

**Input URI:** `{base url}/db/FMLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "448": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "FMLD_examples",
          "GROUP_NAME": "LoadGroups",
          "COVERING_TYPE": "ENVELOP",
          "COVERING_RANGE": ["HALF", "HALF", "FULL", "FULL"],
          "THICKNESS": 0.2,
          "DENSITY": 24.5,
          "DIR": "GZ",
          "SCALE_FACTOR": 1.0
        }
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Finishing Material Load items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Covering Type (`"ENVELOP"` / `"FILL"` / `"SURROUND"`) | `"COVERING_TYPE"` | String | `"ENVELOP"` | Optional |
| (5) | Covering Range [+x, -y, -x, +y] (`"FULL"` / `"HALF"`) | `"COVERING_RANGE"` | Array \[String, 4\] | - | Required |
| (6) | Covering Thickness (d) | `"THICKNESS"` | Number | 0 | Optional |
| (7) | Filling Property (Density) | `"DENSITY"` | Number | 0 | Optional |
| (8) | Direction (`"GX"` / `"GY"` / `"GZ"`) | `"DIR"` | String | `"GZ"` | Optional |
| (9) | Scale Factor | `"SCALE_FACTOR"` | Number | 0 | Required |

### Python 예제

```python
# 마감재 하중 정의 (POST)
fmld_data = {
    "Assign": {
        "200": {   # 요소 200번 (기둥)
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "DL",
                    "GROUP_NAME": "",
                    "COVERING_TYPE": "ENVELOP",   # 외피형
                    "COVERING_RANGE": ["FULL", "FULL", "FULL", "FULL"],  # 4면 전체
                    "THICKNESS": 0.05,     # 50mm 마감재
                    "DENSITY": 20.0,       # 20 kN/m³
                    "DIR": "GZ",
                    "SCALE_FACTOR": 1.0
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/FMLD", fmld_data)

# 조회
all_fmld = midas_api("GET", "/db/FMLD")

# 삭제
midas_api("DELETE", "/db/FMLD", {"Assign": {"200": {}}})
```

---

## 16. /db/POSP — Parameter of Soil Properties

> 토압 계산에 사용되는 지반 특성 파라미터를 정의합니다.

**Input URI:** `{base url}/db/POSP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "NAME": "Soil-1",
      "DESC": "",
      "OPT_USE_N": false,
      "GROUND_LEVEL": 6,
      "BEDROCK_LEVEL": -21,
      "FOOTING_LEVEL": -17.5,
      "ITEMS": [
        {"HEIGHT": 7,  "ANGLE_OR_N": 30, "DENSITY": 17, "VS": 160, "KH": 11449, "DISP": 0.001},
        {"HEIGHT": 1,  "ANGLE_OR_N": 30, "DENSITY": 17, "VS": 160, "KH": 11449, "DISP": 0.001}
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Soil Properties Name | `"NAME"` | String | - | Required |
| 2 | Description | `"DESC"` | String | Blank | Optional |
| 3 | Use N Value (true=N값 / false=내부마찰각) | `"OPT_USE_N"` | Number | false | Optional |
| 4 | Level of Ground Surface | `"GROUND_LEVEL"` | Number | - | Required |
| 5 | Level of Bedrock | `"BEDROCK_LEVEL"` | Number | - | Required |
| 6 | Level of Footing Bottom | `"FOOTING_LEVEL"` | Number | - | Required |
| 7 | Soil Characteristic items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Soil Layer Thickness | `"HEIGHT"` | Number | - | Required |
| (2) | Internal Friction Angle or N Value | `"ANGLE_OR_N"` | Number | - | Required |
| (3) | Unit Volume Weight of Soil | `"DENSITY"` | Number | - | Required |
| (4) | Shear Wave Velocity | `"VS"` | Number | - | Required |
| (5) | Coeff. of Horizontal Ground Reaction | `"KH"` | Number | - | Required |
| (6) | Relative Displacement | `"DISP"` | Number | - | Required |

### Python 예제

```python
# 지반 특성 파라미터 정의 (POST)
posp_data = {
    "Assign": {
        "1": {
            "NAME": "SiteA-Soil",
            "DESC": "A 부지 지반 특성",
            "OPT_USE_N": False,       # 내부마찰각 기준
            "GROUND_LEVEL": 0.0,      # GL±0
            "BEDROCK_LEVEL": -25.0,   # 기반암 GL-25m
            "FOOTING_LEVEL": -10.0,   # 기초저면 GL-10m
            "ITEMS": [
                # [층두께, 내부마찰각(°), 단위중량(kN/m³), 전단파속도, 수평지반반력계수, 상대변위]
                {"HEIGHT": 5.0,  "ANGLE_OR_N": 28, "DENSITY": 17.0, "VS": 150, "KH": 10000, "DISP": 0.001},
                {"HEIGHT": 5.0,  "ANGLE_OR_N": 32, "DENSITY": 18.0, "VS": 200, "KH": 20000, "DISP": 0.001},
                {"HEIGHT": 15.0, "ANGLE_OR_N": 35, "DENSITY": 19.0, "VS": 300, "KH": 50000, "DISP": 0.001},
            ]
        }
    }
}
result = midas_api("POST", "/db/POSP", posp_data)

# 조회
all_posp = midas_api("GET", "/db/POSP")

# 삭제
midas_api("DELETE", "/db/POSP", {"Assign": {"1": {}}})
```

---

## 17. /db/EPST — Static Earth Pressure

> 정적 토압을 산정하여 벽체 요소에 부가합니다.

**Input URI:** `{base url}/db/EPST`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "LOADCASE": "HsX(+)",
      "DIR": "XY",
      "ANGLE": 0,
      "IN_PT": [5000, 0, 0],
      "SF": 1,
      "EP_TYPE": "AT_REST",
      "SURCHARGE_LOAD": 16,
      "WATER_LEVEL": -4.7,
      "SOIL_PROP": "Soil-1",
      "SEL_TYPE": "GRUP",
      "ELEM_TYPE": "FRAME",
      "LOADING_AREA_GROUP": 1,
      "PRES_PROFILE_ITEMS": [
        {"LEVEL": 6,   "SOIL_PRES": 8,   "ADD_PRES": 0},
        {"LEVEL": -1,  "SOIL_PRES": 12,  "ADD_PRES": 0}
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LOADCASE"` | String | - | Required |
| 2 | Load Direction (`"XY"` / `"NORMAL"`) | `"DIR"` | String | `"XY"` | Optional |
| 3 | Static Earth Pressure Angle | `"ANGLE"` | Number | - | Required |
| 4 | Inner Point | `"IN_PT"` | Array \[Number\] | - | Optional |
| 5 | Scale Factor | `"SF"` | Number | - | Required |
| 6 | EP Type (`"AT_REST"` / `"ACTIVE"`) | `"EP_TYPE"` | String | - | Required |
| 7 | Surcharge Load | `"SURCHARGE_LOAD"` | Number | - | Required |
| 8 | Water Level | `"WATER_LEVEL"` | Number | - | Required |
| 9 | Soil Properties Name | `"SOIL_PROP"` | String | - | Required |
| 10 | Selection Type (`"GRUP"` / `"ELEMENT"`) | `"SEL_TYPE"` | String | - | Required |
| 11 | Element Type (`"FRAME"` / `"PLANAR"`) | `"ELEM_TYPE"` | String | - | Required |
| 12 | Node List | `"NODE_LIST"` | Array \[Integer\] | - | Optional |
| 13 | Element List | `"ELEM_LIST"` | Array \[Integer\] | - | Optional |
| 14 | Loading Area Group Name | `"LOADING_AREA_GROUP"` | Integer | - | Optional |
| 15 | Pressure Profile items | `"PRES_PROFILE_ITEMS"` | Array \[Object\] | - | Optional |
| (1) | Level of pressure profile point | `"LEVEL"` | Number | - | Required |
| (2) | Soil pressure at level | `"SOIL_PRES"` | Number | - | Required |
| (3) | Additional pressure at level | `"ADD_PRES"` | Number | - | Required |

### Python 예제

```python
# 정적 토압 부가 (POST)
epst_data = {
    "Assign": {
        "1": {
            "LOADCASE": "EP",
            "DIR": "XY",
            "ANGLE": 0.0,
            "IN_PT": [0, 0, 0],
            "SF": 1.0,
            "EP_TYPE": "AT_REST",         # 정지 토압
            "SURCHARGE_LOAD": 10.0,       # 상재하중 10 kN/m²
            "WATER_LEVEL": -5.0,          # 지하수위 GL-5m
            "SOIL_PROP": "SiteA-Soil",    # POSP에서 정의
            "SEL_TYPE": "ELEMENT",
            "ELEM_TYPE": "FRAME",
            "ELEM_LIST": [501, 502, 503, 504],  # 대상 요소
            "PRES_PROFILE_ITEMS": [
                {"LEVEL": 0.0,  "SOIL_PRES": 0.0,  "ADD_PRES": 5.0},
                {"LEVEL": -5.0, "SOIL_PRES": 42.5, "ADD_PRES": 5.0},
                {"LEVEL": -10.0,"SOIL_PRES": 90.0, "ADD_PRES": 5.0},
            ]
        }
    }
}
result = midas_api("POST", "/db/EPST", epst_data)

# 조회
all_epst = midas_api("GET", "/db/EPST")

# 삭제
midas_api("DELETE", "/db/EPST", {"Assign": {"1": {}}})
```

---

## 18. /db/EPSE — Seismic Earth Pressure

> 지진 시 동적 토압을 산정하여 벽체 요소에 부가합니다.

**Input URI:** `{base url}/db/EPSE`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "LOADCASE": "HaX(+)",
      "DIR": "XY",
      "ANGLE": 0,
      "IN_PT": [0, 0, 0],
      "SF": 1,
      "CODE": "KDS(41-17-00:2019)",
      "SEIS_LOAD": "KDS(2019)",
      "LAYER_PARAM": "SINGLE",
      "LAYER_LV": 0,
      "SOIL_PROP": "Soil-1",
      "SEL_TYPE": "ELEM",
      "ELEM_TYPE": "PLANAR",
      "NODE_LIST": [3461, 3831, 4856, 5597],
      "ELEM_LIST": [18451],
      "PRES_PROFILE_ITEMS": []
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LOADCASE"` | String | - | Required |
| 2 | Load Direction (`"XY"` / `"NORMAL"`) | `"DIR"` | String | `"XY"` | Optional |
| 3 | Seismic Earth Pressure Angle | `"ANGLE"` | Number | 0 | Optional |
| 4 | Inner Point | `"IN_PT"` | Number | - | Optional |
| 5 | Scale Factor | `"SF"` | Number | - | Optional |
| 6 | Design Code | `"CODE"` | String | - | Optional |
| 7 | Seismic Load Name | `"SEIS_LOAD"` | String | - | Required |
| 8 | Soil Layer Parameter (`"SINGLE"` / `"DOUBLE"`) | `"LAYER_PARAM"` | String | `"SINGLE"` | Optional |
| 9 | Soil Second Layer Level (Double Cosine) | `"LAYER_LV"` | Number | 0 | Optional |
| 10 | Soil Properties Name | `"SOIL_PROP"` | String | - | Required |
| 11 | Selection Type (`"GROUP"` / `"ELEMENT"`) | `"SEL_TYPE"` | String | - | Required |
| 12 | Element Type (`"FRAME"` / `"PLANAR"`) | `"ELEM_TYPE"` | String | `"ELEM"` | Optional |
| 13 | Node List | `"NODE_LIST"` | Array \[Integer\] | - | Optional |
| 14 | Element List | `"ELEM_LIST"` | Array \[Integer\] | - | Optional |
| 15 | Loading Area Group Name | `"LOADING_AREA_GROUP"` | Integer | - | Optional |
| 16 | Pressure Profile items | `"PRES_PROFILE_ITEMS"` | Array \[Object\] | - | Optional |
| (1) | Level | `"LEVEL"` | Number | - | Required |
| (2) | Horizontal Coefficient KH | `"KH"` | Number | - | Required |
| (3) | Relative Displacement | `"REL_DISP"` | Number | - | Required |
| (4) | Seismic Pressure | `"SEIS_PRES"` | Number | - | Required |
| (5) | Additional Pressure | `"ADD_PRES"` | Number | - | Optional |

### Python 예제

```python
# 지진 토압 부가 (POST)
epse_data = {
    "Assign": {
        "1": {
            "LOADCASE": "EEP",             # 지진 토압 하중 케이스
            "DIR": "XY",
            "ANGLE": 0.0,
            "IN_PT": [0, 0, 0],
            "SF": 1.0,
            "CODE": "KDS(41-17-00:2019)",
            "SEIS_LOAD": "KDS(2019)",       # POSL에서 정의한 이름
            "LAYER_PARAM": "SINGLE",
            "LAYER_LV": 0.0,
            "SOIL_PROP": "SiteA-Soil",
            "SEL_TYPE": "ELEMENT",
            "ELEM_TYPE": "FRAME",
            "ELEM_LIST": [501, 502, 503],
            "PRES_PROFILE_ITEMS": [
                {"LEVEL": 0.0,  "KH": 0.15, "REL_DISP": 0.01, "SEIS_PRES": 12.5, "ADD_PRES": 0.0},
                {"LEVEL": -10.0,"KH": 0.15, "REL_DISP": 0.01, "SEIS_PRES": 37.5, "ADD_PRES": 0.0},
            ]
        }
    }
}
result = midas_api("POST", "/db/EPSE", epse_data)

# 조회
all_epse = midas_api("GET", "/db/EPSE")

# 삭제
midas_api("DELETE", "/db/EPSE", {"Assign": {"1": {}}})
```

---

## 19. /db/POSL — Parameter of Seismic Loads

> 정적 지진 하중 계산에 필요한 지진 하중 파라미터를 정의합니다 (KDS 41-17-00:2019 기반).

**Input URI:** `{base url}/db/POSL`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "NAME": "KDS(2019)",
      "CODE": "KDS(41-17-00:2019)",
      "METHOD": "RES_DISP",
      "SZ": "1",
      "EPA": 0.22,
      "SC": "S1",
      "FA": 1.12,
      "FV": 0.84,
      "SDS": 0.41066666666666674,
      "SD1": 0.12319999999999999,
      "USER_GROUP": "1",
      "IF": 1.2,
      "RMF": 3
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"NAME"` | String | - | Required |
| 2 | Seismic Load Code | `"CODE"` | String | - | Optional |
| 3 | Seismic Calculation Method (`"RES_DISP"` / `"EQV_STATIC"`) | `"METHOD"` | String | - | Optional |
| 4 | Seismic Zone | `"SZ"` | String | - | Required |
| 5 | Effective Peak Ground Acceleration | `"EPA"` | Number | - | Required |
| 6 | Site Class | `"SC"` | String | - | Required |
| 7 | Short-period Site Coefficient | `"FA"` | Number | - | Required |
| 8 | Long-period Site Coefficient | `"FV"` | Number | - | Required |
| 9 | Design Spectral Acceleration at Short Period | `"SDS"` | Number | - | Required |
| 10 | Design Spectral Acceleration at 1-sec Period | `"SD1"` | Number | - | Required |
| 11 | Seismic User Group | `"USER_GROUP"` | String | - | Optional |
| 12 | Importance Factor | `"IF"` | Number | - | Required |
| 13 | Response Modification Factor | `"RMF"` | Number | - | Required |

### Python 예제

```python
# 지진 하중 파라미터 정의 (POST) — KDS 41-17-00:2019
posl_data = {
    "Assign": {
        "1": {
            "NAME": "KDS2019",
            "CODE": "KDS(41-17-00:2019)",
            "METHOD": "EQV_STATIC",    # 등가정적법
            "SZ": "1",                 # 지진구역 I
            "EPA": 0.22,               # 유효지반가속도
            "SC": "S2",                # 지반종류 (S2)
            "FA": 1.0,                 # 단주기 지반 증폭계수
            "FV": 1.4,                 # 장주기 지반 증폭계수
            "SDS": 0.2933,             # 단주기 설계스펙트럼
            "SD1": 0.1467,             # 1초 설계스펙트럼
            "USER_GROUP": "1",         # 내진등급 I
            "IF": 1.5,                 # 중요도 계수
            "RMF": 3.0                 # 반응수정계수
        }
    }
}
result = midas_api("POST", "/db/POSL", posl_data)

# 조회
all_posl = midas_api("GET", "/db/POSL")

# 삭제
midas_api("DELETE", "/db/POSL", {"Assign": {"1": {}}})
```

---

## 20. /db/SWIND — Static Wind Load

> KDS 41-12:2022 기반 정적 풍하중을 정의합니다. `INPUT_METHOD`에 따라 Simplified / General / Vortex Shedding 방법이 선택됩니다.

**Input URI:** `{base url}/db/SWIND`  
**Active Methods:** `POST, GET, PUT, DELETE`

> **참고:** URL 경로에서 `DB/SWIND` (대문자)를 사용합니다.

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Wind Load Code (`"KDS(41-12: 2022)"`) | `"WIND_CODE"` | string (enum) | - | Required |
| 2 | Description | `"DESC"` | string | `""` | Optional |
| 3 | Scale Factor X | `"SCALE_FACTOR_X"` | number | - | Required |
| 4 | Scale Factor Y | `"SCALE_FACTOR_Y"` | number | - | Required |
| 5 | KDS(41-12:2022) Parameters | `"PARAMETERS"` | object | - | Required |
| (1) | Input Method (0=Simplified / 1=General / 2=General+Vortex) | `"INPUT_METHOD"` | integer (enum) | - | Required |
| **INPUT_METHOD = 0 (Simplified)** | | | | | |
| | Basic Wind Speed | `"WIND_SPEED"` | number | - | Required |
| | Roof Height | `"ROOF_HEIGHT"` | number | system | Optional |
| | Exposure Coefficient CE | `"CE"` | number | 1 | Optional |
| **INPUT_METHOD = 1 (General)** | | | | | |
| | Exposure Category (0=A / 1=B / 2=C / 3=D) | `"EXP_CATEGORY"` | integer (enum) | - | Required |
| | Basic Wind Speed | `"WIND_SPEED"` | number | - | Required |
| | Importance Factor | `"IMPORTANCE_FACTOR"` | number | - | Required |
| | Roof Height | `"ROOF_HEIGHT"` | number | system | Optional |
| | Topographic Effect | `"TOPOGRAPHIC_EFFECT"` | object | - | Optional |
| a | Use Topographic Effect | `"OPT_USE"` | boolean | false | Optional |
| a | Topographic Factor KZT (OPT_USE=true) | `"KZT"` | number | - | Conditional |
| | Direction Factor X | `"DIRECTION_FACTOR_X"` | number | 1 | Optional |
| | Direction Factor Y | `"DIRECTION_FACTOR_Y"` | number | 1 | Optional |
| | Rigidity Classification | `"RIGIDITY"` | integer | - | Required |
| | Gust Factor X | `"GUST_FACTOR_X"` | number | - | Required |
| | Gust Factor Y | `"GUST_FACTOR_Y"` | number | - | Required |
| | Force Coefficient | `"FORCE_COEF"` | object | - | Optional |
| a | Use User-defined Force Coefficient | `"OPT_USE"` | boolean | false | Optional |
| a | Force Coefficient Value (OPT_USE=true) | `"FORCE_COEF"` | number | - | Conditional |
| | Building Type (0=Middle Low Rise / 1=High Rise) | `"BUILDING_TYPE"` | integer (enum) | - | Optional |
| | Vibration Parameters | `"VIBRATION_PARAMS"` | object | - | Optional |
| a | Across-wind Vibration | `"ACROSS_WIND"` | boolean | false | Optional |
| b | Torsional-wind Vibration | `"TORSIONAL_WIND"` | boolean | false | Optional |
| c | Wind Response | `"WIND_RESPONSE"` | boolean | false | Optional |
| d | Building Length X | `"BL_X"` | number | - | Required |
| e | Building Length Y | `"BL_Y"` | number | - | Required |
| f | Natural Frequency X | `"NO_X"` | number | - | Required |
| g | Natural Frequency Y | `"NO_Y"` | number | - | Required |
| h | Torsional Natural Frequency | `"NO_T"` | number | - | Required |
| i | Mass | `"M"` | number | system | Optional |
| j | Mass in X direction | `"MX"` | number | system | Optional |
| k | Mass in Y direction | `"MY"` | number | system | Optional |
| l | Mass Moment of Inertia | `"MI"` | number | system | Optional |
| m | Damping Ratio | `"ZF"` | number | - | Required |
| n | Vibration Mode Coefficient | `"VIBRATION_MODE"` | number | - | Required |
| **INPUT_METHOD = 2 (General + Vortex Shedding)** | | | | | |
| | Roof Height | `"ROOF_HEIGHT"` | number | system | Optional |
| | Vortex Shedding DM | `"DM"` | number | - | Required |
| | Vortex Shedding DB | `"DB"` | number | - | Required |
| | Natural Frequency for Vortex | `"N"` | number | - | Required |
| | Mass for Vortex Check | `"M"` | number | system | Optional |
| | Damping Ratio for Vortex | `"ZF"` | number | - | Required |
| 6 | Additional Story-level Wind Load | `"ADDITIONAL_LOAD"` | array \[object\] | - | Optional |
| (1) | Story Name | `"STORY_NAME"` | string | - | Required |
| (2) | Along-wind Load X | `"ALONG_X"` | number | - | Optional |
| (3) | Along-wind Load Y | `"ALONG_Y"` | number | - | Optional |
| (4) | Across-wind Load X | `"ACROSS_X"` | number | - | Optional |
| (5) | Across-wind Load Y | `"ACROSS_Y"` | number | - | Optional |
| (6) | Torsional Wind Load RZ | `"TORSIONAL_RZ"` | number | - | Optional |
| (7) | Torsional Wind Load RZ X | `"TORSIONAL_RZ_X"` | number | - | Optional |
| (8) | Torsional Wind Load RZ Y | `"TORSIONAL_RZ_Y"` | number | - | Optional |

### Python 예제

```python
# 정적 풍하중 정의 (POST) — INPUT_METHOD=0: Simplified
swind_simplified = {
    "Assign": {
        "1": {
            "WIND_CODE": "KDS(41-12: 2022)",
            "DESC": "Simplified Method",
            "SCALE_FACTOR_X": 1.0,
            "SCALE_FACTOR_Y": 1.0,
            "PARAMETERS": {
                "INPUT_METHOD": 0,          # Simplified Method
                "WIND_SPEED": 30.0,         # 기본풍속 30 m/s
                "ROOF_HEIGHT": 45.0,        # 건물 높이 45m
                "CE": 1.0                   # 노출계수
            }
        }
    }
}
result = midas_api("POST", "/db/SWIND", swind_simplified)

# General Method (INPUT_METHOD=1)
swind_general = {
    "Assign": {
        "2": {
            "WIND_CODE": "KDS(41-12: 2022)",
            "DESC": "General Method",
            "SCALE_FACTOR_X": 1.0,
            "SCALE_FACTOR_Y": 1.0,
            "PARAMETERS": {
                "INPUT_METHOD": 1,
                "EXP_CATEGORY": 1,          # 노출범주 B
                "WIND_SPEED": 30.0,
                "IMPORTANCE_FACTOR": 1.1,
                "ROOF_HEIGHT": 45.0,
                "TOPOGRAPHIC_EFFECT": {"OPT_USE": False},
                "DIRECTION_FACTOR_X": 1.0,
                "DIRECTION_FACTOR_Y": 1.0,
                "RIGIDITY": 1,              # 강성 분류
                "GUST_FACTOR_X": 1.8,
                "GUST_FACTOR_Y": 1.8,
                "BUILDING_TYPE": 1          # 고층 건물
            }
        }
    }
}
midas_api("POST", "/db/SWIND", swind_general)

# 조회
all_swind = midas_api("GET", "/db/SWIND")

# 삭제
midas_api("DELETE", "/db/SWIND", {"Assign": {"1": {}}})
```

---

## 21. /db/SSEIS — Static Seismic Load

> KDS 41-17-00:2019 기반 등가정적 지진하중을 정의합니다.

**Input URI:** `{base url}/db/SSEIS`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Seismic Load Code (`"KDS(41-17-00:2019)"`) | `"SEIS_CODE"` | string (enum) | - | Required |
| 2 | Description | `"DESC"` | string | `""` | Optional |
| 3 | Scale Factor X | `"SCALE_FACTOR_X"` | number | - | Required |
| 4 | Scale Factor Y | `"SCALE_FACTOR_Y"` | number | - | Required |
| 5 | Accidental Eccentricity X (0=Positive / 1=Negative / 2=None) | `"ACCIDENT_ECCEN_X"` | integer (enum) | 0 | Optional |
| 6 | Accidental Eccentricity Y (0=Positive / 1=Negative / 2=None) | `"ACCIDENT_ECCEN_Y"` | integer (enum) | 0 | Optional |
| 7 | Consider Accidental Torsion | `"ACCIDENT_TORSION"` | boolean | false | Optional |
| 8 | KDS(41-17-00:2019) Parameters | `"PARAMETERS"` | object | - | Required |
| (1) | Seismic Zone (0=Zone1 / 1=Zone2) | `"SEIS_ZONE"` | integer (enum) | - | Required |
| (2) | Effective Peak Acceleration | `"EPA"` | number | - | Required |
| (3) | Site Class (0=S1 / 1=S2 / 2=S3 / 3=S4 / 4=S5 / 5=S6) | `"SITE_CLASS"` | integer (enum) | - | Required |
| (4) | Short-period Site Coefficient FA | `"FA"` | number | system | Optional |
| (5) | Long-period Site Coefficient FV | `"FV"` | number | system | Optional |
| (6) | Design Spectral Acceleration at Short Period SDS | `"SDS"` | number | system | Optional |
| (7) | Design Spectral Acceleration at 1-sec SD1 | `"SD1"` | number | system | Optional |
| (8) | Seismic Use Group (0=Special / 1=I / 2=II) | `"SEIS_USE_GROUP"` | integer (enum) | - | Required |
| (9) | Importance Factor | `"IMPORTANCE_FACTOR"` | number | - | Required |
| (10) | Period Method (0=Analytical / 1=Approximate) | `"PERIOD_METHOD"` | integer (enum) | - | Required |
| **PERIOD_METHOD = 0** | | | | | |
| | Analytical Period X | `"PERIOD_ANALYSIS_X"` | number | - | Required |
| | Analytical Period Y | `"PERIOD_ANALYSIS_Y"` | number | - | Required |
| | Approximate Period X | `"PERIOD_APPR_X"` | number | - | Required |
| | Approximate Period Y | `"PERIOD_APPR_Y"` | number | - | Required |
| **PERIOD_METHOD = 1** | | | | | |
| | Approximate Period X | `"PERIOD_APPR_X"` | number | - | Required |
| | Approximate Period Y | `"PERIOD_APPR_Y"` | number | - | Required |
| | Response Modification Factor X | `"RESPONSE_MOD_FACTOR_X"` | number | - | Required |
| | Response Modification Factor Y | `"RESPONSE_MOD_FACTOR_Y"` | number | - | Required |
| 9 | Additional Story-level Seismic Load | `"ADDITIONAL_LOAD"` | object | - | Optional |
| (1) | Story Name | `"STORY_NAME"` | string | - | Required |
| (2) | Additional Seismic Load X | `"ALONG_X"` | number | - | Required |
| (3) | Additional Seismic Load Y | `"ALONG_Y"` | number | - | Required |
| (4) | Additional Torsional Seismic Load RZ | `"TORSIONAL_RZ"` | number | - | Required |

### Python 예제

```python
# 등가정적 지진하중 정의 (POST) — KDS 41-17-00:2019
sseis_data = {
    "Assign": {
        "1": {
            "SEIS_CODE": "KDS(41-17-00:2019)",
            "DESC": "X방향 지진하중",
            "SCALE_FACTOR_X": 1.0,
            "SCALE_FACTOR_Y": 0.0,         # X방향만 적용
            "ACCIDENT_ECCEN_X": 0,          # X방향 우발 편심 (+)
            "ACCIDENT_ECCEN_Y": 2,          # Y방향 우발 편심 없음
            "ACCIDENT_TORSION": True,
            "PARAMETERS": {
                "SEIS_ZONE": 0,             # 지진구역 I
                "EPA": 0.22,
                "SITE_CLASS": 1,            # S2 지반
                "FA": 1.0,
                "FV": 1.4,
                "SDS": 0.2933,
                "SD1": 0.1467,
                "SEIS_USE_GROUP": 1,        # 내진등급 I
                "IMPORTANCE_FACTOR": 1.5,
                "PERIOD_METHOD": 1,         # 근사주기법
                "PERIOD_APPR_X": 1.2,       # X방향 근사주기 (초)
                "PERIOD_APPR_Y": 1.0,       # Y방향 근사주기 (초)
                "RESPONSE_MOD_FACTOR_X": 5.0,  # X방향 반응수정계수
                "RESPONSE_MOD_FACTOR_Y": 5.0   # Y방향 반응수정계수
            }
        },
        "2": {
            "SEIS_CODE": "KDS(41-17-00:2019)",
            "DESC": "Y방향 지진하중",
            "SCALE_FACTOR_X": 0.0,
            "SCALE_FACTOR_Y": 1.0,
            "ACCIDENT_ECCEN_X": 2,
            "ACCIDENT_ECCEN_Y": 0,
            "ACCIDENT_TORSION": True,
            "PARAMETERS": {
                "SEIS_ZONE": 0,
                "EPA": 0.22,
                "SITE_CLASS": 1,
                "FA": 1.0,
                "FV": 1.4,
                "SEIS_USE_GROUP": 1,
                "IMPORTANCE_FACTOR": 1.5,
                "PERIOD_METHOD": 1,
                "PERIOD_APPR_X": 1.2,
                "PERIOD_APPR_Y": 1.0,
                "RESPONSE_MOD_FACTOR_X": 5.0,
                "RESPONSE_MOD_FACTOR_Y": 5.0
            }
        }
    }
}
result = midas_api("POST", "/db/SSEIS", sseis_data)

# 조회
all_sseis = midas_api("GET", "/db/SSEIS")

# 삭제
midas_api("DELETE", "/db/SSEIS", {"Assign": {"2": {}}})
```

---

## 전체 워크플로우 예제

아래는 전형적인 건축 구조물에 정적 하중 데이터를 일괄 입력하는 완성형 예제입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY_HERE"

def midas_api(method: str, endpoint: str, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}

# ─── Step 1: 정적 하중 케이스 정의 ───────────────────────────────
stld_data = {
    "Assign": {
        "1": {"NAME": "DL",  "TYPE": "D",  "DESC": "사하중"},
        "2": {"NAME": "LL",  "TYPE": "L",  "DESC": "활하중"},
        "3": {"NAME": "WX",  "TYPE": "W",  "DESC": "풍하중 +X"},
        "4": {"NAME": "WY",  "TYPE": "W",  "DESC": "풍하중 +Y"},
        "5": {"NAME": "EX",  "TYPE": "E",  "DESC": "지진하중 X"},
        "6": {"NAME": "EY",  "TYPE": "E",  "DESC": "지진하중 Y"},
        "7": {"NAME": "EP",  "TYPE": "EP", "DESC": "토압"},
        "8": {"NAME": "STL", "TYPE": "STL","DESC": "지점 침하"},
    }
}
midas_api("POST", "/db/STLD", stld_data)

# ─── Step 2: 자중 (Self-Weight) ──────────────────────────────────
midas_api("POST", "/db/BODF", {
    "Assign": {
        "1": {"LCNAME": "DL", "GROUP_NAME": "", "FV": [0, 0, -1]}
    }
})

# ─── Step 3: 하중→질량 변환 ──────────────────────────────────────
midas_api("POST", "/db/LTOM", {
    "Assign": {
        "1": {
            "DIR": "XYZ",
            "bNODAL": True, "bBEAM": True, "bFLOOR": True, "bPRES": False,
            "GRAV": 9.806,
            "vLC": [
                {"LCNAME": "DL", "FACTOR": 1.0},
                {"LCNAME": "LL", "FACTOR": 0.25},
            ]
        }
    }
})

# ─── Step 4: 노드 집중하중 ────────────────────────────────────────
midas_api("POST", "/db/CNLD", {
    "Assign": {
        "50": {   # 노드 50번
            "ITEMS": [{"ID": 1, "LCNAME": "LL", "GROUP_NAME": "",
                       "FX": 0, "FY": 0, "FZ": -200.0, "MX": 0, "MY": 0, "MZ": 0}]
        }
    }
})

# ─── Step 5: 보 분포하중 ──────────────────────────────────────────
midas_api("POST", "/db/BMLD", {
    "Assign": {
        "100": {   # 요소 100번
            "ITEMS": [{"ID": 1, "LCNAME": "LL", "GROUP_NAME": "",
                       "CMD": "BEAM", "TYPE": "UNILOAD", "DIRECTION": "GZ",
                       "USE_PROJECTION": False, "USE_ECCEN": False,
                       "D": [0, 1, 0, 0], "P": [-25.0, -25.0, 0, 0]}]
        }
    }
})

# ─── Step 6: 바닥 하중 타입 정의 후 할당 ────────────────────────
midas_api("POST", "/db/FBLD", {
    "Assign": {
        "1": {
            "NAME": "TypFloor",
            "DESC": "",
            "ITEM": [
                {"LCNAME": "DL", "FLOOR_LOAD": 3.5, "OPT_SUB_BEAM_WEIGHT": True},
                {"LCNAME": "LL", "FLOOR_LOAD": 2.5, "OPT_SUB_BEAM_WEIGHT": False},
            ]
        }
    }
})
midas_api("POST", "/db/FBLA", {
    "Assign": {
        "1": {
            "FLOOR_LOAD_TYPE_NAME": "TypFloor",
            "FLOOR_DIST_TYPE": 2,           # Two Way
            "DIR": "GZ",
            "OPT_PROJECTION": False,
            "GROUP_NAME": "FloorGroup",
            "NODES": [11, 12, 13, 14],      # 바닥 영역 노드
        }
    }
})

# ─── Step 7: 지반 파라미터 + 정적 토압 ──────────────────────────
midas_api("POST", "/db/POSP", {
    "Assign": {
        "1": {
            "NAME": "SiteA",
            "OPT_USE_N": False,
            "GROUND_LEVEL": 0.0,
            "BEDROCK_LEVEL": -20.0,
            "FOOTING_LEVEL": -8.0,
            "ITEMS": [
                {"HEIGHT": 8.0, "ANGLE_OR_N": 30, "DENSITY": 18.0,
                 "VS": 200, "KH": 20000, "DISP": 0.001},
                {"HEIGHT": 12.0,"ANGLE_OR_N": 35, "DENSITY": 19.0,
                 "VS": 350, "KH": 60000, "DISP": 0.001},
            ]
        }
    }
})
midas_api("POST", "/db/EPST", {
    "Assign": {
        "1": {
            "LOADCASE": "EP",
            "DIR": "XY", "ANGLE": 0, "IN_PT": [0, 0, 0], "SF": 1.0,
            "EP_TYPE": "AT_REST",
            "SURCHARGE_LOAD": 10.0, "WATER_LEVEL": -3.0,
            "SOIL_PROP": "SiteA",
            "SEL_TYPE": "ELEMENT", "ELEM_TYPE": "FRAME",
            "ELEM_LIST": [201, 202, 203],
            "PRES_PROFILE_ITEMS": [
                {"LEVEL": 0.0,  "SOIL_PRES": 0.0,  "ADD_PRES": 5.0},
                {"LEVEL": -8.0, "SOIL_PRES": 72.0, "ADD_PRES": 5.0},
            ]
        }
    }
})

# ─── Step 8: 지진하중 파라미터 + 정적 지진하중 ──────────────────
midas_api("POST", "/db/POSL", {
    "Assign": {
        "1": {
            "NAME": "KDS2019",
            "CODE": "KDS(41-17-00:2019)",
            "METHOD": "EQV_STATIC",
            "SZ": "1", "EPA": 0.22, "SC": "S2",
            "FA": 1.0, "FV": 1.4,
            "SDS": 0.2933, "SD1": 0.1467,
            "USER_GROUP": "1", "IF": 1.5, "RMF": 5.0
        }
    }
})
midas_api("POST", "/db/SSEIS", {
    "Assign": {
        "1": {
            "SEIS_CODE": "KDS(41-17-00:2019)",
            "DESC": "EX", "SCALE_FACTOR_X": 1.0, "SCALE_FACTOR_Y": 0.0,
            "ACCIDENT_ECCEN_X": 0, "ACCIDENT_ECCEN_Y": 2, "ACCIDENT_TORSION": True,
            "PARAMETERS": {
                "SEIS_ZONE": 0, "EPA": 0.22, "SITE_CLASS": 1,
                "SEIS_USE_GROUP": 1, "IMPORTANCE_FACTOR": 1.5,
                "PERIOD_METHOD": 1,
                "PERIOD_APPR_X": 1.2, "PERIOD_APPR_Y": 1.0,
                "RESPONSE_MOD_FACTOR_X": 5.0, "RESPONSE_MOD_FACTOR_Y": 5.0
            }
        }
    }
})

# ─── Step 9: 정적 풍하중 (KDS 41-12:2022) ───────────────────────
midas_api("POST", "/db/SWIND", {
    "Assign": {
        "1": {
            "WIND_CODE": "KDS(41-12: 2022)",
            "DESC": "Wind X+Y", "SCALE_FACTOR_X": 1.0, "SCALE_FACTOR_Y": 1.0,
            "PARAMETERS": {
                "INPUT_METHOD": 0,       # Simplified
                "WIND_SPEED": 30.0,
                "ROOF_HEIGHT": 45.0,
                "CE": 1.0
            }
        }
    }
})

print("정적 하중 데이터 입력 완료")
```

---

*[06_DB_Static_Loads.md] 작성 완료 — 다음 파일 [07_DB_Temperature_Prestress.md] 진행 준비가 되었습니다.*
