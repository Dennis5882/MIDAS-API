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

---

## 📝 다음 단계

1. [5분 시작 가이드](./QUICK-START.md) - 첫 모델 생성
2. [엔드포인트 가이드](./ENDPOINTS.md) - 전체 엔드포인트
