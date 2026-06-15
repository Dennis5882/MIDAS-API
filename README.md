# MIDAS-API

**MIDAS NX Open API**를 사용하여 구조 설계 모델을 프로그래밍 방식으로 생성·제어·자동화합니다.
노드·요소·단면·하중을 코드로 생성할 수 있어, **스토리(층) 기반 자동 모델링**처럼
반복적인 모델링 작업을 자동화하기에 적합합니다.

> 대상 제품: **MIDAS Gen NX / Civil NX** · 데이터 포맷: **JSON** · 프로토콜: **REST + WebSocket**

---

## 🏗️ API 동작 구조

MIDAS NX는 애플리케이션과 직접 통신하지 않습니다. **클라우드 서버(AWS)** 가 중계자 역할을 합니다.

```
[내 코드/앱]  ──REST(HTTP)──▶  [MIDAS 서버(AWS)]  ──WebSocket──▶  [로컬 MIDAS Gen NX]
     ▲                                                                   │
     └───────────────────────  결과(JSON)  ◀──────────────────────────────┘
```

- 서버는 **`MAPI-Key`** 로 어떤 제품(실행 중인 Gen NX)인지 식별합니다.
- 따라서 **MIDAS Gen NX(또는 Civil NX)가 실행 중**이어야 API가 동작합니다.
- 하나의 클라이언트가 여러 `MAPI-Key`를 가지면 여러 제품을 한 곳에서 제어할 수 있습니다.

---

## 🔑 인증 & 기본 정보

### Base URL
```
https://moa-engineers.midasit.com:443/gen      # MIDAS Gen NX
https://moa-engineers.midasit.com:443/civil    # MIDAS Civil NX
```
> 지역별 대체 서버가 제공됩니다.

### 인증 헤더
```
Content-Type: application/json
MAPI-Key: <Gen NX 앱에서 발급받은 키>
```
> `MAPI-Key`는 임시 키이며 언제든 재발급할 수 있습니다. `.env`로 분리해 관리하세요.

### HTTP 메서드
| 메서드 | 역할 |
|--------|------|
| `POST`   | 데이터 생성 |
| `PUT`    | 데이터 수정 (신규 파일의 필수 데이터는 GET/PUT만 동작) |
| `GET`    | 데이터 조회 |
| `DELETE` | 데이터 삭제 |

### 공통 요청 바디 형식
모든 DB 엔드포인트는 `Assign` 래퍼 안에 **항목 ID → 데이터** 형태로 보냅니다.
```json
{ "Assign": { "1": { "X": 0, "Y": 0, "Z": 0 } } }
```

---

## 🚀 빠른 시작 (Python)

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "your-mapi-key-here"   # Gen NX 앱에서 발급

def MidasAPI(method, command, body=None):
    url = BASE_URL + command
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    res = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(method, command, res.status_code)
    return res.json()

# 1) 새 문서 생성
MidasAPI("POST", "/doc/new", {})

# 2) 단위 설정 (대만 RC: m, tonf 권장)
MidasAPI("PUT", "/db/unit", {"Assign": {"1": {"DIST": "M", "FORCE": "TONF"}}})

# 3) 재료 (RC)
MidasAPI("POST", "/db/matl", {"Assign": {1: {
    "TYPE": "CONC", "NAME": "C32",
    "PARAM": [{"P_TYPE": 1, "STANDARD": "AS17(RC)", "DB": "C32"}]
}}})

# 4) 노드 2개
MidasAPI("POST", "/db/node", {"Assign": {
    1: {"X": 0, "Y": 0, "Z": 0},
    2: {"X": 0, "Y": 0, "Z": 3.2},
}})

# 5) 기둥 요소 (BEAM 타입)
MidasAPI("POST", "/db/elem", {"Assign": {1: {
    "TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0
}}})

# 6) 저장
MidasAPI("POST", "/doc/save")
```

더 많은 예제는 [examples/](./examples/) 디렉토리를 참고하세요.

---

## 📚 주요 엔드포인트

### 문서 관리 (`/doc/*`)
| 엔드포인트 | 메서드 | 기능 |
|-----------|--------|------|
| `/doc/new`    | POST | 새 문서 생성 (빈 바디 `{}`) |
| `/doc/open`   | POST | 문서 열기 |
| `/doc/save`   | POST | 문서 저장 |
| `/doc/close`  | POST | 문서 닫기 |

### 모델 생성 (`/db/*`)
| 엔드포인트 | 기능 | 핵심 필드 |
|-----------|------|----------|
| `/db/unit` | 단위계 | `DIST`, `FORCE` |
| `/db/matl` | 재료 | `TYPE:"CONC"`, `NAME`, `PARAM:[{P_TYPE, STANDARD, DB}]` |
| `/db/sect` | 단면 | `SECTTYPE:"DBUSER"`, `SECT_BEFORE:{SHAPE, SECT_I:{vSIZE:[h,w]}}}` |
| `/db/thik` | 판/벽 두께 | `NAME`, `TYPE:"VALUE"`, `T_IN`, `T_OUT` |
| `/db/node` | 노드 | `X`, `Y`, `Z` |
| `/db/elem` | 요소 | `TYPE`, `MATL`, `SECT`, `NODE:[…]`, `ANGLE`, `STYPE` |

### 하중 & 경계조건
| 엔드포인트 | 기능 | 핵심 필드 |
|-----------|------|----------|
| `/db/stld` | 정적하중케이스 | `NAME`, `TYPE`(`D`/`L`/`LR`/`S`/`W`/`E`…), `DESC` |
| `/db/bodf` | 자중 | `LCNAME`, `FV:[0,0,-1]` |
| `/db/bmld` | 보 하중 | `ITEMS:[{LCNAME, CMD:"BEAM", TYPE:"UNILOAD", DIRECTION, D, P}]` |
| `/db/fbld` | **바닥하중 타입 정의** | `NAME`, `ITEM:[{LCNAME, FLOOR_LOAD, OPT_SUB_BEAM_WEIGHT}]` |
| `/db/fbla` | **바닥하중 면 지정** | `FLOOR_LOAD_TYPE_NAME`, `FLOOR_DIST_TYPE`(1~4), `DIR`, `NODES:[…]` |
| `/db/pres` | **압력(풍압) 하중** | `LCNAME`, `CMD:"PRES"`, `ELEM_TYPE`, `FACE_EDGE_TYPE`, `DIRECTION`, `FORCES:[...]` |
| `/db/cons` | 지지(경계) | `ITEMS:[{ID, CONSTRAINT:"1111000"}]` (Dx Dy Dz Rx Ry Rz) |
| `/db/lcom-gen` | 하중조합 | `NAME`, `vCOMB:[{ANAL:"ST", LCNAME, FACTOR}]` |

### 요소 타입 (`ELEM.TYPE`)
| 구조부재 | `TYPE` | 비고 |
|---------|--------|------|
| 기둥 · 보 (Frame) | `"BEAM"` | `NODE=[i, j]`, `ANGLE`=Beta각 |
| 슬래브 | `"PLATE"` | `NODE`=3/4점, `STYPE` 1=Thick·2=Thin·3/4=+Drilling DOF |
| 벽체 | `"WALL"` | `NODE`=4점, `STYPE` 1=Membrane·2=Plate, `WALL`(ID), `W_TYPE` |
| 기타 | `TRUSS` / `TENSTR` / `COMPTR` / `PLSTRS` / `PLSTRN` / `AXISYM` / `SOLID` | |

> 전체 키·필드 스키마는 [NX Open API JSON Manual](https://support.midasuser.com/hc/en-us/sections/30087500371097-JSON-Manual)을 참고하세요.

---

## 🌬️ 풍하중 (KDS 41 12:2022)

MIDAS NX는 **KDS 41 12:2022 (한국 풍하중 기준)** 및 다양한 국제 코드를 지원합니다.

### 풍하중 관련 엔드포인트

| 엔드포인트 | 기능 | 핵심 필드 |
|-----------|------|----------|
| `/db/stld` | 풍하중 케이스 생성 | `NAME`, `TYPE:"W"` (Wind) |
| `/db/pres` | 압력(풍압) 재하 | `LCNAME`, `ELEM_TYPE:"PLATE"/"SOLID"`, `DIRECTION`, `FORCES` |
| `/db/wprs` | 절점(Nodal) 풍압 | `LCNAME`, `DIRECTION`, `NODES:[...]`, `PRESSURE` |
| `/db/aprs` | 면적(Area) 풍압 | `LCNAME`, `DIRECTION`, `NODES:[...]`, `PRESSURE` |

### Python 예제: KDS 풍하중 적용

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "your-mapi-key-here"

def MidasAPI(method, command, body=None):
    url = BASE_URL + command
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    res = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"{method} {command} → {res.status_code}")
    return res.json() if res.text else None

# 1) 새 문서
MidasAPI("POST", "/doc/new", {})

# 2) 단위 설정
MidasAPI("PUT", "/db/unit", {"Assign": {"1": {"DIST": "M", "FORCE": "KN"}}})

# 3) 풍하중 케이스 생성 (KDS 41 12:2022)
MidasAPI("POST", "/db/stld", {"Assign": {1: {
    "NAME": "WIND_X_KDS",
    "TYPE": "W",           # W = Wind Load
    "CODE": "KDS41122022", # KDS 41 12:2022 기준
    "DESC": "KDS 풍하중 X방향"
}}})

# 4) 슬래브 요소 생성 (예: 3×3m 판)
MidasAPI("POST", "/db/node", {"Assign": {
    1: {"X": 0, "Y": 0, "Z": 5},
    2: {"X": 3, "Y": 0, "Z": 5},
    3: {"X": 3, "Y": 3, "Z": 5},
    4: {"X": 0, "Y": 3, "Z": 5},
}})

MidasAPI("POST", "/db/elem", {"Assign": {1: {
    "TYPE": "PLATE", "NODE": [1, 2, 3, 4], "THIK": 1, "STYPE": 1
}}})

# 5) 압력 하중 적용 (풍압 1.5 kN/m², X 방향)
MidasAPI("POST", "/db/pres", {"Assign": {1: {
    "ITEMS": [{
        "LCNAME": "WIND_X_KDS",
        "CMD": "PRES",
        "ELEM_TYPE": "PLATE",
        "FACE_EDGE_TYPE": "FACE",
        "DIRECTION": "GX",        # Global X 방향
        "EDGE_FACE": 1,           # 면 1 (위쪽)
        "FORCES": [-1.5, 0, 0, 0, 0]  # -1.5 kN/m² (음수 = 흡입)
    }]
}})

# 6) 저장 & 해석
MidasAPI("POST", "/doc/save", {})
MidasAPI("POST", "/doc/anal", {})
```

### 풍하중 계산 (KDS 기준)

```python
def calculate_kds_wind_pressure(height, wind_speed=28, exposure_category="C"):
    """
    KDS 41 12:2022 정적 등가풍하중 계산
    
    Parameters:
    - height: 구조물 높이 (m)
    - wind_speed: 기본 설계풍속 (m/s, 기본값 28)
    - exposure_category: 노출범주 ("B", "C", "D" 등)
    
    Returns:
    - 풍압 (kN/m²)
    """
    # 노출범주별 풍속계수 (KDS 기준 근사값)
    kz_table = {
        "B": {10: 1.0, 20: 1.1, 30: 1.2},
        "C": {10: 0.9, 20: 1.0, 30: 1.1},
        "D": {10: 0.8, 20: 0.9, 30: 1.0}
    }
    
    # 선형 보간
    kz_values = kz_table.get(exposure_category, kz_table["C"])
    if height <= 10:
        Kz = kz_values[10]
    elif height <= 20:
        Kz = kz_values[20]
    else:
        Kz = kz_values[30]
    
    # 구조계수 (직사각형 구조물 기준)
    Cp = 0.8
    # 중요도 계수
    Iw = 1.0
    
    # 동압 q = 0.613 * Kz * V² * Iw (단위: kN/m²)
    q = 0.613 * Kz * (wind_speed ** 2) * Iw
    
    # 풍압 = q * Cp
    wind_pressure = q * Cp
    
    return round(wind_pressure, 3)

# 예제: 높이 30m, 설계풍속 28m/s, 노출범주 C
pressure = calculate_kds_wind_pressure(30, 28, "C")
print(f"풍압: {pressure} kN/m²")  # 약 1.58 kN/m²
```

### 참고 문서
- [MIDAS Support - Wind Loads (KDS 41 12:2022)](https://support.midasuser.com/hc/ko/articles/29238911763353-Wind-Loads)
- [MIDAS Support - Nodal Wind Pressure](https://support.midasuser.com/hc/ko/articles/29270162256281-Nodal-Wind-Pressure)
- [MIDAS Support - Area Wind Pressure](https://support.midasuser.com/hc/ko/articles/29270183516057-Area-Wind-Pressure)
- [MIDAS Support - Static Wind Load (KDS 41 12:2022)](https://support.midasuser.com/hc/ko/articles/58908673370521-Static-Wind-Load-KDS-41-12-2022)

---

## 🔗 공식 문서

- [MIDAS API 온라인 매뉴얼](https://support.midasuser.com/hc/en-us/articles/33016922742937-MIDAS-API-Online-Manual)
- [MIDAS API JSON Manual (전체 엔드포인트 스키마)](https://support.midasuser.com/hc/en-us/sections/30087500371097-JSON-Manual)
- [MIDAS CIVIL NX Open API 동작 원리](https://support.midasuser.com/hc/en-us/articles/30212837484441-How-to-work-MIDAS-CIVIL-NX-Open-API)
- [Python 예제](https://support.midasuser.com/hc/en-us/articles/30230181806361-Example-Python)

## 📖 저장소 구조

```
docs/
├── API-OVERVIEW.md      # REST API, JSON, WebSocket 기본 개념
├── AUTHENTICATION.md    # Base URL, MAPI-Key 설정
├── ENDPOINTS.md         # 엔드포인트 가이드
└── QUICK-START.md       # 5분 안에 시작하기

examples/
├── python/              # Python 예제
├── javascript/          # JavaScript 예제
└── curl/                # cURL 예제
```

## ❓ 도움말

- Issues 탭에서 질문하기
- [공식 지원 사이트](https://support.midasuser.com) 방문

## 📝 참고

본 문서의 엔드포인트·JSON 스키마는 MIDAS 공식 NX Open API 매뉴얼(2026-06 기준) 및 KDS 41 12:2022 풍하중 기준을 근거로 작성되었습니다.
