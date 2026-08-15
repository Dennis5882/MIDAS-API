# CS454 Load Assessment Combinations

> **원문:** [CS454 Load Assessment Combinations](https://support.midasuser.com/hc/ko/articles/60997850893209-CS454-Load-Assessment-Combinations)
> **원문 작성:** 2026-08-10 · **원문 최종 편집:** 2026-08-10

---

## 개요

CS 454 Assessment Combination은 정의는 간단하지만 실제로 구성하는 데는 오래 걸린다. Table
A.1은 극한한계상태(ULS)·사용한계상태(SLS) 4개 조합마다 모든 액션(action)에 개별 부분계수를
지정하고, 그 액션이 불리(adverse)한지 유리(relieving)한지에 따라 다시 다른 값을 요구한다.

라이브로드 모델은 정상교통(normal-traffic) 케이스가 이를 대체하는 특수차량(abnormal
vehicle) 케이스와 같은 조합에 나타나지 않도록 서로 배타적으로 유지해야 하고, 모든
영구하중(permanent action)은 유리·불리 양방향으로 모두 돌려야 하며, 하중 케이스가 추가되거나
계수가 바뀔 때마다 전체 세트를 다시 만들어야 한다 — 이 모든 것을 Load Combinations 표에
수작업으로 입력하기 전에 처리해야 하는 작업이다.

**CS 454 Load Assessment Combinations** Plug-in은 이 과정을 하나의 정의로 압축한다. 연결된
모델에서 하중 케이스를 읽어 각각을 Table A.1의 액션에 매핑하고, 사용자가 확인한 계수를
적용해, 전체 조합 세트와 그 envelope를 한 번의 확정 단계로 CIVIL NX에 기록한다.

## 지원 버전

`MIDAS CIVIL NX 2026 (v1.0.1)`

## 주요 기능

- **Table A.1 그대로:** 모든 조합이 CS 454 version 1.1.0, Appendix A, Table A.1을 그대로
  따름 — 액션별 불리/유리 γ<sub>fL</sub>, 주철(cast iron) 구조 전용 계수 세트, γ<sub>f3</sub>를
  조합계수에 포함할지 저항 검토로 남길지까지 반영.
- **모델에서 매핑, 재입력 없음:** 정적·시공단계·침하·이동하중 케이스를 연결된 모델에서 읽어
  각각 CS 454 액션에, 이동하중은 하중 모델(ALL Model 1·2, SV, SOV, STGO, SO, HB, 관련
  정상교통·보도 하중)에 배정. 매핑되지 않은 케이스는 조용히 기본값 처리되지 않고 조합 생성
  자체를 막으며, Prestress는 CS 455 영역이라 아예 매핑이 거부됨.
- **라이브로드 배타성 정확히 처리:** 카테고리별로 함께/독립/배타 작동을 지정할 수 있어
  정상교통 케이스가 이를 대체하는 특수차량과 같은 조합에 들어가지 않으며, 카테고리 규칙만으로
  표현되지 않는 경우를 위한 교차 카테고리 제외(exclude)/요구(require) 설정도 가능.
- **영구하중 양방향 자동 생성:** both로 설정된 영구하중 그룹은 유리·불리 양쪽 모두 생성되어,
  순열 전체가 수작업 없이 만들어짐.
- **코드가 허용하는 한 조합 수 축소:** 상호 배타 그룹을 하나의 Envelope 서브조합으로 묶어
  Table A.1 계수로 참조하게 함으로써, 모델에 실제로 등록되는 행 수를 줄임.
- **영문으로 읽히는 이름:** 압축 코드 대신 `ULS2-ALL1s-W2-Adv` 형태로 기록되어, 한계상태·조합
  번호·라이브로드 모델·풍하중 서브케이스·영구하중 변형이 MIDAS 표에서 그대로 읽히고,
  description에도 동일 내용이 문장으로 풀어서 기재됨.
- **기록 전 검증:** Preview는 모든 조합을 구성요소·수식·각 항을 만든 조항과 계수까지 전체
  원장(ledger) 형태로 나열하며, commit이 확정되기 전까지는 모델에 아무것도 반영되지 않음.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | CIVIL NX에서 대상 모델을 열고 Plug-in 실행. 연결 정보는 자동으로 채워지며, 상태 배지가 **CIVIL NX connected**가 아니면 **Connection**을 사용 |
| 2 | **Read Model Validation** — 구조 형식과 모델의 하중 케이스를 생성 전 보고. 주철(cast iron) 구조는 Section 8에 따라 허용응력 기준으로 평가되므로 전용 계수 열로 전환되고 SLS 범위가 비활성화됨. 조적 아치(masonry arch)는 이번 버전 범위 밖 |
| 3 | **Load Cases & Mapping**에서 활성화된 모든 케이스에 CS 454 Table A.1 액션을, 모든 이동하중 케이스에는 CS 454 하중모델과 평가 레벨을 지정. MIDAS에서 **Auto Live Load Combination**이 설정된 경우 ULS 전용/SLS 전용 제한이 모델에서 자동 인식·보고되어, SLS 차량이 ULS 조합에 잘못 반영되지 않음 |
| 4 | **Combinations Scope**에서 필요한 조합 1~4번과 한계상태를 체크 — 체크된 항목만 생성됨 |
| 5 | 계수 확정 — Table A.1 전체가 표시되며 액션별 불리/유리 γ<sub>fL</sub>을 평가에 맞게 수정 가능, γ<sub>f3</sub>를 조합계수에 포함할지 저항 검토로 남길지 설정 |
| 6 | **Groups & Relations**에서 카테고리별 그룹을 구성하거나 템플릿 적용, 카테고리 동작(함께/독립/배타), 완전 부재 허용 여부, 배타 그룹의 Envelope 서브조합 병합 여부 설정. 교차 카테고리 제외/요구 추가, 영구하중 그룹을 불리/유리/양쪽으로 설정 |
| 7 | **Preview** 검토 — 생성된 모든 조합을 이름·계열·라이브로드 모델·구성요소 수·경고와 함께 나열, 개별 조합 선택 시 수식과 각 항을 만든 Table A.1 행·계수 전체 원장 확인 |
| 8 | **Commit** — 대상 테이블 선택, 기존 Load Combinations 처리 방식 결정, 이름 충돌 시 접두어 추가, 계열별 Envelope 기록 여부 체크. 전송 전 요약으로 실제로 기록될 내용을 확인 |

## 참고/제약사항

- 주철(Cast iron) 구조는 Section 8에 따라 허용응력 기준 평가로 전환되며 SLS 범위가
  비활성화됨.
- 조적 아치(Masonry arch)는 이번 버전에서 지원하지 않음.
- Prestress 하중 케이스는 CS 455 영역으로 간주되어 매핑 자체가 거부됨.
- 매핑되지 않은 하중 케이스가 있으면 기본값으로 조용히 처리되지 않고 조합 생성이 차단됨.

## 관련 JSON API 엔드포인트

Plug-in이 최종적으로 CIVIL NX에 기록하는 하중조합은 `docs/manual`의 다음 엔드포인트와
대응된다.

- [`/db/LCOM-GEN` — Load Combinations – General](../../manual/13_DB_Load_Combinations.md)

## 결론 (원문)

CS 454 Load Assessment Combinations Plug-in은 DMRB 평가에서 가장 느리고 실수하기 쉬운
부분을 제거한다 — 4개 조합·2개 한계상태에 걸쳐 Table A.1을 읽고, 라이브로드 모델의
배타성을 유지하고, 모든 영구하중을 양방향으로 돌리고, 결과를 수작업으로 입력하는 일.
매핑을 한 번 정의하고 Preview로 확인한 뒤, 하중 케이스·계수·범위가 바뀔 때마다 몇 초 만에
전체 세트를 다시 만들 수 있어, 엔지니어의 시간을 장부 정리가 아닌 평가 자체에 쓸 수 있게
한다.

## 원문 링크

[https://support.midasuser.com/hc/ko/articles/60997850893209-CS454-Load-Assessment-Combinations](https://support.midasuser.com/hc/ko/articles/60997850893209-CS454-Load-Assessment-Combinations)
