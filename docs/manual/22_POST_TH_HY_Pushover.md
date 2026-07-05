# 22. POST – TH / HY / Pushover Result Tables (시간이력·수화열·푸시오버 결과)

> **대상 제품:** MIDAS Gen NX · MIDAS Civil NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

이 파트는 **시간이력(Time History) · 수화열(Heat of Hydration) · 푸시오버(Pushover)** 해석 결과를 다루며, 총 **28개 엔드포인트**로 구성됩니다. 앞선 19~21장과 달리 이 파트의 엔드포인트는 **서로 다른 4개의 URI 그룹**에 속하므로, 그룹별로 요청 구조가 다릅니다.

| 그룹 | 내용 | 공통 URI | 메서드 | 엔드포인트 수 |
|------|------|----------|--------|:---:|
| **A** | 시간이력 / 푸시오버 텍스트 결과 | `POST {base url}/post/TEXT` | `POST` | 10 |
| **B** | 비탄성 힌지(Inelastic Hinge) 시간이력 결과 테이블 | `POST {base url}/post/TABLE` | `POST` | 9 |
| **C** | 수화열 해석 결과 그래픽 표시 | `POST {base url}/view/RESULTGRAPHIC` | `POST` | 5 |
| **D** | 시간이력 스마트 그래프 정의 DB | `{base url}/db/THR*` | `POST · GET · PUT · DELETE` | 4 |

### 전체 엔드포인트 요약 (28개)

| # | 절 | 엔드포인트(제목) | 그룹 | URI | 메서드 |
|---|-----|------------------|:---:|-----|--------|
| 1 | [A-1](#a-1-time-history-text--node-results) | Time History Text – Node Results | A | `post/TEXT` | POST |
| 2 | [A-2](#a-2-time-history-text--element-resulttruss-beam-plane-stressstrain-solid) | TH Text – Element (Truss/Beam/Plane/Solid) | A | `post/TEXT` | POST |
| 3 | [A-3](#a-3-time-history-text--element-resultplate) | TH Text – Element (Plate) | A | `post/TEXT` | POST |
| 4 | [A-4](#a-4-time-history-text--element-resultwall) | TH Text – Element (Wall) | A | `post/TEXT` | POST |
| 5 | [A-5](#a-5-time-history-text--general-link-result) | TH Text – General Link | A | `post/TEXT` | POST |
| 6 | [A-6](#a-6-pushover-text--displacement) | Pushover Text – Displacement | A | `post/TEXT` | POST |
| 7 | [A-7](#a-7-pushover-text--element-resultbeam-truss) | Pushover Text – Element (Beam, Truss) | A | `post/TEXT` | POST |
| 8 | [A-8](#a-8-pushover-text--element-resultwall) | Pushover Text – Element (Wall) | A | `post/TEXT` | POST |
| 9 | [A-9](#a-9-pushover-text--general-link) | Pushover Text – General Link | A | `post/TEXT` | POST |
| 10 | [A-10](#a-10-pushover-text--elastic-link) | Pushover Text – Elastic Link | A | `post/TEXT` | POST |
| 11 | [B-1](#b-1-inelastic-hinge-event-time) | Inelastic Hinge Event Time | B | `post/TABLE` | POST |
| 12 | [B-2](#b-2-inelastic-hinge-beam-summary) | Inelastic Hinge Beam Summary | B | `post/TABLE` | POST |
| 13 | [B-3](#b-3-inelastic-hinge-truss-summary) | Inelastic Hinge Truss Summary | B | `post/TABLE` | POST |
| 14 | [B-4](#b-4-inelastic-hinge-general-link-summary) | Inelastic Hinge General Link Summary | B | `post/TABLE` | POST |
| 15 | [B-5](#b-5-inelastic-hinge-force) | Inelastic Hinge Force | B | `post/TABLE` | POST |
| 16 | [B-6](#b-6-inelastic-hinge-deformation) | Inelastic Hinge Deformation | B | `post/TABLE` | POST |
| 17 | [B-7](#b-7-inelastic-hinge-element-rotation) | Inelastic Hinge Element Rotation | B | `post/TABLE` | POST |
| 18 | [B-8](#b-8-inelastic-hinge-ductility-factordd1) | Inelastic Hinge Ductility Factor (D/D1) | B | `post/TABLE` | POST |
| 19 | [B-9](#b-9-inelastic-hinge-ductility-factordd2) | Inelastic Hinge Ductility Factor (D/D2) | B | `post/TABLE` | POST |
| 20 | [C-1](#c-1-stress--heat-of-hydration) | Stress | C | `view/RESULTGRAPHIC` | POST |
| 21 | [C-2](#c-2-temperature--heat-of-hydration) | Temperature | C | `view/RESULTGRAPHIC` | POST |
| 22 | [C-3](#c-3-displacements--heat-of-hydration) | Displacements | C | `view/RESULTGRAPHIC` | POST |
| 23 | [C-4](#c-4-allowable-tensile-stress--heat-of-hydration) | Allowable Tensile Stress | C | `view/RESULTGRAPHIC` | POST |
| 24 | [C-5](#c-5-crack-ratio--heat-of-hydration) | Crack Ratio | C | `view/RESULTGRAPHIC` | POST |
| 25 | [D-1](#d-1-element-force-smart-graph--dbthre) | Element Force Smart Graph | D | `db/THRE` | POST·GET·PUT·DELETE |
| 26 | [D-2](#d-2-general-link-smart-graph--dbthrg) | General Link Smart Graph | D | `db/THRG` | POST·GET·PUT·DELETE |
| 27 | [D-3](#d-3-inelastic-hinge-smart-graph--dbthri) | Inelastic Hinge Smart Graph | D | `db/THRI` | POST·GET·PUT·DELETE |
| 28 | [D-4](#d-4-seismic-devices-smart-graph--dbthrs) | Seismic Devices Smart Graph | D | `db/THRS` | POST·GET·PUT·DELETE |

---

## 그룹 A. Time History / Pushover Text 결과 (`post/TEXT`)

시간이력·푸시오버 해석의 상세 결과를 **텍스트(JSON) 테이블**로 추출합니다. 반력·변위 테이블(19장)이 `post/TABLE` + `TABLE_TYPE`을 사용하는 것과 달리, 이 그룹은 **`post/TEXT` + `TEXT_TYPE`** 을 사용합니다.

### Input URI (그룹 A 공통)

```
{base url}/post/TEXT
```

### Active Methods

`POST`

### 공통 Request 구조 및 파라미터

요청 바디의 `"Argument"` 객체에서 `TEXT_TYPE`으로 결과 종류를 선택합니다. **아래 표는 그룹 A의 10개 엔드포인트 전체에 공통 적용**되며, 각 절에서는 `TEXT_TYPE` enum과 응답 `HEAD`, 대표 예시만 별도로 기술합니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 결과 텍스트 타입 (엔드포인트별 enum, 각 절 참조) | `"TEXT_TYPE"` | String | — | **Required** |
| 2 | 결과 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |
| 3 | 응답 단위 설정 | `"UNIT"` | Object | System | Optional |
| 3-1 | └ 힘(Force) | `UNIT.FORCE` | String | — | Optional |
| 3-2 | └ 길이(Length) | `UNIT.DIST` | String | — | Optional |
| 3-3 | └ 열(Heat) | `UNIT.HEAT` | String | — | Optional |
| 3-4 | └ 온도(Temperature) | `UNIT.TEMP` | String | — | Optional |
| 4 | 응답 숫자 형식 | `"STYLES"` | Object | System | Optional |
| 4-1 | └ 숫자 형식 · `"Fixed"` / `"Exponential"` | `STYLES.FORMAT` | String | — | Optional |
| 4-2 | └ 소수 자릿수 (0~15) | `STYLES.PLACE` | Integer | — | Optional |
| 5 | 결과 테이블 표시 열 | `"COMPONENTS"` | Array [String] | All | Optional |
| 6 | 노드/요소 지정 (아래 방식 중 하나) | `"NODE_ELEMS"` | Object | — | **Required** |
| 6-1 | 방식1: ID 각각 지정 (예: `[101, 102, 103]`) | `NODE_ELEMS.KEYS` | Array [Integer] | — | Optional |
| 6-2 | 방식2: ID 범위 지정 (예: `"101 to 105"`) | `NODE_ELEMS.TO` | String | — | Optional |
| 6-3 | 방식3: 구조 그룹명 지정 (예: `"SG1"`) | `NODE_ELEMS.STRUCTURE_GROUP_NAME` | String | — | Optional |
| 7 | 요소 결과 출력 위치 (요소 결과 전용) | `"PARTS"` | Array [String] | — | Optional |
| 8 | **시간이력 하중케이스** (TH 결과 전용) | `"TH_CASE_NAME"` | Array [String] | — | **Required** |
| 9 | **푸시오버 하중케이스** (Pushover 결과 전용) | `"PO_CASE_NAME"` | Array [String] | — | **Required** |
| 10 | 출력 스텝 지정 | `"STEP"` | Object | — | **Required** |
| 10-1 | └ 시작 시간/스텝 | `STEP.FROM` | Number | — | Required |
| 10-2 | └ 종료 시간/스텝 | `STEP.TO` | Number | — | Required |
| 10-3 | └ 시간 간격/스텝 간격 | `STEP.STEPS` | Integer | — | Required |
| 11 | 기준점(방식1) · `"Ground"` / `"AddGroundMotion"` | `"REF_PT"` | String | `"Ground"` | Optional |
| 12 | 기준점(방식2) · 다른 노드 지정 | `"ANR_NODE"` | Integer | — | Optional |

> **참고**
> - **`TH_CASE_NAME` vs `PO_CASE_NAME`:** 시간이력 결과(A-1~A-5)는 `TH_CASE_NAME`, 푸시오버 결과(A-6~A-10)는 `PO_CASE_NAME`을 사용합니다.
> - **`STEP`:** 시간이력에서는 `FROM`/`TO`가 **시간(초)** 이며, 푸시오버에서는 **스텝 번호**입니다.
> - **`PARTS`:** 보/트러스/벽 결과는 `["PartI", "PartJ"]`, 평판(Plate) 4절점 요소는 `["PartI", "PartJ", "PartK", "PartL"]`를 사용합니다. 노드 결과·일반링크 결과에는 사용하지 않습니다.
> - **`REF_PT`/`ANR_NODE`:** 관성 응답(변위/속도/가속도)의 기준점 설정입니다. 절점 결과·변위 결과에서 사용합니다.

### 공통 Response 구조

```json
{
  "<TEXT_TYPE>": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."], ["2", "..."]]
  }
}
```

---

### A-1. Time History Text – Node Results

> **기능:** 시간이력 해석에서 절점(Node)의 **변위·속도·가속도**를 시간 스텝별로 추출합니다.

#### `TEXT_TYPE`

| 값 | 설명 |
|----|------|
| `"TH_DISP"` | 변위(Displacement) |
| `"TH_VELOCITY"` | 속도(Velocity) |
| `"TH_ACCEL"` | 가속도(Acceleration) |

#### Response HEAD

`["Index", "Node", "Load", "Time/Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"]`

#### Request / Response JSON

**POST Request Body — 변위(TH_DISP)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_DISP",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_Displacement_Out.JSON",
    "UNIT": { "FORCE": "N", "DIST": "MM" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Node", "Load", "Time/Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "NODE_ELEMS": { "KEYS": [10] },
    "TH_CASE_NAME": ["Elcent"],
    "STEP": { "FROM": 0.1, "TO": 0.5, "STEPS": 1 },
    "REF_PT": "Ground"
  }
}
```

**POST Response Body**

```json
{
  "TH_DISP": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Node", "Load", "Time/Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "DATA": [
      ["1", "10", "Elcent", "0.100", "-0.212573", "-0.367424", "-0.374784", "0.000018", "-0.000011", "0.000022"],
      ["2", "10", "Elcent", "0.200", "-0.748871", "-1.793398", "-1.889303", "0.000136", "-0.000116", "0.000139"],
      ["3", "10", "Elcent", "0.300", "-2.190583", "-6.156868", "-6.706040", "0.000636", "-0.000576", "0.000505"],
      ["4", "10", "Elcent", "0.400", "-2.740721", "-12.268332", "-14.108861", "0.001874", "-0.001677", "0.001110"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 절점 10번의 시간이력 변위를 0.1~0.5초 구간에서 추출 ─────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "TH_DISP",                 # 변위 결과
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [10]},           # 절점 10번
        "TH_CASE_NAME": ["Elcent"],             # 시간이력 하중케이스명
        "STEP": {"FROM": 0.1, "TO": 0.5, "STEPS": 1},
        "REF_PT": "Ground",                     # 기준점: 지반
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
table = res["TH_DISP"]
print("HEAD:", table["HEAD"])
for row in table["DATA"]:
    print(f"  t={row[3]}s  Dx={row[4]}  Dy={row[5]}  Dz={row[6]}")
```

---

### A-2. Time History Text – Element Result(Truss, Beam, Plane Stress/Strain, Solid)

> **기능:** 시간이력 해석의 **트러스·보·평면응력·평면변형·솔리드** 요소 부재력/응력을 추출합니다. 10개의 `TEXT_TYPE`이 있으며, 각 타입마다 응답 `HEAD`가 다릅니다.

#### `TEXT_TYPE` 및 Response HEAD

| `TEXT_TYPE` | 설명 | Response `HEAD` |
|-------------|------|-----------------|
| `"TH_TRUSSFORCE"` | 트러스 부재력 | `["Index", "Elem", "Load", "Time/Step", "Force-I", "Force-J"]` |
| `"TH_TRUSSSTRESS"` | 트러스 응력 | `["Index", "Elem", "Load", "Time/Step", "Stress-I", "Stress-J"]` |
| `"TH_BEAMFORCE"` | 보 부재력 | `["Index", "Elem", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]` |
| `"TH_BEAMSTRESS"` | 보 응력 | `["Index", "Elem", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)"]` |
| `"TH_PLANE_STRESS_FORCE"` | 평면응력 부재력 | `["Index", "Elem", "Load", "Time/Step", "Part", "Fx", "Fy"]` |
| `"TH_PLANESTRESS"` | 평면응력 응력 | `["Index", "Elem", "Load", "Time/Step", "Part", "Sig-xx", "Sig-yy", "Sig-xy"]` |
| `"TH_PLANE_STRAIN_FORCE"` | 평면변형 부재력 | `["Index", "Elem", "Load", "Time/Step", "Part", "Fx", "Fy", "Fz"]` |
| `"TH_PLANE_STRAIN_STRESS"` | 평면변형 응력 | `["Index", "Elem", "Load", "Time/Step", "Part", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy"]` |
| `"TH_SOLIDFORCE"` | 솔리드 부재력 | `["Index", "Elem", "Load", "Time/Step", "Part", "Fx", "Fy", "Fz"]` |
| `"TH_SOLIDSTRESS"` | 솔리드 응력 | `["Index", "Elem", "Load", "Time/Step", "Part", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-yz", "Sig-xz"]` |

#### Request / Response JSON

**POST Request Body — 보 부재력(TH_BEAMFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_BEAMFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_BeamForce_Out.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Part", "Time/Step", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [5] },
    "PARTS": ["PartI", "PartJ"],
    "TH_CASE_NAME": ["Elcent"],
    "STEP": { "FROM": 0.1, "TO": 0.5, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "TH_BEAMFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "5", "Elcent", "0.100", "I[10]", "2.856739", "-1.766507", "0.146287", "-0.353369", "0.592988", "-2.089716"],
      ["2", "5", "Elcent", "0.100", "J[34]", "2.856739", "-1.766507", "0.146287", "-0.353369", "0.519845", "-1.206463"],
      ["3", "5", "Elcent", "0.200", "I[10]", "11.636477", "-6.609388", "0.440853", "-1.620535", "3.932866", "-7.363094"],
      ["4", "5", "Elcent", "0.200", "J[34]", "11.636477", "-6.609388", "0.440853", "-1.620535", "3.712440", "-4.058400"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 보 요소 5번의 I/J 단면 부재력 시간이력 추출 ─────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "TH_BEAMFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [5]},
        "PARTS": ["PartI", "PartJ"],            # 요소 결과 출력 위치
        "TH_CASE_NAME": ["Elcent"],
        "STEP": {"FROM": 0.1, "TO": 0.5, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
for row in res["TH_BEAMFORCE"]["DATA"]:
    print(f"  elem {row[1]} {row[4]} t={row[3]}  Axial={row[5]}  My={row[9]}")
```

---

### A-3. Time History Text – Element Result(Plate)

> **기능:** 시간이력 해석의 **평판(Plate)** 요소 부재력·단위 부재력·응력을 추출합니다.

#### `TEXT_TYPE` 및 Response HEAD

| `TEXT_TYPE` | 설명 | Response `HEAD` |
|-------------|------|-----------------|
| `"TH_PLATEFORCE"` | 판 부재력 | `["Index", "Elem", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"]` |
| `"TH_PLATE_UNIT_FORCE"` | 판 단위 부재력 | `["Index", "Elem", "Load", "Time/Step", "Part", "Fxx", "Fyy", "Fxy", "Mxx", "Myy", "Mxy", "Vxx", "Vyy"]` |
| `"TH_PLATESTRESS"` | 판 응력 | `["Index", "Elem", "Load", "Time/Step", "Part", "Sig-xx(Top)", "Sig-yy(Top)", "Sig-xy(Top)", "Sig-xx(Bot)", "Sig-yy(Bot)", "Sig-xy(Bot)"]` |

#### Request / Response JSON

**POST Request Body — 판 부재력(TH_PLATEFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_PLATEFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_PlateForce_Out.JSON",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "NODE_ELEMS": { "KEYS": [51] },
    "PARTS": ["PartI", "PartJ", "PartK", "PartL"],
    "TH_CASE_NAME": ["Elcent"],
    "STEP": { "FROM": 0.1, "TO": 0.3, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "TH_PLATEFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "DATA": [
      ["1", "51", "Elcent", "0.100", "I", "0.383964", "1.085381", "-0.000122", "-0.000976", "0.000148", "0.000000"],
      ["2", "51", "Elcent", "0.100", "J", "0.376184", "-0.912407", "-0.000206", "-0.000988", "-0.000230", "0.000000"],
      ["3", "51", "Elcent", "0.100", "K", "-0.356719", "-0.607889", "0.000128", "-0.000000", "-0.000092", "0.000000"],
      ["4", "51", "Elcent", "0.100", "L", "-0.403429", "0.434915", "0.000200", "-0.000000", "-0.000059", "0.000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 판 요소 51번의 4절점(I,J,K,L) 판 응력 시간이력 추출 ───────────
payload = {
    "Argument": {
        "TEXT_TYPE": "TH_PLATESTRESS",          # 판 응력
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "NODE_ELEMS": {"KEYS": [51]},
        "PARTS": ["PartI", "PartJ", "PartK", "PartL"],
        "TH_CASE_NAME": ["Elcent"],
        "STEP": {"FROM": 0.1, "TO": 0.3, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
print("HEAD:", res["TH_PLATESTRESS"]["HEAD"])
print("rows:", len(res["TH_PLATESTRESS"]["DATA"]))
```

---

### A-4. Time History Text – Element Result(Wall)

> **기능:** 시간이력 해석의 **벽체(Wall)** 요소 부재력을 추출합니다.

#### `TEXT_TYPE`

| 값 | 설명 |
|----|------|
| `"TH_WALLFORCE"` | 벽체 부재력 |

#### Response HEAD

`["Index", "WallID", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

#### Request / Response JSON

**POST Request Body — 벽체 부재력(TH_WALLFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_WALLFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_WallForce_Out.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "M" },
    "STYLES": { "FORMAT": "Exponential", "PLACE": 3 },
    "COMPONENTS": ["WallID", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [12] },
    "PARTS": ["PartI", "PartJ"],
    "TH_CASE_NAME": ["EQ1"],
    "STEP": { "FROM": 0.1, "TO": 0.18, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "TH_WALLFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "WallID", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "12", "EQ1", "0.100", "I[308]", "-4.386e+02", "0.000e+00", "6.012e+00", "0.000e+00", "1.492e+02", "0.000e+00"],
      ["2", "12", "EQ1", "0.100", "J[314]", "-4.386e+02", "0.000e+00", "6.012e+00", "0.000e+00", "1.323e+02", "0.000e+00"],
      ["3", "12", "EQ1", "0.120", "I[308]", "-4.381e+02", "0.000e+00", "6.313e+00", "0.000e+00", "1.491e+02", "0.000e+00"],
      ["4", "12", "EQ1", "0.120", "J[314]", "-4.381e+02", "0.000e+00", "6.313e+00", "0.000e+00", "1.314e+02", "0.000e+00"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 벽체 12번의 부재력 시간이력을 지수(Exponential) 형식으로 추출 ──
payload = {
    "Argument": {
        "TEXT_TYPE": "TH_WALLFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "M"},
        "STYLES": {"FORMAT": "Exponential", "PLACE": 3},
        "NODE_ELEMS": {"KEYS": [12]},
        "PARTS": ["PartI", "PartJ"],
        "TH_CASE_NAME": ["EQ1"],
        "STEP": {"FROM": 0.1, "TO": 0.18, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
for row in res["TH_WALLFORCE"]["DATA"]:
    print(f"  Wall {row[1]} {row[4]} t={row[3]}  Axial={row[5]}")
```

---

### A-5. Time History Text – General Link Result

> **기능:** 시간이력 해석의 **일반 링크(General Link)** 부재력과 변형을 추출합니다.

#### `TEXT_TYPE` 및 Response HEAD

| `TEXT_TYPE` | 설명 | Response `HEAD` |
|-------------|------|-----------------|
| `"TH_GLINKFORCE"` | 일반링크 부재력 | `["Index", "Key", "Node1", "Node2", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"]` |
| `"TH_GLINKDEFORM"` | 일반링크 변형 | `["Index", "Key", "Node1", "Node2", "Load", "Time/Step", "DX", "DY", "DZ", "RX", "RY", "RZ"]` |

#### Request / Response JSON

**POST Request Body — 일반링크 변형(TH_GLINKDEFORM)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_GLINKDEFORM",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_GlinkDeform_Out.JSON",
    "UNIT": { "FORCE": "N", "DIST": "MM" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Key", "Node1", "Node2", "Load", "Time/Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "TH_CASE_NAME": ["Elcent"],
    "STEP": { "FROM": 0.1, "TO": 0.5, "STEPS": 1 }
  }
}
```

**POST Response Body — 일반링크 부재력(TH_GLINKFORCE)**

```json
{
  "TH_GLINKFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Key", "Node1", "Node2", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "DATA": [
      ["1", "1", "18", "10", "Elcent", "0.100", "I", "-1.216319", "1.099123", "-0.941257", "0.274092", "-0.408692", "-1.029260"],
      ["2", "1", "18", "10", "Elcent", "0.100", "J", "-1.216319", "1.099123", "-0.941257", "0.274092", "-0.408692", "-1.029260"],
      ["3", "1", "18", "10", "Elcent", "0.200", "I", "-2.712090", "2.257943", "-1.365132", "1.280736", "-1.921911", "-0.327463"],
      ["4", "1", "18", "10", "Elcent", "0.200", "J", "-2.712090", "2.257943", "-1.365132", "1.280736", "-1.921911", "-0.327463"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 일반링크 1번의 변형 시간이력 추출 ─────────────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "TH_GLINKDEFORM",
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [1]},
        "TH_CASE_NAME": ["Elcent"],
        "STEP": {"FROM": 0.1, "TO": 0.5, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
tbl = res["TH_GLINKDEFORM"]
print("HEAD:", tbl["HEAD"])
```

---

### A-6. Pushover Text – Displacement

> **기능:** 푸시오버(Pushover) 해석에서 절점의 변위를 스텝별로 추출합니다. 하중케이스는 `PO_CASE_NAME`으로 지정합니다.

#### `TEXT_TYPE`

| 값 | 설명 |
|----|------|
| `"PO_DISP"` | 푸시오버 변위(Displacement) |

#### Response HEAD

`["Index", "Node", "Load", "Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"]`

#### Request / Response JSON

**POST Request Body — 푸시오버 변위(PO_DISP)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_DISP",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_Displacement_Out.JSON",
    "UNIT": { "FORCE": "N", "DIST": "MM" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Node", "Load", "Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "NODE_ELEMS": { "KEYS": [22] },
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 10, "STEPS": 1 },
    "REF_PT": "Ground"
  }
}
```

**POST Response Body**

```json
{
  "PO_DISP": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Node", "Load", "Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "DATA": [
      ["1", "22", "PX", "1", "-4.986447", "0.000000", "-0.017857", "0.000000", "0.000403", "0.000000"],
      ["2", "22", "PX", "2", "-9.972893", "0.000000", "-0.035714", "0.000000", "0.000806", "0.000000"],
      ["3", "22", "PX", "3", "-14.959340", "0.000000", "-0.053572", "0.000000", "0.001210", "0.000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 절점 22번(제어점)의 푸시오버 변위 곡선을 스텝 1~10에서 추출 ────
payload = {
    "Argument": {
        "TEXT_TYPE": "PO_DISP",
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [22]},
        "PO_CASE_NAME": ["PX"],                 # 푸시오버 하중케이스
        "STEP": {"FROM": 1, "TO": 10, "STEPS": 1},
        "REF_PT": "Ground",
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
for row in res["PO_DISP"]["DATA"]:
    print(f"  step {row[3]}  Dx={row[4]}")
```

---

### A-7. Pushover Text – Element Result(Beam, Truss)

> **기능:** 푸시오버 해석의 **보·트러스** 요소 부재력/응력을 스텝별로 추출합니다.

#### `TEXT_TYPE` 및 Response HEAD

| `TEXT_TYPE` | 설명 | Response `HEAD` |
|-------------|------|-----------------|
| `"PO_BEAMFORCE"` | 보 부재력 | `["Index", "Elem", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]` |
| `"PO_BEAMSTRESS"` | 보 응력 | `["Index", "Elem", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z"]` |
| `"PO_TRUSSFORCE"` | 트러스 부재력 | `["Index", "Elem", "Load", "Force-I", "Force-J"]` |
| `"PO_TRUSSSTRESS"` | 트러스 응력 | `["Index", "Elem", "Load", "Step", "Stress-I", "Stress-J"]` |

#### Request / Response JSON

**POST Request Body — 보 부재력(PO_BEAMFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_BEAMFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_BeamForce_Out.JSON",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Part", "Step", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [16] },
    "PARTS": ["PartI", "PartJ"],
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 5, "STEPS": 1 }
  }
}
```

**POST Response Body — 트러스 부재력(PO_TRUSSFORCE)**

```json
{
  "PO_TRUSSFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Force-I", "Force-J"],
    "DATA": [
      ["1", "40", "PX", "12.345678", "12.345678"],
      ["2", "40", "PX", "24.691356", "24.691356"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 보 요소 16번의 푸시오버 부재력을 스텝 1~5에서 추출 ─────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "PO_BEAMFORCE",
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [16]},
        "PARTS": ["PartI", "PartJ"],
        "PO_CASE_NAME": ["PX"],
        "STEP": {"FROM": 1, "TO": 5, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
print("rows:", len(res["PO_BEAMFORCE"]["DATA"]))
```

---

### A-8. Pushover Text – Element Result(Wall)

> **기능:** 푸시오버 해석의 **벽체(Wall)** 요소 부재력을 스텝별로 추출합니다.

#### `TEXT_TYPE`

| 값 | 설명 |
|----|------|
| `"PO_WALLFORCE"` | 벽체 부재력 |

#### Response HEAD

`["Index", "WallID", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

#### Request / Response JSON

**POST Request Body — 벽체 부재력(PO_WALLFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_WALLFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_WallForce_Out.JSON",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Exponential", "PLACE": 3 },
    "COMPONENTS": ["WallID", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [12] },
    "PARTS": ["PartI", "PartJ"],
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 4, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "PO_WALLFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "WallID", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "12", "PX", "1", "I[308]", "-2.045e+02", "0.000e+00", "6.953e+01", "0.000e+00", "-6.679e+01", "0.000e+00"],
      ["2", "12", "PX", "1", "J[314]", "-2.045e+02", "0.000e+00", "6.953e+01", "0.000e+00", "1.279e+02", "0.000e+00"],
      ["3", "12", "PX", "2", "I[308]", "-5.294e+01", "0.000e+00", "1.152e+02", "0.000e+00", "-1.675e+02", "0.000e+00"],
      ["4", "12", "PX", "2", "J[314]", "-5.294e+01", "0.000e+00", "1.152e+02", "0.000e+00", "1.551e+02", "0.000e+00"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 벽체 12번의 푸시오버 부재력 추출 ──────────────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "PO_WALLFORCE",
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Exponential", "PLACE": 3},
        "NODE_ELEMS": {"KEYS": [12]},
        "PARTS": ["PartI", "PartJ"],
        "PO_CASE_NAME": ["PX"],
        "STEP": {"FROM": 1, "TO": 4, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
print("HEAD:", res["PO_WALLFORCE"]["HEAD"])
```

---

### A-9. Pushover Text – General Link

> **기능:** 푸시오버 해석의 **일반 링크(General Link)** 부재력·변형을 스텝별로 추출합니다.

#### `TEXT_TYPE` 및 Response HEAD

| `TEXT_TYPE` | 설명 | Response `HEAD` |
|-------------|------|-----------------|
| `"PO_GLINKFORCE"` | 일반링크 부재력 | `["Index", "Key", "Node1", "Node2", "Load", "Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"]` |
| `"PO_GLINKDEFORM"` | 일반링크 변형 | `["Index", "Key", "Node1", "Node2", "Load", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"]` |

#### Request / Response JSON

**POST Request Body — 일반링크 변형(PO_GLINKDEFORM)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_GLINKDEFORM",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_GlinkDeform_Out.JSON",
    "UNIT": { "FORCE": "N", "DIST": "MM" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Key", "Node1", "Node2", "Load", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 5, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "PO_GLINKDEFORM": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Key", "Node1", "Node2", "Load", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "1", "18", "10", "PX", "1", "-0.010000", "0.000000", "0.000000", "0.000000", "0.000000", "0.000000"],
      ["2", "1", "18", "10", "PX", "2", "-0.020000", "0.000000", "0.000000", "0.000000", "0.000000", "0.000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 일반링크 1번의 푸시오버 부재력을 스텝별로 추출 ────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "PO_GLINKFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [1]},
        "PO_CASE_NAME": ["PX"],
        "STEP": {"FROM": 1, "TO": 5, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
print("HEAD:", res["PO_GLINKFORCE"]["HEAD"])
```

---

### A-10. Pushover Text – Elastic Link

> **기능:** 푸시오버 해석의 **탄성 링크(Elastic Link)** 부재력·변형을 스텝별로 추출합니다.

#### `TEXT_TYPE` 및 Response HEAD

| `TEXT_TYPE` | 설명 | Response `HEAD` |
|-------------|------|-----------------|
| `"PO_ELINKFORCE"` | 탄성링크 부재력 | `["Index", "Key", "Node1", "Node2", "Load", "Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"]` |
| `"PO_ELINKDEFORM"` | 탄성링크 변형 | `["Index", "Key", "Node1", "Node2", "Load", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"]` |

#### Request / Response JSON

**POST Request Body — 탄성링크 부재력(PO_ELINKFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_ELINKFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_ElinkForce_Out.JSON",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Key", "Node1", "Node2", "Load", "Part", "Step", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "PARTS": ["PartI", "PartJ"],
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 5, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "PO_ELINKFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Key", "Node1", "Node2", "Load", "Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "DATA": [
      ["1", "1", "16", "4", "PX", "1", "I", "0.000000", "0.000060", "0.000547", "-0.063083", "0.000000", "0.000000"],
      ["2", "1", "16", "4", "PX", "1", "J", "0.000000", "0.000060", "0.000547", "-0.063083", "0.000000", "0.000000"],
      ["3", "1", "16", "4", "PX", "2", "I", "0.000000", "0.000060", "0.000547", "-0.063083", "0.000000", "0.000000"],
      ["4", "1", "16", "4", "PX", "2", "J", "0.000000", "0.000060", "0.000547", "-0.063083", "0.000000", "0.000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 탄성링크 1번의 푸시오버 변형 추출 ────────────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "PO_ELINKDEFORM",
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [1]},
        "PO_CASE_NAME": ["PX"],
        "STEP": {"FROM": 1, "TO": 5, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
print("HEAD:", res["PO_ELINKDEFORM"]["HEAD"])
```

---

## 그룹 B. Inelastic Hinge 시간이력 결과 테이블 (`post/TABLE`)

비탄성 힌지(Inelastic Hinge)의 시간이력 결과를 테이블로 추출합니다. 이 그룹은 **19장의 `post/TABLE` 공통 구조와 동일**하며, `"Argument"` 객체에서 `TABLE_TYPE`으로 테이블 종류를 선택합니다.

### Input URI (그룹 B 공통)

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 공통 Request 구조 (19장 공통과 동일)

19장과 동일하게 `TABLE_NAME`·`TABLE_TYPE`·`EXPORT_PATH`·`UNIT`(FORCE/DIST)·`STYLES`(FORMAT/PLACE)·`COMPONENTS`·`NODE_ELEMS`(KEYS/TO/STRUCTURE_GROUP_NAME)를 사용합니다. 하중케이스만 시간이력 전용 키를 사용한다는 점이 다릅니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 결과 테이블 제목 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 (각 절 참조) | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 단위 (`FORCE`/`DIST`) | `"UNIT"` | Object | System | Optional |
| 5 | 숫자 형식 (`FORMAT`/`PLACE`) | `"STYLES"` | Object | System | Optional |
| 6 | 표시 열 | `"COMPONENTS"` | Array [String] | All | Optional |
| 7 | 요소 지정 (`KEYS`/`TO`/`STRUCTURE_GROUP_NAME`) | `"NODE_ELEMS"` | Object | All | Optional |
| 8 | **시간이력 하중케이스명** | `"TH_LOAD_CASE_NAMES"` | Array [String] | All | Optional |

> **`TH_LOAD_CASE_NAMES` 접미사 규칙:** `NAME(all)`(전체 스텝), `NAME(TH:max)`(최대 포락), `NAME(TH:min)`(최소 포락), `NAME(max)` / `NAME(min)` 형태를 사용합니다.

### `TABLE_TYPE` 접미사(힌지 유형) 공통 의미

| 접미사 | 의미 |
|--------|------|
| `LUMPED` | 집중형(Lumped) 힌지 |
| `DIST` | 분포형(Distributed) 힌지 |
| `SPRING` | 스프링(Spring) 힌지 |
| `TRUSS` | 트러스(Truss) 힌지 |
| `WALL` | 벽체(Wall) 힌지 |

### 공통 Response 구조

```json
{
  "<TABLE_NAME>": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."]]
  }
}
```

---

### B-1. Inelastic Hinge Event Time

> **기능:** 비탄성 힌지의 **1차/2차/3차 항복 발생 시각(Event Time)** 을 6개 성분(Dx~Rz)별로 추출합니다.

#### `TABLE_TYPE`

| 값 | 힌지 유형 |
|----|-----------|
| `"IEHG_EVENT_TIME_LUMPED"` | 집중형 |
| `"IEHG_EVENT_TIME_DIST"` | 분포형 |
| `"IEHG_EVENT_TIME_SPRING"` | 스프링 |
| `"IEHG_EVENT_TIME_TRUSS"` | 트러스 |
| `"IEHG_EVENT_TIME_WALL"` | 벽체 |

#### Response HEAD (힌지 유형별)

- **Lumped / Dist / Spring:** `["Index", "Elem", "HingeLocation", "Load", "1stYield/Dx", "1stYield/Dy", "1stYield/Dz", "1stYield/Rx", "1stYield/Ry", "1stYield/Rz", "2ndYield/Dx", "2ndYield/Dy", "2ndYield/Dz", "2ndYield/Rx", "2ndYield/Ry", "2ndYield/Rz", "3rdYield/Dx", "3rdYield/Dy", "3rdYield/Dz", "3rdYield/Rx", "3rdYield/Ry", "3rdYield/Rz"]`
- **Truss:** `["Index", "Elem", "InelasticHingeProp.", "Load", "1stYield/Dx", "2ndYield/Dx", "3rdYield/Dx"]`
- **Wall:** `["Index", "WallID", "Story", "HingeLocation", "Load", "1stYield/Dx", ... , "3rdYield/Rz"]` (Lumped 열 앞에 `Story`·`WallID` 추가)
- **General Link 성분(Spring 계열):** `["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "1stYield/Dx", ... , "3rdYield/Rz"]`

#### Request / Response JSON

**POST Request Body — 집중형(IEHG_EVENT_TIME_LUMPED)**

```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_EVENT_TIME_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": [
      "Elem", "HingeLocation", "Load",
      "1stYield/Dx", "1stYield/Dy", "1stYield/Dz", "1stYield/Rx", "1stYield/Ry", "1stYield/Rz",
      "2ndYield/Dx", "2ndYield/Dy", "2ndYield/Dz", "2ndYield/Rx", "2ndYield/Ry", "2ndYield/Rz",
      "3rdYield/Dx", "3rdYield/Dy", "3rdYield/Dz", "3rdYield/Rx", "3rdYield/Ry", "3rdYield/Rz"
    ],
    "TH_LOAD_CASE_NAMES": ["Elcent"]
  }
}
```

**POST Response Body**

```json
{
  "Lumped": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "HingeLocation", "Load", "1stYield/Dx", "1stYield/Dy", "1stYield/Dz", "1stYield/Rx", "1stYield/Ry", "1stYield/Rz", "2ndYield/Dx", "2ndYield/Dy", "2ndYield/Dz", "2ndYield/Rx", "2ndYield/Ry", "2ndYield/Rz", "3rdYield/Dx", "3rdYield/Dy", "3rdYield/Dz", "3rdYield/Rx", "3rdYield/Ry", "3rdYield/Rz"],
    "DATA": [
      ["1", "3", "Center", "Elcent(all)", "1.100000023842", "-", "-", "-", "-", "-", "1.100000023842", "-", "-", "-", "-", "-", "0.000000000000", "-", "-", "-", "-", "-"],
      ["2", "3", "I", "Elcent(all)", "-", "0.100000001490", "0.100000001490", "-", "0.300000011921", "0.300000011921", "-", "0.100000001490", "0.100000001490", "-", "0.500000000000", "0.500000000000", "-", "0.000000000000", "0.000000000000", "-", "0.000000000000", "0.000000000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 집중형 힌지의 항복 이벤트 시각 테이블 추출 ────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Lumped",
        "TABLE_TYPE": "IEHG_EVENT_TIME_LUMPED",  # 집중형 힌지
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 12},
        "TH_LOAD_CASE_NAMES": ["Elcent"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
tbl = res["Lumped"]
print("HEAD 개수:", len(tbl["HEAD"]), "/ DATA 행:", len(tbl["DATA"]))
```

---

### B-2. Inelastic Hinge Beam Summary

> **기능:** 비탄성 보(Beam) 힌지의 **성분별(Dx/Dy/Dz/Ry/Rz) 요약** 을 추출합니다. 변형·부재력·연성도·상태(Status)·성능(Performance)을 한 테이블에 제공합니다.

#### `TABLE_TYPE`

| 값 | 성분 |
|----|------|
| `"IEHG_BEAM_SUM_DX"` | Dx |
| `"IEHG_BEAM_SUM_DY"` | Dy |
| `"IEHG_BEAM_SUM_DZ"` | Dz |
| `"IEHG_BEAM_SUM_RY"` | Ry |
| `"IEHG_BEAM_SUM_RZ"` | Rz |

#### Response HEAD

`["Index", "Type", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"]`

#### Request / Response JSON

**POST Request Body — Dx 성분(IEHG_BEAM_SUM_DX)**

```json
{
  "Argument": {
    "TABLE_NAME": "Dx",
    "TABLE_TYPE": "IEHG_BEAM_SUM_DX",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Type", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "NODE_ELEMS": { "KEYS": [2, 3] },
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Dx": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Type", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "DATA": [
      ["1", "Distributed", "2", "1-Pos", "Column-1", "Elcent(max)", "3.099999904633", "0.004527841229", "3173.563500000000", "36.361083984375", "25.025245666504", "2ndYield", "5~Level", "672.750118000000", "825.120000000000", "-", "0.000124524377", "0.000180930947", "-"],
      ["2", "Lumped", "3", "Center", "Column", "Elcent(max)", "3.099999904633", "0.004969955422", "3412.418000000000", "39.911506652832", "27.468795776367", "2ndYield", "5~Level", "672.750118000000", "825.120000000000", "-", "0.000124524377", "0.000180930947", "-"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 보 힌지 요소 2,3번의 Dx 요약(포락 max/min)을 추출 ─────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Dx",
        "TABLE_TYPE": "IEHG_BEAM_SUM_DX",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [2, 3]},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
for row in res["Dx"]["DATA"]:
    # Status=11번째, Performance=12번째 열
    print(f"  elem {row[2]} {row[3]}: {row[11]} / {row[12]}")
```

---

### B-3. Inelastic Hinge Truss Summary

> **기능:** 비탄성 트러스(Truss) 힌지의 요약(Dx)을 추출합니다.

#### `TABLE_TYPE`

| 값 | 성분 |
|----|------|
| `"IEHG_TRUSS_SUM_DX"` | Dx |

#### Response HEAD

`["Index", "Truss/Elem", "Truss/Node1", "Truss/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"]`

#### Request / Response JSON

**POST Request Body — Dx(IEHG_TRUSS_SUM_DX)**

```json
{
  "Argument": {
    "TABLE_NAME": "Dx",
    "TABLE_TYPE": "IEHG_TRUSS_SUM_DX",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Truss/Elem", "Truss/Node1", "Truss/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "NODE_ELEMS": { "KEYS": [49] },
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Dx": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Truss/Elem", "Truss/Node1", "Truss/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "DATA": [
      ["1", "49", "54", "57", "Truss", "Elcent(min)", "1.799999952316", "-0.000726116123", "-841.719187500000", "0.123781532049", "0.123781532049", "Elastic", "0~1Level", "-0.500000000000", "-1.000000000000", "-", "-0.005866110325", "-0.005866110325", "-"],
      ["2", "49", "54", "57", "Truss", "Elcent(max)", "2.099999904633", "0.001163915265", "832.173000000000", "1.557814478874", "1.072154164314", "2ndYield", "2~3Level", "0.500000000000", "1.000000000000", "-", "0.000747146260", "0.001085585682", "-"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 트러스 힌지 49번의 Dx 요약 추출 ──────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Dx",
        "TABLE_TYPE": "IEHG_TRUSS_SUM_DX",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [49]},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
print("rows:", len(res["Dx"]["DATA"]))
```

---

### B-4. Inelastic Hinge General Link Summary

> **기능:** 비탄성 일반링크(General Link) 힌지의 성분별(Dx/Dy/Dz/Rx/Ry/Rz) 요약을 추출합니다.

#### `TABLE_TYPE`

| 값 | 성분 |
|----|------|
| `"IEHG_GL_LINK_SUM_DX"` | Dx |
| `"IEHG_GL_LINK_SUM_DY"` | Dy |
| `"IEHG_GL_LINK_SUM_DZ"` | Dz |
| `"IEHG_GL_LINK_SUM_RX"` | Rx |
| `"IEHG_GL_LINK_SUM_RY"` | Ry |
| `"IEHG_GL_LINK_SUM_RZ"` | Rz |

#### Response HEAD

`["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"]`

#### Request / Response JSON

**POST Request Body — Dx(IEHG_GL_LINK_SUM_DX)**

```json
{
  "Argument": {
    "TABLE_NAME": "Dx",
    "TABLE_TYPE": "IEHG_GL_LINK_SUM_DX",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Dx": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "DATA": [
      ["1", "1", "GL_1", "18", "10", "GeneralLink", "Elcent(min)", "2.000000000000", "-0.669099271297", "-669.949250000000", "13381.985351562500", "4460.661621093750", "2ndYield", "3~4Level", "-0.500000000000", "-1.000000000000", "-", "-0.000049999999", "-0.000150000007", "-"],
      ["2", "1", "GL_1", "18", "10", "GeneralLink", "Elcent(max)", "2.400000095367", "0.500326693058", "499.476687500000", "10006.534179687500", "3335.511230468750", "2ndYield", "5~Level", "0.500000000000", "1.000000000000", "-", "0.000049999999", "0.000150000007", "-"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 일반링크 힌지의 Dx 요약(포락)을 추출 ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Dx",
        "TABLE_TYPE": "IEHG_GL_LINK_SUM_DX",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
print("HEAD:", res["Dx"]["HEAD"])
```

---

### B-5. Inelastic Hinge Force

> **기능:** 비탄성 힌지의 **최대 부재력(Force)과 발생 시각(Time)** 을 6개 성분(Fx~Mz)별로 추출합니다.

#### `TABLE_TYPE`

| 값 | 힌지 유형 |
|----|-----------|
| `"IEHG_FORCE_LUMPED"` | 집중형 |
| `"IEHG_FORCE_DIST"` | 분포형 |
| `"IEHG_FORCE_SPRING"` | 스프링 |
| `"IEHG_FORCE_TRUSS"` | 트러스 |
| `"IEHG_FORCE_WALL"` | 벽체 |

#### Response HEAD (힌지 유형별)

- **Lumped / Dist:** `["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time", "Fy/Force", "Fy/Time", "Fz/Force", "Fz/Time", "Mx/Force", "Mx/Time", "My/Force", "My/Time", "Mz/Force", "Mz/Time"]`
- **Spring:** `["Index", "Elem", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time"]`
- **Wall:** `["Index", "WallID", "Story", "HingeLocation", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time", ... , "Mz/Force", "Mz/Time"]`
- **Truss:** `["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time", ... , "Mz/Force", "Mz/Time"]`

#### Request / Response JSON

**POST Request Body — 집중형(IEHG_FORCE_LUMPED)**

```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_FORCE_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time", "Fy/Force", "Fy/Time", "Fz/Force", "Fz/Time", "Mx/Force", "Mx/Time", "My/Force", "My/Time", "Mz/Force", "Mz/Time"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Lumped": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time", "Fy/Force", "Fy/Time", "Fz/Force", "Fz/Time", "Mx/Force", "Mx/Time", "My/Force", "My/Time", "Mz/Force", "Mz/Time"],
    "DATA": [
      ["1", "3", "Center", "Column", "Elcent(max)", "3412.418000000000", "3.099999904633", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
      ["2", "3", "I", "Column", "Elcent(max)", "-", "-", "750.083437500000", "3.200000047684", "902.629812500000", "2.599999904633", "-", "-", "2828.398250000000", "2.599999904633", "3067.439000000000", "2.099999904633"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 집중형 힌지의 최대 부재력/발생시각 테이블 추출 ────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Lumped",
        "TABLE_TYPE": "IEHG_FORCE_LUMPED",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
print("rows:", len(res["Lumped"]["DATA"]))
```

---

### B-6. Inelastic Hinge Deformation

> **기능:** 비탄성 힌지의 **최대 변형(Deform)과 발생 시각(Time)** 을 6개 성분(Dx~Rz)별로 추출합니다.

#### `TABLE_TYPE`

| 값 | 힌지 유형 |
|----|-----------|
| `"IEHG_DEFORM_LUMPED"` | 집중형 |
| `"IEHG_DEFORM_DIST"` | 분포형 |
| `"IEHG_DEFORM_SPRING"` | 스프링 |
| `"IEHG_DEFORM_TRUSS"` | 트러스 |
| `"IEHG_DEFORM_WALL"` | 벽체 |

#### Response HEAD (힌지 유형별)

- **Lumped / Dist:** `["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time", "Dy/Deform", "Dy/Time", "Dz/Deform", "Dz/Time", "Rx/Deform", "Rx/Time", "Ry/Deform", "Ry/Time", "Rz/Deform", "Rz/Time"]`
- **Spring:** `["Index", "Elem", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time"]`
- **Wall:** `["Index", "WallID", "Story", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time", ... , "Rz/Deform", "Rz/Time"]`
- **Truss:** `["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time", ... , "Rz/Deform", "Rz/Time"]`

#### Request / Response JSON

**POST Request Body — 집중형(IEHG_DEFORM_LUMPED)**

```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_DEFORM_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time", "Dy/Deform", "Dy/Time", "Dz/Deform", "Dz/Time", "Rx/Deform", "Rx/Time", "Ry/Deform", "Ry/Time", "Rz/Deform", "Rz/Time"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Lumped": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time", "Dy/Deform", "Dy/Time", "Dz/Deform", "Dz/Time", "Rx/Deform", "Rx/Time", "Ry/Deform", "Ry/Time", "Rz/Deform", "Rz/Time"],
    "DATA": [
      ["1", "3", "Center", "Column", "Elcent(max)", "0.004969955422", "3.099999904633", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
      ["2", "3", "I", "Column", "Elcent(max)", "-", "-", "0.003640656127", "3.200000047684", "0.004381065723", "2.599999904633", "-", "-", "0.053212597966", "2.599999904633", "0.057932153344", "2.099999904633"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 분포형 힌지의 변형 테이블을 추출 ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Distributed",
        "TABLE_TYPE": "IEHG_DEFORM_DIST",     # 분포형
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
key = next(iter(res))
print("table:", key, "/ rows:", len(res[key]["DATA"]))
```

---

### B-7. Inelastic Hinge Element Rotation

> **기능:** 비탄성 힌지 요소의 **회전(Rotation)과 발생 시각(Time)** 을 Ry·Rz 성분으로 추출합니다. 보와 벽체 두 유형이 있습니다.

#### `TABLE_TYPE`

| 값 | 유형 |
|----|------|
| `"IEHG_ELEM_ROT_BEAM"` | 보(Beam) 요소 회전 |
| `"IEHG_ELEM_ROT_WALL"` | 벽체(Wall) 요소 회전 |

#### Response HEAD (유형별)

- **Beam:** `["Index", "Elem", "Load", "Part", "Ry/Rotation", "Ry/Time", "Rz/Rotation", "Rz/Time"]`
- **Wall:** `["Index", "Story", "WallID", "Load", "Part", "Ry/Rotation", "Ry/Time", "Rz/Rotation", "Rz/Time"]`

#### Request / Response JSON

**POST Request Body — 보(IEHG_ELEM_ROT_BEAM)**

```json
{
  "Argument": {
    "TABLE_NAME": "Beam",
    "TABLE_TYPE": "IEHG_ELEM_ROT_BEAM",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Part", "Ry/Rotation", "Ry/Time", "Rz/Rotation", "Rz/Time"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Beam": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Ry/Rotation", "Ry/Time", "Rz/Rotation", "Rz/Time"],
    "DATA": [
      ["1", "2", "Elcent(max)", "I", "0.074839800000", "2.600000000000", "0.096699700000", "3.200000000000"],
      ["2", "2", "Elcent(max)", "J", "0.056081600000", "2.600000000000", "0.080104800000", "3.200000000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 보 요소의 소성 회전각(Ry/Rz)과 발생 시각 추출 ────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Beam",
        "TABLE_TYPE": "IEHG_ELEM_ROT_BEAM",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
for row in res["Beam"]["DATA"]:
    print(f"  elem {row[1]} {row[3]}  Ry={row[4]} (t={row[5]})  Rz={row[6]} (t={row[7]})")
```

---

### B-8. Inelastic Hinge Ductility Factor(D/D1)

> **기능:** 비탄성 힌지의 **연성도 계수 D/D1**(1차 항복 대비)의 최댓값과 발생 시각을 6개 성분별로 추출합니다.

#### `TABLE_TYPE`

| 값 | 힌지 유형 |
|----|-----------|
| `"IEHG_DUCT_D1_LUMPED"` | 집중형 |
| `"IEHG_DUCT_D1_DIST"` | 분포형 |
| `"IEHG_DUCT_D1_SPRING"` | 스프링 |
| `"IEHG_DUCT_D1_TRUSS"` | 트러스 |
| `"IEHG_DUCT_D1_WALL"` | 벽체 |

#### Response HEAD (힌지 유형별)

- **Lumped:** `["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max", "Dx/Time", "Dy/max", "Dy/Time", "Dz/max", "Dz/Time", "Rx/max", "Rx/Time", "Ry/max", "Ry/Time", "Rz/max", "Rz/Time"]`
- **Dist:** `["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max(D/D1)", "Dx/Time", "Dy/max(D/D1)", "Dy/Time", "Dz/max(D/D1)", "Dz/Time", "Rx/max(D/D1)", "Rx/Time", "Ry/max(D/D1)", "Ry/Time", "Rz/max(D/D1)", "Rz/Time"]`
- **Spring:** `["Index", "Elem", "InelasticHingeProp.", "Load", "Dx/max(D/D1)", "Dx/Time"]`
- **Wall:** `["Index", "WallID", "Story", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max", "Dx/Time", ... , "Rz/max", "Rz/Time"]`
- **Truss:** `["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Dx/max(D/D1)", "Dx/Time", ... , "Rz/max(D/D1)", "Rz/Time"]`

#### Request / Response JSON

**POST Request Body — 집중형(IEHG_DUCT_D1_LUMPED)**

```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_DUCT_D1_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max", "Dx/Time", "Dy/max", "Dy/Time", "Dz/max", "Dz/Time", "Rx/max", "Rx/Time", "Ry/max", "Ry/Time", "Rz/max", "Rz/Time"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Lumped": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max", "Dx/Time", "Dy/max", "Dy/Time", "Dz/max", "Dz/Time", "Rx/max", "Rx/Time", "Ry/max", "Ry/Time", "Rz/max", "Rz/Time"],
    "DATA": [
      ["1", "3", "Center", "Column", "Elcent(max)", "53.748348", "3.100000", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
      ["2", "3", "I", "Column", "Elcent(max)", "-", "-", "16.149096", "3.200000", "20.864525", "2.700000", "-", "-", "609.587769", "2.600000", "663.790100", "3.200000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 집중형 힌지 연성도 D/D1 테이블 추출 ──────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Lumped",
        "TABLE_TYPE": "IEHG_DUCT_D1_LUMPED",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
print("HEAD:", res["Lumped"]["HEAD"])
```

---

### B-9. Inelastic Hinge Ductility Factor(D/D2)

> **기능:** 비탄성 힌지의 **연성도 계수 D/D2**(2차 항복 대비)의 최댓값과 발생 시각을 6개 성분별로 추출합니다.

#### `TABLE_TYPE`

| 값 | 힌지 유형 |
|----|-----------|
| `"IEHG_DUCT_D2_LUMPED"` | 집중형 |
| `"IEHG_DUCT_D2_DIST"` | 분포형 |
| `"IEHG_DUCT_D2_SPRING"` | 스프링 |
| `"IEHG_DUCT_D2_TRUSS"` | 트러스 |
| `"IEHG_DUCT_D2_WALL"` | 벽체 |

#### Response HEAD (힌지 유형별)

- **Lumped:** `["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max(D/D2)", "Dx/Time", "Dy/max(D/D2)", "Dy/Time", "Dz/max(D/D2)", "Dz/Time", "Rx/max(D/D2)", "Rx/Time", "Ry/max(D/D2)", "Ry/Time", "Rz/max(D/D2)", "Rz/Time"]`
- **Dist / Wall:** `["Index", ... , "Dx/max", "Dx/Time", ... , "Rz/max", "Rz/Time"]` (Dist는 `Elem`, Wall은 `WallID`·`Story` 컬럼 사용)
- **Spring:** `["Index", "Elem", "InelasticHingeProp.", "Load", "Dx/max(D/D2)", "Dx/Time"]`
- **Truss:** `["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Dx/max(D/D2)", "Dx/Time", ... , "Rz/max(D/D2)", "Rz/Time"]`

#### Request / Response JSON

**POST Request Body — 집중형(IEHG_DUCT_D2_LUMPED)**

```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_DUCT_D2_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max", "Dx/Time", "Dy/max", "Dy/Time", "Dz/max", "Dz/Time", "Rx/max", "Rx/Time", "Ry/max", "Ry/Time", "Rz/max", "Rz/Time"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Lumped": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max(D/D2)", "Dx/Time", "Dy/max(D/D2)", "Dy/Time", "Dz/max(D/D2)", "Dz/Time", "Rx/max(D/D2)", "Rx/Time", "Ry/max(D/D2)", "Ry/Time", "Rz/max(D/D2)", "Rz/Time"],
    "DATA": [
      ["1", "3", "Center", "Column", "Elcent(max)", "27.468795776367", "3.099999904633", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
      ["2", "3", "I", "Column", "Elcent(max)", "-", "-", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "-", "-", "96.578498840332", "2.599999904633", "105.144279479980", "2.099999904633"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 벽체 힌지 연성도 D/D2 테이블 추출 ────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Wall",
        "TABLE_TYPE": "IEHG_DUCT_D2_WALL",     # 벽체 힌지
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
key = next(iter(res))
print("table:", key, "/ rows:", len(res[key]["DATA"]))
```

---

## 그룹 C. 수화열 해석 결과 표시 (`view/RESULTGRAPHIC`)

수화열(Heat of Hydration) 해석 결과는 테이블이 아니라 **모델 창의 그래픽(컨투어 등)** 으로 표시됩니다. 따라서 이 그룹은 `post/*`가 아닌 **`view/RESULTGRAPHIC`** 엔드포인트로 요청하며, 요청 구조는 **16장의 RESULTGRAPHIC 구조**를 그대로 재사용합니다.

### Input URI (그룹 C 공통)

```
{base url}/view/RESULTGRAPHIC
```

### Active Methods

`POST`

### 공통 Request 구조

| No. | 설명 | Key | Value 타입 | 비고 |
|-----|------|-----|-----------|------|
| 1 | 결과 그래픽 모드 (엔드포인트별 값, 각 절 참조) | `"CURRENT_MODE"` | String | **Required** |
| 2 | 하중케이스/조합 | `"LOAD_CASE_COMB"` | Object | — |
| 2-1 | └ 수화열 스텝 인덱스 | `LOAD_CASE_COMB.STEP_INDEX` | Integer | 수화열 해석 스텝 |
| 3 | 옵션 (일부 모드) | `"OPTIONS"` | Object | Stress 모드에서 사용 |
| 3-1 | └ 좌표계 (`"UCS"` / `"Local"`) | `OPTIONS.LOCAL_UCS.TYPE` | String | — |
| 3-2 | └ 응력 계산법 (`"Element"` / `"Avg.Nodal"`) | `OPTIONS.AVERAGE_NODAL.TYPE` | String | — |
| 4 | 성분 (일부 모드) | `"COMPONENTS"` | Object | Stress·Displacements 모드 |
| 4-1 | └ 성분명 | `COMPONENTS.COMP` | String | 모드별 enum |
| 5 | 벡터 옵션 (`COMP`가 `"Vector"`일 때) | `"VECTOR_OPTION"` | Object | — |
| 5-1 | └ 벡터 다이어그램 스케일 | `VECTOR_OPTION.SCALE_FACTOR_LENGTH` | Number | — |
| 6 | 표시 유형(컨투어/변형/범례 등, 16장 참조) | `"TYPE_OF_DISPLAY"` | Object | — |

> **참고:** `TYPE_OF_DISPLAY`의 상세 하위 키(`CONTOUR`·`VALUES`·`LEGEND`·`DEFORM`·`MIRRORED`·`CUTTING_PLANE`·`ISO_SURFACE` 등)는 **16장 `/view/RESULTGRAPHIC`** 매뉴얼을 참조하십시오. 아래 예시는 컨투어(`CONTOUR`) 기본 설정을 사용합니다.

### 공통 Response 구조

RESULTGRAPHIC은 그래픽 표시를 갱신하는 명령이므로, 응답은 결과 데이터가 아닌 갱신 메시지입니다(16장과 동일).

```json
{
  "RESULTGRAPHIC": "Result graphic display updated."
}
```

---

### C-1. Stress – Heat of Hydration

> **기능:** 수화열 해석의 **응력(Stress)** 결과를 지정 스텝에서 컨투어/벡터로 표시합니다.

- `CURRENT_MODE`: `"HY_STRESS"`
- `COMPONENTS.COMP` enum: `"Sig-XX"`, `"Sig-YY"`, `"Sig-ZZ"`, `"Sig-XY"`, `"Sig-YZ"`, `"Sig-XZ"`, `"Sig-P1"`, `"Sig-P2"`, `"Sig-P3"`, `"Tresca"`, `"Sig-EFF"`, `"Sig-Pmax"`, `"Sig-xx"`, `"Sig-yy"`, `"Sig-zz"`, `"Sig-xy"`, `"Sig-yz"`, `"Sig-xz"`, `"Vector"`

#### Request / Response JSON

**POST Request Body — 응력 컨투어(Sig-XX)**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_STRESS",
    "LOAD_CASE_COMB": { "STEP_INDEX": 1 },
    "OPTIONS": {
      "LOCAL_UCS": { "TYPE": "UCS" },
      "AVERAGE_NODAL": { "TYPE": "Element" }
    },
    "COMPONENTS": { "COMP": "Sig-XX" },
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

**POST Request Body — 응력 벡터(Vector)**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_STRESS",
    "LOAD_CASE_COMB": { "STEP_INDEX": 3 },
    "OPTIONS": {
      "LOCAL_UCS": { "TYPE": "Local" },
      "AVERAGE_NODAL": { "TYPE": "Element" }
    },
    "COMPONENTS": {
      "COMP": "Vector",
      "VECTOR_OPTION": { "SCALE_FACTOR_LENGTH": 1.0 }
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

**POST Response Body**

```json
{
  "RESULTGRAPHIC": "Result graphic display updated."
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 수화열 스텝 1의 Sig-XX 응력을 컨투어로 표시 ───────────────────
payload = {
    "Argument": {
        "CURRENT_MODE": "HY_STRESS",
        "LOAD_CASE_COMB": {"STEP_INDEX": 1},     # 수화열 해석 스텝 번호
        "OPTIONS": {
            "LOCAL_UCS": {"TYPE": "UCS"},
            "AVERAGE_NODAL": {"TYPE": "Element"},
        },
        "COMPONENTS": {"COMP": "Sig-XX"},
        "TYPE_OF_DISPLAY": {
            "CONTOUR": {"OPT_CHECK": True, "NUM_OF_COLOR": 12, "COLOR_TYPE": "rgb"}
        },
    }
}
res = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(res.json())   # {"RESULTGRAPHIC": "Result graphic display updated."}
```

---

### C-2. Temperature – Heat of Hydration

> **기능:** 수화열 해석의 **온도(Temperature)** 분포를 지정 스텝에서 컨투어로 표시합니다.

- `CURRENT_MODE`: `"HY_TEMPERATURE"`
- 성분(`COMPONENTS`) 없이 스텝(`STEP_INDEX`)만 지정합니다.

#### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_TEMPERATURE",
    "LOAD_CASE_COMB": { "STEP_INDEX": 1 },
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

**POST Response Body**

```json
{
  "RESULTGRAPHIC": "Result graphic display updated."
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 수화열 스텝별 온도 분포를 순차적으로 표시 ────────────────────
for step in range(1, 6):
    payload = {
        "Argument": {
            "CURRENT_MODE": "HY_TEMPERATURE",
            "LOAD_CASE_COMB": {"STEP_INDEX": step},
            "TYPE_OF_DISPLAY": {
                "CONTOUR": {"OPT_CHECK": True, "NUM_OF_COLOR": 12, "COLOR_TYPE": "rgb"}
            },
        }
    }
    res = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
    print(f"step {step}:", res.json())
```

---

### C-3. Displacements – Heat of Hydration

> **기능:** 수화열 해석의 **변위(Displacements)** 를 성분별로 지정 스텝에서 표시합니다.

- `CURRENT_MODE`: `"HY_DISPLACEMENTS"`
- `COMPONENTS.COMP` enum: `"DX"`, `"DY"`, `"DZ"`, `"RX"`, `"RY"`, `"RZ"`, `"DXY"`, `"DYZ"`, `"DXZ"`, `"DXYZ"`

#### Request / Response JSON

**POST Request Body — DX**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_DISPLACEMENTS",
    "LOAD_CASE_COMB": { "STEP_INDEX": 1 },
    "COMPONENTS": { "COMP": "DX" },
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

**POST Response Body**

```json
{
  "RESULTGRAPHIC": "Result graphic display updated."
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 수화열 변위 합(DXYZ)을 컨투어로 표시 ─────────────────────────
payload = {
    "Argument": {
        "CURRENT_MODE": "HY_DISPLACEMENTS",
        "LOAD_CASE_COMB": {"STEP_INDEX": 1},
        "COMPONENTS": {"COMP": "DXYZ"},          # 합변위
        "TYPE_OF_DISPLAY": {
            "CONTOUR": {"OPT_CHECK": True, "NUM_OF_COLOR": 12, "COLOR_TYPE": "rgb"}
        },
    }
}
res = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(res.json())
```

---

### C-4. Allowable Tensile Stress – Heat of Hydration

> **기능:** 수화열 해석의 **허용 인장응력(Allowable Tensile Stress)** 을 지정 스텝에서 컨투어로 표시합니다.

- `CURRENT_MODE`: `"HY_ALLOWABLETENSILESTRESS"`

#### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_ALLOWABLETENSILESTRESS",
    "LOAD_CASE_COMB": { "STEP_INDEX": 1 },
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

**POST Response Body**

```json
{
  "RESULTGRAPHIC": "Result graphic display updated."
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 수화열 허용 인장응력 컨투어 표시 ─────────────────────────────
payload = {
    "Argument": {
        "CURRENT_MODE": "HY_ALLOWABLETENSILESTRESS",
        "LOAD_CASE_COMB": {"STEP_INDEX": 1},
        "TYPE_OF_DISPLAY": {
            "CONTOUR": {"OPT_CHECK": True, "NUM_OF_COLOR": 12, "COLOR_TYPE": "rgb"}
        },
    }
}
res = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(res.json())
```

---

### C-5. Crack Ratio – Heat of Hydration

> **기능:** 수화열 해석의 **균열 지수(Crack Ratio)** 를 지정 스텝에서 컨투어로 표시합니다. 온도응력에 의한 균열 발생 위험을 평가할 때 사용합니다.

- `CURRENT_MODE`: `"HY_CRACKRATIO"`

#### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_CRACKRATIO",
    "LOAD_CASE_COMB": { "STEP_INDEX": 1 },
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

**POST Response Body**

```json
{
  "RESULTGRAPHIC": "Result graphic display updated."
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 최종 스텝의 균열지수를 컨투어로 표시 ─────────────────────────
payload = {
    "Argument": {
        "CURRENT_MODE": "HY_CRACKRATIO",
        "LOAD_CASE_COMB": {"STEP_INDEX": 10},
        "TYPE_OF_DISPLAY": {
            "CONTOUR": {"OPT_CHECK": True, "NUM_OF_COLOR": 12, "COLOR_TYPE": "rgb"}
        },
    }
}
res = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(res.json())
```

---

## 그룹 D. 시간이력 스마트 그래프 DB (`db/THR*`)

시간이력 결과를 **스마트 그래프(Smart Graph)** 로 추출하기 위한 정의 레코드를 생성/조회/수정/삭제하는 **CRUD DB 엔드포인트**입니다. 결과 테이블(그룹 A/B)과 달리, 이 그룹은 "어떤 요소·성분을 그래프로 뽑을지"를 데이터베이스에 등록합니다.

### 공통 사항 (그룹 D DB 엔드포인트)

| 메서드 | 동작 | URL |
|--------|------|-----|
| `POST` | 생성/갱신 (`"Assign"` 바디, ID 키) | `{base url}/db/THR*` |
| `GET` | 전체 조회 | `{base url}/db/THR*` |
| `GET` | 특정 ID 조회 | `{base url}/db/THR*/{id}` |
| `PUT` | 수정 (`"Assign"` 바디, ID 키) | `{base url}/db/THR*` |
| `DELETE` | 삭제 (특정 ID) | `{base url}/db/THR*/{id}` |

> **참고**
> - 요청 바디는 `"Assign"` 객체 아래에 **레코드 ID(문자열 키)** 로 항목을 정의합니다.
> - `GET` 응답은 URI 이름(`THRE`/`THRG`/`THRI`/`THRS`)을 최상위 키로 하여 ID별 레코드를 반환합니다.
> - `GET`은 URL 경로에 ID를 붙여 개별 조회할 수 있고, `DELETE`는 특정 ID를 삭제합니다.
> - `THIS_NAME`은 대상 **시간이력 하중케이스(Time History Load Case)** 이름입니다.

---

### D-1. Element Force Smart Graph – `db/THRE`

> **기능:** 요소 부재력(Element Force)을 시간이력 스마트 그래프로 추출하기 위한 레코드를 정의합니다.

#### Input URI

```
{base url}/db/THRE
```

#### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

#### JSON Schema 속성

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 시간이력 하중케이스명 | `"THIS_NAME"` | String | — | **Required** |
| 2 | 요소 타입 · Beam: `0` / Truss: `1` / Wall: `2` | `"TYPE_ELEMENT"` | Integer | — | **Required** |
| 3 | 요소 번호 | `"PROPERTY_KEY"` | Integer | — | **Required** |
| 4 | 층 이름 (`TYPE_ELEMENT`가 `2`(Wall)일 때) | `"STORY_NAME"` | String | Blank | Optional |
| 5 | 결과 타입 · Force: `0` | `"TYPE_RES"` | Integer | `0` | Optional |
| 6 | 위치 · I-end/Top: `0` / J-end/Bottom: `1` | `"LOCATION"` | Integer | `0` | Optional |
| 7 | 성분 · Axial: `0` / Shear-y: `1` / Shear-z: `2` / Torsion: `3` / Moment-y: `4` / Moment-z: `5` | `"COMP"` | Integer | `0` | Optional |

#### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 102,
      "STORY_NAME": "",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0
    }
  }
}
```

**GET Response Body**

```json
{
  "THRE": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 102,
      "STORY_NAME": "",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0
    }
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── POST: 보 요소 102번의 축력(Axial, I단) 스마트 그래프 정의 ──────
payload = {
    "Assign": {
        "1": {
            "THIS_NAME": "HIST1",      # 시간이력 하중케이스명
            "TYPE_ELEMENT": 0,          # 0=Beam
            "PROPERTY_KEY": 102,        # 요소 번호
            "STORY_NAME": "",
            "TYPE_RES": 0,              # 0=Force
            "LOCATION": 0,              # 0=I-end/Top
            "COMP": 0,                  # 0=Axial
        }
    }
}
requests.post(f"{BASE_URL}/db/THRE", json=payload, headers=HEADERS)

# ── GET: 정의된 요소 부재력 스마트 그래프 전체 조회 ───────────────
res = requests.get(f"{BASE_URL}/db/THRE", headers=HEADERS).json()
for gid, rec in res.get("THRE", {}).items():
    print(f"  [{gid}] elem {rec['PROPERTY_KEY']} COMP={rec['COMP']}")

# ── DELETE: 1번 레코드 삭제 ───────────────────────────────────────
requests.delete(f"{BASE_URL}/db/THRE/1", headers=HEADERS)
```

---

### D-2. General Link Smart Graph – `db/THRG`

> **기능:** 일반 링크(General Link) 결과를 시간이력 스마트 그래프로 추출하기 위한 레코드를 정의합니다.

#### Input URI

```
{base url}/db/THRG
```

#### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

#### JSON Schema 속성

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 이름(시간이력 하중케이스명) | `"THIS_NAME"` | String | — | **Required** |
| 2 | 결과 타입 · Force-Deformation: `0` / Force: `1` / Deformation: `2` | `"TYPE_RES"` | Integer | `0` | Optional |
| 3 | 위치 · i-end: `0` / j-end: `1` | `"LOCATION"` | Integer | `0` | Optional |
| 4 | 성분 (Force-Deformation/Force/Deformation) · Fx-Dx/Fx/Dx: `0` / Fy-Dy/Fy/Dy: `1` / Fz-Dz/Fz/Dz: `2` / Mx-Rx/Mx/Rx: `3` / My-Ry/My/Ry: `4` / Mz-Rz/Mz/Rz: `5` | `"COMP"` | Integer | `0` | Optional |
| 5 | 일반 링크 번호 | `"GENERAL_LINK"` | Integer | — | **Required** |

#### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0,
      "GENERAL_LINK": 1
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0,
      "GENERAL_LINK": 4
    }
  }
}
```

**GET Response Body**

```json
{
  "THRG": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0,
      "GENERAL_LINK": 1
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0,
      "GENERAL_LINK": 4
    }
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── POST: 일반링크 1,4번의 힘-변형(Fx-Dx) 스마트 그래프 정의 ───────
payload = {
    "Assign": {
        "1": {"THIS_NAME": "HIST1", "TYPE_RES": 0, "LOCATION": 0, "COMP": 0, "GENERAL_LINK": 1},
        "2": {"THIS_NAME": "HIST1", "TYPE_RES": 0, "LOCATION": 0, "COMP": 0, "GENERAL_LINK": 4},
    }
}
requests.post(f"{BASE_URL}/db/THRG", json=payload, headers=HEADERS)

# ── PUT: 2번 레코드를 Deformation(Dy)으로 수정 ────────────────────
requests.put(f"{BASE_URL}/db/THRG", headers=HEADERS, json={
    "Assign": {"2": {"THIS_NAME": "HIST1", "TYPE_RES": 2, "LOCATION": 0, "COMP": 1, "GENERAL_LINK": 4}}
})

# ── GET: 특정 ID(1번) 조회 ────────────────────────────────────────
print(requests.get(f"{BASE_URL}/db/THRG/1", headers=HEADERS).json())
```

---

### D-3. Inelastic Hinge Smart Graph – `db/THRI`

> **기능:** 비탄성 힌지(Inelastic Hinge) 결과를 시간이력 스마트 그래프로 추출하기 위한 레코드를 정의합니다.

#### Input URI

```
{base url}/db/THRI
```

#### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

#### JSON Schema 속성

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 이름(시간이력 하중케이스명) | `"THIS_NAME"` | String | — | **Required** |
| 2 | 요소 타입 · Beam: `0` / Truss: `1` / General Link: `3` | `"TYPE_ELEMENT"` | Integer | `0` | Optional |
| 3 | 요소 선택(요소 번호) | `"PROPERTY_KEY"` | Integer | — | **Required** |
| 4 | 층 이름 | `"STORY_NAME"` | String | Blank | Optional |
| 5 | 결과 타입 · Force-Deformation: `0` / Force: `1` / Deformation: `2` | `"TYPE_RES"` | Integer | `0` | Optional |
| 6 | 위치 · 1-Pos: `0` / 2-Pos: `1` / 3-Pos: `2` | `"LOCATION"` | Integer | `0` | Optional |
| 7 | 성분 (Force-Deformation/Force/Deformation) · Fx-Dx/Fx/Dx: `0` / Fy-Dy/Fy/Dy: `1` / Fz-Dz/Fz/Dz: `2` / Mx-Rx/Mx/Rx: `3` / My-Ry/My/Ry: `4` / Mz-Rz/Mz/Rz: `5` | `"COMP"` | Integer | `0` | Optional |

#### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2101,
      "STORY_NAME": "",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2137,
      "STORY_NAME": "",
      "TYPE_RES": 1,
      "LOCATION": 1,
      "COMP": 0
    },
    "3": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2184,
      "STORY_NAME": "",
      "TYPE_RES": 2,
      "LOCATION": 1,
      "COMP": 4
    }
  }
}
```

**GET Response Body**

```json
{
  "THRI": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2101,
      "STORY_NAME": "",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0
    }
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── POST: 비탄성 힌지 3개(힘-변형/힘/변형) 스마트 그래프 정의 ──────
payload = {
    "Assign": {
        "1": {"THIS_NAME": "HIST1", "TYPE_ELEMENT": 0, "PROPERTY_KEY": 2101,
              "STORY_NAME": "", "TYPE_RES": 0, "LOCATION": 0, "COMP": 0},
        "2": {"THIS_NAME": "HIST1", "TYPE_ELEMENT": 0, "PROPERTY_KEY": 2137,
              "STORY_NAME": "", "TYPE_RES": 1, "LOCATION": 1, "COMP": 0},
        "3": {"THIS_NAME": "HIST1", "TYPE_ELEMENT": 0, "PROPERTY_KEY": 2184,
              "STORY_NAME": "", "TYPE_RES": 2, "LOCATION": 1, "COMP": 4},
    }
}
requests.post(f"{BASE_URL}/db/THRI", json=payload, headers=HEADERS)

# ── GET: 전체 조회 ────────────────────────────────────────────────
res = requests.get(f"{BASE_URL}/db/THRI", headers=HEADERS).json()
print("정의된 힌지 그래프 개수:", len(res.get("THRI", {})))
```

---

### D-4. Seismic Devices Smart Graph – `db/THRS`

> **기능:** 지진 보호 장치(Seismic Devices, 감쇠기/면진장치 등)의 결과를 시간이력 스마트 그래프로 추출하기 위한 레코드를 정의합니다.

#### Input URI

```
{base url}/db/THRS
```

#### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

#### JSON Schema 속성

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 이름(시간이력 하중케이스명) | `"THIS_NAME"` | String | — | **Required** |
| 2 | 결과 타입 · Force-Deformation: `0` / Force: `2` / Deformation: `3` / Ductility Factor: `5` / Energy: `7` | `"TYPE_RES"` | Integer | `0` | Optional |
| 3 | 성분 | `"COMP"` | Integer | `0` | Optional |
| 4 | 일반 링크 번호 | `"GENERAL_LINK"` | Integer | — | **Required** |

#### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "COMP": 0,
      "GENERAL_LINK": 1
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 2,
      "COMP": 1,
      "GENERAL_LINK": 4
    },
    "3": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 4,
      "COMP": 2,
      "GENERAL_LINK": 4
    }
  }
}
```

**GET Response Body**

```json
{
  "THRS": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "COMP": 0,
      "GENERAL_LINK": 1
    }
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── POST: 지진 장치(일반링크 1,4번) 스마트 그래프 정의 ────────────
payload = {
    "Assign": {
        "1": {"THIS_NAME": "HIST1", "TYPE_RES": 0, "COMP": 0, "GENERAL_LINK": 1},  # 힘-변형
        "2": {"THIS_NAME": "HIST1", "TYPE_RES": 2, "COMP": 1, "GENERAL_LINK": 4},  # 힘
        "3": {"THIS_NAME": "HIST1", "TYPE_RES": 3, "COMP": 2, "GENERAL_LINK": 4},  # 변형
    }
}
requests.post(f"{BASE_URL}/db/THRS", json=payload, headers=HEADERS)

# ── GET: 전체 조회 후 DELETE로 3번 삭제 ──────────────────────────
res = requests.get(f"{BASE_URL}/db/THRS", headers=HEADERS).json()
print("정의된 장치 그래프:", list(res.get("THRS", {}).keys()))
requests.delete(f"{BASE_URL}/db/THRS/3", headers=HEADERS)
```

---

## End-to-End Workflow

시간이력 스마트 그래프 정의(그룹 D) → 절점 변위 텍스트 결과 추출(그룹 A) → 비탄성 힌지 부재력 테이블 추출(그룹 B)의 전형적인 후처리 흐름을 하나의 스크립트로 보여줍니다.

```python
import requests

# ── 공통 설정 ─────────────────────────────────────────────────────
BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}
TH_CASE = "Elcent"    # 시간이력 하중케이스명


def post(uri, body):
    return requests.post(f"{BASE_URL}{uri}", json=body, headers=HEADERS).json()


# 1) [그룹 D] 요소 부재력 스마트 그래프 레코드 정의 (db/THRE) ─────────
graph_def = {
    "Assign": {
        "1": {
            "THIS_NAME": TH_CASE,
            "TYPE_ELEMENT": 0,     # 0=Beam
            "PROPERTY_KEY": 5,     # 보 요소 5번
            "STORY_NAME": "",
            "TYPE_RES": 0,         # Force
            "LOCATION": 0,         # I-end
            "COMP": 4,             # Moment-y
        }
    }
}
requests.post(f"{BASE_URL}/db/THRE", json=graph_def, headers=HEADERS)
print("[1] 스마트 그래프 정의 완료")

# 2) [그룹 A] 절점 10번의 시간이력 변위 텍스트 결과 추출 (post/TEXT) ──
disp = post("/post/TEXT", {
    "Argument": {
        "TEXT_TYPE": "TH_DISP",
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [10]},
        "TH_CASE_NAME": [TH_CASE],
        "STEP": {"FROM": 0.1, "TO": 0.5, "STEPS": 1},
        "REF_PT": "Ground",
    }
})
peak = max(disp["TH_DISP"]["DATA"], key=lambda r: abs(float(r[4])))
print(f"[2] 절점 10 최대 Dx = {peak[4]} mm (t={peak[3]}s)")

# 3) [그룹 B] 비탄성 힌지(집중형) 부재력 테이블 추출 (post/TABLE) ─────
force = post("/post/TABLE", {
    "Argument": {
        "TABLE_NAME": "Lumped",
        "TABLE_TYPE": "IEHG_FORCE_LUMPED",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "TH_LOAD_CASE_NAMES": [f"{TH_CASE}(TH:max)", f"{TH_CASE}(TH:min)"],
    }
})
tbl = force["Lumped"]
print(f"[3] 힌지 부재력 테이블: {len(tbl['DATA'])}행, HEAD {len(tbl['HEAD'])}열")
for row in tbl["DATA"]:
    print(f"     elem {row[1]} {row[2]}  Fx={row[5]} @ t={row[6]}")

print("\n워크플로 완료: 그래프 정의 → 변위 추출 → 힌지 부재력 추출")
```
