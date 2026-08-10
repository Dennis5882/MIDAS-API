# 17. DB – Bridge Specialization Results

> **대상 제품:** MIDAS Civil NX (교량 특화)  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

이 파트는 교량 특화 결과 설정을 다룹니다. 거더 다이어그램(Girder Diagram) 정의·이미지 Export, 캠버 제어(General / FCM Camber), 케이블 미지하중계수 제약(Unknown Load Factor Constraints)을 포함합니다.

---

## Endpoint 목록

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/db/GSBG`](#1-dbgsbg--bridge-girder-diagrams) | 교량 거더 다이어그램 | POST, GET, PUT, DELETE |
| 2 | [`/db/GCMB`](#2-dbgcmb--general-camber-control) | 일반 캠버 제어 | POST, GET, PUT, DELETE |
| 3 | [`/db/CAMB`](#3-dbcamb--fcm-camber-control) | FCM 캠버 제어 | POST, GET, PUT, DELETE |
| 4 | [`/db/ULFC`](#4-dbulfc--cable-control--unknown-load-factor-constraints) | 케이블 제어 – 미지하중계수 제약 | POST, GET, PUT, DELETE |
| 5 | [`/ope/GSBG`](#5-opegsbg--bridge-girder-diagram-image-export) | 교량 거더 다이어그램 이미지 Export | POST |

---

## 1. `/db/GSBG` — Bridge Girder Diagrams

> **기능:** 교량 거더(Bridge Girder) 요소 그룹에 대한 결과 다이어그램(보 응력 또는 보 부재력/모멘트)을 정의합니다. 결과 타입에 따라 응력 성분(`BSTRSCOMP`) 또는 부재력 성분(`MOMENT_COMP`)을 지정합니다.

### Input URI

```
{base url}/db/GSBG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "GSBG": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "Name", "type": "string" },
      "BATCH": { "description": "Is Batch Boolean", "type": "boolean" },
      "BODY_ELEM_GRUP_K": { "description": "Body Element Group_K", "type": "integer" },
      "ALLSTAGE": { "description": "Is All Stage Boolean", "type": "boolean" },
      "BSTRSCOMP": { "description": "TODO: BSTRSCOMP", "type": "integer" },
      "BSTRSCOMP_SUB": { "description": "TODO: BSTRSCOMP_SUB", "type": "integer" },
      "MOMENT_COMP": { "description": "TODO: MOMENT_COMP", "type": "integer" },
      "_7TH_DOF_TYPE": { "description": "TODO: 7TH_DOF_TYPE", "type": "integer" },
      "DGRM_TYPE": { "description": "TODO: DGRM_TYPE", "type": "integer" },
      "SCALEFACTOR": { "description": "Scale", "type": "number" }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 그룹 이름 | `"NAME"` | String | — | **Required** |
| 2 | 일괄 처리(Batch) | `"BATCH"` | Boolean | `true` | **Required** |
| 3 | 교량 거더 요소 그룹 | `"BODY_ELEM_GRUP_K"` | Integer | — | **Required** |
| 4 | 생성 옵션 · 현재 단계-스텝: `false` / 전체 단계(마지막 스텝): `true` | `"ALLSTAGE"` | Boolean | `false` | Optional |
| 5 | 결과 타입 · 보 응력: `0` / 보 부재력·모멘트: `1` | `"DGRM_TYPE"` | Integer | `0` | Optional |
| 6 | (응력일 때) 보 응력 성분 · Sax: `0` / +Sby: `1` / −Sby: `2` / +Sbz: `3` / −Sbz: `4` / Combined: `5` / 7th DOF: `6` | `"BSTRSCOMP"` | Integer | `0` | Optional |
| 7 | (응력·7th DOF일 때) 응력 표시 위치 · Maximum: `0` / 1(−y,+z): `1` / 2(+y,+z): `2` / 3(+y,−z): `3` / 4(−y,−z): `4` | `"BSTRSCOMP_SUB"` | Integer | `0` | Optional |
| 8 | (응력·7th DOF일 때) 7th DOF 타입 · Sax(Warping): `0` / Ssy(Mt): `1` / Ssy(Mw): `2` / Ssz(Mt): `3` / Ssz(Mw): `4` / Combined(Ssy): `5` / Combined(Ssz): `6` | `"_7TH_DOF_TYPE"` | Integer | `0` | Optional |
| 9 | (부재력일 때) 보 부재력·모멘트 성분 · Fx: `0` / Fy: `1` / Fz: `2` / Mx: `3` / My: `4` / Mz: `5` / Mb: `6` / Mt: `7` / Mw: `8` | `"MOMENT_COMP"` | Integer | `0` | Optional |
| 10 | 스케일 | `"SCALEFACTOR"` | Number | `0` | Optional |

### Request / Response JSON

**POST / PUT Request Body — 보 응력(Beam Stresses)**

```json
{
  "Assign": {
    "1": {
      "NAME": "Dgrm Group1",
      "BATCH": true,
      "BODY_ELEM_GRUP_K": 1,
      "ALLSTAGE": false,
      "DGRM_TYPE": 0,
      "BSTRSCOMP": 6,
      "BSTRSCOMP_SUB": 3,
      "_7TH_DOF_TYPE": 0,
      "SCALEFACTOR": 1
    }
  }
}
```

**POST / PUT Request Body — 보 부재력/모멘트(Beam Forces/Moments)**

```json
{
  "Assign": {
    "2": {
      "NAME": "Dgrm Group2",
      "BATCH": true,
      "BODY_ELEM_GRUP_K": 2,
      "ALLSTAGE": true,
      "DGRM_TYPE": 1,
      "MOMENT_COMP": 4,
      "SCALEFACTOR": 1
    }
  }
}
```

**GET Response Body**

```json
{
  "GSBG": {
    "1": {
      "NAME": "Dgrm Group1",
      "BATCH": true,
      "BODY_ELEM_GRUP_K": 1,
      "ALLSTAGE": false,
      "DGRM_TYPE": 0,
      "BSTRSCOMP": 6,
      "BSTRSCOMP_SUB": 3,
      "_7TH_DOF_TYPE": 0,
      "SCALEFACTOR": 1
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

# ── POST: 거더 다이어그램 2종 생성 (응력 / 부재력) ─────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "Dgrm Group1",
            "BATCH": True,
            "BODY_ELEM_GRUP_K": 1,
            "ALLSTAGE": False,
            "DGRM_TYPE": 0,          # 보 응력
            "BSTRSCOMP": 6,          # 7th DOF
            "BSTRSCOMP_SUB": 3,      # 응력 위치 3(+y,-z)
            "_7TH_DOF_TYPE": 0,      # Sax(Warping)
            "SCALEFACTOR": 1
        },
        "2": {
            "NAME": "Dgrm Group2",
            "BATCH": True,
            "BODY_ELEM_GRUP_K": 2,
            "ALLSTAGE": True,        # 전체 단계(마지막 스텝)
            "DGRM_TYPE": 1,          # 보 부재력/모멘트
            "MOMENT_COMP": 4,        # My
            "SCALEFACTOR": 1
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/GSBG", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 거더 다이어그램 조회 ──────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/GSBG", headers=HEADERS)
for key, val in resp.json().get("GSBG", {}).items():
    dtype = "응력" if val["DGRM_TYPE"] == 0 else "부재력"
    print(f"  [{key}] {val['NAME']} ({dtype})")
```

---

## 2. `/db/GCMB` — General Camber Control

> **기능:** 시공단계 그룹별 캠버(Camber) 기준을 정의합니다. 각 구조 그룹에 대해 캠버 방향(±DX/±DY)을 지정하며, 시작점을 0으로 설정하는 옵션을 제공합니다.

### Input URI

```
{base url}/db/GCMB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "GCMB": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "bSTART_PT_ZERO": { "description": "StartPtZero", "type": "boolean" },
      "GCMB_BASE_ITEMS": {
        "description": "GcmbBaseItems",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "GRUP_NAME": { "description": "GroupName", "type": "string" },
            "DIRECTION": { "description": "Dir", "type": "string" }
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
| 1 | 시작점 0 설정 | `"bSTART_PT_ZERO"` | Boolean | `true` | Optional |
| 2 | 일반 캠버 기준 항목 배열 | `"GCMB_BASE_ITEMS"` | Array [Object] | — | **Required** |
| 2-1 | └ 구조 그룹 이름 | `GCMB_BASE_ITEMS[].GRUP_NAME` | String | — | **Required** |
| 2-2 | └ 방향 · `"+DX"` / `"-DX"` / `"+DY"` / `"-DY"` | `GCMB_BASE_ITEMS[].DIRECTION` | String | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "bSTART_PT_ZERO": true,
      "GCMB_BASE_ITEMS": [
        { "GRUP_NAME": "CS_0", "DIRECTION": "+DX" },
        { "GRUP_NAME": "CS_1", "DIRECTION": "+DX" },
        { "GRUP_NAME": "CS_2", "DIRECTION": "+DX" },
        { "GRUP_NAME": "CS_3", "DIRECTION": "+DX" }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "GCMB": {
    "1": {
      "bSTART_PT_ZERO": true,
      "GCMB_BASE_ITEMS": [
        { "GRUP_NAME": "CS_0", "DIRECTION": "+DX" },
        { "GRUP_NAME": "CS_1", "DIRECTION": "+DX" }
      ]
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

# ── POST: 시공단계 그룹별 캠버 방향 일괄 설정 ──────────────────────
stage_groups = [f"CS_{i}" for i in range(19)]   # CS_0 ~ CS_18
payload = {
    "Assign": {
        "1": {
            "bSTART_PT_ZERO": True,
            "GCMB_BASE_ITEMS": [
                {"GRUP_NAME": g, "DIRECTION": "+DX"} for g in stage_groups
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/GCMB", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 캠버 기준 조회 ────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/GCMB", headers=HEADERS)
data = resp.json().get("GCMB", {})
for key, val in data.items():
    print(f"  [{key}] StartPtZero={val['bSTART_PT_ZERO']}, 항목수={len(val['GCMB_BASE_ITEMS'])}")
```

---

## 3. `/db/CAMB` — FCM Camber Control

> **기능:** FCM(Free Cantilever Method, 캔틸레버 가설공법) 교량의 캠버를 제어합니다. 거더 요소 그룹, 지점 노드 그룹, 키 세그먼트(Key Segment) 요소 그룹을 지정합니다.

### Input URI

```
{base url}/db/CAMB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "CAMB": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "BODY_GROUP_NAME": { "description": "BodyElementGroupName", "type": "string" },
      "SUPP_GROUP_NAME": { "description": "SupportNodeGroup_KName", "type": "string" },
      "KEYSEG_GROUP_NAME": { "description": "KeySegGroupName", "type": "string" }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 교량 거더 요소 그룹 | `"BODY_GROUP_NAME"` | String | — | **Required** |
| 2 | 지점 노드 그룹 | `"SUPP_GROUP_NAME"` | String | — | **Required** |
| 3 | 키 세그먼트 요소 그룹 | `"KEYSEG_GROUP_NAME"` | String | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "BODY_GROUP_NAME": "FSM",
      "SUPP_GROUP_NAME": "PSC-BN",
      "KEYSEG_GROUP_NAME": "Key-SegK1~K5"
    }
  }
}
```

**GET Response Body**

```json
{
  "CAMB": {
    "1": {
      "BODY_GROUP_NAME": "FSM",
      "SUPP_GROUP_NAME": "PSC-BN",
      "KEYSEG_GROUP_NAME": "Key-SegK1~K5"
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

# ── POST: FCM 캠버 제어 설정 ───────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "BODY_GROUP_NAME": "FSM",              # 거더 요소 그룹
            "SUPP_GROUP_NAME": "PSC-BN",           # 지점 노드 그룹
            "KEYSEG_GROUP_NAME": "Key-SegK1~K5"    # 키 세그먼트 그룹
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/CAMB", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: FCM 캠버 제어 조회 ────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/CAMB", headers=HEADERS)
print("GET:", resp.json())
```

---

## 4. `/db/ULFC` — Cable Control – Unknown Load Factor Constraints

> **기능:** 케이블 교량의 미지하중계수(Unknown Load Factor) 해석에 사용할 제약조건을 정의합니다. 반력·변위·트러스력·보력에 대해 등호(Equality) 또는 부등호(Inequality, 상·하한) 조건을 지정합니다.

### Input URI

```
{base url}/db/ULFC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "ULFC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "ConstraintName", "type": "string" },
      "TYPE": { "description": "ConstraintType", "type": "string" },
      "OBJ_ID": { "description": "ObjectID", "type": "integer" },
      "POINT": { "description": "nPoint", "type": "integer" },
      "COMP": { "description": "Component", "type": "integer" },
      "EQ": { "description": "EqualityConditionBoolean", "type": "boolean" },
      "bVALUE": { "description": "ValueBoolean", "type": "boolean" },
      "VALUE": { "description": "ValueDouble", "type": "number" },
      "OtherObject": { "description": "OtherObject", "type": "integer" },
      "bUB": { "description": "UpperBoundBoolean", "type": "boolean" },
      "UB_VALUE": { "description": "UpperBoundValue", "type": "number" },
      "bLB": { "description": "LowerBoundBoolean", "type": "boolean" },
      "LB_VALUE": { "description": "LowerBoundValue", "type": "number" }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 제약조건 이름 | `"NAME"` | String | — | **Required** |
| 2 | 제약조건 타입 · 반력: `"REAC"` / 변위: `"DISP"` / 트러스력: `"TRUSS"` / 보력: `"BEAM"` | `"TYPE"` | String | — | **Required** |
| 3 | 요소/노드 ID | `"OBJ_ID"` | Integer | — | **Required** |
| 4 | 위치(Point) · (`TYPE="BEAM"`일 때) I단: `0` / 1/4: `1` / 2/4: `2` / 3/4: `3` / J단: `4` | `"POINT"` | Integer | — | **Required** |
| 5 | 성분(Component) · 반력·보력/변위/트러스 기준 · FX/DX/I단: `0` / FY/DY/J단: `1` / FZ/DZ: `2` / MX/RX: `3` / MY/RY: `4` / MZ/RZ: `5` | `"COMP"` | Integer | — | **Required** |
| 6 | 등호/부등호 조건 · 등호: `true` / 부등호: `false` | `"EQ"` | Boolean | `false` | Optional |
| **등호(Equality) 조건 (`EQ=true`)** |
| 7 | 값 확인(Check Value) | `"bVALUE"` | Boolean | `false` | Optional |
| 8 | 값(Value) | `"VALUE"` | Number | — | **Required** |
| 9 | 다른 객체(`bVALUE=false`일 때) | `"OtherObject"` | Integer | `0` | Optional |
| **부등호(Inequality) 조건 (`EQ=false`)** |
| 7 | 상한 확인(Check Upper Bound) | `"bUB"` | Boolean | `false` | Optional |
| 8 | 상한 값(Upper Bound Value) | `"UB_VALUE"` | Number | — | **Required** |
| 9 | 하한 확인(Check Lower Bound) | `"bLB"` | Boolean | `false` | Optional |
| 10 | 하한 값(Lower Bound Value) | `"LB_VALUE"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "2": {
      "NAME": "Ele-03",
      "TYPE": "BEAM",
      "OBJ_ID": 3,
      "POINT": 1,
      "COMP": 4,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": -220,
      "bLB": true,
      "LB_VALUE": -230
    },
    "3": {
      "NAME": "Node-07",
      "TYPE": "REAC",
      "OBJ_ID": 7,
      "POINT": 4,
      "COMP": 1,
      "EQ": true,
      "bVALUE": true,
      "VALUE": 500,
      "OtherObject": 0
    },
    "4": {
      "NAME": "Ele-11",
      "TYPE": "DISP",
      "OBJ_ID": 11,
      "POINT": 4,
      "COMP": 2,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": -0.05,
      "bLB": true,
      "LB_VALUE": 0.05
    },
    "7": {
      "NAME": "Node106",
      "TYPE": "DISP",
      "OBJ_ID": 106,
      "POINT": 0,
      "COMP": 0,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": 0.0001,
      "bLB": true,
      "LB_VALUE": -0.0001
    }
  }
}
```

**GET Response Body**

```json
{
  "ULFC": {
    "2": {
      "NAME": "Ele-03",
      "TYPE": "BEAM",
      "OBJ_ID": 3,
      "POINT": 1,
      "COMP": 4,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": -220,
      "bLB": true,
      "LB_VALUE": -230
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

# ── POST: 미지하중계수 제약조건 정의 (부등호 + 등호 혼합) ──────────
payload = {
    "Assign": {
        # 부등호: 보 요소 3번 I단 부근 My를 -230 ~ -220 범위로 제약
        "2": {
            "NAME": "Ele-03", "TYPE": "BEAM", "OBJ_ID": 3,
            "POINT": 1, "COMP": 4, "EQ": False,
            "bUB": True, "UB_VALUE": -220,
            "bLB": True, "LB_VALUE": -230
        },
        # 등호: 노드 7번 반력 FY를 500으로 제약
        "3": {
            "NAME": "Node-07", "TYPE": "REAC", "OBJ_ID": 7,
            "POINT": 4, "COMP": 1, "EQ": True,
            "bVALUE": True, "VALUE": 500, "OtherObject": 0
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/ULFC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 제약조건 조회 ─────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/ULFC", headers=HEADERS)
for key, val in resp.json().get("ULFC", {}).items():
    cond = "등호" if val.get("EQ") else "부등호"
    print(f"  [{key}] {val['NAME']} ({val['TYPE']}) {cond} 제약")
```

---

## 5. `/ope/GSBG` — Bridge Girder Diagram Image Export

> **기능:** [`/db/GSBG`](#1-dbgsbg--bridge-girder-diagrams)로 정의한 거더 다이어그램(응력 또는
> 부재력)을 지정 시공단계 구간에 대해 이미지 파일(bmp/jpg/emf)로 저장(export)합니다. `db/GSBG`가
> 다이어그램 그룹을 **정의**하는 엔드포인트라면, 이 엔드포인트는 그 결과를 **이미지로 뽑아내는**
> 별도의 OPE(Operation) 엔드포인트입니다.

### Input URI

```
{base url}/ope/GSBG
```

### Active Methods

`POST`

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 하중케이스/조합 이름 | `"LC_NAME"` | String | — | **Required** |
| 2 | 다이어그램 타입 · 응력: `0` / 부재력: `1` | `"DGRM_TYPE"` | Integer (enum) | — | **Required** |
| 3 | 일괄 처리 여부 (생략 시 `true`) | `"BATCH"` | Boolean | `true` | Optional |
| 4 | X축 타입 · 거리: `0` / 절점: `1` | `"X_AXIS_TYPE"` | Integer (enum) | `0` | Optional |
| **BATCH = true(생략 포함)** | | | | | |
| 5 | Export할 출력 그룹 이름 목록(문자열 배열) | `"BATCH_LIST"` | Array [String] | — | **Required** |
| **BATCH = false** | | | | | |
| 6 | 교량 거더 요소 그룹 | `"BRDG_GROUP"` | String | — | **Required** |
| 7 | 성분 · 응력(DGRM_TYPE=0): Sax `0` / +Sby `1` / −Sby `2` / +Sbz `3` / −Sbz `4` / Combined `5` / 7th DOF `6` · 부재력(DGRM_TYPE=1): Fx `0` / Fy `1` / Fz `2` / Mx `3` / My `4` / Mz `5` / Mb `6` / Mt `7` / Mw `8` | `"COMPONENTS"` | Integer (enum) | `0` | Optional |
| 8 | (응력·Combined일 때) 응력 표시 위치 · Maximum `0` / 1(−y,+z) `1` / 2(+y,+z) `2` / 3(+y,−z) `3` / 4(−y,−z) `4` | `"COMBINED_COMP"` | Integer (enum) | `0` | Optional |
| 9 | (응력·7th DOF일 때) 7th DOF 타입 · Sax(Warping) `0` / Ssy(Mt) `1` / Ssy(Mw) `2` / Ssz(Mt) `3` / Ssz(Mw) `4` / Combined(Ssy) `5` / Combined(Ssz) `6` | `"7TH_DOF_TYPE"` | Integer (enum) | `0` | Optional |
| **DGRM_TYPE = 0(응력)에서만** | | | | | |
| 10 | 허용응력선 표시 | `"STRESS_LINE"` | Object | — | Optional |
| (1) | 허용응력선 표시 여부 | `STRESS_LINE.OPT_USE` | Boolean | `false` | Optional |
| (2) | 압축 허용응력(OPT_USE=true 시) | `STRESS_LINE.COMP` | Integer | — | 조건부 **Required** |
| (3) | 인장 허용응력(OPT_USE=true 시) | `STRESS_LINE.TENS` | Integer | — | 조건부 **Required** |
| 11 | 다이어그램 생성 대상 시공단계 목록 | `"STAGE_LIST"` | Array [String] | — | **Required** |
| 12 | 생성 이미지 저장 경로 | `"EXPORT_PATH"` | String | — | **Required** |
| 13 | 저장 이미지 확장자 · `"bmp"` / `"jpg"` / `"emf"` | `"EXTENSION"` | String (enum) | — | **Required** |

> ⚠️ 원문 Specifications 표에는 응력 성분 `−Sbz`(4번)가 `"Sbz" 4`로 오타 표기되어 있다. JSON
> Schema의 설명("3: +Sbz, 4: -Sbz")을 근거로 위 표에서는 `−Sbz`로 정정했다.
> `BATCH=true`일 때는 `BRDG_GROUP`·`COMPONENTS`·`COMBINED_COMP`·`7TH_DOF_TYPE`을 최상위에 함께
> 보내면 안 되고, `BATCH=false`일 때는 반대로 `BATCH_LIST`를 보내면 안 된다(원문 JSON Schema
> `allOf`/`if-then` 제약).

### Request / Response JSON

**POST Request Body — 응력, Batch 방식**

```json
{
  "Argument": {
    "LC_NAME": "Dead Load",
    "DGRM_TYPE": 0,
    "BATCH": true,
    "X_AXIS_TYPE": 1,
    "STRESS_LINE": {"OPT_USE": true, "COMP": 210000, "TENS": 180000},
    "BATCH_LIST": ["Stress_Combined_Left", "Stress_7thDOF_Right", "Stress_Girder_Center"],
    "STAGE_LIST": ["CS1", "CS2"],
    "EXPORT_PATH": "C:\\Temp\\GSBG\\StressBatch",
    "EXTENSION": "jpg"
  }
}
```

**POST Request Body — 부재력, 단일 그룹 방식**

```json
{
  "Argument": {
    "LC_NAME": "Dead Load",
    "DGRM_TYPE": 1,
    "BATCH": false,
    "X_AXIS_TYPE": 0,
    "BRDG_GROUP": "BG_RIGHT",
    "COMPONENTS": 8,
    "STAGE_LIST": ["CS1", "CS2"],
    "EXPORT_PATH": "C:\\Temp\\GSBG\\ForceSingle",
    "EXTENSION": "jpg"
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

# ── POST: 응력 다이어그램 이미지 일괄 저장(BATCH) ──────────────────
payload = {
    "Argument": {
        "LC_NAME": "Dead Load",
        "DGRM_TYPE": 0,
        "BATCH": True,
        "X_AXIS_TYPE": 1,
        "STRESS_LINE": {"OPT_USE": True, "COMP": 210000, "TENS": 180000},
        "BATCH_LIST": ["Stress_Combined_Left", "Stress_7thDOF_Right", "Stress_Girder_Center"],
        "STAGE_LIST": ["CS1", "CS2"],
        "EXPORT_PATH": "C:\\Temp\\GSBG\\StressBatch",
        "EXTENSION": "jpg"
    }
}
resp = requests.post(f"{BASE_URL}/ope/GSBG", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## End-to-End Workflow

다음은 케이블 교량 시공단계 해석 후 교량 특화 결과(캠버·거더 다이어그램·미지하중계수)를 설정하는 워크플로우입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── STEP 1: 미지하중계수 제약조건 정의 (케이블 장력 최적화용) ──────
ulfc_payload = {
    "Assign": {
        "1": {
            "NAME": "Deck-Level", "TYPE": "DISP", "OBJ_ID": 106,
            "POINT": 0, "COMP": 2, "EQ": False,
            "bUB": True, "UB_VALUE": 0.01,
            "bLB": True, "LB_VALUE": -0.01
        }
    }
}
r1 = requests.post(f"{BASE_URL}/db/ULFC", json=ulfc_payload, headers=HEADERS)
print(f"STEP1 ULFC: {r1.status_code}")

# ── STEP 2: 일반 캠버 기준 설정 (시공단계 그룹별) ──────────────────
gcmb_payload = {
    "Assign": {
        "1": {
            "bSTART_PT_ZERO": True,
            "GCMB_BASE_ITEMS": [
                {"GRUP_NAME": f"CS_{i}", "DIRECTION": "+DX"} for i in range(10)
            ]
        }
    }
}
r2 = requests.post(f"{BASE_URL}/db/GCMB", json=gcmb_payload, headers=HEADERS)
print(f"STEP2 GCMB: {r2.status_code}")

# ── STEP 3: FCM 캠버 제어 설정 ─────────────────────────────────────
camb_payload = {
    "Assign": {
        "1": {
            "BODY_GROUP_NAME": "FSM",
            "SUPP_GROUP_NAME": "PSC-BN",
            "KEYSEG_GROUP_NAME": "Key-SegK1~K5"
        }
    }
}
r3 = requests.post(f"{BASE_URL}/db/CAMB", json=camb_payload, headers=HEADERS)
print(f"STEP3 CAMB: {r3.status_code}")

# ── STEP 4: 거더 다이어그램 설정 (부재력 My) ───────────────────────
gsbg_payload = {
    "Assign": {
        "1": {
            "NAME": "Girder_My", "BATCH": True, "BODY_ELEM_GRUP_K": 1,
            "ALLSTAGE": True, "DGRM_TYPE": 1, "MOMENT_COMP": 4, "SCALEFACTOR": 1
        }
    }
}
r4 = requests.post(f"{BASE_URL}/db/GSBG", json=gsbg_payload, headers=HEADERS)
print(f"STEP4 GSBG: {r4.status_code}")

# ── 전체 설정 확인 ─────────────────────────────────────────────────
print("\n=== 교량 특화 결과 설정 확인 ===")
for ep in ["ULFC", "GCMB", "CAMB", "GSBG"]:
    r = requests.get(f"{BASE_URL}/db/{ep}", headers=HEADERS)
    data = r.json().get(ep, {})
    print(f"  {ep}: {len(data)}개")
```
