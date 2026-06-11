# cURL 예제

## 사전 준비

1. **MIDAS Gen NX 실행**
2. Open API 메뉴에서 **MAPI-Key** 발급

## 기본 사용법

```bash
#!/bin/bash

BASE_URL="https://moa-engineers.midasit.com:443/gen"   # Civil NX: /civil
MAPI_KEY="your-mapi-key-here"

curl -X GET "${BASE_URL}/db/node" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json"
```

> ⚠️ 인증 헤더는 `Authorization: Bearer`가 아니라 **`MAPI-Key`** 입니다.
> 모든 `/db/*` 요청은 `{"Assign": {...}}` 형식을 사용합니다.

## 예제

### 1. 새 문서 생성

```bash
curl -X POST "${BASE_URL}/doc/new" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### 2. 단위 설정

```bash
curl -X PUT "${BASE_URL}/db/unit" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json" \
  -d '{ "Assign": { "1": { "DIST": "M", "FORCE": "TONF" } } }'
```

### 3. 노드 생성

```bash
curl -X POST "${BASE_URL}/db/node" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json" \
  -d '{ "Assign": { "1": { "X": 0, "Y": 0, "Z": 0 }, "2": { "X": 0, "Y": 0, "Z": 3.2 } } }'
```

### 4. 요소(기둥) 생성

```bash
curl -X POST "${BASE_URL}/db/elem" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json" \
  -d '{ "Assign": { "1": { "TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0 } } }'
```

### 5. 노드 조회

```bash
curl -X GET "${BASE_URL}/db/node" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json"
```

### 6. 문서 저장

```bash
curl -X POST "${BASE_URL}/doc/save" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json"
```
