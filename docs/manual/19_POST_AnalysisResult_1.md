# 19. POST – Analysis Result Tables (Part 1)

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

이 파트는 해석 결과 테이블 중 **반력·변위·트러스·케이블·보·동시 절점력(Concurrent Joint Force)** 결과를 다룹니다. 모든 엔드포인트는 **공통 URI `{base url}/post/TABLE`** 를 사용하며 `POST` 메서드만 지원합니다. 요청 바디의 `"Argument"` 객체에서 `TABLE_TYPE` 값으로 테이블 종류를 결정합니다.

---

## 공통 사항

### Input URI (해석 결과 테이블 공통)

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 공통 Request 구조 및 파라미터

전처리 테이블(18장)보다 확장된 구조로, `UNIT`·`STYLES`·`COMPONENTS`·`NODE_ELEMS`·`LOAD_CASE_NAMES`·`OPT_CS`·`STAGE_STEP`를 지원합니다. **아래 파라미터 표는 13개 테이블 전체에 공통 적용**되며, 각 절에서는 `TABLE_TYPE` enum과 응답 `HEAD` 열, 대표 예시만 별도 기술합니다.

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

> **참고:** `OPT_CS`·`STAGE_STEP`는 시공단계 결과 조회 시 사용합니다(Reaction의 Local–Surface
> Spring 변형, Beam Force (Static Prestress), Concurrent Joint Force는 이 두 필드를 지원하지
> 않음 — 각 절 참조). `STAGE_STEP` 항목은 `"CS1:001(first)"`, `"CS1:002(last)"` 형식입니다.

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
| 1 | [Reaction](#1-reaction) | `REACTIONG` / `REACTIONL` / `REACTIONSURFACESPRING` |
| 2 | [Displacements](#2-displacements) | `DISPLACEMENTG` / `DISPLACEMENTL` |
| 3 | [Truss Force](#3-truss-force) | `TRUSSFORCE` |
| 4 | [Truss Stress](#4-truss-stress) | `TRUSSSTRESS` |
| 5 | [Cable Force](#5-cable-force) | `CABLEFORCE` |
| 6 | [Cable Configuration](#6-cable-configuration) | `CABLECONFIG` |
| 7 | [Cable Efficiency](#7-cable-efficiency) | `CABLEEFFIENCY` |
| 8 | [Beam Force](#8-beam-force) | `BEAMFORCE` / `BEAMFORCEVBM` |
| 9 | [Beam Force (Static Prestress)](#9-beam-force-static-prestress) | `BEAMFORCESTP` |
| 10 | [Beam Stress](#10-beam-stress) | `BEAMSTRESS` / `BEAMSTRESS7DOF` / `BEAMSTRESSVBM` |
| 11 | [Beam Stress (Equivalent)](#11-beam-stress-equivalent) | `BEAMSTRESSDETAIL` |
| 12 | [Beam Stress (PSC)](#12-beam-stress-psc) | `BEAMSTRESSPSC` / `BEAMSTRESS7DOFPSC` |
| 13 | [Concurrent Joint Force](#13-concurrent-joint-force) | `CONCURRENT_JOINT_FORCE` |

---

## 1. Reaction

> **기능:** 지점 반력(전역/국부/면스프링 국부)을 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"REACTIONG"` | Global (전역 좌표계) |
| `"REACTIONL"` | Local (국부 좌표계) |
| `"REACTIONSURFACESPRING"` | Local – Surface Spring (면스프링 국부) |

> ⚠️ 2026-08-26 확인 (article id `36009349748249`): 공식 Specifications 표·JSON Schema enum은
> 모두 `"REACTIONSURFACESPRING"`으로 일치하나, "Reaction(Local-Surface Spring)" Request Example
> 하나만 `"REACTIONLSURFACESPRING"`(L 추가)을 사용한다. 표·스키마 2곳이 일치하는 쪽을 채택하고
> 예제 쪽의 단발성 오타로 판단했으나, 실제 API 동작은 검증하지 않았으므로 오류제보 대상으로 남김.

### Response HEAD

`TABLE_TYPE` 값에 따라 응답 컬럼 구성이 다릅니다.

- `REACTIONG`(Global): `["Index", "Node", "Load", "FX", "FY", "FZ", "MX", "MY", "MZ", "Mb"]` (시공단계 조회 시 `Load` 뒤에 `Stage`/`Step` 추가)
- `REACTIONL`(Local): `["Index", "Node", "Load", "Fx", "Fy", "Fz", "Mx", "My", "Mz", "Mb"]` (Global과 동일 구조이나 필드명이 소문자)
- `REACTIONSURFACESPRING`(Local-Surface Spring): `["Index", "ElementType", "SurfaceSpringType", "Element", "Load", "Node&Part", "Reaction/Area", "Reaction/Length", "Displacement"]`(완전히 다른 구조)

> ⚠️ 2026-08-26 확인: `REACTIONG` 응답에는 `DATA` 배열과 별도로 최상위 `SUB_TABLES` 배열이
> 추가되며, 그 안에 `SUMMATIONOFREACTIONFORCESPRINTOUT` 하위 테이블(`HEAD`: `["Load", "FX(kN)",
> "FY(kN)", "FZ(kN)"]`, 시공단계 조회 시 `Stage`/`Step` 추가)이 포함된다. 이전 버전 문서에는
> 반영되어 있지 않아 아래 예제에 추가함. `REACTIONL`/`REACTIONSURFACESPRING`에는 `SUB_TABLES`가
> 없다.

### Request / Response JSON

**POST Request Body — 전역 반력(일반/Post CS)**

```json
{
  "Argument": {
    "TABLE_NAME": "Reaction(Global)",
    "TABLE_TYPE": "REACTIONG",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Node", "Load", "FX", "FY", "FZ", "MX", "MY", "MZ", "Mb"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Request Body — 전역 반력(시공단계)**

```json
{
  "Argument": {
    "TABLE_NAME": "Reaction(Global)",
    "TABLE_TYPE": "REACTIONG",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Node", "Load", "Stage", "Step", "FX", "FY", "FZ", "MX", "MY", "MZ", "Mb"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS1:001(first)", "CS1:002(last)"]
  }
}
```

**POST Response Body — 전역 반력(General/Post CS)**

```json
{
  "Reaction(Global)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Load", "FX", "FY", "FZ", "MX", "MY", "MZ", "Mb"],
    "DATA": [
      ["1", "1", "DL", "3.082169679668", "0.536339553582", "160.905188552207", "-0.531870057302", "3.112177384191", "0.000000000000", "0.000000000000"]
    ],
    "SUB_TABLES": [
      {
        "SUMMATIONOFREACTIONFORCESPRINTOUT": {
          "HEAD": ["Load", "FX(kN)", "FY(kN)", "FZ(kN)"],
          "DATA": [
            ["DL", "0.000000000000", "0.000000000000", "686.683352297500"]
          ]
        }
      }
    ]
  }
}
```

**POST Request Body — 국부 반력(Local)**

```json
{
  "Argument": {
    "TABLE_NAME": "Reaction(Local)",
    "TABLE_TYPE": "REACTIONL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Node", "Load", "Fx", "Fy", "Fz", "Mx", "My", "Mz", "Mb"],
    "NODE_ELEMS": { "KEYS": [9] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body — 국부 반력(Local)**

```json
{
  "Reaction(Local)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Load", "Fx", "Fy", "Fz", "Mx", "My", "Mz", "Mb"],
    "DATA": [
      ["1", "9", "DL", "-9.528467668945", "108.534577627514", "105.577135693819", "-2.014716071930", "-6.655711206332", "6.655708849960", "0.000000000000"]
    ]
  }
}
```

**POST Request Body — 면스프링 국부 반력(Local-Surface Spring)**

```json
{
  "Argument": {
    "TABLE_NAME": "Reaction(Local-SurfaceSpring)",
    "TABLE_TYPE": "REACTIONSURFACESPRING",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 }
  }
}
```

**POST Response Body — 면스프링 국부 반력(Local-Surface Spring)**

```json
{
  "Reaction(Local-SurfaceSpring)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "ElementType", "SurfaceSpringType", "Element", "Load", "Node&Part", "Reaction/Area", "Reaction/Length", "Displacement"],
    "DATA": [
      ["1", "PLATE", "Planar(Face)", "9", "UL", "5", "1.768850000000", "-", "-0.000901864"]
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

# ── POST: 1번 노드의 DL 하중케이스 전역 반력 추출 ──────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Reaction",
        "TABLE_TYPE": "REACTIONG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Reaction", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Node {d['Node']} ({d['Load']}): FZ={d['FZ']}")
```

---

## 2. Displacements

> **기능:** 절점 변위(전역/국부)를 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"DISPLACEMENTG"` | Global (전역 좌표계) |
| `"DISPLACEMENTL"` | Local (국부 좌표계) |

### Response HEAD

`["Index", "Node", "Load", "DX", "DY", "DZ", "RX", "RY", "RZ"]`(시공단계 조회 시 `Load` 뒤에 `Stage`/`Step` 추가)

### 시공단계(Construction Stage) 전용 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 시공단계 스텝 활성화 | `"OPT_CS"` | Boolean | `false` | Optional |
| 2 | 시공단계 스텝 이름 목록 | `"STAGE_STEP"` | Array [String] | All | Optional |
| 3 | 변위 표시 방식 · 누적: `"Accumulative"` / 현재: `"Current"` / 실제: `"Real"` | `"DISP_OPT"` | String | `"Accumulative"` | Optional |

> ⚠️ 2026-08-26 확인 (article id `36009638400281`): `DISP_OPT`는 이전 버전 문서에 누락되어 있었음
> — `OPT_CS=true`(시공단계 조회)일 때만 의미가 있는 필드로, 공식 Specifications 표·JSON Schema
> 양쪽에 존재.

### Request / Response JSON

**POST Request Body — 전역 변위(General/Post CS)**

```json
{
  "Argument": {
    "TABLE_NAME": "Displacement",
    "TABLE_TYPE": "DISPLACEMENTG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 3 },
    "COMPONENTS": ["Node", "Load", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "LOAD_CASE_NAMES": ["Self(ST)"]
  }
}
```

**POST Response Body — 전역 변위(General/Post CS)**

```json
{
  "Displacement": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Load", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "43", "Self", "5.047e+00", "5.234e-10", "-6.718e-07", "0.000e+00", "-5.108e-03", "1.903e-07"]
    ]
  }
}
```

**POST Request Body — 전역 변위(시공단계)**

```json
{
  "Argument": {
    "TABLE_NAME": "Displacement",
    "TABLE_TYPE": "DISPLACEMENTG",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 6 },
    "COMPONENTS": ["Node", "Load", "Stage", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [43] },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS16:001(first)", "CS16:002(last)"],
    "DISP_OPT": "Accumulative"
  }
}
```

**POST Response Body — 전역 변위(시공단계)**

```json
{
  "Displacement": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Node", "Load", "Stage", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "43", "Summation", "CS16", "001(first)", "-1.950282e+01", "-5.770649e-09", "-5.955365e-07", "0.000000e+00", "1.629373e-03", "2.975638e-06"],
      ["2", "43", "Summation", "CS16", "002(last)", "-7.132734e+01", "2.112468e-08", "-6.235268e-07", "0.000000e+00", "1.215839e-03", "8.756069e-06"]
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

# ── POST: 전역 변위 테이블 추출 ────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Displacement",
        "TABLE_TYPE": "DISPLACEMENTG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 3},
        "LOAD_CASE_NAMES": ["Self(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Displacement", {})
print(f"변위 결과 {len(table.get('DATA', []))}행")
```

---

## 3. Truss Force

> **기능:** 트러스 요소의 부재력(I단·J단 축력)을 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TRUSSFORCE"` | 트러스 부재력 |

### Response HEAD

`["Index", "Elem", "Load", "Force-I", "Force-J"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TrussForce",
    "TABLE_TYPE": "TRUSSFORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Force-I", "Force-J"],
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "TrussForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Force-I", "Force-J"],
    "DATA": [
      ["1", "33", "DL", "788.459634387094", "772.759634387094"]
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

# ── POST: 트러스 부재력 추출 ───────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TrussForce",
        "TABLE_TYPE": "TRUSSFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TrussForce", {})
for row in table.get("DATA", []):
    print(f"  Elem {row[1]}: Force-I={row[3]}, Force-J={row[4]}")
```

---

## 4. Truss Stress

> **기능:** 트러스 요소의 응력(I단·J단)을 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TRUSSSTRESS"` | 트러스 응력 |

### Response HEAD

`["Index", "Elem", "Load", "Stress-I", "Stress-J"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TrussStress",
    "TABLE_TYPE": "TRUSSSTRESS",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Stress-I", "Stress-J"],
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "TrussStress": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Stress-I", "Stress-J"],
    "DATA": [
      ["1", "33", "DL", "157691.926877418999", "154551.926877418999"]
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

# ── POST: 트러스 응력 추출 ─────────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TrussStress",
        "TABLE_TYPE": "TRUSSSTRESS",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TrussStress", {})
print(f"트러스 응력 {len(table.get('DATA', []))}행")
```

---

## 5. Cable Force

> **기능:** 케이블 요소의 장력(Tension)과 성분력(FX/FY/FZ)을 I단·J단별로 추출합니다. 시공단계 스텝(`Step`)별로 조회됩니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"CABLEFORCE"` | 케이블 부재력 |

### Response HEAD

- General/Post CS: `["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "Tension", "FX", "FY", "FZ", "Tension", "FX", "FY", "FZ"]`(뒤쪽 4개 `Tension`·`FX`·`FY`·`FZ`는 J단 성분)
- 시공단계(Construction Stage): `Step` 앞에 `Stage`가 추가된 `["Index", "Elem", "NodeI", "NodeJ", "Load", "Stage", "Step", "Tension", "FX", "FY", "FZ", "Tension", "FX", "FY", "FZ"]`

> ⚠️ 2026-08-26 확인 (article id `36010315199001`): 이전 버전 문서는 General/Post CS 응답 예제에
> `OPT_CS: true`·`STAGE_STEP: ["nl_001"]`·`LOAD_CASE_NAMES: ["SelfWeight(CS)"]` 요청을 잘못 붙여
> 놓아 실제로는 짝이 맞지 않는 요청/응답 조합이었음(`nl_001`은 시공단계 스텝이 아니라 Post-CS
> 비선형 스텝 자동 라벨). 아래에 두 시나리오(General/Post CS, 시공단계)를 정확한 요청/응답 쌍으로
> 분리해 정정.

### Request / Response JSON

**POST Request Body — General/Post CS**

```json
{
  "Argument": {
    "TABLE_NAME": "CableForce",
    "TABLE_TYPE": "CABLEFORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["SelfWeight(ST)"]
  }
}
```

**POST Response Body — General/Post CS**

```json
{
  "CableForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "Tension", "FX", "FY", "FZ", "Tension", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "1", "1", "2", "SelfWeight", "nl_001", "27419.266299103001", "-26808.034545985502", "-0.002024057832", "-5757.208365377180", "27431.024313956001", "26808.034545985502", "0.002024057832", "5812.949225142650"]
    ]
  }
}
```

**POST Request Body — 시공단계(Construction Stage)**

```json
{
  "Argument": {
    "TABLE_NAME": "CableForce",
    "TABLE_TYPE": "CABLEFORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS2:001(last)"]
  }
}
```

**POST Response Body — 시공단계(Construction Stage)**

```json
{
  "CableForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "NodeI", "NodeJ", "Load", "Stage", "Step", "Tension", "FX", "FY", "FZ", "Tension", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "1", "1", "2", "Summation", "CS2", "001(last)", "15538.648867201100", "-15187.887452924801", "-0.000971965905", "-3282.938216819810", "15550.520996389199", "15187.887452924801", "0.000971965905", "3338.679076585290"]
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

# ── POST: 케이블 장력 추출 (일반/Post CS) ──────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "CableForce",
        "TABLE_TYPE": "CABLEFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SelfWeight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CableForce", {})
for row in table.get("DATA", []):
    print(f"  Cable {row[1]}: Tension(I)={row[6]}")
```

---

## 6. Cable Configuration

> **기능:** 케이블 요소의 형상 정보(전체 길이·신장량·무변형 길이·처짐·수평/수직 거리·경사·스큐각 등)를 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"CABLECONFIG"` | 케이블 형상 |

### Response HEAD

- General/Post CS: `["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "TotalLength", "Elongation", "UnstrainedLength", "Sag", "HorizontalDistance", "VerticalDistance", "Gradient", "SkewAngle/IEnd", "SkewAngle/JEnd"]`
- 시공단계(Construction Stage): `Step` 앞에 `Stage`가 추가되고, 대신 뒤쪽의 `SkewAngle/IEnd`·`SkewAngle/JEnd` 2개 컬럼이 응답에서 빠짐 — `["Index", "Elem", "NodeI", "NodeJ", "Load", "Stage", "Step", "TotalLength", "Elongation", "UnstrainedLength", "Sag", "HorizontalDistance", "VerticalDistance", "Gradient"]`(14컬럼)

> ⚠️ 2026-08-26 확인 (article id `36011013418905`): 이전 버전 문서는 General/Post CS 응답 예제에
> `OPT_CS: true`·`STAGE_STEP: ["nl_001"]`·`LOAD_CASE_NAMES: ["SelfWeight(CS)"]` 요청을 잘못 붙여
> 놓아 실제로는 짝이 맞지 않는 요청/응답 조합이었음(5절 Cable Force와 동일한 문제). 아래에 두
> 시나리오를 정확한 요청/응답 쌍으로 분리해 정정. 시공단계 응답이 `SkewAngle` 2개 컬럼을 아예
> 빠뜨리는 것은 원문 자체의 특이사항으로, 원문의 시공단계 Request Example이 `COMPONENTS`에
> `"IEnd"`/`"JEnd"`를 명시적으로 요청함에도 실제 응답엔 반영되지 않는 자기모순 — 오류제보 대상.

### Request / Response JSON

**POST Request Body — General/Post CS**

```json
{
  "Argument": {
    "TABLE_NAME": "CableConfig",
    "TABLE_TYPE": "CABLECONFIG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["SelfWeight(ST)"]
  }
}
```

**POST Response Body — General/Post CS**

```json
{
  "CableConfig": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "TotalLength", "Elongation", "UnstrainedLength", "Sag", "HorizontalDistance", "VerticalDistance", "Gradient", "SkewAngle/IEnd", "SkewAngle/JEnd"],
    "DATA": [
      ["1", "1", "1", "2", "SelfWeight", "nl_001", "16.511543914801", "0.055076495942", "16.456467418860", "0.004194907068", "16.140012646203", "3.482956316281", "0.215796380872", "12.121120396140", "12.233836223754"]
    ]
  }
}
```

**POST Request Body — 시공단계(Construction Stage)**

```json
{
  "Argument": {
    "TABLE_NAME": "CableConfiguration",
    "TABLE_TYPE": "CABLECONFIG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS2:001(last)"]
  }
}
```

**POST Response Body — 시공단계(Construction Stage)**

```json
{
  "CableConfiguration": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "NodeI", "NodeJ", "Load", "Stage", "Step", "TotalLength", "Elongation", "UnstrainedLength", "Sag", "HorizontalDistance", "VerticalDistance", "Gradient"],
    "DATA": [
      ["1", "1", "1", "2", "Summation", "CS2", "001(last)", "16.487684968322", "0.031217549462", "16.456467418860", "0.007390270826", "16.109363292361", "3.511679349731", "0.217989953172"]
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

# ── POST: 케이블 형상 정보 추출 (일반/Post CS) ─────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "CableConfig",
        "TABLE_TYPE": "CABLECONFIG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SelfWeight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CableConfig", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Cable {d['Elem']}: 전체길이={d['TotalLength']}, 무변형길이={d['UnstrainedLength']}")
```

---

## 7. Cable Efficiency

> **기능:** 케이블 요소의 효율(Efficiency, 등가 강성 저감 지표) 관련 값(현 길이·ExA·중량·장력·수정 ExA·효율)을 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"CABLEEFFIENCY"` | 케이블 효율 (원문 철자 그대로) |

> **주의:** `TABLE_TYPE` 값은 원문 API 기준 `"CABLEEFFIENCY"`로, `EFFICIENCY`가 아닌 `EFFIENCY`입니다(오탈자가 API 스펙에 그대로 반영됨).

### Response HEAD

`["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "ChordLength", "ExA", "Weight", "Tension", "ExA(mod)", "Efficiency"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "CableEfficiency",
    "TABLE_TYPE": "CABLEEFFIENCY",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["SelfWeight(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["nl_001"]
  }
}
```

**POST Response Body**

```json
{
  "CableEfficiency": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "ChordLength", "ExA", "Weight", "Tension", "ExA(mod)", "Efficiency"],
    "DATA": [
      ["1", "1", "1", "2", "SelfWeight", "nl_001", "16.511541203676", "8194436.740000000224", "55.740859765477", "27425.145306529499", "8193631.458022129722", "0.999901728209"]
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

# ── POST: 케이블 효율 추출 ─────────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "CableEfficiency",
        "TABLE_TYPE": "CABLEEFFIENCY",   # 원문 철자 그대로 (EFFIENCY)
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SelfWeight(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CableEfficiency", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Cable {d['Elem']}: 효율={d['Efficiency']}")
```

---

## 8. Beam Force

> **기능:** 보 요소의 부재력/모멘트(축력·전단력·비틀림·모멘트·바이모멘트 등)를 부재 위치(Part)별로 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"BEAMFORCE"` | 보 부재력 (부재 위치별) |
| `"BEAMFORCEVBM"` | 보 부재력 (최댓값 기준, View by Max Value) |

> ⚠️ 2026-08-26 확인 (article id `36011262919705`): 두 번째 값은 이전 버전 문서에 `"BEAMFORCEBYMAX"`로
> 되어 있었으나, 이는 공식 JSON Schema의 enum에서만 쓰인 값이고 실제 Request Example과
> Specifications 표는 모두 `"BEAMFORCEVBM"`을 사용한다. 예제·표 기준으로 정정(스키마 오타로 판단,
> 오류제보 대상).

### 부재 위치(Parts) 지정 — 8~12절 공통

`Beam Force`/`Beam Force (Static Prestress)`/`Beam Stress`/`Beam Stress (Equivalent)`/
`Beam Stress (PSC)` 5개 테이블은 아래 `PARTS` 파라미터로 조회할 부재 위치를 지정할 수 있습니다
(생략 시 전체 위치).

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 11 | 부재 위치 · I단: `"PartI"` / 1/4점: `"Part1/4"` / 2/4점: `"Part2/4"` / 3/4점: `"Part3/4"` / J단: `"PartJ"` | `"PARTS"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 확인: 공식 Specifications 표는 값 표기를 `"Part I"`/`"Part J"`처럼 공백 포함으로
> 적었고, JSON Schema의 `enum`은 `"Part1"`(자릿수 1, I가 아님)처럼 표기했으나, 실제 Request
> Example은 둘 다와 다른 공백 없는 `"PartI"`/`"PartJ"`를 사용한다. 예제 기준으로 채택.

### Response HEAD

- `BEAMFORCE`: `["Index", "Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Bi-Moment", "T-Moment", "W-Moment"]`
- `BEAMFORCEVBM`: `Part` 뒤에 어느 성분이 최댓값을 낸 것인지 나타내는 `Component` 컬럼이 추가되고 Bi/T/W-Moment는 없음 — `["Index", "Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

### Request / Response JSON

**POST Request Body — BEAMFORCE**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamForce",
    "TABLE_TYPE": "BEAMFORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "TO": "1 to 10" },
    "LOAD_CASE_NAMES": ["Selfweight(ST)"]
  }
}
```

**POST Response Body — BEAMFORCE**

```json
{
  "BeamForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Bi-Moment", "T-Moment", "W-Moment"],
    "DATA": [
      ["1", "1", "Selfweight", "I", "0.0000", "0.0000", "12.5000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000"],
      ["2", "1", "Selfweight", "J", "0.0000", "0.0000", "-12.5000", "0.0000", "25.0000", "0.0000", "0.0000", "0.0000", "0.0000"]
    ]
  }
}
```

**POST Request Body — BEAMFORCEVBM(View by Max Value)**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamForceViewByMaxValue",
    "TABLE_TYPE": "BEAMFORCEVBM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [2833] },
    "LOAD_CASE_NAMES": ["STLENV_STR(CB:max)", "STLENV_STR(CB:min)"],
    "PARTS": ["PartI", "PartJ"],
    "ITEM_TO_DISPLAY": ["Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]
  }
}
```

**POST Response Body — BEAMFORCEVBM(View by Max Value)**

```json
{
  "BeamForceViewByMaxValue": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "2833", "STLENV_STR(max)", "I[781]", "Axial", "182.614058593750", "0.041735554695", "6.277819091797", "0.006796598315", "21.295148437500", "0.051163814545"],
      ["2", "2833", "STLENV_STR(max)", "I[781]", "Shear-y", "180.999328125000", "0.041774380684", "6.222307861328", "0.006750476599", "21.106847412109", "0.051366916656"]
    ]
  }
}
```

> ⚠️ 2026-08-26 확인: `ITEM_TO_DISPLAY`(`BEAMFORCEVBM` 전용, enum: `Axial`/`Shear-y`/`Shear-z`/
> `Torsion`/`Moment-y`/`Moment-z`)는 이전 버전 문서에 누락되어 있었음 — 최댓값을 계산할 대상
> 성분을 지정하는 필드로, 표시된 `Component` 값과 대응합니다.

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 1~10번 보 요소의 부재력 추출 ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "BeamForce",
        "TABLE_TYPE": "BEAMFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "NODE_ELEMS": {"TO": "1 to 10"},
        "LOAD_CASE_NAMES": ["Selfweight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BeamForce", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} ({d['Part']}): Moment-y={d['Moment-y']}")
```

---

## 9. Beam Force (Static Prestress)

> **기능:** 정적 프리스트레스(Static Prestress) 하중에 대한 보 부재력을 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"BEAMFORCESTP"` | 보 부재력 (정적 프리스트레스) |

> ⚠️ 2026-08-26 확인 (article id `36011373070745`): 이전 버전 문서는 `"BEAMFORCESIP"`로
> 표기했으나, 공식 JSON Schema enum만 그 값을 쓰고 실제 Request Example·Specifications 표는
> 모두 `"BEAMFORCESTP"`를 사용한다. 예제·표 기준으로 정정(스키마 오타로 판단, 오류제보 대상).
> `PARTS`(8절 공통 파라미터 참조, 값 예: `"PartI"`/`"PartJ"`)도 이 테이블에 적용되나 이전
> 버전에는 누락되어 있었음.

### Response HEAD

`["Index", "Elem", "Load", "Part", "Type", "Axial", "Shear-z", "Moment-y"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamForcePS",
    "TABLE_TYPE": "BEAMFORCESTP",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "Type", "Axial", "Shear-z", "Moment-y"],
    "LOAD_CASE_NAMES": ["Prestress(ST)"],
    "PARTS": ["PartI", "PartJ"]
  }
}
```

**POST Response Body**

```json
{
  "BeamForcePS": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Type", "Axial", "Shear-z", "Moment-y"],
    "DATA": [
      ["1", "1", "Prestress", "I", "Pre", "-1200.0000", "50.0000", "0.0000"]
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

# ── POST: 정적 프리스트레스 보 부재력 추출 ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "BeamForcePS",
        "TABLE_TYPE": "BEAMFORCESTP",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["Prestress(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BeamForcePS", {})
print(f"프리스트레스 부재력 {len(table.get('DATA', []))}행")
```

---

## 10. Beam Stress

> **기능:** 보 요소의 응력(축응력·전단응력·휨응력·조합응력)을 추출합니다. 7th DOF(뒴, Warping) 포함 옵션을 지원합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"BEAMSTRESS"` | 보 응력 |
| `"BEAMSTRESS7DOF"` | 보 응력 (7th DOF – Warping 포함) |
| `"BEAMSTRESSVBM"` | 보 응력 (최댓값 기준, View by Max Value) |

> ⚠️ 2026-08-26 확인 (article id `36011455813273`): `BEAMSTRESSVBM`은 이전 버전 문서에 누락되어
> 있었음 — 공식 JSON Schema의 enum에는 없으나 Specifications 표와 완전한 Request/Response
> 예제가 존재해 실존하는 값으로 판단, 보강함(스키마가 예제·표보다 뒤처진 사례).

### 부재 위치·단면위치(Parts / Section Position) 지정

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 11 | 부재 위치 · I단: `"PartI"` / 1/4점: `"Part1/4"` / 2/4점: `"Part2/4"` / 3/4점: `"Part3/4"` / J단: `"PartJ"` | `"PARTS"` | Array [String] | All | Optional |
| 12 | 단면 위치(`BEAMSTRESS7DOF` 전용) · `"Pos-1"`/`"Pos-2"`/`"Pos-3"`/`"Pos-4"`/`"Max"` | `"SECTION_POSITION"` | Array [String] | All | Optional |
| 13 | 최댓값 계산 대상 성분(`BEAMSTRESSVBM` 전용) · `Axial`/`Shear-y`/`Shear-z`/`Bend(+y)`/`Bend(-y)`/`Bend(+z)`/`Bend(-z)` | `"ITEM_TO_DISPLAY"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 확인: 위 3개 파라미터(`PARTS`/`SECTION_POSITION`/`ITEM_TO_DISPLAY`) 모두 이전
> 버전 문서에 누락되어 있었음.

### 시공단계(Construction Stage) 전용 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 시공단계 스텝 활성화 | `"OPT_CS"` | Boolean | `false` | Optional |
| 2 | 시공단계 스텝 이름 목록 | `"STAGE_STEP"` | Array [String] | All | Optional |

> ⚠️ 2026-08-30 정기 점검 확인 (article id `36011455813273`, 원문 갱신 2026-08-27): `BEAMSTRESS`·
> `BEAMSTRESS7DOF` 시공단계(CS) 조회 예제가 원문에 추가/보강되어 있었으나 이전 버전 문서에는
> 반영되지 않았음 — `OPT_CS`/`STAGE_STEP`(공통 파라미터)로 시공단계 스텝별 결과를 조회하며,
> `BEAMSTRESSVBM`은 원문에 CS 전용 예제가 없음(비-CS 예제만 존재).

### Response HEAD

- `BEAMSTRESS`: `["Index", "Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"]`(시공단계 조회 시 `Load` 뒤에 `Stage`/`Step` 추가)
- `BEAMSTRESSVBM`: `Part` 뒤에 `Component` 컬럼이 추가된 것 외에는 `BEAMSTRESS`와 동일 — `["Index", "Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"]`
- `BEAMSTRESS7DOF`: 완전히 다른 구조 — `["Index", "Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Cb(Ssy)", "Cb(Ssz)"]`(시공단계 조회 시 `Load` 뒤에 `Stage`/`Step` 추가)

> ⚠️ 2026-08-26 확인: 이전 버전 문서는 `BEAMSTRESS7DOF`도 `BEAMSTRESS`와 같은 HEAD를 쓰는 것으로
> 오해할 수 있게 단일 HEAD만 표기했으나, 실제로는 7th DOF 전용 컬럼(`SectionPosition`,
> `Sax(Warping)`, `Ssy/Ssz(Mt/Mw)`, `Cb(Ssy/Ssz)`)을 쓰는 별개 구조임을 명시.

### Request / Response JSON

**POST Request Body — BEAMSTRESS(General)**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStress",
    "TABLE_TYPE": "BEAMSTRESS",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)"],
    "NODE_ELEMS": { "TO": "1 to 10" },
    "LOAD_CASE_NAMES": ["Selfweight(ST)"]
  }
}
```

**POST Response Body — BEAMSTRESS(General)**

```json
{
  "BeamStress": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"],
    "DATA": [
      ["1", "1", "Selfweight", "I", "0.0000", "0.0000", "1250.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000"]
    ]
  }
}
```

**POST Request Body — BEAMSTRESS(시공단계)**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStress",
    "TABLE_TYPE": "BEAMSTRESS",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Stage", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "PARTS": ["PartI", "PartJ"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS3:001(first)", "CS3:002(last)"]
  }
}
```

**POST Response Body — BEAMSTRESS(시공단계)**

```json
{
  "BeamStress": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Load", "Stage", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"],
    "DATA": [
      ["1", "1", "Summation", "CS3", "001(first)", "I[1]", "-0.774105629705", "0.000000000000", "-0.633378895214", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "-0.774105629705", "-0.774105629705", "-0.774105629705", "-0.774105629705", "-0.774105629705"],
      ["2", "1", "Summation", "CS3", "001(first)", "J[2]", "-0.787581597130", "0.000000000000", "-0.510199230117", "0.000000000000", "0.000000000000", "-1.517545803005", "1.519418342486", "-2.328225752254", "-2.282028873379", "-2.328225752254", "0.754933827124", "0.708739639195"]
    ]
  }
}
```

**POST Request Body — BEAMSTRESS7DOF(General)**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStress(7thDOF)",
    "TABLE_TYPE": "BEAMSTRESS7DOF",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Cb(Ssy)", "Cb(Ssz)"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["EccentricLoads(ST)"],
    "PARTS": ["PartI", "PartJ"],
    "SECTION_POSITION": ["Pos-1", "Max"]
  }
}
```

**POST Response Body — BEAMSTRESS7DOF(General)**

```json
{
  "BeamStress(7thDOF)": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Cb(Ssy)", "Cb(Ssz)"],
    "DATA": [
      ["1", "1", "EccentricLoads", "I[1]", "Pos-1", "0.000000000000", "-0.000769832639", "0.014441854460", "-0.000722966974", "0.009767207099", "0.013672021820", "0.009044240125"],
      ["2", "1", "EccentricLoads", "I[1]", "Max", "0.000000000000", "-0.000769832639", "0.014441854460", "-0.000722966974", "0.009767207099", "0.013672021820", "0.009044240125"]
    ]
  }
}
```

**POST Request Body — BEAMSTRESS7DOF(시공단계)**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStress(7thDOF)",
    "TABLE_TYPE": "BEAMSTRESS7DOF",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Stage", "Step", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Cb(Ssy)", "Cb(Ssz)"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "PARTS": ["PartI", "PartJ"],
    "SECTION_POSITION": ["Pos-1", "Max"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS3:001(first)", "CS3:002(last)"]
  }
}
```

**POST Response Body — BEAMSTRESS7DOF(시공단계)**

```json
{
  "BeamStress(7thDOF)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Stage", "Step", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Cb(Ssy)", "Cb(Ssz)"],
    "DATA": [
      ["1", "1", "Summation", "CS3", "001(first)", "I[1]", "Pos-1", "0.000000000000", "-0.202862111996", "69.145522875219", "-0.190512326587", "46.763983379006", "68.942660763224", "46.573471052419"],
      ["2", "1", "Summation", "CS3", "001(first)", "I[1]", "Max", "0.000000000000", "-0.202862111996", "69.145522875219", "-0.190512326587", "46.763983379006", "68.942660763224", "46.573471052419"]
    ]
  }
}
```

**POST Request Body — BEAMSTRESSVBM(View by Max Value)**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStressViewByMaxValue",
    "TABLE_TYPE": "BEAMSTRESSVBM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"],
    "NODE_ELEMS": { "KEYS": [2833] },
    "LOAD_CASE_NAMES": ["STLENV_SER(CB:max)", "STLENV_SER(CB:min)"],
    "PARTS": ["PartI", "PartJ"],
    "ITEM_TO_DISPLAY": ["Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)"]
  }
}
```

**POST Response Body — BEAMSTRESSVBM(View by Max Value)**

```json
{
  "BeamStressViewByMaxValue": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"],
    "DATA": [
      ["1", "2833", "STLENV_SER(max)", "I[781]", "Axial", "14501.204492710700", "10.364105217203", "1287.477776027480", "-190.557266825830", "190.557266825830", "-12261.744480687799", "32108.382246495301", "46800.144006031900", "2430.017278848780", "2048.902745197120", "46419.029472380200", "46800.144006031900"]
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

# ── POST: 보 응력 추출 (7th DOF 포함 시 TABLE_TYPE=BEAMSTRESS7DOF) ─
payload = {
    "Argument": {
        "TABLE_NAME": "BeamStress",
        "TABLE_TYPE": "BEAMSTRESS",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "NODE_ELEMS": {"TO": "1 to 10"},
        "LOAD_CASE_NAMES": ["Selfweight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BeamStress", {})
print(f"보 응력 {len(table.get('DATA', []))}행")
```

---

## 11. Beam Stress (Equivalent)

> **기능:** 보 요소의 등가 응력(Equivalent, 단면 위치별 상세 응력 – 수직·전단·Von-Mises·최대전단·주응력)을 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"BEAMSTRESSDETAIL"` | 보 등가 응력 (상세) |

### 부재 위치·단면위치(Parts / Section Position) 지정

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 11 | 부재 위치 · I단: `"PartI"` / 1/4점: `"Part1/4"` / 2/4점: `"Part2/4"` / 3/4점: `"Part3/4"` / J단: `"PartJ"` | `"PARTS"` | Array [String] | All | Optional |
| 12 | 단면 위치(각형강관·I형강 단면의 응력 검토점 번호) · 최댓값: `"Maximum"` / 1~28번 위치: `"1"`~`"28"` | `"SECTION_POSITION"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 확인 (article id `36011572000153`): `PARTS`·`SECTION_POSITION` 모두 이전 버전
> 문서에 누락되어 있었음. `SECTION_POSITION`의 값 체계는 10절(Beam Stress) `BEAMSTRESS7DOF`의
> `"Pos-1"`~`"Pos-4"`/`"Max"`와 다른, 이 테이블 전용의 번호(`"1"`~`"28"`)/`"Maximum"` 체계임에
> 주의.

### Response HEAD

`["Index", "Elem", "Load", "Part", "SectionPosition", "Normal", "Tau_xy", "Tau_xz", "Von-Mises", "Max-Shear", "Princ.(max)", "Princ.(min)"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStressEq",
    "TABLE_TYPE": "BEAMSTRESSDETAIL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "SectionPosition", "Normal", "Tau_xy", "Tau_xz", "Von-Mises", "Max-Shear", "Princ.(max)", "Princ.(min)"],
    "NODE_ELEMS": { "KEYS": [32] },
    "LOAD_CASE_NAMES": ["Selfweight(ST)"],
    "PARTS": ["PartI", "PartJ"],
    "SECTION_POSITION": ["Maximum", "12"]
  }
}
```

**POST Response Body**

```json
{
  "BeamStressEq": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "SectionPosition", "Normal", "Tau_xy", "Tau_xz", "Von-Mises", "Max-Shear", "Princ.(max)", "Princ.(min)"],
    "DATA": [
      ["1", "32", "Selfweight", "I", "1", "0.0000", "0.0000", "1250.0000", "2165.0635", "1250.0000", "1250.0000", "-1250.0000"]
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

# ── POST: 보 등가 응력(상세) 추출 ──────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "BeamStressEq",
        "TABLE_TYPE": "BEAMSTRESSDETAIL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [32]},
        "LOAD_CASE_NAMES": ["Selfweight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BeamStressEq", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} 위치{d['SectionPosition']}: Von-Mises={d['Von-Mises']}")
```

---

## 12. Beam Stress (PSC)

> **기능:** PSC(프리스트레스 콘크리트) 보 요소의 응력을 성분별(축력·모멘트·텐던·합계·전단·비틀림·주응력 등)로 상세 추출합니다. 7th DOF 포함 옵션을 지원합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"BEAMSTRESSPSC"` | PSC 보 응력 |
| `"BEAMSTRESS7DOFPSC"` | PSC 보 응력 (7th DOF – Warping 포함) |

### 부재 위치·단면위치(Parts / Section Position) 지정

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 11 | 부재 위치 · I단: `"PartI"` / 1/4점: `"Part1/4"` / 2/4점: `"Part2/4"` / 3/4점: `"Part3/4"` / J단: `"PartJ"` | `"PARTS"` | Array [String] | All | Optional |
| 12 | 단면 위치(`BEAMSTRESS7DOFPSC` 전용) · `"Pos-1"`~`"Pos-16"` / 최댓값: `"Max"` / 최솟값: `"Min"` / 전체: `"All"` | `"SECTION_POSITION"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 확인 (article id `36011704177561`): `PARTS`·`SECTION_POSITION` 모두 이전 버전
> 문서에 누락되어 있었음. `SECTION_POSITION`의 위치 개수(16개)는 10절 `BEAMSTRESS7DOF`(4개)보다
> 많다 — PSC 단면이 더 세분화된 검토점을 갖기 때문으로 추정.

### Response HEAD

- `BEAMSTRESSPSC`: `["Index", "Elem", "Load", "Part", "SectionPosition", "Sig-xx(Axial)", "Sig-xx(Moment-y)", "Sig-xx(Moment-z)", "Sig-xx(Bar)", "Sig-xx(Summation)", "Sig-zz", "Sig-xz(shear)", "Sig-xz(torsion)", "Sig-xz(bar)", "Sig-Is(shear)", "Sig-Is(shear+torsion)", "Sig-Ps(Max)", "Sig-Ps(Min)"]`
- `BEAMSTRESS7DOFPSC`: 완전히 다른 구조 — `["Index", "Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Combined(Ssy)", "Combined(Ssz)"]`

> ⚠️ 2026-08-26 확인: `BEAMSTRESS7DOFPSC`는 10절 `BEAMSTRESS7DOF`와 개념은 유사하나(같은
> Sax/Ssy/Ssz 구조) 마지막 두 컬럼명이 `Cb(Ssy)`/`Cb(Ssz)`가 아니라 `Combined(Ssy)`/
> `Combined(Ssz)`로 다르게 표기되어 있음 — 원문에서 별개로 작성된 두 아티클 간 명명 불일치로
> 판단(오류라기보다 정보성 기록, 오류제보 대상).

### Request / Response JSON

**POST Request Body — BEAMSTRESSPSC**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStressPSC",
    "TABLE_TYPE": "BEAMSTRESSPSC",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "SectionPosition", "Sig-xx(Axial)", "Sig-xx(Moment-y)", "Sig-xx(Summation)", "Sig-Ps(Max)", "Sig-Ps(Min)"],
    "NODE_ELEMS": { "TO": "1 to 5" },
    "LOAD_CASE_NAMES": ["Selfweight(ST)"]
  }
}
```

**POST Response Body — BEAMSTRESSPSC**

```json
{
  "BeamStressPSC": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "SectionPosition", "Sig-xx(Axial)", "Sig-xx(Moment-y)", "Sig-xx(Moment-z)", "Sig-xx(Bar)", "Sig-xx(Summation)", "Sig-zz", "Sig-xz(shear)", "Sig-xz(torsion)", "Sig-xz(bar)", "Sig-Is(shear)", "Sig-Is(shear+torsion)", "Sig-Ps(Max)", "Sig-Ps(Min)"],
    "DATA": [
      ["1", "1", "Selfweight", "I", "1", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00"]
    ]
  }
}
```

**POST Request Body — BEAMSTRESS7DOFPSC**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStress(7thDOF)(PSC)",
    "TABLE_TYPE": "BEAMSTRESS7DOFPSC",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Combined(Ssy)", "Combined(Ssz)"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["EccentricLoads(ST)"],
    "PARTS": ["PartI", "PartJ"],
    "SECTION_POSITION": ["Pos-7", "All"]
  }
}
```

**POST Response Body — BEAMSTRESS7DOFPSC**

```json
{
  "BeamStress(7thDOF)(PSC)": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Combined(Ssy)", "Combined(Ssz)"],
    "DATA": [
      ["1", "1", "EccentricLoads", "I[1]", "Pos-7", "0.000000000000", "-0.000020377582", "-0.000013533950", "-0.023715019562", "-0.006463496296", "-0.000033911532", "-0.030178515858"],
      ["2", "1", "EccentricLoads", "I[1]", "All", "0.000000000000", "-0.023715019562", "-0.023273488440", "0.023715021748", "-0.015750538530", "-0.039465558092", "-0.039465558092"]
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

# ── POST: PSC 보 응력 추출 (7th DOF 포함 시 BEAMSTRESS7DOFPSC) ─────
payload = {
    "Argument": {
        "TABLE_NAME": "BeamStressPSC",
        "TABLE_TYPE": "BEAMSTRESSPSC",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 4},
        "NODE_ELEMS": {"TO": "1 to 5"},
        "LOAD_CASE_NAMES": ["Selfweight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BeamStressPSC", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} 위치{d['SectionPosition']}: 합계응력={d['Sig-xx(Summation)']}")
```

---

## 13. Concurrent Joint Force

> **기능:** 지정한 반력 절점(`NODE_KEY`)의 반력 성분이 극값(max/min)을 이루는 시점에 대해, 지정된
> 하중케이스 목록의 절점력을 동시(concurrent) 값으로 추출합니다. 이동하중(Moving Load) 해석에서
> `(MV:max)` / `(MV:min)` 계열 하중케이스와 함께 주로 사용됩니다.

### `TABLE_TYPE`

| 값 | 설명 |
| --- | --- |
| `"CONCURRENT_JOINT_FORCE"` | 동시 절점력(Concurrent Joint Force) |

> ⚠️ 2026-08-26 확인 (article id `59520540732185`): 이 테이블은 공통 파라미터 표(위 "공통 Request
> 구조 및 파라미터")가 아니라 **자기 자신만의 독립된 스키마**를 가지며, 공식 JSON Schema에
> `"additionalProperties": false`가 걸려 있어 공통 항목 중 `NODE_ELEMS`/`OPT_CS`/`STAGE_STEP`는
> **이 테이블에 존재하지 않고 사용할 수 없습니다**(전송 시 거부될 가능성). 허용되는 필드는
> `TABLE_TYPE`/`LOAD_CASE_NAMES`/`TABLE_NAME`/`EXPORT_PATH`/`UNIT`/`STYLES`/`COMPONENTS`/
> `ADDITIONAL` 8개뿐입니다. 또한 `LOAD_CASE_NAMES`는 다른 12개 테이블과 달리(공통 표는
> Optional·기본값 All) 공식 스키마의 `required`에 포함되어 **Required**입니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 하중케이스 이름 목록 | `"LOAD_CASE_NAMES"` | Array [String] | — | **Required** |
| 2 | 반력 극값 기준 추가 설정 | `"ADDITIONAL"` | Object | — | **Required** |
| 2-1 | └ 반력 절점 기준 설정 | `ADDITIONAL.SET_REACTION_PARAMS` | Object | — | **Required** |
| 2-1-1 | 　└ 반력 절점 ID | `SET_REACTION_PARAMS.NODE_KEY` | Integer | — | **Required** |
| 2-1-2 | 　└ 반력 성분 사용 여부 6자리(0/1), 순서 Fx·Fy·Fz·Mx·My·Mz | `SET_REACTION_PARAMS.COMPONENT` | String | — | **Required** |

### Response HEAD

응답 `HEAD`는 기본 `"Index"`/`"Elem."`/`"Load"` 3열 뒤에, `"Elem./Component"` + `9[J]/Fx`~
`10[I]/Mz`(반력 절점을 사이에 둔 두 인접 요소 × 6성분 = 12열) 13열짜리 블록이 **반력 성분 개수만큼
(Fx/Fy/Fz/Mx/My/Mz 최대 6개)** 반복되어 이어붙습니다.

`DATA`는 (이전 버전 문서와 반대로) **요소별로 한 행**을 이룹니다 — 절점 양옆의 두 요소(`9[J]`,
`10[I]`) 각각이 한 행이 되며, 각 행 안에서 위 13열 블록이 반력 성분(Fx/Fy/Fz/Mx/My/Mz) 개수만큼
반복됩니다(각 블록의 첫 칸이 `"Fx"`~`"Mz"` 라벨, 나머지 12칸이 그 성분이 극값을 이루는 시점의
동시 절점력).

> ⚠️ 2026-08-26 확인: 이전 버전 문서는 이 구조를 반대로 설명했습니다("성분별 한 행, 요소별 블록
> 반복") — 실제로는 위처럼 요소별 한 행, 성분별 블록 반복입니다. 아래 예제는 공식 예제를 그대로
> 옮긴 것입니다(1개 하중케이스 × 반력성분 6개 선택 시 81열: `Index`/`Elem.`/`Load` 3열 + 13열 ×
> 6블록).

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "CONCURRENT_JOINT_FORCE",
    "LOAD_CASE_NAMES": ["case_01(MV:max)"],
    "TABLE_NAME": "Concurrent Joint Forces",
    "ADDITIONAL": {
      "SET_REACTION_PARAMS": {
        "NODE_KEY": 10,
        "COMPONENT": "111111"
      }
    },
    "UNIT": { "FORCE": "KN", "DIST": "M" }
  }
}
```

**POST Response Body**

```json
{
  "Concurrent Joint Forces": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index", "Elem.", "Load",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz"
    ],
    "DATA": [
      [
        "1", "9[J]", "case_01(max)",
        "Fx", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000",
        "Fy", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000",
        "Fz", "0.000000000000", "0.000000000000", "437.017000000000", "-558.415000000000", "938.805000000000", "0.000000000000", "0.000000000000", "0.000000000000", "437.017000000000", "-558.415000000000", "938.805000000000", "0.000000000000",
        "Mx", "0.000000000000", "0.000000000000", "-41.903300000000", "216.858000000000", "190.624000000000", "0.000000000000", "0.000000000000", "0.000000000000", "-41.903300000000", "216.858000000000", "190.624000000000", "0.000000000000",
        "My", "0.000000000000", "0.000000000000", "399.782000000000", "-422.014000000000", "1067.630000000000", "0.000000000000", "0.000000000000", "0.000000000000", "399.782000000000", "-422.014000000000", "1067.630000000000", "0.000000000000",
        "Mz", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"
      ],
      [
        "2", "10[I]", "case_01(max)",
        "Fx", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000",
        "Fy", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000",
        "Fz", "0.000000000000", "0.000000000000", "437.017000000000", "-558.415000000000", "938.805000000000", "0.000000000000", "0.000000000000", "0.000000000000", "437.017000000000", "-558.415000000000", "938.805000000000", "0.000000000000",
        "Mx", "0.000000000000", "0.000000000000", "-41.903300000000", "216.858000000000", "190.624000000000", "0.000000000000", "0.000000000000", "0.000000000000", "-41.903300000000", "216.858000000000", "190.624000000000", "0.000000000000",
        "My", "0.000000000000", "0.000000000000", "399.782000000000", "-422.014000000000", "1067.630000000000", "0.000000000000", "0.000000000000", "0.000000000000", "399.782000000000", "-422.014000000000", "1067.630000000000", "0.000000000000",
        "Mz", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"
      ]
    ]
  }
}
```

> ⚠️ 2026-08-26 확인: 공식 Response Example은 위 요청(`TABLE_NAME: "Concurrent Joint Forces"`)과
> 짝을 이루는데도 응답 최상위 키가 요청한 `TABLE_NAME`이 아니라 리터럴 `"empty"`로 되어 있습니다
> (`{"empty": {...}}`). 이 챕터의 다른 모든 테이블 및 공통 Response 구조(`{"<TABLE_NAME>": {...}}`)
> 관례와 어긋나는데, 원문 저작 시 실제 값으로 치환하지 않은 복사·붙여넣기 실수인지, 이 엔드포인트만의
> 실제 동작인지 판단할 근거가 없어 실제 API 동작은 검증하지 않았음을 전제로 오류제보 대상으로만
> 남기고, 위 예제는 관례를 따라 `"Concurrent Joint Forces"` 키를 그대로 유지했습니다.

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 반력 절점 10의 극값 시점 동시 절점력 추출 ──────────────────
payload = {
    "Argument": {
        "TABLE_TYPE": "CONCURRENT_JOINT_FORCE",
        "TABLE_NAME": "Concurrent Joint Forces",
        "LOAD_CASE_NAMES": ["case_01(MV:max)"],
        "ADDITIONAL": {
            "SET_REACTION_PARAMS": {"NODE_KEY": 10, "COMPONENT": "111111"}
        },
        "UNIT": {"FORCE": "KN", "DIST": "M"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Concurrent Joint Forces", {})
print(f"동시 절점력 {len(table.get('DATA', []))}행")
```

---

## End-to-End Workflow

다음은 해석 실행 후 반력·변위·부재력·응력을 일괄 추출하는 워크플로우입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

def get_result(table_type, name, load_cases, extra=None):
    """해석 결과 테이블 추출 공통 함수"""
    arg = {
        "TABLE_NAME": name,
        "TABLE_TYPE": table_type,
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": load_cases
    }
    if extra:
        arg.update(extra)
    resp = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    return resp.json().get(name, {})

# ── STEP 1: 지점 반력 (전역) ───────────────────────────────────────
reac = get_result("REACTIONG", "Reaction", ["DL(ST)"])
print(f"STEP1 반력 {len(reac.get('DATA', []))}행")

# ── STEP 2: 절점 변위 (전역) ───────────────────────────────────────
disp = get_result("DISPLACEMENTG", "Disp", ["DL(ST)"])
print(f"STEP2 변위 {len(disp.get('DATA', []))}행")

# ── STEP 3: 트러스 부재력·응력 ─────────────────────────────────────
tf = get_result("TRUSSFORCE", "TrussF", ["DL(ST)"])
ts = get_result("TRUSSSTRESS", "TrussS", ["DL(ST)"])
print(f"STEP3 트러스: 부재력 {len(tf.get('DATA', []))}, 응력 {len(ts.get('DATA', []))}")

# ── STEP 4: 보 부재력·응력 (1~10번 요소) ───────────────────────────
bf = get_result("BEAMFORCE", "BeamF", ["DL(ST)"], extra={"NODE_ELEMS": {"TO": "1 to 10"}})
bs = get_result("BEAMSTRESS", "BeamS", ["DL(ST)"], extra={"NODE_ELEMS": {"TO": "1 to 10"}})
print(f"STEP4 보: 부재력 {len(bf.get('DATA', []))}, 응력 {len(bs.get('DATA', []))}")

# ── STEP 5: 케이블 장력 (시공단계) ─────────────────────────────────
cf = get_result("CABLEFORCE", "CableF", ["SelfWeight(CS)"],
                extra={"OPT_CS": True, "STAGE_STEP": ["nl_001"]})
print(f"STEP5 케이블 장력 {len(cf.get('DATA', []))}행")
```
