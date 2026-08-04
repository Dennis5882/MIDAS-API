# Flared Pier

> **원문:** [Flared Pier](https://support.midasuser.com/hc/en-us/articles/45352026157593-Flared-Pier)
> **원문 작성:** 2025-04-04 · **원문 최종 편집:** 2025-08-01

---

## 개요

Flared Pier Creator Plug-in은 MIDAS CIVIL NX에서 플레어형 교각(flared pier) 생성을
단순화한다. MIDAS CIVIL NX 파일에 미리 정의된 단면·재료 데이터를 활용해, 최소한의 입력으로
플레어형 교각을 효율적으로 생성할 수 있다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

- **사용 편의성:** 교각 기둥의 끝을 정의하기 위해 최상단 노드 레벨만 선택하면 된다.
- **커스터마이즈 가능한 설계:** 로컬축 속성을 기준으로 플레어형 교각을 생성해 정확한 정렬과
  형상을 보장한다.
- **효율성:** Refresh 기능으로 프로세스를 재시작하지 않고도 단면·재료 데이터를 빠르게 갱신할
  수 있다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | Structural Group과 Boundary Group 선택(파일에서 가져옴) |
| 2 | 시작 노드 번호(start node number) 입력 |
| 3 | Reference nodes(받침 하단) 선택 |
| 4 | Sections, Materials 선택 및 각 부분의 length 입력(제목 우측 도움말 옵션으로 각 부분 확인 가능) |

## 참고/제약사항

- 선택한 모든 노드는 동일한 로컬축을 공유해야 한다 — 축이 일치하지 않으면 교각 생성 시
  오류가 발생한다.
- 생성 진행 전 모든 입력값이 0보다 큰지 다시 확인해야 한다.
- MIDAS CIVIL NX에서 변경이 있을 때마다 Refresh 아이콘으로 단면·재료 데이터를 갱신해야 한다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/45352026157593-Flared-Pier](https://support.midasuser.com/hc/en-us/articles/45352026157593-Flared-Pier)
