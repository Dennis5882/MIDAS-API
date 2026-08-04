# Assign Floor Loads

> **원문:** [Assign Floor Loads](https://support.midasuser.com/hc/en-us/articles/52564358801049-Assign-Floor-Loads)
> **원문 작성:** 2025-11-19 · **원문 최종 편집:** 2025-11-19

---

## 개요

바닥하중(Floor Load)을 빠르고 직관적으로 지정하기 위한 Plug-in이다. 노드를 하나씩 수동
선택하거나 텍스트 기반 층고 입력에 의존하지 않고, 모델에서 부재를 드래그로 선택해 하중을
일괄 적용할 수 있다. 적용에 성공·실패한 영역을 그래픽 미리보기와 표 형식 정보 양쪽으로 확인할
수 있다.

## 지원 버전

`MIDAS GEN NX 2026 (v1.1) US`

## 주요 기능

- **시간 절약:** 수동 노드 선택, 다중 노드 텍스트 입력, 반복적인 하중 지정 단계를 없애 몇
  시간 걸리던 작업을 몇 분으로 줄인다.
- **오류 감소:** 노드를 잘못 클릭하거나 형상이 복잡한 경우에도, 그래픽·표 형식 정보로 결과를
  검증할 수 있어 사람 실수를 줄인다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | GEN NX에서 바닥하중을 지정할 요소(Elements)를 선택 |
| 2 | 하중이 적용될 **Plane Type** 선택 |
| 3 | **Floor Load**, **Select Load Group** 등 필요한 항목을 선택한 뒤 **Apply** 클릭 |
| Refresh | 클릭 시 건물 형상·Floor Load·Select Load Group을 갱신 |
| 결과 확인 | Results 탭에서 하중 적용 위치를 그래픽으로 검토 가능. 적용 성공/실패 영역의 노드 번호를 표 형식으로도 확인 가능 |

## 참고/제약사항

- 이 Plug-in은 항상 **"Allow Polygon Type Unit Area"**가 활성화된 상태로 동작한다.
- **"Unmodeled Sub-Beam"**과 **"Convert to Beam Load types"**는 지원하지 않는다.

## 관련 JSON API 엔드포인트

Plug-in이 다루는 "Floor Load" 지정은 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/FBLD` — Define Floor Load Type](../../manual/06_DB_Static_Loads.md)
- [`/db/FBLA` — Assign Floor Loads](../../manual/06_DB_Static_Loads.md)

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/52564358801049-Assign-Floor-Loads](https://support.midasuser.com/hc/en-us/articles/52564358801049-Assign-Floor-Loads)
