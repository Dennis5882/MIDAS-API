# Node Controller

> **원문:** [Node Controller](https://support.midasuser.com/hc/en-us/articles/35654598923161-Node-Controller)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

노드를 선택할 때 Node Table이나 Node Detail Table 사이를 오갈 필요 없이 **노드 좌표 수정**
과정을 단순화하는 것이 목적인 Plug-in이다.

- 노드 좌표 수정 작업을 빠르게 수행
- 수정된 노드 좌표 정보를 표 형식으로 표시

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

기존에는 노드 좌표를 만들거나 수정할 때 주로 두 가지 방식을 썼다.

- Create Nodes 또는 Translate Nodes 기능 사용
- Node 또는 Node Detail Table 사용

이 Plug-in은 수작업이나 Excel 같은 보조 프로그램 의존을 간단한 조작으로 대체한다.

- 노드 좌표 수정 작업을 자동화해 시간 절약
- 작업 중 오류를 줄여 모델 정확도 향상
- 노드 테이블 간 이동 없이 필요한 정보 제공, 워크플로 개선

## 사용 방법

| 항목 | 설명 |
| --- | --- |
| 노드 선택 및 실행 | 선택 없이 Plug-in을 실행하면 노드 선택부터 시작. 이미 노드가 선택되어 있으면 즉시 정보 로드 |
| Create/Translate 토글 | **Create**: 노드 이동 중 추가 노드가 필요할 때의 불편을 없애기 위해 추가됨. **Translate**(기본값): 노드 좌표 이동 수행 |
| 선택 노드 수 표시 | 괄호 안에 선택된 노드 수 표시. 박스에는 선택된 노드 번호가 표시되며 다른 노드 선택으로 변경 가능 |
| 노드 이동 거리 입력 | X, Y, Z 좌표 박스 옆 화살표로 이동 거리값 입력. 화살표 클릭 시 지정한 값만큼 이동(예: 1 입력 후 3번 클릭하면 3m 이동) |
| 단위 변환 | 제품 내 선택된 길이 단위(m, mm, cm, in, ft 등)를 따름. 선택된 여러 노드의 X/Y/Z 값이 동일하면 수정 가능하고, 다르면 "Var."로 표시되어 수정이 차단됨 |
| Apply | 클릭 시 처리 실행 및 모델 데이터 변경 |
| 선택 노드 좌표 표 표시 | 선택된 노드의 좌표를 표 형식으로 표시. 노드 간 좌표값이 다른 경우 표에서 직접 수정 가능 |

## 관련 JSON API 엔드포인트

Plug-in이 다루는 노드 좌표는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/NODE` — Node](../../manual/03_DB_Node_Element.md)

## 결론 (원문)

Node Controller Plug-in을 활용해 구조 모델링 프로젝트에서 노드 좌표를 효율적으로 관리하고
필요한 정보에 빠르게 접근할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35654598923161-Node-Controller](https://support.midasuser.com/hc/en-us/articles/35654598923161-Node-Controller)
