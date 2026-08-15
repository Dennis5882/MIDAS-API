# CS454 Moving Load Generator

> **원문:** [CS454 Moving Load Generator](https://support.midasuser.com/hc/ko/articles/60998764028185-CS454-Moving-Load-Generator)
> **원문 작성:** 2026-08-10 · **원문 최종 편집:** 2026-08-10

---

## 개요

CS 454 이동하중 평가는 공학적 작업이기 전에 긴 타이핑 작업이다. Appendix B, Table B.1은
5개 평가 이동하중 레벨(assessment live loading level)에 걸쳐 22종의 차량 모델을 정의하고,
각 차량마다 축중·축간거리가 따로 지정된다. Clause 5.12.1은 평가 대상 레벨뿐 아니라 그 아래
모든 레벨을 함께 반영하도록 요구하고, 컨보이(convoy)는 개수를 다시 두 배로 늘리며, ALL
model 2·소방차(fire engine) 그룹·특수차량(special vehicle)이 더해진다.

이 차량들은 각각 Vehicular Load 대화상자에서 계수까지 설정해 생성한 뒤, 별도의 Moving Load
Case로 이름·차선 배정·한계상태까지 지정해야 한다 — 그리고 레벨·차선·계수가 바뀔 때마다 전체
세트를 다시 만들어야 한다.

**CS 454 Moving Load Generator** Plug-in은 이 과정을 하나의 정의로 압축한다. MIDAS에서
교통 차선(traffic lane)을 정의해 두면, 이 Plug-in에서 차량 모델과 레벨을 선택하는 것만으로
연결된 모델에 차량과 이동하중 케이스를 한 번의 확정 단계로 생성한다.

## 지원 버전

`MIDAS CIVIL NX 2026 (v1.0.1)`

## 주요 기능

- **Appendix B 그대로:** Table B.1의 22종 차량 모델 전체가 내장되어, 공식 축중·축간거리·총
  중량 그대로 MIDAS의 ALL MODEL 1 서브타입으로 생성됨. Table B.2의 소방차 그룹은 MIDAS에
  대응 서브타입이 없어 사용자 정의 차량(user-defined vehicle)으로 처리.
- **Clause 5.12.1에 따른 레벨 누적:** 평가 레벨 하나를 체크하면 그 아래 모든 레벨이 함께
  포함됨 — 해당 조항이 평가 대상 레벨까지의 모든 차량 모델을 요구하기 때문이며, 조항의 주석은
  일부 26T 차량이 더 무거운 차량보다 더 불리할 수 있다고 기록한다. 이후 차량 목록을 실제로
  지배적인 축 배열로만 좁힐 수 있음.
- **두 라이브로드 모델을 한 번에:** ALL model 1은 Appendix B의 개별 차량으로, ALL model 2는
  Clause 5.17~5.19의 등분포하중(UDL)+집중하중(KEL) 조합으로 생성되며 그 값은 MIDAS가 재하
  길이(loaded length)로부터 산정. 단일 차량·컨보이·둘 다 선택 가능하며 Clause 5.14의 최소
  종방향 간격 1.0m가 적용됨.
- **차선은 한 번만 배정:** 교통 차선, 나란한(straddling) 차선 쌍, Clause 5.16의 잔여 구역
  차선을 한 번만 설정하면 생성되는 모든 케이스에 그대로 적용됨. 특수차량도 동일한 교통
  차선을 사용하며 Appendix C의 전후 25m 이격 거리가 적용됨.
- **모든 계수를 한 곳에서:** Factors 탭이 Vehicular Load·Moving Load Case 대화상자가 요구하는
  모든 값을 포함 — Table 5.19c K-계수 산정을 위한 노면 구분·교통류 구분, 동적증폭계수, 임계·
  기타 축 충격계수, 과적(overload), 유닛 수, 차량 속도, 한계상태, 하중조합. MIDAS의 두
  대화상자를 열 필요가 없음.
- **극한·사용한계상태 동시 처리:** 둘 다 체크하면 모든 차량에 대해 `-ULS`·`-SLS` 접미사가 붙은
  케이스가 한계상태별로 각각 생성됨. 이름·설명은 MIDAS 필드 길이 제한 안에서 자동 조정되며,
  줄인 내용은 Preview에서 보고됨.
- **검증된 항목을 복제해서 기록:** 새 항목은 모델에 이미 존재하는 항목을 복제해 생성하므로
  MIDAS가 쓰는 필드 중첩 구조와 enum 표기가 그대로 보존되고, 이름·서브타입·차량·차선 필드만
  다시 쓰임. 복제할 항목이 모델에 없으면 내장된 CS 454 템플릿이 검증된 MIDAS 항목을 필드
  단위로 재현.
- **기록 전 검증:** Preview는 생성될 모든 차량과 이동하중 케이스를 축 데이터·차선·상태와
  근거가 되는 CS 454 조항 노트까지 함께 나열하며, **Generate**가 확정되기 전까지는 모델에
  아무것도 반영되지 않음.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | CIVIL NX에서 대상 모델을 열고 Plug-in 실행. 연결 정보는 자동으로 채워지며, **Validation Check**가 PyScript·base URI·MAPI key를 다른 작업 전에 먼저 보고 |
| 2 | **Model** 탭에서 **Read model** 클릭. 모델에 이미 있는 교통 차선·차량·이동하중 케이스가 보고되고, payload 템플릿으로 쓸 차량·하중 케이스도 여기서 선택. 교통 차선은 MIDAS에서 먼저 정의해야 함 — 이 Plug-in은 차선을 배정할 뿐 생성하지 않음 |
| 3 | **Loading**에서 정상교통(normal)/특수교통(abnormal) 선택, **ALL model 1**·**ALL model 2** 필요에 따라 체크, 평가하중 레벨 체크. 특정 레벨만 평가하려는 게 아니라면 레벨 누적(level stacking)은 켜 둔 채로 둠. 원치 않는 차량 모델은 체크 해제, 단일 차량/컨보이/둘 다 중 선택 |
| 4 | **Lanes**에서 각 생성 케이스가 차량을 적용할 교통 차선을 체크, Clause 5.16이 요구하는 잔여 구역 차선 설정, 나란한 차선 쌍 추가. 특수교통의 경우 특수차량 종류와 생성될 이름을 설정 |
| 5 | 마찬가지로 **Lanes**에서 차량·하중 케이스 이름 패턴을 서브타입·Table B.1 참조 문자·레벨·특수차량·일련번호 토큰으로 구성. 모델에 이미 존재하는 이름 처리 방식(번호 붙여 나란히 추가/덮어쓰기/건너뛰기) 선택 |
| 6 | **Factors**에서 노면·교통류 구분, 동적증폭계수·축 충격계수, 과적, 유닛 수, 차량 속도, 설계 조합(한계상태, Combination 1/2/3) 설정 |
| 7 | **Preview** 검토 — 생성될 모든 차량을 참조명·레벨·총중량·축중·축간거리와 함께, 모든 이동하중 케이스를 차량·특수차량·차선·상태와 함께 나열. CS 454 근거 조항이 함께 표시되며, 오류가 있으면 해결 전까지 생성이 차단됨 |
| 8 | **Generate** 탭 — **Preview payload**는 실제로 전송될 JSON을 기록 없이 생성, **Write to model**은 이를 커밋. 로그에 기록/건너뜀/이름변경 결과와 이후 모델 상태가 보고되며, 누락된 항목이 있으면 **Diagnostics** 탭에서 각 MAPI 엔드포인트의 응답을 확인 가능 |

## 참고/제약사항

- 교통 차선은 MIDAS에서 먼저 정의해야 한다 — 이 Plug-in은 차선을 배정할 뿐 생성하지 않는다.
- 새 항목은 모델에 이미 존재하는 항목을 복제하는 방식으로 생성되며, 복제할 항목이 없으면
  내장 CS 454 템플릿을 사용한다.
- 이름·설명이 MIDAS 필드 길이 제한을 넘으면 자동으로 줄여서 기록하고, 줄인 내용은 Preview에
  보고된다.

## 관련 JSON API 엔드포인트

Plug-in이 생성한다고 명시한 차량·이동하중 케이스는 `docs/manual`의 다음 엔드포인트와
대응된다.

- [`/db/MVHL` — Vehicles](../../manual/08_DB_Moving_Loads.md)
- [`/db/MVLD` — Moving Load Cases](../../manual/08_DB_Moving_Loads.md)

## 결론 (원문)

CS 454 Moving Load Generator는 DMRB 이동하중 평가에서 가장 느리고 기계적인 부분을
제거한다 — Appendix B의 축 데이터를 Vehicular Load 대화상자에 옮겨 적는 일, Clause 5.12.1이
평가 대상 레벨과 함께 요구하는 하위 레벨을 일일이 챙기는 일, 모든 차량·모든 컨보이·모든
한계상태마다 Moving Load Case를 수작업으로 만드는 일. 차선을 한 번만 정의하고 Preview로
확인한 뒤, 레벨·차선·계수·범위가 바뀔 때마다 몇 초 만에 전체 세트를 다시 만들 수 있어,
엔지니어의 시간을 데이터 입력이 아닌 평가 자체에 쓸 수 있게 한다.

## 원문 링크

[https://support.midasuser.com/hc/ko/articles/60998764028185-CS454-Moving-Load-Generator](https://support.midasuser.com/hc/ko/articles/60998764028185-CS454-Moving-Load-Generator)
