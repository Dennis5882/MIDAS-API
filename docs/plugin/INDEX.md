# MIDAS Plug-in Manual Index

> **출처:** [Plug-in Online Manual](https://support.midasuser.com/hc/en-us/articles/35639730101529-Plug-in-Online-Manual) ·
> Zendesk 섹션 [Plug-in](https://support.midasuser.com/hc/en-us/sections/35681419399961-Plug-in)
> (`section_id = 35681419399961`)
> **최초 생성:** 2026-08-04
> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX

---

## 이 폴더는 무엇인가

`docs/manual/`이 MIDAS NX Open API의 **JSON 스키마 레퍼런스**(Zendesk "JSON Manual" 섹션,
`section_id = 30087500371097`)를 다루는 것과 별개로, 이 폴더는 **MIDAS Plug-in** — MIDAS API와
Python을 결합해 만든, GUI에 내장된 완성형 자동화 도구 — 를 다룬다.

Plug-in도 내부적으로 MIDAS API를 호출한다는 점에서 "API를 활용한 접근"이라는 큰 틀은 JSON
Manual과 같지만, 문서 성격은 다르다:

| | `docs/manual/` (JSON Manual) | `docs/plugin/` (이 폴더) |
| --- | --- | --- |
| 대상 독자 | REST API를 직접 호출하는 개발자 | GUI에서 완성된 도구를 쓰는 엔지니어(+직접 Plug-in을 만들려는 개발자) |
| 원문 성격 | 엔드포인트별 Key/Value 스키마 표 | 스크린샷 기반 GUI 사용법 워크스루 |
| 문서 단위 | 챕터(엔드포인트 그룹) | 개별 Plug-in 툴 1개 = 파일 1개 |
| Zendesk 섹션 | JSON Manual (651개 아티클) | Plug-in (Introduction 4건 + Plug-in Item 53건) |

**따라서 `docs/manual`의 "TABLE_TYPE 표 → Response HEAD → Request/Response JSON → Python 예제"
관례를 그대로 적용하지 않는다.** 대신 [아래 템플릿](#toolsmd-개별-문서-템플릿)을 따른다.

---

## 진행 상태

이 INDEX.md는 카탈로그이자 작업 트래커다. "상태" 컬럼이 ⬜(미작성)인 항목은 아직 개별 문서가
없다 — 원문 링크만 확인된 상태다. 필요할 때(사용자 요청 시) 해당 원문을 다시 스크래핑해
`tools/*.md` 템플릿에 맞춰 채우고, 이 표의 상태를 ✅로 갱신한다. 규모가 크면 CLAUDE.md의
리서치/편집 분리 서브에이전트 패턴을 그대로 재사용한다.

- Guide: 4/4 작성 완료
- Plug-in Item: 5/52 작성 완료 (원문 53건 중 "Image Capture Generator"는 "Easy Capture
  Generator"와 동일 URL의 별칭이라 1건으로 병합)

---

## Guide — 개념·개발 가이드 (4건)

| No. | 이름 | 파일 | 상태 | 원문 링크 |
| --- | --- | --- | --- | --- |
| 1 | Introduction to MIDAS Plug-in | [guide/01_Introduction.md](guide/01_Introduction.md) | ✅ 작성 완료 | [원문](https://support.midasuser.com/hc/en-us/articles/35693347852569-Introduction-to-MIDAS-Plug-in) |
| 2 | How to use MIDAS Plug-ins | [guide/02_How_to_Use.md](guide/02_How_to_Use.md) | ✅ 작성 완료 | [원문](https://support.midasuser.com/hc/en-us/articles/35694950947353-How-to-use-MIDAS-Plug-ins) |
| 3 | Guiding for writing Python Code (Planning/Development Collaboration) | [guide/03_Python_Coding_Guide.md](guide/03_Python_Coding_Guide.md) | ✅ 작성 완료 | [원문](https://support.midasuser.com/hc/ko/articles/44321576105497-Guiding-for-writing-Python-Code-Planning-Development-Collaboration) |
| 4 | A Guide to Creating Plug-in for Developers | [guide/04_Developer_Guide.md](guide/04_Developer_Guide.md) | ✅ 작성 완료 | [원문](https://support.midasuser.com/hc/ko/articles/44321750649369-A-Guide-to-Creating-Plug-in-for-Developers) |

---

## Plug-in Item — 개별 툴 (53건, 고유 52건)

원문 페이지는 하위 카테고리 없이 알파벳순 flat 목록이라, 이 표도 원문 순서를 그대로 따른다.
파일명은 번호를 매기지 않고 툴 이름을 슬러그화한 것 — 신규 Plug-in이 추가돼도 기존 파일 재번호가
필요 없다.

| No. | 이름 | 파일 | 상태 | 원문 링크 |
| --- | --- | --- | --- | --- |
| 1 | 6x6 General Spring for Pile Foundation (KR) | [tools/6x6_General_Spring_for_Pile_Foundation_KR.md](tools/6x6_General_Spring_for_Pile_Foundation_KR.md) | ✅ 작성 완료 | [원문](https://support.midasuser.com/hc/en-us/articles/35651992652441-Pile-Spring) |
| 2 | Alignment Editor | [tools/Alignment_Editor.md](tools/Alignment_Editor.md) | ✅ 작성 완료 | [원문](https://support.midasuser.com/hc/en-us/articles/60307252076441-Alignment-Editor) |
| 3 | Alignment Local Axis for Element | [tools/Alignment_Local_Axis_for_Element.md](tools/Alignment_Local_Axis_for_Element.md) | ✅ 작성 완료 | [원문](https://support.midasuser.com/hc/en-us/articles/35679369131289-Alignment-Local-Axis-for-Element) |
| 4 | Alignment Generator | [tools/Alignment_Generator.md](tools/Alignment_Generator.md) | ✅ 작성 완료 | [원문](https://support.midasuser.com/hc/en-us/articles/40709970824729-Alignment-Generator) |
| 5 | Artificial Earthquake Generator | [tools/Artificial_Earthquake_Generator.md](tools/Artificial_Earthquake_Generator.md) | ✅ 작성 완료 | [원문](https://support.midasuser.com/hc/en-us/articles/35656036758937-Artificial-Earthquake-Generator) |
| 6 | Artificial Earthquake Correlation Checker | [tools/Artificial_Earthquake_Correlation_Checker.md](tools/Artificial_Earthquake_Correlation_Checker.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35650468767385-Artificial-Earthquake-Correlation-Checker) |
| 7 | [AS/NZS 1170.2:2021] Building Wind Loads Generator | [tools/AS_NZS_1170_22021_Building_Wind_Loads_Generator.md](tools/AS_NZS_1170_22021_Building_Wind_Loads_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/46935970426905--AS-1170-2-2021-Building-Wind-Loads-Generator) |
| 8 | [AS 1170.4:2024] Static Seismic Loads Generator | [tools/AS_1170_42024_Static_Seismic_Loads_Generator.md](tools/AS_1170_42024_Static_Seismic_Loads_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/46857988729753--AS-1170-4-2024-Static-Seismic-Loads-Generator) |
| 9 | Assign Floor Loads | [tools/Assign_Floor_Loads.md](tools/Assign_Floor_Loads.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/52564358801049-Assign-Floor-Loads) |
| 10 | Auto Saver | [tools/Auto_Saver.md](tools/Auto_Saver.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35661003551385-Auto-Saver) |
| 11 | Breakdown Load Combination | [tools/Breakdown_Load_Combination.md](tools/Breakdown_Load_Combination.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35845551989401-Breakdown-Load-Combination) |
| 12 | Concrete Material Set EN1992-1-1 | [tools/Concrete_Material_Set_EN1992_1_1.md](tools/Concrete_Material_Set_EN1992_1_1.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/45536334603161-Concrete-Material-Set-EN1992-1-1) |
| 13 | Concurrent Force Calculator | [tools/Concurrent_Force_Calculator.md](tools/Concurrent_Force_Calculator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/60341711486361-Concurrent-Force-Calculator) |
| 14 | Convert Load Combination into SDS Format | [tools/Convert_Load_Combination_into_SDS_Format.md](tools/Convert_Load_Combination_into_SDS_Format.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/45496104876313-Convert-Load-Combinations-into-SDS-Format) |
| 15 | Customized Load Combination | [tools/Customized_Load_Combination.md](tools/Customized_Load_Combination.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/41509743351193-Customized-Load-Combination) |
| 16 | CS Report Generator | [tools/CS_Report_Generator.md](tools/CS_Report_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/56841756166681-CS-Report-Generator) |
| 17 | Dynamic Analysis of Rail Bridge | [tools/Dynamic_Analysis_of_Rail_Bridge.md](tools/Dynamic_Analysis_of_Rail_Bridge.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/60340982021529-Dynamic-Analysis-of-Rail-Bridge) |
| 18 | Easy Capture Generator[^1] | [tools/Easy_Capture_Generator.md](tools/Easy_Capture_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35639906272025-Easy-Capture-Generator) |
| 19 | Easy Load Combinations | [tools/Easy_Load_Combinations.md](tools/Easy_Load_Combinations.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/45543036560921-Easy-Load-Combinations) |
| 20 | Element Information | [tools/Element_Information.md](tools/Element_Information.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35649982873625-Element-Information) |
| 21 | [Eurocode] Fatigue Analysis for Composite Girder Bridge | [tools/Eurocode_Fatigue_Analysis_for_Composite_Girder_Bridge.md](tools/Eurocode_Fatigue_Analysis_for_Composite_Girder_Bridge.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/49393118303897-Road-bridge-Concrete-Fatigue-for-Composite-Section) |
| 22 | Flared Pier | [tools/Flared_Pier.md](tools/Flared_Pier.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/45352026157593-Flared-Pier) |
| 23 | Floor Transition | [tools/Floor_Transition.md](tools/Floor_Transition.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35681919947673-Floor-Transition) |
| 24 | GEN NX to Staad Converter | [tools/GEN_NX_to_Staad_Converter.md](tools/GEN_NX_to_Staad_Converter.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/56728677543321-GEN-NX-to-Staad-Converter) |
| 25 | Group Pile | [tools/Group_Pile.md](tools/Group_Pile.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/45354275911321-Group-Pile) |
| 26 | Inertial Forces Controller | [tools/Inertial_Forces_Controller.md](tools/Inertial_Forces_Controller.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/40706127836953-Inertial-Forces-Controller) |
| 27 | Iterative Response Spectrum | [tools/Iterative_Response_Spectrum.md](tools/Iterative_Response_Spectrum.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/50959239482393-Iterative-Response-Spectrum) |
| 28 | Line to Plate Converter | [tools/Line_to_Plate_Converter.md](tools/Line_to_Plate_Converter.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/60469083421593-Line-To-Plate-Converter) |
| 29 | Load Effect for Load Combination | [tools/Load_Effect_for_Load_Combination.md](tools/Load_Effect_for_Load_Combination.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35649669387289-Load-Effect-for-Load-Combination) |
| 30 | Local Axis | [tools/Local_Axis.md](tools/Local_Axis.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/45537498601881-Local-Axis) |
| 31 | Mirror Tapered Section | [tools/Mirror_Tapered_Section.md](tools/Mirror_Tapered_Section.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35651585867801-Mirror-Tapered-Section) |
| 32 | [MS 1553:2002] Building Wind Loads Generator | [tools/MS_15532002_Building_Wind_Loads_Generator.md](tools/MS_15532002_Building_Wind_Loads_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/47130265330841--MS-1553-2002-Building-Wind-Loads-Generator) |
| 33 | Nastran Importer | [tools/Nastran_Importer.md](tools/Nastran_Importer.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/45548001795865-Nastran-Importer) |
| 34 | Node Controller | [tools/Node_Controller.md](tools/Node_Controller.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35654598923161-Node-Controller) |
| 35 | P-Y Curve Generator | [tools/P_Y_Curve_Generator.md](tools/P_Y_Curve_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/52596776672537-P-Y-Curve-Generator) |
| 36 | Rebar Auto Generator | [tools/Rebar_Auto_Generator.md](tools/Rebar_Auto_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/60470400396953-Rebar-Auto-Generator) |
| 37 | Rebar Spacing Converter | [tools/Rebar_Spacing_Converter.md](tools/Rebar_Spacing_Converter.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35649267067545-Rebar-Spacing-Converter) |
| 38 | Response Spectrum Generator | [tools/Response_Spectrum_Generator.md](tools/Response_Spectrum_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/45716286965273-Response-Spectrum-Generator) |
| 39 | Rigid Link Generator | [tools/Rigid_Link_Generator.md](tools/Rigid_Link_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35651417232025-Rigid-Link-Generator) |
| 40 | Seismic Hazard Map | [tools/Seismic_Hazard_Map.md](tools/Seismic_Hazard_Map.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35658068066841-Seismic-Hazard-Map) |
| 41 | Series Load | [tools/Series_Load.md](tools/Series_Load.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/45545604010521-Series-Load) |
| 42 | SPACE GASS Converter | [tools/SPACE_GASS_Converter.md](tools/SPACE_GASS_Converter.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35824220762521-SPACE-GASS-Converter) |
| 43 | Stiffness Auto Tuner | [tools/Stiffness_Auto_Tuner.md](tools/Stiffness_Auto_Tuner.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/58178248491161-Stiffness-Auto-Tuner) |
| 44 | Substructure Generator | [tools/Substructure_Generator.md](tools/Substructure_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/60317101122329-Substructure-Generator) |
| 45 | [TAIWAN2014] Building Wind Loads Generator | [tools/TAIWAN2014_Building_Wind_Loads_Generator.md](tools/TAIWAN2014_Building_Wind_Loads_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/52808991968665--TAIWAN2014-Building-Wind-Loads-Generator) |
| 46 | Temperature Gradient Stress Generator | [tools/Temperature_Gradient_Stress_Generator.md](tools/Temperature_Gradient_Stress_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/40708129121817-Temperature-Gradient-Stress-Generator) |
| 47 | Temperature Load Calculator for Bridges (HK) | [tools/Temperature_Load_Calculator_for_Bridges_HK.md](tools/Temperature_Load_Calculator_for_Bridges_HK.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/40663607747737-Temperature-Load-Calculator-for-bridges-HK) |
| 48 | Tendon Profile | [tools/Tendon_Profile.md](tools/Tendon_Profile.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/45306728128921-Tendon-Profile) |
| 49 | Traffic Lane Generator | [tools/Traffic_Lane_Generator.md](tools/Traffic_Lane_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/60315550956825-Traffic-Lane-Generator) |
| 50 | Thailand DPT Code Auto Searching | [tools/Thailand_DPT_Code_Auto_Searching.md](tools/Thailand_DPT_Code_Auto_Searching.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/52715682940313-Thailand-DPT-Code-Auto-Searching) |
| 51 | Tunnel Lining Generator | [tools/Tunnel_Lining_Generator.md](tools/Tunnel_Lining_Generator.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/35655721814937-Tunnel-Lining-Model) |
| 52 | Wind Load Calculator for Bridges (HK) | [tools/Wind_Load_Calculator_for_Bridges_HK.md](tools/Wind_Load_Calculator_for_Bridges_HK.md) | ⬜ 미작성 | [원문](https://support.midasuser.com/hc/en-us/articles/40645303004697-Wind-Load-Calculator-for-bridges-HK) |

[^1]: 원문 페이지에는 "Image Capture Generator"라는 이름으로도 한 번 더 나열되어 있으나 같은
    URL(`35639906272025-Easy-Capture-Generator`)을 가리키는 동일 아티클이다.

---

## `tools/*.md` 개별 문서 템플릿

`docs/manual`의 Key/Value 스펙 표 관례 대신, 각 Plug-in 문서는 다음 순서를 따른다:

1. **개요** — 이 Plug-in이 무엇을 하는지 (Intro)
2. **지원 버전** — 원문의 "Developed with" (예: `MIDAS CIVIL NX 2026 (v1.1)`)
3. **주요 기능** — 원문에 Benefits 섹션이 있으면 정리
4. **사용 방법** — UI 옵션/필드별 설명. 표 형식 권장: `| 필드 | 설명 | 옵션·기본값 |`
5. **참고/제약사항** — 원문의 Note, 제약 조건
6. **관련 JSON API 엔드포인트** *(선택)* — 이 Plug-in이 내부적으로 호출하는 것으로 확인되는
   `docs/manual/*` 엔드포인트가 있으면 상호 링크. 확인 안 되면 추측해서 넣지 않는다.
7. **원문 링크**

## 자동 동기화

`docs/manual`과 마찬가지로 `scripts/manual_sync/`가 이 섹션(`plugin`)의 변경도 함께 감지한다.
자세한 내용은 [scripts/manual_sync/README.md](../../scripts/manual_sync/README.md) 참고.
