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
