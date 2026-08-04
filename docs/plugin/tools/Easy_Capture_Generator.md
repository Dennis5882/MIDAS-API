# Easy Capture Generator

> **원문:** [Easy Capture Generator](https://support.midasuser.com/hc/en-us/articles/35639906272025-Easy-Capture-Generator)
> ("Plug-in Item" 목록에는 동일 URL에 대한 별칭으로 "Image Capture Generator"도 함께
> 나열되어 있다.)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

인쇄(출력) 설정을 데이터베이스(DB) 형식으로 저장해 손쉽게 출력할 수 있게 해주는 Plug-in이다.
하나의 DB에 여러 설정을 저장할 수 있고, 구성한 내용을 여러 형식으로 출력할 수 있다.

- 인쇄 설정을 DB 형식으로 저장
- 하나의 DB에 여러 설정을 쉽게 저장·관리
- 다중 인쇄 지원

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

기존에는 인보이스나 보고서를 만들 때마다 인쇄 설정을 반복 입력해야 했고, 모델링이 바뀌거나
출력 결과가 만족스럽지 않으면 다시 작업하는 데 많은 시간이 들었다. 이 Plug-in을 쓰면 사용자가
구성한 설정을 저장해두고 모델링이 바뀌어도 재구성 없이 사용할 수 있다. 또한 비슷한 설정을
그룹화해 여러 하중케이스에 적용할 수 있어 작업 속도를 높이고 출력을 표준화하며 사용자 오류를
줄인다.

- 반복적인 설정 입력을 최소화해 작업 시간 단축
- 다중 출력을 지원해 불필요한 인쇄 시간 절감
- 미리 구성된 입력값을 사용해 사용자 오류 감소

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | DB 탭에서 저장할 DB 선택. Components는 다중 선택 가능, 나머지 옵션은 단일 선택만 가능 |
| 2 | **Save** 버튼을 눌러 저장하고 File List Work Tree에서 입력 정보 확인 |
| 3 | 필요 시 저장할 DB를 추가로 선택 |
| 4 | DB 정보 저장이 끝나면 Type of Display 탭으로 이동 |
| 5 | DB 탭과 동일한 방식으로 옵션 선택 |
| 6 | 저장 버튼 클릭 |
| 7 | View 탭으로 이동 |
| 8 | 원하는 설정을 선택·저장. Active Type에 따라 아래와 같이 설정 |
| 9 | **Active All**: 전체 모델링을 출력 |
| 10 | **Active by Node/Element**: 모델링에서 선택한 부분만 출력. 출력할 요소를 모델에서 선택한 뒤 Plug-in에서 **Active by Node/Element** 선택 |
| 11 | **Active Identity**: Structure Group에 정의된 부분을 출력. 출력할 그룹을 목록에서 선택 |
| 12 | DB/Type of Display/View 정보 저장이 끝나면 **Download** 버튼으로 JSON 형식으로 저장 가능 |
| 13 | Print 탭으로 이동해 File List에서 저장된 DB 확인 |
| 14 | Plug-in 실행 후 사용자가 최근 입력한 정보는 Current에 저장됨. 이전에 저장한 DB를 쓰려면 **Add File** 버튼으로 파일을 불러옴 |
| 15 | 출력할 파일을 선택하고 **Select Load Case** 버튼 클릭 |
| 16 | Load Case 선택 창이 열리면 출력할 Load Case 선택(다중 선택 가능) |
| 17 | 선택한 Load Case를 저장하려면 **Download** 버튼으로 JSON 형식으로 저장. 저장된 DB를 다른 모델링에서 불러오면 존재하지 않는 Load Case 이름은 출력되지 않음 |
| 18 | Load Case 입력이 끝나면 저장 버튼으로 저장 |
| 19 | Plug-in 우측 Print File Work Tree에서 저장된 파일 확인 |
| 20 | **Print Size** 버튼으로 출력 크기 입력(사용자 컴퓨터 환경에 맞춰 픽셀 단위로 조정) |
| 21 | 크기 입력 후 인쇄(print) 버튼 클릭 |

## 관련 JSON API 엔드포인트

Plug-in이 다루는 View/Type of Display/Active 설정은 `docs/manual`의 다음 엔드포인트와
대응된다.

- [`/view/CAPTURE` — Capture](../../manual/16_VIEW.md)
- [`/view/DISPLAY` — Display](../../manual/16_VIEW.md)
- [`/view/ACTIVE` — Active](../../manual/16_VIEW.md)

## 결론 (원문)

이 가이드를 통해 구조 모델링 프로젝트에서 인쇄 관련 설정을 손쉽게 저장·관리하고, 필요한
정보를 빠르게 출력할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35639906272025-Easy-Capture-Generator](https://support.midasuser.com/hc/en-us/articles/35639906272025-Easy-Capture-Generator)
