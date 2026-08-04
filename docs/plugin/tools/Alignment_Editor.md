# Alignment Editor

> **원문:** [Alignment Editor](https://support.midasuser.com/hc/en-us/articles/60307252076441-Alignment-Editor)
> **원문 작성:** 2026-07-22 · **원문 최종 편집:** 2026-07-22

---

## 개요

Alignment Editor Plug-in은 교량 모델의 선형(alignment)을 수정한다. 초기 기준 선형에서 새로운
목표 선형으로 노드 형상을 변환하고, 수직 요소의 베타각(beta angle)을 자동으로 갱신한다.

## 지원 버전

`MIDAS CIVIL NX 2026 (v1.1)`

## 주요 기능

- **선형 인지 변환(Alignment Aware Transformation)** — 모든 노드의 상대 거리·직각 오프셋·표고를
  정확히 새 선형으로 옮겨 모델을 자동 재매핑한다.
- **시간 절약** — 수동 노드 재배치가 필요 없어, 수 시간 걸리던 작업을 클릭 한 번으로 줄인다.
- **오류 감소** — 수동 좌표 편집을 없애 기하·데이터 처리 오류를 크게 줄인다.
- **유연한 보간(Flexible Interpolation)** — 선형 기하 의도에 맞춰 여러 보간 옵션을 제공한다.
- **방향 자동 갱신** — 새 선형을 따라 로컬축이 일관되게 유지되도록 수직 요소의 베타각을 갱신한다.

## 사용 방법

| 필드 | 설명 | 옵션·기본값 |
| --- | --- | --- |
| Initial Points | 초기 선형을 정의하는 테이블. ① **Import Coordinates**를 클릭해 현재 MIDAS CIVIL NX 모델에서 선택된 노드의 좌표를 자동 추출하거나, ② X/Y/Z를 직접 입력·수정 | — |
| Final Points | 목표 선형을 정의하는 테이블. X/Y/Z 좌표를 직접 입력 | — |
| Interpolation Method | 포인트 사이 선형 곡선을 생성할 보간법 선택 | `Cubic` / `Akima` / `Makima` / `PCHIP` |
| Update Alignment | 변환을 적용. 성공 시 "Alignment modified" 확인 메시지 표시 | — |

## 참고/제약사항

- **보간법 선택:** 보간법에 따라 곡선이 제어점을 지나는 방식이 달라진다.
  - `Cubic`은 매끄러운 곡선을 만들지만 급격한 변화 구간 근처에서 오버슈트·언더슈트가 발생할 수
    있다.
  - `Akima`, `Makima`는 오버슈트를 줄인다.
  - `PCHIP`(Piecewise Cubic Hermite Interpolating Polynomial)은 곡선이 인접 포인트 범위를
    벗어나지 않도록 보장한다.
- **선형 포인트 요구사항:** Initial Points·Final Points 테이블 모두 최소 2행 이상이어야 하며,
  X좌표는 오름차순이어야 한다.
- **끝점 처리(End point Behaviour):** 초기 선형의 X 범위를 벗어난 위치의 노드는 가장 가까운
  선형 끝점을 기준으로 강체 회전(rigid rotation) 방식으로 매핑된다.
- **참고 링크(원문 제공):** `scipy.interpolate.CubicSpline`, `scipy.interpolate.Akima1DInterpolator`,
  `scipy.interpolate.PchipInterpolator`

## 결론 (원문)

Alignment Editor는 기하학적 관계를 유지하면서 교량 모델을 갱신된 선형으로 재정렬한다. 노드
좌표와 요소 방향을 자동으로 갱신해, MIDAS Civil NX 안에서 완결된 선형 수정 워크플로를 제공한다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/60307252076441-Alignment-Editor](https://support.midasuser.com/hc/en-us/articles/60307252076441-Alignment-Editor)
