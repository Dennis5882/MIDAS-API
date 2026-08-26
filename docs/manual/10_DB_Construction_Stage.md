# 10. DB – Construction Stage / Heat of Hydration

시공단계(Construction Stage) 및 수화열(Heat of Hydration) 관련 데이터베이스 API입니다.

> **Base URL**
> - MIDAS CIVIL NX : `https://moa-engineers.midasit.com:443/civil`
> - MIDAS GEN NX   : `https://moa-engineers.midasit.com:443/gen`
>
> **인증** : 모든 요청 헤더에 `MAPI-Key: <your-api-key>` 포함

---

## 목차

### Construction Stage Loads

| # | Endpoint | 설명 |
|---|----------|------|
| 1 | [/db/STAG](#1-dbstag--define-construction-stage) | 시공단계 정의 |
| 2 | [/db/CSCS](#2-dbcscs--composite-section-for-construction-stage) | 시공단계 합성 단면 |
| 3 | [/db/TMLD](#3-dbtmld--time-loads-for-construction-stage) | 시공단계 시간 하중 |
| 4 | [/db/STBK](#4-dbstbk--set-back-loads-for-nonlinear-construction-stage) | 비선형 시공단계 Set-Back 하중 |
| 5 | [/db/CMCS](#5-dbcmcs--camber-for-construction-stage) | 시공단계 캠버 |
| 6 | [/db/CRPC](#6-dbcrpc--creep-coefficient-for-construction-stage) | 시공단계 크리프 계수 |

### Heat of Hydration Loads

| # | Endpoint | 설명 |
|---|----------|------|
| 7 | [/db/ETFC](#7-dbetfc--ambient-temperature-functions) | 외기 온도 함수 |
| 8 | [/db/CCFC](#8-dbccfc--convection-coefficient-functions) | 대류 계수 함수 |
| 9 | [/db/HECB](#9-dbhecb--element-convection-boundary) | 요소 대류 경계 |
| 10 | [/db/HSPT](#10-dbhspt--prescribed-temperature) | 지정 온도 |
| 11 | [/db/HSFC](#11-dbhsfc--heat-source-functions) | 열원 함수 |
| 12 | [/db/HAHS](#12-dbhahs--assign-heat-source) | 열원 지정 |
| 13 | [/db/HPCE](#13-dbhpce--pipe-cooling) | 파이프 쿨링 |
| 14 | [/db/HSTG](#14-dbhstg--define-construction-stage-for-hydration) | 수화열 시공단계 정의 |

---

## 1. /db/STAG – Define Construction Stage

시공단계를 정의합니다. 구조 그룹·경계 그룹·하중 그룹의 활성화/비활성화를 단계별로 설정합니다.

### 1-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/STAG` | 전체 시공단계 조회 |
| `GET` | `{base_url}/db/STAG/{id}` | 특정 ID 시공단계 조회 |
| `POST` | `{base_url}/db/STAG` | 시공단계 생성 |
| `PUT` | `{base_url}/db/STAG` | 시공단계 전체 수정 |
| `PUT` | `{base_url}/db/STAG/{id}` | 특정 ID 시공단계 수정 |
| `DELETE` | `{base_url}/db/STAG` | 전체 시공단계 삭제 |
| `DELETE` | `{base_url}/db/STAG/{id}` | 특정 ID 시공단계 삭제 |

### 1-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 시공단계명 | `NAME` | String | - | Required |
| 2 | 시공단계 지속 기간 (일) | `DURATION` | Number | - | Required |
| 3 | 결과 저장 – 단계 | `bSV_RSLT` | Boolean | false | Optional |
| 4 | 결과 저장 – 추가 스텝 | `bSV_STEP` | Boolean | false | Optional |
| 5 | 재료 비선형 해석을 위한 하중 증분 스텝 사용 여부 | `bLOAD_STEP` | Boolean | false | Optional |
| 6 | 하중 증분 스텝 수 (bLOAD_STEP=true 시) | `INCRE_STEP` | Integer | - | Required |
| 7 | 추가 스텝 목록 | `ADD_STEP` | Array[Number] | [] | Optional |
| 8 | 구조 그룹 활성화 목록 | `ACT_ELEM` | Array[Object] | [] | Optional |
| (1) | 활성화할 구조 그룹명 | `GRUP_NAME` | String | - | Required |
| (2) | 재료 나이 (일) | `AGE` | Number | 0 | Optional |
| 9 | 구조 그룹 비활성화 목록 | `DACT_ELEM` | Array[Object] | [] | Optional |
| (1) | 비활성화할 구조 그룹명 | `GRUP_NAME` | String | - | Required |
| (2) | 요소력 재분배 (%) | `REDIST` | Number | 0 | Optional |
| 10 | 경계 그룹 활성화 목록 | `ACT_BNGR` | Array[Object] | [] | Optional |
| (1) | 활성화할 경계 그룹명 | `BNGR_NAME` | String | - | Required |
| (2) | 지점/스프링 위치 (`"DEFORMED"` / `"ORIGINAL"`) | `POS` | String | - | Required |
| 11 | 비활성화할 경계 그룹명 목록 | `DACT_BNGR` | Array[String] | [] | Optional |
| 12 | 하중 그룹 활성화 목록 | `ACT_LOAD` | Array[Object] | [] | Optional |
| (1) | 활성화할 하중 그룹명 | `LOAD_NAME` | String | - | Required |
| (2) | 활성 일 (`"FIRST"` / `"LAST"` / 숫자 문자열) | `DAY` | String | `"FIRST"` | Optional |
| 13 | 하중 그룹 비활성화 목록 | `DACT_LOAD` | Array[Object] | [] | Optional |
| (1) | 비활성화할 하중 그룹명 | `LOAD_NAME` | String | - | Required |
| (2) | 비활성 일 (`"FIRST"` / `"LAST"` / 숫자 문자열) | `DAY` | String | `"FIRST"` | Optional |

### 1-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "NAME": "CS01",
      "DURATION": 10,
      "bSV_RSLT": true,
      "bSV_STEP": true,
      "bLOAD_STEP": true,
      "INCRE_STEP": 5,
      "ADD_STEP": [5, 8],
      "ACT_ELEM": [
        {"GRUP_NAME": "SG_01", "AGE": 10}
      ],
      "ACT_BNGR": [
        {"BNGR_NAME": "BG_01", "POS": "DEFORMED"}
      ],
      "ACT_LOAD": [
        {"LOAD_NAME": "LG_01", "DAY": "5.000000"}
      ]
    },
    "2": {
      "NAME": "CS02",
      "DURATION": 20,
      "bSV_RSLT": true,
      "bSV_STEP": false,
      "bLOAD_STEP": false,
      "ADD_STEP": [],
      "ACT_ELEM": [
        {"GRUP_NAME": "SG_02", "AGE": 20}
      ],
      "ACT_BNGR": [
        {"BNGR_NAME": "BG_02", "POS": "DEFORMED"}
      ],
      "ACT_LOAD": [
        {"LOAD_NAME": "LG_02", "DAY": "FIRST"}
      ]
    },
    "3": {
      "NAME": "CS03",
      "DURATION": 10,
      "bSV_RSLT": true,
      "bSV_STEP": false,
      "bLOAD_STEP": false,
      "ADD_STEP": [],
      "DACT_ELEM": [
        {"GRUP_NAME": "SG_02", "REDIST": 100}
      ],
      "DACT_BNGR": ["BG_02"],
      "DACT_LOAD": [
        {"LOAD_NAME": "LG_02", "DAY": "FIRST"}
      ]
    }
  }
}
```

### 1-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 시공단계 3단계 생성 ──────────────────────────────────────────────────────
stages = {
    "Assign": {
        "1": {
            "NAME": "CS01",
            "DURATION": 14,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_ELEM": [{"GRUP_NAME": "PIER_01", "AGE": 14}],
            "ACT_BNGR": [{"BNGR_NAME": "FND_01", "POS": "DEFORMED"}],
            "ACT_LOAD": [{"LOAD_NAME": "SW_01", "DAY": "FIRST"}]
        },
        "2": {
            "NAME": "CS02",
            "DURATION": 28,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_ELEM": [{"GRUP_NAME": "GIRDER_01", "AGE": 28}],
            "ACT_BNGR": [{"BNGR_NAME": "BRG_01", "POS": "DEFORMED"}],
            "ACT_LOAD": [{"LOAD_NAME": "SW_02", "DAY": "FIRST"}]
        },
        "3": {
            "NAME": "CS03",
            "DURATION": 60,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_LOAD": [{"LOAD_NAME": "SDL", "DAY": "FIRST"}]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/STAG", json=stages, headers=HEADERS)
print("STAG POST:", resp.status_code)

# ── 전체 시공단계 조회 ───────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/STAG", headers=HEADERS)
print("STAG GET:", resp.status_code)

# ── 특정 단계 수정 ───────────────────────────────────────────────────────────
update = {
    "Assign": {
        "1": {
            "NAME": "CS01",
            "DURATION": 21,    # 14일 → 21일로 변경
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_ELEM": [{"GRUP_NAME": "PIER_01", "AGE": 21}],
            "ACT_LOAD": [{"LOAD_NAME": "SW_01", "DAY": "FIRST"}]
        }
    }
}
resp = requests.put(f"{BASE_URL}/db/STAG/1", json=update, headers=HEADERS)
print("STAG PUT/1:", resp.status_code)
```

---

## 2. /db/CSCS – Composite Section for Construction Stage

시공단계별 합성 단면을 정의합니다. 각 파트의 재료·나이·강성 정보를 설정합니다.

### 2-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/CSCS` | 전체 조회 |
| `GET` | `{base_url}/db/CSCS/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/CSCS` | 생성 |
| `PUT` | `{base_url}/db/CSCS` | 전체 수정 |
| `PUT` | `{base_url}/db/CSCS/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/CSCS` | 전체 삭제 |
| `DELETE` | `{base_url}/db/CSCS/{id}` | 특정 ID 삭제 |

### 2-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 단면 ID | `SEC` | Integer | - | Required |
| 2 | 활성 시공단계명 | `ASTAGE` | String | - | Required |
| 3 | 합성 타입 (`"GENERAL"` / `"USER"`) | `TYPE` | String | - | Required |
| 4 | 테이퍼 타입 여부 | `bTAP` | Boolean | false | Optional |
| 5 | 파트 정보 목록 | `vPARTINFO` | Array[Object] | - | Required |
| (1) | 합성 단면 파트 번호 | `PART` | Integer | - | Required |
| (2) | 재료 타입 (`"ELEM"` / `"MATL"`) | `MTYPE` | String | - | Required |
| (3) | 재료 ID (MATL 타입: 재료 번호 문자열, ELEM 타입: 빈 문자열) | `MAT` | String | - | Optional |
| (4) | 합성 단계 (활성 단계: 빈 문자열, 목표 단계: 시공단계명) | `CSTAGE` | String | Blank | Optional |
| (5) | 재료 나이 (일) | `AGE` | Number | 0 | Optional |
| (6) | 부재의 공칭 치수 (h) | `PARTINFO_H` | Number | AUTO | Optional |
| (7) | 체적-표면적 비 (v/s) | `PARTINFO_VS` | Number | 0 | Optional |
| (8) | 노출 표면의 모듈 (M) | `PARTINFO_M` | Number | 0 | Optional |
| (9) | 단면적 강성 스케일 계수 | `AREA` | Number | 1 | Optional |
| (10) | 유효 전단 면적 (y축) 강성 스케일 계수 | `ASY` | Number | 1 | Optional |
| (11) | 유효 전단 면적 (z축) 강성 스케일 계수 | `ASZ` | Number | 1 | Optional |
| (12) | 비틀림 저항 강성 스케일 계수 | `IXX` | Number | 1 | Optional |
| (13) | 관성 모멘트 (y축) 강성 스케일 계수 | `IYY` | Number | 1 | Optional |
| (14) | 관성 모멘트 (z축) 강성 스케일 계수 | `IZZ` | Number | 1 | Optional |
| (15) | 자중 강성 스케일 계수 | `WAREA` | Number | 1 | Optional |
| (16) | 워핑 상수 강성 스케일 계수 | `IW` | Number | 1 | Optional |
| 6 | 공칭 치수(h) 자동 계산 옵션 | `OPT_UPDATE_ALL_H` | Boolean | - | Optional |

> ⚠️ **2026-08-25 확인:** `WAREA`(자중 스케일 계수)는 원문 Specifications 표에는 (14) `IZZ`
> 다음 항목이 곧바로 (15) `IW`로 이어져 있어 아예 빠져 있지만, JSON Schema와 Request Example
> (아래 2-3 예제의 각 파트에 `"WAREA": 1`)에는 `IZZ`와 `IW` 사이에 명시돼 있다 — 원문 표 자체의
> 누락이며 예제가 표보다 우선(CLAUDE.md 원칙)이라 반영했다(아티클 id `35987625234201`).
> `OPT_UPDATE_ALL_H`도 원문 표·예제 모두에 없고 JSON Schema에만 존재 — 예제로 확인되지 않은
> 스키마 전용 필드임을 밝혀 둔다.

`vPARTINFO`의 각 파트에는 이 외에도 JSON Schema에만 존재하고 원문 표·예제 어디에도 나오지 않는
아래 필드들이 있다. 용도(추정: 중립축까지의 거리는 GET 응답 시의 계산 결과, `STIFF_USER*` 3종은
`TYPE="USER"`일 때의 사용자 정의 강성 입력)는 필드명·설명에서 추정한 것으로 공식 문서에 설명이
없어 확정된 것은 아니다.

| 설명 | Key | Value Type | 비고 |
| --- | --- | --- | --- |
| Y축 중립축까지 거리 | `CY` | Number | (추정) 결과 조회 시 값 |
| Z축 중립축까지 거리 | `CZ` | Number | (추정) 결과 조회 시 값 |
| Y축 중립축까지 거리 – I단 (테이퍼) | `CYI` | Number | (추정) 결과 조회 시 값 |
| Z축 중립축까지 거리 – I단 (테이퍼) | `CZI` | Number | (추정) 결과 조회 시 값 |
| Y축 중립축까지 거리 – J단 (테이퍼) | `CYJ` | Number | (추정) 결과 조회 시 값 |
| Z축 중립축까지 거리 – J단 (테이퍼) | `CZJ` | Number | (추정) 결과 조회 시 값 |
| 사용자 정의 강성 (일반) | `STIFF_USER` | Object | (추정) `TYPE="USER"` 시 사용 |
| 사용자 정의 강성 – I단 (테이퍼) | `STIFF_USER_TAPERED_I` | Object | (추정) `TYPE="USER"`+테이퍼 시 사용 |
| 사용자 정의 강성 – J단 (테이퍼) | `STIFF_USER_TAPERED_J` | Object | (추정) `TYPE="USER"`+테이퍼 시 사용 |

`STIFF_USER`/`STIFF_USER_TAPERED_I`/`STIFF_USER_TAPERED_J` 3종은 모두 동일한 하위 구조
(`AREA`/`ASY`/`ASZ`/`IXX`/`IYY`/`IZZ`/`CYP`/`CYM`/`CZP`/`CZM`/`QYB`/`QZB`/`X1`~`X4`/`Y1`~`Y4`/`IW`,
전부 Number, 설명은 스키마상 "Partial stiffness"로만 표기)를 가진다.

### 2-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "SEC": 1,
      "ASTAGE": "CS01",
      "TYPE": "GENERAL",
      "bTAP": false,
      "vPARTINFO": [
        {
          "PART": 1,
          "MTYPE": "ELEM",
          "MAT": "",
          "CSTAGE": "",
          "AGE": 2,
          "PARTINFO_H": 1.5,
          "PARTINFO_VS": 1.5,
          "PARTINFO_M": 1.5,
          "AREA": 1,
          "ASY": 1,
          "ASZ": 1,
          "IXX": 1,
          "IYY": 1,
          "IZZ": 1,
          "WAREA": 1,
          "IW": 1
        },
        {
          "PART": 2,
          "MTYPE": "MATL",
          "MAT": "3",
          "CSTAGE": "CS02",
          "AGE": 5,
          "PARTINFO_H": 0.245,
          "PARTINFO_VS": 0,
          "PARTINFO_M": 0,
          "AREA": 1,
          "ASY": 1,
          "ASZ": 1,
          "IXX": 1,
          "IYY": 1,
          "IZZ": 1,
          "WAREA": 1,
          "IW": 1
        }
      ]
    }
  }
}
```

### 2-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 시공단계 합성 단면 생성 ──────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "SEC": 1,
            "ASTAGE": "CS01",
            "TYPE": "GENERAL",
            "bTAP": False,
            "vPARTINFO": [
                {
                    "PART": 1,
                    "MTYPE": "ELEM",     # 요소 재료 사용
                    "MAT": "",
                    "CSTAGE": "",        # 활성 단계
                    "AGE": 3,
                    "PARTINFO_H": 1.2,
                    "PARTINFO_VS": 1.0,
                    "PARTINFO_M": 0.0,
                    "AREA": 1, "ASY": 1, "ASZ": 1,
                    "IXX": 1, "IYY": 1, "IZZ": 1,
                    "WAREA": 1, "IW": 1
                },
                {
                    "PART": 2,
                    "MTYPE": "MATL",     # 특정 재료 사용
                    "MAT": "2",          # 재료 번호 2번
                    "CSTAGE": "CS02",    # CS02 단계에서 합성
                    "AGE": 7,
                    "PARTINFO_H": 0.3,
                    "PARTINFO_VS": 0.0,
                    "PARTINFO_M": 0.0,
                    "AREA": 1, "ASY": 1, "ASZ": 1,
                    "IXX": 1, "IYY": 1, "IZZ": 1,
                    "WAREA": 1, "IW": 1
                }
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/CSCS", json=payload, headers=HEADERS)
print("CSCS POST:", resp.status_code)

# ── 전체 조회 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/CSCS", headers=HEADERS)
print("CSCS GET:", resp.status_code)
```

---

## 3. /db/TMLD – Time Loads for Construction Stage

시공단계에서의 시간 하중을 정의합니다. 특정 시공단계(ID)에 하중 그룹과 적용 일을 지정합니다.

### 3-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/TMLD` | 전체 조회 |
| `GET` | `{base_url}/db/TMLD/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/TMLD` | 생성 |
| `PUT` | `{base_url}/db/TMLD` | 전체 수정 |
| `PUT` | `{base_url}/db/TMLD/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/TMLD` | 전체 삭제 |
| `DELETE` | `{base_url}/db/TMLD/{id}` | 특정 ID 삭제 |

### 3-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 시공단계 시간 하중 목록 | `ITEMS` | Array[Object] | - | Required |
| (1) | 일련번호 | `ID` | Integer | 0 | Optional |
| (2) | 하중 그룹명 | `GROUP_NAME` | String | Blank | Optional |
| (3) | 시간 하중 (일) | `DAY` | Number | - | Required |

> **주의**: Assign의 키(ID)는 시공단계 번호입니다. 해당 시공단계에 시간 하중을 적용합니다.

### 3-3. Request Body 예시

```json
{
  "Assign": {
    "10": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "DL_BC_2", "DAY": 35}
      ]
    },
    "11": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "DL_BC_2", "DAY": 25}
      ]
    }
  }
}
```

### 3-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 시공단계 시간 하중 생성 ──────────────────────────────────────────────────
# Assign 키는 시공단계 번호 (STAG의 ID)
payload = {
    "Assign": {
        "1": {    # 시공단계 1번에 적용
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SDL", "DAY": 30}
            ]
        },
        "2": {    # 시공단계 2번에 적용
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SDL",  "DAY": 45},
                {"ID": 2, "GROUP_NAME": "LIVE", "DAY": 60}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/TMLD", json=payload, headers=HEADERS)
print("TMLD POST:", resp.status_code)

# ── 특정 시공단계 시간 하중 조회 ─────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/TMLD/1", headers=HEADERS)
print("TMLD GET/1:", resp.json())
```

---

## 4. /db/STBK – Set-Back Loads for Nonlinear Construction Stage

비선형 시공단계 해석에서의 Set-Back 하중(절점 변위 기반)을 정의합니다.

### 4-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/STBK` | 전체 조회 |
| `GET` | `{base_url}/db/STBK/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/STBK` | 생성 |
| `PUT` | `{base_url}/db/STBK` | 전체 수정 |
| `PUT` | `{base_url}/db/STBK/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/STBK` | 전체 삭제 |
| `DELETE` | `{base_url}/db/STBK/{id}` | 특정 ID 삭제 |

### 4-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 절점 1 | `NODE1` | Integer | - | Required |
| 2 | 절점 2 | `NODE2` | Integer | - | Required |
| 3 | X 방향 변위 | `DX` | Number | 0 | Optional |
| 4 | Y 방향 변위 | `DY` | Number | 0 | Optional |
| 5 | Z 방향 변위 | `DZ` | Number | 0 | Optional |
| 6 | 하중 케이스명 | `LCNAME` | String | - | Required |
| 7 | 하중 그룹명 | `GROUP_NAME` | String | Blank | Optional |

### 4-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "NODE1": 39,
      "NODE2": 22,
      "DX": 0.1,
      "DY": 0.2,
      "DZ": 0.3,
      "LCNAME": "LiveLoad",
      "GROUP_NAME": ""
    },
    "2": {
      "NODE1": 28,
      "NODE2": 21,
      "DX": 0.6,
      "DY": 0.1,
      "DZ": 0.1,
      "LCNAME": "DeadLoad",
      "GROUP_NAME": ""
    }
  }
}
```

### 4-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── Set-Back 하중 생성 ───────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NODE1": 10,
            "NODE2": 20,
            "DX": 0.0,
            "DY": 0.005,   # Y 방향 5mm 변위
            "DZ": 0.0,
            "LCNAME": "DL",
            "GROUP_NAME": "LG_CS01"
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/STBK", json=payload, headers=HEADERS)
print("STBK POST:", resp.status_code)

# ── 전체 조회 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/STBK", headers=HEADERS)
print("STBK GET:", resp.status_code)
```

---

## 5. /db/CMCS – Camber for Construction Stage

시공단계별 절점 캠버(초기 변형)를 정의합니다.

### 5-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/CMCS` | 전체 조회 |
| `GET` | `{base_url}/db/CMCS/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/CMCS` | 생성 |
| `PUT` | `{base_url}/db/CMCS` | 전체 수정 |
| `PUT` | `{base_url}/db/CMCS/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/CMCS` | 전체 삭제 |
| `DELETE` | `{base_url}/db/CMCS/{id}` | 특정 ID 삭제 |

### 5-2. 파라미터

> Assign의 키(ID)는 절점 번호입니다.

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 변형 캠버 | `DEFORM` | Number | - | Required |
| 2 | 사용자 정의 캠버 | `USER` | Number | - | Required |

### 5-3. Request Body 예시

```json
{
  "Assign": {
    "23": {"DEFORM": 0.0,  "USER": 0.00 },
    "25": {"DEFORM": 0.1,  "USER": 0.17 },
    "27": {"DEFORM": 0.0,  "USER": 0.28 },
    "28": {"DEFORM": 0.0,  "USER": 0.34 },
    "29": {"DEFORM": 0.0,  "USER": 0.39 },
    "31": {"DEFORM": 0.0,  "USER": 0.46 },
    "33": {"DEFORM": 0.0,  "USER": 0.49 }
  }
}
```

### 5-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 절점 캠버 생성 ───────────────────────────────────────────────────────────
# Assign 키는 절점 번호
camber_data = {}
node_cambers = {
    25: (0.10, 0.17),
    27: (0.00, 0.28),
    29: (0.00, 0.39),
    31: (0.00, 0.46),
    33: (0.00, 0.49),
}
for node_id, (deform, user) in node_cambers.items():
    camber_data[str(node_id)] = {"DEFORM": deform, "USER": user}

payload = {"Assign": camber_data}

resp = requests.post(f"{BASE_URL}/db/CMCS", json=payload, headers=HEADERS)
print("CMCS POST:", resp.status_code)

# ── 특정 절점 캠버 조회 ──────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/CMCS/25", headers=HEADERS)
print("CMCS GET/25:", resp.json())
```

---

## 6. /db/CRPC – Creep Coefficient for Construction Stage

시공단계별 크리프 계수를 정의합니다.

### 6-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/CRPC` | 전체 조회 |
| `GET` | `{base_url}/db/CRPC/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/CRPC` | 생성 |
| `PUT` | `{base_url}/db/CRPC` | 전체 수정 |
| `PUT` | `{base_url}/db/CRPC/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/CRPC` | 전체 삭제 |
| `DELETE` | `{base_url}/db/CRPC/{id}` | 특정 ID 삭제 |

### 6-2. 파라미터

> Assign의 키(ID)는 시공단계 번호입니다.

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 크리프 계수 목록 | `ITEMS` | Array[Object] | - | Required |
| (1) | 일련번호 | `ID` | Integer | 0 | Optional |
| (2) | 하중 그룹명 | `GROUP_NAME` | String | Blank | Optional |
| (3) | 크리프 계수 | `CREEP` | Number | - | Required |

### 6-3. Request Body 예시

```json
{
  "Assign": {
    "25": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "2ndDeadLoad", "CREEP": 1.2}
      ]
    },
    "26": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "Selfweight", "CREEP": 1.5}
      ]
    }
  }
}
```

### 6-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 시공단계 크리프 계수 생성 ────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {    # 시공단계 1번
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SW",  "CREEP": 1.5},
                {"ID": 2, "GROUP_NAME": "SDL", "CREEP": 1.2}
            ]
        },
        "2": {    # 시공단계 2번
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SW",  "CREEP": 2.0}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/CRPC", json=payload, headers=HEADERS)
print("CRPC POST:", resp.status_code)
```

---

## 7. /db/ETFC – Ambient Temperature Functions

수화열 해석에 사용되는 외기 온도 함수를 정의합니다.

### 7-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/ETFC` | 전체 조회 |
| `GET` | `{base_url}/db/ETFC/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/ETFC` | 생성 |
| `PUT` | `{base_url}/db/ETFC` | 전체 수정 |
| `PUT` | `{base_url}/db/ETFC/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/ETFC` | 전체 삭제 |
| `DELETE` | `{base_url}/db/ETFC/{id}` | 특정 ID 삭제 |

### 7-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 함수명 | `NAME` | String | - | Required |
| 2 | 함수 타입 (`"CONST"` / `"SINE"` / `"USER"`) | `TYPE` | String | - | Required |

**Constant 타입 (TYPE="CONST") 추가 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 온도 | `TEMP` | Number | 0 | Optional |

**Sine Function 타입 (TYPE="SINE") 추가 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 최대 온도 (T) | `MAX_TEMP` | Number | 0 | Optional |
| 평균 온도 (To) | `MEAN_TEMP` | Number | 0 | Optional |
| 지연 시간 (to) | `DELAY_TIME` | Number | 0 | Optional |

**User 타입 (TYPE="USER") 추가 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 스케일 계수 | `SCALE_FACTOR` | Number | - | Required |
| 함수 데이터 목록 | `ITEM` | Array[Object] | - | Required |
| - 시간 | `TIME` | Number | - | Required |
| - 온도 | `VALUE` | Number | - | Required |

### 7-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "NAME": "AmbientTemp_Const",
      "TYPE": "CONST",
      "TEMP": 30
    },
    "2": {
      "NAME": "AmbientTemp_User",
      "TYPE": "USER",
      "SCALE_FACTOR": 1,
      "ITEM": [
        {"TIME": 0, "VALUE": 20},
        {"TIME": 1, "VALUE": 30},
        {"TIME": 2, "VALUE": 40}
      ]
    },
    "3": {
      "NAME": "AmbientTemp_Sine",
      "TYPE": "SINE",
      "MAX_TEMP": 20,
      "MEAN_TEMP": 0,
      "DELAY_TIME": 1
    }
  }
}
```

### 7-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 외기 온도 함수 생성 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "AT_Summer",
            "TYPE": "SINE",
            "MAX_TEMP": 35.0,    # 최대 온도 35°C
            "MEAN_TEMP": 20.0,   # 평균 온도 20°C
            "DELAY_TIME": 6.0    # 지연 시간 6시간
        },
        "2": {
            "NAME": "AT_Winter",
            "TYPE": "CONST",
            "TEMP": 5.0          # 일정 온도 5°C
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/ETFC", json=payload, headers=HEADERS)
print("ETFC POST:", resp.status_code)
```

---

## 8. /db/CCFC – Convection Coefficient Functions

수화열 해석에 사용되는 대류 계수 함수를 정의합니다.

### 8-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/CCFC` | 전체 조회 |
| `GET` | `{base_url}/db/CCFC/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/CCFC` | 생성 |
| `PUT` | `{base_url}/db/CCFC` | 전체 수정 |
| `PUT` | `{base_url}/db/CCFC/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/CCFC` | 전체 삭제 |
| `DELETE` | `{base_url}/db/CCFC/{id}` | 특정 ID 삭제 |

### 8-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 함수명 | `NAME` | String | - | Required |
| 2 | 함수 타입 (`"CONST"` / `"USER"`) | `TYPE` | String | - | Required |

**Constant 타입 (TYPE="CONST") 추가 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 대류 계수 | `COEF` | Number | - | Required |

**User 타입 (TYPE="USER") 추가 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 스케일 계수 | `SCALE_FACTOR` | Number | - | Required |
| 함수 데이터 목록 | `ITEM` | Array[Object] | - | Required |
| - 시간 | `TIME` | Number | - | Required |
| - 대류 계수 | `VALUE` | Number | - | Required |

### 8-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "NAME": "CC_Const",
      "TYPE": "CONST",
      "COEF": 15
    },
    "2": {
      "NAME": "CC_User",
      "TYPE": "USER",
      "SCALE_FACTOR": 1.2,
      "ITEM": [
        {"TIME": 0, "VALUE": 25},
        {"TIME": 1, "VALUE": 35}
      ]
    }
  }
}
```

### 8-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 대류 계수 함수 생성 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "CC_Standard",
            "TYPE": "CONST",
            "COEF": 12.0    # 대류 계수 12 W/(m²·K)
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/CCFC", json=payload, headers=HEADERS)
print("CCFC POST:", resp.status_code)
```

---

## 9. /db/HECB – Element Convection Boundary

수화열 해석에서 요소의 대류 경계 조건을 정의합니다.

### 9-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/HECB` | 전체 조회 |
| `GET` | `{base_url}/db/HECB/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/HECB` | 생성 |
| `PUT` | `{base_url}/db/HECB` | 전체 수정 |
| `PUT` | `{base_url}/db/HECB/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/HECB` | 전체 삭제 |
| `DELETE` | `{base_url}/db/HECB/{id}` | 특정 ID 삭제 |

### 9-2. 파라미터

> Assign의 키(ID)는 시공단계 번호입니다.

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 요소 대류 경계 목록 | `ITEMS` | Array[Object] | - | Required |
| (1) | 일련번호 | `ID` | Integer | 0 | Optional |
| (2) | 경계 그룹명 | `GROUP_NAME` | String | Blank | Optional |
| (3) | 면 번호 (Face#1 ~ Face#6) | `FACE_NO` | Integer | - | Required |
| (4) | 대류 계수 함수명 | `CCFC_NAME` | String | - | Required |
| (5) | 외기 온도 함수명 | `ETFC_NAME` | String | - | Required |

### 9-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "",
          "FACE_NO": 1,
          "CCFC_NAME": "CC_Standard",
          "ETFC_NAME": "AT_Summer"
        },
        {
          "ID": 2,
          "GROUP_NAME": "",
          "FACE_NO": 2,
          "CCFC_NAME": "CC_Standard",
          "ETFC_NAME": "AT_Summer"
        }
      ]
    }
  }
}
```

### 9-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 요소 대류 경계 생성 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {    # 시공단계 1번
            "ITEMS": [
                {
                    "ID": 1,
                    "GROUP_NAME": "BG_SURF",
                    "FACE_NO": 1,              # 상면 (Face #1)
                    "CCFC_NAME": "CC_Standard",
                    "ETFC_NAME": "AT_Summer"
                },
                {
                    "ID": 2,
                    "GROUP_NAME": "BG_SIDE",
                    "FACE_NO": 2,              # 측면 (Face #2)
                    "CCFC_NAME": "CC_Standard",
                    "ETFC_NAME": "AT_Summer"
                }
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/HECB", json=payload, headers=HEADERS)
print("HECB POST:", resp.status_code)
```

---

## 10. /db/HSPT – Prescribed Temperature

수화열 해석에서 절점의 지정 온도를 정의합니다.

### 10-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/HSPT` | 전체 조회 |
| `GET` | `{base_url}/db/HSPT/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/HSPT` | 생성 |
| `PUT` | `{base_url}/db/HSPT` | 전체 수정 |
| `PUT` | `{base_url}/db/HSPT/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/HSPT` | 전체 삭제 |
| `DELETE` | `{base_url}/db/HSPT/{id}` | 특정 ID 삭제 |

### 10-2. 파라미터

> Assign의 키(ID)는 시공단계 번호입니다.

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 지정 온도 목록 | `ITEMS` | Array[Object] | - | Required |
| (1) | 일련번호 | `ID` | Integer | 0 | Optional |
| (2) | 경계 그룹명 | `GROUP_NAME` | String | Blank | Optional |
| (3) | 온도 | `TEMPER` | Number | - | Required |

### 10-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "", "TEMPER": 25}
      ]
    },
    "2": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "", "TEMPER": 25}
      ]
    },
    "3": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "", "TEMPER": 20}
      ]
    }
  }
}
```

### 10-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 지정 온도 생성 ───────────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {    # 시공단계 1번
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "BG_BASE", "TEMPER": 15.0}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/HSPT", json=payload, headers=HEADERS)
print("HSPT POST:", resp.status_code)
```

---

## 11. /db/HSFC – Heat Source Functions

수화열 해석에 사용되는 열원 함수를 정의합니다. Constant, Code(함수), User 타입을 지원합니다.

### 11-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/HSFC` | 전체 조회 |
| `GET` | `{base_url}/db/HSFC/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/HSFC` | 생성 |
| `PUT` | `{base_url}/db/HSFC` | 전체 수정 |
| `PUT` | `{base_url}/db/HSFC/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/HSFC` | 전체 삭제 |
| `DELETE` | `{base_url}/db/HSFC/{id}` | 특정 ID 삭제 |

### 11-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 함수명 | `NAME` | String | - | Required |
| 2 | 함수 타입 (`"CONST"` / `"FUNC"` / `"USER"`) | `TYPE` | String | - | Required |

**Constant 타입 (TYPE="CONST") 추가 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 열원 온도 | `TEMP_CONST` | Number | 0 | Optional |

**Code 타입 (TYPE="FUNC") – 콘크리트 데이터 미사용 추가 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 콘크리트 데이터 사용 여부 (`false`) | `OPT_USE_CONC_DATA` | Boolean | false | Optional |
| 최대 단열 온도 상승 (K) | `K` | Number | 0 | Optional |
| 반응 속도 계수 (a) | `ALPHA` | Number | 0 | Optional |

**Code 타입 (TYPE="FUNC") – 콘크리트 데이터 사용 추가 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 콘크리트 데이터 사용 여부 (`true`) | `OPT_USE_CONC_DATA` | Boolean | false | Optional |
| 시멘트 타입 (0=보통, 1=중용열, 2=조기강도, 3=고로슬래그, 4=플라이애시) | `CEMENT_TYPE` | Integer | 0 | Optional |
| 온도 (0=10°C, 1=20°C, 2=30°C) | `TEMP_FUNC` | Integer | 0 | Optional |
| 시멘트 함유량 | `CEMENT_CONT` | Number | 0 | Optional |

**User 타입 (TYPE="USER") 추가 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 데이터 타입 (false=열원, true=온도) | `IS_ADIABATIC_TEMP` | Boolean | true | Optional |
| 스케일 계수 | `SCALE_FACTOR` | Number | - | Required |
| 함수 데이터 목록 | `ITEM` | Array[Object] | - | Required |
| - 시간 | `TIME` | Number | - | Required |
| - 값 (온도 또는 열원) | `VALUE` | Number | - | Required |

### 11-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "NAME": "HS_User",
      "TYPE": "USER",
      "IS_ADIABATIC_TEMP": false,
      "SCALE_FACTOR": 1,
      "ITEM": [
        {"TIME": 0, "VALUE": 0},
        {"TIME": 1, "VALUE": 5},
        {"TIME": 2, "VALUE": 10}
      ]
    },
    "2": {
      "NAME": "HS_Const",
      "TYPE": "CONST",
      "TEMP_CONST": 10
    },
    "3": {
      "NAME": "HS_Code_NoConc",
      "TYPE": "FUNC",
      "OPT_USE_CONC_DATA": false,
      "K": 20,
      "ALPHA": 0
    },
    "4": {
      "NAME": "HS_Code_Conc",
      "TYPE": "FUNC",
      "OPT_USE_CONC_DATA": true,
      "CEMENT_TYPE": 0,
      "TEMP_FUNC": 1,
      "CEMENT_CONT": 2400
    }
  }
}
```

### 11-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 열원 함수 생성 (3가지 타입) ──────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "HSF_Adiabatic",
            "TYPE": "FUNC",
            "OPT_USE_CONC_DATA": True,
            "CEMENT_TYPE": 0,   # 보통 포틀랜드 시멘트
            "TEMP_FUNC": 1,     # 20°C
            "CEMENT_CONT": 300  # 시멘트 함유량 300 kg/m³
        },
        "2": {
            "NAME": "HSF_UserDefined",
            "TYPE": "USER",
            "IS_ADIABATIC_TEMP": True,   # 단열 온도 데이터
            "SCALE_FACTOR": 1.0,
            "ITEM": [
                {"TIME": 0,  "VALUE":  0.0},
                {"TIME": 1,  "VALUE":  8.5},
                {"TIME": 3,  "VALUE": 18.2},
                {"TIME": 7,  "VALUE": 25.6},
                {"TIME": 14, "VALUE": 30.1},
                {"TIME": 28, "VALUE": 33.5}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/HSFC", json=payload, headers=HEADERS)
print("HSFC POST:", resp.status_code)

# ── 전체 조회 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/HSFC", headers=HEADERS)
print("HSFC GET:", resp.status_code)
```

---

## 12. /db/HAHS – Assign Heat Source

요소에 열원 함수를 지정합니다.

### 12-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/HAHS` | 전체 조회 |
| `GET` | `{base_url}/db/HAHS/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/HAHS` | 생성 |
| `PUT` | `{base_url}/db/HAHS` | 전체 수정 |
| `PUT` | `{base_url}/db/HAHS/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/HAHS` | 전체 삭제 |
| `DELETE` | `{base_url}/db/HAHS/{id}` | 특정 ID 삭제 |

### 12-2. 파라미터

> Assign의 키(ID)는 요소 번호입니다.

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 열원 함수명 | `FUNC_NAME` | String | - | Required |

### 12-3. Request Body 예시

```json
{
  "Assign": {
    "358": {"FUNC_NAME": "HSF_Adiabatic"},
    "359": {"FUNC_NAME": "HSF_Adiabatic"},
    "360": {"FUNC_NAME": "HSF_UserDefined"}
  }
}
```

### 12-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 요소에 열원 함수 지정 ────────────────────────────────────────────────────
# Assign 키는 요소 번호
elem_ids = list(range(100, 150))  # 요소 100 ~ 149번
payload = {
    "Assign": {
        str(eid): {"FUNC_NAME": "HSF_Adiabatic"}
        for eid in elem_ids
    }
}

resp = requests.post(f"{BASE_URL}/db/HAHS", json=payload, headers=HEADERS)
print("HAHS POST:", resp.status_code)

# ── 특정 요소 조회 ───────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/HAHS/100", headers=HEADERS)
print("HAHS GET/100:", resp.json())
```

---

## 13. /db/HPCE – Pipe Cooling

수화열 해석에서 파이프 쿨링 시스템을 정의합니다.

### 13-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/HPCE` | 전체 조회 |
| `GET` | `{base_url}/db/HPCE/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/HPCE` | 생성 |
| `PUT` | `{base_url}/db/HPCE` | 전체 수정 |
| `PUT` | `{base_url}/db/HPCE/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/HPCE` | 전체 삭제 |
| `DELETE` | `{base_url}/db/HPCE/{id}` | 특정 ID 삭제 |

### 13-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 파이프 쿨링 이름 | `NAME` | String | - | Required |
| 2 | 파이프 직경 | `DIAMETER` | Number | 0 | Optional |
| 3 | 대류 계수 | `COEF` | Number | 0 | Optional |
| 4 | 비열 | `HEAT` | Number | 0 | Optional |
| 5 | 단위 중량 밀도 | `DENSITY` | Number | 0 | Optional |
| 6 | 유입 온도 | `TEMPER` | Number | 0 | Optional |
| 7 | 유량 | `FLOW_RATE` | Number | 0 | Optional |
| 8 | 유입 시작 시간 | `START_TIME` | Integer | 0 | Optional |
| 9 | 유입 종료 시간 | `END_TIME` | Integer | 0 | Optional |
| 10 | 절점 목록 | `ITEMS` | Array[Integer] | - | Required |

### 13-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "NAME": "PC_Row1",
      "DIAMETER": 0.025,
      "COEF": 850,
      "HEAT": 4200,
      "DENSITY": 1000,
      "TEMPER": 15,
      "FLOW_RATE": 20,
      "START_TIME": 0,
      "END_TIME": 168,
      "ITEMS": [1, 2, 3, 4, 5, 6]
    }
  }
}
```

### 13-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 파이프 쿨링 생성 ─────────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "PC_Layer1",
            "DIAMETER": 0.025,    # 파이프 직경 25mm
            "COEF": 850,          # 대류 계수 850 W/(m²·K)
            "HEAT": 4200,         # 비열 4200 J/(kg·K) (물)
            "DENSITY": 1000,      # 밀도 1000 kg/m³ (물)
            "TEMPER": 15.0,       # 유입 온도 15°C
            "FLOW_RATE": 15.0,    # 유량 15 L/min
            "START_TIME": 0,      # 유입 시작 0시간
            "END_TIME": 168,      # 유입 종료 7일(168시간)
            "ITEMS": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/HPCE", json=payload, headers=HEADERS)
print("HPCE POST:", resp.status_code)
```

---

## 14. /db/HSTG – Define Construction Stage for Hydration

수화열 해석 전용 시공단계를 정의합니다.

### 14-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/HSTG` | 전체 조회 |
| `GET` | `{base_url}/db/HSTG/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/HSTG` | 생성 |
| `PUT` | `{base_url}/db/HSTG` | 전체 수정 |
| `PUT` | `{base_url}/db/HSTG/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/HSTG` | 전체 삭제 |
| `DELETE` | `{base_url}/db/HSTG/{id}` | 특정 ID 삭제 |

### 14-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 수화열 단계명 | `NAME` | String | - | Required |
| 2 | 초기 온도 사용 여부 | `bINITAL_TEMP` | Boolean | false | Optional |
| 3 | 초기 온도 | `INITIAL_TEMP` | Number | - | Optional |
| 4 | 추가 스텝 목록 | `ADD_STEP` | Array[Number] | - | Required |
| 5 | 활성화 구조 그룹 목록 | `ACT_ELEM` | Array[String] | - | Required |
| 6 | 활성화 경계 그룹 목록 | `ACT_BNGR` | Array[String] | - | Required |
| 7 | 비활성화 경계 그룹 목록 | `DACT_BNGR` | Array[String] | - | Required |
| 8 | 활성화 하중 그룹 목록 | `ACT_LOAD` | Array[Object] | [] | Optional |
| (1) | 하중 케이스명 | `LOAD_NAME` | String | - | Optional |
| (2) | 활성화 일 | `DAY` | String | - | Optional |
| 9 | 비활성화 하중 그룹 목록 | `DACT_LOAD` | Array[Object] | [] | Optional |
| (1) | 하중 케이스명 | `LOAD_NAME` | String | - | Optional |
| (2) | 비활성화 일 | `DAY` | String | - | Optional |

### 14-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "NAME": "HY_CS01",
      "bINITAL_TEMP": true,
      "INITIAL_TEMP": 25,
      "ADD_STEP": [10, 20, 30, 45, 60, 80, 100, 130, 170, 250, 350, 500, 700, 1000],
      "ACT_ELEM": ["GR2", "GR1"],
      "ACT_BNGR": ["BNGR3", "BNGR2", "BNGR1"],
      "DACT_BNGR": ["BNGR4"],
      "ACT_LOAD": [
        {"LOAD_NAME": "LG01", "DAY": "10.000000"}
      ],
      "DACT_LOAD": [
        {"LOAD_NAME": "LG02", "DAY": "80.000000"}
      ]
    }
  }
}
```

### 14-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 수화열 시공단계 생성 ─────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "HY_Pour_01",
            "bINITAL_TEMP": True,
            "INITIAL_TEMP": 20.0,       # 초기 타설 온도 20°C
            "ADD_STEP": [
                1, 3, 7, 14, 28, 60, 90, 180, 365
            ],
            "ACT_ELEM": ["ConcGroup_01"],
            "ACT_BNGR": ["FormWork_01"],
            "DACT_BNGR": [],
            "ACT_LOAD": [
                {"LOAD_NAME": "HeatSrc_01", "DAY": "1.000000"}
            ],
            "DACT_LOAD": [
                {"LOAD_NAME": "FormWork_Load", "DAY": "14.000000"}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/HSTG", json=payload, headers=HEADERS)
print("HSTG POST:", resp.status_code)

# ── 전체 조회 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/HSTG", headers=HEADERS)
print("HSTG GET:", resp.status_code)
```

---

## End-to-End 워크플로우 예제

교량 시공단계 해석 + 수화열 해석의 전형적인 설정 흐름입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── STEP 1: 시공단계 정의 (STAG) ────────────────────────────────────────────
stag = {
    "Assign": {
        "1": {
            "NAME": "CS01_Pier",
            "DURATION": 14,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_ELEM": [{"GRUP_NAME": "PIER", "AGE": 14}],
            "ACT_BNGR": [{"BNGR_NAME": "FND", "POS": "DEFORMED"}],
            "ACT_LOAD": [{"LOAD_NAME": "SW_PIER", "DAY": "FIRST"}]
        },
        "2": {
            "NAME": "CS02_Girder",
            "DURATION": 28,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_ELEM": [{"GRUP_NAME": "GIRDER", "AGE": 28}],
            "ACT_BNGR": [{"BNGR_NAME": "BRG", "POS": "DEFORMED"}],
            "ACT_LOAD": [{"LOAD_NAME": "SW_GIRDER", "DAY": "FIRST"}]
        },
        "3": {
            "NAME": "CS03_SDL",
            "DURATION": 90,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_LOAD": [{"LOAD_NAME": "SDL", "DAY": "FIRST"}]
        }
    }
}
r = requests.post(f"{BASE_URL}/db/STAG", json=stag, headers=HEADERS)
print("STEP 1 - STAG:", r.status_code)

# ── STEP 2: 시공단계별 크리프 계수 (CRPC) ───────────────────────────────────
crpc = {
    "Assign": {
        "2": {    # CS02 단계
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SW_PIER",   "CREEP": 1.5},
                {"ID": 2, "GROUP_NAME": "SW_GIRDER",  "CREEP": 1.2}
            ]
        },
        "3": {    # CS03 단계
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SDL", "CREEP": 2.0}
            ]
        }
    }
}
r = requests.post(f"{BASE_URL}/db/CRPC", json=crpc, headers=HEADERS)
print("STEP 2 - CRPC:", r.status_code)

# ── STEP 3: 수화열 외기 온도 함수 (ETFC) ────────────────────────────────────
etfc = {
    "Assign": {
        "1": {"NAME": "AT_25C", "TYPE": "CONST", "TEMP": 25}
    }
}
r = requests.post(f"{BASE_URL}/db/ETFC", json=etfc, headers=HEADERS)
print("STEP 3 - ETFC:", r.status_code)

# ── STEP 4: 수화열 대류 계수 함수 (CCFC) ────────────────────────────────────
ccfc = {
    "Assign": {
        "1": {"NAME": "CC_12", "TYPE": "CONST", "COEF": 12.0}
    }
}
r = requests.post(f"{BASE_URL}/db/CCFC", json=ccfc, headers=HEADERS)
print("STEP 4 - CCFC:", r.status_code)

# ── STEP 5: 열원 함수 (HSFC) ─────────────────────────────────────────────────
hsfc = {
    "Assign": {
        "1": {
            "NAME": "HS_OPC",
            "TYPE": "FUNC",
            "OPT_USE_CONC_DATA": True,
            "CEMENT_TYPE": 0,    # 보통 포틀랜드
            "TEMP_FUNC": 1,      # 20°C
            "CEMENT_CONT": 320
        }
    }
}
r = requests.post(f"{BASE_URL}/db/HSFC", json=hsfc, headers=HEADERS)
print("STEP 5 - HSFC:", r.status_code)

# ── STEP 6: 요소에 열원 지정 (HAHS) ─────────────────────────────────────────
hahs = {
    "Assign": {
        str(eid): {"FUNC_NAME": "HS_OPC"}
        for eid in range(1, 51)    # 요소 1~50번
    }
}
r = requests.post(f"{BASE_URL}/db/HAHS", json=hahs, headers=HEADERS)
print("STEP 6 - HAHS:", r.status_code)

# ── STEP 7: 요소 대류 경계 (HECB) ───────────────────────────────────────────
hecb = {
    "Assign": {
        "1": {    # 시공단계 1번
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "", "FACE_NO": 1, "CCFC_NAME": "CC_12", "ETFC_NAME": "AT_25C"},
                {"ID": 2, "GROUP_NAME": "", "FACE_NO": 2, "CCFC_NAME": "CC_12", "ETFC_NAME": "AT_25C"}
            ]
        }
    }
}
r = requests.post(f"{BASE_URL}/db/HECB", json=hecb, headers=HEADERS)
print("STEP 7 - HECB:", r.status_code)

# ── STEP 8: 수화열 시공단계 정의 (HSTG) ─────────────────────────────────────
hstg = {
    "Assign": {
        "1": {
            "NAME": "HY_CS01",
            "bINITAL_TEMP": True,
            "INITIAL_TEMP": 25,
            "ADD_STEP": [1, 3, 7, 14, 28, 60, 90],
            "ACT_ELEM": ["PIER", "GIRDER"],
            "ACT_BNGR": ["FND", "BRG"],
            "DACT_BNGR": [],
            "ACT_LOAD":  [],
            "DACT_LOAD": []
        }
    }
}
r = requests.post(f"{BASE_URL}/db/HSTG", json=hstg, headers=HEADERS)
print("STEP 8 - HSTG:", r.status_code)

print("\n=== 시공단계 / 수화열 설정 완료 ===")
```

---

*다음 파트: [11_DB_Settlement_Misc_Loads.md](11_DB_Settlement_Misc_Loads.md)*
