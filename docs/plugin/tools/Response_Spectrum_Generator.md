# Response Spectrum Generator

> **원문:** [Response Spectrum Generator](https://support.midasuser.com/hc/en-us/articles/45716286965273-Response-Spectrum-Generator)
> **원문 작성:** 2025-04-14 · **원문 최종 편집:** 2026-07-27

---

## 개요

**NZS 1170.5 (2004)** 등 국가별 내진 하중 기준에 따라 설계응답스펙트럼(Design Response
Spectrum) 데이터를 자동 생성하는 Plug-in이다. 구조 해석용 정밀한 지진 입력함수가 필요한
엔지니어를 위해 만들어졌다. 파라미터를 커스터마이즈하고 실시간 그래프 미리보기를 제공해
응답스펙트럼 생성 과정을 단순화한다.

## 지원 버전

`MIDAS CIVIL NX 2025 (v1.1) US`, `MIDAS GEN NX 2025 (v1.1) US`

## 적용 기준 (원문 명시)

- `NZS 1170.5:2004` — New Zealand Standard for Seismic Actions
- `AS 1170.4:2024` — Australian Standard for Earthquake Actions
- `SBC 301-CR:2018` — Saudi Building Code: Seismic Design Provisions
- `NF EN1998-1:2008` — French National Annex to Eurocode 8
- `UNE EN1998-1:2011` — Spanish National Annex to Eurocode 8
- `SNZ TS 1170.5:2025` — New Zealand Standard for Seismic Actions
- `Peru E.030:2026` — Peru Standard for Seismic design

> ⚠️ 위 "적용 기준" 목록에는 7개 코드가 나열되어 있지만, 원문의 "Note" 절에는 "Currently,
> only NZS 1170.5 (2004) is supported."(현재는 NZS 1170.5(2004)만 지원)라고 명시되어 있어
> 두 절이 서로 모순된다. 이 Plug-in이 실제로 어떤 코드까지 지원하는지는 원문 자체가 불명확한
> 상태이므로, 사용 전 최신 버전에서 지원 코드를 직접 확인할 것을 권장한다.

## 주요 기능

- **코드 기반 스펙트럼 생성:** 선택한 코드에 맞춰 사용자 정의 내진 파라미터로 스펙트럼
  가속도 값을 계산.
- **실시간 시각화:** 생성된 응답스펙트럼 그래프를 적용 전에 미리보기.
- **연동 준비 완료:** 생성된 데이터를 하중케이스나 해석 함수에 바로 할당 가능.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1. Function Name | 스펙트럼 이름 입력(예: RS 01) — 진행을 위해 필수 |
| 2. Design Spectrum Selection | 설계 기준 선택 |
| 3. Set Parameters | 파라미터 설정 |
| 4. Preview Design Spectrum | 입력값 기준 스펙트럼 그래프 확인 |
| 5–6. Apply RS Data | **Update** 클릭 시 해석에 사용할 Response Spectrum Function으로 스펙트럼 할당 |

## 참고/제약사항

- 모든 입력 필드는 유효한 양의 소수값이 필요하다. 잘못된 입력은 경고 모달을 띄운다.
- (원문 Note 명시) 현재는 NZS 1170.5 (2004)만 지원하며, 향후 설계 코드를 변경하면 관련
  내진 파라미터를 모두 다시 설정해야 한다.
- 선택한 코드에 맞춘 로컬 파라미터 설정을 제공하도록 설계되었다.
- 스펙트럼 입력이 필요한 동적 해석 모듈과 함께 쓰기에 적합하다.

## 관련 JSON API 엔드포인트

Plug-in이 생성·할당하는 응답스펙트럼 함수는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/SPFC` — Response Spectrum Functions](../../manual/09_DB_Dynamic_Loads.md)

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/45716286965273-Response-Spectrum-Generator](https://support.midasuser.com/hc/en-us/articles/45716286965273-Response-Spectrum-Generator)
