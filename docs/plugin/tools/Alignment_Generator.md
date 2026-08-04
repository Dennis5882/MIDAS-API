# Alignment Generator

> **원문:** [Alignment Generator](https://support.midasuser.com/hc/en-us/articles/40709970824729-Alignment-Generator)
> **원문 작성:** 2024-12-03 · **원문 최종 편집:** 2025-08-01

---

## 개요

이 Plug-in은 원호(arc) 또는 클로소이드(clothoid)·3차 포물선(cubic parabola)을 포함한 복잡한
선형을 생성한다. 수동 계산·입력 없이 복잡한 선형 생성을 자동화한다. 전역 좌표계 또는
사용자 지정 각도를 기준으로, 각 교각(pier)에 가장 가까운 방향으로 수평 관성력을 정렬한다.

곡선교·램프처럼 교각과 전역 좌표계 사이 정렬이 어긋나 지진 해석 워크플로가 복잡해지기 쉬운
복잡한 교량 형상 모델링에 특히 유용하다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

전통적으로 구조 엔지니어는 CAD 툴로 전체 해석 프로젝트를 준비하면서 선형 분할, 경간장·받침
위치 정의, MIDAS CIVIL NX로 파일 내보내기 같은 반복 작업을 거쳐야 했다. Lisp나 AutoCAD VBA를
쓰더라도 시간이 오래 걸리고 사람 실수가 발생하기 쉬운 과정이었다. Alignment Generator
Plug-in은 MIDAS CIVIL NX 안에서 선형 생성을 직접 자동화해 이런 번거로운 단계를 없애고, 시간을
절약하며 오류를 줄이고 전체 워크플로를 단순화한다.

## 사용 방법

| 필드 | 설명 | 옵션·기본값 |
| --- | --- | --- |
| Segment 추가/Line Type 선택 | 세그먼트를 추가하고(①) 선 종류를 선택(②)하며, 길이·시작/종료 반경을 지정(③) | — |
| 세그먼트 간 거리 | 생성될 노드 사이 거리(=요소 길이)를 입력 | — |
| Structure Group / Material / Section ID | 세그먼트별로 구조 그룹·재료·단면 ID 설정(④) | — |
| 미리보기 그래프 | 입력값에 따라 하단 그래프가 실시간으로 갱신되어 미리보기 제공(⑤) | — |
| Create | 입력 완료 후 클릭하면 노드·요소·로컬축이 생성됨 | — |
| Help 아이콘 | 사용 중 궁금한 점은 도움말 아이콘으로 Plug-in 정보 확인 가능 | — |

> ⚠️ **주의(원문):**
> - 세그먼트 개수가 선형(alignment) 개수와 같을 필요는 없다.
> - 세그먼트 총 길이는 선형 길이보다 작아야 한다.
> - 단면(Section)과 재료(Material)는 Plug-in 실행 전에 미리 생성되어 있어야 한다.
> - 기준 노드 위치는 GCS 기준 (0,0,0)이며, 노드 번호는 X(+) 방향으로 증가한다.
> - 이 Plug-in은 X-Y 평면에서만 동작한다.

생성된 선형은 이후 손쉽게 갱신할 수 있다 — 반경(Radius) 값을 바꾼 뒤 다시 **Create**를
클릭하면 된다.

## 참고/제약사항

Plug-in은 내부 스파이럴 계산 함수로 다음을 지원한다: **Clothoid**, **Cubic Parabola**.

## 결론 (원문)

Alignment Generator Plug-in은 CAD 작업 과정에서 사용자가 씨름하던 시간을 절약하고 사람 실수
가능성을 없앨 수 있다. 사용자는 선형 종류, 반경, 세그먼트 거리만 입력하면 된다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/40709970824729-Alignment-Generator](https://support.midasuser.com/hc/en-us/articles/40709970824729-Alignment-Generator)
