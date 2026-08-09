# AutoGenerationCmFactor 기획문서

> 영상(`docs/plugin_cases/videos/04_AutoGenerationCmFactor.mp4`, 30fps, 1920×1080, 약 189초)을
> 8초 간격으로 프레임 캡처(총 24장) 후 프레임별 육안 분석 + 영상 내 자막(내레이션 캡션)을 근거로
> 작성. 이 영상은 다른 영상들과 달리 화면 녹화 위에 자막 카드를 오버레이한 발표 자료 형태이며,
> 원문 아티클(`docs/plugin_cases/articles/04_AutoGenerationCmFactor.md`)의 4대 기능 설명과 교차
> 확인함. 발표자(참가자명 "제로")가 개발 의도부터 실제 시연, 후기(아쉬운 점)까지 3부 구성으로
> 설명하는 형식.

## 1. 개요

**AutoGenerationCmFactor**는 MIDAS GEN NX의 하중조합 생성 시 필요한 지진하중의 **Cm
Factor(보정계수, Scale-up Factor)**를 KDS 41 17 00 기준에 따라 자동으로 계산하는 Plug-in이다.
모델에 이미 입력된 값들을 API로 불러와 계산에 필요한 항목을 자동 채움하고, 계산 근거를 담은
계산서(.OUT)까지 출력한다.

## 2. 문제 정의

- 자매 프로그램인 **MIDAS ADS**에는 응답스펙트럼 하중케이스에 대한 Modification
  Factor(Scale-up Factor)를 산정하는 기능(`Modification Factor(Scale-up Factor) for Response
  Spectrum Load Cases`)이 있지만, **MIDAS GEN NX에는 동적 지진하중에 대한 보정계수 산정 기능
  자체가 없다.**
- 대신 GEN NX 사용자는 이 보정계수를 산정하기 위해 별도 계산서를 수기로 작성해야 하며, 그
  과정에서 여러 수치(유효중량, 가속도, 지반분류, 고유주기 등)를 모델에서 일일이 옮겨 적어야
  해서 오입력 등 휴먼에러가 발생하기 쉽다.
- 개발자 코멘트(자막): "그 과정에서 각 수치의 오입력 등 휴먼에러를 최소화 하기 위해 플러그인을
  제작하게 되었습니다."

## 3. 목표 사용자

- KDS 41 17 00(건축물 내진설계기준) 기준으로 응답스펙트럼 해석 결과에 지진하중 보정계수(Cm
  Factor)를 적용해 하중조합을 생성해야 하는 구조 설계자.
- 기반암 깊이·지반 평균 전단파속도 등 KDS 41 17 00 4.2.2항의 예외 조항(2)·(3)을 판단해 적용해야
  하는 실무자.

## 4. 핵심 컨셉 / 차별점

- **모델 데이터 자동 취득("가져오기")**: 유효 중량 기준층(지하층 포함/제외), 건축물 높이, 단주기
  가속도(SDS), 1초주기 가속도(SD1), 유효지반가속도(S), 지반분류, 중요도 계수(Ie), 반응수정계수
  (R), 고유치해석 주기(Td,x/Td,y) — 9개 항목을 모델에서 API로 한 번에 불러온다.
- **KDS 41 17 00 4.2.2 (2)·(3) 예외 조항 자동 판정**: 기반암 깊이가 20m를 초과하고 지반 평균
  전단파속도가 360m/s 이상인 경우 Fv의 80%를, 지반분류가 S5이고 기반암 깊이가 불분명한 경우
  Fa·Fv의 110%를 자동 적용 — 사용자가 규정 조항을 직접 판단하지 않아도 값을 비워두면 자동
  산정된다("11번 항목을 빈칸으로 입력하더라도 그 기준에 맞게 자동으로 Fa,Fv가 산정됩니다").
- **골조 형상별 규준식 선택**: 근사고유주기 산정식(Ta = Ct·hn^x)의 계수(Ct, x)를 철근콘크리트
  모멘트골조/철골모멘트골조/철골 편심가새골조 및 좌굴방지가새골조/철근콘크리트전단벽구조·기타골조
  4종 중 선택하도록 해, 골조 형상에 따라 규준식이 다르다는 점을 반영.
- **질량참여율 주기의 엔지니어 재확인 경고**: 고유치해석 주기(Td,x/Td,y)는 진동모드 형상 테이블의
  각 방향별 주기를 자동으로 가져오지만, "질량참여율의 주방향 주기는 엔지니어의 판단이므로 반드시
  재확인이 필요합니다"라는 경고 문구를 UI에 상시 노출 — 자동화가 공학적 판단을 대체하지 않는다는
  점을 명시.
- **계산 근거 계산서(.OUT) 자동 생성**: 계산에 사용한 모든 수치와 산출 과정을 MIDAS ADS의
  보정계수 산정 근거 계산서와 동일한 양식으로 출력해, 검토자가 근거를 추적할 수 있게 한다.

## 5. 워크플로우

### Step 1 — API 연결

- Plug-in 창 상단 `Base URL`, `MAPI-Key` 입력.

### Step 2 — 1. CONDITION: 모델 데이터 자동 취득

"가져오기" 버튼 클릭 시 아래 9개 항목이 모델에서 자동으로 채워짐(자막 근거):

| No. | 항목 | 자동 취득 출처(자막 근거) |
| --- | --- | --- |
| 유효중량 기준층 | 지하층 포함/제외 선택(드롭다운) | 사용자 선택 |
| 1) 건축물 높이 (hn) | Story 최상층 높이 | `Story Data`의 최상층(Roof) `Level(m)` |
| 2) 유효 충량 (W) | Weight Sum(RX, RY)의 총하중(지상층 또는 지하층) | 응답스펙트럼 해석 결과 층별 Weight Sum 테이블 |
| 3)–8) SDS, SD1, S, 지반분류, Ie, R | (영상에 취득 경로가 직접 노출되지 않음, 지진하중 정의 데이터로 추정) | ⚠️ 미확인 |
| 9) 고유치해석 주기 (Td,x / Td,y) | 진동모드 형상(Eigenvalue Analysis / Modal Participation Masses) 테이블의 각 방향별 주기 | 고유치해석 결과 테이블 |

- 10) 규준식(수동입력): 골조 형상 4종 중 선택 (Ct, x 계수 자동 표시).
- 11) 보통암 까지 깊이 / 12) 전단파 속도(수동입력, 선택): 빈칸으로 두면 KDS 41 17 00 4.2.2
  (2)·(3) 조항 기준에 맞춰 Fa/Fv가 자동 산정됨.

### Step 3 — Scale Up Factor(Cm) 계산

- "계산" 버튼 클릭 → 정적 밑면전단력(Vs, X/Y)과 동적 밑면전단력(Vd, X/Y)을 자동 계산해 비교하고,
  최종 Cm Factor(X/Y)를 산출.
- 영상 예시 결과: Vs(X)=15710.30kN, Vs(Y)=15710.30kN, Vd(X)=11885.45kN, Vd(Y)=11575.40kN →
  **Cm Factor X=1.1235, Y=1.1536**.

### Step 4 — 계산서(.OUT) 출력

- "계산서" 버튼 클릭 → `Cm_Factor_Report.out` 파일 다운로드.
- 이 파일을 MIDAS/Text Editor로 열면 MIDAS ADS의 보정계수 산정 근거 계산서와 동일한 양식(설계
  기준, 지진구역, 유효지반가속도, 지반분류, 상수 지반증폭계수, 단주기·1초주기 설계스펙트럼가속도,
  중요도 계수, 반응수정계수, 내진설계 카테고리, 건물의 기본진동주기(고유치해석), 지진응답계수(Cs),
  정적/동적 밑면전단력, Scale-up Factor)이 생성됨.

## 6. 연계 JSON API 엔드포인트

영상에 정확한 요청/응답 페이로드는 노출되지 않았으나, 값을 취득한 화면(Story Data 창, Vibration
Mode Shape 결과 테이블, Story Shear Force Coefficient 결과 테이블)이 명확히 식별되어 아래
엔드포인트로 추정 가능:

| 취득 항목 | 추정 API | 문서 위치 |
| --- | --- | --- |
| 건축물 높이(hn), Story 목록 | `GET /db/STOR` | [`02_DB_Project_Structure.md#14-dbstor--story-data`](../../manual/02_DB_Project_Structure.md#14-dbstor--story-data) |
| 유효 중량(W), Weight Sum X/Y | `POST /post/table` (`TABLE_TYPE: STORY_SHEAR_FORCE_COEFFICIENT`) | [`21_POST_StoryTables.md#4-story-shear-force-coefficient-rs-analysis`](../../manual/21_POST_StoryTables.md#4-story-shear-force-coefficient-rs-analysis) |
| 고유치해석 주기(Td,x, Td,y) | `POST /post/table` (`TABLE_TYPE: EIGENVALUEMODE` 또는 `PARTICIPATIONVECTORMODE`) | [`20_POST_AnalysisResult_2.md#28-vibration-mode-shape`](../../manual/20_POST_AnalysisResult_2.md#28-vibration-mode-shape) |
| 정적/동적 밑면전단력(Vs, Vd) | `POST /post/table` (`TABLE_TYPE: STORY_SHEAR_FOR_RS` 등, 정적 지진하중 결과와의 비교) | [`21_POST_StoryTables.md#3-story-shear-force-rs-analysis`](../../manual/21_POST_StoryTables.md#3-story-shear-force-rs-analysis) |

- ⚠️ 위 표의 매핑은 화면에 표시된 결과 테이블의 컬럼 구성(Story/Spectrum/Shear Force
  X·Y/Weight Sum X·Y/Story Shear Force Coefficient X·Y — 영상 t=80s경 테이블과 `21_
  POST_StoryTables.md` §4의 Response HEAD가 정확히 일치)에 근거해 확인된 것이지만, 실제 이
  Plug-in이 호출하는 요청 바디(TABLE_NAME, LOAD_CASE_NAMES 등)까지는 화면에 노출되지 않아
  추정이다.
- SDS/SD1/S/지반분류/Ie/R(3~8번 항목)은 화면상 "가져오기" 버튼 클릭 한 번으로 일괄 채워지는
  장면만 보이고 출처 UI가 별도로 노출되지 않아, `/db/*` 계열의 지진하중 정의 엔드포인트(예:
  정적 지진하중 데이터) 호출로 추정되나 특정하지 않음(⚠️ 미확인).

## 7. 입력 데이터 규격

- **선행 조건**: GEN NX 모델에 Story Data, 정적 지진하중(등가정적하중법), 응답스펙트럼(RS)
  하중케이스, 고유치해석(모드해석) 결과가 이미 존재해야 함.
- **규준식 선택**: 골조 형상 4종 중 1개 필수 선택.
- **선택 입력**: 보통암까지 깊이(m), 평균 전단파 속도 — 미입력 시 KDS 41 17 00 4.2.2 (2)·(3)
  기준으로 자동 판정.

## 8. 출력 / 생성 결과

- Scale Up Factor(Cm Factor) X/Y 값(화면 표시).
- `Cm_Factor_Report.out` 계산서 파일(MIDAS/Text Editor로 열람 가능, MIDAS ADS와 동일 양식).

## 9. 제약사항 및 한계

- 개발자가 직접 밝힌 아쉬운 점(후기) 2가지:
  1. "하중조합 자동생성"의 보정계수 입력 부분까지는 자동 반영되지 않는다 — 즉 이 Plug-in은
     Cm Factor를 산출까지만 하고, GEN NX의 하중조합 자동생성 기능에 그 값을 자동으로 밀어넣는
     연동까지는 구현하지 못했다.
  2. 계산서(.OUT) 파일을 저장한 뒤에도 MIDAS/Text Editor로 자동으로 열리지 않고, 사용자가 별도
     프로그램으로 수동으로 열어야 한다.
- KDS 41 17 00 기준 전용으로 설계되어 다른 설계기준(코드)에는 적용되지 않는 것으로 보임(영상
  전체가 이 기준만 다룸).
- 질량참여율 기준 주방향 주기는 자동 산정값을 그대로 신뢰하지 말고 엔지니어가 재확인해야 한다는
  경고가 명시적으로 붙어 있음 — 완전 자동화가 아니라 판단 보조 도구로 설계됨.

## 10. 화면 인벤토리

| 시점(초) | 화면 내용 |
| --- | --- |
| 0–8 | 인트로 카드(출품작/참가자명) |
| 16–40 | 1. 개발의도 — MIDAS ADS엔 있고 GEN NX엔 없는 보정계수 산정 기능, 수기 계산서 작성의 번거로움 |
| 48–56 | 2. 플러그인 작동영상 — 전체 UI 최초 노출(CONDITION 9개 항목 + Scale Up Factor 계산 영역) |
| 64–96 | "가져오기" 클릭 → 1~9번 항목 자동 채움, Story Data/Weight Sum/Eigenvalue 결과 테이블에서 값 출처 설명 |
| 104–120 | 질량참여율 주기 재확인 경고, 골조 형상별 규준식(Ct, x) 설명 |
| 128–136 | 11)·12) 보통암 깊이/전단파 속도 수동입력 필드, KDS 41 17 00 4.2.2 조항 설명 |
| 144–152 | "계산" 클릭 → Cm Factor 산출, "계산서" 클릭 → .OUT 파일 다운로드·확인 |
| 160–184 | 3. 후기 — 아쉬운 점 2가지(하중조합 자동생성 미연동, .OUT 자동 열기 미구현) |
| 184–189 | 종료 카드(페이드아웃) |

---

*다음: 05_WallStiffnessAuto 영상 분석 및 기획문서 작성.*
