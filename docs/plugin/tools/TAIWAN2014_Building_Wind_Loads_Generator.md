# [TAIWAN2014] Building Wind Loads Generator

> **원문:** [\[TAIWAN2014\] Building Wind Loads Generator](https://support.midasuser.com/hc/en-us/articles/52808991968665--TAIWAN2014-Building-Wind-Loads-Generator)
> **원문 작성:** 2025-11-27 · **원문 최종 편집:** 2025-12-09

---

## 개요

밀폐형 건물을 대상으로 **대만 TAIWAN(2014)** 기준에 따라 정적 풍하중 계산을 자동화하는
Plug-in이다. 풍하중 설계 파라미터를 입력하면 높이별 풍압·풍력 분포를 즉시 시각화해 풍하중
설계 과정을 단순화한다.

## 지원 버전

- `MIDAS GEN NX 2026 (v1.1) US`
- 적용 기준: TAIWAN 2014 — 第二章 建築物設計風力之計算(대만 내정부 국토관리서)

## 주요 기능

- **기준 준수:** TAIWAN 2014 기준(밀폐형 건물)을 따라 최신 하중 평가 지원.
- **시각적 검증:** 방향별 설계풍압·층력(Story Force)·층전단(Story Shear)·전도모멘트
  (Overturning Moment) 분포를 막대그래프로 표시해 결과를 즉시 확인·해석 가능.
- **상호작용형 워크플로:** 파라미터 변경 시 그래프가 즉시 갱신되어 반복 작업 시간을 줄이고
  모델링 효율을 높임.
- **계산서 내보내기·연동:** 계산된 정적 풍하중을 구조 모델에 직접 적용하거나, 문서화를
  위해 Excel 계산서로 내보낼 수 있음.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 좌측: 풍하중 설계 파라미터 입력 | 구조 모델의 풍하중 설계 파라미터 입력 |
| 우측: 결과 시각화 | Design Wind Pressure·Story Force·Story Shear·Overturning Moment를 X·Y 두 방향 그래프·표로 즉시 표시 |
| Load Cases to Apply to Wind Loads 탭 | 방향별로 풍하중을 적용할 정적하중케이스(Static Load Case) 선택. X·Y 방향 하중케이스는 반드시 서로 달라야 함(덮어쓰기 방지) |
| Apply Wind Loads | 클릭 시 계산된 하중을 구조 모델에 적용 |

## 풍하중 설계 파라미터 (원문 조항 대응)

| 번호 | 파라미터 | 근거 조항 | 설명 |
| --- | --- | --- | --- |
| ① | Basic Wind Speed (V₁₀) | 2.4 基本設計風速 | 대상 부지 10m 높이 기준 10분 평균풍속(재현기간 통상 50년). 대만 풍속지도 또는 지역 규정 참고 |
| ② | Exposure Category | 2.3 風速之垂直分布, 表2.2 | Category A(도심, 20m 초과 건물 50% 이상): α=0.32, Zg=500m, Zmin=18m · Category B(교외/소도시): α=0.25, Zg=400m, Zmin=9m · Category C(개활지/해안): α=0.15, Zg=300m, Zmin=4.5m |
| ③ | Importance Factor (I) | 2.5 用途係數 | 건물 용도·기능에 따른 중요도계수 |
| ④ | Mean Roof Height (hn) | — | 구조 모델의 층 데이터에서 자동 추출된 지반 위 평균 지붕 높이(모델 내 최대 표고). K(z), 거스트영향계수, 지형계수 산정에 사용 |
| ⑤ | Topographic Factor (Kzt) | 表2.3(a)(b)(c) | "Topographic Settings"에서 선택 입력(옵션). 언덕/능선/절벽에 의한 풍속 증가 효과 반영. 방향별로 Hill Shape(Ridge/Escarpment/Hill), Hill Height(H), Hill Length(Lh), Crest-Building Distance(x, 풍상측 양수/풍하측 음수) 지정 → K1(H/Lh, 表2.3(a)), K2(x/Lh, 表2.3(b)), K3(z/Lh, 表2.3(c)) 계산. 지형 효과를 고려하지 않으면 전 층 Kzt=1.0 |
| ⑥ | Structure Type | — | Rigid Structure(고유진동수 > 1Hz, 저·중층 건물, 단순 거스트영향계수 계산) 또는 Flexible Structure(고유진동수 ≤ 1Hz, 고층/세장 건물, 고유진동수·감쇠비 입력 필요, 더 상세한 동적 응답 고려) |
| ⑦ | Gust Effect Factor (G 또는 Gf) | 2.7 陣風反應因子 | "Gust Effect Factor Calculator"로 X·Y 방향 계산. Rigid Structure는 건물 폭(B)·길이(L) 입력 → 난류강도(Iz)·적분길이축척(Lz)·배경응답계수(Q) 자동 산정. Flexible Structure는 X·Y 방향 고유진동수, 감쇠비 추가 입력 필요(공진응답 효과 포함) |
| ⑧ | Building Width and Depth (b × d) | — | 형상계수·풍하중 유효 면적 산정을 위한 건물 평면 치수 |
| ⑨ | Load Cases to Apply to Wind Loads | — | X·Y 방향 풍하중을 적용할 정적하중케이스 각각 지정(서로 달라야 함) |

## 설계 풍압 계산

- **기본 풍압 q(z):** `q(z) = (단위환산상수) × I × V₁₀² × K(z) × Kzt` 형태(원문 수식 이미지
  참고, 단위 kgf/m²를 사용자 단위계로 자동 환산).
- **속도압 노출계수 K(z):** 노출범주별 Zg(구배고도)·α(지수) 기준 높이함수(원문 수식 이미지
  참고). ⚠️ z ≤ 5m인 경우 계산 시 z = 5m으로 처리한다(원문 명시).
- **설계풍압:**
  - 풍상면: `p1(z) = q(z) × G(또는 Gf) × Cpe,windward − q(h) × GCpi`
  - 풍하면: `p2(z) = q(h) × G(또는 Gf) × Cpe,leeward − q(h) × GCpi`
  - 풍향 방향 작용 설계풍압: `p1(z) − p2(z)`
  - `Cpe,windward = 0.8`(고정값), `Cpe,leeward`는 L/B 비에 따라 변동(表2.4 선형보간),
    내압계수 `GCpi = 0.375`(밀폐형 건물 기준)
- **층풍력:** `Story Force = 설계풍압 × 층 노출높이 × 건물 폭(LOADED_BX 또는 LOADED_BY)`
- **층전단·전도모멘트:** 층전단은 해당 층 위 층력들의 누적합, 전도모멘트는 층전단과 층간
  높이의 누적모멘트.

### 계산 흐름 요약 (원문)

1. 파라미터 입력(기본풍속, 노출범주, 중요도계수, 구조형식)
2. 층별 K(z) 계산(표고·노출범주 기준)
3. 지형효과 고려 시 Kzt 계산
4. 건물 치수·동적 특성 기준 거스트영향계수(G 또는 Gf) 산정
5. 풍상·풍하면 Cpe 값 적용
6. 층별 기본풍압 계산
7. 거스트효과·압력계수 적용해 설계풍압 산출
8. 층 형상을 고려한 횡력 계산
9. 힘을 누적해 층전단·전도모멘트 산출
10. 그래프·표로 결과 시각화
11. 구조 모델에 하중 적용 또는 Excel 계산서로 내보내기

## 관련 JSON API 엔드포인트

Plug-in이 계산 결과를 "구조 모델에 직접 적용"한다고 설명하는 부분은, 성격상 `docs/manual`의
정적 풍하중 엔드포인트와 연동될 가능성이 높다. 다만 해당 엔드포인트 문서는 KDS 41-12:2022 /
User Type 기준으로 기술되어 있어 TAIWAN 2014 코드와의 정확한 필드 대응은 확인되지 않았다 —
참고용으로만 링크한다.

- [`/db/SWIND` — Static Wind Load](../../manual/06_DB_Static_Loads.md) *(코드별 필드 대응 미확인)*

## 결론 (원문)

이 Plug-in은 대만 TAIWAN 2014 건축법규에 맞춰 정적 풍하중을 생성하는 포괄적이고 사용하기
쉬운 환경을 제공한다. 표준화된 파라미터 입력과 동적 시각 피드백을 통해 풍하중 설계 과정의
투명성을 보장한다. 엔지니어는 풍속·지형 노출·지형효과·거스트응답 같은 핵심 입력이 층별
풍압·풍력 분포에 미치는 영향을 더 잘 이해할 수 있어 설계 품질과 의사결정 효율을 모두 높인다.
Rigid·Flexible 구조 모두 지원하고 지형효과를 옵션으로 제공해, 대만의 다양한 건물 유형과 부지
조건에 두루 활용할 수 있는 도구다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/52808991968665--TAIWAN2014-Building-Wind-Loads-Generator](https://support.midasuser.com/hc/en-us/articles/52808991968665--TAIWAN2014-Building-Wind-Loads-Generator)
