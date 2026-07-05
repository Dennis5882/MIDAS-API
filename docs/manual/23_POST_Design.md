# 23. POST – Design Tables (설계 결과 테이블)

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

이 파트는 **설계(Design) 결과**를 추출하는 POST 엔드포인트를 다룹니다. 설계 코드 체크(강재), P-M 상관도(Concrete/SRC), 그리고 RC·강재·SRC·냉간성형 부재의 **설계용 부재력(Design Forces)** 테이블을 포함합니다.

설계 결과 엔드포인트는 **세 가지 URI 패턴**으로 나뉩니다.

| # | 엔드포인트 | URI | 메서드 | 요청 형식 |
|---|-----------|-----|--------|-----------|
| 1 | [P-M Interaction Diagram](#1-p-m-interaction-diagram) | `post/PM` | POST | 빈 `Argument` |
| 2 | [Steel Code Check](#2-steel-code-check) | `post/STEELCODECHECK` | POST | 빈 `Argument` |
| 3 | [Concrete Design – Beam Design Forces](#3-concrete-design--beam-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=BEAMDESIGNFORCES` |
| 4 | [Concrete Design – Column Design Forces](#4-concrete-design--column-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=COLUMNDESIGNFORCES` |
| 5 | [Concrete Design – Brace Design Forces](#5-concrete-design--brace-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=BRACEDESIGNFORCES` |
| 6 | [Concrete Design – Wall Design Forces](#6-concrete-design--wall-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=WALLDESIGNFORCES` |
| 7 | [Steel Design – Steel Member Design Forces](#7-steel-design--steel-member-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=STEELMEMBERDESIGNFORCES` |
| 8 | [SRC Design – SRC Beam Design Forces](#8-src-design--src-beam-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=SRCBEAMDESIGNFORCES` |
| 9 | [SRC Design – SRC Column Design Forces](#9-src-design--src-column-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=SRCCOLUMNDESIGNFORCES` |
| 10 | [Cold Formed Design – Cold Formed Steel Member Design Forces](#10-cold-formed-design--cold-formed-steel-member-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=COLDFORMEDSTEELMEMBERDESIGNFORCES` |

> **선행 조건:** 설계 결과를 조회하려면 먼저 해석(Analysis)과 **설계(Design)** 가 완료되어 있어야 합니다. 설계 코드·부재·철근 등의 설정은 **[24_DB_Design.md](./24_DB_Design.md)** 를 참고하세요.

---

## 공통 사항 (Design Forces 테이블, #3~#10)

`post/TABLE`을 사용하는 8개의 설계용 부재력 테이블(#3~#10)은 **19장(Analysis Result Tables)과 동일한 공통 요청 구조**를 사용합니다. 요청 바디의 `"Argument"` 객체에서 `TABLE_TYPE`으로 테이블을 선택하며, 아래 파라미터를 공통으로 지원합니다.

### Input URI

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 공통 Request 파라미터

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 응답 테이블 제목 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 결과 테이블 타입 (테이블별 고정값, 각 절 참조) | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 결과 테이블 저장 경로 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 응답 단위 설정 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 힘(Force) | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 길이(Length) | `UNIT.DIST` | String | — | Optional |
| 5 | 응답 숫자 형식 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 숫자 형식 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 소수 자릿수 (0~15) | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 부재 위치(단부) 지정 · `"PartI"` / `"PartJ"` 등 | `"PARTS"` | Array [String] | All | Optional |
| 7 | 결과 테이블 표시 열 | `"COMPONENTS"` | Array [String] | All | Optional |
| 8 | 요소/부재 지정 (아래 3방식 중 하나) | `"NODE_ELEMS"` | Object | All | Optional |
| 8-1 | 방식1: ID 각각 지정 (예: `[1, 2, 3]`) | `NODE_ELEMS.KEYS` | Array [Integer] | — | Optional |
| 8-2 | 방식2: ID 범위 지정 (예: `"1 to 5"`) | `NODE_ELEMS.TO` | String | — | Optional |
| 8-3 | 방식3: 구조 그룹명 지정 (예: `"SG1"`) | `NODE_ELEMS.STRUCTURE_GROUP_NAME` | String | — | Optional |

### 공통 Response 구조

```json
{
  "<TABLE_TYPE>": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."], ["2", "..."]]
  }
}
```

> **`Type` 열:** 설계용 부재력 테이블의 `Type` 열은 하중조합 극값 종류(`Max` / `Min`)를 의미하며, `LComName` 열은 설계 하중조합 이름입니다.

---

## 1. P-M Interaction Diagram

> **기능:** RC/SRC 기둥·부재의 **P-M 상관도(축력–모멘트 상관곡선)** 데이터를 추출합니다. 별도 인자 없이 현재 모델의 설계 결과 전체를 반환합니다.

### Input URI

```
{base url}/post/PM
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "PM": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "argument": {
        "type": "object",
        "properties": {}
      }
    }
  }
}
```

### Request / Response JSON

요청 바디의 `"Argument"` 는 **빈 객체**입니다. 필터링 없이 현재 설계 결과의 P-M 상관도 데이터셋을 반환합니다.

**POST Request Body**

```json
{
  "Argument": {}
}
```

> **참고:** 매뉴얼에는 고정된 `HEAD`/`DATA` 응답 예시가 공개되어 있지 않습니다. 응답에는 부재/단면별 P-M 상관곡선 좌표 및 소요강도 점 데이터가 포함됩니다. 실제 응답 키 구조는 실행 환경의 설계 코드 설정에 따릅니다.

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "MAPI-Key": "여기에_발급받은_키_입력",
    "Content-Type": "application/json",
}

# P-M 상관도 데이터 추출 (인자 없이 전체 조회)
payload = {"Argument": {}}

res = requests.post(f"{BASE_URL}/post/PM", json=payload, headers=HEADERS)
res.raise_for_status()

pm_data = res.json()
print("P-M Interaction Diagram 응답 키:", list(pm_data.keys()))
```

---

## 2. Steel Code Check

> **기능:** 강재 부재의 **설계 코드 체크 결과**(단면·요소별 조합강도비, 세장비, 처짐, 허용처짐)를 추출합니다.

### Input URI

```
{base url}/post/STEELCODECHECK
```

### Active Methods

`POST`

### Response 필드

| No. | 설명 | Key | Value 타입 |
|-----|------|-----|-----------|
| 1 | 단면 데이터 배열 | `"vSECT"` | Array [Object] |
| 1-(1) | └ 단면 ID | `SECT` | Number |
| 1-(2) | └ 조합 강도비 (Combined Strength Ratio) | `RAT` | Number |
| 1-(3) | └ 세장비 (Slenderness Ratio) | `SLN` | Number |
| 1-(4) | └ 처짐 (Deflection) | `DEF` | Number |
| 1-(5) | └ 허용 처짐 (Allowable Deflection) | `DEFA` | Number |
| 2 | 요소 데이터 배열 | `"vELEM"` | Array [Object] |
| 2-(1) | └ 요소 ID | `ELEM` | Integer |
| 2-(2) | └ 조합 강도비 | `RAT` | Number |
| 2-(3) | └ 세장비 | `SLN` | Number |
| 2-(4) | └ 처짐 | `DEF` | Number |
| 2-(5) | └ 허용 처짐 | `DEFA` | Number |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {}
}
```

**Response Body**

```json
{
  "vSECT": [
    {
      "SECT": 1,
      "RAT": 0.611917806624809,
      "SLN": 0.07680554887655298,
      "DEF": -0.0006249514999156769,
      "DEFA": 0.02279999999996812
    },
    {
      "SECT": 2,
      "RAT": 0.4296192038079335,
      "SLN": 0.04946798063250228,
      "DEF": -0.0006016184741690078,
      "DEFA": 0.02279999999995198
    },
    {
      "SECT": 3,
      "RAT": 0.5268570141827795,
      "SLN": 0.06909209873374429,
      "DEF": 0,
      "DEFA": 0.0014103010198308647
    }
  ],
  "vELEM": [
    {
      "ELEM": 10,
      "RAT": 0.12369675848216558,
      "SLN": 0.0023911209516698797,
      "DEF": 1.0658046060985082e-07,
      "DEFA": 0.0011020776874479453
    },
    {
      "ELEM": 11,
      "RAT": 0.13438019223768993,
      "SLN": 0.04707685968078899,
      "DEF": -0.0001707694272293503,
      "DEFA": 0.021697922312579977
    },
    {
      "ELEM": 12,
      "RAT": 0.20046527423634042,
      "SLN": 0.0494679806323982,
      "DEF": -0.000402594921254891,
      "DEFA": 0.022799999999999952
    }
  ]
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "MAPI-Key": "여기에_발급받은_키_입력",
    "Content-Type": "application/json",
}

# 강재 설계 코드 체크 결과 조회 (인자 없음)
res = requests.post(f"{BASE_URL}/post/STEELCODECHECK", json={"Argument": {}}, headers=HEADERS)
res.raise_for_status()
data = res.json()

# 강도비(RAT)가 1.0 이상인 과설계(N.G.) 단면/요소 필터링
ng_sect = [s for s in data.get("vSECT", []) if s["RAT"] >= 1.0]
ng_elem = [e for e in data.get("vELEM", []) if e["RAT"] >= 1.0]

print(f"검토 단면 수: {len(data.get('vSECT', []))}, N.G. 단면: {len(ng_sect)}")
print(f"검토 요소 수: {len(data.get('vELEM', []))}, N.G. 요소: {len(ng_elem)}")

# 최대 강도비 요소 출력
if data.get("vELEM"):
    worst = max(data["vELEM"], key=lambda e: e["RAT"])
    print(f"최대 강도비 요소: ELEM {worst['ELEM']}, RAT = {worst['RAT']:.3f}")
```

---

## 3. Concrete Design – Beam Design Forces

> **기능:** RC 설계용 **보(Beam) 부재 설계력**을 추출합니다. 휨설계 기준의 축력·비틀림·정/부 모멘트를 제공합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"BEAMDESIGNFORCES"` | RC 보 설계 부재력 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(-)", "My(+)"]`

| 열 | 의미 |
|----|------|
| `Memb` | 부재 번호 |
| `Part` | 부재 단부/위치 (I, J 등) |
| `LComName` | 설계 하중조합 이름 |
| `Type` | 극값 종류 (`Max`/`Min`) |
| `Fz` | 전단력 |
| `Mx` | 비틀림 모멘트 |
| `My(-)` / `My(+)` | 부(-)/정(+) 휨모멘트 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "BEAMDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [1, 2, 3]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(-)", "My(+)"]
  }
}
```

**Response Body**

```json
{
  "BEAMDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(-)", "My(+)"],
    "DATA": [
      ["1", "1", "I", "Strength", "Max", "41.454", "0.000", "73.244", "36.622"]
    ]
  }
}
```

### Python 예제

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "MAPI-Key": "여기에_발급받은_키_입력",
    "Content-Type": "application/json",
}

def get_design_table(table_type, keys=None, parts=None, components=None):
    """설계용 부재력 테이블 공통 조회 헬퍼"""
    arg = {
        "TABLE_TYPE": table_type,
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
    }
    if keys is not None:
        arg["NODE_ELEMS"] = {"KEYS": keys}
    if parts is not None:
        arg["PARTS"] = parts
    if components is not None:
        arg["COMPONENTS"] = components
    res = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    res.raise_for_status()
    return res.json()[table_type]

# RC 보 설계 부재력 조회 (부재 1,2,3의 양 단부)
beam = get_design_table(
    "BEAMDESIGNFORCES",
    keys=[1, 2, 3],
    parts=["PartI", "PartJ"],
)
print("HEAD:", beam["HEAD"])
for row in beam["DATA"]:
    print(row)
```

---

## 4. Concrete Design – Column Design Forces

> **기능:** RC 설계용 **기둥(Column) 부재 설계력**(3축 힘·모멘트)을 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"COLUMNDESIGNFORCES"` | RC 기둥 설계 부재력 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

| 열 | 의미 |
|----|------|
| `Fx` / `Fy` / `Fz` | 축력 및 전단력 (부재 좌표계) |
| `Mx` / `My` / `Mz` | 비틀림 및 2축 휨모멘트 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "COLUMNDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [56]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "COLUMNDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "56", "I", "Strength", "Max", "2510.159", "9.161", "0.271", "0.000", "13.114", "15.975"]
    ]
  }
}
```

### Python 예제

```python
# 3번 예제의 get_design_table() 헬퍼 재사용
column = get_design_table(
    "COLUMNDESIGNFORCES",
    keys=[56],
    parts=["PartI", "PartJ"],
)
print("HEAD:", column["HEAD"])
for row in column["DATA"]:
    print(row)
```

---

## 5. Concrete Design – Brace Design Forces

> **기능:** RC 설계용 **가새(Brace) 부재 설계력**(3축 힘·모멘트)을 추출합니다. 응답 구조는 기둥과 동일합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"BRACEDESIGNFORCES"` | RC 가새 설계 부재력 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "BRACEDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [52]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "BRACEDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "52", "I", "Strength", "Max", "2510.159", "9.161", "0.271", "0.000", "13.114", "15.975"]
    ]
  }
}
```

### Python 예제

```python
# 가새 설계 부재력 조회
brace = get_design_table("BRACEDESIGNFORCES", keys=[52], parts=["PartI", "PartJ"])
print("HEAD:", brace["HEAD"])
for row in brace["DATA"]:
    print(row)
```

---

## 6. Concrete Design – Wall Design Forces

> **기능:** RC 설계용 **벽체(Wall) 부재 설계력**을 추출합니다. 벽체 ID(`WID`)와 층(`Story`) 정보가 추가됩니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"WALLDESIGNFORCES"` | RC 벽체 설계 부재력 |

### Response HEAD

`["Index", "WID", "Story", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

| 열 | 의미 |
|----|------|
| `WID` | 벽체 ID |
| `Story` | 층 이름 |
| `Part` | 벽체 위치 (`Top`/`Bottom` 등) |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "WALLDESIGNFORCES",
    "TABLE_TYPE": "WALLDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [1]
    },
    "COMPONENTS": ["Index", "WID", "Story", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "WALLDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "WID", "Story", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "1", "1F", "Top", "Strength", "Max", "3314.580", "0.000", "19.717", "0.000", "11.341", "0.000"]
    ]
  }
}
```

### Python 예제

```python
# 벽체 설계 부재력 조회 (WID로 지정)
wall = get_design_table("WALLDESIGNFORCES", keys=[1])
print("HEAD:", wall["HEAD"])
for row in wall["DATA"]:
    print(row)
```

---

## 7. Steel Design – Steel Member Design Forces

> **기능:** 강재 설계용 **부재 설계력**(3축 힘·모멘트)을 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"STEELMEMBERDESIGNFORCES"` | 강재 부재 설계 부재력 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "STEELMEMBERDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [1]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "STEELMEMBERDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "1", "I", "sLCB1", "Max", "-17.635", "-0.009", "0.489", "0.000", "-0.000", "-0.000"]
    ]
  }
}
```

### Python 예제

```python
# 강재 부재 설계 부재력 조회 (전체 요소)
steel = get_design_table("STEELMEMBERDESIGNFORCES", parts=["PartI", "PartJ"])
print("HEAD:", steel["HEAD"])
print(f"총 {len(steel['DATA'])}개 행")
for row in steel["DATA"][:5]:
    print(row)
```

---

## 8. SRC Design – SRC Beam Design Forces

> **기능:** SRC(철골 철근콘크리트 합성) 설계용 **보 부재 설계력**을 추출합니다. 응답 열 구성은 RC 보와 유사하나 정/부 모멘트 열 순서(`My(+)`, `My(-)`)에 유의합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"SRCBEAMDESIGNFORCES"` | SRC 보 설계 부재력 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(+)", "My(-)"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "SRCBEAMDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [316]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(+)", "My(-)"]
  }
}
```

**Response Body**

```json
{
  "SRCBEAMDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(+)", "My(-)"],
    "DATA": [
      ["1", "316", "I", "rLCB6", "Max", "152.087", "0.000", "72.164", "244.627"]
    ]
  }
}
```

### Python 예제

```python
# SRC 보 설계 부재력 조회
src_beam = get_design_table("SRCBEAMDESIGNFORCES", keys=[316], parts=["PartI", "PartJ"])
print("HEAD:", src_beam["HEAD"])
for row in src_beam["DATA"]:
    print(row)
```

---

## 9. SRC Design – SRC Column Design Forces

> **기능:** SRC 설계용 **기둥 부재 설계력**(3축 힘·모멘트)을 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"SRCCOLUMNDESIGNFORCES"` | SRC 기둥 설계 부재력 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "SRCCOLUMNDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [365]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "SRCCOLUMNDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "365", "I", "rLCB6", "Max", "-3960.926", "40.952", "4.948", "0.000", "19.165", "69.926"]
    ]
  }
}
```

### Python 예제

```python
# SRC 기둥 설계 부재력 조회
src_col = get_design_table("SRCCOLUMNDESIGNFORCES", keys=[365], parts=["PartI", "PartJ"])
print("HEAD:", src_col["HEAD"])
for row in src_col["DATA"]:
    print(row)
```

---

## 10. Cold Formed Design – Cold Formed Steel Member Design Forces

> **기능:** 냉간성형강(Cold Formed Steel) 설계용 **부재 설계력**(3축 힘·모멘트)을 추출합니다.

### `TABLE_TYPE`

| 값 | 설명 |
|----|------|
| `"COLDFORMEDSTEELMEMBERDESIGNFORCES"` | 냉간성형강 부재 설계 부재력 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "COLDFORMEDSTEELMEMBERDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [313]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "COLDFORMEDSTEELMEMBERDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "313", "I", "cfLCB1", "Max", "-0.000", "0.000", "-58.761", "0.000", "-116.465", "0.000"]
    ]
  }
}
```

### Python 예제

```python
# 냉간성형강 부재 설계 부재력 조회
cf = get_design_table("COLDFORMEDSTEELMEMBERDESIGNFORCES", keys=[313], parts=["PartI", "PartJ"])
print("HEAD:", cf["HEAD"])
for row in cf["DATA"]:
    print(row)
```

---

## End-to-End Workflow

해석·설계 완료 후 강재 코드 체크 결과와 RC 부재별 설계력을 한 번에 수집하는 예제입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "MAPI-Key": "여기에_발급받은_키_입력",
    "Content-Type": "application/json",
}


def post_table(table_type, **arg_extra):
    """post/TABLE 설계 부재력 공통 조회"""
    arg = {
        "TABLE_TYPE": table_type,
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
    }
    arg.update(arg_extra)
    res = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    res.raise_for_status()
    return res.json()[table_type]


def steel_code_check():
    """강재 설계 코드 체크 결과"""
    res = requests.post(f"{BASE_URL}/post/STEELCODECHECK", json={"Argument": {}}, headers=HEADERS)
    res.raise_for_status()
    return res.json()


# 1) 강재 코드 체크 — 최대 강도비 요소 확인
scc = steel_code_check()
if scc.get("vELEM"):
    worst = max(scc["vELEM"], key=lambda e: e["RAT"])
    print(f"[Steel] 최대 강도비 요소 ELEM {worst['ELEM']}: RAT = {worst['RAT']:.3f}")

# 2) RC 보/기둥/벽체 설계력 일괄 수집
for tt, label in [
    ("BEAMDESIGNFORCES", "RC 보"),
    ("COLUMNDESIGNFORCES", "RC 기둥"),
    ("WALLDESIGNFORCES", "RC 벽체"),
]:
    tbl = post_table(tt, PARTS=["PartI", "PartJ"])
    print(f"[{label}] {len(tbl['DATA'])}개 행 — HEAD: {tbl['HEAD']}")

# 3) SRC / 냉간성형 부재 설계력
for tt, label in [
    ("SRCBEAMDESIGNFORCES", "SRC 보"),
    ("SRCCOLUMNDESIGNFORCES", "SRC 기둥"),
    ("COLDFORMEDSTEELMEMBERDESIGNFORCES", "냉간성형강"),
]:
    tbl = post_table(tt, PARTS=["PartI", "PartJ"])
    print(f"[{label}] {len(tbl['DATA'])}개 행")
```

---

> **다음 파트:** **[24_DB_Design.md](./24_DB_Design.md)** — RC·Steel 설계 코드 설정, 설계 부재(Design Member), 비지지 길이(Unbraced Length) 등 설계 입력용 DB 엔드포인트(11개)를 다룹니다.
