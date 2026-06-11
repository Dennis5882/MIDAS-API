# API 엔드포인트 가이드

MIDAS NX Open API의 엔드포인트 참고서입니다. 전체 키·필드 스키마는
[NX Open API JSON Manual](https://support.midasuser.com/hc/en-us/sections/30087500371097-JSON-Manual)을 참고하세요.

## 기본 정보

### Base URL
```
https://moa-engineers.midasit.com:443/gen      # MIDAS Gen NX
https://moa-engineers.midasit.com:443/civil    # MIDAS Civil NX
```

### 인증 헤더
```
MAPI-Key: [Gen NX 앱에서 발급받은 키]
Content-Type: application/json
```

### 공통 바디 형식
모든 `/db/*` 엔드포인트는 `Assign` 래퍼를 사용합니다.
```json
{ "Assign": { "<항목 ID>": { /* 필드 */ } } }
```

---

## 1. 문서 관리 (`/doc/*`)

| 엔드포인트 | 메서드 | 설명 | 바디 |
|-----------|--------|------|------|
| `/doc/new`   | POST | 새 문서 생성 | `{}` |
| `/doc/open`  | POST | 문서 열기 | 파일 경로 |
| `/doc/save`  | POST | 문서 저장 | - |
| `/doc/close` | POST | 문서 닫기 | - |

```python
MidasAPI("POST", "/doc/new", {})
MidasAPI("POST", "/doc/save")
```

---

## 2. 단위 (`/db/unit`)

| 키 | 설명 | 값 |
|----|------|-----|
| `DIST`  | 길이 단위 | `M` / `CM` / `MM` / `IN` / `FT` |
| `FORCE` | 힘 단위 | `KN` / `N` / `KGF` / `TONF` / `LBF` / `KIPS` |

```json
{ "Assign": { "1": { "DIST": "M", "FORCE": "TONF" } } }
```

---

## 3. 재료 (`/db/matl`)

RC(콘크리트) 예시:

```json
{ "Assign": { "1": {
  "TYPE": "CONC",
  "NAME": "C32",
  "PARAM": [ { "P_TYPE": 1, "STANDARD": "AS17(RC)", "DB": "C32" } ]
} } }
```

| 키 | 설명 |
|----|------|
| `TYPE`     | 재료 종류 (`CONC` 등) |
| `NAME`     | 재료 이름 |
| `PARAM`    | `[{ P_TYPE, STANDARD, DB }]` — 규격/DB로 강도 정의 |

---

## 4. 단면 (`/db/sect`) — DB/User 사각 단면 예시

```json
{ "Assign": { "1": {
  "SECTTYPE": "DBUSER",
  "SECT_NAME": "Rectangular",
  "SECT_BEFORE": {
    "USE_SHEAR_DEFORM": true,
    "SHAPE": "SB",
    "DATATYPE": 2,
    "SECT_I": { "vSIZE": [ 1.0, 0.8 ] }
  }
} } }
```

| 키 | 설명 |
|----|------|
| `SECTTYPE`  | `DBUSER` 등 |
| `SHAPE`     | 단면 형상 (`SB`=Solid Rectangle 등) |
| `SECT_I.vSIZE` | 치수 배열 `[H, B]` |

---

## 5. 두께 (`/db/thik`) — 판/벽

```json
{ "Assign": { "1": {
  "NAME": "SLAB150", "TYPE": "VALUE",
  "bINOUT": false, "T_IN": 0.15, "T_OUT": 0, "O_VALUE": 0
} } }
```

| 키 | 설명 |
|----|------|
| `TYPE`   | `VALUE` / `STIFFENED` |
| `bINOUT` | 면내/면외 두께 분리 여부 |
| `T_IN`   | 면내 두께 |
| `T_OUT`  | 면외 두께 (`bINOUT=true`일 때) |

---

## 6. 노드 (`/db/node`)

```json
{ "Assign": {
  "1": { "X": 0, "Y": 0, "Z": 0 },
  "2": { "X": 0, "Y": 0, "Z": 3.2 }
} }
```

---

## 7. 요소 (`/db/elem`)

| 키 | 설명 |
|----|------|
| `TYPE`  | 요소 타입 (아래 표) |
| `MATL`  | 재료 번호 |
| `SECT`  | 단면/두께 번호 |
| `NODE`  | 연결 노드 배열 (최대 8) |
| `ANGLE` | Beta 각 |
| `STYPE` | 요소 서브타입 (Plate/Wall 등) |

### 요소 타입 (`TYPE`)
| 구조부재 | 값 | 비고 |
|---------|-----|------|
| 기둥 · 보 (Frame) | `"BEAM"`   | `NODE=[i, j]` |
| 슬래브 | `"PLATE"`  | `NODE`=3/4점, `STYPE` 1=Thick·2=Thin·3/4=+Drilling DOF |
| 벽체 | `"WALL"`   | `NODE`=4점, `STYPE` 1=Membrane·2=Plate, `WALL`(ID), `W_TYPE` 0=Plate·1=CRB-Pin·2=CRB-Fixed |
| 트러스 | `"TRUSS"`  | |
| 인장전용/Hook/Cable | `"TENSTR"` | `STYPE`/`CABLE`로 구분 |
| 압축전용/Gap | `"COMPTR"` | |
| 평면응력/평면변형/축대칭 | `"PLSTRS"` / `"PLSTRN"` / `"AXISYM"` | |
| 솔리드 | `"SOLID"`  | `NODE`=4/6/8점 |

```json
{ "Assign": { "1": { "TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0 } } }
```

---

## 8. 정적 하중 케이스 (`/db/stld`)

```json
{ "Assign": { "1": { "NAME": "DL", "TYPE": "D", "DESC": "Dead Loads" } } }
```

### 주요 하중 타입 (`TYPE`)
| 값 | 의미 | 값 | 의미 |
|----|------|----|------|
| `USER` | 사용자 정의 | `D`  | 고정하중 |
| `L`    | 활하중 | `LR` | 지붕 활하중 |
| `S`    | 적설하중 | `R`  | 강우하중 |
| `W`    | 풍하중 | `E`  | 지진하중 |
| `EH` / `EV` | 수평/수직 토압 | `B` / `WP` | 부력 / 지하수압 |
| `T` / `TPG` | 온도 / 온도구배 | `PS` | 프리스트레스 |

> 전체 67종은 JSON Manual의 *Static Load Cases* 참고.

---

## 9. 하중 (Loads)

### 자중 (`/db/bodf`)
```json
{ "Assign": { "1": { "LCNAME": "D", "FV": [0, 0, -1] } } }
```

### 보 하중 (`/db/bmld`)
```json
{ "Assign": { "1": { "ITEMS": [ {
  "ID": 1, "LCNAME": "L", "CMD": "BEAM", "TYPE": "UNILOAD",
  "DIRECTION": "GZ", "D": [0, 1], "P": [-30, -30]
} ] } } }
```

### 바닥하중 — 타입 정의 (`/db/fbld`)
```json
{ "Assign": { "1": {
  "NAME": "Residential", "DESC": "",
  "ITEM": [
    { "LCNAME": "D", "FLOOR_LOAD": 1.5, "OPT_SUB_BEAM_WEIGHT": true },
    { "LCNAME": "L", "FLOOR_LOAD": 2.0, "OPT_SUB_BEAM_WEIGHT": true }
  ]
} } }
```

### 바닥하중 — 면 지정 (`/db/fbla`)
```json
{ "Assign": { "1": {
  "FLOOR_LOAD_TYPE_NAME": "Residential",
  "FLOOR_DIST_TYPE": 1,
  "DIR": "GZ",
  "NODES": [508, 509, 511, 510],
  "GROUP_NAME": "Floor3"
} } }
```
| `FLOOR_DIST_TYPE` | 1=One Way · 2=Two Way · 3=Polygon-Centroid · 4=Polygon-Length |
|---|---|

---

## 10. 경계조건 (`/db/cons`) — 지지

```json
{ "Assign": { "1": { "ITEMS": [ { "ID": 1, "CONSTRAINT": "1111000" } ] } } }
```
> `CONSTRAINT` 7자리 = `Dx Dy Dz Rx Ry Rz` (+축회전). `1`=구속, `0`=자유.
> 예: 고정단 `"1111000"`, 핀 `"1110000"`.

---

## 11. 하중조합 (`/db/lcom-gen`)

```json
{ "Assign": { "1": {
  "NAME": "Comb1", "ACTIVE": "ACTIVE", "iTYPE": 0,
  "vCOMB": [
    { "ANAL": "ST", "LCNAME": "DL", "FACTOR": 1.2 },
    { "ANAL": "ST", "LCNAME": "LL", "FACTOR": 1.6 }
  ]
} } }
```

---

## HTTP 상태 코드

| 코드 | 설명 |
|------|------|
| 200 | 요청 성공 |
| 400 | 잘못된 요청 (JSON/필드 오류) |
| 401 | 인증 실패 (MAPI-Key 확인) |
| 403 | 접근 거부 (권한/라이선스) |
| 404 | 경로 오류 |
| 500 | 서버 오류 |

---

## 참고 문서

- [NX Open API JSON Manual](https://support.midasuser.com/hc/en-us/sections/30087500371097-JSON-Manual)
- [MIDAS API 온라인 매뉴얼](https://support.midasuser.com/hc/en-us/articles/33016922742937-MIDAS-API-Online-Manual)
- [Python 예제](https://support.midasuser.com/hc/en-us/articles/30230181806361-Example-Python)
- [인증 설정](./AUTHENTICATION.md) · [API 개요](./API-OVERVIEW.md)
