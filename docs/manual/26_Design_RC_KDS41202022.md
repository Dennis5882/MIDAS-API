# 26. Design Code – RC KDS 41 20:2022 (철근콘크리트 설계)

> **대상 제품:** MIDAS Gen NX · MIDAS Civil NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

이 파트는 **철근콘크리트(RC) 설계 코드 KDS 41 20:2022** 관련 엔드포인트 **70개**(공통 접두사
`KDS-41-20-2022/<CODE>` 엔드포인트 69개 + RC 설계 코드 선택 엔드포인트 `DRC` 1개)를 다룹니다.
`DRC`를 제외한 69개는 공통 URI 접두사 **`{base url}/DESIGN/RC/KDS-41-20-2022/<CODE>`** 를
사용합니다.

> ⚠️ **2026-08-06 신규 엔드포인트 발견:** `DESIGN/RC/DRC`(활성 RC 설계 코드 선택)는 원문
> 생성일이 2026-06-18로 이전부터 있었으나, 챕터 개요 아티클("KDS 41 20 : 2022")에 이 항목을
> 담은 새 "Design Code" 그룹이 2026-08-06에 추가되면서 발견되었다. `KDS-41-20-2022` 접두사를
> 쓰지 않는 별도 URI(`DESIGN/RC/DRC`)라 번호 체계에 영향 없이 `## 0.`으로 추가한다.

- **`"Assign"` 방식:** 설계 코드·부재 파라미터 설정 엔드포인트는 요청 바디에서 `"Assign"` 객체를 사용하며, 각 키는 문자열 ID(예: `"1"`) 또는 부재 번호입니다.
- **`"Argument"` 방식:** 설계 수행(ANAL)·결과 테이블(TABLE)·리포트(REPORT) 엔드포인트는 POST 전용이며 `"Argument"` 객체로 대상·옵션을 지정합니다.
- **메서드 패턴 3종:**
  - **설정 싱글톤** (예: `DCO`, `LLRF`, `MATD`, `MEMB`, `SRDF`, `LMRR`): `GET` · `PUT` · `DELETE` (POST 없음, PUT으로 생성/갱신)
  - **부재별 파라미터** (예: `LENG`, `KFAC`, `FMAG`, 철근 데이터 `REBB` 등): `POST` · `GET` · `PUT` · `DELETE` (부재 ID `Assign`)
  - **설계 수행·결과** (`*-ANAL` / `*-TABLE` / `*-REPORT`, `CDESIGN`, `TABLE`): `POST` 전용 액션

> **참고:** 각 엔드포인트의 정확한 Active Methods는 아래 표와 각 절에 명시되어 있습니다. 강재 설계는 **[25_Design_Steel_KDS41302022.md](./25_Design_Steel_KDS41302022.md)**, SRC 설계는 **[27_Design_SRC_AIKSRC2K.md](./27_Design_SRC_AIKSRC2K.md)** 를 참고하세요. RC 설계 하중조합은 13장(Load Combinations)에서 다룹니다.

---

## Endpoint 목록 (70개)

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 0 | [`DRC`](#0-designrcdrc--rc-설계-코드-선택) | RC 설계 코드 선택 (`KDS-41-20-2022` 접두사 미사용) | GET · PUT · DELETE |
| 1 | [`DCO`](#1-designrckds-41-20-2022dco--콘크리트-설계-코드-옵션) | 콘크리트 설계 코드 옵션 | GET · PUT · DELETE |
| 2 | [`DCTL`](#2-designrckds-41-20-2022dctl--프레임-정의) | 프레임 정의 | GET · PUT · DELETE |
| 3 | [`LLRF`](#3-designrckds-41-20-2022llrf--활하중-저감계수) | 활하중 저감계수 | GET · PUT · DELETE |
| 4 | [`LCTB`](#4-designrckds-41-20-2022lctb--비선형-하중케이스-하중기여) | 비선형 하중케이스 하중기여 | GET · DELETE |
| 5 | [`SRDF`](#5-designrckds-41-20-2022srdf--강도감소계수) | 강도감소계수 | GET · PUT · DELETE |
| 6 | [`EQCT`](#6-designrckds-41-20-2022eqct--지진-하중조합-타입) | 지진 하중조합 타입 | POST · GET · PUT · DELETE |
| 7 | [`ULCT`](#7-designrckds-41-20-2022ulct--지하-하중조합-타입) | 지하 하중조합 타입 | POST · GET · PUT · DELETE |
| 8 | [`SUEQ`](#8-designrckds-41-20-2022sueq--지진-스케일업-계수) | 지진 스케일업 계수 | POST · GET · PUT · DELETE |
| 9 | [`SDGN`](#9-designrckds-41-20-2022sdgn--내진-설계-타입) | 내진 설계 타입 | POST · GET · PUT · DELETE |
| 10 | [`SCOL`](#10-designrckds-41-20-2022scol--내진-기둥-타입) | 내진 기둥 타입 | POST · GET · PUT · DELETE |
| 11 | [`MBTP`](#11-designrckds-41-20-2022mbtp--부재-타입-수정) | 부재 타입 수정 | POST · GET · PUT · DELETE |
| 12 | [`MEMB`](#12-designrckds-41-20-2022memb--부재-배정) | 부재 배정 | GET · PUT · DELETE |
| 13 | [`MATD`](#13-designrckds-41-20-2022matd--콘크리트-재료-수정) | 콘크리트 재료 수정 | GET · PUT · DELETE |
| 14 | [`LENG`](#14-designrckds-41-20-2022leng--비지지-길이l-lb) | 비지지 길이(L, Lb) | POST · GET · PUT · DELETE |
| 15 | [`KFAC`](#15-designrckds-41-20-2022kfac--유효좌굴길이계수k) | 유효좌굴길이계수(K) | POST · GET · PUT · DELETE |
| 16 | [`CMFT`](#16-designrckds-41-20-2022cmft--등가모멘트-보정계수cm) | 등가모멘트 보정계수(Cm) | POST · GET · PUT · DELETE |
| 17 | [`FMAG`](#17-designrckds-41-20-2022fmag--모멘트-확대계수b1δb-b2δs) | 모멘트 확대계수(B1/δb, B2/δs) | POST · GET · PUT · DELETE |
| 18 | [`MLLR`](#18-designrckds-41-20-2022mllr--활하중-저감계수-수정) | 활하중 저감계수 수정 | POST · GET · PUT · DELETE |
| 19 | [`HCBM`](#19-designrckds-41-20-2022hcbm--헌치보-배정) | 헌치보 배정 | POST · GET · PUT · DELETE |
| 20 | [`MRFT`](#20-designrckds-41-20-2022mrft--모멘트-재분배-계수) | 모멘트 재분배 계수 | POST · GET · PUT · DELETE |
| 21 | [`TRFT`](#21-designrckds-41-20-2022trft--비틀림-감소계수) | 비틀림 감소계수 | POST · GET · PUT · DELETE |
| 22 | [`MCMB`](#22-designrckds-41-20-2022mcmb--보-모멘트-산정-방법) | 보 모멘트 산정 방법 | POST · GET · PUT · DELETE |
| 23 | [`DFBA`](#23-designrckds-41-20-2022dfba--부재-배정된-보-설계력) | 부재 배정된 보 설계력 | POST · GET · PUT · DELETE |
| 24 | [`PMDM`](#24-designrckds-41-20-2022pmdm--p-m-곡선-산정-방법) | P-M 곡선 산정 방법 | POST · GET · DELETE · PUT |
| 25 | [`WMAK`](#25-designrckds-41-20-2022wmak--벽체-마크-데이터-수정) | 벽체 마크 데이터 수정 | POST · GET · PUT · DELETE |
| 26 | [`BEMW`](#26-designrckds-41-20-2022bemw--벽체id별-경계요소법) | 벽체ID별 경계요소법 | POST · GET · PUT · DELETE |
| 27 | [`REXC`](#27-designrckds-41-20-2022rexc--철근-노출-조건) | 철근 노출 조건 | POST · GET · PUT · DELETE |
| 28 | [`LMRR`](#28-designrckds-41-20-2022lmrr--최대-철근비-제한) | 최대 철근비 제한 | GET · PUT · DELETE |
| 29 | [`DCRM-BEAM`](#29-designrckds-41-20-2022dcrm-beam--보-부재별-철근-설계기준) | 보 부재별 철근 설계기준 | POST · GET · PUT · DELETE |
| 30 | [`DCRM-COLUMN`](#30-designrckds-41-20-2022dcrm-column--기둥-부재별-철근-설계기준) | 기둥 부재별 철근 설계기준 | POST · GET · PUT · DELETE |
| 31 | [`DCRM-BRACE`](#31-designrckds-41-20-2022dcrm-brace--가새-부재별-철근-설계기준) | 가새 부재별 철근 설계기준 | POST · GET · PUT · DELETE |
| 32 | [`DCRM-WALL`](#32-designrckds-41-20-2022dcrm-wall--벽체-부재별-철근-설계기준) | 벽체 부재별 철근 설계기준 | POST · GET · PUT · DELETE |
| 33 | [`DCRE`](#33-designrckds-41-20-2022dcre--철근-설계기준) | 철근 설계기준 | POST · GET · PUT · DELETE |
| 34 | [`DCREM`](#34-designrckds-41-20-2022dcrem--접합부-보-철근-동일화) | 접합부 보 철근 동일화 | POST · GET · PUT · DELETE |
| 35 | [`REBB`](#35-designrckds-41-20-2022rebb--보-철근-데이터-수정) | 보 철근 데이터 수정 | POST · GET · DELETE · PUT |
| 36 | [`REBC`](#36-designrckds-41-20-2022rebc--기둥-철근-데이터-수정) | 기둥 철근 데이터 수정 | POST · GET · PUT · DELETE |
| 37 | [`REBW`](#37-designrckds-41-20-2022rebw--벽체-철근-데이터-수정) | 벽체 철근 데이터 수정 | POST · PUT · DELETE · GET |
| 38 | [`REBR`](#38-designrckds-41-20-2022rebr--가새-철근-데이터-수정) | 가새 철근 데이터 수정 | POST · GET · PUT · DELETE |
| 39 | [`BD-ANAL`](#39-designrckds-41-20-2022bd-anal--rc-보-설계-수행) | RC 보 설계 수행 | POST |
| 40 | [`BD-TABLE`](#40-designrckds-41-20-2022bd-table--rc-보-설계-테이블) | RC 보 설계 테이블 | POST |
| 41 | [`BD-REPORT`](#41-designrckds-41-20-2022bd-report--rc-보-설계-리포트) | RC 보 설계 리포트 | POST |
| 42 | [`CD-ANAL`](#42-designrckds-41-20-2022cd-anal--rc-기둥-설계-수행) | RC 기둥 설계 수행 | POST |
| 43 | [`CD-TABLE`](#43-designrckds-41-20-2022cd-table--rc-기둥-설계-테이블) | RC 기둥 설계 테이블 | POST |
| 44 | [`CD-REPORT`](#44-designrckds-41-20-2022cd-report--rc-기둥-설계-리포트) | RC 기둥 설계 리포트 | POST |
| 45 | [`BRD-ANAL`](#45-designrckds-41-20-2022brd-anal--rc-가새-설계-수행) | RC 가새 설계 수행 | POST |
| 46 | [`BRD-TABLE`](#46-designrckds-41-20-2022brd-table--rc-가새-설계-테이블) | RC 가새 설계 테이블 | POST |
| 47 | [`BRD-REPORT`](#47-designrckds-41-20-2022brd-report--rc-가새-설계-리포트) | RC 가새 설계 리포트 | POST |
| 48 | [`WD-ANAL`](#48-designrckds-41-20-2022wd-anal--rc-벽체-설계-수행) | RC 벽체 설계 수행 | POST |
| 49 | [`WD-TABLE`](#49-designrckds-41-20-2022wd-table--rc-벽체-설계-테이블) | RC 벽체 설계 테이블 | POST |
| 50 | [`WD-REPORT`](#50-designrckds-41-20-2022wd-report--rc-벽체-설계-리포트) | RC 벽체 설계 리포트 | POST |
| 51 | [`HCD-ANAL`](#51-designrckds-41-20-2022hcd-anal--rc-헌치보-설계-수행) | RC 헌치보 설계 수행 | POST |
| 52 | [`HCD-TABLE`](#52-designrckds-41-20-2022hcd-table--rc-헌치보-설계-테이블) | RC 헌치보 설계 테이블 | POST |
| 53 | [`HCD-REPORT`](#53-designrckds-41-20-2022hcd-report--rc-헌치보-설계-리포트) | RC 헌치보 설계 리포트 | POST |
| 54 | [`BC-ANAL`](#54-designrckds-41-20-2022bc-anal--rc-보-검토-수행) | RC 보 검토 수행 | POST |
| 55 | [`BC-TABLE`](#55-designrckds-41-20-2022bc-table--rc-보-검토-테이블) | RC 보 검토 테이블 | POST |
| 56 | [`BC-REPORT`](#56-designrckds-41-20-2022bc-report--rc-보-검토-리포트) | RC 보 검토 리포트 | POST |
| 57 | [`CC-ANAL`](#57-designrckds-41-20-2022cc-anal--rc-기둥-검토-수행) | RC 기둥 검토 수행 | POST |
| 58 | [`CC-TABLE`](#58-designrckds-41-20-2022cc-table--rc-기둥-검토-테이블) | RC 기둥 검토 테이블 | POST |
| 59 | [`CC-REPORT`](#59-designrckds-41-20-2022cc-report--rc-기둥-검토-리포트) | RC 기둥 검토 리포트 | POST |
| 60 | [`BRC-ANAL`](#60-designrckds-41-20-2022brc-anal--rc-가새-검토-수행) | RC 가새 검토 수행 | POST |
| 61 | [`BRC-TABLE`](#61-designrckds-41-20-2022brc-table--rc-가새-검토-테이블) | RC 가새 검토 테이블 | POST |
| 62 | [`BRC-REPORT`](#62-designrckds-41-20-2022brc-report--rc-가새-검토-리포트) | RC 가새 검토 리포트 | POST |
| 63 | [`WC-ANAL`](#63-designrckds-41-20-2022wc-anal--rc-벽체-검토-수행) | RC 벽체 검토 수행 | POST |
| 64 | [`WC-TABLE`](#64-designrckds-41-20-2022wc-table--rc-벽체-검토-테이블) | RC 벽체 검토 테이블 | POST |
| 65 | [`WC-REPORT`](#65-designrckds-41-20-2022wc-report--rc-벽체-검토-리포트) | RC 벽체 검토 리포트 | POST |
| 66 | [`CDESIGN`](#66-designrckds-41-20-2022cdesign--rc-콘크리트-종합-설계-결과) | RC 콘크리트 종합 설계 결과 | POST |
| 67 | [`TABLE`](#67-designrckds-41-20-2022table--기둥-설계력column-design-forces) | 기둥 설계력(Column Design Forces) | POST |
| 68 | [`TABLE`](#68-designrckds-41-20-2022table--가새-설계력brace-design-forces) | 가새 설계력(Brace Design Forces) | POST |
| 69 | [`TABLE`](#69-designrckds-41-20-2022table--보-설계력beam-design-forces) | 보 설계력(Beam Design Forces) | POST |

---

## 0. `DESIGN/RC/DRC` — RC 설계 코드 선택

> **기능:** 현재 프로젝트에 적용할 **RC 설계 코드**를 선택합니다. 이 챕터의 나머지 69개
> 엔드포인트(`KDS-41-20-2022/<CODE>`)와 달리 URI가 `KDS-41-20-2022` 접두사를 쓰지 않는
> 별도의 상위 선택 엔드포인트입니다.

### Input URI

```
{base url}/DESIGN/RC/DRC
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
                "KDS 41 20 : 2022"
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
| --- | --- | --- | --- | --- | --- |
| 1 | Assign 래퍼 (ID 문자열 키, 1개) | `"Assign"` | Object | — | **필수** |
| 2 | RC 설계 코드 · 현재 `"KDS 41 20 : 2022"` 1개 값만 지원 | `"DGNCODE"` | String (enum) | — | **필수** |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "KDS 41 20 : 2022"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCON": {
    "1": {
      "DGNCODE": "KDS 41 20 : 2022"
    }
  }
}
```

> ⚠️ **응답 최상위 키 주의:** GET 응답의 최상위 키는 `"DCON"`이며(엔드포인트명 `DRC`도,
> 옵션 엔드포인트 `DCO`도 아님), 원문 Response 예제 그대로다.

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/DRC"

# RC 설계 코드 선택 (PUT): KDS 41 20:2022
payload = {"Assign": {"1": {"DGNCODE": "KDS 41 20 : 2022"}}}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 1. `DESIGN/RC/KDS-41-20-2022/DCO` — 콘크리트 설계 코드 옵션

> **기능:** 콘크리트 설계 기준(KDS 41 20:2022) 및 내진 특별규정·비틀림·모멘트 재분배·노출조건·P-M 곡선 산정법 등 전역 설계 옵션을 설정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCO
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
      "maxProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "DESIGN_CD"
          ],
          "additionalProperties": false,
          "properties": {
            "DESIGN_CD": {
              "type": "string",
              "description": "Concrete design code standard",
              "oneOf": [
                {
                  "title": "KDS 41 20 : 2022",
                  "const": "KDS 41 20 : 2022"
                }
              ]
            },
            "SEISMIC_PROV": {
              "type": "boolean",
              "description": "Apply Special Provisions for Seismic Design",
              "default": false
            },
            "SEISMIC": {
              "type": "object",
              "description": "Seismic design parameters",
              "additionalProperties": false,
              "properties": {
                "FRAME_TYPE": {
                  "type": "string",
                  "description": "Select Frame Type",
                  "default": "Special",
                  "oneOf": [
                    {
                      "title": "Special Moment Frames",
                      "const": "Special"
                    },
                    {
                      "title": "Intermediate Moment Frames",
                      "const": "Intermediate"
                    },
                    {
                      "title": "Ordinary Moment Frames",
                      "const": "Ordinary"
                    }
                  ]
                },
                "STRONG_COL_WEAK_LAST": {
                  "type": "boolean",
                  "description": "Consider strong column-weak beam on last floor",
                  "default": true
                },
                "SHEAR_WALL": {
                  "type": "object",
                  "description": "Shear Wall Type configuration",
                  "additionalProperties": false,
                  "properties": {
                    "SPEC_RC_WALL": {
                      "type": "boolean",
                      "description": "Special RC Structural Wall",
                      "default": true
                    },
                    "BDRY_ELEM_MTHD": {
                      "type": "string",
                      "description": "Boundary Element Method",
                      "default": "Displacement",
                      "oneOf": [
                        {
                          "title": "Displacement Based Method",
                          "const": "Displacement"
                        },
                        {
                          "title": "Stress Based Method",
                          "const": "Stress"
                        }
                      ]
                    },
                    "DEFL_AMP_FACT": {
                      "type": "number",
                      "description": "Deflection Amplification Factor (Cd)",
                      "default": 4.5,
                      "enum": [
                        1.25,
                        1.5,
                        2,
                        2.5,
                        3,
                        3.25,
                        4,
                        4.5,
                        5,
                        5.5,
                        6,
                        6.5
                      ]
                    },
                    "IMP_FACT": {
                      "type": "number",
                      "description": "Important Factor (Ie)",
                      "default": 1.2,
                      "enum": [
                        1,
                        1.2,
                        1.5
                      ]
                    }
                  }
                },
                "SHEAR_DES": {
                  "type": "object",
                  "description": "Shear for Design configuration",
                  "additionalProperties": false,
                  "properties": {
                    "R": {
                      "type": "number",
                      "description": "Special-only R factor input shown as 'R*Vc(a1*Σ(Mpr)/L) ≥ max(Ve1,Ve2)/2 , R='",
                      "default": 0,
                      "minimum": 0
                    },
                    "MTHD": {
                      "type": "string",
                      "description": "Calculation method",
                      "default": "MIN",
                      "oneOf": [
                        {
                          "title": "MAX(Ve1,Ve2)",
                          "const": "MAX"
                        },
                        {
                          "title": "MIN(Ve1,Ve2)",
                          "const": "MIN"
                        },
                        {
                          "title": "Ve1",
                          "const": "Ve1"
                        },
                        {
                          "title": "Ve2",
                          "const": "Ve2"
                        }
                      ]
                    },
                    "A1": {
                      "type": "number",
                      "description": "Ve1 = Vg + a1*Σ(Mn)/L coefficient",
                      "default": 1
                    },
                    "A2": {
                      "type": "number",
                      "description": "Ve2 = Vg + a2*Veq coefficient",
                      "default": 2
                    }
                  }
                },
                "BEAM_COL_JNT_DES": {
                  "type": "boolean",
                  "description": "Beam-Column Joint Design",
                  "default": false
                },
                "JOINT": {
                  "type": "object",
                  "description": "Beam-Column Joint configuration",
                  "additionalProperties": false,
                  "properties": {
                    "CHK_POS": {
                      "type": "string",
                      "description": "Select Check Position",
                      "default": "Bottom",
                      "oneOf": [
                        {
                          "title": "Top",
                          "const": "Top"
                        },
                        {
                          "title": "Bottom",
                          "const": "Bottom"
                        }
                      ]
                    },
                    "EXCL_MEM_TYPES": {
                      "type": "array",
                      "description": "Member Types to be excluded in Seismic Design",
                      "items": {
                        "type": "string",
                        "enum": [
                          "SUBBEAM",
                          "CANTIL",
                          "UGBEAMCOL"
                        ]
                      },
                      "uniqueItems": true,
                      "default": [
                        "SUBBEAM",
                        "CANTIL",
                        "UGBEAMCOL"
                      ]
                    }
                  }
                }
              }
            },
            "TORS_DES": {
              "type": "boolean",
              "description": "Torsion Design",
              "default": false
            },
            "TORS_RDCT_FACT": {
              "type": "number",
              "description": "Torsion Reduction Factor for Beam",
              "default": 1,
              "minimum": 0
            },
            "MOM_REDIST_FACT": {
              "type": "number",
              "description": "Moment Redistribution Factor for Beam",
              "default": 1,
              "exclusiveMinimum": 0,
              "maximum": 1
            },
            "MOM_CALC_MTHD": {
              "type": "string",
              "description": "Moment Calculation Method for Beam",
              "default": "Equivalent",
              "oneOf": [
                {
                  "title": "Equivalent Rebar",
                  "const": "Equivalent"
                },
                {
                  "title": "Each Rebar",
                  "const": "Each"
                }
              ]
            },
            "USE_SUBDIV_FORCE": {
              "type": "boolean",
              "description": "Use Subdivided Force for Beam Assigned as Member",
              "default": false
            },
            "EXP_COND": {
              "type": "string",
              "description": "Exposure Condition (kcr)",
              "default": "Dry",
              "oneOf": [
                {
                  "title": "Dry",
                  "const": "Dry"
                },
                {
                  "title": "etc",
                  "const": "etc"
                }
              ]
            },
            "PM_CRV_CALC": {
              "type": "string",
              "description": "P-M Curve Calculation Method",
              "default": "KeepMPConstant",
              "oneOf": [
                {
                  "title": "Keep P Constant",
                  "const": "KeepPConstant"
                },
                {
                  "title": "Keep M/P Constant",
                  "const": "KeepMPConstant"
                }
              ]
            },
            "UG_LC": {
              "type": "boolean",
              "description": "Use Under Ground Load Combination Type for Under Ground Members",
              "default": true
            },
            "CONC_STRS_STRN": {
              "type": "string",
              "description": "Concrete Stress-Strain Type for Bending",
              "default": "Equivalent",
              "oneOf": [
                {
                  "title": "Equivalent-Rectangle",
                  "const": "Equivalent"
                },
                {
                  "title": "Parabola-Rectangle (Average)",
                  "const": "Parabola"
                }
              ]
            },
            "FS_MAIN_BAR": {
              "type": "string",
              "description": "fs of Main bar in Beam Design",
              "default": "2/3fy",
              "oneOf": [
                {
                  "title": "2/3*fy",
                  "const": "2/3fy"
                },
                {
                  "title": "By Program",
                  "const": "ByProgram"
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
| 1 | Assign 래퍼 (ID 문자열 키, 1개) | `"Assign"` | Object | — | **필수** |
| 2 | 설계 코드 (KDS 41 20 : 2022 고정) | `"DESIGN_CD"` | String (oneOf) | — | **필수** |
| 3 | 내진설계 특별규정 적용 | `"SEISMIC_PROV"` | Boolean | `false` | 선택 |
| 4 | 비틀림 설계 | `"TORS_DES"` | Boolean | `false` | 선택 |
| 5 | 보 비틀림 감소계수 (≥0, TORS_DES=true일 때) | `"TORS_RDCT_FACT"` | Number | `1` | 선택 |
| 6 | 보 모멘트 재분배 계수 (>0, ≤1) | `"MOM_REDIST_FACT"` | Number | `1` | 선택 |
| 7 | 보 모멘트 산정법 (Equivalent=등가철근, Each=개별철근) | `"MOM_CALC_MTHD"` | String (oneOf) | `"Equivalent"` | 선택 |
| 8 | 부재 배정 보에 세분화 부재력 사용 | `"USE_SUBDIV_FORCE"` | Boolean | `false` | 선택 |
| 9 | 노출조건 kcr (Dry / etc) | `"EXP_COND"` | String (oneOf) | `"Dry"` | 선택 |
| 10 | P-M 곡선 산정법 (KeepPConstant=P 고정, KeepMPConstant=M/P 고정) | `"PM_CRV_CALC"` | String (oneOf) | `"KeepMPConstant"` | 선택 |
| 11 | 지하부재에 지하 하중조합 타입 사용 | `"UG_LC"` | Boolean | `true` | 선택 |
| 12 | 휨 콘크리트 응력-변형 타입 (Equivalent=등가 사각형, Parabola=포물선-사각형 평균) | `"CONC_STRS_STRN"` | String (oneOf) | `"Equivalent"` | 선택 |
| 13 | 보 설계 주철근 fs (2/3fy / ByProgram) | `"FS_MAIN_BAR"` | String (oneOf) | `"2/3fy"` | 선택 |
| 14 | 내진 설계 파라미터 (SEISMIC_PROV=true일 때) | `"SEISMIC"` | Object | — | 선택 |
| 14.1 | 프레임 타입 (Special=특수, Intermediate=중간, Ordinary=보통 모멘트골조) | `"FRAME_TYPE"` | String (oneOf) | `"Special"` | 선택 |
| 14.2 | 최상층 강기둥-약보 고려 | `"STRONG_COL_WEAK_LAST"` | Boolean | `true` | 선택 |
| 14.3 | 전단벽 설정 (FRAME_TYPE=Special/Intermediate일 때) | `"SHEAR_WALL"` | Object | — | 선택 |
| 14.3.1 | 특수 철근콘크리트 구조벽 | `"SPEC_RC_WALL"` | Boolean | `true` | 선택 |
| 14.3.2 | 경계요소법 (Displacement=변위기반, Stress=응력기반) | `"BDRY_ELEM_MTHD"` | String (oneOf) | `"Displacement"` | 선택 |
| 14.3.3 | 변위 증폭계수 Cd (1.25/1.5/2/2.5/3/3.25/4/4.5/5/5.5/6/6.5) | `"DEFL_AMP_FACT"` | Number (enum) | `4.5` | 선택 |
| 14.3.4 | 중요도 계수 Ie (1 / 1.2 / 1.5) | `"IMP_FACT"` | Number (enum) | `1.2` | 선택 |
| 14.4 | 설계용 전단력 설정 | `"SHEAR_DES"` | Object | — | 선택 |
| 14.4.1 | 산정법 (MAX(Ve1,Ve2) / MIN(Ve1,Ve2) / Ve1 / Ve2) | `"MTHD"` | String (oneOf) | `"MIN"` | 선택 |
| 14.4.2 | R·Vc ≥ max(Ve1,Ve2)/2 의 R (≥0, FRAME_TYPE=Special) | `"R"` | Number | `0` | 선택 |
| 14.4.3 | a1: Ve1 = Vg + a1·Σ(Mn)/L | `"A1"` | Number | `1` | 선택 |
| 14.4.4 | a2: Ve2 = Vg + a2·Veq | `"A2"` | Number | `2` | 선택 |
| 14.5 | 보-기둥 접합부 설계 | `"BEAM_COL_JNT_DES"` | Boolean | `false` | 선택 |
| 14.6 | 보-기둥 접합부 설정 | `"JOINT"` | Object | — | 선택 |
| 14.6.1 | 내진설계 제외 부재타입 (SUBBEAM=소보, CANTIL=캔틸레버, UGBEAMCOL=지하보/기둥) | `"EXCL_MEM_TYPES"` | Array[string] | `["SUBBEAM","CANTIL","UGBEAMCOL"]` | 선택 |
| 14.6.2 | 검토 위치 (Top / Bottom) | `"CHK_POS"` | String (oneOf) | `"Bottom"` | 선택 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DESIGN_CD": "KDS 41 20 : 2022 ",
      "MOM_CALC_MTHD": "Equivalent",
      "EXP_COND": "etc",
      "PM_CRV_CALC": "KeepMPConstant",
      "CONC_STRS_STRN": "Equivalent",
      "FS_MAIN_BAR": "2/3fy",
      "SEISMIC_PROV": true,
      "TORS_DES": true,
      "TORS_RDCT_FACT": 1,
      "MOM_REDIST_FACT": 1,
      "USE_SUBDIV_FORCE": true,
      "UG_LC": true,
      "SEISMIC": {
        "FRAME_TYPE": "Special",
        "STRONG_COL_WEAK_LAST": true,
        "BEAM_COL_JNT_DES": true,
        "JOINT": {
          "CHK_POS": "Top",
          "EXCL_MEM_TYPES": [
            "SUBBEAM",
            "CANTIL",
            "UGBEAMCOL"
          ]
        },
        "SHEAR_WALL": {
          "SPEC_RC_WALL": true,
          "BDRY_ELEM_MTHD": "Displacement",
          "DEFL_AMP_FACT": 4,
          "IMP_FACT": 1.2
        },
        "SHEAR_DES": {
          "R": 0.5,
          "MTHD": "Ve1",
          "A1": 1.1,
          "A2": 1.2
        }
      }
    }
  }
}
```

**GET Response Body (최상위 키 `DCORC`)**

```json
{
  "DCORC": {
    "1": {
      "DESIGN_CD": "KDS 41 20 : 2022 ",
      "SEISMIC_PROV": true,
      "TORS_DES": true,
      "MOM_REDIST_FACT": 1,
      "MOM_CALC_MTHD": "Equivalent",
      "USE_SUBDIV_FORCE": true,
      "EXP_COND": "etc",
      "PM_CRV_CALC": "KeepMPConstant",
      "UG_LC": true,
      "CONC_STRS_STRN": "Equivalent",
      "FS_MAIN_BAR": "2/3fy",
      "SEISMIC": {
        "FRAME_TYPE": "Special",
        "STRONG_COL_WEAK_LAST": true,
        "SHEAR_WALL": {
          "SPEC_RC_WALL": true,
          "BDRY_ELEM_MTHD": "Displacement",
          "DEFL_AMP_FACT": 4,
          "IMP_FACT": 1.2
        },
        "SHEAR_DES": {
          "MTHD": "Ve1",
          "R": 0.5,
          "A1": 1.1,
          "A2": 1.2
        },
        "BEAM_COL_JNT_DES": true,
        "JOINT": {
          "EXCL_MEM_TYPES": [
            "SUBBEAM",
            "CANTIL",
            "UGBEAMCOL"
          ],
          "CHK_POS": "Top"
        }
      },
      "TORS_RDCT_FACT": 1
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCO"

# 1) 전역 콘크리트 설계 옵션 설정 (PUT) — 내진 특별규정 포함
payload = {
    "Assign": {
        "1": {
            "DESIGN_CD": "KDS 41 20 : 2022",
            "SEISMIC_PROV": True,          # 내진 특별규정 적용
            "TORS_DES": True,              # 비틀림 설계 수행
            "MOM_REDIST_FACT": 0.9,        # 모멘트 재분배 계수(0~1)
            "PM_CRV_CALC": "KeepMPConstant",
            "SEISMIC": {
                "FRAME_TYPE": "Special",
                "SHEAR_WALL": {"BDRY_ELEM_MTHD": "Displacement", "IMP_FACT": 1.2},
            },
        }
    }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 현재 설정 조회 (GET)
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 설정 초기화 (DELETE) — 필요 시
# requests.delete(URI, headers=HEADERS)
```

---

## 2. `DESIGN/RC/KDS-41-20-2022/DCTL` — 프레임 정의

> **기능:** 설계 프레임의 X/Y 방향 횡지지 여부(Sway/Non-sway), 유효좌굴길이계수 자동계산, 설계 타입(3D/평면)을 정의합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCTL
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
| 1 | Assign 래퍼 (ID 문자열 키, 1개) | `"Assign"` | Object | — | **필수** |
| 2 | X방향 프레임 (Unbraced Sway=비횡지지/횡변위, Braced Non-sway=횡지지/무횡변위) | `"FRAMEX"` | String (oneOf) | `"Braced Non-sway"` | 선택 |
| 3 | Y방향 프레임 (Unbraced Sway=비횡지지/횡변위, Braced Non-sway=횡지지/무횡변위) | `"FRAMEY"` | String (oneOf) | `"Braced Non-sway"` | 선택 |
| 4 | 유효좌굴길이계수 자동계산 | `"bAUTOKF"` | Boolean | `false` | 선택 |
| 5 | 설계 타입 (3D / XZ / YZ / XY 평면) | `"DT"` | String (oneOf) | `"3D"` | 선택 |

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCTL"

# 프레임 정의 설정 (PUT): X/Y 모두 횡지지, K 자동계산, X-Z 평면 설계
payload = {
    "Assign": {
        "1": {
            "FRAMEX": "Braced Non-sway",
            "FRAMEY": "Braced Non-sway",
            "bAUTOKF": True,
            "DT": "XZ",
        }
    }
}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 3. `DESIGN/RC/KDS-41-20-2022/LLRF` — 활하중 저감계수

> **기능:** 층별·범위별 활하중 저감계수 표를 정의합니다. 적용 성분(축력/모멘트/전단), 계산 규칙, 대상 활하중 케이스를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/LLRF
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
| 1 | Assign 래퍼 (ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 계산 규칙 (0=일반 설계코드, 1=중국 기준) | `"CALC_RULE"` | Integer (oneOf) | `0` | 선택 |
| 3 | 적용 성분 (ALL=전체, AXIAL=축력, MOMENTS=모멘트, SHEAR=전단) | `"APPLIED_COMP"` | Array[string] | `["AXIAL"]` | 선택 |
| 4 | 대상 활하중 케이스명 목록 | `"LIVE_LOAD_CASES"` | Array[string] | — | 선택 |
| 5 | 활하중 저감계수 테이블 데이터 | `"REDUCTION_DATA"` | Array[object] | — | **필수** |
| 5.1 | 층 이름 | `"STORY"` | String | — | **필수** |
| 5.2 | X 최소 좌표 | `"XMIN"` | Number | `0` | 선택 |
| 5.3 | X 최대 좌표 | `"XMAX"` | Number | `0` | 선택 |
| 5.4 | Y 최소 좌표 | `"YMIN"` | Number | `0` | 선택 |
| 5.5 | Y 최대 좌표 | `"YMAX"` | Number | `0` | 선택 |
| 5.6 | 최대값 Rmax (1~0.5, CALC_RULE=0일 때) | `"RANGE_MAX"` | Number (enum) | `1` | 선택 |
| 5.7 | 최소값 Rmin (1~0.5, CALC_RULE=0일 때) | `"RANGE_MIN"` | Number (enum) | `0.5` | 선택 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "CALC_RULE": 0,
      "APPLIED_COMP": [
        "AXIAL"
      ],
      "LIVE_LOAD_CASES": [],
      "REDUCTION_DATA": []
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
        "AXIAL"
      ],
      "LIVE_LOAD_CASES": [],
      "REDUCTION_DATA": []
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/LLRF"

# 활하중 저감계수 설정 (PUT): 특정 층 범위에 저감계수 범위 지정
payload = {
    "Assign": {
        "1": {
            "CALC_RULE": 0,
            "APPLIED_COMP": ["AXIAL", "MOMENTS"],   # 축력·모멘트에 적용
            "LIVE_LOAD_CASES": ["LL"],
            "REDUCTION_DATA": [
                {"STORY": "2F", "XMIN": 0, "XMAX": 30, "YMIN": 0, "YMAX": 20,
                 "RANGE_MAX": 1, "RANGE_MIN": 0.5},
            ],
        }
    }
}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 4. `DESIGN/RC/KDS-41-20-2022/LCTB` — 비선형 하중케이스 하중기여

> **기능:** 비선형 해석 하중케이스의 하중기여(Load Contribution) 항목을 조회·삭제합니다. 각 항목은 계수와 하중케이스명으로 구성됩니다. (읽기 전용 파생 정보 — GET/DELETE만 지원)

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/LCTB
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
| 1 | Assign 래퍼 (ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 하중기여 이름 | `"NAME"` | String | — | **필수** |
| 3 | 설명 | `"DESC"` | String | `""` | 선택 |
| 4 | 하중기여 항목 리스트 | `"BASE_ITEM"` | Array[object] | — | **필수** |
| 4.1 | 계수 | `"FACTOR"` | Number | — | **필수** |
| 4.2 | 하중케이스 이름 | `"LOAD_CASE_NAME"` | String | — | **필수** |

### Request / Response JSON

**GET Response Body (읽기 전용)**

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
    },
    "4": {
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
    "5": {
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
    "6": {
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
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/LCTB"

# LCTB는 GET/DELETE만 지원하는 읽기 전용 파생 정보입니다.
# 1) 비선형 하중케이스 하중기여 조회 (GET)
res = requests.get(URI, headers=HEADERS)
print("GET:", res.status_code, res.json())

# 2) 전체 삭제 (DELETE)
# print("DELETE:", requests.delete(URI, headers=HEADERS).json())
```

---

## 5. `DESIGN/RC/KDS-41-20-2022/SRDF` — 강도감소계수

> **기능:** 인장지배·나선철근·기타철근 부재·전단/비틀림에 대한 강도감소계수 φ 값을 설정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/SRDF
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "description": "RC Strength Reduction Factors settings (KDS 41 20:2022). Supported methods: GET, PUT.",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "PHI_T": {
              "type": "number",
              "description": "For Tensile Control (phi_t)",
              "default": 0.85
            },
            "PHI_C1": {
              "type": "number",
              "description": "Member with Spiral Reinforcement (phi_c1)",
              "default": 0.7
            },
            "PHI_C2": {
              "type": "number",
              "description": "Other Reinforced Member (phi_c2)",
              "default": 0.65
            },
            "PHI_V": {
              "type": "number",
              "description": "For Shear and Torsion (phi_v)",
              "default": 0.75
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
| 1 | Assign 래퍼 (ID 문자열 키, 1개) | `"Assign"` | Object | — | **필수** |
| 2 | 인장지배 φt | `"PHI_T"` | Number | `0.85` | 선택 |
| 3 | 나선철근 부재 φc1 | `"PHI_C1"` | Number | `0.7` | 선택 |
| 4 | 기타 철근 부재 φc2 | `"PHI_C2"` | Number | `0.65` | 선택 |
| 5 | 전단·비틀림 φv | `"PHI_V"` | Number | `0.75` | 선택 |

### Request / Response JSON

**PUT Request Body**

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

**GET Response Body (최상위 키 `SRDFRC`)**

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

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/SRDF"

# 강도감소계수 φ 사용자 지정 (PUT)
payload = {
    "Assign": {
        "1": {"PHI_T": 0.85, "PHI_C1": 0.70, "PHI_C2": 0.65, "PHI_V": 0.75}
    }
}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 6. `DESIGN/RC/KDS-41-20-2022/EQCT` — 지진 하중조합 타입

> **기능:** 부재별로 특수 지진하중(Special Seismic Loads) 또는 수직 지진력(Vertical Seismic Forces) 적용 타입을 배정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/EQCT
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
| 1 | Assign 래퍼 (요소 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 부재 타입 (Special Seismic Loads / Vertical Seismic Forces) | `"TYPE"` | String (oneOf) | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "1066": {
      "TYPE": "Special Seismic Loads"
    },
    "1067": {
      "TYPE": "Special Seismic Loads"
    },
    "1068": {
      "TYPE": "Vertical Seismic Forces"
    },
    "1069": {
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
    "1067": {
      "TYPE": "Special Seismic Loads"
    },
    "1068": {
      "TYPE": "Vertical Seismic Forces"
    },
    "1069": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/EQCT"

# 요소별 지진하중조합 타입 신규 배정 (POST)
payload = {
    "Assign": {
        "1066": {"TYPE": "Special Seismic Loads"},
        "1068": {"TYPE": "Vertical Seismic Forces"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
# 수정은 PUT, 삭제는 DELETE 사용
```

---

## 7. `DESIGN/RC/KDS-41-20-2022/ULCT` — 지하 하중조합 타입

> **기능:** 부재별로 지하(Underground) 하중조합 적용 여부를 배정합니다. true=지하하중용, false=비지하하중용.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/ULCT
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
| 1 | Assign 래퍼 (요소 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 지하 하중 여부 (true=지하하중용, false=비지하하중용) | `"bUNDERLOADTYPE"` | Boolean (oneOf) | `false` | 선택 |

### Request / Response JSON

**POST Request Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/ULCT"

# 요소별 지하 하중조합 타입 배정 (POST)
payload = {
    "Assign": {
        "885": {"bUNDERLOADTYPE": True},    # 지하하중 적용
        "888": {"bUNDERLOADTYPE": False},   # 비지하하중
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 8. `DESIGN/RC/KDS-41-20-2022/SUEQ` — 지진 스케일업 계수

> **기능:** 부재별로 하중케이스(LC) 및 하중조합(LCOM)의 축력·모멘트·전단 각각에 대한 지진 스케일업(증폭) 계수를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/SUEQ
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
| 1 | Assign 래퍼 (요소 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 하중케이스 축력 스케일 계수 | `"LC_AXIAL"` | Number | `1` | 선택 |
| 3 | 하중케이스 모멘트 스케일 계수 | `"LC_MOMENT"` | Number | `1` | 선택 |
| 4 | 하중케이스 전단 스케일 계수 | `"LC_SHEAR"` | Number | `1` | 선택 |
| 5 | 하중조합 축력 스케일 계수 | `"LCOM_AXIAL"` | Number | `1` | 선택 |
| 6 | 하중조합 모멘트 스케일 계수 | `"LCOM_MOMENT"` | Number | `1` | 선택 |
| 7 | 하중조합 전단 스케일 계수 | `"LCOM_SHEAR"` | Number | `1` | 선택 |

### Request / Response JSON

**POST Request Body**

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
    },
    "1057": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "1058": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2
    },
    "1059": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
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
    },
    "1057": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "1058": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2
    },
    "1059": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
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
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/SUEQ"

# 부재별 지진 스케일업 계수 배정 (POST)
payload = {
    "Assign": {
        "915": {
            "LC_AXIAL": 1.2, "LC_MOMENT": 1.2, "LC_SHEAR": 1.2,
            "LCOM_AXIAL": 1.2, "LCOM_MOMENT": 1.2, "LCOM_SHEAR": 1.2,
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 9. `DESIGN/RC/KDS-41-20-2022/SDGN` — 내진 설계 타입

> **기능:** 부재별 내진설계 타입을 배정합니다. 내진(Seismic)/비내진(Non-Seismic)/비내진 저항시스템(Non-Seismic-Force-Resisting) 중 선택합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/SDGN
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
      "description": "Keyed object (dictionary). Each property name is a member ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "NTYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "NTYPE": {
              "type": "string",
              "description": "Seismic design type assigned to the member.",
              "oneOf": [
                {
                  "title": "for Seismic Design",
                  "const": "Seismic"
                },
                {
                  "title": "for Non-Seismic Design",
                  "const": "Non-Seismic"
                },
                {
                  "title": "for Non-Seismic-Force Resisting System",
                  "const": "Non-Seismic-Force-Resisting"
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
| 1 | Assign 래퍼 (부재 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 내진 설계 타입 (Seismic / Non-Seismic / Non-Seismic-Force-Resisting) | `"NTYPE"` | String (oneOf) | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "1": {
      "NTYPE": "Seismic"
    },
    "2": {
      "NTYPE": "Non-Seismic"
    },
    "3": {
      "NTYPE": "Non-Seismic-Force-Resisting"
    }
  }
}
```

**GET Response Body**

```json
{
  "SDGN": {
    "1": {
      "NTYPE": "Seismic"
    },
    "2": {
      "NTYPE": "Non-Seismic"
    },
    "3": {
      "NTYPE": "Non-Seismic-Force-Resisting"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/SDGN"

# 부재별 내진 설계 타입 배정 (POST)
payload = {
    "Assign": {
        "1": {"NTYPE": "Seismic"},
        "2": {"NTYPE": "Non-Seismic"},
        "3": {"NTYPE": "Non-Seismic-Force-Resisting"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 10. `DESIGN/RC/KDS-41-20-2022/SCOL` — 내진 기둥 타입

> **기능:** 부재(기둥)별 층 타입을 배정합니다. 필로티(PILOTI) 또는 연약층(SOFT_STORY)으로 분류합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/SCOL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

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
      "description": "Object keyed by member ID strings (e.g., \"1059\"), where each value is a story type setting object.",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "TYPE"
          ],
          "properties": {
            "TYPE": {
              "type": "string",
              "description": "Story type classification.",
              "oneOf": [
                {
                  "title": "PILOTI",
                  "const": "PILOTI"
                },
                {
                  "title": "SOFT_STORY",
                  "const": "SOFT_STORY"
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
| 1 | Assign 래퍼 (부재 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 층 타입 (PILOTI / SOFT_STORY) | `"TYPE"` | String (oneOf) | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "915": {
      "TYPE": "PILOTI"
    },
    "916": {
      "TYPE": "SOFT_STORY"
    }
  }
}
```

**GET Response Body**

```json
{
  "SCOL": {
    "915": {
      "TYPE": "PILOTI"
    },
    "916": {
      "TYPE": "SOFT_STORY"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/SCOL"

# 기둥 부재의 내진 층 타입 배정 (POST)
payload = {
    "Assign": {
        "915": {"TYPE": "PILOTI"},
        "916": {"TYPE": "SOFT_STORY"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 11. `DESIGN/RC/KDS-41-20-2022/MBTP` — 부재 타입 수정

> **기능:** 요소별 설계 부재 타입을 기둥(COLUMN)/보(BEAM)/가새(BRACE)로 수정 배정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MBTP
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
| 1 | Assign 래퍼 (요소 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 부재 타입 (COLUMN=기둥, BEAM=보, BRACE=가새) | `"TYPE"` | String (oneOf) | — | **필수** |

### Request / Response JSON

**POST Request Body**

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
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MBTP"

# 요소별 설계 부재 타입 수정 (POST)
payload = {
    "Assign": {
        "934": {"TYPE": "BRACE"},
        "1058": {"TYPE": "COLUMN"},
        "1066": {"TYPE": "BEAM"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 12. `DESIGN/RC/KDS-41-20-2022/MEMB` — 부재 배정

> **기능:** 여러 요소를 하나의 설계 부재로 묶어 배정합니다. 요소 리스트와 국부좌표 방향 반전 여부를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MEMB
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
| 1 | Assign 래퍼 (부재 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 요소 리스트 | `"AELEM"` | Array[integer] | — | **필수** |
| 3 | 국부좌표 방향 반전 | `"bREVERSE"` | Boolean | `false` | 선택 |

### Request / Response JSON

**PUT Request Body**

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

**GET Response Body**

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
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MEMB"

# 요소들을 하나의 설계 부재로 배정 (PUT)
payload = {
    "Assign": {
        "1": {"AELEM": [885, 888, 891], "bREVERSE": True},
        "2": {"AELEM": [919]},
    }
}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 13. `DESIGN/RC/KDS-41-20-2022/MATD` — 콘크리트 재료 수정

> **기능:** 재질 ID별 콘크리트·철근 재료를 수정합니다. 표준코드(Standard) 또는 사용자정의(None)로 등급/강도/경량 계수를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MATD
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
            "CONCRETE",
            "REBAR"
          ],
          "additionalProperties": false,
          "properties": {
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
                  "description": "Concrete code type.",
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
                    {
                      "const": "C30",
                      "title": "C30"
                    },
                    {
                      "const": "C35",
                      "title": "C35"
                    },
                    {
                      "const": "C40",
                      "title": "C40"
                    },
                    {
                      "const": "C45",
                      "title": "C45"
                    },
                    {
                      "const": "C49",
                      "title": "C49"
                    },
                    {
                      "const": "C50",
                      "title": "C50"
                    },
                    {
                      "const": "C55",
                      "title": "C55"
                    },
                    {
                      "const": "C60",
                      "title": "C60"
                    },
                    {
                      "const": "C65",
                      "title": "C65"
                    },
                    {
                      "const": "C70",
                      "title": "C70"
                    },
                    {
                      "const": "C75",
                      "title": "C75"
                    },
                    {
                      "const": "C80",
                      "title": "C80"
                    },
                    {
                      "const": "C85",
                      "title": "C85"
                    },
                    {
                      "const": "C90",
                      "title": "C90"
                    },
                    {
                      "const": "C95",
                      "title": "C95"
                    }
                  ]
                },
                "FC": {
                  "type": "number",
                  "description": "Specified compressive strength (fc|fck) in kN/mm². User input when CODE is None. Auto-filled from the selected standard code and grade when CODE is Standard."
                },
                "LIGHTWEIGHT": {
                  "type": "boolean",
                  "description": "Whether the lightweight concrete factor (Lambda) is applied. Editable for both CODE=None and CODE=Standard.",
                  "default": false
                },
                "LAMBDA": {
                  "type": "number",
                  "description": "Lambda value. Editable for both CODE=None and CODE=Standard.",
                  "default": 1
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
            "REBAR": {
              "type": "object",
              "description": "Rebar material selection.",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Rebar code type.",
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
                  "description": "Rebar standard code when CODE is Standard. Currently only KS19(RC) is supported.",
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
                "FY": {
                  "type": "number",
                  "description": "Yield strength Fy of main rebar in kN/mm². User input when CODE is None. Auto-filled from the selected standard code and rebar grade when CODE is Standard."
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
                  "description": "Yield strength Fys of sub-rebar in kN/mm². User input when CODE is None. Auto-filled from the selected standard code and rebar grade when CODE is Standard."
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
                      "SUB_REBAR_NAME",
                      "FY",
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

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 (재질 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 콘크리트 재료 | `"CONCRETE"` | Object | — | **필수** |
| 2.1 | 코드 (None=사용자정의, Standard=표준) | `"CODE"` | String (oneOf) | — | **필수** |
| 2.2 | 경량콘크리트 계수(Lambda) 적용 | `"LIGHTWEIGHT"` | Boolean | `false` | 선택 |
| 2.3 | Lambda 값 | `"LAMBDA"` | Number | `1` | 선택 |
| 2.4 | 표준코드 (KS19(RC)) — CODE=Standard | `"STANDARD_CODE"` | String (oneOf) | — | 조건부 필수 |
| 2.5 | 콘크리트 등급 (C15~C95 중 택1) — CODE=Standard | `"GRADE"` | String (oneOf) | — | 조건부 필수 |
| 2.6 | 사용자정의 재료명 — CODE=None | `"NAME"` | String | — | 조건부 필수 |
| 2.7 | 설계 압축강도 fck (kN/mm²) — CODE=None 입력/Standard 자동 | `"FC"` | Number | — | 조건부 필수 |
| 3 | 철근 재료 | `"REBAR"` | Object | — | **필수** |
| 3.1 | 코드 (None=사용자정의, Standard=표준) | `"CODE"` | String (oneOf) | — | **필수** |
| 3.2 | 표준코드 (KS19(RC)) — CODE=Standard | `"STANDARD_CODE"` | String (oneOf) | — | 조건부 필수 |
| 3.3 | 주철근 등급 (SD300/SD400/SD500/SD600/SD700/SD400S/SD500S/SD600S) — Standard | `"MAIN_REBAR_GRADE"` | String (oneOf) | — | 조건부 필수 |
| 3.4 | 보조철근 등급 (SD300~SD600S) — Standard | `"SUB_REBAR_GRADE"` | String (oneOf) | — | 조건부 필수 |
| 3.5 | 주철근 재료명 — CODE=None | `"MAIN_REBAR_NAME"` | String | — | 조건부 필수 |
| 3.6 | 보조철근 재료명 — CODE=None | `"SUB_REBAR_NAME"` | String | — | 조건부 필수 |
| 3.7 | 주철근 항복강도 Fy (kN/mm²) — None 입력/Standard 자동 | `"FY"` | Number | — | 조건부 필수 |
| 3.8 | 보조철근 항복강도 Fys (kN/mm²) — None 입력/Standard 자동 | `"FYS"` | Number | — | 조건부 필수 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "CONCRETE": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C15",
        "LIGHTWEIGHT": true,
        "LAMBDA": 1
      },
      "REBAR": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD400S",
        "SUB_REBAR_GRADE": "SD600"
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "MATD": {
    "1": {
      "CONCRETE": {
        "CODE": "STANDARD",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C15",
        "LIGHTWEIGHT": true,
        "LAMBDA": 1
      },
      "REBAR": {
        "CODE": "STANDARD",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD400S",
        "SUB_REBAR_GRADE": "SD600"
      }
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MATD"

# 재질 ID 1의 콘크리트/철근 표준 재료 수정 (PUT)
payload = {
    "Assign": {
        "1": {
            "CONCRETE": {
                "CODE": "Standard",
                "STANDARD_CODE": "KS19(RC)",
                "GRADE": "C24",
                "LIGHTWEIGHT": False,
                "LAMBDA": 1,
            },
            "REBAR": {
                "CODE": "Standard",
                "STANDARD_CODE": "KS19(RC)",
                "MAIN_REBAR_GRADE": "SD400",
                "SUB_REBAR_GRADE": "SD400",
            },
        }
    }
}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 14. `DESIGN/RC/KDS-41-20-2022/LENG` — 비지지 길이(L, Lb)

> **기능:** 부재별 비지지 길이 Ly·Lz, 횡좌굴 비지지 길이 Lb, 비틀림 비지지 길이 Lt를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/LENG
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
| 1 | Assign 래퍼 (ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 비지지 길이 Ly | `"LY"` | Number | `0` | 선택 |
| 3 | 비지지 길이 Lz | `"LZ"` | Number | `0` | 선택 |
| 4 | 횡좌굴 비지지 길이 Lb | `"LB"` | Number | `0` | 선택 |
| 5 | 횡좌굴 비지지 길이 미고려 | `"bNOTUSE"` | Boolean | `false` | 선택 |
| 6 | 비틀림 비지지 길이 Lt | `"LT"` | Number | `0` | 선택 |

### Request / Response JSON

**POST Request Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/LENG"

# 부재별 비지지 길이 지정 (POST)
payload = {
    "Assign": {
        "888": {"LY": 3.0, "LZ": 3.0, "LB": 3.0, "bNOTUSE": False, "LT": 3.0},
        "891": {"LY": 4.0, "LZ": 4.0, "LB": 2.0},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 15. `DESIGN/RC/KDS-41-20-2022/KFAC` — 유효좌굴길이계수(K)

> **기능:** 부재별 유효좌굴길이계수 Ky·Kz·Kt를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/KFAC
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
| 1 | Assign 래퍼 (요소 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | Ky | `"Ky"` | Number | `1` | 선택 |
| 3 | Kz | `"Kz"` | Number | `1` | 선택 |
| 4 | Kt | `"Kt"` | Number | `1` | 선택 |

### Request / Response JSON

**POST Request Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/KFAC"

# 부재별 유효좌굴길이계수 K 지정 (POST)
payload = {
    "Assign": {
        "859": {"Ky": 1.0},
        "860": {"Ky": 2.0, "Kz": 2.0},
        "902": {"Kz": 3.0, "Kt": 3.0},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 16. `DESIGN/RC/KDS-41-20-2022/CMFT` — 등가모멘트 보정계수(Cm)

> **기능:** 부재별 등가모멘트 보정계수 CMy·CMz를 지정하거나 자동계산(OPT_AUTO)을 선택합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/CMFT
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
| 1 | Assign 래퍼 (요소 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 자동 계산 | `"OPT_AUTO"` | Boolean | `false` | 선택 |
| 3 | CMy | `"CMY"` | Number | `0` | 선택 |
| 4 | CMz | `"CMZ"` | Number | `0` | 선택 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "1067": {
      "OPT_AUTO": true
    },
    "1068": {
      "OPT_AUTO": true
    },
    "1069": {
      "CMY": 0.7,
      "CMZ": 0.6
    },
    "1070": {
      "CMY": 0.72,
      "CMZ": 0.85
    },
    "1071": {
      "CMY": 0.8,
      "CMZ": 0.8
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
    "1068": {
      "OPT_AUTO": true
    },
    "1069": {
      "CMY": 0.7,
      "CMZ": 0.6
    },
    "1070": {
      "CMY": 0.72,
      "CMZ": 0.85
    },
    "1071": {
      "CMY": 0.8,
      "CMZ": 0.8
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/CMFT"

# 등가모멘트 보정계수 Cm 지정 (POST): 일부는 자동, 일부는 수동값
payload = {
    "Assign": {
        "1067": {"OPT_AUTO": True},              # 자동 계산
        "1069": {"CMY": 0.7, "CMZ": 0.6},        # 수동 입력
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 17. `DESIGN/RC/KDS-41-20-2022/FMAG` — 모멘트 확대계수(B1/δb, B2/δs)

> **기능:** 부재별 모멘트 확대계수를 지정합니다. B1(δb)은 1차(비횡변위) 모멘트, B2(δs)는 2차(횡변위) 모멘트에 대한 계수입니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/FMAG
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
| 1 | Assign 래퍼 (요소 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | B1y - δby (Y축 1차 모멘트 확대) | `"B1Y_DELTA_BY"` | Number | `1` | 선택 |
| 3 | B1z - δbz (Z축 1차 모멘트 확대) | `"B1Z_DELTA_BZ"` | Number | `1` | 선택 |
| 4 | B2y - δsy (Y축 2차 모멘트 확대) | `"B2Y_DELTA_SY"` | Number | `1` | 선택 |
| 5 | B2z - δsz (Z축 2차 모멘트 확대) | `"B2Z_DELTA_SZ"` | Number | `1` | 선택 |

### Request / Response JSON

**POST Request Body**

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
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/FMAG"

# 부재별 모멘트 확대계수 지정 (POST)
payload = {
    "Assign": {
        "915": {"B1Y_DELTA_BY": 1.1, "B1Z_DELTA_BZ": 1.2},
        "1058": {"B2Y_DELTA_SY": 1.3, "B2Z_DELTA_SZ": 1.4},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 18. `DESIGN/RC/KDS-41-20-2022/MLLR` — 활하중 저감계수 수정

> **기능:** 부재별 활하중 저감계수와 적용 성분(축력/모멘트/전단)을 개별 수정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MLLR
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
| 1 | Assign 래퍼 (요소 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 저감계수 (≥0.3, ≤1) | `"FACTOR"` | Number | `1` | 선택 |
| 3 | 적용 성분 | `"COMPONENTS"` | Object | — | 선택 |
| 3.1 | 축력 | `"AXIAL"` | Boolean | `false` | 선택 |
| 3.2 | 모멘트 | `"MOMENT"` | Boolean | `false` | 선택 |
| 3.3 | 전단력 | `"SHEAR"` | Boolean | `false` | 선택 |

### Request / Response JSON

**POST Request Body**

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
    },
    "1057": {
      "FACTOR": null,
      "COMPONENTS": {
        "MOMENT": true
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
    },
    "1057": {
      "COMPONENTS": {
        "MOMENT": true
      }
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MLLR"

# 부재별 활하중 저감계수 수정 (POST)
payload = {
    "Assign": {
        "922": {"COMPONENTS": {"AXIAL": False, "MOMENT": True, "SHEAR": False}},
        "934": {"FACTOR": 0.9, "COMPONENTS": {"AXIAL": True}},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 19. `DESIGN/RC/KDS-41-20-2022/HCBM` — 헌치보 배정

> **기능:** 헌치보(Haunched Beam)를 Part A/B/C 요소 구성으로 배정합니다. 각 파트는 요소 ID 목록(KEYS) 또는 ID 범위(TO)로 지정하며, 설계 위치 타입(Part 1/2 또는 User)을 선택합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/HCBM
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
| 1 | Assign 래퍼 (ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 헌치 이름 | `"NAME"` | String | — | **필수** |
| 3 | Part A 요소 입력 (방식 1개만 사용) | `"PART_A"` | Object | — | **필수** |
| 3.1 | 입력 방식 (KEYS=개별 ID, TO=ID 범위) | `"INPUT_METHOD"` | String (oneOf) | — | **필수** |
| 3.2 | 개별 요소 ID (INPUT_METHOD=KEYS, 최소 1개) | `"KEYS"` | Array[integer] | — | 조건부 |
| 3.3 | ID 범위 (예 "101 to 105") (INPUT_METHOD=TO) | `"TO"` | String | — | 조건부 |
| 4 | Part B 요소 입력 (구조는 Part A와 동일) | `"PART_B"` | Object | — | **필수** |
| 5 | Part C 요소 입력 (구조는 Part A와 동일) | `"PART_C"` | Object | — | **필수** |
| 6 | 설계 위치 타입 (0=Part 1/2, 1=User) | `"POS_TYPE"` | Integer (oneOf) | — | **필수** |
| 7 | 사용자 정의 L1 거리 (POS_TYPE=1일 때) | `"L1"` | Number | `1` | 선택 |
| 8 | 사용자 정의 L2 거리 (POS_TYPE=1일 때) | `"L2"` | Number | `1` | 선택 |

### Request / Response JSON

**POST Request Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/HCBM"

# 헌치보 배정 (POST): Part A=개별 ID, Part B=범위, Part C=개별 ID
payload = {
    "Assign": {
        "1": {
            "NAME": "h1",
            "POS_TYPE": 0,                       # Part 1/2 자동 위치
            "PART_A": {"INPUT_METHOD": "KEYS", "KEYS": [1065]},
            "PART_B": {"INPUT_METHOD": "TO", "TO": "1066to1071"},
            "PART_C": {"INPUT_METHOD": "KEYS", "KEYS": [1072]},
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 20. `DESIGN/RC/KDS-41-20-2022/MRFT` — 모멘트 재분배 계수

> **기능:** 보 부재별 모멘트 재분배 계수를 지정합니다. 보(Beam) 부재 타입에만 적용됩니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MRFT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "description": "Design Parameters - Moment Redistribution Factor (MRFT). Only Beam Member Type is applicable. Supported methods: POST, GET, PUT, DELETE.",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by beam member ID strings (e.g., \"859\"), where each entry represents a moment redistribution factor assigned to the member. Only Beam Member Type is applicable.",
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
              "description": "Moment redistribution factor assigned to the member.",
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

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 (보 부재 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 모멘트 재분배 계수 (>0, ≤1) | `"FACTOR"` | Number | `1` | 선택 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "885": {
      "FACTOR": 1
    },
    "888": {
      "FACTOR": 0.01
    }
  }
}
```

**GET Response Body**

```json
{
  "MRFT": {
    "885": {
      "FACTOR": 1
    },
    "888": {
      "FACTOR": 0.01
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MRFT"

# 보 부재별 모멘트 재분배 계수 지정 (POST) — Beam 타입만 유효
payload = {
    "Assign": {
        "885": {"FACTOR": 1.0},
        "888": {"FACTOR": 0.9},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 21. `DESIGN/RC/KDS-41-20-2022/TRFT` — 비틀림 감소계수

> **기능:** 보 부재별 비틀림 감소계수를 지정합니다. 보(Beam) 부재 타입에만 적용됩니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/TRFT
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
      "description": "Object keyed by beam member ID strings (e.g., \"859\"), where each entry assigns a torsion reduction factor. Only Beam Member Type is applicable.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "FACTOR"
          ],
          "additionalProperties": false,
          "properties": {
            "FACTOR": {
              "type": "number",
              "description": "Torsion reduction factor applied to the member.",
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

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Assign 래퍼 (보 부재 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 비틀림 감소계수 (>0, ≤1) | `"FACTOR"` | Number | `1` | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "888": {
      "FACTOR": 1
    }
  }
}
```

**GET Response Body**

```json
{
  "TRFT": {
    "888": {
      "FACTOR": 1
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/TRFT"

# 보 부재별 비틀림 감소계수 지정 (POST)
payload = {"Assign": {"888": {"FACTOR": 1.0}}}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
# 수정: requests.put(...) / 삭제: requests.delete(...)
```

---

## 22. `DESIGN/RC/KDS-41-20-2022/MCMB` — 보 모멘트 산정 방법

> **기능:** 보 부재별 모멘트 산정 방법을 지정합니다. Each(각 경간별) 또는 Equivalent Frame(등가 골조) 중 선택합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MCMB
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
      "description": "Object keyed by member ID strings (e.g., \"1\"), where each entry represents the moment calculation method assigned to the beam member.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "CALC_METHOD"
          ],
          "additionalProperties": false,
          "properties": {
            "CALC_METHOD": {
              "type": "string",
              "description": "Moment calculation method for the beam member.",
              "oneOf": [
                {
                  "title": "Each Span",
                  "const": "EACH"
                },
                {
                  "title": "Equivalent Frame",
                  "const": "EQUI"
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
| 1 | Assign 래퍼 (부재 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 모멘트 산정 방법 (EACH=각 경간, EQUI=등가 골조) | `"CALC_METHOD"` | String (oneOf) | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "888": {
      "CALC_METHOD": "EACH"
    }
  }
}
```

**GET Response Body**

```json
{
  "MCMB": {
    "888": {
      "CALC_METHOD": "EACH"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MCMB"

# 보 부재별 모멘트 산정 방법 지정 (POST)
payload = {"Assign": {"888": {"CALC_METHOD": "EACH"}}}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 23. `DESIGN/RC/KDS-41-20-2022/DFBA` — 부재 배정된 보 설계력

> **기능:** 부재로 배정된 보의 설계력 타입을 지정합니다. Subdivided Forces(세분화 부재력) 또는 Member Forces(부재력) 중 선택합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DFBA
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
      "description": "Object keyed by member ID strings (e.g., \"1\"), where each entry represents the design force type assigned to the beam member.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "FORCE_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "FORCE_TYPE": {
              "type": "string",
              "description": "Design force type for the beam member.",
              "oneOf": [
                {
                  "title": "Subdivided Forces",
                  "const": "Subdivided Forces"
                },
                {
                  "title": "Member Forces",
                  "const": "Member Forces"
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
| 1 | Assign 래퍼 (부재 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 설계력 타입 (Subdivided Forces / Member Forces) | `"FORCE_TYPE"` | String (oneOf) | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "859": {
      "FORCE_TYPE": "Subdivided Forces"
    },
    "860": {
      "FORCE_TYPE": "Member Forces"
    }
  }
}
```

**GET Response Body**

```json
{
  "DFBA": {
    "859": {
      "FORCE_TYPE": "Subdivided Forces"
    },
    "860": {
      "FORCE_TYPE": "Member Forces"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DFBA"

# 부재 배정된 보의 설계력 타입 지정 (POST)
payload = {
    "Assign": {
        "859": {"FORCE_TYPE": "Subdivided Forces"},
        "860": {"FORCE_TYPE": "Member Forces"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 24. `DESIGN/RC/KDS-41-20-2022/PMDM` — P-M 곡선 산정 방법

> **기능:** 부재별 P-M 상관도(interaction) 설계 산정 방법을 지정합니다. P(축력 고정) 또는 M/P(모멘트/축력비 고정) 중 선택합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/PMDM
```

### Active Methods

`POST` · `GET` · `DELETE` · `PUT`

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
      "description": "Object keyed by member ID strings (e.g., \"1059\"), where each value is a PMDM setting object.",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "CALC_METHOD"
          ],
          "properties": {
            "CALC_METHOD": {
              "type": "string",
              "description": "Calculation method for PM interaction design.",
              "oneOf": [
                {
                  "title": "P",
                  "const": "P"
                },
                {
                  "title": "M/P",
                  "const": "M/P"
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
| 1 | Assign 래퍼 (부재 ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 산정 방법 (P=축력 고정, M/P=M·P비 고정) | `"CALC_METHOD"` | String (oneOf) | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "915": {
      "CALC_METHOD": "P"
    }
  }
}
```

**GET Response Body**

```json
{
  "PMDM": {
    "915": {
      "CALC_METHOD": "P"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/PMDM"

# 부재별 P-M 곡선 산정 방법 지정 (POST)
payload = {"Assign": {"915": {"CALC_METHOD": "P"}}}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 25. `DESIGN/RC/KDS-41-20-2022/WMAK` — 벽체 마크 데이터 수정

> **기능:** 벽체 마크(Wall Mark)를 정의합니다. 마크 이름과 대상 벽체 ID 목록을 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/WMAK
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "title": "Modify Wall Mark Data (WMAK)",
  "description": "POST /DESIGN/RC/KDS-41-20-2022/WMAK — Design Parameters - Modify Wall Mark Data",
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
          "title": "Modify Wall Mark Data",
          "type": "object",
          "required": [
            "MARKNAME",
            "WID_LIST"
          ],
          "additionalProperties": false,
          "properties": {
            "MARKNAME": {
              "type": "string",
              "description": "Wall mark name",
              "minLength": 1
            },
            "WID_LIST": {
              "type": "array",
              "description": "Target wall IDs",
              "items": {
                "type": "integer"
              },
              "minItems": 1
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
| 2 | 벽체 마크 이름 (최소 1자) | `"MARKNAME"` | String | — | **필수** |
| 3 | 대상 벽체 ID 목록 (최소 1개) | `"WID_LIST"` | Array[integer] | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "1": {
      "MARKNAME": "W200",
      "WID_LIST": [
        1,
        2
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "WMAK": {
    "1": {
      "MARKNAME": "W200",
      "WID_LIST": [
        1,
        2
      ]
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/WMAK"

# 벽체 마크 정의 (POST): 벽체 1,2를 마크 "W200"으로 묶음
payload = {"Assign": {"1": {"MARKNAME": "W200", "WID_LIST": [1, 2]}}}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 26. `DESIGN/RC/KDS-41-20-2022/BEMW` — 벽체ID별 경계요소법

> **기능:** 벽체별 경계요소법(Boundary Element Method) 사용 여부와 방식(변위/응력 기반), 최하층 지정 여부 및 층 이름을 설정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/BEMW
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

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
      "description": "Object keyed by index strings (e.g., \"1\"), where each value is a boundary element wall setting object.",
      "minProperties": 1,
      "maxProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "BBNDR_ELEM_METHOD": {
              "type": "boolean",
              "description": "Whether to use boundary element method."
            },
            "NMETHOD_TYPE": {
              "type": "string",
              "description": "Boundary element method type.",
              "oneOf": [
                {
                  "title": "Displacement Based Method",
                  "const": "Displacement Based Method"
                },
                {
                  "title": "Stress Based Method",
                  "const": "Stress Based Method"
                }
              ]
            },
            "BBOT_STOR": {
              "type": "boolean",
              "description": "Whether to use bottom story setting."
            },
            "STOR_NAME": {
              "type": "string",
              "description": "Story name."
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
| 1 | Assign 래퍼 (인덱스 문자열 키, 1개) | `"Assign"` | Object | — | **필수** |
| 2 | 경계요소법 사용 여부 | `"BBNDR_ELEM_METHOD"` | Boolean | — | 선택 |
| 3 | 최하층 설정 사용 여부 | `"BBOT_STOR"` | Boolean | — | 선택 |
| 4 | 방식 타입 (Displacement Based Method / Stress Based Method) — BBNDR_ELEM_METHOD=true | `"NMETHOD_TYPE"` | String (oneOf) | — | 선택 |
| 5 | 층 이름 (BBOT_STOR=true일 때) | `"STOR_NAME"` | String | — | 선택 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "1": {
      "NMETHOD_TYPE": "Displacement Based Method",
      "BBNDR_ELEM_METHOD": true,
      "BBOT_STOR": true,
      "STOR_NAME": "B2"
    }
  }
}
```

**GET Response Body**

```json
{
  "BEMW": {
    "1": {
      "BBNDR_ELEM_METHOD": true,
      "NMETHOD_TYPE": "Displacement Based Method",
      "BBOT_STOR": true,
      "STOR_NAME": "B2"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BEMW"

# 벽체별 경계요소법 설정 (POST): 변위기반, 최하층 B2
payload = {
    "Assign": {
        "1": {
            "BBNDR_ELEM_METHOD": True,
            "NMETHOD_TYPE": "Displacement Based Method",
            "BBOT_STOR": True,
            "STOR_NAME": "B2",
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 27. `DESIGN/RC/KDS-41-20-2022/REXC` — 철근 노출 조건

> **기능:** 부재별 철근 노출 조건(Rebar Exposure Condition)을 지정합니다. Dry(건조) 또는 Etc(기타) 중 선택합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/REXC
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
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "EXPOSURE"
          ],
          "additionalProperties": false,
          "properties": {
            "EXPOSURE": {
              "type": "string",
              "description": "Rebar exposure condition.",
              "default": "Dry",
              "oneOf": [
                {
                  "const": "Etc",
                  "title": "Etc"
                },
                {
                  "const": "Dry",
                  "title": "Dry"
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
| 1 | Assign 래퍼 (ID 문자열 키) | `"Assign"` | Object | — | **필수** |
| 2 | 노출 조건 (Dry=건조, Etc=기타) | `"EXPOSURE"` | String (oneOf) | `"Dry"` | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "17": {
      "EXPOSURE": "Dry"
    },
    "49": {
      "EXPOSURE": "Etc"
    }
  }
}
```

**GET Response Body**

```json
{
  "REXC": {
    "17": {
      "EXPOSURE": "Dry"
    },
    "49": {
      "EXPOSURE": "Etc"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/REXC"

# 부재별 철근 노출 조건 지정 (POST)
payload = {
    "Assign": {
        "17": {"EXPOSURE": "Dry"},
        "49": {"EXPOSURE": "Etc"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 28. `DESIGN/RC/KDS-41-20-2022/LMRR` — 최대 철근비 제한

> **기능:** 설계별 최대 철근비 상한을 설정합니다. 전단벽(Rhow)·기둥(Rhoc)·가새(Rhor) 각각의 최대 철근비를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/LMRR
```

### Active Methods

`GET` · `PUT` · `DELETE`

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
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "minProperties": 1,
      "maxProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "RHOR",
            "RHOC",
            "RHOW"
          ],
          "properties": {
            "RHOW": {
              "type": "number",
              "description": "Maximum rebar ratio for Shear Wall Design (Rhow)."
            },
            "RHOC": {
              "type": "number",
              "description": "Maximum rebar ratio for Column Design (Rhoc)."
            },
            "RHOR": {
              "type": "number",
              "description": "Maximum rebar ratio for Brace Design (Rhor)."
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
| 1 | Assign 래퍼 (ID 문자열 키, 1개) | `"Assign"` | Object | — | **필수** |
| 2 | 전단벽 설계 최대 철근비 Rhow | `"RHOW"` | Number | — | **필수** |
| 3 | 기둥 설계 최대 철근비 Rhoc | `"RHOC"` | Number | — | **필수** |
| 4 | 가새 설계 최대 철근비 Rhor | `"RHOR"` | Number | — | **필수** |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "RHOW": 0.04,
      "RHOC": 0.03,
      "RHOR": 0.03
    }
  }
}
```

**GET Response Body**

```json
{
  "LMRR": {
    "1": {
      "RHOR": 0.03,
      "RHOC": 0.03,
      "RHOW": 0.04
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/LMRR"

# 최대 철근비 제한 설정 (PUT)
payload = {"Assign": {"1": {"RHOW": 0.04, "RHOC": 0.03, "RHOR": 0.03}}}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```



---

## 29. `DESIGN/RC/KDS-41-20-2022/DCRM-BEAM` — 보 부재별 철근 설계기준

> **기능:** 보(Beam) **부재 ID별**로 철근 설계기준(주철근·스터럽·다리 수·측면철근·피복·복철근·간격제한·이음)을 개별 지정합니다. 전역 기준(`DCRE`)을 특정 부재에 덮어쓸 때 사용합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCRM-BEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 규격/배열 enum은 반복 값이 많아 축약했습니다. 실제 스키마에서 철근 규격은 `oneOf`(title=const) 형식의 **19종(D4 ~ D57)**, 스터럽 다리 수는 **19종(2 ~ 20)** 이 전부 나열됩니다. 아래 `enum` 은 앞 5개만 표기합니다.

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "부재 ID 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "description": "보 부재별 철근 규격·배근",
          "required": ["MAIN_REBAR", "STIRRUPS", "STIRRUP_ARRANGEMENT", "SIDE_BAR"],
          "additionalProperties": false,
          "properties": {
            "MAIN_REBAR": { "type": "string", "description": "주철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "STIRRUPS": { "type": "string", "description": "스터럽(전단철근) 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "STIRRUP_ARRANGEMENT": { "type": "integer", "description": "스터럽 다리(leg) 수 (전체 19종: 2 ~ 20)", "enum": [2, 3, 4, 5, 6] },
            "SIDE_BAR": { "type": "string", "description": "측면철근(side bar) 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "DT": { "type": "number", "description": "상단 피복 거리 dT", "default": 0 },
            "DB": { "type": "number", "description": "하단 피복 거리 dB", "default": 0 },
            "DOUBLY_REBAR": { "type": "boolean", "description": "복철근 설계 사용", "default": true },
            "DOUBLY_K": { "type": "number", "description": "복철근 k 계수", "default": 1 },
            "SPACING_LIMIT": { "type": "boolean", "description": "철근 간격 제한 고려", "default": true },
            "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
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
| 1 | 부재 ID 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **필수** |
| 2 | 주철근 규격 · 19종 (D4 ~ D57) | `"MAIN_REBAR"` | String (enum) | — | **필수** |
| 3 | 스터럽(전단철근) 규격 · 19종 (D4 ~ D57) | `"STIRRUPS"` | String (enum) | — | **필수** |
| 4 | 스터럽 다리 수 · 2 ~ 20 | `"STIRRUP_ARRANGEMENT"` | Integer (enum) | — | **필수** |
| 5 | 측면철근 규격 · 19종 (D4 ~ D57) | `"SIDE_BAR"` | String (enum) | — | **필수** |
| 6 | 상단 피복 거리 dT | `"DT"` | Number | `0` | 선택 |
| 7 | 하단 피복 거리 dB | `"DB"` | Number | `0` | 선택 |
| 8 | 복철근 설계 사용 | `"DOUBLY_REBAR"` | Boolean | `true` | 선택 |
| 9 | 복철근 k 계수 | `"DOUBLY_K"` | Number | `1` | 선택 |
| 10 | 철근 간격 제한 고려 | `"SPACING_LIMIT"` | Boolean | `true` | 선택 |
| 11 | 이음 옵션 (`None` \| `50%` \| `100%`) | `"SPLICED_BARS"` | String (enum) | `"50%"` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "885": {
      "MAIN_REBAR": "D4",
      "STIRRUPS": "D4",
      "STIRRUP_ARRANGEMENT": 4,
      "SIDE_BAR": "D4",
      "DT": 0.05,
      "DB": 0.05,
      "DOUBLY_REBAR": true,
      "DOUBLY_K": 1,
      "SPACING_LIMIT": true,
      "SPLICED_BARS": "50%"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCRMB": {
    "885": {
      "MAIN_REBAR": "D4",
      "STIRRUPS": "D4",
      "STIRRUP_ARRANGEMENT": 4,
      "SIDE_BAR": "D4",
      "DT": 0.05,
      "DB": 0.05,
      "DOUBLY_REBAR": true,
      "DOUBLY_K": 1,
      "SPACING_LIMIT": true,
      "SPLICED_BARS": "50%"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCRM-BEAM"

# 1) 보 부재 885 철근 기준 지정 (POST)
payload = {
    "Assign": {
        "885": {
            "MAIN_REBAR": "D22",          # 주철근 규격
            "STIRRUPS": "D10",            # 스터럽 규격
            "STIRRUP_ARRANGEMENT": 4,     # 스터럽 다리 수
            "SIDE_BAR": "D13",            # 측면철근 규격
            "DT": 0.05, "DB": 0.05,       # 상·하단 피복
            "DOUBLY_REBAR": True, "DOUBLY_K": 1,
            "SPACING_LIMIT": True,
            "SPLICED_BARS": "50%",        # 이음 옵션
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)

# 2) 조회 (GET) → 최상위 키는 "DCRMB"
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 수정(PUT) / 삭제(DELETE)
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 30. `DESIGN/RC/KDS-41-20-2022/DCRM-COLUMN` — 기둥 부재별 철근 설계기준

> **기능:** 기둥(Column) **부재 ID별**로 철근 설계기준(주철근·띠철근/나선철근·Y/Z 방향 다리 수·피복·간격제한·이음)을 개별 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCRM-COLUMN
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 철근 규격 enum은 **19종(D4 ~ D57)**, 다리 수 enum은 **19종(2 ~ 20)** 이 전부 나열되나 아래는 앞 5개만 표기합니다.

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "부재 ID 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "description": "기둥 부재별 철근 규격·배근",
          "required": ["MAIN_REBAR", "TIES_SPIRALS", "ARRANGEMENT_Y", "ARRANGEMENT_Z"],
          "additionalProperties": false,
          "properties": {
            "MAIN_REBAR": { "type": "string", "description": "주철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "TIES_SPIRALS": { "type": "string", "description": "띠철근/나선철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "ARRANGEMENT_Y": { "type": "integer", "description": "띠철근 다리 수 (local Y) (전체 19종: 2 ~ 20)", "enum": [2, 3, 4, 5, 6] },
            "ARRANGEMENT_Z": { "type": "integer", "description": "띠철근 다리 수 (local Z) (전체 19종: 2 ~ 20)", "enum": [2, 3, 4, 5, 6] },
            "DO": { "type": "number", "description": "주철근 중심까지 피복 거리 do", "default": 0 },
            "SPACING_LIMIT": { "type": "boolean", "description": "철근 간격 제한 고려", "default": true },
            "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
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
| 1 | 부재 ID 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **필수** |
| 2 | 주철근 규격 · 19종 (D4 ~ D57) | `"MAIN_REBAR"` | String (enum) | — | **필수** |
| 3 | 띠철근/나선철근 규격 · 19종 (D4 ~ D57) | `"TIES_SPIRALS"` | String (enum) | — | **필수** |
| 4 | 띠철근 다리 수 (local Y) · 2 ~ 20 | `"ARRANGEMENT_Y"` | Integer (enum) | — | **필수** |
| 5 | 띠철근 다리 수 (local Z) · 2 ~ 20 | `"ARRANGEMENT_Z"` | Integer (enum) | — | **필수** |
| 6 | 주철근 중심까지 피복 거리 do | `"DO"` | Number | `0` | 선택 |
| 7 | 철근 간격 제한 고려 | `"SPACING_LIMIT"` | Boolean | `true` | 선택 |
| 8 | 이음 옵션 (`None` \| `50%` \| `100%`) | `"SPLICED_BARS"` | String (enum) | `"50%"` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "MAIN_REBAR": "D4",
      "TIES_SPIRALS": "D4",
      "ARRANGEMENT_Y": 2,
      "ARRANGEMENT_Z": 2,
      "DO": 0.05,
      "SPACING_LIMIT": true,
      "SPLICED_BARS": "50%"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCRMC": {
    "915": {
      "MAIN_REBAR": "D4",
      "TIES_SPIRALS": "D4",
      "ARRANGEMENT_Y": 2,
      "ARRANGEMENT_Z": 2,
      "DO": 0.05,
      "SPACING_LIMIT": true,
      "SPLICED_BARS": "50%"
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCRM-COLUMN"

# 기둥 부재 915 철근 기준 지정 (POST)
payload = {
    "Assign": {
        "915": {
            "MAIN_REBAR": "D22",
            "TIES_SPIRALS": "D10",
            "ARRANGEMENT_Y": 3,   # Y 방향 띠철근 다리 수
            "ARRANGEMENT_Z": 3,   # Z 방향 띠철근 다리 수
            "DO": 0.05,
            "SPACING_LIMIT": True,
            "SPLICED_BARS": "50%",
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 최상위 키 "DCRMC"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 31. `DESIGN/RC/KDS-41-20-2022/DCRM-BRACE` — 가새 부재별 철근 설계기준

> **기능:** 가새(Brace) **부재 ID별**로 철근 설계기준을 지정합니다. 필드 구성은 기둥(`DCRM-COLUMN`)과 동일합니다(주철근·띠철근·Y/Z 다리 수·피복·간격제한·이음).

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCRM-BRACE
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 철근 규격 enum은 **19종(D4 ~ D57)**, 다리 수 enum은 **19종(2 ~ 20)** 이며 아래는 앞 5개만 표기합니다.

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "부재 ID 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "description": "가새 부재별 철근 규격·배근",
          "required": ["MAIN_REBAR", "TIES_SPIRALS", "ARRANGEMENT_Y", "ARRANGEMENT_Z"],
          "additionalProperties": false,
          "properties": {
            "MAIN_REBAR": { "type": "string", "description": "주철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "TIES_SPIRALS": { "type": "string", "description": "띠철근/나선철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "ARRANGEMENT_Y": { "type": "integer", "description": "띠철근 다리 수 (local Y) (전체 19종: 2 ~ 20)", "enum": [2, 3, 4, 5, 6] },
            "ARRANGEMENT_Z": { "type": "integer", "description": "띠철근 다리 수 (local Z) (전체 19종: 2 ~ 20)", "enum": [2, 3, 4, 5, 6] },
            "DO": { "type": "number", "description": "주철근 중심까지 피복 거리 do", "default": 0 },
            "SPACING_LIMIT": { "type": "boolean", "description": "철근 간격 제한 고려", "default": true },
            "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
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
| 1 | 부재 ID 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **필수** |
| 2 | 주철근 규격 · 19종 (D4 ~ D57) | `"MAIN_REBAR"` | String (enum) | — | **필수** |
| 3 | 띠철근/나선철근 규격 · 19종 (D4 ~ D57) | `"TIES_SPIRALS"` | String (enum) | — | **필수** |
| 4 | 띠철근 다리 수 (local Y) · 2 ~ 20 | `"ARRANGEMENT_Y"` | Integer (enum) | — | **필수** |
| 5 | 띠철근 다리 수 (local Z) · 2 ~ 20 | `"ARRANGEMENT_Z"` | Integer (enum) | — | **필수** |
| 6 | 주철근 중심까지 피복 거리 do | `"DO"` | Number | `0` | 선택 |
| 7 | 철근 간격 제한 고려 | `"SPACING_LIMIT"` | Boolean | `true` | 선택 |
| 8 | 이음 옵션 (`None` \| `50%` \| `100%`) | `"SPLICED_BARS"` | String (enum) | `"50%"` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "934": {
      "MAIN_REBAR": "D4",
      "TIES_SPIRALS": "D4",
      "ARRANGEMENT_Y": 2,
      "ARRANGEMENT_Z": 2,
      "SPLICED_BARS": "50%",
      "DO": 0.05,
      "SPACING_LIMIT": true
    }
  }
}
```

**GET Response Body**

```json
{
  "DCRMR": {
    "934": {
      "MAIN_REBAR": "D4",
      "TIES_SPIRALS": "D4",
      "ARRANGEMENT_Y": 2,
      "ARRANGEMENT_Z": 2,
      "SPLICED_BARS": "50%",
      "DO": 0.05,
      "SPACING_LIMIT": true
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCRM-BRACE"

# 가새 부재 934 철근 기준 지정 (POST)
payload = {
    "Assign": {
        "934": {
            "MAIN_REBAR": "D22",
            "TIES_SPIRALS": "D10",
            "ARRANGEMENT_Y": 2,
            "ARRANGEMENT_Z": 2,
            "DO": 0.05,
            "SPACING_LIMIT": True,
            "SPLICED_BARS": "50%",
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 최상위 키 "DCRMR"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 32. `DESIGN/RC/KDS-41-20-2022/DCRM-WALL` — 벽체 부재별 철근 설계기준

> **기능:** 벽체(Wall) **ID별**로, 그리고 각 ID 내에서 **층(Story)별**로 철근 설계기준(수직·수평·단부 철근, 경계요소 수평철근, 경계요소 수평/수직 간격, 피복 de/dw)을 개별 지정합니다. 각 벽체 ID는 층별 항목 배열 `"ITEMS"` 를 가지며, 배열의 각 항목이 층 이름(`"STORY"`)과 해당 층의 철근 규격 필드를 함께 포함합니다.
>
> ℹ️ **2026-07-21 반영(구조 변경):** 공식 매뉴얼 스키마가 벽체 ID당 단일 철근 규격 객체(플랫 구조: `Assign.{벽체ID}.{VERTICAL_REBAR, HORIZONTAL_REBAR, END_REBAR, BE_HORZ_REBAR, BE_HORZ_SPACE, BE_VERT_SPACE, DE, DW}`)에서, **층별 항목 배열** `Assign.{벽체ID}.ITEMS[]` 구조로 변경되었습니다. `ITEMS` 는 벽체 ID 아래의 새로운 필수 키이며, 배열의 각 항목은 신규 필수 필드 `"STORY"`(문자열)와 함께 기존 철근/간격 필드를 항목 내부에 포함합니다. 기존 플랫 구조는 더 이상 유효하지 않으므로, 이 스키마로 연동 코드를 작성했다면 반드시 갱신이 필요합니다. GET 응답 최상위 키(`"DCRMW"`)와 Active Methods(POST/GET/PUT/DELETE)는 변경되지 않았습니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCRM-WALL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 철근 규격 enum은 **19종(D4 ~ D57)** 이며 아래는 앞 5개만 표기합니다.

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "벽체 ID 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "description": "벽체별 층(Story)별 배근 지정",
          "required": ["ITEMS"],
          "additionalProperties": false,
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "해당 벽체 ID의 층별 지정 목록",
              "minItems": 1,
              "items": {
                "type": "object",
                "description": "층별 벽체 철근 규격·배근",
                "required": ["STORY", "VERTICAL_REBAR", "HORIZONTAL_REBAR", "END_REBAR", "BE_HORZ_REBAR", "BE_HORZ_SPACE", "BE_VERT_SPACE"],
                "additionalProperties": false,
                "properties": {
                  "STORY": { "type": "string", "description": "층 이름", "minLength": 1 },
                  "VERTICAL_REBAR": { "type": "string", "description": "수직 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                  "HORIZONTAL_REBAR": { "type": "string", "description": "수평 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                  "END_REBAR": { "type": "string", "description": "단부 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                  "BE_HORZ_REBAR": { "type": "string", "description": "경계요소 수평 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                  "BE_HORZ_SPACE": { "type": "number", "description": "경계요소 수평 철근 간격" },
                  "BE_VERT_SPACE": { "type": "number", "description": "경계요소 수직 철근 간격" },
                  "DE": { "type": "number", "description": "단부 피복 거리 de (m)", "default": 0 },
                  "DW": { "type": "number", "description": "벽면 피복 거리 dw (m)", "default": 0 }
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

**Root / Item**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | 벽체 ID 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **필수** |
| 2 | 해당 벽체 ID의 층별 지정 목록 (min 1) | `"ITEMS"` | Array[Object] | — | **필수** |

**`ITEMS` 배열 항목 (층별 배근 지정)**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| a | 층 이름 (최소 1자) | `"STORY"` | String | — | **필수** |
| b | 수직 철근 규격 · 19종 (D4 ~ D57) | `"VERTICAL_REBAR"` | String (enum) | — | **필수** |
| c | 수평 철근 규격 · 19종 (D4 ~ D57) | `"HORIZONTAL_REBAR"` | String (enum) | — | **필수** |
| d | 단부 철근 규격 · 19종 (D4 ~ D57) | `"END_REBAR"` | String (enum) | — | **필수** |
| e | 경계요소 수평 철근 규격 · 19종 (D4 ~ D57) | `"BE_HORZ_REBAR"` | String (enum) | — | **필수** |
| f | 경계요소 수평 철근 간격 | `"BE_HORZ_SPACE"` | Number | — | **필수** |
| g | 경계요소 수직 철근 간격 | `"BE_VERT_SPACE"` | Number | — | **필수** |
| h | 단부 피복 거리 de (m) | `"DE"` | Number | `0` | 선택 |
| i | 벽면 피복 거리 dw (m) | `"DW"` | Number | `0` | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "976": {
      "ITEMS": [
        {
          "STORY": "1F",
          "VERTICAL_REBAR": "D13",
          "HORIZONTAL_REBAR": "D10",
          "END_REBAR": "D13",
          "BE_HORZ_REBAR": "D10",
          "BE_HORZ_SPACE": 0.2,
          "BE_VERT_SPACE": 0.1,
          "DE": 0.05,
          "DW": 0.05
        },
        {
          "STORY": "B1",
          "VERTICAL_REBAR": "D4",
          "HORIZONTAL_REBAR": "D10",
          "END_REBAR": "D5",
          "BE_HORZ_REBAR": "D13",
          "BE_HORZ_SPACE": 0.2,
          "BE_VERT_SPACE": 0.2,
          "DE": 0.05,
          "DW": 0.05
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "DCRMW": {
    "976": {
      "ITEMS": [
        {
          "STORY": "1F",
          "VERTICAL_REBAR": "D13",
          "HORIZONTAL_REBAR": "D10",
          "END_REBAR": "D13",
          "BE_HORZ_REBAR": "D10",
          "BE_HORZ_SPACE": 0.2,
          "BE_VERT_SPACE": 0.1,
          "DE": 0.05,
          "DW": 0.05
        },
        {
          "STORY": "B1",
          "VERTICAL_REBAR": "D4",
          "HORIZONTAL_REBAR": "D10",
          "END_REBAR": "D5",
          "BE_HORZ_REBAR": "D13",
          "BE_HORZ_SPACE": 0.2,
          "BE_VERT_SPACE": 0.2,
          "DE": 0.05,
          "DW": 0.05
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
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCRM-WALL"

# 벽체 976, 층(1F/B1)별 철근 기준 지정 (POST) — ITEMS[] 배열, 항목마다 STORY 포함
payload = {
    "Assign": {
        "976": {
            "ITEMS": [
                {
                    "STORY": "1F",
                    "VERTICAL_REBAR": "D13",     # 수직 철근
                    "HORIZONTAL_REBAR": "D10",   # 수평 철근
                    "END_REBAR": "D13",          # 단부 철근
                    "BE_HORZ_REBAR": "D10",      # 경계요소 수평 철근
                    "BE_HORZ_SPACE": 0.2,        # 경계요소 수평 간격
                    "BE_VERT_SPACE": 0.1,        # 경계요소 수직 간격
                    "DE": 0.05, "DW": 0.05,
                },
                {
                    "STORY": "B1",
                    "VERTICAL_REBAR": "D4",
                    "HORIZONTAL_REBAR": "D10",
                    "END_REBAR": "D5",
                    "BE_HORZ_REBAR": "D13",
                    "BE_HORZ_SPACE": 0.2,
                    "BE_VERT_SPACE": 0.2,
                    "DE": 0.05, "DW": 0.05,
                },
            ]
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 최상위 키 "DCRMW"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 33. `DESIGN/RC/KDS-41-20-2022/DCRE` — 철근 설계기준

> **기능:** 모델 **전역**의 RC 철근 설계기준을 부재 종류별(`BEAM`·`COLUMN`·`BRACE`·`WALL`)로 한 번에 설정합니다. 보/기둥/가새는 `DCRM-*` 와 유사한 필드를 가지되 주철근을 **배열(다중 규격, 최대 5종)** 로 입력하며, 벽체는 직경별 재질 매핑·면외 휨·간격 리스트 등 **추가 설정**을 포함합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCRE
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 철근 규격 enum(**19종 D4 ~ D57**)과 재질 grade enum(**9종**)은 반복이 많아 규격은 앞 5개만, 재질은 전체를 표기합니다. `Assign` 은 `minProperties`·`maxProperties` 가 모두 1 인 **단일 전역 레코드**입니다.

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "인덱스 문자열(예: \"1\") 하나만 갖는 전역 설정 맵.",
      "minProperties": 1,
      "maxProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "BEAM": {
              "type": "object",
              "description": "보 철근 규격·배근",
              "properties": {
                "MAIN_REBAR": { "type": "array", "description": "주철근 규격 (최대 5종)", "default": ["D22"], "items": { "type": "string", "description": "전체 19종: D4 ~ D57", "enum": ["D4", "D5", "D6", "D7", "D8"] } },
                "STIRRUPS": { "type": "string", "description": "스터럽 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "STIRRUP_ARRANGEMENT": { "type": "integer", "description": "스터럽 다리 수 (전체 19종: 2 ~ 20)", "default": 2, "enum": [2, 3, 4, 5, 6] },
                "SIDE_BAR": { "type": "string", "description": "측면철근 규격 (전체 19종: D4 ~ D57)", "default": "D13", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "DT": { "type": "number", "description": "상단 피복", "default": 0 },
                "DB": { "type": "number", "description": "하단 피복", "default": 0 },
                "DOUBLY_REBAR": { "type": "boolean", "description": "복철근 설계", "default": true },
                "DOUBLY_K": { "type": "number", "description": "복철근 k 계수", "default": 1 },
                "SPACING_LIMIT": { "type": "boolean", "description": "간격 제한 고려", "default": true },
                "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
              }
            },
            "COLUMN": {
              "type": "object",
              "description": "기둥 철근 규격·배근",
              "properties": {
                "MAIN_REBAR": { "type": "array", "description": "주철근 규격 (최대 5종)", "default": ["D22"], "items": { "type": "string", "description": "전체 19종: D4 ~ D57", "enum": ["D4", "D5", "D6", "D7", "D8"] } },
                "TIES_SPIRALS": { "type": "string", "description": "띠철근/나선철근 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "ARRANGEMENT_Y": { "type": "integer", "description": "다리 수 (Y) (전체 19종: 2 ~ 20)", "default": 2, "enum": [2, 3, 4, 5, 6] },
                "ARRANGEMENT_Z": { "type": "integer", "description": "다리 수 (Z) (전체 19종: 2 ~ 20)", "default": 2, "enum": [2, 3, 4, 5, 6] },
                "DO": { "type": "number", "description": "주철근 중심 피복 do", "default": 0 },
                "SPACING_LIMIT": { "type": "boolean", "description": "간격 제한 고려", "default": true },
                "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
              }
            },
            "BRACE": {
              "type": "object",
              "description": "가새 철근 규격·배근 (COLUMN과 동일 필드)",
              "properties": {
                "MAIN_REBAR": { "type": "array", "description": "주철근 규격 (최대 5종)", "default": ["D22"], "items": { "type": "string", "description": "전체 19종: D4 ~ D57", "enum": ["D4", "D5", "D6", "D7", "D8"] } },
                "TIES_SPIRALS": { "type": "string", "description": "띠철근/나선철근 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "ARRANGEMENT_Y": { "type": "integer", "description": "다리 수 (Y) (전체 19종: 2 ~ 20)", "default": 2, "enum": [2, 3, 4, 5, 6] },
                "ARRANGEMENT_Z": { "type": "integer", "description": "다리 수 (Z) (전체 19종: 2 ~ 20)", "default": 2, "enum": [2, 3, 4, 5, 6] },
                "DO": { "type": "number", "description": "주철근 중심 피복 do", "default": 0 },
                "SPACING_LIMIT": { "type": "boolean", "description": "간격 제한 고려", "default": true },
                "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
              }
            },
            "WALL": {
              "type": "object",
              "description": "전단벽 철근 규격·배근",
              "properties": {
                "VERTICAL_REBAR": { "type": "array", "description": "수직 철근 규격 (다중 선택)", "default": ["D13"], "items": { "type": "string", "description": "전체 19종: D4 ~ D57", "enum": ["D4", "D5", "D6", "D7", "D8"] } },
                "HORIZONTAL_REBAR": { "type": "string", "description": "수평 철근 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "END_REBAR": { "type": "string", "description": "단부 철근 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "BE_HORZ_REBAR": { "type": "string", "description": "경계요소 수평 철근 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "BE_HORZ_SPACE": { "type": "number", "description": "경계요소 수평 간격", "default": 0.2 },
                "BE_VERT_SPACE": { "type": "number", "description": "경계요소 수직 간격", "default": 0.1 },
                "DE": { "type": "number", "description": "단부 첫 수직철근까지 거리", "default": 0 },
                "DW": { "type": "number", "description": "벽면까지 피복 거리", "default": 0 },
                "MATERIAL_BY_DIAMETER": { "type": "boolean", "description": "직경별 재질 사용", "default": false },
                "MATERIAL_BY_DIAMETER_INPUT": {
                  "type": "object",
                  "description": "직경별 재질 입력 (MATERIAL_BY_DIAMETER=true 일 때)",
                  "properties": {
                    "VERTICAL_END_REBAR": {
                      "type": "array",
                      "description": "수직/단부 철근 재질 매핑",
                      "items": {
                        "type": "object",
                        "properties": {
                          "REBAR_DIAMETER": { "type": "string", "description": "철근 직경 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                          "MATERIAL": { "type": "string", "description": "재질 등급", "enum": ["None", "SD300", "SD400", "SD500", "SD600", "SD700", "SD400S", "SD500S", "SD600S"] }
                        }
                      }
                    },
                    "HORIZONTAL_REBAR": {
                      "type": "array",
                      "description": "수평 철근 재질 매핑 (VERTICAL_END_REBAR와 동일 항목 구조)",
                      "items": {
                        "type": "object",
                        "properties": {
                          "REBAR_DIAMETER": { "type": "string", "description": "철근 직경 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                          "MATERIAL": { "type": "string", "description": "재질 등급", "enum": ["None", "SD300", "SD400", "SD500", "SD600", "SD700", "SD400S", "SD500S", "SD600S"] }
                        }
                      }
                    }
                  }
                },
                "ADDITIONAL_WALL_DATA": {
                  "type": "object",
                  "description": "벽체 추가 데이터",
                  "properties": {
                    "OUT_OF_PLANE_BENDING": { "type": "boolean", "description": "면외 휨 설계", "default": false },
                    "VERTICAL_REBAR_SPACING": {
                      "type": "object",
                      "description": "수직 철근 간격 설정 (생략 시 기본 상태 적용)",
                      "properties": {
                        "UNIT": { "type": "string", "description": "간격 단위", "default": "mm", "enum": ["mm", "in"] },
                        "LIST_FOR_DESIGN": { "type": "array", "description": "설계에 사용할 간격 값 목록", "default": [100, 150], "items": { "type": "number" } }
                      }
                    },
                    "HORIZONTAL_REBAR_SPACING_FROM": { "type": "number", "description": "수평 철근 간격(from). 단위 m 기준 기본 0.05", "default": 0.05 },
                    "END_REBAR_METHOD": { "type": "integer", "description": "단부 철근 설계 방법", "default": 1, "enum": [1, 2, 3, 4] },
                    "DIST1": { "type": "number", "description": "단부 철근 4개 배근 간격", "default": 0.3 },
                    "DIST2": { "type": "number", "description": "단부 철근 6개 배근 간격", "default": 0.15 },
                    "DIST3": { "type": "number", "description": "단부 철근 8개 이상 배근 간격", "default": 0.1 }
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

**Root / 부재 그룹**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | 인덱스 문자열 1개만 갖는 전역 설정 맵 | `"Assign"` | Object | — | **필수** |
| 2 | 보 철근 기준 | `"BEAM"` | Object | — | 선택 |
| 3 | 기둥 철근 기준 | `"COLUMN"` | Object | — | 선택 |
| 4 | 가새 철근 기준 | `"BRACE"` | Object | — | 선택 |
| 5 | 벽체 철근 기준 | `"WALL"` | Object | — | 선택 |

**`BEAM` 객체 (기둥/가새는 유사, `DCRM-*` 참조)**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 주철근 규격 배열 (최대 5종) · 항목은 19종 (D4 ~ D57) | `"MAIN_REBAR"` | Array[String] | `["D22"]` | 선택 |
| b | 스터럽 규격 · 19종 | `"STIRRUPS"` | String (enum) | `"D10"` | 선택 |
| c | 스터럽 다리 수 · 2 ~ 20 | `"STIRRUP_ARRANGEMENT"` | Integer (enum) | `2` | 선택 |
| d | 측면철근 규격 · 19종 | `"SIDE_BAR"` | String (enum) | `"D13"` | 선택 |
| e | 상단/하단 피복 | `"DT"` / `"DB"` | Number | `0` | 선택 |
| f | 복철근 설계 / k 계수 | `"DOUBLY_REBAR"` / `"DOUBLY_K"` | Boolean / Number | `true` / `1` | 선택 |
| g | 간격 제한 고려 | `"SPACING_LIMIT"` | Boolean | `true` | 선택 |
| h | 이음 옵션 (`None` \| `50%` \| `100%`) | `"SPLICED_BARS"` | String (enum) | `"50%"` | 선택 |

**`COLUMN` / `BRACE` 객체 (공통)**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 주철근 규격 배열 (최대 5종) | `"MAIN_REBAR"` | Array[String] | `["D22"]` | 선택 |
| b | 띠철근/나선철근 규격 · 19종 | `"TIES_SPIRALS"` | String (enum) | `"D10"` | 선택 |
| c | 다리 수 Y / Z · 2 ~ 20 | `"ARRANGEMENT_Y"` / `"ARRANGEMENT_Z"` | Integer (enum) | `2` | 선택 |
| d | 주철근 중심 피복 do | `"DO"` | Number | `0` | 선택 |
| e | 간격 제한 / 이음 | `"SPACING_LIMIT"` / `"SPLICED_BARS"` | Boolean / String | `true` / `"50%"` | 선택 |

**`WALL` 객체**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 수직 철근 규격 배열 (다중 선택) · 19종 | `"VERTICAL_REBAR"` | Array[String] | `["D13"]` | 선택 |
| b | 수평 / 단부 / 경계요소 수평 철근 규격 · 19종 | `"HORIZONTAL_REBAR"` / `"END_REBAR"` / `"BE_HORZ_REBAR"` | String (enum) | `"D10"` | 선택 |
| c | 경계요소 수평 / 수직 간격 | `"BE_HORZ_SPACE"` / `"BE_VERT_SPACE"` | Number | `0.2` / `0.1` | 선택 |
| d | 단부 첫 수직철근까지 거리 / 벽면 피복 | `"DE"` / `"DW"` | Number | `0` | 선택 |
| e | 직경별 재질 사용 | `"MATERIAL_BY_DIAMETER"` | Boolean | `false` | 선택 |
| f | 직경별 재질 입력 (사용 시) | `"MATERIAL_BY_DIAMETER_INPUT"` | Object | — | 조건부 |
| g | 벽체 추가 데이터 | `"ADDITIONAL_WALL_DATA"` | Object | — | 선택 |

**`MATERIAL_BY_DIAMETER_INPUT` 객체** — `VERTICAL_END_REBAR`·`HORIZONTAL_REBAR` 두 배열이 동일한 항목 구조를 가집니다.

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 수직/단부 철근 재질 매핑 배열 | `"VERTICAL_END_REBAR"` | Array[Object] | — | 선택 |
| b | 수평 철근 재질 매핑 배열 | `"HORIZONTAL_REBAR"` | Array[Object] | — | 선택 |
| a→ | 철근 직경 · 19종 (D4 ~ D57) | `"REBAR_DIAMETER"` | String (enum) | — | 선택 |
| a→ | 재질 등급 · `None`,`SD300`,`SD400`,`SD500`,`SD600`,`SD700`,`SD400S`,`SD500S`,`SD600S` | `"MATERIAL"` | String (enum) | — | 선택 |

**`ADDITIONAL_WALL_DATA` 객체**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 면외 휨 설계 | `"OUT_OF_PLANE_BENDING"` | Boolean | `false` | 선택 |
| b | 수직 철근 간격 설정 (`UNIT`: `mm`/`in`, `LIST_FOR_DESIGN`: 간격 값 배열) | `"VERTICAL_REBAR_SPACING"` | Object | `{"UNIT":"mm","LIST_FOR_DESIGN":[100,150]}` | 선택 |
| c | 수평 철근 간격(from) | `"HORIZONTAL_REBAR_SPACING_FROM"` | Number | `0.05` | 선택 |
| d | 단부 철근 설계 방법 (`1`=Method-1 … `4`=Method-4) | `"END_REBAR_METHOD"` | Integer (enum) | `1` | 선택 |
| e | 단부 철근 배근 간격 (4개 / 6개 / 8개 이상) | `"DIST1"` / `"DIST2"` / `"DIST3"` | Number | `0.3` / `0.15` / `0.1` | 선택 |

> ⚠️ **예제 표기 차이:** 아래 Request 예제는 `SPLICED_BARS` 를 정수(`1`)로, `VERTICAL_REBAR_SPACING` 을 `["@100", "@150", …]` 문자열 배열로 전송합니다. 스키마 정의(`SPLICED_BARS` = `"50%"` 등 문자열 enum, `VERTICAL_REBAR_SPACING` = 객체)와 표기 방식이 다르므로, 실제 전송 시에는 아래 예제 형식을 그대로 따르는 것이 안전합니다.

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "BEAM": {
        "MAIN_REBAR": ["D22"],
        "STIRRUPS": "D10",
        "STIRRUP_ARRANGEMENT": 2,
        "SIDE_BAR": "D13",
        "DT": 0,
        "DB": 0,
        "DOUBLY_REBAR": true,
        "SPACING_LIMIT": true,
        "DOUBLY_K": 1,
        "SPLICED_BARS": 1
      },
      "COLUMN": {
        "MAIN_REBAR": ["D22"],
        "TIES_SPIRALS": "D10",
        "ARRANGEMENT_Y": 2,
        "ARRANGEMENT_Z": 2,
        "DO": 0,
        "SPACING_LIMIT": true,
        "SPLICED_BARS": 1
      },
      "BRACE": {
        "MAIN_REBAR": ["D22"],
        "TIES_SPIRALS": "D10",
        "ARRANGEMENT_Y": 2,
        "ARRANGEMENT_Z": 2,
        "DO": 0,
        "SPACING_LIMIT": true,
        "SPLICED_BARS": 1
      },
      "WALL": {
        "VERTICAL_REBAR": ["D10", "D13"],
        "HORIZONTAL_REBAR": "D10",
        "END_REBAR": "D13",
        "BE_HORZ_REBAR": "D10",
        "BE_HORZ_SPACE": 0.2,
        "BE_VERT_SPACE": 0.1,
        "DE": 0.05,
        "DW": 0.05,
        "MATERIAL_BY_DIAMETER": false,
        "ADDITIONAL_WALL_DATA": {
          "OUT_OF_PLANE_BENDING": false,
          "VERTICAL_REBAR_SPACING": ["@100", "@150", "@200", "@300", "@400"],
          "HORIZONTAL_REBAR_SPACING_FROM": 0.05,
          "END_REBAR_METHOD": 3,
          "DIST1": 0.3,
          "DIST2": 0.15,
          "DIST3": 0.1
        }
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "DCRE": {
    "1": {
      "BEAM": {
        "MAIN_REBAR": ["D22"],
        "STIRRUPS": "D10",
        "STIRRUP_ARRANGEMENT": 2,
        "SIDE_BAR": "D13",
        "DT": 0,
        "DB": 0,
        "DOUBLY_REBAR": true,
        "SPACING_LIMIT": true,
        "DOUBLY_K": 1,
        "SPLICED_BARS": 1
      },
      "WALL": {
        "VERTICAL_REBAR": ["D10", "D13"],
        "HORIZONTAL_REBAR": "D10",
        "END_REBAR": "D13",
        "BE_HORZ_REBAR": "D10",
        "BE_HORZ_SPACE": 0.2,
        "BE_VERT_SPACE": 0.1,
        "DE": 0.05,
        "DW": 0.05,
        "MATERIAL_BY_DIAMETER": false,
        "ADDITIONAL_WALL_DATA": {
          "OUT_OF_PLANE_BENDING": false,
          "VERTICAL_REBAR_SPACING": ["@100", "@150", "@200", "@300", "@400"],
          "HORIZONTAL_REBAR_SPACING_FROM": 0.05,
          "END_REBAR_METHOD": 3,
          "DIST1": 0.3,
          "DIST2": 0.15,
          "DIST3": 0.1
        }
      }
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCRE"

# 전역 RC 철근 기준 설정 (POST) — 부재 종류별 일괄 지정
payload = {
    "Assign": {
        "1": {
            "BEAM": {
                "MAIN_REBAR": ["D22"],          # 주철근은 배열(최대 5종)
                "STIRRUPS": "D10",
                "STIRRUP_ARRANGEMENT": 2,
                "SIDE_BAR": "D13",
                "DT": 0, "DB": 0,
                "DOUBLY_REBAR": True, "DOUBLY_K": 1,
                "SPACING_LIMIT": True,
                "SPLICED_BARS": 1,              # 예제 표기: 정수
            },
            "COLUMN": {
                "MAIN_REBAR": ["D22"], "TIES_SPIRALS": "D10",
                "ARRANGEMENT_Y": 2, "ARRANGEMENT_Z": 2,
                "DO": 0, "SPACING_LIMIT": True, "SPLICED_BARS": 1,
            },
            "WALL": {
                "VERTICAL_REBAR": ["D10", "D13"],
                "HORIZONTAL_REBAR": "D10", "END_REBAR": "D13",
                "BE_HORZ_REBAR": "D10",
                "BE_HORZ_SPACE": 0.2, "BE_VERT_SPACE": 0.1,
                "DE": 0.05, "DW": 0.05,
                "MATERIAL_BY_DIAMETER": False,
                "ADDITIONAL_WALL_DATA": {
                    "OUT_OF_PLANE_BENDING": False,
                    "VERTICAL_REBAR_SPACING": ["@100", "@150", "@200"],
                    "HORIZONTAL_REBAR_SPACING_FROM": 0.05,
                    "END_REBAR_METHOD": 3,
                    "DIST1": 0.3, "DIST2": 0.15, "DIST3": 0.1,
                },
            },
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 최상위 키 "DCRE"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 34. `DESIGN/RC/KDS-41-20-2022/DCREM` — 접합부 보 철근 동일화

> **기능:** 접합부(절점)에서 만나는 보들의 철근을 **동일하게** 처리하기 위한 설정입니다. 전체 부재에 적용하거나(`SELECT_ALL`), 특정 절점(node)별로 그 절점을 사이에 두는 **정확히 2개의 요소 번호**를 지정합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCREM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "인덱스 문자열(예: \"1\")을 키로 갖는 설정 맵.",
      "minProperties": 1,
      "additionalProperties": {
        "type": "object",
        "additionalProperties": false,
        "required": ["SELECT_ALL"],
        "properties": {
          "SELECT_ALL": { "type": "boolean", "description": "사용 가능한 모든 부재에 적용" },
          "SELECTED_MEMBERS": {
            "type": "object",
            "description": "선택 부재 맵. 각 키는 절점(node) ID 문자열, 값은 해당 절점의 요소 목록.",
            "minProperties": 1,
            "additionalProperties": {
              "type": "object",
              "additionalProperties": false,
              "required": ["ELEM_LIST"],
              "properties": {
                "ELEM_LIST": {
                  "type": "array",
                  "description": "절점이 사이에 위치하는 정확히 2개의 요소 번호",
                  "items": { "type": "integer" },
                  "minItems": 2,
                  "maxItems": 2
                }
              }
            }
          }
        },
        "allOf": [
          {
            "if": { "properties": { "SELECT_ALL": { "const": false } }, "required": ["SELECT_ALL"] },
            "then": { "required": ["SELECTED_MEMBERS"] }
          }
        ]
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | 인덱스 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **필수** |
| 2 | 모든 부재에 적용 | `"SELECT_ALL"` | Boolean | — | **필수** |
| 3 | 선택 부재 맵 (`SELECT_ALL`=false 일 때 필수). 키는 절점 ID 문자열 | `"SELECTED_MEMBERS"` | Object | — | 조건부 필수 |
| 3.1 | 절점을 사이에 두는 정확히 2개의 요소 번호 | `"ELEM_LIST"` | Array[Integer] (길이 2) | — | **필수** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "SELECT_ALL": false,
      "SELECTED_MEMBERS": {
        "347": { "ELEM_LIST": [925, 926] },
        "364": { "ELEM_LIST": [922, 924] },
        "365": { "ELEM_LIST": [924, 925] },
        "396": { "ELEM_LIST": [926, 927] }
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "DCREM": {
    "1": {
      "SELECT_ALL": false,
      "SELECTED_MEMBERS": {
        "347": { "ELEM_LIST": [925, 926] },
        "364": { "ELEM_LIST": [922, 924] },
        "365": { "ELEM_LIST": [924, 925] },
        "396": { "ELEM_LIST": [926, 927] }
      }
    }
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCREM"

# 방법 1) 모든 부재 동일화 (POST)
requests.post(URI, headers=HEADERS, json={"Assign": {"1": {"SELECT_ALL": True}}})

# 방법 2) 절점별로 사이에 위치한 2개 요소 지정
payload = {
    "Assign": {
        "1": {
            "SELECT_ALL": False,
            "SELECTED_MEMBERS": {
                "347": {"ELEM_LIST": [925, 926]},   # 절점 347 좌우 요소
                "364": {"ELEM_LIST": [922, 924]},
            },
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 최상위 키 "DCREM"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 35. `DESIGN/RC/KDS-41-20-2022/REBB` — 보 철근 데이터 수정

> **기능:** 단면(section) 번호별로 콘크리트 보의 철근 데이터를 수정합니다. 각 `ITEMS` 항목은 I·M·J 세 구간(`BAR_SECTOR_I/M/J`)의 상·하단 주철근(레이어별), 스터럽(전단철근), 표피철근(skin bar)과 상·하단 피복(`DT`/`DB`)을 포함하며, `CREATE_SUB_SECTION` 으로 서브 단면을 생성할 수 있습니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/REBB
```

### Active Methods

`POST` · `GET` · `DELETE` · `PUT`

### JSON Schema

> 스키마가 매우 큽니다(≈99KB). 세 구간(`BAR_SECTOR_I/M/J`)은 **동일한 객체 구조**가 반복되므로 아래에서는 `BAR_SECTOR_I` 만 완전히 전개하고, `BAR_SECTOR_M`·`BAR_SECTOR_J` 는 동일 구조임을 표시합니다. 철근 규격 enum(**19종 D4 ~ D57**)은 앞 5개만 표기합니다.

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "단면 번호 문자열을 키로 갖는 맵 (예: \"211\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "콘크리트 보 철근 항목",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": ["BAR_SECTOR_I", "BAR_SECTOR_M", "BAR_SECTOR_J", "DT", "DB"],
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "description": "서브 단면 생성", "default": false },
                  "ID": { "type": "integer", "description": "서브 단면 ID (읽기 전용)" },
                  "ELEMS": {
                    "type": "object",
                    "description": "요소 번호 입력 (CREATE_SUB_SECTION=true 일 때 필수). KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "description": "각 요소 ID 지정", "items": { "type": "integer" } },
                      "TO": { "type": "string", "description": "ID 범위 (예: '1to160')" },
                      "STRUCTURE_GROUP_NAME": { "type": "string", "description": "구조 그룹 이름 지정" }
                    }
                  },
                  "BAR_SECTOR_I": {
                    "type": "object",
                    "description": "I단 구간 철근",
                    "required": ["MAIN_BAR_TOP", "MAIN_BAR_BOT", "SHEAR_BAR"],
                    "properties": {
                      "MAIN_BAR_TOP": {
                        "type": "object",
                        "description": "상단 주철근 (레이어별)",
                        "required": ["LAYER1"],
                        "properties": {
                          "LAYER1": {
                            "type": "object",
                            "required": ["NAME", "NUM"],
                            "properties": {
                              "NAME": { "type": "string", "description": "규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                              "NUM": { "type": "integer", "description": "철근 개수" }
                            }
                          },
                          "LAYER2": {
                            "type": "object",
                            "required": ["NAME", "NUM"],
                            "properties": {
                              "NAME": { "type": "string", "description": "규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                              "NUM": { "type": "integer", "description": "철근 개수" }
                            }
                          }
                        }
                      },
                      "MAIN_BAR_BOT": {
                        "type": "object",
                        "description": "하단 주철근 (레이어별, MAIN_BAR_TOP과 동일 구조: LAYER1 필수 / LAYER2 선택)",
                        "required": ["LAYER1"],
                        "properties": {
                          "LAYER1": { "type": "object", "required": ["NAME", "NUM"], "properties": { "NAME": { "type": "string", "enum": ["D4", "D5", "D6", "D7", "D8"] }, "NUM": { "type": "integer" } } },
                          "LAYER2": { "type": "object", "required": ["NAME", "NUM"], "properties": { "NAME": { "type": "string", "enum": ["D4", "D5", "D6", "D7", "D8"] }, "NUM": { "type": "integer" } } }
                        }
                      },
                      "SHEAR_BAR": {
                        "type": "object",
                        "description": "스터럽 데이터",
                        "required": ["NAME", "LEG", "DIST"],
                        "properties": {
                          "NAME": { "type": "string", "description": "스터럽 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                          "LEG": { "type": "integer", "description": "다리 수" },
                          "DIST": { "type": "number", "description": "스터럽 간격 @" }
                        }
                      },
                      "SKIN_BAR": {
                        "type": "object",
                        "description": "표피철근 (이 객체가 있으면 사용)",
                        "required": ["NAME", "NUM"],
                        "properties": {
                          "NAME": { "type": "string", "description": "표피철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                          "NUM": { "type": "integer", "description": "철근 개수" }
                        }
                      }
                    }
                  },
                  "BAR_SECTOR_M": { "type": "object", "description": "중앙(M) 구간 철근 — BAR_SECTOR_I와 동일 구조 (반복 구조, 지면상 생략)" },
                  "BAR_SECTOR_J": { "type": "object", "description": "J단 구간 철근 — BAR_SECTOR_I와 동일 구조 (반복 구조, 지면상 생략)" },
                  "DT": { "type": "number", "description": "상단 콘크리트면~상단 철근중심 거리" },
                  "DB": { "type": "number", "description": "하단 콘크리트면~하단 철근중심 거리" }
                },
                "allOf": [
                  {
                    "if": { "properties": { "CREATE_SUB_SECTION": { "const": true } }, "required": ["CREATE_SUB_SECTION"] },
                    "then": { "required": ["ELEMS"] }
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
}
```

> **반복 구조 안내:** `BAR_SECTOR_M`·`BAR_SECTOR_J` 는 위 `BAR_SECTOR_I` 와 필드가 완전히 동일합니다(`MAIN_BAR_TOP`/`MAIN_BAR_BOT`(각각 `LAYER1` 필수·`LAYER2` 선택), `SHEAR_BAR`, `SKIN_BAR`). JSON 블록의 유효성을 위해 두 구간은 설명만 남기고 내부 전개는 생략했습니다.

### 파라미터

**Root / Item**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | 단면 번호 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **필수** |
| 2 | 콘크리트 보 철근 항목 (min 1) | `"ITEMS"` | Array[Object] | — | **필수** |
| (1) | 서브 단면 생성 여부 | `"CREATE_SUB_SECTION"` | Boolean | `false` | 선택 |
| (2) | 서브 단면 ID (읽기 전용) | `"ID"` | Integer | — | 선택 |
| (3) | 요소 번호 입력 (`CREATE_SUB_SECTION`=true 일 때 필수) | `"ELEMS"` | Object | — | 조건부 |
| (4) | I단 구간 철근 | `"BAR_SECTOR_I"` | Object | — | **필수** |
| (5) | 중앙(M) 구간 철근 | `"BAR_SECTOR_M"` | Object | — | **필수** |
| (6) | J단 구간 철근 | `"BAR_SECTOR_J"` | Object | — | **필수** |
| (7) | 상단 피복 거리 dT | `"DT"` | Number | — | **필수** |
| (8) | 하단 피복 거리 dB | `"DB"` | Number | — | **필수** |

**`BAR_SECTOR_I/M/J` 구간 객체 (세 구간 동일)**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 상단 주철근 (레이어별) | `"MAIN_BAR_TOP"` | Object | — | **필수** |
| b | 하단 주철근 (레이어별) | `"MAIN_BAR_BOT"` | Object | — | **필수** |
| a/b→ | 레이어1 (필수) / 레이어2 (선택) | `"LAYER1"` / `"LAYER2"` | Object | — | LAYER1 **필수** |
| — | 레이어 내 철근 규격 · 19종 (D4 ~ D57) | `"NAME"` | String (enum) | — | **필수** |
| — | 레이어 내 철근 개수 | `"NUM"` | Integer | — | **필수** |
| c | 스터럽(전단철근) | `"SHEAR_BAR"` | Object | — | **필수** |
| c→ | 스터럽 규격 / 다리 수 / 간격 | `"NAME"` / `"LEG"` / `"DIST"` | String / Integer / Number | — | **필수** |
| d | 표피철근(skin bar, 있으면 사용) | `"SKIN_BAR"` | Object | — | 선택 |
| d→ | 표피철근 규격 / 개수 | `"NAME"` / `"NUM"` | String / Integer | — | **필수** |

**`CREATE_SUB_SECTION == true` 일 때 — `ELEMS` (KEYS / TO / STRUCTURE_GROUP_NAME 중 택1)**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 요소 ID 배열 | `"KEYS"` | Array[Integer] | — | 선택 |
| b | ID 범위 (예: `"1to160"`) | `"TO"` | String | — | 선택 |
| c | 구조 그룹 이름 | `"STRUCTURE_GROUP_NAME"` | String | — | 선택 |

> **예제 표기 차이:** 아래 Request/Response 예제는 상·하단 주철근을 `"vMAIN_BAR_TOP"`/`"vMAIN_BAR_BOT"` **배열**, 표피철근을 `"SKIN_BAR_NAME"`/`"SKIN_BAR_NUM"`, 피복을 `"MAIN_BAR_DC_TOP"`/`"MAIN_BAR_DC_BOT"` 로 표기합니다(스키마의 `LAYER*`/`SKIN_BAR`/`DT`·`DB` 와 표기 방식이 다름). 실제 전송 시에는 아래 예제 형식을 그대로 따르는 것이 안전합니다.

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "211": {
      "ITEMS": [
        {
          "ID": 0,
          "BAR_SECTOR_I": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_M": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_J": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "MAIN_BAR_DC_TOP": 0.06999999999999999,
          "MAIN_BAR_DC_BOT": 0.06999999999999999,
          "bSAME_SIZE_TOP_BOT": true,
          "bSAME_SIZE_IMJ": true,
          "bSAME_SIZE_LAYER": true
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "REBB": {
    "211": {
      "ITEMS": [
        {
          "ID": 0,
          "BAR_SECTOR_I": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_M": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_J": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "MAIN_BAR_DC_TOP": 0.06999999999999999,
          "MAIN_BAR_DC_BOT": 0.06999999999999999,
          "bSAME_SIZE_TOP_BOT": true,
          "bSAME_SIZE_IMJ": true,
          "bSAME_SIZE_LAYER": true
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
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/REBB"

# 단면 211의 보 철근 데이터 수정 (I·M·J 세 구간 동일 적용)
sector = {
    "vMAIN_BAR_TOP": [],
    "vMAIN_BAR_BOT": [],
    "SHEAR_BAR": {"NAME": "D10", "LEG": 2, "DIST": 0.1},   # 스터럽
    "SKIN_BAR_NAME": "",
    "SKIN_BAR_NUM": 2,
}
payload = {
    "Assign": {
        "211": {
            "ITEMS": [
                {
                    "ID": 0,
                    "BAR_SECTOR_I": sector,
                    "BAR_SECTOR_M": sector,
                    "BAR_SECTOR_J": sector,
                    "MAIN_BAR_DC_TOP": 0.07,   # 상단 피복
                    "MAIN_BAR_DC_BOT": 0.07,   # 하단 피복
                    "bSAME_SIZE_TOP_BOT": True,
                    "bSAME_SIZE_IMJ": True,
                    "bSAME_SIZE_LAYER": True,
                }
            ]
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 최상위 키 "REBB"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 36. `DESIGN/RC/KDS-41-20-2022/REBC` — 기둥 철근 데이터 수정

> **기능:** 단면 번호별로 콘크리트 기둥의 철근 데이터를 수정합니다. 주철근(`MAIN_BAR`), 단부/중앙부 전단철근(`SHEAR_BAR_END`/`SHEAR_BAR_CEN`), 피복 거리(`DO`), 후프 타입(`HOOP_TYPE`), 후크 타입(`HOOK_TYPE`)을 포함합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/REBC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 철근 규격 enum(**19종 D4 ~ D57**)은 앞 5개만 표기합니다.

```json
{
  "type": "object",
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "단면 번호 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "콘크리트 기둥 철근 항목",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": ["MAIN_BAR", "SHEAR_BAR_END", "SHEAR_BAR_CEN", "DO"],
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "description": "서브 단면 생성", "default": false },
                  "ID": { "type": "integer", "description": "서브 단면 ID (읽기 전용)" },
                  "ELEMS": {
                    "type": "object",
                    "description": "요소 번호 입력 (CREATE_SUB_SECTION=true 일 때 필수). KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "items": { "type": "integer" } },
                      "TO": { "type": "string", "description": "ID 범위 (예: '1to160')" },
                      "STRUCTURE_GROUP_NAME": { "type": "string" }
                    }
                  },
                  "MAIN_BAR": {
                    "type": "object",
                    "description": "주철근 데이터",
                    "required": ["NAME", "NUM", "ROW", "USE_CORNER"],
                    "properties": {
                      "NAME": { "type": "string", "description": "주철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "NUM": { "type": "integer", "description": "철근 총 개수" },
                      "ROW": { "type": "integer", "description": "철근 열(row) 수" },
                      "USE_CORNER": { "type": "boolean", "description": "코너 철근 사용" },
                      "NAME_CORNER": { "type": "string", "description": "코너 철근 규격 (USE_CORNER=true 일 때, 전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] }
                    }
                  },
                  "SHEAR_BAR_END": {
                    "type": "object",
                    "description": "단부 전단철근 데이터",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "후프 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "LEG_Y": { "type": "integer", "description": "다리 수 (local Y)" },
                      "LEG_Z": { "type": "integer", "description": "다리 수 (local Z)" },
                      "DIST": { "type": "number", "description": "철근 간격 @" }
                    }
                  },
                  "SHEAR_BAR_CEN": {
                    "type": "object",
                    "description": "중앙부 전단철근 데이터 (SHEAR_BAR_END와 동일 구조)",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "LEG_Y": { "type": "integer" },
                      "LEG_Z": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "DO": { "type": "number", "description": "콘크리트면~철근중심 거리" },
                  "HOOP_TYPE": { "type": "string", "description": "후프 철근 타입", "default": "Ties", "enum": ["Ties", "Spirals"] },
                  "HOOK_TYPE": { "type": "integer", "description": "후크 타입 (0: 90+(135 or 180), 1: Both(135 or 180))", "default": 0, "enum": [0, 1] }
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

**Root / Item**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | 단면 번호 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **필수** |
| 2 | 콘크리트 기둥 철근 항목 (min 1) | `"ITEMS"` | Array[Object] | — | **필수** |
| (1) | 서브 단면 생성 여부 | `"CREATE_SUB_SECTION"` | Boolean | `false` | 선택 |
| (2) | 서브 단면 ID (읽기 전용) | `"ID"` | Integer | — | 선택 |
| (3) | 요소 번호 입력 (`CREATE_SUB_SECTION`=true 일 때 필수) | `"ELEMS"` | Object | — | 조건부 |
| (4) | 주철근 | `"MAIN_BAR"` | Object | — | **필수** |
| (5) | 단부 전단철근 | `"SHEAR_BAR_END"` | Object | — | **필수** |
| (6) | 중앙부 전단철근 | `"SHEAR_BAR_CEN"` | Object | — | **필수** |
| (7) | 콘크리트면~철근중심 거리 (do) | `"DO"` | Number | — | **필수** |
| (8) | 후프 철근 타입 (`Ties` \| `Spirals`) | `"HOOP_TYPE"` | String (enum) | `"Ties"` | 선택 |
| (9) | 후크 타입 (`0`: 90+(135 or 180) \| `1`: Both(135 or 180)) | `"HOOK_TYPE"` | Integer (enum) | `0` | 선택 |

**`MAIN_BAR` 객체**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 주철근 규격 · 19종 (D4 ~ D57) | `"NAME"` | String (enum) | — | **필수** |
| b | 철근 총 개수 | `"NUM"` | Integer | — | **필수** |
| c | 열(row) 수 | `"ROW"` | Integer | — | **필수** |
| d | 코너 철근 사용 | `"USE_CORNER"` | Boolean | — | **필수** |
| a' | 코너 철근 규격 (USE_CORNER=true 일 때) · 19종 | `"NAME_CORNER"` | String (enum) | — | 조건부 |

**`SHEAR_BAR_END` / `SHEAR_BAR_CEN` 객체 (동일 구조)**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 후프 철근 규격 · 19종 (D4 ~ D57) | `"NAME"` | String (enum) | — | **필수** |
| b | 다리 수 (local Y) | `"LEG_Y"` | Integer | — | **필수** |
| c | 다리 수 (local Z) | `"LEG_Z"` | Integer | — | **필수** |
| d | 철근 간격 @ | `"DIST"` | Number | — | **필수** |

**`CREATE_SUB_SECTION == true` 일 때 — `ELEMS` (KEYS / TO / STRUCTURE_GROUP_NAME 중 택1)**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 요소 ID 배열 | `"KEYS"` | Array[Integer] | — | 선택 |
| b | ID 범위 (예: `"1to160"`) | `"TO"` | String | — | 선택 |
| c | 구조 그룹 이름 | `"STRUCTURE_GROUP_NAME"` | String | — | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_SECTION": false,
          "MAIN_BAR": { "NAME": "D19", "NUM": 8, "ROW": 3, "USE_CORNER": false },
          "SHEAR_BAR_END": { "NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 100 },
          "SHEAR_BAR_CEN": { "NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 200 },
          "DO": 40,
          "HOOP_TYPE": "Ties",
          "HOOK_TYPE": 0
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "REBC": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_SECTION": false,
          "MAIN_BAR": { "NAME": "D19", "NUM": 8, "ROW": 3, "USE_CORNER": false },
          "SHEAR_BAR_END": { "NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 100 },
          "SHEAR_BAR_CEN": { "NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 200 },
          "DO": 40,
          "HOOP_TYPE": "Ties",
          "HOOK_TYPE": 0
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
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/REBC"

# 단면 1의 기둥 철근 데이터 수정 (POST)
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_SECTION": False,
                    "MAIN_BAR": {"NAME": "D19", "NUM": 8, "ROW": 3, "USE_CORNER": False},
                    "SHEAR_BAR_END": {"NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 100},
                    "SHEAR_BAR_CEN": {"NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 200},
                    "DO": 40,
                    "HOOP_TYPE": "Ties",   # Ties 또는 Spirals
                    "HOOK_TYPE": 0,        # 0: 90+(135/180), 1: Both(135/180)
                }
            ]
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 최상위 키 "REBC"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 37. `DESIGN/RC/KDS-41-20-2022/REBW` — 벽체 철근 데이터 수정

> **기능:** 벽체 ID별로 철근 데이터를 수정합니다. 수직/수평 철근, 단부 철근(End Rebar), 경계요소(Boundary Element) 수평 철근, 피복 거리(dw, de), 두께 및 서브 벽체 ID/층(Story) 정보를 포함합니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/REBW
```

### Active Methods

`POST` · `PUT` · `DELETE` · `GET`

### JSON Schema

> 철근 규격 enum(**19종 D4 ~ D57**)은 앞 5개만 표기합니다. 조건부 필수(`allOf`) 규칙은 스키마 하단에 포함되어 있습니다.

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "벽체 ID 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "벽체 철근 항목",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": ["VERTICAL_REBAR", "HORIZONTAL_REBAR", "CONCRETE_FACE_TO_CENTER_OF_REBAR"],
                "properties": {
                  "CREATE_SUB_WALL_ID": { "type": "boolean", "description": "서브 벽체 ID 생성", "default": false },
                  "SUB_WALL_ID": { "type": "integer", "description": "서브 벽체 ID (CREATE_SUB_WALL_ID=true 일 때 읽기 전용)" },
                  "STORY": {
                    "type": "object",
                    "description": "층 범위 (CREATE_SUB_WALL_ID=true 일 때 필수)",
                    "required": ["FROM", "TO"],
                    "properties": {
                      "FROM": { "type": "string", "description": "시작 층" },
                      "TO": { "type": "string", "description": "종료 층" }
                    }
                  },
                  "VERTICAL_REBAR": {
                    "type": "object",
                    "description": "수직 철근 데이터",
                    "required": ["NAME", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "수직 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "DIST": { "type": "number", "description": "수직 철근 간격" }
                    }
                  },
                  "HORIZONTAL_REBAR": {
                    "type": "object",
                    "description": "수평 철근 데이터",
                    "required": ["NAME", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "수평 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "DIST": { "type": "number", "description": "수평 철근 간격" }
                    }
                  },
                  "USE_END_REBAR": { "type": "boolean", "description": "단부 철근 입력 사용", "default": false },
                  "END_REBAR": {
                    "type": "object",
                    "description": "단부 철근 데이터 (USE_END_REBAR=true 일 때 필수)",
                    "required": ["NAME", "NUM", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "단부(수직) 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "NUM": { "type": "integer", "description": "단부 철근 개수" },
                      "DIST": { "type": "number", "description": "단부 철근 간격" }
                    }
                  },
                  "BE_HORIZONTAL_REBAR": {
                    "type": "object",
                    "description": "경계요소 수평 철근 데이터",
                    "required": ["NAME", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "경계요소 수평 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "DIST": { "type": "number", "description": "경계요소 수평 철근 간격" }
                    }
                  },
                  "BOUNDARY_ELEMENT_LENGTH": { "type": "number", "description": "경계요소 길이", "default": 0 },
                  "CONCRETE_FACE_TO_CENTER_OF_REBAR": {
                    "type": "object",
                    "description": "콘크리트면~철근중심 거리",
                    "required": ["DW", "DE"],
                    "properties": {
                      "DW": { "type": "number", "description": "콘크리트면~수직 철근중심 (dw)" },
                      "DE": { "type": "number", "description": "콘크리트면~경계요소 철근중심 (de)" }
                    }
                  },
                  "USE_MODEL_THICKNESS": { "type": "boolean", "description": "모델 두께 사용", "default": true },
                  "THICKNESS": { "type": "number", "description": "벽체 두께 (USE_MODEL_THICKNESS=false 일 때 필수)" }
                },
                "allOf": [
                  { "if": { "properties": { "CREATE_SUB_WALL_ID": { "const": true } }, "required": ["CREATE_SUB_WALL_ID"] }, "then": { "required": ["SUB_WALL_ID", "STORY"] } },
                  { "if": { "properties": { "USE_END_REBAR": { "const": true } }, "required": ["USE_END_REBAR"] }, "then": { "required": ["END_REBAR"] } },
                  { "if": { "properties": { "USE_MODEL_THICKNESS": { "const": false } }, "required": ["USE_MODEL_THICKNESS"] }, "then": { "required": ["THICKNESS"] } }
                ]
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

**Root / Item**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | 벽체 ID 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **필수** |
| 2 | 벽체 철근 항목 (min 1) | `"ITEMS"` | Array[Object] | — | **필수** |
| (1) | 서브 벽체 ID 생성 | `"CREATE_SUB_WALL_ID"` | Boolean | `false` | 선택 |
| (2) | 서브 벽체 ID (읽기 전용, 생성 시 필수) | `"SUB_WALL_ID"` | Integer | — | 조건부 |
| (3) | 층 범위 (`FROM`/`TO`, 생성 시 필수) | `"STORY"` | Object | — | 조건부 |
| (4) | 수직 철근 (`NAME`·`DIST`) | `"VERTICAL_REBAR"` | Object | — | **필수** |
| (5) | 수평 철근 (`NAME`·`DIST`) | `"HORIZONTAL_REBAR"` | Object | — | **필수** |
| (6) | 단부 철근 입력 사용 | `"USE_END_REBAR"` | Boolean | `false` | 선택 |
| (7) | 단부 철근 (`NAME`·`NUM`·`DIST`, 사용 시 필수) | `"END_REBAR"` | Object | — | 조건부 |
| (8) | 경계요소 수평 철근 (`NAME`·`DIST`) | `"BE_HORIZONTAL_REBAR"` | Object | — | 선택 |
| (9) | 경계요소 길이 | `"BOUNDARY_ELEMENT_LENGTH"` | Number | `0` | 선택 |
| (10) | 콘크리트면~철근중심 거리 (`DW`·`DE`) | `"CONCRETE_FACE_TO_CENTER_OF_REBAR"` | Object | — | **필수** |
| (11) | 모델 두께 사용 | `"USE_MODEL_THICKNESS"` | Boolean | `true` | 선택 |
| (12) | 벽체 두께 (`USE_MODEL_THICKNESS`=false 일 때 필수) | `"THICKNESS"` | Number | — | 조건부 |

**철근 하위 객체 필드 요약**

| 객체 | 필드 | 설명 |
|------|------|------|
| `VERTICAL_REBAR` / `HORIZONTAL_REBAR` / `BE_HORIZONTAL_REBAR` | `NAME` (19종 D4 ~ D57) · `DIST` | 규격 · 간격 |
| `END_REBAR` | `NAME` (19종) · `NUM` · `DIST` | 규격 · 개수 · 간격 |
| `CONCRETE_FACE_TO_CENTER_OF_REBAR` | `DW` · `DE` | 수직/경계요소 철근 피복 |
| `STORY` | `FROM` · `TO` | 시작/종료 층 문자열 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_WALL_ID": true,
          "VERTICAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "HORIZONTAL_REBAR": { "NAME": "D16", "DIST": 200 },
          "USE_END_REBAR": true,
          "BE_HORIZONTAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "BOUNDARY_ELEMENT_LENGTH": 222,
          "CONCRETE_FACE_TO_CENTER_OF_REBAR": { "DW": 50, "DE": 50 },
          "USE_MODEL_THICKNESS": false,
          "END_REBAR": { "NAME": "D25", "NUM": 2, "DIST": 150 },
          "THICKNESS": 1000,
          "SUB_WALL_ID": 1,
          "STORY": { "FROM": "2F", "TO": "Roof" }
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "REBW": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_WALL_ID": true,
          "VERTICAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "HORIZONTAL_REBAR": { "NAME": "D16", "DIST": 200 },
          "USE_END_REBAR": true,
          "BE_HORIZONTAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "BOUNDARY_ELEMENT_LENGTH": 222,
          "CONCRETE_FACE_TO_CENTER_OF_REBAR": { "DW": 50, "DE": 50 },
          "USE_MODEL_THICKNESS": false,
          "END_REBAR": { "NAME": "D25", "NUM": 2, "DIST": 150 },
          "THICKNESS": 1000,
          "SUB_WALL_ID": 1,
          "STORY": { "FROM": "2F", "TO": "Roof" }
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
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/REBW"

# 벽체 1의 철근 데이터 수정 (서브 벽체 + 단부철근 + 사용자 두께)
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_WALL_ID": True,
                    "SUB_WALL_ID": 1,
                    "STORY": {"FROM": "2F", "TO": "Roof"},   # 생성 시 필수
                    "VERTICAL_REBAR": {"NAME": "D19", "DIST": 222},
                    "HORIZONTAL_REBAR": {"NAME": "D16", "DIST": 200},
                    "USE_END_REBAR": True,
                    "END_REBAR": {"NAME": "D25", "NUM": 2, "DIST": 150},   # 사용 시 필수
                    "BE_HORIZONTAL_REBAR": {"NAME": "D19", "DIST": 222},
                    "BOUNDARY_ELEMENT_LENGTH": 222,
                    "CONCRETE_FACE_TO_CENTER_OF_REBAR": {"DW": 50, "DE": 50},
                    "USE_MODEL_THICKNESS": False,
                    "THICKNESS": 1000,   # 모델 두께 미사용 시 필수
                }
            ]
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 최상위 키 "REBW"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 38. `DESIGN/RC/KDS-41-20-2022/REBR` — 가새 철근 데이터 수정

> **기능:** 단면 번호별로 콘크리트 가새(Brace)의 철근 데이터를 수정합니다. 구조는 기둥(`REBC`)과 유사하나 `MAIN_BAR` 에 `USE_CORNER` 가 없고 후크 타입(`HOOK_TYPE`)도 없으며, 주철근(`MAIN_BAR`), 단부/중앙부 전단철근(`SHEAR_BAR_END`/`SHEAR_BAR_CEN`), 피복(`DO`), 후프 타입(`HOOP_TYPE`)으로 구성됩니다.

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/REBR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 철근 규격 enum(**19종 D4 ~ D57**)은 앞 5개만 표기합니다.

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "단면 번호 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "콘크리트 가새 철근 항목",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": ["MAIN_BAR", "SHEAR_BAR_END", "SHEAR_BAR_CEN", "DO"],
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "description": "서브 단면 생성", "default": false },
                  "ID": { "type": "integer", "description": "서브 단면 ID (읽기 전용)" },
                  "ELEMS": {
                    "type": "object",
                    "description": "요소 번호 입력 (CREATE_SUB_SECTION=true 일 때 필수). KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "items": { "type": "integer" } },
                      "TO": { "type": "string", "description": "ID 범위 (예: '1to160')" },
                      "STRUCTURE_GROUP_NAME": { "type": "string" }
                    }
                  },
                  "MAIN_BAR": {
                    "type": "object",
                    "description": "주철근 데이터",
                    "required": ["NAME", "NUM", "ROW"],
                    "properties": {
                      "NAME": { "type": "string", "description": "주철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "NUM": { "type": "integer", "description": "철근 총 개수", "minItems": 4 },
                      "ROW": { "type": "integer", "description": "철근 열(row) 수" }
                    }
                  },
                  "SHEAR_BAR_END": {
                    "type": "object",
                    "description": "단부 전단철근 데이터",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "후프 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "LEG_Y": { "type": "integer", "description": "다리 수 (local Y)" },
                      "LEG_Z": { "type": "integer", "description": "다리 수 (local Z)" },
                      "DIST": { "type": "number", "description": "철근 간격 @" }
                    }
                  },
                  "SHEAR_BAR_CEN": {
                    "type": "object",
                    "description": "중앙부 전단철근 데이터 (SHEAR_BAR_END와 동일 구조)",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "LEG_Y": { "type": "integer" },
                      "LEG_Z": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "DO": { "type": "number", "description": "콘크리트면~철근중심 거리" },
                  "HOOP_TYPE": { "type": "string", "description": "후프 철근 타입", "default": "Ties", "enum": ["Ties", "Spirals"] }
                },
                "allOf": [
                  { "if": { "properties": { "CREATE_SUB_SECTION": { "const": true } }, "required": ["CREATE_SUB_SECTION"] }, "then": { "required": ["ELEMS"] } }
                ]
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

**Root / Item**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | 단면 번호 문자열을 키로 갖는 맵 | `"Assign"` | Object | — | **필수** |
| 2 | 콘크리트 가새 철근 항목 (min 1) | `"ITEMS"` | Array[Object] | — | **필수** |
| (1) | 서브 단면 생성 여부 | `"CREATE_SUB_SECTION"` | Boolean | `false` | 선택 |
| (2) | 서브 단면 ID (읽기 전용) | `"ID"` | Integer | — | 선택 |
| (3) | 요소 번호 입력 (`CREATE_SUB_SECTION`=true 일 때 필수) | `"ELEMS"` | Object | — | 조건부 |
| (4) | 주철근 | `"MAIN_BAR"` | Object | — | **필수** |
| (5) | 단부 전단철근 | `"SHEAR_BAR_END"` | Object | — | **필수** |
| (6) | 중앙부 전단철근 | `"SHEAR_BAR_CEN"` | Object | — | **필수** |
| (7) | 콘크리트면~철근중심 거리 (do) | `"DO"` | Number | — | **필수** |
| (8) | 후프 철근 타입 (`Ties` \| `Spirals`) | `"HOOP_TYPE"` | String (enum) | `"Ties"` | 선택 |

**`MAIN_BAR` 객체** (기둥과 달리 `USE_CORNER`/`NAME_CORNER` 없음)

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 주철근 규격 · 19종 (D4 ~ D57) | `"NAME"` | String (enum) | — | **필수** |
| b | 철근 총 개수 (min 4) | `"NUM"` | Integer | — | **필수** |
| c | 열(row) 수 | `"ROW"` | Integer | — | **필수** |

**`SHEAR_BAR_END` / `SHEAR_BAR_CEN` 객체 (동일 구조)**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 후프 철근 규격 · 19종 (D4 ~ D57) | `"NAME"` | String (enum) | — | **필수** |
| b | 다리 수 (local Y) | `"LEG_Y"` | Integer | — | **필수** |
| c | 다리 수 (local Z) | `"LEG_Z"` | Integer | — | **필수** |
| d | 철근 간격 @ | `"DIST"` | Number | — | **필수** |

**`CREATE_SUB_SECTION == true` 일 때 — `ELEMS` (KEYS / TO / STRUCTURE_GROUP_NAME 중 택1)**

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| a | 요소 ID 배열 | `"KEYS"` | Array[Integer] | — | 선택 |
| b | ID 범위 (예: `"1to160"`) | `"TO"` | String | — | 선택 |
| c | 구조 그룹 이름 | `"STRUCTURE_GROUP_NAME"` | String | — | 선택 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_SECTION": false,
          "MAIN_BAR": { "NAME": "D22", "NUM": 4, "ROW": 2 },
          "SHEAR_BAR_END": { "NAME": "D7", "LEG_Y": 2, "LEG_Z": 2, "DIST": 300 },
          "SHEAR_BAR_CEN": { "NAME": "D22", "LEG_Y": 3, "LEG_Z": 3, "DIST": 300 },
          "DO": 0.05,
          "HOOP_TYPE": "Spirals"
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "REBR": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_SECTION": false,
          "MAIN_BAR": { "NAME": "D22", "NUM": 4, "ROW": 2 },
          "SHEAR_BAR_END": { "NAME": "D7", "LEG_Y": 2, "LEG_Z": 2, "DIST": 300 },
          "SHEAR_BAR_CEN": { "NAME": "D22", "LEG_Y": 3, "LEG_Z": 3, "DIST": 300 },
          "DO": 0.05,
          "HOOP_TYPE": "Spirals"
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
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/REBR"

# 단면 1의 가새 철근 데이터 수정 (POST)
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_SECTION": False,
                    "MAIN_BAR": {"NAME": "D22", "NUM": 4, "ROW": 2},   # USE_CORNER 없음
                    "SHEAR_BAR_END": {"NAME": "D7", "LEG_Y": 2, "LEG_Z": 2, "DIST": 300},
                    "SHEAR_BAR_CEN": {"NAME": "D22", "LEG_Y": 3, "LEG_Z": 3, "DIST": 300},
                    "DO": 0.05,
                    "HOOP_TYPE": "Spirals",   # Ties 또는 Spirals (HOOK_TYPE 없음)
                }
            ]
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 최상위 키 "REBR"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```


---

## 39. `DESIGN/RC/KDS-41-20-2022/BD-ANAL` — RC 보 설계 수행

> **기능:** 지정한 요소 · 단면(또는 전체)에 대해 RC 보 설계 계산을 수행합니다. 결과는 모델에 저장되며 이후 `BD-TABLE` / `BD-REPORT` 로 조회합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BD-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "ALL: all elements, ELEMS: by element No., SECTIONS: by section No.",
          "enum": ["ALL", "ELEMS", "SECTIONS"],
          "default": "ALL"
        },
        "ELEMS": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 수행 대상 (`"ALL"`=전체, `"ELEMS"`=요소번호, `"SECTIONS"`=단면번호) | `"PERFORM_TYPE"` | String (enum) | `"ALL"` | 선택 |
| 3 | 요소 지정 (`ELEMS`/`SECTIONS` 중 하나) — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나 | `"ELEMS"` | Object | — | 조건부 |
| 3.1 | 요소 ID 각각 지정 | `"KEYS"` | Array[Integer] | — | 선택 |
| 3.2 | 요소 ID 범위 (예 `"1to160"`) | `"TO"` | String | — | 선택 |
| 3.3 | 구조 그룹명 | `"STRUCTURE_GROUP_NAME"` | String | — | 선택 |
| 4 | 단면 번호 목록 (`ELEMS`/`SECTIONS` 중 하나) | `"SECTIONS"` | Array[Integer] | — | 조건부 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [79, 80, 81]
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

def rc_post(code, arg):
    # DESIGN/RC 엔드포인트 공통 POST 헬퍼
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 79, 80, 81번 요소에 대해 RC 보 설계 수행
res = rc_post("BD-ANAL", {"PERFORM_TYPE": "ELEMS", "ELEMS": {"KEYS": [79, 80, 81]}})
print("POST:", res.status_code)
print(res.json())   # {"message": "success"}
```

---

## 40. `DESIGN/RC/KDS-41-20-2022/BD-TABLE` — RC 보 설계 테이블

> **기능:** 수행된 RC 보 설계 결과를 표(HEAD/DATA) 형태로 반환합니다. 부재별(MEMB) 또는 단면 속성별(PROP)로 조회할 수 있습니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BD-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["TABLE_TYPE"],
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"], "not": { "required": ["SECTIONS"] } },
        { "required": ["SECTIONS"], "not": { "required": ["ELEMS"] } }
      ],
      "properties": {
        "TABLE_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "PRI_SORT": { "type": "integer", "enum": [0, 1], "default": 1 },
        "RESULT": { "type": "integer", "enum": [0, 1, 2], "default": 0 },
        "TABLE_NAME": { "type": "string", "default": "RC Beam Design Result" },
        "EXPORT_PATH": { "type": "string" },
        "UNIT": { "type": "object" },
        "STYLES": { "type": "object" },
        "COMPONENTS": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 표 타입 (`"MEMB"`=부재별, `"PROP"`=단면별) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 3 | 요소 지정 (`ELEMS`/`SECTIONS` 중 하나) — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` | `"ELEMS"` | Object | — | 조건부 |
| 4 | 단면 번호 목록 | `"SECTIONS"` | Array[Integer] | — | 조건부 |
| 5 | 정렬 기준 (`0`=SECT, `1`=MEMB) — `TABLE_TYPE`=MEMB일 때 | `"PRI_SORT"` | Integer | `1` | 선택 |
| 6 | 결과 필터 (`0`=All, `1`=OK, `2`=NG) | `"RESULT"` | Integer | `0` | 선택 |
| 7 | 응답 표 제목 | `"TABLE_NAME"` | String | `"RC Beam Design Result"` | 선택 |
| 8 | 결과 파일 저장 경로 | `"EXPORT_PATH"` | String | — | 선택 |
| 9 | 단위 설정 (`FORCE`/`DIST`/`HEAT`/`TEMP`) | `"UNIT"` | Object | System | 선택 |
| 10 | 숫자 포맷 (`FORMAT`, `PLACE` 0~15) | `"STYLES"` | Object | System | 선택 |
| 11 | 표시 열 목록 (아래 HEAD 참조) | `"COMPONENTS"` | Array[String] | All | 선택 |

**응답 `HEAD` 열 설명** (25개 열)

| 열 | 의미 |
|----|------|
| `MEMB` / `SECT` | 부재 번호 / 단면 번호 |
| `Span` / `Section` | 스팬 길이 / 단면명 |
| `Bc` / `Hc` | 단면 폭 / 높이 |
| `bf` / `hf` | 플랜지 폭 / 두께 |
| `fck` / `fy` / `fys` | 콘크리트 · 주철근 · 전단철근 설계강도 |
| `POS` | 검토 위치 (`I`/`M`/`J`) |
| `N(-)/Mu` / `LCB_NegMu` / `AsTop` / `Rebar_Top` | 부모멘트 소요강도 · 지배 하중조합 · 상부 철근량 · 상부 배근 |
| `P(+)/Mu` / `LCB_PosMu` / `AsBot` / `Rebar_Bot` | 정모멘트 소요강도 · 지배 하중조합 · 하부 철근량 · 하부 배근 |
| `Vu` / `LCB_Vu` / `AsV` / `Stirrup` | 전단 소요강도 · 지배 하중조합 · 전단 철근량 · 스터럽 배근 |
| `CHK` | 판정 (`OK`/`NG`) |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_NAME": "RC Beam Design Result",
    "COMPONENTS": [
      "MEMB", "SECT", "Span", "Section", "Bc", "Hc", "bf", "hf",
      "fck", "fy", "fys", "POS", "N(-)/Mu", "LCB_NegMu", "AsTop",
      "Rebar_Top", "P(+)/Mu", "LCB_PosMu", "AsBot", "Rebar_Bot",
      "Vu", "LCB_Vu", "AsV", "Stirrup", "CHK"
    ],
    "ELEMS": { "KEYS": [859, 860] }
  }
}
```

**Response Body**

```json
{
  "RC Beam Design Result": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB", "SECT", "Span", "Section", "Bc", "Hc", "bf", "hf",
      "fck", "fy", "fys", "POS", "N(-)/Mu", "LCB_NegMu", "AsTop",
      "Rebar_Top", "P(+)/Mu", "LCB_PosMu", "AsBot", "Rebar_Bot",
      "Vu", "LCB_Vu", "AsV", "Stirrup", "CHK"
    ],
    "DATA": [
      [
        "859", "511", "10.200", "RG1", "0.4500", "0.7000", "0.0000", "0.0000",
        "24000.0", "400000", "400000", "I", "358.563", "6", "0.0018",
        "4-D25", "117.551", "6", "0.0007", "3-D25",
        "211.962", "6", "0.0004", "3-D13 @310", "OK"
      ],
      [
        "859", "511", "10.200", "RG1", "0.4500", "0.7000", "0.0000", "0.0000",
        "24000.0", "400000", "400000", "J", "438.788", "6", "0.0022",
        "5-D25", "80.1426", "8", "0.0005", "3-D25",
        "227.693", "6", "0.0004", "3-D13 @310", "OK"
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# RC 보 설계 결과 표 조회 (부재별, 859·860번)
res = rc_post("BD-TABLE", {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "ELEMS": {"KEYS": [859, 860]},
})
table = res.json()["RC Beam Design Result"]
head = table["HEAD"]
for row in table["DATA"]:
    # HEAD 열과 DATA 값을 짝지어 출력
    print(dict(zip(head, row)))
```

---

## 41. `DESIGN/RC/KDS-41-20-2022/BD-REPORT` — RC 보 설계 리포트

> **기능:** RC 보 설계 결과를 Graphic(JPG) · Detail(DOC) · Summary(TXT) 형식의 파일로 출력합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BD-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["REPORT_TYPE", "EXPORT_PATH", "OUTPUT_NAME"],
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "REPORT_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "CURRENT_MODE_MEMB": { "type": "string", "enum": ["Graphic", "Detail", "Summary"] },
        "CURRENT_MODE_PROP": { "type": "string", "enum": ["Graphic", "Summary"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "DETAIL_POSITIONS": {
          "type": "object",
          "properties": {
            "END_I": { "type": "boolean", "default": true },
            "MID": { "type": "boolean", "default": false },
            "END_J": { "type": "boolean", "default": false }
          }
        },
        "EXPORT_PATH": { "type": "string" },
        "OUTPUT_NAME": { "type": "string" }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 리포트 타입 (`"MEMB"`=부재별, `"PROP"`=단면별) | `"REPORT_TYPE"` | String (enum) | — | **필수** |
| 3 | 출력 모드 (부재별) — `"Graphic"`/`"Detail"`/`"Summary"` | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 조건부 (MEMB) |
| 4 | 출력 모드 (단면별) — `"Graphic"`/`"Summary"` | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 조건부 (PROP) |
| 5 | 요소 지정 (`ELEMS`/`SECTIONS` 중 하나) | `"ELEMS"` | Object | — | 조건부 |
| 6 | 단면 번호 목록 | `"SECTIONS"` | Array[Integer] | — | 조건부 |
| 7 | Detail 출력 위치 (`END_I`/`MID`/`END_J`) — Detail 모드일 때 | `"DETAIL_POSITIONS"` | Object | — | 선택 |
| 8 | 저장 디렉터리 경로 (예 `C:\\MIDAS\\Report\\`) | `"EXPORT_PATH"` | String | — | **필수** |
| 9 | 출력 파일 기본 이름 (다중 요소 시 인덱스·요소번호 접두어 부가) | `"OUTPUT_NAME"` | String | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "out.jpg",
    "ELEMS": {
      "KEYS": [79]
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 79번 보 설계 결과를 Graphic(JPG) 리포트로 출력
res = rc_post("BD-REPORT", {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "out.jpg",
    "ELEMS": {"KEYS": [79]},
})
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...", "MESSAGE": ""}
```

---

## 42. `DESIGN/RC/KDS-41-20-2022/CD-ANAL` — RC 기둥 설계 수행

> **기능:** 지정한 요소 · 단면(또는 전체)에 대해 RC 기둥 설계 계산을 수행합니다. 결과는 이후 `CD-TABLE` / `CD-REPORT` 로 조회합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CD-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "enum": ["ALL", "ELEMS", "SECTIONS"],
          "default": "ALL"
        },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 수행 대상 (`"ALL"`/`"ELEMS"`/`"SECTIONS"`) | `"PERFORM_TYPE"` | String (enum) | `"ALL"` | 선택 |
| 3 | 요소 지정 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나 | `"ELEMS"` | Object | — | 조건부 |
| 4 | 단면 번호 목록 | `"SECTIONS"` | Array[Integer] | — | 조건부 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL",
    "ELEMS": {
      "KEYS": [105, 915]
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 전체 기둥 요소에 대해 RC 기둥 설계 수행
res = rc_post("CD-ANAL", {"PERFORM_TYPE": "ALL"})
print("POST:", res.status_code, res.json())   # {"message": "success"}
```

---

## 43. `DESIGN/RC/KDS-41-20-2022/CD-TABLE` — RC 기둥 설계 테이블

> **기능:** 수행된 RC 기둥 설계 결과를 표(HEAD/DATA) 형태로 반환합니다. P-M 상관 및 전단 검토 결과를 포함합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CD-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["TABLE_TYPE"],
      "additionalProperties": false,
      "properties": {
        "TABLE_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "PRI_SORT": { "type": "integer", "enum": [0, 1], "default": 1 },
        "RESULT": { "type": "integer", "enum": [0, 1, 2], "default": 0 },
        "TABLE_NAME": { "type": "string" },
        "EXPORT_PATH": { "type": "string" },
        "UNIT": { "type": "object" },
        "STYLES": { "type": "object" },
        "COMPONENTS": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 표 타입 (`"MEMB"`/`"PROP"`) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 3 | 요소 지정 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나 | `"ELEMS"` | Object | — | 조건부 |
| 4 | 단면 번호 목록 | `"SECTIONS"` | Array[Integer] | — | 조건부 |
| 5 | 정렬 기준 (`0`=SECT, `1`=MEMB) | `"PRI_SORT"` | Integer | `1` | 선택 |
| 6 | 결과 필터 (`0`=All, `1`=OK, `2`=NG) | `"RESULT"` | Integer | `0` | 선택 |
| 7 | 응답 표 제목 · 저장 경로 · 단위 · 포맷 · 표시 열 | `"TABLE_NAME"`/`"EXPORT_PATH"`/`"UNIT"`/`"STYLES"`/`"COMPONENTS"` | 각 타입 | — | 선택 |

**응답 `HEAD` 열 설명** (32개 열)

| 열 | 의미 |
|----|------|
| `MEMB` / `SECT` / `Section` | 부재 번호 / 단면 번호 / 단면명 |
| `Bc` / `Hc` / `Height` | 단면 폭 / 높이 / 부재 길이 |
| `fck` / `fy` / `fys` | 콘크리트 · 주철근 · 전단철근 설계강도 |
| `LCB` | 지배 하중조합 번호 |
| `phiPn.max` / `Pu` / `phiPn` / `Rat-P` | 최대 설계축강도 · 소요축력 · 설계축강도 · 축력비 |
| `Mc` / `phiMn` / `Rat-M` | 소요모멘트 · 설계휨강도 · 휨비 |
| `Mc/Pu` / `Mcz/Mcy` | 편심 · 이축 모멘트비 |
| `Ast` / `V-Rebar` | 주철근량 · 주철근 배근 |
| `LCB_Vu_end` / `LCB_Vu_mid` | 단부 · 중앙부 전단 지배 하중조합 |
| `Vu.end` / `Vu.mid` / `Rat-V.end` / `Rat-V.mid` | 단부 · 중앙부 소요전단 및 전단비 |
| `As-H.end` / `As-H.mid` / `H-Rebar.end` / `H-Rebar.mid` | 단부 · 중앙부 횡철근량 및 배근 |
| `CHK` | 판정 (`OK`/`NG`) |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0
  }
}
```

**Response Body**

```json
{
  "Result Table": {
    "FORCE": "KGF",
    "DIST": "M",
    "HEAD": [
      "MEMB", "SECT", "Section", "Bc", "Hc", "fck", "Height", "fy", "fys",
      "LCB", "phiPn.max", "Pu", "phiPn", "Rat-P", "Mc", "phiMn", "Rat-M",
      "Mc/Pu", "Mcz/Mcy", "Ast", "V-Rebar", "LCB_Vu_end", "LCB_Vu_mid",
      "Vu.end", "Vu.mid", "Rat-V.end", "Rat-V.mid", "As-H.end", "As-H.mid",
      "H-Rebar.end", "H-Rebar.mid", "CHK"
    ],
    "DATA": [
      [
        "915", "100", "D300", "0.0000", "0.3000", "3059149", "4.0000",
        "6.1E+07", "4.1E+07", "7", "118735", "18065.4", "48178.0", "0.375",
        "1750.05", "4666.58", "0.375", "0.09687", "54.390346", "0.0008",
        "6-0-D13", "7", "7", "412.936", "412.936", "0.027", "0.027",
        "0.0000", "0.0000", "2-D13 @200", "2-D13 @200", "OK"
      ],
      [
        "1059", "100", "D300", "0.0000", "0.3000", "3059149", "4.0000",
        "6.1E+07", "4.1E+07", "7", "119777", "9088.78", "14275.4", "0.637",
        "3543.83", "5584.15", "0.635", "0.38991", "86.471081", "0.0008",
        "4-0-D16", "7", "7", "884.284", "884.284", "0.106", "0.106",
        "0.0000", "0.0000", "2-D7  @200", "2-D7  @200", "OK"
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# RC 기둥 설계 결과 표 조회 (부재별 정렬, NG만 필터하려면 RESULT=2)
res = rc_post("CD-TABLE", {"TABLE_TYPE": "MEMB", "PRI_SORT": 1, "RESULT": 0})
table = res.json()["Result Table"]
head = table["HEAD"]
chk_idx = head.index("CHK")
for row in table["DATA"]:
    # 판정(CHK)이 NG인 기둥만 강조 출력
    mark = "  <-- 검토" if row[chk_idx] != "OK" else ""
    print(row[0], row[chk_idx], mark)
```

---

## 44. `DESIGN/RC/KDS-41-20-2022/CD-REPORT` — RC 기둥 설계 리포트

> **기능:** RC 기둥 설계 결과를 Graphic(JPG) · Detail(DOC) · Summary(TXT) · PM Curve(JPG) 형식의 파일로 출력합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CD-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["REPORT_TYPE", "EXPORT_PATH", "OUTPUT_NAME"],
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "REPORT_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "enum": ["Graphic", "Detail", "Summary", "PMCurve"]
        },
        "CURRENT_MODE_PROP": { "type": "string", "enum": ["Graphic", "Summary"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "EXPORT_PATH": { "type": "string" },
        "OUTPUT_NAME": { "type": "string" }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 리포트 타입 (`"MEMB"`/`"PROP"`) | `"REPORT_TYPE"` | String (enum) | — | **필수** |
| 3 | 출력 모드 (부재별) — `"Graphic"`/`"Detail"`/`"Summary"`/`"PMCurve"` | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 조건부 (MEMB) |
| 4 | 출력 모드 (단면별) — `"Graphic"`/`"Summary"` | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 조건부 (PROP) |
| 5 | 요소 지정 (`ELEMS`/`SECTIONS` 중 하나) | `"ELEMS"` | Object | — | 조건부 |
| 6 | 단면 번호 목록 | `"SECTIONS"` | Array[Integer] | — | 조건부 |
| 7 | 저장 디렉터리 경로 | `"EXPORT_PATH"` | String | — | **필수** |
| 8 | 출력 파일 기본 이름 | `"OUTPUT_NAME"` | String | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result",
    "OUTPUT_NAME": "name",
    "ELEMS": {
      "KEYS": [291, 292]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Resultname",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 291·292번 기둥의 P-M 상관도(PMCurve) 리포트 출력
res = rc_post("CD-REPORT", {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "pm.jpg",
    "ELEMS": {"KEYS": [291, 292]},
})
print(res.json())
```

---

## 45. `DESIGN/RC/KDS-41-20-2022/BRD-ANAL` — RC 가새 설계 수행

> **기능:** 지정한 요소 · 단면(또는 전체)에 대해 RC 가새(Brace) 설계 계산을 수행합니다. 결과는 이후 `BRD-TABLE` / `BRD-REPORT` 로 조회합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRD-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "enum": ["ALL", "ELEMS", "SECTIONS"],
          "default": "ALL"
        },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 수행 대상 (`"ALL"`/`"ELEMS"`/`"SECTIONS"`) | `"PERFORM_TYPE"` | String (enum) | `"ALL"` | 선택 |
| 3 | 요소 지정 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나 | `"ELEMS"` | Object | — | 조건부 |
| 4 | 단면 번호(또는 단면명) 목록 | `"SECTIONS"` | Array | — | 조건부 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "SECTIONS",
    "SECTIONS": ["G1"]
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# "G1" 단면 가새에 대해 RC 가새 설계 수행
res = rc_post("BRD-ANAL", {"PERFORM_TYPE": "SECTIONS", "SECTIONS": ["G1"]})
print("POST:", res.status_code, res.json())   # {"message": "success"}
```

---

## 46. `DESIGN/RC/KDS-41-20-2022/BRD-TABLE` — RC 가새 설계 테이블

> **기능:** 수행된 RC 가새 설계 결과를 표(HEAD/DATA) 형태로 반환합니다. 축력-휨(P-M) 및 전단 검토 결과를 포함합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRD-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["TABLE_TYPE"],
      "additionalProperties": false,
      "properties": {
        "TABLE_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "PRI_SORT": { "type": "integer", "enum": [0, 1], "default": 1 },
        "RESULT": { "type": "integer", "enum": [0, 1, 2], "default": 0 },
        "TABLE_NAME": { "type": "string" },
        "EXPORT_PATH": { "type": "string" },
        "UNIT": { "type": "object" },
        "STYLES": { "type": "object" },
        "COMPONENTS": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 표 타입 (`"MEMB"`/`"PROP"`) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 3 | 요소 지정 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나 | `"ELEMS"` | Object | — | 조건부 |
| 4 | 단면 번호 목록 | `"SECTIONS"` | Array[Integer] | — | 조건부 |
| 5 | 정렬 기준 (`0`=SECT, `1`=MEMB) | `"PRI_SORT"` | Integer | `1` | 선택 |
| 6 | 결과 필터 (`0`=All, `1`=OK, `2`=NG) | `"RESULT"` | Integer | `0` | 선택 |
| 7 | 표 제목 · 저장 경로 · 단위 · 포맷 · 표시 열 | `"TABLE_NAME"`/`"EXPORT_PATH"`/`"UNIT"`/`"STYLES"`/`"COMPONENTS"` | 각 타입 | — | 선택 |

**응답 `HEAD` 열 설명** (28개 열)

| 열 | 의미 |
|----|------|
| `MEMB` / `SECT` / `Section` | 부재 번호 / 단면 번호 / 단면명 |
| `Bc` / `Hc` / `Height` | 단면 폭 / 높이 / 부재 길이 |
| `fck` / `fy` / `fys` | 콘크리트 · 주철근 · 전단철근 설계강도 |
| `LCB` | 지배 하중조합 번호 |
| `phiPn.max` / `Pu` / `phiPn` / `Rat-P` | 최대 설계축강도 · 소요축력 · 설계축강도 · 축력비 |
| `Mc` / `phiMn` / `Rat-M` / `Rat-My` / `Rat-Mz` | 소요모멘트 · 설계휨강도 · 휨비 · y·z축 휨비 |
| `Mc/Pu` / `Mcz/Mcy` | 편심 · 이축 모멘트비 |
| `Ast` / `V-Rebar` | 주철근량 · 주철근 배근 |
| `Vu` / `Rat-V` | 소요전단 · 전단비 |
| `As-H` / `H-Rebar` | 횡철근량 · 횡철근 배근 |
| `CHK` | 판정 (`OK`/`NG`) |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "SECTIONS": [3],
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_NAME": "RC Brace Design Result"
  }
}
```

**Response Body**

```json
{
  "RC Brace Design Result": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB", "SECT", "Section", "Bc", "Hc", "Height", "fck", "fy", "fys",
      "LCB", "phiPn.max", "Pu", "phiPn", "Rat-P", "Mc", "phiMn", "Rat-M",
      "Rat-My", "Rat-Mz", "Mc/Pu", "Mcz/Mcy", "Ast", "V-Rebar", "Vu",
      "Rat-V", "As-H", "H-Rebar", "CHK"
    ],
    "DATA": [
      [
        "789", "411", "G1", "0.4000", "0.7000", "10.200", "24000.0",
        "400000", "400000", "6", "4039.99", "0.00000", "-", "0.000",
        "476.307", "515.983", "0.923", "0.923", "0.000", "-", "0.000000",
        "0.0054", "14-5-D22", "228.405", "0.790", "0.0004", "2-D10 @200", "OK"
      ],
      [
        "873", "513", "RG3", "0.6000", "0.8000", "9.0000", "24000.0",
        "400000", "400000", "6", "6467.23", "0.00000", "-", "0.000",
        "787.844", "789.010", "0.999", "0.999", "0.000", "-", "0.000000",
        "0.0070", "18-5-D22", "392.386", "0.993", "0.0006", "2-D10 @240", "OK"
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 3번 단면 가새 설계 결과 표 조회
res = rc_post("BRD-TABLE", {
    "TABLE_TYPE": "MEMB",
    "SECTIONS": [3],
    "PRI_SORT": 1,
    "RESULT": 0,
})
table = res.json()["RC Brace Design Result"]
head = table["HEAD"]
for row in table["DATA"]:
    print(dict(zip(head, row)))
```

---

## 47. `DESIGN/RC/KDS-41-20-2022/BRD-REPORT` — RC 가새 설계 리포트

> **기능:** RC 가새 설계 결과를 Graphic(JPG) · Detail(DOC) · Summary(TXT) · PM Curve(JPG) 형식의 파일로 출력합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRD-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["REPORT_TYPE", "EXPORT_PATH", "OUTPUT_NAME"],
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "REPORT_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "enum": ["Graphic", "Detail", "Summary", "PMCurve"]
        },
        "CURRENT_MODE_PROP": { "type": "string", "enum": ["Graphic", "Summary"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "EXPORT_PATH": { "type": "string" },
        "OUTPUT_NAME": { "type": "string" }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 리포트 타입 (`"MEMB"`/`"PROP"`) | `"REPORT_TYPE"` | String (enum) | — | **필수** |
| 3 | 출력 모드 (부재별) — `"Graphic"`/`"Detail"`/`"Summary"`/`"PMCurve"` | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 조건부 (MEMB) |
| 4 | 출력 모드 (단면별) — `"Graphic"`/`"Summary"` | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 조건부 (PROP) |
| 5 | 요소 지정 (`ELEMS`/`SECTIONS` 중 하나) | `"ELEMS"` | Object | — | 조건부 |
| 6 | 단면 번호 목록 | `"SECTIONS"` | Array[Integer] | — | 조건부 |
| 7 | 저장 디렉터리 경로 | `"EXPORT_PATH"` | String | — | **필수** |
| 8 | 출력 파일 기본 이름 | `"OUTPUT_NAME"` | String | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "pm.jpg",
    "ELEMS": {
      "KEYS": [789]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\pm.jpg",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 789번 가새의 P-M 상관도(PMCurve) 리포트 출력
res = rc_post("BRD-REPORT", {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "pm.jpg",
    "ELEMS": {"KEYS": [789]},
})
print(res.json())
```

---

## 48. `DESIGN/RC/KDS-41-20-2022/WD-ANAL` — RC 벽체 설계 수행

> **기능:** 지정한 벽체 ID · 층(Story) 조합에 대해 RC 벽체(Wall) 설계 계산을 수행합니다. 벽체는 요소가 아니라 `WALL_IDS` + `STORY` 조합으로 지정합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WD-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "SELECTIONS": {
          "type": "array",
          "description": "Wall ID and Story pairs to design",
          "items": {
            "type": "object",
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "properties": {
                  "KEYS": { "type": "array", "items": { "type": "integer" } },
                  "TO": { "type": "string" }
                }
              },
              "STORY": { "type": "array", "items": { "type": "string" } }
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
| 2 | 벽체 ID · 층 조합 목록 | `"SELECTIONS"` | Array[Object] | — | **필수** |
| 2.1 | 벽체 ID 지정 (`KEYS`=각각, `TO`=범위 예 `"10to20"`) | `"WALL_IDS"` | Object | — | 필수 |
| 2.2 | 대상 층 이름 목록 (예 `["B1F", "1F"]`) | `"STORY"` | Array[String] | — | 필수 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "SELECTIONS": [
      {
        "WALL_IDS": { "KEYS": [1, 2, 3] },
        "STORY": ["B1F", "1F"]
      },
      {
        "WALL_IDS": { "TO": "10to20" },
        "STORY": ["2F", "3F"]
      }
    ]
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 벽체 1·2·3 (B1F·1F), 10~20 (2F·3F) 조합에 대해 RC 벽체 설계 수행
res = rc_post("WD-ANAL", {
    "SELECTIONS": [
        {"WALL_IDS": {"KEYS": [1, 2, 3]}, "STORY": ["B1F", "1F"]},
        {"WALL_IDS": {"TO": "10to20"}, "STORY": ["2F", "3F"]},
    ]
})
print("POST:", res.status_code, res.json())   # {"message": "success"}
```

---

## 49. `DESIGN/RC/KDS-41-20-2022/WD-TABLE` — RC 벽체 설계 테이블

> **기능:** 수행된 RC 벽체 설계 결과를 표 형태로 반환합니다. 응답은 `data` 객체 안에 `COMPONENTS`(열 정의)와 `ROWS`(행 객체 배열)를 담는 구조입니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WD-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["TABLE_TYPE"],
      "additionalProperties": false,
      "properties": {
        "TABLE_TYPE": { "type": "string", "enum": ["WID+STORY", "WID"] },
        "SELECTIONS": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "properties": {
                  "KEYS": { "type": "array", "items": { "type": "integer" } },
                  "TO": { "type": "string" }
                }
              },
              "STORY": { "type": "array", "items": { "type": "string" } }
            }
          }
        },
        "PRI_SORT": { "type": "integer", "enum": [0, 1], "default": 1 },
        "RESULT": { "type": "integer", "enum": [0, 1, 2], "default": 0 },
        "TABLE_NAME": { "type": "string" },
        "UNIT": { "type": "object" },
        "STYLES": { "type": "object" },
        "COMPONENTS": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 표 타입 (`"WID+STORY"`=벽체+층별, `"WID"`=벽체별) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 3 | 벽체 ID · 층 조합 목록 (`WALL_IDS`+`STORY`) | `"SELECTIONS"` | Array[Object] | — | 선택 |
| 4 | 정렬 기준 (`0`/`1`) | `"PRI_SORT"` | Integer | `1` | 선택 |
| 5 | 결과 필터 (`0`=All, `1`=OK, `2`=NG) | `"RESULT"` | Integer | `0` | 선택 |
| 6 | 표 제목 · 단위 · 포맷 · 표시 열 | `"TABLE_NAME"`/`"UNIT"`/`"STYLES"`/`"COMPONENTS"` | 각 타입 | — | 선택 |

**응답 `COMPONENTS`(열) 설명** (13개 열)

| 열 | 의미 |
|----|------|
| `WID` / `Story` / `Wall Mark` | 벽체 ID / 층 / 벽체 부호 |
| `Pu` / `Rat-Py` / `Rat-Pz` | 소요축력 · y·z방향 축력비 |
| `Mcy` / `Mcz` / `Rat-My` / `Rat-Mz` | y·z축 소요모멘트 및 휨비 |
| `Vu` / `Rat-V` | 소요전단 · 전단비 |
| `CHK` | 판정 (`OK`/`NG`) |

> **참고:** 벽체 테이블은 다른 부재와 달리 응답이 `HEAD`/`DATA` 배열이 아니라 `data.COMPONENTS`(열 이름 배열) + `data.ROWS`(열 이름을 키로 갖는 객체 배열) 구조입니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "WID+STORY",
    "SELECTIONS": [
      {
        "WALL_IDS": { "KEYS": [1, 3] },
        "STORY": ["3F"]
      },
      {
        "WALL_IDS": { "TO": "10to12" },
        "STORY": ["3F"]
      }
    ],
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_NAME": "RC Wall Design Result",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "COMPONENTS": [
      "WID", "Story", "Wall Mark", "Pu", "Rat-Py", "Rat-Pz",
      "Mcy", "Mcz", "Rat-My", "Rat-Mz", "Vu", "Rat-V", "CHK"
    ]
  }
}
```

**Response Body**

```json
{
  "status": "success",
  "message": "RC Wall Design Result table generated successfully.",
  "data": {
    "TABLE_NAME": "RC Wall Design Result",
    "TABLE_TYPE": "WID+STORY",
    "UNIT": { "FORCE": "kN", "DIST": "m", "MOMENT": "kN·m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "PRI_SORT": 1,
    "RESULT": 0,
    "TOTAL_COUNT": 5,
    "COMPONENTS": [
      "WID", "Story", "Wall Mark", "Pu", "Rat-Py", "Rat-Pz",
      "Mcy", "Mcz", "Rat-My", "Rat-Mz", "Vu", "Rat-V", "CHK"
    ],
    "ROWS": [
      {
        "WID": 1, "Story": "3F", "Wall Mark": "W1",
        "Pu": "1425.000", "Rat-Py": "0.242", "Rat-Pz": "0.226",
        "Mcy": "318.000", "Mcz": "276.000", "Rat-My": "0.323", "Rat-Mz": "0.281",
        "Vu": "184.000", "Rat-V": "0.254", "CHK": "OK"
      },
      {
        "WID": 10, "Story": "3F", "Wall Mark": "W10",
        "Pu": "4580.000", "Rat-Py": "0.684", "Rat-Pz": "0.652",
        "Mcy": "1450.000", "Mcz": "1125.000", "Rat-My": "0.768", "Rat-Mz": "0.704",
        "Vu": "642.000", "Rat-V": "0.726", "CHK": "OK"
      }
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 3F층 벽체 1·3·10~12 설계 결과 표 조회
res = rc_post("WD-TABLE", {
    "TABLE_TYPE": "WID+STORY",
    "SELECTIONS": [
        {"WALL_IDS": {"KEYS": [1, 3]}, "STORY": ["3F"]},
        {"WALL_IDS": {"TO": "10to12"}, "STORY": ["3F"]},
    ],
    "PRI_SORT": 1,
    "RESULT": 0,
})
data = res.json()["data"]
# 응답은 COMPONENTS(열) + ROWS(행 객체) 구조
for row in data["ROWS"]:
    print(row["WID"], row["Story"], row["Wall Mark"], row["CHK"])
```

---

## 50. `DESIGN/RC/KDS-41-20-2022/WD-REPORT` — RC 벽체 설계 리포트

> **기능:** RC 벽체 설계 결과를 Graphic(JPG) · Detail(DOC) · Summary(TXT) · PM Curve(JPG) 형식의 파일로 출력합니다. 벽체는 `SELECTIONS`(벽체 ID + 층)으로 지정합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WD-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["REPORT_TYPE", "SELECTIONS", "EXPORT_PATH", "OUTPUT_NAME"],
      "additionalProperties": false,
      "properties": {
        "REPORT_TYPE": { "type": "string", "enum": ["WID+STORY", "WID"] },
        "CURRENT_MODE_WID_STORY": {
          "type": "string",
          "enum": ["Graphic", "Detail", "Summary", "PMCurve"]
        },
        "CURRENT_MODE_WID": {
          "type": "string",
          "enum": ["Graphic", "Detail", "Summary", "PMCurve"]
        },
        "SELECTIONS": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "properties": {
                  "KEYS": { "type": "array", "items": { "type": "integer" } },
                  "TO": { "type": "string" }
                }
              },
              "STORY": { "type": "array", "items": { "type": "string" } }
            }
          }
        },
        "EXPORT_PATH": { "type": "string" },
        "OUTPUT_NAME": { "type": "string" }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 리포트 타입 (`"WID+STORY"`/`"WID"`) | `"REPORT_TYPE"` | String (enum) | — | **필수** |
| 3 | 출력 모드 (벽체+층) — `"Graphic"`/`"Detail"`/`"Summary"`/`"PMCurve"` | `"CURRENT_MODE_WID_STORY"` | String (oneOf) | — | 조건부 (WID+STORY) |
| 4 | 출력 모드 (벽체) — 동일 enum | `"CURRENT_MODE_WID"` | String (oneOf) | — | 조건부 (WID) |
| 5 | 벽체 ID · 층 조합 목록 (`WALL_IDS`+`STORY`) | `"SELECTIONS"` | Array[Object] | — | **필수** |
| 6 | 저장 디렉터리 경로 | `"EXPORT_PATH"` | String | — | **필수** |
| 7 | 출력 파일 기본 이름 | `"OUTPUT_NAME"` | String | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "WID+STORY",
    "CURRENT_MODE_WID_STORY": "Detail",
    "SELECTIONS": [
      {
        "WALL_IDS": { "KEYS": [101, 102] },
        "STORY": ["1F", "2F"]
      },
      {
        "WALL_IDS": { "TO": "201to205" },
        "STORY": ["3F"]
      }
    ],
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "RC_Wall_Report"
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\result.jpg",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 벽체 101·102(1F·2F), 201~205(3F) 설계 결과를 Detail(DOC) 리포트로 출력
res = rc_post("WD-REPORT", {
    "REPORT_TYPE": "WID+STORY",
    "CURRENT_MODE_WID_STORY": "Detail",
    "SELECTIONS": [
        {"WALL_IDS": {"KEYS": [101, 102]}, "STORY": ["1F", "2F"]},
        {"WALL_IDS": {"TO": "201to205"}, "STORY": ["3F"]},
    ],
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "RC_Wall_Report",
})
print(res.json())
```

---

## 51. `DESIGN/RC/KDS-41-20-2022/HCD-ANAL` — RC 헌치보 설계 수행

> **기능:** 지정한 헌치보(Haunched Beam) 요소에 대해 RC 설계 계산을 수행합니다. 결과는 이후 `HCD-TABLE` / `HCD-REPORT` 로 조회합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/HCD-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "properties": {
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
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
| 2 | 헌치보 요소 지정 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나 | `"ELEMS"` | Object | — | 선택 |
| 2.1 | 요소 ID 각각 지정 | `"KEYS"` | Array[Integer] | — | 선택 |
| 2.2 | 요소 ID 범위 (예 `"1to160"`) | `"TO"` | String | — | 선택 |
| 2.3 | 구조 그룹명 | `"STRUCTURE_GROUP_NAME"` | String | — | 선택 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "ELEMS": {
      "KEYS": [1065, 1073]
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 1065·1073번 헌치보에 대해 RC 헌치보 설계 수행
res = rc_post("HCD-ANAL", {"ELEMS": {"KEYS": [1065, 1073]}})
print("POST:", res.status_code, res.json())   # {"message": "success"}
```

---

## 52. `DESIGN/RC/KDS-41-20-2022/HCD-TABLE` — RC 헌치보 설계 테이블

> **기능:** 수행된 RC 헌치보 설계 결과를 표(HEAD/DATA) 형태로 반환합니다. 헌치 구간(T/N 구간)별 위치(`POS`)에 따라 휨·전단 검토 결과를 제공합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/HCD-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "RESULT": { "type": "integer", "enum": [0, 1, 2], "default": 0 },
        "TABLE_NAME": { "type": "string" },
        "EXPORT_PATH": { "type": "string" },
        "UNIT": { "type": "object" },
        "STYLES": { "type": "object" },
        "COMPONENTS": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 헌치보 요소 지정 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나 | `"ELEMS"` | Object | — | 선택 |
| 3 | 결과 필터 (`0`=All, `1`=OK, `2`=NG) | `"RESULT"` | Integer | `0` | 선택 |
| 4 | 표 제목 · 저장 경로 · 단위 · 포맷 · 표시 열 | `"TABLE_NAME"`/`"EXPORT_PATH"`/`"UNIT"`/`"STYLES"`/`"COMPONENTS"` | 각 타입 | — | 선택 |

**응답 `HEAD` 열 설명** (20개 열)

| 열 | 의미 |
|----|------|
| `HCBM` / `Section` | 헌치보 부재 번호 / 구간 단면명 (`T1`/`N`/`T2` 등) |
| `Bc-I` / `Hc-I` / `Bc-J` / `Hc-J` | I단 · J단 단면 폭 / 높이 |
| `POS` | 검토 위치 (1~n 분할 지점) |
| `N(-)Mu` / `LCB_NegMu` / `AsTop` / `Rebar_Top` | 부모멘트 소요강도 · 지배 하중조합 · 상부 철근량 · 상부 배근 |
| `P(+)Mu` / `LCB_PosMu` / `AsBot` / `Rebar_Bot` | 정모멘트 소요강도 · 지배 하중조합 · 하부 철근량 · 하부 배근 |
| `Vu` / `LCB_Vu` / `AsV` / `Stirrup` | 전단 소요강도 · 지배 하중조합 · 전단 철근량 · 스터럽 배근 |
| `CHK` | 판정 (`OK`/`NG`) |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "RESULT": 0,
    "COMPONENTS": [
      "HCBM", "Section", "Bc-I", "Hc-I", "Bc-J", "Hc-J", "POS",
      "N(-)Mu", "LCB_NegMu", "AsTop", "Rebar_Top", "P(+)Mu",
      "LCB_PosMu", "AsBot", "Rebar_Bot", "Vu", "LCB_Vu", "AsV",
      "Stirrup", "CHK"
    ],
    "ELEMS": { "KEYS": [1065, 1073] }
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
      "HCBM", "Section", "Bc-I", "Hc-I", "Bc-J", "Hc-J", "POS",
      "N(-)Mu", "LCB_NegMu", "AsTop", "Rebar_Top", "P(+)Mu",
      "LCB_PosMu", "AsBot", "Rebar_Bot", "Vu", "LCB_Vu", "AsV",
      "Stirrup", "CHK"
    ],
    "DATA": [
      [
        "1065", "T1", "1.0000", "0.7000", "1.0000", "0.5000", "1",
        "1102.57", "6", "0.0037", "10-D22", "0.00000", "200", "0.0000",
        "2-D22", "220.513", "6", "0.0009", "2-D10 @160", "OK"
      ],
      [
        "1065", "T2", "1.0000", "0.5000", "1.0000", "0.7000", "7",
        "50.1371", "5", "0.0002", "9-D22", "0.00000", "200", "0.0000",
        "2-D22", "47.9404", "5", "0.0000", "2-D10 @210", "OK"
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 1065·1073번 헌치보 설계 결과 표 조회
res = rc_post("HCD-TABLE", {"RESULT": 0, "ELEMS": {"KEYS": [1065, 1073]}})
table = res.json()["Result Table"]
head = table["HEAD"]
for row in table["DATA"]:
    # 헌치보는 구간(Section)·위치(POS)별로 여러 행이 출력됨
    print(dict(zip(head, row)))
```

---

## 53. `DESIGN/RC/KDS-41-20-2022/HCD-REPORT` — RC 헌치보 설계 리포트

> **기능:** RC 헌치보 설계 결과를 Graphic(JPG) 형식의 파일로 출력합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/HCD-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["CURRENT_MODE", "EXPORT_PATH", "OUTPUT_NAME"],
      "additionalProperties": false,
      "properties": {
        "CURRENT_MODE": { "type": "string", "enum": ["Graphic"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "EXPORT_PATH": { "type": "string" },
        "OUTPUT_NAME": { "type": "string" }
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 출력 모드 (`"Graphic"`=JPG 이미지) | `"CURRENT_MODE"` | String (enum) | — | **필수** |
| 3 | 헌치보 요소 지정 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나 | `"ELEMS"` | Object | — | 선택 |
| 4 | 저장 디렉터리 경로 | `"EXPORT_PATH"` | String | — | **필수** |
| 5 | 출력 파일 기본 이름 | `"OUTPUT_NAME"` | String | — | **필수** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "graphic",
    "ELEMS": {
      "KEYS": [1073]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\graphic",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX (Civil NX는 /civil)
HEADERS = {"MAPI-Key": "<발급된 키>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 1073번 헌치보 설계 결과를 Graphic(JPG) 리포트로 출력
res = rc_post("HCD-REPORT", {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "graphic",
    "ELEMS": {"KEYS": [1073]},
})
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...", "MESSAGE": ""}
```


---

## 54. `DESIGN/RC/KDS-41-20-2022/BC-ANAL` — RC 보 검토 수행

> **기능:** 기존 배근(rebar)이 배정된 RC 보 부재에 대해 **코드 검토(Checking)** 계산을 수행합니다. 전체(`ALL`)·요소별(`ELEMS`)·단면별(`SECTIONS`) 대상 선택을 지원하며, 결과는 이후 `BC-TABLE`/`BC-REPORT`로 조회합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BC-ANAL
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
          "description": "Select target type. ELEMS: by element numbers, SECTIONS: by section numbers, ALL: all elements.",
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
          "description": "Element No. Input",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              },
              "description": "Specify Each ID"
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
          "items": {
            "type": "integer"
          },
          "description": "Section No. Input"
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
| 2 | 수행 대상 타입 (`"ALL"`=전체, `"ELEMS"`=요소별, `"SECTIONS"`=단면별) | `"PERFORM_TYPE"` | String (oneOf) | `"ALL"` | 선택 |
| 3 | 요소 입력 (ELEMS / SECTIONS 중 하나) | `"ELEMS"` | Object | — | 조건부 |
| 3.1 | 개별 ID | `"KEYS"` | Array[Integer] | — | 선택 |
| 3.2 | ID 범위 (예 `"1to160"`) | `"TO"` | String | — | 선택 |
| 3.3 | 구조 그룹 이름 | `"STRUCTURE_GROUP_NAME"` | String | — | 선택 |
| 4 | 단면 번호 (ELEMS / SECTIONS 중 하나) | `"SECTIONS"` | Array[Integer] | — | 조건부 |

> `Argument`는 `"ELEMS"` 또는 `"SECTIONS"` 중 **정확히 하나**만 포함해야 하며(oneOf), `ELEMS` 내부에서도 `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나만 사용합니다. `PERFORM_TYPE="ALL"`이면 대상 지정 없이 전체 보를 검토합니다.

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

BASE_URL = "https://moa-engineers.midasit.com:443/civil"   # Civil NX (Gen NX는 /gen)
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BC-ANAL"

# 전체 RC 보에 대해 코드 검토 수행
payload = {"Argument": {"PERFORM_TYPE": "ALL"}}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())   # {"message": "success"}
```

---

## 55. `DESIGN/RC/KDS-41-20-2022/BC-TABLE` — RC 보 검토 테이블

> **기능:** RC 보 검토 결과를 표(HEAD/DATA) 형식으로 반환합니다. 강도 검토(휨 정/부모멘트·전단)와 배근 상세(주근·스터럽 최소/최대 조건)가 함께 출력됩니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BC-TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 필수 키는 `"TABLE_TYPE"`이며, `"ELEMS"` 또는 `"SECTIONS"` 중 하나(oneOf)를 대상으로 지정합니다. 주요 속성은 다음과 같습니다.

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["TABLE_TYPE"],
      "additionalProperties": false,
      "oneOf": [{"required": ["ELEMS"]}, {"required": ["SECTIONS"]}],
      "properties": {
        "PRI_SORT":    {"type": "integer", "default": 1, "oneOf": [{"title": "Section", "const": 0}, {"title": "Member", "const": 1}]},
        "ELEMS":       {"type": "object", "properties": {"KEYS": {"type": "array", "items": {"type": "integer"}}, "TO": {"type": "string"}, "STRUCTURE_GROUP_NAME": {"type": "string"}}},
        "SECTIONS":    {"type": "array", "items": {"type": "integer"}},
        "RESULT":      {"type": "integer", "default": 0, "oneOf": [{"title": "All", "const": 0}, {"title": "OK", "const": 1}, {"title": "NG", "const": 2}]},
        "TABLE_NAME":  {"type": "string", "default": "RC Beam Checking Result"},
        "TABLE_TYPE":  {"type": "string", "enum": ["MEMB", "PROP"]},
        "EXPORT_PATH": {"type": "string"},
        "UNIT":        {"type": "object", "properties": {"FORCE": {"type": "string"}, "DIST": {"type": "string"}, "HEAT": {"type": "string"}, "TEMP": {"type": "string"}}},
        "STYLES":      {"type": "object", "properties": {"FORMAT": {"type": "string", "enum": ["Default", "Fixed", "Scientific", "General"]}, "PLACE": {"type": "integer", "minimum": 0, "maximum": 15}}},
        "COMPONENTS":  {"type": "array", "items": {"type": "string"}}
      }
    }
  }
}
```

### 파라미터

| No. | 설명 | Key | 타입 | 기본값 | 필수 |
|-----|------|-----|------|--------|------|
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 정렬 기준 (`0`=Section, `1`=Member) | `"PRI_SORT"` | Integer (oneOf) | `1` | 선택 |
| 3 | 결과 필터 (`0`=All, `1`=OK, `2`=NG) | `"RESULT"` | Integer (oneOf) | `0` | 선택 |
| 4 | 응답 테이블 제목 | `"TABLE_NAME"` | String | `"RC Beam Checking Result"` | 선택 |
| 5 | 결과 테이블 타입 (`"MEMB"` 또는 `"PROP"`) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 6 | 대상 요소 (ELEMS / SECTIONS 중 하나) | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 조건부 |
| 7.1 | 개별 ID / ID 범위 / 구조그룹 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 선택 |
| 8 | 결과 저장 경로 | `"EXPORT_PATH"` | String | — | 선택 |
| 9 | 단위 설정 (`FORCE`,`DIST`,`HEAT`,`TEMP`) | `"UNIT"` | Object | System | 선택 |
| 10 | 숫자 형식 (`FORMAT`,`PLACE`) | `"STYLES"` | Object | System | 선택 |
| 11 | 출력 컬럼 목록 | `"COMPONENTS"` | Array[String] | — | 선택 |


**Response HEAD 열 설명** (요청 `COMPONENTS`와 동일 순서로 반환):

| 열(HEAD) | 의미 |
|------|------|
| `MEMB` | Element number |
| `SECT` | Section property number |
| `Span` | Length of beam member |
| `Section` | Symbol for sectional shape (SB: Rectangular, TEE: T-shape) |
| `Bc` | Width of beam member |
| `Hc` | Height (depth) of beam member |
| `bf` | Width of the flange of T-shape section |
| `hf` | Thickness of the flange of T-shape section |
| `fck` | Design compressive strength of concrete (f'c) |
| `fy` | Design yield strength of main rebars |
| `fys` | Design yield strength of shear rebars |
| `POS` | Section design points (I, M, J). M reflects max values at 1/4, 1/2, and 3/4 points. |
| `CHK_STR` | Status of Checking Results (Strength) |
| `Neg_Rebar` | Negative moment strength - Rebar |
| `Neg_As_use` | Negative moment strength - As.use |
| `Neg_Mu` | Negative moment strength - N(-) Mu |
| `Neg_LCB` | Negative moment strength - LCB |
| `Neg_phiMn` | Negative moment strength - N(-) φMn |
| `Rat-N` | Negative moment strength - Ratio (Mu/φMn), red if > 1.0 |
| `Pos_Rebar` | Positive moment strength - Rebar |
| `Pos_As_use` | Positive moment strength - As.use |
| `Pos_Mu` | Positive moment strength - P(+) Mu |
| `Pos_LCB` | Positive moment strength - LCB |
| `Pos_phiMn` | Positive moment strength - P(+) φMn |
| `Rat-P` | Positive moment strength - Ratio (Mu/φMn), red if > 1.0 |
| `Sh_Stirrup` | Shear strength - Stirrup |
| `Sh_Vu` | Shear strength - Vu |
| `Sh_LCB` | Shear strength - LCB |
| `Sh_phiVc` | Shear strength - φVc |
| `Rat-V` | Shear strength - Ratio (Vu/φVc), red if > 1.0 |
| `CHK_RBR` | Status of Checking Results (Rebar Detail) |
| `Top_rho_max` | Main rebar (Top) - ρ.max (%) |
| `Top_rho_use` | Main rebar (Top) - ρ.use (%) |
| `Top_rho_min` | Main rebar (Top) - ρ.min (%) |
| `Top_s_max` | Main rebar (Top) - s.max |
| `Top_s_use` | Main rebar (Top) - s.use |
| `Bot_rho_max` | Main rebar (Bottom) - ρ.max (%) |
| `Bot_rho_use` | Main rebar (Bottom) - ρ.use (%) |
| `Bot_rho_min` | Main rebar (Bottom) - ρ.min (%) |
| `Bot_s_max` | Main rebar (Bottom) - s.max |
| `Bot_s_use` | Main rebar (Bottom) - s.use |
| `St_Av_use` | Stirrup - Av.use |
| `St_Av_min` | Stirrup - Av.min |
| `St_s_max` | Stirrup - s.max |
| `St_s_use` | Stirrup - s.use |


### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PRI_SORT": 1,
    "SECTIONS": [
      7
    ],
    "RESULT": 0,
    "TABLE_NAME": "RC Beam Checking Result",
    "TABLE_TYPE": "MEMB",
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Span",
      "Section",
      "Bc",
      "Hc",
      "bf",
      "hf",
      "fck",
      "fy",
      "fys",
      "POS",
      "CHK_STR",
      "Neg_Rebar",
      "Neg_As_use",
      "Neg_Mu",
      "Neg_LCB",
      "Neg_phiMn",
      "Rat-N",
      "Pos_Rebar",
      "Pos_As_use",
      "Pos_Mu",
      "Pos_LCB",
      "Pos_phiMn",
      "Rat-P",
      "Sh_Stirrup",
      "Sh_Vu",
      "Sh_LCB",
      "Sh_phiVc",
      "Rat-V",
      "CHK_RBR",
      "Top_rho_max",
      "Top_rho_use",
      "Top_rho_min",
      "Top_s_max",
      "Top_s_use",
      "Bot_rho_max",
      "Bot_rho_use",
      "Bot_rho_min",
      "Bot_s_max",
      "Bot_s_use",
      "St_Av_use",
      "St_Av_min",
      "St_s_max",
      "St_s_use"
    ]
  }
}
```

**Response Body** (대표 DATA 2행, 각 행 길이 = HEAD 45열)

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
      "fck",
      "fy",
      "fys",
      "POS",
      "CHK_STR",
      "Neg_Rebar",
      "Neg_As_use",
      "Neg_Mu",
      "Neg_LCB",
      "Neg_phiMn",
      "Rat-N",
      "Pos_Rebar",
      "Pos_As_use",
      "Pos_Mu",
      "Pos_LCB",
      "Pos_phiMn",
      "Rat-P",
      "Sh_Stirrup",
      "Sh_Vu",
      "Sh_LCB",
      "Sh_phiVc",
      "Rat-V",
      "CHK_RBR",
      "Top_rho_max",
      "Top_rho_use",
      "Top_rho_min",
      "Top_s_max",
      "Top_s_use",
      "Bot_rho_max",
      "Bot_rho_use",
      "Bot_rho_min",
      "Bot_s_max",
      "Bot_s_use",
      "St_Av_use",
      "St_Av_min",
      "St_s_max",
      "St_s_use"
    ],
    "DATA": [
      [
        "1086",
        "7",
        "1.0000",
        "N",
        "1.0000",
        "0.5000",
        "0.0000",
        "0.0000",
        "30000.0",
        "600000",
        "400000",
        "I",
        "OK",
        "10-D22",
        "0.0039",
        "769.768",
        "5",
        "775.573",
        "0.99",
        "2-D22",
        "0.0008",
        "0.00000",
        "200",
        "185.633",
        "0.00",
        "2-D10 @160",
        "234.891",
        "5",
        "298.851",
        "0.57",
        "OK",
        "1.384",
        "0.887",
        "0.219",
        "0.1350",
        "0.0970",
        "2.093",
        "0.177",
        "0.000",
        "-",
        "-",
        "0.0000",
        "0.0000",
        "0.2183",
        "0.1600"
      ],
      [
        "1086",
        "7",
        "1.0000",
        "N",
        "1.0000",
        "0.5000",
        "0.0000",
        "0.0000",
        "30000.0",
        "600000",
        "400000",
        "M",
        "OK",
        "10-D22",
        "0.0039",
        "711.692",
        "5",
        "775.573",
        "0.92",
        "2-D22",
        "0.0008",
        "0.00000",
        "200",
        "185.633",
        "0.00",
        "2-D10 @160",
        "229.722",
        "5",
        "298.851",
        "0.55",
        "OK",
        "1.384",
        "0.887",
        "0.219",
        "0.1350",
        "0.0970",
        "2.093",
        "0.177",
        "0.000",
        "-",
        "-",
        "0.0000",
        "0.0000",
        "0.2183",
        "0.1600"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BC-TABLE"

# 단면번호 7 보의 검토 결과 테이블 조회 (부재 기준 정렬)
payload = {
    "Argument": {
        "PRI_SORT": 1,
        "SECTIONS": [7],
        "RESULT": 0,                       # All (OK/NG 모두)
        "TABLE_NAME": "RC Beam Checking Result",
        "TABLE_TYPE": "MEMB",
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
table = res.json()["RC Beam Checking Result"]
print("HEAD 열 수:", len(table["HEAD"]))
for row in table["DATA"]:
    # POS(단부 I/M/J), 강도판정(CHK_STR), 전단비(Rat-V) 출력
    print(row[11], row[12], "Rat-V=", row[29])
```

---

## 56. `DESIGN/RC/KDS-41-20-2022/BC-REPORT` — RC 보 검토 리포트

> **기능:** RC 보 검토 결과를 파일(그래픽 JPG / Detail DOC / Summary TXT)로 내보냅니다. 여러 요소를 지정하면 인덱스·요소번호가 접두된 파일명으로 각각 저장됩니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BC-REPORT
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
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
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
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "DETAIL_POSITIONS": {
          "type": "object",
          "properties": {
            "END_I": {
              "type": "boolean",
              "default": true
            },
            "MID": {
              "type": "boolean",
              "default": false
            },
            "END_J": {
              "type": "boolean",
              "default": false
            }
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "OUTPUT_NAME": {
          "type": "string"
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
| 2 | 리포트 대상 타입 (`"MEMB"` / `"PROP"`) | `"REPORT_TYPE"` | String (enum) | — | **필수** |
| 3 | 요소(MEMB) 출력 모드 (`"Graphic"`/`"Detail"`/`"Summary"`) | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 조건부 |
| 4 | 단면(PROP) 출력 모드 (`"Graphic"`/`"Summary"`) | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 조건부 |
| 5 | 대상 요소 (ELEMS / SECTIONS 중 하나) | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 조건부 |
| 5.1 | 개별 ID / ID 범위 / 구조그룹 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 선택 |
| 6 | Detail 출력 위치 (`END_I`,`MID`,`END_J`) | `"DETAIL_POSITIONS"` | Object | — | 선택 |
| 7 | 리포트 저장 디렉터리 경로 | `"EXPORT_PATH"` | String | — | **필수** |
| 8 | 출력 파일 기본 이름 | `"OUTPUT_NAME"` | String | — | **필수** |

> `REPORT_TYPE="MEMB"`이면 `CURRENT_MODE_MEMB`, `"PROP"`이면 `CURRENT_MODE_PROP`(Graphic/Summary만)을 사용합니다. `DETAIL_POSITIONS`는 `CURRENT_MODE_MEMB="Detail"`일 때만 유효합니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "detail.txt",
    "ELEMS": {
      "KEYS": [
        1086
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

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\detail.txt",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BC-REPORT"

# 요소 1086 보의 Detail 리포트(J 단부)를 TXT로 저장
payload = {
    "Argument": {
        "REPORT_TYPE": "MEMB",
        "CURRENT_MODE_MEMB": "Detail",
        "EXPORT_PATH": "C:\\MIDAS\\Result\\",
        "OUTPUT_NAME": "detail.txt",
        "ELEMS": {"KEYS": [1086]},
        "DETAIL_POSITIONS": {"END_I": False, "MID": False, "END_J": True},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...detail.txt", "MESSAGE": ""}
```

---
## 57. `DESIGN/RC/KDS-41-20-2022/CC-ANAL` — RC 기둥 검토 수행

> **기능:** 배근이 배정된 RC 기둥 부재에 대해 **P-M 상관·전단 코드 검토**를 수행합니다. 전체/요소별/단면별 대상 선택을 지원합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CC-ANAL
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
          "description": "Select target type. ELEMS: by element numbers, SECTIONS: by section numbers, ALL: all elements.",
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
          "description": "Element No. Input",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              },
              "description": "Specify Each ID"
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
          "items": {
            "type": "integer"
          },
          "description": "Section No. Input"
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
| 2 | 수행 대상 타입 (`"ALL"`=전체, `"ELEMS"`=요소별, `"SECTIONS"`=단면별) | `"PERFORM_TYPE"` | String (oneOf) | `"ALL"` | 선택 |
| 3 | 요소 입력 (ELEMS / SECTIONS 중 하나) | `"ELEMS"` | Object | — | 조건부 |
| 3.1 | 개별 ID | `"KEYS"` | Array[Integer] | — | 선택 |
| 3.2 | ID 범위 (예 `"1to160"`) | `"TO"` | String | — | 선택 |
| 3.3 | 구조 그룹 이름 | `"STRUCTURE_GROUP_NAME"` | String | — | 선택 |
| 4 | 단면 번호 (ELEMS / SECTIONS 중 하나) | `"SECTIONS"` | Array[Integer] | — | 조건부 |

> `ELEMS`/`SECTIONS`는 oneOf로 하나만 사용합니다. 예제는 `PERFORM_TYPE="ALL"`과 함께 요소 1059를 지정한 형태입니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL",
    "ELEMS": {
      "KEYS": [
        1059
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

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/CC-ANAL"

# 특정 기둥 요소(1059) 검토 수행
payload = {"Argument": {"PERFORM_TYPE": "ALL", "ELEMS": {"KEYS": [1059]}}}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"message": "success"}
```

---

## 58. `DESIGN/RC/KDS-41-20-2022/CC-TABLE` — RC 기둥 검토 테이블

> **기능:** RC 기둥 검토 결과를 표로 반환합니다. P-M 상관(축력/모멘트 강도비), 단·중앙부 전단, 주근·후프(Hoop) 배근 상세를 포함합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CC-TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 필수 키는 `"TABLE_TYPE"`이며, `"ELEMS"`/`"SECTIONS"` 중 하나(oneOf)를 대상으로 지정합니다. 주요 속성은 다음과 같습니다.

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
        "PRI_SORT": {
          "type": "integer",
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
          "default": "RC Column Checking Result"
        },
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          }
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          }
        },
        "COMPONENTS": {
          "type": "array",
          "items": {
            "type": "string"
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
| 2 | 정렬 기준 (`0`=SECT, `1`=MEMB) | `"PRI_SORT"` | Integer (oneOf) | `1` | 선택 |
| 3 | 결과 필터 (`0`=All, `1`=OK, `2`=NG) | `"RESULT"` | Integer (oneOf) | `0` | 선택 |
| 4 | 응답 테이블 제목 | `"TABLE_NAME"` | String | `"RC Column Checking Result"` | 선택 |
| 5 | 결과 테이블 타입 (`"MEMB"` 또는 `"PROP"`) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 6 | 대상 요소 (ELEMS / SECTIONS 중 하나) | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 조건부 |
| 6.1 | 개별 ID / ID 범위 / 구조그룹 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 선택 |
| 7 | 결과 저장 경로 | `"EXPORT_PATH"` | String | — | 선택 |
| 8 | 단위 설정 (`FORCE`,`DIST`,`HEAT`,`TEMP`) | `"UNIT"` | Object | System | 선택 |
| 9 | 숫자 형식 (`FORMAT`,`PLACE`) | `"STYLES"` | Object | System | 선택 |
| 10 | 출력 컬럼 목록 | `"COMPONENTS"` | Array[String] | — | 선택 |


**Response HEAD 열 설명** (요청 `COMPONENTS`와 동일 순서로 반환):

| 열(HEAD) | 의미 |
|------|------|
| `MEMB` | Element Number |
| `SECT` | Section Property Number |
| `Section` | Sectional Shape |
| `Bc` | Width of Column Member |
| `Hc` | Depth of Column Member |
| `fck` | Design Compressive Strength of Concrete (f'c) |
| `Height` | Height of Column Member |
| `fy` | Design Yield Strength of Main Rebars |
| `fys` | Design Yield Strength of Shear Rebars |
| `CHK_STR` | Status of Checking Results (Strength) |
| `LCB_PM` | Load Combination for Axial-Moment Check |
| `V_Rebar` | Vertical Rebar |
| `phiPn_max` | Maximum Axial Design Strength |
| `Pu` | Factored Axial Force |
| `phiPn` | Design Axial Strength |
| `Rat_P` | Axial Strength Ratio (Pu/φPn) |
| `Mc` | Factored Moment |
| `phiMn` | Design Moment Strength |
| `Rat_M` | Moment Strength Ratio (Mc/φMn) |
| `Rat_My` | Y-axis Moment Strength Ratio |
| `Rat_Mz` | Z-axis Moment Strength Ratio |
| `Mc_Pu` | Eccentricity |
| `Mcz_Mcy` | Moment Rotation (Mcz/Mcy) |
| `MFy` | Moment Factor (Y) |
| `MFz` | Moment Factor (Z) |
| `Mcy` | Factored Moment (Y) |
| `Mcz` | Factored Moment (Z) |
| `LCB_Vu_end` | Load Combination for Shear at End |
| `LCB_Vu_mid` | Load Combination for Shear at Mid |
| `Vu_end` | Factored Shear Force at End |
| `Vu_mid` | Factored Shear Force at Mid |
| `Rat_V_end` | Shear Strength Ratio at End |
| `Rat_V_mid` | Shear Strength Ratio at Mid |
| `CHK_RBR` | Status of Checking Results (Rebar Detail) |
| `H_Rebar_end` | Shear Rebar at End |
| `H_Rebar_mid` | Shear Rebar at Mid |
| `rho_max` | Main Rebar (%) - ρ.max |
| `rho_use` | Main Rebar (%) - ρ.use |
| `rho_min` | Main Rebar (%) - ρ.min |
| `Avy_use_end` | Hoop (End) - Avy.use |
| `Avy_min_end` | Hoop (End) - Avy.min |
| `Avz_use_end` | Hoop (End) - Avz.use |
| `Avz_min_end` | Hoop (End) - Avz.min |
| `s_max_end` | Hoop (End) - s.max |
| `s_use_end` | Hoop (End) - s.use |
| `Avy_use_mid` | Hoop (Mid) - Avy.use |
| `Avy_min_mid` | Hoop (Mid) - Avy.min |
| `Avz_use_mid` | Hoop (Mid) - Avz.use |
| `Avz_min_mid` | Hoop (Mid) - Avz.min |
| `s_max_mid` | Hoop (Mid) - s.max |
| `s_use_mid` | Hoop (Mid) - s.use |


### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_NAME": "RC Column Checking Result",
    "TABLE_TYPE": "MEMB",
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "fck",
      "Height",
      "fy",
      "fys",
      "CHK_STR",
      "LCB_PM",
      "V_Rebar",
      "phiPn_max",
      "Pu",
      "phiPn",
      "Rat_P",
      "Mc",
      "phiMn",
      "Rat_M",
      "Rat_My",
      "Rat_Mz",
      "Mc_Pu",
      "Mcz_Mcy",
      "MFy",
      "MFz",
      "Mcy",
      "Mcz",
      "LCB_Vu_end",
      "LCB_Vu_mid",
      "Vu_end",
      "Vu_mid",
      "Rat_V_end",
      "Rat_V_mid",
      "CHK_RBR",
      "H_Rebar_end",
      "H_Rebar_mid",
      "rho_max",
      "rho_use",
      "rho_min",
      "Avy_use_end",
      "Avy_min_end",
      "Avz_use_end",
      "Avz_min_end",
      "s_max_end",
      "s_use_end",
      "Avy_use_mid",
      "Avy_min_mid",
      "Avz_use_mid",
      "Avz_min_mid",
      "s_max_mid",
      "s_use_mid"
    ],
    "ELEMS": {
      "KEYS": [
        1058
      ]
    }
  }
}
```

**Response Body** (대표 DATA 1행, 각 행 길이 = HEAD 51열)

```json
{
  "RC Column Checking Result": {
    "FORCE": "KGF",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "fck",
      "Height",
      "fy",
      "fys",
      "CHK_STR",
      "LCB_PM",
      "V_Rebar",
      "phiPn_max",
      "Pu",
      "phiPn",
      "Rat_P",
      "Mc",
      "phiMn",
      "Rat_M",
      "Rat_My",
      "Rat_Mz",
      "Mc_Pu",
      "Mcz_Mcy",
      "MFy",
      "MFz",
      "Mcy",
      "Mcz",
      "LCB_Vu_end",
      "LCB_Vu_mid",
      "Vu_end",
      "Vu_mid",
      "Rat_V_end",
      "Rat_V_mid",
      "CHK_RBR",
      "H_Rebar_end",
      "H_Rebar_mid",
      "rho_max",
      "rho_use",
      "rho_min",
      "Avy_use_end",
      "Avy_min_end",
      "Avz_use_end",
      "Avz_min_end",
      "s_max_end",
      "s_use_end",
      "Avy_use_mid",
      "Avy_min_mid",
      "Avz_use_mid",
      "Avz_min_mid",
      "s_max_mid",
      "s_use_mid"
    ],
    "DATA": [
      [
        "1058",
        "100",
        "D300",
        "0.0000",
        "0.3000",
        "3059149",
        "4.0000",
        "6.1E+07",
        "4.1E+07",
        "OK",
        "5",
        "4-2-D22",
        "142746",
        "950.018",
        "116623",
        "0.008",
        "32.2447",
        "3958.30",
        "0.008",
        "0.008",
        "0.008",
        "0.03394",
        "45.000000",
        "1.000",
        "1.000",
        "22.8004",
        "22.8004",
        "47",
        "47",
        "0.00000",
        "0.00000",
        "0.000",
        "0.000",
        "OK",
        "2-D10 @150",
        "2-D10 @150",
        "3.000",
        "2.191",
        "1.000",
        "0.0001",
        "-",
        "0.0001",
        "-",
        "0.2000",
        "0.1500",
        "0.0001",
        "-",
        "0.0001",
        "-",
        "0.2000",
        "0.1500"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/CC-TABLE"

# 요소 1058 기둥의 검토 결과 조회
payload = {
    "Argument": {
        "PRI_SORT": 1,
        "RESULT": 0,
        "TABLE_NAME": "RC Column Checking Result",
        "TABLE_TYPE": "MEMB",
        "ELEMS": {"KEYS": [1058]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
table = res.json()["RC Column Checking Result"]
head = table["HEAD"]
for row in table["DATA"]:
    rec = dict(zip(head, row))
    print(rec["MEMB"], "P비=", rec["Rat_P"], "M비=", rec["Rat_M"], rec["CHK_STR"])
```

---

## 59. `DESIGN/RC/KDS-41-20-2022/CC-REPORT` — RC 기둥 검토 리포트

> **기능:** RC 기둥 검토 결과를 파일(Graphic/Detail/Summary)로 내보냅니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CC-REPORT
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
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
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
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "DETAIL_POSITIONS": {
          "type": "object",
          "properties": {
            "END_I": {
              "type": "boolean",
              "default": true
            },
            "MID": {
              "type": "boolean",
              "default": false
            },
            "END_J": {
              "type": "boolean",
              "default": false
            }
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "OUTPUT_NAME": {
          "type": "string"
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
| 2 | 리포트 대상 타입 (`"MEMB"` / `"PROP"`) | `"REPORT_TYPE"` | String (enum) | — | **필수** |
| 3 | 요소(MEMB) 출력 모드 (`"Graphic"`/`"Detail"`/`"Summary"`) | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 조건부 |
| 4 | 단면(PROP) 출력 모드 (`"Graphic"`/`"Summary"`) | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 조건부 |
| 5 | 대상 요소 (ELEMS / SECTIONS 중 하나) | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 조건부 |
| 5.1 | 개별 ID / ID 범위 / 구조그룹 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 선택 |
| 6 | Detail 출력 위치 (`END_I`,`MID`,`END_J`) | `"DETAIL_POSITIONS"` | Object | — | 선택 |
| 7 | 리포트 저장 디렉터리 경로 | `"EXPORT_PATH"` | String | — | **필수** |
| 8 | 출력 파일 기본 이름 | `"OUTPUT_NAME"` | String | — | **필수** |

> `REPORT_TYPE="MEMB"`이면 `CURRENT_MODE_MEMB`, `"PROP"`이면 `CURRENT_MODE_PROP`(Graphic/Summary만)을 사용합니다. `DETAIL_POSITIONS`는 `CURRENT_MODE_MEMB="Detail"`일 때만 유효합니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "columnresult",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "TO": "1058to1059"
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\columnresult",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/CC-REPORT"

# 요소 1058~1059 기둥의 Graphic 리포트를 저장
payload = {
    "Argument": {
        "REPORT_TYPE": "MEMB",
        "EXPORT_PATH": "C:\\MIDAS\\Result\\",
        "OUTPUT_NAME": "columnresult",
        "CURRENT_MODE_MEMB": "Graphic",
        "ELEMS": {"TO": "1058to1059"},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...", "MESSAGE": ""}
```

---

## 60. `DESIGN/RC/KDS-41-20-2022/BRC-ANAL` — RC 가새 검토 수행

> **기능:** 배근이 배정된 RC 가새(Brace) 부재에 대해 P-M 상관·전단 코드 검토를 수행합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRC-ANAL
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
          "description": "Select target type. ELEMS: by element numbers, SECTIONS: by section numbers, ALL: all elements.",
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
          "description": "Element No. Input",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              },
              "description": "Specify Each ID"
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
          "items": {
            "type": "integer"
          },
          "description": "Section No. Input"
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
| 2 | 수행 대상 타입 (`"ALL"`=전체, `"ELEMS"`=요소별, `"SECTIONS"`=단면별) | `"PERFORM_TYPE"` | String (oneOf) | `"ALL"` | 선택 |
| 3 | 요소 입력 (ELEMS / SECTIONS 중 하나) | `"ELEMS"` | Object | — | 조건부 |
| 3.1 | 개별 ID | `"KEYS"` | Array[Integer] | — | 선택 |
| 3.2 | ID 범위 (예 `"1to160"`) | `"TO"` | String | — | 선택 |
| 3.3 | 구조 그룹 이름 | `"STRUCTURE_GROUP_NAME"` | String | — | 선택 |
| 4 | 단면 번호 (ELEMS / SECTIONS 중 하나) | `"SECTIONS"` | Array[Integer] | — | 조건부 |

> 예제는 요소 883, 902 두 가새를 대상으로 지정한 형태입니다. `ELEMS`/`SECTIONS`는 oneOf로 하나만 사용합니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL",
    "ELEMS": {
      "KEYS": [
        883,
        902
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

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BRC-ANAL"

# 가새 요소 883, 902 검토 수행
payload = {"Argument": {"PERFORM_TYPE": "ALL", "ELEMS": {"KEYS": [883, 902]}}}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"message": "success"}
```

---

## 61. `DESIGN/RC/KDS-41-20-2022/BRC-TABLE` — RC 가새 검토 테이블

> **기능:** RC 가새 검토 결과를 표로 반환합니다. 구성은 기둥 검토와 유사하나 단부 구분이 없는 단일 위치 값(축력/모멘트 강도비, 전단, 후프 배근)을 제공합니다. 응답 최상위 키는 `TABLE_NAME`(미지정 시 예제에서는 `"Result Table"`)입니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRC-TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 필수 키는 `"TABLE_TYPE"`이며, `"ELEMS"`/`"SECTIONS"` 중 하나(oneOf)를 대상으로 지정합니다. 주요 속성은 다음과 같습니다.

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
        "PRI_SORT": {
          "type": "integer",
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
          "default": "RC Brace Checking Result"
        },
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          }
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          }
        },
        "COMPONENTS": {
          "type": "array",
          "items": {
            "type": "string"
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
| 2 | 정렬 기준 (`0`=SECT, `1`=MEMB) | `"PRI_SORT"` | Integer (oneOf) | `1` | 선택 |
| 3 | 결과 필터 (`0`=All, `1`=OK, `2`=NG) | `"RESULT"` | Integer (oneOf) | `0` | 선택 |
| 4 | 응답 테이블 제목 | `"TABLE_NAME"` | String | `"RC Brace Checking Result"` | 선택 |
| 5 | 결과 테이블 타입 (`"MEMB"` 또는 `"PROP"`) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 6 | 대상 요소 (ELEMS / SECTIONS 중 하나) | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 조건부 |
| 6.1 | 개별 ID / ID 범위 / 구조그룹 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 선택 |
| 7 | 결과 저장 경로 | `"EXPORT_PATH"` | String | — | 선택 |
| 8 | 단위 설정 (`FORCE`,`DIST`,`HEAT`,`TEMP`) | `"UNIT"` | Object | System | 선택 |
| 9 | 숫자 형식 (`FORMAT`,`PLACE`) | `"STYLES"` | Object | System | 선택 |
| 10 | 출력 컬럼 목록 | `"COMPONENTS"` | Array[String] | — | 선택 |


**Response HEAD 열 설명** (요청 `COMPONENTS`와 동일 순서로 반환):

| 열(HEAD) | 의미 |
|------|------|
| `MEMB` | Element Number |
| `SECT` | Section Property Number |
| `Section` | Sectional Shape |
| `Bc` | Width of Brace Member |
| `Hc` | Depth of Brace Member |
| `fck` | Design Compressive Strength of Concrete (f'c) |
| `Height` | Height of Brace Member |
| `fy` | Design Yield Strength of Main Rebars |
| `fys` | Design Yield Strength of Shear Rebars |
| `CHK_STR` | Status of Checking Results (Strength) |
| `LCB` | Load Combination for P-M Interaction / Check |
| `phiPn.max` | Maximum Design Axial Strength |
| `Pu` | Factored Axial Force |
| `phiPn` | Design Axial Strength |
| `Rat-P` | Axial Strength Ratio (Pu/phiPn) |
| `Mc` | Factored Moment |
| `phiMn` | Design Moment Strength |
| `Rat-M` | Moment Strength Ratio (Mc/phiMn) |
| `Rat-My` | Y-axis Moment Strength Ratio |
| `Rat-Mz` | Z-axis Moment Strength Ratio |
| `Mc/Pu` | Eccentricity |
| `Mcz/Mcy` | Moment Rotation (Mcz/Mcy) |
| `V-Rebar` | Vertical Rebar |
| `MF.y` | Moment Factor (Y) |
| `MF.z` | Moment Factor (Z) |
| `Mcy` | Factored Moment (Y) |
| `Mcz` | Factored Moment (Z) |
| `H-Rebar` | Hoop / Shear Rebar |
| `Vu` | Factored Shear Force |
| `Rat-V` | Shear Strength Ratio (Vu/phiVn) |
| `CHK_RBR` | Status of Checking Results (Rebar Detail) |
| `rho.max` | Main Rebar (%) - rho.max |
| `rho.use` | Main Rebar (%) - rho.use |
| `rho.min` | Main Rebar (%) - rho.min |
| `Avy.use` | Hoop - Avy.use |
| `Avy.min` | Hoop - Avy.min |
| `Avz.use` | Hoop - Avz.use |
| `Avz.min` | Hoop - Avz.min |
| `s.max` | Hoop - s.max |
| `s.use` | Hoop - s.use |


### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_TYPE": "MEMB",
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "fck",
      "Height",
      "fy",
      "fys",
      "CHK_STR",
      "LCB",
      "phiPn.max",
      "Pu",
      "phiPn",
      "Rat-P",
      "Mc",
      "phiMn",
      "Rat-M",
      "Rat-My",
      "Rat-Mz",
      "Mc/Pu",
      "Mcz/Mcy",
      "V-Rebar",
      "MF.y",
      "MF.z",
      "Mcy",
      "Mcz",
      "H-Rebar",
      "Vu",
      "Rat-V",
      "CHK_RBR",
      "rho.max",
      "rho.use",
      "rho.min",
      "Avy.use",
      "Avy.min",
      "Avz.use",
      "Avz.min",
      "s.max",
      "s.use"
    ],
    "ELEMS": {
      "KEYS": [
        883
      ]
    }
  }
}
```

**Response Body** (대표 DATA 1행, 각 행 길이 = HEAD 40열)

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
      "fck",
      "Height",
      "fy",
      "fys",
      "CHK_STR",
      "LCB",
      "phiPn.max",
      "Pu",
      "phiPn",
      "Rat-P",
      "Mc",
      "phiMn",
      "Rat-M",
      "Rat-My",
      "Rat-Mz",
      "Mc/Pu",
      "Mcz/Mcy",
      "V-Rebar",
      "MF.y",
      "MF.z",
      "Mcy",
      "Mcz",
      "H-Rebar",
      "Vu",
      "Rat-V",
      "CHK_RBR",
      "rho.max",
      "rho.use",
      "rho.min",
      "Avy.use",
      "Avy.min",
      "Avz.use",
      "Avz.min",
      "s.max",
      "s.use"
    ],
    "DATA": [
      [
        "883",
        "2",
        "300x600",
        "0.3000",
        "0.6000",
        "30000.0",
        "3.1100",
        "600000",
        "400000",
        "M-",
        "5",
        "2849.37",
        "0.00000",
        "-",
        "0.000",
        "491.277",
        "199.531",
        "2.462",
        "2.462",
        "0.000",
        "-",
        "0.000000",
        "4-2-D22",
        "1.000",
        "1.000",
        "491.277",
        "0.00000",
        "2-D22 @200",
        "229.714",
        "0.313",
        "M",
        "3.000",
        "0.860",
        "1.000",
        "0.0008",
        "-",
        "0.0008",
        "0.0001",
        "0.2000",
        "0.2000"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BRC-TABLE"

# 요소 883 가새의 검토 결과 조회 (TABLE_NAME 미지정 → 응답 키는 "Result Table")
payload = {
    "Argument": {
        "PRI_SORT": 1,
        "RESULT": 0,
        "TABLE_TYPE": "MEMB",
        "ELEMS": {"KEYS": [883]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
body = res.json()
table = body.get("RC Brace Checking Result") or body["Result Table"]
head = table["HEAD"]
for row in table["DATA"]:
    rec = dict(zip(head, row))
    print(rec["MEMB"], rec["CHK_STR"], "Rat-V=", rec["Rat-V"])
```

---

## 62. `DESIGN/RC/KDS-41-20-2022/BRC-REPORT` — RC 가새 검토 리포트

> **기능:** RC 가새 검토 결과를 파일(Graphic/Detail/Summary)로 내보냅니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRC-REPORT
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
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
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
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "DETAIL_POSITIONS": {
          "type": "object",
          "properties": {
            "END_I": {
              "type": "boolean",
              "default": true
            },
            "MID": {
              "type": "boolean",
              "default": false
            },
            "END_J": {
              "type": "boolean",
              "default": false
            }
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "OUTPUT_NAME": {
          "type": "string"
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
| 2 | 리포트 대상 타입 (`"MEMB"` / `"PROP"`) | `"REPORT_TYPE"` | String (enum) | — | **필수** |
| 3 | 요소(MEMB) 출력 모드 (`"Graphic"`/`"Detail"`/`"Summary"`) | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 조건부 |
| 4 | 단면(PROP) 출력 모드 (`"Graphic"`/`"Summary"`) | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 조건부 |
| 5 | 대상 요소 (ELEMS / SECTIONS 중 하나) | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 조건부 |
| 5.1 | 개별 ID / ID 범위 / 구조그룹 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 선택 |
| 6 | Detail 출력 위치 (`END_I`,`MID`,`END_J`) | `"DETAIL_POSITIONS"` | Object | — | 선택 |
| 7 | 리포트 저장 디렉터리 경로 | `"EXPORT_PATH"` | String | — | **필수** |
| 8 | 출력 파일 기본 이름 | `"OUTPUT_NAME"` | String | — | **필수** |

> `REPORT_TYPE="MEMB"`이면 `CURRENT_MODE_MEMB`, `"PROP"`이면 `CURRENT_MODE_PROP`(Graphic/Summary만)을 사용합니다. `DETAIL_POSITIONS`는 `CURRENT_MODE_MEMB="Detail"`일 때만 유효합니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        883
      ]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\Graphic.jpg",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BRC-REPORT"

# 요소 883 가새의 Graphic(JPG) 리포트 저장
payload = {
    "Argument": {
        "REPORT_TYPE": "MEMB",
        "CURRENT_MODE_MEMB": "Graphic",
        "EXPORT_PATH": "C:\\MIDAS\\Result\\",
        "OUTPUT_NAME": "Graphic.jpg",
        "ELEMS": {"KEYS": [883]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...Graphic.jpg", "MESSAGE": ""}
```

---

## 63. `DESIGN/RC/KDS-41-20-2022/WC-ANAL` — RC 벽체 검토 수행

> **기능:** RC 벽체(Shear Wall) 부재에 대해 코드 검토를 수행합니다. 벽체는 요소번호가 아니라 **벽 ID(WALL_IDS)와 층(STORY)** 조합(`SELECTIONS`)으로 대상을 지정하며, 생략 시 전체 벽·전체 층을 검토합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WC-ANAL
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
      "description": "Execute RC Wall design calculation. If SELECTIONS is omitted or empty, all wall IDs and all stories are included.",
      "additionalProperties": false,
      "properties": {
        "SELECTIONS": {
          "type": "array",
          "minItems": 0,
          "items": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "KEYS": {
                    "type": "array",
                    "items": {
                      "type": "integer"
                    }
                  },
                  "TO": {
                    "type": "string"
                  }
                },
                "oneOf": [
                  {
                    "required": [
                      "KEYS"
                    ],
                    "not": {
                      "required": [
                        "TO"
                      ]
                    }
                  },
                  {
                    "required": [
                      "TO"
                    ],
                    "not": {
                      "required": [
                        "KEYS"
                      ]
                    }
                  }
                ]
              },
              "STORY": {
                "type": "array",
                "items": {
                  "type": "string"
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
| 2 | 벽/층 선택 목록 (생략 시 전체) | `"SELECTIONS"` | Array[Object] | — | 선택 |
| 2.1 | 벽 ID 지정 | `"WALL_IDS"` | Object | — | 선택 |
| 2.1.1 | 개별 벽 ID | `"KEYS"` | Array[Integer] | — | 선택 |
| 2.1.2 | 벽 ID 범위 (예 `"1to20"`) | `"TO"` | String | — | 선택 |
| 2.2 | 층 이름 목록 | `"STORY"` | Array[String] | — | 선택 |

> `WALL_IDS`는 `KEYS` 또는 `TO` 중 하나(oneOf)만 사용합니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "SELECTIONS": [
      {
        "WALL_IDS": {
          "KEYS": [
            1,
            2,
            3
          ]
        },
        "STORY": [
          "B1F",
          "1F"
        ]
      },
      {
        "WALL_IDS": {
          "TO": "10to20"
        },
        "STORY": [
          "2F",
          "3F"
        ]
      }
    ]
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

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/WC-ANAL"

# 벽 1~3(B1F,1F)과 벽 10~20(2F,3F) 검토 수행
payload = {
    "Argument": {
        "SELECTIONS": [
            {"WALL_IDS": {"KEYS": [1, 2, 3]}, "STORY": ["B1F", "1F"]},
            {"WALL_IDS": {"TO": "10to20"}, "STORY": ["2F", "3F"]},
        ]
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"message": "success"}
```

---

## 64. `DESIGN/RC/KDS-41-20-2022/WC-TABLE` — RC 벽체 검토 테이블

> **기능:** RC 벽체 검토 결과를 표로 반환합니다. 벽체는 `TABLE_TYPE`으로 출력 단위를 선택하며(`"WID+STORY"`=벽ID+층, `"WID"`=벽ID), 대상은 `SELECTIONS`(WALL_IDS + STORY)로 지정합니다. 응답은 `HEAD`/`DATA`가 아니라 **`COMPONENTS` + `DATA`(각 행이 컬럼명 키를 가진 객체)** 형식입니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WC-TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 필수 키는 `"TABLE_TYPE"`이며, `SELECTIONS`(생략 시 전체 벽·전체 층)로 대상을 지정합니다. 주요 속성은 다음과 같습니다.

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
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "WID+STORY",
            "WID"
          ]
        },
        "SELECTIONS": {
          "type": "array",
          "minItems": 0,
          "items": {
            "type": "object",
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "properties": {
                  "KEYS": {
                    "type": "array",
                    "items": {
                      "type": "integer"
                    }
                  },
                  "TO": {
                    "type": "string"
                  }
                },
                "oneOf": [
                  {
                    "required": [
                      "KEYS"
                    ],
                    "not": {
                      "required": [
                        "TO"
                      ]
                    }
                  },
                  {
                    "required": [
                      "TO"
                    ],
                    "not": {
                      "required": [
                        "KEYS"
                      ]
                    }
                  }
                ]
              },
              "STORY": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          }
        },
        "PRI_SORT": {
          "type": "integer",
          "default": 1,
          "oneOf": [
            {
              "title": "Story",
              "const": 0
            },
            {
              "title": "WID",
              "const": 1
            }
          ]
        },
        "PRI_SORT_WID": {
          "type": "integer",
          "default": 1,
          "oneOf": [
            {
              "title": "WallMark",
              "const": 0
            },
            {
              "title": "WID",
              "const": 1
            }
          ]
        },
        "RESULT": {
          "type": "integer",
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
          "default": "RC Wall Checking Result"
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          }
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          }
        },
        "COMPONENTS": {
          "type": "array",
          "items": {
            "type": "string"
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
| 2 | 출력 단위 (`"WID+STORY"` / `"WID"`) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 3 | 벽/층 선택 목록 (생략 시 전체) | `"SELECTIONS"` | Array[Object] | — | 선택 |
| 3.1 | 벽 ID (`KEYS` 또는 `TO`) | `"WALL_IDS"` | Object | — | 선택 |
| 3.2 | 층 이름 목록 | `"STORY"` | Array[String] | — | 선택 |
| 4 | WID+STORY 정렬 (`0`=Story, `1`=WID) | `"PRI_SORT"` | Integer | `1` | 선택 |
| 5 | WID 정렬 (`0`=WallMark, `1`=WID) | `"PRI_SORT_WID"` | Integer | `1` | 선택 |
| 6 | 결과 필터 (`0`=All, `1`=OK, `2`=NG) | `"RESULT"` | Integer | `0` | 선택 |
| 7 | 응답 테이블 제목 | `"TABLE_NAME"` | String | `"RC Wall Checking Result"` | 선택 |
| 8 | 결과 저장 경로 | `"EXPORT_PATH"` | String | — | 선택 |
| 9 | 단위 설정 | `"UNIT"` | Object | System | 선택 |
| 10 | 숫자 형식 | `"STYLES"` | Object | System | 선택 |
| 11 | 출력 컬럼 목록 | `"COMPONENTS"` | Array[String] | — | 선택 |


**응답 `COMPONENTS` 열 설명** (예제 요청 기준, `DATA`의 각 객체 키):

| 컬럼 | 의미 |
|------|------|
| `WID` | Wall Number |
| `Story` | Story Name |
| `Wall Mark` | Designation for Shear Wall Member |
| `Pu` | Factored Axial Force (Maximum for Wall Mark) |
| `Rat-Py` | Axial Strength Ratio in Y-direction (Maximum for Wall Mark) |
| `Rat-Pz` | Axial Strength Ratio in Z-direction (Maximum for Wall Mark) |
| `Mcy` | Factored Moment in Y-direction (Maximum for Wall Mark) |
| `Mcz` | Factored Moment in Z-direction (Maximum for Wall Mark) |
| `Rat-My` | Moment Strength Ratio in Y-direction (Maximum for Wall Mark) |
| `Rat-Mz` | Moment Strength Ratio in Z-direction (Maximum for Wall Mark) |
| `Vu` | Factored Shear Force (Maximum for Wall Mark) |
| `phiVn` | Design Shear Strength |
| `Rat-V` | Shear Strength Ratio (Maximum for Wall Mark) |
| `CHK_STR` | Status of Checking Results (Strength) |
| `CHK_RBR` | Status of Checking Results (Rebar Detail) |


### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "WID+STORY",
    "SELECTIONS": [
      {
        "WALL_IDS": {
          "KEYS": [
            1,
            3
          ]
        },
        "STORY": [
          "3F"
        ]
      },
      {
        "WALL_IDS": {
          "TO": "10to12"
        },
        "STORY": [
          "3F"
        ]
      }
    ],
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_NAME": "RC Wall Check Result",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "WID",
      "Story",
      "Wall Mark",
      "Pu",
      "Rat-Py",
      "Rat-Pz",
      "Mcy",
      "Mcz",
      "Rat-My",
      "Rat-Mz",
      "Vu",
      "phiVn",
      "Rat-V",
      "CHK_STR",
      "CHK_RBR"
    ]
  }
}
```

**Response Body** (대표 DATA 2개 객체, 각 객체 키 수 = COMPONENTS 15개)

```json
{
  "TABLE_NAME": "RC Wall Check Result",
  "TABLE_TYPE": "WID+STORY",
  "UNIT": {
    "FORCE": "kN",
    "DIST": "m"
  },
  "STYLES": {
    "FORMAT": "Fixed",
    "PLACE": 3
  },
  "COMPONENTS": [
    "WID",
    "Story",
    "Wall Mark",
    "Pu",
    "Rat-Py",
    "Rat-Pz",
    "Mcy",
    "Mcz",
    "Rat-My",
    "Rat-Mz",
    "Vu",
    "phiVn",
    "Rat-V",
    "CHK_STR",
    "CHK_RBR"
  ],
  "DATA": [
    {
      "WID": 1,
      "Story": "3F",
      "Wall Mark": "W3F-01",
      "Pu": 1280.45,
      "Rat-Py": 0.382,
      "Rat-Pz": 0.417,
      "Mcy": 245.72,
      "Mcz": 318.64,
      "Rat-My": 0.536,
      "Rat-Mz": 0.624,
      "Vu": 186.33,
      "phiVn": 406.834,
      "Rat-V": 0.458,
      "CHK_STR": "OK",
      "CHK_RBR": "OK"
    },
    {
      "WID": 3,
      "Story": "3F",
      "Wall Mark": "W3F-03",
      "Pu": 1545.82,
      "Rat-Py": 0.461,
      "Rat-Pz": 0.489,
      "Mcy": 312.56,
      "Mcz": 405.21,
      "Rat-My": 0.642,
      "Rat-Mz": 0.711,
      "Vu": 224.78,
      "phiVn": 406.474,
      "Rat-V": 0.553,
      "CHK_STR": "OK",
      "CHK_RBR": "OK"
    }
  ]
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/WC-TABLE"

# 3F의 벽 1,3 및 벽 10~12 검토 결과를 벽ID+층 단위로 조회
payload = {
    "Argument": {
        "TABLE_TYPE": "WID+STORY",
        "SELECTIONS": [
            {"WALL_IDS": {"KEYS": [1, 3]}, "STORY": ["3F"]},
            {"WALL_IDS": {"TO": "10to12"}, "STORY": ["3F"]},
        ],
        "PRI_SORT": 1,
        "RESULT": 0,
        "TABLE_NAME": "RC Wall Check Result",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
        "COMPONENTS": ["WID", "Story", "Wall Mark", "Rat-My", "Rat-Mz", "Rat-V", "CHK_STR", "CHK_RBR"],
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
body = res.json()
for rec in body["DATA"]:      # DATA는 객체(dict)의 배열
    print(rec["WID"], rec["Story"], rec["Wall Mark"], rec["CHK_STR"])
```

---

## 65. `DESIGN/RC/KDS-41-20-2022/WC-REPORT` — RC 벽체 검토 리포트

> **기능:** RC 벽체 검토 결과를 파일로 내보냅니다. 벽체는 `REPORT_TYPE`으로 출력 단위(`"WID+STORY"`/`"WID"`)를 정하고 각각 `CURRENT_MODE_WID_STORY`/`CURRENT_MODE_WID`로 모드(Graphic·Detail·Summary·PMCurve)를 지정합니다. 대상은 `SELECTIONS`로 지정합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WC-REPORT
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
      "properties": {
        "REPORT_TYPE": {
          "type": "string",
          "enum": [
            "WID+STORY",
            "WID"
          ],
          "default": "WID+STORY"
        },
        "CURRENT_MODE_WID_STORY": {
          "type": "string",
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
            },
            {
              "title": "PM Curve (JPG image)",
              "const": "PMCurve"
            }
          ]
        },
        "CURRENT_MODE_WID": {
          "type": "string",
          "oneOf": [
            {
              "title": "Graphic (JPG image)",
              "const": "Graphic"
            },
            {
              "title": "Summary (TXT text)",
              "const": "Summary"
            },
            {
              "title": "PM Curve (JPG image)",
              "const": "PMCurve"
            }
          ]
        },
        "SELECTIONS": {
          "type": "array",
          "minItems": 0,
          "items": {
            "type": "object",
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "properties": {
                  "KEYS": {
                    "type": "array",
                    "items": {
                      "type": "integer"
                    }
                  },
                  "TO": {
                    "type": "string"
                  }
                },
                "oneOf": [
                  {
                    "required": [
                      "KEYS"
                    ],
                    "not": {
                      "required": [
                        "TO"
                      ]
                    }
                  },
                  {
                    "required": [
                      "TO"
                    ],
                    "not": {
                      "required": [
                        "KEYS"
                      ]
                    }
                  }
                ]
              },
              "STORY": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "OUTPUT_NAME": {
          "type": "string"
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
| 2 | 출력 단위 (`"WID+STORY"` / `"WID"`) | `"REPORT_TYPE"` | String (enum) | `"WID+STORY"` | **필수** |
| 3 | WID+STORY 모드 (`Graphic`/`Detail`/`Summary`/`PMCurve`) | `"CURRENT_MODE_WID_STORY"` | String (oneOf) | — | 조건부 |
| 4 | WID 모드 (`Graphic`/`Summary`/`PMCurve`, Detail 미지원) | `"CURRENT_MODE_WID"` | String (oneOf) | — | 조건부 |
| 5 | 벽/층 선택 목록 (생략 시 전체) | `"SELECTIONS"` | Array[Object] | — | 선택 |
| 5.1 | 벽 ID (`KEYS` 또는 `TO`) | `"WALL_IDS"` | Object | — | 선택 |
| 5.2 | 층 이름 목록 | `"STORY"` | Array[String] | — | 선택 |
| 6 | 리포트 저장 디렉터리 경로 | `"EXPORT_PATH"` | String | — | **필수** |
| 7 | 출력 파일 기본 이름 | `"OUTPUT_NAME"` | String | — | **필수** |


### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "WID+STORY",
    "CURRENT_MODE_WID_STORY": "Detail",
    "SELECTIONS": [
      {
        "WALL_IDS": {
          "KEYS": [
            1,
            3
          ]
        },
        "STORY": [
          "3F"
        ]
      },
      {
        "WALL_IDS": {
          "TO": "10to12"
        },
        "STORY": [
          "3F"
        ]
      }
    ],
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "RC_Wall_Report.jpg"
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\RC_Wall_Report.jpg",
  "MESSAGE": ""
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/WC-REPORT"

# 3F의 벽 1,3 및 벽 10~12에 대한 Detail 리포트 저장 (WID+STORY 단위)
payload = {
    "Argument": {
        "REPORT_TYPE": "WID+STORY",
        "CURRENT_MODE_WID_STORY": "Detail",
        "SELECTIONS": [
            {"WALL_IDS": {"KEYS": [1, 3]}, "STORY": ["3F"]},
            {"WALL_IDS": {"TO": "10to12"}, "STORY": ["3F"]},
        ],
        "EXPORT_PATH": "C:\\MIDAS\\Report\\",
        "OUTPUT_NAME": "RC_Wall_Report.jpg",
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...", "MESSAGE": ""}
```

---
## 66. `DESIGN/RC/KDS-41-20-2022/CDESIGN` — RC 콘크리트 종합 설계 결과

> **기능:** RC 콘크리트 설계(보·기둥·가새·벽체 통합) 결과를 화면에 표시하고 **이미지 파일로 캡처**합니다. 표시 하중조합, 강도비 성분(축력/전단/휨/조합), 배근 표시, 부재 종류 필터, 값/범례 등 그래픽 옵션을 세밀하게 설정합니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CDESIGN
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
        "FIGURE_NAME",
        "RESULT_GRAPHIC"
      ],
      "additionalProperties": false,
      "properties": {
        "EXPORT_PATH": {
          "type": "string",
          "description": "Image file save path and file name"
        },
        "FIGURE_NAME": {
          "type": "string",
          "description": "Smart report image name"
        },
        "WIDTH": {
          "type": "integer",
          "default": 1000,
          "minimum": 100,
          "maximum": 10000
        },
        "HEIGHT": {
          "type": "integer",
          "default": 1000,
          "minimum": 100,
          "maximum": 10000
        },
        "STAGE_NAME": {
          "type": "string",
          "description": "Construction stage name"
        },
        "SET_HIDDEN": {
          "type": "boolean",
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
          "default": false
        },
        "ZOOM_LEVEL": {
          "type": "number",
          "default": 100,
          "minimum": 25,
          "maximum": 200
        },
        "BGCOLOR_TOP": {
          "type": "object",
          "properties": {
            "R": {
              "type": "integer"
            },
            "G": {
              "type": "integer"
            },
            "B": {
              "type": "integer"
            }
          }
        },
        "BGCOLOR_BOTTOM": {
          "type": "object",
          "properties": {
            "R": {
              "type": "integer"
            },
            "G": {
              "type": "integer"
            },
            "B": {
              "type": "integer"
            }
          }
        },
        "RESULT_GRAPHIC": {
          "type": "object",
          "required": [
            "LOAD_CASE_COMB"
          ],
          "properties": {
            "LOAD_CASE_COMB": {
              "type": "object",
              "required": [
                "TYPE",
                "NAME"
              ],
              "properties": {
                "TYPE": {
                  "type": "string",
                  "oneOf": [
                    {
                      "title": "Concrete Design Load Combination",
                      "const": "CBC"
                    }
                  ]
                },
                "NAME": {
                  "type": "string"
                }
              }
            },
            "COMPONENTS": {
              "type": "string",
              "default": "Combined",
              "oneOf": [
                {
                  "const": "Axial"
                },
                {
                  "const": "Shear-y"
                },
                {
                  "const": "Shear-z"
                },
                {
                  "const": "Bend-y"
                },
                {
                  "const": "Bend-z"
                },
                {
                  "const": "Combined"
                }
              ]
            },
            "TYPE_OF_DISPLAY": {
              "type": "object",
              "properties": {
                "CONTOUR": {
                  "type": "object"
                },
                "LEGEND": {
                  "type": "object"
                },
                "VALUES": {
                  "type": "object"
                }
              }
            },
            "REINFORCEMENT": {
              "type": "boolean",
              "default": true
            },
            "REINFORCEMENT_TYPE": {
              "type": "string",
              "default": "REBAR",
              "oneOf": [
                {
                  "const": "REBAR"
                },
                {
                  "const": "AREA"
                },
                {
                  "const": "RATIO"
                }
              ]
            },
            "DISPLAY_MEMBERS": {
              "type": "object",
              "properties": {
                "BEAM": {
                  "type": "boolean",
                  "default": true
                },
                "COLUMN": {
                  "type": "boolean",
                  "default": true
                },
                "BRACE": {
                  "type": "boolean",
                  "default": true
                },
                "WALL": {
                  "type": "boolean",
                  "default": true
                }
              }
            },
            "OUTPUT_COMPONENT": {
              "type": "object",
              "properties": {
                "RATIO_AXIAL_STRESS": {
                  "type": "boolean",
                  "default": true
                },
                "MAIN_REBAR": {
                  "type": "boolean",
                  "default": true
                },
                "SHEAR_REINFORCEMENT": {
                  "type": "boolean",
                  "default": true
                }
              }
            },
            "COLUMN_SECTION_SIZE": {
              "type": "object",
              "properties": {
                "SCALE_FACTOR": {
                  "type": "number",
                  "default": 1,
                  "minimum": 0.1,
                  "maximum": 100
                }
              }
            },
            "VALUE_OPTION": {
              "type": "object",
              "properties": {
                "DECIMAL_PLACES": {
                  "type": "integer",
                  "default": 2,
                  "minimum": 0,
                  "maximum": 15
                },
                "EXPONENTIAL": {
                  "type": "boolean",
                  "default": false
                }
              }
            },
            "OUTPUT_SECT_LOCATION": {
              "type": "object",
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
                "OPT_MAX": {
                  "type": "boolean",
                  "default": true
                },
                "OPT_ALL": {
                  "type": "boolean",
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
| 1 | Argument 래퍼 | `"Argument"` | Object | — | **필수** |
| 2 | 이미지 저장 경로+파일명 | `"EXPORT_PATH"` | String | — | **필수** |
| 3 | 스마트 리포트 이미지 이름 | `"FIGURE_NAME"` | String | — | **필수** |
| 4 | 이미지 가로 픽셀 (100–10000) | `"WIDTH"` | Integer | `1000` | 선택 |
| 5 | 이미지 세로 픽셀 (100–10000) | `"HEIGHT"` | Integer | `1000` | 선택 |
| 6 | 시공단계 이름 | `"STAGE_NAME"` | String | — | 선택 |
| 7 | Hidden 표시 옵션 | `"SET_HIDDEN"` | Boolean | `false` | 선택 |
| 8 | 화면 Active/Angle/Display 설정 | `"ACTIVE"`/`"ANGLE"`/`"DISPLAY"` | Object | — | 선택 |
| 9 | 투시(원근) 뷰 | `"PERSPECTIVE"` | Boolean | `false` | 선택 |
| 10 | 줌 레벨 (25=축소, 100=fit, 200=최대) | `"ZOOM_LEVEL"` | Number | `100` | 선택 |
| 11 | 배경색 상/하단 (RGB) | `"BGCOLOR_TOP"`/`"BGCOLOR_BOTTOM"` | Object | — | 선택 |
| 12 | 설계결과 그래픽 설정 | `"RESULT_GRAPHIC"` | Object | — | **필수** |
| 12.1 | 하중케이스/조합 (`TYPE`=`"CBC"`, `NAME`) | `"LOAD_CASE_COMB"` | Object | — | **필수** |
| 12.2 | 강도비 성분 (`Axial`/`Shear-y`/`Shear-z`/`Bend-y`/`Bend-z`/`Combined`) | `"COMPONENTS"` | String (oneOf) | `"Combined"` | 선택 |
| 12.3 | 표시 옵션 (`CONTOUR`/`LEGEND`/`VALUES`) | `"TYPE_OF_DISPLAY"` | Object | — | 선택 |
| 12.4 | 배근 표시 여부 | `"REINFORCEMENT"` | Boolean | `true` | 선택 |
| 12.5 | 배근 표시 타입 (`REBAR`/`AREA`/`RATIO`) | `"REINFORCEMENT_TYPE"` | String (oneOf) | `"REBAR"` | 선택 |
| 12.6 | 표시 부재 종류 (`BEAM`/`COLUMN`/`BRACE`/`WALL`) | `"DISPLAY_MEMBERS"` | Object | — | 선택 |
| 12.7 | 출력 성분 (`RATIO_AXIAL_STRESS`/`MAIN_REBAR`/`SHEAR_REINFORCEMENT`) | `"OUTPUT_COMPONENT"` | Object | — | 선택 |
| 12.8 | 기둥 단면 크기 표시 (`SCALE_FACTOR` 0.1–100) | `"COLUMN_SECTION_SIZE"` | Object | — | 선택 |
| 12.9 | 값 표시 형식 (`DECIMAL_PLACES`/`EXPONENTIAL`) | `"VALUE_OPTION"` | Object | — | 선택 |
| 12.10 | 출력 단면 위치 (`OPT_I`/`OPT_CENTER_MID`/`OPT_J`/`OPT_MAX`/`OPT_ALL`) | `"OUTPUT_SECT_LOCATION"` | Object | — | 선택 |

> `RESULT_GRAPHIC.LOAD_CASE_COMB`은 필수이며, `TYPE`은 콘크리트 설계 하중조합을 뜻하는 `"CBC"`, `NAME`은 조합 이름입니다. 성분(`COMPONENTS`)이 `"Combined"`일 때만 `REINFORCEMENT` 관련 세부 옵션이 유효합니다.

### Request / Response JSON

> 매뉴얼에는 CDESIGN의 Request/Response 예시가 별도로 게시되어 있지 않습니다. 아래는 **스키마 필수 필드 기준으로 구성한 대표 요청**이며, 응답은 이미지 캡처 계열 엔드포인트의 표준 성공 응답 형식입니다.

**POST Request Body**

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\Images\\rc_design.jpg",
    "FIGURE_NAME": "RC Concrete Design Result",
    "WIDTH": 1600,
    "HEIGHT": 1000,
    "SET_HIDDEN": true,
    "PERSPECTIVE": false,
    "ZOOM_LEVEL": 100,
    "RESULT_GRAPHIC": {
      "LOAD_CASE_COMB": {
        "TYPE": "CBC",
        "NAME": "cLCB1"
      },
      "COMPONENTS": "Combined",
      "REINFORCEMENT": true,
      "REINFORCEMENT_TYPE": "REBAR",
      "DISPLAY_MEMBERS": {
        "BEAM": true,
        "COLUMN": true,
        "BRACE": true,
        "WALL": true
      },
      "OUTPUT_COMPONENT": {
        "RATIO_AXIAL_STRESS": true,
        "MAIN_REBAR": true,
        "SHEAR_REINFORCEMENT": true
      },
      "OUTPUT_SECT_LOCATION": {
        "OPT_MAX": true
      }
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

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/CDESIGN"

# 콘크리트 설계 조합 cLCB1의 조합강도비(Combined) 결과를 이미지로 캡처
payload = {
    "Argument": {
        "EXPORT_PATH": "C:\\MIDAS\\Images\\rc_design.jpg",
        "FIGURE_NAME": "RC Concrete Design Result",
        "WIDTH": 1600,
        "HEIGHT": 1000,
        "SET_HIDDEN": True,
        "ZOOM_LEVEL": 100,
        "RESULT_GRAPHIC": {
            "LOAD_CASE_COMB": {"TYPE": "CBC", "NAME": "cLCB1"},
            "COMPONENTS": "Combined",
            "REINFORCEMENT": True,
            "REINFORCEMENT_TYPE": "REBAR",
            "DISPLAY_MEMBERS": {"BEAM": True, "COLUMN": True, "BRACE": True, "WALL": True},
            "OUTPUT_SECT_LOCATION": {"OPT_MAX": True},
        },
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # 성공 시 지정 경로에 이미지 파일 생성
```

---

## 67. `DESIGN/RC/KDS-41-20-2022/TABLE` — 기둥 설계력(Column Design Forces)

> **기능:** RC 설계용 **기둥(Column) 부재 설계력**(3축 힘·모멘트)을 하중조합별로 추출합니다.

> **공유 URI:** 67·68·69번(기둥·가새·보 설계력)은 **모두 동일한 URI `DESIGN/RC/KDS-41-20-2022/TABLE`(POST)** 를 사용하며, 요청 바디의 `Argument.TABLE_TYPE` 값(`"COLUMNDESIGNFORCES"`)으로만 구분됩니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument`의 필수 키는 `"TABLE_TYPE"`(이 절에서는 `"COLUMNDESIGNFORCES"` 고정)입니다. 주요 속성은 다음과 같습니다.

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
          "default": ""
        },
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "COLUMNDESIGNFORCES"
          ]
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          },
          "default": "System"
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          },
          "default": "System"
        },
        "COMPONENTS": {
          "type": "array",
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
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          },
          "oneOf": [
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
        "PARTS": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "Part2/4",
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
| 2 | 응답 테이블 제목 | `"TABLE_NAME"` | String | `""` | 선택 |
| 3 | 결과 테이블 타입 (고정값 `"COLUMNDESIGNFORCES"`) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 4 | 결과 저장 경로 | `"EXPORT_PATH"` | String | — | 선택 |
| 5 | 단위 설정 (`FORCE`,`DIST`,`HEAT`,`TEMP`) | `"UNIT"` | Object | System | 선택 |
| 6 | 숫자 형식 (`FORMAT`,`PLACE`) | `"STYLES"` | Object | System | 선택 |
| 7 | 출력 컬럼 목록 | `"COMPONENTS"` | Array[String] | — | 선택 |
| 8 | 노드/요소 선택 (`KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나) | `"NODE_ELEMS"` | Object (oneOf) | — | 선택 |
| 9 | 요소 부위 (`"PartI"`/`"Part2/4"`/`"PartJ"`) | `"PARTS"` | Array[String] | `["All"]` | 선택 |


**`TABLE_TYPE` 값:** `"COLUMNDESIGNFORCES"`

**Response HEAD 열 설명** (`<TABLE_TYPE>` 키 아래 `HEAD`/`DATA`로 반환):

| 열(HEAD) | 의미 |
|------|------|
| `Index` | 행 인덱스 |
| `Memb` | 부재(요소) 번호 |
| `Part` | 부재 위치 (I / 2·4분점 / J) |
| `LComName` | 설계 하중조합 이름 |
| `Type` | 극값 종류 (Max / Min) |
| `Fx` | 축력 (부재 좌표계 x) |
| `Fy` | 전단력 (y) |
| `Fz` | 전단력 (z) |
| `Mx` | 비틀림 모멘트 |
| `My` | 휨모멘트 (y축) |
| `Mz` | 휨모멘트 (z축) |


> **참고:** 응답 최상위 키는 요청 `TABLE_NAME`을 따릅니다. `TABLE_NAME`을 지정하지 않은 경우 예시처럼 `"empty"` 키로, 파일 경로를 지정한 경우 해당 문자열이 키가 됩니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "COLUMNDESIGNFORCES",
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
      "PartI"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        915
      ]
    }
  }
}
```

**Response Body** (대표 DATA 3행, 각 행 길이 = HEAD 11열)

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
        "915",
        "I",
        "cLCB5",
        "Max",
        "117.7094",
        "1.8682",
        "1.4004",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "2",
        "915",
        "I",
        "cLCB6",
        "Max",
        "134.8031",
        "2.2316",
        "1.8042",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "3",
        "915",
        "I",
        "cLCB7",
        "Max",
        "185.2628",
        "3.2994",
        "2.3477",
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
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/TABLE"   # 67·68·69 공용 URI

# 기둥 요소 915의 I 단부 설계력 조회
payload = {
    "Argument": {
        "TABLE_TYPE": "COLUMNDESIGNFORCES",   # 기둥 설계력 선택
        "COMPONENTS": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
        "PARTS": ["PartI"],
        "NODE_ELEMS": {"KEYS": [915]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
table = next(iter(res.json().values()))   # 최상위 키는 TABLE_NAME(미지정 시 "empty")
print("HEAD:", table["HEAD"])
for row in table["DATA"][:5]:
    print(row)
```

---

## 68. `DESIGN/RC/KDS-41-20-2022/TABLE` — 가새 설계력(Brace Design Forces)

> **기능:** RC 설계용 **가새(Brace) 부재 설계력**(3축 힘·모멘트)을 추출합니다. 응답 컬럼 구조는 기둥과 동일합니다.

> **공유 URI:** 67·68·69번(기둥·가새·보 설계력)은 **모두 동일한 URI `DESIGN/RC/KDS-41-20-2022/TABLE`(POST)** 를 사용하며, 요청 바디의 `Argument.TABLE_TYPE` 값(`"BRACEDESIGNFORCES"`)으로만 구분됩니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument`의 필수 키는 `"TABLE_TYPE"`(이 절에서는 `"BRACEDESIGNFORCES"` 고정)입니다. 주요 속성은 다음과 같습니다.

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
          "default": ""
        },
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "BRACEDESIGNFORCES"
          ]
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          },
          "default": "System"
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          },
          "default": "System"
        },
        "COMPONENTS": {
          "type": "array",
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
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          },
          "oneOf": [
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
        "PARTS": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "Part2/4",
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
| 2 | 응답 테이블 제목 | `"TABLE_NAME"` | String | `""` | 선택 |
| 3 | 결과 테이블 타입 (고정값 `"BRACEDESIGNFORCES"`) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 4 | 결과 저장 경로 | `"EXPORT_PATH"` | String | — | 선택 |
| 5 | 단위 설정 (`FORCE`,`DIST`,`HEAT`,`TEMP`) | `"UNIT"` | Object | System | 선택 |
| 6 | 숫자 형식 (`FORMAT`,`PLACE`) | `"STYLES"` | Object | System | 선택 |
| 7 | 출력 컬럼 목록 | `"COMPONENTS"` | Array[String] | — | 선택 |
| 8 | 노드/요소 선택 (`KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나) | `"NODE_ELEMS"` | Object (oneOf) | — | 선택 |
| 9 | 요소 부위 (`"PartI"`/`"Part2/4"`/`"PartJ"`) | `"PARTS"` | Array[String] | `["All"]` | 선택 |


**`TABLE_TYPE` 값:** `"BRACEDESIGNFORCES"`

**Response HEAD 열 설명** (`<TABLE_TYPE>` 키 아래 `HEAD`/`DATA`로 반환):

| 열(HEAD) | 의미 |
|------|------|
| `Index` | 행 인덱스 |
| `Memb` | 부재(요소) 번호 |
| `Part` | 부재 위치 (I / 2·4분점 / J) |
| `LComName` | 설계 하중조합 이름 |
| `Type` | 극값 종류 (Max / Min) |
| `Fx` | 축력 (부재 좌표계 x) |
| `Fy` | 전단력 (y) |
| `Fz` | 전단력 (z) |
| `Mx` | 비틀림 모멘트 |
| `My` | 휨모멘트 (y축) |
| `Mz` | 휨모멘트 (z축) |


> **참고:** 응답 최상위 키는 요청 `TABLE_NAME`을 따릅니다. `TABLE_NAME`을 지정하지 않은 경우 예시처럼 `"empty"` 키로, 파일 경로를 지정한 경우 해당 문자열이 키가 됩니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "BRACEDESIGNFORCES",
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
      "PartI"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        1039
      ]
    }
  }
}
```

**Response Body** (대표 DATA 3행, 각 행 길이 = HEAD 11열)

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
        "1039",
        "I",
        "cLCB5",
        "Max",
        "0.000",
        "0.000",
        "19.261",
        "0.000",
        "-5.636",
        "0.000"
      ],
      [
        "2",
        "1039",
        "I",
        "cLCB6",
        "Max",
        "0.000",
        "0.000",
        "24.089",
        "0.000",
        "-6.988",
        "0.000"
      ],
      [
        "3",
        "1039",
        "I",
        "cLCB7",
        "Max",
        "0.000",
        "0.000",
        "34.656",
        "0.000",
        "-9.946",
        "0.000"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/TABLE"   # 67·68·69 공용 URI

# 가새 요소 1039의 I 단부 설계력 조회 (KN, m, 소수 3자리)
payload = {
    "Argument": {
        "TABLE_TYPE": "BRACEDESIGNFORCES",    # 가새 설계력 선택
        "COMPONENTS": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
        "PARTS": ["PartI"],
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
        "NODE_ELEMS": {"KEYS": [1039]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
table = next(iter(res.json().values()))
for row in table["DATA"][:5]:
    print(row)
```

---

## 69. `DESIGN/RC/KDS-41-20-2022/TABLE` — 보 설계력(Beam Design Forces)

> **기능:** RC 설계용 **보(Beam) 부재 설계력**을 추출합니다. 휨설계 기준의 전단력·비틀림·정/부 모멘트를 제공합니다.

> **공유 URI:** 67·68·69번(기둥·가새·보 설계력)은 **모두 동일한 URI `DESIGN/RC/KDS-41-20-2022/TABLE`(POST)** 를 사용하며, 요청 바디의 `Argument.TABLE_TYPE` 값(`"BEAMDESIGNFORCES"`)으로만 구분됩니다.

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument`의 필수 키는 `"TABLE_TYPE"`(이 절에서는 `"BEAMDESIGNFORCES"` 고정)입니다. 주요 속성은 다음과 같습니다.

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
          "default": ""
        },
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "BEAMDESIGNFORCES"
          ]
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          },
          "default": "System"
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          },
          "default": "System"
        },
        "COMPONENTS": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Memb",
              "Part",
              "LComName",
              "Type",
              "Fz",
              "Mx",
              "My(-)",
              "My(+)"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          },
          "oneOf": [
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
        "PARTS": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "Part2/4",
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
| 2 | 응답 테이블 제목 | `"TABLE_NAME"` | String | `""` | 선택 |
| 3 | 결과 테이블 타입 (고정값 `"BEAMDESIGNFORCES"`) | `"TABLE_TYPE"` | String (enum) | — | **필수** |
| 4 | 결과 저장 경로 | `"EXPORT_PATH"` | String | — | 선택 |
| 5 | 단위 설정 (`FORCE`,`DIST`,`HEAT`,`TEMP`) | `"UNIT"` | Object | System | 선택 |
| 6 | 숫자 형식 (`FORMAT`,`PLACE`) | `"STYLES"` | Object | System | 선택 |
| 7 | 출력 컬럼 목록 | `"COMPONENTS"` | Array[String] | — | 선택 |
| 8 | 노드/요소 선택 (`KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 중 하나) | `"NODE_ELEMS"` | Object (oneOf) | — | 선택 |
| 9 | 요소 부위 (`"PartI"`/`"Part2/4"`/`"PartJ"`) | `"PARTS"` | Array[String] | `["All"]` | 선택 |


**`TABLE_TYPE` 값:** `"BEAMDESIGNFORCES"`

**Response HEAD 열 설명** (`<TABLE_TYPE>` 키 아래 `HEAD`/`DATA`로 반환):

| 열(HEAD) | 의미 |
|------|------|
| `Index` | 행 인덱스 |
| `Memb` | 부재(요소) 번호 |
| `Part` | 부재 위치 (I / 2·4분점 / J) |
| `LComName` | 설계 하중조합 이름 |
| `Type` | 극값 종류 (Max / Min) |
| `Fz` | 전단력 (z) |
| `Mx` | 비틀림 모멘트 |
| `My(-)` | 부(-) 휨모멘트 |
| `My(+)` | 정(+) 휨모멘트 |


> **참고:** 응답 최상위 키는 요청 `TABLE_NAME`을 따릅니다. `TABLE_NAME`을 지정하지 않은 경우 예시처럼 `"empty"` 키로, 파일 경로를 지정한 경우 해당 문자열이 키가 됩니다.

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "C:\\MIDAS\\Result\\Beamresult.json",
    "TABLE_TYPE": "BEAMDESIGNFORCES",
    "COMPONENTS": [
      "Index",
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fz",
      "Mx",
      "My(-)",
      "My(+)"
    ],
    "PARTS": [
      "PartJ"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        984
      ]
    }
  }
}
```

**Response Body** (대표 DATA 3행, 각 행 길이 = HEAD 9열)

```json
{
  "C:\\MIDAS\\Result\\Beamresult.json": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fz",
      "Mx",
      "My(-)",
      "My(+)"
    ],
    "DATA": [
      [
        "1",
        "984",
        "J",
        "cLCB100",
        "Max",
        "3.564",
        "0.000",
        "0.000",
        "3.845"
      ],
      [
        "2",
        "984",
        "J",
        "cLCB101",
        "Max",
        "3.884",
        "0.000",
        "0.000",
        "4.668"
      ],
      [
        "3",
        "984",
        "J",
        "cLCB102",
        "Max",
        "6.624",
        "0.000",
        "0.000",
        "6.045"
      ]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "여기에_발급받은_키_입력", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/TABLE"   # 67·68·69 공용 URI

# 보 요소 984의 J 단부 설계력을 파일로도 저장하며 조회
payload = {
    "Argument": {
        "TABLE_NAME": "C:\\MIDAS\\Result\\Beamresult.json",  # 최상위 응답 키가 이 문자열이 됨
        "TABLE_TYPE": "BEAMDESIGNFORCES",     # 보 설계력 선택
        "COMPONENTS": ["Index", "Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(-)", "My(+)"],
        "PARTS": ["PartJ"],
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
        "NODE_ELEMS": {"KEYS": [984]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
table = next(iter(res.json().values()))
print("HEAD:", table["HEAD"])
for row in table["DATA"][:5]:
    print(row)
```

---
