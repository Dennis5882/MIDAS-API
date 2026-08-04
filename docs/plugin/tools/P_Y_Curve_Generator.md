# P-Y Curve Generator

> **원문:** [P-Y Curve Generator](https://support.midasuser.com/hc/en-us/articles/52596776672537-P-Y-Curve-Generator)
> **원문 작성:** 2025-11-20 · **원문 최종 편집:** 2025-12-18

---

## 개요

API RP2A, Matlock(1970), Reese et al.(1974/1975) 등 국제적으로 통용되는 정식과 다양한 암반
모델을 기반으로 말뚝 기초의 수평 지반저항(P-Y) 곡선을 생성하는 Plug-in이다. MIDAS Civil
NX/Gen과 매끄럽게 연동되며, 심도에 따른 비선형 스프링을 산출해 상세한 지반-구조물 상호작용
모델링을 지원한다.

다층 지반 프로파일을 평가하고 층 전이를 자동으로 감지하며, 엄밀한 지반공학적 정식·등가심도
보정·지반별 저항 모델을 이용해 각 말뚝 노드의 P-Y 곡선을 계산한다. 구조 해석 워크플로에
사용할 스프링 데이터를 빠르게 생성·시각화·내보낼 수 있다.

## 지원 버전

`MIDAS CIVIL NX 2025 (v2.x)`

## 지원 P-Y 모델

| 구분 | 모델 |
| --- | --- |
| 점토(Clay) | Soft Clay — API RP2A(Matlock 1970) · Stiff Clay — Reese et al.(1975), 지하수 없음(지하수 있는 버전은 아직 미구현, 단위중량만 자동 반영) |
| 모래(Sand) | API Sand · Reese et al.(1974) Sand |
| 암반(Rock) | Weak Rock — Reese(1997) · Strong Rock — Tunner(2006), Vuggy Limestone |

### 지원 말뚝 타입

Pipe, Solid Round, H-Section, Box, Solid Rectangle

## 이론적 구현 사항

- **다층 지반과 등가심도(Equivalent Depth, Georgiadis Method):** 말뚝 길이를 따라 서로 다른
  지반층이 있으면, 상부층의 누적 저항을 다음 층의 등가 시작심도로 변환해 각 층의 P-Y 거동이
  올바른 저항 상태에서 시작하도록 한다: `∫[0, h_eq,i] p_i(z) dz = f0_i`
- **노드 영향구간과 스프링 조립:** 각 말뚝 노드는 영향구간(influence zone)을 가지며, 수평
  반력은 `P(y) = ∫[z1, z2] p(y,z) dz`로 계산되어 층 변화·직경 변화·심도별 비선형 강성 변화를
  반영한다.
  - 첫 노드: 지표면부터 중간심도까지
  - 중간 노드: 인접 노드 사이 중간심도
  - 마지막 노드: 이전 중간심도부터 말뚝 선단까지
- **비원형 단면의 유효 직경:** Reese et al.(1974/1975), Matlock(1970), API RP2A 등 고전
  정식은 원형 말뚝 시험에서 유도되어 직경 D를 기준으로 정규화되어 있다. H형강·박스·사각 단면
  등 비원형 단면은 실제 단면과 동일한 흙 접촉 둘레를 갖는 등가 원형 말뚝으로 변환해 적용한다:
  `D_eff = P_shape / π` (P_shape = 실제 말뚝 단면 둘레)
- **군말뚝·경사말뚝(Group and Battered Pile):**
  - **군효과(Group Effect):** 말뚝을 좁은 간격으로 군으로 설치하면 개별 말뚝 주변 저항구간이
    겹쳐 동일 수평변위에서 단일 말뚝보다 적은 하중을 부담한다. p-multiplier는 말뚝 간격과
    군 내 위치에 영향을 받으며, 선두열 말뚝이 후열보다 일반적으로 더 큰 p-multiplier를 갖는다.
    설계 실무에서는 군 전체의 평균 p-multiplier를 대표값으로 쓰는 경우가 많다. Mokwa and
    Duncan(2001)이 말뚝 간격·배치에 따른 p-multiplier 추정 설계 차트를 제안했다.
  - **경사말뚝(Battered Pile):** Kubo(1965), Awoshika & Reese(1971) 연구에 따르면 경사각
    도입(정/부)에 따라 동원되는 지반저항이 수직 말뚝 대비 증가하거나 감소하며, 그 비율은 실험
    관측에 기반한다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1. 지반층 입력 | 수중(submerged)/유효 단위중량은 직접 입력하지 않는다 — Automatic Groundwater Level 모드에서는 사용자가 입력한 포화단위중량에서 물의 단위중량을 빼 부력 효과를 자동 반영한다. 지표면(Ground Level)을 기준으로, 지표 아래 깊이는 양수, 지표 위 높이는 음수로 입력(시추 데이터 관례 기준). 지하수위가 지표보다 높으면 음수로 입력 |
| 2. 말뚝 형상 입력 | MIDAS 제품에서 요소를 선택해 "Import from MIDAS Product"로 직접 가져오기 가능. 모델의 말뚝군 배치가 전역좌표계에 대해 회전되어 있으면 회전각을 지정해 지반 거동 방향을 올바르게 정의. 우측 패널의 "Group Effect Calculator"로 p-multiplier를 자동 계산하거나 수동 입력 가능(X·Y 방향 독립 지정, Excel처럼 범위 드래그로 다중 입력 가능) |
| 3. Pile-Soil Assignment | P-Y 곡선 케이스 생성 시 앞서 정의한 말뚝 정보·지반 프로파일·말뚝 shift 값을 지정. **"Save and Generate Non-Linear Spring"**을 클릭해야 P-Y 곡선이 생성됨 |
| 4. 결과 검토 및 모델링 생성 | 생성된 경계조건 계산 결과를 검토하고, **"Generate Boundary Condition Modelling"** 클릭 시 해당 경계조건이 MIDAS 제품에 직접 생성됨 |

## 검증(Verification)

원문에는 Plug-in이 생성한 P-Y 곡선을 외부 참조 프로그램 결과 및 수기 계산과 정량 비교한
검증 챕터가 포함되어 있다 — 6개 층(Soft Clay → Sand → Sand → Stiff Clay → Weak Rock →
Strong Rock)으로 구성된 예제 지반 프로파일과 길이 15.0m·직경 1.20m 원형 말뚝을 기준으로,
층 전이를 포함한 특정 노드(예: Node 8130, 말뚝심도 9.0~10.0m)에서의 P-Y 적분 과정을 10개
세분점에 대해 사다리꼴적분법으로 계산해 `P = -1607.42 kN`(변위 -1.255879 m 기준)을 도출하는
예시가 상세히 제시되어 있다. 이 저장소 문서에는 방법론만 요약했으며, 전체 수치 예제는 원문을
참고할 것.

## 주요 기능

- 다층 지반 시스템에 대한 심도별 P-Y 스프링 생성
- 등가심도 적분으로 층 전이를 정확히 반영
- 현대 말뚝 설계에서 쓰이는 주요 지반저항 모델 대부분 지원
- P-Y 곡선, 지반 프로파일 차트, 층 요약 제공
- MIDAS Civil/GEN NX 비선형 경계조건과 완전 호환
- 스프링 력-변위 표 내보내기 지원

## 관련 JSON API 엔드포인트

Plug-in이 "Generate Boundary Condition Modelling"으로 생성한다고 설명하는 비선형 스프링
경계조건은, 성격상 `docs/manual`의 다음 엔드포인트들과 연관될 가능성이 높다. 다만 원문에
정확히 어느 엔드포인트(General Link vs Point Spring 등)를 쓰는지 명시되어 있지 않아
참고용으로만 링크한다.

- [`/db/MLFC` — Force-Deformation Function](../../manual/05_DB_Boundary.md) *(대응 미확인)*
- [`/db/NLNK` — General Link](../../manual/05_DB_Boundary.md) *(대응 미확인)*

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/52596776672537-P-Y-Curve-Generator](https://support.midasuser.com/hc/en-us/articles/52596776672537-P-Y-Curve-Generator)
