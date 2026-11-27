# 29. Design Code – PSC AASHTO-LRFD24 (교량 프리스트레스트 콘크리트 설계)

> **예제 Base URL (MIDAS Civil NX)** `https://moa-engineers.midasit.com:443/civil`  
> **인증 헤더** `MAPI-Key: <발급된 키>`  
> **공식 하위 목차** [AASHTO-LRFD24 PSC](https://support.midasuser.com/hc/en-us/articles/64738410396953)

교량 프리스트레스트 콘크리트(PSC) 설계 설정, 설계 수행, 결과 표 및 Excel 보고서를 다룹니다.
공통 URI 접두사는 `{base url}/DESIGN/PSC/AASHTO-LRFD24/<CODE>`입니다.
고유 URI **19개**를 다룹니다. 결과 표는 `TABLE_TYPE`으로 구분하며, 전체 목록은 **29개 절**입니다.
영문 엔드포인트 글 30건과 이전 한국어 글 10건의 표와 Schema를 출처별로 제공합니다. 별도의 재료 부속 글 두 건은 `MATD` 절에 포함했습니다.

---

## Endpoint 목록 (29개 절)

| No. | Endpoint | 기능 | Active Methods |
| --- | --- | --- | --- |
| 0 | [`DSPSC`](#0-dspsc--design-code) | 프로젝트에서 사용할 PSC 설계 기준을 선택합니다. | GET · PUT · DELETE |
| 1 | [`DPSC`](#1-dpsc--design-code-option) | PSC 설계 기준과 긴장재, 균열 검토, 휨·전단 설계 옵션을 설정합니다. | GET · PUT · DELETE |
| 2 | [`MEMB`](#2-memb--psc-segment-assignment) | PSC 설계용 부재에 요소를 배정합니다. | POST · GET · PUT · DELETE |
| 3 | [`SLCT`](#3-slct--serviceability-load-combination-type) | PSC 설계의 사용성 하중조합 유형을 설정합니다. | GET · PUT · DELETE |
| 4 | [`INFS`](#4-infs--interface-shear) | 접합면 전단 검토에 사용할 조건을 입력합니다. | POST · GET · PUT · DELETE |
| 5 | [`MATD`](#5-matd--modify-material) | PSC 설계용 거더·슬래브의 콘크리트 및 철근 재료를 수정합니다. | GET · PUT · DELETE |
| 6 | [`RPSC`](#6-rpsc--longitudinal-rebar-reinforcements) | 종방향 철근 보강 정보를 입력합니다. | POST · GET · PUT · DELETE |
| 7 | [`SECF`](#7-secf--longitudinal-rebar-stiffness) | 종방향 철근의 강성 산정 정보를 입력합니다. | POST · GET · PUT · DELETE |
| 8 | [`STRPSSM`](#8-strpssm--longitudinal-rebar-stress-points) | 종방향 철근의 응력 산정 위치를 입력합니다. | POST · GET · DELETE · PUT |
| 9 | [`DIDP`](#9-didp--design-position) | PSC 설계를 수행할 위치를 지정합니다. | POST · GET · PUT · DELETE |
| 10 | [`DIOP`](#10-diop--output-position) | PSC 설계 결과의 출력 위치를 지정합니다. | POST · GET · PUT · DELETE |
| 11 | [`PSC-ANAL`](#11-psc-anal--perform-design) | PSC 설계를 수행합니다. | POST |
| 12 | [`TABLE` · `PSC_DGN_FORCE`](#12-table--psc_dgn_force--design-forces) | PSC 설계에 사용한 부재력을 조회합니다. | POST |
| 13 | [`TABLE` · `PSC_STRESS_CS`, `PSC_STRESS_CS_VBEAM`](#13-table--psc_stress_cs--check-stress-for-cross-section-at-a-construction-stage) | 시공단계별 단면의 응력 검토 결과를 조회합니다. | POST · GET · DELETE · PUT |
| 14 | [`TABLE` · `PSC_STRESS_TENDON`](#14-table--psc_stress_tendon--check-tensile-stress-for-prestressing-tendons) | 프리스트레싱 긴장재의 인장응력 검토 결과를 조회합니다. | POST |
| 15 | [`TABLE` · `PSC_STRESS_SERVICE`, `PSC_STRESS_SERVICE_VBEAM`](#15-table--psc_stress_service--check-stress-for-cross-section-at-service-loads) | 사용하중에 대한 단면 응력 검토 결과를 조회합니다. | POST |
| 16 | [`TABLE` · `PSC_PRINCIPAL_CS`, `PSC_PRINCIPAL_CS_VBEAM`](#16-table--psc_principal_cs--principal-stress-at-a-construction-stage) | 시공단계별 단면의 주응력 결과를 조회합니다. | POST |
| 17 | [`TABLE` · `PSC_PRINCIPAL_SVC_E`, `PSC_PRINCIPAL_SVC_E_VBEAM`](#17-table--psc_principal_svc_e--principal-stress-at-service-loads-excluding-torsional-shear-stress) | 비틀림 전단응력을 제외한 사용하중 주응력 결과를 조회합니다. | POST |
| 18 | [`TABLE` · `PSC_PRINCIPAL_SVC`, `PSC_PRINCIPAL_SVC_VBEAM`](#18-table--psc_principal_svc--principal-stress-at-service-loads) | 사용하중에 대한 주응력 결과를 조회합니다. | POST |
| 19 | [`TABLE` · `PSC_CRACK_WIDTH`, `PSC_CRACK_WIDTH_VBEAM`](#19-table--psc_crack_width--check-crack-width-at-service-loads) | 사용하중에 대한 균열폭 검토 결과를 조회합니다. | POST |
| 20 | [`TABLE` · `PSC_FLEXURE`, `PSC_FLEXURE_VBEAM`](#20-table--psc_flexure--check-flexure-strength) | 휨강도 검토 결과를 조회합니다. | POST |
| 21 | [`TABLE` · `PSC_SHEAR`, `PSC_SHEAR_VBEAM`](#21-table--psc_shear--check-shear-strength) | 전단강도 검토 결과를 조회합니다. | POST |
| 22 | [`TABLE` · `PSC_SHEAR_TORSION`, `PSC_SHEAR_TORSION_VBEAM`](#22-table--psc_shear_torsion--check-combined-shear-and-torsion-strength) | 전단과 비틀림의 조합 강도 검토 결과를 조회합니다. | POST |
| 23 | [`REPORT`](#23-report--excel-report) | PSC 설계 결과를 Excel 보고서로 내보냅니다. | POST |
| 24 | [`MEMB-VBEAM`](#24-memb-vbeam--psc-segment-assignment---virtual-beam) | PSC 설계용 가상보를 부재로 배정합니다. | POST · GET · PUT · DELETE |
| 25 | [`INFS-VBEAM`](#25-infs-vbeam--interface-shear---virtual-beam) | 가상보의 접합면 전단 검토 조건을 입력합니다. | POST · GET · PUT · DELETE |
| 26 | [`RPSC-VBEAM`](#26-rpsc-vbeam--longitudinal-rebar-reinforcements---virtual-beam) | 가상보의 종방향 철근 보강 정보를 입력합니다. | POST · GET · PUT · DELETE |
| 27 | [`DIDP-VBEAM`](#27-didp-vbeam--design-position---virtual-beam) | 가상보의 PSC 설계 위치를 지정합니다. | POST · GET · PUT · DELETE |
| 28 | [`DIOP-VBEAM`](#28-diop-vbeam--output-position---virtual-beam) | 가상보의 PSC 설계 결과 출력 위치를 지정합니다. | POST · GET · PUT · DELETE |

---

## 0. `DSPSC` — Design Code

> **기능** 프로젝트에서 사용할 PSC 설계 기준을 선택합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/DSPSC
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 57945465173145](https://support.midasuser.com/hc/en-us/articles/57945465173145)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] PSC Design Code · AASHTO-LRFD24: "AASHTO-LRFD24" | `"DGNCODE"` | string | - | **Required** |

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
        "^1$": {
          "type": "object",
          "required": [
            "DGNCODE"
          ],
          "additionalProperties": false,
          "properties": {
            "DGNCODE": {
              "type": "string",
              "description": "PSC Design Code",
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

- `DSPSC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "AASHTO-LRFD24"
    }
  }
}
```

**Response**

```json
{
  "DSPSC": {
    "1": {
      "DGNCODE": "AASHTO-LRFD24"
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/DSPSC"

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

### 이전 한국어 원문

**원문** [한국어 57945478412697](https://support.midasuser.com/hc/ko/articles/57945478412697)

**원문 Active Methods** `POST` · `GET` · `PUT` · `DELETE`

> ⚠️ 메서드는 영문 글에서 GET · PUT · DELETE, 이 글에서 POST · GET · PUT · DELETE입니다. 영문 Schema의 Assign은 ID "1"을 쓰고 이 글은 숫자로 된 ID를 허용하는 패턴을 제시합니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] PSC Design Code · AASHTO-LRFD24: "AASHTO-LRFD24" | `"DGNCODE"` | string | - | **Required** |

**JSON Schema**

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
              "description": "PSC Design Code",
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


---

## 1. `DPSC` — Design Code Option

> **기능** PSC 설계 기준과 긴장재, 균열 검토, 휨·전단 설계 옵션을 설정합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/DPSC
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 57945497373465](https://support.midasuser.com/hc/en-us/articles/57945497373465)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] PSC Design Code · AASHTO-LRFD24 | `"DGNCODE"` | string | - | **Required** |
| 2 | [General] Tendon Type · Low Relaxation Tendons: 0 · Stress Relieved Tendons: 1 · Prestressing Bars: 2 | `"TENDON_TYPE"` | integer | 0 | Optional |
| 3 | [General] Exposure Factor for Crack Width · Class 1 (1.0): 0 · Class 2 (2.0): 1 · USER: 2 | `"EXPOSURE_FACTOR"` | integer | 0 | Optional |
| 4 | [General] User Defined Exposure Factor · Minimum: 0 | `"USER_FACTOR"` | number | 1 | Optional |
| 5 | [General] Corrosive Condition · Severe: 0 · Moderate/Mild: 1 | `"CORROSIVE_CONDITION"` | integer | 0 | Optional |
| 6 | [General] Flexural Strength · Code: 0 · Strain Compatibility: 1 | `"FLEXURAL_STRENGTH"` | integer | 0 | Optional |
| 7 | [General] Construction Type · Segmental: 0 · Non-Segmental: 1 | `"CONSTRUCTION_TYPE"` | integer | 1 | Optional |
| 8 | [General] Stress by Construction Stage | `"STRESS_CS"` | boolean | false | Optional |
| 9 | [General] Stress by Service Load Combinations | `"STRESS_SLC"` | boolean | false | Optional |
| 10 | [General] Stress in Prestressing Tendons | `"STRESS_PT"` | boolean | false | Optional |
| 11 | [General] Principal Stress by Construction Stage | `"PRINCIPAL_STRESS_CS"` | boolean | false | Optional |
| 12 | [General] Principal Stress by Service Load Combination (Max Shear) | `"PRINCIPAL_STRESS_SLC_MAX_SHEAR"` | boolean | false | Optional |
| 13 | [General] Principal Stress by Service Load Combination (Max Torsion) | `"PRINCIPAL_STRESS_SLC_MAX_TORSION"` | boolean | false | Optional |
| 14 | [General] Crack Check Option (Only Composite Section Model) | `"CRACK_CHECK"` | boolean | false | Optional |
| 15 | [General] Flexural Strength Check | `"FLEXURAL_CHECK"` | boolean | false | Optional |
| 16 | [General] Shear Strength Check | `"SHEAR_CHECK"` | boolean | false | Optional |
| 17 | [General] Combined Shear and Torsion Check | `"SHEAR_TORSION_COMBINED"` | boolean | false | Optional |

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
        "^1$": {
          "title": "PSC Design Code",
          "type": "object",
          "required": [
            "DGNCODE"
          ],
          "additionalProperties": false,
          "properties": {
            "DGNCODE": {
              "type": "string",
              "description": "PSC Design Code",
              "enum": [
                "AASHTO-LRFD24"
              ]
            },
            "TENDON_TYPE": {
              "type": "integer",
              "description": "Tendon Type",
              "enum": [
                0,
                1,
                2
              ],
              "default": 0
            },
            "EXPOSURE_FACTOR": {
              "type": "integer",
              "description": "Exposure Factor for Crack Width",
              "enum": [
                0,
                1,
                2
              ],
              "default": 0
            },
            "USER_FACTOR": {
              "type": "number",
              "exclusiveMinimum": 0,
              "default": 1,
              "description": "User Defined Exposure Factor"
            },
            "CORROSIVE_CONDITION": {
              "type": "integer",
              "description": "Corrosive Condition",
              "enum": [
                0,
                1
              ],
              "default": 0
            },
            "FLEXURAL_STRENGTH": {
              "type": "integer",
              "description": "Flexural Strength",
              "enum": [
                0,
                1
              ],
              "default": 0
            },
            "CONSTRUCTION_TYPE": {
              "type": "integer",
              "description": "Construction Type",
              "enum": [
                0,
                1
              ],
              "default": 1
            },
            "STRESS_CS": {
              "type": "boolean",
              "description": "Stress by Construction Stage",
              "default": false
            },
            "STRESS_SLC": {
              "type": "boolean",
              "description": "Stress by Service Load Combinations",
              "default": false
            },
            "STRESS_PT": {
              "type": "boolean",
              "description": "Stress in Prestressing Tendons",
              "default": false
            },
            "PRINCIPAL_STRESS_CS": {
              "type": "boolean",
              "description": "Principal Stress by Construction Stage",
              "default": false
            },
            "PRINCIPAL_STRESS_SLC_MAX_SHEAR": {
              "type": "boolean",
              "description": "Principal Stress by Service Load Combination (Max Shear)",
              "default": false
            },
            "PRINCIPAL_STRESS_SLC_MAX_TORSION": {
              "type": "boolean",
              "description": "Principal Stress by Service Load Combination (Max Torsion)",
              "default": false
            },
            "CRACK_CHECK": {
              "type": "boolean",
              "description": "Crack Check Option",
              "default": false
            },
            "FLEXURAL_CHECK": {
              "type": "boolean",
              "description": "Flexural Strength Check",
              "default": false
            },
            "SHEAR_CHECK": {
              "type": "boolean",
              "description": "Shear Strength Check",
              "default": false
            },
            "SHEAR_TORSION_COMBINED": {
              "type": "boolean",
              "description": "Combined Shear and Torsion Check",
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

- `DPSC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "AASHTO-LRFD24",
      "TENDON_TYPE": 1,
      "EXPOSURE_FACTOR": 2,
      "USER_FACTOR": 0.85,
      "CORROSIVE_CONDITION": 1,
      "FLEXURAL_STRENGTH": 1,
      "CONSTRUCTION_TYPE": 1,
      "STRESS_CS": true,
      "STRESS_SLC": true,
      "STRESS_PT": true,
      "PRINCIPAL_STRESS_CS": true,
      "PRINCIPAL_STRESS_SLC_MAX_SHEAR": true,
      "PRINCIPAL_STRESS_SLC_MAX_TORSION": true,
      "CRACK_CHECK": true,
      "FLEXURAL_CHECK": true,
      "SHEAR_CHECK": true,
      "SHEAR_TORSION_COMBINED": true
    }
  }
}
```

**Response**

```json
{
  "DPSC": {
    "1": {
      "DGNCODE": "AASHTO-LRFD24",
      "TENDON_TYPE": 1,
      "EXPOSURE_FACTOR": 2,
      "USER_FACTOR": 0.85,
      "CORROSIVE_CONDITION": 1,
      "FLEXURAL_STRENGTH": 1,
      "CONSTRUCTION_TYPE": 1,
      "STRESS_CS": true,
      "STRESS_SLC": true,
      "STRESS_PT": true,
      "PRINCIPAL_STRESS_CS": true,
      "PRINCIPAL_STRESS_SLC_MAX_SHEAR": true,
      "PRINCIPAL_STRESS_SLC_MAX_TORSION": true,
      "CRACK_CHECK": true,
      "FLEXURAL_CHECK": true,
      "SHEAR_CHECK": true,
      "SHEAR_TORSION_COMBINED": true
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/DPSC"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "DGNCODE": "AASHTO-LRFD24",
      "TENDON_TYPE": 1,
      "EXPOSURE_FACTOR": 2,
      "USER_FACTOR": 0.85,
      "CORROSIVE_CONDITION": 1,
      "FLEXURAL_STRENGTH": 1,
      "CONSTRUCTION_TYPE": 1,
      "STRESS_CS": true,
      "STRESS_SLC": true,
      "STRESS_PT": true,
      "PRINCIPAL_STRESS_CS": true,
      "PRINCIPAL_STRESS_SLC_MAX_SHEAR": true,
      "PRINCIPAL_STRESS_SLC_MAX_TORSION": true,
      "CRACK_CHECK": true,
      "FLEXURAL_CHECK": true,
      "SHEAR_CHECK": true,
      "SHEAR_TORSION_COMBINED": true
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```

### 이전 한국어 원문

**원문** [한국어 57945475575321](https://support.midasuser.com/hc/ko/articles/57945475575321)

**원문 Active Methods** `POST` · `GET` · `PUT` · `DELETE`

> ⚠️ 메서드는 영문 글에서 GET · PUT · DELETE, 이 글에서 POST · GET · PUT · DELETE입니다. 요청 Schema의 Key 차이는 영문 글만 `CRACK_CHECK`입니다. 영문 Schema의 Assign은 ID "1"을 쓰고 이 글은 숫자 ID 패턴을 제시합니다. 영문 Schema는 DGNCODE를 필수로 지정하며 이 글은 긴장재 및 설계 관련 설정도 필수로 지정합니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] PSC Design Code · AASHTO-LRFD24: "AASHTO-LRFD24" | `"DGNCODE"` | string | - | **Required** |
| 2 | [General] Tendon Type · Low Relaxation Tendons: "0" · Stress Relieved Tendons: "1" · Prestressing Bars: "2" | `"TENDON_TYPE"` | integer | 0 | **Required** |
| 3 | [General] Exposure Factor for Crack Width · Class 1 (1.0): "0" · Class 2 (2.0): "1" · USER: "2" | `"EXPOSURE_FACTOR"` | integer | 0 | **Required** |
| 4 | [General] Corrosive Condition · Severe: "0" · Moderate/Mild: "1" | `"CORROSIVE_CONDITION"` | integer | 0 | **Required** |
| 5 | [General] Flexural Strength · Code: "0" · Strain Compatibility: "1" | `"FLEXURAL_STRENGTH"` | integer | 0 | **Required** |
| 6 | [General] Construction Type · Segmental: "0" · Non-Segmental: "1" | `"CONSTRUCTION_TYPE"` | integer | 1 | **Required** |
| 7 | [General] Stress by Construction Stage | `"STRESS_CS"` | boolean | false | Optional |
| 8 | [General] Stress by Service Load Combinations | `"STRESS_SLC"` | boolean | false | Optional |
| 9 | [General] Stress in Prestressing Tendons | `"STRESS_PT"` | boolean | false | Optional |
| 10 | [General] Principal Stress by Construction Stage | `"PRINCIPAL_STRESS_CS"` | boolean | false | Optional |
| 11 | [General] Principal Stress by Service Load Combination (Max Shear) | `"PRINCIPAL_STRESS_SLC_MAX_SHEAR"` | boolean | false | Optional |
| 12 | [General] Principal Stress by Service Load Combination (Max Torsion) | `"PRINCIPAL_STRESS_SLC_MAX_TORSION"` | boolean | false | Optional |
| 13 | [General] Flexural Strength Check | `"FLEXURAL_CHECK"` | boolean | false | Optional |
| 14 | [General] Shear Strength Check | `"SHEAR_CHECK"` | boolean | false | Optional |
| 15 | [General] Combined Shear and Torsion Check | `"SHEAR_TORSION_COMBINED"` | boolean | false | Optional |
| 16 | [When "EXPOSURE_FACTOR" is 2] User Defined Exposure Factor Constraints: · Value Range: >= 0 | `"USER_FACTOR"` | number | 1 | **Required** |

**JSON Schema**

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
          "title": "PSC Design Code",
          "type": "object",
          "required": [
            "DGNCODE",
            "TENDON_TYPE",
            "EXPOSURE_FACTOR",
            "CORROSIVE_CONDITION",
            "FLEXURAL_STRENGTH",
            "CONSTRUCTION_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "DGNCODE": {
              "type": "string",
              "description": "PSC Design Code",
              "enum": [
                "AASHTO-LRFD24"
              ]
            },
            "TENDON_TYPE": {
              "type": "integer",
              "description": "Tendon Type",
              "enum": [
                0,
                1,
                2
              ],
              "default": 0
            },
            "EXPOSURE_FACTOR": {
              "type": "integer",
              "description": "Exposure Factor for Crack Width",
              "enum": [
                0,
                1,
                2
              ],
              "default": 0
            },
            "USER_FACTOR": {
              "type": "number",
              "minimum": 0,
              "default": 1,
              "description": "User Defined Exposure Factor"
            },
            "CORROSIVE_CONDITION": {
              "type": "integer",
              "description": "Corrosive Condition",
              "enum": [
                0,
                1
              ],
              "default": 0
            },
            "FLEXURAL_STRENGTH": {
              "type": "integer",
              "description": "Flexural Strength",
              "enum": [
                0,
                1
              ],
              "default": 0
            },
            "CONSTRUCTION_TYPE": {
              "type": "integer",
              "description": "Construction Type",
              "enum": [
                0,
                1
              ],
              "default": 1
            },
            "STRESS_CS": {
              "type": "boolean",
              "description": "Stress by Construction Stage",
              "default": false
            },
            "STRESS_SLC": {
              "type": "boolean",
              "description": "Stress by Service Load Combinations",
              "default": false
            },
            "STRESS_PT": {
              "type": "boolean",
              "description": "Stress in Prestressing Tendons",
              "default": false
            },
            "PRINCIPAL_STRESS_CS": {
              "type": "boolean",
              "description": "Principal Stress by Construction Stage",
              "default": false
            },
            "PRINCIPAL_STRESS_SLC_MAX_SHEAR": {
              "type": "boolean",
              "description": "Principal Stress by Service Load Combination (Max Shear)",
              "default": false
            },
            "PRINCIPAL_STRESS_SLC_MAX_TORSION": {
              "type": "boolean",
              "description": "Principal Stress by Service Load Combination (Max Torsion)",
              "default": false
            },
            "FLEXURAL_CHECK": {
              "type": "boolean",
              "description": "Flexural Strength Check",
              "default": false
            },
            "SHEAR_CHECK": {
              "type": "boolean",
              "description": "Shear Strength Check",
              "default": false
            },
            "SHEAR_TORSION_COMBINED": {
              "type": "boolean",
              "description": "Combined Shear and Torsion Check",
              "default": false
            }
          },
          "allOf": [
            {
              "if": {
                "properties": {
                  "EXPOSURE_FACTOR": {
                    "const": 2
                  }
                },
                "required": [
                  "EXPOSURE_FACTOR"
                ]
              },
              "then": {
                "required": [
                  "USER_FACTOR"
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


---

## 2. `MEMB` — PSC Segment Assignment

> **기능** PSC 설계용 부재에 요소를 배정합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/MEMB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 57945530824345](https://support.midasuser.com/hc/en-us/articles/57945530824345)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Element List | `"AELEM"` | array | - | **Required** |
| 2 | [General] Allow Single Element Member | `"ELEM_MEMBER"` | boolean | false | Optional |
| 3 | [General] Joint Type · Resin: 0 · Cement: 1 | `"JOINT_TYPE"` | integer | 0 | Optional |

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
            "ELEM_MEMBER": {
              "type": "boolean",
              "description": "Allow Single Element Member",
              "default": false
            },
            "JOINT_TYPE": {
              "type": "integer",
              "description": "Joint Type",
              "enum": [
                0,
                1
              ],
              "default": 0
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

- `PSCMEMB`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "AELEM": [
        1,
        2,
        3
      ],
      "ELEM_MEMBER": false,
      "JOINT_TYPE": 0
    },
    "2": {
      "AELEM": [
        4,
        5,
        6
      ],
      "ELEM_MEMBER": true,
      "JOINT_TYPE": 1
    }
  }
}
```

**Response**

```json
{
  "PSCMEMB": {
    "1": {
      "AELEM": [
        1,
        2,
        3
      ],
      "ELEM_MEMBER": false,
      "JOINT_TYPE": 0
    },
    "2": {
      "AELEM": [
        4,
        5,
        6
      ],
      "ELEM_MEMBER": true,
      "JOINT_TYPE": 1
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/MEMB"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "AELEM": [
        1,
        2,
        3
      ],
      "ELEM_MEMBER": false,
      "JOINT_TYPE": 0
    },
    "2": {
      "AELEM": [
        4,
        5,
        6
      ],
      "ELEM_MEMBER": true,
      "JOINT_TYPE": 1
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```

### 이전 한국어 원문

**원문** [한국어 57945514821529](https://support.midasuser.com/hc/ko/articles/57945514821529)

**원문 Active Methods** `POST` · `GET` · `PUT` · `DELETE`

> ⚠️ 이전 표에는 ELEM_TYPE 행이 있습니다. 최신 표와 요청 예제는 일반 요소의 URI를 사용합니다. 두 JSON Schema는 같습니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Element List | `"AELEM"` | Array [integer] | - | **Required** |
| 2 | [General] Element Type · Element: "0" · Virtual Beam: "1" | `"ELEM_TYPE"` | integer | 0 | **Required** |
| 3 | [General] Allow Single Element Member | `"ELEM_MEMBER"` | boolean | false | Optional |
| 4 | [General] Joint Type · Resin: "0" · Cement: "1" | `"JOINT_TYPE"` | integer | 0 | **Required** |

**JSON Schema**

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
            "ELEM_MEMBER": {
              "type": "boolean",
              "description": "Allow Single Element Member",
              "default": false
            },
            "JOINT_TYPE": {
              "type": "integer",
              "description": "Joint Type",
              "enum": [
                0,
                1
              ],
              "default": 0
            }
          }
        }
      }
    }
  }
}
```


---

## 3. `SLCT` — Serviceability Load Combination Type

> **기능** PSC 설계의 사용성 하중조합 유형을 설정합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/SLCT
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 57945572333849](https://support.midasuser.com/hc/en-us/articles/57945572333849)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Serviceability Load Combination Name | `"LC_NAME"` | string | - | Optional |
| 2 | [General] Serviceability Load Type · Service Limit(SL): 0 · Service Limit1: 1 · Service Limit3: 2 | `"SL_TYPE"` | integer | - | Optional |

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
          "additionalProperties": false,
          "properties": {
            "LC_NAME": {
              "type": "string",
              "description": "Serviceability Load Combination Name"
            },
            "SL_TYPE": {
              "type": "integer",
              "description": "Serviceability Load Type",
              "enum": [
                0,
                1,
                2
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

- `SLCT`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "2": {
      "LC_NAME": "cLCB2",
      "SL_TYPE": 0
    },
    "3": {
      "LC_NAME": "cLCB3",
      "SL_TYPE": 1
    },
    "4": {
      "LC_NAME": "cLCB4",
      "SL_TYPE": 2
    },
    "5": {
      "LC_NAME": "cLCB5",
      "SL_TYPE": 0
    }
  }
}
```

**Response**

```json
{
  "SLCT": {
    "2": {
      "LC_NAME": "cLCB2",
      "SL_TYPE": 0
    },
    "3": {
      "LC_NAME": "cLCB3",
      "SL_TYPE": 1
    },
    "4": {
      "LC_NAME": "cLCB4",
      "SL_TYPE": 2
    },
    "5": {
      "LC_NAME": "cLCB5",
      "SL_TYPE": 0
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/SLCT"

payload = json.loads(r'''
{
  "Assign": {
    "2": {
      "LC_NAME": "cLCB2",
      "SL_TYPE": 0
    },
    "3": {
      "LC_NAME": "cLCB3",
      "SL_TYPE": 1
    },
    "4": {
      "LC_NAME": "cLCB4",
      "SL_TYPE": 2
    },
    "5": {
      "LC_NAME": "cLCB5",
      "SL_TYPE": 0
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```

### 이전 한국어 원문

**원문** [한국어 57945593541657](https://support.midasuser.com/hc/ko/articles/57945593541657)

**원문 Active Methods** `POST` · `GET` · `PUT` · `DELETE`

> ⚠️ 메서드는 영문 글에서 GET · PUT · DELETE, 이 글에서 POST · GET · PUT · DELETE입니다. 이전 Schema는 LC_NAME과 SL_TYPE을 필수로 지정하고 SL_TYPE의 기본값을 0으로 명시합니다. 영문 Schema에는 이 필수 목록과 기본값이 없습니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Serviceability Load Combination Name | `"LC_NAME"` | string | - | **Required** |
| 2 | [General] Serviceability Load Type · Service Limit(SL): "0" · Strength Limit1: "1" · Strength Limit3: "2" | `"SL_TYPE"` | integer | 0 | **Required** |

**JSON Schema**

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
            "LC_NAME",
            "SL_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "LC_NAME": {
              "type": "string",
              "description": "Serviceability Load Combination Name"
            },
            "SL_TYPE": {
              "type": "integer",
              "description": "Serviceability Load Type",
              "enum": [
                0,
                1,
                2
              ],
              "default": 0
            }
          }
        }
      }
    }
  }
}
```


---

## 4. `INFS` — Interface shear

> **기능** 접합면 전단 검토에 사용할 조건을 입력합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/INFS
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 57945615379609](https://support.midasuser.com/hc/en-us/articles/57945615379609)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings, where each entry represents an element (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] SURFACE_CLASSIFICATION_I | `"SURFACE_CLASSIFICATION_I"` | object | - | Optional |
| 1.1 | └ [General] Surface Classification · Roughened (CIP slab): 0 · Monolithically: 1 · Intentionally roughened (LWC): 2 · Intentionally roughened (NWC): 3 · Not intentionally roughened: 4 · Anchored: 5 | `"SURFACE_CLASSIFICATION"` | integer | 0 | Optional |
| 1.2 | └ [General] Width of the interfacial cross-section engaged in shear transfer, Bvi · Minimum: 0 | `"BVI"` | number | 0 | Optional |
| 1.3 | └ [General] Cross-sectional area of reinforcement crossing the interfacial shear plane, Avf · Minimum: 0 | `"AVF"` | number | 0 | Optional |
| 1.4 | └ [General] Yield strength of reinforcement crossing the interfacial shear plane, Fy · Minimum: 0 | `"FY"` | number | 0 | Optional |
| 2 | [General] SURFACE_CLASSIFICATION_J | `"SURFACE_CLASSIFICATION_J"` | object | - | Optional |
| 2.1 | └ [General] Surface Classification · Roughened (CIP slab): 0 · Monolithically: 1 · Intentionally roughened (LWC): 2 · Intentionally roughened (NWC): 3 · Not intentionally roughened: 4 · Anchored: 5 | `"SURFACE_CLASSIFICATION"` | integer | 0 | Optional |
| 2.2 | └ [General] Width of the interfacial cross-section engaged in shear transfer, Bvi · Minimum: 0 | `"BVI"` | number | 0 | Optional |
| 2.3 | └ [General] Cross-sectional area of reinforcement crossing the interfacial shear plane, Avf · Minimum: 0 | `"AVF"` | number | 0 | Optional |
| 2.4 | └ [General] Yield strength of reinforcement crossing the interfacial shear plane, Fy · Minimum: 0 | `"FY"` | number | 0 | Optional |

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
      "description": "Object keyed by ID strings, where each entry represents an element (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "SURFACE_CLASSIFICATION_I": {
              "type": "object",
              "description": "SURFACE_CLASSIFICATION_I",
              "additionalProperties": false,
              "properties": {
                "SURFACE_CLASSIFICATION": {
                  "type": "integer",
                  "description": "Surface Classification",
                  "enum": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5
                  ],
                  "default": 0
                },
                "BVI": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Width of the interfacial cross-section engaged in shear transfer",
                  "default": 0
                },
                "AVF": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Cross-sectional area of reinforcement crossing the interfacial shear plane",
                  "default": 0
                },
                "FY": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Yield strength of reinforcement crossing the interfacial shear plane",
                  "default": 0
                }
              }
            },
            "SURFACE_CLASSIFICATION_J": {
              "type": "object",
              "description": "SURFACE_CLASSIFICATION_J",
              "additionalProperties": false,
              "properties": {
                "SURFACE_CLASSIFICATION": {
                  "type": "integer",
                  "description": "Surface Classification",
                  "enum": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5
                  ],
                  "default": 0
                },
                "BVI": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Width of the interfacial cross-section engaged in shear transfer",
                  "default": 0
                },
                "AVF": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Cross-sectional area of reinforcement crossing the interfacial shear plane",
                  "default": 0
                },
                "FY": {
                  "type": "number",
                  "minimum": 0,
                  "default": 0,
                  "description": "Yield strength of reinforcement crossing the interfacial shear plane"
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

- `INFS`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 1,
        "BVI": 0.6,
        "AVF": 0.000258,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 2,
        "BVI": 0.6,
        "AVF": 0.000258,
        "FY": 413685
      }
    },
    "2": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 2,
        "BVI": 0.6,
        "AVF": 0.000516,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 3,
        "BVI": 0.6,
        "AVF": 0.000516,
        "FY": 413685
      }
    },
    "3": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 3,
        "BVI": 0.6,
        "AVF": 0.000774,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 4,
        "BVI": 0.6,
        "AVF": 0.000774,
        "FY": 413685
      }
    },
    "4": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 4,
        "BVI": 0.6,
        "AVF": 0.001032,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 5,
        "BVI": 0.6,
        "AVF": 0.001032,
        "FY": 413685
      }
    },
    "5": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 5,
        "BVI": 0.6,
        "AVF": 0.00129,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 0,
        "BVI": 0.6,
        "AVF": 0.00129,
        "FY": 413685
      }
    },
    "6": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 0,
        "BVI": 0.6,
        "AVF": 0.001548,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 1,
        "BVI": 0.6,
        "AVF": 0.001548,
        "FY": 413685
      }
    }
  }
}
```

**Response**

```json
{
  "INFS": {
    "1": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 1,
        "BVI": 0.6,
        "AVF": 0.000258,
        "FY": 413685.0
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 2,
        "BVI": 0.6,
        "AVF": 0.000258,
        "FY": 413685.0
      }
    },
    "2": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 2,
        "BVI": 0.6,
        "AVF": 0.000516,
        "FY": 413685.0
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 3,
        "BVI": 0.6,
        "AVF": 0.000516,
        "FY": 413685.0
      }
    },
    "3": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 3,
        "BVI": 0.6,
        "AVF": 0.000774,
        "FY": 413685.0
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 4,
        "BVI": 0.6,
        "AVF": 0.000774,
        "FY": 413685.0
      }
    },
    "4": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 4,
        "BVI": 0.6,
        "AVF": 0.001032,
        "FY": 413685.0
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 5,
        "BVI": 0.6,
        "AVF": 0.001032,
        "FY": 413685.0
      }
    },
    "5": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 5,
        "BVI": 0.6,
        "AVF": 0.00129,
        "FY": 413685.0
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 0,
        "BVI": 0.6,
        "AVF": 0.00129,
        "FY": 413685.0
      }
    },
    "6": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 0,
        "BVI": 0.6,
        "AVF": 0.001548,
        "FY": 413685.0
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 1,
        "BVI": 0.6,
        "AVF": 0.001548,
        "FY": 413685.0
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/INFS"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 1,
        "BVI": 0.6,
        "AVF": 0.000258,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 2,
        "BVI": 0.6,
        "AVF": 0.000258,
        "FY": 413685
      }
    },
    "2": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 2,
        "BVI": 0.6,
        "AVF": 0.000516,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 3,
        "BVI": 0.6,
        "AVF": 0.000516,
        "FY": 413685
      }
    },
    "3": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 3,
        "BVI": 0.6,
        "AVF": 0.000774,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 4,
        "BVI": 0.6,
        "AVF": 0.000774,
        "FY": 413685
      }
    },
    "4": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 4,
        "BVI": 0.6,
        "AVF": 0.001032,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 5,
        "BVI": 0.6,
        "AVF": 0.001032,
        "FY": 413685
      }
    },
    "5": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 5,
        "BVI": 0.6,
        "AVF": 0.00129,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 0,
        "BVI": 0.6,
        "AVF": 0.00129,
        "FY": 413685
      }
    },
    "6": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 0,
        "BVI": 0.6,
        "AVF": 0.001548,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 1,
        "BVI": 0.6,
        "AVF": 0.001548,
        "FY": 413685
      }
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```

### 이전 한국어 원문

**원문** [한국어 57945592046233](https://support.midasuser.com/hc/ko/articles/57945592046233)

**원문 Active Methods** `POST` · `GET` · `PUT` · `DELETE`

> ⚠️ 이전 Schema는 INTERFACE_SHEAR와 SURFACE_CLASSIFICATION을 필수로 지정합니다. 영문 Schema는 이 필수 목록을 두지 않고 양 끝의 AVF·BVI·FY 기본값을 0으로 명시합니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings, where each entry represents an element (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] SURFACE_CLASSIFICATION_I | `"SURFACE_CLASSIFICATION_I"` | object | - | Optional |
| 1.1 | └ [General] Surface Classification · Roughened (CIP slab): "0" · Monolithically: "1" · Intentionally roughened (LWC): "2" · Intentionally roughened (NWC): "3" · Not intentionally roughened: "4" · Anchored: "5" | `"SURFACE_CLASSIFICATION"` | integer | 0 | Optional |
| 1.2 | └ [General] Bvi Constraints: · Value Range: >= 0 | `"BVI"` | number | - | Optional |
| 1.3 | └ [General] Avf Constraints: · Value Range: >= 0 | `"AVF"` | number | - | Optional |
| 1.4 | └ [General] Fy Constraints: · Value Range: >= 0 | `"FY"` | number | - | Optional |
| 2 | [General] SURFACE_CLASSIFICATION_J | `"SURFACE_CLASSIFICATION_J"` | object | - | Optional |
| 2.1 | └ [General] Surface Classification · Roughened (CIP slab): "0" · Monolithically: "1" · Intentionally roughened (LWC): "2" · Intentionally roughened (NWC): "3" · Not intentionally roughened: "4" · Anchored: "5" | `"SURFACE_CLASSIFICATION"` | integer | 0 | Optional |
| 2.2 | └ [General] Bvi Constraints: · Value Range: >= 0 | `"BVI"` | number | - | Optional |
| 2.3 | └ [General] Avf Constraints: · Value Range: >= 0 | `"AVF"` | number | - | Optional |
| 2.4 | └ [General] Fy Constraints: · Value Range: >= 0 | `"FY"` | number | - | Optional |

**JSON Schema**

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
      "description": "Object keyed by ID strings, where each entry represents an element (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "INTERFACE_SHEAR",
            "SURFACE_CLASSIFICATION"
          ],
          "additionalProperties": false,
          "properties": {
            "SURFACE_CLASSIFICATION_I": {
              "type": "object",
              "description": "SURFACE_CLASSIFICATION_I",
              "additionalProperties": false,
              "x-ui": {
                "label": "SURFACE_CLASSIFICATION_I",
                "order": 3
              },
              "properties": {
                "SURFACE_CLASSIFICATION": {
                  "type": "integer",
                  "description": "Surface Classification",
                  "enum": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5
                  ],
                  "default": 0,
                  "x-ui": {
                    "component": "RadioGroup",
                    "label": "Surface Classification",
                    "order": 1
                  },
                  "x-enum-labels": {
                    "0": "Roughened (CIP slab)",
                    "1": "Monolithically",
                    "2": "Intentionally roughened (LWC)",
                    "3": "Intentionally roughened (NWC)",
                    "4": "Not intentionally roughened",
                    "5": "Anchored"
                  }
                },
                "BVI": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Width of the interfacial cross-section engaged in shear transfer",
                  "x-ui": {
                    "label": "Bvi",
                    "order": 1
                  }
                },
                "AVF": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Cross-sectional area of reinforcement crossing the interfacial shear plane",
                  "x-ui": {
                    "label": "Avf",
                    "order": 2
                  }
                },
                "FY": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Yield strength of reinforcement crossing the interfacial shear plane",
                  "x-ui": {
                    "label": "Fy",
                    "order": 3
                  }
                }
              }
            },
            "SURFACE_CLASSIFICATION_J": {
              "type": "object",
              "description": "SURFACE_CLASSIFICATION_J",
              "additionalProperties": false,
              "x-ui": {
                "label": "SURFACE_CLASSIFICATION_J",
                "order": 3
              },
              "properties": {
                "SURFACE_CLASSIFICATION": {
                  "type": "integer",
                  "description": "Surface Classification",
                  "enum": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5
                  ],
                  "default": 0,
                  "x-ui": {
                    "component": "RadioGroup",
                    "label": "Surface Classification",
                    "order": 1
                  },
                  "x-enum-labels": {
                    "0": "Roughened (CIP slab)",
                    "1": "Monolithically",
                    "2": "Intentionally roughened (LWC)",
                    "3": "Intentionally roughened (NWC)",
                    "4": "Not intentionally roughened",
                    "5": "Anchored"
                  }
                },
                "BVI": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Width of the interfacial cross-section engaged in shear transfer",
                  "x-ui": {
                    "label": "Bvi",
                    "order": 1
                  }
                },
                "AVF": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Cross-sectional area of reinforcement crossing the interfacial shear plane",
                  "x-ui": {
                    "label": "Avf",
                    "order": 2
                  }
                },
                "FY": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Yield strength of reinforcement crossing the interfacial shear plane",
                  "x-ui": {
                    "label": "Fy",
                    "order": 3
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


---

## 5. `MATD` — Modify Material

> **기능** PSC 설계용 거더·슬래브의 콘크리트 및 철근 재료를 수정합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/MATD
```

### Active Methods

`GET` · `PUT` · `DELETE`

> ⚠️ 최신 영문 글과 같은 ID의 한글판은 GET·PUT·DELETE를 나열합니다. 이전 영문 본문에는 POST도 표시됐습니다.

### Specifications

**원문** [영문 58043488354969](https://support.midasuser.com/hc/en-us/articles/58043488354969)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a material ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Girder Material Type | `"GIRDER_MATL_PROP"` | object | - | Optional |
| 1.1 | └ [General] CODE · None: "None" · ASTM19(RC): "ASTM19(RC)" · ASTM(RC): "ASTM(RC)" · U.S.C(US)(RC): "U.S.C(US)(RC)" · U.S.C(SI)(RC): "U.S.C(SI)(RC)" · NMX2023(RC): "NMX2023(RC)" · NMX2023(MKS)(RC): "NMX2023(MKS)(RC)" · NMX NTC-2017(RC): "NMX NTC-2017(RC)" · CSA(RC): "CSA(RC)" · BS(RC): "BS(RC)" · EN04(RC): "EN04(RC)" · EN(RC): "EN(RC)" · NTC08(RC): "NTC08(RC)" · NTC12(RC): "NTC12(RC)" · NTC18(RC): "NTC18(RC)" · UNI(RC): "UNI(RC)" · SS(RC): "SS(RC)" · GOST-SP(RC): "GOST-SP(RC)" · GOST-SNIP(RC): "GOST-SNIP(RC)" · JIS(RC): "JIS(RC)" · JIS-Civil(RC): "JIS-Civil(RC)" · JTJ023-85(RC): "JTJ023-85(RC)" · Q/CR 9300-18(RC): "Q/CR 9300-18(RC)" · GB 50917-13(RC): "GB 50917-13(RC)" · GB/T10(RC): "GB/T10(RC)" · GB(RC): "GB(RC)" · GB-Civil(RC): "GB-Civil(RC)" · TB10092-17(RC): "TB10092-17(RC)" · JTG3362-18(RC): "JTG3362-18(RC)" · JTG04(RC): "JTG04(RC)" · TB05(RC): "TB05(RC)" · KS19(RC): "KS19(RC)" · KS01(RC): "KS01(RC)" · KS(RC): "KS(RC)" · KSCE-LSD15(RC): "KSCE-LSD15(RC)" · KS01-Civil(RC): "KS01-Civil(RC)" · KS-Civil(RC): "KS-Civil(RC)" · PNS49(RC): "PNS49(RC)" · SNI(RC): "SNI(RC)" · TIS(RC): "TIS(RC)" · TIS(MKS)(RC): "TIS(MKS)(RC)" · IRC(RC): "IRC(RC)" · IRS(RC): "IRS(RC)" · IS(RC): "IS(RC)" · CNS560-18(RC): "CNS560-18(RC)" · CNS560(RC): "CNS560(RC)" · CNS(RC): "CNS(RC)" · AS17(RC): "AS17(RC)" · TMH7(RC): "TMH7(RC)" · SP63.2018(RC): "SP63.2018(RC)" · TS(RC): "TS(RC)" · NBR 6118(RC): "NBR 6118(RC)" · TCVN2018(RC): "TCVN2018(RC)" · CSA-S6-25(RC): "CSA-S6-25(RC)" | `"CODE"` | string | - | **Required** |
| 1.2 | └ [When CODE = "None"] NAME | `"NAME"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["ASTM19(RC)", "ASTM(RC)", "U.S.C(US)(RC)"]] GRADE · Grade C2500 · Grade C3000 · Grade C3500 · Grade C4000 · Grade C4500 · Grade C5000 · Grade C6000 · Grade C7000 · Grade C8000 · Grade C9000 · Grade C10000 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["U.S.C(SI)(RC)", "PNS49(RC)"]] GRADE · Grade C18 · Grade C21 · Grade C25 · Grade C28 · Grade C32 · Grade C35 · Grade C42 · Grade C49 · Grade C56 · Grade C63 · Grade C69 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)"]] GRADE · 250-C1A(C) · 250-C1A(B) · 300-C1A(C) · 300-C1A(B) · 350-C1A(C) · 350-C1A(B) · 400-C1B(C) · 400-C1B(B) · 450-C1B(C) · 450-C1B(B) · 500-C1B(C) · 500-C1B(B) · 550-C1B(C) · 550-C1B(B) · 600-C1B(C) · 600-C1B(B) · 650-C1B(C) · 650-C1B(B) · 700-C1B(C) · 700-C1B(B) · 200-C2 · 250-C2 · 300-C2 · 350-C2 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "NMX NTC-2017(RC)"] GRADE · 200-C1C · 250-C1C · 300-C1C · 350-C1C · 400-C1C · 450-C1C · 500-C1C · 550-C1C · 600-C1C · 650-C1C · 700-C1C · 750-C1C · 800-C1C · 200-C1B · 250-C1B · 300-C1B · 350-C1B · 400-C1B · 450-C1B · 500-C1B · 550-C1B · 600-C1B · 650-C1B · 700-C1B · 750-C1B · 800-C1B · 150-C2 · 200-C2 · 250-C2 · 300-C2 · 400-C2 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "CSA(RC)"] GRADE · C25 · C30 · C35 · C40 · C45 · C50 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "BS(RC)"] GRADE · C15 · C20 · C25 · C30 · C35 · C40 · C45 · C50 · C55 · C60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] GRADE · C12/15 · C16/20 · C20/25 · C25/30 · C30/37 · C32/40 · C35/45 · C40/50 · C45/55 · C50/60 · C55/67 · C60/75 · C70/85 · C80/95 · C90/105 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "EN(RC)"] GRADE · C12/15 · C16/20 · C20/25 · C25/30 · C30/37 · C35/45 · C40/50 · C45/55 · C50/60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] GRADE · C8/10 · C12/15 · C16/20 · C20/25 · C25/30 · C28/35 · C30/37 · C32/40 · C35/45 · C40/50 · C45/55 · C50/60 · C55/67 · C60/75 · C70/85 · C80/95 · C90/105 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "UNI(RC)"] GRADE · Rck10 · Rck15 · Rck20 · Rck25 · Rck30 · Rck35 · Rck40 · Rck45 · Rck50 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["GOST-SP(RC)", "GOST-SNIP(RC)"]] GRADE · B20 · B22.5 · B25 · B27.5 · B30 · B35 · B40 · B45 · B50 · B55 · B60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "JIS(RC)"] GRADE · Fc18 · Fc21 · Fc24 · Fc27 · Fc30 · Fc33 · Fc36 · Fc39 · Fc42 · Fc45 · Fc48 · Fc51 · Fc54 · Fc57 · Fc60 · Fc18(LT1) · Fc21(LT1) · Fc24(LT1) · Fc27(LT1) · Fc30(LT1) · Fc33(LT1) · Fc36(LT1) · Fc18(LT2) · Fc21(LT2) · Fc24(LT2) · Fc27(LT2) | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "JIS-Civil(RC)"] GRADE · Fc21 · Fc24 · Fc27 · Fc30 · Fc36 · Fc40 · Fc50 · Fc60 · Fc70 · Fc80 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "JTJ023-85(RC)"] GRADE · C15 · C20 · C25 · C30 · C40 · C50 · C60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] GRADE · C25 · C30 · C35 · C40 · C45 · C50 · C55 · C60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "GB 50917-13(RC)"] GRADE · C30 · C35 · C40 · C45 · C50 · C55 · C60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["GB/T10(RC)", "GB(RC)", "JTG04(RC)"]] GRADE · C15 · C20 · C25 · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "GB-Civil(RC)"] GRADE · 15 · 20 · 25 · 30 · 40 · 50 · 60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "JTG3362-18(RC)"] GRADE · C25 · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "TB05(RC)"] GRADE · C20 · C25 · C30 · C35 · C40 · C45 · C50 · C55 · C60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["KS19(RC)", "KS01(RC)", "KS01-Civil(RC)"]] GRADE · C15 · C18 · C21 · C24 · C27 · C30 · C35 · C40 · C45 · C49 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 · C90 · C95 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] GRADE · C150 · C180 · C210 · C240 · C270 · C300 · C350 · C400 · C450 · C500 · C550 · C600 · C650 · C700 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "KSCE-LSD15(RC)"] GRADE · C15 · C18 · C21 · C24 · C27 · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 · C90 · C95 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "SNI(RC)"] GRADE · fc17 · fc21 · fc25 · fc30 · fc35 · fc40 · fc45 · fc50 · fc55 · fc60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] GRADE · C150 · C180 · C210 · C240 · C250 · C280 · C300 · C320 · C350 · C380 · C400 · C450 · C500 · C550 · C600 · C650 · C700 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "IRC(RC)"] GRADE · M15 · M20 · M25 · M30 · M35 · M40 · M45 · M50 · M55 · M60 · M65 · M70 · M75 · M80 · M85 · M90 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "IRS(RC)"] GRADE · M20 · M25 · M30 · M35 · M40 · M45 · M50 · M55 · M60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "IS(RC)"] GRADE · M10 · M15 · M20 · M25 · M30 · M35 · M40 · M45 · M50 · M55 · M60 · M65 · M70 · M75 · M80 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "CNS560-18(RC)"] GRADE · C210 · C245 · C280 · C315 · C350 · C420 · C490 · C560 · C700 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["CNS560(RC)", "CNS(RC)"]] GRADE · C210 · C245 · C280 · C315 · C350 · C420 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "AS17(RC)"] GRADE · C20 · C25 · C32 · C40 · C50 · C65 · C80 · C100 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "TMH7(RC)"] GRADE · Grade 20 · Grade 25 · Grade 30 · Grade 40 · Grade 50 · Grade 60 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "SP63.2018(RC)"] GRADE · B3.5 · B5 · B7.5 · B10 · B12.5 · B15 · B20 · B25 · B30 · B35 · B40 · B45 · B50 · B55 · B60 · B70 · B80 · B90 · B100 · B3.5A · B5A · B7.5A · B10A · B12.5A · B15A · B20A · B25A · B30A · B35A · B40A · B15B · B20B · B25B · B30B · B35B · B40B · B45B · B50B · B55B · B60B · LB2.5D800 · LB3.5D800 · LB5D800 · LB7.5D800 · LB2.5D1000 · LB3.5D1000 · LB5D1000 · LB7.5D1000 · LB10D1000 · LB12.5D1000 · LB2.5D1200 · LB3.5D1200 · LB5D1200 · LB7.5D1200 · LB10D1200 · LB12.5D1200 · LB15D1200 · LB2.5D1400 · LB3.5D1400 · LB5D1400 · LB7.5D1400 · LB10D1400 · LB12.5D1400 · LB15D1400 · LB20D1400 · LB25D1400 · LB30D1400 · LB3.5D1600 · LB5D1600 · LB7.5D1600 · LB10D1600 · LB12.5D1600 · LB15D1600 · LB20D1600 · LB25D1600 · LB30D1600 · LB35D1600 · LB5D1800 · LB7.5D1800 · LB10D1800 · LB12.5D1800 · LB15D1800 · LB20D1800 · LB25D1800 · LB30D1800 · LB35D1800 · LB40D1800 · LB7.5D2000 · LB10D2000 · LB12.5D2000 · LB15D2000 · LB20D2000 · LB25D2000 · LB30D2000 · LB35D2000 · LB40D2000 · CB1.5D500 · CB1.5D600 · CB2D600 · CB2.5D600 · CB1.5D700 · CB2D700 · CB2.5D700 · CB3.5D700 · CB2.5D800 · CB3.5D800 · CB5D800 · CB3.5D900 · CB5D900 · CB7.5D900 · CB5D1000 · CB7.5D1000 · CB10D1000 · CB7.5D1100 · CB10D1100 · CB12.5D1100 · CB15D1100 · CB10D1200 · CB12.5D1200 · CB15D1200 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "TS(RC)"] GRADE · C16 · C18 · C20 · C25 · C30 · C35 · C40 · C45 · C50 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "NBR 6118(RC)"] GRADE · C20BD · C20GG · C20LS · C20SS · C25BD · C25GG · C25LS · C25SS · C30BD · C30GG · C30LS · C30SS · C35BD · C35GG · C35LS · C35SS · C40BD · C40GG · C40LS · C40SS · C45BD · C45GG · C45LS · C45SS · C50BD · C50GG · C50LS · C50SS · C55BD · C55GG · C55LS · C55SS · C60BD · C60GG · C60LS · C60SS · C65BD · C65GG · C65LS · C65SS · C70BD · C70GG · C70LS · C70SS · C75BD · C75GG · C75LS · C75SS · C80BD · C80GG · C80LS · C80SS · C85BD · C85GG · C85LS · C85SS · C90BD · C90GG · C90LS · C90SS | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "TCVN2018(RC)"] GRADE · B3.5 · B5 · B7.5 · B10 · B12.5 · B15 · B20 · B25 · B30 · B35 · B40 · B45 · B50 · B55 · B60 · B70 · B80 · B90 · B100 | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "CSA-S6-25(RC)"] GRADE · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 | `"GRADE"` | string | - | **Required** |
| 1.4 | └ [When CODE = "None"] COMP_STRENGTH | `"COMP_STRENGTH"` | number | - | **Required** |
| 1.5 | └ [When CODE = "None"] Light Weight Concrete Factor option. | `"LIGHT_WEIGHT_FACTOR"` | boolean | - | Optional |
| 1.6 | └ [When LIGHT_WEIGHT_FACTOR = true] Light Weight Factor value. Required when LIGHT_WEIGHT_FACTOR is true. · Range: 0.75~1 | `"FACTOR_VALUE"` | number | - | **Required** |
| 2 | [General] Girder Rebar Selection | `"GIRDER_REBAR_PROP"` | object | - | Optional |
| 2.1 | └ [General] Rebar design code. If CODE is 'None', input custom rebar names, Fy and Fys directly instead of selecting GRADE_MAIN_REBAR and GRADE_SUB_REBAR. · None: "None" · ASTM19(RC): "ASTM19(RC)" · ASTM(RC): "ASTM(RC)" · U.S.C(US)(RC): "U.S.C(US)(RC)" · U.S.C(SI)(RC): "U.S.C(SI)(RC)" · NMX2023(RC): "NMX2023(RC)" · NMX2023(MKS)(RC): "NMX2023(MKS)(RC)" · NMX NTC-2017(RC): "NMX NTC-2017(RC)" · CSA(RC): "CSA(RC)" · BS(RC): "BS(RC)" · EN04(RC): "EN04(RC)" · EN(RC): "EN(RC)" · NTC08(RC): "NTC08(RC)" · NTC12(RC): "NTC12(RC)" · NTC18(RC): "NTC18(RC)" · UNI(RC): "UNI(RC)" · SS(RC): "SS(RC)" · GOST-SP(RC): "GOST-SP(RC)" · GOST-SNIP(RC): "GOST-SNIP(RC)" · JIS(RC): "JIS(RC)" · JIS-Civil(RC): "JIS-Civil(RC)" · JTJ023-85(RC): "JTJ023-85(RC)" · Q/CR 9300-18(RC): "Q/CR 9300-18(RC)" · GB 50917-13(RC): "GB 50917-13(RC)" · GB/T10(RC): "GB/T10(RC)" · GB(RC): "GB(RC)" · GB-Civil(RC): "GB-Civil(RC)" · TB10092-17(RC): "TB10092-17(RC)" · JTG3362-18(RC): "JTG3362-18(RC)" · JTG04(RC): "JTG04(RC)" · TB05(RC): "TB05(RC)" · KS19(RC): "KS19(RC)" · KS01(RC): "KS01(RC)" · KS(RC): "KS(RC)" · KSCE-LSD15(RC): "KSCE-LSD15(RC)" · KS01-Civil(RC): "KS01-Civil(RC)" · KS-Civil(RC): "KS-Civil(RC)" · PNS49(RC): "PNS49(RC)" · SNI(RC): "SNI(RC)" · TIS(RC): "TIS(RC)" · TIS(MKS)(RC): "TIS(MKS)(RC)" · IRC(RC): "IRC(RC)" · IRS(RC): "IRS(RC)" · IS(RC): "IS(RC)" · CNS560-18(RC): "CNS560-18(RC)" · CNS560(RC): "CNS560(RC)" · CNS(RC): "CNS(RC)" · AS17(RC): "AS17(RC)" · TMH7(RC): "TMH7(RC)" · SP63.2018(RC): "SP63.2018(RC)" · TS(RC): "TS(RC)" · NBR 6118(RC): "NBR 6118(RC)" · TCVN2018(RC): "TCVN2018(RC)" · CSA-S6-25(RC): "CSA-S6-25(RC)" | `"CODE"` | string | - | **Required** |
| 2.2 | └ [When CODE = "ASTM19(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Grade 40 · Grade 60 · Grade 80 · Grade 100 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "ASTM19(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 40 · Grade 60 · Grade 80 · Grade 100 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "ASTM(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Grade 40 · Grade 50 · Grade 60 · Grade 75 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "ASTM(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 40 · Grade 50 · Grade 60 · Grade 75 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "U.S.C(US)(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Grade 40 · Grade 60 · Grade 75 · Grade 80 · Grade 100 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "U.S.C(US)(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 40 · Grade 60 · Grade 75 · Grade 80 · Grade 100 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "U.S.C(SI)(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Grade 280 · Grade 420 · Grade 520 · Grade 550 · Grade 690 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "U.S.C(SI)(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 280 · Grade 420 · Grade 520 · Grade 550 · Grade 690 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)", "NMX NTC-2017(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · Grade 42 · Grade 56 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)", "NMX NTC-2017(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 42 · Grade 56 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "CSA(RC)"] Grade of main rebar. Required when CODE is not 'None'. · 300R · 400R · 500R · 400W · 500W | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "CSA(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · 300R · 400R · 500R · 400W · 500W | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "BS(RC)"] Grade of main rebar. Required when CODE is not 'None'. · S250 · S460 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "BS(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · S250 · S460 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · Class A · Class B · Class C | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · Class A · Class B · Class C | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "EN(RC)"] Grade of main rebar. Required when CODE is not 'None'. · S220 · S250 · S300 · S400 · S460 · S500 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "EN(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · S220 · S250 · S300 · S400 · S460 · S500 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · B450C | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · B450C | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "UNI(RC)"] Grade of main rebar. Required when CODE is not 'None'. · FeB22k · FeB32k · FeB38k · FeB44k · B450C | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "UNI(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · FeB22k · FeB32k · FeB38k · FeB44k · B450C | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "GOST-SP(RC)"] Grade of main rebar. Required when CODE is not 'None'. · A240 · A300 · A400 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "GOST-SP(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · A240 · A300 · A400 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "GOST-SNIP(RC)"] Grade of main rebar. Required when CODE is not 'None'. · A-I · A-II · A-III | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "GOST-SNIP(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · A-I · A-II · A-III | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "JIS(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SR235 · SR295 · SD295A · SD295B · SD345 · SD390 · SD490 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "JIS(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SR235 · SR295 · SD295A · SD295B · SD345 · SD390 · SD490 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "JIS-Civil(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SR235 · SD295A · SD295B · SD345 · SD390 · SD490 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "JIS-Civil(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SR235 · SD295A · SD295B · SD345 · SD390 · SD490 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["JTJ023-85(RC)", "GB-Civil(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · Grade 1 · Grade 2 · Grade 3 · 5 Hao | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["JTJ023-85(RC)", "GB-Civil(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 1 · Grade 2 · Grade 3 · 5 Hao | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRB500 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRB500 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "GB 50917-13(RC)"] Grade of main rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 · HRBF500 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "GB 50917-13(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 · HRBF500 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "GB/T10(RC)"] Grade of main rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 · HRBF500 · RRB500 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "GB/T10(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 · HRBF500 · RRB500 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "GB(RC)"] Grade of main rebar. Required when CODE is not 'None'. · HPB235 · HRB335 · HRB400 · RRB400 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "GB(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · HPB235 · HRB335 · HRB400 · RRB400 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "JTG3362-18(RC)"] Grade of main rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "JTG3362-18(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "JTG04(RC)"] Grade of main rebar. Required when CODE is not 'None'. · R235 · HRB335 · HRB400 · KL400 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "JTG04(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · R235 · HRB335 · HRB400 · KL400 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "TB05(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Q235 · HRB335 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "TB05(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Q235 · HRB335 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "KS19(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SD300 · SD400 · SD500 · SD600 · SD700 · SD400S · SD500S · SD600S | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "KS19(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SD300 · SD400 · SD500 · SD600 · SD700 · SD400S · SD500S · SD600S | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["KS01(RC)", "KSCE-LSD15(RC)", "KS01-Civil(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · SD240 · SD300 · SD350 · SD400 · SD500 · SD600 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["KS01(RC)", "KSCE-LSD15(RC)", "KS01-Civil(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · SD240 · SD300 · SD350 · SD400 · SD500 · SD600 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · SD24 · SD30 · SD35 · SD40 · SD50 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · SD24 · SD30 · SD35 · SD40 · SD50 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "PNS49(RC)"] Grade of main rebar. Required when CODE is not 'None'. · 230R · 280R · 420R · 520R · 550R | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "PNS49(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · 230R · 280R · 420R · 520R · 550R | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "SNI(RC)"] Grade of main rebar. Required when CODE is not 'None'. · BjTP 280 · BjTS 280 · BjTS 420A · BjTS 420B · BjTS 520 · BjTS 550 · BjTS 700 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "SNI(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · BjTP 280 · BjTS 280 · BjTS 420A · BjTS 420B · BjTS 520 · BjTS 550 · BjTS 700 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · SR24 · SD30 · SD40 · SD50 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · SR24 · SD30 · SD40 · SD50 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["IRC(RC)", "IRS(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · Fe415 · Fe500 · Fe550 · Fe600 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["IRC(RC)", "IRS(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · Fe415 · Fe500 · Fe550 · Fe600 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "IS(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Fe240 · Fe250 · Fe415 · Fe500 · Fe550 · Fe600 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "IS(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Fe240 · Fe250 · Fe415 · Fe500 · Fe550 · Fe600 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "CNS560-18(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SD280 · SD280W · SD420 · SD420W · SD490W · SD550W · SD690 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "CNS560-18(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SD280 · SD280W · SD420 · SD420W · SD490W · SD550W · SD690 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "CNS560(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SR240 · SR300 · SD280 · SD280W · SD420 · SD420W · SD490 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "CNS560(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SR240 · SR300 · SD280 · SD280W · SD420 · SD420W · SD490 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "CNS(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SD24 · SD28 · SD30 · SD35 · SD42 · SD42W · SD50 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "CNS(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SD24 · SD28 · SD30 · SD35 · SD42 · SD42W · SD50 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "AS17(RC)"] Grade of main rebar. Required when CODE is not 'None'. · D500L · D500N · D500E · D500LP · D600N | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "AS17(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · D500L · D500N · D500E · D500LP · D600N | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "TMH7(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Type A · Type B · Type C | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "TMH7(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Type A · Type B · Type C | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "SP63.2018(RC)"] Grade of main rebar. Required when CODE is not 'None'. · A240 · A240_sw · A400 · A400_sw · A500 · A500_sw · A600 · A800 · A1000 · B500 · B500_sw · BP500 · BP1200 · BP1300 · BP1400 · BP1500 · BP1600 · K1400 · K1450 · K1500 · K1550 · K1650 · K1750 · K1850 · K1900 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "SP63.2018(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · A240 · A240_sw · A400 · A400_sw · A500 · A500_sw · A600 · A800 · A1000 · B500 · B500_sw · BP500 · BP1200 · BP1300 · BP1400 · BP1500 · BP1600 · K1400 · K1450 · K1500 · K1550 · K1650 · K1750 · K1850 · K1900 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "TS(RC)"] Grade of main rebar. Required when CODE is not 'None'. · B420C · B520C | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "TS(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · B420C · B520C | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "NBR 6118(RC)"] Grade of main rebar. Required when CODE is not 'None'. · CA25 · CA50 · CA60 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "NBR 6118(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · CA25 · CA50 · CA60 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "TCVN2018(RC)"] Grade of main rebar. Required when CODE is not 'None'. · CB300-V · CB400-V · CB500-V · CB600-V | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "TCVN2018(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · CB300-V · CB400-V · CB500-V · CB600-V | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "CSA-S6-25(RC)"] Grade of main rebar. Required when CODE is not 'None'. · 400W · 500W · 600W | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "CSA-S6-25(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · 400W · 500W · 600W | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.4 | └ [When CODE = "None"] User-defined main rebar name. Required when CODE is 'None'. | `"NAME_MAIN_REBAR"` | string | - | **Required** |
| 2.5 | └ [When CODE = "None"] User-defined sub-rebar name. Required when CODE is 'None'. | `"NAME_SUB_REBAR"` | string | - | **Required** |
| 2.6 | └ [When CODE = "None"] Yield strength of main rebar. User input is available when CODE is 'None'. · Minimum: 0 | `"Fy"` | number | - | **Required** |
| 2.7 | └ [When CODE = "None"] Yield strength of sub-rebar. User input is available when CODE is 'None'. · Minimum: 0 | `"Fys"` | number | - | **Required** |
| 3 | [General] Write the slab material (SLAB_MATL_PROP and SLAB_REBAR_PROP). Used only when the model has a composite PSC section; then both slab objects are required. If false or omitted, the stored slab data is kept | `"SLAB_PROP"` | boolean | false | Optional |
| 4 | [When SLAB_PROP = true] Slab Material Type | `"SLAB_MATL_PROP"` | object | - | **Required** |
| 4.1 | └ [When SLAB_PROP = true] Concrete design code. If CODE is 'None', enter a custom material NAME instead of selecting GRADE. · None: "None" · ASTM19(RC): "ASTM19(RC)" · ASTM(RC): "ASTM(RC)" · U.S.C(US)(RC): "U.S.C(US)(RC)" · U.S.C(SI)(RC): "U.S.C(SI)(RC)" · NMX2023(RC): "NMX2023(RC)" · NMX2023(MKS)(RC): "NMX2023(MKS)(RC)" · NMX NTC-2017(RC): "NMX NTC-2017(RC)" · CSA(RC): "CSA(RC)" · BS(RC): "BS(RC)" · EN04(RC): "EN04(RC)" · EN(RC): "EN(RC)" · NTC08(RC): "NTC08(RC)" · NTC12(RC): "NTC12(RC)" · NTC18(RC): "NTC18(RC)" · UNI(RC): "UNI(RC)" · SS(RC): "SS(RC)" · GOST-SP(RC): "GOST-SP(RC)" · GOST-SNIP(RC): "GOST-SNIP(RC)" · JIS(RC): "JIS(RC)" · JIS-Civil(RC): "JIS-Civil(RC)" · JTJ023-85(RC): "JTJ023-85(RC)" · Q/CR 9300-18(RC): "Q/CR 9300-18(RC)" · GB 50917-13(RC): "GB 50917-13(RC)" · GB/T10(RC): "GB/T10(RC)" · GB(RC): "GB(RC)" · GB-Civil(RC): "GB-Civil(RC)" · TB10092-17(RC): "TB10092-17(RC)" · JTG3362-18(RC): "JTG3362-18(RC)" · JTG04(RC): "JTG04(RC)" · TB05(RC): "TB05(RC)" · KS19(RC): "KS19(RC)" · KS01(RC): "KS01(RC)" · KS(RC): "KS(RC)" · KSCE-LSD15(RC): "KSCE-LSD15(RC)" · KS01-Civil(RC): "KS01-Civil(RC)" · KS-Civil(RC): "KS-Civil(RC)" · PNS49(RC): "PNS49(RC)" · SNI(RC): "SNI(RC)" · TIS(RC): "TIS(RC)" · TIS(MKS)(RC): "TIS(MKS)(RC)" · IRC(RC): "IRC(RC)" · IRS(RC): "IRS(RC)" · IS(RC): "IS(RC)" · CNS560-18(RC): "CNS560-18(RC)" · CNS560(RC): "CNS560(RC)" · CNS(RC): "CNS(RC)" · AS17(RC): "AS17(RC)" · TMH7(RC): "TMH7(RC)" · SP63.2018(RC): "SP63.2018(RC)" · TS(RC): "TS(RC)" · NBR 6118(RC): "NBR 6118(RC)" · TCVN2018(RC): "TCVN2018(RC)" · CSA-S6-25(RC): "CSA-S6-25(RC)" | `"CODE"` | string | - | **Required** |
| 4.2 | └ [When CODE = "None"] User-defined concrete material name. Used only when CODE is 'None'. | `"NAME"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["ASTM19(RC)", "ASTM(RC)", "U.S.C(US)(RC)"]] Concrete material grade. Required when CODE is not 'None'. · Grade C2500 · Grade C3000 · Grade C3500 · Grade C4000 · Grade C4500 · Grade C5000 · Grade C6000 · Grade C7000 · Grade C8000 · Grade C9000 · Grade C10000 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["U.S.C(SI)(RC)", "PNS49(RC)"]] Concrete material grade. Required when CODE is not 'None'. · Grade C18 · Grade C21 · Grade C25 · Grade C28 · Grade C32 · Grade C35 · Grade C42 · Grade C49 · Grade C56 · Grade C63 · Grade C69 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)"]] Concrete material grade. Required when CODE is not 'None'. · 250-C1A(C) · 250-C1A(B) · 300-C1A(C) · 300-C1A(B) · 350-C1A(C) · 350-C1A(B) · 400-C1B(C) · 400-C1B(B) · 450-C1B(C) · 450-C1B(B) · 500-C1B(C) · 500-C1B(B) · 550-C1B(C) · 550-C1B(B) · 600-C1B(C) · 600-C1B(B) · 650-C1B(C) · 650-C1B(B) · 700-C1B(C) · 700-C1B(B) · 200-C2 · 250-C2 · 300-C2 · 350-C2 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "NMX NTC-2017(RC)"] Concrete material grade. Required when CODE is not 'None'. · 200-C1C · 250-C1C · 300-C1C · 350-C1C · 400-C1C · 450-C1C · 500-C1C · 550-C1C · 600-C1C · 650-C1C · 700-C1C · 750-C1C · 800-C1C · 200-C1B · 250-C1B · 300-C1B · 350-C1B · 400-C1B · 450-C1B · 500-C1B · 550-C1B · 600-C1B · 650-C1B · 700-C1B · 750-C1B · 800-C1B · 150-C2 · 200-C2 · 250-C2 · 300-C2 · 400-C2 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "CSA(RC)"] Concrete material grade. Required when CODE is not 'None'. · C25 · C30 · C35 · C40 · C45 · C50 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "BS(RC)"] Concrete material grade. Required when CODE is not 'None'. · C15 · C20 · C25 · C30 · C35 · C40 · C45 · C50 · C55 · C60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Concrete material grade. Required when CODE is not 'None'. · C12/15 · C16/20 · C20/25 · C25/30 · C30/37 · C32/40 · C35/45 · C40/50 · C45/55 · C50/60 · C55/67 · C60/75 · C70/85 · C80/95 · C90/105 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "EN(RC)"] Concrete material grade. Required when CODE is not 'None'. · C12/15 · C16/20 · C20/25 · C25/30 · C30/37 · C35/45 · C40/50 · C45/55 · C50/60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Concrete material grade. Required when CODE is not 'None'. · C8/10 · C12/15 · C16/20 · C20/25 · C25/30 · C28/35 · C30/37 · C32/40 · C35/45 · C40/50 · C45/55 · C50/60 · C55/67 · C60/75 · C70/85 · C80/95 · C90/105 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "UNI(RC)"] Concrete material grade. Required when CODE is not 'None'. · Rck10 · Rck15 · Rck20 · Rck25 · Rck30 · Rck35 · Rck40 · Rck45 · Rck50 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["GOST-SP(RC)", "GOST-SNIP(RC)"]] Concrete material grade. Required when CODE is not 'None'. · B20 · B22.5 · B25 · B27.5 · B30 · B35 · B40 · B45 · B50 · B55 · B60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "JIS(RC)"] Concrete material grade. Required when CODE is not 'None'. · Fc18 · Fc21 · Fc24 · Fc27 · Fc30 · Fc33 · Fc36 · Fc39 · Fc42 · Fc45 · Fc48 · Fc51 · Fc54 · Fc57 · Fc60 · Fc18(LT1) · Fc21(LT1) · Fc24(LT1) · Fc27(LT1) · Fc30(LT1) · Fc33(LT1) · Fc36(LT1) · Fc18(LT2) · Fc21(LT2) · Fc24(LT2) · Fc27(LT2) | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "JIS-Civil(RC)"] Concrete material grade. Required when CODE is not 'None'. · Fc21 · Fc24 · Fc27 · Fc30 · Fc36 · Fc40 · Fc50 · Fc60 · Fc70 · Fc80 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "JTJ023-85(RC)"] Concrete material grade. Required when CODE is not 'None'. · C15 · C20 · C25 · C30 · C40 · C50 · C60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Concrete material grade. Required when CODE is not 'None'. · C25 · C30 · C35 · C40 · C45 · C50 · C55 · C60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "GB 50917-13(RC)"] Concrete material grade. Required when CODE is not 'None'. · C30 · C35 · C40 · C45 · C50 · C55 · C60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["GB/T10(RC)", "GB(RC)", "JTG04(RC)"]] Concrete material grade. Required when CODE is not 'None'. · C15 · C20 · C25 · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "GB-Civil(RC)"] Concrete material grade. Required when CODE is not 'None'. · 15 · 20 · 25 · 30 · 40 · 50 · 60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "JTG3362-18(RC)"] Concrete material grade. Required when CODE is not 'None'. · C25 · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "TB05(RC)"] Concrete material grade. Required when CODE is not 'None'. · C20 · C25 · C30 · C35 · C40 · C45 · C50 · C55 · C60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["KS19(RC)", "KS01(RC)", "KS01-Civil(RC)"]] Concrete material grade. Required when CODE is not 'None'. · C15 · C18 · C21 · C24 · C27 · C30 · C35 · C40 · C45 · C49 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 · C90 · C95 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Concrete material grade. Required when CODE is not 'None'. · C150 · C180 · C210 · C240 · C270 · C300 · C350 · C400 · C450 · C500 · C550 · C600 · C650 · C700 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "KSCE-LSD15(RC)"] Concrete material grade. Required when CODE is not 'None'. · C15 · C18 · C21 · C24 · C27 · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 · C90 · C95 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "SNI(RC)"] Concrete material grade. Required when CODE is not 'None'. · fc17 · fc21 · fc25 · fc30 · fc35 · fc40 · fc45 · fc50 · fc55 · fc60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Concrete material grade. Required when CODE is not 'None'. · C150 · C180 · C210 · C240 · C250 · C280 · C300 · C320 · C350 · C380 · C400 · C450 · C500 · C550 · C600 · C650 · C700 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "IRC(RC)"] Concrete material grade. Required when CODE is not 'None'. · M15 · M20 · M25 · M30 · M35 · M40 · M45 · M50 · M55 · M60 · M65 · M70 · M75 · M80 · M85 · M90 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "IRS(RC)"] Concrete material grade. Required when CODE is not 'None'. · M20 · M25 · M30 · M35 · M40 · M45 · M50 · M55 · M60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "IS(RC)"] Concrete material grade. Required when CODE is not 'None'. · M10 · M15 · M20 · M25 · M30 · M35 · M40 · M45 · M50 · M55 · M60 · M65 · M70 · M75 · M80 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "CNS560-18(RC)"] Concrete material grade. Required when CODE is not 'None'. · C210 · C245 · C280 · C315 · C350 · C420 · C490 · C560 · C700 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["CNS560(RC)", "CNS(RC)"]] Concrete material grade. Required when CODE is not 'None'. · C210 · C245 · C280 · C315 · C350 · C420 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "AS17(RC)"] Concrete material grade. Required when CODE is not 'None'. · C20 · C25 · C32 · C40 · C50 · C65 · C80 · C100 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "TMH7(RC)"] Concrete material grade. Required when CODE is not 'None'. · Grade 20 · Grade 25 · Grade 30 · Grade 40 · Grade 50 · Grade 60 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "SP63.2018(RC)"] Concrete material grade. Required when CODE is not 'None'. · B3.5 · B5 · B7.5 · B10 · B12.5 · B15 · B20 · B25 · B30 · B35 · B40 · B45 · B50 · B55 · B60 · B70 · B80 · B90 · B100 · B3.5A · B5A · B7.5A · B10A · B12.5A · B15A · B20A · B25A · B30A · B35A · B40A · B15B · B20B · B25B · B30B · B35B · B40B · B45B · B50B · B55B · B60B · LB2.5D800 · LB3.5D800 · LB5D800 · LB7.5D800 · LB2.5D1000 · LB3.5D1000 · LB5D1000 · LB7.5D1000 · LB10D1000 · LB12.5D1000 · LB2.5D1200 · LB3.5D1200 · LB5D1200 · LB7.5D1200 · LB10D1200 · LB12.5D1200 · LB15D1200 · LB2.5D1400 · LB3.5D1400 · LB5D1400 · LB7.5D1400 · LB10D1400 · LB12.5D1400 · LB15D1400 · LB20D1400 · LB25D1400 · LB30D1400 · LB3.5D1600 · LB5D1600 · LB7.5D1600 · LB10D1600 · LB12.5D1600 · LB15D1600 · LB20D1600 · LB25D1600 · LB30D1600 · LB35D1600 · LB5D1800 · LB7.5D1800 · LB10D1800 · LB12.5D1800 · LB15D1800 · LB20D1800 · LB25D1800 · LB30D1800 · LB35D1800 · LB40D1800 · LB7.5D2000 · LB10D2000 · LB12.5D2000 · LB15D2000 · LB20D2000 · LB25D2000 · LB30D2000 · LB35D2000 · LB40D2000 · CB1.5D500 · CB1.5D600 · CB2D600 · CB2.5D600 · CB1.5D700 · CB2D700 · CB2.5D700 · CB3.5D700 · CB2.5D800 · CB3.5D800 · CB5D800 · CB3.5D900 · CB5D900 · CB7.5D900 · CB5D1000 · CB7.5D1000 · CB10D1000 · CB7.5D1100 · CB10D1100 · CB12.5D1100 · CB15D1100 · CB10D1200 · CB12.5D1200 · CB15D1200 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "TS(RC)"] Concrete material grade. Required when CODE is not 'None'. · C16 · C18 · C20 · C25 · C30 · C35 · C40 · C45 · C50 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "NBR 6118(RC)"] Concrete material grade. Required when CODE is not 'None'. · C20BD · C20GG · C20LS · C20SS · C25BD · C25GG · C25LS · C25SS · C30BD · C30GG · C30LS · C30SS · C35BD · C35GG · C35LS · C35SS · C40BD · C40GG · C40LS · C40SS · C45BD · C45GG · C45LS · C45SS · C50BD · C50GG · C50LS · C50SS · C55BD · C55GG · C55LS · C55SS · C60BD · C60GG · C60LS · C60SS · C65BD · C65GG · C65LS · C65SS · C70BD · C70GG · C70LS · C70SS · C75BD · C75GG · C75LS · C75SS · C80BD · C80GG · C80LS · C80SS · C85BD · C85GG · C85LS · C85SS · C90BD · C90GG · C90LS · C90SS | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "TCVN2018(RC)"] Concrete material grade. Required when CODE is not 'None'. · B3.5 · B5 · B7.5 · B10 · B12.5 · B15 · B20 · B25 · B30 · B35 · B40 · B45 · B50 · B55 · B60 · B70 · B80 · B90 · B100 | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "CSA-S6-25(RC)"] Concrete material grade. Required when CODE is not 'None'. · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 | `"GRADE"` | string | - | **Required** |
| 4.4 | └ [When CODE = "None"] Specified Compressive Strength (f'c). When CODE is 'None', user input is required. When CODE is a design code, this value can be auto-filled from the selected CODE and GRADE. | `"COMP_STRENGTH"` | number | - | **Required** |
| 4.5 | └ [When CODE = "None"] Light Weight Concrete Factor option. | `"LIGHT_WEIGHT_FACTOR"` | boolean | - | Optional |
| 4.6 | └ [When LIGHT_WEIGHT_FACTOR = true] Light Weight Factor value. Required when LIGHT_WEIGHT_FACTOR is true. · Range: 0.75~1 | `"FACTOR_VALUE"` | number | 1 | **Required** |
| 5 | Slab Rebar Selection | `"SLAB_REBAR_PROP"` | object | - | **Required** |
| 5.1 | └ Rebar design code. If CODE is 'None', input custom rebar names, Fy and Fys directly instead of selecting GRADE_MAIN_REBAR and GRADE_SUB_REBAR. · None: "None" · ASTM19(RC): "ASTM19(RC)" · ASTM(RC): "ASTM(RC)" · U.S.C(US)(RC): "U.S.C(US)(RC)" · U.S.C(SI)(RC): "U.S.C(SI)(RC)" · NMX2023(RC): "NMX2023(RC)" · NMX2023(MKS)(RC): "NMX2023(MKS)(RC)" · NMX NTC-2017(RC): "NMX NTC-2017(RC)" · CSA(RC): "CSA(RC)" · BS(RC): "BS(RC)" · EN04(RC): "EN04(RC)" · EN(RC): "EN(RC)" · NTC08(RC): "NTC08(RC)" · NTC12(RC): "NTC12(RC)" · NTC18(RC): "NTC18(RC)" · UNI(RC): "UNI(RC)" · SS(RC): "SS(RC)" · GOST-SP(RC): "GOST-SP(RC)" · GOST-SNIP(RC): "GOST-SNIP(RC)" · JIS(RC): "JIS(RC)" · JIS-Civil(RC): "JIS-Civil(RC)" · JTJ023-85(RC): "JTJ023-85(RC)" · Q/CR 9300-18(RC): "Q/CR 9300-18(RC)" · GB 50917-13(RC): "GB 50917-13(RC)" · GB/T10(RC): "GB/T10(RC)" · GB(RC): "GB(RC)" · GB-Civil(RC): "GB-Civil(RC)" · TB10092-17(RC): "TB10092-17(RC)" · JTG3362-18(RC): "JTG3362-18(RC)" · JTG04(RC): "JTG04(RC)" · TB05(RC): "TB05(RC)" · KS19(RC): "KS19(RC)" · KS01(RC): "KS01(RC)" · KS(RC): "KS(RC)" · KSCE-LSD15(RC): "KSCE-LSD15(RC)" · KS01-Civil(RC): "KS01-Civil(RC)" · KS-Civil(RC): "KS-Civil(RC)" · PNS49(RC): "PNS49(RC)" · SNI(RC): "SNI(RC)" · TIS(RC): "TIS(RC)" · TIS(MKS)(RC): "TIS(MKS)(RC)" · IRC(RC): "IRC(RC)" · IRS(RC): "IRS(RC)" · IS(RC): "IS(RC)" · CNS560-18(RC): "CNS560-18(RC)" · CNS560(RC): "CNS560(RC)" · CNS(RC): "CNS(RC)" · AS17(RC): "AS17(RC)" · TMH7(RC): "TMH7(RC)" · SP63.2018(RC): "SP63.2018(RC)" · TS(RC): "TS(RC)" · NBR 6118(RC): "NBR 6118(RC)" · TCVN2018(RC): "TCVN2018(RC)" · CSA-S6-25(RC): "CSA-S6-25(RC)" | `"CODE"` | string | - | **Required** |
| 5.2 | └ [When CODE = "ASTM19(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Grade 40 · Grade 60 · Grade 80 · Grade 100 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "ASTM19(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 40 · Grade 60 · Grade 80 · Grade 100 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "ASTM(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Grade 40 · Grade 50 · Grade 60 · Grade 75 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "ASTM(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 40 · Grade 50 · Grade 60 · Grade 75 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "U.S.C(US)(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Grade 40 · Grade 60 · Grade 75 · Grade 80 · Grade 100 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "U.S.C(US)(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 40 · Grade 60 · Grade 75 · Grade 80 · Grade 100 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "U.S.C(SI)(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Grade 280 · Grade 420 · Grade 520 · Grade 550 · Grade 690 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "U.S.C(SI)(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 280 · Grade 420 · Grade 520 · Grade 550 · Grade 690 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)", "NMX NTC-2017(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · Grade 42 · Grade 56 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)", "NMX NTC-2017(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 42 · Grade 56 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "CSA(RC)"] Grade of main rebar. Required when CODE is not 'None'. · 300R · 400R · 500R · 400W · 500W | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "CSA(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · 300R · 400R · 500R · 400W · 500W | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "BS(RC)"] Grade of main rebar. Required when CODE is not 'None'. · S250 · S460 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "BS(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · S250 · S460 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · Class A · Class B · Class C | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · Class A · Class B · Class C | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "EN(RC)"] Grade of main rebar. Required when CODE is not 'None'. · S220 · S250 · S300 · S400 · S460 · S500 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "EN(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · S220 · S250 · S300 · S400 · S460 · S500 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · B450C | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · B450C | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "UNI(RC)"] Grade of main rebar. Required when CODE is not 'None'. · FeB22k · FeB32k · FeB38k · FeB44k · B450C | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "UNI(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · FeB22k · FeB32k · FeB38k · FeB44k · B450C | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "GOST-SP(RC)"] Grade of main rebar. Required when CODE is not 'None'. · A240 · A300 · A400 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "GOST-SP(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · A240 · A300 · A400 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "GOST-SNIP(RC)"] Grade of main rebar. Required when CODE is not 'None'. · A-I · A-II · A-III | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "GOST-SNIP(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · A-I · A-II · A-III | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "JIS(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SR235 · SR295 · SD295A · SD295B · SD345 · SD390 · SD490 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "JIS(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SR235 · SR295 · SD295A · SD295B · SD345 · SD390 · SD490 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "JIS-Civil(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SR235 · SD295A · SD295B · SD345 · SD390 · SD490 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "JIS-Civil(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SR235 · SD295A · SD295B · SD345 · SD390 · SD490 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["JTJ023-85(RC)", "GB-Civil(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · Grade 1 · Grade 2 · Grade 3 · 5 Hao | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["JTJ023-85(RC)", "GB-Civil(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · Grade 1 · Grade 2 · Grade 3 · 5 Hao | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRB500 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRB500 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "GB 50917-13(RC)"] Grade of main rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 · HRBF500 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "GB 50917-13(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 · HRBF500 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "GB/T10(RC)"] Grade of main rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 · HRBF500 · RRB500 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "GB/T10(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 · HRBF500 · RRB500 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "GB(RC)"] Grade of main rebar. Required when CODE is not 'None'. · HPB235 · HRB335 · HRB400 · RRB400 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "GB(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · HPB235 · HRB335 · HRB400 · RRB400 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "JTG3362-18(RC)"] Grade of main rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "JTG3362-18(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · HPB300 · HRB400 · HRBF400 · RRB400 · HRB500 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "JTG04(RC)"] Grade of main rebar. Required when CODE is not 'None'. · R235 · HRB335 · HRB400 · KL400 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "JTG04(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · R235 · HRB335 · HRB400 · KL400 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "TB05(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Q235 · HRB335 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "TB05(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Q235 · HRB335 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "KS19(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SD300 · SD400 · SD500 · SD600 · SD700 · SD400S · SD500S · SD600S | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "KS19(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SD300 · SD400 · SD500 · SD600 · SD700 · SD400S · SD500S · SD600S | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["KS01(RC)", "KSCE-LSD15(RC)", "KS01-Civil(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · SD240 · SD300 · SD350 · SD400 · SD500 · SD600 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["KS01(RC)", "KSCE-LSD15(RC)", "KS01-Civil(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · SD240 · SD300 · SD350 · SD400 · SD500 · SD600 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · SD24 · SD30 · SD35 · SD40 · SD50 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · SD24 · SD30 · SD35 · SD40 · SD50 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "PNS49(RC)"] Grade of main rebar. Required when CODE is not 'None'. · 230R · 280R · 420R · 520R · 550R | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "PNS49(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · 230R · 280R · 420R · 520R · 550R | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "SNI(RC)"] Grade of main rebar. Required when CODE is not 'None'. · BjTP 280 · BjTS 280 · BjTS 420A · BjTS 420B · BjTS 520 · BjTS 550 · BjTS 700 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "SNI(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · BjTP 280 · BjTS 280 · BjTS 420A · BjTS 420B · BjTS 520 · BjTS 550 · BjTS 700 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · SR24 · SD30 · SD40 · SD50 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · SR24 · SD30 · SD40 · SD50 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["IRC(RC)", "IRS(RC)"]] Grade of main rebar. Required when CODE is not 'None'. · Fe415 · Fe500 · Fe550 · Fe600 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["IRC(RC)", "IRS(RC)"]] Grade of sub-rebar. Required when CODE is not 'None'. · Fe415 · Fe500 · Fe550 · Fe600 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "IS(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Fe240 · Fe250 · Fe415 · Fe500 · Fe550 · Fe600 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "IS(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Fe240 · Fe250 · Fe415 · Fe500 · Fe550 · Fe600 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "CNS560-18(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SD280 · SD280W · SD420 · SD420W · SD490W · SD550W · SD690 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "CNS560-18(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SD280 · SD280W · SD420 · SD420W · SD490W · SD550W · SD690 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "CNS560(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SR240 · SR300 · SD280 · SD280W · SD420 · SD420W · SD490 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "CNS560(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SR240 · SR300 · SD280 · SD280W · SD420 · SD420W · SD490 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "CNS(RC)"] Grade of main rebar. Required when CODE is not 'None'. · SD24 · SD28 · SD30 · SD35 · SD42 · SD42W · SD50 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "CNS(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · SD24 · SD28 · SD30 · SD35 · SD42 · SD42W · SD50 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "AS17(RC)"] Grade of main rebar. Required when CODE is not 'None'. · D500L · D500N · D500E · D500LP · D600N | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "AS17(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · D500L · D500N · D500E · D500LP · D600N | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "TMH7(RC)"] Grade of main rebar. Required when CODE is not 'None'. · Type A · Type B · Type C | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "TMH7(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · Type A · Type B · Type C | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "SP63.2018(RC)"] Grade of main rebar. Required when CODE is not 'None'. · A240 · A240_sw · A400 · A400_sw · A500 · A500_sw · A600 · A800 · A1000 · B500 · B500_sw · BP500 · BP1200 · BP1300 · BP1400 · BP1500 · BP1600 · K1400 · K1450 · K1500 · K1550 · K1650 · K1750 · K1850 · K1900 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "SP63.2018(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · A240 · A240_sw · A400 · A400_sw · A500 · A500_sw · A600 · A800 · A1000 · B500 · B500_sw · BP500 · BP1200 · BP1300 · BP1400 · BP1500 · BP1600 · K1400 · K1450 · K1500 · K1550 · K1650 · K1750 · K1850 · K1900 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "TS(RC)"] Grade of main rebar. Required when CODE is not 'None'. · B420C · B520C | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "TS(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · B420C · B520C | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "NBR 6118(RC)"] Grade of main rebar. Required when CODE is not 'None'. · CA25 · CA50 · CA60 | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "NBR 6118(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · CA25 · CA50 · CA60 | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "TCVN2018(RC)"] Grade of main rebar. Required when CODE is not 'None'. · CB300-V · CB400-V · CB500-V · CB600-V | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "TCVN2018(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · CB300-V · CB400-V · CB500-V · CB600-V | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "CSA-S6-25(RC)"] Grade of main rebar. Required when CODE is not 'None'. · 400W · 500W · 600W | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "CSA-S6-25(RC)"] Grade of sub-rebar. Required when CODE is not 'None'. · 400W · 500W · 600W | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.4 | └ [When CODE = "None"] User-defined main rebar name. Required when CODE is 'None'. | `"NAME_MAIN_REBAR"` | string | - | **Required** |
| 5.5 | └ [When CODE = "None"] User-defined sub-rebar name. Required when CODE is 'None'. | `"NAME_SUB_REBAR"` | string | - | **Required** |
| 5.6 | └ [When CODE = "None"] Yield strength of main rebar. User input is available when CODE is 'None'. · Minimum: 0 | `"Fy"` | number | - | **Required** |
| 5.7 | └ [When CODE = "None"] Yield strength of sub-rebar. User input is available when CODE is 'None'. · Minimum: 0 | `"Fys"` | number | - | **Required** |

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
          "additionalProperties": false,
          "properties": {
            "GIRDER_MATL_PROP": {
              "type": "object",
              "description": "Girder Material Type",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
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
                    "TCVN2018(RC)",
                    "CSA-S6-25(RC)"
                  ]
                },
                "NAME": {
                  "type": "string",
                  "minLength": 1
                },
                "GRADE": {
                  "type": "string"
                },
                "COMP_STRENGTH": {
                  "type": "number"
                },
                "LIGHT_WEIGHT_FACTOR": {
                  "type": "boolean",
                  "description": "Light Weight Concrete Factor option."
                },
                "FACTOR_VALUE": {
                  "type": "number",
                  "description": "Light Weight Factor value. Required when LIGHT_WEIGHT_FACTOR is true.",
                  "minimum": 0.75,
                  "maximum": 1,
                  "visibleWhen": {
                    "LIGHT_WEIGHT_FACTOR": true
                  }
                }
              }
            },
            "GIRDER_REBAR_PROP": {
              "type": "object",
              "description": "Girder Rebar Selection",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Rebar design code. If CODE is 'None', input custom rebar names, Fy and Fys directly instead of selecting GRADE_MAIN_REBAR and GRADE_SUB_REBAR.",
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
                    "TCVN2018(RC)",
                    "CSA-S6-25(RC)"
                  ]
                },
                "GRADE_MAIN_REBAR": {
                  "type": "string",
                  "description": "Grade of main rebar. Required when CODE is not 'None'."
                },
                "GRADE_SUB_REBAR": {
                  "type": "string",
                  "description": "Grade of sub-rebar. Required when CODE is not 'None'."
                },
                "NAME_MAIN_REBAR": {
                  "type": "string",
                  "description": "User-defined main rebar name. Required when CODE is 'None'.",
                  "minLength": 1
                },
                "NAME_SUB_REBAR": {
                  "type": "string",
                  "description": "User-defined sub-rebar name. Required when CODE is 'None'.",
                  "minLength": 1
                },
                "Fy": {
                  "type": "number",
                  "description": "Yield strength of main rebar. User input is available when CODE is 'None'.",
                  "minimum": 0
                },
                "Fys": {
                  "type": "number",
                  "description": "Yield strength of sub-rebar. User input is available when CODE is 'None'.",
                  "minimum": 0
                }
              }
            },
            "SLAB_PROP": {
              "type": "boolean",
              "default": false,
              "description": "Write the slab material (SLAB_MATL_PROP and SLAB_REBAR_PROP). Used only when the model has a composite PSC section; then both slab objects are required. If false or omitted, the stored slab data is kept"
            },
            "SLAB_MATL_PROP": {
              "type": "object",
              "description": "Slab Material Type",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Concrete design code. If CODE is 'None', enter a custom material NAME instead of selecting GRADE.",
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
                    "TCVN2018(RC)",
                    "CSA-S6-25(RC)"
                  ]
                },
                "NAME": {
                  "type": "string",
                  "description": "User-defined concrete material name. Used only when CODE is 'None'.",
                  "minLength": 1
                },
                "GRADE": {
                  "type": "string",
                  "description": "Concrete material grade. Required when CODE is not 'None'."
                },
                "COMP_STRENGTH": {
                  "type": "number",
                  "description": "Specified Compressive Strength (f'c). When CODE is 'None', user input is required. When CODE is a design code, this value can be auto-filled from the selected CODE and GRADE."
                },
                "LIGHT_WEIGHT_FACTOR": {
                  "type": "boolean",
                  "description": "Light Weight Concrete Factor option."
                },
                "FACTOR_VALUE": {
                  "type": "number",
                  "description": "Light Weight Factor value. Required when LIGHT_WEIGHT_FACTOR is true.",
                  "minimum": 0.75,
                  "maximum": 1,
                  "default": 1,
                  "visibleWhen": {
                    "LIGHT_WEIGHT_FACTOR": true
                  }
                }
              }
            },
            "SLAB_REBAR_PROP": {
              "type": "object",
              "description": "Slab Rebar Selection",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Rebar design code. If CODE is 'None', input custom rebar names, Fy and Fys directly instead of selecting GRADE_MAIN_REBAR and GRADE_SUB_REBAR.",
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
                    "TCVN2018(RC)",
                    "CSA-S6-25(RC)"
                  ]
                },
                "GRADE_MAIN_REBAR": {
                  "type": "string",
                  "description": "Grade of main rebar. Required when CODE is not 'None'."
                },
                "GRADE_SUB_REBAR": {
                  "type": "string",
                  "description": "Grade of sub-rebar. Required when CODE is not 'None'."
                },
                "NAME_MAIN_REBAR": {
                  "type": "string",
                  "description": "User-defined main rebar name. Required when CODE is 'None'.",
                  "minLength": 1
                },
                "NAME_SUB_REBAR": {
                  "type": "string",
                  "description": "User-defined sub-rebar name. Required when CODE is 'None'.",
                  "minLength": 1
                },
                "Fy": {
                  "type": "number",
                  "description": "Yield strength of main rebar. User input is available when CODE is 'None'.",
                  "minimum": 0
                },
                "Fys": {
                  "type": "number",
                  "description": "Yield strength of sub-rebar. User input is available when CODE is 'None'.",
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

- `MATD_PSC_ITEM`

### 부속 Schema — Concrete Material

**원문** [영문 58043328695705](https://support.midasuser.com/hc/en-us/articles/58043328695705)

`GIRDER_MATL_PROP`와 `SLAB_MATL_PROP`에 쓰는 공식 재료 설정 부속 Schema입니다.

> ⚠️ 부속 글의 Input URI에는 `{base url} +`만 표시되어 있습니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Map of keyed objects where each key is a string identifier. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Code · None: "None" · ASTM19(RC): "ASTM19(RC)" · ASTM(RC): "ASTM(RC)" · U.S.C(US)(RC): "U.S.C(US)(RC)" · U.S.C(SI)(RC): "U.S.C(SI)(RC)" · NMX2023(RC): "NMX2023(RC)" · NMX2023(MKS)(RC): "NMX2023(MKS)(RC)" · NMX NTC-2017(RC): "NMX NTC-2017(RC)" · CSA(RC): "CSA(RC)" · BS(RC): "BS(RC)" · EN04(RC): "EN04(RC)" · EN(RC): "EN(RC)" · NTC08(RC): "NTC08(RC)" · NTC12(RC): "NTC12(RC)" · NTC18(RC): "NTC18(RC)" · UNI(RC): "UNI(RC)" · SS(RC): "SS(RC)" · GOST-SP(RC): "GOST-SP(RC)" · GOST-SNIP(RC): "GOST-SNIP(RC)" · JIS(RC): "JIS(RC)" · JIS-Civil(RC): "JIS-Civil(RC)" · JTJ023-85(RC): "JTJ023-85(RC)" · Q/CR 9300-18(RC): "Q/CR 9300-18(RC)" · GB 50917-13(RC): "GB 50917-13(RC)" · GB/T10(RC): "GB/T10(RC)" · GB(RC): "GB(RC)" · GB-Civil(RC): "GB-Civil(RC)" · TB10092-17(RC): "TB10092-17(RC)" · JTG3362-18(RC): "JTG3362-18(RC)" · JTG04(RC): "JTG04(RC)" · TB05(RC): "TB05(RC)" · KS19(RC): "KS19(RC)" · KS01(RC): "KS01(RC)" · KS(RC): "KS(RC)" · KSCE-LSD15(RC): "KSCE-LSD15(RC)" · KS01-Civil(RC): "KS01-Civil(RC)" · KS-Civil(RC): "KS-Civil(RC)" · PNS49(RC): "PNS49(RC)" · SNI(RC): "SNI(RC)" · TIS(RC): "TIS(RC)" · TIS(MKS)(RC): "TIS(MKS)(RC)" · IRC(RC): "IRC(RC)" · IRS(RC): "IRS(RC)" · IS(RC): "IS(RC)" · CNS560-18(RC): "CNS560-18(RC)" · CNS560(RC): "CNS560(RC)" · CNS(RC): "CNS(RC)" · AS17(RC): "AS17(RC)" · TMH7(RC): "TMH7(RC)" · SP63.2018(RC): "SP63.2018(RC)" · TS(RC): "TS(RC)" · NBR 6118(RC): "NBR 6118(RC)" | `"CODE"` | string | - | **Required** |
| 2 | [General] Light Weight Concrete Factor | `"LIGHT_WEIGHT_FACTOR"` | boolean | - | Optional |
| 3 | [When "LIGHT_WEIGHT_FACTOR" is true] Light Weight Factor Value Constraints: · Value Range: >= 0.75, <= 1 | `"FACTOR_VALUE"` | number | 1 | **Required** |
| 4 | [When "CODE" is None] Name Constraints: · Length: min 1 | `"NAME"` | string | - | **Required** |
| 5 | [When "CODE" is None] Specified Compressive Strength (fc\|fck) | `"COMP_STRENGTH"` | number | - | **Required** |
| 6 | [When "CODE" is ASTM19(RC)] Grade · Grade C2500: "Grade C2500" · Grade C3000: "Grade C3000" · Grade C3500: "Grade C3500" · Grade C4000: "Grade C4000" · Grade C4500: "Grade C4500" · Grade C5000: "Grade C5000" · Grade C6000: "Grade C6000" · Grade C7000: "Grade C7000" · Grade C8000: "Grade C8000" · Grade C9000: "Grade C9000" · Grade C10000: "Grade C10000" | `"GRADE"` | string | - | **Required** |
| 7 | [When "CODE" is ASTM(RC)] Grade · Grade C2500: "Grade C2500" · Grade C3000: "Grade C3000" · Grade C3500: "Grade C3500" · Grade C4000: "Grade C4000" · Grade C4500: "Grade C4500" · Grade C5000: "Grade C5000" · Grade C6000: "Grade C6000" · Grade C7000: "Grade C7000" · Grade C8000: "Grade C8000" · Grade C9000: "Grade C9000" · Grade C10000: "Grade C10000" | `"GRADE"` | string | - | **Required** |
| 8 | [When "CODE" is U.S.C(US)(RC)] Grade · Grade C2500: "Grade C2500" · Grade C3000: "Grade C3000" · Grade C3500: "Grade C3500" · Grade C4000: "Grade C4000" · Grade C4500: "Grade C4500" · Grade C5000: "Grade C5000" · Grade C6000: "Grade C6000" · Grade C7000: "Grade C7000" · Grade C8000: "Grade C8000" · Grade C9000: "Grade C9000" · Grade C10000: "Grade C10000" | `"GRADE"` | string | - | **Required** |
| 9 | [When "CODE" is U.S.C(SI)(RC)] Grade · Grade C18: "Grade C18" · Grade C21: "Grade C21" · Grade C25: "Grade C25" · Grade C28: "Grade C28" · Grade C32: "Grade C32" · Grade C35: "Grade C35" · Grade C42: "Grade C42" · Grade C49: "Grade C49" · Grade C56: "Grade C56" · Grade C63: "Grade C63" · Grade C69: "Grade C69" | `"GRADE"` | string | - | **Required** |
| 10 | [When "CODE" is NMX2023(RC)] Grade · 250-C1A(C): "250-C1A(C)" · 250-C1A(B): "250-C1A(B)" · 300-C1A(C): "300-C1A(C)" · 300-C1A(B): "300-C1A(B)" · 350-C1A(C): "350-C1A(C)" · 350-C1A(B): "350-C1A(B)" · 400-C1B(C): "400-C1B(C)" · 400-C1B(B): "400-C1B(B)" · 450-C1B(C): "450-C1B(C)" · 450-C1B(B): "450-C1B(B)" · 500-C1B(C): "500-C1B(C)" · 500-C1B(B): "500-C1B(B)" · 550-C1B(C): "550-C1B(C)" · 550-C1B(B): "550-C1B(B)" · 600-C1B(C): "600-C1B(C)" · 600-C1B(B): "600-C1B(B)" · 650-C1B(C): "650-C1B(C)" · 650-C1B(B): "650-C1B(B)" · 700-C1B(C): "700-C1B(C)" · 700-C1B(B): "700-C1B(B)" · 200-C2: "200-C2" · 250-C2: "250-C2" · 300-C2: "300-C2" · 350-C2: "350-C2" | `"GRADE"` | string | - | **Required** |
| 11 | [When "CODE" is NMX2023(MKS)(RC)] Grade · 250-C1A(C): "250-C1A(C)" · 250-C1A(B): "250-C1A(B)" · 300-C1A(C): "300-C1A(C)" · 300-C1A(B): "300-C1A(B)" · 350-C1A(C): "350-C1A(C)" · 350-C1A(B): "350-C1A(B)" · 400-C1B(C): "400-C1B(C)" · 400-C1B(B): "400-C1B(B)" · 450-C1B(C): "450-C1B(C)" · 450-C1B(B): "450-C1B(B)" · 500-C1B(C): "500-C1B(C)" · 500-C1B(B): "500-C1B(B)" · 550-C1B(C): "550-C1B(C)" · 550-C1B(B): "550-C1B(B)" · 600-C1B(C): "600-C1B(C)" · 600-C1B(B): "600-C1B(B)" · 650-C1B(C): "650-C1B(C)" · 650-C1B(B): "650-C1B(B)" · 700-C1B(C): "700-C1B(C)" · 700-C1B(B): "700-C1B(B)" · 200-C2: "200-C2" · 250-C2: "250-C2" · 300-C2: "300-C2" · 350-C2: "350-C2" | `"GRADE"` | string | - | **Required** |
| 12 | [When "CODE" is NMX NTC-2017(RC)] Grade · 200-C1C: "200-C1C" · 250-C1C: "250-C1C" · 300-C1C: "300-C1C" · 350-C1C: "350-C1C" · 400-C1C: "400-C1C" · 450-C1C: "450-C1C" · 500-C1C: "500-C1C" · 550-C1C: "550-C1C" · 600-C1C: "600-C1C" · 650-C1C: "650-C1C" · 700-C1C: "700-C1C" · 750-C1C: "750-C1C" · 800-C1C: "800-C1C" · 200-C1B: "200-C1B" · 250-C1B: "250-C1B" · 300-C1B: "300-C1B" · 350-C1B: "350-C1B" · 400-C1B: "400-C1B" · 450-C1B: "450-C1B" · 500-C1B: "500-C1B" · 550-C1B: "550-C1B" · 600-C1B: "600-C1B" · 650-C1B: "650-C1B" · 700-C1B: "700-C1B" · 750-C1B: "750-C1B" · 800-C1B: "800-C1B" · 150-C2: "150-C2" · 200-C2: "200-C2" · 250-C2: "250-C2" · 300-C2: "300-C2" · 400-C2: "400-C2" | `"GRADE"` | string | - | **Required** |
| 13 | [When "CODE" is CSA(RC)] Grade · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" | `"GRADE"` | string | - | **Required** |
| 14 | [When "CODE" is BS(RC)] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 15 | [When "CODE" is EN04(RC)] Grade · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C30/37: "C30/37" · C32/40: "C32/40" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" · C55/67: "C55/67" · C60/75: "C60/75" · C70/85: "C70/85" · C80/95: "C80/95" · C90/105: "C90/105" | `"GRADE"` | string | - | **Required** |
| 16 | [When "CODE" is EN(RC)] Grade · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C30/37: "C30/37" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" | `"GRADE"` | string | - | **Required** |
| 17 | [When "CODE" is NTC08(RC)] Grade · C8/10: "C8/10" · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C28/35: "C28/35" · C30/37: "C30/37" · C32/40: "C32/40" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" · C55/67: "C55/67" · C60/75: "C60/75" · C70/85: "C70/85" · C80/95: "C80/95" · C90/105: "C90/105" | `"GRADE"` | string | - | **Required** |
| 18 | [When "CODE" is NTC12(RC)] Grade · C8/10: "C8/10" · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C28/35: "C28/35" · C30/37: "C30/37" · C32/40: "C32/40" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" · C55/67: "C55/67" · C60/75: "C60/75" · C70/85: "C70/85" · C80/95: "C80/95" · C90/105: "C90/105" | `"GRADE"` | string | - | **Required** |
| 19 | [When "CODE" is NTC18(RC)] Grade · C8/10: "C8/10" · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C28/35: "C28/35" · C30/37: "C30/37" · C32/40: "C32/40" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" · C55/67: "C55/67" · C60/75: "C60/75" · C70/85: "C70/85" · C80/95: "C80/95" · C90/105: "C90/105" | `"GRADE"` | string | - | **Required** |
| 20 | [When "CODE" is UNI(RC)] Grade · Rck10: "Rck10" · Rck15: "Rck15" · Rck20: "Rck20" · Rck25: "Rck25" · Rck30: "Rck30" · Rck35: "Rck35" · Rck40: "Rck40" · Rck45: "Rck45" · Rck50: "Rck50" | `"GRADE"` | string | - | **Required** |
| 21 | [When "CODE" is SS(RC)] Grade · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C30/37: "C30/37" · C32/40: "C32/40" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" · C55/67: "C55/67" · C60/75: "C60/75" · C70/85: "C70/85" · C80/95: "C80/95" · C90/105: "C90/105" | `"GRADE"` | string | - | **Required** |
| 22 | [When "CODE" is GOST-SP(RC)] Grade · B20: "B20" · B22.5: "B22.5" · B25: "B25" · B27.5: "B27.5" · B30: "B30" · B35: "B35" · B40: "B40" · B45: "B45" · B50: "B50" · B55: "B55" · B60: "B60" | `"GRADE"` | string | - | **Required** |
| 23 | [When "CODE" is GOST-SNIP(RC)] Grade · B20: "B20" · B22.5: "B22.5" · B25: "B25" · B27.5: "B27.5" · B30: "B30" · B35: "B35" · B40: "B40" · B45: "B45" · B50: "B50" · B55: "B55" · B60: "B60" | `"GRADE"` | string | - | **Required** |
| 24 | [When "CODE" is JIS(RC)] Grade · Fc18: "Fc18" · Fc21: "Fc21" · Fc24: "Fc24" · Fc27: "Fc27" · Fc30: "Fc30" · Fc33: "Fc33" · Fc36: "Fc36" · Fc39: "Fc39" · Fc42: "Fc42" · Fc45: "Fc45" · Fc48: "Fc48" · Fc51: "Fc51" · Fc54: "Fc54" · Fc57: "Fc57" · Fc60: "Fc60" · Fc18(LT1): "Fc18(LT1)" · Fc21(LT1): "Fc21(LT1)" · Fc24(LT1): "Fc24(LT1)" · Fc27(LT1): "Fc27(LT1)" · Fc30(LT1): "Fc30(LT1)" · Fc33(LT1): "Fc33(LT1)" · Fc36(LT1): "Fc36(LT1)" · Fc18(LT2): "Fc18(LT2)" · Fc21(LT2): "Fc21(LT2)" · Fc24(LT2): "Fc24(LT2)" · Fc27(LT2): "Fc27(LT2)" | `"GRADE"` | string | - | **Required** |
| 25 | [When "CODE" is JIS-Civil(RC)] Grade · Fc21: "Fc21" · Fc24: "Fc24" · Fc27: "Fc27" · Fc30: "Fc30" · Fc36: "Fc36" · Fc40: "Fc40" · Fc50: "Fc50" · Fc60: "Fc60" · Fc70: "Fc70" · Fc80: "Fc80" | `"GRADE"` | string | - | **Required** |
| 26 | [When "CODE" is JTJ023-85(RC)] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C40: "C40" · C50: "C50" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 27 | [When "CODE" is Q/CR 9300-18(RC)] Grade · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 28 | [When "CODE" is GB 50917-13(RC)] Grade · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 29 | [When "CODE" is GB/T10(RC)] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" | `"GRADE"` | string | - | **Required** |
| 30 | [When "CODE" is GB(RC)] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" | `"GRADE"` | string | - | **Required** |
| 31 | [When "CODE" is GB-Civil(RC)] Grade · 15: "15" · 20: "20" · 25: "25" · 30: "30" · 40: "40" · 50: "50" · 60: "60" | `"GRADE"` | string | - | **Required** |
| 32 | [When "CODE" is TB10092-17(RC)] Grade · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 33 | [When "CODE" is JTG3362-18(RC)] Grade · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" | `"GRADE"` | string | - | **Required** |
| 34 | [When "CODE" is JTG04(RC)] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" | `"GRADE"` | string | - | **Required** |
| 35 | [When "CODE" is TB05(RC)] Grade · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 36 | [When "CODE" is KS19(RC)] Grade · C15: "C15" · C18: "C18" · C21: "C21" · C24: "C24" · C27: "C27" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C49: "C49" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" · C85: "C85" · C90: "C90" · C95: "C95" | `"GRADE"` | string | - | **Required** |
| 37 | [When "CODE" is KS01(RC)] Grade · C15: "C15" · C18: "C18" · C21: "C21" · C24: "C24" · C27: "C27" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C49: "C49" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" · C85: "C85" · C90: "C90" · C95: "C95" | `"GRADE"` | string | - | **Required** |
| 38 | [When "CODE" is KS(RC)] Grade · C150: "C150" · C180: "C180" · C210: "C210" · C240: "C240" · C270: "C270" · C300: "C300" · C350: "C350" · C400: "C400" · C450: "C450" · C500: "C500" · C550: "C550" · C600: "C600" · C650: "C650" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 39 | [When "CODE" is KSCE-LSD15(RC)] Grade · C15: "C15" · C18: "C18" · C21: "C21" · C24: "C24" · C27: "C27" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" · C85: "C85" · C90: "C90" · C95: "C95" | `"GRADE"` | string | - | **Required** |
| 40 | [When "CODE" is KS01-Civil(RC)] Grade · C15: "C15" · C18: "C18" · C21: "C21" · C24: "C24" · C27: "C27" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C49: "C49" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" · C85: "C85" · C90: "C90" · C95: "C95" | `"GRADE"` | string | - | **Required** |
| 41 | [When "CODE" is KS-Civil(RC)] Grade · C150: "C150" · C180: "C180" · C210: "C210" · C240: "C240" · C270: "C270" · C300: "C300" · C350: "C350" · C400: "C400" · C450: "C450" · C500: "C500" · C550: "C550" · C600: "C600" · C650: "C650" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 42 | [When "CODE" is PNS49(RC)] Grade · Grade C18: "Grade C18" · Grade C21: "Grade C21" · Grade C25: "Grade C25" · Grade C28: "Grade C28" · Grade C32: "Grade C32" · Grade C35: "Grade C35" · Grade C42: "Grade C42" · Grade C49: "Grade C49" · Grade C56: "Grade C56" · Grade C63: "Grade C63" · Grade C69: "Grade C69" | `"GRADE"` | string | - | **Required** |
| 43 | [When "CODE" is SNI(RC)] Grade · fc17: "fc17" · fc21: "fc21" · fc25: "fc25" · fc30: "fc30" · fc35: "fc35" · fc40: "fc40" · fc45: "fc45" · fc50: "fc50" · fc55: "fc55" · fc60: "fc60" | `"GRADE"` | string | - | **Required** |
| 44 | [When "CODE" is TIS(RC)] Grade · C150: "C150" · C180: "C180" · C210: "C210" · C240: "C240" · C250: "C250" · C280: "C280" · C300: "C300" · C320: "C320" · C350: "C350" · C380: "C380" · C400: "C400" · C450: "C450" · C500: "C500" · C550: "C550" · C600: "C600" · C650: "C650" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 45 | [When "CODE" is TIS(MKS)(RC)] Grade · C150: "C150" · C180: "C180" · C210: "C210" · C240: "C240" · C250: "C250" · C280: "C280" · C300: "C300" · C320: "C320" · C350: "C350" · C380: "C380" · C400: "C400" · C450: "C450" · C500: "C500" · C550: "C550" · C600: "C600" · C650: "C650" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 46 | [When "CODE" is IRC(RC)] Grade · M15: "M15" · M20: "M20" · M25: "M25" · M30: "M30" · M35: "M35" · M40: "M40" · M45: "M45" · M50: "M50" · M55: "M55" · M60: "M60" · M65: "M65" · M70: "M70" · M75: "M75" · M80: "M80" · M85: "M85" · M90: "M90" | `"GRADE"` | string | - | **Required** |
| 47 | [When "CODE" is IRS(RC)] Grade · M20: "M20" · M25: "M25" · M30: "M30" · M35: "M35" · M40: "M40" · M45: "M45" · M50: "M50" · M55: "M55" · M60: "M60" | `"GRADE"` | string | - | **Required** |
| 48 | [When "CODE" is IS(RC)] Grade · M10: "M10" · M15: "M15" · M20: "M20" · M25: "M25" · M30: "M30" · M35: "M35" · M40: "M40" · M45: "M45" · M50: "M50" · M55: "M55" · M60: "M60" · M65: "M65" · M70: "M70" · M75: "M75" · M80: "M80" | `"GRADE"` | string | - | **Required** |
| 49 | [When "CODE" is CNS560-18(RC)] Grade · C210: "C210" · C245: "C245" · C280: "C280" · C315: "C315" · C350: "C350" · C420: "C420" · C490: "C490" · C560: "C560" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 50 | [When "CODE" is CNS560(RC)] Grade · C210: "C210" · C245: "C245" · C280: "C280" · C315: "C315" · C350: "C350" · C420: "C420" | `"GRADE"` | string | - | **Required** |
| 51 | [When "CODE" is CNS(RC)] Grade · C210: "C210" · C245: "C245" · C280: "C280" · C315: "C315" · C350: "C350" · C420: "C420" | `"GRADE"` | string | - | **Required** |
| 52 | [When "CODE" is AS17(RC)] Grade · C20: "C20" · C25: "C25" · C32: "C32" · C40: "C40" · C50: "C50" · C65: "C65" · C80: "C80" · C100: "C100" | `"GRADE"` | string | - | **Required** |
| 53 | [When "CODE" is TMH7(RC)] Grade · Grade 20: "Grade 20" · Grade 25: "Grade 25" · Grade 30: "Grade 30" · Grade 40: "Grade 40" · Grade 50: "Grade 50" · Grade 60: "Grade 60" | `"GRADE"` | string | - | **Required** |
| 54 | [When "CODE" is SP63.2018(RC)] Grade · B3.5: "B3.5" · B5: "B5" · B7.5: "B7.5" · B10: "B10" · B12.5: "B12.5" · B15: "B15" · B20: "B20" · B25: "B25" · B30: "B30" · B35: "B35" · B40: "B40" · B45: "B45" · B50: "B50" · B55: "B55" · B60: "B60" · B70: "B70" · B80: "B80" · B90: "B90" · B100: "B100" · B3.5A: "B3.5A" · B5A: "B5A" · B7.5A: "B7.5A" · B10A: "B10A" · B12.5A: "B12.5A" · B15A: "B15A" · B20A: "B20A" · B25A: "B25A" · B30A: "B30A" · B35A: "B35A" · B40A: "B40A" · B15B: "B15B" · B20B: "B20B" · B25B: "B25B" · B30B: "B30B" · B35B: "B35B" · B40B: "B40B" · B45B: "B45B" · B50B: "B50B" · B55B: "B55B" · B60B: "B60B" · LB2.5D800: "LB2.5D800" · LB3.5D800: "LB3.5D800" · LB5D800: "LB5D800" · LB7.5D800: "LB7.5D800" · LB2.5D1000: "LB2.5D1000" · LB3.5D1000: "LB3.5D1000" · LB5D1000: "LB5D1000" · LB7.5D1000: "LB7.5D1000" · LB10D1000: "LB10D1000" · LB12.5D1000: "LB12.5D1000" · LB2.5D1200: "LB2.5D1200" · LB3.5D1200: "LB3.5D1200" · LB5D1200: "LB5D1200" · LB7.5D1200: "LB7.5D1200" · LB10D1200: "LB10D1200" · LB12.5D1200: "LB12.5D1200" · LB15D1200: "LB15D1200" · LB2.5D1400: "LB2.5D1400" · LB3.5D1400: "LB3.5D1400" · LB5D1400: "LB5D1400" · LB7.5D1400: "LB7.5D1400" · LB10D1400: "LB10D1400" · LB12.5D1400: "LB12.5D1400" · LB15D1400: "LB15D1400" · LB20D1400: "LB20D1400" · LB25D1400: "LB25D1400" · LB30D1400: "LB30D1400" · LB3.5D1600: "LB3.5D1600" · LB5D1600: "LB5D1600" · LB7.5D1600: "LB7.5D1600" · LB10D1600: "LB10D1600" · LB12.5D1600: "LB12.5D1600" · LB15D1600: "LB15D1600" · LB20D1600: "LB20D1600" · LB25D1600: "LB25D1600" · LB30D1600: "LB30D1600" · LB35D1600: "LB35D1600" · LB5D1800: "LB5D1800" · LB7.5D1800: "LB7.5D1800" · LB10D1800: "LB10D1800" · LB12.5D1800: "LB12.5D1800" · LB15D1800: "LB15D1800" · LB20D1800: "LB20D1800" · LB25D1800: "LB25D1800" · LB30D1800: "LB30D1800" · LB35D1800: "LB35D1800" · LB40D1800: "LB40D1800" · LB7.5D2000: "LB7.5D2000" · LB10D2000: "LB10D2000" · LB12.5D2000: "LB12.5D2000" · LB15D2000: "LB15D2000" · LB20D2000: "LB20D2000" · LB25D2000: "LB25D2000" · LB30D2000: "LB30D2000" · LB35D2000: "LB35D2000" · LB40D2000: "LB40D2000" · CB1.5D500: "CB1.5D500" · CB1.5D600: "CB1.5D600" · CB2D600: "CB2D600" · CB2.5D600: "CB2.5D600" · CB1.5D700: "CB1.5D700" · CB2D700: "CB2D700" · CB2.5D700: "CB2.5D700" · CB3.5D700: "CB3.5D700" · CB2.5D800: "CB2.5D800" · CB3.5D800: "CB3.5D800" · CB5D800: "CB5D800" · CB3.5D900: "CB3.5D900" · CB5D900: "CB5D900" · CB7.5D900: "CB7.5D900" · CB5D1000: "CB5D1000" · CB7.5D1000: "CB7.5D1000" · CB10D1000: "CB10D1000" · CB7.5D1100: "CB7.5D1100" · CB10D1100: "CB10D1100" · CB12.5D1100: "CB12.5D1100" · CB15D1100: "CB15D1100" · CB10D1200: "CB10D1200" · CB12.5D1200: "CB12.5D1200" · CB15D1200: "CB15D1200" | `"GRADE"` | string | - | **Required** |
| 55 | [When "CODE" is TS(RC)] Grade · C16: "C16" · C18: "C18" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" | `"GRADE"` | string | - | **Required** |
| 56 | [When "CODE" is NBR 6118(RC)] Grade · C20BD: "C20BD" · C20GG: "C20GG" · C20LS: "C20LS" · C20SS: "C20SS" · C25BD: "C25BD" · C25GG: "C25GG" · C25LS: "C25LS" · C25SS: "C25SS" · C30BD: "C30BD" · C30GG: "C30GG" · C30LS: "C30LS" · C30SS: "C30SS" · C35BD: "C35BD" · C35GG: "C35GG" · C35LS: "C35LS" · C35SS: "C35SS" · C40BD: "C40BD" · C40GG: "C40GG" · C40LS: "C40LS" · C40SS: "C40SS" · C45BD: "C45BD" · C45GG: "C45GG" · C45LS: "C45LS" · C45SS: "C45SS" · C50BD: "C50BD" · C50GG: "C50GG" · C50LS: "C50LS" · C50SS: "C50SS" · C55BD: "C55BD" · C55GG: "C55GG" · C55LS: "C55LS" · C55SS: "C55SS" · C60BD: "C60BD" · C60GG: "C60GG" · C60LS: "C60LS" · C60SS: "C60SS" · C65BD: "C65BD" · C65GG: "C65GG" · C65LS: "C65LS" · C65SS: "C65SS" · C70BD: "C70BD" · C70GG: "C70GG" · C70LS: "C70LS" · C70SS: "C70SS" · C75BD: "C75BD" · C75GG: "C75GG" · C75LS: "C75LS" · C75SS: "C75SS" · C80BD: "C80BD" · C80GG: "C80GG" · C80LS: "C80LS" · C80SS: "C80SS" · C85BD: "C85BD" · C85GG: "C85GG" · C85LS: "C85LS" · C85SS: "C85SS" · C90BD: "C90BD" · C90GG: "C90GG" · C90LS: "C90LS" · C90SS: "C90SS" | `"GRADE"` | string | - | **Required** |

**JSON Schema**

```json
{
  "title": "Concrete Material",
  "description": "Detailed schema for concrete material settings used by GIRDER_MATL_PROP and SLAB_MATL_PROP in Modify Material.",
  "type": "object",
  "required": [
    "CODE"
  ],
  "additionalProperties": false,
  "properties": {
    "CODE": {
      "type": "string",
      "description": "Concrete design code. If CODE is 'None', enter a custom material NAME instead of selecting GRADE.",
      "oneOf": [
        {
          "const": "None",
          "title": "None"
        },
        {
          "const": "ASTM19(RC)",
          "title": "ASTM19(RC)"
        },
        {
          "const": "ASTM(RC)",
          "title": "ASTM(RC)"
        },
        {
          "const": "U.S.C(US)(RC)",
          "title": "U.S.C(US)(RC)"
        },
        {
          "const": "U.S.C(SI)(RC)",
          "title": "U.S.C(SI)(RC)"
        },
        {
          "const": "NMX2023(RC)",
          "title": "NMX2023(RC)"
        },
        {
          "const": "NMX2023(MKS)(RC)",
          "title": "NMX2023(MKS)(RC)"
        },
        {
          "const": "NMX NTC-2017(RC)",
          "title": "NMX NTC-2017(RC)"
        },
        {
          "const": "CSA(RC)",
          "title": "CSA(RC)"
        },
        {
          "const": "BS(RC)",
          "title": "BS(RC)"
        },
        {
          "const": "EN04(RC)",
          "title": "EN04(RC)"
        },
        {
          "const": "EN(RC)",
          "title": "EN(RC)"
        },
        {
          "const": "NTC08(RC)",
          "title": "NTC08(RC)"
        },
        {
          "const": "NTC12(RC)",
          "title": "NTC12(RC)"
        },
        {
          "const": "NTC18(RC)",
          "title": "NTC18(RC)"
        },
        {
          "const": "UNI(RC)",
          "title": "UNI(RC)"
        },
        {
          "const": "SS(RC)",
          "title": "SS(RC)"
        },
        {
          "const": "GOST-SP(RC)",
          "title": "GOST-SP(RC)"
        },
        {
          "const": "GOST-SNIP(RC)",
          "title": "GOST-SNIP(RC)"
        },
        {
          "const": "JIS(RC)",
          "title": "JIS(RC)"
        },
        {
          "const": "JIS-Civil(RC)",
          "title": "JIS-Civil(RC)"
        },
        {
          "const": "JTJ023-85(RC)",
          "title": "JTJ023-85(RC)"
        },
        {
          "const": "Q/CR 9300-18(RC)",
          "title": "Q/CR 9300-18(RC)"
        },
        {
          "const": "GB 50917-13(RC)",
          "title": "GB 50917-13(RC)"
        },
        {
          "const": "GB/T10(RC)",
          "title": "GB/T10(RC)"
        },
        {
          "const": "GB(RC)",
          "title": "GB(RC)"
        },
        {
          "const": "GB-Civil(RC)",
          "title": "GB-Civil(RC)"
        },
        {
          "const": "TB10092-17(RC)",
          "title": "TB10092-17(RC)"
        },
        {
          "const": "JTG3362-18(RC)",
          "title": "JTG3362-18(RC)"
        },
        {
          "const": "JTG04(RC)",
          "title": "JTG04(RC)"
        },
        {
          "const": "TB05(RC)",
          "title": "TB05(RC)"
        },
        {
          "const": "KS19(RC)",
          "title": "KS19(RC)"
        },
        {
          "const": "KS01(RC)",
          "title": "KS01(RC)"
        },
        {
          "const": "KS(RC)",
          "title": "KS(RC)"
        },
        {
          "const": "KSCE-LSD15(RC)",
          "title": "KSCE-LSD15(RC)"
        },
        {
          "const": "KS01-Civil(RC)",
          "title": "KS01-Civil(RC)"
        },
        {
          "const": "KS-Civil(RC)",
          "title": "KS-Civil(RC)"
        },
        {
          "const": "PNS49(RC)",
          "title": "PNS49(RC)"
        },
        {
          "const": "SNI(RC)",
          "title": "SNI(RC)"
        },
        {
          "const": "TIS(RC)",
          "title": "TIS(RC)"
        },
        {
          "const": "TIS(MKS)(RC)",
          "title": "TIS(MKS)(RC)"
        },
        {
          "const": "IRC(RC)",
          "title": "IRC(RC)"
        },
        {
          "const": "IRS(RC)",
          "title": "IRS(RC)"
        },
        {
          "const": "IS(RC)",
          "title": "IS(RC)"
        },
        {
          "const": "CNS560-18(RC)",
          "title": "CNS560-18(RC)"
        },
        {
          "const": "CNS560(RC)",
          "title": "CNS560(RC)"
        },
        {
          "const": "CNS(RC)",
          "title": "CNS(RC)"
        },
        {
          "const": "AS17(RC)",
          "title": "AS17(RC)"
        },
        {
          "const": "TMH7(RC)",
          "title": "TMH7(RC)"
        },
        {
          "const": "SP63.2018(RC)",
          "title": "SP63.2018(RC)"
        },
        {
          "const": "TS(RC)",
          "title": "TS(RC)"
        },
        {
          "const": "NBR 6118(RC)",
          "title": "NBR 6118(RC)"
        }
      ]
    },
    "NAME": {
      "type": "string",
      "description": "User-defined concrete material name. Used only when CODE is 'None'.",
      "minLength": 1
    },
    "GRADE": {
      "type": "string",
      "description": "Concrete material grade. Required when CODE is not 'None'."
    },
    "COMP_STRENGTH": {
      "type": "number",
      "description": "Specified Compressive Strength (f'c). When CODE is 'None', user input is required. When CODE is a design code, this value can be auto-filled from the selected CODE and GRADE."
    },
    "LIGHT_WEIGHT_FACTOR": {
      "type": "boolean",
      "description": "Light Weight Concrete Factor option."
    },
    "FACTOR_VALUE": {
      "type": "number",
      "description": "Light Weight Factor value. Required when CODE is 'None' and LIGHT_WEIGHT_FACTOR is true.",
      "minimum": 0.75,
      "maximum": 1,
      "default": 1,
      "visibleWhen": {
        "LIGHT_WEIGHT_FACTOR": true
      }
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
          "COMP_STRENGTH"
        ],
        "not": {
          "required": [
            "GRADE"
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "LIGHT_WEIGHT_FACTOR": {
            "const": true
          }
        },
        "required": [
          "LIGHT_WEIGHT_FACTOR"
        ]
      },
      "then": {
        "required": [
          "FACTOR_VALUE"
        ]
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "ASTM19(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "Grade C2500",
              "Grade C3000",
              "Grade C3500",
              "Grade C4000",
              "Grade C4500",
              "Grade C5000",
              "Grade C6000",
              "Grade C7000",
              "Grade C8000",
              "Grade C9000",
              "Grade C10000"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "ASTM(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "Grade C2500",
              "Grade C3000",
              "Grade C3500",
              "Grade C4000",
              "Grade C4500",
              "Grade C5000",
              "Grade C6000",
              "Grade C7000",
              "Grade C8000",
              "Grade C9000",
              "Grade C10000"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "U.S.C(US)(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "Grade C2500",
              "Grade C3000",
              "Grade C3500",
              "Grade C4000",
              "Grade C4500",
              "Grade C5000",
              "Grade C6000",
              "Grade C7000",
              "Grade C8000",
              "Grade C9000",
              "Grade C10000"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "U.S.C(SI)(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "Grade C18",
              "Grade C21",
              "Grade C25",
              "Grade C28",
              "Grade C32",
              "Grade C35",
              "Grade C42",
              "Grade C49",
              "Grade C56",
              "Grade C63",
              "Grade C69"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NMX2023(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "250-C1A(C)",
              "250-C1A(B)",
              "300-C1A(C)",
              "300-C1A(B)",
              "350-C1A(C)",
              "350-C1A(B)",
              "400-C1B(C)",
              "400-C1B(B)",
              "450-C1B(C)",
              "450-C1B(B)",
              "500-C1B(C)",
              "500-C1B(B)",
              "550-C1B(C)",
              "550-C1B(B)",
              "600-C1B(C)",
              "600-C1B(B)",
              "650-C1B(C)",
              "650-C1B(B)",
              "700-C1B(C)",
              "700-C1B(B)",
              "200-C2",
              "250-C2",
              "300-C2",
              "350-C2"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NMX2023(MKS)(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "250-C1A(C)",
              "250-C1A(B)",
              "300-C1A(C)",
              "300-C1A(B)",
              "350-C1A(C)",
              "350-C1A(B)",
              "400-C1B(C)",
              "400-C1B(B)",
              "450-C1B(C)",
              "450-C1B(B)",
              "500-C1B(C)",
              "500-C1B(B)",
              "550-C1B(C)",
              "550-C1B(B)",
              "600-C1B(C)",
              "600-C1B(B)",
              "650-C1B(C)",
              "650-C1B(B)",
              "700-C1B(C)",
              "700-C1B(B)",
              "200-C2",
              "250-C2",
              "300-C2",
              "350-C2"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NMX NTC-2017(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "200-C1C",
              "250-C1C",
              "300-C1C",
              "350-C1C",
              "400-C1C",
              "450-C1C",
              "500-C1C",
              "550-C1C",
              "600-C1C",
              "650-C1C",
              "700-C1C",
              "750-C1C",
              "800-C1C",
              "200-C1B",
              "250-C1B",
              "300-C1B",
              "350-C1B",
              "400-C1B",
              "450-C1B",
              "500-C1B",
              "550-C1B",
              "600-C1B",
              "650-C1B",
              "700-C1B",
              "750-C1B",
              "800-C1B",
              "150-C2",
              "200-C2",
              "250-C2",
              "300-C2",
              "400-C2"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "CSA(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C25",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "BS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C15",
              "C20",
              "C25",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50",
              "C55",
              "C60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "EN04(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C12/15",
              "C16/20",
              "C20/25",
              "C25/30",
              "C30/37",
              "C32/40",
              "C35/45",
              "C40/50",
              "C45/55",
              "C50/60",
              "C55/67",
              "C60/75",
              "C70/85",
              "C80/95",
              "C90/105"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "EN(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C12/15",
              "C16/20",
              "C20/25",
              "C25/30",
              "C30/37",
              "C35/45",
              "C40/50",
              "C45/55",
              "C50/60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NTC08(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C8/10",
              "C12/15",
              "C16/20",
              "C20/25",
              "C25/30",
              "C28/35",
              "C30/37",
              "C32/40",
              "C35/45",
              "C40/50",
              "C45/55",
              "C50/60",
              "C55/67",
              "C60/75",
              "C70/85",
              "C80/95",
              "C90/105"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NTC12(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C8/10",
              "C12/15",
              "C16/20",
              "C20/25",
              "C25/30",
              "C28/35",
              "C30/37",
              "C32/40",
              "C35/45",
              "C40/50",
              "C45/55",
              "C50/60",
              "C55/67",
              "C60/75",
              "C70/85",
              "C80/95",
              "C90/105"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NTC18(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C8/10",
              "C12/15",
              "C16/20",
              "C20/25",
              "C25/30",
              "C28/35",
              "C30/37",
              "C32/40",
              "C35/45",
              "C40/50",
              "C45/55",
              "C50/60",
              "C55/67",
              "C60/75",
              "C70/85",
              "C80/95",
              "C90/105"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "UNI(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "Rck10",
              "Rck15",
              "Rck20",
              "Rck25",
              "Rck30",
              "Rck35",
              "Rck40",
              "Rck45",
              "Rck50"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "SS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C12/15",
              "C16/20",
              "C20/25",
              "C25/30",
              "C30/37",
              "C32/40",
              "C35/45",
              "C40/50",
              "C45/55",
              "C50/60",
              "C55/67",
              "C60/75",
              "C70/85",
              "C80/95",
              "C90/105"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GOST-SP(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "B20",
              "B22.5",
              "B25",
              "B27.5",
              "B30",
              "B35",
              "B40",
              "B45",
              "B50",
              "B55",
              "B60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GOST-SNIP(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "B20",
              "B22.5",
              "B25",
              "B27.5",
              "B30",
              "B35",
              "B40",
              "B45",
              "B50",
              "B55",
              "B60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "JIS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "Fc18",
              "Fc21",
              "Fc24",
              "Fc27",
              "Fc30",
              "Fc33",
              "Fc36",
              "Fc39",
              "Fc42",
              "Fc45",
              "Fc48",
              "Fc51",
              "Fc54",
              "Fc57",
              "Fc60",
              "Fc18(LT1)",
              "Fc21(LT1)",
              "Fc24(LT1)",
              "Fc27(LT1)",
              "Fc30(LT1)",
              "Fc33(LT1)",
              "Fc36(LT1)",
              "Fc18(LT2)",
              "Fc21(LT2)",
              "Fc24(LT2)",
              "Fc27(LT2)"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "JIS-Civil(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "Fc21",
              "Fc24",
              "Fc27",
              "Fc30",
              "Fc36",
              "Fc40",
              "Fc50",
              "Fc60",
              "Fc70",
              "Fc80"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "JTJ023-85(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C15",
              "C20",
              "C25",
              "C30",
              "C40",
              "C50",
              "C60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "Q/CR 9300-18(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C25",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50",
              "C55",
              "C60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GB 50917-13(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C30",
              "C35",
              "C40",
              "C45",
              "C50",
              "C55",
              "C60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GB/T10(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C15",
              "C20",
              "C25",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50",
              "C55",
              "C60",
              "C65",
              "C70",
              "C75",
              "C80"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GB(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C15",
              "C20",
              "C25",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50",
              "C55",
              "C60",
              "C65",
              "C70",
              "C75",
              "C80"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GB-Civil(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "15",
              "20",
              "25",
              "30",
              "40",
              "50",
              "60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TB10092-17(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C25",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50",
              "C55",
              "C60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "JTG3362-18(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C25",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50",
              "C55",
              "C60",
              "C65",
              "C70",
              "C75",
              "C80"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "JTG04(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C15",
              "C20",
              "C25",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50",
              "C55",
              "C60",
              "C65",
              "C70",
              "C75",
              "C80"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TB05(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C20",
              "C25",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50",
              "C55",
              "C60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KS19(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C15",
              "C18",
              "C21",
              "C24",
              "C27",
              "C30",
              "C35",
              "C40",
              "C45",
              "C49",
              "C50",
              "C55",
              "C60",
              "C65",
              "C70",
              "C75",
              "C80",
              "C85",
              "C90",
              "C95"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KS01(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C15",
              "C18",
              "C21",
              "C24",
              "C27",
              "C30",
              "C35",
              "C40",
              "C45",
              "C49",
              "C50",
              "C55",
              "C60",
              "C65",
              "C70",
              "C75",
              "C80",
              "C85",
              "C90",
              "C95"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C150",
              "C180",
              "C210",
              "C240",
              "C270",
              "C300",
              "C350",
              "C400",
              "C450",
              "C500",
              "C550",
              "C600",
              "C650",
              "C700"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KSCE-LSD15(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C15",
              "C18",
              "C21",
              "C24",
              "C27",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50",
              "C55",
              "C60",
              "C65",
              "C70",
              "C75",
              "C80",
              "C85",
              "C90",
              "C95"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KS01-Civil(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C15",
              "C18",
              "C21",
              "C24",
              "C27",
              "C30",
              "C35",
              "C40",
              "C45",
              "C49",
              "C50",
              "C55",
              "C60",
              "C65",
              "C70",
              "C75",
              "C80",
              "C85",
              "C90",
              "C95"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KS-Civil(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C150",
              "C180",
              "C210",
              "C240",
              "C270",
              "C300",
              "C350",
              "C400",
              "C450",
              "C500",
              "C550",
              "C600",
              "C650",
              "C700"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "PNS49(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "Grade C18",
              "Grade C21",
              "Grade C25",
              "Grade C28",
              "Grade C32",
              "Grade C35",
              "Grade C42",
              "Grade C49",
              "Grade C56",
              "Grade C63",
              "Grade C69"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "SNI(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "fc17",
              "fc21",
              "fc25",
              "fc30",
              "fc35",
              "fc40",
              "fc45",
              "fc50",
              "fc55",
              "fc60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TIS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C150",
              "C180",
              "C210",
              "C240",
              "C250",
              "C280",
              "C300",
              "C320",
              "C350",
              "C380",
              "C400",
              "C450",
              "C500",
              "C550",
              "C600",
              "C650",
              "C700"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TIS(MKS)(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C150",
              "C180",
              "C210",
              "C240",
              "C250",
              "C280",
              "C300",
              "C320",
              "C350",
              "C380",
              "C400",
              "C450",
              "C500",
              "C550",
              "C600",
              "C650",
              "C700"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "IRC(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "M15",
              "M20",
              "M25",
              "M30",
              "M35",
              "M40",
              "M45",
              "M50",
              "M55",
              "M60",
              "M65",
              "M70",
              "M75",
              "M80",
              "M85",
              "M90"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "IRS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "M20",
              "M25",
              "M30",
              "M35",
              "M40",
              "M45",
              "M50",
              "M55",
              "M60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "IS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "M10",
              "M15",
              "M20",
              "M25",
              "M30",
              "M35",
              "M40",
              "M45",
              "M50",
              "M55",
              "M60",
              "M65",
              "M70",
              "M75",
              "M80"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "CNS560-18(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C210",
              "C245",
              "C280",
              "C315",
              "C350",
              "C420",
              "C490",
              "C560",
              "C700"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "CNS560(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C210",
              "C245",
              "C280",
              "C315",
              "C350",
              "C420"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "CNS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C210",
              "C245",
              "C280",
              "C315",
              "C350",
              "C420"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "AS17(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C20",
              "C25",
              "C32",
              "C40",
              "C50",
              "C65",
              "C80",
              "C100"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TMH7(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "Grade 20",
              "Grade 25",
              "Grade 30",
              "Grade 40",
              "Grade 50",
              "Grade 60"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "SP63.2018(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "B3.5",
              "B5",
              "B7.5",
              "B10",
              "B12.5",
              "B15",
              "B20",
              "B25",
              "B30",
              "B35",
              "B40",
              "B45",
              "B50",
              "B55",
              "B60",
              "B70",
              "B80",
              "B90",
              "B100",
              "B3.5A",
              "B5A",
              "B7.5A",
              "B10A",
              "B12.5A",
              "B15A",
              "B20A",
              "B25A",
              "B30A",
              "B35A",
              "B40A",
              "B15B",
              "B20B",
              "B25B",
              "B30B",
              "B35B",
              "B40B",
              "B45B",
              "B50B",
              "B55B",
              "B60B",
              "LB2.5D800",
              "LB3.5D800",
              "LB5D800",
              "LB7.5D800",
              "LB2.5D1000",
              "LB3.5D1000",
              "LB5D1000",
              "LB7.5D1000",
              "LB10D1000",
              "LB12.5D1000",
              "LB2.5D1200",
              "LB3.5D1200",
              "LB5D1200",
              "LB7.5D1200",
              "LB10D1200",
              "LB12.5D1200",
              "LB15D1200",
              "LB2.5D1400",
              "LB3.5D1400",
              "LB5D1400",
              "LB7.5D1400",
              "LB10D1400",
              "LB12.5D1400",
              "LB15D1400",
              "LB20D1400",
              "LB25D1400",
              "LB30D1400",
              "LB3.5D1600",
              "LB5D1600",
              "LB7.5D1600",
              "LB10D1600",
              "LB12.5D1600",
              "LB15D1600",
              "LB20D1600",
              "LB25D1600",
              "LB30D1600",
              "LB35D1600",
              "LB5D1800",
              "LB7.5D1800",
              "LB10D1800",
              "LB12.5D1800",
              "LB15D1800",
              "LB20D1800",
              "LB25D1800",
              "LB30D1800",
              "LB35D1800",
              "LB40D1800",
              "LB7.5D2000",
              "LB10D2000",
              "LB12.5D2000",
              "LB15D2000",
              "LB20D2000",
              "LB25D2000",
              "LB30D2000",
              "LB35D2000",
              "LB40D2000",
              "CB1.5D500",
              "CB1.5D600",
              "CB2D600",
              "CB2.5D600",
              "CB1.5D700",
              "CB2D700",
              "CB2.5D700",
              "CB3.5D700",
              "CB2.5D800",
              "CB3.5D800",
              "CB5D800",
              "CB3.5D900",
              "CB5D900",
              "CB7.5D900",
              "CB5D1000",
              "CB7.5D1000",
              "CB10D1000",
              "CB7.5D1100",
              "CB10D1100",
              "CB12.5D1100",
              "CB15D1100",
              "CB10D1200",
              "CB12.5D1200",
              "CB15D1200"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C16",
              "C18",
              "C20",
              "C25",
              "C30",
              "C35",
              "C40",
              "C45",
              "C50"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NBR 6118(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE"
        ],
        "not": {
          "required": [
            "NAME"
          ]
        },
        "properties": {
          "GRADE": {
            "type": "string",
            "enum": [
              "C20BD",
              "C20GG",
              "C20LS",
              "C20SS",
              "C25BD",
              "C25GG",
              "C25LS",
              "C25SS",
              "C30BD",
              "C30GG",
              "C30LS",
              "C30SS",
              "C35BD",
              "C35GG",
              "C35LS",
              "C35SS",
              "C40BD",
              "C40GG",
              "C40LS",
              "C40SS",
              "C45BD",
              "C45GG",
              "C45LS",
              "C45SS",
              "C50BD",
              "C50GG",
              "C50LS",
              "C50SS",
              "C55BD",
              "C55GG",
              "C55LS",
              "C55SS",
              "C60BD",
              "C60GG",
              "C60LS",
              "C60SS",
              "C65BD",
              "C65GG",
              "C65LS",
              "C65SS",
              "C70BD",
              "C70GG",
              "C70LS",
              "C70SS",
              "C75BD",
              "C75GG",
              "C75LS",
              "C75SS",
              "C80BD",
              "C80GG",
              "C80LS",
              "C80SS",
              "C85BD",
              "C85GG",
              "C85LS",
              "C85SS",
              "C90BD",
              "C90GG",
              "C90LS",
              "C90SS"
            ]
          }
        }
      }
    }
  ]
}
```

### 부속 Schema — Rebar Material

**원문** [영문 58043403493785](https://support.midasuser.com/hc/en-us/articles/58043403493785)

`GIRDER_REBAR_PROP`와 `SLAB_REBAR_PROP`에 쓰는 공식 재료 설정 부속 Schema입니다.

> ⚠️ 부속 글의 Input URI에는 `{base url} +`만 표시되어 있습니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Map of keyed objects where each key is a string identifier. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Code · None: "None" · ASTM19(RC): "ASTM19(RC)" · ASTM(RC): "ASTM(RC)" · U.S.C(US)(RC): "U.S.C(US)(RC)" · U.S.C(SI)(RC): "U.S.C(SI)(RC)" · NMX2023(RC): "NMX2023(RC)" · NMX2023(MKS)(RC): "NMX2023(MKS)(RC)" · NMX NTC-2017(RC): "NMX NTC-2017(RC)" · CSA(RC): "CSA(RC)" · BS(RC): "BS(RC)" · EN04(RC): "EN04(RC)" · EN(RC): "EN(RC)" · NTC08(RC): "NTC08(RC)" · NTC12(RC): "NTC12(RC)" · NTC18(RC): "NTC18(RC)" · UNI(RC): "UNI(RC)" · SS(RC): "SS(RC)" · GOST-SP(RC): "GOST-SP(RC)" · GOST-SNIP(RC): "GOST-SNIP(RC)" · JIS(RC): "JIS(RC)" · JIS-Civil(RC): "JIS-Civil(RC)" · JTJ023-85(RC): "JTJ023-85(RC)" · Q/CR 9300-18(RC): "Q/CR 9300-18(RC)" · GB 50917-13(RC): "GB 50917-13(RC)" · GB/T10(RC): "GB/T10(RC)" · GB(RC): "GB(RC)" · GB-Civil(RC): "GB-Civil(RC)" · TB10092-17(RC): "TB10092-17(RC)" · JTG3362-18(RC): "JTG3362-18(RC)" · JTG04(RC): "JTG04(RC)" · TB05(RC): "TB05(RC)" · KS19(RC): "KS19(RC)" · KS01(RC): "KS01(RC)" · KS(RC): "KS(RC)" · KSCE-LSD15(RC): "KSCE-LSD15(RC)" · KS01-Civil(RC): "KS01-Civil(RC)" · KS-Civil(RC): "KS-Civil(RC)" · PNS49(RC): "PNS49(RC)" · SNI(RC): "SNI(RC)" · TIS(RC): "TIS(RC)" · TIS(MKS)(RC): "TIS(MKS)(RC)" · IRC(RC): "IRC(RC)" · IRS(RC): "IRS(RC)" · IS(RC): "IS(RC)" · CNS560-18(RC): "CNS560-18(RC)" · CNS560(RC): "CNS560(RC)" · CNS(RC): "CNS(RC)" · AS17(RC): "AS17(RC)" · TMH7(RC): "TMH7(RC)" · SP63.2018(RC): "SP63.2018(RC)" · TS(RC): "TS(RC)" · NBR 6118(RC): "NBR 6118(RC)" | `"CODE"` | string | - | **Required** |
| 2 | [When "CODE" is None] Name of Main Rebar Constraints: · Length: min 1 | `"NAME_MAIN_REBAR"` | string | - | **Required** |
| 3 | [When "CODE" is None] Name of Sub-Rebar Constraints: · Length: min 1 | `"NAME_SUB_REBAR"` | string | - | **Required** |
| 4 | [When "CODE" is None] Fy Constraints: · Value Range: >= 0 | `"Fy"` | number | - | **Required** |
| 5 | [When "CODE" is None] Fys Constraints: · Value Range: >= 0 | `"Fys"` | number | - | **Required** |
| 6 | [When "CODE" is ASTM19(RC)] Grade of Main Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 7 | [When "CODE" is ASTM19(RC)] Grade of Sub-Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 8 | [When "CODE" is ASTM(RC)] Grade of Main Rebar · Grade 40: "Grade 40" · Grade 50: "Grade 50" · Grade 60: "Grade 60" · Grade 75: "Grade 75" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 9 | [When "CODE" is ASTM(RC)] Grade of Sub-Rebar · Grade 40: "Grade 40" · Grade 50: "Grade 50" · Grade 60: "Grade 60" · Grade 75: "Grade 75" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 10 | [When "CODE" is U.S.C(US)(RC)] Grade of Main Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 75: "Grade 75" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 11 | [When "CODE" is U.S.C(US)(RC)] Grade of Sub-Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 75: "Grade 75" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 12 | [When "CODE" is U.S.C(SI)(RC)] Grade of Main Rebar · Grade 280: "Grade 280" · Grade 420: "Grade 420" · Grade 520: "Grade 520" · Grade 550: "Grade 550" · Grade 690: "Grade 690" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 13 | [When "CODE" is U.S.C(SI)(RC)] Grade of Sub-Rebar · Grade 280: "Grade 280" · Grade 420: "Grade 420" · Grade 520: "Grade 520" · Grade 550: "Grade 550" · Grade 690: "Grade 690" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 14 | [When "CODE" is NMX2023(RC)] Grade of Main Rebar · Grade 42: "Grade 42" · Grade 56: "Grade 56" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 15 | [When "CODE" is NMX2023(RC)] Grade of Sub-Rebar · Grade 42: "Grade 42" · Grade 56: "Grade 56" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 16 | [When "CODE" is NMX2023(MKS)(RC)] Grade of Main Rebar · Grade 42: "Grade 42" · Grade 56: "Grade 56" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 17 | [When "CODE" is NMX2023(MKS)(RC)] Grade of Sub-Rebar · Grade 42: "Grade 42" · Grade 56: "Grade 56" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 18 | [When "CODE" is NMX NTC-2017(RC)] Grade of Main Rebar · Grade 42: "Grade 42" · Grade 56: "Grade 56" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 19 | [When "CODE" is NMX NTC-2017(RC)] Grade of Sub-Rebar · Grade 42: "Grade 42" · Grade 56: "Grade 56" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 20 | [When "CODE" is CSA(RC)] Grade of Main Rebar · 300R: "300R" · 400R: "400R" · 500R: "500R" · 400W: "400W" · 500W: "500W" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 21 | [When "CODE" is CSA(RC)] Grade of Sub-Rebar · 300R: "300R" · 400R: "400R" · 500R: "500R" · 400W: "400W" · 500W: "500W" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 22 | [When "CODE" is BS(RC)] Grade of Main Rebar · S250: "S250" · S460: "S460" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 23 | [When "CODE" is BS(RC)] Grade of Sub-Rebar · S250: "S250" · S460: "S460" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 24 | [When "CODE" is EN04(RC)] Grade of Main Rebar · Class A: "Class A" · Class B: "Class B" · Class C: "Class C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 25 | [When "CODE" is EN04(RC)] Grade of Sub-Rebar · Class A: "Class A" · Class B: "Class B" · Class C: "Class C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 26 | [When "CODE" is EN(RC)] Grade of Main Rebar · S220: "S220" · S250: "S250" · S300: "S300" · S400: "S400" · S460: "S460" · S500: "S500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 27 | [When "CODE" is EN(RC)] Grade of Sub-Rebar · S220: "S220" · S250: "S250" · S300: "S300" · S400: "S400" · S460: "S460" · S500: "S500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 28 | [When "CODE" is NTC08(RC)] Grade of Main Rebar · B450C: "B450C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 29 | [When "CODE" is NTC08(RC)] Grade of Sub-Rebar · B450C: "B450C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 30 | [When "CODE" is NTC12(RC)] Grade of Main Rebar · B450C: "B450C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 31 | [When "CODE" is NTC12(RC)] Grade of Sub-Rebar · B450C: "B450C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 32 | [When "CODE" is NTC18(RC)] Grade of Main Rebar · B450C: "B450C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 33 | [When "CODE" is NTC18(RC)] Grade of Sub-Rebar · B450C: "B450C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 34 | [When "CODE" is UNI(RC)] Grade of Main Rebar · FeB22k: "FeB22k" · FeB32k: "FeB32k" · FeB38k: "FeB38k" · FeB44k: "FeB44k" · B450C: "B450C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 35 | [When "CODE" is UNI(RC)] Grade of Sub-Rebar · FeB22k: "FeB22k" · FeB32k: "FeB32k" · FeB38k: "FeB38k" · FeB44k: "FeB44k" · B450C: "B450C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 36 | [When "CODE" is SS(RC)] Grade of Main Rebar · Class A: "Class A" · Class B: "Class B" · Class C: "Class C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 37 | [When "CODE" is SS(RC)] Grade of Sub-Rebar · Class A: "Class A" · Class B: "Class B" · Class C: "Class C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 38 | [When "CODE" is GOST-SP(RC)] Grade of Main Rebar · A240: "A240" · A300: "A300" · A400: "A400" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 39 | [When "CODE" is GOST-SP(RC)] Grade of Sub-Rebar · A240: "A240" · A300: "A300" · A400: "A400" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 40 | [When "CODE" is GOST-SNIP(RC)] Grade of Main Rebar · A-I: "A-I" · A-II: "A-II" · A-III: "A-III" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 41 | [When "CODE" is GOST-SNIP(RC)] Grade of Sub-Rebar · A-I: "A-I" · A-II: "A-II" · A-III: "A-III" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 42 | [When "CODE" is JIS(RC)] Grade of Main Rebar · SR235: "SR235" · SR295: "SR295" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 43 | [When "CODE" is JIS(RC)] Grade of Sub-Rebar · SR235: "SR235" · SR295: "SR295" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 44 | [When "CODE" is JIS-Civil(RC)] Grade of Main Rebar · SR235: "SR235" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 45 | [When "CODE" is JIS-Civil(RC)] Grade of Sub-Rebar · SR235: "SR235" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 46 | [When "CODE" is JTJ023-85(RC)] Grade of Main Rebar · Grade 1: "Grade 1" · Grade 2: "Grade 2" · Grade 3: "Grade 3" · 5 Hao: "5 Hao" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 47 | [When "CODE" is JTJ023-85(RC)] Grade of Sub-Rebar · Grade 1: "Grade 1" · Grade 2: "Grade 2" · Grade 3: "Grade 3" · 5 Hao: "5 Hao" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 48 | [When "CODE" is Q/CR 9300-18(RC)] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRB500: "HRB500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 49 | [When "CODE" is Q/CR 9300-18(RC)] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRB500: "HRB500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 50 | [When "CODE" is GB 50917-13(RC)] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 51 | [When "CODE" is GB 50917-13(RC)] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 52 | [When "CODE" is GB/T10(RC)] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" · RRB500: "RRB500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 53 | [When "CODE" is GB/T10(RC)] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" · RRB500: "RRB500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 54 | [When "CODE" is GB(RC)] Grade of Main Rebar · HPB235: "HPB235" · HRB335: "HRB335" · HRB400: "HRB400" · RRB400: "RRB400" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 55 | [When "CODE" is GB(RC)] Grade of Sub-Rebar · HPB235: "HPB235" · HRB335: "HRB335" · HRB400: "HRB400" · RRB400: "RRB400" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 56 | [When "CODE" is GB-Civil(RC)] Grade of Main Rebar · Grade 1: "Grade 1" · Grade 2: "Grade 2" · Grade 3: "Grade 3" · 5 Hao: "5 Hao" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 57 | [When "CODE" is GB-Civil(RC)] Grade of Sub-Rebar · Grade 1: "Grade 1" · Grade 2: "Grade 2" · Grade 3: "Grade 3" · 5 Hao: "5 Hao" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 58 | [When "CODE" is TB10092-17(RC)] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRB500: "HRB500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 59 | [When "CODE" is TB10092-17(RC)] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRB500: "HRB500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 60 | [When "CODE" is JTG3362-18(RC)] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 61 | [When "CODE" is JTG3362-18(RC)] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 62 | [When "CODE" is JTG04(RC)] Grade of Main Rebar · R235: "R235" · HRB335: "HRB335" · HRB400: "HRB400" · KL400: "KL400" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 63 | [When "CODE" is JTG04(RC)] Grade of Sub-Rebar · R235: "R235" · HRB335: "HRB335" · HRB400: "HRB400" · KL400: "KL400" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 64 | [When "CODE" is TB05(RC)] Grade of Main Rebar · Q235: "Q235" · HRB335: "HRB335" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 65 | [When "CODE" is TB05(RC)] Grade of Sub-Rebar · Q235: "Q235" · HRB335: "HRB335" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 66 | [When "CODE" is KS19(RC)] Grade of Main Rebar · SD300: "SD300" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" · SD700: "SD700" · SD400S: "SD400S" · SD500S: "SD500S" · SD600S: "SD600S" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 67 | [When "CODE" is KS19(RC)] Grade of Sub-Rebar · SD300: "SD300" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" · SD700: "SD700" · SD400S: "SD400S" · SD500S: "SD500S" · SD600S: "SD600S" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 68 | [When "CODE" is KS01(RC)] Grade of Main Rebar · SD240: "SD240" · SD300: "SD300" · SD350: "SD350" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 69 | [When "CODE" is KS01(RC)] Grade of Sub-Rebar · SD240: "SD240" · SD300: "SD300" · SD350: "SD350" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 70 | [When "CODE" is KS(RC)] Grade of Main Rebar · SD24: "SD24" · SD30: "SD30" · SD35: "SD35" · SD40: "SD40" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 71 | [When "CODE" is KS(RC)] Grade of Sub-Rebar · SD24: "SD24" · SD30: "SD30" · SD35: "SD35" · SD40: "SD40" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 72 | [When "CODE" is KSCE-LSD15(RC)] Grade of Main Rebar · SD240: "SD240" · SD300: "SD300" · SD350: "SD350" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 73 | [When "CODE" is KSCE-LSD15(RC)] Grade of Sub-Rebar · SD240: "SD240" · SD300: "SD300" · SD350: "SD350" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 74 | [When "CODE" is KS01-Civil(RC)] Grade of Main Rebar · SD240: "SD240" · SD300: "SD300" · SD350: "SD350" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 75 | [When "CODE" is KS01-Civil(RC)] Grade of Sub-Rebar · SD240: "SD240" · SD300: "SD300" · SD350: "SD350" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 76 | [When "CODE" is KS-Civil(RC)] Grade of Main Rebar · SD24: "SD24" · SD30: "SD30" · SD35: "SD35" · SD40: "SD40" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 77 | [When "CODE" is KS-Civil(RC)] Grade of Sub-Rebar · SD24: "SD24" · SD30: "SD30" · SD35: "SD35" · SD40: "SD40" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 78 | [When "CODE" is PNS49(RC)] Grade of Main Rebar · 230R: "230R" · 280R: "280R" · 420R: "420R" · 520R: "520R" · 550R: "550R" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 79 | [When "CODE" is PNS49(RC)] Grade of Sub-Rebar · 230R: "230R" · 280R: "280R" · 420R: "420R" · 520R: "520R" · 550R: "550R" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 80 | [When "CODE" is SNI(RC)] Grade of Main Rebar · BjTP 280: "BjTP 280" · BjTS 280: "BjTS 280" · BjTS 420A: "BjTS 420A" · BjTS 420B: "BjTS 420B" · BjTS 520: "BjTS 520" · BjTS 550: "BjTS 550" · BjTS 700: "BjTS 700" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 81 | [When "CODE" is SNI(RC)] Grade of Sub-Rebar · BjTP 280: "BjTP 280" · BjTS 280: "BjTS 280" · BjTS 420A: "BjTS 420A" · BjTS 420B: "BjTS 420B" · BjTS 520: "BjTS 520" · BjTS 550: "BjTS 550" · BjTS 700: "BjTS 700" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 82 | [When "CODE" is TIS(RC)] Grade of Main Rebar · SR24: "SR24" · SD30: "SD30" · SD40: "SD40" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 83 | [When "CODE" is TIS(RC)] Grade of Sub-Rebar · SR24: "SR24" · SD30: "SD30" · SD40: "SD40" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 84 | [When "CODE" is TIS(MKS)(RC)] Grade of Main Rebar · SR24: "SR24" · SD30: "SD30" · SD40: "SD40" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 85 | [When "CODE" is TIS(MKS)(RC)] Grade of Sub-Rebar · SR24: "SR24" · SD30: "SD30" · SD40: "SD40" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 86 | [When "CODE" is IRC(RC)] Grade of Main Rebar · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 87 | [When "CODE" is IRC(RC)] Grade of Sub-Rebar · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 88 | [When "CODE" is IRS(RC)] Grade of Main Rebar · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 89 | [When "CODE" is IRS(RC)] Grade of Sub-Rebar · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 90 | [When "CODE" is IS(RC)] Grade of Main Rebar · Fe240: "Fe240" · Fe250: "Fe250" · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 91 | [When "CODE" is IS(RC)] Grade of Sub-Rebar · Fe240: "Fe240" · Fe250: "Fe250" · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 92 | [When "CODE" is CNS560-18(RC)] Grade of Main Rebar · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490W: "SD490W" · SD550W: "SD550W" · SD690: "SD690" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 93 | [When "CODE" is CNS560-18(RC)] Grade of Sub-Rebar · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490W: "SD490W" · SD550W: "SD550W" · SD690: "SD690" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 94 | [When "CODE" is CNS560(RC)] Grade of Main Rebar · SR240: "SR240" · SR300: "SR300" · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490: "SD490" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 95 | [When "CODE" is CNS560(RC)] Grade of Sub-Rebar · SR240: "SR240" · SR300: "SR300" · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490: "SD490" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 96 | [When "CODE" is CNS(RC)] Grade of Main Rebar · SD24: "SD24" · SD28: "SD28" · SD30: "SD30" · SD35: "SD35" · SD42: "SD42" · SD42W: "SD42W" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 97 | [When "CODE" is CNS(RC)] Grade of Sub-Rebar · SD24: "SD24" · SD28: "SD28" · SD30: "SD30" · SD35: "SD35" · SD42: "SD42" · SD42W: "SD42W" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 98 | [When "CODE" is AS17(RC)] Grade of Main Rebar · D500L: "D500L" · D500N: "D500N" · D500E: "D500E" · D500LP: "D500LP" · D600N: "D600N" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 99 | [When "CODE" is AS17(RC)] Grade of Sub-Rebar · D500L: "D500L" · D500N: "D500N" · D500E: "D500E" · D500LP: "D500LP" · D600N: "D600N" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 100 | [When "CODE" is TMH7(RC)] Grade of Main Rebar · Type A: "Type A" · Type B: "Type B" · Type C: "Type C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 101 | [When "CODE" is TMH7(RC)] Grade of Sub-Rebar · Type A: "Type A" · Type B: "Type B" · Type C: "Type C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 102 | [When "CODE" is SP63.2018(RC)] Grade of Main Rebar · A240: "A240" · A240_sw: "A240_sw" · A400: "A400" · A400_sw: "A400_sw" · A500: "A500" · A500_sw: "A500_sw" · A600: "A600" · A800: "A800" · A1000: "A1000" · B500: "B500" · B500_sw: "B500_sw" · BP500: "BP500" · BP1200: "BP1200" · BP1300: "BP1300" · BP1400: "BP1400" · BP1500: "BP1500" · BP1600: "BP1600" · K1400: "K1400" · K1450: "K1450" · K1500: "K1500" · K1550: "K1550" · K1650: "K1650" · K1750: "K1750" · K1850: "K1850" · K1900: "K1900" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 103 | [When "CODE" is SP63.2018(RC)] Grade of Sub-Rebar · A240: "A240" · A240_sw: "A240_sw" · A400: "A400" · A400_sw: "A400_sw" · A500: "A500" · A500_sw: "A500_sw" · A600: "A600" · A800: "A800" · A1000: "A1000" · B500: "B500" · B500_sw: "B500_sw" · BP500: "BP500" · BP1200: "BP1200" · BP1300: "BP1300" · BP1400: "BP1400" · BP1500: "BP1500" · BP1600: "BP1600" · K1400: "K1400" · K1450: "K1450" · K1500: "K1500" · K1550: "K1550" · K1650: "K1650" · K1750: "K1750" · K1850: "K1850" · K1900: "K1900" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 104 | [When "CODE" is TS(RC)] Grade of Main Rebar · B420C: "B420C" · B520C: "B520C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 105 | [When "CODE" is TS(RC)] Grade of Sub-Rebar · B420C: "B420C" · B520C: "B520C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 106 | [When "CODE" is NBR 6118(RC)] Grade of Main Rebar · CA25: "CA25" · CA50: "CA50" · CA60: "CA60" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 107 | [When "CODE" is NBR 6118(RC)] Grade of Sub-Rebar · CA25: "CA25" · CA50: "CA50" · CA60: "CA60" | `"GRADE_SUB_REBAR"` | string | - | **Required** |

**JSON Schema**

```json
{
  "title": "Rebar Material",
  "description": "Detailed schema for rebar material settings used by GIRDER_REBAR_PROP and SLAB_REBAR_PROP in Modify Material.",
  "type": "object",
  "required": [
    "CODE"
  ],
  "additionalProperties": false,
  "properties": {
    "CODE": {
      "type": "string",
      "description": "Rebar design code. If CODE is 'None', input custom rebar names, Fy and Fys directly instead of selecting GRADE_MAIN_REBAR and GRADE_SUB_REBAR.",
      "oneOf": [
        {
          "const": "None",
          "title": "None"
        },
        {
          "const": "ASTM19(RC)",
          "title": "ASTM19(RC)"
        },
        {
          "const": "ASTM(RC)",
          "title": "ASTM(RC)"
        },
        {
          "const": "U.S.C(US)(RC)",
          "title": "U.S.C(US)(RC)"
        },
        {
          "const": "U.S.C(SI)(RC)",
          "title": "U.S.C(SI)(RC)"
        },
        {
          "const": "NMX2023(RC)",
          "title": "NMX2023(RC)"
        },
        {
          "const": "NMX2023(MKS)(RC)",
          "title": "NMX2023(MKS)(RC)"
        },
        {
          "const": "NMX NTC-2017(RC)",
          "title": "NMX NTC-2017(RC)"
        },
        {
          "const": "CSA(RC)",
          "title": "CSA(RC)"
        },
        {
          "const": "BS(RC)",
          "title": "BS(RC)"
        },
        {
          "const": "EN04(RC)",
          "title": "EN04(RC)"
        },
        {
          "const": "EN(RC)",
          "title": "EN(RC)"
        },
        {
          "const": "NTC08(RC)",
          "title": "NTC08(RC)"
        },
        {
          "const": "NTC12(RC)",
          "title": "NTC12(RC)"
        },
        {
          "const": "NTC18(RC)",
          "title": "NTC18(RC)"
        },
        {
          "const": "UNI(RC)",
          "title": "UNI(RC)"
        },
        {
          "const": "SS(RC)",
          "title": "SS(RC)"
        },
        {
          "const": "GOST-SP(RC)",
          "title": "GOST-SP(RC)"
        },
        {
          "const": "GOST-SNIP(RC)",
          "title": "GOST-SNIP(RC)"
        },
        {
          "const": "JIS(RC)",
          "title": "JIS(RC)"
        },
        {
          "const": "JIS-Civil(RC)",
          "title": "JIS-Civil(RC)"
        },
        {
          "const": "JTJ023-85(RC)",
          "title": "JTJ023-85(RC)"
        },
        {
          "const": "Q/CR 9300-18(RC)",
          "title": "Q/CR 9300-18(RC)"
        },
        {
          "const": "GB 50917-13(RC)",
          "title": "GB 50917-13(RC)"
        },
        {
          "const": "GB/T10(RC)",
          "title": "GB/T10(RC)"
        },
        {
          "const": "GB(RC)",
          "title": "GB(RC)"
        },
        {
          "const": "GB-Civil(RC)",
          "title": "GB-Civil(RC)"
        },
        {
          "const": "TB10092-17(RC)",
          "title": "TB10092-17(RC)"
        },
        {
          "const": "JTG3362-18(RC)",
          "title": "JTG3362-18(RC)"
        },
        {
          "const": "JTG04(RC)",
          "title": "JTG04(RC)"
        },
        {
          "const": "TB05(RC)",
          "title": "TB05(RC)"
        },
        {
          "const": "KS19(RC)",
          "title": "KS19(RC)"
        },
        {
          "const": "KS01(RC)",
          "title": "KS01(RC)"
        },
        {
          "const": "KS(RC)",
          "title": "KS(RC)"
        },
        {
          "const": "KSCE-LSD15(RC)",
          "title": "KSCE-LSD15(RC)"
        },
        {
          "const": "KS01-Civil(RC)",
          "title": "KS01-Civil(RC)"
        },
        {
          "const": "KS-Civil(RC)",
          "title": "KS-Civil(RC)"
        },
        {
          "const": "PNS49(RC)",
          "title": "PNS49(RC)"
        },
        {
          "const": "SNI(RC)",
          "title": "SNI(RC)"
        },
        {
          "const": "TIS(RC)",
          "title": "TIS(RC)"
        },
        {
          "const": "TIS(MKS)(RC)",
          "title": "TIS(MKS)(RC)"
        },
        {
          "const": "IRC(RC)",
          "title": "IRC(RC)"
        },
        {
          "const": "IRS(RC)",
          "title": "IRS(RC)"
        },
        {
          "const": "IS(RC)",
          "title": "IS(RC)"
        },
        {
          "const": "CNS560-18(RC)",
          "title": "CNS560-18(RC)"
        },
        {
          "const": "CNS560(RC)",
          "title": "CNS560(RC)"
        },
        {
          "const": "CNS(RC)",
          "title": "CNS(RC)"
        },
        {
          "const": "AS17(RC)",
          "title": "AS17(RC)"
        },
        {
          "const": "TMH7(RC)",
          "title": "TMH7(RC)"
        },
        {
          "const": "SP63.2018(RC)",
          "title": "SP63.2018(RC)"
        },
        {
          "const": "TS(RC)",
          "title": "TS(RC)"
        },
        {
          "const": "NBR 6118(RC)",
          "title": "NBR 6118(RC)"
        }
      ]
    },
    "GRADE_MAIN_REBAR": {
      "type": "string",
      "description": "Grade of main rebar. Required when CODE is not 'None'."
    },
    "GRADE_SUB_REBAR": {
      "type": "string",
      "description": "Grade of sub-rebar. Required when CODE is not 'None'."
    },
    "NAME_MAIN_REBAR": {
      "type": "string",
      "description": "User-defined main rebar name. Required when CODE is 'None'.",
      "minLength": 1
    },
    "NAME_SUB_REBAR": {
      "type": "string",
      "description": "User-defined sub-rebar name. Required when CODE is 'None'.",
      "minLength": 1
    },
    "Fy": {
      "type": "number",
      "description": "Yield strength of main rebar. User input is available when CODE is 'None'.",
      "minimum": 0
    },
    "Fys": {
      "type": "number",
      "description": "Yield strength of sub-rebar. User input is available when CODE is 'None'.",
      "minimum": 0
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
          "NAME_MAIN_REBAR",
          "NAME_SUB_REBAR",
          "Fy",
          "Fys"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "GRADE_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "GRADE_SUB_REBAR"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "ASTM19(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• Grade 40 : \"Grade 40\"\n• Grade 60 : \"Grade 60\"\n• Grade 80 : \"Grade 80\"\n• Grade 100 : \"Grade 100\"",
            "enum": [
              "Grade 40",
              "Grade 60",
              "Grade 80",
              "Grade 100"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• Grade 40 : \"Grade 40\"\n• Grade 60 : \"Grade 60\"\n• Grade 80 : \"Grade 80\"\n• Grade 100 : \"Grade 100\"",
            "enum": [
              "Grade 40",
              "Grade 60",
              "Grade 80",
              "Grade 100"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "ASTM(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• Grade 40 : \"Grade 40\"\n• Grade 50 : \"Grade 50\"\n• Grade 60 : \"Grade 60\"\n• Grade 75 : \"Grade 75\"",
            "enum": [
              "Grade 40",
              "Grade 50",
              "Grade 60",
              "Grade 75"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• Grade 40 : \"Grade 40\"\n• Grade 50 : \"Grade 50\"\n• Grade 60 : \"Grade 60\"\n• Grade 75 : \"Grade 75\"",
            "enum": [
              "Grade 40",
              "Grade 50",
              "Grade 60",
              "Grade 75"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "U.S.C(US)(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• Grade 40 : \"Grade 40\"\n• Grade 60 : \"Grade 60\"\n• Grade 75 : \"Grade 75\"\n• Grade 80 : \"Grade 80\"\n• Grade 100 : \"Grade 100\"",
            "enum": [
              "Grade 40",
              "Grade 60",
              "Grade 75",
              "Grade 80",
              "Grade 100"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "Grade 40",
              "Grade 60",
              "Grade 75",
              "Grade 80",
              "Grade 100"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "U.S.C(SI)(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• Grade 280 : \"Grade 280\"\n• Grade 420 : \"Grade 420\"\n• Grade 520 : \"Grade 520\"\n• Grade 550 : \"Grade 550\"\n• Grade 690 : \"Grade 690\"",
            "enum": [
              "Grade 280",
              "Grade 420",
              "Grade 520",
              "Grade 550",
              "Grade 690"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• Grade 280 : \"Grade 280\"\n• Grade 420 : \"Grade 420\"\n• Grade 520 : \"Grade 520\"\n• Grade 550 : \"Grade 550\"\n• Grade 690 : \"Grade 690\"",
            "enum": [
              "Grade 280",
              "Grade 420",
              "Grade 520",
              "Grade 550",
              "Grade 690"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NMX2023(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "Grade 42",
              "Grade 56"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "Grade 42",
              "Grade 56"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NMX2023(MKS)(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "Grade 42",
              "Grade 56"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "Grade 42",
              "Grade 56"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NMX NTC-2017(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "Grade 42",
              "Grade 56"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "Grade 42",
              "Grade 56"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "CSA(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "300R",
              "400R",
              "500R",
              "400W",
              "500W"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "300R",
              "400R",
              "500R",
              "400W",
              "500W"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "BS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "S250",
              "S460"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• S250 : \"S250\"\n• S460 : \"S460\"",
            "enum": [
              "S250",
              "S460"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "EN04(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "Class A",
              "Class B",
              "Class C"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "Class A",
              "Class B",
              "Class C"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "EN(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "S220",
              "S250",
              "S300",
              "S400",
              "S460",
              "S500"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "S220",
              "S250",
              "S300",
              "S400",
              "S460",
              "S500"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NTC08(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "B450C"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• B450C : \"B450C\"",
            "enum": [
              "B450C"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NTC12(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "B450C"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• B450C : \"B450C\"",
            "enum": [
              "B450C"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NTC18(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "B450C"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• B450C : \"B450C\"",
            "enum": [
              "B450C"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "UNI(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• FeB22k : \"FeB22k\"\n• FeB32k : \"FeB32k\"\n• FeB38k : \"FeB38k\"\n• FeB44k : \"FeB44k\"\n• B450C : \"B450C\"",
            "enum": [
              "FeB22k",
              "FeB32k",
              "FeB38k",
              "FeB44k",
              "B450C"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "FeB22k",
              "FeB32k",
              "FeB38k",
              "FeB44k",
              "B450C"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "SS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "Class A",
              "Class B",
              "Class C"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "Class A",
              "Class B",
              "Class C"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GOST-SP(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• A240 : \"A240\"\n• A300 : \"A300\"\n• A400 : \"A400\"",
            "enum": [
              "A240",
              "A300",
              "A400"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• A240 : \"A240\"\n• A300 : \"A300\"\n• A400 : \"A400\"",
            "enum": [
              "A240",
              "A300",
              "A400"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GOST-SNIP(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "A-I",
              "A-II",
              "A-III"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "A-I",
              "A-II",
              "A-III"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "JIS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "SR235",
              "SR295",
              "SD295A",
              "SD295B",
              "SD345",
              "SD390",
              "SD490"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "SR235",
              "SR295",
              "SD295A",
              "SD295B",
              "SD345",
              "SD390",
              "SD490"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "JIS-Civil(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "SR235",
              "SD295A",
              "SD295B",
              "SD345",
              "SD390",
              "SD490"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "SR235",
              "SD295A",
              "SD295B",
              "SD345",
              "SD390",
              "SD490"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "JTJ023-85(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "Grade 1",
              "Grade 2",
              "Grade 3",
              "5 Hao"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "Grade 1",
              "Grade 2",
              "Grade 3",
              "5 Hao"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "Q/CR 9300-18(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "HPB300",
              "HRB400",
              "HRB500"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "HPB300",
              "HRB400",
              "HRB500"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GB 50917-13(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "HPB300",
              "HRB400",
              "HRBF400",
              "RRB400",
              "HRB500",
              "HRBF500"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "HPB300",
              "HRB400",
              "HRBF400",
              "RRB400",
              "HRB500",
              "HRBF500"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GB/T10(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "HPB300",
              "HRB400",
              "HRBF400",
              "RRB400",
              "HRB500",
              "HRBF500",
              "RRB500"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "HPB300",
              "HRB400",
              "HRBF400",
              "RRB400",
              "HRB500",
              "HRBF500",
              "RRB500"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GB(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "HPB235",
              "HRB335",
              "HRB400",
              "RRB400"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "HPB235",
              "HRB335",
              "HRB400",
              "RRB400"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "GB-Civil(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "Grade 1",
              "Grade 2",
              "Grade 3",
              "5 Hao"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "Grade 1",
              "Grade 2",
              "Grade 3",
              "5 Hao"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TB10092-17(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "HPB300",
              "HRB400",
              "HRB500"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "HPB300",
              "HRB400",
              "HRB500"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "JTG3362-18(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "HPB300",
              "HRB400",
              "HRBF400",
              "RRB400",
              "HRB500"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "HPB300",
              "HRB400",
              "HRBF400",
              "RRB400",
              "HRB500"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "JTG04(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "R235",
              "HRB335",
              "HRB400",
              "KL400"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "R235",
              "HRB335",
              "HRB400",
              "KL400"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TB05(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "Q235",
              "HRB335"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• Q235 : \"Q235\"\n• HRB335 : \"HRB335\"",
            "enum": [
              "Q235",
              "HRB335"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KS19(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "SD300",
              "SD400",
              "SD500",
              "SD600",
              "SD700",
              "SD400S",
              "SD500S",
              "SD600S"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "SD300",
              "SD400",
              "SD500",
              "SD600",
              "SD700",
              "SD400S",
              "SD500S",
              "SD600S"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KS01(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "SD240",
              "SD300",
              "SD350",
              "SD400",
              "SD500",
              "SD600"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "SD240",
              "SD300",
              "SD350",
              "SD400",
              "SD500",
              "SD600"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "SD24",
              "SD30",
              "SD35",
              "SD40",
              "SD50"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "SD24",
              "SD30",
              "SD35",
              "SD40",
              "SD50"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KSCE-LSD15(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "SD240",
              "SD300",
              "SD350",
              "SD400",
              "SD500",
              "SD600"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "SD240",
              "SD300",
              "SD350",
              "SD400",
              "SD500",
              "SD600"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KS01-Civil(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "SD240",
              "SD300",
              "SD350",
              "SD400",
              "SD500",
              "SD600"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "SD240",
              "SD300",
              "SD350",
              "SD400",
              "SD500",
              "SD600"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "KS-Civil(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "SD24",
              "SD30",
              "SD35",
              "SD40",
              "SD50"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "SD24",
              "SD30",
              "SD35",
              "SD40",
              "SD50"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "PNS49(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• 230R : \"230R\"\n• 280R : \"280R\"\n• 420R : \"420R\"\n• 520R : \"520R\"\n• 550R : \"550R\"",
            "enum": [
              "230R",
              "280R",
              "420R",
              "520R",
              "550R"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• 230R : \"230R\"\n• 280R : \"280R\"\n• 420R : \"420R\"\n• 520R : \"520R\"\n• 550R : \"550R\"",
            "enum": [
              "230R",
              "280R",
              "420R",
              "520R",
              "550R"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "SNI(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• BjTP 280 : \"BjTP 280\"\n• BjTS 280 : \"BjTS 280\"\n• BjTS 420A : \"BjTS 420A\"\n• BjTS 420B : \"BjTS 420B\"\n• BjTS 520 : \"BjTS 520\"\n• BjTS 550 : \"BjTS 550\"\n• BjTS 700 : \"BjTS 700\"",
            "enum": [
              "BjTP 280",
              "BjTS 280",
              "BjTS 420A",
              "BjTS 420B",
              "BjTS 520",
              "BjTS 550",
              "BjTS 700"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "enum": [
              "BjTP 280",
              "BjTS 280",
              "BjTS 420A",
              "BjTS 420B",
              "BjTS 520",
              "BjTS 550",
              "BjTS 700"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TIS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• SR24 : \"SR24\"\n• SD30 : \"SD30\"\n• SD40 : \"SD40\"\n• SD50 : \"SD50\"",
            "enum": [
              "SR24",
              "SD30",
              "SD40",
              "SD50"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• SR24 : \"SR24\"\n• SD30 : \"SD30\"\n• SD40 : \"SD40\"\n• SD50 : \"SD50\"",
            "enum": [
              "SR24",
              "SD30",
              "SD40",
              "SD50"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TIS(MKS)(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• SR24 : \"SR24\"\n• SD30 : \"SD30\"\n• SD40 : \"SD40\"\n• SD50 : \"SD50\"",
            "enum": [
              "SR24",
              "SD30",
              "SD40",
              "SD50"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• SR24 : \"SR24\"\n• SD30 : \"SD30\"\n• SD40 : \"SD40\"\n• SD50 : \"SD50\"",
            "enum": [
              "SR24",
              "SD30",
              "SD40",
              "SD50"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "IRC(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• Fe415 : \"Fe415\"\n• Fe500 : \"Fe500\"\n• Fe550 : \"Fe550\"\n• Fe600 : \"Fe600\"",
            "enum": [
              "Fe415",
              "Fe500",
              "Fe550",
              "Fe600"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• Fe415 : \"Fe415\"\n• Fe500 : \"Fe500\"\n• Fe550 : \"Fe550\"\n• Fe600 : \"Fe600\"",
            "enum": [
              "Fe415",
              "Fe500",
              "Fe550",
              "Fe600"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "IRS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• Fe415 : \"Fe415\"\n• Fe500 : \"Fe500\"\n• Fe550 : \"Fe550\"\n• Fe600 : \"Fe600\"",
            "enum": [
              "Fe415",
              "Fe500",
              "Fe550",
              "Fe600"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• Fe415 : \"Fe415\"\n• Fe500 : \"Fe500\"\n• Fe550 : \"Fe550\"\n• Fe600 : \"Fe600\"",
            "enum": [
              "Fe415",
              "Fe500",
              "Fe550",
              "Fe600"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "IS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• Fe240 : \"Fe240\"\n• Fe250 : \"Fe250\"\n• Fe415 : \"Fe415\"\n• Fe500 : \"Fe500\"\n• Fe550 : \"Fe550\"\n• Fe600 : \"Fe600\"",
            "enum": [
              "Fe240",
              "Fe250",
              "Fe415",
              "Fe500",
              "Fe550",
              "Fe600"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• Fe240 : \"Fe240\"\n• Fe250 : \"Fe250\"\n• Fe415 : \"Fe415\"\n• Fe500 : \"Fe500\"\n• Fe550 : \"Fe550\"\n• Fe600 : \"Fe600\"",
            "enum": [
              "Fe240",
              "Fe250",
              "Fe415",
              "Fe500",
              "Fe550",
              "Fe600"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "CNS560-18(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• SD280 : \"SD280\"\n• SD280W : \"SD280W\"\n• SD420 : \"SD420\"\n• SD420W : \"SD420W\"\n• SD490W : \"SD490W\"\n• SD550W : \"SD550W\"\n• SD690 : \"SD690\"",
            "enum": [
              "SD280",
              "SD280W",
              "SD420",
              "SD420W",
              "SD490W",
              "SD550W",
              "SD690"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• SD280 : \"SD280\"\n• SD280W : \"SD280W\"\n• SD420 : \"SD420\"\n• SD420W : \"SD420W\"\n• SD490W : \"SD490W\"\n• SD550W : \"SD550W\"\n• SD690 : \"SD690\"",
            "enum": [
              "SD280",
              "SD280W",
              "SD420",
              "SD420W",
              "SD490W",
              "SD550W",
              "SD690"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "CNS560(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• SR240 : \"SR240\"\n• SR300 : \"SR300\"\n• SD280 : \"SD280\"\n• SD280W : \"SD280W\"\n• SD420 : \"SD420\"\n• SD420W : \"SD420W\"\n• SD490 : \"SD490\"",
            "enum": [
              "SR240",
              "SR300",
              "SD280",
              "SD280W",
              "SD420",
              "SD420W",
              "SD490"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• SR240 : \"SR240\"\n• SR300 : \"SR300\"\n• SD280 : \"SD280\"\n• SD280W : \"SD280W\"\n• SD420 : \"SD420\"\n• SD420W : \"SD420W\"\n• SD490 : \"SD490\"",
            "enum": [
              "SR240",
              "SR300",
              "SD280",
              "SD280W",
              "SD420",
              "SD420W",
              "SD490"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "CNS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "enum": [
              "SD24",
              "SD28",
              "SD30",
              "SD35",
              "SD42",
              "SD42W",
              "SD50"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• SD24 : \"SD24\"\n• SD28 : \"SD28\"\n• SD30 : \"SD30\"\n• SD35 : \"SD35\"\n• SD42 : \"SD42\"\n• SD42W : \"SD42W\"\n• SD50 : \"SD50\"",
            "enum": [
              "SD24",
              "SD28",
              "SD30",
              "SD35",
              "SD42",
              "SD42W",
              "SD50"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "AS17(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• D500L : \"D500L\"\n• D500N : \"D500N\"\n• D500E : \"D500E\"\n• D500LP : \"D500LP\"\n• D600N : \"D600N\"",
            "enum": [
              "D500L",
              "D500N",
              "D500E",
              "D500LP",
              "D600N"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• D500L : \"D500L\"\n• D500N : \"D500N\"\n• D500E : \"D500E\"\n• D500LP : \"D500LP\"\n• D600N : \"D600N\"",
            "enum": [
              "D500L",
              "D500N",
              "D500E",
              "D500LP",
              "D600N"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TMH7(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• Type A : \"Type A\"\n• Type B : \"Type B\"\n• Type C : \"Type C\"",
            "enum": [
              "Type A",
              "Type B",
              "Type C"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• Type A : \"Type A\"\n• Type B : \"Type B\"\n• Type C : \"Type C\"",
            "enum": [
              "Type A",
              "Type B",
              "Type C"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "SP63.2018(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• A240 : \"A240\"\n• A240_sw : \"A240_sw\"\n• A400 : \"A400\"\n• A400_sw : \"A400_sw\"\n• A500 : \"A500\"\n• A500_sw : \"A500_sw\"\n• A600 : \"A600\"\n• A800 : \"A800\"\n• A1000 : \"A1000\"\n• B500 : \"B500\"\n• B500_sw : \"B500_sw\"\n• BP500 : \"BP500\"\n• BP1200 : \"BP1200\"\n• BP1300 : \"BP1300\"\n• BP1400 : \"BP1400\"\n• BP1500 : \"BP1500\"\n• BP1600 : \"BP1600\"\n• K1400 : \"K1400\"\n• K1450 : \"K1450\"\n• K1500 : \"K1500\"\n• K1550 : \"K1550\"\n• K1650 : \"K1650\"\n• K1750 : \"K1750\"\n• K1850 : \"K1850\"\n• K1900 : \"K1900\"",
            "enum": [
              "A240",
              "A240_sw",
              "A400",
              "A400_sw",
              "A500",
              "A500_sw",
              "A600",
              "A800",
              "A1000",
              "B500",
              "B500_sw",
              "BP500",
              "BP1200",
              "BP1300",
              "BP1400",
              "BP1500",
              "BP1600",
              "K1400",
              "K1450",
              "K1500",
              "K1550",
              "K1650",
              "K1750",
              "K1850",
              "K1900"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• A240 : \"A240\"\n• A240_sw : \"A240_sw\"\n• A400 : \"A400\"\n• A400_sw : \"A400_sw\"\n• A500 : \"A500\"\n• A500_sw : \"A500_sw\"\n• A600 : \"A600\"\n• A800 : \"A800\"\n• A1000 : \"A1000\"\n• B500 : \"B500\"\n• B500_sw : \"B500_sw\"\n• BP500 : \"BP500\"\n• BP1200 : \"BP1200\"\n• BP1300 : \"BP1300\"\n• BP1400 : \"BP1400\"\n• BP1500 : \"BP1500\"\n• BP1600 : \"BP1600\"\n• K1400 : \"K1400\"\n• K1450 : \"K1450\"\n• K1500 : \"K1500\"\n• K1550 : \"K1550\"\n• K1650 : \"K1650\"\n• K1750 : \"K1750\"\n• K1850 : \"K1850\"\n• K1900 : \"K1900\"",
            "enum": [
              "A240",
              "A240_sw",
              "A400",
              "A400_sw",
              "A500",
              "A500_sw",
              "A600",
              "A800",
              "A1000",
              "B500",
              "B500_sw",
              "BP500",
              "BP1200",
              "BP1300",
              "BP1400",
              "BP1500",
              "BP1600",
              "K1400",
              "K1450",
              "K1500",
              "K1550",
              "K1650",
              "K1750",
              "K1850",
              "K1900"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "TS(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• B420C : \"B420C\"\n• B520C : \"B520C\"",
            "enum": [
              "B420C",
              "B520C"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• B420C : \"B420C\"\n• B520C : \"B520C\"",
            "enum": [
              "B420C",
              "B520C"
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "CODE": {
            "const": "NBR 6118(RC)"
          }
        },
        "required": [
          "CODE"
        ]
      },
      "then": {
        "required": [
          "GRADE_MAIN_REBAR",
          "GRADE_SUB_REBAR"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "Fy"
              ]
            },
            {
              "required": [
                "Fys"
              ]
            },
            {
              "required": [
                "NAME_MAIN_REBAR"
              ]
            },
            {
              "required": [
                "NAME_SUB_REBAR"
              ]
            }
          ]
        },
        "properties": {
          "GRADE_MAIN_REBAR": {
            "type": "string",
            "description": "Grade of main rebar.\n\nEnum Values:\n• CA25 : \"CA25\"\n• CA50 : \"CA50\"\n• CA60 : \"CA60\"",
            "enum": [
              "CA25",
              "CA50",
              "CA60"
            ]
          },
          "GRADE_SUB_REBAR": {
            "type": "string",
            "description": "Grade of sub-rebar.\n\nEnum Values:\n• CA25 : \"CA25\"\n• CA50 : \"CA50\"\n• CA60 : \"CA60\"",
            "enum": [
              "CA25",
              "CA50",
              "CA60"
            ]
          }
        }
      }
    }
  ]
}
```

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "GIRDER_MATL_PROP": {
        "CODE": "ASTM19(RC)",
        "GRADE": "Grade C6000",
        "LIGHT_WEIGHT_FACTOR": true,
        "FACTOR_VALUE": 0.85
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "ASTM19(RC)",
        "GRADE_MAIN_REBAR": "Grade 60",
        "GRADE_SUB_REBAR": "Grade 60"
      },
      "SLAB_PROP": true,
      "SLAB_MATL_PROP": {
        "CODE": "ASTM19(RC)",
        "GRADE": "Grade C4000",
        "LIGHT_WEIGHT_FACTOR": false
      },
      "SLAB_REBAR_PROP": {
        "CODE": "ASTM19(RC)",
        "GRADE_MAIN_REBAR": "Grade 60",
        "GRADE_SUB_REBAR": "Grade 40"
      }
    },
    "2": {
      "GIRDER_MATL_PROP": {
        "CODE": "None",
        "NAME": "User-C4000",
        "COMP_STRENGTH": 27579,
        "LIGHT_WEIGHT_FACTOR": false
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "None",
        "NAME_MAIN_REBAR": "User-Gr60",
        "NAME_SUB_REBAR": "User-Gr40",
        "Fy": 413685,
        "Fys": 275790
      },
      "SLAB_PROP": false
    }
  }
}
```

**Response**

```json
{
  "MATD_PSC_ITEM": {
    "1": {
      "GIRDER_MATL_PROP": {
        "CODE": "ASTM19(RC)",
        "LIGHT_WEIGHT_FACTOR": true,
        "GRADE": "Grade C6000",
        "FACTOR_VALUE": 0.85
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "ASTM19(RC)",
        "GRADE_MAIN_REBAR": "Grade 60",
        "GRADE_SUB_REBAR": "Grade 60"
      },
      "SLAB_PROP": true,
      "SLAB_MATL_PROP": {
        "CODE": "ASTM19(RC)",
        "LIGHT_WEIGHT_FACTOR": false,
        "GRADE": "Grade C4000"
      },
      "SLAB_REBAR_PROP": {
        "CODE": "ASTM19(RC)",
        "GRADE_MAIN_REBAR": "Grade 60",
        "GRADE_SUB_REBAR": "Grade 40"
      }
    },
    "2": {
      "GIRDER_MATL_PROP": {
        "CODE": "None",
        "LIGHT_WEIGHT_FACTOR": false,
        "NAME": "User-C4000",
        "COMP_STRENGTH": 27579.0
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "None",
        "NAME_MAIN_REBAR": "User-Gr60",
        "NAME_SUB_REBAR": "User-Gr40",
        "Fy": 413685.0,
        "Fys": 275790.0
      },
      "SLAB_PROP": false
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/MATD"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "GIRDER_MATL_PROP": {
        "CODE": "ASTM19(RC)",
        "GRADE": "Grade C6000",
        "LIGHT_WEIGHT_FACTOR": true,
        "FACTOR_VALUE": 0.85
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "ASTM19(RC)",
        "GRADE_MAIN_REBAR": "Grade 60",
        "GRADE_SUB_REBAR": "Grade 60"
      },
      "SLAB_PROP": true,
      "SLAB_MATL_PROP": {
        "CODE": "ASTM19(RC)",
        "GRADE": "Grade C4000",
        "LIGHT_WEIGHT_FACTOR": false
      },
      "SLAB_REBAR_PROP": {
        "CODE": "ASTM19(RC)",
        "GRADE_MAIN_REBAR": "Grade 60",
        "GRADE_SUB_REBAR": "Grade 40"
      }
    },
    "2": {
      "GIRDER_MATL_PROP": {
        "CODE": "None",
        "NAME": "User-C4000",
        "COMP_STRENGTH": 27579,
        "LIGHT_WEIGHT_FACTOR": false
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "None",
        "NAME_MAIN_REBAR": "User-Gr60",
        "NAME_SUB_REBAR": "User-Gr40",
        "Fy": 413685,
        "Fys": 275790
      },
      "SLAB_PROP": false
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 6. `RPSC` — Longitudinal Rebar-Reinforcements

> **기능** 종방향 철근 보강 정보를 입력합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/RPSC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 57946907749017](https://support.midasuser.com/hc/en-us/articles/57946907749017)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a section ID (e.g., "1"). The section must be a PSC or composite section. Available only when the model has virtual beams and its PSC design code supports virtual beams. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Same Longitudinal Rebar at I/J | `"OPT_MBAR_J"` | boolean | - | **Required** |
| 2 | [General] Same Shear Rebar at I/J | `"OPT_SBAR_J"` | boolean | - | **Required** |
| 3 | [General] Cracked Section | `"OPT_CRACKED"` | boolean | - | Optional |
| 4 | [General] Shear Reinforcement Items | `"SBAR_ITEMS"` | array [object] | - | **Required** |
| 4.1 | └ [General] Diagonal Reinforcement | `"OPT_DR"` | boolean | false | Optional |
| 4.2 | └ [When OPT_DR = true] [DR] Pitch · Minimum: 0 | `"DR_PITCH"` | number | - | **Required** |
| 4.3 | └ [When OPT_DR = true] [DR] Angle | `"DR_THETA"` | number | - | Optional |
| 4.4 | └ [When OPT_DR = true] [DR] Area · Minimum: 0 | `"DR_AW"` | number | - | **Required** |
| 4.5 | └ [When OPT_DR = true] Steel Bar for Web | `"OPT_SBW"` | boolean | false | Optional |
| 4.6 | └ [When OPT_SBW = true] [SBW] Pitch · Minimum: 0 | `"SBW_PITCH"` | number | - | **Required** |
| 4.7 | └ [When OPT_SBW = true] [SBW] Angle | `"SBW_ANGLE"` | number | - | Optional |
| 4.8 | └ [When OPT_SBW = true] [SBW] Area · Minimum: 0 | `"SBW_AP"` | number | - | **Required** |
| 4.9 | └ [When OPT_SBW = true] [SBW] Pre-force · Minimum: 0 | `"SBW_PS"` | number | - | **Required** |
| 4.10 | └ [When OPT_SBW = true] [SBW] Shear Reduction Factor · Minimum: 0 | `"SBW_FACTOR"` | number | - | **Required** |
| 4.11 | └ [When OPT_SBW = true] Torsional Reinforcement | `"OPT_TR"` | boolean | false | Optional |
| 4.12 | └ [When OPT_TR = true] [TR] Pitch · Minimum: 0 | `"TR_PITCH"` | number | - | **Required** |
| 4.13 | └ [When OPT_TR = true] [TR] Area (Web) · Minimum: 0 | `"TR_AWT"` | number | - | **Required** |
| 4.14 | └ [When OPT_TR = true] [TR] Area (Long.) · Minimum: 0 | `"TR_ALT"` | number | - | **Required** |
| 4.15 | └ [When OPT_TR = true] Stirrup | `"OPT_SR"` | boolean | false | Optional |
| 4.16 | └ [When OPT_SR = true] [SR] Pitch · Minimum: 0 | `"SR_PITCH"` | number | - | **Required** |
| 4.17 | └ [When OPT_SR = true] [SR] Area · Minimum: 0 | `"SR_AW"` | number | - | **Required** |
| 4.18 | └ [When OPT_SR = true] Enclosing Stirrup | `"OPT_LBAR_FLG"` | boolean | false | Optional |
| 4.19 | └ [When OPT_LBAR_FLG = true] Cover Thickness · Minimum: 0 | `"LBAR_THICK"` | number | - | **Required** |
| 4.20 | └ [When OPT_LBAR_FLG = true] Include Flange/Cantilever | `"LBAR_INC_FC"` | boolean | - | Optional |
| 5 | [General] Longitudinal Reinforcement | `"MBARS"` | array [object] | - | **Required** |
| 5.1 | └ [General] Longitudinal Rebar Items | `"MBAR_ITEMS"` | array [object] | - | Optional |
| 5.1.1 | 　　└ [General] Section Positions - I / J · I · J | `"IJ"` | string | - | **Required** |
| 5.1.2 | 　　└ [General] Bar Name | `"NAME"` | string | - | **Required** |
| 5.1.3 | 　　└ [General] Reference Y · Centroid: 0 · Left: 1 | `"REF_Y"` | integer | - | **Required** |
| 5.1.4 | 　　└ [General] Distance from Reference in Y direction | `"Y"` | number | 0 | Optional |
| 5.1.5 | 　　└ [General] Reference Z · Top: 0 · Bottom: 1 | `"REF_Z"` | integer | - | **Required** |
| 5.1.6 | 　　└ [General] Distance from Reference in Z Direction | `"Z"` | number | 0 | Optional |
| 5.1.7 | 　　└ [General] Number of Rebar · Minimum: 0 | `"NUM"` | integer | - | **Required** |
| 5.1.8 | 　　└ [General] Spacing · Minimum: 0 | `"SPACING"` | number | 0 | Optional |
| 5.1.9 | 　　└ [General] Part · 0 · 1 · 2 | `"PART"` | integer | - | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a section ID (e.g., \"1\"). The section must be a PSC or composite section. Available only when the model has virtual beams and its PSC design code supports virtual beams.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "RPSC Longitudinal Rebar",
          "type": "object",
          "description": "Section Manager - Reinforcements (longitudinal and shear reinforcement).",
          "required": [
            "OPT_MBAR_J",
            "OPT_SBAR_J",
            "SBAR_ITEMS",
            "MBARS"
          ],
          "additionalProperties": false,
          "properties": {
            "OPT_MBAR_J": {
              "type": "boolean",
              "description": "Same rebar data at I-end and J-end for longitudinal reinforcement."
            },
            "OPT_SBAR_J": {
              "type": "boolean",
              "description": "Same shear rebar data at I-end and J-end."
            },
            "OPT_CRACKED": {
              "type": "boolean",
              "description": "Cracked section option. Shown only for composite sections; omitted from GET otherwise. When omitted in a request the stored value is kept (false for a new record)."
            },
            "SBAR_ITEMS": {
              "type": "array",
              "description": "Shear reinforcement data. Index 0: I-section, index 1: J-section (when OPT_SBAR_J is false).",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "OPT_DR": {
                    "type": "boolean",
                    "description": "Diagonal reinforcement.",
                    "default": false
                  },
                  "DR_PITCH": {
                    "type": "number",
                    "description": "[DR] Pitch."
                  },
                  "DR_THETA": {
                    "type": "number",
                    "description": "[DR] Angle."
                  },
                  "DR_AW": {
                    "type": "number",
                    "description": "[DR] Area."
                  },
                  "OPT_SBW": {
                    "type": "boolean",
                    "description": "Steel bar for web.",
                    "default": false
                  },
                  "SBW_PITCH": {
                    "type": "number",
                    "description": "[SBW] Pitch."
                  },
                  "SBW_ANGLE": {
                    "type": "number",
                    "description": "[SBW] Angle."
                  },
                  "SBW_AP": {
                    "type": "number",
                    "description": "[SBW] Area."
                  },
                  "SBW_PS": {
                    "type": "number",
                    "description": "[SBW] Pre-force."
                  },
                  "SBW_FACTOR": {
                    "type": "number",
                    "description": "[SBW] Shear reduction factor."
                  },
                  "OPT_TR": {
                    "type": "boolean",
                    "description": "Torsional reinforcement.",
                    "default": false
                  },
                  "TR_PITCH": {
                    "type": "number",
                    "description": "[TR] Pitch."
                  },
                  "TR_AWT": {
                    "type": "number",
                    "description": "[TR] Area (web)."
                  },
                  "TR_ALT": {
                    "type": "number",
                    "description": "[TR] Area (longitudinal)."
                  },
                  "OPT_SR": {
                    "type": "boolean",
                    "description": "Stirrup.",
                    "default": false
                  },
                  "SR_PITCH": {
                    "type": "number",
                    "description": "[SR] Pitch."
                  },
                  "SR_AW": {
                    "type": "number",
                    "description": "[SR] Area."
                  },
                  "OPT_LBAR_FLG": {
                    "type": "boolean",
                    "description": "Enclosing stirrup.",
                    "default": false
                  },
                  "LBAR_THICK": {
                    "type": "number",
                    "description": "Cover thickness for enclosed section area."
                  },
                  "LBAR_INC_FC": {
                    "type": "boolean",
                    "description": "Include flange/cantilever."
                  }
                }
              },
              "minItems": 1,
              "maxItems": 2
            },
            "MBARS": {
              "type": "array",
              "description": "Longitudinal reinforcement. Index 0: I-section, index 1: J-section (when OPT_MBAR_J is false). On PUT, [] or a group without MBAR_ITEMS ({}, the GET form) keeps the existing rebar of that section; {\"MBAR_ITEMS\": []} deletes it. For shear reinforcement only, send any of the three.",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "MBAR_ITEMS": {
                    "type": "array",
                    "description": "Longitudinal reinforcement property details. Omit to keep the existing rebar of this section (PUT); [] deletes it.",
                    "items": {
                      "type": "object",
                      "required": [
                        "IJ",
                        "NAME",
                        "REF_Y",
                        "REF_Z",
                        "NUM",
                        "PART"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "IJ": {
                          "type": "string",
                          "description": "Section position.",
                          "enum": [
                            "I",
                            "J"
                          ]
                        },
                        "NAME": {
                          "type": "string",
                          "description": "Bar name. Must be a rebar name of the model's concrete rebar material code (e.g. D16); otherwise the request is rejected (400).",
                          "minLength": 1
                        },
                        "REF_Y": {
                          "type": "integer",
                          "description": "Reference Y. 0: centroid, 1: left.",
                          "enum": [
                            0,
                            1
                          ]
                        },
                        "Y": {
                          "type": "number",
                          "description": "Distance from reference in Y direction.",
                          "default": 0
                        },
                        "REF_Z": {
                          "type": "integer",
                          "description": "Reference Z. 0: top, 1: bottom.",
                          "enum": [
                            0,
                            1
                          ]
                        },
                        "Z": {
                          "type": "number",
                          "description": "Distance from reference in Z direction.",
                          "default": 0
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars.",
                          "minimum": 0
                        },
                        "SPACING": {
                          "type": "number",
                          "description": "Spacing between rebars.",
                          "default": 0,
                          "minimum": 0
                        },
                        "PART": {
                          "type": "integer",
                          "description": "Part. Allowed values depend on the section: non-composite 0, 1 or 2; concrete composite 1 or 2; steel composite 2.",
                          "enum": [
                            0,
                            1,
                            2
                          ]
                        }
                      }
                    },
                    "minItems": 0
                  }
                }
              },
              "minItems": 0,
              "maxItems": 2
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

- `RPSC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "OPT_MBAR_J": false,
      "OPT_SBAR_J": false,
      "SBAR_ITEMS": [
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        },
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        }
      ],
      "MBARS": [
        {
          "MBAR_ITEMS": [
            {
              "IJ": "I",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.08,
              "NUM": 12,
              "SPACING": 0.15,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.2,
              "NUM": 6,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "I",
              "NAME": "#9",
              "REF_Y": 0,
              "Y": 0.12,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 10,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
        },
        {
          "MBAR_ITEMS": [
            {
              "IJ": "J",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.08,
              "NUM": 12,
              "SPACING": 0.15,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.2,
              "NUM": 6,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "J",
              "NAME": "#9",
              "REF_Y": 0,
              "Y": 0.12,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 10,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
        }
      ]
    }
  }
}
```

**Response**

```json
{
  "RPSC": {
    "1": {
      "OPT_MBAR_J": false,
      "OPT_SBAR_J": false,
      "SBAR_ITEMS": [
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90.0,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90.0,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000.0,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        },
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90.0,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90.0,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000.0,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        }
      ],
      "MBARS": [
        {
          "MBAR_ITEMS": [
            {
              "IJ": "I",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.08,
              "NUM": 12,
              "SPACING": 0.15,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.2,
              "NUM": 6,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "I",
              "NAME": "#9",
              "REF_Y": 0,
              "Y": 0.12,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 10,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
        },
        {
          "MBAR_ITEMS": [
            {
              "IJ": "J",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.08,
              "NUM": 12,
              "SPACING": 0.15,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.2,
              "NUM": 6,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "J",
              "NAME": "#9",
              "REF_Y": 0,
              "Y": 0.12,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 10,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/RPSC"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "OPT_MBAR_J": false,
      "OPT_SBAR_J": false,
      "SBAR_ITEMS": [
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        },
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        }
      ],
      "MBARS": [
        {
          "MBAR_ITEMS": [
            {
              "IJ": "I",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.08,
              "NUM": 12,
              "SPACING": 0.15,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.2,
              "NUM": 6,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "I",
              "NAME": "#9",
              "REF_Y": 0,
              "Y": 0.12,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 10,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
        },
        {
          "MBAR_ITEMS": [
            {
              "IJ": "J",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.08,
              "NUM": 12,
              "SPACING": 0.15,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.2,
              "NUM": 6,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "J",
              "NAME": "#9",
              "REF_Y": 0,
              "Y": 0.12,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 10,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
        }
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```

### 이전 한국어 원문

**원문** [한국어 57946914266905](https://support.midasuser.com/hc/ko/articles/57946914266905)

**원문 Active Methods** `POST` · `GET` · `PUT` · `DELETE`

> ⚠️ 이전 Schema는 주철근 NUM의 최소값과 MBARS·MBAR_ITEMS의 최소 항목 수를 1로, 영문 Schema는 0으로 지정합니다. 이전 Schema에는 OPT_MBAR_J에 따른 MBARS 항목 수 조건도 있습니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Same Longitudinal Rebar at I/J | `"OPT_MBAR_J"` | boolean | - | **Required** |
| 2 | [General] Same Shear Rebar at I/J | `"OPT_SBAR_J"` | boolean | - | **Required** |
| 3 | [General] Cracked Section | `"OPT_CRACKED"` | boolean | - | **Required** |
| 4 | [General] Shear Reinforcement Items Constraints: · Items: 1 ~ 2 Index 0: i-section, Index 1: j-section | `"SBAR_ITEMS"` | Array [object] | - | **Required** |
| 4.1 | └ [General] Diagonal Reinforcement | `"OPT_DR"` | boolean | false | Optional |
| 4.2 | └ [General] Steel Bar for Web | `"OPT_SBW"` | boolean | false | Optional |
| 4.3 | └ [General] Torsional Reinforcement | `"OPT_TR"` | boolean | false | Optional |
| 4.4 | └ [General] Stirrup Exists | `"OPT_SR"` | boolean | false | Optional |
| 4.5 | └ [General] Enclosing Stirrup | `"OPT_LBAR_FLG"` | boolean | false | Optional |
| 4.6 | └ [When "OPT_DR" is true] [DR] Pitch | `"DR_PITCH"` | number | - | Optional |
| 4.7 | └ [When "OPT_DR" is true] [DR] Angle | `"DR_THETA"` | number | - | Optional |
| 4.8 | └ [When "OPT_DR" is true] [DR] Area | `"DR_AW"` | number | - | Optional |
| 4.9 | └ [When "OPT_SBW" is true] [SBW] Pitch | `"SBW_PITCH"` | number | - | Optional |
| 4.10 | └ [When "OPT_SBW" is true] [SBW] Angle | `"SBW_ANGLE"` | number | - | Optional |
| 4.11 | └ [When "OPT_SBW" is true] [SBW] Area | `"SBW_AP"` | number | - | Optional |
| 4.12 | └ [When "OPT_SBW" is true] [SBW] Pre-force | `"SBW_PS"` | number | - | Optional |
| 4.13 | └ [When "OPT_SBW" is true] [SBW] Shear Reduction Factor | `"SBW_FACTOR"` | number | - | Optional |
| 4.14 | └ [When "OPT_TR" is true] [TR] Pitch | `"TR_PITCH"` | number | - | Optional |
| 4.15 | └ [When "OPT_TR" is true] [TR] Area (Web) | `"TR_AWT"` | number | - | Optional |
| 4.16 | └ [When "OPT_TR" is true] [TR] Area (Long.) | `"TR_ALT"` | number | - | Optional |
| 4.17 | └ [When "OPT_SR" is true] [SR] Pitch | `"SR_PITCH"` | number | - | Optional |
| 4.18 | └ [When "OPT_SR" is true] [SR] Area | `"SR_AW"` | number | - | Optional |
| 4.19 | └ [When "OPT_LBAR_FLG" is true] Cover Thickness | `"LBAR_THICK"` | number | - | Optional |
| 4.20 | └ [When "OPT_LBAR_FLG" is true] Include Flange/Cantilever · Check off: "0" · Check on: "1" | `"LBAR_INC_FC"` | integer | - | Optional |
| 5 | [General] Longitudinal Reinforcement Constraints: · Items: 1 ~ 2 Index 0: i-section, Index 1: j-section | `"MBARS"` | Array [object] | - | **Required** |
| 5.1 | └ [General] Longitudinal Rebar Items Constraints: · Items: min 1 | `"MBAR_ITEMS"` | Array [object] | - | **Required** |
| 5.1.1 | 　　└ [General] Section Positions - I / J · I: "I" · J: "J" | `"IJ"` | string | - | **Required** |
| 5.1.2 | 　　└ [General] Bar Name | `"NAME"` | string | - | **Required** |
| 5.1.3 | 　　└ [General] Reference Y · Centroid: "0" · Left: "1" | `"REF_Y"` | integer | - | **Required** |
| 5.1.4 | 　　└ [General] Distance from Reference in Y direction | `"Y"` | number | 0 | Optional |
| 5.1.5 | 　　└ [General] Reference Z · Top: "0" · Bottom: "1" | `"REF_Z"` | integer | - | **Required** |
| 5.1.6 | 　　└ [General] Distance from Reference in Z Direction | `"Z"` | number | 0 | Optional |
| 5.1.7 | 　　└ [General] Number of Rebar Constraints: · Value Range: >= 1 | `"NUM"` | integer | - | **Required** |
| 5.1.8 | 　　└ [General] Spacing Constraints: · Value Range: >= 0 | `"SPACING"` | number | 0 | Optional |
| 5.1.9 | 　　└ [General] Part | `"PART"` | integer | - | **Required** |

**JSON Schema**

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
          "title": "RPSC Longitudinal Rebar",
          "type": "object",
          "description": "Section Manager - Reinforcements. Longitudinal reinforcement data for /db/RPSC.",
          "required": [
            "OPT_MBAR_J",
            "OPT_SBAR_J",
            "OPT_CRACKED",
            "SBAR_ITEMS",
            "MBARS"
          ],
          "additionalProperties": false,
          "properties": {
            "OPT_MBAR_J": {
              "type": "boolean",
              "description": "Same rebar data at I-end and J-end for longitudinal reinforcement.",
              "x-ui": {
                "groupId": "GENERAL",
                "label": "Same Longitudinal Rebar at I/J",
                "order": 1
              }
            },
            "OPT_SBAR_J": {
              "type": "boolean",
              "description": "Same shear rebar data at I-end and J-end.",
              "x-ui": {
                "groupId": "GENERAL",
                "label": "Same Shear Rebar at I/J",
                "order": 2
              }
            },
            "OPT_CRACKED": {
              "type": "boolean",
              "description": "Cracked section option.",
              "x-ui": {
                "groupId": "GENERAL",
                "label": "Cracked Section",
                "order": 3
              }
            },
            "SBAR_ITEMS": {
              "type": "array",
              "description": "Shear reinforcement data. Kept in this longitudinal schema because /db/RPSC requires the shear item list in the documented payload.",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "OPT_DR": {
                    "type": "boolean",
                    "description": "Diagonal reinforcement.",
                    "default": false,
                    "x-ui": {
                      "label": "Diagonal Reinforcement"
                    }
                  },
                  "DR_PITCH": {
                    "type": "number",
                    "description": "[DR] Pitch.",
                    "x-ui": {
                      "label": "[DR] Pitch"
                    },
                    "x-optional-when": {
                      "OPT_DR": true
                    }
                  },
                  "DR_THETA": {
                    "type": "number",
                    "description": "[DR] Angle.",
                    "x-ui": {
                      "label": "[DR] Angle"
                    },
                    "x-optional-when": {
                      "OPT_DR": true
                    }
                  },
                  "DR_AW": {
                    "type": "number",
                    "description": "[DR] Area.",
                    "x-ui": {
                      "label": "[DR] Area"
                    },
                    "x-optional-when": {
                      "OPT_DR": true
                    }
                  },
                  "OPT_SBW": {
                    "type": "boolean",
                    "description": "Steel bar for web.",
                    "default": false,
                    "x-ui": {
                      "label": "Steel Bar for Web"
                    }
                  },
                  "SBW_PITCH": {
                    "type": "number",
                    "description": "[SBW] Pitch.",
                    "x-ui": {
                      "label": "[SBW] Pitch"
                    },
                    "x-optional-when": {
                      "OPT_SBW": true
                    }
                  },
                  "SBW_ANGLE": {
                    "type": "number",
                    "description": "[SBW] Angle.",
                    "x-ui": {
                      "label": "[SBW] Angle"
                    },
                    "x-optional-when": {
                      "OPT_SBW": true
                    }
                  },
                  "SBW_AP": {
                    "type": "number",
                    "description": "[SBW] Area.",
                    "x-ui": {
                      "label": "[SBW] Area"
                    },
                    "x-optional-when": {
                      "OPT_SBW": true
                    }
                  },
                  "SBW_PS": {
                    "type": "number",
                    "description": "[SBW] Pre-force.",
                    "x-ui": {
                      "label": "[SBW] Pre-force"
                    },
                    "x-optional-when": {
                      "OPT_SBW": true
                    }
                  },
                  "SBW_FACTOR": {
                    "type": "number",
                    "description": "[SBW] Shear reduction factor.",
                    "x-ui": {
                      "label": "[SBW] Shear Reduction Factor"
                    },
                    "x-optional-when": {
                      "OPT_SBW": true
                    }
                  },
                  "OPT_TR": {
                    "type": "boolean",
                    "description": "Torsional reinforcement.",
                    "default": false,
                    "x-ui": {
                      "label": "Torsional Reinforcement"
                    }
                  },
                  "TR_PITCH": {
                    "type": "number",
                    "description": "[TR] Pitch.",
                    "x-ui": {
                      "label": "[TR] Pitch"
                    },
                    "x-optional-when": {
                      "OPT_TR": true
                    }
                  },
                  "TR_AWT": {
                    "type": "number",
                    "description": "[TR] Area (web).",
                    "x-ui": {
                      "label": "[TR] Area (Web)"
                    },
                    "x-optional-when": {
                      "OPT_TR": true
                    }
                  },
                  "TR_ALT": {
                    "type": "number",
                    "description": "[TR] Area (longitudinal).",
                    "x-ui": {
                      "label": "[TR] Area (Long.)"
                    },
                    "x-optional-when": {
                      "OPT_TR": true
                    }
                  },
                  "OPT_SR": {
                    "type": "boolean",
                    "description": "Stirrup exists.",
                    "default": false,
                    "x-ui": {
                      "label": "Stirrup Exists"
                    }
                  },
                  "SR_PITCH": {
                    "type": "number",
                    "description": "[SR] Pitch.",
                    "x-ui": {
                      "label": "[SR] Pitch"
                    },
                    "x-optional-when": {
                      "OPT_SR": true
                    }
                  },
                  "SR_AW": {
                    "type": "number",
                    "description": "[SR] Area.",
                    "x-ui": {
                      "label": "[SR] Area"
                    },
                    "x-optional-when": {
                      "OPT_SR": true
                    }
                  },
                  "OPT_LBAR_FLG": {
                    "type": "boolean",
                    "description": "Enclosing stirrup.",
                    "default": false,
                    "x-ui": {
                      "label": "Enclosing Stirrup"
                    }
                  },
                  "LBAR_THICK": {
                    "type": "number",
                    "description": "Cover thickness for enclosed section area.",
                    "x-ui": {
                      "label": "Cover Thickness"
                    },
                    "x-optional-when": {
                      "OPT_LBAR_FLG": true
                    }
                  },
                  "LBAR_INC_FC": {
                    "type": "integer",
                    "description": "Include flange/cantilever. 0: check off, 1: check on.",
                    "enum": [
                      0,
                      1
                    ],
                    "x-ui": {
                      "label": "Include Flange/Cantilever"
                    },
                    "x-enum-labels": [
                      "Check off",
                      "Check on"
                    ],
                    "x-optional-when": {
                      "OPT_LBAR_FLG": true
                    }
                  }
                }
              },
              "minItems": 1,
              "maxItems": 2,
              "x-ui": {
                "component": "Table",
                "groupId": "SHEAR_MIN",
                "label": "Shear Reinforcement Items",
                "order": 4,
                "hint": " Index 0: i-section, Index 1: j-section"
              }
            },
            "MBARS": {
              "type": "array",
              "description": "Longitudinal reinforcement properties. Index 0 is I-section, index 1 is J-section when OPT_MBAR_J is false.",
              "items": {
                "type": "object",
                "required": [
                  "MBAR_ITEMS"
                ],
                "additionalProperties": false,
                "properties": {
                  "MBAR_ITEMS": {
                    "type": "array",
                    "description": "Longitudinal reinforcement property details.",
                    "items": {
                      "type": "object",
                      "required": [
                        "IJ",
                        "NAME",
                        "REF_Y",
                        "REF_Z",
                        "NUM",
                        "PART"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "IJ": {
                          "type": "string",
                          "description": "Section position.",
                          "enum": [
                            "I",
                            "J"
                          ],
                          "x-ui": {
                            "label": "Section Positions - I / J",
                            "order": 1
                          }
                        },
                        "NAME": {
                          "type": "string",
                          "description": "Bar name.",
                          "x-ui": {
                            "label": "Bar Name",
                            "order": 2
                          }
                        },
                        "REF_Y": {
                          "type": "integer",
                          "description": "Reference Y. 0: centroid, 1: left.",
                          "enum": [
                            0,
                            1
                          ],
                          "x-ui": {
                            "label": "Reference Y",
                            "order": 3
                          },
                          "x-enum-labels": [
                            "Centroid",
                            "Left"
                          ]
                        },
                        "Y": {
                          "type": "number",
                          "description": "Distance from reference in Y direction.",
                          "default": 0,
                          "x-ui": {
                            "label": "Distance from Reference in Y direction",
                            "order": 4
                          }
                        },
                        "REF_Z": {
                          "type": "integer",
                          "description": "Reference Z. 0: top, 1: bottom.",
                          "enum": [
                            0,
                            1
                          ],
                          "x-ui": {
                            "label": "Reference Z",
                            "order": 5
                          },
                          "x-enum-labels": [
                            "Top",
                            "Bottom"
                          ]
                        },
                        "Z": {
                          "type": "number",
                          "description": "Distance from reference in Z direction.",
                          "default": 0,
                          "x-ui": {
                            "label": "Distance from Reference in Z Direction",
                            "order": 6
                          }
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars.",
                          "minimum": 1,
                          "x-ui": {
                            "label": "Number of Rebar",
                            "order": 7
                          }
                        },
                        "SPACING": {
                          "type": "number",
                          "description": "Spacing between rebars.",
                          "default": 0,
                          "minimum": 0,
                          "x-ui": {
                            "label": "Spacing",
                            "order": 8
                          }
                        },
                        "PART": {
                          "type": "integer",
                          "description": "Part.",
                          "x-ui": {
                            "label": "Part",
                            "order": 9
                          }
                        }
                      },
                      "x-ui": {
                        "label": "Longitudinal Rebar Item"
                      }
                    },
                    "minItems": 1,
                    "x-ui": {
                      "component": "Table",
                      "label": "Longitudinal Rebar Items"
                    }
                  }
                }
              },
              "minItems": 1,
              "maxItems": 2,
              "x-ui": {
                "component": "Table",
                "groupId": "LONGI",
                "label": "Longitudinal Reinforcement",
                "order": 5,
                "hint": " Index 0: i-section, Index 1: j-section"
              }
            }
          },
          "allOf": [
            {
              "if": {
                "properties": {
                  "OPT_MBAR_J": {
                    "const": true
                  }
                }
              },
              "then": {
                "properties": {
                  "MBARS": {
                    "minItems": 1,
                    "maxItems": 1
                  }
                }
              }
            },
            {
              "if": {
                "properties": {
                  "OPT_MBAR_J": {
                    "const": false
                  }
                }
              },
              "then": {
                "properties": {
                  "MBARS": {
                    "minItems": 2,
                    "maxItems": 2
                  }
                }
              }
            },
            {
              "if": {
                "properties": {
                  "OPT_SBAR_J": {
                    "const": true
                  }
                }
              },
              "then": {
                "properties": {
                  "SBAR_ITEMS": {
                    "minItems": 1,
                    "maxItems": 1
                  }
                }
              }
            },
            {
              "if": {
                "properties": {
                  "OPT_SBAR_J": {
                    "const": false
                  }
                }
              },
              "then": {
                "properties": {
                  "SBAR_ITEMS": {
                    "minItems": 1,
                    "maxItems": 2
                  }
                }
              }
            }
          ],
          "x-ui": {
            "groups": [
              {
                "title": "General Options",
                "id": "GENERAL"
              },
              {
                "title": "Shear Reinforcement Flags",
                "id": "SHEAR_MIN"
              },
              {
                "title": "Longitudinal Rebar",
                "id": "LONGI"
              }
            ]
          }
        }
      }
    }
  }
}
```


---

## 7. `SECF` — Longitudinal Rebar-Stiffness

> **기능** 종방향 철근의 강성 산정 정보를 입력합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/SECF
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 57946987740569](https://support.midasuser.com/hc/en-us/articles/57946987740569)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object. Each property name is a section ID string. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Items | `"ITEMS"` | array [object] | - | **Required** |
| 1.1 | └ [General] ID | `"ID"` | integer | 0 | Optional |
| 1.2 | └ [General] NameofBoundaryGroup | `"GROUP_NAME"` | string |  | Optional |
| 1.3 | └ [General] Area | `"AREA_SF"` | number | 1 | Optional |
| 1.4 | └ [General] AxisYEffectiveShearArea | `"ASY_SF"` | number | 1 | Optional |
| 1.5 | └ [General] AxisZEffectiveShearArea | `"ASZ_SF"` | number | 1 | Optional |
| 1.6 | └ [General] TorsionalResistance | `"IXX_SF"` | number | 1 | Optional |
| 1.7 | └ [General] AxisYAreaMomentofInertia | `"IYY_SF"` | number | 1 | Optional |
| 1.8 | └ [General] AxisZAreaMomentofInertia | `"IZZ_SF"` | number | 1 | Optional |
| 1.9 | └ [General] Weight | `"WGT_SF"` | number | 1 | Optional |
| 1.10 | └ [General] W | `"W_SF"` | number | 1 | Optional |
| 1.11 | └ [General] Part. 1: Before, 2: After, 3: Before and After. Composite sections only: steel composite lets the user choose; concrete composite uses 3. Other sections use 1. · Before: 1 · After: 2 · Before and After: 3 | `"IPART"` | integer | 1 | Optional |
| 1.12 | └ [General] DifferentI=JBoolean. Tapered sections only; other sections always store the same scale factors at I and J. | `"bDiffIJ"` | boolean | true | Optional |
| 1.13 | └ [General] J1 | `"J1"` | number | 1 | Optional |
| 1.14 | └ [General] J2 | `"J2"` | number | 1 | Optional |
| 1.15 | └ [General] J3 | `"J3"` | number | 1 | Optional |
| 1.16 | └ [General] J4 | `"J4"` | number | 1 | Optional |
| 1.17 | └ [General] J5 | `"J5"` | number | 1 | Optional |
| 1.18 | └ [General] J6 | `"J6"` | number | 1 | Optional |
| 1.19 | └ [General] J7 | `"J7"` | number | 1 | Optional |
| 1.20 | └ [General] J8 | `"J8"` | number | 1 | Optional |

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
      "description": "Keyed object. Each property name is a section ID string.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Section Manager - Stiffness",
          "type": "object",
          "description": "Section Manager - Stiffness data for /db/SECF.",
          "required": [
            "ITEMS"
          ],
          "additionalProperties": false,
          "properties": {
            "ITEMS": {
              "description": "Items",
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "ID": {
                    "description": "ID",
                    "type": "integer",
                    "default": 0
                  },
                  "GROUP_NAME": {
                    "description": "NameofBoundaryGroup",
                    "type": "string",
                    "default": ""
                  },
                  "AREA_SF": {
                    "description": "Area",
                    "type": "number",
                    "default": 1
                  },
                  "ASY_SF": {
                    "description": "AxisYEffectiveShearArea",
                    "type": "number",
                    "default": 1
                  },
                  "ASZ_SF": {
                    "description": "AxisZEffectiveShearArea",
                    "type": "number",
                    "default": 1
                  },
                  "IXX_SF": {
                    "description": "TorsionalResistance",
                    "type": "number",
                    "default": 1
                  },
                  "IYY_SF": {
                    "description": "AxisYAreaMomentofInertia",
                    "type": "number",
                    "default": 1
                  },
                  "IZZ_SF": {
                    "description": "AxisZAreaMomentofInertia",
                    "type": "number",
                    "default": 1
                  },
                  "WGT_SF": {
                    "description": "Weight",
                    "type": "number",
                    "default": 1
                  },
                  "W_SF": {
                    "description": "W",
                    "type": "number",
                    "default": 1
                  },
                  "IPART": {
                    "description": "Part. 1: Before, 2: After, 3: Before and After. Composite sections only: steel composite lets the user choose; concrete composite uses 3. Other sections use 1.",
                    "type": "integer",
                    "enum": [
                      1,
                      2,
                      3
                    ],
                    "default": 1
                  },
                  "bDiffIJ": {
                    "description": "DifferentI=JBoolean. Tapered sections only; other sections always store the same scale factors at I and J.",
                    "type": "boolean",
                    "default": true
                  },
                  "J1": {
                    "description": "J1",
                    "type": "number",
                    "default": 1
                  },
                  "J2": {
                    "description": "J2",
                    "type": "number",
                    "default": 1
                  },
                  "J3": {
                    "description": "J3",
                    "type": "number",
                    "default": 1
                  },
                  "J4": {
                    "description": "J4",
                    "type": "number",
                    "default": 1
                  },
                  "J5": {
                    "description": "J5",
                    "type": "number",
                    "default": 1
                  },
                  "J6": {
                    "description": "J6",
                    "type": "number",
                    "default": 1
                  },
                  "J7": {
                    "description": "J7",
                    "type": "number",
                    "default": 1
                  },
                  "J8": {
                    "description": "J8",
                    "type": "number",
                    "default": 1
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

- `SECF`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "",
          "AREA_SF": 1.05,
          "ASY_SF": 0.95,
          "ASZ_SF": 0.95,
          "IXX_SF": 0.9,
          "IYY_SF": 1.1,
          "IZZ_SF": 1.1,
          "WGT_SF": 1.0,
          "W_SF": 1.0,
          "IPART": 1,
          "bDiffIJ": false
        }
      ]
    }
  }
}
```

**Response**

```json
{
  "SECF": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "",
          "AREA_SF": 1.05,
          "ASY_SF": 0.95,
          "ASZ_SF": 0.95,
          "IXX_SF": 0.9,
          "IYY_SF": 1.1,
          "IZZ_SF": 1.1,
          "WGT_SF": 1.0,
          "W_SF": 1.0,
          "IPART": 1,
          "bDiffIJ": false
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/SECF"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "",
          "AREA_SF": 1.05,
          "ASY_SF": 0.95,
          "ASZ_SF": 0.95,
          "IXX_SF": 0.9,
          "IYY_SF": 1.1,
          "IZZ_SF": 1.1,
          "WGT_SF": 1.0,
          "W_SF": 1.0,
          "IPART": 1,
          "bDiffIJ": false
        }
      ]
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```

### 이전 한국어 원문

**원문** [한국어 57946974912921](https://support.midasuser.com/hc/ko/articles/57946974912921)

**원문 Active Methods** `POST` · `GET` · `PUT` · `DELETE`

> ⚠️ 영문 Schema는 IPART를 1·2·3으로 제한합니다. 이전 Schema는 SECTION_TYPE이 COMPOSITE일 때의 조건을 확장 속성에 설명합니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object. Each property name is a section ID string. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Items Constraints: · Items: min 1 | `"ITEMS"` | Array [object] | - | **Required** |
| 1.1 | └ [General] ID | `"ID"` | integer | 0 | Optional |
| 1.2 | └ [General] NameofBoundaryGroup | `"GROUP_NAME"` | string | "" | Optional |
| 1.3 | └ [General] Area | `"AREA_SF"` | number | 1 | Optional |
| 1.4 | └ [General] AxisYEffectiveShearArea | `"ASY_SF"` | number | 1 | Optional |
| 1.5 | └ [General] AxisZEffectiveShearArea | `"ASZ_SF"` | number | 1 | Optional |
| 1.6 | └ [General] TorsionalResistance | `"IXX_SF"` | number | 1 | Optional |
| 1.7 | └ [General] AxisYAreaMomentofInertia | `"IYY_SF"` | number | 1 | Optional |
| 1.8 | └ [General] AxisZAreaMomentofInertia | `"IZZ_SF"` | number | 1 | Optional |
| 1.9 | └ [General] Weight | `"WGT_SF"` | number | 1 | Optional |
| 1.10 | └ [General] W | `"W_SF"` | number | 1 | Optional |
| 1.11 | └ [General] J2 | `"J2"` | number | 1 | Optional |
| 1.12 | └ [General] J3 | `"J3"` | number | 1 | Optional |
| 1.13 | └ [General] J4 | `"J4"` | number | 1 | Optional |
| 1.14 | └ [General] J5 | `"J5"` | number | 1 | Optional |
| 1.15 | └ [General] J6 | `"J6"` | number | 1 | Optional |
| 1.16 | └ [General] J7 | `"J7"` | number | 1 | Optional |
| 1.17 | └ [General] J8 | `"J8"` | number | 1 | Optional |
| 1.18 | └ [When "SECTION_TYPE" is COMPOSITE] Part | `"IPART"` | integer | 1 | Optional |
| 1.19 | └ [When "SECTION_TYPE" is COMPOSITE] DifferentI=JBoolean | `"bDiffIJ"` | boolean | true | Optional |
| 1.20 | └ [When "SECTION_TYPE" is COMPOSITE] J1 | `"J1"` | number | 1 | Optional |

**JSON Schema**

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
      "description": "Keyed object. Each property name is a section ID string.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Section Manager - Stiffness",
          "type": "object",
          "description": "Section Manager - Stiffness data for /db/SECF.",
          "required": [
            "ITEMS"
          ],
          "additionalProperties": false,
          "properties": {
            "ITEMS": {
              "description": "Items",
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "ID": {
                    "description": "ID",
                    "type": "integer",
                    "default": 0
                  },
                  "GROUP_NAME": {
                    "description": "NameofBoundaryGroup",
                    "type": "string",
                    "default": ""
                  },
                  "AREA_SF": {
                    "description": "Area",
                    "type": "number",
                    "default": 1
                  },
                  "ASY_SF": {
                    "description": "AxisYEffectiveShearArea",
                    "type": "number",
                    "default": 1
                  },
                  "ASZ_SF": {
                    "description": "AxisZEffectiveShearArea",
                    "type": "number",
                    "default": 1
                  },
                  "IXX_SF": {
                    "description": "TorsionalResistance",
                    "type": "number",
                    "default": 1
                  },
                  "IYY_SF": {
                    "description": "AxisYAreaMomentofInertia",
                    "type": "number",
                    "default": 1
                  },
                  "IZZ_SF": {
                    "description": "AxisZAreaMomentofInertia",
                    "type": "number",
                    "default": 1
                  },
                  "WGT_SF": {
                    "description": "Weight",
                    "type": "number",
                    "default": 1
                  },
                  "W_SF": {
                    "description": "W",
                    "type": "number",
                    "default": 1
                  },
                  "IPART": {
                    "description": "Part",
                    "type": "integer",
                    "default": 1,
                    "x-optional-when": {
                      "SECTION_TYPE": "COMPOSITE"
                    }
                  },
                  "bDiffIJ": {
                    "description": "DifferentI=JBoolean",
                    "type": "boolean",
                    "default": true,
                    "x-optional-when": {
                      "SECTION_TYPE": "COMPOSITE"
                    }
                  },
                  "J1": {
                    "description": "J1",
                    "type": "number",
                    "default": 1,
                    "x-optional-when": {
                      "SECTION_TYPE": "COMPOSITE"
                    }
                  },
                  "J2": {
                    "description": "J2",
                    "type": "number",
                    "default": 1
                  },
                  "J3": {
                    "description": "J3",
                    "type": "number",
                    "default": 1
                  },
                  "J4": {
                    "description": "J4",
                    "type": "number",
                    "default": 1
                  },
                  "J5": {
                    "description": "J5",
                    "type": "number",
                    "default": 1
                  },
                  "J6": {
                    "description": "J6",
                    "type": "number",
                    "default": 1
                  },
                  "J7": {
                    "description": "J7",
                    "type": "number",
                    "default": 1
                  },
                  "J8": {
                    "description": "J8",
                    "type": "number",
                    "default": 1
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


---

## 8. `STRPSSM` — Longitudinal Rebar-Stress Points

> **기능** 종방향 철근의 응력 산정 위치를 입력합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/STRPSSM
```

### Active Methods

`POST` · `GET` · `DELETE` · `PUT`

### Specifications

**원문** [영문 64738109002649](https://support.midasuser.com/hc/en-us/articles/64738109002649)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Map of section IDs. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Same Additional Stress Points Data at i & j-end | `"OPT_SAME_J"` | boolean | true | Optional |
| 2 | [General] Point Size 1 | `"POINT_SIZE_1"` | integer | - | **Required** |
| 3 | [General] Point Size 2 | `"POINT_SIZE_2"` | integer | - | **Required** |
| 4 | [General] PointData1 | `"POINT1"` | array [object] | - | **Required** |
| 4.1 | └ [General] PointY | `"Y"` | number | - | **Required** |
| 4.2 | └ [General] PointZ | `"Z"` | number | - | **Required** |
| 5 | [General] PointData2 | `"POINT2"` | array [object] | - | **Required** |
| 5.1 | └ [General] PointY | `"Y"` | number | - | **Required** |
| 5.2 | └ [General] PointZ | `"Z"` | number | - | **Required** |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "STRPSSM API Schema",
  "type": "object",
  "description": "Stress point settings for section manager (DB/STRPSSM).",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Map of section IDs.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "POINT_SIZE_1",
            "POINT_SIZE_2",
            "POINT1",
            "POINT2"
          ],
          "additionalProperties": false,
          "properties": {
            "OPT_SAME_J": {
              "description": "Same Additional Stress Points Data at i & j-end",
              "type": "boolean",
              "default": true
            },
            "POINT_SIZE_1": {
              "description": "Point Size 1",
              "type": "integer"
            },
            "POINT_SIZE_2": {
              "description": "Point Size 2",
              "type": "integer"
            },
            "POINT1": {
              "description": "PointData1",
              "type": "array",
              "items": {
                "type": "object",
                "required": [
                  "Y",
                  "Z"
                ],
                "additionalProperties": false,
                "properties": {
                  "Y": {
                    "description": "PointY",
                    "type": "number"
                  },
                  "Z": {
                    "description": "PointZ",
                    "type": "number"
                  }
                }
              }
            },
            "POINT2": {
              "description": "PointData2",
              "type": "array",
              "items": {
                "type": "object",
                "required": [
                  "Y",
                  "Z"
                ],
                "additionalProperties": false,
                "properties": {
                  "Y": {
                    "description": "PointY",
                    "type": "number"
                  },
                  "Z": {
                    "description": "PointZ",
                    "type": "number"
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

- `STRPSSM`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "OPT_SAME_J": false,
      "POINT_SIZE_1": 6,
      "POINT_SIZE_2": 6,
      "POINT1": [
        {
          "Y": -1.2,
          "Z": 0.75
        },
        {
          "Y": 1.2,
          "Z": 0.75
        },
        {
          "Y": 0.13,
          "Z": 0.2
        },
        {
          "Y": 0.33,
          "Z": -0.8
        },
        {
          "Y": -0.33,
          "Z": -0.8
        },
        {
          "Y": -0.13,
          "Z": 0.2
        }
      ],
      "POINT2": [
        {
          "Y": -1.2,
          "Z": 0.7
        },
        {
          "Y": 1.2,
          "Z": 0.7
        },
        {
          "Y": 0.13,
          "Z": 0.0
        },
        {
          "Y": 0.33,
          "Z": -0.85
        },
        {
          "Y": -0.33,
          "Z": -0.85
        },
        {
          "Y": -0.13,
          "Z": 0.0
        }
      ]
    }
  }
}
```

**Response**

```json
{
  "STRPSSM": {
    "1": {
      "OPT_SAME_J": false,
      "POINT_SIZE_1": 6,
      "POINT_SIZE_2": 6,
      "POINT1": [
        {
          "Y": -1.2,
          "Z": 0.75
        },
        {
          "Y": 1.2,
          "Z": 0.75
        },
        {
          "Y": 0.13,
          "Z": 0.2
        },
        {
          "Y": 0.33,
          "Z": -0.8
        },
        {
          "Y": -0.33,
          "Z": -0.8
        },
        {
          "Y": -0.13,
          "Z": 0.2
        }
      ],
      "POINT2": [
        {
          "Y": -1.2,
          "Z": 0.7
        },
        {
          "Y": 1.2,
          "Z": 0.7
        },
        {
          "Y": 0.13,
          "Z": 0.0
        },
        {
          "Y": 0.33,
          "Z": -0.85
        },
        {
          "Y": -0.33,
          "Z": -0.85
        },
        {
          "Y": -0.13,
          "Z": 0.0
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/STRPSSM"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "OPT_SAME_J": false,
      "POINT_SIZE_1": 6,
      "POINT_SIZE_2": 6,
      "POINT1": [
        {
          "Y": -1.2,
          "Z": 0.75
        },
        {
          "Y": 1.2,
          "Z": 0.75
        },
        {
          "Y": 0.13,
          "Z": 0.2
        },
        {
          "Y": 0.33,
          "Z": -0.8
        },
        {
          "Y": -0.33,
          "Z": -0.8
        },
        {
          "Y": -0.13,
          "Z": 0.2
        }
      ],
      "POINT2": [
        {
          "Y": -1.2,
          "Z": 0.7
        },
        {
          "Y": 1.2,
          "Z": 0.7
        },
        {
          "Y": 0.13,
          "Z": 0.0
        },
        {
          "Y": 0.33,
          "Z": -0.85
        },
        {
          "Y": -0.33,
          "Z": -0.85
        },
        {
          "Y": -0.13,
          "Z": 0.0
        }
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

## 9. `DIDP` — Design Position

> **기능** PSC 설계를 수행할 위치를 지정합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/DIDP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 58078143157785](https://support.midasuser.com/hc/en-us/articles/58078143157785)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings, where each entry represents an element (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Moment Type · None: 0 · I: 1 · J: 2 · I & J: 3 | `"MOMENT_TYPE"` | integer | - | **Required** |
| 2 | [General] Shear Type · None: 0 · I: 1 · J: 2 · I & J: 3 | `"SHEAR_TYPE"` | integer | - | **Required** |

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
      "description": "Object keyed by ID strings, where each entry represents an element (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "MOMENT_TYPE",
            "SHEAR_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "MOMENT_TYPE": {
              "type": "integer",
              "description": "Moment Type",
              "enum": [
                0,
                1,
                2,
                3
              ]
            },
            "SHEAR_TYPE": {
              "type": "integer",
              "description": "Shear Type",
              "enum": [
                0,
                1,
                2,
                3
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

- `DIDP`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "MOMENT_TYPE": 0,
      "SHEAR_TYPE": 0
    },
    "2": {
      "MOMENT_TYPE": 1,
      "SHEAR_TYPE": 1
    },
    "3": {
      "MOMENT_TYPE": 2,
      "SHEAR_TYPE": 2
    },
    "4": {
      "MOMENT_TYPE": 3,
      "SHEAR_TYPE": 3
    },
    "5": {
      "MOMENT_TYPE": 3,
      "SHEAR_TYPE": 1
    },
    "6": {
      "MOMENT_TYPE": 1,
      "SHEAR_TYPE": 3
    }
  }
}
```

**Response**

```json
{
  "DIDP": {
    "1": {
      "MOMENT_TYPE": 0,
      "SHEAR_TYPE": 0
    },
    "2": {
      "MOMENT_TYPE": 1,
      "SHEAR_TYPE": 1
    },
    "3": {
      "MOMENT_TYPE": 2,
      "SHEAR_TYPE": 2
    },
    "4": {
      "MOMENT_TYPE": 3,
      "SHEAR_TYPE": 3
    },
    "5": {
      "MOMENT_TYPE": 3,
      "SHEAR_TYPE": 1
    },
    "6": {
      "MOMENT_TYPE": 1,
      "SHEAR_TYPE": 3
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/DIDP"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "MOMENT_TYPE": 0,
      "SHEAR_TYPE": 0
    },
    "2": {
      "MOMENT_TYPE": 1,
      "SHEAR_TYPE": 1
    },
    "3": {
      "MOMENT_TYPE": 2,
      "SHEAR_TYPE": 2
    },
    "4": {
      "MOMENT_TYPE": 3,
      "SHEAR_TYPE": 3
    },
    "5": {
      "MOMENT_TYPE": 3,
      "SHEAR_TYPE": 1
    },
    "6": {
      "MOMENT_TYPE": 1,
      "SHEAR_TYPE": 3
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 10. `DIOP` — Output Position

> **기능** PSC 설계 결과의 출력 위치를 지정합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/DIOP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 58078690517017](https://support.midasuser.com/hc/en-us/articles/58078690517017)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings, where each entry represents an element (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Moment Strength | `"MOMENT_STRENGTH"` | object | - | **Required** |
| 1.1 | └ [General] Positive Moment · None: 0 · I: 1 · J: 2 · I & J: 3 | `"POSITIVE_MOMENT"` | integer | - | **Required** |
| 1.2 | └ [General] Negative Moment · None: 0 · I: 1 · J: 2 · I & J: 3 | `"NEGATIVE_MOMENT"` | integer | - | **Required** |
| 2 | [General] Shear Type · None: 0 · I: 1 · J: 2 · I & J: 3 | `"SHEAR_TYPE"` | integer | - | **Required** |
| 3 | [General] Torsion Type · None: 0 · I: 1 · J: 2 · I & J: 3 | `"TORSION_TYPE"` | integer | - | **Required** |

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
      "description": "Object keyed by ID strings, where each entry represents an element (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "MOMENT_STRENGTH",
            "SHEAR_TYPE",
            "TORSION_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "MOMENT_STRENGTH": {
              "type": "object",
              "description": "Moment Strength",
              "additionalProperties": false,
              "required": [
                "POSITIVE_MOMENT",
                "NEGATIVE_MOMENT"
              ],
              "properties": {
                "POSITIVE_MOMENT": {
                  "type": "integer",
                  "description": "Positive Moment",
                  "enum": [
                    0,
                    1,
                    2,
                    3
                  ]
                },
                "NEGATIVE_MOMENT": {
                  "type": "integer",
                  "description": "Negative Moment",
                  "enum": [
                    0,
                    1,
                    2,
                    3
                  ]
                }
              }
            },
            "SHEAR_TYPE": {
              "type": "integer",
              "description": "Shear Type",
              "enum": [
                0,
                1,
                2,
                3
              ]
            },
            "TORSION_TYPE": {
              "type": "integer",
              "description": "Torsion Type",
              "enum": [
                0,
                1,
                2,
                3
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

- `DIOP`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "46": {
      "SHEAR_TYPE": 0,
      "TORSION_TYPE": 0,
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      }
    }
  }
}
```

**Response**

```json
{
  "DIOP": {
    "46": {
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      },
      "SHEAR_TYPE": 0,
      "TORSION_TYPE": 0
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/DIOP"

payload = json.loads(r'''
{
  "Assign": {
    "46": {
      "SHEAR_TYPE": 0,
      "TORSION_TYPE": 0,
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
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

## 11. `PSC-ANAL` — Perform Design

> **기능** PSC 설계를 수행합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/PSC-ANAL
```

### Active Methods

`POST`

### Specifications

**원문** [영문 57947090728857](https://support.midasuser.com/hc/en-us/articles/57947090728857)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] PSC Perform Design | `"TYPE"` | string | PSC_PERFORM_DESIGN | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "PSC Perform Design",
          "type": "object",
          "required": [
            "TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "TYPE": {
              "type": "string",
              "description": "PSC Perform Design",
              "default": "PSC_PERFORM_DESIGN"
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

- `PSC_PERFORM_RESPONSE`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "1": {
      "TYPE": "PSC_PERFORM_DESIGN"
    }
  }
}
```

**Response**

```json
{
  "PSC_PERFORM_RESPONSE": {
    "SUCCESS": true,
    "MESSAGE": ""
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/PSC-ANAL"

payload = json.loads(r'''
{
  "Argument": {
    "1": {
      "TYPE": "PSC_PERFORM_DESIGN"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```

### 이전 한국어 원문

**원문** [한국어 57947082529945](https://support.midasuser.com/hc/ko/articles/57947082529945)

**원문 Active Methods** `POST`

> ⚠️ 이전 Schema의 TYPE 기본값은 "PSC_Perform_Design"이고, 영문 Schema와 최신 요청 예제는 "PSC_PERFORM_DESIGN"을 사용합니다.

**Specifications**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] PSC Perform Design | `"TYPE"` | string | "PSC_Perform_Design" | **Required** |

**JSON Schema**

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
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "PSC Perform Design",
          "type": "object",
          "required": [
            "TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "TYPE": {
              "type": "string",
              "description": "PSC Perform Design",
              "default": "PSC_Perform_Design"
            }
          }
        }
      }
    }
  }
}
```


---

## 12. `TABLE` · `PSC_DGN_FORCE` — Design Forces

> **기능** PSC 설계에 사용한 부재력을 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58329976060057](https://support.midasuser.com/hc/en-us/articles/58329976060057)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · PSC_DGN_FORCE | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 7.3 | └ [General] Specify Structure Group Name | `"STRUCTURE_GROUP_NAME"` | string | - | Optional |
| 8 | [General] Element Parts | `"PARTS"` | array | ["All"] | Optional |

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
            "PSC_DGN_FORCE"
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
              "Elem",
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
          }
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
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

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `TEST` — `Index`, `Elem`, `Part`, `LComName`, `Type`, `Fx`, `Fy`, `Fz`, `Mx`, `My`, `Mz`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_DGN_FORCE",
    "COMPONENTS": [
      "Elem",
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
      "PartI",
      "PartJ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    }
  }
}
```

**Response**

```json
{
  "TEST": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
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
        "1",
        "I",
        "t1",
        "-",
        "-522.3250",
        "160.5134",
        "5251.2995",
        "127261.6960",
        "-190141.3440",
        "855.3526"
      ],
      [
        "2",
        "1",
        "I",
        "t2",
        "-",
        "-44887.8440",
        "-24.0405",
        "6097.2835",
        "-660.3240",
        "-26261.9340",
        "790.3708"
      ],
      [
        "3",
        "1",
        "I",
        "t3",
        "-",
        "-1.5914",
        "0.4888",
        "17.0109",
        "386.9365",
        "-578.5244",
        "2.6056"
      ],
      [
        "4",
        "1",
        "I",
        "t4",
        "-",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "5",
        "1",
        "I",
        "cLCB1",
        "FX-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "6",
        "1",
        "I",
        "cLCB1",
        "FX-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "7",
        "1",
        "I",
        "cLCB1",
        "FY-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "8",
        "1",
        "I",
        "cLCB1",
        "FY-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "9",
        "1",
        "I",
        "cLCB1",
        "FZ-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "10",
        "1",
        "I",
        "cLCB1",
        "FZ-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "11",
        "1",
        "I",
        "cLCB1",
        "MX-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "12",
        "1",
        "I",
        "cLCB1",
        "MX-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "13",
        "1",
        "I",
        "cLCB1",
        "MY-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "14",
        "1",
        "I",
        "cLCB1",
        "MY-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "15",
        "1",
        "I",
        "cLCB1",
        "MZ-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "16",
        "1",
        "I",
        "cLCB1",
        "MZ-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "17",
        "1",
        "I",
        "cLCB2",
        "FX-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "18",
        "1",
        "I",
        "cLCB2",
        "FX-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "19",
        "1",
        "I",
        "cLCB2",
        "FY-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "20",
        "1",
        "I",
        "cLCB2",
        "FY-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "21",
        "1",
        "I",
        "cLCB2",
        "FZ-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "22",
        "1",
        "I",
        "cLCB2",
        "FZ-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "23",
        "1",
        "I",
        "cLCB2",
        "MX-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "24",
        "1",
        "I",
        "cLCB2",
        "MX-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "25",
        "1",
        "I",
        "cLCB2",
        "MY-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "26",
        "1",
        "I",
        "cLCB2",
        "MY-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "27",
        "1",
        "I",
        "cLCB2",
        "MZ-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "28",
        "1",
        "I",
        "cLCB2",
        "MZ-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "29",
        "1",
        "I",
        "cLCB3",
        "-",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "30",
        "1",
        "I",
        "cLCB4",
        "-",
        "-46007.9836",
        "168.4733",
        "14315.5996",
        "196538.7951",
        "-321023.6989",
        "2324.9512"
      ],
      [
        "31",
        "1",
        "I",
        "cLCB5",
        "FX-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "32",
        "1",
        "I",
        "cLCB5",
        "FX-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "33",
        "1",
        "I",
        "cLCB5",
        "FY-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "34",
        "1",
        "I",
        "cLCB5",
        "FY-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "35",
        "1",
        "I",
        "cLCB5",
        "FZ-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "36",
        "1",
        "I",
        "cLCB5",
        "FZ-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "37",
        "1",
        "I",
        "cLCB5",
        "MX-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "38",
        "1",
        "I",
        "cLCB5",
        "MX-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "39",
        "1",
        "I",
        "cLCB5",
        "MY-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "40",
        "1",
        "I",
        "cLCB5",
        "MY-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "41",
        "1",
        "I",
        "cLCB5",
        "MZ-MAX",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "42",
        "1",
        "I",
        "cLCB5",
        "MZ-MIN",
        "-45873.2269",
        "127.0693",
        "12964.1416",
        "163703.3968",
        "-271969.5049",
        "2104.2934"
      ],
      [
        "43",
        "1",
        "I",
        "cLCB6",
        "FX-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "44",
        "1",
        "I",
        "cLCB6",
        "FX-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "45",
        "1",
        "I",
        "cLCB6",
        "FY-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "46",
        "1",
        "I",
        "cLCB6",
        "FY-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "47",
        "1",
        "I",
        "cLCB6",
        "FZ-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "48",
        "1",
        "I",
        "cLCB6",
        "FZ-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "49",
        "1",
        "I",
        "cLCB6",
        "MX-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "50",
        "1",
        "I",
        "cLCB6",
        "MX-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "51",
        "1",
        "I",
        "cLCB6",
        "MY-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "52",
        "1",
        "I",
        "cLCB6",
        "MY-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "53",
        "1",
        "I",
        "cLCB6",
        "MZ-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "54",
        "1",
        "I",
        "cLCB6",
        "MZ-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "55",
        "1",
        "I",
        "cLCB7",
        "FX-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "56",
        "1",
        "I",
        "cLCB7",
        "FX-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "57",
        "1",
        "I",
        "cLCB7",
        "FY-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "58",
        "1",
        "I",
        "cLCB7",
        "FY-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "59",
        "1",
        "I",
        "cLCB7",
        "FZ-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "60",
        "1",
        "I",
        "cLCB7",
        "FZ-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "61",
        "1",
        "I",
        "cLCB7",
        "MX-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "62",
        "1",
        "I",
        "cLCB7",
        "MX-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "63",
        "1",
        "I",
        "cLCB7",
        "MY-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "64",
        "1",
        "I",
        "cLCB7",
        "MY-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "65",
        "1",
        "I",
        "cLCB7",
        "MZ-MAX",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "66",
        "1",
        "I",
        "cLCB7",
        "MZ-MIN",
        "-45781.8338",
        "193.6172",
        "11612.6819",
        "130868.0151",
        "-222915.3155",
        "2075.6920"
      ],
      [
        "67",
        "1",
        "I",
        "cLCB8",
        "FX-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "68",
        "1",
        "I",
        "cLCB8",
        "FX-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "69",
        "1",
        "I",
        "cLCB8",
        "FY-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "70",
        "1",
        "I",
        "cLCB8",
        "FY-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "71",
        "1",
        "I",
        "cLCB8",
        "FZ-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "72",
        "1",
        "I",
        "cLCB8",
        "FZ-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "73",
        "1",
        "I",
        "cLCB8",
        "MX-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "74",
        "1",
        "I",
        "cLCB8",
        "MX-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "75",
        "1",
        "I",
        "cLCB8",
        "MY-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "76",
        "1",
        "I",
        "cLCB8",
        "MY-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "77",
        "1",
        "I",
        "cLCB8",
        "MZ-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "78",
        "1",
        "I",
        "cLCB8",
        "MZ-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "79",
        "1",
        "I",
        "cLCB9",
        "FX-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "80",
        "1",
        "I",
        "cLCB9",
        "FX-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "81",
        "1",
        "I",
        "cLCB9",
        "FY-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "82",
        "1",
        "I",
        "cLCB9",
        "FY-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "83",
        "1",
        "I",
        "cLCB9",
        "FZ-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "84",
        "1",
        "I",
        "cLCB9",
        "FZ-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "85",
        "1",
        "I",
        "cLCB9",
        "MX-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "86",
        "1",
        "I",
        "cLCB9",
        "MX-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "87",
        "1",
        "I",
        "cLCB9",
        "MY-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "88",
        "1",
        "I",
        "cLCB9",
        "MY-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "89",
        "1",
        "I",
        "cLCB9",
        "MZ-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "90",
        "1",
        "I",
        "cLCB9",
        "MZ-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "91",
        "1",
        "I",
        "cLCB10",
        "FX-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "92",
        "1",
        "I",
        "cLCB10",
        "FX-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "93",
        "1",
        "I",
        "cLCB10",
        "FY-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "94",
        "1",
        "I",
        "cLCB10",
        "FY-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "95",
        "1",
        "I",
        "cLCB10",
        "FZ-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "96",
        "1",
        "I",
        "cLCB10",
        "FZ-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "97",
        "1",
        "I",
        "cLCB10",
        "MX-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "98",
        "1",
        "I",
        "cLCB10",
        "MX-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "99",
        "1",
        "I",
        "cLCB10",
        "MY-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "100",
        "1",
        "I",
        "cLCB10",
        "MY-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "101",
        "1",
        "I",
        "cLCB10",
        "MZ-MAX",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "102",
        "1",
        "I",
        "cLCB10",
        "MZ-MIN",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "103",
        "1",
        "I",
        "cLCB11",
        "-",
        "-88309.1624",
        "-22.2864",
        "17729.1771",
        "130868.2201",
        "-244229.2003",
        "1693.2381"
      ],
      [
        "104",
        "1",
        "I",
        "cLCB12",
        "FX-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "105",
        "1",
        "I",
        "cLCB12",
        "FX-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "106",
        "1",
        "I",
        "cLCB12",
        "FY-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "107",
        "1",
        "I",
        "cLCB12",
        "FY-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "108",
        "1",
        "I",
        "cLCB12",
        "FZ-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "109",
        "1",
        "I",
        "cLCB12",
        "FZ-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "110",
        "1",
        "I",
        "cLCB12",
        "MX-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "111",
        "1",
        "I",
        "cLCB12",
        "MX-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "112",
        "1",
        "I",
        "cLCB12",
        "MY-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "113",
        "1",
        "I",
        "cLCB12",
        "MY-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "114",
        "1",
        "I",
        "cLCB12",
        "MZ-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "115",
        "1",
        "I",
        "cLCB12",
        "MZ-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "116",
        "1",
        "I",
        "cLCB13",
        "FX-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "117",
        "1",
        "I",
        "cLCB13",
        "FX-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "118",
        "1",
        "I",
        "cLCB13",
        "FY-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "119",
        "1",
        "I",
        "cLCB13",
        "FY-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "120",
        "1",
        "I",
        "cLCB13",
        "FZ-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "121",
        "1",
        "I",
        "cLCB13",
        "FZ-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "122",
        "1",
        "I",
        "cLCB13",
        "MX-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "123",
        "1",
        "I",
        "cLCB13",
        "MX-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "124",
        "1",
        "I",
        "cLCB13",
        "MY-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "125",
        "1",
        "I",
        "cLCB13",
        "MY-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "126",
        "1",
        "I",
        "cLCB13",
        "MZ-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "127",
        "1",
        "I",
        "cLCB13",
        "MZ-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "128",
        "1",
        "J",
        "t1",
        "-",
        "-522.3250",
        "160.5134",
        "5899.0110",
        "127261.6960",
        "-214786.0960",
        "145.8097"
      ],
      [
        "129",
        "1",
        "J",
        "t2",
        "-",
        "-43374.5280",
        "-24.0405",
        "4531.7890",
        "-660.3849",
        "-49394.5000",
        "896.5821"
      ],
      [
        "130",
        "1",
        "J",
        "t3",
        "-",
        "-1.5914",
        "0.4888",
        "17.0109",
        "386.9365",
        "-653.7204",
        "0.4450"
      ],
      [
        "131",
        "1",
        "J",
        "t4",
        "-",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "132",
        "1",
        "J",
        "cLCB1",
        "FX-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "133",
        "1",
        "J",
        "cLCB1",
        "FX-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "134",
        "1",
        "J",
        "cLCB1",
        "FY-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "135",
        "1",
        "J",
        "cLCB1",
        "FY-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "136",
        "1",
        "J",
        "cLCB1",
        "FZ-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "137",
        "1",
        "J",
        "cLCB1",
        "FZ-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "138",
        "1",
        "J",
        "cLCB1",
        "MX-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "139",
        "1",
        "J",
        "cLCB1",
        "MX-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "140",
        "1",
        "J",
        "cLCB1",
        "MY-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "141",
        "1",
        "J",
        "cLCB1",
        "MY-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "142",
        "1",
        "J",
        "cLCB1",
        "MZ-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "143",
        "1",
        "J",
        "cLCB1",
        "MZ-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "144",
        "1",
        "J",
        "cLCB2",
        "FX-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "145",
        "1",
        "J",
        "cLCB2",
        "FX-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "146",
        "1",
        "J",
        "cLCB2",
        "FY-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "147",
        "1",
        "J",
        "cLCB2",
        "FY-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "148",
        "1",
        "J",
        "cLCB2",
        "FZ-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "149",
        "1",
        "J",
        "cLCB2",
        "FZ-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "150",
        "1",
        "J",
        "cLCB2",
        "MX-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "151",
        "1",
        "J",
        "cLCB2",
        "MX-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "152",
        "1",
        "J",
        "cLCB2",
        "MY-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "153",
        "1",
        "J",
        "cLCB2",
        "MY-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "154",
        "1",
        "J",
        "cLCB2",
        "MZ-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "155",
        "1",
        "J",
        "cLCB2",
        "MZ-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "156",
        "1",
        "J",
        "cLCB3",
        "-",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "157",
        "1",
        "J",
        "cLCB4",
        "-",
        "-44494.6676",
        "168.4733",
        "13792.7091",
        "196476.0250",
        "-382789.3987",
        "1580.1629"
      ],
      [
        "158",
        "1",
        "J",
        "cLCB5",
        "FX-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "159",
        "1",
        "J",
        "cLCB5",
        "FX-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "160",
        "1",
        "J",
        "cLCB5",
        "FY-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "161",
        "1",
        "J",
        "cLCB5",
        "FY-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "162",
        "1",
        "J",
        "cLCB5",
        "FZ-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "163",
        "1",
        "J",
        "cLCB5",
        "FZ-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "164",
        "1",
        "J",
        "cLCB5",
        "MX-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "165",
        "1",
        "J",
        "cLCB5",
        "MX-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "166",
        "1",
        "J",
        "cLCB5",
        "MY-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "167",
        "1",
        "J",
        "cLCB5",
        "MY-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "168",
        "1",
        "J",
        "cLCB5",
        "MZ-MAX",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "169",
        "1",
        "J",
        "cLCB5",
        "MZ-MIN",
        "-44359.9109",
        "127.0693",
        "12267.4837",
        "163651.0782",
        "-327377.0723",
        "1542.5296"
      ],
      [
        "170",
        "1",
        "J",
        "cLCB6",
        "FX-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "171",
        "1",
        "J",
        "cLCB6",
        "FX-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "172",
        "1",
        "J",
        "cLCB6",
        "FY-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "173",
        "1",
        "J",
        "cLCB6",
        "FY-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "174",
        "1",
        "J",
        "cLCB6",
        "FZ-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "175",
        "1",
        "J",
        "cLCB6",
        "FZ-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "176",
        "1",
        "J",
        "cLCB6",
        "MX-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "177",
        "1",
        "J",
        "cLCB6",
        "MX-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "178",
        "1",
        "J",
        "cLCB6",
        "MY-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "179",
        "1",
        "J",
        "cLCB6",
        "MY-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "180",
        "1",
        "J",
        "cLCB6",
        "MZ-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "181",
        "1",
        "J",
        "cLCB6",
        "MZ-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "182",
        "1",
        "J",
        "cLCB7",
        "FX-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "183",
        "1",
        "J",
        "cLCB7",
        "FX-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "184",
        "1",
        "J",
        "cLCB7",
        "FY-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "185",
        "1",
        "J",
        "cLCB7",
        "FY-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "186",
        "1",
        "J",
        "cLCB7",
        "FZ-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "187",
        "1",
        "J",
        "cLCB7",
        "FZ-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "188",
        "1",
        "J",
        "cLCB7",
        "MX-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "189",
        "1",
        "J",
        "cLCB7",
        "MX-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "190",
        "1",
        "J",
        "cLCB7",
        "MY-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "191",
        "1",
        "J",
        "cLCB7",
        "MY-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "192",
        "1",
        "J",
        "cLCB7",
        "MZ-MAX",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "193",
        "1",
        "J",
        "cLCB7",
        "MZ-MIN",
        "-44268.5178",
        "193.6172",
        "10742.2567",
        "130826.1480",
        "-271964.7436",
        "1219.7562"
      ],
      [
        "194",
        "1",
        "J",
        "cLCB8",
        "FX-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "195",
        "1",
        "J",
        "cLCB8",
        "FX-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "196",
        "1",
        "J",
        "cLCB8",
        "FY-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "197",
        "1",
        "J",
        "cLCB8",
        "FY-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "198",
        "1",
        "J",
        "cLCB8",
        "FZ-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "199",
        "1",
        "J",
        "cLCB8",
        "FZ-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "200",
        "1",
        "J",
        "cLCB8",
        "MX-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "201",
        "1",
        "J",
        "cLCB8",
        "MX-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "202",
        "1",
        "J",
        "cLCB8",
        "MY-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "203",
        "1",
        "J",
        "cLCB8",
        "MY-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "204",
        "1",
        "J",
        "cLCB8",
        "MZ-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "205",
        "1",
        "J",
        "cLCB8",
        "MZ-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "206",
        "1",
        "J",
        "cLCB9",
        "FX-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "207",
        "1",
        "J",
        "cLCB9",
        "FX-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "208",
        "1",
        "J",
        "cLCB9",
        "FY-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "209",
        "1",
        "J",
        "cLCB9",
        "FY-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "210",
        "1",
        "J",
        "cLCB9",
        "FZ-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "211",
        "1",
        "J",
        "cLCB9",
        "FZ-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "212",
        "1",
        "J",
        "cLCB9",
        "MX-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "213",
        "1",
        "J",
        "cLCB9",
        "MX-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "214",
        "1",
        "J",
        "cLCB9",
        "MY-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "215",
        "1",
        "J",
        "cLCB9",
        "MY-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "216",
        "1",
        "J",
        "cLCB9",
        "MZ-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "217",
        "1",
        "J",
        "cLCB9",
        "MZ-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "218",
        "1",
        "J",
        "cLCB10",
        "FX-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "219",
        "1",
        "J",
        "cLCB10",
        "FX-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "220",
        "1",
        "J",
        "cLCB10",
        "FY-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "221",
        "1",
        "J",
        "cLCB10",
        "FY-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "222",
        "1",
        "J",
        "cLCB10",
        "FZ-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "223",
        "1",
        "J",
        "cLCB10",
        "FZ-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "224",
        "1",
        "J",
        "cLCB10",
        "MX-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "225",
        "1",
        "J",
        "cLCB10",
        "MX-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "226",
        "1",
        "J",
        "cLCB10",
        "MY-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "227",
        "1",
        "J",
        "cLCB10",
        "MY-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "228",
        "1",
        "J",
        "cLCB10",
        "MZ-MAX",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "229",
        "1",
        "J",
        "cLCB10",
        "MZ-MIN",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "230",
        "1",
        "J",
        "cLCB11",
        "-",
        "-85347.9024",
        "-22.2864",
        "15360.8859",
        "130826.2947",
        "-316661.1524",
        "1791.6390"
      ],
      [
        "231",
        "1",
        "J",
        "cLCB12",
        "FX-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "232",
        "1",
        "J",
        "cLCB12",
        "FX-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "233",
        "1",
        "J",
        "cLCB12",
        "FY-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "234",
        "1",
        "J",
        "cLCB12",
        "FY-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "235",
        "1",
        "J",
        "cLCB12",
        "FZ-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "236",
        "1",
        "J",
        "cLCB12",
        "FZ-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "237",
        "1",
        "J",
        "cLCB12",
        "MX-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "238",
        "1",
        "J",
        "cLCB12",
        "MX-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "239",
        "1",
        "J",
        "cLCB12",
        "MY-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "240",
        "1",
        "J",
        "cLCB12",
        "MY-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "241",
        "1",
        "J",
        "cLCB12",
        "MZ-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "242",
        "1",
        "J",
        "cLCB12",
        "MZ-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "243",
        "1",
        "J",
        "cLCB13",
        "FX-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "244",
        "1",
        "J",
        "cLCB13",
        "FX-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "245",
        "1",
        "J",
        "cLCB13",
        "FY-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "246",
        "1",
        "J",
        "cLCB13",
        "FY-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "247",
        "1",
        "J",
        "cLCB13",
        "FZ-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "248",
        "1",
        "J",
        "cLCB13",
        "FZ-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "249",
        "1",
        "J",
        "cLCB13",
        "MX-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "250",
        "1",
        "J",
        "cLCB13",
        "MX-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "251",
        "1",
        "J",
        "cLCB13",
        "MY-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "252",
        "1",
        "J",
        "cLCB13",
        "MY-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "253",
        "1",
        "J",
        "cLCB13",
        "MZ-MAX",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "254",
        "1",
        "J",
        "cLCB13",
        "MZ-MIN",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ]
    ]
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_DGN_FORCE",
    "COMPONENTS": [
      "Elem",
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
      "PartI",
      "PartJ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
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

## 13. `TABLE` · `PSC_STRESS_CS` — Check stress for cross section at a construction stage

> **기능** 시공단계별 단면의 응력 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST` · `GET` · `DELETE` · `PUT`

### Specifications

**원문** [영문 58334071429401](https://support.midasuser.com/hc/en-us/articles/58334071429401)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · Check Stress for Cross Section at a Construction Stage: "PSC_STRESS_CS" · Check Stress for Cross Section at a Construction Stage (Virtual Beam): "PSC_STRESS_CS_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 8 | [General] Element Parts | `"PARTS"` | array | ["All"] | Optional |
| 9 | [General] Compression/Tension | `"COMP_TENS"` | array | ["All"] | Optional |
| 10 | [General] Girder/Slab · Girder: "girder" · Slab: "slab" | `"GIRDER_SLAB"` | string | girder | Optional |

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
          "description": "PSC Stress Result Table Type",
          "enum": [
            "PSC_STRESS_CS",
            "PSC_STRESS_CS_VBEAM"
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
              "Elem",
              "Part",
              "Girder/Slab",
              "Comp./Tens.",
              "Stage",
              "CHK",
              "FT",
              "FB",
              "FTL",
              "FBL",
              "FTR",
              "FBR",
              "FMAX",
              "ALW"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Element No. Input",
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
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress",
          "items": {
            "type": "string",
            "enum": [
              "Compression",
              "Tension"
            ]
          },
          "default": [
            "All"
          ]
        },
        "GIRDER_SLAB": {
          "type": "string",
          "description": "Girder or Slab Selection",
          "default": "girder",
          "enum": [
            "girder",
            "slab"
          ]
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `TEST` — `Index`, `Elem`, `Part`, `Girder/Slab`, `Comp./Tens.`, `Stage`, `FT`, `FB`, `FTL`, `FBL`, `FTR`, `FBR`, `FMAX`, `ALW`

### Request / Response JSON

**Request — PSC_STRESS_CS**

```json
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_STRESS_CS",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Girder/Slab",
      "Comp./Tens.",
      "Stage",
      "FT",
      "FB",
      "FTL",
      "FBL",
      "FTR",
      "FBR",
      "FMAX",
      "ALW"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Tension",
      "Compression"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
```

**Request — PSC_STRESS_CS_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_STRESS_CS_VBEAM",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Girder/Slab",
      "Comp./Tens.",
      "Stage",
      "FT",
      "FB",
      "FTL",
      "FBL",
      "FTR",
      "FBR",
      "FMAX",
      "ALW"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Tension",
      "Compression"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        201
      ]
    }
  }
}
```

**Response — PSC_STRESS_CS**

```json
{
  "TEST": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Girder/Slab",
      "Comp./Tens.",
      "Stage",
      "FT",
      "FB",
      "FTL",
      "FBL",
      "FTR",
      "FBR",
      "FMAX",
      "ALW"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[3]",
        "Girder(PSC)",
        "Compression",
        "CS1",
        "3751.3677",
        "12246.9260",
        "3751.1188",
        "12246.7940",
        "3751.6170",
        "12247.0580",
        "12247.0580",
        "26000.0000"
      ],
      [
        "2",
        "1",
        "I[3]",
        "Girder(PSC)",
        "Tension",
        "CS1",
        "3751.3677",
        "12246.9260",
        "3751.1188",
        "12246.7940",
        "3751.6170",
        "12247.0580",
        "3751.1188",
        "-3985.6650"
      ],
      [
        "3",
        "2",
        "I[5]",
        "Girder(PSC)",
        "Compression",
        "CS1",
        "-249.7975",
        "17570.0600",
        "-250.0384",
        "17569.9320",
        "-249.5570",
        "17570.1880",
        "17570.1880",
        "26000.0000"
      ],
      [
        "4",
        "2",
        "I[5]",
        "Girder(PSC)",
        "Tension",
        "CS2",
        "-322.5890",
        "17131.6785",
        "-373.7556",
        "17104.5900",
        "-271.4219",
        "17158.7680",
        "-373.7556",
        "-1378.9519"
      ],
      [
        "5",
        "3",
        "I[4]",
        "Girder(PSC)",
        "Compression",
        "CS1",
        "-2662.2040",
        "20678.9410",
        "-2662.4385",
        "20678.8180",
        "-2661.9700",
        "20679.0660",
        "20679.0660",
        "26000.0000"
      ],
      [
        "6",
        "3",
        "I[4]",
        "Girder(PSC)",
        "Tension",
        "CS2",
        "-2684.2205",
        "20212.5085",
        "-2729.2760",
        "20188.6560",
        "-2639.1658",
        "20236.3600",
        "-2729.2760",
        "-1378.9519"
      ]
    ]
  }
}
```

**Response — PSC_STRESS_CS_VBEAM**

```json
{
  "TEST": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Girder/Slab",
      "Comp./Tens.",
      "Stage",
      "FT",
      "FB",
      "FTL",
      "FBL",
      "FTR",
      "FBR",
      "FMAX",
      "ALW"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "Girder(Composite)",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "2",
        "201",
        "I",
        "Girder(Composite)",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
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
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_STRESS_CS",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Girder/Slab",
      "Comp./Tens.",
      "Stage",
      "FT",
      "FB",
      "FTL",
      "FBL",
      "FTR",
      "FBR",
      "FMAX",
      "ALW"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Tension",
      "Compression"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 14. `TABLE` · `PSC_STRESS_TENDON` — Check tensile stress for Prestressing tendons

> **기능** 프리스트레싱 긴장재의 인장응력 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58337271509017](https://support.midasuser.com/hc/en-us/articles/58337271509017)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · Check Tensile Stress for Prestressing Tendons: "PSC_STRESS_TENDON" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Tendon Selection | `"TENDON"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |

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
          "description": "Check Tensile Stress for Prestressing Tendons - Result Table Type",
          "enum": [
            "PSC_STRESS_TENDON"
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
              "Tendon",
              "FDL1",
              "FDL2",
              "FLL1",
              "AFDL1",
              "AFDL2",
              "AFLL1"
            ]
          }
        },
        "TENDON": {
          "type": "object",
          "description": "Tendon Number",
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
            }
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `test` — `Index`, `FDL1`, `FDL2`, `FLL1`, `AFDL1`, `AFDL2`, `AFLL1`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_TENDON",
    "TABLE_NAME": "test",
    "COMPONENTS": [
      "FDL1",
      "FDL2",
      "FLL1",
      "AFDL1",
      "AFDL2",
      "AFLL1"
    ],
    "TENDON": {
      "KEYS": [
        1
      ]
    }
  }
}
```

**Response**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "FDL1",
      "FDL2",
      "FLL1",
      "AFDL1",
      "AFDL2",
      "AFLL1"
    ],
    "DATA": [
      [
        "1",
        "1135758.6930",
        "1262391.6367",
        "1224976.1691",
        "1302000.0000",
        "1376400.0000",
        "1264000.0000"
      ]
    ]
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_TENDON",
    "TABLE_NAME": "test",
    "COMPONENTS": [
      "FDL1",
      "FDL2",
      "FLL1",
      "AFDL1",
      "AFDL2",
      "AFLL1"
    ],
    "TENDON": {
      "KEYS": [
        1
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

## 15. `TABLE` · `PSC_STRESS_SERVICE` — Check stress for cross section at service loads

> **기능** 사용하중에 대한 단면 응력 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58334269624601](https://support.midasuser.com/hc/en-us/articles/58334269624601)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · Check Stress for Cross Section at a service loads: "PSC_STRESS_SERVICE" · Check Stress for Cross Section at a service loads (Virtual Beam): "PSC_STRESS_SERVICE_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 8 | [General] Element Parts | `"PARTS"` | array | ["All"] | Optional |
| 9 | [General] Compression/Tension | `"COMP_TENS"` | array | ["All"] | Optional |
| 10 | [General] Girder/Slab · Girder: "girder" · Slab: "slab" | `"GIRDER_SLAB"` | string | girder | Optional |

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
          "description": "Check Stress for Cross Section at a service loads - Result Table Type",
          "enum": [
            "PSC_STRESS_SERVICE",
            "PSC_STRESS_SERVICE_VBEAM"
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
              "Elem",
              "Part",
              "Girder/Slab",
              "Comp./Tens.",
              "LComName",
              "Type",
              "CHK",
              "FT",
              "FB",
              "FTL",
              "FBL",
              "FTR",
              "FBR",
              "FMAX",
              "ALW"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Element No. Input",
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
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress",
          "items": {
            "type": "string",
            "enum": [
              "Compression",
              "Tension"
            ]
          },
          "default": [
            "All"
          ]
        },
        "GIRDER_SLAB": {
          "type": "string",
          "description": "Girder or Slab Selection",
          "default": "girder",
          "enum": [
            "girder",
            "slab"
          ]
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `test` — `Index`, `Elem`, `Part`, `Girder/Slab`, `Comp./Tens.`, `LComName`, `Type`, `CHK`, `FT`, `FB`, `FTL`, `FBL`, `FTR`, `FBR`, `FMAX`, `ALW`

### Request / Response JSON

**Request — PSC_STRESS_SERVICE**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_STRESS_SERVICE",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Girder/Slab",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "FT",
      "FB",
      "FTL",
      "FBL",
      "FTR",
      "FBR",
      "FMAX",
      "ALW"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Compression",
      "Tension"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
```

**Request — PSC_STRESS_SERVICE_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_STRESS_SERVICE_VBEAM",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Girder/Slab",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "FT",
      "FB",
      "FTL",
      "FBL",
      "FTR",
      "FBR",
      "FMAX",
      "ALW"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Compression",
      "Tension"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        201
      ]
    }
  }
}
```

**Response — PSC_STRESS_SERVICE**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Girder/Slab",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "FT",
      "FB",
      "FTL",
      "FBL",
      "FTR",
      "FBR",
      "FMAX",
      "ALW"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[1]",
        "Girder(PSC)",
        "Compression",
        "cLCB3",
        "-",
        "OK",
        "238.4914",
        "634.0510",
        "238.4915",
        "634.0511",
        "238.4915",
        "634.0511",
        "634.0511",
        "18000.0000"
      ],
      [
        "2",
        "1",
        "I[1]",
        "Girder(PSC)",
        "Tension",
        "cLCB4",
        "-",
        "OK",
        "238.4914",
        "634.0510",
        "238.4915",
        "634.0511",
        "238.4915",
        "634.0511",
        "238.4914",
        "-1574.3377"
      ],
      [
        "3",
        "2",
        "I[2]",
        "Girder(PSC)",
        "Compression",
        "cLCB3",
        "-",
        "OK",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "18000.0000"
      ],
      [
        "4",
        "2",
        "I[2]",
        "Girder(PSC)",
        "Tension",
        "cLCB4",
        "-",
        "NG",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "-2332.7193",
        "-2332.7193",
        "-1574.3377"
      ],
      [
        "5",
        "3",
        "I[3]",
        "Girder(PSC)",
        "Compression",
        "cLCB3",
        "-",
        "OK",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "18000.0000"
      ],
      [
        "6",
        "3",
        "I[3]",
        "Girder(PSC)",
        "Tension",
        "cLCB4",
        "-",
        "NG",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "-4020.8716",
        "-4020.8716",
        "-1574.3377"
      ]
    ]
  }
}
```

**Response — PSC_STRESS_SERVICE_VBEAM**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Girder/Slab",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "FT",
      "FB",
      "FTL",
      "FBL",
      "FTR",
      "FBR",
      "FMAX",
      "ALW"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "Girder(Composite)",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "-0.0000",
        "-0.0000",
        "718.8343",
        "-593.0222",
        "729.3292",
        "-593.0222",
        "729.3292",
        "18000.0000"
      ],
      [
        "2",
        "201",
        "I",
        "Girder(Composite)",
        "Tension",
        "cLCB3",
        "-",
        "OK",
        "-0.0000",
        "-0.0000",
        "718.8343",
        "-593.0222",
        "729.3292",
        "-593.0222",
        "-593.0222",
        "-1574.3377"
      ]
    ]
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_STRESS_SERVICE",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Girder/Slab",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "FT",
      "FB",
      "FTL",
      "FBL",
      "FTR",
      "FBR",
      "FMAX",
      "ALW"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Compression",
      "Tension"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 16. `TABLE` · `PSC_PRINCIPAL_CS` — Principal stress at a construction stage

> **기능** 시공단계별 단면의 주응력 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58332500765849](https://support.midasuser.com/hc/en-us/articles/58332500765849)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · Principal stress at a construction stage: "PSC_PRINCIPAL_CS" · Principal stress at a construction stage (Virtual Beam): "PSC_PRINCIPAL_CS_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 8 | [General] Element Parts | `"PARTS"` | array | ["All"] | Optional |
| 9 | [General] Compression/Tension | `"COMP_TENS"` | array | ["All"] | Optional |

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
          "description": "Principal stress at a construction stage",
          "enum": [
            "PSC_PRINCIPAL_CS",
            "PSC_PRINCIPAL_CS_VBEAM"
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
              "Elem",
              "Part",
              "Comp./Tens.",
              "Stage",
              "CHK",
              "Sig_P1",
              "Sig_P2",
              "Sig_P3",
              "Sig_P4",
              "Sig_P5",
              "Sig_P6",
              "Sig_P7",
              "Sig_P8",
              "Sig_P9",
              "Sig_P10",
              "Sig_MAX",
              "Sig_AP"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Element No. Input",
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
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress",
          "items": {
            "type": "string",
            "enum": [
              "Tension"
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

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `test` — `Index`, `Elem`, `Part`, `Comp./Tens.`, `Stage`, `CHK`, `Sig_P1`, `Sig_P2`, `Sig_P3`, `Sig_P4`, `Sig_P5`, `Sig_P6`, `Sig_P7`, `Sig_P8`, `Sig_P9`, `Sig_P10`, `Sig_MAX`, `Sig_AP`

### Request / Response JSON

**Request — PSC_PRINCIPAL_CS**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_PRINCIPAL_CS",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Comp./Tens.",
      "Stage",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "PARTS": [
      "PartJ"
    ],
    "COMP_TENS": [
      "Tension"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
```

**Request — PSC_PRINCIPAL_CS_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_PRINCIPAL_CS_VBEAM",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Comp./Tens.",
      "Stage",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "PARTS": [
      "PartJ"
    ],
    "COMP_TENS": [
      "Tension"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        201
      ]
    }
  }
}
```

**Response — PSC_PRINCIPAL_CS**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Comp./Tens.",
      "Stage",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[3]",
        "Tension",
        "CS1",
        "OK",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-801.6216",
        "-801.6145",
        "-1219.4860",
        "-1219.4793",
        "-530.5488",
        "-530.5564",
        "-1219.4860",
        "-1826.7631"
      ],
      [
        "2",
        "1",
        "I[3]",
        "Tension",
        "CS1",
        "OK",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-801.6216",
        "-801.6145",
        "-1219.4860",
        "-1219.4793",
        "-530.5488",
        "-530.5564",
        "-1219.4860",
        "-1826.7631"
      ],
      [
        "3",
        "1",
        "J[5]",
        "Tension",
        "CS2",
        "OK",
        "-349.3734",
        "-299.4497",
        "-0.0191",
        "-0.0191",
        "-769.0312",
        "-791.1918",
        "-743.7100",
        "-761.7593",
        "-223.1049",
        "-231.5367",
        "-791.1918",
        "-1826.7631"
      ],
      [
        "4",
        "1",
        "J[5]",
        "Tension",
        "CS2",
        "OK",
        "-349.3734",
        "-299.4497",
        "-0.0191",
        "-0.0191",
        "-769.0312",
        "-791.1918",
        "-743.7100",
        "-761.7593",
        "-223.1049",
        "-231.5367",
        "-791.1918",
        "-1826.7631"
      ],
      [
        "5",
        "2",
        "I[5]",
        "Tension",
        "CS2",
        "OK",
        "-374.5124",
        "-272.4621",
        "-0.0165",
        "-0.0166",
        "-769.1347",
        "-783.0025",
        "-741.4659",
        "-755.1232",
        "-222.1546",
        "-229.5137",
        "-783.0025",
        "-1826.7631"
      ],
      [
        "6",
        "2",
        "I[5]",
        "Tension",
        "CS2",
        "OK",
        "-374.5124",
        "-272.4621",
        "-0.0165",
        "-0.0166",
        "-769.1347",
        "-783.0025",
        "-741.4659",
        "-755.1232",
        "-222.1546",
        "-229.5137",
        "-783.0025",
        "-1826.7631"
      ],
      [
        "7",
        "2",
        "J[4]",
        "Tension",
        "CS2",
        "NG",
        "-2715.5849",
        "-2655.3847",
        "-0.0140",
        "-0.0140",
        "-1091.4839",
        "-1110.2810",
        "-714.9782",
        "-730.9582",
        "-181.3549",
        "-187.9516",
        "-2715.5849",
        "-1826.7631"
      ],
      [
        "8",
        "2",
        "J[4]",
        "Tension",
        "CS2",
        "NG",
        "-2715.5849",
        "-2655.3847",
        "-0.0140",
        "-0.0140",
        "-1091.4839",
        "-1110.2810",
        "-714.9782",
        "-730.9582",
        "-181.3549",
        "-187.9516",
        "-2715.5849",
        "-1826.7631"
      ],
      [
        "9",
        "3",
        "I[4]",
        "Tension",
        "CS2",
        "NG",
        "-2729.3504",
        "-2639.2427",
        "-0.0100",
        "-0.0101",
        "-1090.6490",
        "-1098.2308",
        "-712.0669",
        "-723.4036",
        "-180.5708",
        "-185.9027",
        "-2729.3504",
        "-1826.7631"
      ],
      [
        "10",
        "3",
        "I[4]",
        "Tension",
        "CS2",
        "NG",
        "-2729.3504",
        "-2639.2427",
        "-0.0100",
        "-0.0101",
        "-1090.6490",
        "-1098.2308",
        "-712.0669",
        "-723.4036",
        "-180.5708",
        "-185.9027",
        "-2729.3504",
        "-1826.7631"
      ],
      [
        "11",
        "3",
        "J[7]",
        "Tension",
        "CS2",
        "NG",
        "-4930.6572",
        "-4869.3977",
        "-0.0088",
        "-0.0088",
        "-1367.4143",
        "-1374.0560",
        "-477.8365",
        "-489.5011",
        "-102.1837",
        "-106.2005",
        "-4930.6572",
        "-1826.7631"
      ],
      [
        "12",
        "3",
        "J[7]",
        "Tension",
        "CS2",
        "NG",
        "-4930.6572",
        "-4869.3977",
        "-0.0088",
        "-0.0088",
        "-1367.4143",
        "-1374.0560",
        "-477.8365",
        "-489.5011",
        "-102.1837",
        "-106.2005",
        "-4930.6572",
        "-1826.7631"
      ]
    ]
  }
}
```

**Response — PSC_PRINCIPAL_CS_VBEAM**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Comp./Tens.",
      "Stage",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "DATA": [
      [
        "1",
        "201",
        "J",
        "Tension",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
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
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_PRINCIPAL_CS",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Comp./Tens.",
      "Stage",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "PARTS": [
      "PartJ"
    ],
    "COMP_TENS": [
      "Tension"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```

### 추가 원문 — PSC_PRINCIPAL_CS

**원문** [영문 58336859751193](https://support.midasuser.com/hc/en-us/articles/58336859751193)

**원문 Active Methods** `POST`

> ⚠️ 목차에 연결된 글은 일반 부재와 가상보 예제를 함께 제공합니다. 이 글의 Schema에는 `Argument.NODE_ELEMS.STRUCTURE_GROUP_NAME`이 있어 아래에 별도로 싣습니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Map of keyed objects where each key is a string identifier. | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name Output table title in response | `"TABLE_NAME"` | string | "" | Optional |
| 2 | [General] Table Type · Principal stress at a construction stage: "PSC_PRINCIPAL_CS" · Principal stress at a construction stage (Virtual Beam): "PSC_PRINCIPAL_CS_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path Optional: Save results to file path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place Constraints: · Value Range: >= 0, <= 15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components · Elem: "Elem" · Part: "Part" · Comp./Tens.: "Comp./Tens." · Stage: "Stage" · CHK: "CHK" · Sig_P1: "Sig_P1" · Sig_P2: "Sig_P2" · Sig_P3: "Sig_P3" · Sig_P4: "Sig_P4" · Sig_P5: "Sig_P5" · Sig_P6: "Sig_P6" · Sig_P7: "Sig_P7" · Sig_P8: "Sig_P8" · Sig_P9: "Sig_P9" · Sig_P10: "Sig_P10" · Sig_MAX: "Sig_MAX" · Sig_AP: "Sig_AP" | `"COMPONENTS"` | Array [string] | - | Optional |
| 7 | [General] Node/Element Selection Use only ONE of the three methods: KEYS, TO, or STRUCTURE_GROUP_NAME | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | Array [integer] | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 7.3 | └ [General] Specify Structure Group Name | `"STRUCTURE_GROUP_NAME"` | string | - | Optional |
| 8 | [General] Element Parts · PartI: "PartI" · PartJ: "PartJ" | `"PARTS"` | Array [string] | ["All"] | Optional |
| 9 | [General] Compression/Tension · Tension: "Tension" | `"COMP_TENS"` | Array [string] | ["All"] | Optional |

**JSON Schema**

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
          "description": "Principal stress at a construction stage",
          "enum": [
            "PSC_PRINCIPAL_CS",
            "PSC_PRINCIPAL_CS_VBEAM"
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
              "Elem",
              "Part",
              "Comp./Tens.",
              "Stage",
              "CHK",
              "Sig_P1",
              "Sig_P2",
              "Sig_P3",
              "Sig_P4",
              "Sig_P5",
              "Sig_P6",
              "Sig_P7",
              "Sig_P8",
              "Sig_P9",
              "Sig_P10",
              "Sig_MAX",
              "Sig_AP"
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
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress",
          "items": {
            "type": "string",
            "enum": [
              "Tension"
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

**Request / Response JSON**

**Request**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_PRINCIPAL_CS",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Comp./Tens.",
      "Stage",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "PARTS": [
      "PartJ"
    ],
    "COMP_TENS": [
      "Tension"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
```

**Response**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Comp./Tens.",
      "Stage",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[3]",
        "Tension",
        "CS1",
        "OK",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-801.6216",
        "-801.6145",
        "-1219.4860",
        "-1219.4793",
        "-530.5488",
        "-530.5564",
        "-1219.4860",
        "-1826.7631"
      ],
      [
        "2",
        "1",
        "I[3]",
        "Tension",
        "CS1",
        "OK",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-801.6216",
        "-801.6145",
        "-1219.4860",
        "-1219.4793",
        "-530.5488",
        "-530.5564",
        "-1219.4860",
        "-1826.7631"
      ],
      [
        "3",
        "1",
        "J[5]",
        "Tension",
        "CS2",
        "OK",
        "-349.3734",
        "-299.4497",
        "-0.0191",
        "-0.0191",
        "-769.0312",
        "-791.1918",
        "-743.7100",
        "-761.7593",
        "-223.1049",
        "-231.5367",
        "-791.1918",
        "-1826.7631"
      ],
      [
        "4",
        "1",
        "J[5]",
        "Tension",
        "CS2",
        "OK",
        "-349.3734",
        "-299.4497",
        "-0.0191",
        "-0.0191",
        "-769.0312",
        "-791.1918",
        "-743.7100",
        "-761.7593",
        "-223.1049",
        "-231.5367",
        "-791.1918",
        "-1826.7631"
      ],
      [
        "5",
        "2",
        "I[5]",
        "Tension",
        "CS2",
        "OK",
        "-374.5124",
        "-272.4621",
        "-0.0165",
        "-0.0166",
        "-769.1347",
        "-783.0025",
        "-741.4659",
        "-755.1232",
        "-222.1546",
        "-229.5137",
        "-783.0025",
        "-1826.7631"
      ],
      [
        "6",
        "2",
        "I[5]",
        "Tension",
        "CS2",
        "OK",
        "-374.5124",
        "-272.4621",
        "-0.0165",
        "-0.0166",
        "-769.1347",
        "-783.0025",
        "-741.4659",
        "-755.1232",
        "-222.1546",
        "-229.5137",
        "-783.0025",
        "-1826.7631"
      ],
      [
        "7",
        "2",
        "J[4]",
        "Tension",
        "CS2",
        "NG",
        "-2715.5849",
        "-2655.3847",
        "-0.0140",
        "-0.0140",
        "-1091.4839",
        "-1110.2810",
        "-714.9782",
        "-730.9582",
        "-181.3549",
        "-187.9516",
        "-2715.5849",
        "-1826.7631"
      ],
      [
        "8",
        "2",
        "J[4]",
        "Tension",
        "CS2",
        "NG",
        "-2715.5849",
        "-2655.3847",
        "-0.0140",
        "-0.0140",
        "-1091.4839",
        "-1110.2810",
        "-714.9782",
        "-730.9582",
        "-181.3549",
        "-187.9516",
        "-2715.5849",
        "-1826.7631"
      ],
      [
        "9",
        "3",
        "I[4]",
        "Tension",
        "CS2",
        "NG",
        "-2729.3504",
        "-2639.2427",
        "-0.0100",
        "-0.0101",
        "-1090.6490",
        "-1098.2308",
        "-712.0669",
        "-723.4036",
        "-180.5708",
        "-185.9027",
        "-2729.3504",
        "-1826.7631"
      ],
      [
        "10",
        "3",
        "I[4]",
        "Tension",
        "CS2",
        "NG",
        "-2729.3504",
        "-2639.2427",
        "-0.0100",
        "-0.0101",
        "-1090.6490",
        "-1098.2308",
        "-712.0669",
        "-723.4036",
        "-180.5708",
        "-185.9027",
        "-2729.3504",
        "-1826.7631"
      ],
      [
        "11",
        "3",
        "J[7]",
        "Tension",
        "CS2",
        "NG",
        "-4930.6572",
        "-4869.3977",
        "-0.0088",
        "-0.0088",
        "-1367.4143",
        "-1374.0560",
        "-477.8365",
        "-489.5011",
        "-102.1837",
        "-106.2005",
        "-4930.6572",
        "-1826.7631"
      ],
      [
        "12",
        "3",
        "J[7]",
        "Tension",
        "CS2",
        "NG",
        "-4930.6572",
        "-4869.3977",
        "-0.0088",
        "-0.0088",
        "-1367.4143",
        "-1374.0560",
        "-477.8365",
        "-489.5011",
        "-102.1837",
        "-106.2005",
        "-4930.6572",
        "-1826.7631"
      ]
    ]
  }
}
```


---

## 17. `TABLE` · `PSC_PRINCIPAL_SVC_E` — Principal stress at service loads (excluding torsional shear stress)

> **기능** 비틀림 전단응력을 제외한 사용하중 주응력 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58336954415385](https://support.midasuser.com/hc/en-us/articles/58336954415385)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · Principal Stress at Service Loads (Excl. Torsional Shear Stress): "PSC_PRINCIPAL_SVC_E" · Principal Stress at Service Loads (Excl. Torsional Shear Stress) - Virtual Beam: "PSC_PRINCIPAL_SVC_E_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 8 | [General] Element Parts | `"PARTS"` | array | ["All"] | Optional |
| 9 | [General] Compression/Tension | `"COMP_TENS"` | array | ["All"] | Optional |

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
          "description": "Principal stress at service loads (excluding torsional shear stress) - Result Table Type",
          "enum": [
            "PSC_PRINCIPAL_SVC_E",
            "PSC_PRINCIPAL_SVC_E_VBEAM"
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
              "Elem",
              "Part",
              "Comp./Tens.",
              "LComName",
              "Type",
              "CHK",
              "Sig_P1",
              "Sig_P2",
              "Sig_P3",
              "Sig_P4",
              "Sig_P5",
              "Sig_P6",
              "Sig_P7",
              "Sig_P8",
              "Sig_P9",
              "Sig_P10",
              "Sig_MAX",
              "Sig_AP"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Element No. Input",
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
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress",
          "items": {
            "type": "string",
            "enum": [
              "Tension"
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

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `TEST` — `Index`, `Elem`, `Part`, `Comp./Tens.`, `LComName`, `Type`, `CHK`, `Sig_P1`, `Sig_P2`, `Sig_P3`, `Sig_P4`, `Sig_P5`, `Sig_P6`, `Sig_P7`, `Sig_P8`, `Sig_P9`, `Sig_P10`, `Sig_MAX`, `Sig_AP`

### Request / Response JSON

**Request — PSC_PRINCIPAL_SVC_E**

```json
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_PRINCIPAL_SVC_E",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Tension"
    ],
    "NODE_ELEMS": {
      "TO": "1to5"
    }
  }
}
```

**Request — PSC_PRINCIPAL_SVC_E_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_PRINCIPAL_SVC_E_VBEAM",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Tension"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        201
      ]
    }
  }
}
```

**Response — PSC_PRINCIPAL_SVC_E**

```json
{
  "TEST": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[3]",
        "Tension",
        "cLCB10",
        "FX-MAX",
        "NG",
        "-29065.1201",
        "-28656.8952",
        "-2217.2060",
        "-2224.9109",
        "-11665.3052",
        "-22919.2938",
        "-948.4351",
        "-15502.3918",
        "-597.0194",
        "-6122.8733",
        "-29065.1201",
        "-1826.7631"
      ],
      [
        "2",
        "2",
        "I[5]",
        "Tension",
        "cLCB10",
        "FX-MAX",
        "NG",
        "-61643.3381",
        "-60922.2571",
        "-1480.3160",
        "-1485.1134",
        "-33868.5470",
        "-33816.7932",
        "-7924.3781",
        "-8500.2931",
        "-1812.9995",
        "-1972.9199",
        "-61643.3381",
        "-1826.7631"
      ],
      [
        "3",
        "3",
        "I[4]",
        "Tension",
        "cLCB10",
        "FX-MAX",
        "NG",
        "-79455.3988",
        "-78698.3410",
        "-802.0009",
        "-804.1877",
        "-45129.5513",
        "-40819.2917",
        "-11476.0507",
        "-1643.2435",
        "-2068.0012",
        "-353.7743",
        "-79455.3988",
        "-1826.7631"
      ],
      [
        "4",
        "4",
        "I[7]",
        "Tension",
        "cLCB10",
        "FX-MAX",
        "NG",
        "-87253.0855",
        "-86562.4849",
        "-384.7878",
        "-385.6694",
        "-49837.3488",
        "-44900.6279",
        "-12897.7803",
        "-461.2578",
        "-2018.3794",
        "-0.2026",
        "-87253.0855",
        "-1826.7631"
      ],
      [
        "5",
        "5",
        "I[6]",
        "Tension",
        "cLCB10",
        "FX-MAX",
        "NG",
        "-87476.5519",
        "-86891.7426",
        "-178.3674",
        "-178.7127",
        "-49641.1435",
        "-45664.8870",
        "-12389.7215",
        "-2979.6527",
        "-1756.8995",
        "-136.3141",
        "-87476.5519",
        "-1826.7631"
      ]
    ]
  }
}
```

**Response — PSC_PRINCIPAL_SVC_E_VBEAM**

```json
{
  "TEST": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "Tension",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
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
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_PRINCIPAL_SVC_E",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Tension"
    ],
    "NODE_ELEMS": {
      "TO": "1to5"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 18. `TABLE` · `PSC_PRINCIPAL_SVC` — Principal stress at service loads

> **기능** 사용하중에 대한 주응력 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58337159836441](https://support.midasuser.com/hc/en-us/articles/58337159836441)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · Principal Stress at Service Loads: "PSC_PRINCIPAL_SVC" · Principal Stress at Service Loads (Virtual Beam): "PSC_PRINCIPAL_SVC_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 8 | [General] Element Parts | `"PARTS"` | array | ["All"] | Optional |
| 9 | [General] Compression/Tension | `"COMP_TENS"` | array | ["All"] | Optional |

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
          "description": "Principal stress at service loads - Result Table Type",
          "enum": [
            "PSC_PRINCIPAL_SVC",
            "PSC_PRINCIPAL_SVC_VBEAM"
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
              "Elem",
              "Part",
              "Comp./Tens.",
              "LComName",
              "Type",
              "CHK",
              "Sig_P1",
              "Sig_P2",
              "Sig_P3",
              "Sig_P4",
              "Sig_P5",
              "Sig_P6",
              "Sig_P7",
              "Sig_P8",
              "Sig_P9",
              "Sig_P10",
              "Sig_MAX",
              "Sig_AP"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Element No. Input",
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
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress",
          "items": {
            "type": "string",
            "enum": [
              "Tension"
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

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `TEST` — `Index`, `Elem`, `Part`, `Comp./Tens.`, `LComName`, `Type`, `CHK`, `Sig_P1`, `Sig_P2`, `Sig_P3`, `Sig_P4`, `Sig_P5`, `Sig_P6`, `Sig_P7`, `Sig_P8`, `Sig_P9`, `Sig_P10`, `Sig_MAX`, `Sig_AP`

### Request / Response JSON

**Request — PSC_PRINCIPAL_SVC**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_SVC",
    "TABLE_NAME": "TEST",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Tension"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
```

**Request — PSC_PRINCIPAL_SVC_VBEAM**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_SVC_VBEAM",
    "TABLE_NAME": "TEST",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Tension"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        201
      ]
    }
  }
}
```

**Response — PSC_PRINCIPAL_SVC**

```json
{
  "TEST": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[3]",
        "Tension",
        "cLCB10",
        "FX-MAX",
        "NG",
        "-29065.1201",
        "-28656.8952",
        "-2217.2060",
        "-2224.9109",
        "-11665.3052",
        "-22919.2938",
        "-948.4351",
        "-15502.3918",
        "-597.0194",
        "-6122.8733",
        "-29065.1201",
        "-1826.7631"
      ],
      [
        "2",
        "2",
        "I[5]",
        "Tension",
        "cLCB10",
        "FX-MAX",
        "NG",
        "-61643.3381",
        "-60922.2571",
        "-1480.3160",
        "-1485.1134",
        "-33868.5470",
        "-33816.7932",
        "-7924.3781",
        "-8500.2931",
        "-1812.9995",
        "-1972.9199",
        "-61643.3381",
        "-1826.7631"
      ],
      [
        "3",
        "3",
        "I[4]",
        "Tension",
        "cLCB10",
        "FX-MAX",
        "NG",
        "-79455.3988",
        "-78698.3410",
        "-802.0009",
        "-804.1877",
        "-45129.5513",
        "-40819.2917",
        "-11476.0507",
        "-1643.2435",
        "-2068.0012",
        "-353.7743",
        "-79455.3988",
        "-1826.7631"
      ]
    ]
  }
}
```

**Response — PSC_PRINCIPAL_SVC_VBEAM**

```json
{
  "TEST": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "Tension",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
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
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_SVC",
    "TABLE_NAME": "TEST",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Comp./Tens.",
      "LComName",
      "Type",
      "CHK",
      "Sig_P1",
      "Sig_P2",
      "Sig_P3",
      "Sig_P4",
      "Sig_P5",
      "Sig_P6",
      "Sig_P7",
      "Sig_P8",
      "Sig_P9",
      "Sig_P10",
      "Sig_MAX",
      "Sig_AP"
    ],
    "PARTS": [
      "PartI"
    ],
    "COMP_TENS": [
      "Tension"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 19. `TABLE` · `PSC_CRACK_WIDTH` — Check crack width at service loads

> **기능** 사용하중에 대한 균열폭 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58337212919321](https://support.midasuser.com/hc/en-us/articles/58337212919321)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · Check Crack Width at Service Loads: "PSC_CRACK_WIDTH" · Check Crack Width at Service Loads (Virtual Beam): "PSC_CRACK_WIDTH_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 8 | [General] Element Parts | `"PARTS"` | array | ["All"] | Optional |
| 9 | [General] Top/Bottom | `"TOP_BOT"` | array | ["All"] | Optional |

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
          "description": "Check Crack Width at Service Loads - Result Table Type",
          "enum": [
            "PSC_CRACK_WIDTH",
            "PSC_CRACK_WIDTH_VBEAM"
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
              "Elem",
              "Part",
              "Top/Bottom",
              "LComName",
              "Type",
              "CHK",
              "FT",
              "FB",
              "fss",
              "s_use",
              "s_max"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Element No. Input",
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
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        },
        "TOP_BOT": {
          "type": "array",
          "description": "Top or Bottom",
          "items": {
            "type": "string",
            "enum": [
              "Top",
              "Bottom"
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

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `test` — `Index`, `Elem`, `Part`, `Top/Bottom`, `LComName`, `Type`, `CHK`, `FT`, `FB`, `fss`, `s_use`, `s_max`

### Request / Response JSON

**Request — PSC_CRACK_WIDTH**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_CRACK_WIDTH",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Top/Bottom",
      "LComName",
      "Type",
      "CHK",
      "FT",
      "FB",
      "fss",
      "s_use",
      "s_max"
    ],
    "PARTS": [
      "PartI"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
```

**Request — PSC_CRACK_WIDTH_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_CRACK_WIDTH_VBEAM",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Top/Bottom",
      "LComName",
      "Type",
      "CHK",
      "FT",
      "FB",
      "fss",
      "s_use",
      "s_max"
    ],
    "PARTS": [
      "PartI"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        201
      ]
    }
  }
}
```

**Response — PSC_CRACK_WIDTH**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Top/Bottom",
      "LComName",
      "Type",
      "CHK",
      "FT",
      "FB",
      "fss",
      "s_use",
      "s_max"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[1]",
        "Bottom",
        "cLCB2",
        "-",
        "OK",
        "238.4915",
        "634.0511",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "2",
        "1",
        "I[1]",
        "Top",
        "cLCB2",
        "-",
        "OK",
        "238.4915",
        "634.0511",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "3",
        "2",
        "I[2]",
        "Bottom",
        "cLCB2",
        "-",
        "OK",
        "2087.5340",
        "-2332.7193",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "4",
        "2",
        "I[2]",
        "Top",
        "cLCB2",
        "-",
        "OK",
        "2087.5340",
        "-2332.7193",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "5",
        "3",
        "I[3]",
        "Bottom",
        "cLCB2",
        "-",
        "OK",
        "3146.8461",
        "-4020.8716",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "6",
        "3",
        "I[3]",
        "Top",
        "cLCB2",
        "-",
        "OK",
        "3146.8461",
        "-4020.8716",
        "0.0000",
        "0.0000",
        "0.0000"
      ]
    ]
  }
}
```

**Response — PSC_CRACK_WIDTH_VBEAM**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Top/Bottom",
      "LComName",
      "Type",
      "CHK",
      "FT",
      "FB",
      "fss",
      "s_use",
      "s_max"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "Bottom",
        "cLCB2",
        "-",
        "OK",
        "718.8343",
        "-593.0222",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "2",
        "201",
        "I",
        "Top",
        "-",
        "-",
        "-",
        "-",
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
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_CRACK_WIDTH",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Top/Bottom",
      "LComName",
      "Type",
      "CHK",
      "FT",
      "FB",
      "fss",
      "s_use",
      "s_max"
    ],
    "PARTS": [
      "PartI"
    ],
    "NODE_ELEMS": {
      "TO": "1to3"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 20. `TABLE` · `PSC_FLEXURE` — Check Flexure Strength

> **기능** 휨강도 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58329524570905](https://support.midasuser.com/hc/en-us/articles/58329524570905)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · Check Flexure Strength: "PSC_FLEXURE" · Check Flexure Strength (Virtual Beam): "PSC_FLEXURE_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 8 | [General] Element Parts | `"PARTS"` | array | ["All"] | Optional |
| 9 | [General] Positive/Negative | `"POS_NEG"` | array | ["All"] | Optional |

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
          "description": "Check Flexure Strength - Result Table Type",
          "enum": [
            "PSC_FLEXURE",
            "PSC_FLEXURE_VBEAM"
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
              "Elem",
              "Part",
              "Positive/Negative",
              "LComName",
              "Type",
              "CHK",
              "Muy",
              "Mcr",
              "Mny",
              "PhiMny",
              "Ratio",
              "PhiMny/min"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Element No. Input",
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
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        },
        "POS_NEG": {
          "type": "array",
          "description": "Positive or Negative Moment",
          "items": {
            "type": "string",
            "enum": [
              "Positive",
              "Negative"
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

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `TEST` — `Index`, `Elem`, `Part`, `Positive/Negative`, `LComName`, `Type`, `CHK`, `Muy`, `Mcr`, `Mny`, `PhiMny`, `Ratio`, `PhiMny/min`

### Request / Response JSON

**Request — PSC_FLEXURE**

```json
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_FLEXURE",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Positive/Negative",
      "LComName",
      "Type",
      "CHK",
      "Muy",
      "Mcr",
      "Mny",
      "PhiMny",
      "Ratio",
      "PhiMny/min"
    ],
    "PARTS": [
      "PartI"
    ],
    "POS_NEG": [
      "Positive"
    ]
  }
}
```

**Request — PSC_FLEXURE_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_FLEXURE_VBEAM",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Positive/Negative",
      "LComName",
      "Type",
      "CHK",
      "Muy",
      "Mcr",
      "Mny",
      "PhiMny",
      "Ratio",
      "PhiMny/min"
    ],
    "PARTS": [
      "PartI"
    ],
    "POS_NEG": [
      "Positive"
    ]
  }
}
```

**Response — PSC_FLEXURE**

```json
{
  "TEST": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Positive/Negative",
      "LComName",
      "Type",
      "CHK",
      "Muy",
      "Mcr",
      "Mny",
      "PhiMny",
      "Ratio",
      "PhiMny/min"
    ],
    "DATA": [
      [
        "1",
        "46",
        "I[1]",
        "Positive",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "39255.5537",
        "8404.5356",
        "6303.4017",
        "0.0000",
        "larger than 100"
      ],
      [
        "2",
        "47",
        "I[2]",
        "Positive",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "39275.0927",
        "8404.5356",
        "6303.4017",
        "0.0000",
        "larger than 100"
      ],
      [
        "3",
        "48",
        "I[3]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "529.5963",
        "39448.4986",
        "8404.5356",
        "6303.4017",
        "0.0840",
        "8.9491"
      ],
      [
        "4",
        "49",
        "I[4]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1328.2398",
        "39675.8249",
        "8404.5356",
        "6303.4017",
        "0.2107",
        "3.5682"
      ],
      [
        "5",
        "50",
        "I[5]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1440.0132",
        "39716.4275",
        "8404.5356",
        "6303.4017",
        "0.2285",
        "3.2912"
      ],
      [
        "6",
        "51",
        "I[6]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1965.0824",
        "39880.7109",
        "8404.5356",
        "6303.4017",
        "0.3117",
        "2.4118"
      ],
      [
        "7",
        "148",
        "I[104]",
        "Positive",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "39265.0220",
        "8404.5356",
        "6303.4017",
        "0.0000",
        "larger than 100"
      ],
      [
        "8",
        "149",
        "I[105]",
        "Positive",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "39283.7178",
        "8404.5356",
        "6303.4017",
        "0.0000",
        "larger than 100"
      ],
      [
        "9",
        "150",
        "I[106]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "548.6292",
        "39449.9412",
        "8404.5356",
        "6303.4017",
        "0.0870",
        "8.6386"
      ],
      [
        "10",
        "151",
        "I[107]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1341.7895",
        "39667.5397",
        "8404.5356",
        "6303.4017",
        "0.2129",
        "3.5321"
      ],
      [
        "11",
        "152",
        "I[108]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1464.4618",
        "39707.6965",
        "8404.5356",
        "6303.4017",
        "0.2323",
        "3.2363"
      ],
      [
        "12",
        "153",
        "I[109]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1996.7806",
        "39867.4023",
        "8404.5356",
        "6303.4017",
        "0.3168",
        "2.3735"
      ],
      [
        "13",
        "250",
        "I[207]",
        "Positive",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "39259.2475",
        "8404.5356",
        "6303.4017",
        "0.0000",
        "larger than 100"
      ],
      [
        "14",
        "251",
        "I[208]",
        "Positive",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "39279.5194",
        "8404.5356",
        "6303.4017",
        "0.0000",
        "larger than 100"
      ],
      [
        "15",
        "252",
        "I[209]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "549.8661",
        "39450.9671",
        "8404.5356",
        "6303.4017",
        "0.0872",
        "8.6192"
      ],
      [
        "16",
        "253",
        "I[210]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1376.2448",
        "39676.4281",
        "8404.5356",
        "6303.4017",
        "0.2183",
        "3.4437"
      ],
      [
        "17",
        "254",
        "I[211]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1500.1698",
        "39717.5487",
        "8404.5356",
        "6303.4017",
        "0.2380",
        "3.1592"
      ],
      [
        "18",
        "255",
        "I[212]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "2053.9119",
        "39882.3212",
        "8404.5356",
        "6303.4017",
        "0.3258",
        "2.3075"
      ],
      [
        "19",
        "352",
        "I[310]",
        "Positive",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "39259.2487",
        "8404.5356",
        "6303.4017",
        "0.0000",
        "larger than 100"
      ],
      [
        "20",
        "353",
        "I[311]",
        "Positive",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "39279.5050",
        "8404.5356",
        "6303.4017",
        "0.0000",
        "larger than 100"
      ],
      [
        "21",
        "354",
        "I[312]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "555.2808",
        "39450.7428",
        "8404.5356",
        "6303.4017",
        "0.0881",
        "8.5351"
      ],
      [
        "22",
        "355",
        "I[313]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1383.0897",
        "39676.2814",
        "8404.5356",
        "6303.4017",
        "0.2194",
        "3.4267"
      ],
      [
        "23",
        "356",
        "I[314]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1506.6121",
        "39717.3384",
        "8404.5356",
        "6303.4017",
        "0.2390",
        "3.1457"
      ],
      [
        "24",
        "357",
        "I[315]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "2060.1353",
        "39882.0459",
        "8404.5356",
        "6303.4017",
        "0.3268",
        "2.3005"
      ],
      [
        "25",
        "454",
        "I[413]",
        "Positive",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "39265.0110",
        "8404.5356",
        "7984.3088",
        "0.0000",
        "larger than 100"
      ],
      [
        "26",
        "455",
        "I[414]",
        "Positive",
        "gLCB6",
        "FX-MAX",
        "OK",
        "12.7476",
        "39283.6435",
        "8404.5356",
        "6303.4017",
        "0.0020",
        "larger than 100"
      ],
      [
        "27",
        "456",
        "I[415]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "584.4453",
        "39449.8667",
        "8404.5356",
        "6303.4017",
        "0.0927",
        "8.1092"
      ],
      [
        "28",
        "457",
        "I[416]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1374.0609",
        "39667.3196",
        "8404.5356",
        "6303.4017",
        "0.2180",
        "3.4492"
      ],
      [
        "29",
        "458",
        "I[417]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1496.5402",
        "39707.4556",
        "8404.5356",
        "6303.4017",
        "0.2374",
        "3.1669"
      ],
      [
        "30",
        "459",
        "I[418]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "2025.6189",
        "39866.7837",
        "8404.5356",
        "6303.4017",
        "0.3214",
        "2.3397"
      ],
      [
        "31",
        "556",
        "I[516]",
        "Positive",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "39254.1974",
        "8404.5356",
        "7984.3088",
        "0.0000",
        "larger than 100"
      ],
      [
        "32",
        "557",
        "I[517]",
        "Positive",
        "gLCB6",
        "FX-MAX",
        "OK",
        "15.3581",
        "39273.3630",
        "8404.5356",
        "6303.4017",
        "0.0024",
        "larger than 100"
      ],
      [
        "33",
        "558",
        "I[518]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "576.2388",
        "39446.3435",
        "8404.5356",
        "6303.4017",
        "0.0914",
        "8.2247"
      ],
      [
        "34",
        "559",
        "I[519]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1367.5329",
        "39673.0773",
        "8404.5356",
        "6303.4017",
        "0.2170",
        "3.4657"
      ],
      [
        "35",
        "560",
        "I[520]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1478.1051",
        "39713.6341",
        "8404.5356",
        "6303.4017",
        "0.2345",
        "3.2064"
      ],
      [
        "36",
        "561",
        "I[521]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "OK",
        "1997.6868",
        "39877.5764",
        "8404.5356",
        "6303.4017",
        "0.3169",
        "2.3724"
      ],
      [
        "37",
        "659",
        "I[2487]",
        "Positive",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "38",
        "2404",
        "I[2554]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "NG",
        "0.0000",
        "28017.0887",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "39",
        "2405",
        "I[2555]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "NG",
        "0.0000",
        "28017.0887",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "40",
        "2406",
        "I[2556]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "NG",
        "0.0000",
        "28017.0887",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "41",
        "2407",
        "I[2557]",
        "Positive",
        "gLCB1",
        "FX-MAX",
        "NG",
        "0.0000",
        "28017.0887",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ]
    ]
  }
}
```

**Response — PSC_FLEXURE_VBEAM**

```json
{
  "TEST": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Positive/Negative",
      "LComName",
      "Type",
      "CHK",
      "Muy",
      "Mcr",
      "Mny",
      "PhiMny",
      "Ratio",
      "PhiMny/min"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "Positive",
        "cLCB1",
        "-",
        "OK",
        "3964.3236",
        "2662.9898",
        "6185.3591",
        "6185.3591",
        "0.6409",
        "2.3227"
      ]
    ]
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "TEST",
    "TABLE_TYPE": "PSC_FLEXURE",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Positive/Negative",
      "LComName",
      "Type",
      "CHK",
      "Muy",
      "Mcr",
      "Mny",
      "PhiMny",
      "Ratio",
      "PhiMny/min"
    ],
    "PARTS": [
      "PartI"
    ],
    "POS_NEG": [
      "Positive"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 21. `TABLE` · `PSC_SHEAR` — Check Shear Strength

> **기능** 전단강도 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58333287089689](https://support.midasuser.com/hc/en-us/articles/58333287089689)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · Check Shear Strength: "PSC_SHEAR" · Check Shear Strength (Virtual Beam): "PSC_SHEAR_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 8 | [General] Element Parts | `"PARTS"` | array | ["All"] | Optional |
| 9 | [General] Max/Min | `"MAX_MIN"` | array | ["All"] | Optional |

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
          "description": "Check Shear Strength - Result Table Type",
          "enum": [
            "PSC_SHEAR",
            "PSC_SHEAR_VBEAM"
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
              "Elem",
              "Part",
              "Max/Min",
              "LComName",
              "Type",
              "CHK",
              "Vu",
              "Mu",
              "Vn",
              "Phi",
              "Vc",
              "Vs",
              "Vp",
              "PhiVn",
              "de",
              "dv",
              "ex",
              "theta",
              "beta",
              "Avs",
              "Ast",
              "Al",
              "bv",
              "Avs_min",
              "Avs_req",
              "Al_min",
              "bv_min",
              "Vri",
              "Vui",
              "Interface_Shear"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Element No. Input",
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
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        },
        "MAX_MIN": {
          "type": "array",
          "description": "Maximum or Minimum Shear",
          "items": {
            "type": "string",
            "enum": [
              "Max",
              "Min"
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

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `test` — `Index`, `Elem`, `Part`, `Max/Min`, `LComName`, `Type`, `CHK`, `Vu`, `Mu`, `Vn`, `Phi`, `Vc`, `Vs`, `Vp`, `PhiVn`, `de`, `dv`, `ex`, `theta`, `beta`, `Avs`, `Ast`, `Al`, `bv`, `Avs_min`, `Avs_req`, `Al_min`, `bv_min`, `Vri`, `Vui`

### Request / Response JSON

**Request — PSC_SHEAR**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_SHEAR",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "Type",
      "CHK",
      "Vu",
      "Mu",
      "Vn",
      "Phi",
      "Vc",
      "Vs",
      "Vp",
      "PhiVn",
      "de",
      "dv",
      "ex",
      "theta",
      "beta",
      "Avs",
      "Ast",
      "Al",
      "bv",
      "Avs_min",
      "Avs_req",
      "Al_min",
      "bv_min",
      "Vri",
      "Vui",
      "Interface_Shear"
    ],
    "PARTS": [
      "PartI"
    ],
    "MAX_MIN": [
      "Max"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        46,
        47
      ]
    }
  }
}
```

**Request — PSC_SHEAR_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_SHEAR_VBEAM",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "Type",
      "CHK",
      "Vu",
      "Mu",
      "Vn",
      "Phi",
      "Vc",
      "Vs",
      "Vp",
      "PhiVn",
      "de",
      "dv",
      "ex",
      "theta",
      "beta",
      "Avs",
      "Ast",
      "Al",
      "bv",
      "Avs_min",
      "Avs_req",
      "Al_min",
      "bv_min",
      "Vri",
      "Vui",
      "Interface_Shear"
    ],
    "PARTS": [
      "PartI"
    ],
    "MAX_MIN": [
      "Max"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        201
      ]
    }
  }
}
```

**Response — PSC_SHEAR**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "Type",
      "CHK",
      "Vu",
      "Mu",
      "Vn",
      "Phi",
      "Vc",
      "Vs",
      "Vp",
      "PhiVn",
      "de",
      "dv",
      "ex",
      "theta",
      "beta",
      "Avs",
      "Ast",
      "Al",
      "bv",
      "Avs_min",
      "Avs_req",
      "Al_min",
      "bv_min",
      "Vri",
      "Vui"
    ],
    "DATA": [
      [
        "1",
        "46",
        "I[1]",
        "Max",
        "gLCB14",
        "-",
        "NG",
        "129.2448",
        "-7963.3324",
        "80.4168",
        "0.9000",
        "80.4168",
        "0.0000",
        "0.0000",
        "72.3751",
        "0.2540",
        "1.1521",
        "0.0060",
        "50.0000",
        "0.8727",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0125",
        "-",
        "-"
      ],
      [
        "2",
        "47",
        "I[2]",
        "Max",
        "gLCB12",
        "FX-MAX",
        "OK",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "-",
        "-"
      ]
    ]
  }
}
```

**Response — PSC_SHEAR_VBEAM**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "Type",
      "CHK",
      "Vu",
      "Mu",
      "Vn",
      "Phi",
      "Vc",
      "Vs",
      "Vp",
      "PhiVn",
      "de",
      "dv",
      "ex",
      "theta",
      "beta",
      "Avs",
      "Ast",
      "Al",
      "bv",
      "Avs_min",
      "Avs_req",
      "Al_min",
      "bv_min",
      "Vri",
      "Vui"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "Max",
        "cLCB1",
        "-",
        "OK",
        "-844.2907",
        "3964.3236",
        "2058.3947",
        "0.9000",
        "1957.2526",
        "0.0000",
        "101.1422",
        "1852.5553",
        "2.0500",
        "2.2853",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.3400",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0455",
        "-",
        "-"
      ]
    ]
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_SHEAR",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "Type",
      "CHK",
      "Vu",
      "Mu",
      "Vn",
      "Phi",
      "Vc",
      "Vs",
      "Vp",
      "PhiVn",
      "de",
      "dv",
      "ex",
      "theta",
      "beta",
      "Avs",
      "Ast",
      "Al",
      "bv",
      "Avs_min",
      "Avs_req",
      "Al_min",
      "bv_min",
      "Vri",
      "Vui",
      "Interface_Shear"
    ],
    "PARTS": [
      "PartI"
    ],
    "MAX_MIN": [
      "Max"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        46,
        47
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

## 22. `TABLE` · `PSC_SHEAR_TORSION` — Check Combined Shear and Torsion Strength

> **기능** 전단과 비틀림의 조합 강도 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58332864321305](https://support.midasuser.com/hc/en-us/articles/58332864321305)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string |  | Optional |
| 2 | [General] Table Type · Check Combined Shear and Torsion Strength: "PSC_SHEAR_TORSION" · Check Combined Shear and Torsion Strength (Virtual Beam): "PSC_SHEAR_TORSION_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 5.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range (e.g., '1to160') | `"TO"` | string | - | Optional |
| 8 | [General] Element Parts | `"PARTS"` | array | ["All"] | Optional |
| 9 | [General] Max/Min | `"MAX_MIN"` | array | ["All"] | Optional |

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
          "description": "Check Combined Shear and Torsion Strength - Result Table Type",
          "enum": [
            "PSC_SHEAR_TORSION",
            "PSC_SHEAR_TORSION_VBEAM"
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
              "Elem",
              "Part",
              "Max/Min",
              "LComName",
              "Type",
              "CHK",
              "Vu",
              "Mu",
              "Tu",
              "Vn",
              "Tn",
              "Phi",
              "Phi_t",
              "Vc",
              "Vs",
              "Vp",
              "PhiVn",
              "Phi_tTn",
              "de",
              "dv",
              "ex",
              "theta",
              "beta",
              "Avs",
              "Ast",
              "Al",
              "bv",
              "Avs_min",
              "Avs_req",
              "Al_min",
              "bv_min",
              "At",
              "At_req"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Element No. Input",
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
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        },
        "MAX_MIN": {
          "type": "array",
          "description": "Shear Max/Min or Torsion Max",
          "items": {
            "type": "string",
            "enum": [
              "V-Max",
              "V-Min",
              "T-Max"
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

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- **PSC_SHEAR_TORSION** — `test` — `Index`, `Elem`, `Part`, `Max/Min`, `LComName`, `Type`, `CHK`, `Vu`, `Mu`, `Tu`, `Vn`, `Tn`, `Phi`, `Phi_t`, `Vc`, `Vs`, `Vp`, `PhiVn`, `de`, `dv`, `ex`, `theta`, `beta`, `Avs`, `Ast`, `Al`, `bv`, `Avs_min`, `Avs_req`, `Al_min`, `bv_min`, `At`, `At_req`
- **PSC_SHEAR_TORSION_VBEAM** — `test` — `Index`, `Elem`, `Part`, `Max/Min`, `LComName`, `Type`, `CHK`, `Vu`, `Mu`, `Tu`, `Vn`, `Tn`, `Phi`, `Phi_t`, `Vc`, `Vs`, `Vp`, `PhiVn`, `Phi_tTn`, `de`, `dv`, `ex`, `theta`, `beta`, `Avs`, `Ast`, `Al`, `bv`, `Avs_min`, `Avs_req`, `Al_min`, `bv_min`, `At`, `At_req`

### Request / Response JSON

**Request — PSC_SHEAR_TORSION**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_SHEAR_TORSION",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "Type",
      "CHK",
      "Vu",
      "Mu",
      "Tu",
      "Vn",
      "Tn",
      "Phi",
      "Phi_t",
      "Vc",
      "Vs",
      "Vp",
      "PhiVn",
      "Phi_tTn",
      "de",
      "dv",
      "ex",
      "theta",
      "beta",
      "Avs",
      "Ast",
      "Al",
      "bv",
      "Avs_min",
      "Avs_req",
      "Al_min",
      "bv_min",
      "At",
      "At_req"
    ],
    "PARTS": [
      "PartI"
    ],
    "MAX_MIN": [
      "V-Max"
    ]
  }
}
```

**Request — PSC_SHEAR_TORSION_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_SHEAR_TORSION_VBEAM",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "Type",
      "CHK",
      "Vu",
      "Mu",
      "Tu",
      "Vn",
      "Tn",
      "Phi",
      "Phi_t",
      "Vc",
      "Vs",
      "Vp",
      "PhiVn",
      "Phi_tTn",
      "de",
      "dv",
      "ex",
      "theta",
      "beta",
      "Avs",
      "Ast",
      "Al",
      "bv",
      "Avs_min",
      "Avs_req",
      "Al_min",
      "bv_min",
      "At",
      "At_req"
    ],
    "PARTS": [
      "PartI"
    ],
    "MAX_MIN": [
      "V-Max"
    ]
  }
}
```

**Response — PSC_SHEAR_TORSION**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "Type",
      "CHK",
      "Vu",
      "Mu",
      "Tu",
      "Vn",
      "Tn",
      "Phi",
      "Phi_t",
      "Vc",
      "Vs",
      "Vp",
      "PhiVn",
      "de",
      "dv",
      "ex",
      "theta",
      "beta",
      "Avs",
      "Ast",
      "Al",
      "bv",
      "Avs_min",
      "Avs_req",
      "Al_min",
      "bv_min",
      "At",
      "At_req"
    ],
    "DATA": [
      [
        "1",
        "46",
        "I[1]",
        "V-Max",
        "gLCB14",
        "-",
        "OK",
        "129.2448",
        "-7963.3324",
        "-0.1000",
        "80.4168",
        "0.0000",
        "0.9000",
        "0.9000",
        "80.4168",
        "0.0000",
        "0.0000",
        "72.3751",
        "0.2540",
        "1.1521",
        "0.0060",
        "50.0000",
        "0.8727",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0125",
        "0.0000",
        "0.0000"
      ],
      [
        "2",
        "47",
        "I[2]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "3",
        "48",
        "I[3]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "4",
        "49",
        "I[4]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "5",
        "50",
        "I[5]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "6",
        "51",
        "I[6]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "7",
        "148",
        "I[104]",
        "V-Max",
        "gLCB14",
        "-",
        "OK",
        "162.7951",
        "-7943.7234",
        "-0.0737",
        "80.4168",
        "0.0000",
        "0.9000",
        "0.9000",
        "80.4168",
        "0.0000",
        "0.0000",
        "72.3751",
        "0.2540",
        "1.1521",
        "0.0060",
        "50.0000",
        "0.8727",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0157",
        "0.0000",
        "0.0000"
      ],
      [
        "8",
        "149",
        "I[105]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "9",
        "150",
        "I[106]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "10",
        "151",
        "I[107]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "11",
        "152",
        "I[108]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "12",
        "153",
        "I[109]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "13",
        "250",
        "I[207]",
        "V-Max",
        "gLCB14",
        "-",
        "OK",
        "153.1010",
        "-7968.8293",
        "-0.0387",
        "80.4168",
        "0.0000",
        "0.9000",
        "0.9000",
        "80.4168",
        "0.0000",
        "0.0000",
        "72.3751",
        "0.2540",
        "1.1521",
        "0.0060",
        "50.0000",
        "0.8727",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0148",
        "0.0000",
        "0.0000"
      ],
      [
        "14",
        "251",
        "I[208]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "15",
        "252",
        "I[209]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "16",
        "253",
        "I[210]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "17",
        "254",
        "I[211]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "18",
        "255",
        "I[212]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "19",
        "352",
        "I[310]",
        "V-Max",
        "gLCB14",
        "-",
        "OK",
        "132.3113",
        "-7967.0353",
        "0.0133",
        "80.4168",
        "0.0000",
        "0.9000",
        "0.9000",
        "80.4168",
        "0.0000",
        "0.0000",
        "72.3751",
        "0.2540",
        "1.1521",
        "0.0060",
        "50.0000",
        "0.8727",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0128",
        "0.0000",
        "0.0000"
      ],
      [
        "20",
        "353",
        "I[311]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "21",
        "354",
        "I[312]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "22",
        "355",
        "I[313]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "23",
        "356",
        "I[314]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "24",
        "357",
        "I[315]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "25",
        "454",
        "I[413]",
        "V-Max",
        "gLCB14",
        "-",
        "OK",
        "91.8793",
        "-7931.2428",
        "0.0497",
        "80.4168",
        "0.0000",
        "0.9000",
        "0.9000",
        "80.4168",
        "0.0000",
        "0.0000",
        "72.3751",
        "0.2540",
        "1.1521",
        "0.0060",
        "50.0000",
        "0.8727",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0089",
        "0.0000",
        "0.0000"
      ],
      [
        "26",
        "455",
        "I[414]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "27",
        "456",
        "I[415]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "28",
        "457",
        "I[416]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "29",
        "458",
        "I[417]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "30",
        "459",
        "I[418]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "31",
        "556",
        "I[516]",
        "V-Max",
        "gLCB14",
        "-",
        "OK",
        "32.8478",
        "-7950.1354",
        "0.0822",
        "80.4168",
        "0.0000",
        "0.9000",
        "0.9000",
        "80.4168",
        "0.0000",
        "0.0000",
        "72.3751",
        "0.2540",
        "1.1521",
        "0.0060",
        "50.0000",
        "0.8727",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0032",
        "0.0000",
        "0.0000"
      ],
      [
        "32",
        "557",
        "I[517]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "33",
        "558",
        "I[518]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "34",
        "559",
        "I[519]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "35",
        "560",
        "I[520]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "36",
        "561",
        "I[521]",
        "V-Max",
        "gLCB13",
        "MZ-MIN",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "442.2925",
        "0.0000",
        "0.9000",
        "0.9000",
        "442.2925",
        "0.0000",
        "0.0000",
        "398.0633",
        "0.0000",
        "1.1521",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "37",
        "659",
        "I[2487]",
        "V-Max",
        "gLCB14",
        "-",
        "OK",
        "802.7569",
        "-77.8886",
        "0.1793",
        "80.4168",
        "0.0000",
        "0.9000",
        "0.9000",
        "80.4168",
        "0.0000",
        "0.0000",
        "72.3751",
        "0.0000",
        "1.1521",
        "0.0060",
        "50.0000",
        "0.8727",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.1524",
        "0.0000",
        "0.0000",
        "-",
        "0.0774",
        "0.0000",
        "0.0000"
      ],
      [
        "38",
        "2404",
        "I[2554]",
        "V-Max",
        "gLCB16",
        "-",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "2219.8917",
        "0.0000",
        "0.9000",
        "0.9000",
        "4439.7834",
        "0.0000",
        "0.0000",
        "1997.9025",
        "0.0000",
        "2.1600",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.8160",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "39",
        "2405",
        "I[2555]",
        "V-Max",
        "gLCB16",
        "-",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "2219.8917",
        "0.0000",
        "0.9000",
        "0.9000",
        "4439.7834",
        "0.0000",
        "0.0000",
        "1997.9025",
        "0.0000",
        "2.1600",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.8160",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "40",
        "2406",
        "I[2556]",
        "V-Max",
        "gLCB16",
        "-",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "2219.8917",
        "0.0000",
        "0.9000",
        "0.9000",
        "4439.7834",
        "0.0000",
        "0.0000",
        "1997.9025",
        "0.0000",
        "2.1600",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.8160",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "41",
        "2407",
        "I[2557]",
        "V-Max",
        "gLCB16",
        "-",
        "OK",
        "0.0000",
        "0.0000",
        "0.0000",
        "2219.8917",
        "0.0000",
        "0.9000",
        "0.9000",
        "4439.7834",
        "0.0000",
        "0.0000",
        "1997.9025",
        "0.0000",
        "2.1600",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.8160",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ]
    ]
  }
}
```

**Response — PSC_SHEAR_TORSION_VBEAM**

```json
{
  "test": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "Type",
      "CHK",
      "Vu",
      "Mu",
      "Tu",
      "Vn",
      "Tn",
      "Phi",
      "Phi_t",
      "Vc",
      "Vs",
      "Vp",
      "PhiVn",
      "Phi_tTn",
      "de",
      "dv",
      "ex",
      "theta",
      "beta",
      "Avs",
      "Ast",
      "Al",
      "bv",
      "Avs_min",
      "Avs_req",
      "Al_min",
      "bv_min",
      "At",
      "At_req"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "V-Max",
        "cLCB1",
        "-",
        "OK",
        "-844.2907",
        "3964.3236",
        "0.0000",
        "2058.3947",
        "0.0000",
        "0.9000",
        "0.9000",
        "1957.2526",
        "0.0000",
        "101.1422",
        "1852.5553",
        "0.0000",
        "2.0500",
        "2.2853",
        "0.0000",
        "29.0000",
        "4.8000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.3400",
        "0.0000",
        "0.0000",
        "-",
        "0.0455",
        "0.0000",
        "0.0000"
      ]
    ]
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "test",
    "TABLE_TYPE": "PSC_SHEAR_TORSION",
    "COMPONENTS": [
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "Type",
      "CHK",
      "Vu",
      "Mu",
      "Tu",
      "Vn",
      "Tn",
      "Phi",
      "Phi_t",
      "Vc",
      "Vs",
      "Vp",
      "PhiVn",
      "Phi_tTn",
      "de",
      "dv",
      "ex",
      "theta",
      "beta",
      "Avs",
      "Ast",
      "Al",
      "bv",
      "Avs_min",
      "Avs_req",
      "Al_min",
      "bv_min",
      "At",
      "At_req"
    ],
    "PARTS": [
      "PartI"
    ],
    "MAX_MIN": [
      "V-Max"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 23. `REPORT` — Excel Report

> **기능** PSC 설계 결과를 Excel 보고서로 내보냅니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/REPORT
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738145948953](https://support.midasuser.com/hc/en-us/articles/64738145948953)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Excel report export folder path. If empty, the project file directory is used. | `"EXPORT_PATH"` | string |  | Optional |
| 2 | [General] Excel report output file name without extension. If empty, the project file name is used. | `"OUTPUT_NAME"` | string |  | Optional |

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
      "required": [],
      "additionalProperties": false,
      "properties": {
        "EXPORT_PATH": {
          "type": "string",
          "description": "Excel report export folder path. If empty, the project file directory is used.",
          "default": ""
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "Excel report output file name without extension. If empty, the project file name is used.",
          "default": ""
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `PSC_EXCEL_RESPONSE`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PSC_Design_Report_AASHTO-LRFD24"
  }
}
```

**Response**

```json
{
  "PSC_EXCEL_RESPONSE": {
    "SUCCESS": true,
    "FILE_PATH": "C:\\MIDAS\\Report\\PSC_Design_Report_AASHTO-LRFD24.xlsx",
    "MESSAGE": ""
  }
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/REPORT"

payload = json.loads(r'''
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PSC_Design_Report_AASHTO-LRFD24"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 24. `MEMB-VBEAM` — PSC Segment Assignment - Virtual Beam

> **기능** PSC 설계용 가상보를 부재로 배정합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/MEMB-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 57945521269145](https://support.midasuser.com/hc/en-us/articles/57945521269145)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Element List | `"AELEM"` | array | - | **Required** |
| 2 | [General] Allow Single Element Member | `"ELEM_MEMBER"` | boolean | false | Optional |
| 3 | [General] Joint Type · Resin: 0 · Cement: 1 | `"JOINT_TYPE"` | integer | 0 | Optional |

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
            "ELEM_MEMBER": {
              "type": "boolean",
              "description": "Allow Single Element Member",
              "default": false
            },
            "JOINT_TYPE": {
              "type": "integer",
              "description": "Joint Type",
              "enum": [
                0,
                1
              ],
              "default": 0
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

- `PSCMEMB`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "AELEM": [
        201
      ],
      "ELEM_MEMBER": true,
      "JOINT_TYPE": 1
    }
  }
}
```

**Response**

```json
{
  "PSCMEMB": {
    "1": {
      "AELEM": [
        201
      ],
      "ELEM_MEMBER": true,
      "JOINT_TYPE": 1
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/MEMB-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "AELEM": [
        201
      ],
      "ELEM_MEMBER": true,
      "JOINT_TYPE": 1
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```

### 이전 한국어 원문

**원문** [한국어 57945562325273](https://support.midasuser.com/hc/ko/articles/57945562325273)

**원문 Active Methods** `POST` · `GET` · `PUT` · `DELETE`

> ⚠️ 이전 표에는 ELEM_TYPE 행이 있습니다. 최신 표와 요청 예제는 가상보의 URI를 사용합니다. 두 JSON Schema는 같습니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Element List | `"AELEM"` | Array [integer] | - | **Required** |
| 2 | [General] Element Type · Element: "0" · Virtual Beam: "1" | `"ELEM_TYPE"` | integer | 0 | **Required** |
| 3 | [General] Allow Single Element Member | `"ELEM_MEMBER"` | boolean | false | Optional |
| 4 | [General] Joint Type · Resin: "0" · Cement: "1" | `"JOINT_TYPE"` | integer | 0 | **Required** |

**JSON Schema**

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
            "ELEM_MEMBER": {
              "type": "boolean",
              "description": "Allow Single Element Member",
              "default": false
            },
            "JOINT_TYPE": {
              "type": "integer",
              "description": "Joint Type",
              "enum": [
                0,
                1
              ],
              "default": 0
            }
          }
        }
      }
    }
  }
}
```


---

## 25. `INFS-VBEAM` — Interface shear - Virtual Beam

> **기능** 가상보의 접합면 전단 검토 조건을 입력합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/INFS-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 57945623457561](https://support.midasuser.com/hc/en-us/articles/57945623457561)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings, where each entry represents a virtual beam (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] SURFACE_CLASSIFICATION_I | `"SURFACE_CLASSIFICATION_I"` | object | - | Optional |
| 1.1 | └ [General] Surface Classification · Roughened (CIP slab): 0 · Monolithically: 1 · Intentionally roughened (LWC): 2 · Intentionally roughened (NWC): 3 · Not intentionally roughened: 4 · Anchored: 5 | `"SURFACE_CLASSIFICATION"` | integer | 0 | Optional |
| 1.2 | └ [General] Width of the interfacial cross-section engaged in shear transfer, Bvi · Minimum: 0 | `"BVI"` | number | 0 | Optional |
| 1.3 | └ [General] Cross-sectional area of reinforcement crossing the interfacial shear plane, Avf · Minimum: 0 | `"AVF"` | number | 0 | Optional |
| 1.4 | └ [General] Yield strength of reinforcement crossing the interfacial shear plane, Fy · Minimum: 0 | `"FY"` | number | 0 | Optional |
| 2 | [General] SURFACE_CLASSIFICATION_J | `"SURFACE_CLASSIFICATION_J"` | object | - | Optional |
| 2.1 | └ [General] Surface Classification · Roughened (CIP slab): 0 · Monolithically: 1 · Intentionally roughened (LWC): 2 · Intentionally roughened (NWC): 3 · Not intentionally roughened: 4 · Anchored: 5 | `"SURFACE_CLASSIFICATION"` | integer | 0 | Optional |
| 2.2 | └ [General] Width of the interfacial cross-section engaged in shear transfer, Bvi · Minimum: 0 | `"BVI"` | number | 0 | Optional |
| 2.3 | └ [General] Cross-sectional area of reinforcement crossing the interfacial shear plane, Avf · Minimum: 0 | `"AVF"` | number | 0 | Optional |
| 2.4 | └ [General] Yield strength of reinforcement crossing the interfacial shear plane, Fy · Minimum: 0 | `"FY"` | number | 0 | Optional |

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
      "description": "Object keyed by ID strings, where each entry represents a virtual beam (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "SURFACE_CLASSIFICATION_I": {
              "type": "object",
              "description": "SURFACE_CLASSIFICATION_I",
              "additionalProperties": false,
              "properties": {
                "SURFACE_CLASSIFICATION": {
                  "type": "integer",
                  "description": "Surface Classification",
                  "enum": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5
                  ],
                  "default": 0
                },
                "BVI": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Width of the interfacial cross-section engaged in shear transfer",
                  "default": 0
                },
                "AVF": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Cross-sectional area of reinforcement crossing the interfacial shear plane",
                  "default": 0
                },
                "FY": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Yield strength of reinforcement crossing the interfacial shear plane",
                  "default": 0
                }
              }
            },
            "SURFACE_CLASSIFICATION_J": {
              "type": "object",
              "description": "SURFACE_CLASSIFICATION_J",
              "additionalProperties": false,
              "properties": {
                "SURFACE_CLASSIFICATION": {
                  "type": "integer",
                  "description": "Surface Classification",
                  "enum": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5
                  ],
                  "default": 0
                },
                "BVI": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Width of the interfacial cross-section engaged in shear transfer",
                  "default": 0
                },
                "AVF": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Cross-sectional area of reinforcement crossing the interfacial shear plane",
                  "default": 0
                },
                "FY": {
                  "type": "number",
                  "minimum": 0,
                  "default": 0,
                  "description": "Yield strength of reinforcement crossing the interfacial shear plane"
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

- `INFS`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "201": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 1,
        "BVI": 0.6,
        "AVF": 0.000516,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 2,
        "BVI": 0.6,
        "AVF": 0.000387,
        "FY": 413685
      }
    }
  }
}
```

**Response**

```json
{
  "INFS": {
    "201": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 1,
        "BVI": 0.6,
        "AVF": 0.000516,
        "FY": 413685.0
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 2,
        "BVI": 0.6,
        "AVF": 0.000387,
        "FY": 413685.0
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/INFS-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "201": {
      "SURFACE_CLASSIFICATION_I": {
        "SURFACE_CLASSIFICATION": 1,
        "BVI": 0.6,
        "AVF": 0.000516,
        "FY": 413685
      },
      "SURFACE_CLASSIFICATION_J": {
        "SURFACE_CLASSIFICATION": 2,
        "BVI": 0.6,
        "AVF": 0.000387,
        "FY": 413685
      }
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```

### 이전 한국어 원문

**원문** [한국어 57945623305113](https://support.midasuser.com/hc/ko/articles/57945623305113)

**원문 Active Methods** `POST` · `GET` · `PUT` · `DELETE`

> ⚠️ 이전 Schema는 INTERFACE_SHEAR와 SURFACE_CLASSIFICATION을 필수로 지정합니다. 영문 Schema는 이 필수 목록을 두지 않고 양 끝의 AVF·BVI·FY 기본값을 0으로 명시합니다.

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings, where each entry represents an element (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] SURFACE_CLASSIFICATION_I | `"SURFACE_CLASSIFICATION_I"` | object | - | Optional |
| 1.1 | └ [General] Surface Classification · Roughened (CIP slab): "0" · Monolithically: "1" · Intentionally roughened (LWC): "2" · Intentionally roughened (NWC): "3" · Not intentionally roughened: "4" · Anchored: "5" | `"SURFACE_CLASSIFICATION"` | integer | 0 | Optional |
| 1.2 | └ [General] Bvi Constraints: · Value Range: >= 0 | `"BVI"` | number | - | Optional |
| 1.3 | └ [General] Avf Constraints: · Value Range: >= 0 | `"AVF"` | number | - | Optional |
| 1.4 | └ [General] Fy Constraints: · Value Range: >= 0 | `"FY"` | number | - | Optional |
| 2 | [General] SURFACE_CLASSIFICATION_J | `"SURFACE_CLASSIFICATION_J"` | object | - | Optional |
| 2.1 | └ [General] Surface Classification · Roughened (CIP slab): "0" · Monolithically: "1" · Intentionally roughened (LWC): "2" · Intentionally roughened (NWC): "3" · Not intentionally roughened: "4" · Anchored: "5" | `"SURFACE_CLASSIFICATION"` | integer | 0 | Optional |
| 2.2 | └ [General] Bvi Constraints: · Value Range: >= 0 | `"BVI"` | number | - | Optional |
| 2.3 | └ [General] Avf Constraints: · Value Range: >= 0 | `"AVF"` | number | - | Optional |
| 2.4 | └ [General] Fy Constraints: · Value Range: >= 0 | `"FY"` | number | - | Optional |

**JSON Schema**

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
      "description": "Object keyed by ID strings, where each entry represents an element (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "INTERFACE_SHEAR",
            "SURFACE_CLASSIFICATION"
          ],
          "additionalProperties": false,
          "properties": {
            "SURFACE_CLASSIFICATION_I": {
              "type": "object",
              "description": "SURFACE_CLASSIFICATION_I",
              "additionalProperties": false,
              "x-ui": {
                "label": "SURFACE_CLASSIFICATION_I",
                "order": 3
              },
              "properties": {
                "SURFACE_CLASSIFICATION": {
                  "type": "integer",
                  "description": "Surface Classification",
                  "enum": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5
                  ],
                  "default": 0,
                  "x-ui": {
                    "component": "RadioGroup",
                    "label": "Surface Classification",
                    "order": 1
                  },
                  "x-enum-labels": {
                    "0": "Roughened (CIP slab)",
                    "1": "Monolithically",
                    "2": "Intentionally roughened (LWC)",
                    "3": "Intentionally roughened (NWC)",
                    "4": "Not intentionally roughened",
                    "5": "Anchored"
                  }
                },
                "BVI": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Width of the interfacial cross-section engaged in shear transfer",
                  "x-ui": {
                    "label": "Bvi",
                    "order": 1
                  }
                },
                "AVF": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Cross-sectional area of reinforcement crossing the interfacial shear plane",
                  "x-ui": {
                    "label": "Avf",
                    "order": 2
                  }
                },
                "FY": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Yield strength of reinforcement crossing the interfacial shear plane",
                  "x-ui": {
                    "label": "Fy",
                    "order": 3
                  }
                }
              }
            },
            "SURFACE_CLASSIFICATION_J": {
              "type": "object",
              "description": "SURFACE_CLASSIFICATION_J",
              "additionalProperties": false,
              "x-ui": {
                "label": "SURFACE_CLASSIFICATION_J",
                "order": 3
              },
              "properties": {
                "SURFACE_CLASSIFICATION": {
                  "type": "integer",
                  "description": "Surface Classification",
                  "enum": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5
                  ],
                  "default": 0,
                  "x-ui": {
                    "component": "RadioGroup",
                    "label": "Surface Classification",
                    "order": 1
                  },
                  "x-enum-labels": {
                    "0": "Roughened (CIP slab)",
                    "1": "Monolithically",
                    "2": "Intentionally roughened (LWC)",
                    "3": "Intentionally roughened (NWC)",
                    "4": "Not intentionally roughened",
                    "5": "Anchored"
                  }
                },
                "BVI": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Width of the interfacial cross-section engaged in shear transfer",
                  "x-ui": {
                    "label": "Bvi",
                    "order": 1
                  }
                },
                "AVF": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Cross-sectional area of reinforcement crossing the interfacial shear plane",
                  "x-ui": {
                    "label": "Avf",
                    "order": 2
                  }
                },
                "FY": {
                  "type": "number",
                  "minimum": 0,
                  "description": "Yield strength of reinforcement crossing the interfacial shear plane",
                  "x-ui": {
                    "label": "Fy",
                    "order": 3
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


---

## 26. `RPSC-VBEAM` — Longitudinal Rebar-Reinforcements - Virtual Beam

> **기능** 가상보의 종방향 철근 보강 정보를 입력합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/RPSC-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738154715545](https://support.midasuser.com/hc/en-us/articles/64738154715545)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a virtual section ID (e.g., "1"). Available only when the model has virtual beams and its PSC design code supports virtual beams. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Same Longitudinal Rebar at I/J | `"OPT_MBAR_J"` | boolean | - | **Required** |
| 2 | [General] Same Shear Rebar at I/J | `"OPT_SBAR_J"` | boolean | - | **Required** |
| 3 | [General] Cracked Section | `"OPT_CRACKED"` | boolean | - | Optional |
| 4 | [General] Shear Reinforcement Items | `"SBAR_ITEMS"` | array [object] | - | **Required** |
| 4.1 | └ [General] Diagonal Reinforcement | `"OPT_DR"` | boolean | false | Optional |
| 4.2 | └ [When OPT_DR = true] [DR] Pitch · Minimum: 0 | `"DR_PITCH"` | number | - | **Required** |
| 4.3 | └ [When OPT_DR = true] [DR] Angle | `"DR_THETA"` | number | - | Optional |
| 4.4 | └ [When OPT_DR = true] [DR] Area · Minimum: 0 | `"DR_AW"` | number | - | **Required** |
| 4.5 | └ [When OPT_DR = true] Steel Bar for Web | `"OPT_SBW"` | boolean | false | Optional |
| 4.6 | └ [When OPT_SBW = true] [SBW] Pitch · Minimum: 0 | `"SBW_PITCH"` | number | - | **Required** |
| 4.7 | └ [When OPT_SBW = true] [SBW] Angle | `"SBW_ANGLE"` | number | - | Optional |
| 4.8 | └ [When OPT_SBW = true] [SBW] Area · Minimum: 0 | `"SBW_AP"` | number | - | **Required** |
| 4.9 | └ [When OPT_SBW = true] [SBW] Pre-force · Minimum: 0 | `"SBW_PS"` | number | - | **Required** |
| 4.10 | └ [When OPT_SBW = true] [SBW] Shear Reduction Factor · Minimum: 0 | `"SBW_FACTOR"` | number | - | **Required** |
| 4.11 | └ [When OPT_SBW = true] Torsional Reinforcement | `"OPT_TR"` | boolean | false | Optional |
| 4.12 | └ [When OPT_TR = true] [TR] Pitch · Minimum: 0 | `"TR_PITCH"` | number | - | **Required** |
| 4.13 | └ [When OPT_TR = true] [TR] Area (Web) · Minimum: 0 | `"TR_AWT"` | number | - | **Required** |
| 4.14 | └ [When OPT_TR = true] [TR] Area (Long.) · Minimum: 0 | `"TR_ALT"` | number | - | **Required** |
| 4.15 | └ [When OPT_TR = true] Stirrup | `"OPT_SR"` | boolean | false | Optional |
| 4.16 | └ [When OPT_SR = true] [SR] Pitch · Minimum: 0 | `"SR_PITCH"` | number | - | **Required** |
| 4.17 | └ [When OPT_SR = true] [SR] Area · Minimum: 0 | `"SR_AW"` | number | - | **Required** |
| 4.18 | └ [When OPT_SR = true] Enclosing Stirrup | `"OPT_LBAR_FLG"` | boolean | false | Optional |
| 4.19 | └ [When OPT_LBAR_FLG = true] Cover Thickness · Minimum: 0 | `"LBAR_THICK"` | number | - | **Required** |
| 4.20 | └ [When OPT_LBAR_FLG = true] Include Flange/Cantilever | `"LBAR_INC_FC"` | boolean | - | Optional |
| 5 | [General] Longitudinal Reinforcement | `"MBARS"` | array [object] | - | **Required** |
| 5.1 | └ [General] Longitudinal Rebar Items | `"MBAR_ITEMS"` | array [object] | - | Optional |
| 5.1.1 | 　　└ [General] Section Positions - I / J · I · J | `"IJ"` | string | - | **Required** |
| 5.1.2 | 　　└ [General] Bar Name | `"NAME"` | string | - | **Required** |
| 5.1.3 | 　　└ [General] Reference Y · Centroid: 0 · Left: 1 | `"REF_Y"` | integer | - | **Required** |
| 5.1.4 | 　　└ [General] Distance from Reference in Y direction | `"Y"` | number | 0 | Optional |
| 5.1.5 | 　　└ [General] Reference Z · Top: 0 · Bottom: 1 | `"REF_Z"` | integer | - | **Required** |
| 5.1.6 | 　　└ [General] Distance from Reference in Z Direction | `"Z"` | number | 0 | Optional |
| 5.1.7 | 　　└ [General] Number of Rebar · Minimum: 0 | `"NUM"` | integer | - | **Required** |
| 5.1.8 | 　　└ [General] Spacing · Minimum: 0 | `"SPACING"` | number | 0 | Optional |
| 5.1.9 | 　　└ [General] Part · 0 · 1 · 2 | `"PART"` | integer | - | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a virtual section ID (e.g., \"1\"). Available only when the model has virtual beams and its PSC design code supports virtual beams.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "RPSC Longitudinal Rebar",
          "type": "object",
          "description": "Section Manager - Reinforcements (longitudinal and shear reinforcement).",
          "required": [
            "OPT_MBAR_J",
            "OPT_SBAR_J",
            "SBAR_ITEMS",
            "MBARS"
          ],
          "additionalProperties": false,
          "properties": {
            "OPT_MBAR_J": {
              "type": "boolean",
              "description": "Same rebar data at I-end and J-end for longitudinal reinforcement."
            },
            "OPT_SBAR_J": {
              "type": "boolean",
              "description": "Same shear rebar data at I-end and J-end."
            },
            "OPT_CRACKED": {
              "type": "boolean",
              "description": "Cracked section option. Applies only to composite sections; when omitted the stored value is kept (false for a new record). Not returned by GET."
            },
            "SBAR_ITEMS": {
              "type": "array",
              "description": "Shear reinforcement data. Index 0: I-section, index 1: J-section (when OPT_SBAR_J is false).",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "OPT_DR": {
                    "type": "boolean",
                    "description": "Diagonal reinforcement.",
                    "default": false
                  },
                  "DR_PITCH": {
                    "type": "number",
                    "description": "[DR] Pitch."
                  },
                  "DR_THETA": {
                    "type": "number",
                    "description": "[DR] Angle."
                  },
                  "DR_AW": {
                    "type": "number",
                    "description": "[DR] Area."
                  },
                  "OPT_SBW": {
                    "type": "boolean",
                    "description": "Steel bar for web.",
                    "default": false
                  },
                  "SBW_PITCH": {
                    "type": "number",
                    "description": "[SBW] Pitch."
                  },
                  "SBW_ANGLE": {
                    "type": "number",
                    "description": "[SBW] Angle."
                  },
                  "SBW_AP": {
                    "type": "number",
                    "description": "[SBW] Area."
                  },
                  "SBW_PS": {
                    "type": "number",
                    "description": "[SBW] Pre-force."
                  },
                  "SBW_FACTOR": {
                    "type": "number",
                    "description": "[SBW] Shear reduction factor."
                  },
                  "OPT_TR": {
                    "type": "boolean",
                    "description": "Torsional reinforcement.",
                    "default": false
                  },
                  "TR_PITCH": {
                    "type": "number",
                    "description": "[TR] Pitch."
                  },
                  "TR_AWT": {
                    "type": "number",
                    "description": "[TR] Area (web)."
                  },
                  "TR_ALT": {
                    "type": "number",
                    "description": "[TR] Area (longitudinal)."
                  },
                  "OPT_SR": {
                    "type": "boolean",
                    "description": "Stirrup.",
                    "default": false
                  },
                  "SR_PITCH": {
                    "type": "number",
                    "description": "[SR] Pitch."
                  },
                  "SR_AW": {
                    "type": "number",
                    "description": "[SR] Area."
                  },
                  "OPT_LBAR_FLG": {
                    "type": "boolean",
                    "description": "Enclosing stirrup.",
                    "default": false
                  },
                  "LBAR_THICK": {
                    "type": "number",
                    "description": "Cover thickness for enclosed section area."
                  },
                  "LBAR_INC_FC": {
                    "type": "boolean",
                    "description": "Include flange/cantilever."
                  }
                }
              },
              "minItems": 1,
              "maxItems": 2
            },
            "MBARS": {
              "type": "array",
              "description": "Longitudinal reinforcement. Index 0: I-section, index 1: J-section (when OPT_MBAR_J is false). On PUT, [] or a group without MBAR_ITEMS ({}, the GET form) keeps the existing rebar of that section; {\"MBAR_ITEMS\": []} deletes it. For shear reinforcement only, send any of the three.",
              "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "MBAR_ITEMS": {
                    "type": "array",
                    "description": "Longitudinal reinforcement property details. Omit to keep the existing rebar of this section (PUT); [] deletes it.",
                    "items": {
                      "type": "object",
                      "required": [
                        "IJ",
                        "NAME",
                        "REF_Y",
                        "REF_Z",
                        "NUM",
                        "PART"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "IJ": {
                          "type": "string",
                          "description": "Section position.",
                          "enum": [
                            "I",
                            "J"
                          ]
                        },
                        "NAME": {
                          "type": "string",
                          "description": "Bar name. Must be a rebar name of the model's concrete rebar material code (e.g. D16); otherwise the request is rejected (400).",
                          "minLength": 1
                        },
                        "REF_Y": {
                          "type": "integer",
                          "description": "Reference Y. 0: centroid, 1: left.",
                          "enum": [
                            0,
                            1
                          ]
                        },
                        "Y": {
                          "type": "number",
                          "description": "Distance from reference in Y direction.",
                          "default": 0
                        },
                        "REF_Z": {
                          "type": "integer",
                          "description": "Reference Z. 0: top, 1: bottom.",
                          "enum": [
                            0,
                            1
                          ]
                        },
                        "Z": {
                          "type": "number",
                          "description": "Distance from reference in Z direction.",
                          "default": 0
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars.",
                          "minimum": 0
                        },
                        "SPACING": {
                          "type": "number",
                          "description": "Spacing between rebars.",
                          "default": 0,
                          "minimum": 0
                        },
                        "PART": {
                          "type": "integer",
                          "description": "Part. Allowed values depend on the section: non-composite 0, 1 or 2; concrete composite 1 or 2; steel composite 2.",
                          "enum": [
                            0,
                            1,
                            2
                          ]
                        }
                      }
                    },
                    "minItems": 0
                  }
                }
              },
              "minItems": 0,
              "maxItems": 2
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

- `RPSC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "201": {
      "OPT_MBAR_J": false,
      "OPT_SBAR_J": false,
      "OPT_CRACKED": true,
      "SBAR_ITEMS": [
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        },
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        }
      ],
      "MBARS": [
        {
          "MBAR_ITEMS": [
            {
              "IJ": "I",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.0,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 8,
              "SPACING": 0.1,
              "PART": 1
            },
            {
              "IJ": "I",
              "NAME": "#5",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.5,
              "NUM": 4,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "I",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.06,
              "NUM": 15,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
        },
        {
          "MBAR_ITEMS": [
            {
              "IJ": "J",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.0,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 8,
              "SPACING": 0.1,
              "PART": 1
            },
            {
              "IJ": "J",
              "NAME": "#5",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.5,
              "NUM": 4,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "J",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.06,
              "NUM": 15,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
        }
      ]
    }
  }
}
```

**Response**

```json
{
  "RPSC": {
    "201": {
      "OPT_MBAR_J": false,
      "OPT_SBAR_J": false,
      "OPT_CRACKED": true,
      "SBAR_ITEMS": [
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90.0,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90.0,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000.0,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        },
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90.0,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90.0,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000.0,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        }
      ],
      "MBARS": [
        {
          "MBAR_ITEMS": [
            {
              "IJ": "I",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.0,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 8,
              "SPACING": 0.1,
              "PART": 1
            },
            {
              "IJ": "I",
              "NAME": "#5",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.5,
              "NUM": 4,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "I",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.06,
              "NUM": 15,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
        },
        {
          "MBAR_ITEMS": [
            {
              "IJ": "J",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.0,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 8,
              "SPACING": 0.1,
              "PART": 1
            },
            {
              "IJ": "J",
              "NAME": "#5",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.5,
              "NUM": 4,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "J",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.06,
              "NUM": 15,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/RPSC-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "201": {
      "OPT_MBAR_J": false,
      "OPT_SBAR_J": false,
      "OPT_CRACKED": true,
      "SBAR_ITEMS": [
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        },
        {
          "OPT_DR": true,
          "DR_PITCH": 0.15,
          "DR_THETA": 90,
          "DR_AW": 0.000516,
          "OPT_SBW": true,
          "SBW_PITCH": 0.6,
          "SBW_ANGLE": 90,
          "SBW_AP": 0.00014,
          "SBW_PS": 1300000,
          "SBW_FACTOR": 0.5,
          "OPT_TR": true,
          "TR_PITCH": 0.2,
          "TR_AWT": 0.000129,
          "TR_ALT": 0.00258,
          "OPT_SR": true,
          "SR_PITCH": 0.3,
          "SR_AW": 0.000258,
          "OPT_LBAR_FLG": true,
          "LBAR_THICK": 0.25,
          "LBAR_INC_FC": true
        }
      ],
      "MBARS": [
        {
          "MBAR_ITEMS": [
            {
              "IJ": "I",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.0,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 8,
              "SPACING": 0.1,
              "PART": 1
            },
            {
              "IJ": "I",
              "NAME": "#5",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.5,
              "NUM": 4,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "I",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.06,
              "NUM": 15,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
        },
        {
          "MBAR_ITEMS": [
            {
              "IJ": "J",
              "NAME": "#8",
              "REF_Y": 0,
              "Y": 0.0,
              "REF_Z": 1,
              "Z": 0.08,
              "NUM": 8,
              "SPACING": 0.1,
              "PART": 1
            },
            {
              "IJ": "J",
              "NAME": "#5",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.5,
              "NUM": 4,
              "SPACING": 0.2,
              "PART": 1
            },
            {
              "IJ": "J",
              "NAME": "#6",
              "REF_Y": 1,
              "Y": 0.1,
              "REF_Z": 0,
              "Z": 0.06,
              "NUM": 15,
              "SPACING": 0.15,
              "PART": 2
            }
          ]
        }
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

## 27. `DIDP-VBEAM` — Design Position - Virtual Beam

> **기능** 가상보의 PSC 설계 위치를 지정합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/DIDP-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 58078226966169](https://support.midasuser.com/hc/en-us/articles/58078226966169)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings, where each entry represents a virtual beam (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Moment Type · None: 0 · I: 1 · J: 2 · I & J: 3 | `"MOMENT_TYPE"` | integer | - | **Required** |
| 2 | [General] Shear Type · None: 0 · I: 1 · J: 2 · I & J: 3 | `"SHEAR_TYPE"` | integer | - | **Required** |

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
      "description": "Object keyed by ID strings, where each entry represents a virtual beam (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "MOMENT_TYPE",
            "SHEAR_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "MOMENT_TYPE": {
              "type": "integer",
              "description": "Moment Type",
              "enum": [
                0,
                1,
                2,
                3
              ]
            },
            "SHEAR_TYPE": {
              "type": "integer",
              "description": "Shear Type",
              "enum": [
                0,
                1,
                2,
                3
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

- `DIDP`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "201": {
      "MOMENT_TYPE": 2,
      "SHEAR_TYPE": 1
    }
  }
}
```

**Response**

```json
{
  "DIDP": {
    "201": {
      "MOMENT_TYPE": 2,
      "SHEAR_TYPE": 1
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/DIDP-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "201": {
      "MOMENT_TYPE": 2,
      "SHEAR_TYPE": 1
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 28. `DIOP-VBEAM` — Output Position - Virtual Beam

> **기능** 가상보의 PSC 설계 결과 출력 위치를 지정합니다.

### Input URI

```
{base url}/DESIGN/PSC/AASHTO-LRFD24/DIOP-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 58094307410457](https://support.midasuser.com/hc/en-us/articles/58094307410457)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings, where each entry represents a virtual beam (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Moment Strength | `"MOMENT_STRENGTH"` | object | - | **Required** |
| 1.1 | └ [General] Positive Moment · None: 0 · I: 1 · J: 2 · I & J: 3 | `"POSITIVE_MOMENT"` | integer | - | **Required** |
| 1.2 | └ [General] Negative Moment · None: 0 · I: 1 · J: 2 · I & J: 3 | `"NEGATIVE_MOMENT"` | integer | - | **Required** |
| 2 | [General] Shear Type · None: 0 · I: 1 · J: 2 · I & J: 3 | `"SHEAR_TYPE"` | integer | - | **Required** |
| 3 | [General] Torsion Type · None: 0 · I: 1 · J: 2 · I & J: 3 | `"TORSION_TYPE"` | integer | - | **Required** |

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
      "description": "Object keyed by ID strings, where each entry represents a virtual beam (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "MOMENT_STRENGTH",
            "SHEAR_TYPE",
            "TORSION_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "MOMENT_STRENGTH": {
              "type": "object",
              "description": "Moment Strength",
              "additionalProperties": false,
              "required": [
                "POSITIVE_MOMENT",
                "NEGATIVE_MOMENT"
              ],
              "properties": {
                "POSITIVE_MOMENT": {
                  "type": "integer",
                  "description": "Positive Moment",
                  "enum": [
                    0,
                    1,
                    2,
                    3
                  ]
                },
                "NEGATIVE_MOMENT": {
                  "type": "integer",
                  "description": "Negative Moment",
                  "enum": [
                    0,
                    1,
                    2,
                    3
                  ]
                }
              }
            },
            "SHEAR_TYPE": {
              "type": "integer",
              "description": "Shear Type",
              "enum": [
                0,
                1,
                2,
                3
              ]
            },
            "TORSION_TYPE": {
              "type": "integer",
              "description": "Torsion Type",
              "enum": [
                0,
                1,
                2,
                3
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

- `DIOP`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "46": {
      "SHEAR_TYPE": 0,
      "TORSION_TYPE": 0,
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      }
    }
  }
}
```

**Response**

```json
{
  "DIOP": {
    "46": {
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      },
      "SHEAR_TYPE": 0,
      "TORSION_TYPE": 0
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
URI = f"{BASE_URL}/DESIGN/PSC/AASHTO-LRFD24/DIOP-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "46": {
      "SHEAR_TYPE": 0,
      "TORSION_TYPE": 0,
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      }
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```
