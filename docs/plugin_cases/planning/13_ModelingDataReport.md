# ModelingDataReport 기획문서

> 영상(`docs/plugin_cases/videos/13_ModelingDataReport.mp4`, 30fps, 1920×1080, 약 230초)을 8초
> 간격으로 프레임 캡처(총 29장) 후 프레임별 육안 분석 + 자막을 근거로 작성. 원문
> 아티클(`docs/plugin_cases/articles/13_ModelingDataReport.md`)의 3대 기능 설명과 교차 확인함.
> 이 세션의 20개 사례 중 가장 정보 밀도가 높은 산출물(총 31페이지 PDF, 5개 챕터)을 만드는
> Plug-in으로, 모델링 검수 항목을 거의 전수 조사하는 것이 핵심.

## 1. 개요

**Modeling Data Report**는 GEN NX에 열려있는 모델의 선언 데이터(구조형식/층/재료/단면/경계조건/
하중/해석옵션)를 MIDAS API로 전수 수집하여, 구조계산서 부록에 바로 첨부할 수 있는 "모델링 검토
보고서"(PDF, Excel)로 자동 생성하는 Plug-in이다.

## 2. 문제 정의

- GEN NX 모델을 시니어가 검수하거나 다른 담당자에게 인수인계할 때, 메뉴 곳곳에 흩어진 설정
  (자중, 경계조건, 강성계수 등)을 하나씩 확인해야 하는데, 메뉴 위치를 몰라 항목을 놓치기 쉽다.
- 층간변위·비정형(연층·편심 등) 평가처럼 내진 관련 검토 문서 작성은 여러 결과 테이블을 조합
  해야 해서 별도로 문서를 만드는 데 시간이 오래 걸린다.
- 시니어와 주니어 간 모델링 확인(리뷰) 과정이 반복적이고 표준화되어 있지 않다.

## 3. 목표 사용자

- GEN NX 모델을 검수·인수인계해야 하는 시니어/주니어 구조 엔지니어.
- 구조계산서 부록에 모델링 검토 보고서를 첨부해야 하는 실무자.

## 4. 핵심 컨셉 / 차별점

- **선언 여부(Boolean) 전수 점검**: 재료·단면·강성계수·경계조건·해석옵션 등 GEN NX의 개별
  입력 메뉴 하나하나를 "선언"/"–"(미선언)로 표로 나열해, 사용자가 "이 항목을 넣었는지 안
  넣었는지" 자체를 잊어버리는 실수를 원천 차단한다(예: 3.1절 "선언 현황(Properties)" 표에
  Material Properties/Section Stiffness Scale Factor/Thickness/Wall Stiffness Scale Factor
  등 10여 항목을 선언/미선언으로 일괄 나열).
- **자중 산정을 절점 좌표 기반으로 자동 검증**: 절점 좌표로부터 연면적·면적당 중력하중을 자동
  산정해 표시(1.1 모델 요약), 하중 케이스별 집계표(2.4절)로 잘못 입력된 하중을 발견할 수 있게
  한다.
- **최하단 절점-지점 선언 개수 대조 자동화**: "최하층(B1F) 레벨 절점 수: 257 vs Support 선언
  절점 수: 257 → 미선언 절점: 0(누락 없음)"처럼 자동 대조표를 만들어, 지점 조건 누락을
  자동으로 잡아낸다(3.10절) — 단순 나열이 아니라 실제 정합성 검증 로직이 들어간 부분.
  ⚠️ 이 문서 관례상 이런 자동 검증은 명시된 항목에 한정되므로, "몇 개 vs 몇 개"라는 두 숫자를
  API로 각각 취득한 뒤 비교하는 것으로 보이며 그 외 항목까지 전부 이런 정합성 검증이 있는지는
  확인되지 않았다.
- **Self Check 체크박스**: 각 항목 옆에 사용자가 직접 체크할 수 있는 "Self Check" 칸을 배치해,
  검토자가 항목별로 "내가 직접 확인했음"을 표시하며 체크리스트처럼 사용할 수 있게 한다.
- **5개 챕터로 구조화**: General(구조 개요·건축개요 검증) → Structure(골조·하중·층 질량) →
  Properties & Boundary(재료·단면·지점) → Analysis Option(필수 해석 옵션) → Load(하중·풍/지진·
  층간변위·비정형)로 구성해, 전처리(모델링)와 후처리(해석 옵션·비정형 평가)를 하나의 문서로
  통합.
- **Story Drift·비정형 평가까지 자동 산출**: 우발편심(Accidental Eccentricity)을 고려한 층간
  변위, 강성 불규칙(Soft Story, X/Y 방향), 편심(Torsional) 비정형 판정 결과를 Regular/Irregular
  로 자동 산출해 방대한 표로 제공 — 원문 3번 기능("층간변위와 비정형 평가까지 자동으로 정리되어
  내진 관련 검토 문서 작성 부담이 줄어듭니다")과 정확히 일치.

## 5. 워크플로우

### Step 1 — API 연결 및 모델 수집

- "Modeling Data Report" 창에서 `Base URL`, `MAPI-Key` 입력.
- "1. 모델 수집" 클릭 → 하중케이스별 계산 진행 로그(Calculating Loads for Load Case DL/WX/
  WY/EX/EY/WX(A)...) → 자동으로 지하/지상/옥탑 층을 분류(사용자가 필요 시 직접 수정 가능,
  드롭다운으로 지하/지상/옥탑 재분류).

### Step 2 — 계수 입력

- 건축물 중요도, 변위증폭계수 C_d, 초과강도계수 Ω_0, 여용도계수 등을 입력 — 이 계수들이 층간
  변위·비정형 평가에 반영됨.

### Step 3 — 보고서 생성(PDF)

- "2. 리포트 생성(PDF)" 클릭 → 5개 챕터로 구성된 보고서(총 31페이지) 생성:

**Chapter 01. General** (구조 개요·건축개요 검증)
- 1. General — 데이터 수집(열려 있는 모델에서 실시간 수집), 수집 시각, 해석 여부.
- 전체 형상(Isometric)·평면(Top) 이미지 자동 캡처.
- 1.1 모델 요약: 건물 규모(지하 1층/지상 20층+옥탑 1, 총 22개층), 건물 가로폭/세로폭/높이,
  건축물 중요도(풍하중·지진하중 중요도계수), 모델링 연면적(철골 격자 근사), 건물 전체
  중량(전층 고정하중의 합산), 지진 유효 중량(지진하중 산정 시 적용된 MASS), 대표층 면적당
  하중(면적/DL sum/LL sum/면적당 DL/면적당 LL).
- 고유치해석 결과 표(Mode No/Frequency/Period/TRAN-X/TRAN-Y/ROTN-Z).
- 풍하중 개요(자동/수동 산정 여부, 적용 기준 KDS(41-12:2022), 기본풍속, 중요도계수 I_w,
  세장비 λ, 해석방법, 가스트영향계수, 풍직각횡하중 Across Wind, Wind Shear).
- 지진하중 개요(적용 기준 KDS(41-17-00:2019), 중요도계수 I_E, 지역계수 S, 지반분류).

**Chapter 02. Structure** (골조·하중·층 질량)
- Structure Type/Mass Control Parameter/Building Control 팝업 그대로 캡처해 선언 상태 확인
  (3-D/X-Z Plane/Y-Z Plane/X-Y Plane/Constraint RZ, Lumped Mass/Consistent Mass 등).
- 2.3 Story Data — Wind·Seismic(층별 Floor Width, Center, Eccentricity, Accidental/Inherent
  Eccentricity, Torsional Amplification Factor X/Y).
- 2.4.2~2.4.5 하중케이스별 집계표(DL/LL/WX/WY — Z방향, Level/Input/Self Weight/Sum).
- 2.5 Story Mass(Translational Mass X/Y-DIR, Rotational Mass, Center of Mass X/Y-Coord).

**Chapter 03. Properties & Boundary** (재료·단면·지점)
- 3.1 선언 현황(Properties): Material Properties/Material Design Data/Design Code(Material)/
  Design Steel Code/Time Dependent Material(Creep·Comp. Strength)/Section Properties/Section
  Stiffness Scale Factor/Thickness/Wall Stiffness Scale Factor/Plate Stiffness Scale
  Factor/Element Stiffness Scale Factor/Effective Width Scale Factor — 선언/미선언 표.
- 3.2 Material Properties(ID/Name/Type/Standard/DB/탄성계수/포아송비/열팽창계수/단위중량/
  감쇠비), 3.3 Design Code, 3.4 Material Design Data, 3.5 Thickness, 3.6 Section
  Properties(전 30개), 3.7 Section Stiffness Scale Factor(fArea/fAsy/fAsz/fIxx/fIyy/fIzz/
  fWgt/적용 Element 수).
- 3.9 선언 현황(Boundary): Supports/Point Spring/General Spring/Surface Spring/Rigid
  Link/Elastic Link/General Link Properties/General Link/Beam End Release/Beam End
  Offsets/Plate End Release/Linear Constraints/Panel Zone Effects/Diaphragm Disconnect/
  Boundary Group.
- **3.10 Supports — 최하층 전수 대조**: 최하층(B1F) 레벨 절점 수 vs Support 선언 절점 수를
  대조해 미선언 절점 수(누락 없음 등)를 자동 산출 — 구속 패턴(Dx Dy Dz Rx Ry Rz Rw)도 함께
  표시.
- 3.11 Elastic Link(Type/수량), 3.12 Beam End Release(해제 자유도별 수량).

**Chapter 04. Analysis Option** (필수 해석 옵션)
- Main Control Data(Auto Rotational DOF Constraint, Number of Iterations/Load Case,
  Convergence Tolerance, Consider Section Stiffness Scale Factor for Stress Calculation
  등), Eigenvalue Analysis Control(Type of Analysis, Number of Frequencies, Eigenvalue
  Control Parameters) 팝업을 그대로 캡처.
- P-Delta/Buckling/Nonlinear/Construction Stage/Settlement/Heat of Hydration/Moving
  Load/Pushover/Inelastic Hinge Control 등 나머지 옵션은 "선언된 항목 없음"으로 명시(실제
  이 예제 모델에는 사용되지 않았음을 투명하게 표기).

**Chapter 05. Load** (하중·풍/지진·층간변위·비정형)
- 5.2 Static Load Cases — 케이스별 정리(산정 구분: 직접 입력/자동 산정, 입력된 하중 상세,
  Description), 5.3 Dynamic Load Cases(응답스펙트럼 RS, 각도, 스펙트럼 함수, 모드 조합 CQC,
  우발편심 5.00%).
- 5.1 Gravity Load — 입력 메뉴별 선언 매트릭스(Self-Weight/Nodal Body Force/Nodal Loads/
  Element Beam Load/Define Floor Load Type/Finishing Material Loads × DL/LL).
- 5.2.3 Across Wind — 진동 파라미터(Across Wind 고려, Torsional/Wind Response 고려, 건물
  폭, 고유진동수, 질량 M/Mx/My, 질량관성모멘트 Mt), 5.2.4 풍동실험 대상 검토(전층, 세장비 λ =
  H/√(B·D) 기준으로 풍동실험 판정 Regular/비대상 자동 분류), 5.2.5/5.2.6 방향별 Story
  Force·Story Shear.
- **5.4 Story Drift 및 비정형 평가**: 층간변위·안정성계수·비정형 검토·RS 층전단 — 5.4.1 Story
  Drift(X방향, Maximum Drift of All Vertical Elements, Allowable Story Drift, Drift at the
  Center of Mass), 5.4.6~5.4.7 우발편심 고려 편심 검토(RY(RS)+RY(ES) 등 조합별 Regular/
  Irregular 판정), Stiffness Irregularity Check(Soft Story, X방향) — 강성비·판정을 층별로
  전량 나열.

### Step 4 — 결과 확인 및 출력

- "PDF로 저장/인쇄" 버튼으로 최종 보고서(31페이지) 다운로드, Adobe Acrobat 등으로 열람.
- Excel 출력("Excel 출력" 버튼)도 별도 지원(화면상 상세 시연은 노출되지 않음).

## 6. 연계 JSON API 엔드포인트

화면에 정확한 요청 로그는 노출되지 않았으나(하중 계산 진행 메시지만 노출), 보고서에 담긴
항목들은 `docs/manual`의 다음 엔드포인트들과 명확히 대응된다:

| 챕터 | 항목 | 추정 API | 문서 위치 |
| --- | --- | --- | --- |
| 01/02 | Story Data | `GET /db/STOR` | [`02_DB_Project_Structure.md#15-dbstor--story-data`](../../manual/02_DB_Project_Structure.md#15-dbstor--story-data) |
| 01/02 | Node/Element 수, 좌표 | `GET /db/NODE`, `GET /db/ELEM` | [`03_DB_Node_Element.md#1-dbnode`](../../manual/03_DB_Node_Element.md#1-dbnode), [`#2-dbelem`](../../manual/03_DB_Node_Element.md#2-dbelem) |
| 01 | 고유치해석 결과 | `POST /post/table`(`EIGENVALUEMODE`/`PARTICIPATIONVECTORMODE`) | [`20_POST_AnalysisResult_2.md#28-vibration-mode-shape`](../../manual/20_POST_AnalysisResult_2.md#28-vibration-mode-shape) |
| 03 | Material Properties | `GET /db/MATL` | [`04_DB_Properties.md#1-dbmatl`](../../manual/04_DB_Properties.md#1-dbmatl) |
| 03 | Section Properties | `GET /db/SECT` | [`04_DB_Properties.md#12-dbsect`](../../manual/04_DB_Properties.md#12-dbsect) |
| 03 | Thickness | `GET /db/THIK` | [`04_DB_Properties.md`](../../manual/04_DB_Properties.md) (§13 THIK) |
| 03 | Section Stiffness Scale Factor | `GET /db/ESSF`(Element Stiffness Scale Factor) | [`04_DB_Properties.md#31-dbessf`](../../manual/04_DB_Properties.md#31-dbessf) |
| 03 | Supports | `GET /db/CONS` | [`05_DB_Boundary.md#1-dbcons--constraint-support`](../../manual/05_DB_Boundary.md#1-dbcons--constraint-support) |
| 03 | Elastic Link | `GET /db/ELNK` | [`05_DB_Boundary.md#6-dbelnk--elastic-link`](../../manual/05_DB_Boundary.md#6-dbelnk--elastic-link) |
| 04 | Analysis Control(Main/Eigenvalue) | `GET /db/*`(Analysis Control 계열) | [`12_DB_Analysis_Control.md`](../../manual/12_DB_Analysis_Control.md) |
| 05 | Static/Dynamic Load Cases | `GET /db/STLD`, `GET /db/SPLC` | [`06_DB_Static_Loads.md#1-dbstld--static-load-cases`](../../manual/06_DB_Static_Loads.md#1-dbstld--static-load-cases), [`09_DB_Dynamic_Loads.md#2-dbsplc--response-spectrum-load-cases`](../../manual/09_DB_Dynamic_Loads.md#2-dbsplc--response-spectrum-load-cases) |
| 05 | Story Drift, 비정형 평가 | `POST /post/table`(Story Drift, `STIFFNESS_IRREGULARITY_X/Y`, Eccentricity 계열) | [`21_POST_StoryTables.md#1-story-drift`](../../manual/21_POST_StoryTables.md#1-story-drift), [`21_POST_StoryTables.md#13-stiffness-irregularity-check-soft-story`](../../manual/21_POST_StoryTables.md#13-stiffness-irregularity-check-soft-story) |

- ⚠️ 3.1절/3.9절의 "Wall Stiffness Scale Factor"·"Plate Stiffness Scale Factor" 선언 여부
  항목은 #5(WallStiffnessAuto) 문서에서 이미 확인한 것과 동일하게, `docs/manual`에 전용 GET
  엔드포인트가 별도 문서화되어 있지 않은 항목이다(`/db/ESSF`만 Element 단위로 존재). 이 Plug-in
  이 이 항목의 선언 여부를 어떤 API로 조회하는지는 확인되지 않았다.
- 이 Plug-in은 모델의 사실상 모든 `/db/*` 조회 엔드포인트와 다수의 `/post/table` 결과 테이블을
  총망라해서 호출하는 것으로 보이며, 위 표는 화면에 노출된 항목 중 확인 가능한 일부만 정리한
  것이다(⚠️ 전수 목록이 아님).

## 7. 입력 데이터 규격

- **선행 조건**: 해석이 완료된(또는 부분 완료) GEN NX 모델.
- **계수 입력**: 건축물 중요도, 변위증폭계수 C_d, 초과강도계수 Ω_0, 여용도계수.
- **층 분류**: 자동 분류된 지하/지상/옥탑을 필요 시 사용자가 직접 수정.

## 8. 출력 / 생성 결과

- "Modeling Data Report" PDF(총 31페이지, 5개 챕터).
- Excel 형태의 동일 데이터 출력(버튼만 확인, 상세 미시연).

## 9. 제약사항 및 한계

- 이 보고서는 어디까지나 "선언 여부"와 "값의 정합성"을 자동 대조하는 도구이며, 그 값이 구조
  적으로 옳은지(예: 재료 강도가 설계 의도와 맞는지)까지 판단해주지는 않는다 — 체크리스트형
  검수 보조 도구.
- 3.10절의 "최하단 절점-지점 대조"처럼 명시적으로 확인된 자동 검증 로직 외에, 다른 항목들도
  전부 유사한 정합성 검증을 거치는지는 화면상 확인되지 않았다(단순 나열형 표도 다수 존재).
- P-Delta/Buckling/Pushover 등 미사용 해석 옵션은 "선언된 항목 없음"으로만 표시되며, 이것이
  "정상적으로 사용 안 함"인지 "실수로 누락"인지는 엔지니어가 별도로 판단해야 한다.

## 10. 화면 인벤토리

| 시점(초) | 화면 내용 |
| --- | --- |
| 0–16 | 인트로 내레이션, GEN NX 예제 모델(아파트 22층) 진입 |
| 16–40 | Plug-in 최초 실행, 하중 계산 로그, Base URL/MAPI-Key 연결 |
| 40–72 | 층 분류(지하/지상/옥탑) 수정, 계수 입력(중요도·C_d·Ω_0) |
| 72–104 | Chapter 01 General — 모델 요약, 고유치해석 결과, 풍/지진하중 개요 |
| 104–136 | Chapter 02 Structure — Structure Type/Building Control, Story Data, 하중케이스 집계표, Story Mass |
| 136–168 | Chapter 03 Properties & Boundary — 선언 현황, Material/Section/Stiffness Scale Factor, Supports 대조, Elastic Link/Beam End Release |
| 168–184 | Chapter 04 Analysis Option — Main Control/Eigenvalue Control 팝업 캡처 |
| 184–216 | Chapter 05 Load — Static/Dynamic Load Cases, Gravity Load 매트릭스, Across Wind, Story Drift, 비정형 평가(Stiffness Irregularity) |
| 216–224 | PDF 최종본 확인(Adobe Acrobat, 31페이지), 마무리 내레이션 |
| 224–230 | 종료 카드 |

---

*다음: 14_GenSnap 영상 분석 및 기획문서 작성.*
