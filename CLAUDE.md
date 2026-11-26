# CLAUDE.md

이 저장소에서 작업할 때 지켜야 할 규칙과 맥락입니다.

## 이 저장소는 무엇인가

**MIDAS NX Open API**(MIDAS Gen NX / Civil NX)에 대한 사람이 직접 큐레이션한 **JSON 스키마 매뉴얼**
저장소입니다. 코드 라이브러리가 아니라 문서 저장소입니다.

- `docs/manual/01_DOC.md` ~ `27_Design_SRC_AIKSRC2K.md` + `16_2_VIEW_ResultGraphic.md` — 28개 파일.
  공식 목차의 276개 경로와 설계코드 엔드포인트를
  MIDAS 공식 Zendesk 온라인 매뉴얼 기준으로 문서화. `docs/manual/INDEX.md`가 전체 목차/개수 색인.
- `docs/plugin/` — MIDAS Plug-in(MIDAS API + Python으로 만든, GUI에 내장된 완성형 자동화 도구)
  문서. `docs/manual/`과 별개 폴더인 이유와 문서 성격 차이는 `docs/plugin/INDEX.md` 상단 참고.
  `INDEX.md`가 카탈로그이자 진행 상태(작성/미작성) 트래커 — 개별 툴 문서는 점진적으로 채워나가는
  중이니 상태를 먼저 확인할 것.
- `docs/AUTHENTICATION.md` — 인증, GET/PUT 워크플로, 방화벽 가이드 등 Quick Tips.
- `examples/` — Python/VBA/JavaScript/curl/기타 언어 예제.
- `scripts/manual_sync/` — 공식 사이트와의 정기 동기화 도구, `docs/manual`·`docs/plugin` 둘 다
  대상 (아래 참고).

## 매뉴얼/플러그인 동기화 워크플로 (`scripts/manual_sync/`)

목적: 공식 Zendesk Help Center 두 섹션과 각각의 로컬 문서를 정기적으로 맞추는 것. 설계 원칙은
**목록 비교는 AI 없이, 실제 패치가 필요한 항목만 AI 호출** — 자세한 흐름은
`scripts/manual_sync/README.md` 참고.

| 섹션 이름(`--section`) | Zendesk 대상 | 추적 방식 | 로컬 문서 |
| --- | --- | --- | --- |
| `manual` | JSON Manual 섹션(651개 아티클, `section_id=30087500371097`) | 섹션 목록 API 그대로 사용 | `docs/manual/*.md` |
| `plugin` | Plug-in 섹션(`section_id=35681419399961`) | ⚠️ 섹션 목록 API가 랜딩 페이지 1건만 반환하므로, `common.py`의 `PLUGIN_ARTICLE_IDS`(78개 고정 목록)를 1건씩 개별 조회 | `docs/plugin/**/*.md` |

```bash
cd scripts/manual_sync
python fetch_manifest.py                  # 스냅샷 갱신, 인자 없으면 manual+plugin 전체
python fetch_manifest.py --section plugin # 특정 섹션만
python check_diff.py                      # 변경 여부 확인 (exit 0=둘 다 없음, 1=하나라도 있음)
python validate_manual.py                 # 패치 후 항상 실행 — docs/manual+docs/plugin 모두 검증
python check_coverage.py                  # 누락 점검 (변경 여부와 무관, exit 1=미검토 항목 있음)
python check_fields.py                    # 필드(Key) 단위 누락 점검 (exit 1=빠진 Key 있음)
python fill_fields.py                     # 빠진 Key를 공식 표에서 그대로 옮겨 섹션 끝에 추가 (추가만, 재실행 안전)
python build_index.py                     # docs/index/ (endpoints.json, chunks.jsonl) 자동 생성
python eval_retrieval.py                  # 색인 검색 시험 (BM25)
```

**"정기 업데이트 체크" 요청을 받으면:**

1. `check_diff.py`로 두 섹션 각각의 변경된 아티클 id 목록을 뽑는다.
2. 플래그된 아티클마다 원문을 다시 읽고, 문서와 필드/내용 단위로 대조한다 — 타임스탬프만 갱신된
   화장빨 변경(cosmetic bump)과 실제 내용 변경을 반드시 구분한다. 타임스탬프 diff만 보고
   변경됐다고 가정하지 않는다.
   - **`locale_note`를 먼저 본다.** 아티클 레벨 `updated_at`은 ko/en-us/**ja** 번역본
     타임스탬프의 최댓값인데 이 저장소는 en-us 본문만 받아온다. 그래서 ko/ja만 편집된 경우
     "changed로 잡혔는데 받아온 본문은 그대로"인 상태가 되고, 이걸 화장빨로 넘기면 실제 변경을
     통째로 놓친다. `check_diff.py`가 changed마다 판정해 주므로 `en-us did NOT`이 뜨면 해당
     로케일 페이지를 직접 열어 대조할 것.
   - `plugin` 섹션에서 랜딩 article(id `35639730101529`, "Plug-in Online Manual")이 변경으로
     잡히면, 이는 실제 내용 변경이 아니라 **Plug-in 목록 자체가 추가/삭제/개명됐다는 신호**일 수
     있다. 랜딩 페이지를 재스크래핑해 링크 목록을 다시 뽑고, `docs/plugin/INDEX.md` 및
     `common.py`의 `PLUGIN_ARTICLE_IDS`와 대조해서 갱신한다.
3. 실제 변경 건만 해당 문서(`docs/manual/*.md` 또는 `docs/plugin/**/*.md`)에 반영, 필요 시
   `INDEX.md`(날짜·항목 개수·상태)도 갱신. `docs/plugin`의 "⬜ 미작성" 항목은 diff가 없어도
   당연히 그대로 둔다 — 작성 여부는 아직 정기 점검 대상이 아니다.
4. `validate_manual.py` 통과 확인 후 `fetch_manifest.py`로 해당 섹션 매니페스트 재스냅샷.
5. `check_diff.py`를 다시 돌려 `has_diff: false`인지 확인.
   - **`fetch_manifest.py`를 `check_diff.py`보다 먼저 돌리지 않는다** — 기준 매니페스트를
     덮어써서 diff가 비어 버린다.
6. **`check_coverage.py`를 매번 돌린다 — diff가 0건이어도 생략하지 않는다.** `check_diff.py`는
   *변경된* 글만 보므로, 처음 문서화할 때 빠진 글은 수정되기 전까지 다시 걸리지 않는다.
   점검 A(글마다 섹션 유무)와 점검 B(공식 목차 표 ↔ `docs/manual` 양방향, 목차↔본문 Input URI
   대조)를 함께 수행한다. 출력의 `NEW` 항목은 문서화하거나, 검토 후
   `coverage_exceptions.json`에 **사유와 함께** 등록한다. 아직 문서화하지 않은 실제 누락은 예외에
   넣지 않는다.
7. **`check_fields.py`로 필드 단위 누락을 본다.** 섹션이 있어도 대표 예시만 실은 곳은 점검 A·B를
   통과하므로, 이 점검의 `unique gaps` 수치가 늘지 않았는지 확인한다. "Key가 문서에 언급되는가"만
   보므로 설명의 정확성은 보증하지 않는다. 늘었으면 해당 섹션을 보강하고, README의 "현재 상태"
   수치와 기준일도 함께 갱신한다. 빠진 Key는 `fill_fields.py`로 채우고(생성 블록은 `<!-- om-fields -->`
   마커로 감싸며 공식 글 기준으로 매번 다시 만들어진다), 반영 후 `build_index.py`로 `docs/index/`를
   다시 만든다. `docs/index/`는 자동 생성물이므로 손으로 고치지 않는다.
8. 커밋·푸시는 사용자가 명시적으로 지시할 때만 진행한다 (자동 push 없음 — 아래 참고).

규모가 크면(예: 20~30개 아티클 동시 플래그) 병렬 서브에이전트로 나눠서: 1차는 리서치/대조
전담(원문 vs 매뉴얼 비교, 실제 변경 여부만 판정), 2차는 1차에서 확정된 사실만 가지고 실제 패치를
적용하는 편집 전담으로 분리하면 효율적이다. 편집 에이전트에게는 반드시 원문 파일 경로, 대상 섹션,
정확한 필드 diff, 따라 할 스타일 템플릿 섹션을 구체적으로 지정한다.

### 알려진 환경 이슈

- **`python3`는 이 머신에서 깨진 Windows Store 스텁을 가리킨다.** 반드시 `python`(3.13.5) 사용.
- **`check_diff.py`의 stdout이 Windows 콘솔(cp949)에서 `UnicodeEncodeError`를 낼 수 있다**
  (`\xa0` 등 미인코딩 문자). `PYTHONIOENCODING=utf-8`을 설정하고 결과를 파일로 리다이렉트해서
  읽는 방식으로 우회한다 (직접 stdout 캡처에 의존하지 않음).

### 스크래핑한 원문을 파싱할 때

공식 아티클 본문을 프로그램으로 대조하려면 두 가지를 먼저 정규화해야 한다. 둘 다 실제로
파싱을 실패시킨다:

- **공백이 U+00A0(non-breaking space)** — 콜론 뒤와 들여쓰기가 일반 공백이 아니다.
  `text.replace("\xa0", " ")` 를 먼저 하지 않으면 정규식·`json.loads` 가 조용히 빗나간다.
- **예제 JSON에 불법 이스케이프** — 일부 아티클의 `EXPORT_PATH` 가 `"D:\00.2023년\..."` 처럼
  역슬래시를 이스케이프하지 않아 그 블록만 `json.loads` 에서 탈락한다. 블록이 통째로 조용히
  누락되므로, 파싱 실패를 무시하지 말고 역슬래시를 이중화해 재시도할 것.

### 공식 문서의 오타·자기모순 처리 원칙

공식 아티클에는 오타와 내부 모순이 흔하다. 같은 아티클의 Specifications 표와 Request 예제가
서로 다른 Key를 제시하는 경우도 있다. 판단 기준:

- **예제(Request Examples)가 표보다 우선한다.** 예제는 실제 동작하는 페이로드이고, 표는 사람이
  옮겨 적은 것이다. 실제로 오타는 항상 표에서만 나왔다.
- **표와 예제가 어긋나면 예제 우선 원칙을 적용하기 전에 반대 로케일부터 받아본다.** 같은
  아티클 id라도 `/hc/ko/`와 `/hc/en-us/`의 본문이 다를 수 있다. 실제로 `/ope/MEMB`는 영문
  요청 예제가 `ELEM_LIST`(표와 일치)인데 한글 요청 예제만 `AELEM`이라, 한글만 보고 예제 우선
  원칙을 적용했다가 방향을 반대로 판단한 사례가 있다(2026-09-06). 한쪽 로케일이 내적으로 일관되고 다른 쪽만 자기모순이면
  일관된 쪽이 정본이다.
- **같은 enum을 문서화한 다른 아티클과 교차 확인한다.** 예: `STORY_DRIFT_METHOD` 3개 값을
  10·13·17절 아티클이 각각 다른 위치에 오타를 냈고, 17절만 온전했다.
- **원문과 다르게 적었다면 그 자리에 근거를 ⚠️ 주석으로 남긴다.** 안 남기면 다음 동기화에서
  "원문과 다르다"며 오타로 되돌려 놓게 된다. 실제로 그 사고가 한 번 있었다.
- 반대로 표기가 애매해 판단을 보류한 경우도 주석으로 명시한다 (예: 20장 Wall Force의
  `SECT_POSITION`·`PARTS` 는 공식 Specifications 표에 설명이 없어 추정임을 밝혀 둠).

## 공개 범위

이 저장소는 **공개 저장소**입니다.

- **공식 온라인 매뉴얼에 공개된 내용은 가능한 한 빠짐없이** `docs/manual`에 반영합니다.
- **공식 온라인 매뉴얼에 없는 내용은 올리지 않습니다.** 로컬에만 두는 파일은 `.git/info/exclude`로
  제외합니다. 세부 기준은 로컬 전용 `CLAUDE.local.md`를 따릅니다.

## `docs/manual/*.md` 문서 관례

각 엔드포인트 섹션은 다음 순서를 따른다:

1. `TABLE_TYPE`(또는 해당 엔드포인트의) enum/스펙 표
2. `Response HEAD`
3. (해당 시) ADDITIONAL 서브섹션 — 제목 형식은 `### ADDITIONAL — <설명> (<날짜> 공식 반영)`,
   요청에 중첩 config 객체가 추가된 경우에만 넣는다
4. `Request / Response JSON`
5. `Python Example`

파라미터 표는 `| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |` 컬럼을 쓴다. 중첩 필드는 설명 앞에
1단계는 `└`, 2단계는 전각 공백 2개 + `└` 를 붙여 들여쓰기를 표시한다.

**설명 언어:** 파라미터 표의 설명은 **원문 언어 그대로** 옮긴다 — 원문이 한글이면 한글, 영문이면
영문. 번역하지 않는다(원문 그대로의 표현을 보존하고 토큰도 아낀다). 저장소 쪽에서 덧붙이는
`기능` 요약·⚠️ 주석은 한글로 쓴다. 이 원칙은 새로 쓰거나 고치는 표에 적용하며, 기존 한글 표를
일괄로 바꾸지는 않는다.

**JP 제품 버전 전용 항목:** 공식 문서에 `ᴶ⁾`(MIDAS CIVIL NX JP Version only)가 붙은 엔드포인트·
`TABLE_TYPE`·필드는 문서의 해당 행에 `ᴶ⁾`를 남기고 `docs/manual/jp_only.json`의 `exclude`에 등록한다
(다른 버전 대상 코드 생성에서 빼기 위한 목록). 일본 **설계코드** 값은 제품 버전 전용과 별개이며
제외하지 않는다. 표시가 불확실하면 `needs_check`에 사유와 함께 둔다.

**표 마크다운 스타일:** 새로 추가하는 표는 반드시 spaced separator(`| --- | --- |`)를 쓴다.
compact(`|---|---|`)는 MD060 린트에 걸린다. **단, 기존에 이미 있던 compact 스타일 표는 건드리지
않는다** — 이미 걸려 있지 않고, 이번 작업 범위가 아니다.

MD024(중복 헤딩)/MD036(강조를 헤딩처럼 사용) 경고는 `20_POST_AnalysisResult_2.md`,
`21_POST_StoryTables.md`, `26_Design_RC_KDS41202022.md` 등 기존 챕터 전체에 이미 깔린 파일 전역
컨벤션이다. 새 섹션이 같은 패턴을 따라가면서 같은 경고가 나는 것은 정상 — "고쳐야 할 것"이 아니다.

**새 섹션(`## N. …`)을 추가하면 챕터 상단의 목록 표(예: 20장 "테이블 목록")에 해당 행도 반드시
추가한다.** `validate_manual.py`는 *TOC 링크 → 헤딩* 방향만 검사하므로, 목록 표에서 빠진 헤딩은
검증을 통과해 버린다. 섹션 개수와 목록 표 행 수가 일치하는지 직접 확인할 것.

새 엔드포인트를 챕터에 추가할 때 챕터 소속 판단이 애매하면(예: 결과 테이블이 POST 챕터 여러 개에
걸칠 수 있는 경우) 공식 아티클 자체의 제목과 각 챕터 문서 서두에 명시된 스코프(예: "17개" 같은
개수 문구)를 근거로 판단한다.

## `docs/plugin/*.md` 문서 관례

`docs/manual`의 Key/Value 스키마 표 관례를 그대로 쓰지 않는다 — Plug-in 원문은 REST 엔드포인트
스펙이 아니라 GUI 사용법 워크스루이기 때문. 개별 툴 문서(`docs/plugin/tools/*.md`)는 다음 순서를
따른다 (`docs/plugin/INDEX.md` 하단에 동일 템플릿이 있음):

1. 개요(Intro) 2. 지원 버전(Developed with) 3. 주요 기능(Benefits, 있으면) 4. 사용 방법(UI
필드별 설명, 표 가능) 5. 참고/제약사항(Note) 6. *(확인된 경우만)* 관련 JSON API 엔드포인트 —
Plug-in이 내부적으로 호출하는 것으로 보이는 `docs/manual/*` 엔드포인트가 있으면 상호 링크,
불확실하면 추측해서 넣지 않는다 7. 원문 링크.

**개별 툴 문서(`tools/*.md`) 52건은 점진적으로 작성한다** — 한 번에 다 채우지 않는다.
`docs/plugin/INDEX.md`의 "상태" 컬럼이 ⬜(미작성)인 항목은 사용자가 요청할 때(또는 배치로)
원문을 다시 스크래핑해 위 템플릿에 맞춰 작성하고, 상태를 ✅로 갱신한다. 규모가 크면 위
"매뉴얼/플러그인 동기화 워크플로"에서 설명한 리서치/편집 분리 서브에이전트 패턴을 그대로
재사용한다. `guide/` 아래 4개 개념·개발 가이드 문서는 이미 전체 작성되어 있다.

파일명은 번호가 아니라 툴 이름을 슬러그화한 것을 쓴다(`tools/Alignment_Editor.md` 등) — 신규
Plug-in이 수시로 추가되는 flat 목록이라 번호를 매기면 삽입할 때마다 재번호가 필요해지기 때문.

## Git 컨벤션

- **커밋·푸시는 사용자가 명시적으로 지시했을 때만 수행한다.** "커밋 푸시" 같은 명확한 지시가
  없으면 변경사항을 만들어도 커밋하지 않는다.
- 커밋 전 `git status --short`로 의도한 파일만 스테이징됐는지 확인.
