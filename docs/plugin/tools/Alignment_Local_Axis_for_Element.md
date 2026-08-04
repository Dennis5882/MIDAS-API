# Alignment Local Axis for Element

> **원문:** [Alignment Local Axis for Element](https://support.midasuser.com/hc/en-us/articles/35679369131289-Alignment-Local-Axis-for-Element)
> **원문 작성:** 2024-07-30 · **원문 최종 편집:** 2025-08-01

---

## 개요

판(Plate) 요소의 로컬 z축을 기준점(Reference Point)에 맞춰 정렬한다. 원통형 구조물의 로컬축을
정렬할 때 유용하다.

## 지원 버전

- `MIDAS CIVIL NX 2024 (v1.1) US`
- 적용 기준: General Use(특정 설계기준 무관)

## 주요 기능

특정 지점을 기준으로 구조물의 로컬축을 정렬하는 데 사용할 수 있다.

## 사용 방법

| 필드 | 설명 | 옵션·기본값 |
| --- | --- | --- |
| Select Elements | midas Civil에서 요소를 선택한 뒤 Plug-in 창에 진입 | — |
| Reference Point | 로컬 z축을 정렬할 기준 노드의 좌표를 입력. 로컬 z축이 해당 노드점을 향하도록 정렬됨 | — |

## 참고/제약사항

Plate 요소 로컬축 정렬 로직은 다음과 같다.

1. Plate 요소 로컬 방향을 따라 법선 벡터를 계산한다.
2. 평면 중심에서 Reference Point까지의 벡터를 계산한다.
3. 두 벡터 사이 각도가 90도 미만이면 로컬축을 정렬하지 않고, 90도를 초과하면 Plate 요소의
   방향을 반전해 반대 축으로 정렬한다.

## 결론 (원문)

특정 요소의 축을 손쉽게 반전할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35679369131289-Alignment-Local-Axis-for-Element](https://support.midasuser.com/hc/en-us/articles/35679369131289-Alignment-Local-Axis-for-Element)
