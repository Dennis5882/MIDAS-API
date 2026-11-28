# AGENTS.md

> **Using this repository to find or call MIDAS API endpoints?** Read [llms.txt](./llms.txt) instead.
> It explains where to look up an endpoint, which sources you may cite, and the chapter map.
> This file is for agents that **edit or maintain** this repository.

## 먼저 읽을 것

이 저장소의 작업 규칙 본문은 [CLAUDE.md](./CLAUDE.md)에 있습니다. 작업을 시작하기 전에 전부 읽고 따르세요.
이 파일은 그 요약과 진입점일 뿐이며, 둘이 다르면 CLAUDE.md가 우선합니다.

## 저장소 성격

- MIDAS NX Open API 공식 온라인 매뉴얼(JSON Manual)을 원문에 충실하게 옮긴 **공개 문서 저장소**입니다. 코드 라이브러리가 아닙니다.
- 문서: `docs/manual/` (엔드포인트 챕터, 목차는 `INDEX.md`), `docs/plugin/` (Plug-in 툴), `docs/AUTHENTICATION.md`.
- 도구: `scripts/manual_sync/` (공식 사이트 동기화와 점검).
- 자동 생성물: `docs/index/`, `llms.txt`, 문서 안의 `<!-- om-fields -->` 블록. **손으로 고치지 않습니다.**

## 꼭 지킬 것

- **원문 그대로.** 파라미터 표의 설명은 공식 원문 언어 그대로 옮기고 번역하지 않습니다. 저장소가 덧붙이는 `기능` 요약과 ⚠️ 주석만 한글로 씁니다.
- **공식 매뉴얼에 없는 내용은 올리지 않습니다.** 공개 저장소입니다. 실측 결과, 사내 정보, 티켓 내용 등을 문서·주석·커밋 메시지에 쓰지 않습니다.
- 공식 문서의 오타·모순은 CLAUDE.md의 "공식 문서의 오타·자기모순 처리 원칙"을 따르고, 원문과 다르게 적은 곳에는 ⚠️ 주석으로 근거를 남깁니다.
- 새 표는 spaced separator(`| --- |`)를 씁니다. 기존 compact 표는 건드리지 않습니다.
- 새 섹션을 추가하면 챕터 상단 목록 표에도 행을 추가합니다.
- **커밋·푸시는 사용자가 명시적으로 지시했을 때만** 합니다.
- 비밀값(`MAPI-Key` 등)은 커밋하지 않습니다.

## 실행 환경

- Python은 `python -X utf8`로 실행합니다. 이 저장소의 기준 환경(Windows)에서는 `python3`를 쓰지 않습니다.
- Windows 콘솔 인코딩 문제를 피하려면 `PYTHONIOENCODING=utf-8`을 설정합니다.
- 파일마다 줄바꿈(CRLF/LF)을 원래대로 유지합니다.

## 변경 후 점검 (`scripts/manual_sync/`에서 실행)

```bash
python -X utf8 validate_manual.py                     # JSON 블록, 목차 앵커, 파일 간 링크
python -X utf8 check_coverage.py                      # 공식 글 ↔ 문서 섹션 누락
python -X utf8 check_fields.py                        # 필드(Key) 단위 누락
python -X utf8 restore_descriptions.py --dry-run --english   # 설명이 원문과 다른 행
python -X utf8 build_index.py                         # docs/index/와 llms.txt 다시 생성
python -X utf8 check_specs.py                          # 기본값·타입·필수·Response HEAD 원문 대조
python -X utf8 -m unittest discover -p 'test*.py'
```

정기 동기화 순서와 각 점검의 판단 기준은 CLAUDE.md의 "매뉴얼/플러그인 동기화 워크플로"를 따릅니다.
특히 `fetch_manifest.py`를 `check_diff.py`보다 먼저 실행하지 않습니다.
