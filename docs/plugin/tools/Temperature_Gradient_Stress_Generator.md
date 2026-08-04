# Temperature Gradient Stress Generator

> **원문:** [Temperature Gradient Stress Generator](https://support.midasuser.com/hc/en-us/articles/40708129121817-Temperature-Gradient-Stress-Generator)
> **원문 작성:** 2024-12-03 · **원문 최종 편집:** 2025-08-01

---

## 개요

**AASHTO-LRFD** 기준으로 PSC·콘크리트·강합성 단면의 온도 구배(temperature gradient)를
고려한 자기평형응력(Self-Equilibrating Stress)을 계산하는 Plug-in이다. 교량 단면에 온도
구배를 적용할 때 열 영향에 의한 응력을 수동으로 계산·입력할 필요가 없다. 자기평형응력값을
응력 요약표에 바로 제공하며, 비대칭·합성 단면을 포함한 복잡한 교량 형상 모델링에 특히
유용해 온도 유발 응력의 해석·설계 과정을 단순화한다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

PSC·콘크리트·강합성 단면에 대한 온도 구배 영향을 분석하려면 전통적으로 자기평형응력을 수동
계산해야 했고, 시간이 오래 걸리고 오류가 발생하기 쉬웠다. 이 Plug-in은 이 과정을 자동화해
자기평형응력을 계산하고 응력 요약표에 바로 표시한다. 반복적인 수동 입력이나 별도 계산 없이
워크플로를 단순화하고 시간을 절약하며 정확성을 보장한다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | **Import Section**을 클릭하고 온도 구배를 적용할 단면 선택(Civil 파일에서 가져옴) |
| 2 | 단면 선택 후 Civil 파일 기준으로 Temperature zone, girder surface, girder materials 옵션을 선택하고, 단면 하단에 표시된 T3 옵션 적용을 선택 |
| 3 | 선택한 재료·옵션에 따라 계산값이 표(⑤)에 표시됨. 자기평형응력도 여기서 확인 가능. 옵션에 따라 온도 구배(⑥)와 자기평형응력(⑦)이 실시간으로 변경됨 |
| 4 | 요소에 온도하중 추가 — Heating load(①), Cooling load(②) 추가(한 하중케이스를 선택하면 하나만 선택 가능) |
| 5 | 적용할 요소를 선택하면 온도하중이 추가된 것을 확인 가능 |

## 참고/제약사항 — 기존 기능과의 차이

Civil 사용자 대부분은 단면 특성에 따라 온도 구배를 적용하는 기존 기능(`Load > Temperature >
Temperature Loads > Temp. Gradient & Beam Section Temp.`)을 이미 알고 있다.

- **기존 방식:** PSC 보에 온도 구배를 적용하려면 단면 온도를 추가해야 한다. 깊이, 온도 변화
  위치, 온도 변동을 추가하고 요소를 선택해 하중을 사용해야 한다. 적용된 하중은 응력값을
  보여주지 않는다.
- **Plug-in 방식:** 가장 큰 차이는 Plug-in이 응력 요약표에 자기평형응력을 보여준다는 점이다.
  우측에서 비선형 온도 구배 그래프와 자기평형응력 차트를 확인할 수 있다.

> ⚠️ 원문의 "Conclusion" 문단은 "Inertial Forces Controller" 아티클의 결론(관성력 방향 자동
> 변환 관련 내용)이 그대로 복사되어 있어, 이 아티클(온도 구배 응력)과 무관한 원문 자기모순이다.
> 이 문서에는 옮기지 않았다.

## 관련 JSON API 엔드포인트

Plug-in이 다루는 보 단면 온도는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/BTMP` — Beam Section Temperature](../../manual/07_DB_Temperature_Prestress.md)

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/40708129121817-Temperature-Gradient-Stress-Generator](https://support.midasuser.com/hc/en-us/articles/40708129121817-Temperature-Gradient-Stress-Generator)
