# Local Axis

> **원문:** [Local Axis](https://support.midasuser.com/hc/en-us/articles/45537498601881-Local-Axis)
> **원문 작성:** 2025-04-09 · **원문 최종 편집:** 2025-08-01

---

## 개요

Plug-in을 이용해 접선 방향 노드 로컬축(tangential Node Local Axis) 위치를 구한다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

구조물을 설계하려면 특정 좌표축을 기준으로 모델링·해석한다. 좌표축은 기본적으로 전역축
(Global Axis)을 쓰지만, 부재가 매개변수형(parametric) 형상을 가지면 로컬축(Local Axis)을
이용한 입력·결과값으로 하중·부재력을 확인한다.

기존 해석 프로그램에서는 전역축에서 로컬축으로 바꾸기 위해 두 축의 회전값을 구해 직접
적용해야 했다. 이 Plug-in은 로컬축 값을 선택한 모든 노드를 동시에 계산해, 회전된 값을 연산과
프로그램에 직접 입력한다.

- 수동 로컬축 연산을 자동화해 설계 시간 단축
- 반복 수정 작업으로 인한 사람 실수 감소
- 다양한 접선 계산 공식 선택지로 정확하고 효율적인 설계 지원

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | Cubic Spline의 Type 선택 |
| 2 | Local Axis를 적용할 노드 선택. **Import Node** 버튼으로 CIVIL NX 모델링에서 직접 선택해 가져와야 함 |
| 3 | Local Axis가 모델링에 적용됨 |
| 4 | 그래프로 Spline 형상을 실시간 확인 가능 |

Spline 버튼으로 Spline 간 차이를 시각적으로 확인할 수 있다.

## 참고/제약사항

- Import Node는 CIVIL NX 모델링에서 직접 선택으로 가져오며 반드시 **Import Node** 버튼을
  통해 실행해야 한다. Plug-in은 X-Y 평면에 대한 정보만 가져온다.
- Spline은 X축의 양(+)의 방향으로만 생성된다.
- Start Point와 End Point는 Cubic Spline의 시작·끝 각도를 계산하는 데 적용되며, Clamped
  Cubic Spline에서만 동작한다.

## 관련 JSON API 엔드포인트

Plug-in이 적용하는 노드 로컬축은 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/SKEW` — Node Local Axis](../../manual/03_DB_Node_Element.md)

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/45537498601881-Local-Axis](https://support.midasuser.com/hc/en-us/articles/45537498601881-Local-Axis)
