# Concrete Material Set EN1992-1-1

> **원문:** [Concrete Material Set EN1992-1-1](https://support.midasuser.com/hc/en-us/articles/45536334603161-Concrete-Material-Set-EN1992-1-1)
> **원문 작성:** 2025-04-09 · **원문 최종 편집:** 2025-08-01

---

## 개요

**EN 1992-1-1** 기준에 따라 콘크리트 재료 물성과 시간 의존 거동(크리프, 건조수축) 계산 입력을
자동화하는 Plug-in이다. 설계 파라미터를 검증할 수 있는 시각화 도구를 제공하며 유로코드 규격
준수를 돕는다.

## 지원 버전

- `MIDAS CIVIL NX 2024 (v1.1) US`
- 적용 기준: EN 1992-1-1, EN 1992-2-1

## 주요 기능

- **기준 준수:** 재료·시간 의존 물성 계산에서 EN 1992-1-1을 완전히 따른다.
- **시각적 검증:** 크리프 계수, 건조수축 변형률, 응력-변형률 곡선 등 핵심 결과를 그래프로
  표시해 정확성을 점검할 수 있다.
- **효율성:** 압축/인장 강도, 탄성계수, 시간 의존 효과에 대한 수동 계산을 없앤다.

## 사용 방법

| 탭 | 설명 |
| --- | --- |
| Concrete | 콘크리트 등급(Concrete Grade) 선택 및 부분계수(partial factor) 입력. 콘크리트 응력-변형률 관계 선택 및 다이어그램 확인. **Additional Information**으로 세부 정보 확인 |
| Time-Dependent | 시간 의존 물성 입력. 표시할 항목 선택 — 크리프 계수(Creep coefficients), 건조수축 변형률(Shrinkage strain), 평균 압축강도(Mean compressive strength), 평균 인장강도(Mean tensile strength), 탄성계수(Elastic modulus). **Additional Info** 버튼으로 세부 정보 확인 |

## 참고/제약사항

- **EN 1992-2 지원:** 이 코드는 입력 저장용으로만 선택 가능하며, 계산은 수행되지 않는다.
- **MIDAS CIVIL NX 연동:** 계산된 시간 의존 물성(예: 크리프 계수)은 모델에 자동 반영되지
  **않는다**. 해당 값은 사용자가 직접 모델에 입력해야 한다.
- **입력 검증:** 입력한 값(콘크리트 재령, 습도 등)이 EN 1992-1-1 요구사항에 부합하는지
  확인해야 한다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/45536334603161-Concrete-Material-Set-EN1992-1-1](https://support.midasuser.com/hc/en-us/articles/45536334603161-Concrete-Material-Set-EN1992-1-1)
