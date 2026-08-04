# [AS/NZS 1170.2:2021] Building Wind Loads Generator

> **원문:** [\[AS/NZS 1170.2:2021\] Building Wind Load Generator](https://support.midasuser.com/hc/en-us/articles/46935970426905--AS-1170-2-2021-Building-Wind-Loads-Generator)
> **원문 작성:** 2025-05-15 · **원문 최종 편집:** 2026-02-24

---

## 개요

**AS/NZS 1170.2:2021** 기준에 따라 밀폐형(enclosed) 건물의 정적 풍하중 계산을 자동화하는
Plug-in이다. 풍하중 설계 파라미터를 입력하면 높이별 풍압·풍력 분포를 즉시 시각화해 풍하중
설계 과정을 단순화한다.

> ⚠️ AS/NZS 1170.2:2021은 호주·뉴질랜드 공동 기준이지만, 이 Plug-in은 현재 **호주(AS)
> 조항만** 구현한다(원문 명시).

## 지원 버전

- `MIDAS GEN NX 2026 (v1.1) US`
- 적용 기준: AS/NZS 1170.2:2021 (Structural design actions, Part 2: Wind actions)

## 주요 기능

- **기준 준수:** 최신 AS/NZS 1170.2:2021 기준(밀폐형 건물)을 따라 최신 하중 평가를 지원.
- **시각적 검증:** 방향별 층력(Story Force)·층전단(Story Shear)·전도모멘트(Overturning
  Moment) 분포를 라인 차트로 표시해 결과를 즉시 확인·해석 가능.
- **상호작용형 워크플로:** 파라미터 변경 시 그래프가 즉시 갱신되어 반복 작업 시간을 줄이고
  모델링 효율을 높임.
- **계산서 내보내기·연동:** 계산된 정적 풍하중을 구조 모델에 직접 적용하거나, 문서화·추가
  활용을 위해 Excel 계산서로 내보낼 수 있음.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 풍하중 설계 파라미터 입력 | 기본적으로 8방위(cardinal direction) 각각에 대해 개별 입력 가능. `Mz,cat`, `Ms`, `Mt`를 방향별로 직접 지정 가능 |
| Wind Load Input Condition → Input Only Worst-Case Value | 모든 방향에 단일 풍하중 파라미터 세트를 적용하려면 선택. 하나의 지배적(governing) 값 세트를 전 방향에 사용 |
| Calculate Wind Load | 클릭 시 계산 수행. Story Force·Story Shear·Overturning Moment를 그래프·표로 즉시 시각화(0°, 90°, 180°, 270° 각 방향별 확인 가능) |
| Apply | 계산된 하중을 구조 모델에 적용. 구조물 방향에 따라 +X, +Y, -X, -Y 방향으로 적용되며, 토글 버튼으로 양(+) 방향(+X, +Y)에만 적용하도록 제한 가능 |

## 풍하중 설계 파라미터 (원문 조항 대응)

| 기호 | 명칭 | 근거 조항 | 비고 |
| --- | --- | --- | --- |
| V_R | Regional Wind Speed(지역 풍속, m/s) | Section 3 | 호주는 Table 3.1(A) 또는 Fundamental Basic Wind Velocity Map 참고 |
| M_c | Climate change multiplier | Table 3.3 | 지역에 따라 보통 1.0 또는 1.05 |
| M_d | Wind Direction Multiplier | Section 3, Table 3.2(A) | 호주 기준 0.75~1.00 범위, 방위에 따라 다름 |
| M_z,cat | Terrain/Height Multiplier | Section 4.2 | 지형 거칠기·높이 반영. Clause 4.2.3에서 상류 지형이 여럿일 때 평균화 허용 |
| M_s | Shielding Multiplier | Section 4.3, Table 4.2 | 높이 ≤ 25m는 Table 4.2 사용. 25m 초과 또는 shielding 미적용 시 1.0 |
| M_t | Topographic Multiplier | Section 4.4 | Region A4(고도 400m 이상)는 Eq. 4.4(1), Region A0는 Eq. 4.4(2), 그 외는 Clause 4.4.1(c)(i)/(ii) 중 큰 값 |
| V_des,θ | Orthogonal design wind speed | Section 4 | 직교 방향 ±45° 범위의 site wind speed를 선형보간한 최댓값 |
| C_shp | Aerodynamic shape factor | Equation 5.2(1) | 이 Plug-in은 K factor(Ka, Kc,e, Kl, Kp)를 기본 1.0으로 가정하여 계산에 명시적으로 반영하지 않음 |
| C_pe | External pressure coefficient | Table 5.2(A)(풍상벽)/5.2(B)(풍하벽) | h/d 비에 따라 결정 |
| K_a | Area reduction factor | Clause 5.4.2, Table 5.4 | 밀폐형 건물 지붕·벽 적용, 그 외는 기본 1.0 |
| K_c,e | Action combination factor(외압) | Clause 5.4.3 | 일반적으로 1.0 |
| K_l | Local pressure factor(클래딩) | Clause 5.4.4 | 일반적으로 1.0(국부 클래딩압이 적용되는 경우 제외) |
| K_p | Porous cladding reduction factor | Clause 5.4.5 | 일반적으로 1.0, 투과성 클래딩 시 Table 5.8 참고 |
| C_dyn | Dynamic response factor | Section 6 | 1차 고유진동수 > 1Hz면 1.0. 0.2~1.0Hz는 Clause 6.4(along-wind)/6.5(cross-wind) 적용 |
| 건물 평면 치수 (b × d) | — | — | 형상계수·풍하중 노출 면적 산정에 사용 |

설계 풍압(Pa)은 `p = p_air × V_des,θ² × C_shp × C_dyn` 형태의 식으로 계산된다(원문 수식 이미지
참고, p_air = 공기밀도 1.2 kg/m³).

## 참고/제약사항

- 이 Plug-in은 **유연한 고층 건물(flexible tall building)을 지원하지 않는다.** 해당하는 경우
  사용자가 Equation 6.2(1) 또는 6.3(2)로 C_dyn을 직접 계산해야 한다.
- K factor들은 기본 1.0으로 가정되므로, 국부 클래딩압·다공성 클래딩 등 K factor가 1.0이 아닌
  조건이 있다면 결과를 별도로 검토해야 한다.

## 관련 JSON API 엔드포인트

Plug-in이 계산 결과를 "구조 모델에 직접 적용"한다고 설명하는 부분은, 성격상 `docs/manual`의
정적 풍하중 엔드포인트와 연동될 가능성이 높다. 다만 해당 엔드포인트 문서는 KDS 41-12:2022 /
User Type 기준으로 기술되어 있어 AS/NZS 1170.2 코드와의 정확한 필드 대응은 확인되지 않았다 —
참고용으로만 링크한다.

- [`/db/SWIND` — Static Wind Load](../../manual/06_DB_Static_Loads.md) *(코드별 필드 대응 미확인)*

> ⚠️ 원문의 "Conclusion" 문단은 "AS 1170.4:2024 지진하중 Plug-in"에 대한 설명을 그대로
> 복사한 것으로 보이는 자기모순(다른 Plug-in 아티클과 문구가 동일)이 있어 이 문서에는
> 옮기지 않았다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/46935970426905--AS-1170-2-2021-Building-Wind-Loads-Generator](https://support.midasuser.com/hc/en-us/articles/46935970426905--AS-1170-2-2021-Building-Wind-Loads-Generator)
