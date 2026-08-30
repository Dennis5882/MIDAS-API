# WallMarkAutoMapper 기획문서

> 영상(`docs/plugin_cases/videos/02_WallMarkAutoMapper.mp4`, 60fps, 3840×2160, 약 300초)을 10초
> 간격으로 프레임 캡처(총 30장) 후 프레임별 육안 분석 + 영상 내 자막(내레이션 캡션)을 근거로 작성.
> 원문 아티클(`docs/plugin_cases/articles/02_WallMarkAutoMapper.md`)의 4대 기능 설명과 교차 확인함.

## 1. 개요

**WallMarkAutoMapper**는 DXF 구조평면도에서 추출한 벽체명(Wall Mark) 텍스트와 좌표를, MIDAS GEN
NX 해석모델에 이미 부여되어 있는 Wall ID의 벽체 중심 좌표와 자동으로 매칭하여, 도면상의 벽체명을
해당 Wall ID의 Wall Mark로 일괄 부여·관리하는 Plug-in이다. 매칭 결과는 Preview 화면과 결과표에서
검토한 뒤 사용자가 선택한 항목만 모델에 반영한다.

## 2. 문제 정의

- GEN NX 기본 UI(`Modify Wall Mark Data`)는 Wall Mark 이름과 그에 속하는 Wall ID 목록
  (`WID_LIST`)을 사용자가 하나씩 직접 입력해야 한다.
- 벽식 구조 아파트처럼 벽체 수가 많아질수록(영상 예시 기준 벽 102개, Wall Mark 100개) 반복 입력
  시간이 길어지고, 누락·오타 등 실수 확률이 높아진다.
- 이미 입력된 항목을 수정하려 해도 목록을 스크롤하며 하나씩 찾아야 해서 전체 항목을 한눈에
  대조하기 어렵다.
- 영상 자막 기준 정량 효과: 수작업 시 벽체 100개 기준 약 50분(1건당 약 30초 가정: 도면 확인 +
  Wall ID 확인 + 입력) 소요 → Plug-in 사용 시 약 20분(설정 5분 + 결과 검토 약 13분 + 적용 확인
  2분)으로 약 **60% 시간 절감**.

## 3. 목표 사용자

- DXF 구조평면도와 GEN NX 해석모델을 함께 다루는 구조 설계자·모델링 담당자.
- 특히 벽체 수가 많은 벽식 구조(아파트 등) 프로젝트에서 Wall Mark(설계 표기명)를 반복적으로
  갱신해야 하는 사용자.

## 4. 핵심 컨셉 / 차별점

- **좌표 기반 자동 매칭**: 텍스트 완전일치가 아니라, DXF에서 추출한 Wall Mark 삽입 좌표와 GEN NX
  Wall ID의 중심 좌표 간 XY 직선거리를 계산해 가장 가까운 후보를 연결한다. 도면상의 벽체명이 GEN
  NX Wall ID와 이름이 달라도(예: 도면은 "HW5", 모델은 Wall ID 1) 위치 기준으로 매칭 가능.
- **3단계 신뢰도 분류(허용거리 × 75% 임계값)**: 사용자가 지정한 허용 거리를 기준으로 결과를
  OK/검토 필요/매칭 실패 3단계로 자동 분류해, 전수 검토가 아닌 예외 건 위주 검토가 가능하게 한다.
- **생성(생성) / 수정(수정) 2-모드**: 최초 일괄 부여용 "Wall Mark 생성" 모드와, 이미 부여된
  Wall Mark를 조회·수정·삭제하는 "Wall Mark 수정" 모드를 UI 상단 탭으로 분리.
- **Excel 왕복 편집 지원**: 결과표를 Excel로 내보내 대량 검토·수정 후 다시 가져와 반영 가능
  (검토 인력이 여러 명이거나 물량이 매우 많을 때 유용).
- **미리보기 확인 후 선택적 반영**: "적용 미리보기" 창에서 신규/수정/변경 없음/충돌·적용 불가 건을
  구분해 보여주고, 선택한 항목만 실제 모델에 반영한다 — 실수로 전체를 덮어쓰는 사고를 방지.

## 5. 워크플로우

### Step 0 — DXF 파일 준비 (사전 작업, GEN NX 밖에서)

- GEN NX 모델을 **AutoCAD DXF File**로 내보내기(`Export > AutoCAD DXF File`)한 뒤, 그 DXF 위에
  캐드 프로그램에서 벽체명(Wall Mark) 텍스트를 배치해 별도 레이어(영상 예시: `A-WALL_CENTERLINE`)로
  관리한다.
- ⚠️ 제약: 해석 모델과 도면의 스케일이 반드시 동일해야 하며(mm 단위 권장), 벽체명 텍스트는 벽체
  중심선에 인접하게 배치해야 매칭 정확도가 올라간다(자막: "벽체의 중심과 벽체명에 인접하게
  위치해야 매칭 결과의 정확도가 올라갑니다").

### Step 1 — API 연결 및 데이터 로드 (Wall Mark 생성 모드)

좌측 패널 3개 그룹:

| 그룹 | 필드 | 설명 |
| --- | --- | --- |
| API 설정 | 연결 버튼 | Mapi Key를 입력해 열려 있는 GEN NX 파일과 연결 |
| GEN NX 설정 | Load 층(드롭다운, 기본 "전체 층") | 매칭 대상 층 범위 선택 |
| GEN NX 설정 | Wall Type: MEMBRANE / PLATE (토글) | 매칭 대상 벽 요소 타입 선택 |
| GEN NX 설정 | "GEN NX 불러오기" 버튼 | 선택 조건으로 모델의 벽체 Node/Element 데이터 로드 |
| DXF 설정 | DXF 파일 불러오기 | 대상 DXF 파일 선택 (예: `Sample_Wallmark.dxf`) |
| DXF 설정 | Wall Mark 레이어(드롭다운) | 벽체명 텍스트가 있는 레이어 지정 (예: `A-WALL_CENTERLINE`) |
| 매칭 설정 | 매칭 허용 거리(mm, 기본값 1000) | OK/검토 필요/매칭 실패를 가르는 거리 기준 |

연결 후 작업 로그(좌측 하단)에 순서대로 표시되는 상태 메시지:
1. "GEN NX 연결 확인 완료. STOR 28개를 불러왔습니다."
2. "GEN NX 불러오기를 실행하세요."
3. "GEN NX 데이터 로드 완료: NODE 7461개, ELEM 7377개, STOR 28개, Load 층 전체 층, Wall 후보
   102개"

중앙 Wall Mark Preview에 로드된 벽체 형상(GEN NX Wall, 실선)이 표시된다(Marks 0 | Walls 102).

### Step 2 — 자동 매칭 실행

"▶ 자동 매칭 실행" 버튼 클릭 시:

- DXF의 Wall Mark 레이어에서 텍스트/좌표를 추출하고, GEN NX Wall ID별 중심 좌표와 비교해 매칭.
- 매칭 허용거리 기준 3단계 분류:

| 상태 | 조건 | 의미 |
| --- | --- | --- |
| OK | 거리 ≤ 허용거리 × 75% | 자동 매칭 성공으로 표시 |
| 검토 필요 | 허용거리 × 75% < 거리 ≤ 허용거리 | 허용 범위 안이지만 사용자 확인 필요 |
| 매칭 실패 | 허용거리 안에 사용 가능한 후보가 없음 | Wall ID를 자동 배정하지 않음 |

- 실행 후 로그: "101호.dxf에서 Wall Mark 100개를 매칭했습니다. 허용 거리 1000.0mm, 매칭 요약:
  OK 80개, 검토 필요 18개, 매칭 실패 2개"
- 하단 Summary Card에 총 Wall Mark 수(100개), 매칭 성공(80개, 80%), 검토 필요(18개, 18%), 매칭
  실패(2개, 2%)를 즉시 표시.
- 중앙 Preview는 기본적으로 "검토 필요"·"매칭 실패" 항목만 강조 표시하며, 마우스 휠로 확대/축소,
  드래그로 화면 이동하면서 도면과 대조 검토 가능. 범례: GEN NX Wall(회색 실선) / 매칭 성공(초록
  점선) / 검토 필요(주황 점선) / 미매칭(빨강 점선) / 마크 충돌(보라 점선).
- 우측 "자동 매칭 결과" 표: 컬럼 `적용(체크박스) | Wall Mark | Wall ID | 거리 | 상태`. 필터·정렬로
  검토 필요 항목만 골라볼 수 있고, 셀을 직접 클릭해 Wall Mark 이름을 인라인 수정 가능.

### Step 3 — 결과 적용

- 반영할 항목을 체크(개별 또는 "전체 선택")한 뒤 "Wall Mark 적용" 버튼 클릭 → **Wall Mark 적용
  미리보기** 모달 오픈.
- 모달 내 필터 탭: 전체 / 신규 / 수정 / 변경 없음 / 충돌·적용 불가. 표 컬럼:
  `구분 | Wall Mark | 변경 전 WID_LIST | 변경 후 WID_LIST | 상태/메모`.
- 안내 문구(자막): "결과표에서 선택한 Wall Mark만 GEN NX에 반영합니다. 해석 모델에 이미 적용되어
  있지만, 매칭 결과에 없는 Wall Mark는 변경하지 않습니다." — 즉 부분 적용을 해도 기존 미대상
  항목은 보존되는 non-destructive 반영 방식.
- "적용" 클릭 시 최종 반영, 로그에 "Wall Mark 수정내역 저장: 1건" 등으로 기록.

### Step 4 — Excel 왕복 편집(선택)

- "EXCEL 내보내기" → `DXF Wall Mark Auto Mapper — Review / Apply Excel Template v1` 형식의
  워크북 생성. 컬럼: `Apply | Story | Wall Mark(도면) | 최종 Wall Mark | Wall ID | Status |
  Dist. | Conf. | Note`.
- Excel 상에서 `Apply` 열(Y/N)로 반영 여부를 표시하고, `Status`가 `Review`(허용거리 내 검토 필요)
  또는 `Unmatched`(후보 없음)인 행은 `Note` 열에 사유가 자동 기재됨(예: "허용 거리 내 검토
  필요", "후보 없음").
- 수정된 Excel을 "EXCEL 가져오기"로 재반입하면 결과표에 반영되어, 대량 검토를 스프레드시트에서
  진행할 수 있다.
- PDF 결과표 출력 버튼도 별도 제공(보고/기록용, 상세 동작은 영상에 노출되지 않음).

### Step 5 — Wall Mark 수정 모드 (기존 Wall Mark 조회·수정·삭제)

상단 탭을 "Wall Mark 수정"으로 전환하면 좌측 설정 패널은 생성 모드와 동일(API/GEN NX 설정)하되,
동작이 다르다:

- 로그: "GET db/WMAK 조회 검증이 진행되었습니다" → "모드 전환: 작업 데이터를 초기화했습니다" →
  "수정 모드 불러오기 완료: Wall 후보 102개, Wall Mark 87개"
- 우측 "Wall Mark 수정" 표: 컬럼 `선택 | 상태(변경 없음/변경/삭제 등) | Wall Mark | WID_LIST |
  변경 전 WID_LIST`. 이미 모델에 저장된 Wall Mark를 그대로 불러와 편집 가능한 그리드로 표시.
- 표 안에서 마우스 우클릭 시 컨텍스트 메뉴로 "행 추가 / 행 삭제 / 행 삭제 취소" 가능 — 즉 특정
  Wall Mark에 Wall ID를 추가·제외하거나 Wall Mark 자체를 삭제하는 것도 이 화면에서 처리.
- Preview 범례도 생성 모드와 다르게 GEN NX Wall / 변경 / 삭제 / NG 4종으로 구성.
- "Wall Mark 적용" 버튼으로 생성 모드와 동일하게 미리보기 → 최종 반영.

## 6. 연계 JSON API 엔드포인트

영상 내 작업 로그에 명시적으로 노출된 API 호출/데이터 대상 기준:

| 시점 | 로그 문구 | 추정 API | 문서 위치 |
| --- | --- | --- | --- |
| 연결 직후 | "STOR 28개를 불러왔습니다" | `GET /db/STOR` | [`02_DB_Project_Structure.md#14-dbstor--story-data`](../../manual/02_DB_Project_Structure.md#14-dbstor--story-data) |
| GEN NX 불러오기 | "NODE 7461개, ELEM 7377개... 불러왔습니다" | `GET /db/NODE`, `GET /db/ELEM` | [`03_DB_Node_Element.md#1-dbnode`](../../manual/03_DB_Node_Element.md#1-dbnode), [`03_DB_Node_Element.md#2-dbelem`](../../manual/03_DB_Node_Element.md#2-dbelem) |
| 수정 모드 진입 | "GET db/WMAK 조회 검증이 진행되었습니다" | `GET /db/WMAK` | [`24_DB_Design.md#9-dbwmak--modify-wall-mark-design-벽체-마크-설계-수정`](../../manual/24_DB_Design.md#9-dbwmak--modify-wall-mark-design-벽체-마크-설계-수정) |
| Wall Mark 적용 | "Wall Mark 수정내역 저장" | `POST /db/WMAK` (신규/변경분), 필요 시 `PUT`/`DELETE` | 위와 동일 |

- ⚠️ `/db/WMAK`의 공식 스키마는 `{"WMAK": {"<ID>": {"MARKNAME": "...", "WID_LIST": [...]}}}`
  구조이며, 영상의 결과표·수정 테이블에 표시되는 `Wall Mark`/`WID_LIST`/`변경 전 WID_LIST` 컬럼
  명칭이 이 스키마의 `MARKNAME`/`WID_LIST`와 정확히 대응된다 — 다른 8개 Plug-in과 달리 이 건은
  화면 로그에 실제 엔드포인트 이름(`db/WMAK`)이 텍스트로 노출되어 있어 추정이 아니라 확인된
  근거다.
- Wall ID별 중심 좌표 계산에 필요한 벽체 요소 선별(Wall Type: MEMBRANE/PLATE) 로직은 화면에
  드러나지 않아 정확한 필터링 방식(예: `/db/ELEM`의 `TYPE` 필드 활용 여부)은 확인되지 않았다.

## 7. 입력 데이터 규격

- **DXF 파일**: GEN NX에서 `Export > AutoCAD DXF File`로 내보낸 뒤, 벽체명 텍스트(TEXT/MTEXT)를
  별도 레이어에 추가한 파일. 해석 모델과 동일 스케일(mm 권장), 원점 좌표계 일치가 전제.
- **Wall Mark 레이어**: DXF 내 벽체명 텍스트가 위치한 레이어명을 UI에서 지정(예:
  `A-WALL_CENTERLINE`).
- **매칭 허용 거리**: mm 단위, 사용자가 직접 입력(영상 기본값 1000mm).
- **GEN NX 모델**: 이미 Wall ID가 부여된 벽 요소(Membrane 또는 Plate)를 포함해야 함.

## 8. 출력 / 생성 결과

- GEN NX 모델의 `/db/WMAK` 데이터(Wall Mark ↔ Wall ID 목록 매핑) 갱신.
- Excel 결과표(`.xlsx`) — 검토·승인 이력 관리용.
- PDF 결과표 — 보고용 출력.

## 9. 제약사항 및 한계

- 매칭은 순수 좌표 거리 기준이므로, 벽체명 텍스트가 벽체 중심에서 멀리 떨어져 배치되거나 여러
  벽체가 허용거리 내에 밀집한 경우 "검토 필요"/"매칭 실패"가 늘어난다 — 완전 자동화가 아니라
  자동 매칭 + 사람 검토를 전제로 설계됨.
- 해석 모델과 DXF 도면의 스케일·원점이 다르면 매칭 자체가 성립하지 않는다(사전 준비 단계의 필수
  전제).
- "Wall Mark 적용" 시 결과표에 없는 기존 Wall Mark는 변경되지 않는 partial-update 방식이라,
  전체 재동기화가 필요한 경우 별도로 "Wall Mark 수정" 모드에서 전체 삭제 후 재생성하는 등의
  추가 작업이 필요할 수 있음(영상에 직접 언급되지는 않았으나 UI 동작상 유추됨 — ⚠️ 확인 필요).

## 10. 화면 인벤토리

| 시점(초) | 화면 내용 |
| --- | --- |
| 0–10 | 인트로 타이틀(제목/한 줄 소개) |
| 20–50 | 01·WHY — 기존 수작업 방식의 3가지 불편(개별 입력, WID_LIST 직접 작성, 전체 비교 어려움) |
| 60–100 | 02·SOLUTION — 4단계 프로세스(DXF → GEN NX → MATCH → APPLY) 및 매칭 상태 판정 기준(75%) 설명 |
| 110 | Wall Mark Auto Mapper 실제 UI 최초 진입(연결 전 상태) |
| 120–140 | 좌측 설정 영역 구조 설명, API 연결(Mapi Key) |
| 140–170 | GEN NX 데이터 로드 완료, DXF 파일 생성 방법(AutoCAD Export) 안내 슬라이드 |
| 180–230 | 자동 매칭 실행 → Summary Card, Preview 필터링, 결과표 검토 |
| 230–250 | Wall Mark 적용 미리보기 모달, Excel 내보내기(엑셀 템플릿 화면) |
| 250–280 | Wall Mark 수정 모드: 로드, 표에서 인라인 편집, 우클릭 행 추가/삭제, 적용 |
| 280–300 | 04·IMPACT — 기대 효과 요약(50분 → 20분, 약 60% 절감) |

---

*다음: 03_VibrationAnalysisAssistant 영상 분석 및 기획문서 작성.*
