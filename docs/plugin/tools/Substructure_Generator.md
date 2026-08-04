# Substructure Generator

> **원문:** [Substructure Generator](https://support.midasuser.com/hc/en-us/articles/60317101122329-Substructure-Generator)
> **원문 작성:** 2026-07-22 · **원문 최종 편집:** 2026-07-27

---

## 개요

Civil NX에서 하부구조(Substructure) 모델을 매끄럽게 생성하고 상세 보고서를 만들도록 설계된
Plug-in이다. 형상 생성과 문서화를 모두 자동화해 엔지니어에게 고효율 워크플로를 제공한다.

## 지원 버전

`MIDAS CIVIL NX 2025 (v2.2)`

## 주요 기능

- **종합적인 모델 생성:** 경계조건까지 완전히 정의된, 즉시 해석 가능한 3D 하부구조 모델을
  자동 생성.
- **자동 문서화:** 모든 입력 요약, 계산된 하중, Midas Civil NX에서 동적으로 캡처한 스크린샷
  (BMD 다이어그램, 변위 컨투어, 단면 뷰 등)이 담긴 다운로드 가능한 `.xlsx` Excel 보고서 생성.
- **통합 하중·응답스펙트럼:** 정적·이동·풍·지진 하중을 절점하중으로 정확히 적용하고,
  응답스펙트럼 함수도 생성.
- **다양한 기초 옵션:** 직접기초(Open Foundation)와 말뚝기초(Pile Foundation) 입력 모두
  지원.

## 사용 방법 (9개 탭)

| 탭 | 설명 |
| --- | --- |
| Initial Data | 시작점 좌표와 교각 코핑(Pier Cap)·교각(Pier)·기초(Footing)의 재료 물성 설정 |
| Superstructure | 주로 Excel 보고서 생성과 풍하중 자동 계산에 쓰이는 유효경간 등 치수 수집 |
| Pier & Pier Cap | 물리적 치수, 형상(원형/사각형), 요소 메시 길이 정의 |
| Foundation | 직접기초 또는 말뚝기초 입력(치수, 깊이, 메시 크기, SBC·지반계수 등 지반 물성) |
| Bearing | 받침 배치(양쪽/중앙), 거리, 페데스탈 높이, 탄성링크 강성값 설정 |
| Loading | 받침 위치에 절점하중으로 적용되는 정적하중(자중, SIDL) 입력 |
| Moving Load | 절점하중으로 적용되는 이동하중 최대 반력(수직·종방향·횡방향) 입력 |
| Dynamic Load | 풍하중 파라미터와 지진하중 데이터(IS 1893 기준 응답스펙트럼) 정의 |
| Create Model | 최종 실행 탭 — Midas Civil NX 모델 생성 및 Excel 보고서 다운로드 |

**입력값 저장/재사용:** 어느 탭에서든 **Download (.json)** 버튼으로 현재 입력을 JSON 파일로
저장할 수 있다. 이 JSON은 모든 탭의 데이터를 포함하므로, 어느 탭에서 다운로드/업로드하든
전체 입력이 저장·복원된다. 저장한 JSON을 다시 쓰려면 **Upload**로 업로드한 뒤 **Apply**를
클릭하면 모든 저장값이 자동 복원된다.

## 참고/제약사항

데이터 입력 전, 보고서에 이미지가 올바르게 표시되도록 다음 설정을 적용해야 한다.

1. Civil NX에서 **Display Option**(Alt + E) 진입
2. **Draw** 탭에서 **"Hidden Option (Model)"** 열기
3. Thickness Option에서 **"Plane Thickness"** 활성화

## 관련 JSON API 엔드포인트

Plug-in이 생성한다고 명시한 응답스펙트럼 함수는 `docs/manual`의 다음 엔드포인트와
대응된다. 정적/이동/풍/지진 하중이 정확히 어느 `/db/*` 엔드포인트로 기록되는지는 원문에
명시되어 있지 않아 링크하지 않았다.

- [`/db/SPFC` — Response Spectrum Functions](../../manual/09_DB_Dynamic_Loads.md) *(응답스펙트럼 함수 한정)*

## 결론 (원문)

Sub Structure Generator로 상세한 3D 하부구조 모델을 빠르게 구축하는 동시에 종합적인
엔지니어링 보고서를 생성할 수 있다. 이 Plug-in은 수작업 모델링·문서화 시간을 크게 줄인다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/60317101122329-Substructure-Generator](https://support.midasuser.com/hc/en-us/articles/60317101122329-Substructure-Generator)
