# 라이브 검증 요청: 철근 배근 3종 REBB / REBC / REBW (2026-09-27)

`/db/REBB`(보), `/db/REBC`(기둥), `/db/REBW`(벽) 세 엔드포인트는 **공식 문서가 두 세대의 Key 체계로
갈려 있습니다.** 어느 쪽이 현재 제품의 실제 API인지는 문서만으로 가릴 수 없어서, 실제 제품에서
확인을 요청드립니다.

이 결과로 `docs/manual/24_DB_Design.md`를 어느 세대 기준으로 정리할지, 공식 담당자에게 어느
로케일을 고쳐 달라고 할지가 정해집니다.

## 문서 상황

| 엔드포인트 | 아티클 | ko 페이지 (2025 편집) | en-us 스키마 (2026-06-25) | en-us 예제 |
| --- | --- | --- | --- | --- |
| `/db/REBB` | `49513985245849` | 구 세대 | 신 세대 | **구 세대** |
| `/db/REBC` | `49513980544793` | 구 세대 | 신 세대 | 신 세대 |
| `/db/REBW` | `49514033006745` | 구 세대 | 신 세대 | 신 세대 |

세대별 대표 Key는 다음과 같습니다.

| 엔드포인트 | 구 세대 (ko) | 신 세대 (en-us) |
| --- | --- | --- |
| REBB | `ID`, `BAR_SECTOR_I`/`M`/`J`, `vMAIN_BAR_TOP`, `vMAIN_BAR_BOT`, `bSAME_SIZE_TOP_BOT` | `CREATE_SUB_SECTION`, `ELEMS`(`KEYS`/`TO`/`STRUCTURE_GROUP_NAME`) 외 |
| REBC | `ID`, `vMAIN_BAR`, `bUSE_CORNER`, `D0`, `HOOP_TYPE`, `bSAME_SPACE_END_CEN` | `CREATE_SUB_SECTION`, `MAIN_BAR`, `USE_CORNER`, `DO`, `HOOK_TYPE` |
| REBW | `ID`, `bUSE_MODEL_THICK`, `VER_BAR`, `HOR_BAR`, `NUM_END_BAR`, `BE_HOR_BAR`, `BE_LENGTH` | `CREATE_SUB_WALL_ID`, `VERTICAL_REBAR`, `HORIZONTAL_REBAR`, `END_REBAR`, `BE_HORIZONTAL_REBAR`, `BOUNDARY_ELEMENT_LENGTH`, `USE_MODEL_THICKNESS` |

REBB는 **영문 페이지 안에서도** 스키마(신)와 예제(구)가 세대가 다릅니다.

## 검증 방법

지난 요청들과 같은 원칙입니다. **HTTP 상태 코드만으로 판정하지 말고, 쓰기 후 GET으로 실제 저장된
값과 Key 이름까지 확인해 주세요.** 이 API는 오류 본문을 HTTP 201로 돌려주거나 모르는 필드를
조용히 무시하는 경우가 있습니다.

전제 조건(보·기둥·벽 요소, 단면, 재질, REBW는 층 정보)은 공식 예제가 가리키는 요소 번호에 맞춰
스크래치 모델에 만들어 주세요. 요소 번호만 스크래치 모델에 맞게 바꾸는 것은 괜찮습니다.

### 가장 결정적인 확인: GET 응답의 Key 이름

세대를 가리는 가장 확실한 방법은 **제품이 돌려주는 GET 응답이 어느 세대 Key로 되어 있는가**입니다.
가능하면 GUI에서 철근을 직접 입력한 뒤(또는 아래 (a)/(b) 중 성공한 쪽으로 만든 뒤) GET 응답의
최상위 구조와 Key 이름을 그대로 적어 주세요.

### 엔드포인트별 변형

각 엔드포인트마다:

- **(a) ko 페이지의 Request 예제를 그대로** POST
- **(b) en-us 페이지의 Request 예제를 그대로** POST
- 각각 직후 GET으로 반영 여부와 Key 이름 확인

REBB는 en-us 예제가 구 세대라 (a)와 사실상 같습니다. 그래서 REBB에 한해 하나를 더 부탁드립니다.

- **(c) REBB: en-us JSON Schema 기준 신 세대 페이로드** (`CREATE_SUB_SECTION`, `ELEMS` 사용)로
  POST 후 GET. 스키마만 있고 예제가 없어서, 스키마의 required 필드만 채운 최소 페이로드면 됩니다.

## 판정 기준

| 결과 | 의미 |
| --- | --- |
| (a)만 반영 | 현재 제품은 **구 세대**. en-us 신 스키마가 아직 제품에 없거나 다른 버전용 |
| (b)만 반영 | 현재 제품은 **신 세대**. ko 페이지가 낡은 것 |
| 둘 다 반영 | 두 체계를 모두 받음. GET 응답 Key 이름이 어느 쪽인지가 정본 판단 근거 |
| 둘 다 거부 | 예제 자체가 불완전. 오류 본문 내용이 필요합니다 |

## 회신 형식

| 엔드포인트 | 변형 | 제품 | 빌드 | HTTP | 응답 요약 | GET 결과 (Key 이름 포함) | 판정 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REBB | (a) ko 예제 | | | | | | |
| REBB | (b) en-us 예제 | | | | | | |
| REBB | (c) 신 스키마 최소 | | | | | | |
| REBC | (a) ko 예제 | | | | | | |
| REBC | (b) en-us 예제 | | | | | | |
| REBW | (a) ko 예제 | | | | | | |
| REBW | (b) en-us 예제 | | | | | | |

그리고 별도로 **GUI 입력 후 GET 응답의 Key 이름**(엔드포인트별 최상위 구조 한 덩어리)을
붙여 주세요.

Gen NX에서 먼저 확인하고, 가능하면 Civil NX에서도 같은지 봐 주시면 좋겠습니다. 두 제품이
다르게 동작하면 그 자체가 중요한 결과입니다.
