# [AS 1170.4:2024] Static Seismic Loads Generator

> **원문:** [\[AS 1170.4:2024\] Static Seismic Loads Generator](https://support.midasuser.com/hc/en-us/articles/46857988729753--AS-1170-4-2024-Static-Seismic-Loads-Generator)
> **원문 작성:** 2025-05-13 · **원문 최종 편집:** 2025-08-13

---

## 개요

**AS 1170.4:2024** 기준에 따라 등가정적 지진하중 계산을 자동화하는 Plug-in이다. 지진 설계
파라미터를 입력하면 X·Y 두 방향의 층별 횡력 분포를 즉시 시각화해 내진 설계 워크플로를
단순화한다.

## 지원 버전

- `MIDAS GEN NX 2024 (v1.1) US`
- 적용 기준: AS 1170.4:2024 (Structural design actions, Part 4: Earthquake actions in
  Australia)

## 주요 기능

- **기준 준수:** 최신 AS 1170.4:2024 기준을 따라 최신 정적 횡하중 계산 지원.
- **시각적 검증:** 방향별 층력(Story Force)·층전단(Story Shear)·전도모멘트(Overturning
  Moment) 분포를 듀얼 막대그래프로 표시해 결과를 즉시 확인·해석 가능.
- **상호작용형 워크플로:** 파라미터 변경 시 그래프가 즉시 갱신되어 반복 작업 시간을 줄이고
  모델링 효율을 높임.
- **계산서 내보내기·연동:** 계산된 정적 지진하중을 구조 모델에 직접 적용하거나, 문서화를
  위해 Excel 계산서로 내보낼 수 있음.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 좌측: 지진 설계 파라미터 입력 | 아래 표의 파라미터를 입력 |
| 우측: 결과 시각화 | Story Force·Story Shear·Overturning Moment를 X·Y 두 방향 그래프·표로 즉시 표시 |
| Load Cases to Apply to Seismic Loads 탭 | 방향별로 지진하중을 적용할 정적하중케이스(Static Load Case) 선택 |
| Apply Seismic Loads | 클릭하면 계산된 하중을 구조 모델에 적용 |

## 지진 설계 파라미터 (원문 조항 대응)

| 번호 | 파라미터 | 근거 조항 | 설명 |
| --- | --- | --- | --- |
| ① | Sub-Soil Class | Section 4.1.1 / 4.2 | `Ae, Be, Ce, De, Ee` 중 선택 |
| ② | Annual Probability of Exceedance | Table 3.1 | 초과확률에 따라 확률계수(kp) 결정 |
| ③ | Hazard Factor (Z) | Table 3.2, Figures 3.2(A)–3.2(G) | 호주 지역별 Z값 |
| ④ | kp × Z | Table 3.3 | kp·Z 곱을 자동 계산하고 Table 3.3의 최솟값과 비교 검증 |
| ⑤ | Importance Level | NCC / AS/NZS 1170.0 Appendix F | 이 Plug-in은 Level `2, 3, 4`만 지원. Level 1(지진하중 고려 불필요)과 주거용(domestic) 구조물은 미지원 |
| ⑥ | Structure Height (hn) | — | 기초에서 지진하중에 기여하는 최고 질량까지의 총 높이. 모델링상 최대 층고 사용 |
| ⑦ | Earthquake Design Category (EDC) | Table 2.1 | 아래 "EDC 지원 범위" 참고 |
| ⑧ | Sp, μ | Table 6.5 | 구조 성능계수(Sp)·구조 연성계수(μ), X·Y 방향 개별 설정 가능 |
| ⑨ | Fundamental Period (T₁) | Equation 6.2(7) | 방향별 고유주기(초) 직접 입력 또는 **Period Calculator**로 코드 근사식 자동 계산. X·Y 방향 개별 설정 가능 |

### EDC(Earthquake Design Category) 지원 범위

| EDC | 해석 방법 | 근거 조항 | 이 Plug-in 지원 여부 |
| --- | --- | --- | --- |
| I | Simple Static Method | Clause 5.2, 5.3 | 지원 |
| II | Static Analysis | Clause 5.2, 5.4 | 지원 |
| III | Dynamic Analysis 필요 | Clause 5.2, 5.5 | **미지원** — 별도 Plug-in "[AS 1170.4:2024] Response Spectrum Generator" 사용 |

### 밑면전단력(Base Shear) 계산식

- **EDC I (Simple Static Method, Eq. 5.3, Clause 5.3):** 층 i의 지진중량 Wi를 사용해 계산.
- **EDC II (Static Analysis, Eq. 6.2(3), Clause 6.2.1):** `kp·Z`(확률계수×위험계수), `Ch(T1)`
  (Clause 6.4의 탄성 부지 위험 스펙트럼 값), `Sp`(구조 성능계수, Table 6.5), `μ`(구조
  연성계수, Table 6.5), `Wt`(전체 층의 Wi 합)를 사용해 계산.

## 결론 (원문)

이 Plug-in은 AS 1170.4:2024 기준에 맞춰 정적 지진하중을 생성하는 포괄적이고 사용하기 쉬운
환경을 제공한다. 표준화된 파라미터 입력과 동적 시각 피드백을 통해 지진 설계 과정의 투명성을
보장한다. 엔지니어는 지반 등급·구조 높이·연성 같은 핵심 입력이 층별 하중 분포에 미치는 영향을
더 잘 이해할 수 있어 설계 품질과 의사결정 효율을 모두 높인다. 입력부터 시각화·내보내기까지
이어지는 원활한 워크플로가 수작업 부담을 크게 줄이고 표준화되고 재현 가능한 결과를 촉진한다.

## 참고/제약사항

- **EDC III(동적 해석 필요) 구조물은 이 Plug-in으로 처리할 수 없다** — 별도의 "[AS
  1170.4:2024] Response Spectrum Generator" Plug-in을 사용해야 한다.
- Importance Level 1 구조물과 주거용(domestic housing) 구조물은 지원하지 않는다.

## 관련 JSON API 엔드포인트

Plug-in이 계산 결과를 적용하는 "Static Load Cases"는 `docs/manual`의 다음 엔드포인트와
대응된다. 다만 AS 1170.4 코드 자체와의 정확한 필드 대응(지진하중 전용 테이블 포함 여부)은
확인되지 않았다 — 참고용으로만 링크한다.

- [`/db/STLD` — Static Load Cases](../../manual/06_DB_Static_Loads.md) *(적용 대상 하중케이스)*
- [`/db/SSEIS` — Static Seismic Load (KDS 41-17-00:2019 / User Type)](../../manual/06_DB_Static_Loads.md) *(코드별 필드 대응 미확인)*

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/46857988729753--AS-1170-4-2024-Static-Seismic-Loads-Generator](https://support.midasuser.com/hc/en-us/articles/46857988729753--AS-1170-4-2024-Static-Seismic-Loads-Generator)
