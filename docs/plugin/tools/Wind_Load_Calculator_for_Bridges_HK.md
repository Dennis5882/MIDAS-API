# Wind Load Calculator for Bridges (HK)

> **원문:** [Wind Load Calculator for bridges (HK)](https://support.midasuser.com/hc/en-us/articles/40645303004697-Wind-Load-Calculator-for-bridges-HK)
> **원문 작성:** 2024-12-02 · **원문 최종 편집:** 2025-08-01

---

## 개요

홍콩 Highways Department가 발간한 **STRUCTURES DESIGN MANUAL for Highways and Railways
2013 Edition(SDM 2013)** 3.4절 Wind Actions을 기준으로, 교량 구조물에 작용하는 풍하중의
첨두속도압(Peak Velocity Pressure)을 계산하는 Plug-in이다. 교량에 작용하는 풍유발력 계산
방법 2가지를 지원하며 설계용 상세 결과를 제공한다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

- 균일 풍압과 풍속 프로파일을 기준으로 교량 구조물에 대한 풍작용 영향을 빠르고 정확하게
  분석.
- SDM 2013 지침 기준 정확한 풍유발력 제공.
- 풍압 계산에 **Simplified Procedure**와 **Full Procedure** 모두 지원.
- 풍압 데이터를 구조 해석에 손쉽게 연동.
- 교량 구조물에 대한 풍작용 영향을 명확하고 상세하게 시각화.
- SDM 2013 기준에 따라 다양한 교량 형상·지형 처리 가능.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | Plug-in을 실행하고 하중조합 목록에서 풍하중용 하중케이스 이름 선택 |
| 2 | **Velocity Pressure Case** 정의. 정의된 케이스가 없으면 우측 `(...)` 버튼으로 Velocity Pressure Case 추가 |
| Velocity Pressure Cases Dialog | ① Add(신규 케이스 추가) ② Close(닫기) ③ Modify(선택 케이스 수정) ④ Delete(선택 케이스 삭제) |
| 3 | Add 클릭 시 **Simplified Procedure**(Clause 3.4.2) 또는 **Full Procedure**(Clause 3.4.3) 중 선택해 신규 데이터 입력. Velocity Pressure Name 지정 |
| 4 | 선택한 Velocity Pressure Case 검토(단위: kN/m²) |
| 5 | Force Coefficient 지정. 우측 `(...)` 버튼으로 BS EN 기준 자동 계산 활성화 가능 |
| 6 | Structural Factor(CsCd) 지정. 코드 기준값은 1.0 |
| 7 | 대상 요소 선택 — 모델에서 하중을 적용할 보 요소를 선택한 뒤 Plug-in으로 가져옴 |
| 8 | 하중 적용 방향 지정 |
| 9 | 필요 시 Restraint Height 입력 — 모델에 포함되지 않은 난간(parapet)·방호벽(barrier) 등의 추가 높이 |
| Apply | 설정 완료 후 클릭하면 하중이 입력됨 |

## 참고/제약사항

### Procedure 선택 기준

| 절차 | 근거 조항 | 적용 대상 |
| --- | --- | --- |
| Simplified Procedure | Clause 3.4.2 | 단순한 요구사항으로 충분한 대다수 고속도로 구조물에 적용 |
| Full Procedure | Clause 3.4.3 | 풍유발 파괴에 대해 더 높은 수준의 구조적 신뢰성이 요구되는 구조물. 다음 중 하나에 해당하면 **필수**: ① 경간이 100m를 초과하는 교량, ② 전략도로(Strategic Routes)에 위치하거나 Chief Highway Engineer/Bridges and Structures가 지정한 교량, ③ 지상 높이가 40m를 초과하는 교량 |

> ⚠️ Clause 3.4.4에 정의된 **Dynamic Response Procedure**는 이 Plug-in에서 다루지 않는다
> (참고: UK NA to BS EN 1991-1-4 Clause NA.2.49).

Simplified Procedure를 선택하면 관련 기준에 따라 첨두풍압(Peak Wind Pressure)이 자동
계산되어 제공된다.

**사용자 입력·계산:** 사용자가 기준 표의 변수를 입력하고 Calculate 버튼을 클릭하면
풍속압(Wind Velocity Pressure)이 계산·적용된다.

**자동 계산에 사용되는 표:**
- Table 3.6: Wind Velocities
- Table 3.7: Peak Velocity Pressure
- Table 3.8: Exposure to Wind

메뉴 탐색을 단순화하기 위해 Simplified Procedure는 Section 3.4.1 General에 제시된 Table
3.6 Wind Velocity 값을 포함한다. **Full Procedure**에서는 첨두속도압 또는 평균속도압
계산에 더 상세한 입력이 필요하며, 선택한 탭에 따라 계산에 사용되는 파라미터가 달라진다.
각 입력 필드의 툴팁은 SDM2013 기준과 각 파라미터의 풍하중 효과 계산상 역할을 기준으로
제공된다.

## 관련 JSON API 엔드포인트

Plug-in이 계산 결과를 적용하는 대상은 성격상 `docs/manual`의 정적 풍하중·정적하중케이스
엔드포인트와 연동될 가능성이 높다. 다만 SDM 2013(홍콩) 코드와의 정확한 필드 대응은
확인되지 않았다 — 참고용으로만 링크한다.

- [`/db/STLD` — Static Load Cases](../../manual/06_DB_Static_Loads.md) *(적용 대상 하중케이스)*
- [`/db/SWIND` — Static Wind Load](../../manual/06_DB_Static_Loads.md) *(코드별 필드 대응 미확인)*

## 결론 (원문)

이 Plug-in으로 교량 구조물에 대한 풍작용의 영향을 명확히 이해할 수 있어, 엔지니어와
설계자가 SDM 2013 지침을 풍하중 해석에 효율적으로 적용하는 데 도움이 된다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/40645303004697-Wind-Load-Calculator-for-bridges-HK](https://support.midasuser.com/hc/en-us/articles/40645303004697-Wind-Load-Calculator-for-bridges-HK)
