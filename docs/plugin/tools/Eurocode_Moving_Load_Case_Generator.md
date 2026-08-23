# Eurocode Moving Load Case Generator

> **원문:** [Eurocode Moving Load Case Generator](https://support.midasuser.com/hc/ko/articles/61259043302041-Eurocode-Moving-Load-Case-Generator)
> **원문 작성:** 2026-08-18 · **원문 최종 편집:** 2026-08-18

---

## 개요

EN 1991-2 교통하중은 엔지니어링 작업이기 전에 긴 타이핑 작업이다. Load Model 1만 해도
명목차선마다 값이 달라지는 tandem system과 UDL을 각각의 보정계수와 함께 다뤄야 하고, Load
Model 2는 별도의 단축하중, Load Model 3은 동시에 하나만 재하 가능한 특수차량 세트이며,
여기에 cl 4.6의 피로하중모델과 Section 6의 철도하중모델은 포함되지도 않는다. 이 모든 하중은
MIDAS에서 차량(vehicle)으로 만든 뒤 올바른 차선·명목차선 번호·계수를 갖는 이동하중 케이스로
다시 연결해야 하며, 차선이 하나만 바뀌어도 전체를 다시 만들어야 한다. **Eurocode Moving
Load Generator**는 이 작업을 대신한다 — 열린 모델에서 교통차선을 읽고, Table 4.4a의 교통
하중군(traffic load group)을 출발점으로 삼아 그로부터 파생되는 차량과 이동하중 케이스를
생성한다.

## 지원 버전

`MIDAS CIVIL NX 2026 (v2.2)` — Plug-in 버전 `1.0.0`

## 주요 기능

- **하중군을 1차 입력으로:** EN 1991-2 Table 4.4a의 gr1a·gr1b·gr3·gr4·gr5를 1차 선택
  대상으로 삼고, cl 4.5.1에 따라 상호 배타적으로 처리 — 하중군을 고르면 그것이 포함하는
  하중모델이 함께 체크되어 둘이 어긋나지 않음.
- **EN 1991-2 전체 커버:** Section 4의 Load Model 1~4·보도하중, cl 4.6의 피로하중모델
  FLM1~4, Section 6의 LM71·SW/0·SW/2·HSLM-A·HSLM-B까지 — 도로·피로·철도 모델을 한 번에
  또는 개별적으로 생성 가능.
- **국가결정변수(NDP)를 계수로 처리:** MIDAS는 이동하중 코드로 단일 EUROCODE 항목만 갖고
  있어(국가별 목록이 아님), 유일한 분기는 LM3 특수차량 세트(UK NA SV/SOV 또는 EN Annex A
  모델)뿐 — 나머지 보정계수는 일반 숫자값이라 어떤 부속서든 계수 편집만으로 표현 가능하며
  일반적인 값에는 프리셋 제공.
- **Characteristic·Frequent 값 모두 생성 가능:** EN 1990 Table A2.1의 ψ 계수를 차량에
  기록하고, 대표값(frequent/characteristic/둘 다)에 따라 케이스를 생성 — 어떤 값인지 하중
  케이스 이름에 표기.
- **명목차선 번호를 한 번만 부여:** 모델의 각 교통차선에 역할(도로차선/보도/잔여영역/
  철도)을 지정하면 도로차선은 cl 4.2.3의 명목차선 번호를 받고, 그 번호가 Table 4.2 행과
  보정계수를 결정 — Lanes 탭에서 결과값을 기록 전에 확인 가능.
- **철도차선을 도로차선과 분리:** MIDAS는 Eurocode에서 철도차선과 도로차선을 같은 다이얼로그로
  같은 목록에 저장해 구분이 없으므로, Track 역할로 이를 구분 — 차선이 지정되지 않은 철도
  케이스는 무재하로 조용히 기록되는 대신 생성을 거부.
- **철도 조합 데이터까지 기록:** cl 6.8.1 Table 6.11의 하중 트랙 수별 ψ1 계수와 다중재하
  계수를 MIDAS Railway Bridge Data에 기록(ψ0은 MIDAS가 조합 생성 시 0.8로 고정하므로 별도
  입력 없음).
- **생성 불가 항목을 명시:** 표준 축하중 세트가 없는 피로하중모델 5(FLM5)와, 정적하중으로
  분류되는 cl 4.4의 제동·가속·원심력이 본질인 gr2는 조용히 생략하지 않고 생성 불가 사유를
  명시.
- **기록 전 미리보기 및 dry run:** 모든 차량·케이스를 관련 조항과 함께 나열하고, Dry run으로
  모델을 건드리지 않고 실제 전송될 payload를 미리 구성 가능.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | CIVIL NX에서 교량 모델을 열고 Plug-in 실행 — 연결 정보는 자동 설정 |
| 2 | **Model** 탭에서 Read model — 이동하중 코드, 교통차선, 기존 차량·이동하중 케이스를 보고. 코드가 Eurocode가 아니면 MIDAS Load > Moving Load > Moving Load Code에서 설정 후 다시 읽어야 함 |
| 3 | **Load models** 탭에서 적용할 EN 1991-2 항목을 고르고 교통 하중군을 체크 — 하중군이 필수로 요구하는 하위 모델은 잠금 표시되고 나머지는 해제 가능(보도하중이 없는 교량에서 해당 항목만 해제 등). 개별 하중모델별 케이스 생성 옵션도 있으나 기본값은 꺼짐 |
| 4 | **Lanes** 탭에서 모든 차선에 역할(도로차선/보도/잔여영역/철도) 부여, 잔여영역 재하 여부와 MIDAS 최적화(어느 차선을 재하할지 자동 선택) 여부 결정. 하단 표에서 보정계수 적용 후 각 차선의 LM1 값을 확인 |
| 5 | 이름 규칙 설정 — 하중모델·MIDAS 하위타입·하중군·대표값·일련번호를 조합해 사람이 읽을 수 있는 이름으로 생성, 동일 이름 기존 케이스 처리 방식도 여기서 결정 |
| 6 | **Factors** 탭에서 국가부속서(NDP) 프리셋 선택 후 명목차선별 tandem·UDL 보정계수, 잔여영역 계수, LM2용 betaQ, LM3 특수차량 세트, ψ 조합계수, 철도 classification factor 및 Railway Bridge Data 확인/수정. 생성할 대표값(frequent/characteristic/둘 다) 체크 |
| 7 | Preview 검토 — 생성될 모든 차량·이동하중 케이스를 관련 EN 1991-2 조항과 함께 확인, 문제 항목과 확인이 필요한 항목이 구분되어 표시 |
| 8 | **Generate** 탭에서 Dry run(전송 없이 payload만 구성) 또는 Write to model(실제 기록) 선택. 로그는 모든 기록 내용을 남기며, 내장 payload로 대체 생성된 항목은 별도 표시 |

## 참고/제약사항

- 피로하중모델 5(FLM5)는 표준 축하중 세트가 없어 생성되지 않음.
- gr2(제동·가속·원심력)는 정적하중으로 분류되어 이동하중 케이스로 생성되지 않음.
- 철도 케이스는 반드시 차선(Track 역할)이 지정돼야 하며, 지정되지 않으면 생성이 거부됨.
- ψ0는 MIDAS가 하중조합 생성 시 자동으로 0.8을 적용하므로 Plug-in에서 별도로 입력받지 않음.
- 이동하중 코드가 Eurocode가 아닌 모델에는 기록을 거부.

## 관련 JSON API 엔드포인트

Plug-in이 생성하는 차량과 이동하중 케이스는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/MVHL` — Vehicles](../../manual/08_DB_Moving_Loads.md)
- [`/db/MVLDeu` — Moving Load Cases – Eurocode](../../manual/08_DB_Moving_Loads.md)

## 결론 (원문)

Eurocode Moving Load Generator는 EN 1991-2 평가에서 느리고 기계적인 부분 — 모든
하중모델·특수차량마다 차량을 만들고, 각각에 차선·명목차선 번호·보정계수·대표값을 갖춘
이동하중 케이스를 만드는 작업 — 을 제거한다. 남는 것은 엔지니어링 판단이다: 구조물이 받아야
할 교통 하중군, 적용할 국가부속서 값, 결과의 의미 — 모델에 기록되기 전 모든 생성 항목이
근거 조항과 함께 목록으로 제시된다.

## 원문 링크

[https://support.midasuser.com/hc/ko/articles/61259043302041-Eurocode-Moving-Load-Case-Generator](https://support.midasuser.com/hc/ko/articles/61259043302041-Eurocode-Moving-Load-Case-Generator)
