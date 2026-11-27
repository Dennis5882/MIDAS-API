# 32. Design Code – PSC KDS 24 14 21:2021 (교량 프리스트레스트 콘크리트 설계)

> **예제 Base URL (MIDAS Civil NX)** `https://moa-engineers.midasit.com:443/civil`  
> **인증 헤더** `MAPI-Key: <발급된 키>`  
> **공식 하위 목차** [KDS 24 14 21:2021 PSC 설계](https://support.midasuser.com/hc/ko/articles/64738439500697)

교량 PSC 부재의 설계 기준과 재료, 설계 실행, 결과 표와 도형을 다룹니다.
고유 URI **16개**와 본문 **33절**을 다룹니다.
공통 URI 접두사는 `{base url}/DESIGN/PSC/KDS-24-14-21-2021/<CODE>`입니다.
기준 선택에는 `{base url}/DESIGN/PSC/DSPSC`를 사용합니다.
공용 `TABLE` URI의 18개 결과 절은 `TABLE_TYPE`으로 구분합니다.

---

## Endpoint 목록 (33개 절)

| No. | Endpoint | 기능 | Active Methods |
| --- | --- | --- | --- |
| 0 | [`DSPSC`](#0-dspsc--design-code-kds-24-14-21--2021) | PSC 설계 기준을 KDS 24 14 21:2021로 설정하거나 조회합니다. | GET · PUT · DELETE |
| 1 | [`DPSC`](#1-dpsc--design-code-option) | PSC 설계 기준과 긴장재, 균열 검토, 휨·전단 설계 옵션을 설정합니다. | GET · PUT · DELETE |
| 2 | [`PESC`](#2-pesc--exposure-class) | 부재의 노출등급을 설정합니다. | POST · GET · PUT · DELETE |
| 3 | [`DIDP`](#3-didp--design-position) | PSC 설계를 수행할 위치를 지정합니다. | POST · GET · PUT · DELETE |
| 4 | [`MATD`](#4-matd--modify-material) | PSC 설계용 거더·슬래브의 콘크리트 및 철근 재료를 수정합니다. | GET · PUT · DELETE |
| 5 | [`DIOP`](#5-diop--output-position) | PSC 설계 결과의 출력 위치를 지정합니다. | POST · GET · PUT · DELETE |
| 6 | [`SLCT`](#6-slct--serviceability-load-combination-type) | PSC 설계의 사용성 하중조합 유형을 설정합니다. | GET · PUT · DELETE |
| 7 | [`PSCN`](#7-pscn--shear-connector) | 전단연결재 정보를 설정합니다. | POST · GET · PUT · DELETE |
| 8 | [`PSC-ANAL`](#8-psc-anal--perform-design) | PSC 설계를 수행합니다. | POST |
| 9 | [`TABLE` · `PSC_SHEAR_TORSION`](#9-table--psc_shear_torsion--check-combined-shear-and-torsion-strength) | 전단과 비틀림의 조합 강도 검토 결과를 조회합니다. | POST |
| 10 | [`TABLE` · `PSC_CRACK_WIDTH`](#10-table--psc_crack_width--check-crack-width-at-service-loads) | 사용하중에 대한 균열폭 검토 결과를 조회합니다. | POST |
| 11 | [`TABLE` · `PSC_FLEXURE`](#11-table--psc_flexure--check-flexure-strength) | 휨강도 검토 결과를 조회합니다. | POST |
| 12 | [`TABLE` · `PSC_SHEAR`](#12-table--psc_shear--check-shear-strength) | 전단강도 검토 결과를 조회합니다. | POST |
| 13 | [`TABLE` · `PSC_STRESS_CS`](#13-table--psc_stress_cs--check-stress-for-cross-section-at-a-construction-stage) | 시공단계별 단면의 응력 검토 결과를 조회합니다. | POST |
| 14 | [`TABLE` · `PSC_STRESS_SERVICE`](#14-table--psc_stress_service--check-stress-for-cross-section-at-service-loads) | 사용하중에 대한 단면 응력 검토 결과를 조회합니다. | POST |
| 15 | [`TABLE` · `PSC_STRESS_TENDON`](#15-table--psc_stress_tendon--check-tensile-stress-for-prestressing-tendons) | 프리스트레싱 긴장재의 인장응력 검토 결과를 조회합니다. | POST |
| 16 | [`TABLE` · `PSC_DGN_FORCE`](#16-table--psc_dgn_force--design-forces) | PSC 설계에 사용한 부재력을 조회합니다. | POST |
| 17 | [`REPORT`](#17-report--excel-report) | PSC 설계 결과를 Excel 보고서로 내보냅니다. | POST |
| 18 | [`TABLE` · `PSC_PRINCIPAL_CS`](#18-table--psc_principal_cs--principal-stress-at-a-construction-stage) | 시공단계별 단면의 주응력 결과를 조회합니다. | POST |
| 19 | [`TABLE` · `PSC_PRINCIPAL_SVC`](#19-table--psc_principal_svc--principal-stress-at-service-loads) | 사용하중에 대한 주응력 결과를 조회합니다. | POST |
| 20 | [`DRESULT`](#20-dresult--psc-result-diagram) | PSC 설계 결과 도형을 조회합니다. | POST |
| 21 | [`DIDP-VBEAM`](#21-didp-vbeam--design-position---virtual-beam) | 가상보의 PSC 설계 위치를 지정합니다. | POST · GET · PUT · DELETE |
| 22 | [`PESC-VBEAM`](#22-pesc-vbeam--exposure-class---virtual-beam) | 가상보의 노출등급을 설정합니다. | POST · GET · PUT · DELETE |
| 23 | [`DIOP-VBEAM`](#23-diop-vbeam--output-position---virtual-beam) | 가상보의 PSC 설계 결과 출력 위치를 지정합니다. | POST · GET · PUT · DELETE |
| 24 | [`PSCN-VBEAM`](#24-pscn-vbeam--shear-connector---virtual-beam) | 가상보의 전단연결재 정보를 설정합니다. | POST · GET · PUT · DELETE |
| 25 | [`TABLE` · `PSC_SHEAR_TORSION_VBEAM`](#25-table--psc_shear_torsion_vbeam--check-combined-shear-and-torsion-strength---virtual-beam) | 가상보의 전단과 비틀림의 조합 강도 검토 결과를 조회합니다. | POST |
| 26 | [`TABLE` · `PSC_CRACK_WIDTH_VBEAM`](#26-table--psc_crack_width_vbeam--check-crack-width-at-service-loads---virtual-beam) | 가상보의 사용하중에 대한 균열폭 검토 결과를 조회합니다. | POST |
| 27 | [`TABLE` · `PSC_FLEXURE_VBEAM`](#27-table--psc_flexure_vbeam--check-flexure-strength---virtual-beam) | 가상보의 휨강도 검토 결과를 조회합니다. | POST |
| 28 | [`TABLE` · `PSC_SHEAR_VBEAM`](#28-table--psc_shear_vbeam--check-shear-strength---virtual-beam) | 가상보의 전단강도 검토 결과를 조회합니다. | POST |
| 29 | [`TABLE` · `PSC_STRESS_SERVICE_VBEAM`](#29-table--psc_stress_service_vbeam--check-stress-for-cross-section-at-service-loads---virtual-beam) | 가상보의 사용하중에 대한 단면 응력 검토 결과를 조회합니다. | POST |
| 30 | [`TABLE` · `PSC_STRESS_TENDON_VBEAM`](#30-table--psc_stress_tendon_vbeam--check-tensile-stress-for-prestressing-tendons---virtual-beam) | 가상보의 프리스트레싱 긴장재의 인장응력 검토 결과를 조회합니다. | POST |
| 31 | [`TABLE` · `PSC_PRINCIPAL_CS_VBEAM`](#31-table--psc_principal_cs_vbeam--principal-stress-at-a-construction-stage---virtual-beam) | 가상보의 시공단계별 단면의 주응력 결과를 조회합니다. | POST |
| 32 | [`TABLE` · `PSC_PRINCIPAL_SVC_VBEAM`](#32-table--psc_principal_svc_vbeam--principal-stress-at-service-loads---virtual-beam) | 가상보의 사용하중에 대한 주응력 결과를 조회합니다. | POST |

---

## 0. `DSPSC` — Design Code (KDS 24 14 21 : 2021)

> **기능** PSC 설계 기준을 KDS 24 14 21:2021로 설정하거나 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/DSPSC
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738155393433](https://support.midasuser.com/hc/ko/articles/64738155393433)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an ID string (e.g., "1"). | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] PSC Design Code · KDS 24 14 21 : 2021: "KDS 24 14 21 : 2021" | `"DGNCODE"` | string | - | **Required** |

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
              "description": "PSC Design Code",
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

- `DSPSC`

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
  "DSPSC": {
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
URI = f"{BASE_URL}/DESIGN/PSC/DSPSC"

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

## 1. `DPSC` — Design Code Option

> **기능** PSC 설계 기준과 긴장재, 균열 검토, 휨·전단 설계 옵션을 설정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/DPSC
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738155455769](https://support.midasuser.com/hc/ko/articles/64738155455769)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Single settings record: the only accepted key is "1". | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Design Code · KDS 24 14 21 : 2021 | `"DGNCODE"` | string | KDS 24 14 21 : 2021 | **Required** |
| 2 | [General] Design Calculation Input Variables | `"DESIGN_INPUT"` | object | - | Optional |
| 2.1 | └ [General] Shear Strength | `"SHEAR_STRENGTH"` | object | - | Optional |
| 2.1.1 | 　　└ [General] Strut angle for shear resistance (Degree) · Range: 21.8~45 | `"STRUT_ANGLE"` | number | 45 | Optional |
| 2.2 | └ [General] Type of Prestressing Steel (Bond Strength Ratio Applied) · Round Bar and Wire: "ROUND BAR AND WIRE" · Strand: "STRAND" · Deformed Wire: "DEFORMED WIRE" · Deformed Bar: "DEFORMED BAR" | `"TENDON_TYPE"` | string | ROUND BAR AND WIRE | Optional |
| 2.3 | └ [General] Cement Classification · Portland cement, Class 1, moist cure (0.35): "CLASS 1 MOIST CURE" · Portland cement, Class 1, steme cure (0.15): "CLASS 1 STEAM CURE" · Portland cement, Class 3, moist cure (0.25): "CLASS 3 MOIST CURE" · Portland cement, Class 3, steme cure (0.12): "CLASS 3 STEAM CURE" · Portland cement, Class 2 (0.40): "CLASS 2" | `"CEMENT_CLASSIFICATION"` | string | CLASS 1 MOIST CURE | Optional |
| 2.4 | └ [General] User-defined Input Data | `"USER_DEFINED_INPUT"` | boolean | false | Optional |
| 2.5 | └ [General] Concrete Stress Calculation · Rectangular Stress Block: "RECTANGULAR STRESS BLOCK" · Stress-Strain (Parabolic-Plateau): "PARABOLIC-PLATEAU" | `"CONCRETE_STRESS_CALCULATION"` | string | RECTANGULAR STRESS BLOCK | Optional |
| 2.6 | └ [General] Beta (Interface Shear Check) · 1.0: "1" · Exact Design: "EXACT DESIGN" | `"INTERFACE_SHEAR_BETA"` | string | 1 | Optional |
| 3 | [General] Modify Design Parameters | `"MODIFY_DESIGN_PARAMETERS"` ¹⁾ | object | - | Optional |
| 4 | [General] Output Input Variables | `"OUTPUT"` | object | - | Optional |
| 4.1 | └ [General] Ultimate Limit State | `"ULS"` | object | - | Optional |
| 4.1.1 | 　　└ [General] Flexural Strength Check | `"FLEXURE"` | boolean | false | Optional |
| 4.1.2 | 　　└ [General] Shear Strength Check | `"SHEAR"` | boolean | false | Optional |
| 4.1.3 | 　　└ [General] Torsional Strength Check | `"TORSION"` | boolean | false | Optional |
| 4.2 | └ [General] Serviceability Limit State | `"SLS"` | object | - | Optional |
| 4.2.1 | 　　└ [General] Section Stress at Construction Stage | `"STRESS_CS"` | boolean | false | Optional |
| 4.2.2 | 　　└ [General] Section Stress under Service Load | `"STRESS_SERVICE"` | boolean | false | Optional |
| 4.2.3 | 　　└ [General] Principal Stress at Section during Construction Stage | `"PRINCIPAL_STRESS_CS"` | boolean | false | Optional |
| 4.2.4 | 　　└ [General] Principal Stress at Section under Service Load | `"PRINCIPAL_STRESS_SERVICE"` | boolean | false | Optional |
| 4.2.5 | 　　└ [General] Maximum Stress in Prestressing Steel | `"TENDON_MAX_STRESS"` | boolean | false | Optional |
| 4.2.6 | 　　└ [General] Crack Check | `"CRACK"` | boolean | false | Optional |

**Modify Design Parameters ¹⁾**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Update by Code | `"UPDATE_BY_CODE"` | boolean | false | Optional |
| 2 | Material Partial Factors | `"MATERIAL_RESISTANCE_FACTORS"` | object | - | Optional |
| 2.1 | └ Ultimate Load Combination | `"ULTIMATE"` | object | - | Optional |
| 2.1.1 | 　　└ Concrete · Minimum: 0 | `"CONCRETE"` | number | 0.65 | Optional |
| 2.1.2 | 　　└ Reinforcement · Minimum: 0 | `"REINFORCEMENT"` | number | 0.9 | Optional |
| 2.1.3 | 　　└ Prestressing Steel · Minimum: 0 | `"TENDON"` | number | 0.9 | Optional |
| 2.2 | └ Service Load Combination | `"SERVICE"` | object | - | Optional |
| 2.2.1 | 　　└ Concrete · Minimum: 0 | `"CONCRETE"` | number | 1 | Optional |
| 2.2.2 | 　　└ Reinforcement · Minimum: 0 | `"REINFORCEMENT"` | number | 1 | Optional |
| 2.2.3 | 　　└ Prestressing Steel · Minimum: 0 | `"TENDON"` | number | 1 | Optional |
| 3 | Stress Limits | `"STRESS_LIMITS"` | object | - | Optional |
| 3.1 | └ Concrete | `"CONCRETE"` | object | - | Optional |
| 3.1.1 | 　　└ k1 · Minimum: 0 | `"K1"` | number | 0.6 | Optional |
| 3.1.2 | 　　└ k6 · Minimum: 0 | `"K6"` | number | 0.7 | Optional |
| 3.2 | └ Prestressing Steel | `"TENDON"` | object | - | Optional |
| 3.2.1 | 　　└ k1 · Minimum: 0 | `"K1"` | number | 0.8 | Optional |
| 3.2.2 | 　　└ k2 · Minimum: 0 | `"K2"` | number | 0.9 | Optional |
| 3.2.3 | 　　└ k5 · Minimum: 0 | `"K5"` | number | 0.65 | Optional |
| 3.2.4 | 　　└ k7 · Minimum: 0 | `"K7"` | number | 0.75 | Optional |
| 3.2.5 | 　　└ k8 · Minimum: 0 | `"K8"` | number | 0.85 | Optional |
| 4 | Reduction Factor for Principal Stress | `"PRINCIPAL_STRESS_REDUCTION"` | object | - | Optional |
| 4.1 | └ Construction Stage | `"CS"` | object | - | Optional |
| 4.1.1 | 　　└ Compression · Minimum: 0 | `"COMPRESSION"` | number | 1 | Optional |
| 4.1.2 | 　　└ Tension · Minimum: 0 | `"TENSION"` | number | 1 | Optional |
| 4.2 | └ Serviceability Limit State | `"SLS"` | object | - | Optional |
| 4.2.1 | 　　└ Compression · Minimum: 0 | `"COMPRESSION"` | number | 1 | Optional |
| 4.2.2 | 　　└ Tension · Minimum: 0 | `"TENSION"` | number | 1 | Optional |

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
          "title": "PSC Design Code",
          "type": "object",
          "description": "Design Code Option for KDS 24 14 21 : 2021. DGNCODE is required like the other Design Code Option schemas; the code is taken from the URL. PUT merges: other fields not sent keep their stored values.",
          "required": [
            "DGNCODE"
          ],
          "additionalProperties": false,
          "properties": {
            "DGNCODE": {
              "type": "string",
              "description": "PSC Design Code",
              "enum": [
                "KDS 24 14 21 : 2021"
              ],
              "default": "KDS 24 14 21 : 2021"
            },
            "DESIGN_INPUT": {
              "type": "object",
              "description": "Design calculation input variables (upper half of the PSC Design Code dialog).",
              "additionalProperties": false,
              "properties": {
                "SHEAR_STRENGTH": {
                  "type": "object",
                  "description": "Shear strength.",
                  "additionalProperties": false,
                  "properties": {
                    "STRUT_ANGLE": {
                      "type": "number",
                      "description": "Strut angle theta for shear and torsion resistance, in degrees (21.8 to 45).",
                      "minimum": 21.8,
                      "maximum": 45,
                      "default": 45
                    }
                  }
                },
                "TENDON_TYPE": {
                  "type": "string",
                  "description": "Type of prestressing steel. Sets the bond strength ratio used in the crack check.",
                  "default": "ROUND BAR AND WIRE",
                  "enum": [
                    "ROUND BAR AND WIRE",
                    "STRAND",
                    "DEFORMED WIRE",
                    "DEFORMED BAR"
                  ]
                },
                "CEMENT_CLASSIFICATION": {
                  "type": "string",
                  "description": "Cement type and curing. Sets the strength development coefficient s (0.35, 0.15, 0.25, 0.12, 0.40 in list order).",
                  "default": "CLASS 1 MOIST CURE",
                  "enum": [
                    "CLASS 1 MOIST CURE",
                    "CLASS 1 STEAM CURE",
                    "CLASS 3 MOIST CURE",
                    "CLASS 3 STEAM CURE",
                    "CLASS 2"
                  ]
                },
                "USER_DEFINED_INPUT": {
                  "type": "boolean",
                  "description": "Use the factors in MODIFY_DESIGN_PARAMETERS (enables the Modify design parameters button).",
                  "default": false
                },
                "CONCRETE_STRESS_CALCULATION": {
                  "type": "string",
                  "description": "Concrete stress distribution used for the flexural strength.",
                  "default": "RECTANGULAR STRESS BLOCK",
                  "enum": [
                    "RECTANGULAR STRESS BLOCK",
                    "PARABOLIC-PLATEAU"
                  ]
                },
                "INTERFACE_SHEAR_BETA": {
                  "type": "string",
                  "description": "Beta for the interface shear check of composite sections.",
                  "default": "1",
                  "enum": [
                    "1",
                    "EXACT DESIGN"
                  ]
                }
              }
            },
            "MODIFY_DESIGN_PARAMETERS": {
              "type": "object",
              "description": "Factors of the Modify Design Parameters window. Accepted only when DESIGN_INPUT.USER_DEFINED_INPUT is true (sent or stored). Factors not sent keep their stored values.",
              "additionalProperties": false,
              "properties": {
                "UPDATE_BY_CODE": {
                  "type": "boolean",
                  "description": "true resets every factor of this window to the code values, as the Update by Code button does. Not stored or returned.",
                  "default": false
                },
                "MATERIAL_RESISTANCE_FACTORS": {
                  "type": "object",
                  "description": "Material resistance factors.",
                  "additionalProperties": false,
                  "properties": {
                    "ULTIMATE": {
                      "type": "object",
                      "description": "Ultimate load combinations.",
                      "additionalProperties": false,
                      "properties": {
                        "CONCRETE": {
                          "type": "number",
                          "description": "Material resistance factor of concrete, phi_c. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 0.65
                        },
                        "REINFORCEMENT": {
                          "type": "number",
                          "description": "Material resistance factor of reinforcement, phi_s. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 0.9
                        },
                        "TENDON": {
                          "type": "number",
                          "description": "Material resistance factor of prestressing steel, phi_ps. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 0.9
                        }
                      }
                    },
                    "SERVICE": {
                      "type": "object",
                      "description": "Service load combinations.",
                      "additionalProperties": false,
                      "properties": {
                        "CONCRETE": {
                          "type": "number",
                          "description": "Material resistance factor of concrete, phi_c. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 1
                        },
                        "REINFORCEMENT": {
                          "type": "number",
                          "description": "Material resistance factor of reinforcement, phi_s. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 1
                        },
                        "TENDON": {
                          "type": "number",
                          "description": "Material resistance factor of prestressing steel, phi_ps. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 1
                        }
                      }
                    }
                  }
                },
                "STRESS_LIMITS": {
                  "type": "object",
                  "description": "Stress limit factors.",
                  "additionalProperties": false,
                  "properties": {
                    "CONCRETE": {
                      "type": "object",
                      "description": "Concrete stress limit factors.",
                      "additionalProperties": false,
                      "properties": {
                        "K1": {
                          "type": "number",
                          "description": "Concrete compression limit k1*fck and tension limit k1*fctm after losses, and k1*fck(t) at transfer for post-tensioned members. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 0.6
                        },
                        "K6": {
                          "type": "number",
                          "description": "Concrete compression limit k6*fck(t) at transfer for pre-tensioned members. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 0.7
                        }
                      }
                    },
                    "TENDON": {
                      "type": "object",
                      "description": "Prestressing steel stress limit factors.",
                      "additionalProperties": false,
                      "properties": {
                        "K1": {
                          "type": "number",
                          "description": "Tendon stress limit during jacking, min(k1*fpu, k2*fpy). Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 0.8
                        },
                        "K2": {
                          "type": "number",
                          "description": "Tendon stress limit during jacking, min(k1*fpu, k2*fpy). Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 0.9
                        },
                        "K5": {
                          "type": "number",
                          "description": "Tendon stress limit under service loads after all losses, k5*fpy. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 0.65
                        },
                        "K7": {
                          "type": "number",
                          "description": "Tendon stress limit immediately after transfer, min(k7*fpu, k8*fpy). Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 0.75
                        },
                        "K8": {
                          "type": "number",
                          "description": "Tendon stress limit immediately after transfer, min(k7*fpu, k8*fpy). Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 0.85
                        }
                      }
                    }
                  }
                },
                "PRINCIPAL_STRESS_REDUCTION": {
                  "type": "object",
                  "description": "Reduction factors for principal stress.",
                  "additionalProperties": false,
                  "properties": {
                    "CS": {
                      "type": "object",
                      "description": "Construction stage.",
                      "additionalProperties": false,
                      "properties": {
                        "COMPRESSION": {
                          "type": "number",
                          "description": "kc: principal compressive stress limit kc*fck(t) at construction stage. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 1
                        },
                        "TENSION": {
                          "type": "number",
                          "description": "kt: principal tensile stress limit kt*fctm(t) at construction stage. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 1
                        }
                      }
                    },
                    "SLS": {
                      "type": "object",
                      "description": "Serviceability limit state.",
                      "additionalProperties": false,
                      "properties": {
                        "COMPRESSION": {
                          "type": "number",
                          "description": "kc: principal compressive stress limit kc*fck under service loads. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 1
                        },
                        "TENSION": {
                          "type": "number",
                          "description": "kt: principal tensile stress limit kt*fctm under service loads. Must be greater than 0.",
                          "exclusiveMinimum": 0,
                          "default": 1
                        }
                      }
                    }
                  }
                }
              }
            },
            "OUTPUT": {
              "type": "object",
              "description": "Check items written to the design output. They do not change the design results.",
              "additionalProperties": false,
              "properties": {
                "ULS": {
                  "type": "object",
                  "description": "Ultimate limit state.",
                  "additionalProperties": false,
                  "properties": {
                    "FLEXURE": {
                      "type": "boolean",
                      "description": "Flexural strength check.",
                      "default": false
                    },
                    "SHEAR": {
                      "type": "boolean",
                      "description": "Shear strength check.",
                      "default": false
                    },
                    "TORSION": {
                      "type": "boolean",
                      "description": "Torsional strength check.",
                      "default": false
                    }
                  }
                },
                "SLS": {
                  "type": "object",
                  "description": "Serviceability limit state.",
                  "additionalProperties": false,
                  "properties": {
                    "STRESS_CS": {
                      "type": "boolean",
                      "description": "Section stress at construction stage.",
                      "default": false
                    },
                    "STRESS_SERVICE": {
                      "type": "boolean",
                      "description": "Section stress under service loads.",
                      "default": false
                    },
                    "PRINCIPAL_STRESS_CS": {
                      "type": "boolean",
                      "description": "Principal stress at construction stage.",
                      "default": false
                    },
                    "PRINCIPAL_STRESS_SERVICE": {
                      "type": "boolean",
                      "description": "Principal stress under service loads.",
                      "default": false
                    },
                    "TENDON_MAX_STRESS": {
                      "type": "boolean",
                      "description": "Maximum stress in prestressing steel.",
                      "default": false
                    },
                    "CRACK": {
                      "type": "boolean",
                      "description": "Crack check.",
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
      "DESIGN_INPUT": {
        "SHEAR_STRENGTH": {
          "STRUT_ANGLE": 40.0
        }
      },
      "DGNCODE": "KDS 24 14 21 : 2021"
    }
  }
}
```

**Response**

```json
{
  "DPSC": {
    "1": {
      "DGNCODE": "KDS 24 14 21 : 2021",
      "DESIGN_INPUT": {
        "SHEAR_STRENGTH": {
          "STRUT_ANGLE": 40
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/DPSC"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "DESIGN_INPUT": {
        "SHEAR_STRENGTH": {
          "STRUT_ANGLE": 40.0
        }
      },
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

## 2. `PESC` — Exposure Class

> **기능** 부재의 노출등급을 설정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/PESC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738184902809](https://support.midasuser.com/hc/ko/articles/64738184902809)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a beam element number (e.g., "12"). Element Type = Element of the panel. Virtual beams use /DESIGN/PSC/KDS-24-14-21-2021/PESC-VBEAM | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Both end parts(i & j) have the same Exposure Class | `"BOTH_ENDS"` | boolean | true | Optional |
| 2 | [General] I | `"I"` | object | - | Optional |
| 2.1 | └ [General] Top · EC1 · EC2 · EC3 · EC4 · ED1 · ED2 · ED3 · ES1 · ES2 · ES3 | `"TOP"` | string | EC1 | Optional |
| 2.2 | └ [General] Bottom · EC1 · EC2 · EC3 · EC4 · ED1 · ED2 · ED3 · ES1 · ES2 · ES3 | `"BOTTOM"` | string | EC1 | Optional |
| 3 | [General] J | `"J"` | object | - | Optional |
| 3.1 | └ [General] Top · EC1 · EC2 · EC3 · EC4 · ED1 · ED2 · ED3 · ES1 · ES2 · ES3 | `"TOP"` | string | EC1 | Optional |
| 3.2 | └ [General] Bottom · EC1 · EC2 · EC3 · EC4 · ED1 · ED2 · ED3 · ES1 · ES2 · ES3 | `"BOTTOM"` | string | EC1 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a beam element number (e.g., \"12\"). Element Type = Element of the panel. Virtual beams use /DESIGN/PSC/KDS-24-14-21-2021/PESC-VBEAM",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Exposure Class",
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "BOTH_ENDS": {
              "type": "boolean",
              "description": "Both end parts (i & j) have the same Exposure Class. true: the I-end classes are stored for the J end as well; J must then be omitted or equal to I (otherwise rejected). Omitted on PUT: the stored value is kept",
              "default": true
            },
            "I": {
              "type": "object",
              "description": "Exposure classes at the I end (tab I). Omitted members keep the stored values on PUT",
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "string",
                  "description": "Exposure class of the top face at the I end (KDS 24 14 21 : 2021 classes EC1-EC4, ED1-ED3, ES1-ES3)",
                  "enum": [
                    "EC1",
                    "EC2",
                    "EC3",
                    "EC4",
                    "ED1",
                    "ED2",
                    "ED3",
                    "ES1",
                    "ES2",
                    "ES3"
                  ],
                  "default": "EC1"
                },
                "BOTTOM": {
                  "type": "string",
                  "description": "Exposure class of the bottom face at the I end (KDS 24 14 21 : 2021 classes EC1-EC4, ED1-ED3, ES1-ES3)",
                  "enum": [
                    "EC1",
                    "EC2",
                    "EC3",
                    "EC4",
                    "ED1",
                    "ED2",
                    "ED3",
                    "ES1",
                    "ES2",
                    "ES3"
                  ],
                  "default": "EC1"
                }
              }
            },
            "J": {
              "type": "object",
              "description": "Exposure classes at the J end (tab J). Used when BOTH_ENDS is false; with BOTH_ENDS true it must be omitted or equal to I",
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "string",
                  "description": "Exposure class of the top face at the J end (KDS 24 14 21 : 2021 classes EC1-EC4, ED1-ED3, ES1-ES3)",
                  "enum": [
                    "EC1",
                    "EC2",
                    "EC3",
                    "EC4",
                    "ED1",
                    "ED2",
                    "ED3",
                    "ES1",
                    "ES2",
                    "ES3"
                  ],
                  "default": "EC1"
                },
                "BOTTOM": {
                  "type": "string",
                  "description": "Exposure class of the bottom face at the J end (KDS 24 14 21 : 2021 classes EC1-EC4, ED1-ED3, ES1-ES3)",
                  "enum": [
                    "EC1",
                    "EC2",
                    "EC3",
                    "EC4",
                    "ED1",
                    "ED2",
                    "ED3",
                    "ES1",
                    "ES2",
                    "ES3"
                  ],
                  "default": "EC1"
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

- `PESC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "I": {
        "TOP": "EC3",
        "BOTTOM": "EC2"
      }
    }
  }
}
```

**Response**

```json
{
  "PESC": {
    "1": {
      "I": {
        "TOP": "EC3",
        "BOTTOM": "EC2"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/PESC"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "I": {
        "TOP": "EC3",
        "BOTTOM": "EC2"
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

## 3. `DIDP` — Design Position

> **기능** PSC 설계를 수행할 위치를 지정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/DIDP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738168449433](https://support.midasuser.com/hc/ko/articles/64738168449433)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element ID string (e.g., "1"): a beam element with a PSC or composite section and a concrete design material. Virtual beams use /DESIGN/PSC/KDS-24-14-21-2021/DIDP-VBEAM | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Moment Resistance · None: 0 · I: 1 · J: 2 · I & J: 3 | `"MOMENT_TYPE"` | integer | 3 | **Required** |
| 2 | [General] Shear Resistance · None: 0 · I: 1 · J: 2 · I & J: 3 | `"SHEAR_TYPE"` | integer | 3 | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is an element ID string (e.g., \"1\"): a beam element with a PSC or composite section and a concrete design material. Virtual beams use /DESIGN/PSC/KDS-24-14-21-2021/DIDP-VBEAM",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Position for PSC Design",
          "type": "object",
          "required": [
            "MOMENT_TYPE",
            "SHEAR_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "MOMENT_TYPE": {
              "type": "integer",
              "description": "Ends checked for moment resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
              "default": 3,
              "enum": [
                0,
                1,
                2,
                3
              ]
            },
            "SHEAR_TYPE": {
              "type": "integer",
              "description": "Ends checked for shear resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
              "default": 3,
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
      "MOMENT_TYPE": 3,
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
      "MOMENT_TYPE": 3,
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/DIDP"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "MOMENT_TYPE": 3,
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

## 4. `MATD` — Modify Material

> **기능** PSC 설계용 거더·슬래브의 콘크리트 및 철근 재료를 수정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/MATD
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738160285721](https://support.midasuser.com/hc/ko/articles/64738160285721)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a concrete material ID string (e.g., "1"): an existing material whose design type is concrete. Writing deletes PSC design results | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Concrete Material Selection | `"GIRDER_MATL_PROP"` | object | - | **Required** |
| 1.1 | └ [General] Code · None · KSCE-LSD15(RC) · KS01-Civil(RC) · KS-Civil(RC) · KS19(RC) · KS01(RC) · KS(RC) | `"CODE"` | string | - | **Required** |
| 1.2 | └ [General] Grade | `"GRADE"` | string | - | Optional |
| 1.3 | └ [When CODE = "None"] Name | `"NAME"` | string | - | **Required** |
| 1.4 | └ [When CODE = "None"] Specified Compressive Strength (fc\|fck) · Minimum: 0 | `"COMP_STRENGTH"` | number | - | **Required** |
| 1.5 | └ [When CODE = "None"] Light Weight Concrete Factor (Lambda) | `"LIGHT_WEIGHT_FACTOR"` | boolean | false | Optional |
| 1.6 | └ [When LIGHT_WEIGHT_FACTOR = true] Lambda · Range: 0.75~1 | `"FACTOR_VALUE"` | number | 1 | **Required** |
| 1.2 | └ [When CODE = "KSCE-LSD15(RC)"] Grade · C15 · C18 · C21 · C24 · C27 · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 · C90 · C95 | `"GRADE"` | string | - | Optional |
| 1.2 | └ [When CODE in ["KS01-Civil(RC)", "KS19(RC)", "KS01(RC)"]] Grade · C15 · C18 · C21 · C24 · C27 · C30 · C35 · C40 · C45 · C49 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 · C90 · C95 | `"GRADE"` | string | - | Optional |
| 1.2 | └ [When CODE in ["KS-Civil(RC)", "KS(RC)"]] Grade · C150 · C180 · C210 · C240 · C270 · C300 · C350 · C400 · C450 · C500 · C550 · C600 · C650 · C700 | `"GRADE"` | string | - | Optional |
| 2 | [General] Rebar Selection | `"GIRDER_REBAR_PROP"` | object | - | **Required** |
| 2.1 | └ [General] Code · None · KSCE-LSD15(RC) · KS01-Civil(RC) · KS-Civil(RC) · KS19(RC) · KS01(RC) · KS(RC) | `"CODE"` | string | - | **Required** |
| 2.2 | └ [General] Grade of Main Rebar | `"GRADE_MAIN_REBAR"` | string | - | Optional |
| 2.3 | └ [When CODE = "None"] Name of Main Rebar | `"NAME_MAIN_REBAR"` | string | - | **Required** |
| 2.4 | └ [When CODE = "None"] Fy · Minimum: 0 | `"Fy"` | number | - | **Required** |
| 2.5 | └ [When CODE = "None"] Grade of Sub-Rebar | `"GRADE_SUB_REBAR"` | string | - | Optional |
| 2.6 | └ [When CODE = "None"] Name of Sub-Rebar | `"NAME_SUB_REBAR"` | string | - | **Required** |
| 2.7 | └ [When CODE = "None"] Fys · Minimum: 0 | `"Fys"` | number | - | **Required** |
| 2.2 | └ [When CODE in ["KSCE-LSD15(RC)", "KS01-Civil(RC)", "KS01(RC)"]] Grade of Main Rebar · SD240 · SD300 · SD350 · SD400 · SD500 · SD600 | `"GRADE_MAIN_REBAR"` | string | - | Optional |
| 2.2 | └ [When CODE in ["KS-Civil(RC)", "KS(RC)"]] Grade of Main Rebar · SD24 · SD30 · SD35 · SD40 · SD50 | `"GRADE_MAIN_REBAR"` | string | - | Optional |
| 2.2 | └ [When CODE = "KS19(RC)"] Grade of Main Rebar · SD300 · SD400 · SD500 · SD600 · SD700 · SD400S · SD500S · SD600S | `"GRADE_MAIN_REBAR"` | string | - | Optional |
| 2.5 | └ [When CODE in ["KSCE-LSD15(RC)", "KS01-Civil(RC)", "KS01(RC)"]] Grade of Sub-Rebar · SD240 · SD300 · SD350 · SD400 · SD500 · SD600 | `"GRADE_SUB_REBAR"` | string | - | Optional |
| 2.5 | └ [When CODE in ["KS-Civil(RC)", "KS(RC)"]] Grade of Sub-Rebar · SD24 · SD30 · SD35 · SD40 · SD50 | `"GRADE_SUB_REBAR"` | string | - | Optional |
| 2.5 | └ [When CODE = "KS19(RC)"] Grade of Sub-Rebar · SD300 · SD400 · SD500 · SD600 · SD700 · SD400S · SD500S · SD600S | `"GRADE_SUB_REBAR"` | string | - | Optional |
| 3 | [General] Slab | `"SLAB_PROP"` | boolean | false | Optional |
| 4 | [When SLAB_PROP = true] Concrete Material Selection | `"SLAB_MATL_PROP"` | object | - | **Required** |
| 4.1 | └ [When SLAB_PROP = true] Code · None · KSCE-LSD15(RC) · KS01-Civil(RC) · KS-Civil(RC) · KS19(RC) · KS01(RC) · KS(RC) | `"CODE"` | string | - | **Required** |
| 4.2 | └ [When SLAB_PROP = true] Grade | `"GRADE"` | string | - | Optional |
| 4.3 | └ [When CODE = "None"] Name | `"NAME"` | string | - | **Required** |
| 4.4 | └ [When CODE = "None"] Specified Compressive Strength (fc\|fck) · Minimum: 0 | `"COMP_STRENGTH"` | number | - | **Required** |
| 4.5 | └ [When CODE = "None"] Light Weight Concrete Factor (Lambda) | `"LIGHT_WEIGHT_FACTOR"` | boolean | false | Optional |
| 4.6 | └ [When LIGHT_WEIGHT_FACTOR = true] Lambda · Range: 0.75~1 | `"FACTOR_VALUE"` | number | 1 | **Required** |
| 4.2 | └ [When CODE = "KSCE-LSD15(RC)"] Grade · C15 · C18 · C21 · C24 · C27 · C30 · C35 · C40 · C45 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 · C90 · C95 | `"GRADE"` | string | - | Optional |
| 4.2 | └ [When CODE in ["KS01-Civil(RC)", "KS19(RC)", "KS01(RC)"]] Grade · C15 · C18 · C21 · C24 · C27 · C30 · C35 · C40 · C45 · C49 · C50 · C55 · C60 · C65 · C70 · C75 · C80 · C85 · C90 · C95 | `"GRADE"` | string | - | Optional |
| 4.2 | └ [When CODE in ["KS-Civil(RC)", "KS(RC)"]] Grade · C150 · C180 · C210 · C240 · C270 · C300 · C350 · C400 · C450 · C500 · C550 · C600 · C650 · C700 | `"GRADE"` | string | - | Optional |
| 5 | Rebar Selection | `"SLAB_REBAR_PROP"` | object | - | **Required** |
| 5.1 | └ Code · None · KSCE-LSD15(RC) · KS01-Civil(RC) · KS-Civil(RC) · KS19(RC) · KS01(RC) · KS(RC) | `"CODE"` | string | - | **Required** |
| 5.2 | └ Grade of Main Rebar | `"GRADE_MAIN_REBAR"` | string | - | Optional |
| 5.3 | └ [When CODE = "None"] Name of Main Rebar | `"NAME_MAIN_REBAR"` | string | - | **Required** |
| 5.4 | └ [When CODE = "None"] Fy · Minimum: 0 | `"Fy"` | number | - | **Required** |
| 5.5 | └ [When CODE = "None"] Grade of Sub-Rebar | `"GRADE_SUB_REBAR"` | string | - | Optional |
| 5.6 | └ [When CODE = "None"] Name of Sub-Rebar | `"NAME_SUB_REBAR"` | string | - | **Required** |
| 5.7 | └ [When CODE = "None"] Fys · Minimum: 0 | `"Fys"` | number | - | **Required** |
| 5.2 | └ [When CODE in ["KSCE-LSD15(RC)", "KS01-Civil(RC)", "KS01(RC)"]] Grade of Main Rebar · SD240 · SD300 · SD350 · SD400 · SD500 · SD600 | `"GRADE_MAIN_REBAR"` | string | - | Optional |
| 5.2 | └ [When CODE in ["KS-Civil(RC)", "KS(RC)"]] Grade of Main Rebar · SD24 · SD30 · SD35 · SD40 · SD50 | `"GRADE_MAIN_REBAR"` | string | - | Optional |
| 5.2 | └ [When CODE = "KS19(RC)"] Grade of Main Rebar · SD300 · SD400 · SD500 · SD600 · SD700 · SD400S · SD500S · SD600S | `"GRADE_MAIN_REBAR"` | string | - | Optional |
| 5.5 | └ [When CODE in ["KSCE-LSD15(RC)", "KS01-Civil(RC)", "KS01(RC)"]] Grade of Sub-Rebar · SD240 · SD300 · SD350 · SD400 · SD500 · SD600 | `"GRADE_SUB_REBAR"` | string | - | Optional |
| 5.5 | └ [When CODE in ["KS-Civil(RC)", "KS(RC)"]] Grade of Sub-Rebar · SD24 · SD30 · SD35 · SD40 · SD50 | `"GRADE_SUB_REBAR"` | string | - | Optional |
| 5.5 | └ [When CODE = "KS19(RC)"] Grade of Sub-Rebar · SD300 · SD400 · SD500 · SD600 · SD700 · SD400S · SD500S · SD600S | `"GRADE_SUB_REBAR"` | string | - | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a concrete material ID string (e.g., \"1\"): an existing material whose design type is concrete. Writing deletes PSC design results",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Modify Concrete Materials",
          "type": "object",
          "required": [
            "GIRDER_MATL_PROP",
            "GIRDER_REBAR_PROP"
          ],
          "additionalProperties": false,
          "properties": {
            "GIRDER_MATL_PROP": {
              "type": "object",
              "description": "Girder concrete material selection",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Korean concrete standard, or \"None\" for a user-defined concrete.",
                  "enum": [
                    "None",
                    "KSCE-LSD15(RC)",
                    "KS01-Civil(RC)",
                    "KS-Civil(RC)",
                    "KS19(RC)",
                    "KS01(RC)",
                    "KS(RC)"
                  ]
                },
                "GRADE": {
                  "type": "string",
                  "description": "Concrete grade of CODE (list depends on the code; checked against the material DB). Required when CODE is not None. fck is then taken from the DB"
                },
                "NAME": {
                  "type": "string",
                  "minLength": 1,
                  "description": "User-defined concrete name. Required when CODE is None (the Grade field becomes Name in the dialog)"
                },
                "COMP_STRENGTH": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "description": "Specified compressive strength fck, model stress unit, > 0. Required when CODE is None; ignored when CODE is a DB code (the grade value is used). fci is stored as 0.7 fck"
                },
                "LIGHT_WEIGHT_FACTOR": {
                  "type": "boolean",
                  "default": false,
                  "description": "Apply the light weight concrete factor (Lambda)"
                },
                "FACTOR_VALUE": {
                  "type": "number",
                  "minimum": 0.75,
                  "maximum": 1,
                  "default": 1,
                  "description": "Lambda value, 0.75 to 1.0. Used when LIGHT_WEIGHT_FACTOR is true (required then)"
                }
              }
            },
            "GIRDER_REBAR_PROP": {
              "type": "object",
              "description": "Girder rebar selection",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Korean rebar standard (same list as the concrete Code), or \"None\" for user-defined rebar",
                  "enum": [
                    "None",
                    "KSCE-LSD15(RC)",
                    "KS01-Civil(RC)",
                    "KS-Civil(RC)",
                    "KS19(RC)",
                    "KS01(RC)",
                    "KS(RC)"
                  ]
                },
                "GRADE_MAIN_REBAR": {
                  "type": "string",
                  "description": "Main rebar grade of CODE (checked against the material DB). Required when CODE is not None; Fy is then taken from the DB"
                },
                "NAME_MAIN_REBAR": {
                  "type": "string",
                  "minLength": 1,
                  "description": "User-defined main rebar name. Required when CODE is None"
                },
                "Fy": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "description": "Main rebar yield strength Fy, model stress unit, > 0. Required when CODE is None; ignored for a DB code"
                },
                "GRADE_SUB_REBAR": {
                  "type": "string",
                  "description": "Sub-rebar (shear rebar) grade of CODE. Required when CODE is not None; Fys is then taken from the DB"
                },
                "NAME_SUB_REBAR": {
                  "type": "string",
                  "minLength": 1,
                  "description": "User-defined sub-rebar name. Required when CODE is None"
                },
                "Fys": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "description": "Sub-rebar yield strength Fys, model stress unit, > 0. Required when CODE is None; ignored for a DB code"
                }
              }
            },
            "SLAB_PROP": {
              "type": "boolean",
              "default": false,
              "description": "Write the slab material (SLAB_MATL_PROP and SLAB_REBAR_PROP). Only used on a model with a composite PSC section, where both slab objects are then required; if false or omitted the stored slab data is kept"
            },
            "SLAB_MATL_PROP": {
              "type": "object",
              "description": "Slab concrete material selection",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Korean concrete standard, or \"None\" for a user-defined concrete.",
                  "enum": [
                    "None",
                    "KSCE-LSD15(RC)",
                    "KS01-Civil(RC)",
                    "KS-Civil(RC)",
                    "KS19(RC)",
                    "KS01(RC)",
                    "KS(RC)"
                  ]
                },
                "GRADE": {
                  "type": "string",
                  "description": "Concrete grade of CODE (list depends on the code; checked against the material DB). Required when CODE is not None. fck is then taken from the DB"
                },
                "NAME": {
                  "type": "string",
                  "minLength": 1,
                  "description": "User-defined concrete name. Required when CODE is None (the Grade field becomes Name in the dialog)"
                },
                "COMP_STRENGTH": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "description": "Specified compressive strength fck, model stress unit, > 0. Required when CODE is None; ignored when CODE is a DB code (the grade value is used). fci is stored as 0.7 fck"
                },
                "LIGHT_WEIGHT_FACTOR": {
                  "type": "boolean",
                  "default": false,
                  "description": "Apply the light weight concrete factor (Lambda)"
                },
                "FACTOR_VALUE": {
                  "type": "number",
                  "minimum": 0.75,
                  "maximum": 1,
                  "default": 1,
                  "description": "Lambda value, 0.75 to 1.0. Used when LIGHT_WEIGHT_FACTOR is true (required then)"
                }
              }
            },
            "SLAB_REBAR_PROP": {
              "type": "object",
              "description": "Slab rebar selection",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Korean rebar standard (same list as the concrete Code), or \"None\" for user-defined rebar",
                  "enum": [
                    "None",
                    "KSCE-LSD15(RC)",
                    "KS01-Civil(RC)",
                    "KS-Civil(RC)",
                    "KS19(RC)",
                    "KS01(RC)",
                    "KS(RC)"
                  ]
                },
                "GRADE_MAIN_REBAR": {
                  "type": "string",
                  "description": "Main rebar grade of CODE (checked against the material DB). Required when CODE is not None; Fy is then taken from the DB"
                },
                "NAME_MAIN_REBAR": {
                  "type": "string",
                  "minLength": 1,
                  "description": "User-defined main rebar name. Required when CODE is None"
                },
                "Fy": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "description": "Main rebar yield strength Fy, model stress unit, > 0. Required when CODE is None; ignored for a DB code"
                },
                "GRADE_SUB_REBAR": {
                  "type": "string",
                  "description": "Sub-rebar (shear rebar) grade of CODE. Required when CODE is not None; Fys is then taken from the DB"
                },
                "NAME_SUB_REBAR": {
                  "type": "string",
                  "minLength": 1,
                  "description": "User-defined sub-rebar name. Required when CODE is None"
                },
                "Fys": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "description": "Sub-rebar yield strength Fys, model stress unit, > 0. Required when CODE is None; ignored for a DB code"
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
        "CODE": "KSCE-LSD15(RC)",
        "GRADE": "C40"
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "KSCE-LSD15(RC)",
        "GRADE_MAIN_REBAR": "SD400",
        "GRADE_SUB_REBAR": "SD400"
      }
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
        "CODE": "KSCE-LSD15(RC)",
        "GRADE": "C40"
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "KSCE-LSD15(RC)",
        "GRADE_MAIN_REBAR": "SD400",
        "GRADE_SUB_REBAR": "SD400"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/MATD"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "GIRDER_MATL_PROP": {
        "CODE": "KSCE-LSD15(RC)",
        "GRADE": "C40"
      },
      "GIRDER_REBAR_PROP": {
        "CODE": "KSCE-LSD15(RC)",
        "GRADE_MAIN_REBAR": "SD400",
        "GRADE_SUB_REBAR": "SD400"
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

## 5. `DIOP` — Output Position

> **기능** PSC 설계 결과의 출력 위치를 지정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/DIOP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738147909657](https://support.midasuser.com/hc/ko/articles/64738147909657)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is an element ID string (e.g., "1"): a beam element with a PSC or composite section and a concrete design material. Virtual beams use /DESIGN/PSC/KDS-24-14-21-2021/DIOP-VBEAM | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Moment Resistance | `"MOMENT_STRENGTH"` | object | - | **Required** |
| 1.1 | └ [General] Positive Moment · None: 0 · I: 1 · J: 2 · I & J: 3 | `"POSITIVE_MOMENT"` | integer | 3 | **Required** |
| 1.2 | └ [General] Negative Moment · None: 0 · I: 1 · J: 2 · I & J: 3 | `"NEGATIVE_MOMENT"` | integer | 3 | **Required** |
| 2 | [General] Shear Resistance · None: 0 · I: 1 · J: 2 · I & J: 3 | `"SHEAR_TYPE"` | integer | 3 | **Required** |
| 3 | [General] Torsional Resistance · None: 0 · I: 1 · J: 2 · I & J: 3 | `"TORSION_TYPE"` | integer | 3 | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is an element ID string (e.g., \"1\"): a beam element with a PSC or composite section and a concrete design material. Virtual beams use /DESIGN/PSC/KDS-24-14-21-2021/DIOP-VBEAM",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Position for PSC Output",
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
              "description": "Output positions for moment resistance, positive and negative moment",
              "required": [
                "POSITIVE_MOMENT",
                "NEGATIVE_MOMENT"
              ],
              "additionalProperties": false,
              "properties": {
                "POSITIVE_MOMENT": {
                  "type": "integer",
                  "description": "Ends output for positive moment resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
                  "default": 3,
                  "enum": [
                    0,
                    1,
                    2,
                    3
                  ]
                },
                "NEGATIVE_MOMENT": {
                  "type": "integer",
                  "description": "Ends output for negative moment resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
                  "default": 3,
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
              "description": "Ends output for shear resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
              "default": 3,
              "enum": [
                0,
                1,
                2,
                3
              ]
            },
            "TORSION_TYPE": {
              "type": "integer",
              "description": "Ends output for torsional resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
              "default": 3,
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
    "1": {
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      },
      "SHEAR_TYPE": 3,
      "TORSION_TYPE": 0
    }
  }
}
```

**Response**

```json
{
  "DIOP": {
    "1": {
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      },
      "SHEAR_TYPE": 3,
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/DIOP"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      },
      "SHEAR_TYPE": 3,
      "TORSION_TYPE": 0
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 6. `SLCT` — Serviceability Load Combination Type

> **기능** PSC 설계의 사용성 하중조합 유형을 설정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/SLCT
```

### Active Methods

`GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738155883673](https://support.midasuser.com/hc/ko/articles/64738155883673)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a load combination index string, such as "1". | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Serviceability Load Combination Name | `"LC_NAME"` | string | - | **Required** |
| 2 | [General] Serviceability Load Type · Serviceability Load Combination: 0 · Serviceability Load Combination I: 1 · Serviceability Load Combination III/IV: 2 · Serviceability Load Combination V: 3 | `"SL_TYPE"` | integer | 0 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a load combination index string, such as \"1\".",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "LC_NAME"
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
                2,
                3
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

- `SLCT`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "3": {
      "LC_NAME": "cLCB3",
      "SL_TYPE": 3
    }
  }
}
```

**Response**

```json
{
  "SLCT": {
    "3": {
      "LC_NAME": "cLCB3",
      "SL_TYPE": 3
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/SLCT"

payload = json.loads(r'''
{
  "Assign": {
    "3": {
      "LC_NAME": "cLCB3",
      "SL_TYPE": 3
    }
  }
}
''')
response = requests.put(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 7. `PSCN` — Shear Connector

> **기능** 전단연결재 정보를 설정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/PSCN
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738185313305](https://support.midasuser.com/hc/ko/articles/64738185313305)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a beam element number (e.g., "21"). Element Type = Element of the panel. Virtual beams use /DESIGN/PSC/KDS-24-14-21-2021/PSCN-VBEAM | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Both end parts(i & j) have the same shear connector | `"BOTH_ENDS"` | boolean | true | Optional |
| 2 | [General] I | `"I"` | object | - | Optional |
| 2.1 | └ [General] Surface Classification(cl.6.2.5) · Very Smooth: "VERY SMOOTH" · Smooth: "SMOOTH" · Rough: "ROUGH" · Indented: "INDENTED" | `"SURFACE_CLASS"` | string | VERY SMOOTH | Optional |
| 2.2 | └ [General] Angle · Range: 0~90 | `"ANGLE"` | number | 0 | Optional |
| 2.3 | └ [General] As · Minimum: 0 | `"AREA"` | number | 0 | Optional |
| 2.4 | └ [General] Fy · Minimum: 0 | `"FY"` | number | 0 | Optional |
| 3 | [General] J | `"J"` | object | - | Optional |
| 3.1 | └ [General] Surface Classification(cl.6.2.5) · Very Smooth: "VERY SMOOTH" · Smooth: "SMOOTH" · Rough: "ROUGH" · Indented: "INDENTED" | `"SURFACE_CLASS"` | string | VERY SMOOTH | Optional |
| 3.2 | └ [General] Angle · Range: 0~90 | `"ANGLE"` | number | 0 | Optional |
| 3.3 | └ [General] As · Minimum: 0 | `"AREA"` | number | 0 | Optional |
| 3.4 | └ [General] Fy · Minimum: 0 | `"FY"` | number | 0 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a beam element number (e.g., \"21\"). Element Type = Element of the panel. Virtual beams use /DESIGN/PSC/KDS-24-14-21-2021/PSCN-VBEAM",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Shear Connector",
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "BOTH_ENDS": {
              "type": "boolean",
              "description": "Both end parts (i & j) have the same shear connector. true: the I-end values are stored for the J end as well; J must then be omitted or equal to I (otherwise rejected). Omitted on PUT: the stored value is kept",
              "default": true
            },
            "I": {
              "type": "object",
              "description": "Shear connector at the I end (tab I). Omitted members keep the stored values on PUT",
              "additionalProperties": false,
              "properties": {
                "SURFACE_CLASS": {
                  "type": "string",
                  "description": "Surface classification of the interface at the I end",
                  "enum": [
                    "VERY SMOOTH",
                    "SMOOTH",
                    "ROUGH",
                    "INDENTED"
                  ],
                  "default": "VERY SMOOTH"
                },
                "ANGLE": {
                  "type": "number",
                  "description": "Angle of the shear connector at the I end [deg], 0 to 90",
                  "default": 0,
                  "minimum": 0,
                  "maximum": 90
                },
                "AREA": {
                  "type": "number",
                  "description": "Area of the shear connector As at the I end, in the model area unit (>= 0)",
                  "default": 0,
                  "minimum": 0
                },
                "FY": {
                  "type": "number",
                  "description": "Yield strength of the shear connector Fy at the I end, in the model stress unit (>= 0)",
                  "default": 0,
                  "minimum": 0
                }
              }
            },
            "J": {
              "type": "object",
              "description": "Shear connector at the J end (tab J). Used when BOTH_ENDS is false; with BOTH_ENDS true it must be omitted or equal to I",
              "additionalProperties": false,
              "properties": {
                "SURFACE_CLASS": {
                  "type": "string",
                  "description": "Surface classification of the interface at the J end",
                  "enum": [
                    "VERY SMOOTH",
                    "SMOOTH",
                    "ROUGH",
                    "INDENTED"
                  ],
                  "default": "VERY SMOOTH"
                },
                "ANGLE": {
                  "type": "number",
                  "description": "Angle of the shear connector at the J end [deg], 0 to 90",
                  "default": 0,
                  "minimum": 0,
                  "maximum": 90
                },
                "AREA": {
                  "type": "number",
                  "description": "Area of the shear connector As at the J end, in the model area unit (>= 0)",
                  "default": 0,
                  "minimum": 0
                },
                "FY": {
                  "type": "number",
                  "description": "Yield strength of the shear connector Fy at the J end, in the model stress unit (>= 0)",
                  "default": 0,
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

- `PSCN`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "1": {
      "I": {
        "SURFACE_CLASS": "ROUGH",
        "ANGLE": 90.0,
        "AREA": 157.0,
        "FY": 400.0
      }
    }
  }
}
```

**Response**

```json
{
  "PSCN": {
    "1": {
      "I": {
        "SURFACE_CLASS": "ROUGH",
        "ANGLE": 90,
        "AREA": 157,
        "FY": 400
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/PSCN"

payload = json.loads(r'''
{
  "Assign": {
    "1": {
      "I": {
        "SURFACE_CLASS": "ROUGH",
        "ANGLE": 90.0,
        "AREA": 157.0,
        "FY": 400.0
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

## 8. `PSC-ANAL` — Perform Design

> **기능** PSC 설계를 수행합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/PSC-ANAL
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738185410457](https://support.midasuser.com/hc/ko/articles/64738185410457)

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

- `SUCCESS`, `RESULT`, `CATEGORY`, `MESSAGE`

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
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "MESSAGE": ""
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/PSC-ANAL"

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


---

## 9. `TABLE` · `PSC_SHEAR_TORSION` — Check Combined Shear and Torsion Strength

> **기능** 전단과 비틀림의 조합 강도 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738160708633](https://support.midasuser.com/hc/ko/articles/64738160708633)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Check Combined Shear and Torsion Strength: "PSC_SHEAR_TORSION" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Element | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Max/Min | `"MAX_MIN"` | array | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check Combined Shear and Torsion Strength - Result Table Type",
          "enum": [
            "PSC_SHEAR_TORSION"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "Elem",
              "Part",
              "Max/Min",
              "LComName",
              "DesignSituations",
              "Type",
              "CHK",
              "Tu",
              "Td,max",
              "Vu",
              "Vd,max",
              "Ratio",
              "Asl",
              "Asl,req",
              "s",
              "sl,max",
              "rho_st",
              "rho_st,min"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "MAX_MIN": {
          "type": "array",
          "description": "V-Max, V-Min or T-Max Rows (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "V-Max",
              "V-Min",
              "T-Max"
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

- `empty` — `Index`, `Elem`, `Part`, `Max/Min`, `LComName`, `DesignSituations`, `Type`, `CHK`, `Tu`, `Td,max`, `Vu`, `Vd,max`, `Ratio`, `Asl`, `Asl,req`, `s`, `sl,max`, `rho_st`, `rho_st,min`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_SHEAR_TORSION"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "DesignSituations",
      "Type",
      "CHK",
      "Tu",
      "Td,max",
      "Vu",
      "Vd,max",
      "Ratio",
      "Asl",
      "Asl,req",
      "s",
      "sl,max",
      "rho_st",
      "rho_st,min"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[1]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-2238.0767",
        "9476.9789",
        "0.2362",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "2",
        "1",
        "I[1]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-2238.0767",
        "9476.9789",
        "0.2362",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "3",
        "1",
        "I[1]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-2238.0767",
        "9476.9789",
        "0.2362",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "4",
        "1",
        "J[2]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-1287.5913",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "5",
        "1",
        "J[2]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-1287.5913",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "6",
        "1",
        "J[2]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-1287.5913",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "7",
        "2",
        "I[2]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-1287.5913",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "8",
        "2",
        "I[2]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-1287.5913",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "9",
        "2",
        "I[2]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-1287.5913",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "10",
        "2",
        "J[3]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "11",
        "2",
        "J[3]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "12",
        "2",
        "J[3]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "13",
        "3",
        "I[3]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "14",
        "3",
        "I[3]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "15",
        "3",
        "I[3]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "16",
        "3",
        "J[4]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "0.0000",
        "9476.9789",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "17",
        "3",
        "J[4]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "0.0000",
        "9476.9789",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "18",
        "3",
        "J[4]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "0.0000",
        "9476.9789",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "19",
        "4",
        "I[4]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-0.0000",
        "9476.9789",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "20",
        "4",
        "I[4]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-0.0000",
        "9476.9789",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "21",
        "4",
        "I[4]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "-0.0000",
        "9476.9789",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "22",
        "4",
        "J[5]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "23",
        "4",
        "J[5]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "24",
        "4",
        "J[5]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "25",
        "5",
        "I[5]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "26",
        "5",
        "I[5]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "27",
        "5",
        "I[5]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "587.5766",
        "9476.9789",
        "0.0620",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "28",
        "5",
        "J[6]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "1287.5914",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "29",
        "5",
        "J[6]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "1287.5914",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "30",
        "5",
        "J[6]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "1287.5914",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "31",
        "6",
        "I[6]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "1287.5914",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "32",
        "6",
        "I[6]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "1287.5914",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "33",
        "6",
        "I[6]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "1287.5914",
        "9476.9789",
        "0.1359",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "34",
        "6",
        "J[7]",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "2238.0767",
        "9476.9789",
        "0.2362",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "35",
        "6",
        "J[7]",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "2238.0767",
        "9476.9789",
        "0.2362",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
      ],
      [
        "36",
        "6",
        "J[7]",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "45564.2604",
        "2238.0767",
        "9476.9789",
        "0.2362",
        "0.0000",
        "0.0000",
        "0.0000",
        "1.4854",
        "0.0000",
        "0.0013"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_SHEAR_TORSION"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 10. `TABLE` · `PSC_CRACK_WIDTH` — Check crack width at service loads

> **기능** 사용하중에 대한 균열폭 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738185602457](https://support.midasuser.com/hc/ko/articles/64738185602457)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Check crack width at service loads: "PSC_CRACK_WIDTH" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Element | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Top/Bottom | `"TOP_BOT"` | array | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check crack width at service loads - Result Table Type",
          "enum": [
            "PSC_CRACK_WIDTH"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "Elem",
              "Part",
              "Top/Bottom",
              "LComName",
              "ServiceabilityLoadType",
              "Type",
              "CHK",
              "N_Ed",
              "M_Ed",
              "S_r,max",
              "Ep_sm-Ep_cm",
              "Wk",
              "Wmax",
              "As",
              "As,min"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "TOP_BOT": {
          "type": "array",
          "description": "Top or Bottom Fiber (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Top",
              "Bottom"
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

- `crack` — `Index`, `Elem`, `Part`, `Top/Bottom`, `LComName`, `ServiceabilityLoadType`, `Type`, `CHK`, `N_Ed`, `M_Ed`, `S_r,max`, `Ep_sm-Ep_cm`, `Wk`, `Wmax`, `As`, `As,min`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_CRACK_WIDTH",
    "NODE_ELEMS": {
      "TO": "1to5"
    },
    "TOP_BOT": [
      "Top"
    ],
    "TABLE_NAME": "crack"
  }
}
```

**Response**

```json
{
  "crack": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Top/Bottom",
      "LComName",
      "ServiceabilityLoadType",
      "Type",
      "CHK",
      "N_Ed",
      "M_Ed",
      "S_r,max",
      "Ep_sm-Ep_cm",
      "Wk",
      "Wmax",
      "As",
      "As,min"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[1]",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-1894.4455",
        "-567.1705",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "2",
        "1",
        "J[2]",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2011.7441",
        "6342.1130",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "3",
        "2",
        "I[2]",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2011.7441",
        "6342.1130",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "4",
        "2",
        "J[3]",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2092.9110",
        "10293.5890",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "5",
        "3",
        "I[3]",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2092.9110",
        "10293.5890",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "6",
        "3",
        "J[4]",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2034.4089",
        "11601.2394",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "7",
        "4",
        "I[4]",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2034.4086",
        "11601.2396",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "8",
        "4",
        "J[5]",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2092.9106",
        "10293.5891",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "9",
        "5",
        "I[5]",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2092.9106",
        "10293.5891",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "10",
        "5",
        "J[6]",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2011.7439",
        "6342.1131",
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_CRACK_WIDTH",
    "NODE_ELEMS": {
      "TO": "1to5"
    },
    "TOP_BOT": [
      "Top"
    ],
    "TABLE_NAME": "crack"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 11. `TABLE` · `PSC_FLEXURE` — Check Flexure Strength

> **기능** 휨강도 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738148517657](https://support.midasuser.com/hc/ko/articles/64738148517657)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Check Flexure Strength: "PSC_FLEXURE" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Element | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Positive/Negative | `"POS_NEG"` | array | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check Flexure Strength - Result Table Type",
          "enum": [
            "PSC_FLEXURE"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "Elem",
              "Element",
              "Part",
              "Positive/Negative",
              "LComName",
              "DesignSituations",
              "Type",
              "CHK",
              "Mu",
              "Md",
              "Mu/Md",
              "c,max",
              "c",
              "As,max",
              "As,min",
              "As"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "POS_NEG": {
          "type": "array",
          "description": "Positive or Negative Moment (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Positive",
              "Negative"
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

- `empty` — `Index`, `Elem`, `Part`, `Positive/Negative`, `LComName`, `DesignSituations`, `Type`, `CHK`, `Mu`, `Md`, `Mu/Md`, `c,max`, `c`, `As,max`, `As,min`, `As`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_FLEXURE"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Positive/Negative",
      "LComName",
      "DesignSituations",
      "Type",
      "CHK",
      "Mu",
      "Md",
      "Mu/Md",
      "c,max",
      "c",
      "As,max",
      "As,min",
      "As"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[1]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "-567.1705",
        "2687.7921",
        "0.2110",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "2",
        "1",
        "I[1]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "2756.1276",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "3",
        "1",
        "J[2]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "2078.3390",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "4",
        "1",
        "J[2]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "8207.1770",
        "3365.5807",
        "2.4386",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "5",
        "2",
        "I[2]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "2078.3390",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "6",
        "2",
        "I[2]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "8207.1770",
        "3365.5807",
        "2.4386",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "7",
        "2",
        "J[3]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "1533.7346",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "8",
        "2",
        "J[3]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "13277.6912",
        "3910.1850",
        "3.3957",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "9",
        "3",
        "I[3]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "1533.7346",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "10",
        "3",
        "I[3]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "13277.6912",
        "3910.1850",
        "3.3957",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "11",
        "3",
        "J[4]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "1264.6545",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "12",
        "3",
        "J[4]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "14958.3544",
        "4179.2652",
        "3.5792",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "13",
        "4",
        "I[4]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "1264.6545",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "14",
        "4",
        "I[4]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "14958.3546",
        "4179.2652",
        "3.5792",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "15",
        "4",
        "J[5]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "1533.7346",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "16",
        "4",
        "J[5]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "13277.6914",
        "3910.1850",
        "3.3957",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "17",
        "5",
        "I[5]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "1533.7346",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "18",
        "5",
        "I[5]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "13277.6914",
        "3910.1850",
        "3.3957",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "19",
        "5",
        "J[6]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "2078.3390",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "20",
        "5",
        "J[6]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "8207.1771",
        "3365.5807",
        "2.4386",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "21",
        "6",
        "I[6]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "2078.3390",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "22",
        "6",
        "I[6]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "8207.1771",
        "3365.5807",
        "2.4386",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "23",
        "6",
        "J[7]",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "-567.1703",
        "2687.7921",
        "0.2110",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
        "0.0000"
      ],
      [
        "24",
        "6",
        "J[7]",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "2756.1276",
        "0.0000",
        "0.7922",
        "0.0373",
        "0.0653",
        "0.0065",
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_FLEXURE"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 12. `TABLE` · `PSC_SHEAR` — Check Shear Strength

> **기능** 전단강도 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738185885081](https://support.midasuser.com/hc/ko/articles/64738185885081)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Check Shear Strength: "PSC_SHEAR" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Element | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Max/Min | `"MAX_MIN"` | array | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check Shear Strength - Result Table Type",
          "enum": [
            "PSC_SHEAR"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "Elem",
              "Part",
              "Max/Min",
              "LComName",
              "DesignSituations",
              "Type",
              "CHK",
              "Vu",
              "Vd",
              "Vu/Vd",
              "rho_v",
              "rho_v,min",
              "s",
              "s,max"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "MAX_MIN": {
          "type": "array",
          "description": "Maximum or Minimum Shear (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Max",
              "Min"
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

- `empty` — `Index`, `Elem`, `Part`, `Max/Min`, `LComName`, `DesignSituations`, `Type`, `CHK`, `Vu`, `Vd`, `Vu/Vd`, `rho_v`, `rho_v,min`, `s`, `s,max`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_SHEAR"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
      "Max/Min",
      "LComName",
      "DesignSituations",
      "Type",
      "CHK",
      "Vu",
      "Vd",
      "Vu/Vd",
      "rho_v",
      "rho_v,min",
      "s",
      "s,max"
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[1]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-2238.0767",
        "3096.0441",
        "0.7229",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "2",
        "1",
        "I[1]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-2238.0767",
        "3096.0441",
        "0.7229",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "3",
        "1",
        "J[2]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-1287.5913",
        "3124.3892",
        "0.4121",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "4",
        "1",
        "J[2]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-1287.5913",
        "3124.3892",
        "0.4121",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "5",
        "2",
        "I[2]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-1287.5913",
        "3124.3892",
        "0.4121",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "6",
        "2",
        "I[2]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-1287.5913",
        "3124.3892",
        "0.4121",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "7",
        "2",
        "J[3]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-587.5766",
        "1317.9184",
        "0.4458",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "8",
        "2",
        "J[3]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-587.5766",
        "1317.9184",
        "0.4458",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "9",
        "3",
        "I[3]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-587.5766",
        "1317.9184",
        "0.4458",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "10",
        "3",
        "I[3]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-587.5766",
        "1317.9184",
        "0.4458",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "11",
        "3",
        "J[4]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "0.0000",
        "1312.4006",
        "0.0000",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "12",
        "3",
        "J[4]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "0.0000",
        "1312.4006",
        "0.0000",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "13",
        "4",
        "I[4]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-0.0000",
        "1312.4006",
        "0.0000",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "14",
        "4",
        "I[4]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-0.0000",
        "1312.4006",
        "0.0000",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "15",
        "4",
        "J[5]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "587.5766",
        "1317.9184",
        "0.4458",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "16",
        "4",
        "J[5]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "587.5766",
        "1317.9184",
        "0.4458",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "17",
        "5",
        "I[5]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "587.5766",
        "1317.9184",
        "0.4458",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "18",
        "5",
        "I[5]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "587.5766",
        "1317.9184",
        "0.4458",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "19",
        "5",
        "J[6]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "1287.5914",
        "3124.3891",
        "0.4121",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "20",
        "5",
        "J[6]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "1287.5914",
        "3124.3891",
        "0.4121",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "21",
        "6",
        "I[6]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "1287.5914",
        "3124.3891",
        "0.4121",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "22",
        "6",
        "I[6]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "1287.5914",
        "3124.3891",
        "0.4121",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "23",
        "6",
        "J[7]",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "2238.0767",
        "3096.0440",
        "0.7229",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
      ],
      [
        "24",
        "6",
        "J[7]",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "2238.0767",
        "3096.0440",
        "0.7229",
        "0.0000",
        "0.0013",
        "0.0000",
        "1.4854"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_SHEAR"
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
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738186026905](https://support.midasuser.com/hc/ko/articles/64738186026905)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Check stress for cross section at a construction stage: "PSC_STRESS_CS" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Element | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Comp./Tens. | `"COMP_TENS"` | array | - | Optional |
| 10 | [General] Girder/Slab · Girder: "Girder" · Slab: "Slab" | `"SELECTION_TYPE"` | string | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check stress for cross section at a construction stage - Result Table Type",
          "enum": [
            "PSC_STRESS_CS"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Compression",
              "Tension"
            ]
          }
        },
        "SELECTION_TYPE": {
          "type": "string",
          "description": "Girder or Slab Selection",
          "enum": [
            "Girder",
            "Slab"
          ]
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `empty` — `Index`, `Elem`, `Part`, `Comp./Tens.`, `Stage`, `CHK`, `FT`, `FB`, `FTL`, `FBL`, `FTR`, `FBR`, `FMAX`, `ALW`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_CS"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Elem",
      "Part",
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
    ],
    "DATA": [
      [
        "1",
        "1",
        "I[1]",
        "Compression",
        "CS2_Tensioning",
        "OK",
        "239.0478",
        "635.5305",
        "239.0478",
        "635.5305",
        "239.0478",
        "635.5305",
        "635.5305",
        "20857.2580"
      ],
      [
        "2",
        "1",
        "I[1]",
        "Tension",
        "CS2_Tensioning",
        "OK",
        "239.0478",
        "635.5305",
        "239.0478",
        "635.5305",
        "239.0478",
        "635.5305",
        "239.0478",
        "2067.7960"
      ],
      [
        "3",
        "1",
        "J[2]",
        "Compression",
        "CS1_Erection",
        "OK",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "12859.6737"
      ],
      [
        "4",
        "1",
        "J[2]",
        "Tension",
        "CS1_Erection",
        "NG",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "-3234.5712",
        "1274.9127"
      ],
      [
        "5",
        "2",
        "I[2]",
        "Compression",
        "CS1_Erection",
        "OK",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "12859.6737"
      ],
      [
        "6",
        "2",
        "I[2]",
        "Tension",
        "CS1_Erection",
        "NG",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "-3234.5712",
        "1274.9127"
      ],
      [
        "7",
        "2",
        "J[3]",
        "Compression",
        "CS1_Erection",
        "OK",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "12859.6737"
      ],
      [
        "8",
        "2",
        "J[3]",
        "Tension",
        "CS1_Erection",
        "NG",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "-5175.3505",
        "1274.9127"
      ],
      [
        "9",
        "3",
        "I[3]",
        "Compression",
        "CS1_Erection",
        "OK",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "12859.6737"
      ],
      [
        "10",
        "3",
        "I[3]",
        "Tension",
        "CS1_Erection",
        "NG",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "-5175.3505",
        "1274.9127"
      ],
      [
        "11",
        "3",
        "J[4]",
        "Compression",
        "CS1_Erection",
        "OK",
        "3545.6060",
        "-5822.2935",
        "3545.6060",
        "-5822.2935",
        "3545.6060",
        "-5822.2935",
        "3545.6060",
        "12859.6737"
      ],
      [
        "12",
        "3",
        "J[4]",
        "Tension",
        "CS1_Erection",
        "NG",
        "3545.6060",
        "-5822.2935",
        "3545.6060",
        "-5822.2935",
        "3545.6060",
        "-5822.2935",
        "-5822.2935",
        "1274.9127"
      ],
      [
        "13",
        "4",
        "I[4]",
        "Compression",
        "CS1_Erection",
        "OK",
        "3545.6060",
        "-5822.2935",
        "3545.6060",
        "-5822.2935",
        "3545.6060",
        "-5822.2935",
        "3545.6060",
        "12859.6737"
      ],
      [
        "14",
        "4",
        "I[4]",
        "Tension",
        "CS1_Erection",
        "NG",
        "3545.6060",
        "-5822.2935",
        "3545.6060",
        "-5822.2935",
        "3545.6060",
        "-5822.2935",
        "-5822.2935",
        "1274.9127"
      ],
      [
        "15",
        "4",
        "J[5]",
        "Compression",
        "CS1_Erection",
        "OK",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "12859.6737"
      ],
      [
        "16",
        "4",
        "J[5]",
        "Tension",
        "CS1_Erection",
        "NG",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "-5175.3505",
        "1274.9127"
      ],
      [
        "17",
        "5",
        "I[5]",
        "Compression",
        "CS1_Erection",
        "OK",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "12859.6737"
      ],
      [
        "18",
        "5",
        "I[5]",
        "Tension",
        "CS1_Erection",
        "NG",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "3151.6442",
        "-5175.3505",
        "-5175.3505",
        "1274.9127"
      ],
      [
        "19",
        "5",
        "J[6]",
        "Compression",
        "CS1_Erection",
        "OK",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "12859.6737"
      ],
      [
        "20",
        "5",
        "J[6]",
        "Tension",
        "CS1_Erection",
        "NG",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "-3234.5712",
        "1274.9127"
      ],
      [
        "21",
        "6",
        "I[6]",
        "Compression",
        "CS1_Erection",
        "OK",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "12859.6737"
      ],
      [
        "22",
        "6",
        "I[6]",
        "Tension",
        "CS1_Erection",
        "NG",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "1969.7732",
        "-3234.5712",
        "-3234.5712",
        "1274.9127"
      ],
      [
        "23",
        "6",
        "J[7]",
        "Compression",
        "CS2_Tensioning",
        "OK",
        "239.0477",
        "635.5303",
        "239.0478",
        "635.5303",
        "239.0478",
        "635.5303",
        "635.5303",
        "20857.2580"
      ],
      [
        "24",
        "6",
        "J[7]",
        "Tension",
        "CS2_Tensioning",
        "OK",
        "239.0477",
        "635.5303",
        "239.0478",
        "635.5303",
        "239.0478",
        "635.5303",
        "239.0477",
        "2067.7960"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_CS"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 14. `TABLE` · `PSC_STRESS_SERVICE` — Check stress for cross section at service loads

> **기능** 사용하중에 대한 단면 응력 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738156595097](https://support.midasuser.com/hc/ko/articles/64738156595097)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Check stress for cross section at service loads: "PSC_STRESS_SERVICE" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Element | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Comp./Tens. | `"COMP_TENS"` | array | - | Optional |
| 10 | [General] Girder/Slab · Girder: "Girder" · Slab: "Slab" | `"SELECTION_TYPE"` | string | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check stress for cross section at service loads - Result Table Type",
          "enum": [
            "PSC_STRESS_SERVICE"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Compression",
              "Tension"
            ]
          }
        },
        "SELECTION_TYPE": {
          "type": "string",
          "description": "Girder or Slab Selection",
          "enum": [
            "Girder",
            "Slab"
          ]
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `empty` — `Index`, `Elem`, `Part`, `Comp./Tens.`, `LComName`, `Type`, `CHK`, `FT`, `FB`, `FTL`, `FBL`, `FTR`, `FBR`, `FMAX`, `ALW`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_SERVICE"
  }
}
```

**Response**

```json
{
  "empty": {
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
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "238.4914",
        "634.0510",
        "238.4915",
        "634.0511",
        "238.4915",
        "634.0511",
        "634.0511",
        "24000"
      ],
      [
        "2",
        "1",
        "J[2]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "24000"
      ],
      [
        "3",
        "2",
        "I[2]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "-2332.7193",
        "2087.5340",
        "24000"
      ],
      [
        "4",
        "2",
        "J[3]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "24000"
      ],
      [
        "5",
        "3",
        "I[3]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "-4020.8716",
        "3146.8461",
        "24000"
      ],
      [
        "6",
        "3",
        "J[4]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "3479.1790",
        "-4594.4926",
        "3479.1790",
        "-4594.4926",
        "3479.1790",
        "-4594.4926",
        "3479.1790",
        "24000"
      ],
      [
        "7",
        "4",
        "I[4]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "3479.1790",
        "-4594.4928",
        "3479.1790",
        "-4594.4928",
        "3479.1790",
        "-4594.4928",
        "3479.1790",
        "24000"
      ],
      [
        "8",
        "4",
        "J[5]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "3146.8461",
        "-4020.8717",
        "3146.8461",
        "-4020.8717",
        "3146.8461",
        "-4020.8717",
        "3146.8461",
        "24000"
      ],
      [
        "9",
        "5",
        "I[5]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "3146.8461",
        "-4020.8717",
        "3146.8461",
        "-4020.8717",
        "3146.8461",
        "-4020.8717",
        "3146.8461",
        "24000"
      ],
      [
        "10",
        "5",
        "J[6]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "2087.5339",
        "-2332.7194",
        "2087.5339",
        "-2332.7194",
        "2087.5339",
        "-2332.7194",
        "2087.5339",
        "24000"
      ],
      [
        "11",
        "6",
        "I[6]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "2087.5339",
        "-2332.7194",
        "2087.5339",
        "-2332.7194",
        "2087.5339",
        "-2332.7194",
        "2087.5339",
        "24000"
      ],
      [
        "12",
        "6",
        "J[7]",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "238.4914",
        "634.0508",
        "238.4914",
        "634.0509",
        "238.4914",
        "634.0509",
        "634.0509",
        "24000"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_SERVICE"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 15. `TABLE` · `PSC_STRESS_TENDON` — Check tensile stress for Prestressing tendons

> **기능** 프리스트레싱 긴장재의 인장응력 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738156696729](https://support.midasuser.com/hc/ko/articles/64738156696729)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Check tensile stress for Prestressing tendons: "PSC_STRESS_TENDON" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Tendon | `"TENDON"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check tensile stress for Prestressing tendons - Result Table Type",
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
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each Tendon ID",
              "items": {
                "type": "integer",
                "minimum": 1
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify Tendon ID Range (e.g., '1to10')"
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

- `empty` — `Index`, `Tendon`, `FDL1`, `FDL2`, `FLL1`, `AFDL1`, `AFDL2`, `AFLL1`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_TENDON",
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
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Tendon",
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
        "T1",
        "1135758.6930",
        "1262391.6367",
        "1224976.1691",
        "1422000.0000",
        "1343000.0000",
        "1027000.0000"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_TENDON",
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

## 16. `TABLE` · `PSC_DGN_FORCE` — Design Forces

> **기능** PSC 설계에 사용한 부재력을 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738186294169](https://support.midasuser.com/hc/ko/articles/64738186294169)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · PSC Design Forces: "PSC_DGN_FORCE" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Element | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 7.3 | └ [General] Structure Group Name | `"STRUCTURE_GROUP_NAME"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Design Forces - Result Table Type",
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
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
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

- `empty` — `Index`, `Elem`, `Part`, `LComName`, `Type`, `Fx`, `Fy`, `Fz`, `Mx`, `My`, `Mz`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_DGN_FORCE"
  }
}
```

**Response**

```json
{
  "empty": {
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
        "cLCB1",
        "-",
        "-1894.4455",
        "0.0000",
        "-2238.0767",
        "0.0000",
        "-567.1705",
        "0.0000"
      ],
      [
        "2",
        "1",
        "I",
        "cLCB2",
        "-",
        "-1894.4455",
        "0.0000",
        "-1790.4614",
        "0.0000",
        "-567.1705",
        "0.0000"
      ],
      [
        "3",
        "1",
        "I",
        "cLCB3",
        "-",
        "-1894.4455",
        "0.0000",
        "-1790.4614",
        "0.0000",
        "-567.1705",
        "0.0000"
      ],
      [
        "4",
        "1",
        "J",
        "cLCB1",
        "-",
        "-2011.7441",
        "0.0000",
        "-1388.4984",
        "0.0000",
        "8207.1770",
        "0.0000"
      ],
      [
        "5",
        "1",
        "J",
        "cLCB2",
        "-",
        "-2011.7441",
        "0.0000",
        "-1090.0882",
        "0.0000",
        "6342.1130",
        "0.0000"
      ],
      [
        "6",
        "1",
        "J",
        "cLCB3",
        "-",
        "-2011.7441",
        "0.0000",
        "-1090.0882",
        "0.0000",
        "6342.1130",
        "0.0000"
      ],
      [
        "7",
        "2",
        "I",
        "cLCB1",
        "-",
        "-2011.7441",
        "0.0000",
        "-1388.4984",
        "0.0000",
        "8207.1770",
        "0.0000"
      ],
      [
        "8",
        "2",
        "I",
        "cLCB2",
        "-",
        "-2011.7441",
        "0.0000",
        "-1090.0882",
        "0.0000",
        "6342.1130",
        "0.0000"
      ],
      [
        "9",
        "2",
        "I",
        "cLCB3",
        "-",
        "-2011.7441",
        "0.0000",
        "-1090.0882",
        "0.0000",
        "6342.1130",
        "0.0000"
      ],
      [
        "10",
        "2",
        "J",
        "cLCB1",
        "-",
        "-2092.9110",
        "0.0000",
        "-665.6297",
        "0.0000",
        "13277.6912",
        "0.0000"
      ],
      [
        "11",
        "2",
        "J",
        "cLCB2",
        "-",
        "-2092.9110",
        "0.0000",
        "-516.4246",
        "0.0000",
        "10293.5890",
        "0.0000"
      ],
      [
        "12",
        "2",
        "J",
        "cLCB3",
        "-",
        "-2092.9110",
        "0.0000",
        "-516.4246",
        "0.0000",
        "10293.5890",
        "0.0000"
      ],
      [
        "13",
        "3",
        "I",
        "cLCB1",
        "-",
        "-2092.9110",
        "0.0000",
        "-665.6297",
        "0.0000",
        "13277.6912",
        "0.0000"
      ],
      [
        "14",
        "3",
        "I",
        "cLCB2",
        "-",
        "-2092.9110",
        "0.0000",
        "-516.4246",
        "0.0000",
        "10293.5890",
        "0.0000"
      ],
      [
        "15",
        "3",
        "I",
        "cLCB3",
        "-",
        "-2092.9110",
        "0.0000",
        "-516.4246",
        "0.0000",
        "10293.5890",
        "0.0000"
      ],
      [
        "16",
        "3",
        "J",
        "cLCB1",
        "-",
        "-2034.4089",
        "0.0000",
        "0.0000",
        "0.0000",
        "14958.3544",
        "0.0000"
      ],
      [
        "17",
        "3",
        "J",
        "cLCB2",
        "-",
        "-2034.4089",
        "0.0000",
        "0.0000",
        "0.0000",
        "11601.2394",
        "0.0000"
      ],
      [
        "18",
        "3",
        "J",
        "cLCB3",
        "-",
        "-2034.4089",
        "0.0000",
        "0.0000",
        "0.0000",
        "11601.2394",
        "0.0000"
      ],
      [
        "19",
        "4",
        "I",
        "cLCB1",
        "-",
        "-2034.4086",
        "0.0000",
        "-0.0000",
        "0.0000",
        "14958.3546",
        "0.0000"
      ],
      [
        "20",
        "4",
        "I",
        "cLCB2",
        "-",
        "-2034.4086",
        "0.0000",
        "-0.0000",
        "0.0000",
        "11601.2396",
        "0.0000"
      ],
      [
        "21",
        "4",
        "I",
        "cLCB3",
        "-",
        "-2034.4086",
        "0.0000",
        "-0.0000",
        "0.0000",
        "11601.2396",
        "0.0000"
      ],
      [
        "22",
        "4",
        "J",
        "cLCB1",
        "-",
        "-2092.9106",
        "0.0000",
        "665.6297",
        "0.0000",
        "13277.6914",
        "0.0000"
      ],
      [
        "23",
        "4",
        "J",
        "cLCB2",
        "-",
        "-2092.9106",
        "0.0000",
        "516.4246",
        "0.0000",
        "10293.5891",
        "0.0000"
      ],
      [
        "24",
        "4",
        "J",
        "cLCB3",
        "-",
        "-2092.9106",
        "0.0000",
        "516.4246",
        "0.0000",
        "10293.5891",
        "0.0000"
      ],
      [
        "25",
        "5",
        "I",
        "cLCB1",
        "-",
        "-2092.9106",
        "0.0000",
        "665.6297",
        "0.0000",
        "13277.6914",
        "0.0000"
      ],
      [
        "26",
        "5",
        "I",
        "cLCB2",
        "-",
        "-2092.9106",
        "0.0000",
        "516.4246",
        "0.0000",
        "10293.5891",
        "0.0000"
      ],
      [
        "27",
        "5",
        "I",
        "cLCB3",
        "-",
        "-2092.9106",
        "0.0000",
        "516.4246",
        "0.0000",
        "10293.5891",
        "0.0000"
      ],
      [
        "28",
        "5",
        "J",
        "cLCB1",
        "-",
        "-2011.7439",
        "0.0000",
        "1388.4984",
        "0.0000",
        "8207.1771",
        "0.0000"
      ],
      [
        "29",
        "5",
        "J",
        "cLCB2",
        "-",
        "-2011.7439",
        "0.0000",
        "1090.0882",
        "0.0000",
        "6342.1131",
        "0.0000"
      ],
      [
        "30",
        "5",
        "J",
        "cLCB3",
        "-",
        "-2011.7439",
        "0.0000",
        "1090.0882",
        "0.0000",
        "6342.1131",
        "0.0000"
      ],
      [
        "31",
        "6",
        "I",
        "cLCB1",
        "-",
        "-2011.7439",
        "0.0000",
        "1388.4984",
        "0.0000",
        "8207.1771",
        "0.0000"
      ],
      [
        "32",
        "6",
        "I",
        "cLCB2",
        "-",
        "-2011.7439",
        "0.0000",
        "1090.0882",
        "0.0000",
        "6342.1131",
        "0.0000"
      ],
      [
        "33",
        "6",
        "I",
        "cLCB3",
        "-",
        "-2011.7439",
        "0.0000",
        "1090.0882",
        "0.0000",
        "6342.1131",
        "0.0000"
      ],
      [
        "34",
        "6",
        "J",
        "cLCB1",
        "-",
        "-1894.4450",
        "0.0000",
        "2238.0767",
        "0.0000",
        "-567.1703",
        "0.0000"
      ],
      [
        "35",
        "6",
        "J",
        "cLCB2",
        "-",
        "-1894.4450",
        "0.0000",
        "1790.4614",
        "0.0000",
        "-567.1703",
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_DGN_FORCE"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 17. `REPORT` — Excel Report

> **기능** PSC 설계 결과를 Excel 보고서로 내보냅니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/REPORT
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738177779609](https://support.midasuser.com/hc/ko/articles/64738177779609)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Export Path | `"EXPORT_PATH"` | string |  | Optional |
| 2 | [General] Output Name | `"OUTPUT_NAME"` | string |  | Optional |

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
      "properties": {
        "EXPORT_PATH": {
          "type": "string",
          "description": "Excel report export folder path. If empty, the folder of the model file is used.",
          "default": ""
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "Excel report output file name ('.xlsx' is appended when missing). If empty, the model file name is used.",
          "default": ""
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

**Request**

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PSC_Design_Report_KDS-24-14-21-2021"
  }
}
```

**Response**

```json
{
  "SUCCESS": true,
  "RESULT": "SUCCESS",
  "CATEGORY": "NONE",
  "FILE_PATH": "C:\\MIDAS\\Report\\PSC_Design_Report_KDS-24-14-21-2021.xlsx",
  "MESSAGE": ""
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/REPORT"

payload = json.loads(r'''
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "PSC_Design_Report_KDS-24-14-21-2021"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 18. `TABLE` · `PSC_PRINCIPAL_CS` — Principal stress at a construction stage

> **기능** 시공단계별 단면의 주응력 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738149275545](https://support.midasuser.com/hc/ko/articles/64738149275545)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Principal stress at a construction stage: "PSC_PRINCIPAL_CS" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Element | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Comp./Tens. | `"COMP_TENS"` | array | - | Optional |
| 10 | [General] Girder/Slab · Girder: "Girder" · Slab: "Slab" | `"SELECTION_TYPE"` | string | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Principal stress at a construction stage - Result Table Type",
          "enum": [
            "PSC_PRINCIPAL_CS"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Tension"
            ]
          }
        },
        "SELECTION_TYPE": {
          "type": "string",
          "description": "Girder or Slab Selection",
          "enum": [
            "Girder",
            "Slab"
          ]
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `empty` — `Index`, `Elem`, `Part`, `Comp./Tens.`, `Stage`, `CHK`, `Sig_P1`, `Sig_P2`, `Sig_P3`, `Sig_P4`, `Sig_P5`, `Sig_P6`, `Sig_P7`, `Sig_P8`, `Sig_P9`, `Sig_P10`, `Sig_MAX`, `Sig_AP`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_CS"
  }
}
```

**Response**

```json
{
  "empty": {
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
        "I[1]",
        "Tension",
        "CS3_Service",
        "OK",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-861.2622",
        "-861.2622",
        "-921.6736",
        "-921.6736",
        "-682.8835",
        "-682.8835",
        "-921.6736",
        "2798.2703"
      ],
      [
        "2",
        "1",
        "J[2]",
        "Tension",
        "CS3_Service",
        "OK",
        "-0.0000",
        "-0.0000",
        "-2358.5360",
        "-2358.5360",
        "-347.8636",
        "-347.8636",
        "-497.9312",
        "-497.9312",
        "-1755.9939",
        "-1755.9939",
        "-2358.5360",
        "2798.2703"
      ],
      [
        "3",
        "2",
        "I[2]",
        "Tension",
        "CS3_Service",
        "OK",
        "-0.0000",
        "-0.0000",
        "-2358.5360",
        "-2358.5360",
        "-347.8636",
        "-347.8636",
        "-497.9312",
        "-497.9312",
        "-1755.9939",
        "-1755.9939",
        "-2358.5360",
        "2798.2703"
      ],
      [
        "4",
        "2",
        "J[3]",
        "Tension",
        "CS3_Service",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4065.0295",
        "-4065.0295",
        "-80.1918",
        "-80.1918",
        "-172.4138",
        "-172.4138",
        "-2821.0969",
        "-2821.0969",
        "-4065.0295",
        "2798.2703"
      ],
      [
        "5",
        "3",
        "I[3]",
        "Tension",
        "CS3_Service",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4065.0295",
        "-4065.0295",
        "-80.1918",
        "-80.1918",
        "-172.4138",
        "-172.4138",
        "-2821.0969",
        "-2821.0969",
        "-4065.0295",
        "2798.2703"
      ],
      [
        "6",
        "3",
        "J[4]",
        "Tension",
        "CS3_Service",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4642.5450",
        "-4642.5450",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-3212.9428",
        "-3212.9428",
        "-4642.5450",
        "2798.2703"
      ],
      [
        "7",
        "4",
        "I[4]",
        "Tension",
        "CS3_Service",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4642.5455",
        "-4642.5455",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-3212.9428",
        "-3212.9428",
        "-4642.5455",
        "2798.2703"
      ],
      [
        "8",
        "4",
        "J[5]",
        "Tension",
        "CS3_Service",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4065.0298",
        "-4065.0298",
        "-80.1918",
        "-80.1918",
        "-172.4138",
        "-172.4138",
        "-2821.0972",
        "-2821.0972",
        "-4065.0298",
        "2798.2703"
      ],
      [
        "9",
        "5",
        "I[5]",
        "Tension",
        "CS3_Service",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4065.0298",
        "-4065.0298",
        "-80.1918",
        "-80.1918",
        "-172.4138",
        "-172.4138",
        "-2821.0972",
        "-2821.0972",
        "-4065.0298",
        "2798.2703"
      ],
      [
        "10",
        "5",
        "J[6]",
        "Tension",
        "CS3_Service",
        "OK",
        "-0.0000",
        "-0.0000",
        "-2358.5360",
        "-2358.5360",
        "-347.8636",
        "-347.8636",
        "-497.9313",
        "-497.9313",
        "-1755.9939",
        "-1755.9939",
        "-2358.5360",
        "2798.2703"
      ],
      [
        "11",
        "6",
        "I[6]",
        "Tension",
        "CS3_Service",
        "OK",
        "-0.0000",
        "-0.0000",
        "-2358.5360",
        "-2358.5360",
        "-347.8636",
        "-347.8636",
        "-497.9313",
        "-497.9313",
        "-1755.9939",
        "-1755.9939",
        "-2358.5360",
        "2798.2703"
      ],
      [
        "12",
        "6",
        "J[7]",
        "Tension",
        "CS3_Service",
        "OK",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-861.2622",
        "-861.2622",
        "-921.6737",
        "-921.6737",
        "-682.8835",
        "-682.8835",
        "-921.6737",
        "2798.2703"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_CS"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 19. `TABLE` · `PSC_PRINCIPAL_SVC` — Principal stress at service loads

> **기능** 사용하중에 대한 주응력 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738170061209](https://support.midasuser.com/hc/ko/articles/64738170061209)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Principal stress at service loads: "PSC_PRINCIPAL_SVC" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Element | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Comp./Tens. | `"COMP_TENS"` | array | - | Optional |
| 10 | [General] Girder/Slab · Girder: "Girder" · Slab: "Slab" | `"SELECTION_TYPE"` | string | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Principal stress at service loads - Result Table Type",
          "enum": [
            "PSC_PRINCIPAL_SVC"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Tension"
            ]
          }
        },
        "SELECTION_TYPE": {
          "type": "string",
          "description": "Girder or Slab Selection",
          "enum": [
            "Girder",
            "Slab"
          ]
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `empty` — `Index`, `Elem`, `Part`, `Comp./Tens.`, `LComName`, `Type`, `CHK`, `Sig_P1`, `Sig_P2`, `Sig_P3`, `Sig_P4`, `Sig_P5`, `Sig_P6`, `Sig_P7`, `Sig_P8`, `Sig_P9`, `Sig_P10`, `Sig_MAX`, `Sig_AP`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_SVC"
  }
}
```

**Response**

```json
{
  "empty": {
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
        "I[1]",
        "Tension",
        "cLCB2",
        "-",
        "OK",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-858.3592",
        "-858.3592",
        "-918.5621",
        "-918.5621",
        "-679.0792",
        "-679.0792",
        "-918.5621",
        "2243.4047"
      ],
      [
        "2",
        "1",
        "J[2]",
        "Tension",
        "cLCB2",
        "-",
        "NG",
        "-0.0000",
        "-0.0000",
        "-2332.7193",
        "-2332.7193",
        "-343.7275",
        "-343.7275",
        "-490.8186",
        "-490.8186",
        "-1735.0753",
        "-1735.0753",
        "-2332.7193",
        "2243.4047"
      ],
      [
        "3",
        "2",
        "I[2]",
        "Tension",
        "cLCB2",
        "-",
        "NG",
        "-0.0000",
        "-0.0000",
        "-2332.7193",
        "-2332.7193",
        "-343.7275",
        "-343.7275",
        "-490.8186",
        "-490.8186",
        "-1735.0753",
        "-1735.0753",
        "-2332.7193",
        "2243.4047"
      ],
      [
        "4",
        "2",
        "J[3]",
        "Tension",
        "cLCB2",
        "-",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4020.8716",
        "-4020.8716",
        "-78.3762",
        "-78.3762",
        "-165.9415",
        "-165.9415",
        "-2784.7474",
        "-2784.7474",
        "-4020.8716",
        "2243.4047"
      ],
      [
        "5",
        "3",
        "I[3]",
        "Tension",
        "cLCB2",
        "-",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4020.8716",
        "-4020.8716",
        "-78.3762",
        "-78.3762",
        "-165.9415",
        "-165.9415",
        "-2784.7474",
        "-2784.7474",
        "-4020.8716",
        "2243.4047"
      ],
      [
        "6",
        "3",
        "J[4]",
        "Tension",
        "cLCB2",
        "-",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4594.4926",
        "-4594.4926",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-3173.8037",
        "-3173.8037",
        "-4594.4926",
        "2243.4047"
      ],
      [
        "7",
        "4",
        "I[4]",
        "Tension",
        "cLCB2",
        "-",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4594.4928",
        "-4594.4928",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-3173.8039",
        "-3173.8039",
        "-4594.4928",
        "2243.4047"
      ],
      [
        "8",
        "4",
        "J[5]",
        "Tension",
        "cLCB2",
        "-",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4020.8717",
        "-4020.8717",
        "-78.3762",
        "-78.3762",
        "-165.9415",
        "-165.9415",
        "-2784.7476",
        "-2784.7476",
        "-4020.8717",
        "2243.4047"
      ],
      [
        "9",
        "5",
        "I[5]",
        "Tension",
        "cLCB2",
        "-",
        "NG",
        "-0.0000",
        "-0.0000",
        "-4020.8717",
        "-4020.8717",
        "-78.3762",
        "-78.3762",
        "-165.9415",
        "-165.9415",
        "-2784.7476",
        "-2784.7476",
        "-4020.8717",
        "2243.4047"
      ],
      [
        "10",
        "5",
        "J[6]",
        "Tension",
        "cLCB2",
        "-",
        "NG",
        "-0.0000",
        "-0.0000",
        "-2332.7194",
        "-2332.7194",
        "-343.7275",
        "-343.7275",
        "-490.8187",
        "-490.8187",
        "-1735.0754",
        "-1735.0754",
        "-2332.7194",
        "2243.4047"
      ],
      [
        "11",
        "6",
        "I[6]",
        "Tension",
        "cLCB2",
        "-",
        "NG",
        "-0.0000",
        "-0.0000",
        "-2332.7194",
        "-2332.7194",
        "-343.7275",
        "-343.7275",
        "-490.8187",
        "-490.8187",
        "-1735.0754",
        "-1735.0754",
        "-2332.7194",
        "2243.4047"
      ],
      [
        "12",
        "6",
        "J[7]",
        "Tension",
        "cLCB2",
        "-",
        "OK",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-0.0000",
        "-858.3593",
        "-858.3593",
        "-918.5622",
        "-918.5622",
        "-679.0792",
        "-679.0792",
        "-918.5622",
        "2243.4047"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_SVC"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 20. `DRESULT` — PSC Result Diagram

> **기능** PSC 설계 결과 도형을 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/DRESULT
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738170139545](https://support.midasuser.com/hc/ko/articles/64738170139545)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Image File Save Path & File Name | `"EXPORT_PATH"` | string | - | Optional |
| 2 | [General] Url Name | `"URL_NAME"` | string | - | Optional |
| 3 | [General] Smart Report Image Name | `"FIGURE_NAME"` | string | - | Optional |
| 4 | [General] Image Width's Pixel Size · Minimum: 1 | `"WIDTH"` | integer | - | Optional |
| 5 | [General] Image Height's Pixel Size · Minimum: 1 | `"HEIGHT"` | integer | - | Optional |
| 6 | [General] Construction Stage Name | `"STAGE_NAME"` | string | - | Optional |
| 7 | [General] Set Mode · Pre: "PRE" · Post: "POST" | `"SET_MODE"` | string | - | Optional |
| 8 | [General] Hidden Option | `"SET_HIDDEN"` | boolean | false | Optional |
| 9 | [General] Active | `"ACTIVE"` | object | - | Optional |
| 10 | [General] Angle | `"ANGLE"` | object | - | Optional |
| 11 | [General] Display Settings | `"DISPLAY"` | object | - | Optional |
| 12 | [General] Perspective | `"PERSPECTIVE"` | boolean | false | Optional |
| 13 | [General] Zoom Level | `"ZOOM_LEVEL"` | number | 100 | Optional |
| 14 | [General] Background Color Top | `"BGCOLOR_TOP"` | object | - | Optional |
| 14.1 | └ [General] Red · Range: 0~255 | `"R"` | integer | - | **Required** |
| 14.2 | └ [General] Green · Range: 0~255 | `"G"` | integer | - | **Required** |
| 14.3 | └ [General] Blue · Range: 0~255 | `"B"` | integer | - | **Required** |
| 15 | [General] Background Color Bottom | `"BGCOLOR_BOTTOM"` | object | - | Optional |
| 15.1 | └ [General] Red · Range: 0~255 | `"R"` | integer | - | **Required** |
| 15.2 | └ [General] Green · Range: 0~255 | `"G"` | integer | - | **Required** |
| 15.3 | └ [General] Blue · Range: 0~255 | `"B"` | integer | - | **Required** |
| 16 | [General] Result Graphic | `"RESULT_GRAPHIC"` ¹⁾ | object | - | Optional |

**Result Graphic ¹⁾**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Current Mode · PSC Result Diagram: "PSC_DESIGN_DIAGRAM" | `"CURRENT_MODE"` | string | PSC_DESIGN_DIAGRAM | **Required** |
| 2 | Components | `"COMPONENTS"` | object | - | Optional |
| 2.1 | └ Components · Flexure-y: "FLEXURE_Y" · Shear: "SHEAR" · Torsion (Vmx): "TORSION_VMAX" · Torsion (Tmx): "TORSION_TMAX" | `"COMP"` | string | FLEXURE_Y | Optional |
| 2.2 | └ Option · Force: "FORCE" · Safety Factor: "SAFETY_FACTOR" | `"CRITERIA"` | string | FORCE | Optional |
| 2.3 | └ Criteria Line · Minimum: 0 | `"CRITERIA_LINE"` | number | 1 | Optional |
| 2.4 | └ Positive/Negative | `"SIGN"` | object | - | Optional |
| 2.4.1 | 　　└ Positive | `"MAX"` | boolean | true | Optional |
| 2.4.2 | 　　└ Negative | `"MIN"` | boolean | true | Optional |
| 2.5 | └ Ultimate Force/Criteria Diagram. | `"RESISTANCE_LINE"` | object | - | Optional |
| 2.5.1 | 　　└ Color | `"COLOR"` | object | - | Optional |
| 2.5.1.1 | 　　　　└ Red · Range: 0~255 | `"R"` | integer | - | **Required** |
| 2.5.1.2 | 　　　　└ Green · Range: 0~255 | `"G"` | integer | - | **Required** |
| 2.5.1.3 | 　　　　└ Blue · Range: 0~255 | `"B"` | integer | - | **Required** |
| 2.5.2 | 　　└ Thick. · Range: 0~20 | `"THICKNESS"` | integer | 1 | Optional |
| 2.6 | └ Diagram Option | `"DIAGRAM"` | object | - | Optional |
| 2.6.1 | 　　└ Scale Factor · Minimum: 0 | `"SCALE_FACTOR"` | number | 1 | Optional |
| 2.6.2 | 　　└ Fill Type · No: "NONE" · Line: "LINE" · Solid: "SOLID" | `"FILL"` | string | LINE | Optional |
| 2.6.3 | 　　└ Direction | `"DIRECTION"` | object | - | Optional |
| 2.6.3.1 | 　　　　└ Direction · Global: "GLOBAL" · Local: "LOCAL" | `"TYPE"` | string | LOCAL | Optional |
| 2.6.3.2 | 　　　　└ [When TYPE = "Global"] Axis · X Axis: "X" · Y Axis: "Y" · Z Axis: "Z" | `"AXIS"` | string | MAJOR | **Required** |
| 3 | Type of Display | `"TYPE_OF_DISPLAY"` | object | - | Optional |
| 3.1 | └ Contour | `"CONTOUR"` | object | - | Optional |
| 3.1.1 | 　　└ Contour | `"OPT_CHECK"` | boolean | true | Optional |
| 3.2 | └ Legend | `"LEGEND"` | object | - | Optional |
| 3.2.1 | 　　└ Legend | `"OPT_CHECK"` | boolean | true | Optional |
| 3.3 | └ Values | `"VALUES"` | object | - | Optional |
| 3.3.1 | 　　└ Values | `"OPT_CHECK"` | boolean | false | Optional |
| 3.3.2 | 　　└ Decimal Points · Minimum: 0 | `"DECIMAL_PT"` | integer | 0 | Optional |
| 3.3.3 | 　　└ Value Exp. | `"VALUE_EXP"` | boolean | false | Optional |
| 4 | Value Output Location | `"OUTPUT_SECT_LOCATION"` | object | - | Optional |
| 4.1 | └ I | `"OPT_I"` | boolean | false | Optional |
| 4.2 | └ Center | `"OPT_CENTER_MID"` | boolean | false | Optional |
| 4.3 | └ J | `"OPT_J"` | boolean | false | Optional |
| 4.4 | └ Abs Max / Min/Max / All · Abs Max: "Abs Max" · Min/Max: "Min/Max" · All: "All" | `"OPT_MAX_MINMAX_ALL"` | string | - | Optional |

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
      "properties": {
        "EXPORT_PATH": {
          "type": "string",
          "description": "Image file save path and file name"
        },
        "URL_NAME": {
          "type": "string",
          "description": "Temporary image name (base64 return)"
        },
        "FIGURE_NAME": {
          "type": "string",
          "description": "Smart report image name"
        },
        "WIDTH": {
          "type": "integer",
          "description": "Image width in pixels",
          "minimum": 1
        },
        "HEIGHT": {
          "type": "integer",
          "description": "Image height in pixels",
          "minimum": 1
        },
        "STAGE_NAME": {
          "type": "string",
          "description": "Construction stage name"
        },
        "SET_MODE": {
          "type": "string",
          "description": "Set mode option",
          "enum": [
            "PRE",
            "POST"
          ]
        },
        "SET_HIDDEN": {
          "type": "boolean",
          "description": "Hidden option",
          "default": false
        },
        "ACTIVE": {
          "type": "object",
          "description": "View/Active settings"
        },
        "ANGLE": {
          "type": "object",
          "description": "View/Angle settings"
        },
        "DISPLAY": {
          "type": "object",
          "description": "View/Display settings"
        },
        "PERSPECTIVE": {
          "type": "boolean",
          "description": "Enable perspective view",
          "default": false
        },
        "ZOOM_LEVEL": {
          "type": "number",
          "description": "Zoom level",
          "default": 100
        },
        "BGCOLOR_TOP": {
          "type": "object",
          "description": "Background color top",
          "additionalProperties": false,
          "required": [
            "R",
            "G",
            "B"
          ],
          "properties": {
            "R": {
              "type": "integer",
              "minimum": 0,
              "maximum": 255
            },
            "G": {
              "type": "integer",
              "minimum": 0,
              "maximum": 255
            },
            "B": {
              "type": "integer",
              "minimum": 0,
              "maximum": 255
            }
          }
        },
        "BGCOLOR_BOTTOM": {
          "type": "object",
          "description": "Background color bottom",
          "additionalProperties": false,
          "required": [
            "R",
            "G",
            "B"
          ],
          "properties": {
            "R": {
              "type": "integer",
              "minimum": 0,
              "maximum": 255
            },
            "G": {
              "type": "integer",
              "minimum": 0,
              "maximum": 255
            },
            "B": {
              "type": "integer",
              "minimum": 0,
              "maximum": 255
            }
          }
        },
        "RESULT_GRAPHIC": {
          "type": "object",
          "description": "PSC Result Diagram settings",
          "required": [
            "CURRENT_MODE"
          ],
          "additionalProperties": false,
          "properties": {
            "CURRENT_MODE": {
              "type": "string",
              "description": "Current result mode",
              "default": "PSC_DESIGN_DIAGRAM",
              "enum": [
                "PSC_DESIGN_DIAGRAM"
              ]
            },
            "COMPONENTS": {
              "type": "object",
              "description": "Components of the PSC design diagram (flat: COMP, CRITERIA ... directly under COMPONENTS)",
              "additionalProperties": false,
              "properties": {
                "COMP": {
                  "type": "string",
                  "default": "FLEXURE_Y",
                  "enum": [
                    "FLEXURE_Y",
                    "SHEAR",
                    "TORSION_VMAX",
                    "TORSION_TMAX"
                  ]
                },
                "CRITERIA": {
                  "type": "string",
                  "default": "FORCE",
                  "enum": [
                    "FORCE",
                    "SAFETY_FACTOR"
                  ]
                },
                "CRITERIA_LINE": {
                  "type": "number",
                  "exclusiveMinimum": 0,
                  "default": 1
                },
                "SIGN": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "MAX": {
                      "type": "boolean",
                      "default": true
                    },
                    "MIN": {
                      "type": "boolean",
                      "default": true
                    }
                  }
                },
                "RESISTANCE_LINE": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "COLOR": {
                      "type": "object",
                      "description": "Ultimate force / criteria line color",
                      "additionalProperties": false,
                      "required": [
                        "R",
                        "G",
                        "B"
                      ],
                      "properties": {
                        "R": {
                          "type": "integer",
                          "minimum": 0,
                          "maximum": 255
                        },
                        "G": {
                          "type": "integer",
                          "minimum": 0,
                          "maximum": 255
                        },
                        "B": {
                          "type": "integer",
                          "minimum": 0,
                          "maximum": 255
                        }
                      }
                    },
                    "THICKNESS": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 20,
                      "default": 1
                    }
                  }
                },
                "DIAGRAM": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "SCALE_FACTOR": {
                      "type": "number",
                      "exclusiveMinimum": 0,
                      "default": 1
                    },
                    "FILL": {
                      "type": "string",
                      "default": "LINE",
                      "enum": [
                        "NONE",
                        "LINE",
                        "SOLID"
                      ]
                    },
                    "DIRECTION": {
                      "type": "object",
                      "additionalProperties": false,
                      "properties": {
                        "TYPE": {
                          "type": "string",
                          "default": "LOCAL",
                          "enum": [
                            "GLOBAL",
                            "LOCAL"
                          ]
                        },
                        "AXIS": {
                          "type": "string",
                          "default": "MAJOR",
                          "enum": [
                            "X",
                            "Y",
                            "Z",
                            "MAJOR",
                            "MINOR"
                          ]
                        }
                      }
                    }
                  }
                }
              }
            },
            "TYPE_OF_DISPLAY": {
              "type": "object",
              "description": "Type of display",
              "additionalProperties": false,
              "properties": {
                "CONTOUR": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "OPT_CHECK": {
                      "type": "boolean",
                      "default": true
                    }
                  }
                },
                "LEGEND": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "OPT_CHECK": {
                      "type": "boolean",
                      "default": true
                    }
                  }
                },
                "VALUES": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "OPT_CHECK": {
                      "type": "boolean",
                      "default": false
                    },
                    "DECIMAL_PT": {
                      "type": "integer",
                      "minimum": 0,
                      "default": 0
                    },
                    "VALUE_EXP": {
                      "type": "boolean",
                      "default": false
                    }
                  }
                }
              }
            },
            "OUTPUT_SECT_LOCATION": {
              "type": "object",
              "description": "Value output location",
              "additionalProperties": false,
              "properties": {
                "OPT_I": {
                  "type": "boolean",
                  "default": false
                },
                "OPT_CENTER_MID": {
                  "type": "boolean",
                  "default": false
                },
                "OPT_J": {
                  "type": "boolean",
                  "default": false
                },
                "OPT_MAX_MINMAX_ALL": {
                  "type": "string",
                  "enum": [
                    "Abs Max",
                    "Min/Max",
                    "All"
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
```

### Response HEAD

공식 응답 예제의 최상위 Key입니다.

- `base64String`

### Request / Response JSON

**Request**

```json
{
  "Argument": {}
}
```

**Response**

```json
{
  "base64String": "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/...(JPEG, base64)"
}
```

### Python 예제

```python
import json
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/DRESULT"

payload = json.loads(r'''
{
  "Argument": {}
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 21. `DIDP-VBEAM` — Design Position - Virtual Beam

> **기능** 가상보의 PSC 설계 위치를 지정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/DIDP-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738161973017](https://support.midasuser.com/hc/ko/articles/64738161973017)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a virtual beam ID string (e.g., "1"). Element Type = Virtual Beam of the Position for PSC Design panel (shown only in virtual-beam mode). Elements use /DESIGN/PSC/KDS-24-14-21-2021/DIDP | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Moment Resistance · None: 0 · I: 1 · J: 2 · I & J: 3 | `"MOMENT_TYPE"` | integer | 3 | **Required** |
| 2 | [General] Shear Resistance · None: 0 · I: 1 · J: 2 · I & J: 3 | `"SHEAR_TYPE"` | integer | 3 | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a virtual beam ID string (e.g., \"1\"). Element Type = Virtual Beam of the Position for PSC Design panel (shown only in virtual-beam mode). Elements use /DESIGN/PSC/KDS-24-14-21-2021/DIDP",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Position for PSC Design - Virtual Beam",
          "type": "object",
          "required": [
            "MOMENT_TYPE",
            "SHEAR_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "MOMENT_TYPE": {
              "type": "integer",
              "description": "Ends checked for moment resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
              "default": 3,
              "enum": [
                0,
                1,
                2,
                3
              ]
            },
            "SHEAR_TYPE": {
              "type": "integer",
              "description": "Ends checked for shear resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
              "default": 3,
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
      "MOMENT_TYPE": 3,
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
      "MOMENT_TYPE": 3,
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/DIDP-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "201": {
      "MOMENT_TYPE": 3,
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

## 22. `PESC-VBEAM` — Exposure Class - Virtual Beam

> **기능** 가상보의 노출등급을 설정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/PESC-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738170322969](https://support.midasuser.com/hc/ko/articles/64738170322969)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a virtual beam number (e.g., "1"). Element Type = Virtual Beam of the panel (shown when the model has a virtual section for design, KDS 24 14 21 : 2021 only). Elements use /DESIGN/PSC/KDS-24-14-21-2021/PESC | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Both end parts(i & j) have the same Exposure Class | `"BOTH_ENDS"` | boolean | true | Optional |
| 2 | [General] I | `"I"` | object | - | Optional |
| 2.1 | └ [General] Top · EC1 · EC2 · EC3 · EC4 · ED1 · ED2 · ED3 · ES1 · ES2 · ES3 | `"TOP"` | string | EC1 | Optional |
| 2.2 | └ [General] Bottom · EC1 · EC2 · EC3 · EC4 · ED1 · ED2 · ED3 · ES1 · ES2 · ES3 | `"BOTTOM"` | string | EC1 | Optional |
| 3 | [General] J | `"J"` | object | - | Optional |
| 3.1 | └ [General] Top · EC1 · EC2 · EC3 · EC4 · ED1 · ED2 · ED3 · ES1 · ES2 · ES3 | `"TOP"` | string | EC1 | Optional |
| 3.2 | └ [General] Bottom · EC1 · EC2 · EC3 · EC4 · ED1 · ED2 · ED3 · ES1 · ES2 · ES3 | `"BOTTOM"` | string | EC1 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a virtual beam number (e.g., \"1\"). Element Type = Virtual Beam of the panel (shown when the model has a virtual section for design, KDS 24 14 21 : 2021 only). Elements use /DESIGN/PSC/KDS-24-14-21-2021/PESC",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Exposure Class (Virtual Beam)",
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "BOTH_ENDS": {
              "type": "boolean",
              "description": "Both end parts (i & j) have the same Exposure Class. true: the I-end classes are stored for the J end as well; J must then be omitted or equal to I (otherwise rejected). Omitted on PUT: the stored value is kept",
              "default": true
            },
            "I": {
              "type": "object",
              "description": "Exposure classes at the I end (tab I). Omitted members keep the stored values on PUT",
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "string",
                  "description": "Exposure class of the top face at the I end (KDS 24 14 21 : 2021 classes EC1-EC4, ED1-ED3, ES1-ES3)",
                  "enum": [
                    "EC1",
                    "EC2",
                    "EC3",
                    "EC4",
                    "ED1",
                    "ED2",
                    "ED3",
                    "ES1",
                    "ES2",
                    "ES3"
                  ],
                  "default": "EC1"
                },
                "BOTTOM": {
                  "type": "string",
                  "description": "Exposure class of the bottom face at the I end (KDS 24 14 21 : 2021 classes EC1-EC4, ED1-ED3, ES1-ES3)",
                  "enum": [
                    "EC1",
                    "EC2",
                    "EC3",
                    "EC4",
                    "ED1",
                    "ED2",
                    "ED3",
                    "ES1",
                    "ES2",
                    "ES3"
                  ],
                  "default": "EC1"
                }
              }
            },
            "J": {
              "type": "object",
              "description": "Exposure classes at the J end (tab J). Used when BOTH_ENDS is false; with BOTH_ENDS true it must be omitted or equal to I",
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "string",
                  "description": "Exposure class of the top face at the J end (KDS 24 14 21 : 2021 classes EC1-EC4, ED1-ED3, ES1-ES3)",
                  "enum": [
                    "EC1",
                    "EC2",
                    "EC3",
                    "EC4",
                    "ED1",
                    "ED2",
                    "ED3",
                    "ES1",
                    "ES2",
                    "ES3"
                  ],
                  "default": "EC1"
                },
                "BOTTOM": {
                  "type": "string",
                  "description": "Exposure class of the bottom face at the J end (KDS 24 14 21 : 2021 classes EC1-EC4, ED1-ED3, ES1-ES3)",
                  "enum": [
                    "EC1",
                    "EC2",
                    "EC3",
                    "EC4",
                    "ED1",
                    "ED2",
                    "ED3",
                    "ES1",
                    "ES2",
                    "ES3"
                  ],
                  "default": "EC1"
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

- `PESC`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "201": {
      "I": {
        "TOP": "EC3",
        "BOTTOM": "EC2"
      }
    }
  }
}
```

**Response**

```json
{
  "PESC": {
    "201": {
      "I": {
        "TOP": "EC3",
        "BOTTOM": "EC2"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/PESC-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "201": {
      "I": {
        "TOP": "EC3",
        "BOTTOM": "EC2"
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

## 23. `DIOP-VBEAM` — Output Position - Virtual Beam

> **기능** 가상보의 PSC 설계 결과 출력 위치를 지정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/DIOP-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738170410649](https://support.midasuser.com/hc/ko/articles/64738170410649)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a virtual beam ID string (e.g., "1"). Element Type = Virtual Beam of the Position for PSC Output panel (shown only in virtual-beam mode). Elements use /DESIGN/PSC/KDS-24-14-21-2021/DIOP | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Moment Resistance | `"MOMENT_STRENGTH"` | object | - | **Required** |
| 1.1 | └ [General] Positive Moment · None: 0 · I: 1 · J: 2 · I & J: 3 | `"POSITIVE_MOMENT"` | integer | 3 | **Required** |
| 1.2 | └ [General] Negative Moment · None: 0 · I: 1 · J: 2 · I & J: 3 | `"NEGATIVE_MOMENT"` | integer | 3 | **Required** |
| 2 | [General] Shear Resistance · None: 0 · I: 1 · J: 2 · I & J: 3 | `"SHEAR_TYPE"` | integer | 3 | **Required** |
| 3 | [General] Torsional Resistance · None: 0 · I: 1 · J: 2 · I & J: 3 | `"TORSION_TYPE"` | integer | 3 | **Required** |

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
      "description": "Keyed object (dictionary). Each property name is a virtual beam ID string (e.g., \"1\"). Element Type = Virtual Beam of the Position for PSC Output panel (shown only in virtual-beam mode). Elements use /DESIGN/PSC/KDS-24-14-21-2021/DIOP",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Position for PSC Output - Virtual Beam",
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
              "description": "Output positions for moment resistance, positive and negative moment",
              "required": [
                "POSITIVE_MOMENT",
                "NEGATIVE_MOMENT"
              ],
              "additionalProperties": false,
              "properties": {
                "POSITIVE_MOMENT": {
                  "type": "integer",
                  "description": "Ends output for positive moment resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
                  "default": 3,
                  "enum": [
                    0,
                    1,
                    2,
                    3
                  ]
                },
                "NEGATIVE_MOMENT": {
                  "type": "integer",
                  "description": "Ends output for negative moment resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
                  "default": 3,
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
              "description": "Ends output for shear resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
              "default": 3,
              "enum": [
                0,
                1,
                2,
                3
              ]
            },
            "TORSION_TYPE": {
              "type": "integer",
              "description": "Ends output for torsional resistance. 0 = None, 1 = end I, 2 = end J, 3 = both ends (I & J). Other values are rejected",
              "default": 3,
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
    "201": {
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      },
      "SHEAR_TYPE": 3,
      "TORSION_TYPE": 3
    }
  }
}
```

**Response**

```json
{
  "DIOP": {
    "201": {
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      },
      "SHEAR_TYPE": 3,
      "TORSION_TYPE": 3
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/DIOP-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "201": {
      "MOMENT_STRENGTH": {
        "POSITIVE_MOMENT": 3,
        "NEGATIVE_MOMENT": 3
      },
      "SHEAR_TYPE": 3,
      "TORSION_TYPE": 3
    }
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 24. `PSCN-VBEAM` — Shear Connector - Virtual Beam

> **기능** 가상보의 전단연결재 정보를 설정합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/PSCN-VBEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### Specifications

**원문** [한국어 64738170475289](https://support.midasuser.com/hc/ko/articles/64738170475289)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Keyed object (dictionary). Each property name is a virtual beam number (e.g., "1"). Element Type = Virtual Beam of the panel (shown when the model has a virtual section for design, KDS 24 14 21 : 2021 only). Elements use /DESIGN/PSC/KDS-24-14-21-2021/PSCN | `"Assign"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Both end parts(i & j) have the same shear connector | `"BOTH_ENDS"` | boolean | true | Optional |
| 2 | [General] I | `"I"` | object | - | Optional |
| 2.1 | └ [General] Surface Classification(cl.6.2.5) · Very Smooth: "VERY SMOOTH" · Smooth: "SMOOTH" · Rough: "ROUGH" · Indented: "INDENTED" | `"SURFACE_CLASS"` | string | VERY SMOOTH | Optional |
| 2.2 | └ [General] Angle · Range: 0~90 | `"ANGLE"` | number | 0 | Optional |
| 2.3 | └ [General] As · Minimum: 0 | `"AREA"` | number | 0 | Optional |
| 2.4 | └ [General] Fy · Minimum: 0 | `"FY"` | number | 0 | Optional |
| 3 | [General] J | `"J"` | object | - | Optional |
| 3.1 | └ [General] Surface Classification(cl.6.2.5) · Very Smooth: "VERY SMOOTH" · Smooth: "SMOOTH" · Rough: "ROUGH" · Indented: "INDENTED" | `"SURFACE_CLASS"` | string | VERY SMOOTH | Optional |
| 3.2 | └ [General] Angle · Range: 0~90 | `"ANGLE"` | number | 0 | Optional |
| 3.3 | └ [General] As · Minimum: 0 | `"AREA"` | number | 0 | Optional |
| 3.4 | └ [General] Fy · Minimum: 0 | `"FY"` | number | 0 | Optional |

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
      "description": "Keyed object (dictionary). Each property name is a virtual beam number (e.g., \"1\"). Element Type = Virtual Beam of the panel (shown when the model has a virtual section for design, KDS 24 14 21 : 2021 only). Elements use /DESIGN/PSC/KDS-24-14-21-2021/PSCN",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "title": "Shear Connector (Virtual Beam)",
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "BOTH_ENDS": {
              "type": "boolean",
              "description": "Both end parts (i & j) have the same shear connector. true: the I-end values are stored for the J end as well; J must then be omitted or equal to I (otherwise rejected). Omitted on PUT: the stored value is kept",
              "default": true
            },
            "I": {
              "type": "object",
              "description": "Shear connector at the I end (tab I). Omitted members keep the stored values on PUT",
              "additionalProperties": false,
              "properties": {
                "SURFACE_CLASS": {
                  "type": "string",
                  "description": "Surface classification of the interface at the I end",
                  "enum": [
                    "VERY SMOOTH",
                    "SMOOTH",
                    "ROUGH",
                    "INDENTED"
                  ],
                  "default": "VERY SMOOTH"
                },
                "ANGLE": {
                  "type": "number",
                  "description": "Angle of the shear connector at the I end [deg], 0 to 90",
                  "default": 0,
                  "minimum": 0,
                  "maximum": 90
                },
                "AREA": {
                  "type": "number",
                  "description": "Area of the shear connector As at the I end, in the model area unit (>= 0)",
                  "default": 0,
                  "minimum": 0
                },
                "FY": {
                  "type": "number",
                  "description": "Yield strength of the shear connector Fy at the I end, in the model stress unit (>= 0)",
                  "default": 0,
                  "minimum": 0
                }
              }
            },
            "J": {
              "type": "object",
              "description": "Shear connector at the J end (tab J). Used when BOTH_ENDS is false; with BOTH_ENDS true it must be omitted or equal to I",
              "additionalProperties": false,
              "properties": {
                "SURFACE_CLASS": {
                  "type": "string",
                  "description": "Surface classification of the interface at the J end",
                  "enum": [
                    "VERY SMOOTH",
                    "SMOOTH",
                    "ROUGH",
                    "INDENTED"
                  ],
                  "default": "VERY SMOOTH"
                },
                "ANGLE": {
                  "type": "number",
                  "description": "Angle of the shear connector at the J end [deg], 0 to 90",
                  "default": 0,
                  "minimum": 0,
                  "maximum": 90
                },
                "AREA": {
                  "type": "number",
                  "description": "Area of the shear connector As at the J end, in the model area unit (>= 0)",
                  "default": 0,
                  "minimum": 0
                },
                "FY": {
                  "type": "number",
                  "description": "Yield strength of the shear connector Fy at the J end, in the model stress unit (>= 0)",
                  "default": 0,
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

- `PSCN`

### Request / Response JSON

**Request**

```json
{
  "Assign": {
    "201": {
      "I": {
        "SURFACE_CLASS": "ROUGH",
        "ANGLE": 90.0,
        "AREA": 0.0004,
        "FY": 400000.0
      }
    }
  }
}
```

**Response**

```json
{
  "PSCN": {
    "201": {
      "I": {
        "SURFACE_CLASS": "ROUGH",
        "ANGLE": 90,
        "AREA": 0.0004,
        "FY": 400000
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/PSCN-VBEAM"

payload = json.loads(r'''
{
  "Assign": {
    "201": {
      "I": {
        "SURFACE_CLASS": "ROUGH",
        "ANGLE": 90.0,
        "AREA": 0.0004,
        "FY": 400000.0
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

## 25. `TABLE` · `PSC_SHEAR_TORSION_VBEAM` — Check Combined Shear and Torsion Strength - Virtual Beam

> **기능** 가상보의 전단과 비틀림의 조합 강도 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738178557849](https://support.midasuser.com/hc/ko/articles/64738178557849)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Shear and Torsion Strength - Virtual Beam: "PSC_SHEAR_TORSION_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Virtual Beam | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Max/Min | `"MAX_MIN"` | array | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check Combined Shear and Torsion Strength - Virtual Beam - Result Table Type",
          "enum": [
            "PSC_SHEAR_TORSION_VBEAM"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "VirtualBeam",
              "Part",
              "Max/Min",
              "LComName",
              "DesignSituations",
              "Type",
              "CHK",
              "Tu",
              "Td,max",
              "Vu",
              "Vd,max",
              "Ratio",
              "Asl",
              "Asl,req",
              "s",
              "sl,max",
              "rho_st",
              "rho_st,min"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "MAX_MIN": {
          "type": "array",
          "description": "V-Max, V-Min or T-Max Rows (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "V-Max",
              "V-Min",
              "T-Max"
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

- `empty` — `Index`, `VirtualBeam`, `Part`, `Max/Min`, `LComName`, `DesignSituations`, `Type`, `CHK`, `Tu`, `Td,max`, `Vu`, `Vd,max`, `Ratio`, `Asl`, `Asl,req`, `s`, `sl,max`, `rho_st`, `rho_st,min`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_SHEAR_TORSION_VBEAM"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "VirtualBeam",
      "Part",
      "Max/Min",
      "LComName",
      "DesignSituations",
      "Type",
      "CHK",
      "Tu",
      "Td,max",
      "Vu",
      "Vd,max",
      "Ratio",
      "Asl",
      "Asl,req",
      "s",
      "sl,max",
      "rho_st",
      "rho_st,min"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "3807.9488",
        "-743.1485",
        "3863.0924",
        "0.0370",
        "0.0000",
        "0.0000",
        "0.0000",
        "2.0235",
        "0.0000",
        "0.0013"
      ],
      [
        "2",
        "201",
        "I",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "3807.9488",
        "-743.1485",
        "3863.0924",
        "0.0370",
        "0.0000",
        "0.0000",
        "0.0000",
        "2.0235",
        "0.0000",
        "0.0013"
      ],
      [
        "3",
        "201",
        "I",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "3807.9488",
        "-743.1485",
        "3863.0924",
        "0.0370",
        "0.0000",
        "0.0000",
        "0.0000",
        "2.0235",
        "0.0000",
        "0.0013"
      ],
      [
        "4",
        "201",
        "J",
        "T-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "-0.0000",
        "3807.9487",
        "743.1486",
        "4796.6226",
        "0.0240",
        "0.0000",
        "0.0000",
        "0.0000",
        "2.0235",
        "0.0000",
        "0.0013"
      ],
      [
        "5",
        "201",
        "J",
        "V-Max",
        "cLCB1",
        "-",
        "-",
        "NG",
        "-0.0000",
        "3807.9487",
        "743.1486",
        "4796.6226",
        "0.0240",
        "0.0000",
        "0.0000",
        "0.0000",
        "2.0235",
        "0.0000",
        "0.0013"
      ],
      [
        "6",
        "201",
        "J",
        "V-Min",
        "cLCB1",
        "-",
        "-",
        "NG",
        "-0.0000",
        "3807.9487",
        "743.1486",
        "4796.6226",
        "0.0240",
        "0.0000",
        "0.0000",
        "0.0000",
        "2.0235",
        "0.0000",
        "0.0013"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_SHEAR_TORSION_VBEAM"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 26. `TABLE` · `PSC_CRACK_WIDTH_VBEAM` — Check crack width at service loads - Virtual Beam

> **기능** 가상보의 사용하중에 대한 균열폭 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738187199001](https://support.midasuser.com/hc/ko/articles/64738187199001)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Crack width at service - Virtual Beam: "PSC_CRACK_WIDTH_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Virtual Beam | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Top/Bottom | `"TOP_BOT"` | array | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check crack width at service loads - Virtual Beam - Result Table Type",
          "enum": [
            "PSC_CRACK_WIDTH_VBEAM"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "VirtualBeam",
              "Part",
              "Top/Bottom",
              "LComName",
              "ServiceabilityLoadType",
              "Type",
              "CHK",
              "N_Ed",
              "M_Ed",
              "S_r,max",
              "Ep_sm-Ep_cm",
              "Wk",
              "Wmax",
              "As",
              "As,min"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "TOP_BOT": {
          "type": "array",
          "description": "Top or Bottom Fiber (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Top",
              "Bottom"
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

- `empty` — `Index`, `VirtualBeam`, `Part`, `Top/Bottom`, `LComName`, `ServiceabilityLoadType`, `Type`, `CHK`, `N_Ed`, `M_Ed`, `S_r,max`, `Ep_sm-Ep_cm`, `Wk`, `Wmax`, `As`, `As,min`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_CRACK_WIDTH_VBEAM"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "VirtualBeam",
      "Part",
      "Top/Bottom",
      "LComName",
      "ServiceabilityLoadType",
      "Type",
      "CHK",
      "N_Ed",
      "M_Ed",
      "S_r,max",
      "Ep_sm-Ep_cm",
      "Wk",
      "Wmax",
      "As",
      "As,min"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "Bottom",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2011.7441",
        "2779.3165",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "2",
        "201",
        "I",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2011.7441",
        "2779.3165",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "3",
        "201",
        "J",
        "Bottom",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2011.7439",
        "2779.3167",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "4",
        "201",
        "J",
        "Top",
        "cLCB2",
        "사용하중조합I",
        "-",
        "OK",
        "-2011.7439",
        "2779.3167",
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_CRACK_WIDTH_VBEAM"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 27. `TABLE` · `PSC_FLEXURE_VBEAM` — Check Flexure Strength - Virtual Beam

> **기능** 가상보의 휨강도 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738187255065](https://support.midasuser.com/hc/ko/articles/64738187255065)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Flexure Strength - Virtual Beam: "PSC_FLEXURE_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Virtual Beam | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Positive/Negative | `"POS_NEG"` | array | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check Flexure Strength - Virtual Beam - Result Table Type",
          "enum": [
            "PSC_FLEXURE_VBEAM"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "VirtualBeam",
              "Part",
              "Positive/Negative",
              "LComName",
              "DesignSituations",
              "Type",
              "CHK",
              "Mu",
              "Md",
              "Mu/Md",
              "c,max",
              "c",
              "As,max",
              "As,min",
              "As"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "POS_NEG": {
          "type": "array",
          "description": "Positive or Negative Moment (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Positive",
              "Negative"
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

- `empty` — `Index`, `VirtualBeam`, `Part`, `Positive/Negative`, `LComName`, `DesignSituations`, `Type`, `CHK`, `Mu`, `Md`, `Mu/Md`, `c,max`, `c`, `As,max`, `As,min`, `As`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_FLEXURE_VBEAM"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "VirtualBeam",
      "Part",
      "Positive/Negative",
      "LComName",
      "DesignSituations",
      "Type",
      "CHK",
      "Mu",
      "Md",
      "Mu/Md",
      "c,max",
      "c",
      "As,max",
      "As,min",
      "As"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "2587.4232",
        "0.0000",
        "1.0792",
        "0.0830",
        "0.0367",
        "0.0032",
        "0.0000"
      ],
      [
        "2",
        "201",
        "I",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "3964.3236",
        "4775.6684",
        "0.8301",
        "1.0792",
        "0.0789",
        "0.0367",
        "0.0036",
        "0.0000"
      ],
      [
        "3",
        "201",
        "J",
        "Negative",
        "cLCB1",
        "-",
        "-",
        "NG",
        "0.0000",
        "1433.3658",
        "0.0000",
        "1.0792",
        "0.0830",
        "0.0367",
        "0.0032",
        "0.0000"
      ],
      [
        "4",
        "201",
        "J",
        "Positive",
        "cLCB1",
        "-",
        "-",
        "NG",
        "3964.3239",
        "5929.7258",
        "0.6686",
        "1.0792",
        "0.0789",
        "0.0367",
        "0.0036",
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_FLEXURE_VBEAM"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 28. `TABLE` · `PSC_SHEAR_VBEAM` — Check Shear Strength - Virtual Beam

> **기능** 가상보의 전단강도 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738150120729](https://support.midasuser.com/hc/ko/articles/64738150120729)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Shear Strength - Virtual Beam: "PSC_SHEAR_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Virtual Beam | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Max/Min | `"MAX_MIN"` | array | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check Shear Strength - Virtual Beam - Result Table Type",
          "enum": [
            "PSC_SHEAR_VBEAM"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "VirtualBeam",
              "Part",
              "Max/Min",
              "LComName",
              "DesignSituations",
              "Type",
              "CHK",
              "Vu",
              "Vd",
              "Vu/Vd",
              "rho_v",
              "rho_v,min",
              "s",
              "s,max"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "MAX_MIN": {
          "type": "array",
          "description": "Maximum or Minimum Shear (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Max",
              "Min"
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

- `empty` — `Index`, `VirtualBeam`, `Part`, `Max/Min`, `LComName`, `DesignSituations`, `Type`, `CHK`, `Vu`, `Vd`, `Vu/Vd`, `rho_v`, `rho_v,min`, `s`, `s,max`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_SHEAR_VBEAM"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "VirtualBeam",
      "Part",
      "Max/Min",
      "LComName",
      "DesignSituations",
      "Type",
      "CHK",
      "Vu",
      "Vd",
      "Vu/Vd",
      "rho_v",
      "rho_v,min",
      "s",
      "s,max"
    ],
    "DATA": [
      [
        "1",
        "201",
        "I",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-743.1485",
        "1516.1662",
        "0.4901",
        "0.0000",
        "0.0013",
        "0.0000",
        "2.0235"
      ],
      [
        "2",
        "201",
        "I",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "-743.1485",
        "1516.1662",
        "0.4901",
        "0.0000",
        "0.0013",
        "0.0000",
        "2.0235"
      ],
      [
        "3",
        "201",
        "J",
        "Max",
        "cLCB1",
        "-",
        "-",
        "OK",
        "743.1486",
        "1447.5270",
        "0.5134",
        "0.0000",
        "0.0013",
        "0.0000",
        "2.0235"
      ],
      [
        "4",
        "201",
        "J",
        "Min",
        "cLCB1",
        "-",
        "-",
        "OK",
        "743.1486",
        "1447.5270",
        "0.5134",
        "0.0000",
        "0.0013",
        "0.0000",
        "2.0235"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_SHEAR_VBEAM"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 29. `TABLE` · `PSC_STRESS_SERVICE_VBEAM` — Check stress for cross section at service loads - Virtual Beam

> **기능** 가상보의 사용하중에 대한 단면 응력 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738157757465](https://support.midasuser.com/hc/ko/articles/64738157757465)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Principal stress at CS - Virtual Beam: "PSC_STRESS_SERVICE_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Virtual Beam | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Comp./Tens. | `"COMP_TENS"` | array | - | Optional |
| 10 | [General] Girder/Slab · Girder: "Girder" · Slab: "Slab" | `"SELECTION_TYPE"` | string | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check stress for cross section at service loads - Virtual Beam - Result Table Type",
          "enum": [
            "PSC_STRESS_SERVICE_VBEAM"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "VirtualBeam",
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
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Compression",
              "Tension"
            ]
          }
        },
        "SELECTION_TYPE": {
          "type": "string",
          "description": "Girder or Slab Selection",
          "enum": [
            "Girder",
            "Slab"
          ]
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `empty` — `Index`, `VirtualBeam`, `Part`, `Girder/Slab`, `Comp./Tens.`, `LComName`, `Type`, `CHK`, `FT`, `FB`, `FTL`, `FBL`, `FTR`, `FBR`, `FMAX`, `ALW`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_SERVICE_VBEAM"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "VirtualBeam",
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
        "Girder",
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
        "729.32915625",
        "24000"
      ],
      [
        "2",
        "201",
        "J",
        "Girder",
        "Compression",
        "cLCB2",
        "-",
        "OK",
        "-0.0000",
        "-0.0000",
        "718.8343",
        "-593.0225",
        "729.3291",
        "-593.0225",
        "729.329125",
        "24000"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_SERVICE_VBEAM"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 30. `TABLE` · `PSC_STRESS_TENDON_VBEAM` — Check tensile stress for Prestressing tendons - Virtual Beam

> **기능** 가상보의 프리스트레싱 긴장재의 인장응력 검토 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738170871577](https://support.midasuser.com/hc/ko/articles/64738170871577)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Stress of tendons - Virtual Beam: "PSC_STRESS_TENDON_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Tendon | `"TENDON"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Check tensile stress for Prestressing tendons - Virtual Beam - Result Table Type",
          "enum": [
            "PSC_STRESS_TENDON_VBEAM"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each Tendon ID",
              "items": {
                "type": "integer",
                "minimum": 1
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify Tendon ID Range (e.g., '1to10')"
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

- `empty` — `Index`, `Tendon`, `FDL1`, `FDL2`, `FLL1`, `AFDL1`, `AFDL2`, `AFLL1`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_TENDON_VBEAM"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Tendon",
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
        "T1",
        "1135758.6930",
        "1262391.6367",
        "1230629.6463",
        "1422000.0000",
        "1343000.0000",
        "1027000.0000"
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_STRESS_TENDON_VBEAM"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 31. `TABLE` · `PSC_PRINCIPAL_CS_VBEAM` — Principal stress at a construction stage - Virtual Beam

> **기능** 가상보의 시공단계별 단면의 주응력 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738150381977](https://support.midasuser.com/hc/ko/articles/64738150381977)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Principal stress at CS - Virtual Beam: "PSC_PRINCIPAL_CS_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Virtual Beam | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Comp./Tens. | `"COMP_TENS"` | array | - | Optional |
| 10 | [General] Girder/Slab · Girder: "Girder" · Slab: "Slab" | `"SELECTION_TYPE"` | string | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Principal stress at a construction stage - Virtual Beam - Result Table Type",
          "enum": [
            "PSC_PRINCIPAL_CS_VBEAM"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "VirtualBeam",
              "Part",
              "Girder/Slab",
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
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Tension"
            ]
          }
        },
        "SELECTION_TYPE": {
          "type": "string",
          "description": "Girder or Slab Selection",
          "enum": [
            "Girder",
            "Slab"
          ]
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `empty` — `Index`, `VirtualBeam`, `Part`, `Girder/Slab`, `Comp./Tens.`, `Stage`, `CHK`, `Sig_P1`, `Sig_P2`, `Sig_P3`, `Sig_P4`, `Sig_P5`, `Sig_P6`, `Sig_P7`, `Sig_P8`, `Sig_P9`, `Sig_P10`, `Sig_MAX`, `Sig_AP`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_CS_VBEAM"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "VirtualBeam",
      "Part",
      "Girder/Slab",
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
        "I",
        "Girder",
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
      ],
      [
        "2",
        "201",
        "J",
        "Girder",
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_CS_VBEAM"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```


---

## 32. `TABLE` · `PSC_PRINCIPAL_SVC_VBEAM` — Principal stress at service loads - Virtual Beam

> **기능** 가상보의 사용하중에 대한 주응력 결과를 조회합니다.

### Input URI

```
{base url}/DESIGN/PSC/KDS-24-14-21-2021/TABLE
```

### Active Methods

`POST`

### Specifications

**원문** [한국어 64738162892825](https://support.midasuser.com/hc/ko/articles/64738162892825)

**Keyed Object Entry**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [Root Object] Argument object | `"Argument"` | object | - | **Required** |

**Item (Value Object Schema)**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | [General] Table Name | `"TABLE_NAME"` | string | - | Optional |
| 2 | [General] Table Type · Principal stress at service - Virtual Beam: "PSC_PRINCIPAL_SVC_VBEAM" | `"TABLE_TYPE"` | string | - | **Required** |
| 3 | [General] Export Path | `"EXPORT_PATH"` | string | - | Optional |
| 4 | [General] Unit Settings | `"UNIT"` | object | - | Optional |
| 4.1 | └ [General] Force unit | `"FORCE"` | string | - | Optional |
| 4.2 | └ [General] Length/Distance unit | `"DIST"` | string | - | Optional |
| 4.3 | └ [General] Heat unit | `"HEAT"` | string | - | Optional |
| 4.4 | └ [General] Temperature unit | `"TEMP"` | string | - | Optional |
| 5 | [General] Number Format | `"STYLES"` | object | - | Optional |
| 5.1 | └ Number format · Default: "Default" · Fixed: "Fixed" · Scientific: "Scientific" · General: "General" | `"FORMAT"` | string | - | Optional |
| 5.2 | └ [General] Digit place · Range: 0~15 | `"PLACE"` | integer | - | Optional |
| 6 | [General] Components | `"COMPONENTS"` | array | - | Optional |
| 7 | [General] Virtual Beam | `"NODE_ELEMS"` | object | - | Optional |
| 7.1 | └ [General] Specify Each ID | `"KEYS"` | array | - | Optional |
| 7.2 | └ [General] Specify ID Range | `"TO"` | string | - | Optional |
| 8 | [General] Part Number | `"PARTS"` | array | - | Optional |
| 9 | [General] Comp./Tens. | `"COMP_TENS"` | array | - | Optional |
| 10 | [General] Girder/Slab · Girder: "Girder" · Slab: "Slab" | `"SELECTION_TYPE"` | string | - | Optional |

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
          "description": "Response Table Title"
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Principal stress at service loads - Virtual Beam - Result Table Type",
          "enum": [
            "PSC_PRINCIPAL_SVC_VBEAM"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting (omit to use the model unit)",
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
          "description": "Response Number Format (omit to use the model format)",
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
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "VirtualBeam",
              "Part",
              "Girder/Slab",
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
          "description": "Node/Element No. Input",
          "additionalProperties": false,
          "maxProperties": 1,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer",
                "minimum": 1
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
          "description": "Element Part Number (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "PartJ"
            ]
          }
        },
        "COMP_TENS": {
          "type": "array",
          "description": "Compression or Tension Stress (omit for all)",
          "items": {
            "type": "string",
            "enum": [
              "Tension"
            ]
          }
        },
        "SELECTION_TYPE": {
          "type": "string",
          "description": "Girder or Slab Selection",
          "enum": [
            "Girder",
            "Slab"
          ]
        }
      }
    }
  }
}
```

### Response HEAD

공식 응답 예제의 표 이름과 `HEAD` 열 순서입니다.

- `empty` — `Index`, `VirtualBeam`, `Part`, `Girder/Slab`, `Comp./Tens.`, `LComName`, `Type`, `CHK`, `Sig_P1`, `Sig_P2`, `Sig_P3`, `Sig_P4`, `Sig_P5`, `Sig_P6`, `Sig_P7`, `Sig_P8`, `Sig_P9`, `Sig_P10`, `Sig_MAX`, `Sig_AP`

### Request / Response JSON

**Request**

```json
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_SVC_VBEAM"
  }
}
```

**Response**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "VirtualBeam",
      "Part",
      "Girder/Slab",
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
        "Girder",
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
        "-",
        "-"
      ],
      [
        "2",
        "201",
        "J",
        "Girder",
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
URI = f"{BASE_URL}/DESIGN/PSC/KDS-24-14-21-2021/TABLE"

payload = json.loads(r'''
{
  "Argument": {
    "TABLE_TYPE": "PSC_PRINCIPAL_SVC_VBEAM"
  }
}
''')
response = requests.post(URI, headers=HEADERS, json=payload)
response.raise_for_status()
print(response.json())
```
