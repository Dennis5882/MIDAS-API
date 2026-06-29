# MIDAS NX Open API — JSON Manual Index

> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **최초 생성:** 2024.05.28 · **공식 최종 편집:** 2026.06.23 · **이 파일 동기화:** 2026-06-29  
> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX

---

## 목차 구조

| 파일 | 섹션 | 설명 |
|------|------|------|
| [01_DOC.md](./01_DOC.md) | DOC | 문서 생성·열기·저장·닫기·해석 실행 (11개) |
| [02_DB_Project_Structure.md](./02_DB_Project_Structure.md) | DB – Project / Structure | 프로젝트 정보·단위·구조타입·그룹·층 데이터 (10개) |
| [03_DB_Node_Element.md](./03_DB_Node_Element.md) | DB – Node / Element | 노드·요소·로컬축·도메인 (6개) |
| [04_DB_Properties.md](./04_DB_Properties.md) | DB – Properties | 재료·단면·두께·힌지·섬유단면 (31개) |
| [05_DB_Boundary.md](./05_DB_Boundary.md) | DB – Boundary | 지지·스프링·링크·해제·내진장치 (24개) |
| [06_DB_Static_Loads.md](./06_DB_Static_Loads.md) | DB – Static Loads | 정적하중케이스·자중·보하중·바닥하중·풍하중·지진하중 (21개) |
| [07_DB_Temperature_Prestress.md](./07_DB_Temperature_Prestress.md) | DB – Temperature / Prestress | 온도·텐던·PS 하중 (12개) |
| [08_DB_Moving_Loads.md](./08_DB_Moving_Loads.md) | DB – Moving Loads | 이동하중 (교량 전용, 28개) |
| [09_DB_Dynamic_Loads.md](./09_DB_Dynamic_Loads.md) | DB – Dynamic Loads | 응답스펙트럼·시간이력 (12개) |
| [10_DB_Construction_Stage.md](./10_DB_Construction_Stage.md) | DB – Construction Stage / Hydration | 시공단계·수화열 (14개) |
| [11_DB_Settlement_Misc_Loads.md](./11_DB_Settlement_Misc_Loads.md) | DB – Settlement / Misc Loads | 침하·파도·비선형 초기하중 등 (9개) |
| [12_DB_Analysis_Control.md](./12_DB_Analysis_Control.md) | DB – Analysis Control | 해석 제어 데이터 (21개) |
| [13_DB_Load_Combinations.md](./13_DB_Load_Combinations.md) | DB – Load Combinations / Results | 하중조합·결과 설정 (12개) |
| [14_DB_Pushover.md](./14_DB_Pushover.md) | DB – Pushover | 푸시오버 해석 제어·힌지·하중 (6개) |
| [15_OPE.md](./15_OPE.md) | OPE | GUI 연동 운영 함수 (18개) |
| [16_VIEW.md](./16_VIEW.md) | VIEW | 뷰 제어·캡처·결과 표시 (7개) |
| [17_DB_Bridge.md](./17_DB_Bridge.md) | DB – Bridge Specialization | 거더·캠버·케이블 결과 설정 (4개) |
| [18_POST_PreProcess.md](./18_POST_PreProcess.md) | POST – Pre-Process Tables | 중량·질량·하중·재료·단면·층 요약 (~10개) |
| [19_POST_AnalysisResult_1.md](./19_POST_AnalysisResult_1.md) | POST – Analysis Result Tables Part 1 | 반력·변위·트러스·케이블·보 결과 (~15개) |
| [20_POST_AnalysisResult_2.md](./20_POST_AnalysisResult_2.md) | POST – Analysis Result Tables Part 2 | 판·평면·축대칭·솔리드·링크·모드·텐던·시공단계 (~35개) |
| [21_POST_StoryTables.md](./21_POST_StoryTables.md) | POST – Analysis Story Tables | 층변위·층전단·층비틀림·불규칙 검토 (~17개) |
| [22_POST_TH_HY_Pushover.md](./22_POST_TH_HY_Pushover.md) | POST – TH / HY / Pushover Result Tables | 시간이력·수화열·푸시오버 결과 (~30개) |
| [23_POST_Design.md](./23_POST_Design.md) | POST – Design Tables | P-M·Steel·RC·SRC·냉간성형 설계 결과 (~10개) |
| [24_DB_Design.md](./24_DB_Design.md) | DB – Design | RC·Steel 설계 코드·부재·비지지 길이 (11개) |
| [25_Design_Steel_KDS41302022.md](./25_Design_Steel_KDS41302022.md) | Design Code – STEEL KDS 41 30:2022 | 강재 설계 코드 설정·부재·비지지길이·좌굴·설계검토 (27개) |
| [26_Design_RC_KDS41202022.md](./26_Design_RC_KDS41202022.md) | Design Code – RC KDS 41 20:2022 | RC 설계 코드 설정·보·기둥·벽체·슬래브 설계 (65개) |
| [27_Design_SRC_AIKSRC2K.md](./27_Design_SRC_AIKSRC2K.md) | Design Code – SRC AIK-SRC2K | SRC 합성부재 설계 코드 설정·보·기둥 설계 (23개) |

---

## INTRODUCTION

이 매뉴얼은 MIDAS NX 시리즈(Civil NX · Gen NX)에 대한 **MIDAS API JSON 구조 매뉴얼**입니다.  
MIDAS API는 RESTful API 기반으로 동작하며, 각 기능의 Endpoint·Method·JSON 구조·예제를 제공합니다.

### Base URL

```
https://moa-engineers.midasit.com:443/gen      # MIDAS Gen NX
https://moa-engineers.midasit.com:443/civil    # MIDAS Civil NX
```

### 인증 헤더

```http
MAPI-Key: <Gen NX 앱에서 발급받은 키>
Content-Type: application/json
```

### Endpoint 분류 개요

---

## DOC

문서(Document) 파트 작업. **POST 메서드만** 사용.  
바디는 `"Argument"` 키로 시작하며, 빈 바디인 경우 `{}` 사용.

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/doc/NEW` | New Project |
| 2 | `/doc/OPEN` | Open Project |
| 3 | `/doc/CLOSE` | Close Project |
| 4 | `/doc/SAVE` | Save |
| 5 | `/doc/SAVEAS` | Save As |
| 6 | `/doc/STAGAS` | Save Current Stage As |
| 7 | `/doc/IMPORT` | Import to JSON |
| 8 | `/doc/IMPORTMXT` | Import to mct/mgt |
| 9 | `/doc/EXPORT` | Export to JSON |
| 10 | `/doc/EXPORTMXT` | Export to mct/mgt |
| 11 | `/doc/ANAL` | Perform Analysis |

---

## DB

MIDAS NX 파일에 저장되는 데이터. MCT/MGT 기능과 동일한 역할.  
일반적으로 POST/GET/PUT/DELETE 메서드를 사용하나, **단위·구조타입 등 신규 파일 필수 데이터는 GET/PUT만 동작**.

요청 바디는 `"Assign"` 키로 시작하며, 번호 키(ID) → 데이터 구조를 사용.

### Project

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/PJCF` | Project Information |
| 2 | `/db/UNIT` | Unit System |
| 3 | `/db/STYP` | Structure Type |
| 4 | `/db/STYP-M1` | Structure Type (Hyper-S) |
| 5 | `/db/GRUP` | Structure Group |
| 6 | `/db/BNGR` | Boundary Group |
| 7 | `/db/LDGR` | Load Group |
| 8 | `/db/TDGR` | Tendon Group |

### View

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/NPLN` | Named Plane |
| 2 | `/db/CO_M` | Material Color |
| 3 | `/db/CO_S` | Section Color |
| 4 | `/db/CO_T` | Thickness Color |
| 5 | `/db/CO_F` | Floor Load Color |

### Structure

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/SPAN` | Span Information |
| 2 | `/db/STOR` | Story Data |

### Node / Element

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/NODE` | Node |
| 2 | `/db/ELEM` | Element |
| 3 | `/db/SKEW` | Node Local Axis |
| 4 | `/db/MADO` | Define Domain |
| 5 | `/db/SBDO` | Define Sub-Domain |
| 6 | `/db/DOEL` | Domain-Element |

### Properties

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/MATL` | Material Properties |
| 2 | `/db/MATL-M1` | Material Properties (Hyper-S) |
| 3 | `/db/IMFM` | Inelastic Material Properties for Fiber Model |
| 4 | `/db/IMFM-M1` | Inelastic Material Link for Auto Generation (Hyper-S) |
| 5 | `/db/TDMF` | Time Dependent Material – User Defined |
| 6 | `/db/TDMT` | Time Dependent Material – Creep/Shrinkage |
| 7 | `/db/TDME` | Time Dependent Material – Compressive Strength |
| 8 | `/db/EDMP` | Change Property |
| 9 | `/db/TMAT` | Time Dependent Material Link |
| 10 | `/db/EPMT` | Plastic Material |
| 11 | `/db/EPMT-M1` | Plastic Material (Hyper-S) |
| 12 | `/db/SECT` | Section Properties (Common / DB·User / Value / SRC / PSC / Tapered 등) |
| 13 | `/db/THIK` | Thickness (Value / Stiffened DB·User·Value) |
| 14 | `/db/TSGR` | Tapered Group |
| 15 | `/db/SECF` | Section Manager – Stiffness |
| 16 | `/db/RPSC` | Section Manager – Reinforcements |
| 17 | `/db/STRPSSM` | Section Manager – Stress Points |
| 18 | `/db/PSSF` | Section Manager – Plate Stiffness Scale Factor |
| 19 | `/db/VBEM` | Virtual Beam |
| 20 | `/db/VSEC` | Virtual Section |
| 21 | `/db/EWSF` | Effective Width Scale Factor |
| 22 | `/db/IEHC` | Inelastic Hinge Control Data |
| 23 | `/db/IEHG` | Assign Inelastic Hinge Properties |
| 24 | `/db/IEHG-BEAM-M1` | Assign Inelastic Hinges – Beam (Hyper-S) |
| 25 | `/db/IEHG-TRUSS-M1` | Assign Inelastic Hinges – Truss (Hyper-S) |
| 26 | `/db/IEHG-GL-M1` | Assign Inelastic Hinges – General Link (Hyper-S) |
| 27 | `/db/IEHG-PSS-M1` | Assign Inelastic Hinges – Point Spring Support (Hyper-S) |
| 28 | `/db/FIMP` | Inelastic Material Properties |
| 29 | `/db/FIBR` | Fiber Division of Section |
| 30 | `/db/GRDP` | Group Damping |
| 31 | `/db/ESSF` | Element Stiffness Scale Factor |

### Boundary

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/CONS` | Constraint Support |
| 2 | `/db/NSPR` | Point Spring |
| 3 | `/db/GSTP` | Define General Spring Type |
| 4 | `/db/GSPR` | Assign General Spring Supports |
| 5 | `/db/SSPS` | Surface Spring |
| 6 | `/db/ELNK` | Elastic Link |
| 7 | `/db/RIGD` | Rigid Link |
| 8 | `/db/NLLP` | General Link Properties |
| 9 | `/db/NLNK` | General Link |
| 10 | `/db/NLNK-M1` | General Link (Hyper-S) |
| 11 | `/db/CGLP` | Change General Link Property |
| 12 | `/db/FRLS` | Beam End Release |
| 13 | `/db/OFFS` | Beam End Offsets |
| 14 | `/db/PRLS` | Plate End Release |
| 15 | `/db/MLFC` | Force-Deformation Function |
| 16 | `/db/SDVI` | Seismic Device – Viscous/Oil Damper |
| 17 | `/db/SDVE` | Seismic Device – Viscoelastic Damper |
| 18 | `/db/SDST` | Seismic Device – Steel Damper |
| 19 | `/db/SDHY` | Seismic Device – Hysteretic Isolator (MSS) |
| 20 | `/db/SDIS` | Seismic Device – Isolator (MSS) |
| 21 | `/db/MCON` | Linear Constraints |
| 22 | `/db/PZEF` | Panel Zone Effects |
| 23 | `/db/CLDR` | Define Constraints Label Direction |
| 24 | `/db/DRLS` | Diaphragm Disconnect |

### Static Loads

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/STLD` | Static Load Cases |
| 2 | `/db/BODF` | Self-Weight |
| 3 | `/db/CNLD` | Nodal Loads |
| 4 | `/db/BMLD` | Beam Loads |
| 5 | `/db/SDSP` | Specified Displacements of Support |
| 6 | `/db/NMAS` | Nodal Masses |
| 7 | `/db/LTOM` | Loads to Masses |
| 8 | `/db/NBOF` | Nodal Body Force |
| 9 | `/db/PSLT` | Define Pressure Load Type |
| 10 | `/db/PRES` | Assign Pressure Loads |
| 11 | `/db/PNLD` | Define Plane Load Type |
| 12 | `/db/PNLA` | Assign Plane Loads |
| 13 | `/db/FBLD` | Define Floor Load Type |
| 14 | `/db/FBLA` | Assign Floor Loads |
| 15 | `/db/FMLD` | Finishing Material Loads |
| 16 | `/db/POSP` | Parameter of Soil Properties |
| 17 | `/db/EPST` | Static Earth Pressure |
| 18 | `/db/EPSE` | Seismic Earth Pressure |
| 19 | `/db/POSL` | Parameter of Seismic Loads |
| 20 | `/db/SWIND` | Static Wind Load (KDS 41-12:2022 / User Type) |
| 21 | `/db/SSEIS` | Static Seismic Load (KDS 41-17-00:2019 / User Type) |

### Temperature Loads

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/ETMP` | Element Temperature |
| 2 | `/db/GTMP` | Temperature Gradient |
| 3 | `/db/BTMP` | Beam Section Temperature |
| 4 | `/db/STMP` | System Temperature |
| 5 | `/db/NTMP` | Nodal Temperature |

### Prestress Loads

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/TDNT` | Tendon Property |
| 2 | `/db/TDNA` | Tendon Profile |
| 3 | `/db/TDCS` | Tendon Location for Composite Section |
| 4 | `/db/TDPL` | Tendon Prestress |
| 5 | `/db/PRST` | Prestress Beam Loads |
| 6 | `/db/PTNS` | Pretension Loads |
| 7 | `/db/EXLD` | External Type Load Case for Pretension |

### Moving Loads

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/MVCD` | Moving Load Code |
| 2 | `/db/LLAN` | Traffic Line Lanes |
| 3 | `/db/LLANch` | Traffic Line Lanes – China |
| 4 | `/db/LLANid` | Traffic Line Lanes – India |
| 5 | `/db/LLANtr` | Traffic Line Lanes – Transverse |
| 6 | `/db/LLANop` | Traffic Line Lanes – Moving Load Optimization |
| 7 | `/db/SLAN` | Traffic Surface Lanes |
| 8 | `/db/SLANch` | Traffic Surface Lanes – China |
| 9 | `/db/SLANop` | Traffic Surface Lanes – Moving Load Optimization |
| 10 | `/db/MVHL` | Vehicles (AASHTO / LRFD / Canada / BS / Eurocode / Korea 등) |
| 11 | `/db/MVHLtr` | Vehicles – Transverse |
| 12 | `/db/MVLD` | Moving Load Cases |
| 13 | `/db/MVLDch` | Moving Load Cases – China |
| 14 | `/db/MVLDid` | Moving Load Cases – India |
| 15 | `/db/MVLDbs` | Moving Load Cases – BS |
| 16 | `/db/MVLDeu` | Moving Load Cases – Eurocode |
| 17 | `/db/MVLDpl` | Moving Load Cases – Poland |
| 18 | `/db/MVLDtr` | Moving Load Cases – Transverse |
| 19 | `/db/CRGR` | Concurrent Reaction Group |
| 20 | `/db/CJFG` | Concurrent Joint Force Group |
| 21 | `/db/MVHC` | Vehicle Classes |
| 22 | `/db/SINF` | Plate Element for Influence Surface |
| 23 | `/db/MLSP` | Lane Support – Negative Moments at Interior Piers |
| 24 | `/db/MLSR` | Lane Support – Reactions at Interior Piers |
| 25 | `/db/DYLA` | Dynamic Load Allowance |
| 26 | `/db/IMPF` | Additional Impact Factor |
| 27 | `/db/DYFG` | Railway Dynamic Factor |
| 28 | `/db/DYNF` | Railway Dynamic Factor by Element |

### Dynamic Loads

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/SPFC` | Response Spectrum Functions (User / Korea / US / Eurocode / China 등) |
| 2 | `/db/SPLC` | Response Spectrum Load Cases |
| 3 | `/db/THGC` | Time History Global Control |
| 4 | `/db/THGC-M1` | Time History Global Control (Hyper-S) |
| 5 | `/db/THOO-M1` | Time History Output Option (Hyper-S) |
| 6 | `/db/THIS` | Time History Load Cases |
| 7 | `/db/THIS-M1` | Time History Load Cases (Hyper-S) |
| 8 | `/db/THFC` | Time History Functions |
| 9 | `/db/THGA` | Ground Acceleration |
| 10 | `/db/THNL` | Dynamic Nodal Loads |
| 11 | `/db/THSL` | Time Varying Static Loads |
| 12 | `/db/THMS` | Multiple Support Excitation |

### Construction Stage Loads

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/STAG` | Define Construction Stage |
| 2 | `/db/CSCS` | Composite Section for Construction Stage |
| 3 | `/db/TMLD` | Time Loads for Construction Stage |
| 4 | `/db/STBK` | Set-Back Loads for Nonlinear Construction Stage |
| 5 | `/db/CMCS` | Camber for Construction Stage |
| 6 | `/db/CRPC` | Creep Coefficient for Construction Stage |

### Heat of Hydration Loads

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/ETFC` | Ambient Temperature Functions |
| 2 | `/db/CCFC` | Convection Coefficient Functions |
| 3 | `/db/HECB` | Element Convection Boundary |
| 4 | `/db/HSPT` | Prescribed Temperature |
| 5 | `/db/HSFC` | Heat Source Functions |
| 6 | `/db/HAHS` | Assign Heat Source |
| 7 | `/db/HPCE` | Pipe Cooling |
| 8 | `/db/HSTG` | Define Construction Stage for Hydration |

### Settlement Loads

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/SMPT` | Settlement Group |
| 2 | `/db/SMLC` | Settlement Load Cases |

### Miscellaneous Loads

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/PLCB` | Pre-composite Section |
| 2 | `/db/LDSQ` | Load Sequence for Nonlinear |
| 3 | `/db/WVLD` | Wave Loads |
| 4 | `/db/IELC` | Ignore Elements for Load Cases |
| 5 | `/db/IFGS` | Large Displacement – Initial Forces for Geometric Stiffness |
| 6 | `/db/EFCT` | Small Displacement – Initial Force Control Data |
| 7 | `/db/INMF` | Small Displacement – Initial Element Force |

### Analysis Control

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/ACTL` | Main Control Data |
| 2 | `/db/ACTL-M1` | Main Control Data (Hyper-S) |
| 3 | `/db/PDEL` | P-Delta Analysis Control |
| 4 | `/db/BUCK` | Buckling Analysis Control |
| 5 | `/db/EIGV` | Eigenvalue Analysis Control |
| 6 | `/db/EIGV-M1` | Eigenvalue Analysis Control (Hyper-S) |
| 7 | `/db/HHCT` | Heat of Hydration Analysis Control |
| 8 | `/db/HHCT-M1` | Heat of Hydration Analysis Control (Hyper-S) |
| 9 | `/db/MVCT` | Moving Load Analysis Control |
| 10 | `/db/MVCTch` | Moving Load Analysis Control – China |
| 11 | `/db/MVCTid` | Moving Load Analysis Control – India |
| 12 | `/db/MVCTbs` | Moving Load Analysis Control – BS |
| 13 | `/db/MVCTtr` | Moving Load Analysis Control – Transverse |
| 14 | `/db/SMCT` | Settlement Analysis Control Data |
| 15 | `/db/NLCT` | Nonlinear Analysis Control Data |
| 16 | `/db/NLCT-M1` | Nonlinear Analysis Control (Hyper-S) |
| 17 | `/db/STCT` | Construction Stage Analysis Control Data |
| 18 | `/db/STCT-M1` | Construction Stage Analysis Control Data (Hyper-S) |
| 19 | `/db/BCCT` | Boundary Change Assignment |
| 20 | `/db/BCGD-M1` | Assign Boundary Combination (Hyper-S) |
| 21 | `/db/BCGA-M1` | Assign Boundary Combination (Hyper-S) |

### Analysis Results / Load Combinations

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/LCOM-GEN` | Load Combinations – General |
| 2 | `/db/LCOM-CONC` | Load Combinations – Concrete Design |
| 3 | `/db/LCOM-STEEL` | Load Combinations – Steel Design |
| 4 | `/db/LCOM-SRC` | Load Combinations – SRC Design |
| 5 | `/db/LCOM-STLCOMP` | Load Combinations – Composite Steel Girder Design |
| 6 | `/db/LCOM-SEISMIC` | Load Combinations – Seismic Design |
| 7 | `/db/CUTL` | Cutting Line |
| 8 | `/db/CLWP` | Plate Cutting Line Diagram |

### Bridge Specialization Results

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/GSBG` | Bridge Girder Diagrams |
| 2 | `/db/GCMB` | General Camber Control |
| 3 | `/db/CAMB` | FCM Camber Control |
| 4 | `/db/ULFC` | Cable Control – Unknown Load Factor Constraints |

### Pushover

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/POGD` | Pushover Analysis Control Data |
| 2 | `/db/POGD-M1` | Pushover Global Control (Hyper-S) |
| 3 | `/db/IEPI` | Ignore Elements for Pushover Initial Load |
| 4 | `/db/PHGE` | Assign Pushover Hinge Properties |
| 5 | `/db/POLC` | Pushover Load Cases |
| 6 | `/db/POLC-M1` | Pushover Load Case (Hyper-S) |

### Design (DB)

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/db/DCON` | RC Design Code |
| 2 | `/db/MATD` | Modify Concrete Materials |
| 3 | `/db/RCHK` | Rebar Input for Checking |
| 4 | `/db/LENG` | Unbraced Length |
| 5 | `/db/MEMB` | Member Assignment |
| 6 | `/db/DCTL` | Definition of Frame |
| 7 | `/db/LTSR` | Limiting Slenderness Ratio |
| 8 | `/db/ULCT` | Underground Load Combination Type |
| 9 | `/db/MBTP` | Modify Member Type |
| 10 | `/db/WMAK` | Modify Wall Mark Design |
| 11 | `/db/DSTL` | Steel Design Code |

---

## OPE

GUI 또는 사전처리 계산값 제어 함수. DB에 저장되지 않는 데이터.

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/ope/PROJECTSTATUS` | Project Status |
| 2 | `/ope/DIVIDEELEM` | Divide Elements |
| 3 | `/ope/SECTPROP` | Section Properties Calculation Results |
| 4 | `/ope/USLC` | Using Load Combinations |
| 5 | `/ope/LINEBMLD` | Line Beam Load |
| 6 | `/ope/AUTOMESH` | Auto-Mesh Planar Area |
| 7 | `/ope/SSPS` | Surface Spring |
| 8 | `/ope/EDMP` | Change Property |
| 9 | `/ope/STOR` | Story Calculation |
| 10 | `/ope/STORY_PARAM` | Story Check Parameter |
| 11 | `/ope/STORY_IRR_PARAM` | Story Irregularity Check Parameter |
| 12 | `/ope/STORPROP` | Story Properties |
| 13 | `/ope/MEMB` | Member Assignment |
| 14 | `/ope/GUSTFACTOR` | Gust Factor Calculator |
| 15 | `/ope/LCOM-GEN` | Load Combination (General) – KDS:2022 / AIK-SRC2K |
| 16 | `/ope/LCOM-CONC` | Load Combination (Concrete) – KDS 41 20:2022 |
| 17 | `/ope/LCOM-STEEL` | Load Combination (Steel) – KDS 41 30:2022 |
| 18 | `/ope/LCOM-SRC` | Load Combination (SRC) – KDS 41 SRC:2022 / AIK-SRC2K |

---

## VIEW

모델 뷰 제어. Capture는 Angle·Active·Display·ResultGraphic과 함께 사용 가능.

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/view/SELECT` | Select |
| 2 | `/view/CAPTURE` | Capture |
| 3 | `/view/PRECAPTURE` | Dialog Capture |
| 4 | `/view/ANGLE` | Viewpoint |
| 5 | `/view/ACTIVE` | Active |
| 6 | `/view/DISPLAY` | Display |
| 7 | `/view/RESULTGRAPHIC` | Type of Display / 반력·변위·트러스·보·판·응력 등 결과 표시 |

---

## POST

전처리·후처리 테이블 추출용. 상세 사용법: *Designing with Intent: The Vision Behind POST/TABLE* 참조.

### Pre-Process Table

| No. | 테이블 타입 |
|-----|------------|
| 1 | Element Weight Table |
| 2 | Nodal Body Force Table |
| 3 | Mass Summary Table |
| 4 | Load Summary Table |
| 5 | Material Table |
| 6 | Section Table |
| 7 | Restraint Support Table |
| 8 | Story Mass Summary Table |
| 9 | Story Load Summary Table |
| 10 | Story Weight Table |

### Analysis Result Table (주요)

반력·변위·트러스·케이블·보·판·솔리드·Elastic Link·General Link·진동모드·좌굴모드·텐던 등 24종

### Analysis Story Table

층간변위·층변위·층전단력·층모드형상·비틀림·전도모멘트·축력합·안정계수·불규칙 검토 등 16종

### Design (POST)

| No. | Endpoint | 기능 |
|-----|----------|------|
| 1 | `/post/PM` | P-M Interaction Diagram |
| 2 | `/post/STEELCODECHECK` | Steel Code Check |
| 3 | `/post/BEAMDESIGNFORCES` | Concrete – Beam Design Force |
| 4 | `/post/COLUMNDESIGNFORCES` | Concrete – Column Design Forces |
| 5 | `/post/BRACEDESIGNFORCES` | Concrete – Brace Design Forces |
| 6 | `/post/WALLDESIGNFORCES` | Concrete – Wall Design Forces |
| 7 | `/post/STEELMEMBERDESIGNFORCES` | Steel – Member Design Forces |
| 8 | `/post/SRCBEAMDESIGNFORCES` | SRC – Beam Design Forces |
| 9 | `/post/SRCCOLUMNDESIGNFORCES` | SRC – Column Design Forces |
| 10 | `/post/COLDFORMEDSTEELMEMBERDESIGNFORCES` | Cold Formed – Member Design Forces |

---

## Design (Code Design)

설계코드 기반 구조 부재 검토 API 테이블.

### STEEL
| Code | 상세 |
|------|------|
| `KDS-41-30-2022` | KDS 41 30 : 2022 |

### RC
| Code | 상세 |
|------|------|
| `KDS-41-20-2022` | KDS 41 20 : 2022 |

### SRC
| Code | 상세 |
|------|------|
| `AIK-SRC2K` | AIK-SRC2K |

---

> **범례:**  
> ᴴˢ⁾ = Hyper-S solver 전용  
> ᴶ⁾ = MIDAS Civil NX JP 버전 전용
