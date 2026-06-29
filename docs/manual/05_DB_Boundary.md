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
| 19 | [`/db/SDHY`](#19-dbsdhy--seismic-device--hysteretic-isolatormss) | Seismic Device – Hysteretic Isolator (MSS) |
| 20 | [`/db/SDIS`](#20-dbsdis--seismic-device--isolatormss) | Seismic Device – Isolator (MSS) |
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

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Point Spring (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Spring Type · `"LINEAR"` / `"COMP"` / `"TENS"` / `"MULTI"` | `"TYPE"` | String | — | Required |
| (3) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Create Function Type · 0=점 스프링 함수, 1=면 스프링 함수 | `"FormType"` | Integer | 0 | Optional |
| — | **LINEAR 전용** | | | | |
| (5) | Spring Stiffness `[SDx, SDy, SDz, SRx, SRy, SRz]` | `"SDR"` | Array[Number,6] | — | Required |
| (6) | Fixed Option `[SDx, SDy, SDz, SRx, SRy, SRz]` | `"F_S"` | Array[Boolean,6] | false | Optional |
| (7) | Damping Constant | `"DAMPING"` | Boolean | — | Optional |
| — | **COMP / TENS / MULTI 전용** | | | | |
| (5) | Direction · 1=Dx, 2=Dy, 3=Dz, 4=Dy&Dz | `"DIR"` | Integer | — | Required |
| (6) | Displacement Values `[Disp_1, Disp_2, Disp_3]` | `"DV"` | Array[Number] | — | Required |
| (7) | Spring Stiffness Values `[K_1, K_2, K_3]` | `"SK"` | Array[Number] | — | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "2": {
      "ITEMS": [{
        "ID": 1, "TYPE": "LINEAR", "GROUP_NAME": "Service",
        "SDR": [1000, 500, 500, 0, 0, 0],
        "F_S": [false, false, false, false, false, false]
      }]
    },
    "4": {
      "ITEMS": [{
        "ID": 1, "TYPE": "COMP", "GROUP_NAME": "Service",
        "DIR": 4, "DV": [0, 0, 0], "SK": [1000, 0, 0]
      }]
    }
  }
}
```

### Python 예제

```python
# --- NSPR: 점 스프링 배정 ---

# 절점 2: 선형 스프링 (수평 Kx=1000, Ky=500 kN/m)
nspr_linear = {
    "Assign": {
        "2": {
            "ITEMS": [{
                "ID": 2,
                "TYPE": "LINEAR",
                "GROUP_NAME": "Foundation_Spring",
                "SDR": [1000.0, 500.0, 500.0, 0.0, 0.0, 0.0],
                "F_S": [False, False, False, False, False, False]
            }]
        }
    }
}

# 절점 4: 압축 전용 스프링 (토압 방향)
nspr_comp = {
    "Assign": {
        "4": {
            "ITEMS": [{
                "ID": 4,
                "TYPE": "COMP",
                "GROUP_NAME": "Soil_Spring",
                "DIR": 4,            # Dy & Dz
                "DV": [0.0, 0.0, 0.0],
                "SK": [2000.0, 0.0, 0.0]
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

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | General Spring Name | `"NAME"` | String | — | Required |
| 2 | Stiffness Matrix Option | `"OPT_STIFFNESS"` | Boolean | false | Optional |
| 3 | Stiffness Matrix (상삼각 21항) | `"SPRING"` | Array[Number,21] | 0 | Optional |
| 4 | Mass Matrix Option | `"OPT_MASS"` | Boolean | false | Optional |
| 5 | Mass Matrix (상삼각 21항) | `"MASS"` | Array[Number,21] | 0 | Optional |
| 6 | Damping Matrix Option | `"OPT_DAMPING"` | Boolean | false | Optional |
| 7 | Damping Matrix (상삼각 21항) | `"DAMPING"` | Array[Number,21] | 0 | Optional |

> **주의:** `SPRING`/`MASS`/`DAMPING` 배열은 옵션 플래그가 `true`일 때만 유효합니다.

### 요청 바디 예시

```json
{
  "Assign": {
    "3": {
      "NAME": "GS_Damping",
      "OPT_STIFFNESS": true,
      "SPRING": [1000, 0, 0, 0, 0, 0, 500, 0, 0, 0, 0, 500, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      "OPT_DAMPING": true,
      "DAMPING": [50, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
  }
}
```

### Python 예제

```python
# --- GSTP: 일반 스프링 타입 정의 ---
# 상삼각 행렬 21항 순서: K11, K12, K13, K14, K15, K16,
#                           K22, K23, K24, K25, K26,
#                               K33, K34, K35, K36,
#                                   K44, K45, K46,
#                                       K55, K56,
#                                           K66

gstp_data = {
    "Assign": {
        "1": {
            "NAME": "Foundation_GS",
            "OPT_STIFFNESS": True,
            # Kx=1000, Ky=800, Kz=800, 회전 0 (대각항만 값)
            "SPRING": [
                1000, 0, 0, 0, 0, 0,
                      800, 0, 0, 0, 0,
                           800, 0, 0, 0,
                                0, 0, 0,
                                   0, 0,
                                      0
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

| LINK 값 | 설명 | 추가 키 |
|---------|------|---------|
| `"GEN"` | General (6자유도 스프링) | `SDR[6]`, `R_S[6]`, `bSHEAR`, `DR[2]` |
| `"RIGID"` | 강체 링크 | (없음) |
| `"SADDLE"` | 안장 (교량 받침 특화) | (없음) |
| `"TENS"` | Tension-Only | `SDR[6]` (Dx만 유효) |
| `"COMP"` | Compression-Only | `SDR[6]` (Dx만 유효) |
| `"MULTILINEAR"` | Multi-Linear | `DIR`, `MLFC`(함수 ID), `bSHEAR`, `DRENDI` |
| `"RAILINTERACT"` | Rail Track Interaction | `DIR`, `RLFC`(함수 ID), `bSHEAR`, `DRENDI` |

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

Hyper-S 솔버 전용 일반 링크 배정 엔드포인트입니다. 공식 사이트의 JSON 스키마 예제는 제공되지 않으나, 파라미터 구조는 NLNK에 준합니다.

**Endpoint:** `{base url}/db/NLNK-M1`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 요청 파라미터

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | General Link Property Name | `"PROP_NAME"` | String | — | Required |
| 2 | Node 1 ID | `"NODE1"` | Integer | — | Required |
| 3 | Node 2 ID | `"NODE2"` | Integer | — | Required |

### Python 예제

```python
# --- NLNK-M1: Hyper-S 전용 일반 링크 배정 ---
# Hyper-S 솔버 사용 시에만 유효

nlnk_m1_data = {
    "Assign": {
        "1": {
            "PROP_NAME": "GL_HyperS_Prop",
            "NODE1": 20,
            "NODE2": 21
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
| 6 | Property Data (DOF별 6항목) | `"ITEM"` | Array[Object,6] | Required |
| (1) | DOF 활성화 여부 | `"OPT_DOF"` | Boolean | Required |
| (2) | 초기 감쇠계수 CE | `"CE"` | Number | Required |
| (3) | 최대 감쇠력 P₁ | `"P1"` | Number | Required |
| (4) | 이차 감쇠계수 C₁ | `"C1"` | Number | Required |
| (5) | 감쇠 감소 계수 α₁ | `"ALPHA1"` | Number | Required |
| (6) | 초기 강성 K₀ | `"K0"` | Number | Required |

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
      "ITEM": [
        { "OPT_DOF": true, "CE": 500, "P1": 1000, "C1": 200, "ALPHA1": 0.5, "K0": 0 },
        { "OPT_DOF": false, "CE": 0, "P1": 0, "C1": 0, "ALPHA1": 1, "K0": 0 },
        { "OPT_DOF": false, "CE": 0, "P1": 0, "C1": 0, "ALPHA1": 1, "K0": 0 },
        { "OPT_DOF": false, "CE": 0, "P1": 0, "C1": 0, "ALPHA1": 1, "K0": 0 },
        { "OPT_DOF": false, "CE": 0, "P1": 0, "C1": 0, "ALPHA1": 1, "K0": 0 },
        { "OPT_DOF": false, "CE": 0, "P1": 0, "C1": 0, "ALPHA1": 1, "K0": 0 }
      ]
    }
  }
}
```

### Python 예제

```python
# --- SDVI: 점성 댐퍼 물성 정의 ---
# ITEM 배열 순서: Dx, Dy, Dz, Rx, Ry, Rz

def make_dof_item(active, CE=0, P1=0, C1=0, alpha1=1.0, K0=0):
    return {"OPT_DOF": active, "CE": CE, "P1": P1, "C1": C1, "ALPHA1": alpha1, "K0": K0}

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

| No. | 설명 | 키 | 타입 | 필수 |
|-----|------|----|------|------|
| 1 | Common Data (SDVI와 동일 구조) | `"COMMON"` | Object | Required |
| 2 | Material Type · `"GR100"` / `"GR300"` / `"SR05"` / `"GR400"` / `"CST"` / `"TRC"` | `"MATERIAL_TYPE"` | String | Required |
| 3 | Shear Area | `"SHEAR_AREA"` | Number | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "Viscoelastic01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "VE-200", "TYPE_NUMBER": "VE200-A"
      },
      "MATERIAL_TYPE": "GR100",
      "SHEAR_AREA": 0.05
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
            "SHEAR_AREA": 0.05          # 전단 면적 (m²)
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

| No. | 설명 | 키 | 타입 | 필수 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| 2 | Direction | `"DIR"` | String | Required |
| 3 | Hysteresis Model · `"BL2"` 등 | `"SDST_HYS_MODEL"` | String | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "SteelDamper01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "SD-300", "TYPE_NUMBER": "SD300-A"
      },
      "DIR": "Dx",
      "SDST_HYS_MODEL": "BL2"
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
            "SDST_HYS_MODEL": "BL2"     # Bilinear 이력 모델
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

| No. | 설명 | 키 | 타입 | 필수 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| 2 | Hysteresis Model · `"DegradingBiLinear"` 등 | `"SDHY_HYS_MODEL"` | String | Required |
| 3 | Number of Shear Springs (MSS 전단 스프링 수) | `"MSS"` | Integer | Required |
| 4 | Initial Stiffness K₀ | `"K0"` | Number | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "HystereticIsolator01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "HI-500", "TYPE_NUMBER": "HI500-A"
      },
      "SDHY_HYS_MODEL": "DegradingBiLinear",
      "MSS": 8,
      "K0": 5000
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
            "K0": 5000.0        # 초기 강성 (kN/m)
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

| No. | 설명 | 키 | 타입 | 필수 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| 2 | Device Type · `"LRB"` / `"NRB"` / `"SB"` | `"SDIS_DEV_TYPE"` | String | Required |
| 3 | Number of Shear Springs | `"MSS"` | Integer | Required |
| 4 | Adjustment Parameter τk | `"TAU_K"` | Number | Required |
| 5 | Adjustment Parameter τq | `"TAU_Q"` | Number | Required |
| 6 | Vertical Stiffness Kv | `"KV"` | Number | Required |
| 7 | LRB Data (SDIS_DEV_TYPE="LRB"일 때) | `"LRB"` | Object | Required |
| — | Hysteresis Model | `"SDIS_HYS_MODEL"` | String | Required |
| — | Rubber Cross Section Area AR | `"AR"` | Number | Required |
| — | Total Thickness of Rubber TR | `"TR"` | Number | Required |
| — | Initial Stiffness KE | `"KE"` | Number | Required |
| — | 2nd Stiffness K2 | `"K2"` | Number | Required |
| — | Characteristic Strength QD | `"QD"` | Number | Required |
| 8 | NRB Data (SDIS_DEV_TYPE="NRB"일 때) | `"NRB"` | Object | Required |
| — | Horizontal Stiffness KH | `"KH"` | Number | Required |
| 9 | SB Data (SDIS_DEV_TYPE="SB"일 때) | `"SB"` | Object | Required |
| — | Area of Sliding Head AS | `"AS"` | Number | Required |
| — | Initial Stiffness K₀ | `"K0"` | Number | Required |
| — | Frictional Factor μ₀ | `"MU0"` | Number | Required |

### 요청 바디 예시 (LRB)

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
        "AR": 0.196, "TR": 0.15, "KE": 20000, "K2": 2000,
        "QD": 80, "DX": 0, "OPT_CONS_NONL": false,
        "BETA": 0.1, "ALPHA": 0.5, "SIGMA_V": 3000
      }
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
                "AR": 0.196,    # 고무 단면적 (m²)
                "TR": 0.150,    # 고무 총 두께 (m)
                "KE": 20000.0,  # 초기 강성 (kN/m)
                "K2": 2000.0,   # 이차 강성 (kN/m)
                "QD": 80.0,     # 특성강도 (kN)
                "DX": 0,        # 수직 방향 설정
                "OPT_CONS_NONL": False,
                "BETA": 0.1,
                "ALPHA": 0.5,
                "SIGMA_V": 3000.0   # 인장 강도 한계 (kN/m²)
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

| No. | 설명 | 키 | 타입 | 기본값 | 필수 |
|-----|------|----|------|--------|------|
| 1 | Linear Constraints (배열로 삽입) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | DOF of Constraint Node (6자리: DX∼RZ) | `"SLAVE_TYPE"` | String(6) | — | Required |
| (4) | Constraint Type · `"EX"`=Explicit, `"WD"`=Weighted Displacement | `"TYPE"` | String | — | Required |
| (5) | Independent Nodes (Explicit: 등변위 / WD: 계수 곱) | `"SLAVES"` | Array[Object] | — | Required |
| i | Node ID | `"NODE_KEY"` | Integer | — | Required |
| ii | Coefficient | `"COEFF"` | Number | — | Required |

### 요청 바디 예시

```json
{
  "Assign": {
    "21": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service", "SLAVE_TYPE": "100000",
        "TYPE": "EX",
        "SLAVES": [
          { "NODE_KEY": 10, "COEFF": 1.0 },
          { "NODE_KEY": 11, "COEFF": -1.0 }
        ]
      }]
    }
  }
}
```

### Python 예제

```python
# --- MCON: 선형 구속조건 (층 다이어프램 구속 대안) ---
# EX 타입: 두 절점의 특정 DOF를 등변위 구속
# WD 타입: 가중치 곱 변위 구속 (경사 지붕, 비정형 구조 등)

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
                    {"NODE_KEY": 5,  "COEFF":  1.0},
                    {"NODE_KEY": 10, "COEFF": -1.0}
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
                    {"NODE_KEY": 10, "COEFF": 0.5},
                    {"NODE_KEY": 15, "COEFF": 0.5}
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
