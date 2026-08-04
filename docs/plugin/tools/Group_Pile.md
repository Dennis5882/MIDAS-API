# Group Pile

> **원문:** [Group Pile](https://support.midasuser.com/hc/en-us/articles/45354275911321-Group-Pile)
> **원문 작성:** 2025-04-04 · **원문 최종 편집:** 2025-08-01

---

## 개요

Group Pile Generator Plug-in은 MIDAS CIVIL NX에서 파일캡(pile cap)을 포함한 군말뚝(group
pile) 생성을 자동화한다. 기존 Civil 파일 데이터와 직접 연동해 수동 입력을 줄이고 말뚝 설계의
일관성을 보장한다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

- **사용 편의성:** 기초 끝을 정의하기 위해 최상단 노드 레벨만 선택하면 된다.
- **원활한 데이터 연동:** MIDAS CIVIL NX 파일에서 단면·재료 데이터를 자동으로 가져온다.
- **향상된 성능:** 군말뚝 설정을 한 번 마치면 이후 많은 말뚝을 효율적으로 생성할 수 있다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | Structural Group, Boundary Group, Pile Material, Pile Section, Pile Cap Material(옵션), Pile Cap Section(옵션) 선택 |
| 2 | 시작 노드 번호(start node numbers) 입력 |
| 3 | Pile array numbers, 중심 간 간격(Spacing), Edge length, Pile Diameter, Length, Cap height(옵션) 입력. Length 단위는 `D`(말뚝 치수 기준) 또는 `L`(전역 단위 기준) 중 선택 |
| 4 | 파일캡을 함께 생성하려면 체크박스를 선택하고 Pile Cap(옵션) 정보 입력 |
| 5 | 군말뚝 생성 전 교각 하단 노드(bottom of pier node) 선택 |

## 참고/제약사항

- **로컬축 일관성:** 선택한 모든 노드는 말뚝이 올바르게 정렬되도록 동일한 로컬축을 공유해야
  한다.
- **입력 검증:** 간격·깊이 등 수치 입력값은 반드시 0보다 커야 오류를 피할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/45354275911321-Group-Pile](https://support.midasuser.com/hc/en-us/articles/45354275911321-Group-Pile)
