# 16-2. VIEW – Result Graphic 결과 모드별 요청

> **Source**: [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)
> **작성일**: 2026-11-26 (공식 개별 글 28건 기준)

[16장 7절 `/view/RESULTGRAPHIC`](./16_VIEW.md#7-viewresultgraphic--result-graphic)의 결과 모드(`CURRENT_MODE`)별 파라미터와 요청 예제입니다.
`TYPE_OF_DISPLAY` 하위 항목의 공통 상세는 16장 7절을, 수화열 결과 모드는 [22장 그룹 C](./22_POST_TH_HY_Pushover.md)를 보세요.

## 공통 사항

- **Input URI**: `{base url}/view/RESULTGRAPHIC`
- **Active Methods**: `POST`
- 요청 바디는 `"Argument"` 객체입니다.

> ⚠️ **`CURRENT_MODE` 표기:** 공식 Specifications 표는 `"Plate Forces/Moments"`처럼 공백을 넣어 적고,
> 요청 예제와 JSON Schema는 대부분 `"PlateForces/Moments"`처럼 공백 없이 적습니다. 이 문서는 **예제
> 표기**를 씁니다. 파라미터 설명은 공식 원문(영문) 그대로입니다.

<!-- om-fields:35997813329177 -->
**OM 원문 추가 필드 — Plate Forces/Moments - Result Display ([35997813329177](https://support.midasuser.com/hc/en-us/articles/35997813329177))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `OPT_CUR_STEP_FORCE`, `OPT_MAXMIN_DIAGRAM`

<!-- /om-fields -->


## 결과 모드 목록 (28개)

| No. | 결과 | `CURRENT_MODE` | 예제 수 |
| --- | --- | --- | --- |
| 1 | [Reaction Forces/Moments (Result Display)](#1-reaction-forcesmoments-result-display) | `"ReactionForces/Moments"` | 1 |
| 2 | [Soil Pressure (Result Display)](#2-soil-pressure-result-display) | `"SoilPressure"` | 1 |
| 3 | [Deformed Shape (Result Display)](#3-deformed-shape-result-display) | `"DeformedShape"` | 1 |
| 4 | [Displacement Contour (Result Display)](#4-displacement-contour-result-display) | `"DisplacementContour"` | 1 |
| 5 | [Truss Forces (Result Display)](#5-truss-forces-result-display) | `"TrussForces"` | 1 |
| 6 | [Beam Forces/Moments (Result Display)](#6-beam-forcesmoments-result-display) | `"BeamForces/Moments"` | 1 |
| 7 | [Beam Diagrams (Result Display)](#7-beam-diagrams-result-display) | `"BeamDiagrams"` | 1 |
| 8 | [Plate Forces/Moments (Result Display)](#8-plate-forcesmoments-result-display) | `"PlateForces/Moments"` | 4 |
| 9 | [Plate Cutting Line Diagram (Result Display)](#9-plate-cutting-line-diagram-result-display) | `"PlateCuttingLineDiagram"` | 2 |
| 10 | [Resultant Force Diagram (Result Display)](#10-resultant-force-diagram-result-display) | `"Resultant Force Diagram"` | 1 |
| 11 | [Truss Stresses (Result Display)](#11-truss-stresses-result-display) | `"TrussStresses"` | 1 |
| 12 | [Beam Stresses (Result Display)](#12-beam-stresses-result-display) | `"BeamStresses"` | 1 |
| 13 | [Beam Stresses Diagram (Result Display)](#13-beam-stresses-diagram-result-display) | `"BeamStressesDiagram"` | 1 |
| 14 | [Beam Stresses (Equivalent) (Result Display)](#14-beam-stresses-equivalent-result-display) | `"BeamStresses(Equivalent)"` | 1 |
| 15 | [Beam Stresses Diagram (Equivalent) (Result Display)](#15-beam-stresses-diagram-equivalent-result-display) | `"BeamStressesDiagram(Equivalent)"` | 1 |
| 16 | [Beam Stresses (PSC) (Result Display)](#16-beam-stresses-psc-result-display) | `"BeamStresses(PSC)"` | 1 |
| 17 | [Plane-Stress/Plate Stresses (Result Display)](#17-plane-stressplate-stresses-result-display) | `"Plane-Stress/PlateStresses"` | 3 |
| 18 | [Plane Strain Stresses (Result Display)](#18-plane-strain-stresses-result-display) | `"PlaneStrainStresses"` | 3 |
| 19 | [Axisymmetric Stresses (Result Display)](#19-axisymmetric-stresses-result-display) | `"AxisymmetricStresses"` | 3 |
| 20 | [Solid Stresses (Result Display)](#20-solid-stresses-result-display) | `"SolidStresses"` | 3 |
| 21 | [Reactions (Moving Tracer Display)](#21-reactions-moving-tracer-display) | `"MVLTRC_Reactions"` | 1 |
| 22 | [Displacements (Moving Tracer Display)](#22-displacements-moving-tracer-display) | `"MVLTRC_Displacements"` | 1 |
| 23 | [Truss Forces (Moving Tracer Display)](#23-truss-forces-moving-tracer-display) | `"MVLTRC_TrussForces"` | 1 |
| 24 | [Beam Forces/Moments (Moving Tracer Display)](#24-beam-forcesmoments-moving-tracer-display) | `"MVLTRC_BeamForces/Moments"` | 1 |
| 25 | [Plate Forces/Moments (Moving Tracer Display)](#25-plate-forcesmoments-moving-tracer-display) | `"MVLTRC_PlateForces/Moments"` | 1 |
| 26 | [Beam Stresses (Moving Tracer Display)](#26-beam-stresses-moving-tracer-display) | `"MVLTRC_BeamStresses"` | 1 |
| 27 | [Vibration Mode Shapes (Mode Shapes Display)](#27-vibration-mode-shapes-mode-shapes-display) | `"VibrationModeShapes"` | 1 |
| 28 | [Buckling Mode Shapes (Mode Shapes Display)](#28-buckling-mode-shapes-mode-shapes-display) | `"Buckling Mode Shapes"` | 1 |

<!-- om-fields:35996812786841 -->
**OM 원문 추가 필드 — Type of Display ([35996812786841](https://support.midasuser.com/hc/en-us/articles/35996812786841))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (4) | Contour Line Color | `"CONTOUR_LINE_COLOR"` | Object | - | Optional |
| (5) | Element Edge Color | `"ELEMENT_EDGE_COLOR"` | Object | - | Optional |

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `OPT_INCLUDE_IMPFACT_FACTOR`

<!-- /om-fields -->

<!-- om-fields:35997661413785 -->
**OM 원문 추가 필드 — Truss Forces - Result Display ([35997661413785](https://support.midasuser.com/hc/en-us/articles/35997661413785))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `OPT_IJ_MAX_ALL`

<!-- /om-fields -->

<!-- om-fields:35997711810969 -->
**OM 원문 추가 필드 — Beam Forces/Moments - Result Display ([35997711810969](https://support.midasuser.com/hc/en-us/articles/35997711810969))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `OPT_MAX_MIN_MAX_ALL`

<!-- /om-fields -->

<!-- om-fields:36001119330969 -->
**OM 원문 추가 필드 — Beam Stresses - Result Display ([36001119330969](https://support.midasuser.com/hc/en-us/articles/36001119330969))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `OPT_MAX_MIN_MAX_ALL`

<!-- /om-fields -->

<!-- om-fields:36001679829785 -->
**OM 원문 추가 필드 — Beam Stresses Diagram - Result Display ([36001679829785](https://support.midasuser.com/hc/en-us/articles/36001679829785))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `OPT_MAX_MIN_MAX_ALL`

<!-- /om-fields -->

<!-- om-fields:36002326176665 -->
**OM 원문 추가 필드 — Beam Stresses (Equivalent) - Result Display ([36002326176665](https://support.midasuser.com/hc/en-us/articles/36002326176665))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `OPT_MAX_MIN_MAX_ALL`

<!-- /om-fields -->

<!-- om-fields:36002496760217 -->
**OM 원문 추가 필드 — Beam Stresses Diagram (Equivalent) - Result Display ([36002496760217](https://support.midasuser.com/hc/en-us/articles/36002496760217))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `OPT_MAX_MIN_MAX_ALL`

<!-- /om-fields -->

<!-- om-fields:36002716977817 -->
**OM 원문 추가 필드 — Beam Stresses (PSC) - Result Display ([36002716977817](https://support.midasuser.com/hc/en-us/articles/36002716977817))**

공식 글의 Specifications 표 중 위 섹션에 없던 행을 원문 그대로 옮겼습니다.

Schema·요청 예제에만 있는 Key (원문 오탈자 포함 가능): `OPT_MAX_MIN_MAX_ALL`

<!-- /om-fields -->
















---

## 1. Reaction Forces/Moments (Result Display)

> **Source**: [Reaction Forces/Moments - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/35997222326937)
>
> **`CURRENT_MODE`**: `"ReactionForces/Moments"`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Reaction Forces/Moments" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "FX", "FY", "FZ", "FXYZ" · "MX", "MY", "MZ", "MXYZ" · "Mb" | `"COMP"` | String | "FX" | Optional |
| (2) | └ Node Local Axis (if defined) · Local Coord System: true · Global Coord System: false | `"OPT_LOCAL_CHECK"` | Boolean | false | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (2) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (3) | └ Arrow Scale Factor | `"ARROW_SCALE_FACTOR"` | Number | 1 | Optional |

### Request JSON

**Reaction Forces/Moments**

```json
{
  "Argument": {
    "CURRENT_MODE": "ReactionForces/Moments",
    "LOAD_CASE_COMB": {"TYPE": "ST", "MINMAX": "max", "NAME": "DL", "STEP_INDEX": 1},
    "COMPONENTS": {"COMP": "Fxyz", "OPT_LOCAL_CHECK": true},
    "TYPE_OF_DISPLAY": {"VALUES": {"OPT_CHECK": true}, "LEGEND": {"OPT_CHECK": true}, "ARROW_SCALE_FACTOR": 1.0}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'ReactionForces/Moments',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'MINMAX': 'max', 'NAME': 'DL', 'STEP_INDEX': 1},
        'COMPONENTS': {'COMP': 'Fxyz', 'OPT_LOCAL_CHECK': True},
        'TYPE_OF_DISPLAY': {
            'VALUES': {'OPT_CHECK': True},
            'LEGEND': {'OPT_CHECK': True},
            'ARROW_SCALE_FACTOR': 1.0
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 2. Soil Pressure (Result Display)

> **Source**: [Soil Pressure - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/35997247818393)
>
> **`CURRENT_MODE`**: `"SoilPressure"`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Soil Pressure" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "PX", "PY", "PZ" | `"COMP"` | String | "PX" | Optional |
| (2) | └ Node Local Axis (if defined) · Local Coord System: true · Global Coord System: false | `"OPT_LOCAL_CHECK"` | Boolean | false | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |

### Request JSON

**Soil Pressure**

```json
{
  "Argument": {
    "CURRENT_MODE": "SoilPressure",
    "LOAD_CASE_COMB": {"TYPE": "ST", "MINMAX": "max", "NAME": "DL", "STEP_INDEX": 1},
    "COMPONENTS": {"COMP": "Pz", "OPT_LOCAL_CHECK": true},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": true},
      "MIRRORED": {"OPT_CHECK": true},
      "DEFORM": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true}
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'SoilPressure',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'MINMAX': 'max', 'NAME': 'DL', 'STEP_INDEX': 1},
        'COMPONENTS': {'COMP': 'Pz', 'OPT_LOCAL_CHECK': True},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'VALUES': {'OPT_CHECK': True},
            'LEGEND': {'OPT_CHECK': True},
            'MIRRORED': {'OPT_CHECK': True},
            'DEFORM': {'OPT_CHECK': True},
            'UNDEFORMED': {'OPT_CHECK': True}
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 3. Deformed Shape (Result Display)

> **Source**: [Deformed Shape - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/35997589496089)
>
> **`CURRENT_MODE`**: `"DeformedShape"`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Deformed Shape" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| (5) | └ Time History Function Type · Displacement: "Displacement" · Velocity: "Velocity" · Acceleration: "Acceleration" · Absolute Acceleration: "Absolute Acceleration" | `"TH_OPTION"` | String | "Displacement" | Optional |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "DX", "DY", "DZ" · "DXY", "DYZ", "DXZ" · "DXYZ" | `"COMP"` | String | "DX" | Optional |
| (2) | └ Node Local Axis (if defined) · Local Coord System: true · Global Coord System: false | `"OPT_LOCAL_CHECK"` | Boolean | false | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (2) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (6) | └ Current Step Displacement | `"OPT_CUR_STEP_DISPLACEMENT"` | Boolean | false | Optional |
| (7) | └ Stage/Step Real Displacement | `"OPT_STAGE_STEP_REAL_DISPLACEMENT"` | Boolean | false | Optional |
| (8) | └ Including Camber Displacement | `"OPT_INCLUDING_CAMBER_DISPLACEMENT"` | Boolean | false | Optional |

### Request JSON

**Deformed Shape**

```json
{
  "Argument": {
    "CURRENT_MODE": "DeformedShape",
    "LOAD_CASE_COMB": {"TYPE": "st", "MINMAX": "max", "NAME": "DL", "STEP_INDEX": 1, "TH_OPTION": "Displacement"},
    "COMPONENTS": {"COMP": "Dz", "OPT_LOCAL_CHECK": true},
    "TYPE_OF_DISPLAY": {
      "DEFORM": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": true},
      "MIRRORED": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true},
      "OPT_CUR_STEP_DISPLACEMENT": true,
      "OPT_STAGE_STEP_REAL_DISPLACEMENT": true,
      "OPT_INCLUDING_CAMBER_DISPLACEMENT": true
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'DeformedShape',
        'LOAD_CASE_COMB': {
            'TYPE': 'st',
            'MINMAX': 'max',
            'NAME': 'DL',
            'STEP_INDEX': 1,
            'TH_OPTION': 'Displacement'
        },
        'COMPONENTS': {'COMP': 'Dz', 'OPT_LOCAL_CHECK': True},
        'TYPE_OF_DISPLAY': {
            'DEFORM': {'OPT_CHECK': True},
            'VALUES': {'OPT_CHECK': True},
            'LEGEND': {'OPT_CHECK': True},
            'MIRRORED': {'OPT_CHECK': True},
            'UNDEFORMED': {'OPT_CHECK': True},
            'OPT_CUR_STEP_DISPLACEMENT': True,
            'OPT_STAGE_STEP_REAL_DISPLACEMENT': True,
            'OPT_INCLUDING_CAMBER_DISPLACEMENT': True
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 4. Displacement Contour (Result Display)

> **Source**: [Displacement Contour - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/35997611572505)
>
> **`CURRENT_MODE`**: `"DisplacementContour"`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Displacement Contour" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| (5) | └ Time History Function Type · Displacement: "Displacement" · Velocity: "Velocity" · Acceleration: "Acceleration" · Absolute Acceleration: "Absolute Acceleration" | `"TH_OPTION"` | String | "Displacement" | Optional |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "DX", "DY", "DZ" · "RX", "RY", "RZ", "RW" · "DXY", "DYZ", "DXZ", "DXYZ" | `"COMP"` | String | "DX" | Optional |
| (2) | └ Node Local Axis (if defined) · Local Coord System: true · Global Coord System: false | `"OPT_LOCAL_CHECK"` | Boolean | false | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (7) | └ Cutting Diagram | `"CUTTING_DIAGRAM"` | Object | - | Optional |
| (8) | └ Current Step Displacement (Not opened function) | `"OPT_CUR_STEP_DISPLACEMENT"` | Boolean | false | Optional |
| (9) | └ Stage/Step Real Displacement (Not opened function) | `"OPT_STAGE_STEP_REAL_DISPLACEMENT"` | Boolean | false | Optional |
| (10) | └ Including Camber Displacement (Not opened function) | `"OPT_INCLUDING_CAMBER_DISPLACEMENT"` | Boolean | false | Optional |

### Request JSON

**Displacement Contour**

```json
{
  "Argument": {
    "CURRENT_MODE": "DisplacementContour",
    "LOAD_CASE_COMB": {"TYPE": "String", "MINMAX": "String", "NAME": "String", "STEP_INDEX": 1, "TH_OPTION": "Integer"},
    "COMPONENTS": {"COMP": "String", "OPT_LOCAL_CHECK": true},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "DEFORM": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": true},
      "MIRRORED": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true},
      "CUTTING_DIAGRAM": {"OPT_CHECK": true},
      "OPT_CUR_STEP_DISPLACEMENT": true,
      "OPT_STAGE_STEP_REAL_DISPLACEMENT": true,
      "OPT_INCLUDING_CAMBER_DISPLACEMENT": true
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'DisplacementContour',
        'LOAD_CASE_COMB': {
            'TYPE': 'String',
            'MINMAX': 'String',
            'NAME': 'String',
            'STEP_INDEX': 1,
            'TH_OPTION': 'Integer'
        },
        'COMPONENTS': {'COMP': 'String', 'OPT_LOCAL_CHECK': True},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'DEFORM': {'OPT_CHECK': True},
            'VALUES': {'OPT_CHECK': True},
            'LEGEND': {'OPT_CHECK': True},
            'MIRRORED': {'OPT_CHECK': True},
            'UNDEFORMED': {'OPT_CHECK': True},
            'CUTTING_DIAGRAM': {'OPT_CHECK': True},
            'OPT_CUR_STEP_DISPLACEMENT': True,
            'OPT_STAGE_STEP_REAL_DISPLACEMENT': True,
            'OPT_INCLUDING_CAMBER_DISPLACEMENT': True
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 5. Truss Forces (Result Display)

> **Source**: [Truss Forces - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/35997661413785)
>
> **`CURRENT_MODE`**: `"TrussForces"`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Truss Forces" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · Abs Max: "All" · Tension Forces: "Tens." · Compression Forces: "Comp." | `"COMP"` | String | "All" | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (7) | └ Current Step Force | `"OPT_CUR_STEP_FORCE"` | Boolean | false | Optional |
| 5 | Output Section Location · When "VALUES" is True | `"OUTPUT_SECT_LOCATION"` | Object | - | Optional |
| (1) | └ Available Options · Interior: "I" · Exterior: "J" · ABS Max: "Max" · Both: "All" | `"OPT_I_J_MAX_ALL"` | String | "I" | Optional |

### Request JSON

**Truss Forces**

```json
{
  "Argument": {
    "CURRENT_MODE": "TrussForces",
    "LOAD_CASE_COMB": {"TYPE": "st", "MINMAX": "max", "NAME": "dl", "STEP_INDEX": 1},
    "COMPONENTS": {"COMP": "All"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "DEFORM": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": true},
      "MIRRORED": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true},
      "OPT_CUR_STEP_FORCE": false
    },
    "OUTPUT_SECT_LOCATION": {"OPT_I_J_MAX_ALL": "i"}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'TrussForces',
        'LOAD_CASE_COMB': {'TYPE': 'st', 'MINMAX': 'max', 'NAME': 'dl', 'STEP_INDEX': 1},
        'COMPONENTS': {'COMP': 'All'},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'DEFORM': {'OPT_CHECK': True},
            'VALUES': {'OPT_CHECK': True},
            'LEGEND': {'OPT_CHECK': True},
            'MIRRORED': {'OPT_CHECK': True},
            'UNDEFORMED': {'OPT_CHECK': True},
            'OPT_CUR_STEP_FORCE': False
        },
        'OUTPUT_SECT_LOCATION': {'OPT_I_J_MAX_ALL': 'i'}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 6. Beam Forces/Moments (Result Display)

> **Source**: [Beam Forces/Moments - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/35997711810969)
>
> **`CURRENT_MODE`**: `"BeamForces/Moments"`
>
> ⚠️ 공식 예제의 `"OPE_J"`는 표·JSON Schema의 `"OPT_J"`(Output End Location) 오탈자로 보고 예제에서 `"OPT_J"`로 정정했습니다.

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Beam Forces/Moments" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Parts Name defined in the Composite Section for Construction Stage | `"PART"` | String | "Total" | Optional |
| (2) | └ Components Name · "Fx", "Fy", "Fz" · "Mx, "My", "Mz" · "Mb", "Mt, "Mw" | `"COMP"` | String | "Fx" | Optional |
| (3) | └ Show Truss Forces | `"OPT_SHOW_TRUSS_FORCES"` | Boolean | false | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (7) | └ Current Step Force | `"OPT_CUR_STEP_FORCE"` | Boolean | false | Optional |
| (8) | └ Yield Point | `"YIELD_POINT"` | Object | - | Optional |
| 5 | Output Section Location · When "VALUES" is True | `"OUTPUT_SECT_LOCATION"` | Object | - | Optional |
| (1) | └ By Member | `"OPT_BY_MEMBER"` | Boolean | false | Optional |
| (2) | └ [Output by Element Locations] Output Start Location | `"OPT_I"` | Boolean | false | Optional |
| (3) | └ Output Center/Mid Location | `"OPT_CENTER_MID"` | Boolean | false | Optional |
| (4) | └ Output End Location | `"OPT_J"` | Boolean | false | Optional |
| (2) | └ [Output by Element Values] Output Section Location · "Abs Max" · "Min/Max" · "All" | `"OPT_MAX_MINMAX_ALL"` | String | - | Optional |

### Request JSON

**Beam Forces/Moments**

```json
{
  "Argument": {
    "CURRENT_MODE": "BeamForces/Moments",
    "LOAD_CASE_COMB": {"TYPE": "st", "MINMAX": "max", "NAME": "dl", "STEP_INDEX": 1},
    "COMPONENTS": {"PART": "total", "COMP": "Fx", "OPT_SHOW_TRUSS_FORCES": true},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "DEFORM": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": false},
      "MIRRORED": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true},
      "OPT_CUR_STEP_FORCE": false,
      "YIELD_POINT": {"OPT_CHECK": true}
    },
    "OUTPUT_SECT_LOCATION": {"OPT_I": true, "OPT_CENTER_MID": true, "OPT_J": true, "OPT_BY_MEMBER": true}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'BeamForces/Moments',
        'LOAD_CASE_COMB': {'TYPE': 'st', 'MINMAX': 'max', 'NAME': 'dl', 'STEP_INDEX': 1},
        'COMPONENTS': {'PART': 'total', 'COMP': 'Fx', 'OPT_SHOW_TRUSS_FORCES': True},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'DEFORM': {'OPT_CHECK': True},
            'VALUES': {'OPT_CHECK': True},
            'LEGEND': {'OPT_CHECK': False},
            'MIRRORED': {'OPT_CHECK': True},
            'UNDEFORMED': {'OPT_CHECK': True},
            'OPT_CUR_STEP_FORCE': False,
            'YIELD_POINT': {'OPT_CHECK': True}
        },
        'OUTPUT_SECT_LOCATION': {'OPT_I': True, 'OPT_CENTER_MID': True, 'OPT_J': True, 'OPT_BY_MEMBER': True}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 7. Beam Diagrams (Result Display)

> **Source**: [Beam Diagrams - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/35997754209817)
>
> **`CURRENT_MODE`**: `"BeamDiagrams"`
>
> ⚠️ 공식 예제의 `"OPE_J"`는 표·JSON Schema의 `"OPT_J"`(Output End Location) 오탈자로 보고 예제에서 `"OPT_J"`로 정정했습니다.

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Beam Diagrams" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| (5) | └ Display Absolute Maximum Values of Envelope | `"OPT_MAXMIN_DIAGRAM"` | Boolean | true | Optional |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Parts Name defined in the Composite Section for Construction Stage | `"PART"` | String | "Total" | Optional |
| (2) | └ Components Name · "Fx", "Mx" · "Fy", "Fz", "Fyz" · "My, "Mz", "Myz" · "Mb", "Mt, "Mw" | `"COMP"` | String | "Fx" | Optional |
| (3) | └ Show Truss Forces | `"OPT_SHOW_TRUSS_FORCES"` | Boolean | false | Optional |
| (4) | └ Only Truss Forces | `"OPT_ONLY_TRUSS_FORCES"` | Boolean | false | Optional |
| 4 | Display Options | `"DISPLAY_OPTIONS"` | Object | - | **Required** |
| (1) | └ Fidelity of Diagram · "Exact" · "5 Points" | `"FIDELITY"` | String | "5 Points" | Optional |
| (2) | └ Fill of Diagram · No Fill: "No" · Line Fill: "Line" · Solid Fill: "Solid" | `"FILL"` | String | "Solid Fill" | Optional |
| (3) | └ Scale of Diagram | `"SCALE"` | Number | 1 | Optional |
| 5 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (7) | └ Current Step Force | `"OPT_CUR_STEP_FORCE"` | Boolean | false | Optional |
| (8) | └ Yield Point | `"YIELD_POINT"` | Object | - | Optional |
| 6 | Output Section Location · When "VALUES" is True | `"OUTPUT_SECT_LOCATION"` | Object | - | Optional |
| (1) | └ By Member | `"OPT_BY_MEMBER"` | Boolean | false | Optional |
| (2) | └ [Output by Element Locations] Output Start Location | `"OPT_I"` | Boolean | false | Optional |
| (3) | └ Output Center/Mid Location | `"OPT_CENTER_MID"` | Boolean | false | Optional |
| (4) | └ Output End Location | `"OPT_J"` | Boolean | false | Optional |
| (2) | └ [Output by Element Values] Output Section Location · "Abs Max" · "Min/Max" · "All" | `"OPT_MAX_MINMAX_ALL"` | String | - | Optional |

### Request JSON

**Beam Diagrams**

```json
{
  "Argument": {
    "CURRENT_MODE": "BeamDiagrams",
    "LOAD_CASE_COMB": {"TYPE": "st", "MINMAX": "max", "NAME": "dl", "STEP_INDEX": 1, "OPT_MAXMIN_DIAGRAM": true},
    "COMPONENTS": {"PART": "total", "COMP": "Fx", "OPT_SHOW_TRUSS_FORCES": true, "OPT_ONLY_TRUSS_FORCES": true},
    "DISPLAY_OPTIONS": {"FIDELITY": "Exact", "FILL": "Solid", "SCALE": 1.0},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "DEFORM": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": false},
      "MIRRORED": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true},
      "OPT_CUR_STEP_FORCE": false
    },
    "OUTPUT_SECT_LOCATION": {
      "OPT_I": true,
      "OPT_CENTER_MID": true,
      "OPT_J": true,
      "OPT_MAX_MINMAX_ALL": "absmax",
      "OPT_BY_MEMBER": true
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'BeamDiagrams',
        'LOAD_CASE_COMB': {
            'TYPE': 'st',
            'MINMAX': 'max',
            'NAME': 'dl',
            'STEP_INDEX': 1,
            'OPT_MAXMIN_DIAGRAM': True
        },
        'COMPONENTS': {
            'PART': 'total',
            'COMP': 'Fx',
            'OPT_SHOW_TRUSS_FORCES': True,
            'OPT_ONLY_TRUSS_FORCES': True
        },
        'DISPLAY_OPTIONS': {'FIDELITY': 'Exact', 'FILL': 'Solid', 'SCALE': 1.0},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'DEFORM': {'OPT_CHECK': True},
            'VALUES': {'OPT_CHECK': True},
            'LEGEND': {'OPT_CHECK': False},
            'MIRRORED': {'OPT_CHECK': True},
            'UNDEFORMED': {'OPT_CHECK': True},
            'OPT_CUR_STEP_FORCE': False
        },
        'OUTPUT_SECT_LOCATION': {
            'OPT_I': True,
            'OPT_CENTER_MID': True,
            'OPT_J': True,
            'OPT_MAX_MINMAX_ALL': 'absmax',
            'OPT_BY_MEMBER': True
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 8. Plate Forces/Moments (Result Display)

> **Source**: [Plate Forces/Moments - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/35997813329177)
>
> **`CURRENT_MODE`**: `"PlateForces/Moments"`
>
> ⚠️ Wood Armer Moment 옵션의 위치 Key가 표·Schema는 `"TYPE"`, 예제는 `"POSITION"`입니다. 예제는 원문 그대로 두었습니다.
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `COMPONENTS.WOOD_ARMER_MOMENT_OPTION.POSITION`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Plate Forces/Moments" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Plate Force Options | `"OPTIONS"` | Object | - | Optional |
| (1) | └ Coordinate System Options | `"LOCAL_UCS"` | Object | - | Optional |
| i. | 　　└ Coordinate System · User Coord System: "UCS" · Local Coord System: "Local" | `"TYPE"` | String | "UCS" | Optional |
| ii. | 　　└ User Coordinate System Name · When "TYPE" is UCS / "Current UCS" | `"UCS_NAME"` | String | "Current UCS" | Optional |
| iii. | 　　└ Print UCS Axis · When "TYPE" is UCS / Show the UCS axis: true / Hide the UCS axis: false | `"OPT_PRINT_UCS_AXIS"` | Boolean | true | Optional |
| (2) | └ Result Type Options | `"AVERAGE_NODAL"` | Object | - | Optional |
| i. | 　　└ Average Calculation Method · Element Forces: "Element" · Average Nodal Forces: "Avg.Nodal" | `"TYPE"` | String | "Element" | Optional |
| ii. | 　　└ Average Nodal Active Only · When "TYPE" is Avg.Nodal | `"OPT_ACTIVE_ONLY"` | Boolean | false | Optional |
| 4 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · Local/UCS / "Fxx", "Fyy", "Fxy" / "Fmax", "Fmin", "FMax" / "Mxx, "Myy", "Mxy" / "Mmax", "Mmin, "MMax" / "Vxx", "Vyy", "VMax" / "Wood Armer Moment" / "Fvector", "Mvector" | `"COMP"` | String | "Fxx" | Optional |
| (2) | └ Wood Armer Moment Options | `"WOOD_ARMER_MOMENT_OPTION"` | Object | - | Optional |
| i. | 　　└ Position · "TOP", "Bottom", "Both" | `"TYPE"` | String | "TOP" | Optional |
| ii. | 　　└ Direction · "Dir1", "Dir2" | `"DIRECTION"` | String | "Dir1" | Optional |
| iii. | 　　└ Apply Upon · Active: true · Inactive: false | `"OPT_APPLY_UPON_OK"` | String | true | Optional |
| (3) | └ Vector Options | `"VECTOR_OPTION"` | Object | - | Optional |
| i. | 　　└ Display Positive Value of the Principal Forces in Vectors | `"OPT_POSITIVE"` | Boolean | true | Optional |
| ii. | 　　└ Display Negative Value of the Principal Forces in Vectors | `"OPT_NEGATIVE"` | Boolean | false | Optional |
| iii. | 　　└ Vector Diagram Scale Factor Length | `"SCALE_FACTOR_LENGTH"` | Number | 1 | Optional |
| iv. | 　　└ Vector Diagram Scale Factor Thickness | `"SCALE_FACTOR_THICKNESS"` | Integer | 1 | Optional |
| 5 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (7) | └ Display Option Details | `"DISP_OPT"` | Object | - | Optional |
| (8) | └ Cutting Diagram | `"CUTTING_DIAGRAM"` | Object | - | Optional |

### Request JSON

**Plate Options (Local)**

```json
{
  "Argument": {
    "CURRENT_MODE": "PlateForces/Moments",
    "LOAD_CASE_COMB": {"TYPE": "ST", "MINMAX": "Max", "NAME": "DEADLOAD", "STEP_INDEX": 1},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "Local"}, "AVERAGE_NODAL": {"TYPE": "Element"}},
    "COMPONENTS": {"COMP": "MMax"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "DEFORM": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": true},
      "MIRRORED": {"OPT_CHECK": true},
      "CUTTING_DIAGRAM": {"OPT_CHECK": true}
    }
  }
}
```

**Plate Options (Local - Wood Armer Moment )**

```json
{
  "Argument": {
    "CURRENT_MODE": "PlateForces/Moments",
    "LOAD_CASE_COMB": {"TYPE": "ST", "MINMAX": "Max", "NAME": "DEADLOAD", "STEP_INDEX": 1},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "Local"}, "AVERAGE_NODAL": {"TYPE": "Element"}},
    "COMPONENTS": {"COMP": "WoodArmerMoment", "WOOD_ARMER_MOMENT_OPTION": {"POSITION": "Top", "DIRECTION": "Dir.1"}},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "DEFORM": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": true},
      "MIRRORED": {"OPT_CHECK": true},
      "CUTTING_DIAGRAM": {"OPT_CHECK": true}
    }
  }
}
```

**Plate Options (Local - Vector)**

```json
{
  "Argument": {
    "CURRENT_MODE": "PlateForces/Moments",
    "LOAD_CASE_COMB": {"TYPE": "ST", "MINMAX": "Max", "NAME": "DEADLOAD", "STEP_INDEX": 1},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "Local"}, "AVERAGE_NODAL": {"TYPE": "Element", "OPT_ACTIVE_ONLY": true}},
    "COMPONENTS": {
      "COMP": "Mvector",
      "VECTOR_OPTION": {"OPT_POSITIVE": true, "OPT_NEGATIVE": true, "SCALE_FACTOR_LENGTH": 1.0, "SCALE_FACTOR_THICKNESS": 1}
    },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "DEFORM": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": true},
      "MIRRORED": {"OPT_CHECK": true},
      "CUTTING_DIAGRAM": {"OPT_CHECK": true}
    }
  }
}
```

**Plate Options (UCS)**

```json
{
  "Argument": {
    "CURRENT_MODE": "PlateForces/Moments",
    "LOAD_CASE_COMB": {"TYPE": "ST", "MINMAX": "Max", "NAME": "DEADLOAD", "STEP_INDEX": 1},
    "OPTIONS": {
      "LOCAL_UCS": {"TYPE": "UCS", "UCS_NAME": "CurrentUCS", "OPT_PRINT_UCS_AXIS": true},
      "AVERAGE_NODAL": {"TYPE": "Avg.Nodal", "OPT_ACTIVE_ONLY": true}
    },
    "COMPONENTS": {"COMP": "MMax"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "DEFORM": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": true},
      "MIRRORED": {"OPT_CHECK": true},
      "CUTTING_DIAGRAM": {"OPT_CHECK": true}
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'PlateForces/Moments',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'MINMAX': 'Max', 'NAME': 'DEADLOAD', 'STEP_INDEX': 1},
        'OPTIONS': {'LOCAL_UCS': {'TYPE': 'Local'}, 'AVERAGE_NODAL': {'TYPE': 'Element'}},
        'COMPONENTS': {'COMP': 'MMax'},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'DEFORM': {'OPT_CHECK': True},
            'UNDEFORMED': {'OPT_CHECK': True},
            'VALUES': {'OPT_CHECK': True},
            'LEGEND': {'OPT_CHECK': True},
            'MIRRORED': {'OPT_CHECK': True},
            'CUTTING_DIAGRAM': {'OPT_CHECK': True}
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 9. Plate Cutting Line Diagram (Result Display)

> **Source**: [Plate Cutting Line Diagram - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36000934415257)
>
> **`CURRENT_MODE`**: `"PlateCuttingLineDiagram"`
>
> ⚠️ 표는 `"NORMAL_TO_PLATE"`, 예제는 `"NORMAL_TO_PLANE"`입니다(설명은 "Normal: true / In Plane: false"). 예제는 원문 그대로 두었습니다.
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `OPTIONS.PLATE_DIAGRAM.NORMAL_TO_PLANE`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Plate Cutting Line Diagram" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Cutting Line ¹⁾ | `"CUTTING_NAME"` | Array [String] | - | **Required** |
| 4 | Options | `"OPTIONS"` | Object | - | Optional |
| (1) | └ Plate Force Options | `"AVERAGE_NODAL"` | Object | - | Optional |
| i. | 　　└ Average Calculation Method · Element Forces: "Element" · Average Nodal Forces: "Avg.Nodal" | `"TYPE"` | String | "Element" | Optional |
| ii. | 　　└ Average Nodal Active Only · When "TYPE" is Avg.Nodal | `"OPT_ACTIVE_ONLY"` | Boolean | false | Optional |
| (2) | └ Result Type Options | `"PLATE_DIAGRAM"` | Object | - | Optional |
| i. | 　　└ Options · Normal: true · In Plane: false | `"NORMAL_TO_PLATE"` | Boolean | - | **Required** |
| ii. | 　　└ Scale Factor | `"SCALE_FACTOR"` | Number | 1 | Optional |
| iii. | 　　└ Reverse | `"REVERSE"` | Boolean | false | Optional |
| iv. | 　　└ Value Output | `"VALUE_OUTPUT"` | Boolean | false | Optional |
| v. | 　　└ MinMax Only | `"MINMAX_ONLY"` | Boolean | false | Optional |
| 5 | Select Cutting Line | `"CUTTING_NAME"` | Array [String] | - | **Required** |
| 6 | Components | `"COMPONENTS"` | Object | - | **Required** |
| (1) | └ Components Name · "Fxx", "Fyy", "Fxy" · "Mxx", "Myy", "Mxy" · "Vxx", "Vyy" | `"COMP"` | String | "Fxx" | Optional |

### Request JSON

**Average Nodal, Mxx Options**

```json
{
  "Argument": {
    "CURRENT_MODE": "PlateCuttingLineDiagram",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad"},
    "OPTIONS": {
      "AVERAGE_NODAL": {"TYPE": "Avg.Nodal", "OPT_ACTIVE_ONLY": true},
      "PLATE_DIAGRAM": {
        "NORMAL_TO_PLANE": true,
        "SCALE_FACTOR": 1.1,
        "REVERSE": false,
        "VALUE_OUTPUT": true,
        "MINMAX_ONLY": true
      }
    },
    "CUTTING_NAME": ["CUT1"],
    "COMPONENTS": {"COMP": "Mxx"}
  }
}
```

**Element, Fxx Options**

```json
{
  "Argument": {
    "CURRENT_MODE": "PlateCuttingLineDiagram",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad"},
    "OPTIONS": {
      "AVERAGE_NODAL": {"TYPE": "Element"},
      "PLATE_DIAGRAM": {
        "NORMAL_TO_PLANE": true,
        "SCALE_FACTOR": 1.1,
        "REVERSE": false,
        "VALUE_OUTPUT": true,
        "MINMAX_ONLY": true
      }
    },
    "CUTTING_NAME": ["CUT1"],
    "COMPONENTS": {"COMP": "Fxx"}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'PlateCuttingLineDiagram',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'DeadLoad'},
        'OPTIONS': {
            'AVERAGE_NODAL': {'TYPE': 'Avg.Nodal', 'OPT_ACTIVE_ONLY': True},
            'PLATE_DIAGRAM': {
                'NORMAL_TO_PLANE': True,
                'SCALE_FACTOR': 1.1,
                'REVERSE': False,
                'VALUE_OUTPUT': True,
                'MINMAX_ONLY': True
            }
        },
        'CUTTING_NAME': ['CUT1'],
        'COMPONENTS': {'COMP': 'Mxx'}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 10. Resultant Force Diagram (Result Display)

> **Source**: [Resultant Force Diagram - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/50694881913241)
>
> **`CURRENT_MODE`**: `"Resultant Force Diagram"`
>
> ⚠️ Specifications 표는 `CURRENT_MODE`를 `"Beam Diagrams"`로 적었으나 예제는 `"Resultant Force Diagram"`입니다. 예제를 따릅니다.

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Beam Diagrams" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · ST, CS, RS, TH, MV, SM, CB | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Max, Min, All | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · Fx, Fy, Fz, Mx, My, Mz | `"COMP"` | String | "Fx" | Optional |
| 4 | Options | `"OPTIONS"` | Object | - | **Required** |
| (1) | └ Scale Factor | `"SCALE_FACTOR"` | Number | 1 | Optional |
| (2) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (3) | └ Reverse | `"OPT_REVERSE"` | Boolean | false | Optional |
| (4) | └ Top Alignment | `"OPT_TOP_ALIGNMENT"` | Boolean | false | Optional |
| 5 | Output Section Location When "VALUES" is True | `"OUTPUT_SECT_LOCATION"` | Object | - | Optional |
| (1) | └ Available Options · I, J, All | `"OPT_I_J_ALL"` | String | "I" | Optional |

### Request JSON

**Resultant Force Diagram**

```json
{
  "Argument": {
    "CURRENT_MODE": "Resultant Force Diagram",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DC2"},
    "COMPONENTS": {"COMP": "Fx"},
    "OPTIONS": {"SCALE_FACTOR": 1.1, "VALUES": {"OPT_CHECK": true}, "OPT_REVERSE": true, "OPT_TOP_ALIGNMENT": true},
    "OUTPUT_SECT_LOCATION": {"OPT_I_J_ALL": "I"}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'Resultant Force Diagram',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'DC2'},
        'COMPONENTS': {'COMP': 'Fx'},
        'OPTIONS': {
            'SCALE_FACTOR': 1.1,
            'VALUES': {'OPT_CHECK': True},
            'OPT_REVERSE': True,
            'OPT_TOP_ALIGNMENT': True
        },
        'OUTPUT_SECT_LOCATION': {'OPT_I_J_ALL': 'I'}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 11. Truss Stresses (Result Display)

> **Source**: [Truss Stresses - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36001099992985)
>
> **`CURRENT_MODE`**: `"TrussStresses"`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Truss Stresses" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · Abs Max: "All" · Tension Stresses: "Tens." · Compression Stresses: "Comp." | `"COMP"` | String | "All" | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (7) | └ Yield Point | `"YIELD_POINT"` | Object | - | Optional |
| 5 | Output Section Location · When "VALUES" is True | `"OUTPUT_SECT_LOCATION"` | Object | - | Optional |
| (1) | └ Available Options · Interior: "I" · Exterior: "J" · ABS Max: "Max" · Both: "All" | `"OPT_I_J_MAX_ALL"` | String | "I" | Optional |

### Request JSON

**Truss Stresses**

```json
{
  "Argument": {
    "CURRENT_MODE": "TrussStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "SelfWeight"},
    "COMPONENTS": {"COMP": "All", "STEP_INDEX": 10},
    "TYPE_OF_DISPLAY": {"CONTOUR": {"OPT_CHECK": true}, "VALUES": {"OPT_CHECK": true}},
    "OUTPUT_SECT_LOCATION": {"OPT_I_J_MAX_ALL": "All"}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'TrussStresses',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'SelfWeight'},
        'COMPONENTS': {'COMP': 'All', 'STEP_INDEX': 10},
        'TYPE_OF_DISPLAY': {'CONTOUR': {'OPT_CHECK': True}, 'VALUES': {'OPT_CHECK': True}},
        'OUTPUT_SECT_LOCATION': {'OPT_I_J_MAX_ALL': 'All'}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 12. Beam Stresses (Result Display)

> **Source**: [Beam Stresses - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36001119330969)
>
> **`CURRENT_MODE`**: `"BeamStresses"`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Beam Stresses" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Parts Name defined in the Composite Section for Construction Stage | `"PART"` | String | "Total" | Optional |
| (2) | └ Components Name · "Sax", "Ssy", "Ssz" · "Sby","Sbz", "Combined" · "7th DOF" | `"COMP"` | String | "Sax" | Optional |
| (3) | └ When "COMP" is 7th DOF · "Sax(Warping)" · "Ssy(Mt)" · "Ssy(Mw)" · "Ssz(Mw)" · "Combined(Ssy)" · "Combined(Ssz)" | `"COMP_7TH_DOF"` | String | "Sax(Warping)" | Optional |
| (4) | └ When "COMP" is 7th DOF or Combined · "Maximum" · "1 (-y, +z)" · "2 (+y, +z)" · "3 (+y, -z)" · "4 (-y, -z)" | `"COMP_SUB"` | String | "Maximum" | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| 5 | Output Section Location · When "VALUES" is True | `"OUTPUT_SECT_LOCATION"` | Object | - | Optional |
| (1) | └ [Output by Element Locations] Output Start Location | `"OPT_I"` | Boolean | false | Optional |
| (2) | └ Output Center Location | `"OPT_CENTER_MID"` | Boolean | false | Optional |
| (3) | └ Output End Location | `"OPT_J"` | Boolean | false | Optional |
| (1) | └ [Output by Element Values] Output Section Location · "Max" · "All" | `"OPT_MAX_ALL"` | String | - | Optional |

### Request JSON

**Beam Stresses**

```json
{
  "Argument": {
    "CURRENT_MODE": "BeamStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "SelfWeight", "STEP_INDEX": 10},
    "COMPONENTS": {"PART": "Total", "COMP": "7thDOF", "COMP_7TH_DOF": "Combined(Ssy)", "COMP_SUB": "Maximum"},
    "TYPE_OF_DISPLAY": {"CONTOUR": {"OPT_CHECK": true}, "VALUES": {"OPT_CHECK": true}},
    "OUTPUT_SECT_LOCATION": {"OPT_MAX_ALL": "Max"}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'BeamStresses',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'SelfWeight', 'STEP_INDEX': 10},
        'COMPONENTS': {
            'PART': 'Total',
            'COMP': '7thDOF',
            'COMP_7TH_DOF': 'Combined(Ssy)',
            'COMP_SUB': 'Maximum'
        },
        'TYPE_OF_DISPLAY': {'CONTOUR': {'OPT_CHECK': True}, 'VALUES': {'OPT_CHECK': True}},
        'OUTPUT_SECT_LOCATION': {'OPT_MAX_ALL': 'Max'}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 13. Beam Stresses Diagram (Result Display)

> **Source**: [Beam Stresses Diagram - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36001679829785)
>
> **`CURRENT_MODE`**: `"BeamStressesDiagram"`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Beam Stresses Diagram" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| (5) | └ Display Absolute Maximum Values of Envelope | `"OPT_MAXMIN_DIAGRAM"` | Boolean | true | Optional |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Parts Name defined in the Composite Section for Construction Stage | `"PART"` | String | "Total" | Optional |
| (2) | └ Components Name · "Sax", "Ssy", "Ssz" · "Sby","Sbz", "Combined" · "7th DOF" | `"COMP"` | String | "Sax" | Optional |
| (3) | └ When "COMP" is 7th DOF · "Sax(Warping)" · "Ssy(Mt)" · "Ssy(Mw)" · "Ssz(Mw)" · "Combined(Ssy)" · "Combined(Ssz)" | `"COMP_7TH_DOF"` | String | "Sax(Warping)" | Optional |
| (4) | └ When "COMP" is 7th DOF or Combined · "Maximum" · "1 (-y, +z)" · "2 (+y, +z)" · "3 (+y, -z)" · "4 (-y, -z)" | `"COMP_SUB"` | String | "Maximum" | Optional |
| 4 | Display Options | `"DISPLAY_OPTIONS"` | Object | - | Optional |
| (1) | └ Fill of Diagram · No Fill: "No" · Line Fill: "Line" · Solid Fill: "Solid" | `"FILL"` | String | "Solid Fill" | Optional |
| (2) | └ Scale of Diagram | `"SCALE"` | Number | 1 | Optional |
| 5 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| 6 | Output Section Location · When "VALUES" is True | `"OUTPUT_SECT_LOCATION"` | Object | - | Optional |
| (1) | └ [Output by Element Locations] Output Start Location | `"OPT_I"` | Boolean | false | Optional |
| (2) | └ Output Center Location | `"OPT_CENTER_MID"` | Boolean | false | Optional |
| (3) | └ Output End Location | `"OPT_J"` | Boolean | false | Optional |
| (1) | └ [Output by Element Values] Output Section Location · "Max" · "All" | `"OPT_MAX_MINMAX_ALL"` | String | - | Optional |

### Request JSON

**Beam Stresses Diagram**

```json
{
  "Argument": {
    "CURRENT_MODE": "BeamStressesDiagram",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "SelfWeight", "STEP_INDEX": 10},
    "COMPONENTS": {"PART": "Total", "COMP": "7thDOF", "COMP_7TH_DOF": "Combined(Ssy)", "COMP_SUB": "Maximum"},
    "DISPLAY_OPTIONS": {"SCALE": 1.0, "FILL": "Solid"},
    "TYPE_OF_DISPLAY": {"CONTOUR": {"OPT_CHECK": true}, "VALUES": {"OPT_CHECK": true}},
    "OUTPUT_SECT_LOCATION": {"OPT_MAX_MINMAX_ALL": "all"}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'BeamStressesDiagram',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'SelfWeight', 'STEP_INDEX': 10},
        'COMPONENTS': {
            'PART': 'Total',
            'COMP': '7thDOF',
            'COMP_7TH_DOF': 'Combined(Ssy)',
            'COMP_SUB': 'Maximum'
        },
        'DISPLAY_OPTIONS': {'SCALE': 1.0, 'FILL': 'Solid'},
        'TYPE_OF_DISPLAY': {'CONTOUR': {'OPT_CHECK': True}, 'VALUES': {'OPT_CHECK': True}},
        'OUTPUT_SECT_LOCATION': {'OPT_MAX_MINMAX_ALL': 'all'}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 14. Beam Stresses (Equivalent) (Result Display)

> **Source**: [Beam Stresses (Equivalent) - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36002326176665)
>
> **`CURRENT_MODE`**: `"BeamStresses(Equivalent)"`
>
> ⚠️ 단면 출력 위치 Key가 표는 `"OPT_MAX_MINMAX_ALL"`, 예제는 `"OPT_MAX_ALL"`입니다. 예제는 원문 그대로 두었습니다.
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `OUTPUT_SECT_LOCATION.OPT_MAX_ALL`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Beam Stresses(Equivalent)" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "Normal", · "Tau_xy" · "Tau_xz" · "Von-Mises" · "Max-Shear" · "Princ.(max)" · "Princ.(min)" | `"COMP"` | String | "Normal" | Optional |
| (2) | └ Location for the Display of Stress · "Maximum" · "1(-y, +z)" · "2(+y, +z)" · "3(+y, -z)" · "4(-y, -z)" · "5(N.A. -y)" · "6(N.A. +y)" · "7(N.A. -z)" · "8(N.A. +z)" | `"COMP_SUB"` | String | "Maximum" | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| 5 | Output Section Location · When "VALUES" is True | `"OUTPUT_SECT_LOCATION"` | Object | - | Optional |
| (1) | └ [Output by Element Locations] Output Start Location | `"OPT_I"` | Boolean | false | Optional |
| (2) | └ Output Center Location | `"OPT_CENTER_MID"` | Boolean | false | Optional |
| (3) | └ Output End Location | `"OPT_J"` | Boolean | false | Optional |
| (1) | └ [Output by Element Values] Output Section Location · "Max" · "All" | `"OPT_MAX_MINMAX_ALL"` | String | - | Optional |

### Request JSON

**Beam Stresses(Equivalent)**

```json
{
  "Argument": {
    "CURRENT_MODE": "BeamStresses(Equivalent)",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "SelfWeight", "STEP_INDEX": 10},
    "COMPONENTS": {"COMP": "Max-Shear", "COMP_SUB": "Maximum"},
    "TYPE_OF_DISPLAY": {"CONTOUR": {"OPT_CHECK": true}, "VALUES": {"OPT_CHECK": true}},
    "OUTPUT_SECT_LOCATION": {"OPT_MAX_ALL": "all"}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'BeamStresses(Equivalent)',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'SelfWeight', 'STEP_INDEX': 10},
        'COMPONENTS': {'COMP': 'Max-Shear', 'COMP_SUB': 'Maximum'},
        'TYPE_OF_DISPLAY': {'CONTOUR': {'OPT_CHECK': True}, 'VALUES': {'OPT_CHECK': True}},
        'OUTPUT_SECT_LOCATION': {'OPT_MAX_ALL': 'all'}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 15. Beam Stresses Diagram (Equivalent) (Result Display)

> **Source**: [Beam Stresses Diagram (Equivalent) - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36002496760217)
>
> **`CURRENT_MODE`**: `"BeamStressesDiagram(Equivalent)"`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Beam Stresses Diagram (Equivalent)" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| (5) | └ Display Absolute Maximum Values of Envelope | `"OPT_MAXMIN_DIAGRAM"` | Boolean | true | Optional |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "Normal" · "Tau_xy" · "Tau_xz" · "Von-Mises" · "Max-Shear" · "Princ.(max)" · "Princ.(min)" | `"COMP"` | String | "Normal" | Optional |
| (2) | └ Location for the Display of Stress. · "Maximum" · "1(-y, +z)" · "2(+y, +z)" · "3(+y, -z)" · "4(-y, -z)" · "5(N.A. -y)" · "6(N.A. +y)" · "7(N.A. -z)" · "8(N.A. +z)" | `"COMP_SUB"` | String | "Maximum" | Optional |
| 4 | Display Options | `"DISPLAY_OPTIONS"` | Object | - | Optional |
| (1) | └ Fill of Diagram · No Fill: "No" · Line Fill: "Line" · Solid Fill: "Solid" | `"FILL"` | String | "Solid Fill" | Optional |
| (2) | └ Scale of Diagram | `"SCALE"` | Number | 1 | Optional |
| 5 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| 6 | Output Section Location · When "VALUES" is True | `"OUTPUT_SECT_LOCATION"` | Object | - | Optional |
| (1) | └ [Output by Element Locations] Output Start Location | `"OPT_I"` | Boolean | false | Optional |
| (2) | └ Output Center Location | `"OPT_CENTER_MID"` | Boolean | false | Optional |
| (3) | └ Output End Location | `"OPT_J"` | Boolean | false | Optional |
| (1) | └ [Output by Element Values] Output Section Location · "Abs Max" · "Min/Max" · "All" | `"OPT_MAX_MINMAX_ALL"` | String | - | Optional |

### Request JSON

**Beam Stresses Diagram (Equivalent)**

```json
{
  "Argument": {
    "CURRENT_MODE": "BeamStressesDiagram(Equivalent)",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "SelfWeight", "STEP_INDEX": 10},
    "COMPONENTS": {"COMP": "Max-Shear", "COMP_SUB": "Maximum"},
    "DISPLAY_OPTIONS": {"SCALE": 1.0, "FILL": "Solid"},
    "TYPE_OF_DISPLAY": {"CONTOUR": {"OPT_CHECK": true}, "VALUES": {"OPT_CHECK": true}},
    "OUTPUT_SECT_LOCATION": {"OPT_MAX_MINMAX_ALL": "all"}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'BeamStressesDiagram(Equivalent)',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'SelfWeight', 'STEP_INDEX': 10},
        'COMPONENTS': {'COMP': 'Max-Shear', 'COMP_SUB': 'Maximum'},
        'DISPLAY_OPTIONS': {'SCALE': 1.0, 'FILL': 'Solid'},
        'TYPE_OF_DISPLAY': {'CONTOUR': {'OPT_CHECK': True}, 'VALUES': {'OPT_CHECK': True}},
        'OUTPUT_SECT_LOCATION': {'OPT_MAX_MINMAX_ALL': 'all'}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 16. Beam Stresses (PSC) (Result Display)

> **Source**: [Beam Stresses (PSC) - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36002716977817)
>
> **`CURRENT_MODE`**: `"BeamStresses(PSC)"`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Beam Stresses (PSC)" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| (5) | └ Display Absolute Maximum Values of Envelope | `"OPT_MAXMIN_DIAGRAM"` | Boolean | true | Optional |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "Sig-xx(Axial)" · "Sig-xx(Moment-y)" · "Sig-xx(Moment-z)" · "Sig-xx(Bar)" · "Sig-xx(Summation)" · "Sig-zz" · "Sig-xz(Shear)" · "Sig-xz(torsion)" · "Sig-xz(bar)" · "Sig-Is(shear)" · "Sig-Is(shear+torsion)" | `"COMP"` | String | "Sig-xx(Axial)" | Optional |
| (2) | └ Location for the Display of Stress · "Position 1" to "Position 16" · "Max", "Min" · "Max/Min", "Abs Max" | `"COMP_SUB"` | String | "Position 1" | Optional |
| 4 | Display Options | `"DISPLAY_OPTIONS"` | Object | - | Optional |
| (1) | └ Fill of Diagram · No Fill: "No" · Line Fill: "Line" · Solid Fill: "Solid" | `"FILL"` | String | "Solid Fill" | Optional |
| (2) | └ Scale of Diagram | `"SCALE"` | Number | 1 | Optional |
| 5 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| 6 | Output Section Location · When "VALUES" is True | `"OUTPUT_SECT_LOCATION"` | Object | - | Optional |
| (1) | └ [Output by Element Locations] Output Start Location | `"OPT_I"` | Boolean | false | Optional |
| (2) | └ Output Center Location | `"OPT_CENTER_MID"` | Boolean | false | Optional |
| (3) | └ Output End Location | `"OPT_J"` | Boolean | false | Optional |
| (1) | └ [Output by Element Values] Output Section Location · "Abs Max" · "Min/Max" · "All" | `"OPT_MAX_MINMAX_ALL"` | String | - | Optional |

### Request JSON

**Beam Stresses (PSC)**

```json
{
  "Argument": {
    "CURRENT_MODE": "BeamStresses(PSC)",
    "LOAD_CASE_COMB": {"TYPE": "SM", "MINMAX": "Max", "NAME": "Settlement"},
    "COMPONENTS": {"COMP_SUB": "Position1", "COMP": "Sig-xx(Axial)"},
    "DISPLAY_OPTIONS": {"SCALE": 1.0, "FILL": "Solid"},
    "TYPE_OF_DISPLAY": {"CONTOUR": {"OPT_CHECK": true}, "VALUES": {"OPT_CHECK": true}},
    "OUTPUT_SECT_LOCATION": {"OPT_MAX_MINMAX_ALL": "all"}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'BeamStresses(PSC)',
        'LOAD_CASE_COMB': {'TYPE': 'SM', 'MINMAX': 'Max', 'NAME': 'Settlement'},
        'COMPONENTS': {'COMP_SUB': 'Position1', 'COMP': 'Sig-xx(Axial)'},
        'DISPLAY_OPTIONS': {'SCALE': 1.0, 'FILL': 'Solid'},
        'TYPE_OF_DISPLAY': {'CONTOUR': {'OPT_CHECK': True}, 'VALUES': {'OPT_CHECK': True}},
        'OUTPUT_SECT_LOCATION': {'OPT_MAX_MINMAX_ALL': 'all'}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 17. Plane-Stress/Plate Stresses (Result Display)

> **Source**: [Plane-Stress/Plate Stresses - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36002978639641)
>
> **`CURRENT_MODE`**: `"Plane-Stress/PlateStresses"`
>
> ⚠️ 이 글의 첫 예제 "Stress Options (Local)"은 `CURRENT_MODE`가 `"BeamStresses(PSC)"`로, Beam Stresses (PSC) 예제가 섞인 것으로 보입니다. Plane-Stress/Plate 요청에는 나머지 예제를 쓰세요.
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `OPTIONS.SURFACE`, `TYPE_OF_DISPLAY.VALUES.DECIMAL_PT`, `TYPE_OF_DISPLAY.VALUES.VALUE_EXP`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Plane-Stress/Plate Stresses" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Plate Force Options | `"OPTIONS"` | Object | - | Optional |
| (1) | └ Coordinate System Options | `"LOCAL_UCS"` | Object | - | Optional |
| i. | 　　└ Coordinate System · User Coord System: "UCS" · Local Coord System: "Local" | `"TYPE"` | String | "UCS" | Optional |
| ii. | 　　└ User Coordinate System Name · When "TYPE" is UCS / "Current UCS" | `"UCS_NAME"` | String | "Current UCS" | Optional |
| iii. | 　　└ Print UCS Axis · When "TYPE" is UCS / Show the UCS axis: true / Hide the UCS axis: false | `"OPT_PRINT_UCS_AXIS"` | Boolean | true | Optional |
| (2) | └ Result Type Options | `"AVERAGE_NODAL"` | Object | - | Optional |
| i. | 　　└ Average Calculation Method · Element Forces: "Element" · Average Nodal Forces: "Avg.Nodal" | `"TYPE"` | String | "Element" | Optional |
| ii. | 　　└ Average Nodal Active Only · When "TYPE" is Avg.Nodal | `"OPT_ACTIVE_ONLY"` | Boolean | false | Optional |
| 4 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · UCS / "Sig-xx", "Sig-yy", "Sig-zz" / "Sig-xy", "Sig-yz", "Sig-xz" / "Sig-max" / "Sig-min" / "Sig-eff" / "Max-Shear" | `"COMP"` | String | "Fxx" | Optional |
| (2) | └ Vector Options | `"VECTOR_OPTION"` | Object | - | Optional |
| i. | 　　└ Display Positive Value of the Principal Forces in Vectors | `"OPT_POSITIVE"` | Boolean | true | Optional |
| ii. | 　　└ Display Negative Value of the Principal Forces in Vectors | `"OPT_NEGATIVE"` | Boolean | false | Optional |
| iii. | 　　└ Vector Diagram Scale Factor Length | `"SCALE_FACTOR_LENGTH"` | Number | 1 | Optional |
| iv. | 　　└ Vector Diagram Scale Factor Thickness | `"SCALE_FACTOR_THICKNESS"` | Integer | 1 | Optional |
| 5 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (7) | └ Display Option Details | `"DISP_OPT"` | Object | - | Optional |
| (8) | └ Yield Point | `"YIELD_POINT"` | Object | - | Optional |
| (9) | └ Cutting Diagram | `"CUTTING_DIAGRAM"` | Object | - | Optional |

### Request JSON

**Stress Options (Local) (원문 오류: 다른 결과 모드의 예제)**

```json
{
  "Argument": {
    "CURRENT_MODE": "BeamStresses(PSC)",
    "LOAD_CASE_COMB": {"TYPE": "SM", "MINMAX": "Max", "NAME": "Settlement"},
    "COMPONENTS": {"COMP_SUB": "Position1", "COMP": "Sig-xx(Axial)"},
    "DISPLAY_OPTIONS": {"SCALE": 1.0, "FILL": "Solid"},
    "TYPE_OF_DISPLAY": {"CONTOUR": {"OPT_CHECK": true}, "VALUES": {"OPT_CHECK": true}},
    "OUTPUT_SECT_LOCATION": {"OPT_MAX_MINMAX_ALL": "all"}
  }
}
```

**Stress Options (Local - Vector)**

```json
{
  "Argument": {
    "CURRENT_MODE": "Plane-Stress/PlateStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 10},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "Local"}, "AVERAGE_NODAL": {"TYPE": "Element"}, "SURFACE": "Top"},
    "COMPONENTS": {
      "COMP": "Vector",
      "VECTOR_OPTION": {"OPT_POSITIVE": true, "OPT_NEGATIVE": true, "SCALE_FACTOR_LENGTH": 1.0, "SCALE_FACTOR_THICKNESS": 2}
    },
    "TYPE_OF_DISPLAY": {"CONTOUR": {"OPT_CHECK": true}}
  }
}
```

**Stress Options (UCS)**

```json
{
  "Argument": {
    "CURRENT_MODE": "Plane-Stress/PlateStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 10},
    "OPTIONS": {
      "LOCAL_UCS": {"TYPE": "UCS", "UCS_NAME": "CurrentUCS"},
      "AVERAGE_NODAL": {"TYPE": "Element"},
      "SURFACE": "Top"
    },
    "COMPONENTS": {"COMP": "Sig-eff"},
    "TYPE_OF_DISPLAY": {"VALUES": {"OPT_CHECK": true, "DECIMAL_PT": 5, "VALUE_EXP": true}}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'Plane-Stress/PlateStresses',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'DeadLoad', 'STEP_INDEX': 10},
        'OPTIONS': {'LOCAL_UCS': {'TYPE': 'Local'}, 'AVERAGE_NODAL': {'TYPE': 'Element'}, 'SURFACE': 'Top'},
        'COMPONENTS': {
            'COMP': 'Vector',
            'VECTOR_OPTION': {
                'OPT_POSITIVE': True,
                'OPT_NEGATIVE': True,
                'SCALE_FACTOR_LENGTH': 1.0,
                'SCALE_FACTOR_THICKNESS': 2
            }
        },
        'TYPE_OF_DISPLAY': {'CONTOUR': {'OPT_CHECK': True}}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 18. Plane Strain Stresses (Result Display)

> **Source**: [Plane Strain Stresses - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36003113196441)
>
> **`CURRENT_MODE`**: `"PlaneStrainStresses"`
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `OPTIONS.SURFACE`, `TYPE_OF_DISPLAY.CONTOUR.NUM_OF_COLOR`, `TYPE_OF_DISPLAY.CONTOUR.COLOR_TYPE`, `TYPE_OF_DISPLAY.CONTOUR.GRADIENT_FILL`, `TYPE_OF_DISPLAY.CONTOUR.CONTOUR_FILL`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Plane Strain Stresses" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Plate Force Options | `"OPTIONS"` | Object | - | Optional |
| (1) | └ Coordinate System Options | `"LOCAL_UCS"` | Object | - | Optional |
| i. | 　　└ Coordinate System · User Coord System: "UCS" · Local Coord System: "Local" | `"TYPE"` | String | "UCS" | Optional |
| ii. | 　　└ User Coordinate System Name <strong>· </strong>When "TYPE" is UCS / "Current UCS" | `"UCS_NAME"` | String | "Current UCS" | Optional |
| iii. | 　　└ Print UCS Axis <strong>· </strong>When "TYPE" is UCS / Show the UCS axis: true / Hide the UCS axis: false | `"OPT_PRINT_UCS_AXIS"` | Boolean | true | Optional |
| (2) | └ Result Type Options | `"AVERAGE_NODAL"` | Object | - | Optional |
| i. | 　　└ Average Calculation Method · Element Forces: "Element" · Average Nodal Forces: "Avg.Nodal" | `"TYPE"` | String | "Element" | Optional |
| ii. | 　　└ Average Nodal Active Only · When "TYPE" is Avg.Nodal | `"OPT_ACTIVE_ONLY"` | Boolean | false | Optional |
| 4 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name <strong>· </strong>UCS / "Sig-xx", "Sig-yy", "Sig-zz" / "Sig-xy", "Sig-yz", "Sig-xz" / "Sig-p1" / "Sig-p2" / "Sig-p3" / "Max-Shear" / "Sig-eff" / "Sig-pmax" | `"COMP"` | String | "Fxx" | Optional |
| (2) | └ Vector Options | `"VECTOR_OPTION"` | Object | - | Optional |
| i. | 　　└ Display Positive Value of the Principal Forces in Vectors | `"OPT_POSITIVE"` | Boolean | true | Optional |
| ii. | 　　└ Display Negative Value of the Principal Forces in Vectors | `"OPT_NEGATIVE"` | Boolean | false | Optional |
| iii. | 　　└ Vector Diagram Scale Factor Length | `"SCALE_FACTOR_LENGTH"` | Number | 1 | Optional |
| iv. | 　　└ Vector Diagram Scale Factor Thickness | `"SCALE_FACTOR_THICKNESS"` | Integer | 1 | Optional |
| 5 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (7) | └ Display Option Details | `"DISP_OPT"` | Object | - | Optional |
| (8) | └ Yield Point | `"YIELD_POINT"` | Object | - | Optional |
| (9) | └ Cutting Diagram | `"CUTTING_DIAGRAM"` | Object | - | Optional |

### Request JSON

**Stress Options (Local)**

```json
{
  "Argument": {
    "CURRENT_MODE": "PlaneStrainStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 1},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "Local"}, "AVERAGE_NODAL": {"TYPE": "Avg.Nodal"}, "SURFACE": "Top"},
    "COMPONENTS": {"COMP": "Sig-xx"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 6,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
      }
    }
  }
}
```

**Stress Options (Local - Vector)**

```json
{
  "Argument": {
    "CURRENT_MODE": "PlaneStrainStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 10},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "Local"}, "AVERAGE_NODAL": {"TYPE": "Element"}},
    "COMPONENTS": {
      "COMP": "Vector",
      "VECTOR_OPTION": {"OPT_POSITIVE": true, "OPT_NEGATIVE": true, "SCALE_FACTOR_LENGTH": 1.0, "SCALE_FACTOR_THICKNESS": 2}
    },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
      }
    }
  }
}
```

**Stress Options (UCS)**

```json
{
  "Argument": {
    "CURRENT_MODE": "PlaneStrainStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 10},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "UCS", "UCS_NAME": "CurrentUCS"}, "AVERAGE_NODAL": {"TYPE": "Avg.Nodal"}},
    "COMPONENTS": {"COMP": "Sig-eff"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
      }
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'PlaneStrainStresses',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'DeadLoad', 'STEP_INDEX': 1},
        'OPTIONS': {
            'LOCAL_UCS': {'TYPE': 'Local'},
            'AVERAGE_NODAL': {'TYPE': 'Avg.Nodal'},
            'SURFACE': 'Top'
        },
        'COMPONENTS': {'COMP': 'Sig-xx'},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {
                'OPT_CHECK': True,
                'NUM_OF_COLOR': 6,
                'COLOR_TYPE': 'rgb',
                'GRADIENT_FILL': False,
                'CONTOUR_FILL': False
            }
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 19. Axisymmetric Stresses (Result Display)

> **Source**: [Axisymmetric Stresses - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36003190685209)
>
> **`CURRENT_MODE`**: `"AxisymmetricStresses"`
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `OPTIONS.SURFACE`, `TYPE_OF_DISPLAY.CONTOUR.NUM_OF_COLOR`, `TYPE_OF_DISPLAY.CONTOUR.COLOR_TYPE`, `TYPE_OF_DISPLAY.CONTOUR.GRADIENT_FILL`, `TYPE_OF_DISPLAY.CONTOUR.CONTOUR_FILL`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Axisymmetric Stresses" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Plate Force Options | `"OPTIONS"` | Object | - | Optional |
| (1) | └ Coordinate System Options | `"LOCAL_UCS"` | Object | - | Optional |
| i. | 　　└ Coordinate System · User Coord System: "UCS" · Local Coord System: "Local" | `"TYPE"` | String | "UCS" | Optional |
| ii. | 　　└ User Coordinate System Name <strong>· </strong>When "TYPE" is UCS / "Current UCS" | `"UCS_NAME"` | String | "Current UCS" | Optional |
| iii. | 　　└ Print UCS Axis <strong>· </strong>When "TYPE" is UCS / Show the UCS axis: true / Hide the UCS axis: false | `"OPT_PRINT_UCS_AXIS"` | Boolean | true | Optional |
| (2) | └ Result Type Options | `"AVERAGE_NODAL"` | Object | - | Optional |
| i. | 　　└ Average Calculation Method · Element Forces: "Element" · Average Nodal Forces: "Avg.Nodal" | `"TYPE"` | String | "Element" | Optional |
| ii. | 　　└ Average Nodal Active Only · When "TYPE" is Avg.Nodal | `"OPT_ACTIVE_ONLY"` | Boolean | false | Optional |
| 4 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name <strong>· </strong>UCS / "Sig-xx", "Sig-yy", "Sig-zz" / "Sig-xy", "Sig-yz", "Sig-xz" / "Sig-p1" / "Sig-p2" / "Sig-p3" / "Max-Shear" / "Sig-eff" / "Sig-pmax" | `"COMP"` | String | "Fxx" | Optional |
| (2) | └ Vector Options | `"VECTOR_OPTION"` | Object | - | Optional |
| i. | 　　└ Display Positive Value of the Principal Forces in Vectors | `"OPT_POSITIVE"` | Boolean | true | Optional |
| ii. | 　　└ Display Negative Value of the Principal Forces in Vectors | `"OPT_NEGATIVE"` | Boolean | false | Optional |
| iii. | 　　└ Vector Diagram Scale Factor Length | `"SCALE_FACTOR_LENGTH"` | Number | 1 | Optional |
| iv. | 　　└ Vector Diagram Scale Factor Thickness | `"SCALE_FACTOR_THICKNESS"` | Integer | 1 | Optional |
| 5 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (7) | └ Display Option Details | `"DISP_OPT"` | Object | - | Optional |
| (8) | └ Yield Point | `"YIELD_POINT"` | Object | - | Optional |

### Request JSON

**Stress Options (Local)**

```json
{
  "Argument": {
    "CURRENT_MODE": "AxisymmetricStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 1},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "Local"}, "AVERAGE_NODAL": {"TYPE": "Avg.Nodal"}, "SURFACE": "Top"},
    "COMPONENTS": {"COMP": "Sig-xx"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 6,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
      }
    }
  }
}
```

**Stress Options (Local - Vector)**

```json
{
  "Argument": {
    "CURRENT_MODE": "AxisymmetricStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 10},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "Local"}, "AVERAGE_NODAL": {"TYPE": "Element"}},
    "COMPONENTS": {
      "COMP": "Vector",
      "VECTOR_OPTION": {"OPT_POSITIVE": true, "OPT_NEGATIVE": true, "SCALE_FACTOR_LENGTH": 1.0, "SCALE_FACTOR_THICKNESS": 2}
    },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
      }
    }
  }
}
```

**Stress Options (UCS)**

```json
{
  "Argument": {
    "CURRENT_MODE": "AxisymmetricStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 10},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "UCS", "UCS_NAME": "CurrentUCS"}, "AVERAGE_NODAL": {"TYPE": "Avg.Nodal"}},
    "COMPONENTS": {"COMP": "Sig-eff"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
      }
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'AxisymmetricStresses',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'DeadLoad', 'STEP_INDEX': 1},
        'OPTIONS': {
            'LOCAL_UCS': {'TYPE': 'Local'},
            'AVERAGE_NODAL': {'TYPE': 'Avg.Nodal'},
            'SURFACE': 'Top'
        },
        'COMPONENTS': {'COMP': 'Sig-xx'},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {
                'OPT_CHECK': True,
                'NUM_OF_COLOR': 6,
                'COLOR_TYPE': 'rgb',
                'GRADIENT_FILL': False,
                'CONTOUR_FILL': False
            }
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 20. Solid Stresses (Result Display)

> **Source**: [Solid Stresses - Result Display ↗](https://support.midasuser.com/hc/en-us/articles/36004183629209)
>
> **`CURRENT_MODE`**: `"SolidStresses"`
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `OPTIONS.SURFACE`, `TYPE_OF_DISPLAY.CONTOUR.NUM_OF_COLOR`, `TYPE_OF_DISPLAY.CONTOUR.COLOR_TYPE`, `TYPE_OF_DISPLAY.CONTOUR.GRADIENT_FILL`, `TYPE_OF_DISPLAY.CONTOUR.CONTOUR_FILL`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Solid Stresses" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Static Load: "ST" · Construction Stage: "CS" · Response Spectrum: "RS" · Time History: "TH" · Moving Load: "MV" · Settlement: "SM" · Load Combinations: "CB" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Step of Load Case | `"STEP_INDEX"` | Integer | - | **Required** |
| 3 | Plate Force Options | `"OPTIONS"` | Object | - | Optional |
| (1) | └ Coordinate System Options | `"LOCAL_UCS"` | Object | - | Optional |
| i. | 　　└ Coordinate System · User Coord. System: "UCS" · Local Coord. System: "Local" | `"TYPE"` | String | "UCS" | Optional |
| ii. | 　　└ User Coordinate System Name <strong>· </strong>When "TYPE" is UCS / "Current UCS" | `"UCS_NAME"` | String | "Current UCS" | Optional |
| iii. | 　　└ Print UCS Axis <strong>· </strong>When "TYPE" is UCS / Show the UCS axis: true / Hide the UCS axis: false | `"OPT_PRINT_UCS_AXIS"` | Boolean | true | Optional |
| (2) | └ Result Type Options | `"AVERAGE_NODAL"` | Object | - | Optional |
| i. | 　　└ Average Calculation Method · Element Forces: "Element" · Average Nodal Forces: "Avg.Nodal" | `"TYPE"` | String | "Element" | Optional |
| ii. | 　　└ Average Nodal Active Only · When "TYPE" is Avg.Nodal | `"OPT_ACTIVE_ONLY"` | Boolean | false | Optional |
| 4 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name <strong>· </strong>UCS / "Sig-xx", "Sig-yy", "Sig-zz" / "Sig-xy", "Sig-yz", "Sig-xz" / "Sig-p1" / "Sig-p2" / "Sig-p3" / "Max-Shear" / "Sig-eff" / "Sig-pmax" | `"COMP"` | String | "Fxx" | Optional |
| (2) | └ Vector Options | `"VECTOR_OPTION"` | Object | - | Optional |
| i. | 　　└ Display Positive Value of the Principal Forces in Vectors | `"OPT_POSITIVE"` | Boolean | true | Optional |
| ii. | 　　└ Display Negative Value of the Principal Forces in Vectors | `"OPT_NEGATIVE"` | Boolean | false | Optional |
| iii. | 　　└ Vector Diagram Scale Factor Length | `"SCALE_FACTOR_LENGTH"` | Number | 1 | Optional |
| iv. | 　　└ Vector Diagram Scale Factor Thickness | `"SCALE_FACTOR_THICKNESS"` | Integer | 1 | Optional |
| 5 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Deformation Details | `"DEFORM"` | Object | - | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (6) | └ Symmetric Model Mirror Detail | `"MIRRORED"` | Object | - | Optional |
| (7) | └ Display Option Details | `"DISP_OPT"` | Object | - | Optional |
| (8) | └ Yield Point | `"YIELD_POINT"` | Object | - | Optional |
| (9) | └ Cutting Plane Detail Dialog | `"CUTTING_PLANE"` | Object | - | Optional |

### Request JSON

**Stress Options (Local)**

```json
{
  "Argument": {
    "CURRENT_MODE": "SolidStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 1},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "Local"}, "AVERAGE_NODAL": {"TYPE": "Avg.Nodal"}, "SURFACE": "Top"},
    "COMPONENTS": {"COMP": "Sig-xx"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 6,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
      }
    }
  }
}
```

**Stress Options (Local - Vector)**

```json
{
  "Argument": {
    "CURRENT_MODE": "SolidStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 10},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "Local"}, "AVERAGE_NODAL": {"TYPE": "Element"}},
    "COMPONENTS": {
      "COMP": "Vector",
      "VECTOR_OPTION": {"OPT_POSITIVE": true, "OPT_NEGATIVE": true, "SCALE_FACTOR_LENGTH": 1.0, "SCALE_FACTOR_THICKNESS": 2}
    },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
      }
    }
  }
}
```

**Stress Options (UCS)**

```json
{
  "Argument": {
    "CURRENT_MODE": "SolidStresses",
    "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DeadLoad", "STEP_INDEX": 10},
    "OPTIONS": {"LOCAL_UCS": {"TYPE": "UCS", "UCS_NAME": "CurrentUCS"}, "AVERAGE_NODAL": {"TYPE": "Avg.Nodal"}},
    "COMPONENTS": {"COMP": "Sig-eff"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
      }
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'SolidStresses',
        'LOAD_CASE_COMB': {'TYPE': 'ST', 'NAME': 'DeadLoad', 'STEP_INDEX': 1},
        'OPTIONS': {
            'LOCAL_UCS': {'TYPE': 'Local'},
            'AVERAGE_NODAL': {'TYPE': 'Avg.Nodal'},
            'SURFACE': 'Top'
        },
        'COMPONENTS': {'COMP': 'Sig-xx'},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {
                'OPT_CHECK': True,
                'NUM_OF_COLOR': 6,
                'COLOR_TYPE': 'rgb',
                'GRADIENT_FILL': False,
                'CONTOUR_FILL': False
            }
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 21. Reactions (Moving Tracer Display)

> **Source**: [Reactions - Moving Tracer Display ↗](https://support.midasuser.com/hc/en-us/articles/36004234384665)
>
> **`CURRENT_MODE`**: `"MVLTRC_Reactions"`
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `TYPE_OF_DISPLAY.APPLIED_LOADS.SCALE_FACTOR`, `TYPE_OF_DISPLAY.APPLIED_LOADS.OPT_LOAD_VALUES`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_TYPE`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_DECIMAL_PT`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "MVLTRC_Reactions" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Moving Load: "MV" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Select Support Node Number | `"KEY_NODE_ELEM"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "FX", "FY", "FZ" · "MX", "MY", "MZ" · "Mb" | `"COMP"` | String | "FX" | Optional |
| (2) | └ Node Local Axis · Local Coord System: true · Global Coord System: false | `"OPT_LOCAL_CHECK"` | Boolean | false | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (3) | └ Applied Loads (Moving Load Tracer Detail) | `"APPLIED_LOADS"` | Object | - | Optional |
| (4) | └ Include Impact Factor | `"OPT_INCLUDE_IMPACT_FACTOR"` | Boolean | false | Optional |

### Request JSON

**Moving Tracer Reactions**

```json
{
  "Argument": {
    "CURRENT_MODE": "MVLTRC_Reactions",
    "LOAD_CASE_COMB": {"TYPE": "MV", "MINMAX": "Max", "NAME": "DB", "KEY_NODE_ELEM": 1},
    "COMPONENTS": {"COMP": "Fz", "OPT_LOCAL_CHECK": true},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "APPLIED_LOADS": {
        "OPT_CHECK": true,
        "SCALE_FACTOR": 1.0,
        "OPT_LOAD_VALUES": false,
        "VALUE_TYPE": "Exponential",
        "VALUE_DECIMAL_PT": 1
      },
      "OPT_INCLUDE_IMPACT_FACTOR": true
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'MVLTRC_Reactions',
        'LOAD_CASE_COMB': {'TYPE': 'MV', 'MINMAX': 'Max', 'NAME': 'DB', 'KEY_NODE_ELEM': 1},
        'COMPONENTS': {'COMP': 'Fz', 'OPT_LOCAL_CHECK': True},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'APPLIED_LOADS': {
                'OPT_CHECK': True,
                'SCALE_FACTOR': 1.0,
                'OPT_LOAD_VALUES': False,
                'VALUE_TYPE': 'Exponential',
                'VALUE_DECIMAL_PT': 1
            },
            'OPT_INCLUDE_IMPACT_FACTOR': True
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 22. Displacements (Moving Tracer Display)

> **Source**: [Displacements - Moving Tracer Display ↗](https://support.midasuser.com/hc/en-us/articles/36004334029593)
>
> **`CURRENT_MODE`**: `"MVLTRC_Displacements"`
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `TYPE_OF_DISPLAY.APPLIED_LOADS.SCALE_FACTOR`, `TYPE_OF_DISPLAY.APPLIED_LOADS.OPT_LOAD_VALUES`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_TYPE`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_DECIMAL_PT`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "MVLTRC_Displacements" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Moving Load: "MV" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Select Support Node Number | `"KEY_NODE_ELEM"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "DX", "DY", "DZ" · "RX", "RY", "RZ" · "RW" | `"COMP"` | String | "DX" | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (3) | └ Applied Loads (Moving Load Tracer Detail) | `"APPLIED_LOADS"` | Object | - | Optional |
| (4) | └ Include Impact Factor | `"OPT_INCLUDE_IMPACT_FACTOR"` | Boolean | false | Optional |

### Request JSON

**Moving Tracer Displacements**

```json
{
  "Argument": {
    "CURRENT_MODE": "MVLTRC_Displacements",
    "LOAD_CASE_COMB": {"TYPE": "MV", "MINMAX": "Max", "NAME": "DB", "KEY_NODE_ELEM": 1},
    "COMPONENTS": {"COMP": "Dz"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "APPLIED_LOADS": {
        "OPT_CHECK": true,
        "SCALE_FACTOR": 1.0,
        "OPT_LOAD_VALUES": false,
        "VALUE_TYPE": "Exponential",
        "VALUE_DECIMAL_PT": 1
      },
      "OPT_INCLUDE_IMPACT_FACTOR": true
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'MVLTRC_Displacements',
        'LOAD_CASE_COMB': {'TYPE': 'MV', 'MINMAX': 'Max', 'NAME': 'DB', 'KEY_NODE_ELEM': 1},
        'COMPONENTS': {'COMP': 'Dz'},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'APPLIED_LOADS': {
                'OPT_CHECK': True,
                'SCALE_FACTOR': 1.0,
                'OPT_LOAD_VALUES': False,
                'VALUE_TYPE': 'Exponential',
                'VALUE_DECIMAL_PT': 1
            },
            'OPT_INCLUDE_IMPACT_FACTOR': True
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 23. Truss Forces (Moving Tracer Display)

> **Source**: [Truss Forces - Moving Tracer Display ↗](https://support.midasuser.com/hc/en-us/articles/36004378825497)
>
> **`CURRENT_MODE`**: `"MVLTRC_TrussForces"`
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `TYPE_OF_DISPLAY.APPLIED_LOADS.SCALE_FACTOR`, `TYPE_OF_DISPLAY.APPLIED_LOADS.OPT_LOAD_VALUES`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_TYPE`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_DECIMAL_PT`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "MVLTRC_Truss Forces" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Moving Load: "MV" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Select Support Node Number | `"KEY_NODE_ELEM"` | Integer | - | **Required** |
| 3 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (3) | └ Applied Loads (Moving Load Tracer Detail) | `"APPLIED_LOADS"` | Object | - | Optional |
| (4) | └ Include Impact Factor | `"OPT_INCLUDE_IMPACT_FACTOR"` | Boolean | false | Optional |

### Request JSON

**Moving Tracer Truss Forces**

```json
{
  "Argument": {
    "CURRENT_MODE": "MVLTRC_TrussForces",
    "LOAD_CASE_COMB": {"TYPE": "MV", "MINMAX": "Max", "NAME": "DB", "KEY_NODE_ELEM": 1},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "APPLIED_LOADS": {
        "OPT_CHECK": true,
        "SCALE_FACTOR": 1.0,
        "OPT_LOAD_VALUES": false,
        "VALUE_TYPE": "Exponential",
        "VALUE_DECIMAL_PT": 1
      },
      "OPT_INCLUDE_IMPACT_FACTOR": true
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'MVLTRC_TrussForces',
        'LOAD_CASE_COMB': {'TYPE': 'MV', 'MINMAX': 'Max', 'NAME': 'DB', 'KEY_NODE_ELEM': 1},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'APPLIED_LOADS': {
                'OPT_CHECK': True,
                'SCALE_FACTOR': 1.0,
                'OPT_LOAD_VALUES': False,
                'VALUE_TYPE': 'Exponential',
                'VALUE_DECIMAL_PT': 1
            },
            'OPT_INCLUDE_IMPACT_FACTOR': True
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 24. Beam Forces/Moments (Moving Tracer Display)

> **Source**: [Beam Forces/Moments - Moving Tracer Display ↗](https://support.midasuser.com/hc/en-us/articles/36004453575193)
>
> **`CURRENT_MODE`**: `"MVLTRC_BeamForces/Moments"`
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `TYPE_OF_DISPLAY.APPLIED_LOADS.SCALE_FACTOR`, `TYPE_OF_DISPLAY.APPLIED_LOADS.OPT_LOAD_VALUES`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_TYPE`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_DECIMAL_PT`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "MVLTRC_Beam Forces/Moments" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Moving Load: "MV" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Select Support Node Number | `"KEY_NODE_ELEM"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "FX", "FY", "FZ" · "MX", "MY", "MZ" · "Mb", "Mt", "Mw" | `"COMP"` | String | "FX" | Optional |
| (2) | └ Parts · "i" · "1/4" · "1/2" · "3/4" · "j" | `"PART"` | String | "i" | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (3) | └ Applied Loads (Moving Load Tracer Detail) | `"APPLIED_LOADS"` | Object | - | Optional |
| (4) | └ Include Impact Factor | `"OPT_INCLUDE_IMPACT_FACTOR"` | Boolean | false | Optional |

### Request JSON

**Moving Tracer Beam Forces/Moments**

```json
{
  "Argument": {
    "CURRENT_MODE": "MVLTRC_BeamForces/Moments",
    "LOAD_CASE_COMB": {"TYPE": "MV", "MINMAX": "Max", "NAME": "DB", "KEY_NODE_ELEM": 1},
    "COMPONENTS": {"PART": "1/4", "COMP": "My"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "APPLIED_LOADS": {
        "OPT_CHECK": true,
        "SCALE_FACTOR": 1.0,
        "OPT_LOAD_VALUES": false,
        "VALUE_TYPE": "Exponential",
        "VALUE_DECIMAL_PT": 1
      },
      "OPT_INCLUDE_IMPACT_FACTOR": true
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'MVLTRC_BeamForces/Moments',
        'LOAD_CASE_COMB': {'TYPE': 'MV', 'MINMAX': 'Max', 'NAME': 'DB', 'KEY_NODE_ELEM': 1},
        'COMPONENTS': {'PART': '1/4', 'COMP': 'My'},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'APPLIED_LOADS': {
                'OPT_CHECK': True,
                'SCALE_FACTOR': 1.0,
                'OPT_LOAD_VALUES': False,
                'VALUE_TYPE': 'Exponential',
                'VALUE_DECIMAL_PT': 1
            },
            'OPT_INCLUDE_IMPACT_FACTOR': True
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 25. Plate Forces/Moments (Moving Tracer Display)

> **Source**: [Plate Forces/Moments - Moving Tracer Display ↗](https://support.midasuser.com/hc/en-us/articles/36004497508505)
>
> **`CURRENT_MODE`**: `"MVLTRC_PlateForces/Moments"`
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `TYPE_OF_DISPLAY.APPLIED_LOADS.SCALE_FACTOR`, `TYPE_OF_DISPLAY.APPLIED_LOADS.OPT_LOAD_VALUES`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_TYPE`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_DECIMAL_PT`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "MVLTRC_Plate Forces/Moments" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Moving Load: "MV" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Select Support Node Number | `"KEY_NODE_ELEM"` | Integer | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "Fxx", "Fyy", "Fxy" · "Mxx", "Myy", "Mxy" · "Vxx", "Vyy" | `"COMP"` | String | "Fxx" | Optional |
| (2) | └ Parts · "cent." · "i" · "j" · "k" · "l" | `"PART"` | String | "i" | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (3) | └ Applied Loads (Moving Load Tracer Detail) | `"APPLIED_LOADS"` | Object | - | Optional |
| (4) | └ Include Impact Factor | `"OPT_INCLUDE_IMPACT_FACTOR"` | Boolean | false | Optional |

### Request JSON

**Moving Tracer Plate Forces/Moments**

```json
{
  "Argument": {
    "CURRENT_MODE": "MVLTRC_PlateForces/Moments",
    "LOAD_CASE_COMB": {"TYPE": "MV", "MINMAX": "Max", "NAME": "DB", "KEY_NODE_ELEM": 1},
    "COMPONENTS": {"PART": "cent.", "COMP": "Mxx"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "APPLIED_LOADS": {
        "OPT_CHECK": true,
        "SCALE_FACTOR": 1.0,
        "OPT_LOAD_VALUES": false,
        "VALUE_TYPE": "Exponential",
        "VALUE_DECIMAL_PT": 1
      },
      "OPT_INCLUDE_IMPACT_FACTOR": true
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'MVLTRC_PlateForces/Moments',
        'LOAD_CASE_COMB': {'TYPE': 'MV', 'MINMAX': 'Max', 'NAME': 'DB', 'KEY_NODE_ELEM': 1},
        'COMPONENTS': {'PART': 'cent.', 'COMP': 'Mxx'},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'APPLIED_LOADS': {
                'OPT_CHECK': True,
                'SCALE_FACTOR': 1.0,
                'OPT_LOAD_VALUES': False,
                'VALUE_TYPE': 'Exponential',
                'VALUE_DECIMAL_PT': 1
            },
            'OPT_INCLUDE_IMPACT_FACTOR': True
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 26. Beam Stresses (Moving Tracer Display)

> **Source**: [Beam Stresses - Moving Tracer Display ↗](https://support.midasuser.com/hc/en-us/articles/36005757391385)
>
> **`CURRENT_MODE`**: `"MVLTRC_BeamStresses"`
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `TYPE_OF_DISPLAY.APPLIED_LOADS.OPT_LOAD_VALUES`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_TYPE`, `TYPE_OF_DISPLAY.APPLIED_LOADS.VALUE_DECIMAL_PT`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "MVLTRC_Beam Stresses" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Load Case · Moving Load: "MV" | `"TYPE"` | String | - | **Required** |
| (2) | └ Load Type · Envelop Max: "Max" · Envelop Min: "Min" · Envelop Abs Max: "All" | `"MINMAX"` | String | "Max" | Optional |
| (3) | └ Load Name | `"NAME"` | String | - | **Required** |
| (4) | └ Select Support Node Number | `"KEY_NODE_ELEM"` | Integer | - | **Required** |
| (5) | └ Scale factor | `"SCALE_FACTOR"` | Number | 1 | Optional |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "1 (-y, +z)" · "2 (+y, +z)" · "3 (+y, -z)" · "4 (-y, -z)" | `"COMP"` | String | "1 (-y, +z)" | Optional |
| (2) | └ Parts · "i" · "1/4" · "1/2" · "3/4" · "j" | `"PART"` | String | "i" | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |
| (2) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (3) | └ Applied Loads (Moving Load Tracer Detail) | `"APPLIED_LOADS"` | Object | - | Optional |

### Request JSON

**Moving Tracer Beam Stresses**

```json
{
  "Argument": {
    "CURRENT_MODE": "MVLTRC_BeamStresses",
    "LOAD_CASE_COMB": {"TYPE": "MV", "MINMAX": "Max", "NAME": "MVL", "KEY_NODE_ELEM": 1, "SCALE_FACTOR": 1.0},
    "COMPONENTS": {"PART": "1/4", "COMP": "1(-y,+z)"},
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {"OPT_CHECK": true},
      "APPLIED_LOADS": {
        "OPT_CHECK": true,
        "SCALE_FACTOR": 1.0,
        "OPT_LOAD_VALUES": false,
        "VALUE_TYPE": "Exponential",
        "VALUE_DECIMAL_PT": 1
      }
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'MVLTRC_BeamStresses',
        'LOAD_CASE_COMB': {'TYPE': 'MV', 'MINMAX': 'Max', 'NAME': 'MVL', 'KEY_NODE_ELEM': 1, 'SCALE_FACTOR': 1.0},
        'COMPONENTS': {'PART': '1/4', 'COMP': '1(-y,+z)'},
        'TYPE_OF_DISPLAY': {
            'CONTOUR': {'OPT_CHECK': True},
            'APPLIED_LOADS': {
                'OPT_CHECK': True,
                'SCALE_FACTOR': 1.0,
                'OPT_LOAD_VALUES': False,
                'VALUE_TYPE': 'Exponential',
                'VALUE_DECIMAL_PT': 1
            }
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 27. Vibration Mode Shapes (Mode Shapes Display)

> **Source**: [Vibration Mode Shapes - Mode Shapes Display ↗](https://support.midasuser.com/hc/en-us/articles/36005864558617)
>
> **`CURRENT_MODE`**: `"VibrationModeShapes"`
>
> ⚠️ 예제에는 있으나 Specifications 표에 없는 Key: `TYPE_OF_DISPLAY.VALUES.DECIMAL_PT`

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Vibration Mode Shapes" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Mode Number | `"NAME"` | String | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "Md-X", "Md-Y", "Md-Z" · "Md-XY", "Md-YZ", "Md-XZ" · "Md-XYZ" | `"COMP"` | String | "Md-XYZ" | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Mode Shape | `"MODE_SHAPE"` | Object |  | Optional |
| (2) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |

### Request JSON

**Vibration Mode Shapes**

```json
{
  "Argument": {
    "CURRENT_MODE": "VibrationModeShapes",
    "LOAD_CASE_COMB": {"NAME": "Mode6"},
    "COMPONENTS": {"COMP": "Md-XZ"},
    "TYPE_OF_DISPLAY": {"VALUES": {"OPT_CHECK": true, "DECIMAL_PT": 5}}
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'VibrationModeShapes',
        'LOAD_CASE_COMB': {'NAME': 'Mode6'},
        'COMPONENTS': {'COMP': 'Md-XZ'},
        'TYPE_OF_DISPLAY': {'VALUES': {'OPT_CHECK': True, 'DECIMAL_PT': 5}}
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```

---

## 28. Buckling Mode Shapes (Mode Shapes Display)

> **Source**: [Buckling Mode Shapes - Mode Shapes Display ↗](https://support.midasuser.com/hc/en-us/articles/36005908557465)
>
> **`CURRENT_MODE`**: `"Buckling Mode Shapes"`
>
> ⚠️ 공식 예제의 `"COUNTOUR"`는 `"CONTOUR"` 오탈자로 보고 예제에서 정정했습니다.

### Specifications

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Result Graphic Mode · "Buckling Mode Shapes" | `"CURRENT_MODE"` | String | - | **Required** |
| 2 | Load Case and Combinations | `"LOAD_CASE_COMB"` | Object | - | **Required** |
| (1) | └ Mode Number | `"NAME"` | String | - | **Required** |
| 3 | Components | `"COMPONENTS"` | Object | - | Optional |
| (1) | └ Components Name · "Md-X", "Md-Y", "Md-Z" · "Md-XY", "Md-YZ", "Md-XZ" · "Md-XYZ" | `"COMP"` | String | "Fxx" | Optional |
| 4 | Type of Display ¹⁾ | `"TYPE_OF_DISPLAY"` | Object | - | Optional |
| (1) | └ Mode Shape | `"MODE_SHAPE"` | Boolean | false | Optional |
| (2) | └ Display Undeformed Shape | `"UNDEFORMED"` | Boolean | false | Optional |
| (3) | └ Values Output Details | `"VALUES"` | Object | - | Optional |
| (4) | └ Legend Details | `"LEGEND"` | Object | - | Optional |
| (5) | └ Contour Details | `"CONTOUR"` | Object | - | Optional |

### Request JSON

**Buckling Mode Shapes**

```json
{
  "Argument": {
    "CURRENT_MODE": "Buckling Mode Shapes",
    "LOAD_CASE_COMB": {"NAME": "Mode 2"},
    "COMPONENTS": {"COMP": "Md-XYZ"},
    "TYPE_OF_DISPLAY": {
      "MODE_SHAPE": {"OPT_CHECK": true},
      "UNDEFORMED": {"OPT_CHECK": true},
      "VALUES": {"OPT_CHECK": true},
      "LEGEND": {"OPT_CHECK": true},
      "CONTOUR": {"OPT_CHECK": true}
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

payload = {
    'Argument': {
        'CURRENT_MODE': 'Buckling Mode Shapes',
        'LOAD_CASE_COMB': {'NAME': 'Mode 2'},
        'COMPONENTS': {'COMP': 'Md-XYZ'},
        'TYPE_OF_DISPLAY': {
            'MODE_SHAPE': {'OPT_CHECK': True},
            'UNDEFORMED': {'OPT_CHECK': True},
            'VALUES': {'OPT_CHECK': True},
            'LEGEND': {'OPT_CHECK': True},
            'CONTOUR': {'OPT_CHECK': True}
        }
    }
}

resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(resp.status_code, resp.json())
```
