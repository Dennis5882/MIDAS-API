# 25. Design Code – STEEL KDS 41 30:2022 (강재 설계)

> **대상 제품:** MIDAS Gen NX · MIDAS Civil NX
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

이 장은 **강재(Steel) 설계 기준 KDS 41 30:2022** 의 설계 입력·수행·결과 관련 **27개 엔드포인트**를 다룹니다. 모든 엔드포인트는 다음 공통 URI 접두어를 공유합니다.

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/<CODE>
```

여기서 `<CODE>`는 각 엔드포인트 코드(`DCO`, `LENG`, `MEMB`, `CODE-ANAL` 등)입니다.

> **공통 규약 — 요청 래퍼:**
> - **설정(config)·부재(member) 엔드포인트**는 최상위에 `"Assign"` 객체를 두고, 그 안에서 대상 ID(요소·부재·재질 ID 등)를 **문자열 키**로 사용하여 각 레코드를 담습니다. GET 응답은 최상위 키가 해당 엔드포인트 코드(예: `DCO`, `LENG`)로 바뀌어 동일 구조로 반환됩니다.
> - **수행/결과(action) 엔드포인트**는 `"Assign"` 대신 최상위에 `"Argument"` 객체를 두는 POST 전용 작업입니다.

> **메서드 패턴 3종:**
> 1. **Config-singleton** (예: `DCO`, `DCTL`, `LLRF`, `SRDF`, `SMODI`, `MEMB`) — 모델당 하나의 전역/집합 설정으로, **POST가 없습니다**. 레코드는 최초 조회 시 암묵적으로 생성되거나 **PUT** 으로 설정/수정합니다. (`LCTB`는 `GET`·`DELETE`만 지원하는 파생 정보입니다.)
> 2. **Member-CRUD** (예: `HCBM`, `LENG`, `KFAC`, `LTSR`, `SLRS`, `SERV`, `EQCT`, `ULCT`, `SUEQ`, `CRCM`, `CMFT`, `FMAG`, `CBFT`, `MBTP`, `MLLR`) — 부재/ID 키 기반 **전체 CRUD**(POST·GET·PUT·DELETE)를 지원합니다.
> 3. **POST-action** (`CODE-ANAL`, `CODE-TABLE`, `CODE-REPORT`, `DREULT`, `TABLE`) — 검토 수행·결과표·보고서·이미지 출력 등의 **작업으로 POST만** 지원합니다.

> ⚠️ **엔드포인트마다 Active Methods가 다릅니다.** 아래 각 절의 **Active Methods**를 정확히 따르세요. (예: `DCO`/`DCTL`/`LLRF`/`SMODI`/`MEMB` = GET·PUT·DELETE, `LCTB` = GET·DELETE, `SRDF` = GET·DELETE·PUT, 5개 action 엔드포인트 = POST.)

---

## Endpoint 목록

### 그룹 1. 설계 코드·일반 설정

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`.../DCO`](#1-designsteelkds-41-30-2022dco--design-code-option-설계-코드-옵션) | Design Code Option (설계 코드 옵션) | GET · PUT · DELETE |
| 2 | [`.../DCTL`](#2-designsteelkds-41-30-2022dctl--definition-of-frame-프레임-정의) | Definition of Frame (프레임 정의) | GET · PUT · DELETE |
| 3 | [`.../LLRF`](#3-designsteelkds-41-30-2022llrf--live-load-reduction-factor-활하중-저감계수) | Live Load Reduction Factor (활하중 저감계수) | GET · PUT · DELETE |
| 4 | [`.../LCTB`](#4-designsteelkds-41-30-2022lctb--load-contribution-for-nonlinear-load-case-비선형-하중케이스-하중기여) | Load Contribution for Nonlinear Load Case (비선형 하중케이스 하중기여) | GET · DELETE |
| 5 | [`.../SRDF`](#5-designsteelkds-41-30-2022srdf--strength-reduction-factors-강도감소계수-φ) | Strength Reduction Factors (강도감소계수 φ) | GET · DELETE · PUT |
| 6 | [`.../SERV`](#6-designsteelkds-41-30-2022serv--serviceability-parameters-사용성-파라미터) | Serviceability Parameters (사용성 파라미터) | POST · GET · PUT · DELETE |
| 7 | [`.../EQCT`](#7-designsteelkds-41-30-2022eqct--seismic-load-combination-type-지진하중-조합-타입) | Seismic Load Combination Type (지진하중 조합 타입) | POST · GET · PUT · DELETE |
| 8 | [`.../ULCT`](#8-designsteelkds-41-30-2022ulct--underground-load-combination-type-지하-하중조합-타입) | Underground Load Combination Type (지하 하중조합 타입) | POST · GET · PUT · DELETE |
| 9 | [`.../SUEQ`](#9-designsteelkds-41-30-2022sueq--scale-up-factor-for-earthquake-지진-증폭계수) | Scale up Factor for Earthquake (지진 증폭계수) | POST · GET · PUT · DELETE |
| 10 | [`.../CRCM`](#10-designsteelkds-41-30-2022crcm--combined-ratio-calculation-method-for-circular-section-원형단면-조합비-계산법) | Combined Ratio Calculation Method for Circular Section (원형단면 조합비 계산법) | POST · GET · PUT · DELETE |

### 그룹 2. 부재별 설계 파라미터

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 11 | [`.../HCBM`](#11-designsteelkds-41-30-2022hcbm--haunched-beam-assignment-헌치-보-배정) | Haunched Beam Assignment (헌치 보 배정) | POST · GET · PUT · DELETE |
| 12 | [`.../LENG`](#12-designsteelkds-41-30-2022leng--unbraced-length-비지지-길이-l-lb) | Unbraced Length (비지지 길이 L, Lb) | POST · GET · PUT · DELETE |
| 13 | [`.../KFAC`](#13-designsteelkds-41-30-2022kfac--effective-length-factor-유효좌굴길이계수-k) | Effective Length Factor (유효좌굴길이계수 K) | POST · GET · PUT · DELETE |
| 14 | [`.../LTSR`](#14-designsteelkds-41-30-2022ltsr--limiting-slenderness-ratio-세장비-제한) | Limiting Slenderness Ratio (세장비 제한) | POST · GET · PUT · DELETE |
| 15 | [`.../CMFT`](#15-designsteelkds-41-30-2022cmft--equivalent-moment-correction-factor-등가모멘트-보정계수-cm) | Equivalent Moment Correction Factor (등가모멘트 보정계수 Cm) | POST · GET · PUT · DELETE |
| 16 | [`.../FMAG`](#16-designsteelkds-41-30-2022fmag--moment-magnifier-모멘트-증폭계수-b1δb-b2δs) | Moment Magnifier (모멘트 증폭계수 B1/Δb, B2/Δs) | POST · GET · PUT · DELETE |
| 17 | [`.../CBFT`](#17-designsteelkds-41-30-2022cbft--bending-coefficient-휨계수-cb) | Bending Coefficient (휨계수 Cb) | POST · GET · PUT · DELETE |
| 18 | [`.../MBTP`](#18-designsteelkds-41-30-2022mbtp--modify-member-type-부재-타입-수정) | Modify Member Type (부재 타입 수정) | POST · GET · PUT · DELETE |
| 19 | [`.../SLRS`](#19-designsteelkds-41-30-2022slrs--seismic-load-resisting-system-by-member-부재별-내진-저항시스템) | Seismic Load Resisting System by Member (부재별 내진 저항시스템) | POST · GET · PUT · DELETE |
| 20 | [`.../MLLR`](#20-designsteelkds-41-30-2022mllr--modify-live-load-reduction-factor-활하중-저감계수-수정) | Modify Live Load Reduction Factor (활하중 저감계수 수정) | POST · GET · PUT · DELETE |
| 21 | [`.../MEMB`](#21-designsteelkds-41-30-2022memb--member-assignment-설계-부재-배정) | Member Assignment (설계 부재 배정) | GET · PUT · DELETE |

### 그룹 3. 재료

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 22 | [`.../SMODI`](#22-designsteelkds-41-30-2022smodi--modify-steel-material-강재-재질-수정) | Modify Steel Material (강재 재질 수정) | GET · PUT · DELETE |

### 그룹 4. 설계 수행·결과 (POST 전용)

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 23 | [`.../CODE-ANAL`](#23-designsteelkds-41-30-2022code-anal--steel-code-check-perform-강재-코드-검토-수행) | Steel Code Check Perform (강재 코드 검토 수행) | POST |
| 24 | [`.../CODE-TABLE`](#24-designsteelkds-41-30-2022code-table--steel-code-check-table-강재-코드-검토-표) | Steel Code Check Table (강재 코드 검토 표) | POST |
| 25 | [`.../CODE-REPORT`](#25-designsteelkds-41-30-2022code-report--steel-code-check-report-강재-코드-검토-보고서) | Steel Code Check Report (강재 코드 검토 보고서) | POST |
| 26 | [`.../DREULT`](#26-designsteelkds-41-30-2022dreult--steel-design-result-강재-설계-결과-이미지) | Steel Design Result (강재 설계 결과 이미지) | POST |
| 27 | [`.../TABLE`](#27-designsteelkds-41-30-2022table--steel-member-design-forces-강재-부재-설계-부재력) | Steel Member Design Forces (강재 부재 설계 부재력) | POST |

---

## 1. `DESIGN/STEEL/KDS-41-30-2022/DCO` — Design Code Option (설계 코드 옵션)

> **기능:** 강재 설계 기준(KDS 41 30:2022) 및 횡지지·처짐검토·내진 특별규정·원형단면 조합비 방법 등 전역 설계 옵션을 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/DCO
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Steel Design Code",
          "type": "object",
          "required": [
            "DGNCODE"
          ],
          "additionalProperties": false,
          "properties": {
            "DGNCODE": {
              "type": "string",
              "description": "Design Code",
              "enum": [
                "KDS 41 30 : 2022"
              ]
            },
            "LAT_BRACE": {
              "type": "boolean",
              "description": "All Beams/Girders are Laterally Braced",
              "default": false
            },
            "DEFL_CHK": {
              "type": "boolean",
              "description": "Check Beam/Column Deflection",
              "default": true
            },
            "SEISMIC": {
              "type": "boolean",
              "description": "Apply Special Provisions for Seismic Design",
              "default": false
            },
            "COMB_RATIO": {
              "type": "integer",
              "description": "Combined Ratio Method for Circular Section",
              "default": 0,
              "oneOf": [
                {
                  "title": "SRSS (Square root of sum of square)",
                  "const": 0
                },
                {
                  "title": "Linear Sum",
                  "const": 1
                }
              ]
            },
            "SEIS_SYS": {
              "type": "string",
              "description": "Seismic Load Resisting System",
              "enum": [
                "Special Moment Frames",
                "Intermediate Moment Frames",
                "Ordinary Moment Frames",
                "Special Concentrically Braced Frames",
                "Ordinary Concentrically Braced Frames",
                "Eccentrically Braced Frames",
                "Buckling-Restrained Braced Frames",
                "Special Plate Shear Walls"
              ],
              "default": "Special Moment Frames"
            },
            "COL_WEAK": {
              "type": "boolean",
              "description": "Consider strong column-weak beam on last floor",
              "default": true
            },
            "UNDGR_LD": {
              "type": "boolean",
              "description": "Use Under Ground Load Combination Type for Under Ground Members",
              "default": true
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 (ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 설계 코드 (KDS 41 30 : 2022 고정) | `"DGNCODE"` | String (enum) | — | **필수** |
| 3 | 모든 보/거더 횡지지 가정 | `"LAT_BRACE"` | Boolean | `false` | 선택 |
| 4 | 보/기둥 처짐 검토 | `"DEFL_CHK"` | Boolean | `true` | 선택 |
| 5 | 내진설계 특별규정 적용 | `"SEISMIC"` | Boolean | `false` | 선택 |
| 6 | 원형단면 조합비 방법 (0=SRSS, 1=Linear Sum) | `"COMB_RATIO"` | Integer | `0` | 선택 |
| 7 | 내진 저항시스템 (SEISMIC=true일 때) — Special/Intermediate/Ordinary Moment Frames, Special/Ordinary Concentrically Braced Frames, Eccentrically Braced Frames, Buckling-Restrained Braced Frames, Special Plate Shear Walls | `"SEIS_SYS"` | String (enum) | `"Special Moment Frames"` | 조건부 필수 |
| 8 | 최상층 강기둥-약보 고려 | `"COL_WEAK"` | Boolean | `true` | 선택 |
| 9 | 지하부재에 지하 하중조합 타입 사용 | `"UNDGR_LD"` | Boolean | `true` | 선택 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "KDS 41 30 : 2022",
      "LAT_BRACE": false,
      "DEFL_CHK": true,
      "SEISMIC": true,
      "COMB_RATIO": 1,
      "SEIS_SYS": "Special Moment Frames",
      "COL_WEAK": true,
      "UNDGR_LD": true
    }
  }
}
```

**GET Response Body**

```json
{
  "DCO": {
    "1": {
      "DGNCODE": "KDS 41 30 : 2022",
      "LAT_BRACE": false,
      "DEFL_CHK": true,
      "SEISMIC": true,
      "COMB_RATIO": 1,
      "UNDGR_LD": true,
      "SEIS_SYS": "Special Moment Frames",
      "COL_WEAK": true
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/DCO"

# 1) 설정 (PUT)
payload = {
  "Assign": {
    "1": {
      "DGNCODE": "KDS 41 30 : 2022",
      "LAT_BRACE": false,
      "DEFL_CHK": true,
      "SEISMIC": true,
      "COMB_RATIO": 1,
      "SEIS_SYS": "Special Moment Frames",
      "COL_WEAK": true,
      "UNDGR_LD": true
    }
  }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 조회 (GET)
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 삭제 (DELETE) — 필요 시
# requests.delete(URI, headers=HEADERS)
```

---

## 2. `DESIGN/STEEL/KDS-41-30-2022/DCTL` — Definition of Frame (프레임 정의)

> **기능:** 설계 프레임의 X/Y 방향 횡지지 여부(Sway/Non-sway), 유효좌굴길이계수 자동계산, 설계 타입(3D/평면)을 정의합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/DCTL
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "description": "Definition of Frame (shared structure: T_DCTL_D). Supported methods: GET, PUT.",
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "FRAMEX": {
              "type": "string",
              "description": "X-Direction of Frame",
              "default": "Braced Non-sway",
              "oneOf": [
                {
                  "title": "Unbraced | Sway",
                  "const": "Unbraced Sway"
                },
                {
                  "title": "Braced | Non-sway",
                  "const": "Braced Non-sway"
                }
              ]
            },
            "FRAMEY": {
              "type": "string",
              "description": "Y-Direction of Frame",
              "default": "Braced Non-sway",
              "oneOf": [
                {
                  "title": "Unbraced | Sway",
                  "const": "Unbraced Sway"
                },
                {
                  "title": "Braced | Non-sway",
                  "const": "Braced Non-sway"
                }
              ]
            },
            "bAUTOKF": {
              "type": "boolean",
              "description": "Auto Calculate Effective Length Factor",
              "default": false
            },
            "DT": {
              "type": "string",
              "description": "Design Type",
              "default": "3D",
              "oneOf": [
                {
                  "title": "3-D",
                  "const": "3D"
                },
                {
                  "title": "X-Z Plane",
                  "const": "XZ"
                },
                {
                  "title": "Y-Z Plane",
                  "const": "YZ"
                },
                {
                  "title": "X-Y Plane",
                  "const": "XY"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 (ID 1개만 허용, maxProperties=1) | `"Assign"` | Object | — | **필수** |
| 2 | X방향 프레임 (`"Unbraced Sway"`=비횡지지·Sway, `"Braced Non-sway"`=횡지지·Non-sway) | `"FRAMEX"` | String (oneOf) | `"Braced Non-sway"` | 선택 |
| 3 | Y방향 프레임 (값은 FRAMEX와 동일) | `"FRAMEY"` | String (oneOf) | `"Braced Non-sway"` | 선택 |
| 4 | 유효좌굴길이계수 자동계산 | `"bAUTOKF"` | Boolean | `false` | 선택 |
| 5 | 설계 타입 (`"3D"`=3-D, `"XZ"`=X-Z평면, `"YZ"`=Y-Z평면, `"XY"`=X-Y평면) | `"DT"` | String (oneOf) | `"3D"` | 선택 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": true,
      "DT": "XZ"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCTL": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": true,
      "DT": "XZ"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/DCTL"

# 1) 설정 (PUT)
payload = {
  "Assign": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": true,
      "DT": "XZ"
    }
  }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 조회 (GET)
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 삭제 (DELETE) — 필요 시
# requests.delete(URI, headers=HEADERS)
```

---

## 3. `DESIGN/STEEL/KDS-41-30-2022/LLRF` — Live Load Reduction Factor (활하중 저감계수)

> **기능:** 층·평면 범위별 활하중 저감계수 테이블과 적용 성분(축력/모멘트/전단)을 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/LLRF
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "REDUCTION_DATA"
          ],
          "additionalProperties": false,
          "properties": {
            "CALC_RULE": {
              "type": "integer",
              "default": 0,
              "oneOf": [
                {
                  "title": "by General Design Code",
                  "const": 0
                },
                {
                  "title": "by Chinese Standard",
                  "const": 1
                }
              ]
            },
            "APPLIED_COMP": {
              "type": "array",
              "description": "Applied Components Selection",
              "items": {
                "type": "string",
                "enum": [
                  "ALL",
                  "AXIAL",
                  "MOMENTS",
                  "SHEAR"
                ]
              },
              "default": [
                "AXIAL"
              ]
            },
            "LIVE_LOAD_CASES": {
              "type": "array",
              "description": "Live Load Case Names (user defined list)",
              "items": {
                "type": "string"
              }
            },
            "REDUCTION_DATA": {
              "type": "array",
              "description": "Live Load Reduction Factor Table Data",
              "items": {
                "type": "object",
                "required": [
                  "STORY"
                ],
                "properties": {
                  "STORY": {
                    "type": "string",
                    "description": "Story Name"
                  },
                  "XMIN": {
                    "type": "number",
                    "default": 0,
                    "description": "X Min coordinate"
                  },
                  "XMAX": {
                    "type": "number",
                    "default": 0,
                    "description": "X Max coordinate"
                  },
                  "YMIN": {
                    "type": "number",
                    "default": 0,
                    "description": "Y Min coordinate"
                  },
                  "YMAX": {
                    "type": "number",
                    "default": 0,
                    "description": "Y Max coordinate"
                  },
                  "RANGE_MAX": {
                    "type": "number",
                    "description": "Range Max value (only for General Design Code)",
                    "enum": [
                      1,
                      0.95,
                      0.9,
                      0.85,
                      0.8,
                      0.75,
                      0.7,
                      0.65,
                      0.6,
                      0.55,
                      0.5
                    ],
                    "default": 1
                  },
                  "RANGE_MIN": {
                    "type": "number",
                    "description": "Range Min value (only for General Design Code)",
                    "enum": [
                      1,
                      0.95,
                      0.9,
                      0.85,
                      0.8,
                      0.75,
                      0.7,
                      0.65,
                      0.6,
                      0.55,
                      0.5
                    ],
                    "default": 0.5
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 계산 규칙 (0=by General Design Code, 1=by Chinese Standard) | `"CALC_RULE"` | Integer | `0` | 선택 |
| 3 | 적용 성분 (`"ALL"`,`"AXIAL"`,`"MOMENTS"`,`"SHEAR"`) | `"APPLIED_COMP"` | Array[String] | `["AXIAL"]` | 선택 |
| 4 | 활하중 케이스 이름 목록 | `"LIVE_LOAD_CASES"` | Array[String] | — | 선택 |
| 5 | 저감계수 테이블 데이터 | `"REDUCTION_DATA"` | Array[Object] | — | **필수** |
| 5.1 | 층 이름 | `"STORY"` | String | — | **필수** |
| 5.2 | X 최소 좌표 | `"XMIN"` | Number | `0` | 선택 |
| 5.3 | X 최대 좌표 | `"XMAX"` | Number | `0` | 선택 |
| 5.4 | Y 최소 좌표 | `"YMIN"` | Number | `0` | 선택 |
| 5.5 | Y 최대 좌표 | `"YMAX"` | Number | `0` | 선택 |
| 5.6 | Rmax (General Design Code 전용, enum 1~0.5) | `"RANGE_MAX"` | Number | `1` | 선택 |
| 5.7 | Rmin (General Design Code 전용, enum 1~0.5) | `"RANGE_MIN"` | Number | `0.5` | 선택 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "CALC_RULE": 0,
      "APPLIED_COMP": [
        "AXIAL",
        "SHEAR",
        "MOMENTS",
        "ALL"
      ],
      "LIVE_LOAD_CASES": [
        "LL2"
      ],
      "REDUCTION_DATA": [
        {
          "STORY": "B2",
          "XMIN": -7.5,
          "XMAX": 1.15,
          "YMIN": -7.45,
          "YMAX": -7.45,
          "RANGE_MAX": 0.9,
          "RANGE_MIN": 0.6
        },
        {
          "STORY": "B2",
          "XMIN": -7.5,
          "XMAX": 1.15,
          "YMIN": -7.45,
          "YMAX": -7.45
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LLRF": {
    "1": {
      "CALC_RULE": 0,
      "APPLIED_COMP": [
        "AXIAL",
        "SHEAR",
        "MOMENTS",
        "ALL"
      ],
      "LIVE_LOAD_CASES": [
        "LL2"
      ],
      "REDUCTION_DATA": [
        {
          "STORY": "B2",
          "XMIN": -7.5,
          "XMAX": 1.15,
          "YMIN": -7.45,
          "YMAX": -7.45,
          "RANGE_MAX": 0.9,
          "RANGE_MIN": 0.6
        },
        {
          "STORY": "B2",
          "XMIN": -7.5,
          "XMAX": 1.15,
          "YMIN": -7.45,
          "YMAX": -7.45
        }
      ]
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/LLRF"

# 1) 설정 (PUT)
payload = {
  "Assign": {
    "1": {
      "CALC_RULE": 0,
      "APPLIED_COMP": [
        "AXIAL",
        "SHEAR",
        "MOMENTS",
        "ALL"
      ],
      "LIVE_LOAD_CASES": [
        "LL2"
      ],
      "REDUCTION_DATA": [
        {
          "STORY": "B2",
          "XMIN": -7.5,
          "XMAX": 1.15,
          "YMIN": -7.45,
          "YMAX": -7.45,
          "RANGE_MAX": 0.9,
          "RANGE_MIN": 0.6
        },
        {
          "STORY": "B2",
          "XMIN": -7.5,
          "XMAX": 1.15,
          "YMIN": -7.45,
          "YMAX": -7.45
        }
      ]
    }
  }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 조회 (GET)
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 삭제 (DELETE) — 필요 시
# requests.delete(URI, headers=HEADERS)
```

---

## 4. `DESIGN/STEEL/KDS-41-30-2022/LCTB` — Load Contribution for Nonlinear Load Case (비선형 하중케이스 하중기여)

> **기능:** 비선형 해석 하중케이스에 대한 하중 기여(Load Contribution) 정의를 조회/삭제합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/LCTB
```

### Active Methods

`GET` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "NAME",
            "BASE_ITEM"
          ],
          "additionalProperties": false,
          "properties": {
            "NAME": {
              "type": "string",
              "description": "Load Contribution Name"
            },
            "DESC": {
              "type": "string",
              "description": "Description",
              "default": ""
            },
            "BASE_ITEM": {
              "type": "array",
              "description": "Load Contribution Items",
              "items": {
                "type": "object",
                "required": [
                  "FACTOR",
                  "LOAD_CASE_NAME"
                ],
                "additionalProperties": false,
                "properties": {
                  "FACTOR": {
                    "type": "number",
                    "description": "Factor"
                  },
                  "LOAD_CASE_NAME": {
                    "type": "string",
                    "description": "Load Case Name"
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 하중기여 이름 | `"NAME"` | String | — | **필수** |
| 3 | 설명 | `"DESC"` | String | `""` | 선택 |
| 4 | 하중기여 항목 | `"BASE_ITEM"` | Array[Object] | — | **필수** |
| 4.1 | 계수 | `"FACTOR"` | Number | — | **필수** |
| 4.2 | 하중케이스 이름 | `"LOAD_CASE_NAME"` | String | — | **필수** |

### Request / Response JSON

**GET Response Body** (LCTB는 조회·삭제 전용)

```json
{
  "LCTB": {
    "2": {
      "NAME": "NgLCB6",
      "DESC": "",
      "BASE_ITEM": [
        {
          "FACTOR": 1.2,
          "LOAD_CASE_NAME": "DL"
        },
        {
          "FACTOR": 1.6,
          "LOAD_CASE_NAME": "LL"
        },
        {
          "FACTOR": 0.5,
          "LOAD_CASE_NAME": "SL"
        }
      ]
    },
    "3": {
      "NAME": "NgLCB7",
      "DESC": "",
      "BASE_ITEM": [
        {
          "FACTOR": 1.2,
          "LOAD_CASE_NAME": "DL"
        },
        {
          "FACTOR": 1.6,
          "LOAD_CASE_NAME": "SL"
        },
        {
          "FACTOR": 1,
          "LOAD_CASE_NAME": "LL"
        }
      ]
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/LCTB"

# LCTB는 GET / DELETE만 지원 (조회 및 삭제)
res = requests.get(URI, headers=HEADERS)
print("GET:", res.status_code, res.json())

# 전체 삭제
# requests.delete(URI, headers=HEADERS)
```

---

## 5. `DESIGN/STEEL/KDS-41-30-2022/SRDF` — Strength Reduction Factors (강도감소계수 φ)

> **기능:** 인장/압축/휨/전단에 대한 강도감소계수(φ) 값을 설정합니다. φ_t2(순단면 파단)는 0.75 고정(read-only)입니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/SRDF
```

### Active Methods

`GET` · `DELETE` · `PUT`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "description": "Strength Reduction Factors settings (shared structure: T_DSTL_D). Supported methods: GET, PUT. Checklist Text (view-only).",
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "PHI_T1": {
              "type": "number",
              "description": "For Yielding in Gross Section (phi_t1)",
              "default": 0.9
            },
            "PHI_T2": {
              "type": "number",
              "description": "For Fracture in Net Section (phi_t2) - read-only fixed value",
              "const": 0.75,
              "default": 0.75,
              "readOnly": true
            },
            "PHI_C": {
              "type": "number",
              "description": "For Compression Members (phi_c)",
              "default": 0.9
            },
            "PHI_B": {
              "type": "number",
              "description": "For Flexural Members (phi_b)",
              "default": 0.9
            },
            "PHI_V": {
              "type": "number",
              "description": "For Shear (phi_v)",
              "default": 0.9
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 (ID 1개만 허용, maxProperties=1) | `"Assign"` | Object | — | **필수** |
| 2 | 총단면 항복 (φ_t1) | `"PHI_T1"` | Number | `0.9` | 선택 |
| 3 | 순단면 파단 (φ_t2) — 0.75 고정 read-only | `"PHI_T2"` | Number (const 0.75) | `0.75` | 선택 |
| 4 | 압축부재 (φ_c) | `"PHI_C"` | Number | `0.9` | 선택 |
| 5 | 휨부재 (φ_b) | `"PHI_B"` | Number | `0.9` | 선택 |
| 6 | 전단 (φ_v) | `"PHI_V"` | Number | `0.9` | 선택 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "PHI_T1": 0.75,
      "PHI_T2": 0.75,
      "PHI_C": 0.25,
      "PHI_B": 0.45,
      "PHI_V": 0.85
    }
  }
}
```

**GET Response Body**

```json
{
  "SRDF": {
    "1": {
      "PHI_T1": 0.75,
      "PHI_T2": 0.75,
      "PHI_C": 0.25,
      "PHI_B": 0.45,
      "PHI_V": 0.85
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/SRDF"

# 1) 설정 (PUT)
payload = {
  "Assign": {
    "1": {
      "PHI_T1": 0.75,
      "PHI_T2": 0.75,
      "PHI_C": 0.25,
      "PHI_B": 0.45,
      "PHI_V": 0.85
    }
  }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 조회 (GET)
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 삭제 (DELETE) — 필요 시
# requests.delete(URI, headers=HEADERS)
```

---

## 6. `DESIGN/STEEL/KDS-41-30-2022/SERV` — Serviceability Parameters (사용성 파라미터)

> **기능:** 부재별 처짐 제어값(Deflection Control)과 처짐 증폭계수(DAF)를 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/SERV
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "DEFLECT_CONTROL": {
              "type": "number",
              "description": "Deflection Control",
              "default": 300
            },
            "DAF": {
              "type": "number",
              "description": "Deflection Amplification Factor",
              "default": 1
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 처짐 제어값 (span/n) | `"DEFLECT_CONTROL"` | Number | `300` | 선택 |
| 3 | 처짐 증폭계수 | `"DAF"` | Number | `1` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "DEFLECT_CONTROL": 400,
      "DAF": 2
    },
    "934": {
      "DAF": 2
    },
    "1057": {
      "DEFLECT_CONTROL": 500
    }
  }
}
```

**GET Response Body**

```json
{
  "SERV": {
    "915": {
      "DEFLECT_CONTROL": 400,
      "DAF": 2
    },
    "934": {
      "DAF": 2
    },
    "1057": {
      "DEFLECT_CONTROL": 500
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/SERV"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "915": {
      "DEFLECT_CONTROL": 400,
      "DAF": 2
    },
    "934": {
      "DAF": 2
    },
    "1057": {
      "DEFLECT_CONTROL": 500
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 7. `DESIGN/STEEL/KDS-41-30-2022/EQCT` — Seismic Load Combination Type (지진하중 조합 타입)

> **기능:** 부재별로 특별 지진하중(Special Seismic Loads) 또는 수직 지진력(Vertical Seismic Forces) 적용 타입을 배정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/EQCT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "TYPE": {
              "type": "string",
              "description": "Assign Member Type",
              "oneOf": [
                {
                  "title": "Special Seismic Loads",
                  "const": "Special Seismic Loads"
                },
                {
                  "title": "Vertical Seismic Forces",
                  "const": "Vertical Seismic Forces"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 부재 타입 (`"Special Seismic Loads"`, `"Vertical Seismic Forces"`) | `"TYPE"` | String (oneOf) | — | **필수** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1066": {
      "TYPE": "Special Seismic Loads"
    },
    "1068": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
```

**GET Response Body**

```json
{
  "EQCT": {
    "1066": {
      "TYPE": "Special Seismic Loads"
    },
    "1068": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/EQCT"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "1066": {
      "TYPE": "Special Seismic Loads"
    },
    "1068": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 8. `DESIGN/STEEL/KDS-41-30-2022/ULCT` — Underground Load Combination Type (지하 하중조합 타입)

> **기능:** 부재별로 지하 하중조합(Underground Loads) 적용 여부를 배정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/ULCT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "description": "Underground Load Combination settings. Checklist Text (view-only).",
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "bUNDERLOADTYPE": {
              "type": "boolean",
              "description": "Assign Member: true for Underground Loads, false for None-underground Loads",
              "oneOf": [
                {
                  "title": "For Underground Loads",
                  "const": true
                },
                {
                  "title": "For None-underground Loads",
                  "const": false
                }
              ],
              "default": false
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 지하 하중 타입 (`true`=지하 하중용, `false`=비지하 하중용) | `"bUNDERLOADTYPE"` | Boolean (oneOf) | `false` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "885": {
      "bUNDERLOADTYPE": true
    },
    "888": {
      "bUNDERLOADTYPE": false
    }
  }
}
```

**GET Response Body**

```json
{
  "ULCT": {
    "885": {
      "bUNDERLOADTYPE": true
    },
    "888": {
      "bUNDERLOADTYPE": false
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/ULCT"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "885": {
      "bUNDERLOADTYPE": true
    },
    "888": {
      "bUNDERLOADTYPE": false
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 9. `DESIGN/STEEL/KDS-41-30-2022/SUEQ` — Scale up Factor for Earthquake (지진 증폭계수)

> **기능:** 부재별로 하중케이스/하중조합의 축력·모멘트·전단 지진 증폭계수를 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/SUEQ
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "LC_AXIAL": {
              "type": "number",
              "description": "Load Case - Axial Scale Factor",
              "default": 1
            },
            "LC_MOMENT": {
              "type": "number",
              "description": "Load Case - Moment Scale Factor",
              "default": 1
            },
            "LC_SHEAR": {
              "type": "number",
              "description": "Load Case - Shear Scale Factor",
              "default": 1
            },
            "LCOM_AXIAL": {
              "type": "number",
              "description": "Load Combination - Axial Scale Factor",
              "default": 1
            },
            "LCOM_MOMENT": {
              "type": "number",
              "description": "Load Combination - Moment Scale Factor",
              "default": 1
            },
            "LCOM_SHEAR": {
              "type": "number",
              "description": "Load Combination - Shear Scale Factor",
              "default": 1
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 하중케이스 - 축력 증폭계수 | `"LC_AXIAL"` | Number | `1` | 선택 |
| 3 | 하중케이스 - 모멘트 증폭계수 | `"LC_MOMENT"` | Number | `1` | 선택 |
| 4 | 하중케이스 - 전단 증폭계수 | `"LC_SHEAR"` | Number | `1` | 선택 |
| 5 | 하중조합 - 축력 증폭계수 | `"LCOM_AXIAL"` | Number | `1` | 선택 |
| 6 | 하중조합 - 모멘트 증폭계수 | `"LCOM_MOMENT"` | Number | `1` | 선택 |
| 7 | 하중조합 - 전단 증폭계수 | `"LCOM_SHEAR"` | Number | `1` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "934": {
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    }
  }
}
```

**GET Response Body**

```json
{
  "SUEQ": {
    "915": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "934": {
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/SUEQ"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "915": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "934": {
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 10. `DESIGN/STEEL/KDS-41-30-2022/CRCM` — Combined Ratio Calculation Method for Circular Section (원형단면 조합비 계산법)

> **기능:** 원형(관형) 단면의 조합강도 계산 방법(SRSS / Linear Sum)을 부재별로 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CRCM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Combined Strength Method",
          "type": "object",
          "required": [
            "METHOD"
          ],
          "additionalProperties": false,
          "properties": {
            "METHOD": {
              "type": "string",
              "description": "Combined Strength Method",
              "oneOf": [
                {
                  "title": "SRSS",
                  "const": "SRSS"
                },
                {
                  "title": "Linear Sum",
                  "const": "Linear Sum"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 조합강도 방법 (`"SRSS"`, `"Linear Sum"`) | `"METHOD"` | String (oneOf) | — | **필수** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1058": {
      "METHOD": "Linear Sum"
    },
    "1059": {
      "METHOD": "SRSS"
    }
  }
}
```

**GET Response Body**

```json
{
  "CRCM": {
    "1058": {
      "METHOD": "Linear Sum"
    },
    "1059": {
      "METHOD": "SRSS"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CRCM"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "1058": {
      "METHOD": "Linear Sum"
    },
    "1059": {
      "METHOD": "SRSS"
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 11. `DESIGN/STEEL/KDS-41-30-2022/HCBM` — Haunched Beam Assignment (헌치 보 배정)

> **기능:** 요소를 Part A/B/C로 그룹화하여 헌치 보(Haunched Beam) 설계 부재를 정의합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/HCBM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "NAME",
            "PART_A",
            "PART_B",
            "PART_C",
            "POS_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "NAME": {
              "type": "string",
              "description": "Haunch Name"
            },
            "PART_A": {
              "type": "object",
              "description": "Element No. Input for Part A (Use only one method)",
              "additionalProperties": false,
              "required": [
                "INPUT_METHOD"
              ],
              "properties": {
                "INPUT_METHOD": {
                  "type": "string",
                  "description": "Select input method for Part A",
                  "oneOf": [
                    {
                      "title": "Specify each Element ID",
                      "const": "KEYS"
                    },
                    {
                      "title": "Specify ID range",
                      "const": "TO"
                    }
                  ]
                },
                "KEYS": {
                  "type": "array",
                  "items": {
                    "type": "integer"
                  },
                  "minItems": 1,
                  "description": "Specify each Element ID"
                },
                "TO": {
                  "type": "string",
                  "description": "Specify ID range (e.g. \"101 to 105\")"
                }
              }
            },
            "PART_B": {
              "type": "object",
              "description": "Element No. Input for Part B (Use only one method)",
              "additionalProperties": false,
              "required": [
                "INPUT_METHOD"
              ],
              "properties": {
                "INPUT_METHOD": {
                  "type": "string",
                  "description": "Select input method for Part B",
                  "oneOf": [
                    {
                      "title": "Specify each Element ID",
                      "const": "KEYS"
                    },
                    {
                      "title": "Specify ID range",
                      "const": "TO"
                    }
                  ]
                },
                "KEYS": {
                  "type": "array",
                  "items": {
                    "type": "integer"
                  },
                  "minItems": 1,
                  "description": "Specify each Element ID"
                },
                "TO": {
                  "type": "string",
                  "description": "Specify ID range (e.g. \"101 to 105\")"
                }
              }
            },
            "PART_C": {
              "type": "object",
              "description": "Element No. Input for Part C (Use only one method)",
              "additionalProperties": false,
              "required": [
                "INPUT_METHOD"
              ],
              "properties": {
                "INPUT_METHOD": {
                  "type": "string",
                  "description": "Select input method for Part C",
                  "oneOf": [
                    {
                      "title": "Specify each Element ID",
                      "const": "KEYS"
                    },
                    {
                      "title": "Specify ID range",
                      "const": "TO"
                    }
                  ]
                },
                "KEYS": {
                  "type": "array",
                  "items": {
                    "type": "integer"
                  },
                  "minItems": 1,
                  "description": "Specify each Element ID"
                },
                "TO": {
                  "type": "string",
                  "description": "Specify ID range (e.g. \"101 to 105\")"
                }
              }
            },
            "POS_TYPE": {
              "type": "integer",
              "description": "Design Position Type",
              "oneOf": [
                {
                  "title": "Part 1/2",
                  "const": 0
                },
                {
                  "title": "User",
                  "const": 1
                }
              ]
            },
            "L1": {
              "type": "number",
              "description": "User defined L1 distance",
              "default": 1
            },
            "L2": {
              "type": "number",
              "description": "User defined L2 distance",
              "default": 1
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 헌치 이름 | `"NAME"` | String | — | **필수** |
| 3 | Part A 요소 입력 (방법 1개만 사용) | `"PART_A"` | Object | — | **필수** |
| 3.1 | 입력 방법 (`"KEYS"`=개별 ID, `"TO"`=범위) | `"INPUT_METHOD"` | String (oneOf) | — | **필수** |
| 3.2 | 개별 요소 ID (INPUT_METHOD=KEYS, minItems 1) | `"KEYS"` | Array[Integer] | — | 조건부 |
| 3.3 | ID 범위 문자열 (INPUT_METHOD=TO, 예 `"101 to 105"`) | `"TO"` | String | — | 조건부 |
| 4 | Part B 요소 입력 (구조는 PART_A와 동일) | `"PART_B"` | Object | — | **필수** |
| 5 | Part C 요소 입력 (구조는 PART_A와 동일) | `"PART_C"` | Object | — | **필수** |
| 6 | 설계 위치 타입 (0=Part 1/2, 1=User) | `"POS_TYPE"` | Integer (oneOf) | — | **필수** |
| 7 | 사용자 정의 L1 거리 (POS_TYPE=1) | `"L1"` | Number | `1` | 선택 |
| 8 | 사용자 정의 L2 거리 (POS_TYPE=1) | `"L2"` | Number | `1` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NAME": "h1",
      "POS_TYPE": 0,
      "L1": 0.5,
      "L2": 0.5,
      "PART_A": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1065
        ]
      },
      "PART_B": {
        "INPUT_METHOD": "TO",
        "TO": "1066to1071"
      },
      "PART_C": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1072
        ]
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "HCBM": {
    "1": {
      "NAME": "h1",
      "PART_A": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1065
        ]
      },
      "PART_B": {
        "INPUT_METHOD": "TO",
        "TO": "1066to1071"
      },
      "PART_C": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1072
        ]
      },
      "POS_TYPE": 0,
      "L1": 0.5,
      "L2": 0.5
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/HCBM"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "1": {
      "NAME": "h1",
      "POS_TYPE": 0,
      "L1": 0.5,
      "L2": 0.5,
      "PART_A": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1065
        ]
      },
      "PART_B": {
        "INPUT_METHOD": "TO",
        "TO": "1066to1071"
      },
      "PART_C": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1072
        ]
      }
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 12. `DESIGN/STEEL/KDS-41-30-2022/LENG` — Unbraced Length (비지지 길이 L, Lb)

> **기능:** 부재별 비지지 길이(Ly, Lz), 횡비지지 길이(Lb), 비틀림 비지지 길이(Lt)를 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/LENG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "LY": {
              "type": "number",
              "description": "Unbraced Length Ly",
              "default": 0
            },
            "LZ": {
              "type": "number",
              "description": "Unbraced Length Lz",
              "default": 0
            },
            "LB": {
              "type": "number",
              "description": "Laterally Unbraced Length",
              "default": 0
            },
            "bNOTUSE": {
              "type": "boolean",
              "description": "Do not consider of laterally unbraced length",
              "default": false
            },
            "LT": {
              "type": "number",
              "description": "Torsional Unbraced Length",
              "default": 0
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 비지지 길이 Ly | `"LY"` | Number | `0` | 선택 |
| 3 | 비지지 길이 Lz | `"LZ"` | Number | `0` | 선택 |
| 4 | 횡비지지 길이 Lb | `"LB"` | Number | `0` | 선택 |
| 5 | 횡비지지 길이 미고려 | `"bNOTUSE"` | Boolean | `false` | 선택 |
| 6 | 비틀림 비지지 길이 Lt | `"LT"` | Number | `0` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "888": {
      "LY": 1,
      "LZ": 1,
      "LB": 1,
      "bNOTUSE": true,
      "LT": 1
    },
    "891": {
      "LY": 1,
      "LZ": 1,
      "LB": 2
    }
  }
}
```

**GET Response Body**

```json
{
  "LENG": {
    "888": {
      "LY": 1,
      "LZ": 1,
      "LB": 1,
      "bNOTUSE": true,
      "LT": 1
    },
    "891": {
      "LY": 1,
      "LZ": 1,
      "LB": 2
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/LENG"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "888": {
      "LY": 1,
      "LZ": 1,
      "LB": 1,
      "bNOTUSE": true,
      "LT": 1
    },
    "891": {
      "LY": 1,
      "LZ": 1,
      "LB": 2
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 13. `DESIGN/STEEL/KDS-41-30-2022/KFAC` — Effective Length Factor (유효좌굴길이계수 K)

> **기능:** 부재별 유효좌굴길이계수 Ky, Kz, Kt를 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/KFAC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "Ky": {
              "type": "number",
              "description": "Ky",
              "default": 1
            },
            "Kz": {
              "type": "number",
              "description": "Kz",
              "default": 1
            },
            "Kt": {
              "type": "number",
              "description": "Kt",
              "default": 1
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 유효좌굴길이계수 Ky | `"Ky"` | Number | `1` | 선택 |
| 3 | 유효좌굴길이계수 Kz | `"Kz"` | Number | `1` | 선택 |
| 4 | 유효좌굴길이계수 Kt | `"Kt"` | Number | `1` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "859": {
      "Ky": 1
    },
    "860": {
      "Ky": 2,
      "Kz": 2
    },
    "902": {
      "Kz": 3,
      "Kt": 3
    }
  }
}
```

**GET Response Body**

```json
{
  "KFAC": {
    "859": {
      "Ky": 1
    },
    "860": {
      "Ky": 2,
      "Kz": 2
    },
    "902": {
      "Kz": 3,
      "Kt": 3
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/KFAC"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "859": {
      "Ky": 1
    },
    "860": {
      "Ky": 2,
      "Kz": 2
    },
    "902": {
      "Kz": 3,
      "Kt": 3
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 14. `DESIGN/STEEL/KDS-41-30-2022/LTSR` — Limiting Slenderness Ratio (세장비 제한)

> **기능:** 부재별 압축/인장 세장비 제한값을 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/LTSR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "COMP",
            "TENS"
          ],
          "additionalProperties": false,
          "properties": {
            "bNOTCHECK": {
              "type": "boolean",
              "description": "Do not check for Slenderness Ratio",
              "default": false
            },
            "COMP": {
              "type": "number",
              "description": "Limiting Slenderness Ratio for Compression"
            },
            "TENS": {
              "type": "number",
              "description": "Limiting Slenderness Ratio for Tension"
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 세장비 검토 안함 | `"bNOTCHECK"` | Boolean | `false` | 선택 |
| 3 | 압축 세장비 제한 | `"COMP"` | Number | — | **필수** |
| 4 | 인장 세장비 제한 | `"TENS"` | Number | — | **필수** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1067": {
      "COMP": 300,
      "TENS": 200
    },
    "1068": {
      "COMP": 300,
      "TENS": 200
    }
  }
}
```

**GET Response Body**

```json
{
  "LTSR": {
    "1067": {
      "COMP": 300,
      "TENS": 200
    },
    "1068": {
      "COMP": 300,
      "TENS": 200
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/LTSR"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "1067": {
      "COMP": 300,
      "TENS": 200
    },
    "1068": {
      "COMP": 300,
      "TENS": 200
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 15. `DESIGN/STEEL/KDS-41-30-2022/CMFT` — Equivalent Moment Correction Factor (등가모멘트 보정계수 Cm)

> **기능:** 부재별 등가모멘트 보정계수 CMy, CMz를 자동계산 또는 사용자값으로 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CMFT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "OPT_AUTO": {
              "type": "boolean",
              "description": "Auto Calculate",
              "default": false
            },
            "CMY": {
              "type": "number",
              "description": "CMy",
              "default": 0
            },
            "CMZ": {
              "type": "number",
              "description": "CMz",
              "default": 0
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 자동계산 | `"OPT_AUTO"` | Boolean | `false` | 선택 |
| 3 | CMy | `"CMY"` | Number | `0` | 선택 |
| 4 | CMz | `"CMZ"` | Number | `0` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1067": {
      "OPT_AUTO": true
    },
    "1069": {
      "CMY": 0.7,
      "CMZ": 0.6
    },
    "1070": {
      "CMY": 0.72,
      "CMZ": 0.85
    }
  }
}
```

**GET Response Body**

```json
{
  "CMFT": {
    "1067": {
      "OPT_AUTO": true
    },
    "1069": {
      "CMY": 0.7,
      "CMZ": 0.6
    },
    "1070": {
      "CMY": 0.72,
      "CMZ": 0.85
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CMFT"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "1067": {
      "OPT_AUTO": true
    },
    "1069": {
      "CMY": 0.7,
      "CMZ": 0.6
    },
    "1070": {
      "CMY": 0.72,
      "CMZ": 0.85
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 16. `DESIGN/STEEL/KDS-41-30-2022/FMAG` — Moment Magnifier (모멘트 증폭계수 B1/Δb, B2/Δs)

> **기능:** 부재별 1차/2차 모멘트 증폭계수(B1y·B1z, B2y·B2z)를 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/FMAG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "B1Y_DELTA_BY": {
              "type": "number",
              "description": "B1y - Delta by (First Order Moment Y)",
              "default": 1
            },
            "B1Z_DELTA_BZ": {
              "type": "number",
              "description": "B1z - Delta bz (First Order Moment Z)",
              "default": 1
            },
            "B2Y_DELTA_SY": {
              "type": "number",
              "description": "B2y - Delta sy (Second Order Moment Y)",
              "default": 1
            },
            "B2Z_DELTA_SZ": {
              "type": "number",
              "description": "B2z - Delta sz (Second Order Moment Z)",
              "default": 1
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | B1y - Δby (1차 모멘트 Y) | `"B1Y_DELTA_BY"` | Number | `1` | 선택 |
| 3 | B1z - Δbz (1차 모멘트 Z) | `"B1Z_DELTA_BZ"` | Number | `1` | 선택 |
| 4 | B2y - Δsy (2차 모멘트 Y) | `"B2Y_DELTA_SY"` | Number | `1` | 선택 |
| 5 | B2z - Δsz (2차 모멘트 Z) | `"B2Z_DELTA_SZ"` | Number | `1` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2
    },
    "1058": {
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    }
  }
}
```

**GET Response Body**

```json
{
  "FMAG": {
    "915": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1,
      "B2Z_DELTA_SZ": 1
    },
    "1058": {
      "B1Y_DELTA_BY": 1,
      "B1Z_DELTA_BZ": 1,
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/FMAG"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "915": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2
    },
    "1058": {
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 17. `DESIGN/STEEL/KDS-41-30-2022/CBFT` — Bending Coefficient (휨계수 Cb)

> **기능:** 부재별 횡좌굴 휨계수 Cb를 자동계산 또는 사용자값으로 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CBFT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "AUTO_CAL": {
              "type": "boolean",
              "description": "Auto Calculate by Program",
              "default": false
            },
            "VALUE": {
              "type": "number",
              "description": "Bending Coefficient (Cb) Value",
              "default": 1
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 프로그램 자동계산 | `"AUTO_CAL"` | Boolean | `false` | 선택 |
| 3 | 휨계수 Cb 값 (AUTO_CAL=false일 때) | `"VALUE"` | Number | `1` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "AUTO_CAL": true
    },
    "1058": {
      "AUTO_CAL": false,
      "VALUE": 1.2
    },
    "1059": {
      "AUTO_CAL": false,
      "VALUE": 1.25
    }
  }
}
```

**GET Response Body**

```json
{
  "CBFT": {
    "915": {
      "AUTO_CAL": true
    },
    "1058": {
      "AUTO_CAL": false,
      "VALUE": 1.2
    },
    "1059": {
      "AUTO_CAL": false,
      "VALUE": 1.25
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CBFT"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "915": {
      "AUTO_CAL": true
    },
    "1058": {
      "AUTO_CAL": false,
      "VALUE": 1.2
    },
    "1059": {
      "AUTO_CAL": false,
      "VALUE": 1.25
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 18. `DESIGN/STEEL/KDS-41-30-2022/MBTP` — Modify Member Type (부재 타입 수정)

> **기능:** 요소의 설계 부재 타입(Column/Beam/Brace)을 변경합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/MBTP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "TYPE": {
              "type": "string",
              "description": "Member Type",
              "oneOf": [
                {
                  "title": "Column",
                  "const": "COLUMN"
                },
                {
                  "title": "Beam",
                  "const": "BEAM"
                },
                {
                  "title": "Brace",
                  "const": "BRACE"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 부재 타입 (`"COLUMN"`, `"BEAM"`, `"BRACE"`) | `"TYPE"` | String (oneOf) | — | **필수** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "934": {
      "TYPE": "BRACE"
    },
    "1058": {
      "TYPE": "COLUMN"
    },
    "1066": {
      "TYPE": "BEAM"
    }
  }
}
```

**GET Response Body**

```json
{
  "MBTP": {
    "934": {
      "TYPE": "BRACE"
    },
    "1058": {
      "TYPE": "COLUMN"
    },
    "1066": {
      "TYPE": "BEAM"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/MBTP"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "934": {
      "TYPE": "BRACE"
    },
    "1058": {
      "TYPE": "COLUMN"
    },
    "1066": {
      "TYPE": "BEAM"
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 19. `DESIGN/STEEL/KDS-41-30-2022/SLRS` — Seismic Load Resisting System by Member (부재별 내진 저항시스템)

> **기능:** 부재별 내진 저항 골조 타입(가새골조/편심가새/좌굴방지가새/특수전단벽)과 검토 옵션을 설정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/SLRS
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "FRAME_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "FRAME_TYPE": {
              "type": "string",
              "description": "Seismic Load Resisting System Frame Type",
              "oneOf": [
                {
                  "title": "Special Concentrically Braced Frames",
                  "const": "Special Concentrically Braced Frames"
                },
                {
                  "title": "Ordinary Concentrically Braced Frames",
                  "const": "Ordinary Concentrically Braced Frames"
                },
                {
                  "title": "Eccentrically Braced Frames",
                  "const": "Eccentrically Braced Frames"
                },
                {
                  "title": "Buckling Restrained Braced Frames",
                  "const": "Buckling Restrained Braced Frames"
                },
                {
                  "title": "Special Plate Shear Walls",
                  "const": "Special Plate Shear Walls"
                }
              ]
            },
            "CHECK_OPTION": {
              "type": "boolean",
              "description": "Check for Brace Slenderness Ratio / Check for Links (not supported for Buckling-Restrained Braced Frames and Special Plate Shear Walls)",
              "default": true
            }
          },
          "allOf": [
            {
              "if": {
                "properties": {
                  "FRAME_TYPE": {
                    "enum": [
                      "Buckling Restrained Braced Frames",
                      "Special Plate Shear Walls"
                    ]
                  }
                },
                "required": [
                  "FRAME_TYPE"
                ]
              },
              "then": {
                "properties": {
                  "CHECK_OPTION": {
                    "const": false
                  }
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 내진 저항시스템 골조 타입 (`"Special Concentrically Braced Frames"`, `"Ordinary Concentrically Braced Frames"`, `"Eccentrically Braced Frames"`, `"Buckling Restrained Braced Frames"`, `"Special Plate Shear Walls"`) | `"FRAME_TYPE"` | String (oneOf) | — | **필수** |
| 3 | 가새 세장비 검토 / 링크 검토 (Buckling Restrained·Special Plate Shear Walls는 미지원 → false 강제) | `"CHECK_OPTION"` | Boolean | `true` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "FRAME_TYPE": "Special Concentrically Braced Frames",
      "CHECK_OPTION": true
    },
    "934": {
      "FRAME_TYPE": "Ordinary Concentrically Braced Frames",
      "CHECK_OPTION": false
    },
    "1058": {
      "FRAME_TYPE": "Buckling Restrained Braced Frames"
    }
  }
}
```

**GET Response Body**

```json
{
  "SLRS": {
    "915": {
      "FRAME_TYPE": "Special Concentrically Braced Frames",
      "CHECK_OPTION": true
    },
    "934": {
      "FRAME_TYPE": "Ordinary Concentrically Braced Frames",
      "CHECK_OPTION": false
    },
    "1058": {
      "FRAME_TYPE": "Buckling Restrained Braced Frames"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/SLRS"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "915": {
      "FRAME_TYPE": "Special Concentrically Braced Frames",
      "CHECK_OPTION": true
    },
    "934": {
      "FRAME_TYPE": "Ordinary Concentrically Braced Frames",
      "CHECK_OPTION": false
    },
    "1058": {
      "FRAME_TYPE": "Buckling Restrained Braced Frames"
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 20. `DESIGN/STEEL/KDS-41-30-2022/MLLR` — Modify Live Load Reduction Factor (활하중 저감계수 수정)

> **기능:** 부재별 활하중 저감계수(0.3~1.0)와 적용 성분(축력/모멘트/전단)을 개별 수정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/MLLR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "FACTOR": {
              "type": "number",
              "description": "Reduction Factor",
              "default": 1,
              "minimum": 0.3,
              "maximum": 1
            },
            "COMPONENTS": {
              "type": "object",
              "description": "Applied Components",
              "additionalProperties": false,
              "properties": {
                "AXIAL": {
                  "type": "boolean",
                  "description": "Axial Force",
                  "default": false
                },
                "MOMENT": {
                  "type": "boolean",
                  "description": "Moments",
                  "default": false
                },
                "SHEAR": {
                  "type": "boolean",
                  "description": "Shear Forces",
                  "default": false
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 저감계수 (범위 0.3 ~ 1.0) | `"FACTOR"` | Number | `1` | 선택 |
| 3 | 적용 성분 | `"COMPONENTS"` | Object | — | 선택 |
| 3.1 | 축력 | `"AXIAL"` | Boolean | `false` | 선택 |
| 3.2 | 모멘트 | `"MOMENT"` | Boolean | `false` | 선택 |
| 3.3 | 전단력 | `"SHEAR"` | Boolean | `false` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "922": {
      "COMPONENTS": {
        "AXIAL": false,
        "MOMENT": true,
        "SHEAR": false
      }
    },
    "934": {
      "FACTOR": 0.9,
      "COMPONENTS": {
        "AXIAL": true,
        "SHEAR": false
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "MLLR": {
    "922": {
      "COMPONENTS": {
        "AXIAL": false,
        "MOMENT": true,
        "SHEAR": false
      }
    },
    "934": {
      "FACTOR": 0.9,
      "COMPONENTS": {
        "AXIAL": true,
        "SHEAR": false
      }
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/MLLR"

# 1) 생성/설정 (POST)
payload = {
  "Assign": {
    "922": {
      "COMPONENTS": {
        "AXIAL": false,
        "MOMENT": true,
        "SHEAR": false
      }
    },
    "934": {
      "FACTOR": 0.9,
      "COMPONENTS": {
        "AXIAL": true,
        "SHEAR": false
      }
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 조회 (GET) / 수정 (PUT) / 삭제 (DELETE)
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 21. `DESIGN/STEEL/KDS-41-30-2022/MEMB` — Member Assignment (설계 부재 배정)

> **기능:** 설계 부재 ID에 요소 리스트를 배정하고 로컬 방향 반전 여부를 지정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/MEMB
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "AELEM"
          ],
          "additionalProperties": false,
          "properties": {
            "AELEM": {
              "type": "array",
              "description": "Element Lists",
              "items": {
                "type": "integer"
              }
            },
            "bREVERSE": {
              "type": "boolean",
              "description": "Reverse Local Direction",
              "default": false
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 | `"Assign"` | Object | — | **필수** |
| 2 | 요소 리스트 | `"AELEM"` | Array[Integer] | — | **필수** |
| 3 | 로컬 방향 반전 | `"bREVERSE"` | Boolean | `false` | 선택 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "AELEM": [
        933,
        934
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        906,
        891
      ],
      "bREVERSE": true
    }
  }
}
```

**GET Response Body**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [
        933,
        934
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        906,
        891
      ],
      "bREVERSE": true
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/MEMB"

# 1) 설정 (PUT)
payload = {
  "Assign": {
    "1": {
      "AELEM": [
        933,
        934
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        906,
        891
      ],
      "bREVERSE": true
    }
  }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 조회 (GET)
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 삭제 (DELETE) — 필요 시
# requests.delete(URI, headers=HEADERS)
```

---

## 22. `DESIGN/STEEL/KDS-41-30-2022/SMODI` — Modify Steel Material (강재 재질 수정)

> **기능:** 재질 ID별로 강재 재질을 표준코드(KS22(S)) 기반 또는 사용자정의(None)로 수정합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/SMODI
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is a material ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "CODE"
          ],
          "additionalProperties": false,
          "properties": {
            "CODE": {
              "type": "string",
              "description": "Steel material code type.",
              "oneOf": [
                {
                  "const": "None",
                  "title": "None"
                },
                {
                  "const": "Standard",
                  "title": "Standard"
                }
              ]
            },
            "STANDARD_CODE": {
              "type": "string",
              "description": "Steel standard code when CODE is Standard. Currently only KS22(S) is supported.",
              "oneOf": [
                {
                  "const": "KS22(S)",
                  "title": "KS22(S)"
                }
              ]
            },
            "GRADE": {
              "type": "string",
              "description": "Steel grade when CODE is Standard.",
              "oneOf": [
                {
                  "const": "SS235",
                  "title": "SS235"
                },
                {
                  "const": "SS275",
                  "title": "SS275"
                },
                {
                  "const": "SS315",
                  "title": "SS315"
                },
                {
                  "const": "SS410",
                  "title": "SS410"
                },
                {
                  "const": "SS450",
                  "title": "SS450"
                },
                {
                  "const": "SS550",
                  "title": "SS550"
                },
                {
                  "const": "SM275",
                  "title": "SM275"
                },
                {
                  "const": "SM355",
                  "title": "SM355"
                },
                {
                  "const": "SM420",
                  "title": "SM420"
                },
                {
                  "const": "SM460",
                  "title": "SM460"
                },
                {
                  "const": "SM275TMC",
                  "title": "SM275TMC"
                },
                {
                  "const": "SM355TMC",
                  "title": "SM355TMC"
                },
                {
                  "const": "SM420TMC",
                  "title": "SM420TMC"
                },
                {
                  "const": "SM460TMC",
                  "title": "SM460TMC"
                },
                {
                  "const": "SMA275A",
                  "title": "SMA275A"
                },
                {
                  "const": "SMA275B",
                  "title": "SMA275B"
                },
                {
                  "const": "SMA275C",
                  "title": "SMA275C"
                },
                {
                  "const": "SMA355A",
                  "title": "SMA355A"
                },
                {
                  "const": "SMA355B",
                  "title": "SMA355B"
                },
                {
                  "const": "SMA355C",
                  "title": "SMA355C"
                },
                {
                  "const": "SMA460",
                  "title": "SMA460"
                },
                {
                  "const": "HSM500",
                  "title": "HSM500"
                },
                {
                  "const": "SN275A",
                  "title": "SN275A"
                },
                {
                  "const": "SN275B",
                  "title": "SN275B"
                },
                {
                  "const": "SN275C",
                  "title": "SN275C"
                },
                {
                  "const": "SN355",
                  "title": "SN355"
                },
                {
                  "const": "SN460",
                  "title": "SN460"
                },
                {
                  "const": "SHN275",
                  "title": "SHN275"
                },
                {
                  "const": "SHN355",
                  "title": "SHN355"
                },
                {
                  "const": "SHN420",
                  "title": "SHN420"
                },
                {
                  "const": "SHN460",
                  "title": "SHN460"
                },
                {
                  "const": "HSB380",
                  "title": "HSB380"
                },
                {
                  "const": "HSB460",
                  "title": "HSB460"
                },
                {
                  "const": "HSB690",
                  "title": "HSB690"
                },
                {
                  "const": "HSA650",
                  "title": "HSA650"
                },
                {
                  "const": "SGT275",
                  "title": "SGT275"
                },
                {
                  "const": "SGT355",
                  "title": "SGT355"
                },
                {
                  "const": "SGT410",
                  "title": "SGT410"
                },
                {
                  "const": "SGT450",
                  "title": "SGT450"
                },
                {
                  "const": "SGT550",
                  "title": "SGT550"
                },
                {
                  "const": "SRT275",
                  "title": "SRT275"
                },
                {
                  "const": "SRT355",
                  "title": "SRT355"
                },
                {
                  "const": "SRT410",
                  "title": "SRT410"
                },
                {
                  "const": "SRT450",
                  "title": "SRT450"
                },
                {
                  "const": "SRT550",
                  "title": "SRT550"
                },
                {
                  "const": "SNT275",
                  "title": "SNT275"
                },
                {
                  "const": "SNT355",
                  "title": "SNT355"
                },
                {
                  "const": "SNT460",
                  "title": "SNT460"
                },
                {
                  "const": "SHT410",
                  "title": "SHT410"
                },
                {
                  "const": "SHT460",
                  "title": "SHT460"
                },
                {
                  "const": "SNRT295E",
                  "title": "SNRT295E"
                },
                {
                  "const": "SNRT390E",
                  "title": "SNRT390E"
                },
                {
                  "const": "SNRT275A",
                  "title": "SNRT275A"
                },
                {
                  "const": "SNRT355A",
                  "title": "SNRT355A"
                },
                {
                  "const": "SSC275",
                  "title": "SSC275"
                },
                {
                  "const": "SWH275",
                  "title": "SWH275"
                },
                {
                  "const": "SWH355",
                  "title": "SWH355"
                },
                {
                  "const": "SWH420",
                  "title": "SWH420"
                },
                {
                  "const": "SWH460",
                  "title": "SWH460"
                },
                {
                  "const": "SF490",
                  "title": "SF490"
                },
                {
                  "const": "SF540",
                  "title": "SF540"
                },
                {
                  "const": "SDP1",
                  "title": "SDP1"
                },
                {
                  "const": "SDP2",
                  "title": "SDP2"
                },
                {
                  "const": "SDP3",
                  "title": "SDP3"
                },
                {
                  "const": "SWPC1",
                  "title": "SWPC1"
                },
                {
                  "const": "SWPD1",
                  "title": "SWPD1"
                },
                {
                  "const": "SWPC",
                  "title": "SWPC"
                },
                {
                  "const": "SWPD",
                  "title": "SWPD"
                }
              ]
            },
            "NAME": {
              "type": "string",
              "description": "User-defined steel material name when CODE is None."
            },
            "ES": {
              "type": "number",
              "description": "Modulus of Elasticity (Es). When CODE is None, user input is required. When CODE is Standard, this value is auto-filled from the selected standard code and grade and should be treated as read-only in UI."
            },
            "PS": {
              "type": "number",
              "description": "Poisson's Ratio (Ps). When CODE is None, user input is required. When CODE is Standard, this value is auto-filled from the selected standard code and grade and should be treated as read-only in UI."
            },
            "FU": {
              "type": "number",
              "description": "Tensile Strength (Fu). When CODE is None, user input is required. When CODE is Standard, this value is auto-filled from the selected standard code and grade and should be treated as read-only in UI."
            },
            "FY": {
              "type": "number",
              "description": "Yield Strength (Fy) for CODE=None. Required when CODE is None."
            },
            "FY1": {
              "type": "number",
              "description": "Yield Strength (Fy1). Auto-filled from the selected standard code and grade when CODE is Standard."
            },
            "FY2": {
              "type": "number",
              "description": "Yield Strength (Fy2). Auto-filled from the selected standard code and grade when CODE is Standard."
            },
            "FY3": {
              "type": "number",
              "description": "Yield Strength (Fy3). Auto-filled from the selected standard code and grade when CODE is Standard."
            },
            "FY4": {
              "type": "number",
              "description": "Yield Strength (Fy4). Auto-filled from the selected standard code and grade when CODE is Standard."
            },
            "FY5": {
              "type": "number",
              "description": "Yield Strength (Fy5). Auto-filled from the selected standard code and grade when CODE is Standard."
            }
          },
          "allOf": [
            {
              "if": {
                "properties": {
                  "CODE": {
                    "const": "None"
                  }
                },
                "required": [
                  "CODE"
                ]
              },
              "then": {
                "required": [
                  "NAME",
                  "ES",
                  "PS",
                  "FU"
                ]
              }
            },
            {
              "if": {
                "properties": {
                  "CODE": {
                    "const": "Standard"
                  }
                },
                "required": [
                  "CODE"
                ]
              },
              "then": {
                "required": [
                  "STANDARD_CODE",
                  "GRADE"
                ]
              }
            }
          ]
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 (재질 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 재질 코드 타입 (`"None"`=사용자정의, `"Standard"`=표준코드) | `"CODE"` | String (oneOf) | — | **필수** |
| 3 | 표준 코드 (CODE=Standard, 현재 `"KS22(S)"`만 지원) | `"STANDARD_CODE"` | String (oneOf) | — | 조건부 필수 |
| 4 | 강종 Grade (CODE=Standard) — SS235/SS275/…/SM355/…/SN460/SHN460/HSB690/HSA650/… 등 KS22(S) 68종 | `"GRADE"` | String (oneOf) | — | 조건부 필수 |
| 5 | 사용자 정의 재질명 (CODE=None) | `"NAME"` | String | — | 조건부 필수 |
| 6 | 항복강도 Fy (CODE=None) | `"FY"` | Number | — | 조건부 필수 |
| 7 | 탄성계수 Es (CODE=None 입력 / Standard 자동채움) | `"ES"` | Number | — | 조건부 필수 |
| 8 | 포아송비 Ps (CODE=None 입력 / Standard 자동채움) | `"PS"` | Number | — | 조건부 필수 |
| 9 | 인장강도 Fu (CODE=None 입력 / Standard 자동채움) | `"FU"` | Number | — | 조건부 필수 |
| 10 | 항복강도 Fy1 (CODE=Standard 자동채움) | `"FY1"` | Number | — | 선택 |
| 11 | 항복강도 Fy2 (CODE=Standard 자동채움) | `"FY2"` | Number | — | 선택 |
| 12 | 항복강도 Fy3 (CODE=Standard 자동채움) | `"FY3"` | Number | — | 선택 |
| 13 | 항복강도 Fy4 (CODE=Standard 자동채움) | `"FY4"` | Number | — | 선택 |
| 14 | 항복강도 Fy5 (CODE=Standard 자동채움) | `"FY5"` | Number | — | 선택 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "100": {
      "CODE": "Standard",
      "STANDARD_CODE": "KS22(S)",
      "GRADE": "SM355"
    },
    "101": {
      "CODE": "None",
      "ES": 40000000,
      "PS": 0,
      "FU": 0,
      "NAME": "test",
      "FY": 0
    }
  }
}
```

**GET Response Body**

```json
{
  "SMODI": {
    "100": {
      "CODE": "Standard",
      "STANDARD_CODE": "KS22(S)",
      "GRADE": "SM355"
    },
    "101": {
      "CODE": "None",
      "ES": 40000000,
      "PS": 0,
      "FU": 0,
      "NAME": "test",
      "FY": 0
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/SMODI"

# 1) 설정 (PUT)
payload = {
  "Assign": {
    "100": {
      "CODE": "Standard",
      "STANDARD_CODE": "KS22(S)",
      "GRADE": "SM355"
    },
    "101": {
      "CODE": "None",
      "ES": 40000000,
      "PS": 0,
      "FU": 0,
      "NAME": "test",
      "FY": 0
    }
  }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 조회 (GET)
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 삭제 (DELETE) — 필요 시
# requests.delete(URI, headers=HEADERS)
```

---

## 23. `DESIGN/STEEL/KDS-41-30-2022/CODE-ANAL` — Steel Code Check Perform (강재 코드 검토 수행)

> **기능:** 전체/요소별/단면별 대상에 대해 강재 코드 검토(설계 계산)를 실행합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CODE-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "ELEMS"
          ]
        },
        {
          "required": [
            "SECTIONS"
          ]
        }
      ],
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for design calculation.",
          "oneOf": [
            {
              "title": "All Elements",
              "const": "ALL"
            },
            {
              "title": "By Element No.",
              "const": "ELEMS"
            },
            {
              "title": "By Section No.",
              "const": "SECTIONS"
            }
          ],
          "default": "ALL"
        },
        "ELEMS": {
          "type": "object",
          "description": "Element No. Input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to160')"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify Structure Group Name"
            }
          },
          "oneOf": [
            {
              "required": [
                "KEYS"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "TO"
                    ]
                  },
                  {
                    "required": [
                      "STRUCTURE_GROUP_NAME"
                    ]
                  }
                ]
              }
            },
            {
              "required": [
                "TO"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "KEYS"
                    ]
                  },
                  {
                    "required": [
                      "STRUCTURE_GROUP_NAME"
                    ]
                  }
                ]
              }
            },
            {
              "required": [
                "STRUCTURE_GROUP_NAME"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "KEYS"
                    ]
                  },
                  {
                    "required": [
                      "TO"
                    ]
                  }
                ]
              }
            }
          ]
        },
        "SECTIONS": {
          "type": "array",
          "description": "Section No. Input.",
          "items": {
            "type": "integer"
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 수행 대상 타입 (`"ALL"`=전체 요소, `"ELEMS"`=요소별, `"SECTIONS"`=단면별) | `"PERFORM_TYPE"` | String (oneOf) | `"ALL"` | 선택 |
| 3 | 요소 입력 (ELEMS/SECTIONS 중 하나) | `"ELEMS"` | Object | — | 조건부 |
| 3.1 | 개별 ID | `"KEYS"` | Array[Integer] | — | 선택 |
| 3.2 | ID 범위 (예 `"1to160"`) | `"TO"` | String | — | 선택 |
| 3.3 | 구조 그룹 이름 | `"STRUCTURE_GROUP_NAME"` | String | — | 선택 |
| 4 | 단면 번호 (ELEMS/SECTIONS 중 하나) | `"SECTIONS"` | Array[Integer] | — | 조건부 |

> `Argument`는 `"ELEMS"` 또는 `"SECTIONS"` 중 **정확히 하나**만 포함해야 하며(oneOf), `ELEMS` 내부에서는 `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나만 사용합니다. `PERFORM_TYPE="ALL"`이면 대상 지정 없이 전체 수행됩니다.
>
> ⚠️ 2026-08-26 확인 (article id `57389469766681`): 공식 JSON Schema는 최상위 `Argument`에
> `"ELEMS"` 또는 `"SECTIONS"` 중 하나가 항상 있어야 한다고 명시(`oneOf`)하지만, 공식
> Request 예제는 `{"Argument": {"PERFORM_TYPE": "ALL"}}`처럼 둘 다 생략한 형태입니다(원문
> 자체의 스키마·예제 불일치). 예제가 실제 동작을 반영한다고 보고 `PERFORM_TYPE="ALL"`일 때는
> 둘 다 생략 가능한 것으로 기술을 유지합니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
```

**Response Body**

```json
{
  "message": "success"
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CODE-ANAL"

# 강재 코드 검토(설계 계산) 실행
payload = {
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())
```

---

## 24. `DESIGN/STEEL/KDS-41-30-2022/CODE-TABLE` — Steel Code Check Table (강재 코드 검토 표)

> **기능:** 강재 코드 검토 결과를 표(부재기준 MEMB / 단면기준 PROP) 형태로 반환합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CODE-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "TABLE_TYPE"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "ELEMS"
          ]
        },
        {
          "required": [
            "SECTIONS"
          ]
        }
      ],
      "properties": {
        "TABLE_TYPE": {
          "type": "string",
          "description": "Result Table Type",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element No. Input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to160')"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify Structure Group Name"
            }
          },
          "oneOf": [
            {
              "required": [
                "KEYS"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "TO"
                    ]
                  },
                  {
                    "required": [
                      "STRUCTURE_GROUP_NAME"
                    ]
                  }
                ]
              }
            },
            {
              "required": [
                "TO"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "KEYS"
                    ]
                  },
                  {
                    "required": [
                      "STRUCTURE_GROUP_NAME"
                    ]
                  }
                ]
              }
            },
            {
              "required": [
                "STRUCTURE_GROUP_NAME"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "KEYS"
                    ]
                  },
                  {
                    "required": [
                      "TO"
                    ]
                  }
                ]
              }
            }
          ]
        },
        "SECTIONS": {
          "type": "array",
          "description": "List of section numbers to include in the table.",
          "items": {
            "type": "integer"
          }
        },
        "PRI_SORT": {
          "type": "integer",
          "description": "Sorting criteria for member-based output (by Section No. or Member No.)",
          "default": 1,
          "oneOf": [
            {
              "title": "SECT",
              "const": 0
            },
            {
              "title": "MEMB",
              "const": 1
            }
          ]
        },
        "RESULT": {
          "type": "integer",
          "description": "Filter results by check status",
          "default": 0,
          "oneOf": [
            {
              "title": "All",
              "const": 0
            },
            {
              "title": "OK",
              "const": 1
            },
            {
              "title": "NG",
              "const": 2
            }
          ]
        },
        "VIEW_RATPC": {
          "type": "boolean",
          "description": "Filter to show only members with RatPc greater than 0.4",
          "default": false
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response Table Title",
          "default": ""
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting",
          "properties": {
            "FORCE": {
              "type": "string",
              "description": "Force unit"
            },
            "DIST": {
              "type": "string",
              "description": "Length/Distance unit"
            },
            "HEAT": {
              "type": "string",
              "description": "Heat unit"
            },
            "TEMP": {
              "type": "string",
              "description": "Temperature unit"
            }
          }
        },
        "STYLES": {
          "type": "object",
          "description": "Response Number Format",
          "properties": {
            "FORMAT": {
              "type": "string",
              "description": "Number format",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "description": "Digit place",
              "minimum": 0,
              "maximum": 15
            }
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "CHK",
              "MEMB",
              "COM",
              "SECT",
              "SHR",
              "Section",
              "Material",
              "Fy",
              "LCB",
              "Len",
              "Lb",
              "Ly",
              "Lz",
              "Cb",
              "Ky",
              "Kz",
              "B1y",
              "B1z",
              "B2y",
              "B2z",
              "RatPc",
              "Pu",
              "pPn",
              "Muy",
              "pMny",
              "Muz",
              "pMnz",
              "Vuy",
              "pVny",
              "Vuz",
              "pVnz",
              "Tu",
              "pTn",
              "Def",
              "Defa"
            ]
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 표 타입 (`"MEMB"`=부재기준, `"PROP"`=단면기준) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 3 | 요소 입력 (ELEMS/SECTIONS 중 하나) — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` | `"ELEMS"` | Object | — | 조건부 |
| 4 | 단면 번호 (ELEMS/SECTIONS 중 하나) | `"SECTIONS"` | Array[Integer] | — | 조건부 |
| 5 | 1차 정렬 (0=SECT, 1=MEMB) | `"PRI_SORT"` | Integer (oneOf) | `1` | 선택 |
| 6 | 결과 필터 (0=All, 1=OK, 2=NG) | `"RESULT"` | Integer (oneOf) | `0` | 선택 |
| 7 | RatPc > 0.4 부재만 표시 | `"VIEW_RATPC"` | Boolean | `false` | 선택 |
| 8 | 응답 표 제목 | `"TABLE_NAME"` | String | `""` | 선택 |
| 9 | 결과 파일 저장 경로 | `"EXPORT_PATH"` | String | — | 선택 |
| 10 | 단위 설정 | `"UNIT"` | Object | — | 선택 |
| 10.1 | 힘 단위 | `"FORCE"` | String | — | 선택 |
| 10.2 | 길이 단위 | `"DIST"` | String | — | 선택 |
| 10.3 | 열 단위 | `"HEAT"` | String | — | 선택 |
| 10.4 | 온도 단위 | `"TEMP"` | String | — | 선택 |
| 11 | 숫자 포맷 | `"STYLES"` | Object | — | 선택 |
| 11.1 | 포맷 (Default/Fixed/Scientific/General) | `"FORMAT"` | String (enum) | — | 선택 |
| 11.2 | 소수 자릿수 (0~15) | `"PLACE"` | Integer | — | 선택 |
| 12 | 결과 표 성분 목록 | `"COMPONENTS"` | Array[String] | — | 선택 |

> **`COMPONENTS` 주요 성분:** `CHK`(검토결과), `MEMB`(부재번호), `COM`(최대 조합 상호작용비), `SECT`(단면번호), `SHR`(전단응력비), `Section`(단면명), `Material`(재질명), `Fy`(항복강도), `LCB`(지배 하중조합), `Len`(부재길이), `Lb`(횡지지길이), `Ly`/`Lz`(비지지길이), `Cb`(휨계수), `Ky`/`Kz`(유효길이계수), `B1y`/`B1z`/`B2y`/`B2z`(모멘트 증폭계수), `RatPc`(축강도비), `Pu`/`pPn`(소요/설계 축강도), `Muy`/`pMny`·`Muz`/`pMnz`(소요/설계 휨강도), `Vuy`/`pVny`·`Vuz`/`pVnz`(소요/설계 전단강도), `Tu`/`pTn`(소요/설계 비틀림강도), `Def`/`Defa`(처짐/허용처짐).

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "PROP",
    "PRI_SORT": 1,
    "RESULT": 0,
    "COMPONENTS": [
      "CHK",
      "MEMB",
      "COM",
      "SECT",
      "SHR",
      "Section",
      "Material",
      "Fy",
      "LCB",
      "Len",
      "Lb",
      "Ly",
      "Lz",
      "Cb",
      "Ky",
      "Kz",
      "B1y",
      "B1z",
      "B2y",
      "B2z",
      "RatPc",
      "Pu",
      "pPn",
      "Muy",
      "pMny",
      "Muz",
      "pMnz",
      "Vuy",
      "pVny",
      "Vuz",
      "pVnz",
      "Tu",
      "pTn",
      "Def",
      "Defa"
    ],
    "ELEMS": {
      "KEYS": [
        888
      ]
    }
  }
}
```

**Response Body**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "CHK",
      "MEMB",
      "COM",
      "SECT",
      "SHR",
      "Section",
      "Material",
      "Fy",
      "LCB",
      "Len",
      "Lb",
      "Ly",
      "Lz",
      "Cb",
      "Ky",
      "Kz",
      "B1y",
      "B1z",
      "B2y",
      "B2z",
      "RatPc",
      "Pu",
      "pPn",
      "Muy",
      "pMny",
      "Muz",
      "pMnz",
      "Vuy",
      "pVny",
      "Vuz",
      "pVnz",
      "Tu",
      "pTn",
      "Def",
      "Defa"
    ],
    "DATA": [
      [
        "OK",
        "888",
        "0.000",
        "1",
        "0.000",
        "400x600, BT 600x400x6/6",
        "SM355",
        "355000",
        "10",
        "3.25000",
        "3.25000",
        "3.25000",
        "3.25000",
        "1.000",
        "1.000",
        "1.000",
        "1.000",
        "1.000",
        "1.000",
        "1.000",
        "0.000",
        "0.00000",
        "1905.50",
        "0.00000",
        "150.596",
        "0.00000",
        "51.1371",
        "0.00000",
        "460.080",
        "0.00000",
        "73.9731",
        "-",
        "-",
        "-",
        "-"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CODE-TABLE"

# 강재 코드 검토 결과 표 조회
payload = {
  "Argument": {
    "TABLE_TYPE": "PROP",
    "PRI_SORT": 1,
    "RESULT": 0,
    "COMPONENTS": [
      "CHK",
      "MEMB",
      "COM",
      "SECT",
      "SHR",
      "Section",
      "Material",
      "Fy",
      "LCB",
      "Len",
      "Lb",
      "Ly",
      "Lz",
      "Cb",
      "Ky",
      "Kz",
      "B1y",
      "B1z",
      "B2y",
      "B2z",
      "RatPc",
      "Pu",
      "pPn",
      "Muy",
      "pMny",
      "Muz",
      "pMnz",
      "Vuy",
      "pVny",
      "Vuz",
      "pVnz",
      "Tu",
      "pTn",
      "Def",
      "Defa"
    ],
    "ELEMS": {
      "KEYS": [
        888
      ]
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())
```

---

## 25. `DESIGN/STEEL/KDS-41-30-2022/CODE-REPORT` — Steel Code Check Report (강재 코드 검토 보고서)

> **기능:** 강재 코드 검토 보고서를 Graphic(JPG)/Detail(DOC)/Summary(TXT) 형식으로 파일에 출력합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CODE-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "REPORT_TYPE",
        "CURRENT_MODE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "ELEMS"
          ]
        },
        {
          "required": [
            "SECTIONS"
          ]
        }
      ],
      "properties": {
        "REPORT_TYPE": {
          "type": "string",
          "description": "Report Table Type",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE": {
          "type": "string",
          "description": "Report output mode",
          "oneOf": [
            {
              "title": "Graphic (JPG image)",
              "const": "Graphic"
            },
            {
              "title": "Detail (DOC document)",
              "const": "Detail"
            },
            {
              "title": "Summary (TXT text)",
              "const": "Summary"
            }
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element No. Input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to160')"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify Structure Group Name"
            }
          },
          "oneOf": [
            {
              "required": [
                "KEYS"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "TO"
                    ]
                  },
                  {
                    "required": [
                      "STRUCTURE_GROUP_NAME"
                    ]
                  }
                ]
              }
            },
            {
              "required": [
                "TO"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "KEYS"
                    ]
                  },
                  {
                    "required": [
                      "STRUCTURE_GROUP_NAME"
                    ]
                  }
                ]
              }
            },
            {
              "required": [
                "STRUCTURE_GROUP_NAME"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "KEYS"
                    ]
                  },
                  {
                    "required": [
                      "TO"
                    ]
                  }
                ]
              }
            }
          ]
        },
        "SECTIONS": {
          "type": "array",
          "description": "List of section numbers to include in the report",
          "items": {
            "type": "integer"
          }
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Directory path to save the report files"
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "Output file base name. For multiple elements, files are prefixed with index and element number (e.g. 001_E859_filename.jpg, 002_E1_filename.jpg)"
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 보고서 표 타입 (`"MEMB"`, `"PROP"`) | `"REPORT_TYPE"` | String (enum) | — | **필수** |
| 3 | 출력 모드 (`"Graphic"`=JPG, `"Detail"`=DOC, `"Summary"`=TXT) | `"CURRENT_MODE"` | String (oneOf) | — | **필수** |
| 4 | 요소 입력 (ELEMS/SECTIONS 중 하나) — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` | `"ELEMS"` | Object | — | 조건부 |
| 5 | 단면 번호 (ELEMS/SECTIONS 중 하나) | `"SECTIONS"` | Array[Integer] | — | 조건부 |
| 6 | 저장 디렉터리 경로 (예 `C:\\MIDAS\\Report\\`) | `"EXPORT_PATH"` | String | — | **필수** |
| 7 | 출력 파일 기본 이름 (다중 요소 시 인덱스·요소번호 접두어 부가) | `"OUTPUT_NAME"` | String | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "out.jpg",
    "ELEMS": {
      "KEYS": [
        888,
        1058
      ]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\out.jpg",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CODE-REPORT"

# 강재 코드 검토 보고서 파일 출력
payload = {
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "out.jpg",
    "ELEMS": {
      "KEYS": [
        888,
        1058
      ]
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())
```

---

## 26. `DESIGN/STEEL/KDS-41-30-2022/DREULT` — Steel Design Result (강재 설계 결과 이미지)

> **기능:** 강재 설계 결과를 화면에 표시하고 이미지(JPG)로 캡처·저장합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/DREULT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "EXPORT_PATH",
        "RESULT_GRAPHIC"
      ],
      "additionalProperties": false,
      "properties": {
        "EXPORT_PATH": {
          "type": "string",
          "description": "Image file save path and file name."
        },
        "FIGURE_NAME": {
          "type": "string",
          "description": "Smart report image name."
        },
        "SET_HIDDEN": {
          "type": "boolean",
          "description": "Hidden option.",
          "default": false
        },
        "ACTIVE": {
          "type": "object",
          "description": "View/Active settings. For detailed field specifications, refer to the Active documentation."
        },
        "WIDTH": {
          "type": "integer",
          "description": "Image width in pixels.",
          "default": 1000,
          "minimum": 100,
          "maximum": 10000
        },
        "HEIGHT": {
          "type": "integer",
          "description": "Image height in pixels.",
          "default": 1000,
          "minimum": 100,
          "maximum": 10000
        },
        "STAGE_NAME": {
          "type": "string",
          "description": "Construction stage name."
        },
        "ANGLE": {
          "type": "object",
          "description": "View angle settings.",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "HORIZONTAL": {
              "type": "number",
              "description": "Horizontal rotation angle.",
              "default": 0
            },
            "VERTICAL": {
              "type": "number",
              "description": "Vertical rotation angle.",
              "default": 0
            }
          }
        },
        "DISPLAY": {
          "type": "object",
          "description": "View/Display settings. For detailed field specifications, refer to the Display documentation."
        },
        "PERSPECTIVE": {
          "type": "boolean",
          "description": "Enable perspective view.",
          "default": false
        },
        "ZOOM_LEVEL": {
          "type": "number",
          "description": "Zoom level.",
          "default": 100,
          "minimum": 25,
          "maximum": 200
        },
        "BGCOLOR_TOP": {
          "type": "object",
          "description": "Top background color.",
          "additionalProperties": false,
          "properties": {
            "R": {
              "type": "integer",
              "description": "Red component.",
              "minimum": 0,
              "maximum": 255
            },
            "G": {
              "type": "integer",
              "description": "Green component.",
              "minimum": 0,
              "maximum": 255
            },
            "B": {
              "type": "integer",
              "description": "Blue component.",
              "minimum": 0,
              "maximum": 255
            }
          }
        },
        "RESULT_GRAPHIC": {
          "type": "object",
          "description": "Result graphic display settings.",
          "required": [
            "CURRENT_MODE",
            "LOAD_CASE_COMB"
          ],
          "additionalProperties": false,
          "properties": {
            "CURRENT_MODE": {
              "type": "string",
              "description": "Current mode.",
              "oneOf": [
                {
                  "title": "Steel Design",
                  "const": "INFLL_DESIGN_STEEL"
                }
              ]
            },
            "LOAD_CASE_COMB": {
              "type": "object",
              "description": "Load cases and combinations.",
              "required": [
                "TYPE",
                "NAME"
              ],
              "additionalProperties": false,
              "properties": {
                "TYPE": {
                  "type": "string",
                  "description": "Load case type.",
                  "oneOf": [
                    {
                      "title": "Steel Design Load Combination",
                      "const": "CBS"
                    }
                  ]
                },
                "NAME": {
                  "type": "string",
                  "description": "Load case or combination name."
                }
              }
            },
            "COMPONENTS": {
              "type": "object",
              "description": "Component selection for design result display.",
              "required": [],
              "additionalProperties": false,
              "properties": {
                "COMP": {
                  "type": "string",
                  "description": "Design component to display.",
                  "default": "Combined",
                  "oneOf": [
                    {
                      "title": "Axial",
                      "const": "Axial"
                    },
                    {
                      "title": "Shear-y",
                      "const": "Shear-y"
                    },
                    {
                      "title": "Shear-z",
                      "const": "Shear-z"
                    },
                    {
                      "title": "Bend-y",
                      "const": "Bend-y"
                    },
                    {
                      "title": "Bend-z",
                      "const": "Bend-z"
                    },
                    {
                      "title": "Combined",
                      "const": "Combined"
                    }
                  ]
                }
              }
            },
            "TYPE_OF_DISPLAY": {
              "type": "object",
              "description": "Display options for design result visualization.",
              "required": [],
              "additionalProperties": false,
              "properties": {
                "CONTOUR": {
                  "type": "object",
                  "description": "Contour display settings.",
                  "required": [],
                  "additionalProperties": false,
                  "properties": {
                    "OPT_CHECK": {
                      "type": "boolean",
                      "description": "Enable contour display.",
                      "default": false
                    },
                    "NUM_OF_COLOR": {
                      "type": "integer",
                      "description": "Number of contour colors.",
                      "default": 12,
                      "minimum": 2,
                      "maximum": 20
                    },
                    "COLOR_TYPE": {
                      "type": "string",
                      "description": "Contour color type.",
                      "default": "vrgb",
                      "oneOf": [
                        {
                          "title": "V->R->G->B",
                          "const": "vrgb"
                        },
                        {
                          "title": ">R->G->B",
                          "const": "rgb"
                        },
                        {
                          "title": "R->B->G",
                          "const": "rbg"
                        },
                        {
                          "title": "Gray Scaled",
                          "const": "gray scaled"
                        }
                      ]
                    },
                    "OPTIONS": {
                      "type": "object",
                      "description": "Contour options.",
                      "required": [],
                      "additionalProperties": false,
                      "properties": {
                        "GRADIENT_FILL": {
                          "type": "boolean",
                          "description": "Use gradient fill.",
                          "default": false
                        },
                        "CONTOUR_FILL": {
                          "type": "boolean",
                          "description": "Use contour fill.",
                          "default": true
                        }
                      }
                    }
                  }
                },
                "VALUES": {
                  "type": "object",
                  "description": "Value display settings.",
                  "required": [],
                  "additionalProperties": false,
                  "properties": {
                    "OPT_CHECK": {
                      "type": "boolean",
                      "description": "Enable value display.",
                      "default": false
                    },
                    "DECIMAL_PT": {
                      "type": "integer",
                      "description": "Decimal places.",
                      "default": 0,
                      "minimum": 0,
                      "maximum": 15
                    },
                    "VALUE_EXP": {
                      "type": "boolean",
                      "description": "Use exponential notation.",
                      "default": false
                    },
                    "MINMAX_ONLY": {
                      "type": "object",
                      "description": "Min/max display settings.",
                      "required": [],
                      "additionalProperties": false,
                      "properties": {
                        "MAXMIN": {
                          "type": "string",
                          "description": "Min/max display mode.",
                          "default": "Min & Max",
                          "oneOf": [
                            {
                              "title": "Min. & Max",
                              "const": "Min & Max"
                            },
                            {
                              "title": "Absolut Max",
                              "const": "Abs Max"
                            },
                            {
                              "title": "Maximum",
                              "const": "max"
                            },
                            {
                              "title": "MMinimumin",
                              "const": "min"
                            }
                          ]
                        },
                        "LIMIT_SCALE": {
                          "type": "integer",
                          "description": "Scale limit.",
                          "default": 0
                        }
                      }
                    },
                    "SET_ORIENT": {
                      "type": "integer",
                      "description": "Value text orientation.",
                      "default": 0
                    }
                  }
                },
                "LEGEND": {
                  "type": "object",
                  "description": "Legend display settings.",
                  "required": [],
                  "additionalProperties": false,
                  "properties": {
                    "OPT_CHECK": {
                      "type": "boolean",
                      "description": "Enable legend display.",
                      "default": false
                    },
                    "POSITION": {
                      "type": "string",
                      "description": "Legend position.",
                      "default": "left",
                      "oneOf": [
                        {
                          "title": "Right",
                          "const": "right"
                        },
                        {
                          "title": "Left",
                          "const": "left"
                        },
                        {
                          "title": "Top",
                          "const": "top"
                        },
                        {
                          "title": "Bottom",
                          "const": "bottom"
                        }
                      ]
                    },
                    "VALUE_EXP": {
                      "type": "boolean",
                      "description": "Use exponential notation for legend values.",
                      "default": true
                    },
                    "DECIMAL_PT": {
                      "type": "integer",
                      "description": "Decimal places for legend values.",
                      "default": 0,
                      "minimum": 0,
                      "maximum": 15
                    }
                  }
                },
                "CODE_CHECKING_RATIO": {
                  "type": "object",
                  "description": "Steel code checking ratio display settings.",
                  "required": [],
                  "additionalProperties": false,
                  "properties": {
                    "CHECK": {
                      "type": "boolean",
                      "description": "Enable code checking ratio display.",
                      "default": true
                    },
                    "DISPLAY_MEMBERS": {
                      "type": "object",
                      "description": "Steel member types to display.",
                      "required": [],
                      "additionalProperties": false,
                      "properties": {
                        "BEAM": {
                          "type": "boolean",
                          "description": "Display beam members.",
                          "default": true
                        },
                        "COLUMN": {
                          "type": "boolean",
                          "description": "Display column members.",
                          "default": true
                        },
                        "BRACE": {
                          "type": "boolean",
                          "description": "Display brace members.",
                          "default": true
                        }
                      }
                    },
                    "COLUMN_SECTION_SIZE": {
                      "type": "object",
                      "description": "Column section size display settings.",
                      "required": [],
                      "additionalProperties": false,
                      "properties": {
                        "SCALE_FACTOR": {
                          "type": "number",
                          "description": "Scale factor for column section visualization.",
                          "default": 1,
                          "minimum": 0.1,
                          "maximum": 100
                        }
                      }
                    },
                    "VALUE_OPTION": {
                      "type": "object",
                      "description": "Value display format settings.",
                      "required": [],
                      "additionalProperties": false,
                      "properties": {
                        "DECIMAL_PLACES": {
                          "type": "integer",
                          "description": "Number of decimal places.",
                          "default": 2,
                          "minimum": 0,
                          "maximum": 15
                        },
                        "EXPONENTIAL": {
                          "type": "boolean",
                          "description": "Use exponential notation.",
                          "default": false
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 이미지 저장 경로 및 파일명 | `"EXPORT_PATH"` | String | — | **필수** |
| 3 | 스마트 리포트 이미지 이름 | `"FIGURE_NAME"` | String | — | 선택 |
| 4 | Hidden 옵션 | `"SET_HIDDEN"` | Boolean | `false` | 선택 |
| 5 | View/Active 설정 (Active 문서 참조) | `"ACTIVE"` | Object | — | 선택 |
| 6 | 이미지 폭 px (100~10000) | `"WIDTH"` | Integer | `1000` | 선택 |
| 7 | 이미지 높이 px (100~10000) | `"HEIGHT"` | Integer | `1000` | 선택 |
| 8 | 시공단계 이름 | `"STAGE_NAME"` | String | — | 선택 |
| 9 | 뷰 각도 | `"ANGLE"` | Object | — | 선택 |
| 9.1 | 수평 회전각 | `"HORIZONTAL"` | Number | `0` | 선택 |
| 9.2 | 수직 회전각 | `"VERTICAL"` | Number | `0` | 선택 |
| 10 | View/Display 설정 (Display 문서 참조) | `"DISPLAY"` | Object | — | 선택 |
| 11 | 원근투영 | `"PERSPECTIVE"` | Boolean | `false` | 선택 |
| 12 | 줌 레벨 (25~200) | `"ZOOM_LEVEL"` | Number | `100` | 선택 |
| 13 | 상단 배경색 (R/G/B, 0~255) | `"BGCOLOR_TOP"` | Object | — | 선택 |
| 14 | 결과 그래픽 설정 | `"RESULT_GRAPHIC"` | Object | — | **필수** |
| 14.1 | 현재 모드 (`"INFLL_DESIGN_STEEL"`=Steel Design) | `"CURRENT_MODE"` | String (oneOf) | — | **필수** |
| 14.2 | 하중케이스/조합 | `"LOAD_CASE_COMB"` | Object | — | **필수** |
| 14.2.1 | 하중 타입 (`"CBS"`=Steel Design Load Combination) | `"TYPE"` | String (oneOf) | — | **필수** |
| 14.2.2 | 하중 이름 | `"NAME"` | String | — | **필수** |
| 14.3 | 표시 성분 (`COMP`: Axial/Shear-y/Shear-z/Bend-y/Bend-z/Combined) | `"COMPONENTS"` | Object | — | 선택 |
| 14.4 | 표시 타입 (CONTOUR / VALUES / LEGEND / CODE_CHECKING_RATIO) | `"TYPE_OF_DISPLAY"` | Object | — | 선택 |
| 14.4.1 | Contour (OPT_CHECK, NUM_OF_COLOR 2~20, COLOR_TYPE vrgb/rgb/rbg/gray scaled, OPTIONS.GRADIENT_FILL·CONTOUR_FILL) | `"CONTOUR"` | Object | — | 선택 |
| 14.4.2 | Values (OPT_CHECK, DECIMAL_PT, VALUE_EXP, MINMAX_ONLY.MAXMIN, SET_ORIENT) | `"VALUES"` | Object | — | 선택 |
| 14.4.3 | Legend (OPT_CHECK, POSITION right/left/top/bottom, VALUE_EXP, DECIMAL_PT) | `"LEGEND"` | Object | — | 선택 |
| 14.4.4 | Code Checking Ratio (COMP=Combined일 때; CHECK, DISPLAY_MEMBERS.BEAM·COLUMN·BRACE, COLUMN_SECTION_SIZE.SCALE_FACTOR, VALUE_OPTION) | `"CODE_CHECKING_RATIO"` | Object | — | 선택 |

> `RESULT_GRAPHIC` 하위는 위 표 외에도 스키마에 상세 중첩 필드가 정의되어 있습니다(각 색상/값/범례 옵션의 기본값·범위는 위의 **JSON Schema** 블록 참조).

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\result\\steel design result.jpg",
    "SET_HIDDEN": true,
    "WIDTH": 1000,
    "HEIGHT": 1000,
    "PERSPECTIVE": false,
    "ZOOM_LEVEL": 100,
    "RESULT_GRAPHIC": {
      "CURRENT_MODE": "INFLL_DESIGN_STEEL",
      "LOAD_CASE_COMB": {
        "TYPE": "CBS",
        "NAME": "STEEL_gLCB5"
      },
      "COMPONENTS": {
        "COMP": "Combined"
      },
      "TYPE_OF_DISPLAY": {
        "LEGEND": {
          "OPT_CHECK": true,
          "VALUE_EXP": false,
          "DECIMAL_PT": 3
        },
        "CONTOUR": {
          "OPT_CHECK": true,
          "OPTIONS": {
            "GRADIENT_FILL": true
          }
        },
        "VALUES": {
          "OPT_CHECK": true,
          "DECIMAL_PT": 5,
          "VALUE_EXP": true,
          "SET_ORIENT": 15,
          "MINMAX_ONLY": {
            "MAXMIN": "min",
            "LIMIT_SCALE": 5
          }
        },
        "CODE_CHECKING_RATIO": {
          "CHECK": true,
          "DISPLAY_MEMBERS": {
            "COLUMN": true,
            "BEAM": false,
            "BRACE": true
          }
        }
      }
    }
  }
}
```

**Response Body**

```json
{
  "message": "MIDAS GEN NX command complete"
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/DREULT"

# 강재 설계 결과 이미지 캡처/저장
payload = {
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\result\\steel design result.jpg",
    "SET_HIDDEN": true,
    "WIDTH": 1000,
    "HEIGHT": 1000,
    "PERSPECTIVE": false,
    "ZOOM_LEVEL": 100,
    "RESULT_GRAPHIC": {
      "CURRENT_MODE": "INFLL_DESIGN_STEEL",
      "LOAD_CASE_COMB": {
        "TYPE": "CBS",
        "NAME": "STEEL_gLCB5"
      },
      "COMPONENTS": {
        "COMP": "Combined"
      },
      "TYPE_OF_DISPLAY": {
        "LEGEND": {
          "OPT_CHECK": true,
          "VALUE_EXP": false,
          "DECIMAL_PT": 3
        },
        "CONTOUR": {
          "OPT_CHECK": true,
          "OPTIONS": {
            "GRADIENT_FILL": true
          }
        },
        "VALUES": {
          "OPT_CHECK": true,
          "DECIMAL_PT": 5,
          "VALUE_EXP": true,
          "SET_ORIENT": 15,
          "MINMAX_ONLY": {
            "MAXMIN": "min",
            "LIMIT_SCALE": 5
          }
        },
        "CODE_CHECKING_RATIO": {
          "CHECK": true,
          "DISPLAY_MEMBERS": {
            "COLUMN": true,
            "BEAM": false,
            "BRACE": true
          }
        }
      }
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())
```

---

## 27. `DESIGN/STEEL/KDS-41-30-2022/TABLE` — Steel Member Design Forces (강재 부재 설계 부재력)

> **기능:** 강재 설계 부재력 표(STEELMEMBERDESIGNFORCES)를 반환하거나 파일로 저장합니다.

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "TABLE_TYPE"
      ],
      "additionalProperties": false,
      "properties": {
        "TABLE_NAME": {
          "type": "string",
          "description": "Response Table Title",
          "default": ""
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Result Table Type",
          "enum": [
            "STEELMEMBERDESIGNFORCES"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting",
          "properties": {
            "FORCE": {
              "type": "string",
              "description": "Force unit"
            },
            "DIST": {
              "type": "string",
              "description": "Length/Distance unit"
            },
            "HEAT": {
              "type": "string",
              "description": "Heat unit"
            },
            "TEMP": {
              "type": "string",
              "description": "Temperature unit"
            }
          },
          "default": "System"
        },
        "STYLES": {
          "type": "object",
          "description": "Response Number Format",
          "properties": {
            "FORMAT": {
              "type": "string",
              "description": "Number format",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "description": "Digit place",
              "minimum": 0,
              "maximum": 15
            }
          },
          "default": "System"
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Memb",
              "Part",
              "LComName",
              "Type",
              "Fx",
              "Fy",
              "Fz",
              "Mx",
              "My",
              "Mz"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to160')"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify Structure Group Name"
            }
          },
          "oneOf": [
            {
              "required": [
                "KEYS"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "TO"
                    ]
                  },
                  {
                    "required": [
                      "STRUCTURE_GROUP_NAME"
                    ]
                  }
                ]
              }
            },
            {
              "required": [
                "TO"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "KEYS"
                    ]
                  },
                  {
                    "required": [
                      "STRUCTURE_GROUP_NAME"
                    ]
                  }
                ]
              }
            },
            {
              "required": [
                "STRUCTURE_GROUP_NAME"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "KEYS"
                    ]
                  },
                  {
                    "required": [
                      "TO"
                    ]
                  }
                ]
              }
            }
          ]
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "Part1/4",
              "Part2/4",
              "Part3/4",
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 응답 표 제목 | `"TABLE_NAME"` | String | `""` | 선택 |
| 3 | 표 타입 (`"STEELMEMBERDESIGNFORCES"` 고정) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 4 | 결과 파일 저장 경로 | `"EXPORT_PATH"` | String | — | 선택 |
| 5 | 단위 설정 (FORCE/DIST/HEAT/TEMP) | `"UNIT"` | Object | `"System"` | 선택 |
| 6 | 숫자 포맷 (FORMAT: Default/Fixed/Scientific/General, PLACE 0~15) | `"STYLES"` | Object | `"System"` | 선택 |
| 7 | 결과 표 성분 (`Index`,`Memb`,`Part`,`LComName`,`Type`,`Fx`,`Fy`,`Fz`,`Mx`,`My`,`Mz`) | `"COMPONENTS"` | Array[String] | — | 선택 |
| 8 | 노드/요소 선택 (`KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나) | `"NODE_ELEMS"` | Object | — | 선택 |
| 9 | 요소 파트 (`PartI`,`Part1/4`,`Part2/4`,`Part3/4`,`PartJ`) | `"PARTS"` | Array[String] | `["All"]` | 선택 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "STEELMEMBERDESIGNFORCES",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\SteelMemberForces.json",
    "COMPONENTS": [
      "Index",
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fx",
      "Fy",
      "Fz",
      "Mx",
      "My",
      "Mz"
    ],
    "PARTS": [
      "All",
      "PartI",
      "Part1/4",
      "Part2/4",
      "Part3/4",
      "PartJ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1072
      ]
    }
  }
}
```

**Response Body**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fx",
      "Fy",
      "Fz",
      "Mx",
      "My",
      "Mz"
    ],
    "DATA": [
      [
        "1",
        "1072",
        "I",
        "gLCB183",
        "Max",
        "0.0000",
        "0.0000",
        "-137.7264",
        "0.0000",
        "-144.9112",
        "0.0000"
      ],
      [
        "2",
        "1072",
        "I",
        "gLCB184",
        "Max",
        "0.0000",
        "0.0000",
        "-118.0512",
        "0.0000",
        "-124.2096",
        "0.0000"
      ],
      [
        "3",
        "1072",
        "1/4",
        "gLCB183",
        "Max",
        "0.0000",
        "0.0000",
        "-107.3363",
        "0.0000",
        "-83.5333",
        "0.0000"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/TABLE"

# 강재 부재 설계 부재력 표 조회
payload = {
  "Argument": {
    "TABLE_TYPE": "STEELMEMBERDESIGNFORCES",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\SteelMemberForces.json",
    "COMPONENTS": [
      "Index",
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fx",
      "Fy",
      "Fz",
      "Mx",
      "My",
      "Mz"
    ],
    "PARTS": [
      "All",
      "PartI",
      "Part1/4",
      "Part2/4",
      "Part3/4",
      "PartJ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1072
      ]
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())
```

---

## End-to-End Workflow

아래 예제는 강재 설계의 전형적 흐름을 하나로 연결합니다: **설계 코드 옵션(DCO, PUT) → 비지지 길이(LENG, POST) → 설계 부재 배정(MEMB, PUT) → 코드 검토 수행(CODE-ANAL) → 결과 표 조회(CODE-TABLE / TABLE)**. 공통 base 접두어를 처리하는 재사용 헬퍼를 포함합니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
STEEL_BASE = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022"


def steel(method, code, payload=None):
    """DESIGN/STEEL/KDS-41-30-2022/<code> 공통 호출 헬퍼"""
    url = f"{STEEL_BASE}/{code}"
    res = requests.request(method, url, headers=HEADERS, json=payload)
    res.raise_for_status()
    try:
        return res.json()
    except ValueError:
        return res.text


# 1) 설계 코드 옵션 설정 (DCO, PUT) — config-singleton
steel("PUT", "DCO", {
    "Assign": {"1": {
        "DGNCODE": "KDS 41 30 : 2022",
        "DEFL_CHK": True,
        "SEISMIC": False,
        "COMB_RATIO": 0,
    }}
})

# 2) 비지지 길이 설정 (LENG, POST) — member-CRUD
steel("POST", "LENG", {
    "Assign": {
        "888": {"LY": 3.5, "LZ": 3.5, "LB": 3.5},
        "891": {"LY": 4.0, "LZ": 4.0, "LB": 2.0},
    }
})

# 3) 설계 부재 배정 (MEMB, PUT) — 요소를 설계 부재로 묶음
steel("PUT", "MEMB", {
    "Assign": {
        "1": {"AELEM": [933, 934], "bREVERSE": False},
        "2": {"AELEM": [906, 891], "bREVERSE": True},
    }
})

# 4) 강재 코드 검토 수행 (CODE-ANAL, POST) — 전체 요소 대상
print("코드 검토:", steel("POST", "CODE-ANAL", {"Argument": {"PERFORM_TYPE": "ALL"}}))

# 5-a) 코드 검토 결과 표 조회 (CODE-TABLE, POST)
table = steel("POST", "CODE-TABLE", {
    "Argument": {
        "TABLE_TYPE": "MEMB",
        "PRI_SORT": 1,
        "RESULT": 0,
        "COMPONENTS": ["CHK", "MEMB", "SECT", "Section", "Material", "COM", "RatPc"],
        "ELEMS": {"KEYS": [888]},
    }
})
print("검토 표:", table)

# 5-b) 강재 부재 설계 부재력 표 조회 (TABLE, POST)
forces = steel("POST", "TABLE", {
    "Argument": {
        "TABLE_TYPE": "STEELMEMBERDESIGNFORCES",
        "COMPONENTS": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
        "NODE_ELEMS": {"KEYS": [1072]},
    }
})
print("부재력 표:", forces)
```
