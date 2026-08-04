# Floor Transition

> **원문:** [Floor Transition](https://support.midasuser.com/hc/en-us/articles/35681919947673-Floor-Transition)
> **원문 작성:** 2024-07-30 · **원문 최종 편집:** 2025-08-01

---

## 개요

측정된 층(floor)의 형상을 구조 모델 내 다른 층으로 옮기거나 전환하는 것을 돕는 Plug-in이다.
다층 건물에서 특히 유용하다.

- 다층 건물에서 층을 전환하는 기능 제공
- 층 정보 또는 Z좌표를 기준으로 노드·요소 좌표 변환

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

노드·요소 좌표를 자동 조정해, 수작업이나 Excel 같은 보조 프로그램에 의존할 필요를 없앤다.
벽체 벨트(wall belt)가 있는 구조물에서 모델 일부를 수직으로 이동할 때 특히 유용하다.

- 노드·요소 좌표 조정을 자동화해 시간을 크게 절약.
- 수작업 과정에서 발생할 수 있는 오류를 줄여 모델 정확도 향상.
- 구조 모델 수정을 단순화해 효율적인 프로젝트 관리 지원.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | "From Floor"에 속하는 하단 층에서 기준 노드(Criteria Node) 1개 선택 |
| 2 | 이동시킬 층("From Floor") 입력 |
| 3 | 전환할 목적지 층("To Floor") 입력 |
| 4 | **Apply** 버튼 클릭 |

**예시:** 11층 건물에서 2층 프레임을 5층으로 옮기려면, 2층에 속한 노드 번호(예: "172")를
선택하고 "From Floor"에 "2", "To Floor"에 "5"를 입력한 뒤 Apply를 클릭하면 2층 프레임이
5층으로 이동한다.

## 참고/제약사항

- **층 정보가 있는 경우:** 구조물의 각 층이 층 정보(Story Data)로 명확히 식별되면 그 데이터를
  기준으로 동작한다. 예: 11층 건물의 2층→5층 이동 시 From Floor에 "2", To Floor에 "5" 입력.
- **층 정보가 없는 경우:** 별도 층 정보가 없으면 수직 좌표(Z좌표)를 기준으로 동작한다. 예:
  노드 그룹의 Z좌표가 0, 5, 10이면 각각 "1층", "2층", "3층"으로 간주해 입력한다 — Z=0인 노드
  그룹을 "1", Z=5를 "2", Z=10을 "3"으로 정의한다.

## 관련 JSON API 엔드포인트

Plug-in이 기준으로 삼는 층 정보는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/STOR` — Story Data](../../manual/02_DB_Project_Structure.md)

## 결론 (원문)

Floor Transition Plug-in은 구조 모델링 프로젝트에서 층 형상 변환을 돕는다. 노드·요소 좌표
조정을 자동화하고 층 정보를 효과적으로 관리해, 더 정확하고 빠른 모델링 작업을 가능하게 한다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35681919947673-Floor-Transition](https://support.midasuser.com/hc/en-us/articles/35681919947673-Floor-Transition)
