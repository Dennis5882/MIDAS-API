# 16. VIEW

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

`VIEW` 파트는 모델 뷰(View)를 제어하는 함수로, 선택 상태 조회, 화면 캡처, 시점(Viewpoint) 조정, 활성화(Active) 제어, 표시(Display) 옵션, 결과 그래픽(Result Graphic) 표시를 다룹니다. `CAPTURE`는 `ANGLE`·`ACTIVE`·`DISPLAY`·`RESULTGRAPHIC` 옵션을 하나의 요청에 통합하여 사용할 수 있습니다.

---

## Endpoint 목록

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/view/SELECT`](#1-viewselect--select) | 선택된 노드/요소 ID 조회 | GET |
| 2 | [`/view/CAPTURE`](#2-viewcapture--capture) | 모델 화면 캡처 (이미지 저장) | POST |
| 3 | [`/view/PRECAPTURE`](#3-viewprecapture--dialog-capture) | 다이얼로그(사전처리) 캡처 | POST |
| 4 | [`/view/ANGLE`](#4-viewangle--viewpoint) | 시점(Viewpoint) 각도 설정 | POST |
| 5 | [`/view/ACTIVE`](#5-viewactive--active) | 활성화(Active) 대상 제어 | POST |
| 6 | [`/view/DISPLAY`](#6-viewdisplay--display) | 표시(Display) 옵션 설정 | POST |
| 7 | [`/view/RESULTGRAPHIC`](#7-viewresultgraphic--result-graphic) | 결과 그래픽 표시 설정 | POST |

---

## 1. `/view/SELECT` — Select

> **기능:** 현재 모델 뷰에서 사용자가 선택한 노드(Node)와 요소(Element)의 ID 목록을 조회합니다. 응답 전용(GET) 엔드포인트입니다.

### Input URI

```
{base url}/view/SELECT
```

### Active Methods

`GET`

### Response JSON

```json
{
  "SELECT": {
    "NODE_LIST": [67, 130, 171, 172, 173, 178, 179],
    "ELEM_LIST": [92, 93, 99, 106, 235, 308, 313, 314, 315, 316, 317, 323, 324, 325, 335, 336, 337, 338, 339, 340]
  }
}
```

### Parameters

응답 전용(GET) 엔드포인트로 요청 바디가 없습니다.

| No. | 설명 | Key | Value 타입 |
|-----|------|-----|-----------|
| 1 | 선택된 노드 ID 목록 | `"NODE_LIST"` | Array [Integer] |
| 2 | 선택된 요소 ID 목록 | `"ELEM_LIST"` | Array [Integer] |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── GET: 현재 선택된 노드/요소 조회 ────────────────────────────────
resp = requests.get(f"{BASE_URL}/view/SELECT", headers=HEADERS)
sel = resp.json().get("SELECT", {})
print(f"선택된 노드 {len(sel.get('NODE_LIST', []))}개: {sel.get('NODE_LIST')}")
print(f"선택된 요소 {len(sel.get('ELEM_LIST', []))}개: {sel.get('ELEM_LIST')}")
```

---

## 2. `/view/CAPTURE` — Capture

> **기능:** 현재 모델 뷰를 이미지 파일로 캡처하여 저장합니다. 시점(`ANGLE`), 활성화(`ACTIVE`), 표시(`DISPLAY`), 결과 그래픽(`RESULT_GRAPHIC`) 옵션을 하나의 요청에 통합하여 지정할 수 있습니다. Smart(Dynamic) Report 모드와 User Setting 모드를 지원합니다.

### Input URI

```
{base url}/view/CAPTURE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "CAPTURE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "FIGURE_NAME": { "type": "string" },
          "EXPORT_PATH": { "type": "string" },
          "WIDTH": { "type": "integer" },
          "HEIGHT": { "type": "integer" },
          "STAGE_NAME": { "type": "string" },
          "SET_MODE": { "type": "string" },
          "SET_HIDDEN": { "type": "boolean" },
          "ACTIVE": { "type": "object", "description": "View/Active" },
          "ANGLE": { "type": "object", "description": "View/Angle" },
          "DISPLAY": { "type": "object", "description": "View/Display" },
          "RESULT_GRAPHIC": { "type": "object", "description": "View/Result Graphic" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 그룹 | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|------|-----|-----------|--------|------|
| 1 | Smart Report | 이미지 파일 저장 경로 및 파일명 | `"EXPORT_PATH"` | String | — | **Required** |
| 2 | Smart Report | Smart Report 이미지 이름 | `"FIGURE_NAME"` | String | — | **Required** |
| 1 | User Setting | 이미지 파일 저장 경로 및 파일명 | `"EXPORT_PATH"` | String | — | **Required** |
| 2 | User Setting | 시공단계 이름 | `"STAGE_NAME"` | String | — | Optional |
| 3 | User Setting | 해석 모드 선택 · Pre-Mode: `"pre"` / Post-Mode: `"post"` | `"SET_MODE"` | String | — | Optional |
| 4 | User Setting | 은선(Hidden) 옵션 · Hidden: `true` / Not Hidden: `false` | `"SET_HIDDEN"` | Boolean | `false` | Optional |
| 5 | User Setting | 이미지 높이 픽셀 크기 | `"HEIGHT"` | Integer | — | Optional |
| 6 | User Setting | 이미지 너비 픽셀 크기 | `"WIDTH"` | Integer | — | Optional |
| 7 | User Setting | 시점 (`view/ANGLE` 매뉴얼 참조) | `"ANGLE"` | Object | — | Optional |
| 8 | User Setting | 활성화 (`view/ACTIVE` 매뉴얼 참조) | `"ACTIVE"` | Object | — | Optional |
| 9 | User Setting | 표시 (`view/DISPLAY` 매뉴얼 참조) | `"DISPLAY"` | Object | — | Optional |
| 10 | User Setting | 원근감(Perspective) | `"PERSPECTIVE"` | Boolean | `false` | Optional |
| 11 | User Setting | 줌 레벨 · Zoom Out: `25 ≤ value < 100` / Zoom Fit: `100` / Zoom In: `100 < value < 200` | `"ZOOM_LEVEL"` | Number | `100` | Optional |
| 12 | User Setting | 상단 배경색 | `"BGCOLOR_TOP"` | Object | — | Optional |
| 12-1 | | └ Red | `BGCOLOR_TOP.R` | Integer | — | Optional |
| 12-2 | | └ Green | `BGCOLOR_TOP.G` | Integer | — | Optional |
| 12-3 | | └ Blue | `BGCOLOR_TOP.B` | Integer | — | Optional |
| 13 | User Setting | 하단 배경색 | `"BGCOLOR_BOTTOM"` | Object | — | Optional |
| 13-1 | | └ Red | `BGCOLOR_BOTTOM.R` | Integer | — | Optional |
| 13-2 | | └ Green | `BGCOLOR_BOTTOM.G` | Integer | — | Optional |
| 13-3 | | └ Blue | `BGCOLOR_BOTTOM.B` | Integer | — | Optional |
| 14 | User Setting | 결과 표시 (`view/RESULTGRAPHIC` 매뉴얼 참조) | `"RESULT_GRAPHIC"` | Object | — | Optional |

> **참고:** `PERSPECTIVE`, `ZOOM_LEVEL`, `BGCOLOR_TOP`, `BGCOLOR_BOTTOM`은 예제 JSON에서 `DISPLAY` 객체 내부에 포함되어 전달됩니다(아래 Request 예시 참조).

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "SET_MODE": "post",
    "SET_HIDDEN": false,
    "EXPORT_PATH": "C:\\MIDAS\\CaptureTest\\image.jpg",
    "HEIGHT": 1000,
    "WIDTH": 1000,
    "ACTIVE": {
      "ACTIVE_MODE": "Active",
      "N_LIST": [104, 125, 151, 153],
      "E_LIST": [196, 228, 229, 231, 232, 269, 270, 279, 280, 291, 292, 349, 350]
    },
    "ANGLE": {
      "HORIZONTAL": 45,
      "VERTICAL": 60
    },
    "DISPLAY": {
      "NODE": { "NODE": true, "NODE_NUMBER": true },
      "PERSPECTIVE": true,
      "ZOOM_LEVEL": 150,
      "BGCOLOR_TOP": { "R": 255, "G": 125, "B": 125 }
    },
    "RESULT_GRAPHIC": {
      "CURRENT_MODE": "beam diagrams",
      "LOAD_CASE_COMB": { "TYPE": "ST", "NAME": "DL" },
      "COMPONENTS": { "PART": "total", "COMP": "Fx" },
      "DISPLAY_OPTIONS": { "FIDELITY": "Exact", "FILL": "line fill", "SCALE": 1.0 },
      "TYPE_OF_DISPLAY": {
        "CONTOUR": { "OPT_CHECK": true },
        "DEFORM": { "OPT_CHECK": true },
        "LEGEND": { "OPT_CHECK": true },
        "VALUES": { "OPT_CHECK": true }
      },
      "OUTPUT_SECT_LOCATION": { "OPT_I": true, "OPT_CENTER_MID": true, "OPT_J": true }
    }
  }
}
```

**POST Response Body**

```json
{
  "CAPTURE": {
    "message": "Success"
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

# ── POST: 보 부재력 다이어그램(Fx)을 이미지로 캡처 ─────────────────
payload = {
    "Argument": {
        "SET_MODE": "post",
        "SET_HIDDEN": False,
        "EXPORT_PATH": "C:\\MIDAS\\CaptureTest\\beam_Fx.jpg",
        "HEIGHT": 1000,
        "WIDTH": 1000,
        "ACTIVE": {"ACTIVE_MODE": "All"},
        "ANGLE": {"HORIZONTAL": 45, "VERTICAL": 60},
        "DISPLAY": {
            "PERSPECTIVE": True,
            "ZOOM_LEVEL": 100,
            "BGCOLOR_TOP": {"R": 255, "G": 255, "B": 255}
        },
        "RESULT_GRAPHIC": {
            "CURRENT_MODE": "beam diagrams",
            "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DL"},
            "COMPONENTS": {"PART": "total", "COMP": "Fx"},
            "DISPLAY_OPTIONS": {"FIDELITY": "Exact", "FILL": "line fill", "SCALE": 1.0},
            "TYPE_OF_DISPLAY": {
                "CONTOUR": {"OPT_CHECK": True},
                "LEGEND": {"OPT_CHECK": True},
                "VALUES": {"OPT_CHECK": True}
            }
        }
    }
}
resp = requests.post(f"{BASE_URL}/view/CAPTURE", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 3. `/view/PRECAPTURE` — Dialog Capture

> **기능:** 특정 다이얼로그(사전처리 미리보기) 화면을 이미지 파일로 캡처합니다. 현재 섬유 단면(Fiber Division of Section) 미리보기를 지원합니다.

### Input URI

```
{base url}/view/PRECAPTURE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "CAPTURE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "EXPORT_PATH": { "description": "Save Path", "type": "string" },
          "VIEW_TYPE": { "description": "Preview Picture Type", "type": "string", "enum": ["FIBR"] },
          "OPTION": {
            "description": "Option for Capture",
            "type": "object",
            "properties": {
              "ID": { "description": "Picture Type ID Number", "type": "integer" }
            }
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
| 1 | 이미지 파일 저장 경로 및 파일명 | `"EXPORT_PATH"` | String | — | **Required** |
| 2 | 미리보기 그림 타입 · 단면 섬유분할: `"FIBR"` | `"VIEW_TYPE"` | String | — | **Required** |
| 3 | 캡처 옵션 | `"OPTION"` | Object | — | **Required** |
| 3-1 | └ 그림 타입 ID 번호 | `OPTION.ID` | Integer | — | **Required** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\CaptureTest\\Test.jpg",
    "VIEW_TYPE": "FIBR",
    "OPTION": { "ID": 1 }
  }
}
```

**POST Response Body**

```json
{
  "CAPTURE": {
    "message": "Success"
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

# ── POST: 섬유 단면(Fiber) 미리보기 다이얼로그 캡처 ────────────────
payload = {
    "Argument": {
        "EXPORT_PATH": "C:\\MIDAS\\CaptureTest\\fiber_sect_1.jpg",
        "VIEW_TYPE": "FIBR",      # Fiber Division of Section
        "OPTION": {"ID": 1}       # 단면 ID 1번
    }
}
resp = requests.post(f"{BASE_URL}/view/PRECAPTURE", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 4. `/view/ANGLE` — Viewpoint

> **기능:** 모델 뷰의 시점(Viewpoint)을 수평/수직 각도로 설정합니다.

### Input URI

```
{base url}/view/ANGLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "ANGLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "HORIZONTAL": { "type": "number" },
          "VERTICAL": { "type": "number" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 수평 시점 각도 | `"HORIZONTAL"` | Number | `0` | Optional |
| 2 | 수직 시점 각도 | `"VERTICAL"` | Number | `0` | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "HORIZONTAL": 30,
    "VERTICAL": 15
  }
}
```

**POST Response Body**

```json
{
  "ANGLE": {
    "message": "Success"
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

# ── POST: 시점을 수평 30°, 수직 15°로 설정 ─────────────────────────
payload = {"Argument": {"HORIZONTAL": 30, "VERTICAL": 15}}
resp = requests.post(f"{BASE_URL}/view/ANGLE", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 5. `/view/ACTIVE` — Active

> **기능:** 모델 뷰에서 활성화(Active)할 대상을 지정합니다. 전체(All), 노드/요소 지정(Active), 아이덴티티 그룹 지정(Identity)의 3가지 모드를 지원합니다.

### Input URI

```
{base url}/view/ACTIVE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "ACTIVE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "ACTIVE_MODE": {
            "type": "string",
            "description": "ActiveModeType",
            "enum": ["All", "Active", "Identity"]
          },
          "N_LIST": {
            "type": "array",
            "items": { "type": "integer" },
            "description": "NodeNumberList"
          },
          "E_LIST": {
            "type": "array",
            "items": { "type": "integer" },
            "description": "ElementNumberList"
          },
          "IDENTITY_TYPE": {
            "type": "string",
            "description": "IdentityType",
            "enum": ["Group", "NamedPlane", "LoadGroup", "BoundaryGroup"]
          },
          "IDENTITY_LIST": {
            "type": "array",
            "items": { "type": "string" }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 모드 | 설명 | Key | Value 타입 | 필수 |
|-----|------|------|-----|-----------|------|
| 1 | All | 활성화 모드 · 전체 활성화: `"All"` | `"ACTIVE_MODE"` | String | **Required** |
| 1 | Active | 활성화 모드 · 노드/요소 지정: `"Active"` | `"ACTIVE_MODE"` | String | **Required** |
| 2 | Active | 노드 번호 목록 | `"N_LIST"` | Array [Integer] | **Required** |
| 3 | Active | 요소 번호 목록 | `"E_LIST"` | Array [Integer] | **Required** |
| 1 | Identity | 활성화 모드 · 아이덴티티 지정: `"Identity"` | `"ACTIVE_MODE"` | String | **Required** |
| 2 | Identity | 아이덴티티 타입 · 구조그룹: `"Group"` / 명명평면: `"NamedPlane"` / 하중그룹: `"LoadGroup"` / 경계그룹: `"BoundaryGroup"` | `"IDENTITY_TYPE"` | String | **Required** |
| 3 | Identity | 아이덴티티 이름 목록 | `"IDENTITY_LIST"` | Array [String] | **Required** |

### Request / Response JSON

**POST Request Body — Mode 1: All**

```json
{
  "Argument": {
    "ACTIVE_MODE": "All"
  }
}
```

**POST Request Body — Mode 2: Active by Node/Element**

```json
{
  "Argument": {
    "ACTIVE_MODE": "Active",
    "N_LIST": [469, 770, 772, 773],
    "E_LIST": [1631, 1646, 1654]
  }
}
```

**POST Request Body — Mode 3: Active by Identity**

```json
{
  "Argument": {
    "ACTIVE_MODE": "Identity",
    "IDENTITY_TYPE": "BoundaryGroup",
    "IDENTITY_LIST": ["Support", "Support2", "Support3"]
  }
}
```

**POST Response Body**

```json
{
  "ACTIVE": {
    "message": "Success"
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

# ── POST: Mode 2 - 특정 노드/요소만 활성화 ────────────────────────
payload_active = {
    "Argument": {
        "ACTIVE_MODE": "Active",
        "N_LIST": [469, 770, 772, 773],
        "E_LIST": [1631, 1646, 1654]
    }
}
resp = requests.post(f"{BASE_URL}/view/ACTIVE", json=payload_active, headers=HEADERS)
print("POST (Active):", resp.status_code, resp.json())

# ── POST: Mode 3 - 경계그룹으로 활성화 ─────────────────────────────
payload_identity = {
    "Argument": {
        "ACTIVE_MODE": "Identity",
        "IDENTITY_TYPE": "BoundaryGroup",
        "IDENTITY_LIST": ["Support", "Support2", "Support3"]
    }
}
resp = requests.post(f"{BASE_URL}/view/ACTIVE", json=payload_identity, headers=HEADERS)
print("POST (Identity):", resp.status_code, resp.json())

# ── POST: Mode 1 - 전체 활성화(초기화) ─────────────────────────────
resp = requests.post(f"{BASE_URL}/view/ACTIVE", json={"Argument": {"ACTIVE_MODE": "All"}}, headers=HEADERS)
print("POST (All):", resp.status_code, resp.json())
```

---

## 6. `/view/DISPLAY` — Display

> **기능:** 모델 창에 표시되는 절점(Node)·요소(Element)·특성(Property)·경계조건(Boundary)·하중(Load)·기타(Misc)·뷰(View) 항목의 표시 여부와 표시 옵션(번호, 이름, 국부축, 하중값 포맷 등)을 일괄 제어합니다. 이 엔드포인트는 `POST` 전용이며, `"Argument"` 하위에 제어하려는 그룹 객체만 선택적으로 전달합니다.

### Input URI

```
{base url}/view/DISPLAY
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "DISPLAY": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "NODE": {
            "type": "object",
            "properties": {
              "NODE": { "type": "boolean" },
              "NODE_NUMBER": { "type": "boolean" },
              "STORY_NAME": { "type": "boolean" },
              "NODE_LOCAL_AXIS": { "type": "boolean" }
            }
          },
          "ELEMENT": {
            "type": "object",
            "properties": {
              "ELEM_NUMBER": { "type": "boolean" },
              "ELEM_NUMBER_WITH_BORDER": { "type": "boolean" },
              "ELEM_TYPE_NUMBER": { "type": "boolean" },
              "ELEM_TYPE_NAME": { "type": "boolean" },
              "WALL_ID": { "type": "boolean" },
              "GAP": { "type": "boolean" },
              "HOOK": { "type": "boolean" },
              "CABLE": { "type": "boolean" },
              "LOCAL_AXIS": { "type": "boolean" },
              "LOCAL_AXIS_LABEL": { "type": "boolean" },
              "LOCAL_DIRECTION": { "type": "boolean" },
              "SUB_DOMAIN_REBAR_DIRECTION": { "type": "boolean" }
            }
          },
          "PROPERTY": {
            "type": "object",
            "properties": {
              "MATERIAL_NUMBER": { "type": "boolean" },
              "MATERIAL_NAME": { "type": "boolean" },
              "PROPERTY_NUMBER": { "type": "boolean" },
              "PROPERTY_NAME": { "type": "boolean" },
              "SECTION_SHAPE": { "type": "boolean" },
              "TAPERED_SECTION_GROUP": { "type": "boolean" },
              "TIME_DEPENDENT_MATERIAL_LINK": { "type": "boolean" },
              "INELASTIC_HINGE_NAME": { "type": "boolean" },
              "INELASTIC_HINGE_SYMBOL": { "type": "boolean" },
              "REINFORCEMENT_OF_SECTIONS": { "type": "boolean" },
              "VIRTUAL_SECTION_LOCAL_AXIS": { "type": "boolean" }
            }
          },
          "GROUP_SELECTION": {
            "type": "array",
            "items": { "type": "string" }
          },
          "BOUNDARY": {
            "type": "object",
            "properties": {
              "SUPPORT": { "type": "boolean" },
              "SUPPORT_BY_DIRECTION": { "type": "boolean" },
              "POINT_SPRING_SUPPORT": { "type": "boolean" },
              "POINT_SPRING_SUPPORT_COMP_TENS": { "type": "boolean" },
              "POINT_SPRING_SUPPORT_MULTI_LINEAR": { "type": "boolean" },
              "POINT_SPRING_SUPPORT_BY_DIRECTION": { "type": "boolean" },
              "POINT_SPRING_SUPPORT_BY_DIRECTION_COMP_TENS": { "type": "boolean" },
              "POINT_SPRING_SUPPORT_BY_DIRECTION_MULTI_LINEAR": { "type": "boolean" },
              "SURFACE_SPRING_SUPPORT_TYPE": { "type": "boolean" },
              "SURFACE_SPRING_SUPPORT_LINEAR": { "type": "boolean" },
              "SURFACE_SPRING_SUPPORT_COMP_TENS": { "type": "boolean" },
              "GENERAL_SPRING_SUPPORT": { "type": "boolean" },
              "ELASTIC_LINK": { "type": "boolean" },
              "ELASTIC_LINK_LOCAL_AXIS": { "type": "boolean" },
              "ELASTIC_LINK_TYPE": { "type": "boolean" },
              "ELASTIC_LINK_NUMBER": { "type": "boolean" },
              "GENERAL_LINK": { "type": "boolean" },
              "GENERAL_LINK_NUMBER": { "type": "boolean" },
              "GENERAL_LINK_LOCAL_AXIS": { "type": "boolean" },
              "GENERAL_LINK_TYPE": { "type": "boolean" },
              "CHANGE_GENERAL_LINK_PROPERTIES": { "type": "boolean" },
              "BEAM_END_RELEASE_SYMBOL": { "type": "boolean" },
              "BEAM_END_RELEASE_DIGIT": { "type": "boolean" },
              "BEAM_END_OFFSET_SYMBOL": { "type": "boolean" },
              "BEAM_END_OFFSET_DIGIT": { "type": "boolean" },
              "PLATE_END_RELEASE_SYMBOL": { "type": "boolean" },
              "PLATE_END_RELEASE_DIGIT": { "type": "boolean" },
              "RIGID_LINK": { "type": "boolean" },
              "LINEAR_CONSTRAINTS": { "type": "boolean" },
              "REACTION_POSITION": { "type": "boolean" },
              "STORY_DIAPHRAGM": { "type": "boolean" },
              "DIAPHRAGM_DISCONNECT": { "type": "boolean" }
            }
          },
          "LOAD": {
            "type": "object",
            "properties": {
              "CASE_SELECTION": {
                "type": "object",
                "properties": {
                  "TYPE": { "type": "string" },
                  "NAME": { "type": "string" }
                }
              },
              "GROUP_SELECTION": {
                "type": "array",
                "items": { "type": "string" }
              },
              "LOAD_VALUE": {
                "type": "object",
                "properties": {
                  "FORMAT": { "type": "string" },
                  "PLACE": { "type": "integer" }
                }
              },
              "NODAL_BODY_FORCE": { "type": "boolean" },
              "NODAL_LOAD": { "type": "boolean" },
              "SPECIFIED_DISPLACEMENT": { "type": "boolean" },
              "BEAM_LOAD": { "type": "boolean" },
              "PRESTRESS_LOAD": { "type": "boolean" },
              "PRETENSION_LOAD": { "type": "boolean" },
              "FLOOR_LOAD": { "type": "boolean" },
              "FLOOR_LOAD_NAME": { "type": "boolean" },
              "FLOOR_LOAD_AREA": { "type": "boolean" },
              "LOADING_AREA_PLANE": { "type": "boolean" },
              "FINISHING_MATERIAL_LOAD": { "type": "boolean" },
              "PRESSURE_LOAD": { "type": "boolean" },
              "AREA_PRESSURE_LOADS": { "type": "boolean" },
              "PLANE_LOAD": { "type": "boolean" },
              "PLANE_LOAD_NAME": { "type": "boolean" },
              "NODAL_TEMPERATURE": { "type": "boolean" },
              "ELEMENT_TEMPERATURE": { "type": "boolean" },
              "TEMPERATURE_GRADIENT": { "type": "boolean" },
              "BEAM_SECTION_TEMPERATURE": { "type": "boolean" },
              "TENDON_PRESTRESS": { "type": "boolean" },
              "WIND_LOAD": { "type": "boolean" },
              "AREA_WIND_PRESSURE": { "type": "boolean" },
              "AREA_WIND_PRESSURE_NAME": { "type": "boolean" },
              "BEAM_WIND_PRESSURE": { "type": "boolean" },
              "NODAL_WIND_PRESSURE": { "type": "boolean" },
              "FUNCTION_WIND_PRESSURE": { "type": "boolean" },
              "FUNCTION_WIND_PRESSURE_NAME": { "type": "boolean" },
              "SEISMIC_EARTH_PRESSURE": { "type": "boolean" },
              "STATIC_EARTH_PRESSURE": { "type": "boolean" },
              "SEISMIC_LOAD": { "type": "boolean" },
              "DYNAMIC_NODAL_LOAD": { "type": "boolean" },
              "MULTIPLE_SUPPORT_EXCITATION": { "type": "boolean" },
              "MULTIPLE_SUPPORT_EXCITATION_FUNCTION_NAME": { "type": "boolean" },
              "DIR_X": { "type": "boolean" },
              "DIR_Y": { "type": "boolean" },
              "DIR_Z": { "type": "boolean" }
            }
          },
          "MISC": {
            "type": "object",
            "properties": {
              "NODAL_MASS": { "type": "boolean" },
              "LOAD_TO_MASS": { "type": "boolean" },
              "TENDON_PROFILE_NAMES": { "type": "boolean" },
              "TENDON_PROFILE_POINT": { "type": "boolean" },
              "INITIAL_FORCES_FOR_GEOMETRIC_STIFFNESS": { "type": "boolean" },
              "SETTLEMENT_GROUP": { "type": "boolean" },
              "SETTLEMENT_GROUP_VALUE": { "type": "boolean" },
              "HEAT_OF_HYDRATION_VALUE": { "type": "boolean" },
              "HEAT_OF_HYDRATION_FUNC_NAME": { "type": "boolean" },
              "HEAT_OF_HYDRATION_ELEMENT_CONVECTION_BOUNDARY": { "type": "boolean" },
              "HEAT_OF_HYDRATION_PRESCRIBED_TEMPERATURE": { "type": "boolean" },
              "HEAT_OF_HYDRATION_HEAT_SOURCE": { "type": "boolean" },
              "HEAT_OF_HYDRATION_PIPE_COOLING_ELEMENT": { "type": "boolean" },
              "GRID_MODEL_LOAD_LINE": { "type": "boolean" }
            }
          },
          "VIEW": {
            "type": "object",
            "properties": {
              "UCS_AXIS": { "type": "boolean" },
              "VIEWPORT_GIZMO": { "type": "boolean" },
              "VIEW_POINT": { "type": "boolean" },
              "DESCRIPTION": { "type": "string" },
              "LABEL_ORIENTATION": { "type": "integer" }
            }
          }
        }
      }
    }
  }
}
```

> **참고:** 원본 스키마에는 `MISC.GRID_MODEL_LOAD_LINE`가 누락되어 있으나 예제 및 Specifications에 존재하므로 포함했습니다(`GRID_MODEL_LOAD_LINE`은 MIDAS CIVIL NX JP 버전 전용). 또한 원본 스키마/예제의 `VIEWPPORT_GIZMO`는 오탈자이며 정식 Key는 `VIEWPORT_GIZMO`입니다.

### Parameters

#### 1) Node Display — `Argument.NODE` (Object, Optional)

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 절점 표시 옵션 그룹 | `NODE` | Object | - | Optional |
| (1) | 절점(Node) 표시 | `NODE.NODE` | Boolean | false | Optional |
| (2) | 절점 번호(Node Number) | `NODE.NODE_NUMBER` | Boolean | false | Optional |
| (3) | 절점 국부좌표축(Node Local Axis) | `NODE.NODE_LOCAL_AXIS` | Boolean | false | Optional |
| (4) | 층 이름(Story Name) ᴳ⁾ | `NODE.STORY_NAME` | Boolean | false | Optional |

#### 2) Element Display — `Argument.ELEMENT` (Object, Optional)

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 2 | 요소 표시 옵션 그룹 | `ELEMENT` | Object | - | Optional |
| (1) | 요소 번호(Element Number) | `ELEMENT.ELEM_NUMBER` | Boolean | false | Optional |
| (2) | 테두리 포함 요소 번호 | `ELEMENT.ELEM_NUMBER_WITH_BORDER` | Boolean | false | Optional |
| (3) | 요소 타입 번호 | `ELEMENT.ELEM_TYPE_NUMBER` | Boolean | false | Optional |
| (4) | 요소 타입 이름 | `ELEMENT.ELEM_TYPE_NAME` | Boolean | false | Optional |
| (5) | 벽체 ID(Wall ID) ᴳ⁾ | `ELEMENT.WALL_ID` | Boolean | false | Optional |
| (6) | 간극 요소(Gap) | `ELEMENT.GAP` | Boolean | false | Optional |
| (7) | 훅 요소(Hook) | `ELEMENT.HOOK` | Boolean | false | Optional |
| (8) | 케이블(Cable) | `ELEMENT.CABLE` | Boolean | false | Optional |
| (9) | 국부좌표축(Local Axis) | `ELEMENT.LOCAL_AXIS` | Boolean | false | Optional |
| (10) | 국부축 라벨 (Local Axis가 True일 때) | `ELEMENT.LOCAL_AXIS_LABEL` | Boolean | false | Optional |
| (11) | 국부 방향(Local Direction) | `ELEMENT.LOCAL_DIRECTION` | Boolean | false | Optional |
| (12) | 서브도메인 철근 방향 | `ELEMENT.SUB_DOMAIN_REBAR_DIRECTION` | Boolean | false | Optional |

#### 3) Property Display — `Argument.PROPERTY` (Object, Optional)

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 3 | 특성 표시 옵션 그룹 | `PROPERTY` | Object | - | Optional |
| (1) | 재료 번호(Material Number) ˢ¹⁾ | `PROPERTY.MATERIAL_NUMBER` | Boolean | false | Optional |
| (2) | 재료 이름(Material Name) ˢ¹⁾ | `PROPERTY.MATERIAL_NAME` | Boolean | false | Optional |
| (3) | 특성 번호(Property Number) ˢ¹⁾ | `PROPERTY.PROPERTY_NUMBER` | Boolean | false | Optional |
| (4) | 특성 이름(Property Name) ˢ¹⁾ | `PROPERTY.PROPERTY_NAME` | Boolean | false | Optional |
| (5) | 단면 형상(Section Shape) | `PROPERTY.SECTION_SHAPE` | Boolean | false | Optional |
| (6) | 변단면 그룹(Tapered Section Group) ˢ¹⁾ | `PROPERTY.TAPERED_SECTION_GROUP` | Boolean | false | Optional |
| (7) | 시간의존재료 링크 ˢ¹⁾ | `PROPERTY.TIME_DEPENDENT_MATERIAL_LINK` | Boolean | false | Optional |
| (8) | 비탄성 힌지 이름 ˢ²⁾ | `PROPERTY.INELASTIC_HINGE_NAME` | Boolean | false | Optional |
| (9) | 비탄성 힌지 기호 ˢ²⁾ | `PROPERTY.INELASTIC_HINGE_SYMBOL` | Boolean | false | Optional |
| (10) | 단면 배근(Reinforcement of Sections) | `PROPERTY.REINFORCEMENT_OF_SECTIONS` | Boolean | false | Optional |
| (11) | 가상 단면 국부축 | `PROPERTY.VIRTUAL_SECTION_LOCAL_AXIS` | Boolean | false | Optional |

#### 4) Boundary Display — `Argument.GROUP_SELECTION` / `Argument.BOUNDARY`

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 4 | 경계 그룹 선택 | `GROUP_SELECTION` | Array[String] | All | Optional |
| 5 | 경계조건 표시 옵션 그룹 | `BOUNDARY` | Object | - | Optional |
| (1) | 지점(Support) ˢ³⁾ | `BOUNDARY.SUPPORT` | Boolean | false | Optional |
| (2) | 방향별 지점 ˢ³⁾ | `BOUNDARY.SUPPORT_BY_DIRECTION` | Boolean | false | Optional |
| (3) | 점 스프링 지점 ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT` | Boolean | false | Optional |
| (4) | 점 스프링 지점(압축/인장) ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT_COMP_TENS` | Boolean | false | Optional |
| (5) | 점 스프링 지점(다중선형) ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT_MULTI_LINEAR` | Boolean | false | Optional |
| (6) | 방향별 점 스프링 지점 ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT_BY_DIRECTION` | Boolean | false | Optional |
| (7) | 방향별 점 스프링 지점(압축/인장) ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT_BY_DIRECTION_COMP_TENS` | Boolean | false | Optional |
| (8) | 방향별 점 스프링 지점(다중선형) ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT_BY_DIRECTION_MULTI_LINEAR` | Boolean | false | Optional |
| (9) | 면 스프링 지점 타입 | `BOUNDARY.SURFACE_SPRING_SUPPORT_TYPE` | Boolean | false | Optional |
| (10) | 면 스프링 지점(선형) | `BOUNDARY.SURFACE_SPRING_SUPPORT_LINEAR` | Boolean | false | Optional |
| (11) | 면 스프링 지점(압축/인장) | `BOUNDARY.SURFACE_SPRING_SUPPORT_COMP_TENS` | Boolean | false | Optional |
| (12) | 일반 스프링 지점 | `BOUNDARY.GENERAL_SPRING_SUPPORT` | Boolean | false | Optional |
| (13) | 탄성 링크(Elastic Link) | `BOUNDARY.ELASTIC_LINK` | Boolean | false | Optional |
| (14) | 탄성 링크 국부축 (Elastic Link가 True일 때) | `BOUNDARY.ELASTIC_LINK_LOCAL_AXIS` | Boolean | false | Optional |
| (15) | 탄성 링크 타입 (Elastic Link가 True일 때) | `BOUNDARY.ELASTIC_LINK_TYPE` | Boolean | false | Optional |
| (16) | 탄성 링크 번호 (Elastic Link가 True일 때) | `BOUNDARY.ELASTIC_LINK_NUMBER` | Boolean | false | Optional |
| (17) | 일반 링크(General Link) ˢ⁵⁾, ˢ⁶⁾ | `BOUNDARY.GENERAL_LINK` | Boolean | false | Optional |
| (18) | 일반 링크 번호 ˢ⁷⁾, ˢ⁸⁾ | `BOUNDARY.GENERAL_LINK_NUMBER` | Boolean | false | Optional |
| (19) | 일반 링크 국부축 ˢ⁵⁾, ˢ⁸⁾ | `BOUNDARY.GENERAL_LINK_LOCAL_AXIS` | Boolean | false | Optional |
| (20) | 일반 링크 타입 ˢ⁶⁾, ˢ⁷⁾ | `BOUNDARY.GENERAL_LINK_TYPE` | Boolean | false | Optional |
| (21) | 일반 링크 특성 변경 | `BOUNDARY.CHANGE_GENERAL_LINK_PROPERTIES` | Boolean | false | Optional |
| (22) | 보 단부 해제 기호 ˢ⁹⁾ | `BOUNDARY.BEAM_END_RELEASE_SYMBOL` | Boolean | false | Optional |
| (23) | 보 단부 해제 수치 ˢ⁹⁾ | `BOUNDARY.BEAM_END_RELEASE_DIGIT` | Boolean | false | Optional |
| (24) | 보 단부 오프셋 기호 | `BOUNDARY.BEAM_END_OFFSET_SYMBOL` | Boolean | false | Optional |
| (25) | 보 단부 오프셋 수치 | `BOUNDARY.BEAM_END_OFFSET_DIGIT` | Boolean | false | Optional |
| (26) | 판 단부 해제 기호 ˢ¹⁰⁾ | `BOUNDARY.PLATE_END_RELEASE_SYMBOL` | Boolean | false | Optional |
| (27) | 판 단부 해제 수치 ˢ¹⁰⁾ | `BOUNDARY.PLATE_END_RELEASE_DIGIT` | Boolean | false | Optional |
| (28) | 강체 링크(Rigid Link) | `BOUNDARY.RIGID_LINK` | Boolean | false | Optional |
| (29) | 선형 구속(Linear Constraints) | `BOUNDARY.LINEAR_CONSTRAINTS` | Boolean | false | Optional |
| (30) | 반력 위치(Reaction Position) | `BOUNDARY.REACTION_POSITION` | Boolean | false | Optional |
| (31) | 층 강막(Story Diaphragm) ᴳ⁾ | `BOUNDARY.STORY_DIAPHRAGM` | Boolean | false | Optional |
| (32) | 강막 분리(Diaphragm Disconnect) ᴳ⁾ | `BOUNDARY.DIAPHRAGM_DISCONNECT` | Boolean | false | Optional |

#### 5) Load Display — `Argument.LOAD` (Object, Optional)

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 6 | 하중 표시 옵션 그룹 | `LOAD` | Object | - | Optional |
| (1) | 하중 케이스로 하중 선택 | `LOAD.CASE_SELECTION` | Object | All | Optional |
| i. | 하중 케이스 타입 (정적하중: `"ST"`) | `LOAD.CASE_SELECTION.TYPE` | String | - | Required |
| ii. | 하중 케이스 이름 | `LOAD.CASE_SELECTION.NAME` | String | - | Required |
| (2) | 하중 그룹 선택 | `LOAD.GROUP_SELECTION` | Array[String] | All | Optional |
| (3) | 하중값(Load Value) | `LOAD.LOAD_VALUE` | Object | - | Optional |
| i. | 표시 형식 (`"Default"` / `"Fixed"` / `"Scientific"`) | `LOAD.LOAD_VALUE.FORMAT` | String | - | Required |
| ii. | 소수점 자리수 | `LOAD.LOAD_VALUE.PLACE` | Integer | - | Required |
| (4) | 절점 체적력(Nodal Body Force) | `LOAD.NODAL_BODY_FORCE` | Boolean | false | Optional |
| (5) | 절점 하중(Nodal Load) | `LOAD.NODAL_LOAD` | Boolean | false | Optional |
| (6) | 강제 변위(Specified Displacement) | `LOAD.SPECIFIED_DISPLACEMENT` | Boolean | false | Optional |
| (7) | 보 하중(Beam Load) | `LOAD.BEAM_LOAD` | Boolean | false | Optional |
| (8) | 프리스트레스 하중 | `LOAD.PRESTRESS_LOAD` | Boolean | false | Optional |
| (9) | 프리텐션 하중 | `LOAD.PRETENSION_LOAD` | Boolean | false | Optional |
| (10) | 바닥 하중(Floor Load) | `LOAD.FLOOR_LOAD` | Boolean | false | Optional |
| (11) | 바닥 하중 이름 | `LOAD.FLOOR_LOAD_NAME` | Boolean | false | Optional |
| (12) | 바닥 하중 면적 | `LOAD.FLOOR_LOAD_AREA` | Boolean | false | Optional |
| (13) | 하중 재하 평면(Loading Area Plane) ᴳ⁾ | `LOAD.LOADING_AREA_PLANE` | Boolean | false | Optional |
| (14) | 마감재 하중(Finishing Material Load) ᴳ⁾ | `LOAD.FINISHING_MATERIAL_LOAD` | Boolean | false | Optional |
| (15) | 압력 하중(Pressure Load) | `LOAD.PRESSURE_LOAD` | Boolean | false | Optional |
| (16) | 면적 압력 하중(Area Pressure Loads) | `LOAD.AREA_PRESSURE_LOADS` | Boolean | false | Optional |
| (17) | 평면 하중(Plane Load) | `LOAD.PLANE_LOAD` | Boolean | false | Optional |
| (18) | 평면 하중 이름 | `LOAD.PLANE_LOAD_NAME` | Boolean | false | Optional |
| (19) | 절점 온도(Nodal Temperature) | `LOAD.NODAL_TEMPERATURE` | Boolean | false | Optional |
| (20) | 요소 온도(Element Temperature) | `LOAD.ELEMENT_TEMPERATURE` | Boolean | false | Optional |
| (21) | 온도 구배(Temperature Gradient) | `LOAD.TEMPERATURE_GRADIENT` | Boolean | false | Optional |
| (22) | 보 단면 온도 | `LOAD.BEAM_SECTION_TEMPERATURE` | Boolean | false | Optional |
| (23) | 텐던 프리스트레스 | `LOAD.TENDON_PRESTRESS` | Boolean | false | Optional |
| (24) | 풍하중(Wind Load) ᴳ⁾ | `LOAD.WIND_LOAD` | Boolean | false | Optional |
| (25) | 면적 풍압(Area Wind Pressure) ᴳ⁾ | `LOAD.AREA_WIND_PRESSURE` | Boolean | false | Optional |
| (26) | 면적 풍압 이름 ᴳ⁾ | `LOAD.AREA_WIND_PRESSURE_NAME` | Boolean | false | Optional |
| (27) | 보 풍압(Beam Wind Pressure) ᴳ⁾ | `LOAD.BEAM_WIND_PRESSURE` | Boolean | false | Optional |
| (28) | 절점 풍압(Nodal Wind Pressure) ᴳ⁾ | `LOAD.NODAL_WIND_PRESSURE` | Boolean | false | Optional |
| (29) | 함수 풍압(Function Wind Pressure) ᴳ⁾ | `LOAD.FUNCTION_WIND_PRESSURE` | Boolean | false | Optional |
| (30) | 함수 풍압 이름 ᴳ⁾ | `LOAD.FUNCTION_WIND_PRESSURE_NAME` | Boolean | false | Optional |
| (31) | 지진 토압(Seismic Earth Pressure) ᴳ⁾ | `LOAD.SEISMIC_EARTH_PRESSURE` | Boolean | false | Optional |
| (32) | 정적 토압(Static Earth Pressure) ᴳ⁾ | `LOAD.STATIC_EARTH_PRESSURE` | Boolean | false | Optional |
| (33) | 지진 하중(Seismic Load) ᴳ⁾ | `LOAD.SEISMIC_LOAD` | Boolean | false | Optional |
| (34) | 동적 절점 하중 | `LOAD.DYNAMIC_NODAL_LOAD` | Boolean | false | Optional |
| (35) | 다지점 지반가진(Multiple Support Excitation) | `LOAD.MULTIPLE_SUPPORT_EXCITATION` | Boolean | false | Optional |
| (36) | 다지점 지반가진 함수 이름 | `LOAD.MULTIPLE_SUPPORT_EXCITATION_FUNCTION_NAME` | Boolean | false | Optional |
| (37) | X 방향 (가진 함수 이름이 True일 때) | `LOAD.DIR_X` | Boolean | false | Optional |
| (38) | Y 방향 (가진 함수 이름이 True일 때) | `LOAD.DIR_Y` | Boolean | false | Optional |
| (39) | Z 방향 (가진 함수 이름이 True일 때) | `LOAD.DIR_Z` | Boolean | false | Optional |

#### 6) Miscellaneous Display — `Argument.MISC` (Object, Optional)

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 7 | 기타 표시 옵션 그룹 | `MISC` | Object | - | Optional |
| (1) | 절점 질량(Nodal Mass) | `MISC.NODAL_MASS` | Boolean | false | Optional |
| (2) | 하중을 질량으로(Load to Mass) | `MISC.LOAD_TO_MASS` | Boolean | false | Optional |
| (3) | 텐던 프로파일 이름 | `MISC.TENDON_PROFILE_NAMES` | Boolean | false | Optional |
| (4) | 텐던 프로파일 점 | `MISC.TENDON_PROFILE_POINT` | Boolean | false | Optional |
| (5) | 기하강성 초기력 | `MISC.INITIAL_FORCES_FOR_GEOMETRIC_STIFFNESS` | Boolean | false | Optional |
| (6) | 침하 그룹(Settlement Group) | `MISC.SETTLEMENT_GROUP` | Boolean | false | Optional |
| (7) | 침하 그룹 값 (Settlement Group이 True일 때) | `MISC.SETTLEMENT_GROUP_VALUE` | Boolean | false | Optional |
| (8) | 수화열 값 | `MISC.HEAT_OF_HYDRATION_VALUE` | Boolean | false | Optional |
| (9) | 수화열 함수 이름 | `MISC.HEAT_OF_HYDRATION_FUNC_NAME` | Boolean | false | Optional |
| (10) | 수화열 요소 대류 경계 | `MISC.HEAT_OF_HYDRATION_ELEMENT_CONVECTION_BOUNDARY` | Boolean | false | Optional |
| (11) | 수화열 지정 온도 | `MISC.HEAT_OF_HYDRATION_PRESCRIBED_TEMPERATURE` | Boolean | false | Optional |
| (12) | 수화열 열원(Heat Source) | `MISC.HEAT_OF_HYDRATION_HEAT_SOURCE` | Boolean | false | Optional |
| (13) | 수화열 파이프 쿨링 요소 | `MISC.HEAT_OF_HYDRATION_PIPE_COOLING_ELEMENT` | Boolean | false | Optional |
| (14) | 그리드 모델 하중선(Grid Model Load Line) ᴶ⁾ | `MISC.GRID_MODEL_LOAD_LINE` | Boolean | false | Optional |

#### 7) View Display — `Argument.VIEW` (Object, Optional)

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 8 | 뷰 표시 옵션 그룹 | `VIEW` | Object | - | Optional |
| (1) | UCS 축(UCS Axis) | `VIEW.UCS_AXIS` | Boolean | false | Optional |
| (2) | 동적 뷰 제어(Viewport Gizmo) | `VIEW.VIEWPORT_GIZMO` | Boolean | false | Optional |
| (3) | 뷰 포인트(View Point) | `VIEW.VIEW_POINT` | Boolean | false | Optional |
| (4) | 설명(Description) | `VIEW.DESCRIPTION` | String | Blank | Optional |
| (5) | 라벨 방향(Label Orientation) | `VIEW.LABEL_ORIENTATION` | Integer | 0 | Optional |

> **각주(Footnotes)**
> - ˢ#⁾ : 상호 배타적 옵션. 같은 `#` 그룹 내에서는 하나만 선택 가능합니다.
> - ᴳ⁾ : MIDAS GEN NX 전용
> - ᴶ⁾ : MIDAS CIVIL NX JP 버전 전용

### Request / Response JSON

**POST Request Body — Node Display**

```json
{
  "Argument": {
    "NODE": {
      "NODE": false,
      "NODE_NUMBER": false,
      "STORY_NAME": false,
      "NODE_LOCAL_AXIS": false
    }
  }
}
```

**POST Request Body — Element Display**

```json
{
  "Argument": {
    "ELEMENT": {
      "ELEM_NUMBER": true,
      "ELEM_NUMBER_WITH_BORDER": true,
      "ELEM_TYPE_NUMBER": true,
      "ELEM_TYPE_NAME": true,
      "WALL_ID": true,
      "GAP": true,
      "HOOK": true,
      "CABLE": true,
      "LOCAL_AXIS": true,
      "LOCAL_AXIS_LABEL": true,
      "LOCAL_DIRECTION": true,
      "SUB_DOMAIN_REBAR_DIRECTION": true
    }
  }
}
```

**POST Request Body — Boundary Display**

```json
{
  "Argument": {
    "GROUP_SELECTION": ["Bndr Group 1"],
    "BOUNDARY": {
      "SUPPORT": true,
      "SUPPORT_BY_DIRECTION": true,
      "POINT_SPRING_SUPPORT": true,
      "ELASTIC_LINK": true,
      "ELASTIC_LINK_LOCAL_AXIS": true,
      "GENERAL_LINK": true,
      "RIGID_LINK": true,
      "REACTION_POSITION": true,
      "STORY_DIAPHRAGM": true,
      "DIAPHRAGM_DISCONNECT": true
    }
  }
}
```

**POST Request Body — Load Display**

```json
{
  "Argument": {
    "LOAD": {
      "CASE_SELECTION": {
        "TYPE": "st",
        "NAME": "DL"
      },
      "GROUP_SELECTION": ["Load Group 1", "Load Group 2", "Load Group 3"],
      "LOAD_VALUE": {
        "FORMAT": "Fixed",
        "PLACE": 1
      },
      "NODAL_LOAD": true,
      "BEAM_LOAD": true,
      "PRESSURE_LOAD": true,
      "WIND_LOAD": true,
      "SEISMIC_LOAD": true
    }
  }
}
```

**POST Request Body — View Display**

```json
{
  "Argument": {
    "VIEW": {
      "UCS_AXIS": true,
      "VIEWPORT_GIZMO": true,
      "VIEW_POINT": true,
      "DESCRIPTION": "Test",
      "LABEL_ORIENTATION": 15
    }
  }
}
```

**POST Response Body**

```json
{
  "DISPLAY": "Display settings updated."
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

# ── POST: 요소 표시 항목 + 하중 표시 + 뷰 옵션 설정 ────────────────
payload = {
    "Argument": {
        "ELEMENT": {
            "ELEM_NUMBER": True,          # 요소 번호 표시
            "ELEM_TYPE_NAME": True,       # 요소 타입 이름 표시
            "LOCAL_AXIS": True,           # 국부좌표축 표시
            "LOCAL_AXIS_LABEL": True      # 국부축 라벨(LOCAL_AXIS가 True일 때)
        },
        "LOAD": {
            "CASE_SELECTION": {"TYPE": "st", "NAME": "DL"},   # 정적하중 케이스
            "GROUP_SELECTION": ["Load Group 1"],              # 표시할 하중 그룹
            "LOAD_VALUE": {"FORMAT": "Fixed", "PLACE": 1},    # 고정 소수점 1자리
            "NODAL_LOAD": True,           # 절점 하중 표시
            "BEAM_LOAD": True             # 보 하중 표시
        },
        "VIEW": {
            "UCS_AXIS": True,             # UCS 축 표시
            "VIEWPORT_GIZMO": True,       # 동적 뷰 제어 기즈모
            "LABEL_ORIENTATION": 15       # 라벨 방향(각도)
        }
    }
}
resp = requests.post(f"{BASE_URL}/view/DISPLAY", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 7. `/view/RESULTGRAPHIC` — Result Graphic

> **기능:** 반력/변위/보 다이어그램/평면·판 응력/솔리드 응력 등 해석 결과를 모델 창에 그래픽으로 표시하는 방식을 제어합니다. 현재 결과 모드(`CURRENT_MODE`), 하중 케이스/조합(`LOAD_CASE_COMB`), 성분(`COMPONENTS`)과 함께 `TYPE_OF_DISPLAY` 객체 아래에서 컨투어(Contour)·수치(Values)·범례(Legend)·변형(Deform)·표시옵션·대칭 미러·절단 다이어그램/평면·재하하중·등가면(IsoSurface) 등을 세부 설정합니다. 이 엔드포인트는 `POST` 전용입니다.

### Input URI

```
{base url}/view/RESULTGRAPHIC
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "RESULTGRAPHIC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "ArgumentSchema",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TYPE_OF_DISPLAY": {
            "type": "object",
            "description": "TypeofDisplay",
            "properties": {
              "CONTOUR": {
                "type": "object",
                "description": "ContourDetails",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "NUM_OF_COLOR": { "type": "integer", "description": "SelecttheNumberofColortoDrawtheContour" },
                  "COLOR_TYPE": {
                    "type": "string",
                    "description": "SelecttheTypeofColors",
                    "enum": ["vrgb", "rgb", "brg", "grayscaled"]
                  },
                  "OPTIONS": {
                    "type": "object",
                    "description": "SpecifyOptionsforContourRepresentation",
                    "properties": {
                      "CONTOUR_FILL": { "type": "boolean", "description": "SelecttheTypeofFill" },
                      "GRADIENT_FILL": { "type": "boolean", "description": "GradientFill" }
                    }
                  }
                }
              },
              "VALUES": {
                "type": "object",
                "description": "ValuesOutputDetails",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "VALUE_EXP": { "type": "boolean", "description": "SelectExponentialorFixedValue" },
                  "DECIMAL_PT": { "type": "integer", "description": "SelecttheNumberofDecimalPlacestoDisplay" },
                  "SET_ORIENT": { "type": "integer", "description": "SetstheOrientationoftheValue" },
                  "MINMAX_ONLY": {
                    "type": "object",
                    "description": "Enable'MinMaxOnly'",
                    "properties": {
                      "MAXMIN": {
                        "type": "string",
                        "description": "MinMaxTypeofValues",
                        "enum": ["Min&Max", "AbsMax", "Max", "Min"]
                      },
                      "LIMIT_SCALE": { "type": "integer", "description": "LimitScale" }
                    }
                  }
                }
              },
              "LEGEND": {
                "type": "object",
                "description": "LegendDetails",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "POSITION": {
                    "type": "string",
                    "description": "Positionofthelegendinthedisplaywindow",
                    "enum": ["right", "left"]
                  },
                  "VALUE_EXP": { "type": "boolean", "description": "SelectExponentialorFixedValue" },
                  "DECIMAL_PT": { "type": "integer", "description": "SelecttheNumberofDecimalPlacestoDisplay" }
                }
              },
              "DEFORM": {
                "type": "object",
                "description": "DeformationDetails",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "SCALE_FACTOR": { "type": "number", "description": "DeformationScaleFactor" },
                  "REAL_DEFORM": { "type": "boolean", "description": "DeformationType" },
                  "REL_DISP": { "type": "boolean", "description": "RelativeDeformation" },
                  "REAL_DISP": { "type": "boolean", "description": "RealStructuralDeformation" }
                }
              },
              "DISP_OPT": {
                "type": "object",
                "description": "DisplayOptionDetails",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "ELEMENT_CENTER": { "type": "boolean", "description": "PlaceContourinElementCenter" },
                  "VALUE_MAX": { "type": "boolean", "description": "SelectShowingValuesofMaximumorElementCenter" }
                }
              },
              "MIRRORED": {
                "type": "object",
                "description": "SymmetricModelMirrorDetail",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "MIRROR_BY_1": {
                    "type": "object",
                    "description": "MirrorByHalfModel",
                    "properties": {
                      "DIRECTION": {
                        "type": "string",
                        "description": "MirrorByDirection(Half)",
                        "enum": ["XY", "YZ", "XZ"]
                      },
                      "OFFSET": { "type": "number", "description": "MirrorByOffsetDistance(Half)" }
                    }
                  },
                  "MIRROR_BY_2": {
                    "type": "object",
                    "description": "MirrorByHalfModel",
                    "properties": {
                      "DIRECTION": {
                        "type": "string",
                        "description": "MirrorByDirection(Quarter)",
                        "enum": ["XY", "YZ", "XZ"]
                      },
                      "OFFSET": { "type": "number", "description": "MirrorByOffsetDistance(Quarter)" }
                    }
                  }
                }
              },
              "CUTTING_DIAGRAM": {
                "type": "object",
                "description": "CuttingDiagram",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "CUTTING_MODE": {
                    "type": "string",
                    "description": "CuttingDiagramMode",
                    "enum": ["line", "plane"]
                  },
                  "CUTTING_NAME": {
                    "type": "array",
                    "description": "SelectCuttingLineorPlane",
                    "items": { "type": "string" }
                  },
                  "NORMAL_TO_PLANE": { "type": "boolean", "description": "DisplaytheGraphDirectionOptionofPlateElements" },
                  "SCALE_FACTOR": { "type": "number", "description": "ScaleFactorforDiagramOutputRatio" },
                  "REVERSE": { "type": "boolean", "description": "ExpresstheDiagramintheReverseDirection" },
                  "VALUE_OUTPUT": { "type": "boolean", "description": "ProducetheOutputinValues" },
                  "MINMAX_ONLY": { "type": "boolean", "description": "ShowonlytheMaximumandMinimumvalues" }
                }
              },
              "CUTTING_PLANE": {
                "type": "object",
                "description": "CuttingPlaneDetailDialog",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "PLANE_NAME": {
                    "type": "array",
                    "description": "SelecttheCuttingPlanes",
                    "items": { "type": "string" }
                  },
                  "FREE_EDGE": { "type": "boolean", "description": "DrawtheOutlineOption" }
                }
              },
              "APPLIED_LOADS": {
                "type": "object",
                "description": "AppliedLoads(MovingLoadTracerDetail)",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "SCALE_FACTOR": { "type": "number", "description": "LoadScaleFactor" },
                  "OPT_LOAD_VALUES": { "type": "boolean", "description": "ShowLoadValues" },
                  "VALUE_TYPE": {
                    "type": "string",
                    "description": "SelecttheValueOutputType",
                    "enum": ["Exponential", "Fixed"]
                  },
                  "VALUE_DECIMAL_PT": { "type": "integer", "description": "ValueOutputDecimalPoint" }
                }
              },
              "ISO_SURFACE": {
                "type": "object",
                "description": "IsoSurfaceDetailDialog",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "DRAW_POLYLINE": { "type": "boolean", "description": "DrawPolygonOutline" },
                  "TRANSPARENCY": { "type": "number", "description": "Transparent(ScreenOnly)" },
                  "FREE_EDGE": { "type": "boolean", "description": "Outline(highlight)theSolidElementMode" },
                  "VALUE_MODE": {
                    "type": "object",
                    "description": "SelecttheValuestobeDisplayedforStress",
                    "properties": {
                      "VALUE_TYPE": {
                        "type": "string",
                        "enum": ["relative", "values"],
                        "description": "IsoSurfaceValuesType"
                      },
                      "VALUE": {
                        "type": "array",
                        "items": { "type": "number" },
                        "description": "IsoSurfaceValues"
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
}
```

> **참고:** 위 JSON Schema는 `Argument.TYPE_OF_DISPLAY` 하위만 상세히 정의합니다. 실제 요청에서는 `TYPE_OF_DISPLAY`와 함께 결과 모드 지정용 최상위 키(`CURRENT_MODE`, `LOAD_CASE_COMB`, `COMPONENTS`, `DISPLAY_OPTIONS`, `OPTIONS`, `OUTPUT_SECT_LOCATION` 등)를 함께 전달합니다. 결과 항목(모드)마다 사용 가능한 키가 다르므로 해당 항목의 매뉴얼을 참조하십시오. 또한 Specifications에는 스키마에 없는 추가 `TYPE_OF_DISPLAY` 하위 키(`UNDEFORMED`, `ARROW_SCALE_FACTOR`, `OPT_CUR_STEP_DISPLACEMENT` 등)가 정의되어 있어 아래 파라미터 표에 모두 포함했습니다.

### Parameters

#### 1) Type of Display — `Argument.TYPE_OF_DISPLAY` (Object, Optional)

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 표시 유형(Type of Display) | `TYPE_OF_DISPLAY` | Object | System | Optional |
| (1) | 컨투어 상세(Contour Details) | `TYPE_OF_DISPLAY.CONTOUR` | Object | - | Optional |
| (2) | 수치 출력 상세(Values Output Details) | `TYPE_OF_DISPLAY.VALUES` | Object | - | Optional |
| (3) | 범례 상세(Legend Details) | `TYPE_OF_DISPLAY.LEGEND` | Object | - | Optional |
| (4) | 변형 상세(Deformation Details) | `TYPE_OF_DISPLAY.DEFORM` | Object | - | Optional |
| (5) | 표시 옵션 상세(Display Option Details) | `TYPE_OF_DISPLAY.DISP_OPT` | Object | - | Optional |
| (6) | 대칭 모델 미러 상세(Symmetric Model Mirror) | `TYPE_OF_DISPLAY.MIRRORED` | Object | - | Optional |
| (7) | 절단 다이어그램(Cutting Diagram) | `TYPE_OF_DISPLAY.CUTTING_DIAGRAM` | Object | - | Optional |
| (8) | 절단 평면 상세(Cutting Plane Detail) | `TYPE_OF_DISPLAY.CUTTING_PLANE` | Object | - | Optional |
| (9) | 재하 하중(Applied Loads, 이동하중 추적) | `TYPE_OF_DISPLAY.APPLIED_LOADS` | Object | - | Optional |
| (10) | 등가면 상세(IsoSurface Detail) | `TYPE_OF_DISPLAY.ISO_SURFACE` | Object | - | Optional |
| (11) | 미변형 형상 표시(Display Undeformed Shape) | `TYPE_OF_DISPLAY.UNDEFORMED` | Object | - | Optional |
| (12) | 화살표 스케일 계수(Arrow Scale Factor) | `TYPE_OF_DISPLAY.ARROW_SCALE_FACTOR` | Number | 1 | Optional |
| (13) | 현재 스텝 변위 | `TYPE_OF_DISPLAY.OPT_CUR_STEP_DISPLACEMENT` | Boolean | false | Optional |
| (14) | 단계/스텝 실제 변위 | `TYPE_OF_DISPLAY.OPT_STAGE_STEP_REAL_DISPLACEMENT` | Boolean | false | Optional |
| (15) | 캠버 변위 포함 | `TYPE_OF_DISPLAY.OPT_INCLUDING_CAMBER_DISPLACEMENT` | Boolean | false | Optional |
| (16) | 현재 스텝 힘(Current Step Force) | `TYPE_OF_DISPLAY.OPT_CUR_STEP_FORCE` | Boolean | false | Optional |
| (17) | 항복점(Yield Point) | `TYPE_OF_DISPLAY.YIELD_POINT` | Object | - | Optional |
| (18) | 충격계수 포함(Include Impact Factor) | `TYPE_OF_DISPLAY.OPT_INCLUDE_IMPACT_FACTOR` | Boolean | false | Optional |
| (19) | 모드 형상(Mode Shape) | `TYPE_OF_DISPLAY.MODE_SHAPE` | Object | - | Optional |
| (20) | 스케일 계수(Scale Factor) | `TYPE_OF_DISPLAY.SCALE_FACTOR` | Number | 1 | Optional |
| (21) | 3차 보간(Cubic Interpolation) | `TYPE_OF_DISPLAY.OPT_CUBIC_INTERPOLATION` | Boolean | false | Optional |
| (22) | 3차 보간 계수(Cubic Interpolation Factor) | `TYPE_OF_DISPLAY.CUBIC_INTERPOLATION_FACTOR` | Number | 0.5 | Optional |

#### 2) Contour Details — `TYPE_OF_DISPLAY.CONTOUR`

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 1 | 컨투어 상세 | `CONTOUR` | Object | - | Optional |
| (1) | 표시 유형 제어 (표시: true / 숨김: false) | `CONTOUR.OPT_CHECK` | Boolean | false | Optional |
| (2) | 컨투어 색상 개수 (6 / 12 / 18 / 24) | `CONTOUR.NUM_OF_COLOR` | Integer | 12 | Optional |
| (3) | 색상 타입 (V→R→G→B: `"vrgb"`, R→G→B: `"rgb"`, R→B→G: `"rbg"`, Gray Scaled: `"gray scaled"`) | `CONTOUR.COLOR_TYPE` | String | `"vrgb"` | Optional |
| (4) | 컨투어 표현 옵션 | `CONTOUR.OPTIONS` | Object | - | Optional |
| i. | 채움 방식 (Contour Fill: true / 선만 그림: false) | `CONTOUR.OPTIONS.CONTOUR_FILL` | Boolean | true | Optional |
| ii. | 그라디언트 채움 (`CONTOUR_FILL`이 true일 때) | `CONTOUR.OPTIONS.GRADIENT_FILL` | Boolean | false | Optional |

> 스키마 `enum` 정의값: `COLOR_TYPE` = `["vrgb", "rgb", "brg", "grayscaled"]` (Specifications 표기와 상이하며, Specifications 기준 값은 `"vrgb"`/`"rgb"`/`"rbg"`/`"gray scaled"` 입니다).

#### 3) Values Output Details — `TYPE_OF_DISPLAY.VALUES`

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 1 | 수치 출력 상세 | `VALUES` | Object | - | Optional |
| (1) | 표시 유형 제어 (표시: true / 숨김: false) | `VALUES.OPT_CHECK` | Boolean | false | Optional |
| (2) | 지수/고정 표기 선택 (지수: true / 고정: false) | `VALUES.VALUE_EXP` | Boolean | false | Optional |
| (3) | 소수점 자리수 | `VALUES.DECIMAL_PT` | Integer | 0 | Optional |
| (4) | 수치 방향(0~180, 15 단위 증가) | `VALUES.SET_ORIENT` | Integer | 0 | Optional |
| (5) | "MinMax Only" 활성화 | `VALUES.MINMAX_ONLY` | Object | - | Optional |
| i. | MinMax 유형 (Min.&Max.: `"Min & Max"`, Abs Max.: `"Abs Max"`, Max: `"Max"`, Min: `"Min"`) | `VALUES.MINMAX_ONLY.MAXMIN` | String | `"Min & Max"` | Optional |
| ii. | 한계 스케일(Limit Scale, 0~100) | `VALUES.MINMAX_ONLY.LIMIT_SCALE` | Integer | 0 | Optional |

> 스키마 `enum` 정의값: `MAXMIN` = `["Min&Max", "AbsMax", "Max", "Min"]`.

#### 4) Legend Details — `TYPE_OF_DISPLAY.LEGEND`

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 1 | 범례 상세 | `LEGEND` | Object | - | Optional |
| (1) | 표시 유형 제어 (표시: true / 숨김: false) | `LEGEND.OPT_CHECK` | Boolean | false | Optional |
| (2) | 범례 위치 (오른쪽: `"right"`, 왼쪽: `"left"`) | `LEGEND.POSITION` | String | `"left"` | Optional |
| (3) | 지수/고정 표기 선택 (지수: true / 고정: false) | `LEGEND.VALUE_EXP` | Boolean | true | Optional |
| (4) | 소수점 자리수 (`VALUE_EXP`이 false일 때) | `LEGEND.DECIMAL_PT` | Integer | 0 | Optional |

#### 5) Deformation Details — `TYPE_OF_DISPLAY.DEFORM`

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 변형 상세 | `DEFORM` | Object | - | Optional |
| (1) | 표시 유형 제어 (표시: true / 숨김: false) | `DEFORM.OPT_CHECK` | Boolean | false | Optional |
| (2) | 변형 스케일 계수(변위 확대/축소) | `DEFORM.SCALE_FACTOR` | Number | 0 | Optional |
| (3) | 변형 유형 (Real Deform.: true / Nodal Deform: false) | `DEFORM.REAL_DEFORM` | Boolean | false | Optional |
| (4) | 상대 변형(Relative Deformation) | `DEFORM.REL_DISP` | Boolean | false | Optional |
| (5) | 실제 구조 변형 (스케일 없이 표시: true / 자동 스케일: false) | `DEFORM.REAL_DISP` | Boolean | false | Optional |

#### 6) Display Option Details — `TYPE_OF_DISPLAY.DISP_OPT`

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 표시 옵션 상세 | `DISP_OPT` | Object | - | Optional |
| (1) | 표시 유형 제어 (표시: true / 숨김: false) | `DISP_OPT.OPT_CHECK` | Boolean | false | Optional |
| (2) | 요소 중심에 컨투어 배치 (표시: true / 숨김: false) | `DISP_OPT.ELEMENT_CENTER` | Boolean | false | Optional |
| (3) | 최댓값/요소 중심값 표시 선택 (최댓값: true / 요소 중심값: false) | `DISP_OPT.VALUE_MAX` | Boolean | false | Optional |

#### 7) Symmetric Model Mirror Detail — `TYPE_OF_DISPLAY.MIRRORED`

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 1 | 대칭 모델 미러 상세 | `MIRRORED` | Object | - | Optional |
| (1) | 표시 유형 제어 (표시: true / 숨김: false) | `MIRRORED.OPT_CHECK` | Boolean | false | Optional |
| (2) | 절반 모델 미러(Half) | `MIRRORED.MIRROR_BY_1` | Object | - | Required |
| i. | 미러 방향(Half) (XY-Plane at Z: `"XY"`, YZ-Plane at X: `"YZ"`, XZ-Plane at Y: `"XZ"`) | `MIRRORED.MIRROR_BY_1.DIRECTION` | String | - | Required |
| ii. | 미러 오프셋 거리(Half) | `MIRRORED.MIRROR_BY_1.OFFSET` | Number | - | Required |
| (3) | 1/4 모델 미러(Quarter) | `MIRRORED.MIRROR_BY_2` | Object | - | Optional |
| i. | 미러 방향(Quarter) (`"XY"` / `"YZ"` / `"XZ"`) | `MIRRORED.MIRROR_BY_2.DIRECTION` | String | - | Required |
| ii. | 미러 오프셋 거리(Quarter) | `MIRRORED.MIRROR_BY_2.OFFSET` | Number | - | Required |

#### 8) Cutting Diagram — `TYPE_OF_DISPLAY.CUTTING_DIAGRAM`

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 1 | 절단 다이어그램 | `CUTTING_DIAGRAM` | Object | - | Optional |
| (1) | 표시 유형 제어 (표시: true / 숨김: false) | `CUTTING_DIAGRAM.OPT_CHECK` | Boolean | false | Optional |
| (2) | 절단 모드 (Cutting Line: `"line"`, Cutting Plane: `"plane"`) | `CUTTING_DIAGRAM.CUTTING_MODE` | String | `"line"` | Optional |
| (3) | 절단선/절단면 선택 (정의된 Cutting Line 이름 ᶜᵁᵀᴸ⁾, 또는 Current UCS 평면 `"XY"`/`"XZ"`/`"YZ"`, 또는 명명 평면 고유키 db/NPLN) | `CUTTING_DIAGRAM.CUTTING_NAME` | Array[String] | - | Required |
| (4) | 판 요소 그래프 방향 옵션 (법선방향: true / 면내방향: false) | `CUTTING_DIAGRAM.NORMAL_TO_PLANE` | Boolean | true | Optional |
| (5) | 다이어그램 출력 비율 스케일 계수 | `CUTTING_DIAGRAM.SCALE_FACTOR` | Number | 0 | Optional |
| (6) | 다이어그램 역방향 표현 (Reverse: true / Normal: false) | `CUTTING_DIAGRAM.REVERSE` | Boolean | false | Optional |
| (7) | 수치로 출력 (활성: true / 비활성: false) | `CUTTING_DIAGRAM.VALUE_OUTPUT` | Boolean | false | Optional |
| (8) | 최대/최솟값만 표시 (`VALUE_OUTPUT`이 true일 때) | `CUTTING_DIAGRAM.MINMAX_ONLY` | Boolean | false | Optional |

> ᶜᵁᵀᴸ⁾ : Cutting Line Function(db/CUTL)으로 정의된 절단선.

#### 9) Cutting Plane Detail Dialog — `TYPE_OF_DISPLAY.CUTTING_PLANE`

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 1 | 절단 평면 상세 | `CUTTING_PLANE` | Object | - | Optional |
| (1) | 표시 유형 제어 (표시: true / 숨김: false) | `CUTTING_PLANE.OPT_CHECK` | Boolean | false | Optional |
| (2) | 절단 평면 선택 (Current UCS x-y: `"XY"`, x-z: `"XZ"`, y-z: `"YZ"`, 또는 명명 평면 고유키 db/NPLN) | `CUTTING_PLANE.PLANE_NAME` | Array[String] | - | Required |
| (3) | 외곽선 그리기 옵션 (Free Edge: true / Free Face: false) | `CUTTING_PLANE.FREE_EDGE` | Boolean | true | Optional |

#### 10) Applied Loads (Moving Load Tracer Detail) — `TYPE_OF_DISPLAY.APPLIED_LOADS`

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 1 | 재하 하중(이동하중 추적) 상세 | `APPLIED_LOADS` | Object | - | Optional |
| (1) | 표시 유형 제어 (표시: true / 숨김: false) | `APPLIED_LOADS.OPT_CHECK` | Boolean | false | Optional |
| (2) | 하중 스케일 계수 | `APPLIED_LOADS.SCALE_FACTOR` | Number | 0 | Optional |
| (3) | 하중값 표시 (활성: true / 비활성: false) | `APPLIED_LOADS.OPT_LOAD_VALUES` | Boolean | false | Optional |
| (4) | 값 출력 타입 (`OPT_LOAD_VALUES`이 true일 때 — 지수: `"Exponential"`, 고정: `"Fixed"`) | `APPLIED_LOADS.VALUE_TYPE` | String | `"Exponential"` | Optional |
| (5) | 값 출력 소수점 자리 (`OPT_LOAD_VALUES`이 true일 때, 0 이상) | `APPLIED_LOADS.VALUE_DECIMAL_PT` | Integer | 0 | Optional |

#### 11) IsoSurface Detail Dialog — `TYPE_OF_DISPLAY.ISO_SURFACE`

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 1 | 등가면(IsoSurface) 상세 | `ISO_SURFACE` | Object | - | Optional |
| (1) | 표시 유형 제어 (표시: true / 숨김: false) | `ISO_SURFACE.OPT_CHECK` | Boolean | false | Optional |
| (2) | 폴리곤 외곽선 그리기 (활성: true / 비활성: false) | `ISO_SURFACE.DRAW_POLYLINE` | Boolean | false | Optional |
| (3) | 투명도(화면 전용, 최대 255 / 최소 0) | `ISO_SURFACE.TRANSPARENCY` | Number | 255 | Optional |
| (4) | 솔리드 요소 외곽선 강조 (Free Face: true / Free Edge: false) | `ISO_SURFACE.FREE_EDGE` | Boolean | true | Optional |
| (5) | 응력 표시 값 선택 | `ISO_SURFACE.VALUE_MODE` | Object | - | Optional |
| i. | 등가면 값 타입 (Relative: `"relative"`, Values: `"values"`) | `ISO_SURFACE.VALUE_MODE.VALUE_TYPE` | String | `"relative"` | Optional |
| ii. | 등가면 값 (Relative Type: 최대 1 / 최소 0) | `ISO_SURFACE.VALUE_MODE.VALUE` | Array[Number] | - | Required |

### Request / Response JSON

**POST Request Body — Contour Details (보 다이어그램 결과)**

```json
{
  "Argument": {
    "CURRENT_MODE": "beamdiagrams",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "DL"
    },
    "COMPONENTS": {
      "PART": "total",
      "COMP": "Fx"
    },
    "DISPLAY_OPTIONS": {
      "FIDELITY": "Exact",
      "FILL": "line",
      "SCALE": 1.0
    },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 6,
        "COLOR_TYPE": "rgb",
        "OPTIONS": {
          "GRADIENT_FILL": false,
          "CONTOUR_FILL": false
        }
      }
    },
    "OUTPUT_SECT_LOCATION": {
      "OPT_I": true,
      "OPT_CENTER_MID": true,
      "OPT_J": true
    }
  }
}
```

**POST Request Body — Values Output Details (반력 결과)**

```json
{
  "Argument": {
    "CURRENT_MODE": "reactionforces/moments",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "DL"
    },
    "COMPONENTS": {
      "COMP": "Fxyz",
      "OPT_LOCAL_CHECK": true
    },
    "TYPE_OF_DISPLAY": {
      "VALUES": {
        "OPT_CHECK": true,
        "DECIMAL_PT": 5,
        "VALUE_EXP": true,
        "MINMAX_ONLY": {
          "MAXMIN": "absmax",
          "LIMIT_SCALE": 5
        },
        "SET_ORIENT": 15
      },
      "ARROW_SCALE_FACTOR": 1.0
    }
  }
}
```

**POST Request Body — Deformation Details (변형 + 컨투어)**

```json
{
  "Argument": {
    "CURRENT_MODE": "beamdiagrams",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "DL"
    },
    "COMPONENTS": {
      "PART": "total",
      "COMP": "Fx"
    },
    "DISPLAY_OPTIONS": {
      "FIDELITY": "Exact",
      "FILL": "line",
      "SCALE": 1.0
    },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 6,
        "COLOR_TYPE": "rgb",
        "OPTIONS": {
          "GRADIENT_FILL": false,
          "CONTOUR_FILL": false
        }
      },
      "DEFORM": {
        "OPT_CHECK": true,
        "SCALE_FACTOR": 2.0,
        "REL_DISP": true,
        "REAL_DISP": true,
        "REAL_DEFORM": true
      }
    },
    "OUTPUT_SECT_LOCATION": {
      "OPT_I": true,
      "OPT_CENTER_MID": true,
      "OPT_J": true
    }
  }
}
```

**POST Request Body — Symmetric Model Mirror (평면/판 응력)**

```json
{
  "Argument": {
    "CURRENT_MODE": "Plane-Stress/PlateStresses",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "SelfWeight",
      "STEP_INDEX": 1
    },
    "OPTIONS": {
      "LOCAL_UCS": {
        "TYPE": "UCS",
        "UCS_NAME": "CurrentUCS"
      },
      "AVERAGE_NODAL": {
        "TYPE": "Avg.Nodal"
      },
      "SURFACE": "Top"
    },
    "COMPONENTS": {
      "COMP": "Sig-eff"
    },
    "TYPE_OF_DISPLAY": {
      "MIRRORED": {
        "OPT_CHECK": true,
        "MIRROR_BY_1": {
          "DIRECTION": "YZ",
          "OFFSET": 3
        },
        "MIRROR_BY_2": {
          "DIRECTION": "XZ",
          "OFFSET": 5
        }
      }
    }
  }
}
```

**POST Request Body — IsoSurface Detail (솔리드 응력)**

```json
{
  "Argument": {
    "CURRENT_MODE": "solidstresses",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "DL",
      "STEP_INDEX": 1
    },
    "OPTIONS": {
      "LOCAL_UCS": {
        "TYPE": "UCS",
        "UCS_NAME": "CurrentUCS"
      },
      "AVERAGE_NODAL": {
        "TYPE": "Avg.Nodal"
      }
    },
    "COMPONENTS": {
      "COMP": "Sig-eff"
    },
    "TYPE_OF_DISPLAY": {
      "ISO_SURFACE": {
        "OPT_CHECK": true,
        "DRAW_POLYLINE": true,
        "FREE_EDGE": false,
        "TRANSPARENCY": 50,
        "VALUE_MODE": {
          "VALUE_TYPE": "relative",
          "VALUE": [0, 0.25, 0.5, 0.75, 1]
        }
      }
    }
  }
}
```

**POST Response Body**

```json
{
  "RESULTGRAPHIC": "Result graphic display updated."
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

# ── POST: 반력(Reaction) 결과를 수치 + 범례로 표시 ─────────────────
def show_reaction_values():
    payload = {
        "Argument": {
            "CURRENT_MODE": "reactionforces/moments",   # 결과 모드: 반력/모멘트
            "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DL"},
            "COMPONENTS": {"COMP": "Fxyz", "OPT_LOCAL_CHECK": True},
            "TYPE_OF_DISPLAY": {
                "VALUES": {
                    "OPT_CHECK": True,
                    "VALUE_EXP": True,
                    "DECIMAL_PT": 5,
                    "SET_ORIENT": 15,
                    "MINMAX_ONLY": {"MAXMIN": "AbsMax", "LIMIT_SCALE": 5}
                },
                "LEGEND": {"OPT_CHECK": True, "POSITION": "right", "VALUE_EXP": True, "DECIMAL_PT": 2},
                "ARROW_SCALE_FACTOR": 1.0
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
    print("반력 표시:", resp.status_code, resp.json())


# ── POST: 보 다이어그램 결과를 컨투어 + 변형으로 표시 ──────────────
def show_beam_contour_with_deform():
    payload = {
        "Argument": {
            "CURRENT_MODE": "beamdiagrams",             # 결과 모드: 보 다이어그램
            "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DL"},
            "COMPONENTS": {"PART": "total", "COMP": "Fx"},
            "DISPLAY_OPTIONS": {"FIDELITY": "Exact", "FILL": "line", "SCALE": 1.0},
            "TYPE_OF_DISPLAY": {
                "CONTOUR": {
                    "OPT_CHECK": True,
                    "NUM_OF_COLOR": 6,
                    "COLOR_TYPE": "rgb",
                    "OPTIONS": {"CONTOUR_FILL": False, "GRADIENT_FILL": False}
                },
                "DEFORM": {
                    "OPT_CHECK": True,
                    "SCALE_FACTOR": 2.0,
                    "REAL_DEFORM": True,
                    "REL_DISP": True,
                    "REAL_DISP": True
                }
            },
            "OUTPUT_SECT_LOCATION": {"OPT_I": True, "OPT_CENTER_MID": True, "OPT_J": True}
        }
    }
    resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
    print("보 컨투어+변형 표시:", resp.status_code, resp.json())


show_reaction_values()
show_beam_contour_with_deform()
```

---

## End-to-End Workflow

다음은 해석 결과를 시점·활성화·표시 옵션과 함께 이미지로 캡처하는 워크플로우입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── STEP 1: 선택 상태 확인 ─────────────────────────────────────────
r1 = requests.get(f"{BASE_URL}/view/SELECT", headers=HEADERS)
print(f"STEP1 SELECT: {r1.status_code}, {r1.json().get('SELECT', {})}")

# ── STEP 2: 시점 설정 ──────────────────────────────────────────────
r2 = requests.post(f"{BASE_URL}/view/ANGLE",
                   json={"Argument": {"HORIZONTAL": 30, "VERTICAL": 15}}, headers=HEADERS)
print(f"STEP2 ANGLE: {r2.status_code}")

# ── STEP 3: 특정 그룹만 활성화 ─────────────────────────────────────
r3 = requests.post(f"{BASE_URL}/view/ACTIVE",
                   json={"Argument": {"ACTIVE_MODE": "Identity",
                                      "IDENTITY_TYPE": "Group",
                                      "IDENTITY_LIST": ["Girder"]}}, headers=HEADERS)
print(f"STEP3 ACTIVE: {r3.status_code}")

# ── STEP 4: 시점·활성화·표시·결과그래픽을 통합하여 이미지 캡처 ─────
capture_payload = {
    "Argument": {
        "SET_MODE": "post",
        "EXPORT_PATH": "C:\\MIDAS\\report\\girder_moment.jpg",
        "WIDTH": 1600, "HEIGHT": 900,
        "ANGLE": {"HORIZONTAL": 30, "VERTICAL": 15},
        "ACTIVE": {"ACTIVE_MODE": "Identity", "IDENTITY_TYPE": "Group", "IDENTITY_LIST": ["Girder"]},
        "DISPLAY": {"PERSPECTIVE": True, "ZOOM_LEVEL": 100},
        "RESULT_GRAPHIC": {
            "CURRENT_MODE": "beam diagrams",
            "LOAD_CASE_COMB": {"TYPE": "CB", "NAME": "cLCB1"},
            "COMPONENTS": {"PART": "total", "COMP": "My"},
            "TYPE_OF_DISPLAY": {"CONTOUR": {"OPT_CHECK": True}, "LEGEND": {"OPT_CHECK": True}}
        }
    }
}
r4 = requests.post(f"{BASE_URL}/view/CAPTURE", json=capture_payload, headers=HEADERS)
print(f"STEP4 CAPTURE: {r4.status_code}")
```
