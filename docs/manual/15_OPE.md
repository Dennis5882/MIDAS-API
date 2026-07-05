# 15. OPE

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

`OPE`(Operation) 파트는 GUI 또는 사전처리 계산값을 제어하는 함수로, **DB에 저장되지 않는 데이터**를 다룹니다. 요청 바디는 `"Argument"` 키로 시작하며, 대부분 `POST` 단일 메서드로 동작합니다(일부 조회형 엔드포인트는 `GET`도 지원).

---

## Endpoint 목록

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/ope/PROJECTSTATUS`](#1-opeprojectstatus--project-status) | 프로젝트 현황 조회 | GET |
| 2 | [`/ope/DIVIDEELEM`](#2-opedivideelem--divide-elements) | 요소 분할 | POST |
| 3 | [`/ope/SECTPROP`](#3-opesectprop--section-properties-calculation-results) | 단면 특성값 계산 결과 | GET |
| 4 | [`/ope/USLC`](#4-opeuslc--using-load-combinations) | 하중조합 사용 설정 | POST |
| 5 | [`/ope/LINEBMLD`](#5-opelinebmld--line-beam-load) | 라인 보하중 생성 | POST |
| 6 | [`/ope/AUTOMESH`](#6-opeautomesh--auto-mesh-planar-area) | 평면 영역 자동 메싱 | POST |
| 7 | [`/ope/SSPS`](#7-opessps--surface-spring) | 면 스프링 → 점스프링/탄성링크 변환 | POST |
| 8 | [`/ope/EDMP`](#8-opeedmp--change-property) | 부재 특성 변경(수축·크리프용) | POST |
| 9 | [`/ope/STOR`](#9-opestor--story-calculation) | 층 계산 옵션 | POST |
| 10 | [`/ope/STORY_PARAM`](#10-opestory_param--story-check-parameter) | 층 검토 파라미터 | GET, POST |
| 11 | [`/ope/STORY_IRR_PARAM`](#11-opestory_irr_param--story-irregularity-check-parameter) | 층 불규칙성 검토 파라미터 | GET, POST |
| 12 | [`/ope/STORPROP`](#12-opestorprop--story-properties) | 층 속성 결과 | POST |
| 13 | [`/ope/MEMB`](#13-opememb--member-assignment) | 부재(Member) 배정 | POST |
| 14 | [`/ope/GUSTFACTOR`](#14-opegustfactor--gust-factor-calculator) | 거스트영향계수 계산기 | POST |
| 15 | [`/ope/LCOM-GEN`](#15-opelcom-gen--load-combination-general--kds-2022--aik-src2k) | 하중조합(일반) 자동 생성 | POST |
| 16 | [`/ope/LCOM-CONC`](#16-opelcom-conc--load-combination-concrete--kds-41-20-2022) | 하중조합(콘크리트) 자동 생성 | POST |
| 17 | [`/ope/LCOM-STEEL`](#17-opelcom-steel--load-combination-steel--kds-41-30-2022) | 하중조합(강재) 자동 생성 | POST |
| 18 | [`/ope/LCOM-SRC`](#18-opelcom-src--load-combination-src--kds-41-src-2022--aik-src2k) | 하중조합(SRC) 자동 생성 | POST |

> **참고:** `/ope/LCOM-GEN`, `/ope/LCOM-SRC`는 `DGNCODE` 값에 따라 **KDS:2022 계열**과 **AIK-SRC2K 계열**의 두 가지 스키마를 지원합니다. 본 문서에서는 KDS:2022 스키마를 기준으로 상세 설명하고, AIK-SRC2K 변형은 별도로 함께 표기합니다.

---

## 1. `/ope/PROJECTSTATUS` — Project Status

> **기능:** 현재 프로젝트의 각종 데이터 개수(노드·요소·재료·하중케이스 등) 현황을 조회합니다. DB 저장 없이 실시간 집계 결과만 반환합니다.

### Input URI

```
{base url}/ope/PROJECTSTATUS
```

### Active Methods

`GET`

### Response JSON

```json
{
  "PROJECTSTATUS": {
    "HEAD": ["Name", "Count", "LastNo."],
    "DATA": [
      ["StructureType", "1", "0"],
      ["NamedUCS", "0", "0"],
      ["NamedPlane", "0", "0"],
      ["LineGrid", "0", "0"],
      ["Group", "3", "0"],
      ["BoundaryGroup", "0", "0"],
      ["LoadGroup", "0", "0"],
      ["Node", "69", "69"],
      ["Element", "164", "164"],
      ["Material", "1", "1"],
      ["Section", "31", "9999"],
      ["Thickness", "0", "0"],
      ["Support", "24", "0"],
      ["NodalMass", "69", "0"]
    ],
    "HEAD_LOAD": ["Name", "Count"],
    "DATA_LOAD": [
      ["StaticLoadCase", "9"],
      ["SelfWeight", "2"],
      ["NodalLoad", "45"],
      ["BeamLoad", "76"],
      ["SpectrumFunction", "1"],
      ["SpectrumLoad", "2"],
      ["LoadComb(Concrete)", "37"]
    ]
  }
}
```

### Parameters

응답 전용(GET) 엔드포인트로 요청 바디가 없습니다.

| No. | 설명 | Key | Value 타입 |
|-----|------|-----|-----------|
| 1 | 모델 데이터 현황 테이블 헤더 (Name, Count, LastNo.) | `"HEAD"` | Array [String] |
| 2 | 모델 데이터 현황 목록 (구조타입·노드·요소·재료·단면·지점 등) | `"DATA"` | Array [Array] |
| 3 | 하중 데이터 현황 테이블 헤더 (Name, Count) | `"HEAD_LOAD"` | Array [String] |
| 4 | 하중 데이터 현황 목록 (하중케이스·자중·절점하중·보하중·스펙트럼·하중조합 등) | `"DATA_LOAD"` | Array [Array] |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── GET: 프로젝트 현황 조회 ────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/ope/PROJECTSTATUS", headers=HEADERS)
status = resp.json().get("PROJECTSTATUS", {})

print("=== 모델 데이터 현황 ===")
for row in status.get("DATA", []):
    name, count, last_no = row
    if int(count) > 0:
        print(f"  {name}: {count}개 (최종번호 {last_no})")

print("\n=== 하중 데이터 현황 ===")
for row in status.get("DATA_LOAD", []):
    name, count = row
    if int(count) > 0:
        print(f"  {name}: {count}개")
```

---

## 2. `/ope/DIVIDEELEM` — Divide Elements

> **기능:** 지정한 요소(선·평면·솔리드)를 등분할·비등분할·비율분할·평행 브레이싱·노드기준 분할 등 다양한 방식으로 세분화합니다.

### Input URI

```
{base url}/ope/DIVIDEELEM
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "DIVIDEELEM": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TARGETS": { "type": "array", "items": { "type": "integer" } },
          "START_NUMBER": {
            "type": "object",
            "properties": {
              "NODE_NUMBER": {
                "type": "object",
                "properties": {
                  "NUMBER_OPTION": { "type": "string", "enum": ["Smallest", "Largest", "User"] },
                  "USER_NUM": { "type": "integer" }
                }
              },
              "ELEM_NUMBER": {
                "type": "object",
                "properties": {
                  "NUMBER_OPTION": { "type": "string", "enum": ["Smallest", "Largest", "User"] },
                  "USER_NUM": { "type": "integer" }
                }
              }
            }
          },
          "DIVIDE": {
            "type": "object",
            "properties": {
              "ELEM_TYPE": { "type": "string", "enum": ["Frame", "Wall", "Planar", "Solid"] },
              "DIV_METHOD": { "type": "string", "enum": ["Equal", "Unequal", "ParametricUnequal", "ParallelBracing", "DividebyNode"] },
              "OPTION": {
                "type": "object",
                "properties": {
                  "EQUAL_OPTION": {
                    "type": "object",
                    "properties": {
                      "NUM_X": { "type": "integer" },
                      "NUM_Y": { "type": "integer" },
                      "NUM_Z": { "type": "integer" }
                    }
                  },
                  "UNEQUAL_OPTION": {
                    "type": "object",
                    "properties": {
                      "DIST_X": { "type": "string" },
                      "DIST_Y": { "type": "string" },
                      "DIST_Z": { "type": "string" }
                    }
                  },
                  "PARAMETRIC_OPTION": {
                    "type": "object",
                    "properties": {
                      "RATIO_X": { "type": "string" },
                      "RATIO_Y": { "type": "string" },
                      "RATIO_Z": { "type": "string" }
                    }
                  },
                  "PARALLEL_OPTION": {
                    "type": "object",
                    "properties": {
                      "NUM_OF_DIVISIONS": { "type": "integer" },
                      "MAIN_POST_ELEM": { "type": "array", "items": { "type": "integer" } }
                    }
                  },
                  "BY_NODE_OPTION": {
                    "type": "object",
                    "properties": {
                      "ELEM_NUM": { "type": "integer" },
                      "NODE_NUM": { "type": "integer" }
                    }
                  }
                }
              },
              "SUBDIVIDE_ELEM": { "type": "boolean" },
              "MERGE_DUPLICATE_NODES": {
                "type": "object",
                "properties": {
                  "OPT_CHECK": { "type": "boolean" },
                  "TOLERANCE": { "type": "number" }
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

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 분할 대상 요소 ID | `"TARGETS"` | Array [Integer] | — | Optional |
| 2 | 시작 노드/요소 번호 | `"START_NUMBER"` | Object | System | Optional |
| 2-1 | └ 노드 번호 옵션 · 최소 미사용: `"Smallest"` / 최대+1: `"Largest"` / 사용자지정: `"User"` | `START_NUMBER.NODE_NUMBER.NUMBER_OPTION` | String | — | Optional |
| 2-2 | └ 사용자 지정 노드 번호 (`NUMBER_OPTION="User"`일 때) | `START_NUMBER.NODE_NUMBER.USER_NUM` | Integer | — | Optional |
| 2-3 | └ 요소 번호 옵션 (노드와 동일 enum) | `START_NUMBER.ELEM_NUMBER.NUMBER_OPTION` | String | — | Optional |
| 2-4 | └ 사용자 지정 요소 번호 | `START_NUMBER.ELEM_NUMBER.USER_NUM` | Integer | — | Optional |
| 3 | 분할 설정 | `"DIVIDE"` | Object | — | **Required** |
| 3-1 | └ 요소 타입 · 선요소: `"Frame"` / 벽: `"Wall"` / 평면: `"Planar"` / 솔리드: `"Solid"` | `DIVIDE.ELEM_TYPE` | String | — | **Required** |
| 3-2 | └ 분할 방법 · 등분할: `"Equal"` / 비등분할: `"Unequal"` / 비율분할: `"ParametricUnequal"` / 평행브레이싱: `"ParallelBracing"` / 노드기준: `"DividebyNode"` | `DIVIDE.DIV_METHOD` | String | — | **Required** |
| 3-3 | └ 분할 옵션 (DIV_METHOD별 하위 객체 중 하나) | `DIVIDE.OPTION` | Object | — | **Required** |
| — | Equal: X/Y/Z 방향 분할수 (Frame=X만, Planar=X,Y, Wall=X,Z, Solid=X,Y,Z) | `OPTION.EQUAL_OPTION.{NUM_X,NUM_Y,NUM_Z}` | Integer | — | **Required** |
| — | Unequal: X/Y/Z 방향 비등분할 거리 문자열 (예: `"3@2.0"`) | `OPTION.UNEQUAL_OPTION.{DIST_X,DIST_Y,DIST_Z}` | String | — | **Required** |
| — | ParametricUnequal: X/Y/Z 방향 비율 문자열 (예: `"3@0.3"`) | `OPTION.PARAMETRIC_OPTION.{RATIO_X,RATIO_Y,RATIO_Z}` | String | — | **Required** |
| — | ParallelBracing: 분할 수 / 기준 기둥(Post) 요소 목록 | `OPTION.PARALLEL_OPTION.{NUM_OF_DIVISIONS,MAIN_POST_ELEM}` | Integer/Array | — | **Required** |
| — | DividebyNode: 대상 요소번호 / 분할기준 노드번호 | `OPTION.BY_NODE_OPTION.{ELEM_NUM,NODE_NUM}` | Integer | — | **Required** |
| 4 | 선요소 재분할 여부 | `DIVIDE.SUBDIVIDE_ELEM` | Boolean | — | Optional |
| 5 | 중복 노드 병합 | `DIVIDE.MERGE_DUPLICATE_NODES` | Object | — | Optional |
| 5-1 | └ 활성화 여부 | `MERGE_DUPLICATE_NODES.OPT_CHECK` | Boolean | — | Optional |
| 5-2 | └ 병합 허용오차 | `MERGE_DUPLICATE_NODES.TOLERANCE` | Number | — | Optional |

### Request / Response JSON

**POST Request Body — Frame 등분할**

```json
{
  "Argument": {
    "TARGETS": [1],
    "DIVIDE": {
      "ELEM_TYPE": "Frame",
      "DIV_METHOD": "Equal",
      "OPTION": { "EQUAL_OPTION": { "NUM_X": 10 } }
    }
  }
}
```

**POST Request Body — Planar 비등분할**

```json
{
  "Argument": {
    "TARGETS": [1],
    "DIVIDE": {
      "ELEM_TYPE": "Planar",
      "DIV_METHOD": "Unequal",
      "OPTION": { "UNEQUAL_OPTION": { "DIST_X": "2@2.5", "DIST_Y": "2@3.0" } }
    }
  }
}
```

**POST Request Body — Frame 평행 브레이싱**

```json
{
  "Argument": {
    "DIVIDE": {
      "ELEM_TYPE": "Frame",
      "DIV_METHOD": "ParallelBracing",
      "OPTION": { "PARALLEL_OPTION": { "NUM_OF_DIVISIONS": 3, "MAIN_POST_ELEM": [1, 3] } }
    }
  }
}
```

**POST Response Body**

```json
{
  "DIVIDEELEM": {
    "1": {
      "TYPE": "PLATE",
      "MATL": 1,
      "SECT": 1,
      "NODE": [1, 5, 8, 7, 0, 0, 0, 0],
      "ANGLE": 0,
      "STYPE": 1
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: Frame 요소 10등분할 ──────────────────────────────────────
payload = {
    "Argument": {
        "TARGETS": [1],
        "DIVIDE": {
            "ELEM_TYPE": "Frame",
            "DIV_METHOD": "Equal",
            "OPTION": {"EQUAL_OPTION": {"NUM_X": 10}}
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/DIVIDEELEM", json=payload, headers=HEADERS)
print("POST (Equal):", resp.status_code, resp.json())

# ── POST: Solid 요소 비율분할 ──────────────────────────────────────
payload2 = {
    "Argument": {
        "TARGETS": [1],
        "DIVIDE": {
            "ELEM_TYPE": "Solid",
            "DIV_METHOD": "ParametricUnequal",
            "OPTION": {
                "PARAMETRIC_OPTION": {
                    "RATIO_X": "3@0.3",
                    "RATIO_Y": "4@0.2",
                    "RATIO_Z": "0.1,0.2,0.3"
                }
            }
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/DIVIDEELEM", json=payload2, headers=HEADERS)
print("POST (ParametricUnequal):", resp.status_code, resp.json())
```

---

## 3. `/ope/SECTPROP` — Section Properties Calculation Results

> **기능:** 등록된 단면의 계산된 단면 특성값(면적·관성모멘트·단면계수 등)을 조회합니다.

### Input URI

```
{base url}/ope/SECTPROP
```

### Active Methods

`GET`

### Response JSON

```json
{
  "SECTPROP": {
    "1": {
      "HEAD": ["Property", "Value", "Unit"],
      "DATA": [
        ["Area", "0.011980", "m2"],
        ["Asy", "0.007500", "m2"],
        ["Asz", "0.003000", "m2"],
        ["Ixx", "0.000001", "m4"],
        ["Iyy", "0.000204", "m4"],
        ["Izz", "0.000068", "m4"],
        ["Cyp", "0.150000", "m"],
        ["Cym", "0.150000", "m"],
        ["Czp", "0.150000", "m"],
        ["Czm", "0.150000", "m"],
        ["Qyb", "0.073237", "m2"],
        ["Qzb", "0.011250", "m2"],
        ["Peri:O", "1.780000", "m"],
        ["Peri:I", "0.000000", "m"],
        ["Center:y", "0.150000", "m"],
        ["Center:z", "0.150000", "m"]
      ]
    }
  }
}
```

### Parameters

응답 전용(GET) 엔드포인트입니다. Key(`"1"`)는 단면 ID입니다.

| No. | 설명 | Key | Value 타입 |
|-----|------|-----|-----------|
| 1 | 결과 테이블 헤더 (Property, Value, Unit) | `"HEAD"` | Array [String] |
| 2 | 단면 특성값 목록 (Area, Asy, Asz, Ixx, Iyy, Izz, Cyp/Cym/Czp/Czm, Qyb, Qzb, Peri:O/I, Center:y/z, 꼭짓점 좌표 y1~y4/z1~z4 등) | `"DATA"` | Array [Array] |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── GET: 전체 단면 특성값 조회 ─────────────────────────────────────
resp = requests.get(f"{BASE_URL}/ope/SECTPROP", headers=HEADERS)
props = resp.json().get("SECTPROP", {})

for sect_id, result in props.items():
    print(f"[단면 {sect_id}]")
    for row in result["DATA"]:
        name, value, unit = row
        print(f"  {name} = {value} {unit}")
```

---

## 4. `/ope/USLC` — Using Load Combinations

> **기능:** 정의된 하중조합을 설계용 프리픽스와 함께 강재/콘크리트/SRC 설계에 사용하도록 지정하고, 각 하중조합에 포함할 하중 종류를 선택합니다.

### Input URI

```
{base url}/ope/USLC
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "USLC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "PREFIX": { "type": "string" },
          "POSITION": { "type": "string", "enum": ["STEEL", "CONC", "SRC"] },
          "LCOM_LIST": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "TYPE": { "type": "string", "enum": ["GEN", "STEEL", "CONC", "SRC", "STLCOMP", "SEISMIC"] },
                "NAME": { "type": "string" }
              }
            }
          },
          "LOADS": {
            "type": "object",
            "properties": {
              "SELF_WEIGHT": { "type": "boolean", "default": true },
              "NODAL_BODY_FROCE": { "type": "boolean", "default": true },
              "NODAL_LOAD": { "type": "boolean", "default": true },
              "SPECIFIED_DISPLACEMENT": { "type": "boolean", "default": true },
              "BEAM_LOAD": { "type": "boolean", "default": true },
              "FLOOR_LOAD": { "type": "boolean", "default": true },
              "FINISHING_MATERIAL_LOAD": { "type": "boolean", "default": true },
              "PRESSURE_LOAD": { "type": "boolean", "default": true },
              "PLANE_LOAD": { "type": "boolean", "default": true },
              "SYSTEM_TEMPERATURE": { "type": "boolean", "default": true },
              "NODAL_TEMPERATURE": { "type": "boolean", "default": true },
              "ELEMENT_TEMPERATURE": { "type": "boolean", "default": true },
              "TEMPERATURE_GRADIENT": { "type": "boolean", "default": true },
              "BEAM_SECTION_TEMPERATURE": { "type": "boolean", "default": true },
              "PRESTRESS_LOAD": { "type": "boolean", "default": true },
              "PRETENSION_LOAD": { "type": "boolean", "default": true },
              "TENDON_PRESTRESS_LOAD": { "type": "boolean", "default": true }
            }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 하중케이스/설계조합 이름 접두어 | `"PREFIX"` | String | System | Optional |
| 2 | 설계조합 생성 위치 · 강재: `"STEEL"` / 콘크리트: `"CONC"` / SRC: `"SRC"` | `"POSITION"` | String | — | **Required** |
| 3 | 선택된 조합 목록 | `"LCOM_LIST"` | Array [Object] | — | **Required** |
| 3-1 | └ 하중조합 타입 · 일반: `"GEN"` / 강재: `"STEEL"` / 콘크리트: `"CONC"` / SRC: `"SRC"` / 강합성거더: `"STLCOMP"` / 내진: `"SEISMIC"` | `LCOM_LIST[].TYPE` | String | — | **Required** |
| 3-2 | └ 하중조합 이름 | `LCOM_LIST[].NAME` | String | — | **Required** |
| 4 | 선택 하중 종류 | `"LOADS"` | Object | — | Optional |
| 4-1 | └ 자중 | `LOADS.SELF_WEIGHT` | Boolean | `true` | Optional |
| 4-2 | └ 절점체적력 | `LOADS.NODAL_BODY_FROCE` | Boolean | `true` | Optional |
| 4-3 | └ 절점하중 | `LOADS.NODAL_LOAD` | Boolean | `true` | Optional |
| 4-4 | └ 지정변위 | `LOADS.SPECIFIED_DISPLACEMENT` | Boolean | `true` | Optional |
| 4-5 | └ 보하중 | `LOADS.BEAM_LOAD` | Boolean | `true` | Optional |
| 4-6 | └ 바닥하중 | `LOADS.FLOOR_LOAD` | Boolean | `true` | Optional |
| 4-7 | └ 마감재하중 | `LOADS.FINISHING_MATERIAL_LOAD` | Boolean | `true` | Optional |
| 4-8 | └ 압력하중 | `LOADS.PRESSURE_LOAD` | Boolean | `true` | Optional |
| 4-9 | └ 평면하중 | `LOADS.PLANE_LOAD` | Boolean | `true` | Optional |
| 4-10 | └ 시스템 온도 | `LOADS.SYSTEM_TEMPERATURE` | Boolean | `true` | Optional |
| 4-11 | └ 절점 온도 | `LOADS.NODAL_TEMPERATURE` | Boolean | `true` | Optional |
| 4-12 | └ 요소 온도 | `LOADS.ELEMENT_TEMPERATURE` | Boolean | `true` | Optional |
| 4-13 | └ 온도구배 | `LOADS.TEMPERATURE_GRADIENT` | Boolean | `true` | Optional |
| 4-14 | └ 보단면 온도 | `LOADS.BEAM_SECTION_TEMPERATURE` | Boolean | `true` | Optional |
| 4-15 | └ 프리스트레스 하중 | `LOADS.PRESTRESS_LOAD` | Boolean | `true` | Optional |
| 4-16 | └ 프리텐션 하중 | `LOADS.PRETENSION_LOAD` | Boolean | `true` | Optional |
| 4-17 | └ 텐던 프리스트레스 하중 | `LOADS.TENDON_PRESTRESS_LOAD` | Boolean | `true` | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "LCOM_LIST": [
      { "TYPE": "STEEL", "NAME": "sLCB1" }
    ],
    "PREFIX": "N",
    "POSITION": "STEEL",
    "LOADS": {
      "SELF_WEIGHT": true,
      "NODAL_BODY_FROCE": true,
      "NODAL_LOAD": true,
      "SPECIFIED_DISPLACEMENT": true,
      "BEAM_LOAD": true,
      "FLOOR_LOAD": true,
      "FINISHING_MATERIAL_LOAD": true,
      "PRESSURE_LOAD": true,
      "PLANE_LOAD": true,
      "SYSTEM_TEMPERATURE": true,
      "NODAL_TEMPERATURE": true,
      "ELEMENT_TEMPERATURE": true,
      "TEMPERATURE_GRADIENT": true,
      "BEAM_SECTION_TEMPERATURE": true,
      "PRESTRESS_LOAD": true,
      "PRETENSION_LOAD": true,
      "TENDON_PRESTRESS_LOAD": true
    }
  }
}
```

**POST Response Body**

```json
{
  "USLC": {
    "message": "Success"
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 강재 설계 하중조합에 사용될 하중 지정 ────────────────────
payload = {
    "Argument": {
        "LCOM_LIST": [
            {"TYPE": "STEEL", "NAME": "sLCB1"},
            {"TYPE": "STEEL", "NAME": "sLCB2"}
        ],
        "PREFIX": "N",
        "POSITION": "STEEL",
        "LOADS": {
            "SELF_WEIGHT": True,
            "NODAL_LOAD": True,
            "BEAM_LOAD": True,
            "FLOOR_LOAD": True
            # 나머지는 기본값(true) 적용
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/USLC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 5. `/ope/LINEBMLD` — Line Beam Load

> **기능:** 하중이 작용하는 선(Line)을 절점 2개 또는 선택된 요소로 정의하여, 그 선을 지나는 부재들에 자동으로 집중/등분포/사다리꼴/곡선 하중을 생성·분배합니다.

### Input URI

```
{base url}/ope/LINEBMLD
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "LINEBMLD": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "LCNAME": { "type": "string" },
          "GROUP_NAME": { "type": "string" },
          "TYPE": { "type": "string" },
          "TARGET": {
            "type": "object",
            "properties": {
              "METHOD": { "type": "integer" },
              "ELEM": { "type": "array", "items": { "type": "integer" } },
              "NODE": { "type": "array", "items": { "type": "integer" } }
            }
          },
          "ECCEN": {
            "type": "object",
            "properties": {
              "USE": { "type": "boolean" },
              "TYPE": { "type": "integer" },
              "DIR": { "type": "string" },
              "I_END": { "type": "number" },
              "J_END": { "type": "number" },
              "USE_J_END": { "type": "boolean" }
            }
          },
          "ADD_H": {
            "type": "object",
            "properties": {
              "USE": { "type": "boolean" },
              "I_END": { "type": "number" },
              "J_END": { "type": "number" },
              "USE_J_END": { "type": "boolean" }
            }
          },
          "LOAD": {
            "type": "object",
            "properties": {
              "DIR": { "type": "string" },
              "USE_PROJECTION": { "type": "boolean" },
              "TYPE": { "type": "integer" },
              "D": { "type": "array", "items": { "type": "number" } },
              "P": { "type": "array", "items": { "type": "number" } },
              "A": { "type": "number" },
              "B": { "type": "number" },
              "C": { "type": "number" }
            }
          },
          "COPY": {
            "type": "object",
            "properties": {
              "USE": { "type": "boolean" },
              "AXIS": { "type": "string" },
              "DIST": { "type": "string" }
            }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 하중케이스 이름 | `"LCNAME"` | String | — | **Required** |
| 2 | 하중 그룹 이름 | `"GROUP_NAME"` | String | — | Optional |
| 3 | 하중 타입 · 집중하중: `"CONLOAD"` / 집중모멘트: `"CONMOMENT"` / 등분포하중: `"UNILOAD"` / 등분포모멘트: `"UNIMOMENT"` / 사다리꼴하중: `"TRALOAD"` / 사다리꼴모멘트: `"TRAMOMENT"` / 등분포압력: `"UNIPRESSURE"` / 사다리꼴압력: `"TRAPRESSURE"` / 곡선하중: `"CURVED"` | `"TYPE"` | String | — | **Required** |
| 4 | 하중 적용 대상 정보 | `"TARGET"` | Object | — | **Required** |
| 4-1 | └ 적용 방법 · 하중선 위: `0` / 선택 요소: `1` | `TARGET.METHOD` | Integer | — | **Required** |
| 4-2 | └ 적용 대상 요소 목록 | `TARGET.ELEM` | Array [Integer] | — | **Required** |
| 4-3 | └ 하중선 정의 노드 (2개) | `TARGET.NODE` | Array [Integer, 2] | — | **Required** |
| 5 | 편심 옵션(`TYPE`이 CONLOAD/UNILOAD/TRALOAD/CURVED일 때만 사용 가능) | `"ECCEN"` | Object | — | Optional |
| 5-1 | └ 활성화 | `ECCEN.USE` | Boolean | `false` | — |
| 5-2 | └ 타입 · 도심: `0` / 옵셋: `1` | `ECCEN.TYPE` | Integer | — | — |
| 5-3 | └ 방향 · 국부y: `"LY"` / 국부z: `"LZ"` / 전체X: `"GX"` / 전체Y: `"GY"` / 전체Z: `"GZ"` | `ECCEN.DIR` | String | — | — |
| 5-4 | └ I단 편심량 | `ECCEN.I_END` | Number | — | — |
| 5-5 | └ J단 편심량(`USE_J_END=true`일 때) | `ECCEN.J_END` | Number | — | — |
| 5-6 | └ J단 편심 활성화 | `ECCEN.USE_J_END` | Boolean | — | — |
| 6 | 상단 추가높이 옵션(`TYPE`이 UNIPRESSURE/TRAPRESSURE일 때만 사용 가능) | `"ADD_H"` | Object | — | Optional |
| 6-1 | └ 활성화 | `ADD_H.USE` | Boolean | `false` | — |
| 6-2 | └ I단 값 | `ADD_H.I_END` | Number | — | — |
| 6-3 | └ J단 값(`USE_J_END=true`일 때) | `ADD_H.J_END` | Number | — | — |
| 6-4 | └ J단 활성화 | `ADD_H.USE_J_END` | Boolean | — | — |
| 7 | 하중 값 | `"LOAD"` | Object | — | **Required** |
| 7-1 | └ 방향 · 국부x/y/z(`"LX"`/`"LY"`/`"LZ"`), 전체X/Y/Z(`"GX"`/`"GY"`/`"GZ"`); `UNIPRESSURE`/`TRAPRESSURE`는 `ADD_H` 설정에 따라 `LY`/`LZ`만 가능 | `LOAD.DIR` | String | — | **Required** |
| 7-2 | └ 투영 여부 (METHOD=0→기본 false, METHOD=1→기본 true) | `LOAD.USE_PROJECTION` | Boolean | System | Optional |
| 7-3 | └ 거리 타입(`CURVED` 제외 모든 타입) · 상대: `0` / 절대: `1` | `LOAD.TYPE` | Integer | — | **Required** |
| 7-4 | └ 거리 배열 [x1,x2,x3,x4] (`CURVED` 제외) | `LOAD.D` | Array [Number, 4] | — | **Required** |
| 7-5 | └ 크기 배열 [P1,P2,P3,P4] (`CURVED` 제외) | `LOAD.P` | Array [Number, 4] | — | **Required** |
| 7-6 | └ 곡선식 계수 a (`CURVED` 전용) | `LOAD.A` | Number | — | **Required** |
| 7-7 | └ 곡선식 계수 b (`CURVED` 전용) | `LOAD.B` | Number | — | **Required** |
| 7-8 | └ 곡선식 계수 c (`CURVED` 전용) | `LOAD.C` | Number | — | **Required** |
| 8 | 복사 옵션 | `"COPY"` | Object | — | Optional |
| 8-1 | └ 활성화 | `COPY.USE` | Boolean | `false` | — |
| 8-2 | └ 복사 축 · `"X"`/`"Y"`/`"Z"` | `COPY.AXIS` | String | — | — |
| 8-3 | └ 복사 거리 (예: `"10@3.0"`) | `COPY.DIST` | String | — | — |

### Request / Response JSON

**POST Request Body — 집중하중**

```json
{
  "Argument": {
    "LCNAME": "CONLOAD_03",
    "GROUP_NAME": "LoadGroup1",
    "TYPE": "CONLOAD",
    "TARGET": { "METHOD": 0, "NODE": [23, 33] },
    "LOAD": {
      "DIR": "GZ",
      "TYPE": 1,
      "D": [0.75, 1.35, 1.95, 2.55],
      "P": [-1, -2, -3, -4]
    }
  }
}
```

**POST Request Body — 편심을 가진 집중하중**

```json
{
  "Argument": {
    "LCNAME": "CONLOAD_14",
    "TYPE": "CONLOAD",
    "TARGET": { "METHOD": 0, "NODE": [56, 66] },
    "ECCEN": {
      "USE": true,
      "TYPE": 0,
      "DIR": "LZ",
      "I_END": -0.15,
      "J_END": 0.15,
      "USE_J_END": true
    },
    "LOAD": {
      "DIR": "GZ",
      "TYPE": 1,
      "D": [0.75, 1.35, 1.95, 2.55],
      "P": [-1, -2, -3, -4]
    }
  }
}
```

**POST Response Body**

```json
{
  "LINEBMLD": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "A",
          "GROUP_NAME": "",
          "CMD": "LINE",
          "TYPE": "CONLOAD",
          "DIRECTION": "GZ",
          "USE_PROJECTION": false,
          "USE_ECCEN": false,
          "D": [0.075, 0.135, 0.195, 0.255],
          "P": [-1, -2, -3, -4],
          "USE_ADDITIONAL": false,
          "ADDITIONAL_I_END": 0,
          "ADDITIONAL_J_END": 0,
          "USE_ADDITIONAL_J_END": false
        }
      ]
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 노드 라인에 사다리꼴 하중 생성 ───────────────────────────
payload = {
    "Argument": {
        "LCNAME": "TRALOAD_03",
        "GROUP_NAME": "LoadGroup1",
        "TYPE": "TRALOAD",
        "TARGET": {"METHOD": 0, "NODE": [23, 33]},
        "LOAD": {
            "DIR": "GZ",
            "USE_PROJECTION": True,
            "TYPE": 1,
            "D": [0.75, 1.35, 1.95, 2.55],
            "P": [-1, -2, -3, -4]
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/LINEBMLD", json=payload, headers=HEADERS)
print("POST (사다리꼴):", resp.status_code, resp.json())

# ── POST: 등분포하중 후 Y축 방향 복사 ──────────────────────────────
payload2 = {
    "Argument": {
        "LCNAME": "UNILOAD_17",
        "TYPE": "UNILOAD",
        "TARGET": {"METHOD": 0, "NODE": [78, 88]},
        "LOAD": {"DIR": "GZ", "TYPE": 0, "D": [0.25, 0.85], "P": [-3]},
        "COPY": {"USE": True, "AXIS": "Y", "DIST": "10@3.0"}
    }
}
resp = requests.post(f"{BASE_URL}/ope/LINEBMLD", json=payload2, headers=HEADERS)
print("POST (복사):", resp.status_code, resp.json())
```

---

## 6. `/ope/AUTOMESH` — Auto-Mesh Planar Area

> **기능:** 노드·선요소·평면요소로 둘러싸인 영역을 자동으로 사각형/삼각형 메시로 분할하여 판(Plate)·평면응력·평면변형률·축대칭 요소를 생성합니다.

### Input URI

```
{base url}/ope/AUTOMESH
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "AUTOMESH": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "MESHER": {
            "type": "object",
            "properties": {
              "METHOD": { "type": "string" },
              "TARGETS": { "type": "array", "items": { "type": "integer" } },
              "TYPE": { "type": "string" },
              "MESH_INNER_DOMAIN": { "type": "boolean" },
              "INCLUDE_INTERIOR_NODES": {
                "type": "object",
                "properties": {
                  "OPT_CHECK": { "type": "boolean" },
                  "OPTION": { "type": "string" },
                  "VALUE": { "type": "array", "items": { "type": "integer" } }
                }
              },
              "INCLUDE_INTERIOR_LINES": {
                "type": "object",
                "properties": {
                  "OPT_CHECK": { "type": "boolean" },
                  "OPTION": { "type": "string" },
                  "VALUE": { "type": "array", "items": { "type": "integer" } }
                }
              },
              "INCLUDE_BOUNDARY_CONNECTIVITY": { "type": "boolean" }
            }
          },
          "MESH_SIZE": {
            "type": "object",
            "properties": {
              "LENGTH": { "type": "integer" },
              "DIV": { "type": "integer" }
            }
          },
          "PROPERTY": {
            "type": "object",
            "properties": {
              "ELEMENT_TYPE": { "type": "string" },
              "ELEMENT_SUB_TYPE": {
                "type": "object",
                "properties": {
                  "TYPE": { "type": "string" },
                  "WITH_DRILLING_DOF": { "type": "boolean" }
                }
              },
              "MATERIAL": { "type": "integer" },
              "THICKNESS": { "type": "integer" }
            }
          },
          "DOMAIN_NAME": {
            "type": "object",
            "properties": { "NAME": { "type": "string" } }
          },
          "ADDITIONAL_OPTION": {
            "type": "object",
            "properties": {
              "DELETE_LINE_ELEM": { "type": "boolean" },
              "SUBDIVIDE_LINE_ELEM": { "type": "boolean" }
            }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 메셔 설정 | `"MESHER"` | Object | — | **Required** |
| 1-1 | └ 자동 메시 방법 · 노드: `"Nodes"` / 선요소: `"Line Elements"` / 평면요소: `"Planar Elements"` | `MESHER.METHOD` | String | `"Line Elements"` | Optional |
| 1-2 | └ 메시 대상 요소/노드 목록 | `MESHER.TARGETS` | Array [Integer] | — | **Required** |
| 1-3 | └ 메시 형태 · 사각형: `"Quadrilateral"` / 사각+삼각: `"Quad and Triangle"` / 삼각형: `"Triangle"` | `MESHER.TYPE` | String | `"Quadrilateral"` | Optional |
| 1-4 | └ 내부 도메인 메시 생성 여부 | `MESHER.MESH_INNER_DOMAIN` | Boolean | `false` | Optional |
| 1-5 | └ 영역 내 노드 고려 옵션 | `MESHER.INCLUDE_INTERIOR_NODES` | Object | — | Optional |
| 1-5-a | 　└ 활성화 | `INCLUDE_INTERIOR_NODES.OPT_CHECK` | Boolean | `true` | Optional |
| 1-5-b | 　└ 감지 방식 · `"Auto"`/`"User"` | `INCLUDE_INTERIOR_NODES.OPTION` | String | `"Auto"` | Optional |
| 1-5-c | 　└ 포함 노드 번호(User일 때) | `INCLUDE_INTERIOR_NODES.VALUE` | Array [Integer] | — | **Required**(User일 때) |
| 1-6 | └ 영역 내 선요소 고려 옵션 (구조는 1-5와 동일) | `MESHER.INCLUDE_INTERIOR_LINES` | Object | — | Optional |
| 1-7 | └ 메시 경계 연결 여부 | `MESHER.INCLUDE_BOUNDARY_CONNECTIVITY` | Boolean | `true` | Optional |
| 2 | 메시 크기 | `"MESH_SIZE"` | Object | — | **Required** |
| 2-1 | └ 길이 기준 (`DIV`와 동시 사용 불가) | `MESH_SIZE.LENGTH` | Number | — | **Required** |
| 2-2 | └ 분할수 기준 (`LENGTH`와 동시 사용 불가) | `MESH_SIZE.DIV` | Number | — | **Required** |
| 3 | 요소 속성 | `"PROPERTY"` | Object | — | **Required** |
| 3-1 | └ 요소 타입 · `"Plate"`/`"Plane Stress"`/`"Plane Strain"`/`"Axisymmetric"` | `PROPERTY.ELEMENT_TYPE` | String | `"Plate"` | Optional |
| 3-2 | └ 요소 세부 타입 | `PROPERTY.ELEMENT_SUB_TYPE` | Object | — | Optional |
| 3-2-a | 　└ 판 두께 타입(`ELEMENT_TYPE="Plate"`일 때) · `"Thick"`/`"Thin"` | `ELEMENT_SUB_TYPE.TYPE` | String | `"Thick"` | Optional |
| 3-2-b | 　└ Drilling DOF 사용(`Plate`/`Plane Stress`일 때) | `ELEMENT_SUB_TYPE.WITH_DRILLING_DOF` | Boolean | `true` | Optional |
| 3-3 | └ 재료 번호 | `PROPERTY.MATERIAL` | Integer | — | **Required** |
| 3-4 | └ 두께 번호(`Plate`/`Plane Stress`일 때) | `PROPERTY.THICKNESS` | Integer | — | Optional |
| 4 | 도메인 이름 | `"DOMAIN_NAME"` | Object | — | **Required** |
| 4-1 | └ 이름 | `DOMAIN_NAME.NAME` | String | — | **Required** |
| 5 | 추가 옵션 | `"ADDITIONAL_OPTION"` | Object | — | Optional |
| 5-1 | └ 원본 선/경계 요소 삭제 | `ADDITIONAL_OPTION.DELETE_LINE_ELEM` | Boolean | `false` | Optional |
| 5-2 | └ 원본 선/경계 요소 재분할 | `ADDITIONAL_OPTION.SUBDIVIDE_LINE_ELEM` | Boolean | `true` | Optional |

### Request / Response JSON

**POST Request Body — 선요소 기본 메싱**

```json
{
  "Argument": {
    "MESHER": { "TARGETS": [1400, 1397, 1398, 1399] },
    "MESH_SIZE": { "LENGTH": 1 },
    "PROPERTY": { "MATERIAL": 1, "THICKNESS": 1 },
    "DOMAIN_NAME": { "NAME": "frame" }
  }
}
```

**POST Request Body — 평면요소 + 사각/삼각 + 내부노드/선 지정 + 추가옵션**

```json
{
  "Argument": {
    "MESHER": {
      "METHOD": "PlanarElements",
      "TARGETS": [1402],
      "TYPE": "Quadandtriangle",
      "MESH_INNER_DOMAIN": true,
      "INCLUDE_INTERIOR_NODES": { "OPT_CHECK": true, "OPTION": "User", "VALUE": [1] },
      "INCLUDE_INTERIOR_LINES": { "OPT_CHECK": true, "OPTION": "User", "VALUE": [2] },
      "INCLUDE_BOUNDARY_CONNECTIVITY": true
    },
    "MESH_SIZE": { "DIV": 3 },
    "PROPERTY": {
      "ELEMENT_TYPE": "Plate",
      "ELEMENT_SUB_TYPE": { "TYPE": "Thick", "WITH_DRILLING_DOF": true },
      "MATERIAL": 1,
      "THICKNESS": 1
    },
    "DOMAIN_NAME": { "NAME": "Plate2" },
    "ADDITIONAL_OPTION": { "DELETE_LINE_ELEM": false, "SUBDIVIDE_LINE_ELEM": true }
  }
}
```

**POST Response Body**

```json
{
  "AUTOMESH": {
    "1794": { "TYPE": "PLATE", "MATL": 1, "SECT": 1, "NODE": [1545, 1980, 1985, 1984, 0, 0, 0, 0], "ANGLE": 0, "STYPE": 3 },
    "1795": { "TYPE": "PLATE", "MATL": 1, "SECT": 1, "NODE": [1984, 1985, 1986, 1983, 0, 0, 0, 0], "ANGLE": 0, "STYPE": 3 }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 노드로 둘러싸인 영역 자동 메싱 (평면응력, 사각+삼각) ─────
payload = {
    "Argument": {
        "MESHER": {
            "METHOD": "Nodes",
            "TARGETS": [502, 503, 504],
            "TYPE": "Quadandtriangle",
            "MESH_INNER_DOMAIN": True,
            "INCLUDE_INTERIOR_NODES": {"OPT_CHECK": True, "OPTION": "User", "VALUE": [1]},
            "INCLUDE_INTERIOR_LINES": {"OPT_CHECK": True, "OPTION": "User", "VALUE": [2]},
            "INCLUDE_BOUNDARY_CONNECTIVITY": True
        },
        "MESH_SIZE": {"DIV": 3},
        "PROPERTY": {
            "ELEMENT_TYPE": "PlaneStress",
            "ELEMENT_SUB_TYPE": {"TYPE": "Thick", "WITH_DRILLING_DOF": True},
            "MATERIAL": 1,
            "THICKNESS": 1
        },
        "DOMAIN_NAME": {"NAME": "Plate2"},
        "ADDITIONAL_OPTION": {"DELETE_LINE_ELEM": False, "SUBDIVIDE_LINE_ELEM": True}
    }
}
resp = requests.post(f"{BASE_URL}/ope/AUTOMESH", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 7. `/ope/SSPS` — Surface Spring

> **기능:** 면 스프링(Surface Spring) 경계조건을 점스프링(Point Spring) 또는 탄성링크(Elastic Link)로 변환하여 생성합니다. 프레임/평면/솔리드(면·절점) 요소별 변환 방식을 지원합니다.

### Input URI

```
{base url}/ope/SSPS
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "SSPS": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "CONVERT_TO": { "type": "string", "enum": ["POINT_SPRING", "ELASTIC_LINK"] },
          "GROUP_NAME": { "type": "string" },
          "NODE_ELEMS": {
            "type": "object",
            "properties": { "KEYS": { "type": "array", "items": { "type": "integer" } } }
          },
          "ELEMENT": {
            "type": "object",
            "properties": {
              "TYPE": { "type": "string", "enum": ["FRAME", "PLANAR", "SOLID_FACE", "SOLID_NODE"] },
              "FACE": { "type": "integer", "enum": [1, 2, 3, 4, 5, 6] },
              "WIDTH": { "type": "number" }
            }
          },
          "BOUNDARY": {
            "type": "object",
            "properties": {
              "TYPE": { "type": "string", "enum": ["LINEAR", "COMP", "TENS", "MULTI"] },
              "DIR": { "type": "integer", "enum": [0, 1, 2, 3, 4, 5, 6, 7] },
              "STIFF": { "type": "array", "items": { "type": "number" }, "maxItems": 3 },
              "PHU": { "type": "number" },
              "SUBGRADE": { "type": "number" },
              "LENGTH": { "type": "number" },
              "bDAMP": { "type": "boolean" },
              "DAMP": { "type": "array", "items": { "type": "number" }, "maxItems": 3 }
            }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 변환 방식 · 점스프링: `"POINT_SPRING"` / 탄성링크: `"ELASTIC_LINK"` | `"CONVERT_TO"` | String | — | **Required** |
| 2 | 경계 그룹 이름 | `"GROUP_NAME"` | String | `""` | Optional |
| 3 | 대상 노드/요소 번호 목록 | `"NODE_ELEMS"` | Object | — | **Required** |
| 3-1 | └ 번호 배열 | `NODE_ELEMS.KEYS` | Array [Integer] | — | **Required** |
| 4 | 요소 타입 정보 | `"ELEMENT"` | Object | — | **Required** |
| 4-1 | └ 타입 · 프레임: `"FRAME"` / 평면: `"PLANAR"` / 솔리드(면): `"SOLID_FACE"` / 솔리드(절점): `"SOLID_NODE"` | `ELEMENT.TYPE` | String | — | **Required** |
| 4-2 | └ 폭 (`FRAME` 전용) | `ELEMENT.WIDTH` | Number | — | **Required**(FRAME일 때) |
| 4-3 | └ 면 번호 1~6 (`SOLID_FACE` 전용) | `ELEMENT.FACE` | Integer | — | **Required**(SOLID_FACE일 때) |
| 5 | 경계 정보 | `"BOUNDARY"` | Object | — | **Required** |
| 5-1 | └ 경계 타입 · 선형: `"LINEAR"` / 압축전담: `"COMP"` / 인장전담: `"TENS"` / 다선형: `"MULTI"` | `BOUNDARY.TYPE` | String | — | **Required** |
| 5-2 | └ 강성 [Kx,Ky,Kz] (LINEAR/MULTI) | `BOUNDARY.STIFF` | Array [Number, 3] | — | **Required**(해당 타입) |
| 5-3 | └ 감쇠 고려 여부 (LINEAR/MULTI) | `BOUNDARY.bDAMP` | Boolean | — | **Required**(해당 타입) |
| 5-4 | └ 감쇠상수 [Cx,Cy,Cz] (LINEAR/MULTI) | `BOUNDARY.DAMP` | Array [Number, 3] | — | **Required**(해당 타입) |
| 5-5 | └ 경계 방향(COMP/TENS/점스프링 외 모든 경우) · Normal(+): `0` / Normal(-): `1` / UCS-x(+): `2` / UCS-x(-): `3` / UCS-y(+): `4` / UCS-y(-): `5` / UCS-z(+): `6` / UCS-z(-): `7` | `BOUNDARY.DIR` | Integer | — | **Required**(해당 타입) |
| 5-6 | └ 지반반력계수 (COMP/TENS/탄성링크 전체) | `BOUNDARY.SUBGRADE` | Number | — | **Required**(해당 타입) |
| 5-7 | └ 한계강도 (MULTI/탄성링크 MULTI) | `BOUNDARY.PHU` | Number | — | **Required**(해당 타입) |
| 5-8 | └ 탄성링크 길이 (`CONVERT_TO="ELASTIC_LINK"` 전체 타입) | `BOUNDARY.LENGTH` | Number | — | **Required**(탄성링크) |

> **참고:** `BOUNDARY` 필드 필수 여부는 `CONVERT_TO`(점스프링/탄성링크)와 `BOUNDARY.TYPE`(선형/압축전담/인장전담/다선형) 조합에 따라 달라집니다. 자세한 조합은 위 표의 "필수" 열 조건을 참고하세요.

### Request / Response JSON

**POST Request Body — 점스프링(프레임)**

```json
{
  "Argument": {
    "CONVERT_TO": "POINT_SPRING",
    "GROUP_NAME": "B1",
    "NODE_ELEMS": { "KEYS": [61, 62, 63] },
    "ELEMENT": { "TYPE": "FRAME", "WIDTH": 10 },
    "BOUNDARY": {
      "TYPE": "LINEAR",
      "STIFF": [1000, 2000, 3000],
      "bDAMP": true,
      "DAMP": [1, 2, 3]
    }
  }
}
```

**POST Request Body — 탄성링크(솔리드 면)**

```json
{
  "Argument": {
    "CONVERT_TO": "ELASTIC_LINK",
    "GROUP_NAME": "B1",
    "NODE_ELEMS": { "KEYS": [71, 72, 73] },
    "ELEMENT": { "TYPE": "SOLID_FACE", "FACE": 1 },
    "BOUNDARY": { "TYPE": "TENS", "DIR": 7, "SUBGRADE": 5000, "LENGTH": 0.5 }
  }
}
```

**POST Response Body**

```json
{
  "SSPS": {
    "message": "Success"
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 프레임 면스프링 → 점스프링(선형) 변환 ────────────────────
payload = {
    "Argument": {
        "CONVERT_TO": "POINT_SPRING",
        "GROUP_NAME": "B1",
        "NODE_ELEMS": {"KEYS": [61, 62, 63]},
        "ELEMENT": {"TYPE": "FRAME", "WIDTH": 10},
        "BOUNDARY": {
            "TYPE": "LINEAR",
            "STIFF": [1000, 2000, 3000],
            "bDAMP": True,
            "DAMP": [1, 2, 3]
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/SSPS", json=payload, headers=HEADERS)
print("POST (Point Spring):", resp.status_code, resp.json())

# ── POST: 솔리드(절점) 면스프링 → 탄성링크(다선형) 변환 ────────────
payload2 = {
    "Argument": {
        "CONVERT_TO": "ELASTIC_LINK",
        "GROUP_NAME": "B1",
        "NODE_ELEMS": {"KEYS": [56, 57, 58, 59, 60, 61, 62, 63]},
        "ELEMENT": {"TYPE": "SOLID_NODE"},
        "BOUNDARY": {"TYPE": "MULTI", "DIR": 7, "SUBGRADE": 5000, "PHU": 500, "LENGTH": 0.5}
    }
}
resp = requests.post(f"{BASE_URL}/ope/SSPS", json=payload2, headers=HEADERS)
print("POST (Elastic Link):", resp.status_code, resp.json())
```

---

## 8. `/ope/EDMP` — Change Property

> **기능:** 수축·크리프 계산에 필요한 부재의 명목크기(Notional Size of Member) 또는 체적표면비(Volume Surface Ratio)를 지정 또는 자동계산합니다.

### Input URI

```
{base url}/ope/EDMP
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "EDMP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "NODE_ELEMS": {
            "type": "object",
            "properties": { "KEYS": { "type": "array", "items": { "type": "integer" } } }
          },
          "TYPE": { "description": "TYPE", "type": "string", "enum": ["NSM", "VSR"] },
          "AUTO": { "description": "Auto Calculate", "type": "boolean" },
          "CODE": {
            "description": "CODE",
            "type": "string",
            "enum": ["Korean Standard", "CEB-FIP(1990)", "Japanese Standard", "Chinese Standard"]
          },
          "PARAMETER": { "description": "Parameter Value(a)", "type": "number" },
          "H_VS": { "description": "Change Property Value h(v/s)", "type": "number" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 대상 노드/요소 번호 | `"NODE_ELEMS"` | Object | — | **Required** |
| 1-1 | └ 번호 배열 (예: `[101, 102, 103]`) | `NODE_ELEMS.KEYS` | Array [Integer] | — | **Required** |
| 2 | 변경 방법 · 명목크기: `"NSM"` / 체적표면비: `"VSR"` | `"TYPE"` | String | `"NSM"` | Optional |
| 3 | 자동계산 여부 (체적표면비는 `false`만 가능) | `"AUTO"` | Boolean | `false` | Optional |
| 4 | 기준 코드 · 한국표준: `"Korean Standard"` / CEB-FIP(1990) / 일본표준 / 중국표준 (`AUTO=true`이고 `TYPE="NSM"`일 때만 사용) | `"CODE"` | String | `"Korean Standard"` | Optional |
| 5 | 파라미터 값(a) (`AUTO=false`일 때 필수) | `"PARAMETER"` | Number | — | **Required**(AUTO=false) |
| 6 | 변경값 · 명목크기: h / 체적표면비: v/s | `"H_VS"` | Number | — | **Required** |

### Request / Response JSON

**POST Request Body — 명목크기 자동계산**

```json
{
  "Argument": {
    "NODE_ELEMS": { "KEYS": [1, 2, 3] },
    "TYPE": "NSM",
    "AUTO": true,
    "CODE": "Korean Standard",
    "PARAMETER": 0.5
  }
}
```

**POST Request Body — 체적표면비 수동입력**

```json
{
  "Argument": {
    "NODE_ELEMS": { "KEYS": [1, 2, 3] },
    "TYPE": "VSR",
    "AUTO": false,
    "H_VS": 1.0
  }
}
```

**POST Response Body**

```json
{
  "EDMP": {
    "message": "Success"
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 명목크기(Notional Size) 자동계산 ─────────────────────────
payload = {
    "Argument": {
        "NODE_ELEMS": {"KEYS": [1, 2, 3]},
        "TYPE": "NSM",
        "AUTO": True,
        "CODE": "Korean Standard",
        "PARAMETER": 0.5
    }
}
resp = requests.post(f"{BASE_URL}/ope/EDMP", json=payload, headers=HEADERS)
print("POST (NSM):", resp.status_code, resp.json())

# ── POST: 체적표면비(V/S) 직접 입력 ─────────────────────────────────
payload2 = {
    "Argument": {
        "NODE_ELEMS": {"KEYS": [1, 2, 3]},
        "TYPE": "VSR",
        "AUTO": False,
        "H_VS": 1.0
    }
}
resp = requests.post(f"{BASE_URL}/ope/EDMP", json=payload2, headers=HEADERS)
print("POST (VSR):", resp.status_code, resp.json())
```

---

## 9. `/ope/STOR` — Story Calculation

> **기능:** 층(Story) 계산 시 지진/풍하중 우발편심(Accidental Eccentricity) 고려 여부와 값을 설정하고, 층별 계산 결과를 반환합니다.

### Input URI

```
{base url}/ope/STOR
```

### Active Methods

`POST`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "SEIS_ECC": { "INC_SEIS_ECC": false, "SEIS_ECC_VALUE": 5 },
    "WIND_ECC": { "INC_WIND_ECC": false, "WIND_ECC_VALUE": 15 }
  }
}
```

**POST Response Body**

```json
{
  "STOR": {
    "string": {
      "STORY_NAME": "string",
      "STORY_LEVEL": 0,
      "bFLOOR_DIAPHRAGM": false,
      "WIND_FLOOR_WIDTH_X": 0,
      "WIND_FLOOR_WIDTH_Y": 0,
      "WIND_CENTER_X": 0,
      "WIND_CENTER_Y": 0,
      "WIND_ECCENT_X": 0,
      "WIND_ECCENT_Y": 0,
      "SEIS_ACC_ECCENT_X": 0,
      "SEIS_ACC_ECCENT_Y": 0,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 0,
      "STORY_AREA_ITEMS": [{ "X": 0, "Y": 0, "Z": 0 }]
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 지진 우발편심 | `"SEIS_ECC"` | Object | — | **Required** |
| 1-1 | └ 지진 우발편심 포함 여부 | `SEIS_ECC.INC_SEIS_ECC` | Boolean | — | **Required** |
| 1-2 | └ 지진 우발편심 값(%) | `SEIS_ECC.SEIS_ECC_VALUE` | Number | — | **Required** |
| 2 | 풍하중 편심 | `"WIND_ECC"` | Object | — | **Required** |
| 2-1 | └ 풍하중 편심 포함 여부 | `WIND_ECC.INC_WIND_ECC` | Boolean | — | **Required** |
| 2-2 | └ 풍하중 편심 값(%) | `WIND_ECC.WIND_ECC_VALUE` | Number | — | **Required** |

응답의 각 층(`"string"`은 층 이름) 항목에는 층 레벨, 다이아프램 여부, 풍하중/지진 편심량, 비틀림증폭계수, 층 면적 좌표 목록(`STORY_AREA_ITEMS`)이 포함됩니다.

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 층 계산 옵션(우발편심) 설정 및 결과 조회 ─────────────────
payload = {
    "Argument": {
        "SEIS_ECC": {"INC_SEIS_ECC": True, "SEIS_ECC_VALUE": 5},
        "WIND_ECC": {"INC_WIND_ECC": True, "WIND_ECC_VALUE": 15}
    }
}
resp = requests.post(f"{BASE_URL}/ope/STOR", json=payload, headers=HEADERS)
stories = resp.json().get("STOR", {})
for name, info in stories.items():
    print(f"[{info['STORY_NAME']}] Level={info['STORY_LEVEL']}, Diaphragm={info['bFLOOR_DIAPHRAGM']}")
```

---

## 10. `/ope/STORY_PARAM` — Story Check Parameter

> **기능:** 층간변위비·비틀림 등 층 검토에 사용할 국가별 기준코드(Country Code)를 설정하거나 조회합니다.

### Input URI

```
{base url}/ope/STORY_PARAM
```

### Active Methods

`GET` · `POST`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "COUNTRY_CODE": "NTC2012"
  }
}
```

**GET / POST Response Body**

```json
{
  "STORY_PARAM": {
    "COUNTRY_CODE": "NTC2012"
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 국가 기준코드 설정 · `"NTC2012"` / `"NTC2008"` / `"KBC2009"` / `"NSR-10"` / `"NTC2018"` / `"NTCS2020"` / `"IS1893(2016)"` / `"IS16700(2023)"` | `"COUNTRY_CODE"` | String | — | **Required** |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 층 검토 기준코드 설정 ────────────────────────────────────
payload = {"Argument": {"COUNTRY_CODE": "KBC2009"}}
resp = requests.post(f"{BASE_URL}/ope/STORY_PARAM", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 현재 설정된 기준코드 조회 ─────────────────────────────────
resp = requests.get(f"{BASE_URL}/ope/STORY_PARAM", headers=HEADERS)
print("GET:", resp.json())
```

---

## 11. `/ope/STORY_IRR_PARAM` — Story Irregularity Check Parameter

> **기능:** 층 불규칙성(비틀림·강성·강도) 검토를 위한 국가 기준코드, 층간변위 산정방법, 층강성 산정방법, 지진거동계수를 설정 또는 조회합니다.

### Input URI

```
{base url}/ope/STORY_IRR_PARAM
```

### Active Methods

`GET` · `POST`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "COUNTRY_CODE": "NSR-10",
    "STORY_DRIFT_METHOD": "Max.DriftofOuterExtremePoints",
    "STORY_STIFFNESS_METHOD": "1/StoryDriftRatio",
    "SEISMIC_BEHAVIOR_FACTOR": "3orbelow"
  }
}
```

**GET / POST Response Body**

```json
{
  "STORY_IRR_PARAM": {
    "COUNTRY_CODE": "NSR-10",
    "STORY_DRIFT_METHOD": "Max.DriftofOuterExtremePoints",
    "STORY_STIFFNESS_METHOD": "1/StoryDriftRatio",
    "SEISMIC_BEHAVIOR_FACTOR": "3orbelow"
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 국가 기준코드 · `"NTC2018"` / `"NTC2012"` / `"NTC2008"` / `"KBC2009"` / `"NSR-10"` / `"NTCS2020"` / `"NTCS2023"` / `"NSCP2015"` / `"IS1893(2016)"` / `"IS16700(2023)"` | `"COUNTRY_CODE"` | String | — | **Required** |
| 2 | 층간변위 산정방법 · 질량중심 변위: `"Drift at the Center of Mass"` / 최외곽점 최대변위: `"Max. Drift of Outer Extreme Points"` / 전체 수직요소 최대변위: `"Max. Drift of All Vertical Elements"` | `"STORY_DRIFT_METHOD"` | String | — | **Required** |
| 3 | 층강성 산정방법 · `"1 / Story Drift Ratio"` / `"Story Shear / Story Drift"` | `"STORY_STIFFNESS_METHOD"` | String | — | **Required** |
| 4 | 지진거동계수(`COUNTRY_CODE`가 `"NTCS2023"` 또는 `"NTCS2020"`일 때만 필요) · `"4"` / `"3 or below"` | `"SEISMIC_BEHAVIOR_FACTOR"` | String | — | 조건부 **Required** |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 층 불규칙성 검토 파라미터 설정 ───────────────────────────
payload = {
    "Argument": {
        "COUNTRY_CODE": "NTCS2023",
        "STORY_DRIFT_METHOD": "Max.DriftofOuterExtremePoints",
        "STORY_STIFFNESS_METHOD": "1/StoryDriftRatio",
        "SEISMIC_BEHAVIOR_FACTOR": "3orbelow"   # NTCS2023이므로 필수
    }
}
resp = requests.post(f"{BASE_URL}/ope/STORY_IRR_PARAM", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 현재 설정 조회 ────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/ope/STORY_IRR_PARAM", headers=HEADERS)
print("GET:", resp.json())
```

---

## 12. `/ope/STORPROP` — Story Properties

> **기능:** 층별 중량, 표고, 재하높이, 재하폭(Bx/By) 등 층 속성 계산 결과를 지정한 단위·형식으로 조회합니다.

### Input URI

```
{base url}/ope/STORPROP
```

### Active Methods

`POST`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "FORCE_UNIT": "KN",
    "LENGTH_UNIT": "M",
    "FORMAT": "Default",
    "PLACE": 4
  }
}
```

**POST Response Body**

```json
{
  "STORYPROP": {
    "FORCE": "KN",
    "LENGTH": "M",
    "HEAD": ["Story", "Weight", "Elev.", "LoadedH", "LoadedBx", "LoadedBy"],
    "DATA": [
      { "STORY": "Roof", "WEIGHT": "3256.1530", "ELEV": "50.0000", "LOADED_H": "2.0000", "LOADED_BX": "29.1000", "LOADED_BY": "36.0000" },
      { "STORY": "12F", "WEIGHT": "3984.8264", "ELEV": "46.0000", "LOADED_H": "4.0000", "LOADED_BX": "29.1000", "LOADED_BY": "36.0000" },
      { "STORY": "G.L.", "WEIGHT": "0.0000", "ELEV": "0.0000", "LOADED_H": "2.5000", "LOADED_BX": "27.6000", "LOADED_BY": "36.0000" }
    ]
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 힘 단위 · `"N"`/`"KN"`/`"KGF"`/`"TONF"`/`"LBF"`/`"KIPS"` | `"FORCE_UNIT"` | String | System | Optional |
| 2 | 길이 단위 · `"M"`/`"CM"`/`"MM"`/`"FT"`/`"IN"` | `"LENGTH_UNIT"` | String | System | Optional |
| 3 | 응답 숫자 형식 · `"Fixed"`/`"Scientific"` | `"FORMAT"` | String | System | Optional |
| 4 | 응답 숫자 소수 자릿수(0~15) | `"PLACE"` | String | System | Optional |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 층 속성 결과 조회(KN, M, 소수점 4자리) ───────────────────
payload = {
    "Argument": {
        "FORCE_UNIT": "KN",
        "LENGTH_UNIT": "M",
        "FORMAT": "Default",
        "PLACE": 4
    }
}
resp = requests.post(f"{BASE_URL}/ope/STORPROP", json=payload, headers=HEADERS)
result = resp.json().get("STORYPROP", {})
for row in result.get("DATA", []):
    print(f"{row['STORY']}: 중량={row['WEIGHT']}{result['FORCE']}, 표고={row['ELEV']}{result['LENGTH']}")
```

---

## 13. `/ope/MEMB` — Member Assignment

> **기능:** 여러 요소를 하나의 부재(Member)로 자동/수동 배정합니다. 설계 검토 시 부재 단위 검토를 위해 사용됩니다.

### Input URI

```
{base url}/ope/MEMB
```

### Active Methods

`POST`

### Request / Response JSON

**POST Request Body — 수동 배정**

```json
{
  "Argument": {
    "ASSIGN_TYPE": "MANUAL",
    "SELECTION_TYPE": "SELECTION",
    "ELEM_LIST": [640, 692],
    "ALLOW_SINGLE": false
  }
}
```

**POST Request Body — 자동 배정(전체 요소)**

```json
{
  "Argument": {
    "ASSIGN_TYPE": "AUTO",
    "SELECTION_TYPE": "ALL",
    "ALLOW_SINGLE": true
  }
}
```

**POST Response Body**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [640, 692],
      "bREVERSE": false
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 배정 타입 · 수동: `"MANUAL"` / 자동: `"AUTO"` | `"ASSIGN_TYPE"` | String | — | **Required** |
| 2 | 선택 타입 · 전체: `"ALL"` / 선택: `"SELECTION"` | `"SELECTION_TYPE"` | String | — | **Required** |
| 3 | 대상 요소 목록 (`SELECTION_TYPE="ALL"`이면 무시됨) | `"ELEM_LIST"` | Array | — | 조건부 **Required** |
| 4 | 단일요소 부재 허용 여부 | `"ALLOW_SINGLE"` | Boolean | — | **Required** |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 특정 요소들을 하나의 부재로 수동 배정 ────────────────────
payload = {
    "Argument": {
        "ASSIGN_TYPE": "MANUAL",
        "SELECTION_TYPE": "SELECTION",
        "ELEM_LIST": [640, 692],
        "ALLOW_SINGLE": False
    }
}
resp = requests.post(f"{BASE_URL}/ope/MEMB", json=payload, headers=HEADERS)
print("POST (수동):", resp.status_code, resp.json())

# ── POST: 전체 모델 자동 부재 배정 ─────────────────────────────────
payload2 = {
    "Argument": {
        "ASSIGN_TYPE": "AUTO",
        "SELECTION_TYPE": "ALL",
        "ALLOW_SINGLE": True
    }
}
resp = requests.post(f"{BASE_URL}/ope/MEMB", json=payload2, headers=HEADERS)
print("POST (자동):", resp.status_code, resp.json())
```

---

## 14. `/ope/GUSTFACTOR` — Gust Factor Calculator

> **기능:** KDS 41 12:2022 풍하중 기준에 따라 강성/유연 구조물의 거스트영향계수(Gust Effect Factor)를 계산합니다.

### Input URI

```
{base url}/ope/GUSTFACTOR
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "description": "GUSTFACTOR request item. STRUCTURE_TYPE controls whether RIGID_PARAM or FLEXIBLE_PARAM is required.",
      "required": ["WIND_CODE", "STRUCTURE_TYPE"],
      "properties": {
        "WIND_CODE": { "type": "string", "enum": ["KDS(41-12:2022)"] },
        "STRUCTURE_TYPE": { "type": "string", "enum": ["RIGID", "FLEXIBLE"], "description": "Structure type classification." },
        "RIGID_PARAM": {
          "type": "object",
          "required": ["EXP_CATEGORY", "ROOF_HEIGHT", "BREADTH_X", "BREADTH_Y"],
          "properties": {
            "EXP_CATEGORY": { "type": "string", "description": "Exposure category." },
            "ROOF_HEIGHT": { "type": "number", "minimum": 0, "description": "Roof height." },
            "BREADTH_X": { "type": "number", "minimum": 0, "description": "Plan breadth in global X direction." },
            "BREADTH_Y": { "type": "number", "minimum": 0, "description": "Plan breadth in global Y direction." }
          }
        },
        "FLEXIBLE_PARAM": {
          "type": "object",
          "required": [
            "EXP_CATEGORY", "BASIC_WIND_SPEED", "IMPORTANCE_FACTOR", "DIRECTION_FACTOR_X", "DIRECTION_FACTOR_Y",
            "BREADTH_X", "BREADTH_Y", "STORY_HEIGHT_MAX", "FREQUENCY_X", "FREQUENCY_Y", "DAMPING",
            "TOTAL_MASS", "MX", "MY", "VIBRATION"
          ],
          "properties": {
            "EXP_CATEGORY": { "type": "string", "description": "Exposure category." },
            "BASIC_WIND_SPEED": { "type": "number", "minimum": 0, "description": "Basic wind speed." },
            "IMPORTANCE_FACTOR": { "type": "number", "minimum": 0, "description": "Importance factor." },
            "TOPOGRAPHIC_EFFECT": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Whether to use topographic effect." },
                "KZT": { "type": "number", "minimum": 0, "description": "Topographic factor Kzt. Required only if OPT_USE=true." }
              },
              "description": "Optional. If omitted, treated as OPT_USE=false."
            },
            "DIRECTION_FACTOR_X": { "type": "number", "minimum": 0, "description": "Direction factor in X." },
            "DIRECTION_FACTOR_Y": { "type": "number", "minimum": 0, "description": "Direction factor in Y." },
            "BREADTH_X": { "type": "number", "minimum": 0, "description": "Plan breadth in global X direction." },
            "BREADTH_Y": { "type": "number", "minimum": 0, "description": "Plan breadth in global Y direction." },
            "STORY_HEIGHT_MAX": { "type": "number", "minimum": 0, "description": "Maximum story or roof height used for flexible response." },
            "FREQUENCY_X": { "type": "number", "minimum": 0, "description": "Fundamental frequency in X." },
            "FREQUENCY_Y": { "type": "number", "minimum": 0, "description": "Fundamental frequency in Y." },
            "DAMPING": { "type": "number", "minimum": 0, "description": "Damping ratio, for example 0.03." },
            "TOTAL_MASS": { "type": "number", "minimum": 0, "description": "Total mass." },
            "MX": { "type": "number", "minimum": 0, "description": "Mass term in X." },
            "MY": { "type": "number", "minimum": 0, "description": "Mass term in Y." },
            "VIBRATION": { "type": "number", "minimum": 0, "description": "Vibration-related factor or flag." }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 풍하중 기준코드 · `"KDS(41-12:2022)"` | `"WIND_CODE"` | String (enum) | — | **Required** |
| 2 | 구조물 타입 · 강성: `"RIGID"` / 유연: `"FLEXIBLE"` | `"STRUCTURE_TYPE"` | String (enum) | — | **Required** |
| **STRUCTURE_TYPE = "RIGID"인 경우** |
| 3 | 강성구조 파라미터 | `"RIGID_PARAM"` | Object | — | 조건부 **Required** |
| 3-1 | └ 지표면 노출유형 | `RIGID_PARAM.EXP_CATEGORY` | String | — | **Required** |
| 3-2 | └ 지붕높이 | `RIGID_PARAM.ROOF_HEIGHT` | Number (≥0) | — | **Required** |
| 3-3 | └ 평면 폭(X방향) | `RIGID_PARAM.BREADTH_X` | Number (≥0) | — | **Required** |
| 3-4 | └ 평면 폭(Y방향) | `RIGID_PARAM.BREADTH_Y` | Number (≥0) | — | **Required** |
| **STRUCTURE_TYPE = "FLEXIBLE"인 경우** |
| 4 | 유연구조 파라미터 | `"FLEXIBLE_PARAM"` | Object | — | 조건부 **Required** |
| 4-1 | └ 지표면 노출유형 | `FLEXIBLE_PARAM.EXP_CATEGORY` | String | — | **Required** |
| 4-2 | └ 기본풍속(m/s) | `FLEXIBLE_PARAM.BASIC_WIND_SPEED` | Number (≥0) | — | **Required** |
| 4-3 | └ 중요도계수 | `FLEXIBLE_PARAM.IMPORTANCE_FACTOR` | Number (≥0) | — | **Required** |
| 4-4 | └ 지형효과 고려 옵션 | `FLEXIBLE_PARAM.TOPOGRAPHIC_EFFECT` | Object | — | Optional (생략 시 미사용) |
| 4-4-a | 　└ 사용 여부 | `TOPOGRAPHIC_EFFECT.OPT_USE` | Boolean | `false` | **Required** |
| 4-4-b | 　└ 지형계수 Kzt (`OPT_USE=true`일 때 필수) | `TOPOGRAPHIC_EFFECT.KZT` | Number (≥0) | — | 조건부 **Required** |
| 4-5 | └ 방향계수(X) | `FLEXIBLE_PARAM.DIRECTION_FACTOR_X` | Number (≥0) | — | **Required** |
| 4-6 | └ 방향계수(Y) | `FLEXIBLE_PARAM.DIRECTION_FACTOR_Y` | Number (≥0) | — | **Required** |
| 4-7 | └ 평면 폭(X방향) | `FLEXIBLE_PARAM.BREADTH_X` | Number (≥0) | — | **Required** |
| 4-8 | └ 평면 폭(Y방향) | `FLEXIBLE_PARAM.BREADTH_Y` | Number (≥0) | — | **Required** |
| 4-9 | └ 최대 층고/지붕높이 | `FLEXIBLE_PARAM.STORY_HEIGHT_MAX` | Number (≥0) | — | **Required** |
| 4-10 | └ 고유진동수(X, Hz) | `FLEXIBLE_PARAM.FREQUENCY_X` | Number (≥0) | — | **Required** |
| 4-11 | └ 고유진동수(Y, Hz) | `FLEXIBLE_PARAM.FREQUENCY_Y` | Number (≥0) | — | **Required** |
| 4-12 | └ 감쇠비 | `FLEXIBLE_PARAM.DAMPING` | Number (≥0) | — | **Required** |
| 4-13 | └ 총 질량 | `FLEXIBLE_PARAM.TOTAL_MASS` | Number (≥0) | — | **Required** |
| 4-14 | └ 질량항(X) | `FLEXIBLE_PARAM.MX` | Number (≥0) | — | **Required** |
| 4-15 | └ 질량항(Y) | `FLEXIBLE_PARAM.MY` | Number (≥0) | — | **Required** |
| 4-16 | └ 진동 관련 계수 | `FLEXIBLE_PARAM.VIBRATION` | Number (≥0) | — | **Required** |

### Request / Response JSON

**POST Request Body — 유연구조**

```json
{
  "Argument": {
    "WIND_CODE": "KDS(41-12:2022)",
    "STRUCTURE_TYPE": "FLEXIBLE",
    "FLEXIBLE_PARAM": {
      "EXP_CATEGORY": "B",
      "BASIC_WIND_SPEED": 38,
      "IMPORTANCE_FACTOR": 1,
      "TOPOGRAPHIC_EFFECT": { "OPT_USE": true, "KZT": 1.1 },
      "DIRECTION_FACTOR_X": 0.85,
      "DIRECTION_FACTOR_Y": 0.85,
      "BREADTH_X": 32,
      "BREADTH_Y": 24,
      "STORY_HEIGHT_MAX": 72,
      "FREQUENCY_X": 0.42,
      "FREQUENCY_Y": 0.48,
      "DAMPING": 0.03,
      "TOTAL_MASS": 85000,
      "MX": 82000,
      "MY": 80500,
      "VIBRATION": 1
    }
  }
}
```

**POST Request Body — 강성구조**

```json
{
  "Argument": {
    "WIND_CODE": "KDS(41-12:2022)",
    "STRUCTURE_TYPE": "RIGID",
    "RIGID_PARAM": {
      "EXP_CATEGORY": "C",
      "ROOF_HEIGHT": 30,
      "BREADTH_X": 20,
      "BREADTH_Y": 15
    }
  }
}
```

**POST Response Body**

```json
{
  "OPE_GUSTFACTOR_RESPONSE": {
    "GUST_FACTOR_X": 1.7400999942907864,
    "GUST_FACTOR_Y": 1.7513941589768178
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 유연구조 거스트영향계수 계산 ─────────────────────────────
payload = {
    "Argument": {
        "WIND_CODE": "KDS(41-12:2022)",
        "STRUCTURE_TYPE": "FLEXIBLE",
        "FLEXIBLE_PARAM": {
            "EXP_CATEGORY": "B",
            "BASIC_WIND_SPEED": 38,
            "IMPORTANCE_FACTOR": 1,
            "TOPOGRAPHIC_EFFECT": {"OPT_USE": True, "KZT": 1.1},
            "DIRECTION_FACTOR_X": 0.85,
            "DIRECTION_FACTOR_Y": 0.85,
            "BREADTH_X": 32,
            "BREADTH_Y": 24,
            "STORY_HEIGHT_MAX": 72,
            "FREQUENCY_X": 0.42,
            "FREQUENCY_Y": 0.48,
            "DAMPING": 0.03,
            "TOTAL_MASS": 85000,
            "MX": 82000,
            "MY": 80500,
            "VIBRATION": 1
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/GUSTFACTOR", json=payload, headers=HEADERS)
result = resp.json().get("OPE_GUSTFACTOR_RESPONSE", {})
print(f"거스트영향계수 Gx = {result['GUST_FACTOR_X']:.4f}")
print(f"거스트영향계수 Gy = {result['GUST_FACTOR_Y']:.4f}")
```

---

## 15. `/ope/LCOM-GEN` — Load Combination (General) – KDS:2022 / AIK-SRC2K

> **기능:** 설계기준(콘크리트/강재/SRC)에 따라 응답스펙트럼 축계수, 풍하중 조합, 직교효과, 특별지진하중·수직지진력·지하구조물하중 등의 옵션을 지정하여 설계하중조합을 자동으로 생성합니다. 본 엔드포인트는 POST 전용이며, 기존 설계하중조합에 추가(ADD)하거나 전체를 대체(REPLACE)하는 방식으로 동작합니다. 동일 엔드포인트는 `DGNCODE: "AIK-SRC2K"`를 지정하는 더 단순한 스키마(`OPTION` + `DGNCODE` + `RS_SCALE_FACTOR`)도 지원하며 이는 본 문서 하단의 "LCOM-GEN/SRC AIK-SRC2K 변형 스키마" 절에서 다룹니다. 본 절은 `CODE_SELECTION`으로 CONCRETE/STEEL/SRC 바디를 선택하는 KDS:2022 변형만을 다룹니다.

### Input URI

```
{base url}/ope/LCOM-GEN
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "description": "LCOM-GEN item for KDS 2022. Body structure is selected by CODE_SELECTION.",
      "oneOf": [
        {
          "type": "object",
          "required": ["OPTION", "CODE_SELECTION", "DGNCODE", "RS_SCALE_FACTOR", "ORTHO_EFFECT", "ADDITIONAL_LOAD", "CS_ANALYSIS", "PRESTRESS_LOSS"],
          "properties": {
            "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
            "ADD_ENVELOPE": { "type": "boolean", "default": true, "description": "Add envelope option for LCOM-GEN" },
            "CODE_SELECTION": { "type": "string", "const": "CONCRETE", "description": "CONCRETE design code body" },
            "DGNCODE": { "type": "string", "const": "KDS 41 20 : 2022", "default": "KDS 41 20 : 2022", "description": "Concrete design code value. General group key: KDS_2022" },
            "RS_SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "WIND_LOAD_COMB": {
              "type": "object",
              "required": ["PARAMETERS"],
              "properties": {
                "PARAMETERS": {
                  "type": "array",
                  "description": "List of wind load combination sets",
                  "items": {
                    "type": "object",
                    "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                    "properties": {
                      "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                      "WIND_LOAD_CASE": {
                        "type": "object",
                        "properties": {
                          "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                          "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                          "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                        }
                      },
                      "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                      "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                    }
                  }
                },
                "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
              }
            },
            "ORTHO_EFFECT": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
                "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
                "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
              }
            },
            "ADDITIONAL_LOAD": {
              "type": "object",
              "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
              "properties": {
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Special Seismic Load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      }
                    }
                  }
                },
                "VERTICAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Vertical Seismic Forces" },
                    "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
                  }
                }
              }
            },
            "UNDERGROUND_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "description": "for Underground Load" },
                "SCALE_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                },
                "LOAD_CASE_LIST": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                      "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                      "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                      "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                    }
                  }
                },
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "Whether to use special load for underground load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      },
                      "description": "Over-strength factors for underground special load"
                    }
                  }
                }
              }
            },
            "CS_ANALYSIS": { "type": "boolean" },
            "PRESTRESS_LOSS": { "type": "boolean" }
          }
        },
        {
          "type": "object",
          "required": ["OPTION", "CODE_SELECTION", "DGNCODE", "RS_SCALE_FACTOR", "ORTHO_EFFECT", "ADDITIONAL_LOAD"],
          "properties": {
            "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
            "ADD_ENVELOPE": { "type": "boolean", "default": true, "description": "Add envelope option for LCOM-GEN" },
            "CODE_SELECTION": { "type": "string", "const": "STEEL", "description": "STEEL design code body" },
            "DGNCODE": { "type": "string", "const": "KDS 41 30 : 2022", "default": "KDS 41 30 : 2022", "description": "Steel design code value. General group key: KDS_2022" },
            "RS_SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "WIND_LOAD_COMB": {
              "type": "object",
              "required": ["PARAMETERS"],
              "properties": {
                "PARAMETERS": {
                  "type": "array",
                  "description": "List of wind load combination sets",
                  "items": {
                    "type": "object",
                    "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                    "properties": {
                      "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                      "WIND_LOAD_CASE": {
                        "type": "object",
                        "properties": {
                          "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                          "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                          "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                        }
                      },
                      "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                      "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                    }
                  }
                },
                "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
              }
            },
            "ORTHO_EFFECT": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
                "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
                "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
              }
            },
            "ADDITIONAL_LOAD": {
              "type": "object",
              "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
              "properties": {
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Special Seismic Load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      }
                    }
                  }
                },
                "VERTICAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Vertical Seismic Forces" },
                    "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
                  }
                }
              }
            },
            "UNDERGROUND_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "description": "for Underground Load" },
                "SCALE_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                },
                "LOAD_CASE_LIST": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                      "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                      "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                      "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                    }
                  }
                },
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "Whether to use special load for underground load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      },
                      "description": "Over-strength factors for underground special load"
                    }
                  }
                }
              }
            }
          }
        },
        {
          "type": "object",
          "required": ["OPTION", "CODE_SELECTION", "DGNCODE", "RS_SCALE_FACTOR", "WIND_LOAD_COMB", "ORTHO_EFFECT", "ADDITIONAL_LOAD", "UNDERGROUND_LOAD"],
          "properties": {
            "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
            "ADD_ENVELOPE": { "type": "boolean", "default": true, "description": "Add envelope option for LCOM-GEN" },
            "CODE_SELECTION": { "type": "string", "const": "SRC", "description": "SRC design code body" },
            "DGNCODE": { "type": "string", "const": "KDS 41 SRC : 2022", "default": "KDS 41 SRC : 2022", "description": "SRC design code value. General group key: KDS_2022" },
            "RS_SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "WIND_LOAD_COMB": {
              "type": "object",
              "required": ["PARAMETERS"],
              "properties": {
                "PARAMETERS": {
                  "type": "array",
                  "description": "List of wind load combination sets",
                  "items": {
                    "type": "object",
                    "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                    "properties": {
                      "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                      "WIND_LOAD_CASE": {
                        "type": "object",
                        "properties": {
                          "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                          "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                          "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                        }
                      },
                      "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                      "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                    }
                  }
                },
                "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
              }
            },
            "ORTHO_EFFECT": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
                "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
                "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
              }
            },
            "ADDITIONAL_LOAD": {
              "type": "object",
              "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
              "properties": {
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Special Seismic Load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      }
                    }
                  }
                },
                "VERTICAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Vertical Seismic Forces" },
                    "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
                  }
                }
              }
            },
            "UNDERGROUND_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "description": "for Underground Load" },
                "SCALE_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                },
                "LOAD_CASE_LIST": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                      "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                      "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                      "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                    }
                  }
                },
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "Whether to use special load for underground load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      },
                      "description": "Over-strength factors for underground special load"
                    }
                  }
                }
              }
            }
          }
        }
      ]
    }
  }
}
```

### Parameters

`Argument`는 `CODE_SELECTION` 값(`CONCRETE` / `STEEL` / `SRC`)에 따라 서로 다른 바디 구조를 갖는 `oneOf` 스키마입니다. 세 바디는 대부분의 필드를 공유하며, 차이는 표에 명시되어 있습니다(`DGNCODE`의 const 값, `CS_ANALYSIS`/`PRESTRESS_LOSS` 필드 유무, `WIND_LOAD_COMB`/`UNDERGROUND_LOAD`의 필수 여부).

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|---|---|---|---|---|---|
| 1 | OPTION – 기존 조합에 추가할지 전체 대체할지 | `OPTION` | string (enum) | `ADD`, `REPLACE` | 필수 |
| 2 | Add envelope option for LCOM-GEN (CONCRETE/STEEL 바디에만 존재) | `ADD_ENVELOPE` | boolean | 기본값 `true` | 선택 |
| 3 | 설계 카테고리 선택 – 바디 구조 분기 키 | `CODE_SELECTION` | string (const) | `CONCRETE` \| `STEEL` \| `SRC` | 필수 |
| 4 | 설계기준 코드 값. `CODE_SELECTION="CONCRETE"`일 때 const/기본값 `"KDS 41 20 : 2022"` | `DGNCODE` | string (const) | `KDS 41 20 : 2022` | 필수 (CONCRETE 바디에서) |
| 4' | 설계기준 코드 값. `CODE_SELECTION="STEEL"`일 때 const/기본값 `"KDS 41 30 : 2022"` | `DGNCODE` | string (const) | `KDS 41 30 : 2022` | 필수 (STEEL 바디에서) |
| 4'' | 설계기준 코드 값. `CODE_SELECTION="SRC"`일 때 const/기본값 `"KDS 41 SRC : 2022"` | `DGNCODE` | string (const) | `KDS 41 SRC : 2022` | 필수 (SRC 바디에서) |
| 5 | 응답스펙트럼 하중조합 목록 | `RS_SCALE_FACTOR` | array [object] | - | 필수 (세 바디 모두) |
| 5-1 | 하중 케이스명 (정적: `NAME(ST)`, 응답스펙트럼: `NAME(RS)`) | `RS_SCALE_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 5-2 | 축계수 | `RS_SCALE_FACTOR[].FACTOR` | number | - | 필수 |
| 6 | 풍하중 조합 세트. SRC 바디에서는 `WIND_LOAD_COMB` 자체가 필수, CONCRETE/STEEL 바디에서는 선택 | `WIND_LOAD_COMB` | object | - | SRC: 필수 / CONCRETE·STEEL: 선택 |
| 6-1 | 풍하중 조합 세트 목록 | `WIND_LOAD_COMB.PARAMETERS` | array [object] | - | 필수 (WIND_LOAD_COMB 사용 시) |
| 6-1-a | 풍하중 그룹 | `WIND_LOAD_COMB.PARAMETERS[].BUILDING_TYPE` | string (enum) | `MIDDLE`, `HIGH` | 필수 |
| 6-1-b | 풍하중 방향별 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE` | object | - | 필수 |
| 6-1-b-1 | 순풍(Along) 방향 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ALONG` | string | - | 선택 |
| 6-1-b-2 | 횡풍(Across) 방향 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ACROSS` | string | - | 선택 |
| 6-1-b-3 | 비틀림(Torsion) 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.TORSION` | string | - | 선택 |
| 6-1-c | 거스트 계수(GD) | `WIND_LOAD_COMB.PARAMETERS[].GUST_FACTOR` | number | 최소값 0 | 선택 |
| 6-1-d | Kappa 계수 | `WIND_LOAD_COMB.PARAMETERS[].KAPPA_FACTOR` | number | 최소값 0 | 선택 |
| 6-2 | 비틀림 풍하중 방향 | `WIND_LOAD_COMB.TORSION_DIR` | string (enum) | `BOTH`, `POSITIVE`, `NEGATIVE` (기본값 `BOTH`) | 선택 |
| 7 | 직교효과 고려 옵션 | `ORTHO_EFFECT` | object | - | 필수 (세 바디 모두) |
| 7-1 | 직교효과 고려 여부 | `ORTHO_EFFECT.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 7-2 | 직교효과 방식 – `ORTHO_EFFECT.OPT_USE`가 `true`일 때 필수 | `ORTHO_EFFECT.TYPE` | string (enum) | `100_30`, `SRSS` | 조건부 필수 |
| 7-3 | 직교 하중케이스 쌍 (Load Case1, Load Case2) – `ORTHO_EFFECT.OPT_USE`가 `true`일 때 필수 | `ORTHO_EFFECT.LOAD_GROUP` | array [string] (길이 2 고정, `minItems`/`maxItems`=2) | - | 조건부 필수 |
| 8 | 추가 하중 옵션 컨테이너 | `ADDITIONAL_LOAD` | object | - | 필수 (세 바디 모두) |
| 8-1 | 특별지진하중 옵션 | `ADDITIONAL_LOAD.SPECIAL_LOAD` | object | - | 필수 |
| 8-1-a | 특별지진하중 사용 여부 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | - | 필수 |
| 8-1-b | 수직하중계수 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 8-1-c | Sds – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.SDS` | number | 최소값 0 | 조건부 필수 |
| 8-1-d | 초과강도계수 목록 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 조건부 필수 |
| 8-1-d-1 | 하중 케이스명 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 8-1-d-2 | 축계수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 필수 |
| 8-2 | 수직지진력 옵션 | `ADDITIONAL_LOAD.VERTICAL_LOAD` | object | - | 필수 |
| 8-2-a | 수직지진력 고려 여부 | `ADDITIONAL_LOAD.VERTICAL_LOAD.OPT_USE` | boolean | - | 필수 |
| 8-2-b | 수직력 계수 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.VERTICAL_LOAD.FORCE_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 9 | 지하구조물 하중 옵션. SRC 바디에서는 `UNDERGROUND_LOAD` 자체가 필수, CONCRETE/STEEL 바디에서는 `ADDITIONAL_LOAD`의 하위가 아닌 별도 최상위 옵션(선택) | `UNDERGROUND_LOAD` | object | - | SRC: 필수 / CONCRETE·STEEL: 선택 |
| 9-1 | 지하구조물 하중 사용 여부 | `UNDERGROUND_LOAD.OPT_USE` | boolean | - | 필수 (UNDERGROUND_LOAD 사용 시) |
| 9-2 | 지하구조물 하중 축계수 목록 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SCALE_FACTOR` | array [object] | - | 조건부 필수 |
| 9-2-a | 하중 케이스명 | `UNDERGROUND_LOAD.SCALE_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 9-2-b | 축계수 | `UNDERGROUND_LOAD.SCALE_FACTOR[].FACTOR` | number | - | 필수 |
| 9-3 | 지진 하중케이스 목록 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.LOAD_CASE_LIST` | array [object] | - | 조건부 필수 |
| 9-3-a | 지진 하중케이스명 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE` | string | - | 필수 |
| 9-3-b | 지진 하중케이스 방향 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].DIRECTION` | string (enum) | `POSITIVE`, `NEGATIVE` | 필수 |
| 9-3-c | 토압 하중케이스 – 지진 성분 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_SEISMIC` | array [string] | - | 필수 |
| 9-3-d | 토압 하중케이스 – 정적 성분 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_STATIC` | array [string] | - | 필수 |
| 9-4 | 지하구조물 특별하중 사용 옵션 – `UNDERGROUND_LOAD` 내부, 최상위 `SPECIAL_LOAD`와 별개 | `UNDERGROUND_LOAD.SPECIAL_LOAD` | object | - | 선택 |
| 9-4-a | 지하구조물 특별하중 사용 여부 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | - | 필수 |
| 9-4-b | 수직하중계수 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 9-4-c | Sds – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.SDS` | number | 최소값 0 | 조건부 필수 |
| 9-4-d | 지하구조물 특별하중 초과강도계수 목록 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 조건부 필수 |
| 9-4-d-1 | 하중 케이스명 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 9-4-d-2 | 축계수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 필수 |
| 10 | 시공단계 해석결과 반영 여부 (CONCRETE 바디에만 존재) | `CS_ANALYSIS` | boolean | - | 필수 (CONCRETE 바디에서) |
| 11 | 프리스트레스 손실 반영 여부 (CONCRETE 바디에만 존재) | `PRESTRESS_LOSS` | boolean | - | 필수 (CONCRETE 바디에서) |

> **참고 – 바디별 required 차이 요약**
> - `CODE_SELECTION="CONCRETE"`: `OPTION`, `CODE_SELECTION`, `DGNCODE`, `RS_SCALE_FACTOR`, `ORTHO_EFFECT`, `ADDITIONAL_LOAD`, `CS_ANALYSIS`, `PRESTRESS_LOSS`가 required (`WIND_LOAD_COMB`, `UNDERGROUND_LOAD`는 선택).
> - `CODE_SELECTION="STEEL"`: `OPTION`, `CODE_SELECTION`, `DGNCODE`, `RS_SCALE_FACTOR`, `ORTHO_EFFECT`, `ADDITIONAL_LOAD`가 required (`WIND_LOAD_COMB`, `UNDERGROUND_LOAD`, `CS_ANALYSIS`, `PRESTRESS_LOSS`는 존재하지 않거나 선택).
> - `CODE_SELECTION="SRC"`: `OPTION`, `CODE_SELECTION`, `DGNCODE`, `RS_SCALE_FACTOR`, `WIND_LOAD_COMB`, `ORTHO_EFFECT`, `ADDITIONAL_LOAD`, `UNDERGROUND_LOAD`가 required (`CS_ANALYSIS`, `PRESTRESS_LOSS`는 존재하지 않음).

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "ADD_ENVELOPE": true,
    "CODE_SELECTION": "CONCRETE",
    "DGNCODE": "KDS 41 20 : 2022",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1 }
    ],
    "WIND_LOAD_COMB": {
      "PARAMETERS": [
        {
          "BUILDING_TYPE": "HIGH",
          "WIND_LOAD_CASE": { "ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)" },
          "GUST_FACTOR": 2.2,
          "KAPPA_FACTOR": 0.55
        }
      ],
      "TORSION_DIR": "BOTH"
    },
    "ORTHO_EFFECT": {
      "OPT_USE": true,
      "TYPE": "100_30",
      "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
    },
    "ADDITIONAL_LOAD": {
      "SPECIAL_LOAD": {
        "OPT_USE": true,
        "VERTICAL_LOAD_FACTOR": 0.2,
        "SDS": 0.5,
        "OVER_STRENGTH_FACTOR": [
          { "LOAD_CASE": "RX(RS)", "FACTOR": 2.5 },
          { "LOAD_CASE": "RY(RS)", "FACTOR": 2.5 }
        ]
      },
      "VERTICAL_LOAD": { "OPT_USE": true, "FORCE_FACTOR": 0.2 }
    },
    "UNDERGROUND_LOAD": { "OPT_USE": false },
    "CS_ANALYSIS": false,
    "PRESTRESS_LOSS": false
  }
}
```

**POST Response Body**

```json
{
  "message": "LCOM-GEN generated successfully.",
  "Argument": {
    "OPTION": "ADD",
    "CODE_SELECTION": "CONCRETE",
    "DGNCODE": "KDS 41 20 : 2022",
    "GENERATED_COMB_COUNT": 24
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: KDS 41 20:2022 콘크리트 설계 하중조합 자동 생성 ──────────
payload = {
    "Argument": {
        "OPTION": "ADD",
        "ADD_ENVELOPE": True,
        "CODE_SELECTION": "CONCRETE",
        "DGNCODE": "KDS 41 20 : 2022",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1}
        ],
        "WIND_LOAD_COMB": {
            "PARAMETERS": [
                {
                    "BUILDING_TYPE": "HIGH",
                    "WIND_LOAD_CASE": {"ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)"},
                    "GUST_FACTOR": 2.2,
                    "KAPPA_FACTOR": 0.55
                }
            ],
            "TORSION_DIR": "BOTH"
        },
        "ORTHO_EFFECT": {
            "OPT_USE": True,
            "TYPE": "100_30",
            "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
        },
        "ADDITIONAL_LOAD": {
            "SPECIAL_LOAD": {
                "OPT_USE": True,
                "VERTICAL_LOAD_FACTOR": 0.2,
                "SDS": 0.5,
                "OVER_STRENGTH_FACTOR": [
                    {"LOAD_CASE": "RX(RS)", "FACTOR": 2.5},
                    {"LOAD_CASE": "RY(RS)", "FACTOR": 2.5}
                ]
            },
            "VERTICAL_LOAD": {"OPT_USE": True, "FORCE_FACTOR": 0.2}
        },
        "UNDERGROUND_LOAD": {"OPT_USE": False},
        "CS_ANALYSIS": False,
        "PRESTRESS_LOSS": False
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-GEN", json=payload, headers=HEADERS)
resp.raise_for_status()
print(resp.json())
```

---

## 16. `/ope/LCOM-CONC` — Load Combination (Concrete) – KDS 41 20:2022

> **기능:** KDS 41 20:2022 콘크리트 구조 설계기준에 따라 응답스펙트럼 축계수, 풍하중 조합, 직교효과, 특별지진하중·수직지진력·지하구조물하중 옵션을 지정하여 콘크리트 부재 설계용 하중조합을 자동 생성합니다. POST 전용 엔드포인트이며, 기존 조합에 추가(ADD)하거나 전체를 대체(REPLACE)할 수 있습니다.

### Input URI

```
{base url}/ope/LCOM-CONC
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["OPTION", "DGNCODE"],
      "properties": {
        "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
        "DGNCODE": { "type": "string", "enum": ["KDS 41 20 : 2022"] },
        "RS_SCALE_FACTOR": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["LOAD_CASE", "FACTOR"],
            "properties": {
              "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
              "FACTOR": { "type": "number", "description": "Scale Factor" }
            }
          }
        },
        "WIND_LOAD_COMB": {
          "type": "object",
          "required": ["PARAMETERS"],
          "properties": {
            "PARAMETERS": {
              "type": "array",
              "description": "List of wind load combination sets",
              "items": {
                "type": "object",
                "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                "properties": {
                  "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                  "WIND_LOAD_CASE": {
                    "type": "object",
                    "properties": {
                      "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                      "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                      "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                    }
                  },
                  "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                  "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                }
              }
            },
            "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
          }
        },
        "ORTHO_EFFECT": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
            "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
            "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
          }
        },
        "ADDITIONAL_LOAD": {
          "type": "object",
          "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
          "properties": {
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Special Seismic Load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                }
              }
            },
            "VERTICAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Vertical Seismic Forces" },
                "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
              }
            }
          }
        },
        "UNDERGROUND_LOAD": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "for Underground Load" },
            "SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "LOAD_CASE_LIST": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                  "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                  "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                  "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                }
              }
            },
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Whether to use special load for underground load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  },
                  "description": "Over-strength factors for underground special load"
                }
              }
            }
          }
        },
        "CS_ANALYSIS": { "type": "boolean", "default": false },
        "PRESTRESS_LOSS": { "type": "boolean", "default": false }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|---|---|---|---|---|---|
| 1 | OPTION – 기존 조합에 추가할지 전체 대체할지 | `OPTION` | string (enum) | `ADD`, `REPLACE` | 필수 |
| 2 | 콘크리트 설계기준 코드 값 | `DGNCODE` | string (enum) | `KDS 41 20 : 2022` | 필수 |
| 3 | 응답스펙트럼 하중조합 목록 | `RS_SCALE_FACTOR` | array [object] | - | 선택 |
| 3-1 | 하중 케이스명 (정적: `NAME(ST)`, 응답스펙트럼: `NAME(RS)`) | `RS_SCALE_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 3-2 | 축계수 | `RS_SCALE_FACTOR[].FACTOR` | number | - | 필수 |
| 4 | 풍하중 조합 세트 | `WIND_LOAD_COMB` | object | - | 선택 |
| 4-1 | 풍하중 조합 세트 목록 | `WIND_LOAD_COMB.PARAMETERS` | array [object] | - | 필수 (WIND_LOAD_COMB 사용 시) |
| 4-1-a | 풍하중 그룹 | `WIND_LOAD_COMB.PARAMETERS[].BUILDING_TYPE` | string (enum) | `MIDDLE`, `HIGH` | 필수 |
| 4-1-b | 풍하중 방향(Wind Direction)별 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE` | object | - | 필수 |
| 4-1-b-1 | 순풍(Along) 방향 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ALONG` | string | - | 선택 |
| 4-1-b-2 | 횡풍(Across) 방향 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ACROSS` | string | - | 선택 |
| 4-1-b-3 | 비틀림(Torsion) 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.TORSION` | string | - | 선택 |
| 4-1-c | 거스트 계수 | `WIND_LOAD_COMB.PARAMETERS[].GUST_FACTOR` | number | 최소값 0 | 선택 |
| 4-1-d | Kappa 계수 | `WIND_LOAD_COMB.PARAMETERS[].KAPPA_FACTOR` | number | 최소값 0 | 선택 |
| 4-2 | 비틀림 풍하중 방향 | `WIND_LOAD_COMB.TORSION_DIR` | string (enum) | `BOTH`, `POSITIVE`, `NEGATIVE` (기본값 `BOTH`) | 선택 |
| 5 | 직교효과 고려 옵션 | `ORTHO_EFFECT` | object | - | 선택 |
| 5-1 | 직교효과 고려 여부 | `ORTHO_EFFECT.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 5-2 | 직교효과 방식 – `ORTHO_EFFECT.OPT_USE`가 `true`일 때 필수 | `ORTHO_EFFECT.TYPE` | string (enum) | `100_30`, `SRSS` | 조건부 필수 |
| 5-3 | 직교 하중케이스 쌍 (길이 2 고정) – `ORTHO_EFFECT.OPT_USE`가 `true`일 때 필수 | `ORTHO_EFFECT.LOAD_GROUP` | array [string] | - | 조건부 필수 |
| 6 | 추가 하중 옵션 컨테이너 | `ADDITIONAL_LOAD` | object | - | 선택 |
| 6-1 | 특별지진하중 옵션 | `ADDITIONAL_LOAD.SPECIAL_LOAD` | object | - | 필수 (ADDITIONAL_LOAD 사용 시) |
| 6-1-a | 특별지진하중 사용 여부 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 6-1-b | 수직하중계수 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 6-1-c | Sds – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.SDS` | number | 최소값 0 | 조건부 필수 |
| 6-1-d | 초과강도계수 목록 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 조건부 필수 |
| 6-1-d-1 | 하중 케이스명 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 6-1-d-2 | 축계수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 필수 |
| 6-2 | 수직지진력 옵션 | `ADDITIONAL_LOAD.VERTICAL_LOAD` | object | - | 필수 (ADDITIONAL_LOAD 사용 시) |
| 6-2-a | 수직지진력 고려 여부 | `ADDITIONAL_LOAD.VERTICAL_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 6-2-b | 수직력 계수 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.VERTICAL_LOAD.FORCE_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 7 | 지하구조물 하중 옵션 | `UNDERGROUND_LOAD` | object | - | 선택 |
| 7-1 | 지하구조물 하중 사용 여부 | `UNDERGROUND_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 (UNDERGROUND_LOAD 사용 시) |
| 7-2 | 지하구조물 하중 축계수 목록 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SCALE_FACTOR` | array [object] | - | 조건부 필수 |
| 7-2-a | 하중 케이스명 | `UNDERGROUND_LOAD.SCALE_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 7-2-b | 축계수 | `UNDERGROUND_LOAD.SCALE_FACTOR[].FACTOR` | number | - | 필수 |
| 7-3 | 지진 하중케이스 목록 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.LOAD_CASE_LIST` | array [object] | - | 조건부 필수 |
| 7-3-a | 하중 케이스명 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE` | string | - | 필수 |
| 7-3-b | 지진 하중케이스 방향 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].DIRECTION` | string (enum) | `POSITIVE`, `NEGATIVE` | 필수 |
| 7-3-c | 지진 성분 토압 하중케이스명 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_SEISMIC` | array [string] | - | 필수 |
| 7-3-d | 정적 성분 토압 하중케이스명 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_STATIC` | array [string] | - | 필수 |
| 7-4 | 지하구조물 특별하중 사용 옵션 | `UNDERGROUND_LOAD.SPECIAL_LOAD` | object | - | 선택 |
| 7-4-a | 지하구조물 특별하중 사용 여부 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 7-4-b | 수직하중계수 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 7-4-c | Sds – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.SDS` | number | 최소값 0 | 조건부 필수 |
| 7-4-d | 지하구조물 특별하중 초과강도계수 목록(설명: Over-strength factors) – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 조건부 필수 |
| 7-4-d-1 | 하중 케이스명 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 7-4-d-2 | 축계수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 필수 |
| 8 | 시공단계 해석결과 반영 여부 | `CS_ANALYSIS` | boolean | 기본값 `false` | 선택 |
| 9 | 프리스트레스 손실 반영 여부 | `PRESTRESS_LOSS` | boolean | 기본값 `false` | 선택 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 20 : 2022",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1 }
    ],
    "WIND_LOAD_COMB": {
      "PARAMETERS": [
        {
          "BUILDING_TYPE": "HIGH",
          "WIND_LOAD_CASE": { "ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)" },
          "GUST_FACTOR": 2.2,
          "KAPPA_FACTOR": 0.55
        }
      ],
      "TORSION_DIR": "BOTH"
    },
    "ORTHO_EFFECT": {
      "OPT_USE": true,
      "TYPE": "100_30",
      "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
    },
    "ADDITIONAL_LOAD": {
      "SPECIAL_LOAD": {
        "OPT_USE": true,
        "VERTICAL_LOAD_FACTOR": 0.2,
        "SDS": 0.5,
        "OVER_STRENGTH_FACTOR": [
          { "LOAD_CASE": "RX(RS)", "FACTOR": 2.5 },
          { "LOAD_CASE": "RY(RS)", "FACTOR": 2.5 }
        ]
      },
      "VERTICAL_LOAD": { "OPT_USE": true, "FORCE_FACTOR": 0.2 }
    },
    "UNDERGROUND_LOAD": { "OPT_USE": false },
    "CS_ANALYSIS": false,
    "PRESTRESS_LOSS": false
  }
}
```

**POST Response Body**

```json
{
  "message": "LCOM-CONC generated successfully.",
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 20 : 2022",
    "GENERATED_COMB_COUNT": 18
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: KDS 41 20:2022 콘크리트 설계 하중조합 자동 생성 ──────────
payload = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "KDS 41 20 : 2022",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1}
        ],
        "WIND_LOAD_COMB": {
            "PARAMETERS": [
                {
                    "BUILDING_TYPE": "HIGH",
                    "WIND_LOAD_CASE": {"ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)"},
                    "GUST_FACTOR": 2.2,
                    "KAPPA_FACTOR": 0.55
                }
            ],
            "TORSION_DIR": "BOTH"
        },
        "ORTHO_EFFECT": {
            "OPT_USE": True,
            "TYPE": "100_30",
            "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
        },
        "ADDITIONAL_LOAD": {
            "SPECIAL_LOAD": {
                "OPT_USE": True,
                "VERTICAL_LOAD_FACTOR": 0.2,
                "SDS": 0.5,
                "OVER_STRENGTH_FACTOR": [
                    {"LOAD_CASE": "RX(RS)", "FACTOR": 2.5},
                    {"LOAD_CASE": "RY(RS)", "FACTOR": 2.5}
                ]
            },
            "VERTICAL_LOAD": {"OPT_USE": True, "FORCE_FACTOR": 0.2}
        },
        "UNDERGROUND_LOAD": {"OPT_USE": False},
        "CS_ANALYSIS": False,
        "PRESTRESS_LOSS": False
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-CONC", json=payload, headers=HEADERS)
resp.raise_for_status()
print(resp.json())
```

---

## 17. `/ope/LCOM-STEEL` — Load Combination (Steel) – KDS 41 30:2022

> **기능:** KDS 41 30:2022 강구조 설계기준에 따라 응답스펙트럼 축계수, 풍하중 조합, 직교효과, 특별지진하중·수직지진력·지하구조물하중 옵션을 지정하여 강재 부재 설계용 하중조합을 자동 생성합니다. POST 전용 엔드포인트이며, 기존 조합에 추가(ADD)하거나 전체를 대체(REPLACE)할 수 있습니다. LCOM-CONC와 스키마 구조가 동일하나 `CS_ANALYSIS`, `PRESTRESS_LOSS` 필드는 존재하지 않습니다.

### Input URI

```
{base url}/ope/LCOM-STEEL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["OPTION", "DGNCODE"],
      "properties": {
        "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
        "DGNCODE": { "type": "string", "enum": ["KDS 41 30 : 2022"] },
        "RS_SCALE_FACTOR": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["LOAD_CASE", "FACTOR"],
            "properties": {
              "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
              "FACTOR": { "type": "number", "description": "Scale Factor" }
            }
          }
        },
        "WIND_LOAD_COMB": {
          "type": "object",
          "required": ["PARAMETERS"],
          "properties": {
            "PARAMETERS": {
              "type": "array",
              "description": "List of wind load combination sets",
              "items": {
                "type": "object",
                "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                "properties": {
                  "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                  "WIND_LOAD_CASE": {
                    "type": "object",
                    "properties": {
                      "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                      "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                      "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                    }
                  },
                  "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                  "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                }
              }
            },
            "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
          }
        },
        "ORTHO_EFFECT": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
            "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
            "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
          }
        },
        "ADDITIONAL_LOAD": {
          "type": "object",
          "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
          "properties": {
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Special Seismic Load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                }
              }
            },
            "VERTICAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Vertical Seismic Forces" },
                "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
              }
            }
          }
        },
        "UNDERGROUND_LOAD": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "for Underground Load" },
            "SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "LOAD_CASE_LIST": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                  "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                  "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                  "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                }
              }
            },
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Whether to use special load for underground load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  },
                  "description": "Over-strength factors for underground special load"
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

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|---|---|---|---|---|---|
| 1 | OPTION – 기존 조합에 추가할지 전체 대체할지 | `OPTION` | string (enum) | `ADD`, `REPLACE` | 필수 |
| 2 | 강재 설계기준 코드 값 | `DGNCODE` | string (enum) | `KDS 41 30 : 2022` | 필수 |
| 3 | 응답스펙트럼 하중조합 목록 | `RS_SCALE_FACTOR` | array [object] | - | 선택 |
| 3-1 | 하중 케이스명 (정적: `NAME(ST)`, 응답스펙트럼: `NAME(RS)`) | `RS_SCALE_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 3-2 | 축계수 | `RS_SCALE_FACTOR[].FACTOR` | number | - | 필수 |
| 4 | 풍하중 조합 세트 | `WIND_LOAD_COMB` | object | - | 선택 |
| 4-1 | 풍하중 조합 세트 목록 | `WIND_LOAD_COMB.PARAMETERS` | array [object] | - | 필수 (WIND_LOAD_COMB 사용 시) |
| 4-1-a | 풍하중 그룹 | `WIND_LOAD_COMB.PARAMETERS[].BUILDING_TYPE` | string (enum) | `MIDDLE`, `HIGH` | 필수 |
| 4-1-b | WIND_LOAD_CASE 컨테이너 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE` | object | - | 필수 |
| 4-1-b-1 | 순풍(Along) 방향 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ALONG` | string | - | 선택 |
| 4-1-b-2 | 횡풍(Across) 방향 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ACROSS` | string | - | 선택 |
| 4-1-b-3 | 비틀림(Torsion) 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.TORSION` | string | - | 선택 |
| 4-1-c | 거스트 계수 | `WIND_LOAD_COMB.PARAMETERS[].GUST_FACTOR` | number | 최소값 0 | 선택 |
| 4-1-d | Kappa 계수 | `WIND_LOAD_COMB.PARAMETERS[].KAPPA_FACTOR` | number | 최소값 0 | 선택 |
| 4-2 | 비틀림 풍하중 방향 | `WIND_LOAD_COMB.TORSION_DIR` | string (enum) | `BOTH`, `POSITIVE`, `NEGATIVE` (기본값 `BOTH`) | 선택 |
| 5 | 직교효과 고려 옵션 | `ORTHO_EFFECT` | object | - | 선택 |
| 5-1 | 직교효과 고려 여부 | `ORTHO_EFFECT.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 5-2 | 직교효과 방식 – `ORTHO_EFFECT.OPT_USE`가 `true`일 때 필수 | `ORTHO_EFFECT.TYPE` | string (enum) | `100_30`, `SRSS` | 조건부 필수 |
| 5-3 | 직교 하중케이스 쌍 (길이 2 고정) – `ORTHO_EFFECT.OPT_USE`가 `true`일 때 필수 | `ORTHO_EFFECT.LOAD_GROUP` | array [string] | - | 조건부 필수 |
| 6 | 추가 하중 옵션 컨테이너 | `ADDITIONAL_LOAD` | object | - | 선택 |
| 6-1 | 특별지진하중 옵션 | `ADDITIONAL_LOAD.SPECIAL_LOAD` | object | - | 필수 (ADDITIONAL_LOAD 사용 시) |
| 6-1-a | 특별지진하중 사용 여부 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 6-1-b | 수직하중계수 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 6-1-c | Sds – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.SDS` | number | 최소값 0 | 조건부 필수 |
| 6-1-d | Over Strength Factor 목록 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 조건부 필수 |
| 6-1-d-1 | 하중 케이스명 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 6-1-d-2 | 축계수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 필수 |
| 6-2 | 수직지진력 옵션 | `ADDITIONAL_LOAD.VERTICAL_LOAD` | object | - | 필수 (ADDITIONAL_LOAD 사용 시) |
| 6-2-a | 수직지진력 고려 여부 | `ADDITIONAL_LOAD.VERTICAL_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 6-2-b | 수직력 계수 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.VERTICAL_LOAD.FORCE_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 7 | 지하구조물 하중 옵션 | `UNDERGROUND_LOAD` | object | - | 선택 |
| 7-1 | 지하구조물 하중 사용 여부 | `UNDERGROUND_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 (UNDERGROUND_LOAD 사용 시) |
| 7-2 | 지하구조물 하중 축계수 목록 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SCALE_FACTOR` | array [object] | - | 조건부 필수 |
| 7-2-a | 하중 케이스명 | `UNDERGROUND_LOAD.SCALE_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 7-2-b | 축계수 | `UNDERGROUND_LOAD.SCALE_FACTOR[].FACTOR` | number | - | 필수 |
| 7-3 | 지진 하중케이스 목록 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.LOAD_CASE_LIST` | array [object] | - | 조건부 필수 |
| 7-3-a | 하중 케이스명 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE` | string | - | 필수 |
| 7-3-b | 지진 하중케이스 방향 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].DIRECTION` | string (enum) | `POSITIVE`, `NEGATIVE` | 필수 |
| 7-3-c | 지진 성분 토압 하중케이스명 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_SEISMIC` | array [string] | - | 필수 |
| 7-3-d | 정적 성분 토압 하중케이스명 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_STATIC` | array [string] | - | 필수 |
| 7-4 | 지하구조물 특별하중 사용 옵션 | `UNDERGROUND_LOAD.SPECIAL_LOAD` | object | - | 선택 |
| 7-4-a | 지하구조물 특별하중 사용 여부 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 7-4-b | 수직하중계수 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 7-4-c | Sds – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.SDS` | number | 최소값 0 | 조건부 필수 |
| 7-4-d | 지하구조물 특별하중 초과강도계수 목록 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 조건부 필수 |
| 7-4-d-1 | 하중 케이스명 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 7-4-d-2 | 축계수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 필수 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 30 : 2022",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1 }
    ],
    "WIND_LOAD_COMB": {
      "PARAMETERS": [
        {
          "BUILDING_TYPE": "HIGH",
          "WIND_LOAD_CASE": { "ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)" },
          "GUST_FACTOR": 2.2,
          "KAPPA_FACTOR": 0.55
        }
      ],
      "TORSION_DIR": "BOTH"
    },
    "ORTHO_EFFECT": {
      "OPT_USE": true,
      "TYPE": "100_30",
      "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
    },
    "ADDITIONAL_LOAD": {
      "SPECIAL_LOAD": {
        "OPT_USE": true,
        "VERTICAL_LOAD_FACTOR": 0.2,
        "SDS": 0.5,
        "OVER_STRENGTH_FACTOR": [
          { "LOAD_CASE": "RX(RS)", "FACTOR": 2.5 },
          { "LOAD_CASE": "RY(RS)", "FACTOR": 2.5 }
        ]
      },
      "VERTICAL_LOAD": { "OPT_USE": true, "FORCE_FACTOR": 0.2 }
    },
    "UNDERGROUND_LOAD": { "OPT_USE": false }
  }
}
```

**POST Response Body**

```json
{
  "message": "LCOM-STEEL generated successfully.",
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 30 : 2022",
    "GENERATED_COMB_COUNT": 16
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: KDS 41 30:2022 강구조 설계 하중조합 자동 생성 ────────────
payload = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "KDS 41 30 : 2022",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1}
        ],
        "WIND_LOAD_COMB": {
            "PARAMETERS": [
                {
                    "BUILDING_TYPE": "HIGH",
                    "WIND_LOAD_CASE": {"ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)"},
                    "GUST_FACTOR": 2.2,
                    "KAPPA_FACTOR": 0.55
                }
            ],
            "TORSION_DIR": "BOTH"
        },
        "ORTHO_EFFECT": {
            "OPT_USE": True,
            "TYPE": "100_30",
            "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
        },
        "ADDITIONAL_LOAD": {
            "SPECIAL_LOAD": {
                "OPT_USE": True,
                "VERTICAL_LOAD_FACTOR": 0.2,
                "SDS": 0.5,
                "OVER_STRENGTH_FACTOR": [
                    {"LOAD_CASE": "RX(RS)", "FACTOR": 2.5},
                    {"LOAD_CASE": "RY(RS)", "FACTOR": 2.5}
                ]
            },
            "VERTICAL_LOAD": {"OPT_USE": True, "FORCE_FACTOR": 0.2}
        },
        "UNDERGROUND_LOAD": {"OPT_USE": False}
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-STEEL", json=payload, headers=HEADERS)
resp.raise_for_status()
print(resp.json())
```

---

## 18. `/ope/LCOM-SRC` — Load Combination (SRC) – KDS 41 SRC:2022 / AIK-SRC2K

> **기능:** KDS 41 SRC:2022 합성구조(강관콘크리트/매입형강 등) 설계기준에 따라 응답스펙트럼 축계수, 풍하중 조합, 직교효과, 특별지진하중·수직지진력·지하구조물하중 옵션을 지정하여 SRC 부재 설계용 하중조합을 자동 생성합니다. POST 전용 엔드포인트이며, 기존 조합에 추가(ADD)하거나 전체를 대체(REPLACE)할 수 있습니다. 동일 엔드포인트는 `DGNCODE: "AIK-SRC2K"`를 지정하는 더 단순한 스키마(`OPTION` + `DGNCODE` + `RS_SCALE_FACTOR`)도 지원하며 이는 본 문서 하단의 "LCOM-GEN/SRC AIK-SRC2K 변형 스키마" 절에서 다룹니다. 본 절은 KDS 41 SRC:2022 변형만을 다룹니다.

### Input URI

```
{base url}/ope/LCOM-SRC
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["OPTION", "DGNCODE"],
      "properties": {
        "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
        "DGNCODE": { "type": "string", "enum": ["KDS 41 SRC : 2022"] },
        "RS_SCALE_FACTOR": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["LOAD_CASE", "FACTOR"],
            "properties": {
              "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
              "FACTOR": { "type": "number", "description": "Scale Factor" }
            }
          }
        },
        "WIND_LOAD_COMB": {
          "type": "object",
          "required": ["PARAMETERS"],
          "properties": {
            "PARAMETERS": {
              "type": "array",
              "description": "List of wind load combination sets",
              "items": {
                "type": "object",
                "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                "properties": {
                  "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                  "WIND_LOAD_CASE": {
                    "type": "object",
                    "properties": {
                      "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                      "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                      "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                    }
                  },
                  "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                  "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                }
              }
            },
            "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
          }
        },
        "ORTHO_EFFECT": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
            "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
            "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
          }
        },
        "ADDITIONAL_LOAD": {
          "type": "object",
          "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
          "properties": {
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Special Seismic Load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                }
              }
            },
            "VERTICAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Vertical Seismic Forces" },
                "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
              }
            }
          }
        },
        "UNDERGROUND_LOAD": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "for Underground Load" },
            "SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "LOAD_CASE_LIST": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                  "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                  "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                  "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                }
              }
            },
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Whether to use special load for underground load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  },
                  "description": "Over-strength factors for underground special load"
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

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|---|---|---|---|---|---|
| 1 | OPTION – 기존 조합에 추가할지 전체 대체할지 | `OPTION` | string (enum) | `ADD`, `REPLACE` | 필수 |
| 2 | SRC 설계기준 코드 값 | `DGNCODE` | string (enum) | `KDS 41 SRC : 2022` | 필수 |
| 3 | 응답스펙트럼 하중조합 목록 | `RS_SCALE_FACTOR` | array [object] | - | 선택 |
| 3-1 | 하중 케이스명 (정적: `NAME(ST)`, 응답스펙트럼: `NAME(RS)`) | `RS_SCALE_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 3-2 | 축계수 | `RS_SCALE_FACTOR[].FACTOR` | number | - | 필수 |
| 4 | 풍하중 조합 세트 | `WIND_LOAD_COMB` | object | - | 선택 |
| 4-1 | 풍하중 조합 세트 목록 | `WIND_LOAD_COMB.PARAMETERS` | array [object] | - | 필수 (WIND_LOAD_COMB 사용 시) |
| 4-1-a | 풍하중 그룹 | `WIND_LOAD_COMB.PARAMETERS[].BUILDING_TYPE` | string (enum) | `MIDDLE`, `HIGH` | 필수 |
| 4-1-b | 풍하중 방향(Wind Direction)별 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE` | object | - | 필수 |
| 4-1-b-1 | 순풍(Along) 방향 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ALONG` | string | - | 선택 |
| 4-1-b-2 | 횡풍(Across) 방향 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ACROSS` | string | - | 선택 |
| 4-1-b-3 | 비틀림(Torsion) 하중 케이스 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.TORSION` | string | - | 선택 |
| 4-1-c | 거스트 계수 | `WIND_LOAD_COMB.PARAMETERS[].GUST_FACTOR` | number | 최소값 0 | 선택 |
| 4-1-d | Kappa 계수 | `WIND_LOAD_COMB.PARAMETERS[].KAPPA_FACTOR` | number | 최소값 0 | 선택 |
| 4-2 | 비틀림 풍하중 방향 | `WIND_LOAD_COMB.TORSION_DIR` | string (enum) | `BOTH`, `POSITIVE`, `NEGATIVE` (기본값 `BOTH`) | 선택 |
| 5 | 직교효과 고려 옵션 | `ORTHO_EFFECT` | object | - | 선택 |
| 5-1 | 직교효과 고려 여부 | `ORTHO_EFFECT.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 5-2 | 직교효과 방식 – `ORTHO_EFFECT.OPT_USE`가 `true`일 때 필수 | `ORTHO_EFFECT.TYPE` | string (enum) | `100_30`, `SRSS` | 조건부 필수 |
| 5-3 | 직교 하중케이스 쌍 (길이 2 고정) – `ORTHO_EFFECT.OPT_USE`가 `true`일 때 필수 | `ORTHO_EFFECT.LOAD_GROUP` | array [string] | - | 조건부 필수 |
| 6 | 추가 하중 옵션 컨테이너 | `ADDITIONAL_LOAD` | object | - | 선택 |
| 6-1 | 특별지진하중 옵션 | `ADDITIONAL_LOAD.SPECIAL_LOAD` | object | - | 필수 (ADDITIONAL_LOAD 사용 시) |
| 6-1-a | 특별지진하중 사용 여부 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 6-1-b | 수직하중계수 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 6-1-c | Sds – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.SDS` | number | 최소값 0 | 조건부 필수 |
| 6-1-d | Over strength factor 목록 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 조건부 필수 |
| 6-1-d-1 | 하중 케이스명 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 6-1-d-2 | 축계수 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 필수 |
| 6-2 | 수직지진력 옵션 | `ADDITIONAL_LOAD.VERTICAL_LOAD` | object | - | 필수 (ADDITIONAL_LOAD 사용 시) |
| 6-2-a | 수직지진력 고려 여부 | `ADDITIONAL_LOAD.VERTICAL_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 6-2-b | 수직력 계수 – `OPT_USE`가 `true`일 때 필수 | `ADDITIONAL_LOAD.VERTICAL_LOAD.FORCE_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 7 | 지하구조물 하중 옵션 | `UNDERGROUND_LOAD` | object | - | 선택 |
| 7-1 | 지하구조물 하중 사용 여부 | `UNDERGROUND_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 (UNDERGROUND_LOAD 사용 시) |
| 7-2 | 지하구조물 하중 축계수 목록 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SCALE_FACTOR` | array [object] | - | 조건부 필수 |
| 7-2-a | 하중 케이스명 | `UNDERGROUND_LOAD.SCALE_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 7-2-b | 축계수 | `UNDERGROUND_LOAD.SCALE_FACTOR[].FACTOR` | number | - | 필수 |
| 7-3 | 지진 하중케이스 목록(Seismic Load Case List) – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.LOAD_CASE_LIST` | array [object] | - | 조건부 필수 |
| 7-3-a | 하중 케이스명 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE` | string | - | 필수 |
| 7-3-b | 지진 하중케이스 방향 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].DIRECTION` | string (enum) | `POSITIVE`, `NEGATIVE` | 필수 |
| 7-3-c | 지진 성분 토압 하중케이스명 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_SEISMIC` | array [string] | - | 필수 |
| 7-3-d | 정적 성분 토압 하중케이스명 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_STATIC` | array [string] | - | 필수 |
| 7-4 | 지하구조물 특별하중 사용 옵션 | `UNDERGROUND_LOAD.SPECIAL_LOAD` | object | - | 선택 |
| 7-4-a | 지하구조물 특별하중 사용 여부 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 기본값 `false` | 필수 |
| 7-4-b | 수직하중계수 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 최소값 0 | 조건부 필수 |
| 7-4-c | Sds – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.SDS` | number | 최소값 0 | 조건부 필수 |
| 7-4-d | 지하구조물 특별하중 초과강도계수 목록 – `OPT_USE`가 `true`일 때 필수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 조건부 필수 |
| 7-4-d-1 | 하중 케이스명 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 필수 |
| 7-4-d-2 | 축계수 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 필수 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 SRC : 2022",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1 }
    ],
    "WIND_LOAD_COMB": {
      "PARAMETERS": [
        {
          "BUILDING_TYPE": "HIGH",
          "WIND_LOAD_CASE": { "ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)" },
          "GUST_FACTOR": 2.2,
          "KAPPA_FACTOR": 0.55
        }
      ],
      "TORSION_DIR": "BOTH"
    },
    "ORTHO_EFFECT": {
      "OPT_USE": true,
      "TYPE": "100_30",
      "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
    },
    "ADDITIONAL_LOAD": {
      "SPECIAL_LOAD": {
        "OPT_USE": true,
        "VERTICAL_LOAD_FACTOR": 0.2,
        "SDS": 0.5,
        "OVER_STRENGTH_FACTOR": [
          { "LOAD_CASE": "RX(RS)", "FACTOR": 2.5 },
          { "LOAD_CASE": "RY(RS)", "FACTOR": 2.5 }
        ]
      },
      "VERTICAL_LOAD": { "OPT_USE": true, "FORCE_FACTOR": 0.2 }
    },
    "UNDERGROUND_LOAD": { "OPT_USE": false }
  }
}
```

**POST Response Body**

```json
{
  "message": "LCOM-SRC generated successfully.",
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 SRC : 2022",
    "GENERATED_COMB_COUNT": 20
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: KDS 41 SRC:2022 합성구조 설계 하중조합 자동 생성 ─────────
payload = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "KDS 41 SRC : 2022",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1}
        ],
        "WIND_LOAD_COMB": {
            "PARAMETERS": [
                {
                    "BUILDING_TYPE": "HIGH",
                    "WIND_LOAD_CASE": {"ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)"},
                    "GUST_FACTOR": 2.2,
                    "KAPPA_FACTOR": 0.55
                }
            ],
            "TORSION_DIR": "BOTH"
        },
        "ORTHO_EFFECT": {
            "OPT_USE": True,
            "TYPE": "100_30",
            "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
        },
        "ADDITIONAL_LOAD": {
            "SPECIAL_LOAD": {
                "OPT_USE": True,
                "VERTICAL_LOAD_FACTOR": 0.2,
                "SDS": 0.5,
                "OVER_STRENGTH_FACTOR": [
                    {"LOAD_CASE": "RX(RS)", "FACTOR": 2.5},
                    {"LOAD_CASE": "RY(RS)", "FACTOR": 2.5}
                ]
            },
            "VERTICAL_LOAD": {"OPT_USE": True, "FORCE_FACTOR": 0.2}
        },
        "UNDERGROUND_LOAD": {"OPT_USE": False}
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-SRC", json=payload, headers=HEADERS)
resp.raise_for_status()
print(resp.json())
```

---

## LCOM-GEN/SRC AIK-SRC2K 변형 스키마

`/ope/LCOM-GEN`, `/ope/LCOM-SRC`는 `DGNCODE`가 `"AIK-SRC2K"`일 때 아래의 단순화된 스키마를 사용합니다(위 15·18절의 KDS:2022 스키마와 별개).

### JSON Schema (공통)

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["OPTION", "DGNCODE"],
      "properties": {
        "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
        "DGNCODE": { "type": "string", "enum": ["AIK-SRC2K"] },
        "RS_SCALE_FACTOR": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["LOAD_CASE", "FACTOR"],
            "properties": {
              "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
              "FACTOR": { "type": "number", "description": "Scale Factor" }
            }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 필수 |
|-----|------|-----|-----------|------|
| 1 | 처리 방식 · 추가: `"ADD"` / 대체: `"REPLACE"` | `"OPTION"` | String (enum) | **Required** |
| 2 | 설계코드 · `"AIK-SRC2K"` | `"DGNCODE"` | String (enum) | **Required** |
| 3 | 응답스펙트럼 하중케이스별 배율 목록 (`/ope/LCOM-GEN`에서는 **Required**, `/ope/LCOM-SRC`에서는 Optional) | `"RS_SCALE_FACTOR"` | Array [Object] | 엔드포인트별 상이 |
| 3-1 | └ 하중케이스명 · 정적: `NAME(ST)` / 응답스펙트럼: `NAME(RS)` | `RS_SCALE_FACTOR[].LOAD_CASE` | String | **Required** |
| 3-2 | └ 배율 | `RS_SCALE_FACTOR[].FACTOR` | Number | **Required** |

### Request Body 예시

**`/ope/LCOM-GEN` (AIK-SRC2K)**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "AIK-SRC2K",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1 }
    ]
  }
}
```

**`/ope/LCOM-SRC` (AIK-SRC2K)**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "AIK-SRC2K",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1.2 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1.3 }
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: AIK-SRC2K 기준 일반 하중조합 자동 생성 ───────────────────
payload = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "AIK-SRC2K",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1}
        ]
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-GEN", json=payload, headers=HEADERS)
print("POST (LCOM-GEN, AIK-SRC2K):", resp.status_code, resp.json())

# ── POST: AIK-SRC2K 기준 SRC 하중조합 자동 생성 ────────────────────
payload2 = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "AIK-SRC2K",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1.2},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1.3}
        ]
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-SRC", json=payload2, headers=HEADERS)
print("POST (LCOM-SRC, AIK-SRC2K):", resp.status_code, resp.json())
```

---

## End-to-End Workflow

다음은 모델 전처리(메싱·부재배정) 및 설계 하중조합 자동생성 워크플로우입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── STEP 1: 프로젝트 현황 확인 ─────────────────────────────────────
r1 = requests.get(f"{BASE_URL}/ope/PROJECTSTATUS", headers=HEADERS)
print(f"STEP1 PROJECTSTATUS: {r1.status_code}")

# ── STEP 2: 평면 영역 자동 메싱 ────────────────────────────────────
mesh_payload = {
    "Argument": {
        "MESHER": {"METHOD": "PlanarElements", "TARGETS": [1401]},
        "MESH_SIZE": {"LENGTH": 1},
        "PROPERTY": {"ELEMENT_TYPE": "Plate", "MATERIAL": 1, "THICKNESS": 1},
        "DOMAIN_NAME": {"NAME": "Slab_1F"}
    }
}
r2 = requests.post(f"{BASE_URL}/ope/AUTOMESH", json=mesh_payload, headers=HEADERS)
print(f"STEP2 AUTOMESH: {r2.status_code}")

# ── STEP 3: 부재(Member) 자동 배정 ─────────────────────────────────
memb_payload = {"Argument": {"ASSIGN_TYPE": "AUTO", "SELECTION_TYPE": "ALL", "ALLOW_SINGLE": True}}
r3 = requests.post(f"{BASE_URL}/ope/MEMB", json=memb_payload, headers=HEADERS)
print(f"STEP3 MEMB: {r3.status_code}")

# ── STEP 4: 층 검토 파라미터 설정 ──────────────────────────────────
story_payload = {"Argument": {"COUNTRY_CODE": "KBC2009"}}
r4 = requests.post(f"{BASE_URL}/ope/STORY_PARAM", json=story_payload, headers=HEADERS)
print(f"STEP4 STORY_PARAM: {r4.status_code}")

# ── STEP 5: 강재 설계 하중조합 자동 생성 ───────────────────────────
lcom_steel_payload = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "KDS(41-30:2022)",
        "STATIC_LOADS": [
            {"LOAD_CASE": "DeadLoad(ST)", "TYPE": "DEAD"},
            {"LOAD_CASE": "LiveLoad(ST)", "TYPE": "LIVE"}
        ]
    }
}
r5 = requests.post(f"{BASE_URL}/ope/LCOM-STEEL", json=lcom_steel_payload, headers=HEADERS)
print(f"STEP5 LCOM-STEEL: {r5.status_code}")

# ── STEP 6: 생성된 하중조합을 강재설계 검토에 사용 지정 ────────────
uslc_payload = {
    "Argument": {
        "LCOM_LIST": [{"TYPE": "STEEL", "NAME": "sLCB1"}],
        "PREFIX": "N",
        "POSITION": "STEEL",
        "LOADS": {"SELF_WEIGHT": True, "NODAL_LOAD": True, "BEAM_LOAD": True}
    }
}
r6 = requests.post(f"{BASE_URL}/ope/USLC", json=uslc_payload, headers=HEADERS)
print(f"STEP6 USLC: {r6.status_code}")
```
