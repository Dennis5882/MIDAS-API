# [MS 1553:2002] Building Wind Loads Generator

> **원문:** [\[MS 1553:2002\] Building Wind Loads Generator](https://support.midasuser.com/hc/en-us/articles/47130265330841--MS-1553-2002-Building-Wind-Loads-Generator)
> **원문 작성:** 2025-05-20 · **원문 최종 편집:** 2025-08-05

---

## 개요

말레이시아 건축구조물 대상 **MS 1553:2002** 기준에 따라 정적 풍하중 계산을 자동화하는
Plug-in이다. 풍하중 설계 파라미터를 입력하면 높이별 풍압·풍력 분포를 즉시 시각화해 풍하중
평가 과정을 단순화한다.

## 지원 버전

- `MIDAS GEN NX 2024 (v1.1) US`
- 적용 기준: MS 1553:2002 (Code of Practice on Wind Loading for Building Structures)

## 주요 기능

- **기준 준수:** MS 1553:2002를 완전히 준수해 말레이시아 소재 구조물의 일관되고 신뢰성 있는
  풍하중 계산을 지원.
- **시각적 검증:** 방향별 층력(Story Force)·층전단(Story Shear)·전도모멘트(Overturning
  Moment)를 자동 생성 막대그래프로 표시해 결과를 확인.
- **상호작용형 워크플로:** 설계 파라미터 조정 시 그래프·계산이 즉시 갱신되어 수동 재계산을
  최소화하고 설계 반복 속도를 높임.
- **계산서 내보내기·연동:** 구조 모델에 하중을 직접 적용하거나, 문서화·다른 도구 연동을 위해
  Excel로 결과를 내보낼 수 있음.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 좌측: 풍하중 설계 파라미터 입력 | 구조 모델의 풍하중 설계 파라미터 입력 |
| 우측: 결과 시각화 | Story Force·Story Shear·Overturning Moment를 X·Y 두 방향 그래프·표로 즉시 표시 |
| X-Dir / Y-Dir 탭 | 전역좌표계 X방향·Y방향에 작용하는 풍하중 파라미터를 각 탭에서 입력 |
| Apply(주 대화상자 우측) | 방향별로 풍하중을 적용할 정적하중케이스(Static Load Case) 선택 |
| Apply(최종) | 계산된 하중을 구조 모델에 적용 |

## 풍하중 설계 파라미터 (원문 조항 대응)

| 기호 | 명칭 | 근거 조항 | 비고 |
| --- | --- | --- | --- |
| V_s | Basic Wind Speed | Figure 3.1 / Fundamental Basic Wind Velocity Map | 재현기간 50년 기준, Zone I 33.5 m/s, Zone II 32.5 m/s 권장값 |
| M_d | Climate change multiplier | — | 값은 1.0 |
| M_z,cat | Terrain/Height Multiplier | Section 4.2, Clause 4.2.3 | 지형 거칠기·높이 반영, 상류 지형이 여럿이면 평균화 허용 |
| M_s | Shielding Multiplier | Section 4.3, Table 4.3 | Shielding 효과를 무시하거나 특정 방향에 미적용, 또는 평균 상향 경사가 0.2 초과 시 1.0 |
| M_h | Hill Shape Multiplier | Section 4.4, Figures 4.3–4.4 | 특정 지역 지형대(local topographic zone)의 특정 방위를 제외하면 1.0 |
| V_des | Building design wind speed | Table 3.2 | 최대 site wind speed(V_sit)에 중요도계수(I) 곱 |
| C_fig | Aerodynamic shape factor | Section 5.2(a) | — |
| C_pe | External pressure coefficient | Table 5.2(a)(풍상벽)/5.2(b)(풍하벽) | h/d 비에 따라 결정 |
| K_a | Area reduction factor | Clause 5.4.2, Table 5.4 | 밀폐형 건물 지붕·벽 적용, 그 외는 기본 1.0 |
| K_c | Combination factor(외압) | Clause 5.4.3 | 여러 면의 압력이 함께 작용할 때 1.0 미만 계수 적용 가능 |
| K_l | Local pressure factor(클래딩) | Clause 5.4.4 | 기본 1.0, 국부 클래딩압 적용 시 예외 |
| K_p | Porous cladding reduction factor | Clause 5.4.5, Table 5.8 | 일반적으로 1.0, 투과성 클래딩 시 Table 5.8 참고 |
| C_dyn | Dynamic response factor | Section 6 | 1차 고유진동수 > 1Hz면 1.0. 0.2~1.0Hz는 Clause 6.2(along-wind)/6.3(cross-wind) 적용 |
| 건물 평면 치수 (b × d) | — | — | 형상계수·풍하중 노출 면적 산정에 사용 |
| Importance Factor / Wind Direction | — | Table 3.2 | 구조물 분류에 따라 0.87, 1.0, 1.15, 1.15 중 선택. 주 풍향이 축·하중 배정을 결정 |

건물 설계 풍압(Pa)은 `p = 0.5·p_air × V_des² × C_fig × C_dyn` 형태의 식으로 계산된다(원문
수식 이미지 참고, p_air = 공기밀도 1.225 kg/m³, `0.5·p_air` = 0.613).

> ⚠️ 원문 파라미터 번호 ③과 ④가 모두 "M_z,cat: Terrain/Height Multiplier"로 동일하게
> 중복 기재되어 있다 — 원문 자체의 번호 매김 오류로 보이며, 이 문서에는 한 항목으로만
> 정리했다.

## 참고/제약사항

- 이 Plug-in은 **유연한 고층 건물(flexible tall building)을 지원하지 않는다.** 해당하는
  경우 사용자가 Equation (10) 또는 (19)로 C_dyn을 직접 계산해야 한다.

## 관련 JSON API 엔드포인트

Plug-in이 계산 결과를 "구조 모델에 직접 적용"한다고 설명하는 부분은, 성격상 `docs/manual`의
정적 풍하중 엔드포인트와 연동될 가능성이 높다. 다만 해당 엔드포인트 문서는 KDS 41-12:2022 /
User Type 기준으로 기술되어 있어 MS 1553:2002 코드와의 정확한 필드 대응은 확인되지 않았다 —
참고용으로만 링크한다.

- [`/db/SWIND` — Static Wind Load](../../manual/06_DB_Static_Loads.md) *(코드별 필드 대응 미확인)*

## 결론 (원문)

이 Plug-in은 MS 1553:2002 기반 정적 풍하중 생성을 위한 빠르고 직관적인 솔루션을 제공한다.
기본 풍속, 지형 범주, shielding, 건물 높이 등 핵심 풍하중 설계 파라미터를 안내해 풍하중
결정의 명확성과 일관성을 높인다. 실시간 시각화와 내보내기 기능으로 엔지니어는 부지·건물
특성이 풍하중에 미치는 영향을 빠르게 평가할 수 있다. 단순화된 워크플로는 수동 입력을
최소화하고 표준화되고 재현 가능한 풍하중 설계 결과를 촉진한다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/47130265330841--MS-1553-2002-Building-Wind-Loads-Generator](https://support.midasuser.com/hc/en-us/articles/47130265330841--MS-1553-2002-Building-Wind-Loads-Generator)
