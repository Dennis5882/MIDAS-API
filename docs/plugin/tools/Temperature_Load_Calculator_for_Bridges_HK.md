# Temperature Load Calculator for Bridges (HK)

> **원문:** [Temperature Load Calculator for bridges (HK)](https://support.midasuser.com/hc/en-us/articles/40663607747737-Temperature-Load-Calculator-for-bridges-HK)
> **원문 작성:** 2024-12-02 · **원문 최종 편집:** 2025-08-01

---

## 개요

**STRUCTURES DESIGN MANUAL for Highways and Railways 2013 Edition(SDM 2013)** 3.5절
Temperature Effects를 기준으로 교량 구조물의 온도 작용(thermal action)을 계산하는
Plug-in이다. 상부구조 내 균일온도 변화(uniform temperature change)와 온도구배
(temperature gradient)를 모두 고려해 결과적인 온도 하중을 산정한다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

- 온도 변화에 의한 교량 구조물의 열 영향을 빠르고 정확하게 분석.
- SDM 2013 기준 균일온도 변화·온도차를 모두 고려해 온도 작용을 정확히 모델링.
- 구조 해석에 온도 작용을 빠르게 반영할 수 있도록 지원.
- 온도구배·균일온도 변화가 교량 구조물에 미치는 영향을 시각화.
- 최종 설계에 모든 온도 기여분이 정확히 반영되도록 보장.

## 사용 방법

### Uniform Temperature(균일온도)

| 단계 | 설명 |
| --- | --- |
| 1. 구조 유형별 파라미터 입력 | Superstructure Type(SDM2013 Figure 3.2 분류 참고), Structure Type(Normal/Minor, Clause 3.5.2(3) 참고), Deck Surfacing Type(SDM2013 Table 3.18 분류 참고, "Thickness" 선택 시 포장 두께 정의 가능), Height above Sea Level(Clause 3.5.2(5) 참고) |
| 2. UNIFORM 탭 선택 | 균일온도 지정 |
| 3. Adjustment to Temperature | 계산 방법 2가지 — **Ceiling Method**(음의 보정값 사용, 계산에 큰 영향), **Linear Interpolation**(중간 보정값 적용 방식이 달라 Ceiling Method와 다른 최종 결과) |
| 4. 열작용 파라미터·계산 결과 | 균일 교량온도, 보정값 등 계산된 열작용 파라미터 표시(참고용) |
| 5. 하중케이스 배정 | 균일온도에 의한 신축·수축용 하중케이스를 대상 요소에 배정 |
| 6. Apply Uniform Temperature Loads | 선택 요소에 균일온도 효과 하중 적용 실행 |

### Temperature Differences(온도차)

| 단계 | 설명 |
| --- | --- |
| 1. 구조 유형별 파라미터 입력 | Uniform Temperature 절 참고 |
| 2. DIFFERENCES 탭 선택 | 온도차 지정 |
| 3. Adjustment to Temperature | Uniform Temperature 절과 동일 방식 |
| 4. 열작용 파라미터·계산 결과 | 교량 부재 간 온도차, 보정값 등 표시(참고용) |
| 5. 하중케이스 배정 | 계산된 온도차 기준으로 가열(heating)·냉각(cooling) 하중케이스를 대상 요소에 배정 |
| 6. Apply Temperature Differences Loads | 선택 요소에 온도차 효과 하중 적용 실행 |

## 참고/제약사항

### 공통 제약

1. 각 하중케이스는 동일해야 한다(identical load cases).
2. 하중케이스는 적용 전 Load Case Menu에 미리 정의되어 있어야 한다.
3. 하중은 MIDAS Civil에 지정된 초기온도에 대한 상대 온도값으로 적용된다.

### Uniform Bridge Temperature

1. 모든 요소 타입에 적용 가능.
2. 선택한 하중케이스에 MIDAS Civil의 Element Temperature Load가 지정되어 있으면 안 된다.

### Temperature Differences

1. **보 요소에만** 적용 가능.
2. 지원 단면 타입/형상:
   - Type 1(USER): `H`, `B`
   - Type 2(COMPOSITE): `B`, `I`, `Tub`, `GB`, `GI`, `GT`
   - Type 3(PSC): `1CELL`, `2CELL`, `3CELL`, `NCEL`, `NCE2`, `PSCM`, `PSCI`, `PSCH`,
     `PSCT`, `PSCB`, `VALUE`
3. 단면/슬래브 높이값이 예시 계산에 사용되며, 선택한 실제 요소 단면 기준으로 하중이 재계산·
   적용된다.
4. 상부구조 유형별 최소 적용 단면 높이: Type 1 — 600mm, Type 2 — 슬래브 높이 + 400mm,
   Type 3 — 135mm 이상

## 관련 JSON API 엔드포인트

Plug-in이 다루는(또는 참고하는) 온도 하중은 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/ETMP` — Element Temperature](../../manual/07_DB_Temperature_Prestress.md) *(Uniform Bridge Temperature 제약조건에서 명시적으로 언급)*
- [`/db/BTMP` — Beam Section Temperature](../../manual/07_DB_Temperature_Prestress.md) *(Temperature Differences 대응 추정)*

## 결론 (원문)

이 Plug-in으로 교량 구조물에 작용하는 온도 작용을 효율적으로 분석할 수 있고, SDM 2013 기반
정확한 데이터를 제공해 정보에 근거한 설계 과정을 지원한다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/40663607747737-Temperature-Load-Calculator-for-bridges-HK](https://support.midasuser.com/hc/en-us/articles/40663607747737-Temperature-Load-Calculator-for-bridges-HK)
