# Concurrent Force Calculator

> **원문:** [Concurrent Force Calculator](https://support.midasuser.com/hc/en-us/articles/60341711486361-Concurrent-Force-Calculator)
> **원문 작성:** 2026-07-23 · **원문 최종 편집:** 2026-07-23

---

## 개요

선택한 구조 요소로부터 동시력(concurrent force) 결과를 추출·내보내는 Plug-in이다.
사용자가 선택한 요소·하중조합·력 성분을 기준으로 정리된 표 형태의 력 데이터를 생성해 해석
결과 검토 과정을 단순화한다. 후처리(post-processing) 작업을 간소화해 구조 성능 평가와 엔지니어링
보고서 작성을 쉽게 해준다.

## 지원 버전

`MIDAS CIVIL NX 2025 (v2.1)`

## 주요 기능

- 선택한 구조 요소로부터 동시 내력(internal force) 결과를 빠르게 추출.
- 수동 데이터 수집·후처리에 드는 시간을 줄임.
- 필요한 요소·하중조합에만 집중할 수 있음.
- 다음 력 성분을 선택적으로 지원: `FX`(축력), `FY`(전단력), `FZ`(전단력), `MX`(비틀림모멘트),
  `MY`(휨모멘트), `MZ`(휨모멘트).
- 결과를 Microsoft Excel로 직접 내보내 추가 분석·보고·문서화에 활용 가능.
- 새 Excel 워크시트 생성 또는 기존 워크시트 업데이트 중 선택 가능.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1. 구조 요소 선택 | 동시력 결과가 필요한 모델의 구조 요소 선택 |
| 2. 하중조합 선택 | 결과를 추출할 하중조합을 하나 이상 선택 |
| 3. 력 성분 선택 | 출력에 포함할 력 성분 선택(`FX`, `FY`, `FZ`, `MX`, `MY`, `MZ`) |
| 4. 결과 생성 | Plug-in을 실행해 선택한 요소·하중조합의 동시력 데이터를 추출 |
| 5. Excel로 내보내기 | 새 워크시트로 내보내거나 기존 워크시트를 갱신. 내보낸 표는 검토·필터링·보고에 용이하게 정리됨 |

## 참고/제약사항

- Plug-in 실행 전 구조 해석이 성공적으로 완료되어 있어야 한다.
- 선택된 요소만 처리되며, 선택하지 않은 요소는 출력에 포함되지 않는다.

## 결론 (원문)

Concurrent Force Calculator는 구조 해석 모델에서 동시력 결과를 빠르고 효율적으로 추출·정리·
내보내는 방법을 제공한다. 요소·하중조합·력 성분을 선택적으로 추출할 수 있어 수작업 부담을
최소화하고 엔지니어링 후처리·보고 워크플로의 정확성과 효율성을 높인다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/60341711486361-Concurrent-Force-Calculator](https://support.midasuser.com/hc/en-us/articles/60341711486361-Concurrent-Force-Calculator)
