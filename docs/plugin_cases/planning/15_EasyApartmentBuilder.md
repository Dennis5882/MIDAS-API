# EasyApartmentBuilder 기획문서

> 영상(`docs/plugin_cases/videos/15_EasyApartmentBuilder.mp4`, 60fps, 3840×2160, 약 313초)을
> 10초 간격으로 프레임 캡처(총 32장) 후 프레임별 육안 분석 + 화면 하단 자막을 근거로 작성.
> 원문 아티클(`docs/plugin_cases/articles/15_EasyApartmentBuilder.md`)의 4대 기능 설명과 교차
> 확인함. #1(WALL STACKER)과 목적·워크플로우가 유사한 "DXF → 아파트 벽식 골조 자동 모델링"
> 계열 Plug-in이지만, **Wall Mark(사용자 표기명) → Wall ID(GEN NX 설계 단위) 2단계 분리**와
> **기준층 복사** 기능에 특화되어 있다는 점이 다르다.

## 1. 개요

**Easy Apartment Builder(EAB)**는 구조평면도 기반 DXF를 바탕으로 Wall Mark/ID 자동화를 통해
쉽고 빠른 아파트 해석모델링을 구현하는 Plug-in이다. 벽체의 표기명(Wall Mark)을 자동 생성하고,
GEN NX의 벽체설계 로직(Wall ID별 설계)을 만족하도록 Wall ID를 자동 할당하며, 기준층을 지정해
여러 층에 동일한 Wall Mark/ID를 반복 적용할 수 있다.

## 2. 문제 정의

- 아파트처럼 벽체 수가 많은 벽식 구조는 DXF 도면의 벽체 하나하나에 이름(Mark)을 붙이고, GEN
  NX 설계 단위인 Wall ID를 배정하는 작업이 반복적이고 시간이 오래 걸린다.
- Wall Mark(도면 표기용 이름)와 Wall ID(GEN NX 벽체 설계 로직의 실제 단위)는 서로 다른
  개념인데, 이를 사람이 수작업으로 일일이 매핑하면 오류가 발생하기 쉽다.
- 여러 층(기준층 반복 등)에 동일한 벽체 구성이 반복되는데, 매 층 새로 작업하면 비효율적이다.

## 3. 목표 사용자

- 아파트(벽식 구조)의 구조평면도 DXF를 GEN NX 해석모델로 빠르게 옮겨야 하는 구조 모델러.
- Wall Mark·Wall ID 체계를 프로젝트 표준에 맞게 정리하며 모델링해야 하는 실무자.

## 4. 핵심 컨셉 / 차별점

- **CAD 요소 타입별 자동 매핑**: DXF의 선 요소(Line, Poly Line)는 벽체·보 요소로, 점
  요소(Point)는 기둥으로 자동 인식·고려 — 레이어 선택 시 "Wall / Beam & Column" 3분류 팝업으로
  사용자가 확정.
- **Wall Mark → Wall ID 2단계 워크플로우**: ① 평면에서 벽체를 선택해 Wall Mark(예: W1, CW1)를
  자동 또는 수동 할당하고(같은 Mark로 여러 벽체를 병합 가능) → ② "Wall ID 자동생성" 버튼으로
  Wall Mark 할당 순 1001번부터 자동 채번된 Wall ID를 부여. Mark(사람이 읽는 표기)와 ID(GEN NX
  설계 단위)를 명확히 분리해, 도면 표기 관례를 유지하면서도 GEN NX 벽체 설계 로직을 만족.
- **기준층 지정 및 복사**: DXF 파일(층)마다 "기준층" 배지를 지정하면, 해당 층에서 정의한 Wall
  Mark/ID/Material/Thickness를 다른 층에 동일하게 그대로 복사해 적용 — 반복 입력을 없앰. 영상
  시연에서 기준층(01 1F to 17F.dxf)에서 만든 250여 개 Wall Mark를 "02 18F to 25F.dxf" 층에
  복사하는 장면으로 확인됨(할당 개수 250개 → 152개로 재구성).
- **Material/Thickness를 Plug-in 화면에서 직접 배정**: 별도 GEN NX 화면을 오가지 않고, Wall
  Mark를 선택한 채로 Material(C30, C27 등)과 Thickness(T200, T250 등)를 바로 배정 — 원문 4번
  기능("모델링이 어떻게 구현될지 Material, Properties, Thickness를 확인할 수 있으며")과 일치.
- **Beam/Col도 한 번에 고려**: 별도 "Beam/Col" 탭에서 각 DXF 층(01 1F to 17F / 02 18F to 25F
  / 03 옥탑층)마다 Line 요소를 Beam으로 매핑할 Material·Section을 지정해, 벽체뿐 아니라 보·
  기둥까지 하나의 워크플로우 안에서 함께 처리.
- **사용자 편의기능(단축키·상호작용)**: 마우스 휠(Zoom In/Out), Ctrl+Z(Undo), Load/Save As
  (기존 작업 저장·불러오기), 클릭/좌우 드래그/우좌 드래그로 평면 요소 선택(NX와 동일한 조작
  체계), 요소별 View Active/Inactive, Story Data·Wall 데이터 입력 시 Tab/Enter로 입력칸 이동,
  dxf 층을 클릭 후 드래그로 여러 층 한 번에 선택, Wall 탭에서 Wall Mark 현황 중 평면에서 선택한
  Mark를 목록 맨 위로 이동하는 등 실무 편의 기능을 다수 제공.
- **모델 빌드 전 최종 확인 및 영향 범위 요약**: "Model Build 확인" 모달에서 벽체 분할(Wall
  Segment Length) 값을 지정하면 생성 예정 Element 개수(Wall+Beam/Column)와 Wall Mark/Wall ID/
  Story 항목 수까지 사전에 요약해 보여준 뒤 "Build 실행".

## 5. 워크플로우

### Step 1 — Apps에서 실행 및 DXF 불러오기

- GEN NX `Apps > My Work`에서 "EAB" Plug-in 실행 → 별도 웹뷰(브라우저 기반 Floor Plan Editor)
  창이 열림.
- "우측에서 DXF 파일을 불러오세요" 안내에 따라 Story Data 탭에서 층 목록(1F~11F 등)을 먼저
  확인(Height/Level 값 표시, Ground Level 지정 가능).
- "불러오기" 버튼으로 DXF 파일(예: `01 1F to 17F.dxf`, `02 18F to 25F.dxf`, `03 최상층.dxf`)을
  순차적으로 여러 개 불러옴 — 각 DXF가 해당하는 층 범위를 체크박스로 매핑.

### Step 2 — 기준층 지정 및 DXF Layer별 요소 정의

- 불러온 DXF 파일마다 "기준층" 배지를 지정(예: 01 1F to 17F.dxf를 기준층으로).
- "레이어 선택" 모달에서 DXF의 Layer별로 Wall / Beam & Column 요소 타입을 지정.

### Step 3 — Wall 요소 정의(Wall Mark 자동 할당 → 수정·병합)

- Wall 탭에서 "자동할당" 클릭 → 선택 안 한 전체 벽체에 W1, W2, W3...처럼 Wall Mark가 자동
  부여됨(우측 "WALL MARK 현황" 표에 Mark/Wall ID/Material/Thickness 컬럼으로 나열).
- 평면에서 벽체를 직접 클릭/드래그로 선택 → "WALL MARK 할당" 입력란에 원하는 이름(예: CW1,
  CW2, CW4)을 입력하고 "할당" → 선택한 여러 벽체를 하나의 Mark로 병합.
- Properties 할당: Material·Thickness 드롭다운으로 선택한 Mark의 재료·두께를 배정.

### Step 4 — Wall ID 자동생성

- "Wall ID 자동생성" 버튼 클릭 → "Wall Mark 할당 순 전체에 1001번부터 순서대로 부여됩니다"
  안내 후 Wall ID가 자동 채번됨(예: CW1→1001, CW2→1002, CW3→1003, CW4→1004, W2→1005...).

### Step 5 — 기준층 데이터 복사

- 다른 DXF 층(예: 02 18F to 25F.dxf)에서 "기준층 Data 복사하여 가져오기"를 실행 → 기준층에서
  정의한 Wall Mark/ID/Material/Thickness가 해당 층에 그대로 복사됨(WALL MARK 현황 항목 수가
  250개 → 152개로, 즉 해당 층의 실제 벽체 구성에 맞게 재적용).
- 층별로 Material/Thickness를 다르게 재지정도 가능(예: 상부층은 C27로 변경).

### Step 6 — Beam/Col 요소 추가

- "Beam/Col" 탭으로 전환 → DXF 층별(01 1F to 17F / Beam, 02 18F to 25F / Beam, 03 최상층 /
  Beam)로 Line 요소에 매핑할 Material·Section을 지정.

### Step 7 — Model Build

- 우측 하단 "Model Build" 버튼 → "Model Build 확인" 모달에서 단위계(m, Plan Editor 모델 단위)
  확인 및 Wall Segment Length(벽체 분할 길이, 예 1~1.5m) 입력.
- 생성 예정 요약 자동 표시: "Wall Element(3837개, Beam/Column Element 312개 완료), Wall
  Mark(Mark별 Wall ID 그룹), Story 정보 등록(27개)" 등 — 4199개 Element(Wall 3887 + B/C 312),
  Wall 260개, Story 26개.
- "Build 실행" 클릭 → GEN NX 모델에 실제 반영.

### Step 8 — GEN NX 모델 결과 확인

- GEN NX 트리 메뉴에서 Stories(27), Nodes(4995), Elements(4199, Beam 312/Wall 3887)가 생성된
  것 확인, Material 2종(C30, C27), Section 2종(Col, Beam), Thickness 4종(T150/T200/T250/T300).
- 평면도에서 자동 부여된 Wall ID(1001, 1002...)와 Wall Mark(CW1, CW2, W101...)가 도면 위에
  라벨로 표시됨을 확인.
- GEN NX 기본 메뉴 `Structure > Building > Auto Wall ID Generation`(GEN NX 자체 마법사 도구)
  화면에서도 "Modify Wall Mark Data"로 Plug-in이 만든 Wall Mark/ID 데이터가 그대로 반영되어
  있음을 재확인 — 즉 Plug-in의 출력이 GEN NX 네이티브 Wall Mark 체계와 완전히 호환됨.
- Structure 리본의 `Story > Story Data` 창에서도 Plug-in이 등록한 층 데이터(Floor Width,
  Floor Center, Eccentricity 등)가 GEN NX에 정상 반영됨을 최종 확인.

## 6. 연계 JSON API 엔드포인트

화면에 정확한 API 호출 로그는 노출되지 않았으나(브라우저 기반 UI에서 처리), 최종 GEN NX 결과
화면에서 데이터 구조가 명확히 확인되어 대응 가능하다:

| 기능 | 추정 API | 문서 위치 |
| --- | --- | --- |
| Story Data 등록 | `POST /db/STOR` | [`02_DB_Project_Structure.md#15-dbstor--story-data`](../../manual/02_DB_Project_Structure.md#15-dbstor--story-data) |
| 벽체/보 Node·Element 생성 | `POST /db/NODE`, `POST /db/ELEM` | [`03_DB_Node_Element.md#1-dbnode`](../../manual/03_DB_Node_Element.md#1-dbnode), [`#2-dbelem`](../../manual/03_DB_Node_Element.md#2-dbelem) |
| Material/Section/Thickness 생성 | `POST /db/MATL`, `POST /db/SECT`, `POST /db/THIK` | [`04_DB_Properties.md#1-dbmatl`](../../manual/04_DB_Properties.md#1-dbmatl), [`#12-dbsect`](../../manual/04_DB_Properties.md#12-dbsect) |
| Wall Mark(Mark ↔ Wall ID 매핑) | `POST /db/WMAK` | [`24_DB_Design.md#9-dbwmak--modify-wall-mark-design-벽체-마크-설계-수정`](../../manual/24_DB_Design.md#9-dbwmak--modify-wall-mark-design-벽체-마크-설계-수정) |

- GEN NX 네이티브 `Structure > Building > Auto Wall ID Generation`(트리 메뉴 "Modify Wall Mark
  Data") 화면에 Plug-in이 만든 Wall Mark/Wall ID 데이터가 그대로 나타나는 것을 확인했으므로,
  `/db/WMAK`(`{"WMAK": {"<ID>": {"MARKNAME": "...", "WID_LIST": [...]}}}`) 스키마 사용이
  #2(WallMarkAutoMapper)와 동일하게 강하게 뒷받침된다.
- ⚠️ 브라우저 기반 웹뷰(Floor Plan Editor)에서 실시간으로 이루어지는 DXF 파싱·Wall Mark 자동
  할당·기준층 복사 로직 자체는 GEN NX Open API 호출이 아니라 Plug-in 자체 로직(클라이언트
  사이드)으로 보이며, 최종 "Model Build" 단계에서만 GEN NX API가 일괄 호출되는 구조로 추정된다
  (정확한 호출 시점·배치 여부는 화면상 확인되지 않음).

## 7. 입력 데이터 규격

- **DXF 파일**: 구조평면도, 층별로 여러 파일 업로드 가능. 선(벽체·보), 점(기둥) 요소 레이어
  구분 필요.
- **Story Data**: 층별 높이(Height)·레벨(Level), Ground Level 지정.
- **Wall Segment Length**: 벽체 분할 길이(m) — Model Build 시 지정.

## 8. 출력 / 생성 결과

- GEN NX 모델의 Story Data, Node/Element(Wall/Beam/Column), Material/Section/Thickness,
  Wall Mark(`/db/WMAK`) 데이터 전체.

## 9. 제약사항 및 한계

- "추후 개선사항"으로 개발자가 직접 명시: "Beam 요소 적용 시 최하층 형성 → 삭제되도록 개선"
  — 현재는 최하층(지하/기초 레벨)에 불필요한 Beam 요소가 함께 생성되는 한계가 있으며, 향후
  자동 삭제되도록 개선할 계획임을 밝힘.
- Wall Segment Length(분할 길이) 값에 따라 생성되는 Element 수가 크게 달라지므로(안내
  문구: "예) 길이 7.0m 벽체 2.0m 입력 시 4분할(약 1.75m), 균열 노드는 최대한 겹치지 않는 지점
  자동 배치됩니다"), 값 선택에 따른 결과 검토가 필요.
- Wall Mark 자동 할당은 벽체 배치 순서(선택 순서)를 기준으로 채번되므로, 프로젝트 표준
  명명 규칙과 다를 경우 수동 재할당이 필요할 수 있다.

## 10. 화면 인벤토리

| 시점(초) | 화면 내용 |
| --- | --- |
| 0–10 | 인트로(Plug-in Info: 닉네임 이현파파, Easy Apartment Builder, 기능 요약) |
| 10–20 | 고려사항/편의기능 슬라이드(CAD dxf 요소 특성별 부재 Type, 단축키, 추후 개선사항, 기대효과) |
| 20–40 | Apps에서 EAB 실행, Floor Plan Editor 웹뷰 최초 진입, Story Data 확인 |
| 40–60 | DXF 파일 여러 개 불러오기(1F~17F/18F~25F/최상층), 층 매핑 |
| 60–100 | DXF Layer별 요소 정의(레이어 선택 모달), Wall Mark 자동할당 |
| 100–190 | Wall Mark 변경·병합, Material/Thickness 배정, Wall ID 자동생성, 기준층 Data 복사 |
| 190–230 | Beam/Col 탭에서 Material/Section 배정 |
| 230–250 | Model Build 확인 모달(Wall Segment Length, 생성 예정 요약) → Build 실행 |
| 250–313 | GEN NX 결과 확인(3D 형상, Wall ID/Mark 라벨, 네이티브 Wall Mark 데이터·Story Data 창 대조) |

---

*다음: 16_CRANE_LOADER 영상 분석 및 기획문서 작성.*
