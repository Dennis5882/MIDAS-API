# Load Effect for Load Combination

> **원문:** [Load Effect for LC](https://support.midasuser.com/hc/en-us/articles/35649669387289-Load-Effect-for-Load-Combination)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

지정한 하중조합(Load Combination)에 포함된 각 하중케이스(Load Case)의 보 력(Beam force)
값을 추출해, 하중조합에 대한 각 하중케이스의 기여도를 부재력 관점에서 쉽게 파악할 수 있게
해주는 Plug-in이다. 각 하중케이스가 결과에 미치는 영향을 빠르고 정확하게 분석할 수 있다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

제품에 자주 들어오던 문의:

- 결과가 단순히 Excel 스타일 표로만 출력됨.
- 예상치 못한 결과가 나오면 사용자가 하중 설정을 수동으로 확인해야 함.

이 Plug-in은 각 입력값을 관리하고, 필터링 시스템으로 잘못된 값을 추적하며, 결과 탭에서
빠르게 분석할 수 있게 해준다. 전 세계 고객이 원하는 기능으로 꼽혔으며, 오류 발생 시 문제를
쉽게 식별할 수 있게 해준다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 하중조합 목록 확인 | 1. Plug-in을 실행하고 하중조합 목록에서 원하는 일반 하중조합 선택. 2. 선택한 하중조합을 확인하고 **Select** 클릭 |
| 하중조합 확인 | 3. 모델 뷰에서 검토할 요소 선택. 4. Plug-in에서 **Import** 버튼을 눌러 선택한 요소 저장. 5. 출력할 보 력 결과의 Position, Unit, Style 설정 |
| 하중케이스 목록 확인 | 6. **Create Force** 클릭 시 해당 하중조합의 Beam force 데이터가 우측 "Force Table"에 출력됨. 이동하중케이스가 포함된 경우 최대·최소값 케이스가 동시에 표시될 수 있음 |
| 결과 검증 | 7. Force Table 출력 후, 예를 들어 gLBC4(min)의 값을 선택해 부재력을 구성하는 load effect 확인. 8. 선택 시 해당 하중조합을 구성하는 하중케이스들과 각각의 Unfactored Value, Factor, Factored Value가 출력됨. 9. 가장 불리한 값은 **빨간색**, 영향이 가장 적은 값은 **파란색**으로 시각화됨. Sort by Absolute 또는 Sort by Max/Min을 선택하면 그 기준으로 정렬됨 |

## 관련 JSON API 엔드포인트

Plug-in이 다루는 하중조합·부재력 결과는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/LCOM-GEN` — Load Combinations (General)](../../manual/13_DB_Load_Combinations.md)
- [`POST 8. Beam Force`](../../manual/19_POST_AnalysisResult_1.md)

## 결론 (원문)

이 가이드를 통해 최종 결과에 기여하는 중간값을 명확히 이해하고, Load Effect Analysis
Plug-in으로 각 하중케이스의 기여도를 효율적으로 분석할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35649669387289-Load-Effect-for-Load-Combination](https://support.midasuser.com/hc/en-us/articles/35649669387289-Load-Effect-for-Load-Combination)
