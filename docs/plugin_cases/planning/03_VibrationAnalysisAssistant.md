# VibrationAnalysisAssistant 기획문서

> 영상(`docs/plugin_cases/videos/03_VibrationAnalysisAssistant.mp4`, 30fps, 3840×2160, 약 285초)을
> 10초 간격으로 프레임 캡처(총 29장) 후 프레임별 육안 분석 + 영상 내 자막(내레이션 캡션)을 근거로
> 작성. 원문 아티클(`docs/plugin_cases/articles/03_VibrationAnalysisAssistant.md`)의 4대 기능
> 설명과 교차 확인함.

## 1. 개요

**Vibration Analysis Assistant**는 MIDAS GEN NX 해석모델에서 슬래브·보 부재의 보행하중 진동
검토에 필요한 Time History Function(시간이력 함수), Time History Load Case(시간이력 하중
케이스), Dynamic Nodal Load(동적 절점 하중) 3종 입력을 한 화면에서 입력·검토·적용하는 Plug-in
이다. 그래프와 표로 하중 특성을 실시간 확인한 뒤 GEN NX API로 모델에 반영한다.

## 2. 문제 정의

- GEN NX 기본 UI에서는 Time History Function(하중 함수), Time History Load Case(해석 케이스),
  Time History Analysis Data(동적 절점 하중) 입력이 각각 별개의 창(`Add/Modify/Show Time History
  Functions`, `Add/Modify Time History Load Cases`, `Time History Analysis Data`)으로 나뉘어
  있어, 사용자가 여러 창을 오가며 관련 변수를 입력·대조해야 한다.
- 입력값을 바꿔도 그 결과(하중 시간함수 형태, 피크값 등)를 바로 확인할 방법이 없어, 잘못된
  `Time Step`이나 `Repeat` 값이 실제 모델 반영 전까지 발견되지 않을 위험이 있다.
- 여러 창을 오가는 과정에서 Node 번호, 하중 방향, 시간 간격 등에 입력 오류가 발생하기 쉽다.

## 3. 목표 사용자

- 바닥판/보 부재의 보행하중(사용성) 진동 검토를 수행하는 구조 엔지니어.
- IABSE(국제교량구조공학협회) 기준의 Heel Drop-Walking Continuous 보행하중 함수를 반복적으로
  다양한 조건(보행 주파수, 감쇠비, 하중 노드 등)으로 적용해야 하는 실무자.

## 4. 핵심 컨셉 / 차별점

- **단일 화면 통합 입력**: Time History Function / Damping(Modal) / Dynamic Nodal Loads /
  Time History Load Case 4개 입력 그룹을 하나의 화면에 배치하고, 그 아래 실시간 미리보기
  그래프·표를 붙여 컨텍스트 전환 없이 작업할 수 있게 한다.
- **실시간 하중함수 미리보기(Walking Load Preview)**: `G`, `Walking Frequency fs`, `Time Step`,
  `Repeat` 등 입력값을 바꾸는 즉시 우측 `Time Function Graph`와 `Time Function Table`이
  동기화되어, Peak 하중·지속시간(Duration)·반복 횟수(Steps)를 바로 확인할 수 있다. 모델 반영
  전에 오류를 미리 발견하는 것이 핵심 가치.
- **하중 타입 고정**: 이 Plug-in은 IABSE 보행하중 함수 중 **Heel Drop-Walking
  Continuous(IABSE)** 한 가지 타입만 지원하도록 범위를 고정해, 입력 항목을 보행하중 검토에
  필요한 최소 집합으로 단순화했다.
- **적용 후 재조회 검증**: API로 GEN NX에 반영한 뒤 곧바로 재조회하여 실제 모델에 정상 반영됐는지
  확인하는 절차가 워크플로에 포함되어 있다.

## 5. 워크플로우

### Step 1 — API 연결

- 좌측 상단 "API 설정" 버튼 클릭 → Base URL과 MAPI-Key 입력 모달.
- 우측 상단 상태 배지 4단계: `GEN NX Disconnected`(연결 안 됨, 빨강) / `Connection failed`(연결
  실패, MAPI-Key 확인 필요) / `Checking...`(연결 중) / `GEN NX Connected`(연결 완료, 초록).

### Step 2 — 4개 입력 그룹 작성

화면은 좌측부터 4개 패널로 구성:

| 패널 | 필드 | 설명 |
| --- | --- | --- |
| **Time History Function** | Function Name | 시간이력 함수 이름 |
| | Scale Factor | 생성된 하중 시간함수에 적용할 배율 |
| | G (kN) | 보행하중 산정에 사용하는 기준 하중 |
| | Walking Frequency fs (Hz) | 보행 주파수 |
| | Time Step (sec) | 하중 시간함수 생성 간격 |
| | Repeat | 보행하중 반복 횟수 |
| **Time History Load Case** | Name | Load Case 이름 |
| | Description | 해석 케이스 설명 |
| | Analysis Type | Linear / Nonlinear |
| | Analysis Method | Modal / Direct Integration |
| | Time History Type | Transient / Periodic |
| | End Time (sec) | 해석 종료 시간 |
| | Time Increment (sec) | 해석 시간 간격 |
| | Step Number Increment for Output | 출력 스텝 배수 |
| **Damping - Modal** | Damping Ratio | 전체 모드에 적용할 감쇠비 |
| | Table – Mode / Damping Ratio (+/− 버튼) | 개별 모드별 감쇠비 추가·삭제 |
| **Dynamic Nodal Loads** | Node No. | 동적 절점하중을 적용할 Node 번호 |
| | THLC Name | 하중을 적용할 Time History Load Case 선택 |
| | Option | ADD / Replace / Delete |
| | Function Name | 적용할 Time History Function 선택 |
| | Direction | X / Y / Z |
| | Arrival Time | 동적하중이 시작되는 시간 |
| | Scale Factor | 절점하중에 적용할 배율(음수 입력 시 하중 방향 반전) |

### Step 3 — 실시간 미리보기 확인

- 우측 하단 **Walking Load Preview**에 `Time Function Graph`(꺾은선)와 `Time Function Table`
  (Time/Load 값 목록)이 항상 동기화 표시.
- 상단에 `Peak`(최대 하중), `Duration`(지속시간), `Steps`(스텝 수) 3개 요약값 표시.
- 영상 시연: `Repeat`를 1 → 10으로 바꾸자 그래프가 단일 파형에서 10회 반복 파형으로, Duration이
  0.5초 → 5.0초로, Steps가 1.0 → 10.0으로 즉시 갱신됨. `Time Step`을 0.0050 → 0.0010초로,
  `End Time`을 8초 → 20초로 조정하는 등 여러 파라미터를 실시간으로 조정하며 확인.
- `Scale Factor`(Dynamic Nodal Loads 쪽)를 1.000 → −1.000으로 바꾸면 Peak 값 부호가
  +0.908 kN → −0.908 kN으로 반전되는 것도 실시간 반영됨 — 하중 재하 방향 검증에 활용 가능.

### Step 4 — GEN NX 적용 및 검증

- 모든 입력을 검토한 뒤 "GEN NX 적용" 버튼 클릭.
- 하단 로그에 적용 결과 요약: "적용 완료 (ADD): THFC #1, THIS #1, THNL 1개 node 반영" — 이
  로그 문구가 실제 호출된 API 엔드포인트 이름(THFC/THIS/THNL)을 그대로 노출.
- 이어서 실제 GEN NX 프로그램 화면(Tree Menu)으로 전환해 반영 결과를 재조회: `Time History
  Analysis > Time History Load Cases`(Case 1: Walking_TH_01), `Time Forcing Functions`
  (Function 1: Walk-cont(IABSE)), `Dynamic Nodal Loads`(Type 1: LoadCase=Walking_TH_01,
  Function=Walk-cont(IABSE))가 모두 트리에 생성된 것을 확인 — "정상적으로 반영되었는지를
  확인합니다"라는 내레이션과 함께 재조회 검증 단계가 워크플로에 명시적으로 포함됨.

## 6. 연계 JSON API 엔드포인트

인트로 슬라이드에 "GEN NX API: THFC · THIS · THNL"로 명시되어 있고, 적용 완료 로그에도 동일한
3개 코드가 그대로 노출되어 — 이 3건은 추정이 아니라 화면에 직접 확인된 근거다.

| 입력 그룹 | 엔드포인트 | 문서 위치 |
| --- | --- | --- |
| Time History Function | `/db/THFC` | [`09_DB_Dynamic_Loads.md#8-dbthfc--time-history-functions`](../../manual/09_DB_Dynamic_Loads.md#8-dbthfc--time-history-functions) |
| Time History Load Case | `/db/THIS` | [`09_DB_Dynamic_Loads.md#6-dbthis--time-history-load-cases`](../../manual/09_DB_Dynamic_Loads.md#6-dbthis--time-history-load-cases) |
| Dynamic Nodal Loads | `/db/THNL` | [`09_DB_Dynamic_Loads.md#10-dbthnl--dynamic-nodal-loads`](../../manual/09_DB_Dynamic_Loads.md#10-dbthnl--dynamic-nodal-loads) |

- ⚠️ 3개 엔드포인트 모두 GET/POST/PUT/PUT-with-id/DELETE/DELETE-with-id를 지원하며, Plug-in의
  `Option`(ADD/Replace/Delete) 필드는 이 CRUD 동작(주로 POST=ADD, PUT=Replace, DELETE=Delete)에
  대응되는 것으로 보이나, 화면상 실제 HTTP 메서드까지는 노출되지 않아 정확한 매핑은 추정이다.
- Modal Damping(감쇠비) 입력이 `/db/THIS`의 요청 바디 내 감쇠 관련 필드로 들어가는지, 별도
  엔드포인트가 있는지는 화면상 확인되지 않았다.

## 7. 입력 데이터 규격

- **하중 함수 타입**: Heel Drop-Walking Continuous(IABSE) 고정 — 다른 IABSE 보행하중 타입(예:
  Heel Drop 단독)은 이 Plug-in에서 지원하지 않음.
- **적용 대상**: 실제 GEN NX 모델에 존재하는 Node 번호(Dynamic Nodal Loads의 Node No.).
- **필수 수치 입력**: G(kN), Walking Frequency(Hz), Time Step(sec), Repeat, End Time(sec),
  Time Increment(sec), Damping Ratio, Arrival Time(sec), Scale Factor.

## 8. 출력 / 생성 결과

- GEN NX 모델의 `/db/THFC`(시간이력 함수), `/db/THIS`(시간이력 하중 케이스), `/db/THNL`(동적
  절점하중) 데이터 생성.
- 화면상 그래프·표 형태의 하중 함수 미리보기(모델에는 저장되지 않는 검토용 산출물).

## 9. 제약사항 및 한계

- 지원 하중 타입이 Heel Drop-Walking Continuous(IABSE) 하나로 고정되어 있어, 다른 보행하중
  기준(예: 특정 국가 기준의 별도 시간함수)을 적용하려면 이 Plug-in의 범위 밖이다.
- Damping은 Modal(모드별 감쇠비) 방식만 화면에 노출되며, Direct Integration 해석에서 흔히
  쓰이는 Rayleigh 감쇠 등 다른 감쇠 정의 방식은 영상에서 확인되지 않았다.
- 적용은 ADD/Replace/Delete 옵션 기준 1개 Node·1개 Function·1개 Load Case 단위로 진행되는
  것으로 보이며, 여러 Node에 동일 조건을 일괄 적용하는 배치 기능은 영상에서 확인되지 않았다
  (⚠️ 미확인).

## 10. 화면 인벤토리

| 시점(초) | 화면 내용 |
| --- | --- |
| 0–10 | 인트로 타이틀(제목/한 줄 소개, GEN NX API: THFC·THIS·THNL) |
| 20–30 | 01·WHY — 기존 GEN NX 3개 입력창(Time History Function/Load Case/Analysis Data)이 분리되어 있는 문제 |
| 30–110 | 02·CHALLENGE — Plug-in 전체 UI 개요(좌: 입력 4패널, 우: Walking Load Preview) |
| 120–170 | 03·UI — API 설정(연결 배지 4단계), THF·THLS 필드별 설명, Damping·Dynamic Nodal Loads 필드별 설명 |
| 180–230 | 실제 프로그램 시연: Repeat/Time Step/End Time 값 변경 → 그래프·표 실시간 갱신, Scale Factor 음수 반전 |
| 230–240 | GEN NX 적용 → 로그(THFC #1, THIS #1, THNL 1개 반영) → GEN NX 프로그램에서 Tree Menu 재조회 검증 |
| 250–285 | 04·IMPACT — 적용 기대 효과(입력 시간 단축·오류 감소·검토 편의 향상) |

---

*다음: 04_AutoGenerationCmFactor 영상 분석 및 기획문서 작성.*
