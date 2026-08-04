# Inertial Forces Controller

> **원문:** [Inertial Forces Controller](https://support.midasuser.com/hc/en-us/articles/40706127836953-Inertial-Forces-Controller)
> **원문 작성:** 2024-12-03 · **원문 최종 편집:** 2025-08-01

---

## 개요

곡선교 교각에 작용하는 관성력(inertial force)의 방향을 자동으로 변환하는 Plug-in이다.
곡선교에 관성력을 적용할 때 교각마다 하중 방향을 수동으로 계산·입력할 필요가 없다. 전역
좌표계 또는 사용자 지정 각도를 기준으로, 각 교각의 가장 가까운 방향으로 수평 관성력을
변환·적용한다. 교각과 전역 좌표계가 어긋나는 복잡한 교량 형상 모델링에 특히 유용해 지진
해석 워크플로를 단순화한다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

MIDAS CIVIL에서 곡선교 교각에 관성력을 적용하려면 전통적으로 교각마다 하중 방향을 수동으로
계산·입력해야 했고, 이는 시간이 오래 걸리고 오류가 발생하기 쉬웠다. 이 Plug-in은 회전각을
하나 또는 여러 개 입력하면 해당하는 하중케이스를 자동으로 생성한다. 수동 변환이나 반복 입력
없이 과정을 단순화해 시간을 절약하고 정확성을 보장한다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| Time History Load Cases 선택 | 해석 방법(Analysis Method)이 "Static"으로 설정된 시간이력 하중케이스 목록이 표시됨 |
| Static Load 선택 | "Nodal Body Force"와 "Nodal Loads"가 할당된 케이스만 표시됨 |
| Time History Functions 선택 | 제품 설정에서 Time Forcing Functions Data가 "Normal" 타입으로 구성된 함수가 표시됨. 기본값으로 "Linear" 함수도 제공(Preset: Linear) |
| Scale Factor(④) 입력 | 시간하중함수의 배율(scale factor) 입력 |
| 수평하중 각도(⑥) 입력 | 전역좌표계 Z축에 대한 X축 회전각으로, 지반가속도 수평성분 방향에 정렬됨. 양의 실수 입력 가능하며 "+" 버튼(⑤)으로 여러 회전각 정의 가능 |
| Create(⑦) | 클릭 시 절점체적력(nodal body force)이 추가된 정적하중케이스, 시간이력 하중케이스, 시간하중함수, 시간변동 정적하중이 새로 생성됨 |

> ⚠️ **주의(원문):** Scale Factor(④)는 0보다 커야 한다. 각도(⑥)는 서로 같은 크기로 정의할
> 수 없다.

추가되는 nodal body force는 "Static Load 이름_각도deg"(각도는 도(degree) 단위, "Static
Load" 설정 기준) 형태로 생성된다. 기존에 입력된 nodal body force 하중은 하중 각도에 따라
좌표 변환된다.

## 참고/제약사항

좌표 변환 계산(Coordinate-transformation Calculation) 예시: 30도 방향으로 생성하면, 원래
정적하중으로부터 좌표 변환된 정적하중케이스가 자동으로 생성된다.

## 관련 JSON API 엔드포인트

Plug-in이 생성한다고 명시한 데이터는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/STLD` — Static Load Cases](../../manual/06_DB_Static_Loads.md)
- [`/db/NBOF` — Nodal Body Force](../../manual/06_DB_Static_Loads.md)
- [`/db/THIS` — Time History Load Cases](../../manual/09_DB_Dynamic_Loads.md)
- [`/db/THFC` — Time History Functions](../../manual/09_DB_Dynamic_Loads.md)
- [`/db/THSL` — Time Varying Static Loads](../../manual/09_DB_Dynamic_Loads.md)

## 결론 (원문)

Inertial Forces Controller Plug-in은 브레이스 개수를 기준으로 적용해야 할 관성력의 하중
방향을 자동으로 변환해, 사용자의 시간을 절약하고 잠재적인 사람 실수를 없앤다. 사용자는
전역좌표계 Z축을 기준으로 한 수평 방향만 입력하면 관성력을 손쉽게 제어할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/40706127836953-Inertial-Forces-Controller](https://support.midasuser.com/hc/en-us/articles/40706127836953-Inertial-Forces-Controller)
