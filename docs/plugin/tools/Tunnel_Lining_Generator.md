# Tunnel Lining Generator

> **원문:** [Tunnel Lining Model](https://support.midasuser.com/hc/en-us/articles/35655721814937-Tunnel-Lining-Model)
> ("Plug-in Item" 목록 표기는 "Tunnel Lining Generator"이나, 아티클 자체 제목은 "Tunnel
> Lining Model"이다.)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

터널 라이닝(tunnel lining) 해석용 midas Civil 모델을 생성하는 Plug-in이다. DXF 파일에서
가져온 요소를 기준으로 새 노드를 만들고, 지반계수(subgrade modulus)를 계산해 압축전용
탄성링크(elastic link, compression only)로 연결한다. 스프링 계수는 콘크리트 라이닝
상세설계기준(한국도로공사 2016)에 따라 AFTES, U.S 공식을 적용한다.

- 라이닝 해석용 모델 생성
- 지반계수와 요소 크기를 기준으로 스프링을 자동 계산·생성

## 지원 버전

- `MIDAS CIVIL NX 2024 (v1.1) US`
- 적용 기준: Korea Design Standard (KDS)

## 주요 기능

터널 라이닝 해석에서는 DXF 파일(라이닝 중심선)을 midas Civil로 가져온 뒤 지반계수로 스프링
강성을 계산한다. 이 Plug-in은 각 요소로부터 1m 거리에 노드를 자동 생성하고, 지반계수와
포아송비를 고려한 AFTES 공식으로 지반계수를 자동 계산한다. 끝단 경계조건으로는 Hinge와
Spring 모델을 지원하며, Spring 모델은 요소의 단면 크기를 고려해 스프링 강성을 계산한다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| DXF 임포트 | 터널 라이닝 중심선이 담긴 DXF 파일을 midas Civil로 가져옴. 요소에 할당된 단면이 없으면 끝단 경계조건은 반드시 Hinge로 생성해야 함(스프링 강성 계산에는 요소 폭이 필요) |
| Selected Elements | 라이닝 모델을 생성할 요소를 MIDAS Civil에서 선택한 뒤 Plug-in을 클릭해 요소를 가져옴 |
| Subgrade Modulus | 스프링 강성 계산에 필요한 지반계수·포아송비 입력, AFTES 공식으로 Ks 계산 |
| End Boundary Condition | Hinge: 끝단 노드에 Hinge 경계조건 생성(단면 할당 여부와 무관). Spring: 라이닝 축을 따라 압축전용 탄성링크 생성(스프링 강성은 요소 폭 기준 계산) |
| Create | 라이닝 모델 생성 — 각 요소의 법선 방향 벡터를 고려해 1m 거리에 노드점을 생성하고, 그 노드와 원래 노드를 압축전용 탄성링크로 연결 |

## 참고/제약사항

끝단 스프링 경계조건은 요소에 단면이 할당되어 있는 경우에만 계산할 수 있다.

## 관련 JSON API 엔드포인트

Plug-in이 생성하는 노드·탄성링크는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/NODE` — Node](../../manual/03_DB_Node_Element.md)
- [`/db/ELNK` — Elastic Link](../../manual/05_DB_Boundary.md)

## 결론 (원문)

이 Plug-in으로 경계조건이 포함된 터널 라이닝 모델 파일을 생성할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35655721814937-Tunnel-Lining-Model](https://support.midasuser.com/hc/en-us/articles/35655721814937-Tunnel-Lining-Model)
