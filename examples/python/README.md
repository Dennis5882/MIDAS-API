# Python 예제

## 사전 준비

1. **MIDAS Gen NX 실행** (API는 실행 중인 제품과 통신)
2. Open API 메뉴에서 **MAPI-Key** 발급

## 설치

```bash
pip install requests python-dotenv
```

## 환경 변수 설정

`.env` 파일을 만들고 다음을 입력하세요 (`.gitignore`에 `.env` 추가 권장):

```env
MIDAS_BASE_URL=https://moa-engineers.midasit.com:443/gen
MIDAS_MAPI_KEY=your-mapi-key-here
```

## 실행

```bash
python basic_example.py
```

성공하면 MIDAS Gen NX 화면에 사각 기둥 1개가 생성됩니다.

## 예제 파일

- `basic_example.py` — `MidasAPI()` 헬퍼 + 새문서→단위→재료→단면→노드→요소→지지→저장

## 핵심 패턴

```python
def MidasAPI(method, command, body=None):
    url = BASE_URL + command
    headers = {"MAPI-Key": MAPI_KEY, "Content-Type": "application/json"}
    return getattr(requests, method.lower())(url, headers=headers, json=body).json()

# 모든 /db/* 요청은 Assign 래퍼 사용
MidasAPI("POST", "/db/node", {"Assign": {1: {"X": 0, "Y": 0, "Z": 0}}})
```
