# 라이브 재검증 요청 (2026-09-27)

2026-09-18 검증 결과([live_verification_feedback_20260918.md](live_verification_feedback_20260918.md))를
Jira 코멘트에 인용하기 전에, **현재 설치된 빌드에서도 결과가 같은지** 확인하려는 요청입니다.
지난 검증은 Gen NX 2026 v2.1 / Civil NX 2026 v2.2, **Build 09/15/2026** 기준이었습니다.

범위는 코멘트에 실제로 들어가는 4개 항목뿐입니다. 절차와 페이로드는 지난 요청서
([live_verification_requests_20260918.md](live_verification_requests_20260918.md))와 같습니다.

## 먼저 확인할 것

**설치된 빌드가 09/15/2026에서 바뀌었는지 먼저 봐 주세요.** 바뀌지 않았다면 재실행할 필요 없이
"빌드 동일"로만 회신해 주셔도 됩니다. 9/18 결과를 그대로 인용하겠습니다.

## 재검증 항목

| 항목 | 엔드포인트 | 확인할 것 | 9/18 결과 |
| --- | --- | --- | --- |
| A-8 | `/db/SSEIS` | `IINHERENT_TORSION = true`, `NHERENT_TORSION = true`를 각각 보낸 뒤 GET의 `INHERENT_TORSION` 값 | 둘 다 HTTP 201이지만 무시됨, GET은 `false` |
| A-7 | `/ope/MEMB` | `ASSIGN_TYPE: "MANUAL"` + `SELETION_TYPE: "SELECTION"`으로 보낸 뒤 선택 요소가 반영되는지 | Gen·Civil 모두 반영됨 (별칭으로 동작) |
| B-2 (2D) | `/db/TDNA` | `PROFY[].RADIUS = false` | Gen·Civil 모두 `Wrong Field`, GET `Not Found Key` |
| B-2 (3D) | `/db/TDNA` | `PROF[].RADIUS = [0, 20]` | Gen·Civil 모두 `Wrong Field`, GET `Not Found Key` |

지난번과 마찬가지로 **HTTP 상태 코드만으로 판정하지 말고 GET 재조회까지** 해 주세요. 이 API는
오류 본문을 HTTP 201로 돌려주는 경우가 있습니다.

## 회신 형식

| 항목 | 제품 | 빌드 | 9/18과 같은가 | 달라졌다면 내용 |
| --- | --- | --- | --- | --- |
| A-8 | Gen | | | |
| A-7 | Gen / Civil | | | |
| B-2 (2D) | Gen / Civil | | | |
| B-2 (3D) | Gen / Civil | | | |

결과가 9/18과 다르면 그 항목은 Jira 코멘트에서 빼거나 문구를 고친 뒤 올리겠습니다.
