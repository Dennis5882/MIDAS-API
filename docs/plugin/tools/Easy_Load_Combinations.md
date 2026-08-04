# Easy Load Combinations

> **원문:** [Easy Load Combinations](https://support.midasuser.com/hc/en-us/articles/45543036560921-Easy-Load-Combinations)
> **원문 작성:** 2025-04-09 · **원문 최종 편집:** 2025-08-01

---

## 개요

MIDAS CIVIL NX에서 하중조합을 생성하는 과정을 단순화하는 Plug-in이다. 몇 번의 클릭만으로
하중케이스를 가져오고, 조합계수를 적용하며, 조합된 하중케이스를 모델에 바로 전송할 수 있어
시간을 절약하고 오류를 줄인다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

- **자동 가져오기:** MIDAS 모델링 파일에 맞춰 하중케이스가 자동으로 가져와지고 갱신됨.
- **손쉬운 조합:** 하중케이스를 선택하고 계수를 적용하는 것만으로 빠르게 새 하중조합 생성.
- **원클릭 적용:** 조합된 하중케이스를 클릭 한 번으로 모델에 바로 전송.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | Plug-in을 열면 MIDAS CIVIL NX 파일의 모든 하중케이스를 자동으로 가져옴 |
| 2 | Plug-in 인터페이스 목록에서 원하는 하중케이스를 선택하고, 설계 요구사항에 맞는 조합계수를 각각 입력 |
| 3 | **Add** 클릭 시 입력한 파라미터로 새 하중조합 세트 생성. **Update/Overwrite** 클릭 시 하중조합을 CIVIL NX로 전송 |
| 4 | 제품의 Result > Load Combination에서 데이터 업데이트 성공 여부 확인 가능 |

## 참고/제약사항

- 하중조합을 생성하기 전, 가져온 모든 하중케이스가 MIDAS CIVIL NX 모델과 일치하는지
  확인해야 한다.
- 유로코드 이동하중의 경우, 호환성 문제를 피하려면 v1.1.0 이상을 사용해야 한다.
- 모델에 적용하기 전 조합계수의 정확성을 다시 한번 확인해야 한다.

## 관련 JSON API 엔드포인트

Plug-in이 다루는 하중조합은 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/LCOM-GEN` — Load Combinations (General)](../../manual/13_DB_Load_Combinations.md)

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/45543036560921-Easy-Load-Combinations](https://support.midasuser.com/hc/en-us/articles/45543036560921-Easy-Load-Combinations)
