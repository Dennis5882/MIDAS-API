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

> **참고:** `OPT_CS`·`STAGE_STEP`는 시공단계 결과 조회 시 사용합니다. 판/솔리드 변형률(비선형·시공단계), 텐던 신장량 등 `Step`·`Stage` 열을 포함하는 테이블에서 함께 지정합니다. `STAGE_STEP` 항목은 `"CS1:001(first)"`, `"CS1:002(last)"` 또는 `"nl_001"` 형식입니다. 단 텐던 계열 일부(30·31·33·34·36절), 동시절점력류(19장 13절 유사 패턴), 텐던 배치(32절)는 이 두 필드를 지원하지 않으니 해당 절의 전용 파라미터를 확인하세요.

> ⚠️ 2026-08-26 확인: 아래 두 파라미터는 이전 버전 문서에 전체가 누락되어 있었음 — 39개 테이블 중
> 다수(1~19, 22~25절)에서 공식 스키마에 존재하나, 테이블마다 적용 여부가 달라 공통 표에 넣지
> 않고 이 표로 정리합니다. 각 절에는 해당하는 것만 있으면 "전용 파라미터"로 별도 표기합니다.
>
> | 파라미터 | 설명 | Value 타입 | 기본값 | 적용 절(1~25절 기준) |
> |---|---|---|---|---|
> | `"AVERAGE_NODAL_RESULT"` | 절점 평균값 결과 옵션 | Boolean | `false` | 1,2,3,4,5,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25 |
> | `"NODE_FLAG"` (하위: `CENTER`/`NODES`, 둘 다 Boolean/`false`) | 요소 중심(Cent)/절점(Node)별 출력 여부 | Object | — | 3,4,5,6,7,10,11,14,15,18,19,22,23,24,25 |
>
> 20~21절(Solid Force Local/Global)은 원문에 두 파라미터 모두 없음을 확인(변경 없음).

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional — 절점 평균값 결과 옵션)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional — 절점 평균값 결과 옵션)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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
| `"PLATEFORCEULVBM"` | 단위 길이당 부재력 (국부, 최댓값 기준, View by Max Value) |
| `"PLATEFORCEUGVBM"` | 단위 길이당 부재력 (전역, 최댓값 기준, View by Max Value) |
| `"PLATEFORCEWA"` | 단위 길이당 부재력 (Wood-Armer 설계 모멘트) |

> ⚠️ 2026-08-26 확인 (article id `36012822385817`): 이 테이블은 `AVERAGE_NODAL_RESULT`/
> `NODE_FLAG`(공통 사항 참조)에 더해 `ULVBM`/`UGVBM` 전용 `"ITEM_TO_DISPLAY"`(Array [String],
> enum: `Fxx`/`Fyy`/`Fxy`/`Mxx`/`Myy`/`Mxy`/`Vxx`/`Vyy`, 기본값 All, Optional)를 지원합니다.
> 또한 이전 버전 문서는 `PLATEFORCEUL`/`UG`용 Response HEAD 하나만 표기해 `ULVBM`/`UGVBM`·`WA`도
> 같은 구조인 것으로 오인될 수 있었음 — 실제로는 아래처럼 3종류의 서로 다른 응답 구조를 가짐.

### Response HEAD

- `PLATEFORCEUL`/`PLATEFORCEUG`: `["Index", "Elem", "Load", "Node", "Fxx", "Fyy", "Fxy", "Fmax", "Fmin", "Angle", "Mxx", "Myy", "Mxy", "Mmax", "Mmin", "Angle", "Vxx", "Vyy"]`
- `PLATEFORCEULVBM`/`PLATEFORCEUGVBM`: `Node` 뒤에 `Component` 컬럼이 추가되고 `Fmax`/`Fmin`/`Mmax`/`Mmin`/`Angle`은 빠짐 — `["Index", "Elem", "Load", "Node", "Component", "Fxx", "Fyy", "Fxy", "Mxx", "Myy", "Mxy", "Vxx", "Vyy"]`
- `PLATEFORCEWA`(Wood-Armer): 완전히 다른 구조 — `Fxx`/`Fyy` 계열이 아예 없고, 4개 방향(Top Dir.1/Dir.2, Bot Dir.1/Dir.2)별 `Ma`/`Mb`/`Mab`/`W-AMoment` 블록이 반복 — `["Index", "Elem", "Load", "Node", "Ma", "Mb", "Mab", "W-AMomentTopDir.1", "Ma", "Mb", "Mab", "W-AMomentTopDir.2", "Ma", "Mb", "Mab", "W-AMomentBotDir.1", "Ma", "Mb", "Mab", "W-AMomentBotDir.2"]`

### Request / Response JSON

**POST Request Body — PLATEFORCEUL**

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

**POST Response Body — PLATEFORCEUL**

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

**POST Request Body — PLATEFORCEULVBM(View by Max Value)**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateForce(UL:L)ViewByMaxValue",
    "TABLE_TYPE": "PLATEFORCEULVBM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Component", "Fxx", "Fyy", "Fxy", "Mxx", "Myy", "Mxy", "Vxx", "Vyy"],
    "NODE_ELEMS": { "KEYS": [503] },
    "LOAD_CASE_NAMES": ["STLENV_STR(CB:max)", "STLENV_STR(CB:min)"],
    "AVERAGE_NODAL_RESULT": true,
    "NODE_FLAG": { "CENTER": false, "NODES": true },
    "ITEM_TO_DISPLAY": ["Fxx", "Fyy", "Fxy", "Mxx", "Myy", "Mxy", "Vxx", "Vyy"]
  }
}
```

**POST Response Body — PLATEFORCEULVBM(View by Max Value)**

```json
{
  "PlateForce(UL:L)ViewByMaxValue": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Component", "Fxx", "Fyy", "Fxy", "Mxx", "Myy", "Mxy", "Vxx", "Vyy"],
    "DATA": [
      ["1", "503", "STLENV_STR(max)", "52", "Fxx", "14.643051500000", "14.413288400000", "28.554175400000", "6.211062100000", "11.092328400000", "11.090774500000", "23.467790500000", "69.014747700000"],
      ["2", "503", "STLENV_STR(max)", "52", "Fyy", "14.643051500000", "14.413288400000", "28.554175400000", "6.211062100000", "11.092328400000", "11.090774500000", "23.467790500000", "69.014747700000"]
    ]
  }
}
```

**POST Request Body — PLATEFORCEWA(Wood-Armer)**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateForce(UnitLength:W-AMoment)",
    "TABLE_TYPE": "PLATEFORCEWA",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Ma", "Mb", "Mab", "W-AMomentTopDir.1", "Ma", "Mb", "Mab", "W-AMomentTopDir.2", "Ma", "Mb", "Mab", "W-AMomentBotDir.1", "Ma", "Mb", "Mab", "W-AMomentBotDir.2"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"],
    "AVERAGE_NODAL_RESULT": true,
    "NODE_FLAG": { "CENTER": false, "NODES": true }
  }
}
```

**POST Response Body — PLATEFORCEWA(Wood-Armer)**

```json
{
  "PlateForce(UnitLength:W-AMoment)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Ma", "Mb", "Mab", "W-AMomentTopDir.1", "Ma", "Mb", "Mab", "W-AMomentTopDir.2", "Ma", "Mb", "Mab", "W-AMomentBotDir.1", "Ma", "Mb", "Mab", "W-AMomentBotDir.2"],
    "DATA": [
      ["1", "592", "DL", "773", "1.744257540000", "0.141650776000", "0.000000000120", "0.054348959200", "1.744257540000", "0.141650776000", "0.000000000120", "0.105709883000", "1.744257540000", "0.141650776000", "0.000000000120", "1.788450260000", "1.744257540000", "0.141650776000", "0.000000000120", "0.237204424000"]
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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional — 요소중심(Cent)/절점별 출력 여부)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional — 요소중심(Cent)/절점별 출력 여부)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional — 절점 평균값 결과 옵션)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional — 절점 평균값 결과 옵션)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStressLocal",
    "TABLE_TYPE": "PLANESTRESSSL",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

> ⚠️ 2026-08-26 확인: `COMPONENTS`에 `"Angle"`이 누락되어 있었고(HEAD에는 이미 있었음), `UNIT`이
> `kN`/`m`로 잘못 표기되어 있었음(DATA 값 자체는 원문 예제의 N/mm 값과 동일해 단위 표기만 불일치
> — N/mm로 정정).

**POST Response Body**

```json
{
  "PlaneStressLocal": {
    "FORCE": "N",
    "DIST": "mm",
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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStressGlobal",
    "TABLE_TYPE": "PLANESTRESSSG",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

> ⚠️ 2026-08-26 확인: `COMPONENTS`에 `"Angle"`이 누락되어 있었고, `UNIT`이 `kN`/`m`로 잘못
> 표기되어 있었음(값은 원문 N/mm 예제와 동일 — 10절과 동일 패턴).

**POST Response Body**

```json
{
  "PlaneStressGlobal": {
    "FORCE": "N",
    "DIST": "mm",
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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional — 절점 평균값 결과 옵션)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional — 절점 평균값 결과 옵션)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainStressLocal",
    "TABLE_TYPE": "PLANESTRAINSL",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

> ⚠️ 2026-08-26 확인: `UNIT`이 `kN`/`m`로 잘못 표기되어 있었음(값은 원문 N/mm 예제와 동일).

**POST Response Body**

```json
{
  "PlaneStrainStressLocal": {
    "FORCE": "N",
    "DIST": "mm",
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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainStressGlobal",
    "TABLE_TYPE": "PLANESTRAINSG",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

> ⚠️ 2026-08-26 확인: `UNIT`이 `kN`/`m`로 잘못 표기되어 있었음(값은 원문 N/mm 예제와 동일).

**POST Response Body**

```json
{
  "PlaneStrainStressGlobal": {
    "FORCE": "N",
    "DIST": "mm",
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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional — 절점 평균값 결과 옵션)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional — 절점 평균값 결과 옵션)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional — 요소중심(Cent)/절점별 출력 여부)를 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

### Response HEAD

- `SOLID_LOCA_TOTAL_STRAIN`: `["Index", "Elem", "Load", "Step", "Node", "Strain-xx", "Strain-yy", "Strain-zz", "Strain-xy", "Strain-yz", "Strain-xz", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"]`
- `SOLID_LOCA_PLAST_STRAIN`: 위 컬럼 뒤에 `Comp.Damage`/`Tens.Damage`/`Damage` 3개 컬럼이 추가됩니다.

> ⚠️ 2026-08-26 확인: `SOLID_LOCA_PLAST_STRAIN` 전용 컬럼 3개(`Comp.Damage`/`Tens.Damage`/
> `Damage`)가 이전 버전 문서에 누락되어 있었음(단일 HEAD로 표기해 소성/전체 변형률이 동일 구조인
> 것처럼 오인될 소지).

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

> ⚠️ 2026-08-26 확인: 이 테이블은 `"AVERAGE_NODAL_RESULT"`(Boolean, 기본값 `false`, Optional)와 `"NODE_FLAG"`(Object: `CENTER`/`NODES`, 둘 다 Boolean·기본값 `false`, Optional) 모두 지원합니다(공통 사항의 적용 절 표 참조). 이전 버전 문서에 누락되어 있었음.

### Response HEAD

- `SOLID_GLOB_TOTAL_STRAIN`: `["Index", "Elem", "Load", "Step", "Node", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"]`
- `SOLID_GLOB_PLAST_STRAIN`: 위 컬럼 뒤에 `Comp.Damage`/`Tens.Damage`/`Damage` 3개 컬럼이 추가됩니다.

> ⚠️ 2026-08-26 확인: `SOLID_GLOB_PLAST_STRAIN` 전용 컬럼 3개(`Comp.Damage`/`Tens.Damage`/
> `Damage`)가 이전 버전 문서에 누락되어 있었음(24절과 동일 패턴).

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
| `"ELASTICLINKVBM"` | 탄성 링크 부재력 (최댓값 기준, View by Max Value) |

> ⚠️ 2026-08-26 확인 (article id `36017416195737`): `ELASTICLINKVBM` 전용 파라미터
> `"ITEM_TO_DISPLAY"`(Array [String], enum: `Axial`/`Shear-y`/`Shear-z`/`Torsion`/`Moment-y`/
> `Moment-z`, 기본값 All, Optional)가 이전 버전 문서에 누락되어 있었음 — 최댓값을 계산할 대상
> 성분을 지정하는 필드.

### Response HEAD

- `ELASTICLINK`: `["Index", "No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`
- `ELASTICLINKVBM`: `Node` 뒤에 어느 성분이 최댓값을 낸 것인지 나타내는 `Component` 컬럼이 추가됨 — `["Index", "No.", "Load", "Node", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

### Request / Response JSON

**POST Request Body — ELASTICLINK**

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

**POST Response Body — ELASTICLINK**

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

**POST Request Body — ELASTICLINKVBM(View by Max Value)**

```json
{
  "Argument": {
    "TABLE_NAME": "ElasticLinkViewByMaxValueItems",
    "TABLE_TYPE": "ELASTICLINKVBM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["STLENV_STR(CB:max)", "STLENV_STR(CB:min)"],
    "ITEM_TO_DISPLAY": ["Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]
  }
}
```

**POST Response Body — ELASTICLINKVBM(View by Max Value)**

```json
{
  "ElasticLinkViewByMaxValueItems": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "No.", "Load", "Node", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1", "STLENV_STR(max)", "1", "Axial", "8.761203247070", "16.289886962891", "45.691238769531", "0.000035891681", "8.390747558594", "6.234448486328"],
      ["2", "1", "STLENV_STR(max)", "1", "Shear-y", "8.761203247070", "16.289886962891", "45.691238769531", "0.000035891681", "8.390747558594", "6.234448486328"]
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
| `"GENERAL_LINK_FORCEVBM"` | 일반 링크 부재력 (최댓값 기준, View by Max Value) |
| `"GENERAL_LINK_DEFORM"` | 일반 링크 변형 (Deform) |

> ⚠️ 2026-08-26 확인 (article id `36017500761369`): `GENERAL_LINK_FORCEVBM` 전용 파라미터
> `"ITEM_TO_DISPLAY"`(Array [String], enum: `Axial`/`Shear-y`/`Shear-z`/`Torsion`/`Moment-y`/
> `Moment-z`, 기본값 All, Optional)가 이전 버전 문서에 누락되어 있었음(26절 Elastic Link와 동일
> 패턴). 또한 `GENERAL_LINK_DEFORM`은 부재력과 전혀 다른 응답 구조(양단 변위/회전)를 가지는데
> 이전 버전 문서는 부재력용 Response HEAD 하나만 표기해 DEFORM도 같은 구조로 오인할 수 있었음.

### Response HEAD

- `GENERAL_LINK_FORCE`: `["Index", "No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`
- `GENERAL_LINK_FORCEVBM`: `Node` 뒤에 `Component` 컬럼 추가 — `["Index", "No.", "Load", "Node", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`
- `GENERAL_LINK_DEFORM`: 완전히 다른 구조 — 링크 양단의 변위(Dx/Dy/Dz)·회전(Rx/Ry/Rz)이 `Node` 블록별로 반복 — `["Index", "No.", "Load", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"]`

### Request / Response JSON

**POST Request Body — GENERAL_LINK_FORCE**

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

**POST Response Body — GENERAL_LINK_FORCE**

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

**POST Request Body — GENERAL_LINK_FORCEVBM(View by Max Value)**

```json
{
  "Argument": {
    "TABLE_NAME": "GeneralLink-Force-ViewByMaxValueItems",
    "TABLE_TYPE": "GENERAL_LINK_FORCEVBM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "NODE_ELEMS": { "KEYS": [2] },
    "LOAD_CASE_NAMES": ["STLENV_STR(CB:max)", "STLENV_STR(CB:min)"],
    "ITEM_TO_DISPLAY": ["Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]
  }
}
```

**POST Request Body — GENERAL_LINK_DEFORM**

```json
{
  "Argument": {
    "TABLE_NAME": "GeneralLink-Deformation",
    "TABLE_TYPE": "GENERAL_LINK_DEFORM",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["No.", "Load", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["SWofGirders(ST)"]
  }
}
```

**POST Response Body — GENERAL_LINK_DEFORM**

```json
{
  "GeneralLink-Deformation": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "No.", "Load", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "DATA": [
      ["1", "1", "SWofGirders", "3536", "-2.537631746597e-05", "1.256078938754e-04", "-1.455055139484e-01", "-4.829228297583e-07", "1.587459476372e-04", "-1.964780569004e-05", "1236", "-2.537631746597e-05", "1.256078938754e-04", "-1.455055139484e-01", "-4.829228297583e-07", "1.587459476372e-04", "-1.964780569004e-05"]
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

### 전용 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 8 | 모드 번호 목록 (`"Mode" + 번호`, 예: `"Mode1"`) | `"MODES"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 확인 (article id `36017669319321`): `MODES` 파라미터와 응답의 `SUB_TABLES`
> 배열(모드해석 요약 정보) 모두 이전 버전 문서에 누락되어 있었음.

### Response HEAD

메인 `HEAD`/`DATA`: `["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"]`

이와 별도로, 응답 최상위에 모드해석 요약 정보를 담은 `SUB_TABLES` 배열이 추가되며, 아래 4종
하위 테이블을 포함합니다(각 `HEAD`/`DATA`는 모드 번호별 1행):

| 하위 테이블 키 | 내용 | HEAD |
|---|---|---|
| `EIGENVALUEANALYSIS` | 고유진동수·주기 | `["ModeNo", "Frequency(rad/sec)", "Frequency(cycle/sec)", "Period(sec)", "Tolerance"]` |
| `MODALPARTICIPATIONMASSESPRINTOUT(1)` | 모달 참여질량(%, 누적%) | `["ModeNo", "TRAN-XMASS(%)", "TRAN-XSUM(%)", "TRAN-YMASS(%)", "TRAN-YSUM(%)", "TRAN-ZMASS(%)", "TRAN-ZSUM(%)", "ROTN-XMASS(%)", "ROTN-XSUM(%)", "ROTN-YMASS(%)", "ROTN-YSUM(%)", "ROTN-ZMASS(%)", "ROTN-ZSUM(%)"]` |
| `MODALPARTICIPATIONMASSESPRINTOUT(2)` | 모달 참여질량(절대값, 누적값) | 위와 동일 컬럼명에서 `(%)` 제거 |
| `MODALPARTICIPATIONFACTORPRINTOUT(kN,m)` | 모달 참여계수 | `["ModeNo", "TRAN-XValue", "TRAN-YValue", "TRAN-ZValue", "ROTN-XValue", "ROTN-YValue", "ROTN-ZValue"]` |
| `MODALDIRECTIONFACTORPRINTOUT` | 모달 방향계수 | 위와 동일 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "EigenvalueMode",
    "TABLE_TYPE": "EIGENVALUEMODE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "MODES": ["Mode1", "Mode2"]
  }
}
```

**POST Response Body**

```json
{
  "EigenvalueMode": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "1", "1", "3.837572718516e-02", "-2.976241858587e-07", "0.000000000000e+00", "2.380992695526e-07", "4.126895212051e-06", "-5.142371718861e-07"],
      ["2", "1", "2", "4.396886676826e-05", "7.802487500606e-04", "3.449011941636e-10", "-6.241987277788e-04", "-5.791213526283e-04", "1.761254899933e-03"]
    ],
    "SUB_TABLES": [
      {
        "EIGENVALUEANALYSIS": {
          "HEAD": ["ModeNo", "Frequency(rad/sec)", "Frequency(cycle/sec)", "Period(sec)", "Tolerance"],
          "DATA": [
            ["1.0000", "9.1608", "1.4580", "0.6859", "0.0000e+00"],
            ["2.0000", "9.8717", "1.5711", "0.6365", "0.0000e+00"]
          ]
        }
      },
      {
        "MODALPARTICIPATIONMASSESPRINTOUT(1)": {
          "HEAD": ["ModeNo", "TRAN-XMASS(%)", "TRAN-XSUM(%)", "TRAN-YMASS(%)", "TRAN-YSUM(%)", "TRAN-ZMASS(%)", "TRAN-ZSUM(%)", "ROTN-XMASS(%)", "ROTN-XSUM(%)", "ROTN-YMASS(%)", "ROTN-YSUM(%)", "ROTN-ZMASS(%)", "ROTN-ZSUM(%)"],
          "DATA": [
            ["1.0000", "91.64", "91.64", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "0.01", "0.01", "0.00", "0.00"]
          ]
        }
      },
      {
        "MODALPARTICIPATIONMASSESPRINTOUT(2)": {
          "HEAD": ["ModeNo", "TRAN-XMASS", "TRAN-XSUM", "TRAN-YMASS", "TRAN-YSUM", "TRAN-ZMASS", "TRAN-ZSUM", "ROTN-XMASS", "ROTN-XSUM", "ROTN-YMASS", "ROTN-YSUM", "ROTN-ZMASS", "ROTN-ZSUM"],
          "DATA": [
            ["1.0000", "724.1700", "724.1700", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "148.1200", "148.1200", "0.00", "0.00"]
          ]
        }
      },
      {
        "MODALPARTICIPATIONFACTORPRINTOUT(kN,m)": {
          "HEAD": ["ModeNo", "TRAN-XValue", "TRAN-YValue", "TRAN-ZValue", "ROTN-XValue", "ROTN-YValue", "ROTN-ZValue"],
          "DATA": [
            ["1.0000", "26.91", "-0.01", "0.06", "0.00", "0.18", "0.00"]
          ]
        }
      },
      {
        "MODALDIRECTIONFACTORPRINTOUT": {
          "HEAD": ["ModeNo", "TRAN-XValue", "TRAN-YValue", "TRAN-ZValue", "ROTN-XValue", "ROTN-YValue", "ROTN-ZValue"],
          "DATA": [
            ["1.0000", "99.98", "0.00", "0.00", "0.00", "0.01", "0.00"]
          ]
        }
      }
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

### 전용 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 8 | 모드 번호 목록 (`"Mode" + 번호`, 예: `"Mode1"`) | `"MODES"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 확인 (article id `36017712087065`): `MODES` 파라미터와 응답의 `SUB_TABLES`
> (`BUCKLINGANALYSIS` — 모드별 좌굴계수(Eigenvalue)·Tolerance)가 이전 버전 문서에 누락되어
> 있었음(28절 Vibration Mode Shape와 동일 패턴).

### Response HEAD

메인 `HEAD`/`DATA`: `["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"]`

이와 별도로 응답 최상위에 `SUB_TABLES` 배열이 추가되며, `BUCKLINGANALYSIS` 하위 테이블
(`HEAD`: `["Mode", "Eigenvalue", "Tolerance"]`, 모드 번호별 1행)을 포함합니다.

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
    "NODE_ELEMS": { "KEYS": [1] },
    "MODES": ["Mode1", "Mode2"]
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
      ["1", "1", "1", "-3.068406433733e-05", "1.071752325513e-10", "-2.756625224655e-08", "0.000000000000e+00", "2.040060468720e-08", "1.430189905494e-10"],
      ["2", "1", "2", "8.776101828229e-08", "0.000000000000e+00", "-1.232408164286e-08", "0.000000000000e+00", "4.962889338148e-08", "0.000000000000e+00"]
    ],
    "SUB_TABLES": [
      {
        "BUCKLINGANALYSIS": {
          "HEAD": ["Mode", "Eigenvalue", "Tolerance"],
          "DATA": [
            ["1", "2.909991059676e+03", "0.0000e+00"],
            ["2", "3.056712238985e+03", "0.0000e+00"]
          ]
        }
      }
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

### ADDITIONAL — 텐던 그룹·시공단계 지정 (2026-08-26 공식 반영)

이 테이블은 공통 사항의 `NODE_ELEMS`를 사용하지 **않으며**, 대신 아래 `ADDITIONAL` 객체로
텐던 그룹과 시공단계를 지정합니다(둘 다 Required).

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 7 | 텐던 그룹·시공단계 지정 | `"ADDITIONAL"` | Object | — | **Required** |
| 7-1 | └ 텐던 그룹·시공단계 설정 | `ADDITIONAL.SET_TENDON_PARAMS` | Object | — | **Required** |
| 7-1-1 | 　└ 텐던 그룹 이름 | `SET_TENDON_PARAMS.TENDON_GROUP` | String | — | **Required** |
| 7-1-2 | 　└ 시공단계 이름 | `SET_TENDON_PARAMS.STAGE` | String | — | **Required** |

> ⚠️ 2026-08-26 확인 (article id `36018062664857`): 이전 버전 문서는 이 테이블도 공통
> `NODE_ELEMS`(요소 지정)를 쓰는 것으로 오기하고 있었으나, 공식 스키마에는 `NODE_ELEMS`가 아예
> 없고 `ADDITIONAL.SET_TENDON_PARAMS`(텐던 그룹명 + 시공단계명, 둘 다 Required)로 대상을
> 지정합니다 — 이전 예제로는 실제 데이터를 선택할 수 없었음.

### Response HEAD

`["Index", "Elem", "Part", "TendonNumber", "Yp", "Zp", "AverageSinθ", "AverageCosθ", "AverageStress", "AverageForce"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonArrangement(TendonGroup)",
    "TABLE_TYPE": "TNDN_ARRANGEMENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "TendonNumber", "Yp", "Zp", "AverageSinθ", "AverageCosθ", "AverageStress", "AverageForce"],
    "ADDITIONAL": {
      "SET_TENDON_PARAMS": {
        "TENDON_GROUP": "Top-P2-A",
        "STAGE": "CS2"
      }
    }
  }
}
```

**POST Response Body**

```json
{
  "TendonArrangement(TendonGroup)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Part", "TendonNumber", "Yp", "Zp", "AverageSinθ", "AverageCosθ", "AverageStress", "AverageForce"],
    "DATA": [
      ["1", "50", "I", "0", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"],
      ["2", "50", "J", "0", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"]
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

# ── POST: 텐던 배치 추출 (텐던그룹 + 시공단계 지정) ────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TendonArrangement(TendonGroup)",
        "TABLE_TYPE": "TNDN_ARRANGEMENT",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "ADDITIONAL": {
            "SET_TENDON_PARAMS": {"TENDON_GROUP": "Top-P2-A", "STAGE": "CS2"}
        }
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonArrangement(TendonGroup)", {})
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

### ADDITIONAL — 텐던 그룹·시공단계 지정 (2026-08-26 공식 반영)

이 테이블은 공통 사항의 `NODE_ELEMS`/`LOAD_CASE_NAMES`/`OPT_CS`/`STAGE_STEP`를 지원하지 **않고**,
대신 32절(Tendon Arrangement)과 동일한 `ADDITIONAL.SET_TENDON_PARAMS`(텐던 그룹명 + 시공단계명,
둘 다 Required)로 대상을 지정합니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 7 | 텐던 그룹·시공단계 지정 | `"ADDITIONAL"` | Object | — | **Required** |
| 7-1 | └ 텐던 그룹·시공단계 설정 | `ADDITIONAL.SET_TENDON_PARAMS` | Object | — | **Required** |
| 7-1-1 | 　└ 텐던 그룹 이름 | `SET_TENDON_PARAMS.TENDON_GROUP` | String | — | **Required** |
| 7-1-2 | 　└ 시공단계 이름 | `SET_TENDON_PARAMS.STAGE` | String | — | **Required** |

> ⚠️ 2026-08-26 확인 (article id `36018150905881`): 이전 버전 문서는 `NODE_ELEMS`로 대상을
> 지정했으나 공식 스키마에는 없는 필드이며, 실제로는 `ADDITIONAL.SET_TENDON_PARAMS`가 필요함.

### Response HEAD

- `TNDN_LOSS_STRESS`: `["Index", "Elem", "Part", "Stress(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Stress(AfterAllLoss)/Stress(AfterImmediateLoss)", "EffectiveNum."]`
- `TNDN_LOSS_FORCE`: `Stress(...)` 대신 `Force(...)` 컬럼명 사용 — `["Index", "Elem", "Part", "Force(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Force(AfterAllLoss)/Force(AfterImmediateLoss)", "EffectiveNum."]`

### Request / Response JSON

**POST Request Body — TNDN_LOSS_STRESS**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonLoss(Stress)",
    "TABLE_TYPE": "TNDN_LOSS_STRESS",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "Stress(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Stress(AfterAllLoss)/Stress(AfterImmediateLoss)", "EffectiveNum."],
    "ADDITIONAL": {
      "SET_TENDON_PARAMS": { "TENDON_GROUP": "Bot-Key-B", "STAGE": "CS16" }
    }
  }
}
```

**POST Response Body — TNDN_LOSS_STRESS**

```json
{
  "TendonLoss(Stress)": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Part", "Stress(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Stress(AfterAllLoss)/Stress(AfterImmediateLoss)", "EffectiveNum."],
    "DATA": [
      ["1", "33", "I", "1029.576204812610", "1.193871724644", "1.001159575871", "-68.776503747849", "-44.450510039386", "0.891185187130", "2.000000000000"],
      ["2", "33", "J", "1135.213914944730", "0.738061054845", "1.000650151522", "-64.974951541191", "-49.011270158760", "0.900240686663", "2.000000000000"]
    ]
  }
}
```

**POST Request Body — TNDN_LOSS_FORCE**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonLoss(Force)",
    "TABLE_TYPE": "TNDN_LOSS_FORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "Force(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Force(AfterAllLoss)/Force(AfterImmediateLoss)", "EffectiveNum."],
    "ADDITIONAL": {
      "SET_TENDON_PARAMS": { "TENDON_GROUP": "Bot-Key-B", "STAGE": "CS16" }
    }
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

# ── POST: 텐던 손실 추출 (응력 기준) ───────────────────────────────
#   부재력 기준: TABLE_TYPE="TNDN_LOSS_FORCE"
payload = {
    "Argument": {
        "TABLE_NAME": "TendonLoss(Stress)",
        "TABLE_TYPE": "TNDN_LOSS_STRESS",
        "UNIT": {"FORCE": "N", "DIST": "mm"},
        "ADDITIONAL": {
            "SET_TENDON_PARAMS": {"TENDON_GROUP": "Bot-Key-B", "STAGE": "CS16"}
        }
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonLoss(Stress)", {})
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
| `"TNDN_WEIGHT_PROFILE"` | 텐던 물량 (형상별 Profile) |
| `"TNDN_WEIGHT_PROPERTY"` | 텐던 물량 (특성별 Property) |
| `"TNDN_WEIGHT_GROUP"` | 텐던 물량 (그룹별 Group) |

> ⚠️ 2026-08-26 확인 (article id `36018235852569`): 이전 버전 문서는 `TABLE_TYPE`을
> `"TNDN_WEIGHT_GROUP"`으로 표기하면서도 예제 자체는 실제로 `"TNDN_WEIGHT_PROFILE"`(형상별)
> 응답 데이터(`TendonName`/`TendonNum` 컬럼, `"Bot-Key-A01"` 등)를 그대로 사용하고 있었음 —
> Group 응답은 컬럼 구성이 전혀 다름. 3종 모두 응답 구조가 달라 아래에 각각 정정·추가함.

### Response HEAD

- `TNDN_WEIGHT_PROFILE`: `["Index", "TendonName", "TendonNum", "Area", "Length", "Weight/Length", "Weight", "TotalWeight"]`
- `TNDN_WEIGHT_PROPERTY`: `["Index", "TendonProperty", "Area", "TotalLength", "Weight/Length", "TotalWeight"]`
- `TNDN_WEIGHT_GROUP`: `["Index", "TendonGroup", "TotalLength", "TotalWeight"]`

### Request / Response JSON

**POST Request Body — TNDN_WEIGHT_PROFILE**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonProfile",
    "TABLE_TYPE": "TNDN_WEIGHT_PROFILE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonName", "TendonNum", "Area", "Length", "Weight/Length", "Weight", "TotalWeight"]
  }
}
```

**POST Response Body — TNDN_WEIGHT_PROFILE**

```json
{
  "TendonProfile": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonName", "TendonNum", "Area", "Length", "Weight/Length", "Weight", "TotalWeight"],
    "DATA": [
      ["1", "Bot-Key-A01", "1.000000000000", "0.002635300000", "21.048299083539", "0.202871198248", "4.270093656165", "4.270093656165"],
      ["2", "Bot-Key-A02", "1.000000000000", "0.002635300000", "21.035730337216", "0.202871198248", "4.267543819538", "4.267543819538"]
    ]
  }
}
```

**POST Request Body — TNDN_WEIGHT_PROPERTY**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonProperty",
    "TABLE_TYPE": "TNDN_WEIGHT_PROPERTY",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonProperty", "Area", "TotalLength", "Weight/Length", "TotalWeight"]
  }
}
```

**POST Response Body — TNDN_WEIGHT_PROPERTY**

```json
{
  "TendonProperty": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonProperty", "Area", "TotalLength", "Weight/Length", "TotalWeight"],
    "DATA": [
      ["1", "Bot", "0.002635300000", "2073.687453151790", "0.202871198248", "420.691458413265"],
      ["2", "Top", "0.002635300000", "5553.015935350260", "0.202871198248", "1126.546996696130"],
      ["3", "SUM", "-", "7626.703388502000", "-", "1547.238455109000"]
    ]
  }
}
```

**POST Request Body — TNDN_WEIGHT_GROUP**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonGroup",
    "TABLE_TYPE": "TNDN_WEIGHT_GROUP",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonGroup", "TotalLength", "TotalWeight"]
  }
}
```

**POST Response Body — TNDN_WEIGHT_GROUP**

```json
{
  "TendonGroup": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonGroup", "TotalLength", "TotalWeight"],
    "DATA": [
      ["1", "Bot-Key-A", "446.379820137516", "90.557608985136"]
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

# ── POST: 텐던 물량 추출 (형상별) ──────────────────────────────────
#   특성별: TABLE_TYPE="TNDN_WEIGHT_PROPERTY"
#   그룹별: TABLE_TYPE="TNDN_WEIGHT_GROUP"
payload = {
    "Argument": {
        "TABLE_NAME": "TendonProfile",
        "TABLE_TYPE": "TNDN_WEIGHT_PROFILE",
        "UNIT": {"FORCE": "kN", "DIST": "m"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonProfile", {})
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

> ⚠️ 2026-08-26 확인 (article id `36018411935129`): 이 테이블은 공통 사항의 `NODE_ELEMS`를
> 지원하지 **않습니다**(공식 스키마에 `TABLE_NAME`/`TABLE_TYPE`/`EXPORT_PATH`/`UNIT`/`STYLES`/
> `COMPONENTS`만 존재) — 이전 버전 문서에 잘못 포함되어 있었음. 대상 제한 없이 전체 텐던 요소가
> 반환됩니다.

### Response HEAD

- `TNDN_APPROX_LOSS_STRESS`: `["Index", "Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Stress(ImmediateLoss)", "Stress(AllLoss)", "Stress(AllLoss)/Stress"]`
- `TNDN_APPROX_LOSS_FORCE`: `Stress(...)` 대신 `Force(...)` 컬럼명 사용 — `["Index", "Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Force(ImmediateLoss)", "Force(AllLoss)", "Force(AllLoss)/Force"]`

### Request / Response JSON

**POST Request Body — TNDN_APPROX_LOSS_STRESS**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonApproximateLoss(Stress)",
    "TABLE_TYPE": "TNDN_APPROX_LOSS_STRESS",
    "UNIT": { "FORCE": "kips", "DIST": "in" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Stress(ImmediateLoss)", "Stress(AllLoss)", "Stress(AllLoss)/Stress"]
  }
}
```

**POST Response Body — TNDN_APPROX_LOSS_STRESS**

```json
{
  "TendonApproximateLoss(Stress)": {
    "FORCE": "kips",
    "DIST": "in",
    "HEAD": ["Index", "Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Stress(ImmediateLoss)", "Stress(AllLoss)", "Stress(AllLoss)/Stress"],
    "DATA": [
      ["1", "1", "I", "-6.424509690435", "-8.904593184079", "-9.582009033589", "-2.465640773855", "-27.376752681958", "196.075490309565", "175.123247318042", "0.893141957934"]
    ]
  }
}
```

**POST Request Body — TNDN_APPROX_LOSS_FORCE**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonApproximateLoss(Force)",
    "TABLE_TYPE": "TNDN_APPROX_LOSS_FORCE",
    "UNIT": { "FORCE": "kips", "DIST": "in" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Force(ImmediateLoss)", "Force(AllLoss)", "Force(AllLoss)/Force"]
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

# ── POST: 텐던 근사 손실 추출 (응력 기준) ──────────────────────────
#   부재력 기준: TABLE_TYPE="TNDN_APPROX_LOSS_FORCE"
payload = {
    "Argument": {
        "TABLE_NAME": "TendonApproximateLoss(Stress)",
        "TABLE_TYPE": "TNDN_APPROX_LOSS_STRESS",
        "UNIT": {"FORCE": "kips", "DIST": "in"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonApproximateLoss(Stress)", {})
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

> ⚠️ 2026-08-26 확인 (article id `36018521410457`): 이 테이블은 부재 위치 지정 파라미터
> `"PARTS"`(Array [String], 값: `"PartI"`/`"Part1/4"`/`"Part2/4"`/`"Part3/4"`/`"PartJ"`, 기본값
> All, Optional — 19장 8~12절의 PARTS와 동일 패턴)를 지원합니다. 이전 버전 문서에 누락되어
> 있었음.

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
    "STAGE_STEP": ["CS1:001(first)"],
    "PARTS": ["PartI", "PartJ"]
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

> ⚠️ 2026-08-26 확인 (article id `36018582743705`): 이 테이블은 부재 위치 지정 파라미터
> `"PARTS"`(Array [String], 값: `"PartI"`/`"Part1/4"`/`"Part2/4"`/`"Part3/4"`/`"PartJ"`, 기본값
> All, Optional)를 지원합니다(37절과 동일). 이전 버전 문서에 누락되어 있었음.

### Response HEAD

- General/Post CS: `["Index", "Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"]`
- 시공단계(Construction Stage, `COMPONENTS`에 `Stage`/`Step`을 포함할 때): `Load` 뒤에 `Stage`/`Step`이 추가됨 — `["Index", "Elem", "Load", "Stage", "Step", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"]`

> ⚠️ 2026-08-26 확인: 시공단계 조회 시 `Stage`/`Step` 컬럼이 추가되는 점이 이전 버전 문서에
> 누락되어 있었음(37절의 공식 예제는 이 컬럼을 포함하지 않아 37절 자체는 정정하지 않음 — 원문
> 아티클 간 표기 차이로 판단, 오류제보 대상).

### Request / Response JSON

**POST Request Body — General/Post CS**

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
    "PARTS": ["PartI", "PartJ"]
  }
}
```

**POST Response Body — General/Post CS**

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

**POST Request Body — 시공단계(Construction Stage)**

```json
{
  "Argument": {
    "TABLE_NAME": "Self-ConstraintBeamForce",
    "TABLE_TYPE": "SELF_CONST_BEAM_FORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Stage", "Step", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "PARTS": ["PartI", "PartJ"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS4:001(first)", "CS4:002(last)"]
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
