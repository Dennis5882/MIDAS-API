# MIDAS-API

**MIDAS NX Open API**(MIDAS Gen NX · Civil NX) 공식 온라인 매뉴얼을 **빠짐없이, 원문에 충실하게,
개발자와 AI가 읽기 좋게** 옮긴 참조본입니다.

> **이 저장소는 공식 문서가 아닙니다.** 정본은
> [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937-MIDAS-API-Online-Manual)이며,
> 원문의 권리는 원 저작자(MIDASIT)에 있습니다. 내용이 다르면 공식 매뉴얼이 우선합니다.

---

## 범위

| 맡는 것 | 맡지 않는 것 |
| --- | --- |
| 공식 온라인 매뉴얼에 공개된 내용 | 공식 매뉴얼에 없는 내용 |
| 원문 충실성 — 원문과 다르게 적은 곳은 그 자리에 ⚠️와 근거 | 실제 API 동작의 보증 |
| 공식 글 번호(article id)로 출처 추적 | 코드 라이브러리 제공 |
| 원문 안의 누락·오탈자·자기모순 표시 | |

## 현재 상태 (2026-11-27 기준)

| 항목 | 상태 |
| --- | --- |
| 공식 목차의 경로 276개 (`db` 229 · `ope` 19 · `doc` 11 · `post` 10 · `view` 7) | 모두 해당 섹션 있음 (표기가 목차와 다른 9건 포함) |
| 설계코드 챕터 | STEEL KDS 41 30:2022 · RC KDS 41 20:2022 · SRC AIK-SRC2K · RC AASHTO-LRFD24/20 (교량) |
| 결과 표시 모드 (`view/RESULTGRAPHIC`) | [16-2장](./docs/manual/16_2_VIEW_ResultGraphic.md)에 개별 글 28건 |
| Plug-in 문서 | 73건 중 63건 작성 ([목록](./docs/plugin/INDEX.md)) |
| 교량 설계·평가 신규 글 (2026-11-26 공식 공개) | RC AASHTO-LRFD24/20 102건 반영([28장](./docs/manual/28_Design_RC_AASHTO_LRFD.md)). PSC AASHTO 설계·평가, RC·PSC KDS 24 14 21 글은 작성 중 |
| 필드 단위 완전성 | 공식 글 608건(ko 전용 글 포함)의 요청 Key 11,062개가 모두 문서에 있음. 2026-11-26에 빠져 있던 744개를 해당 섹션 끝의 **"OM 원문 추가 필드"** 블록으로 원문 그대로 추가함 (설명은 영문 원문, 정리·번역 없음) |
| AI 검색용 색인 | `docs/index/`에 엔드포인트 573개 색인(문서화 497, 작성 중인 교량 설계·평가 76)과 청크 1,829개. 검색 시험(BM25)에서 엔드포인트 찾기 hit@5 91%, Key 찾기 hit@5 76.7% (아래 "AI·RAG용 데이터") |

## 문서 읽는 법

- [docs/manual/INDEX.md](./docs/manual/INDEX.md)가 전체 목차입니다.
- **파라미터 설명**은 원문 언어 그대로 옮깁니다. 기존 표도 공식 Specifications 행과 짝이 확인된 설명을 복원했습니다. 보류 사유는 [description_holds.json](./scripts/manual_sync/description_holds.json)에서 확인할 수 있습니다. 09·10·27장의 별도 표에는 기존 번역이 남아 있습니다.
- **⚠️ 표시**는 원문의 오탈자·모순, 또는 원문과 다르게 적은 이유입니다.
- **`ᴶ⁾` 표시**는 MIDAS Civil NX JP 버전 전용입니다. 목록은 [jp_only.json](./docs/manual/jp_only.json)에 있습니다.
- **예제의 출처:** JSON 예제는 원문을 옮긴 것이며 일부는 발췌·재구성했습니다. 매뉴얼 챕터의 **Python 예제는 원문에 없는 것으로, 원문 스키마를 바탕으로 이 저장소에서 작성**했습니다.

---

## 빠른 시작 (Python)

아래 함수는 공식 [Python 예제](https://support.midasuser.com/hc/en-us/articles/30230181806361-Example-Python)의 것입니다.

```python
import requests

# function for MIDAS Open API
def MidasAPI(method, command, body=None):
    base_url = "base_url_here"
    mapi_key = "your_api_key_here"

    url = base_url + command
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": mapi_key
    }

    if method == "POST":
        response = requests.post(url=url, headers=headers, json=body)
    elif method == "PUT":
        response = requests.put(url=url, headers=headers, json=body)
    elif method == "GET":
        response = requests.get(url=url, headers=headers)
    elif method == "DELETE":
        response = requests.delete(url=url, headers=headers)

    print(method, command, response.status_code)
    return response.json()
```

절점 생성 요청은 공식 [Node](https://support.midasuser.com/hc/en-us/articles/35806845654169) 글의 예제입니다.

```python
node_json = {
    "Assign": {
        "1": {"X": -1, "Y": -1, "Z": -1},
        "2": {"X": -2, "Y": -2, "Z": -2},
        "3": {"X": -3, "Y": -3, "Z": -3}
    }
}
MidasAPI("POST", "/db/node", node_json)
```

| 항목 | 값 |
| --- | --- |
| Base URL | `https://moa-engineers.midasit.com:443/gen` (Gen NX) · `/civil` (Civil NX) |
| 인증 헤더 | `MAPI-Key: <제품에서 발급받은 키>` |
| 자세한 설정 | [docs/AUTHENTICATION.md](./docs/AUTHENTICATION.md) |

`MAPI-Key`는 `.env`로 분리해 관리하고 저장소에 커밋하지 마세요.

---

## AI·RAG용 데이터

`docs/index/`는 `docs/manual`에서 **자동 생성**한 파일입니다. 직접 고치지 마세요.

| 파일 | 내용 |
| --- | --- |
| `endpoints.json` | 엔드포인트별 메서드, 공식 글 번호·URL·갱신일, 문서 위치, Key 목록, JP 전용 여부, 문서화 여부(`documented`) |
| `chunks.jsonl` | 엔드포인트 섹션 단위 청크(URI·메서드·표·요청 예제를 함께 묶음, 최대 약 3,500자, 큰 표·코드블록은 분할). 각 청크에 파일, 제목 경로, 엔드포인트, 공식 글 번호, 출처(`source`) 포함 |
| `eval_questions.json` | 검색 시험 질문 250개 (공식 글에서만 생성, 고정 시드) |

청크의 `source` 값으로 무엇을 근거로 삼을지 고르세요.

| `source` | 청크 수 | 내용 |
| --- | --- | --- |
| `om` | 1,058 | 공식 글을 정리한 본문. 파라미터 설명은 공식 원문을 따르며, 보존한 번역이나 ⚠️ 주석을 포함할 수 있음 |
| `om-verbatim` | 126 | "OM 원문 추가 필드" 블록. 공식 표를 그대로 옮긴 것 |
| `repo-example` | 645 | 이 저장소가 작성한 Python 예제·워크플로. **공식 내용이 아니므로 근거로 인용하지 말 것** |

검색 시험 결과는 `python scripts/manual_sync/eval_retrieval.py`로 다시 잴 수 있습니다 (2026-11-27 28장 추가 후 재측정, BM25 기준).

| 질문 | 건수 | hit@1 | hit@5 | hit@10 |
| --- | --- | --- | --- | --- |
| 엔드포인트 찾기 (글 제목 → 해당 청크) | 100 | 79% | 91% | 93% |
| Key 찾기 (글 제목 + 설명 → 그 Key가 든 청크) | 150 | 54% | 76.7% | 82.0% |

시험의 한계:

- BM25는 일부러 단순한 기준선입니다. 벡터 검색을 쓰면 같은 청크로 더 나을 수 있습니다.
- 청크가 클수록 맞히기 쉬워집니다. 청크 중앙값은 약 1,200자입니다.
- 질문은 공식 글의 영문 설명이라, 같은 문구를 담은 `om-verbatim` 청크가 유리합니다. 한글로 번역된 설명은 상대적으로 덜 잡힙니다.
- `KEYS`·`EXPORT_PATH`처럼 여러 글이 공유하는 항목은 어느 글의 것인지 가리기 어렵습니다.
- "찾았는가"만 봅니다. 설명이 맞는지는 보지 않습니다.

## 저장소 구조

```text
docs/
├── manual/              # JSON Manual 참조본 (INDEX.md부터, 01~27장 + 16-2장)
├── plugin/              # Plug-in 문서
├── index/               # AI·RAG용 자동 생성 색인과 청크
└── AUTHENTICATION.md    # Base URL, MAPI-Key, 언어별 인증 예제
examples/                # 예제 코드 (출처는 examples/README.md)
scripts/manual_sync/     # 공식 매뉴얼과의 동기화·점검 도구
```

## 동기화·점검 도구

모두 AI 호출 없이 동작합니다. 자세한 사용법은 [scripts/manual_sync/README.md](./scripts/manual_sync/README.md).

| 스크립트 | 확인하는 것 |
| --- | --- |
| `check_diff.py` | 공식 글의 추가·삭제·변경 (GitHub Actions가 매주 실행) |
| `check_coverage.py` | 모든 글에 섹션이 있는지, 공식 목차와 어긋나지 않는지 |
| `check_fields.py` | 공식 글의 요청 Key가 문서에 있는지 |
| `fill_fields.py` | 빠진 Key를 공식 표에서 그대로 옮겨 섹션 끝에 추가 (추가만 함) |
| `build_index.py` · `eval_retrieval.py` | AI용 색인·청크 생성, 검색 시험 |
| `restore_descriptions.py --dry-run` | 문서 파라미터의 설명·필수 표기와 공식 Specifications 비교 |
| `validate_manual.py` | JSON 코드블록과 목차 앵커 |

## 공식 문서

- [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937-MIDAS-API-Online-Manual)
- [JSON Manual 섹션](https://support.midasuser.com/hc/en-us/sections/30087500371097-JSON-Manual)
- [MIDAS CIVIL NX Open API 동작 원리](https://support.midasuser.com/hc/en-us/articles/30212837484441-How-to-work-MIDAS-CIVIL-NX-Open-API)
- 예제: [Python](https://support.midasuser.com/hc/en-us/articles/30230181806361-Example-Python) · [Excel VBA](https://support.midasuser.com/hc/en-us/articles/30506684736665-Example-Excel-VBA) · [기타 언어](https://support.midasuser.com/hc/en-us/articles/30506872725017-Example-Various-Programming-Languages)
