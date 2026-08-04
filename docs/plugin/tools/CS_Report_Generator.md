# CS Report Generator

> **원문:** [CS Report Generator](https://support.midasuser.com/hc/en-us/articles/56841756166681-CS-Report-Generator)
> **원문 작성:** 2026-04-10 · **원문 최종 편집:** 2026-04-10

---

## 개요

MIDAS CIVIL NX 모델의 명확한 단계별(stage-wise) 시공단계 보고서를 생성하는 Plug-in이다.
시공단계 전반의 구조·경계·하중 그룹의 활성화/비활성화 상태를 요약해 빠른 검증·문서화를
돕는다. Excel 기반 보고서 미리보기와 다운로드를 제공한다.

## 지원 버전

`MIDAS CIVIL NX 2026 (v1.1)`

## 주요 기능

- **빠른 개요:** 시공단계별 활성/비활성 구조 그룹, 경계 그룹, 하중 그룹을 하나의 통합 Excel
  보고서로 즉시 요약.
- **모델링 오류 감소:** 시공단계 설정을 표 형식으로 노출해, 누락되거나 의도치 않은 활성화를
  발견하는 데 도움.
- **시간 절약 워크플로:** CIVIL NX 안의 여러 대화상자·표·창을 수동으로 확인하는 대신 모든
  시공단계 데이터를 자동 추출.

## 사용 방법

| 버튼 | 설명 |
| --- | --- |
| Generate Report | 시공단계 데이터를 추출해 Excel 보고서를 자동 생성·미리보기 |
| Download Excel Report | `.xlsx` 형식으로 보고서 내보내기 |
| Reset | 현재 세션을 초기화하고 새 보고서 생성 |

## 참고/제약사항

이 Plug-in은 다음을 **수정하지 않는다** — 읽기 전용(read-only) 검증·보고 유틸리티다.

- 모델 데이터
- 시공단계(Construction Stages)
- 활성화/비활성화 설정

## 관련 JSON API 엔드포인트

Plug-in이 추출하는 시공단계 정의는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/STAG` — Define Construction Stage](../../manual/10_DB_Construction_Stage.md)

## 결론 (원문)

Construction Stage Report Generator는 MIDAS CIVIL NX에서 시공단계 설정을 검증하는 과정을
단순화한다. 명확하고 구조화되어 있으며 내보낼 수 있는 요약을 제공해, 엔지니어가 모델을
빠르게 검증하고 오류를 줄이며 생산성을 높일 수 있게 한다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/56841756166681-CS-Report-Generator](https://support.midasuser.com/hc/en-us/articles/56841756166681-CS-Report-Generator)
