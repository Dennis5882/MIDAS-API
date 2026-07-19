# 기타 언어 예제 (C# · Java · Dart · C · Node.js)

REST API는 플랫폼에 종속되지 않으므로, 여기 소개된 언어 외에도 HTTP 클라이언트가 있는
어떤 언어로도 MIDAS NX Open API를 호출할 수 있습니다. 아래는 `POST /db/node`로 절점 1개를
생성하는 동일한 요청을 여러 언어로 옮긴 스니펫입니다 (전용 폴더가 없는 언어들만 모았습니다 —
Python은 [`python/`](./python/), JavaScript(Node.js/axios)는 [`javascript/`](./javascript/),
cURL은 [`curl/`](./curl/), Excel VBA는 [`vba/`](./vba/) 참고).

출처: [MIDAS Support "Example: Various Programming Languages"](https://support.midasuser.com/hc/en-us/articles/30506872725017-Example-Various-Programming-Languages)
(원문 스니펫을 그대로 옮기되, Node.js/Axios 예제의 화살표 함수 오탈자(`= {` → `=> {`)와
누락된 baseURL 조합만 바로잡았습니다.)

공통 요청:

```json
POST {baseURL}/db/node
{
  "Assign": {
    "1": { "X": 1, "Y": 2, "Z": 3 }
  }
}
```

## C# — HttpClient

```csharp
var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Post, "https://moa-engineers.midasit.com:443/civil/db/node");
request.Headers.Add("MAPI-Key", "your_api_key_here");
var content = new StringContent(
    "{\"Assign\":{\"1\":{\"X\":1,\"Y\":2,\"Z\":3}}}",
    null, "application/json");
request.Content = content;
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
```

## JavaScript — Fetch (브라우저)

```javascript
const myHeaders = new Headers();
myHeaders.append("MAPI-Key", "your_api_key_here");
myHeaders.append("Content-Type", "application/json");

const raw = JSON.stringify({
  Assign: { "1": { X: 1, Y: 2, Z: 3 } },
});

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow",
};

fetch("https://moa-engineers.midasit.com:443/civil/db/node", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.log("error", error));
```

## Java — OkHttp

```java
OkHttpClient client = new OkHttpClient().newBuilder().build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"Assign\":{\"1\":{\"X\":1,\"Y\":2,\"Z\":3}}}");
Request request = new Request.Builder()
    .url("https://moa-engineers.midasit.com:443/civil/db/node")
    .method("POST", body)
    .addHeader("MAPI-Key", "your_api_key_here")
    .addHeader("Content-Type", "application/json")
    .build();
Response response = client.newCall(request).execute();
```

## Dart — Dio

```dart
import 'dart:convert';
import 'package:dio/dio.dart';

var headers = {
  'MAPI-Key': 'your_api_key_here',
  'Content-Type': 'application/json',
};
var data = json.encode({
  "Assign": {
    "1": {"X": 1, "Y": 2, "Z": 3}
  }
});
var dio = Dio();
var response = await dio.request(
  'https://moa-engineers.midasit.com:443/civil/db/node',
  options: Options(method: 'POST', headers: headers),
  data: data,
);

if (response.statusCode == 200) {
  print(json.encode(response.data));
} else {
  print(response.statusMessage);
}
```

## C — libcurl

```c
#include <curl/curl.h>

CURL *curl;
CURLcode res;
curl = curl_easy_init();
if (curl) {
    curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "POST");
    curl_easy_setopt(curl, CURLOPT_URL, "https://moa-engineers.midasit.com:443/civil/db/node");
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, "MAPI-Key: your_api_key_here");
    headers = curl_slist_append(headers, "Content-Type: application/json");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    const char *data = "{\"Assign\":{\"1\":{\"X\":1,\"Y\":2,\"Z\":3}}}";
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
    res = curl_easy_perform(curl);
    curl_slist_free_all(headers);
}
curl_easy_cleanup(curl);
```

## Node.js — Axios

> 원문 예제는 `url: '/db/node'`만 있고 `baseURL`이 없었고, `.then((response) = {`처럼
> 화살표 함수 오탈자(`=`가 `=>`여야 함)가 있어 그대로면 문법 오류가 납니다. 아래는 두 가지를
> 바로잡은 버전입니다. Node.js에서 axios를 더 본격적으로 쓰는 예제는 [`javascript/README.md`](./javascript/README.md)를 참고하세요.

```javascript
const axios = require("axios");

const data = JSON.stringify({
  Assign: { "1": { X: 1, Y: 2, Z: 3 } },
});

const config = {
  method: "post",
  maxBodyLength: Infinity,
  baseURL: "https://moa-engineers.midasit.com:443/civil",
  url: "/db/node",
  headers: {
    "MAPI-Key": "your_api_key_here",
    "Content-Type": "application/json",
  },
  data,
};

axios
  .request(config)
  .then((response) => {
    console.log(JSON.stringify(response.data));
  })
  .catch((error) => {
    console.log(error);
  });
```
