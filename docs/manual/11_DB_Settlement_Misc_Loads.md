# 11. DB – Settlement / Miscellaneous Loads

침하하중(Settlement Loads) 및 기타 하중(Miscellaneous Loads) 관련 데이터베이스 API입니다.

> **Base URL**
> - Civil NX : `https://moa-engineers.midasit.com:443/civil`
> - Gen NX   : `https://moa-engineers.midasit.com:443/gen`
>
> **인증 헤더** : 모든 요청에 `MAPI-Key: <your_api_key>` 헤더를 포함해야 합니다.

---

## 목차

### Settlement Loads (2개)

| No. | Endpoint | 설명 |
|-----|----------|------|
| 1 | [/db/SMPT](#1-dbsmpt--settlement-group) | Settlement Group |
| 2 | [/db/SMLC](#2-dbsmlc--settlement-load-cases) | Settlement Load Cases |

### Miscellaneous Loads (7개)

| No. | Endpoint | 설명 |
|-----|----------|------|
| 3 | [/db/PLCB](#3-dbplcb--pre-composite-section) | Pre-composite Section |
| 4 | [/db/LDSQ](#4-dbldsq--load-sequence-for-nonlinear) | Load Sequence for Nonlinear |
| 5 | [/db/WVLD](#5-dbwvld--wave-loads) | Wave Loads |
| 6 | [/db/IELC](#6-dbielc--ignore-elements-for-load-cases) | Ignore Elements for Load Cases |
| 7 | [/db/IFGS](#7-dbifgs--large-displacement--initial-forces-for-geometric-stiffness) | Large Displacement – Initial Forces for Geometric Stiffness |
| 8 | [/db/EFCT](#8-dbefct--small-displacement--initial-force-control-data) | Small Displacement – Initial Force Control Data |
| 9 | [/db/INMF](#9-dbinmf--small-displacement--initial-element-force) | Small Displacement – Initial Element Force |

---

## 1. /db/SMPT — Settlement Group

지점 침하 그룹을 정의합니다. 침하 변위를 적용할 노드 목록과 침하량을 저장합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/SMPT` | 침하 그룹 생성 |
| GET | `{base_url}/db/SMPT` | 전체 침하 그룹 조회 |
| GET | `{base_url}/db/SMPT/{id}` | 특정 침하 그룹 조회 |
| PUT | `{base_url}/db/SMPT/{id}` | 침하 그룹 수정 |
| DELETE | `{base_url}/db/SMPT/{id}` | 침하 그룹 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Settlement Group Name | `"NAME"` | String | - | Required |
| 2 | Settlement Displacement | `"SETTLE"` | Number | - | Required |
| 3 | Node List | `"ITEMS"` | Array [Integer] | - | Required |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "NAME": "SG1",
      "SETTLE": 25,
      "ITEMS": [100, 101]
    },
    "2": {
      "NAME": "SG2",
      "SETTLE": 15,
      "ITEMS": [102, 103]
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

# 침하 그룹 생성
def create_settlement_groups():
    payload = {
        "Assign": {
            "1": {
                "NAME": "SG1",   # 침하 그룹 이름
                "SETTLE": 25,    # 침하량 (mm)
                "ITEMS": [100, 101]  # 적용 노드 목록
            },
            "2": {
                "NAME": "SG2",
                "SETTLE": 15,
                "ITEMS": [102, 103]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/SMPT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Settlement Groups created:", resp.json())

# 전체 침하 그룹 조회
def get_all_settlement_groups():
    resp = requests.get(f"{BASE_URL}/db/SMPT", headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

create_settlement_groups()
```

---

## 2. /db/SMLC — Settlement Load Cases

침하 하중 케이스(Settlement Load Cases)를 정의합니다. 침하 그룹을 참조하여 최솟값/최댓값 그룹 수와 스케일 팩터를 설정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/SMLC` | 침하 하중 케이스 생성 |
| GET | `{base_url}/db/SMLC` | 전체 조회 |
| GET | `{base_url}/db/SMLC/{id}` | 특정 케이스 조회 |
| PUT | `{base_url}/db/SMLC/{id}` | 수정 |
| DELETE | `{base_url}/db/SMLC/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Settlement Load Case No. (Assign Key) | `"KEY"` | Integer | - | Required |
| 2 | Settlement Load Case Name | `"NAME"` | String | - | Required |
| 3 | Description | `"DESC"` | String | - | Required |
| 4 | Settlement Scale Factor | `"FACTOR"` | Number | - | Required |
| 5 | Settlement – Min. Group Nos. | `"MIN"` | Integer | - | Required |
| 6 | Settlement – Max. Group Nos. | `"MAX"` | Integer | - | Required |
| 7 | Selected Settlement Group Names | `"ST_GROUPS"` | Array [String] | - | Required |

> **참고**: `MIN` / `MAX` 는 하중 케이스에 포함되는 침하 그룹의 최소/최대 개수를 의미합니다.

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "NAME": "SMLC1",
      "DESC": "",
      "FACTOR": 1.2,
      "MIN": 1,
      "MAX": 1,
      "ST_GROUPS": ["SG1", "SG2"]
    },
    "2": {
      "NAME": "SMLC2",
      "DESC": "",
      "FACTOR": 1.0,
      "MIN": 1,
      "MAX": 1,
      "ST_GROUPS": ["SG1", "SG2"]
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

# 침하 하중 케이스 생성
def create_settlement_load_cases():
    payload = {
        "Assign": {
            "1": {
                "NAME": "SMLC1",
                "DESC": "Settlement Load Case 1",
                "FACTOR": 1.2,      # 스케일 팩터
                "MIN": 1,           # 최소 그룹 수
                "MAX": 1,           # 최대 그룹 수
                "ST_GROUPS": ["SG1", "SG2"]  # 참조 침하 그룹 목록
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/SMLC", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Settlement Load Cases created:", resp.json())

create_settlement_load_cases()
```

---

## 3. /db/PLCB — Pre-composite Section

합성 이전(Pre-composite) 단계에 적용되는 정적 하중 케이스 목록을 지정합니다. 합성 구조 해석 시 슬래브 타설 전 거더만으로 지지되는 하중 케이스를 설정합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/PLCB` | Pre-composite 하중 케이스 설정 |
| GET | `{base_url}/db/PLCB` | 전체 조회 |
| GET | `{base_url}/db/PLCB/{id}` | 특정 항목 조회 |
| PUT | `{base_url}/db/PLCB/{id}` | 수정 |
| DELETE | `{base_url}/db/PLCB/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Static Load Case Names | `"LCNAME_ITEM"` | Array [String] | - | Required |

> **참고**: Assign Key `"1"` 이 유일한 레코드로, 시스템 전체에 하나의 Pre-composite 목록을 가집니다.

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "LCNAME_ITEM": ["DL(BC)1", "DL(BC)3"]
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

# Pre-composite 하중 케이스 설정
def set_precomposite_load_cases():
    payload = {
        "Assign": {
            "1": {
                # 합성 이전 단계 정적 하중 케이스 목록
                "LCNAME_ITEM": ["DL(BC)1", "DL(BC)3"]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/PLCB", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Pre-composite Load Cases set:", resp.json())

# 수정 (PUT)
def update_precomposite_load_cases():
    payload = {
        "LCNAME_ITEM": ["DL(BC)1", "DL(BC)2", "DL(BC)3"]
    }
    resp = requests.put(f"{BASE_URL}/db/PLCB/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Updated:", resp.json())

set_precomposite_load_cases()
```

---

## 4. /db/LDSQ — Load Sequence for Nonlinear

비선형 해석에 적용되는 하중 순서(Load Sequence)를 정의합니다. 비선형 해석에서 하중이 적용되는 순서를 제어합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/LDSQ` | 비선형 하중 순서 생성 |
| GET | `{base_url}/db/LDSQ` | 전체 조회 |
| GET | `{base_url}/db/LDSQ/{id}` | 특정 항목 조회 |
| PUT | `{base_url}/db/LDSQ/{id}` | 수정 |
| DELETE | `{base_url}/db/LDSQ/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Load Case Names (순서 배열) | `"LCNAME_ITEM"` | Array [String] | - | Required |

> **참고**: Assign Key는 하중 순서 세트 번호입니다. `LCNAME_ITEM` 배열의 순서가 비선형 해석에서의 하중 적용 순서가 됩니다.

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "LCNAME_ITEM": ["DL(BC)4", "DL(AC)"]
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

# 비선형 하중 순서 생성
def create_load_sequence():
    payload = {
        "Assign": {
            "1": {
                # 비선형 해석 하중 적용 순서 (배열 순서대로 적용)
                "LCNAME_ITEM": ["DL(BC)4", "DL(AC)"]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/LDSQ", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Load Sequence created:", resp.json())

create_load_sequence()
```

---

## 5. /db/WVLD — Wave Loads

해양 구조물에 적용되는 파랑 하중(Wave Loads)을 정의합니다. Morison 방정식 기반으로 항력·관성력 계수, 파랑 특성, 조류 프로파일, 해양 성장 등을 포함합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/WVLD` | 파랑 하중 생성 |
| GET | `{base_url}/db/WVLD` | 전체 조회 |
| GET | `{base_url}/db/WVLD/{id}` | 특정 파랑 하중 조회 |
| PUT | `{base_url}/db/WVLD/{id}` | 수정 |
| DELETE | `{base_url}/db/WVLD/{id}` | 삭제 |

### Parameters — 기본 설정

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Wave Load Name | `"NAME"` | String | - | Required |
| 2 | Description | `"DESC"` | String | - | Optional |
| 3 | Use Static Load Generation | `"bSTLD"` | Boolean | false | Optional |
| 4 | Use Time History Load Generation | `"bTHIS"` | Boolean | false | Optional |
| 5 | Time History Load Case Name | `"NAME_THIS"` | String | - | Optional |
| 6 | Vertical Coordinate (`"GLOBAL_X"` / `"GLOBAL_Y"` / `"GLOBAL_Z"`) | `"VERT_COORD"` | String | `"GLOBAL_Z"` | Required |
| 7 | Water Weight Density | `"DENSITY"` | Number | - | Required |
| 8 | Water Depth | `"DEPTH"` | Number | - | Required |
| 9 | Use Self Weight | `"bSELFW"` | Boolean | false | Optional |
| 10 | Use Buoyancy Load | `"bBUOYANT"` | Boolean | false | Optional |

### Parameters — COEF 객체 (항력·관성력 계수)

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|------------|----------|
| 1 | Type (`"CONST"` / `"GROUP"`) | `"TYPE"` | String | Required |
| 2 | Coefficients – Slender Element Array | `"COEF_S"` | Array [Object] | Optional |
| 3 | Coefficients – Rigid Element Array | `"COEF_R"` | Array [Object] | Optional |
| 4 | Override Coefficients with Structure Group | `"bOVER"` | Boolean | Optional |
| 5 | Override Slender Element Array | `"OVER_S"` | Array [Object] | Optional |
| 6 | Override Rigid Element Array | `"OVER_R"` | Array [Object] | Optional |

**COEF_S / COEF_R / OVER_S / OVER_R 항목 구조:**

| Key | Value Type | Description |
|-----|------------|-------------|
| `"GRUP"` | String | Structure Group Name |
| `"DIA"` | Number | Diameter |
| `"DRAG_COEF_X"` | Number | Drag Coefficient X |
| `"DRAG_COEF_Y"` | Number | Drag Coefficient Y |
| `"DRAG_COEF_Z"` | Number | Drag Coefficient Z |
| `"INER_COEF_X"` | Number | Inertia Coefficient X |
| `"INER_COEF_Y"` | Number | Inertia Coefficient Y |
| `"INER_COEF_Z"` | Number | Inertia Coefficient Z |

### Parameters — CHAR 객체 (파랑 특성)

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|------------|----------|
| 1 | Theory Type (`"AIRY"` / `"STOKES"` / `"STREAM"`) | `"THEORY"` | String | Required |
| 2 | Function Order (Stokes/Stream 이론에서 사용) | `"FUNC"` | Integer | Optional |
| 3 | Wave Direction (degrees) | `"DIR"` | Number | Required |
| 4 | Wave Height | `"HEIGHT"` | Number | Required |
| 5 | Wave Length / Wave Period 선택 (`"LENGTH"` / `"PERIOD"`) | `"CHAR_TYPE"` | String | Required |
| 6 | Wave Length | `"LENGTH"` | Number | Optional |
| 7 | Wave Period | `"PERIOD"` | Number | Optional |
| 8 | Kinematics Factor | `"K_FACTOR"` | Number | Optional |
| 9 | Current Surface Velocity | `"SURFACE_V"` | Number | Optional |
| 10 | Current Bottom Velocity | `"BOTTOM_Y"` | Number | Optional |

### Parameters — PROF 객체 (조류 프로파일)

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|------------|----------|
| 1 | Current Direction (degrees) | `"CUR_DIR"` | Number | Optional |
| 2 | Current Blockage Factor | `"CUR_FACTOR"` | Number | Optional |
| 3 | Grid Data (elevation × velocity points) | `"GRID_DATA"` | Array [Object] | Optional |

**GRID_DATA 항목 구조:**

| Key | Value Type | Description |
|-----|------------|-------------|
| `"D"` | Number | Elevation |
| `"V"` | Number | Velocity |

### Parameters — 기타 설정

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|------------|----------|
| 1 | Flood Condition (Structure Group Names) | `"FLOOD_GRUP"` | Array [String] | Optional |
| 2 | Marine Growth Data | `"GROWTH"` | Array [Object] | Optional |
| 3 | Grid X Size | `"GRID_X"` | Integer | Optional |
| 4 | Grid Z Size | `"GRID_Z"` | Integer | Optional |
| 5 | User Defined Grid Data (2D Array) | `"USERGRID"` | Array [Array [Object]] | Optional |
| 6 | Trajectory Grid Data (2D Array) | `"TRAJ"` | Array [Array [Object]] | Optional |
| 7 | Crest Critical Position (`"MAX"` / `"MANUAL"`) | `"CREST"` | String | Optional |
| 8 | Crest Position Unit | `"UNIT"` | String | Optional |
| 9 | Initial Position | `"INITAL_POS"` | Number | Optional |
| 10 | Increase Step | `"STEP"` | Number | Optional |
| 11 | Number of Positions | `"POS"` | Integer | Optional |

**GROWTH 항목 구조:**

| Key | Value Type | Description |
|-----|------------|-------------|
| `"Z"` | Number | Elevation |
| `"T"` | Number | Thickness |

**USERGRID / TRAJ 항목 구조 (각 격자점):**

| Key | Value Type | Description |
|-----|------------|-------------|
| `"X"` | Number | X 좌표 |
| `"Z"` | Number | Z 좌표 |
| `"ELEV"` | Number | Elevation |
| `"VX"` | Number | Velocity X |
| `"VCX"` | Number | Current Velocity X |
| `"VT"` | Number | Total Velocity |
| `"VZ"` | Number | Velocity Z |
| `"AX"` | Number | Acceleration X |
| `"AZ"` | Number | Acceleration Z |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "NAME": "WV_100Y",
      "DESC": "100-year return period wave",
      "bSTLD": true,
      "bTHIS": false,
      "NAME_THIS": "",
      "VERT_COORD": "GLOBAL_Z",
      "DENSITY": 10.05,
      "DEPTH": 30.0,
      "COEF": {
        "TYPE": "CONST",
        "COEF_S": [
          {
            "GRUP": "",
            "DIA": 0.5,
            "DRAG_COEF_X": 0.0,
            "DRAG_COEF_Y": 0.65,
            "DRAG_COEF_Z": 0.65,
            "INER_COEF_X": 0.0,
            "INER_COEF_Y": 2.0,
            "INER_COEF_Z": 2.0
          }
        ],
        "COEF_R": [],
        "bOVER": false,
        "OVER_S": [],
        "OVER_R": []
      },
      "CHAR": {
        "THEORY": "STOKES",
        "FUNC": 5,
        "DIR": 0.0,
        "HEIGHT": 12.5,
        "CHAR_TYPE": "PERIOD",
        "LENGTH": 0.0,
        "PERIOD": 14.0,
        "K_FACTOR": 1.0,
        "SURFACE_V": 0.5,
        "BOTTOM_Y": 0.1
      },
      "PROF": {
        "CUR_DIR": 0.0,
        "CUR_FACTOR": 0.9,
        "GRID_DATA": [
          {"D": 0.0,   "V": 0.5},
          {"D": -15.0, "V": 0.3},
          {"D": -30.0, "V": 0.1}
        ]
      },
      "FLOOD_GRUP": [],
      "GROWTH": [
        {"Z": 0.0,   "T": 0.05},
        {"Z": -10.0, "T": 0.08}
      ],
      "GRID_X": 10,
      "GRID_Z": 10,
      "bSELFW": true,
      "bBUOYANT": true,
      "CREST": "MAX",
      "UNIT": "m",
      "INITAL_POS": 0.0,
      "STEP": 1.0,
      "POS": 10
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

def create_wave_load():
    payload = {
        "Assign": {
            "1": {
                "NAME": "WV_100Y",
                "DESC": "100-year return period wave load",
                "bSTLD": True,          # 정적 하중 생성 사용
                "bTHIS": False,         # 시간이력 하중 생성 미사용
                "NAME_THIS": "",
                "VERT_COORD": "GLOBAL_Z",  # 수직 좌표축
                "DENSITY": 10.05,       # 물 단위중량 (kN/m³)
                "DEPTH": 30.0,          # 수심 (m)
                # 항력·관성력 계수
                "COEF": {
                    "TYPE": "CONST",    # 일정 계수 (CONST) 또는 구조그룹별 (GROUP)
                    "COEF_S": [
                        {
                            "GRUP": "",
                            "DIA": 0.5,           # 부재 직경
                            "DRAG_COEF_X": 0.0,
                            "DRAG_COEF_Y": 0.65,  # 항력 계수 Y
                            "DRAG_COEF_Z": 0.65,  # 항력 계수 Z
                            "INER_COEF_X": 0.0,
                            "INER_COEF_Y": 2.0,   # 관성력 계수 Y
                            "INER_COEF_Z": 2.0    # 관성력 계수 Z
                        }
                    ],
                    "COEF_R": [],
                    "bOVER": False,
                    "OVER_S": [],
                    "OVER_R": []
                },
                # 파랑 특성
                "CHAR": {
                    "THEORY": "STOKES",  # Airy / Stokes / Stream
                    "FUNC": 5,           # Stokes 5차
                    "DIR": 0.0,          # 파랑 진행 방향 (°)
                    "HEIGHT": 12.5,      # 파고 (m)
                    "CHAR_TYPE": "PERIOD",
                    "LENGTH": 0.0,
                    "PERIOD": 14.0,      # 파주기 (s)
                    "K_FACTOR": 1.0,     # 운동학적 계수
                    "SURFACE_V": 0.5,    # 표면 유속
                    "BOTTOM_Y": 0.1      # 저면 유속
                },
                # 조류 프로파일
                "PROF": {
                    "CUR_DIR": 0.0,
                    "CUR_FACTOR": 0.9,
                    "GRID_DATA": [
                        {"D": 0.0,   "V": 0.5},
                        {"D": -15.0, "V": 0.3},
                        {"D": -30.0, "V": 0.1}
                    ]
                },
                "FLOOD_GRUP": [],
                # 해양 성장 (Marine Growth)
                "GROWTH": [
                    {"Z": 0.0,   "T": 0.05},
                    {"Z": -10.0, "T": 0.08}
                ],
                "GRID_X": 10,
                "GRID_Z": 10,
                "bSELFW": True,      # 자중 포함
                "bBUOYANT": True,    # 부력 포함
                "CREST": "MAX",
                "UNIT": "m",
                "INITAL_POS": 0.0,
                "STEP": 1.0,
                "POS": 10
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/WVLD", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Wave Load created:", resp.json())

create_wave_load()
```

---

## 6. /db/IELC — Ignore Elements for Load Cases

특정 요소를 지정된 하중 케이스에서 무시하도록 설정합니다. 비선형 해석 등에서 특정 요소가 하중 전달에 참여하지 않도록 제어합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/IELC` | 무시 요소 설정 생성 |
| GET | `{base_url}/db/IELC` | 전체 조회 |
| GET | `{base_url}/db/IELC/{id}` | 특정 항목 조회 |
| PUT | `{base_url}/db/IELC/{id}` | 수정 |
| DELETE | `{base_url}/db/IELC/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Element ID | `"ELEMENT"` | Integer | - | Required |
| 2 | Load Case Name | `"LCNAME"` | String | - | Required |
| 3 | Ignore Option | `"OPT_IGNORE"` | Boolean | - | Required |

> **참고**: 각 레코드는 하나의 (요소, 하중케이스) 조합을 나타냅니다. 동일 요소에 여러 하중케이스를 무시하려면 레코드를 복수로 등록합니다.

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "ELEMENT": 5,
      "LCNAME": "DL",
      "OPT_IGNORE": true
    },
    "2": {
      "ELEMENT": 5,
      "LCNAME": "LL",
      "OPT_IGNORE": true
    },
    "3": {
      "ELEMENT": 18,
      "LCNAME": "DL",
      "OPT_IGNORE": false
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

def set_ignore_elements():
    payload = {
        "Assign": {
            "1": {
                "ELEMENT": 5,          # 요소 ID
                "LCNAME": "DL",        # 하중 케이스 이름
                "OPT_IGNORE": True     # true: 이 하중케이스에서 해당 요소 무시
            },
            "2": {
                "ELEMENT": 5,
                "LCNAME": "LL",
                "OPT_IGNORE": True
            },
            "3": {
                "ELEMENT": 18,
                "LCNAME": "DL",
                "OPT_IGNORE": False    # false: 무시 해제
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/IELC", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Ignore Elements set:", resp.json())

set_ignore_elements()
```

---

## 7. /db/IFGS — Large Displacement – Initial Forces for Geometric Stiffness

대변위(Large Displacement) 해석에서 기하학적 강성 행렬 계산에 사용될 초기 힘(Initial Force)을 요소별로 정의합니다. Assign Key는 요소(Element) ID입니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/IFGS` | 초기 힘 생성 |
| GET | `{base_url}/db/IFGS` | 전체 조회 |
| GET | `{base_url}/db/IFGS/{element_id}` | 특정 요소 조회 |
| PUT | `{base_url}/db/IFGS/{element_id}` | 수정 |
| DELETE | `{base_url}/db/IFGS/{element_id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Direction (`"GX"` / `"GY"` / `"GZ"` / `"AXIAL"`) | `"DIR"` | String | - | Required |
| 2 | Initial Force | `"INIT_FORCE"` | Number | - | Required |

> **참고**: Assign Key는 요소 번호(Element ID)입니다. `"DIR"`은 초기 힘의 작용 방향이며, `"AXIAL"`은 축방향을 의미합니다.

### Request Body (POST)

```json
{
  "Assign": {
    "9": {
      "DIR": "GY",
      "INIT_FORCE": 200
    },
    "16": {
      "DIR": "AXIAL",
      "INIT_FORCE": 10
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

def set_initial_forces_geometric_stiffness():
    payload = {
        "Assign": {
            # Key = Element ID
            "9": {
                "DIR": "GY",         # 전체 좌표계 Y 방향
                "INIT_FORCE": 200    # 초기 힘 (kN)
            },
            "16": {
                "DIR": "AXIAL",      # 부재 축방향
                "INIT_FORCE": 10
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/IFGS", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Initial Forces (Geometric Stiffness) set:", resp.json())

set_initial_forces_geometric_stiffness()
```

---

## 8. /db/EFCT — Small Displacement – Initial Force Control Data

소변위(Small Displacement) 해석에서의 초기 힘 제어 데이터를 정의합니다. 하중 케이스 또는 하중 조합을 초기 힘으로 설정하고, 기하학적 강성에 반영할지 여부를 제어합니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/EFCT` | 초기 힘 제어 데이터 생성 |
| GET | `{base_url}/db/EFCT` | 전체 조회 |
| GET | `{base_url}/db/EFCT/{id}` | 특정 항목 조회 |
| PUT | `{base_url}/db/EFCT/{id}` | 수정 |
| DELETE | `{base_url}/db/EFCT/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Use Add Initial Force to Element Force | `"bADDLC"` | Boolean | false | Optional |
| 2 | Load Case Name | `"LCNAME"` | String | - | Required |
| 3 | Use Initial Force Combination | `"bUSECOMB"` | Boolean | false | Optional |
| 4 | Initial Force Combination Cases | `"COMB_LIST"` | Array [Object] | - | Required |
| (1) | Load Case Name | `"LCNAME"` | String | - | Required |
| (2) | Scale Factor | `"FACTOR"` | Number | - | Required |
| 5 | Check to Reflect Initial Axial Forces into Geometric Stiffness | `"bCHECK_GEOM_STIFF"` | Boolean | false | Optional |

> **참고**:
> - `bADDLC = true`: 요소 힘에 초기 힘을 더합니다.
> - `bUSECOMB = true`: 단일 하중케이스(`LCNAME`) 대신 `COMB_LIST`의 조합을 초기 힘으로 사용합니다.
> - `bCHECK_GEOM_STIFF = true`: 초기 축력을 기하학적 강성 행렬에 반영합니다.

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "bADDLC": false,
      "LCNAME": "DL",
      "bUSECOMB": true,
      "COMB_LIST": [
        {
          "LCNAME": "DL",
          "FACTOR": 1.2
        },
        {
          "LCNAME": "LL",
          "FACTOR": 1.0
        }
      ],
      "bCHECK_GEOM_STIFF": false
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

def set_initial_force_control():
    payload = {
        "Assign": {
            "1": {
                "bADDLC": False,        # 요소 힘에 초기 힘 추가 여부
                "LCNAME": "DL",         # 기준 하중 케이스
                "bUSECOMB": True,       # 조합 사용 여부
                "COMB_LIST": [
                    {
                        "LCNAME": "DL",
                        "FACTOR": 1.2   # 하중케이스 스케일 팩터
                    },
                    {
                        "LCNAME": "LL",
                        "FACTOR": 1.0
                    }
                ],
                # 초기 축력을 기하학적 강성에 반영
                "bCHECK_GEOM_STIFF": False
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/EFCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Initial Force Control Data set:", resp.json())

set_initial_force_control()
```

---

## 9. /db/INMF — Small Displacement – Initial Element Force

소변위 해석에서 요소별 초기 힘(Initial Element Force)을 직접 지정합니다. 요소 타입에 따라 힘 배열의 크기가 다릅니다.

### HTTP Methods

| Method | URL | 설명 |
|--------|-----|------|
| POST | `{base_url}/db/INMF` | 초기 요소 힘 생성 |
| GET | `{base_url}/db/INMF` | 전체 조회 |
| GET | `{base_url}/db/INMF/{id}` | 특정 항목 조회 |
| PUT | `{base_url}/db/INMF/{id}` | 수정 |
| DELETE | `{base_url}/db/INMF/{id}` | 삭제 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Element Type | `"ELEM_TYPE"` | String | - | Required |
| 2 | Element ID | `"ELEM_KEY"` | Integer | - | Required |
| 3 | Element Forces | `"ELEMENT_FORCES"` | Array [Number] | - | Required |

**ELEM_TYPE 값:**

| Value | Description |
|-------|-------------|
| `"BEAM"` | 보(Beam) 요소 |
| `"TRUSS"` | 트러스(Truss) 요소 |
| `"E-LINK"` | Elastic Link 요소 |
| `"G-LINK"` | General Link 요소 |

**ELEMENT_FORCES 배열 구조 (요소 타입별):**

| ELEM_TYPE | 배열 크기 | 순서 |
|-----------|-----------|------|
| `"BEAM"` | 12 | Axial-i, Vy-i, Vz-i, Torsion-i, My-i, Mz-i, Axial-j, Vy-j, Vz-j, Torsion-j, My-j, Mz-j |
| `"TRUSS"` | 2 | Axial-i, Axial-j |
| `"E-LINK"` | 12 | Axial-i, Vy-i, Vz-i, Torsion-i, My-i, Mz-i, Axial-j, Vy-j, Vz-j, Torsion-j, My-j, Mz-j |
| `"G-LINK"` | 12 | Axial-i, Vy-i, Vz-i, Torsion-i, My-i, Mz-i, Axial-j, Vy-j, Vz-j, Torsion-j, My-j, Mz-j |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "ELEM_TYPE": "BEAM",
      "ELEM_KEY": 15,
      "ELEMENT_FORCES": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    },
    "2": {
      "ELEM_TYPE": "TRUSS",
      "ELEM_KEY": 112,
      "ELEMENT_FORCES": [1, 2]
    },
    "3": {
      "ELEM_TYPE": "E-LINK",
      "ELEM_KEY": 1,
      "ELEMENT_FORCES": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    },
    "4": {
      "ELEM_TYPE": "G-LINK",
      "ELEM_KEY": 1,
      "ELEMENT_FORCES": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
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

def set_initial_element_forces():
    payload = {
        "Assign": {
            # Assign Key: 레코드 순번 (요소 ID가 아님)
            "1": {
                "ELEM_TYPE": "BEAM",  # 보 요소
                "ELEM_KEY": 15,       # 요소 ID
                # [Axial-i, Vy-i, Vz-i, T-i, My-i, Mz-i,
                #  Axial-j, Vy-j, Vz-j, T-j, My-j, Mz-j]
                "ELEMENT_FORCES": [100, 0, 50, 0, 200, 0, -100, 0, -50, 0, -200, 0]
            },
            "2": {
                "ELEM_TYPE": "TRUSS",  # 트러스 요소
                "ELEM_KEY": 112,
                # [Axial-i, Axial-j]
                "ELEMENT_FORCES": [150, -150]
            },
            "3": {
                "ELEM_TYPE": "E-LINK",  # Elastic Link
                "ELEM_KEY": 1,
                "ELEMENT_FORCES": [10, 0, 0, 0, 0, 0, -10, 0, 0, 0, 0, 0]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/INMF", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Initial Element Forces set:", resp.json())

# 특정 요소 초기 힘 조회
def get_initial_element_force(record_id: int):
    resp = requests.get(f"{BASE_URL}/db/INMF/{record_id}", headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

set_initial_element_forces()
```

---

## End-to-End 워크플로우 예제

침하 해석 및 기타 하중 설정 전체 흐름: **SMPT → SMLC → PLCB → LDSQ → WVLD → IELC → EFCT → INMF**

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

# Step 1: 침하 그룹 정의
post("/db/SMPT", {"Assign": {
    "1": {"NAME": "SG1", "SETTLE": 25, "ITEMS": [100, 101]},
    "2": {"NAME": "SG2", "SETTLE": 15, "ITEMS": [102, 103]}
}})

# Step 2: 침하 하중 케이스 정의
post("/db/SMLC", {"Assign": {
    "1": {
        "NAME": "SLC1",
        "DESC": "",
        "FACTOR": 1.0,
        "MIN": 1,
        "MAX": 2,
        "ST_GROUPS": ["SG1", "SG2"]
    }
}})

# Step 3: Pre-composite 하중 케이스 설정
post("/db/PLCB", {"Assign": {
    "1": {"LCNAME_ITEM": ["DL(BC)1", "DL(BC)2"]}
}})

# Step 4: 비선형 하중 순서 설정
post("/db/LDSQ", {"Assign": {
    "1": {"LCNAME_ITEM": ["DL", "LL", "SLC1"]}
}})

# Step 5: 파랑 하중 정의
post("/db/WVLD", {"Assign": {
    "1": {
        "NAME": "WV_OPE",
        "DESC": "Operating wave",
        "bSTLD": True,
        "bTHIS": False,
        "NAME_THIS": "",
        "VERT_COORD": "GLOBAL_Z",
        "DENSITY": 10.05,
        "DEPTH": 30.0,
        "COEF": {
            "TYPE": "CONST",
            "COEF_S": [{"GRUP": "", "DIA": 0.5,
                        "DRAG_COEF_X": 0.0, "DRAG_COEF_Y": 0.65, "DRAG_COEF_Z": 0.65,
                        "INER_COEF_X": 0.0, "INER_COEF_Y": 2.0, "INER_COEF_Z": 2.0}],
            "COEF_R": [], "bOVER": False, "OVER_S": [], "OVER_R": []
        },
        "CHAR": {
            "THEORY": "AIRY", "FUNC": 1,
            "DIR": 0.0, "HEIGHT": 5.0,
            "CHAR_TYPE": "PERIOD", "LENGTH": 0.0, "PERIOD": 8.0,
            "K_FACTOR": 1.0, "SURFACE_V": 0.3, "BOTTOM_Y": 0.05
        },
        "PROF": {"CUR_DIR": 0.0, "CUR_FACTOR": 1.0, "GRID_DATA": []},
        "FLOOD_GRUP": [], "GROWTH": [],
        "GRID_X": 5, "GRID_Z": 5,
        "bSELFW": True, "bBUOYANT": True,
        "CREST": "MAX", "UNIT": "m",
        "INITAL_POS": 0.0, "STEP": 1.0, "POS": 5
    }
}})

# Step 6: 특정 요소 하중케이스 무시 설정
post("/db/IELC", {"Assign": {
    "1": {"ELEMENT": 5, "LCNAME": "WV_OPE", "OPT_IGNORE": True}
}})

# Step 7: 소변위 초기 힘 제어 설정
post("/db/EFCT", {"Assign": {
    "1": {
        "bADDLC": False,
        "LCNAME": "DL",
        "bUSECOMB": False,
        "COMB_LIST": [],
        "bCHECK_GEOM_STIFF": True
    }
}})

# Step 8: 초기 요소 힘 지정
post("/db/INMF", {"Assign": {
    "1": {
        "ELEM_TYPE": "BEAM",
        "ELEM_KEY": 15,
        "ELEMENT_FORCES": [100, 0, 50, 0, 200, 0, -100, 0, -50, 0, -200, 0]
    }
}})

print("\nAll Settlement & Miscellaneous Load settings applied successfully.")
```

---

*다음 파트: [12_DB_Analysis_Control.md](12_DB_Analysis_Control.md)*
