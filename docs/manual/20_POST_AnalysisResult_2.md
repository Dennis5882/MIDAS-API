# 20. POST – Analysis Result Tables (Part 2)

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

이 파트는 해석 결과 테이블 중 **판(Plate)·평면응력(Plane Stress)·평면변형률(Plane Strain)·축대칭(Axisymmetric)·솔리드(Solid)·링크(Link)·모드(Mode)·텐던(Tendon)·시공단계 합성단면(Composite Section for C.S.)·벽체(Wall)** 결과를 다룹니다. 모든 엔드포인트는 **공통 URI `{base url}/post/TABLE`** 를 사용하며 `POST` 메서드만 지원합니다. 요청 바디의 `"Argument"` 객체에서 `TABLE_TYPE` 값으로 테이블 종류를 결정합니다.

---

## 공통 사항

### Input URI (해석 결과 테이블 공통)

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 공통 Request 구조 및 파라미터

전처리 테이블(18장)보다 확장된 구조로, `UNIT`·`STYLES`·`COMPONENTS`·`NODE_ELEMS`·`LOAD_CASE_NAMES`·`OPT_CS`·`STAGE_STEP`를 지원합니다. **아래 파라미터 표는 본 파트의 39개 테이블 전체에 공통 적용**되며, 각 절에서는 `TABLE_TYPE` enum과 응답 `HEAD` 열, 대표 예시만 별도 기술합니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 응답 테이블 제목 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 (테이블별 enum, 각 절 참조) | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 응답 단위 설정 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 힘(Force) | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 길이(Length) | `UNIT.DIST` | String | — | Optional |
| 4-3 | └ 열(Heat) | `UNIT.HEAT` | String | — | Optional |
| 4-4 | └ 온도(Temperature) | `UNIT.TEMP` | String | — | Optional |
| 5 | 응답 숫자 형식 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 숫자 형식 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 소수 자릿수 (0~15) | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 결과 테이블 표시 열 | `"COMPONENTS"` | Array [String] | All | Optional |
| 7 | 노드/요소 지정 (아래 3방식 중 하나) | `"NODE_ELEMS"` | Object | All | Optional |
| 7-1 | 방식1: ID 각각 지정 (예: `[101, 102, 103]`) | `NODE_ELEMS.KEYS` | Array [Integer] | — | Optional |
| 7-2 | 방식2: ID 범위 지정 (예: `"101 to 105"`) | `NODE_ELEMS.TO` | String | — | Optional |
| 7-3 | 방식3: 구조 그룹명 지정 (예: `"SG1"`) | `NODE_ELEMS.STRUCTURE_GROUP_NAME` | String | — | Optional |
| 8 | 하중 이름 & 타입 (아래 접미사 규칙) | `"LOAD_CASE_NAMES"` | Array [String] | All | Optional |
| 9 | 시공단계 스텝 활성화 | `"OPT_CS"` | Boolean | `false` | Optional |
| 10 | 시공단계 스텝 이름 | `"STAGE_STEP"` | Array [String] | All | Optional |

**`LOAD_CASE_NAMES` 접미사 규칙**

| 하중 유형 | 표기 |
|-----------|------|
| 정적 하중케이스 | `NAME(ST)` |
| 일반 조합 | `NAME(CB)` / `NAME(CB:all)` / `NAME(CB:max)` / `NAME(CB:min)` |
| 시공단계 | `NAME(CS)` |
| 응답스펙트럼 | `NAME(RS)` |
| 이동하중 | `NAME(MV:all)` / `NAME(MV:max)` / `NAME(MV:min)` |
| 침하하중 | `NAME(SM:all)` / `NAME(SM:max)` / `NAME(SM:min)` |

> **참고:** `OPT_CS`·`STAGE_STEP`는 시공단계 결과 조회 시 사용합니다. 판/솔리드 변형률(비선형·시공단계), 텐던 신장량 등 `Step`·`Stage` 열을 포함하는 테이블에서 함께 지정합니다. `STAGE_STEP` 항목은 `"CS1:001(first)"`, `"CS1:002(last)"` 또는 `"nl_001"` 형식입니다.

### 공통 Response 구조

```json
{
  "<TABLE_NAME>": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."], ["2", "..."]]
  }
}
```

---

## 테이블 목록

| No. | 테이블 | `TABLE_TYPE` |
|-----|--------|--------------|
| 1 | [Plate Force (Local)](#1-plate-force-local) | `PLATEFORCEL` |
| 2 | [Plate Force (Global)](#2-plate-force-global) | `PLATEFORCEG` |
| 3 | [Plate Force (Unit Length)](#3-plate-force-unit-length) | `PLATEFORCEUL` / `PLATEFORCEUG` / `PLATEFORCEULVBM` / `PLATEFORCEUGVBM` / `PLATEFORCEWA` |
| 4 | [Plate Stress (Local)](#4-plate-stress-local) | `PLATESTRESSL` |
| 5 | [Plate Stress (Global)](#5-plate-stress-global) | `PLATESTRESSG` |
| 6 | [Plate Strain (Local)](#6-plate-strain-local) | `PLATESTRAINPL` / `PLATESTRAINTL` |
| 7 | [Plate Strain (Global)](#7-plate-strain-global) | `PLATESTRAINPG` / `PLATESTRAINTG` |
| 8 | [Plane Stress Force (Local)](#8-plane-stress-force-local) | `PLANESTRESSFL` |
| 9 | [Plane Stress Force (Global)](#9-plane-stress-force-global) | `PLANESTRESSFG` |
| 10 | [Plane Stress (Local)](#10-plane-stress-local) | `PLANESTRESSSL` |
| 11 | [Plane Stress (Global)](#11-plane-stress-global) | `PLANESTRESSSG` |
| 12 | [Plane Strain Force (Local)](#12-plane-strain-force-local) | `PLANESTRAINFL` |
| 13 | [Plane Strain Force (Global)](#13-plane-strain-force-global) | `PLANESTRAINFG` |
| 14 | [Plane Strain Stress (Local)](#14-plane-strain-stress-local) | `PLANESTRAINSL` |
| 15 | [Plane Strain Stress (Global)](#15-plane-strain-stress-global) | `PLANESTRAINSG` |
| 16 | [Axisymmetric Force (Local)](#16-axisymmetric-force-local) | `AXISYMMETRICFL` |
| 17 | [Axisymmetric Force (Global)](#17-axisymmetric-force-global) | `AXISYMMETRICFG` |
| 18 | [Axisymmetric Stress (Local)](#18-axisymmetric-stress-local) | `AXISYMMETRICSL` |
| 19 | [Axisymmetric Stress (Global)](#19-axisymmetric-stress-global) | `AXISYMMETRICSG` |
| 20 | [Solid Force (Local)](#20-solid-force-local) | `SOLIDFL` |
| 21 | [Solid Force (Global)](#21-solid-force-global) | `SOLIDFG` |
| 22 | [Solid Stress (Local)](#22-solid-stress-local) | `SOLIDSL` |
| 23 | [Solid Stress (Global)](#23-solid-stress-global) | `SOLIDSG` |
| 24 | [Solid Strain (Local)](#24-solid-strain-local) | `SOLID_LOCA_PLAST_STRAIN` / `SOLID_LOCA_TOTAL_STRAIN` |
| 25 | [Solid Strain (Global)](#25-solid-strain-global) | `SOLID_GLOB_PLAST_STRAIN` / `SOLID_GLOB_TOTAL_STRAIN` |
| 26 | [Elastic Link](#26-elastic-link) | `ELASTICLINK` / `ELASTICLINKVBM` |
| 27 | [General Link](#27-general-link) | `GENERAL_LINK_FORCE` / `GENERAL_LINK_FORCEVBM` / `GENERAL_LINK_DEFORM` |
| 28 | [Vibration Mode Shape](#28-vibration-mode-shape) | `EIGENVALUEMODE` / `PARTICIPATIONVECTORMODE` |
| 29 | [Buckling Mode Shape](#29-buckling-mode-shape) | `BUCKLINGMODE` |
| 30 | [Tendon Coordinates](#30-tendon-coordinates) | `TNDN_COORDINATES` |
| 31 | [Tendon Elongation](#31-tendon-elongation) | `TNDN_ELONGATION` |
| 32 | [Tendon Arrangement](#32-tendon-arrangement) | `TNDN_ARRANGEMENT` |
| 33 | [Tendon Loss](#33-tendon-loss) | `TNDN_LOSS_FORCE` / `TNDN_LOSS_STRESS` |
| 34 | [Tendon Weight](#34-tendon-weight) | `TNDN_WEIGHT_GROUP` / `TNDN_WEIGHT_PROFILE` / `TNDN_WEIGHT_PROPERTY` |
| 35 | [Tendon Stress Limit Check](#35-tendon-stress-limit-check) | `TNDN_STRS_LIMIT_CHECK` |
| 36 | [Tendon Approximate Loss](#36-tendon-approximate-loss) | `TNDN_APPROX_LOSS_FORCE` / `TNDN_APPROX_LOSS_STRESS` |
| 37 | [Composite Section for C.S. (Force and Stress)](#37-composite-section-for-cs-force-and-stress) | `COMPSECTBEAMFORCE` / `COMPSECTBEAMSTRESS` |
| 38 | [Composite Section for C.S. (Self-Constraint Force and Stress)](#38-composite-section-for-cs-self-constraint-force-and-stress) | `SELF_CONST_BEAM_FORCE` / `SELF_CONST_BEAM_STRESS` |
| 39 | [Wall Force](#39-wall-force) | `WALL_FORCE_MOMENT` |

---

## 1. Plate Force (Local)

> **기능:** 판(Plate) 요소의 부재력/모멘트를 요소 국부 좌표계(Local) 기준으로 절점별 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLATEFORCEL"` | Plate 부재력 (국부 좌표계, Local) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateForceLocal",
    "TABLE_TYPE": "PLATEFORCEL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlateForceLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "592", "DL", "773", "39.425020700000", "0.000000000025", "10.288067200000", "0.000000000090", "-2.325503050000", "0.000000000297"]
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

# ── POST: 판 요소 부재력 (국부 좌표계) 추출 ────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlateForceLocal",
        "TABLE_TYPE": "PLATEFORCEL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [592]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateForceLocal", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} Node {d['Node']}: Fx={d['Fx']}, Mz={d['Mz']}")
```

---

## 2. Plate Force (Global)

> **기능:** 판(Plate) 요소의 부재력/모멘트를 전역 좌표계(Global) 기준으로 절점별 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLATEFORCEG"` | Plate 부재력 (전역 좌표계, Global) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "FX", "FY", "FZ", "MX", "MY", "MZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateForceGlobal",
    "TABLE_TYPE": "PLATEFORCEG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlateForceGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "DATA": [
      ["1", "592", "DL", "773", "39.425020700000", "0.000000000025", "10.288067200000", "0.000000000090", "-2.325503050000", "0.000000000297"]
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

# ── POST: 판 요소 부재력 (전역 좌표계) 추출 ────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlateForceGlobal",
        "TABLE_TYPE": "PLATEFORCEG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [592]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateForceGlobal", {})
print(f"판 부재력(전역) {len(table.get('DATA', []))}행")
```

---

## 3. Plate Force (Unit Length)

> **기능:** 판(Plate) 요소의 단위 길이당 부재력/모멘트(막력 Fxx·Fyy·Fxy, 휨 Mxx·Myy·Mxy, 주값 Fmax/Fmin·Mmax/Mmin, 전단 Vxx·Vyy)를 추출합니다. 국부/전역, 일반/최댓값 기준(by-max), Wood-Armer 설계 모멘트를 선택할 수 있습니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLATEFORCEUL"` | 단위 길이당 부재력 (국부 좌표계, Unit Length Local) |
| `"PLATEFORCEUG"` | 단위 길이당 부재력 (전역 좌표계, Unit Length Global) |
| `"PLATEFORCEULVBM"` | 단위 길이당 부재력 (국부, 최댓값 기준 by-max) |
| `"PLATEFORCEUGVBM"` | 단위 길이당 부재력 (전역, 최댓값 기준 by-max) |
| `"PLATEFORCEWA"` | 단위 길이당 부재력 (Wood-Armer 설계 모멘트) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fxx", "Fyy", "Fxy", "Fmax", "Fmin", "Angle", "Mxx", "Myy", "Mxy", "Mmax", "Mmin", "Angle", "Vxx", "Vyy"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateForceUnitLength",
    "TABLE_TYPE": "PLATEFORCEUL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fxx", "Fyy", "Fxy", "Fmax", "Fmin", "Mxx", "Myy", "Mxy", "Mmax", "Mmin", "Vxx", "Vyy"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlateForceUnitLength": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fxx", "Fyy", "Fxy", "Fmax", "Fmin", "Angle", "Mxx", "Myy", "Mxy", "Mmax", "Mmin", "Angle", "Vxx", "Vyy"],
    "DATA": [
      ["1", "592", "DL", "773", "-108.226897000000", "5.103138340000", "-0.000000011818", "5.103138340000", "-108.226897000000", "-89.999999994025", "1.744257540000", "0.141650776000", "0.000000000120", "1.744257540000", "0.141650776000", "0.000000004303", "-1.405381470000", "-0.000000000024"]
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

# ── POST: 단위 길이당 판 부재력 추출 ───────────────────────────────
#   Wood-Armer 설계 모멘트: TABLE_TYPE="PLATEFORCEWA"
#   최댓값 기준(by-max):   TABLE_TYPE="PLATEFORCEULVBM" / "PLATEFORCEUGVBM"
payload = {
    "Argument": {
        "TABLE_NAME": "PlateForceUnitLength",
        "TABLE_TYPE": "PLATEFORCEUL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [592]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateForceUnitLength", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']}: Mmax={d['Mmax']}, Mmin={d['Mmin']}")
```

---

## 4. Plate Stress (Local)

> **기능:** 판(Plate) 요소의 응력을 요소 국부 좌표계(Local) 기준으로 상·하면(Top/Bot)별로 추출합니다. 성분 응력(Sig-xx·yy·xy), 주응력(Sig-Max/Min), 유효응력(Sig-EFF), 최대전단(Max-Shear)을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLATESTRESSL"` | Plate 응력 (국부 좌표계, Local) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Part", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear", "Part", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"]`  
(앞쪽 8개는 `Top` 성분, 뒤쪽 8개는 `Bot` 성분)

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateStressLocal",
    "TABLE_TYPE": "PLATESTRESSL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Part", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Sig-EFF", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlateStressLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Part", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear", "Part", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"],
    "DATA": [
      ["1", "592", "DL", "773", "Top", "-0.600356311193", "0.006814078891", "-0.000000000059", "0.006814078891", "-0.600356311193", "-89.999999994449", "0.603792188859", "0.303585195042", "Bot", "-0.265458864386", "0.034011027791", "-0.000000000036", "0.034011027791", "-0.265458864386", "-89.999999993166", "0.283995928680", "0.149734946089"]
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

# ── POST: 판 응력 (국부 좌표계) 추출 ───────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlateStressLocal",
        "TABLE_TYPE": "PLATESTRESSL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [592]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateStressLocal", {})
print(f"판 응력(국부) {len(table.get('DATA', []))}행")
```

---

## 5. Plate Stress (Global)

> **기능:** 판(Plate) 요소의 응력을 전역 좌표계(Global) 기준으로 상·하면(Top/Bot)별로 추출합니다. 6성분 응력(Sig-XX·YY·ZZ·XY·YZ·XZ)과 주응력·유효응력·최대전단을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLATESTRESSG"` | Plate 응력 (전역 좌표계, Global) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Part", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "ANG", "Sig-EFF", "Max-Shear", "Part", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "ANG", "Sig-EFF", "Max-Shear"]`  
(앞쪽 11개는 `Top` 성분, 뒤쪽 11개는 `Bot` 성분)

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateStressGlobal",
    "TABLE_TYPE": "PLATESTRESSG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Part", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "Sig-EFF", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlateStressGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Part", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "ANG", "Sig-EFF", "Max-Shear", "Part", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "ANG", "Sig-EFF", "Max-Shear"],
    "DATA": [
      ["1", "592", "DL", "773", "Top", "-0.600356311193", "0.006814078891", "0.000000000000", "-0.000000000059", "0.000000000000", "0.000000000000", "0.006814078891", "-0.600356311193", "0.000000005579", "0.603792188859", "0.303585195042", "Bot", "-0.265458864386", "0.034011027791", "0.000000000000", "-0.000000000036", "0.000000000000", "0.000000000000", "0.034011027791", "-0.265458864386", "0.000000026901", "0.283995928680", "0.149734946089"]
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

# ── POST: 판 응력 (전역 좌표계) 추출 ───────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlateStressGlobal",
        "TABLE_TYPE": "PLATESTRESSG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [592]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateStressGlobal", {})
print(f"판 응력(전역) {len(table.get('DATA', []))}행")
```

---

## 6. Plate Strain (Local)

> **기능:** 판(Plate) 요소의 변형률을 요소 국부 좌표계(Local) 기준으로 상·하면(Top/Bot)별로 추출합니다. 소성 변형률(Plastic)/전체 변형률(Total)을 선택할 수 있으며, 비선형·시공단계의 `Step`별로 조회됩니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLATESTRAINPL"` | Plate 변형률 (국부, 소성 Plastic Strain) |
| `"PLATESTRAINTL"` | Plate 변형률 (국부, 전체 Total Strain) |

### Response HEAD

`["Index", "Elem", "Load", "Step", "Node", "Part", "Strain-xx", "Strain-yy", "Strain-xy", "Strain-Max", "Strain-Min", "Angle", "Max-Shear", "Part", "Strain-xx", "Strain-yy", "Strain-xy", "Strain-Max", "Strain-Min", "Angle", "Max-Shear"]`  
(앞쪽 7개는 `Top` 성분, 뒤쪽 7개는 `Bot` 성분)

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateStrainLocal",
    "TABLE_TYPE": "PLATESTRAINTL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Step", "Node", "Part", "Strain-xx", "Strain-yy", "Strain-xy", "Strain-Max", "Strain-Min", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Comp(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["nl_001"]
  }
}
```

**POST Response Body**

```json
{
  "PlateStrainLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Step", "Node", "Part", "Strain-xx", "Strain-yy", "Strain-xy", "Strain-Max", "Strain-Min", "Angle", "Max-Shear", "Part", "Strain-xx", "Strain-yy", "Strain-xy", "Strain-Max", "Strain-Min", "Angle", "Max-Shear"],
    "DATA": [
      ["1", "1", "Comp", "nl_001", "Cent", "Top", "-8.741440490892e-07", "9.705634584017e-06", "3.124953352515e-06", "1.055970672867e-05", "-1.728216193741e-06", "7.471396063715e+01", "6.143961461205e-06", "Bot", "-8.741440490892e-07", "9.705634584017e-06", "3.124953352515e-06", "1.055970672867e-05", "-1.728216193741e-06", "7.471396063715e+01", "6.143961461205e-06"]
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

# ── POST: 판 변형률 (국부) 추출 ───────────────────────────────────
#   소성 변형률: TABLE_TYPE="PLATESTRAINPL"
payload = {
    "Argument": {
        "TABLE_NAME": "PlateStrainLocal",
        "TABLE_TYPE": "PLATESTRAINTL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["Comp(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateStrainLocal", {})
print(f"판 변형률(국부) {len(table.get('DATA', []))}행")
```

---

## 7. Plate Strain (Global)

> **기능:** 판(Plate) 요소의 변형률을 전역 좌표계(Global) 기준으로 상·하면(Top/Bot)별로 추출합니다. 소성/전체 변형률을 선택할 수 있으며 6성분(Strain-XX·YY·ZZ·XY·YZ·XZ)과 주변형률·최대전단을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLATESTRAINPG"` | Plate 변형률 (전역, 소성 Plastic Strain) |
| `"PLATESTRAINTG"` | Plate 변형률 (전역, 전체 Total Strain) |

### Response HEAD

`["Index", "Elem", "Load", "Step", "Node", "Part", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-Max", "Strain-Min", "Angle", "Max-Shear", "Part", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-Max", "Strain-Min", "Angle", "Max-Shear"]`  
(앞쪽 10개는 `Top` 성분, 뒤쪽 10개는 `Bot` 성분)

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateStrainGlobal",
    "TABLE_TYPE": "PLATESTRAINTG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Step", "Node", "Part", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-Max", "Strain-Min", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Comp(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["nl_001"]
  }
}
```

**POST Response Body**

```json
{
  "PlateStrainGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Step", "Node", "Part", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-Max", "Strain-Min", "Angle", "Max-Shear", "Part", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-Max", "Strain-Min", "Angle", "Max-Shear"],
    "DATA": [
      ["1", "1", "Comp", "nl_001", "Cent", "Top", "-8.741440490892e-07", "0.000000000000e+00", "9.705634584017e-06", "0.000000000000e+00", "0.000000000000e+00", "3.124953352515e-06", "1.055970672867e-05", "-1.728216193741e-06", "7.471396063715e+01", "6.143961461205e-06", "Bot", "-8.741440490892e-07", "0.000000000000e+00", "9.705634584017e-06", "0.000000000000e+00", "0.000000000000e+00", "3.124953352515e-06", "1.055970672867e-05", "-1.728216193741e-06", "7.471396063715e+01", "6.143961461205e-06"]
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

# ── POST: 판 변형률 (전역) 추출 ───────────────────────────────────
#   소성 변형률: TABLE_TYPE="PLATESTRAINPG"
payload = {
    "Argument": {
        "TABLE_NAME": "PlateStrainGlobal",
        "TABLE_TYPE": "PLATESTRAINTG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["Comp(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateStrainGlobal", {})
print(f"판 변형률(전역) {len(table.get('DATA', []))}행")
```

---

## 8. Plane Stress Force (Local)

> **기능:** 평면응력(Plane Stress) 요소의 절점 부재력을 요소 국부 좌표계(Local) 기준으로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLANESTRESSFL"` | 평면응력 요소 부재력 (국부 좌표계, Local) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fx", "Fy"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStressForceLocal",
    "TABLE_TYPE": "PLANESTRESSFL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fx", "Fy"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStressForceLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fx", "Fy"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "-920.132331101835", "-13.885776516351"]
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

# ── POST: 평면응력 요소 부재력 (국부) 추출 ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStressForceLocal",
        "TABLE_TYPE": "PLANESTRESSFL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStressForceLocal", {})
for row in table.get("DATA", []):
    print(f"  Elem {row[1]} Node {row[3]}: Fx={row[4]}, Fy={row[5]}")
```

---

## 9. Plane Stress Force (Global)

> **기능:** 평면응력(Plane Stress) 요소의 절점 부재력을 전역 좌표계(Global) 기준으로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLANESTRESSFG"` | 평면응력 요소 부재력 (전역 좌표계, Global) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStressForceGlobal",
    "TABLE_TYPE": "PLANESTRESSFG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "FX", "FY", "FZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStressForceGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "-920.132331101835", "-13.885776516351", "0.000000000000"]
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

# ── POST: 평면응력 요소 부재력 (전역) 추출 ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStressForceGlobal",
        "TABLE_TYPE": "PLANESTRESSFG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStressForceGlobal", {})
print(f"평면응력 부재력(전역) {len(table.get('DATA', []))}행")
```

---

## 10. Plane Stress (Local)

> **기능:** 평면응력(Plane Stress) 요소의 응력을 요소 국부 좌표계(Local) 기준으로 추출합니다. 성분 응력·주응력·유효응력(Sig-EFF)·최대전단을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLANESTRESSSL"` | 평면응력 요소 응력 (국부 좌표계, Local) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStressLocal",
    "TABLE_TYPE": "PLANESTRESSSL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Sig-EFF", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStressLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "9.923982961671", "1.180584451040", "-0.319470675593", "9.935640398605", "1.168927014105", "-2.089787188087", "9.405812140923", "4.967820199303"]
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

# ── POST: 평면응력 요소 응력 (국부) 추출 ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStressLocal",
        "TABLE_TYPE": "PLANESTRESSSL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStressLocal", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']}: Sig-EFF={d['Sig-EFF']}")
```

---

## 11. Plane Stress (Global)

> **기능:** 평면응력(Plane Stress) 요소의 응력을 전역 좌표계(Global) 기준으로 추출합니다. 6성분 응력(Sig-XX·YY·ZZ·XY·YZ·XZ)과 주응력·유효응력·최대전단을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLANESTRESSSG"` | 평면응력 요소 응력 (전역 좌표계, Global) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStressGlobal",
    "TABLE_TYPE": "PLANESTRESSSG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "Sig-EFF", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStressGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "9.923982961671", "1.180584451040", "0.000000000000", "-0.319470675593", "0.000000000000", "0.000000000000", "9.935640398605", "1.168927014105", "-2.089787188087", "9.405812140923", "4.967820199303"]
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

# ── POST: 평면응력 요소 응력 (전역) 추출 ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStressGlobal",
        "TABLE_TYPE": "PLANESTRESSSG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStressGlobal", {})
print(f"평면응력 응력(전역) {len(table.get('DATA', []))}행")
```

---

## 12. Plane Strain Force (Local)

> **기능:** 평면변형률(Plane Strain) 요소의 절점 부재력을 요소 국부 좌표계(Local) 기준으로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLANESTRAINFL"` | 평면변형률 요소 부재력 (국부 좌표계, Local) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainForceLocal",
    "TABLE_TYPE": "PLANESTRAINFL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStrainForceLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "-1027.821540000000", "-45.249848700000", "0.000000000000"]
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

# ── POST: 평면변형률 요소 부재력 (국부) 추출 ───────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStrainForceLocal",
        "TABLE_TYPE": "PLANESTRAINFL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStrainForceLocal", {})
print(f"평면변형률 부재력(국부) {len(table.get('DATA', []))}행")
```

---

## 13. Plane Strain Force (Global)

> **기능:** 평면변형률(Plane Strain) 요소의 절점 부재력을 전역 좌표계(Global) 기준으로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLANESTRAINFG"` | 평면변형률 요소 부재력 (전역 좌표계, Global) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainForceGlobal",
    "TABLE_TYPE": "PLANESTRAINFG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "FX", "FY", "FZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStrainForceGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "-1027.821540000000", "0.000000000000", "-45.249848700000"]
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

# ── POST: 평면변형률 요소 부재력 (전역) 추출 ───────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStrainForceGlobal",
        "TABLE_TYPE": "PLANESTRAINFG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStrainForceGlobal", {})
print(f"평면변형률 부재력(전역) {len(table.get('DATA', []))}행")
```

---

## 14. Plane Strain Stress (Local)

> **기능:** 평면변형률(Plane Strain) 요소의 응력을 요소 국부 좌표계(Local) 기준으로 추출합니다. 성분 응력·주응력(Sig-P1/P2/P3)·최대전단·유효응력(Sig-EFF)·팔면체 응력(Sig-OCT)을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLANESTRAINSL"` | 평면변형률 요소 응력 (국부 좌표계, Local) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainStressLocal",
    "TABLE_TYPE": "PLANESTRAINSL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStrainStressLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "11.045924719309", "1.590139074056", "2.274491482806", "-0.288713831615", "11.054731825832", "2.274491482806", "1.581331967533", "4.736699929150", "9.146540205732", "4.311720402579"]
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

# ── POST: 평면변형률 요소 응력 (국부) 추출 ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStrainStressLocal",
        "TABLE_TYPE": "PLANESTRAINSL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStrainStressLocal", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']}: Sig-EFF={d['Sig-EFF']}")
```

---

## 15. Plane Strain Stress (Global)

> **기능:** 평면변형률(Plane Strain) 요소의 응력을 전역 좌표계(Global) 기준으로 추출합니다. 성분 응력·주응력·최대전단·유효응력·팔면체 응력을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"PLANESTRAINSG"` | 평면변형률 요소 응력 (전역 좌표계, Global) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainStressGlobal",
    "TABLE_TYPE": "PLANESTRAINSG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStrainStressGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "11.045924719309", "2.274491482806", "1.590139074056", "-0.288713831615", "11.054731825832", "2.274491482806", "1.581331967533", "4.736699929150", "9.146540205732", "4.311720402579"]
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

# ── POST: 평면변형률 요소 응력 (전역) 추출 ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStrainStressGlobal",
        "TABLE_TYPE": "PLANESTRAINSG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStrainStressGlobal", {})
print(f"평면변형률 응력(전역) {len(table.get('DATA', []))}행")
```

---

## 16. Axisymmetric Force (Local)

> **기능:** 축대칭(Axisymmetric) 요소의 절점 부재력을 요소 국부 좌표계(Local) 기준으로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"AXISYMMETRICFL"` | 축대칭 요소 부재력 (국부 좌표계, Local) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "AxiForceLocal",
    "TABLE_TYPE": "AXISYMMETRICFL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "NODE_ELEMS": { "KEYS": [168] },
    "LOAD_CASE_NAMES": ["Pressure(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "AxiForceLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "DATA": [
      ["1", "168", "Pressure", "195", "38.836185000000", "-21.331526100000", "0.000000000000"]
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

# ── POST: 축대칭 요소 부재력 (국부) 추출 ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "AxiForceLocal",
        "TABLE_TYPE": "AXISYMMETRICFL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [168]},
        "LOAD_CASE_NAMES": ["Pressure(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("AxiForceLocal", {})
print(f"축대칭 부재력(국부) {len(table.get('DATA', []))}행")
```

---

## 17. Axisymmetric Force (Global)

> **기능:** 축대칭(Axisymmetric) 요소의 절점 부재력을 전역 좌표계(Global) 기준으로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"AXISYMMETRICFG"` | 축대칭 요소 부재력 (전역 좌표계, Global) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "AxiForceGlobal",
    "TABLE_TYPE": "AXISYMMETRICFG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "FX", "FY", "FZ"],
    "NODE_ELEMS": { "KEYS": [168] },
    "LOAD_CASE_NAMES": ["Pressure(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "AxiForceGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "168", "Pressure", "195", "37.968593500000", "0.000000000000", "-22.839378200000"]
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

# ── POST: 축대칭 요소 부재력 (전역) 추출 ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "AxiForceGlobal",
        "TABLE_TYPE": "AXISYMMETRICFG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [168]},
        "LOAD_CASE_NAMES": ["Pressure(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("AxiForceGlobal", {})
print(f"축대칭 부재력(전역) {len(table.get('DATA', []))}행")
```

---

## 18. Axisymmetric Stress (Local)

> **기능:** 축대칭(Axisymmetric) 요소의 응력을 요소 국부 좌표계(Local) 기준으로 추출합니다. 성분 응력·주응력·최대전단·유효응력·팔면체 응력을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"AXISYMMETRICSL"` | 축대칭 요소 응력 (국부 좌표계, Local) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "AxiStressLocal",
    "TABLE_TYPE": "AXISYMMETRICSL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [168] },
    "LOAD_CASE_NAMES": ["Pressure(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "AxiStressLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "DATA": [
      ["1", "168", "Pressure", "195", "1990.431496539230", "2083.494588655180", "2037.166754685250", "593.843481294873", "2632.626761027040", "2037.166754685250", "1441.299324167370", "595.663718429839", "1031.719844657850", "486.357398961529"]
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

# ── POST: 축대칭 요소 응력 (국부) 추출 ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "AxiStressLocal",
        "TABLE_TYPE": "AXISYMMETRICSL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [168]},
        "LOAD_CASE_NAMES": ["Pressure(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("AxiStressLocal", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']}: Sig-P1={d['Sig-P1']}, Sig-EFF={d['Sig-EFF']}")
```

---

## 19. Axisymmetric Stress (Global)

> **기능:** 축대칭(Axisymmetric) 요소의 응력을 전역 좌표계(Global) 기준으로 추출합니다. 성분 응력·주응력·최대전단·유효응력·팔면체 응력을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"AXISYMMETRICSG"` | 축대칭 요소 응력 (전역 좌표계, Global) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "AxiStressGlobal",
    "TABLE_TYPE": "AXISYMMETRICSG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [168] },
    "LOAD_CASE_NAMES": ["Pressure(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "AxiStressGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "DATA": [
      ["1", "168", "Pressure", "195", "2037.166754718370", "2037.166754685250", "2036.759330476040", "595.663683594885", "2632.626761026030", "2037.166754685250", "1441.299324168380", "595.663718428826", "1031.719844655510", "486.357398960426"]
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

# ── POST: 축대칭 요소 응력 (전역) 추출 ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "AxiStressGlobal",
        "TABLE_TYPE": "AXISYMMETRICSG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [168]},
        "LOAD_CASE_NAMES": ["Pressure(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("AxiStressGlobal", {})
print(f"축대칭 응력(전역) {len(table.get('DATA', []))}행")
```

---

## 20. Solid Force (Local)

> **기능:** 솔리드(Solid) 요소의 절점 부재력을 요소 국부 좌표계(Local) 기준으로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"SOLIDFL"` | 솔리드 요소 부재력 (국부 좌표계, Local) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidForceLocal",
    "TABLE_TYPE": "SOLIDFL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "NODE_ELEMS": { "KEYS": [3381] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "SolidForceLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "DATA": [
      ["1", "3381", "DL", "4052", "0.707825934544", "0.602292418927", "0.687505765503"]
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

# ── POST: 솔리드 요소 부재력 (국부) 추출 ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "SolidForceLocal",
        "TABLE_TYPE": "SOLIDFL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [3381]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidForceLocal", {})
print(f"솔리드 부재력(국부) {len(table.get('DATA', []))}행")
```

---

## 21. Solid Force (Global)

> **기능:** 솔리드(Solid) 요소의 절점 부재력을 전역 좌표계(Global) 기준으로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"SOLIDFG"` | 솔리드 요소 부재력 (전역 좌표계, Global) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidForceGlobal",
    "TABLE_TYPE": "SOLIDFG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "FX", "FY", "FZ"],
    "NODE_ELEMS": { "KEYS": [3381] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "SolidForceGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "3381", "DL", "4052", "0.845100207437", "-0.386754897708", "0.687505765503"]
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

# ── POST: 솔리드 요소 부재력 (전역) 추출 ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "SolidForceGlobal",
        "TABLE_TYPE": "SOLIDFG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [3381]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidForceGlobal", {})
print(f"솔리드 부재력(전역) {len(table.get('DATA', []))}행")
```

---

## 22. Solid Stress (Local)

> **기능:** 솔리드(Solid) 요소의 응력을 요소 국부 좌표계(Local) 기준으로 추출합니다. 6성분 응력·주응력(Sig-P1/P2/P3)과 각 주응력의 방향 코사인(P1/ux·uy·uz 등)·최대전단·유효응력·팔면체 응력을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"SOLIDSL"` | 솔리드 요소 응력 (국부 좌표계, Local) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-yz", "Sig-xz", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT", "Sig-P1/ux", "Sig-P1/uy", "Sig-P1/uz", "Sig-P2/ux", "Sig-P2/uy", "Sig-P2/uz", "Sig-P3/ux", "Sig-P3/uy", "Sig-P3/uz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidStressLocal",
    "TABLE_TYPE": "SOLIDSL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-yz", "Sig-xz", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [3381] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "SolidStressLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-yz", "Sig-xz", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT", "Sig-P1/ux", "Sig-P1/uy", "Sig-P1/uz", "Sig-P2/ux", "Sig-P2/uy", "Sig-P2/uz", "Sig-P3/ux", "Sig-P3/uy", "Sig-P3/uz"],
    "DATA": [
      ["1", "3381", "DL", "Cent", "-0.009540404177", "-0.009754688093", "-0.067613370680", "0.000000149510", "-0.000003700681", "-0.003643177715", "-0.009312743454", "-0.009754688186", "-0.067841031311", "0.029264143929", "0.058308571635", "0.027486924270", "0.998052857758", "0.000859886913", "-0.062367890106", "-0.000862168620", "0.999999628286", "-0.000009672638", "0.062367858606", "0.000063425441", "0.998053228135"]
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

# ── POST: 솔리드 요소 응력 (국부) 추출 ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "SolidStressLocal",
        "TABLE_TYPE": "SOLIDSL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [3381]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidStressLocal", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']}: Sig-P1={d['Sig-P1']}, Sig-EFF={d['Sig-EFF']}")
```

---

## 23. Solid Stress (Global)

> **기능:** 솔리드(Solid) 요소의 응력을 전역 좌표계(Global) 기준으로 추출합니다. 6성분 응력·주응력·방향 코사인·최대전단·유효응력·팔면체 응력을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"SOLIDSG"` | 솔리드 요소 응력 (전역 좌표계, Global) |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT", "Sig-P1/ux", "Sig-P1/uy", "Sig-P1/uz", "Sig-P2/ux", "Sig-P2/uy", "Sig-P2/uz", "Sig-P3/ux", "Sig-P3/uy", "Sig-P3/uz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidStressGlobal",
    "TABLE_TYPE": "SOLIDSG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [3381] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "SolidStressGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT", "Sig-P1/ux", "Sig-P1/uy", "Sig-P1/uz", "Sig-P2/ux", "Sig-P2/uy", "Sig-P2/uz", "Sig-P3/ux", "Sig-P3/uy", "Sig-P3/uz"],
    "DATA": [
      ["1", "3381", "DL", "4052", "-0.013482340647", "-0.013660921945", "-0.066735565488", "0.000127121684", "0.003275593336", "-0.002050775097", "-0.013403458224", "-0.013459546178", "-0.067015823678", "0.026806182727", "0.053584343493", "0.025259901766", "0.999095568656", "0.020691098082", "-0.037147316882", "-0.018358914462", "0.997903478478", "0.062061243156", "0.038353552001", "-0.061323128609", "0.997380809393"]
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

# ── POST: 솔리드 요소 응력 (전역) 추출 ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "SolidStressGlobal",
        "TABLE_TYPE": "SOLIDSG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [3381]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidStressGlobal", {})
print(f"솔리드 응력(전역) {len(table.get('DATA', []))}행")
```

---

## 24. Solid Strain (Local)

> **기능:** 솔리드(Solid) 요소의 변형률을 요소 국부 좌표계(Local) 기준으로 추출합니다. 소성/전체 변형률을 선택할 수 있으며, 비선형·시공단계의 `Step`별로 조회됩니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"SOLID_LOCA_PLAST_STRAIN"` | 솔리드 변형률 (국부, 소성 Plastic Strain) |
| `"SOLID_LOCA_TOTAL_STRAIN"` | 솔리드 변형률 (국부, 전체 Total Strain) |

### Response HEAD

`["Index", "Elem", "Load", "Step", "Node", "Strain-xx", "Strain-yy", "Strain-zz", "Strain-xy", "Strain-yz", "Strain-xz", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidStrainLocal",
    "TABLE_TYPE": "SOLID_LOCA_TOTAL_STRAIN",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Step", "Node", "Strain-xx", "Strain-yy", "Strain-zz", "Strain-xy", "Strain-yz", "Strain-xz", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [205] },
    "LOAD_CASE_NAMES": ["Comp(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["nl_001"]
  }
}
```

**POST Response Body**

```json
{
  "SolidStrainLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Step", "Node", "Strain-xx", "Strain-yy", "Strain-zz", "Strain-xy", "Strain-yz", "Strain-xz", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"],
    "DATA": [
      ["1", "205", "Comp", "nl_001", "1", "4.390947924304e-06", "-1.526607997151e-07", "-1.869003906363e-07", "1.999020761608e-06", "-2.101840625867e-08", "6.652619107252e-07", "5.215377841926e-06", "-1.701366927411e-07", "-9.938544152325e-07", "3.104616128579e-06"]
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

# ── POST: 솔리드 변형률 (국부) 추출 ───────────────────────────────
#   소성 변형률: TABLE_TYPE="SOLID_LOCA_PLAST_STRAIN"
payload = {
    "Argument": {
        "TABLE_NAME": "SolidStrainLocal",
        "TABLE_TYPE": "SOLID_LOCA_TOTAL_STRAIN",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [205]},
        "LOAD_CASE_NAMES": ["Comp(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidStrainLocal", {})
print(f"솔리드 변형률(국부) {len(table.get('DATA', []))}행")
```

---

## 25. Solid Strain (Global)

> **기능:** 솔리드(Solid) 요소의 변형률을 전역 좌표계(Global) 기준으로 추출합니다. 소성/전체 변형률을 선택할 수 있으며, 비선형·시공단계의 `Step`별로 조회됩니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"SOLID_GLOB_PLAST_STRAIN"` | 솔리드 변형률 (전역, 소성 Plastic Strain) |
| `"SOLID_GLOB_TOTAL_STRAIN"` | 솔리드 변형률 (전역, 전체 Total Strain) |

### Response HEAD

`["Index", "Elem", "Load", "Step", "Node", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidStrainGlobal",
    "TABLE_TYPE": "SOLID_GLOB_TOTAL_STRAIN",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Step", "Node", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [205] },
    "LOAD_CASE_NAMES": ["Comp(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["nl_001"]
  }
}
```

**POST Response Body**

```json
{
  "SolidStrainGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Step", "Node", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"],
    "DATA": [
      ["1", "205", "Comp", "nl_001", "1", "-1.526607997151e-07", "-1.869003906363e-07", "4.390947924304e-06", "-2.101840625867e-08", "6.652619107252e-07", "1.999020761608e-06", "5.215377841926e-06", "-1.701366927411e-07", "-9.938544152325e-07", "3.104616128579e-06"]
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

# ── POST: 솔리드 변형률 (전역) 추출 ───────────────────────────────
#   소성 변형률: TABLE_TYPE="SOLID_GLOB_PLAST_STRAIN"
payload = {
    "Argument": {
        "TABLE_NAME": "SolidStrainGlobal",
        "TABLE_TYPE": "SOLID_GLOB_TOTAL_STRAIN",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [205]},
        "LOAD_CASE_NAMES": ["Comp(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidStrainGlobal", {})
print(f"솔리드 변형률(전역) {len(table.get('DATA', []))}행")
```

---

## 26. Elastic Link

> **기능:** 탄성 링크(Elastic Link) 요소의 부재력(축력·전단·비틀림·모멘트)을 절점별로 추출합니다. 일반/최댓값 기준(by-max)을 선택할 수 있습니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"ELASTICLINK"` | 탄성 링크 부재력 |
| `"ELASTICLINKVBM"` | 탄성 링크 부재력 (최댓값 기준 by-max) |

### Response HEAD

`["Index", "No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "ElasticLink",
    "TABLE_TYPE": "ELASTICLINK",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "LOAD_CASE_NAMES": ["SWofGirders(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "ElasticLink": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1", "SWofGirders", "1", "-2.163226913452", "0.262795234546", "7.112188879013", "-0.000000245586", "1.306126533508", "0.030306393385"]
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

# ── POST: 탄성 링크 부재력 추출 ────────────────────────────────────
#   최댓값 기준(by-max): TABLE_TYPE="ELASTICLINKVBM"
payload = {
    "Argument": {
        "TABLE_NAME": "ElasticLink",
        "TABLE_TYPE": "ELASTICLINK",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SWofGirders(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("ElasticLink", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Link {d['No.']}: Axial={d['Axial']}, Shear-z={d['Shear-z']}")
```

---

## 27. General Link

> **기능:** 일반 링크(General Link) 요소의 부재력(축력·전단·비틀림·모멘트) 또는 변형(Deform)을 추출합니다. 부재력은 일반/최댓값 기준(by-max)을 선택할 수 있습니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"GENERAL_LINK_FORCE"` | 일반 링크 부재력 |
| `"GENERAL_LINK_FORCEVBM"` | 일반 링크 부재력 (최댓값 기준 by-max) |
| `"GENERAL_LINK_DEFORM"` | 일반 링크 변형 (Deform) |

### Response HEAD

`["Index", "No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "GeneralLink",
    "TABLE_TYPE": "GENERAL_LINK_FORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "LOAD_CASE_NAMES": ["SWofGirders(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "GeneralLink": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1", "SWofGirders", "3536", "-24.885666367763", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"]
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

# ── POST: 일반 링크 부재력 추출 ────────────────────────────────────
#   최댓값 기준(by-max): TABLE_TYPE="GENERAL_LINK_FORCEVBM"
#   변형(Deform):        TABLE_TYPE="GENERAL_LINK_DEFORM"
payload = {
    "Argument": {
        "TABLE_NAME": "GeneralLink",
        "TABLE_TYPE": "GENERAL_LINK_FORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SWofGirders(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("GeneralLink", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Link {d['No.']}: Axial={d['Axial']}")
```

---

## 28. Vibration Mode Shape

> **기능:** 고유치 해석(Eigenvalue) 진동 모드형상 또는 참여벡터(Participation Vector) 모드형상을 절점별·모드별로 추출합니다(병진 UX·UY·UZ, 회전 RX·RY·RZ).

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"EIGENVALUEMODE"` | 고유치(Eigenvalue) 진동 모드형상 |
| `"PARTICIPATIONVECTORMODE"` | 참여벡터(Participation Vector) 모드형상 |

### Response HEAD

`["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "VibrationMode",
    "TABLE_TYPE": "EIGENVALUEMODE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [1] }
  }
}
```

**POST Response Body**

```json
{
  "VibrationMode": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "1", "1", "3.837572718516e-02", "-2.976241858587e-07", "0.000000000000e+00", "2.380992695526e-07", "4.126895212051e-06", "-5.142371718861e-07"]
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

# ── POST: 진동 모드형상 추출 ───────────────────────────────────────
#   참여벡터: TABLE_TYPE="PARTICIPATIONVECTORMODE"
payload = {
    "Argument": {
        "TABLE_NAME": "VibrationMode",
        "TABLE_TYPE": "EIGENVALUEMODE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [1]}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("VibrationMode", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Node {d['Node']} Mode {d['Mode']}: UX={d['UX']}")
```

---

## 29. Buckling Mode Shape

> **기능:** 좌굴 해석(Buckling)의 모드형상을 절점별·모드별로 추출합니다(병진 UX·UY·UZ, 회전 RX·RY·RZ).

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"BUCKLINGMODE"` | 좌굴(Buckling) 모드형상 |

### Response HEAD

`["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "BucklingMode",
    "TABLE_TYPE": "BUCKLINGMODE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [1] }
  }
}
```

**POST Response Body**

```json
{
  "BucklingMode": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "1", "1", "-3.068406433733e-05", "1.071752325513e-10", "-2.756625224655e-08", "0.000000000000e+00", "2.040060468720e-08", "1.430189905494e-10"]
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

# ── POST: 좌굴 모드형상 추출 ───────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "BucklingMode",
        "TABLE_TYPE": "BUCKLINGMODE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [1]}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BucklingMode", {})
print(f"좌굴 모드형상 {len(table.get('DATA', []))}행")
```

---

## 30. Tendon Coordinates

> **기능:** 텐던(Tendon)의 프로파일 좌표(x·y·z)를 텐던별·구간(No)별로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TNDN_COORDINATES"` | 텐던 좌표 |

### Response HEAD

`["Index", "TendonName", "No", "x", "y", "z"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonCoordinates",
    "TABLE_TYPE": "TNDN_COORDINATES",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonName", "No", "x", "y", "z"]
  }
}
```

**POST Response Body**

```json
{
  "TendonCoordinates": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonName", "No", "x", "y", "z"],
    "DATA": [
      ["1", "Bot-Key-A01", "0", "139.500000000000", "0.000000000000", "0.000000000000"]
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

# ── POST: 텐던 좌표 추출 ───────────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TendonCoordinates",
        "TABLE_TYPE": "TNDN_COORDINATES",
        "UNIT": {"FORCE": "kN", "DIST": "m"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonCoordinates", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['TendonName']} #{d['No']}: ({d['x']}, {d['y']}, {d['z']})")
```

---

## 31. Tendon Elongation

> **기능:** 텐던(Tendon)의 신장량(Elongation)을 시공단계(Stage)·스텝(Step)별로 추출합니다. 텐던 자체 신장·요소 신장·합계를 시작단(Begin)/종단(End)으로 구분합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TNDN_ELONGATION"` | 텐던 신장량 |

### Response HEAD

`["Index", "TendonName", "Stage", "Step", "TendonElongation/Begin", "TendonElongation/End", "ElementElongation/Begin", "ElementElongation/End", "Summation/Begin", "Summation/End"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonElongation",
    "TABLE_TYPE": "TNDN_ELONGATION",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonName", "Stage", "Step", "TendonElongation/Begin", "TendonElongation/End", "ElementElongation/Begin", "ElementElongation/End", "Summation/Begin", "Summation/End"]
  }
}
```

**POST Response Body**

```json
{
  "TendonElongation": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonName", "Stage", "Step", "TendonElongation/Begin", "TendonElongation/End", "ElementElongation/Begin", "ElementElongation/End", "Summation/Begin", "Summation/End"],
    "DATA": [
      ["1", "Bot-Key-A01", "CS16", "001(first)", "0.127805425338", "0.000000000000", "0.000217812956", "0.000000000000", "0.128023238294", "0.000000000000"]
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

# ── POST: 텐던 신장량 추출 ─────────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TendonElongation",
        "TABLE_TYPE": "TNDN_ELONGATION",
        "UNIT": {"FORCE": "kN", "DIST": "m"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonElongation", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['TendonName']} ({d['Stage']}): 합계={d['Summation/Begin']}")
```

---

## 32. Tendon Arrangement

> **기능:** 텐던(Tendon)의 요소 내 배치 정보(단면 위치 Yp·Zp, 평균 방향 sin/cos, 평균 응력·평균 힘)를 요소·위치(Part)·텐던 번호별로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TNDN_ARRANGEMENT"` | 텐던 배치 |

### Response HEAD

`["Index", "Elem", "Part", "TendonNumber", "Yp", "Zp", "AverageSinθ", "AverageCosθ", "AverageStress", "AverageForce"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonArrangement",
    "TABLE_TYPE": "TNDN_ARRANGEMENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "TendonNumber", "Yp", "Zp", "AverageSinθ", "AverageCosθ", "AverageStress", "AverageForce"],
    "NODE_ELEMS": { "KEYS": [50] }
  }
}
```

**POST Response Body**

```json
{
  "TendonArrangement": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Part", "TendonNumber", "Yp", "Zp", "AverageSinθ", "AverageCosθ", "AverageStress", "AverageForce"],
    "DATA": [
      ["1", "50", "I", "0", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"]
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

# ── POST: 텐던 배치 추출 ───────────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TendonArrangement",
        "TABLE_TYPE": "TNDN_ARRANGEMENT",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [50]}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonArrangement", {})
print(f"텐던 배치 {len(table.get('DATA', []))}행")
```

---

## 33. Tendon Loss

> **기능:** 텐던(Tendon)의 손실(Loss)을 요소·위치(Part)별로 추출합니다. 즉시 손실 후 응력, 탄성변형 손실, 크리프/건조수축 손실, 릴랙세이션 손실, 전체 손실 후/즉시 손실 후 응력비, 유효 개수를 포함합니다. 부재력(Force)/응력(Stress) 기준을 선택할 수 있습니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TNDN_LOSS_FORCE"` | 텐던 손실 (부재력 Force 기준) |
| `"TNDN_LOSS_STRESS"` | 텐던 손실 (응력 Stress 기준) |

### Response HEAD

`["Index", "Elem", "Part", "Stress(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Stress(AfterAllLoss)/Stress(AfterImmediateLoss)", "EffectiveNum."]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonLoss",
    "TABLE_TYPE": "TNDN_LOSS_STRESS",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "Stress(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Stress(AfterAllLoss)/Stress(AfterImmediateLoss)", "EffectiveNum."],
    "NODE_ELEMS": { "KEYS": [33] }
  }
}
```

**POST Response Body**

```json
{
  "TendonLoss": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Part", "Stress(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Stress(AfterAllLoss)/Stress(AfterImmediateLoss)", "EffectiveNum."],
    "DATA": [
      ["1", "33", "I", "1029.576204812610", "1.193871724644", "1.001159575871", "-68.776503747849", "-44.450510039386", "0.891185187130", "2.000000000000"]
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

# ── POST: 텐던 손실 추출 ───────────────────────────────────────────
#   부재력 기준: TABLE_TYPE="TNDN_LOSS_FORCE"
payload = {
    "Argument": {
        "TABLE_NAME": "TendonLoss",
        "TABLE_TYPE": "TNDN_LOSS_STRESS",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [33]}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonLoss", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} ({d['Part']}): 릴랙세이션손실={d['RelaxationLoss']}")
```

---

## 34. Tendon Weight

> **기능:** 텐던(Tendon)의 물량(Weight)을 그룹별/형상별/특성별로 추출합니다. 텐던 개수·단면적·길이·단위 길이당 중량·중량·총중량을 포함합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TNDN_WEIGHT_GROUP"` | 텐던 물량 (그룹별 Group) |
| `"TNDN_WEIGHT_PROFILE"` | 텐던 물량 (형상별 Profile) |
| `"TNDN_WEIGHT_PROPERTY"` | 텐던 물량 (특성별 Property) |

### Response HEAD

`["Index", "TendonName", "TendonNum", "Area", "Length", "Weight/Length", "Weight", "TotalWeight"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonWeight",
    "TABLE_TYPE": "TNDN_WEIGHT_GROUP",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonName", "TendonNum", "Area", "Length", "Weight/Length", "Weight", "TotalWeight"]
  }
}
```

**POST Response Body**

```json
{
  "TendonWeight": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonName", "TendonNum", "Area", "Length", "Weight/Length", "Weight", "TotalWeight"],
    "DATA": [
      ["1", "Bot-Key-A01", "1.000000000000", "0.002635300000", "21.048299083539", "0.202871198248", "4.270093656165", "4.270093656165"]
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

# ── POST: 텐던 물량 추출 ───────────────────────────────────────────
#   형상별: TABLE_TYPE="TNDN_WEIGHT_PROFILE"
#   특성별: TABLE_TYPE="TNDN_WEIGHT_PROPERTY"
payload = {
    "Argument": {
        "TABLE_NAME": "TendonWeight",
        "TABLE_TYPE": "TNDN_WEIGHT_GROUP",
        "UNIT": {"FORCE": "kN", "DIST": "m"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonWeight", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['TendonName']}: 총중량={d['TotalWeight']}")
```

---

## 35. Tendon Stress Limit Check

> **기능:** 텐던(Tendon)의 응력 한계 검토 결과를 추출합니다. 텐던 응력(f_p1·f_p2·f_pe)과 정착부/정착부 이격/사용상태 응력 한계를 비교합니다. `ADDITIONAL.REDUCTION_FACTOR`로 각 응력 한계에 곱할 감소계수를 직접 지정할 수 있습니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TNDN_STRS_LIMIT_CHECK"` | 텐던 응력 한계 검토 |

### Response HEAD

`["Index", "Tendon", "Tendon Stress/f_p1", "Tendon Stress/f_p2", "Tendon Stress/f_pe", "Tendon Stress Limit/Immediately after anchor set/At anch.", "Tendon Stress Limit/Immediately after anchor set/Away from anch.", "Tendon Stress Limit/At service"]`

### `ADDITIONAL.REDUCTION_FACTOR` (Optional)

정착 직후(anchor set) / 사용상태(service) 응력 한계에 곱하는 감소계수. 생략 시 기본값 사용.

| Key | 설명 | Value Type | Default |
|-----|------|-----------|---------|
| `"AT_ANCH"` | 정착부(anchorage) 응력 한계 감소계수 (post-tensioning 전용) | Number | 0.7 |
| `"AWAY_FROM_ANCH"` | 정착부 이격(away from anchorages) 응력 한계 감소계수 (post-tensioning 전용) | Number | 0.74 |
| `"AT_SERVICE"` | 사용상태(service) 응력 한계 감소계수 | Number | 0.8 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonStressLimitCheck",
    "TABLE_TYPE": "TNDN_STRS_LIMIT_CHECK",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Tendon", "TendonStress/f_p1", "TendonStress/f_p2", "TendonStress/f_pe", "TendonStressLimit/Atanch.", "TendonStressLimit/Awayfromanch.", "TendonStressLimit/Atservice"],
    "ADDITIONAL": {
      "REDUCTION_FACTOR": { "AT_ANCH": 1, "AWAY_FROM_ANCH": 1, "AT_SERVICE": 1 }
    }
  }
}
```

**POST Response Body**

```json
{
  "TendonStressLimitCheck": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Tendon", "Tendon Stress/f_p1", "Tendon Stress/f_p2", "Tendon Stress/f_pe", "Tendon Stress Limit/Immediately after anchor set/At anch.", "Tendon Stress Limit/Immediately after anchor set/Away from anch.", "Tendon Stress Limit/At service"],
    "DATA": [
      ["1", "A1L", "1094382.612985240063", "1209052.195195989916", "1037017.037908399943", "1900000.000000000000", "1900000.000000000000", "1600000.000000000000"]
    ]
  }
}
```

> ⚠️ 응답 루트 키가 `TendonStressLimit`에서 **`TendonStressLimitCheck`** 로 변경되었습니다(2026-07 공식 매뉴얼 갱신 반영).

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 텐던 응력 한계 검토 추출 ─────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TendonStressLimitCheck",
        "TABLE_TYPE": "TNDN_STRS_LIMIT_CHECK",
        "UNIT": {"FORCE": "kN", "DIST": "m"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonStressLimitCheck", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['Tendon']}: f_pe={d['Tendon Stress/f_pe']} / 한계(service)={d['Tendon Stress Limit/At service']}")
```

---

## 36. Tendon Approximate Loss

> **기능:** 텐던(Tendon)의 근사 손실(Approximate Loss)을 요소·위치(Part)별로 추출합니다. 즉시 손실, 크리프/건조수축/릴랙세이션 손실, 전체 손실과 즉시/전체 손실 후 응력 및 응력비를 포함합니다. 부재력(Force)/응력(Stress) 기준을 선택할 수 있습니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TNDN_APPROX_LOSS_FORCE"` | 텐던 근사 손실 (부재력 Force 기준) |
| `"TNDN_APPROX_LOSS_STRESS"` | 텐던 근사 손실 (응력 Stress 기준) |

### Response HEAD

`["Index", "Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Stress(ImmediateLoss)", "Stress(AllLoss)", "Stress(AllLoss)/Stress"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonApproxLoss",
    "TABLE_TYPE": "TNDN_APPROX_LOSS_STRESS",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Stress(ImmediateLoss)", "Stress(AllLoss)", "Stress(AllLoss)/Stress"],
    "NODE_ELEMS": { "KEYS": [1] }
  }
}
```

**POST Response Body**

```json
{
  "TendonApproxLoss": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Stress(ImmediateLoss)", "Stress(AllLoss)", "Stress(AllLoss)/Stress"],
    "DATA": [
      ["1", "1", "I", "-6.424509690435", "-8.904593184079", "-9.582009033589", "-2.465640773855", "-27.376752681958", "196.075490309565", "175.123247318042", "0.893141957934"]
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

# ── POST: 텐던 근사 손실 추출 ──────────────────────────────────────
#   부재력 기준: TABLE_TYPE="TNDN_APPROX_LOSS_FORCE"
payload = {
    "Argument": {
        "TABLE_NAME": "TendonApproxLoss",
        "TABLE_TYPE": "TNDN_APPROX_LOSS_STRESS",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonApproxLoss", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} ({d['Part']}): 전체손실={d['AllLoss']}")
```

---

## 37. Composite Section for C.S. (Force and Stress)

> **기능:** 시공단계 합성단면(Composite Section for Construction Stage)의 부재력/응력을 단면 파트(SectionPart)·부재 위치(Part)별로 추출합니다. 축력·모멘트-y·모멘트-z를 포함하며 부재력/응력 기준을 선택할 수 있습니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"COMPSECTBEAMFORCE"` | 시공단계 합성단면 부재력 (Beam Force) |
| `"COMPSECTBEAMSTRESS"` | 시공단계 합성단면 응력 (Beam Stress) |

### Response HEAD

`["Index", "Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "CompSectForce",
    "TABLE_TYPE": "COMPSECTBEAMFORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DL(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS1:001(first)"]
  }
}
```

**POST Response Body**

```json
{
  "CompSectForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1", "DL", "1", "I", "-0.000471429623", "-0.000083949590", "-0.077218286415"]
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

# ── POST: 시공단계 합성단면 부재력 추출 ────────────────────────────
#   응력 기준: TABLE_TYPE="COMPSECTBEAMSTRESS"
payload = {
    "Argument": {
        "TABLE_NAME": "CompSectForce",
        "TABLE_TYPE": "COMPSECTBEAMFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DL(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["CS1:001(first)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CompSectForce", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} 단면{d['SectionPart']}: Moment-z={d['Moment-z']}")
```

---

## 38. Composite Section for C.S. (Self-Constraint Force and Stress)

> **기능:** 시공단계 합성단면의 자기구속(Self-Constraint) 부재력/응력을 단면 파트(SectionPart)·부재 위치(Part)별로 추출합니다. 온도구배(TG) 등 자기평형 하중에 대한 축력·모멘트-y·모멘트-z를 포함하며 부재력/응력 기준을 선택할 수 있습니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"SELF_CONST_BEAM_FORCE"` | 합성단면 자기구속 부재력 (Self-Constraint Beam Force) |
| `"SELF_CONST_BEAM_STRESS"` | 합성단면 자기구속 응력 (Self-Constraint Beam Stress) |

### Response HEAD

`["Index", "Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SelfConstForce",
    "TABLE_TYPE": "SELF_CONST_BEAM_FORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["TG(+)(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS1:001(first)"]
  }
}
```

**POST Response Body**

```json
{
  "SelfConstForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1", "TG(+)", "1", "I", "326.337945299092", "-691.230653270694", "0.000000000000"]
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

# ── POST: 시공단계 합성단면 자기구속 부재력 추출 ───────────────────
#   응력 기준: TABLE_TYPE="SELF_CONST_BEAM_STRESS"
payload = {
    "Argument": {
        "TABLE_NAME": "SelfConstForce",
        "TABLE_TYPE": "SELF_CONST_BEAM_FORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["TG(+)(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["CS1:001(first)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SelfConstForce", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} 단면{d['SectionPart']}: Axial={d['Axial']}, Moment-y={d['Moment-y']}")
```

---

## 39. Wall Force

> **기능:** 벽체(Wall) 요소의 부재력/모멘트를 층(Story)·레벨(top/bot)별로 추출합니다. 일반 Plate Force와 달리 `STORY_NAMES`로 층을 지정할 수 있고, 응답에 상/하단(Part: `top`/`bot`) 값이 함께 제공됩니다.
>
> ℹ️ **2026-07-22 신규 반영:** 공식 매뉴얼에서 이번에 확인된 항목으로, 이전 버전 문서에는 누락되어 있었습니다.

### `TABLE_TYPE`

| 값 | 설명 |
| --- | --- |
| `"WALL_FORCE_MOMENT"` | 벽체 부재력/모멘트 (층·상하단별) |

### Response HEAD

`["Index", "Story", "Level", "Wall", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

> HEAD의 `Part`·`Axial`·... 열이 두 번 반복되는 것은 각각 상단(`top`)·하단(`bot`) 값을 의미합니다.

### 전용 파라미터

공통 파라미터(`TABLE_NAME`/`TABLE_TYPE`/`EXPORT_PATH`/`UNIT`/`STYLES`/`COMPONENTS`/`NODE_ELEMS`/`LOAD_CASE_NAMES`) 외에 아래 항목을 추가로 지원합니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 층 이름 지정 | `"STORY_NAMES"` | Array [String] | All | Optional |

> ℹ️ **2026-07-30 공식 확인:** 이전 버전 문서는 JSON Schema에만 등장하던 `SECT_POSITION`·`PARTS`를 추정 설명과 함께 실었으나, 공식 담당자 확인 결과 이 Table Type(`WALL_FORCE_MOMENT`)은 두 항목을 지원하지 않으며 공식 아티클에서도 제거되었습니다(Jira MAPI-2012). 이에 맞춰 위 표에서도 제거했습니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "WALL_FORCE_MOMENT",
    "TABLE_TYPE": "WALL_FORCE_MOMENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "NODE_ELEMS": { "KEYS": [1, 2, 3] },
    "LOAD_CASE_NAMES": ["gLCB6(CB)"],
    "STORY_NAMES": ["1F"],
    "COMPONENTS": ["Story", "Level", "Wall", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]
  }
}
```

**POST Response Body**

```json
{
  "WALL_FORCE_MOMENT": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Wall", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1F", "0.000", "1", "gLCB6", "top", "-8546.789", "0.000", "-57.818", "0.000", "114.403", "0.000", "bot", "-8750.140", "0.000", "-57.818", "0.000", "-174.688", "0.000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 벽체 부재력(층별) 추출 ───────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "WALL_FORCE_MOMENT",
        "TABLE_TYPE": "WALL_FORCE_MOMENT",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1, 2, 3]},
        "LOAD_CASE_NAMES": ["gLCB6(CB)"],
        "STORY_NAMES": ["1F"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("WALL_FORCE_MOMENT", {})

# 주의: 이 테이블은 HEAD에 Part·Axial·… 열이 top/bot 두 번 반복되므로
# 다른 절처럼 dict(zip(head, row))로 감싸면 bot 값이 top 값을 덮어씁니다.
# 위치 인덱스로 상·하단을 분리해서 읽습니다.
for row in table.get("DATA", []):
    story, wall, load = row[1], row[3], row[4]
    top = row[5:12]    # Part, Axial, Shear-y, Shear-z, Torsion, Moment-y, Moment-z
    bot = row[12:19]   # 동일 순서의 하단 값
    print(f"  Wall {wall} ({story}, {load}): Axial top={top[1]} / bot={bot[1]}")
```

---

## End-to-End Workflow

다음은 해석 실행 후 판 응력·솔리드 응력·링크 부재력·진동 모드형상·텐던 손실을 순차적으로 일괄 추출하는 워크플로우입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

def get_result(table_type, name, load_cases=None, extra=None):
    """해석 결과 테이블 추출 공통 함수"""
    arg = {
        "TABLE_NAME": name,
        "TABLE_TYPE": table_type,
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6}
    }
    if load_cases:
        arg["LOAD_CASE_NAMES"] = load_cases
    if extra:
        arg.update(extra)
    resp = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    return resp.json().get(name, {})

# ── STEP 1: 판 응력 (전역) ─────────────────────────────────────────
ps = get_result("PLATESTRESSG", "PlateStress", ["DL(ST)"],
                extra={"NODE_ELEMS": {"KEYS": [592]}})
print(f"STEP1 판 응력 {len(ps.get('DATA', []))}행")

# ── STEP 2: 솔리드 응력 (전역) ─────────────────────────────────────
ss = get_result("SOLIDSG", "SolidStress", ["DL(ST)"],
                extra={"NODE_ELEMS": {"KEYS": [3381]}})
print(f"STEP2 솔리드 응력 {len(ss.get('DATA', []))}행")

# ── STEP 3: 탄성 링크 부재력 ───────────────────────────────────────
lf = get_result("ELASTICLINK", "ElasticLink", ["SWofGirders(ST)"])
print(f"STEP3 링크 부재력 {len(lf.get('DATA', []))}행")

# ── STEP 4: 진동 모드형상 (하중케이스 불필요) ──────────────────────
vm = get_result("EIGENVALUEMODE", "VibMode",
                extra={"STYLES": {"FORMAT": "Scientific", "PLACE": 12},
                       "NODE_ELEMS": {"KEYS": [1]}})
print(f"STEP4 진동 모드형상 {len(vm.get('DATA', []))}행")

# ── STEP 5: 텐던 손실 (응력 기준) ──────────────────────────────────
tl = get_result("TNDN_LOSS_STRESS", "TendonLoss",
                extra={"NODE_ELEMS": {"KEYS": [33]}})
print(f"STEP5 텐던 손실 {len(tl.get('DATA', []))}행")
```
