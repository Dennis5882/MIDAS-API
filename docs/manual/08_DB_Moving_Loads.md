# DB – Moving Loads

> **대상 제품:** MIDAS Civil NX (이동하중은 Civil NX 전용)
> **Base URL:** `https://moa-engineers.midasit.com:443/civil`
> **인증:** 모든 요청에 `MAPI-Key: <key>` 헤더 필수
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> ⚠️ **이 섹션의 모든 엔드포인트는 MIDAS Civil NX 전용입니다.**

---

## 목차

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | [/db/MVCD](#1-dbmvcd--moving-load-code) | Moving Load Code |
| 2 | [/db/LLAN](#2-dbllan--traffic-line-lanes) | Traffic Line Lanes |
| 3 | [/db/LLANch](#3-dbllanch--traffic-line-lanes--china) | Traffic Line Lanes – China |
| 4 | [/db/LLANid](#4-dbllanid--traffic-line-lanes--india) | Traffic Line Lanes – India |
| 5 | [/db/LLANtr](#5-dbllantr--traffic-line-lanes--transverse) | Traffic Line Lanes – Transverse |
| 6 | [/db/LLANop](#6-dbllanop--traffic-line-lanes--moving-load-optimization) | Traffic Line Lanes – Moving Load Optimization |
| 7 | [/db/SLAN](#7-dbslan--traffic-surface-lanes) | Traffic Surface Lanes |
| 8 | [/db/SLANch](#8-dbslanch--traffic-surface-lanes--china) | Traffic Surface Lanes – China |
| 9 | [/db/SLANop](#9-dbslanop--traffic-surface-lanes--moving-load-optimization) | Traffic Surface Lanes – Moving Load Optimization |
| 10 | [/db/MVHL](#10-dbmvhl--vehicles) | Vehicles (AASHTO / LRFD / Canada / BS / Eurocode / Korea 등) |
| 11 | [/db/MVHLtr](#11-dbmvhltr--vehicles--transverse) | Vehicles – Transverse |
| 12 | [/db/MVLD](#12-dbmvld--moving-load-cases) | Moving Load Cases |
| 13 | [/db/MVLDch](#13-dbmvldch--moving-load-cases--china) | Moving Load Cases – China |
| 14 | [/db/MVLDid](#14-dbmvldid--moving-load-cases--india) | Moving Load Cases – India |
| 15 | [/db/MVLDbs](#15-dbmvldbs--moving-load-cases--bs) | Moving Load Cases – BS |
| 16 | [/db/MVLDeu](#16-dbmvldeu--moving-load-cases--eurocode) | Moving Load Cases – Eurocode |
| 17 | [/db/MVLDpl](#17-dbmvldpl--moving-load-cases--poland) | Moving Load Cases – Poland |
| 18 | [/db/MVLDtr](#18-dbmvldtr--moving-load-cases--transverse) | Moving Load Cases – Transverse |
| 19 | [/db/CRGR](#19-dbcrgr--concurrent-reaction-group) | Concurrent Reaction Group |
| 20 | [/db/CJFG](#20-dbcjfg--concurrent-joint-force-group) | Concurrent Joint Force Group |
| 21 | [/db/MVHC](#21-dbmvhc--vehicle-classes) | Vehicle Classes |
| 22 | [/db/SINF](#22-dbsinf--plate-element-for-influence-surface) | Plate Element for Influence Surface |
| 23 | [/db/MLSP](#23-dbmlsp--lane-support--negative-moments-at-interior-piers) | Lane Support – Negative Moments at Interior Piers |
| 24 | [/db/MLSR](#24-dbmlsr--lane-support--reactions-at-interior-piers) | Lane Support – Reactions at Interior Piers |
| 25 | [/db/DYLA](#25-dbdyla--dynamic-load-allowance) | Dynamic Load Allowance |
| 26 | [/db/IMPF](#26-dbimpf--additional-impact-factor) | Additional Impact Factor |
| 27 | [/db/DYFG](#27-dbdyfg--railway-dynamic-factor) | Railway Dynamic Factor |
| 28 | [/db/DYNF](#28-dbdynf--railway-dynamic-factor-by-element) | Railway Dynamic Factor by Element |

---

## 공통 Python 헬퍼

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "<YOUR_MAPI_KEY>",
}

def mv_get(endpoint: str) -> dict:
    res = requests.get(f"{BASE_URL}/db/{endpoint}", headers=HEADERS)
    res.raise_for_status()
    return res.json()

def mv_post(endpoint: str, assign: dict) -> dict:
    body = {"Assign": assign}
    res = requests.post(f"{BASE_URL}/db/{endpoint}", headers=HEADERS, json=body)
    res.raise_for_status()
    return res.json()

def mv_put(endpoint: str, assign: dict) -> dict:
    body = {"Assign": assign}
    res = requests.put(f"{BASE_URL}/db/{endpoint}", headers=HEADERS, json=body)
    res.raise_for_status()
    return res.json()

def mv_delete(endpoint: str, keys: list) -> dict:
    body = {"Assign": {k: {} for k in keys}}
    res = requests.delete(f"{BASE_URL}/db/{endpoint}", headers=HEADERS, json=body)
    res.raise_for_status()
    return res.json()
```

---

## 1. /db/MVCD – Moving Load Code

> 이동하중 해석에 사용할 설계 기준 코드를 설정합니다.

**Input URI:** `{base url}/db/MVCD`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "CODE": "KSCE-LSD15"
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Moving Load Code ¹⁾ | `"CODE"` | String | – | Required |

**¹⁾ Moving Load Code 값표**

| 기준 코드 | CODE 값 |
|-----------|---------|
| KSCE-LSD15 (한국) | `"KSCE-LSD15"` |
| Korea (KS-RB / KS2005) | `"KOREA"` |
| AASHTO Standard | `"AASHTO STANDARD"` |
| AASHTO LRFD | `"AASHTO LRFD"` |
| PENNDOT | `"AASHTO LRFD(PENDOT)"` |
| China | `"CHINA"` |
| India | `"INDIA"` |
| Taiwan | `"TAIWAN"` |
| Canada | `"CANADA"` |
| BS | `"BS"` |
| Eurocode | `"EUROCODE"` |
| Australia | `"AUSTRALIA"` |
| Poland | `"POLAND"` |
| Russia | `"RUSSIA"` |
| South Africa | `"SOUTH AFRICA"` |
| Transverse | `"TRANS"` |

### Python 예제

```python
# 이동하중 코드를 KSCE-LSD15로 설정
result = mv_post("MVCD", {
    "1": {"CODE": "KSCE-LSD15"}
})
print(result)
```

---

## 2. /db/LLAN – Traffic Line Lanes

> 교량 거더 요소(Beam Element) 기반의 차선 이동 경로를 정의합니다.

**Input URI:** `{base url}/db/LLAN`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "FORWARD",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 3,
        "OPT_AUTO_LANE": true,
        "ALLOW_WIDTH": 3
      },
      "LANE_ITEMS": [
        {"ELEM": 1, "ECC": -1.5},
        {"ELEM": 2, "ECC": -1.5},
        {"ELEM": 3, "ECC": -1.5}
      ]
    }
  }
}
```

### Parameters – COMMON

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Name of Line Lane | `"LL_NAME"` | String | – | Required |
| 2 | Lane Width ¹⁾ | `"WIDTH"` | Number | – | Required |
| 3 | Wheel Spacing | `"WHEEL_SPACE"` | Number | 0 | Optional |
| 4 | Transverse Lane Optimization ²⁾ | `"OPT_AUTO_LANE"` | Boolean | false | Optional |
| 5 | Allow Width for Optimization ²⁾ | `"ALLOW_WIDTH"` | Number | – | Optional |
| 6 | Load Distribution (`"LANE"` / `"CROSS"`) | `"LOAD_DIST"` | String | – | Required |
| 7 | Name of Structure Group ³⁾ | `"GROUP_NAME"` | String | `""` | Optional |
| 8 | Skew Start ³⁾ | `"SKEW_START"` | Number | 0 | Optional |
| 9 | Skew End ³⁾ | `"SKEW_END"` | Number | 0 | Optional |
| 10 | Moving Direction (`"FORWARD"` / `"BACKWARD"` / `"BOTH"`) | `"MOVING"` | String | – | Required |

> ¹⁾ Eurocode, Australia, Poland, BS, Russia, South Africa에서만 유효  
> ²⁾ Taiwan에서는 사용 불가  
> ³⁾ Load Distribution이 Cross Beam인 경우에만 사용

### Parameters – LANE_ITEMS (코드별 추가 필드)

| 코드 | 추가 Key | 설명 |
|------|----------|------|
| KSCE-LSD15, Canada, BS, Russia, South Africa | `"ECC"` | Eccentricity (Optional) |
| Korea, AASHTO Standard, Taiwan | `"ECC"`, `"FACT"`, `"SPAN_START"` | ECC·충격계수·경간시작 |
| AASHTO LRFD | `"ECC"`, `"SPAN_START"`, `"CENT_F"` | ECC·경간시작·원심력계수 |
| PENNDOT | `"ECC"`, `"SPAN_START"` | ECC·경간시작 |
| Eurocode | `"ECC"`, `"ECCEN_VERT_LOAD"` | ECC·캔트 고려 수직편심 |
| Australia, Poland | `"ECC"`, `"SPAN_START"` | ECC·경간시작 |

### Python 예제

```python
# KSCE-LSD15 기준 차선 정의 (Lane Element 방식)
result = mv_post("LLAN", {
    "1": {
        "COMMON": {
            "LL_NAME": "LL_01",
            "LOAD_DIST": "LANE",
            "GROUP_NAME": "",
            "SKEW_START": 0,
            "SKEW_END": 0,
            "MOVING": "FORWARD",
            "WHEEL_SPACE": 1.8,
            "WIDTH": 3,
            "OPT_AUTO_LANE": True,
            "ALLOW_WIDTH": 3,
        },
        "LANE_ITEMS": [
            {"ELEM": 1, "ECC": -1.5},
            {"ELEM": 2, "ECC": -1.5},
            {"ELEM": 3, "ECC": -1.5},
        ],
    },
    "2": {
        "COMMON": {
            "LL_NAME": "LL_02",
            "LOAD_DIST": "CROSS",
            "GROUP_NAME": "CrossBeam",
            "SKEW_START": 10,
            "SKEW_END": 10,
            "MOVING": "BOTH",
            "WHEEL_SPACE": 1.8,
            "WIDTH": 3,
            "OPT_AUTO_LANE": True,
            "ALLOW_WIDTH": 3,
        },
        "LANE_ITEMS": [
            {"ELEM": 163, "ECC": -1.5},
            {"ELEM": 164, "ECC": -1.5},
            {"ELEM": 165, "ECC": -1.55},
        ],
    },
})
print(result)
```

---

## 3. /db/LLANch – Traffic Line Lanes – China

> China 기준 차선 이동 경로. 중국 도시교량·고속도로교 충격계수를 별도 지정합니다.

**Input URI:** `{base url}/db/LLANch`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "BOTH",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 3,
        "OPT_AUTO_LANE": true,
        "ALLOW_WIDTH": 3
      },
      "LANE_ITEMS": [
        {"ELEM": 1, "ECC": -1.5, "SPAN": 12, "SPAN_START": true, "SCALE_FACTOR": 1.1}
      ]
    }
  }
}
```

### Parameters – COMMON

LLAN COMMON과 동일 구조 (`"LL_NAME"`, `"LOAD_DIST"`, `"MOVING"` 등)

### Parameters – LANE_ITEMS

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Element No. | `"ELEM"` | Integer | – | Required |
| 2 | Eccentricity | `"ECC"` | Number | 0 | Optional |
| 3 | Span Length | `"SPAN"` | Number | 0 | Optional |
| 4 | Span Start | `"SPAN_START"` | Boolean | false | Optional |
| 5 | Scale Factor | `"SCALE_FACTOR"` | Number | 0 | Optional |

### Python 예제

```python
result = mv_post("LLANch", {
    "1": {
        "COMMON": {
            "LL_NAME": "LL_01",
            "LOAD_DIST": "LANE",
            "GROUP_NAME": "",
            "SKEW_START": 0,
            "SKEW_END": 0,
            "MOVING": "BOTH",
            "WHEEL_SPACE": 1.8,
            "WIDTH": 3,
            "OPT_AUTO_LANE": True,
            "ALLOW_WIDTH": 3,
        },
        "LANE_ITEMS": [
            {"ELEM": 1,   "ECC": -1.5, "SPAN": 12, "SPAN_START": True,  "SCALE_FACTOR": 1.1},
            {"ELEM": 2,   "ECC": -1.5, "SPAN": 12, "SPAN_START": False, "SCALE_FACTOR": 1.1},
            {"ELEM": 3,   "ECC": -1.5, "SPAN": 12, "SPAN_START": False, "SCALE_FACTOR": 1.1},
        ],
    }
})
print(result)
```

---

## 4. /db/LLANid – Traffic Line Lanes – India

> India (IRC) 기준 차선. IF/CDA 또는 경간 길이 방식으로 충격계수를 지정합니다.

**Input URI:** `{base url}/db/LLANid`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "BOTH",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 0,
        "OPT_AUTO_LANE": false,
        "ALLOW_WIDTH": 0
      },
      "LANE_ITEMS": [
        {"ELEM": 1, "ECC": -1.5, "SPAN": 12, "IMPACT_SPAN": 1, "IMPACT_FACTOR": 0}
      ]
    }
  }
}
```

### Parameters – LANE_ITEMS

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Element No. | `"ELEM"` | Integer | – | Required |
| 2 | Eccentricity | `"ECC"` | Number | 0 | Optional |
| 3 | Option (0=IF/CDA, 1=Span Length) | `"IMPACT_SPAN"` | Integer | 0 | Optional |
| 4 | Scale Factor (when IMPACT_SPAN=0) | `"IMPACT_FACTOR"` | Number | 0 | Optional |
| 5 | Span Length (when IMPACT_SPAN=1) | `"SPAN"` | Number | 0 | Optional |

### Python 예제

```python
result = mv_post("LLANid", {
    "1": {
        "COMMON": {
            "LL_NAME": "LL_01",
            "LOAD_DIST": "LANE",
            "GROUP_NAME": "",
            "SKEW_START": 0,
            "SKEW_END": 0,
            "MOVING": "BOTH",
            "WHEEL_SPACE": 1.8,
            "WIDTH": 0,
            "OPT_AUTO_LANE": False,
            "ALLOW_WIDTH": 0,
        },
        "LANE_ITEMS": [
            {"ELEM": 1, "ECC": -1.5, "SPAN": 12, "IMPACT_SPAN": 1, "IMPACT_FACTOR": 0},
            {"ELEM": 2, "ECC": -1.5, "SPAN": 12, "IMPACT_SPAN": 1, "IMPACT_FACTOR": 0},
        ],
    }
})
print(result)
```

---

## 5. /db/LLANtr – Traffic Line Lanes – Transverse

> Transverse 이동하중 코드용 차선. 요소별 하중 계수만 정의합니다.

**Input URI:** `{base url}/db/LLANtr`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LL_NAME": "LL_01",
      "LANE_ITEMS": [
        {"ELEM": 1, "FACTOR": 1.1},
        {"ELEM": 2, "FACTOR": 1.1},
        {"ELEM": 3, "FACTOR": 1.1}
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Name of Line Lane | `"LL_NAME"` | String | – | Required |
| 2 | Lane Items | `"LANE_ITEMS"` | Array[Object] | – | Required |
| (1) | Element ID | `"ELEM"` | Integer | – | Required |
| (2) | Factor | `"FACTOR"` | Number | – | Required |

### Python 예제

```python
result = mv_post("LLANtr", {
    "1": {
        "LL_NAME": "LL_01",
        "LANE_ITEMS": [
            {"ELEM": 1, "FACTOR": 1.1},
            {"ELEM": 2, "FACTOR": 1.1},
            {"ELEM": 3, "FACTOR": 1.1},
        ],
    }
})
print(result)
```

---

## 6. /db/LLANop – Traffic Line Lanes – Moving Load Optimization

> 이동하중 최적화(Moving Load Optimization) 전용 차선 정의.  
> 차선 폭 내 최적 위치를 자동 탐색합니다.

**Input URI:** `{base url}/db/LLANop`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LL_NAME": "LL_01",
      "LOAD_DIST": "LANE",
      "GROUP_NAME": "",
      "SKEW_START": 0,
      "SKEW_END": 0,
      "MOVING": "BOTH",
      "OPTIM_WIDTH": 5,
      "LANE_WIDTH": 3,
      "OFFSET_TYPE": 0,
      "DIVIDE_NUM": 2,
      "ANAL_LANE_OFFSET": 1,
      "WHEEL_SPACE": 1.8288,
      "MARGIN": 0.1,
      "LANE_ITEMS": [
        {"ELEM": 1, "ECC": -1.5, "FACT": 1.25, "SPAN_START": true},
        {"ELEM": 2, "ECC": -1.5, "FACT": 1.25, "SPAN_START": false}
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Name of Line Lane | `"LL_NAME"` | String | – | Required |
| 2 | Load Distribution (`"LANE"` / `"CROSS"`) | `"LOAD_DIST"` | String | – | Required |
| 3 | Structure Group Name | `"GROUP_NAME"` | String | `""` | Optional |
| 4 | Skew Start | `"SKEW_START"` | Number | 0 | Optional |
| 5 | Skew End | `"SKEW_END"` | Number | 0 | Optional |
| 6 | Moving Direction | `"MOVING"` | String | – | Required |
| 7 | Optimization Width | `"OPTIM_WIDTH"` | Number | – | Required |
| 8 | Lane Width | `"LANE_WIDTH"` | Number | – | Required |
| 9 | Offset Type (0=Fixed, 1=Division) | `"OFFSET_TYPE"` | Integer | – | Required |
| 10 | Number of Division | `"DIVIDE_NUM"` | Integer | – | Optional |
| 11 | Analysis Lane Offset | `"ANAL_LANE_OFFSET"` | Number | – | Optional |
| 12 | Wheel Spacing | `"WHEEL_SPACE"` | Number | 0 | Optional |
| 13 | Margin | `"MARGIN"` | Number | 0 | Optional |
| 14 | Lane Items (ELEM, ECC, 코드별 추가 필드) | `"LANE_ITEMS"` | Array[Object] | – | Required |

### Python 예제

```python
result = mv_post("LLANop", {
    "1": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "BOTH",
        "OPTIM_WIDTH": 5,
        "LANE_WIDTH": 3,
        "OFFSET_TYPE": 0,
        "DIVIDE_NUM": 2,
        "ANAL_LANE_OFFSET": 1,
        "WHEEL_SPACE": 1.8288,
        "MARGIN": 0.1,
        "LANE_ITEMS": [
            {"ELEM": 1, "ECC": -1.5, "SPAN_START": True, "CENT_F": 0.5},
            {"ELEM": 2, "ECC": -1.5, "SPAN_START": False, "CENT_F": 0.5},
        ],
    }
})
print(result)
```

---

## 7. /db/SLAN – Traffic Surface Lanes

> 판요소(Plate Element) 기반 면 차선 이동 경로. 노드 기준으로 차선 경로를 정의합니다.

**Input URI:** `{base url}/db/SLAN`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "LL_01",
      "WIDTH": 3,
      "WHEEL_SPACE": 1.8,
      "SKEW_START": 10,
      "SKEW_END": 15,
      "bOPTIMIZE": true,
      "ALLOW_WIDTH": 3,
      "MV_DIR": "BOTH",
      "LANE_ITEMS": [
        {"NODE": 1, "OFFSET": -1.5},
        {"NODE": 2, "OFFSET": -1.5},
        {"NODE": 3, "OFFSET": -1.5},
        {"NODE": 4, "OFFSET": -1.5}
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Name of Surface Lane | `"NAME"` | String | – | Required |
| 2 | Lane Width | `"WIDTH"` | Number | – | Required |
| 3 | Wheel Spacing | `"WHEEL_SPACE"` | Number | 0 | Optional |
| 4 | Skew Start | `"SKEW_START"` | Number | 0 | Optional |
| 5 | Skew End | `"SKEW_END"` | Number | 0 | Optional |
| 6 | Transverse Lane Optimization ¹⁾ | `"bOPTIMIZE"` | Boolean | false | Optional |
| 7 | Allow Width for Optimization ¹⁾ | `"ALLOW_WIDTH"` | Number | 0 | Optional |
| 8 | Moving Direction (`"FORWARD"` / `"BACKWARD"` / `"BOTH"`) | `"MV_DIR"` | String | – | Required |
| 9 | Sequence Number (Unique) | `"SEQ"` | Integer | 1 | Optional |
| 10 | Lane Items | `"LANE_ITEMS"` | Array[Object] | – | Required |

> ¹⁾ India, Taiwan에서는 사용 불가

### Parameters – LANE_ITEMS (코드별 추가 필드)

| 코드 | 추가 Key | 설명 |
|------|----------|------|
| KSCE-LSD15, Canada, BS, Russia, South Africa | `"NODE"`, `"OFFSET"` | 노드·편심 |
| Korea, AASHTO Standard, Taiwan | `"NODE"`, `"OFFSET"`, `"IMPACT_FACTOR"`, `"bSPAN_START"` | +충격계수·경간시작 |
| AASHTO LRFD | `"NODE"`, `"OFFSET"`, `"bSPAN_START"`, `"CENTRI_FORCE"` | +경간시작·원심력계수 |
| PENNDOT, Australia, Poland | `"NODE"`, `"OFFSET"`, `"bSPAN_START"` | +경간시작 |
| India | `"NODE"`, `"OFFSET"`, `"IMPACT_SPAN_TYPE"`, `"IMPACT_FACTOR_INDIA"`, `"SPAN_LENGTH"` | 충격 방식 분기 |
| Eurocode | `"NODE"`, `"OFFSET"`, `"ECCEN_VERT_LOAD"` | +캔트 고려 수직편심 |

### Python 예제

```python
# KSCE-LSD15 기준 면 차선 정의
result = mv_post("SLAN", {
    "1": {
        "NAME": "SL_01",
        "WIDTH": 3,
        "WHEEL_SPACE": 1.8,
        "SKEW_START": 0,
        "SKEW_END": 0,
        "bOPTIMIZE": True,
        "ALLOW_WIDTH": 3,
        "MV_DIR": "BOTH",
        "LANE_ITEMS": [
            {"NODE": 1, "OFFSET": -1.5},
            {"NODE": 2, "OFFSET": -1.5},
            {"NODE": 3, "OFFSET": -1.5},
            {"NODE": 4, "OFFSET": -1.5},
        ],
    }
})
print(result)
```

---

## 8. /db/SLANch – Traffic Surface Lanes – China

> China 기준 면 차선. 각 노드에 경간 길이(`SPAN_LENGTH`)를 추가 지정합니다.

**Input URI:** `{base url}/db/SLANch`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "LL_01",
      "WIDTH": 3,
      "WHEEL_SPACE": 1.8,
      "SKEW_START": 10,
      "SKEW_END": 15,
      "bOPTIMIZE": true,
      "ALLOW_WIDTH": 3,
      "MV_DIR": "BOTH",
      "LANE_ITEMS": [
        {"NODE": 1, "OFFSET": -1.5, "SPAN_LENGTH": 12},
        {"NODE": 2, "OFFSET": -1.5, "SPAN_LENGTH": 12}
      ]
    }
  }
}
```

### Parameters – LANE_ITEMS

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Node No. | `"NODE"` | Integer | – | Required |
| 2 | Offset Distance to Lane Center | `"OFFSET"` | Number | 0 | Optional |
| 3 | Span Length | `"SPAN_LENGTH"` | Number | 0 | Optional |

### Python 예제

```python
result = mv_post("SLANch", {
    "1": {
        "NAME": "SL_01",
        "WIDTH": 3,
        "WHEEL_SPACE": 1.8,
        "SKEW_START": 0,
        "SKEW_END": 0,
        "bOPTIMIZE": True,
        "ALLOW_WIDTH": 3,
        "MV_DIR": "BOTH",
        "LANE_ITEMS": [
            {"NODE": 1, "OFFSET": -1.5, "SPAN_LENGTH": 12},
            {"NODE": 2, "OFFSET": -1.5, "SPAN_LENGTH": 12},
        ],
    }
})
print(result)
```

---

## 9. /db/SLANop – Traffic Surface Lanes – Moving Load Optimization

> 이동하중 최적화 전용 면 차선. 차선 폭 내 최적 위치를 탐색합니다.

**Input URI:** `{base url}/db/SLANop`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LANE_NAME": "LL_01",
      "SKEW_START": 10,
      "SKEW_END": 15,
      "MOVING": "BOTH",
      "OPTIMIZE_WIDTH": 4,
      "LANE_WIDTH": 3,
      "WHEEL_SPACE": 1.8288,
      "MARGIN": 0.1,
      "OFFSET_TYPE": 0,
      "DIVIDE_NUM": 2,
      "ITEMS": [
        {"NODE_KEY": 1, "OFFSET": -1.5, "FACTOR": 1.25, "SPAN_START": true},
        {"NODE_KEY": 2, "OFFSET": -1.5, "FACTOR": 1.25, "SPAN_START": false}
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Lane Name | `"LANE_NAME"` | String | – | Required |
| 2 | Skew Start | `"SKEW_START"` | Number | 0 | Optional |
| 3 | Skew End | `"SKEW_END"` | Number | 0 | Optional |
| 4 | Moving Direction | `"MOVING"` | String | – | Required |
| 5 | Optimization Width | `"OPTIMIZE_WIDTH"` | Number | – | Required |
| 6 | Lane Width | `"LANE_WIDTH"` | Number | – | Required |
| 7 | Wheel Spacing | `"WHEEL_SPACE"` | Number | 0 | Optional |
| 8 | Margin | `"MARGIN"` | Number | 0 | Optional |
| 9 | Offset Type (0=Fixed, 1=Division) | `"OFFSET_TYPE"` | Integer | – | Required |
| 10 | Number of Division | `"DIVIDE_NUM"` | Integer | – | Optional |
| 11 | Analysis Lane Offset | `"ANALYSIS_LANE_OFFSET"` | Number | – | Optional |
| 12 | Items | `"ITEMS"` | Array[Object] | – | Required |
| (1) | Node Key | `"NODE_KEY"` | Integer | – | Required |
| (2) | Offset | `"OFFSET"` | Number | 0 | Optional |
| (3) | Impact Factor / Centrifugal Force | `"FACTOR"` / `"CENT_F"` | Number | 0 | Optional |
| (4) | Span Start | `"SPAN_START"` | Boolean | false | Optional |

### Python 예제

```python
result = mv_post("SLANop", {
    "1": {
        "LANE_NAME": "SL_OP_01",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "BOTH",
        "OPTIMIZE_WIDTH": 4,
        "LANE_WIDTH": 3,
        "WHEEL_SPACE": 1.8288,
        "MARGIN": 0.1,
        "OFFSET_TYPE": 0,
        "DIVIDE_NUM": 2,
        "ITEMS": [
            {"NODE_KEY": 1, "OFFSET": -1.5, "FACTOR": 1.25, "SPAN_START": True},
            {"NODE_KEY": 2, "OFFSET": -1.5, "FACTOR": 1.25, "SPAN_START": False},
        ],
    }
})
print(result)
```

---

## 10. /db/MVHL – Vehicles

> 이동하중 차량을 정의합니다. `STANDARD_CODE` 필드로 설계 기준을 구분하며, 사전 정의 차량(`VEHICLE_TYPE_NAME`)과 사용자 정의 차량(`USER_LOAD_TYPE`)을 모두 지원합니다.

**Input URI:** `{base url}/db/MVHL`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body – AASHTO Standard

```json
{
  "Assign": {
    "1": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_H20-44",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "H20-44",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    }
  }
}
```

### Request Body – AASHTO LRFD

```json
{
  "Assign": {
    "1": {
      "MVLD_CODE": 2,
      "VEHICLE_LOAD_NAME": "US(ALL)_HL-93TRK",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "HL-93TRK",
      "STANDARD_CODE": "AASHTO-LRFD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 25,
        "CENT_F": true
      }
    }
  }
}
```

### Request Body – Korea (KS-RB)

```json
{
  "Assign": {
    "1": {
      "MVLD_CODE": 6,
      "VEHICLE_LOAD_NAME": "KR(SRB)_DB-24",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "DB-24",
      "STANDARD_CODE": "KS-RB",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    }
  }
}
```

### Parameters – 공통

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Moving Load Code (Integer) | `"MVLD_CODE"` | Integer | – | Required |
| 2 | Vehicular Load Name (사용자 지정) | `"VEHICLE_LOAD_NAME"` | String | – | Required |
| 3 | Vehicular Load Number | `"VEHICLE_LOAD_NUM"` | Integer | – | Required |
| 4 | Vehicular Type Name (기본 차량 이름) | `"VEHICLE_TYPE_NAME"` | String | – | Required |
| 5 | Standard Code ¹⁾ | `"STANDARD_CODE"` | String | – | Required |
| 6 | User Load Type (사용자 정의 시) | `"USER_LOAD_TYPE"` | String | – | Optional |
| 7 | Default Parameters | `"VEH_DEFAULT"` | Object | – | Required |
| 8 | Load Items (사용자 정의 축하중 배열) | `"LOAD_ITEMS"` | Array[Object] | – | Optional |

> ¹⁾ STANDARD_CODE 주요 값: `"AASHTO-STD"`, `"AASHTO-LRFD"`, `"KS-RB"`, `"KS2005"`, `"KSCE-LSD15"`, `"BS"`, `"EUROCODE"`, `"CANADA"`, `"AUSTRALIA"`, `"CHINA"`, `"INDIA"`, `"TAIWAN"`, `"POLAND"`, `"RUSSIA"`, `"SOUTH_AFRICA"`

### Parameters – VEH_DEFAULT (공통 필드)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Uniform Load | `"UNIFORM_LOAD"` | Number | – | Optional |
| 2 | Dynamic Load Allowance (%) | `"DYN_LOAD_ALLOWANCE"` | Number | – | Optional |
| 3 | Width 1 (W1) | `"W1"` | Number | – | Optional |
| 4 | Width 2 (W2) | `"W2"` | Number | – | Optional |
| 5 | Distance 1 (D1) | `"D1"` | Number | – | Optional |
| 6 | Distance 2 (D2) | `"D2"` | Number | – | Optional |
| 7 | Point Load (PL) | `"PL"` | Number | – | Optional |
| 8 | PLM | `"PLM"` | Number | – | Optional |
| 9 | PLV | `"PLV"` | Number | – | Optional |
| 10 | Add Centrifugal Force | `"CENT_F"` | Boolean | false | Optional |

### Parameters – LOAD_ITEMS (사용자 정의 차량)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Point Load | `"POINT_LOAD"` | Number | – | Required |
| 2 | Point Distance | `"POINT_DIST"` | Number | – | Required |

### Parameters – VEH_KSCE_LSD15 (`STANDARD_CODE: "KSCE-LSD15"` 전용)

> ℹ️ **2026-07-30 반영.** `STANDARD_CODE`가 `"KSCE-LSD15"`일 때는 `VEH_DEFAULT` 대신 이 전용 객체를 사용합니다(공식 매뉴얼의 별도 아티클 ["Vehicles - KSCE-LSD15"](https://support.midasuser.com/hc/en-us/articles/35958367637273-Vehicles-KSCE-LSD15)에만 문서화되어 있어 이전 버전에는 누락돼 있었습니다). 공식 Specifications 표는 표준 차량(Standard)·사용자 정의 Truck/Lane(1st·2nd Model)·Train·Lane 5가지 상황별로 필수/선택 여부가 달라지므로, 아래 표는 JSON Schema 기준으로 전체 필드를 통합해 실었습니다 — 실제 필수 여부는 `USER_LOAD_TYPE`/`LENGTH_LANE` 조합에 따라 달라지니 예제를 참고하십시오.

| No. | Description | Key | Value 타입 | 기본값 | 필수 |
| --- | --- | --- | --- | --- | --- |
| 1 | Load Type ¹⁾ — `0`=75% of Design Load / `1`=25% of Design Load | `"LOAD_TYPE"` | Integer | `0` | Optional |
| 2 | Lane Loaded Length (User Defined Truck/Lane 전용) | `"LOADED_LENGTH"` | Number | `60` | Optional |
| 3 | Distribution Load Not Exceeding Loaded Length | `"W1"` | Number | `12.7` | Optional |
| 4 | Distribution Load Exceeding Loaded Length | `"W2"` | Number | `12.7` | Optional |
| 5 | Spacing dD1 (User Defined Train 전용) | `"D1"` | Number | `0` | Optional |
| 6 | Spacing dD2 (User Defined Train 전용) | `"D2"` | Number | `0` | Optional |
| 7 | Exponent to Calculate Distribution Load of W2 | `"EXP"` | Number | `0.1` | Optional |
| 8 | Dynamic Load Allowance (%) | `"DYN_LOAD_ALLOWANCE"` | Number | `0` | Optional |
| 9 | Length of Lane Load · `0`=1st Model / `1`=2nd Model | `"LENGTH_LANE"` | Integer | — | Required |
| 10 | Length of Lane Load(User) — `LENGTH_LANE: 0`일 때 | `"LENGTH_LANE_USER"` | Number | `0` | Optional |
| 11 | Convert Point Load to Distributed Load | `"CONVERT_DIST_LOAD"` | Boolean | `false` | Optional |
| 12 | Number of Uniform Load (Lane 전용) · N개면 N-1 | `"UNIFORM_LOAD_NUM"` | Number | `0` | Optional |
| 13 | Uniform Load Distance (Lane 전용) | `"UNIFORM_LOAD_DIST"` | Number | `0` | Optional |
| 14 | Uniform Load (Lane 전용) | `"UNIFORM_LOAD_W"` | Number | — | Required |
| 15 | Uniform Load Length (Lane 전용) | `"UNIFORM_LOAD_LOAD_LENGTH_L"` | Number | — | Required |
| 16 | 축하중 배열 | `"POINT_ITEMS"` | Array [Object] | — | Required |
| 16-1 | └ 하중(Load) | `POINT_ITEMS[].POINT_LOAD` | Number | — | Required |
| 16-2 | └ 간격(Spacing) | `POINT_ITEMS[].POINT_DIST` | Number | — | Required |
| 16-3 | └ 등분포 환산 길이 — `CONVERT_DIST_LOAD: true`일 때 | `POINT_ITEMS[].POINT_DIST2` | Number | `0` | Optional |

> ¹⁾ 공식 Specifications 표에는 `LOAD_TYPE`이 `"KL-510LNE"` 전용이라 적혀 있지만, 공식 Request Examples는 `KL-510TRK`·`KL-510FTG` 표준 차량 예제에도 `"LOAD_TYPE": 0`을 그대로 포함합니다. 필드 자체는 모든 표준 차량 요청에 공통으로 실려 있고(기본값 `0`), 값 `1`(25% of Design Load)이 실제로 의미를 갖는 건 `KL-510LNE`뿐인 것으로 판단됩니다 — CLAUDE.md 원칙에 따라 예제를 기준으로 반영.

**요청 예시 — 표준 차량(Standard)**

```json
{
  "Assign": {
    "1": {
      "MVLD_CODE": 13,
      "VEHICLE_LOAD_NAME": "ST_KL-510TRK",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "KL-510TRK",
      "STANDARD_CODE": "KSCE-LSD15",
      "VEH_KSCE_LSD15": {
        "LOAD_TYPE": 0,
        "DYN_LOAD_ALLOWANCE": 25,
        "LENGTH_LANE": 0,
        "LENGTH_LANE_USER": 0,
        "CONVERT_DIST_LOAD": false,
        "POINT_ITEMS": [
          { "POINT_LOAD": 48, "POINT_DIST": 3.6 },
          { "POINT_LOAD": 135, "POINT_DIST": 1.2 },
          { "POINT_LOAD": 135, "POINT_DIST": 7.2 },
          { "POINT_LOAD": 192, "POINT_DIST": 0 }
        ]
      }
    }
  }
}
```

**요청 예시 — 사용자 정의(User Defined) Truck/Lane**

```json
{
  "Assign": {
    "8": {
      "MVLD_CODE": 13,
      "VEHICLE_LOAD_NAME": "UD_Truck/Lane1",
      "VEHICLE_LOAD_NUM": 2,
      "USER_LOAD_TYPE": "Truck/Lane",
      "VEH_KSCE_LSD15": {
        "LOADED_LENGTH": 60,
        "W1": 12.7,
        "W2": 12.7,
        "EXP": 0.1,
        "DYN_LOAD_ALLOWANCE": 25,
        "LENGTH_LANE": 0,
        "LENGTH_LANE_USER": 1.5,
        "CONVERT_DIST_LOAD": true,
        "POINT_ITEMS": [
          { "POINT_LOAD": 100, "POINT_DIST": 0.2, "POINT_DIST2": 0.45 }
        ]
      }
    }
  }
}
```

### Python 예제

```python
# KSCE-LSD15 기준 사전 정의 차량 — MVLD_CODE는 KSCE-LSD15 전용 코드(13)를 사용
result = mv_post("MVHL", {
    "1": {
        "MVLD_CODE": 13,   # KSCE-LSD15 코드
        "VEHICLE_LOAD_NAME": "KL-510FTG",
        "VEHICLE_LOAD_NUM": 1,
        "VEHICLE_TYPE_NAME": "ST_KL-510FTG",
        "STANDARD_CODE": "KSCE-LSD15",
        "VEH_KSCE_LSD15": {
            "LOAD_TYPE": 0,
            "DYN_LOAD_ALLOWANCE": 15,
            "LENGTH_LANE": 0,
            "LENGTH_LANE_USER": 0,
            "CONVERT_DIST_LOAD": False,
            "POINT_ITEMS": [
                {"POINT_LOAD": 38.4, "POINT_DIST": 3.6},
                {"POINT_LOAD": 108, "POINT_DIST": 1.2},
                {"POINT_LOAD": 108, "POINT_DIST": 7.2},
                {"POINT_LOAD": 153.6, "POINT_DIST": 0},
            ],
        },
    }
})
print(result)
```

---

## 11. /db/MVHLtr – Vehicles – Transverse

> Transverse 이동하중 코드용 차량. 횡방향 배치 파라미터를 정의합니다.

**Input URI:** `{base url}/db/MVHLtr`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "Trans",
      "P": 120,
      "W": 2.3,
      "LW": 10,
      "NUM": 4,
      "DW": 0.3,
      "DV": 0.4,
      "DE": 0.5,
      "OPT_MEDIAN_STRIP": false
    },
    "2": {
      "NAME": "Trans_Medians",
      "P": 120,
      "W": 2.3,
      "LW": 10,
      "NUM": 4,
      "DW": 0.3,
      "DV": 0.4,
      "DE": 0.5,
      "OPT_MEDIAN_STRIP": true,
      "ML": 15,
      "MW": 1,
      "LEFT_LANES": 2
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Vehicular Load Name | `"NAME"` | String | – | Required |
| 2 | Wheel Load (P) | `"P"` | Number | – | Required |
| 3 | Distribution Width | `"W"` | Number | – | Required |
| 4 | Longitudinal Width | `"LW"` | Number | – | Required |
| 5 | Max. Number of Lanes (n) | `"NUM"` | Integer | – | Required |
| 6 | Distance between Wheels (Dw) | `"DW"` | Number | – | Required |
| 7 | Min. Distance between Vehicle (Dv) | `"DV"` | Number | – | Required |
| 8 | Edge Distance of Wheel Loads (De) | `"DE"` | Number | 0 | Optional |
| 9 | Median Strip Option | `"OPT_MEDIAN_STRIP"` | Boolean | false | Optional |
| 10 | Location (Ml) | `"ML"` | Number | – | Required (if OPT_MEDIAN_STRIP=true) |
| 11 | Width (Mw) | `"MW"` | Number | – | Required (if OPT_MEDIAN_STRIP=true) |
| 12 | Max. Number of Left Lanes (n1) | `"LEFT_LANES"` | Integer | – | Required (if OPT_MEDIAN_STRIP=true) |

### Python 예제

```python
result = mv_post("MVHLtr", {
    "1": {
        "NAME": "Trans_Basic",
        "P": 120,
        "W": 2.3,
        "LW": 10,
        "NUM": 4,
        "DW": 0.3,
        "DV": 0.4,
        "DE": 0.5,
        "OPT_MEDIAN_STRIP": False,
    }
})
print(result)
```

---

## 12. /db/MVLD – Moving Load Cases

> 이동하중 하중 케이스를 정의합니다. General Load, Permit Vehicle, Moving Load Optimization의 세 가지 타입을 지원하며, 이동하중 코드별로 구조가 다릅니다.

**Input URI:** `{base url}/db/MVLD`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body – KSCE-LSD15 (General Load)

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "TYPE": 0,
      "DEFAULT": {
        "SCALE_FACTORS": [1, 0.9, 0.8, 0.7, 0.65, 0.65],
        "COMB_OPTION": "COMBINED",
        "LANE_FACTOR_TYPE": 1,
        "SUB_LOAD_DATAS": [
          {
            "VEHICLE_TYPE": "VL",
            "VEHICLE_NAME": "ST_KL-510FTG",
            "SCALE_FACTOR": 1,
            "MIN_LOADED_LANE": 1,
            "MAX_LOADED_LANE": 2,
            "LANE_NAMES": ["LL_01", "LL_02"]
          }
        ]
      }
    }
  }
}
```

### Request Body – AASHTO LRFD (Permit Vehicle)

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Permit",
      "DESC": "",
      "TYPE": 1,
      "PERMIT_LOAD": {
        "VEHICLE_LOAD_NAME": "UD_PermitTruck",
        "REF_LANE": "LL_01",
        "SCALE_FACTOR": 1
      }
    }
  }
}
```

### Request Body – Moving Load Optimization

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Optimize",
      "DESC": "",
      "TYPE": 2,
      "AUTO_OPTIMIZE": {
        "LANE_NAME": "LL_01",
        "SCALE_FACTORS": [1.2, 1, 0.85, 0.65, 0.65, 0.65],
        "MIN_VEHL_DIST": 1,
        "MIN_NUM_VEHICLE": 1,
        "MAX_NUM_VEHICLE": 2,
        "OPTIMIZE_ITEMS": [
          {"VEHICLE_TYPE": "VL", "VEHICLE_NAME": "HL-93TRK", "SCALE_FACTOR": 1}
        ]
      }
    }
  }
}
```

### Parameters – 공통

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Load Type (0=General, 1=Permit, 2=Optimization) | `"TYPE"` | Integer | – | Required |

### Parameters – DEFAULT (General Load, KSCE-LSD15 / AASHTO STD / LRFD / PENNDOT / Taiwan / Canada)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Lane Factor Type (1=Multiple Presence Factor) | `"LANE_FACTOR_TYPE"` | Integer | – | Required |
| 2 | Multiple Presence Factor [L1~L6+] | `"SCALE_FACTORS"` | Array[Number, 6] | – | Required |
| 3 | Loading Effect (`"COMBINED"` / `"INDEPENDENT"`) | `"COMB_OPTION"` | String | – | Required |
| 4 | Sub Load Cases | `"SUB_LOAD_DATAS"` | Array[Object] | – | Required |
| (i) | Vehicle Type (`"VL"` / `"VC"`) | `"VEHICLE_TYPE"` | String | – | Required |
| (ii) | Vehicle Name | `"VEHICLE_NAME"` | String | – | Required |
| (iii) | Scale Factor | `"SCALE_FACTOR"` | Number | – | Required |
| (iv) | Min. Number of Loaded Lane | `"MIN_LOADED_LANE"` | Integer | – | Required |
| (v) | Max. Number of Loaded Lane | `"MAX_LOADED_LANE"` | Integer | – | Required |
| (vi) | Selected Lanes | `"LANE_NAMES"` | Array[String] | – | Required |

### Parameters – DEFAULT (Korea – 추가 필드)

| No. | Description | Key | Value Type |
|-----|-------------|-----|-----------|
| 1 | Lane Factor Type (0=Multi-Lane KS Rail, 1=MPF) | `"LANE_FACTOR_TYPE"` | Integer |
| 2 | 2-Lane Factor L1 | `"_2_LANE_FACTOR_1"` | Number |
| 3 | 2-Lane Factor L2 | `"_2_LANE_FACTOR_2"` | Number |
| 4~7 | 3+ Lane Factors (L1~L4) | `"_3_LANE_FACTOR_1"` ~ `"_3_LANE_FACTOR_4"` | Number |

### Parameters – PERMIT_LOAD (TYPE=1)

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Vehicle Load Name | `"VEHICLE_LOAD_NAME"` | String | Required |
| 2 | Reference Lane | `"REF_LANE"` | String | Required |
| 3 | Scale Factor | `"SCALE_FACTOR"` | Number | Required |

### Parameters – AUTO_OPTIMIZE (TYPE=2)

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Multiple Presence Factor | `"SCALE_FACTORS"` | Array[Number, 6] | Required |
| 2 | Min. Vehicle Distance | `"MIN_VEHL_DIST"` | Number | Required |
| 3 | Loaded Lane Name | `"LANE_NAME"` | String | Required |
| 4 | Min. Number of Vehicle | `"MIN_NUM_VEHICLE"` | Integer | Required |
| 5 | Max. Number of Vehicle | `"MAX_NUM_VEHICLE"` | Integer | Required |
| 6 | Optimize Items | `"OPTIMIZE_ITEMS"` | Array[Object] | Required |

### Python 예제

```python
# KSCE-LSD15 General Load Case
result = mv_post("MVLD", {
    "1": {
        "LCNAME": "MV_KSCE_1",
        "DESC": "",
        "TYPE": 0,
        "DEFAULT": {
            "SCALE_FACTORS": [1, 0.9, 0.8, 0.7, 0.65, 0.65],
            "COMB_OPTION": "COMBINED",
            "LANE_FACTOR_TYPE": 1,
            "SUB_LOAD_DATAS": [
                {
                    "VEHICLE_TYPE": "VL",
                    "VEHICLE_NAME": "ST_KL-510FTG",
                    "SCALE_FACTOR": 1,
                    "MIN_LOADED_LANE": 1,
                    "MAX_LOADED_LANE": 2,
                    "LANE_NAMES": ["LL_01", "LL_02"],
                }
            ],
        },
    }
})
print(result)
```

---

## 13. /db/MVLDch – Moving Load Cases – China

> China 이동하중 하중 케이스. 교량 타입별 차선 계수를 별도 지정합니다.

**Input URI:** `{base url}/db/MVLDch`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "OPT_AUTO_OPTIMIZE": false,
      "BRIDGE_TYPE": 2,
      "SCALE_FACTOR_O": [1, 1, 0.8, 0.67, 0.6, 0.55, 0.55, 0.55],
      "SCALE_FACTOR_N": [1, 1, 0.78, 0.67, 0.6, 0.55, 0.52, 0.5],
      "SCALE_FACTOR_JTG": [1.2, 1, 0.78, 0.67, 0.6, 0.55, 0.52, 0.5],
      "LOADING_EFFECT": 1,
      "SUB_LOAD_ITEMS": [
        {
          "VEHICLE_CLASS": "CH(CJJ11)_C-CD(A/B)",
          "VEHICLE_TYPE": "VL",
          "SCALE_FACTOR": 1,
          "MIN_NUM_LOADED_LANES": 1,
          "MAX_NUM_LOADED_LANES": 2,
          "SELECTED_LANES": ["LL_01", "LL_02"]
        }
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Moving Load Optimization | `"OPT_AUTO_OPTIMIZE"` | Boolean | false | Optional |
| 4 | Bridge Type (0=Old Urban, 1=Highway/New Urban, 2=JTG B01-2014) | `"BRIDGE_TYPE"` | Integer | – | Required |
| 5 | Scale Factor for Old Urban Bridge [1~7, ≥8] | `"SCALE_FACTOR_O"` | Array[Number, 8] | – | Required |
| 6 | Scale Factor for Highway/New Urban Bridge | `"SCALE_FACTOR_N"` | Array[Number, 8] | – | Required |
| 7 | Scale Factor for JTG B01-2014 | `"SCALE_FACTOR_JTG"` | Array[Number, 8] | – | Required |
| 8 | Combination Option (0=Combined, 1=Independent) | `"LOADING_EFFECT"` | Integer | – | Required |
| 9 | Sub-Load Cases | `"SUB_LOAD_ITEMS"` | Array[Object] | – | Required |
| (i) | Vehicle Type (`"VL"` / `"VC"`) | `"VEHICLE_TYPE"` | String | – | Required |
| (ii) | Vehicle Class Name | `"VEHICLE_CLASS"` | String | – | Required |
| (iii) | Scale Factor | `"SCALE_FACTOR"` | Number | – | Required |
| (iv) | Min. Number of Loaded Lanes | `"MIN_NUM_LOADED_LANES"` | Integer | – | Required |
| (v) | Max. Number of Loaded Lanes | `"MAX_NUM_LOADED_LANES"` | Integer | – | Required |
| (vi) | Selected Lanes | `"SELECTED_LANES"` | Array[String] | – | Required |

### Python 예제

```python
result = mv_post("MVLDch", {
    "1": {
        "LCNAME": "MV_China_1",
        "DESC": "",
        "OPT_AUTO_OPTIMIZE": False,
        "BRIDGE_TYPE": 2,
        "SCALE_FACTOR_O":   [1, 1, 0.80, 0.67, 0.60, 0.55, 0.55, 0.55],
        "SCALE_FACTOR_N":   [1, 1, 0.78, 0.67, 0.60, 0.55, 0.52, 0.50],
        "SCALE_FACTOR_JTG": [1.2, 1, 0.78, 0.67, 0.60, 0.55, 0.52, 0.50],
        "LOADING_EFFECT": 1,
        "SUB_LOAD_ITEMS": [
            {
                "VEHICLE_CLASS": "CH(CJJ11)_C-CD(A/B)",
                "VEHICLE_TYPE": "VL",
                "SCALE_FACTOR": 1,
                "MIN_NUM_LOADED_LANES": 1,
                "MAX_NUM_LOADED_LANES": 2,
                "SELECTED_LANES": ["LL_01", "LL_02"],
            }
        ],
    }
})
print(result)
```

---

## 14. /db/MVLDid – Moving Load Cases – India

> India (IRC) 이동하중 하중 케이스. Auto Live Load Combinations 및 Permit Vehicle을 지원합니다.

**Input URI:** `{base url}/db/MVLDid`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_India_1",
      "DESC": "",
      "SCALE_FACTOR": [1, 0.9, 0.8, 0.8],
      "NUM_LOADED_LANES": 2,
      "SUB_LOAD_ITEMS": [
        {
          "VEHICLE_CLASS_1": "IN(IRC)_(25t1)_BroadGauge-1676mm",
          "SCALE_FACTOR": 1,
          "MIN_NUM_LOADED_LANES": 1,
          "MAX_NUM_LOADED_LANES": 2,
          "SELECTED_LANES": ["LL_01", "LL_02"]
        }
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Multiple Presence Factor [1-2, 3, 4, ≥5] | `"SCALE_FACTOR"` | Array[Number, 4] | – | Required |
| 4 | Auto Live Load Combinations | `"OPT_AUTO_LL"` | Boolean | false | Optional |
| 5 | Load Cases for Permit Vehicle | `"OPT_LC_FOR_PERMIT_LOAD"` | Boolean | false | Optional |
| **General Load** | | | | | |
| 6 | Number of Loaded Lanes | `"NUM_LOADED_LANES"` | Integer | – | Required |
| 7 | Sub-Load Cases | `"SUB_LOAD_ITEMS"` | Array[Object] | – | Required |
| **Permit Vehicle (OPT_LC_FOR_PERMIT_LOAD=true)** | | | | | |
| 6 | Permit Vehicle ID | `"PERMIT_VEHICLE"` | Integer | – | Required |
| 7 | Reference Lane ID | `"REF_LANE"` | Integer | – | Required |
| 8 | Eccentricity | `"ECCEN"` | Number | – | Required |
| 9 | Scale Factor | `"PERMIT_SCALE_FACTOR"` | Number | – | Required |

### Python 예제

```python
result = mv_post("MVLDid", {
    "1": {
        "LCNAME": "MV_India_1",
        "DESC": "",
        "SCALE_FACTOR": [1, 0.9, 0.8, 0.8],
        "NUM_LOADED_LANES": 2,
        "SUB_LOAD_ITEMS": [
            {
                "VEHICLE_CLASS_1": "IN(IRC6)_ClassA",
                "SCALE_FACTOR": 1,
                "MIN_NUM_LOADED_LANES": 1,
                "MAX_NUM_LOADED_LANES": 2,
                "SELECTED_LANES": ["LL_01", "LL_02"],
            }
        ],
    }
})
print(result)
```

---

## 15. /db/MVLDbs – Moving Load Cases – BS

> BS (British Standard) 이동하중 하중 케이스.

**Input URI:** `{base url}/db/MVLDbs`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_BS_1",
      "DESC": "",
      "bAUTOOPTIMIZE": false,
      "LOADMODEL": "STANDER",
      "bAUTOLIVELOADCOMB": true,
      "DGNCOMBFACTORTYPE": "ULTIMATE",
      "COMBMETHOD": "COMB_1",
      "LCDATA_STANDARD": {
        "LOADINGEFFECT": "INDEPEND",
        "SUBLOADDATA": [
          {
            "SCALEFACTOR": 1,
            "NUMLOADEDLANE": 4,
            "VEHICLE_NAME": "BS_(BD21)_HA&HB(Auto)",
            "SELECTEDLANES": ["LL_01", "LL_02", "LL_03", "LL_04"],
            "STRAD_LANE": [
              {"STARDD_LANE_1": "LL_03", "STARDD_LANE_2": "LL_04"}
            ]
          }
        ]
      }
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Moving Load Optimization | `"bAUTOOPTIMIZE"` | Boolean | false | Optional |
| 4 | Load Model (`"STANDER"` / `"SPECAIL"` / `"ALL_MODE_1"`) | `"LOADMODEL"` | String | – | Required |
| 5 | Auto Live Load Combination | `"bAUTOLIVELOADCOMB"` | Boolean | false | Optional |
| 6 | Design Combination Factor Type (`"ULTIMATE"` / `"SERVICEABIL"`) | `"DGNCOMBFACTORTYPE"` | String | – | Required |
| 7 | Combination Method (`"COMB_1"` / `"COMB_2_3"`) | `"COMBMETHOD"` | String | – | Required |
| 8 | Standard Load Case Data | `"LCDATA_STANDARD"` | Object | – | Required (when STANDER) |
| 9 | Special Load Case Data | `"LCDATA_SPECIAL"` | Object | – | Required (when SPECAIL) |
| 10 | All Mode Load Case Data | `"LCDATA_ALLMODE"` | Object | – | Required (when ALL_MODE_1) |

### Python 예제

```python
result = mv_post("MVLDbs", {
    "1": {
        "LCNAME": "MV_BS_Standard",
        "DESC": "",
        "bAUTOOPTIMIZE": False,
        "LOADMODEL": "STANDER",
        "bAUTOLIVELOADCOMB": True,
        "DGNCOMBFACTORTYPE": "ULTIMATE",
        "COMBMETHOD": "COMB_1",
        "LCDATA_STANDARD": {
            "LOADINGEFFECT": "INDEPEND",
            "SUBLOADDATA": [
                {
                    "SCALEFACTOR": 1,
                    "NUMLOADEDLANE": 4,
                    "VEHICLE_NAME": "BS_(BD21)_HA&HB(Auto)",
                    "SELECTEDLANES": ["LL_01", "LL_02", "LL_03", "LL_04"],
                    "STRAD_LANE": [
                        {"STARDD_LANE_1": "LL_03", "STARDD_LANE_2": "LL_04"}
                    ],
                }
            ],
        },
    }
})
print(result)
```

---

## 16. /db/MVLDeu – Moving Load Cases – Eurocode

> Eurocode (EN 1991-2) 이동하중 하중 케이스. 5가지 Load Model 타입(`TYPE_LOADMODEL`)과 각 타입별 **General Load** / **Moving Load Optimization**(`OPT_AUTO_OPTIMIZE`) 두 입력 모드를 지원합니다.

**Input URI:** `{base url}/db/MVLDeu`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body – LM 1 / FLM 1 / Footbridge (TYPE_LOADMODEL = 1, General Load)

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 1,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(FF)_Uniformload(Road)",
      "OPT_LEADING": false,
      "SLN_LIST": ["LL_01", "LL_02"],
      "SRA_LIST": ["LL_04"],
      "FLN_LIST": ["LL_03"]
    }
  }
}
```

### Request Body – LM 2/3/4, FLM 2/3/4, Permit Truck (TYPE_LOADMODEL = 2, General Load)

```json
{
  "Assign": {
    "2": {
      "LCNAME": "MV_Case2",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 2,
      "DESC": "",
      "OPT_COMB": 1,
      "OPT_LEADING": true,
      "SUB_LOAD_LIST": [
        {
          "TYPE": 2,
          "NAME": "EU_(FF)_ConcentratedLoad",
          "SCALE_FACTOR": 1,
          "MIN_LOAD_LANE_TYPE": 1,
          "MAX_LOAD_LANE_TYPE": 4,
          "SLN_LIST": ["LL_01", "LL_02", "LL_03", "LL_04"]
        }
      ]
    }
  }
}
```

### Request Body – LM 1 & 3 Multi (TYPE_LOADMODEL = 3, General Load)

```json
{
  "Assign": {
    "3": {
      "LCNAME": "MV_Case3",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 3,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "UD_LoadModel3",
      "OPT_LEADING": false,
      "SLN_LIST": ["LL_01", "LL_02"],
      "SRA_LIST": ["LL_04"]
    }
  }
}
```

### Request Body – LM 1 & 3 Multi (Straddling) (TYPE_LOADMODEL = 4, General Load)

```json
{
  "Assign": {
    "4": {
      "LCNAME": "MV_Case4",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 4,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(R)_LoadModel3(UKNA)_SOV250_Auto",
      "OPT_LEADING": false,
      "SLN_LIST": ["LL_01", "LL_03", "LL_04"],
      "SRA_LIST": ["LL_02"],
      "STL_LIST": [
        {"NAME1": "LL_03", "NAME2": "LL_04"}
      ]
    }
  }
}
```

### Request Body – Railway Bridge (TYPE_LOADMODEL = 5, General Load)

```json
{
  "Assign": {
    "5": {
      "LCNAME": "MV_Case5",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 5,
      "DESC": "",
      "OPT_COMB": 1,
      "SCALE_FACTOR1": 0.8,
      "SCALE_FACTOR2": 0.7,
      "SCALE_FACTOR3": 0.6,
      "OPT_PSI_FACTOR": false,
      "MULTI_FACTOR1": 1,
      "MULTI_FACTOR2": 1,
      "MULTI_FACTOR3": 0.75,
      "SUB_LOAD_LIST": [
        {
          "TYPE": 2,
          "NAME": "EU_(RFL)_HSLMB",
          "SCALE_FACTOR": 1,
          "MIN_LOAD_LANE_TYPE": 1,
          "MAX_LOAD_LANE_TYPE": 4,
          "SLN_LIST": ["LL_01", "LL_02", "LL_03", "LL_04"]
        }
      ]
    }
  }
}
```

### Request Body – Moving Load Optimization (OPT_AUTO_OPTIMIZE = true, 예: LM 1)

```json
{
  "Assign": {
    "6": {
      "LCNAME": "MV_Case6",
      "OPT_AUTO_OPTIMIZE": true,
      "TYPE_LOADMODEL": 1,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(FF)_Uniformload(Road)",
      "OPT_LEADING": false,
      "MINVHLDIST": 1,
      "OPTIMIZE_LANE_NAME": "LL_01",
      "LOADEDLANE": 3,
      "SLN_LIST": ["LL_01", "LL_03", "LL_04"]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Load Model Type ¹⁾ | `"TYPE_LOADMODEL"` | Integer | – | Required |
| 4 | Moving Load Optimization (General Load: `false` / Optimization: `true`) | `"OPT_AUTO_OPTIMIZE"` | Boolean | false | Optional |
| 5 | Ignore ψ(1) factor | `"OPT_LEADING"` | Boolean | – | Required (LM1/3/4, General·Optimization) |
| 6 | Load Case – Vehicle | `"VHLNAME1"` | String | – | Required (LM1/3/4) |
| 7 | Load Case – Footway | `"VHLNAME2"` | String | – | Optional (LM1) / Required (LM3/4, Optimization) |
| 8 | Selected Lanes | `"SLN_LIST"` | Array[String] | – | Required (LM1/3/4) |
| 9 | Remaining Area | `"SRA_LIST"` | Array[String] | – | Required (LM1/3) |
| 10 | Footway Lanes (LM1) | `"FLN_LIST"` | Array[String] | – | Required (LM1) |
| 11 | Straddling Lanes — `(1)` Start Lane `"NAME1"`, `(2)` End Lane `"NAME2"` | `"STL_LIST"` | Array[Object] | – | Required (LM4) |
| 12 | Loading Effect (Combined: `0` / Independent: `1`) | `"OPT_COMB"` | String | – | Required (LM2/5) |
| 13 | Sub-Load Cases — `(1)` Vehicle Load Type ²⁾ `"TYPE"`, `(2)` Name `"NAME"`, `(3)` Scale Factor `"SCALE_FACTOR"`, `(4)` Min. Loaded Lanes `"MIN_LOAD_LANE_TYPE"`, `(5)` Max. Loaded Lanes `"MAX_LOAD_LANE_TYPE"`, `(6)` Selected Lanes `"SLN_LIST"` | `"SUB_LOAD_LIST"` | Array[Object] | – | Required (LM2/5, General) |
| 14 | Ignore ψ1 factor | `"OPT_PSI_FACTOR"` | Boolean | – | Required (LM5) |
| 15 | ψ1 factor for Lane 1/2/3+ | `"SCALE_FACTOR1"/"SCALE_FACTOR2"/"SCALE_FACTOR3"` | Number | – | Required (LM5) |
| 16 | Multi Presence Factor for Lane 1/2/3+ | `"MULTI_FACTOR1"/"MULTI_FACTOR2"/"MULTI_FACTOR3"` | Number | – | Required (LM5) |
| 17 | Min. Vehicle Distance | `"MINVHLDIST"` | Number | – | Required (Optimization) |
| 18 | Assignment Lane | `"OPTIMIZE_LANE_NAME"` | String | – | Required (Optimization) |
| 19 | Number of Loaded Lane | `"LOADEDLANE"` | Integer | – | Required (Optimization, LM1/3/4) |
| 20 | Min./Max. Number of Vehicle | `"MIN_NUM_VHL"/"MAX_NUM_VHL"` | Integer | – | Required (Optimization, LM2/5) |
| 21 | Sub-Load Cases for Optimization — `(1)` Type `"TYPE"`, `(2)` Name `"NAME"`, `(3)` Scale Factor `"SCALE_FACTOR"` | `"OPTIMIZE_LIST"` | Array[Object] | – | Required (Optimization, LM2/5) |

> ¹⁾ TYPE_LOADMODEL:  
> 1 = LM 1, FLM 1 / Footbridge  
> 2 = LM 2, 3, 4 / FLM 2, 3, 4 / Footbridge / Permit Truck  
> 3 = LM 1 & 3 Multi  
> 4 = LM 1 & 3 Multi (Straddling)  
> 5 = Railway Bridge
>
> ²⁾ Vehicle Load Type(`"TYPE"`): Vehicle Class = `1` (Eurocode에서는 미사용) / Vehicle Load = `2` (Eurocode 고정값)

### Python 예제

```python
result = mv_post("MVLDeu", {
    "1": {
        "LCNAME": "MV_Case1",
        "OPT_AUTO_OPTIMIZE": False,
        "TYPE_LOADMODEL": 1,
        "DESC": "",
        "VHLNAME1": "EU_(R)_LoadModel1",
        "VHLNAME2": "EU_(FF)_Uniformload(Road)",
        "OPT_LEADING": False,
        "SLN_LIST": ["LL_01", "LL_02"],
        "SRA_LIST": ["LL_04"],
        "FLN_LIST": ["LL_03"],
    }
})
print(result)
```

---

## 17. /db/MVLDpl – Moving Load Cases – Poland

> Poland 이동하중 하중 케이스. 3가지 Load Model (Vehicle S, Vehicle K, Military)을 지원합니다.

**Input URI:** `{base url}/db/MVLDpl`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV1",
      "DESC": "",
      "LOAD_MODEL": 1,
      "bAUTO_OPTIMIZE": false,
      "bPERMIT_LOAD": false,
      "DEFAULT": {
        "COMB_OPTION": "INDEPENDENT",
        "SUB_LOAD_DATAS": [
          {
            "VEHICLE_NAME": "VehicleS",
            "SCALE_FACTOR": 1,
            "MIN_LOADED_LANE": 1,
            "MAX_LOADED_LANE": 2,
            "LANE_NAMES": ["L1", "L2"]
          }
        ]
      }
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Moving Load Optimization | `"bAUTO_OPTIMIZE"` | Boolean | false | Optional |
| 4 | Load Case for Permit Vehicle | `"bPERMIT_LOAD"` | Boolean | false | Optional |
| 5 | Load Model (1=Vehicle S/2S/Permit, 2=Vehicle K, 3=Military) | `"LOAD_MODEL"` | Integer | – | Required |
| 6 | Sub-Load Cases | `"DEFAULT"` | Object | – | Required |
| (1) | Loading Effect (`"COMBINED"` / `"INDEPENDENT"`) ¹⁾ | `"COMB_OPTION"` | String | – | Required |
| (2) | Sub-Load Data | `"SUB_LOAD_DATAS"` | Array[Object] | – | Required |
| (3) | Vehicle Name ²⁾ | `"VEHICLE_LOAD_NAME"` | String | – | Required |

> ¹⁾ Vehicle S/2S/Permit 타입에서만 사용  
> ²⁾ Vehicle K, Military 타입에서는 `"VEHICLE_LOAD_NAME"` 최상위 키로 지정

### Python 예제

```python
result = mv_post("MVLDpl", {
    "1": {
        "LCNAME": "MV_PL_VehicleS",
        "DESC": "",
        "LOAD_MODEL": 1,
        "bAUTO_OPTIMIZE": False,
        "bPERMIT_LOAD": False,
        "DEFAULT": {
            "COMB_OPTION": "INDEPENDENT",
            "SUB_LOAD_DATAS": [
                {
                    "VEHICLE_NAME": "VehicleS",
                    "SCALE_FACTOR": 1,
                    "MIN_LOADED_LANE": 1,
                    "MAX_LOADED_LANE": 2,
                    "LANE_NAMES": ["L1", "L2"],
                }
            ],
        },
    }
})
print(result)
```

---

## 18. /db/MVLDtr – Moving Load Cases – Transverse

> Transverse 이동하중 코드 전용 하중 케이스.

**Input URI:** `{base url}/db/MVLDtr`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "MVHL_NAME": "Trans",
      "SCALEFACTOR": 1,
      "LLAN_NAME": "LL_01",
      "NUM_LANE": 3,
      "ITEMS": [1, 1, 0.9, 0.75]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Vehicle Name | `"MVHL_NAME"` | String | – | Required |
| 4 | Scale Factor | `"SCALEFACTOR"` | Number | – | Required |
| 5 | Line Lane | `"LLAN_NAME"` | String | – | Required |
| 6 | Number of Loaded Lanes | `"NUM_LANE"` | Integer | – | Required |
| 7 | Factors (Length: NUM_LANE + 1) | `"ITEMS"` | Array[Number] | – | Required |

### Python 예제

```python
result = mv_post("MVLDtr", {
    "1": {
        "LCNAME": "MV_Trans_1",
        "DESC": "",
        "MVHL_NAME": "Trans",
        "SCALEFACTOR": 1,
        "LLAN_NAME": "LL_01",
        "NUM_LANE": 3,
        "ITEMS": [1, 1, 0.9, 0.75],
    }
})
print(result)
```

---

## 19. /db/CRGR – Concurrent Reaction Group

> 이동하중 해석 시 반력을 동시에 추출할 구조 그룹들을 정의합니다.

**Input URI:** `{base url}/db/CRGR`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "GROUPS": ["Main3", "Main4", "Main5"]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Structure Group Names | `"GROUPS"` | Array[String] | – | Required |

### Python 예제

```python
result = mv_post("CRGR", {
    "1": {"GROUPS": ["Main3", "Main4", "Main5"]},
    "2": {"GROUPS": ["Pier1", "Pier2"]},
})
print(result)
```

---

## 20. /db/CJFG – Concurrent Joint Force Group

> 이동하중 해석 시 절점 힘을 동시에 추출할 구조 그룹들을 정의합니다.

**Input URI:** `{base url}/db/CJFG`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "GROUPS": ["Main1", "Main2", "Main3", "Main4"]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Structure Group Names | `"GROUPS"` | Array[String] | – | Required |

### Python 예제

```python
result = mv_post("CJFG", {
    "1": {"GROUPS": ["Main1", "Main2", "Main3", "Main4"]},
})
print(result)
```

---

## 21. /db/MVHC – Vehicle Classes

> 여러 차량을 하나의 클래스로 묶어 Moving Load Case에서 그룹으로 사용합니다.

**Input URI:** `{base url}/db/MVHC`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 사용 가능 이동하중 코드: AASHTO Standard, AASHTO LRFD, PENNDOT, Canada, Australia, Russia, Korea, KSCE-LSD15, China, Taiwan

### Request Body

```json
{
  "Assign": {
    "1": {
      "VEHICLE_CLS_NAME": "VCN1",
      "VEHICLE_LD_NAMES": ["DB-18"]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Vehicle Class Name | `"VEHICLE_CLS_NAME"` | String | – | Required |
| 2 | Selected Vehicle List | `"VEHICLE_LD_NAMES"` | Array[String] | – | Required |

### Python 예제

```python
result = mv_post("MVHC", {
    "1": {
        "VEHICLE_CLS_NAME": "Heavy_Trucks",
        "VEHICLE_LD_NAMES": ["DB-18", "DB-24", "HL-93TRK"],
    }
})
print(result)
```

---

## 22. /db/SINF – Plate Element for Influence Surface

> 영향면(Influence Surface) 해석에 사용할 판 요소 목록을 지정합니다.

**Input URI:** `{base url}/db/SINF`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 사용 가능 코드: AASHTO Standard, AASHTO LRFD, PENNDOT, Canada, BS, Eurocode, South Africa, Korea, KSCE-LSD15, China, Taiwan

### Request Body

```json
{
  "Assign": {
    "1": {
      "ELEM_LISTS": [438, 439, 444, 462, 463]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Assigned Element List | `"ELEM_LISTS"` | Array[Integer] | – | Required |

### Python 예제

```python
result = mv_post("SINF", {
    "1": {"ELEM_LISTS": [438, 439, 440, 441, 442, 443, 444]},
})
print(result)
```

---

## 23. /db/MLSP – Lane Support – Negative Moments at Interior Piers

> 연속교 내측 지점부 부(-) 모멘트 차선 지지 위치를 지정합니다.

**Input URI:** `{base url}/db/MLSP`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 사용 가능 코드: AASHTO Standard, AASHTO LRFD, PENNDOT, Korea, Taiwan

### Request Body – Auto Input

```json
{
  "Assign": {
    "1": {
      "TYPE": "AutoInput",
      "GROUP_NAME": "CrossBeam"
    }
  }
}
```

### Request Body – User Input (Beam)

```json
{
  "Assign": {
    "1": {
      "TYPE": "UserInput",
      "ELEMENT_NO": 179,
      "ELEMENT_TYPE": "BEAM",
      "POSITION": "Both"
    },
    "2": {
      "TYPE": "UserInput",
      "ELEMENT_NO": 180,
      "ELEMENT_TYPE": "BEAM",
      "POSITION": "End-I"
    }
  }
}
```

### Request Body – User Input (Plate)

```json
{
  "Assign": {
    "1": {
      "TYPE": "UserInput",
      "ELEMENT_NO": 540,
      "ELEMENT_TYPE": "PLATE"
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Input Type (`"AutoInput"` / `"UserInput"`) ¹⁾ | `"TYPE"` | String | – | Required |
| 2 | Structure Group Name (AutoInput 전용) | `"GROUP_NAME"` | String | – | Required (AutoInput) |
| 3 | Element ID | `"ELEMENT_NO"` | Integer | – | Required (UserInput) |
| 4 | Element Type (`"BEAM"` / `"PLATE"`) | `"ELEMENT_TYPE"` | String | – | Required (UserInput) |
| 5 | Position (`"Both"` / `"End-I"` / `"End-J"`, BEAM 전용) | `"POSITION"` | String | – | Required (BEAM) |

> ¹⁾ AutoInput은 AASHTO LRFD에서만 사용 가능

### Python 예제

```python
# Auto Input (AASHTO LRFD 전용)
result = mv_post("MLSP", {
    "1": {
        "TYPE": "AutoInput",
        "GROUP_NAME": "CrossBeam",
    }
})

# User Input (Beam Element)
result2 = mv_post("MLSP", {
    "1": {"TYPE": "UserInput", "ELEMENT_NO": 179, "ELEMENT_TYPE": "BEAM", "POSITION": "Both"},
    "2": {"TYPE": "UserInput", "ELEMENT_NO": 180, "ELEMENT_TYPE": "BEAM", "POSITION": "End-I"},
    "3": {"TYPE": "UserInput", "ELEMENT_NO": 540, "ELEMENT_TYPE": "PLATE"},
})
print(result, result2)
```

---

## 24. /db/MLSR – Lane Support – Reactions at Interior Piers

> 연속교 내측 지점부 반력 차선 지지 절점을 지정합니다.

**Input URI:** `{base url}/db/MLSR`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 사용 가능 코드: AASHTO LRFD, PENNDOT

### Request Body

```json
{
  "Assign": {
    "60":  {"NODE": 0},
    "201": {"NODE": 0},
    "202": {"NODE": 0},
    "203": {"NODE": 0}
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Fixed Value: 0 (Key는 Node ID) | `"NODE"` | Integer | – | Required |

> **참고:** `"Assign"` 오브젝트의 키 값이 지지 절점 ID이며, 값 `{"NODE": 0}`은 고정값입니다.

### Python 예제

```python
# 내측 지점부 절점 60, 201, 202 지정
result = mv_post("MLSR", {
    "60":  {"NODE": 0},
    "201": {"NODE": 0},
    "202": {"NODE": 0},
})
print(result)
```

---

## 25. /db/DYLA – Dynamic Load Allowance

> 구조 그룹별로 충격 계수(Dynamic Load Allowance, IM)를 설정합니다.

**Input URI:** `{base url}/db/DYLA`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 사용 가능 코드: AASHTO LRFD, PENNDOT, KSCE-LSD15

### Request Body

```json
{
  "Assign": {
    "1": {
      "FACTOR": 15,
      "ITEMS": ["Main4", "Main5", "Main6"]
    },
    "2": {
      "FACTOR": 10,
      "ITEMS": ["Main1", "Main2", "Main7"]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Impact Factor (%) | `"FACTOR"` | Number | – | Required |
| 2 | Selected Structure Group List | `"ITEMS"` | Array[String] | – | Required |

### Python 예제

```python
result = mv_post("DYLA", {
    "1": {"FACTOR": 33, "ITEMS": ["Deck_Joints"]},
    "2": {"FACTOR": 25, "ITEMS": ["All_Other_Components"]},
    "3": {"FACTOR": 15, "ITEMS": ["Fatigue"]},
})
print(result)
```

---

## 26. /db/IMPF – Additional Impact Factor

> 차선별, 요소 타입별로 추가 충격 계수 또는 유효 경간 길이를 설정합니다.

**Input URI:** `{base url}/db/IMPF`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 사용 가능 코드: Korea

### Request Body – Line Lane (Impact Factor)

```json
{
  "Assign": {
    "82": {
      "ITEMS": [
        {
          "ID": 1,
          "LANE_TYPE": "LINE",
          "LANE_NAME": "LL_01",
          "FACT_TYPE": "IMPACT_FACT",
          "FACTOR": 0.3
        }
      ]
    }
  }
}
```

### Request Body – Line Lane (Effective Span Length – Auto Calculation)

```json
{
  "Assign": {
    "163": {
      "ITEMS": [
        {
          "ID": 1,
          "LANE_TYPE": "LINE",
          "LANE_NAME": "LL_01",
          "ELEMTYPE": "BEAM",
          "FACT_TYPE": "EFF_SPAN_LEN_AUTO",
          "FACTOR": 0,
          "PARTS": [true, true, true, true, true],
          "COMPONENTS": [true, true, true, true, true, true, false, false]
        }
      ]
    }
  }
}
```

### Request Body – Surface Lane

```json
{
  "Assign": {
    "527": {
      "ITEMS": [
        {
          "ID": 1,
          "LANE_TYPE": "SURFACE",
          "LANE_NAME": "SL_01",
          "FACT_TYPE": "IMPACT_FACT",
          "FACTOR": 0.3
        }
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Additional Impact Factor Items | `"ITEMS"` | Array[Object] | – | Required |

**Line Lane / Surface Lane (Impact Factor, Effective Span Length – User Input)**

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Serial Number | `"ID"` | Integer | Required |
| 2 | Lane Type (`"LINE"` / `"SURFACE"`) | `"LANE_TYPE"` | String | Required |
| 3 | Lane Name | `"LANE_NAME"` | String | Required |
| 4 | Factor Type (`"IMPACT_FACT"` / `"EFF_SPAN_LEN_USER"`) | `"FACT_TYPE"` | String | Required |
| 5 | Factor | `"FACTOR"` | Number | Required |

**Line Lane (Effective Span Length – Auto Calculation)**

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Serial Number | `"ID"` | Integer | Required |
| 2 | Lane Type: `"LINE"` | `"LANE_TYPE"` | String | Required |
| 3 | Lane Name | `"LANE_NAME"` | String | Required |
| 4 | Element Type (`"BEAM"` / `"TRUSS"` / `"PLATE"`) | `"ELEMTYPE"` | String | Required |
| 5 | Factor Type: `"EFF_SPAN_LEN_AUTO"` | `"FACT_TYPE"` | String | Required |
| 6 | Parts (Beam: [i, 1/4, 1/2, 3/4, j] / Plate: [cent, i, j, k, l]) | `"PARTS"` | Array[Boolean] | Required |
| 7 | Components (Beam: [My_max, My_min, Mz_max, Mz_min, Fx_max, Fx_min] / Truss: [Max, Min] / Plate: [Mxx_max, Mxx_min, Myy_max, Myy_min, Fxx_max, Fxx_min, Fyy_max, Fyy_min]) | `"COMPONENTS"` | Array[Boolean] | Required |

### Python 예제

```python
# 보 요소 자동 유효 경간 길이 계산
result = mv_post("IMPF", {
    "163": {
        "ITEMS": [
            {
                "ID": 1,
                "LANE_TYPE": "LINE",
                "LANE_NAME": "LL_01",
                "ELEMTYPE": "BEAM",
                "FACT_TYPE": "EFF_SPAN_LEN_AUTO",
                "FACTOR": 0,
                "PARTS": [True, True, True, True, True],
                "COMPONENTS": [True, True, True, True, True, True, False, False],
            }
        ]
    }
})
print(result)
```

---

## 27. /db/DYFG – Railway Dynamic Factor

> Eurocode 기반 철도 동적 계수(φ)를 전체 모델에 적용합니다.

**Input URI:** `{base url}/db/DYFG`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 사용 가능 코드: Eurocode

### Request Body – Auto Input

```json
{
  "Assign": {
    "1": {
      "INPUT_TYPE": 0,
      "LENGTH": 12,
      "MAINTAIN_TYPE": 0,
      "OPT_REDUCE_EFF": true,
      "HEIGHT_COVER": 1
    }
  }
}
```

### Request Body – User Input

```json
{
  "Assign": {
    "1": {
      "INPUT_TYPE": 1,
      "DYN_FACTOR": 1.2611627362707665
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Input Type (0=Auto, 1=User) | `"INPUT_TYPE"` | Integer | – | Required |
| 2 | Determinant Length (Lφ) | `"LENGTH"` | Number | – | Required (Auto) |
| 3 | Quality of Track Maintenance (0=Carefully, 1=Standard) | `"MAINTAIN_TYPE"` | Integer | – | Required (Auto) |
| 4 | Consider Reduced Dynamic Effect | `"OPT_REDUCE_EFF"` | Boolean | false | Optional |
| 5 | Height of Cover (h) (OPT_REDUCE_EFF=true 시) | `"HEIGHT_COVER"` | Number | – | Required |
| 6 | Dynamic Factor (φ) (INPUT_TYPE=1 시) | `"DYN_FACTOR"` | Number | – | Required (User) |

### Python 예제

```python
# Auto Input (전체 모델)
result = mv_post("DYFG", {
    "1": {
        "INPUT_TYPE": 0,
        "LENGTH": 12,
        "MAINTAIN_TYPE": 0,
        "OPT_REDUCE_EFF": True,
        "HEIGHT_COVER": 1,
    }
})
print(result)
```

---

## 28. /db/DYNF – Railway Dynamic Factor by Element

> Eurocode 기반 철도 동적 계수(φ)를 요소 단위로 적용합니다.  
> DYFG와 동일한 구조이나 `"Assign"` 키 값이 요소 ID입니다.

**Input URI:** `{base url}/db/DYNF`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 사용 가능 코드: Eurocode

### Request Body – Auto Input

```json
{
  "Assign": {
    "249": {
      "INPUT_TYPE": 0,
      "LENGTH": 12,
      "MAINTAIN_TYPE": 1,
      "OPT_REDUCE_EFF": true,
      "HEIGHT_COVER": 1
    }
  }
}
```

### Request Body – User Input

```json
{
  "Assign": {
    "88": {
      "INPUT_TYPE": 1,
      "DYN_FACTOR": 1.3
    }
  }
}
```

### Parameters

DYFG와 동일한 파라미터 구조. `"Assign"` 키 값이 개별 요소 ID.

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Input Type (0=Auto, 1=User) | `"INPUT_TYPE"` | Integer | – | Required |
| 2 | Determinant Length (Lφ) | `"LENGTH"` | Number | – | Required (Auto) |
| 3 | Quality of Track Maintenance (0=Carefully, 1=Standard) | `"MAINTAIN_TYPE"` | Integer | – | Required (Auto) |
| 4 | Consider Reduced Dynamic Effect | `"OPT_REDUCE_EFF"` | Boolean | false | Optional |
| 5 | Height of Cover (h) | `"HEIGHT_COVER"` | Number | – | Required (OPT_REDUCE_EFF=true) |
| 6 | Dynamic Factor (φ) | `"DYN_FACTOR"` | Number | – | Required (User) |

### Python 예제

```python
# 요소별 Auto Input
result = mv_post("DYNF", {
    "249": {
        "INPUT_TYPE": 0,
        "LENGTH": 12,
        "MAINTAIN_TYPE": 1,
        "OPT_REDUCE_EFF": True,
        "HEIGHT_COVER": 1,
    },
    "88": {
        "INPUT_TYPE": 1,
        "DYN_FACTOR": 1.3,
    },
})
print(result)
```

---

## 이동하중 모델링 워크플로우 예제

> 교량 이동하중 해석 전체 설정 순서 (KSCE-LSD15 기준)

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "<YOUR_MAPI_KEY>",
}

def post(ep, assign):
    r = requests.post(f"{BASE_URL}/db/{ep}", headers=HEADERS, json={"Assign": assign})
    r.raise_for_status()
    print(f"  ✓ {ep}: {r.status_code}")
    return r.json()

# Step 1: 이동하중 코드 설정
post("MVCD", {"1": {"CODE": "KSCE-LSD15"}})

# Step 2: 차선 정의 (Lane Element 방식)
post("LLAN", {
    "1": {
        "COMMON": {
            "LL_NAME": "LL_01", "LOAD_DIST": "LANE", "GROUP_NAME": "",
            "SKEW_START": 0, "SKEW_END": 0, "MOVING": "BOTH",
            "WHEEL_SPACE": 1.8, "WIDTH": 3, "OPT_AUTO_LANE": True, "ALLOW_WIDTH": 3,
        },
        "LANE_ITEMS": [
            {"ELEM": i, "ECC": -1.5} for i in range(1, 11)
        ],
    },
    "2": {
        "COMMON": {
            "LL_NAME": "LL_02", "LOAD_DIST": "LANE", "GROUP_NAME": "",
            "SKEW_START": 0, "SKEW_END": 0, "MOVING": "BOTH",
            "WHEEL_SPACE": 1.8, "WIDTH": 3, "OPT_AUTO_LANE": True, "ALLOW_WIDTH": 3,
        },
        "LANE_ITEMS": [
            {"ELEM": i, "ECC": 1.5} for i in range(1, 11)
        ],
    },
})

# Step 3: 차량 정의 (KSCE-LSD15 표준 차량 — MVLD_CODE 13 + VEH_KSCE_LSD15 스키마 사용)
post("MVHL", {
    "1": {
        "MVLD_CODE": 13, "VEHICLE_LOAD_NAME": "KL-510FTG",
        "VEHICLE_LOAD_NUM": 1, "VEHICLE_TYPE_NAME": "KL-510FTG",
        "STANDARD_CODE": "KSCE-LSD15",
        "VEH_KSCE_LSD15": {
            "LOAD_TYPE": 0, "DYN_LOAD_ALLOWANCE": 15,
            "LENGTH_LANE": 0, "LENGTH_LANE_USER": 0, "CONVERT_DIST_LOAD": False,
            "POINT_ITEMS": [
                {"POINT_LOAD": 38.4, "POINT_DIST": 3.6},
                {"POINT_LOAD": 108, "POINT_DIST": 1.2},
                {"POINT_LOAD": 108, "POINT_DIST": 7.2},
                {"POINT_LOAD": 153.6, "POINT_DIST": 0},
            ],
        },
    }
})

# Step 4: 이동하중 케이스 정의
post("MVLD", {
    "1": {
        "LCNAME": "MV_KSCE_1", "DESC": "", "TYPE": 0,
        "DEFAULT": {
            "SCALE_FACTORS": [1, 0.9, 0.8, 0.7, 0.65, 0.65],
            "COMB_OPTION": "COMBINED",
            "LANE_FACTOR_TYPE": 1,
            "SUB_LOAD_DATAS": [{
                "VEHICLE_TYPE": "VL", "VEHICLE_NAME": "KL-510FTG",
                "SCALE_FACTOR": 1, "MIN_LOADED_LANE": 1, "MAX_LOADED_LANE": 2,
                "LANE_NAMES": ["LL_01", "LL_02"],
            }],
        },
    }
})

# Step 5: 충격 계수 설정 (AASHTO LRFD 사용 시)
# post("DYLA", {"1": {"FACTOR": 33, "ITEMS": ["Deck"]}})

print("이동하중 모델링 완료!")
```
