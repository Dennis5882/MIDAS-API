# cURL 예제

## 기본 사용법

```bash
#!/bin/bash

API_KEY="your-api-key-here"
BASE_URL="https://your-midas-server.com/api/v1"

curl -X GET "${BASE_URL}/db/PJCF" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json"
```

## 예제

### 1. 프로젝트 정보 조회

```bash
curl -X GET https://your-midas-server.com/api/v1/db/PJCF \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### 2. 새 프로젝트 생성

```bash
curl -X POST https://your-midas-server.com/api/v1/doc/NEW \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "project_name": "My Project",
    "unit": "m"
  }'
```

### 3. 단위 정보 조회

```bash
curl -X GET https://your-midas-server.com/api/v1/db/UNIT \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### 4. 재료 목록 조회

```bash
curl -X GET https://your-midas-server.com/api/v1/db/MATL \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### 5. 노드 목록 조회

```bash
curl -X GET https://your-midas-server.com/api/v1/db/NODE \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### 6. 요소 목록 조회

```bash
curl -X GET https://your-midas-server.com/api/v1/db/ELEM \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```
