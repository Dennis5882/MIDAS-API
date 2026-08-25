# 05 · DB – Boundary

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:** `https://moa-engineers.midasit.com:443/gen`  
> **인증:** 모든 요청에 `MAPI-Key: <your-key>` 헤더 필수  
> **출처:** [MIDAS API Online Manual – Boundary](https://support.midasuser.com/hc/en-us/articles/33016922742937)

---

## 목차

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | [`/db/CONS`](#1-dbcons--constraint-support) | Constraint Support (절점 지지조건) |
| 2 | [`/db/NSPR`](#2-dbnspr--point-spring) | Point Spring (점 스프링) |
| 3 | [`/db/GSTP`](#3-dbgstp--define-general-spring-type) | Define General Spring Type (일반 스프링 타입 정의) |
| 4 | [`/db/GSPR`](#4-dbgspr--assign-general-spring-supports) | Assign General Spring Supports (일반 스프링 지지 배정) |
| 5 | [`/db/SSPS`](#5-dbssps--surface-spring) | Surface Spring (면 스프링) |
| 6 | [`/db/ELNK`](#6-dbelnk--elastic-link) | Elastic Link |
| 7 | [`/db/RIGD`](#7-dbrigd--rigid-link) | Rigid Link |
| 8 | [`/db/NLLP`](#8-dbnllp--general-link-properties) | General Link Properties (일반 링크 속성 정의) |
| 9 | [`/db/NLNK`](#9-dbnlnk--general-link) | General Link (일반 링크 배정) |
| 10 | [`/db/NLNK-M1`](#10-dbnlnk-m1--general-link-hyper-s) | General Link – Hyper-S |
| 11 | [`/db/CGLP`](#11-dbcglp--change-general-link-property) | Change General Link Property |
| 12 | [`/db/FRLS`](#12-dbfrls--beam-end-release) | Beam End Release (보 단부 해제) |
| 13 | [`/db/OFFS`](#13-dboffs--beam-end-offsets) | Beam End Offsets (보 단부 오프셋) |
| 14 | [`/db/PRLS`](#14-dbprls--plate-end-release) | Plate End Release (판 단부 해제) |
| 15 | [`/db/MLFC`](#15-dbmlfc--force-deformation-function) | Force-Deformation Function (비선형 함수 정의) |
| 16 | [`/db/SDVI`](#16-dbsdvi--seismic-device--viscousoil-damper) | Seismic Device – Viscous/Oil Damper |
| 17 | [`/db/SDVE`](#17-dbsdve--seismic-device--viscoelastic-damper) | Seismic Device – Viscoelastic Damper |
| 18 | [`/db/SDST`](#18-dbsdst--seismic-device--steel-damper) | Seismic Device – Steel Damper |
| 19 | [`/db/SDHY`](#19-dbsdhy--seismic-device--hysteretic-isolator-mss) | Seismic Device – Hysteretic Isolator (MSS) |
| 20 | [`/db/SDIS`](#20-dbsdis--seismic-device--isolator-mss) | Seismic Device – Isolator (MSS) |
| 21 | [`/db/MCON`](#21-dbmcon--linear-constraints) | Linear Constraints (선형 구속조건) |
| 22 | [`/db/PZEF`](#22-dbpzef--panel-zone-effects) | Panel Zone Effects |
| 23 | [`/db/CLDR`](#23-dbcldr--define-constraints-label-direction) | Define Constraints Label Direction |
| 24 | [`/db/DRLS`](#24-dbdrls--diaphragm-disconnect) | Diaphragm Disconnect (다이어프램 해제) |

---

## 공통 Python 헬퍼

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "your-mapi-key-here"

def midas_api(method: str, endpoint: str, body=None):
    """MIDAS NX API 호출 헬퍼"""
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}
```

---

## 1. `/db/CONS` — Constraint Support

절점에 지지조건(고정·핀·롤러 등)을 배정합니다.  
`CONSTRAINT` 문자열 7자리는 `[DX, DY, DZ, RX, RY, RZ, RW]` 순서이며, `1`=구속, `0`=자유입니다.  
RW는 Warping Torsion 자유도입니다.

**Endpoint:** `{base url}/db/CONS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Constraint Supports (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Constraint `[DX,DY,DZ,RX,RY,RZ,RW]` · `1`=구속, `0`=자유 | `"CONSTRAINT"` | String(7) | — | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        { "ID": 1, "GROUP_NAME": "Support", "CONSTRAINT": "1111111" }
      ]
    },
    "2": {
      "ITEMS": [
        { "ID": 2, "GROUP_NAME": "Support", "CONSTRAINT": "1110000" }
      ]
    },
    "5": {
      "ITEMS": [
        { "ID": 5, "GROUP_NAME": "Support", "CONSTRAINT": "1111000" }
      ]
    }
  }
}
```

### Python 예제

```python
# --- CONS: 절점 지지조건 설정 ---
# CONSTRAINT 코드표
# "1111111" → 완전 고정 (Fixed)
# "1110000" → 핀 지지 (Pin: DX DY DZ 구속, 회전 자유)
# "1111000" → 일반 힌지 (DX DY DZ RX 구속)
# "1010000" → 롤러 (DY만 구속)

cons_data = {
    "Assign": {
        # 절점 1: 완전 고정
        "1": {"ITEMS": [{"ID": 1, "GROUP_NAME": "Foundation", "CONSTRAINT": "1111111"}]},
        # 절점 5: 핀 지지
        "5": {"ITEMS": [{"ID": 5, "GROUP_NAME": "Foundation", "CONSTRAINT": "1110000"}]},
        # 절점 10: Y방향 롤러
        "10": {"ITEMS": [{"ID": 10, "GROUP_NAME": "Foundation", "CONSTRAINT": "0110000"}]},
    }
}

# 지지조건 입력
result = midas_api("POST", "/db/CONS", cons_data)

# 전체 조회
all_cons = midas_api("GET", "/db/CONS")

# 특정 절점(ID=5) 수정
update_data = {
    "Assign": {
        "5": {"ITEMS": [{"ID": 5, "GROUP_NAME": "Foundation", "CONSTRAINT": "1111000"}]}
    }
}
midas_api("PUT", "/db/CONS", update_data)

# 특정 절점(ID=10) 지지 해제
midas_api("DELETE", "/db/CONS", {"Assign": {"10": {}}})
```

---

## 2. `/db/NSPR` — Point Spring

절점에 점 스프링을 배정합니다. Linear / Compression-Only / Tension-Only / Multi-Linear 네 가지 타입을 지원합니다.

**Endpoint:** `{base url}/db/NSPR`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

> ⚠️ **2026-08-25 재확인 전면 정정.** 이전 버전은 COMP/TENS/MULTI 세 타입을 하나로 묶어
> `DIR`(1~4)·`DV`·존재하지 않는 `"SK"` 필드로 잘못 기재하고 있었다(아티클 id
> `35945908301081`). 실제로는 **COMP/TENS는 `STIFF`(단일 강성값)**, **MULTI는
> `FUNCTION`(MLFC 함수 ID)**을 쓰며, `DIR`은 0~6(Vector 포함) enum이고 `DV`는 `DIR=6`
> (Vector)일 때만 쓰는 방향 벡터다. LINEAR 타입의 `Cr`(감쇠계수 배열)도 누락돼 있었다.

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Point Spring (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Spring Type · `"LINEAR"` / `"COMP"` / `"TENS"` / `"MULTI"` | `"TYPE"` | String | — | Required |
| (3) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Create Function Type · 0=점 스프링 함수, 1=면 스프링 함수 | `"FormType"` | Integer | 0 | Optional |

#### LINEAR 전용

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (5) | Spring Stiffness `[SDx, SDy, SDz, SRx, SRy, SRz]` | `"SDR"` | Array[Number,6] | — | Required |
| (6) | Fixed Option `[SDx, SDy, SDz, SRx, SRy, SRz]` | `"F_S"` | Array[Boolean,6] | false | Optional |
| (7) | Damping Constant 사용 여부 | `"DAMPING"` | Boolean | false | Optional |
| (8) | Damping `[Cx, Cy, Cz, CRx, CRy, CRz]` | `"Cr"` | Array[Number,6] | 0 | Optional |

#### COMP(Compression-Only) / TENS(Tension-Only) 전용

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (5) | Stiffness | `"STIFF"` | Number | — | Required |
| (6) | Direction · Dx(+):0 / Dx(–):1 / Dy(+):2 / Dy(–):3 / Dz(+):4 / Dz(–):5 / Vector:6 | `"DIR"` | Integer | — | Required |
| (7) | Normal Vector(`DIR`=6일 때) | `"DV"` | Array[Number,3] | 0 | Optional |

#### MULTI(Multi-Linear) 전용

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (5) | Force-Deformation 함수 ID(`/db/MLFC`에서 정의) | `"FUNCTION"` | Integer | — | Required |
| (6) | Direction · Dx(+):0 / Dx(–):1 / Dy(+):2 / Dy(–):3 / Dz(+):4 / Dz(–):5 / Vector:6 | `"DIR"` | Integer | — | Required |
| (7) | Normal Vector(`DIR`=6일 때) | `"DV"` | Array[Number,3] | 0 | Optional |

#### By Surface Spring Function 전용(`FormType`=1일 때 공통 추가)

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| (9) | Width of Frame | `"EFFAREA"` | Number | 0 | Optional |
| (10) | Modulus of Subgrade Reaction `[Kx, Ky, Kz]` | `"DK"` | Array[Number,3] | 0 | Optional |

### 요청 바디 예시

```json
{
  "Assign": {
    "2": {
      "ITEMS": [{
        "ID": 1, "TYPE": "LINEAR", "GROUP_NAME": "Service",
        "SDR": [33000, 34000, 35000, 33000000, 34000000, 35000000],
        "F_S": [false, false, false, false, false, false],
        "DAMPING": true,
        "Cr": [1, 2, 3, 4, 5, 6]
      }]
    },
    "4": {
      "ITEMS": [{
        "ID": 1, "TYPE": "COMP", "GROUP_NAME": "Service",
        "DIR": 4, "DV": [0, 0, 0], "STIFF": 1000000
      }]
    },
    "6": {
      "ITEMS": [{
        "ID": 1, "TYPE": "TENS", "GROUP_NAME": "Service",
        "DIR": 6, "DV": [0, -1, -1], "STIFF": 1000000
      }]
    },
    "8": {
      "ITEMS": [{
        "ID": 1, "TYPE": "MULTI", "GROUP_NAME": "Service",
        "DIR": 4, "DV": [0, 0, 0], "FUNCTION": 1
      }]
    }
  }
}
```

### Python 예제

```python
# --- NSPR: 점 스프링 배정 ---

# 절점 2: 선형 스프링 (수평 Kx=33000, Ky=34000, Kz=35000 kN/m)
nspr_linear = {
    "Assign": {
        "2": {
            "ITEMS": [{
                "ID": 2,
                "TYPE": "LINEAR",
                "GROUP_NAME": "Foundation_Spring",
                "SDR": [33000.0, 34000.0, 35000.0, 33000000.0, 34000000.0, 35000000.0],
                "F_S": [False, False, False, False, False, False]
            }]
        }
    }
}

# 절점 4: 압축 전용 스프링 — DIR=6(Vector), DV로 방향 지정 (토압 방향)
nspr_comp = {
    "Assign": {
        "4": {
            "ITEMS": [{
                "ID": 4,
                "TYPE": "COMP",
                "GROUP_NAME": "Soil_Spring",
                "DIR": 6,            # Vector 방식
                "DV": [0.0, -1.0, -1.0],
                "STIFF": 2000000.0
            }]
        }
    }
}

midas_api("POST", "/db/NSPR", nspr_linear)
midas_api("POST", "/db/NSPR", nspr_comp)

# 전체 조회
all_nspr = midas_api("GET", "/db/NSPR")
```

---

## 3. `/db/GSTP` — Define General Spring Type

전체 6×6 강성·질량·감쇠 행렬을 사용자 정의하는 일반 스프링 타입을 정의합니다.  
`SPRING`, `MASS`, `DAMPING` 배열은 **상삼각 행렬** 21개 항목으로 구성됩니다.

**Endpoint:** `{base url}/db/GSTP`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

> ⚠️ **2026-08-25 재확인 정정.** 21항 배열의 인덱스-행렬위치 매핑이 실제로는 "대각항 6개
> 먼저, 그다음 비대각항을 행 순서로" 배치되는 방식이다(아티클 id `35946004118169`, footnote
> ¹⁾). 이전 버전이 적어둔 표준 상삼각(K11,K12,K13,...,K22,K23,...) 순서와 다르므로, 그
> 순서대로 배열을 채우면 완전히 다른 스프링 위치에 값이 들어간다 — 실무에 영향이 큰
> 정정이라 아래 표·예제를 원문 그대로 교체했다.

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | General Spring Name | `"NAME"` | String | — | Required |
| 2 | Stiffness Matrix Option | `"OPT_STIFFNESS"` | Boolean | false | Optional |
| 3 | Stiffness Matrix (21항) ¹⁾ | `"SPRING"` | Array[Number,21] | 0 | Optional |
| 4 | Mass Matrix Option | `"OPT_MASS"` | Boolean | false | Optional |
| 5 | Mass Matrix (21항) ¹⁾ | `"MASS"` | Array[Number,21] | 0 | Optional |
| 6 | Damping Matrix Option | `"OPT_DAMPING"` | Boolean | false | Optional |
| 7 | Damping Matrix (21항) ¹⁾ | `"DAMPING"` | Array[Number,21] | 0 | Optional |

> **주의:** `SPRING`/`MASS`/`DAMPING` 배열은 옵션 플래그가 `true`일 때만 유효합니다.

#### ¹⁾ 21항 배열 인덱스 ↔ 행렬 위치(Row, Column) 매핑 (1-based)

| 인덱스(0-based) | 위치 | 인덱스 | 위치 | 인덱스 | 위치 |
| --- | --- | --- | --- | --- | --- |
| 0 | (1,1) | 7 | (1,3) | 14 | (2,6) |
| 1 | (2,2) | 8 | (1,4) | 15 | (3,4) |
| 2 | (3,3) | 9 | (1,5) | 16 | (3,5) |
| 3 | (4,4) | 10 | (1,6) | 17 | (3,6) |
| 4 | (5,5) | 11 | (2,3) | 18 | (4,5) |
| 5 | (6,6) | 12 | (2,4) | 19 | (4,6) |
| 6 | (1,2) | 13 | (2,5) | 20 | (5,6) |

대각항(1,1)~(6,6) 6개가 먼저 오고, 그 뒤로 (1,2)부터 행 순서대로 비대각항이 이어진다.

### 요청 바디 예시

```json
{
  "Assign": {
    "3": {
      "NAME": "GS_Damping",
      "SPRING": [1, 7, 12, 16, 19, 21, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 17, 18, 20],
      "MASS": [1, 7, 12, 16, 19, 21, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 17, 18, 20]
    }
  }
}
```

> 위 예제는 원문 그대로 값 자체가 배열 내 위치를 나타내는 자리표시자(placeholder)이며,
> `OPT_STIFFNESS`/`OPT_MASS`/`OPT_DAMPING` 옵션 플래그는 원문 예제에 없다 — 실제 사용 시
> 사용할 행렬에 해당하는 옵션을 `true`로 함께 보내야 한다.

### Python 예제

```python
# --- GSTP: 일반 스프링 타입 정의 ---
# 21항 순서(0-based): 0~5=대각항(1,1)~(6,6), 6~10=(1,2)~(1,6),
#                      11~14=(2,3)~(2,6), 15~17=(3,4)~(3,6),
#                      18~19=(4,5)~(4,6), 20=(5,6)

gstp_data = {
    "Assign": {
        "1": {
            "NAME": "Foundation_GS",
            "OPT_STIFFNESS": True,
            # 대각항만 값(비대각항 전부 0): idx0~5 = Kxx,Kyy,Kzz,Krxrx,Kryry,Krzrz
            "SPRING": [
                1000, 800, 800, 0, 0, 0,   # 대각항: Kx=1000, Ky=800, Kz=800, 회전 0
                0, 0, 0, 0, 0,              # (1,2)~(1,6)
                0, 0, 0, 0,                 # (2,3)~(2,6)
                0, 0, 0,                    # (3,4)~(3,6)
                0, 0,                       # (4,5)~(4,6)
                0                           # (5,6)
            ]
        }
    }
}

midas_api("POST", "/db/GSTP", gstp_data)
```

---

## 4. `/db/GSPR` — Assign General Spring Supports

GSTP에서 정의한 일반 스프링 타입을 절점에 배정합니다.

**Endpoint:** `{base url}/db/GSPR`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | General Spring (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Defined General Spring Name (GSTP에서 정의한 이름) | `"TYPE_NAME"` | String | — | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "14": {
      "ITEMS": [
        { "ID": 14, "GROUP_NAME": "Service", "TYPE_NAME": "Foundation_GS" }
      ]
    }
  }
}
```

### Python 예제

```python
# --- GSPR: 일반 스프링 지지 배정 ---
# 사전조건: GSTP에 "Foundation_GS" 타입이 정의되어 있어야 함

gspr_data = {
    "Assign": {
        "10": {"ITEMS": [{"ID": 10, "GROUP_NAME": "Pile_Cap", "TYPE_NAME": "Foundation_GS"}]},
        "11": {"ITEMS": [{"ID": 11, "GROUP_NAME": "Pile_Cap", "TYPE_NAME": "Foundation_GS"}]},
        "12": {"ITEMS": [{"ID": 12, "GROUP_NAME": "Pile_Cap", "TYPE_NAME": "Foundation_GS"}]},
    }
}

midas_api("POST", "/db/GSPR", gspr_data)
```

---

## 5. `/db/SSPS` — Surface Spring

요소(프레임·판·솔리드)의 면 또는 모서리에 지반반력계수 기반의 스프링을 배정합니다.

**Endpoint:** `{base url}/db/SSPS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Surface Spring (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Element Type · `"FRAME"` / `"PLANAR(FACE)"` / `"PLANAR(EDGE)"` / `"SOLID"` | `"ELEM_TYPE"` | String | — | Required |
| (4) | Edge/Face 선택 · FRAME: Local x=2, y=0, z=1 · PLANAR/SOLID: Edge#1∼4=0∼3 | `"EDGE_FACE"` | Integer | 0 | Optional |
| (5) | Spring Type · 0=Linear, 1=Comp.-Only, 2=Tens.-Only | `"SPRING_TYPE"` | Integer | 0 | Optional |
| (6) | Modulus of Subgrade Reaction Ks | `"MODULUS"` | Number | — | Required |
| (7) | Width(FRAME 전용) | `"WIDTH"` | Number | — | Required(FRAME) |

### 요청 바디 예시 (FRAME / PLANAR / SOLID)

```json
{
  "Assign": {
    "1": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Soil", "ELEM_TYPE": "FRAME",
        "EDGE_FACE": 1, "WIDTH": 1.2, "SPRING_TYPE": 0, "MODULUS": 500
      }]
    },
    "21": {
      "ITEMS": [{
        "ID": 21, "GROUP_NAME": "Soil", "ELEM_TYPE": "PLANAR(FACE)",
        "SPRING_TYPE": 0, "MODULUS": 500
      }]
    },
    "41": {
      "ITEMS": [{
        "ID": 41, "GROUP_NAME": "Soil", "ELEM_TYPE": "SOLID",
        "EDGE_FACE": 4, "SPRING_TYPE": 0, "MODULUS": 500
      }]
    }
  }
}
```

### Python 예제

```python
# --- SSPS: 면 스프링 배정 ---
# 판요소(PLANAR) 지반스프링 - 지하외벽/기초 슬래브 모델링에 활용

ssps_data = {
    "Assign": {
        # 판요소 ID 5: 기초 슬래브 면에 선형 지반 반력 스프링 Ks=30000 kN/m³
        "5": {
            "ITEMS": [{
                "ID": 5,
                "GROUP_NAME": "Foundation_Slab",
                "ELEM_TYPE": "PLANAR(FACE)",
                "SPRING_TYPE": 0,   # 0 = Linear
                "MODULUS": 30000.0  # Ks (kN/m³)
            }]
        },
        # 프레임요소 ID 3: 말뚝 측면에 압축 전용 수평 스프링
        "3": {
            "ITEMS": [{
                "ID": 3,
                "GROUP_NAME": "Pile_Side",
                "ELEM_TYPE": "FRAME",
                "EDGE_FACE": 0,     # Local y 방향
                "WIDTH": 1.0,
                "SPRING_TYPE": 1,   # 1 = Compression-Only
                "MODULUS": 10000.0  # Ks (kN/m³)
            }]
        }
    }
}

midas_api("POST", "/db/SSPS", ssps_data)
```

---

## 6. `/db/ELNK` — Elastic Link

두 절점 사이에 탄성 링크를 배정합니다. 링크 타입은 `LINK` 키로 구분하며 7가지를 지원합니다.

**Endpoint:** `{base url}/db/ELNK`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 공통 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Node Numbers `[i-node, j-node]` | `"NODE"` | Array[Integer,2] | — | Required |
| 2 | Boundary Group Name | `"BNGR_NAME"` | String | Blank | Optional |
| 3 | Beta Angle (°) | `"ANGLE"` | Number | 0 | Optional |
| 4 | Link Type | `"LINK"` | String | — | Required |

### LINK 타입별 추가 파라미터

> ⚠️ 원문 Specifications 표는 `"LINK"` 값을 `"MULTI LINEAR"`·`"RAIL INTERACT"`(공백 포함)로
> 적고 있으나, JSON Schema·Request Example은 모두 공백 없는 `"MULTILINEAR"`·`"RAILINTERACT"`를
> 쓴다(예제가 표보다 우선). 아래는 정상 표기이니 되돌리지 말 것(아티클 id `35946439146649`,
> 2026-08-25 확인 — 오류제보 대상).

| LINK 값 | 설명 | 추가 키 |
|---------|------|---------|
| `"GEN"` | General (6자유도 스프링) | `SDR[6]`, `R_S[6]`, `bSHEAR`, `DR[2]` |
| `"RIGID"` | 강체 링크 | (없음) |
| `"SADDLE"` | 안장 (교량 받침 특화) | (없음) |
| `"TENS"` | Tension-Only | `SDR[6]` (Dx만 유효) |
| `"COMP"` | Compression-Only | `SDR[6]` (Dx만 유효) |
| `"MULTILINEAR"` | Multi-Linear | `DIR`(0=Dx/1=Dy/2=Dz/3=Rx/4=Ry/5=Rz), `MLFC`(함수 ID), `bSHEAR`, `DRENDI` |
| `"RAILINTERACT"` | Rail Track Interaction | `DIR`(**1=Dy/2=Dz만 유효** — Multi-Linear와 enum 범위가 다름), `RLFC`(함수 ID), `bSHEAR`, `DRENDI` |

`SDR` / `R_S` 배열 순서: `[SDx, SDy, SDz, SRx, SRy, SRz]`  
`DIR` 값: 0=Dx, 1=Dy, 2=Dz, 3=Rx, 4=Ry, 5=Rz

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "NODE": [1, 2], "LINK": "GEN", "ANGLE": 0,
      "SDR": [1000, 500, 500, 0, 0, 0],
      "R_S": [false, false, false, false, false, false],
      "bSHEAR": false, "DR": [0, 0]
    },
    "3": { "NODE": [3, 4], "LINK": "RIGID", "ANGLE": 0, "BNGR_NAME": "Service" },
    "5": { "NODE": [5, 6], "LINK": "COMP", "ANGLE": 0, "SDR": [1100, 0, 0, 0, 0, 0] },
    "6": {
      "NODE": [6, 7], "LINK": "MULTILINEAR", "ANGLE": 0,
      "BNGR_NAME": "Service", "DIR": 1, "MLFC": 1, "DRENDI": 0.5
    }
  }
}
```

### Python 예제

```python
# --- ELNK: 탄성 링크 배정 ---

elnk_data = {
    "Assign": {
        # GEN 타입: 6 자유도 독립 스프링
        "1": {
            "NODE": [1, 2],
            "LINK": "GEN",
            "ANGLE": 0.0,
            "SDR": [5000.0, 3000.0, 3000.0, 0.0, 0.0, 0.0],  # kN/m
            "R_S": [False, False, False, False, False, False],
            "bSHEAR": False,
            "DR": [0.0, 0.0]
        },
        # RIGID 타입: 강체 링크
        "2": {
            "NODE": [3, 4],
            "LINK": "RIGID",
            "ANGLE": 0.0,
            "BNGR_NAME": "Seismic_Links"
        },
        # TENS 타입: 인장 전용
        "3": {
            "NODE": [5, 6],
            "LINK": "TENS",
            "ANGLE": 0.0,
            "SDR": [2000.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        },
        # MULTILINEAR 타입: 비선형 함수 참조 (MLFC ID=1 필요)
        "4": {
            "NODE": [7, 8],
            "LINK": "MULTILINEAR",
            "ANGLE": 0.0,
            "BNGR_NAME": "Nonlinear_Links",
            "DIR": 1,       # Dy 방향
            "MLFC": 1,      # Force-Deformation 함수 ID
            "DRENDI": 0.5   # 전단 스프링 위치 비율
        }
    }
}

midas_api("POST", "/db/ELNK", elnk_data)
```

---

## 7. `/db/RIGD` — Rigid Link

마스터 절점과 다수의 슬레이브 절점 사이에 강체 링크를 배정합니다.  
`DOF` 정수의 각 자릿수는 `1`=강체, `0`=자유이며 자릿수 순서는 DX↔6th, DY↔5th, DZ↔4th, RX↔3rd, RY↔2nd, RZ↔1st입니다.

**Endpoint:** `{base url}/db/RIGD`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Rigid Link (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number (마스터 절점 ID) | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Degree of Freedom (정수: 각 자리가 DX∼RZ) | `"DOF"` | Integer | — | Required |
| (4) | Slave Node ID Numbers | `"S_NODE"` | Array[Integer] | — | Required |

**DOF 예시:**  
`110001` → DX(=1), DY(=1), DZ(=0), RX(=0), RY(=0), RZ(=1) 구속

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Diaphragm",
        "DOF": 110001,
        "S_NODE": [2, 3, 4, 5, 6, 7, 8]
      }]
    }
  }
}
```

### Python 예제

```python
# --- RIGD: 강체 링크 (층 다이어프램 모델링에 사용) ---

rigd_data = {
    "Assign": {
        # 마스터 절점 1: DX, DY, RZ 구속 (평면 다이어프램)
        # DOF = 110001 → 6th(DX)=1, 5th(DY)=1, 4th(DZ)=0, 3rd(RX)=0, 2nd(RY)=0, 1st(RZ)=1
        "1": {
            "ITEMS": [{
                "ID": 1,
                "GROUP_NAME": "Floor_Diaphragm",
                "DOF": 110001,
                "S_NODE": [2, 3, 4, 5, 6, 7, 8, 9, 10]
            }]
        }
    }
}

midas_api("POST", "/db/RIGD", rigd_data)
```

---

## 8. `/db/NLLP` — General Link Properties

일반 링크(General Link)에 사용할 비선형 속성을 정의합니다. `APPLICATION_TYPE` + `APPLICATION_TYPE_D` 조합으로 장치 유형을 지정합니다.

**Endpoint:** `{base url}/db/NLLP`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### APPLICATION_TYPE 조합표

| APPLICATION_TYPE | APPLICATION_TYPE_D | 설명 |
|------------------|--------------------|------|
| `"ELEMENT"` | `"SPG"` | Spring (스프링) |
| `"ELEMENT"` | `"DSP"` | Linear Dashpot |
| `"ELEMENT"` | `"SLD"` | Spring & Linear Dashpot |
| `"ELEMENT2"` | `"VI"` | Viscous/Oil Damper → 내부 SDVI 참조 |
| `"ELEMENT2"` | `"VE"` | Viscoelastic Damper → 내부 SDVE 참조 |
| `"ELEMENT2"` | `"ST"` | Steel Damper → 내부 SDST 참조 |
| `"ELEMENT2"` | `"HY"` | Hysteretic Isolator → 내부 SDHY 참조 |
| `"ELEMENT2"` | `"IS"` | Isolator (MSS) → 내부 SDIS 참조 |
| `"FORCE"` | `"VD"` | Force-Type Viscoelastic Damper |
| `"FORCE"` | `"GAP"` | Gap |
| `"FORCE"` | `"HOOK"` | Hook |
| `"FORCE"` | `"HS"` | Hysteretic System |
| `"FORCE"` | `"LRBI"` | Lead Rubber Bearing Isolator |
| `"FORCE"` | `"FPSI"` | Friction Pendulum System Isolator |
| `"FORCE"` | `"TFPSI"` | Triple Friction Pendulum System Isolator |

### 요청 파라미터 (공통)

> ⚠️ **2026-08-25 재확인 보강:** 공통 필드 뒤에 `DIST_RATIO_DY`/`DIST_RATIO_DZ`/
> `COUPLED_INPUT_METHOD` 3개가 누락돼 있었다(아티클 id `35946764618905`). 이 원문은
> `APPLICATION_TYPE`/`APPLICATION_TYPE_D` 조합 14가지마다 별도 파라미터 세트(장치별
> 상세 물성)를 갖는 6000줄 이상의 방대한 문서라, 위 "APPLICATION_TYPE 조합표"에 정리한
> 개요 수준으로만 다루고 조합별 상세 필드는(SDVI/SDVE/SDST/SDHY/SDIS로 참조되는 것
> 외의 FORCE 계열 GAP/HOOK/HS/LRBI/FPSI/TFPSI 등) 전수 기재하지 않는다(SECT/TDMT/FIMP와
> 동일 원칙).

| No. | 설명 | 키 | 타입 | 필수 |
|-----|------|----|------|------|
| 1 | General Link Property Name | `"PROPERTY_NAME"` | String | Required |
| 2 | Description | `"DESC"` | String | Optional |
| 3 | Application Type | `"APPLICATION_TYPE"` | String | Required |
| 4 | Property/Devices Type | `"APPLICATION_TYPE_D"` | String | Required |
| 5 | Self-Weight (Total) | `"TOTAL_WEIGHT"` | Number | Optional |
| 6 | Lumped Weight Ratio | `"L_WEIGHT_RATIO"` | Number | Optional |
| 7 | Use Mass Option | `"OPT_USE_MASS"` | Boolean | Optional |
| 8 | Mass (Total) | `"TOTAL_MASS"` | Number | Optional |
| 9 | Lumped Mass Ratio | `"L_MASS_RATIO"` | Number | Optional |
| 10 | Shear Spring Location Option | `"OPT_SHEAR_SPR_LOC"` | Boolean | Optional |
| 11 | Distance Ratio from End I (Dy) | `"DIST_RATIO_DY"` | Number | Optional |
| 12 | Distance Ratio from End I (Dz) | `"DIST_RATIO_DZ"` | Number | Optional |
| 13 | Coupled Input Method | `"COUPLED_INPUT_METHOD"` | Integer | Optional |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "PROPERTY_NAME": "GL_Spring01", "APPLICATION_TYPE": "ELEMENT",
      "APPLICATION_TYPE_D": "SPG", "DESC": "Foundation Spring",
      "TOTAL_WEIGHT": 0, "OPT_USE_MASS": false
    },
    "11": {
      "PROPERTY_NAME": "GL_ViscousDamper01", "APPLICATION_TYPE": "ELEMENT2",
      "APPLICATION_TYPE_D": "VI", "DESC": "Seismic Viscous Damper"
    }
  }
}
```

### Python 예제

```python
# --- NLLP: 일반 링크 속성 정의 ---

nllp_data = {
    "Assign": {
        # 스프링 타입 일반 링크
        "1": {
            "PROPERTY_NAME": "GL_Isolator_Spring",
            "DESC": "Base Isolation Spring",
            "APPLICATION_TYPE": "ELEMENT",
            "APPLICATION_TYPE_D": "SPG",
            "TOTAL_WEIGHT": 0.0,
            "OPT_USE_MASS": False
        },
        # 지진격리장치 (납고무받침 - ELEMENT2 + IS)
        # 실제 장치 데이터는 SDIS에서 별도 정의
        "2": {
            "PROPERTY_NAME": "GL_LRB_01",
            "DESC": "Lead Rubber Bearing",
            "APPLICATION_TYPE": "ELEMENT2",
            "APPLICATION_TYPE_D": "IS"
        }
    }
}

midas_api("POST", "/db/NLLP", nllp_data)
```

---

## 9. `/db/NLNK` — General Link

NLLP에서 정의한 일반 링크 속성을 두 절점 사이에 배정합니다. 좌표계(요소계/전역계)에 따른 방향 지정 방법이 세 가지입니다.

**Endpoint:** `{base url}/db/NLNK`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Node 1 ID | `"NODE1"` | Integer | — | Required |
| 2 | Node 2 ID | `"NODE2"` | Integer | — | Required |
| 3 | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| 4 | General Link Property Name | `"PROP_NAME"` | String | — | Required |
| 5 | Inelastic Hinge Property Name | `"IEHP_NAME"` | String | Blank | Optional |
| 6 | Reference Coordinate System · 0=Element, 1=Global | `"REF_SYSTEM"` | Integer | — | Required |
| — | **REF_SYSTEM=0 (요소계)** | | | | |
| 7 | Beta Angle (°) | `"BETA_ANGLE"` | Number | 0 | Optional |
| — | **REF_SYSTEM=1 (전역계) – Angle 방식** | | | | |
| 7 | Input Method · 0=Angle | `"INPUT_METHOD"` | Integer | — | Required |
| 8 | Angle Values `[about X, about y', about z'']` | `"ANGLE_VALUES"` | Array[Object] | — | Required |
| — | **REF_SYSTEM=1 (전역계) – 3Points 방식** | | | | |
| 7 | Input Method · 1=3 Points | `"INPUT_METHOD"` | Integer | — | Required |
| 8 | Point Values `[P0[3], P1[3], P2[3]]` | `"POINT_VALUES"` | Array[Object,3] | — | Required |
| — | **REF_SYSTEM=1 (전역계) – Vector 방식** | | | | |
| 7 | Input Method · 2=Vector | `"INPUT_METHOD"` | Integer | — | Required |
| 8 | Vector Points `[V1[3], V2[3]]` | `"VECTOR_VALUES"` | Array[Object,2] | — | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "NODE1": 10, "NODE2": 11,
      "PROP_NAME": "GL_LRB_01", "REF_SYSTEM": 0, "BETA_ANGLE": 0,
      "GROUP_NAME": "Isolation_Layer"
    },
    "2": {
      "NODE1": 11, "NODE2": 12, "PROP_NAME": "GL_LRB_01",
      "REF_SYSTEM": 1, "INPUT_METHOD": 0,
      "ANGLE_VALUES": [{ "VALUE": [0, 0, 30] }]
    }
  }
}
```

### Python 예제

```python
# --- NLNK: 일반 링크 배정 ---
# 사전조건: NLLP에 "GL_LRB_01" 속성이 정의되어 있어야 함

nlnk_data = {
    "Assign": {
        # 요소 좌표계 기준, 베타각 0도
        "1": {
            "NODE1": 10, "NODE2": 11,
            "PROP_NAME": "GL_LRB_01",
            "IEHP_NAME": "",
            "REF_SYSTEM": 0,
            "BETA_ANGLE": 0.0,
            "GROUP_NAME": "Isolation_Level_1"
        },
        # 전역 좌표계 기준, 각도 방법
        "2": {
            "NODE1": 12, "NODE2": 13,
            "PROP_NAME": "GL_LRB_01",
            "REF_SYSTEM": 1,
            "INPUT_METHOD": 0,
            "ANGLE_VALUES": [{"VALUE": [0.0, 0.0, 0.0]}],
            "GROUP_NAME": "Isolation_Level_1"
        }
    }
}

midas_api("POST", "/db/NLNK", nlnk_data)
```

---

## 10. `/db/NLNK-M1` — General Link (Hyper-S)

Hyper-S 솔버 전용 일반 링크 배정 엔드포인트입니다.

> ⚠️ **2026-08-25 재확인 전면 보강.** 이전 버전은 "공식 사이트에 JSON 스키마 예제가 없다"고
> 적고 3개 필드짜리 스텁으로 남겨져 있었으나, 실제로는 아티클 id `56511465190937`(928줄)에
> 온전한 스펙이 있다 — 이번 정기점검 재대조로 발견. 구조는 9번 절 `/db/NLNK`와 거의 동일
> (좌표계·입력방식 분기까지 동일)하며, `IEHP_NAME`(비선형 힌지 속성)만 빠져 있다.

**Endpoint:** `{base url}/db/NLNK-M1`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | General Link Property Name | `"PROP_NAME"` | String | — | Required |
| 2 | Node 1 ID | `"NODE1"` | Integer | — | Required |
| 3 | Node 2 ID | `"NODE2"` | Integer | — | Required |
| 4 | Reference Coordinate System · 0=Element, 1=Global | `"REF_SYSTEM"` | Integer | — | Required |
| 5 (REF_SYSTEM=0) | Beta Angle | `"BETA_ANGLE"` | Number | 0 | Required |
| 6 (REF_SYSTEM=1) | Input Method · 0=Angle, 1=3 Points, 2=Vector | `"INPUT_METHOD"` | Integer | — | Required |
| 7 (INPUT_METHOD=0) | Angle Values `[about X, about y', about z'']` | `"ANGLE_VALUES"` | Array[Object] | — | Required |
| 8 (INPUT_METHOD=1) | Point Values `[P0[3], P1[3], P2[3]]` | `"POINT_VALUES"` | Array[Object] | — | Required |
| 9 (INPUT_METHOD=2) | Vector Values `[V1[3], V2[3]]` | `"VECTOR_VALUES"` | Array[Object] | — | Required |
| 10 | Boundary Group Name | `"GROUP_NAME"` | String | — | Optional |

각 `ANGLE_VALUES`/`POINT_VALUES`/`VECTOR_VALUES` 배열 원소는 `{"VALUE": [x, y, z]}` 형태의
object다(NLNK와 동일).

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "PROP_NAME": "NLL_PROP_1",
      "NODE1": 101,
      "NODE2": 102,
      "REF_SYSTEM": 0,
      "BETA_ANGLE": 0,
      "GROUP_NAME": "Boundary Group 1"
    },
    "2": {
      "PROP_NAME": "NLL_PROP_1",
      "NODE1": 101,
      "NODE2": 102,
      "REF_SYSTEM": 1,
      "INPUT_METHOD": 0,
      "ANGLE_VALUES": [{ "VALUE": [0, 0, 0] }],
      "GROUP_NAME": "Boundary Group 1"
    }
  }
}
```

### Python 예제

```python
# --- NLNK-M1: Hyper-S 전용 일반 링크 배정 ---
# Hyper-S 솔버 사용 시에만 유효, 구조는 /db/NLNK와 동일(IEHP_NAME 제외)

nlnk_m1_data = {
    "Assign": {
        "1": {
            "PROP_NAME": "GL_HyperS_Prop",
            "NODE1": 20,
            "NODE2": 21,
            "REF_SYSTEM": 0,
            "BETA_ANGLE": 0,
            "GROUP_NAME": "Isolation_Level_1"
        }
    }
}

midas_api("POST", "/db/NLNK-M1", nlnk_m1_data)
```

---

## 11. `/db/CGLP` — Change General Link Property

특정 일반 링크 요소의 속성을 다른 NLLP 속성으로 변경합니다.

**Endpoint:** `{base url}/db/CGLP`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | General Link ID Number | `"GLINK_KEY"` | Integer | — | Required |
| 2 | Change Property Name (NLLP에서 정의된 이름) | `"CHANGE_PROPERTY_NAME"` | String | — | Required |
| 3 | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": { "GLINK_KEY": 1, "CHANGE_PROPERTY_NAME": "GL_LRB_02", "GROUP_NAME": "Stage2" },
    "2": { "GLINK_KEY": 2, "CHANGE_PROPERTY_NAME": "GL_LRB_02", "GROUP_NAME": "Stage2" }
  }
}
```

### Python 예제

```python
# --- CGLP: 일반 링크 속성 변경 (시공단계별 속성 교체에 사용) ---

cglp_data = {
    "Assign": {
        # 일반 링크 요소 1, 2의 속성을 "GL_LRB_02"로 교체
        "1": {"GLINK_KEY": 1, "CHANGE_PROPERTY_NAME": "GL_LRB_02", "GROUP_NAME": "PostTension"},
        "2": {"GLINK_KEY": 2, "CHANGE_PROPERTY_NAME": "GL_LRB_02", "GROUP_NAME": "PostTension"},
    }
}

midas_api("POST", "/db/CGLP", cglp_data)
```

---

## 12. `/db/FRLS` — Beam End Release

보 요소의 단부 자유도를 해제합니다. `FLAG_I`/`FLAG_J`는 7자리 문자열 `[Fx, Fy, Fz, Mx, My, Mz, Mb]`이며, `1`=해제, `0`=연결입니다.  
`bVALUE=true`이면 부분 고정도(Partial Fixity) 값을 `VALUE_I`/`VALUE_J`에 입력합니다.

**Endpoint:** `{base url}/db/FRLS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Beam End Release (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Input Method · false=Relative, true=Value | `"bVALUE"` | Boolean | false | Optional |
| (4) | Release i-Node `[Fx,Fy,Fz,Mx,My,Mz,Mb]` | `"FLAG_I"` | String(7) | — | Required |
| (5) | Partial Fixity for i-Node `[Fx,Fy,Fz,Mx,My,Mz,Mb]` | `"VALUE_I"` | Array[Number,7] | 0 | Optional |
| (6) | Release j-Node `[Fx,Fy,Fz,Mx,My,Mz,Mb]` | `"FLAG_J"` | String(7) | — | Required |
| (7) | Partial Fixity for j-Node `[Fx,Fy,Fz,Mx,My,Mz,Mb]` | `"VALUE_J"` | Array[Number,7] | 0 | Optional |

### 요청 바디 예시

```json
{
  "Assign": {
    "9": {
      "ITEMS": [{
        "ID": 9, "GROUP_NAME": "Service", "bVALUE": false,
        "FLAG_I": "0000100", "VALUE_I": [0, 0, 0, 0, 0, 0, 0],
        "FLAG_J": "0000100", "VALUE_J": [0, 0, 0, 0, 0, 0, 0]
      }]
    }
  }
}
```

### Python 예제

```python
# --- FRLS: 보 단부 모멘트 해제 (핀 접합 모델링) ---
# FLAG 코드: "0000110" → My, Mz 해제 (핀 접합)
# FLAG 코드: "0000010" → Mz만 해제 (2D 핀)
# FLAG 코드: "0001110" → Mx, My, Mz 해제 (완전 힌지)

frls_data = {
    "Assign": {
        # 보 요소 9: 양단 My 해제 (단순보 수직 면내 핀 접합)
        "9": {
            "ITEMS": [{
                "ID": 9,
                "GROUP_NAME": "Pin_Beam",
                "bVALUE": False,
                "FLAG_I": "0000100",   # My 해제
                "VALUE_I": [0, 0, 0, 0, 0, 0, 0],
                "FLAG_J": "0000100",   # My 해제
                "VALUE_J": [0, 0, 0, 0, 0, 0, 0]
            }]
        },
        # 보 요소 12: i단 완전 핀, j단 모멘트 연속
        "12": {
            "ITEMS": [{
                "ID": 12,
                "GROUP_NAME": "Pin_Beam",
                "bVALUE": False,
                "FLAG_I": "0001110",   # Mx, My, Mz 해제
                "VALUE_I": [0, 0, 0, 0, 0, 0, 0],
                "FLAG_J": "0000000",   # 완전 연속
                "VALUE_J": [0, 0, 0, 0, 0, 0, 0]
            }]
        }
    }
}

midas_api("POST", "/db/FRLS", frls_data)
```

---

## 13. `/db/OFFS` — Beam End Offsets

보 요소 단부에 편심(오프셋)을 적용합니다. 전역 좌표계(GLOBAL) 또는 요소 좌표계(ELEMENT) 기준으로 입력합니다.

**Endpoint:** `{base url}/db/OFFS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Beam End Offsets (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Reference CS · `"GLOBAL"` / `"ELEMENT"` | `"TYPE"` | String | — | Required |
| — | **GLOBAL 전용** | | | | |
| (4) | i-단 X방향 오프셋 (GCS) | `"RGDXi"` | Number | 0 | Optional |
| (5) | i-단 Y방향 오프셋 (GCS) | `"RGDYi"` | Number | 0 | Optional |
| (6) | i-단 Z방향 오프셋 (GCS) | `"RGDZi"` | Number | 0 | Optional |
| (7) | j-단 X방향 오프셋 (GCS) | `"RGDXj"` | Number | 0 | Optional |
| (8) | j-단 Y방향 오프셋 (GCS) | `"RGDYj"` | Number | 0 | Optional |
| (9) | j-단 Z방향 오프셋 (GCS) | `"RGDZj"` | Number | 0 | Optional |
| — | **ELEMENT 전용** | | | | |
| (4) | i-단 y방향 오프셋 (ECS) | `"RGDYi"` | Number | 0 | Optional |
| (5) | i-단 z방향 오프셋 (ECS) | `"RGDZi"` | Number | 0 | Optional |
| (6) | j-단 y방향 오프셋 (ECS) | `"RGDYj"` | Number | 0 | Optional |
| (7) | j-단 z방향 오프셋 (ECS) | `"RGDZj"` | Number | 0 | Optional |

### 요청 바디 예시

```json
{
  "Assign": {
    "8": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service", "TYPE": "GLOBAL",
        "RGDXi": 0.11, "RGDYi": 0.12, "RGDZi": 0.13,
        "RGDXj": 0.21, "RGDYj": 0.22, "RGDZj": 0.23
      }]
    },
    "7": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service", "TYPE": "ELEMENT",
        "RGDYi": 0.11, "RGDZi": 0.12, "RGDYj": 0.21, "RGDZj": 0.22
      }]
    }
  }
}
```

### Python 예제

```python
# --- OFFS: 보 단부 오프셋 (슬래브·거더 편심 모델링) ---

offs_data = {
    "Assign": {
        # 요소 5: 슬래브와 거더의 중립축 차이 반영 (요소 좌표계)
        # z방향 오프셋 0.15m (슬래브 상단 - 거더 중립축 거리)
        "5": {
            "ITEMS": [{
                "ID": 5,
                "GROUP_NAME": "Slab_Offset",
                "TYPE": "ELEMENT",
                "RGDYi": 0.0,
                "RGDZi": 0.15,  # m 단위, 슬래브-거더 편심
                "RGDYj": 0.0,
                "RGDZj": 0.15
            }]
        }
    }
}

midas_api("POST", "/db/OFFS", offs_data)
```

---

## 14. `/db/PRLS` — Plate End Release

판 요소 각 절점 위치의 자유도를 해제합니다. N1∼N4는 판의 각 꼭짓점 절점이며, 배열 값 `1`=해제, `0`=연결입니다.  
배열 순서: `[Fx, Fy, Fz, Mx, My]`

**Endpoint:** `{base url}/db/PRLS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Plate End Release (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Position N1 `[Fx,Fy,Fz,Mx,My]` · 1=해제 | `"N1"` | Array[Integer,5] | — | Required |
| (4) | Position N2 `[Fx,Fy,Fz,Mx,My]` | `"N2"` | Array[Integer,5] | — | Required |
| (5) | Position N3 `[Fx,Fy,Fz,Mx,My]` | `"N3"` | Array[Integer,5] | — | Required |
| (6) | Position N4 `[Fx,Fy,Fz,Mx,My]` | `"N4"` | Array[Integer,5] | — | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "21": {
      "ITEMS": [{
        "ID": 21, "GROUP_NAME": "Service",
        "N1": [1, 0, 1, 0, 1],
        "N2": [1, 0, 1, 0, 1],
        "N3": [1, 0, 1, 0, 1],
        "N4": [1, 0, 1, 0, 1]
      }]
    }
  }
}
```

### Python 예제

```python
# --- PRLS: 판 단부 해제 ---
# N1~N4: 판 요소의 4개 절점 순서대로 해제 조건 지정
# [Fx, Fy, Fz, Mx, My] = 1이면 해제

prls_data = {
    "Assign": {
        "21": {
            "ITEMS": [{
                "ID": 21,
                "GROUP_NAME": "Slab_Release",
                "N1": [0, 0, 0, 0, 0],  # 완전 연속
                "N2": [0, 0, 0, 0, 0],
                "N3": [0, 0, 0, 0, 1],  # My 해제
                "N4": [0, 0, 0, 0, 1]   # My 해제
            }]
        }
    }
}

midas_api("POST", "/db/PRLS", prls_data)
```

---

## 15. `/db/MLFC` — Force-Deformation Function

Elastic Link (MULTILINEAR) 또는 General Link (FORCE 타입)에서 참조하는 비선형 힘-변위 함수를 정의합니다.

**Endpoint:** `{base url}/db/MLFC`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Function Name | `"NAME"` | String | — | Required |
| 2 | Type · `"FORCE"` (힘-변위) / `"MOMENT"` (모멘트-회전각) | `"TYPE"` | String | `"MOMENT"` | Optional |
| 3 | Symmetric · true=대칭, false=비대칭 | `"SYMM"` | Boolean | false | Optional |
| 4 | Function ID | `"FUNC_ID"` | Integer | 0 | Optional |
| 5 | Function Data (X=변위/회전, Y=힘/모멘트) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | X-Axis (Displacement m / Radian) | `"X"` | Number | — | Required |
| (2) | Y-Axis (Force kN / Moment kN·m) | `"Y"` | Number | — | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "NAME": "Force_Deform_Isolator",
      "TYPE": "FORCE", "SYMM": false, "FUNC_ID": 0,
      "ITEMS": [
        { "X": -0.20, "Y": -1200 },
        { "X": -0.05, "Y": -500 },
        { "X":  0.00, "Y":    0 },
        { "X":  0.05, "Y":  500 },
        { "X":  0.20, "Y": 1200 }
      ]
    },
    "2": {
      "NAME": "Moment_Radian_Hinge",
      "TYPE": "MOMENT", "SYMM": true, "FUNC_ID": 0,
      "ITEMS": [
        { "X": 0.00, "Y":    0 },
        { "X": 0.01, "Y":  500 },
        { "X": 0.03, "Y":  800 },
        { "X": 0.10, "Y":  900 }
      ]
    }
  }
}
```

### Python 예제

```python
# --- MLFC: 힘-변위 함수 정의 ---
# ELNK MULTILINEAR 타입 또는 NLLP FORCE 타입에서 MLFC ID를 참조

mlfc_data = {
    "Assign": {
        "1": {
            "NAME": "Bilinear_Isolator_FD",
            "TYPE": "FORCE",
            "SYMM": False,          # 비대칭 (인장/압축 다른 경우)
            "FUNC_ID": 0,
            "ITEMS": [
                {"X": -0.200, "Y": -1200.0},   # 최대 압축
                {"X": -0.050, "Y":  -300.0},   # 항복 전
                {"X":  0.000, "Y":     0.0},   # 원점
                {"X":  0.050, "Y":   300.0},   # 항복 후
                {"X":  0.200, "Y":  1200.0}    # 최대 인장
            ]
        }
    }
}

midas_api("POST", "/db/MLFC", mlfc_data)
```

---

## 16. `/db/SDVI` — Seismic Device – Viscous/Oil Damper

내진용 점성 댐퍼(Viscous Damper) 또는 오일 댐퍼(Oil Damper)의 물성을 정의합니다.  
NLLP의 `APPLICATION_TYPE_D="VI"`에서 참조됩니다.

**Endpoint:** `{base url}/db/SDVI`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 필수 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| (1) | Name | `"NAME"` | String | Required |
| (2) | Description | `"DESC"` | String | Optional |
| (3) | Input Method · 0=사용자 입력, 1=참조 DB | `"INPUT_METHOD"` | Integer | Required |
| (4) | Company | `"COMPANY"` | String | Required |
| (5) | Product Name | `"PRODUCT_NAME"` | String | Required |
| (6) | Type Number | `"TYPE_NUMBER"` | String | Required |
| 2 | Device Type | `"DEVICE_TYPE"` | String | Optional |
| 3 | Damper Model · 0=Single Dashpot, 1=Kelvin(Voigt), 2=Maxwell | `"DAMPER_TYPE"` | Integer | Required |
| 4 | Dashpot Type · 0=Linear Elastic, 1=Bilinear, 2=Exponential | `"DASHPOT_TYPE"` | Integer | Required |
| 5 | Input Type · 0=감쇠비 α₁, 1=감쇠상수 C₁ | `"INPUT_TYPE"` | Integer | Required |
| 6 | Input Type (Exponential Function Type용) | `"INPUT_TYPE_EXFN"` | Integer | Required |
| 7 | Property Data (DOF별 6항목) | `"ITEM"` | Array[Object,6] | Required |
| (1) | DOF 활성화 여부 | `"OPT_DOF"` | Boolean | Required |
| (2) | 초기 감쇠계수 CE | `"CE"` | Number | Required |
| (3) | 최대 감쇠력 P₁ | `"P1"` | Number | Required |
| (4) | 이차 감쇠계수 C₁ | `"C1"` | Number | Required |
| (5) | 감쇠 감소 계수 α₁ | `"ALPHA1"` | Number | Required |
| (6) | 초기 강성 K₀ | `"K0"` | Number | Required |
| (7) | 감쇠력(Exponential, Damping Force) | `"EXFN_PY"` | Number | Required |
| (8) | 기준 속도(Exponential, Reference Velocity) | `"EXFN_VY"` | Number | Required |
| (9) | 감쇠 지수(Exponential, Damping Exponent) | `"EXFN_DE"` | Number | Required |
| (10) | 감쇠계수(Exponential, Damping Coefficient) | `"EXFN_DC"` | Number | Required |
| (11) | Exponential 초기 감쇠계수 사용 여부 | `"OPT_EXFN_CE"` | Boolean | Required |
| (12) | Exponential 초기 감쇠계수 값 | `"EXFN_CE"` | Number | Required |

> ⚠️ **2026-08-25 재확인 보강:** `INPUT_TYPE_EXFN`(최상위)과 `ITEM[]`의 (7)~(12) 6개
> Exponential Function Type(`DASHPOT_TYPE=2`) 전용 필드가 누락돼 있었다. 원문 Request
> Example을 보면 `DASHPOT_TYPE` 값과 무관하게 `ITEM[]` 각 원소가 항상 12개 필드를 모두
> 포함해 전송한다(아티클 id `35947995586713`).

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "ViscousDamper_D01", "DESC": "",
        "INPUT_METHOD": 0, "COMPANY": "", "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 0,
      "DASHPOT_TYPE": 0,
      "INPUT_TYPE": 0,
      "INPUT_TYPE_EXFN": 0,
      "ITEM": [
        { "OPT_DOF": true, "CE": 13000, "P1": 0, "C1": 0, "ALPHA1": 0, "K0": 0,
          "EXFN_PY": 1, "EXFN_VY": 1, "EXFN_DE": 0.3, "EXFN_DC": 1,
          "OPT_EXFN_CE": false, "EXFN_CE": 1 },
        { "OPT_DOF": false, "CE": 0, "P1": 0, "C1": 0, "ALPHA1": 0, "K0": 0,
          "EXFN_PY": 1, "EXFN_VY": 1, "EXFN_DE": 0.3, "EXFN_DC": 1,
          "OPT_EXFN_CE": false, "EXFN_CE": 1 }
      ]
    }
  }
}
```

### Python 예제

```python
# --- SDVI: 점성 댐퍼 물성 정의 ---
# ITEM 배열 순서: Dx, Dy, Dz, Rx, Ry, Rz
# DASHPOT_TYPE 값과 무관하게 ITEM 각 원소는 12개 필드를 모두 전송해야 함

def make_dof_item(active, CE=0, P1=0, C1=0, alpha1=1.0, K0=0,
                   exfn_py=1, exfn_vy=1, exfn_de=0.3, exfn_dc=1,
                   opt_exfn_ce=False, exfn_ce=1):
    return {
        "OPT_DOF": active, "CE": CE, "P1": P1, "C1": C1, "ALPHA1": alpha1, "K0": K0,
        "EXFN_PY": exfn_py, "EXFN_VY": exfn_vy, "EXFN_DE": exfn_de, "EXFN_DC": exfn_dc,
        "OPT_EXFN_CE": opt_exfn_ce, "EXFN_CE": exfn_ce
    }

sdvi_data = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "OilDamper_500kN",
                "DESC": "Seismic Oil Damper 500kN",
                "INPUT_METHOD": 0,
                "COMPANY": "SUMITOMO",
                "PRODUCT_NAME": "OD-500",
                "TYPE_NUMBER": "OD500-A"
            },
            "DEVICE_TYPE": "",
            "DAMPER_TYPE": 2,       # Maxwell 모델
            "DASHPOT_TYPE": 2,      # 지수함수 타입
            "INPUT_TYPE": 0,        # 감쇠비 α₁ 입력
            "INPUT_TYPE_EXFN": 0,
            "ITEM": [
                make_dof_item(True,  CE=500, P1=1000, C1=200, alpha1=0.5),  # Dx 활성
                make_dof_item(False),   # Dy 비활성
                make_dof_item(False),   # Dz
                make_dof_item(False),   # Rx
                make_dof_item(False),   # Ry
                make_dof_item(False),   # Rz
            ]
        }
    }
}

midas_api("POST", "/db/SDVI", sdvi_data)
```

---

## 17. `/db/SDVE` — Seismic Device – Viscoelastic Damper

점탄성 댐퍼(Viscoelastic Damper) 물성을 정의합니다.  
NLLP의 `APPLICATION_TYPE_D="VE"`에서 참조됩니다.

**Endpoint:** `{base url}/db/SDVE`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

> ⚠️ **2026-08-25 재확인 전면 보강.** 이전 버전은 `COMMON`/`MATERIAL_TYPE`/`SHEAR_AREA` 3개
> 필드만 있었으나, 원문(아티클 id `35948062417049`)의 실제 Request Example은 이 아래 14개
> 필드를 추가로 전송한다 — 표만 보고는 알 수 없고 Request Example로만 확인 가능했다.

| No. | 설명 | 키 | 타입 | 필수 |
|-----|------|----|------|------|
| 1 | Common Data (SDVI와 동일 구조) | `"COMMON"` | Object | Required |
| 2 | Material Type · `"GR100"` / `"GR300"` / `"SR05"` / `"GR400"` / `"CST"` / `"TRC"` | `"MATERIAL_TYPE"` | String | Required |
| 3 | Shear Area | `"SHEAR_AREA"` | Number | Required |
| 4 | Thickness | `"THICKNESS"` | Number | Required |
| 5 | Multiplier | `"MULTIPL"` | Number | Required |
| 6 | Direction(`"Dx"`/`"Dy"`/`"Dz"` 등) | `"DIR"` | String | Required |
| 7 | Frequency | `"FREQ"` | Number | Required |
| 8 | Stiffness Factor | `"STIFF_FACTOR"` | Number | Required |
| 9 | Damping Factor | `"DAMP_FACTOR"` | Number | Required |
| 10 | Reference Temperature | `"REF_T"` | Number | Required |
| 11 | Limit Deformation | `"LIMIT_DEF"` | Number | Required |
| 12 | Effective Stiffness | `"EFF_STIFF"` | Number | Required |
| 13 | Equivalent Damping | `"EQUI_DAMP"` | Number | Required |
| 14 | Use Mount Stiffness | `"OPT_MOUNT_STIFF"` | Boolean | Required |
| 15 | Mount Stiffness | `"MOUNT_STIFF"` | Number | Required |
| 16 | Use Kinetic Friction | `"OPT_KINETIC_FRIC"` | Boolean | Required |
| 17 | Kinetic Friction | `"KINETIC_FRIC"` | Number | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "Viscoelastic01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "MATERIAL_TYPE": "GR100",
      "SHEAR_AREA": 0.2,
      "THICKNESS": 0.02,
      "MULTIPL": 1,
      "DIR": "Dx",
      "FREQ": 0,
      "STIFF_FACTOR": 1,
      "DAMP_FACTOR": 1,
      "REF_T": 20,
      "LIMIT_DEF": 0.3,
      "EFF_STIFF": 0,
      "EQUI_DAMP": 0,
      "OPT_MOUNT_STIFF": true,
      "MOUNT_STIFF": 1200,
      "OPT_KINETIC_FRIC": false,
      "KINETIC_FRIC": 0
    }
  }
}
```

### Python 예제

```python
# --- SDVE: 점탄성 댐퍼 물성 정의 ---

sdve_data = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "VE_Damper_GR100",
                "DESC": "Viscoelastic Damper - SUMITOMO GR100",
                "INPUT_METHOD": 0,
                "PRODUCT_NAME": "GR100-Series",
                "TYPE_NUMBER": "GR100-200"
            },
            "MATERIAL_TYPE": "GR100",   # SUMITOMO GR100 재료
            "SHEAR_AREA": 0.2,          # 전단 면적 (m²)
            "THICKNESS": 0.02,          # 두께 (m)
            "MULTIPL": 1,               # 배수(적층 개수 등)
            "DIR": "Dx",
            "FREQ": 0,
            "STIFF_FACTOR": 1,
            "DAMP_FACTOR": 1,
            "REF_T": 20,                # 기준 온도 (°C)
            "LIMIT_DEF": 0.3,           # 한계 변형
            "EFF_STIFF": 0,
            "EQUI_DAMP": 0,
            "OPT_MOUNT_STIFF": True,
            "MOUNT_STIFF": 1200,
            "OPT_KINETIC_FRIC": False,
            "KINETIC_FRIC": 0
        }
    }
}

midas_api("POST", "/db/SDVE", sdve_data)
```

---

## 18. `/db/SDST` — Seismic Device – Steel Damper

강재 댐퍼(Steel Damper) 물성을 정의합니다.  
NLLP의 `APPLICATION_TYPE_D="ST"`에서 참조됩니다.

**Endpoint:** `{base url}/db/SDST`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

> ⚠️ **2026-08-25 재확인 전면 정정.** 원문 Specifications 표는 이 엔드포인트에 `MATERIAL_TYPE`
> (SUMITOMO GR100 등)·`MULTIPL` 필드가 있는 것으로 적어놓았으나, 이는 **17번 절 SDVE(점탄성
> 댐퍼) 페이지 내용이 잘못 섞여 들어간 것**으로 판단된다 — JSON Schema와 실제 Request
> Example 어디에도 `MATERIAL_TYPE`은 없다. 대신 실제로는 `K0`/`P1`/`ALPHA1`/`KB`와 이력모델별
> 하위 객체(`BL2`/`LY2`/`LY3`/`IK2`)가 쓰인다(아티클 id `35948150053529`, 오류제보 대상).

| No. | 설명 | 키 | 타입 | 필수 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| 2 | Direction | `"DIR"` | String | Required |
| 3 | Hysteresis Model · Degrading Bilinear: `"BL2"` / Low Yielding Steel(LY2): `"LY2"` / Low Yielding Steel(LY3): `"LY3"` / Isotropic-Kinematic(IK2): `"IK2"` | `"SDST_HYS_MODEL"` | String | Required |
| 4 | Initial Stiffness (K0) | `"K0"` | Number | Required |
| 5 | Yield Strength (P1) | `"P1"` | Number | Required |
| 6 | Stiffness Factor (α1) | `"ALPHA1"` | Number | Required |
| 7 | Mounting Parts Stiffness (Kb) | `"KB"` | Number | Required |

#### `SDST_HYS_MODEL` 별 하위 객체

| Model | Key | 하위 필드 |
| --- | --- | --- |
| `"BL2"` | `"BL2"` | `BETA`(Exponent in Unloading Stiffness Calculation) |
| `"LY2"` | `"LY2"` | `ALPHA2`(Stiffness Factor), `THETA`(Strength Factor) |
| `"LY3"` | `"LY3"` | `ALPHA2`, `THETA`, `GAMMA`(Stiffness Ratio) |
| `"IK2"` | `"IK2"` | `GAMMA`(Isotropic Factor) |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "SteelDamper01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "DIR": "Dx",
      "SDST_HYS_MODEL": "BL2",
      "K0": 1000,
      "P1": 100,
      "ALPHA1": 0.2,
      "KB": 2000,
      "BL2": { "BETA": 0 }
    }
  }
}
```

### Python 예제

```python
# --- SDST: 강재 댐퍼 물성 정의 ---

sdst_data = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "SteelDamper_Dx_300kN",
                "DESC": "Steel Damper 300kN Bilinear",
                "INPUT_METHOD": 0,
                "PRODUCT_NAME": "SD-300",
                "TYPE_NUMBER": "SD300-B"
            },
            "DIR": "Dx",
            "SDST_HYS_MODEL": "BL2",     # Degrading Bilinear 이력 모델
            "K0": 1000,                  # 초기 강성
            "P1": 100,                   # 항복강도
            "ALPHA1": 0.2,               # 강성 계수
            "KB": 2000,                  # 부착부 강성
            "BL2": {"BETA": 0}           # BL2 모델 전용 파라미터
        }
    }
}

midas_api("POST", "/db/SDST", sdst_data)
```

---

## 19. `/db/SDHY` — Seismic Device – Hysteretic Isolator (MSS)

이력형 지진격리장치(다중 전단 스프링 모델, MSS)의 물성을 정의합니다.  
NLLP의 `APPLICATION_TYPE_D="HY"`에서 참조됩니다.

**Endpoint:** `{base url}/db/SDHY`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

> ⚠️ **2026-08-25 재확인 보강.** `P1`/`P2`/`ALPHA1`/`ALPHA2`/`BETA`/`Phi`/`LAMBDA` 7개
> 필드가 누락돼 있었다(아티클 id `35948292269977`). 원문 표에는 `MULTIPL`(Multiplier)도
> 있으나 JSON Schema·Request Example 어디에도 나타나지 않아(SDST/SDVE 표에서 반복적으로
> 발견된 것과 같은 원문 오류로 판단) 표에 넣지 않았다.

| No. | 설명 | 키 | 타입 | 필수 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| 2 | Hysteresis Model · `"DegradingBiLinear"` 등 | `"SDHY_HYS_MODEL"` | String | Required |
| 3 | Number of Shear Springs (MSS 전단 스프링 수) | `"MSS"` | Integer | Required |
| 4 | K0 Initial Stiffness | `"K0"` | Number | Required |
| 5 | P1 Yield Strength | `"P1"` | Number | Required |
| 6 | P2 Yield Strength | `"P2"` | Number | Required |
| 7 | Alpha1 Stiffness Factor | `"ALPHA1"` | Number | Required |
| 8 | Alpha2 Stiffness Factor | `"ALPHA2"` | Number | Required |
| 9 | Beta(Exponent in Unloading Stiffness Calculation) | `"BETA"` | Number | Required |
| 10 | Phi | `"Phi"` | Number | Required |
| 11 | Lambda | `"LAMBDA"` | Number | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "HystereticIsolator01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "SDHY_HYS_MODEL": "DegradingBiLinear",
      "MSS": 8,
      "K0": 1000,
      "P1": 100,
      "P2": 0,
      "ALPHA1": 1,
      "ALPHA2": 0,
      "BETA": 0.5,
      "Phi": 0,
      "LAMBDA": 8
    }
  }
}
```

### Python 예제

```python
# --- SDHY: 이력형 격리장치 물성 정의 ---

sdhy_data = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "HI_DegBilinear_500",
                "DESC": "Hysteretic Isolator - Degrading Bilinear",
                "INPUT_METHOD": 0,
                "PRODUCT_NAME": "HI-500",
                "TYPE_NUMBER": "HI500-A"
            },
            "SDHY_HYS_MODEL": "DegradingBiLinear",
            "MSS": 8,           # 전단 스프링 분할 수
            "K0": 5000.0,       # 초기 강성 (kN/m)
            "P1": 100.0,        # 1차 항복강도
            "P2": 0.0,          # 2차 항복강도
            "ALPHA1": 1.0,
            "ALPHA2": 0.0,
            "BETA": 0.5,
            "Phi": 0.0,
            "LAMBDA": 8.0
        }
    }
}

midas_api("POST", "/db/SDHY", sdhy_data)
```

---

## 20. `/db/SDIS` — Seismic Device – Isolator (MSS)

MSS 기반 지진격리장치(납고무 LRB / 천연고무 NRB / 미끄럼 SB)의 물성을 정의합니다.  
NLLP의 `APPLICATION_TYPE_D="IS"`에서 참조됩니다.

**Endpoint:** `{base url}/db/SDIS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

> ⚠️ **2026-08-25 재확인 전면 정정.** 이전 버전은 (1) `SDIS_DEV_TYPE` 세 번째 값을 `"SB"`로
> 잘못 기재(실제로는 **`"SLD"`**, 데이터 객체 키만 `"SB"`), (2) LRB의 `DX`/`OPT_CONS_NONL`/
> `BETA`/`ALPHA`/`SIGMA_V`를 서로 같은 레벨의 형제 필드로 잘못 기재(실제로는 **`DX`가
> `{OPT_CONS_NONL, BETA, ALPHA, SIGMA_V}`를 담는 하위 객체**), (3) LRB의 `KE`·`K0`(이름이
> 비슷하지만 별개인 두 초기강성 필드) 중 `K0`을 누락, (4) NRB Data가 `KH` 하나뿐인 것으로
> 잘못 기재(실제로는 `AR`/`TR`/`KH`/`DX{...}` 4+4개), (5) SB Data의 `QD`(Index)·`Pi_VALUE`를
> 누락한 채 작성돼 있었다. 원문 JSON Schema + Request Example 대조로 전면 재작성했다
> (아티클 id `35948330042649`, 오류제보 대상).

| No. | 설명 | 키 | 타입 | 필수 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| 2 | Device Type · `"LRB"` / `"NRB"` / `"SLD"`(데이터는 `"SB"` 객체에 담김) | `"SDIS_DEV_TYPE"` | String | Required |
| 3 | Number of Shear Springs | `"MSS"` | Integer | Required |
| 4 | Adjustment Parameter τk | `"TAU_K"` | Number | Required |
| 5 | Adjustment Parameter τq | `"TAU_Q"` | Number | Required |
| 6 | Vertical Stiffness Kv | `"KV"` | Number | Required |
| 7 | LRB Data (SDIS_DEV_TYPE="LRB"일 때) | `"LRB"` | Object | Required |
| 8 | NRB Data (SDIS_DEV_TYPE="NRB"일 때) | `"NRB"` | Object | Required |
| 9 | SB Data (SDIS_DEV_TYPE="SLD"일 때) | `"SB"` | Object | Required |

**`LRB` 객체**

| No. | 설명 | 키 | 타입 | 필수 |
| --- | --- | --- | --- | --- |
| (1) | Hysteresis Model | `"SDIS_HYS_MODEL"` | String | Required |
| (2) | Initial Stiffness Ke | `"KE"` | Number | Required |
| (3) | Rubber Cross Section Area AR | `"AR"` | Number | Required |
| (4) | Total Thickness of Rubber TR | `"TR"` | Number | Required |
| (5) | Initial Stiffness K0(KE와 별개 필드) | `"K0"` | Number | Required |
| (6) | 2nd Stiffness K2 | `"K2"` | Number | Required |
| (7) | Characteristic Strength QD | `"QD"` | Number | Required |
| (8) | Vertical Direction Properties | `"DX"` | Object | Optional |
| (8)-i | Use Consider Vertical Direction Nonlinearity(`DX` 하위) | `"OPT_CONS_NONL"` | Boolean | Optional |
| (8)-ii | Tensile Stiffness Reduction Factor β(`DX` 하위) | `"BETA"` | Number | Optional |
| (8)-iii | Tensile Stiffness Reduction Ratio α(`DX` 하위) | `"ALPHA"` | Number | Optional |
| (8)-iv | Tensile Limit Strength(`DX` 하위) | `"SIGMA_V"` | Number | Optional |

**`NRB` 객체**

| No. | 설명 | 키 | 타입 | 필수 |
| --- | --- | --- | --- | --- |
| (1) | Rubber Cross Section Area AR | `"AR"` | Number | Required |
| (2) | Total Thickness of Rubber TR | `"TR"` | Number | Required |
| (3) | Horizontal Stiffness KH | `"KH"` | Number | Required |
| (4) | Vertical Direction Properties(`DX`, LRB와 동일 구조) | `"DX"` | Object | Optional |

**`SB` 객체**(SDIS_DEV_TYPE=`"SLD"`)

| No. | 설명 | 키 | 타입 | 필수 |
| --- | --- | --- | --- | --- |
| (1) | Area of Sliding Head AS | `"AS"` | Number | Required |
| (2) | Initial Stiffness K0 | `"K0"` | Number | Required |
| (3) | Index Qd | `"QD"` | Integer | Required |
| (4) | Pi | `"Pi_VALUE"` | Number | Required |
| (5) | Frictional Factor μ0 | `"MU0"` | Number | Required |

### 요청 바디 예시 (LRB / NRB / SLD)

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "LRB_Isolator_01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "LRB-500", "TYPE_NUMBER": "LRB500-A"
      },
      "SDIS_DEV_TYPE": "LRB", "MSS": 8,
      "TAU_K": 1.0, "TAU_Q": 1.0, "KV": 150000,
      "LRB": {
        "SDIS_HYS_MODEL": "BiLinear",
        "KE": 20000, "AR": 0.196, "TR": 0.15, "K0": 20000, "K2": 2000, "QD": 80,
        "DX": { "OPT_CONS_NONL": false, "BETA": 0.1, "ALPHA": 0.5, "SIGMA_V": 3000 }
      }
    },
    "3": {
      "COMMON": {
        "NAME": "NRB_Isolator_01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "SDIS_DEV_TYPE": "NRB", "MSS": 8,
      "TAU_K": 1.0, "KV": 150000,
      "NRB": { "AR": 0.196, "TR": 0.15, "KH": 1200 }
    },
    "4": {
      "COMMON": {
        "NAME": "SlidingBearing_01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "SDIS_DEV_TYPE": "SLD", "MSS": 8,
      "TAU_K": 1.0, "TAU_Q": 1.0, "KV": 150000,
      "SB": { "AS": 0.05, "K0": 100000, "QD": 2, "Pi_VALUE": 0, "MU0": 0.05 }
    }
  }
}
```

### Python 예제

```python
# --- SDIS: 지진격리장치 물성 정의 (LRB) ---
# LRB: Lead Rubber Bearing (납고무 받침)
# 납고무 받침은 비선형 시간이력 해석에서 필수적인 격리장치

sdis_lrb_data = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "LRB_500kN",
                "DESC": "Lead Rubber Bearing 500kN",
                "INPUT_METHOD": 0,
                "PRODUCT_NAME": "LRB-500",
                "TYPE_NUMBER": "LRB500-Standard"
            },
            "SDIS_DEV_TYPE": "LRB",
            "MSS": 8,               # 전단 스프링 분할 수
            "TAU_K": 1.0,           # 강성 보정 계수
            "TAU_Q": 1.0,           # 항복력 보정 계수
            "KV": 150000.0,         # 수직 강성 (kN/m)
            "LRB": {
                "SDIS_HYS_MODEL": "BiLinear",   # 이력 모델
                "KE": 20000.0,  # 초기 강성 Ke (kN/m)
                "AR": 0.196,    # 고무 단면적 (m²)
                "TR": 0.150,    # 고무 총 두께 (m)
                "K0": 20000.0,  # 초기 강성 K0 (KE와 별개 필드, kN/m)
                "K2": 2000.0,   # 이차 강성 (kN/m)
                "QD": 80.0,     # 특성강도 (kN)
                "DX": {                  # 수직 방향 특성(선택)
                    "OPT_CONS_NONL": False,
                    "BETA": 0.1,
                    "ALPHA": 0.5,
                    "SIGMA_V": 3000.0    # 인장 강도 한계 (kN/m²)
                }
            }
        }
    }
}

midas_api("POST", "/db/SDIS", sdis_lrb_data)
```

---

## 21. `/db/MCON` — Linear Constraints

절점 간 선형 종속 구속조건(등변위, 가중 변위 등)을 설정합니다.  
`SLAVE_TYPE` 6자리는 `[DX,DY,DZ,RX,RY,RZ]` 순서, `1`=구속 활성.

**Endpoint:** `{base url}/db/MCON`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

> ⚠️ **2026-08-25 재확인 정정.** `SLAVES[]`의 필드가 `TYPE`에 따라 다르다 — 이전 버전은 두
> 타입 모두 `COEFF`를 쓰는 것으로 잘못 기재했으나, 실제로는 **`"EX"`만 `COEFF`+`DOF`
> 조합**을 쓰고(원소마다 개별 DOF 지정), **`"WD"`는 `WEIGHT"` 하나만** 쓴다(아티클 id
> `35948507217689`).

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Linear Constraints (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | DOF of Constraint Node (6자리: DX∼RZ) | `"SLAVE_TYPE"` | String(6) | — | Required |
| (4) | Constraint Type · `"EX"`=Explicit, `"WD"`=Weighted Displacement | `"TYPE"` | String | — | Required |
| (5) | Independent Nodes | `"SLAVES"` | Array[Object] | — | Required |

**`TYPE="EX"`(Explicit)일 때 `SLAVES[]`**

| No. | 설명 | 키 | 타입 | 필수 |
| --- | --- | --- | --- | --- |
| i | Node ID | `"NODE_KEY"` | Integer | Required |
| ii | Coefficient | `"COEFF"` | Number | Required |
| iii | Degree of Freedom · DX:0/DY:1/DZ:2/RX:3/RY:4/RZ:5 | `"DOF"` | Integer | Required |

**`TYPE="WD"`(Weighted Displacement)일 때 `SLAVES[]`**

| No. | 설명 | 키 | 타입 | 필수 |
| --- | --- | --- | --- | --- |
| i | Node ID | `"NODE_KEY"` | Integer | Required |
| ii | Weight | `"WEIGHT"` | Number | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "21": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service", "SLAVE_TYPE": "100000",
        "TYPE": "EX",
        "SLAVES": [
          { "NODE_KEY": 22, "COEFF": 0.5, "DOF": 0 },
          { "NODE_KEY": 23, "COEFF": 0.5, "DOF": 1 }
        ]
      }]
    }
  }
}
```

### Python 예제

```python
# --- MCON: 선형 구속조건 (층 다이어프램 구속 대안) ---
# EX 타입: NODE_KEY+COEFF+DOF 조합으로 등변위/가중 구속 (DOF는 원소별 개별 지정)
# WD 타입: NODE_KEY+WEIGHT만 사용 (경사 지붕, 비정형 구조 등)

mcon_data = {
    "Assign": {
        # 절점 5, 10의 DX 변위를 동일하게 구속
        "1": {
            "ITEMS": [{
                "ID": 1,
                "GROUP_NAME": "Diaphragm_Constraint",
                "SLAVE_TYPE": "100000",   # DX만 활성
                "TYPE": "EX",
                "SLAVES": [
                    {"NODE_KEY": 5,  "COEFF":  1.0, "DOF": 0},
                    {"NODE_KEY": 10, "COEFF": -1.0, "DOF": 0}
                ]
            }]
        },
        # 가중 변위 구속 (WD): D_node5 = 0.5 * D_node10 + 0.5 * D_node15
        "2": {
            "ITEMS": [{
                "ID": 2,
                "GROUP_NAME": "Weighted_Constraint",
                "SLAVE_TYPE": "110001",   # DX, DY, RZ
                "TYPE": "WD",
                "SLAVES": [
                    {"NODE_KEY": 10, "WEIGHT": 0.5},
                    {"NODE_KEY": 15, "WEIGHT": 0.5}
                ]
            }]
        }
    }
}

midas_api("POST", "/db/MCON", mcon_data)
```

---

## 22. `/db/PZEF` — Panel Zone Effects

보-기둥 접합부의 패널 존(Panel Zone) 변형 효과를 설정합니다.

**Endpoint:** `{base url}/db/PZEF`  
**Methods:** `POST` · `GET` · `PUT`  
*(DELETE 미지원)*

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Auto Calculate Panel Zone Offset Distances | `"OPT_OFFSET"` | Boolean | — | Required |
| 2 | Offset Factor | `"OFFS_FACTOR"` | Number | — | Required |
| 3 | Output Position | `"OUTPUT_POSITION"` | Integer | — | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "OPT_OFFSET": true,
      "OFFS_FACTOR": 1.0,
      "OUTPUT_POSITION": 1
    }
  }
}
```

### Python 예제

```python
# --- PZEF: 패널 존 효과 설정 ---
# 보-기둥 접합부에서 강체 오프셋 자동 계산 사용

pzef_data = {
    "Assign": {
        "1": {
            "OPT_OFFSET": True,     # 자동 계산 사용
            "OFFS_FACTOR": 1.0,     # 오프셋 계수 (1.0 = 전체 적용)
            "OUTPUT_POSITION": 1    # 결과 출력 위치
        }
    }
}

# 패널 존 효과 설정 (프로젝트 전역 설정)
midas_api("POST", "/db/PZEF", pzef_data)

# 현재 설정 조회
current_pzef = midas_api("GET", "/db/PZEF")

# 설정 수정
pzef_data["Assign"]["1"]["OFFS_FACTOR"] = 0.8
midas_api("PUT", "/db/PZEF", pzef_data)
```

---

## 23. `/db/CLDR` — Define Constraints Label Direction

구속조건 레이블의 표시 방향을 절점별로 지정합니다.

**Endpoint:** `{base url}/db/CLDR`  
**Methods:** `POST` · `GET` · `PUT`  
*(DELETE 미지원)*

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Constraint Label Direction | `"DIR"` | Integer | — | Required |

**DIR 값:**

| 값 | 방향 |
|----|------|
| 0 | Local x (+) |
| 1 | Local x (–) |
| 2 | Local y (+) |
| 3 | Local y (–) |
| 4 | Local z (+) |
| 5 | Local z (–) |

### 요청 바디 예시

```json
{
  "Assign": {
    "53": { "DIR": 0 },
    "55": { "DIR": 1 },
    "57": { "DIR": 2 },
    "59": { "DIR": 3 },
    "61": { "DIR": 4 },
    "63": { "DIR": 5 }
  }
}
```

### Python 예제

```python
# --- CLDR: 구속 레이블 방향 설정 ---
# 키: 절점 ID, 값: DIR(0~5)

cldr_data = {
    "Assign": {
        "10": {"DIR": 4},   # Local z (+) 방향으로 레이블 표시
        "11": {"DIR": 4},
        "12": {"DIR": 4},
        "20": {"DIR": 0},   # Local x (+) 방향
    }
}

midas_api("POST", "/db/CLDR", cldr_data)
```

---

## 24. `/db/DRLS` — Diaphragm Disconnect

다이어프램에서 특정 절점을 제외(해제)합니다.  
`Assign` 키는 **절점 ID**, 값은 빈 객체 `{}` 입니다.

**Endpoint:** `{base url}/db/DRLS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Assign Object · 키=절점 번호, 값=빈 객체 | `"Assign"` | Object | `{}` | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {},
    "2": {},
    "5": {}
  }
}
```

### Python 예제

```python
# --- DRLS: 다이어프램 해제 ---
# 다이어프램에서 분리할 절점 ID를 키로 지정
# 예: 수직 부재, 코어벽 연결 절점 등을 다이어프램에서 제외

drls_data = {
    "Assign": {
        "5": {},    # 절점 5를 다이어프램에서 해제
        "12": {},   # 절점 12 해제
        "18": {},   # 절점 18 해제
    }
}

# 다이어프램 해제 절점 등록
midas_api("POST", "/db/DRLS", drls_data)

# 현재 해제 목록 조회
current_drls = midas_api("GET", "/db/DRLS")

# 특정 절점(ID=5) 해제 취소
midas_api("DELETE", "/db/DRLS", {"Assign": {"5": {}}})
```

---

## 전체 Boundary 설정 예제 (워크플로)

아래는 일반적인 RC 건물 모델에서 Boundary 데이터를 순서대로 입력하는 실무 예제입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "your-mapi-key-here"

def midas_api(method, endpoint, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    r = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{r.status_code}] {method.upper()} {endpoint}")
    return r.json() if r.text else {}

# ── STEP 1: 지지조건 입력 ──────────────────────────────────────
# 1층 기둥 하단 절점(1~4) 완전 고정
cons_data = {
    "Assign": {
        str(n): {
            "ITEMS": [{"ID": n, "GROUP_NAME": "Foundation", "CONSTRAINT": "1111111"}]
        }
        for n in range(1, 5)
    }
}
midas_api("POST", "/db/CONS", cons_data)

# ── STEP 2: 힘-변위 함수 정의 (비선형 링크용) ────────────────────
mlfc_data = {
    "Assign": {
        "1": {
            "NAME": "Isolator_FD",
            "TYPE": "FORCE", "SYMM": True, "FUNC_ID": 0,
            "ITEMS": [
                {"X": 0.00, "Y":    0},
                {"X": 0.05, "Y":  300},
                {"X": 0.15, "Y":  500},
                {"X": 0.30, "Y":  600}
            ]
        }
    }
}
midas_api("POST", "/db/MLFC", mlfc_data)

# ── STEP 3: 강체 링크 (층 다이어프램) ────────────────────────────
rigd_data = {
    "Assign": {
        "100": {
            "ITEMS": [{
                "ID": 100,
                "GROUP_NAME": "Floor_Diaphragm",
                "DOF": 110001,           # DX, DY, RZ 구속
                "S_NODE": list(range(5, 25))  # 5∼24 슬레이브 절점
            }]
        }
    }
}
midas_api("POST", "/db/RIGD", rigd_data)

# ── STEP 4: 보 단부 해제 (핀 접합 보) ────────────────────────────
frls_data = {
    "Assign": {
        str(eid): {
            "ITEMS": [{
                "ID": eid,
                "GROUP_NAME": "Pin_Beams",
                "bVALUE": False,
                "FLAG_I": "0000110",   # My, Mz 해제
                "VALUE_I": [0]*7,
                "FLAG_J": "0000110",
                "VALUE_J": [0]*7
            }]
        }
        for eid in [101, 102, 103, 104]
    }
}
midas_api("POST", "/db/FRLS", frls_data)

# ── STEP 5: 패널 존 효과 ──────────────────────────────────────
midas_api("POST", "/db/PZEF", {
    "Assign": {"1": {"OPT_OFFSET": True, "OFFS_FACTOR": 1.0, "OUTPUT_POSITION": 1}}
})

print("Boundary 설정 완료")
```

---

> **[05_DB_Boundary.md] 작성 완료 — 다음 파일 [06_DB_Static_Loads.md] 진행 준비가 되었습니다.**
