# 30. Rating – PSC AASHTO-LRFR19 (교량 프리스트레스트 콘크리트 내하력 평가)

> **예제 Base URL (MIDAS Civil NX)** `https://moa-engineers.midasit.com:443/civil`  
> **인증 헤더** `MAPI-Key: <발급된 키>`  
> **공식 하위 목차** [AASHTO-LRFR19 PSC 평가](https://support.midasuser.com/hc/en-us/articles/64738444883737)

PSC 교량의 평가 기준과 평가 케이스 설정, 내하력 평가 실행, 결과 표 및 보고서를 다룹니다.
고유 URI **23개**와 본문 **34절**을 다룹니다.
공통 URI 접두사는 `{base url}/RATING/PSC/AASHTO-LRFR19/<CODE>`입니다.
기준 선택에는 `{base url}/RATING/PSC/DSRPSC`를 사용합니다.
공용 `TABLE` URI의 12개 결과 절은 `TABLE_TYPE`으로 구분합니다.

---

## Endpoint 목록 (34개 절)

| No. | Endpoint | 기능 | Active Methods |
| --- | --- | --- | --- |
| 0 | [`DSRPSC`](#0-dsrpsc--rating-code) | PSC 내하력 평가에 적용할 기준을 선택합니다. | GET · PUT · DELETE |
| 1 | [`RCO`](#1-rco--rating-code-option) | 평가 기준과 평가 옵션을 설정합니다. | GET · PUT · DELETE |
| 2 | [`DCTL`](#2-dctl--definition-of-frame) | 평가 대상 프레임의 조건을 설정합니다. | GET · PUT · DELETE |
| 3 | [`MEMB`](#3-memb--member-assignment) | 평가 대상 요소를 부재로 배정합니다. | POST · GET · PUT · DELETE |
| 4 | [`OPE_MEMB`](#4-ope_memb--auto-member-assignment) | 평가 대상 요소의 부재 배정을 자동으로 수행합니다. | POST |
| 5 | [`LENG`](#5-leng--unbraced-lengthllb) | 부재의 비지지 길이 L과 Lb를 설정합니다. | POST · GET · PUT · DELETE |
| 6 | [`SPLT`](#6-splt--span-length) | 부재의 지간 길이를 설정합니다. | POST · GET · PUT · DELETE |
| 7 | [`KFAC`](#7-kfac--effective-length-factor-k) | 부재의 유효길이계수 K를 설정합니다. | POST · GET · PUT · DELETE |
| 8 | [`LTSR`](#8-ltsr--limiting-slenderness-ratio) | 부재의 세장비 한계를 설정합니다. | POST · GET · PUT · DELETE |
| 9 | [`RPSC`](#9-rpsc--reinforcement-information) | 평가에 사용할 철근 보강 정보를 입력합니다. | POST · GET · DELETE · PUT |
| 10 | [`DATR`](#10-datr--diagnostic-test-result) | 내하력 평가에 사용할 진단 시험 결과를 입력합니다. | POST · GET · PUT · DELETE |
| 11 | [`MATD`](#11-matd--modify-material) | 평가에 사용할 콘크리트 및 철근 재료를 수정합니다. | GET · PUT · DELETE |
| 12 | [`DFRC`](#12-dfrc--define-rating-case) | 평가 케이스를 정의합니다. | POST · GET · PUT · DELETE |
| 13 | [`RTGS`](#13-rtgs--rating-group-setting) | 평가 그룹을 설정합니다. | POST · GET · PUT · DELETE |
| 14 | [`PFRO`](#14-pfro--position-for-rating-output) | 평가 결과를 출력할 위치를 지정합니다. | POST · GET · PUT · DELETE |
| 15 | [`RPSC-ANAL`](#15-rpsc-anal--perform-rating) | PSC 내하력 평가를 실행합니다. | POST |
| 16 | [`TABLE` · `PSC_RATING_SVC_SUM_DGN`, `PSC_RATING_SVC_SUM_LEG`, `PSC_RATING_SVC_SUM_DGN_VBEAM`, `PSC_RATING_SVC_SUM_LEG_VBEAM`](#16-table--psc_rating_svc_sum_dgn--service-limit-state-summary-design-live-legal) | 설계 활하중 및 법정하중의 사용한계상태 평가 요약을 조회합니다. | POST |
| 17 | [`TABLE` · `PSC_RATING_SVC_SUM_PER`, `PSC_RATING_SVC_SUM_PER_VBEAM`](#17-table--psc_rating_svc_sum_per--service-limit-state-summary-permit) | 허가하중의 사용한계상태 평가 요약을 조회합니다. | POST |
| 18 | [`TABLE` · `PSC_RATING_STR_SUM_FLEX`, `PSC_RATING_STR_SUM_FLEX_VBEAM`](#18-table--psc_rating_str_sum_flex--strength-limit-state-summary-flexural) | 휨에 대한 강도한계상태 평가 요약을 조회합니다. | POST |
| 19 | [`TABLE` · `PSC_RATING_STR_SUM_SHEAR`, `PSC_RATING_STR_SUM_SHEAR_VBEAM`](#19-table--psc_rating_str_sum_shear--strength-limit-state-summary-shear) | 전단에 대한 강도한계상태 평가 요약을 조회합니다. | POST |
| 20 | [`TABLE` · `PSC_RATING_STRESS_DGN`, `PSC_RATING_STRESS_LEG`, `PSC_RATING_STRESS_DGN_VBEAM`, `PSC_RATING_STRESS_LEG_VBEAM`](#20-table--psc_rating_stress_dgn--stress-rating-factordesign-live-legal) | 설계 활하중 및 법정하중의 응력 평가계수를 조회합니다. | POST |
| 21 | [`TABLE` · `PSC_RATING_STRESS_PER`, `PSC_RATING_STRESS_PER_VBEAM`](#21-table--psc_rating_stress_per--stress-rating-factorpermit) | 허가하중의 응력 평가계수를 조회합니다. | POST |
| 22 | [`TABLE` · `PSC_RATING_FLEXURE`, `PSC_RATING_FLEXURE_VBEAM`](#22-table--psc_rating_flexure--flexural-strength-rating-factor) | 휨강도 평가계수를 조회합니다. | POST |
| 23 | [`TABLE` · `PSC_RATING_SHEAR`, `PSC_RATING_SHEAR_VBEAM`](#23-table--psc_rating_shear--shear-strength-rating-factor) | 전단강도 평가계수를 조회합니다. | POST |
| 24 | [`TABLE` · `PSC_RATING_STRESS_DETAIL_DGN`, `PSC_RATING_STRESS_DETAIL_LEG`, `PSC_RATING_STRESS_DETAIL_DGN_VBEAM`, `PSC_RATING_STRESS_DETAIL_LEG_VBEAM`](#24-table--psc_rating_stress_detail_dgn--stress-rating-detaildesign-live-legal) | 설계 활하중 및 법정하중의 응력 평가 상세 결과를 조회합니다. | POST |
| 25 | [`TABLE` · `PSC_RATING_STRESS_DETAIL_PER`, `PSC_RATING_STRESS_DETAIL_PER_VBEAM`](#25-table--psc_rating_stress_detail_per--stress-rating-detailpermit) | 허가하중의 응력 평가 상세 결과를 조회합니다. | POST |
| 26 | [`TABLE` · `PSC_RATING_FLEXURE_DETAIL`, `PSC_RATING_FLEXURE_DETAIL_VBEAM`](#26-table--psc_rating_flexure_detail--flexural-strength-rating-detail) | 휨강도 평가 상세 결과를 조회합니다. | POST |
| 27 | [`TABLE` · `PSC_RATING_SHEAR_DETAIL`, `PSC_RATING_SHEAR_DETAIL_VBEAM`](#27-table--psc_rating_shear_detail--shear-strength-rating-detail) | 전단강도 평가 상세 결과를 조회합니다. | POST |
| 28 | [`REPORT`](#28-report--rating-result-report) | 내하력 평가 결과를 보고서로 내보냅니다. | POST |
| 29 | [`LENG-VBEAM`](#29-leng-vbeam--unbraced-lengthllb---virtual-beam) | 가상보의 비지지 길이 L과 Lb를 설정합니다. | POST · GET · PUT · DELETE |
| 30 | [`SPLT-VBEAM`](#30-splt-vbeam--span-length---virtual-beam) | 가상보의 지간 길이를 설정합니다. | POST · GET · PUT · DELETE |
| 31 | [`RPSC-VBEAM`](#31-rpsc-vbeam--reinforcement-information---virtual-beam) | 가상보 평가에 사용할 철근 보강 정보를 입력합니다. | POST · GET · PUT · DELETE |
| 32 | [`DATR-VBEAM`](#32-datr-vbeam--diagnostic-test-result---virtual-beam) | 가상보 평가에 사용할 진단 시험 결과를 입력합니다. | POST · GET · PUT · DELETE |
| 33 | [`PFRO-VBEAM`](#33-pfro-vbeam--position-for-rating-output---virtual-beam) | 가상보 평가 결과를 출력할 위치를 지정합니다. | POST · GET · PUT · DELETE |

---

## 0. `DSRPSC` — Rating Code

> **기능** PSC 내하력 평가에 적용할 기준을 선택합니다.

### Input URI

```
{base url}/RATING/PSC/DSRPSC
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738316306713](https://support.midasuser.com/hc/en-us/articles/64738316306713)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). The key must be "1" (single record). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] PSC Rating Code · AASHTO-LRFR19 | `"DGNCODE"` | string | - | **Required** |

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
      "description": "Keyed object (dictionary). The key must be \"1\" (single record).",
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
              "description": "PSC Rating Code",
              "enum": [
                "AASHTO-LRFR19"
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

- `DSRPSC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "AASHTO-LRFR19"
    }
  }
}
```

**Response**

```json
{
  "DSRPSC": {
    "1": {
      "DGNCODE": "AASHTO-LRFR19"
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
URI = f"{BASE_URL}/RATING/PSC/DSRPSC"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "DGNCODE": "AASHTO-LRFR19"
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 1. `RCO` — Rating Code Option

> **기능** 평가 기준과 평가 옵션을 설정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/RCO
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738346390041](https://support.midasuser.com/hc/en-us/articles/64738346390041)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). The key must be "1" (single record). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Strength Limit State Flexure | `"SLS_FLEX"` | boolean | true | Optional |
| 2 | [General] Nominal Flexural Resistance Type · Code: 0 · Strain Compatibility: 1 | `"NOMINAL_FLEX_RESIST"` | integer | 0 | Optional |
| 3 | [General] Strength Limit State Shear | `"SLS_SHEAR"` | boolean | true | Optional |
| 4 | [General] Strength Limit State Shear Type · Non-Segmental Bridge: 0 · Segmental Bridge: 1 | `"SLS_SHEAR_TYPE"` | integer | 0 | Optional |
| 5 | [General] Design Load Stress | `"DESIGN_LOAD_STRESS"` | boolean | true | Optional |
| 6 | [General] Compressive Stress - Design Load | `"COMP_STRESS_DESIGN"` | number | 0 | Optional |
| 7 | [General] Tensile Stress - Design Load | `"TENSILE_STRESS_DESIGN"` | number | 0 | Optional |
| 8 | [General] Stress for Composite Section(Slab) - Design Load | `"STRESS_COMPSITE_SECTION_DESIGN"` | boolean | false | Optional |
| 9 | [General] Compressive Stress (Slab) - Design Load | `"COMP_STRESS_SLAB_DESIGN"` | number | 0 | Optional |
| 10 | [General] Tensile Stress (Slab) - Design Load | `"TENSILE_STRESS_SLAB_DESIGN"` | number | 0 | Optional |
| 11 | [General] Legal Load Stress | `"LEGAL_LOAD_STRESS"` | boolean | true | Optional |
| 12 | [General] Compressive Stress - Legal Load | `"COMP_STRESS_LEGAL"` | number | 0 | Optional |
| 13 | [General] Tensile Stress - Legal Load | `"TENSILE_STRESS_LEGAL"` | number | 0 | Optional |
| 14 | [General] Stress for Composite Section(Slab) - Legal Load | `"STRESS_COMPSITE_SECTION_LEGAL"` | boolean | false | Optional |
| 15 | [General] Compressive Stress (Slab) - Legal Load | `"COMP_STRESS_SLAB_LEGAL"` | number | 0 | Optional |
| 16 | [General] Tensile Stress (Slab) - Legal Load | `"TENSILE_STRESS_SLAB_LEGAL"` | number | 0 | Optional |
| 17 | [General] Permit Load Stress | `"PERMIT_LOAD_STRESS"` | boolean | true | Optional |
| 18 | [General] Prestressing Steel Stress - Permit Load | `"PRESTRESSING_STEEL"` | number | 0 | Optional |
| 19 | [General] Reinforcement Stress - Permit Load | `"REINFORCEMENT"` | number | 0 | Optional |
| 20 | [General] Load Test Measurement · Strain: 0 · Displacement: 1 | `"LOAD_TEST_MEASUREMENT"` | integer | 0 | Optional |
| 21 | [General] System Factor · Minimum: 0 | `"SYSTEM_FACTOR"` | number | 1 | Optional |

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
      "description": "Keyed object (dictionary). The key must be \"1\" (single record).",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "patternProperties": {
        "^1$": {
          "title": "PSC Rating Code Option",
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "SLS_FLEX": {
              "type": "boolean",
              "description": "Strength Limit State Flexure",
              "default": true
            },
            "NOMINAL_FLEX_RESIST": {
              "type": "integer",
              "description": "Nominal Flexural Resistance",
              "enum": [
                0,
                1
              ],
              "default": 0
            },
            "SLS_SHEAR": {
              "type": "boolean",
              "description": "Strength Limit State Shear",
              "default": true
            },
            "SLS_SHEAR_TYPE": {
              "type": "integer",
              "description": "Strength Limit State Shear Type",
              "enum": [
                0,
                1
              ],
              "default": 0
            },
            "DESIGN_LOAD_STRESS": {
              "type": "boolean",
              "description": "Design Load Stress",
              "default": true
            },
            "COMP_STRESS_DESIGN": {
              "type": "number",
              "description": "Compressive Stress - Design Load",
              "default": 0
            },
            "TENSILE_STRESS_DESIGN": {
              "type": "number",
              "description": "Tensile Stress - Design Load",
              "default": 0
            },
            "STRESS_COMPSITE_SECTION_DESIGN": {
              "type": "boolean",
              "description": "Stress for Composite Section(Slab) - Design Load",
              "default": false
            },
            "COMP_STRESS_SLAB_DESIGN": {
              "type": "number",
              "description": "Compressive Stress (Slab) - Design Load",
              "default": 0
            },
            "TENSILE_STRESS_SLAB_DESIGN": {
              "type": "number",
              "description": "Tensile Stress (Slab) - Design Load",
              "default": 0
            },
            "LEGAL_LOAD_STRESS": {
              "type": "boolean",
              "description": "Legal Load Stress",
              "default": true
            },
            "COMP_STRESS_LEGAL": {
              "type": "number",
              "description": "Compressive Stress - Legal Load",
              "default": 0
            },
            "TENSILE_STRESS_LEGAL": {
              "type": "number",
              "description": "Tensile Stress - Legal Load",
              "default": 0
            },
            "STRESS_COMPSITE_SECTION_LEGAL": {
              "type": "boolean",
              "description": "Stress for Composite Section(Slab) - Legal Load",
              "default": false
            },
            "COMP_STRESS_SLAB_LEGAL": {
              "type": "number",
              "description": "Compressive Stress (Slab) - Legal Load",
              "default": 0
            },
            "TENSILE_STRESS_SLAB_LEGAL": {
              "type": "number",
              "description": "Tensile Stress (Slab) - Legal Load",
              "default": 0
            },
            "PERMIT_LOAD_STRESS": {
              "type": "boolean",
              "description": "Permit Load Stress",
              "default": true
            },
            "PRESTRESSING_STEEL": {
              "type": "number",
              "description": "Prestressing Steel Stress - Permit Load",
              "default": 0
            },
            "REINFORCEMENT": {
              "type": "number",
              "description": "Reinforcement Stress - Permit Load",
              "default": 0
            },
            "LOAD_TEST_MEASUREMENT": {
              "type": "integer",
              "description": "Load Test Measurement",
              "enum": [
                0,
                1
              ],
              "default": 0
            },
            "SYSTEM_FACTOR": {
              "type": "number",
              "description": "System Factor",
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

- `RCO`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "SLS_FLEX": true,
      "NOMINAL_FLEX_RESIST": 1,
      "SLS_SHEAR": true,
      "SLS_SHEAR_TYPE": 1,
      "DESIGN_LOAD_STRESS": true,
      "COMP_STRESS_DESIGN": 16547423,
      "TENSILE_STRESS_DESIGN": 3102641,
      "STRESS_COMPSITE_SECTION_DESIGN": true,
      "COMP_STRESS_SLAB_DESIGN": 12410567,
      "TENSILE_STRESS_SLAB_DESIGN": 2068428,
      "LEGAL_LOAD_STRESS": true,
      "COMP_STRESS_LEGAL": 16547423,
      "TENSILE_STRESS_LEGAL": 3102641,
      "STRESS_COMPSITE_SECTION_LEGAL": true,
      "COMP_STRESS_SLAB_LEGAL": 12410567,
      "TENSILE_STRESS_SLAB_LEGAL": 2068428,
      "PERMIT_LOAD_STRESS": true,
      "PRESTRESSING_STEEL": 1675000000,
      "REINFORCEMENT": 330000000,
      "LOAD_TEST_MEASUREMENT": 0,
      "SYSTEM_FACTOR": 1.0
    }
  }
}
```

**Response**

```json
{
  "RCO": {
    "1": {
      "SLS_FLEX": true,
      "NOMINAL_FLEX_RESIST": 1,
      "SLS_SHEAR": true,
      "SLS_SHEAR_TYPE": 1,
      "DESIGN_LOAD_STRESS": true,
      "COMP_STRESS_DESIGN": 16547423.0,
      "TENSILE_STRESS_DESIGN": 3102641.0,
      "STRESS_COMPSITE_SECTION_DESIGN": true,
      "COMP_STRESS_SLAB_DESIGN": 12410567.0,
      "TENSILE_STRESS_SLAB_DESIGN": 2068428.0,
      "LEGAL_LOAD_STRESS": true,
      "COMP_STRESS_LEGAL": 16547423.0,
      "TENSILE_STRESS_LEGAL": 3102641.0,
      "STRESS_COMPSITE_SECTION_LEGAL": true,
      "COMP_STRESS_SLAB_LEGAL": 12410567.0,
      "TENSILE_STRESS_SLAB_LEGAL": 2068428.0,
      "PERMIT_LOAD_STRESS": true,
      "PRESTRESSING_STEEL": 1675000000.0,
      "REINFORCEMENT": 330000000.0,
      "LOAD_TEST_MEASUREMENT": 0,
      "SYSTEM_FACTOR": 1.0
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/RCO"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "SLS_FLEX": true,
      "NOMINAL_FLEX_RESIST": 1,
      "SLS_SHEAR": true,
      "SLS_SHEAR_TYPE": 1,
      "DESIGN_LOAD_STRESS": true,
      "COMP_STRESS_DESIGN": 16547423,
      "TENSILE_STRESS_DESIGN": 3102641,
      "STRESS_COMPSITE_SECTION_DESIGN": true,
      "COMP_STRESS_SLAB_DESIGN": 12410567,
      "TENSILE_STRESS_SLAB_DESIGN": 2068428,
      "LEGAL_LOAD_STRESS": true,
      "COMP_STRESS_LEGAL": 16547423,
      "TENSILE_STRESS_LEGAL": 3102641,
      "STRESS_COMPSITE_SECTION_LEGAL": true,
      "COMP_STRESS_SLAB_LEGAL": 12410567,
      "TENSILE_STRESS_SLAB_LEGAL": 2068428,
      "PERMIT_LOAD_STRESS": true,
      "PRESTRESSING_STEEL": 1675000000,
      "REINFORCEMENT": 330000000,
      "LOAD_TEST_MEASUREMENT": 0,
      "SYSTEM_FACTOR": 1.0
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

> **기능** 평가 대상 프레임의 조건을 설정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/DCTL
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738342143513](https://support.midasuser.com/hc/en-us/articles/64738342143513)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). The key must be "1" (single record). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] X-Direction of Frame · Unbraced \| Sway: "Unbraced Sway" · Braced \| Non-sway: "Braced Non-sway" | `"FRAMEX"` | string | Braced Non-sway | Optional |
| 2 | [General] Y-Direction of Frame · Unbraced \| Sway: "Unbraced Sway" · Braced \| Non-sway: "Braced Non-sway" | `"FRAMEY"` | string | Braced Non-sway | Optional |
| 3 | [General] Auto Calculate Effective Length Factor | `"bAUTOKF"` | boolean | false | Optional |
| 4 | [General] Design Type · 3-D: "3D" · X-Z Plane: "XZ" · Y-Z Plane: "YZ" · X-Y Plane: "XY" | `"DT"` | string | 3D | Optional |

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "description": "Definition of Frame (shared structure: T_DCTL_D). Supported methods: GET, PUT, DELETE.",
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). The key must be \"1\" (single record).",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "patternProperties": {
        "^1$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "FRAMEX": {
              "type": "string",
              "description": "X-Direction of Frame",
              "default": "Braced Non-sway",
              "enum": [
                "Unbraced Sway",
                "Braced Non-sway"
              ]
            },
            "FRAMEY": {
              "type": "string",
              "description": "Y-Direction of Frame",
              "default": "Braced Non-sway",
              "enum": [
                "Unbraced Sway",
                "Braced Non-sway"
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
              "enum": [
                "3D",
                "XZ",
                "YZ",
                "XY"
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

- `DCTL`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "FRAMEX": "Unbraced Sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": true,
      "DT": "3D"
    }
  }
}
```

**Response**

```json
{
  "DCTL": {
    "1": {
      "FRAMEX": "Unbraced Sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": true,
      "DT": "3D"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/DCTL"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "FRAMEX": "Unbraced Sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": true,
      "DT": "3D"
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 3. `MEMB` — Member Assignment

> **기능** 평가 대상 요소를 부재로 배정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/MEMB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738326098585](https://support.midasuser.com/hc/en-us/articles/64738326098585)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a member ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Element Lists. Elements must be connected and must not belong to another member. | `"AELEM"` | array | - | **Required** |
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
      "description": "Keyed object (dictionary). Each property name is a member ID string (e.g., \"1\").",
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
              "description": "Element Lists. Elements must be connected and must not belong to another member.",
              "minItems": 1,
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
        1,
        2,
        3,
        4,
        5,
        6,
        7
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        8,
        9,
        10,
        11,
        12,
        13,
        14
      ],
      "bREVERSE": true
    },
    "3": {
      "AELEM": [
        15,
        16,
        17,
        18,
        19,
        20,
        21
      ],
      "bREVERSE": false
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
        1,
        2,
        3,
        4,
        5,
        6,
        7
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        8,
        9,
        10,
        11,
        12,
        13,
        14
      ],
      "bREVERSE": true
    },
    "3": {
      "AELEM": [
        15,
        16,
        17,
        18,
        19,
        20,
        21
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/MEMB"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "AELEM": [
        1,
        2,
        3,
        4,
        5,
        6,
        7
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        8,
        9,
        10,
        11,
        12,
        13,
        14
      ],
      "bREVERSE": true
    },
    "3": {
      "AELEM": [
        15,
        16,
        17,
        18,
        19,
        20,
        21
      ],
      "bREVERSE": false
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 4. `OPE_MEMB` — Auto Member Assignment

> **기능** 평가 대상 요소의 부재 배정을 자동으로 수행합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/OPE_MEMB
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738333001241](https://support.midasuser.com/hc/en-us/articles/64738333001241)

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
  "description": "Member Assignment (Add/Replace) request schema (POST /RATING/PSC/AASHTO-LRFR19/OPE_MEMB)",
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
    "ALLOW_SINGLE": true
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
      3,
      4,
      5
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
        3,
        4,
        5
      ],
      "bREVERSE": true
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/OPE_MEMB"

payload = json.loads(r'''
{
  "Argument": {
    "ASSIGN_TYPE": "AUTO",
    "SELECTION_TYPE": "SELECTION",
    "ELEM_LIST": [
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
    "ALLOW_SINGLE": true
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 5. `LENG` — Unbraced Length(L,Lb)

> **기능** 부재의 비지지 길이 L과 Lb를 설정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/LENG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738317990681](https://support.midasuser.com/hc/en-us/articles/64738317990681)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element number (e.g., "1"). The element must exist in the model. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Unbraced Length Ly · Minimum: 0 | `"LY"` | number | 0 | Optional |
| 2 | [General] Unbraced Length Lz · Minimum: 0 | `"LZ"` | number | 0 | Optional |
| 3 | [General] Laterally Unbraced Length. Used only when bNOTUSE is false. · Minimum: 0 | `"LB"` | number | 0 | Optional |
| 4 | [General] Do not consider of laterally unbraced length | `"bNOTUSE"` | boolean | false | Optional |

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
      "description": "Keyed object (dictionary). Each property name is an element number (e.g., \"1\"). The element must exist in the model.",
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
              "default": 0,
              "minimum": 0
            },
            "LZ": {
              "type": "number",
              "description": "Unbraced Length Lz",
              "default": 0,
              "minimum": 0
            },
            "LB": {
              "type": "number",
              "description": "Laterally Unbraced Length. Used only when bNOTUSE is false.",
              "default": 0,
              "minimum": 0
            },
            "bNOTUSE": {
              "type": "boolean",
              "description": "Do not consider of laterally unbraced length",
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

- `LENG`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "2": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "3": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "4": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "5": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "6": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "7": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": true
    }
  }
}
```

**Response**

```json
{
  "LENG": {
    "1": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "2": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "3": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "4": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "5": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "6": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "7": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": true
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/LENG"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "2": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "3": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "4": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "5": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "6": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": false
    },
    "7": {
      "LY": 4.5,
      "LZ": 4.5,
      "LB": 9.0,
      "bNOTUSE": true
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 6. `SPLT` — Span Length

> **기능** 부재의 지간 길이를 설정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/SPLT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738318269209](https://support.midasuser.com/hc/en-us/articles/64738318269209)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element number (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Span Length · Minimum: 0 | `"SPAN_LENGTH"` | number | 0 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is an element number (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "SPAN_LENGTH": {
              "type": "number",
              "description": "Span Length",
              "default": 0,
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

- `SPLT`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "SPAN_LENGTH": 30.0
    },
    "2": {
      "SPAN_LENGTH": 30.0
    },
    "3": {
      "SPAN_LENGTH": 30.0
    },
    "4": {
      "SPAN_LENGTH": 30.0
    },
    "5": {
      "SPAN_LENGTH": 30.0
    },
    "6": {
      "SPAN_LENGTH": 30.0
    },
    "7": {
      "SPAN_LENGTH": 30.0
    }
  }
}
```

**Response**

```json
{
  "SPLT": {
    "1": {
      "SPAN_LENGTH": 30.0
    },
    "2": {
      "SPAN_LENGTH": 30.0
    },
    "3": {
      "SPAN_LENGTH": 30.0
    },
    "4": {
      "SPAN_LENGTH": 30.0
    },
    "5": {
      "SPAN_LENGTH": 30.0
    },
    "6": {
      "SPAN_LENGTH": 30.0
    },
    "7": {
      "SPAN_LENGTH": 30.0
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/SPLT"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "SPAN_LENGTH": 30.0
    },
    "2": {
      "SPAN_LENGTH": 30.0
    },
    "3": {
      "SPAN_LENGTH": 30.0
    },
    "4": {
      "SPAN_LENGTH": 30.0
    },
    "5": {
      "SPAN_LENGTH": 30.0
    },
    "6": {
      "SPAN_LENGTH": 30.0
    },
    "7": {
      "SPAN_LENGTH": 30.0
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 7. `KFAC` — Effective Length Factor (K)

> **기능** 부재의 유효길이계수 K를 설정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/KFAC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738333862297](https://support.midasuser.com/hc/en-us/articles/64738333862297)

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
              "description": "Ky",
              "default": 1,
              "exclusiveMinimum": 0
            },
            "Kz": {
              "type": "number",
              "description": "Kz",
              "default": 1,
              "exclusiveMinimum": 0
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

- `KFAC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "Ky": 1.0,
      "Kz": 1.2
    },
    "2": {
      "Ky": 0.8,
      "Kz": 1.0
    },
    "3": {
      "Ky": 1.0,
      "Kz": 1.2
    },
    "4": {
      "Ky": 0.8,
      "Kz": 1.0
    },
    "5": {
      "Ky": 1.0,
      "Kz": 1.2
    },
    "6": {
      "Ky": 0.8,
      "Kz": 1.0
    },
    "7": {
      "Ky": 1.0,
      "Kz": 1.2
    }
  }
}
```

**Response**

```json
{
  "KFAC": {
    "1": {
      "Ky": 1.0,
      "Kz": 1.2
    },
    "2": {
      "Ky": 0.8,
      "Kz": 1.0
    },
    "3": {
      "Ky": 1.0,
      "Kz": 1.2
    },
    "4": {
      "Ky": 0.8,
      "Kz": 1.0
    },
    "5": {
      "Ky": 1.0,
      "Kz": 1.2
    },
    "6": {
      "Ky": 0.8,
      "Kz": 1.0
    },
    "7": {
      "Ky": 1.0,
      "Kz": 1.2
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/KFAC"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "Ky": 1.0,
      "Kz": 1.2
    },
    "2": {
      "Ky": 0.8,
      "Kz": 1.0
    },
    "3": {
      "Ky": 1.0,
      "Kz": 1.2
    },
    "4": {
      "Ky": 0.8,
      "Kz": 1.0
    },
    "5": {
      "Ky": 1.0,
      "Kz": 1.2
    },
    "6": {
      "Ky": 0.8,
      "Kz": 1.0
    },
    "7": {
      "Ky": 1.0,
      "Kz": 1.2
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 8. `LTSR` — Limiting Slenderness Ratio

> **기능** 부재의 세장비 한계를 설정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/LTSR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738369226009](https://support.midasuser.com/hc/en-us/articles/64738369226009)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Object keyed by ID strings (e.g., "1"), where each entry represents an element. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Do not check for Slenderness Ratio | `"bNOTCHECK"` | boolean | false | Optional |
| 2 | [General] Limiting Slenderness Ratio for Compression. Used only when bNOTCHECK is false. · Minimum: 0 | `"COMP"` | number | 200 | Optional |
| 3 | [General] Limiting Slenderness Ratio for Tension. Used only when bNOTCHECK is false. · Minimum: 0 | `"TENS"` | number | 300 | Optional |

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
            "bNOTCHECK": {
              "type": "boolean",
              "description": "Do not check for Slenderness Ratio",
              "default": false
            },
            "COMP": {
              "type": "number",
              "description": "Limiting Slenderness Ratio for Compression. Used only when bNOTCHECK is false.",
              "default": 200,
              "exclusiveMinimum": 0
            },
            "TENS": {
              "type": "number",
              "description": "Limiting Slenderness Ratio for Tension. Used only when bNOTCHECK is false.",
              "default": 300,
              "exclusiveMinimum": 0
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

- `PSCLTSR`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "2": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "3": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "4": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "5": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "6": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "7": {
      "bNOTCHECK": true,
      "COMP": 120,
      "TENS": 240
    }
  }
}
```

**Response**

```json
{
  "PSCLTSR": {
    "1": {
      "bNOTCHECK": false,
      "COMP": 120.0,
      "TENS": 240.0
    },
    "2": {
      "bNOTCHECK": false,
      "COMP": 120.0,
      "TENS": 240.0
    },
    "3": {
      "bNOTCHECK": false,
      "COMP": 120.0,
      "TENS": 240.0
    },
    "4": {
      "bNOTCHECK": false,
      "COMP": 120.0,
      "TENS": 240.0
    },
    "5": {
      "bNOTCHECK": false,
      "COMP": 120.0,
      "TENS": 240.0
    },
    "6": {
      "bNOTCHECK": false,
      "COMP": 120.0,
      "TENS": 240.0
    },
    "7": {
      "bNOTCHECK": true,
      "COMP": 120.0,
      "TENS": 240.0
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/LTSR"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "2": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "3": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "4": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "5": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "6": {
      "bNOTCHECK": false,
      "COMP": 120,
      "TENS": 240
    },
    "7": {
      "bNOTCHECK": true,
      "COMP": 120,
      "TENS": 240
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 9. `RPSC` — Reinforcement Information

> **기능** 평가에 사용할 철근 보강 정보를 입력합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/RPSC
```

### Active Methods

`POST` · `GET` · `DELETE` · `PUT`

### Specifications

**원문** [영문 64738361256985](https://support.midasuser.com/hc/en-us/articles/64738361256985)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a section ID (e.g., "1"). The section must be a PSC or composite section. | `"Assign"` | object | - | **Required** |

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
| 4.15 | └ [When OPT_TR = true] Stirrup Exists | `"OPT_SR"` | boolean | false | Optional |
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
      "description": "Keyed object (dictionary). Each property name is a section ID (e.g., \"1\"). The section must be a PSC or composite section.",
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
              "description": "Cracked section option. Applies only to composite sections; when omitted the stored value is kept (false for a new record)."
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
                    "description": "Stirrup exists.",
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
    "11": {
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
    },
    "12": {
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
    "11": {
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
    },
    "12": {
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/RPSC"

payload = json.loads(r'''
{
  "Assign": {
    "11": {
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
    },
    "12": {
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

## 10. `DATR` — Diagnostic Test Result

> **기능** 내하력 평가에 사용할 진단 시험 결과를 입력합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/DATR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738334701593](https://support.midasuser.com/hc/en-us/articles/64738334701593)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element number (e.g., "1"). The element must exist in the model. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Position Type · I: 0 · J: 1 · I & J: 2 | `"POSITION"` | integer | 0 | **Required** |
| 2 | [General] Load Test Measurement Type · Auto Calculation: 0 · User Input: 1 | `"LTM_TYPE"` | integer | 0 | **Required** |
| 3 | [General] Strain(I) | `"STRAIN_I"` | number | 1e-05 | Optional |
| 4 | [General] Strain(J) | `"STRAIN_J"` | number | 1e-05 | Optional |
| 5 | [General] Kb | `"KB"` | number | 1 | Optional |
| 6 | [General] K | `"K"` | number | 1 | Optional |
| 3 | [When LTM_TYPE = "Auto Calculation", POSITION in ["I", "I & J"]] Strain(I) · Minimum: 0 | `"STRAIN_I"` | number | 1e-05 | Optional |
| 4 | [When LTM_TYPE = "Auto Calculation", POSITION in ["J", "I & J"]] Strain(J) · Minimum: 0 | `"STRAIN_J"` | number | 1e-05 | Optional |
| 5 | [When LTM_TYPE = "Auto Calculation"] Kb · Minimum: 0 | `"KB"` | number | 1 | Optional |
| 6 | [When LTM_TYPE = "User Input"] K · Minimum: 0 | `"K"` | number | 1 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is an element number (e.g., \"1\"). The element must exist in the model.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Load Test Measurements",
          "type": "object",
          "required": [
            "POSITION",
            "LTM_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "POSITION": {
              "type": "integer",
              "description": "Position Type",
              "default": 0,
              "enum": [
                0,
                1,
                2
              ]
            },
            "LTM_TYPE": {
              "type": "integer",
              "description": "Load Test Measurement Type",
              "default": 0,
              "enum": [
                0,
                1
              ]
            },
            "STRAIN_I": {
              "type": "number",
              "description": "Strain at I-End. Required when LTM_TYPE is Auto Calculation(0) and POSITION is I(0) or I & J(2).",
              "default": 1e-05
            },
            "STRAIN_J": {
              "type": "number",
              "description": "Strain at J-End. Required when LTM_TYPE is Auto Calculation(0) and POSITION is J(1) or I & J(2).",
              "default": 1e-05
            },
            "KB": {
              "type": "number",
              "description": "Load Test Measurement Benefit Factor. Required when LTM_TYPE is Auto Calculation(0).",
              "default": 1
            },
            "K": {
              "type": "number",
              "description": "Adjustment Factor. Required when LTM_TYPE is User Input(1).",
              "default": 1
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

- `DATR`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "POSITION": 0,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "KB": 0.8
    },
    "2": {
      "POSITION": 1,
      "LTM_TYPE": 0,
      "STRAIN_J": 0.00011,
      "KB": 0.8
    },
    "3": {
      "POSITION": 2,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "STRAIN_J": 0.0001,
      "KB": 0.5
    },
    "4": {
      "POSITION": 2,
      "LTM_TYPE": 1,
      "K": 1.1
    }
  }
}
```

**Response**

```json
{
  "DATR": {
    "1": {
      "POSITION": 0,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "KB": 0.8
    },
    "2": {
      "POSITION": 1,
      "LTM_TYPE": 0,
      "STRAIN_J": 0.00011,
      "KB": 0.8
    },
    "3": {
      "POSITION": 2,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "STRAIN_J": 0.0001,
      "KB": 0.5
    },
    "4": {
      "POSITION": 2,
      "LTM_TYPE": 1,
      "K": 1.1
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/DATR"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "POSITION": 0,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "KB": 0.8
    },
    "2": {
      "POSITION": 1,
      "LTM_TYPE": 0,
      "STRAIN_J": 0.00011,
      "KB": 0.8
    },
    "3": {
      "POSITION": 2,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "STRAIN_J": 0.0001,
      "KB": 0.5
    },
    "4": {
      "POSITION": 2,
      "LTM_TYPE": 1,
      "K": 1.1
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 11. `MATD` — Modify Material

> **기능** 평가에 사용할 콘크리트 및 철근 재료를 수정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/MATD
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738369976729](https://support.midasuser.com/hc/en-us/articles/64738369976729)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a concrete material ID (e.g., "1"). Only concrete (type C) materials are serviced. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Girder Material Type | `"GIRDER_MATL_PROP"` | object | - | **Required** |
| 1.1 | └ [General] Code · None: "None" · ASTM19(RC): "ASTM19(RC)" · ASTM(RC): "ASTM(RC)" · U.S.C(US)(RC): "U.S.C(US)(RC)" · U.S.C(SI)(RC): "U.S.C(SI)(RC)" · NMX2023(RC): "NMX2023(RC)" · NMX2023(MKS)(RC): "NMX2023(MKS)(RC)" · NMX NTC-2017(RC): "NMX NTC-2017(RC)" · CSA(RC): "CSA(RC)" · BS(RC): "BS(RC)" · EN04(RC): "EN04(RC)" · EN(RC): "EN(RC)" · NTC08(RC): "NTC08(RC)" · NTC12(RC): "NTC12(RC)" · NTC18(RC): "NTC18(RC)" · UNI(RC): "UNI(RC)" · SS(RC): "SS(RC)" · GOST-SP(RC): "GOST-SP(RC)" · GOST-SNIP(RC): "GOST-SNIP(RC)" · JIS(RC): "JIS(RC)" · JIS-Civil(RC): "JIS-Civil(RC)" · JTJ023-85(RC): "JTJ023-85(RC)" · Q/CR 9300-18(RC): "Q/CR 9300-18(RC)" · GB 50917-13(RC): "GB 50917-13(RC)" · GB/T10(RC): "GB/T10(RC)" · GB(RC): "GB(RC)" · GB-Civil(RC): "GB-Civil(RC)" · TB10092-17(RC): "TB10092-17(RC)" · JTG3362-18(RC): "JTG3362-18(RC)" · JTG04(RC): "JTG04(RC)" · TB05(RC): "TB05(RC)" · KS19(RC): "KS19(RC)" · KS01(RC): "KS01(RC)" · KS(RC): "KS(RC)" · KSCE-LSD15(RC): "KSCE-LSD15(RC)" · KS01-Civil(RC): "KS01-Civil(RC)" · KS-Civil(RC): "KS-Civil(RC)" · PNS49(RC): "PNS49(RC)" · SNI(RC): "SNI(RC)" · TIS(RC): "TIS(RC)" · TIS(MKS)(RC): "TIS(MKS)(RC)" · IRC(RC): "IRC(RC)" · IRS(RC): "IRS(RC)" · IS(RC): "IS(RC)" · CNS560-18(RC): "CNS560-18(RC)" · CNS560(RC): "CNS560(RC)" · CNS(RC): "CNS(RC)" · AS17(RC): "AS17(RC)" · TMH7(RC): "TMH7(RC)" · SP63.2018(RC): "SP63.2018(RC)" · TS(RC): "TS(RC)" · NBR 6118(RC): "NBR 6118(RC)" · TCVN2018(RC): "TCVN2018(RC)" · CSA-S6-25(RC): "CSA-S6-25(RC)" | `"CODE"` | string | - | **Required** |
| 1.2 | └ [When CODE = "None"] Name | `"NAME"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["ASTM19(RC)", "ASTM(RC)", "U.S.C(US)(RC)"]] Grade · Grade C2500: "Grade C2500" · Grade C3000: "Grade C3000" · Grade C3500: "Grade C3500" · Grade C4000: "Grade C4000" · Grade C4500: "Grade C4500" · Grade C5000: "Grade C5000" · Grade C6000: "Grade C6000" · Grade C7000: "Grade C7000" · Grade C8000: "Grade C8000" · Grade C9000: "Grade C9000" · Grade C10000: "Grade C10000" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["U.S.C(SI)(RC)", "PNS49(RC)"]] Grade · Grade C18: "Grade C18" · Grade C21: "Grade C21" · Grade C25: "Grade C25" · Grade C28: "Grade C28" · Grade C32: "Grade C32" · Grade C35: "Grade C35" · Grade C42: "Grade C42" · Grade C49: "Grade C49" · Grade C56: "Grade C56" · Grade C63: "Grade C63" · Grade C69: "Grade C69" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)"]] Grade · 250-C1A(C): "250-C1A(C)" · 250-C1A(B): "250-C1A(B)" · 300-C1A(C): "300-C1A(C)" · 300-C1A(B): "300-C1A(B)" · 350-C1A(C): "350-C1A(C)" · 350-C1A(B): "350-C1A(B)" · 400-C1B(C): "400-C1B(C)" · 400-C1B(B): "400-C1B(B)" · 450-C1B(C): "450-C1B(C)" · 450-C1B(B): "450-C1B(B)" · 500-C1B(C): "500-C1B(C)" · 500-C1B(B): "500-C1B(B)" · 550-C1B(C): "550-C1B(C)" · 550-C1B(B): "550-C1B(B)" · 600-C1B(C): "600-C1B(C)" · 600-C1B(B): "600-C1B(B)" · 650-C1B(C): "650-C1B(C)" · 650-C1B(B): "650-C1B(B)" · 700-C1B(C): "700-C1B(C)" · 700-C1B(B): "700-C1B(B)" · 200-C2: "200-C2" · 250-C2: "250-C2" · 300-C2: "300-C2" · 350-C2: "350-C2" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "NMX NTC-2017(RC)"] Grade · 200-C1C: "200-C1C" · 250-C1C: "250-C1C" · 300-C1C: "300-C1C" · 350-C1C: "350-C1C" · 400-C1C: "400-C1C" · 450-C1C: "450-C1C" · 500-C1C: "500-C1C" · 550-C1C: "550-C1C" · 600-C1C: "600-C1C" · 650-C1C: "650-C1C" · 700-C1C: "700-C1C" · 750-C1C: "750-C1C" · 800-C1C: "800-C1C" · 200-C1B: "200-C1B" · 250-C1B: "250-C1B" · 300-C1B: "300-C1B" · 350-C1B: "350-C1B" · 400-C1B: "400-C1B" · 450-C1B: "450-C1B" · 500-C1B: "500-C1B" · 550-C1B: "550-C1B" · 600-C1B: "600-C1B" · 650-C1B: "650-C1B" · 700-C1B: "700-C1B" · 750-C1B: "750-C1B" · 800-C1B: "800-C1B" · 150-C2: "150-C2" · 200-C2: "200-C2" · 250-C2: "250-C2" · 300-C2: "300-C2" · 400-C2: "400-C2" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "CSA(RC)"] Grade · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "BS(RC)"] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Grade · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C30/37: "C30/37" · C32/40: "C32/40" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" · C55/67: "C55/67" · C60/75: "C60/75" · C70/85: "C70/85" · C80/95: "C80/95" · C90/105: "C90/105" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "EN(RC)"] Grade · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C30/37: "C30/37" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Grade · C8/10: "C8/10" · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C28/35: "C28/35" · C30/37: "C30/37" · C32/40: "C32/40" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" · C55/67: "C55/67" · C60/75: "C60/75" · C70/85: "C70/85" · C80/95: "C80/95" · C90/105: "C90/105" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "UNI(RC)"] Grade · Rck10: "Rck10" · Rck15: "Rck15" · Rck20: "Rck20" · Rck25: "Rck25" · Rck30: "Rck30" · Rck35: "Rck35" · Rck40: "Rck40" · Rck45: "Rck45" · Rck50: "Rck50" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["GOST-SP(RC)", "GOST-SNIP(RC)"]] Grade · B20: "B20" · B22.5: "B22.5" · B25: "B25" · B27.5: "B27.5" · B30: "B30" · B35: "B35" · B40: "B40" · B45: "B45" · B50: "B50" · B55: "B55" · B60: "B60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "JIS(RC)"] Grade · Fc18: "Fc18" · Fc21: "Fc21" · Fc24: "Fc24" · Fc27: "Fc27" · Fc30: "Fc30" · Fc33: "Fc33" · Fc36: "Fc36" · Fc39: "Fc39" · Fc42: "Fc42" · Fc45: "Fc45" · Fc48: "Fc48" · Fc51: "Fc51" · Fc54: "Fc54" · Fc57: "Fc57" · Fc60: "Fc60" · Fc18(LT1): "Fc18(LT1)" · Fc21(LT1): "Fc21(LT1)" · Fc24(LT1): "Fc24(LT1)" · Fc27(LT1): "Fc27(LT1)" · Fc30(LT1): "Fc30(LT1)" · Fc33(LT1): "Fc33(LT1)" · Fc36(LT1): "Fc36(LT1)" · Fc18(LT2): "Fc18(LT2)" · Fc21(LT2): "Fc21(LT2)" · Fc24(LT2): "Fc24(LT2)" · Fc27(LT2): "Fc27(LT2)" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "JIS-Civil(RC)"] Grade · Fc21: "Fc21" · Fc24: "Fc24" · Fc27: "Fc27" · Fc30: "Fc30" · Fc36: "Fc36" · Fc40: "Fc40" · Fc50: "Fc50" · Fc60: "Fc60" · Fc70: "Fc70" · Fc80: "Fc80" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "JTJ023-85(RC)"] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C40: "C40" · C50: "C50" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Grade · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "GB 50917-13(RC)"] Grade · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["GB/T10(RC)", "GB(RC)", "JTG04(RC)"]] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "GB-Civil(RC)"] Grade · 15: "15" · 20: "20" · 25: "25" · 30: "30" · 40: "40" · 50: "50" · 60: "60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "JTG3362-18(RC)"] Grade · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "TB05(RC)"] Grade · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["KS19(RC)", "KS01(RC)", "KS01-Civil(RC)"]] Grade · C15: "C15" · C18: "C18" · C21: "C21" · C24: "C24" · C27: "C27" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C49: "C49" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" · C85: "C85" · C90: "C90" · C95: "C95" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Grade · C150: "C150" · C180: "C180" · C210: "C210" · C240: "C240" · C270: "C270" · C300: "C300" · C350: "C350" · C400: "C400" · C450: "C450" · C500: "C500" · C550: "C550" · C600: "C600" · C650: "C650" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "KSCE-LSD15(RC)"] Grade · C15: "C15" · C18: "C18" · C21: "C21" · C24: "C24" · C27: "C27" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" · C85: "C85" · C90: "C90" · C95: "C95" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "SNI(RC)"] Grade · fc17: "fc17" · fc21: "fc21" · fc25: "fc25" · fc30: "fc30" · fc35: "fc35" · fc40: "fc40" · fc45: "fc45" · fc50: "fc50" · fc55: "fc55" · fc60: "fc60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Grade · C150: "C150" · C180: "C180" · C210: "C210" · C240: "C240" · C250: "C250" · C280: "C280" · C300: "C300" · C320: "C320" · C350: "C350" · C380: "C380" · C400: "C400" · C450: "C450" · C500: "C500" · C550: "C550" · C600: "C600" · C650: "C650" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "IRC(RC)"] Grade · M15: "M15" · M20: "M20" · M25: "M25" · M30: "M30" · M35: "M35" · M40: "M40" · M45: "M45" · M50: "M50" · M55: "M55" · M60: "M60" · M65: "M65" · M70: "M70" · M75: "M75" · M80: "M80" · M85: "M85" · M90: "M90" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "IRS(RC)"] Grade · M20: "M20" · M25: "M25" · M30: "M30" · M35: "M35" · M40: "M40" · M45: "M45" · M50: "M50" · M55: "M55" · M60: "M60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "IS(RC)"] Grade · M10: "M10" · M15: "M15" · M20: "M20" · M25: "M25" · M30: "M30" · M35: "M35" · M40: "M40" · M45: "M45" · M50: "M50" · M55: "M55" · M60: "M60" · M65: "M65" · M70: "M70" · M75: "M75" · M80: "M80" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "CNS560-18(RC)"] Grade · C210: "C210" · C245: "C245" · C280: "C280" · C315: "C315" · C350: "C350" · C420: "C420" · C490: "C490" · C560: "C560" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE in ["CNS560(RC)", "CNS(RC)"]] Grade · C210: "C210" · C245: "C245" · C280: "C280" · C315: "C315" · C350: "C350" · C420: "C420" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "AS17(RC)"] Grade · C20: "C20" · C25: "C25" · C32: "C32" · C40: "C40" · C50: "C50" · C65: "C65" · C80: "C80" · C100: "C100" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "TMH7(RC)"] Grade · Grade 20: "Grade 20" · Grade 25: "Grade 25" · Grade 30: "Grade 30" · Grade 40: "Grade 40" · Grade 50: "Grade 50" · Grade 60: "Grade 60" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "SP63.2018(RC)"] Grade · B3.5: "B3.5" · B5: "B5" · B7.5: "B7.5" · B10: "B10" · B12.5: "B12.5" · B15: "B15" · B20: "B20" · B25: "B25" · B30: "B30" · B35: "B35" · B40: "B40" · B45: "B45" · B50: "B50" · B55: "B55" · B60: "B60" · B70: "B70" · B80: "B80" · B90: "B90" · B100: "B100" · B3.5A: "B3.5A" · B5A: "B5A" · B7.5A: "B7.5A" · B10A: "B10A" · B12.5A: "B12.5A" · B15A: "B15A" · B20A: "B20A" · B25A: "B25A" · B30A: "B30A" · B35A: "B35A" · B40A: "B40A" · B15B: "B15B" · B20B: "B20B" · B25B: "B25B" · B30B: "B30B" · B35B: "B35B" · B40B: "B40B" · B45B: "B45B" · B50B: "B50B" · B55B: "B55B" · B60B: "B60B" · LB2.5D800: "LB2.5D800" · LB3.5D800: "LB3.5D800" · LB5D800: "LB5D800" · LB7.5D800: "LB7.5D800" · LB2.5D1000: "LB2.5D1000" · LB3.5D1000: "LB3.5D1000" · LB5D1000: "LB5D1000" · LB7.5D1000: "LB7.5D1000" · LB10D1000: "LB10D1000" · LB12.5D1000: "LB12.5D1000" · LB2.5D1200: "LB2.5D1200" · LB3.5D1200: "LB3.5D1200" · LB5D1200: "LB5D1200" · LB7.5D1200: "LB7.5D1200" · LB10D1200: "LB10D1200" · LB12.5D1200: "LB12.5D1200" · LB15D1200: "LB15D1200" · LB2.5D1400: "LB2.5D1400" · LB3.5D1400: "LB3.5D1400" · LB5D1400: "LB5D1400" · LB7.5D1400: "LB7.5D1400" · LB10D1400: "LB10D1400" · LB12.5D1400: "LB12.5D1400" · LB15D1400: "LB15D1400" · LB20D1400: "LB20D1400" · LB25D1400: "LB25D1400" · LB30D1400: "LB30D1400" · LB3.5D1600: "LB3.5D1600" · LB5D1600: "LB5D1600" · LB7.5D1600: "LB7.5D1600" · LB10D1600: "LB10D1600" · LB12.5D1600: "LB12.5D1600" · LB15D1600: "LB15D1600" · LB20D1600: "LB20D1600" · LB25D1600: "LB25D1600" · LB30D1600: "LB30D1600" · LB35D1600: "LB35D1600" · LB5D1800: "LB5D1800" · LB7.5D1800: "LB7.5D1800" · LB10D1800: "LB10D1800" · LB12.5D1800: "LB12.5D1800" · LB15D1800: "LB15D1800" · LB20D1800: "LB20D1800" · LB25D1800: "LB25D1800" · LB30D1800: "LB30D1800" · LB35D1800: "LB35D1800" · LB40D1800: "LB40D1800" · LB7.5D2000: "LB7.5D2000" · LB10D2000: "LB10D2000" · LB12.5D2000: "LB12.5D2000" · LB15D2000: "LB15D2000" · LB20D2000: "LB20D2000" · LB25D2000: "LB25D2000" · LB30D2000: "LB30D2000" · LB35D2000: "LB35D2000" · LB40D2000: "LB40D2000" · CB1.5D500: "CB1.5D500" · CB1.5D600: "CB1.5D600" · CB2D600: "CB2D600" · CB2.5D600: "CB2.5D600" · CB1.5D700: "CB1.5D700" · CB2D700: "CB2D700" · CB2.5D700: "CB2.5D700" · CB3.5D700: "CB3.5D700" · CB2.5D800: "CB2.5D800" · CB3.5D800: "CB3.5D800" · CB5D800: "CB5D800" · CB3.5D900: "CB3.5D900" · CB5D900: "CB5D900" · CB7.5D900: "CB7.5D900" · CB5D1000: "CB5D1000" · CB7.5D1000: "CB7.5D1000" · CB10D1000: "CB10D1000" · CB7.5D1100: "CB7.5D1100" · CB10D1100: "CB10D1100" · CB12.5D1100: "CB12.5D1100" · CB15D1100: "CB15D1100" · CB10D1200: "CB10D1200" · CB12.5D1200: "CB12.5D1200" · CB15D1200: "CB15D1200" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "TS(RC)"] Grade · C16: "C16" · C18: "C18" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "NBR 6118(RC)"] Grade · C20BD: "C20BD" · C20GG: "C20GG" · C20LS: "C20LS" · C20SS: "C20SS" · C25BD: "C25BD" · C25GG: "C25GG" · C25LS: "C25LS" · C25SS: "C25SS" · C30BD: "C30BD" · C30GG: "C30GG" · C30LS: "C30LS" · C30SS: "C30SS" · C35BD: "C35BD" · C35GG: "C35GG" · C35LS: "C35LS" · C35SS: "C35SS" · C40BD: "C40BD" · C40GG: "C40GG" · C40LS: "C40LS" · C40SS: "C40SS" · C45BD: "C45BD" · C45GG: "C45GG" · C45LS: "C45LS" · C45SS: "C45SS" · C50BD: "C50BD" · C50GG: "C50GG" · C50LS: "C50LS" · C50SS: "C50SS" · C55BD: "C55BD" · C55GG: "C55GG" · C55LS: "C55LS" · C55SS: "C55SS" · C60BD: "C60BD" · C60GG: "C60GG" · C60LS: "C60LS" · C60SS: "C60SS" · C65BD: "C65BD" · C65GG: "C65GG" · C65LS: "C65LS" · C65SS: "C65SS" · C70BD: "C70BD" · C70GG: "C70GG" · C70LS: "C70LS" · C70SS: "C70SS" · C75BD: "C75BD" · C75GG: "C75GG" · C75LS: "C75LS" · C75SS: "C75SS" · C80BD: "C80BD" · C80GG: "C80GG" · C80LS: "C80LS" · C80SS: "C80SS" · C85BD: "C85BD" · C85GG: "C85GG" · C85LS: "C85LS" · C85SS: "C85SS" · C90BD: "C90BD" · C90GG: "C90GG" · C90LS: "C90LS" · C90SS: "C90SS" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "TCVN2018(RC)"] Grade · B3.5: "B3.5" · B5: "B5" · B7.5: "B7.5" · B10: "B10" · B12.5: "B12.5" · B15: "B15" · B20: "B20" · B25: "B25" · B30: "B30" · B35: "B35" · B40: "B40" · B45: "B45" · B50: "B50" · B55: "B55" · B60: "B60" · B70: "B70" · B80: "B80" · B90: "B90" · B100: "B100" | `"GRADE"` | string | - | **Required** |
| 1.3 | └ [When CODE = "CSA-S6-25(RC)"] Grade · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" · C85: "C85" | `"GRADE"` | string | - | **Required** |
| 1.4 | └ [When CODE = "None"] Specified Compressive Strength (fc\|fck) · Minimum: 0 | `"COMP_STRENGTH"` | number | - | **Required** |
| 1.5 | └ [When CODE = "None"] Light Weight Concrete Factor | `"LIGHT_WEIGHT_FACTOR"` | boolean | - | Optional |
| 1.6 | └ [When LIGHT_WEIGHT_FACTOR = true] Light Weight Factor Value · Range: 0.75~1 | `"FACTOR_VALUE"` | number | - | **Required** |
| 2 | [General] Girder Rebar Selection | `"GIRDER_REBAR_PROP"` | object | - | **Required** |
| 2.1 | └ [General] Code · None: "None" · ASTM19(RC): "ASTM19(RC)" · ASTM(RC): "ASTM(RC)" · U.S.C(US)(RC): "U.S.C(US)(RC)" · U.S.C(SI)(RC): "U.S.C(SI)(RC)" · NMX2023(RC): "NMX2023(RC)" · NMX2023(MKS)(RC): "NMX2023(MKS)(RC)" · NMX NTC-2017(RC): "NMX NTC-2017(RC)" · CSA(RC): "CSA(RC)" · BS(RC): "BS(RC)" · EN04(RC): "EN04(RC)" · EN(RC): "EN(RC)" · NTC08(RC): "NTC08(RC)" · NTC12(RC): "NTC12(RC)" · NTC18(RC): "NTC18(RC)" · UNI(RC): "UNI(RC)" · SS(RC): "SS(RC)" · GOST-SP(RC): "GOST-SP(RC)" · GOST-SNIP(RC): "GOST-SNIP(RC)" · JIS(RC): "JIS(RC)" · JIS-Civil(RC): "JIS-Civil(RC)" · JTJ023-85(RC): "JTJ023-85(RC)" · Q/CR 9300-18(RC): "Q/CR 9300-18(RC)" · GB 50917-13(RC): "GB 50917-13(RC)" · GB/T10(RC): "GB/T10(RC)" · GB(RC): "GB(RC)" · GB-Civil(RC): "GB-Civil(RC)" · TB10092-17(RC): "TB10092-17(RC)" · JTG3362-18(RC): "JTG3362-18(RC)" · JTG04(RC): "JTG04(RC)" · TB05(RC): "TB05(RC)" · KS19(RC): "KS19(RC)" · KS01(RC): "KS01(RC)" · KS(RC): "KS(RC)" · KSCE-LSD15(RC): "KSCE-LSD15(RC)" · KS01-Civil(RC): "KS01-Civil(RC)" · KS-Civil(RC): "KS-Civil(RC)" · PNS49(RC): "PNS49(RC)" · SNI(RC): "SNI(RC)" · TIS(RC): "TIS(RC)" · TIS(MKS)(RC): "TIS(MKS)(RC)" · IRC(RC): "IRC(RC)" · IRS(RC): "IRS(RC)" · IS(RC): "IS(RC)" · CNS560-18(RC): "CNS560-18(RC)" · CNS560(RC): "CNS560(RC)" · CNS(RC): "CNS(RC)" · AS17(RC): "AS17(RC)" · TMH7(RC): "TMH7(RC)" · SP63.2018(RC): "SP63.2018(RC)" · TS(RC): "TS(RC)" · NBR 6118(RC): "NBR 6118(RC)" · TCVN2018(RC): "TCVN2018(RC)" · CSA-S6-25(RC): "CSA-S6-25(RC)" | `"CODE"` | string | - | **Required** |
| 2.2 | └ [When CODE = "ASTM19(RC)"] Grade of Main Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "ASTM19(RC)"] Grade of Sub-Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "ASTM(RC)"] Grade of Main Rebar · Grade 40: "Grade 40" · Grade 50: "Grade 50" · Grade 60: "Grade 60" · Grade 75: "Grade 75" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "ASTM(RC)"] Grade of Sub-Rebar · Grade 40: "Grade 40" · Grade 50: "Grade 50" · Grade 60: "Grade 60" · Grade 75: "Grade 75" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "U.S.C(US)(RC)"] Grade of Main Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 75: "Grade 75" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "U.S.C(US)(RC)"] Grade of Sub-Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 75: "Grade 75" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "U.S.C(SI)(RC)"] Grade of Main Rebar · Grade 280: "Grade 280" · Grade 420: "Grade 420" · Grade 520: "Grade 520" · Grade 550: "Grade 550" · Grade 690: "Grade 690" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "U.S.C(SI)(RC)"] Grade of Sub-Rebar · Grade 280: "Grade 280" · Grade 420: "Grade 420" · Grade 520: "Grade 520" · Grade 550: "Grade 550" · Grade 690: "Grade 690" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)", "NMX NTC-2017(RC)"]] Grade of Main Rebar · Grade 42: "Grade 42" · Grade 56: "Grade 56" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)", "NMX NTC-2017(RC)"]] Grade of Sub-Rebar · Grade 42: "Grade 42" · Grade 56: "Grade 56" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "CSA(RC)"] Grade of Main Rebar · 300R: "300R" · 400R: "400R" · 500R: "500R" · 400W: "400W" · 500W: "500W" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "CSA(RC)"] Grade of Sub-Rebar · 300R: "300R" · 400R: "400R" · 500R: "500R" · 400W: "400W" · 500W: "500W" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "BS(RC)"] Grade of Main Rebar · S250: "S250" · S460: "S460" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "BS(RC)"] Grade of Sub-Rebar · S250: "S250" · S460: "S460" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Grade of Main Rebar · Class A: "Class A" · Class B: "Class B" · Class C: "Class C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Grade of Sub-Rebar · Class A: "Class A" · Class B: "Class B" · Class C: "Class C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "EN(RC)"] Grade of Main Rebar · S220: "S220" · S250: "S250" · S300: "S300" · S400: "S400" · S460: "S460" · S500: "S500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "EN(RC)"] Grade of Sub-Rebar · S220: "S220" · S250: "S250" · S300: "S300" · S400: "S400" · S460: "S460" · S500: "S500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Grade of Main Rebar · B450C: "B450C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Grade of Sub-Rebar · B450C: "B450C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "UNI(RC)"] Grade of Main Rebar · FeB22k: "FeB22k" · FeB32k: "FeB32k" · FeB38k: "FeB38k" · FeB44k: "FeB44k" · B450C: "B450C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "UNI(RC)"] Grade of Sub-Rebar · FeB22k: "FeB22k" · FeB32k: "FeB32k" · FeB38k: "FeB38k" · FeB44k: "FeB44k" · B450C: "B450C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "GOST-SP(RC)"] Grade of Main Rebar · A240: "A240" · A300: "A300" · A400: "A400" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "GOST-SP(RC)"] Grade of Sub-Rebar · A240: "A240" · A300: "A300" · A400: "A400" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "GOST-SNIP(RC)"] Grade of Main Rebar · A-I: "A-I" · A-II: "A-II" · A-III: "A-III" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "GOST-SNIP(RC)"] Grade of Sub-Rebar · A-I: "A-I" · A-II: "A-II" · A-III: "A-III" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "JIS(RC)"] Grade of Main Rebar · SR235: "SR235" · SR295: "SR295" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "JIS(RC)"] Grade of Sub-Rebar · SR235: "SR235" · SR295: "SR295" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "JIS-Civil(RC)"] Grade of Main Rebar · SR235: "SR235" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "JIS-Civil(RC)"] Grade of Sub-Rebar · SR235: "SR235" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["JTJ023-85(RC)", "GB-Civil(RC)"]] Grade of Main Rebar · Grade 1: "Grade 1" · Grade 2: "Grade 2" · Grade 3: "Grade 3" · 5 Hao: "5 Hao" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["JTJ023-85(RC)", "GB-Civil(RC)"]] Grade of Sub-Rebar · Grade 1: "Grade 1" · Grade 2: "Grade 2" · Grade 3: "Grade 3" · 5 Hao: "5 Hao" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRB500: "HRB500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRB500: "HRB500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "GB 50917-13(RC)"] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "GB 50917-13(RC)"] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "GB/T10(RC)"] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" · RRB500: "RRB500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "GB/T10(RC)"] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" · RRB500: "RRB500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "GB(RC)"] Grade of Main Rebar · HPB235: "HPB235" · HRB335: "HRB335" · HRB400: "HRB400" · RRB400: "RRB400" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "GB(RC)"] Grade of Sub-Rebar · HPB235: "HPB235" · HRB335: "HRB335" · HRB400: "HRB400" · RRB400: "RRB400" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "JTG3362-18(RC)"] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "JTG3362-18(RC)"] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "JTG04(RC)"] Grade of Main Rebar · R235: "R235" · HRB335: "HRB335" · HRB400: "HRB400" · KL400: "KL400" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "JTG04(RC)"] Grade of Sub-Rebar · R235: "R235" · HRB335: "HRB335" · HRB400: "HRB400" · KL400: "KL400" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "TB05(RC)"] Grade of Main Rebar · Q235: "Q235" · HRB335: "HRB335" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "TB05(RC)"] Grade of Sub-Rebar · Q235: "Q235" · HRB335: "HRB335" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "KS19(RC)"] Grade of Main Rebar · SD300: "SD300" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" · SD700: "SD700" · SD400S: "SD400S" · SD500S: "SD500S" · SD600S: "SD600S" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "KS19(RC)"] Grade of Sub-Rebar · SD300: "SD300" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" · SD700: "SD700" · SD400S: "SD400S" · SD500S: "SD500S" · SD600S: "SD600S" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["KS01(RC)", "KSCE-LSD15(RC)", "KS01-Civil(RC)"]] Grade of Main Rebar · SD240: "SD240" · SD300: "SD300" · SD350: "SD350" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["KS01(RC)", "KSCE-LSD15(RC)", "KS01-Civil(RC)"]] Grade of Sub-Rebar · SD240: "SD240" · SD300: "SD300" · SD350: "SD350" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Grade of Main Rebar · SD24: "SD24" · SD30: "SD30" · SD35: "SD35" · SD40: "SD40" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Grade of Sub-Rebar · SD24: "SD24" · SD30: "SD30" · SD35: "SD35" · SD40: "SD40" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "PNS49(RC)"] Grade of Main Rebar · 230R: "230R" · 280R: "280R" · 420R: "420R" · 520R: "520R" · 550R: "550R" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "PNS49(RC)"] Grade of Sub-Rebar · 230R: "230R" · 280R: "280R" · 420R: "420R" · 520R: "520R" · 550R: "550R" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "SNI(RC)"] Grade of Main Rebar · BjTP 280: "BjTP 280" · BjTS 280: "BjTS 280" · BjTS 420A: "BjTS 420A" · BjTS 420B: "BjTS 420B" · BjTS 520: "BjTS 520" · BjTS 550: "BjTS 550" · BjTS 700: "BjTS 700" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "SNI(RC)"] Grade of Sub-Rebar · BjTP 280: "BjTP 280" · BjTS 280: "BjTS 280" · BjTS 420A: "BjTS 420A" · BjTS 420B: "BjTS 420B" · BjTS 520: "BjTS 520" · BjTS 550: "BjTS 550" · BjTS 700: "BjTS 700" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Grade of Main Rebar · SR24: "SR24" · SD30: "SD30" · SD40: "SD40" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Grade of Sub-Rebar · SR24: "SR24" · SD30: "SD30" · SD40: "SD40" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE in ["IRC(RC)", "IRS(RC)"]] Grade of Main Rebar · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE in ["IRC(RC)", "IRS(RC)"]] Grade of Sub-Rebar · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "IS(RC)"] Grade of Main Rebar · Fe240: "Fe240" · Fe250: "Fe250" · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "IS(RC)"] Grade of Sub-Rebar · Fe240: "Fe240" · Fe250: "Fe250" · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "CNS560-18(RC)"] Grade of Main Rebar · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490W: "SD490W" · SD550W: "SD550W" · SD690: "SD690" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "CNS560-18(RC)"] Grade of Sub-Rebar · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490W: "SD490W" · SD550W: "SD550W" · SD690: "SD690" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "CNS560(RC)"] Grade of Main Rebar · SR240: "SR240" · SR300: "SR300" · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490: "SD490" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "CNS560(RC)"] Grade of Sub-Rebar · SR240: "SR240" · SR300: "SR300" · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490: "SD490" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "CNS(RC)"] Grade of Main Rebar · SD24: "SD24" · SD28: "SD28" · SD30: "SD30" · SD35: "SD35" · SD42: "SD42" · SD42W: "SD42W" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "CNS(RC)"] Grade of Sub-Rebar · SD24: "SD24" · SD28: "SD28" · SD30: "SD30" · SD35: "SD35" · SD42: "SD42" · SD42W: "SD42W" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "AS17(RC)"] Grade of Main Rebar · D500L: "D500L" · D500N: "D500N" · D500E: "D500E" · D500LP: "D500LP" · D600N: "D600N" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "AS17(RC)"] Grade of Sub-Rebar · D500L: "D500L" · D500N: "D500N" · D500E: "D500E" · D500LP: "D500LP" · D600N: "D600N" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "TMH7(RC)"] Grade of Main Rebar · Type A: "Type A" · Type B: "Type B" · Type C: "Type C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "TMH7(RC)"] Grade of Sub-Rebar · Type A: "Type A" · Type B: "Type B" · Type C: "Type C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "SP63.2018(RC)"] Grade of Main Rebar · A240: "A240" · A240_sw: "A240_sw" · A400: "A400" · A400_sw: "A400_sw" · A500: "A500" · A500_sw: "A500_sw" · A600: "A600" · A800: "A800" · A1000: "A1000" · B500: "B500" · B500_sw: "B500_sw" · BP500: "BP500" · BP1200: "BP1200" · BP1300: "BP1300" · BP1400: "BP1400" · BP1500: "BP1500" · BP1600: "BP1600" · K1400: "K1400" · K1450: "K1450" · K1500: "K1500" · K1550: "K1550" · K1650: "K1650" · K1750: "K1750" · K1850: "K1850" · K1900: "K1900" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "SP63.2018(RC)"] Grade of Sub-Rebar · A240: "A240" · A240_sw: "A240_sw" · A400: "A400" · A400_sw: "A400_sw" · A500: "A500" · A500_sw: "A500_sw" · A600: "A600" · A800: "A800" · A1000: "A1000" · B500: "B500" · B500_sw: "B500_sw" · BP500: "BP500" · BP1200: "BP1200" · BP1300: "BP1300" · BP1400: "BP1400" · BP1500: "BP1500" · BP1600: "BP1600" · K1400: "K1400" · K1450: "K1450" · K1500: "K1500" · K1550: "K1550" · K1650: "K1650" · K1750: "K1750" · K1850: "K1850" · K1900: "K1900" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "TS(RC)"] Grade of Main Rebar · B420C: "B420C" · B520C: "B520C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "TS(RC)"] Grade of Sub-Rebar · B420C: "B420C" · B520C: "B520C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "NBR 6118(RC)"] Grade of Main Rebar · CA25: "CA25" · CA50: "CA50" · CA60: "CA60" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "NBR 6118(RC)"] Grade of Sub-Rebar · CA25: "CA25" · CA50: "CA50" · CA60: "CA60" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "TCVN2018(RC)"] Grade of Main Rebar · CB300-V: "CB300-V" · CB400-V: "CB400-V" · CB500-V: "CB500-V" · CB600-V: "CB600-V" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "TCVN2018(RC)"] Grade of Sub-Rebar · CB300-V: "CB300-V" · CB400-V: "CB400-V" · CB500-V: "CB500-V" · CB600-V: "CB600-V" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.2 | └ [When CODE = "CSA-S6-25(RC)"] Grade of Main Rebar · 400W: "400W" · 500W: "500W" · 600W: "600W" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 2.3 | └ [When CODE = "CSA-S6-25(RC)"] Grade of Sub-Rebar · 400W: "400W" · 500W: "500W" · 600W: "600W" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 2.4 | └ [When CODE = "None"] Name of Main Rebar | `"NAME_MAIN_REBAR"` | string | - | **Required** |
| 2.5 | └ [When CODE = "None"] Name of Sub-Rebar | `"NAME_SUB_REBAR"` | string | - | **Required** |
| 2.6 | └ [When CODE = "None"] Fy · Minimum: 0 | `"Fy"` | number | - | **Required** |
| 2.7 | └ [When CODE = "None"] Fys · Minimum: 0 | `"Fys"` | number | - | **Required** |
| 3 | [General] Use Slab Property | `"SLAB_PROP"` | boolean | false | Optional |
| 4 | [When SLAB_PROP = true] Slab Material Type | `"SLAB_MATL_PROP"` | object | - | **Required** |
| 4.1 | └ [When SLAB_PROP = true] Code · None: "None" · ASTM19(RC): "ASTM19(RC)" · ASTM(RC): "ASTM(RC)" · U.S.C(US)(RC): "U.S.C(US)(RC)" · U.S.C(SI)(RC): "U.S.C(SI)(RC)" · NMX2023(RC): "NMX2023(RC)" · NMX2023(MKS)(RC): "NMX2023(MKS)(RC)" · NMX NTC-2017(RC): "NMX NTC-2017(RC)" · CSA(RC): "CSA(RC)" · BS(RC): "BS(RC)" · EN04(RC): "EN04(RC)" · EN(RC): "EN(RC)" · NTC08(RC): "NTC08(RC)" · NTC12(RC): "NTC12(RC)" · NTC18(RC): "NTC18(RC)" · UNI(RC): "UNI(RC)" · SS(RC): "SS(RC)" · GOST-SP(RC): "GOST-SP(RC)" · GOST-SNIP(RC): "GOST-SNIP(RC)" · JIS(RC): "JIS(RC)" · JIS-Civil(RC): "JIS-Civil(RC)" · JTJ023-85(RC): "JTJ023-85(RC)" · Q/CR 9300-18(RC): "Q/CR 9300-18(RC)" · GB 50917-13(RC): "GB 50917-13(RC)" · GB/T10(RC): "GB/T10(RC)" · GB(RC): "GB(RC)" · GB-Civil(RC): "GB-Civil(RC)" · TB10092-17(RC): "TB10092-17(RC)" · JTG3362-18(RC): "JTG3362-18(RC)" · JTG04(RC): "JTG04(RC)" · TB05(RC): "TB05(RC)" · KS19(RC): "KS19(RC)" · KS01(RC): "KS01(RC)" · KS(RC): "KS(RC)" · KSCE-LSD15(RC): "KSCE-LSD15(RC)" · KS01-Civil(RC): "KS01-Civil(RC)" · KS-Civil(RC): "KS-Civil(RC)" · PNS49(RC): "PNS49(RC)" · SNI(RC): "SNI(RC)" · TIS(RC): "TIS(RC)" · TIS(MKS)(RC): "TIS(MKS)(RC)" · IRC(RC): "IRC(RC)" · IRS(RC): "IRS(RC)" · IS(RC): "IS(RC)" · CNS560-18(RC): "CNS560-18(RC)" · CNS560(RC): "CNS560(RC)" · CNS(RC): "CNS(RC)" · AS17(RC): "AS17(RC)" · TMH7(RC): "TMH7(RC)" · SP63.2018(RC): "SP63.2018(RC)" · TS(RC): "TS(RC)" · NBR 6118(RC): "NBR 6118(RC)" · TCVN2018(RC): "TCVN2018(RC)" · CSA-S6-25(RC): "CSA-S6-25(RC)" | `"CODE"` | string | - | **Required** |
| 4.2 | └ [When CODE = "None"] Name | `"NAME"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["ASTM19(RC)", "ASTM(RC)", "U.S.C(US)(RC)"]] Grade · Grade C2500: "Grade C2500" · Grade C3000: "Grade C3000" · Grade C3500: "Grade C3500" · Grade C4000: "Grade C4000" · Grade C4500: "Grade C4500" · Grade C5000: "Grade C5000" · Grade C6000: "Grade C6000" · Grade C7000: "Grade C7000" · Grade C8000: "Grade C8000" · Grade C9000: "Grade C9000" · Grade C10000: "Grade C10000" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["U.S.C(SI)(RC)", "PNS49(RC)"]] Grade · Grade C18: "Grade C18" · Grade C21: "Grade C21" · Grade C25: "Grade C25" · Grade C28: "Grade C28" · Grade C32: "Grade C32" · Grade C35: "Grade C35" · Grade C42: "Grade C42" · Grade C49: "Grade C49" · Grade C56: "Grade C56" · Grade C63: "Grade C63" · Grade C69: "Grade C69" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)"]] Grade · 250-C1A(C): "250-C1A(C)" · 250-C1A(B): "250-C1A(B)" · 300-C1A(C): "300-C1A(C)" · 300-C1A(B): "300-C1A(B)" · 350-C1A(C): "350-C1A(C)" · 350-C1A(B): "350-C1A(B)" · 400-C1B(C): "400-C1B(C)" · 400-C1B(B): "400-C1B(B)" · 450-C1B(C): "450-C1B(C)" · 450-C1B(B): "450-C1B(B)" · 500-C1B(C): "500-C1B(C)" · 500-C1B(B): "500-C1B(B)" · 550-C1B(C): "550-C1B(C)" · 550-C1B(B): "550-C1B(B)" · 600-C1B(C): "600-C1B(C)" · 600-C1B(B): "600-C1B(B)" · 650-C1B(C): "650-C1B(C)" · 650-C1B(B): "650-C1B(B)" · 700-C1B(C): "700-C1B(C)" · 700-C1B(B): "700-C1B(B)" · 200-C2: "200-C2" · 250-C2: "250-C2" · 300-C2: "300-C2" · 350-C2: "350-C2" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "NMX NTC-2017(RC)"] Grade · 200-C1C: "200-C1C" · 250-C1C: "250-C1C" · 300-C1C: "300-C1C" · 350-C1C: "350-C1C" · 400-C1C: "400-C1C" · 450-C1C: "450-C1C" · 500-C1C: "500-C1C" · 550-C1C: "550-C1C" · 600-C1C: "600-C1C" · 650-C1C: "650-C1C" · 700-C1C: "700-C1C" · 750-C1C: "750-C1C" · 800-C1C: "800-C1C" · 200-C1B: "200-C1B" · 250-C1B: "250-C1B" · 300-C1B: "300-C1B" · 350-C1B: "350-C1B" · 400-C1B: "400-C1B" · 450-C1B: "450-C1B" · 500-C1B: "500-C1B" · 550-C1B: "550-C1B" · 600-C1B: "600-C1B" · 650-C1B: "650-C1B" · 700-C1B: "700-C1B" · 750-C1B: "750-C1B" · 800-C1B: "800-C1B" · 150-C2: "150-C2" · 200-C2: "200-C2" · 250-C2: "250-C2" · 300-C2: "300-C2" · 400-C2: "400-C2" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "CSA(RC)"] Grade · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "BS(RC)"] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Grade · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C30/37: "C30/37" · C32/40: "C32/40" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" · C55/67: "C55/67" · C60/75: "C60/75" · C70/85: "C70/85" · C80/95: "C80/95" · C90/105: "C90/105" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "EN(RC)"] Grade · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C30/37: "C30/37" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Grade · C8/10: "C8/10" · C12/15: "C12/15" · C16/20: "C16/20" · C20/25: "C20/25" · C25/30: "C25/30" · C28/35: "C28/35" · C30/37: "C30/37" · C32/40: "C32/40" · C35/45: "C35/45" · C40/50: "C40/50" · C45/55: "C45/55" · C50/60: "C50/60" · C55/67: "C55/67" · C60/75: "C60/75" · C70/85: "C70/85" · C80/95: "C80/95" · C90/105: "C90/105" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "UNI(RC)"] Grade · Rck10: "Rck10" · Rck15: "Rck15" · Rck20: "Rck20" · Rck25: "Rck25" · Rck30: "Rck30" · Rck35: "Rck35" · Rck40: "Rck40" · Rck45: "Rck45" · Rck50: "Rck50" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["GOST-SP(RC)", "GOST-SNIP(RC)"]] Grade · B20: "B20" · B22.5: "B22.5" · B25: "B25" · B27.5: "B27.5" · B30: "B30" · B35: "B35" · B40: "B40" · B45: "B45" · B50: "B50" · B55: "B55" · B60: "B60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "JIS(RC)"] Grade · Fc18: "Fc18" · Fc21: "Fc21" · Fc24: "Fc24" · Fc27: "Fc27" · Fc30: "Fc30" · Fc33: "Fc33" · Fc36: "Fc36" · Fc39: "Fc39" · Fc42: "Fc42" · Fc45: "Fc45" · Fc48: "Fc48" · Fc51: "Fc51" · Fc54: "Fc54" · Fc57: "Fc57" · Fc60: "Fc60" · Fc18(LT1): "Fc18(LT1)" · Fc21(LT1): "Fc21(LT1)" · Fc24(LT1): "Fc24(LT1)" · Fc27(LT1): "Fc27(LT1)" · Fc30(LT1): "Fc30(LT1)" · Fc33(LT1): "Fc33(LT1)" · Fc36(LT1): "Fc36(LT1)" · Fc18(LT2): "Fc18(LT2)" · Fc21(LT2): "Fc21(LT2)" · Fc24(LT2): "Fc24(LT2)" · Fc27(LT2): "Fc27(LT2)" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "JIS-Civil(RC)"] Grade · Fc21: "Fc21" · Fc24: "Fc24" · Fc27: "Fc27" · Fc30: "Fc30" · Fc36: "Fc36" · Fc40: "Fc40" · Fc50: "Fc50" · Fc60: "Fc60" · Fc70: "Fc70" · Fc80: "Fc80" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "JTJ023-85(RC)"] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C40: "C40" · C50: "C50" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Grade · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "GB 50917-13(RC)"] Grade · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["GB/T10(RC)", "GB(RC)", "JTG04(RC)"]] Grade · C15: "C15" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "GB-Civil(RC)"] Grade · 15: "15" · 20: "20" · 25: "25" · 30: "30" · 40: "40" · 50: "50" · 60: "60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "JTG3362-18(RC)"] Grade · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "TB05(RC)"] Grade · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["KS19(RC)", "KS01(RC)", "KS01-Civil(RC)"]] Grade · C15: "C15" · C18: "C18" · C21: "C21" · C24: "C24" · C27: "C27" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C49: "C49" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" · C85: "C85" · C90: "C90" · C95: "C95" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Grade · C150: "C150" · C180: "C180" · C210: "C210" · C240: "C240" · C270: "C270" · C300: "C300" · C350: "C350" · C400: "C400" · C450: "C450" · C500: "C500" · C550: "C550" · C600: "C600" · C650: "C650" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "KSCE-LSD15(RC)"] Grade · C15: "C15" · C18: "C18" · C21: "C21" · C24: "C24" · C27: "C27" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" · C85: "C85" · C90: "C90" · C95: "C95" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "SNI(RC)"] Grade · fc17: "fc17" · fc21: "fc21" · fc25: "fc25" · fc30: "fc30" · fc35: "fc35" · fc40: "fc40" · fc45: "fc45" · fc50: "fc50" · fc55: "fc55" · fc60: "fc60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Grade · C150: "C150" · C180: "C180" · C210: "C210" · C240: "C240" · C250: "C250" · C280: "C280" · C300: "C300" · C320: "C320" · C350: "C350" · C380: "C380" · C400: "C400" · C450: "C450" · C500: "C500" · C550: "C550" · C600: "C600" · C650: "C650" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "IRC(RC)"] Grade · M15: "M15" · M20: "M20" · M25: "M25" · M30: "M30" · M35: "M35" · M40: "M40" · M45: "M45" · M50: "M50" · M55: "M55" · M60: "M60" · M65: "M65" · M70: "M70" · M75: "M75" · M80: "M80" · M85: "M85" · M90: "M90" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "IRS(RC)"] Grade · M20: "M20" · M25: "M25" · M30: "M30" · M35: "M35" · M40: "M40" · M45: "M45" · M50: "M50" · M55: "M55" · M60: "M60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "IS(RC)"] Grade · M10: "M10" · M15: "M15" · M20: "M20" · M25: "M25" · M30: "M30" · M35: "M35" · M40: "M40" · M45: "M45" · M50: "M50" · M55: "M55" · M60: "M60" · M65: "M65" · M70: "M70" · M75: "M75" · M80: "M80" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "CNS560-18(RC)"] Grade · C210: "C210" · C245: "C245" · C280: "C280" · C315: "C315" · C350: "C350" · C420: "C420" · C490: "C490" · C560: "C560" · C700: "C700" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE in ["CNS560(RC)", "CNS(RC)"]] Grade · C210: "C210" · C245: "C245" · C280: "C280" · C315: "C315" · C350: "C350" · C420: "C420" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "AS17(RC)"] Grade · C20: "C20" · C25: "C25" · C32: "C32" · C40: "C40" · C50: "C50" · C65: "C65" · C80: "C80" · C100: "C100" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "TMH7(RC)"] Grade · Grade 20: "Grade 20" · Grade 25: "Grade 25" · Grade 30: "Grade 30" · Grade 40: "Grade 40" · Grade 50: "Grade 50" · Grade 60: "Grade 60" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "SP63.2018(RC)"] Grade · B3.5: "B3.5" · B5: "B5" · B7.5: "B7.5" · B10: "B10" · B12.5: "B12.5" · B15: "B15" · B20: "B20" · B25: "B25" · B30: "B30" · B35: "B35" · B40: "B40" · B45: "B45" · B50: "B50" · B55: "B55" · B60: "B60" · B70: "B70" · B80: "B80" · B90: "B90" · B100: "B100" · B3.5A: "B3.5A" · B5A: "B5A" · B7.5A: "B7.5A" · B10A: "B10A" · B12.5A: "B12.5A" · B15A: "B15A" · B20A: "B20A" · B25A: "B25A" · B30A: "B30A" · B35A: "B35A" · B40A: "B40A" · B15B: "B15B" · B20B: "B20B" · B25B: "B25B" · B30B: "B30B" · B35B: "B35B" · B40B: "B40B" · B45B: "B45B" · B50B: "B50B" · B55B: "B55B" · B60B: "B60B" · LB2.5D800: "LB2.5D800" · LB3.5D800: "LB3.5D800" · LB5D800: "LB5D800" · LB7.5D800: "LB7.5D800" · LB2.5D1000: "LB2.5D1000" · LB3.5D1000: "LB3.5D1000" · LB5D1000: "LB5D1000" · LB7.5D1000: "LB7.5D1000" · LB10D1000: "LB10D1000" · LB12.5D1000: "LB12.5D1000" · LB2.5D1200: "LB2.5D1200" · LB3.5D1200: "LB3.5D1200" · LB5D1200: "LB5D1200" · LB7.5D1200: "LB7.5D1200" · LB10D1200: "LB10D1200" · LB12.5D1200: "LB12.5D1200" · LB15D1200: "LB15D1200" · LB2.5D1400: "LB2.5D1400" · LB3.5D1400: "LB3.5D1400" · LB5D1400: "LB5D1400" · LB7.5D1400: "LB7.5D1400" · LB10D1400: "LB10D1400" · LB12.5D1400: "LB12.5D1400" · LB15D1400: "LB15D1400" · LB20D1400: "LB20D1400" · LB25D1400: "LB25D1400" · LB30D1400: "LB30D1400" · LB3.5D1600: "LB3.5D1600" · LB5D1600: "LB5D1600" · LB7.5D1600: "LB7.5D1600" · LB10D1600: "LB10D1600" · LB12.5D1600: "LB12.5D1600" · LB15D1600: "LB15D1600" · LB20D1600: "LB20D1600" · LB25D1600: "LB25D1600" · LB30D1600: "LB30D1600" · LB35D1600: "LB35D1600" · LB5D1800: "LB5D1800" · LB7.5D1800: "LB7.5D1800" · LB10D1800: "LB10D1800" · LB12.5D1800: "LB12.5D1800" · LB15D1800: "LB15D1800" · LB20D1800: "LB20D1800" · LB25D1800: "LB25D1800" · LB30D1800: "LB30D1800" · LB35D1800: "LB35D1800" · LB40D1800: "LB40D1800" · LB7.5D2000: "LB7.5D2000" · LB10D2000: "LB10D2000" · LB12.5D2000: "LB12.5D2000" · LB15D2000: "LB15D2000" · LB20D2000: "LB20D2000" · LB25D2000: "LB25D2000" · LB30D2000: "LB30D2000" · LB35D2000: "LB35D2000" · LB40D2000: "LB40D2000" · CB1.5D500: "CB1.5D500" · CB1.5D600: "CB1.5D600" · CB2D600: "CB2D600" · CB2.5D600: "CB2.5D600" · CB1.5D700: "CB1.5D700" · CB2D700: "CB2D700" · CB2.5D700: "CB2.5D700" · CB3.5D700: "CB3.5D700" · CB2.5D800: "CB2.5D800" · CB3.5D800: "CB3.5D800" · CB5D800: "CB5D800" · CB3.5D900: "CB3.5D900" · CB5D900: "CB5D900" · CB7.5D900: "CB7.5D900" · CB5D1000: "CB5D1000" · CB7.5D1000: "CB7.5D1000" · CB10D1000: "CB10D1000" · CB7.5D1100: "CB7.5D1100" · CB10D1100: "CB10D1100" · CB12.5D1100: "CB12.5D1100" · CB15D1100: "CB15D1100" · CB10D1200: "CB10D1200" · CB12.5D1200: "CB12.5D1200" · CB15D1200: "CB15D1200" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "TS(RC)"] Grade · C16: "C16" · C18: "C18" · C20: "C20" · C25: "C25" · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "NBR 6118(RC)"] Grade · C20BD: "C20BD" · C20GG: "C20GG" · C20LS: "C20LS" · C20SS: "C20SS" · C25BD: "C25BD" · C25GG: "C25GG" · C25LS: "C25LS" · C25SS: "C25SS" · C30BD: "C30BD" · C30GG: "C30GG" · C30LS: "C30LS" · C30SS: "C30SS" · C35BD: "C35BD" · C35GG: "C35GG" · C35LS: "C35LS" · C35SS: "C35SS" · C40BD: "C40BD" · C40GG: "C40GG" · C40LS: "C40LS" · C40SS: "C40SS" · C45BD: "C45BD" · C45GG: "C45GG" · C45LS: "C45LS" · C45SS: "C45SS" · C50BD: "C50BD" · C50GG: "C50GG" · C50LS: "C50LS" · C50SS: "C50SS" · C55BD: "C55BD" · C55GG: "C55GG" · C55LS: "C55LS" · C55SS: "C55SS" · C60BD: "C60BD" · C60GG: "C60GG" · C60LS: "C60LS" · C60SS: "C60SS" · C65BD: "C65BD" · C65GG: "C65GG" · C65LS: "C65LS" · C65SS: "C65SS" · C70BD: "C70BD" · C70GG: "C70GG" · C70LS: "C70LS" · C70SS: "C70SS" · C75BD: "C75BD" · C75GG: "C75GG" · C75LS: "C75LS" · C75SS: "C75SS" · C80BD: "C80BD" · C80GG: "C80GG" · C80LS: "C80LS" · C80SS: "C80SS" · C85BD: "C85BD" · C85GG: "C85GG" · C85LS: "C85LS" · C85SS: "C85SS" · C90BD: "C90BD" · C90GG: "C90GG" · C90LS: "C90LS" · C90SS: "C90SS" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "TCVN2018(RC)"] Grade · B3.5: "B3.5" · B5: "B5" · B7.5: "B7.5" · B10: "B10" · B12.5: "B12.5" · B15: "B15" · B20: "B20" · B25: "B25" · B30: "B30" · B35: "B35" · B40: "B40" · B45: "B45" · B50: "B50" · B55: "B55" · B60: "B60" · B70: "B70" · B80: "B80" · B90: "B90" · B100: "B100" | `"GRADE"` | string | - | **Required** |
| 4.3 | └ [When CODE = "CSA-S6-25(RC)"] Grade · C30: "C30" · C35: "C35" · C40: "C40" · C45: "C45" · C50: "C50" · C55: "C55" · C60: "C60" · C65: "C65" · C70: "C70" · C75: "C75" · C80: "C80" · C85: "C85" | `"GRADE"` | string | - | **Required** |
| 4.4 | └ [When CODE = "None"] Specified Compressive Strength (fc\|fck) · Minimum: 0 | `"COMP_STRENGTH"` | number | - | **Required** |
| 4.5 | └ [When CODE = "None"] Light Weight Concrete Factor | `"LIGHT_WEIGHT_FACTOR"` | boolean | - | Optional |
| 4.6 | └ [When LIGHT_WEIGHT_FACTOR = true] Light Weight Factor Value · Range: 0.75~1 | `"FACTOR_VALUE"` | number | - | **Required** |
| 5 | Slab Rebar Selection | `"SLAB_REBAR_PROP"` | object | - | **Required** |
| 5.1 | └ Code · None: "None" · ASTM19(RC): "ASTM19(RC)" · ASTM(RC): "ASTM(RC)" · U.S.C(US)(RC): "U.S.C(US)(RC)" · U.S.C(SI)(RC): "U.S.C(SI)(RC)" · NMX2023(RC): "NMX2023(RC)" · NMX2023(MKS)(RC): "NMX2023(MKS)(RC)" · NMX NTC-2017(RC): "NMX NTC-2017(RC)" · CSA(RC): "CSA(RC)" · BS(RC): "BS(RC)" · EN04(RC): "EN04(RC)" · EN(RC): "EN(RC)" · NTC08(RC): "NTC08(RC)" · NTC12(RC): "NTC12(RC)" · NTC18(RC): "NTC18(RC)" · UNI(RC): "UNI(RC)" · SS(RC): "SS(RC)" · GOST-SP(RC): "GOST-SP(RC)" · GOST-SNIP(RC): "GOST-SNIP(RC)" · JIS(RC): "JIS(RC)" · JIS-Civil(RC): "JIS-Civil(RC)" · JTJ023-85(RC): "JTJ023-85(RC)" · Q/CR 9300-18(RC): "Q/CR 9300-18(RC)" · GB 50917-13(RC): "GB 50917-13(RC)" · GB/T10(RC): "GB/T10(RC)" · GB(RC): "GB(RC)" · GB-Civil(RC): "GB-Civil(RC)" · TB10092-17(RC): "TB10092-17(RC)" · JTG3362-18(RC): "JTG3362-18(RC)" · JTG04(RC): "JTG04(RC)" · TB05(RC): "TB05(RC)" · KS19(RC): "KS19(RC)" · KS01(RC): "KS01(RC)" · KS(RC): "KS(RC)" · KSCE-LSD15(RC): "KSCE-LSD15(RC)" · KS01-Civil(RC): "KS01-Civil(RC)" · KS-Civil(RC): "KS-Civil(RC)" · PNS49(RC): "PNS49(RC)" · SNI(RC): "SNI(RC)" · TIS(RC): "TIS(RC)" · TIS(MKS)(RC): "TIS(MKS)(RC)" · IRC(RC): "IRC(RC)" · IRS(RC): "IRS(RC)" · IS(RC): "IS(RC)" · CNS560-18(RC): "CNS560-18(RC)" · CNS560(RC): "CNS560(RC)" · CNS(RC): "CNS(RC)" · AS17(RC): "AS17(RC)" · TMH7(RC): "TMH7(RC)" · SP63.2018(RC): "SP63.2018(RC)" · TS(RC): "TS(RC)" · NBR 6118(RC): "NBR 6118(RC)" · TCVN2018(RC): "TCVN2018(RC)" · CSA-S6-25(RC): "CSA-S6-25(RC)" | `"CODE"` | string | - | **Required** |
| 5.2 | └ [When CODE = "ASTM19(RC)"] Grade of Main Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "ASTM19(RC)"] Grade of Sub-Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "ASTM(RC)"] Grade of Main Rebar · Grade 40: "Grade 40" · Grade 50: "Grade 50" · Grade 60: "Grade 60" · Grade 75: "Grade 75" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "ASTM(RC)"] Grade of Sub-Rebar · Grade 40: "Grade 40" · Grade 50: "Grade 50" · Grade 60: "Grade 60" · Grade 75: "Grade 75" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "U.S.C(US)(RC)"] Grade of Main Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 75: "Grade 75" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "U.S.C(US)(RC)"] Grade of Sub-Rebar · Grade 40: "Grade 40" · Grade 60: "Grade 60" · Grade 75: "Grade 75" · Grade 80: "Grade 80" · Grade 100: "Grade 100" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "U.S.C(SI)(RC)"] Grade of Main Rebar · Grade 280: "Grade 280" · Grade 420: "Grade 420" · Grade 520: "Grade 520" · Grade 550: "Grade 550" · Grade 690: "Grade 690" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "U.S.C(SI)(RC)"] Grade of Sub-Rebar · Grade 280: "Grade 280" · Grade 420: "Grade 420" · Grade 520: "Grade 520" · Grade 550: "Grade 550" · Grade 690: "Grade 690" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)", "NMX NTC-2017(RC)"]] Grade of Main Rebar · Grade 42: "Grade 42" · Grade 56: "Grade 56" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["NMX2023(RC)", "NMX2023(MKS)(RC)", "NMX NTC-2017(RC)"]] Grade of Sub-Rebar · Grade 42: "Grade 42" · Grade 56: "Grade 56" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "CSA(RC)"] Grade of Main Rebar · 300R: "300R" · 400R: "400R" · 500R: "500R" · 400W: "400W" · 500W: "500W" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "CSA(RC)"] Grade of Sub-Rebar · 300R: "300R" · 400R: "400R" · 500R: "500R" · 400W: "400W" · 500W: "500W" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "BS(RC)"] Grade of Main Rebar · S250: "S250" · S460: "S460" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "BS(RC)"] Grade of Sub-Rebar · S250: "S250" · S460: "S460" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Grade of Main Rebar · Class A: "Class A" · Class B: "Class B" · Class C: "Class C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["EN04(RC)", "SS(RC)"]] Grade of Sub-Rebar · Class A: "Class A" · Class B: "Class B" · Class C: "Class C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "EN(RC)"] Grade of Main Rebar · S220: "S220" · S250: "S250" · S300: "S300" · S400: "S400" · S460: "S460" · S500: "S500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "EN(RC)"] Grade of Sub-Rebar · S220: "S220" · S250: "S250" · S300: "S300" · S400: "S400" · S460: "S460" · S500: "S500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Grade of Main Rebar · B450C: "B450C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["NTC08(RC)", "NTC12(RC)", "NTC18(RC)"]] Grade of Sub-Rebar · B450C: "B450C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "UNI(RC)"] Grade of Main Rebar · FeB22k: "FeB22k" · FeB32k: "FeB32k" · FeB38k: "FeB38k" · FeB44k: "FeB44k" · B450C: "B450C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "UNI(RC)"] Grade of Sub-Rebar · FeB22k: "FeB22k" · FeB32k: "FeB32k" · FeB38k: "FeB38k" · FeB44k: "FeB44k" · B450C: "B450C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "GOST-SP(RC)"] Grade of Main Rebar · A240: "A240" · A300: "A300" · A400: "A400" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "GOST-SP(RC)"] Grade of Sub-Rebar · A240: "A240" · A300: "A300" · A400: "A400" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "GOST-SNIP(RC)"] Grade of Main Rebar · A-I: "A-I" · A-II: "A-II" · A-III: "A-III" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "GOST-SNIP(RC)"] Grade of Sub-Rebar · A-I: "A-I" · A-II: "A-II" · A-III: "A-III" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "JIS(RC)"] Grade of Main Rebar · SR235: "SR235" · SR295: "SR295" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "JIS(RC)"] Grade of Sub-Rebar · SR235: "SR235" · SR295: "SR295" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "JIS-Civil(RC)"] Grade of Main Rebar · SR235: "SR235" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "JIS-Civil(RC)"] Grade of Sub-Rebar · SR235: "SR235" · SD295A: "SD295A" · SD295B: "SD295B" · SD345: "SD345" · SD390: "SD390" · SD490: "SD490" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["JTJ023-85(RC)", "GB-Civil(RC)"]] Grade of Main Rebar · Grade 1: "Grade 1" · Grade 2: "Grade 2" · Grade 3: "Grade 3" · 5 Hao: "5 Hao" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["JTJ023-85(RC)", "GB-Civil(RC)"]] Grade of Sub-Rebar · Grade 1: "Grade 1" · Grade 2: "Grade 2" · Grade 3: "Grade 3" · 5 Hao: "5 Hao" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRB500: "HRB500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["Q/CR 9300-18(RC)", "TB10092-17(RC)"]] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRB500: "HRB500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "GB 50917-13(RC)"] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "GB 50917-13(RC)"] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "GB/T10(RC)"] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" · RRB500: "RRB500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "GB/T10(RC)"] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" · HRBF500: "HRBF500" · RRB500: "RRB500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "GB(RC)"] Grade of Main Rebar · HPB235: "HPB235" · HRB335: "HRB335" · HRB400: "HRB400" · RRB400: "RRB400" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "GB(RC)"] Grade of Sub-Rebar · HPB235: "HPB235" · HRB335: "HRB335" · HRB400: "HRB400" · RRB400: "RRB400" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "JTG3362-18(RC)"] Grade of Main Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "JTG3362-18(RC)"] Grade of Sub-Rebar · HPB300: "HPB300" · HRB400: "HRB400" · HRBF400: "HRBF400" · RRB400: "RRB400" · HRB500: "HRB500" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "JTG04(RC)"] Grade of Main Rebar · R235: "R235" · HRB335: "HRB335" · HRB400: "HRB400" · KL400: "KL400" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "JTG04(RC)"] Grade of Sub-Rebar · R235: "R235" · HRB335: "HRB335" · HRB400: "HRB400" · KL400: "KL400" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "TB05(RC)"] Grade of Main Rebar · Q235: "Q235" · HRB335: "HRB335" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "TB05(RC)"] Grade of Sub-Rebar · Q235: "Q235" · HRB335: "HRB335" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "KS19(RC)"] Grade of Main Rebar · SD300: "SD300" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" · SD700: "SD700" · SD400S: "SD400S" · SD500S: "SD500S" · SD600S: "SD600S" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "KS19(RC)"] Grade of Sub-Rebar · SD300: "SD300" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" · SD700: "SD700" · SD400S: "SD400S" · SD500S: "SD500S" · SD600S: "SD600S" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["KS01(RC)", "KSCE-LSD15(RC)", "KS01-Civil(RC)"]] Grade of Main Rebar · SD240: "SD240" · SD300: "SD300" · SD350: "SD350" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["KS01(RC)", "KSCE-LSD15(RC)", "KS01-Civil(RC)"]] Grade of Sub-Rebar · SD240: "SD240" · SD300: "SD300" · SD350: "SD350" · SD400: "SD400" · SD500: "SD500" · SD600: "SD600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Grade of Main Rebar · SD24: "SD24" · SD30: "SD30" · SD35: "SD35" · SD40: "SD40" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["KS(RC)", "KS-Civil(RC)"]] Grade of Sub-Rebar · SD24: "SD24" · SD30: "SD30" · SD35: "SD35" · SD40: "SD40" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "PNS49(RC)"] Grade of Main Rebar · 230R: "230R" · 280R: "280R" · 420R: "420R" · 520R: "520R" · 550R: "550R" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "PNS49(RC)"] Grade of Sub-Rebar · 230R: "230R" · 280R: "280R" · 420R: "420R" · 520R: "520R" · 550R: "550R" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "SNI(RC)"] Grade of Main Rebar · BjTP 280: "BjTP 280" · BjTS 280: "BjTS 280" · BjTS 420A: "BjTS 420A" · BjTS 420B: "BjTS 420B" · BjTS 520: "BjTS 520" · BjTS 550: "BjTS 550" · BjTS 700: "BjTS 700" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "SNI(RC)"] Grade of Sub-Rebar · BjTP 280: "BjTP 280" · BjTS 280: "BjTS 280" · BjTS 420A: "BjTS 420A" · BjTS 420B: "BjTS 420B" · BjTS 520: "BjTS 520" · BjTS 550: "BjTS 550" · BjTS 700: "BjTS 700" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Grade of Main Rebar · SR24: "SR24" · SD30: "SD30" · SD40: "SD40" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["TIS(RC)", "TIS(MKS)(RC)"]] Grade of Sub-Rebar · SR24: "SR24" · SD30: "SD30" · SD40: "SD40" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE in ["IRC(RC)", "IRS(RC)"]] Grade of Main Rebar · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE in ["IRC(RC)", "IRS(RC)"]] Grade of Sub-Rebar · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "IS(RC)"] Grade of Main Rebar · Fe240: "Fe240" · Fe250: "Fe250" · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "IS(RC)"] Grade of Sub-Rebar · Fe240: "Fe240" · Fe250: "Fe250" · Fe415: "Fe415" · Fe500: "Fe500" · Fe550: "Fe550" · Fe600: "Fe600" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "CNS560-18(RC)"] Grade of Main Rebar · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490W: "SD490W" · SD550W: "SD550W" · SD690: "SD690" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "CNS560-18(RC)"] Grade of Sub-Rebar · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490W: "SD490W" · SD550W: "SD550W" · SD690: "SD690" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "CNS560(RC)"] Grade of Main Rebar · SR240: "SR240" · SR300: "SR300" · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490: "SD490" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "CNS560(RC)"] Grade of Sub-Rebar · SR240: "SR240" · SR300: "SR300" · SD280: "SD280" · SD280W: "SD280W" · SD420: "SD420" · SD420W: "SD420W" · SD490: "SD490" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "CNS(RC)"] Grade of Main Rebar · SD24: "SD24" · SD28: "SD28" · SD30: "SD30" · SD35: "SD35" · SD42: "SD42" · SD42W: "SD42W" · SD50: "SD50" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "CNS(RC)"] Grade of Sub-Rebar · SD24: "SD24" · SD28: "SD28" · SD30: "SD30" · SD35: "SD35" · SD42: "SD42" · SD42W: "SD42W" · SD50: "SD50" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "AS17(RC)"] Grade of Main Rebar · D500L: "D500L" · D500N: "D500N" · D500E: "D500E" · D500LP: "D500LP" · D600N: "D600N" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "AS17(RC)"] Grade of Sub-Rebar · D500L: "D500L" · D500N: "D500N" · D500E: "D500E" · D500LP: "D500LP" · D600N: "D600N" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "TMH7(RC)"] Grade of Main Rebar · Type A: "Type A" · Type B: "Type B" · Type C: "Type C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "TMH7(RC)"] Grade of Sub-Rebar · Type A: "Type A" · Type B: "Type B" · Type C: "Type C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "SP63.2018(RC)"] Grade of Main Rebar · A240: "A240" · A240_sw: "A240_sw" · A400: "A400" · A400_sw: "A400_sw" · A500: "A500" · A500_sw: "A500_sw" · A600: "A600" · A800: "A800" · A1000: "A1000" · B500: "B500" · B500_sw: "B500_sw" · BP500: "BP500" · BP1200: "BP1200" · BP1300: "BP1300" · BP1400: "BP1400" · BP1500: "BP1500" · BP1600: "BP1600" · K1400: "K1400" · K1450: "K1450" · K1500: "K1500" · K1550: "K1550" · K1650: "K1650" · K1750: "K1750" · K1850: "K1850" · K1900: "K1900" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "SP63.2018(RC)"] Grade of Sub-Rebar · A240: "A240" · A240_sw: "A240_sw" · A400: "A400" · A400_sw: "A400_sw" · A500: "A500" · A500_sw: "A500_sw" · A600: "A600" · A800: "A800" · A1000: "A1000" · B500: "B500" · B500_sw: "B500_sw" · BP500: "BP500" · BP1200: "BP1200" · BP1300: "BP1300" · BP1400: "BP1400" · BP1500: "BP1500" · BP1600: "BP1600" · K1400: "K1400" · K1450: "K1450" · K1500: "K1500" · K1550: "K1550" · K1650: "K1650" · K1750: "K1750" · K1850: "K1850" · K1900: "K1900" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "TS(RC)"] Grade of Main Rebar · B420C: "B420C" · B520C: "B520C" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "TS(RC)"] Grade of Sub-Rebar · B420C: "B420C" · B520C: "B520C" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "NBR 6118(RC)"] Grade of Main Rebar · CA25: "CA25" · CA50: "CA50" · CA60: "CA60" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "NBR 6118(RC)"] Grade of Sub-Rebar · CA25: "CA25" · CA50: "CA50" · CA60: "CA60" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "TCVN2018(RC)"] Grade of Main Rebar · CB300-V: "CB300-V" · CB400-V: "CB400-V" · CB500-V: "CB500-V" · CB600-V: "CB600-V" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "TCVN2018(RC)"] Grade of Sub-Rebar · CB300-V: "CB300-V" · CB400-V: "CB400-V" · CB500-V: "CB500-V" · CB600-V: "CB600-V" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.2 | └ [When CODE = "CSA-S6-25(RC)"] Grade of Main Rebar · 400W: "400W" · 500W: "500W" · 600W: "600W" | `"GRADE_MAIN_REBAR"` | string | - | **Required** |
| 5.3 | └ [When CODE = "CSA-S6-25(RC)"] Grade of Sub-Rebar · 400W: "400W" · 500W: "500W" · 600W: "600W" | `"GRADE_SUB_REBAR"` | string | - | **Required** |
| 5.4 | └ [When CODE = "None"] Name of Main Rebar | `"NAME_MAIN_REBAR"` | string | - | **Required** |
| 5.5 | └ [When CODE = "None"] Name of Sub-Rebar | `"NAME_SUB_REBAR"` | string | - | **Required** |
| 5.6 | └ [When CODE = "None"] Fy · Minimum: 0 | `"Fy"` | number | - | **Required** |
| 5.7 | └ [When CODE = "None"] Fys · Minimum: 0 | `"Fys"` | number | - | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a concrete material ID (e.g., \"1\"). Only concrete (type C) materials are serviced.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "GIRDER_MATL_PROP",
            "GIRDER_REBAR_PROP"
          ],
          "additionalProperties": false,
          "properties": {
            "GIRDER_MATL_PROP": {
              "title": "Girder Material Type",
              "description": "Girder Material Type settings reused from design-input/modify-material-concrete.",
              "type": "object",
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
                  "description": "Light Weight Factor value. Required when CODE is 'None' and LIGHT_WEIGHT_FACTOR is true.",
                  "minimum": 0.75,
                  "maximum": 1,
                  "visibleWhen": {
                    "LIGHT_WEIGHT_FACTOR": true
                  }
                }
              }
            },
            "GIRDER_REBAR_PROP": {
              "title": "Girder Rebar Selection",
              "description": "Girder Rebar Selection settings reused from design-input/modify-material-rebar.",
              "type": "object",
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
              "description": "Whether to apply slab material and rebar properties. When true, SLAB_MATL_PROP and SLAB_REBAR_PROP are required. Applied only for PSC composite sections; ignored otherwise.",
              "default": false
            },
            "SLAB_MATL_PROP": {
              "title": "Slab Material Type",
              "description": "Slab Material Type settings reused from design-input/modify-material-concrete.",
              "type": "object",
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
                  "description": "Light Weight Factor value. Required when CODE is 'None' and LIGHT_WEIGHT_FACTOR is true.",
                  "minimum": 0.75,
                  "maximum": 1,
                  "visibleWhen": {
                    "LIGHT_WEIGHT_FACTOR": true
                  }
                }
              }
            },
            "SLAB_REBAR_PROP": {
              "title": "Slab Rebar Selection",
              "description": "Slab Rebar Selection settings reused from design-input/modify-material-rebar.",
              "type": "object",
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
        "COMP_STRENGTH": 27579038,
        "LIGHT_WEIGHT_FACTOR": false
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "None",
        "NAME_MAIN_REBAR": "User-Gr60",
        "NAME_SUB_REBAR": "User-Gr40",
        "Fy": 413685473,
        "Fys": 275790316
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
        "COMP_STRENGTH": 27579038.0
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "None",
        "NAME_MAIN_REBAR": "User-Gr60",
        "NAME_SUB_REBAR": "User-Gr40",
        "Fy": 413685473.0,
        "Fys": 275790316.0
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/MATD"

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
        "COMP_STRENGTH": 27579038,
        "LIGHT_WEIGHT_FACTOR": false
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "None",
        "NAME_MAIN_REBAR": "User-Gr60",
        "NAME_SUB_REBAR": "User-Gr40",
        "Fy": 413685473,
        "Fys": 275790316
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

## 12. `DFRC` — Define Rating Case

> **기능** 평가 케이스를 정의합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/DFRC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 58412610890137](https://support.midasuser.com/hc/en-us/articles/58412610890137)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a rating case ID (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Name of Rating Case | `"NAME"` | string | - | **Required** |
| 2 | [General] Description | `"DESC"` | string |  | Optional |
| 3 | [General] Limit State · Service Limit State: 0 · Strength Limit State: 1 | `"LIMIT_STATE"` | integer | 0 | **Required** |
| 4 | [General] Primary Vehicle | `"PRIMARY_VEH"` | object | - | **Required** |
| 4.1 | └ [General] Primary Vehicle | `"LOAD_CASE_NAME"` | string | - | **Required** |
| 4.2 | └ [General] Primary Vehicle Factor · Minimum: 0 | `"FACTOR"` | number | 1 | Optional |
| 5 | [General] Adjacent Vehicle | `"ADJACENT_VEH"` | object | - | **Required** |
| 5.1 | └ [General] Adjacent Vehicle | `"LOAD_CASE_NAME"` | string | - | **Required** |
| 5.2 | └ [General] Adjacent Vehicle Factor · Minimum: 0 | `"FACTOR"` | number | 1 | Optional |
| 6 | [General] Evaluation Live Load Model · Design Live Load: 0 · Legal Load: 1 · Permit Load: 2 | `"EVAL_TYPE"` | integer | 0 | Optional |
| 7 | [General] Load Items - Service Limit State | `"LOAD_ITEMS_SER"` ¹⁾ | object | - | Optional |
| 8 | [General] Load Items - Strength Limit State | `"LOAD_ITEMS_STR"` ²⁾ | object | - | Optional |

**Load Items - Service Limit State ¹⁾**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | DC | `"DC"` | object | - | Optional |
| 1.1 | └ Factor | `"FACTOR"` | object | - | Optional |
| 1.1.1 | 　　└ max · Minimum: 0 | `"MAX"` | number | 1 | Optional |
| 1.1.2 | 　　└ min · Minimum: 0 | `"MIN"` | number | 1 | Optional |
| 1.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 2 | DW | `"DW"` | object | - | Optional |
| 2.1 | └ Factor | `"FACTOR"` | object | - | Optional |
| 2.1.1 | 　　└ max · Minimum: 0 | `"MAX"` | number | 1 | Optional |
| 2.1.2 | 　　└ min · Minimum: 0 | `"MIN"` | number | 1 | Optional |
| 2.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 3 | Temperature | `"TEMP"` | object | - | Optional |
| 3.1 | └ Factor · Minimum: 0 | `"FACTOR"` | number | 1 | Optional |
| 3.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 4 | T. Gradient | `"TGRADIENT"` | object | - | Optional |
| 4.1 | └ Factor · Minimum: 0 | `"FACTOR"` | number | 1 | Optional |
| 4.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 5 | Secondary | `"SECONDARY"` | object | - | Optional |
| 5.1 | └ Factor · Minimum: 0 | `"FACTOR"` | number | 1 | Optional |
| 5.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 6 | Permanent | `"PERMANENT"` | object | - | Optional |
| 6.1 | └ Factor · Minimum: 0 | `"FACTOR"` | number | 1 | Optional |
| 6.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 7 | User Defined | `"USER_DEFINED"` | object | - | Optional |
| 7.1 | └ Factor · Minimum: 0 | `"FACTOR"` | number | 1 | Optional |
| 7.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |

**Load Items - Strength Limit State ²⁾**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | DC | `"DC"` | object | - | Optional |
| 1.1 | └ Factor | `"FACTOR"` | object | - | Optional |
| 1.1.1 | 　　└ max · Minimum: 0 | `"MAX"` | number | 1.25 | Optional |
| 1.1.2 | 　　└ min · Minimum: 0 | `"MIN"` | number | 0.9 | Optional |
| 1.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 2 | DW | `"DW"` | object | - | Optional |
| 2.1 | └ Factor | `"FACTOR"` | object | - | Optional |
| 2.1.1 | 　　└ max · Minimum: 0 | `"MAX"` | number | 1.5 | Optional |
| 2.1.2 | 　　└ min · Minimum: 0 | `"MIN"` | number | 0.9 | Optional |
| 2.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 3 | Temperature | `"TEMP"` | object | - | Optional |
| 3.1 | └ Factor · Minimum: 0 | `"FACTOR"` | number | 1 | Optional |
| 3.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 4 | T. Gradient | `"TGRADIENT"` | object | - | Optional |
| 4.1 | └ Factor · Minimum: 0 | `"FACTOR"` | number | 1 | Optional |
| 4.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 5 | Secondary | `"SECONDARY"` | object | - | Optional |
| 5.1 | └ Factor · Minimum: 0 | `"FACTOR"` | number | 1 | Optional |
| 5.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 6 | Permanent | `"PERMANENT"` | object | - | Optional |
| 6.1 | └ Factor · Minimum: 0 | `"FACTOR"` | number | 1.25 | Optional |
| 6.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |
| 7 | User Defined | `"USER_DEFINED"` | object | - | Optional |
| 7.1 | └ Factor · Minimum: 0 | `"FACTOR"` | number | 1.25 | Optional |
| 7.2 | └ Load Cases | `"LOAD_CASES"` | array | - | Optional |

### JSON Schema

```json
{
  "type": "object",
  "description": "Define PSC rating case (DFRC) data. Supported methods: POST, GET, PUT, DELETE.",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is a rating case ID (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "DFRC",
          "type": "object",
          "description": "PSC rating case definition mapped to the DFRC body. LOAD_ITEMS is split into Service and Strength variants according to LIMIT_STATE.",
          "required": [
            "NAME",
            "LIMIT_STATE",
            "PRIMARY_VEH",
            "ADJACENT_VEH"
          ],
          "additionalProperties": false,
          "properties": {
            "NAME": {
              "type": "string",
              "description": "Rating case name.",
              "minLength": 1
            },
            "DESC": {
              "type": "string",
              "description": "Description.",
              "default": ""
            },
            "LIMIT_STATE": {
              "type": "integer",
              "description": "Rating limit state.",
              "enum": [
                0,
                1
              ],
              "default": 0
            },
            "PRIMARY_VEH": {
              "type": "object",
              "description": "Primary vehicle live load case and rating factor.",
              "required": [
                "LOAD_CASE_NAME"
              ],
              "additionalProperties": false,
              "properties": {
                "LOAD_CASE_NAME": {
                  "type": "string",
                  "description": "Primary vehicle moving load case name, including suffix such as (MV).",
                  "minLength": 1
                },
                "FACTOR": {
                  "type": "number",
                  "description": "Primary vehicle factor.",
                  "default": 1,
                  "minimum": 0
                }
              }
            },
            "ADJACENT_VEH": {
              "type": "object",
              "description": "Adjacent vehicle live load case and rating factor.",
              "required": [
                "LOAD_CASE_NAME"
              ],
              "additionalProperties": false,
              "properties": {
                "LOAD_CASE_NAME": {
                  "type": "string",
                  "description": "Adjacent vehicle moving load case name, including suffix such as (MV).",
                  "minLength": 1
                },
                "FACTOR": {
                  "type": "number",
                  "description": "Adjacent vehicle factor.",
                  "default": 1,
                  "minimum": 0
                }
              }
            },
            "EVAL_TYPE": {
              "type": "integer",
              "description": "Evaluation live load model. Permit Load is used by LRFR19 rating code.",
              "enum": [
                0,
                1,
                2
              ],
              "default": 0
            },
            "LOAD_ITEMS_SER": {
              "type": "object",
              "description": "Service limit state rating load items. Use only when LIMIT_STATE is 0 (LOAD_ITEMS_STR is ignored). Defaults (all 1.00) apply when a rating case is created or its LIMIT_STATE is changed; otherwise omitted items keep their stored values.",
              "additionalProperties": false,
              "properties": {
                "DC": {
                  "type": "object",
                  "description": "Dead load component rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "object",
                      "description": "DC max/min rating factors.",
                      "additionalProperties": false,
                      "properties": {
                        "MAX": {
                          "type": "number",
                          "description": "Maximum DC rating factor.",
                          "default": 1,
                          "minimum": 0
                        },
                        "MIN": {
                          "type": "number",
                          "description": "Minimum DC rating factor.",
                          "default": 1,
                          "minimum": 0
                        }
                      }
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "DW": {
                  "type": "object",
                  "description": "Wearing surface and utility load component rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "object",
                      "description": "DW max/min rating factors.",
                      "additionalProperties": false,
                      "properties": {
                        "MAX": {
                          "type": "number",
                          "description": "Maximum DW rating factor.",
                          "default": 1,
                          "minimum": 0
                        },
                        "MIN": {
                          "type": "number",
                          "description": "Minimum DW rating factor.",
                          "default": 1,
                          "minimum": 0
                        }
                      }
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "TEMP": {
                  "type": "object",
                  "description": "Temperature rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "number",
                      "description": "Temperature rating factor.",
                      "default": 1,
                      "minimum": 0
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "TGRADIENT": {
                  "type": "object",
                  "description": "Temperature gradient rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "number",
                      "description": "T. Gradient rating factor.",
                      "default": 1,
                      "minimum": 0
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "SECONDARY": {
                  "type": "object",
                  "description": "Secondary load rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "number",
                      "description": "Secondary rating factor.",
                      "default": 1,
                      "minimum": 0
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "PERMANENT": {
                  "type": "object",
                  "description": "Permanent load rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "number",
                      "description": "Permanent rating factor.",
                      "default": 1,
                      "minimum": 0
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "USER_DEFINED": {
                  "type": "object",
                  "description": "User defined load rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "number",
                      "description": "User Defined rating factor.",
                      "default": 1,
                      "minimum": 0
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                }
              }
            },
            "LOAD_ITEMS_STR": {
              "type": "object",
              "description": "Strength limit state rating load items. Use only when LIMIT_STATE is 1 (LOAD_ITEMS_SER is ignored). Defaults (LRFR strength factors) apply when a rating case is created or its LIMIT_STATE is changed; otherwise omitted items keep their stored values.",
              "additionalProperties": false,
              "properties": {
                "DC": {
                  "type": "object",
                  "description": "Dead load component rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "object",
                      "description": "DC max/min rating factors.",
                      "additionalProperties": false,
                      "properties": {
                        "MAX": {
                          "type": "number",
                          "description": "Maximum DC rating factor.",
                          "default": 1.25,
                          "minimum": 0
                        },
                        "MIN": {
                          "type": "number",
                          "description": "Minimum DC rating factor.",
                          "default": 0.9,
                          "minimum": 0
                        }
                      }
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "DW": {
                  "type": "object",
                  "description": "Wearing surface and utility load component rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "object",
                      "description": "DW max/min rating factors.",
                      "additionalProperties": false,
                      "properties": {
                        "MAX": {
                          "type": "number",
                          "description": "Maximum DW rating factor.",
                          "default": 1.5,
                          "minimum": 0
                        },
                        "MIN": {
                          "type": "number",
                          "description": "Minimum DW rating factor.",
                          "default": 0.9,
                          "minimum": 0
                        }
                      }
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "TEMP": {
                  "type": "object",
                  "description": "Temperature rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "number",
                      "description": "Temperature rating factor.",
                      "default": 1,
                      "minimum": 0
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "TGRADIENT": {
                  "type": "object",
                  "description": "Temperature gradient rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "number",
                      "description": "T. Gradient rating factor.",
                      "default": 1,
                      "minimum": 0
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "SECONDARY": {
                  "type": "object",
                  "description": "Secondary load rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "number",
                      "description": "Secondary rating factor.",
                      "default": 1,
                      "minimum": 0
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "PERMANENT": {
                  "type": "object",
                  "description": "Permanent load rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "number",
                      "description": "Permanent rating factor.",
                      "default": 1.25,
                      "minimum": 0
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
                      }
                    }
                  }
                },
                "USER_DEFINED": {
                  "type": "object",
                  "description": "User defined load rating item.",
                  "additionalProperties": false,
                  "properties": {
                    "FACTOR": {
                      "type": "number",
                      "description": "User Defined rating factor.",
                      "default": 1.25,
                      "minimum": 0
                    },
                    "LOAD_CASES": {
                      "type": "array",
                      "description": "Load case names assigned to this rating load item, each written as name(TYPE), e.g. \"SW(ST)\". TYPE: ST, CS, RS, TH, MV, SM, CB. The load case must exist in the model.",
                      "items": {
                        "type": "string",
                        "minLength": 1,
                        "pattern": "^.+\\((ST|CS|RS|TH|MV|SM|CB)\\)$"
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

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `DFRC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "7": {
      "NAME": "Rating case",
      "DESC": "",
      "LIMIT_STATE": 1,
      "PRIMARY_VEH": {
        "LOAD_CASE_NAME": "MV(MV)",
        "FACTOR": 1.0
      },
      "ADJACENT_VEH": {
        "LOAD_CASE_NAME": "MV(MV)",
        "FACTOR": 1.0
      },
      "EVAL_TYPE": 2,
      "LOAD_ITEMS_STR": {
        "DC": {
          "FACTOR": {
            "MAX": 1.25,
            "MIN": 0.9
          },
          "LOAD_CASES": [
            "Dead Load(CS)"
          ]
        },
        "DW": {
          "FACTOR": {
            "MAX": 1.5,
            "MIN": 0.9
          },
          "LOAD_CASES": []
        },
        "TEMP": {
          "FACTOR": 1.0,
          "LOAD_CASES": []
        },
        "TGRADIENT": {
          "FACTOR": 1.0,
          "LOAD_CASES": []
        },
        "SECONDARY": {
          "FACTOR": 1.0,
          "LOAD_CASES": []
        },
        "PERMANENT": {
          "FACTOR": 1.25,
          "LOAD_CASES": []
        },
        "USER_DEFINED": {
          "FACTOR": 1.25,
          "LOAD_CASES": []
        }
      }
    }
  }
}
```

**Response**

```json
{
  "DFRC": {
    "7": {
      "NAME": "Rating case",
      "DESC": "",
      "LIMIT_STATE": 1,
      "PRIMARY_VEH": {
        "LOAD_CASE_NAME": "MV(MV)",
        "FACTOR": 1.0
      },
      "ADJACENT_VEH": {
        "LOAD_CASE_NAME": "MV(MV)",
        "FACTOR": 1.0
      },
      "EVAL_TYPE": 2,
      "LOAD_ITEMS_STR": {
        "DC": {
          "FACTOR": {
            "MAX": 1.25,
            "MIN": 0.9
          },
          "LOAD_CASES": [
            "Dead Load(CS)"
          ]
        },
        "DW": {
          "FACTOR": {
            "MAX": 1.5,
            "MIN": 0.9
          },
          "LOAD_CASES": []
        },
        "TEMP": {
          "FACTOR": 1.0,
          "LOAD_CASES": []
        },
        "TGRADIENT": {
          "FACTOR": 1.0,
          "LOAD_CASES": []
        },
        "SECONDARY": {
          "FACTOR": 1.0,
          "LOAD_CASES": []
        },
        "PERMANENT": {
          "FACTOR": 1.25,
          "LOAD_CASES": []
        },
        "USER_DEFINED": {
          "FACTOR": 1.25,
          "LOAD_CASES": []
        }
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/DFRC"

payload = json.loads(r'''
{
  "Assign": {
    "7": {
      "NAME": "Rating case",
      "DESC": "",
      "LIMIT_STATE": 1,
      "PRIMARY_VEH": {
        "LOAD_CASE_NAME": "MV(MV)",
        "FACTOR": 1.0
      },
      "ADJACENT_VEH": {
        "LOAD_CASE_NAME": "MV(MV)",
        "FACTOR": 1.0
      },
      "EVAL_TYPE": 2,
      "LOAD_ITEMS_STR": {
        "DC": {
          "FACTOR": {
            "MAX": 1.25,
            "MIN": 0.9
          },
          "LOAD_CASES": [
            "Dead Load(CS)"
          ]
        },
        "DW": {
          "FACTOR": {
            "MAX": 1.5,
            "MIN": 0.9
          },
          "LOAD_CASES": []
        },
        "TEMP": {
          "FACTOR": 1.0,
          "LOAD_CASES": []
        },
        "TGRADIENT": {
          "FACTOR": 1.0,
          "LOAD_CASES": []
        },
        "SECONDARY": {
          "FACTOR": 1.0,
          "LOAD_CASES": []
        },
        "PERMANENT": {
          "FACTOR": 1.25,
          "LOAD_CASES": []
        },
        "USER_DEFINED": {
          "FACTOR": 1.25,
          "LOAD_CASES": []
        }
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

## 13. `RTGS` — Rating Group Setting

> **기능** 평가 그룹을 설정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/RTGS
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738356812057](https://support.midasuser.com/hc/en-us/articles/64738356812057)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a structure group ID. It must be the ID of the group named in GROUP (e.g., "1" for the group whose ID is 1). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Selected Rating Group | `"GROUP"` | string | - | **Required** |
| 2 | [General] Check Position · I-End: 0 · J-End: 1 · All: 2 | `"POSITION"` | integer | - | **Required** |
| 3 | [General] Condition Factor · Range: 0~1 | `"FACTOR"` | number | 1 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a structure group ID. It must be the ID of the group named in GROUP (e.g., \"1\" for the group whose ID is 1).",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Rating Group Setting",
          "type": "object",
          "required": [
            "GROUP",
            "POSITION"
          ],
          "additionalProperties": false,
          "properties": {
            "GROUP": {
              "type": "string",
              "description": "Selected Rating Group. Name of a structure group that exists in the model; its group ID must equal the key.",
              "minLength": 1
            },
            "POSITION": {
              "type": "integer",
              "description": "Check Position",
              "enum": [
                0,
                1,
                2
              ]
            },
            "FACTOR": {
              "type": "number",
              "description": "Condition Factor",
              "default": 1,
              "exclusiveMinimum": 0,
              "maximum": 1
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

- `RTGS`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "5": {
      "GROUP": "Girder",
      "POSITION": 2,
      "FACTOR": 1.0
    },
    "12": {
      "GROUP": "10th Point Girder-1-i",
      "POSITION": 0,
      "FACTOR": 0.95
    },
    "13": {
      "GROUP": "10th Point Girder-1-j",
      "POSITION": 1,
      "FACTOR": 0.95
    }
  }
}
```

**Response**

```json
{
  "RTGS": {
    "5": {
      "GROUP": "Girder",
      "POSITION": 2,
      "FACTOR": 1.0
    },
    "12": {
      "GROUP": "10th Point Girder-1-i",
      "POSITION": 0,
      "FACTOR": 0.95
    },
    "13": {
      "GROUP": "10th Point Girder-1-j",
      "POSITION": 1,
      "FACTOR": 0.95
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/RTGS"

payload = json.loads(r'''
{
  "Assign": {
    "5": {
      "GROUP": "Girder",
      "POSITION": 2,
      "FACTOR": 1.0
    },
    "12": {
      "GROUP": "10th Point Girder-1-i",
      "POSITION": 0,
      "FACTOR": 0.95
    },
    "13": {
      "GROUP": "10th Point Girder-1-j",
      "POSITION": 1,
      "FACTOR": 0.95
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 14. `PFRO` — Position for Rating Output

> **기능** 평가 결과를 출력할 위치를 지정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/PFRO
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 58381791502873](https://support.midasuser.com/hc/en-us/articles/58381791502873)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element number (e.g., "1"). The element must exist in the model. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Position Type · I: 0 · J: 1 · I & J: 2 | `"PART"` | integer | 0 | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is an element number (e.g., \"1\"). The element must exist in the model.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "PART"
          ],
          "additionalProperties": false,
          "properties": {
            "PART": {
              "type": "integer",
              "description": "Part Type",
              "default": 0,
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

- `PFRO`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "166": {
      "PART": 0
    },
    "167": {
      "PART": 1
    },
    "168": {
      "PART": 2
    },
    "169": {
      "PART": 0
    }
  }
}
```

**Response**

```json
{
  "PFRO": {
    "166": {
      "PART": 0
    },
    "167": {
      "PART": 1
    },
    "168": {
      "PART": 2
    },
    "169": {
      "PART": 0
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/PFRO"

payload = json.loads(r'''
{
  "Assign": {
    "166": {
      "PART": 0
    },
    "167": {
      "PART": 1
    },
    "168": {
      "PART": 2
    },
    "169": {
      "PART": 0
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 15. `RPSC-ANAL` — Perform Rating

> **기능** PSC 내하력 평가를 실행합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/RPSC-ANAL
```

### Active Methods

`POST`

### Specifications

**원문** [영문 58381619465241](https://support.midasuser.com/hc/en-us/articles/58381619465241)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Perform Rating | `"TYPE"` | string | PERFORM_RATING | **Required** |

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
          "title": "Perform Rating",
          "type": "object",
          "required": [
            "TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "TYPE": {
              "type": "string",
              "description": "Perform Rating",
              "default": "PERFORM_RATING"
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

- `message`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "1": {
      "TYPE": "PERFORM_RATING"
    }
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/RPSC-ANAL"

payload = json.loads(r'''
{
  "Argument": {
    "1": {
      "TYPE": "PERFORM_RATING"
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 16. `TABLE` · `PSC_RATING_SVC_SUM_DGN` — Service Limit State Summary (Design Live, Legal)

> **기능** 설계 활하중 및 법정하중의 사용한계상태 평가 요약을 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738379883033](https://support.midasuser.com/hc/en-us/articles/64738379883033)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Service Limit State Summary (Design Live): "PSC_RATING_SVC_SUM_DGN" · Service Limit State Summary (Legal): "PSC_RATING_SVC_SUM_LEG" · Service Limit State Summary (Design Live) - Virtual Beam: "PSC_RATING_SVC_SUM_DGN_VBEAM" · Service Limit State Summary (Legal) - Virtual Beam: "PSC_RATING_SVC_SUM_LEG_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Rating Case | `"RATING_CASE"` | array | - | Optional |
| 4 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 5 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 5.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 5.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 5.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 5.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 6 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 6.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 6.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 7 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_SVC_SUM_DGN",
            "PSC_RATING_SVC_SUM_LEG",
            "PSC_RATING_SVC_SUM_DGN_VBEAM",
            "PSC_RATING_SVC_SUM_LEG_VBEAM"
          ]
        },
        "RATING_CASE": {
          "type": "array",
          "description": "Rating case name filter (names defined in Define Rating Case). Design Live tables list Service limit state cases with Design Live Load; Legal tables list Service limit state cases with Legal Load. If no listed case applies, the result is empty. Omit (or []) for all cases.",
          "items": {
            "type": "string"
          }
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Factor/Stress pairs are selected together (e.g. \"DC/Factor\" also returns \"DC/Stress\"). Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "RatingCase",
              "Component",
              "MinimumRatingFactor",
              "Location",
              "RelativeLocation",
              "Capacity",
              "Demand",
              "Point",
              "DC/Factor",
              "DC/Stress",
              "DW/Factor",
              "DW/Stress",
              "Temperature/Factor",
              "Temperature/Stress",
              "T.Gradient/Factor",
              "T.Gradient/Stress",
              "Permanent/Factor",
              "Permanent/Stress",
              "Secondary/Factor",
              "Secondary/Stress",
              "UserDefined/Factor",
              "UserDefined/Stress",
              "Pri.LL/Factor",
              "Pri.LL/Stress",
              "AdjLL/Factor",
              "AdjLL/Stress"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Service Limit State Summary (Design Live, Legal)` — `Index`, `RatingCase`, `Component`, `MinimumRatingFactor`, `Location`, `RelativeLocation`, `Capacity`, `Demand`, `Point`, `DC/Factor`, `DC/Stress`, `DW/Factor`, `DW/Stress`, `Temperature/Factor`, `Temperature/Stress`, `T.Gradient/Factor`, `T.Gradient/Stress`, `Permanent/Factor`, `Permanent/Stress`, `Secondary/Factor`, `Secondary/Stress`, `UserDefined/Factor`, `UserDefined/Stress`, `Pri.LL/Factor`, `Pri.LL/Stress`, `AdjLL/Factor`, `AdjLL/Stress`

### Request / Response JSON

**Request — PSC_RATING_SVC_SUM_DGN**

```json
{
  "Argument": {
    "TABLE_NAME": "Service Limit State Summary (Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_SVC_SUM_DGN",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "Component",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "Capacity",
      "Demand",
      "Point",
      "DC/Factor",
      "DC/Stress",
      "DW/Factor",
      "DW/Stress",
      "Temperature/Factor",
      "Temperature/Stress",
      "T.Gradient/Factor",
      "T.Gradient/Stress",
      "Permanent/Factor",
      "Permanent/Stress",
      "Secondary/Factor",
      "Secondary/Stress",
      "UserDefined/Factor",
      "UserDefined/Stress",
      "Pri.LL/Factor",
      "Pri.LL/Stress",
      "AdjLL/Factor",
      "AdjLL/Stress"
    ]
  }
}
```

**Request — PSC_RATING_SVC_SUM_LEG**

```json
{
  "Argument": {
    "TABLE_NAME": "Service Limit State Summary (Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_SVC_SUM_LEG",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "Component",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "Capacity",
      "Demand",
      "Point",
      "DC/Factor",
      "DC/Stress",
      "DW/Factor",
      "DW/Stress",
      "Temperature/Factor",
      "Temperature/Stress",
      "T.Gradient/Factor",
      "T.Gradient/Stress",
      "Permanent/Factor",
      "Permanent/Stress",
      "Secondary/Factor",
      "Secondary/Stress",
      "UserDefined/Factor",
      "UserDefined/Stress",
      "Pri.LL/Factor",
      "Pri.LL/Stress",
      "AdjLL/Factor",
      "AdjLL/Stress"
    ]
  }
}
```

**Request — PSC_RATING_SVC_SUM_DGN_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Service Limit State Summary (Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_SVC_SUM_DGN_VBEAM",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "Component",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "Capacity",
      "Demand",
      "Point",
      "DC/Factor",
      "DC/Stress",
      "DW/Factor",
      "DW/Stress",
      "Temperature/Factor",
      "Temperature/Stress",
      "T.Gradient/Factor",
      "T.Gradient/Stress",
      "Permanent/Factor",
      "Permanent/Stress",
      "Secondary/Factor",
      "Secondary/Stress",
      "UserDefined/Factor",
      "UserDefined/Stress",
      "Pri.LL/Factor",
      "Pri.LL/Stress",
      "AdjLL/Factor",
      "AdjLL/Stress"
    ]
  }
}
```

**Request — PSC_RATING_SVC_SUM_LEG_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Service Limit State Summary (Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_SVC_SUM_LEG_VBEAM",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "Component",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "Capacity",
      "Demand",
      "Point",
      "DC/Factor",
      "DC/Stress",
      "DW/Factor",
      "DW/Stress",
      "Temperature/Factor",
      "Temperature/Stress",
      "T.Gradient/Factor",
      "T.Gradient/Stress",
      "Permanent/Factor",
      "Permanent/Stress",
      "Secondary/Factor",
      "Secondary/Stress",
      "UserDefined/Factor",
      "UserDefined/Stress",
      "Pri.LL/Factor",
      "Pri.LL/Stress",
      "AdjLL/Factor",
      "AdjLL/Stress"
    ]
  }
}
```

**Response — PSC_RATING_SVC_SUM_DGN**

```json
{
  "Service Limit State Summary (Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "RatingCase",
      "Component",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "Capacity",
      "Demand",
      "Point",
      "DC/Factor",
      "DC/Stress",
      "DW/Factor",
      "DW/Stress",
      "Temperature/Factor",
      "Temperature/Stress",
      "T.Gradient/Factor",
      "T.Gradient/Stress",
      "Permanent/Factor",
      "Permanent/Stress",
      "Secondary/Factor",
      "Secondary/Stress",
      "UserDefined/Factor",
      "UserDefined/Stress",
      "Pri.LL/Factor",
      "Pri.LL/Stress",
      "AdjLL/Factor",
      "AdjLL/Stress"
    ],
    "DATA": [
      [
        "1",
        "ser_DC(MAX)_A.V(Fz-Min)",
        "Slab Tens.",
        "-0.845",
        "3 - J",
        "-",
        "0.327",
        "3604.114",
        "Left Bottom",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "3604.114",
        "1.000",
        "3604.114"
      ],
      [
        "2",
        "ser_DC(MAX)_A.V(My-Max)",
        "Girder Comp.",
        "0.776",
        "5 - I",
        "-",
        "-1.135",
        "-4404.656",
        "Right Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "-4404.656",
        "1.000",
        "-4404.656"
      ],
      [
        "3",
        "ser_DC(MAX)_A.V(My-Max)",
        "Girder Tens.",
        "-12.268",
        "2 - I",
        "-",
        "0.130",
        "2425.130",
        "Left Bottom",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "2425.130",
        "1.000",
        "2425.130"
      ],
      [
        "4",
        "ser_DC(MAX)_A.V(My-Min)",
        "Slab Comp.",
        "33.448",
        "2 - J",
        "-",
        "-1.560",
        "-87.973",
        "Left Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "-87.973",
        "1.000",
        "-87.973"
      ]
    ]
  }
}
```

**Response — PSC_RATING_SVC_SUM_LEG**

```json
{
  "Service Limit State Summary (Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "RatingCase",
      "Component",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "Capacity",
      "Demand",
      "Point",
      "DC/Factor",
      "DC/Stress",
      "DW/Factor",
      "DW/Stress",
      "Temperature/Factor",
      "Temperature/Stress",
      "T.Gradient/Factor",
      "T.Gradient/Stress",
      "Permanent/Factor",
      "Permanent/Stress",
      "Secondary/Factor",
      "Secondary/Stress",
      "UserDefined/Factor",
      "UserDefined/Stress",
      "Pri.LL/Factor",
      "Pri.LL/Stress",
      "AdjLL/Factor",
      "AdjLL/Stress"
    ],
    "DATA": [
      [
        "1",
        "SER_L_DC(MAX)_A.V(Fx-Max)",
        "Slab Tens.",
        "-1.000",
        "5 - J",
        "-",
        "0.000",
        "26.391",
        "Left Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "26.391",
        "1.000",
        "26.391"
      ],
      [
        "2",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "Girder Comp.",
        "9.426",
        "6 - J",
        "-",
        "-1.906",
        "-1260.431",
        "Left Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "-1260.431",
        "1.000",
        "-1260.431"
      ],
      [
        "3",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "Girder Tens.",
        "4.691",
        "4 - I",
        "-",
        "2.580",
        "3125.933",
        "Left Bottom",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "3125.933",
        "1.000",
        "3125.933"
      ],
      [
        "4",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "Slab Comp.",
        "-25.341",
        "2 - J",
        "-",
        "0.021",
        "-3380.221",
        "Right Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "-3380.221",
        "1.000",
        "-3380.221"
      ]
    ]
  }
}
```

**Response — PSC_RATING_SVC_SUM_DGN_VBEAM**

```json
{
  "Service Limit State Summary (Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "RatingCase",
      "Component",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "Capacity",
      "Demand",
      "Point",
      "DC/Factor",
      "DC/Stress",
      "DW/Factor",
      "DW/Stress",
      "Temperature/Factor",
      "Temperature/Stress",
      "T.Gradient/Factor",
      "T.Gradient/Stress",
      "Permanent/Factor",
      "Permanent/Stress",
      "Secondary/Factor",
      "Secondary/Stress",
      "UserDefined/Factor",
      "UserDefined/Stress",
      "Pri.LL/Factor",
      "Pri.LL/Stress",
      "AdjLL/Factor",
      "AdjLL/Stress"
    ],
    "DATA": [
      [
        "1",
        "ser_DC(MAX)_A.V(Fx-Max)",
        "Slab Tens.",
        "-1.000",
        "5 - J",
        "-",
        "0.000",
        "26.391",
        "Left Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "26.391",
        "1.000",
        "26.391"
      ],
      [
        "2",
        "ser_DC(MAX)_A.V(My-Max)",
        "Girder Comp.",
        "17.360",
        "6 - J",
        "-",
        "-3.356",
        "-1260.431",
        "Left Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "-1260.431",
        "1.000",
        "-1260.431"
      ],
      [
        "3",
        "ser_DC(MAX)_A.V(My-Max)",
        "Girder Tens.",
        "7.890",
        "4 - I",
        "-",
        "4.031",
        "3125.933",
        "Left Bottom",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "3125.933",
        "1.000",
        "3125.933"
      ],
      [
        "4",
        "ser_DC(MAX)_A.V(My-Max)",
        "Slab Comp.",
        "-25.341",
        "2 - J",
        "-",
        "0.021",
        "-3380.221",
        "Right Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "-3380.221",
        "1.000",
        "-3380.221"
      ]
    ]
  }
}
```

**Response — PSC_RATING_SVC_SUM_LEG_VBEAM**

```json
{
  "Service Limit State Summary (Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "RatingCase",
      "Component",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "Capacity",
      "Demand",
      "Point",
      "DC/Factor",
      "DC/Stress",
      "DW/Factor",
      "DW/Stress",
      "Temperature/Factor",
      "Temperature/Stress",
      "T.Gradient/Factor",
      "T.Gradient/Stress",
      "Permanent/Factor",
      "Permanent/Stress",
      "Secondary/Factor",
      "Secondary/Stress",
      "UserDefined/Factor",
      "UserDefined/Stress",
      "Pri.LL/Factor",
      "Pri.LL/Stress",
      "AdjLL/Factor",
      "AdjLL/Stress"
    ],
    "DATA": [
      [
        "1",
        "SER_L_DC(MAX)_A.V(Fx-Max)",
        "Slab Tens.",
        "-1.000",
        "5 - J",
        "-",
        "0.000",
        "26.391",
        "Left Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "26.391",
        "1.000",
        "26.391"
      ],
      [
        "2",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "Girder Comp.",
        "9.426",
        "6 - J",
        "-",
        "-1.906",
        "-1260.431",
        "Left Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "-1260.431",
        "1.000",
        "-1260.431"
      ],
      [
        "3",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "Girder Tens.",
        "4.691",
        "4 - I",
        "-",
        "2.580",
        "3125.933",
        "Left Bottom",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "3125.933",
        "1.000",
        "3125.933"
      ],
      [
        "4",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "Slab Comp.",
        "-25.341",
        "2 - J",
        "-",
        "0.021",
        "-3380.221",
        "Right Top",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "-3380.221",
        "1.000",
        "-3380.221"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Service Limit State Summary (Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_SVC_SUM_DGN",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "Component",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "Capacity",
      "Demand",
      "Point",
      "DC/Factor",
      "DC/Stress",
      "DW/Factor",
      "DW/Stress",
      "Temperature/Factor",
      "Temperature/Stress",
      "T.Gradient/Factor",
      "T.Gradient/Stress",
      "Permanent/Factor",
      "Permanent/Stress",
      "Secondary/Factor",
      "Secondary/Stress",
      "UserDefined/Factor",
      "UserDefined/Stress",
      "Pri.LL/Factor",
      "Pri.LL/Stress",
      "AdjLL/Factor",
      "AdjLL/Stress"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 17. `TABLE` · `PSC_RATING_SVC_SUM_PER` — Service Limit State Summary (Permit)

> **기능** 허가하중의 사용한계상태 평가 요약을 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738357949721](https://support.midasuser.com/hc/en-us/articles/64738357949721)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Service Limit State Summary (Permit): "PSC_RATING_SVC_SUM_PER" · Service Limit State Summary (Permit) - Virtual Beam: "PSC_RATING_SVC_SUM_PER_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Rating Case | `"RATING_CASE"` | array | - | Optional |
| 4 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 5 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 5.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 5.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 5.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 5.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 6 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 6.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 6.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 7 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_SVC_SUM_PER",
            "PSC_RATING_SVC_SUM_PER_VBEAM"
          ]
        },
        "RATING_CASE": {
          "type": "array",
          "description": "Rating case name filter (names defined in Define Rating Case). Only Service limit state cases with Permit Load apply. If no listed case applies, the result is empty. Omit (or []) for all cases.",
          "items": {
            "type": "string"
          }
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "RatingCase",
              "Tendon/Rebar",
              "MinimumStressRatio",
              "Location",
              "RelativeLocation",
              "AllowableStress",
              "AppliedStress",
              "Cracked/Uncracked",
              "M_Demand",
              "Mcr",
              "Effectivestress",
              "DeadLoadstress",
              "LiveLoadstress"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Service Limit State Summary (Permit)` — `Index`, `RatingCase`, `Tendon/Rebar`, `MinimumStressRatio`, `Location`, `RelativeLocation`, `AllowableStress`, `AppliedStress`, `Cracked/Uncracked`, `M_Demand`, `Mcr`, `Effectivestress`, `DeadLoadstress`, `LiveLoadstress`

### Request / Response JSON

**Request — PSC_RATING_SVC_SUM_PER**

```json
{
  "Argument": {
    "TABLE_NAME": "Service Limit State Summary (Permit)",
    "TABLE_TYPE": "PSC_RATING_SVC_SUM_PER",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "Tendon/Rebar",
      "MinimumStressRatio",
      "Location",
      "RelativeLocation",
      "AllowableStress",
      "AppliedStress",
      "Cracked/Uncracked",
      "M_Demand",
      "Mcr",
      "Effectivestress",
      "DeadLoadstress",
      "LiveLoadstress"
    ]
  }
}
```

**Request — PSC_RATING_SVC_SUM_PER_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Service Limit State Summary (Permit)",
    "TABLE_TYPE": "PSC_RATING_SVC_SUM_PER_VBEAM",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "Tendon/Rebar",
      "MinimumStressRatio",
      "Location",
      "RelativeLocation",
      "AllowableStress",
      "AppliedStress",
      "Cracked/Uncracked",
      "M_Demand",
      "Mcr",
      "Effectivestress",
      "DeadLoadstress",
      "LiveLoadstress"
    ]
  }
}
```

**Response — PSC_RATING_SVC_SUM_PER**

```json
{
  "Service Limit State Summary (Permit)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "RatingCase",
      "Tendon/Rebar",
      "MinimumStressRatio",
      "Location",
      "RelativeLocation",
      "AllowableStress",
      "AppliedStress",
      "Cracked/Uncracked",
      "M_Demand",
      "Mcr",
      "Effectivestress",
      "DeadLoadstress",
      "LiveLoadstress"
    ],
    "DATA": [
      [
        "1",
        "SER_P_DC(MAX)_A.V(Fx-Min)",
        "Tendon",
        "67.199",
        "13 - J",
        "-",
        "1675000.000",
        "24925.845",
        "Uncracked",
        "-11.656",
        "3591.140",
        "504574.606",
        "0.000",
        "1561.858"
      ]
    ]
  }
}
```

**Response — PSC_RATING_SVC_SUM_PER_VBEAM**

```json
{
  "Service Limit State Summary (Permit)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "RatingCase",
      "Tendon/Rebar",
      "MinimumStressRatio",
      "Location",
      "RelativeLocation",
      "AllowableStress",
      "AppliedStress",
      "Cracked/Uncracked",
      "M_Demand",
      "Mcr",
      "Effectivestress",
      "DeadLoadstress",
      "LiveLoadstress"
    ],
    "DATA": [
      [
        "1",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "Rebar",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "1 - I",
        "-",
        "30000.000",
        "0.000",
        "Uncracked",
        "0.000",
        "1981.168",
        "506670.503",
        "0.000",
        "0.000"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Service Limit State Summary (Permit)",
    "TABLE_TYPE": "PSC_RATING_SVC_SUM_PER",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "Tendon/Rebar",
      "MinimumStressRatio",
      "Location",
      "RelativeLocation",
      "AllowableStress",
      "AppliedStress",
      "Cracked/Uncracked",
      "M_Demand",
      "Mcr",
      "Effectivestress",
      "DeadLoadstress",
      "LiveLoadstress"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 18. `TABLE` · `PSC_RATING_STR_SUM_FLEX` — Strength Limit State Summary (Flexural)

> **기능** 휨에 대한 강도한계상태 평가 요약을 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738380475929](https://support.midasuser.com/hc/en-us/articles/64738380475929)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Strength Limit State Summary (Flexural): "PSC_RATING_STR_SUM_FLEX" · Strength Limit State Summary (Flexural) - Virtual Beam: "PSC_RATING_STR_SUM_FLEX_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Rating Case | `"RATING_CASE"` | array | - | Optional |
| 4 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 5 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 5.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 5.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 5.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 5.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 6 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 6.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 6.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 7 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_STR_SUM_FLEX",
            "PSC_RATING_STR_SUM_FLEX_VBEAM"
          ]
        },
        "RATING_CASE": {
          "type": "array",
          "description": "Rating case name filter (names defined in Define Rating Case). Only Strength limit state cases apply (Design Live, Legal and Permit). If no listed case applies, the result is empty. Omit (or []) for all cases.",
          "items": {
            "type": "string"
          }
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Factor/Force pairs are selected together (e.g. \"DC/Factor\" also returns \"DC/Force\"). Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "RatingCase",
              "RatingLevel",
              "Positive/Negative",
              "MinimumRatingFactor",
              "Location",
              "RelativeLocation",
              "LRFDResistanceFactor",
              "Capacity",
              "Demand",
              "DC/Factor",
              "DC/Force",
              "DW/Factor",
              "DW/Force",
              "Temperature/Factor",
              "Temperature/Force",
              "T.Gradient/Factor",
              "T.Gradient/Force",
              "Permanent/Factor",
              "Permanent/Force",
              "Secondary/Factor",
              "Secondary/Force",
              "UserDefined/Factor",
              "UserDefined/Force",
              "Pri.LL/Factor",
              "Pri.LL/Force",
              "AdjLL/Factor",
              "AdjLL/Force"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Strength Limit State Summary (Flexural)` — `Index`, `RatingCase`, `RatingLevel`, `Positive/Negative`, `MinimumRatingFactor`, `Location`, `RelativeLocation`, `LRFDResistanceFactor`, `Capacity`, `Demand`, `DC/Factor`, `DC/Force`, `DW/Factor`, `DW/Force`, `Temperature/Factor`, `Temperature/Force`, `T.Gradient/Factor`, `T.Gradient/Force`, `Permanent/Factor`, `Permanent/Force`, `Secondary/Factor`, `Secondary/Force`, `UserDefined/Factor`, `UserDefined/Force`, `Pri.LL/Factor`, `Pri.LL/Force`, `AdjLL/Factor`, `AdjLL/Force`

### Request / Response JSON

**Request — PSC_RATING_STR_SUM_FLEX**

```json
{
  "Argument": {
    "TABLE_NAME": "Strength Limit State Summary (Flexural)",
    "TABLE_TYPE": "PSC_RATING_STR_SUM_FLEX",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "RatingLevel",
      "Positive/Negative",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "LRFDResistanceFactor",
      "Capacity",
      "Demand",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
```

**Request — PSC_RATING_STR_SUM_FLEX_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Strength Limit State Summary (Flexural)",
    "TABLE_TYPE": "PSC_RATING_STR_SUM_FLEX_VBEAM",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "RatingLevel",
      "Positive/Negative",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "LRFDResistanceFactor",
      "Capacity",
      "Demand",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
```

**Response — PSC_RATING_STR_SUM_FLEX**

```json
{
  "Strength Limit State Summary (Flexural)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "RatingCase",
      "RatingLevel",
      "Positive/Negative",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "LRFDResistanceFactor",
      "Capacity",
      "Demand",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ],
    "DATA": [
      [
        "1",
        "STR_DC(MAX)_A.V(Fx-Max)",
        "Design Live",
        "Positive",
        "-1.000",
        "18 - I",
        "-",
        "0.750",
        "0.000",
        "495.305",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "495.305",
        "1.000",
        "495.305"
      ],
      [
        "2",
        "STR_L_DC(MAX)_A.V(Fx-Max)",
        "Legal",
        "Positive",
        "-1.000",
        "18 - I",
        "-",
        "0.750",
        "0.000",
        "495.305",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "495.305",
        "1.000",
        "495.305"
      ],
      [
        "3",
        "STR_P_DC(MAX)_A.V(Fx-Max)",
        "Permit",
        "Positive",
        "-1.000",
        "18 - I",
        "-",
        "0.750",
        "0.000",
        "495.305",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "495.305",
        "1.000",
        "495.305"
      ]
    ]
  }
}
```

**Response — PSC_RATING_STR_SUM_FLEX_VBEAM**

```json
{
  "Strength Limit State Summary (Flexural)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "RatingCase",
      "RatingLevel",
      "Positive/Negative",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "LRFDResistanceFactor",
      "Capacity",
      "Demand",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ],
    "DATA": [
      [
        "1",
        "STR_DC(MAX)_A.V(Fx-Max)",
        "Design Live",
        "Positive",
        "-1.000",
        "18 - I",
        "-",
        "0.750",
        "0.000",
        "495.305",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "495.305",
        "1.000",
        "495.305"
      ],
      [
        "2",
        "STR_L_DC(MAX)_A.V(Fx-Max)",
        "Legal",
        "Positive",
        "-1.000",
        "18 - I",
        "-",
        "0.750",
        "0.000",
        "495.305",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "495.305",
        "1.000",
        "495.305"
      ],
      [
        "3",
        "STR_P_DC(MAX)_A.V(Fx-Max)",
        "Permit",
        "Positive",
        "-1.000",
        "18 - I",
        "-",
        "0.750",
        "0.000",
        "495.305",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "495.305",
        "1.000",
        "495.305"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Strength Limit State Summary (Flexural)",
    "TABLE_TYPE": "PSC_RATING_STR_SUM_FLEX",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "RatingLevel",
      "Positive/Negative",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "LRFDResistanceFactor",
      "Capacity",
      "Demand",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 19. `TABLE` · `PSC_RATING_STR_SUM_SHEAR` — Strength Limit State Summary (Shear)

> **기능** 전단에 대한 강도한계상태 평가 요약을 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738351943449](https://support.midasuser.com/hc/en-us/articles/64738351943449)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Strength Limit State Summary (Shear): "PSC_RATING_STR_SUM_SHEAR" · Strength Limit State Summary (Shear) - Virtual Beam: "PSC_RATING_STR_SUM_SHEAR_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Rating Case | `"RATING_CASE"` | array | - | Optional |
| 4 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 5 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 5.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 5.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 5.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 5.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 6 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 6.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 6.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 7 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_STR_SUM_SHEAR",
            "PSC_RATING_STR_SUM_SHEAR_VBEAM"
          ]
        },
        "RATING_CASE": {
          "type": "array",
          "description": "Rating case name filter (names defined in Define Rating Case). Only Strength limit state cases apply (Design Live, Legal and Permit). If no listed case applies, the result is empty. Omit (or []) for all cases.",
          "items": {
            "type": "string"
          }
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Factor/Force pairs are selected together (e.g. \"DC/Factor\" also returns \"DC/Force\"). Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "RatingCase",
              "RatingLevel",
              "MinimumRatingFactor",
              "Location",
              "RelativeLocation",
              "LRFDResistanceFactor",
              "Capacity",
              "Demand",
              "DC/Factor",
              "DC/Force",
              "DW/Factor",
              "DW/Force",
              "Temperature/Factor",
              "Temperature/Force",
              "T.Gradient/Factor",
              "T.Gradient/Force",
              "Permanent/Factor",
              "Permanent/Force",
              "Secondary/Factor",
              "Secondary/Force",
              "UserDefined/Factor",
              "UserDefined/Force",
              "Pri.LL/Factor",
              "Pri.LL/Force",
              "AdjLL/Factor",
              "AdjLL/Force"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Strength Limit State Summary (Shear)` — `Index`, `RatingCase`, `RatingLevel`, `MinimumRatingFactor`, `Location`, `RelativeLocation`, `LRFDResistanceFactor`, `Capacity`, `Demand`, `DC/Factor`, `DC/Force`, `DW/Factor`, `DW/Force`, `Temperature/Factor`, `Temperature/Force`, `T.Gradient/Factor`, `T.Gradient/Force`, `Permanent/Factor`, `Permanent/Force`, `Secondary/Factor`, `Secondary/Force`, `UserDefined/Factor`, `UserDefined/Force`, `Pri.LL/Factor`, `Pri.LL/Force`, `AdjLL/Factor`, `AdjLL/Force`

### Request / Response JSON

**Request — PSC_RATING_STR_SUM_SHEAR**

```json
{
  "Argument": {
    "TABLE_NAME": "Strength Limit State Summary (Shear)",
    "TABLE_TYPE": "PSC_RATING_STR_SUM_SHEAR",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "RatingLevel",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "LRFDResistanceFactor",
      "Capacity",
      "Demand",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
```

**Request — PSC_RATING_STR_SUM_SHEAR_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Strength Limit State Summary (Shear)",
    "TABLE_TYPE": "PSC_RATING_STR_SUM_SHEAR_VBEAM",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "RatingLevel",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "LRFDResistanceFactor",
      "Capacity",
      "Demand",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
```

**Response — PSC_RATING_STR_SUM_SHEAR**

```json
{
  "Strength Limit State Summary (Shear)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "RatingCase",
      "RatingLevel",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "LRFDResistanceFactor",
      "Capacity",
      "Demand",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ],
    "DATA": [
      [
        "1",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "-1.443",
        "2 - I",
        "-",
        "0.900",
        "325.765",
        "-318.166",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "2",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "-1.443",
        "2 - I",
        "-",
        "0.900",
        "325.765",
        "-318.166",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "3",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "-1.443",
        "2 - I",
        "-",
        "0.900",
        "325.765",
        "-318.166",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ]
    ]
  }
}
```

**Response — PSC_RATING_STR_SUM_SHEAR_VBEAM**

```json
{
  "Strength Limit State Summary (Shear)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "RatingCase",
      "RatingLevel",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "LRFDResistanceFactor",
      "Capacity",
      "Demand",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ],
    "DATA": [
      [
        "1",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "-1.550",
        "2 - I",
        "-",
        "0.900",
        "325.765",
        "-318.166",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "2",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "-1.550",
        "2 - I",
        "-",
        "0.900",
        "325.765",
        "-318.166",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "3",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "-1.550",
        "2 - I",
        "-",
        "0.900",
        "325.765",
        "-318.166",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Strength Limit State Summary (Shear)",
    "TABLE_TYPE": "PSC_RATING_STR_SUM_SHEAR",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "RatingCase",
      "RatingLevel",
      "MinimumRatingFactor",
      "Location",
      "RelativeLocation",
      "LRFDResistanceFactor",
      "Capacity",
      "Demand",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 20. `TABLE` · `PSC_RATING_STRESS_DGN` — Stress Rating Factor(Design Live, Legal)

> **기능** 설계 활하중 및 법정하중의 응력 평가계수를 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738372749721](https://support.midasuser.com/hc/en-us/articles/64738372749721)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Stress Rating Factor (Design Live): "PSC_RATING_STRESS_DGN" · Stress Rating Factor (Legal): "PSC_RATING_STRESS_LEG" · Stress Rating Factor (Design Live) - Virtual Beam: "PSC_RATING_STRESS_DGN_VBEAM" · Stress Rating Factor (Legal) - Virtual Beam: "PSC_RATING_STRESS_LEG_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 3.1 | └ [General] Specify Each ID. IDs without stress rating results are ignored; if none match (or the list is empty), all elements are returned. | `"KEYS"` | array | - | Optional |
| 3.2 | └ [General] Specify ID Range (e.g., '1to5') | `"TO"` | string | - | Optional |
| 4 | [General] Element Parts | `"PARTS"` | array | - | Optional |
| 5 | [General] Compression/Tension | `"COMP_TENS"` | array | - | Optional |
| 6 | [General] Girder/Slab · Girder · Slab | `"GIRDER_SLAB"` | string | - | Optional |
| 7 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 8 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 8.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 8.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 8.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 8.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 9 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 9.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 9.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 10 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_STRESS_DGN",
            "PSC_RATING_STRESS_LEG",
            "PSC_RATING_STRESS_DGN_VBEAM",
            "PSC_RATING_STRESS_LEG_VBEAM"
          ]
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input. Use KEYS or TO, not both (sending both returns an error).",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID. IDs without stress rating results are ignored; if none match (or the list is empty), all elements are returned.",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to5')"
            }
          },
          "additionalProperties": false
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "Part I",
              "Part J"
            ]
          }
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
          }
        },
        "GIRDER_SLAB": {
          "type": "string",
          "description": "Girder or Slab",
          "enum": [
            "Girder",
            "Slab"
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Group",
              "Elem.",
              "Part",
              "Girder/Slab",
              "RelativeLocation",
              "Comp./Tens.",
              "RatingCase",
              "RatingFactor",
              "Check"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Stress Rating Factor(Design Live, Legal)` — `Index`, `Group`, `Elem.`, `Part`, `Girder/Slab`, `RelativeLocation`, `Comp./Tens.`, `RatingCase`, `RatingFactor`, `Check`

### Request / Response JSON

**Request — PSC_RATING_STRESS_DGN**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Factor(Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DGN",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "COMP_TENS": [
      "Compression",
      "Tension"
    ],
    "GIRDER_SLAB": "Girder",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "Comp./Tens.",
      "RatingCase",
      "RatingFactor",
      "Check"
    ]
  }
}
```

**Request — PSC_RATING_STRESS_LEG**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Factor(Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_STRESS_LEG",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "COMP_TENS": [
      "Compression",
      "Tension"
    ],
    "GIRDER_SLAB": "Girder",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "Comp./Tens.",
      "RatingCase",
      "RatingFactor",
      "Check"
    ]
  }
}
```

**Request — PSC_RATING_STRESS_DGN_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Factor(Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DGN_VBEAM",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "COMP_TENS": [
      "Compression",
      "Tension"
    ],
    "GIRDER_SLAB": "Girder",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "Comp./Tens.",
      "RatingCase",
      "RatingFactor",
      "Check"
    ]
  }
}
```

**Request — PSC_RATING_STRESS_LEG_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Factor(Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_STRESS_LEG_VBEAM",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "COMP_TENS": [
      "Compression",
      "Tension"
    ],
    "GIRDER_SLAB": "Girder",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "Comp./Tens.",
      "RatingCase",
      "RatingFactor",
      "Check"
    ]
  }
}
```

**Response — PSC_RATING_STRESS_DGN**

```json
{
  "Stress Rating Factor(Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "Comp./Tens.",
      "RatingCase",
      "RatingFactor",
      "Check"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "Comp.",
        "ser_DC(MAX)_A.V(Fx-Min)",
        "171.232",
        "OK"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "Tens.",
        "ser_DC(MAX)_A.V(My-Min)",
        "17.693",
        "OK"
      ],
      [
        "3",
        "Girder",
        "2",
        "J[3]",
        "Girder(PSC)",
        "-",
        "Comp.",
        "ser_DC(MAX)_A.V(My-Max)",
        "8.593",
        "OK"
      ],
      [
        "4",
        "Girder",
        "2",
        "J[3]",
        "Girder(PSC)",
        "-",
        "Tens.",
        "ser_DC(MAX)_A.V(My-Max)",
        "0.623",
        "NG"
      ]
    ]
  }
}
```

**Response — PSC_RATING_STRESS_LEG**

```json
{
  "Stress Rating Factor(Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "Comp./Tens.",
      "RatingCase",
      "RatingFactor",
      "Check"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "Comp.",
        "SER_L_DC(MAX)_A.V(My-Min)",
        "97.257",
        "OK"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "Tens.",
        "SER_L_DC(MAX)_A.V(My-Min)",
        "49.444",
        "OK"
      ],
      [
        "3",
        "Girder",
        "2",
        "J[3]",
        "Girder(PSC)",
        "-",
        "Comp.",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "12.010",
        "OK"
      ],
      [
        "4",
        "Girder",
        "2",
        "J[3]",
        "Girder(PSC)",
        "-",
        "Tens.",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "12.936",
        "OK"
      ]
    ]
  }
}
```

**Response — PSC_RATING_STRESS_DGN_VBEAM**

```json
{
  "Stress Rating Factor(Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "Comp./Tens.",
      "RatingCase",
      "RatingFactor",
      "Check"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "1",
        "J[2]",
        "Girder(Composite)",
        "-",
        "Comp.",
        "ser_DC(MAX)_A.V(My-Min)",
        "367.801",
        "OK"
      ],
      [
        "2",
        "Girder",
        "1",
        "J[2]",
        "Girder(Composite)",
        "-",
        "Tens.",
        "ser_DC(MAX)_A.V(My-Max)",
        "15.960",
        "OK"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "Comp.",
        "ser_DC(MAX)_A.V(My-Min)",
        "367.794",
        "OK"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "Tens.",
        "ser_DC(MAX)_A.V(My-Max)",
        "15.960",
        "OK"
      ],
      [
        "5",
        "Girder",
        "2",
        "J[3]",
        "Girder(Composite)",
        "-",
        "Comp.",
        "ser_DC(MAX)_A.V(My-Min)",
        "448.335",
        "OK"
      ],
      [
        "6",
        "Girder",
        "2",
        "J[3]",
        "Girder(Composite)",
        "-",
        "Tens.",
        "ser_DC(MAX)_A.V(Fx-Min)",
        "13.531",
        "OK"
      ],
      [
        "7",
        "Girder",
        "3",
        "I[3]",
        "Girder(Composite)",
        "-",
        "Comp.",
        "ser_DC(MAX)_A.V(My-Max)",
        "27.417",
        "OK"
      ],
      [
        "8",
        "Girder",
        "3",
        "I[3]",
        "Girder(Composite)",
        "-",
        "Tens.",
        "ser_DC(MAX)_A.V(My-Max)",
        "9.278",
        "OK"
      ],
      [
        "9",
        "Girder",
        "3",
        "J[4]",
        "Girder(Composite)",
        "-",
        "Comp.",
        "ser_DC(MAX)_A.V(My-Max)",
        "23.580",
        "OK"
      ],
      [
        "10",
        "Girder",
        "3",
        "J[4]",
        "Girder(Composite)",
        "-",
        "Tens.",
        "ser_DC(MAX)_A.V(My-Max)",
        "7.890",
        "OK"
      ]
    ]
  }
}
```

**Response — PSC_RATING_STRESS_LEG_VBEAM**

```json
{
  "Stress Rating Factor(Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "Comp./Tens.",
      "RatingCase",
      "RatingFactor",
      "Check"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "1",
        "J[2]",
        "Girder(Composite)",
        "-",
        "Comp.",
        "SER_L_DC(MAX)_A.V(My-Min)",
        "233.475",
        "OK"
      ],
      [
        "2",
        "Girder",
        "1",
        "J[2]",
        "Girder(Composite)",
        "-",
        "Tens.",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "9.858",
        "OK"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "Comp.",
        "SER_L_DC(MAX)_A.V(My-Min)",
        "233.468",
        "OK"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "Tens.",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "9.858",
        "OK"
      ],
      [
        "5",
        "Girder",
        "2",
        "J[3]",
        "Girder(Composite)",
        "-",
        "Comp.",
        "SER_L_DC(MAX)_A.V(My-Min)",
        "284.694",
        "OK"
      ],
      [
        "6",
        "Girder",
        "2",
        "J[3]",
        "Girder(Composite)",
        "-",
        "Tens.",
        "SER_L_DC(MAX)_A.V(Fx-Min)",
        "8.302",
        "OK"
      ],
      [
        "7",
        "Girder",
        "3",
        "I[3]",
        "Girder(Composite)",
        "-",
        "Comp.",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "14.051",
        "OK"
      ],
      [
        "8",
        "Girder",
        "3",
        "I[3]",
        "Girder(Composite)",
        "-",
        "Tens.",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "5.579",
        "OK"
      ],
      [
        "9",
        "Girder",
        "3",
        "J[4]",
        "Girder(Composite)",
        "-",
        "Comp.",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "12.019",
        "OK"
      ],
      [
        "10",
        "Girder",
        "3",
        "J[4]",
        "Girder(Composite)",
        "-",
        "Tens.",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "4.691",
        "OK"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Factor(Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DGN",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "COMP_TENS": [
      "Compression",
      "Tension"
    ],
    "GIRDER_SLAB": "Girder",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "Comp./Tens.",
      "RatingCase",
      "RatingFactor",
      "Check"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 21. `TABLE` · `PSC_RATING_STRESS_PER` — Stress Rating Factor(Permit)

> **기능** 허가하중의 응력 평가계수를 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738388181529](https://support.midasuser.com/hc/en-us/articles/64738388181529)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Stress Rating Factor (Permit): "PSC_RATING_STRESS_PER" · Stress Rating Factor (Permit) - Virtual Beam: "PSC_RATING_STRESS_PER_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 3.1 | └ [General] Specify Each ID. IDs without stress rating results are ignored; if none match (or the list is empty), all elements are returned. | `"KEYS"` | array | - | Optional |
| 3.2 | └ [General] Specify ID Range (e.g., '1to5') | `"TO"` | string | - | Optional |
| 4 | [General] Element Parts | `"PARTS"` | array | - | Optional |
| 5 | [General] Girder/Slab · Girder · Slab | `"GIRDER_SLAB"` | string | - | Optional |
| 6 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 7 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 7.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 7.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 7.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 7.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 8 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 8.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 8.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 9 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_STRESS_PER",
            "PSC_RATING_STRESS_PER_VBEAM"
          ]
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input. Use KEYS or TO, not both (sending both returns an error).",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID. IDs without stress rating results are ignored; if none match (or the list is empty), all elements are returned.",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to5')"
            }
          },
          "additionalProperties": false
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "Part I",
              "Part J"
            ]
          }
        },
        "GIRDER_SLAB": {
          "type": "string",
          "description": "Girder or Slab. Accepted by the server but has no effect on the Permit stress rating table.",
          "enum": [
            "Girder",
            "Slab"
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Group",
              "Elem.",
              "Part",
              "RelativeLocation",
              "Tendon/Rebar",
              "RatingCase",
              "StressRatio",
              "Check"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Stress Rating Factor(Permit)` — `Index`, `Group`, `Elem.`, `Part`, `RelativeLocation`, `Tendon/Rebar`, `RatingCase`, `StressRatio`, `Check`

### Request / Response JSON

**Request — PSC_RATING_STRESS_PER**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Factor(Permit)",
    "TABLE_TYPE": "PSC_RATING_STRESS_PER",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "Tendon/Rebar",
      "RatingCase",
      "StressRatio",
      "Check"
    ]
  }
}
```

**Request — PSC_RATING_STRESS_PER_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Factor(Permit)",
    "TABLE_TYPE": "PSC_RATING_STRESS_PER_VBEAM",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "Tendon/Rebar",
      "RatingCase",
      "StressRatio",
      "Check"
    ]
  }
}
```

**Response — PSC_RATING_STRESS_PER**

```json
{
  "Stress Rating Factor(Permit)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "Tendon/Rebar",
      "RatingCase",
      "StressRatio",
      "Check"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Tendon",
        "SER_P_DC(MAX)_A.V(Fx-Min)",
        "Infinite",
        "OK"
      ],
      [
        "2",
        "Girder",
        "2",
        "J[3]",
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

**Response — PSC_RATING_STRESS_PER_VBEAM**

```json
{
  "Stress Rating Factor(Permit)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "Tendon/Rebar",
      "RatingCase",
      "StressRatio",
      "Check"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "1",
        "I[1]",
        "-",
        "Rebar",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "OK"
      ],
      [
        "2",
        "Girder",
        "1",
        "J[2]",
        "-",
        "Rebar",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "OK"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Rebar",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "OK"
      ],
      [
        "4",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Rebar",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "OK"
      ],
      [
        "5",
        "Girder",
        "3",
        "I[3]",
        "-",
        "Rebar",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "OK"
      ],
      [
        "6",
        "Girder",
        "3",
        "J[4]",
        "-",
        "Rebar",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "OK"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Factor(Permit)",
    "TABLE_TYPE": "PSC_RATING_STRESS_PER",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "Tendon/Rebar",
      "RatingCase",
      "StressRatio",
      "Check"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 22. `TABLE` · `PSC_RATING_FLEXURE` — Flexural Strength Rating Factor

> **기능** 휨강도 평가계수를 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738373247513](https://support.midasuser.com/hc/en-us/articles/64738373247513)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Flexural Strength Rating Factor: "PSC_RATING_FLEXURE" · Flexural Strength Rating Factor - Virtual Beam: "PSC_RATING_FLEXURE_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 3.1 | └ [General] Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned. | `"KEYS"` | array | - | Optional |
| 3.2 | └ [General] Specify ID Range (e.g., '1to5') | `"TO"` | string | - | Optional |
| 4 | [General] Element Parts | `"PARTS"` | array | - | Optional |
| 5 | [General] Positive/Negative | `"POS_NEG"` | array | - | Optional |
| 6 | [General] Rating Case | `"RATING_CASE"` | array | - | Optional |
| 7 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 8 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 8.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 8.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 8.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 8.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 9 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 9.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 9.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 10 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_FLEXURE",
            "PSC_RATING_FLEXURE_VBEAM"
          ]
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input. Use KEYS or TO, not both (sending both returns an error).",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned.",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to5')"
            }
          },
          "additionalProperties": false
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "Part I",
              "Part J"
            ]
          }
        },
        "POS_NEG": {
          "type": "array",
          "description": "Positive or Negative",
          "items": {
            "type": "string",
            "enum": [
              "Positive",
              "Negative"
            ]
          }
        },
        "RATING_CASE": {
          "type": "array",
          "description": "Rating case name filter (names defined in Define Rating Case). Only Strength limit state cases apply. Matching ignores case and spaces. Names that do not match are ignored; if none match, all cases are returned. Omit (or []) for all cases.",
          "items": {
            "type": "string"
          }
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Group",
              "Elem.",
              "Part",
              "RelativeLocation",
              "Positive/Negative",
              "RatingCase",
              "RatingLevel",
              "LRFDResistanceFactor",
              "SystemFactor",
              "ConditionFactor",
              "RatingFactor",
              "Check"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Flexural Strength Rating Factor` — `Index`, `Group`, `Elem.`, `Part`, `RelativeLocation`, `Positive/Negative`, `RatingCase`, `RatingLevel`, `LRFDResistanceFactor`, `SystemFactor`, `ConditionFactor`, `RatingFactor`, `Check`

### Request / Response JSON

**Request — PSC_RATING_FLEXURE**

```json
{
  "Argument": {
    "TABLE_NAME": "Flexural Strength Rating Factor",
    "TABLE_TYPE": "PSC_RATING_FLEXURE",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "POS_NEG": [
      "Positive",
      "Negative"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "Positive/Negative",
      "RatingCase",
      "RatingLevel",
      "LRFDResistanceFactor",
      "SystemFactor",
      "ConditionFactor",
      "RatingFactor",
      "Check"
    ]
  }
}
```

**Request — PSC_RATING_FLEXURE_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Flexural Strength Rating Factor",
    "TABLE_TYPE": "PSC_RATING_FLEXURE_VBEAM",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "POS_NEG": [
      "Positive",
      "Negative"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "Positive/Negative",
      "RatingCase",
      "RatingLevel",
      "LRFDResistanceFactor",
      "SystemFactor",
      "ConditionFactor",
      "RatingFactor",
      "Check"
    ]
  }
}
```

**Response — PSC_RATING_FLEXURE**

```json
{
  "Flexural Strength Rating Factor": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "Positive/Negative",
      "RatingCase",
      "RatingLevel",
      "LRFDResistanceFactor",
      "SystemFactor",
      "ConditionFactor",
      "RatingFactor",
      "Check"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Negative",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "0.975",
        "1.000",
        "1.000",
        "63.768",
        "OK"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Negative",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "0.975",
        "1.000",
        "1.000",
        "63.768",
        "OK"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Negative",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "0.975",
        "1.000",
        "1.000",
        "63.768",
        "OK"
      ],
      [
        "4",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Negative",
        "STR_DC(MAX)_A.V(Fx-Min)",
        "Design Live",
        "0.976",
        "1.000",
        "1.000",
        "369.026",
        "OK"
      ],
      [
        "5",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Positive",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "0.761",
        "1.000",
        "1.000",
        "0.814",
        "NG"
      ],
      [
        "6",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Negative",
        "STR_L_DC(MAX)_A.V(Fx-Min)",
        "Legal",
        "0.976",
        "1.000",
        "1.000",
        "369.026",
        "OK"
      ],
      [
        "7",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Positive",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "0.761",
        "1.000",
        "1.000",
        "0.814",
        "NG"
      ],
      [
        "8",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Negative",
        "STR_P_DC(MAX)_A.V(Fx-Min)",
        "Permit",
        "0.976",
        "1.000",
        "1.000",
        "369.026",
        "OK"
      ],
      [
        "9",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Positive",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "0.761",
        "1.000",
        "1.000",
        "0.814",
        "NG"
      ]
    ]
  }
}
```

**Response — PSC_RATING_FLEXURE_VBEAM**

```json
{
  "Flexural Strength Rating Factor": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "Positive/Negative",
      "RatingCase",
      "RatingLevel",
      "LRFDResistanceFactor",
      "SystemFactor",
      "ConditionFactor",
      "RatingFactor",
      "Check"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "1",
        "J[2]",
        "-",
        "Positive",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "1.000",
        "1.000",
        "1.000",
        "8.676",
        "OK"
      ],
      [
        "2",
        "Girder",
        "1",
        "J[2]",
        "-",
        "Negative",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "1.000",
        "1.000",
        "1.000",
        "257.665",
        "OK"
      ],
      [
        "3",
        "Girder",
        "1",
        "J[2]",
        "-",
        "Positive",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "1.000",
        "1.000",
        "1.000",
        "8.676",
        "OK"
      ],
      [
        "4",
        "Girder",
        "1",
        "J[2]",
        "-",
        "Negative",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "1.000",
        "1.000",
        "1.000",
        "257.665",
        "OK"
      ],
      [
        "5",
        "Girder",
        "1",
        "J[2]",
        "-",
        "Positive",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "1.000",
        "1.000",
        "1.000",
        "8.676",
        "OK"
      ],
      [
        "6",
        "Girder",
        "1",
        "J[2]",
        "-",
        "Negative",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "1.000",
        "1.000",
        "1.000",
        "257.665",
        "OK"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Positive",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "1.000",
        "1.000",
        "1.000",
        "8.676",
        "OK"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Negative",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "1.000",
        "1.000",
        "1.000",
        "257.665",
        "OK"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Positive",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "1.000",
        "1.000",
        "1.000",
        "8.676",
        "OK"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Negative",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "1.000",
        "1.000",
        "1.000",
        "257.665",
        "OK"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Positive",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "1.000",
        "1.000",
        "1.000",
        "8.676",
        "OK"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "-",
        "Negative",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "1.000",
        "1.000",
        "1.000",
        "257.665",
        "OK"
      ],
      [
        "13",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Positive",
        "STR_DC(MAX)_A.V(Fx-Min)",
        "Design Live",
        "1.000",
        "1.000",
        "1.000",
        "7.291",
        "OK"
      ],
      [
        "14",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Negative",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "1.000",
        "1.000",
        "1.000",
        "314.115",
        "OK"
      ],
      [
        "15",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Positive",
        "STR_L_DC(MAX)_A.V(Fx-Min)",
        "Legal",
        "1.000",
        "1.000",
        "1.000",
        "7.291",
        "OK"
      ],
      [
        "16",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Negative",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "1.000",
        "1.000",
        "1.000",
        "314.115",
        "OK"
      ],
      [
        "17",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Positive",
        "STR_P_DC(MAX)_A.V(Fx-Min)",
        "Permit",
        "1.000",
        "1.000",
        "1.000",
        "7.291",
        "OK"
      ],
      [
        "18",
        "Girder",
        "2",
        "J[3]",
        "-",
        "Negative",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "1.000",
        "1.000",
        "1.000",
        "314.115",
        "OK"
      ],
      [
        "19",
        "Girder",
        "3",
        "I[3]",
        "-",
        "Positive",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "1.000",
        "1.000",
        "1.000",
        "4.864",
        "OK"
      ],
      [
        "20",
        "Girder",
        "3",
        "I[3]",
        "-",
        "Negative",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "1.000",
        "1.000",
        "1.000",
        "314.115",
        "OK"
      ],
      [
        "21",
        "Girder",
        "3",
        "I[3]",
        "-",
        "Positive",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "1.000",
        "1.000",
        "1.000",
        "4.864",
        "OK"
      ],
      [
        "22",
        "Girder",
        "3",
        "I[3]",
        "-",
        "Negative",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "1.000",
        "1.000",
        "1.000",
        "314.115",
        "OK"
      ],
      [
        "23",
        "Girder",
        "3",
        "I[3]",
        "-",
        "Positive",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "1.000",
        "1.000",
        "1.000",
        "4.864",
        "OK"
      ],
      [
        "24",
        "Girder",
        "3",
        "I[3]",
        "-",
        "Negative",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "1.000",
        "1.000",
        "1.000",
        "314.115",
        "OK"
      ],
      [
        "25",
        "Girder",
        "3",
        "J[4]",
        "-",
        "Positive",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "1.000",
        "1.000",
        "1.000",
        "4.073",
        "OK"
      ],
      [
        "26",
        "Girder",
        "3",
        "J[4]",
        "-",
        "Negative",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "1.000",
        "1.000",
        "1.000",
        "402.036",
        "OK"
      ],
      [
        "27",
        "Girder",
        "3",
        "J[4]",
        "-",
        "Positive",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "1.000",
        "1.000",
        "1.000",
        "4.073",
        "OK"
      ],
      [
        "28",
        "Girder",
        "3",
        "J[4]",
        "-",
        "Negative",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "1.000",
        "1.000",
        "1.000",
        "402.036",
        "OK"
      ],
      [
        "29",
        "Girder",
        "3",
        "J[4]",
        "-",
        "Positive",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "1.000",
        "1.000",
        "1.000",
        "4.073",
        "OK"
      ],
      [
        "30",
        "Girder",
        "3",
        "J[4]",
        "-",
        "Negative",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "1.000",
        "1.000",
        "1.000",
        "402.036",
        "OK"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Flexural Strength Rating Factor",
    "TABLE_TYPE": "PSC_RATING_FLEXURE",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "POS_NEG": [
      "Positive",
      "Negative"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "Positive/Negative",
      "RatingCase",
      "RatingLevel",
      "LRFDResistanceFactor",
      "SystemFactor",
      "ConditionFactor",
      "RatingFactor",
      "Check"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 23. `TABLE` · `PSC_RATING_SHEAR` — Shear Strength Rating Factor

> **기능** 전단강도 평가계수를 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738373579929](https://support.midasuser.com/hc/en-us/articles/64738373579929)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Shear Strength Rating Factor: "PSC_RATING_SHEAR" · Shear Strength Rating Factor - Virtual Beam: "PSC_RATING_SHEAR_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 3.1 | └ [General] Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned. | `"KEYS"` | array | - | Optional |
| 3.2 | └ [General] Specify ID Range (e.g., '1to5') | `"TO"` | string | - | Optional |
| 4 | [General] Element Parts | `"PARTS"` | array | - | Optional |
| 5 | [General] Rating Case | `"RATING_CASE"` | array | - | Optional |
| 6 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 7 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 7.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 7.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 7.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 7.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 8 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 8.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 8.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 9 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_SHEAR",
            "PSC_RATING_SHEAR_VBEAM"
          ]
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input. Use KEYS or TO, not both (sending both returns an error).",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned.",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to5')"
            }
          },
          "additionalProperties": false
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "Part I",
              "Part J"
            ]
          }
        },
        "RATING_CASE": {
          "type": "array",
          "description": "Rating case name filter (names defined in Define Rating Case). Only Strength limit state cases apply. Matching ignores case and spaces. Names that do not match are ignored; if none match, all cases are returned. Omit (or []) for all cases.",
          "items": {
            "type": "string"
          }
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Group",
              "Elem.",
              "Part",
              "RelativeLocation",
              "RatingCase",
              "RatingLevel",
              "LRFDResistanceFactor",
              "SystemFactor",
              "ConditionFactor",
              "RatingFactor",
              "Check"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Shear Strength Rating Factor` — `Index`, `Group`, `Elem.`, `Part`, `RelativeLocation`, `RatingCase`, `RatingLevel`, `LRFDResistanceFactor`, `SystemFactor`, `ConditionFactor`, `RatingFactor`, `Check`

### Request / Response JSON

**Request — PSC_RATING_SHEAR**

```json
{
  "Argument": {
    "TABLE_NAME": "Shear Strength Rating Factor",
    "TABLE_TYPE": "PSC_RATING_SHEAR",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "LRFDResistanceFactor",
      "SystemFactor",
      "ConditionFactor",
      "RatingFactor",
      "Check"
    ]
  }
}
```

**Request — PSC_RATING_SHEAR_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Shear Strength Rating Factor",
    "TABLE_TYPE": "PSC_RATING_SHEAR_VBEAM",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "LRFDResistanceFactor",
      "SystemFactor",
      "ConditionFactor",
      "RatingFactor",
      "Check"
    ]
  }
}
```

**Response — PSC_RATING_SHEAR**

```json
{
  "Shear Strength Rating Factor": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "LRFDResistanceFactor",
      "SystemFactor",
      "ConditionFactor",
      "RatingFactor",
      "Check"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "0.900",
        "1.000",
        "1.000",
        "0.318",
        "NG"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "0.900",
        "1.000",
        "1.000",
        "0.318",
        "NG"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "0.900",
        "1.000",
        "1.000",
        "0.318",
        "NG"
      ],
      [
        "4",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "0.900",
        "1.000",
        "1.000",
        "-0.736",
        "NG"
      ],
      [
        "5",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "0.900",
        "1.000",
        "1.000",
        "-0.736",
        "NG"
      ],
      [
        "6",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "0.900",
        "1.000",
        "1.000",
        "-0.736",
        "NG"
      ]
    ]
  }
}
```

**Response — PSC_RATING_SHEAR_VBEAM**

```json
{
  "Shear Strength Rating Factor": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "LRFDResistanceFactor",
      "SystemFactor",
      "ConditionFactor",
      "RatingFactor",
      "Check"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "1",
        "J[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "0.900",
        "1.000",
        "1.000",
        "-0.079",
        "NG"
      ],
      [
        "2",
        "Girder",
        "1",
        "J[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "0.900",
        "1.000",
        "1.000",
        "-0.079",
        "NG"
      ],
      [
        "3",
        "Girder",
        "1",
        "J[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "0.900",
        "1.000",
        "1.000",
        "-0.079",
        "NG"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "0.900",
        "1.000",
        "1.000",
        "-0.079",
        "NG"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "0.900",
        "1.000",
        "1.000",
        "-0.079",
        "NG"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "0.900",
        "1.000",
        "1.000",
        "-0.079",
        "NG"
      ],
      [
        "7",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "0.900",
        "1.000",
        "1.000",
        "0.170",
        "NG"
      ],
      [
        "8",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "0.900",
        "1.000",
        "1.000",
        "0.170",
        "NG"
      ],
      [
        "9",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "0.900",
        "1.000",
        "1.000",
        "0.170",
        "NG"
      ],
      [
        "10",
        "Girder",
        "3",
        "I[3]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "0.900",
        "1.000",
        "1.000",
        "0.170",
        "NG"
      ],
      [
        "11",
        "Girder",
        "3",
        "I[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "0.900",
        "1.000",
        "1.000",
        "0.170",
        "NG"
      ],
      [
        "12",
        "Girder",
        "3",
        "I[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "0.900",
        "1.000",
        "1.000",
        "0.170",
        "NG"
      ],
      [
        "13",
        "Girder",
        "3",
        "J[4]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "0.900",
        "1.000",
        "1.000",
        "0.692",
        "NG"
      ],
      [
        "14",
        "Girder",
        "3",
        "J[4]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "0.900",
        "1.000",
        "1.000",
        "0.692",
        "NG"
      ],
      [
        "15",
        "Girder",
        "3",
        "J[4]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "0.900",
        "1.000",
        "1.000",
        "0.692",
        "NG"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Shear Strength Rating Factor",
    "TABLE_TYPE": "PSC_RATING_SHEAR",
    "NODE_ELEMS": {
      "TO": "1to3"
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "LRFDResistanceFactor",
      "SystemFactor",
      "ConditionFactor",
      "RatingFactor",
      "Check"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 24. `TABLE` · `PSC_RATING_STRESS_DETAIL_DGN` — Stress Rating Detail(Design Live, Legal)

> **기능** 설계 활하중 및 법정하중의 응력 평가 상세 결과를 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738521745945](https://support.midasuser.com/hc/en-us/articles/64738521745945)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Stress Rating Detail (Design Live): "PSC_RATING_STRESS_DETAIL_DGN" · Stress Rating Detail (Legal): "PSC_RATING_STRESS_DETAIL_LEG" · Stress Rating Detail (Design Live) - Virtual Beam: "PSC_RATING_STRESS_DETAIL_DGN_VBEAM" · Stress Rating Detail (Legal) - Virtual Beam: "PSC_RATING_STRESS_DETAIL_LEG_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Rating Case | `"RATING_CASE"` | array | - | Optional |
| 4 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 4.1 | └ [General] Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned. | `"KEYS"` | array | - | Optional |
| 4.2 | └ [General] Specify ID Range (e.g., '1to5') | `"TO"` | string | - | Optional |
| 5 | [General] Element Parts | `"PARTS"` | array | - | Optional |
| 6 | [General] Girder/Slab · Girder · Slab | `"GIRDER_SLAB"` | string | - | Optional |
| 7 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 8 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 8.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 8.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 8.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 8.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 9 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 9.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 9.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 10 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_STRESS_DETAIL_DGN",
            "PSC_RATING_STRESS_DETAIL_LEG",
            "PSC_RATING_STRESS_DETAIL_DGN_VBEAM",
            "PSC_RATING_STRESS_DETAIL_LEG_VBEAM"
          ]
        },
        "RATING_CASE": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Rating case name filter (names defined in Define Rating Case). Only Service limit state cases of the table evaluation apply (Design Live cases for *_DGN, Legal cases for *_LEG). Matching ignores case and spaces. Names that do not match are ignored; if none match, the result is empty. Omit (or []) for all cases."
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input. Use KEYS or TO, not both (sending both returns an error).",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned.",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to5')"
            }
          },
          "additionalProperties": false
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "Part I",
              "Part J"
            ]
          }
        },
        "GIRDER_SLAB": {
          "type": "string",
          "description": "Girder or Slab",
          "enum": [
            "Girder",
            "Slab"
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Requesting one column of a group (e.g. \"RatingFactor/CFactor\", \"DC/Factor\") returns the whole group. Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Group",
              "Elem.",
              "Part",
              "Girder/Slab",
              "RelativeLocation",
              "RatingCase",
              "RatingFactor/CFactor",
              "RatingFactor/TFactor",
              "Capacity/Comp.",
              "Capacity/Tens.",
              "DC/Factor",
              "DC/LeftTopStress",
              "DC/RightTopStress",
              "DC/RightBottomStress",
              "DC/LeftBottomStress",
              "DW/Factor",
              "DW/LeftTopStress",
              "DW/RightTopStress",
              "DW/RightBottomStress",
              "DW/LeftBottomStress",
              "Temperature/Factor",
              "Temperature/LeftTopStress",
              "Temperature/RightTopStress",
              "Temperature/RightBottomStress",
              "Temperature/LeftBottomStress",
              "T.Gradient/Factor",
              "T.Gradient/LeftTopStress",
              "T.Gradient/RightTopStress",
              "T.Gradient/RightBottomStress",
              "T.Gradient/LeftBottomStress",
              "Permanent/Factor",
              "Permanent/LeftTopStress",
              "Permanent/RightTopStress",
              "Permanent/RightBottomStress",
              "Permanent/LeftBottomStress",
              "Secondary/Factor",
              "Secondary/LeftTopStress",
              "Secondary/RightTopStress",
              "Secondary/RightBottomStress",
              "Secondary/LeftBottomStress",
              "UserDefined/Factor",
              "UserDefined/LeftTopStress",
              "UserDefined/RightTopStress",
              "UserDefined/RightBottomStress",
              "UserDefined/LeftBottomStress",
              "Pri.LL/Factor",
              "Pri.LL/LeftTopStress",
              "Pri.LL/RightTopStress",
              "Pri.LL/RightBottomStress",
              "Pri.LL/LeftBottomStress",
              "AdjLL/Factor",
              "AdjLL/LeftTopStress",
              "AdjLL/RightTopStress",
              "AdjLL/RightBottomStress",
              "AdjLL/LeftBottomStress"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Stress Rating Detail(Design Live, Legal)` — `Index`, `Group`, `Elem.`, `Part`, `Girder/Slab`, `RelativeLocation`, `RatingCase`, `RatingFactor/CFactor`, `RatingFactor/TFactor`, `Capacity/Comp.`, `Capacity/Tens.`, `DC/Factor`, `DC/LeftTopStress`, `DC/RightTopStress`, `DC/RightBottomStress`, `DC/LeftBottomStress`, `DW/Factor`, `DW/LeftTopStress`, `DW/RightTopStress`, `DW/RightBottomStress`, `DW/LeftBottomStress`, `Temperature/Factor`, `Temperature/LeftTopStress`, `Temperature/RightTopStress`, `Temperature/RightBottomStress`, `Temperature/LeftBottomStress`, `T.Gradient/Factor`, `T.Gradient/LeftTopStress`, `T.Gradient/RightTopStress`, `T.Gradient/RightBottomStress`, `T.Gradient/LeftBottomStress`, `Permanent/Factor`, `Permanent/LeftTopStress`, `Permanent/RightTopStress`, `Permanent/RightBottomStress`, `Permanent/LeftBottomStress`, `Secondary/Factor`, `Secondary/LeftTopStress`, `Secondary/RightTopStress`, `Secondary/RightBottomStress`, `Secondary/LeftBottomStress`, `UserDefined/Factor`, `UserDefined/LeftTopStress`, `UserDefined/RightTopStress`, `UserDefined/RightBottomStress`, `UserDefined/LeftBottomStress`, `Pri.LL/Factor`, `Pri.LL/LeftTopStress`, `Pri.LL/RightTopStress`, `Pri.LL/RightBottomStress`, `Pri.LL/LeftBottomStress`, `AdjLL/Factor`, `AdjLL/LeftTopStress`, `AdjLL/RightTopStress`, `AdjLL/RightBottomStress`, `AdjLL/LeftBottomStress`

### Request / Response JSON

**Request — PSC_RATING_STRESS_DETAIL_DGN**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Detail(Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DETAIL_DGN",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "RatingCase",
      "RatingFactor/CFactor",
      "RatingFactor/TFactor",
      "Capacity/Comp.",
      "Capacity/Tens.",
      "DC/Factor",
      "DC/LeftTopStress",
      "DC/RightTopStress",
      "DC/RightBottomStress",
      "DC/LeftBottomStress",
      "DW/Factor",
      "DW/LeftTopStress",
      "DW/RightTopStress",
      "DW/RightBottomStress",
      "DW/LeftBottomStress",
      "Temperature/Factor",
      "Temperature/LeftTopStress",
      "Temperature/RightTopStress",
      "Temperature/RightBottomStress",
      "Temperature/LeftBottomStress",
      "T.Gradient/Factor",
      "T.Gradient/LeftTopStress",
      "T.Gradient/RightTopStress",
      "T.Gradient/RightBottomStress",
      "T.Gradient/LeftBottomStress",
      "Permanent/Factor",
      "Permanent/LeftTopStress",
      "Permanent/RightTopStress",
      "Permanent/RightBottomStress",
      "Permanent/LeftBottomStress",
      "Secondary/Factor",
      "Secondary/LeftTopStress",
      "Secondary/RightTopStress",
      "Secondary/RightBottomStress",
      "Secondary/LeftBottomStress",
      "UserDefined/Factor",
      "UserDefined/LeftTopStress",
      "UserDefined/RightTopStress",
      "UserDefined/RightBottomStress",
      "UserDefined/LeftBottomStress",
      "Pri.LL/Factor",
      "Pri.LL/LeftTopStress",
      "Pri.LL/RightTopStress",
      "Pri.LL/RightBottomStress",
      "Pri.LL/LeftBottomStress",
      "AdjLL/Factor",
      "AdjLL/LeftTopStress",
      "AdjLL/RightTopStress",
      "AdjLL/RightBottomStress",
      "AdjLL/LeftBottomStress"
    ]
  }
}
```

**Request — PSC_RATING_STRESS_DETAIL_LEG**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Detail(Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DETAIL_LEG",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "RatingCase",
      "RatingFactor/CFactor",
      "RatingFactor/TFactor",
      "Capacity/Comp.",
      "Capacity/Tens.",
      "DC/Factor",
      "DC/LeftTopStress",
      "DC/RightTopStress",
      "DC/RightBottomStress",
      "DC/LeftBottomStress",
      "DW/Factor",
      "DW/LeftTopStress",
      "DW/RightTopStress",
      "DW/RightBottomStress",
      "DW/LeftBottomStress",
      "Temperature/Factor",
      "Temperature/LeftTopStress",
      "Temperature/RightTopStress",
      "Temperature/RightBottomStress",
      "Temperature/LeftBottomStress",
      "T.Gradient/Factor",
      "T.Gradient/LeftTopStress",
      "T.Gradient/RightTopStress",
      "T.Gradient/RightBottomStress",
      "T.Gradient/LeftBottomStress",
      "Permanent/Factor",
      "Permanent/LeftTopStress",
      "Permanent/RightTopStress",
      "Permanent/RightBottomStress",
      "Permanent/LeftBottomStress",
      "Secondary/Factor",
      "Secondary/LeftTopStress",
      "Secondary/RightTopStress",
      "Secondary/RightBottomStress",
      "Secondary/LeftBottomStress",
      "UserDefined/Factor",
      "UserDefined/LeftTopStress",
      "UserDefined/RightTopStress",
      "UserDefined/RightBottomStress",
      "UserDefined/LeftBottomStress",
      "Pri.LL/Factor",
      "Pri.LL/LeftTopStress",
      "Pri.LL/RightTopStress",
      "Pri.LL/RightBottomStress",
      "Pri.LL/LeftBottomStress",
      "AdjLL/Factor",
      "AdjLL/LeftTopStress",
      "AdjLL/RightTopStress",
      "AdjLL/RightBottomStress",
      "AdjLL/LeftBottomStress"
    ]
  }
}
```

**Request — PSC_RATING_STRESS_DETAIL_DGN_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Detail(Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DETAIL_DGN_VBEAM",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "RatingCase",
      "RatingFactor/CFactor",
      "RatingFactor/TFactor",
      "Capacity/Comp.",
      "Capacity/Tens.",
      "DC/Factor",
      "DC/LeftTopStress",
      "DC/RightTopStress",
      "DC/RightBottomStress",
      "DC/LeftBottomStress",
      "DW/Factor",
      "DW/LeftTopStress",
      "DW/RightTopStress",
      "DW/RightBottomStress",
      "DW/LeftBottomStress",
      "Temperature/Factor",
      "Temperature/LeftTopStress",
      "Temperature/RightTopStress",
      "Temperature/RightBottomStress",
      "Temperature/LeftBottomStress",
      "T.Gradient/Factor",
      "T.Gradient/LeftTopStress",
      "T.Gradient/RightTopStress",
      "T.Gradient/RightBottomStress",
      "T.Gradient/LeftBottomStress",
      "Permanent/Factor",
      "Permanent/LeftTopStress",
      "Permanent/RightTopStress",
      "Permanent/RightBottomStress",
      "Permanent/LeftBottomStress",
      "Secondary/Factor",
      "Secondary/LeftTopStress",
      "Secondary/RightTopStress",
      "Secondary/RightBottomStress",
      "Secondary/LeftBottomStress",
      "UserDefined/Factor",
      "UserDefined/LeftTopStress",
      "UserDefined/RightTopStress",
      "UserDefined/RightBottomStress",
      "UserDefined/LeftBottomStress",
      "Pri.LL/Factor",
      "Pri.LL/LeftTopStress",
      "Pri.LL/RightTopStress",
      "Pri.LL/RightBottomStress",
      "Pri.LL/LeftBottomStress",
      "AdjLL/Factor",
      "AdjLL/LeftTopStress",
      "AdjLL/RightTopStress",
      "AdjLL/RightBottomStress",
      "AdjLL/LeftBottomStress"
    ]
  }
}
```

**Request — PSC_RATING_STRESS_DETAIL_LEG_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Detail(Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DETAIL_LEG_VBEAM",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "RatingCase",
      "RatingFactor/CFactor",
      "RatingFactor/TFactor",
      "Capacity/Comp.",
      "Capacity/Tens.",
      "DC/Factor",
      "DC/LeftTopStress",
      "DC/RightTopStress",
      "DC/RightBottomStress",
      "DC/LeftBottomStress",
      "DW/Factor",
      "DW/LeftTopStress",
      "DW/RightTopStress",
      "DW/RightBottomStress",
      "DW/LeftBottomStress",
      "Temperature/Factor",
      "Temperature/LeftTopStress",
      "Temperature/RightTopStress",
      "Temperature/RightBottomStress",
      "Temperature/LeftBottomStress",
      "T.Gradient/Factor",
      "T.Gradient/LeftTopStress",
      "T.Gradient/RightTopStress",
      "T.Gradient/RightBottomStress",
      "T.Gradient/LeftBottomStress",
      "Permanent/Factor",
      "Permanent/LeftTopStress",
      "Permanent/RightTopStress",
      "Permanent/RightBottomStress",
      "Permanent/LeftBottomStress",
      "Secondary/Factor",
      "Secondary/LeftTopStress",
      "Secondary/RightTopStress",
      "Secondary/RightBottomStress",
      "Secondary/LeftBottomStress",
      "UserDefined/Factor",
      "UserDefined/LeftTopStress",
      "UserDefined/RightTopStress",
      "UserDefined/RightBottomStress",
      "UserDefined/LeftBottomStress",
      "Pri.LL/Factor",
      "Pri.LL/LeftTopStress",
      "Pri.LL/RightTopStress",
      "Pri.LL/RightBottomStress",
      "Pri.LL/LeftBottomStress",
      "AdjLL/Factor",
      "AdjLL/LeftTopStress",
      "AdjLL/RightTopStress",
      "AdjLL/RightBottomStress",
      "AdjLL/LeftBottomStress"
    ]
  }
}
```

**Response — PSC_RATING_STRESS_DETAIL_DGN**

```json
{
  "Stress Rating Detail(Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "RatingCase",
      "RatingFactor/CFactor",
      "RatingFactor/TFactor",
      "Capacity/Comp.",
      "Capacity/Tens.",
      "DC/Factor",
      "DC/LeftTopStress",
      "DC/RightTopStress",
      "DC/RightBottomStress",
      "DC/LeftBottomStress",
      "DW/Factor",
      "DW/LeftTopStress",
      "DW/RightTopStress",
      "DW/RightBottomStress",
      "DW/LeftBottomStress",
      "Temperature/Factor",
      "Temperature/LeftTopStress",
      "Temperature/RightTopStress",
      "Temperature/RightBottomStress",
      "Temperature/LeftBottomStress",
      "T.Gradient/Factor",
      "T.Gradient/LeftTopStress",
      "T.Gradient/RightTopStress",
      "T.Gradient/RightBottomStress",
      "T.Gradient/LeftBottomStress",
      "Permanent/Factor",
      "Permanent/LeftTopStress",
      "Permanent/RightTopStress",
      "Permanent/RightBottomStress",
      "Permanent/LeftBottomStress",
      "Secondary/Factor",
      "Secondary/LeftTopStress",
      "Secondary/RightTopStress",
      "Secondary/RightBottomStress",
      "Secondary/LeftBottomStress",
      "UserDefined/Factor",
      "UserDefined/LeftTopStress",
      "UserDefined/RightTopStress",
      "UserDefined/RightBottomStress",
      "UserDefined/LeftBottomStress",
      "Pri.LL/Factor",
      "Pri.LL/LeftTopStress",
      "Pri.LL/RightTopStress",
      "Pri.LL/RightBottomStress",
      "Pri.LL/LeftBottomStress",
      "AdjLL/Factor",
      "AdjLL/LeftTopStress",
      "AdjLL/RightTopStress",
      "AdjLL/RightBottomStress",
      "AdjLL/LeftBottomStress"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(Fx-Max)",
        "81.286",
        "17.708",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "531.744",
        "531.881",
        "-211.492",
        "-211.567",
        "1.000",
        "531.744",
        "531.881",
        "-211.492",
        "-211.567"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(Fx-Min)",
        "171.232",
        "170.927",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "57.862",
        "57.820",
        "-101.044",
        "-101.021",
        "1.000",
        "57.862",
        "57.820",
        "-101.044",
        "-101.021"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(Fy-Max)",
        "98.555",
        "21.639",
        "-2.525",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "439.424",
        "439.812",
        "-174.665",
        "-174.876",
        "1.000",
        "439.424",
        "439.812",
        "-174.665",
        "-174.876"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(Fy-Min)",
        "166.194",
        "37.228",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "260.229",
        "259.914",
        "-104.088",
        "-103.917",
        "1.000",
        "260.229",
        "259.914",
        "-104.088",
        "-103.917"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(Fz-Max)",
        "1418276693226939904.000",
        "185987507951446016.000",
        "-1.405",
        "0.325",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(Fz-Min)",
        "121.111",
        "26.889",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "356.699",
        "356.651",
        "-142.517",
        "-142.491",
        "1.000",
        "356.699",
        "356.651",
        "-142.517",
        "-142.491"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(Mx-Max)",
        "183.975",
        "41.028",
        "-2.525",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "236.700",
        "236.917",
        "-94.001",
        "-94.119",
        "1.000",
        "236.700",
        "236.917",
        "-94.001",
        "-94.119"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(Mx-Min)",
        "103.794",
        "22.919",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "415.911",
        "416.001",
        "-166.068",
        "-166.117",
        "1.000",
        "415.911",
        "416.001",
        "-166.068",
        "-166.117"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(My-Max)",
        "1418276693226939904.000",
        "185987507951446016.000",
        "-1.405",
        "0.325",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(My-Min)",
        "80.993",
        "17.693",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "532.184",
        "532.321",
        "-212.249",
        "-212.324",
        "1.000",
        "532.184",
        "532.321",
        "-212.249",
        "-212.324"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(Mz-Max)",
        "166.195",
        "37.228",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "260.228",
        "259.912",
        "-104.087",
        "-103.917",
        "1.000",
        "260.228",
        "259.912",
        "-104.087",
        "-103.917"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MAX)_A.V(Mz-Min)",
        "98.554",
        "21.639",
        "-2.525",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "439.426",
        "439.814",
        "-174.666",
        "-174.876",
        "1.000",
        "439.426",
        "439.814",
        "-174.666",
        "-174.876"
      ],
      [
        "13",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(Fx-Max)",
        "81.286",
        "17.708",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "531.744",
        "531.881",
        "-211.492",
        "-211.567",
        "1.000",
        "531.744",
        "531.881",
        "-211.492",
        "-211.567"
      ],
      [
        "14",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(Fx-Min)",
        "171.232",
        "170.927",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "57.862",
        "57.820",
        "-101.044",
        "-101.021",
        "1.000",
        "57.862",
        "57.820",
        "-101.044",
        "-101.021"
      ],
      [
        "15",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(Fy-Max)",
        "98.555",
        "21.639",
        "-2.525",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "439.424",
        "439.812",
        "-174.665",
        "-174.876",
        "1.000",
        "439.424",
        "439.812",
        "-174.665",
        "-174.876"
      ],
      [
        "16",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(Fy-Min)",
        "166.194",
        "37.228",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "260.229",
        "259.914",
        "-104.088",
        "-103.917",
        "1.000",
        "260.229",
        "259.914",
        "-104.088",
        "-103.917"
      ],
      [
        "17",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(Fz-Max)",
        "1418276693226939904.000",
        "185987507951446016.000",
        "-1.405",
        "0.325",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000"
      ],
      [
        "18",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(Fz-Min)",
        "121.111",
        "26.889",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "356.699",
        "356.651",
        "-142.517",
        "-142.491",
        "1.000",
        "356.699",
        "356.651",
        "-142.517",
        "-142.491"
      ],
      [
        "19",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(Mx-Max)",
        "183.975",
        "41.028",
        "-2.525",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "236.700",
        "236.917",
        "-94.001",
        "-94.119",
        "1.000",
        "236.700",
        "236.917",
        "-94.001",
        "-94.119"
      ],
      [
        "20",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(Mx-Min)",
        "103.794",
        "22.919",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "415.911",
        "416.001",
        "-166.068",
        "-166.117",
        "1.000",
        "415.911",
        "416.001",
        "-166.068",
        "-166.117"
      ],
      [
        "21",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(My-Max)",
        "1418276693226939904.000",
        "185987507951446016.000",
        "-1.405",
        "0.325",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000"
      ],
      [
        "22",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(My-Min)",
        "80.993",
        "17.693",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "532.184",
        "532.321",
        "-212.249",
        "-212.324",
        "1.000",
        "532.184",
        "532.321",
        "-212.249",
        "-212.324"
      ],
      [
        "23",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(Mz-Max)",
        "166.195",
        "37.228",
        "-2.524",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "260.228",
        "259.912",
        "-104.087",
        "-103.917",
        "1.000",
        "260.228",
        "259.912",
        "-104.087",
        "-103.917"
      ],
      [
        "24",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "ser_DC(MIN)_A.V(Mz-Min)",
        "98.554",
        "21.639",
        "-2.525",
        "1.443",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "439.426",
        "439.814",
        "-174.666",
        "-174.876",
        "1.000",
        "439.426",
        "439.814",
        "-174.666",
        "-174.876"
      ]
    ]
  }
}
```

**Response — PSC_RATING_STRESS_DETAIL_LEG**

```json
{
  "Stress Rating Detail(Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "RatingCase",
      "RatingFactor/CFactor",
      "RatingFactor/TFactor",
      "Capacity/Comp.",
      "Capacity/Tens.",
      "DC/Factor",
      "DC/LeftTopStress",
      "DC/RightTopStress",
      "DC/RightBottomStress",
      "DC/LeftBottomStress",
      "DW/Factor",
      "DW/LeftTopStress",
      "DW/RightTopStress",
      "DW/RightBottomStress",
      "DW/LeftBottomStress",
      "Temperature/Factor",
      "Temperature/LeftTopStress",
      "Temperature/RightTopStress",
      "Temperature/RightBottomStress",
      "Temperature/LeftBottomStress",
      "T.Gradient/Factor",
      "T.Gradient/LeftTopStress",
      "T.Gradient/RightTopStress",
      "T.Gradient/RightBottomStress",
      "T.Gradient/LeftBottomStress",
      "Permanent/Factor",
      "Permanent/LeftTopStress",
      "Permanent/RightTopStress",
      "Permanent/RightBottomStress",
      "Permanent/LeftBottomStress",
      "Secondary/Factor",
      "Secondary/LeftTopStress",
      "Secondary/RightTopStress",
      "Secondary/RightBottomStress",
      "Secondary/LeftBottomStress",
      "UserDefined/Factor",
      "UserDefined/LeftTopStress",
      "UserDefined/RightTopStress",
      "UserDefined/RightBottomStress",
      "UserDefined/LeftBottomStress",
      "Pri.LL/Factor",
      "Pri.LL/LeftTopStress",
      "Pri.LL/RightTopStress",
      "Pri.LL/RightBottomStress",
      "Pri.LL/LeftBottomStress",
      "AdjLL/Factor",
      "AdjLL/LeftTopStress",
      "AdjLL/RightTopStress",
      "AdjLL/RightBottomStress",
      "AdjLL/LeftBottomStress"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(Fx-Max)",
        "97.609",
        "49.485",
        "-3.026",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "531.744",
        "531.881",
        "-211.492",
        "-211.567",
        "1.000",
        "531.744",
        "531.881",
        "-211.492",
        "-211.567"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(Fx-Min)",
        "205.401",
        "462.958",
        "-3.025",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "57.862",
        "57.820",
        "-101.044",
        "-101.021",
        "1.000",
        "57.862",
        "57.820",
        "-101.044",
        "-101.021"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(Fy-Max)",
        "118.298",
        "60.067",
        "-3.026",
        "3.895",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "439.424",
        "439.812",
        "-174.665",
        "-174.876",
        "1.000",
        "439.424",
        "439.812",
        "-174.665",
        "-174.876"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(Fy-Min)",
        "199.364",
        "102.160",
        "-3.025",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "260.229",
        "259.914",
        "-104.088",
        "-103.917",
        "1.000",
        "260.229",
        "259.914",
        "-104.088",
        "-103.917"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(Fz-Max)",
        "1923638285899940096.000",
        "1588753121899670016.000",
        "-1.906",
        "2.776",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(Fz-Min)",
        "145.337",
        "74.261",
        "-3.025",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "356.699",
        "356.651",
        "-142.517",
        "-142.491",
        "1.000",
        "356.699",
        "356.651",
        "-142.517",
        "-142.491"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(Mx-Max)",
        "220.658",
        "112.364",
        "-3.026",
        "3.895",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "236.700",
        "236.917",
        "-94.001",
        "-94.119",
        "1.000",
        "236.700",
        "236.917",
        "-94.001",
        "-94.119"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(Mx-Min)",
        "124.584",
        "63.546",
        "-3.025",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "415.911",
        "416.001",
        "-166.068",
        "-166.117",
        "1.000",
        "415.911",
        "416.001",
        "-166.068",
        "-166.117"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "1923638285899940096.000",
        "1588753121899670016.000",
        "-1.906",
        "2.776",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(My-Min)",
        "97.257",
        "49.444",
        "-3.026",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "532.184",
        "532.321",
        "-212.249",
        "-212.324",
        "1.000",
        "532.184",
        "532.321",
        "-212.249",
        "-212.324"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(Mz-Max)",
        "199.365",
        "102.161",
        "-3.025",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "260.228",
        "259.912",
        "-104.087",
        "-103.917",
        "1.000",
        "260.228",
        "259.912",
        "-104.087",
        "-103.917"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MAX)_A.V(Mz-Min)",
        "118.297",
        "60.067",
        "-3.026",
        "3.895",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "439.426",
        "439.814",
        "-174.666",
        "-174.876",
        "1.000",
        "439.426",
        "439.814",
        "-174.666",
        "-174.876"
      ],
      [
        "13",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(Fx-Max)",
        "97.609",
        "49.485",
        "-3.026",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "531.744",
        "531.881",
        "-211.492",
        "-211.567",
        "1.000",
        "531.744",
        "531.881",
        "-211.492",
        "-211.567"
      ],
      [
        "14",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(Fx-Min)",
        "205.401",
        "462.958",
        "-3.025",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "57.862",
        "57.820",
        "-101.044",
        "-101.021",
        "1.000",
        "57.862",
        "57.820",
        "-101.044",
        "-101.021"
      ],
      [
        "15",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(Fy-Max)",
        "118.298",
        "60.067",
        "-3.026",
        "3.895",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "439.424",
        "439.812",
        "-174.665",
        "-174.876",
        "1.000",
        "439.424",
        "439.812",
        "-174.665",
        "-174.876"
      ],
      [
        "16",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(Fy-Min)",
        "199.364",
        "102.160",
        "-3.025",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "260.229",
        "259.914",
        "-104.088",
        "-103.917",
        "1.000",
        "260.229",
        "259.914",
        "-104.088",
        "-103.917"
      ],
      [
        "17",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(Fz-Max)",
        "1923638285899940096.000",
        "1588753121899670016.000",
        "-1.906",
        "2.776",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000"
      ],
      [
        "18",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(Fz-Min)",
        "145.337",
        "74.261",
        "-3.025",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "356.699",
        "356.651",
        "-142.517",
        "-142.491",
        "1.000",
        "356.699",
        "356.651",
        "-142.517",
        "-142.491"
      ],
      [
        "19",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(Mx-Max)",
        "220.658",
        "112.364",
        "-3.026",
        "3.895",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "236.700",
        "236.917",
        "-94.001",
        "-94.119",
        "1.000",
        "236.700",
        "236.917",
        "-94.001",
        "-94.119"
      ],
      [
        "20",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(Mx-Min)",
        "124.584",
        "63.546",
        "-3.025",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "415.911",
        "416.001",
        "-166.068",
        "-166.117",
        "1.000",
        "415.911",
        "416.001",
        "-166.068",
        "-166.117"
      ],
      [
        "21",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(My-Max)",
        "1923638285899940096.000",
        "1588753121899670016.000",
        "-1.906",
        "2.776",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000",
        "1.000",
        "-0.000",
        "-0.000",
        "0.000",
        "0.000"
      ],
      [
        "22",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(My-Min)",
        "97.257",
        "49.444",
        "-3.026",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "532.184",
        "532.321",
        "-212.249",
        "-212.324",
        "1.000",
        "532.184",
        "532.321",
        "-212.249",
        "-212.324"
      ],
      [
        "23",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(Mz-Max)",
        "199.365",
        "102.161",
        "-3.025",
        "3.894",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "260.228",
        "259.912",
        "-104.087",
        "-103.917",
        "1.000",
        "260.228",
        "259.912",
        "-104.087",
        "-103.917"
      ],
      [
        "24",
        "Girder",
        "2",
        "I[2]",
        "Girder(PSC)",
        "-",
        "SER_L_DC(MIN)_A.V(Mz-Min)",
        "118.297",
        "60.067",
        "-3.026",
        "3.895",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "439.426",
        "439.814",
        "-174.666",
        "-174.876",
        "1.000",
        "439.426",
        "439.814",
        "-174.666",
        "-174.876"
      ]
    ]
  }
}
```

**Response — PSC_RATING_STRESS_DETAIL_DGN_VBEAM**

```json
{
  "Stress Rating Detail(Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "RatingCase",
      "RatingFactor/CFactor",
      "RatingFactor/TFactor",
      "Capacity/Comp.",
      "Capacity/Tens.",
      "DC/Factor",
      "DC/LeftTopStress",
      "DC/RightTopStress",
      "DC/RightBottomStress",
      "DC/LeftBottomStress",
      "DW/Factor",
      "DW/LeftTopStress",
      "DW/RightTopStress",
      "DW/RightBottomStress",
      "DW/LeftBottomStress",
      "Temperature/Factor",
      "Temperature/LeftTopStress",
      "Temperature/RightTopStress",
      "Temperature/RightBottomStress",
      "Temperature/LeftBottomStress",
      "T.Gradient/Factor",
      "T.Gradient/LeftTopStress",
      "T.Gradient/RightTopStress",
      "T.Gradient/RightBottomStress",
      "T.Gradient/LeftBottomStress",
      "Permanent/Factor",
      "Permanent/LeftTopStress",
      "Permanent/RightTopStress",
      "Permanent/RightBottomStress",
      "Permanent/LeftBottomStress",
      "Secondary/Factor",
      "Secondary/LeftTopStress",
      "Secondary/RightTopStress",
      "Secondary/RightBottomStress",
      "Secondary/LeftBottomStress",
      "UserDefined/Factor",
      "UserDefined/LeftTopStress",
      "UserDefined/RightTopStress",
      "UserDefined/RightBottomStress",
      "UserDefined/LeftBottomStress",
      "Pri.LL/Factor",
      "Pri.LL/LeftTopStress",
      "Pri.LL/RightTopStress",
      "Pri.LL/RightBottomStress",
      "Pri.LL/LeftBottomStress",
      "AdjLL/Factor",
      "AdjLL/LeftTopStress",
      "AdjLL/RightTopStress",
      "AdjLL/RightBottomStress",
      "AdjLL/LeftBottomStress"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(Fx-Max)",
        "86.647",
        "30.710",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-242.521",
        "-242.521",
        "876.466",
        "876.466",
        "1.000",
        "-242.521",
        "-242.521",
        "876.466",
        "876.466"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(Fx-Min)",
        "97.460",
        "34.622",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-215.886",
        "-215.886",
        "780.208",
        "780.208",
        "1.000",
        "-215.886",
        "-215.886",
        "780.208",
        "780.208"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(Fy-Max)",
        "63.986",
        "22.511",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-327.090",
        "-327.090",
        "1182.097",
        "1182.097",
        "1.000",
        "-327.090",
        "-327.090",
        "1182.097",
        "1182.097"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(Fy-Min)",
        "141.287",
        "50.478",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-149.390",
        "-149.390",
        "539.893",
        "539.893",
        "1.000",
        "-149.390",
        "-149.390",
        "539.893",
        "539.893"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(Fz-Max)",
        "99.227",
        "35.261",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(Fz-Min)",
        "48.608",
        "16.948",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(Mx-Max)",
        "48.608",
        "16.948",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(Mx-Min)",
        "99.227",
        "35.261",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(My-Max)",
        "45.879",
        "15.960",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-453.429",
        "-453.429",
        "1638.681",
        "1638.681",
        "1.000",
        "-453.429",
        "-453.429",
        "1638.681",
        "1638.681"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(My-Min)",
        "367.794",
        "1453.905",
        "-3.982",
        "4.347",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(Mz-Max)",
        "367.794",
        "1453.905",
        "-3.982",
        "4.347",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MAX)_A.V(Mz-Min)",
        "51.866",
        "18.126",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-402.078",
        "-402.078",
        "1453.100",
        "1453.100",
        "1.000",
        "-402.078",
        "-402.078",
        "1453.100",
        "1453.100"
      ],
      [
        "13",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(Fx-Max)",
        "86.647",
        "30.710",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-242.521",
        "-242.521",
        "876.466",
        "876.466",
        "1.000",
        "-242.521",
        "-242.521",
        "876.466",
        "876.466"
      ],
      [
        "14",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(Fx-Min)",
        "97.460",
        "34.622",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-215.886",
        "-215.886",
        "780.208",
        "780.208",
        "1.000",
        "-215.886",
        "-215.886",
        "780.208",
        "780.208"
      ],
      [
        "15",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(Fy-Max)",
        "63.986",
        "22.511",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-327.090",
        "-327.090",
        "1182.097",
        "1182.097",
        "1.000",
        "-327.090",
        "-327.090",
        "1182.097",
        "1182.097"
      ],
      [
        "16",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(Fy-Min)",
        "141.287",
        "50.478",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-149.390",
        "-149.390",
        "539.893",
        "539.893",
        "1.000",
        "-149.390",
        "-149.390",
        "539.893",
        "539.893"
      ],
      [
        "17",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(Fz-Max)",
        "99.227",
        "35.261",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455"
      ],
      [
        "18",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(Fz-Min)",
        "48.608",
        "16.948",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515"
      ],
      [
        "19",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(Mx-Max)",
        "48.608",
        "16.948",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515"
      ],
      [
        "20",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(Mx-Min)",
        "99.227",
        "35.261",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455"
      ],
      [
        "21",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(My-Max)",
        "45.879",
        "15.960",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-453.429",
        "-453.429",
        "1638.681",
        "1638.681",
        "1.000",
        "-453.429",
        "-453.429",
        "1638.681",
        "1638.681"
      ],
      [
        "22",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(My-Min)",
        "367.794",
        "1453.905",
        "-3.982",
        "4.347",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446"
      ],
      [
        "23",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(Mz-Max)",
        "367.794",
        "1453.905",
        "-3.982",
        "4.347",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446"
      ],
      [
        "24",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "ser_DC(MIN)_A.V(Mz-Min)",
        "51.866",
        "18.126",
        "-3.083",
        "4.031",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-402.078",
        "-402.078",
        "1453.100",
        "1453.100",
        "1.000",
        "-402.078",
        "-402.078",
        "1453.100",
        "1453.100"
      ]
    ]
  }
}
```

**Response — PSC_RATING_STRESS_DETAIL_LEG_VBEAM**

```json
{
  "Stress Rating Detail(Design Live, Legal)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "RatingCase",
      "RatingFactor/CFactor",
      "RatingFactor/TFactor",
      "Capacity/Comp.",
      "Capacity/Tens.",
      "DC/Factor",
      "DC/LeftTopStress",
      "DC/RightTopStress",
      "DC/RightBottomStress",
      "DC/LeftBottomStress",
      "DW/Factor",
      "DW/LeftTopStress",
      "DW/RightTopStress",
      "DW/RightBottomStress",
      "DW/LeftBottomStress",
      "Temperature/Factor",
      "Temperature/LeftTopStress",
      "Temperature/RightTopStress",
      "Temperature/RightBottomStress",
      "Temperature/LeftBottomStress",
      "T.Gradient/Factor",
      "T.Gradient/LeftTopStress",
      "T.Gradient/RightTopStress",
      "T.Gradient/RightBottomStress",
      "T.Gradient/LeftBottomStress",
      "Permanent/Factor",
      "Permanent/LeftTopStress",
      "Permanent/RightTopStress",
      "Permanent/RightBottomStress",
      "Permanent/LeftBottomStress",
      "Secondary/Factor",
      "Secondary/LeftTopStress",
      "Secondary/RightTopStress",
      "Secondary/RightBottomStress",
      "Secondary/LeftBottomStress",
      "UserDefined/Factor",
      "UserDefined/LeftTopStress",
      "UserDefined/RightTopStress",
      "UserDefined/RightBottomStress",
      "UserDefined/LeftBottomStress",
      "Pri.LL/Factor",
      "Pri.LL/LeftTopStress",
      "Pri.LL/RightTopStress",
      "Pri.LL/RightBottomStress",
      "Pri.LL/LeftBottomStress",
      "AdjLL/Factor",
      "AdjLL/LeftTopStress",
      "AdjLL/RightTopStress",
      "AdjLL/RightBottomStress",
      "AdjLL/LeftBottomStress"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(Fx-Max)",
        "45.413",
        "19.300",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-242.521",
        "-242.521",
        "876.466",
        "876.466",
        "1.000",
        "-242.521",
        "-242.521",
        "876.466",
        "876.466"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(Fx-Min)",
        "51.140",
        "21.805",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-215.886",
        "-215.886",
        "780.208",
        "780.208",
        "1.000",
        "-215.886",
        "-215.886",
        "780.208",
        "780.208"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(Fy-Max)",
        "33.413",
        "14.052",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-327.090",
        "-327.090",
        "1182.097",
        "1182.097",
        "1.000",
        "-327.090",
        "-327.090",
        "1182.097",
        "1182.097"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(Fy-Min)",
        "74.348",
        "31.956",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-149.390",
        "-149.390",
        "539.893",
        "539.893",
        "1.000",
        "-149.390",
        "-149.390",
        "539.893",
        "539.893"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(Fz-Max)",
        "52.075",
        "22.214",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(Fz-Min)",
        "25.270",
        "10.490",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(Mx-Max)",
        "25.270",
        "10.490",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(Mx-Min)",
        "52.075",
        "22.214",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(My-Max)",
        "23.825",
        "9.858",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-453.429",
        "-453.429",
        "1638.681",
        "1638.681",
        "1.000",
        "-453.429",
        "-453.429",
        "1638.681",
        "1638.681"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(My-Min)",
        "233.468",
        "968.454",
        "-2.532",
        "2.896",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(Mz-Max)",
        "233.468",
        "968.454",
        "-2.532",
        "2.896",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MAX)_A.V(Mz-Min)",
        "26.995",
        "11.244",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-402.078",
        "-402.078",
        "1453.100",
        "1453.100",
        "1.000",
        "-402.078",
        "-402.078",
        "1453.100",
        "1453.100"
      ],
      [
        "13",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(Fx-Max)",
        "45.413",
        "19.300",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-242.521",
        "-242.521",
        "876.466",
        "876.466",
        "1.000",
        "-242.521",
        "-242.521",
        "876.466",
        "876.466"
      ],
      [
        "14",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(Fx-Min)",
        "51.140",
        "21.805",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-215.886",
        "-215.886",
        "780.208",
        "780.208",
        "1.000",
        "-215.886",
        "-215.886",
        "780.208",
        "780.208"
      ],
      [
        "15",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(Fy-Max)",
        "33.413",
        "14.052",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-327.090",
        "-327.090",
        "1182.097",
        "1182.097",
        "1.000",
        "-327.090",
        "-327.090",
        "1182.097",
        "1182.097"
      ],
      [
        "16",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(Fy-Min)",
        "74.348",
        "31.956",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-149.390",
        "-149.390",
        "539.893",
        "539.893",
        "1.000",
        "-149.390",
        "-149.390",
        "539.893",
        "539.893"
      ],
      [
        "17",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(Fz-Max)",
        "52.075",
        "22.214",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455"
      ],
      [
        "18",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(Fz-Min)",
        "25.270",
        "10.490",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515"
      ],
      [
        "19",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(Mx-Max)",
        "25.270",
        "10.490",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515",
        "1.000",
        "-428.479",
        "-428.479",
        "1548.515",
        "1548.515"
      ],
      [
        "20",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(Mx-Min)",
        "52.075",
        "22.214",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455",
        "1.000",
        "-212.081",
        "-212.081",
        "766.455",
        "766.455"
      ],
      [
        "21",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(My-Max)",
        "23.825",
        "9.858",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-453.429",
        "-453.429",
        "1638.681",
        "1638.681",
        "1.000",
        "-453.429",
        "-453.429",
        "1638.681",
        "1638.681"
      ],
      [
        "22",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(My-Min)",
        "233.468",
        "968.454",
        "-2.532",
        "2.896",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446"
      ],
      [
        "23",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(Mz-Max)",
        "233.468",
        "968.454",
        "-2.532",
        "2.896",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446",
        "1.000",
        "20.599",
        "20.599",
        "-74.446",
        "-74.446"
      ],
      [
        "24",
        "Girder",
        "2",
        "I[2]",
        "Girder(Composite)",
        "-",
        "SER_L_DC(MIN)_A.V(Mz-Min)",
        "26.995",
        "11.244",
        "-1.633",
        "2.581",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "0.000",
        "0.000",
        "0.000",
        "0.000",
        "1.000",
        "-402.078",
        "-402.078",
        "1453.100",
        "1453.100",
        "1.000",
        "-402.078",
        "-402.078",
        "1453.100",
        "1453.100"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Detail(Design Live, Legal)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DETAIL_DGN",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "Girder/Slab",
      "RelativeLocation",
      "RatingCase",
      "RatingFactor/CFactor",
      "RatingFactor/TFactor",
      "Capacity/Comp.",
      "Capacity/Tens.",
      "DC/Factor",
      "DC/LeftTopStress",
      "DC/RightTopStress",
      "DC/RightBottomStress",
      "DC/LeftBottomStress",
      "DW/Factor",
      "DW/LeftTopStress",
      "DW/RightTopStress",
      "DW/RightBottomStress",
      "DW/LeftBottomStress",
      "Temperature/Factor",
      "Temperature/LeftTopStress",
      "Temperature/RightTopStress",
      "Temperature/RightBottomStress",
      "Temperature/LeftBottomStress",
      "T.Gradient/Factor",
      "T.Gradient/LeftTopStress",
      "T.Gradient/RightTopStress",
      "T.Gradient/RightBottomStress",
      "T.Gradient/LeftBottomStress",
      "Permanent/Factor",
      "Permanent/LeftTopStress",
      "Permanent/RightTopStress",
      "Permanent/RightBottomStress",
      "Permanent/LeftBottomStress",
      "Secondary/Factor",
      "Secondary/LeftTopStress",
      "Secondary/RightTopStress",
      "Secondary/RightBottomStress",
      "Secondary/LeftBottomStress",
      "UserDefined/Factor",
      "UserDefined/LeftTopStress",
      "UserDefined/RightTopStress",
      "UserDefined/RightBottomStress",
      "UserDefined/LeftBottomStress",
      "Pri.LL/Factor",
      "Pri.LL/LeftTopStress",
      "Pri.LL/RightTopStress",
      "Pri.LL/RightBottomStress",
      "Pri.LL/LeftBottomStress",
      "AdjLL/Factor",
      "AdjLL/LeftTopStress",
      "AdjLL/RightTopStress",
      "AdjLL/RightBottomStress",
      "AdjLL/LeftBottomStress"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 25. `TABLE` · `PSC_RATING_STRESS_DETAIL_PER` — Stress Rating Detail(Permit)

> **기능** 허가하중의 응력 평가 상세 결과를 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738373950617](https://support.midasuser.com/hc/en-us/articles/64738373950617)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Stress Rating Detail (Permit): "PSC_RATING_STRESS_DETAIL_PER" · Stress Rating Detail (Permit) - Virtual Beam: "PSC_RATING_STRESS_DETAIL_PER_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Rating Case | `"RATING_CASE"` | array | - | Optional |
| 4 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 4.1 | └ [General] Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned. | `"KEYS"` | array | - | Optional |
| 4.2 | └ [General] Specify ID Range (e.g., '1to5') | `"TO"` | string | - | Optional |
| 5 | [General] Element Parts | `"PARTS"` | array | - | Optional |
| 6 | [General] Girder/Slab · Girder · Slab | `"GIRDER_SLAB"` | string | - | Optional |
| 7 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 8 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 8.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 8.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 8.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 8.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 9 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 9.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 9.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 10 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_STRESS_DETAIL_PER",
            "PSC_RATING_STRESS_DETAIL_PER_VBEAM"
          ]
        },
        "RATING_CASE": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Rating case name filter (names defined in Define Rating Case). Only Service limit state Permit cases apply. Matching ignores case and spaces. Names that do not match are ignored; if none match, the result is empty. Omit (or []) for all cases."
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input. Use KEYS or TO, not both (sending both returns an error).",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned.",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to5')"
            }
          },
          "additionalProperties": false
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "Part I",
              "Part J"
            ]
          }
        },
        "GIRDER_SLAB": {
          "type": "string",
          "description": "Girder or Slab. Accepted by the server but has no effect on the Permit stress rating detail table.",
          "enum": [
            "Girder",
            "Slab"
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
          "description": "Components of Result Table. Omit (or list all 15) to get all columns. Known server issue: when only some columns are requested, the server appends empty \"TFactor\"/\"Tens.\" columns and returns \"StressRatio/TFactor\" under the label \"StressRatio/Tens.\"; request all columns to get correct headers. Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Group",
              "Elem.",
              "Part",
              "RelativeLocation",
              "RatingCase",
              "StressRatio/TFactor",
              "AllowableStress/Tens.",
              "Cracked/Uncracked",
              "M_Demand",
              "Mcr",
              "Tendon/Rebar",
              "EffectivestressofTendon",
              "DeadLoadstress",
              "LiveLoadstress"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Stress Rating Detail(Permit)` — `Index`, `Group`, `Elem.`, `Part`, `RelativeLocation`, `RatingCase`, `StressRatio/TFactor`, `AllowableStress/Tens.`, `Cracked/Uncracked`, `M_Demand`, `Mcr`, `Tendon/Rebar`, `EffectivestressofTendon`, `DeadLoadstress`, `LiveLoadstress`

### Request / Response JSON

**Request — PSC_RATING_STRESS_DETAIL_PER**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Detail(Permit)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DETAIL_PER",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "StressRatio/TFactor",
      "AllowableStress/Tens.",
      "Cracked/Uncracked",
      "M_Demand",
      "Mcr",
      "Tendon/Rebar",
      "EffectivestressofTendon",
      "DeadLoadstress",
      "LiveLoadstress"
    ]
  }
}
```

**Request — PSC_RATING_STRESS_DETAIL_PER_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Detail(Permit)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DETAIL_PER_VBEAM",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "StressRatio/TFactor",
      "AllowableStress/Tens.",
      "Cracked/Uncracked",
      "M_Demand",
      "Mcr",
      "Tendon/Rebar",
      "EffectivestressofTendon",
      "DeadLoadstress",
      "LiveLoadstress"
    ]
  }
}
```

**Response — PSC_RATING_STRESS_DETAIL_PER**

```json
{
  "Stress Rating Detail(Permit)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "StressRatio/TFactor",
      "AllowableStress/Tens.",
      "Cracked/Uncracked",
      "M_Demand",
      "Mcr",
      "Tendon/Rebar",
      "EffectivestressofTendon",
      "DeadLoadstress",
      "LiveLoadstress"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-231.938",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "38875.448"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fx-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-49.572",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "7239.018"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fy-Max)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-191.702",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "31627.731"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fy-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-113.599",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "17868.133"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fz-Max)",
        "-",
        "-",
        "-",
        "0.000",
        "931.496",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fz-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-155.754",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "25226.479"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Mx-Max)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-103.238",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "16095.973"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Mx-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-181.611",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "29820.384"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(My-Max)",
        "-",
        "-",
        "-",
        "0.000",
        "931.496",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(My-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-232.312",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "38938.050"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Mz-Max)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-113.598",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "17868.020"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Mz-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-191.703",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "31627.849"
      ],
      [
        "13",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fx-Max)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-231.938",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "38875.448"
      ],
      [
        "14",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fx-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-49.572",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "7239.018"
      ],
      [
        "15",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fy-Max)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-191.702",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "31627.731"
      ],
      [
        "16",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fy-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-113.599",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "17868.133"
      ],
      [
        "17",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fz-Max)",
        "-",
        "-",
        "-",
        "0.000",
        "931.496",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "18",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fz-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-155.754",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "25226.479"
      ],
      [
        "19",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Mx-Max)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-103.238",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "16095.973"
      ],
      [
        "20",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Mx-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-181.611",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "29820.384"
      ],
      [
        "21",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(My-Max)",
        "-",
        "-",
        "-",
        "0.000",
        "931.496",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "22",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(My-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-232.312",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "38938.050"
      ],
      [
        "23",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Mz-Max)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-113.598",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "17868.020"
      ],
      [
        "24",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Mz-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-191.703",
        "3599.019",
        "Tendon",
        "506277.321",
        "0.000",
        "31627.849"
      ],
      [
        "25",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "-",
        "-",
        "-",
        "716.199",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "26",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fx-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-40.696",
        "3588.088",
        "Tendon",
        "503914.829",
        "0.000",
        "5856.648"
      ],
      [
        "27",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fy-Max)",
        "-",
        "-",
        "-",
        "627.076",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "28",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fy-Min)",
        "-",
        "-",
        "-",
        "337.037",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "29",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fz-Max)",
        "-",
        "-",
        "-",
        "342.151",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "30",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fz-Min)",
        "-",
        "-",
        "-",
        "728.581",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "31",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Mx-Max)",
        "-",
        "-",
        "-",
        "373.653",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "32",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Mx-Min)",
        "-",
        "-",
        "-",
        "521.951",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "33",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(My-Max)",
        "-",
        "-",
        "-",
        "742.867",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "34",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(My-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-40.696",
        "3588.088",
        "Tendon",
        "503914.829",
        "0.000",
        "5856.648"
      ],
      [
        "35",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Mz-Max)",
        "-",
        "-",
        "-",
        "337.037",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "36",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Mz-Min)",
        "-",
        "-",
        "-",
        "627.076",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "37",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fx-Max)",
        "-",
        "-",
        "-",
        "716.199",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "38",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fx-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-40.696",
        "3588.088",
        "Tendon",
        "503914.829",
        "0.000",
        "5856.648"
      ],
      [
        "39",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fy-Max)",
        "-",
        "-",
        "-",
        "627.076",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "40",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fy-Min)",
        "-",
        "-",
        "-",
        "337.037",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "41",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fz-Max)",
        "-",
        "-",
        "-",
        "342.151",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "42",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fz-Min)",
        "-",
        "-",
        "-",
        "728.581",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "43",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Mx-Max)",
        "-",
        "-",
        "-",
        "373.653",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "44",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Mx-Min)",
        "-",
        "-",
        "-",
        "521.951",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "45",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(My-Max)",
        "-",
        "-",
        "-",
        "742.867",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "46",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(My-Min)",
        "Infinite",
        "1675000.000",
        "Uncracked",
        "-40.696",
        "3588.088",
        "Tendon",
        "503914.829",
        "0.000",
        "5856.648"
      ],
      [
        "47",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Mz-Max)",
        "-",
        "-",
        "-",
        "337.037",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ],
      [
        "48",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Mz-Min)",
        "-",
        "-",
        "-",
        "627.076",
        "932.852",
        "-",
        "-",
        "-",
        "-"
      ]
    ]
  }
}
```

**Response — PSC_RATING_STRESS_DETAIL_PER_VBEAM**

```json
{
  "Stress Rating Detail(Permit)": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "StressRatio/TFactor",
      "AllowableStress/Tens.",
      "Cracked/Uncracked",
      "M_Demand",
      "Mcr",
      "Tendon/Rebar",
      "EffectivestressofTendon",
      "DeadLoadstress",
      "LiveLoadstress"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "798.418",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fx-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "710.732",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fy-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1076.833",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fy-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "491.816",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fz-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "698.203",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Fz-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1410.622",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Mx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1410.622",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Mx-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "698.203",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(My-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1492.759",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(My-Min)",
        "Infinite",
        "30000.000",
        "Uncracked",
        "-67.817",
        "10809.377",
        "Tendon",
        "504678.794",
        "0.000",
        "12212.257"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Mz-Max)",
        "Infinite",
        "30000.000",
        "Uncracked",
        "-67.817",
        "10809.377",
        "Tendon",
        "504678.794",
        "0.000",
        "12212.257"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MAX)_A.V(Mz-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1323.704",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "13",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "798.418",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "14",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fx-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "710.732",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "15",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fy-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1076.833",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "16",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fy-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "491.816",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "17",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fz-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "698.203",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "18",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Fz-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1410.622",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "19",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Mx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1410.622",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "20",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Mx-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "698.203",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "21",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(My-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1492.759",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "22",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(My-Min)",
        "Infinite",
        "30000.000",
        "Uncracked",
        "-67.817",
        "10809.377",
        "Tendon",
        "504678.794",
        "0.000",
        "12212.257"
      ],
      [
        "23",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Mz-Max)",
        "Infinite",
        "30000.000",
        "Uncracked",
        "-67.817",
        "10809.377",
        "Tendon",
        "504678.794",
        "0.000",
        "12212.257"
      ],
      [
        "24",
        "Girder",
        "2",
        "I[2]",
        "-",
        "SER_P_DC(MIN)_A.V(Mz-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1323.704",
        "2113.840",
        "Rebar",
        "504678.794",
        "0.000",
        "0.000"
      ],
      [
        "25",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1104.686",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "26",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fx-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1742.235",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "27",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fy-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1619.707",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "28",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fy-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1035.489",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "29",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fz-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1397.943",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "30",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Fz-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Cracked",
        "2140.584",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "31",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Mx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Cracked",
        "2140.584",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "32",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Mx-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1397.943",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "33",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(My-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Cracked",
        "2463.213",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "34",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(My-Min)",
        "Infinite",
        "30000.000",
        "Uncracked",
        "-55.668",
        "10796.106",
        "Tendon",
        "503560.081",
        "0.000",
        "10030.269"
      ],
      [
        "35",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Mz-Max)",
        "Infinite",
        "30000.000",
        "Uncracked",
        "-55.668",
        "10796.106",
        "Tendon",
        "503560.081",
        "0.000",
        "10030.269"
      ],
      [
        "36",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MAX)_A.V(Mz-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Cracked",
        "2463.213",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "37",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1104.686",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "38",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fx-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1742.235",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "39",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fy-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1619.707",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "40",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fy-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1035.489",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "41",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fz-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1397.943",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "42",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Fz-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Cracked",
        "2140.584",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "43",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Mx-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Cracked",
        "2140.584",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "44",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Mx-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Uncracked",
        "1397.943",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "45",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(My-Max)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Cracked",
        "2463.213",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
      ],
      [
        "46",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(My-Min)",
        "Infinite",
        "30000.000",
        "Uncracked",
        "-55.668",
        "10796.106",
        "Tendon",
        "503560.081",
        "0.000",
        "10030.269"
      ],
      [
        "47",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Mz-Max)",
        "Infinite",
        "30000.000",
        "Uncracked",
        "-55.668",
        "10796.106",
        "Tendon",
        "503560.081",
        "0.000",
        "10030.269"
      ],
      [
        "48",
        "Girder",
        "2",
        "J[3]",
        "-",
        "SER_P_DC(MIN)_A.V(Mz-Min)",
        "10000000000000000725314363815292351261583744096465219555182101554790400.000",
        "30000.000",
        "Cracked",
        "2463.213",
        "2114.500",
        "Rebar",
        "503560.081",
        "0.000",
        "0.000"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Stress Rating Detail(Permit)",
    "TABLE_TYPE": "PSC_RATING_STRESS_DETAIL_PER",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "GIRDER_SLAB": "Girder",
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "StressRatio/TFactor",
      "AllowableStress/Tens.",
      "Cracked/Uncracked",
      "M_Demand",
      "Mcr",
      "Tendon/Rebar",
      "EffectivestressofTendon",
      "DeadLoadstress",
      "LiveLoadstress"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 26. `TABLE` · `PSC_RATING_FLEXURE_DETAIL` — Flexural Strength Rating Detail

> **기능** 휨강도 평가 상세 결과를 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738538376345](https://support.midasuser.com/hc/en-us/articles/64738538376345)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Flexural Capacity Demand Ratio: "PSC_RATING_FLEXURE_DETAIL" · Flexural Capacity Demand Ratio - Virtual Beam: "PSC_RATING_FLEXURE_DETAIL_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 3.1 | └ [General] Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned. | `"KEYS"` | array | - | Optional |
| 3.2 | └ [General] Specify ID Range (e.g., '1to5') | `"TO"` | string | - | Optional |
| 4 | [General] Element Parts | `"PARTS"` | array | - | Optional |
| 5 | [General] Rating Case | `"RATING_CASE"` | array | - | Optional |
| 6 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 7 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 7.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 7.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 7.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 7.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 8 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 8.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 8.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 9 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_FLEXURE_DETAIL",
            "PSC_RATING_FLEXURE_DETAIL_VBEAM"
          ]
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input. Use KEYS or TO, not both (sending both returns an error).",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned.",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to5')"
            }
          },
          "additionalProperties": false
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "Part I",
              "Part J"
            ]
          }
        },
        "RATING_CASE": {
          "type": "array",
          "description": "Rating case name filter (names defined in Define Rating Case). Only Strength limit state cases apply (Design Live, Legal and Permit). Matching ignores case and spaces. Names that do not match are ignored; if none match, the result is empty. Omit (or []) for all cases.",
          "items": {
            "type": "string"
          }
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Requesting one column of a group (e.g. \"DC/Factor\", \"ReinforcementRequirement/min\") returns the whole group. Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Group",
              "Elem.",
              "Part",
              "RelativeLocation",
              "RatingCase",
              "RatingLevel",
              "RatingFactor",
              "Mn",
              "Areas/Rebar",
              "Areas/Tendon",
              "ReinforcementRequirement/min",
              "ReinforcementRequirement/max",
              "DC/Factor",
              "DC/Force",
              "DW/Factor",
              "DW/Force",
              "Temperature/Factor",
              "Temperature/Force",
              "T.Gradient/Factor",
              "T.Gradient/Force",
              "Permanent/Factor",
              "Permanent/Force",
              "Secondary/Factor",
              "Secondary/Force",
              "UserDefined/Factor",
              "UserDefined/Force",
              "Pri.LL/Factor",
              "Pri.LL/Force",
              "AdjLL/Factor",
              "AdjLL/Force"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Flexural Strength Rating Detail` — `Index`, `Group`, `Elem.`, `Part`, `RelativeLocation`, `RatingCase`, `RatingLevel`, `RatingFactor`, `Mn`, `Areas/Rebar`, `Areas/Tendon`, `ReinforcementRequirement/min`, `ReinforcementRequirement/max`, `DC/Factor`, `DC/Force`, `DW/Factor`, `DW/Force`, `Temperature/Factor`, `Temperature/Force`, `T.Gradient/Factor`, `T.Gradient/Force`, `Permanent/Factor`, `Permanent/Force`, `Secondary/Factor`, `Secondary/Force`, `UserDefined/Factor`, `UserDefined/Force`, `Pri.LL/Factor`, `Pri.LL/Force`, `AdjLL/Factor`, `AdjLL/Force`

### Request / Response JSON

**Request — PSC_RATING_FLEXURE_DETAIL**

```json
{
  "Argument": {
    "TABLE_NAME": "Flexural Strength Rating Detail",
    "TABLE_TYPE": "PSC_RATING_FLEXURE_DETAIL",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "RatingFactor",
      "Mn",
      "Areas/Rebar",
      "Areas/Tendon",
      "ReinforcementRequirement/min",
      "ReinforcementRequirement/max",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
```

**Request — PSC_RATING_FLEXURE_DETAIL_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Flexural Strength Rating Detail",
    "TABLE_TYPE": "PSC_RATING_FLEXURE_DETAIL_VBEAM",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "RatingFactor",
      "Mn",
      "Areas/Rebar",
      "Areas/Tendon",
      "ReinforcementRequirement/min",
      "ReinforcementRequirement/max",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
```

**Response — PSC_RATING_FLEXURE_DETAIL**

```json
{
  "Flexural Strength Rating Detail": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "RatingFactor",
      "Mn",
      "Areas/Rebar",
      "Areas/Tendon",
      "ReinforcementRequirement/min",
      "ReinforcementRequirement/max",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Max)",
        "Design Live",
        "63.872",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-115.969",
        "1.000",
        "-115.969"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Min)",
        "Design Live",
        "302.527",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-24.786",
        "1.000",
        "-24.786"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Max)",
        "Design Live",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Min)",
        "Design Live",
        "131.452",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Max)",
        "Design Live",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "95.603",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-77.877",
        "1.000",
        "-77.877"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Max)",
        "Design Live",
        "144.745",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-51.619",
        "1.000",
        "-51.619"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Min)",
        "Design Live",
        "81.849",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-90.806",
        "1.000",
        "-90.806"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "63.768",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-116.156",
        "1.000",
        "-116.156"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Max)",
        "Design Live",
        "131.453",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Min)",
        "Design Live",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "13",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Max)",
        "Design Live",
        "63.872",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-115.969",
        "1.000",
        "-115.969"
      ],
      [
        "14",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Min)",
        "Design Live",
        "302.527",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-24.786",
        "1.000",
        "-24.786"
      ],
      [
        "15",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Max)",
        "Design Live",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "16",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Min)",
        "Design Live",
        "131.452",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "17",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Max)",
        "Design Live",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "18",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Min)",
        "Design Live",
        "95.603",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-77.877",
        "1.000",
        "-77.877"
      ],
      [
        "19",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Max)",
        "Design Live",
        "144.745",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-51.619",
        "1.000",
        "-51.619"
      ],
      [
        "20",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Min)",
        "Design Live",
        "81.849",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-90.806",
        "1.000",
        "-90.806"
      ],
      [
        "21",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(My-Max)",
        "Design Live",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "22",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(My-Min)",
        "Design Live",
        "63.768",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-116.156",
        "1.000",
        "-116.156"
      ],
      [
        "23",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Max)",
        "Design Live",
        "131.453",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "24",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Min)",
        "Design Live",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "25",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Max)",
        "Legal",
        "63.872",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-115.969",
        "1.000",
        "-115.969"
      ],
      [
        "26",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Min)",
        "Legal",
        "302.527",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-24.786",
        "1.000",
        "-24.786"
      ],
      [
        "27",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Max)",
        "Legal",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "28",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Min)",
        "Legal",
        "131.452",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "29",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Max)",
        "Legal",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "30",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "95.603",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-77.877",
        "1.000",
        "-77.877"
      ],
      [
        "31",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Max)",
        "Legal",
        "144.745",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-51.619",
        "1.000",
        "-51.619"
      ],
      [
        "32",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Min)",
        "Legal",
        "81.849",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-90.806",
        "1.000",
        "-90.806"
      ],
      [
        "33",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "34",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "63.768",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-116.156",
        "1.000",
        "-116.156"
      ],
      [
        "35",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Max)",
        "Legal",
        "131.453",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "36",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Min)",
        "Legal",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "37",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Max)",
        "Legal",
        "63.872",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-115.969",
        "1.000",
        "-115.969"
      ],
      [
        "38",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Min)",
        "Legal",
        "302.527",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-24.786",
        "1.000",
        "-24.786"
      ],
      [
        "39",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Max)",
        "Legal",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "40",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Min)",
        "Legal",
        "131.452",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "41",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Max)",
        "Legal",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "42",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Min)",
        "Legal",
        "95.603",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-77.877",
        "1.000",
        "-77.877"
      ],
      [
        "43",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Max)",
        "Legal",
        "144.745",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-51.619",
        "1.000",
        "-51.619"
      ],
      [
        "44",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Min)",
        "Legal",
        "81.849",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-90.806",
        "1.000",
        "-90.806"
      ],
      [
        "45",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Max)",
        "Legal",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "46",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Min)",
        "Legal",
        "63.768",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-116.156",
        "1.000",
        "-116.156"
      ],
      [
        "47",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Max)",
        "Legal",
        "131.453",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "48",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Min)",
        "Legal",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "49",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Max)",
        "Permit",
        "63.872",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-115.969",
        "1.000",
        "-115.969"
      ],
      [
        "50",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Min)",
        "Permit",
        "302.527",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-24.786",
        "1.000",
        "-24.786"
      ],
      [
        "51",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Max)",
        "Permit",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "52",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Min)",
        "Permit",
        "131.452",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "53",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Max)",
        "Permit",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "54",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "95.603",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-77.877",
        "1.000",
        "-77.877"
      ],
      [
        "55",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Max)",
        "Permit",
        "144.745",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-51.619",
        "1.000",
        "-51.619"
      ],
      [
        "56",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Min)",
        "Permit",
        "81.849",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-90.806",
        "1.000",
        "-90.806"
      ],
      [
        "57",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "58",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "63.768",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-116.156",
        "1.000",
        "-116.156"
      ],
      [
        "59",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Max)",
        "Permit",
        "131.453",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "60",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Min)",
        "Permit",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "61",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Max)",
        "Permit",
        "63.872",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-115.969",
        "1.000",
        "-115.969"
      ],
      [
        "62",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Min)",
        "Permit",
        "302.527",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-24.786",
        "1.000",
        "-24.786"
      ],
      [
        "63",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Max)",
        "Permit",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ],
      [
        "64",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Min)",
        "Permit",
        "131.452",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "65",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Max)",
        "Permit",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "66",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Min)",
        "Permit",
        "95.603",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-77.877",
        "1.000",
        "-77.877"
      ],
      [
        "67",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Max)",
        "Permit",
        "144.745",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-51.619",
        "1.000",
        "-51.619"
      ],
      [
        "68",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Min)",
        "Permit",
        "81.849",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-90.806",
        "1.000",
        "-90.806"
      ],
      [
        "69",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Max)",
        "Permit",
        "-",
        "-",
        "0.000",
        "0.000",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "70",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Min)",
        "Permit",
        "63.768",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-116.156",
        "1.000",
        "-116.156"
      ],
      [
        "71",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Max)",
        "Permit",
        "131.453",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-56.799",
        "1.000",
        "-56.799"
      ],
      [
        "72",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Min)",
        "Permit",
        "77.488",
        "7715.874",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-95.851",
        "1.000",
        "-95.851"
      ]
    ]
  }
}
```

**Response — PSC_RATING_FLEXURE_DETAIL_VBEAM**

```json
{
  "Flexural Strength Rating Detail": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "RatingFactor",
      "Mn",
      "Areas/Rebar",
      "Areas/Tendon",
      "ReinforcementRequirement/min",
      "ReinforcementRequirement/max",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Max)",
        "Design Live",
        "17.091",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "399.209",
        "1.000",
        "399.209"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Min)",
        "Design Live",
        "19.323",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "355.366",
        "1.000",
        "355.366"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Max)",
        "Design Live",
        "12.414",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "538.417",
        "1.000",
        "538.417"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Min)",
        "Design Live",
        "28.370",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "245.908",
        "1.000",
        "245.908"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Max)",
        "Design Live",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Max)",
        "Design Live",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Min)",
        "Design Live",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "8.676",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "746.380",
        "1.000",
        "746.380"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Max)",
        "Design Live",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Min)",
        "Design Live",
        "9.912",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "661.852",
        "1.000",
        "661.852"
      ],
      [
        "13",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Max)",
        "Design Live",
        "17.091",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "399.209",
        "1.000",
        "399.209"
      ],
      [
        "14",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Min)",
        "Design Live",
        "19.323",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "355.366",
        "1.000",
        "355.366"
      ],
      [
        "15",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Max)",
        "Design Live",
        "12.414",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "538.417",
        "1.000",
        "538.417"
      ],
      [
        "16",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Min)",
        "Design Live",
        "28.370",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "245.908",
        "1.000",
        "245.908"
      ],
      [
        "17",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Max)",
        "Design Live",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "18",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Min)",
        "Design Live",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "19",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Max)",
        "Design Live",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "20",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Min)",
        "Design Live",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "21",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(My-Max)",
        "Design Live",
        "8.676",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "746.380",
        "1.000",
        "746.380"
      ],
      [
        "22",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(My-Min)",
        "Design Live",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "23",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Max)",
        "Design Live",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "24",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Min)",
        "Design Live",
        "9.912",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "661.852",
        "1.000",
        "661.852"
      ],
      [
        "25",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Max)",
        "Legal",
        "17.091",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "399.209",
        "1.000",
        "399.209"
      ],
      [
        "26",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Min)",
        "Legal",
        "19.323",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "355.366",
        "1.000",
        "355.366"
      ],
      [
        "27",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Max)",
        "Legal",
        "12.414",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "538.417",
        "1.000",
        "538.417"
      ],
      [
        "28",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Min)",
        "Legal",
        "28.370",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "245.908",
        "1.000",
        "245.908"
      ],
      [
        "29",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Max)",
        "Legal",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "30",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "31",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Max)",
        "Legal",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "32",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Min)",
        "Legal",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "33",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "8.676",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "746.380",
        "1.000",
        "746.380"
      ],
      [
        "34",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "35",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Max)",
        "Legal",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "36",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Min)",
        "Legal",
        "9.912",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "661.852",
        "1.000",
        "661.852"
      ],
      [
        "37",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Max)",
        "Legal",
        "17.091",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "399.209",
        "1.000",
        "399.209"
      ],
      [
        "38",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Min)",
        "Legal",
        "19.323",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "355.366",
        "1.000",
        "355.366"
      ],
      [
        "39",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Max)",
        "Legal",
        "12.414",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "538.417",
        "1.000",
        "538.417"
      ],
      [
        "40",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Min)",
        "Legal",
        "28.370",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "245.908",
        "1.000",
        "245.908"
      ],
      [
        "41",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Max)",
        "Legal",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "42",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Min)",
        "Legal",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "43",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Max)",
        "Legal",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "44",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Min)",
        "Legal",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "45",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Max)",
        "Legal",
        "8.676",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "746.380",
        "1.000",
        "746.380"
      ],
      [
        "46",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Min)",
        "Legal",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "47",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Max)",
        "Legal",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "48",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Min)",
        "Legal",
        "9.912",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "661.852",
        "1.000",
        "661.852"
      ],
      [
        "49",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Max)",
        "Permit",
        "17.091",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "399.209",
        "1.000",
        "399.209"
      ],
      [
        "50",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Min)",
        "Permit",
        "19.323",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "355.366",
        "1.000",
        "355.366"
      ],
      [
        "51",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Max)",
        "Permit",
        "12.414",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "538.417",
        "1.000",
        "538.417"
      ],
      [
        "52",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Min)",
        "Permit",
        "28.370",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "245.908",
        "1.000",
        "245.908"
      ],
      [
        "53",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Max)",
        "Permit",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "54",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "55",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Max)",
        "Permit",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "56",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Min)",
        "Permit",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "57",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "8.676",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "746.380",
        "1.000",
        "746.380"
      ],
      [
        "58",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "59",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Max)",
        "Permit",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "60",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Min)",
        "Permit",
        "9.912",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "661.852",
        "1.000",
        "661.852"
      ],
      [
        "61",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Max)",
        "Permit",
        "17.091",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "399.209",
        "1.000",
        "399.209"
      ],
      [
        "62",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Min)",
        "Permit",
        "19.323",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "355.366",
        "1.000",
        "355.366"
      ],
      [
        "63",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Max)",
        "Permit",
        "12.414",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "538.417",
        "1.000",
        "538.417"
      ],
      [
        "64",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Min)",
        "Permit",
        "28.370",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "245.908",
        "1.000",
        "245.908"
      ],
      [
        "65",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Max)",
        "Permit",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "66",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Min)",
        "Permit",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "67",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Max)",
        "Permit",
        "9.240",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "705.311",
        "1.000",
        "705.311"
      ],
      [
        "68",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Min)",
        "Permit",
        "19.688",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "349.102",
        "1.000",
        "349.102"
      ],
      [
        "69",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Max)",
        "Permit",
        "8.676",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "746.380",
        "1.000",
        "746.380"
      ],
      [
        "70",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Min)",
        "Permit",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "71",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Max)",
        "Permit",
        "257.665",
        "8770.885",
        "0.000",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-33.908",
        "1.000",
        "-33.908"
      ],
      [
        "72",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Min)",
        "Permit",
        "9.912",
        "7222.265",
        "0.006",
        "0.004",
        "NG",
        "NG",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "661.852",
        "1.000",
        "661.852"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Flexural Strength Rating Detail",
    "TABLE_TYPE": "PSC_RATING_FLEXURE_DETAIL",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "RatingFactor",
      "Mn",
      "Areas/Rebar",
      "Areas/Tendon",
      "ReinforcementRequirement/min",
      "ReinforcementRequirement/max",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 27. `TABLE` · `PSC_RATING_SHEAR_DETAIL` — Shear Strength Rating Detail

> **기능** 전단강도 평가 상세 결과를 조회합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738404144537](https://support.midasuser.com/hc/en-us/articles/64738404144537)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | empty | Optional |
| 2 | [General] Table Type · Shear Strength Data: "PSC_RATING_SHEAR_DETAIL" · Shear Strength Data - Virtual Beam: "PSC_RATING_SHEAR_DETAIL_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Node/Element Selection | `"NODE_ELEMS"` | object | - | Optional |
| 3.1 | └ [General] Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned. | `"KEYS"` | array | - | Optional |
| 3.2 | └ [General] Specify ID Range (e.g., '1to5') | `"TO"` | string | - | Optional |
| 4 | [General] Element Parts | `"PARTS"` | array | - | Optional |
| 5 | [General] Rating Case | `"RATING_CASE"` | array | - | Optional |
| 6 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 7 | [General] Unit Settings | `"UNIT"` | object | System | Optional |
| 7.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 7.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 7.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 7.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 8 | [General] Number Format | `"STYLES"` | object | System | Optional |
| 8.1 | └ Number format · Default · Fixed · Scientific · General | `"FORMAT"` | string | - | Optional |
| 8.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 9 | [General] Components | `"COMPONENTS"` | array | - | Optional |

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
          "default": "empty"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "PSC Rating Result Table Type",
          "enum": [
            "PSC_RATING_SHEAR_DETAIL",
            "PSC_RATING_SHEAR_DETAIL_VBEAM"
          ]
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input. Use KEYS or TO, not both (sending both returns an error).",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID. IDs without rating results are ignored; if none match (or the list is empty), all elements are returned.",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to5')"
            }
          },
          "additionalProperties": false
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "Part I",
              "Part J"
            ]
          }
        },
        "RATING_CASE": {
          "type": "array",
          "description": "Rating case name filter (names defined in Define Rating Case). Only Strength limit state cases apply (Design Live, Legal and Permit). Matching ignores case and spaces. Names that do not match are ignored; if none match, the result is empty. Omit (or []) for all cases.",
          "items": {
            "type": "string"
          }
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
          "description": "Components of Result Table. Omit to get all columns. \"Index\" is always returned and cannot be requested alone. Requesting one column of a group (e.g. \"DC/Factor\", \"Pri.LL/Factor\") returns the whole group. Unknown names are dropped.",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Group",
              "Elem.",
              "Part",
              "RelativeLocation",
              "RatingCase",
              "RatingLevel",
              "RatingFactor",
              "Vn",
              "DC/Factor",
              "DC/Force",
              "DW/Factor",
              "DW/Force",
              "Temperature/Factor",
              "Temperature/Force",
              "T.Gradient/Factor",
              "T.Gradient/Force",
              "Permanent/Factor",
              "Permanent/Force",
              "Secondary/Factor",
              "Secondary/Force",
              "UserDefined/Factor",
              "UserDefined/Force",
              "Pri.LL/Factor",
              "Pri.LL/Force",
              "AdjLL/Factor",
              "AdjLL/Force"
            ]
          }
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `Shear Strength Rating Detail` — `Index`, `Group`, `Elem.`, `Part`, `RelativeLocation`, `RatingCase`, `RatingLevel`, `RatingFactor`, `Vn`, `DC/Factor`, `DC/Force`, `DW/Factor`, `DW/Force`, `Temperature/Factor`, `Temperature/Force`, `T.Gradient/Factor`, `T.Gradient/Force`, `Permanent/Factor`, `Permanent/Force`, `Secondary/Factor`, `Secondary/Force`, `UserDefined/Factor`, `UserDefined/Force`, `Pri.LL/Factor`, `Pri.LL/Force`, `AdjLL/Factor`, `AdjLL/Force`

### Request / Response JSON

**Request — PSC_RATING_SHEAR_DETAIL**

```json
{
  "Argument": {
    "TABLE_NAME": "Shear Strength Rating Detail",
    "TABLE_TYPE": "PSC_RATING_SHEAR_DETAIL",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "RatingFactor",
      "Vn",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
```

**Request — PSC_RATING_SHEAR_DETAIL_VBEAM**

```json
{
  "Argument": {
    "TABLE_NAME": "Shear Strength Rating Detail",
    "TABLE_TYPE": "PSC_RATING_SHEAR_DETAIL_VBEAM",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "RatingFactor",
      "Vn",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
```

**Response — PSC_RATING_SHEAR_DETAIL**

```json
{
  "Shear Strength Rating Detail": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "RatingFactor",
      "Vn",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Max)",
        "Design Live",
        "0.494",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.238",
        "1.000",
        "-352.238"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Min)",
        "Design Live",
        "162.182",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Max)",
        "Design Live",
        "0.724",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.232",
        "1.000",
        "-305.232"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Min)",
        "Design Live",
        "2.214",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Max)",
        "Design Live",
        "-",
        "-",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "0.318",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-399.248",
        "1.000",
        "-399.248"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Max)",
        "Design Live",
        "1.908",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-181.000",
        "1.000",
        "-181.000"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Min)",
        "Design Live",
        "1.059",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "-",
        "-",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "0.494",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.262",
        "1.000",
        "-352.262"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Max)",
        "Design Live",
        "2.214",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.748",
        "1.000",
        "-163.748"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Min)",
        "Design Live",
        "0.724",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.233",
        "1.000",
        "-305.233"
      ],
      [
        "13",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Max)",
        "Design Live",
        "0.494",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.238",
        "1.000",
        "-352.238"
      ],
      [
        "14",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Min)",
        "Design Live",
        "162.182",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "15",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Max)",
        "Design Live",
        "0.724",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.232",
        "1.000",
        "-305.232"
      ],
      [
        "16",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Min)",
        "Design Live",
        "2.214",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "17",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Max)",
        "Design Live",
        "-",
        "-",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "18",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Min)",
        "Design Live",
        "0.318",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-399.248",
        "1.000",
        "-399.248"
      ],
      [
        "19",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Max)",
        "Design Live",
        "1.908",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-181.000",
        "1.000",
        "-181.000"
      ],
      [
        "20",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Min)",
        "Design Live",
        "1.059",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "21",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(My-Max)",
        "Design Live",
        "-",
        "-",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "22",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(My-Min)",
        "Design Live",
        "0.494",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.262",
        "1.000",
        "-352.262"
      ],
      [
        "23",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Max)",
        "Design Live",
        "2.214",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.748",
        "1.000",
        "-163.748"
      ],
      [
        "24",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Min)",
        "Design Live",
        "0.724",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.233",
        "1.000",
        "-305.233"
      ],
      [
        "25",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Max)",
        "Legal",
        "0.494",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.238",
        "1.000",
        "-352.238"
      ],
      [
        "26",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Min)",
        "Legal",
        "162.182",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "27",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Max)",
        "Legal",
        "0.724",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.232",
        "1.000",
        "-305.232"
      ],
      [
        "28",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Min)",
        "Legal",
        "2.214",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "29",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Max)",
        "Legal",
        "-",
        "-",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "30",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "0.318",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-399.248",
        "1.000",
        "-399.248"
      ],
      [
        "31",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Max)",
        "Legal",
        "1.908",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-181.000",
        "1.000",
        "-181.000"
      ],
      [
        "32",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Min)",
        "Legal",
        "1.059",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "33",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "-",
        "-",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "34",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "0.494",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.262",
        "1.000",
        "-352.262"
      ],
      [
        "35",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Max)",
        "Legal",
        "2.214",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.748",
        "1.000",
        "-163.748"
      ],
      [
        "36",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Min)",
        "Legal",
        "0.724",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.233",
        "1.000",
        "-305.233"
      ],
      [
        "37",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Max)",
        "Legal",
        "0.494",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.238",
        "1.000",
        "-352.238"
      ],
      [
        "38",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Min)",
        "Legal",
        "162.182",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "39",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Max)",
        "Legal",
        "0.724",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.232",
        "1.000",
        "-305.232"
      ],
      [
        "40",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Min)",
        "Legal",
        "2.214",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "41",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Max)",
        "Legal",
        "-",
        "-",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "42",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Min)",
        "Legal",
        "0.318",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-399.248",
        "1.000",
        "-399.248"
      ],
      [
        "43",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Max)",
        "Legal",
        "1.908",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-181.000",
        "1.000",
        "-181.000"
      ],
      [
        "44",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Min)",
        "Legal",
        "1.059",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "45",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Max)",
        "Legal",
        "-",
        "-",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "46",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Min)",
        "Legal",
        "0.494",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.262",
        "1.000",
        "-352.262"
      ],
      [
        "47",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Max)",
        "Legal",
        "2.214",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.748",
        "1.000",
        "-163.748"
      ],
      [
        "48",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Min)",
        "Legal",
        "0.724",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.233",
        "1.000",
        "-305.233"
      ],
      [
        "49",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Max)",
        "Permit",
        "0.494",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.238",
        "1.000",
        "-352.238"
      ],
      [
        "50",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Min)",
        "Permit",
        "162.182",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "51",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Max)",
        "Permit",
        "0.724",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.232",
        "1.000",
        "-305.232"
      ],
      [
        "52",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Min)",
        "Permit",
        "2.214",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "53",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Max)",
        "Permit",
        "-",
        "-",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "54",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "0.318",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-399.248",
        "1.000",
        "-399.248"
      ],
      [
        "55",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Max)",
        "Permit",
        "1.908",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-181.000",
        "1.000",
        "-181.000"
      ],
      [
        "56",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Min)",
        "Permit",
        "1.059",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "57",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "-",
        "-",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "58",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "0.494",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.262",
        "1.000",
        "-352.262"
      ],
      [
        "59",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Max)",
        "Permit",
        "2.214",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.748",
        "1.000",
        "-163.748"
      ],
      [
        "60",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Min)",
        "Permit",
        "0.724",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.233",
        "1.000",
        "-305.233"
      ],
      [
        "61",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Max)",
        "Permit",
        "0.494",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.238",
        "1.000",
        "-352.238"
      ],
      [
        "62",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Min)",
        "Permit",
        "162.182",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "63",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Max)",
        "Permit",
        "0.724",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.232",
        "1.000",
        "-305.232"
      ],
      [
        "64",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Min)",
        "Permit",
        "2.214",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "65",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Max)",
        "Permit",
        "-",
        "-",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "66",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Min)",
        "Permit",
        "0.318",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-399.248",
        "1.000",
        "-399.248"
      ],
      [
        "67",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Max)",
        "Permit",
        "1.908",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-181.000",
        "1.000",
        "-181.000"
      ],
      [
        "68",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Min)",
        "Permit",
        "1.059",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "69",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Max)",
        "Permit",
        "-",
        "-",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000"
      ],
      [
        "70",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Min)",
        "Permit",
        "0.494",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-352.262",
        "1.000",
        "-352.262"
      ],
      [
        "71",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Max)",
        "Permit",
        "2.214",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.748",
        "1.000",
        "-163.748"
      ],
      [
        "72",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Min)",
        "Permit",
        "0.724",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-305.233",
        "1.000",
        "-305.233"
      ],
      [
        "73",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Max)",
        "Design Live",
        "-0.728",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-336.816",
        "1.000",
        "-336.816"
      ],
      [
        "74",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Min)",
        "Design Live",
        "162.182",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "75",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Max)",
        "Design Live",
        "-0.230",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "76",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Min)",
        "Design Live",
        "-0.441",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "77",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Max)",
        "Design Live",
        "3.527",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "20.227",
        "1.000",
        "20.227"
      ],
      [
        "78",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "-0.736",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-347.162",
        "1.000",
        "-347.162"
      ],
      [
        "79",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Max)",
        "Design Live",
        "16.496",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "5.234",
        "1.000",
        "5.234"
      ],
      [
        "80",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Min)",
        "Design Live",
        "-0.642",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "81",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "-0.478",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-175.449",
        "1.000",
        "-175.449"
      ],
      [
        "82",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "162.182",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "83",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Max)",
        "Design Live",
        "-0.441",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "84",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Min)",
        "Design Live",
        "-0.230",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "85",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Max)",
        "Design Live",
        "-0.728",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-336.816",
        "1.000",
        "-336.816"
      ],
      [
        "86",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Min)",
        "Design Live",
        "162.182",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "87",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Max)",
        "Design Live",
        "-0.230",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "88",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Min)",
        "Design Live",
        "-0.441",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "89",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Max)",
        "Design Live",
        "3.527",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "20.227",
        "1.000",
        "20.227"
      ],
      [
        "90",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Min)",
        "Design Live",
        "-0.736",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-347.162",
        "1.000",
        "-347.162"
      ],
      [
        "91",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Max)",
        "Design Live",
        "16.496",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "5.234",
        "1.000",
        "5.234"
      ],
      [
        "92",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Min)",
        "Design Live",
        "-0.642",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "93",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(My-Max)",
        "Design Live",
        "-0.478",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-175.449",
        "1.000",
        "-175.449"
      ],
      [
        "94",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(My-Min)",
        "Design Live",
        "162.182",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "95",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Max)",
        "Design Live",
        "-0.441",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "96",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Min)",
        "Design Live",
        "-0.230",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "97",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Max)",
        "Legal",
        "-0.728",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-336.816",
        "1.000",
        "-336.816"
      ],
      [
        "98",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Min)",
        "Legal",
        "162.182",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "99",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Max)",
        "Legal",
        "-0.230",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "100",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Min)",
        "Legal",
        "-0.441",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "101",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Max)",
        "Legal",
        "3.527",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "20.227",
        "1.000",
        "20.227"
      ],
      [
        "102",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "-0.736",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-347.162",
        "1.000",
        "-347.162"
      ],
      [
        "103",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Max)",
        "Legal",
        "16.496",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "5.234",
        "1.000",
        "5.234"
      ],
      [
        "104",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Min)",
        "Legal",
        "-0.642",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "105",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "-0.478",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-175.449",
        "1.000",
        "-175.449"
      ],
      [
        "106",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "162.182",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "107",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Max)",
        "Legal",
        "-0.441",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "108",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Min)",
        "Legal",
        "-0.230",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "109",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Max)",
        "Legal",
        "-0.728",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-336.816",
        "1.000",
        "-336.816"
      ],
      [
        "110",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Min)",
        "Legal",
        "162.182",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "111",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Max)",
        "Legal",
        "-0.230",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "112",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Min)",
        "Legal",
        "-0.441",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "113",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Max)",
        "Legal",
        "3.527",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "20.227",
        "1.000",
        "20.227"
      ],
      [
        "114",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Min)",
        "Legal",
        "-0.736",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-347.162",
        "1.000",
        "-347.162"
      ],
      [
        "115",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Max)",
        "Legal",
        "16.496",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "5.234",
        "1.000",
        "5.234"
      ],
      [
        "116",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Min)",
        "Legal",
        "-0.642",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "117",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Max)",
        "Legal",
        "-0.478",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-175.449",
        "1.000",
        "-175.449"
      ],
      [
        "118",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Min)",
        "Legal",
        "162.182",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "119",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Max)",
        "Legal",
        "-0.441",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "120",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Min)",
        "Legal",
        "-0.230",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "121",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Max)",
        "Permit",
        "-0.728",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-336.816",
        "1.000",
        "-336.816"
      ],
      [
        "122",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Min)",
        "Permit",
        "162.182",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "123",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Max)",
        "Permit",
        "-0.230",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "124",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Min)",
        "Permit",
        "-0.441",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "125",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Max)",
        "Permit",
        "3.527",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "20.227",
        "1.000",
        "20.227"
      ],
      [
        "126",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "-0.736",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-347.162",
        "1.000",
        "-347.162"
      ],
      [
        "127",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Max)",
        "Permit",
        "16.496",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "5.234",
        "1.000",
        "5.234"
      ],
      [
        "128",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Min)",
        "Permit",
        "-0.642",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "129",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "-0.478",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-175.449",
        "1.000",
        "-175.449"
      ],
      [
        "130",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "162.182",
        "584.782",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "131",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Max)",
        "Permit",
        "-0.441",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "132",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Min)",
        "Permit",
        "-0.230",
        "101.751",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "133",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Max)",
        "Permit",
        "-0.728",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-336.816",
        "1.000",
        "-336.816"
      ],
      [
        "134",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Min)",
        "Permit",
        "162.182",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "135",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Max)",
        "Permit",
        "-0.230",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ],
      [
        "136",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Min)",
        "Permit",
        "-0.441",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "137",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Max)",
        "Permit",
        "3.527",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "20.227",
        "1.000",
        "20.227"
      ],
      [
        "138",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Min)",
        "Permit",
        "-0.736",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-347.162",
        "1.000",
        "-347.162"
      ],
      [
        "139",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Max)",
        "Permit",
        "16.496",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "5.234",
        "1.000",
        "5.234"
      ],
      [
        "140",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Min)",
        "Permit",
        "-0.642",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-255.655",
        "1.000",
        "-255.655"
      ],
      [
        "141",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Max)",
        "Permit",
        "-0.478",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-175.449",
        "1.000",
        "-175.449"
      ],
      [
        "142",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Min)",
        "Permit",
        "162.182",
        "584.782",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-3.225",
        "1.000",
        "-3.225"
      ],
      [
        "143",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Max)",
        "Permit",
        "-0.441",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-163.749",
        "1.000",
        "-163.749"
      ],
      [
        "144",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Min)",
        "Permit",
        "-0.230",
        "101.751",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-118.998",
        "1.000",
        "-118.998"
      ]
    ]
  }
}
```

**Response — PSC_RATING_SHEAR_DETAIL_VBEAM**

```json
{
  "Shear Strength Rating Detail": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "RatingFactor",
      "Vn",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ],
    "DATA": [
      [
        "1",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Max)",
        "Design Live",
        "104.237",
        "488.880",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "4.181",
        "1.000",
        "4.181"
      ],
      [
        "2",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Min)",
        "Design Live",
        "1.428",
        "434.292",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-161.005",
        "1.000",
        "-161.005"
      ],
      [
        "3",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Max)",
        "Design Live",
        "1.964",
        "405.877",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-123.249",
        "1.000",
        "-123.249"
      ],
      [
        "4",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Min)",
        "Design Live",
        "2.916",
        "484.996",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "5",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Max)",
        "Design Live",
        "16.369",
        "494.179",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "6",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "-0.079",
        "325.765",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "7",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Max)",
        "Design Live",
        "-0.079",
        "325.765",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "8",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Min)",
        "Design Live",
        "16.369",
        "494.179",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "9",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "1.107",
        "358.131",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-152.981",
        "1.000",
        "-152.981"
      ],
      [
        "10",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "11",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Max)",
        "Design Live",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "12",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Min)",
        "Design Live",
        "0.069",
        "339.193",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-285.528",
        "1.000",
        "-285.528"
      ],
      [
        "13",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Max)",
        "Design Live",
        "104.237",
        "488.880",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "4.181",
        "1.000",
        "4.181"
      ],
      [
        "14",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Min)",
        "Design Live",
        "1.428",
        "434.292",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-161.005",
        "1.000",
        "-161.005"
      ],
      [
        "15",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Max)",
        "Design Live",
        "1.964",
        "405.877",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-123.249",
        "1.000",
        "-123.249"
      ],
      [
        "16",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Min)",
        "Design Live",
        "2.916",
        "484.996",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "17",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Max)",
        "Design Live",
        "16.369",
        "494.179",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "18",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Min)",
        "Design Live",
        "-0.079",
        "325.765",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "19",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Max)",
        "Design Live",
        "-0.079",
        "325.765",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "20",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Min)",
        "Design Live",
        "16.369",
        "494.179",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "21",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(My-Max)",
        "Design Live",
        "1.107",
        "358.131",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-152.981",
        "1.000",
        "-152.981"
      ],
      [
        "22",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(My-Min)",
        "Design Live",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "23",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Max)",
        "Design Live",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "24",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Min)",
        "Design Live",
        "0.069",
        "339.193",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-285.528",
        "1.000",
        "-285.528"
      ],
      [
        "25",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Max)",
        "Legal",
        "104.237",
        "488.880",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "4.181",
        "1.000",
        "4.181"
      ],
      [
        "26",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Min)",
        "Legal",
        "1.428",
        "434.292",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-161.005",
        "1.000",
        "-161.005"
      ],
      [
        "27",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Max)",
        "Legal",
        "1.964",
        "405.877",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-123.249",
        "1.000",
        "-123.249"
      ],
      [
        "28",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Min)",
        "Legal",
        "2.916",
        "484.996",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "29",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Max)",
        "Legal",
        "16.369",
        "494.179",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "30",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "-0.079",
        "325.765",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "31",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Max)",
        "Legal",
        "-0.079",
        "325.765",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "32",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Min)",
        "Legal",
        "16.369",
        "494.179",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "33",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "1.107",
        "358.131",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-152.981",
        "1.000",
        "-152.981"
      ],
      [
        "34",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "35",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Max)",
        "Legal",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "36",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Min)",
        "Legal",
        "0.069",
        "339.193",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-285.528",
        "1.000",
        "-285.528"
      ],
      [
        "37",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Max)",
        "Legal",
        "104.237",
        "488.880",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "4.181",
        "1.000",
        "4.181"
      ],
      [
        "38",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Min)",
        "Legal",
        "1.428",
        "434.292",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-161.005",
        "1.000",
        "-161.005"
      ],
      [
        "39",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Max)",
        "Legal",
        "1.964",
        "405.877",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-123.249",
        "1.000",
        "-123.249"
      ],
      [
        "40",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Min)",
        "Legal",
        "2.916",
        "484.996",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "41",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Max)",
        "Legal",
        "16.369",
        "494.179",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "42",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Min)",
        "Legal",
        "-0.079",
        "325.765",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "43",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Max)",
        "Legal",
        "-0.079",
        "325.765",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "44",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Min)",
        "Legal",
        "16.369",
        "494.179",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "45",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Max)",
        "Legal",
        "1.107",
        "358.131",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-152.981",
        "1.000",
        "-152.981"
      ],
      [
        "46",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Min)",
        "Legal",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "47",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Max)",
        "Legal",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "48",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Min)",
        "Legal",
        "0.069",
        "339.193",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-285.528",
        "1.000",
        "-285.528"
      ],
      [
        "49",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Max)",
        "Permit",
        "104.237",
        "488.880",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "4.181",
        "1.000",
        "4.181"
      ],
      [
        "50",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Min)",
        "Permit",
        "1.428",
        "434.292",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-161.005",
        "1.000",
        "-161.005"
      ],
      [
        "51",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Max)",
        "Permit",
        "1.964",
        "405.877",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-123.249",
        "1.000",
        "-123.249"
      ],
      [
        "52",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Min)",
        "Permit",
        "2.916",
        "484.996",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "53",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Max)",
        "Permit",
        "16.369",
        "494.179",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "54",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "-0.079",
        "325.765",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "55",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Max)",
        "Permit",
        "-0.079",
        "325.765",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "56",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Min)",
        "Permit",
        "16.369",
        "494.179",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "57",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "1.107",
        "358.131",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-152.981",
        "1.000",
        "-152.981"
      ],
      [
        "58",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "59",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Max)",
        "Permit",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "60",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Min)",
        "Permit",
        "0.069",
        "339.193",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-285.528",
        "1.000",
        "-285.528"
      ],
      [
        "61",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Max)",
        "Permit",
        "104.237",
        "488.880",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "4.181",
        "1.000",
        "4.181"
      ],
      [
        "62",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Min)",
        "Permit",
        "1.428",
        "434.292",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-161.005",
        "1.000",
        "-161.005"
      ],
      [
        "63",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Max)",
        "Permit",
        "1.964",
        "405.877",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-123.249",
        "1.000",
        "-123.249"
      ],
      [
        "64",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Min)",
        "Permit",
        "2.916",
        "484.996",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "65",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Max)",
        "Permit",
        "16.369",
        "494.179",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "66",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Min)",
        "Permit",
        "-0.079",
        "325.765",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "67",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Max)",
        "Permit",
        "-0.079",
        "325.765",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-318.166",
        "1.000",
        "-318.166"
      ],
      [
        "68",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Min)",
        "Permit",
        "16.369",
        "494.179",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "25.607",
        "1.000",
        "25.607"
      ],
      [
        "69",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Max)",
        "Permit",
        "1.107",
        "358.131",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-152.981",
        "1.000",
        "-152.981"
      ],
      [
        "70",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Min)",
        "Permit",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "71",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Max)",
        "Permit",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "72",
        "Girder",
        "2",
        "I[2]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Min)",
        "Permit",
        "0.069",
        "339.193",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-285.528",
        "1.000",
        "-285.528"
      ],
      [
        "73",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Max)",
        "Design Live",
        "1.917",
        "402.613",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-124.229",
        "1.000",
        "-124.229"
      ],
      [
        "74",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fx-Min)",
        "Design Live",
        "1.409",
        "344.253",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-128.609",
        "1.000",
        "-128.609"
      ],
      [
        "75",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Max)",
        "Design Live",
        "2.465",
        "362.745",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-94.206",
        "1.000",
        "-94.206"
      ],
      [
        "76",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fy-Min)",
        "Design Live",
        "2.346",
        "414.343",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "77",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Max)",
        "Design Live",
        "4.672",
        "392.252",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "78",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Fz-Min)",
        "Design Live",
        "0.170",
        "297.380",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "79",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Max)",
        "Design Live",
        "0.170",
        "297.380",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "80",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Mx-Min)",
        "Design Live",
        "4.672",
        "392.252",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "81",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(My-Max)",
        "Design Live",
        "3.289",
        "308.337",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "82",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(My-Min)",
        "Design Live",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "83",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Max)",
        "Design Live",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "84",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MAX)_A.V(Mz-Min)",
        "Design Live",
        "3.289",
        "308.337",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "85",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Max)",
        "Design Live",
        "1.917",
        "402.613",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-124.229",
        "1.000",
        "-124.229"
      ],
      [
        "86",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fx-Min)",
        "Design Live",
        "1.409",
        "344.253",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-128.609",
        "1.000",
        "-128.609"
      ],
      [
        "87",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Max)",
        "Design Live",
        "2.465",
        "362.745",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-94.206",
        "1.000",
        "-94.206"
      ],
      [
        "88",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fy-Min)",
        "Design Live",
        "2.346",
        "414.343",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "89",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Max)",
        "Design Live",
        "4.672",
        "392.252",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "90",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Fz-Min)",
        "Design Live",
        "0.170",
        "297.380",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "91",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Max)",
        "Design Live",
        "0.170",
        "297.380",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "92",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Mx-Min)",
        "Design Live",
        "4.672",
        "392.252",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "93",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(My-Max)",
        "Design Live",
        "3.289",
        "308.337",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "94",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(My-Min)",
        "Design Live",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "95",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Max)",
        "Design Live",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "96",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_DC(MIN)_A.V(Mz-Min)",
        "Design Live",
        "3.289",
        "308.337",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "97",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Max)",
        "Legal",
        "1.917",
        "402.613",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-124.229",
        "1.000",
        "-124.229"
      ],
      [
        "98",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fx-Min)",
        "Legal",
        "1.409",
        "344.253",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-128.609",
        "1.000",
        "-128.609"
      ],
      [
        "99",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Max)",
        "Legal",
        "2.465",
        "362.745",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-94.206",
        "1.000",
        "-94.206"
      ],
      [
        "100",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fy-Min)",
        "Legal",
        "2.346",
        "414.343",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "101",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Max)",
        "Legal",
        "4.672",
        "392.252",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "102",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Fz-Min)",
        "Legal",
        "0.170",
        "297.380",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "103",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Max)",
        "Legal",
        "0.170",
        "297.380",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "104",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Mx-Min)",
        "Legal",
        "4.672",
        "392.252",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "105",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Max)",
        "Legal",
        "3.289",
        "308.337",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "106",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(My-Min)",
        "Legal",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "107",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Max)",
        "Legal",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "108",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MAX)_A.V(Mz-Min)",
        "Legal",
        "3.289",
        "308.337",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "109",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Max)",
        "Legal",
        "1.917",
        "402.613",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-124.229",
        "1.000",
        "-124.229"
      ],
      [
        "110",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fx-Min)",
        "Legal",
        "1.409",
        "344.253",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-128.609",
        "1.000",
        "-128.609"
      ],
      [
        "111",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Max)",
        "Legal",
        "2.465",
        "362.745",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-94.206",
        "1.000",
        "-94.206"
      ],
      [
        "112",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fy-Min)",
        "Legal",
        "2.346",
        "414.343",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "113",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Max)",
        "Legal",
        "4.672",
        "392.252",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "114",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Fz-Min)",
        "Legal",
        "0.170",
        "297.380",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "115",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Max)",
        "Legal",
        "0.170",
        "297.380",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "116",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Mx-Min)",
        "Legal",
        "4.672",
        "392.252",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "117",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Max)",
        "Legal",
        "3.289",
        "308.337",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "118",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(My-Min)",
        "Legal",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "119",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Max)",
        "Legal",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "120",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_L_DC(MIN)_A.V(Mz-Min)",
        "Legal",
        "3.289",
        "308.337",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "121",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Max)",
        "Permit",
        "1.917",
        "402.613",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-124.229",
        "1.000",
        "-124.229"
      ],
      [
        "122",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fx-Min)",
        "Permit",
        "1.409",
        "344.253",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-128.609",
        "1.000",
        "-128.609"
      ],
      [
        "123",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Max)",
        "Permit",
        "2.465",
        "362.745",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-94.206",
        "1.000",
        "-94.206"
      ],
      [
        "124",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fy-Min)",
        "Permit",
        "2.346",
        "414.343",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "125",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Max)",
        "Permit",
        "4.672",
        "392.252",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "126",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Fz-Min)",
        "Permit",
        "0.170",
        "297.380",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "127",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Max)",
        "Permit",
        "0.170",
        "297.380",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "128",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Mx-Min)",
        "Permit",
        "4.672",
        "392.252",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "129",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Max)",
        "Permit",
        "3.289",
        "308.337",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "130",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(My-Min)",
        "Permit",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "131",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Max)",
        "Permit",
        "236.621",
        "657.551",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "132",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MAX)_A.V(Mz-Min)",
        "Permit",
        "3.289",
        "308.337",
        "1.250",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "133",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Max)",
        "Permit",
        "1.917",
        "402.613",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-124.229",
        "1.000",
        "-124.229"
      ],
      [
        "134",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fx-Min)",
        "Permit",
        "1.409",
        "344.253",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-128.609",
        "1.000",
        "-128.609"
      ],
      [
        "135",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Max)",
        "Permit",
        "2.465",
        "362.745",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-94.206",
        "1.000",
        "-94.206"
      ],
      [
        "136",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fy-Min)",
        "Permit",
        "2.346",
        "414.343",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-111.454",
        "1.000",
        "-111.454"
      ],
      [
        "137",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Max)",
        "Permit",
        "4.672",
        "392.252",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "138",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Fz-Min)",
        "Permit",
        "0.170",
        "297.380",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "139",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Max)",
        "Permit",
        "0.170",
        "297.380",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-228.685",
        "1.000",
        "-228.685"
      ],
      [
        "140",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Mx-Min)",
        "Permit",
        "4.672",
        "392.252",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "62.241",
        "1.000",
        "62.241"
      ],
      [
        "141",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Max)",
        "Permit",
        "3.289",
        "308.337",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
      ],
      [
        "142",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(My-Min)",
        "Permit",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "143",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Max)",
        "Permit",
        "236.621",
        "657.551",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-2.491",
        "1.000",
        "-2.491"
      ],
      [
        "144",
        "Girder",
        "2",
        "J[3]",
        "-",
        "STR_P_DC(MIN)_A.V(Mz-Min)",
        "Permit",
        "3.289",
        "308.337",
        "0.900",
        "0.000",
        "1.500",
        "0.000",
        "1.000",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "0.000",
        "1.250",
        "0.000",
        "1.000",
        "-64.700",
        "1.000",
        "-64.700"
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_NAME": "Shear Strength Rating Detail",
    "TABLE_TYPE": "PSC_RATING_SHEAR_DETAIL",
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "PARTS": [
      "Part I",
      "Part J"
    ],
    "RATING_CASE": [
      "ser",
      "STR",
      "SER_L",
      "SER_P",
      "STR_L",
      "STR_P"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M",
      "HEAT": "KCAL",
      "TEMP": "C"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Index",
      "Group",
      "Elem.",
      "Part",
      "RelativeLocation",
      "RatingCase",
      "RatingLevel",
      "RatingFactor",
      "Vn",
      "DC/Factor",
      "DC/Force",
      "DW/Factor",
      "DW/Force",
      "Temperature/Factor",
      "Temperature/Force",
      "T.Gradient/Factor",
      "T.Gradient/Force",
      "Permanent/Factor",
      "Permanent/Force",
      "Secondary/Factor",
      "Secondary/Force",
      "UserDefined/Factor",
      "UserDefined/Force",
      "Pri.LL/Factor",
      "Pri.LL/Force",
      "AdjLL/Factor",
      "AdjLL/Force"
    ]
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 28. `REPORT` — Rating Result Report

> **기능** 내하력 평가 결과를 보고서로 내보냅니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/REPORT
```

### Active Methods

`POST`

### Specifications

**원문** [영문 64738374621849](https://support.midasuser.com/hc/en-us/articles/64738374621849)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Creates the AASHTO-LRFR19 PSC rating Excel report. All fields are optional ({} is valid). Prerequisites: rating code AASHTO-LRFR19, rating results, and at least one output position in Position for Rating Output (/RATING/PSC/AASHTO-LRFR19/PFRO or PFRO-VBEAM); otherwise SUCCESS is false with a MESSAGE. | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Export Path | `"EXPORT_PATH"` | string |  | Optional |
| 2 | [General] Output Name | `"OUTPUT_NAME"` | string |  | Optional |
| 3 | [General] Save Image | `"SAVE_IMAGE_OPTION"` | boolean | false | Optional |

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
      "description": "Creates the AASHTO-LRFR19 PSC rating Excel report. All fields are optional ({} is valid). Prerequisites: rating code AASHTO-LRFR19, rating results, and at least one output position in Position for Rating Output (/RATING/PSC/AASHTO-LRFR19/PFRO or PFRO-VBEAM); otherwise SUCCESS is false with a MESSAGE.",
      "required": [],
      "additionalProperties": false,
      "properties": {
        "EXPORT_PATH": {
          "type": "string",
          "description": "Excel report export folder path. If empty, the folder of the model file is used. A trailing backslash is added when missing.",
          "default": ""
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "Excel report output file name. '.xlsx' is appended when missing. If empty, the model file name is used.",
          "default": ""
        },
        "SAVE_IMAGE_OPTION": {
          "type": "boolean",
          "description": "Whether to save images used in the Excel report.",
          "default": false
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
    "OUTPUT_NAME": "PSC_Rating_Report_AASHTO-LRFR19",
    "SAVE_IMAGE_OPTION": false
  }
}
```

**Response**

```json
{
  "PSC_EXCEL_RESPONSE": {
    "SUCCESS": true,
    "FILE_PATH": "C:\\MIDAS\\Report\\PSC_Rating_Report_AASHTO-LRFR19.xlsx",
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/REPORT"

payload = json.loads(r'''
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PSC_Rating_Report_AASHTO-LRFR19",
    "SAVE_IMAGE_OPTION": false
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 29. `LENG-VBEAM` — Unbraced Length(L,Lb) - Virtual Beam

> **기능** 가상보의 비지지 길이 L과 Lb를 설정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/LENG-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738366579993](https://support.midasuser.com/hc/en-us/articles/64738366579993)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a virtual beam number (e.g., "1"). The virtual beam must exist in the model. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Unbraced Length Ly · Minimum: 0 | `"LY"` | number | 0 | Optional |
| 2 | [General] Unbraced Length Lz · Minimum: 0 | `"LZ"` | number | 0 | Optional |
| 3 | [General] Laterally Unbraced Length. Used only when bNOTUSE is false. · Minimum: 0 | `"LB"` | number | 0 | Optional |
| 4 | [General] Do not consider of laterally unbraced length | `"bNOTUSE"` | boolean | false | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a virtual beam number (e.g., \"1\"). The virtual beam must exist in the model.",
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
              "default": 0,
              "minimum": 0
            },
            "LZ": {
              "type": "number",
              "description": "Unbraced Length Lz",
              "default": 0,
              "minimum": 0
            },
            "LB": {
              "type": "number",
              "description": "Laterally Unbraced Length. Used only when bNOTUSE is false.",
              "default": 0,
              "minimum": 0
            },
            "bNOTUSE": {
              "type": "boolean",
              "description": "Do not consider of laterally unbraced length",
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

- `LENG`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "2": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "3": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "4": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "5": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "6": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    }
  }
}
```

**Response**

```json
{
  "LENG": {
    "1": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "2": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "3": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "4": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "5": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "6": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/LENG-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "2": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "3": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "4": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "5": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    },
    "6": {
      "LY": 5.0,
      "LZ": 5.0,
      "LB": 10.0,
      "bNOTUSE": false
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 30. `SPLT-VBEAM` — Span Length - Virtual Beam

> **기능** 가상보의 지간 길이를 설정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/SPLT-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738366802329](https://support.midasuser.com/hc/en-us/articles/64738366802329)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a virtual beam number (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Span Length · Minimum: 0 | `"SPAN_LENGTH"` | number | 0 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a virtual beam number (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "SPAN_LENGTH": {
              "type": "number",
              "description": "Span Length",
              "default": 0,
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

- `SPLT`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "SPAN_LENGTH": 30.0
    },
    "2": {
      "SPAN_LENGTH": 30.0
    },
    "3": {
      "SPAN_LENGTH": 30.0
    },
    "4": {
      "SPAN_LENGTH": 30.0
    },
    "5": {
      "SPAN_LENGTH": 30.0
    },
    "6": {
      "SPAN_LENGTH": 30.0
    }
  }
}
```

**Response**

```json
{
  "SPLT": {
    "1": {
      "SPAN_LENGTH": 30.0
    },
    "2": {
      "SPAN_LENGTH": 30.0
    },
    "3": {
      "SPAN_LENGTH": 30.0
    },
    "4": {
      "SPAN_LENGTH": 30.0
    },
    "5": {
      "SPAN_LENGTH": 30.0
    },
    "6": {
      "SPAN_LENGTH": 30.0
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/SPLT-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "SPAN_LENGTH": 30.0
    },
    "2": {
      "SPAN_LENGTH": 30.0
    },
    "3": {
      "SPAN_LENGTH": 30.0
    },
    "4": {
      "SPAN_LENGTH": 30.0
    },
    "5": {
      "SPAN_LENGTH": 30.0
    },
    "6": {
      "SPAN_LENGTH": 30.0
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 31. `RPSC-VBEAM` — Reinforcement Information - Virtual Beam

> **기능** 가상보 평가에 사용할 철근 보강 정보를 입력합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/RPSC-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738375226521](https://support.midasuser.com/hc/en-us/articles/64738375226521)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a virtual section ID (e.g., "1"). | `"Assign"` | object | - | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a virtual section ID (e.g., \"1\").",
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
    "1": {
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
    },
    "2": {
      "OPT_MBAR_J": true,
      "OPT_SBAR_J": true,
      "OPT_CRACKED": false,
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
    },
    "2": {
      "OPT_MBAR_J": true,
      "OPT_SBAR_J": true,
      "OPT_CRACKED": false,
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/RPSC-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
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
    },
    "2": {
      "OPT_MBAR_J": true,
      "OPT_SBAR_J": true,
      "OPT_CRACKED": false,
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

## 32. `DATR-VBEAM` — Diagnostic Test Result - Virtual Beam

> **기능** 가상보 평가에 사용할 진단 시험 결과를 입력합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/DATR-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 64738390613657](https://support.midasuser.com/hc/en-us/articles/64738390613657)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a virtual beam ID (e.g., "1"). The virtual beam must exist in the model. | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Position Type · I: 0 · J: 1 · I & J: 2 | `"POSITION"` | integer | - | **Required** |
| 2 | [General] Load Test Measurement Type · Auto Calculation: 0 · User Input: 1 | `"LTM_TYPE"` | integer | - | **Required** |
| 3 | [General] Strain(I) | `"STRAIN_I"` | number | 1e-05 | Optional |
| 4 | [General] Strain(J) | `"STRAIN_J"` | number | 1e-05 | Optional |
| 5 | [General] Kb | `"KB"` | number | 1 | Optional |
| 6 | [General] K | `"K"` | number | 1 | Optional |
| 3 | [When LTM_TYPE = "Auto Calculation", POSITION in ["I", "I & J"]] Strain(I) · Minimum: 0 | `"STRAIN_I"` | number | 1e-05 | Optional |
| 4 | [When LTM_TYPE = "Auto Calculation", POSITION in ["J", "I & J"]] Strain(J) · Minimum: 0 | `"STRAIN_J"` | number | 1e-05 | Optional |
| 5 | [When LTM_TYPE = "Auto Calculation"] Kb · Minimum: 0 | `"KB"` | number | 1 | Optional |
| 6 | [When LTM_TYPE = "User Input"] K · Minimum: 0 | `"K"` | number | 1 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a virtual beam ID (e.g., \"1\"). The virtual beam must exist in the model.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Load Test Measurements",
          "type": "object",
          "required": [
            "POSITION",
            "LTM_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "POSITION": {
              "type": "integer",
              "description": "Position Type",
              "enum": [
                0,
                1,
                2
              ]
            },
            "LTM_TYPE": {
              "type": "integer",
              "description": "Load Test Measurement Type",
              "enum": [
                0,
                1
              ]
            },
            "STRAIN_I": {
              "type": "number",
              "description": "Strain at I-End. Required when LTM_TYPE is Auto Calculation(0) and POSITION is I(0) or I & J(2).",
              "default": 1e-05
            },
            "STRAIN_J": {
              "type": "number",
              "description": "Strain at J-End. Required when LTM_TYPE is Auto Calculation(0) and POSITION is J(1) or I & J(2).",
              "default": 1e-05
            },
            "KB": {
              "type": "number",
              "description": "Load Test Measurement Benefit Factor. Required when LTM_TYPE is Auto Calculation(0).",
              "default": 1
            },
            "K": {
              "type": "number",
              "description": "Adjustment Factor. Required when LTM_TYPE is User Input(1).",
              "default": 1
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

- `DATR`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "POSITION": 0,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "KB": 0.8
    },
    "2": {
      "POSITION": 1,
      "LTM_TYPE": 0,
      "STRAIN_J": 0.00011,
      "KB": 0.8
    },
    "3": {
      "POSITION": 2,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "STRAIN_J": 0.0001,
      "KB": 0.5
    },
    "4": {
      "POSITION": 2,
      "LTM_TYPE": 1,
      "K": 1.1
    }
  }
}
```

**Response**

```json
{
  "DATR": {
    "1": {
      "POSITION": 0,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "KB": 0.8
    },
    "2": {
      "POSITION": 1,
      "LTM_TYPE": 0,
      "STRAIN_J": 0.00011,
      "KB": 0.8
    },
    "3": {
      "POSITION": 2,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "STRAIN_J": 0.0001,
      "KB": 0.5
    },
    "4": {
      "POSITION": 2,
      "LTM_TYPE": 1,
      "K": 1.1
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/DATR-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "POSITION": 0,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "KB": 0.8
    },
    "2": {
      "POSITION": 1,
      "LTM_TYPE": 0,
      "STRAIN_J": 0.00011,
      "KB": 0.8
    },
    "3": {
      "POSITION": 2,
      "LTM_TYPE": 0,
      "STRAIN_I": 0.00012,
      "STRAIN_J": 0.0001,
      "KB": 0.5
    },
    "4": {
      "POSITION": 2,
      "LTM_TYPE": 1,
      "K": 1.1
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 33. `PFRO-VBEAM` — Position for Rating Output - Virtual Beam

> **기능** 가상보 평가 결과를 출력할 위치를 지정합니다.

### Input URI

```
{base url}/RATING/PSC/AASHTO-LRFR19/PFRO-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [영문 58381704142105](https://support.midasuser.com/hc/en-us/articles/58381704142105)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Position Type · I: 0 · J: 1 · I & J: 2 | `"PART"` | integer | 0 | **Required** |

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
            "PART"
          ],
          "additionalProperties": false,
          "properties": {
            "PART": {
              "type": "integer",
              "description": "Part Type",
              "default": 0,
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

- `PFRO`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "PART": 0
    },
    "2": {
      "PART": 1
    },
    "3": {
      "PART": 2
    }
  }
}
```

**Response**

```json
{
  "PFRO": {
    "1": {
      "PART": 0
    },
    "2": {
      "PART": 1
    },
    "3": {
      "PART": 2
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
URI = f"{BASE_URL}/RATING/PSC/AASHTO-LRFR19/PFRO-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "PART": 0
    },
    "2": {
      "PART": 1
    },
    "3": {
      "PART": 2
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```
