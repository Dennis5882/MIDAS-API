# 라이브 검증 피드백 (2026-09-18)

검증 제품은 MIDAS Gen NX 2026 v2.1과 MIDAS Civil NX 2026 v2.2이며, 두
제품 모두 같은 시점(2026-09-18)의 설치본이다. 모든 검증은 자동 저장 후 빈 스크래치
문서에서 수행했다. HTTP 상태만 보지 않고 응답 본문과 후속 GET을 함께
판정했다.

## 결과 요약

| 항목 | 제품 | 변형한 필드 | HTTP 상태 | 응답 요약 | GET 재조회 결과 | 판정 |
| --- | --- | --- | --- | --- | --- | --- |
| A-1 (b) | Gen | `SELETION_TYPE` | 200 | `MEMB.1.AELEM = [2,3]` | `/db/MEMB/1.AELEM = [2,3]` | 수용·반영됨 |
| A-1 (b) | Civil | `SELETION_TYPE` | 200 | `MEMB.1.AELEM = [2,3]` | `/db/MEMB/1.AELEM = [2,3]` | 수용·반영됨 |
| A-2 (b) | Gen | `SEIS_CODE = "KDS(41-17-00: 2019)"` | 201 | 공백 없는 코드로 응답 | `KDS(41-17-00:2019)` | 수용·정규화됨 |
| A-3 (b) | Gen | `PROFY[1].RADIUS = false` | 201 + 오류 본문 | `Wrong Field` | `Not Found Key` | 거부 |
| A-3 (b) | Civil | `PROFY[1].RADIUS = false` | 201 + 오류 본문 | `Wrong Field` | `Not Found Key` | 거부 |
| A-3 (c) | Gen | `PROF[1].RADIUS = [0,20]` | 201 + 오류 본문 | `Wrong Field` | `Not Found Key` | 거부 |
| A-3 (c) | Civil | `PROF[1].RADIUS = [0,20]` | 201 + 오류 본문 | `Wrong Field` | `Not Found Key` | 거부 |
| B-1 | Gen | `IINHERENT_TORSION = true` | 201 | 오타 키가 응답에서 사라짐 | `INHERENT_TORSION = false` | 수용되나 무시됨 |
| B-1 | Gen | `NHERENT_TORSION = true` | 201 | 오타 키가 응답에서 사라짐 | `INHERENT_TORSION = false` | 수용되나 무시됨 |
| B-2 MATD | Gen | `bSERVCHECK = true` | 200 | 요청값 응답 | `true` | 수용·반영됨 |
| B-2 MATD | Gen | `dSHORTTERM = 1.25` | 200 | 요청값 응답 | `1.25` | 수용·반영됨 |
| B-2 MATD | Gen | `dLONGTERM = 1.5` | 200 | 요청값 응답 | `1.5` | 수용·반영됨 |
| B-2 MATD | Civil | `bSERVCHECK = true` | 200 | 요청값 응답 | 필드 없음 | 수용되나 무시됨 |
| B-2 MATD | Civil | `dSHORTTERM = 1.25` | 200 | 요청값 응답 | 필드 없음 | 수용되나 무시됨 |
| B-2 MATD | Civil | `dLONGTERM = 1.5` | 200 | 요청값 응답 | 필드 없음 | 수용되나 무시됨 |
| B-2 SPLC POST | Gen | `aACCECC_ECCEN_LIST[0].ALONG = 2.5` | 201 | 요청값 응답 | `2.5` | 수용·반영됨 |
| B-2 SPLC PUT | Gen | `ALONG: 2.5 -> 3.5` | 200 | `3.5`로 응답 | 기존값 `2.5` 유지 | 수용되나 무시됨 |

## A-1 결론

`SELECTION_TYPE`과 표의 오타 `SELETION_TYPE`은 현재 두 제품에서 모두
동일하게 동작하는 별칭이다. 따라서 표의 철자는 정정하는 것이 맞지만,
오타를 복사한 호출이 조용히 무시되어 선택이 사라지는 유형은 아니다.
공식 예제의 모델 전용 요소 번호 `640, 692`만 스크래치 모델의 실제 beam
요소 `2, 3`으로 치환했다.

## A-2 결론

콜론 뒤 공백이 있는 KDS 코드도 Gen이 수용하며, POST 응답과 GET 저장값을
공백 없는 표준 문자열로 정규화한다. 한글 예제를 복사해도 현재 제품에서
실패하지 않으므로 표기 통일 요청 수준이다.

## A-3 결론

공식 온라인 아티클의 2D Round/Element와 3D Round/Element 예제를 그대로
기준으로 사용했다. 예제와 같은 30 m 연속 beam 30개, Tendon Group, 공식
Magura Tendon Property를 각 스크래치 문서에 만들었다.

- 2D 기준의 `PROFY`와 `PROFZ` 숫자 `RADIUS` 값 `0, 20, 0`은 두 제품에서
  생성되고 GET에도 숫자로 보존됐다.
- 3D 기준의 `PROF` 숫자 `RADIUS` 값 `0, 20, 0`도 두 제품에서 생성되고
  GET에도 숫자로 보존됐다.
- `PROFY.RADIUS = false`와 `PROF.RADIUS = [0,20]`은 두 제품 모두
  `Wrong Field`로 거부됐다. 이 API는 오류 본문을 HTTP 201로 돌려주므로
  상태 코드만 보면 성공으로 오판한다.

따라서 두 문제 행의 실제 wire type은 모두 `Number`이며, 2D `Boolean` 및
3D `Array` 표기는 오류다.

## B-1 결론

정상 `INHERENT_TORSION = true`는 GET에도 `true`로 저장됐다. 반면
`IINHERENT_TORSION`과 `NHERENT_TORSION`은 HTTP 201이지만 오타 키가
응답에서 사라지고, GET의 정상 필드는 기본값 `false`였다. 두 오타 모두
서버가 조용히 무시하므로 예제를 복사한 사용자는 옵션이 적용됐다고
오해할 수 있다.

## B-2 결론

### `/db/MATD`

Gen에서는 `bSERVCHECK`, `dSHORTTERM`, `dLONGTERM`을 각각 하나씩 추가한
PUT과 세 필드를 함께 보낸 PUT이 모두 GET에 보존됐다. 따라서 세 필드는
Gen에서 실제 동작하며 Specifications 표 누락을 보완할 근거가 된다.

Civil에서는 같은 PUT이 HTTP 200이고 즉시 응답에도 입력값이 나타나지만,
후속 GET에는 세 필드가 모두 존재하지 않는다. 기준 PUT의 다른 재료 값은
정상 저장되므로 요청 전체가 실패한 것은 아니다. 현재 Build에서 이 세
필드는 Civil에 전송할 수는 있으나 지속되지 않는 Gen 전용 동작으로 보인다.

### `/db/SPLC`

공식 기본 응답스펙트럼 예제에 Gen NX 전용 우발편심 블록을 붙였다. 실제
Story와 Response Spectrum Function을 먼저 생성했다. `ALONG = 2.5`를 담은
POST는 후속 GET에 그대로 저장됐다. 같은 레코드에 `ALONG = 3.5`를 보낸
PUT은 응답에는 3.5를 돌려줬지만 후속 GET에는 기존 2.5가 남았다.

따라서 `ALONG`은 Gen의 생성 경로에서는 실제 wire field지만, 현재 Build의
갱신 경로는 변경을 조용히 무시한다. PUT 응답만 확인하면 반영됐다고
오판할 수 있으므로 문서 오류 제보와 별도로 제품 동작 확인이 필요하다.
