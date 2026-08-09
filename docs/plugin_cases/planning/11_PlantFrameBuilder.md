# PlantFrameBuilder 기획문서

> 영상(`docs/plugin_cases/videos/11_PlantFrameBuilder.mp4`, 30fps, 1920×1080, 약 165초)을 6초
> 간격으로 프레임 캡처(총 28장) 후 프레임별 육안 분석 + 자막을 근거로 작성. 원문
> 아티클(`docs/plugin_cases/articles/11_PlantFrameBuilder.md`)의 2대 기능 설명과 교차 확인함.
> "GENERATE READINESS" 체크리스트와 "GENERATE COMPLETE MODEL" 진행 로그가 화면에 그대로
> 노출되어, 생성 파이프라인의 단계 구성을 매우 구체적으로 확인할 수 있는 사례.

## 1. 개요

**Plant Frame Builder**는 Bay 간격·층고 등 입력값만으로 2열 다층 Pipe Rack(플랜트 배관
지지 구조물)의 초기 구조해석용 철골 Frame 모델(Node/Column/Beam/Brace/Support)을 자동
생성하는 GEN NX API Plug-in이다.

## 2. 문제 정의

- 수십·수백 개의 Node와 Element를 하나씩 손으로 그리는 기존 방식은 번거롭다.
- CAD에서 DXF로 골조를 그려 GEN NX로 Import해도, 형상을 바꿀 때마다(Bay 수, 층수, 간격 등)
  처음부터 다시 반복해야 하는 왕복 작업이 발생한다.
- 기존 GEN NX 방식(Copy/이동 반복으로 층 쌓기)도 반복 작업이며, 형상 변경 시 재작업 비용이
  크다.

## 3. 목표 사용자

- 플랜트(석유화학·발전 등) 프로젝트에서 배관 지지용 Pipe Rack 골조를 초기 구조해석 모델로
  빠르게 만들어야 하는 구조 엔지니어.
- 여러 형상 대안(Bay 수, 층수, 브레이스 배치 등)을 반복 비교 검토해야 하는 초기 설계 단계
  실무자.

## 4. 핵심 컨셉 / 차별점

- **파라미터 입력 → 실시간 3D 미리보기 → 클릭 한 번, 수십 초 만에 생성**: CAD 없이 GEN NX
  안에서 바로 Bay 수·간격, Rack 폭, Level 수·층고 같은 파라미터만 조정하면 우측 "구조
  미리보기"가 즉시 갱신되고, 최종적으로 버튼 한 번으로 전체 모델이 생성된다.
- **기존 모델의 Material/Section 재사용 + 신규 정의 동시 지원**: "데이터 가져오기"를 누르면
  현재 GEN NX 모델에 이미 정의된 Material(#1 Frame)·Section 7종이 그대로 드롭다운에 채워져
  재사용할 수 있고, 동시에 "+ 신규 Steel Material 정의"/"+ DB Section 추가"로 그 자리에서
  새 재료·단면을 정의해 "생성 예정 목록"에 추가할 수도 있다(즉시 생성하지 않고 최종 Generate
  Complete Model 실행 시 일괄 생성).
- **부재 종류별 독립 단면 배정**: Column, Trans.(횡) Beam, Long.(종) Beam, Brace 4종 부재에
  각각 다른 단면을 배정 가능. X-Brace 토글로 브레이스 사용 여부를 켜고, Brace Bay를 Bay
  1/3/5/7...처럼 개별적으로 선택해 가새를 넣을 위치를 직접 고를 수 있다.
- **지점 조건 3종(Fixed/Pinned/None)**: 지지 조건을 절점 구속 방식으로 선택.
- **상세 설정(원점, 기준 레벨, ID 할당)**: Origin X/Y, Base Elev. Z, Brace를 넣을 Level을
  개별 체크, 자동 ID 할당(Node/Element 채번 최댓값+1 규칙) 등 세부 옵션을 "상세 설정 펼치기"
  로 노출.
- **VALIDATE & PREVIEW → GENERATE READINESS 2단계 사전 검증**: 생성 직전 입력값 전체를
  요약 표(Unit, Material 배정, Section 배정, Column/Beam/Brace 단면 등)로 한눈에 정리하고,
  이어서 예상 생성 수량(Node/Column/Beam/Brace 개수와 정확한 ID 범위, 예: Column ID 1~160,
  Brace ID 391~550)까지 미리 계산해 보여준다. "GENERATE READINESS" 체크리스트(모델 데이터
  조회/Unit 조회/Material 배정/Section 배정/이름 충돌 없음/입력 검증/모델 충돌 검증 7항목)가
  모두 통과해야만 "확인 후 생성" 버튼이 활성화된다.
- **Undo 미지원 명시**: "이 플러그인은 Undo/자동 Rollback을 지원하지 않습니다. 생성 후
  되돌리려면 GEN NX에서 직접 삭제해야 합니다"라고 생성 직전 경고 문구를 명시 — 되돌릴 수 없는
  작업임을 사용자에게 명확히 인지시킨 뒤에만 진행.
- **단계별 진행 로그 노출**: 생성 실행 시 "전처리 진행: 재조회 → 사전검증 → Unit → Material
  → Section (각 단계 실패 시 이후 전부 중단)" 순서와 각 단계의 성공/건너뜀 상태를 실시간으로
  표시 — 중간에 실패하면 이후 단계를 모두 중단하는 안전한 순차 파이프라인 구조.

## 5. 워크플로우

### Step 1 — API 연결

- "GEN NX Plant Frame Builder" 창에서 `Base URL`, `MAPI-Key` 입력. "Key는 세션 메모리에서만
  쓰이고 어디에도 저장되지 않습니다"라고 명시.

### Step 2 — 데이터 가져오기

- "데이터 가져오기" 클릭 → 현재 GEN NX 모델의 Unit(예: KN/M/KCAL/C), Material(Frame #1),
  Section(7종) 목록을 자동 조회.

### Step 3 — 기본 설정 (형상 파라미터)

| 필드 | 설명 | 예시 값 |
| --- | --- | --- |
| Bay 수 | 종방향 경간 수 | 3 → 15 |
| Bay 간격 | 동일 간격 또는 Bay별 Custom | 6 (m) |
| Rack 폭 | 횡방향 폭 | 8 (m) |
| Level 수 | 층수 | 2 → 5 |
| 층고 | 동일 층고 또는 Custom | 4 (m) |

- 값을 바꾸면 좌측 "구조 미리보기" 3D 등각도가 즉시 갱신되며, Bay/Rack/Level/Brace/Support
  요약 텍스트도 함께 업데이트된다.

### Step 4 — 재료·단면·브레이스·지점 설정

- Material: 기존 Frame(#1) 재사용 또는 "+ 신규 Steel Material 정의"(Standard: KS22(S),
  DB 강종: SS235 등)로 신규 생성 후 "생성 예정 목록에 추가".
- Column/Trans. Beam/Long. Beam 단면: 각각 드롭다운에서 기존 Section 선택 또는 "+ DB
  Section 추가"(Shape: H-Section 등, 단면명 직접 입력, KS21 카탈로그 등에서 확인된 12종만
  표시)로 신규 정의.
- X-Brace 토글 on 시 Brace 단면 지정 및 Brace Bay를 개별 체크박스로 선택(예: Bay 1, 3, 5,
  7, 9, 11, 13, 15 — 홀수 Bay마다 가새 배치).
- Support: Fixed/Pinned/None 중 선택(예: Pinned로 변경 시 미리보기의 지점 마커가 삼각형
  힌지 기호로 즉시 바뀜).
- 상세 설정: Origin X/Y, Base Elev. Z, 가새를 넣을 Level 개별 체크(Level 1~5 중 선택), 자동
  ID 할당 토글(켜면 "Node 1 / Element (현재 최대 ID + 1, 데이터 가져오기 결과)"로 자동 채번).

### Step 5 — 검증 및 미리보기

- "VALIDATE & PREVIEW" 섹션에서 "검증 통과 — 아래 내용으로 일괄 생성할 수 있습니다" 확인.
- 입력값 요약 표(현재 Unit, Unit 적용 방식, Material 배정/신규 Material, Column/Trans. Beam/
  Long. Beam 단면 등)로 최종 설정을 재확인.
- 예상 생성 수량 표(PIPE RACK): Node 192개(ID 1~192), Column 160개, Transverse Beam 80개,
  Longitudinal Beam 150개, Brace 160개, 전체 Element 550개(ID 1~550, Column ID 1~160,
  Transverse Beam ID 161~240, Longitudinal Beam ID 241~390, Brace ID 391~550), Support
  32개(PINNED), 좌표 범위(X 0~90/Y 0~8/Z 0~20), Brace 위치 목록까지 상세 표시.

### Step 6 — 생성 준비 상태 확인 (GENERATE READINESS)

- 체크리스트 7항목: 모델 데이터 조회(Base URL/MAPI-Key/데이터 가져오기), Unit 조회,
  Material 배정, Section 배정(Column/Trans./Long./Brace), 이름 충돌 없음, 입력 검증, 모델
  충돌 검증 — 전부 ✓(성공)일 때만 다음 단계 진행 가능.
- ⚠️ 시연 중 형상을 되돌린 직후 "모델 충돌 검증" 항목이 ✕(실패)로 표시된 프레임이 포착됨 —
  이전 생성 결과와 좌표가 겹치는 경우 사전에 걸러내는 검증 단계가 실제로 작동함을 보여준다
  (재설정 후 다시 ✓로 통과).

### Step 7 — 모델 생성

- "GENERATE COMPLETE MODEL" 섹션에 "생성 전 최종 확인" 경고 박스: 사용할 Unit, 신규 Material/
  Section 유무, 생성될 Node/Element/Support 수, ID 범위, Undo 미지원 경고를 재확인시키고
  "확인 후 생성" 버튼 클릭.
- 진행 로그: "전처리 진행: 재조회 → 사전검증(ID·이름 충돌) → Unit 적용 → Material 생성/재조회
  검증 → Section 생성/재조회 검증 → (Frame 생성 순서) Node → Column → Transverse → Longitudinal
  → Brace → Support" 각 단계가 순서대로 성공(●) 표시되며 실행됨.
- 완료 후 GEN NX 모델 트리에 Nodes 192, Elements 550(Truss 160, Beam 390), Material 1,
  Section 7, Supports 32(Type 1 [111000])가 실제로 생성된 것을 확인하고, 3D 등각도로 회전해
  최종 Pipe Rack 골조 형상을 검토.

## 6. 연계 JSON API 엔드포인트

화면에 정확한 엔드포인트 이름은 노출되지 않았으나, "Frame 생성 순서: Node → Column →
Transverse → Longitudinal → Brace → Support"라는 명시적 순서와 GEN NX 모델 트리에 최종
반영된 데이터 구조(Nodes/Elements(Truss·Beam)/Material/Section/Supports)로 정확히 매핑
가능하다:

| 생성 순서 | 대상 | 추정 API | 문서 위치 |
| --- | --- | --- | --- |
| 1 | Material(신규 Steel Material) | `POST /db/MATL` | [`04_DB_Properties.md#1-dbmatl`](../../manual/04_DB_Properties.md#1-dbmatl) |
| 2 | Section(신규 DB Section) | `POST /db/SECT` | [`04_DB_Properties.md#12-dbsect`](../../manual/04_DB_Properties.md#12-dbsect) |
| 3 | Node(192개) | `POST /db/NODE` | [`03_DB_Node_Element.md#1-dbnode`](../../manual/03_DB_Node_Element.md#1-dbnode) |
| 4 | Column/Beam(Trans.·Long.) | `POST /db/ELEM`(Beam) | [`03_DB_Node_Element.md#2-dbelem`](../../manual/03_DB_Node_Element.md#2-dbelem) |
| 5 | Brace | `POST /db/ELEM`(Truss) | 위와 동일 |
| 6 | Support(32개, Fixed/Pinned) | `POST /db/CONS` | [`05_DB_Boundary.md#1-dbcons--constraint-support`](../../manual/05_DB_Boundary.md#1-dbcons--constraint-support) |

- ⚠️ 위 매핑은 화면에 표시된 "Frame 생성 순서"와 최종 생성된 GEN NX 모델 트리 항목(Truss
  160개 / Beam 390개로 분류됨 — Column·Beam은 Beam 타입, Brace는 Truss 타입으로 생성된 것으로
  추정)에 근거한 것이며, 실제 요청 바디나 정확한 호출 횟수(개별 POST 반복 vs 배치 POST)는
  화면에 노출되지 않아 확인되지 않았다.
- Unit 적용("Unit 적용" 단계가 로그에 별도로 존재)이 `/db/UNIT` 계열 엔드포인트를 호출하는
  것으로 추정되나, `docs/manual`에서 해당 엔드포인트를 아직 확인하지 못했다(⚠️ 미확인).

## 7. 입력 데이터 규격

- **형상 파라미터**: Bay 수, Bay 간격(동일/Custom), Rack 폭, Level 수, 층고(동일/Custom).
- **재료·단면**: Column/Trans. Beam/Long. Beam/Brace 각각 기존 또는 신규 Section, Material.
- **브레이스**: X-Brace 사용 여부, 브레이스 배치 Bay·Level.
- **지점 조건**: Fixed/Pinned/None.
- **상세 설정**: Origin X/Y, Base Elev. Z, 자동 ID 할당 여부.

## 8. 출력 / 생성 결과

- GEN NX 모델에 생성된 Node·Column·Transverse Beam·Longitudinal Beam·Brace·Support 전체
  Pipe Rack 골조(초기 구조해석용).
- 생성 전 확인 가능한 예상 수량·ID 범위 요약 정보.

## 9. 제약사항 및 한계

- Undo/자동 Rollback을 지원하지 않는다 — 생성 후 되돌리려면 GEN NX에서 사용자가 직접 삭제해야
  한다. 이는 이 Plug-in 자체가 명시적으로 경고하는 한계다.
- 생성되는 것은 "초기 구조해석용" Frame 모델이며, 실제 배관 하중·풍하중 등 하중 재하나 부재
  검토·설계까지는 이 Plug-in의 범위에 포함되지 않는 것으로 보인다(원문·화면 어디에도 하중
  재하 기능 언급 없음).
- 모델 충돌 검증(기존 모델과 좌표 겹침 여부)이 자동으로 이루어지지만, 겹치지 않는 위치로
  자동 재배치까지 해주는지, 아니면 단순히 실패 신호만 주는지는 화면상 실패 후 재시도하는
  장면만 확인되고 자동 회피 로직은 확인되지 않았다.

## 10. 화면 인벤토리

| 시점(초) | 화면 내용 |
| --- | --- |
| 0–12 | 인트로(Plant Frame Builder 개요 슬라이드, 생성 전 최종 확인 UI 미리보기) |
| 12–30 | WHY — 기존 수작업/DXF Import 방식의 번거로움, "CAD 없이 GEN NX 안에서 바로" 컨셉 소개 |
| 30–66 | 실제 GEN NX 진입, API 연결(Base URL/MAPI-Key), 데이터 가져오기 |
| 66–96 | 기본 설정(Material/Column/Beam/Brace 단면, 신규 Steel Material·DB Section 정의) |
| 96–138 | Bay 수/Level 수/Bay 간격 등 파라미터 조정에 따른 실시간 미리보기 갱신, X-Brace·Brace Bay·지점 조건, 상세 설정(원점/Brace Level/자동 ID) |
| 138–150 | VALIDATE & PREVIEW 요약 표, GENERATE READINESS 체크리스트, 예상 생성 수량·ID 범위 확인 |
| 150–162 | "확인 후 생성" 실행 → 단계별 진행 로그 → 최종 3D 모델 생성 결과 확인(트리 항목·회전 검토) |
| 162–165 | 마무리 |

---

*다음: 12_OTChecker 영상 분석 및 기획문서 작성.*
