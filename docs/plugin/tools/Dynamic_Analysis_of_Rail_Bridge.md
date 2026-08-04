# Dynamic Analysis of Rail Bridge

> **원문:** [Dynamic Analysis of Rail Bridge](https://support.midasuser.com/hc/en-us/articles/60340982021529-Dynamic-Analysis-of-Rail-Bridge)
> **원문 작성:** 2026-07-23 · **원문 최종 편집:** 2026-07-23

---

## 개요

철도 교량의 동적 해석은 다양한 열차 하중·운행 속도 조건에서 구조 가속도를 정밀하게 평가해야
한다. 이 Plug-in은 해석 모델 안에 다수의 시간이력 하중케이스 생성을 자동화해, 하중 정의·
데이터 추출·결과 해석에 드는 수작업을 크게 줄인다. 교량의 동적 응답을 정확하고 일관되게
평가할 수 있도록 효율을 높인다.

## 지원 버전

`MIDAS CIVIL NX 2026 (v1.1)`

## 주요 기능

- **자동화된 효율성:** 다양한 속도·구성에 걸친 시간이력 하중케이스의 반복적 수동 정의를
  없앤다.
- **표준화·일관성:** 국제 표준(**EN1991-2:2003, Clause 6.4.6.3 (2)**)에 근거한 기본 감쇠값을
  적용해 신뢰성 있는 해석을 지원한다.
- **원활한 보고·내보내기:** 운행 속도 대 최대 가속도를 즉시 그래프로 표시하고, 종합적인
  보고를 위한 동적 Excel 내보내기 기능을 제공한다.

## 사용 방법

| 필드 | 설명 |
| --- | --- |
| Train Speed Parameters | Initial Speed·Final Speed·Speed Increment를 정의하면 필요한 모든 시간이력 하중케이스가 자동 생성됨 |
| Time Step Increment | 각 시간이력 케이스의 솔버 적분용 시간 간격(Δt) 설정 |
| Bridge Type for Damping | 사전 설정된 교량 유형(EN1991-2 기본값 적용) 선택 또는 사용자 정의 감쇠값 직접 입력 |
| Train Load File | 열차 하중 데이터(일련번호, 축하중, 축간거리)가 담긴 Excel 파일 업로드. Plug-in이 자동 검증하고 인접 창에 설정을 미리보기 |
| Rail Track Nodes | 동적 축하중이 이동할 궤도 경로를 나타내는 구조 노드 그룹 지정 |
| Acceleration Output Nodes | 수직 구조 가속도 응답을 평가할 구조 노드 그룹 선택 |
| Speed vs. Acceleration Plot | 정의된 속도 범위에서 절대 최대 가속도 곡선을 검토하고 전체 데이터셋을 Excel로 내보내기 |

## 참고/제약사항

해석 실행 전 반드시 확인해야 할 핵심 모델링 조건(원문 명시):

- **요소 메시 형상:** 궤도 경로를 따라 연속된 임의의 두 교량 요소 길이 합(x1 + x2)은 임의의
  두 열차 축 사이 최소 거리(d_min)보다 반드시 커야 한다 — `x1 + x2 > d_min`.
- **데이터 완결성:** Plug-in 인터페이스 대화상자의 모든 필수 입력 필드는 동적 솔버 실행 전에
  채워지고 검증되어 있어야 한다.

## 관련 JSON API 엔드포인트

Plug-in이 생성하는 시간이력 하중케이스는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/THIS` — Time History Load Cases](../../manual/09_DB_Dynamic_Loads.md)

## 결론 (원문)

Dynamic Analysis of Rail Bridge Plug-in은 복잡한 열차-구조물 동적 상호작용 해석을 표준화되고
신뢰성 있으며 고도로 자동화된 절차로 전환한다. 자동 하중케이스 생성, 기준 준수 감쇠값,
그래픽 출력을 통합해, 엔지니어는 고속철도 운행 조건에서 교량의 동적 성능을 완전한 확신을
가지고 효율적으로 검증할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/60340982021529-Dynamic-Analysis-of-Rail-Bridge](https://support.midasuser.com/hc/en-us/articles/60340982021529-Dynamic-Analysis-of-Rail-Bridge)
