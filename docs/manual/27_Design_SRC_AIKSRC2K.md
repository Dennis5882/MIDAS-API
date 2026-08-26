# 27. Design Code – SRC AIK-SRC2K (SRC 합성부재 설계)

> **대상 제품:** MIDAS Gen NX · MIDAS Civil NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

이 파트는 **SRC(철골 철근콘크리트 합성부재) 설계 코드 AIK-SRC2K** 엔드포인트 **27개**를 다룹니다. 모든 엔드포인트는 공통 URI 접두사 **`{base url}/DESIGN/SRC/AIK-SRC2K/<CODE>`** 를 사용합니다.

- **`"Assign"` 방식:** 설계 코드·부재 파라미터·재료·단면 설정 엔드포인트는 요청 바디에서 `"Assign"` 객체(키=ID 문자열 또는 부재 번호)를 사용합니다.
- **`"Argument"` 방식:** 검토 수행(`*-ANAL`)·결과 테이블(`*-TABLE`, `TABLE`)·리포트(`*-REPORT`)·최적설계(`OCHECK`) 엔드포인트는 `POST` 전용이며 `"Argument"` 객체로 대상·옵션을 지정합니다.
- **메서드 패턴:** 엔드포인트마다 다릅니다(예: `DSRC`=PUT·DELETE, `DCO`=PUT·GET·DELETE, 설정 싱글톤=GET·PUT·DELETE, 부재 파라미터=POST·GET·PUT·DELETE, 액션=POST 전용). 각 절의 Active Methods를 확인하세요.
- **`TABLE` 공용 URI:** SRC 보/기둥 설계력은 동일 URI `DESIGN/SRC/AIK-SRC2K/TABLE`을 사용하며 `TABLE_TYPE`(`SRCBEAMDESIGNFORCES`/`SRCCOLUMNDESIGNFORCES`)로 구분합니다.

> **참고:** 강재 설계는 **[25_Design_Steel_KDS41302022.md](./25_Design_Steel_KDS41302022.md)**, RC 설계는 **[26_Design_RC_KDS41202022.md](./26_Design_RC_KDS41202022.md)** 를 참고하세요. SRC 설계 하중조합은 13장(Load Combinations)에서 다룹니다.

---

## Endpoint 목록 (27개)

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`DSRC`](#1-designsrcaik-src2kdsrc--src-설계-코드) | SRC 설계 코드 | `PUT` · `DELETE` |
| 2 | [`DCO`](#2-designsrcaik-src2kdco--설계-코드-옵션) | 설계 코드 옵션 | `PUT` · `GET` · `DELETE` |
| 3 | [`DCTL`](#3-designsrcaik-src2kdctl--프레임-정의) | 프레임 정의 | `GET` · `PUT` · `DELETE` |
| 4 | [`LLRF`](#4-designsrcaik-src2kllrf--활하중-저감계수) | 활하중 저감계수 | `GET` · `PUT` · `DELETE` |
| 5 | [`LCTB`](#5-designsrcaik-src2klctb--비선형-하중케이스-하중기여) | 비선형 하중케이스 하중기여 | `GET` · `DELETE` |
| 6 | [`LENG`](#6-designsrcaik-src2kleng--비지지-길이l-lb) | 비지지 길이(L, Lb) | `POST` · `GET` · `PUT` · `DELETE` |
| 7 | [`KFAC`](#7-designsrcaik-src2kkfac--유효좌굴길이계수k) | 유효좌굴길이계수(K) | `POST` · `GET` · `PUT` · `DELETE` |
| 8 | [`LTSR`](#8-designsrcaik-src2kltsr--세장비-제한) | 세장비 제한 | `POST` · `GET` · `PUT` · `DELETE` |
| 9 | [`CMFT`](#9-designsrcaik-src2kcmft--등가모멘트-보정계수cm) | 등가모멘트 보정계수(Cm) | `POST` · `GET` · `PUT` · `DELETE` |
| 10 | [`FMAG`](#10-designsrcaik-src2kfmag--모멘트-확대계수b1δb-b2δs) | 모멘트 확대계수(B1/δb, B2/δs) | `POST` · `GET` · `PUT` · `DELETE` |
| 11 | [`MLLR`](#11-designsrcaik-src2kmllr--활하중-저감계수-수정) | 활하중 저감계수 수정 | `POST` · `GET` · `PUT` · `DELETE` |
| 12 | [`SUEQ`](#12-designsrcaik-src2ksueq--지진-스케일업-계수) | 지진 스케일업 계수 | `POST` · `GET` · `PUT` · `DELETE` |
| 13 | [`MBTP`](#13-designsrcaik-src2kmbtp--부재-타입-수정) | 부재 타입 수정 | `POST` · `GET` · `PUT` · `DELETE` |
| 14 | [`EQCT`](#14-designsrcaik-src2keqct--지진-하중조합-타입) | 지진 하중조합 타입 | `POST` · `GET` · `PUT` · `DELETE` |
| 15 | [`BC-ANAL`](#15-designsrcaik-src2kbc-anal--src-보-검토-수행) | SRC 보 검토 수행 | `POST` |
| 16 | [`BC-TABLE`](#16-designsrcaik-src2kbc-table--src-보-검토-테이블) | SRC 보 검토 테이블 | `POST` |
| 17 | [`BC-REPORT`](#17-designsrcaik-src2kbc-report--src-보-검토-리포트) | SRC 보 검토 리포트 | `POST` |
| 18 | [`CC-ANAL`](#18-designsrcaik-src2kcc-anal--src-기둥-검토-수행) | SRC 기둥 검토 수행 | `POST` |
| 19 | [`CC-TABLE`](#19-designsrcaik-src2kcc-table--src-기둥-검토-테이블) | SRC 기둥 검토 테이블 | `POST` |
| 20 | [`CC-REPORT`](#20-designsrcaik-src2kcc-report--src-기둥-검토-리포트) | SRC 기둥 검토 리포트 | `POST` |
| 21 | [`OCHECK`](#21-designsrcaik-src2kocheck--src-최적-설계) | SRC 최적 설계 | `POST` |
| 22 | [`TABLE` (보)](#22-designsrcaik-src2ktable--src-보-설계력) | SRC 보 설계력 | `POST` |
| 23 | [`TABLE` (기둥)](#23-designsrcaik-src2ktable--src-기둥-설계력) | SRC 기둥 설계력 | `POST` |
| 24 | [`MATD`](#24-designsrcaik-src2kmatd--src-재료-수정) | SRC 재료 수정 | `GET` · `PUT` · `DELETE` |
| 25 | [`MCRD`](#25-designsrcaik-src2kmcrd--src-기둥-단면-데이터-수정) | SRC 기둥 단면 데이터 수정 | `POST` · `GET` · `PUT` · `DELETE` |
| 26 | [`MEMB`](#26-designsrcaik-src2kmemb--부재-배정) | 부재 배정 | `GET` · `PUT` · `DELETE` |
| 27 | [`MRBD`](#27-designsrcaik-src2kmrbd--src-보-단면-데이터-수정) | SRC 보 단면 데이터 수정 | `POST` · `GET` · `PUT` · `DELETE` |

---

## 1. `DESIGN/SRC/AIK-SRC2K/DSRC` — SRC 설계 코드

> **기능:** SRC 설계 코드(AIK-SRC2K)를 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/DSRC
```

### Active Methods

`PUT` · `DELETE`

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
      "maxProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
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
                "AIK-SRC2K"
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `DGNCODE` | string | 설계 코드 — 가능값: `AIK-SRC2K` |  | O |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "AIK-SRC2K"
    }
  }
}
```

**Response Body**

```json
{
  "DSRC": {
    "1": {
      "DGNCODE": "AIK-SRC2K"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "1": {
            "DGNCODE": "AIK-SRC2K"
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DSRC", json=payload, headers=HEADERS)
res.raise_for_status()

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DSRC", headers=HEADERS)
```

---

## 2. `DESIGN/SRC/AIK-SRC2K/DCO` — 설계 코드 옵션

> **기능:** SRC 설계 코드 옵션(내진 적용 등 전역 설계 옵션)을 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/DCO
```

### Active Methods

`PUT` · `GET` · `DELETE`

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
      "minProperties": 1,
      "maxProeprties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "DGNCODE",
            "SEISMIC"
          ],
          "additionalProperties": false,
          "properties": {
            "DGNCODE": {
              "type": "string",
              "description": "Design code.",
              "default": "AIK-SRC2K",
              "oneOf": [
                {
                  "const": "AIK-SRC2K",
                  "title": "AIK-SRC2K"
                }
              ]
            },
            "SEISMIC": {
              "type": "boolean",
              "description": "Whether seismic design is applied.",
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `DGNCODE` | string | 설계 코드. — `AIK-SRC2K`=AIK-SRC2K | AIK-SRC2K | O |
| `SEISMIC` | boolean | 내진설계 적용 여부. | true | O |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "AIK-SRC2K",
      "SEISMIC": true
    }
  }
}
```

**Response Body**

```json
{
  "SRCDCO": {
    "1": {
      "DGNCODE": "AIK-SRC2K",
      "SEISMIC": true
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "1": {
            "DGNCODE": "AIK-SRC2K",
            "SEISMIC": true
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCO", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCO", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCO", headers=HEADERS)
```

---

## 3. `DESIGN/SRC/AIK-SRC2K/DCTL` — 프레임 정의

> **기능:** 설계용 프레임(무/유측 이동, 자동 K 산정 등)을 정의합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/DCTL
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `FRAMEX` | string | X방향 프레임 — `Unbraced Sway`=비횡지지 \| Sway; `Braced Non-sway`=횡지지 \| Non-sway | Braced Non-sway |  |
| `FRAMEY` | string | Y방향 프레임 — `Unbraced Sway`=비횡지지 \| Sway; `Braced Non-sway`=횡지지 \| Non-sway | Braced Non-sway |  |
| `bAUTOKF` | boolean | 유효좌굴길이계수 자동계산 | false |  |
| `DT` | string | 설계 타입 — `3D`=3-D; `XZ`=X-Z 평면; `YZ`=Y-Z 평면; `XY`=X-Y 평면 | 3D |  |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

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

**Response Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
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
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCTL", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCTL", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCTL", headers=HEADERS)
```

---

## 4. `DESIGN/SRC/AIK-SRC2K/LLRF` — 활하중 저감계수

> **기능:** 활하중 저감계수(부재 지지 층수/영향면적 기반)를 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/LLRF
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
                      "...(전체 11개)"
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
                      "...(전체 11개)"
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `CALC_RULE` | integer | — `0`=일반 설계 기준; `1`=중국 표준 기준 | 0 |  |
| `APPLIED_COMP` | array | 적용 성분 선택 | ["AXIAL"] |  |
| `LIVE_LOAD_CASES` | array | 활하중 케이스 이름 (사용자 정의 목록) |  |  |
| `REDUCTION_DATA` | array | 활하중 저감계수 테이블 데이터 |  | O |
| └ `STORY` | string | 층 이름 |  | O |
| └ `XMIN` | number | X 최소 좌표 | 0 |  |
| └ `XMAX` | number | X 최대 좌표 | 0 |  |
| └ `YMIN` | number | Y 최소 좌표 | 0 |  |
| └ `YMAX` | number | Y 최대 좌표 | 0 |  |
| └ `RANGE_MAX` | number | 구간 최대값 (General Design Code 전용) — 가능값 11개: `1` ~ `0.5` | 1 |  |
| └ `RANGE_MIN` | number | 구간 최소값 (General Design Code 전용) — 가능값 11개: `1` ~ `0.5` | 0.5 |  |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

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

**Response Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
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
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LLRF", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LLRF", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LLRF", headers=HEADERS)
```

---

## 5. `DESIGN/SRC/AIK-SRC2K/LCTB` — 비선형 하중케이스 하중기여

> **기능:** 비선형 하중케이스에 대한 하중 기여(Load Contribution)를 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/LCTB
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `NAME` | string | 하중기여 이름 |  | O |
| `DESC` | string | 설명 |  |  |
| `BASE_ITEM` | array | 하중기여 항목 |  | O |
| └ `FACTOR` | number | 계수 |  | O |
| └ `LOAD_CASE_NAME` | string | 하중케이스 이름 |  | O |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Response Body**

```json
{
  "LCTB": {
    "1": {
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
    "2": {
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
    },
    "3": {
      "NAME": "NgLCB8",
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
          "FACTOR": 0.65,
          "LOAD_CASE_NAME": "WX"
        },
        {
          "FACTOR": 0.65,
          "LOAD_CASE_NAME": "WX(A)"
        }
      ]
    },
    "4": {
      "NAME": "NgLCB9",
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
          "FACTOR": 0.65,
          "LOAD_CASE_NAME": "WX"
        },
        {
          "FACTOR": -0.65,
          "LOAD_CASE_NAME": "WX(A)"
        }
      ]
    },
    "5": {
      "NAME": "NgLCB10",
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
          "FACTOR": 0.65,
          "LOAD_CASE_NAME": "WY"
        },
        {
          "FACTOR": 0.65,
          "LOAD_CASE_NAME": "WY(A)"
        }
      ]
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (GET)
payload = {}
res = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LCTB", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LCTB", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LCTB", headers=HEADERS)
```

---

## 6. `DESIGN/SRC/AIK-SRC2K/LENG` — 비지지 길이(L, Lb)

> **기능:** 부재별 비지지 길이(Ly, Lz, Lb)를 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/LENG
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `LY` | number | 비지지 길이 Ly | 0 |  |
| `LZ` | number | 비지지 길이 Lz | 0 |  |
| `LB` | number | 횡방향 비지지 길이 | 0 |  |
| `bNOTUSE` | boolean | 횡방향 비지지 길이 고려 안 함 | false |  |
| `LT` | number | 비틀림 비지지 길이 | 0 |  |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "LZ": 2,
      "LY": 1
    },
    "874": {
      "LY": 1,
      "LZ": 1
    }
  }
}
```

**Response Body**

```json
{
  "LENG": {
    "868": {
      "LY": 1,
      "LZ": 2
    },
    "874": {
      "LY": 1,
      "LZ": 1
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "868": {
            "LZ": 2,
            "LY": 1
        },
        "874": {
            "LY": 1,
            "LZ": 1
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LENG", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LENG", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LENG", headers=HEADERS)
```

---

## 7. `DESIGN/SRC/AIK-SRC2K/KFAC` — 유효좌굴길이계수(K)

> **기능:** 부재별 유효좌굴길이계수(Ky, Kz)를 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/KFAC
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `Ky` | number | Ky | 1 |  |
| `Kz` | number | Kz | 1 |  |
| `Kt` | number | Kt | 1 |  |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "Ky": 1
    },
    "874": {
      "Ky": 2,
      "Kz": 2
    },
    "885": {
      "Kz": 3,
      "Kt": 3
    }
  }
}
```

**Response Body**

```json
{
  "KFAC": {
    "868": {
      "Ky": 1
    },
    "874": {
      "Ky": 2,
      "Kz": 2
    },
    "885": {
      "Kz": 3,
      "Kt": 3
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "868": {
            "Ky": 1
        },
        "874": {
            "Ky": 2,
            "Kz": 2
        },
        "885": {
            "Kz": 3,
            "Kt": 3
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/KFAC", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/KFAC", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/KFAC", headers=HEADERS)
```

---

## 8. `DESIGN/SRC/AIK-SRC2K/LTSR` — 세장비 제한

> **기능:** 부재별 압축/인장 세장비 제한값을 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/LTSR
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `bNOTCHECK` | boolean | 세장비 검토 안 함 | false |  |
| `COMP` | number | 압축재 세장비 제한값 |  | O |
| `TENS` | number | 인장재 세장비 제한값 |  | O |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "COMP": 300,
      "TENS": 200
    },
    "874": {
      "COMP": 300,
      "TENS": 200
    },
    "885": {
      "COMP": 300,
      "TENS": 200
    }
  }
}
```

**Response Body**

```json
{
  "LTSR": {
    "868": {
      "COMP": 300,
      "TENS": 200
    },
    "874": {
      "COMP": 300,
      "TENS": 200
    },
    "885": {
      "COMP": 300,
      "TENS": 200
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "868": {
            "COMP": 300,
            "TENS": 200
        },
        "874": {
            "COMP": 300,
            "TENS": 200
        },
        "885": {
            "COMP": 300,
            "TENS": 200
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LTSR", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LTSR", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LTSR", headers=HEADERS)
```

---

## 9. `DESIGN/SRC/AIK-SRC2K/CMFT` — 등가모멘트 보정계수(Cm)

> **기능:** 부재별 등가모멘트 보정계수(Cm)를 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/CMFT
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `OPT_AUTO` | boolean | 자동 계산 | false |  |
| `CMY` | number | CMy | 0 |  |
| `CMZ` | number | CMz | 0 |  |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "OPT_AUTO": true
    },
    "874": {
      "OPT_AUTO": true
    },
    "885": {
      "CMY": 0.7,
      "CMZ": 0.6
    }
  }
}
```

**Response Body**

```json
{
  "CMFT": {
    "868": {
      "OPT_AUTO": true
    },
    "874": {
      "OPT_AUTO": true
    },
    "885": {
      "CMY": 0.7,
      "CMZ": 0.6
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "868": {
            "OPT_AUTO": true
        },
        "874": {
            "OPT_AUTO": true
        },
        "885": {
            "CMY": 0.7,
            "CMZ": 0.6
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CMFT", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CMFT", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CMFT", headers=HEADERS)
```

---

## 10. `DESIGN/SRC/AIK-SRC2K/FMAG` — 모멘트 확대계수(B1/δb, B2/δs)

> **기능:** 부재별 모멘트 확대계수(B1/δb, B2/δs)를 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/FMAG
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `B1Y_DELTA_BY` | number | B1y - Δby (1차 모멘트 Y) | 1 |  |
| `B1Z_DELTA_BZ` | number | B1z - Δbz (1차 모멘트 Z) | 1 |  |
| `B2Y_DELTA_SY` | number | B2y - Δsy (2차 모멘트 Y) | 1 |  |
| `B2Z_DELTA_SZ` | number | B2z - Δsz (2차 모멘트 Z) | 1 |  |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2
    },
    "874": {
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    },
    "885": {
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1.3
    }
  }
}
```

**Response Body**

```json
{
  "FMAG": {
    "868": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2
    },
    "874": {
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    },
    "885": {
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1.3
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "868": {
            "B1Y_DELTA_BY": 1.1,
            "B1Z_DELTA_BZ": 1.2
        },
        "874": {
            "B2Y_DELTA_SY": 1.3,
            "B2Z_DELTA_SZ": 1.4
        },
        "885": {
            "B1Z_DELTA_BZ": 1.2,
            "B2Y_DELTA_SY": 1.3
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/FMAG", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/FMAG", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/FMAG", headers=HEADERS)
```

---

## 11. `DESIGN/SRC/AIK-SRC2K/MLLR` — 활하중 저감계수 수정

> **기능:** 부재별 활하중 저감계수를 수정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MLLR
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `FACTOR` | number | 저감계수 | 1 |  |
| `COMPONENTS` | object | 적용 성분 |  |  |
| └ `AXIAL` | boolean | 축력 | false |  |
| └ `MOMENT` | boolean | 모멘트 | false |  |
| └ `SHEAR` | boolean | 전단력 | false |  |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "COMPONENTS": {
        "AXIAL": false,
        "MOMENT": true,
        "SHEAR": false
      }
    },
    "874": {
      "FACTOR": 0.9,
      "COMPONENTS": {
        "AXIAL": true,
        "SHEAR": false
      }
    }
  }
}
```

**Response Body**

```json
{
  "MLLR": {
    "868": {
      "COMPONENTS": {
        "AXIAL": false,
        "MOMENT": true,
        "SHEAR": false
      }
    },
    "874": {
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "868": {
            "COMPONENTS": {
                "AXIAL": false,
                "MOMENT": true,
                "SHEAR": false
            }
        },
        "874": {
            "FACTOR": 0.9,
            "COMPONENTS": {
                "AXIAL": true,
                "SHEAR": false
            }
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MLLR", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MLLR", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MLLR", headers=HEADERS)
```

---

## 12. `DESIGN/SRC/AIK-SRC2K/SUEQ` — 지진 스케일업 계수

> **기능:** 지진하중에 대한 스케일업 계수를 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/SUEQ
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `LC_AXIAL` | number | 하중케이스 - 축력 증폭계수 | 1 |  |
| `LC_MOMENT` | number | 하중케이스 - 모멘트 증폭계수 | 1 |  |
| `LC_SHEAR` | number | 하중케이스 - 전단 증폭계수 | 1 |  |
| `LCOM_AXIAL` | number | 하중조합 - 축력 증폭계수 | 1 |  |
| `LCOM_MOMENT` | number | 하중조합 - 모멘트 증폭계수 | 1 |  |
| `LCOM_SHEAR` | number | 하중조합 - 전단 증폭계수 | 1 |  |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "874": {
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    }
  }
}
```

**Response Body**

```json
{
  "SUEQ": {
    "868": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "874": {
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "868": {
            "LC_AXIAL": 1.2,
            "LC_MOMENT": 1.2,
            "LC_SHEAR": 1.2,
            "LCOM_AXIAL": 1.2,
            "LCOM_MOMENT": 1.2,
            "LCOM_SHEAR": 1.2
        },
        "874": {
            "LC_SHEAR": 1.2,
            "LCOM_AXIAL": 1.2,
            "LCOM_MOMENT": 1.2,
            "LCOM_SHEAR": 1.2
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/SUEQ", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/SUEQ", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/SUEQ", headers=HEADERS)
```

---

## 13. `DESIGN/SRC/AIK-SRC2K/MBTP` — 부재 타입 수정

> **기능:** 부재의 설계 타입(보/기둥 등)을 수정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MBTP
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `TYPE` | string | 부재 타입 — `COLUMN`=기둥; `BEAM`=보; `BRACE`=가새 |  | O |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "TYPE": "BRACE"
    },
    "874": {
      "TYPE": "COLUMN"
    }
  }
}
```

**Response Body**

```json
{
  "MBTP": {
    "868": {
      "TYPE": "BRACE"
    },
    "874": {
      "TYPE": "COLUMN"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "868": {
            "TYPE": "BRACE"
        },
        "874": {
            "TYPE": "COLUMN"
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MBTP", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MBTP", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MBTP", headers=HEADERS)
```

---

## 14. `DESIGN/SRC/AIK-SRC2K/EQCT` — 지진 하중조합 타입

> **기능:** 지진 하중조합 타입을 설정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/EQCT
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `TYPE` | string | 부재 타입 배정 — `Special Seismic Loads`=특별 지진하중; `Vertical Seismic Forces`=수직 지진력 |  | O |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "TYPE": "Special Seismic Loads"
    },
    "874": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
```

**Response Body**

```json
{
  "EQCT": {
    "868": {
      "TYPE": "Special Seismic Loads"
    },
    "874": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "868": {
            "TYPE": "Special Seismic Loads"
        },
        "874": {
            "TYPE": "Vertical Seismic Forces"
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/EQCT", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/EQCT", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/EQCT", headers=HEADERS)
```

---

## 15. `DESIGN/SRC/AIK-SRC2K/BC-ANAL` — SRC 보 검토 수행

> **기능:** SRC 보 검토(설계 계산)를 수행합니다. POST 전용 액션입니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/BC-ANAL
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
          "description": "Select target type for design calculation. ELEMS: by element numbers, SECTIONS: by section numbers, ALL: all elements.",
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
          }
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `PERFORM_TYPE` | string | 설계 계산 대상 타입 선택. ELEMS: 요소번호별, SECTIONS: 단면번호별, ALL: 전체 요소. — `ALL`=전체 요소; `ELEMS`=요소번호별; `SECTIONS`=단면번호별 | ALL |  |
| `ELEMS` | object | 요소 번호 입력. |  |  |
| └ `KEYS` | array | 개별 ID 지정 |  |  |
| └ `TO` | string | ID 범위 지정 (예: '1to160') |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 구조 그룹 이름 지정 |  |  |
| `SECTIONS` | array | 단면 번호 입력. |  |  |

> 위 필드는 `"Argument"` 객체 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL",
    "ELEMS": {
      "KEYS": [
        922
      ]
    }
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 설계 수행/결과 조회 (POST 액션)
payload = {
    "Argument": {
        "PERFORM_TYPE": "ALL",
        "ELEMS": {
            "KEYS": [
                922
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/BC-ANAL", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 16. `DESIGN/SRC/AIK-SRC2K/BC-TABLE` — SRC 보 검토 테이블

> **기능:** SRC 보 검토 결과 테이블(HEAD/DATA)을 조회합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/BC-TABLE
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
          "description": "Element number input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify each element ID",
              "items": {
                "type": "integer"
              },
              "minItems": 1
            },
            "TO": {
              "type": "string",
              "description": "Specify element ID range (e.g., \"1to160\")"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify structure group name"
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
          "description": "Filter results by checking status",
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
        "TABLE_NAME": {
          "type": "string",
          "description": "Response Table Title",
          "default": "SRC Checking Result"
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting",
          "additionalProperties": false,
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
          "additionalProperties": false,
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
          "description": "Components of SRC Checking Result Table",
          "items": {
            "type": "string",
            "enum": [
              "MEMB",
              "SECT",
              "Span",
              "Section",
              "Bc",
              "...(전체 27개)"
            ]
          }
        }
      }
    }
  }
}
```

### 파라미터

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `TABLE_TYPE` | string | 결과표 타입 — 가능값: `MEMB`, `PROP` |  | O |
| `ELEMS` | object | 요소 번호 입력. |  |  |
| └ `KEYS` | array | 개별 요소 ID 지정 |  |  |
| └ `TO` | string | 요소 ID 범위 지정 (예: "1to160") |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 구조 그룹 이름 지정 |  |  |
| `SECTIONS` | array | 표에 포함할 단면 번호 목록. |  |  |
| `PRI_SORT` | integer | 부재 기준 출력의 정렬 기준 (단면번호 또는 부재번호) — `0`=SECT; `1`=MEMB | 1 |  |
| `RESULT` | integer | 검토 상태로 결과 필터링 — `0`=전체; `1`=OK; `2`=NG | 0 |  |
| `TABLE_NAME` | string | 결과표 제목 | SRC Checking Result |  |
| `EXPORT_PATH` | string | 결과표 저장 경로 |  |  |
| `UNIT` | object | 결과 단위 설정 |  |  |
| └ `FORCE` | string | 힘 단위 |  |  |
| └ `DIST` | string | 길이/거리 단위 |  |  |
| └ `HEAT` | string | 열 단위 |  |  |
| └ `TEMP` | string | 온도 단위 |  |  |
| `STYLES` | object | 결과 숫자 형식 |  |  |
| └ `FORMAT` | string | 숫자 형식 — 가능값: `Default`, `Fixed`, `Scientific`, `General` |  |  |
| └ `PLACE` | integer | 소수 자릿수 |  |  |
| `COMPONENTS` | array | SRC 검토 결과표 구성 항목 |  |  |

> 위 필드는 `"Argument"` 객체 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Span",
      "Section",
      "Bc",
      "Hc",
      "Material",
      "Fy",
      "fc",
      "Fyr",
      "Fys",
      "POS",
      "CHK",
      "AsTop",
      "AsBot",
      "N_M",
      "LCB_N",
      "N_Mrs",
      "Rat_N",
      "P_M",
      "LCB_P",
      "P_Mrs",
      "Rat_P",
      "V",
      "LCB_V",
      "Vrs",
      "Rat_V"
    ],
    "ELEMS": {
      "KEYS": [
        922
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
    "DIST": "MM",
    "HEAD": [
      "MEMB",
      "SECT",
      "Span",
      "Section",
      "Bc",
      "Hc",
      "Material",
      "Fy",
      "fc",
      "Fyr",
      "Fys",
      "POS",
      "CHK",
      "AsTop",
      "AsBot",
      "N_M",
      "LCB_N",
      "N_Mrs",
      "Rat_N",
      "P_M",
      "LCB_P",
      "P_Mrs",
      "Rat_P",
      "V",
      "LCB_V",
      "Vrs",
      "Rat_V"
    ],
    "DATA": [
      [
        "922",
        "3",
        "4460.0",
        "H src200x100x5.5/8, H 200x100x5.5/8",
        "400.00",
        "400.00",
        "SS410",
        "0.4100",
        "0.03000",
        "0.40000",
        "0.40000",
        "I",
        "OK",
        "253.40",
        "774.20",
        "62068.5",
        "7",
        "68471.1",
        "0.91",
        "7082.47",
        "7",
        "105831",
        "0.07",
        "68.6914",
        "7",
        "251.879",
        "0.27"
      ],
      [
        "922",
        "3",
        "4460.0",
        "H src200x100x5.5/8, H 200x100x5.5/8",
        "400.00",
        "400.00",
        "SS410",
        "0.4100",
        "0.03000",
        "0.40000",
        "0.40000",
        "M",
        "OK",
        "397.20",
        "28.100",
        "0.00000",
        "7",
        "78786.7",
        "0.00",
        "43273.9",
        "7",
        "52309.1",
        "0.83",
        "51.2916",
        "7",
        "251.879",
        "0.20"
      ],
      [
        "922",
        "3",
        "4460.0",
        "H src200x100x5.5/8, H 200x100x5.5/8",
        "400.00",
        "400.00",
        "SS410",
        "0.4100",
        "0.03000",
        "0.40000",
        "0.40000",
        "J",
        "OK",
        "573.00",
        "573.00",
        "35970.5",
        "7",
        "91397.9",
        "0.39",
        "25750.1",
        "7",
        "91397.9",
        "0.28",
        "67.3729",
        "7",
        "251.879",
        "0.27"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 설계 수행/결과 조회 (POST 액션)
payload = {
    "Argument": {
        "TABLE_TYPE": "MEMB",
        "PRI_SORT": 1,
        "RESULT": 0,
        "COMPONENTS": [
            "MEMB",
            "SECT",
            "Span",
            "Section",
            "Bc",
            "Hc",
            "Material",
            "Fy",
            "fc",
            "Fyr",
            "Fys",
            "POS",
            "CHK",
            "AsTop",
            "AsBot",
            "N_M",
            "LCB_N",
            "N_Mrs",
            "Rat_N",
            "P_M",
            "LCB_P",
            "P_Mrs",
            "Rat_P",
            "V",
            "LCB_V",
            "Vrs",
            "Rat_V"
        ],
        "ELEMS": {
            "KEYS": [
                922
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/BC-TABLE", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 17. `DESIGN/SRC/AIK-SRC2K/BC-REPORT` — SRC 보 검토 리포트

> **기능:** SRC 보 검토 리포트를 생성/조회합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/BC-REPORT
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
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "description": "Report output mode for element-based report",
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
        "CURRENT_MODE_PROP": {
          "type": "string",
          "description": "Report output mode for property-based report",
          "oneOf": [
            {
              "title": "Graphic (JPG image)",
              "const": "Graphic"
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
          }
        },
        "SECTIONS": {
          "type": "array",
          "description": "List of section numbers to include in the report.",
          "items": {
            "type": "integer"
          }
        },
        "DETAIL_POSITIONS": {
          "type": "object",
          "description": "Print positions for Detail report",
          "properties": {
            "END_I": {
              "type": "boolean",
              "description": "Include End I position",
              "default": true
            },
            "MID": {
              "type": "boolean",
              "description": "Include Mid position",
              "default": false
            },
            "END_J": {
              "type": "boolean",
              "description": "Include End J position",
              "default": false
            }
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `REPORT_TYPE` | string | 보고서 표 타입 — 가능값: `MEMB`, `PROP` |  | O |
| `CURRENT_MODE_MEMB` | string | 요소 기준 보고서의 출력 모드 — `Graphic`=그래픽 (JPG 이미지); `Detail`=상세 (DOC 문서); `Summary`=요약 (TXT 텍스트) |  |  |
| `CURRENT_MODE_PROP` | string | 특성 기준 보고서의 출력 모드 — `Graphic`=그래픽 (JPG 이미지); `Summary`=요약 (TXT 텍스트) |  |  |
| `ELEMS` | object | 요소 번호 입력. |  |  |
| └ `KEYS` | array | 개별 ID 지정 |  |  |
| └ `TO` | string | ID 범위 지정 (예: '1to160') |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 구조 그룹 이름 지정 |  |  |
| `SECTIONS` | array | 보고서에 포함할 단면 번호 목록. |  |  |
| `DETAIL_POSITIONS` | object | 상세 보고서 출력 위치 |  |  |
| └ `END_I` | boolean | I단 위치 포함 | true |  |
| └ `MID` | boolean | 중앙 위치 포함 | false |  |
| └ `END_J` | boolean | J단 위치 포함 | false |  |
| `EXPORT_PATH` | string | 보고서 파일을 저장할 디렉토리 경로 |  | O |
| `OUTPUT_NAME` | string | 출력 파일 기본 이름. 요소가 여러 개인 경우 파일명 앞에 순번과 요소번호가 붙습니다(예: 001_E859_filename.jpg, 002_E1_filename.jpg). |  | O |

> 위 필드는 `"Argument"` 객체 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "GRAPHIC.jpg",
    "CURRENT_MODE_MEMB": "Graphic"
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\GRAPHIC.jpg",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 설계 수행/결과 조회 (POST 액션)
payload = {
    "Argument": {
        "REPORT_TYPE": "MEMB",
        "EXPORT_PATH": "C:\\MIDAS\\Result\\",
        "OUTPUT_NAME": "GRAPHIC.jpg",
        "CURRENT_MODE_MEMB": "Graphic"
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/BC-REPORT", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 18. `DESIGN/SRC/AIK-SRC2K/CC-ANAL` — SRC 기둥 검토 수행

> **기능:** SRC 기둥 검토(설계 계산)를 수행합니다. POST 전용 액션입니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/CC-ANAL
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
          "description": "Select target type for design calculation. ELEMS: by element numbers, SECTIONS: by section numbers, ALL: all elements.",
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
          }
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `PERFORM_TYPE` | string | 설계 계산 대상 타입 선택. ELEMS: 요소번호별, SECTIONS: 단면번호별, ALL: 전체 요소. — `ALL`=전체 요소; `ELEMS`=요소번호별; `SECTIONS`=단면번호별 | ALL |  |
| `ELEMS` | object | 요소 번호 입력. |  |  |
| └ `KEYS` | array | 개별 ID 지정 |  |  |
| └ `TO` | string | ID 범위 지정 (예: '1to160') |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 구조 그룹 이름 지정 |  |  |
| `SECTIONS` | array | 단면 번호 입력. |  |  |

> 위 필드는 `"Argument"` 객체 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL",
    "ELEMS": {
      "KEYS": [
        1062
      ]
    }
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 설계 수행/결과 조회 (POST 액션)
payload = {
    "Argument": {
        "PERFORM_TYPE": "ALL",
        "ELEMS": {
            "KEYS": [
                1062
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CC-ANAL", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 19. `DESIGN/SRC/AIK-SRC2K/CC-TABLE` — SRC 기둥 검토 테이블

> **기능:** SRC 기둥 검토 결과 테이블(HEAD/DATA)을 조회합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/CC-TABLE
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
          "description": "Element number input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify each element ID",
              "items": {
                "type": "integer"
              },
              "minItems": 1
            },
            "TO": {
              "type": "string",
              "description": "Specify element ID range (e.g., \"1to160\")"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify structure group name"
            }
          },
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
            },
            {
              "required": [
                "STRUCTURE_GROUP_NAME"
              ]
            }
          ]
        },
        "SECTIONS": {
          "type": "array",
          "description": "List of section property numbers to include in the table.",
          "items": {
            "type": "integer"
          },
          "minItems": 1
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
          "description": "Filter results by checking status",
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
        "TABLE_NAME": {
          "type": "string",
          "description": "Response Table Title",
          "default": "SRC Column Checking Result"
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting",
          "additionalProperties": false,
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
          "additionalProperties": false,
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
          "description": "Components of SRC Column Checking Result Table (SSRC79 style). SEL is not included.",
          "items": {
            "type": "string",
            "enum": [
              "CHK",
              "MEMB",
              "SECT",
              "COM",
              "SHR",
              "...(전체 31개)"
            ]
          }
        }
      }
    }
  }
}
```

### 파라미터

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `TABLE_TYPE` | string | 결과표 타입 — 가능값: `MEMB`, `PROP` |  | O |
| `ELEMS` | object | 요소 번호 입력. |  |  |
| └ `KEYS` | array | 개별 요소 ID 지정 |  |  |
| └ `TO` | string | 요소 ID 범위 지정 (예: "1to160") |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 구조 그룹 이름 지정 |  |  |
| `SECTIONS` | array | 표에 포함할 단면 특성 번호 목록. |  |  |
| `PRI_SORT` | integer | 부재 기준 출력의 정렬 기준 (단면번호 또는 부재번호) — `0`=SECT; `1`=MEMB | 1 |  |
| `RESULT` | integer | 검토 상태로 결과 필터링 — `0`=전체; `1`=OK; `2`=NG | 0 |  |
| `TABLE_NAME` | string | 결과표 제목 | SRC Column Checking Result |  |
| `EXPORT_PATH` | string | 결과표 저장 경로 |  |  |
| `UNIT` | object | 결과 단위 설정 |  |  |
| └ `FORCE` | string | 힘 단위 |  |  |
| └ `DIST` | string | 길이/거리 단위 |  |  |
| └ `HEAT` | string | 열 단위 |  |  |
| └ `TEMP` | string | 온도 단위 |  |  |
| `STYLES` | object | 결과 숫자 형식 |  |  |
| └ `FORMAT` | string | 숫자 형식 — 가능값: `Default`, `Fixed`, `Scientific`, `General` |  |  |
| └ `PLACE` | integer | 소수 자릿수 |  |  |
| `COMPONENTS` | array | SRC 기둥 검토 결과표 구성 항목 (SSRC79 방식). SEL은 포함되지 않음. |  |  |

> 위 필드는 `"Argument"` 객체 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "COMPONENTS": [
      "CHK",
      "MEMB",
      "SECT",
      "COM",
      "SHR",
      "Type",
      "Rebar",
      "Section",
      "Material",
      "Fys",
      "Fyr",
      "fc",
      "Bc",
      "Hc",
      "LCB",
      "Len",
      "Ly",
      "Lz",
      "Ky",
      "Kz",
      "Cmy",
      "Cmz",
      "Pa",
      "My",
      "Mz",
      "fa",
      "fby",
      "fbz",
      "Fa",
      "FBy",
      "FBz"
    ],
    "ELEMS": {
      "KEYS": [
        1062
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
    "DIST": "MM",
    "HEAD": [
      "CHK",
      "MEMB",
      "SECT",
      "COM",
      "SHR",
      "Type",
      "Rebar",
      "Section",
      "Material",
      "Fys",
      "Fyr",
      "fc",
      "Bc",
      "Hc",
      "LCB",
      "Len",
      "Ly",
      "Lz",
      "Ky",
      "Kz",
      "Cmy",
      "Cmz",
      "Pa",
      "My",
      "Mz",
      "fa",
      "fby",
      "fbz",
      "Fa",
      "FBy",
      "FBz"
    ],
    "DATA": [
      [
        "OK",
        "1062",
        "4",
        "0.394",
        "0.039",
        "RHB",
        "4-2-D4",
        "C src200x100x5.5/8, H 200x100x5.5/8",
        "SS410",
        "0.41000",
        "0.40000",
        "0.03000",
        "400.00",
        "400.00",
        "7",
        "4512.08",
        "4512.08",
        "4512.08",
        "1.000",
        "1.000",
        "0.850",
        "0.850",
        "-651.51",
        "26932.7",
        "2822.88",
        "0.2399",
        "0.0700",
        "0.0124",
        "0.7894",
        "0.2733",
        "0.2733"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 설계 수행/결과 조회 (POST 액션)
payload = {
    "Argument": {
        "TABLE_TYPE": "MEMB",
        "PRI_SORT": 1,
        "RESULT": 0,
        "COMPONENTS": [
            "CHK",
            "MEMB",
            "SECT",
            "COM",
            "SHR",
            "Type",
            "Rebar",
            "Section",
            "Material",
            "Fys",
            "Fyr",
            "fc",
            "Bc",
            "Hc",
            "LCB",
            "Len",
            "Ly",
            "Lz",
            "Ky",
            "Kz",
            "Cmy",
            "Cmz",
            "Pa",
            "My",
            "Mz",
            "fa",
            "fby",
            "fbz",
            "Fa",
            "FBy",
            "FBz"
        ],
        "ELEMS": {
            "KEYS": [
                1062
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CC-TABLE", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 20. `DESIGN/SRC/AIK-SRC2K/CC-REPORT` — SRC 기둥 검토 리포트

> **기능:** SRC 기둥 검토 리포트를 생성/조회합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/CC-REPORT
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
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "description": "Report output mode for element-based report",
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
        "CURRENT_MODE_PROP": {
          "type": "string",
          "description": "Report output mode for property-based report",
          "oneOf": [
            {
              "title": "Graphic (JPG image)",
              "const": "Graphic"
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
          }
        },
        "SECTIONS": {
          "type": "array",
          "description": "List of section numbers to include in the report.",
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
          "description": "Output file base name. For multiple elements, files are prefixed with index and element number (e.g. 001_E100_filename.jpg, 002_E865_filename.jpg)"
        }
      }
    }
  }
}
```

### 파라미터

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `REPORT_TYPE` | string | 보고서 표 타입 — 가능값: `MEMB`, `PROP` |  | O |
| `CURRENT_MODE_MEMB` | string | 요소 기준 보고서의 출력 모드 — `Graphic`=그래픽 (JPG 이미지); `Detail`=상세 (DOC 문서); `Summary`=요약 (TXT 텍스트) |  |  |
| `CURRENT_MODE_PROP` | string | 특성 기준 보고서의 출력 모드 — `Graphic`=그래픽 (JPG 이미지); `Summary`=요약 (TXT 텍스트) |  |  |
| `ELEMS` | object | 요소 번호 입력. |  |  |
| └ `KEYS` | array | 개별 ID 지정 |  |  |
| └ `TO` | string | ID 범위 지정 (예: '1to160') |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 구조 그룹 이름 지정 |  |  |
| `SECTIONS` | array | 보고서에 포함할 단면 번호 목록. |  |  |
| `EXPORT_PATH` | string | 보고서 파일을 저장할 디렉토리 경로 |  | O |
| `OUTPUT_NAME` | string | 출력 파일 기본 이름. 요소가 여러 개인 경우 파일명 앞에 순번과 요소번호가 붙습니다(예: 001_E100_filename.jpg, 002_E865_filename.jpg). |  | O |

> 위 필드는 `"Argument"` 객체 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "Detail.txt",
    "ELEMS": {
      "KEYS": [
        1062
      ]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\Detail.txt",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 설계 수행/결과 조회 (POST 액션)
payload = {
    "Argument": {
        "REPORT_TYPE": "MEMB",
        "CURRENT_MODE_MEMB": "Detail",
        "EXPORT_PATH": "C:\\MIDAS\\Result\\",
        "OUTPUT_NAME": "Detail.txt",
        "ELEMS": {
            "KEYS": [
                1062
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CC-REPORT", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 21. `DESIGN/SRC/AIK-SRC2K/OCHECK` — SRC 최적 설계

> **기능:** SRC 최적 설계(Optimal Design)를 수행합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/OCHECK
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
      "additionalProperties": false,
      "required": [
        "SECT_LIST",
        "OUTPUT"
      ],
      "properties": {
        "SECT_LIST": {
          "type": "array",
          "description": "Section List & Design Criteria (SRC). Each item corresponds to one Section No entry and its design criteria (POST input only).",
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "SECT_NO",
              "SECT_DB"
            ],
            "properties": {
              "SECT_NO": {
                "type": "integer",
                "description": "Section Number (input)."
              },
              "SECT_DB": {
                "type": "string",
                "description": "Design Criteria - SectDB",
                "oneOf": [
                  {
                    "title": "BUILT (Welded sections)",
                    "const": "BUILT"
                  },
                  {
                    "title": "KS21 (Korean Standard rolled sections)",
                    "const": "KS21"
                  },
                  {
                    "title": "USER (User-defined sections)",
                    "const": "USER"
                  }
                ]
              },
              "ALLOW": {
                "type": "number",
                "description": "Design Criteria - Allow",
                "default": 1
              },
              "D1": {
                "type": "number",
                "description": "Design Criteria - D1",
                "default": 0
              },
              "D2": {
                "type": "number",
                "description": "Design Criteria - D2",
                "default": 0
              },
              "D3": {
                "type": "number",
                "description": "Design Criteria - D3",
                "default": 0
              },
              "D4": {
                "type": "number",
                "description": "Design Criteria - D4",
                "default": 0
              },
              "D5": {
                "type": "number",
                "description": "Design Criteria - D5",
                "default": 0
              },
              "D6": {
                "type": "number",
                "description": "Design Criteria - D6",
                "default": 0
              }
            }
          }
        },
        "ANALYSIS_OPT": {
          "type": "object",
          "description": "Analysis option - number of re-analysis iterations",
          "additionalProperties": false,
          "properties": {
            "ANAL_TIME": {
              "type": "integer",
              "description": "Number of re-analysis iterations (max 10). Set 0 for section selection only without re-analysis.",
              "default": 1,
              "minimum": 0,
              "maximum": 10
            }
          }
        },
        "PLATE_THICKNESS": {
          "type": "array",
          "description": "Plate thickness list for BUILT sections (max 50 entries)",
          "items": {
            "type": "number"
          }
        },
        "COLUMN_DESIGN": {
          "type": "object",
          "description": "Column design settings for optimal design of column members",
          "additionalProperties": false,
          "properties": {
            "APPLIED_FORCES": {
              "type": "integer",
              "description": "Applied forces and moments method for column design",
              "default": 0,
              "oneOf": [
                {
                  "title": "Axial Forces and Moments",
                  "const": 0
                },
                {
                  "title": "Axial Forces Only",
                  "const": 1
                }
              ]
            },
            "JOINT_METHOD": {
              "type": "integer",
              "description": "Joint method of built-up column splices",
              "default": 1,
              "oneOf": [
                {
                  "title": "Internal Const (Fixed inside, expand outward)",
                  "const": 0
                },
                {
                  "title": "External Const (Fixed outside, adjust inward)",
                  "const": 1
                }
              ]
            }
          }
        },
        "USER_DEFINED_SECT": {
          "type": "array",
          "description": "User-defined section database. Each row defines a section with No, Shape, and dimensions D1-D6.",
          "items": {
            "type": "object",
            "required": [
              "NO",
              "SHAPE"
            ],
            "additionalProperties": false,
            "properties": {
              "NO": {
                "type": "integer",
                "description": "Section No."
              },
              "SHAPE": {
                "type": "string",
                "description": "Section shape (L, C, H, T, B, P, SR, SB, 2L, 2C)"
              },
              "D1": {
                "type": "number",
                "default": 0
              },
              "D2": {
                "type": "number",
                "default": 0
              },
              "D3": {
                "type": "number",
                "default": 0
              },
              "D4": {
                "type": "number",
                "default": 0
              },
              "D5": {
                "type": "number",
                "default": 0
              },
              "D6": {
                "type": "number",
                "default": 0
              }
            }
          }
        },
        "OUTPUT": {
          "type": "object",
          "description": "Output options for optimal design results (can select multiple simultaneously)",
          "required": [
            "EXPORT_PATH"
          ],
          "additionalProperties": false,
          "properties": {
            "GRAPH_MAX_RATIO": {
              "type": "boolean",
              "description": "Output Max. Ratio graph",
              "default": true
            },
            "GRAPH_AVG_RATIO": {
              "type": "boolean",
              "description": "Output Average Ratio graph",
              "default": true
            },
            "GRAPH_WEIGHT": {
              "type": "boolean",
              "description": "Output Weight graph",
              "default": true
            },
            "GRAPH_WEIGHT_SUM": {
              "type": "boolean",
              "description": "Output Weight Sum graph",
              "default": true
            },
            "GRAPH_WEIGHT_RATIO": {
              "type": "boolean",
              "description": "Output Weight Ratio graph",
              "default": true
            },
            "TEXT_REPORT": {
              "type": "boolean",
              "description": "Output results as text report to screen and file",
              "default": true
            },
            "MODEL_UPDATE": {
              "type": "boolean",
              "description": "Apply selected optimal sections to the model",
              "default": true
            },
            "EXPORT_PATH": {
              "type": "string",
              "description": "File path to save report output"
            }
          }
        }
      }
    }
  }
}
```

### 파라미터

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `SECT_LIST` | array | 단면 목록 및 설계 기준(SRC). 각 항목은 하나의 단면번호와 그 설계 기준에 대응합니다(POST 입력 전용). |  | O |
| └ `SECT_NO` | integer | 단면 번호(입력). |  | O |
| └ `SECT_DB` | string | 설계 기준 - 단면 DB — `BUILT`=BUILT (용접 단면); `KS21`=KS21 (한국산업표준 압연 단면); `USER`=USER (사용자 정의 단면) |  | O |
| └ `ALLOW` | number | 설계 기준 - 허용치 | 1 |  |
| └ `D1` | number | 설계 기준 - D1 | 0 |  |
| └ `D2` | number | 설계 기준 - D2 | 0 |  |
| └ `D3` | number | 설계 기준 - D3 | 0 |  |
| └ `D4` | number | 설계 기준 - D4 | 0 |  |
| └ `D5` | number | 설계 기준 - D5 | 0 |  |
| └ `D6` | number | 설계 기준 - D6 | 0 |  |
| `ANALYSIS_OPT` | object | 해석 옵션 - 재해석 반복 횟수 |  |  |
| └ `ANAL_TIME` | integer | 재해석 반복 횟수(최대 10). 재해석 없이 단면 선정만 할 경우 0으로 설정. | 1 |  |
| `PLATE_THICKNESS` | array | BUILT 단면의 플레이트 두께 목록 (최대 50개) |  |  |
| `COLUMN_DESIGN` | object | 기둥 부재 최적설계를 위한 기둥 설계 설정 |  |  |
| └ `APPLIED_FORCES` | integer | 기둥 설계용 적용 부재력·모멘트 방법 — `0`=축력 및 모멘트; `1`=축력만 | 0 |  |
| └ `JOINT_METHOD` | integer | 조립기둥 이음 접합 방법 — `0`=Internal Const (내측 고정, 외측으로 확장); `1`=External Const (외측 고정, 내측 조정) | 1 |  |
| `USER_DEFINED_SECT` | array | 사용자 정의 단면 데이터베이스. 각 행은 No, 형상, 치수 D1~D6으로 단면을 정의함. |  |  |
| └ `NO` | integer | 단면 번호 |  | O |
| └ `SHAPE` | string | 단면 형상 (L, C, H, T, B, P, SR, SB, 2L, 2C) |  | O |
| └ `D1` | number |  | 0 |  |
| └ `D2` | number |  | 0 |  |
| └ `D3` | number |  | 0 |  |
| └ `D4` | number |  | 0 |  |
| └ `D5` | number |  | 0 |  |
| └ `D6` | number |  | 0 |  |
| `OUTPUT` | object | 최적설계 결과 출력 옵션 (동시에 여러 개 선택 가능) |  | O |
| └ `GRAPH_MAX_RATIO` | boolean | 최대 비율 그래프 출력 | true |  |
| └ `GRAPH_AVG_RATIO` | boolean | 평균 비율 그래프 출력 | true |  |
| └ `GRAPH_WEIGHT` | boolean | 중량 그래프 출력 | true |  |
| └ `GRAPH_WEIGHT_SUM` | boolean | 중량 합계 그래프 출력 | true |  |
| └ `GRAPH_WEIGHT_RATIO` | boolean | 중량 비율 그래프 출력 | true |  |
| └ `TEXT_REPORT` | boolean | 결과를 텍스트 보고서로 화면 및 파일에 출력 | true |  |
| └ `MODEL_UPDATE` | boolean | 선택된 최적 단면을 모델에 적용 | true |  |
| └ `EXPORT_PATH` | string | 보고서 출력을 저장할 파일 경로 |  | O |

> 위 필드는 `"Argument"` 객체 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "SECT_LIST": [
      {
        "SECT_NO": 4,
        "SECT_DB": "KS21",
        "ALLOW": 1,
        "D1": 0,
        "D2": 0,
        "D3": 0,
        "D4": 0,
        "D5": 0,
        "D6": 0
      }
    ],
    "OUTPUT": {
      "GRAPH_MAX_RATIO": true,
      "GRAPH_AVG_RATIO": true,
      "GRAPH_WEIGHT": true,
      "GRAPH_WEIGHT_SUM": true,
      "GRAPH_WEIGHT_RATIO": true,
      "TEXT_REPORT": true,
      "MODEL_UPDATE": true,
      "EXPORT_PATH": "C:\\MIDAS\\Result\\"
    }
  }
}
```

**Response Body**

```json
{
  "ODSR_RUN_RESPONSE": {
    "FORCE": "KN",
    "DIST": "MM",
    "HEAD": [
      "No",
      "Name",
      "SteelSize",
      "Astl",
      "COM",
      "Axial",
      "Ben-y",
      "Ben-z",
      "Shear"
    ],
    "DATA": [
      [
        "4",
        "C src200x100x5.5/8",
        "LH 150x75x3.2/4.5",
        "1126.00",
        "0.511",
        "0.339",
        "0.330",
        "0.047",
        "0.086"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 설계 수행/결과 조회 (POST 액션)
payload = {
    "Argument": {
        "SECT_LIST": [
            {
                "SECT_NO": 4,
                "SECT_DB": "KS21",
                "ALLOW": 1,
                "D1": 0,
                "D2": 0,
                "D3": 0,
                "D4": 0,
                "D5": 0,
                "D6": 0
            }
        ],
        "OUTPUT": {
            "GRAPH_MAX_RATIO": true,
            "GRAPH_AVG_RATIO": true,
            "GRAPH_WEIGHT": true,
            "GRAPH_WEIGHT_SUM": true,
            "GRAPH_WEIGHT_RATIO": true,
            "TEXT_REPORT": true,
            "MODEL_UPDATE": true,
            "EXPORT_PATH": "C:\\MIDAS\\Result\\"
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/OCHECK", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 22. `DESIGN/SRC/AIK-SRC2K/TABLE` — SRC 보 설계력

> **기능:** SRC 보 설계력(Design Forces) 테이블을 조회합니다. URI는 `TABLE` 공용이며 `TABLE_TYPE`=`SRCBEAMDESIGNFORCES`로 구분합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/TABLE
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
            "SRCBEAMDESIGNFORCES"
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
              "Memb",
              "Part",
              "LComName",
              "Type",
              "Fz",
              "Mx",
              "My(+)",
              "My(-)"
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
          }
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `TABLE_NAME` | string | 결과표 제목 |  |  |
| `TABLE_TYPE` | string | 결과표 타입 — 가능값: `SRCBEAMDESIGNFORCES` |  | O |
| `EXPORT_PATH` | string | 결과표 저장 경로 |  |  |
| `UNIT` | object | 결과 단위 설정 | System |  |
| └ `FORCE` | string | 힘 단위 |  |  |
| └ `DIST` | string | 길이/거리 단위 |  |  |
| └ `HEAT` | string | 열 단위 |  |  |
| └ `TEMP` | string | 온도 단위 |  |  |
| `STYLES` | object | 결과 숫자 형식 | System |  |
| └ `FORMAT` | string | 숫자 형식 — 가능값: `Default`, `Fixed`, `Scientific`, `General` |  |  |
| └ `PLACE` | integer | 소수 자릿수 |  |  |
| `COMPONENTS` | array | 결과표 구성 항목 |  |  |
| `NODE_ELEMS` | object | 절점/요소 번호 입력 |  |  |
| └ `KEYS` | array | 개별 ID 지정 |  |  |
| └ `TO` | string | ID 범위 지정 (예: '1to160') |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 구조 그룹 이름 지정 |  |  |
| `PARTS` | array | 요소 파트 번호 | ["All"] |  |

> 위 필드는 `"Argument"` 객체 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "SRCBEAMDESIGNFORCES",
    "COMPONENTS": [
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fz",
      "Mx",
      "My(+)",
      "My(-)"
    ],
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        926
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
    "DIST": "MM",
    "HEAD": [
      "Index",
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fz",
      "Mx",
      "My(+)",
      "My(-)"
    ],
    "DATA": [
      [
        "1",
        "926",
        "I",
        "gLCB5",
        "Max",
        "1.2976",
        "0.0000",
        "349.6767",
        "0.0000"
      ],
      [
        "2",
        "926",
        "I",
        "gLCB6",
        "Max",
        "1.3023",
        "0.0000",
        "364.0208",
        "0.0000"
      ],
      [
        "3",
        "926",
        "I",
        "gLCB7",
        "Max",
        "1.8279",
        "0.0000",
        "548.4875",
        "0.0000"
      ],
      [
        "4",
        "926",
        "J",
        "gLCB5",
        "Max",
        "1.5838",
        "0.0000",
        "341.5056",
        "0.0000"
      ],
      [
        "5",
        "926",
        "J",
        "gLCB6",
        "Max",
        "1.9019",
        "0.0000",
        "338.3354",
        "0.0000"
      ],
      [
        "6",
        "926",
        "J",
        "gLCB7",
        "Max",
        "2.3987",
        "0.0000",
        "535.9536",
        "0.0000"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 설계 수행/결과 조회 (POST 액션)
payload = {
    "Argument": {
        "TABLE_TYPE": "SRCBEAMDESIGNFORCES",
        "COMPONENTS": [
            "Memb",
            "Part",
            "LComName",
            "Type",
            "Fz",
            "Mx",
            "My(+)",
            "My(-)"
        ],
        "PARTS": [
            "PartI",
            "PartJ"
        ],
        "NODE_ELEMS": {
            "KEYS": [
                926
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/TABLE", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 23. `DESIGN/SRC/AIK-SRC2K/TABLE` — SRC 기둥 설계력

> **기능:** SRC 기둥 설계력(Design Forces) 테이블을 조회합니다. URI는 `TABLE` 공용이며 `TABLE_TYPE`=`SRCCOLUMNDESIGNFORCES`로 구분합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/TABLE
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
            "SRCCOLUMNDESIGNFORCES"
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
              "Memb",
              "Part",
              "LComName",
              "Type",
              "Fx",
              "...(전체 10개)"
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
          }
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `TABLE_NAME` | string | 결과표 제목 |  |  |
| `TABLE_TYPE` | string | 결과표 타입 — 가능값: `SRCCOLUMNDESIGNFORCES` |  | O |
| `EXPORT_PATH` | string | 결과표 저장 경로 |  |  |
| `UNIT` | object | 결과 단위 설정 | System |  |
| └ `FORCE` | string | 힘 단위 |  |  |
| └ `DIST` | string | 길이/거리 단위 |  |  |
| └ `HEAT` | string | 열 단위 |  |  |
| └ `TEMP` | string | 온도 단위 |  |  |
| `STYLES` | object | 결과 숫자 형식 | System |  |
| └ `FORMAT` | string | 숫자 형식 — 가능값: `Default`, `Fixed`, `Scientific`, `General` |  |  |
| └ `PLACE` | integer | 소수 자릿수 |  |  |
| `COMPONENTS` | array | 결과표 구성 항목 |  |  |
| `NODE_ELEMS` | object | 절점/요소 번호 입력 |  |  |
| └ `KEYS` | array | 개별 ID 지정 |  |  |
| └ `TO` | string | ID 범위 지정 (예: '1to160') |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 구조 그룹 이름 지정 |  |  |
| `PARTS` | array | 요소 파트 번호 | ["All"] |  |

> 위 필드는 `"Argument"` 객체 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "SRCCOLUMNDESIGNFORCES",
    "COMPONENTS": [],
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1062
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
    "DIST": "MM",
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
        "1062",
        "I",
        "gLCB5",
        "Max",
        "-471.0683",
        "-0.3080",
        "-3.9955",
        "0.0000",
        "-0.0044",
        "-570.8548"
      ],
      [
        "2",
        "1062",
        "I",
        "gLCB6",
        "Max",
        "-527.5717",
        "-0.2221",
        "-5.1406",
        "0.0000",
        "-0.0058",
        "-547.2386"
      ],
      [
        "3",
        "1062",
        "I",
        "gLCB7",
        "Max",
        "-672.6419",
        "-1.0422",
        "-6.7439",
        "0.0000",
        "-0.0077",
        "-1879.5452"
      ],
      [
        "4",
        "1062",
        "J",
        "gLCB5",
        "Max",
        "-446.4142",
        "-0.3080",
        "-2.1875",
        "0.0000",
        "13949.2064",
        "818.9043"
      ],
      [
        "5",
        "1062",
        "J",
        "gLCB6",
        "Max",
        "-506.4395",
        "-0.2221",
        "-3.5909",
        "0.0000",
        "19698.7242",
        "454.9329"
      ],
      [
        "6",
        "1062",
        "J",
        "gLCB7",
        "Max",
        "-651.5098",
        "-1.0422",
        "-5.1942",
        "0.0000",
        "26932.6614",
        "2822.8793"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 설계 수행/결과 조회 (POST 액션)
payload = {
    "Argument": {
        "TABLE_TYPE": "SRCCOLUMNDESIGNFORCES",
        "COMPONENTS": [],
        "PARTS": [
            "PartI",
            "PartJ"
        ],
        "NODE_ELEMS": {
            "KEYS": [
                1062
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/TABLE", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 24. `DESIGN/SRC/AIK-SRC2K/MATD` — SRC 재료 수정

> **기능:** SRC 재료(콘크리트/강재 등급)를 수정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MATD
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
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "STEEL",
            "CONCRETE",
            "REINFORCEMENT"
          ],
          "additionalProperties": false,
          "properties": {
            "STEEL": {
              "type": "object",
              "description": "Steel material selection.",
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
                    "...(전체 68개)"
                  ]
                },
                "NAME": {
                  "type": "string",
                  "description": "User-defined steel material name when CODE is None."
                },
                "ES": {
                  "type": "number",
                  "description": "Modulus of Elasticity. User input when CODE is None. Auto-filled when CODE is Standard."
                },
                "FU": {
                  "type": "number",
                  "description": "Tensile Strength. User input when CODE is None. Auto-filled when CODE is Standard."
                },
                "FY": {
                  "type": "number",
                  "description": "Yield Strength for CODE=None."
                },
                "FY1": {
                  "type": "number",
                  "description": "Yield Strength Fy1. Auto-filled when CODE is Standard."
                },
                "FY2": {
                  "type": "number",
                  "description": "Yield Strength Fy2. Auto-filled when CODE is Standard."
                },
                "FY3": {
                  "type": "number",
                  "description": "Yield Strength Fy3. Auto-filled when CODE is Standard."
                },
                "FY4": {
                  "type": "number",
                  "description": "Yield Strength Fy4. Auto-filled when CODE is Standard."
                },
                "FY5": {
                  "type": "number",
                  "description": "Yield Strength Fy5. Auto-filled when CODE is Standard."
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
                      "FU",
                      "FY"
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
            },
            "CONCRETE": {
              "type": "object",
              "description": "Concrete material selection.",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Concrete material code type.",
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
                  "description": "Concrete standard code when CODE is Standard. Currently only KS19(RC) is supported.",
                  "oneOf": [
                    {
                      "const": "KS19(RC)",
                      "title": "KS19(RC)"
                    }
                  ]
                },
                "NAME": {
                  "type": "string",
                  "description": "User-defined concrete material name when CODE is None."
                },
                "GRADE": {
                  "type": "string",
                  "description": "Concrete grade when CODE is Standard.",
                  "oneOf": [
                    {
                      "const": "C15",
                      "title": "C15"
                    },
                    {
                      "const": "C18",
                      "title": "C18"
                    },
                    {
                      "const": "C21",
                      "title": "C21"
                    },
                    {
                      "const": "C24",
                      "title": "C24"
                    },
                    {
                      "const": "C27",
                      "title": "C27"
                    },
                    "...(전체 20개)"
                  ]
                },
                "FC": {
                  "type": "number",
                  "description": "Specified Compressive Strength. User input when CODE is None. Auto-filled when CODE is Standard."
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
                      "FC"
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
            },
            "REINFORCEMENT": {
              "type": "object",
              "description": "Reinforcement material selection.",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Reinforcement code type.",
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
                  "description": "Reinforcement standard code when CODE is Standard. Currently only KS19(RC) is supported.",
                  "oneOf": [
                    {
                      "const": "KS19(RC)",
                      "title": "KS19(RC)"
                    }
                  ]
                },
                "MAIN_REBAR_NAME": {
                  "type": "string",
                  "description": "User-defined main rebar name when CODE is None."
                },
                "MAIN_REBAR_GRADE": {
                  "type": "string",
                  "description": "Grade of main rebar when CODE is Standard.",
                  "oneOf": [
                    {
                      "const": "SD300",
                      "title": "SD300"
                    },
                    {
                      "const": "SD400",
                      "title": "SD400"
                    },
                    {
                      "const": "SD500",
                      "title": "SD500"
                    },
                    {
                      "const": "SD600",
                      "title": "SD600"
                    },
                    {
                      "const": "SD700",
                      "title": "SD700"
                    },
                    {
                      "const": "SD400S",
                      "title": "SD400S"
                    },
                    {
                      "const": "SD500S",
                      "title": "SD500S"
                    },
                    {
                      "const": "SD600S",
                      "title": "SD600S"
                    }
                  ]
                },
                "FYR": {
                  "type": "number",
                  "description": "Yield Strength of main rebar. User input when CODE is None. Auto-filled when CODE is Standard."
                },
                "SUB_REBAR_NAME": {
                  "type": "string",
                  "description": "User-defined sub-rebar name when CODE is None."
                },
                "SUB_REBAR_GRADE": {
                  "type": "string",
                  "description": "Grade of sub-rebar when CODE is Standard.",
                  "oneOf": [
                    {
                      "const": "SD300",
                      "title": "SD300"
                    },
                    {
                      "const": "SD400",
                      "title": "SD400"
                    },
                    {
                      "const": "SD500",
                      "title": "SD500"
                    },
                    {
                      "const": "SD600",
                      "title": "SD600"
                    },
                    {
                      "const": "SD700",
                      "title": "SD700"
                    },
                    {
                      "const": "SD400S",
                      "title": "SD400S"
                    },
                    {
                      "const": "SD500S",
                      "title": "SD500S"
                    },
                    {
                      "const": "SD600S",
                      "title": "SD600S"
                    }
                  ]
                },
                "FYS": {
                  "type": "number",
                  "description": "Yield Strength of sub-rebar. User input when CODE is None. Auto-filled when CODE is Standard."
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
                      "MAIN_REBAR_NAME",
                      "FYR",
                      "SUB_REBAR_NAME",
                      "FYS"
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
                      "MAIN_REBAR_GRADE",
                      "SUB_REBAR_GRADE"
                    ]
                  }
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `STEEL` | object | 강재 재질 선택. |  | O |
| └ `CODE` | string | 강재 재질 코드 타입. — `None`=없음; `Standard`=표준 |  | O |
| └ `STANDARD_CODE` | string | CODE가 Standard일 때의 강재 표준 코드. 현재 KS22(S)만 지원됨. — `KS22(S)`=KS22(S) |  |  |
| └ `GRADE` | string | CODE가 Standard일 때의 강재 등급. — `SS235`=SS235; `SS275`=SS275; `SS315`=SS315; `SS410`=SS410; `SS450`=SS450; `SS550`=SS550; `SM275`=SM275; `SM355`=SM355; `SM420`=SM420; `SM460`=SM460; `SM275TMC`=SM275TMC; `SM355TMC`=SM355TMC …(전체 68개) |  |  |
| └ `NAME` | string | CODE가 None일 때의 사용자 정의 강재 이름. |  |  |
| └ `ES` | number | 탄성계수. CODE가 None일 때 사용자 입력. CODE가 Standard일 때 자동 입력. |  |  |
| └ `FU` | number | 인장강도. CODE가 None일 때 사용자 입력. CODE가 Standard일 때 자동 입력. |  |  |
| └ `FY` | number | CODE=None일 때의 항복강도. |  |  |
| └ `FY1` | number | 항복강도 Fy1. CODE가 Standard일 때 자동 입력. |  |  |
| └ `FY2` | number | 항복강도 Fy2. CODE가 Standard일 때 자동 입력. |  |  |
| └ `FY3` | number | 항복강도 Fy3. CODE가 Standard일 때 자동 입력. |  |  |
| └ `FY4` | number | 항복강도 Fy4. CODE가 Standard일 때 자동 입력. |  |  |
| └ `FY5` | number | 항복강도 Fy5. CODE가 Standard일 때 자동 입력. |  |  |
| `CONCRETE` | object | 콘크리트 재질 선택. |  | O |
| └ `CODE` | string | 콘크리트 재질 코드 타입. — `None`=없음; `Standard`=표준 |  | O |
| └ `STANDARD_CODE` | string | CODE가 Standard일 때의 콘크리트 표준 코드. 현재 KS19(RC)만 지원됨. — `KS19(RC)`=KS19(RC) |  |  |
| └ `NAME` | string | CODE가 None일 때의 사용자 정의 콘크리트 재질 이름. |  |  |
| └ `GRADE` | string | CODE가 Standard일 때의 콘크리트 등급. — `C15`=C15; `C18`=C18; `C21`=C21; `C24`=C24; `C27`=C27; `C30`=C30; `C35`=C35; `C40`=C40; `C45`=C45; `C49`=C49; `C50`=C50; `C55`=C55 …(전체 20개) |  |  |
| └ `FC` | number | 설계기준압축강도. CODE가 None일 때 사용자 입력. CODE가 Standard일 때 자동 입력. |  |  |
| `REINFORCEMENT` | object | 철근 재질 선택. |  | O |
| └ `CODE` | string | 철근 코드 타입. — `None`=없음; `Standard`=표준 |  | O |
| └ `STANDARD_CODE` | string | CODE가 Standard일 때의 철근 표준 코드. 현재 KS19(RC)만 지원됨. — `KS19(RC)`=KS19(RC) |  |  |
| └ `MAIN_REBAR_NAME` | string | CODE가 None일 때의 사용자 정의 주철근 이름. |  |  |
| └ `MAIN_REBAR_GRADE` | string | CODE가 Standard일 때의 주철근 등급. — `SD300`=SD300; `SD400`=SD400; `SD500`=SD500; `SD600`=SD600; `SD700`=SD700; `SD400S`=SD400S; `SD500S`=SD500S; `SD600S`=SD600S |  |  |
| └ `FYR` | number | 주철근 항복강도. CODE가 None일 때 사용자 입력. CODE가 Standard일 때 자동 입력. |  |  |
| └ `SUB_REBAR_NAME` | string | CODE가 None일 때의 사용자 정의 보조철근 이름. |  |  |
| └ `SUB_REBAR_GRADE` | string | CODE가 Standard일 때의 보조철근 등급. — `SD300`=SD300; `SD400`=SD400; `SD500`=SD500; `SD600`=SD600; `SD700`=SD700; `SD400S`=SD400S; `SD500S`=SD500S; `SD600S`=SD600S |  |  |
| └ `FYS` | number | 보조철근 항복강도. CODE가 None일 때 사용자 입력. CODE가 Standard일 때 자동 입력. |  |  |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "5": {
      "STEEL": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS22(S)",
        "GRADE": "SM275TMC"
      },
      "CONCRETE": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C65"
      },
      "REINFORCEMENT": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD700",
        "SUB_REBAR_GRADE": "SD700"
      }
    }
  }
}
```

**Response Body**

```json
{
  "MATD": {
    "5": {
      "STEEL": {
        "CODE": "STANDARD",
        "STANDARD_CODE": "KS22(S)",
        "GRADE": "SM275TMC"
      },
      "CONCRETE": {
        "CODE": "STANDARD",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C65"
      },
      "REINFORCEMENT": {
        "CODE": "STANDARD",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD700",
        "SUB_REBAR_GRADE": "SD700"
      }
    }
  }
}
```

> ⚠️ **2026-08-27 확인 (article id `59471948895129`):** GET/PUT 응답 예제의 `"CODE"` 값이 `"STANDARD"`(대문자)로, PUT 요청 예제·JSON Schema의 `oneOf`("Standard")와 대소문자가 다르다 — 원문 자체의 모순이며, 예제 원문을 그대로 유지한다. (26장 MATD와 동일한 패턴.)

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "5": {
            "STEEL": {
                "CODE": "Standard",
                "STANDARD_CODE": "KS22(S)",
                "GRADE": "SM275TMC"
            },
            "CONCRETE": {
                "CODE": "Standard",
                "STANDARD_CODE": "KS19(RC)",
                "GRADE": "C65"
            },
            "REINFORCEMENT": {
                "CODE": "Standard",
                "STANDARD_CODE": "KS19(RC)",
                "MAIN_REBAR_GRADE": "SD700",
                "SUB_REBAR_GRADE": "SD700"
            }
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MATD", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MATD", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MATD", headers=HEADERS)
```

---

## 25. `DESIGN/SRC/AIK-SRC2K/MCRD` — SRC 기둥 단면 데이터 수정

> **기능:** SRC 기둥 단면 데이터(매입형강 배치 등)를 수정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MCRD
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
      "description": "Keyed object (dictionary). Each property name is a section ID string.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "MAIN_BAR",
            "SHEAR_BAR"
          ],
          "additionalProperties": false,
          "properties": {
            "MAIN_BAR": {
              "type": "object",
              "required": [
                "NUM",
                "NAME",
                "ROW",
                "DO"
              ],
              "description": "Main rebar data.",
              "additionalProperties": false,
              "properties": {
                "USE_REBAR_SPACE": {
                  "type": "boolean",
                  "description": "Auto-calculated rebar spacing.",
                  "default": true
                },
                "REBAR_SPACE": {
                  "type": "number",
                  "description": "Main rebar spacing. Used when USE_REBAR_SPACE is false.",
                  "default": 0,
                  "minimum": 0
                },
                "NUM": {
                  "type": "integer",
                  "description": "Total number of main rebars. Must be a multiple of 4.",
                  "minimum": 4,
                  "multipleOf": 4
                },
                "NAME": {
                  "type": "string",
                  "description": "Main rebar size designation.",
                  "oneOf": [
                    {
                      "title": "D4",
                      "const": "D4"
                    },
                    {
                      "title": "D5",
                      "const": "D5"
                    },
                    {
                      "title": "D6",
                      "const": "D6"
                    },
                    {
                      "title": "D7",
                      "const": "D7"
                    },
                    {
                      "title": "D8",
                      "const": "D8"
                    },
                    "...(전체 19개)"
                  ]
                },
                "ROW": {
                  "type": "integer",
                  "description": "Number of rebar rows for rectangular section. Must be a multiple of 2.",
                  "minimum": 2,
                  "multipleOf": 2
                },
                "DO": {
                  "type": "number",
                  "description": "Concrete cover / center distance d0.",
                  "minimum": 0
                }
              }
            },
            "SHEAR_BAR": {
              "type": "object",
              "required": [
                "NAME",
                "DIST"
              ],
              "description": "Hoop/tie rebar data.",
              "additionalProperties": false,
              "properties": {
                "NAME": {
                  "type": "string",
                  "description": "Hoop/tie rebar size designation.",
                  "oneOf": [
                    {
                      "title": "D4",
                      "const": "D4"
                    },
                    {
                      "title": "D5",
                      "const": "D5"
                    },
                    {
                      "title": "D6",
                      "const": "D6"
                    },
                    {
                      "title": "D7",
                      "const": "D7"
                    },
                    {
                      "title": "D8",
                      "const": "D8"
                    },
                    "...(전체 19개)"
                  ]
                },
                "DIST": {
                  "type": "number",
                  "description": "Hoop/tie rebar spacing. Used when USE_REBAR_SPACE is false.",
                  "exclusiveMinimum": 0
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `MAIN_BAR` | object | 주철근 데이터. |  | O |
| └ `USE_REBAR_SPACE` | boolean | 자동 계산된 철근 간격. | true |  |
| └ `REBAR_SPACE` | number | 주철근 간격. USE_REBAR_SPACE가 false일 때 사용. | 0 |  |
| └ `NUM` | integer | 주철근 총 개수. 4의 배수여야 함. |  | O |
| └ `NAME` | string | 주철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ `ROW` | integer | 사각형 단면의 철근 열 수. 2의 배수여야 함. |  | O |
| └ `DO` | number | 콘크리트 피복 / 중심간 거리 d0. |  | O |
| `SHEAR_BAR` | object | 후프/타이 철근 데이터. |  | O |
| └ `NAME` | string | 후프/타이 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ `DIST` | number | 후프/타이 철근 간격. USE_REBAR_SPACE가 false일 때 사용. |  | O |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "4": {
      "MAIN_BAR": {
        "USE_REBAR_SPACE": true,
        "REBAR_SPACE": 0,
        "NUM": 4,
        "NAME": "D4",
        "ROW": 2,
        "DO": 0.05
      },
      "SHEAR_BAR": {
        "NAME": "D4",
        "DIST": 300
      }
    }
  }
}
```

**Response Body**

```json
{
  "MCRD": {
    "4": {
      "MAIN_BAR": {
        "USE_REBAR_SPACE": true,
        "NUM": 4,
        "NAME": "D4",
        "ROW": 2,
        "DO": 0.05,
        "REBAR_SPACE": 0
      },
      "SHEAR_BAR": {
        "NAME": "D4",
        "DIST": 300
      }
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "4": {
            "MAIN_BAR": {
                "USE_REBAR_SPACE": true,
                "REBAR_SPACE": 0,
                "NUM": 4,
                "NAME": "D4",
                "ROW": 2,
                "DO": 0.05
            },
            "SHEAR_BAR": {
                "NAME": "D4",
                "DIST": 300
            }
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MCRD", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MCRD", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MCRD", headers=HEADERS)
```

---

## 26. `DESIGN/SRC/AIK-SRC2K/MEMB` — 부재 배정

> **기능:** 설계 부재(요소→부재) 배정을 관리합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MEMB
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `AELEM` | array | 요소 목록 |  | O |
| `bREVERSE` | boolean | 부재축 방향 반전 | false |  |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "1": {
      "AELEM": [
        859,
        860,
        861
      ],
      "bREVERSE": true
    },
    "2": {
      "AELEM": [
        883,
        868
      ],
      "bREVERSE": true
    }
  }
}
```

**Response Body**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [
        859,
        860,
        861
      ],
      "bREVERSE": true
    },
    "2": {
      "AELEM": [
        883,
        868
      ],
      "bREVERSE": true
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "1": {
            "AELEM": [
                859,
                860,
                861
            ],
            "bREVERSE": true
        },
        "2": {
            "AELEM": [
                883,
                868
            ],
            "bREVERSE": true
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MEMB", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MEMB", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MEMB", headers=HEADERS)
```

---

## 27. `DESIGN/SRC/AIK-SRC2K/MRBD` — SRC 보 단면 데이터 수정

> **기능:** SRC 보 단면 데이터(매입형강/철근 배치 등)를 수정합니다.

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MRBD
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
      "description": "Keyed object (dictionary). Each property name is a Section ID.",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "DT",
            "DB",
            "SHEAR_BAR"
          ],
          "anyOf": [
            {
              "required": [
                "BAR_SECTOR_I"
              ]
            },
            {
              "required": [
                "BAR_SECTOR_M"
              ]
            },
            {
              "required": [
                "BAR_SECTOR_J"
              ]
            }
          ],
          "additionalProperties": false,
          "properties": {
            "BAR_SECTOR_I": {
              "type": "object",
              "description": "Rebar configuration at I-section.",
              "required": [
                "TOP",
                "BOT",
                "STIRRUP_SPACE"
              ],
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "object",
                  "description": "Top rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "BOT": {
                  "type": "object",
                  "description": "Bottom rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "STIRRUP_SPACE": {
                  "type": "number",
                  "description": "Stirrup spacing at I-section.",
                  "exclusiveMinimum": 0
                },
                "STIRRUP_NUM": {
                  "type": "integer",
                  "description": "Number of stirrup sets at I-section.",
                  "default": 2,
                  "minimum": 2,
                  "maximum": 20
                }
              }
            },
            "BAR_SECTOR_M": {
              "type": "object",
              "description": "Rebar configuration at M-section.",
              "required": [
                "TOP",
                "BOT",
                "STIRRUP_SPACE"
              ],
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "object",
                  "description": "Top rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "BOT": {
                  "type": "object",
                  "description": "Bottom rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "STIRRUP_SPACE": {
                  "type": "number",
                  "description": "Stirrup spacing at M-section.",
                  "exclusiveMinimum": 0
                },
                "STIRRUP_NUM": {
                  "type": "integer",
                  "description": "Number of stirrup sets at M-section.",
                  "default": 2,
                  "minimum": 2,
                  "maximum": 20
                }
              }
            },
            "BAR_SECTOR_J": {
              "type": "object",
              "description": "Rebar configuration at J-section.",
              "required": [
                "TOP",
                "BOT",
                "STIRRUP_SPACE"
              ],
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "object",
                  "description": "Top rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "BOT": {
                  "type": "object",
                  "description": "Bottom rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "STIRRUP_SPACE": {
                  "type": "number",
                  "description": "Stirrup spacing at J-section.",
                  "exclusiveMinimum": 0
                },
                "STIRRUP_NUM": {
                  "type": "integer",
                  "description": "Number of stirrup sets at J-section.",
                  "default": 2,
                  "minimum": 2,
                  "maximum": 20
                }
              }
            },
            "DT": {
              "type": "number",
              "description": "Top rebar cover thickness.",
              "exclusiveMinimum": 0
            },
            "DB": {
              "type": "number",
              "description": "Bottom rebar cover thickness.",
              "exclusiveMinimum": 0
            },
            "SHEAR_BAR": {
              "type": "string",
              "description": "Stirrup rebar size designation.",
              "oneOf": [
                {
                  "title": "D4",
                  "const": "D4"
                },
                {
                  "title": "D5",
                  "const": "D5"
                },
                {
                  "title": "D6",
                  "const": "D6"
                },
                {
                  "title": "D7",
                  "const": "D7"
                },
                {
                  "title": "D8",
                  "const": "D8"
                },
                "...(전체 19개)"
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

| Key | 타입 | 설명 | 기본값 | 필수 |
|-----|------|------|--------|------|
| `BAR_SECTOR_I` | object | I단면 철근 배치. |  |  |
| └ `TOP` | object | 상부 철근 배치. |  | O |
| └ └ `LAYER1` | object | 상부 철근 1단. |  | O |
| └ └ └ `NAME` | string | 상부 철근 1단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 상부 철근 1단의 철근 개수. |  | O |
| └ └ `LAYER2` | object | 상부 철근 2단. |  |  |
| └ └ └ `NAME` | string | 상부 철근 2단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 상부 철근 2단의 철근 개수. |  | O |
| └ `BOT` | object | 하부 철근 배치. |  | O |
| └ └ `LAYER1` | object | 하부 철근 1단. |  | O |
| └ └ └ `NAME` | string | 하부 철근 1단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 하부 철근 1단의 철근 개수. |  | O |
| └ └ `LAYER2` | object | 하부 철근 2단. |  |  |
| └ └ └ `NAME` | string | 하부 철근 2단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 하부 철근 2단의 철근 개수. |  | O |
| └ `STIRRUP_SPACE` | number | I단면 스터럽 간격. |  | O |
| └ `STIRRUP_NUM` | integer | I단면 스터럽 세트 수. | 2 |  |
| `BAR_SECTOR_M` | object | M단면 철근 배치. |  |  |
| └ `TOP` | object | 상부 철근 배치. |  | O |
| └ └ `LAYER1` | object | 상부 철근 1단. |  | O |
| └ └ └ `NAME` | string | 상부 철근 1단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 상부 철근 1단의 철근 개수. |  | O |
| └ └ `LAYER2` | object | 상부 철근 2단. |  |  |
| └ └ └ `NAME` | string | 상부 철근 2단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 상부 철근 2단의 철근 개수. |  | O |
| └ `BOT` | object | 하부 철근 배치. |  | O |
| └ └ `LAYER1` | object | 하부 철근 1단. |  | O |
| └ └ └ `NAME` | string | 하부 철근 1단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 하부 철근 1단의 철근 개수. |  | O |
| └ └ `LAYER2` | object | 하부 철근 2단. |  |  |
| └ └ └ `NAME` | string | 하부 철근 2단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 하부 철근 2단의 철근 개수. |  | O |
| └ `STIRRUP_SPACE` | number | M단면 스터럽 간격. |  | O |
| └ `STIRRUP_NUM` | integer | M단면 스터럽 세트 수. | 2 |  |
| `BAR_SECTOR_J` | object | J단면 철근 배치. |  |  |
| └ `TOP` | object | 상부 철근 배치. |  | O |
| └ └ `LAYER1` | object | 상부 철근 1단. |  | O |
| └ └ └ `NAME` | string | 상부 철근 1단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 상부 철근 1단의 철근 개수. |  | O |
| └ └ `LAYER2` | object | 상부 철근 2단. |  |  |
| └ └ └ `NAME` | string | 상부 철근 2단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 상부 철근 2단의 철근 개수. |  | O |
| └ `BOT` | object | 하부 철근 배치. |  | O |
| └ └ `LAYER1` | object | 하부 철근 1단. |  | O |
| └ └ └ `NAME` | string | 하부 철근 1단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 하부 철근 1단의 철근 개수. |  | O |
| └ └ `LAYER2` | object | 하부 철근 2단. |  |  |
| └ └ └ `NAME` | string | 하부 철근 2단의 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |
| └ └ └ `NUM` | integer | 하부 철근 2단의 철근 개수. |  | O |
| └ `STIRRUP_SPACE` | number | J단면 스터럽 간격. |  | O |
| └ `STIRRUP_NUM` | integer | J단면 스터럽 세트 수. | 2 |  |
| `DT` | number | 상부 철근 피복 두께. |  | O |
| `DB` | number | 하부 철근 피복 두께. |  | O |
| `SHEAR_BAR` | string | 스터럽 철근 규격. — `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(전체 19개) |  | O |

> 위 필드는 `"Assign"` 객체의 각 ID 키(예: `"1"`) 하위에 위치합니다.

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "3": {
      "DT": 0.1,
      "DB": 0.1,
      "SHEAR_BAR": "D4",
      "BAR_SECTOR_I": {
        "STIRRUP_SPACE": 150,
        "STIRRUP_NUM": 2,
        "TOP": {
          "LAYER1": {
            "NAME": "D32",
            "NUM": 2
          },
          "LAYER2": {
            "NAME": "D32",
            "NUM": 2
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D35",
            "NUM": 1
          },
          "LAYER2": {
            "NAME": "D35",
            "NUM": 3
          }
        }
      },
      "BAR_SECTOR_M": {
        "STIRRUP_SPACE": 150,
        "TOP": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 1
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 2
          }
        }
      },
      "BAR_SECTOR_J": {
        "STIRRUP_SPACE": 150,
        "TOP": {
          "LAYER1": {
            "NAME": "D51",
            "NUM": 2
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 2
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
  "MRBD": {
    "3": {
      "BAR_SECTOR_I": {
        "TOP": {
          "LAYER1": {
            "NAME": "D32",
            "NUM": 2
          },
          "LAYER2": {
            "NAME": "D32",
            "NUM": 2
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D35",
            "NUM": 1
          },
          "LAYER2": {
            "NAME": "D35",
            "NUM": 3
          }
        },
        "STIRRUP_SPACE": 150,
        "STIRRUP_NUM": 2
      },
      "BAR_SECTOR_M": {
        "TOP": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 1
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 2
          }
        },
        "STIRRUP_SPACE": 150
      },
      "BAR_SECTOR_J": {
        "TOP": {
          "LAYER1": {
            "NAME": "D51",
            "NUM": 2
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 2
          }
        },
        "STIRRUP_SPACE": 150
      },
      "DT": 0.1,
      "DB": 0.1,
      "SHEAR_BAR": "D4"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}

# 데이터 설정 (PUT)
payload = {
    "Assign": {
        "3": {
            "DT": 0.1,
            "DB": 0.1,
            "SHEAR_BAR": "D4",
            "BAR_SECTOR_I": {
                "STIRRUP_SPACE": 150,
                "STIRRUP_NUM": 2,
                "TOP": {
                    "LAYER1": {
                        "NAME": "D32",
                        "NUM": 2
                    },
                    "LAYER2": {
                        "NAME": "D32",
                        "NUM": 2
                    }
                },
                "BOT": {
                    "LAYER1": {
                        "NAME": "D35",
                        "NUM": 1
                    },
                    "LAYER2": {
                        "NAME": "D35",
                        "NUM": 3
                    }
                }
            },
            "BAR_SECTOR_M": {
                "STIRRUP_SPACE": 150,
                "TOP": {
                    "LAYER1": {
                        "NAME": "D43",
                        "NUM": 1
                    }
                },
                "BOT": {
                    "LAYER1": {
                        "NAME": "D43",
                        "NUM": 2
                    }
                }
            },
            "BAR_SECTOR_J": {
                "STIRRUP_SPACE": 150,
                "TOP": {
                    "LAYER1": {
                        "NAME": "D51",
                        "NUM": 2
                    }
                },
                "BOT": {
                    "LAYER1": {
                        "NAME": "D43",
                        "NUM": 2
                    }
                }
            }
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MRBD", json=payload, headers=HEADERS)
res.raise_for_status()

# 설정값 조회 (GET)
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MRBD", headers=HEADERS)
print(got.json())

# 삭제: requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MRBD", headers=HEADERS)
```
