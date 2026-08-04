# Artificial Earthquake Correlation Checker

> **원문:** [Artificial Earthquake Correlation](https://support.midasuser.com/hc/en-us/articles/35650468767385-Artificial-Earthquake-Correlation-Checker)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

KDS 설계기준에 따르면 인공지진파 사이의 상관계수는 0.16을 넘지 않아야 한다. 이 Plug-in은
midas Civil의 인공지진파(Time History Function) 사이 상관계수를 계산한다.

## 지원 버전

- `MIDAS GEN NX 2026 (v1.1)`
- 적용 기준: Korean Standard (KDS)

## 주요 기능

일반적으로 시간-가속도 데이터로부터 상관계수를 계산할 때 Excel을 사용한다. 이 Plug-in은
Time History Function을 선택하는 것만으로 상관계수를 빠르게 검토할 수 있고, 결과를 표 형식으로
확인할 수 있다.

## 사용 방법

| 필드 | 설명 | 옵션·기본값 |
| --- | --- | --- |
| Time History Functions | 현재 로드된 Time History Function 목록을 가져옴(**Refresh** 버튼으로 갱신 가능). 상관계수를 검토할 Time History Function을 선택 | — |
| Correlation Coefficient Target | 상관계수 상한값 입력 | 기본값 `0.16` |
| Calculate | 클릭하면 상관계수 계산. 결과는 우측 하단 표에서 확인 | — |

결과 표 색상/표기 기준:

| 표기 | 의미 |
| --- | --- |
| 파란색 값 | 상관계수가 한계값보다 작음 |
| 빨간색 값 | 상관계수가 한계값보다 큼 |
| `NG` | Time History Function의 데이터 개수가 서로 달라 상관계수를 계산할 수 없음 |

## 참고/제약사항

인공지진파의 상관계수는 KDS 17 10 00(내진설계 일반) 기준에 따라 계산된다.

## 관련 JSON API 엔드포인트

Plug-in이 대상으로 삼는 Civil의 "Time History Functions"는 `docs/manual`의 다음 엔드포인트와
대응된다.

- [`/db/THFC` — Time History Functions](../../manual/09_DB_Dynamic_Loads.md)

## 결론 (원문)

Time History Function 데이터로부터 상관계수를 계산한다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35650468767385-Artificial-Earthquake-Correlation-Checker](https://support.midasuser.com/hc/en-us/articles/35650468767385-Artificial-Earthquake-Correlation-Checker)
