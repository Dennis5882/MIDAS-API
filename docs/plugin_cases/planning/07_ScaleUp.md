# ScaleUp 기획문서

> 영상(`docs/plugin_cases/videos/07_ScaleUp.mp4`, 30fps, 3840×2160, 약 189초)을 8초 간격으로
> 프레임 캡처(총 24장) 후 프레임별 육안 분석 + 화면 상단 큰 자막(단계 제목)과 하단 말풍선 자막을
> 근거로 작성. 원문 아티클(`docs/plugin_cases/articles/07_ScaleUp.md`)의 4대 기능 설명과 교차
> 확인함. #4(AutoGenerationCmFactor)와 목적(Cm 보정계수 산정)은 유사하지만, ScaleUp은 MIDAS
> 공식 "Apps"(Structure Analysis 패널 > Apps) 플랫폼에 등록된 완성형 마법사(Wizard) UI이며,
> **Cm 산정에서 그치지 않고 하중조합 자동 생성·보고서 출력까지** 전 과정을 포함한다는 점에서
> 범위가 더 넓다. 특히 "GEN NX DATA MAP" 화면에 실제 호출 API 5종이 텍스트로 그대로 노출되어
> API 매핑 근거가 매우 강하다.

## 1. 개요

**ScaleUp(Scale Up SE)**는 내진설계기준에 따라 응답스펙트럼해석의 보정계수 Cm을 자동으로
계산하고, 설계용 하중조합을 GEN NX에 자동으로 생성하는 Plug-in이다. Cm 산정에 필요한 해석결과와
하중케이스 정보를 GEN NX에서 자동으로 불러오며, 해석결과 확인 → Cm 산정 → 설계용 하중조합 생성
→ 보고서 출력까지 하나의 연속된 5단계 마법사 흐름으로 수행한다.

## 2. 문제 정의

- 등가정적해석과 응답스펙트럼해석의 밑면전단력을 방향별로 비교해 보정계수 Cm을 산정하는 절차는
  여러 결과표와 계산 시트를 오가야 하는 반복 작업이다.
- Cm을 산정한 뒤에도 이를 적용한 설계용 하중조합을 다시 GEN NX에 수동으로 입력해야 하는 추가
  단계가 필요하다.

## 3. 목표 사용자

- 처음 이 작업 흐름을 접하는 사용자도 포함 — 원문 4대 기능의 1번이 "처음 사용자를 위한 단계별
  안내"일 정도로 신규 사용자 온보딩을 의식한 설계.
- 응답스펙트럼해석 결과에 Cm 보정계수를 적용해 설계용 하중조합을 생성해야 하는 구조 설계자.

## 4. 핵심 컨셉 / 차별점

- **상단 상태 안내바 + 맥동(pulse) 강조 효과**: 5단계(①설계조건 입력 ②모델 데이터 확인 ③Cm
  산출 ④하중조합 생성 ⑤보고서) 진행 상태를 항상 상단에 표시하고, 다음에 입력해야 할 필드를
  파란색 테두리로 맥동 강조 — 처음 쓰는 사용자도 "다음에 뭘 해야 하는지" 헤매지 않게 설계.
- **즐겨찾기(횡력저항시스템) 관리**: 반응수정계수(R)·초과강도계수(Ω0)·변위증폭계수(Cd) 등을
  포함한 "횡력저항시스템"을 검색·즐겨찾기로 저장해두고 재사용 가능 — 매번 코드표를 뒤져 R/Ω0/Cd
  값을 입력하지 않아도 됨.
- **실시간 응답스펙트럼 시각화**: 입력한 설계조건(지진구역, 지반등급, 중요도 등)에 따른
  응답스펙트럼 그래프가 구간별(단주기/전이/장주기)로 즉시 그려지고, 특정 주기(T)에서의 Sa 값을
  마우스로 조회 가능.
- **GEN NX 데이터 맵으로 출처 투명화**: "GEN NX 데이터 불러오기" 버튼 한 번으로 Cm 산정에 필요한
  5개 항목(층높이, RS 케이스, 고유치결과, 유효중량, 층전단력)을 자동 취득하되, "모델 데이터
  출처와 원본 테이블" 화면에서 **각 항목이 정확히 어떤 API로 취득됐는지**(예: `GET db/STOR`,
  `GET db/SPLC`, `POST TABLE - EIGENVALUEMODE`)와 그 원본 응답 테이블을 직접 확인할 수 있게
  공개 — 자동화의 블랙박스화를 막는 설계.
- **Cm 산정에서 하중조합 생성까지 끊김 없는 연속 흐름**: 산정된 Cm을 그대로 4단계(하중조합 생성)
  로 넘겨 RC/Steel/SRC 등 설계기준별 하중조합을 GEN NX의 `Load Combinations` 창에 실제로
  생성하고, 특수지진하중·수직지진력조합·직교효과 고려 같은 지진 설계 추가 옵션까지 한 화면에서
  선택 가능.
- **산정 근거 보고서 출력**: 계산 전 과정(설계조건, GEN NX 모델 데이터, Cm 계산 과정, 설계
  스펙트럼)을 담은 "Scale Up 산정 보고서"를 웹/PDF로 즉시 출력.

## 5. 워크플로우

### Step 0 — Apps 플랫폼에서 실행

- MIDAS GEN NX 우측 `Tree Menu 2 > Apps`에서 "Scale Up SE" 앱을 선택 → "Run" 클릭 → 플러그인
  실행.
- 실행 전 확인 안내: "GEN NX API Settings에서 API Connection 상태가 Connect인지 확인한 후 Run
  버튼을 누르세요", "응답스펙트럼해석과 고유치해석 결과가 생성된 모델에서 실행하세요."

### Step 1 — 설계조건 입력

- 지진구역, 지도값 S 직접입력, 지반종류, 중요도계수 Ie, 횡력저항시스템(R/Ω0/Cd 자동 표시)을
  입력.
- 즐겨찾기로 자주 쓰는 횡력저항시스템을 저장·불러오기 가능(즐겨찾기 관리 모달: 검색, 추가,
  제거).
- 약산주기 산정식(예: "4. 철근콘크리트 전단벽구조 및 기타 골조", Ta = 0.0488·hn^0.75)과 KDS
  41 17 00 4.2.2 (2)·(3) 조항 체크박스("기반암 깊이 20m 초과 & Vs≥360 → Fv×0.8", "S5 & 깊이
  불명 → Fa,Fv×1.1") 제공 — #4 AutoGenerationCmFactor와 동일한 KDS 41 17 00 로직을 공유.
- 입력에 따라 설계 응답스펙트럼(SDS, SD1, S, To, Ts, R/Ie 등)이 실시간 표와 그래프로 계산되며,
  특정 주기의 Sa 값(탄성 Sa vs ELF 유효값 Cs)을 툴팁으로 비교 확인 가능.

### Step 2 — 모델 데이터 확인 (GEN NX 데이터 연동)

- "Gen NX 데이터 불러오기" 버튼으로 Cm 산정에 필요한 정보를 자동으로 불러옴(수동입력도 가능).
- 불러온 항목: 층 목록/hn, RS 케이스/기준주기, Td/상당방향 Wx·Wy(유효지진중량), 유효중량
  요약(질량 API 실패 시 수동 입력 대체 가능), 침하 케이스/자동 산정.
- **"모델 데이터 출처와 원본 테이블"** 팝업에서 5개 취득 항목별 출처 API와 원본 응답 테이블을
  직접 열람 가능(6절 참고) — 확인이 필요한 경우 연동된 원본 데이터를 검증할 수 있음.
- 최종적으로 X/Y방향 RS 케이스, Td,x/Td,y, 유효지진중량 Wx/Wy, 신뢰 범위(1F~지하 5F 등)를
  화면에 요약 표시.

### Step 3 — Cm 산출

- "Cm 계산" 버튼 클릭 → 방향별 밑면전단력 기준 비교(정적 계산 결과 확인 / Cm 계산) 실행.
- 결과: Cm,x = 1.19(보통 필요), Cm,y = 1.034(보통 필요) — 방향별 Vs(등가정적)·0.85Vs(최소
  기준)·Vt(응답스펙트럼)·기준 대비 비율을 표로 함께 제시.
- 안내 문구: "층간변위에는 Cm을 적용하지 않습니다. (KDS 41 17 00 7.3.3.5(2): 얼중 진동수 제어는
  스케일 전 값 유지를 유지하세요)"(⚠️ 화면 캡처 해상도상 완전히 판독되지 않는 부분 있음, 취지는
  Cm이 층간변위 검토에는 적용되지 않는다는 KDS 조항 안내로 보임).

### Step 4 — 하중조합 생성

- 구조 설계 구분(예: RC · KDS 41 20 : 2022) 및 생성 방식(예: "기존 조합에 추가") 선택.
- Envelope 조합 추가 체크박스, X/Y방향별 적용 Factor(Cm,x=1.19, Cm,y=1.034) 자동 반영된
  RX(RS)/RY(RS) 조합 미리보기.
- 지진 설계 추가 옵션: 특수지진하중 조합 생성(DCM SDS 사용 시 특별지진하중 조합 일괄 생성),
  수직지진력 조합 생성, 직교효과 고려(선택한 RX/RY 케이스에 100:30 또는 SRSS 직교효과 조합
  적용).
- "확인 후 GEN NX ..." 버튼 클릭 → 요청 상세(API 요청 상세) 확인 후 "Gen NX 하중조합 생성"
  실행 → GEN NX의 `Load Combinations` 창(Steel/Concrete/SRC/Cold Formed Steel/Footing/
  Aluminum Design 탭 포함)에 실제로 하중조합이 생성됨.

### Step 5 — 보고서

- 표지명(프로젝트명, 회사명)을 입력하고 "Scale Up 산정 보고서"를 웹 또는 PDF로 출력.
- 보고서 구성: ① 설계조건(하중, 유효지반가속도 S, 지반등급/중요도, 횡력저항시스템, 약산주기),
  ② GEN NX 모델 데이터(X/Y방향 hn/Ta, 등가대체중량 W, 방향별 주기 Td, 밑면전단력 Vt, 상당방향
  적용), ③ 계산과정(X/Y방향별 T_use, Cu 기준, Sd1 확산, Cu 하한, Cu 적용, Vs, 0.85Vs/Vt, Cm),
  ④ 설계 응답스펙트럼(그래프), ⑤ Cm 산정 결과(요약).

## 6. 연계 JSON API 엔드포인트

**"GEN NX DATA MAP" 화면에 5개 취득 항목의 출처 API가 그대로 텍스트로 노출**되어 있어, 확인된
근거로 매핑 가능하다:

| 화면 표시(항목 번호) | 화면 표시 텍스트 | 문서 위치 |
| --- | --- | --- |
| 01 층높이 | `GET db/STOR` | [`02_DB_Project_Structure.md#14-dbstor--story-data`](../../manual/02_DB_Project_Structure.md#14-dbstor--story-data) |
| 02 RS 케이스 | `GET db/SPLC` (RS 하중케이스 · GET db/SPLC 드롭다운으로 재확인) | [`09_DB_Dynamic_Loads.md#2-dbsplc--response-spectrum-load-cases`](../../manual/09_DB_Dynamic_Loads.md#2-dbsplc--response-spectrum-load-cases) |
| 03 고유치결과 | `POST TABLE · EIGENVALUEMODE` | [`20_POST_AnalysisResult_2.md#28-vibration-mode-shape`](../../manual/20_POST_AnalysisResult_2.md#28-vibration-mode-shape) |
| 04 유효지진중량 | `NODE · MASS · SUMMARY XY` (드롭다운에 `Mass Summary X · POST post/TABLE · MASS_SUMMARY_X`, `Mass Summary Y · ...MASS_SUMMARY_Y` 노출) | [`18_POST_PreProcess.md#3-mass-summary-table`](../../manual/18_POST_PreProcess.md#3-mass-summary-table) |
| 05 층전단력 | `POST TABLE · STORY_SHEAR_FOR_RS` | [`21_POST_StoryTables.md#3-story-shear-force-rs-analysis`](../../manual/21_POST_StoryTables.md#3-story-shear-force-rs-analysis) |
| 하중조합 생성 요청 | `POST ope/LCOM-*` (화면상 "RC · KDS 41 20 : 2022" 선택 상태 기준 `LCOM-CONC`로 추정) | [`15_OPE.md#16-opelcom-conc--load-combination-concrete--kds-41-202022`](../../manual/15_OPE.md#16-opelcom-conc--load-combination-concrete--kds-41-202022) |

- "GEN NX DATA MAP" 드롭다운에는 위 5개 외에도 `홀 정보 · GET db/STOR`, `모든 고유주기 ·
  POST post/TABLE - EIGENVALUEMODE`, `모든 참여질량율 · POST post/TABLE - EIGENVALUEMODE`,
  `절점 정보 · GET db/NODE` 등 추가 후보 항목이 노출되어, 이 5개 매핑 슬롯이 각각 여러 원본
  테이블 중 선택 가능한 구조임을 확인.
- ⚠️ 하중조합 생성 API는 화면상 `POST ope/LCOM-*`으로 끝부분이 잘려 노출되어(아이콘에 가려짐)
  정확한 스킴명(LCOM-CONC/LCOM-GEN/LCOM-STEEL/LCOM-SRC 중 하나)은 "구조 설계 구분"이 RC ·
  KDS 41 20 : 2022로 선택된 정황에 근거한 추정이다.

## 7. 입력 데이터 규격

- **선행 조건**: 응답스펙트럼해석과 고유치해석 결과가 이미 생성된 GEN NX 모델.
- **설계조건**: 지진구역, 지도값 S, 지반종류, 중요도계수 Ie, 횡력저항시스템(R/Ω0/Cd), 약산주기
  산정식.

## 8. 출력 / 생성 결과

- Cm,x / Cm,y 보정계수 값.
- GEN NX `Load Combinations`(Concrete/Steel/SRC 등)에 Cm 적용 하중조합 자동 생성(RX(RS)×Cm,x,
  RY(RS)×Cm,y 등).
- "Scale Up 산정 보고서"(웹/PDF).

## 9. 제약사항 및 한계

- Cm 계산 화면에 "층간변위에는 Cm을 적용하지 않습니다"라는 KDS 41 17 00 관련 경고가 명시되어
  있어, 이 Plug-in이 생성하는 하중조합은 강도 설계용이며 층간변위(사용성) 검토에는 별도 하중
  케이스를 써야 함을 시사.
- #4(AutoGenerationCmFactor)와 목적이 겹치는 부분이 있으나, ScaleUp은 MIDAS 공식 Apps
  플랫폼(등록형 마법사 UI)에서 동작하고 하중조합 생성·보고서까지 포함하는 더 넓은 범위를
  다룸 — 두 Plug-in의 관계(경쟁/보완)는 원문에 명시되지 않아 판단 보류.

## 10. 화면 인벤토리

| 시점(초) | 화면 내용 |
| --- | --- |
| 0–8 | Apps 목록에서 "Scale Up SE" 선택, 실행 전 확인 안내 |
| 8–40 | 플러그인 실행, 설계조건 입력 UI(지진구역/지반/중요도/횡력저항시스템, 즐겨찾기) |
| 40–72 | 응답스펙트럼 실시간 그래프·구간별 Sa 조회, "다음: 모델 데이터 확인" 진입 |
| 72–96 | GEN NX 데이터 불러오기, "GEN NX DATA MAP"(원본 API·테이블 5종 노출) |
| 96–120 | 모델 데이터 확인 화면 요약, Cm 계산 실행 |
| 120–144 | Cm,x/Cm,y 산출 결과, 밑면전단력 비교표, "다음: 하중조합 생성" |
| 144–168 | 하중조합 생성 옵션(구조 설계 구분, Envelope, 지진 설계 추가 옵션), GEN NX Load Combinations 창에 실제 생성 |
| 168–189 | 보고서 표지 입력 → 인쇄/PDF 출력 → 최종 산정 보고서 내용 확인 |

---

*다음: 08_ScaffoldModel 영상 분석 및 기획문서 작성.*
