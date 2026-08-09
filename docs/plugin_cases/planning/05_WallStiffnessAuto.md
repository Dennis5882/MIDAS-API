# WallStiffnessAuto 기획문서

> 영상(`docs/plugin_cases/videos/05_WallStiffnessAuto.mp4`, 30fps, 1920×1080, 약 134초)을 6초
> 간격으로 프레임 캡처(총 23장) 후 프레임별 육안 분석 + 영상 내 자막(내레이션 캡션)을 근거로
> 작성. 원문 아티클(`docs/plugin_cases/articles/05_WallStiffnessAuto.md`)의 4대 기능 설명과 교차
> 확인함. 이 영상은 발표 슬라이드와 실제 GEN NX 화면 녹화가 결합된 데모 형식이며, 특히 마지막
> "요약·확장" 슬라이드에 실제 사용한 API 목록이 그대로 텍스트로 노출되어 있어 다른 Plug-in보다
> API 매핑 근거가 강함.

## 1. 개요

**WallStiffnessAuto**는 GEN NX API로 RC 벽체 설계(KDS-41-20-2022) 결과를 직접 조회해, 설계
기준을 초과(NG)한 벽체의 강성 증감계수(WSSF, Wall Stiffness Scale Factor)를 NG가 모두 해소될
때까지 스스로 낮춰가며 반복 수렴시키는 Plug-in이다. "구조해석 → 벽체 설계·검토 → NG 추출 →
강성계수 저감"의 4단계 사이클을 NG가 0이 될 때까지 프로그램이 자동으로 반복한다.

## 2. 문제 정의

- 초기 모델링 단계에서 강성이 큰 벽체는 설계 응력비가 기준을 초과(NG)하는 경우가 흔한데, 이때
  실무자는 해당 벽체의 강성을 임의로 낮추고 → 재해석 → 재설계 검토를 반복하며 NG가 없어질 때까지
  수동으로 값을 조정한다.
- 이 반복 조정 작업은 벽체 수가 많을수록(영상 예시 다층 건물, NG 5건 → 대상 요소 24개 시작)
  시간이 오래 걸리고 사람이 개입해야 하는 전형적인 반복 작업이다.

## 3. 목표 사용자

- KDS-41-20-2022 기준 RC 벽체 설계를 수행하며, 강성 저감(균열 단면 반영 등)을 통해 NG를 해소해야
  하는 구조 설계자.
- 특히 벽식 구조 등 벽체가 많아 반복 조정 시간이 큰 프로젝트의 실무자.

## 4. 핵심 컨셉 / 차별점

- **해석→설계→추출→저감 4단계 자동 사이클**: 구조해석(POST doc/ANAL) → 벽체 설계·검토(WD/
  WC-ANAL) → NG 추출(WD/WC-TABLE) → 강성계수 저감(PUT db/WSSF)을 하나의 루프로 묶어, NG가 0이
  될 때까지 프로그램이 자동으로 반복. 사람은 설정 후 시작 버튼만 누르면 된다.
- **저감 조건 파라미터화**: 회당 감소량(Step), 최소 계수 하한, 최대 반복 횟수 3개 파라미터로
  자동 반복의 범위를 제어 — 무한정 낮아지지 않도록 하한을 두고, 반복이 끝나지 않을 경우를 대비해
  최대 횟수를 둠.
- **이력 자동 기록**: 반복마다 NG·응력비·적용 계수를 화면 표와 CSV 파일로 자동 저장해, 사후
  추적·검증이 가능하게 한다.
- **즉시 복원**: 저감된 계수를 버튼 하나로 저감 이전 값(1.0)으로 되돌릴 수 있어, 시행착오
  비용이 낮다.
- **범용 확장 설계**: 발표자 스스로 "벽체(WSSF)·빔(ESSF) 강성 API가 서로 달라 부재 종류별 분기가
  필요"하다고 인지하고, 벽체·빔 각각 다른 강성 API·NG 판정 단위를 공통 자동 반복 구조 위에서
  동작하도록 설계 — 실제로 빔 강성 자동 조절(ESSF) 기능이 2026-08-03 업데이트로 추가 예정임을
  요약 슬라이드에서 명시.

## 5. 워크플로우

### Step 1 — API 연결

- Plug-in 창에서 `BASE_URL`, `MAPI-KEY` 입력(자막: "① BASE_URL과 MAPI-Key를 입력합니다").
- 설계기준 표시란에 `KDS-41-20-2022 (RC Wall)`이 자동으로 표시되는 것으로 보아 벽체 검토
  기준이 코드에 고정되어 있음.

### Step 2 — 저감 조건 설정

- ② 회당 감소량(Step), 최소 계수 하한, 최대 반복 횟수 3개 필드 설정.
- 영상 예시 값: 회당 감소량 0.1, 최소 계수 하한 0.3, 최대 반복 횟수 10.

### Step 3 — 자동 반복 시작

- ③ "자동 반복 시작" 버튼 클릭 → 아래 4단계를 설정한 횟수만큼 자동 반복:
  1. **구조해석 실행** (`POST doc/ANAL`) — GEN NX 내에서 "Analysis is now completed" 진행
     상태 창(Forming Element Stiffness and Load Matrices → Static Analysis → Eigenvalue
     Analysis → Response Spectrum Analysis)이 표시됨.
  2. **벽체 설계·검토** (`WD/WC-ANAL`) — "Start Design by KDS 41 20 : 2022" 진행 상태 창
     (Design Relief of Concrete Wall → Check Complete Wall → Converting Design Results →
     Creating design result file 순으로 진행).
  3. **NG 추출** (`WD/WC-TABLE`) — 반복별 NG 대상 벽체 리스트를 표(층, Wall ID, ID, 지배응력비,
     최대응력비, 반복횟수, 적용계수)로 표시. 예: "1반복 NG 이력 (예 벽체 대상만 결과)" 표에
     `1F/13`, `2F/22`, `1F/24`, `2F/46`, `1F/72` 등이 표시됨.
  4. **강성계수 저감** (`PUT db/WSSF`) — 부재별 현재 강성계수 현황 표시줄로 저감 진행률을 시각화.
- 반복 로그 예시: "Create Load Combination : 164", "End Creating Load Combinations for Design/
  Checking.", "Start Design by KDS 41 20 : 2022", "End Design by KDS 41 20 : 2022" — 이 4개
  로그 순환이 반복마다 재발생.

### Step 4 — 결과 확인

- ④ 반복이 끝나면 "설계완료" 알림 팝업으로 결과를 확인. NG가 계속 남아있으면 "최대 반복 도달"
  알림으로 별도 안내(즉 두 가지 종료 조건: NG=0 도달, 또는 최대 반복 횟수 도달).
- 트리 메뉴에 `Wall Stiffness Scale Factor` 그룹이 생성되어 `Type 1 | Group=Default; Shear=0.7;
  Bending=0.7`처럼 그룹별 최종 저감 계수가 남아 검토 가능.

### Step 5 — NG 이력 CSV 출력

- 반복별 NG 부재·응력비·적용 계수를 기록한 CSV 파일을 산출 결과물로 제공.

## 6. 연계 JSON API 엔드포인트

**"요약·그리고 확장" 슬라이드에 실제 사용한 GEN NX API 목록이 그대로 텍스트로 노출**되어 있어,
이 Plug-in은 추정이 아니라 화면에 직접 확인된 근거로 매핑 가능한 드문 사례다.

| 화면 표시 | 용도(화면 표시) | 문서 위치 |
| --- | --- | --- |
| `POST doc/ANAL` | 구조해석 실행 | [`01_DOC.md#11-docanal--perform-analysis`](../../manual/01_DOC.md#11-docanal--perform-analysis) |
| `POST WD/WC-ANAL` | 벽체 설계·배근 검토 | [`26_Design_RC_KDS41202022.md#63-designrckds-41-20-2022wc-anal--rc-벽체-검토-수행`](../../manual/26_Design_RC_KDS41202022.md#63-designrckds-41-20-2022wc-anal--rc-벽체-검토-수행) |
| `POST WD/WC-TABLE` | NG 부재·응력비 조회 | [`26_Design_RC_KDS41202022.md#64-designrckds-41-20-2022wc-table--rc-벽체-검토-테이블`](../../manual/26_Design_RC_KDS41202022.md#64-designrckds-41-20-2022wc-table--rc-벽체-검토-테이블) |
| `GET db/ELEM · NODE · STOR` | 요소·층 매핑 | [`03_DB_Node_Element.md#1-dbnode`](../../manual/03_DB_Node_Element.md#1-dbnode), [`#2-dbelem`](../../manual/03_DB_Node_Element.md#2-dbelem), [`02_DB_Project_Structure.md#14-dbstor--story-data`](../../manual/02_DB_Project_Structure.md#14-dbstor--story-data) |
| `GET / PUT db/WSSF` | 강성 증감계수 조회·적용 | ⚠️ 이 저장소의 `docs/manual`에는 `/db/WSSF` 전용 엔드포인트 문서가 없다(아래 참고) |
| `GET view/SELECT` | 선택 부재 읽기 | [`16_VIEW.md#1-viewselect--select`](../../manual/16_VIEW.md#1-viewselect--select) |

- ⚠️ **`/db/WSSF` 관련 중요 발견**: `docs/manual`에는 유사한 이름의 `/db/ESSF`(Element Stiffness
  Scale Factor, [`04_DB_Properties.md#31-dbessf`](../../manual/04_DB_Properties.md#31-dbessf))만
  문서화되어 있고, 이는 요소(Element) 단위로 `AREA_SF`/`ASY_SF`/`IYY_SF`/`IZZ_SF` 등을 직접
  지정하는 방식이다. 반면 영상 속 GEN NX 트리 메뉴에는 `Wall Stiffness Scale Factor` 항목이
  별도로 존재하며 `Type N | Group=...; Shear=x; Bending=y` 형태로 **그룹 단위 전단/휨 강성
  계수**를 관리한다 — `/db/ESSF`의 요소별 축력/비틀림/휨/전단/자중 6종 계수 구조와는 다르다.
  `12_DB_Analysis_Control.md:2384`의 Analysis Control 옵션 표에 `"bWSSF"`(Wall Stiffness Scale
  Factor 사용 여부 Boolean)와 `12_DB_Analysis_Control.md:2600`의 약어표에 `"WSSF"` = Wall
  Stiffness Scale Factor 라는 용어 자체는 존재하지만, 이 값을 그룹 단위로 GET/PUT하는 전용
  엔드포인트(`/db/WSSF`)는 이 저장소에 아직 문서화되지 않은 상태다. 즉 화면에 노출된 이 API
  이름은 실제 존재하는 것으로 보이나(개발자가 정확히 "GET / PUT db/WSSF"로 명시), 이 저장소의
  매뉴얼 커버리지 공백(gap)으로 별도 확인이 필요하다.

## 7. 입력 데이터 규격

- **선행 조건**: RC 벽체가 KDS-41-20-2022 기준으로 이미 정의되어 있고, 응답스펙트럼 해석
  하중케이스가 설정되어 있어야 함(진행 상태 창에 Eigenvalue Analysis, Response Spectrum
  Analysis가 포함됨).
- **저감 조건 파라미터**: 회당 감소량(Step, 예 0.1), 최소 계수 하한(예 0.3), 최대 반복 횟수
  (예 10).

## 8. 출력 / 생성 결과

- GEN NX 모델의 `Wall Stiffness Scale Factor` 그룹별 최종 강성계수(Shear/Bending).
- 반복별 NG·응력비·적용계수 이력 CSV 파일.
- "설계완료" 또는 "최대 반복 도달" 알림.

## 9. 제약사항 및 한계

- 요약 슬라이드에 개발자가 직접 밝힌 기술적 도전 3가지:
  1. 벽체(WSSF)·빔(ESSF) 강성 API가 서로 달라 부재 종류별 분기 처리가 필요함.
  2. NG 결과가 "Wall ID + 층" 단위로 나오기 때문에, 절점 좌표로 층을 추정해 실제 요소로 매핑하는
     과정이 필요함(즉 NG 결과 자체가 즉시 element ID로 떨어지지 않음).
  3. 강성 저감이 잘 먹히지 않는(수렴하지 않는) 부재(축력·휨 지배)를 자동 판별해 무한반복을
     방지해야 함.
- 현재(영상 시점) 벽체(WSSF) 강성 자동 조절만 구현 완료 상태이며, 빔(ESSF) 강성 자동 조절은
  "26.08.03 업데이트 예정"으로 아직 별도 개발 중이었음(⚠️ 영상 제작 시점 기준 — 실제 배포
  여부는 이 문서 작성 시점에 재확인 필요).
- 최대 반복 횟수에 도달해도 NG가 남아있을 수 있으며, 이 경우 프로그램이 자동으로 해결하지 못하고
  "최대 반복 도달" 알림만 표시 — 최종 판단은 엔지니어 몫.

## 10. 화면 인벤토리

| 시점(초) | 화면 내용 |
| --- | --- |
| 0–6 | 인트로 — 출품작/닉네임/기능 한 줄 요약 |
| 6–12 | THE SOLUTION — 4단계 사이클(구조해석→벽체 설계·검토→NG 추출→강성계수 저감) 다이어그램, 클릭 한 번/이력 자동 기록/즉시 복원 |
| 12–18 | 자동 반복 실행 UI 설명(NG 부재·응력비 확인, 저감 조건 설정, NG 해소·계수 이력 CSV) |
| 18–132 | 실전 데모(전체 시연 영상, 서버 연결부터 결과 확인까지): API 연결 → 저감 조건 설정 → 자동 반복 시작 → 해석/설계/NG추출/강성저감 N회 반복(로그·진행상태창 다수) → "설계완료" 알림 |
| 132–134 | SUMMARY — 활용한 GEN NX API 6종, 기술적 도전 3가지, 향후 업데이트(빔 ESSF), 범용성 설명 |

---

*다음: 06_WallHelper 영상 분석 및 기획문서 작성.*
