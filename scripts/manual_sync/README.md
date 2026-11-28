# MIDAS API Manual Sync

`docs/manual/`(JSON Manual 섹션)과 `docs/plugin/`(Plug-in 섹션)을 MIDAS API 공식 온라인 매뉴얼(Zendesk Help Center)과 정기적으로 동기화하기 위한 스크립트 모음입니다. 핵심 설계: **목록 비교는 AI 없이, 실제 패치가 필요한 항목에 대해서만 AI를 호출**해서 매번 전체를 재검토하는 데 드는 토큰 비용을 피합니다.

## 추적 대상 섹션

`common.py`의 `SECTIONS`에 등록되어 있으며, `--section manual|plugin` 인자로 개별 지정하거나 생략해 전체를 대상으로 실행할 수 있습니다. 두 섹션은 추적 **방식(mode)**이 다릅니다.

| 이름 | mode | 대상 문서 | 매니페스트 |
| --- | --- | --- | --- |
| `manual` | `section` — `sections/{id}/articles.json`로 860개 아티클을 나열 (en-us 790 + ko 전용 70, 두 로케일 목록을 합침) (JSON Manual, `section_id=30087500371097`) | `docs/manual/*.md` — REST 엔드포인트 스키마 표 | `docs/manual/.sync_manifest.json` |
| `plugin` | `id_list` — `common.PLUGIN_ARTICLE_IDS`(78개, 명시적 목록)를 `articles/{id}.json`로 1건씩 조회 | `docs/plugin/**/*.md` — GUI 내장 Plug-in 툴 사용법 | `docs/plugin/.sync_manifest.json` |

`plugin`이 `id_list`인 이유: Plug-in Zendesk 섹션(`section_id=35681419399961`)은 `sections/{id}/articles.json`을 호출해도 "Plug-in Online Manual" 랜딩 페이지 **1건만** 돌아옵니다. 나머지 56개(가이드 4 + 개별 툴 52)는 그 랜딩 페이지 본문 HTML 안에 있는 `<a href>` 링크일 뿐이고, 각각 API로는 찾을 수 없는 별도 `section_id`에 흩어져 있습니다. 그래서 `docs/plugin/INDEX.md`를 만들 때 추출한 57개 article id를 `common.py`에 고정 목록으로 박아두고 개별 조회합니다. **신규 Plug-in이 추가되면 랜딩 페이지 자체의 `updated_at`이 바뀌므로 `changed` 목록에 랜딩 article(`35639730101529`)이 잡히고**, 이를 신호로 랜딩 페이지를 재스크래핑해 `PLUGIN_ARTICLE_IDS`와 `INDEX.md`를 갱신해야 합니다(코드 수정이 필요하므로 자동 반영되지 않음).

## 구성

| 파일 | 역할 | AI 사용 |
|---|---|---|
| `common.py` | Zendesk API 호출, 섹션 레지스트리, 매니페스트 로드/저장, diff 계산 공통 로직 | ✗ |
| `fetch_manifest.py` | 현재 홈페이지 상태를 섹션별 `.sync_manifest.json`에 스냅샷으로 저장 (`--section` 생략 시 전체) | ✗ |
| `check_diff.py` | 매니페스트와 현재 홈페이지 상태를 섹션별로 비교해 added/removed/changed article만 추출 (`--section` 생략 시 전체). changed 항목마다 **어느 로케일이 바뀌었는지** 판정해 `locale_note`로 표시 (`--no-locales`로 생략 가능) | ✗ |
| `validate_manual.py` | `docs/manual/*.md` + `docs/plugin/**/*.md`의 JSON 코드블록 유효성 + TOC 앵커 정합성 검증 | ✗ |
| `check_coverage.py` | 변경 여부와 무관한 누락 점검 — (A) manual 섹션의 모든 글이 `docs/manual`에 섹션을 갖는지, (B) 공식 목차 표와 `docs/manual`의 양방향 대조 및 목차↔글 본문 Input URI 대조 | ✗ |
| `check_fields.py` | 필드 단위 누락 점검 — 공식 글의 Specifications 표 Key와 Schema·요청 예제의 JSON Key가 해당 문서 섹션(챕터 공통 표 포함)에 있는지 대조 | ✗ |
| `fill_fields.py` | 빠진 Key를 공식 Specifications 표에서 원문 그대로 옮겨 해당 섹션 끝에 `<!-- om-fields -->` 블록으로 추가. 기존 텍스트는 수정하지 않고, 재실행하면 블록만 다시 만듦 | ✗ |
| `restore_descriptions.py` | 설명·필수 표기를 공식 Specifications와 대조. 기본 적용은 한글 설명, `--english` 적용은 영어 설명 대상 | ✗ |
| `check_specs.py` | 색인으로 공식 글을 식별해 기본값·Value 타입·필수 표기와 판별 값별 Response HEAD를 대조. 실제 차이가 있으면 종료 1 | ✗ |
| `description_holds.json` | 원문과 다르게 보존한 설명·필수 값 및 대조 기준 | — |
| `build_index.py` | `docs/index/endpoints.json`·`chunks.jsonl` 생성 (AI·RAG용). 끝에 `build_llms.py`를 불러 루트 `llms.txt`도 다시 만듦 | ✗ |
| `build_llms.py` | 루트 `llms.txt`(AI 에이전트용 진입점) 생성. 네트워크 없이 `docs/index/`와 `docs/manual/INDEX.md`만 읽음 | ✗ |
| `eval_retrieval.py` | 청크 색인의 검색 시험 (BM25, 질문은 공식 글에서만 생성) | ✗ |
| `om_parse.py` | 공식 글 HTML의 Specifications 표 파서 (공용) | ✗ |
| `coverage_exceptions.json` | 검토를 마친 `check_coverage.py` 항목과 그 사유 | — |

AI(Claude)는 CI에서 자동 호출되지 않습니다 — **API 키를 CI에 등록하지 않는 것이 의도된 설계**입니다. 대신 GitHub Actions는 변경 여부만 무료로 확인해서 GitHub Issue로 알리고, 실제 패치는 사람이 Claude Code 대화창을 열어 직접 트리거합니다.

## 동작 원리

```
[매주, 저비용, 무료] GitHub Actions → check_diff.py (manual + plugin 두 섹션 모두)
      │  Zendesk article의 id/updated_at만 조회, 매니페스트와 비교
      │  → 순수 스크립트, LLM 미호출, API 키 불필요
      │
      ├─ 변경 없음 → 종료
      │
      └─ 변경 있음 → GitHub Issue 생성/갱신 (diff + 붙여넣을 프롬프트 포함)
             │
             └─ [사람이 트리거] 이슈 내용을 Claude Code 대화창에 붙여넣음
                    → 해당 항목만 재스크래핑 → 매핑되는 섹션만 패치
                    → validate_manual.py로 검증 → fetch_manifest.py로 매니페스트 갱신
                    → 커밋·푸시는 사용자 확인 후 진행
```

## 로컬 실행

```bash
cd scripts/manual_sync

# 최초 1회 또는 업데이트 반영 후 스냅샷 갱신 (인자 없으면 manual+plugin 전체)
python3 fetch_manifest.py
python3 fetch_manifest.py --section plugin   # 특정 섹션만

# 변경 여부만 확인 (exit 0 = 변경없음, exit 1 = 변경있음 + diff 출력)
python3 check_diff.py

# 문서 패치 후 항상 실행 — JSON/TOC 무결성 검증 (docs/manual + docs/plugin 모두 스캔)
python3 validate_manual.py

# 누락 점검 — 정기 점검마다 실행 (exit 0 = 미검토 항목 없음)
python3 check_coverage.py

# 필드 단위 누락 점검 (--out 으로 글별 상세 JSON 저장)
python3 check_fields.py --out fields.json

# 설명과 필수 표기 차이 점검
python -X utf8 restore_descriptions.py --dry-run

# 문서 반영 후 색인을 갱신하고 글별 스펙 점검
python -X utf8 build_index.py
python -X utf8 check_specs.py --json

# 한 챕터의 영어 설명 복원 후보 확인 및 보고서 경로 지정
python -X utf8 restore_descriptions.py --file 02_DB_Project_Structure.md --dry-run --english --report ../../work_orders/02_review.md
```

`restore_descriptions.py --dry-run`은 따옴표로 묶인 Key가 있는 6열 파라미터 표를 대조하고
결과를 보고서에 덧붙입니다. 차이가 보이면 공식 글을 확인해 원문 변경과 기존 편집을 구분합니다.
정기 점검에서 확인할 수치는 영어 행의 `변경` + `보류 — 원문 변경`입니다.
등록된 행의 공식 설명이나 필수 값이 [description_holds.json](description_holds.json)에 기록된 값과
달라지면 `보류 — 원문 변경`으로 표시됩니다. 보류 목록에는 범위·단위와 필수 조건을 보존한 사유도 있습니다.
`--dry-run` 없이 실행하면 짝이 확인된 한글 설명을 복원합니다. 영어 행은 `--english`로 지정합니다.
JP·⚠️ 보호 행도 원문과 대조하며 실제 차이는 의도적 차이로 분류합니다. 보류, 모호, 짝 없음 행은 보고서에서 확인할 수 있습니다.

2026-11-27 기준(공식 글 860건)으로 대조한 영어 행은 6,582개입니다. 변경 0행, 보류 — 원문 변경 0행, 보류 17행입니다.
보류 17행 중 16행은 공식 표가 같은 글의 예제·Schema와 어긋나 기존 표기를 유지한 행이며, 문서의 해당 표 아래 ⚠️ 주석에 원문 표기를 적었습니다.

`check_specs.py`는 `endpoints.json`의 글별 위치와 `chunks.jsonl`을 이용한다. 결과에는 공식 글 ID,
로케일, 문서 위치 및 비교 값이 포함된다. `--file`로 번호가 붙은 챕터 하나를 선택하고, `--source`로
저장한 공식 원문을 재사용할 수 있다. [spec_holds.json](spec_holds.json)은 보류의 근거와 원문 값을
기록한다. 원문 값이 달라지면 다시 실제 차이로 표시된다.

## 필드 점검 읽는 법 (`check_fields.py`)

- `unique gaps (endpoint, key)`가 대표 수치입니다. 국가별 글처럼 여러 글이 같은 스키마를 공유하므로
  글 단위 합계(`missing keys`)는 같은 누락을 여러 번 셉니다.
- Key 이름이 섹션에 **언급되는지**만 봅니다. 설명·타입이 맞는지는 확인하지 않습니다.
- Schema나 예제에만 있는 Key도 포함합니다. 원문 Schema의 오탈자가 Key로 잡힐 수 있습니다.
- 2026-11-26 첫 측정: unique gaps 744개(이 중 Specifications 표에 있는 것 611개), 65개 엔드포인트.
  같은 날 `fill_fields.py`로 모두 추가해 0이 됐다. 이후 0이 아니면 공식 글이 바뀌었거나 문서가 달라진 것이다.
- `fill_fields.py`가 넣은 행은 원문 그대로라 중첩 필드의 상위 Key가 표에 보이지 않을 수 있다(`No.`만 남음).

## 누락 점검 메모 (`check_coverage.py`)

2026-11-27 기준 매뉴얼 33개 파일에 교량 설계·평가 28~32장을 포함합니다.
공식 글 838건의 요청 Key 13,359개에서 누락 0건이며, coverage의 NEW와 stale은 모두 0건입니다.

- `check_diff.py`만으로는 **처음부터 빠진 글**을 찾지 못합니다. `/db/HHND`·`/db/GALD`·`/db/ULCT`는
  매니페스트에 등록돼 있었지만 섹션이 없었고, 글이 수정되지 않아 계속 통과했습니다(2026-11-26 추가).
- **공식 목차 표에 행이 없는 엔드포인트**: `/db/REBB`, `/db/REBC`, `/db/REBR`, `/db/REBW`. 개별
  글과 24장 섹션은 있으므로 "문서에만 있음"은 오류가 아닙니다. `/db/HHCT-M1`은 목차에 있지만
  앞의 `/` 없이 `db/HHCT-M1`로 적혀 있어, `/`로 시작하는 행만 세면 누락으로 잘못 보입니다.
- 목차의 주소가 글 본문과 다른 경우가 있습니다(`/db/ULCT`, 설계 부재력 `/post/…DESIGNFORCES`).
  글 본문 Input URI만 대조하면 놓치므로 목차 대조를 함께 봅니다.
- GitHub Actions는 `check_diff.py`만 실행합니다. 누락 점검은 로컬에서 실행합니다.

## 로케일 판정 — `changed`가 떴는데 본문은 그대로일 때

Zendesk의 아티클 레벨 `updated_at`은 **그 아티클의 모든 번역본 `updated_at` 중 최댓값**입니다.
그런데 `common.py`의 `BASE`(`SYNC_LOCALE = "en-us"`)는 **영문 본문만** 받아옵니다. 그래서
ko나 ja만 편집된 경우 → `check_diff.py`는 changed로 잡는데 → 받아온 영문 본문은 한 글자도 안
바뀐 상태가 됩니다. 이걸 "타임스탬프만 갱신된 화장빨"로 판정하고 넘기면 **실제 변경을 통째로
놓칩니다.**

`check_diff.py`는 changed 항목마다 `articles/{id}/translations.json`을 한 번 호출해
(직전 스냅샷의 `updated_at`보다 새로운 로케일만 골라) 다음 셋 중 하나로 판정합니다:

| `locale_note` | 뜻 | 대응 |
| --- | --- | --- |
| `en-us changed — normal review` | 평소대로 영문 본문이 바뀜 | 기존 절차대로 대조 |
| `ko/ja changed but en-us did NOT ...` | **우리가 받는 본문에는 안 보이는 변경** | 해당 로케일 페이지를 직접 열어 대조 |
| `metadata only — no translation body is newer` | 어떤 번역본도 새로워지지 않음 | 진짜 화장빨, 넘어가도 됨 |

전수 스캔 근거(2026-09-06, 719건):

- 719건 중 492건이 `ko+en-us+ja`, 174건이 `ko+en-us`. **ja 번역이 존재한다는 사실 자체가
  이 스캔 전까지 파악되지 않았습니다.**
- `/ope/MEMB`(`49514964272665`)의 `2026-07-30` 갱신은 ko도 en-us도 아닌 **ja 번역**이 만든
  것이었습니다. 정작 ko와 en-us 본문은 요청 Key가 서로 다른 채로 2025년부터 방치돼 있었고,
  그 분기를 못 본 탓에 한때 **방향을 반대로 판단**했습니다.
- SSEIS(`58908676674585`)의 ko 본문 오염도 en-us는 멀쩡한 채 ko만 바뀐 경우라, 이 판정이
  없으면 화장빨로 걸러졌을 사안이었습니다.

**로케일 간 본문이 얼마나 벌어져 있는지 전수 점검하려면** `translations.json`의
`updated_at`·본문 길이를 아티클별로 비교하면 됩니다(`common.py`의 `fetch_translations()`).
2026-09-06 스캔에서는 본문 길이 비율이 크게 어긋난 9건과, **ko 본문이 서로 바이트 단위로
동일한 아티클 쌍 2쌍**(SSEIS, Static Wind Load)이 나왔습니다.

## GitHub Actions (체크 전용, API 키 불필요)

`.github/workflows/manual-sync.yml`이 매주 월요일(UTC 03:17) `check_diff.py`만 실행합니다. 변경이 감지되면:
- 실행 로그에 diff 출력
- `manual-diff` 아티팩트로 diff JSON 업로드
- 저장소에 "MIDAS API manual 변경 감지" 이슈를 생성(이미 열려있으면 코멘트 추가) — 이슈 본문에 **그대로 복사해서 Claude Code 대화창에 붙여넣을 프롬프트**가 포함되어 있습니다.

추가 시크릿 등록이 필요 없습니다(기본 `GITHUB_TOKEN`만 사용). **수동 실행:** Actions 탭 → "MIDAS API Manual Sync Check" → Run workflow.

## 실제 갱신은 어떻게 하나요

1. 이슈 알림(또는 직접 `python3 check_diff.py` 실행 결과)을 확인
2. 이슈 본문의 프롬프트를 그대로 이 저장소가 열려있는 Claude Code 대화창에 붙여넣기
3. Claude가 diff에 해당하는 article만 재확인해서 매핑되는 섹션을 패치하고 `validate_manual.py`로 검증
4. 커밋·푸시는 Claude가 항상 사용자 확인을 받고 진행 (자동 push/PR 없음)
