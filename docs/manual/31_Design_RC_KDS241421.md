# 31. Design Code – RC KDS 24 14 21:2021 (교량 철근콘크리트 설계)

> **예제 Base URL (MIDAS Civil NX)** `https://moa-engineers.midasit.com:443/civil`  
> **인증 헤더** `MAPI-Key: <발급된 키>`  
> **공식 하위 목차** [KDS 24 14 21:2021 RC 설계](https://support.midasuser.com/hc/ko/articles/64738414827033)

교량 RC 부재의 설계 기준과 하중조합, 부재 배정, 철근 입력 및 설계 실행을 다룹니다.
고유 URI **19개**와 본문 **19절**을 다룹니다.
공통 URI 접두사는 `{base url}/DESIGN/RC/KDS-24-14-21-2021/<CODE>`입니다.
기준 선택에는 `{base url}/DESIGN/RC/DRC`를 사용합니다.

---

## Endpoint 목록 (19개 절)

| No. | Endpoint | 기능 | Active Methods |
| --- | --- | --- | --- |
| 0 | [`DRC`](#0-drc--design-code-kds-24-14-21--2021) | 교량 RC 설계 기준을 KDS 24 14 21:2021로 설정하거나 조회합니다. | GET · PUT · DELETE |
| 1 | [`OPE_MEMB`](#1-ope_memb--auto-member-assignment) | 설계 대상 요소를 RC 부재로 자동 배정합니다. | POST |
| 2 | [`DCTL`](#2-dctl--definition-of-frame) | 프레임의 설계 조건을 정의합니다. | GET · PUT · DELETE |
| 3 | [`DCO`](#3-dco--design-code-option) | 교량 RC 설계 기준의 옵션을 설정합니다. | GET · PUT · DELETE |
| 4 | [`KFAC`](#4-kfac--effective-length-factor-k) | 부재별 유효길이계수 K를 지정합니다. | POST · GET · PUT · DELETE |
| 5 | [`LTSR`](#5-ltsr--limiting-slenderness-ratio) | 부재별 세장비 한계를 설정합니다. | POST · GET · PUT · DELETE |
| 6 | [`LCMT`](#6-lcmt--load-combination-type) | 설계에 사용할 하중조합 유형을 설정합니다. | GET · PUT · DELETE |
| 7 | [`LCTB`](#7-lctb--load-contribution-for-nonlinear-load-case) | 비선형 하중 케이스에 기여하는 하중과 계수를 조회합니다. | GET · DELETE |
| 8 | [`MEMB`](#8-memb--member-assignment) | RC 설계 대상 요소의 부재 배정을 관리합니다. | POST · GET · PUT · DELETE |
| 9 | [`RCPL`](#9-rcpl--member-assignment-plate) | 판 요소를 RC 설계용 부재에 배정합니다. | POST · GET · PUT · DELETE |
| 10 | [`MBTP`](#10-mbtp--modify-member-type) | 지정한 요소의 부재 유형을 수정합니다. | POST · GET · PUT · DELETE |
| 11 | [`MATD`](#11-matd--modify-rc-materials) | RC 설계에 사용할 콘크리트와 철근 재료를 수정합니다. | GET · PUT · DELETE |
| 12 | [`CMFT`](#12-cmft--moment-factor-cm) | 부재별 모멘트 계수 Cm을 지정합니다. | POST · GET · PUT · DELETE |
| 13 | [`FMAG`](#13-fmag--moment-magnifier-b1delta_b-b2delta_s) | 부재별 모멘트 확대계수 B1/δb와 B2/δs를 지정합니다. | POST · GET · PUT · DELETE |
| 14 | [`SLTC`](#14-sltc--shortlong-term-load-case) | 단기·장기 하중 케이스를 지정합니다. | GET · PUT · DELETE |
| 15 | [`LENG`](#15-leng--unbraced-length-l-lb) | 부재별 비지지 길이 L과 Lb를 지정합니다. | POST · GET · PUT · DELETE |
| 16 | [`REBT`](#16-rebt--column-general-section-rebar) | 기둥의 일반 단면 철근을 입력합니다. | POST · GET · PUT · DELETE |
| 17 | [`RIBC`](#17-ribc--rebar-input-beam-column-section) | 보와 기둥 단면의 철근 데이터를 입력합니다. | GET · PUT · DELETE |
| 18 | [`PERFORM-DESIGN`](#18-perform-design--perform-design) | 교량 RC 부재의 설계를 실행합니다. | POST |

---

## 0. `DRC` — Design Code (KDS 24 14 21 : 2021)

> **기능** 교량 RC 설계 기준을 KDS 24 14 21:2021로 설정하거나 조회합니다.

다른 기준의 DRC는 [26장 KDS 41](./26_Design_RC_KDS41202022.md#0-designrcdrc--rc-design-code-rc-설계-코드-선택)과 [28장 AASHTO LRFD](./28_Design_RC_AASHTO_LRFD.md#0-designrcdrc--design-code-aashto-lrfd2420)를 참고하세요.

### Input URI

```
{base url}/DESIGN/RC/DRC
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738309723033](https://support.midasuser.com/hc/ko/articles/64738309723033)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] RC Design Code · KDS 24 14 21 : 2021 | `"DGNCODE"` | string | KDS 24 14 21 : 2021 | **Required** |

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
      "propertyNames": {
        "const": "1"
      },
      "patternProperties": {
        "^[0-9]+$": {
          "title": "RC Design Code",
          "type": "object",
          "required": [
            "DGNCODE"
          ],
          "additionalProperties": false,
          "properties": {
            "DGNCODE": {
              "type": "string",
              "description": "RC design code (Design > Design Code Option > Design Code)",
              "default": "KDS 24 14 21 : 2021",
              "enum": [
                "KDS 24 14 21 : 2021"
              ]
            }
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `DRC`

> ⚠️ 공식 응답 예제의 최상위 Key는 `DRC`입니다. KDS 41 20:2022와 LRFD24/20 공식 예제는 `DCON`을 사용합니다.

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "KDS 24 14 21 : 2021"
    }
  }
}
```

**Response**

```json
{
  "DRC": {
    "1": {
      "DGNCODE": "KDS 24 14 21 : 2021"
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/DRC"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "DGNCODE": "KDS 24 14 21 : 2021"
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 1. `OPE_MEMB` — Auto Member Assignment

> **기능** 설계 대상 요소를 RC 부재로 자동 배정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/OPE_MEMB
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738338914329](https://support.midasuser.com/hc/ko/articles/64738338914329)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Assign Type · Manual: "MANUAL" · Automatic: "AUTO" | `"ASSIGN_TYPE"` | string | - | **Required** |
| 2 | [General] Selection Type · All: "ALL" · By Selection: "SELECTION" | `"SELECTION_TYPE"` | string | SELECTION | Optional |
| 3 | [General] Element List | `"ELEM_LIST"` | array | - | Optional |
| 4 | [General] Allow Single Element Member | `"ALLOW_SINGLE"` | boolean | - | **Required** |

### JSON Schema

```json
{
  "type": "object",
  "description": "Member Assignment (Add/Replace) request schema (POST /DESIGN/RC/KDS-24-14-21-2021/OPE_MEMB)",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "ASSIGN_TYPE",
        "ALLOW_SINGLE"
      ],
      "additionalProperties": false,
      "properties": {
        "ASSIGN_TYPE": {
          "type": "string",
          "description": "Assign type",
          "enum": [
            "MANUAL",
            "AUTO"
          ]
        },
        "SELECTION_TYPE": {
          "type": "string",
          "description": "Selection type. ALL is available only with ASSIGN_TYPE AUTO.",
          "default": "SELECTION",
          "enum": [
            "ALL",
            "SELECTION"
          ]
        },
        "ELEM_LIST": {
          "type": "array",
          "description": "Element list. Required unless ASSIGN_TYPE is AUTO and SELECTION_TYPE is ALL (then all elements are used and this list is ignored). Non-frame elements are skipped.",
          "items": {
            "type": "integer"
          },
          "minItems": 1
        },
        "ALLOW_SINGLE": {
          "type": "boolean",
          "description": "Allow single element member"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `MEMB`

### Request / Response JSON

**Request — Automatic, selected elements**

```json
{
  "Argument": {
    "ASSIGN_TYPE": "AUTO",
    "SELECTION_TYPE": "SELECTION",
    "ELEM_LIST": [
      1,
      2,
      3
    ],
    "ALLOW_SINGLE": false
  }
}
```

**Request — Automatic, all elements**

```json
{
  "Argument": {
    "ASSIGN_TYPE": "AUTO",
    "SELECTION_TYPE": "ALL",
    "ALLOW_SINGLE": true
  }
}
```

**Response**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [
        1,
        2,
        3
      ],
      "bREVERSE": false
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/OPE_MEMB"

payload = json.loads(r'''
{
  "Argument": {
    "ASSIGN_TYPE": "AUTO",
    "SELECTION_TYPE": "SELECTION",
    "ELEM_LIST": [
      1,
      2,
      3
    ],
    "ALLOW_SINGLE": false
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 2. `DCTL` — Definition of Frame

> **기능** 프레임의 설계 조건을 정의합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/DCTL
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738329174425](https://support.midasuser.com/hc/ko/articles/64738329174425)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] X-Direction of Frame · Unbraced \| Sway: "Unbraced Sway" · Braced \| Non-sway: "Braced Non-sway" | `"FRAMEX"` | string | Unbraced Sway | Optional |
| 2 | [General] Y-Direction of Frame · Unbraced \| Sway: "Unbraced Sway" · Braced \| Non-sway: "Braced Non-sway" | `"FRAMEY"` | string | Unbraced Sway | Optional |
| 3 | [General] Design Type · 3-D: "3D" · X-Z Plane: "XZ" · Y-Z Plane: "YZ" · X-Y Plane: "XY" | `"DT"` | string | 3D | Optional |
| 4 | [General] Auto Calculate Effective Length Factors | `"bAUTOKF"` | boolean | false | Optional |

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
      "propertyNames": {
        "const": "1"
      },
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Definition of Frame",
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "FRAMEX": {
              "type": "string",
              "description": "X-Direction of Frame",
              "default": "Unbraced Sway",
              "enum": [
                "Unbraced Sway",
                "Braced Non-sway"
              ]
            },
            "FRAMEY": {
              "type": "string",
              "description": "Y-Direction of Frame",
              "default": "Unbraced Sway",
              "enum": [
                "Unbraced Sway",
                "Braced Non-sway"
              ]
            },
            "DT": {
              "type": "string",
              "description": "Design Type",
              "default": "3D",
              "enum": [
                "3D",
                "XZ",
                "YZ",
                "XY"
              ]
            },
            "bAUTOKF": {
              "type": "boolean",
              "description": "Auto calculate effective length factors",
              "default": false
            }
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `DCTL`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": false,
      "DT": "XZ"
    }
  }
}
```

**Response**

```json
{
  "DCTL": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": false,
      "DT": "XZ"
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/DCTL"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": false,
      "DT": "XZ"
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 3. `DCO` — Design Code Option

> **기능** 교량 RC 설계 기준의 옵션을 설정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/DCO
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738299867033](https://support.midasuser.com/hc/ko/articles/64738299867033)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Single settings record: the only accepted key is "1". | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] RC Design Code · KDS 24 14 21 : 2021 | `"DGNCODE"` | string | - | **Required** |

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
      "description": "Single settings record: the only accepted key is \"1\".",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "RC Design Code",
          "type": "object",
          "required": [
            "DGNCODE"
          ],
          "additionalProperties": false,
          "properties": {
            "DGNCODE": {
              "type": "string",
              "description": "RC Design Code",
              "enum": [
                "KDS 24 14 21 : 2021"
              ]
            }
          }
        }
      },
      "maxProperties": 1,
      "propertyNames": {
        "const": "1"
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `DCO`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "KDS 24 14 21 : 2021"
    }
  }
}
```

**Response**

```json
{
  "DCO": {
    "1": {
      "DGNCODE": "KDS 24 14 21 : 2021"
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/DCO"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "DGNCODE": "KDS 24 14 21 : 2021"
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 4. `KFAC` — Effective Length Factor (K)

> **기능** 부재별 유효길이계수 K를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/KFAC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738314048281](https://support.midasuser.com/hc/ko/articles/64738314048281)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings (e.g., "1"), where each entry represents an element | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Ky · Minimum: 0 | `"Ky"` | number | 1 | Optional |
| 2 | [General] Kz · Minimum: 0 | `"Kz"` | number | 1 | Optional |

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
              "description": "Effective length factor Ky. Must be greater than 0",
              "default": 1,
              "exclusiveMinimum": 0
            },
            "Kz": {
              "type": "number",
              "description": "Effective length factor Kz. Must be greater than 0",
              "default": 1,
              "exclusiveMinimum": 0
            }
          },
          "title": "Effective Length Factor(K)"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `KFAC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "859": {
      "Ky": 1.0,
      "Kz": 1.0
    },
    "860": {
      "Ky": 1.2,
      "Kz": 0.8
    }
  }
}
```

**Response**

```json
{
  "KFAC": {
    "859": {
      "Ky": 1.0,
      "Kz": 1.0
    },
    "860": {
      "Ky": 1.2,
      "Kz": 0.8
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/KFAC"

payload = json.loads(r'''
{
  "Assign": {
    "859": {
      "Ky": 1.0,
      "Kz": 1.0
    },
    "860": {
      "Ky": 1.2,
      "Kz": 0.8
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 5. `LTSR` — Limiting Slenderness Ratio

> **기능** 부재별 세장비 한계를 설정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/LTSR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738314188057](https://support.midasuser.com/hc/ko/articles/64738314188057)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Compression | `"COMP"` | number | 200 | Optional |
| 2 | [General] Tension | `"TENS"` | number | 300 | Optional |
| 3 | [General] Do not Check | `"bNOTCHECK"` | boolean | false | Optional |

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
      "description": "Keyed object (dictionary). Each property name is an element ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Limiting Slenderness Ratio",
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "COMP": {
              "type": "number",
              "description": "Limiting slenderness ratio for compression (set to 0 and disabled when bNOTCHECK is checked). Must be greater than 0 unless bNOTCHECK is true",
              "default": 200
            },
            "TENS": {
              "type": "number",
              "description": "Limiting slenderness ratio for tension (set to 0 and disabled when bNOTCHECK is checked). Must be greater than 0 unless bNOTCHECK is true",
              "default": 300
            },
            "bNOTCHECK": {
              "type": "boolean",
              "description": "Do not check for slenderness ratio",
              "default": false
            }
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `LTSR`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "5": {
      "COMP": 100,
      "TENS": 200
    }
  }
}
```

**Response**

```json
{
  "LTSR": {
    "5": {
      "COMP": 100,
      "TENS": 200
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/LTSR"

payload = json.loads(r'''
{
  "Assign": {
    "5": {
      "COMP": 100,
      "TENS": 200
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 6. `LCMT` — Load Combination Type

> **기능** 설계에 사용할 하중조합 유형을 설정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/LCMT
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738323036057](https://support.midasuser.com/hc/ko/articles/64738323036057)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Single settings record: the only accepted key is "1". | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Load Combinations | `"LOAD_COMBINATIONS"` | array [object] | - | **Required** |
| 1.1 | └ [General] Load Combination | `"NAME"` | string | - | **Required** |
| 1.2 | └ [General] Limit State · Ultimate Limit State: "ULTIMATE" · Extreme Limit State: "EXTREME" · Service Limit State: "SERVICE" · None (Load Combination List): "NONE" | `"LIMIT_STATE"` | string | - | **Required** |

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
      "description": "Single settings record: the only accepted key is \"1\".",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "propertyNames": {
        "const": "1"
      },
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Load Combination Type",
          "type": "object",
          "required": [
            "LOAD_COMBINATIONS"
          ],
          "additionalProperties": false,
          "properties": {
            "LOAD_COMBINATIONS": {
              "type": "array",
              "minItems": 1,
              "description": "Concrete Design tab: load combinations to put into a limit state list. Combinations not listed keep their current list",
              "items": {
                "type": "object",
                "required": [
                  "NAME",
                  "LIMIT_STATE"
                ],
                "additionalProperties": false,
                "properties": {
                  "NAME": {
                    "type": "string",
                    "minLength": 1,
                    "description": "Name of an existing concrete load combination (Load Combination List)"
                  },
                  "LIMIT_STATE": {
                    "type": "string",
                    "description": "Limit state list the combination goes to. NONE removes it from all three lists",
                    "enum": [
                      "ULTIMATE",
                      "EXTREME",
                      "SERVICE",
                      "NONE"
                    ]
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

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `LCMT`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "LOAD_COMBINATIONS": [
        {
          "NAME": "cLCB1",
          "LIMIT_STATE": "ULTIMATE"
        },
        {
          "NAME": "cLCB2",
          "LIMIT_STATE": "EXTREME"
        },
        {
          "NAME": "cLCB3",
          "LIMIT_STATE": "SERVICE"
        }
      ]
    }
  }
}
```

**Response**

```json
{
  "LCMT": {
    "1": {
      "LOAD_COMBINATIONS": [
        {
          "NAME": "cLCB1",
          "LIMIT_STATE": "ULTIMATE"
        },
        {
          "NAME": "cLCB2",
          "LIMIT_STATE": "EXTREME"
        },
        {
          "NAME": "cLCB3",
          "LIMIT_STATE": "SERVICE"
        }
      ]
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/LCMT"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "LOAD_COMBINATIONS": [
        {
          "NAME": "cLCB1",
          "LIMIT_STATE": "ULTIMATE"
        },
        {
          "NAME": "cLCB2",
          "LIMIT_STATE": "EXTREME"
        },
        {
          "NAME": "cLCB3",
          "LIMIT_STATE": "SERVICE"
        }
      ]
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 7. `LCTB` — Load Contribution for Nonlinear Load Case

> **기능** 비선형 하중 케이스에 기여하는 하중과 계수를 조회합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/LCTB
```

### Active Methods

`GET` · `DELETE`

### Specifications

**원문** [한국어 64738300405657](https://support.midasuser.com/hc/ko/articles/64738300405657)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Load Contribution Name | `"NAME"` | string | - | **Required** |
| 2 | [General] Description | `"DESC"` | string |  | Optional |
| 3 | [General] Load Contribution Items | `"BASE_ITEM"` | array [object] | - | **Required** |
| 3.1 | └ [General] Factor | `"FACTOR"` | number | - | **Required** |
| 3.2 | └ [General] Load Case Name | `"LOAD_CASE_NAME"` | string | - | **Required** |

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

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `LCTB`

> ⚠️ 공식 Active Methods에는 GET과 DELETE가 나열됩니다. `Assign` 바디가 있는 공식 요청 예제에는 메서드가 표시되지 않습니다.

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "NAME": "NL_cLCB1",
      "DESC": "",
      "BASE_ITEM": [
        {
          "FACTOR": 1.25,
          "LOAD_CASE_NAME": "DL"
        },
        {
          "FACTOR": 1.75,
          "LOAD_CASE_NAME": "LL"
        }
      ]
    }
  }
}
```

**Response**

```json
{
  "LCTB": {
    "1": {
      "NAME": "NL-Sum",
      "DESC": "",
      "BASE_ITEM": [
        {
          "FACTOR": 1.0,
          "LOAD_CASE_NAME": "DL"
        },
        {
          "FACTOR": 1.0,
          "LOAD_CASE_NAME": "WS"
        }
      ]
    }
  }
}
```

### Python 예제

공식 Active Methods의 GET을 사용해 조회합니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/LCTB"

response = requests.get(URI, headers=HEADERS)
response.raise_for_status()
print(response.json())
```


---

## 8. `MEMB` — Member Assignment

> **기능** RC 설계 대상 요소의 부재 배정을 관리합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/MEMB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738314609689](https://support.midasuser.com/hc/ko/articles/64738314609689)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Element List | `"AELEM"` | array | - | **Required** |
| 2 | [General] Reverse Local Direction | `"bREVERSE"` | boolean | false | Optional |

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
              "description": "Element numbers of the member. Beam or truss elements only",
              "items": {
                "type": "integer",
                "minimum": 1
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

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `MEMB`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "AELEM": [
        885,
        888,
        891
      ],
      "bREVERSE": true
    },
    "2": {
      "AELEM": [
        919
      ],
      "bREVERSE": true
    }
  }
}
```

**Response**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [
        860,
        861,
        862,
        863,
        864
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        865,
        866
      ],
      "bREVERSE": false
    },
    "3": {
      "AELEM": [
        1020,
        1021,
        1022
      ],
      "bREVERSE": false
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/MEMB"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "AELEM": [
        885,
        888,
        891
      ],
      "bREVERSE": true
    },
    "2": {
      "AELEM": [
        919
      ],
      "bREVERSE": true
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 9. `RCPL` — Member Assignment (Plate)

> **기능** 판 요소를 RC 설계용 부재에 배정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/RCPL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738323461145](https://support.midasuser.com/hc/ko/articles/64738323461145)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a plate design member ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Name | `"NAME"` | string | - | **Required** |
| 2 | [General] Elements | `"ELEM_LIST"` | array | - | **Required** |
| 3 | [General] Design Type · Beam: "BEAM" · Wall: "WALL" | `"PLATE_MEMB"` | string | BEAM | Optional |
| 4 | [General] Axis · Local: "LOCAL" · UCS: "UCS" | `"AXIS_TYPE"` | string | LOCAL | Optional |
| 5 | [When AXIS_TYPE = "UCS"] UCS | `"UCS_NAME"` | string | - | **Required** |
| 6 | [When AXIS_TYPE = "UCS"] Force · Element: "ELEMENT" · Avg. Nodal: "AVG. NODAL" | `"ANA_TYPE"` | string | ELEMENT | Optional |
| 7 | [When AXIS_TYPE = "UCS"] Avg.Nodal Active Only | `"ACTIVE_ONLY"` | boolean | false | Optional |
| 8 | [When AXIS_TYPE = "UCS"] Direction · X-Dir (Mxx): "X" · Y-Dir (Myy): "Y" | `"DIR"` | string | X | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a plate design member ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Member Assignment (Plate)",
          "type": "object",
          "required": [
            "NAME",
            "ELEM_LIST"
          ],
          "additionalProperties": false,
          "properties": {
            "NAME": {
              "type": "string",
              "minLength": 1,
              "description": "Design member name, unique across records (case-insensitive)"
            },
            "ELEM_LIST": {
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "integer",
                "minimum": 1
              },
              "description": "Plate (or plane-stress) elements of this design member, all with one material and one thickness. Replaces the stored set"
            },
            "PLATE_MEMB": {
              "type": "string",
              "default": "BEAM",
              "description": "Design Type",
              "enum": [
                "BEAM",
                "WALL"
              ]
            },
            "AXIS_TYPE": {
              "type": "string",
              "default": "LOCAL",
              "description": "Plate Force Option: axis system of the design direction",
              "enum": [
                "LOCAL",
                "UCS"
              ]
            },
            "UCS_NAME": {
              "type": "string",
              "description": "Name of an existing Named UCS. Required when AXIS_TYPE is UCS"
            },
            "ANA_TYPE": {
              "type": "string",
              "default": "ELEMENT",
              "description": "Plate Force Option: result values used for design",
              "enum": [
                "ELEMENT",
                "AVG. NODAL"
              ]
            },
            "ACTIVE_ONLY": {
              "type": "boolean",
              "default": false,
              "description": "Avg.Nodal Active Only (used only when ANA_TYPE is AVG. NODAL)"
            },
            "DIR": {
              "type": "string",
              "default": "X",
              "description": "Design direction of the rebar. One element has at most one record per direction",
              "enum": [
                "X",
                "Y"
              ]
            }
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `RCPL`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "NAME": "SDB",
      "ELEM_LIST": [
        8,
        9
      ],
      "PLATE_MEMB": "BEAM",
      "AXIS_TYPE": "LOCAL",
      "ANA_TYPE": "ELEMENT",
      "DIR": "X"
    },
    "2": {
      "NAME": "SDB-Y",
      "ELEM_LIST": [
        8,
        9
      ],
      "PLATE_MEMB": "BEAM",
      "AXIS_TYPE": "LOCAL",
      "ANA_TYPE": "AVG. NODAL",
      "ACTIVE_ONLY": true,
      "DIR": "Y"
    }
  }
}
```

**Response**

```json
{
  "RCPL": {
    "1": {
      "NAME": "SDB",
      "ELEM_LIST": [
        8,
        9
      ],
      "PLATE_MEMB": "BEAM",
      "AXIS_TYPE": "LOCAL",
      "ANA_TYPE": "ELEMENT",
      "ACTIVE_ONLY": false,
      "DIR": "X"
    },
    "2": {
      "NAME": "SDB-Y",
      "ELEM_LIST": [
        8,
        9
      ],
      "PLATE_MEMB": "BEAM",
      "AXIS_TYPE": "LOCAL",
      "ANA_TYPE": "AVG. NODAL",
      "ACTIVE_ONLY": true,
      "DIR": "Y"
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/RCPL"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "NAME": "SDB",
      "ELEM_LIST": [
        8,
        9
      ],
      "PLATE_MEMB": "BEAM",
      "AXIS_TYPE": "LOCAL",
      "ANA_TYPE": "ELEMENT",
      "DIR": "X"
    },
    "2": {
      "NAME": "SDB-Y",
      "ELEM_LIST": [
        8,
        9
      ],
      "PLATE_MEMB": "BEAM",
      "AXIS_TYPE": "LOCAL",
      "ANA_TYPE": "AVG. NODAL",
      "ACTIVE_ONLY": true,
      "DIR": "Y"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 10. `MBTP` — Modify Member Type

> **기능** 지정한 요소의 부재 유형을 수정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/MBTP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738300815385](https://support.midasuser.com/hc/ko/articles/64738300815385)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings (e.g., "1"), where each entry represents an element. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Member Type · Beam: "BEAM" · Column: "COLUMN" · Brace: "BRACE" | `"TYPE"` | string | - | **Required** |

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
              "enum": [
                "BEAM",
                "COLUMN",
                "BRACE"
              ]
            }
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `MBTP`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "934": {
      "TYPE": "BRACE"
    },
    "1058": {
      "TYPE": "COLUMN"
    },
    "1059": {
      "TYPE": "COLUMN"
    },
    "1066": {
      "TYPE": "BEAM"
    }
  }
}
```

**Response**

```json
{
  "MBTP": {
    "934": {
      "TYPE": "BRACE"
    },
    "1058": {
      "TYPE": "COLUMN"
    },
    "1059": {
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
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/MBTP"

payload = json.loads(r'''
{
  "Assign": {
    "934": {
      "TYPE": "BRACE"
    },
    "1058": {
      "TYPE": "COLUMN"
    },
    "1059": {
      "TYPE": "COLUMN"
    },
    "1066": {
      "TYPE": "BEAM"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 11. `MATD` — Modify RC Materials

> **기능** RC 설계에 사용할 콘크리트와 철근 재료를 수정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/MATD
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738300984857](https://support.midasuser.com/hc/ko/articles/64738300984857)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a concrete material ID string (e.g., "1"): an existing material whose design type is concrete | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Concrete material for design | `"CONCRETE"` | object | - | **Required** |
| 1.1 | └ [General] Code · None (user-defined): "None" · Material DB code: "Standard" | `"CODE"` | string | - | **Required** |
| 1.2 | └ [General] Standard Code · KSCE-LSD15(RC) · KS01-Civil(RC) · KS-Civil(RC) · KS19(RC) · KS01(RC) · KS(RC) | `"STANDARD_CODE"` | string | - | Optional |
| 1.3 | └ [General] Grade | `"GRADE"` | string | - | Optional |
| 1.4 | └ [When CODE = "None (user-defined)"] Name | `"NAME"` | string | - | **Required** |
| 1.5 | └ [When CODE = "None (user-defined)"] Specified Compressive Strength (fc\|fck) · Minimum: 0 | `"FC"` | number | - | **Required** |
| 1.3 | └ [When STANDARD_CODE = "KSCE-LSD15(RC)"] Grade · C15 · C18 · C21 · C24 · C27 · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 · C90 · C95 | `"GRADE"` | string | - | Optional |
| 1.3 | └ [When STANDARD_CODE in ["KS01-Civil(RC)", "KS19(RC)", "KS01(RC)"]] Grade · C15 · C18 · C21 · C24 · C27 · C30 · C35 · C40 · C45 · C49 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 · C90 · C95 | `"GRADE"` | string | - | Optional |
| 1.3 | └ [When STANDARD_CODE in ["KS-Civil(RC)", "KS(RC)"]] Grade · C150 · C180 · C210 · C240 · C270 · C300 · C350 · C400 · C450 · C500 · C550 · C600 · C650 · C700 | `"GRADE"` | string | - | Optional |
| 2 | [General] Rebar material for design | `"REBAR"` | object | - | **Required** |
| 2.1 | └ [General] Code · None (user-defined): "None" · Material DB code: "Standard" | `"CODE"` | string | - | **Required** |
| 2.2 | └ [General] Standard Code · KSCE-LSD15(RC) · KS01-Civil(RC) · KS-Civil(RC) · KS19(RC) · KS01(RC) · KS(RC) | `"STANDARD_CODE"` | string | - | Optional |
| 2.3 | └ [General] Grade of Main Rebar | `"MAIN_REBAR_GRADE"` | string | - | Optional |
| 2.4 | └ [General] Grade of Sub-Rebar | `"SUB_REBAR_GRADE"` | string | - | Optional |
| 2.5 | └ [When CODE = "None (user-defined)"] Name of Main Rebar | `"MAIN_REBAR_NAME"` | string | - | **Required** |
| 2.6 | └ [When CODE = "None (user-defined)"] Name of Sub-Rebar | `"SUB_REBAR_NAME"` | string | - | **Required** |
| 2.7 | └ [When CODE = "None (user-defined)"] Fy · Minimum: 0 | `"FY"` | number | - | **Required** |
| 2.8 | └ [When CODE = "None (user-defined)"] Fys · Minimum: 0 | `"FYS"` | number | - | **Required** |
| 2.3 | └ [When STANDARD_CODE in ["KSCE-LSD15(RC)", "KS01-Civil(RC)", "KS01(RC)"]] Grade of Main Rebar · SD240 · SD300 · SD350 · SD400 · SD500 · SD600 | `"MAIN_REBAR_GRADE"` | string | - | Optional |
| 2.4 | └ [When STANDARD_CODE in ["KSCE-LSD15(RC)", "KS01-Civil(RC)", "KS01(RC)"]] Grade of Sub-Rebar · SD240 · SD300 · SD350 · SD400 · SD500 · SD600 | `"SUB_REBAR_GRADE"` | string | - | Optional |
| 2.3 | └ [When STANDARD_CODE in ["KS-Civil(RC)", "KS(RC)"]] Grade of Main Rebar · SD24 · SD30 · SD35 · SD40 · SD50 | `"MAIN_REBAR_GRADE"` | string | - | Optional |
| 2.4 | └ [When STANDARD_CODE in ["KS-Civil(RC)", "KS(RC)"]] Grade of Sub-Rebar · SD24 · SD30 · SD35 · SD40 · SD50 | `"SUB_REBAR_GRADE"` | string | - | Optional |
| 2.3 | └ [When STANDARD_CODE = "KS19(RC)"] Grade of Main Rebar · SD300 · SD400 · SD500 · SD600 · SD700 · SD400S · SD500S · SD600S | `"MAIN_REBAR_GRADE"` | string | - | Optional |
| 2.4 | └ [When STANDARD_CODE = "KS19(RC)"] Grade of Sub-Rebar · SD300 · SD400 · SD500 · SD600 · SD700 · SD400S · SD500S · SD600S | `"SUB_REBAR_GRADE"` | string | - | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a concrete material ID string (e.g., \"1\"): an existing material whose design type is concrete",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Modify Concrete Materials",
          "type": "object",
          "required": [
            "CONCRETE",
            "REBAR"
          ],
          "additionalProperties": false,
          "properties": {
            "CONCRETE": {
              "type": "object",
              "description": "Concrete material for design",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "enum": [
                    "None",
                    "Standard"
                  ],
                  "description": "Concrete code kind: \"Standard\" = a Korean material DB code given in STANDARD_CODE; \"None\" = user-defined concrete"
                },
                "STANDARD_CODE": {
                  "type": "string",
                  "enum": [
                    "KSCE-LSD15(RC)",
                    "KS01-Civil(RC)",
                    "KS-Civil(RC)",
                    "KS19(RC)",
                    "KS01(RC)",
                    "KS(RC)"
                  ],
                  "description": "Korean material DB code of the concrete. Required when CODE is Standard"
                },
                "GRADE": {
                  "type": "string",
                  "description": "Concrete grade of STANDARD_CODE (list depends on the code). Required when CODE is Standard; fck is then taken from the DB"
                },
                "NAME": {
                  "type": "string",
                  "minLength": 1,
                  "description": "User-defined concrete name. Required when CODE is None (the Grade field becomes Name in the dialog)"
                },
                "FC": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "description": "Specified compressive strength fck, model stress unit, > 0. Required when CODE is None; ignored when CODE is Standard (the grade value is used)"
                }
              }
            },
            "REBAR": {
              "type": "object",
              "description": "Rebar material for design",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "enum": [
                    "None",
                    "Standard"
                  ],
                  "description": "Rebar code kind: \"Standard\" = a Korean material DB code given in STANDARD_CODE; \"None\" = user-defined rebar"
                },
                "STANDARD_CODE": {
                  "type": "string",
                  "enum": [
                    "KSCE-LSD15(RC)",
                    "KS01-Civil(RC)",
                    "KS-Civil(RC)",
                    "KS19(RC)",
                    "KS01(RC)",
                    "KS(RC)"
                  ],
                  "description": "Korean material DB code of the rebar. Required when CODE is Standard"
                },
                "MAIN_REBAR_GRADE": {
                  "type": "string",
                  "description": "Main rebar grade of STANDARD_CODE. Required when CODE is Standard; fy is then taken from the DB"
                },
                "SUB_REBAR_GRADE": {
                  "type": "string",
                  "description": "Sub-rebar (shear rebar) grade of STANDARD_CODE. Required when CODE is Standard; fys is then taken from the DB"
                },
                "MAIN_REBAR_NAME": {
                  "type": "string",
                  "minLength": 1,
                  "description": "User-defined main rebar name. Required when CODE is None"
                },
                "SUB_REBAR_NAME": {
                  "type": "string",
                  "minLength": 1,
                  "description": "User-defined sub-rebar name. Required when CODE is None"
                },
                "FY": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "description": "Main rebar yield strength fy, model stress unit, > 0. Required when CODE is None; ignored when CODE is Standard"
                },
                "FYS": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "description": "Sub-rebar yield strength fys, model stress unit, > 0. Required when CODE is None; ignored when CODE is Standard"
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

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `MATD`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "CONCRETE": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C30"
      },
      "REBAR": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD400",
        "SUB_REBAR_GRADE": "SD400"
      }
    }
  }
}
```

**Response**

```json
{
  "MATD": {
    "1": {
      "CONCRETE": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C30",
        "FC": 30000
      },
      "REBAR": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD400",
        "SUB_REBAR_GRADE": "SD400",
        "FY": 400000,
        "FYS": 400000
      }
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/MATD"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "CONCRETE": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C30"
      },
      "REBAR": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD400",
        "SUB_REBAR_GRADE": "SD400"
      }
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 12. `CMFT` — Moment Factor (Cm)

> **기능** 부재별 모멘트 계수 Cm을 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/CMFT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738323971737](https://support.midasuser.com/hc/ko/articles/64738323971737)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element ID string (e.g., "1"). Element Type = Element. Virtual beams use /DESIGN/RC/KDS-24-14-21-2021/CMFT-VBEAM. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Cmy · Range: 0~1 | `"CMY"` | number | 0 | Optional |
| 2 | [General] Cmz · Range: 0~1 | `"CMZ"` | number | 0 | Optional |
| 3 | [General] Calculate by Program | `"OPT_AUTO"` | boolean | false | Optional |

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
      "description": "Keyed object (dictionary). Each property name is an element ID string (e.g., \"1\"). Element Type = Element. Virtual beams use /DESIGN/RC/KDS-24-14-21-2021/CMFT-VBEAM.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Moment Factor(Cm)",
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "CMY": {
              "type": "number",
              "description": "Moment factor Cmy (set to 0 and disabled when OPT_AUTO is checked). Range 0.0 to 1.0. Values outside it are rejected",
              "default": 0,
              "minimum": 0,
              "maximum": 1
            },
            "CMZ": {
              "type": "number",
              "description": "Moment factor Cmz (set to 0 and disabled when OPT_AUTO is checked). Range 0.0 to 1.0. Values outside it are rejected",
              "default": 0,
              "minimum": 0,
              "maximum": 1
            },
            "OPT_AUTO": {
              "type": "boolean",
              "description": "Calculate Cm by program",
              "default": false
            }
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `CMFT`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "5": {
      "CMY": 0.85,
      "CMZ": 0.9
    }
  }
}
```

**Response**

```json
{
  "CMFT": {
    "5": {
      "CMY": 0.85,
      "CMZ": 0.9
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/CMFT"

payload = json.loads(r'''
{
  "Assign": {
    "5": {
      "CMY": 0.85,
      "CMZ": 0.9
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 13. `FMAG` — Moment Magnifier (B1/Delta_b, B2/Delta_s)

> **기능** 부재별 모멘트 확대계수 B1/δb와 B2/δs를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/FMAG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738301246745](https://support.midasuser.com/hc/ko/articles/64738301246745)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element ID string (e.g., "1"). Element Type = Element. Virtual beams use /DESIGN/RC/KDS-24-14-21-2021/FMAG-VBEAM. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] B1y\|Delta_by · Range: 1~100 | `"B1Y_DELTA_BY"` | number | 1 | Optional |
| 2 | [General] B1z\|Delta_bz · Range: 1~100 | `"B1Z_DELTA_BZ"` | number | 1 | Optional |
| 3 | [General] B2y\|Delta_sy · Range: 1~100 | `"B2Y_DELTA_SY"` | number | 1 | Optional |
| 4 | [General] B2z\|Delta_sz · Range: 1~100 | `"B2Z_DELTA_SZ"` | number | 1 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is an element ID string (e.g., \"1\"). Element Type = Element. Virtual beams use /DESIGN/RC/KDS-24-14-21-2021/FMAG-VBEAM.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Moment Magnifier(B1/Delta_b,B2/Delta_s)",
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "B1Y_DELTA_BY": {
              "type": "number",
              "description": "B1y|Delta_by (dialog initial value 0). Range 1.0 <= value < 100",
              "default": 1,
              "minimum": 1,
              "exclusiveMaximum": 100
            },
            "B1Z_DELTA_BZ": {
              "type": "number",
              "description": "B1z|Delta_bz (dialog initial value 0). Range 1.0 <= value < 100",
              "default": 1,
              "minimum": 1,
              "exclusiveMaximum": 100
            },
            "B2Y_DELTA_SY": {
              "type": "number",
              "description": "B2y|Delta_sy (dialog initial value 1). Range 1.0 <= value < 100",
              "default": 1,
              "minimum": 1,
              "exclusiveMaximum": 100
            },
            "B2Z_DELTA_SZ": {
              "type": "number",
              "description": "B2z|Delta_sz (dialog initial value 1). Range 1.0 <= value < 100",
              "default": 1,
              "minimum": 1,
              "exclusiveMaximum": 100
            }
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `FMAG`

### Request / Response JSON

**Request**

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
    },
    "1059": {
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1.3
    }
  }
}
```

**Response**

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
    },
    "1059": {
      "B1Y_DELTA_BY": 1,
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/FMAG"

payload = json.loads(r'''
{
  "Assign": {
    "915": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2
    },
    "1058": {
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    },
    "1059": {
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1.3
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 14. `SLTC` — Short/Long term Load Case

> **기능** 단기·장기 하중 케이스를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/SLTC
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738301388313](https://support.midasuser.com/hc/ko/articles/64738301388313)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Single settings record: the only accepted key is "1". | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Long-term | `"LONG_TERM_LOADS"` | array [object] | - | Optional |
| 1.1 | └ [General] Load Case | `"LOAD_CASE_NAME"` | string | - | **Required** |
| 2 | [General] Short-term | `"SHORT_TERM_LOADS"` | array [object] | - | Optional |
| 2.1 | └ [General] Load Case | `"LOAD_CASE_NAME"` | string | - | **Required** |

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
      "description": "Single settings record: the only accepted key is \"1\".",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "propertyNames": {
        "const": "1"
      },
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Short/Long term Load Case",
          "type": "object",
          "additionalProperties": false,
          "description": "Every load case of the model is in exactly one of the two dialog lists, Long-term or Short-term. PUT moves the listed load cases to the given list (like the dialog arrows); unlisted load cases keep their term. GET returns both lists. A new model starts with the long-term static load case types in Long-term",
          "properties": {
            "LONG_TERM_LOADS": {
              "type": "array",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "required": [
                  "LOAD_CASE_NAME"
                ],
                "properties": {
                  "LOAD_CASE_NAME": {
                    "type": "string",
                    "minLength": 1,
                    "description": "Name of an existing load case as shown in the dialog lists (static, response spectrum, time history or moving load case). An unknown name, or a name used by load cases of more than one type, rejects the request"
                  }
                }
              },
              "minItems": 1,
              "description": "Load cases to place in the Long-term list. Load cases not listed in either list keep their current term. A load case must not appear in both lists (rejected)"
            },
            "SHORT_TERM_LOADS": {
              "type": "array",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "required": [
                  "LOAD_CASE_NAME"
                ],
                "properties": {
                  "LOAD_CASE_NAME": {
                    "type": "string",
                    "minLength": 1,
                    "description": "Name of an existing load case as shown in the dialog lists (static, response spectrum, time history or moving load case). An unknown name, or a name used by load cases of more than one type, rejects the request"
                  }
                }
              },
              "minItems": 1,
              "description": "Load cases to place in the Short-term list. Load cases not listed in either list keep their current term. A load case must not appear in both lists (rejected)"
            }
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SLTC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "LONG_TERM_LOADS": [
        {
          "LOAD_CASE_NAME": "DW"
        }
      ],
      "SHORT_TERM_LOADS": [
        {
          "LOAD_CASE_NAME": "LL"
        }
      ]
    }
  }
}
```

**Response**

```json
{
  "SLTC": {
    "1": {
      "LONG_TERM_LOADS": [
        {
          "LOAD_CASE_NAME": "DC"
        },
        {
          "LOAD_CASE_NAME": "DW"
        }
      ],
      "SHORT_TERM_LOADS": [
        {
          "LOAD_CASE_NAME": "LL"
        },
        {
          "LOAD_CASE_NAME": "WS"
        }
      ]
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/SLTC"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "LONG_TERM_LOADS": [
        {
          "LOAD_CASE_NAME": "DW"
        }
      ],
      "SHORT_TERM_LOADS": [
        {
          "LOAD_CASE_NAME": "LL"
        }
      ]
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 15. `LENG` — Unbraced Length (L, Lb)

> **기능** 부재별 비지지 길이 L과 Lb를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/LENG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738331110681](https://support.midasuser.com/hc/ko/articles/64738331110681)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). Element Type = Element. Virtual beams use /DESIGN/RC/KDS-24-14-21-2021/LENG-VBEAM. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Ly · Minimum: 0 | `"LY"` | number | 0 | Optional |
| 2 | [General] Lz · Minimum: 0 | `"LZ"` | number | 0 | Optional |
| 3 | [General] Lb · Minimum: 0 | `"LB"` | number | 0 | Optional |
| 4 | [General] Do not consider | `"bNOTUSE"` | boolean | false | Optional |
| 3 | [When bNOTUSE = true] Lb · 0 · Minimum: 0 | `"LB"` | number | 0 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\"). Element Type = Element. Virtual beams use /DESIGN/RC/KDS-24-14-21-2021/LENG-VBEAM.",
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
              "description": "Unbraced length Ly. Must not be negative",
              "default": 0,
              "minimum": 0
            },
            "LZ": {
              "type": "number",
              "description": "Unbraced length Lz. Must not be negative",
              "default": 0,
              "minimum": 0
            },
            "LB": {
              "type": "number",
              "description": "Laterally unbraced length Lb. Must be 0 (or omitted) when bNOTUSE is true. Must not be negative",
              "default": 0,
              "minimum": 0
            },
            "bNOTUSE": {
              "type": "boolean",
              "description": "Do not consider the laterally unbraced length (Lb is set to 0 and disabled)",
              "default": false
            }
          },
          "title": "Unbraced Length(L,Lb)"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `LENG`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "888": {
      "LY": 1,
      "LZ": 1,
      "LB": 0,
      "bNOTUSE": true
    },
    "891": {
      "LY": 1,
      "LZ": 1,
      "LB": 2
    }
  }
}
```

**Response**

```json
{
  "LENG": {
    "888": {
      "LY": 1,
      "LZ": 1,
      "LB": 0,
      "bNOTUSE": true
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
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/LENG"

payload = json.loads(r'''
{
  "Assign": {
    "888": {
      "LY": 1,
      "LZ": 1,
      "LB": 0,
      "bNOTUSE": true
    },
    "891": {
      "LY": 1,
      "LZ": 1,
      "LB": 2
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 16. `REBT` — Column General Section Rebar

> **기능** 기둥의 일반 단면 철근을 입력합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/REBT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738324659225](https://support.midasuser.com/hc/ko/articles/64738324659225)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a section ID string (e.g., "4") of a general section. Writing a section deletes the member-level rebar (RBTE) of the elements that use it | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Origin Type · Centroid: "CENTROID" · Left-Bottom: "LEFT BOTTOM" | `"ORIGIN_TYPE"` | string | CENTROID | Optional |
| 2 | [General] Apply same rebar data to both I and J-end (Main Rebar) | `"SAME_IJ_MAIN"` | boolean | true | Optional |
| 3 | [General] Main Rebar (I) | `"MAIN_BAR_I"` | array [object] | - | Optional |
| 3.1 | └ [General] No. · Minimum: 1 | `"NUM"` | integer | - | Optional |
| 3.2 | └ [General] Rebar | `"NAME"` | string | - | Optional |
| 3.3 | └ [General] y | `"Y"` | number | - | Optional |
| 3.4 | └ [General] z | `"Z"` | number | - | Optional |
| 4 | [General] Main Rebar (J) | `"MAIN_BAR_J"` | array [object] | - | Optional |
| 4.1 | └ [General] No. · Minimum: 1 | `"NUM"` | integer | - | Optional |
| 4.2 | └ [General] Rebar | `"NAME"` | string | - | Optional |
| 4.3 | └ [General] y | `"Y"` | number | - | Optional |
| 4.4 | └ [General] z | `"Z"` | number | - | Optional |
| 5 | [General] Apply same rebar data to both I and J-end (Shear Rebar) | `"SAME_IJ_SHEAR"` | boolean | true | Optional |
| 6 | [General] Shear Rebar (I) | `"SHEAR_BAR_I"` | object | - | Optional |
| 6.1 | └ [General] Rebar | `"NAME"` | string | - | Optional |
| 6.2 | └ [General] Number on Y-Dir · Minimum: 0 | `"LEG_Y"` | integer | - | Optional |
| 6.3 | └ [General] Number on Z-Dir · Minimum: 0 | `"LEG_Z"` | integer | - | Optional |
| 6.4 | └ [General] Space on X-Dir · Minimum: 0 | `"DIST"` | number | - | Optional |
| 7 | [General] Shear Rebar (J) | `"SHEAR_BAR_J"` | object | - | Optional |
| 7.1 | └ [General] Rebar | `"NAME"` | string | - | Optional |
| 7.2 | └ [General] Number on Y-Dir · Minimum: 0 | `"LEG_Y"` | integer | - | Optional |
| 7.3 | └ [General] Number on Z-Dir · Minimum: 0 | `"LEG_Z"` | integer | - | Optional |
| 7.4 | └ [General] Space on X-Dir · Minimum: 0 | `"DIST"` | number | - | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a section ID string (e.g., \"4\") of a general section. Writing a section deletes the member-level rebar (RBTE) of the elements that use it",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Rebar Input for General Section",
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "ORIGIN_TYPE": {
              "type": "string",
              "default": "CENTROID",
              "description": "Origin the dialog shows the coordinates in. Y and Z are always centroid-relative regardless of this value. Omitted on PUT keeps the stored value, on POST the default",
              "enum": [
                "CENTROID",
                "LEFT BOTTOM"
              ]
            },
            "SAME_IJ_MAIN": {
              "type": "boolean",
              "default": true,
              "description": "Apply same rebar data to both I and J-end (Main Rebar tab). When true the J-end main bars are copied from the I end on save, so MAIN_BAR_J is discarded"
            },
            "MAIN_BAR_I": {
              "type": "array",
              "description": "I-end main bars (Main Rebar tab, I). Omitting the array leaves the stored bars unchanged; when present, entries are merged by NUM. At least one bar must remain. Collection items are paired with the stored items by request position and missing properties are filled in from them, so read the record with GET, edit it and send every property of every item back. A bar cannot be removed with PUT: to remove bars, DELETE the record and POST the bars to keep",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "NUM": {
                    "type": "integer",
                    "description": "Bar number in this collection. Matches a stored bar to update it (bars are never removed by PUT); on POST a number that is not stored appends. Every save renumbers the collection to 1..N, so re-read the record before reusing it",
                    "minimum": 1
                  },
                  "NAME": {
                    "type": "string",
                    "description": "Bar size (Dia). Required when the bar is appended. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected"
                  },
                  "Y": {
                    "type": "number",
                    "description": "Bar centre, section local y, from the section design centroid (current length unit). Always centroid-relative, whatever ORIGIN_TYPE is. Required when the bar is appended"
                  },
                  "Z": {
                    "type": "number",
                    "description": "Bar centre, section local z, from the section design centroid (current length unit). Always centroid-relative, whatever ORIGIN_TYPE is. Required when the bar is appended"
                  }
                }
              }
            },
            "MAIN_BAR_J": {
              "type": "array",
              "description": "J-end main bars (Main Rebar tab, J). Used only when SAME_IJ_MAIN is false; then at least one bar must remain. Same item rule as MAIN_BAR_I: send every property of every item. A bar cannot be removed with PUT: to remove bars, DELETE the record and POST the bars to keep",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "NUM": {
                    "type": "integer",
                    "description": "Bar number in this collection. Matches a stored bar to update it (bars are never removed by PUT); on POST a number that is not stored appends. Every save renumbers the collection to 1..N, so re-read the record before reusing it",
                    "minimum": 1
                  },
                  "NAME": {
                    "type": "string",
                    "description": "Bar size (Dia). Required when the bar is appended. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected"
                  },
                  "Y": {
                    "type": "number",
                    "description": "Bar centre, section local y, from the section design centroid (current length unit). Always centroid-relative, whatever ORIGIN_TYPE is. Required when the bar is appended"
                  },
                  "Z": {
                    "type": "number",
                    "description": "Bar centre, section local z, from the section design centroid (current length unit). Always centroid-relative, whatever ORIGIN_TYPE is. Required when the bar is appended"
                  }
                }
              }
            },
            "SAME_IJ_SHEAR": {
              "type": "boolean",
              "default": true,
              "description": "Apply same rebar data to both I and J-end (Shear Rebar tab). When true SHEAR_BAR_J is copied from SHEAR_BAR_I on save"
            },
            "SHEAR_BAR_I": {
              "type": "object",
              "additionalProperties": false,
              "description": "I-end shear (stirrup) bar (Shear Rebar tab, I). Omitted leaves the stored value unchanged",
              "properties": {
                "NAME": {
                  "type": "string",
                  "description": "Hoop bar size. The empty string means no hoop bar (the state of a new record), so a GET result can be sent back unchanged. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected"
                },
                "LEG_Y": {
                  "type": "integer",
                  "description": "Number of legs in section local y",
                  "minimum": 0
                },
                "LEG_Z": {
                  "type": "integer",
                  "description": "Number of legs in section local z",
                  "minimum": 0
                },
                "DIST": {
                  "type": "number",
                  "description": "Longitudinal hoop spacing in section local x (current length unit)",
                  "minimum": 0
                }
              }
            },
            "SHEAR_BAR_J": {
              "type": "object",
              "additionalProperties": false,
              "description": "J-end shear (stirrup) bar (Shear Rebar tab, J). Omitted leaves the stored value unchanged. Overwritten from SHEAR_BAR_I when SAME_IJ_SHEAR is true",
              "properties": {
                "NAME": {
                  "type": "string",
                  "description": "Hoop bar size. The empty string means no hoop bar (the state of a new record), so a GET result can be sent back unchanged. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected"
                },
                "LEG_Y": {
                  "type": "integer",
                  "description": "Number of legs in section local y",
                  "minimum": 0
                },
                "LEG_Z": {
                  "type": "integer",
                  "description": "Number of legs in section local z",
                  "minimum": 0
                },
                "DIST": {
                  "type": "number",
                  "description": "Longitudinal hoop spacing in section local x (current length unit)",
                  "minimum": 0
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

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `REBT`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "4": {
      "ORIGIN_TYPE": "CENTROID",
      "SAME_IJ_MAIN": true,
      "MAIN_BAR_I": [
        {
          "NUM": 1,
          "NAME": "D25",
          "Y": 220,
          "Z": 220
        },
        {
          "NUM": 2,
          "NAME": "D25",
          "Y": -220,
          "Z": 220
        },
        {
          "NUM": 3,
          "NAME": "D25",
          "Y": -220,
          "Z": -220
        },
        {
          "NUM": 4,
          "NAME": "D25",
          "Y": 220,
          "Z": -220
        }
      ],
      "SAME_IJ_SHEAR": true,
      "SHEAR_BAR_I": {
        "NAME": "D13",
        "LEG_Y": 2,
        "LEG_Z": 2,
        "DIST": 150
      }
    }
  }
}
```

**Response**

```json
{
  "REBT": {
    "4": {
      "ORIGIN_TYPE": "CENTROID",
      "SAME_IJ_MAIN": true,
      "MAIN_BAR_I": [
        {
          "NUM": 1,
          "NAME": "D25",
          "Y": 220,
          "Z": 220
        },
        {
          "NUM": 2,
          "NAME": "D25",
          "Y": -220,
          "Z": 220
        },
        {
          "NUM": 3,
          "NAME": "D25",
          "Y": -220,
          "Z": -220
        },
        {
          "NUM": 4,
          "NAME": "D25",
          "Y": 220,
          "Z": -220
        }
      ],
      "MAIN_BAR_J": [
        {
          "NUM": 1,
          "NAME": "D25",
          "Y": 220,
          "Z": 220
        },
        {
          "NUM": 2,
          "NAME": "D25",
          "Y": -220,
          "Z": 220
        },
        {
          "NUM": 3,
          "NAME": "D25",
          "Y": -220,
          "Z": -220
        },
        {
          "NUM": 4,
          "NAME": "D25",
          "Y": 220,
          "Z": -220
        }
      ],
      "SAME_IJ_SHEAR": true,
      "SHEAR_BAR_I": {
        "NAME": "D13",
        "LEG_Y": 2,
        "LEG_Z": 2,
        "DIST": 150
      },
      "SHEAR_BAR_J": {
        "NAME": "D13",
        "LEG_Y": 2,
        "LEG_Z": 2,
        "DIST": 150
      }
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/REBT"

payload = json.loads(r'''
{
  "Assign": {
    "4": {
      "ORIGIN_TYPE": "CENTROID",
      "SAME_IJ_MAIN": true,
      "MAIN_BAR_I": [
        {
          "NUM": 1,
          "NAME": "D25",
          "Y": 220,
          "Z": 220
        },
        {
          "NUM": 2,
          "NAME": "D25",
          "Y": -220,
          "Z": 220
        },
        {
          "NUM": 3,
          "NAME": "D25",
          "Y": -220,
          "Z": -220
        },
        {
          "NUM": 4,
          "NAME": "D25",
          "Y": 220,
          "Z": -220
        }
      ],
      "SAME_IJ_SHEAR": true,
      "SHEAR_BAR_I": {
        "NAME": "D13",
        "LEG_Y": 2,
        "LEG_Z": 2,
        "DIST": 150
      }
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 17. `RIBC` — Rebar Input (Beam, Column Section)

> **기능** 보와 기둥 단면의 철근 데이터를 입력합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/RIBC
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738316031641](https://support.midasuser.com/hc/ko/articles/64738316031641)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a design section ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Member Type · Beam Section: "BEAM" · Column Section: "COLUMN" | `"MEMBTYPE"` | string | - | **Required** |
| 2 | [General] Crack Checking · Dry: 0 · Humidity: 1 · Corrosion: 2 · High Corrosion: 3 | `"ENVTYPE"` | integer | - | Optional |
| 3 | [When MEMBTYPE = "Beam Section"] Beam Section | `"BEAM"` ¹⁾ | object | - | **Required** |
| 4 | [When MEMBTYPE = "Column Section"] Column Section | `"COLM"` ²⁾ | object | - | **Required** |

**Beam Section ¹⁾**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Same as i-Node (I, M, J) | `"OPTION_IMJSAME"` | boolean | false | Optional |
| 2 | Main Rebar | `"vMAIN"` | array [object] | - | Optional |
| 2.1 | └ Position · i-Node: "I" · middle: "M" · j-Node: "J" | `"SECTOR"` | string | - | **Required** |
| 2.2 | └ Top | `"POS_TOP_LAYERS"` | array [object] | - | Optional |
| 2.2.1 | 　　└ Layer · Range: 1~10 | `"LAYER"` | integer | - | **Required** |
| 2.2.2 | 　　└ Num · Minimum: 1 | `"BAR_NUM"` | integer | - | **Required** |
| 2.2.3 | 　　└ Size1 | `"BAR_NAME1"` | string | - | **Required** |
| 2.2.4 | 　　└ Size2 | `"BAR_NAME2"` | string |  | Optional |
| 2.2.5 | 　　└ Dt · Minimum: 0 | `"dD"` | number | - | **Required** |
| 2.3 | └ Bottom | `"POS_BOT_LAYERS"` | array [object] | - | Optional |
| 2.3.1 | 　　└ Layer · Range: 1~10 | `"LAYER"` | integer | - | **Required** |
| 2.3.2 | 　　└ Num · Minimum: 1 | `"BAR_NUM"` | integer | - | **Required** |
| 2.3.3 | 　　└ Size1 | `"BAR_NAME1"` | string | - | **Required** |
| 2.3.4 | 　　└ Size2 | `"BAR_NAME2"` | string |  | Optional |
| 2.3.5 | 　　└ Db · Minimum: 0 | `"dD"` | number | - | **Required** |
| 3 | Stirrups | `"vSUB_BAR"` | array [object] | - | Optional |
| 3.1 | └ Position · i-Node: "I" · middle: "M" · j-Node: "J" | `"SECTOR"` | string | - | **Required** |
| 3.2 | └ Size | `"SUB_BARNAME"` | string | - | **Required** |
| 3.3 | └ Spacing · Minimum: 0 | `"dSUB_BARDIST"` | number | - | **Required** |
| 3.4 | └ Number · Range: 2~99 | `"dSUB_BARNUM"` | number | - | **Required** |
| 3.5 | └ Angle | `"dSUB_BARANGLE"` | number | - | Optional |

**Column Section ²⁾**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Rebar Data | `"vLAYER"` | array [object] | - | Optional |
| 1.1 | └ Layer · Range: 1~5 | `"INDEX"` | integer | - | **Required** |
| 1.2 | └ Dc · Minimum: 0 | `"dDc"` | number | - | **Required** |
| 1.3 | └ Positions | `"vPOSITION"` | array [object] | - | **Required** |
| 1.3.1 | 　　└ Position · Pos1: "P1" · Pos2: "P2" · Pos3: "P3" | `"POSITION"` | string | - | **Required** |
| 1.3.2 | 　　└ Div. N · Minimum: 0 | `"BAR_NUM"` | integer | - | **Required** |
| 1.3.3 | 　　└ Size1 | `"BAR_NAME1"` | string | - | **Required** |
| 1.3.4 | 　　└ Size2 | `"BAR_NAME2"` | string |  | Optional |
| 2 | Type of Hoop Rebar | `"SUB_BAR"` | object | - | Optional |
| 2.1 | └ Ties/Spirals Size | `"SUBBAR_NAME"` | string | - | **Required** |
| 2.2 | └ Space · Minimum: 0 | `"SUBBAR_DIST"` | number | - | **Required** |
| 2.3 | └ Number · Range: 2~99 | `"SUBBAR_NUM"` | number | - | Optional |
| 2.4 | └ Number y · Range: 2~99 | `"SUBBAR_NUM_Y"` | number | - | Optional |
| 2.5 | └ Number z · Range: 2~99 | `"SUBBAR_NUM_Z"` | number | - | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a design section ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Rebar Input",
          "type": "object",
          "required": [
            "MEMBTYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "MEMBTYPE": {
              "type": "string",
              "description": "Member type of the section record. Writing one type makes the record that type",
              "enum": [
                "BEAM",
                "COLUMN"
              ]
            },
            "ENVTYPE": {
              "type": "integer",
              "description": "Crack Checking exposure condition (beam section). Omitted keeps the stored value",
              "enum": [
                0,
                1,
                2,
                3
              ]
            },
            "BEAM": {
              "type": "object",
              "description": "Beam Section Data for Checking. Required when MEMBTYPE is BEAM (not read otherwise)",
              "additionalProperties": false,
              "properties": {
                "OPTION_IMJSAME": {
                  "type": "boolean",
                  "default": false,
                  "description": "When true, after the merge the i-Node data are copied to middle and j-Node (not stored)"
                },
                "vMAIN": {
                  "type": "array",
                  "description": "Main rebar per position. Merged by SECTOR (each SECTOR at most once); positions not listed are left alone. Collection items are paired with the stored items by request position and missing properties are filled in from them, so read the record with GET, edit it and send every property of every item back",
                  "maxItems": 3,
                  "items": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": [
                      "SECTOR"
                    ],
                    "properties": {
                      "SECTOR": {
                        "type": "string",
                        "description": "Position along the member",
                        "enum": [
                          "I",
                          "M",
                          "J"
                        ]
                      },
                      "POS_TOP_LAYERS": {
                        "type": "array",
                        "description": "Complete top layer set of this position. Omitting the array leaves the stored top layers unchanged; when present it replaces them (slots not listed are cleared). Collection items are paired with the stored items by request position and missing properties are filled in from them, so read the record with GET, edit it and send every property of every item back",
                        "items": {
                          "type": "object",
                          "additionalProperties": false,
                          "required": [
                            "LAYER",
                            "dD",
                            "BAR_NUM",
                            "BAR_NAME1"
                          ],
                          "properties": {
                            "LAYER": {
                              "type": "integer",
                              "description": "Top layer slot 1 to 10 (slot number, not list position; a skipped number stays an empty layer)",
                              "minimum": 1,
                              "maximum": 10
                            },
                            "BAR_NUM": {
                              "type": "integer",
                              "description": "Number of bars in this layer, 1 or more",
                              "minimum": 1
                            },
                            "BAR_NAME1": {
                              "type": "string",
                              "description": "Size1 (primary bar size). Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected"
                            },
                            "BAR_NAME2": {
                              "type": "string",
                              "description": "Size2 (secondary bar size). Optional; empty on a new record. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected",
                              "default": ""
                            },
                            "dD": {
                              "type": "number",
                              "description": "Cover to this top layer (Dt). Greater than 0 and at most the limit for the section shape",
                              "exclusiveMinimum": 0
                            }
                          }
                        }
                      },
                      "POS_BOT_LAYERS": {
                        "type": "array",
                        "description": "Complete bottom layer set of this position. Omitting the array leaves the stored bottom layers unchanged; when present it replaces them (slots not listed are cleared). Collection items are paired with the stored items by request position and missing properties are filled in from them, so read the record with GET, edit it and send every property of every item back",
                        "items": {
                          "type": "object",
                          "additionalProperties": false,
                          "required": [
                            "LAYER",
                            "dD",
                            "BAR_NUM",
                            "BAR_NAME1"
                          ],
                          "properties": {
                            "LAYER": {
                              "type": "integer",
                              "description": "Bottom layer slot 1 to 10 (slot number, not list position; a skipped number stays an empty layer)",
                              "minimum": 1,
                              "maximum": 10
                            },
                            "BAR_NUM": {
                              "type": "integer",
                              "description": "Number of bars in this layer, 1 or more",
                              "minimum": 1
                            },
                            "BAR_NAME1": {
                              "type": "string",
                              "description": "Size1 (primary bar size). Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected"
                            },
                            "BAR_NAME2": {
                              "type": "string",
                              "description": "Size2 (secondary bar size). Optional; empty on a new record. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected",
                              "default": ""
                            },
                            "dD": {
                              "type": "number",
                              "description": "Cover to this bottom layer (Db). Greater than 0 and at most the limit for the section shape",
                              "exclusiveMinimum": 0
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "vSUB_BAR": {
                  "type": "array",
                  "description": "Stirrups per position. Merged by SECTOR (each SECTOR at most once); positions not listed are left alone. Collection items are paired with the stored items by request position and missing properties are filled in from them, so read the record with GET, edit it and send every property of every item back",
                  "maxItems": 3,
                  "items": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": [
                      "SECTOR",
                      "dSUB_BARNUM",
                      "SUB_BARNAME",
                      "dSUB_BARDIST"
                    ],
                    "properties": {
                      "SECTOR": {
                        "type": "string",
                        "description": "Position along the member",
                        "enum": [
                          "I",
                          "M",
                          "J"
                        ]
                      },
                      "SUB_BARNAME": {
                        "type": "string",
                        "description": "Stirrup size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected",
                        "minLength": 1
                      },
                      "dSUB_BARDIST": {
                        "type": "number",
                        "description": "Stirrup spacing, greater than 0",
                        "exclusiveMinimum": 0
                      },
                      "dSUB_BARNUM": {
                        "type": "number",
                        "description": "Number of stirrup legs, 2 to 99",
                        "minimum": 2,
                        "maximum": 99
                      },
                      "dSUB_BARANGLE": {
                        "type": "number",
                        "description": "Stirrup angle in degrees (90 on a new record). Collection items are paired with the stored items by request position and missing properties are filled in from them, so read the record with GET, edit it and send every property of every item back"
                      }
                    }
                  }
                }
              }
            },
            "COLM": {
              "type": "object",
              "description": "Column Section Data for Checking. Required when MEMBTYPE is COLUMN (not read otherwise)",
              "additionalProperties": false,
              "properties": {
                "vLAYER": {
                  "type": "array",
                  "description": "Complete layer set. Omitting the array leaves the stored layers unchanged; when present it replaces them. Collection items are paired with the stored items by request position and missing properties are filled in from them, so read the record with GET, edit it and send every property of every item back",
                  "maxItems": 5,
                  "items": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": [
                      "INDEX",
                      "dDc",
                      "vPOSITION"
                    ],
                    "properties": {
                      "INDEX": {
                        "type": "integer",
                        "description": "Layer slot 1 to 5 (slot number, not list position)",
                        "minimum": 1,
                        "maximum": 5
                      },
                      "dDc": {
                        "type": "number",
                        "description": "Cover to this layer (Dc). Greater than 0 and at most the limit for the section shape",
                        "exclusiveMinimum": 0
                      },
                      "vPOSITION": {
                        "type": "array",
                        "description": "Bars of this layer by position (each POSITION at most once). Collection items are paired with the stored items by request position and missing properties are filled in from them, so read the record with GET, edit it and send every property of every item back",
                        "maxItems": 3,
                        "items": {
                          "type": "object",
                          "additionalProperties": false,
                          "required": [
                            "POSITION",
                            "BAR_NUM",
                            "BAR_NAME1"
                          ],
                          "properties": {
                            "POSITION": {
                              "type": "string",
                              "description": "Rebar position of the layer. Only positions the section shape provides are accepted: circular/pipe P1, SB/B/TRK/STRK/H P1-P2, others P1-P3",
                              "enum": [
                                "P1",
                                "P2",
                                "P3"
                              ]
                            },
                            "BAR_NUM": {
                              "type": "integer",
                              "description": "Number of bars at this position (Div. N), 0 or more",
                              "minimum": 0
                            },
                            "BAR_NAME1": {
                              "type": "string",
                              "description": "Size1 (primary bar size). Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected"
                            },
                            "BAR_NAME2": {
                              "type": "string",
                              "description": "Size2 (secondary bar size). Optional; empty on a new record. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected",
                              "default": ""
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "SUB_BAR": {
                  "type": "object",
                  "description": "Ties / spirals (Type of Hoop Rebar). Omitted leaves the stored value unchanged. The leg count form follows the section shape: SUBBAR_NUM for circular and pipe sections, SUBBAR_NUM_Y / SUBBAR_NUM_Z for other shapes (the other form is rejected)",
                  "additionalProperties": false,
                  "required": [
                    "SUBBAR_NAME",
                    "SUBBAR_DIST"
                  ],
                  "properties": {
                    "SUBBAR_NAME": {
                      "type": "string",
                      "description": "Ties/Spirals size (also used for the y and z directions). Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected"
                    },
                    "SUBBAR_DIST": {
                      "type": "number",
                      "description": "Tie / spiral spacing, greater than 0",
                      "exclusiveMinimum": 0
                    },
                    "SUBBAR_NUM": {
                      "type": "number",
                      "description": "Number of tie legs, 2 to 99. Circular and pipe sections only (applied to y and z together)",
                      "minimum": 2,
                      "maximum": 99
                    },
                    "SUBBAR_NUM_Y": {
                      "type": "number",
                      "description": "Number of tie legs along y, 2 to 99. Sections other than circular and pipe only",
                      "minimum": 2,
                      "maximum": 99
                    },
                    "SUBBAR_NUM_Z": {
                      "type": "number",
                      "description": "Number of tie legs along z, 2 to 99. Sections other than circular and pipe only",
                      "minimum": 2,
                      "maximum": 99
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

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `RIBC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "2": {
      "MEMBTYPE": "BEAM",
      "ENVTYPE": 2,
      "BEAM": {
        "OPTION_IMJSAME": true,
        "vMAIN": [
          {
            "SECTOR": "I",
            "POS_TOP_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.05,
                "BAR_NUM": 4,
                "BAR_NAME1": "D22",
                "BAR_NAME2": ""
              }
            ],
            "POS_BOT_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.05,
                "BAR_NUM": 4,
                "BAR_NAME1": "D22",
                "BAR_NAME2": "D22"
              }
            ]
          }
        ],
        "vSUB_BAR": [
          {
            "SECTOR": "I",
            "dSUB_BARNUM": 2,
            "SUB_BARNAME": "D13",
            "dSUB_BARDIST": 0.15,
            "dSUB_BARANGLE": 90
          }
        ]
      }
    }
  }
}
```

**Response**

```json
{
  "RIBC": {
    "2": {
      "MEMBTYPE": "BEAM",
      "ENVTYPE": 2,
      "BEAM": {
        "OPTION_IMJSAME": true,
        "vMAIN": [
          {
            "SECTOR": "I",
            "POS_TOP_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.05,
                "BAR_NUM": 4,
                "BAR_NAME1": "D22",
                "BAR_NAME2": ""
              }
            ],
            "POS_BOT_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.05,
                "BAR_NUM": 4,
                "BAR_NAME1": "D22",
                "BAR_NAME2": "D22"
              }
            ]
          }
        ],
        "vSUB_BAR": [
          {
            "SECTOR": "I",
            "dSUB_BARNUM": 2,
            "SUB_BARNAME": "D13",
            "dSUB_BARDIST": 0.15,
            "dSUB_BARANGLE": 90
          }
        ]
      }
    }
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/RIBC"

payload = json.loads(r'''
{
  "Assign": {
    "2": {
      "MEMBTYPE": "BEAM",
      "ENVTYPE": 2,
      "BEAM": {
        "OPTION_IMJSAME": true,
        "vMAIN": [
          {
            "SECTOR": "I",
            "POS_TOP_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.05,
                "BAR_NUM": 4,
                "BAR_NAME1": "D22",
                "BAR_NAME2": ""
              }
            ],
            "POS_BOT_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.05,
                "BAR_NUM": 4,
                "BAR_NAME1": "D22",
                "BAR_NAME2": "D22"
              }
            ]
          }
        ],
        "vSUB_BAR": [
          {
            "SECTOR": "I",
            "dSUB_BARNUM": 2,
            "SUB_BARNAME": "D13",
            "dSUB_BARDIST": 0.15,
            "dSUB_BARANGLE": 90
          }
        ]
      }
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 18. `PERFORM-DESIGN` — Perform Design

> **기능** 교량 RC 부재의 설계를 실행합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-24-14-21-2021/PERFORM-DESIGN
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738331596057](https://support.midasuser.com/hc/ko/articles/64738331596057)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Perform Design: hands the elements over to the external design program UMD (midas UMD) with the options of the UMD Select Position dialog. Needs analysis results, an installed UMD and the LSD option licence. Design results stay in UMD (no Civil result table) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Elements | `"ELEMS"` | object | - | Optional |
| 1.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 1.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 2 | [General] Seismic Performance | `"SEISMIC"` | boolean | false | Optional |
| 3 | [When SEISMIC = true] Select RC Design · COLUMN | `"RC_TYPE"` | string | BEAM | **Required** |
| 4 | [When SEISMIC = true] Auto Design | `"RC_AUTO"` | boolean | false | Optional |
| 5 | [When SEISMIC = true] I | `"POS_I"` | boolean | true | Optional |
| 6 | [When SEISMIC = true] Mid | `"POS_M"` | boolean | false | Optional |
| 7 | [When SEISMIC = true] J | `"POS_J"` | boolean | true | Optional |
| 8 | [When SEISMIC = true] UMD Mode · List: "LIST" · Optimum: "OPTIMUM" · Edit: "EDIT" | `"UMD_MODE"` | string | LIST | Optional |

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
      "description": "Perform Design: hands the elements over to the external design program UMD (midas UMD) with the options of the UMD Select Position dialog. Needs analysis results, an installed UMD and the LSD option licence. Design results stay in UMD (no Civil result table)",
      "properties": {
        "ELEMS": {
          "type": "object",
          "description": "Element selection (the elements selected before Perform Design). Omitted = connect UMD only (nothing is handed over).",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID (element numbers)",
              "items": {
                "type": "integer",
                "minimum": 1
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g. '1to160'; '1-10' is also accepted)"
            }
          }
        },
        "SEISMIC": {
          "type": "boolean",
          "default": false,
          "description": "Seismic Performance. Columns only (RC_TYPE COLUMN or RC_AUTO); needs the seismic performance option licence"
        },
        "RC_TYPE": {
          "type": "string",
          "default": "BEAM",
          "description": "Select RC Design: member type the elements are designed as. Ignored when RC_AUTO is true; must be COLUMN when SEISMIC is true",
          "enum": [
            "BEAM",
            "COLUMN",
            "WALL"
          ]
        },
        "RC_AUTO": {
          "type": "boolean",
          "default": false,
          "description": "Auto Design: beam, column and wall together, UMD classifies the members"
        },
        "POS_I": {
          "type": "boolean",
          "default": true,
          "description": "Design Position I"
        },
        "POS_M": {
          "type": "boolean",
          "default": false,
          "description": "Design Position Mid. No effect for a column (RC_TYPE COLUMN without RC_AUTO)"
        },
        "POS_J": {
          "type": "boolean",
          "default": true,
          "description": "Design Position J"
        },
        "UMD_MODE": {
          "type": "string",
          "default": "LIST",
          "description": "UMD Mode: view UMD switches to after the hand-off",
          "enum": [
            "LIST",
            "OPTIMUM",
            "EDIT"
          ]
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `message`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "ELEMS": {
      "KEYS": [
        1,
        2,
        3,
        4
      ]
    },
    "SEISMIC": false,
    "RC_TYPE": "BEAM",
    "RC_AUTO": false,
    "POS_I": true,
    "POS_M": true,
    "POS_J": true,
    "UMD_MODE": "LIST"
  }
}
```

**Response**

```json
{
  "message": "success"
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-24-14-21-2021/PERFORM-DESIGN"

payload = json.loads(r'''
{
  "Argument": {
    "ELEMS": {
      "KEYS": [
        1,
        2,
        3,
        4
      ]
    },
    "SEISMIC": false,
    "RC_TYPE": "BEAM",
    "RC_AUTO": false,
    "POS_I": true,
    "POS_M": true,
    "POS_J": true,
    "UMD_MODE": "LIST"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```
