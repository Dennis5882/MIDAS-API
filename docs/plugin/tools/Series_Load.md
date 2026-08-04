# Series Load

> **원문:** [Series Load](https://support.midasuser.com/hc/en-us/articles/45545604010521-Series-Load)
> **원문 작성:** 2025-04-09 · **원문 최종 편집:** 2025-08-01

---

## 개요

Series Load Plug-in은 MIDAS CIVIL NX의 연속 구조물에 일정 간격으로 커스텀 정적 보하중
(집중하중, 분포하중, 원심하중)을 적용하는 것을 자동화한다. 교량이나 원형 구조물처럼 곡선
또는 스플라인 정렬된 요소에 반복 하중을 정의하는 과정을 단순화한다.

### 주요 특징(원문)

- 정적하중조합을 활주하중(live load)으로 적용.
- 노드 스플라인 형상에 기반한 방향성을 가진 원심력(centrifugal force) 지원.
- i-node부터 시작하는 연속 구조물과 호환.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

- **효율성:** 긴 경간에 걸친 반복 하중의 수동 입력을 없앤다.
- **정밀성:** 스플라인 접선에 수직인 원심력 방향을 자동 계산한다.
- **유연성:** 집중하중, 분포하중, 원심하중과 함께 동작한다.
- **고급 스플라인 옵션:** 매끄러운 하중 정렬을 위해 Monotone Cubic Hermite Spline(권장)을
  사용한다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| Vertical Loads 입력 | 보에 작용하는 집중하중 |
| Distributed Loads 입력 | 보에 작용하는 분포하중 |
| Impact Loads 입력 | 수직하중에 대한 충격계수(magnification factor) |
| Centrifugal Loads 입력 | 수직하중과 함께 적용 |
| Beam Geometry 선택 | — |
| 공통 설정 선택·입력 | 사전 설정 하중을 선택하고 각 케이스 간 거리로 정적하중케이스 개수 결정 |
| Load Points Setting 입력 | 하중점 설정(집중하중 간 거리) |
| 제어판 입력·선택 | 정적하중 생성 옵션 확인 |
| 적용 | 위 입력을 모두 마친 뒤 적용할 요소를 선택하고 **APPLY SERIES LOADS** 클릭 |
| 확인 | 생성된 정적하중케이스 확인 |

## 참고/제약사항

- **연속 구조물 전용:** 끊어진(disjointed) 요소에는 하중을 적용할 수 없다.
- **스플라인 의존성:** 원심력 방향은 연결된 노드 스플라인의 접선에서 도출된다.
- **입력 검증:** 모든 하중의 크기는 0보다 커야 한다.

## 관련 JSON API 엔드포인트

Plug-in이 생성하는 하중은 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/STLD` — Static Load Cases](../../manual/06_DB_Static_Loads.md)
- [`/db/BMLD` — Beam Loads](../../manual/06_DB_Static_Loads.md)

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/45545604010521-Series-Load](https://support.midasuser.com/hc/en-us/articles/45545604010521-Series-Load)
