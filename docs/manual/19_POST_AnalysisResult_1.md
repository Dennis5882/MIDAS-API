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

> **참고:** `OPT_CS`·`STAGE_STEP`는 시공단계 결과 조회 시 사용합니다(Reaction–Local Surface Spring 제외). `STAGE_STEP` 항목은 `"CS1:001(first)"`, `"CS1:002(last)"` 형식입니다.

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
| 8 | [Beam Force](#8-beam-force) | `BEAMFORCE` / `BEAMFORCEBYMAX` |
| 9 | [Beam Force (Static Prestress)](#9-beam-force-static-prestress) | `BEAMFORCESIP` |
| 10 | [Beam Stress](#10-beam-stress) | `BEAMSTRESS` / `BEAMSTRESS7DOF` |
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

### Response HEAD

`["Index", "Node", "Load", "FX", "FY", "FZ", "MX", "MY", "MZ", "Mb"]`

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

**POST Response Body**

```json
{
  "Reaction(Global)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Load", "FX", "FY", "FZ", "MX", "MY", "MZ", "Mb"],
    "DATA": [
      ["1", "1", "DL", "3.082169679668", "0.536339553582", "160.905188552207", "-0.531870057302", "3.112177384191", "0.000000000000", "0.000000000000"]
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

`["Index", "Node", "Load", "DX", "DY", "DZ", "RX", "RY", "RZ"]`

### Request / Response JSON

**POST Request Body**

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

**POST Response Body**

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

`["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "Tension", "FX", "FY", "FZ", "Tension", "FX", "FY", "FZ"]`  
(뒤쪽 4개 `Tension`·`FX`·`FY`·`FZ`는 J단 성분)

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "CableForce",
    "TABLE_TYPE": "CABLEFORCE",
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

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 케이블 장력 추출 (시공단계) ──────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "CableForce",
        "TABLE_TYPE": "CABLEFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SelfWeight(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
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

`["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "TotalLength", "Elongation", "UnstrainedLength", "Sag", "HorizontalDistance", "VerticalDistance", "Gradient", "SkewAngle/IEnd", "SkewAngle/JEnd"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "CableConfig",
    "TABLE_TYPE": "CABLECONFIG",
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

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 케이블 형상 정보 추출 ────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "CableConfig",
        "TABLE_TYPE": "CABLECONFIG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SelfWeight(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
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
| `"BEAMFORCEBYMAX"` | 보 부재력 (최댓값 기준) |

### Response HEAD

`["Index", "Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Bi-Moment", "T-Moment", "W-Moment"]`

### Request / Response JSON

**POST Request Body**

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

**POST Response Body**

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
| `"BEAMFORCESIP"` | 보 부재력 (정적 프리스트레스) |

### Response HEAD

`["Index", "Elem", "Load", "Part", "Type", "Axial", "Shear-z", "Moment-y"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamForcePS",
    "TABLE_TYPE": "BEAMFORCESIP",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "Type", "Axial", "Shear-z", "Moment-y"],
    "LOAD_CASE_NAMES": ["Prestress(ST)"]
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
        "TABLE_TYPE": "BEAMFORCESIP",
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

### Response HEAD

`["Index", "Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"]`

### Request / Response JSON

**POST Request Body**

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

**POST Response Body**

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
    "LOAD_CASE_NAMES": ["Selfweight(ST)"]
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

### Response HEAD

`["Index", "Elem", "Load", "Part", "SectionPosition", "Sig-xx(Axial)", "Sig-xx(Moment-y)", "Sig-xx(Moment-z)", "Sig-xx(Bar)", "Sig-xx(Summation)", "Sig-zz", "Sig-xz(shear)", "Sig-xz(torsion)", "Sig-xz(bar)", "Sig-Is(shear)", "Sig-Is(shear+torsion)", "Sig-Ps(Max)", "Sig-Ps(Min)"]`

### Request / Response JSON

**POST Request Body**

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

**POST Response Body**

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

> ⚠️ 이 테이블 타입은 공통 파라미터 표(위 "공통 Request 구조 및 파라미터")의 10개 항목 외에
> `"ADDITIONAL"` 객체가 **Required**로 추가됩니다. 다른 12개 테이블에는 없는 이 타입 전용 항목입니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 11 | 반력 극값 기준 추가 설정 | `"ADDITIONAL"` | Object | — | **Required** |
| 11-1 | └ 반력 절점 기준 설정 | `ADDITIONAL.SET_REACTION_PARAMS` | Object | — | **Required** |
| 11-1-1 | 　└ 반력 절점 ID | `SET_REACTION_PARAMS.NODE_KEY` | Integer | — | **Required** |
| 11-1-2 | 　└ 반력 성분 사용 여부 6자리(0/1), 순서 Fx·Fy·Fz·Mx·My·Mz | `SET_REACTION_PARAMS.COMPONENT` | String | — | **Required** |

### Response HEAD

응답 `HEAD`/`DATA`는 `COMPONENTS`에 지정한 `"Elem./Component"` + `9[J]/Fx`~`10[I]/Mz` 12개 열
블록이, 조회 대상 요소 개수만큼 반복되어 하나의 `HEAD` 배열에 이어붙는 구조입니다(기본 `"Index"`,
`"Elem."`, `"Load"` 3열 + 요소별 12열 × N). `DATA`는 요소가 아니라 **성분(Fx/Fy/Fz/Mx/My/Mz)별로
한 행**을 이루며, 각 행 안에서 요소별 블록이 반복됩니다.

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

**POST Response Body (발췌)**

```json
{
  "Concurrent Joint Forces": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Elem.", "Load", "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz"],
    "DATA": [
      ["1", "9[J]", "case_01(max)", "Fz", "0.0", "0.0", "437.017", "-558.415", "938.805", "0.0"]
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
