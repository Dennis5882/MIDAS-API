# DB – Temperature / Prestress

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:** `https://moa-engineers.midasit.com:443/gen`  
> **인증:** 모든 요청에 `MAPI-Key: <key>` 헤더 필수  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

---

## 목차

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | [/db/ETMP](#1-dbetmp--element-temperature) | Element Temperature |
| 2 | [/db/GTMP](#2-dbgtmp--temperature-gradient) | Temperature Gradient |
| 3 | [/db/BTMP](#3-dbbtmp--beam-section-temperature) | Beam Section Temperature |
| 4 | [/db/STMP](#4-dbstmp--system-temperature) | System Temperature |
| 5 | [/db/NTMP](#5-dbntmp--nodal-temperature) | Nodal Temperature |
| 6 | [/db/TDNT](#6-dbtdnt--tendon-property) | Tendon Property |
| 7 | [/db/TDNA](#7-dbtdna--tendon-profile) | Tendon Profile |
| 8 | [/db/TDCS](#8-dbtdcs--tendon-location-for-composite-section) | Tendon Location for Composite Section |
| 9 | [/db/TDPL](#9-dbtdpl--tendon-prestress) | Tendon Prestress |
| 10 | [/db/PRST](#10-dbprst--prestress-beam-loads) | Prestress Beam Loads |
| 11 | [/db/PTNS](#11-dbptns--pretension-loads) | Pretension Loads |
| 12 | [/db/EXLD](#12-dbexld--external-type-load-case-for-pretension) | External Type Load Case for Pretension |

---

## 공통 Python 헬퍼

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY_HERE"

def midas_api(method: str, endpoint: str, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}
```

---

## 1. /db/ETMP — Element Temperature

> 요소(Element)에 균일 온도 하중을 적용합니다. 키(key)는 **요소 번호**이며, `ITEMS` 배열로 여러 하중 케이스를 동시에 입력할 수 있습니다.

**Input URI:** `{base url}/db/ETMP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "TEMP": 35
        },
        {
          "ID": 2,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "",
          "TEMP": -20
        }
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Element Temperature (배열 오브젝트로 입력) | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Temperature | `"TEMP"` | Number | - | Required |

### Python 예제

```python
# 요소 온도 하중 적용 (POST)
# 키 = 요소 번호, ITEMS 배열로 여러 하중 케이스 동시 입력 가능
etmp_data = {
    "Assign": {
        "1": {   # 요소 1번
            "ITEMS": [
                {"ID": 1, "LCNAME": "Temp(+)", "GROUP_NAME": "", "TEMP": 35},
                {"ID": 2, "LCNAME": "Temp(-)", "GROUP_NAME": "", "TEMP": -20},
            ]
        },
        "5": {   # 요소 5번
            "ITEMS": [
                {"ID": 1, "LCNAME": "Temp(+)", "GROUP_NAME": "", "TEMP": 35},
            ]
        },
    }
}
result = midas_api("POST", "/db/ETMP", etmp_data)

# 전체 조회 (GET)
all_etmp = midas_api("GET", "/db/ETMP")

# 수정 (PUT)
update_data = {
    "Assign": {
        "1": {"ITEMS": [{"ID": 1, "LCNAME": "Temp(+)", "GROUP_NAME": "", "TEMP": 40}]}
    }
}
midas_api("PUT", "/db/ETMP", update_data)

# 삭제 (DELETE)
midas_api("DELETE", "/db/ETMP", {"Assign": {"1": {}}})
```

---

## 2. /db/GTMP — Temperature Gradient

> 보(Beam) 또는 판(Plate) 요소에 온도 구배 하중을 적용합니다. 보 요소는 z방향과 y방향 구배를 모두 지정할 수 있습니다.

**Input URI:** `{base url}/db/GTMP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

**Beam 타입 예시:**

```json
{
  "Assign": {
    "2": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "TYPE": 1,
          "TZ": 10,
          "USE_HZ": true,
          "TY": -10,
          "USE_HY": true
        },
        {
          "ID": 2,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "",
          "TYPE": 1,
          "TZ": 10,
          "USE_HZ": false,
          "HZ": 1.2,
          "TY": -10,
          "USE_HY": false,
          "HY": 0.5
        }
      ]
    }
  }
}
```

**Plate 타입 예시:**

```json
{
  "Assign": {
    "21": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "TYPE": 2,
          "TZ": 10,
          "USE_HZ": true
        },
        {
          "ID": 2,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "",
          "TYPE": 2,
          "TZ": 10,
          "USE_HZ": false,
          "HZ": 0.2
        }
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Temperature Gradient (배열 오브젝트로 입력) | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Element Type · Beam: `1` · Plate: `2` | `"TYPE"` | Integer | - | Required |
| (5) | T2z − T1z | `"TZ"` | Number | - | Required |
| (6) | Use Section Hz | `"USE_HZ"` | Boolean | `false` | Optional |
| (7) | Hz value (`USE_HZ` = false 일 때 사용) | `"HZ"` | Number | - | Optional |
| (8) | T2y − T1y (Beam 타입 전용) | `"TY"` | Number | - | Required (Beam) |
| (9) | Use Section Hy (Beam 타입 전용) | `"USE_HY"` | Boolean | `false` | Optional |
| (10) | Hy value (`USE_HY` = false 일 때 사용, Beam 전용) | `"HY"` | Number | - | Optional |

### Python 예제

```python
# 보 요소에 온도 구배 적용 (POST)
gtmp_beam = {
    "Assign": {
        "2": {   # 요소 2번 (보)
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "Temp(+)",
                    "GROUP_NAME": "",
                    "TYPE": 1,      # Beam
                    "TZ": 10,       # z방향 온도차 (T2z - T1z)
                    "USE_HZ": True, # 단면 Hz 사용
                    "TY": -10,      # y방향 온도차 (T2y - T1y)
                    "USE_HY": True, # 단면 Hy 사용
                },
            ]
        }
    }
}
midas_api("POST", "/db/GTMP", gtmp_beam)

# 판 요소에 온도 구배 적용 (POST)
gtmp_plate = {
    "Assign": {
        "21": {   # 요소 21번 (판)
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "Temp(+)",
                    "GROUP_NAME": "",
                    "TYPE": 2,       # Plate
                    "TZ": 10,
                    "USE_HZ": False,
                    "HZ": 0.2,       # Hz 직접 입력
                },
            ]
        }
    }
}
midas_api("POST", "/db/GTMP", gtmp_plate)
```

---

## 3. /db/BTMP — Beam Section Temperature

> 보 단면의 온도 분포를 구간별로 정의합니다. 일반 단면(General)과 PSC/합성 단면(PSC/Composite) 두 가지 모드를 지원합니다.

**Input URI:** `{base url}/db/BTMP`  
**Active Methods:** `POST, GET, PUT, DELETE`

> ⚠️ MIDAS Civil NX 전용 기능

### 요청 바디 구조

**General – 단면 재료 자동 참조 (Elements):**

```json
{
  "Assign": {
    "51": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "DIR": "LZ",
          "REF": "Centroid",
          "NUM": 1,
          "bPSC": false,
          "vSECTTMP": [
            {
              "TYPE": "ELEMENT",
              "VAL_B": 0.2,
              "VAL_H1": 0.1,
              "VAL_H2": 0.2,
              "VAL_T1": 3,
              "VAL_T2": 12.4
            }
          ]
        }
      ]
    }
  }
}
```

**General – 재료 직접 입력 (User Input):**

```json
{
  "Assign": {
    "51": {
      "ITEMS": [
        {
          "ID": 2,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "DIR": "LZ",
          "REF": "Centroid",
          "NUM": 1,
          "bPSC": false,
          "vSECTTMP": [
            {
              "TYPE": "INPUT",
              "ELAST": 34800000,
              "THERMAL": 1e-05,
              "VAL_B": 0.2,
              "VAL_H1": 0.1,
              "VAL_H2": 0.2,
              "VAL_T1": 3,
              "VAL_T2": 12.4
            }
          ]
        }
      ]
    }
  }
}
```

**PSC/Composite – 단면 재료 자동 참조 (Elements):**

```json
{
  "Assign": {
    "56": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "",
          "DIR": "LZ",
          "REF": "Top",
          "NUM": 1,
          "bPSC": true,
          "vSECTTMP": [
            {
              "TYPE": "ELEMENT",
              "REF": 0,
              "OPT_B": 1,
              "VAL_B": 0.3,
              "OPT_H1": 3,
              "VAL_H1": 0.2,
              "OPT_H2": 3,
              "VAL_H2": 0.4,
              "VAL_T1": 3,
              "VAL_T2": 12.4
            }
          ]
        }
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Beam Section Temperature (배열 오브젝트로 입력) | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Direction · Local-y: `"LY"` · Local-z: `"LZ"` | `"DIR"` | String | `"LZ"` | Optional |
| (5) | Ref. Position · `"Centroid"` · `"+End(Top)"` → `"Top"` · `"-End(Bot)"` → `"Bot"` | `"REF"` | String | `"Centroid"` | Optional |
| (6) | Number of Section Temperature (`vSECTTMP` 항목 수) | `"NUM"` | Integer | - | Required |
| (7) | Section Type · General: `false` · PSC/Composite: `true` | `"bPSC"` | Boolean | `false` | Optional |
| (8) | Section Temperature List | `"vSECTTMP"` | Array \[Object\] | - | Required |
| i | Material Type · Element: `"ELEMENT"` · Input: `"INPUT"` | `"TYPE"` | String | `"ELEMENT"` | Optional |
| ii | B Value | `"VAL_B"` | Number | 0 | Optional |
| iii | H1 Value | `"VAL_H1"` | Number | - | Optional |
| iv | H2 Value | `"VAL_H2"` | Number | - | Optional |
| v | T1 Value | `"VAL_T1"` | Number | 0 | Optional |
| vi | T2 Value | `"VAL_T2"` | Number | 0 | Optional |
| vii | Modulus of Elasticity (`TYPE` = `"INPUT"` 일 때) | `"ELAST"` | Number | - | Optional |
| viii | Thermal Coefficient (`TYPE` = `"INPUT"` 일 때) | `"THERMAL"` | Number | - | Optional |
| ix | Ref. (`bPSC` = true) · Top: `0` · Bottom: `1` | `"REF"` | Integer | 0 | Optional |
| x | B-Type (`bPSC` = true) · Section: `0` · Value: `1` | `"OPT_B"` | Integer | 1 | Optional |
| xi | H1-Type (`bPSC` = true) · Z1:`0` · Z2:`1` · Z3:`2` · Value:`3` | `"OPT_H1"` | Integer | 3 | Optional |
| xii | H2-Type (`bPSC` = true) · Z1:`0` · Z2:`1` · Z3:`2` · Value:`3` | `"OPT_H2"` | Integer | 3 | Optional |

### Python 예제

```python
# 일반 보 단면 온도 분포 정의 (POST) — 단면 재료 자동 참조
btmp_general = {
    "Assign": {
        "51": {
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "Temp(+)",
                    "GROUP_NAME": "",
                    "DIR": "LZ",
                    "REF": "Centroid",
                    "NUM": 1,
                    "bPSC": False,
                    "vSECTTMP": [
                        {"TYPE": "ELEMENT", "VAL_B": 0.2, "VAL_H1": 0.1, "VAL_H2": 0.2, "VAL_T1": 3, "VAL_T2": 12.4}
                    ],
                }
            ]
        }
    }
}
midas_api("POST", "/db/BTMP", btmp_general)

# PSC/합성 단면 온도 분포 정의 (POST)
btmp_psc = {
    "Assign": {
        "56": {
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "Temp(-)",
                    "GROUP_NAME": "",
                    "DIR": "LZ",
                    "REF": "Top",
                    "NUM": 1,
                    "bPSC": True,
                    "vSECTTMP": [
                        {
                            "TYPE": "ELEMENT",
                            "REF": 0,
                            "OPT_B": 1, "VAL_B": 0.3,
                            "OPT_H1": 3, "VAL_H1": 0.2,
                            "OPT_H2": 3, "VAL_H2": 0.4,
                            "VAL_T1": 3, "VAL_T2": 12.4,
                        }
                    ],
                }
            ]
        }
    }
}
midas_api("POST", "/db/BTMP", btmp_psc)
```

---

## 4. /db/STMP — System Temperature

> 전체 구조물(시스템)에 균일한 온도 변화를 적용합니다. 키(key)는 **순번**이며, 하나의 항목에 하중 케이스와 온도값을 직접 기입합니다.

**Input URI:** `{base url}/db/STMP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "TEMPER": 12.5,
      "LCNAME": "Temp(+)",
      "GROUP_NAME": "LoadGroup1"
    },
    "2": {
      "TEMPER": -32.3,
      "LCNAME": "Temp(-)",
      "GROUP_NAME": "LoadGroup2"
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | - | Required |
| 2 | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| 3 | System Temperature | `"TEMPER"` | Number | 0 | Optional |

### Python 예제

```python
# 시스템 온도 하중 적용 (POST)
stmp_data = {
    "Assign": {
        "1": {"TEMPER": 12.5,  "LCNAME": "Temp(+)", "GROUP_NAME": ""},
        "2": {"TEMPER": -32.3, "LCNAME": "Temp(-)", "GROUP_NAME": ""},
    }
}
midas_api("POST", "/db/STMP", stmp_data)

# 조회 (GET)
midas_api("GET", "/db/STMP")

# 수정 (PUT)
midas_api("PUT", "/db/STMP", {
    "Assign": {"1": {"TEMPER": 15.0, "LCNAME": "Temp(+)", "GROUP_NAME": ""}}
})

# 삭제 (DELETE)
midas_api("DELETE", "/db/STMP", {"Assign": {"2": {}}})
```

---

## 5. /db/NTMP — Nodal Temperature

> 노드(Node)에 온도 하중을 직접 적용합니다. 키(key)는 **노드 번호**이며, `ITEMS` 배열로 여러 하중 케이스를 동시에 입력할 수 있습니다.

**Input URI:** `{base url}/db/NTMP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "190": {
      "ITEMS": [
        {"ID": 1, "LCNAME": "Temp(-)", "GROUP_NAME": "LoadGroup2", "TEMPER": -3},
        {"ID": 3, "LCNAME": "Temp(+)", "GROUP_NAME": "LoadGroup1", "TEMPER":  2}
      ]
    },
    "234": {
      "ITEMS": [
        {"ID": 1, "LCNAME": "Temp(-)", "GROUP_NAME": "LoadGroup2", "TEMPER": -5},
        {"ID": 3, "LCNAME": "Temp(+)", "GROUP_NAME": "LoadGroup1", "TEMPER":  3}
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Nodal Temperature (배열 오브젝트로 입력) | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Temperature | `"TEMPER"` | Number | - | Required |

### Python 예제

```python
# 노드 온도 하중 적용 (POST)
ntmp_data = {
    "Assign": {
        "190": {
            "ITEMS": [
                {"ID": 1, "LCNAME": "Temp(-)", "GROUP_NAME": "", "TEMPER": -3},
                {"ID": 2, "LCNAME": "Temp(+)", "GROUP_NAME": "", "TEMPER":  2},
            ]
        },
        "234": {
            "ITEMS": [
                {"ID": 1, "LCNAME": "Temp(-)", "GROUP_NAME": "", "TEMPER": -5},
                {"ID": 2, "LCNAME": "Temp(+)", "GROUP_NAME": "", "TEMPER":  3},
            ]
        },
    }
}
midas_api("POST", "/db/NTMP", ntmp_data)

# 조회 (GET)
midas_api("GET", "/db/NTMP")

# 삭제 (DELETE)
midas_api("DELETE", "/db/NTMP", {"Assign": {"190": {}}})
```

---

## 6. /db/TDNT — Tendon Property

> 텐던의 물성(재료 번호, 단면적, 이완 특성, 마찰 계수 등)을 정의합니다. 텐던 타입(INTERNAL/EXTERNAL)과 인장 방식(PRE/POST)에 따라 사용 가능한 파라미터가 달라집니다.

**Input URI:** `{base url}/db/TDNT`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

**Magura 이완 계수 예시 (내부/외부):**

```json
{
  "Assign": {
    "1": {
      "NAME": "In_Pre_Magura",
      "TYPE": "INTERNAL",
      "MATL": 1,
      "AREA": 0.00504,
      "D_AREA": 0.0152,
      "RM": 0,
      "RV": 45,
      "US": 1860000,
      "YS": 1570000,
      "LT": "PRE"
    },
    "2": {
      "NAME": "In_Post_Magura",
      "TYPE": "INTERNAL",
      "MATL": 1,
      "AREA": 0.00504,
      "D_AREA": 0.1,
      "RM": 0,
      "RV": 45,
      "US": 1860000,
      "YS": 1570000,
      "LT": "POST",
      "ASB": 0.006,
      "ASE": 0.006,
      "bBONDED": true,
      "FF": 0.3,
      "WF": 0.0066
    },
    "3": {
      "NAME": "Ext_Magura",
      "TYPE": "EXTERNAL",
      "MATL": 1,
      "AREA": 0.00504,
      "RM": 0,
      "RV": 10,
      "US": 1860000,
      "YS": 1570000,
      "ASB": 0.006,
      "ASE": 0.006,
      "ALPHA": 3000,
      "FF": 0.3
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Tendon Name | `"NAME"` | String | - | Required |
| 2 | Tendon Type · Internal: `"INTERNAL"` · External: `"EXTERNAL"` | `"TYPE"` | String | `"EXTERNAL"` | Optional |
| 3 | Tensioning Type · Post-Tension: `"POST"` · Pre-Tension: `"PRE"` · External: 미사용 | `"LT"` | String | `"PRE"` | Optional |
| 4 | Tendon Material No. | `"MATL"` | Integer | - | Required |
| 5 | Total Tendon Area | `"AREA"` | Number | - | Required |
| 6 | Diameter · Post: Duct 직경 · Pre: Strand 직경 · External: 미사용 | `"D_AREA"` | Number | - | Required |
| 7 | Anchorage Slip - Begin (Post/External 전용) | `"ASB"` | Number | 0 | Optional |
| 8 | Anchorage Slip - End (Post/External 전용) | `"ASE"` | Number | 0 | Optional |
| 9 | Bond Type (Post 전용) | `"bBONDED"` | Boolean | `false` | Optional |
| 10 | External Cable Moment Magnifier (External 전용) | `"ALPHA"` | Number | 0 | Optional |
| 11 | Relaxation Coefficient – Code ¹⁾ | `"RM"` | Integer | - | Required |
| 12 | Relaxation Coefficient – Factor ¹⁾ | `"RV"` | Integer | - | Required |
| 13 | Ultimate Strength | `"US"` | Number | 0 | Optional |
| 14 | Yield Strength | `"YS"` | Number | 0 | Optional |
| 15 | Curvature Friction Factor (Post/External 전용) | `"FF"` | Number | 0 | Optional |
| 16 | Wobble Friction Factor (Post 전용, Magura/IRC/KSCE/IRC112 코드) | `"WF"` | Number | 0 | Optional |
| 16 | Wobble Type (CEB-FIP/European 코드) · Fraction Factor: `0` · Unintentional Angular: `1` | `"W_TYPE"` | Integer | 0 | Optional |
| 17 | Wobble Fraction Factor (`W_TYPE`=0) | `"WF"` | Number | 0 | Optional |
| 17 | Unintentional Angular Disp. (`W_TYPE`=1) | `"W_ANGLE"` | Number | 0 | Optional |
| 18 | Relaxation Coefficient Class (CEB-FIP 2010 전용) | `"TDMFK"` | Integer | 1 | Optional |
| — | Relaxation Factor ξ (TB05/TB10092/Q-CR/AS/JTJ/JTG 코드) | `"FT"` | Number | - | Required |
| — | Low Relaxation (TB05/TB10092/Q-CR 코드) | `"LR"` | Boolean | `false` | Optional |
| — | Overstress Reduction Factor 적용 (TB05/TB10092/Q-CR/JTG 코드) | `"bOSRF"` | Boolean | `false` | Optional |
| — | Characteristic Strength fpk (TB05/TB10092/Q-CR/JTJ/JTG 코드) | `"FPK"` | Number | - | Required |
| — | Relaxation Function Name (User Defined) | `"TDMFNAME"` | String | - | Required |

> ¹⁾ **이완 계수 코드(RM) 및 인수(RV/FT/TDMFK) 표**

| Standard | RM | RV | FT | TDMFK |
|----------|----|----|-----|-------|
| Magura | `0` | `10` or `45` | - | - |
| IRC:18-2000 | `4` | Normal:`1` / Row:`2` | - | - |
| KSCE LSD15 | `6` | Ordinary:`1` / Low:`2` / Hot-rolled:`3` | - | - |
| IRC:112-2011 | `7` | Normal:`1` / Row:`2` | - | - |
| CEB-FIP 1978 | `1` | Number | - | - |
| European | `5` | Ordinary:`1` / Low:`2` / Hot-rolled:`3` | - | - |
| CEB-FIP 1990 | `8` | Number | - | - |
| CEB-FIP 2010 | `9` | Number | - | Class1-Slow:`1` / Class2-Mean:`2` / Class3-Rapid:`3` |
| TB05 | `3` | - | Number | - |
| TB10092-17 | `10` | - | Number | - |
| Q/CR 9300-18 | `12` | - | Number | - |
| AS 5100.5-2017 | `11` | - | Number | - |
| JTJ023-85 | `13` | - | Number | - |
| JTG18/JTG04 | `2` | - | `1` or `0.3` | - |
| User Defined | `100` | - | - | - |

### Python 예제

```python
# 텐던 물성 정의 (POST) — KSCE LSD15 기준, 내부 Post-Tension
tdnt_data = {
    "Assign": {
        "1": {
            "NAME": "T1_Post_KSCE",
            "TYPE": "INTERNAL",
            "MATL": 1,
            "AREA": 0.00504,     # 텐던 전체 면적 (m²)
            "D_AREA": 0.1,       # 덕트 직경 (m)
            "RM": 6,             # KSCE LSD15
            "RV": 2,             # Low relaxation
            "US": 1860000,       # 극한강도 (kN/m²)
            "YS": 1570000,       # 항복강도 (kN/m²)
            "LT": "POST",
            "ASB": 0.006,        # 시점 정착 활동량 (m)
            "ASE": 0.006,        # 종점 정착 활동량 (m)
            "bBONDED": True,     # 그라우팅(부착)
            "FF": 0.3,           # 곡률 마찰계수
            "WF": 0.0066,        # 파상 마찰계수
        }
    }
}
midas_api("POST", "/db/TDNT", tdnt_data)

# 조회 (GET)
midas_api("GET", "/db/TDNT")

# 삭제 (DELETE)
midas_api("DELETE", "/db/TDNT", {"Assign": {"1": {}}})
```

---

## 7. /db/TDNA — Tendon Profile

> 텐던의 배치 경로(프로파일)를 정의합니다. 2D/3D 및 Spline/Round 조합, 기준축 타입(Element/Straight/Curve)에 따라 입력 구조가 달라집니다.

**Input URI:** `{base url}/db/TDNA`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

**2D Spline 타입 (Element 기준):**

```json
{
  "Assign": {
    "1": {
      "NAME": "2D/Spline/Element",
      "TDN_PROP": 1,
      "ELEM": [1101, 1102, 1103, 1104, 1105],
      "BELENG": 0,
      "ELENG": 0,
      "CURVE": "SPLINE",
      "INPUT": "2D",
      "TDN_GRUP": 1,
      "LENG_OPT": "AUTO2",
      "bTP": false,
      "SHAPE": "ELEMENT",
      "INS_PT": "END-I",
      "INS_ELEM": 1101,
      "AXIS_IJ": "I-J",
      "XAR_ANGLE": 0,
      "bPJ": true,
      "OFF_YZ": [0, 0],
      "PROFY": [
        {"PT": [0, -0.5], "bFIX": true, "R": 0},
        {"PT": [15, -0.3], "bFIX": false, "R": 0},
        {"PT": [30, -0.5], "bFIX": true, "R": 0}
      ],
      "PROFZ": [
        {"PT": [0, -0.6], "bFIX": true, "R": 0, "bBOTZ": false},
        {"PT": [15, -0.3], "bFIX": false, "R": 0, "bBOTZ": false},
        {"PT": [30, -0.6], "bFIX": true, "R": 0, "bBOTZ": false}
      ]
    }
  }
}
```

**3D Spline 타입 (Element 기준):**

```json
{
  "Assign": {
    "3": {
      "NAME": "3D/Spline/Element",
      "TDN_PROP": 1,
      "ELEM": [1301, 1302, 1303, 1304, 1305],
      "BELENG": 0,
      "ELENG": 0,
      "CURVE": "SPLINE",
      "INPUT": "3D",
      "TDN_GRUP": 1,
      "LENG_OPT": "USER",
      "BLEN": 0,
      "ELEN": 0,
      "bTP": true,
      "CNT": 2,
      "DeBondBLEN": 1.2,
      "DeBondELEN": 1.2,
      "SHAPE": "ELEMENT",
      "INS_PT": "END-I",
      "INS_ELEM": 1301,
      "AXIS_IJ": "I-J",
      "XAR_ANGLE": 0,
      "bPJ": true,
      "OFF_YZ": [-0.5, 0],
      "PROF": [
        {"PT": [0, 0, -0.6], "bFIX": true, "R": [1.2, 1.2]},
        {"PT": [30, 0, -0.6], "bFIX": false, "R": [0, 0]}
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Tendon Name | `"NAME"` | String | - | Required |
| 2 | Tendon Group No. | `"TDN_GRUP"` | Integer | 0 | Optional |
| 3 | Tendon Property No. | `"TDN_PROP"` | Integer | - | Required |
| 4 | Assigned Elements No. | `"ELEM"` | Array \[Integer\] | - | Required |
| 5 | Input Type · 2D: `"2D"` · 3D: `"3D"` | `"INPUT"` | String | - | Required |
| 6 | Curve Type · Spline: `"SPLINE"` · Round: `"ROUND"` | `"CURVE"` | String | - | Required |
| 7 | Straight Length – Begin (Spline 전용) | `"BELENG"` | Number | 0 | Optional |
| 8 | Straight Length – End (Spline 전용) | `"ELENG"` | Number | 0 | Optional |
| 9 | Typical Tendon | `"bTP"` | Boolean | `false` | Optional |
| 10 | No. of Tendons (`bTP` = true 일 때 필수) | `"CNT"` | Number | - | Optional |
| 11 | Transfer Length Option · `"USER"` · `"AUTO1"` · `"AUTO2"` | `"LENG_OPT"` | String | - | Required |
| 12 | Transfer Length – Begin | `"BLEN"` | Number | 0 | Optional |
| 13 | Transfer Length – End | `"ELEN"` | Number | 0 | Optional |
| 14 | Debonded Length – Begin (Pre-tensioning 전용) | `"DeBondBLEN"` | Number | 0 | Optional |
| 15 | Debonded Length – End (Pre-tensioning 전용) | `"DeBondELEN"` | Number | 0 | Optional |
| 16 | Reference Axis · `"ELEMENT"` · `"STRAIGHT"` · `"CURVE"` | `"SHAPE"` | String | - | Required |

**SHAPE = "ELEMENT" 일 때 추가 파라미터:**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 17 | Profile Insertion Point · `"END-I"` · `"END-J"` | `"INS_PT"` | String | - | Required |
| 18 | Profile Insertion Point Element No. | `"INS_ELEM"` | Integer | - | Required |
| 19 | x Axis Direction · `"I-J"` · `"J-I"` | `"AXIS_IJ"` | String | `"I-J"` | Optional |
| 20 | x Axis Rotation Angle | `"XAR_ANGLE"` | Number | 0 | Optional |
| 21 | Projection | `"bPJ"` | Boolean | `false` | Optional |
| 22 | Offset (y, z) | `"OFF_YZ"` | Array \[Number, 2\] | `[0,0]` | Optional |

**SHAPE = "STRAIGHT" 일 때 추가 파라미터:**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 17 | Insertion Point \[x, y, z\] | `"IP"` | Array \[Number, 3\] | `[0,0,0]` | Optional |
| 18 | x Axis Direction · `"X"` · `"Y"` · `"VECTOR"` | `"AXIS"` | String | `"X"` | Optional |
| 19 | Vector \[x, y\] | `"VEC"` | Array \[Number, 2\] | `[0,0]` | Optional |
| 20 | x Axis Rotation Angle | `"XAR_ANGLE"` | Number | 0 | Optional |
| 21 | Projection | `"bPJ"` | Boolean | `false` | Optional |
| 22 | Grad. Rot. Angle Type · `"X"` · `"Y"` | `"GR_AXIS"` | String | `"Y"` | Optional |
| 23 | Grad. Rot. Angle | `"GR_ANGLE"` | Number | 0 | Optional |

**SHAPE = "CURVE" 일 때 추가 파라미터:**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 17 | Insertion Point \[x, y, z\] | `"IP"` | Array \[Number, 3\] | `[0,0,0]` | Optional |
| 18 | Radius Center (X, Y) | `"RC"` | Array \[Number, 2\] | 0 | Optional |
| 19 | Offset | `"OFFSET"` | Number | 0 | Optional |
| 20 | Direction · CW: `"CW"` · CCW: `"CCW"` | `"DIR"` | String | `"CW"` | Optional |
| 21 | x Axis Rotation Angle | `"XAR_ANGLE"` | Number | 0 | Optional |
| 22 | Grad. Rot. Angle Type · `"X"` · `"Y"` | `"GR_AXIS"` | String | `"Y"` | Optional |
| 23 | Grad. Rot. Angle | `"GR_ANGLE"` | Number | 0 | Optional |

**프로파일 좌표 (INPUT=2D):**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 24 | Profile in x-y plane | `"PROFY"` | Array \[Object\] | - | Required |
| (1) | Coordinates \[x, y\] | `"PT"` | Array \[Number, 2\] | - | Required |
| (2) | Fix Option (Spline) | `"bFIX"` | Boolean | `false` | Optional |
| (3) | Radius – degree (Spline) / length (Round) | `"R"` / `"RADIUS"` | Number | 0 | Optional |
| 25 | Profile in x-z plane | `"PROFZ"` | Array \[Object\] | - | Required |
| (1) | Coordinates \[x, y\] | `"PT"` | Array \[Number, 2\] | - | Required |
| (4) | BOT Option (ELEMENT 타입 전용) | `"bBOTZ"` | Boolean | `false` | Optional |

**프로파일 좌표 (INPUT=3D):**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 24 | 3D Profile | `"PROF"` | Array \[Object\] | - | Required |
| (1) | Coordinates \[x, y, z\] | `"PT"` | Array \[Number, 3\] | - | Required |
| (2) | Fix Option (Spline) | `"bFIX"` | Boolean | `false` | Optional |
| (3) | Radius – degree \[Ry, Rz\] (Spline) / length (Round) | `"R"` / `"RADIUS"` | Array or Number | 0 | Optional |

### Python 예제

```python
# 2D Spline 텐던 프로파일 정의 (POST) — Element 기준축
tdna_data = {
    "Assign": {
        "1": {
            "NAME": "T1_Profile_2D",
            "TDN_PROP": 1,          # TDNT에서 정의한 텐던 물성 번호
            "ELEM": [101, 102, 103, 104, 105],  # 배치 요소 목록
            "BELENG": 0,
            "ELENG": 0,
            "CURVE": "SPLINE",
            "INPUT": "2D",
            "TDN_GRUP": 1,
            "LENG_OPT": "AUTO2",
            "bTP": False,
            "SHAPE": "ELEMENT",
            "INS_PT": "END-I",
            "INS_ELEM": 101,
            "AXIS_IJ": "I-J",
            "XAR_ANGLE": 0,
            "bPJ": True,
            "OFF_YZ": [0, 0],
            "PROFY": [
                {"PT": [0,  -0.5], "bFIX": True,  "R": 0},
                {"PT": [15, -0.3], "bFIX": False, "R": 0},
                {"PT": [30, -0.5], "bFIX": True,  "R": 0},
            ],
            "PROFZ": [
                {"PT": [0,  -0.6], "bFIX": True,  "R": 0, "bBOTZ": False},
                {"PT": [15, -0.3], "bFIX": False, "R": 0, "bBOTZ": False},
                {"PT": [30, -0.6], "bFIX": True,  "R": 0, "bBOTZ": False},
            ],
        }
    }
}
midas_api("POST", "/db/TDNA", tdna_data)

# 조회 (GET)
midas_api("GET", "/db/TDNA")
```

---

## 8. /db/TDCS — Tendon Location for Composite Section

> 합성 단면(Construction Stage)에서 텐던 프로파일이 속하는 파트 번호를 지정합니다.

**Input URI:** `{base url}/db/TDCS`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "TDNA": 1,
      "CSCS": 1,
      "PART_NUM": 1
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Tendon Profile No. | `"TDNA"` | Integer | - | Required |
| 2 | Composite Section for Construction Stage No. | `"CSCS"` | Integer | - | Required |
| 3 | Part Number | `"PART_NUM"` | Integer | - | Required |

### Python 예제

```python
# 합성 단면 텐던 위치 지정 (POST)
tdcs_data = {
    "Assign": {
        "1": {
            "TDNA": 1,       # 텐던 프로파일 번호 (TDNA)
            "CSCS": 1,       # 시공단계 합성 단면 번호
            "PART_NUM": 1,   # 파트 번호
        }
    }
}
midas_api("POST", "/db/TDCS", tdcs_data)

# 조회 (GET)
midas_api("GET", "/db/TDCS")

# 삭제 (DELETE)
midas_api("DELETE", "/db/TDCS", {"Assign": {"1": {}}})
```

---

## 9. /db/TDPL — Tendon Prestress

> 텐던 프로파일에 프리스트레스 하중을 적용합니다. 키(key)는 **텐던 프로파일 번호(TDNA)**이며, 인장력 또는 응력값으로 입력합니다.

**Input URI:** `{base url}/db/TDPL`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "2": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PS",
          "GROUP_NAME": "LoadGroup",
          "TENDON_NAME": "2D/Round/Element",
          "TYPE": "FORCE",
          "ORDER": "BOTH",
          "BEGIN": 1360000,
          "END": 1360000,
          "GROUTING": 1
        }
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Tendon Prestress (배열 오브젝트로 입력) | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Tendon Profile Name | `"TENDON_NAME"` | String | - | Required |
| (5) | Prestress Load Type · Stress: `"STRESS"` · Force: `"FORCE"` | `"TYPE"` | String | `"STRESS"` | Optional |
| (6) | Jacking Step · Begin: `"BEGIN"` · End: `"END"` · Both: `"BOTH"` | `"ORDER"` | String | `"BEGIN"` | Optional |
| (7) | Jacking Force / Stress at Begin | `"BEGIN"` | Number | - | Required |
| (8) | Jacking Force / Stress at End | `"END"` | Number | - | Required |
| (9) | Grouting Stage | `"GROUTING"` | Integer | 0 | Optional |

### Python 예제

```python
# 텐던 프리스트레스 적용 (POST)
tdpl_data = {
    "Assign": {
        "1": {   # 텐던 프로파일 1번 (TDNA 번호)
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "PS",
                    "GROUP_NAME": "",
                    "TENDON_NAME": "T1_Profile_2D",  # TDNA에서 정의한 이름
                    "TYPE": "FORCE",     # 인장력으로 입력
                    "ORDER": "BOTH",     # 시점·종점 동시 인장
                    "BEGIN": 1360000,    # 시점 인장력 (kN/m²)
                    "END": 1360000,      # 종점 인장력
                    "GROUTING": 1,       # 그라우팅 시공단계
                }
            ]
        }
    }
}
midas_api("POST", "/db/TDPL", tdpl_data)

# 조회 (GET)
midas_api("GET", "/db/TDPL")

# 삭제 (DELETE)
midas_api("DELETE", "/db/TDPL", {"Assign": {"1": {}}})
```

---

## 10. /db/PRST — Prestress Beam Loads

> 보 요소에 직접 프리스트레스 하중을 적용합니다 (텐던 프로파일 불필요). 키(key)는 **요소 번호**입니다.

**Input URI:** `{base url}/db/PRST`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1101": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PS",
          "GROUP_NAME": "LoadGroup",
          "DIR": 1,
          "TENSION": 1360,
          "DISTANCE_I": 0.2,
          "DISTANCE_M": 0.3,
          "DISTANCE_J": 0.4
        }
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Prestress Beam Loads (배열 오브젝트로 입력) | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Direction · Local y: `0` · Local z: `1` | `"DIR"` | Integer | 0 | Optional |
| (5) | Tension | `"TENSION"` | Number | - | Required |
| (6) | Distance – I (Di) | `"DISTANCE_I"` | Number | 0 | Optional |
| (7) | Distance – M (Dm) | `"DISTANCE_M"` | Number | 0 | Optional |
| (8) | Distance – J (Dj) | `"DISTANCE_J"` | Number | 0 | Optional |

### Python 예제

```python
# 보 프리스트레스 하중 적용 (POST)
prst_data = {
    "Assign": {
        "1101": {   # 요소 1101번
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "PS",
                    "GROUP_NAME": "",
                    "DIR": 1,             # Local z 방향
                    "TENSION": 1360,      # 인장력
                    "DISTANCE_I": 0.2,    # i단 편심거리 (m)
                    "DISTANCE_M": 0.3,    # 중앙 편심거리 (m)
                    "DISTANCE_J": 0.4,    # j단 편심거리 (m)
                }
            ]
        },
        "1102": {
            "ITEMS": [
                {"ID": 1, "LCNAME": "PS", "GROUP_NAME": "", "DIR": 1,
                 "TENSION": 1360, "DISTANCE_I": 0.2, "DISTANCE_M": 0.3, "DISTANCE_J": 0.4}
            ]
        },
    }
}
midas_api("POST", "/db/PRST", prst_data)

# 조회 (GET)
midas_api("GET", "/db/PRST")

# 삭제 (DELETE)
midas_api("DELETE", "/db/PRST", {"Assign": {"1101": {}}})
```

---

## 11. /db/PTNS — Pretension Loads

> 트러스/케이블 요소에 프리텐션(초기 인장력)을 부가합니다. 키(key)는 **요소 번호**입니다.

**Input URI:** `{base url}/db/PTNS`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "3431": {
      "ITEMS": [
        {"ID": 1, "LCNAME": "PrS1", "GROUP_NAME": "LoadGroup", "TENSION": 130}
      ]
    },
    "3432": {
      "ITEMS": [
        {"ID": 1, "LCNAME": "PrS1", "GROUP_NAME": "LoadGroup", "TENSION": 130}
      ]
    },
    "3433": {
      "ITEMS": [
        {"ID": 1, "LCNAME": "PrS2", "GROUP_NAME": "LoadGroup", "TENSION": 130}
      ]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Pretension Loads (배열 오브젝트로 입력) | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Pretension Load | `"TENSION"` | Number | - | Required |

### Python 예제

```python
# 프리텐션 하중 적용 (POST)
# 하중 케이스 PrS1은 EXLD에서 External Type으로 별도 지정 필요
ptns_data = {
    "Assign": {
        "3431": {
            "ITEMS": [{"ID": 1, "LCNAME": "PrS1", "GROUP_NAME": "", "TENSION": 130}]
        },
        "3432": {
            "ITEMS": [{"ID": 1, "LCNAME": "PrS1", "GROUP_NAME": "", "TENSION": 130}]
        },
        "3433": {
            "ITEMS": [{"ID": 1, "LCNAME": "PrS2", "GROUP_NAME": "", "TENSION": 130}]
        },
    }
}
midas_api("POST", "/db/PTNS", ptns_data)

# 조회 (GET)
midas_api("GET", "/db/PTNS")

# 삭제 (DELETE)
midas_api("DELETE", "/db/PTNS", {"Assign": {"3431": {}}})
```

---

## 12. /db/EXLD — External Type Load Case for Pretension

> 프리텐션 하중에 사용할 하중 케이스를 External Type으로 지정합니다. PTNS에서 참조하는 하중 케이스명을 이 엔드포인트에 등록해야 합니다.

**Input URI:** `{base url}/db/EXLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 요청 바디 구조

```json
{
  "Assign": {
    "1": {
      "LCNAME_ITEM": ["PrS1", "PrS2"]
    }
  }
}
```

### 파라미터

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name (프리텐션 하중이 있는 케이스만 입력) | `"LCNAME_ITEM"` | Array \[String\] | - | Required |

### Python 예제

```python
# 프리텐션용 External Type 하중 케이스 등록 (POST)
# STLD에서 TYPE="PS" 등으로 정의된 케이스 중 프리텐션 케이스를 여기 등록
exld_data = {
    "Assign": {
        "1": {
            "LCNAME_ITEM": ["PrS1", "PrS2"]  # PTNS에서 사용한 하중 케이스명
        }
    }
}
midas_api("POST", "/db/EXLD", exld_data)

# 조회 (GET)
midas_api("GET", "/db/EXLD")

# 수정 (PUT) — 하중 케이스 추가
midas_api("PUT", "/db/EXLD", {
    "Assign": {"1": {"LCNAME_ITEM": ["PrS1", "PrS2", "PrS3"]}}
})

# 삭제 (DELETE)
midas_api("DELETE", "/db/EXLD", {"Assign": {"1": {}}})
```

---

## 워크플로우 예제 — 프리스트레스트 콘크리트 보 모델링

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY_HERE"

def midas_api(method, endpoint, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    r = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{r.status_code}] {method.upper()} {endpoint}")
    return r.json() if r.text else {}

# 1단계: 정적 하중 케이스 생성 (STLD 참조)
midas_api("POST", "/db/STLD", {
    "Assign": {
        "1": {"NAME": "PS",    "TYPE": "PS",  "DESC": "Prestress"},
        "2": {"NAME": "Temp+", "TYPE": "T",   "DESC": "Temperature +"},
        "3": {"NAME": "PrS1",  "TYPE": "PS",  "DESC": "Pretension LC1"},
    }
})

# 2단계: 온도 하중 적용
midas_api("POST", "/db/ETMP", {
    "Assign": {
        "1": {"ITEMS": [{"ID": 1, "LCNAME": "Temp+", "GROUP_NAME": "", "TEMP": 25}]}
    }
})

# 3단계: 텐던 물성 정의
midas_api("POST", "/db/TDNT", {
    "Assign": {
        "1": {
            "NAME": "TD1_KSCE",
            "TYPE": "INTERNAL",
            "MATL": 1,
            "AREA": 0.00504,
            "D_AREA": 0.1,
            "RM": 6,         # KSCE LSD15
            "RV": 2,         # Low relaxation
            "US": 1860000,
            "YS": 1570000,
            "LT": "POST",
            "ASB": 0.006,
            "ASE": 0.006,
            "bBONDED": True,
            "FF": 0.3,
            "WF": 0.0066,
        }
    }
})

# 4단계: 텐던 프로파일 정의
midas_api("POST", "/db/TDNA", {
    "Assign": {
        "1": {
            "NAME": "TD1_Profile",
            "TDN_PROP": 1,
            "ELEM": [101, 102, 103, 104, 105],
            "BELENG": 0, "ELENG": 0,
            "CURVE": "SPLINE", "INPUT": "2D",
            "TDN_GRUP": 1, "LENG_OPT": "AUTO2",
            "bTP": False, "SHAPE": "ELEMENT",
            "INS_PT": "END-I", "INS_ELEM": 101,
            "AXIS_IJ": "I-J", "XAR_ANGLE": 0,
            "bPJ": True, "OFF_YZ": [0, 0],
            "PROFY": [
                {"PT": [0,  0],    "bFIX": True,  "R": 0},
                {"PT": [12, -0.5], "bFIX": False, "R": 0},
                {"PT": [24, 0],    "bFIX": True,  "R": 0},
            ],
            "PROFZ": [
                {"PT": [0,  -0.5], "bFIX": True,  "R": 0, "bBOTZ": False},
                {"PT": [12, -0.05],"bFIX": False, "R": 0, "bBOTZ": False},
                {"PT": [24, -0.5], "bFIX": True,  "R": 0, "bBOTZ": False},
            ],
        }
    }
})

# 5단계: 텐던 프리스트레스 하중 적용
midas_api("POST", "/db/TDPL", {
    "Assign": {
        "1": {
            "ITEMS": [{
                "ID": 1,
                "LCNAME": "PS",
                "GROUP_NAME": "",
                "TENDON_NAME": "TD1_Profile",
                "TYPE": "FORCE",
                "ORDER": "BOTH",
                "BEGIN": 1360000,
                "END": 1360000,
                "GROUTING": 1,
            }]
        }
    }
})

# 6단계: 프리텐션 External Type 등록 (필요 시)
midas_api("POST", "/db/EXLD", {
    "Assign": {"1": {"LCNAME_ITEM": ["PrS1"]}}
})

print("PSC 보 프리스트레스 하중 정의 완료")
```
