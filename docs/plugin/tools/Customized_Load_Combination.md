# Customized Load Combination

> **원문:** [Customized Load Combination](https://support.midasuser.com/hc/en-us/articles/41509743351193-Customized-Load-Combination)
> **원문 작성:** 2024-12-23 · **원문 최종 편집:** 2025-08-01

---

## 개요

midas Civil NX에서 구조 설계용 하중조합을 생성·관리하는 과정을 단순화하는 Plug-in이다.
특정 설계 시나리오에 필요한 하중케이스·계수·설정을 정의하는 옵션을 제공해, 표준 및 커스텀
설계 코드 모두와 호환된다.

## 지원 버전

`MIDAS CIVIL NX 2025 (v1.1) US`

## 주요 기능

제품에 자주 들어오던 문의:

- 특정 국가나 개정/구버전 코드용 하중조합이 빠져 있음.
- 지자체 요구사항, 까다로운 심의 절차, 설계자의 의도를 반영하기 위한 추가 특수 하중조합이
  필요함.

많은 수의 하중조합을 정의하는 것은 번거로운 작업이라, 이 Plug-in은 다음 기능을 제공한다.

- 최소한의 입력으로 하중조합 생성.
- Excel 파일에서 입력 데이터를 가져오는 옵션.
- 생성한 하중조합을 wizard 파일로 내보내 재사용 — 하중조합 생성 입력값 라이브러리를 직접
  구축할 수 있어 시간을 크게 절약.
- 생성된 조합의 envelope를 자동 생성.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | "Customized Load Combination Auto-Generator" Plug-in 실행 |
| 2 | 하중조합 목록에 입력 추가 — A: 하중조합 이름, B: Active 상태(아래 표), C: Type(아래 표) |
| 3 | 하중케이스·하중계수 추가 — A: Load Case 이름(Civil에서 생성된 항목이 드롭다운으로 임포트되며 Plug-in에서 정의한 조합도 포함, 예: Static, RS, MVL, TH, Settlement 등), B: Sign(아래 표), C: Factor(최대 5개, 사용자가 직접 입력, 임포트된 하중케이스는 최소 1개 factor 필요, 한 하중조합 내 동일 순번 factor는 동시 사용됨) |
| 4 | 추가 입력 — A: Generate Envelope Load Combinations(생성된 조합의 envelope 생성), B: Generate Inactive Load Combinations("Inactive"로 표시된 하중조합 생성), C: Generate Load Combinations In(하중조합을 생성할 탭 선택: Steel Design / Concrete Design / SRC Design / Composite Steel Girder Design) |
| 5 | **Generate Load Combination** 클릭 |
| 6 | 생성 완료 알림 확인 |
| 7 | Results > Load Combination > Steel Design 등 경로에서 결과 확인 |
| 8 | Export Load Combination Input(wizard 파일 내보내기, TMH·AREMA 등 특정 코드 템플릿 생성이나 오류 시 재생성에 유용) / Import Load Combination Input(생성된 wizard 파일 가져오기) |

### B: Active 상태 옵션

| 옵션 | 설명 |
| --- | --- |
| Inactive | 사용자가 선택한 경우 Civil에 생성될 수 있음 |
| Local | Plug-in 안에서만 표시됨 |
| Strength | Civil에 생성되며 극한한계상태(ULS)로 설계됨 |
| Service | Civil에 생성되며 사용한계상태(SLS)로 설계됨 |

### C: Type 옵션

| 옵션 | 설명 |
| --- | --- |
| Add | 조합 내 모든 케이스를 합산 |
| Either | 조합 내 케이스 중 하나만 고려 |
| Envelope | 조합 내 케이스의 envelope 생성 |

### B(하중계수 Sign) 옵션

| 옵션 | 설명 |
| --- | --- |
| `+` | 양(positive)의 계수 값만 |
| `-` | 음(negative)의 계수 값만 |
| `±` | 양/음 계수의 순열(permutation) |
| `+, -` | 양만 적용한 경우와 음만 적용한 경우 각각 |

## 관련 JSON API 엔드포인트

"Generate Load Combinations In"에서 선택하는 4가지 탭은 `docs/manual`의 다음 엔드포인트와
대응된다.

- [`/db/LCOM-STEEL` — Load Combinations (Steel Design)](../../manual/13_DB_Load_Combinations.md)
- [`/db/LCOM-CONC` — Load Combinations (Concrete Design)](../../manual/13_DB_Load_Combinations.md)
- [`/db/LCOM-SRC` — Load Combinations (SRC Design)](../../manual/13_DB_Load_Combinations.md)
- [`/db/LCOM-STLCOMP` — Load Combinations (Composite Steel Girder Design)](../../manual/13_DB_Load_Combinations.md)

## 결론 (원문)

Customized Load Combination Auto-Generator Plug-in은 하중조합 정의·관리 과정을 크게
단순화해 사용자의 시간과 노력을 절약한다. 하중조합 생성·내보내기를 자동화해 효율을 높이고
다양한 설계 기준 준수를 보장한다. 사용자는 향후 프로젝트를 위한 하중조합을 빠르게 생성·저장·
재사용할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/41509743351193-Customized-Load-Combination](https://support.midasuser.com/hc/en-us/articles/41509743351193-Customized-Load-Combination)
