# Element Information

> **원문:** [Element Information](https://support.midasuser.com/hc/en-us/articles/35649982873625-Element-Information)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

요소(Element) 정보를 손쉽게 확인할 수 있게 해주는 Plug-in이다. 특정 요소의 세부 정보를
빠르게 확인·검토할 때 사용한다.

- 요소 정보를 빠르게 확인
- 요소 테이블을 출력하지 않고도 모델링 작업 중 필요한 세부 정보 제공

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

선택한 요소의 상세 표를 보여주는 기존 방식은 Element Table과 Element Detail Table에
대응된다.

- **Element Table:** 전체 요소 목록을 표시하며 선택한 요소가 강조 표시됨.
- **Element Detail Table:** 선택한 요소만 표에 표시됨.

기존 방식은 선택한 요소 정보를 직관적으로 확인하기 번거로웠다. 이 Plug-in에서는 Element
Table이나 Element Detail Table로 이동하지 않고도 선택한 요소 정보를 바로 확인할 수 있다.

- 요소 정보를 빠르게 확인해 오류 감소
- 요소 테이블 간 이동 없이 모델링 작업 중 필요한 정보 제공, 워크플로 개선

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | 모델링에서 요소 선택 |
| 2 | Plug-in에 커서를 올려 실행 |
| 3 | 선택한 요소의 타입, 재료, 단면, 연결 노드 번호, 길이, 면적, 체적, 단위중량, 총중량, Beam End Release 정보 확인 가능 |
| 4 | **Detail** 토글을 활성화하면 각 요소 정보가 행 단위로 정렬되어 표시됨 |

## 표시 항목 (Element Information)

| 항목 | 설명 |
| --- | --- |
| Elem ID | 요소 ID |
| Node Con | 연결된 노드 ID |
| Type | 요소 타입 — `BEAM`(일반/변단면 보), `TRUSS`(트러스), `TENSTR`(인장전용/Hook/케이블), `COMPTR`(압축전용/Gap), `PLATE`(판), `WALL`(벽체), `PLSTRS`(평면응력), `PLSTRN`(평면변형), `AXISYM`(축대칭), `SOLID`(솔리드) |
| Material | 요소에 할당된 재료 이름 |
| Section | 요소에 할당된 단면 이름 |
| L/A/V | 길이 / 면적(Plate인 경우) / 체적(Solid인 경우) |
| Weight (U) | 단위 길이/면적/체적당 중량(단위중량) |
| Weight (T) | 요소 총중량 |
| BER (Beam End Release) | I/J단 해제 정보 표시. `-`(해제 정보 없음), `F`(고정, Fixed), `P`(힌지, Pinned) |

## 관련 JSON API 엔드포인트

Plug-in이 표시하는 요소 정보는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/ELEM` — Element](../../manual/03_DB_Node_Element.md)

## 결론 (원문)

이 가이드를 통해 구조 모델링 프로젝트에서 요소 정보를 효율적으로 관리하고, Element
Information Plug-in으로 필요한 정보에 빠르게 접근할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35649982873625-Element-Information](https://support.midasuser.com/hc/en-us/articles/35649982873625-Element-Information)
