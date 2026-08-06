# Easy Result Table

> **원문:** [Easy Result Table](https://support.midasuser.com/hc/ko/articles/49504449511705-Easy-Result-Table)
> **원문 작성:** 2025-08-05 · **원문 최종 편집:** 2026-07-27

---

## 개요

구조계산서에 들어가는 후처리 결과 테이블(Reaction, Story Drift 등)을 메뉴별로 하나씩 찾아
들어가지 않고, 필요한 테이블을 한 번에 모아 구조계산서용 PDF로 일괄 출력하는 Plug-in이다.

## 지원 버전

`MIDAS GEN NX 2025 (v1.1) KR`

## 주요 기능

- 프로젝트마다 반복되던 "결과 테이블별로 메뉴에 들어가 수동 확인·저장" 과정을 제거 — 구조계산서에
  들어가는 결과 테이블은 적게는 3개, 많게는 10개 이상이라 반복 작업 부담이 컸다.
- 자주 확인하는 테이블 구성을 **세팅값으로 미리 저장**해두고, 이후 프로젝트에서도 동일 설정을
  불러와 자동 출력.

## 사용 방법

| 영역 | 설명 |
| --- | --- |
| Result Table 리스트 | 사용 가능한 결과 항목(Reaction, Story Drift, Overturning Moment 등)을 트리 구조로 표시. 각 항목 우측 **Add** 버튼으로 현재 테이블에 추가 |
| Settings 패널 | 리스트에서 선택한 항목의 세부 옵션(표시할 층 범위, 단위, 정렬 순서 등) 조정 후 **Save**로 확정 |
| Save / Load | 재설정 정보·결과 테이블 구성을 로컬 `.json`으로 저장/재사용 |
| CREATE TABLE | Add된 모든 항목·설정을 반영해 최종 결과 테이블 생성 → **Export to PDF**로 구조계산서용 PDF 출력 |
| 리스트 관리 툴바 | `+`: 커스텀 항목 추가 다이얼로그, 🗑️: 선택 항목 삭제 |

**사용 절차:** 원하는 그룹에서 `Add` 클릭 → 추가된 항목 선택(Settings 패널 활성화) → Load Case
Name·Units(Force, Distance)·Styles(Style, Decimal Places) 지정 → `Save` → `Create Table` →
Table Processing Status에서 성공(OK)/출력 불가(NG) 확인 → `Download PDF`
(`all-table-YYYY-MM-DD.pdf`).

## 참고/제약사항

이 Plug-in이 출력을 지원하는 후처리 결과 테이블 목록:

- Reaction Force/Moments(Global)
- Vibration Mode Shape(Eigenvalue Mode)
- Story Drift (X, Y)
- Story Displacement (X, Y)
- Story Shear (Response Spectrum Analysis)
- Story Eccentricity
- Story Shear Force Ratio
- Stability Coefficient (X, Y)
- Weight Irregularity Check (X, Y)
- Overturning Moment
- Story Axial Force Sum
- Torsional Amplification Factor (X, Y)
- Stiffness Irregularity Check (Soft Story) (X, Y)
- Capacity Irregularity Check (Weak Story)

## 관련 JSON API 엔드포인트

Plug-in이 조회하는 후처리 결과 테이블은 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/post/table` — Reaction](../../manual/19_POST_AnalysisResult_1.md#1-reaction)
- [`/post/table` — Vibration Mode Shape](../../manual/20_POST_AnalysisResult_2.md#28-vibration-mode-shape)
- [`/post/table` — Story Drift 등 층 결과 테이블 전반](../../manual/21_POST_StoryTables.md) *(Story
  Displacement, Story Shear, Story Eccentricity, Overturning Moment 등 목록 대부분이 이 챕터에
  해당)*

## 결론 (원문)

이 Plug-in은 반복적인 후처리 결과 출력 업무를 자동화하여, 시간을 절약하고 문서화의 일관성을
유지할 수 있는 강력한 도구다.

## 원문 링크

[https://support.midasuser.com/hc/ko/articles/49504449511705-Easy-Result-Table](https://support.midasuser.com/hc/ko/articles/49504449511705-Easy-Result-Table)
