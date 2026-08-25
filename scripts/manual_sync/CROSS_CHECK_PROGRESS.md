# docs/manual 전체 재검증 진행 현황

`docs/manual/*.md`의 각 엔드포인트 절을 공식 Zendesk 원문과 필드 단위로 다시 대조하는 전수
재검증 작업 진행판. 계기·방법론은 `.claude/plans/scalable-leaping-melody.md`(2026-08-25 승인)
참고. `check_diff.py`의 `updated_at` 기반 정기점검으로는 "원문은 그대로인데 우리 문서 자체가
잘못 옮겨 적힌" 케이스(예: 18장 9절)를 잡을 수 없어서 시작한 별도 작업.

아티클 id 매핑은 `article_map.json`에 별도 기록. 상태: ⬜ 미착수 · 🔍 진행중 · ✅ 완료.

| 챕터 | 상태 | 절 개수 | 발견·수정 이슈 | 완료일 |
| --- | --- | --- | --- | --- |
| INDEX.md | ✅ | — | 챕터별 개수 표기 오류 3건 정정: 17장(4→5), 19장(12→13), 26장(69→70) | 2026-08-25 |
| 01_DOC.md | ✅ | 11 | 이슈 없음 — 11/11 절 원문과 완전 일치(절마다 공식 문서 링크가 이미 정확히 박혀 있어 매핑도 수월) | 2026-08-25 |
| 02_DB_Project_Structure.md | ✅ | 14 | STYP 6개 필드 기본값 오류 정정(bMASSOFFSET/bSELFWEIGHT/bALIGNBEAM/bALIGNSLAB/bROTRIGID `-`→`false`, SMASS `-`→`1`). NPLN 2건 정정(TOL 기본값 `-`→`0`, COORD Required→Optional/기본값 0). PJCF 원문 오타 확인(Key `APROVE`, 우리 문서는 이미 정상 표기라 근거 주석만 추가, 오류제보 대상). 나머지 11개 절은 완전 일치 | 2026-08-25 |
| 03_DB_Node_Element.md | ✅ | 6 | 6/6 절 필드 완전 일치. SKEW에 `iMETHOD` 기본값(1=Angle, 원문 명시) 정보성 주석만 추가 | 2026-08-25 |
| 04_DB_Properties.md | ✅ | 32 | **32/32절 완료.** 실제 오류·누락 정정 다수(전체 챕터 중 가장 많은 발견): TDMT§6 CODE코드표 5개 누락 보강 · **TDME§7 전면정정(KDS-2016이 A/B계수 오기재→실제 iCTYPE+DENSITY)** · EPMT§10 전면보강(Drucker/Masonry/ConcDamage 모델 통째 누락, HARDENING_COEF Required 오기재) · TSGR§14 Y축 3필드 누락 · SECF§15 J단 11필드 누락 · RPSC§16 SBW/TR/SR/MBAR 전체 누락 · IEHC§22 Wall계열 11필드 누락+예제 필드명 오류 · FIMP§28 Kent&Park 4필드 누락 · FIBR§29 FIBR_BASE 8필드+모니터링 2필드 누락, FIBR_BASE_KEY 타입 오기재(Boolean→Integer) · GRDP§30 Rayleigh감쇠 계열 18필드+우선순위 4필드 누락(가장 큰 누락) · ESSF§31 iPart 누락 · MATD§32 원문 오타(RABAR_CODENAME) 확인+DESIGN 미문서화 4필드 발견. SECT§12는 공통부 100% 일치 확인, 형상별 세부 파라미터는 원문이 8개 서브아티클·최대 9700줄 규모라 대표 예시 수준 유지(TDMT/FIMP 다중모델과 동일 원칙). `-M1`(Hyper-S) 스텁 4개는 기존 의도적 패턴 확인, 미확장 | 2026-08-25 |
| 05_DB_Boundary.md | ✅ | 24 | **24/24절 완료.** 실제 오류 다수 발견·정정: **NSPR§2 전면 정정 — COMP/TENS/MULTI 구조가 완전히 잘못됨(가짜 필드 "SK" 삭제, 실제는 STIFF/FUNCTION+DIR(0-6 Vector 포함))** · **GSTP§3 21항 배열 인덱스 매핑이 실제와 다름(대각항 6개 우선 배치, 표준 상삼각 아님) — 실무 영향 큰 정정** · SSPS§5 WIDTH 필드 누락 · ELNK§6 원문 표 오타(MULTI LINEAR/RAIL INTERACT 공백) 확인+RAILINTERACT DIR enum 범위 다름 명시 · **SDVE§17 14필드 누락(3→17개)** · **SDST§18 원문 표가 SDVE 내용과 혼선(가짜 MATERIAL_TYPE) — 실제 K0/P1/ALPHA1/KB+이력모델별 하위객체로 전면 정정** · SDVI§16 Exponential Function 6필드+최상위 1필드 누락 · SDHY§19 7필드 누락(원문 MULTIPL은 스키마·예제에 없어 제외) · **SDIS§20 전면 정정(SDIS_DEV_TYPE 3번째 값 SB→SLD, LRB의 DX 중첩객체 구조 오류, NRB 8필드 중 1개만 기재, SB 5필드 중 2개 누락)** · MCON§21 EX/WD 타입별 SLAVES 필드 오류(COEFF+DOF vs WEIGHT 구분 안 됨) · NLLP§8 공통필드 3개 누락(대형 아티클이라 장치별 상세는 SECT/TDMT 원칙대로 미전개) · **NLNK-M1§10 — "원문 예제 없음" 스텁이었으나 실제로는 928줄 온전한 스펙 존재, NLNK와 거의 동일 구조로 전면 보강**. NLNK§9는 재확인 결과 VECTOR_VALUES 등 기존 표기가 정확해 수정 없음(표 오류만 원문 쪽에 있었음, 예제 대조로 확인) | 2026-08-25 |
| 06_DB_Static_Loads.md | ✅ | 21 | **21/21절 완료.** 대부분 완전 일치(STLD 67종 Load Type 전수 확인 포함, SWIND·SSEIS KDS 변형도 필드 단위 100% 일치 확인). 실제 오류 3건: PSLT§9 Key 오류(표는 CMD, 실제는 LOADCASENAME — 우리 문서 자체의 표/예제 불일치였음) · PNLA§12 조건 라벨 오류(원문이 "SELECT_TYPE=SOLID"라고 잘못 적음 — SELECT_TYPE enum에 SOLID가 없어 실제로는 ELEM_TYPE=SOLID로 정정, 오류제보 대상) · EPSE§18 예제 자체 오타(SEL_TYPE "ELEM"→"ELEMENT"). INHERENT_TORSION 오타(21절, 오늘 오전 정기점검에서 이미 확인)는 오류제보 대상으로 별도 관리 | 2026-08-25 |
| 07_DB_Temperature_Prestress.md | ✅ | 12 | **12/12절 완료.** 대부분 완전 일치(ETMP/GTMP/BTMP/STMP/NTMP/TDCS/TDPL/PRST/PTNS/EXLD 10개 절은 스키마·예제·표 모두 원문과 100% 일치, TDNT§6은 14개 코드표준 전체 RM/RV/FT/TDMFK 매핑까지 완전 일치). 실제 누락 1건: **TDNA§7 — Round 타입 프로파일 좌표 구조(`RADIUS`/`OPT`/`ANGLE`/`HEIGHT`/`RADIUS2`) 전체 누락**, 기존엔 Spline 타입(`bFIX`/`R`)만 문서화되어 있었음(2D/3D 모두 보강). 원문 표의 `RADIUS` Value Type "Boolean" 표기는 예제(숫자값)와 모순되는 원문 오타로 판단, Number로 기재. | 2026-08-25 |
| 08_DB_Moving_Loads.md | ✅ | 28 | **28/28절 완료.** 이 챕터에서 가장 큰 발견: **§10 MVHL(Vehicles)** — `VEH_DEFAULT`가 15개 국가/코드 중 5개(AASHTO Std/LRFD·PENNDOT·Korea·Taiwan)에만 쓰이고 나머지 10개(KSCE-LSD15 기존 확인 + Canada·Australia·South Africa·China·Poland·BS·Eurocode·Russia·India)는 각자 전용 `VEH_XX` 객체를 쓰는데 문서엔 전혀 없었음 — 5개(Canada/Australia/SouthAfrica/China/Poland)는 전체 하위모드, 4개(BS/Eurocode/Russia/India, 원문 자체가 매우 방대)는 대표 모드만 보강(SECT/TDMT 원칙, 사용자 확인). **§12 MVLD** Australia(LOAD_MODEL/LOAD_COMB_TYPE/FATIGUE/ASL)·Russia(LOAD_COMB_TYPE) 전용 필드 누락 보강 + 지원 매트릭스 추가. **§13 MVLDch**·**§14 MVLDid**·**§17 MVLDpl** 각각 Moving Load Optimization/서브필드/Permit 객체 누락 보강. **§15 MVLDbs** LOADMODEL enum 누락값(ALL_MODE_2) + LCDATA_* 6개 객체 중 5개 미문서 보강(대표 1개 전체+나머지 요약). **§7 TDNA**(7장, 관련) 스타일의 완전 일치 절도 다수(ETMP/GTMP/BTMP 등 1~9,11,18~28절 대부분 100% 일치). §16 MVLDeu는 이미 매우 정확했고 사소한 주석 오류 1건만 정정. §26 IMPF PARTS 필드가 Truss 예제엔 없음을 주석 추가. | 2026-08-25 |
| 09_DB_Dynamic_Loads.md | ✅ | 12 | **12/12절 완료.** §1 SPFC(Response Spectrum Functions) — China/Japan/Taiwan/India/Other Countries 5개 국가 계열이 통째로 누락돼 있었음(MVHL과 동일 패턴). Japan(4코드)·India(3코드)는 전체, China(9코드)·Taiwan(7코드)·Other Countries(8코드)는 대표 코드 1개만 상세화(SECT/TDMT 원칙) — 총 9개 SPEC_CODE 계열 모두 매핑표 이상 보강. §2 SPLC 원문 표 자체 오류 2건 정정(ACCECC_PERTCENT→ACCECC_PERCENT, bACCECC_CONSIDER_GL 중복 오기→bACCECC_MINIMUM_TORSION, 둘 다 예제 없어 스키마 근거). §3 THGC 완전 일치. §4 THGC-M1 HINGE_OPT 서브필드 설명 오류 정정(enum·기본값 누락). §5 THOO-M1 완전 일치. **§6 THIS — Key 오타 발견(`aMDAMPING`→실제는 `aDAMP`, 실사용 시 파라미터 무시되는 실질 버그) + Mass&Stiffness Proportional 감쇠 서브필드·Static 모드 증분제어(SCALE/iCTRL/TINC/MNODE/MDIR)·Nonlinear 공통 반복제어 블록(iMAXITER~dTOL) 전체 누락 보강, iMDTYPE 4번째 값(Element M&S) 추가**. §7 THIS-M1(234K자 원문, 최대 규모) — ANAL_METHOD 3번째 값(Static=2) 누락, GEOM_NL_TYPE(Schema/DB 값 스왑 주의 원문 그대로 명시)·M&S감쇠 세부·Static 증분제어(INC_CTRL)·Direct Integration 적분법(TIME_PARAM)·BOUNDARY_NL_ANAL 블록 보강. §8 THFC·§9 THGA·§10 THNL·§11 THSL·§12 THMS는 완전 일치(THMS는 Y/Z 방향 Optional 처리도 이미 정확). | 2026-08-25 |
| 10_DB_Construction_Stage.md | ⬜ | 14 | | |
| 11_DB_Settlement_Misc_Loads.md | ⬜ | 9 | | |
| 12_DB_Analysis_Control.md | ⬜ | 21 | | |
| 13_DB_Load_Combinations.md | ⬜ | 8 | | |
| 14_DB_Pushover.md | ⬜ | 6 | | |
| 15_OPE.md | ⬜ | 19 | | |
| 16_VIEW.md | ⬜ | 7 | | |
| 17_DB_Bridge.md | 🔍 | 5 | 5절(/ope/GSBG) Sbz 부호 오타 확인 완료 — 공식 오타, 오류제보 대상. 1~4절 미착수 | |
| 18_POST_PreProcess.md | 🔍 | 10 | 9절(Story Load Summary Table) 전면 오류 발견·정정 완료(우리 쪽 스크래핑 실수, UNIT/STYLES/COMPONENTS/LOAD_CASE_NAMES 허구 기재 + TABLE_TYPE 오기). 나머지 9개 절 미착수 | |
| 19_POST_AnalysisResult_1.md | ⬜ | 13 | | |
| 20_POST_AnalysisResult_2.md | ⬜ | 39 | | |
| 21_POST_StoryTables.md | ⬜ | 17 | | |
| 22_POST_TH_HY_Pushover.md | ⬜ | 28(그룹 A-D) | | |
| 23_POST_Design.md | ⬜ | 10 | | |
| 24_DB_Design.md | ⬜ | 13 | | |
| 25_Design_Steel_KDS41302022.md | ⬜ | 27 | | |
| 26_Design_RC_KDS41202022.md | ⬜ | 70(0~69) | | |
| 27_Design_SRC_AIKSRC2K.md | ⬜ | 27 | | |

## 다음 세션 시작점

`10_DB_Construction_Stage.md`(14절)부터 순서대로. INDEX.md + 01~09장 완료. 17장·18장은 오늘
별건 확인 중 부분적으로 들여다본 절만 검증됐고 나머지 절은 미착수 상태이니, 전체 순서상 도달하면
이미 확인된 절은 재작업 없이 표만 갱신.
