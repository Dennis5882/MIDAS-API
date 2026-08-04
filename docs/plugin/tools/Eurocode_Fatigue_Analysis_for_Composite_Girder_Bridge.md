# [Eurocode] Fatigue Analysis for Composite Girder Bridge

> **원문:** [Fatigue Analysis for Composite Girder Bridge \[NTC 2018\]](https://support.midasuser.com/hc/en-us/articles/49393118303897-Road-bridge-Concrete-Fatigue-for-Composite-Section)
> ("Plug-in Item" 목록 표기는 "[Eurocode] Fatigue Analysis for Composite Girder Bridge"이나,
> 아티클 자체 제목은 "Fatigue Analysis for Composite Girder Bridge [NTC 2018]"이다.)
> **원문 작성:** 2025-08-01 · **원문 최종 편집:** 2026-01-06

---

## 개요

**Eurocode** 기준으로 합성 교량(composite bridge)의 피로 해석을 수행하는 Plug-in으로,
이탈리아 국가부속서 **NTC 2018**도 지원한다. MIDAS Civil NX와 연동되어 콘크리트, 철근,
강거더(steel girder)에 대한 피로 평가를 수행한다. 피로 파라미터 설정, 구조 데이터 가져오기,
피로 안전성 검토 결과 생성을 지원한다.

## 지원 버전

- `MIDAS CIVIL NX 2025 (v2.x)`
- 적용 기준:
  - `EN 1991-2:2003` — Eurocode 1, Part 2: Traffic loads on bridges
  - `EN 1992-1-1:2004` — Eurocode 2, Part 1-1: General rules and rules for buildings
  - `EN 1992-2:2005` — Eurocode 2, Part 2: Concrete bridges
  - `EN 1993-1-1:2005` — Eurocode 3, Part 1-1: General rules and rules for buildings
  - `EN 1993-1-9:2005` — Eurocode 3, Part 1-9: Fatigue
  - `EN 1993-2:2006` — Eurocode 3, Part 2: Steel bridges
  - `NTC 2018` (Italy) — Norme Tecniche per le Costruzioni(이탈리아 국가부속서)

## 주요 기능

- Eurocode 피로 설계 규정과 이탈리아 국가부속서(NTC 2018)를 완전히 준수.
- 콘크리트·철근·강거더 등 다중 피로 검토 지원.
- 안전율 차트, 응력범위 다이어그램, 보정계수 요약 등 시각적 결과 제공.
- **MIDAS Civil API를 통한 스마트 데이터 가져오기** 지원(원문 명시).
- 피로 케이스를 추가/편집/복사/삭제로 관리.
- 엔지니어링 문서화를 위한 결과 내보내기.

### 지원 피로 케이스 유형

| 구분 | 유형 |
| --- | --- |
| 공통(철도·도로) | Concrete Shear (보강근 불필요) · Concrete Shear (보강근 필요) · Steel Girder (직응력) · Steel Girder (전단응력) |
| 철도 전용 | Concrete Compression (Damage Equivalent Stress Method) · Reinforcing Steel (Damage Equivalent Stress Method – Railway) |
| 도로 전용 | Concrete Compression (Simplified Method) · Reinforcing Steel (Damage Equivalent Stress Method – Road) |

### 지원 단면

`COMPOSITE-I`, `COMPOSITE-T`, `STEEL-I (Type-1)`, `Steel Box Type1`, `Steel I Type1`,
`Steel Tub Type1`, `Steel Box Type2`, `Steel I Type2`, `Steel Tub Type2`

## 사용 방법 (Reinforcing Steel 기준 예시 워크플로)

| 단계 | 설명 |
| --- | --- |
| ① Plug-in 실행 | 피로 검토·MIDAS API 연동용 대시보드 접속. 실행 시 교량 유형(철도/도로) 선택 |
| ② MIDAS Civil API 연결 | 열려 있는 MIDAS Civil NX 모델에 연결해 피로 해석용 구조 데이터 자동 조회 |
| ③ 전역 파라미터 설정 | 부분안전계수(γ), 설계수명(연수 또는 사이클 수) 정의 |
| ④ 피로 유형 선택 | 검토 방법 선택 |
| ⑤ 피로 케이스 관리 | 생성된 피로 케이스 목록 확인, 편집/복사/삭제로 다중 시나리오 관리 |
| ⑥ MIDAS Civil NX 결과 가져오기 | 하중케이스·시공단계 기준 응력·력 결과를 MIDAS Civil에서 가져옴 |
| ⑦ 요소 가져오기 | MIDAS Civil에서 선택한 요소 ID를 가져옴 |
| ⑧ 데이터 로드 | 해석 대상 요소와 해당 피로 조건에 따른 하중값 확인 |
| ⑨ (선택) 피로 전용 파라미터 입력 | 특정 피로 방법에서만 제공되는 탭 |
| ⑩ (선택) 보정계수 계산 | NTC:2018에 따른 λ(람다) 값 계산 |
| ⑪ 피로 해석 실행 | 등가응력, 손상지수, 피로 안전성 계산 |
| ⑫ 결과 확인 | 선택한 피로 케이스에 따라 응력범위 비교, 보정계수, 피로 안전율 등 표시 |
| ⑬ 결과 저장 | 현재 해석 결과를 저장하고 보고·추가 검토용으로 내보내기 |

## 피로 케이스별 핵심 입력 (요약)

각 피로 케이스 유형은 여러 페이지(Fatigue Settings → 단면/재료 특성 → 보정계수)로 구성된
전용 입력 마법사를 가진다. 대표 항목:

| 피로 케이스 | 핵심 입력 | 비고 |
| --- | --- | --- |
| Concrete Compression (Simplified Method) | `fck`, `σc,max`, `σc,min` | σc,max·σc,min은 압축응력(양수)만 유효 — 0 이하(인장 또는 0)면 평가에서 제외 |
| Concrete Shear (보강근 불필요) | `Vsd,max`, `Vsd,min`(CB 포함 콘크리트 설계 하중조합에서 가져옴), 단면 특성(`d`, `bw`, `Qn`, `J`, `Vrd,c`) | 콘크리트 인장부가 있는 단면만 자동 로드, 아니면 수동 입력(Section Property Calculator 활용 가능) |
| Concrete Shear (보강근 필요) | 지간장 `L`, 유효깊이 `d`, 전단하중 `Vsd`, 전단보강근 제원, 교통조건(도로/철도별 상이) | 보정계수 λc0~λc4, 도로는 `λs = φfat·λs1·λs2·λs3·λs4`, 철도는 `λs = λs1·λs2·λs3·λs4` |
| Steel Girder (직응력) | 지간장 `L`, Detail category(예: 160, 140, 125…) → `Δσamm` 자동 설정, 직응력(Civil에서 가져오거나 수동 입력) | 철도는 `Δσ1`·`Δσ1+2` 모두 필요, 도로는 `Δσ1`만 필요 |
| Steel Girder (전단응력) | 지간장 `L`, Detail Category(Shear, 기본 100 또는 80) → `Δτamm` 자동 설정, `Δτ1`(정적하중케이스만 가져오기 가능) | 이동하중은 사전에 정적하중으로 변환 필요, MIDAS NX "Analysis / Main Control Data / Calculate Equivalent Beam Stresses" 옵션 활성화 필요 |
| Concrete Compression (Damage Equivalent Stress Method, 철도) | `fck`, `L`, `σc,max,71`, `σc,perm`(Civil 결과에서 가져옴) | 두 값 모두 0 초과여야 함 |
| Reinforcing Steel (Damage Equivalent Stress Method – Railway) | `L`, `fck`, 철근/콘크리트 탄성계수, 유효깊이 `d`, 균열상태 판정(수동/자동), 철근 종류, `ΔσRsk`, 교통조건 | 균열 자동판정: fb > fctd면 균열 단면, 아니면 비균열. 비균열 단면은 인장응력(Δσ1, Δσ1+2), 균열 단면은 휨모멘트 Msd 필요 |
| Reinforcing Steel (Damage Equivalent Stress Method – Road) | Railway 버전과 유사한 파라미터 세트(지간장·유효깊이·재료 물성·교통조건 등) | 사양 유사, 도로 교통조건 적용 |

## 참고/제약사항

- 모든 응력/력 입력값에는 유효성 검사가 있다 — 조건을 만족하지 않는 경우(예: 압축응력이어야
  할 값이 0 이하) 해당 케이스는 평가에서 제외된다.
- Steel Girder (전단응력) 케이스는 정적하중케이스만 가져올 수 있으며, 이동하중은 사전에
  정적하중으로 변환해야 한다.
- 보정계수(λ)는 자동 계산되지만, 자동 계산을 끄면 수동으로 재정의할 수 있는 항목도 있다
  (예: Reinforcing Steel – Railway의 λs1~λs4).

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/49393118303897-Road-bridge-Concrete-Fatigue-for-Composite-Section](https://support.midasuser.com/hc/en-us/articles/49393118303897-Road-bridge-Concrete-Fatigue-for-Composite-Section)
