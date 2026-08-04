# Line to Plate Converter

> **원문:** [Line To Plate Converter](https://support.midasuser.com/hc/en-us/articles/60469083421593-Line-To-Plate-Converter)
> **원문 작성:** 2026-07-27 · **원문 최종 편집:** 2026-07-29

---

## 개요

MIDAS CIVIL NX에서 선택한 Beam 요소를 더 상세하고 정확한 해석을 위해 Plate 요소로 변환하는
Plug-in이다. 메시 밀도, 분할 방법, 변환된 판과 나머지 프레임 모델 사이의 경계 연결성을 유연하게
제어할 수 있다. 원래 단면 형상·재료·강성 특성에 맞춘 Plate 단면을 생성해 원본 모델의 구조적
의도를 유지한다.

## 지원 버전

`MIDAS CIVIL NX 2026 (v1.1)`

## 주요 기능

- **해석 정확도 향상:** 1D 보 요소를 2D 판 요소로 변환해 더 상세하고 정확한 해석을 제공한다.
- **유연한 메싱 제어:** 종방향 분할 전략을 목표 메시 크기(m) 또는 분할 개수 중 선택할 수
  있고, 단면 메시 크기 파라미터로 횡방향 메시 밀도를 별도로 제어할 수 있다.
- **구조적 연결성 유지:** 옵션인 Rigid Link 기능이 경간 양 끝에 강체 링크를 자동 생성해,
  변환된 판 메시와 나머지 프레임 모델 사이 연결성·경계 구속을 유지한다.
- **시간 절약:** 판 메시 생성, 두께 지정, 기존 모델과의 연결이라는 번거로운 수작업을
  자동화한다. 몇 시간 걸리던 수동 모델링을 클릭 몇 번으로 줄인다.

## 사용 방법

| 필드 | 설명 | 옵션·기본값 |
| --- | --- | --- |
| 요소 선택 | MIDAS CIVIL NX에서 Plate로 변환할 Beam 요소 선택 | — |
| Division Type 토글 | OFF: Mesh division(개수) — 종방향 분할 개수 입력, ON: Mesh size(m) — 종방향 목표 메시 크기(m) 입력 | 개수 범위 2~500(기본 5), 크기 범위 0.1~10.0m(기본 0.50m) |
| Section Mesh size (m) | 단면을 판 스트립으로 나누는 횡방향 세분화 크기 | 범위 0.1~10.0m, 기본 0.50m |
| Rigid Link 체크박스 | 활성화 시 경간 양 끝에 강체 링크를 생성해 원래 프레임 모델과의 연결성 유지 | 기본 활성화 |
| Convert | 클릭 시 변환 시작. 처리 중에는 모든 입력 필드가 비활성화되고 진행률 스피너 표시 | — |

## 참고/제약사항

- Plug-in은 선택된 1D 요소를 모델에서 **삭제**한다. 연관된 하중·텐던이 있다면 함께 삭제되며,
  필요 시 수동으로 다시 만들어야 한다.
- 선택한 요소가 하나의 연속된 체인이 아니면, 가장 작은 요소 ID부터 시작하는 연속 구간만
  처리된다.
- 지원하지 않는 단면 타입은 "Unsupported Section" 오류 메시지를 표시하고 인터페이스가
  초기화되어 재시도할 수 있다.

### 지원 단면 (Uniform·Tapered)

| 이름 | Shape Code |
| --- | --- |
| Angle | `L` |
| Channel | `C` |
| H/I-Section | `H` |
| T-Section | `T` |
| Box | `B` |
| Pipe | `P` |
| Solid Rectangle | `SB` |
| PSC 1-Cell | `1-CEL` |
| PSC 2-Cell | `2-CEL` |

## 관련 JSON API 엔드포인트

Plug-in이 다루는 요소·강체 링크는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/ELEM` — Element](../../manual/03_DB_Node_Element.md)
- [`/db/RIGD` — Rigid Link](../../manual/05_DB_Boundary.md)

## 결론 (원문)

Line to Plate Converter Plug-in은 엔지니어가 단순 보 모델을 판 요소 모델로 손쉽게 변환할 수
있게 돕는다. 정렬, 보간, 메싱, 요소 생성, 강체 링크를 자동으로 처리해 모델링 노력을 줄이고
고급 해석에 정확하고 신뢰성 있는 결과를 제공한다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/60469083421593-Line-To-Plate-Converter](https://support.midasuser.com/hc/en-us/articles/60469083421593-Line-To-Plate-Converter)
