# Floor Load Table Generator

> **원문:** [Floor Load Table Generator](https://support.midasuser.com/hc/ko/articles/49475987573657-Floor-Load-Table-Generator)
> **원문 작성:** 2025-08-04 · **원문 최종 편집:** 2026-07-27

---

## 개요

구조설계에서 사용하는 중력 방향 바닥하중(Dead Load / Live Load) 정보를 실(room)·공간 단위로
일괄 관리하고, 구조계산서용 하중표(PDF)와 해석 모델 입력을 동시에 자동 처리하는 Plug-in이다.

## 지원 버전

`MIDAS GEN NX 2025 (v1.1) KR`

## 주요 기능

- 한 번의 세팅으로 **PDF 출력 + 해석 모델 자동 입력을 동시 처리**.
- 하중 조건을 **프로파일(.json)로 저장/불러오기**해 프로젝트마다 재사용 가능.
- 구조 형식에 관계없이 범용적으로 적용 가능.
- 층별·공간별(마감재·천장·설비 조건 등)로 반복되던 수작업 하중표 작성·재입력 과정을 제거해
  업무 시간을 절감하고 오류를 방지.

## 사용 방법

| 영역 | 설명 |
| --- | --- |
| Global Setting | 프로젝트명, DL/LL Factor(하중계수), DL/LL Case(매핑할 Load Case), 회사 로고 이미지 등 전체 프로젝트 공통 정보 설정 |
| Category | Category Name 입력 후 `+` 버튼으로 카테고리(예: 사무실, 기계실) 생성 — 공간·용도별 하중 분류 단위 |
| Load Group | 선택한 Category 안에서 세부 하중 그룹 추가. 각 그룹에 면적, DL, LL 등 하중 정보 입력 — 구조계산서 테이블의 핵심 데이터 |
| Save / Load | 설정과 하중표 구성을 로컬 `.json` 파일로 저장/재사용 |
| Export to PDF | 하중 테이블을 구조계산서용 PDF로 출력 |
| Send to MIDAS | 입력된 Load Group 정보를 Gen NX의 **Define Floor Load** 항목에 일괄 등록 |

**Load Group 입력 항목:**

| 항목 | 설명 |
| --- | --- |
| Name | 재료·구성 요소명 (예: 콘크리트 슬래브, 보통 모르터) |
| Type | `thickness`(두께 기반 산정) 또는 `load`(면적당 하중 직접 입력) 선택 |
| Thickness (mm) | 두께값 — Type이 `thickness`일 때만 활성화 |
| Unit Weight (kN/m³) | 재료 단위중량 |
| Load (kN/m²) | Type이 `thickness`이면 `Thickness × Unit Weight / 1000`으로 자동 계산, `load`이면 직접 입력 |

## 참고/제약사항

- LL(활하중) 기본값은 자동 계산되지 않고 통상 수동 입력한다.
- Export to PDF 클릭 시 카테고리 선택 팝업에서 출력 대상 카테고리를 지정해야 하며, 파일은
  `프로젝트명-YYYY-MM-DD.pdf` 형식으로 저장된다.
- 저장된 설정 파일은 `floor-load-settings-YYYY-MM-DD.pdf`(원문 표기 그대로)라는 이름으로
  다운로드되나, 실제로는 재사용을 위한 `.json` 설정 파일이다.

## 관련 JSON API 엔드포인트

Plug-in이 참조·기록하는 데이터는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/STLD` — Static Load Cases](../../manual/06_DB_Static_Loads.md) *(DL/LL Case 매핑 대상)*
- [`/db/FBLD` — Define Floor Load Type](../../manual/06_DB_Static_Loads.md#13-dbfbld--define-floor-load-type)
- [`/db/FBLA` — Assign Floor Loads](../../manual/06_DB_Static_Loads.md#14-dbfbla--assign-floor-loads)

## 결론 (원문)

이 Plug-in은 구조계산서용 하중표 작성과 제품 내 하중 입력을 단일 작업으로 통합 처리할 수 있도록
설계된 실무 중심 Plug-in이다.

## 원문 링크

[https://support.midasuser.com/hc/ko/articles/49475987573657-Floor-Load-Table-Generator](https://support.midasuser.com/hc/ko/articles/49475987573657-Floor-Load-Table-Generator)
