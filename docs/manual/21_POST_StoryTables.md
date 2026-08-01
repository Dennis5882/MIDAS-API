# 21. POST – Analysis Story Tables (층 결과 테이블)

> **대상 제품:** MIDAS Gen NX (주) · MIDAS Civil NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/49511531295257)

이 파트는 건축물 해석의 **층 단위 결과 테이블 17종**을 다룹니다. 층변위(Story Drift)·층변위비·층변위(Story Displacement)·층전단력(응답스펙트럼)·전단력계수·모드형상·전단력비·편심(Eccentricity)·전도모멘트(Overturning Moment)·층 축력 합·안정계수(Stability Coefficient)·비틀림 불규칙(Torsional Irregularity)·비틀림 증폭계수·강성 불규칙(연층)·강도 불규칙(약층)·평면 정형성 기준·설계 층전단력 검토·중량 불규칙 검토 등 내진 설계에 필요한 층 결과를 포함합니다. 모든 엔드포인트는 **공통 URI `{base url}/post/TABLE`** 를 사용하며 `POST` 메서드만 지원합니다. 요청 바디의 `"Argument"` 객체에서 `TABLE_TYPE` 값으로 테이블 종류를 결정합니다.

---

## 공통 사항

### Input URI (층 결과 테이블 공통)

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 공통 Request 구조 및 파라미터

해석 결과 테이블(19장)과 동일한 확장 구조로, `UNIT`·`STYLES`·`COMPONENTS`·`NODE_ELEMS`·`LOAD_CASE_NAMES`·`OPT_CS`·`STAGE_STEP`를 지원합니다. **아래 파라미터 표는 17개 테이블 전체에 공통 적용**되며, 각 절에서는 `TABLE_TYPE` enum과 응답 `HEAD` 열, 대표 예시만 별도 기술합니다.

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

> **참고:** `OPT_CS`·`STAGE_STEP`는 시공단계 결과 조회 시 사용합니다. `STAGE_STEP` 항목은 `"CS1:001(first)"`, `"CS1:002(last)"` 형식입니다.

> **층 결과 테이블 하중 유의사항:** 층 결과 테이블은 일반적으로 정적 지진하중 `(ST)`, 응답스펙트럼 `(RS)`, 하중조합 `(CB)` 유형의 `LOAD_CASE_NAMES`를 사용합니다. 특히 **응답스펙트럼 기반 테이블(Story Shear Force (R.S.), Story Shear Force Coefficient (R.S.), Story Mode Shape)** 은 반드시 `(RS)` 하중케이스가 정의·해석되어 있어야 하며, 해당 하중이 없으면 `DATA`가 비어 반환됩니다.

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
| 1 | [Story Drift](#1-story-drift) | `STORY_DRIFT_X` / `STORY_DRIFT_Y` / `STORY_DRIFT_COMB` |
| 2 | [Story Displacement](#2-story-displacement) | `STORY_DISPLACEMENT_X` / `STORY_DISPLACEMENT_Y` / `STORY_DISPLACEMENT_COMB` |
| 3 | [Story Shear Force (R.S. Analysis)](#3-story-shear-force-rs-analysis) | `STORY_SHEAR_FOR_RS` |
| 4 | [Story Shear Force Coefficient (R.S. Analysis)](#4-story-shear-force-coefficient-rs-analysis) | `STORY_SHEAR_FORCE_COEFFICIENT` |
| 5 | [Story Mode Shape](#5-story-mode-shape) | `STORY_MODE_SHAPE` |
| 6 | [Story Shear Force Ratio](#6-story-shear-force-ratio) | `STORY_SHEAR_FORCE_RATIO` |
| 7 | [Story Eccentricity](#7-story-eccentricity) | `STORY_ECNTRICITY` |
| 8 | [Overturning Moment](#8-overturning-moment) | `OVERTURNING_MOMENT` |
| 9 | [Story Axial Force Sum](#9-story-axial-force-sum) | `STORY_AXIAL_FORCE_SUM` |
| 10 | [Story Stability Coefficient](#10-story-stability-coefficient) | `STORY_STABILITY_COEFFICIENT_X` / `STORY_STABILITY_COEFFICIENT_Y` |
| 11 | [Torsional Irregularity Check](#11-torsional-irregularity-check) | `TORSIONAL_IRREGULARITY_X` / `TORSIONAL_IRREGULARITY_Y` |
| 12 | [Torsional Amplification Factor](#12-torsional-amplification-factor) | `TORSIONAL_AMPLIFICATION_FACTOR_X` / `TORSIONAL_AMPLIFICATION_FACTOR_Y` |
| 13 | [Stiffness Irregularity Check (Soft Story)](#13-stiffness-irregularity-check-soft-story) | `STIFFNESS_IRREGULARITY_X` / `STIFFNESS_IRREGULARITY_Y` |
| 14 | [Capacity Irregularity Check (Weak Story)](#14-capacity-irregularity-check-weak-story) | `CAPACITY_IRREGULARITY` |
| 15 | [Criteria for Regularity in Plan](#15-criteria-for-regularity-in-plan) | `CRITERIA_FOR_REGULARITY_IN_PLAN` |
| 16 | [Ultimate Story Shear For Check](#16-ultimate-story-shear-for-check) | `ULTIMATE_STORY_SHEAR_FORCE_CHECK` |
| 17 | [Weight Irregularity Check](#17-weight-irregularity-check) | `WEIGHT_IRREGULARITY_X` / `WEIGHT_IRREGULARITY_Y` |

---

## 1. Story Drift

> **기능:** 각 층의 층간변위(Story Drift)와 층간변위비(Story Drift Ratio)를 추출합니다. X/Y 각 방향과 조합(Combined)에 대해 허용 층간변위비 초과 여부(OK/NG)를 함께 제공하여 내진 설계의 층간변위 검토에 사용합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STORY_DRIFT_X"` | X방향 층간변위 |
| `"STORY_DRIFT_Y"` | Y방향 층간변위 |
| `"STORY_DRIFT_COMB"` | 조합(Combined) 층간변위 (전 방향/선택 절점 포함 상세) |

### Response HEAD

**`STORY_DRIFT_X`**

```json
["Index", "Load Case", "Story", "Story Height", "P-Delta Incremental Factor", "Allowable Story Drift Ratio", "Maximum Drift of All Vertical Elements/Node", "Maximum Drift of All Vertical Elements/Story Drift", "Maximum Drift of All Vertical Elements/Modified Drift", "Maximum Drift of All Vertical Elements/Story Drift Ratio", "Maximum Drift of All Vertical Elements/Remark", "Drift at the Center of Mass/Story Drift", "Drift at the Center of Mass/Modified Drift", "Drift at the Center of Mass/Drift Factor", "Drift at the Center of Mass/Story Drift Ratio", "Drift at the Center of Mass/Remark"]
```

**`STORY_DRIFT_Y`**

```json
["Index", "LoadCase", "Story", "StoryHeight", "P-DeltaIncrementalFactor", "AllowableStoryDriftRatio", "MaximumDriftofAllVerticalElements/Node", "MaximumDriftofAllVerticalElements/StoryDrift", "MaximumDriftofAllVerticalElements/ModifiedDrift", "MaximumDriftofAllVerticalElements/StoryDriftRatio", "MaximumDriftofAllVerticalElements/Remark", "DriftattheCenterofMass/StoryDrift", "DriftattheCenterofMass/ModifiedDrift", "DriftattheCenterofMass/DriftFactor", "DriftattheCenterofMass/StoryDriftRatio", "DriftattheCenterofMass/Remark"]
```

**`STORY_DRIFT_COMB`**

```json
["Index", "Load Case", "Story", "Story Height", "P-Delta Incremental Factor", "Allowable Story Drift Ratio", "Maximum Drift of All Vertical Elements/Shear-Weighted Average Drift of Vertical Elements", "Maximum Drift of All Vertical Elements/Node", "Maximum Drift of All Vertical Elements/Story Drift", "Maximum Drift of All Vertical Elements/Modified Drift", "Maximum Drift of All Vertical Elements/Story Drift Ratio", "Drift at the Center of Mass/Remark", "Drift at the Center of Mass/Story Drift", "Drift at the Center of Mass/Modified Drift", "Drift at the Center of Mass/Drift Factor", "Drift at the Center of Mass/Story Drift Ratio", "Average Drift of Vertical Elements/Remark", "Average Drift of Vertical Elements/Story Drift", "Average Drift of Vertical Elements/Modified Drift", "Average Drift of Vertical Elements/Drift Factor", "Average Drift of Vertical Elements/Story Drift Ratio", "Drift of a Vertical Line on Selected Node/Remark", "Drift of a Vertical Line on Selected Node/Story Drift", "Drift of a Vertical Line on Selected Node/Modified Drift", "Drift of a Vertical Line on Selected Node/Drift Factor", "Drift of a Vertical Line on Selected Node/Story Drift Ratio", "Average Drift of Vertical Lines on Selected Nodes/Remark", "Average Drift of Vertical Lines on Selected Nodes/Story Drift", "Average Drift of Vertical Lines on Selected Nodes/Modified Drift", "Average Drift of Vertical Lines on Selected Nodes/Drift Factor", "Average Drift of Vertical Lines on Selected Nodes/Story Drift Ratio"]
```

### `ADDITIONAL` — 층간변위 세부 설정 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 `"ADDITIONAL"` 요청 객체가 추가로 문서화되어 있어 반영합니다. 층간변위 허용비 판정 방식(Method 1/2)과 조합(Comb) 테이블의 추가 산출 방식을 세부 제어합니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 세부 설정 객체 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 층간변위비 판정 파라미터 | `ADDITIONAL.SET_STORY_DRIFT_PARAMS` | Object | — | Optional |
| 1-1-1 | 　　└ 판정 방식: `true`=Method 1(응답수정계수), `false`=Method 2(변위증폭계수) | `SET_STORY_DRIFT_PARAMS.RESPONSE_MOD_FACTOR_CHECK` | Boolean | `false` | Optional |
| 1-1-2 | 　　└ (Method 1) 응답수정계수 값 — `RESPONSE_MOD_FACTOR_CHECK: true`일 때만 | `SET_STORY_DRIFT_PARAMS.RESPONSE_MOD_FACTOR_VALUE` | Number | `1` | Optional |
| 1-1-3 | 　　└ (Method 2) 변위증폭계수(Cd) — `RESPONSE_MOD_FACTOR_CHECK: false`일 때만 | `SET_STORY_DRIFT_PARAMS.DEFLECTION_AMPL_FACTOR_VALUE` | Number | `1` | Optional |
| 1-1-4 | 　　└ (Method 2) 중요도계수 | `SET_STORY_DRIFT_PARAMS.IMPORTANCE_FACTOR_VALUE` | Number | `1.5` | Optional |
| 1-1-5 | 　　└ 스케일 계수 | `SET_STORY_DRIFT_PARAMS.SCALE_FACTOR_VALUE` | Number | `1` | Optional |
| 1-1-6 | 　　└ 허용 층간변위비 | `SET_STORY_DRIFT_PARAMS.ALLOWABLE_RATIO` | Number | `0.015` | Optional |
| 1-1-7 | 　　└ P-Delta 검토용 수직하중 조합 목록 | `SET_STORY_DRIFT_PARAMS.LCOMS` | Array [Object] | — | Optional |
| 1-1-7-1 | 　　　　└ 하중케이스명 / 계수 | `LCOMS[].NAME` / `LCOMS[].FACTOR` | String / Number | — | Optional |
| 1-1-8 | 　　└ Beta 값 설정 | `SET_STORY_DRIFT_PARAMS.BETA` | Object | — | Optional |
| 1-1-8-1 | 　　　　└ 방식: `"FIXED"`(1.0 고정) / `"USER"`(층별 직접 입력) | `BETA.FIX_USER_CHECK` | String | `"FIXED"` | Optional |
| 1-1-8-2 | 　　　　└ 적용 시작/종료 층 — `FIX_USER_CHECK: "USER"`일 때만 | `BETA.NAME_FROM` / `BETA.NAME_TO` | String | — | Optional |
| 1-1-8-3 | 　　　　└ 사용자 지정 Beta 값 — `FIX_USER_CHECK: "USER"`일 때만 | `BETA.VALUE` | Number | `0` | Optional |
| 1-2 | └ (`STORY_DRIFT_COMB` 전용) 추가 산출 방식 선택 | `ADDITIONAL.SET_STORY_DRIFT_CALCULATION_METHOD` | Object | `DRIFT_AT_THE_CENTER_OF_MASS` | Optional |
| 1-2-1 | 　　└ 질량중심 변위 | `SET_STORY_DRIFT_CALCULATION_METHOD.DRIFT_AT_THE_CENTER_OF_MASS` | Boolean | `true` | Optional |
| 1-2-2 | 　　└ 수직요소 평균변위 | `SET_STORY_DRIFT_CALCULATION_METHOD.AVERAGE_DRIFT_OF_VERTICAL_ELEMENTS` | Boolean | `false` | Optional |
| 1-2-3 | 　　└ 선택 절점 기준 수직선 변위 (X_DIR/Y_DIR/COMBINED **Required**) | `SET_STORY_DRIFT_CALCULATION_METHOD.DRIFT_OF_A_VERTICAL_LINE_ON_SELECTED_NODE` | Object | — | Optional |
| 1-2-4 | 　　└ 선택 절점(복수) 기준 수직선 평균변위 (X_DIR/Y_DIR/COMBINED 배열, **Required**) | `SET_STORY_DRIFT_CALCULATION_METHOD.AVERAGE_DRIFT_OF_VERTICAL_LINES_ON_SELECTED_NODES` | Object | — | Optional |
| 1-2-5 | 　　└ 전단력 가중 평균변위 | `SET_STORY_DRIFT_CALCULATION_METHOD.SHEAR_WEIGHTED_AVERAGE_DRIFT_OF_VERTICAL_ELEMENTS` | Boolean | `false` | Optional |

> ℹ️ **2026-07-29 공식 정정 반영:** 이전에는 방향 Key가 Specifications 표(`X_DIR`)와 요청 예제(`X-DIR`) 사이에서 불일치했고, `AVERAGE_DRIFT_OF_VERTICAL_LINES_ON_SELECTED_NODES`의 Value 타입도 `Array [Object]`로 잘못 기재되어 있었습니다. 공식 문서가 두 항목 모두 정정되어(`X_DIR`로 통일, 타입은 `Object`로 수정) 아래 예제도 그에 맞춰 갱신했습니다.

**요청 예시 — `ADDITIONAL` 포함 (Comb)**

```json
{
  "Argument": {
    "TABLE_TYPE": "STORY_DRIFT_COMB",
    "LOAD_CASE_NAMES": ["RX(RS)", "RY(RS)"],
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "ADDITIONAL": {
      "SET_STORY_DRIFT_PARAMS": {
        "RESPONSE_MOD_FACTOR_CHECK": true,
        "RESPONSE_MOD_FACTOR_VALUE": 3,
        "SCALE_FACTOR_VALUE": 4.0,
        "ALLOWABLE_RATIO": 0.03
      },
      "SET_STORY_DRIFT_CALCULATION_METHOD": {
        "DRIFT_AT_THE_CENTER_OF_MASS": true,
        "AVERAGE_DRIFT_OF_VERTICAL_ELEMENTS": true,
        "DRIFT_OF_A_VERTICAL_LINE_ON_SELECTED_NODE": { "X_DIR": 109 },
        "AVERAGE_DRIFT_OF_VERTICAL_LINES_ON_SELECTED_NODES": { "X_DIR": [262, 260] },
        "SHEAR_WEIGHTED_AVERAGE_DRIFT_OF_VERTICAL_ELEMENTS": true
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body — X방향 층간변위**

```json
{
  "Argument": {
    "TABLE_NAME": "Story Drift(X)",
    "TABLE_TYPE": "STORY_DRIFT_X",
    "UNIT": { "FORCE": "kN", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST Response Body — X방향 층간변위**

```json
{
  "Story Drift(X)": {
    "FORCE": "kN",
    "DIST": "mm",
    "HEAD": ["Index", "Load Case", "Story", "Story Height", "P-Delta Incremental Factor", "Allowable Story Drift Ratio", "Maximum Drift of All Vertical Elements/Node", "Maximum Drift of All Vertical Elements/Story Drift", "Maximum Drift of All Vertical Elements/Modified Drift", "Maximum Drift of All Vertical Elements/Story Drift Ratio", "Maximum Drift of All Vertical Elements/Remark", "Drift at the Center of Mass/Story Drift", "Drift at the Center of Mass/Modified Drift", "Drift at the Center of Mass/Drift Factor", "Drift at the Center of Mass/Story Drift Ratio", "Drift at the Center of Mass/Remark"],
    "DATA": [
      ["1", "RX(RS)", "3F", "4000.000000", "1.000000", "0.020000", "21", "1.998633", "4.996583", "0.001249", "OK", "1.998633", "4.996583", "1.000000", "0.001249", "OK"]
    ]
  }
}
```

**POST Request Body — 조합(Combined) 층간변위**

```json
{
  "Argument": {
    "TABLE_NAME": "Story Drift(Comb)",
    "TABLE_TYPE": "STORY_DRIFT_COMB",
    "UNIT": { "FORCE": "kN", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["gLCB1(CB)"]
  }
}
```

**POST Response Body — 조합(Combined) 층간변위 (일부 열 예시)**

```json
{
  "Story Drift(Comb)": {
    "FORCE": "kN",
    "DIST": "mm",
    "HEAD": ["Index", "Load Case", "Story", "Story Height", "P-Delta Incremental Factor", "Allowable Story Drift Ratio", "Maximum Drift of All Vertical Elements/Shear-Weighted Average Drift of Vertical Elements", "Maximum Drift of All Vertical Elements/Node", "Maximum Drift of All Vertical Elements/Story Drift", "Maximum Drift of All Vertical Elements/Modified Drift", "Maximum Drift of All Vertical Elements/Story Drift Ratio", "Drift at the Center of Mass/Remark", "Drift at the Center of Mass/Story Drift", "Drift at the Center of Mass/Modified Drift", "Drift at the Center of Mass/Drift Factor", "Drift at the Center of Mass/Story Drift Ratio", "Average Drift of Vertical Elements/Remark", "Average Drift of Vertical Elements/Story Drift", "Average Drift of Vertical Elements/Modified Drift", "Average Drift of Vertical Elements/Drift Factor", "Average Drift of Vertical Elements/Story Drift Ratio", "Drift of a Vertical Line on Selected Node/Remark", "Drift of a Vertical Line on Selected Node/Story Drift", "Drift of a Vertical Line on Selected Node/Modified Drift", "Drift of a Vertical Line on Selected Node/Drift Factor", "Drift of a Vertical Line on Selected Node/Story Drift Ratio", "Average Drift of Vertical Lines on Selected Nodes/Remark", "Average Drift of Vertical Lines on Selected Nodes/Story Drift", "Average Drift of Vertical Lines on Selected Nodes/Modified Drift", "Average Drift of Vertical Lines on Selected Nodes/Drift Factor", "Average Drift of Vertical Lines on Selected Nodes/Story Drift Ratio"],
    "DATA": [
      ["1", "RX(RS)", "1F", "6.0000", "-", "0.0300", "48", "0.0042", "0.0505", "0.0084", "OK", "0.0041", "0.0487", "1.0379", "0.0081", "OK", "0.0041", "0.0489", "1.0333", "0.0082", "OK", "-", "-", "-", "-", "-", "0.0339", "0.4074", "0.1240", "0.0679", "NG"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# 층간변위(X방향) 테이블 조회 — 허용 변위비 초과 여부(OK/NG) 확인
payload = {
    "Argument": {
        "TABLE_NAME": "Story Drift(X)",
        "TABLE_TYPE": "STORY_DRIFT_X",
        "UNIT": {"FORCE": "kN", "DIST": "mm"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["RX(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Story Drift(X)", {})
head = table.get("HEAD", [])

# 각 층의 최대 층간변위비와 판정(Remark) 출력
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    story = d["Story"]
    ratio = d["Maximum Drift of All Vertical Elements/Story Drift Ratio"]
    remark = d["Maximum Drift of All Vertical Elements/Remark"]
    print(f"{story}: 층간변위비={ratio}, 판정={remark}")
```

---

## 2. Story Displacement

> **기능:** 각 층 절점의 최대변위·평균변위 및 그 비(Maximum/Average)를 추출합니다. 비틀림 거동 및 층 변위 분포 확인에 사용합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STORY_DISPLACEMENT_X"` | X방향 층 변위 |
| `"STORY_DISPLACEMENT_Y"` | Y방향 층 변위 |
| `"STORY_DISPLACEMENT_COMB"` | 조합(Combined) 층 변위 |

### Response HEAD

```json
["Index", "LoadCase", "Node", "Story", "Level", "StoryHeight", "MaximumDisplacement", "AverageDisplacement", "Maximum/Average"]
```

### Request / Response JSON

**POST Request Body — X방향 층 변위**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_DISPLACEMENT_X",
    "TABLE_TYPE": "STORY_DISPLACEMENT_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST Response Body — X방향 층 변위**

```json
{
  "STORY_DISPLACEMENT_X": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "LoadCase", "Node", "Story", "Level", "StoryHeight", "MaximumDisplacement", "AverageDisplacement", "Maximum/Average"],
    "DATA": [
      ["1", "RX(RS)", "5004", "2F", "11.5000", "0.0000", "0.0070", "0.0070", "1.0000"],
      ["2", "RX(RS)", "47", "1F", "5.5000", "6.0000", "0.0031", "0.0030", "1.0283"]
    ]
  }
}
```

**POST Request Body — 조합(Combined) 층 변위**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_DISPLACEMENT_COMB",
    "TABLE_TYPE": "STORY_DISPLACEMENT_COMB",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["gLCB1(CB)"]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 층 변위(Y방향) — 최대/평균 변위비로 비틀림 거동 확인
payload = {
    "Argument": {
        "TABLE_NAME": "STORY_DISPLACEMENT_Y",
        "TABLE_TYPE": "STORY_DISPLACEMENT_Y",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "LOAD_CASE_NAMES": ["RY(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_DISPLACEMENT_Y", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']} (Node {d['Node']}): Max/Avg={d['Maximum/Average']}")
```

---

## 3. Story Shear Force (R.S. Analysis)

> **기능:** 응답스펙트럼(R.S.) 해석 결과로부터 각 층의 관성력(Inertia Force), 스프링 반력 포함/미포함 전단력, 편심(Eccentricity), 층력(Story Force), 편심모멘트를 추출합니다. **`(RS)` 하중케이스가 필요합니다.**

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STORY_SHEAR_FOR_RS"` | 응답스펙트럼 해석 층전단력 |

### Response HEAD

```json
["Index", "Story", "Level", "Spectrum", "Inertia Force/X", "Inertia Force/Y", "Shear Force/Spring Reactions/X", "Shear Force/Spring Reactions/Y", "Shear Force/Without Spring/X", "Shear Force/Without Spring/Y", "Shear Force/With Spring/X", "Shear Force/With Spring/Y", "Eccentricity", "Story Force", "Eccentric Moment"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_SHEAR_FOR_RS",
    "TABLE_TYPE": "STORY_SHEAR_FOR_RS",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["Rx(RS)"]
  }
}
```

**POST Response Body**

```json
{
  "STORY_SHEAR_FOR_RS": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Spectrum", "Inertia Force/X", "Inertia Force/Y", "Shear Force/Spring Reactions/X", "Shear Force/Spring Reactions/Y", "Shear Force/Without Spring/X", "Shear Force/Without Spring/Y", "Shear Force/With Spring/X", "Shear Force/With Spring/Y", "Eccentricity", "Story Force", "Eccentric Moment"],
    "DATA": [
      ["1", "2F", "11.500000000000", "RX(RS)", "5.942538531202", "-1.613724870840", "0.000000000000", "0.000000000000", "94.786719429559", "19.670201963351", "94.786719429559", "19.670201963351", "0.000000000000", "5.942538531202", "0.000000000000"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 응답스펙트럼 층전단력 — (RS) 하중이 반드시 필요
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_SHEAR_FOR_RS",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["Rx(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_SHEAR_FOR_RS", {})
head = table.get("HEAD", [])
if not table.get("DATA"):
    print("결과 없음 — (RS) 하중케이스 정의/해석 여부를 확인하세요.")
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: Vx(With Spring)={d['Shear Force/With Spring/X']}")
```

---

## 4. Story Shear Force Coefficient (R.S. Analysis)

> **기능:** 응답스펙트럼 해석의 층별 전단력과 누적 중량합(Weight Sum)으로부터 층전단력계수(Story Shear Force Coefficient)를 X/Y방향으로 산정합니다. **`(RS)` 하중케이스가 필요합니다.**

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STORY_SHEAR_FORCE_COEFFICIENT"` | 응답스펙트럼 해석 층전단력계수 |

### Response HEAD

```json
["Index", "Story", "Spectrum", "Shear Force/X", "Shear Force/Y", "Weight Sum/X", "Weight Sum/Y", "Story Shear Force Coefficient/X", "Story Shear Force Coefficient/Y"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_SHEAR_FORCE_COEFFICIENT",
    "TABLE_TYPE": "STORY_SHEAR_FORCE_COEFFICIENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["Rx(RS)"]
  }
}
```

**POST Response Body**

```json
{
  "STORY_SHEAR_FORCE_COEFFICIENT": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Spectrum", "Shear Force/X", "Shear Force/Y", "Weight Sum/X", "Weight Sum/Y", "Story Shear Force Coefficient/X", "Story Shear Force Coefficient/Y"],
    "DATA": [
      ["1", "1F", "RX(RS)", "732.983113710330", "140.189527295489", "8235.050199781430", "8235.050199781430", "0.089007728663", "0.017023518241"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 층전단력계수(V/W) 조회
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_SHEAR_FORCE_COEFFICIENT",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["Rx(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_SHEAR_FORCE_COEFFICIENT", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: Cs,x={d['Story Shear Force Coefficient/X']}, Cs,y={d['Story Shear Force Coefficient/Y']}")
```

---

## 5. Story Mode Shape

> **기능:** 각 층 대표 절점의 모드별 변위 형상(UX, UY, UZ, RX, RY, RZ)을 추출합니다. 층 단위 모드 형상 확인 및 동적 거동 평가에 사용합니다. **모드 해석(R.S.) 결과가 필요합니다.**

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STORY_MODE_SHAPE"` | 층 모드 형상 |

### Response HEAD

```json
["Index", "Story", "Level", "X", "Y", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"]
```

### 전용 파라미터 — 모드 필터 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 조회할 모드를 선택적으로 필터링하는 `"MODES"` 요청 배열이 문서화되어 있어 반영합니다. 지정하지 않으면 전체 모드가 반환됩니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 조회할 모드 번호 목록 (`"Mode" + 번호`, 예: `"Mode1"`) | `"MODES"` | Array [String] | All | Optional |

**요청 예시 — `MODES` 포함**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_MODE_SHAPE",
    "TABLE_TYPE": "STORY_MODE_SHAPE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "MODES": ["Mode1", "Mode2"]
  }
}
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_MODE_SHAPE",
    "TABLE_TYPE": "STORY_MODE_SHAPE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 }
  }
}
```

**POST Response Body**

```json
{
  "STORY_MODE_SHAPE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "X", "Y", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "2F", "11.500000000000", "13.793310881566", "0.000000000000", "1", "-0.000000001120", "0.000000005610", "0.000000000000", "0.000000000000", "0.000000000000", "-0.000000000135"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 층 모드 형상 — 1차 모드의 층별 UX/UY 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_MODE_SHAPE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 6}
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_MODE_SHAPE", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    if d["Mode"] == "1":
        print(f"Mode1 {d['Story']}: UX={d['UX']}, UY={d['UY']}")
```

---

## 6. Story Shear Force Ratio

> **기능:** 각 층에 대해 부재 유형(Frame/Wall 등)별 전단력과 전체 층전단력에 대한 분담률(Ratio)을 두 방향(Angle1/Angle2)으로 추출합니다. 부재별 전단력 분담 검토에 사용합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STORY_SHEAR_FORCE_RATIO"` | 층전단력 분담비 |

### Response HEAD

이 테이블은 두 가지 HEAD 배열을 사용합니다. 첫 행에는 `Index`가 포함되며, 동일 그룹의 이어지는 행에서는 `Index` 열이 생략되어 반환될 수 있습니다.

**HEAD (Index 포함)**

```json
["Index", "Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"]
```

**HEAD (Index 생략)**

```json
["Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"]
```

응답 본문에는 위 `DATA` 외에도 부재유형별 층전단력 합계를 정리한 `"SUB_TABLES"` 배열이 함께 포함됩니다. 자세한 내용은 아래 `SUB_TABLES` 항목을 참고하십시오.

### `ADDITIONAL` — 각도 및 대상 층 설정 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 대상 층을 지정하는 `"STORY_NAMES"` 요청 배열과 `"ADDITIONAL"` 요청 객체가 추가로 문서화되어 있어 반영합니다. `ADDITIONAL.SET_ANGLE.ANGLE`은 Angle1/Angle2 산정 기준각으로, 이 테이블에서는 **필수 입력(Required)** 입니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 대상 층 이름 목록 | `"STORY_NAMES"` | Array [String] | All | Optional |
| 2 | 세부 설정 객체 | `"ADDITIONAL"` | Object | — | Optional |
| 2-1 | └ 각도 설정 | `ADDITIONAL.SET_ANGLE` | Object | — | **Required** |
| 2-1-1 | 　　└ Angle1 입력값 (Angle2 = Angle1 + 90°) | `SET_ANGLE.ANGLE` | Number | — | **Required** |

**요청 예시 — `STORY_NAMES` / `ADDITIONAL` 포함**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "STORY_SHEAR_FORCE_RATIO",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "LOAD_CASE_NAMES": ["EX(ST)"],
    "STORY_NAMES": ["2F"],
    "ADDITIONAL": {
      "SET_ANGLE": { "ANGLE": 33.5 }
    }
  }
}
```

### `SUB_TABLES` — 층전단력 합계 하위 테이블 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 응답 본문 최상위에 부재유형별 층전단력 합계를 정리한 `"SUB_TABLES"` 배열이 추가로 문서화되어 있어 반영합니다. 배열의 각 원소는 하위 테이블 이름을 Key로 갖는 객체이며, 각 하위 테이블은 자체 `HEAD`/`DATA` 구조를 갖습니다.

| No. | 설명 | Key | Value 타입 | 비고 |
| --- | --- | --- | --- | --- |
| 1 | 하위 테이블 목록 | `"SUB_TABLES"` | Array [Object] | 응답 전용 (Read Only) |
| 1-1 | └ 선형 합산 층전단력 | `"LINEAR SUMMATION OF STORY SHEAR FORCE"` | Object | `HEAD`/`DATA` 구조 |
| 1-2 | └ 수치 합산 층전단력 | `"NUMERICAL SUMMATION OF STORY SHEAR FORCE"` | Object | `HEAD`/`DATA` 구조 |

**`SUB_TABLES` 하위 테이블 HEAD** (Type = `"Sum"` 행은 부재유형 합계이며 `Ratio1`/`Ratio2`는 빈 문자열로 반환됨)

```json
["Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_SHEAR_FORCE_RATIO",
    "TABLE_TYPE": "STORY_SHEAR_FORCE_RATIO",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["EX(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "STORY_SHEAR_FORCE_RATIO": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"],
    "DATA": [
      ["1", "2F", "5.000000000000", "EX", "Frame(Beam)", "129", "33.500000000000", "28.665741744457", "0.007935020134", "123.500000000000", "-22.438153697157", "0.009384022933"],
      ["2", "2F", "5.000000000000", "EX", "Frame(Beam)", "130", "33.500000000000", "797.380554817400", "0.220724473589", "123.500000000000", "-544.234513929400", "0.227608261730"]
    ],
    "SUB_TABLES": [
      {
        "LINEAR SUMMATION OF STORY SHEAR FORCE": {
          "HEAD": ["Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"],
          "DATA": [
            ["2F", "", "EX", "Frame(Beam)", "", "33.500000000000", "797.380554817400", "0.220724473589", "123.500000000000", "-544.234513929400", "0.227608261730"],
            ["2F", "", "EX", "Wall", "", "33.500000000000", "2815.180127076000", "0.779275526411", "123.500000000000", "-1846.867240428000", "0.772391738270"],
            ["2F", "", "EX", "Sum", "", "33.500000000000", "3612.560681894000", "", "123.500000000000", "-2391.101754358000", ""]
          ]
        }
      },
      {
        "NUMERICAL SUMMATION OF STORY SHEAR FORCE": {
          "HEAD": ["Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"],
          "DATA": [
            ["2F", "", "EX", "Frame(Beam)", "", "33.500000000000", "797.380554817400", "0.220724473589", "123.500000000000", "-544.234513929400", "0.227608261730"],
            ["2F", "", "EX", "Wall", "", "33.500000000000", "2815.180127076000", "0.779275526411", "123.500000000000", "-1846.867240428000", "0.772391738270"],
            ["2F", "", "EX", "Sum", "", "33.500000000000", "3612.560681894000", "", "123.500000000000", "-2391.101754358000", ""]
          ]
        }
      }
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 층전단력 분담비 — 부재 유형별 분담률 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_SHEAR_FORCE_RATIO",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["EX(ST)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_SHEAR_FORCE_RATIO", {})
head = table.get("HEAD", [])  # 응답의 HEAD 기준으로 매핑
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d.get('Story')} {d.get('Type')}: Ratio1={d.get('Ratio1')}, Ratio2={d.get('Ratio2')}")
```

---

## 7. Story Eccentricity

> **기능:** 각 층의 무게중심(Weight Center)·강성중심(Stiffness Center) 좌표, 편심거리(Ecc. Dist.), 비틀림 강성, 탄성반경(El. Radius), 편심비(Ecc. Ratio)를 추출합니다. 편심에 의한 비틀림 검토에 사용합니다.

> **철자 유의:** 이 테이블의 `TABLE_TYPE` 값은 API 규격상 `"STORY_ECNTRICITY"` 로 **철자가 의도적으로 누락(Ec**c**ent → Ecnt)** 되어 있습니다. 오타처럼 보이더라도 반드시 API가 요구하는 문자열 그대로 `"STORY_ECNTRICITY"` 를 사용해야 합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STORY_ECNTRICITY"` | 층 편심 (철자 그대로 사용, API 규격) |

### Response HEAD

```json
["Index", "Story", "Level", "Weight Center/X", "Weight Center/Y", "Stiffness Center/X", "Stiffness Center/Y", "Ecc. Dist./X", "Ecc. Dist./Y", "Torsional Stiffness", "El. Radius/X", "El. Radius/Y", "Ecc. Ratio/X", "Ecc. Ratio/Y"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_ECNTRICITY",
    "TABLE_TYPE": "STORY_ECNTRICITY",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 }
  }
}
```

**POST Response Body**

```json
{
  "STORY_ECNTRICITY": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Weight Center/X", "Weight Center/Y", "Stiffness Center/X", "Stiffness Center/Y", "Ecc. Dist./X", "Ecc. Dist./Y", "Torsional Stiffness", "El. Radius/X", "El. Radius/Y", "Ecc. Ratio/X", "Ecc. Ratio/Y"],
    "DATA": [
      ["1", "Roof", "8.500000000000", "-3.615980663971", "-2.556113113542", "-5.744037990008", "0.437974763722", "2.128057326037", "2.994087877264", "10819091.305889900774", "2.299549236852", "2.770672579299", "1.302032515452", "0.768065249549"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 층 편심 — 철자 주의: "STORY_ECNTRICITY" (API 규격 그대로)
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_ECNTRICITY",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6}
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_ECNTRICITY", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: 편심비 X={d['Ecc. Ratio/X']}, Y={d['Ecc. Ratio/Y']}")
```

---

## 8. Overturning Moment

> **기능:** 각 층의 전도모멘트(Overturning Moment)를 부재 유형(Frame/Wall)별 분담값·분담비와 함께 두 방향(Angle1/Angle2)에 대해 추출합니다. 전도 안정성 및 벽체/골조 분담 검토에 사용합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"OVERTURNING_MOMENT"` | 전도모멘트 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Reduction Factor", "Angle1", "Overturning Moment by Vertical Member Types/Frame/Value", "Overturning Moment by Vertical Member Types/Frame/Ratio", "Overturning Moment by Vertical Member Types/Wall/Value", "Overturning Moment by Vertical Member Types/Wall/Ratio", "Sum of Story Force1 * Distance", "Overturning Moment1", "Angle2", "Overturning Moment by Vertical Member Types/Frame/Value", "Overturning Moment by Vertical Member Types/Frame/Ratio", "Overturning Moment by Vertical Member Types/Wall/Value", "Overturning Moment by Vertical Member Types/Wall/Ratio", "Sum of Story Force2 * Distance", "Overturning Moment2"]
```

### `ADDITIONAL` — 전도모멘트 산정 조건 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 `"ADDITIONAL"` 요청 객체가 추가로 문서화되어 있어 반영합니다. 전도모멘트 산정 기준각(Angle1/Angle2)과 응답스펙트럼 스케일 계수, 감소계수(Reduction Factor) 산정 방식을 세부 제어합니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 세부 설정 객체 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 각도 설정 | `ADDITIONAL.SET_ANGLE` | Object | — | Optional |
| 1-1-1 | 　　└ Angle1 입력값 (Angle2 = Angle1 + 90°) | `SET_ANGLE.ANGLE` | Number | `0` | Optional |
| 1-2 | └ 전도모멘트 산정 파라미터 | `ADDITIONAL.SET_OVERTURNING_MOMENT_PARAMS` | Object | — | Optional |
| 1-2-1 | 　　└ 응답스펙트럼 스케일 계수 | `SET_OVERTURNING_MOMENT_PARAMS.SF_FOR_RS` | Number | `1` | Optional |
| 1-2-2 | 　　└ 감소계수(Reduction Factor) 산정 방식: `"FIXED"`(1.0 고정) / `"AUTO"`(자동 산정) | `SET_OVERTURNING_MOMENT_PARAMS.DEFINE_RF` | String | `"FIXED"` | Optional |

**요청 예시 — `ADDITIONAL` 포함**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "OVERTURNING_MOMENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "LOAD_CASE_NAMES": ["Rx(RS)", "Ry(RS)"],
    "ADDITIONAL": {
      "SET_ANGLE": { "ANGLE": 33.5 },
      "SET_OVERTURNING_MOMENT_PARAMS": {
        "SF_FOR_RS": 0,
        "DEFINE_RF": "AUTO"
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "OVERTURNING_MOMENT",
    "TABLE_TYPE": "OVERTURNING_MOMENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["Rx(RS)"]
  }
}
```

**POST Response Body**

```json
{
  "OVERTURNING_MOMENT": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Reduction Factor", "Angle1", "Overturning Moment by Vertical Member Types/Frame/Value", "Overturning Moment by Vertical Member Types/Frame/Ratio", "Overturning Moment by Vertical Member Types/Wall/Value", "Overturning Moment by Vertical Member Types/Wall/Ratio", "Sum of Story Force1 * Distance", "Overturning Moment1", "Angle2", "Overturning Moment by Vertical Member Types/Frame/Value", "Overturning Moment by Vertical Member Types/Frame/Ratio", "Overturning Moment by Vertical Member Types/Wall/Value", "Overturning Moment by Vertical Member Types/Wall/Ratio", "Sum of Story Force2 * Distance", "Overturning Moment2"],
    "DATA": [
      ["1", "RX(RS)", "12F", "46.000000000000", "4.000000000000", "1.000000000000", "0.000000000000", "2295.801974529160", "0.585868242113", "1622.829911454460", "0.414131757887", "3918.631885983620", "3918.631885983620", "90.000000000000", "569.013713175881", "0.581454548541", "409.590228617339", "0.418545451459", "978.603941793220", "978.603941793220"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 전도모멘트 — 방향1 전도모멘트와 벽체 분담비 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "OVERTURNING_MOMENT",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["Rx(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("OVERTURNING_MOMENT", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: OTM1={d['Overturning Moment1']}, "
          f"Wall분담비={d['Overturning Moment by Vertical Member Types/Wall/Ratio']}")
```

---

## 9. Story Axial Force Sum

> **기능:** 각 층 수직부재(기둥·벽체)의 축력 합(Axial Force Sum)과 축력 중심(Center of Axial Forces) 좌표를 추출합니다. 층 수직하중 분포 및 축력 중심 확인에 사용합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STORY_AXIAL_FORCE_SUM"` | 층 축력 합 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Axial Force Sum of Vertical Elements", "Center of Axial Forces/X Coordinate", "Center of Axial Forces/Y Coordinate"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_AXIAL_FORCE_SUM",
    "TABLE_TYPE": "STORY_AXIAL_FORCE_SUM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "STORY_AXIAL_FORCE_SUM": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Axial Force Sum of Vertical Elements", "Center of Axial Forces/X Coordinate", "Center of Axial Forces/Y Coordinate"],
    "DATA": [
      ["1", "DL", "12F", "46.000000000000", "4.000000000000", "-2243898.534310730174", "18.015185337274", "14.191484061342"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 층 축력 합 — 고정하중(DL) 기준
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_AXIAL_FORCE_SUM",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_AXIAL_FORCE_SUM", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: ΣN={d['Axial Force Sum of Vertical Elements']}")
```

---

## 10. Story Stability Coefficient

> **기능:** 각 층의 안정계수(Stability Coefficient, θ)를 수직하중·층전단력·수정 층간변위로부터 산정하고 허용한계(Allowable Limit) 초과 여부(OK/NG)와 P-Delta 증폭계수를 함께 제공합니다. X/Y 각 방향에 대해 P-Δ 효과를 검토합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STORY_STABILITY_COEFFICIENT_X"` | X방향 안정계수 |
| `"STORY_STABILITY_COEFFICIENT_Y"` | Y방향 안정계수 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Story Height", "Vertical Load", "Story Shear Force", "Modified Story Drift", "Beta", "Stability Coefficient", "Allowable Limit", "Remark", "P-Delta Incremental Factor"]
```

### `ADDITIONAL` — 안정계수 산정 파라미터 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 `"ADDITIONAL"` 요청 객체가 추가로 문서화되어 있어 반영합니다. 안정계수(θ) 산정에 사용되는 변위증폭계수·중요도계수 등의 파라미터와 Beta 값, 층간변위 산정 방식을 세부 제어합니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 세부 설정 객체 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 안정계수 산정 파라미터 | `ADDITIONAL.SET_STABILITY_COEFFICIENT_PARAMS` | Object | — | Optional |
| 1-1-1 | 　　└ 변위증폭계수(Cd) | `SET_STABILITY_COEFFICIENT_PARAMS.DEFLECTION_AMPL_FACTOR_VALUE` | Number | System | Optional |
| 1-1-2 | 　　└ 중요도계수 | `SET_STABILITY_COEFFICIENT_PARAMS.IMPORTANCE_FACTOR_VALUE` | Integer | System | Optional |
| 1-1-3 | 　　└ 스케일 계수 | `SET_STABILITY_COEFFICIENT_PARAMS.SCALE_FACTOR_VALUE` | Integer | System | Optional |
| 1-1-4 | 　　└ P-Delta 검토용 수직하중 조합 목록 | `SET_STABILITY_COEFFICIENT_PARAMS.LCOMS` | Array [Object] | System | Optional |
| 1-1-4-1 | 　　　　└ 하중케이스명 / 계수 | `LCOMS[].NAME` / `LCOMS[].FACTOR` | String / Number | — | Optional |
| 1-1-5 | 　　└ Beta 값 설정 | `SET_STABILITY_COEFFICIENT_PARAMS.BETA` | Object | — | Optional |
| 1-1-5-1 | 　　　　└ 방식: `"FIXED"`(1.0 고정) / `"USER"`(층별 직접 입력) | `BETA.FIX_USER_CHECK` | String | System | Optional |
| 1-1-5-2 | 　　　　└ 적용 시작/종료 층 — `FIX_USER_CHECK: "USER"`일 때만 | `BETA.NAME_FROM` / `BETA.NAME_TO` | String | — | Optional |
| 1-1-5-3 | 　　　　└ 사용자 지정 Beta 값 — `FIX_USER_CHECK: "USER"`일 때만 | `BETA.VALUE` | Number | — | Optional |
| 1-2 | └ 층간변위 산정 방식 선택 | `ADDITIONAL.SET_CALCULATION_METHOD` | Object | — | Optional |
| 1-2-1 | 　　└ 방식: `"Drift on the Center of Mass"`(질량중심 변위) / `"Max. Drift of Outer Extreme Points"`(외곽 최대변위) / `"Max. Drift of All Vertical Elements"`(전 수직요소 최대변위) | `SET_CALCULATION_METHOD.STORY_DRIFT_METHOD` | String | — | Optional |

> ℹ️ **2026-07-30 공식 확인 — `STORY_DRIFT_METHOD` 값 정정.** 이 테이블의 공식 Specifications 표는 첫 번째 값을 `"Drfit on the Center of Mass"`로 적고 있습니다. 이전 버전 문서는 [13. Stiffness Irregularity Check](#13-stiffness-irregularity-check-soft-story)·[17. Weight Irregularity Check](#17-weight-irregularity-check)와 동일 enum이라 가정하고 `"Drift at the Center of Mass"`로 정정해 실었으나, **이는 잘못된 교정이었습니다.** 공식 담당자 확인 결과(Jira MAPI-2009) API는 제품 UI 문구를 그대로 따르도록 설계되어 있고, 이 테이블(Story Stability Coefficient)이 속한 제품 화면은 실제로 "Drift **on**"을 사용하며 "Drift at"을 쓰는 것은 Weight Irregularity Check뿐입니다. 즉 오타는 철자(`Drfit`→`Drift`)뿐이고 전치사(`on`)는 의도된 표기이므로, 위 표는 철자만 정정한 `"Drift on the Center of Mass"`로 기재했습니다.

**요청 예시 — `ADDITIONAL` 포함**

```json
{
  "Argument": {
    "TABLE_TYPE": "STORY_STABILITY_COEFFICIENT_X",
    "LOAD_CASE_NAMES": ["RX(RS)"],
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "ADDITIONAL": {
      "SET_STABILITY_COEFFICIENT_PARAMS": {
        "DEFLECTION_AMPL_FACTOR_VALUE": 2,
        "IMPORTANCE_FACTOR_VALUE": 5,
        "SCALE_FACTOR_VALUE": 2,
        "LCOMS": [
          { "NAME": "DL", "FACTOR": 1 }
        ],
        "BETA": {
          "FIX_USER_CHECK": "USER",
          "NAME_FROM": "1F",
          "NAME_TO": "12F",
          "VALUE": 2
        }
      },
      "SET_CALCULATION_METHOD": {
        "STORY_DRIFT_METHOD": "Max. Drift of All Vertical Elements"
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body — X방향**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_STABILITY_COEFFICIENT_X",
    "TABLE_TYPE": "STORY_STABILITY_COEFFICIENT_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST Response Body — X방향**

```json
{
  "STORY_STABILITY_COEFFICIENT_X": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Story Height", "Vertical Load", "Story Shear Force", "Modified Story Drift", "Beta", "Stability Coefficient", "Allowable Limit", "Remark", "P-Delta Incremental Factor"],
    "DATA": [
      ["1", "RX(RS)", "12F", "4.000000000000", "9981.361069987301", "979.657971495906", "0.001432662061", "1.000000000000", "0.000912302925", "0.250000000000", "OK", "1.000000000000"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 안정계수(Y방향) — 허용한계 초과 여부(OK/NG) 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_STABILITY_COEFFICIENT_Y",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["RY(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_STABILITY_COEFFICIENT_Y", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: θ={d['Stability Coefficient']} (한계={d['Allowable Limit']}) → {d['Remark']}")
```

---

## 11. Torsional Irregularity Check

> **기능:** 비틀림 불규칙(Torsional Irregularity) 검토 테이블입니다. 극단부 층간변위의 평균 및 1.2배 값과 최대값(Maximum Value)을 비교하여 비틀림 불규칙 여부(Regular/Irregular)를 X/Y 방향으로 판정합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TORSIONAL_IRREGULARITY_X"` | X방향 비틀림 불규칙 검토 |
| `"TORSIONAL_IRREGULARITY_Y"` | Y방향 비틀림 불규칙 검토 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Average Value of Extreme Points/Story Drift", "Average Value of Extreme Points/1.2*Story Drift", "Maximum Value/Node", "Maximum Value/Story Drift", "Remark"]
```

### `ADDITIONAL` — 비틀림 불규칙 검토 대상 극단부 절점 선택 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 `"ADDITIONAL"` 요청 객체가 추가로 문서화되어 있어 반영합니다. 비틀림 불규칙 검토에 사용할 극단부(Extreme Points) 절점을 자동 계산 대신 사용자가 직접 지정할 수 있습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 세부 설정 객체 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 비틀림 불규칙 검토 대상 극단부 절점 선택 | `ADDITIONAL.SELECT_IRREGULAR_ENDS` | Object | — | Required |
| 1-1-1 | 　　└ 절점 선택 방식: `false`=자동 계산 / `true`=사용자 지정 | `SELECT_IRREGULAR_ENDS.USER_DEFINE` | Boolean | — | Required |
| 1-1-2 | 　　└ 극단부 절점 번호 2개 지정 — `USER_DEFINE: true`일 때만 | `SELECT_IRREGULAR_ENDS.SELECT_NODES` | Array [Integer] | — | Required |

**요청 예시 — `ADDITIONAL` 포함**

```json
{
  "Argument": {
    "TABLE_TYPE": "TORSIONAL_IRREGULARITY_X",
    "LOAD_CASE_NAMES": ["RX(RS)"],
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "ADDITIONAL": {
      "SELECT_IRREGULAR_ENDS": {
        "USER_DEFINE": true,
        "SELECT_NODES": [1, 37]
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body — X방향**

```json
{
  "Argument": {
    "TABLE_NAME": "TORSIONAL_IRREGULARITY_X",
    "TABLE_TYPE": "TORSIONAL_IRREGULARITY_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST Response Body — X방향**

```json
{
  "TORSIONAL_IRREGULARITY_X": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Average Value of Extreme Points/Story Drift", "Average Value of Extreme Points/1.2*Story Drift", "Maximum Value/Node", "Maximum Value/Story Drift", "Remark"],
    "DATA": [
      ["1", "RX(RS)", "12F", "46.0000", "4.0000", "0.0016", "0.0019", "388", "0.0018", "Regular"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 비틀림 불규칙 검토(X방향) — 판정(Remark) 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "TORSIONAL_IRREGULARITY_X",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "LOAD_CASE_NAMES": ["RX(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TORSIONAL_IRREGULARITY_X", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: 최대변위={d['Maximum Value/Story Drift']} → {d['Remark']}")
```

---

## 12. Torsional Amplification Factor

> **기능:** 비틀림 증폭계수(Torsional Amplification Factor, Ax)를 산정합니다. 극단부 평균변위와 최대변위(Maximum Displacement)의 비를 이용하여 우발 비틀림모멘트에 대한 증폭계수를 X/Y 방향으로 계산합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"TORSIONAL_AMPLIFICATION_FACTOR_X"` | X방향 비틀림 증폭계수 |
| `"TORSIONAL_AMPLIFICATION_FACTOR_Y"` | Y방향 비틀림 증폭계수 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Average Displacement of Extreme Points", "Maximum Displacement/Node", "Maximum Displacement/Displacement", "Torsional Amplification Factor", "Note"]
```

### `ADDITIONAL` — 비틀림 증폭계수 산정 대상 극단부 절점 선택 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 `"ADDITIONAL"` 요청 객체가 추가로 문서화되어 있어 반영합니다. 비틀림 증폭계수(Ax) 산정에 사용할 극단부(Extreme Points) 절점을 자동 계산 대신 사용자가 직접 지정할 수 있습니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 세부 설정 객체 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 비틀림 증폭계수 산정 대상 극단부 절점 선택 | `ADDITIONAL.SELECT_IRREGULAR_ENDS` | Object | — | Required |
| 1-1-1 | 　　└ 절점 선택 방식: `false`=자동 계산 / `true`=사용자 지정 | `SELECT_IRREGULAR_ENDS.USER_DEFINE` | Boolean | — | Required |
| 1-1-2 | 　　└ 극단부 절점 번호 2개 지정 — `USER_DEFINE: true`일 때만 | `SELECT_IRREGULAR_ENDS.SELECT_NODES` | Array [Integer] | — | Required |

**요청 예시 — `ADDITIONAL` 포함**

```json
{
  "Argument": {
    "TABLE_TYPE": "TORSIONAL_AMPLIFICATION_FACTOR_X",
    "LOAD_CASE_NAMES": ["RX(RS)"],
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "ADDITIONAL": {
      "SELECT_IRREGULAR_ENDS": {
        "USER_DEFINE": true,
        "SELECT_NODES": [424, 1]
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body — X방향**

```json
{
  "Argument": {
    "TABLE_NAME": "TORSIONAL_AMPLIFICATION_FACTOR_X",
    "TABLE_TYPE": "TORSIONAL_AMPLIFICATION_FACTOR_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST Response Body — X방향**

```json
{
  "TORSIONAL_AMPLIFICATION_FACTOR_X": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Average Displacement of Extreme Points", "Maximum Displacement/Node", "Maximum Displacement/Displacement", "Torsional Amplification Factor", "Note"],
    "DATA": [
      ["1", "RX(RS)", "Roof", "50.0000", "0.0000", "0.0224", "424", "0.0269", "1.0063", ""]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 비틀림 증폭계수(Y방향) — Ax 값 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "TORSIONAL_AMPLIFICATION_FACTOR_Y",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "LOAD_CASE_NAMES": ["RY(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TORSIONAL_AMPLIFICATION_FACTOR_Y", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: Ax={d['Torsional Amplification Factor']}")
```

---

## 13. Stiffness Irregularity Check (Soft Story)

> **기능:** 강성 불규칙(연층, Soft Story) 검토 테이블입니다. 각 층 강성(Story Stiffness)을 상부층 강성의 0.7배(0.7Ku1)·0.8배 평균(0.8Ku123)과 비교하고 층강성비·층변위각비로 연층 여부(Regular/Irregular)를 X/Y 방향으로 판정합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STIFFNESS_IRREGULARITY_X"` | X방향 강성 불규칙(연층) 검토 |
| `"STIFFNESS_IRREGULARITY_Y"` | Y방향 강성 불규칙(연층) 검토 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Story Drift", "Story Shear Force", "Story Stiffness", "Upper Story Stiffness/0.7Ku1", "Upper Story Stiffness/0.8Ku123", "Story Stiffness Ratio", "Story Drift Angle Ratio", "Remark"]
```

### `ADDITIONAL` — 층강성 산정방식 설정 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 `"ADDITIONAL"` 요청 객체가 추가로 문서화되어 있어 반영합니다. 연층(Soft Story) 판정에 사용할 층간변위 산정방식과 층강성 산정방식을 지정합니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 세부 설정 객체 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 산정방식 설정 | `ADDITIONAL.SET_CALCULATION_METHOD` | Object | — | Required |
| 1-1-1 | 　　└ 층간변위 산정방식: `"Drift at the Center of Mass"`(질량중심 변위) / `"Max. Drift of Outer Extreme Points"`(외곽 최대변위) / `"Max. Drift of All Vertical Elements"`(전 수직요소 최대변위) | `SET_CALCULATION_METHOD.STORY_DRIFT_METHOD` | String | `"Drift at the Center of Mass"` | Optional |

> ⚠️ **`STORY_DRIFT_METHOD` 값 표기 주의.** 이 테이블의 공식 Specifications 표는 세 번째 값을 `"Max. Drfit of All Vertical Elements"`로 적고 있으나, 이는 공식 문서의 오타입니다(`Drfit` → `Drift`). [17. Weight Irregularity Check](#17-weight-irregularity-check) 공식 아티클은 동일 enum을 정상 표기로 기재하고 있어 위 표에는 정규 표기를 실었습니다. 다음 동기화 때 "원문과 다르다"고 되돌리지 마십시오.
| 1-1-2 | 　　└ 층강성 산정방식: `"1 / Story Drift Ratio"`(층간변위비 역수) / `"Story Shear / Story Drift"`(층전단력/층간변위) | `SET_CALCULATION_METHOD.STORY_STIFFNESS_METHOD` | String | `"1 / Story Drift Ratio"` | Optional |

**요청 예시 — `ADDITIONAL` 포함**

```json
{
  "Argument": {
    "TABLE_TYPE": "STIFFNESS_IRREGULARITY_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["RX(RS)"],
    "ADDITIONAL": {
      "SET_CALCULATION_METHOD": {
        "STORY_DRIFT_METHOD": "Drift at the Center of Mass",
        "STORY_STIFFNESS_METHOD": "1 / Story Drift Ratio"
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body — X방향**

```json
{
  "Argument": {
    "TABLE_NAME": "STIFFNESS_IRREGULARITY_X",
    "TABLE_TYPE": "STIFFNESS_IRREGULARITY_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST Response Body — X방향**

```json
{
  "STIFFNESS_IRREGULARITY_X": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Story Drift", "Story Shear Force", "Story Stiffness", "Upper Story Stiffness/0.7Ku1", "Upper Story Stiffness/0.8Ku123", "Story Stiffness Ratio", "Story Drift Angle Ratio", "Remark"],
    "DATA": [
      ["1", "RX(RS)", "12F", "46.0000", "4.0000", "0.0016", "979.6580", "2536.9104", "0.0000", "0.0000", "0.0000", "0.0000", "Regular"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 강성 불규칙(연층) 검토(X방향) — 층강성비와 판정 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "STIFFNESS_IRREGULARITY_X",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "LOAD_CASE_NAMES": ["RX(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STIFFNESS_IRREGULARITY_X", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: 층강성비={d['Story Stiffness Ratio']} → {d['Remark']}")
```

---

## 14. Capacity Irregularity Check (Weak Story)

> **기능:** 강도 불규칙(약층, Weak Story) 검토 테이블입니다. 각 층의 전단강도(Story Shear Strength)를 상부층 전단강도와 비교하여 전단강도비(Story Shear Strength Ratio)와 약층 여부(Remark)를 두 방향(Angle1/Angle2)으로 판정합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"CAPACITY_IRREGULARITY"` | 강도 불규칙(약층) 검토 |

### Response HEAD

```json
["Index", "Story", "Level", "Story Height", "Angle1", "Story Shear Strength1", "Upper Story Shear Strength1", "Story Shear Strength Ratio1", "Remark1", "Angle2", "Story Shear Strength2", "Upper Story Shear Strength2", "Story Shear Strength Ratio2", "Remark2"]
```

### `ADDITIONAL` — 강도 산정 각도 설정 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 `"ADDITIONAL"` 요청 객체가 추가로 문서화되어 있어 반영합니다. 전단강도(Story Shear Strength)를 산정할 기준 각도(Angle1)를 지정하며, Angle2는 Angle1 + 90°로 자동 산정됩니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 세부 설정 객체 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 각도 설정 | `ADDITIONAL.SET_ANGLE` | Object | — | Required |
| 1-1-1 | 　　└ Angle1 입력 각도(°) — Angle2 = Angle1 + 90° | `SET_ANGLE.ANGLE` | Number | — | Required |

**요청 예시 — `ADDITIONAL` 포함**

```json
{
  "Argument": {
    "TABLE_TYPE": "CAPACITY_IRREGULARITY",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "ADDITIONAL": {
      "SET_ANGLE": {
        "ANGLE": 33.5
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "CAPACITY_IRREGULARITY",
    "TABLE_TYPE": "CAPACITY_IRREGULARITY",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 }
  }
}
```

**POST Response Body**

```json
{
  "CAPACITY_IRREGULARITY": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Story Height", "Angle1", "Story Shear Strength1", "Upper Story Shear Strength1", "Story Shear Strength Ratio1", "Remark1", "Angle2", "Story Shear Strength2", "Upper Story Shear Strength2", "Story Shear Strength Ratio2", "Remark2"],
    "DATA": [
      ["1", "12F", "46.0000", "4.0000", "33.5000", "12695.2055", "0.0000", "0.0000", "-", "123.5000", "12960.1189", "0.0000", "0.0000", "-"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 강도 불규칙(약층) 검토 — 방향별 전단강도비/판정 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "CAPACITY_IRREGULARITY",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4}
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CAPACITY_IRREGULARITY", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: 강도비1={d['Story Shear Strength Ratio1']}({d['Remark1']}), "
          f"강도비2={d['Story Shear Strength Ratio2']}({d['Remark2']})")
```

---

## 15. Criteria for Regularity in Plan

> **기능:** 평면 정형성(Regularity in Plan) 판정 기준 테이블입니다. 병진질량(Translational Mass)·회전질량(Rotational Mass), 회전반경비(Rx), r²/Is² 값을 산정하여 X/Y 방향 평면 정형성 여부(Regular/Irregular)를 검토합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"CRITERIA_FOR_REGULARITY_IN_PLAN"` | 평면 정형성 판정 기준 |

### Response HEAD

```json
["Index", "Story", "Level", "Translational Mass/X-DIR", "Translational Mass/Y-DIR", "Rotational Mass", "Rx/X", "Rx/Y", "r²/Is²/X", "r²/Is²/Y", "Check/X", "Check/Y"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "CRITERIA_FOR_REGULARITY_IN_PLAN",
    "TABLE_TYPE": "CRITERIA_FOR_REGULARITY_IN_PLAN",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 }
  }
}
```

**POST Response Body**

```json
{
  "CRITERIA_FOR_REGULARITY_IN_PLAN": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Translational Mass/X-DIR", "Translational Mass/Y-DIR", "Rotational Mass", "Rx/X", "Rx/Y", "r²/Is²/X", "r²/Is²/Y", "Check/X", "Check/Y"],
    "DATA": [
      ["1", "Roof", "50.0000", "943.5741", "943.5741", "196998.8801", "11.3386", "15.0598", "0.6158", "1.0863", "Irregular", "Regular"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 평면 정형성 판정 — 방향별 Check 결과 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "CRITERIA_FOR_REGULARITY_IN_PLAN",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4}
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CRITERIA_FOR_REGULARITY_IN_PLAN", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: Check X={d['Check/X']}, Y={d['Check/Y']}")
```

---

## 16. Ultimate Story Shear For Check

> **기능:** 설계 층전단력 검토(Ultimate Story Shear Force Check) 테이블입니다. 작용 전단력(Applied Shear Force, Ve)과 시계방향/반시계방향 극한전단력(Ultimate Shear Force, Vp)을 기둥·벽체별로 비교하여 전단강도 확보 여부(OK/NG)를 판정합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"ULTIMATE_STORY_SHEAR_FORCE_CHECK"` | 설계 층전단력 검토 |

### Response HEAD

```json
["Index", "Story", "Load Case", "Angle", "Applied Shear Force (Ve)", "Clockwise/Ultimate Shear Force1 (Vp)/Column", "Clockwise/Ultimate Shear Force1 (Vp)/Wall", "Clockwise/Ultimate Shear Force1 (Vp)/SUM", "Clockwise/Ratio1", "Clockwise/Beta1", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/Column", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/Wall", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/SUM", "Counter-Clockwise/Ratio2", "Counter-Clockwise/Beta2", "MIN", "Remark"]
```

### `ADDITIONAL` — 전단력 산정 각도 설정 (2026-07-30 공식 반영)

> ℹ️ 공식 매뉴얼에 `"ADDITIONAL"` 요청 객체가 추가로 문서화되어 있어 반영합니다. [14. Capacity Irregularity Check](#14-capacity-irregularity-check-weak-story)와 필드 구성은 동일하지만(전단력을 산정할 기준 각도(Angle) 지정), 공식 Specifications 표 기준으로 **여기서는 `SET_ANGLE`/`ANGLE` 모두 Optional**입니다 — 14장은 Required이므로 필수 여부가 서로 다릅니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 세부 설정 객체 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 각도 설정 | `ADDITIONAL.SET_ANGLE` | Object | — | Optional |
| 1-1-1 | 　　└ 산정 각도(°) | `SET_ANGLE.ANGLE` | Number | — | Optional |

**요청 예시 — `ADDITIONAL` 포함**

```json
{
  "Argument": {
    "TABLE_TYPE": "ULTIMATE_STORY_SHEAR_FORCE_CHECK",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["Rx(RS)"],
    "ADDITIONAL": {
      "SET_ANGLE": {
        "ANGLE": 0
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "ULTIMATE_STORY_SHEAR_FORCE_CHECK",
    "TABLE_TYPE": "ULTIMATE_STORY_SHEAR_FORCE_CHECK",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["Rx(RS)"]
  }
}
```

**POST Response Body**

```json
{
  "ULTIMATE_STORY_SHEAR_FORCE_CHECK": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Load Case", "Angle", "Applied Shear Force (Ve)", "Clockwise/Ultimate Shear Force1 (Vp)/Column", "Clockwise/Ultimate Shear Force1 (Vp)/Wall", "Clockwise/Ultimate Shear Force1 (Vp)/SUM", "Clockwise/Ratio1", "Clockwise/Beta1", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/Column", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/Wall", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/SUM", "Counter-Clockwise/Ratio2", "Counter-Clockwise/Beta2", "MIN", "Remark"],
    "DATA": [
      ["1", "PR", "Rx(RS)", "0.0000", "298.9810", "0.0000", "0.0000", "0.0000", "0.0000", "-", "0.0000", "0.0000", "0.0000", "0.0000", "-", "-", "OK"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 설계 층전단력 검토 — 작용전단력(Ve)과 최종 판정(Remark) 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "ULTIMATE_STORY_SHEAR_FORCE_CHECK",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "LOAD_CASE_NAMES": ["Rx(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("ULTIMATE_STORY_SHEAR_FORCE_CHECK", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: Ve={d['Applied Shear Force (Ve)']} → {d['Remark']}")
```

---

## 17. Weight Irregularity Check

> **기능:** 중량 불규칙(Weight Irregularity) 검토 테이블입니다. 각 층 중량(Story Weight)을 인접(하부) 층 중량의 1.25배·0.75배와 비교하여 중량비(Story Weight Ratio)로 중량 불규칙 여부(Regular/Irregular)를 X/Y 방향으로 판정합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"WEIGHT_IRREGULARITY_X"` | X방향 중량 불규칙 검토 |
| `"WEIGHT_IRREGULARITY_Y"` | Y방향 중량 불규칙 검토 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Story Weight", "Adjacent Story Weight/1.25M(Lower)", "Adjacent Story Weight/0.75M(Lower)", "Story Weight Ratio", "Story Drift Angle Ratio", "Remark"]
```

### `SET_CALCULATION_METHOD` — 층간변위 산정방식 설정 (2026-07-24 공식 반영)

> ℹ️ 공식 매뉴얼에 `"SET_CALCULATION_METHOD"` 요청 필드가 추가로 문서화되어 있어 반영합니다. 다른 테이블과 달리 `"ADDITIONAL"` 객체로 감싸지 않고 `"Argument"` 바로 하위(= `"TABLE_TYPE"`, `"UNIT"` 등과 동일 레벨)에 위치합니다.

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 산정방식 설정 (`"ADDITIONAL"`이 아닌 `"Argument"` 최상위 필드) | `"SET_CALCULATION_METHOD"` | Object | — | Optional |
| 1-1 | └ 층간변위 산정방식: `"Drift at the Center of Mass"`(질량중심 변위) / `"Max. Drift of Outer Extreme Points"`(외곽 최대변위) / `"Max. Drift of All Vertical Elements"`(전 수직요소 최대변위) | `SET_CALCULATION_METHOD.STORY_DRIFT_METHOD` | String | `""` | Optional |

**요청 예시 — `SET_CALCULATION_METHOD` 포함**

```json
{
  "Argument": {
    "TABLE_TYPE": "WEIGHT_IRREGULARITY_X",
    "UNIT": { "FORCE": "kgf", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["DL(ST)"],
    "SET_CALCULATION_METHOD": {
      "STORY_DRIFT_METHOD": "Drift at the Center of Mass"
    }
  }
}
```

### Request / Response JSON

**POST Request Body — X방향**

```json
{
  "Argument": {
    "TABLE_NAME": "WEIGHT_IRREGULARITY_X",
    "TABLE_TYPE": "WEIGHT_IRREGULARITY_X",
    "UNIT": { "FORCE": "kgf", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body — X방향**

```json
{
  "WEIGHT_IRREGULARITY_X": {
    "FORCE": "kgf",
    "DIST": "mm",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Story Weight", "Adjacent Story Weight/1.25M(Lower)", "Adjacent Story Weight/0.75M(Lower)", "Story Weight Ratio", "Story Drift Angle Ratio", "Remark"],
    "DATA": [
      ["1", "DL", "Roof", "57700", "0", "750967.810373254", "800925.897425977", "480555.538455586", "0.172030728414953", "0", "Regular"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 중량 불규칙 검토(Y방향) — 중량비와 판정 확인
payload = {
    "Argument": {
        "TABLE_TYPE": "WEIGHT_IRREGULARITY_Y",
        "UNIT": {"FORCE": "kgf", "DIST": "mm"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("WEIGHT_IRREGULARITY_Y", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: 중량비={d['Story Weight Ratio']} → {d['Remark']}")
```

---

## End-to-End Workflow

다음은 응답스펙트럼 해석 실행 후 주요 층 결과 테이블(층간변위 → 층 변위 → 층전단력(RS) → 비틀림 불규칙 → 중량 불규칙)을 순차 추출하여 요약을 출력하는 워크플로우입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

def get_story_table(table_type, name, load_cases=None, unit=None, place=6, extra=None):
    """층 결과 테이블 추출 공통 함수"""
    arg = {
        "TABLE_NAME": name,
        "TABLE_TYPE": table_type,
        "UNIT": unit or {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": place}
    }
    if load_cases:
        arg["LOAD_CASE_NAMES"] = load_cases
    if extra:
        arg.update(extra)
    resp = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    table = resp.json().get(name, {})
    return table.get("HEAD", []), table.get("DATA", [])

# ── STEP 1: 층간변위(X) — 허용 변위비 판정 ─────────────────────────
head, data = get_story_table("STORY_DRIFT_X", "Drift(X)", ["RX(RS)"],
                             unit={"FORCE": "kN", "DIST": "mm"})
ng = [dict(zip(head, r)) for r in data
      if dict(zip(head, r)).get("Maximum Drift of All Vertical Elements/Remark") == "NG"]
print(f"STEP1 층간변위: {len(data)}개 층, 초과(NG) {len(ng)}개 층")

# ── STEP 2: 층 변위(X) — 최대/평균 변위비 ──────────────────────────
head, data = get_story_table("STORY_DISPLACEMENT_X", "Disp(X)", ["RX(RS)"], place=4)
for r in data[:3]:
    d = dict(zip(head, r))
    print(f"  STEP2 {d['Story']}: Max/Avg={d['Maximum/Average']}")

# ── STEP 3: 층전단력(응답스펙트럼) ─────────────────────────────────
head, data = get_story_table("STORY_SHEAR_FOR_RS", "ShearRS", ["Rx(RS)"])
if data:
    d = dict(zip(head, data[0]))
    print(f"STEP3 층전단력(RS) 최상층: Vx={d['Shear Force/With Spring/X']}")
else:
    print("STEP3 층전단력(RS): 결과 없음 — (RS) 하중케이스 확인 필요")

# ── STEP 4: 비틀림 불규칙(X) ───────────────────────────────────────
head, data = get_story_table("TORSIONAL_IRREGULARITY_X", "TorIrr(X)", ["RX(RS)"], place=4)
irr = [dict(zip(head, r)) for r in data
       if dict(zip(head, r)).get("Remark") == "Irregular"]
print(f"STEP4 비틀림 불규칙: {len(data)}개 층 중 Irregular {len(irr)}개 층")

# ── STEP 5: 중량 불규칙(X) ─────────────────────────────────────────
head, data = get_story_table("WEIGHT_IRREGULARITY_X", "WtIrr(X)", ["DL(ST)"],
                             unit={"FORCE": "kgf", "DIST": "mm"})
for r in data[:3]:
    d = dict(zip(head, r))
    print(f"  STEP5 {d['Story']}: 중량비={d['Story Weight Ratio']} → {d['Remark']}")

print("층 결과 테이블 일괄 추출 완료")
```
