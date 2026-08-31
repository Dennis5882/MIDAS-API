# JavaScript 예제

## 사전 준비

1. **MIDAS Gen NX 실행**
2. Open API 메뉴에서 **MAPI-Key** 발급

## Node.js 설치

```bash
npm init -y
npm install axios
```

## 기본 예제

```javascript
const axios = require("axios");

const client = axios.create({
  baseURL: "https://moa-engineers.midasit.com:443/gen", // Civil NX: /civil
  headers: {
    "MAPI-Key": process.env.MIDAS_MAPI_KEY, // ⚠️ Authorization Bearer 아님
    "Content-Type": "application/json",
  },
});

async function main() {
  // 1) 새 문서
  await client.post("/doc/new", {});

  // 2) 단위
  await client.put("/db/unit", { Assign: { 1: { DIST: "M", FORCE: "TONF" } } });

  // 3) 노드 2개
  await client.post("/db/node", {
    Assign: { 1: { X: 0, Y: 0, Z: 0 }, 2: { X: 0, Y: 0, Z: 3.2 } },
  });

  // 4) 기둥 요소
  await client.post("/db/elem", {
    Assign: { 1: { TYPE: "BEAM", MATL: 1, SECT: 1, NODE: [1, 2], ANGLE: 0 } },
  });

  // 5) 저장
  await client.post("/doc/save");
  console.log("완료!");
}

main().catch((e) => console.error(e.response?.status, e.message));
```

## 브라우저에서 사용

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const BASE_URL = "https://moa-engineers.midasit.com:443/gen";
  const MAPI_KEY = "your-mapi-key-here";

  axios.get(`${BASE_URL}/db/node`, {
    headers: { "MAPI-Key": MAPI_KEY, "Content-Type": "application/json" },
  })
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));
</script>
```

> 참고: 모든 `/db/*` 요청은 `{ Assign: { "<ID>": { ... } } }` 형식을 사용합니다.

---

## 예제 파일 / Example Files

### [auto-save-before-analysis.html](./auto-save-before-analysis.html)

**KO** — 해석 실행 전 자동 저장 패턴. 핵심 흐름:

1. `GET /mapikey/verify` → 연결 상태 확인 (`j.user`는 표시용일 뿐, 저장 경로 구성엔 쓰지 않음)
2. 호출자가 지정한 저장 폴더(`saveDir`, 미지정 시 `C:/Temp` 폴백)로 파일 경로 구성
3. `POST /doc/saveas` → 저장 완료 후
4. `POST /doc/anal` → 해석 실행

주의 사항:
- `/doc/saveas` 를 `/doc/anal` **보다 먼저** 호출해야 합니다. 순서가 바뀌면 Gen NX가 저장 다이얼로그를 띄워 자동화가 중단됩니다.
- `%USERPROFILE%` 같은 환경변수는 MAPI 서버가 인식하지 못합니다.
- ⚠️ 로그인 이메일(`/mapikey/verify`의 `j.user`) 앞부분을 Windows 사용자명으로 가정해 `C:/Users/{이메일 앞부분}/...` 경로를 추정하지 마세요 — 로그인 이메일 계정과 PC의 실제 Windows 계정명은 다를 수 있습니다. 저장 폴더는 호출자가 실제 존재하는 경로를 직접 지정해야 합니다.
- `/doc/SAVEAS` 공식 문서엔 대상 폴더가 없을 때의 동작이 명시돼 있지 않지만, **실제 MAPI 호출로 확인**(2026-08-31): 폴더가 없으면 Gen NX가 "잘못된 경로가 있습니다" 에러 다이얼로그를 띄우고 MAPI 호출은 타임아웃되며, 폴더는 자동 생성되지 않습니다. 폴더를 미리 만들면 `200 OK`로 정상 저장됩니다(`C:/Temp`도 Windows 기본 폴더가 아니므로 직접 생성이 필요할 수 있습니다).
- 모델 생성(`PUT /db/node` 등) **전에** `PUT /db/unit`으로 단위계를 설정하세요. Gen NX가 다른 단위로 열려 있으면 좌표가 잘못 해석되어 해석 경고가 발생합니다.

**EN** — Auto-save pattern before running structural analysis. Key flow:

1. `GET /mapikey/verify` → confirm the connection (`j.user` is for display only, not used to build the save path)
2. Build the file path inside a caller-provided save folder (`saveDir`, falls back to `C:/Temp`)
3. `POST /doc/saveas` → save the file first
4. `POST /doc/anal` → then run analysis

Important notes:
- Always call `/doc/saveas` **before** `/doc/anal`. Reversing the order causes Gen NX to show a save dialog, which blocks automation.
- Environment variables like `%USERPROFILE%` are **not** resolved by the MAPI server.
- ⚠️ Don't guess a Windows folder from the local part of the login email (`j.user` from `/mapikey/verify`) — the login email account and the PC's actual Windows account name can differ. Always pass a real, existing folder as the save directory yourself.
- The official `/doc/SAVEAS` doc does not state what happens if the target folder doesn't exist, but this was **verified with a live MAPI call** (2026-08-31): if the folder is missing, Gen NX shows an "invalid path" error dialog and the MAPI call times out — the folder is not auto-created. Creating it beforehand results in a normal `200 OK` save (`C:/Temp` is not a default Windows folder either, so you may need to create it yourself).
- Set the unit system via `PUT /db/unit` **before** creating model entities (`PUT /db/node`, etc.). If Gen NX is open in a different unit, coordinates will be misinterpreted and analysis warnings will occur.
