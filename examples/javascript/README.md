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

1. `GET /mapikey/verify` → 로그인 이메일(`j.user`) 회수
2. 이메일 `@` 앞 부분으로 저장 경로 동적 구성
3. `POST /doc/saveas` → 저장 완료 후
4. `POST /doc/anal` → 해석 실행

주의 사항:
- `/doc/saveas` 를 `/doc/anal` **보다 먼저** 호출해야 합니다. 순서가 바뀌면 Gen NX가 저장 다이얼로그를 띄워 자동화가 중단됩니다.
- `%USERPROFILE%` 같은 환경변수는 MAPI 서버가 인식하지 못합니다. `/mapikey/verify`의 `j.user`로 경로를 직접 구성하세요.
- 모델 생성(`PUT /db/node` 등) **전에** `PUT /db/unit`으로 단위계를 설정하세요. Gen NX가 다른 단위로 열려 있으면 좌표가 잘못 해석되어 해석 경고가 발생합니다.

**EN** — Auto-save pattern before running structural analysis. Key flow:

1. `GET /mapikey/verify` → retrieve logged-in user email (`j.user`)
2. Extract username (before `@`) and build a dynamic save path
3. `POST /doc/saveas` → save the file first
4. `POST /doc/anal` → then run analysis

Important notes:
- Always call `/doc/saveas` **before** `/doc/anal`. Reversing the order causes Gen NX to show a save dialog, which blocks automation.
- Environment variables like `%USERPROFILE%` are **not** resolved by the MAPI server. Build the path from `j.user` returned by `/mapikey/verify`.
- Set the unit system via `PUT /db/unit` **before** creating model entities (`PUT /db/node`, etc.). If Gen NX is open in a different unit, coordinates will be misinterpreted and analysis warnings will occur.
