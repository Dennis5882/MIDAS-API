# Stiffness Auto Tuner

> **원문:** [Stiffness Auto Tuner](https://support.midasuser.com/hc/en-us/articles/58178248491161-Stiffness-Auto-Tuner)
> **원문 작성:** 2026-05-22 · **원문 최종 편집:** 2026-08-13

---

## 개요

Beam/Wall Stiffness Auto Tuner는 선택한 보 요소의 Element Stiffness Factor와 벽체 요소의
Wall Stiffness Factor 자동 조정을 지원하는 Plug-in이다. 사용자가 정의한 조건을 기준으로
해석과 설계 검토를 반복 수행하고, 부재 검토비(check ratio)가 사용자가 설정한 목표비를
만족하는지 확인한 뒤, 정의된 강성 저감 순서에 따라 Stiffness Factor를 갱신한다. 보·벽체의
Stiffness Factor를 수정하고 해석을 재실행하는 반복적인 수작업을 줄여준다. 최종 적용된 강성
조건은 MIDAS 모델에서 바로 확인할 수 있다.

## 지원 버전

- `MIDAS GEN NX 2026 v2.2`
- 적용 기준: KDS 41 20 2022 RC — Beam check는 Beam Check 결과 사용, Wall check는 Wall
  Design 결과 사용

## 주요 기능

- **보·벽체 일괄 적용:** 보(Beam)와 벽체(Wall)를 한 번에 대상으로 설정하여, 각 부재의
  Stiffness Factor 조정 및 반복 해석을 일괄 수행 가능(2026-08-13 원문 개정으로 추가).
- **자동 반복(Automatic iteration):** 해석 수행, 설계 결과 조회, 사용자가 설정한 목표비
  기준 Stiffness Factor 갱신을 반복 수행.
- **모델 기반 요소 선택:** MIDAS GEN NX에서 선택한 대상 부재를 Plug-in과 바로 동기화.
- **Stiffness Factor 순서 제어:** 강성 저감 간격을 설정하고, 반복 해석에 쓸 강성 저감 순서를
  값 추가/삭제로 직접 구성 가능.
- **자동 그룹 생성:** 보 요소의 경우 최종 해석이 끝나면 강성 기준으로 Element Group이 자동
  생성됨(예: `AutoTuner_Beam [0.80] [Node=0; Element=4]`).

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | Plug-in을 실행하고 상위 탭에서 보 또는 벽체에 대한 조건을 입력(2026-08-13 원문 개정 — 이전에는 **Beam Stiffness Tuner**/**Wall Stiffness Tuner**를 별도 Plug-in으로 선택했으나, 하나의 화면에서 탭으로 전환하는 방식으로 변경됨) |
| 2 | MIDAS 모델에서 대상 부재를 선택하고 **Sync from product** 클릭. 보 강성 조정은 선택된 보 요소를, 벽체 강성 조정은 선택된 벽체 요소를 Wall ID·층 정보 기준으로 가져옴 |
| 3 | 필요 시 특정 Section 또는 Wall ID에 할당된 부재를 일괄 선택 가능 |
| 4 | (옵션) 보에 이미 적용된 Section Stiffness Factor를 함께 고려할지 설정. 활성화하면 Element Stiffness Factor뿐 아니라 기존 Section Stiffness Factor도 고려해 더 작은 값을 기준으로 해석·설계 수행 |
| 5 | **Decrement Stiffness Step Value** 설정. 지정한 간격에 따라 100%부터 낮은 값까지 강성 저감 순서를 생성해 **Stiffness decrement sequence**에 표시 |
| 6 | **Value to insert**에 값을 입력하면 Stiffness decrement sequence에 추가됨. **Value to delete**로 시퀀스에서 값 삭제 가능 |
| 7 | **Iteration Number**와 **Target Ratio** 입력. Target Ratio는 추가 강성 저감이 필요한지 판단하는 설계비 기준값 |
| 8 | **Analysis scope**에서 보와 벽체를 모두 실행 단계에 포함할지, 개별로 실행할지 설정(2026-08-13 원문 개정으로 추가) |
| 9 | 최종 결과 대화상자 검토 — 목표비를 여전히 초과하는 부재, 최소 강성 한계에 도달한 부재, 선택 요소에 적용된 최종 강성값을 요약해 보여줌 |
| 10 | 최종 반복이 끝나면 MIDAS 모델에 강성 그룹이 자동 생성되고, 선택된 요소가 최종 강성비 기준으로 해당 그룹에 할당됨 |
| Back | 메인 페이지로 이동 |
| Refresh | 모델을 새로 열었거나 모델 정보가 변경됐을 때 최신 정보로 Plug-in 갱신 |

## 결론 (원문)

이 Plug-in은 반복 해석·설계 검토 결과를 바탕으로 보·벽체 강성계수를 자동 조정하는 워크플로를
제공한다. 부재 선택, 강성 저감 순서 설정, 목표비 입력, 자동 그룹 할당을 하나의 워크플로로
연결해 강성 조정에 필요한 반복 수작업을 줄인다. 사용자는 생성된 강성값을 설계 검토 과정의
일부로 활용하고, 최종 모델 거동이 프로젝트 요구사항을 만족하는지 검증해야 한다.

## 관련 JSON API 엔드포인트

Plug-in이 조정한다고 명시한 보 요소 강성계수는 `docs/manual`의 다음 엔드포인트와 대응된다.
벽체 강성계수(Wall Stiffness Factor)가 어느 엔드포인트에 대응하는지는 원문에 명시되어 있지
않아 링크하지 않았다.

- [`/db/ESSF` — Element Stiffness Scale Factor](../../manual/04_DB_Properties.md) *(보 요소 한정, 벽체 대응 미확인)*

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/58178248491161-Stiffness-Auto-Tuner](https://support.midasuser.com/hc/en-us/articles/58178248491161-Stiffness-Auto-Tuner)
