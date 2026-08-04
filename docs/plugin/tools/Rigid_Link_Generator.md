# Rigid Link Generator

> **원문:** [Rigid link generator](https://support.midasuser.com/hc/en-us/articles/35651417232025-Rigid-Link-Generator)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

마스터 노드(Master Node)와 슬레이브 노드(Slave Node) 그룹을 선택해, 마스터 노드에서 거리상
가장 가까운 슬레이브 노드로 강체 링크(Rigid Link)를 생성하는 Plug-in이다. 등간격이 아닌
Rigid Link를 만들 때도 거리(Distance) 값을 입력할 필요가 없다 — 마스터 노드에서 가장 가까운
슬레이브 노드로 Rigid Link가 생성된다. 프레임 요소와 판 요소가 강체 링크로 연결되는
상부구조(superstructure) 모델링에 유용하다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

midas Civil에서 Rigid Link를 만들려면 마스터 노드를 선택한 뒤 연결할 정확한 슬레이브 노드를
선택해야 한다. 또한 등간격이 아닌 Rigid Link를 만들려면 'Copy Rigid Link' 기능으로 정확한
간격을 입력해야 한다. 이 Plug-in은 마스터 노드를 선택한 후 슬레이브 노드를 하나씩 선택하거나
등간격이 아닌 간격을 입력하지 않고도 Rigid Link를 생성할 수 있게 해준다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| Master Node 선택 | 마스터 노드가 될 노드 선택. midas Civil에서 노드를 선택한 뒤 Plug-in의 'Select Master Nodes' 필드를 클릭해 해당 노드를 입력(예시에서는 거더에 해당하는 노드를 선택) |
| Slave Node 선택 | 마스터 노드와 연결될 슬레이브 노드 선택. 정확한 슬레이브 노드를 선택할 필요는 없음(예시에서는 슬래브 요소 전체를 선택) |
| Link Property | Rigid Link의 속성 선택(midas Civil과 동일) |
| Apply | 클릭 시 마스터 노드에서 슬레이브 노드 그룹 중 가장 가까운 노드로 Rigid Link 생성 |

## 결론 (원문)

거더를 보 요소로, 슬래브를 판 요소로 모델링하는 경우처럼 상부구조를 모델링할 때 유용하다.
마스터 노드에서 가장 가까운 노드로 Rigid Link가 생성된다.

## 관련 JSON API 엔드포인트

Plug-in이 생성하는 Rigid Link는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/RIGD` — Rigid Link](../../manual/05_DB_Boundary.md)

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35651417232025-Rigid-Link-Generator](https://support.midasuser.com/hc/en-us/articles/35651417232025-Rigid-Link-Generator)
