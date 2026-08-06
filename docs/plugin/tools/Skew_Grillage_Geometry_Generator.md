# Skew Grillage Geometry Generator

> **원문:** [Skew Grillage Geometry Generator](https://support.midasuser.com/hc/ko/articles/60848423734169-Skew-Grillage-Geometry-Generator)
> **원문 작성:** 2026-08-06 · **원문 최종 편집:** 2026-08-06

---

## 개요

경사(skew) 그릴리지(grillage)는 설명은 간단하지만 만들기는 번거롭다. 지지선이 데크 폭 방향으로
경간을 따라 어긋나고, 모든 종방향 거더는 각 횡부재 위치에서 분할되어야 하며, 단부 크로스빔은
모든 거더에 닿아야 하고, 절점·요소 번호는 전 과정에서 일관되게 유지되어야 한다. 이 시퀀스는
스큐각·경간·거더 수가 바뀔 때마다 반복해야 한다.

이 Plug-in은 이 과정을 파라메트릭 정의 하나로 만든다. 경간, 데크 폭, 거더 수, 횡방향 간격,
스큐각을 입력하면 절점·요소 수를 함께 보여주는 실시간 정투상(orthographic) 프리뷰로 전체
그릴리지를 확인할 수 있고, 확정 시 CIVIL NX 모델에 연결된 절점과 보 요소로 한 번에 기록된다.

## 지원 버전

`MIDAS CIVIL NX 2026 (v1.0.2)`

## 주요 기능

- **Parametric from end to end** — 스큐, 경간, 데크 폭, 거더 수, 횡방향 간격을 바꾸면 횡부재
  배치·단부 열·스큐 경계보를 포함한 전체 그릴리지가 즉시 재생성된다.
- **Seen before it is built** — 평면 뷰로 열리는 정투상 3D 프리뷰가 절점·요소 수, 거더 간격,
  전형 베이 간격, 지지단 오프셋을 입력값 변경과 동시에 실시간으로 표시해, 모델에 반영되기 전에
  오류를 잡을 수 있다.
- **Correct connectivity** — 모든 횡부재 교차점에서 종방향 거더를 분할해, 교차만 하고 접합되지
  않은 보가 아니라 실제로 구조적으로 연결된 그릴리지를 만든다. 선택한 간격이 경간을 정확히
  나누지 못하면 마지막 베이는 자동으로 축소된다.
- **Two cross-member conventions** — 횡부재를 스큐 지지선을 따르게 하거나 거더에 수직으로
  배치하는 두 방식을 지원한다. 수직 방식에서는 양쪽 지지점에서 모든 거더가 연결되도록 단부
  크로스빔이 자동 생성된다.
- **Tidied before committing** — 프리뷰의 임의 두 절점 간 실제 거리를 측정할 수 있고, 간격이
  너무 좁은 횡방향 열은 중복 절점을 삭제하고 거더를 재연결하는 방식으로 병합할 수 있다.
- **Safe on a live model** — 시작 절점·요소 ID의 충돌 여부를 확인하고, 기존 모델이 있으면
  교체 전에 경고하며, 누락된 재료·단면은 모델의 단위계 기준으로 자동 생성하고, 요소 기록에
  실패하면 새로 생성된 절점을 롤백한다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | CIVIL NX에서 새 모델을 열고 Plug-in 실행 — 연결 정보는 자동 제공되며, 상태 배지가 "CIVIL NX connected"가 아니면 **Connection** 사용 |
| 2 | 데크 지오메트리 입력 — 경간(모든 거더의 두 지지선 사이 거리), 데크 폭, 종방향 거더 수, 횡방향 간격 |
| 3 | 스큐각 설정 — 슬라이더 또는 직접 입력, 범위 **-60°~+60°**. `0°`는 거더에 수직, 양수 값은 `+Y` 지지단을 `+X` 방향으로 이동시킴 |
| 4 | 횡부재 방향 선택 — **Parallel to skew**(모든 횡부재가 지지선을 따름) / **Perpendicular to girders**(거더 공통 겹침 구간에 걸치고, 각 지지점에 단부 크로스빔 자동 추가) |
| 5 | Model origin 설정 — Origin X/Y/Z로 데크 중심선 시작점을 CIVIL NX 전역 좌표계에 배치(기본값 0, 순수 평행이동이라 지오메트리 지표는 변하지 않음) |
| 6 | Model assignment 설정 — 재료 ID, 종/횡방향 단면 ID, 첫 절점 ID, 첫 요소 ID 입력. **Create missing default properties**를 선택 유지하면 누락된 재료·단면이 모델의 현재 단위계로 자동 생성됨 |
| 7 | 프리뷰 확인 — 기본은 평면 뷰, **3D** 선택 또는 드래그로 회전, 스크롤로 확대/축소, **Reset view**로 평면 뷰 복귀. **Measure**로 임의 두 절점 간 3D 거리·좌표차 확인, **Merge beams**로 중복 횡방향 열 제거·거더 재연결 |
| 8 | Create Geometry — 추가될 절점·요소 요약을 검토 후 확정. 모델에 기존 절점·요소가 있으면 기존 개수를 보여주는 2차 경고가 표시됨 |
| 9 | (필요 시) Download API payload — 생성된 절점·요소 데이터를 JSON 파일로 저장해 검토·재사용 |

## 참고/제약사항

- 스큐각 입력 범위는 -60°~+60°로 제한된다.
- Model origin 변경은 순수 평행이동이므로 리포트되는 지오메트리 지표(거더 간격, 베이 간격 등)에
  영향을 주지 않는다.

## 관련 JSON API 엔드포인트

Plug-in이 생성하는 절점·보 요소·재료·단면은 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/NODE` — Node](../../manual/03_DB_Node_Element.md#1-dbnode)
- [`/db/ELEM` — Element](../../manual/03_DB_Node_Element.md#2-dbelem) *(보 요소)*
- [`/db/MATL` — Material Properties](../../manual/04_DB_Properties.md#1-dbmatl) *(누락 시 자동 생성)*
- [`/db/SECT` — Section Properties](../../manual/04_DB_Properties.md#12-dbsect) *(누락 시 자동 생성)*

## 결론 (원문)

이 Plug-in은 그릴리지 모델링에서 느리고 오류가 나기 쉬운 부분 — 스큐 오프셋을 수동으로
계산하고, 모든 횡부재마다 거더를 분할하고, 파라미터가 바뀔 때마다 모델 번호를 다시 매기는
작업 — 을 제거한다. 데크를 한 번 정의하고 프리뷰로 검증한 뒤, 스큐·경간·거더 배치가 바뀔 때마다
몇 초 만에 재생성할 수 있다. 엔지니어는 지오메트리 생성이 아니라 해석에 시간을 쓸 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/ko/articles/60848423734169-Skew-Grillage-Geometry-Generator](https://support.midasuser.com/hc/ko/articles/60848423734169-Skew-Grillage-Geometry-Generator)
