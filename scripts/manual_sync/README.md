# MIDAS API Manual Sync

`docs/manual/`(JSON Manual 섹션)과 `docs/plugin/`(Plug-in 섹션)을 MIDAS API 공식 온라인 매뉴얼(Zendesk Help Center)과 정기적으로 동기화하기 위한 스크립트 모음입니다. 핵심 설계: **목록 비교는 AI 없이, 실제 패치가 필요한 항목에 대해서만 AI를 호출**해서 매번 전체를 재검토하는 데 드는 토큰 비용을 피합니다.

## 추적 대상 섹션

`common.py`의 `SECTIONS`에 등록되어 있으며, `--section manual|plugin` 인자로 개별 지정하거나 생략해 전체를 대상으로 실행할 수 있습니다. 두 섹션은 추적 **방식(mode)**이 다릅니다.

| 이름 | mode | 대상 문서 | 매니페스트 |
| --- | --- | --- | --- |
| `manual` | `section` — `sections/{id}/articles.json`로 651개 아티클을 한 번에 나열 (JSON Manual, `section_id=30087500371097`) | `docs/manual/*.md` — REST 엔드포인트 스키마 표 | `docs/manual/.sync_manifest.json` |
| `plugin` | `id_list` — `common.PLUGIN_ARTICLE_IDS`(57개, 명시적 목록)를 `articles/{id}.json`로 1건씩 조회 | `docs/plugin/**/*.md` — GUI 내장 Plug-in 툴 사용법 | `docs/plugin/.sync_manifest.json` |

`plugin`이 `id_list`인 이유: Plug-in Zendesk 섹션(`section_id=35681419399961`)은 `sections/{id}/articles.json`을 호출해도 "Plug-in Online Manual" 랜딩 페이지 **1건만** 돌아옵니다. 나머지 56개(가이드 4 + 개별 툴 52)는 그 랜딩 페이지 본문 HTML 안에 있는 `<a href>` 링크일 뿐이고, 각각 API로는 찾을 수 없는 별도 `section_id`에 흩어져 있습니다. 그래서 `docs/plugin/INDEX.md`를 만들 때 추출한 57개 article id를 `common.py`에 고정 목록으로 박아두고 개별 조회합니다. **신규 Plug-in이 추가되면 랜딩 페이지 자체의 `updated_at`이 바뀌므로 `changed` 목록에 랜딩 article(`35639730101529`)이 잡히고**, 이를 신호로 랜딩 페이지를 재스크래핑해 `PLUGIN_ARTICLE_IDS`와 `INDEX.md`를 갱신해야 합니다(코드 수정이 필요하므로 자동 반영되지 않음).

## 구성

| 파일 | 역할 | AI 사용 |
|---|---|---|
| `common.py` | Zendesk API 호출, 섹션 레지스트리, 매니페스트 로드/저장, diff 계산 공통 로직 | ✗ |
| `fetch_manifest.py` | 현재 홈페이지 상태를 섹션별 `.sync_manifest.json`에 스냅샷으로 저장 (`--section` 생략 시 전체) | ✗ |
| `check_diff.py` | 매니페스트와 현재 홈페이지 상태를 섹션별로 비교해 added/removed/changed article만 추출 (`--section` 생략 시 전체) | ✗ |
| `validate_manual.py` | `docs/manual/*.md` + `docs/plugin/**/*.md`의 JSON 코드블록 유효성 + TOC 앵커 정합성 검증 | ✗ |
| `prompt_sample.md` | 최초 매뉴얼 문서(01~27)를 사람이 손으로 생성할 때 썼던 프롬프트 예시 (참고용, 실행 스크립트 아님) | — |

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
```

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
