# 03 DB — Node / Element

> **Source**: [MIDAS API Online Manual](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **Sync date**: 2026-06-29  
> **Endpoints covered**: `/db/NODE`, `/db/ELEM`, `/db/SKEW`, `/db/MADO`, `/db/SBDO`, `/db/DOEL`

---

## Table of Contents

| No. | Endpoint | 기능 | Methods |
|-----|----------|------|---------|
| 1 | [`/db/NODE`](#1-dbnode) | Node | POST, GET, PUT, DELETE |
| 2 | [`/db/ELEM`](#2-dbelem) | Element | POST, GET, PUT, DELETE |
| 3 | [`/db/SKEW`](#3-dbskew) | Node Local Axis | POST, GET, PUT, DELETE |
| 4 | [`/db/MADO`](#4-dbmado) | Define Domain | POST, GET, PUT, DELETE |
| 5 | [`/db/SBDO`](#5-dbsbdo) | Define Sub-Domain | POST, GET, PUT, DELETE |
| 6 | [`/db/DOEL`](#6-dbdoel) | Domain-Element | POST, GET, PUT, DELETE |

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

## 1. `/db/NODE`

> **Node** — 절점(노드)의 전체 좌표계(Global) 좌표를 정의합니다.

- **URL**: `{base url}/db/NODE`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Node ↗](https://support.midasuser.com/hc/en-us/articles/35806845654169)

### JSON Schema

```json
{
  "NODE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "X": { "description": "GLOBAL X-POSITION", "type": "number" },
      "Y": { "description": "GLOBAL Y-POSITION", "type": "number" },
      "Z": { "description": "GLOBAL Z-POSITION", "type": "number" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Coordinates - x | `"X"` | Number | 0 | Optional |
| 2 | Coordinates - y | `"Y"` | Number | 0 | Optional |
| 3 | Coordinates - z | `"Z"` | Number | 0 | Optional |

### Request Body (Assign)

```json
{
  "Assign": {
    "1": { "X": -1, "Y": -1, "Z": -1 },
    "2": { "X": -2, "Y": -2, "Z": -2 },
    "3": { "X": -3, "Y": -3, "Z": -3 }
  }
}
```

### Python 예제

```python
# --- GET: 전체 절점 조회 ---
result = midas_api("GET", "/db/NODE")
nodes = result.get("NODE", {})
print(f"총 절점 수: {len(nodes)}")

# --- POST: 절점 생성 ---
# 절점 ID를 키로, 좌표를 값으로 지정
node_data = {
    "Assign": {
        "1": {"X": 0.0, "Y": 0.0, "Z": 0.0},
        "2": {"X": 6.0, "Y": 0.0, "Z": 0.0},
        "3": {"X": 6.0, "Y": 0.0, "Z": 4.0},
        "4": {"X": 0.0, "Y": 0.0, "Z": 4.0},
    }
}
midas_api("POST", "/db/NODE", node_data)

# --- PUT: 절점 수정 ---
update_data = {
    "Assign": {
        "2": {"X": 7.0, "Y": 0.0, "Z": 0.0}  # 2번 절점 X 좌표 변경
    }
}
midas_api("PUT", "/db/NODE", update_data)

# --- DELETE: 절점 삭제 ---
delete_data = {"Assign": {"4": None}}
midas_api("DELETE", "/db/NODE", delete_data)
```

### 고급 예제 — 격자 절점 자동 생성

```python
def create_grid_nodes(nx, ny, nz, dx, dy, dz, start_id=1):
    """
    3D 격자 절점 생성
    
    Args:
        nx, ny, nz: X, Y, Z 방향 분할 수 (절점 수 = (nx+1)*(ny+1)*(nz+1))
        dx, dy, dz: X, Y, Z 방향 간격
        start_id: 시작 절점 번호
    
    Returns:
        Assign dict for /db/NODE
    """
    assign = {}
    node_id = start_id
    for k in range(nz + 1):
        for j in range(ny + 1):
            for i in range(nx + 1):
                assign[str(node_id)] = {
                    "X": i * dx,
                    "Y": j * dy,
                    "Z": k * dz
                }
                node_id += 1
    return {"Assign": assign}

# 예시: 3칸 × 1칸 × 4층 (6m 경간, 6m 경간, 3m 층고)
node_body = create_grid_nodes(nx=3, ny=1, nz=4, dx=6.0, dy=6.0, dz=3.0)
print(f"생성된 절점 수: {len(node_body['Assign'])}")  # (3+1)*(1+1)*(4+1) = 40
midas_api("POST", "/db/NODE", node_body)
```

---

## 2. `/db/ELEM`

> **Element** — 요소(부재)를 정의합니다. BEAM, TRUSS, TENSTR, COMPTR, PLATE, WALL, PLSTRS, PLSTRN, AXISYM, SOLID 등 10가지 요소 유형을 지원합니다.

- **URL**: `{base url}/db/ELEM`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Element ↗](https://support.midasuser.com/hc/en-us/articles/35806934300825)

### JSON Schema

```json
{
  "ELEM": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "TYPE":    { "description": "ELEMENT TYPE",            "type": "string" },
      "MATL":    { "description": "MATERIAL NUM",            "type": "integer" },
      "SECT":    { "description": "SECTION NUM",             "type": "integer" },
      "NODE":    { "description": "NODE NUM",                "type": "array", "items": { "type": "integer", "maxItems": 8 } },
      "ANGLE":   { "description": "ELEMENT ANGLE",          "type": "number" },
      "STYPE":   { "description": "ELEMENT SUBTYPE",        "type": "integer" },
      "TENS":    { "description": "TENS FORCE",              "type": "number" },
      "T_LIMIT": { "description": "TENS LIMIT",             "type": "number" },
      "T_bLMT":  { "description": "USE TENS LIMIT?",        "type": "boolean" },
      "NON_LEN": { "description": "NON LINEAR LENGTH",      "type": "number" },
      "CABLE":   { "description": "CABLE OPTION",           "type": "integer" },
      "C_RAT":   { "description": "CABLE LENGTH RATIO",     "type": "number" },
      "WALL":    { "description": "WALL ID",                "type": "integer" },
      "W_CON":   { "description": "CONNECTED NODE NUM",     "type": "integer" },
      "W_TYPE":  { "description": "WALL TYPE",              "type": "integer" },
      "LCAXIS":  { "description": "LOCAL AXIS",             "type": "integer" }
    }
  }
}
```

### Specifications

#### 공통 키 (Common Keys) + Solid

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Element Type ¹⁾ | `"TYPE"` | String | `"BEAM"` | Optional |
| 2 | Material No. | `"MATL"` | Integer | - | **Required** |
| 3 | Section / Thickness No. | `"SECT"` | Integer | - | **Required** |
| 4 | Node No. ²⁾ | `"NODE"` | Array[Integer] | - | **Required** |

#### Beam, Truss, Plane Strain, Axisymmetric

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |

#### Tension only — Truss (STYPE: 1)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Truss: 1 | `"STYPE"` | Integer | - | **Required** |
| 7 | Allowable Compression (Negative Value Only) | `"TENS"` | Number | 0 | Optional |
| 8 | Tension Limit Value (Positive Value Only) | `"T_LIMIT"` | Number | 0 | Optional |
| 9 | Tension Limit | `"T_bLMT"` | Boolean | false | Optional |

#### Tension only — Hook (STYPE: 2)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Hook: 2 | `"STYPE"` | Integer | - | **Required** |
| 7 | Hook Length | `"NON_LEN"` | Number | 0 | Optional |

#### Tension only — Cable (STYPE: 3)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Cable: 3 | `"STYPE"` | Integer | - | **Required** |
| 7 | Cable Type • Pretension: 1 • Horizontal: 2 • Lu: 3 | `"CABLE"` | Integer | - | **Required** |
| 8 | Pretension / Horizontal | `"TENS"` | Number | 0 | Optional |
| 9 | Lu (Range: 0.5~1.5) | `"NON_LEN"` | Number | - | **Required** |

#### Compression only — Truss (STYPE: 1)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Truss: 1 | `"STYPE"` | Integer | - | **Required** |
| 7 | Allowable Tension (Positive Value Only) | `"TENS"` | Number | 0 | Optional |
| 8 | Compression Limit | `"T_bLMT"` | Boolean | false | Optional |
| 9 | Compression Limit Value (Negative Value Only) | `"T_LIMIT"` | Number | - | Optional |

#### Compression only — Gap (STYPE: 2)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Gap: 2 | `"STYPE"` | Integer | - | **Required** |
| 7 | Gap | `"NON_LEN"` | Number | 0 | Optional |

#### Wall

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Membrane: 1 • Plate: 2 | `"STYPE"` | Integer | - | **Required** |
| 7 | Wall ID | `"WALL"` | Integer | - | **Required** |
| 8 | Orientation • Beta Angle: 0 • Ref Point: 1 • Ref Vector: 2 | `"W_CON"` | Integer | - | **Required** |
| 9 | Wall Type • Plate base: 0 • CRB-Pin: 1 • CRB-Fixed: 2 | `"W_TYPE"` | Integer | 0 | Optional |

#### Plate

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Thick: 1 • Thin: 2 • Thick+Drilling DOF: 3 • Thin+Drilling DOF: 4 | `"STYPE"` | Integer | - | **Required** |

#### Plane Stress

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Drilling DOF Inactive: 1 • Drilling DOF Active: 2 | `"STYPE"` | Integer | - | **Required** |

### 요소 유형 코드표 ¹⁾

| No. | Element Type | `"TYPE"` |
|-----|--------------|----------|
| 1 | General Beam / Tapered Beam | `"BEAM"` |
| 2 | Truss | `"TRUSS"` |
| 3 | Tension only / Hook / Cable | `"TENSTR"` |
| 4 | Compression only / Gap | `"COMPTR"` |
| 5 | Plate | `"PLATE"` |
| 6 | Wall | `"WALL"` |
| 7 | Plane stress | `"PLSTRS"` |
| 8 | Plane strain | `"PLSTRN"` |
| 9 | Axisymmetric | `"AXISYM"` |
| 10 | Solid | `"SOLID"` |

### 절점 수 요약 ²⁾

| Element Type | Min Nodes | Max Nodes | Notes |
|--------------|-----------|-----------|-------|
| BEAM, TRUSS, TENSTR, COMPTR | 2 | 2 | - |
| PLATE, PLSTRS, PLSTRN, AXISYM | 3 | 4 | Triangle or Quad |
| WALL | 4 | 4 | Quad only |
| SOLID | 4 | 8 | Tet(4), Wedge(6), Hex(8) |

### Request Body 예제

#### BEAM

```json
{
  "Assign": {
    "198": {
      "TYPE": "BEAM",
      "MATL": 1,
      "SECT": 1,
      "NODE": [30, 74],
      "ANGLE": 0
    }
  }
}
```

#### TRUSS

```json
{
  "Assign": {
    "13": {
      "TYPE": "TRUSS",
      "MATL": 1,
      "SECT": 1,
      "NODE": [24, 25],
      "ANGLE": 0
    }
  }
}
```

#### TENSTR (Cable)

```json
{
  "Assign": {
    "6": {
      "TYPE": "TENSTR",
      "MATL": 1,
      "SECT": 1,
      "NODE": [11, 12],
      "ANGLE": 0,
      "STYPE": 3,
      "TENS": 0.5,
      "CABLE": 1
    }
  }
}
```

#### COMPTR (Truss)

```json
{
  "Assign": {
    "22": {
      "TYPE": "COMPTR",
      "MATL": 1,
      "SECT": 1,
      "NODE": [50, 51],
      "ANGLE": 0,
      "STYPE": 1,
      "TENS": 27,
      "T_LIMIT": -15,
      "T_bLMT": true
    }
  }
}
```

#### PLATE (Quad, Thick)

```json
{
  "Assign": {
    "30": {
      "TYPE": "PLATE",
      "MATL": 1,
      "SECT": 1,
      "NODE": [56, 69, 70, 57],
      "ANGLE": 0,
      "STYPE": 1
    }
  }
}
```

#### WALL

```json
{
  "Assign": {
    "1": {
      "TYPE": "WALL",
      "MATL": 1,
      "SECT": 1,
      "NODE": [1, 2, 4, 3],
      "STYPE": 1,
      "WALL": 1,
      "W_CON": 0,
      "W_TYPE": 0
    }
  }
}
```

#### SOLID (Hexahedral, 8-node)

```json
{
  "Assign": {
    "42": {
      "TYPE": "SOLID",
      "MATL": 1,
      "SECT": 0,
      "NODE": [27, 6, 7, 28, 113, 107, 108, 114]
    }
  }
}
```

### Python 예제

```python
# --- GET: 전체 요소 조회 ---
result = midas_api("GET", "/db/ELEM")
elems = result.get("ELEM", {})
print(f"총 요소 수: {len(elems)}")

# 요소 유형별 집계
from collections import Counter
type_count = Counter(e["TYPE"] for e in elems.values())
print(dict(type_count))

# --- POST: 보(BEAM) 요소 생성 ---
beam_data = {
    "Assign": {
        "1": {"TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0},
        "2": {"TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [3, 4], "ANGLE": 0},
    }
}
midas_api("POST", "/db/ELEM", beam_data)

# --- DELETE: 특정 요소 삭제 ---
delete_data = {"Assign": {"5": None}}
midas_api("DELETE", "/db/ELEM", delete_data)
```

### 고급 예제 — 라멘 골조 자동 생성

```python
def create_moment_frame(
    n_bays_x: int,
    n_stories: int,
    bay_width: float,
    story_height: float,
    col_matl: int,
    col_sect: int,
    beam_matl: int,
    beam_sect: int,
    node_start_id: int = 1,
    elem_start_id: int = 1
):
    """
    2D 라멘 골조 (Moment Frame) 절점 및 보/기둥 요소 자동 생성
    
    Args:
        n_bays_x: X 방향 경간 수
        n_stories: 층 수
        bay_width: 경간 폭 (m)
        story_height: 층고 (m)
        col_matl/col_sect: 기둥 재료/단면 번호
        beam_matl/beam_sect: 보 재료/단면 번호
    
    Returns:
        (node_body, elem_body) tuple for /db/NODE and /db/ELEM
    """
    n_cols = n_bays_x + 1  # 기둥 수 (X 방향)
    
    # 절점 생성 (Y=0 평면)
    nodes = {}
    nid = node_start_id
    node_map = {}  # (i_col, i_story) -> node_id
    for i_story in range(n_stories + 1):  # 0층 ~ n_stories층
        for i_col in range(n_cols):
            nodes[str(nid)] = {
                "X": i_col * bay_width,
                "Y": 0.0,
                "Z": i_story * story_height
            }
            node_map[(i_col, i_story)] = nid
            nid += 1
    
    # 요소 생성
    elems = {}
    eid = elem_start_id
    
    # 기둥 (Column): 각 층의 수직 부재
    for i_story in range(n_stories):
        for i_col in range(n_cols):
            n_bot = node_map[(i_col, i_story)]
            n_top = node_map[(i_col, i_story + 1)]
            elems[str(eid)] = {
                "TYPE": "BEAM",
                "MATL": col_matl,
                "SECT": col_sect,
                "NODE": [n_bot, n_top],
                "ANGLE": 0
            }
            eid += 1
    
    # 보 (Beam): 각 층의 수평 부재
    for i_story in range(1, n_stories + 1):  # 1층 ~ n_stories층
        for i_bay in range(n_bays_x):
            n_left = node_map[(i_bay, i_story)]
            n_right = node_map[(i_bay + 1, i_story)]
            elems[str(eid)] = {
                "TYPE": "BEAM",
                "MATL": beam_matl,
                "SECT": beam_sect,
                "NODE": [n_left, n_right],
                "ANGLE": 0
            }
            eid += 1
    
    node_body = {"Assign": nodes}
    elem_body = {"Assign": elems}
    
    n_nodes = len(nodes)
    n_elems = len(elems)
    n_cols_total = n_cols * n_stories
    n_beams_total = n_bays_x * n_stories
    print(f"생성: 절점 {n_nodes}개, 요소 {n_elems}개 (기둥 {n_cols_total}개, 보 {n_beams_total}개)")
    
    return node_body, elem_body


# 사용 예시: 3경간 × 5층 라멘 골조 (경간 6m, 층고 3.5m)
node_body, elem_body = create_moment_frame(
    n_bays_x=3, n_stories=5,
    bay_width=6.0, story_height=3.5,
    col_matl=1, col_sect=1,
    beam_matl=1, beam_sect=2
)

midas_api("POST", "/db/NODE", node_body)
midas_api("POST", "/db/ELEM", elem_body)
```

---

## 3. `/db/SKEW`

> **Node Local Axis** — 절점 국부 좌표계를 정의합니다. 4가지 입력 방법(Angle, 3 Points, Vector, Line Vector)을 지원합니다.

- **URL**: `{base url}/db/SKEW`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Node Local Axis ↗](https://support.midasuser.com/hc/en-us/articles/35807178748569)

### JSON Schema

```json
{
  "SKEW": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "iMETHOD": { "description": "Input method",       "type": "integer" },
      "ANGLE_X":  { "description": "Angle x",           "type": "number" },
      "ANGLE_Y":  { "description": "Angle y",           "type": "number" },
      "ANGLE_Z":  { "description": "Angle z",           "type": "number" },
      "P0X":      { "description": "Point Coordinate x", "type": "number" },
      "P0Y":      { "description": "Point Coordinate y", "type": "number" },
      "P0Z":      { "description": "Point Coordinate z", "type": "number" },
      "P1X":      { "description": "Point Coordinate x", "type": "number" },
      "P1Y":      { "description": "Point Coordinate y", "type": "number" },
      "P1Z":      { "description": "Point Coordinate z", "type": "number" },
      "P2X":      { "description": "Point Coordinate x", "type": "number" },
      "P2Y":      { "description": "Point Coordinate y", "type": "number" },
      "P2Z":      { "description": "Point Coordinate z", "type": "number" },
      "V1X":      { "description": "Direction Vector x", "type": "number" },
      "V1Y":      { "description": "Direction Vector y", "type": "number" },
      "V1Z":      { "description": "Direction Vector z", "type": "number" },
      "V2X":      { "description": "Direction Vector x", "type": "number" },
      "V2Y":      { "description": "Direction Vector y", "type": "number" },
      "V2Z":      { "description": "Direction Vector z", "type": "number" },
      "LV0X":     { "description": "Direction Vector x", "type": "number" },
      "LV0Y":     { "description": "Direction Vector y", "type": "number" },
      "LV0Z":     { "description": "Direction Vector z", "type": "number" },
      "LV1X":     { "description": "Direction Vector x", "type": "number" },
      "LV1Y":     { "description": "Direction Vector y", "type": "number" },
      "LV1Z":     { "description": "Direction Vector z", "type": "number" },
      "LV2X":     { "description": "Direction Vector x", "type": "number" },
      "LV2Y":     { "description": "Direction Vector y", "type": "number" },
      "LV2Z":     { "description": "Direction Vector z", "type": "number" },
      "REFTYPE":  { "description": "Reference Type",    "type": "integer" },
      "G_DIR":    { "description": "Global Direction",  "type": "integer" },
      "L_DIR":    { "description": "Local Direction",   "type": "integer" }
    }
  }
}
```

### Specifications

#### iMETHOD = 1 (Angle)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Input Method • Angle: 1 | `"iMETHOD"` | Integer | - | Optional |
| 2 | About x | `"ANGLE_X"` | Number | 0 | Optional |
| 3 | About y | `"ANGLE_Y"` | Number | 0 | Optional |
| 4 | About z | `"ANGLE_Z"` | Number | 0 | Optional |

#### iMETHOD = 2 (3 Points)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Input Method • 3 Points: 2 | `"iMETHOD"` | Integer | - | Optional |
| 2~4 | P0 Coordinate (x, y, z) | `"P0X"` `"P0Y"` `"P0Z"` | Number | 0 | Optional |
| 5~7 | P1 Coordinate (x, y, z) | `"P1X"` `"P1Y"` `"P1Z"` | Number | 0 | Optional |
| 8~10 | P2 Coordinate (x, y, z) | `"P2X"` `"P2Y"` `"P2Z"` | Number | 0 | Optional |

#### iMETHOD = 3 (Vector)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Input Method • Vector: 3 | `"iMETHOD"` | Integer | - | Optional |
| 2~4 | Direction Vector V1 (x, y, z) | `"V1X"` `"V1Y"` `"V1Z"` | Number | 0 | Optional |
| 5~7 | Direction Vector V2 (x, y, z) | `"V2X"` `"V2Y"` `"V2Z"` | Number | 0 | Optional |

#### iMETHOD = 4 (Line Vector)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Input Method • Line Vector: 4 | `"iMETHOD"` | Integer | - | Optional |
| 2~4 | Direction Vector V0 (x, y, z) | `"LV0X"` `"LV0Y"` `"LV0Z"` | Number | 0 | Optional |
| 5~7 | Direction Vector V1 (x, y, z) | `"LV1X"` `"LV1Y"` `"LV1Z"` | Number | 0 | Optional |
| 8~10 | Direction Vector V2 (x, y, z) | `"LV2X"` `"LV2Y"` `"LV2Z"` | Number | 0 | Optional |
| 11 | Reference Type • Ref. Point: 1 (P0, P1 required) • Global Direction: 2 (P0 required) | `"REFTYPE"` | Integer | - | **Required** |
| 12 | Global Direction • Global X: 0 • Global Y: 1 • Global Z: 2 | `"G_DIR"` | Integer | - | **Required** |
| 13 | Local Direction • Local x: 0 • Local y: 1 • Local z: 2 | `"L_DIR"` | Integer | - | **Required** |

### Request Body 예제

#### Method 1 — Angle

```json
{
  "Assign": {
    "1": {
      "iMETHOD": 1,
      "ANGLE_X": 45,
      "ANGLE_Y": 0,
      "ANGLE_Z": 90
    }
  }
}
```

#### Method 2 — 3 Points

```json
{
  "Assign": {
    "2": {
      "iMETHOD": 2,
      "P0X": 130, "P0Y": 3.35, "P0Z": 0,
      "P1X": 127, "P1Y": 3.35, "P1Z": 0,
      "P2X": 127, "P2Y": -3.35, "P2Z": 0
    }
  }
}
```

#### Method 3 — Vector

```json
{
  "Assign": {
    "3": {
      "iMETHOD": 3,
      "V1X": 0, "V1Y": -2.95, "V1Z": 0,
      "V2X": -3, "V2Y": 0, "V2Z": 0
    }
  }
}
```

### Python 예제

```python
# 절점 국부 좌표계 설정 (Angle 방식)
# 사용 예: 경사진 교각 기초 절점에 국부 좌표계 적용
skew_data = {
    "Assign": {
        "5": {
            "iMETHOD": 1,
            "ANGLE_X": 0,
            "ANGLE_Y": 0,
            "ANGLE_Z": 30  # Z축 기준 30° 회전
        }
    }
}
midas_api("POST", "/db/SKEW", skew_data)

# 조회 및 확인
result = midas_api("GET", "/db/SKEW")
print(f"정의된 국부 좌표계 수: {len(result.get('SKEW', {}))}")
```

---

## 4. `/db/MADO`

> **Define Domain** — 메시 도메인(Main Domain)을 정의합니다. Plane Stress, Plate, Plane Strain, Axisymmetric 요소 유형에 대한 도메인을 설정합니다.

- **URL**: `{base url}/db/MADO`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Define Domain ↗](https://support.midasuser.com/hc/en-us/articles/35807228332825)

### JSON Schema

```json
{
  "MADO": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":     { "description": "Domain Name",      "type": "string" },
      "TYPE":     { "description": "Element Type",     "type": "integer" },
      "MATL":     { "description": "Element Material", "type": "integer" },
      "PROP":     { "description": "Element Property", "type": "integer" },
      "SUB_TYPE": { "description": "Sub Type",         "type": "integer" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Domain Name | `"NAME"` | String | - | **Required** |
| 2 | Element Type • Plane Stress: 3 • Plate: 4 • Plane Strain: 6 • Axisymmetric: 7 | `"TYPE"` | Integer | - | **Required** |
| 3 | Material ID | `"MATL"` | Integer | - | **Required** |
| 4 | Element Property | `"PROP"` | Integer | - | **Required** |
| 5 | Sub Type | `"SUB_TYPE"` | Integer | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "DM1",
      "TYPE": 4,
      "MATL": 0,
      "PROP": 0,
      "SUB_TYPE": 2
    }
  }
}
```

### Python 예제

```python
# Plate 도메인 생성
domain_data = {
    "Assign": {
        "1": {
            "NAME": "SLAB_DOMAIN",
            "TYPE": 4,      # Plate
            "MATL": 1,      # 재료 1번
            "PROP": 1,      # 두께 속성 1번
            "SUB_TYPE": 1   # 서브타입
        }
    }
}
midas_api("POST", "/db/MADO", domain_data)

# 전체 도메인 조회
result = midas_api("GET", "/db/MADO")
domains = result.get("MADO", {})
for did, d in domains.items():
    print(f"Domain {did}: {d['NAME']} (TYPE={d['TYPE']})")
```

---

## 5. `/db/SBDO`

> **Define Sub-Domain** — 도메인 내 Sub-Domain을 정의합니다. 철근 방향, 부재 유형, 기본 철근 배근 등을 설정합니다. **GEN NX**와 **CIVIL NX**에서 일부 파라미터가 다릅니다.

- **URL**: `{base url}/db/SBDO`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Define Sub-Domain ↗](https://support.midasuser.com/hc/en-us/articles/35807304820761)

### JSON Schema

```json
{
  "SBDO": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "SUB_DOMAIN_NAME":  { "description": "Sub Domain Name",       "type": "string" },
      "MEMBER_TYPE":      { "description": "Member Type",           "type": "integer" },
      "V1":               { "description": "V1",                    "type": "number" },
      "V2":               { "description": "V2",                    "type": "number" },
      "DOMAIN_NAME":      { "description": "Domain Name",          "type": "string" },
      "bUseMt":           { "description": "Use Mt",               "type": "boolean" },
      "THICKNESS":        { "description": "Thickness",            "type": "number" },
      "OPT_BASIC_REBAR":  { "description": "Basic Rebar Boolean",  "type": "boolean" },
      "TOP_REBAR_NAME_X": { "description": "Top Rebar Name: X-Dir","type": "string" },
      "TOP_REBAR_SPACE_X":{ "description": "Top Rebar Space: X-Dir","type": "number" },
      "BOTTOM_REBAR_NAME_X":  { "description": "Bottom Rebar Name: X-Dir",  "type": "string" },
      "BOTTOM_REBAR_SPACE_X": { "description": "Bottom Rebar Space: X-Dir", "type": "number" },
      "TOP_REBAR_NAME_Y": { "description": "Top Rebar Name: Y-Dir","type": "string" },
      "TOP_REBAR_SPACE_Y":{ "description": "Top Rebar Space: Y-Dir","type": "number" },
      "BOTTOM_REBAR_NAME_Y":  { "description": "Bottom Rebar Name: Y-Dir",  "type": "string" },
      "BOTTOM_REBAR_SPACE_Y": { "description": "Bottom Rebar Space: Y-Dir", "type": "number" },
      "AXIS_VECTOR":      { "description": "Axis Vector",          "type": "array", "items": { "type": "number" } },
      "OPT_REBAR_MATL":   { "description": "Rebar Material Boolean","type": "boolean" },
      "REBAR_MATL_KEY":   { "description": "Rebar Material Key",   "type": "integer" },
      "REBAR_AXIS_TYPE":  { "description": "Rebar Axis Type",      "type": "integer" },
      "STR_UCS":          { "description": "UCS",                  "type": "string" },
      "MEMB_TYPE_CIVIL":  { "description": "Member Type Civil",    "type": "integer" }
    }
  }
}
```

### Specifications

#### 공통 키

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Sub Domain Name | `"SUB_DOMAIN_NAME"` | String | - | **Required** |
| 2 | Rebar Dir.1 | `"V1"` | Number | - | **Required** |
| 3 | Rebar Dir.2 | `"V2"` | Number | - | **Required** |
| 4 | Domain Name | `"DOMAIN_NAME"` | String | - | **Required** |

#### CIVIL NX Only

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Member Type Civil • None: 0 • Plate Beam (1D): 1 • Plate Column (1D): 2 • Shell: 3 | `"MEMB_TYPE_CIVIL"` | Integer | - | **Required** |
| 6 | Rebar Direction • Local: 0 • UCS: 1 • Reference Axis: 2 | `"REBAR_AXIS_TYPE"` | Integer | 0 | Optional |
| 7 | UCS (Rebar Direction이 UCS인 경우) | `"STR_UCS"` | String | Blank | Optional |
| 8 | Axis Vector (Rebar Direction이 Reference Axis인 경우) | `"AXIS_VECTOR"` | Number | 0 | Optional |

#### GEN NX Only

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Member Type • None: 0 • Slab: 1 • Mat: 2 | `"MEMBER_TYPE"` | Integer | - | **Required** |
| 6 | Basic Rebar Option | `"OPT_BASIC_REBAR"` | Boolean | false | Optional |
| 7 | Top Rebar Name (X-Dir) | `"TOP_REBAR_NAME_X"` | String | Blank | Optional |
| 8 | Top Rebar Space (X-Dir) | `"TOP_REBAR_SPACE_X"` | Number | 0 | Optional |
| 9 | Bottom Rebar Name (X-Dir) | `"BOTTOM_REBAR_NAME_X"` | String | Blank | Optional |
| 10 | Bottom Rebar Space (X-Dir) | `"BOTTOM_REBAR_SPACE_X"` | Number | 0 | Optional |
| 11 | Top Rebar Name (Y-Dir) | `"TOP_REBAR_NAME_Y"` | String | Blank | Optional |
| 12 | Top Rebar Space (Y-Dir) | `"TOP_REBAR_SPACE_Y"` | Number | 0 | Optional |
| 13 | Bottom Rebar Name (Y-Dir) | `"BOTTOM_REBAR_NAME_Y"` | String | Blank | Optional |
| 14 | Bottom Rebar Space (Y-Dir) | `"BOTTOM_REBAR_SPACE_Y"` | Number | 0 | Optional |
| 15 | Rebar Material Option | `"OPT_REBAR_MATL"` | Boolean | false | Optional |
| 16 | Rebar Material Key | `"REBAR_MATL_KEY"` | Integer | 0 | Optional |
| 17 | Use Mt | `"bUseMt"` | Boolean | - | **Required** |
| 18 | Thickness | `"THICKNESS"` | Number | - | **Required** |

### Request Body 예제

#### CIVIL NX

```json
{
  "Assign": {
    "1": {
      "SUB_DOMAIN_NAME": "SDM1",
      "MEMBER_TYPE": 1,
      "V1": 0,
      "V2": 90,
      "DOMAIN_NAME": "DM1",
      "AXIS_VECTOR": [0, 0, 0, 0, 0, 0],
      "bUseMt": true,
      "STR_UCS": "",
      "MEMB_TYPE_CIVIL": 1
    }
  }
}
```

#### GEN NX (기본 철근 배근 포함)

```json
{
  "Assign": {
    "1": {
      "SUB_DOMAIN_NAME": "SDM1",
      "MEMBER_TYPE": 1,
      "V1": 0,
      "V2": 90,
      "DOMAIN_NAME": "DM1",
      "bUseMt": true,
      "THICKNESS": 0,
      "OPT_BASIC_REBAR": false,
      "TOP_REBAR_NAME_X": "D10",
      "TOP_REBAR_SPACE_X": 0.4,
      "BOTTOM_REBAR_NAME_X": "D10",
      "BOTTOM_REBAR_SPACE_X": 0.4,
      "TOP_REBAR_NAME_Y": "D10",
      "TOP_REBAR_SPACE_Y": 0.4,
      "BOTTOM_REBAR_NAME_Y": "D10",
      "BOTTOM_REBAR_SPACE_Y": 0.4,
      "OPT_REBAR_MATL": false,
      "REBAR_MATL_KEY": 0
    }
  }
}
```

### Python 예제

```python
# GEN NX Sub-Domain 생성 (슬래브)
sub_domain_data = {
    "Assign": {
        "1": {
            "SUB_DOMAIN_NAME": "SLAB_SUB",
            "MEMBER_TYPE": 1,       # Slab
            "V1": 0,                # X 방향 철근 (0°)
            "V2": 90,               # Y 방향 철근 (90°)
            "DOMAIN_NAME": "SLAB_DOMAIN",
            "bUseMt": True,
            "THICKNESS": 0.2,       # 두께 200mm
            "OPT_BASIC_REBAR": True,
            "TOP_REBAR_NAME_X": "D13",
            "TOP_REBAR_SPACE_X": 0.15,
            "BOTTOM_REBAR_NAME_X": "D13",
            "BOTTOM_REBAR_SPACE_X": 0.15,
            "TOP_REBAR_NAME_Y": "D13",
            "TOP_REBAR_SPACE_Y": 0.15,
            "BOTTOM_REBAR_NAME_Y": "D13",
            "BOTTOM_REBAR_SPACE_Y": 0.15,
            "OPT_REBAR_MATL": False,
            "REBAR_MATL_KEY": 0
        }
    }
}
midas_api("POST", "/db/SBDO", sub_domain_data)
```

---

## 6. `/db/DOEL`

> **Domain-Element** — 특정 요소를 Main-Domain 또는 Sub-Domain에 할당합니다.

- **URL**: `{base url}/db/DOEL`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Domain-Element ↗](https://support.midasuser.com/hc/en-us/articles/35807341514393)

### JSON Schema

```json
{
  "DOEL": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "TYPE":             { "description": "Domain Type",     "type": "integer" },
      "KEY_DOMAIN":       { "description": "Key Domain",      "type": "integer" },
      "MAIN_DOMAIN_NAME": { "description": "Main Domain Name","type": "string" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Domain Type • Main-Domain: 0 • Sub-Domain: 1 | `"TYPE"` | Integer | - | **Required** |
| 2 | Key Domain | `"KEY_DOMAIN"` | Integer | - | **Required** |
| 3 | Main Domain Name | `"MAIN_DOMAIN_NAME"` | String | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "163": { "TYPE": 1, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1" },
    "164": { "TYPE": 1, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1" },
    "165": { "TYPE": 0, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1" },
    "170": { "TYPE": 0, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1" },
    "171": { "TYPE": 0, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1" }
  }
}
```

### Python 예제

```python
# 요소를 도메인에 할당
# 163, 164번 요소 → Sub-Domain 1 ("DM1")
# 165, 170번 요소 → Main-Domain 1 ("DM1")
doel_data = {
    "Assign": {
        "163": {"TYPE": 1, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1"},
        "164": {"TYPE": 1, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1"},
        "165": {"TYPE": 0, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1"},
        "170": {"TYPE": 0, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1"},
    }
}
midas_api("POST", "/db/DOEL", doel_data)

# 전체 Domain-Element 할당 조회
result = midas_api("GET", "/db/DOEL")
assignments = result.get("DOEL", {})
print(f"총 할당된 요소 수: {len(assignments)}")

# Sub-Domain 할당 요소만 필터
sub_domain_elems = {k: v for k, v in assignments.items() if v["TYPE"] == 1}
print(f"Sub-Domain 할당 요소: {len(sub_domain_elems)}개")
```

---

## 전체 워크플로우 예제 — 3경간 × 5층 RC 라멘 골조 + 슬래브

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

# ── Step 1: 새 프로젝트 생성 ─────────────────────────────────
midas_api("POST", "/doc/NEW", {"Argument": {}})

# ── Step 2: 단위 설정 (KN, M) ──────────────────────────────
midas_api("PUT", "/db/UNIT", {
    "Assign": {"1": {"FORCE": "KN", "DIST": "M", "HEAT": "KJ", "TEMPER": "C"}}
})

# ── Step 3: 절점 생성 (라멘 골조, Y=0 평면) ──────────────────
n_bays, n_stories = 3, 5
bay_w, story_h = 6.0, 3.5
n_cols = n_bays + 1
nodes = {}
node_map = {}
nid = 1
for i_s in range(n_stories + 1):
    for i_c in range(n_cols):
        nodes[str(nid)] = {"X": i_c * bay_w, "Y": 0.0, "Z": i_s * story_h}
        node_map[(i_c, i_s)] = nid
        nid += 1

midas_api("POST", "/db/NODE", {"Assign": nodes})

# ── Step 4: 요소 생성 (기둥 + 보) ───────────────────────────
elems = {}
eid = 1
# 기둥 (단면 1번)
for i_s in range(n_stories):
    for i_c in range(n_cols):
        elems[str(eid)] = {
            "TYPE": "BEAM", "MATL": 1, "SECT": 1,
            "NODE": [node_map[(i_c, i_s)], node_map[(i_c, i_s + 1)]],
            "ANGLE": 0
        }
        eid += 1
# 보 (단면 2번)
for i_s in range(1, n_stories + 1):
    for i_b in range(n_bays):
        elems[str(eid)] = {
            "TYPE": "BEAM", "MATL": 1, "SECT": 2,
            "NODE": [node_map[(i_b, i_s)], node_map[(i_b + 1, i_s)]],
            "ANGLE": 0
        }
        eid += 1

midas_api("POST", "/db/ELEM", {"Assign": elems})

# ── Step 5: 저장 ─────────────────────────────────────────────
midas_api("POST", "/doc/SAVE", {"Argument": {}})

print("✓ RC 라멘 골조 모델 생성 완료")
print(f"  절점: {len(nodes)}개, 요소: {len(elems)}개")
print(f"  기둥: {n_cols * n_stories}개, 보: {n_bays * n_stories}개")
```

---

*[03_DB_Node_Element.md] 작성 완료 — 다음 파일 [04_DB_Properties.md] 진행 준비가 되었습니다.*
