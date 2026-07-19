# 인증 설정 가이드

MIDAS NX Open API는 **`MAPI-Key`** 헤더로 인증합니다.

---

## 🔑 MAPI-Key 발급

`MAPI-Key`는 **MIDAS Gen NX(또는 Civil NX) 애플리케이션**에서 직접 발급합니다.

1. MIDAS Gen NX를 실행합니다.
2. Open API / Apps 메뉴에서 **API Key 발급**을 선택합니다.
3. 생성된 키(긴 문자열)를 복사합니다.

> `MAPI-Key`는 **임시 키**입니다. 서버는 이 키로 어떤 제품(실행 중인 Gen NX)에
> 연결할지 식별합니다. 언제든 재발급할 수 있으며, 무작위 추측이 거의 불가능한
> 긴 문자/숫자 조합입니다.

---

## 📍 Base URL

```
https://moa-engineers.midasit.com:443/gen      # MIDAS Gen NX
https://moa-engineers.midasit.com:443/civil    # MIDAS Civil NX
```

> 지역별 대체 서버가 제공됩니다. 사용 환경에 맞는 서버 주소를 확인하세요.

---

## 🔐 인증 헤더

모든 요청 헤더에 다음을 포함합니다.

```
MAPI-Key: YOUR_MAPI_KEY
Content-Type: application/json
```

> ⚠️ 인증에는 `Authorization: Bearer` 가 아니라 **`MAPI-Key`** 헤더를 사용합니다.

---

## 💻 언어별 설정

### Python

```python
import requests, os

BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

headers = {
    "MAPI-Key": MAPI_KEY,
    "Content-Type": "application/json",
}

res = requests.get(f"{BASE_URL}/db/node", headers=headers)
print(res.status_code, res.json())
```

### JavaScript (Node.js)

```javascript
const axios = require("axios");

const client = axios.create({
  baseURL: "https://moa-engineers.midasit.com:443/gen",
  headers: {
    "MAPI-Key": process.env.MIDAS_MAPI_KEY,
    "Content-Type": "application/json",
  },
});

client.get("/db/node").then(r => console.log(r.data));
```

### cURL

```bash
curl -X GET "https://moa-engineers.midasit.com:443/gen/db/node" \
  -H "MAPI-Key: $MIDAS_MAPI_KEY" \
  -H "Content-Type: application/json"
```

### Excel VBA

```vb
Sub GetNodes()
    Dim http As Object
    Set http = CreateObject("MSXML2.XMLHTTP")
    http.Open "GET", "https://moa-engineers.midasit.com:443/gen/db/node", False
    http.SetRequestHeader "MAPI-Key", "your-mapi-key-here"
    http.SetRequestHeader "Content-Type", "application/json"
    http.Send
    MsgBox http.responseText
End Sub
```

---

## 💡 실전 팁

### JSON 스키마를 못 찾았을 때 — GET → 수정 → PUT/POST

특정 데이터의 JSON 구조가 매뉴얼에서 바로 안 보일 때, 매뉴얼을 뒤지는 대신 제품에서 직접
뽑아내는 방법입니다.

1. MIDAS Gen/Civil NX GUI에서 원하는 데이터를 직접 입력합니다.
2. 해당 리소스를 `GET`으로 조회해 실제 JSON 형식을 확인합니다.
3. 응답의 최상위 키(예: `"NODE"`)를 **`"Assign"`으로 바꿔서** 그대로 `PUT`/`POST` 바디로 재사용합니다.
4. 반대로, 제품에서 데이터를 지운 뒤 `POST`로 원하는 값을 입력해보며 검증할 수도 있습니다.

```python
# 1) GUI에서 만든 데이터를 GET으로 확인
resp = requests.get(f"{BASE_URL}/db/node", headers=HEADERS).json()
# resp == {"NODE": {"1": {"X": 0, "Y": 0, "Z": 0}, ...}}

# 2) 최상위 키만 "Assign"으로 바꿔서 그대로 재사용
body = {"Assign": resp["NODE"]}
requests.put(f"{BASE_URL}/db/node", headers=HEADERS, json=body)
```

### `/info/db/...` — DB 리소스 스키마 인트로스펙션

`baseURL`과 `db` 사이에 `info`를 끼워 넣으면, 해당 DB 리소스의 Key 설명과 Value 타입을
서버가 직접 반환해줍니다. 매뉴얼에 없는 필드거나 최신 스펙을 즉석에서 확인하고 싶을 때
유용합니다.

```bash
curl -X GET "https://moa-engineers.midasit.com:443/civil/info/db/node" \
  -H "MAPI-Key: $MIDAS_MAPI_KEY"
```

> 일반 엔드포인트는 `{base url}/db/NODE`이고, 인트로스펙션 엔드포인트는
> `{base url}/info/db/NODE`처럼 `db` 앞에 `info`가 붙습니다.

---

## 🛡️ 보안 팁

### ✅ 해야 할 것
- `MAPI-Key`를 `.env` 파일에 저장하고 환경 변수로 사용
- `.env`를 `.gitignore`에 추가
- 노출 의심 시 앱에서 즉시 재발급

### ❌ 하지 말아야 할 것
- 키를 코드에 하드코딩
- 공개 저장소(GitHub 등)에 키 업로드

### .env 예시
```env
MIDAS_BASE_URL=https://moa-engineers.midasit.com:443/gen
MIDAS_MAPI_KEY=your-mapi-key-here
```

```python
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("MIDAS_BASE_URL")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY")
```

---

## ⚠️ 오류 해결

| 코드 | 원인 | 해결 |
|------|------|------|
| 401 Unauthorized | 키가 잘못됨/누락 | `MAPI-Key` 헤더 값 확인 |
| 403 Forbidden | 권한 부족 | 키 권한/제품 라이선스 확인 |
| 연결 실패/타임아웃 | **Gen NX 미실행** | MIDAS Gen NX 실행 여부 확인 |
| Base URL 오류(404) | 잘못된 서버/경로 | `/gen` 또는 `/civil` 경로 확인 |

> 가장 흔한 실수: **MIDAS Gen NX가 실행되어 있지 않은 경우**. 서버는 실행 중인
> 제품과 WebSocket으로 연결되어야 동작합니다.

### 연결 전 상태 확인 — `/mapikey/verify`

여러 요청을 연달아 보내기 전에, 제품이 서버에 정상 연결되어 있는지 먼저 확인할 수 있습니다.
Base URL에서 제품 경로(`/gen`, `/civil`)를 뺀 주소에 `/mapikey/verify`를 붙여 `GET`으로 호출합니다.

```bash
curl -X GET "https://moa-engineers.midasit.com:443/mapikey/verify" \
  -H "MAPI-Key: $MIDAS_MAPI_KEY"
```

```json
{
    "user": "User_ID",
    "program": "civil",
    "connectionID": "Connection_ID",
    "keyVerified": true,
    "status": "connected"
}
```

| 키 | 의미 |
| --- | --- |
| `status` | 제품-서버 연결 상태 |
| `keyVerified` | MAPI-Key 유효 여부 |
| `user` | 제품에 로그인된 사용자 ID |
| `program` | 연결된 제품 (`gen` / `civil`) |
| `connectionID` | 클라이언트를 식별하는 휘발성 ID |

### 사내망/방화벽 환경 연결 문제

"Connect" 버튼을 눌러도 상태가 바뀌지 않는다면, 대부분 사내 방화벽이 외부로 나가는
`http(s)`/`WebSocket` 요청을 막고 있는 경우입니다. 네트워크/보안팀에 아래 정보로 허용을
요청하세요.

| 항목 | 값 |
| --- | --- |
| Protocol | `https`, `wss` |
| Port | `443` |
| IP | `121.157.60.1/32` (MIDAS Public NAT IP) |
| URI | `https://moa-engineers.midasit.com` |

> **SSL 인터셉션(SSL Inspection) 환경 주의:** 사내 프록시가 모든 트래픽에 SSL 인터셉션을
> 적용하는 경우, `moa-engineers.midasit.com`을 인터셉션 대상에서 제외해야 연결이 됩니다.
> 여러 기업 고객이 이 설정으로 문제를 해결한 사례가 있습니다 — 방화벽/프록시 자체는
> 정상이어도 SSL 인터셉션 때문에 연결이 거부될 수 있다는 점을 network/보안팀에 함께
> 전달하세요.

---

## 📝 다음 단계

1. [README 빠른 시작](../README.md#-빠른-시작-python) - 첫 모델 생성
2. [MIDAS API JSON Manual 목차](./manual/INDEX.md) - 전체 엔드포인트·JSON 스키마
