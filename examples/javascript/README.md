# JavaScript 예제

## Node.js 설치

```bash
npm init -y
npm install axios
```

## 기본 예제

```javascript
const axios = require('axios');

const API_KEY = 'your-api-key-here';
const BASE_URL = 'https://your-midas-server.com/api/v1';

const client = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Authorization': `Bearer ${API_KEY}`,
    'Content-Type': 'application/json'
  }
});

// 프로젝트 정보 조회
client.get('/db/PJCF')
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
```

## 브라우저에서 사용

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const API_KEY = 'your-api-key-here';
  const BASE_URL = 'https://your-midas-server.com/api/v1';

  axios.get(`${BASE_URL}/db/PJCF`, {
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json'
    }
  })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
</script>
```
