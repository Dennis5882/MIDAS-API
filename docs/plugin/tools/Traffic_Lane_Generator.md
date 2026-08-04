# Traffic Lane Generator

> **원문:** [Traffic Lane Generator](https://support.midasuser.com/hc/en-us/articles/60315550956825-Traffic-Lane-Generator)
> **원문 작성:** 2026-07-22 · **원문 최종 편집:** 2026-07-23

---

## 개요

Traffic Lane Generator는 클릭 한 번으로 여러 개의 차선(traffic lane)을 생성할 수 있게
해주는 Plug-in이다.

## 지원 버전

`MIDAS CIVIL NX 2025 (v2.2)`

## 주요 기능

- **효율성:** 클릭 한 번으로 여러 차선을 생성해, 전통적으로 반복적이던 과정을 자동화한다.
- **폭넓은 호환성:** 현재 15개 이동하중 코드(moving load code)를 지원한다.
- **직관적인 인터페이스:** Plug-in 입력이 Civil NX 사용자 인터페이스와 동일해 기존
  사용자의 학습 곡선을 줄인다.
- **즉시 적용:** 여러 차선을 동시에 생성해 Civil NX 모델 내 선택한 요소에 자동 적용한다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | Civil NX에서 차선을 적용할 기준 요소 직접 선택 |
| 2 | 드롭다운 메뉴에서 적용할 이동하중 코드 선택 |
| 3 | 좌측 패널에서 윤간거리(wheel spacing), 차선 폭, 경간장, 충격계수, 차량하중 분배 등 일반 차선 파라미터 정의 |
| 4 | 우측 Lane Configuration 섹션 표에서 차선을 추가·삭제하고 각 차선(L1, L2, L3 등)의 편심(eccentricity) 지정 |
| 5 | 창 우측 하단 **"Generate Traffic Lanes"** 버튼을 클릭해 생성 실행 |

## 결론 (원문)

Traffic Lane Generator는 Civil NX에서 차선 정의 과정을 단순화한다. API 연동을 활용해
정확성을 보장하면서 수동 반복 작업을 없애, 엔지니어가 핵심 해석·설계 작업에 더 많은 시간을
쏟을 수 있게 한다.

## 관련 JSON API 엔드포인트

Plug-in이 생성하는 차선은 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/LLAN` — Traffic Line Lanes](../../manual/08_DB_Moving_Loads.md)

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/60315550956825-Traffic-Lane-Generator](https://support.midasuser.com/hc/en-us/articles/60315550956825-Traffic-Lane-Generator)
