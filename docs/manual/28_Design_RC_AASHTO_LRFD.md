# 28. Design Code – RC AASHTO-LRFD24 / LRFD20 (교량 철근콘크리트 설계)

> **예제 Base URL (MIDAS Civil NX)** `https://moa-engineers.midasit.com:443/civil`  
> **인증 헤더** `MAPI-Key: <발급된 키>`  
> **공식 하위 목차** [AASHTO-LRFD24 RC](https://support.midasuser.com/hc/en-us/articles/64738422777881) · [AASHTO-LRFD20 RC](https://support.midasuser.com/hc/en-us/articles/64738411036185)

AASHTO-LRFD24 및 LRFD20 교량 철근콘크리트(RC) 설계의 **코드별 50개 절과 공용 DRC 1개 절**을 다룹니다.
코드별 절에는 두 판의 Input URI가 있으며, 공용 DRC를 포함한 고유 URI는 **101개**입니다.

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/<CODE>`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/<CODE>`
- **설계 기준 선택** `{base url}/DESIGN/RC/DRC`

설정 요청에는 `"Assign"` 객체를, 설계·검토 수행, 결과 표, 보고서 요청에는 `"Argument"` 객체를 사용합니다.
두 판의 공통 표와 Schema는 한 번 싣고, 요청이나 응답 예제가 달라지는 절에는 판을 표시했습니다.

---

## Endpoint 목록 (51개 절)

| No. | Endpoint | 기능 | Active Methods |
| --- | --- | --- | --- |
| 0 | [`DRC`](#0-designrcdrc--design-code-aashto-lrfd2420) | 프로젝트의 RC 설계 기준을 AASHTO-LRFD24 또는 AASHTO-LRFD20으로 설정하거나 조회합니다. | GET · PUT · DELETE |
| 1 | [`DCO`](#1-dco--design-code-option) | RC 설계 기준, 내진 특례 적용, 내진 구역, 판 기둥의 축력·모멘트 상호작용 및 보의 모멘트 재분배 옵션을 설정합니다. | GET · PUT · DELETE |
| 2 | [`DCTL`](#2-dctl--definition-of-frame) | 프레임의 설계 조건을 정의합니다. | GET · PUT · DELETE |
| 3 | [`LCTB`](#3-lctb--load-contribution-for-nonlinear-load-case) | 비선형 하중 케이스에 기여하는 하중과 계수를 조회합니다. | GET · DELETE |
| 4 | [`SRDF`](#4-srdf--strength-reduction-factors) | 인장·압축·전단 및 비틀림에 적용할 강도 감소계수를 설정합니다. | GET · PUT · DELETE |
| 5 | [`SLTC`](#5-sltc--shortlong-term-load-case) | 단기·장기 하중 케이스를 지정합니다. | GET · PUT · DELETE |
| 6 | [`LMRR`](#6-lmrr--limiting-maximum-rebar-ratio) | 최대 철근비 제한을 설정합니다. | GET · PUT · DELETE |
| 7 | [`MATD`](#7-matd--modify-rc-materials) | RC 설계에 사용할 콘크리트와 철근 재료를 수정합니다. | GET · PUT · DELETE |
| 8 | [`MBTP`](#8-mbtp--modify-member-type) | 지정한 요소의 부재 유형을 수정합니다. | POST · GET · PUT · DELETE |
| 9 | [`MEMB`](#9-memb--member-assignment) | RC 설계 대상 요소의 부재 배정을 관리합니다. | POST · GET · PUT · DELETE |
| 10 | [`OPE_MEMB`](#10-ope_memb--auto-member-assignment) | 설계 대상 요소를 RC 부재로 자동 배정합니다. | POST |
| 11 | [`LENG`](#11-leng--unbraced-length-l-lb) | 부재별 비지지 길이 L과 Lb를 지정합니다. | POST · GET · PUT · DELETE |
| 12 | [`KFAC`](#12-kfac--effective-length-factor-k) | 부재별 유효길이계수 K를 지정합니다. | POST · GET · PUT · DELETE |
| 13 | [`CMFT`](#13-cmft--moment-factor-cm) | 부재별 모멘트 계수 Cm을 지정합니다. | POST · GET · PUT · DELETE |
| 14 | [`FMAG`](#14-fmag--moment-magnifier-b1delta_b-b2delta_s) | 부재별 모멘트 확대계수 B1/δb와 B2/δs를 지정합니다. | POST · GET · PUT · DELETE |
| 15 | [`LTSR`](#15-ltsr--limiting-slenderness-ratio) | 부재별 세장비 한계를 설정합니다. | POST · GET · PUT · DELETE |
| 16 | [`RMFR`](#16-rmfr--response-modification-factor-r) | 부재별 응답수정계수 R을 지정합니다. | POST · GET · PUT · DELETE |
| 17 | [`SUFC`](#17-sufc--scale-up-factor-for-column) | 기둥의 스케일업 계수를 지정합니다. | POST · GET · PUT · DELETE |
| 18 | [`RDGN`](#18-rdgn--rebar-input-for-design-beam-column-section) | 보·기둥 단면의 설계용 철근 데이터를 입력합니다. | GET · PUT · DELETE |
| 19 | [`RCHK`](#19-rchk--rebar-input-for-checking-beam-column-section) | 보·기둥 단면의 검토용 철근 데이터를 입력합니다. | GET · PUT · DELETE |
| 20 | [`REBT`](#20-rebt--column-general-section-rebar) | 기둥의 일반 단면 철근을 입력합니다. | POST · GET · PUT · DELETE |
| 21 | [`RIPB`](#21-ripb--rebar-input-for-plate-beam) | 판 보의 철근 배치를 입력합니다. | POST · GET · PUT · DELETE |
| 22 | [`RIPC`](#22-ripc--rebar-input-for-plate-column) | 판 기둥의 철근 배치를 입력합니다. | POST · GET · PUT · DELETE |
| 23 | [`PBDD`](#23-pbdd--plate-beam-data-for-design) | 판 보의 설계용 데이터를 입력합니다. | POST · GET · PUT · DELETE |
| 24 | [`PBDC`](#24-pbdc--plate-beam-data-for-checking) | 판 보의 검토용 데이터를 입력합니다. | POST · GET · PUT · DELETE |
| 25 | [`PCDD`](#25-pcdd--plate-column-data-for-design) | 판 기둥의 설계용 데이터를 입력합니다. | POST · GET · PUT · DELETE |
| 26 | [`PCDC`](#26-pcdc--plate-column-data-for-checking) | 판 기둥의 검토용 데이터를 입력합니다. | POST · GET · PUT · DELETE |
| 27 | [`BD-ANAL`](#27-bd-anal--beam-design-perform) | 보 설계를 수행합니다. | POST |
| 28 | [`BD-TABLE`](#28-bd-table--beam-design-table) | 보 설계 결과를 표로 반환합니다. | POST |
| 29 | [`BD-REPORT`](#29-bd-report--beam-design-report) | 보 설계 결과를 보고서 파일로 내보냅니다. | POST |
| 30 | [`BC-ANAL`](#30-bc-anal--beam-checking-perform) | 보 검토를 수행합니다. | POST |
| 31 | [`BC-TABLE`](#31-bc-table--beam-checking-table) | 보 검토 결과를 표로 반환합니다. | POST |
| 32 | [`BC-REPORT`](#32-bc-report--beam-checking-report) | 보 검토 결과를 보고서 파일로 내보냅니다. | POST |
| 33 | [`CD-ANAL`](#33-cd-anal--column-design-perform) | 기둥 설계를 수행합니다. | POST |
| 34 | [`CD-TABLE`](#34-cd-table--column-design-table) | 기둥 설계 결과를 표로 반환합니다. | POST |
| 35 | [`CD-REPORT`](#35-cd-report--column-design-report) | 기둥 설계 결과를 보고서 파일로 내보냅니다. | POST |
| 36 | [`CC-ANAL`](#36-cc-anal--column-checking-perform) | 기둥 검토를 수행합니다. | POST |
| 37 | [`CC-TABLE`](#37-cc-table--column-checking-table) | 기둥 검토 결과를 표로 반환합니다. | POST |
| 38 | [`CC-REPORT`](#38-cc-report--column-checking-report) | 기둥 검토 결과를 보고서 파일로 내보냅니다. | POST |
| 39 | [`PBD-ANAL`](#39-pbd-anal--plate-beam-design-perform) | 판 보 설계를 수행합니다. | POST |
| 40 | [`PBD-TABLE`](#40-pbd-table--plate-beam-design-table) | 판 보 설계 결과를 표로 반환합니다. | POST |
| 41 | [`PBD-REPORT`](#41-pbd-report--plate-beam-design-report) | 판 보 설계 결과를 보고서 파일로 내보냅니다. | POST |
| 42 | [`PBC-ANAL`](#42-pbc-anal--plate-beam-checking-perform) | 판 보 검토를 수행합니다. | POST |
| 43 | [`PBC-TABLE`](#43-pbc-table--plate-beam-checking-table) | 판 보 검토 결과를 표로 반환합니다. | POST |
| 44 | [`PBC-REPORT`](#44-pbc-report--plate-beam-checking-report) | 판 보 검토 결과를 보고서 파일로 내보냅니다. | POST |
| 45 | [`PCD-ANAL`](#45-pcd-anal--plate-column-design-perform) | 판 기둥 설계를 수행합니다. | POST |
| 46 | [`PCD-TABLE`](#46-pcd-table--plate-column-design-table) | 판 기둥 설계 결과를 표로 반환합니다. | POST |
| 47 | [`PCD-REPORT`](#47-pcd-report--plate-column-design-report) | 판 기둥 설계 결과를 보고서 파일로 내보냅니다. | POST |
| 48 | [`PCC-ANAL`](#48-pcc-anal--plate-column-checking-perform) | 판 기둥 검토를 수행합니다. | POST |
| 49 | [`PCC-TABLE`](#49-pcc-table--plate-column-checking-table) | 판 기둥 검토 결과를 표로 반환합니다. | POST |
| 50 | [`PCC-REPORT`](#50-pcc-report--plate-column-checking-report) | 판 기둥 검토 결과를 보고서 파일로 내보냅니다. | POST |

---

## 0. `DESIGN/RC/DRC` — Design Code (AASHTO-LRFD24/20)

> **기능** 프로젝트의 RC 설계 기준을 AASHTO-LRFD24 또는 AASHTO-LRFD20으로 설정하거나 조회합니다.

KDS 41 20:2022의 선택 값은 [26장 DRC](./26_Design_RC_KDS41202022.md#0-designrcdrc--rc-design-code-rc-설계-코드-선택)를 참고하세요.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738171212185) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738214699289)

### Input URI

```
{base url}/DESIGN/RC/DRC
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] LRFD24: RC Design Code · AASHTO-LRFD24<br>LRFD20: RC Design Code · AASHTO-LRFD20 | `"DGNCODE"` | string | LRFD24: AASHTO-LRFD24<br>LRFD20: AASHTO-LRFD20 | **Required** |

### JSON Schema

아래 JSON Schema는 LRFD24 원문입니다. LRFD20의 `DGNCODE` enum과 기본값은 `"AASHTO-LRFD20"`입니다.

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
              "default": "AASHTO-LRFD24",
              "enum": [
                "AASHTO-LRFD24"
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

- `DCON`

> ⚠️ 두 LRFD 판의 응답 예제는 최상위 Key에 `"DCON"`을 사용합니다. KDS 24 14 21:2021 공식 응답 예제에는 `"DRC"`가 표시됩니다.

### Request / Response JSON

**LRFD24 Request**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "AASHTO-LRFD24"
    }
  }
}
```

**LRFD24 Response**

```json
{
  "DCON": {
    "1": {
      "DGNCODE": "AASHTO-LRFD24"
    }
  }
}
```

**LRFD20 Request**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "AASHTO-LRFD20"
    }
  }
}
```

**LRFD20 Response**

```json
{
  "DCON": {
    "1": {
      "DGNCODE": "AASHTO-LRFD20"
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

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
      "DGNCODE": "AASHTO-LRFD24"
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 1. `DCO` — Design Code Option

> **기능** RC 설계 기준, 내진 특례 적용, 내진 구역, 판 기둥의 축력·모멘트 상호작용 및 보의 모멘트 재분배 옵션을 설정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738163367193) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738252667417)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/DCO`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/DCO`

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Single settings record: the only accepted key is "1". | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] LRFD24: RC Design Code · AASHTO-LRFD24<br>LRFD20: RC Design Code · AASHTO-LRFD20 | `"DGNCODE"` | string | - | **Required** |
| 2 | [General] Apply special provisions for seismic design | `"SEISMIC_PROV"` | boolean | false | Optional |
| 3 | [General] Select Seismic Zone · Seismic Zone 1: 0 · Seismic Zone 2: 1 · Seismic Zone 3: 2 · Seismic Zone 4: 3 | `"SEISMIC_ZONE"` | integer | 0 | Optional |
| 4 | [General] Consider Axial-Moment Interaction for Plate Column Moment Redistribution Factor for Beam | `"PLATE_COLUMN_PM"` | boolean | false | Optional |
| 5 | [General] Moment redistribution factor for beams · Range: 0~1 | `"MOM_REDIST_FACT"` | number | 1 | Optional |

### JSON Schema

아래 JSON Schema는 LRFD24 원문입니다. LRFD20의 `DGNCODE` enum 값은 `"AASHTO-LRFD20"`입니다.

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
                "AASHTO-LRFD24"
              ]
            },
            "SEISMIC_PROV": {
              "type": "boolean",
              "description": "Apply special provisions for seismic design",
              "default": false
            },
            "SEISMIC_ZONE": {
              "type": "integer",
              "description": "Select Seismic Zone. Used only when SEISMIC_PROV is true. Optional: when omitted the default is kept",
              "enum": [
                0,
                1,
                2,
                3
              ],
              "default": 0
            },
            "PLATE_COLUMN_PM": {
              "type": "boolean",
              "default": false,
              "description": "Consider Axial-Moment Interaction for Plate Column Moment Redistribution Factor for Beam"
            },
            "MOM_REDIST_FACT": {
              "type": "number",
              "exclusiveMinimum": 0,
              "maximum": 1,
              "description": "Moment redistribution factor for beams(0 < value <= 1)",
              "default": 1
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

아래 LRFD24 예제의 `DGNCODE`를 LRFD20에서는 `"AASHTO-LRFD20"`으로 바꿉니다.

**Request**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "AASHTO-LRFD24",
      "SEISMIC_PROV": true,
      "SEISMIC_ZONE": 1,
      "PLATE_COLUMN_PM": true,
      "MOM_REDIST_FACT": 0.9
    }
  }
}
```

**Response**

```json
{
  "DCO": {
    "1": {
      "DGNCODE": "AASHTO-LRFD24",
      "SEISMIC_PROV": true,
      "SEISMIC_ZONE": 1,
      "PLATE_COLUMN_PM": true,
      "MOM_REDIST_FACT": 0.9
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/DCO"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/DCO

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "DGNCODE": "AASHTO-LRFD24",
      "SEISMIC_PROV": true,
      "SEISMIC_ZONE": 1,
      "PLATE_COLUMN_PM": true,
      "MOM_REDIST_FACT": 0.9
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 2. `DCTL` — Definition of Frame

> **기능** 프레임의 설계 조건을 정의합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738159008665) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738241525017)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/DCTL`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/DCTL`

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

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

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/DCTL"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/DCTL

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

## 3. `LCTB` — Load Contribution for Nonlinear Load Case

> **기능** 비선형 하중 케이스에 기여하는 하중과 계수를 조회합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738163908633) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738246033049)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/LCTB`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/LCTB`

### Active Methods

`GET` · `DELETE`

### Specifications

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

> ⚠️ 두 판의 공식 Active Methods에는 GET과 DELETE만 나열됩니다. 영문·한글 공식 요청 예제에 포함된 `"Assign"` 바디에는 메서드가 명시되어 있지 않아 아래에 예제로만 싣습니다.

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

공식 Active Methods의 GET을 사용해 데이터를 조회합니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/LCTB"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/LCTB

response = requests.get(URI, headers=HEADERS)
response.raise_for_status()
print(response.json())
```


---

## 4. `SRDF` — Strength Reduction Factors

> **기능** 인장·압축·전단 및 비틀림에 적용할 강도 감소계수를 설정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738203377305) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738260337561)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/SRDF`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/SRDF`

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] For Tensile Control (phi_t) · Minimum: 0 | `"PHI_T"` | number | 0.9 | Optional |
| 2 | [General] Member with Spiral Reinforcement (phi_c1) · Minimum: 0 | `"PHI_C1"` | number | 0.75 | Optional |
| 3 | [General] Other Reinforced Member (phi_c2) · Minimum: 0 | `"PHI_C2"` | number | 0.75 | Optional |
| 4 | [General] For Shear and Torsion (phi_v) · Minimum: 0 | `"PHI_V"` | number | 0.9 | Optional |

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
          "title": "Strength Reduction Factors",
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "PHI_T": {
              "type": "number",
              "description": "For Tensile Control (phi_t). Must not be negative. 0 means the code default (GET returns the effective value); no upper limit is checked",
              "default": 0.9,
              "minimum": 0
            },
            "PHI_C1": {
              "type": "number",
              "description": "For Compressive Control - Member with Spiral Reinforcement (phi_c1). Must not be negative. 0 means the code default (GET returns the effective value); no upper limit is checked",
              "default": 0.75,
              "minimum": 0
            },
            "PHI_C2": {
              "type": "number",
              "description": "For Compressive Control - Other Reinforced Member (phi_c2). Must not be negative. 0 means the code default (GET returns the effective value); no upper limit is checked",
              "default": 0.75,
              "minimum": 0
            },
            "PHI_V": {
              "type": "number",
              "description": "For Shear and Torsion (phi_v). Must not be negative. 0 means the code default (GET returns the effective value); no upper limit is checked",
              "default": 0.9,
              "minimum": 0
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

- `SRDFRC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "PHI_T": 0.8,
      "PHI_C1": 0.65,
      "PHI_C2": 0.6,
      "PHI_V": 0.6
    }
  }
}
```

**Response**

```json
{
  "SRDFRC": {
    "1": {
      "PHI_T": 0.8,
      "PHI_C1": 0.65,
      "PHI_C2": 0.6,
      "PHI_V": 0.6
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/SRDF"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/SRDF

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "PHI_T": 0.8,
      "PHI_C1": 0.65,
      "PHI_C2": 0.6,
      "PHI_V": 0.6
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 5. `SLTC` — Short/Long term Load Case

> **기능** 단기·장기 하중 케이스를 지정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738171817625) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738215365913)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/SLTC`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/SLTC`

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

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

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/SLTC"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/SLTC

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

## 6. `LMRR` — Limiting Maximum Rebar Ratio

> **기능** 최대 철근비 제한을 설정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738173921177) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738260540953)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/LMRR`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/LMRR`

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Single settings record: the only accepted key is "1". | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Maximum rebar ratio of columns (>= 0). 0 uses the code default of 0.08. Must not be negative. 0 means the code default 0.08 (GET returns the effective value); no upper limit is checked · Minimum: 0 | `"RHOC"` | number | 0.08 | Optional |

### JSON Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "Assign"
  ],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Single settings record: the only accepted key is \"1\".",
      "minProperties": 1,
      "maxProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "additionalProperties": false,
          "type": "object",
          "properties": {
            "RHOC": {
              "type": "number",
              "description": "Maximum rebar ratio of columns (>= 0). 0 uses the code default of 0.08. Must not be negative. 0 means the code default 0.08 (GET returns the effective value); no upper limit is checked",
              "default": 0.08,
              "minimum": 0
            }
          }
        }
      },
      "propertyNames": {
        "const": "1"
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `LMRR`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "RHOC": 0.06
    }
  }
}
```

**Response**

```json
{
  "LMRR": {
    "1": {
      "RHOC": 0.06
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/LMRR"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/LMRR

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "RHOC": 0.06
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 7. `MATD` — Modify RC Materials

> **기능** RC 설계에 사용할 콘크리트와 철근 재료를 수정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738195166233) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738255824921)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/MATD`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/MATD`

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a concrete material ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Concrete Material Selection | `"CONCRETE"` | object | - | **Required** |
| 1.1 | └ [General] Code · None · ASTM19(RC) · ASTM(RC) · U.S.C(US)(RC) · U.S.C(SI)(RC) · NMX2023(RC) · NMX2023(MKS)(RC) · NMX NTC-2017(RC) · CSA(RC) · CSA-S6-25(RC) · BS(RC) · EN04(RC) · EN(RC) · NTC08(RC) · NTC12(RC) · NTC18(RC) · UNI(RC) · SS(RC) · GOST-SP(RC) · GOST-SNIP(RC) · JIS(RC) · JIS-Civil(RC) · JTJ023-85(RC) · Q/CR 9300-18(RC) · GB 50917-13(RC) · GB/T10(RC) · GB(RC) · GB-Civil(RC) · TB10092-17(RC) · JTG3362-18(RC) · SI 466(RC) · JTG04(RC) · TB05(RC) · KS19(RC) · KS01(RC) · KS(RC) · KSCE-LSD15(RC) · KS01-Civil(RC) · KS-Civil(RC) · PNS49(RC) · SNI(RC) · TIS(RC) · TIS(MKS)(RC) · IRC(RC) · IRS(RC) · IS(RC) · CNS560-18(RC) · CNS560(RC) · CNS(RC) · AS17(RC) · TMH7(RC) · SP63.2018(RC) · TS(RC) · NBR 6118(RC) · TCVN2018(RC) | `"CODE"` | string | - | **Required** |
| 1.2 | └ [General] Grade | `"GRADE"` | string | - | Optional |
| 1.3 | └ [When CODE = "None"] Name | `"NAME"` | string | - | **Required** |
| 1.4 | └ [When CODE = "None"] Specified Compressive Strength (fc'\|fck) · Minimum: 0 | `"FC"` | number | - | **Required** |
| 1.5 | └ [When CODE = "None"] Light Weight Concrete Factor (Lambda) | `"LIGHTWEIGHT"` | boolean | false | Optional |
| 1.6 | └ [When CODE = "None"] Lambda · Range: 0.75~1 | `"LAMBDA"` | number | 1 | Optional |
| 2 | [General] Rebar Selection | `"REBAR"` | object | - | **Required** |
| 2.1 | └ [General] Code · None · ASTM19(RC) · ASTM(RC) · U.S.C(US)(RC) · U.S.C(SI)(RC) · NMX2023(RC) · NMX2023(MKS)(RC) · NMX NTC-2017(RC) · CSA(RC) · CSA-S6-25(RC) · BS(RC) · EN04(RC) · EN(RC) · NTC08(RC) · NTC12(RC) · NTC18(RC) · UNI(RC) · SS(RC) · GOST-SP(RC) · GOST-SNIP(RC) · JIS(RC) · JIS-Civil(RC) · JTJ023-85(RC) · Q/CR 9300-18(RC) · GB 50917-13(RC) · GB/T10(RC) · GB(RC) · GB-Civil(RC) · TB10092-17(RC) · JTG3362-18(RC) · SI 466(RC) · JTG04(RC) · TB05(RC) · KS19(RC) · KS01(RC) · KS(RC) · KSCE-LSD15(RC) · KS01-Civil(RC) · KS-Civil(RC) · PNS49(RC) · SNI(RC) · TIS(RC) · TIS(MKS)(RC) · IRC(RC) · IRS(RC) · IS(RC) · CNS560-18(RC) · CNS560(RC) · CNS(RC) · AS17(RC) · TMH7(RC) · SP63.2018(RC) · TS(RC) · NBR 6118(RC) · TCVN2018(RC) | `"CODE"` | string | - | **Required** |
| 2.2 | └ [When CODE = "None"] Main Rebar (Grade / Name) | `"MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "None"] Fy · Minimum: 0 | `"FY"` | number | - | **Required** |
| 2.4 | └ [When CODE = "None"] Sub-Rebar (Grade / Name) | `"SUB_REBAR"` | string | - | **Required** |
| 2.5 | └ [When CODE = "None"] Fys · Minimum: 0 | `"FYS"` | number | - | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a concrete material ID string (e.g., \"1\").",
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
              "description": "Concrete material selection",
              "additionalProperties": false,
              "required": [
                "CODE"
              ],
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Concrete material DB code from the dialog Code list, or \"None\" for a user-defined concrete",
                  "enum": [
                    "None",
                    "ASTM19(RC)",
                    "ASTM(RC)",
                    "U.S.C(US)(RC)",
                    "U.S.C(SI)(RC)",
                    "NMX2023(RC)",
                    "NMX2023(MKS)(RC)",
                    "NMX NTC-2017(RC)",
                    "CSA(RC)",
                    "CSA-S6-25(RC)",
                    "BS(RC)",
                    "EN04(RC)",
                    "EN(RC)",
                    "NTC08(RC)",
                    "NTC12(RC)",
                    "NTC18(RC)",
                    "UNI(RC)",
                    "SS(RC)",
                    "GOST-SP(RC)",
                    "GOST-SNIP(RC)",
                    "JIS(RC)",
                    "JIS-Civil(RC)",
                    "JTJ023-85(RC)",
                    "Q/CR 9300-18(RC)",
                    "GB 50917-13(RC)",
                    "GB/T10(RC)",
                    "GB(RC)",
                    "GB-Civil(RC)",
                    "TB10092-17(RC)",
                    "JTG3362-18(RC)",
                    "SI 466(RC)",
                    "JTG04(RC)",
                    "TB05(RC)",
                    "KS19(RC)",
                    "KS01(RC)",
                    "KS(RC)",
                    "KSCE-LSD15(RC)",
                    "KS01-Civil(RC)",
                    "KS-Civil(RC)",
                    "PNS49(RC)",
                    "SNI(RC)",
                    "TIS(RC)",
                    "TIS(MKS)(RC)",
                    "IRC(RC)",
                    "IRS(RC)",
                    "IS(RC)",
                    "CNS560-18(RC)",
                    "CNS560(RC)",
                    "CNS(RC)",
                    "AS17(RC)",
                    "TMH7(RC)",
                    "SP63.2018(RC)",
                    "TS(RC)",
                    "NBR 6118(RC)",
                    "TCVN2018(RC)"
                  ]
                },
                "GRADE": {
                  "type": "string",
                  "description": "Concrete grade of CODE (list depends on the code). Required when CODE is not None"
                },
                "NAME": {
                  "type": "string",
                  "description": "User-defined concrete name. Required when CODE is None; it becomes the material name"
                },
                "FC": {
                  "type": "number",
                  "description": "Specified compressive strength (fc'), model stress unit, > 0. Required when CODE is None; ignored when CODE is a DB code (the grade wins)",
                  "exclusiveMinimum": 0
                },
                "LIGHTWEIGHT": {
                  "type": "boolean",
                  "description": "Apply the light weight concrete factor (Lambda)",
                  "default": false
                },
                "LAMBDA": {
                  "type": "number",
                  "description": "Concrete density modification factor lambda (0.75 to 1.0). Used only when LIGHTWEIGHT is true; stored as 1.0 otherwise",
                  "default": 1,
                  "minimum": 0.75,
                  "maximum": 1
                }
              }
            },
            "REBAR": {
              "type": "object",
              "description": "Rebar material selection",
              "additionalProperties": false,
              "required": [
                "CODE"
              ],
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Rebar material DB code from the dialog Code list, or \"None\" for a user-defined rebar",
                  "enum": [
                    "None",
                    "ASTM19(RC)",
                    "ASTM(RC)",
                    "U.S.C(US)(RC)",
                    "U.S.C(SI)(RC)",
                    "NMX2023(RC)",
                    "NMX2023(MKS)(RC)",
                    "NMX NTC-2017(RC)",
                    "CSA(RC)",
                    "CSA-S6-25(RC)",
                    "BS(RC)",
                    "EN04(RC)",
                    "EN(RC)",
                    "NTC08(RC)",
                    "NTC12(RC)",
                    "NTC18(RC)",
                    "UNI(RC)",
                    "SS(RC)",
                    "GOST-SP(RC)",
                    "GOST-SNIP(RC)",
                    "JIS(RC)",
                    "JIS-Civil(RC)",
                    "JTJ023-85(RC)",
                    "Q/CR 9300-18(RC)",
                    "GB 50917-13(RC)",
                    "GB/T10(RC)",
                    "GB(RC)",
                    "GB-Civil(RC)",
                    "TB10092-17(RC)",
                    "JTG3362-18(RC)",
                    "SI 466(RC)",
                    "JTG04(RC)",
                    "TB05(RC)",
                    "KS19(RC)",
                    "KS01(RC)",
                    "KS(RC)",
                    "KSCE-LSD15(RC)",
                    "KS01-Civil(RC)",
                    "KS-Civil(RC)",
                    "PNS49(RC)",
                    "SNI(RC)",
                    "TIS(RC)",
                    "TIS(MKS)(RC)",
                    "IRC(RC)",
                    "IRS(RC)",
                    "IS(RC)",
                    "CNS560-18(RC)",
                    "CNS560(RC)",
                    "CNS(RC)",
                    "AS17(RC)",
                    "TMH7(RC)",
                    "SP63.2018(RC)",
                    "TS(RC)",
                    "NBR 6118(RC)",
                    "TCVN2018(RC)"
                  ]
                },
                "MAIN_REBAR": {
                  "type": "string",
                  "description": "Main rebar grade of CODE, or the user-defined main rebar name when CODE is None"
                },
                "FY": {
                  "type": "number",
                  "description": "Main rebar yield strength fy, model stress unit, > 0. Required when CODE is None; ignored otherwise",
                  "exclusiveMinimum": 0
                },
                "SUB_REBAR": {
                  "type": "string",
                  "description": "Sub (shear / tie) rebar grade of CODE, or the user-defined sub-rebar name when CODE is None"
                },
                "FYS": {
                  "type": "number",
                  "description": "Sub rebar yield strength fys, model stress unit, > 0. Required when CODE is None; ignored otherwise",
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
        "CODE": "ASTM19(RC)",
        "GRADE": "Grade C4000",
        "LIGHTWEIGHT": false
      },
      "REBAR": {
        "CODE": "ASTM19(RC)",
        "MAIN_REBAR": "Grade 60",
        "SUB_REBAR": "Grade 60"
      }
    },
    "2": {
      "CONCRETE": {
        "CODE": "None",
        "NAME": "C35",
        "FC": 35000,
        "LIGHTWEIGHT": true,
        "LAMBDA": 0.85
      },
      "REBAR": {
        "CODE": "None",
        "MAIN_REBAR": "SD420",
        "SUB_REBAR": "SD420",
        "FY": 420000,
        "FYS": 420000
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
        "CODE": "ASTM19(RC)",
        "GRADE": "Grade C4000",
        "LIGHTWEIGHT": false
      },
      "REBAR": {
        "CODE": "ASTM19(RC)",
        "MAIN_REBAR": "Grade 60",
        "SUB_REBAR": "Grade 60"
      }
    },
    "2": {
      "CONCRETE": {
        "CODE": "None",
        "NAME": "C35",
        "FC": 35000,
        "LIGHTWEIGHT": true,
        "LAMBDA": 0.85
      },
      "REBAR": {
        "CODE": "None",
        "MAIN_REBAR": "SD420",
        "SUB_REBAR": "SD420",
        "FY": 420000,
        "FYS": 420000
      }
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/MATD"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/MATD

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "CONCRETE": {
        "CODE": "ASTM19(RC)",
        "GRADE": "Grade C4000",
        "LIGHTWEIGHT": false
      },
      "REBAR": {
        "CODE": "ASTM19(RC)",
        "MAIN_REBAR": "Grade 60",
        "SUB_REBAR": "Grade 60"
      }
    },
    "2": {
      "CONCRETE": {
        "CODE": "None",
        "NAME": "C35",
        "FC": 35000,
        "LIGHTWEIGHT": true,
        "LAMBDA": 0.85
      },
      "REBAR": {
        "CODE": "None",
        "MAIN_REBAR": "SD420",
        "SUB_REBAR": "SD420",
        "FY": 420000,
        "FYS": 420000
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

## 8. `MBTP` — Modify Member Type

> **기능** 지정한 요소의 부재 유형을 수정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738165226777) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738254934041)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/MBTP`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/MBTP`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

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

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/MBTP"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/MBTP

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

## 9. `MEMB` — Member Assignment

> **기능** RC 설계 대상 요소의 부재 배정을 관리합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738202041497) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738233234201)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/MEMB`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/MEMB`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

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

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/MEMB"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/MEMB

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

## 10. `OPE_MEMB` — Auto Member Assignment

> **기능** 설계 대상 요소를 RC 부재로 자동 배정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738188059673) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738252454809)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/OPE_MEMB`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/OPE_MEMB`

### Active Methods

`POST`

### Specifications

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

아래 JSON Schema에서 설명에 나오는 기준명은 LRFD20 원문에서 `AASHTO-LRFD20`입니다.

```json
{
  "type": "object",
  "description": "Member Assignment (Add/Replace) request schema (POST /DESIGN/RC/AASHTO-LRFD24/OPE_MEMB)",
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

**Request — Manual, selected elements**

```json
{
  "Argument": {
    "ASSIGN_TYPE": "MANUAL",
    "ELEM_LIST": [
      1,
      2,
      3
    ],
    "ALLOW_SINGLE": false
  }
}
```

**Response — Automatic, selected elements**

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

**Response — Automatic, all elements**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21
      ],
      "bREVERSE": true
    }
  }
}
```

**Response — Manual, selected elements**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [
        1,
        2,
        3
      ],
      "bREVERSE": true
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/OPE_MEMB"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/OPE_MEMB

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

## 11. `LENG` — Unbraced Length (L, Lb)

> **기능** 부재별 비지지 길이 L과 Lb를 지정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738180983961) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738216197273)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/LENG`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/LENG`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] LRFD24: Keyed object (dictionary). Each property name is an ID string (e.g., "1"). Element Type = Element. Virtual beams use /DESIGN/RC/AASHTO-LRFD24/LENG-VBEAM.<br>LRFD20: Keyed object (dictionary). Each property name is an ID string (e.g., "1"). Element Type = Element. Virtual beams use /DESIGN/RC/AASHTO-LRFD20/LENG-VBEAM. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Ly · Minimum: 0 | `"LY"` | number | 0 | Optional |
| 2 | [General] Lz · Minimum: 0 | `"LZ"` | number | 0 | Optional |
| 3 | [General] Lb · Minimum: 0 | `"LB"` | number | 0 | Optional |
| 4 | [General] Do not consider | `"bNOTUSE"` | boolean | false | Optional |
| 3 | [When bNOTUSE = true] Lb · 0 · Minimum: 0 | `"LB"` | number | 0 | Optional |

### JSON Schema

아래 JSON Schema에서 설명에 나오는 기준명은 LRFD20 원문에서 `AASHTO-LRFD20`입니다.

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
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\"). Element Type = Element. Virtual beams use /DESIGN/RC/AASHTO-LRFD24/LENG-VBEAM.",
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

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/LENG"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/LENG

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

## 12. `KFAC` — Effective Length Factor (K)

> **기능** 부재별 유효길이계수 K를 지정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738202531865) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738233665561)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/KFAC`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/KFAC`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

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

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/KFAC"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/KFAC

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

## 13. `CMFT` — Moment Factor (Cm)

> **기능** 부재별 모멘트 계수 Cm을 지정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738202837273) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738216948121)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/CMFT`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/CMFT`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] LRFD24: Keyed object (dictionary). Each property name is an element ID string (e.g., "1"). Element Type = Element. Virtual beams use /DESIGN/RC/AASHTO-LRFD24/CMFT-VBEAM.<br>LRFD20: Keyed object (dictionary). Each property name is an element ID string (e.g., "1"). Element Type = Element. Virtual beams use /DESIGN/RC/AASHTO-LRFD20/CMFT-VBEAM. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Cmy · Range: 0~1 | `"CMY"` | number | 0 | Optional |
| 2 | [General] Cmz · Range: 0~1 | `"CMZ"` | number | 0 | Optional |
| 3 | [General] Calculate by Program | `"OPT_AUTO"` | boolean | false | Optional |

### JSON Schema

아래 JSON Schema에서 설명에 나오는 기준명은 LRFD20 원문에서 `AASHTO-LRFD20`입니다.

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
      "description": "Keyed object (dictionary). Each property name is an element ID string (e.g., \"1\"). Element Type = Element. Virtual beams use /DESIGN/RC/AASHTO-LRFD24/CMFT-VBEAM.",
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

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/CMFT"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/CMFT

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

## 14. `FMAG` — Moment Magnifier (B1/Delta_b, B2/Delta_s)

> **기능** 부재별 모멘트 확대계수 B1/δb와 B2/δs를 지정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738194020505) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738226311193)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/FMAG`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/FMAG`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] LRFD24: Keyed object (dictionary). Each property name is an element ID string (e.g., "1"). Element Type = Element. Virtual beams use /DESIGN/RC/AASHTO-LRFD24/FMAG-VBEAM.<br>LRFD20: Keyed object (dictionary). Each property name is an element ID string (e.g., "1"). Element Type = Element. Virtual beams use /DESIGN/RC/AASHTO-LRFD20/FMAG-VBEAM. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] B1y\|Delta_by · Range: 1~100 | `"B1Y_DELTA_BY"` | number | 1 | Optional |
| 2 | [General] B1z\|Delta_bz · Range: 1~100 | `"B1Z_DELTA_BZ"` | number | 1 | Optional |
| 3 | [General] B2y\|Delta_sy · Range: 1~100 | `"B2Y_DELTA_SY"` | number | 1 | Optional |
| 4 | [General] B2z\|Delta_sz · Range: 1~100 | `"B2Z_DELTA_SZ"` | number | 1 | Optional |

### JSON Schema

아래 JSON Schema에서 설명에 나오는 기준명은 LRFD20 원문에서 `AASHTO-LRFD20`입니다.

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
      "description": "Keyed object (dictionary). Each property name is an element ID string (e.g., \"1\"). Element Type = Element. Virtual beams use /DESIGN/RC/AASHTO-LRFD24/FMAG-VBEAM.",
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

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/FMAG"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/FMAG

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

## 15. `LTSR` — Limiting Slenderness Ratio

> **기능** 부재별 세장비 한계를 설정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738193630361) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738233898521)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/LTSR`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/LTSR`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

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

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/LTSR"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/LTSR

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

## 16. `RMFR` — Response Modification Factor (R)

> **기능** 부재별 응답수정계수 R을 지정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738195017113) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738255664409)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/RMFR`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/RMFR`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Fx · Minimum: 0 | `"FX"` | number | 1 | Optional |
| 2 | [General] Fy · Minimum: 0 | `"FY"` | number | 1 | Optional |
| 3 | [General] Fz · Minimum: 0 | `"FZ"` | number | 1 | Optional |
| 4 | [General] Mx · Minimum: 0 | `"MX"` | number | 1 | Optional |
| 5 | [General] My · Minimum: 0 | `"MY"` | number | 1 | Optional |
| 6 | [General] Mz · Minimum: 0 | `"MZ"` | number | 1 | Optional |

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
          "title": "Response Modification Factor (R)",
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "FX": {
              "type": "number",
              "description": "Response modification factor for Fx. Must not be negative (0 or greater)",
              "default": 1,
              "minimum": 0
            },
            "FY": {
              "type": "number",
              "description": "Response modification factor for Fy. Must not be negative (0 or greater)",
              "default": 1,
              "minimum": 0
            },
            "FZ": {
              "type": "number",
              "description": "Response modification factor for Fz. Must not be negative (0 or greater)",
              "default": 1,
              "minimum": 0
            },
            "MX": {
              "type": "number",
              "description": "Response modification factor for Mx. Must not be negative (0 or greater)",
              "default": 1,
              "minimum": 0
            },
            "MY": {
              "type": "number",
              "description": "Response modification factor for My. Must not be negative (0 or greater)",
              "default": 1,
              "minimum": 0
            },
            "MZ": {
              "type": "number",
              "description": "Response modification factor for Mz. Must not be negative (0 or greater)",
              "default": 1,
              "minimum": 0
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

- `RMFR`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "FX": 1.5,
      "FY": 1.5,
      "FZ": 1.5,
      "MX": 1,
      "MY": 2,
      "MZ": 2
    }
  }
}
```

**Response**

```json
{
  "RMFR": {
    "1": {
      "FX": 1.5,
      "FY": 1.5,
      "FZ": 1.5,
      "MX": 1,
      "MY": 2,
      "MZ": 2
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/RMFR"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/RMFR

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "FX": 1.5,
      "FY": 1.5,
      "FZ": 1.5,
      "MX": 1,
      "MY": 2,
      "MZ": 2
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 17. `SUFC` — Scale-up Factor for Column

> **기능** 기둥의 스케일업 계수를 지정합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738191026841) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738277463961)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/SUFC`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/SUFC`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Scale Up Factor · Minimum: 1 | `"FACTOR"` | number | 1 | Optional |

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
          "title": "Scale Up Factor for Column",
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "FACTOR": {
              "type": "number",
              "description": "Scale-up factor applied to the design forces of the element (>= 1.0). Beam (frame) elements only. Optional: 1.0 when omitted",
              "default": 1,
              "minimum": 1
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

- `SUFC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "FACTOR": 1.2
    },
    "2": {
      "FACTOR": 1.5
    }
  }
}
```

**Response**

```json
{
  "SUFC": {
    "1": {
      "FACTOR": 1.2
    },
    "2": {
      "FACTOR": 1.5
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/SUFC"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/SUFC

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "FACTOR": 1.2
    },
    "2": {
      "FACTOR": 1.5
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 18. `RDGN` — Rebar Input for Design (Beam, Column Section)

> **기능** 보·기둥 단면의 설계용 철근 데이터를 입력합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738166471577) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738277948569)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/RDGN`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/RDGN`

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a design section ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Member Type · Beam Section: "BEAM" · Column Section: "COLUMN" | `"MEMBTYPE"` | string | - | **Required** |
| 2 | [When MEMBTYPE = "Beam Section"] Beam Section | `"BEAM"` | object | - | **Required** |
| 2.1 | └ [When MEMBTYPE = "Beam Section"] Stirrups Data | `"STIRRUP"` | object | - | **Required** |
| 2.1.1 | 　　└ [When MEMBTYPE = "Beam Section"] Size | `"SIZE"` | string | - | **Required** |
| 2.1.2 | 　　└ [When MEMBTYPE = "Beam Section"] Number · Range: 2~99 | `"NUMBER"` | number | - | **Required** |
| 2.2 | └ [When MEMBTYPE = "Beam Section"] Dt · Minimum: 0 | `"DT"` | number | - | **Required** |
| 2.3 | └ [When MEMBTYPE = "Beam Section"] Db · Minimum: 0 | `"DB"` | number | - | **Required** |
| 3 | [When MEMBTYPE = "Column Section"] Column Section | `"COLM"` | object | - | **Required** |
| 3.1 | └ [When MEMBTYPE = "Column Section"] Ties/Spirals | `"TIE_SPIRAL"` | object | - | **Required** |
| 3.1.1 | 　　└ [When MEMBTYPE = "Column Section"] Size | `"SIZE"` | string | - | **Required** |
| 3.1.2 | 　　└ [When MEMBTYPE = "Column Section"] Number · Range: 2~99 | `"NUMBER"` | number | - | **Required** |
| 3.2 | └ [When MEMBTYPE = "Column Section"] Dc · Minimum: 0 | `"DC"` | number | - | **Required** |

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
          "title": "Rebar Input for Design",
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
            "BEAM": {
              "type": "object",
              "description": "Beam Section Data for Design. Used when MEMBTYPE is BEAM (not read otherwise). Rectangular, T and inverted T sections only. Torsional Reinforcement of the dialog is enabled only for SNiP 2.05.03-84 / SP 35.13330 and is not part of this record",
              "additionalProperties": false,
              "required": [
                "STIRRUP",
                "DT",
                "DB"
              ],
              "properties": {
                "STIRRUP": {
                  "type": "object",
                  "description": "Stirrup size and number of legs",
                  "additionalProperties": false,
                  "required": [
                    "SIZE",
                    "NUMBER"
                  ],
                  "properties": {
                    "SIZE": {
                      "type": "string",
                      "description": "Size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected"
                    },
                    "NUMBER": {
                      "type": "number",
                      "description": "Number of stirrup legs, 2 to 99",
                      "minimum": 2,
                      "maximum": 99
                    }
                  }
                },
                "DT": {
                  "type": "number",
                  "description": "Cover to the top rebar, measured from the top fiber. Greater than 0; for rectangular and T sections also less than half the section height. The same value applies at the I, M and J positions",
                  "exclusiveMinimum": 0
                },
                "DB": {
                  "type": "number",
                  "description": "Cover to the bottom rebar, measured from the bottom fiber. Greater than 0; for rectangular and T sections also less than half the section height",
                  "exclusiveMinimum": 0
                }
              }
            },
            "COLM": {
              "type": "object",
              "description": "Column Section Data for Design. Used when MEMBTYPE is COLUMN (not read otherwise)",
              "additionalProperties": false,
              "required": [
                "TIE_SPIRAL",
                "DC"
              ],
              "properties": {
                "TIE_SPIRAL": {
                  "type": "object",
                  "description": "Tie or spiral size and number of legs",
                  "additionalProperties": false,
                  "required": [
                    "SIZE",
                    "NUMBER"
                  ],
                  "properties": {
                    "SIZE": {
                      "type": "string",
                      "description": "Size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code). An empty or unknown name is rejected"
                    },
                    "NUMBER": {
                      "type": "number",
                      "description": "Number of tie legs, 2 to 99",
                      "minimum": 2,
                      "maximum": 99
                    }
                  }
                },
                "DC": {
                  "type": "number",
                  "description": "Cover to the rebar. Greater than 0; below the wall thickness when the section has one, otherwise below half the section width",
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

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `RDGN`

> ⚠️ 표의 조건에 나오는 "Beam Section"과 "Column Section"은 화면에 표시되는 이름입니다. 요청의 `MEMBTYPE` 값은 JSON Schema의 `"BEAM"`, `"COLUMN"`을 사용합니다. 기둥 데이터는 `"COLM"`에 담습니다.

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "MEMBTYPE": "BEAM",
      "BEAM": {
        "STIRRUP": {
          "SIZE": "D13",
          "NUMBER": 2
        },
        "DT": 0.05,
        "DB": 0.06
      }
    }
  }
}
```

**Response**

```json
{
  "RDGN": {
    "1": {
      "MEMBTYPE": "BEAM",
      "BEAM": {
        "STIRRUP": {
          "SIZE": "D13",
          "NUMBER": 2
        },
        "DT": 0.05,
        "DB": 0.06
      }
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/RDGN"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/RDGN

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "MEMBTYPE": "BEAM",
      "BEAM": {
        "STIRRUP": {
          "SIZE": "D13",
          "NUMBER": 2
        },
        "DT": 0.05,
        "DB": 0.06
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

## 19. `RCHK` — Rebar Input for Checking (Beam, Column Section)

> **기능** 보·기둥 단면의 검토용 철근 데이터를 입력합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738166640537) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738261735833)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/RCHK`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/RCHK`

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a design section ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Member Type · Beam Section: "BEAM" · Column Section: "COLUMN" | `"MEMBTYPE"` | string | - | **Required** |
| 2 | [General] Crack Checking · Class 1 exposure condition: 0 · Class 2 exposure condition: 1 | `"ENVTYPE"` | integer | - | Optional |
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
          "title": "Rebar Input for Checking",
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
              "description": "Crack Checking exposure condition (AASHTO: 0 = Class 1, 1 = Class 2; Corrosion / High Corrosion are hidden for AASHTO). Omitted keeps the stored value",
              "enum": [
                0,
                1
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

- `RCHK`

> ⚠️ 표의 조건에 나오는 "Beam Section"과 "Column Section"은 화면에 표시되는 이름입니다. 요청의 `MEMBTYPE` 값은 JSON Schema의 `"BEAM"`, `"COLUMN"`을 사용합니다. 기둥 데이터는 `"COLM"`에 담습니다.

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "2": {
      "MEMBTYPE": "BEAM",
      "ENVTYPE": 1,
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
  "RCHK": {
    "2": {
      "MEMBTYPE": "BEAM",
      "ENVTYPE": 1,
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

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/RCHK"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/RCHK

payload = json.loads(r'''
{
  "Assign": {
    "2": {
      "MEMBTYPE": "BEAM",
      "ENVTYPE": 1,
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

## 20. `REBT` — Column General Section Rebar

> **기능** 기둥의 일반 단면 철근을 입력합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738166885529) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738261970201)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/REBT`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/REBT`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a section ID string (e.g., "4") of a general section. Writing a section deletes the member-level rebar (RBTE) of the elements that use it | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Origin Type · Centroid: "CENTROID" · Left-Bottom: "LEFT BOTTOM" | `"ORIGIN_TYPE"` | string | CENTROID | Optional |
| 2 | [General] Rebar | `"MAIN_BAR"` | array [object] | - | Optional |
| 2.1 | └ [General] No. · Minimum: 1 | `"NUM"` | integer | - | Optional |
| 2.2 | └ [General] Rebar | `"NAME"` | string | - | Optional |
| 2.3 | └ [General] y | `"Y"` | number | - | Optional |
| 2.4 | └ [General] z | `"Z"` | number | - | Optional |
| 3 | [General] Hoop Rebar | `"HOOP_BAR"` | object | - | Optional |
| 3.1 | └ [General] Size | `"NAME"` | string | - | Optional |
| 3.2 | └ [General] Leg y · Minimum: 0 | `"LEG_Y"` | integer | - | Optional |
| 3.3 | └ [General] Leg z · Minimum: 0 | `"LEG_Z"` | integer | - | Optional |
| 3.4 | └ [General] Spacing · Minimum: 0 | `"DIST"` | number | - | Optional |

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
            "MAIN_BAR": {
              "type": "array",
              "description": "Main bars, applied along the whole member (Rebar tab; AASHTO uses one set for I and J). Omitting the array leaves the stored bars unchanged; when present, entries are merged by NUM. At least one bar must remain. Collection items are paired with the stored items by request position and missing properties are filled in from them, so read the record with GET, edit it and send every property of every item back. A bar cannot be removed with PUT: to remove bars, DELETE the record and POST the bars to keep",
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
            "HOOP_BAR": {
              "type": "object",
              "additionalProperties": false,
              "description": "Hoop bar, applied along the whole member (Hoop Rebar tab). Omitted leaves the stored value unchanged",
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
      "MAIN_BAR": [
        {
          "NUM": 1,
          "NAME": "#8",
          "Y": 0.22,
          "Z": 0.22
        },
        {
          "NUM": 2,
          "NAME": "#8",
          "Y": -0.22,
          "Z": 0.22
        },
        {
          "NUM": 3,
          "NAME": "#8",
          "Y": -0.22,
          "Z": -0.22
        },
        {
          "NUM": 4,
          "NAME": "#8",
          "Y": 0.22,
          "Z": -0.22
        }
      ],
      "HOOP_BAR": {
        "NAME": "#4",
        "LEG_Y": 2,
        "LEG_Z": 2,
        "DIST": 0.15
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
      "MAIN_BAR": [
        {
          "NUM": 1,
          "NAME": "#8",
          "Y": 0.22,
          "Z": 0.22
        },
        {
          "NUM": 2,
          "NAME": "#8",
          "Y": -0.22,
          "Z": 0.22
        },
        {
          "NUM": 3,
          "NAME": "#8",
          "Y": -0.22,
          "Z": -0.22
        },
        {
          "NUM": 4,
          "NAME": "#8",
          "Y": 0.22,
          "Z": -0.22
        }
      ],
      "HOOP_BAR": {
        "NAME": "#4",
        "LEG_Y": 2,
        "LEG_Z": 2,
        "DIST": 0.15
      }
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/REBT"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/REBT

payload = json.loads(r'''
{
  "Assign": {
    "4": {
      "ORIGIN_TYPE": "CENTROID",
      "MAIN_BAR": [
        {
          "NUM": 1,
          "NAME": "#8",
          "Y": 0.22,
          "Z": 0.22
        },
        {
          "NUM": 2,
          "NAME": "#8",
          "Y": -0.22,
          "Z": 0.22
        },
        {
          "NUM": 3,
          "NAME": "#8",
          "Y": -0.22,
          "Z": -0.22
        },
        {
          "NUM": 4,
          "NAME": "#8",
          "Y": 0.22,
          "Z": -0.22
        }
      ],
      "HOOP_BAR": {
        "NAME": "#4",
        "LEG_Y": 2,
        "LEG_Z": 2,
        "DIST": 0.15
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

## 21. `RIPB` — Rebar Input for Plate Beam

> **기능** 판 보의 철근 배치를 입력합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738205329049) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738270545945)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/RIPB`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/RIPB`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a record ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Name | `"NAME"` | string | - | Optional |
| 2 | [General] Main Rebar | `"MAIN"` ¹⁾ | object | - | Optional |
| 3 | [General] Distribution Bar | `"DISTRIBUTION"` ²⁾ | object | - | Optional |
| 4 | [General] Stirrup | `"USE_STIRRUP"` | boolean | false | Optional |
| 5 | [When USE_STIRRUP = true] Stirrup Data | `"STIRRUP"` | object | - | **Required** |
| 5.1 | └ [When USE_STIRRUP = true] Size | `"SIZE"` | string | - | Optional |
| 5.2 | └ [When USE_STIRRUP = true] Spacing · Minimum: 0 | `"SPACING"` | number | - | Optional |
| 5.3 | └ [When USE_STIRRUP = true] Number · Minimum: 0 | `"NUMBER"` | integer | - | Optional |

**Main Rebar ¹⁾**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Top | `"TOP"` | object | - | Optional |
| 1.1 | └ Number of Layers · Range: 0~3 | `"LAYER"` | integer | - | Optional |
| 1.2 | └ Layers | `"LAYERS"` | array [object] | - | Optional |
| 1.2.1 | 　　└ Layer · Range: 1~3 | `"LAYER"` | integer | - | **Required** |
| 1.2.2 | 　　└ CTC · Minimum: 0 | `"CTC"` | number | - | Optional |
| 1.2.3 | 　　└ Size1 | `"SIZE1"` | string | - | Optional |
| 1.2.4 | 　　└ Size2 | `"SIZE2"` | string | - | Optional |
| 1.2.5 | 　　└ Dt · Minimum: 0 | `"DT"` | number | - | Optional |
| 2 | Bottom | `"BOTTOM"` | object | - | Optional |
| 2.1 | └ Number of Layers · Range: 0~3 | `"LAYER"` | integer | - | Optional |
| 2.2 | └ Layers | `"LAYERS"` | array [object] | - | Optional |
| 2.2.1 | 　　└ Layer · Range: 1~3 | `"LAYER"` | integer | - | **Required** |
| 2.2.2 | 　　└ CTC · Minimum: 0 | `"CTC"` | number | - | Optional |
| 2.2.3 | 　　└ Size1 | `"SIZE1"` | string | - | Optional |
| 2.2.4 | 　　└ Size2 | `"SIZE2"` | string | - | Optional |
| 2.2.5 | 　　└ Db · Minimum: 0 | `"DB"` | number | - | Optional |

**Distribution Bar ²⁾**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Top | `"TOP"` | object | - | Optional |
| 1.1 | └ Number of Layers · Range: 0~3 | `"LAYER"` | integer | - | Optional |
| 1.2 | └ Layers | `"LAYERS"` | array [object] | - | Optional |
| 1.2.1 | 　　└ Layer · Range: 1~3 | `"LAYER"` | integer | - | **Required** |
| 1.2.2 | 　　└ CTC · Minimum: 0 | `"CTC"` | number | - | Optional |
| 1.2.3 | 　　└ Size1 | `"SIZE1"` | string | - | Optional |
| 2 | Bottom | `"BOTTOM"` | object | - | Optional |
| 2.1 | └ Number of Layers · Range: 0~3 | `"LAYER"` | integer | - | Optional |
| 2.2 | └ Layers | `"LAYERS"` | array [object] | - | Optional |
| 2.2.1 | 　　└ Layer · Range: 1~3 | `"LAYER"` | integer | - | **Required** |
| 2.2.2 | 　　└ CTC · Minimum: 0 | `"CTC"` | number | - | Optional |
| 2.2.3 | 　　└ Size1 | `"SIZE1"` | string | - | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a record ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Rebar Input for Plate Beam",
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "NAME": {
              "type": "string",
              "minLength": 1,
              "maxLength": 20,
              "description": "Record name, 1 to 20 characters and unique. Plate beam checking data refers to the record by this name. Required for a new record"
            },
            "MAIN": {
              "type": "object",
              "description": "Main rebar. A new record starts with one empty layer in each table, as in the dialog, so send SIZE1 for it or set LAYER to 0. Changing a record clears existing design results",
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "object",
                  "description": "Main rebar layers on the top side",
                  "additionalProperties": false,
                  "properties": {
                    "LAYER": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 3,
                      "description": "Number of layers, 0 to 3. Lowering it clears the layers above the new count"
                    },
                    "LAYERS": {
                      "type": "array",
                      "maxItems": 3,
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                          "LAYER"
                        ],
                        "properties": {
                          "LAYER": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 3,
                            "description": "Layer number counted from the top face, 1 to 3. Identifies the layer; properties not sent keep their stored values"
                          },
                          "CTC": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Bar spacing (CTC), current length unit, 0 or greater"
                          },
                          "SIZE1": {
                            "type": "string",
                            "description": "Bar size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          },
                          "SIZE2": {
                            "type": "string",
                            "description": "Second bar size of the layer, or empty. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          },
                          "DT": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Distance from the top face to the layer, current length unit, 0 or greater and increasing with the layer number"
                          }
                        }
                      },
                      "description": "Layers matched by LAYER. Layers that are not listed keep their stored values, and an empty list changes nothing. A layer number above the layer count is rejected"
                    }
                  }
                },
                "BOTTOM": {
                  "type": "object",
                  "description": "Main rebar layers on the bottom side",
                  "additionalProperties": false,
                  "properties": {
                    "LAYER": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 3,
                      "description": "Number of layers, 0 to 3. Lowering it clears the layers above the new count"
                    },
                    "LAYERS": {
                      "type": "array",
                      "maxItems": 3,
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                          "LAYER"
                        ],
                        "properties": {
                          "LAYER": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 3,
                            "description": "Layer number counted from the bottom face, 1 to 3. Identifies the layer; properties not sent keep their stored values"
                          },
                          "CTC": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Bar spacing (CTC), current length unit, 0 or greater"
                          },
                          "SIZE1": {
                            "type": "string",
                            "description": "Bar size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          },
                          "SIZE2": {
                            "type": "string",
                            "description": "Second bar size of the layer, or empty. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          },
                          "DB": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Distance from the bottom face to the layer, current length unit, 0 or greater and increasing with the layer number"
                          }
                        }
                      },
                      "description": "Layers matched by LAYER. Layers that are not listed keep their stored values, and an empty list changes nothing. A layer number above the layer count is rejected"
                    }
                  }
                }
              }
            },
            "DISTRIBUTION": {
              "type": "object",
              "description": "Distribution bar. A new record starts with one empty layer in each table, as in the dialog, so send SIZE1 for it or set LAYER to 0",
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "object",
                  "description": "Distribution bar layers on the top side",
                  "additionalProperties": false,
                  "properties": {
                    "LAYER": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 3,
                      "description": "Number of layers, 0 to 3. Lowering it clears the layers above the new count"
                    },
                    "LAYERS": {
                      "type": "array",
                      "maxItems": 3,
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                          "LAYER"
                        ],
                        "properties": {
                          "LAYER": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 3,
                            "description": "Layer number, 1 to 3. Identifies the layer; properties not sent keep their stored values. The design uses the cover of the main rebar layer with the same number"
                          },
                          "CTC": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Bar spacing (CTC), current length unit, 0 or greater"
                          },
                          "SIZE1": {
                            "type": "string",
                            "description": "Bar size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          }
                        }
                      },
                      "description": "Layers matched by LAYER. Layers that are not listed keep their stored values, and an empty list changes nothing. A layer number above the layer count is rejected"
                    }
                  }
                },
                "BOTTOM": {
                  "type": "object",
                  "description": "Distribution bar layers on the bottom side",
                  "additionalProperties": false,
                  "properties": {
                    "LAYER": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 3,
                      "description": "Number of layers, 0 to 3. Lowering it clears the layers above the new count"
                    },
                    "LAYERS": {
                      "type": "array",
                      "maxItems": 3,
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                          "LAYER"
                        ],
                        "properties": {
                          "LAYER": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 3,
                            "description": "Layer number, 1 to 3. Identifies the layer; properties not sent keep their stored values. The design uses the cover of the main rebar layer with the same number"
                          },
                          "CTC": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Bar spacing (CTC), current length unit, 0 or greater"
                          },
                          "SIZE1": {
                            "type": "string",
                            "description": "Bar size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          }
                        }
                      },
                      "description": "Layers matched by LAYER. Layers that are not listed keep their stored values, and an empty list changes nothing. A layer number above the layer count is rejected"
                    }
                  }
                }
              }
            },
            "USE_STIRRUP": {
              "type": "boolean",
              "default": false,
              "description": "Use stirrups (Stirrup checkbox) in the shear design. A new record starts with false"
            },
            "STIRRUP": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "SIZE": {
                  "type": "string",
                  "description": "Stirrup bar size. Returned and accepted only when USE_STIRRUP is true. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                },
                "SPACING": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Stirrup spacing, current length unit, greater than 0. Returned and accepted only when USE_STIRRUP is true"
                },
                "NUMBER": {
                  "type": "integer",
                  "minimum": 0,
                  "description": "Number of stirrup legs, greater than 0. Returned and accepted only when USE_STIRRUP is true"
                }
              },
              "description": "Stirrup size, spacing and number of legs. Used only when USE_STIRRUP is true. Deleting a record also deletes the plate beam checking data that refer to it"
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

- `RIPB`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "NAME": "PB-1",
      "MAIN": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#5",
              "SIZE2": "",
              "DT": 0.05
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 2,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#6",
              "SIZE2": "#5",
              "DB": 0.05
            },
            {
              "LAYER": 2,
              "CTC": 0.4,
              "SIZE1": "#6",
              "DB": 0.1
            }
          ]
        }
      },
      "DISTRIBUTION": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        }
      },
      "STIRRUP": {
        "SIZE": "#4",
        "SPACING": 0.3,
        "NUMBER": 2
      },
      "USE_STIRRUP": true
    }
  }
}
```

**Response**

```json
{
  "RIPB": {
    "1": {
      "NAME": "PB-1",
      "MAIN": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#5",
              "SIZE2": "",
              "DT": 0.05
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 2,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#6",
              "SIZE2": "#5",
              "DB": 0.05
            },
            {
              "LAYER": 2,
              "CTC": 0.4,
              "SIZE1": "#6",
              "DB": 0.1
            }
          ]
        }
      },
      "DISTRIBUTION": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        }
      },
      "STIRRUP": {
        "SIZE": "#4",
        "SPACING": 0.3,
        "NUMBER": 2
      },
      "USE_STIRRUP": true
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/RIPB"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/RIPB

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "NAME": "PB-1",
      "MAIN": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#5",
              "SIZE2": "",
              "DT": 0.05
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 2,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#6",
              "SIZE2": "#5",
              "DB": 0.05
            },
            {
              "LAYER": 2,
              "CTC": 0.4,
              "SIZE1": "#6",
              "DB": 0.1
            }
          ]
        }
      },
      "DISTRIBUTION": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        }
      },
      "STIRRUP": {
        "SIZE": "#4",
        "SPACING": 0.3,
        "NUMBER": 2
      },
      "USE_STIRRUP": true
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 22. `RIPC` — Rebar Input for Plate Column

> **기능** 판 기둥의 철근 배치를 입력합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738206001433) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738257757081)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/RIPC`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/RIPC`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a record ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Name | `"NAME"` | string | - | Optional |
| 2 | [General] Main Rebar | `"MAIN"` ¹⁾ | object | - | Optional |
| 3 | [General] Distribution Bar | `"DISTRIBUTION"` ²⁾ | object | - | Optional |
| 4 | [General] Stirrup | `"USE_STIRRUP"` | boolean | false | Optional |
| 5 | [General] Stirrup Data | `"STIRRUP"` | object | - | Optional |
| 5.1 | └ [General] Size | `"SIZE"` | string | - | Optional |
| 5.2 | └ [General] Spacing · Minimum: 0 | `"SPACING"` | number | - | Optional |
| 5.3 | └ [General] Number · Minimum: 0 | `"NUMBER"` | integer | - | Optional |

**Main Rebar ¹⁾**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Top | `"TOP"` | object | - | Optional |
| 1.1 | └ Number of Layers · Range: 0~3 | `"LAYER"` | integer | - | Optional |
| 1.2 | └ Layers | `"LAYERS"` | array [object] | - | Optional |
| 1.2.1 | 　　└ Layer · Range: 1~3 | `"LAYER"` | integer | - | **Required** |
| 1.2.2 | 　　└ CTC · Minimum: 0 | `"CTC"` | number | - | Optional |
| 1.2.3 | 　　└ Size1 | `"SIZE1"` | string | - | Optional |
| 1.2.4 | 　　└ Size2 | `"SIZE2"` | string | - | Optional |
| 1.2.5 | 　　└ Dt · Minimum: 0 | `"DT"` | number | - | Optional |
| 2 | Bottom | `"BOTTOM"` | object | - | Optional |
| 2.1 | └ Number of Layers · Range: 0~3 | `"LAYER"` | integer | - | Optional |
| 2.2 | └ Layers | `"LAYERS"` | array [object] | - | Optional |
| 2.2.1 | 　　└ Layer · Range: 1~3 | `"LAYER"` | integer | - | **Required** |
| 2.2.2 | 　　└ CTC · Minimum: 0 | `"CTC"` | number | - | Optional |
| 2.2.3 | 　　└ Size1 | `"SIZE1"` | string | - | Optional |
| 2.2.4 | 　　└ Size2 | `"SIZE2"` | string | - | Optional |
| 2.2.5 | 　　└ Db · Minimum: 0 | `"DB"` | number | - | Optional |

**Distribution Bar ²⁾**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Top | `"TOP"` | object | - | Optional |
| 1.1 | └ Number of Layers · Range: 0~3 | `"LAYER"` | integer | - | Optional |
| 1.2 | └ Layers | `"LAYERS"` | array [object] | - | Optional |
| 1.2.1 | 　　└ Layer · Range: 1~3 | `"LAYER"` | integer | - | **Required** |
| 1.2.2 | 　　└ CTC · Minimum: 0 | `"CTC"` | number | - | Optional |
| 1.2.3 | 　　└ Size1 | `"SIZE1"` | string | - | Optional |
| 2 | Bottom | `"BOTTOM"` | object | - | Optional |
| 2.1 | └ Number of Layers · Range: 0~3 | `"LAYER"` | integer | - | Optional |
| 2.2 | └ Layers | `"LAYERS"` | array [object] | - | Optional |
| 2.2.1 | 　　└ Layer · Range: 1~3 | `"LAYER"` | integer | - | **Required** |
| 2.2.2 | 　　└ CTC · Minimum: 0 | `"CTC"` | number | - | Optional |
| 2.2.3 | 　　└ Size1 | `"SIZE1"` | string | - | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a record ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Rebar Input for Plate Column",
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "NAME": {
              "type": "string",
              "minLength": 1,
              "maxLength": 20,
              "description": "Record name, 1 to 20 characters and unique. Plate column checking data refers to the record by this name. Required for a new record"
            },
            "MAIN": {
              "type": "object",
              "description": "Main rebar. A new record starts with one empty layer in each table, as in the dialog, so send SIZE1 for it or set LAYER to 0. Changing a record clears existing design results",
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "object",
                  "description": "Main rebar layers on the top side",
                  "additionalProperties": false,
                  "properties": {
                    "LAYER": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 3,
                      "description": "Number of layers, 0 to 3. Lowering it clears the layers above the new count"
                    },
                    "LAYERS": {
                      "type": "array",
                      "maxItems": 3,
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                          "LAYER"
                        ],
                        "properties": {
                          "LAYER": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 3,
                            "description": "Layer number counted from the top face, 1 to 3. Identifies the layer; properties not sent keep their stored values"
                          },
                          "CTC": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Bar spacing (CTC), current length unit, 0 or greater"
                          },
                          "SIZE1": {
                            "type": "string",
                            "description": "Bar size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          },
                          "SIZE2": {
                            "type": "string",
                            "description": "Second bar size of the layer, or empty. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          },
                          "DT": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Distance from the top face to the layer, current length unit, 0 or greater and increasing with the layer number"
                          }
                        }
                      },
                      "description": "Layers matched by LAYER. Layers that are not listed keep their stored values, and an empty list changes nothing. A layer number above the layer count is rejected"
                    }
                  }
                },
                "BOTTOM": {
                  "type": "object",
                  "description": "Main rebar layers on the bottom side",
                  "additionalProperties": false,
                  "properties": {
                    "LAYER": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 3,
                      "description": "Number of layers, 0 to 3. Lowering it clears the layers above the new count"
                    },
                    "LAYERS": {
                      "type": "array",
                      "maxItems": 3,
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                          "LAYER"
                        ],
                        "properties": {
                          "LAYER": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 3,
                            "description": "Layer number counted from the bottom face, 1 to 3. Identifies the layer; properties not sent keep their stored values"
                          },
                          "CTC": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Bar spacing (CTC), current length unit, 0 or greater"
                          },
                          "SIZE1": {
                            "type": "string",
                            "description": "Bar size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          },
                          "SIZE2": {
                            "type": "string",
                            "description": "Second bar size of the layer, or empty. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          },
                          "DB": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Distance from the bottom face to the layer, current length unit, 0 or greater and increasing with the layer number"
                          }
                        }
                      },
                      "description": "Layers matched by LAYER. Layers that are not listed keep their stored values, and an empty list changes nothing. A layer number above the layer count is rejected"
                    }
                  }
                }
              }
            },
            "DISTRIBUTION": {
              "type": "object",
              "description": "Distribution bar. A new record starts with one empty layer in each table, as in the dialog, so send SIZE1 for it or set LAYER to 0",
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "object",
                  "description": "Distribution bar layers on the top side",
                  "additionalProperties": false,
                  "properties": {
                    "LAYER": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 3,
                      "description": "Number of layers, 0 to 3. Lowering it clears the layers above the new count"
                    },
                    "LAYERS": {
                      "type": "array",
                      "maxItems": 3,
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                          "LAYER"
                        ],
                        "properties": {
                          "LAYER": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 3,
                            "description": "Layer number, 1 to 3. Identifies the layer; properties not sent keep their stored values. The design uses the cover of the main rebar layer with the same number"
                          },
                          "CTC": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Bar spacing (CTC), current length unit, 0 or greater"
                          },
                          "SIZE1": {
                            "type": "string",
                            "description": "Bar size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          }
                        }
                      },
                      "description": "Layers matched by LAYER. Layers that are not listed keep their stored values, and an empty list changes nothing. A layer number above the layer count is rejected"
                    }
                  }
                },
                "BOTTOM": {
                  "type": "object",
                  "description": "Distribution bar layers on the bottom side",
                  "additionalProperties": false,
                  "properties": {
                    "LAYER": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 3,
                      "description": "Number of layers, 0 to 3. Lowering it clears the layers above the new count"
                    },
                    "LAYERS": {
                      "type": "array",
                      "maxItems": 3,
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": [
                          "LAYER"
                        ],
                        "properties": {
                          "LAYER": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 3,
                            "description": "Layer number, 1 to 3. Identifies the layer; properties not sent keep their stored values. The design uses the cover of the main rebar layer with the same number"
                          },
                          "CTC": {
                            "type": "number",
                            "minimum": 0,
                            "description": "Bar spacing (CTC), current length unit, 0 or greater"
                          },
                          "SIZE1": {
                            "type": "string",
                            "description": "Bar size. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                          }
                        }
                      },
                      "description": "Layers matched by LAYER. Layers that are not listed keep their stored values, and an empty list changes nothing. A layer number above the layer count is rejected"
                    }
                  }
                }
              }
            },
            "USE_STIRRUP": {
              "type": "boolean",
              "default": false,
              "description": "Use stirrups (Stirrup checkbox) in the shear check. A new record starts with false"
            },
            "STIRRUP": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "SIZE": {
                  "type": "string",
                  "description": "Stirrup bar size. Always returned and stored, because the column hoop check uses it even when USE_STIRRUP is false. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                },
                "SPACING": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Stirrup spacing, current length unit. Greater than 0 when USE_STIRRUP is true, 0 or greater otherwise"
                },
                "NUMBER": {
                  "type": "integer",
                  "minimum": 0,
                  "description": "Number of stirrup legs. Greater than 0 when USE_STIRRUP is true, 0 or greater otherwise"
                }
              },
              "description": "Stirrup size, spacing and number of legs. Stored even when USE_STIRRUP is false (the column hoop check uses it). Deleting a record also deletes the plate column checking data that refer to it"
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

- `RIPC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "NAME": "PC-1",
      "MAIN": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#6",
              "DT": 0.05
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#6",
              "DB": 0.05
            }
          ]
        }
      },
      "DISTRIBUTION": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        }
      },
      "STIRRUP": {
        "SIZE": "#4",
        "SPACING": 0.15,
        "NUMBER": 2
      },
      "USE_STIRRUP": false
    }
  }
}
```

**Response**

```json
{
  "RIPC": {
    "1": {
      "NAME": "PC-1",
      "MAIN": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#6",
              "DT": 0.05
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#6",
              "DB": 0.05
            }
          ]
        }
      },
      "DISTRIBUTION": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        }
      },
      "STIRRUP": {
        "SIZE": "#4",
        "SPACING": 0.15,
        "NUMBER": 2
      },
      "USE_STIRRUP": false
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/RIPC"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/RIPC

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "NAME": "PC-1",
      "MAIN": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#6",
              "DT": 0.05
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.2,
              "SIZE1": "#6",
              "DB": 0.05
            }
          ]
        }
      },
      "DISTRIBUTION": {
        "TOP": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        },
        "BOTTOM": {
          "LAYER": 1,
          "LAYERS": [
            {
              "LAYER": 1,
              "CTC": 0.3,
              "SIZE1": "#4"
            }
          ]
        }
      },
      "STIRRUP": {
        "SIZE": "#4",
        "SPACING": 0.15,
        "NUMBER": 2
      },
      "USE_STIRRUP": false
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 23. `PBDD` — Plate Beam Data for Design

> **기능** 판 보의 설계용 데이터를 입력합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738195863065) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738256740633)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PBDD`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PBDD`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a row ID string (e.g., "1") of the data list. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sub-Domain · Minimum: 1 | `"SUB_DOMAIN"` | integer | - | **Required** |
| 2 | [General] Plate Force Option · Element: "ELEMENT" · Avg. Nodal: "AVG. NODAL" | `"FORCE_OPTION"` | string | ELEMENT | Optional |
| 3 | [General] Main Rebar Direction · Dir. 1: "DIR. 1" · Dir. 2: "DIR. 2" | `"DIRECTION"` | string | DIR. 1 | Optional |
| 4 | [General] Stirrups Data | `"STIRRUP"` | object | - | Optional |
| 4.1 | └ [General] Size | `"SIZE"` | string | - | Optional |
| 4.2 | └ [General] Number · Minimum: 0 | `"NUMBER"` | integer | 0 | Optional |
| 5 | [General] Dt · Minimum: 0 | `"DT"` | number | - | **Required** |
| 6 | [General] Db · Minimum: 0 | `"DB"` | number | - | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a row ID string (e.g., \"1\") of the data list.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Plate Beam Data for Design",
          "type": "object",
          "required": [
            "SUB_DOMAIN",
            "DT",
            "DB"
          ],
          "additionalProperties": false,
          "properties": {
            "SUB_DOMAIN": {
              "type": "integer",
              "minimum": 1,
              "description": "Sub-domain number (key of an existing plate beam sub-domain of the model, e.g. 1, 2, 3). The sub-domain must exist and be a plate beam sub-domain; at most one row per sub-domain, whatever the direction"
            },
            "FORCE_OPTION": {
              "type": "string",
              "description": "Plate force option",
              "default": "ELEMENT",
              "enum": [
                "ELEMENT",
                "AVG. NODAL"
              ]
            },
            "DIRECTION": {
              "type": "string",
              "description": "Main reinforcement direction",
              "default": "DIR. 1",
              "enum": [
                "DIR. 1",
                "DIR. 2"
              ]
            },
            "STIRRUP": {
              "type": "object",
              "description": "Stirrups: bar size and number of legs",
              "additionalProperties": false,
              "properties": {
                "SIZE": {
                  "type": "string",
                  "description": "Stirrup bar size. May be empty when NUMBER is 0. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                },
                "NUMBER": {
                  "type": "integer",
                  "minimum": 0,
                  "default": 0,
                  "description": "Number of stirrup legs (>= 0). 0 means no stirrups"
                }
              }
            },
            "DT": {
              "type": "number",
              "exclusiveMinimum": 0,
              "description": "Distance Dt from the top fiber to the centroid of the top reinforcement (> 0, model length unit)"
            },
            "DB": {
              "type": "number",
              "exclusiveMinimum": 0,
              "description": "Distance Db from the bottom fiber to the centroid of the bottom reinforcement (> 0, model length unit)"
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

- `PBDD`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "SUB_DOMAIN": 1,
      "FORCE_OPTION": "ELEMENT",
      "DIRECTION": "DIR. 1",
      "STIRRUP": {
        "SIZE": "#4",
        "NUMBER": 2
      },
      "DT": 0.05,
      "DB": 0.05
    }
  }
}
```

**Response**

```json
{
  "PBDD": {
    "1": {
      "SUB_DOMAIN": 1,
      "FORCE_OPTION": "ELEMENT",
      "DIRECTION": "DIR. 1",
      "STIRRUP": {
        "SIZE": "#4",
        "NUMBER": 2
      },
      "DT": 0.05,
      "DB": 0.05
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PBDD"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PBDD

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "SUB_DOMAIN": 1,
      "FORCE_OPTION": "ELEMENT",
      "DIRECTION": "DIR. 1",
      "STIRRUP": {
        "SIZE": "#4",
        "NUMBER": 2
      },
      "DT": 0.05,
      "DB": 0.05
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 24. `PBDC` — Plate Beam Data for Checking

> **기능** 판 보의 검토용 데이터를 입력합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738205576857) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738262829209)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PBDC`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PBDC`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a row ID string (e.g., "1") of the data list. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sub-Domain · Minimum: 1 | `"SUB_DOMAIN"` | integer | - | **Required** |
| 2 | [General] Plate Force Option · Element: "ELEMENT" · Avg. Nodal: "AVG. NODAL" | `"FORCE_OPTION"` | string | ELEMENT | Optional |
| 3 | [General] Checking Direction · Dir. 1: "DIR. 1" · Dir. 2: "DIR. 2" | `"DIRECTION"` | string | DIR. 1 | Optional |
| 4 | [General] Rebar Data | `"REINFORCEMENT"` | string | - | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a row ID string (e.g., \"1\") of the data list.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Plate Beam Data for Checking",
          "type": "object",
          "required": [
            "SUB_DOMAIN",
            "REINFORCEMENT"
          ],
          "additionalProperties": false,
          "properties": {
            "SUB_DOMAIN": {
              "type": "integer",
              "minimum": 1,
              "description": "Sub-domain number (key of an existing plate beam sub-domain of the model, e.g. 1, 2, 3). The sub-domain must exist and be a plate beam sub-domain; at most one row per sub-domain, whatever the direction"
            },
            "FORCE_OPTION": {
              "type": "string",
              "description": "Plate force option",
              "default": "ELEMENT",
              "enum": [
                "ELEMENT",
                "AVG. NODAL"
              ]
            },
            "DIRECTION": {
              "type": "string",
              "description": "Checking direction",
              "default": "DIR. 1",
              "enum": [
                "DIR. 1",
                "DIR. 2"
              ]
            },
            "REINFORCEMENT": {
              "type": "string",
              "description": "Name of the plate beam rebar input (RIPB) to check against"
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

- `PBDC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "SUB_DOMAIN": 1,
      "FORCE_OPTION": "AVG. NODAL",
      "DIRECTION": "DIR. 2",
      "REINFORCEMENT": "PB-1"
    }
  }
}
```

**Response**

```json
{
  "PBDC": {
    "1": {
      "SUB_DOMAIN": 1,
      "FORCE_OPTION": "AVG. NODAL",
      "DIRECTION": "DIR. 2",
      "REINFORCEMENT": "PB-1"
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PBDC"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PBDC

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "SUB_DOMAIN": 1,
      "FORCE_OPTION": "AVG. NODAL",
      "DIRECTION": "DIR. 2",
      "REINFORCEMENT": "PB-1"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 25. `PCDD` — Plate Column Data for Design

> **기능** 판 기둥의 설계용 데이터를 입력합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738205789081) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738263039641)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PCDD`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PCDD`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a row ID string (e.g., "1") of the data list. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sub-Domain · Minimum: 1 | `"SUB_DOMAIN"` | integer | - | **Required** |
| 2 | [General] Plate Force Option · Element: "ELEMENT" · Avg. Nodal: "AVG. NODAL" | `"FORCE_OPTION"` | string | ELEMENT | Optional |
| 3 | [General] Main Rebar Direction · Dir. 1: "DIR. 1" · Dir. 2: "DIR. 2" | `"DIRECTION"` | string | DIR. 1 | Optional |
| 4 | [General] Stirrups Data | `"STIRRUP"` | object | - | Optional |
| 4.1 | └ [General] Size | `"SIZE"` | string | - | Optional |
| 4.2 | └ [General] Number · Minimum: 0 | `"NUMBER"` | integer | 0 | Optional |
| 5 | [General] Dt · Minimum: 0 | `"DT"` | number | - | **Required** |
| 6 | [General] Db · Minimum: 0 | `"DB"` | number | - | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a row ID string (e.g., \"1\") of the data list.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Plate Column Data for Design",
          "type": "object",
          "required": [
            "SUB_DOMAIN",
            "DT",
            "DB"
          ],
          "additionalProperties": false,
          "properties": {
            "SUB_DOMAIN": {
              "type": "integer",
              "minimum": 1,
              "description": "Sub-domain number (key of an existing plate column sub-domain of the model, e.g. 1, 2, 3). The sub-domain must exist and be a plate column sub-domain; at most one row per sub-domain, whatever the direction"
            },
            "FORCE_OPTION": {
              "type": "string",
              "description": "Plate force option",
              "default": "ELEMENT",
              "enum": [
                "ELEMENT",
                "AVG. NODAL"
              ]
            },
            "DIRECTION": {
              "type": "string",
              "description": "Main reinforcement direction",
              "default": "DIR. 1",
              "enum": [
                "DIR. 1",
                "DIR. 2"
              ]
            },
            "STIRRUP": {
              "type": "object",
              "description": "Stirrups: bar size and number of legs",
              "additionalProperties": false,
              "properties": {
                "SIZE": {
                  "type": "string",
                  "description": "Stirrup bar size. May be empty when NUMBER is 0. Rebar designation from the model's concrete rebar size list (not a fixed enum: one list per model, chosen by the concrete rebar material code)"
                },
                "NUMBER": {
                  "type": "integer",
                  "minimum": 0,
                  "default": 0,
                  "description": "Number of stirrup legs (>= 0). 0 means no stirrups"
                }
              }
            },
            "DT": {
              "type": "number",
              "exclusiveMinimum": 0,
              "description": "Distance Dt from the top fiber to the centroid of the top reinforcement (> 0, model length unit)"
            },
            "DB": {
              "type": "number",
              "exclusiveMinimum": 0,
              "description": "Distance Db from the bottom fiber to the centroid of the bottom reinforcement (> 0, model length unit)"
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

- `PCDD`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "SUB_DOMAIN": 2,
      "FORCE_OPTION": "AVG. NODAL",
      "DIRECTION": "DIR. 2",
      "DT": 0.05,
      "DB": 0.05
    }
  }
}
```

**Response**

```json
{
  "PCDD": {
    "1": {
      "SUB_DOMAIN": 2,
      "FORCE_OPTION": "AVG. NODAL",
      "DIRECTION": "DIR. 2",
      "DT": 0.05,
      "DB": 0.05
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PCDD"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PCDD

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "SUB_DOMAIN": 2,
      "FORCE_OPTION": "AVG. NODAL",
      "DIRECTION": "DIR. 2",
      "DT": 0.05,
      "DB": 0.05
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 26. `PCDC` — Plate Column Data for Checking

> **기능** 판 기둥의 검토용 데이터를 입력합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738209928473) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738258023577)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PCDC`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PCDC`

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a row ID string (e.g., "1") of the data list. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sub-Domain · Minimum: 1 | `"SUB_DOMAIN"` | integer | - | **Required** |
| 2 | [General] Plate Force Option · Element: "ELEMENT" · Avg. Nodal: "AVG. NODAL" | `"FORCE_OPTION"` | string | ELEMENT | Optional |
| 3 | [General] Checking Direction · Dir. 1: "DIR. 1" · Dir. 2: "DIR. 2" | `"DIRECTION"` | string | DIR. 1 | Optional |
| 4 | [General] Rebar Data | `"REINFORCEMENT"` | string | - | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a row ID string (e.g., \"1\") of the data list.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Plate Column Data for Checking",
          "type": "object",
          "required": [
            "SUB_DOMAIN",
            "REINFORCEMENT"
          ],
          "additionalProperties": false,
          "properties": {
            "SUB_DOMAIN": {
              "type": "integer",
              "minimum": 1,
              "description": "Sub-domain number (key of an existing plate column sub-domain of the model, e.g. 1, 2, 3). The sub-domain must exist and be a plate column sub-domain; at most one row per sub-domain, whatever the direction"
            },
            "FORCE_OPTION": {
              "type": "string",
              "description": "Plate force option",
              "default": "ELEMENT",
              "enum": [
                "ELEMENT",
                "AVG. NODAL"
              ]
            },
            "DIRECTION": {
              "type": "string",
              "description": "Checking direction",
              "default": "DIR. 1",
              "enum": [
                "DIR. 1",
                "DIR. 2"
              ]
            },
            "REINFORCEMENT": {
              "type": "string",
              "description": "Name of the plate column rebar input (RIPC) to check against"
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

- `PCDC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "SUB_DOMAIN": 2,
      "REINFORCEMENT": "PC-1"
    }
  }
}
```

**Response**

```json
{
  "PCDC": {
    "1": {
      "SUB_DOMAIN": 2,
      "REINFORCEMENT": "PC-1"
    }
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PCDC"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PCDC

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "SUB_DOMAIN": 2,
      "REINFORCEMENT": "PC-1"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 27. `BD-ANAL` — Beam Design Perform

> **기능** 보 설계를 수행합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738197210521) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738251141273)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/BD-ANAL`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/BD-ANAL`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Beam Design perform (RC Code Design) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Perform Target · All Elements: "ALL" · By Element No.: "ELEMS" · By Section No.: "SECTIONS" | `"PERFORM_TYPE"` | string | ALL | Optional |
| 2 | [When PERFORM_TYPE = "By Element No."] Element No. | `"ELEMS"` | object | - | **Required** |
| 2.1 | └ [When PERFORM_TYPE = "By Element No."] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [When PERFORM_TYPE = "By Element No."] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [When PERFORM_TYPE = "By Section No."] Section No. | `"SECTIONS"` | array | - | **Required** |

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
      "description": "Beam Design perform (RC Code Design)",
      "additionalProperties": false,
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for design calculation. ALL: all elements, ELEMS: by element numbers, SECTIONS: by section numbers.",
          "default": "ALL",
          "enum": [
            "ALL",
            "ELEMS",
            "SECTIONS"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Give one of KEYS or TO (when both are given the product uses KEYS).",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section No. input. Required when PERFORM_TYPE is SECTIONS.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- **By Element No. (ELEMS)** — `message`
- **All Elements (ALL)** — `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`
- **By Section No. (SECTIONS)** — `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`, `DETAILS`

### Request / Response JSON

**Request — By Element No. (ELEMS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        79,
        80,
        81
      ]
    }
  }
}
```

**Request — All Elements (ALL)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
```

**Request — By Section No. (SECTIONS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "SECTIONS",
    "SECTIONS": [
      1
    ]
  }
}
```

**Response — By Element No. (ELEMS)**

```json
{
  "message": "success"
}
```

**Response — All Elements (ALL)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — By Section No. (SECTIONS)**

```json
{
  "SUCCESS": true,
  "RESULT": "PARTIAL_SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": "Some elements were skipped. See DETAILS.",
  "DETAILS": [
    "Elem 7: Not an RC beam (the member type is not Beam)."
  ]
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/BD-ANAL"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/BD-ANAL

payload = json.loads(r'''
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        79,
        80,
        81
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 28. `BD-TABLE` — Beam Design Table

> **기능** 보 설계 결과를 표로 반환합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738212961433) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738296500505)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/BD-TABLE`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/BD-TABLE`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Beam Design result table (Copy Table of the result dialog) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sorted by · Member: "MEMB" · Section: "PROP" | `"TABLE_TYPE"` | string | - | **Required** |
| 2 | [General] Primary Sorting Option · SECT: 0 · MEMB: 1 | `"PRI_SORT"` | integer | 1 | Optional |
| 3 | [General] Result View Option · All: 0 · OK: 1 · NG: 2 | `"RESULT"` | integer | 0 | Optional |
| 4 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 4.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 4.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 5 | [General] Section No. | `"SECTIONS"` | array | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 8 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 8.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 8.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 8.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 8.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 9 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 9.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 9.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 10 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |

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
      "description": "Beam Design result table (Copy Table of the result dialog)",
      "additionalProperties": false,
      "required": [
        "TABLE_TYPE"
      ],
      "properties": {
        "TABLE_TYPE": {
          "type": "string",
          "description": "Sorted by: MEMB (Member) or PROP (Section)",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "PRI_SORT": {
          "type": "integer",
          "description": "Primary sorting option (Member sort): 0 = SECT, 1 = MEMB",
          "default": 1,
          "enum": [
            0,
            1
          ]
        },
        "RESULT": {
          "type": "integer",
          "description": "Result view option: All / OK / NG",
          "default": 0,
          "enum": [
            0,
            1,
            2
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section numbers. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Columns to return, by column name (exact, case-sensitive; any other name is rejected). Empty or omitted = all columns. x-enum-labels gives the dialog caption of each name.",
          "items": {
            "type": "string",
            "enum": [
              "MEMB",
              "SECT",
              "Span",
              "Section",
              "Bc",
              "Hc",
              "bf",
              "hf",
              "fc",
              "fy",
              "fys",
              "POS",
              "CHK",
              "N_Mu",
              "N_LCB",
              "AsTop",
              "P_Mu",
              "P_LCB",
              "AsBot",
              "Vu",
              "V_LCB",
              "Av",
              "Tu",
              "T_LCB",
              "St",
              "Stirrups"
            ]
          }
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response table title"
        },
        "UNIT": {
          "type": "object",
          "description": "Response unit setting. Omitted = model unit system.",
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
          "description": "Response number format",
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
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result table save path (optional)"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Result Table` — `MEMB`, `SECT`, `Section`, `POS`, `CHK`, `N_Mu`, `N_LCB`, `AsTop`, `P_Mu`, `P_LCB`, `AsBot`, `Vu`, `V_LCB`, `Av`, `Stirrups`

### Request / Response JSON

**Request — Member (MEMB)**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        1
      ]
    },
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "POS",
      "CHK",
      "N_Mu",
      "N_LCB",
      "AsTop",
      "P_Mu",
      "P_LCB",
      "AsBot",
      "Vu",
      "V_LCB",
      "Av",
      "Stirrups"
    ]
  }
}
```

**Request — Section (PROP)**

```json
{
  "Argument": {
    "TABLE_TYPE": "PROP",
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        1
      ]
    },
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "POS",
      "CHK",
      "N_Mu",
      "N_LCB",
      "AsTop",
      "P_Mu",
      "P_LCB",
      "AsBot",
      "Vu",
      "V_LCB",
      "Av",
      "Stirrups"
    ]
  }
}
```

**Response — Member (MEMB)**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "POS",
      "CHK",
      "N_Mu",
      "N_LCB",
      "AsTop",
      "P_Mu",
      "P_LCB",
      "AsBot",
      "Vu",
      "V_LCB",
      "Av",
      "Stirrups"
    ],
    "DATA": [
      [
        "1",
        "1",
        "Beam",
        "I",
        "**V*",
        "492.613",
        "3-MY",
        "0.0024",
        "0.00000",
        "2+FY",
        "0.0000",
        "678.803",
        "5-FZ",
        "0.0020",
        "2.0-P10 @0.080"
      ],
      [
        "1",
        "1",
        "Beam",
        "M",
        "**V*",
        "410.563",
        "3-MY",
        "0.0020",
        "0.00000",
        "2+FY",
        "0.0000",
        "646.103",
        "5-FZ",
        "0.0020",
        "2.0-P10 @0.080"
      ],
      [
        "1",
        "1",
        "Beam",
        "J",
        "OK",
        "263.933",
        "3-MY",
        "0.0012",
        "52.3710",
        "4+MY",
        "0.0003",
        "341.177",
        "5+MY",
        "0.0020",
        "2.0-P10 @0.078"
      ]
    ]
  }
}
```

**Response — Section (PROP)**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "POS",
      "CHK",
      "N_Mu",
      "N_LCB",
      "AsTop",
      "P_Mu",
      "P_LCB",
      "AsBot",
      "Vu",
      "V_LCB",
      "Av",
      "Stirrups"
    ],
    "DATA": [
      [
        "0",
        "1",
        "B400x700",
        "I",
        "OK",
        "316.364",
        "1",
        "0.0014",
        "0.00000",
        "1",
        "0.0000",
        "342.988",
        "1",
        "0.0012",
        "2.0-#4  @0.208"
      ],
      [
        "0",
        "1",
        "B400x700",
        "M",
        "OK",
        "16.2488",
        "1",
        "0.0001",
        "326.740",
        "1",
        "0.0014",
        "257.241",
        "1",
        "0.0012",
        "2.0-#4  @0.208"
      ],
      [
        "0",
        "1",
        "B400x700",
        "J",
        "OK",
        "0.00000",
        "1",
        "0.0000",
        "369.613",
        "1",
        "0.0016",
        "85.7471",
        "1",
        "0.0017",
        "2.0-#4  @0.156"
      ]
    ]
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/BD-TABLE"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/BD-TABLE

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        1
      ]
    },
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "POS",
      "CHK",
      "N_Mu",
      "N_LCB",
      "AsTop",
      "P_Mu",
      "P_LCB",
      "AsBot",
      "Vu",
      "V_LCB",
      "Av",
      "Stirrups"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 29. `BD-REPORT` — Beam Design Report

> **기능** 보 설계 결과를 보고서 파일로 내보냅니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738210302361) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738251423129)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/BD-REPORT`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/BD-REPORT`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Beam Design report | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sorted by · Member: "MEMB" · Section: "PROP" | `"REPORT_TYPE"` | string | - | **Required** |
| 2 | [General] Report Mode · Graphic: "Graphic" · Detail: "Detail" · Summary: "Summary" · Summary By LCB: "SUMMARY BY LCB" | `"CURRENT_MODE_MEMB"` | string | - | Optional |
| 3 | [General] Report Mode · Graphic: "Graphic" · Summary: "Summary" | `"CURRENT_MODE_PROP"` | string | - | Optional |
| 4 | [General] Report Mode (common) · Graphic: "Graphic" · Detail: "Detail" · Summary: "Summary" · Summary By LCB: "SUMMARY BY LCB" | `"CURRENT_MODE"` | string | - | Optional |
| 5 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 5.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 5.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 6 | [General] Section No. | `"SECTIONS"` | array | - | Optional |
| 7 | [General] Option for Detail Print Position | `"DETAIL_POSITIONS"` | object | - | Optional |
| 7.1 | └ [General] I | `"END_I"` | boolean | true | Optional |
| 7.2 | └ [General] M | `"MID"` | boolean | false | Optional |
| 7.3 | └ [General] J | `"END_J"` | boolean | false | Optional |
| 8 | [General] Export Path | `"EXPORT_PATH"` | string | - | **Required** |
| 9 | [General] Output File Name | `"OUTPUT_NAME"` | string | - | **Required** |

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
      "description": "Beam Design report",
      "additionalProperties": false,
      "required": [
        "REPORT_TYPE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "properties": {
        "REPORT_TYPE": {
          "type": "string",
          "description": "Sorted by: MEMB (Member) or PROP (Section)",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "description": "Output when sorted by member (buttons of the result dialog) Takes precedence over CURRENT_MODE.",
          "enum": [
            "Graphic",
            "Detail",
            "Summary",
            "SUMMARY BY LCB"
          ]
        },
        "CURRENT_MODE_PROP": {
          "type": "string",
          "description": "Output when sorted by section (Detail and Summary By LCB are disabled in section order) Takes precedence over CURRENT_MODE.",
          "enum": [
            "Graphic",
            "Summary"
          ]
        },
        "CURRENT_MODE": {
          "type": "string",
          "description": "Report kind used when the mode of the REPORT_TYPE (CURRENT_MODE_MEMB / CURRENT_MODE_PROP) is not given; matched without regard to case",
          "enum": [
            "Graphic",
            "Detail",
            "Summary",
            "SUMMARY BY LCB"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section numbers. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "DETAIL_POSITIONS": {
          "type": "object",
          "description": "Option for Detail print position (I / M / J check boxes of the beam result dialog)",
          "additionalProperties": false,
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
          "description": "File name in EXPORT_PATH. Graphic: must end with .bmp, .emf or .jpg (otherwise INVALID_EXPORT_PATH). Detail: .doc is added when missing. Summary / SUMMARY BY LCB / PMCurve: .txt is added when there is no extension. An existing file of that name is replaced",
          "minLength": 1
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- **Member - Graphic / Member - Detail / Member - Summary By LCB / Member - Summary** — `SUCCESS`, `RESULT`, `CATEGORY`, `FILE_PATH`, `MESSAGE`
- **Section - Graphic / Section - Summary** — `SUCCESS`, `RESULT`, `CATEGORY`, `FILE_PATH`, `MESSAGE`, `DETAILS`

### Request / Response JSON

**LRFD24 Request — Member - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_24_Graphic.jpg",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD24 Request — Member - Detail**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_24_MEMB_Detail",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD24 Request — Member - Summary By LCB**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "SUMMARY BY LCB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_24_MEMB_SUMMARY_BY_LCB",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD24 Request — Member - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_24_MEMB_Summary",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD24 Request — Section - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_24_PROP_Graphic.jpg",
    "SECTIONS": [
      1
    ]
  }
}
```

**LRFD24 Request — Section - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_24_PROP_Summary",
    "SECTIONS": [
      1
    ]
  }
}
```

**LRFD24 Response — Member - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_24_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_24_MEMB_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Summary By LCB**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_24_MEMB_SUMMARY_BY_LCB.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_24_MEMB_Summary.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Section - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "PARTIAL_SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_24_PROP_Graphic.jpg",
  "MESSAGE": "Some elements were skipped. See DETAILS.",
  "DETAILS": [
    "Elem 7: Not an RC beam (the member type is not Beam)."
  ]
}
```

**LRFD24 Response — Section - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "PARTIAL_SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_24_PROP_Summary.txt",
  "MESSAGE": "Some elements were skipped. See DETAILS.",
  "DETAILS": [
    "Elem 7: Not an RC beam (the member type is not Beam)."
  ]
}
```

**LRFD20 Request — Member - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_20_Graphic.jpg",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD20 Request — Member - Detail**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_20_MEMB_Detail",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD20 Request — Member - Summary By LCB**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "SUMMARY BY LCB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_20_MEMB_SUMMARY_BY_LCB",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD20 Request — Member - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_20_MEMB_Summary",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD20 Request — Section - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_20_PROP_Graphic.jpg",
    "SECTIONS": [
      1
    ]
  }
}
```

**LRFD20 Request — Section - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_20_PROP_Summary",
    "SECTIONS": [
      1
    ]
  }
}
```

**LRFD20 Response — Member - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_20_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_20_MEMB_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Summary By LCB**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_20_MEMB_SUMMARY_BY_LCB.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_20_MEMB_Summary.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Section - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "PARTIAL_SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_20_PROP_Graphic.jpg",
  "MESSAGE": "Some elements were skipped. See DETAILS.",
  "DETAILS": [
    "Elem 7: Not an RC beam (the member type is not Beam)."
  ]
}
```

**LRFD20 Response — Section - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "PARTIAL_SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BD_20_PROP_Summary.txt",
  "MESSAGE": "Some elements were skipped. See DETAILS.",
  "DETAILS": [
    "Elem 7: Not an RC beam (the member type is not Beam)."
  ]
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/BD-REPORT"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/BD-REPORT

# 보고서 예제의 EXPORT_PATH는 사용할 저장 경로로 바꿉니다.
payload = json.loads(r'''
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BD_24_Graphic.jpg",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 30. `BC-ANAL` — Beam Checking Perform

> **기능** 보 검토를 수행합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738237317657) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738274149657)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/BC-ANAL`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/BC-ANAL`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Execute checking calculation | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Perform Target · All Elements: "ALL" · By Element No.: "ELEMS" · By Section No.: "SECTIONS" | `"PERFORM_TYPE"` | string | ALL | Optional |
| 2 | [When PERFORM_TYPE = "By Element No."] Element No. | `"ELEMS"` | object | - | **Required** |
| 2.1 | └ [When PERFORM_TYPE = "By Element No."] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [When PERFORM_TYPE = "By Element No."] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [When PERFORM_TYPE = "By Section No."] Section No. | `"SECTIONS"` | array | - | **Required** |

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
      "description": "Execute checking calculation",
      "additionalProperties": false,
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for checking. ALL: all elements, ELEMS: by element numbers, SECTIONS: by section numbers.",
          "default": "ALL",
          "enum": [
            "ALL",
            "ELEMS",
            "SECTIONS"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Give one of KEYS or TO (when both are given the product uses KEYS).",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section No. input. Required when PERFORM_TYPE is SECTIONS.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- **All Elements (ALL)** — `message`
- **By Element No. (ELEMS)** — `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`
- **By Section No. (SECTIONS)** — `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`, `DETAILS`

### Request / Response JSON

**Request — All Elements (ALL)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
```

**Request — By Element No. (ELEMS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**Request — By Section No. (SECTIONS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "SECTIONS",
    "SECTIONS": [
      1
    ]
  }
}
```

**Response — All Elements (ALL)**

```json
{
  "message": "success"
}
```

**Response — By Element No. (ELEMS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — By Section No. (SECTIONS)**

```json
{
  "SUCCESS": true,
  "RESULT": "PARTIAL_SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": "Some elements were skipped. See DETAILS.",
  "DETAILS": [
    "Elem 7: Not an RC beam (the member type is not Beam)."
  ]
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/BC-ANAL"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/BC-ANAL

payload = json.loads(r'''
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 31. `BC-TABLE` — Beam Checking Table

> **기능** 보 검토 결과를 표로 반환합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738222854937) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738311943577)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/BC-TABLE`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/BC-TABLE`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Beam Checking result table (Copy Table of the result dialog) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sorted by · Member: "MEMB" · Section: "PROP" | `"TABLE_TYPE"` | string | - | **Required** |
| 2 | [General] Primary Sorting Option · SECT: 0 · MEMB: 1 | `"PRI_SORT"` | integer | 1 | Optional |
| 3 | [General] Results · Strength: "STRENGTH" · Serviceability: "SERVICEABILITY" | `"LIMIT_STATE"` | string | - | **Required** |
| 4 | [General] Result View Option · All: 0 · OK: 1 · NG: 2 | `"RESULT"` | integer | 0 | Optional |
| 5 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 5.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 5.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 6 | [General] Section No. | `"SECTIONS"` | array | - | Optional |
| 7 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 8 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 9 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 9.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 9.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 9.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 9.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 10 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 10.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 10.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 11 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |

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
      "description": "Beam Checking result table (Copy Table of the result dialog)",
      "additionalProperties": false,
      "required": [
        "TABLE_TYPE",
        "LIMIT_STATE"
      ],
      "properties": {
        "TABLE_TYPE": {
          "type": "string",
          "description": "Sorted by: MEMB (Member) or PROP (Section)",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "PRI_SORT": {
          "type": "integer",
          "description": "Primary sorting option (Member sort): 0 = SECT, 1 = MEMB",
          "default": 1,
          "enum": [
            0,
            1
          ]
        },
        "LIMIT_STATE": {
          "type": "string",
          "description": "Results view of the check dialog: Strength or Serviceability columns",
          "enum": [
            "STRENGTH",
            "SERVICEABILITY"
          ]
        },
        "RESULT": {
          "type": "integer",
          "description": "Result view option: All / OK / NG",
          "default": 0,
          "enum": [
            0,
            1,
            2
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section numbers. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Columns to return, by column name (exact, case-sensitive). Only the columns of the LIMIT_STATE view are accepted: STRENGTH = common + strength columns, SERVICEABILITY = common + serviceability columns. Empty or omitted = all columns of the view. x-enum-labels gives the dialog caption of each name.",
          "items": {
            "type": "string",
            "enum": [
              "MEMB",
              "SECT",
              "Span",
              "Section",
              "Bc",
              "Hc",
              "bf",
              "hf",
              "fc",
              "fy",
              "fys",
              "POS",
              "CHK",
              "AsTop",
              "AsBot",
              "N_Mu",
              "N_Mr",
              "N_LCB",
              "Rat_N",
              "P_Mu",
              "P_Mr",
              "P_LCB",
              "Rat_P",
              "Vu",
              "pV",
              "V_LCB",
              "Rat_V",
              "Tu",
              "Tn",
              "T_LCB",
              "Rat_T",
              "Top_S",
              "Top_Sa",
              "Bot_S",
              "Bot_Sa"
            ]
          }
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response table title"
        },
        "UNIT": {
          "type": "object",
          "description": "Response unit setting. Omitted = model unit system.",
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
          "description": "Response number format",
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
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result table save path (optional)"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- **Member (MEMB) / Section (PROP)** — `RC Beam Checking Result` — `MEMB`, `SECT`, `Section`, `POS`, `CHK`, `N_Mu`, `N_Mr`, `N_LCB`, `Rat_N`, `P_Mu`, `P_Mr`, `P_LCB`, `Rat_P`, `Vu`, `pV`, `V_LCB`, `Rat_V`
- **Serviceability (SERVICEABILITY)** — `RC Beam Checking Result` — `MEMB`, `SECT`, `Span`, `Section`, `Bc`, `Hc`, `bf`, `hf`, `fc`, `fy`, `fys`, `POS`, `CHK`, `Top_S`, `Top_Sa`, `Bot_S`, `Bot_Sa`

### Request / Response JSON

**Request — Member (MEMB)**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "LIMIT_STATE": "STRENGTH",
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        1
      ]
    },
    "TABLE_NAME": "RC Beam Checking Result",
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "POS",
      "CHK",
      "N_Mu",
      "N_Mr",
      "N_LCB",
      "Rat_N",
      "P_Mu",
      "P_Mr",
      "P_LCB",
      "Rat_P",
      "Vu",
      "pV",
      "V_LCB",
      "Rat_V"
    ]
  }
}
```

**Request — Section (PROP)**

```json
{
  "Argument": {
    "TABLE_TYPE": "PROP",
    "LIMIT_STATE": "STRENGTH",
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        1
      ]
    },
    "TABLE_NAME": "RC Beam Checking Result",
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "POS",
      "CHK",
      "N_Mu",
      "N_Mr",
      "N_LCB",
      "Rat_N",
      "P_Mu",
      "P_Mr",
      "P_LCB",
      "Rat_P",
      "Vu",
      "pV",
      "V_LCB",
      "Rat_V"
    ]
  }
}
```

**Request — Serviceability (SERVICEABILITY)**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "LIMIT_STATE": "SERVICEABILITY",
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        1
      ]
    },
    "TABLE_NAME": "RC Beam Checking Result"
  }
}
```

**Response — Member (MEMB)**

```json
{
  "RC Beam Checking Result": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "POS",
      "CHK",
      "N_Mu",
      "N_Mr",
      "N_LCB",
      "Rat_N",
      "P_Mu",
      "P_Mr",
      "P_LCB",
      "Rat_P",
      "Vu",
      "pV",
      "V_LCB",
      "Rat_V"
    ],
    "DATA": [
      [
        "1",
        "1",
        "Beam",
        "I",
        "**V*",
        "492.613",
        "601.781",
        "3-MY",
        "0.819",
        "0.00000",
        "601.781",
        "2+FY",
        "0.000",
        "678.803",
        "562.289",
        "5-FZ",
        "1.207"
      ],
      [
        "1",
        "1",
        "Beam",
        "M",
        "**V*",
        "410.563",
        "601.781",
        "3-MY",
        "0.682",
        "0.00000",
        "601.781",
        "2+FY",
        "0.000",
        "646.103",
        "595.366",
        "5-FZ",
        "1.085"
      ],
      [
        "1",
        "1",
        "Beam",
        "J",
        "OK",
        "263.933",
        "601.781",
        "3-MY",
        "0.439",
        "52.3710",
        "601.781",
        "4+MY",
        "0.087",
        "596.044",
        "618.483",
        "5-FZ",
        "0.964"
      ]
    ]
  }
}
```

**Response — Section (PROP)**

```json
{
  "RC Beam Checking Result": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "POS",
      "CHK",
      "N_Mu",
      "N_Mr",
      "N_LCB",
      "Rat_N",
      "P_Mu",
      "P_Mr",
      "P_LCB",
      "Rat_P",
      "Vu",
      "pV",
      "V_LCB",
      "Rat_V"
    ],
    "DATA": [
      [
        "0",
        "1",
        "B400x700",
        "I",
        "OK",
        "316.364",
        "2784.82",
        "1",
        "0.114",
        "0.00000",
        "2784.82",
        "1",
        "0.000",
        "342.988",
        "641.230",
        "1",
        "0.535"
      ],
      [
        "0",
        "1",
        "B400x700",
        "M",
        "OK",
        "16.2488",
        "2784.82",
        "1",
        "0.006",
        "326.740",
        "2784.82",
        "1",
        "0.117",
        "257.241",
        "672.003",
        "1",
        "0.383"
      ],
      [
        "0",
        "1",
        "B400x700",
        "J",
        "OK",
        "0.00000",
        "2784.82",
        "1",
        "0.000",
        "369.613",
        "2784.82",
        "1",
        "0.133",
        "85.7471",
        "657.935",
        "1",
        "0.130"
      ]
    ]
  }
}
```

**Response — Serviceability (SERVICEABILITY)**

```json
{
  "RC Beam Checking Result": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Span",
      "Section",
      "Bc",
      "Hc",
      "bf",
      "hf",
      "fc",
      "fy",
      "fys",
      "POS",
      "CHK",
      "Top_S",
      "Top_Sa",
      "Bot_S",
      "Bot_Sa"
    ],
    "DATA": [
      [
        "1",
        "1",
        "4.0000",
        "B400x700",
        "0.4000",
        "0.7000",
        "0.0000",
        "0.0000",
        "27579.0",
        "413686",
        "275790",
        "I",
        "OK",
        "0.1200",
        "0.4572",
        "0.0000",
        "0.4572"
      ],
      [
        "1",
        "1",
        "4.0000",
        "B400x700",
        "0.4000",
        "0.7000",
        "0.0000",
        "0.0000",
        "27579.0",
        "413686",
        "275790",
        "M",
        "OK",
        "0.1200",
        "0.4572",
        "0.1200",
        "0.4572"
      ],
      [
        "1",
        "1",
        "4.0000",
        "B400x700",
        "0.4000",
        "0.7000",
        "0.0000",
        "0.0000",
        "27579.0",
        "413686",
        "275790",
        "J",
        "OK",
        "0.0000",
        "0.4572",
        "0.1200",
        "0.4572"
      ]
    ]
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/BC-TABLE"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/BC-TABLE

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "LIMIT_STATE": "STRENGTH",
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        1
      ]
    },
    "TABLE_NAME": "RC Beam Checking Result",
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "POS",
      "CHK",
      "N_Mu",
      "N_Mr",
      "N_LCB",
      "Rat_N",
      "P_Mu",
      "P_Mr",
      "P_LCB",
      "Rat_P",
      "Vu",
      "pV",
      "V_LCB",
      "Rat_V"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 32. `BC-REPORT` — Beam Checking Report

> **기능** 보 검토 결과를 보고서 파일로 내보냅니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738237510809) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738274509337)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/BC-REPORT`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/BC-REPORT`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Beam Checking report | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sorted by · Member: "MEMB" · Section: "PROP" | `"REPORT_TYPE"` | string | - | **Required** |
| 2 | [General] Report Mode · Graphic: "Graphic" · Detail: "Detail" · Summary: "Summary" · Summary By LCB: "SUMMARY BY LCB" | `"CURRENT_MODE_MEMB"` | string | - | Optional |
| 3 | [General] Report Mode · Graphic: "Graphic" · Summary: "Summary" | `"CURRENT_MODE_PROP"` | string | - | Optional |
| 4 | [General] Report Mode (common) · Graphic: "Graphic" · Detail: "Detail" · Summary: "Summary" · Summary By LCB: "SUMMARY BY LCB" | `"CURRENT_MODE"` | string | - | Optional |
| 5 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 5.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 5.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 6 | [General] Section No. | `"SECTIONS"` | array | - | Optional |
| 7 | [General] Option for Detail Print Position | `"DETAIL_POSITIONS"` | object | - | Optional |
| 7.1 | └ [General] I | `"END_I"` | boolean | true | Optional |
| 7.2 | └ [General] M | `"MID"` | boolean | false | Optional |
| 7.3 | └ [General] J | `"END_J"` | boolean | false | Optional |
| 8 | [General] Export Path | `"EXPORT_PATH"` | string | - | **Required** |
| 9 | [General] Output File Name | `"OUTPUT_NAME"` | string | - | **Required** |

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
      "description": "Beam Checking report",
      "additionalProperties": false,
      "required": [
        "REPORT_TYPE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "properties": {
        "REPORT_TYPE": {
          "type": "string",
          "description": "Sorted by: MEMB (Member) or PROP (Section)",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "description": "Output when sorted by member (buttons of the result dialog) Takes precedence over CURRENT_MODE.",
          "enum": [
            "Graphic",
            "Detail",
            "Summary",
            "SUMMARY BY LCB"
          ]
        },
        "CURRENT_MODE_PROP": {
          "type": "string",
          "description": "Output when sorted by section (Detail and Summary By LCB are disabled in section order) Takes precedence over CURRENT_MODE.",
          "enum": [
            "Graphic",
            "Summary"
          ]
        },
        "CURRENT_MODE": {
          "type": "string",
          "description": "Report kind used when the mode of the REPORT_TYPE (CURRENT_MODE_MEMB / CURRENT_MODE_PROP) is not given; matched without regard to case",
          "enum": [
            "Graphic",
            "Detail",
            "Summary",
            "SUMMARY BY LCB"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section numbers. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "DETAIL_POSITIONS": {
          "type": "object",
          "description": "Option for Detail print position (I / M / J check boxes of the beam result dialog)",
          "additionalProperties": false,
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
          "description": "File name in EXPORT_PATH. Graphic: must end with .bmp, .emf or .jpg (otherwise INVALID_EXPORT_PATH). Detail: .doc is added when missing. Summary / SUMMARY BY LCB / PMCurve: .txt is added when there is no extension. An existing file of that name is replaced",
          "minLength": 1
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- **Member - Detail / Member - Graphic / Member - Summary By LCB / Member - Summary** — `SUCCESS`, `RESULT`, `CATEGORY`, `FILE_PATH`, `MESSAGE`
- **Section - Graphic / Section - Summary** — `SUCCESS`, `RESULT`, `CATEGORY`, `FILE_PATH`, `MESSAGE`, `DETAILS`

### Request / Response JSON

**LRFD24 Request — Member - Detail**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_24_Detail",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    },
    "DETAIL_POSITIONS": {
      "END_I": false,
      "MID": false,
      "END_J": true
    }
  }
}
```

**LRFD24 Request — Member - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_24_MEMB_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD24 Request — Member - Summary By LCB**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "SUMMARY BY LCB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_24_MEMB_SUMMARY_BY_LCB",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD24 Request — Member - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_24_MEMB_Summary",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD24 Request — Section - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_24_PROP_Graphic.jpg",
    "SECTIONS": [
      1
    ]
  }
}
```

**LRFD24 Request — Section - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_24_PROP_Summary",
    "SECTIONS": [
      1
    ]
  }
}
```

**LRFD24 Response — Member - Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_24_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_24_MEMB_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Summary By LCB**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_24_MEMB_SUMMARY_BY_LCB.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_24_MEMB_Summary.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Section - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "PARTIAL_SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_24_PROP_Graphic.jpg",
  "MESSAGE": "Some elements were skipped. See DETAILS.",
  "DETAILS": [
    "Elem 7: Not an RC beam (the member type is not Beam)."
  ]
}
```

**LRFD24 Response — Section - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "PARTIAL_SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_24_PROP_Summary.txt",
  "MESSAGE": "Some elements were skipped. See DETAILS.",
  "DETAILS": [
    "Elem 7: Not an RC beam (the member type is not Beam)."
  ]
}
```

**LRFD20 Request — Member - Detail**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_20_Detail",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    },
    "DETAIL_POSITIONS": {
      "END_I": false,
      "MID": false,
      "END_J": true
    }
  }
}
```

**LRFD20 Request — Member - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_20_MEMB_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD20 Request — Member - Summary By LCB**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "SUMMARY BY LCB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_20_MEMB_SUMMARY_BY_LCB",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD20 Request — Member - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_20_MEMB_Summary",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    }
  }
}
```

**LRFD20 Request — Section - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_20_PROP_Graphic.jpg",
    "SECTIONS": [
      1
    ]
  }
}
```

**LRFD20 Request — Section - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_20_PROP_Summary",
    "SECTIONS": [
      1
    ]
  }
}
```

**LRFD20 Response — Member - Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_20_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_20_MEMB_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Summary By LCB**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_20_MEMB_SUMMARY_BY_LCB.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_20_MEMB_Summary.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Section - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "PARTIAL_SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_20_PROP_Graphic.jpg",
  "MESSAGE": "Some elements were skipped. See DETAILS.",
  "DETAILS": [
    "Elem 7: Not an RC beam (the member type is not Beam)."
  ]
}
```

**LRFD20 Response — Section - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "PARTIAL_SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\BC_20_PROP_Summary.txt",
  "MESSAGE": "Some elements were skipped. See DETAILS.",
  "DETAILS": [
    "Elem 7: Not an RC beam (the member type is not Beam)."
  ]
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/BC-REPORT"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/BC-REPORT

# 보고서 예제의 EXPORT_PATH는 사용할 저장 경로로 바꿉니다.
payload = json.loads(r'''
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "BC_24_Detail",
    "ELEMS": {
      "KEYS": [
        1,
        2
      ]
    },
    "DETAIL_POSITIONS": {
      "END_I": false,
      "MID": false,
      "END_J": true
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 33. `CD-ANAL` — Column Design Perform

> **기능** 기둥 설계를 수행합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738236128793) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738251691033)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/CD-ANAL`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/CD-ANAL`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Column Design perform (RC Code Design) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Perform Target · All Elements: "ALL" · By Element No.: "ELEMS" · By Section No.: "SECTIONS" | `"PERFORM_TYPE"` | string | ALL | Optional |
| 2 | [When PERFORM_TYPE = "By Element No."] Element No. | `"ELEMS"` | object | - | **Required** |
| 2.1 | └ [When PERFORM_TYPE = "By Element No."] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [When PERFORM_TYPE = "By Element No."] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [When PERFORM_TYPE = "By Section No."] Section No. | `"SECTIONS"` | array | - | **Required** |

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
      "description": "Column Design perform (RC Code Design)",
      "additionalProperties": false,
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for design calculation. ALL: all elements, ELEMS: by element numbers, SECTIONS: by section numbers.",
          "default": "ALL",
          "enum": [
            "ALL",
            "ELEMS",
            "SECTIONS"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Give one of KEYS or TO (when both are given the product uses KEYS).",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section No. input. Required when PERFORM_TYPE is SECTIONS.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- **By Element No. (ELEMS)** — `message`
- **All Elements (ALL) / By Section No. (SECTIONS)** — `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`

### Request / Response JSON

**Request — By Element No. (ELEMS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        105,
        915
      ]
    }
  }
}
```

**Request — All Elements (ALL)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
```

**Request — By Section No. (SECTIONS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "SECTIONS",
    "SECTIONS": [
      2
    ]
  }
}
```

**Response — By Element No. (ELEMS)**

```json
{
  "message": "success"
}
```

**Response — All Elements (ALL)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — By Section No. (SECTIONS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/CD-ANAL"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/CD-ANAL

payload = json.loads(r'''
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        105,
        915
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 34. `CD-TABLE` — Column Design Table

> **기능** 기둥 설계 결과를 표로 반환합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738230363929) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738292710681)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/CD-TABLE`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/CD-TABLE`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Column Design result table (Copy Table of the result dialog) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sorted by · Member: "MEMB" · Section: "PROP" | `"TABLE_TYPE"` | string | - | **Required** |
| 2 | [General] Primary Sorting Option · SECT: 0 · MEMB: 1 | `"PRI_SORT"` | integer | 1 | Optional |
| 3 | [General] Result View Option · All: 0 · OK: 1 · NG: 2 | `"RESULT"` | integer | 0 | Optional |
| 4 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 4.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 4.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 5 | [General] Section No. | `"SECTIONS"` | array | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 8 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 8.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 8.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 8.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 8.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 9 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 9.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 9.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 10 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |

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
      "description": "Column Design result table (Copy Table of the result dialog)",
      "additionalProperties": false,
      "required": [
        "TABLE_TYPE"
      ],
      "properties": {
        "TABLE_TYPE": {
          "type": "string",
          "description": "Sorted by: MEMB (Member) or PROP (Section)",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "PRI_SORT": {
          "type": "integer",
          "description": "Primary sorting option (Member sort): 0 = SECT, 1 = MEMB",
          "default": 1,
          "enum": [
            0,
            1
          ]
        },
        "RESULT": {
          "type": "integer",
          "description": "Result view option: All / OK / NG",
          "default": 0,
          "enum": [
            0,
            1,
            2
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section numbers. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Columns to return, by column name (exact, case-sensitive; any other name is rejected). Empty or omitted = all columns. x-enum-labels gives the dialog caption of each name.",
          "items": {
            "type": "string",
            "enum": [
              "MEMB",
              "SECT",
              "Section",
              "t",
              "Bc",
              "a",
              "Hc",
              "b",
              "fc",
              "Height",
              "fy",
              "fys",
              "CHK",
              "LCB",
              "POS",
              "Pu",
              "Rat_P",
              "Mc",
              "Rat_M",
              "Ast",
              "V_LCB",
              "V_POS",
              "Asvy",
              "Asvz",
              "Ties_Spirals",
              "Vu",
              "Rat_V"
            ]
          }
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response table title"
        },
        "UNIT": {
          "type": "object",
          "description": "Response unit setting. Omitted = model unit system.",
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
          "description": "Response number format",
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
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result table save path (optional)"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Result Table` — `MEMB`, `SECT`, `Section`, `t`, `Bc`, `a`, `Hc`, `b`, `fc`, `Height`, `fy`, `fys`, `CHK`, `LCB`, `POS`, `Pu`, `Rat_P`, `Mc`, `Rat_M`, `Ast`, `V_LCB`, `V_POS`, `Asvy`, `Asvz`, `Ties_Spirals`, `Vu`, `Rat_V`

### Request / Response JSON

**Request — Member (MEMB)**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**Request — Section (PROP)**

```json
{
  "Argument": {
    "TABLE_TYPE": "PROP",
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**Response — Member (MEMB)**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "t",
      "Bc",
      "a",
      "Hc",
      "b",
      "fc",
      "Height",
      "fy",
      "fys",
      "CHK",
      "LCB",
      "POS",
      "Pu",
      "Rat_P",
      "Mc",
      "Rat_M",
      "Ast",
      "V_LCB",
      "V_POS",
      "Asvy",
      "Asvz",
      "Ties_Spirals",
      "Vu",
      "Rat_V"
    ],
    "DATA": [
      [
        "5",
        "2",
        "C500x500",
        "0.0000",
        "0.5000",
        "0.0000",
        "0.5000",
        "0.0000",
        "27579.0",
        "3.0000",
        "413686",
        "275790",
        "**V",
        "1",
        "J",
        "367.972",
        "0.959",
        "316.364",
        "0.959",
        "0.0034",
        "1",
        "J",
        "0.0000",
        "0.0000",
        "2.0-#4  @0.304",
        "311.311",
        "1.146"
      ],
      [
        "6",
        "2",
        "C500x500",
        "0.0000",
        "0.5000",
        "0.0000",
        "0.5000",
        "0.0000",
        "27579.0",
        "3.0000",
        "413686",
        "275790",
        "**V",
        "1",
        "J",
        "367.972",
        "0.959",
        "316.364",
        "0.959",
        "0.0034",
        "1",
        "J",
        "0.0000",
        "0.0000",
        "2.0-#4  @0.304",
        "370.958",
        "1.178"
      ]
    ]
  }
}
```

**Response — Section (PROP)**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "t",
      "Bc",
      "a",
      "Hc",
      "b",
      "fc",
      "Height",
      "fy",
      "fys",
      "CHK",
      "LCB",
      "POS",
      "Pu",
      "Rat_P",
      "Mc",
      "Rat_M",
      "Ast",
      "V_LCB",
      "V_POS",
      "Asvy",
      "Asvz",
      "Ties_Spirals",
      "Vu",
      "Rat_V"
    ],
    "DATA": [
      [
        "0",
        "2",
        "C500x500",
        "0.0000",
        "0.5000",
        "0.0000",
        "0.5000",
        "0.0000",
        "27579.0",
        "3.0000",
        "413686",
        "275790",
        "**V",
        "1",
        "J",
        "367.972",
        "0.959",
        "316.364",
        "0.959",
        "0.0034",
        "1",
        "J",
        "0.0000",
        "0.0000",
        "2.0-#4  @0.304",
        "370.958",
        "1.178"
      ]
    ]
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/CD-TABLE"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/CD-TABLE

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 35. `CD-REPORT` — Column Design Report

> **기능** 기둥 설계 결과를 보고서 파일로 내보냅니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738227830297) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738280917785)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/CD-REPORT`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/CD-REPORT`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Column Design report | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sorted by · Member: "MEMB" · Section: "PROP" | `"REPORT_TYPE"` | string | - | **Required** |
| 2 | [General] Report Mode · Graphic: "Graphic" · Detail: "Detail" · Summary: "Summary" · Summary By LCB: "SUMMARY BY LCB" · Draw PM Curve: "PMCurve" | `"CURRENT_MODE_MEMB"` | string | - | Optional |
| 3 | [General] Report Mode · Graphic: "Graphic" · Summary: "Summary" · Draw PM Curve: "PMCurve" | `"CURRENT_MODE_PROP"` | string | - | Optional |
| 4 | [General] Report Mode (common) · Graphic: "Graphic" · Detail: "Detail" · Summary: "Summary" · Summary By LCB: "SUMMARY BY LCB" · Draw PM Curve: "PMCurve" | `"CURRENT_MODE"` | string | - | Optional |
| 5 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 5.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 5.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 6 | [General] Section No. | `"SECTIONS"` | array | - | Optional |
| 7 | [General] Export Path | `"EXPORT_PATH"` | string | - | **Required** |
| 8 | [General] Output File Name | `"OUTPUT_NAME"` | string | - | **Required** |

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
      "description": "Column Design report",
      "additionalProperties": false,
      "required": [
        "REPORT_TYPE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "properties": {
        "REPORT_TYPE": {
          "type": "string",
          "description": "Sorted by: MEMB (Member) or PROP (Section)",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "description": "Output when sorted by member (buttons of the result dialog) Takes precedence over CURRENT_MODE.",
          "enum": [
            "Graphic",
            "Detail",
            "Summary",
            "SUMMARY BY LCB",
            "PMCurve"
          ]
        },
        "CURRENT_MODE_PROP": {
          "type": "string",
          "description": "Output when sorted by section (Detail and Summary By LCB are disabled in section order) Takes precedence over CURRENT_MODE.",
          "enum": [
            "Graphic",
            "Summary",
            "PMCurve"
          ]
        },
        "CURRENT_MODE": {
          "type": "string",
          "description": "Report kind used when the mode of the REPORT_TYPE (CURRENT_MODE_MEMB / CURRENT_MODE_PROP) is not given; matched without regard to case",
          "enum": [
            "Graphic",
            "Detail",
            "Summary",
            "SUMMARY BY LCB",
            "PMCurve"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section numbers. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Directory path to save the report files"
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "File name in EXPORT_PATH. Graphic: must end with .bmp, .emf or .jpg (otherwise INVALID_EXPORT_PATH). Detail: .doc is added when missing. Summary / SUMMARY BY LCB / PMCurve: .txt is added when there is no extension. An existing file of that name is replaced",
          "minLength": 1
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SUCCESS`, `RESULT`, `CATEGORY`, `FILE_PATH`, `MESSAGE`

### Request / Response JSON

**LRFD24 Request — Member - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_24_Graphic.jpg",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD24 Request — Member - Detail**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_24_MEMB_Detail",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD24 Request — Member - Draw PM Curve**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_24_MEMB_PMCurve",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD24 Request — Member - Summary By LCB**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "SUMMARY BY LCB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_24_MEMB_SUMMARY_BY_LCB",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD24 Request — Member - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_24_MEMB_Summary",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD24 Request — Section - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_24_PROP_Graphic.jpg",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD24 Request — Section - Draw PM Curve**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_24_PROP_PMCurve",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD24 Request — Section - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_24_PROP_Summary",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD24 Response — Member - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_24_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_24_MEMB_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Draw PM Curve**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_24_MEMB_PMCurve.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Summary By LCB**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_24_MEMB_SUMMARY_BY_LCB.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_24_MEMB_Summary.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Section - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_24_PROP_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD24 Response — Section - Draw PM Curve**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_24_PROP_PMCurve.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Section - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_24_PROP_Summary.txt",
  "MESSAGE": ""
}
```

**LRFD20 Request — Member - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_20_Graphic.jpg",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD20 Request — Member - Detail**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_20_MEMB_Detail",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD20 Request — Member - Draw PM Curve**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_20_MEMB_PMCurve",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD20 Request — Member - Summary By LCB**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "SUMMARY BY LCB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_20_MEMB_SUMMARY_BY_LCB",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD20 Request — Member - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_20_MEMB_Summary",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD20 Request — Section - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_20_PROP_Graphic.jpg",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD20 Request — Section - Draw PM Curve**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_20_PROP_PMCurve",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD20 Request — Section - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_20_PROP_Summary",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD20 Response — Member - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_20_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_20_MEMB_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Draw PM Curve**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_20_MEMB_PMCurve.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Summary By LCB**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_20_MEMB_SUMMARY_BY_LCB.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_20_MEMB_Summary.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Section - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_20_PROP_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD20 Response — Section - Draw PM Curve**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_20_PROP_PMCurve.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Section - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CD_20_PROP_Summary.txt",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/CD-REPORT"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/CD-REPORT

# 보고서 예제의 EXPORT_PATH는 사용할 저장 경로로 바꿉니다.
payload = json.loads(r'''
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CD_24_Graphic.jpg",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 36. `CC-ANAL` — Column Checking Perform

> **기능** 기둥 검토를 수행합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738211981849) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738283304089)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/CC-ANAL`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/CC-ANAL`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Column Checking perform (RC Code Check) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Perform Target · All Elements: "ALL" · By Element No.: "ELEMS" · By Section No.: "SECTIONS" | `"PERFORM_TYPE"` | string | ALL | Optional |
| 2 | [When PERFORM_TYPE = "By Element No."] Element No. | `"ELEMS"` | object | - | **Required** |
| 2.1 | └ [When PERFORM_TYPE = "By Element No."] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [When PERFORM_TYPE = "By Element No."] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [When PERFORM_TYPE = "By Section No."] Section No. | `"SECTIONS"` | array | - | **Required** |

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
      "description": "Column Checking perform (RC Code Check)",
      "additionalProperties": false,
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for design calculation. ALL: all elements, ELEMS: by element numbers, SECTIONS: by section numbers.",
          "default": "ALL",
          "enum": [
            "ALL",
            "ELEMS",
            "SECTIONS"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Give one of KEYS or TO (when both are given the product uses KEYS).",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section No. input. Required when PERFORM_TYPE is SECTIONS.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- **By Element No. (ELEMS)** — `message`
- **All Elements (ALL) / By Section No. (SECTIONS)** — `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`

### Request / Response JSON

**Request — By Element No. (ELEMS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        1059
      ]
    }
  }
}
```

**Request — All Elements (ALL)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
```

**Request — By Section No. (SECTIONS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "SECTIONS",
    "SECTIONS": [
      2
    ]
  }
}
```

**Response — By Element No. (ELEMS)**

```json
{
  "message": "success"
}
```

**Response — All Elements (ALL)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — By Section No. (SECTIONS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/CC-ANAL"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/CC-ANAL

payload = json.loads(r'''
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        1059
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 37. `CC-TABLE` — Column Checking Table

> **기능** 기둥 검토 결과를 표로 반환합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738213884953) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738327706777)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/CC-TABLE`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/CC-TABLE`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Column Checking result table (Copy Table of the result dialog) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sorted by · Member: "MEMB" · Section: "PROP" | `"TABLE_TYPE"` | string | - | **Required** |
| 2 | [General] Primary Sorting Option · SECT: 0 · MEMB: 1 | `"PRI_SORT"` | integer | 1 | Optional |
| 3 | [General] Result View Option · All: 0 · OK: 1 · NG: 2 | `"RESULT"` | integer | 0 | Optional |
| 4 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 4.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 4.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 5 | [General] Section No. | `"SECTIONS"` | array | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 8 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 8.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 8.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 8.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 8.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 9 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 9.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 9.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 10 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |

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
      "description": "Column Checking result table (Copy Table of the result dialog)",
      "additionalProperties": false,
      "required": [
        "TABLE_TYPE"
      ],
      "properties": {
        "TABLE_TYPE": {
          "type": "string",
          "description": "Sorted by: MEMB (Member) or PROP (Section)",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "PRI_SORT": {
          "type": "integer",
          "description": "Primary sorting option (Member sort): 0 = SECT, 1 = MEMB",
          "default": 1,
          "enum": [
            0,
            1
          ]
        },
        "RESULT": {
          "type": "integer",
          "description": "Result view option: All / OK / NG",
          "default": 0,
          "enum": [
            0,
            1,
            2
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section numbers. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Columns to return, by column name (exact, case-sensitive; any other name is rejected). Empty or omitted = all columns. x-enum-labels gives the dialog caption of each name.",
          "items": {
            "type": "string",
            "enum": [
              "MEMB",
              "SECT",
              "Section",
              "t",
              "Bc",
              "a",
              "Hc",
              "b",
              "fc",
              "Height",
              "fy",
              "fys",
              "CHK",
              "LCB",
              "POS",
              "Ast",
              "Rho",
              "Pr_max",
              "Pu",
              "Mc",
              "Pr",
              "Mr",
              "Rat_P",
              "Rat_M",
              "V_LCB",
              "Asvy",
              "Asvz",
              "Vu",
              "Rat_V"
            ]
          }
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response table title"
        },
        "UNIT": {
          "type": "object",
          "description": "Response unit setting. Omitted = model unit system.",
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
          "description": "Response number format",
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
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result table save path (optional)"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- **Member (MEMB)** — `Result Table` — `MEMB`, `SECT`, `Section`, `Bc`, `Hc`, `Height`, `fc`, `fy`, `CHK`, `LCB`, `POS`, `Pu`, `Pr`, `Rat_P`, `Mc`, `Mr`, `Rat_M`, `V_LCB`, `Vu`, `Rat_V`
- **Section (PROP)** — `Result Table` — `MEMB`, `SECT`, `Section`, `Bc`, `Hc`, `fc`, `Height`, `fy`, `CHK`, `LCB`, `POS`, `Pu`, `Mc`, `Pr`, `Mr`, `Rat_P`, `Rat_M`, `V_LCB`, `Vu`, `Rat_V`

### Request / Response JSON

**Request — Member (MEMB)**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        2
      ]
    },
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "Height",
      "fc",
      "fy",
      "CHK",
      "LCB",
      "POS",
      "Pu",
      "Pr",
      "Rat_P",
      "Mc",
      "Mr",
      "Rat_M",
      "V_LCB",
      "Vu",
      "Rat_V"
    ]
  }
}
```

**Request — Section (PROP)**

```json
{
  "Argument": {
    "TABLE_TYPE": "PROP",
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    },
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "Height",
      "fc",
      "fy",
      "CHK",
      "LCB",
      "POS",
      "Pu",
      "Pr",
      "Rat_P",
      "Mc",
      "Mr",
      "Rat_M",
      "V_LCB",
      "Vu",
      "Rat_V"
    ]
  }
}
```

**Response — Member (MEMB)**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "Height",
      "fc",
      "fy",
      "CHK",
      "LCB",
      "POS",
      "Pu",
      "Pr",
      "Rat_P",
      "Mc",
      "Mr",
      "Rat_M",
      "V_LCB",
      "Vu",
      "Rat_V"
    ],
    "DATA": [
      [
        "2",
        "2",
        "Column",
        "0.5000",
        "0.5000",
        "3.0000",
        "32000.0",
        "460000",
        "OK",
        "3+MY",
        "J",
        "619.122",
        "740.828",
        "0.836",
        "492.613",
        "589.449",
        "0.836",
        "5-FZ",
        "257.958",
        "0.347"
      ]
    ]
  }
}
```

**Response — Section (PROP)**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "fc",
      "Height",
      "fy",
      "CHK",
      "LCB",
      "POS",
      "Pu",
      "Mc",
      "Pr",
      "Mr",
      "Rat_P",
      "Rat_M",
      "V_LCB",
      "Vu",
      "Rat_V"
    ],
    "DATA": [
      [
        "0",
        "2",
        "C500x500",
        "0.5000",
        "0.5000",
        "27579.0",
        "3.0000",
        "413686",
        "**V",
        "1",
        "J",
        "367.972",
        "316.364",
        "605.258",
        "520.370",
        "0.608",
        "0.608",
        "1",
        "528.959",
        "1.360"
      ]
    ]
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/CC-TABLE"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/CC-TABLE

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        2
      ]
    },
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "Height",
      "fc",
      "fy",
      "CHK",
      "LCB",
      "POS",
      "Pu",
      "Pr",
      "Rat_P",
      "Mc",
      "Mr",
      "Rat_M",
      "V_LCB",
      "Vu",
      "Rat_V"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 38. `CC-REPORT` — Column Checking Report

> **기능** 기둥 검토 결과를 보고서 파일로 내보냅니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738229302169) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738275205657)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/CC-REPORT`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/CC-REPORT`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Column Checking report | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Sorted by · Member: "MEMB" · Section: "PROP" | `"REPORT_TYPE"` | string | - | **Required** |
| 2 | [General] Report Mode · Graphic: "Graphic" · Detail: "Detail" · Summary: "Summary" · Summary By LCB: "SUMMARY BY LCB" · Draw PM Curve: "PMCurve" | `"CURRENT_MODE_MEMB"` | string | - | Optional |
| 3 | [General] Report Mode · Graphic: "Graphic" · Summary: "Summary" · Draw PM Curve: "PMCurve" | `"CURRENT_MODE_PROP"` | string | - | Optional |
| 4 | [General] Report Mode (common) · Graphic: "Graphic" · Detail: "Detail" · Summary: "Summary" · Summary By LCB: "SUMMARY BY LCB" · Draw PM Curve: "PMCurve" | `"CURRENT_MODE"` | string | - | Optional |
| 5 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 5.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 5.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 6 | [General] Section No. | `"SECTIONS"` | array | - | Optional |
| 7 | [General] Export Path | `"EXPORT_PATH"` | string | - | **Required** |
| 8 | [General] Output File Name | `"OUTPUT_NAME"` | string | - | **Required** |

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
      "description": "Column Checking report",
      "additionalProperties": false,
      "required": [
        "REPORT_TYPE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "properties": {
        "REPORT_TYPE": {
          "type": "string",
          "description": "Sorted by: MEMB (Member) or PROP (Section)",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "description": "Output when sorted by member (buttons of the result dialog) Takes precedence over CURRENT_MODE.",
          "enum": [
            "Graphic",
            "Detail",
            "Summary",
            "SUMMARY BY LCB",
            "PMCurve"
          ]
        },
        "CURRENT_MODE_PROP": {
          "type": "string",
          "description": "Output when sorted by section (Detail and Summary By LCB are disabled in section order) Takes precedence over CURRENT_MODE.",
          "enum": [
            "Graphic",
            "Summary",
            "PMCurve"
          ]
        },
        "CURRENT_MODE": {
          "type": "string",
          "description": "Report kind used when the mode of the REPORT_TYPE (CURRENT_MODE_MEMB / CURRENT_MODE_PROP) is not given; matched without regard to case",
          "enum": [
            "Graphic",
            "Detail",
            "Summary",
            "SUMMARY BY LCB",
            "PMCurve"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element selection. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
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
        "SECTIONS": {
          "type": "array",
          "description": "Section numbers. Use either ELEMS or SECTIONS, not both. Omit both for all elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Directory path to save the report files"
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "File name in EXPORT_PATH. Graphic: must end with .bmp, .emf or .jpg (otherwise INVALID_EXPORT_PATH). Detail: .doc is added when missing. Summary / SUMMARY BY LCB / PMCurve: .txt is added when there is no extension. An existing file of that name is replaced",
          "minLength": 1
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SUCCESS`, `RESULT`, `CATEGORY`, `FILE_PATH`, `MESSAGE`

### Request / Response JSON

**LRFD24 Request — Member - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_24_Graphic.jpg",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD24 Request — Member - Detail**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_24_MEMB_Detail",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD24 Request — Member - Draw PM Curve**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_24_MEMB_PMCurve",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD24 Request — Member - Summary By LCB**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "SUMMARY BY LCB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_24_MEMB_SUMMARY_BY_LCB",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD24 Request — Member - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_24_MEMB_Summary",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD24 Request — Section - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_24_PROP_Graphic.jpg",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD24 Request — Section - Draw PM Curve**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_24_PROP_PMCurve",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD24 Request — Section - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_24_PROP_Summary",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD24 Response — Member - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_24_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_24_MEMB_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Draw PM Curve**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_24_MEMB_PMCurve.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Summary By LCB**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_24_MEMB_SUMMARY_BY_LCB.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Member - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_24_MEMB_Summary.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Section - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_24_PROP_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD24 Response — Section - Draw PM Curve**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_24_PROP_PMCurve.txt",
  "MESSAGE": ""
}
```

**LRFD24 Response — Section - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_24_PROP_Summary.txt",
  "MESSAGE": ""
}
```

**LRFD20 Request — Member - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_20_Graphic.jpg",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD20 Request — Member - Detail**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_20_MEMB_Detail",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD20 Request — Member - Draw PM Curve**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_20_MEMB_PMCurve",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD20 Request — Member - Summary By LCB**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "SUMMARY BY LCB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_20_MEMB_SUMMARY_BY_LCB",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD20 Request — Member - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_20_MEMB_Summary",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
```

**LRFD20 Request — Section - Graphic**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_20_PROP_Graphic.jpg",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD20 Request — Section - Draw PM Curve**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_20_PROP_PMCurve",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD20 Request — Section - Summary**

```json
{
  "Argument": {
    "REPORT_TYPE": "PROP",
    "CURRENT_MODE_PROP": "Summary",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_20_PROP_Summary",
    "SECTIONS": [
      2
    ]
  }
}
```

**LRFD20 Response — Member - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_20_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_20_MEMB_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Draw PM Curve**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_20_MEMB_PMCurve.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Summary By LCB**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_20_MEMB_SUMMARY_BY_LCB.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Member - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_20_MEMB_Summary.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Section - Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_20_PROP_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD20 Response — Section - Draw PM Curve**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_20_PROP_PMCurve.txt",
  "MESSAGE": ""
}
```

**LRFD20 Response — Section - Summary**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\CC_20_PROP_Summary.txt",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/CC-REPORT"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/CC-REPORT

# 보고서 예제의 EXPORT_PATH는 사용할 저장 경로로 바꿉니다.
payload = json.loads(r'''
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "CC_24_Graphic.jpg",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "KEYS": [
        5,
        6
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 39. `PBD-ANAL` — Plate Beam Design Perform

> **기능** 판 보 설계를 수행합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738236498585) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738288802201)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PBD-ANAL`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PBD-ANAL`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Beam Design perform (RC Code Design) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Perform Target · All Elements: "ALL" · By Element No.: "ELEMS" · By Sub-Domain No.: "SUB_DOMAINS" | `"PERFORM_TYPE"` | string | ALL | Optional |
| 2 | [When PERFORM_TYPE = "By Element No."] Element No. | `"ELEMS"` | object | - | **Required** |
| 2.1 | └ [When PERFORM_TYPE = "By Element No."] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [When PERFORM_TYPE = "By Element No."] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [When PERFORM_TYPE = "By Sub-Domain No."] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | **Required** |

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
      "description": "Plate Beam Design perform (RC Code Design)",
      "additionalProperties": false,
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for design calculation. ALL: all plate elements, ELEMS: by element numbers, SUB_DOMAINS: by sub-domain numbers.",
          "default": "ALL",
          "enum": [
            "ALL",
            "ELEMS",
            "SUB_DOMAINS"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate element selection. Give one of KEYS or TO (when both are given the product uses KEYS).",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Element numbers to perform. When both selectors are given, KEYS is used",
              "items": {
                "type": "integer",
                "minimum": 1
              }
            },
            "TO": {
              "type": "string",
              "description": "Element number range, e.g. \"1to10\""
            }
          }
        },
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`

### Request / Response JSON

**Request — By Element No. (ELEMS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "TO": "101to120"
    }
  }
}
```

**Request — All Elements (ALL)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
```

**Request — By Sub-Domain No. (SUB_DOMAINS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "SUB_DOMAINS",
    "SUB_DOMAINS": [
      1
    ]
  }
}
```

**Response — By Element No. (ELEMS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — All Elements (ALL)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — By Sub-Domain No. (SUB_DOMAINS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PBD-ANAL"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PBD-ANAL

payload = json.loads(r'''
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "TO": "101to120"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 40. `PBD-TABLE` — Plate Beam Design Table

> **기능** 판 보 설계 결과를 표로 반환합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738230566041) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738293137433)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PBD-TABLE`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PBD-TABLE`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Beam Design result table (Copy Table of the result dialog) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Result View Option · All: 0 · OK: 1 · NG: 2 | `"RESULT"` | integer | 0 | Optional |
| 2 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 2.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [General] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | Optional |
| 4 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 5 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 6 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 6.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 6.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 6.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 6.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 7 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 7.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 7.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 8 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |

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
      "description": "Plate Beam Design result table (Copy Table of the result dialog)",
      "additionalProperties": false,
      "properties": {
        "RESULT": {
          "type": "integer",
          "description": "Result view option: All / OK / NG",
          "default": 0,
          "enum": [
            0,
            1,
            2
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate elements to include. When both selectors are given, KEYS is used. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
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
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Columns to return, by column name (exact, case-sensitive; any other name is rejected). Empty or omitted = all columns. x-enum-labels gives the dialog caption of each name.",
          "items": {
            "type": "string",
            "enum": [
              "Sub-Domain_No",
              "Sub_Domain",
              "Major_Dir",
              "CHK",
              "Pos_Req_As",
              "Pos_Elem",
              "Pos_Node",
              "Pos_LCB_M",
              "Pos_Mu",
              "Pos_Mr",
              "Pos_Ratio_M",
              "Neg_Req_As",
              "Neg_Elem",
              "Neg_Node",
              "Neg_LCB_M",
              "Neg_Mu",
              "Neg_Mr",
              "Neg_Ratio_M",
              "V_Elem",
              "V_Node",
              "LCB_V",
              "Vu",
              "Vr",
              "Ratio_V",
              "As_V",
              "Stirrup"
            ]
          }
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response table title"
        },
        "UNIT": {
          "type": "object",
          "description": "Response unit setting. Omitted = model unit system.",
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
          "description": "Response number format",
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
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result table save path (optional)"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Result Table` — `Sub-Domain_No`, `Sub_Domain`, `Major_Dir`, `CHK`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    },
    "COMPONENTS": [
      "Sub-Domain_No",
      "Sub_Domain",
      "Major_Dir",
      "CHK"
    ]
  }
}
```

**Response**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Sub-Domain_No",
      "Sub_Domain",
      "Major_Dir",
      "CHK"
    ],
    "DATA": [
      [
        "1",
        "SDB",
        "Dir1",
        "OK"
      ]
    ]
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PBD-TABLE"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PBD-TABLE

payload = json.loads(r'''
{
  "Argument": {
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    },
    "COMPONENTS": [
      "Sub-Domain_No",
      "Sub_Domain",
      "Major_Dir",
      "CHK"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 41. `PBD-REPORT` — Plate Beam Design Report

> **기능** 판 보 설계 결과를 보고서 파일로 내보냅니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738228204825) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738265135641)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PBD-REPORT`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PBD-REPORT`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Beam Design report | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Report Mode · Graphic: "Graphic" · Detail: "Detail" | `"CURRENT_MODE"` | string | - | **Required** |
| 2 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 2.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [General] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | Optional |
| 4 | [General] Export Path | `"EXPORT_PATH"` | string | - | **Required** |
| 5 | [General] Output File Name | `"OUTPUT_NAME"` | string | - | **Required** |

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
      "description": "Plate Beam Design report",
      "additionalProperties": false,
      "required": [
        "CURRENT_MODE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "properties": {
        "CURRENT_MODE": {
          "type": "string",
          "description": "Output (buttons of the plate result dialog)",
          "enum": [
            "Graphic",
            "Detail"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate elements to include. When both selectors are given, KEYS is used. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
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
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Directory path to save the report files"
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "File name in EXPORT_PATH. Graphic: must end with .bmp, .emf or .jpg (otherwise INVALID_EXPORT_PATH). Detail: .doc is added when missing. Summary / SUMMARY BY LCB / PMCurve: .txt is added when there is no extension. An existing file of that name is replaced",
          "minLength": 1
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SUCCESS`, `RESULT`, `CATEGORY`, `FILE_PATH`, `MESSAGE`

### Request / Response JSON

**LRFD24 Request — Graphic**

```json
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PBD_24_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
```

**LRFD24 Request — Detail**

```json
{
  "Argument": {
    "CURRENT_MODE": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PBD_24_Detail",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
```

**LRFD24 Response — Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PBD_24_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD24 Response — Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PBD_24_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD20 Request — Graphic**

```json
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PBD_20_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
```

**LRFD20 Request — Detail**

```json
{
  "Argument": {
    "CURRENT_MODE": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PBD_20_Detail",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
```

**LRFD20 Response — Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PBD_20_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD20 Response — Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PBD_20_Detail.doc",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PBD-REPORT"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PBD-REPORT

# 보고서 예제의 EXPORT_PATH는 사용할 저장 경로로 바꿉니다.
payload = json.loads(r'''
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PBD_24_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 42. `PBC-ANAL` — Plate Beam Checking Perform

> **기능** 판 보 검토를 수행합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738229428889) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738284070809)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PBC-ANAL`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PBC-ANAL`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Beam Checking perform (RC Code Check) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Perform Target · All Elements: "ALL" · By Element No.: "ELEMS" · By Sub-Domain No.: "SUB_DOMAINS" | `"PERFORM_TYPE"` | string | ALL | Optional |
| 2 | [When PERFORM_TYPE = "By Element No."] Element No. | `"ELEMS"` | object | - | **Required** |
| 2.1 | └ [When PERFORM_TYPE = "By Element No."] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [When PERFORM_TYPE = "By Element No."] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [When PERFORM_TYPE = "By Sub-Domain No."] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | **Required** |

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
      "description": "Plate Beam Checking perform (RC Code Check)",
      "additionalProperties": false,
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for design calculation. ALL: all plate elements, ELEMS: by element numbers, SUB_DOMAINS: by sub-domain numbers.",
          "default": "ALL",
          "enum": [
            "ALL",
            "ELEMS",
            "SUB_DOMAINS"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate element selection. Give one of KEYS or TO (when both are given the product uses KEYS).",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Element numbers to perform. When both selectors are given, KEYS is used",
              "items": {
                "type": "integer",
                "minimum": 1
              }
            },
            "TO": {
              "type": "string",
              "description": "Element number range, e.g. \"1to10\""
            }
          }
        },
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`

### Request / Response JSON

**Request — By Element No. (ELEMS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "TO": "101to120"
    }
  }
}
```

**Request — All Elements (ALL)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
```

**Request — By Sub-Domain No. (SUB_DOMAINS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "SUB_DOMAINS",
    "SUB_DOMAINS": [
      1
    ]
  }
}
```

**Response — By Element No. (ELEMS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — All Elements (ALL)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — By Sub-Domain No. (SUB_DOMAINS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PBC-ANAL"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PBC-ANAL

payload = json.loads(r'''
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "TO": "101to120"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 43. `PBC-TABLE` — Plate Beam Checking Table

> **기능** 판 보 검토 결과를 표로 반환합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738240093849) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738298647833)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PBC-TABLE`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PBC-TABLE`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Beam Checking result table (Copy Table of the result dialog) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Results · Strength: "STRENGTH" · Serviceability: "SERVICEABILITY" | `"LIMIT_STATE"` | string | - | **Required** |
| 2 | [General] Result View Option · All: 0 · OK: 1 · NG: 2 | `"RESULT"` | integer | 0 | Optional |
| 3 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 3.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 3.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 4 | [General] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | Optional |
| 5 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 6 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 7 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 7.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 7.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 7.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 7.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 8 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 8.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 8.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 9 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |

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
      "description": "Plate Beam Checking result table (Copy Table of the result dialog)",
      "additionalProperties": false,
      "required": [
        "LIMIT_STATE"
      ],
      "properties": {
        "LIMIT_STATE": {
          "type": "string",
          "description": "Results view of the check dialog: Strength or Serviceability columns",
          "enum": [
            "STRENGTH",
            "SERVICEABILITY"
          ]
        },
        "RESULT": {
          "type": "integer",
          "description": "Result view option: All / OK / NG",
          "default": 0,
          "enum": [
            0,
            1,
            2
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate elements to include. When both selectors are given, KEYS is used. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
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
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Columns to return, by column name (exact, case-sensitive). Only the columns of the LIMIT_STATE view are accepted: STRENGTH = common + strength columns, SERVICEABILITY = common + serviceability columns. Empty or omitted = all columns of the view. x-enum-labels gives the dialog caption of each name.",
          "items": {
            "type": "string",
            "enum": [
              "Sub-Domain_No",
              "Sub_Domain",
              "Major_Dir",
              "CHK",
              "Pos_Use_As",
              "Pos_Elem",
              "Pos_Node",
              "Pos_LCB_M",
              "Pos_Mu",
              "Pos_Mr",
              "Pos_Ratio_M",
              "Neg_Use_As",
              "Neg_Elem",
              "Neg_Node",
              "Neg_LCB_M",
              "Neg_Mu",
              "Neg_Mr",
              "Neg_Ratio_M",
              "V_Elem",
              "V_Node",
              "LCB_V",
              "Vu",
              "Vr",
              "Ratio_V",
              "Top_Elem",
              "Top_Node",
              "Top_LCB",
              "Top_S",
              "Top_Sa",
              "Bot_Elem",
              "Bot_Node",
              "Bot_LCB",
              "Bot_S",
              "Bot_Sa"
            ]
          }
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response table title"
        },
        "UNIT": {
          "type": "object",
          "description": "Response unit setting. Omitted = model unit system.",
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
          "description": "Response number format",
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
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result table save path (optional)"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- **Serviceability (SERVICEABILITY)** — `Result Table` — `Sub-Domain_No`, `CHK`, `Top_S`
- **Strength (STRENGTH)** — `Result Table` — `Sub-Domain_No`, `Sub_Domain`, `Major_Dir`, `CHK`, `Pos_Use_As`, `Pos_Elem`, `Pos_Node`, `Pos_LCB_M`, `Pos_Mu`, `Pos_Mr`, `Pos_Ratio_M`, `Neg_Use_As`, `Neg_Elem`, `Neg_Node`, `Neg_LCB_M`, `Neg_Mu`, `Neg_Mr`, `Neg_Ratio_M`, `V_Elem`, `V_Node`, `LCB_V`, `Vu`, `Vr`, `Ratio_V`

### Request / Response JSON

**Request — Serviceability (SERVICEABILITY)**

```json
{
  "Argument": {
    "LIMIT_STATE": "SERVICEABILITY",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    },
    "COMPONENTS": [
      "Sub-Domain_No",
      "CHK",
      "Top_S"
    ]
  }
}
```

**Request — Strength (STRENGTH)**

```json
{
  "Argument": {
    "LIMIT_STATE": "STRENGTH",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
```

**Response — Serviceability (SERVICEABILITY)**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Sub-Domain_No",
      "CHK",
      "Top_S"
    ],
    "DATA": [
      [
        "1",
        "OK*",
        "0.2000"
      ]
    ]
  }
}
```

**Response — Strength (STRENGTH)**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Sub-Domain_No",
      "Sub_Domain",
      "Major_Dir",
      "CHK",
      "Pos_Use_As",
      "Pos_Elem",
      "Pos_Node",
      "Pos_LCB_M",
      "Pos_Mu",
      "Pos_Mr",
      "Pos_Ratio_M",
      "Neg_Use_As",
      "Neg_Elem",
      "Neg_Node",
      "Neg_LCB_M",
      "Neg_Mu",
      "Neg_Mr",
      "Neg_Ratio_M",
      "V_Elem",
      "V_Node",
      "LCB_V",
      "Vu",
      "Vr",
      "Ratio_V"
    ],
    "DATA": [
      [
        "1",
        "SDB",
        "Dir1",
        "OK",
        "0.0019",
        "9",
        "14",
        "2",
        "0.00000",
        "153.338",
        "0.0000",
        "0.0010",
        "8",
        "13",
        "1",
        "63.7335",
        "89.7941",
        "0.7098",
        "8",
        "13",
        "1",
        "34.5023",
        "408.883",
        "0.0844"
      ]
    ]
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PBC-TABLE"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PBC-TABLE

payload = json.loads(r'''
{
  "Argument": {
    "LIMIT_STATE": "SERVICEABILITY",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    },
    "COMPONENTS": [
      "Sub-Domain_No",
      "CHK",
      "Top_S"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 44. `PBC-REPORT` — Plate Beam Checking Report

> **기능** 판 보 검토 결과를 보고서 파일로 내보냅니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738209117081) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738275892761)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PBC-REPORT`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PBC-REPORT`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Beam Checking report | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Report Mode · Graphic: "Graphic" · Detail: "Detail" | `"CURRENT_MODE"` | string | - | **Required** |
| 2 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 2.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [General] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | Optional |
| 4 | [General] Export Path | `"EXPORT_PATH"` | string | - | **Required** |
| 5 | [General] Output File Name | `"OUTPUT_NAME"` | string | - | **Required** |

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
      "description": "Plate Beam Checking report",
      "additionalProperties": false,
      "required": [
        "CURRENT_MODE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "properties": {
        "CURRENT_MODE": {
          "type": "string",
          "description": "Output (buttons of the plate result dialog)",
          "enum": [
            "Graphic",
            "Detail"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate elements to include. When both selectors are given, KEYS is used. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
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
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Directory path to save the report files"
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "File name in EXPORT_PATH. Graphic: must end with .bmp, .emf or .jpg (otherwise INVALID_EXPORT_PATH). Detail: .doc is added when missing. Summary / SUMMARY BY LCB / PMCurve: .txt is added when there is no extension. An existing file of that name is replaced",
          "minLength": 1
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SUCCESS`, `RESULT`, `CATEGORY`, `FILE_PATH`, `MESSAGE`

### Request / Response JSON

**LRFD24 Request — Graphic**

```json
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PBC_24_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
```

**LRFD24 Request — Detail**

```json
{
  "Argument": {
    "CURRENT_MODE": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PBC_24_Detail",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
```

**LRFD24 Response — Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PBC_24_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD24 Response — Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PBC_24_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD20 Request — Graphic**

```json
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PBC_20_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
```

**LRFD20 Request — Detail**

```json
{
  "Argument": {
    "CURRENT_MODE": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PBC_20_Detail",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
```

**LRFD20 Response — Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PBC_20_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD20 Response — Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PBC_20_Detail.doc",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PBC-REPORT"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PBC-REPORT

# 보고서 예제의 EXPORT_PATH는 사용할 저장 경로로 바꿉니다.
payload = json.loads(r'''
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PBC_24_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        8,
        9
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 45. `PCD-ANAL` — Plate Column Design Perform

> **기능** 판 기둥 설계를 수행합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738236921881) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738303295641)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PCD-ANAL`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PCD-ANAL`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Column Design perform (RC Code Design) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Perform Target · All Elements: "ALL" · By Element No.: "ELEMS" · By Sub-Domain No.: "SUB_DOMAINS" | `"PERFORM_TYPE"` | string | ALL | Optional |
| 2 | [When PERFORM_TYPE = "By Element No."] Element No. | `"ELEMS"` | object | - | **Required** |
| 2.1 | └ [When PERFORM_TYPE = "By Element No."] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [When PERFORM_TYPE = "By Element No."] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [When PERFORM_TYPE = "By Sub-Domain No."] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | **Required** |

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
      "description": "Plate Column Design perform (RC Code Design)",
      "additionalProperties": false,
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for design calculation. ALL: all plate elements, ELEMS: by element numbers, SUB_DOMAINS: by sub-domain numbers.",
          "default": "ALL",
          "enum": [
            "ALL",
            "ELEMS",
            "SUB_DOMAINS"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate element selection. Give one of KEYS or TO (when both are given the product uses KEYS).",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Element numbers to perform. When both selectors are given, KEYS is used",
              "items": {
                "type": "integer",
                "minimum": 1
              }
            },
            "TO": {
              "type": "string",
              "description": "Element number range, e.g. \"1to10\""
            }
          }
        },
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`

### Request / Response JSON

**Request — By Element No. (ELEMS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        10,
        11,
        12
      ]
    }
  }
}
```

**Request — All Elements (ALL)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
```

**Request — By Sub-Domain No. (SUB_DOMAINS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "SUB_DOMAINS",
    "SUB_DOMAINS": [
      2
    ]
  }
}
```

**Response — By Element No. (ELEMS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — All Elements (ALL)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — By Sub-Domain No. (SUB_DOMAINS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PCD-ANAL"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PCD-ANAL

payload = json.loads(r'''
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        10,
        11,
        12
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 46. `PCD-TABLE` — Plate Column Design Table

> **기능** 판 기둥 설계 결과를 표로 반환합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738230818969) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738336880153)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PCD-TABLE`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PCD-TABLE`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Column Design result table (Copy Table of the result dialog) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Result View Option · All: 0 · OK: 1 · NG: 2 | `"RESULT"` | integer | 0 | Optional |
| 2 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 2.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [General] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | Optional |
| 4 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 5 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 6 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 6.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 6.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 6.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 6.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 7 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 7.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 7.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 8 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |

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
      "description": "Plate Column Design result table (Copy Table of the result dialog)",
      "additionalProperties": false,
      "properties": {
        "RESULT": {
          "type": "integer",
          "description": "Result view option: All / OK / NG",
          "default": 0,
          "enum": [
            0,
            1,
            2
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate elements to include. When both selectors are given, KEYS is used. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
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
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Columns to return, by column name (exact, case-sensitive; any other name is rejected). Empty or omitted = all columns. x-enum-labels gives the dialog caption of each name.",
          "items": {
            "type": "string",
            "enum": [
              "Sub-Domain_No",
              "Sub_Domain",
              "Major_Dir",
              "CHK",
              "Pos_Req_As",
              "Pos_Elem",
              "Pos_Node",
              "Pos_LCB_M",
              "Pos_Mu",
              "Pos_Mr",
              "Pos_Pu",
              "Pos_Pr",
              "Pos_Ratio_M",
              "Neg_Req_As",
              "Neg_Elem",
              "Neg_Node",
              "Neg_LCB_M",
              "Neg_Mu",
              "Neg_Mr",
              "Neg_Pu",
              "Neg_Pr",
              "Neg_Ratio_M",
              "V_Elem",
              "V_Node",
              "LCB_V",
              "Vu",
              "Vr",
              "Ratio_V",
              "As_V",
              "Stirrup"
            ]
          }
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response table title"
        },
        "UNIT": {
          "type": "object",
          "description": "Response unit setting. Omitted = model unit system.",
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
          "description": "Response number format",
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
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result table save path (optional)"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Result Table` — `Sub-Domain_No`, `Sub_Domain`, `Major_Dir`, `CHK`, `Pos_Req_As`, `Pos_Elem`, `Pos_Node`, `Pos_LCB_M`, `Pos_Mu`, `Pos_Mr`, `Pos_Pu`, `Pos_Pr`, `Pos_Ratio_M`, `Neg_Req_As`, `Neg_Elem`, `Neg_Node`, `Neg_LCB_M`, `Neg_Mu`, `Neg_Mr`, `Neg_Pu`, `Neg_Pr`, `Neg_Ratio_M`, `V_Elem`, `V_Node`, `LCB_V`, `Vu`, `Vr`, `Ratio_V`, `As_V`, `Stirrup`

### Request / Response JSON

두 판의 요청과 `HEAD` 열은 같습니다. 공식 응답 예제의 레코드와 수치가 달라 두 응답을 함께 싣습니다.

**Request**

```json
{
  "Argument": {
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
```

**LRFD24 Response**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Sub-Domain_No",
      "Sub_Domain",
      "Major_Dir",
      "CHK",
      "Pos_Req_As",
      "Pos_Elem",
      "Pos_Node",
      "Pos_LCB_M",
      "Pos_Mu",
      "Pos_Mr",
      "Pos_Pu",
      "Pos_Pr",
      "Pos_Ratio_M",
      "Neg_Req_As",
      "Neg_Elem",
      "Neg_Node",
      "Neg_LCB_M",
      "Neg_Mu",
      "Neg_Mr",
      "Neg_Pu",
      "Neg_Pr",
      "Neg_Ratio_M",
      "V_Elem",
      "V_Node",
      "LCB_V",
      "Vu",
      "Vr",
      "Ratio_V",
      "As_V",
      "Stirrup"
    ],
    "DATA": [
      [
        "2",
        "SDC",
        "Dir1",
        "OK",
        "0.0000",
        "10",
        "16",
        "2",
        "0.00000",
        "0.00000",
        "0.00000",
        "4529.69",
        "0.0000",
        "0.0000",
        "10",
        "13",
        "2",
        "45.8882",
        "66.5227",
        "0.00000",
        "0.00000",
        "0.6898",
        "10",
        "14",
        "1",
        "34.5023",
        "599.247",
        "0.0576",
        "0.0521",
        "2-#4@0.1951"
      ]
    ]
  }
}
```

**LRFD20 Response**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Sub-Domain_No",
      "Sub_Domain",
      "Major_Dir",
      "CHK",
      "Pos_Req_As",
      "Pos_Elem",
      "Pos_Node",
      "Pos_LCB_M",
      "Pos_Mu",
      "Pos_Mr",
      "Pos_Pu",
      "Pos_Pr",
      "Pos_Ratio_M",
      "Neg_Req_As",
      "Neg_Elem",
      "Neg_Node",
      "Neg_LCB_M",
      "Neg_Mu",
      "Neg_Mr",
      "Neg_Pu",
      "Neg_Pr",
      "Neg_Ratio_M",
      "V_Elem",
      "V_Node",
      "LCB_V",
      "Vu",
      "Vr",
      "Ratio_V",
      "As_V",
      "Stirrup"
    ],
    "DATA": [
      [
        "2",
        "SDC",
        "Dir1",
        "OK",
        "0.0000",
        "10",
        "16",
        "1",
        "0.00000",
        "0.00000",
        "0.00000",
        "4529.69",
        "0.0000",
        "0.0000",
        "10",
        "13",
        "1",
        "63.7335",
        "66.5227",
        "0.00000",
        "0.00000",
        "0.9581",
        "10",
        "14",
        "1",
        "34.5023",
        "599.247",
        "0.0576",
        "0.0521",
        "2-#4@0.1951"
      ]
    ]
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PCD-TABLE"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PCD-TABLE

payload = json.loads(r'''
{
  "Argument": {
    "RESULT": 0,
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 47. `PCD-REPORT` — Plate Column Design Report

> **기능** 판 기둥 설계 결과를 보고서 파일로 내보냅니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738228543385) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738265747993)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PCD-REPORT`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PCD-REPORT`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Column Design report | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Report Mode · Graphic: "Graphic" · Detail: "Detail" | `"CURRENT_MODE"` | string | - | **Required** |
| 2 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 2.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [General] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | Optional |
| 4 | [General] Export Path | `"EXPORT_PATH"` | string | - | **Required** |
| 5 | [General] Output File Name | `"OUTPUT_NAME"` | string | - | **Required** |

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
      "description": "Plate Column Design report",
      "additionalProperties": false,
      "required": [
        "CURRENT_MODE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "properties": {
        "CURRENT_MODE": {
          "type": "string",
          "description": "Output (buttons of the plate result dialog)",
          "enum": [
            "Graphic",
            "Detail"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate elements to include. When both selectors are given, KEYS is used. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
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
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Directory path to save the report files"
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "File name in EXPORT_PATH. Graphic: must end with .bmp, .emf or .jpg (otherwise INVALID_EXPORT_PATH). Detail: .doc is added when missing. Summary / SUMMARY BY LCB / PMCurve: .txt is added when there is no extension. An existing file of that name is replaced",
          "minLength": 1
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SUCCESS`, `RESULT`, `CATEGORY`, `FILE_PATH`, `MESSAGE`

### Request / Response JSON

**LRFD24 Request — Graphic**

```json
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PCD_24_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
```

**LRFD24 Request — Detail**

```json
{
  "Argument": {
    "CURRENT_MODE": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PCD_24_Detail",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
```

**LRFD24 Response — Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PCD_24_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD24 Response — Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PCD_24_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD20 Request — Graphic**

```json
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PCD_20_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
```

**LRFD20 Request — Detail**

```json
{
  "Argument": {
    "CURRENT_MODE": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PCD_20_Detail",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
```

**LRFD20 Response — Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PCD_20_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD20 Response — Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PCD_20_Detail.doc",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PCD-REPORT"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PCD-REPORT

# 보고서 예제의 EXPORT_PATH는 사용할 저장 경로로 바꿉니다.
payload = json.loads(r'''
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PCD_24_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 48. `PCC-ANAL` — Plate Column Checking Perform

> **기능** 판 기둥 검토를 수행합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738229803801) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738291830681)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PCC-ANAL`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PCC-ANAL`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Column Checking perform (RC Code Check) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Perform Target · All Elements: "ALL" · By Element No.: "ELEMS" · By Sub-Domain No.: "SUB_DOMAINS" | `"PERFORM_TYPE"` | string | ALL | Optional |
| 2 | [When PERFORM_TYPE = "By Element No."] Element No. | `"ELEMS"` | object | - | **Required** |
| 2.1 | └ [When PERFORM_TYPE = "By Element No."] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [When PERFORM_TYPE = "By Element No."] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [When PERFORM_TYPE = "By Sub-Domain No."] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | **Required** |

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
      "description": "Plate Column Checking perform (RC Code Check)",
      "additionalProperties": false,
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for design calculation. ALL: all plate elements, ELEMS: by element numbers, SUB_DOMAINS: by sub-domain numbers.",
          "default": "ALL",
          "enum": [
            "ALL",
            "ELEMS",
            "SUB_DOMAINS"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate element selection. Give one of KEYS or TO (when both are given the product uses KEYS).",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Element numbers to perform. When both selectors are given, KEYS is used",
              "items": {
                "type": "integer",
                "minimum": 1
              }
            },
            "TO": {
              "type": "string",
              "description": "Element number range, e.g. \"1to10\""
            }
          }
        },
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`

### Request / Response JSON

**Request — By Element No. (ELEMS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        10,
        11,
        12
      ]
    }
  }
}
```

**Request — All Elements (ALL)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
```

**Request — By Sub-Domain No. (SUB_DOMAINS)**

```json
{
  "Argument": {
    "PERFORM_TYPE": "SUB_DOMAINS",
    "SUB_DOMAINS": [
      2
    ]
  }
}
```

**Response — By Element No. (ELEMS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — All Elements (ALL)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

**Response — By Sub-Domain No. (SUB_DOMAINS)**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PCC-ANAL"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PCC-ANAL

payload = json.loads(r'''
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [
        10,
        11,
        12
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 49. `PCC-TABLE` — Plate Column Checking Table

> **기능** 판 기둥 검토 결과를 표로 반환합니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738240305945) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738313020697)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PCC-TABLE`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PCC-TABLE`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Column Checking result table (Copy Table of the result dialog) | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Results · Strength: "STRENGTH" · Serviceability: "SERVICEABILITY" | `"LIMIT_STATE"` | string | - | **Required** |
| 2 | [General] Result View Option · All: 0 · OK: 1 · NG: 2 | `"RESULT"` | integer | 0 | Optional |
| 3 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 3.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 3.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 4 | [General] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | Optional |
| 5 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 6 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 7 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 7.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 7.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 7.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 7.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 8 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 8.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 8.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 9 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |

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
      "description": "Plate Column Checking result table (Copy Table of the result dialog)",
      "additionalProperties": false,
      "required": [
        "LIMIT_STATE"
      ],
      "properties": {
        "LIMIT_STATE": {
          "type": "string",
          "description": "Results view of the check dialog: Strength or Serviceability columns",
          "enum": [
            "STRENGTH",
            "SERVICEABILITY"
          ]
        },
        "RESULT": {
          "type": "integer",
          "description": "Result view option: All / OK / NG",
          "default": 0,
          "enum": [
            0,
            1,
            2
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate elements to include. When both selectors are given, KEYS is used. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
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
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Columns to return, by column name (exact, case-sensitive). Only the columns of the LIMIT_STATE view are accepted: STRENGTH = common + strength columns, SERVICEABILITY = common + serviceability columns. Empty or omitted = all columns of the view. x-enum-labels gives the dialog caption of each name.",
          "items": {
            "type": "string",
            "enum": [
              "Sub-Domain_No",
              "Sub_Domain",
              "Major_Dir",
              "CHK",
              "Pos_Use_As",
              "Pos_Elem",
              "Pos_Node",
              "Pos_LCB_M",
              "Pos_Mu",
              "Pos_Mr",
              "Pos_Pu",
              "Pos_Pr",
              "Pos_Ratio_M",
              "Neg_Use_As",
              "Neg_Elem",
              "Neg_Node",
              "Neg_LCB_M",
              "Neg_Mu",
              "Neg_Mr",
              "Neg_Pu",
              "Neg_Pr",
              "Neg_Ratio_M",
              "P_Elem",
              "P_Node",
              "LCB_P",
              "Pu",
              "Pr",
              "Ratio_P",
              "V_Elem",
              "V_Node",
              "LCB_V",
              "Vu",
              "Vr",
              "Ratio_V",
              "Top_Elem",
              "Top_Node",
              "Top_LCB",
              "Top_S",
              "Top_Sa",
              "Bot_Elem",
              "Bot_Node",
              "Bot_LCB",
              "Bot_S",
              "Bot_Sa"
            ]
          }
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response table title"
        },
        "UNIT": {
          "type": "object",
          "description": "Response unit setting. Omitted = model unit system.",
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
          "description": "Response number format",
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
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result table save path (optional)"
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- **Serviceability (SERVICEABILITY)** — `Result Table` — `Sub-Domain_No`, `CHK`, `Top_S`
- **Strength (STRENGTH)** — `Result Table` — `Sub-Domain_No`, `Sub_Domain`, `Major_Dir`, `CHK`, `Pos_Use_As`, `Pos_Elem`, `Pos_Node`, `Pos_LCB_M`, `Pos_Mu`, `Pos_Mr`, `Pos_Pu`, `Pos_Pr`, `Pos_Ratio_M`, `Neg_Use_As`, `Neg_Elem`, `Neg_Node`, `Neg_LCB_M`, `Neg_Mu`, `Neg_Mr`, `Neg_Pu`, `Neg_Pr`, `Neg_Ratio_M`, `P_Elem`, `P_Node`, `LCB_P`, `Pu`, `Pr`, `Ratio_P`, `V_Elem`, `V_Node`, `LCB_V`, `Vu`, `Vr`, `Ratio_V`

### Request / Response JSON

**Request — Serviceability (SERVICEABILITY)**

```json
{
  "Argument": {
    "LIMIT_STATE": "SERVICEABILITY",
    "ELEMS": {
      "KEYS": [
        10
      ]
    },
    "COMPONENTS": [
      "Sub-Domain_No",
      "CHK",
      "Top_S"
    ]
  }
}
```

**Request — Strength (STRENGTH)**

```json
{
  "Argument": {
    "LIMIT_STATE": "STRENGTH",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
```

**Response — Serviceability (SERVICEABILITY)**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Sub-Domain_No",
      "CHK",
      "Top_S"
    ],
    "DATA": [
      [
        "2",
        "OK*",
        "0.2000"
      ]
    ]
  }
}
```

**Response — Strength (STRENGTH)**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Sub-Domain_No",
      "Sub_Domain",
      "Major_Dir",
      "CHK",
      "Pos_Use_As",
      "Pos_Elem",
      "Pos_Node",
      "Pos_LCB_M",
      "Pos_Mu",
      "Pos_Mr",
      "Pos_Pu",
      "Pos_Pr",
      "Pos_Ratio_M",
      "Neg_Use_As",
      "Neg_Elem",
      "Neg_Node",
      "Neg_LCB_M",
      "Neg_Mu",
      "Neg_Mr",
      "Neg_Pu",
      "Neg_Pr",
      "Neg_Ratio_M",
      "P_Elem",
      "P_Node",
      "LCB_P",
      "Pu",
      "Pr",
      "Ratio_P",
      "V_Elem",
      "V_Node",
      "LCB_V",
      "Vu",
      "Vr",
      "Ratio_V"
    ],
    "DATA": [
      [
        "2",
        "SDC",
        "Dir1",
        "OK",
        "0.0014",
        "10",
        "16",
        "2",
        "0.00000",
        "0.00000",
        "0.00000",
        "4884.26",
        "0.0000",
        "0.0014",
        "10",
        "13",
        "2",
        "45.8882",
        "129.132",
        "0.00000",
        "0.00000",
        "0.3554",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "10",
        "13",
        "1",
        "34.5023",
        "186.215",
        "0.1853"
      ]
    ]
  }
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PCC-TABLE"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PCC-TABLE

payload = json.loads(r'''
{
  "Argument": {
    "LIMIT_STATE": "SERVICEABILITY",
    "ELEMS": {
      "KEYS": [
        10
      ]
    },
    "COMPONENTS": [
      "Sub-Domain_No",
      "CHK",
      "Top_S"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 50. `PCC-REPORT` — Plate Column Checking Report

> **기능** 판 기둥 검토 결과를 보고서 파일로 내보냅니다.

**원문** [LRFD24](https://support.midasuser.com/hc/en-us/articles/64738199945625) · [LRFD20](https://support.midasuser.com/hc/en-us/articles/64738276563225)

### Input URI

- **LRFD24** `{base url}/DESIGN/RC/AASHTO-LRFD24/PCC-REPORT`
- **LRFD20** `{base url}/DESIGN/RC/AASHTO-LRFD20/PCC-REPORT`

### Active Methods

`POST`

### Specifications

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Plate Column Checking report | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Report Mode · Graphic: "Graphic" · Detail: "Detail" | `"CURRENT_MODE"` | string | - | **Required** |
| 2 | [General] Element No. | `"ELEMS"` | object | - | Optional |
| 2.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 2.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 3 | [General] Sub-Domain No. | `"SUB_DOMAINS"` | array | - | Optional |
| 4 | [General] Export Path | `"EXPORT_PATH"` | string | - | **Required** |
| 5 | [General] Output File Name | `"OUTPUT_NAME"` | string | - | **Required** |

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
      "description": "Plate Column Checking report",
      "additionalProperties": false,
      "required": [
        "CURRENT_MODE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "properties": {
        "CURRENT_MODE": {
          "type": "string",
          "description": "Output (buttons of the plate result dialog)",
          "enum": [
            "Graphic",
            "Detail"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Plate elements to include. When both selectors are given, KEYS is used. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
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
        "SUB_DOMAINS": {
          "type": "array",
          "description": "Sub-domain numbers (keys of /DB/SBDO). The plate elements of these sub-domains are selected. Use either ELEMS or SUB_DOMAINS, not both. Omit both for all plate elements.",
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Directory path to save the report files"
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "File name in EXPORT_PATH. Graphic: must end with .bmp, .emf or .jpg (otherwise INVALID_EXPORT_PATH). Detail: .doc is added when missing. Summary / SUMMARY BY LCB / PMCurve: .txt is added when there is no extension. An existing file of that name is replaced",
          "minLength": 1
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `SUCCESS`, `RESULT`, `CATEGORY`, `FILE_PATH`, `MESSAGE`

### Request / Response JSON

**LRFD24 Request — Graphic**

```json
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PCC_24_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
```

**LRFD24 Request — Detail**

```json
{
  "Argument": {
    "CURRENT_MODE": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PCC_24_Detail",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
```

**LRFD24 Response — Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PCC_24_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD24 Response — Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PCC_24_Detail.doc",
  "MESSAGE": ""
}
```

**LRFD20 Request — Graphic**

```json
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PCC_20_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
```

**LRFD20 Request — Detail**

```json
{
  "Argument": {
    "CURRENT_MODE": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PCC_20_Detail",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
```

**LRFD20 Response — Graphic**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PCC_20_Graphic.jpg",
  "MESSAGE": ""
}
```

**LRFD20 Response — Detail**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PCC_20_Detail.doc",
  "MESSAGE": ""
}
```

### Python 예제

호출할 설계기준과 일치하는 URI를 선택한 뒤, 위 공식 요청 예제의 JSON을 사용합니다.

```python
import json

import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/AASHTO-LRFD24/PCC-REPORT"
# LRFD20 URI: {base url}/DESIGN/RC/AASHTO-LRFD20/PCC-REPORT

# 보고서 예제의 EXPORT_PATH는 사용할 저장 경로로 바꿉니다.
payload = json.loads(r'''
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PCC_24_Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        10
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```
