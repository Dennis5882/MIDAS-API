# Iterative Response Spectrum

> **원문:** [Iterative Response Spectrum](https://support.midasuser.com/hc/en-us/articles/50959239482393-Iterative-Response-Spectrum)
> **원문 작성:** 2025-09-24 · **원문 최종 편집:** 2025-10-14

---

## 개요

지반 비선형성을 고려하면서 응답스펙트럼(Response Spectrum) 선형 해석을 수행할 수 있게 하는
Plug-in이다. MIDAS Civil NX에서 응답스펙트럼 해석의 반복적 강성 갱신을 자동화한다. 포인트
스프링(point spring)을 처리하고 변위 결과를 추출해 수렴할 때까지 강성을 반복 갱신한다.
사용자는 반복(iteration) 전반의 강성 변화를 추적하고 결과를 효율적으로 비교할 수 있다.

## 지원 버전

`MIDAS CIVIL NX 2025 (v2.1) US`

## 주요 기능

변위 결과를 기반으로 수렴할 때까지 스프링 강성을 갱신하는 반복 응답스펙트럼 해석 과정을
자동화한다. 수동 강성 조정과 해석 재실행이 필요 없어 시간을 크게 절약하고 오류를 줄인다.
강성 변화를 손쉽게 추적할 수 있고 모든 결과를 Excel로 내보낼 수 있다. MIDAS Civil NX의
비선형 지반-구조물 상호작용(soil-structure interaction) 케이스에 특히 유용하다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | 빈 경계 그룹(Empty Boundary Group) 생성 |
| 2 | **Connect** 클릭 → Marketplace를 열고 Iterative Response Spectrum Plug-in 실행 |
| 3 | Empty Boundary Group, Response Spectrum case, Tolerance 값을 선택하고 **Run Analysis** 클릭 |
| 4 | 해석이 수렴하면 모든 반복(iteration)의 결과를 Excel 형식으로 다운로드 가능 |

## 참고/제약사항 — Plug-in이 고려하는 가정

1. **Force-deformation Function:** 양(+)/음(-) 방향에 대해 대칭으로 간주한다. 예: +Dx/-Dx
   방향에 정의된 스프링은 +Dx로 변환된다. F-D 함수에는 음(negative)의 기울기가 없어야 한다.
2. **선형 스프링 강성:** 한 노드에 한 방향으로만 다선형(multi-linear) 스프링 정의가 있는
   경우, 첫 반복 이후 다른 방향에는 최소 강성(병진 자유도에 한해 0.001)이 적용된다.
3. **일정 강도(Uniform capacity):** 변형이 Force-deformation Function에 정의된 범위를
   초과하면, ITR 스크립트는 새로 얻은 변형까지 마지막으로 정의된 지점의 힘을 일정하게
   유지한다.
4. **노드 로컬축:** 다선형 스프링 정의에 노드 로컬축이 정의되어 있으면 시컨트(secant) 강성
   계산에 노드 로컬 변위를 사용하고, 정의되어 있지 않으면 전역 노드 변위를 사용한다.
5. **시공단계(CS):** 시공단계가 정의되어 있지 않으면 다선형 정의를 가진 모든 노드가 ITR
   스크립트 반복 대상이 된다. 시공단계가 정의되어 있으면, 마지막 시공단계에서 활성화된 경계
   그룹을 확인하고 그 안에서 포인트 선형/다선형 스프링을 가진 노드를 식별해 반복 대상으로
   삼는다. `Default` 옵션/그룹에 속한 경계 파라미터는 이 Plug-in에서 고려되지 않는다.
6. **Tolerance:** 비율로 입력한다(예: `0.05` = 5%). 모든 병진 자유도(로컬/전역)에 대해
   검사하며, 직전 반복 대비 노드 변위를 확인한다. 예: Tolerance 0.01, 이전 변위 5, 새 변위
   6이면 `(6-5)/5 = 0.2 > 0.01`이므로 Plug-in은 새 변위에 대한 힘을 보간하고 강성을 계산해
   해석을 다시 실행한다.

## 관련 JSON API 엔드포인트

Plug-in이 다루는 경계 그룹·응답스펙트럼 하중케이스는 `docs/manual`의 다음 엔드포인트와
대응된다. 다만 포인트 스프링 자체가 어느 엔드포인트(`/db/NSPR`, `/db/GSPR` 등)에 대응하는지는
원문에 명시되어 있지 않아 링크하지 않았다.

- [`/db/BNGR` — Boundary Group](../../manual/02_DB_Project_Structure.md)
- [`/db/SPLC` — Response Spectrum Load Cases](../../manual/09_DB_Dynamic_Loads.md)

## 결론 (원문)

Iterative Response Spectrum Plug-in은 수렴할 때까지 강성 갱신을 자동화해 비선형 응답스펙트럼
해석을 단순화한다. 사용자는 최소한의 입력으로 정확한 지반-구조물 상호작용 해석을 수행할 수
있어 수작업을 줄이고 신뢰성을 높인다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/50959239482393-Iterative-Response-Spectrum](https://support.midasuser.com/hc/en-us/articles/50959239482393-Iterative-Response-Spectrum)
