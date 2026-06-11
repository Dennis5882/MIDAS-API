# 5분 안에 시작하기

이 가이드를 따라 5분 안에 첫 모델을 MIDAS Gen NX에 생성해 보세요! 🚀

---

## ⚙️ 사전 준비 (1분)

### 필요한 것

1. **MIDAS Gen NX 실행** ⚠️ — API는 실행 중인 제품과 통신합니다.
2. **Base URL**
   ```
   https://moa-engineers.midasit.com:443/gen
   ```
3. **MAPI-Key** — Gen NX 앱의 Open API 메뉴에서 발급
   ```
   eyJhbGciOi...
   ```

---

## 🐍 Python으로 시작 (3분)

### 1단계: 라이브러리 설치

```bash
pip install requests
```

### 2단계: 코드 작성

`quickstart.py` 파일을 만들고 다음을 입력하세요:

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "your-mapi-key-here"   # Gen NX 앱에서 발급

def MidasAPI(method, command, body=None):
    url = BASE_URL + command
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    res = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(method, command, "->", res.status_code)
    return res.json()

# 1) 새 문서
MidasAPI("POST", "/doc/new", {})

# 2) 단위 (대만 RC: m, tonf)
MidasAPI("PUT", "/db/unit", {"Assign": {"1": {"DIST": "M", "FORCE": "TONF"}}})

# 3) 재료 (RC C32)
MidasAPI("POST", "/db/matl", {"Assign": {1: {
    "TYPE": "CONC", "NAME": "C32",
    "PARAM": [{"P_TYPE": 1, "STANDARD": "AS17(RC)", "DB": "C32"}]
}}})

# 4) 단면 (600x600 사각 기둥)
MidasAPI("POST", "/db/sect", {"Assign": {1: {
    "SECTTYPE": "DBUSER", "SECT_NAME": "C600",
    "SECT_BEFORE": {"SHAPE": "SB", "DATATYPE": 2, "SECT_I": {"vSIZE": [0.6, 0.6]}}
}}})

# 5) 노드 2개 (3.2m 기둥)
MidasAPI("POST", "/db/node", {"Assign": {
    1: {"X": 0, "Y": 0, "Z": 0},
    2: {"X": 0, "Y": 0, "Z": 3.2},
}})

# 6) 기둥 요소
MidasAPI("POST", "/db/elem", {"Assign": {1: {
    "TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0
}}})

# 7) 하단 고정 지지
MidasAPI("POST", "/db/cons", {"Assign": {1: {
    "ITEMS": [{"ID": 1, "CONSTRAINT": "1111111"}]
}}})

# 8) 저장
MidasAPI("POST", "/doc/save")
print("완료! Gen NX 화면을 확인하세요.")
```

### 3단계: 실행

```bash
python quickstart.py
```

**성공 시 출력:**

```
POST /doc/new -> 200
PUT /db/unit -> 200
POST /db/matl -> 200
POST /db/sect -> 200
POST /db/node -> 200
POST /db/elem -> 200
POST /db/cons -> 200
POST /doc/save -> 200
완료! Gen NX 화면을 확인하세요.
```

→ MIDAS Gen NX 화면에 기둥 1개가 생성됩니다.

---

## 🌐 cURL로 확인 (1분)

노드를 조회해 봅니다.

```bash
curl -X GET "https://moa-engineers.midasit.com:443/gen/db/node" \
  -H "MAPI-Key: your-mapi-key-here" \
  -H "Content-Type: application/json"
```

---

## 🎯 다음 단계

| 문서 | 설명 |
|------|------|
| [엔드포인트 가이드](./ENDPOINTS.md) | 모든 엔드포인트와 JSON 스키마 |
| [인증 설정](./AUTHENTICATION.md) | MAPI-Key 안전하게 관리하기 |
| [예제 코드](../examples/) | 더 많은 실제 예제 |

---

## ⚠️ 자주 묻는 질문

### Q: 연결이 안 돼요 / 타임아웃
**A:** **MIDAS Gen NX가 실행 중인지** 확인하세요. API는 실행 중인 제품과 WebSocket으로 통신합니다.

### Q: 401 Unauthorized
**A:** `MAPI-Key` 값이 정확한지 확인하세요. (헤더 이름은 `Authorization`이 아니라 `MAPI-Key`)

### Q: 404 Not Found
**A:** Base URL 경로(`/gen` 또는 `/civil`)와 엔드포인트 철자를 확인하세요.

### Q: 200인데 모델이 안 보여요
**A:** 화면 갱신(Fit View) 후 확인하거나, `/doc/save` 호출 여부를 확인하세요.

---

## 💡 팁

- 🔒 `MAPI-Key`는 `.env`에 저장하세요.
- 🧪 `requests` 응답 `status_code`를 매 호출마다 로깅하면 디버깅이 쉽습니다.
- 📚 [NX Open API JSON Manual](https://support.midasuser.com/hc/en-us/sections/30087500371097-JSON-Manual)에서 각 엔드포인트의 정확한 필드를 확인하세요.
