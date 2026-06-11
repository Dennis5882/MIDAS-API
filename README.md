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

본 문서의 엔드포인트·JSON 스키마는 MIDAS 공식 NX Open API 매뉴얼(2026-06 기준)을 근거로 작성되었습니다.
