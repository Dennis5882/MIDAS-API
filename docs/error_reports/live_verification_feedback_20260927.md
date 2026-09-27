# 라이브 재검증 피드백 (2026-09-27)

[live_verification_requests_20260927.md](live_verification_requests_20260927.md)에 대한 회신이다.

**빌드가 바뀌었으므로 재실행했다.** 9/18 검증은 Gen NX 2026 v2.1 / Civil NX 2026 v2.2,
Build 09/15/2026이었고, 현재 설치본은 **Gen NX 2026 v2.2 / Civil NX 2026 v2.2, 둘 다
Build 09/24/2026**이다(두 제품의 About 창, 작성자 확인). Gen은 v2.1에서 v2.2로 올라갔다.

절차와 페이로드는 9/18과 같다. 같은 하네스(`MIDAS-API-NX-SDK/scripts/live_manual_feedback.py`의
`b1`·`a1`·`a3`)를 그대로 돌렸고, 각 변형은 저장 후 빈 스크래치 문서에서 수행했다. HTTP 상태만
보지 않고 응답 본문과 후속 GET을 함께 판정했다.

## 회신

| 항목 | 제품 | 빌드 | 9/18과 같은가 | 달라졌다면 내용 |
| --- | --- | --- | --- | --- |
| A-8 | Gen | 09/24/2026 | **같음** | - |
| A-7 | Gen / Civil | 09/24/2026 | **같음** (두 제품 모두) | - |
| B-2 (2D) | Gen / Civil | 09/24/2026 | **같음** (두 제품 모두) | - |
| B-2 (3D) | Gen / Civil | 09/24/2026 | **같음** (두 제품 모두) | - |

**네 항목 모두 9/18 결과를 그대로 인용해도 된다.**

## 상세

| 항목 | 제품 | 보낸 것 | HTTP | 응답 요약 | GET 재조회 | 판정 |
| --- | --- | --- | --- | --- | --- | --- |
| A-8 (대조) | Gen | `INHERENT_TORSION = true` | 201 | 정상 | `INHERENT_TORSION = true` | 수용·반영됨 |
| A-8 | Gen | `IINHERENT_TORSION = true` | 201 | 오타 키가 응답에서 사라짐 | `INHERENT_TORSION = false` | 수용되나 무시됨 |
| A-8 | Gen | `NHERENT_TORSION = true` | 201 | 오타 키가 응답에서 사라짐 | `INHERENT_TORSION = false` | 수용되나 무시됨 |
| A-7 (대조) | Gen, Civil | `SELECTION_TYPE: "SELECTION"` | 200 | `MEMB.1.AELEM = [2,3]` | `AELEM = [2,3]` | 수용·반영됨 |
| A-7 | Gen, Civil | `SELETION_TYPE: "SELECTION"` | 200 | `MEMB.1.AELEM = [2,3]` | `AELEM = [2,3]` | 수용·반영됨 (별칭) |
| B-2 2D (대조) | Gen, Civil | 공식 예제 그대로, `RADIUS` 숫자 | 201 | 생성 | `PROFY`·`PROFZ`의 `RADIUS = [0,20,0]` 숫자로 보존 | 수용·반영됨 |
| B-2 2D | Gen, Civil | `PROFY[1].RADIUS = false` | 201 + 오류 본문 | `Wrong Field` | `Not Found Key` | 거부 |
| B-2 3D (대조) | Gen, Civil | 공식 예제 그대로, `RADIUS` 숫자 | 201 | 생성 | `PROF`의 `RADIUS = [0,20,0]` 숫자로 보존 | 수용·반영됨 |
| B-2 3D | Gen, Civil | `PROF[1].RADIUS = [0, 20]` | 201 + 오류 본문 | `Wrong Field` | `Not Found Key` | 거부 |

A-7의 요소 번호는 9/18과 같이 공식 예제의 `640, 692`를 스크래치 모델의 실제 beam `2, 3`으로만
치환했다. B-2의 기준 모델도 9/18과 같이 공식 예제와 같은 30 m 연속 beam 30개, Tendon Group,
공식 Tendon Property를 매 변형마다 새로 만들었다.

B-2의 거부는 타입 때문이라는 결론도 그대로다. 같은 구간에 숫자를 보낸 대조군은 두 제품 모두
생성되고 GET에도 숫자로 남았고, `false`와 `[0, 20]`만 거부됐다. 오류 본문이 **HTTP 201**로
오므로 상태 코드만 보면 성공으로 오판한다는 점도 9/18과 같다.

## 요청 범위 밖이지만 적어 둘 것

- A-7: POST 응답은 `bREVERSE: false`인데 후속 GET은 `bREVERSE: true`다. 정상 키와 오타 키에서
  **똑같이** 나타나므로 A-7의 판정(별칭)에는 영향이 없다. 9/18 회신은 `AELEM`만 기록해서 이
  값이 그때도 같았는지는 이 기록으로 확인할 수 없다.
- 같은 날 같은 빌드에서 SDK 쪽 전체 재검증도 돌았다. 확정된 라이브 케이스 302개(엔드포인트·제품
  쌍) 전부가 두 SDK에서 통과해 회귀가 없었고, 원래 실패하던 미확정 케이스 34개 중 새로 통과한
  것도 없었다. 기록은 `MIDAS-API-NX-SDK/docs/live_verification_notes.md`의 2026-09-27 항목.
