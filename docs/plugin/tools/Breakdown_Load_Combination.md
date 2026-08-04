# Breakdown Load Combination

> **원문:** [Breakdown Load Combination](https://support.midasuser.com/hc/en-us/articles/35845551989401-Breakdown-Load-Combination)
> **원문 작성:** 2024-08-02 · **원문 최종 편집:** 2025-08-01

---

## 개요

MIDAS CIVIL의 기본 하중케이스(primary load case)를 기준으로, 복잡한 하중조합(load
combination)을 단순하고 기초적인 형태로 분해하는 Plug-in이다. 다양한 하중조합의 영향을
분석하고, 특정 조합이 구조물에 미치는 영향을 정밀하게 파악할 수 있다.

- 하중조합을 기본 하중케이스로 변환
- MIDAS CIVIL의 기본 하중케이스를 이용해 복잡한 하중조합을 기초 형태로 단순화

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

MIDAS CIVIL은 정적(Static), 이동(Moving), 시공단계(Construction Stage), 온도(Thermal),
응답스펙트럼(Response Spectrum), 침하(Settlement), 푸시오버(Pushover) 7가지 기본 하중케이스를
제공한다. 사용자는 이 기본 하중조합을 바탕으로 어떤 하중조합이 구조물에 critical할지
예상한다.

설계 코드에 따라 수백 개의 하중조합이 필요할 수 있으며, 특히 유로코드는 매우 복잡하고 세밀한
하중조합·변동계수를 요구한다. 하중조합을 고려할 때 사용자는 일종의 "하중조합 로드맵"을
가정하고 만든다. 최종 결과에 도달하기 위해 기본 하중케이스와 생성된 하중조합을 반복적으로
조합하게 되는데, 이 반복 조합 방식에서 문제가 발생한다 — 분석 결과를 바탕으로 특정 세그먼트에
불리한 영향을 주는 하중케이스를 찾아 각 하중조합을 역추적하고 싶어지는 것이다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | 해석을 수행하고 하중조합(Load Combinations)을 생성 |
| 2 | Civil에서 요소를 선택하고 **Import Load Combinations** 버튼 클릭 |
| 3 | 분해할 대상 하중조합, 요소 끝단(element end), envelope 타입, 해당 력/모멘트를 선택하고 **Breakdown data** 버튼 클릭(필요 시 접두사(Prefix) 이름 입력 가능) |
| 4 | 새로 분해된 하중조합이 생성됨 |

## 참고/제약사항

- **해석 후 사용:** 'PostCS' 및 'locked' 상태에서 사용해야 한다.
- **요소 개수 제한:** 동시 분해 가능한 요소는 최대 5개.
- **하중조합 접두사:** LCB Prefix를 입력하면 생성되는 하중조합 이름에 반영되고, 입력하지
  않으면 선택된 하중조합을 기준으로 이름이 생성된다. 분해된 LC의 문자 수 제한은 **20자**이므로
  하중케이스 이름이나 Prefix 이름을 그에 맞게 조정해야 한다.
- **하중케이스 기준:** Active 컬럼에서 'Strength/Stress', 'Serviceability', 'Active' 기준 중
  하나가 선택되어 있어야 한다.
- **하중케이스 타입:** Type 컬럼에서 'Add' 또는 'Envelope' 타입이 선택되어 있어야 한다.
- **코드 제약:** 남아프리카공화국(South Africa)·프랑스(France) 이동하중은 지원하지 않는다.
- **하중계수 부호:** 이동하중·침하하중처럼 비대칭 하중케이스는 양(positive)의 하중계수만
  허용된다 — 음의 하중계수는 허용되지 않는다.

## 관련 JSON API 엔드포인트

Plug-in이 다루는 하중조합은 `docs/manual`의 다음 엔드포인트와 대응된다. 다만 정확히 어느
설계군(General/Concrete/Steel 등) 엔드포인트를 사용하는지는 원문에 명시되어 있지 않다.

- [`/db/LCOM-GEN` — Load Combinations (General)](../../manual/13_DB_Load_Combinations.md)

## 결론 (원문)

이 가이드를 통해 MIDAS CIVIL의 기본 하중케이스를 이용해 복잡한 하중조합을 더 다루기 쉬운
형태로 효과적으로 변환할 수 있다. 이 필수 도구는 엔지니어가 세밀하고 정확한 영향 분석을
수행하도록 돕고 구조 평가의 정밀도를 높인다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35845551989401-Breakdown-Load-Combination](https://support.midasuser.com/hc/en-us/articles/35845551989401-Breakdown-Load-Combination)
