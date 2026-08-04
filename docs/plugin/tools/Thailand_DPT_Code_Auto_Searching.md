# Thailand DPT Code Auto Searching

> **원문:** [Thailand DPT Code Auto Searching](https://support.midasuser.com/hc/en-us/articles/52715682940313-Thailand-DPT-Code-Auto-Searching)
> **원문 작성:** 2025-11-24 · **원문 최종 편집:** 2025-11-25

---

## 개요

태국 건물 위치(도(Province)·군(District))를 기준으로 **DPT**(Department of Public Works
and Town & Country Planning) 설계 코드를 빠르고 직관적으로 검색하도록 만들어진 Plug-in이다.
복잡한 설계 코드 문서를 수동으로 검색할 필요 없이, 지도 기반 인터페이스에서 건물 위치를
선택하기만 하면 해당 지역의 지진하중 설계 파라미터(Seismic Zone, Ss, S1)와 풍하중 설계
파라미터(Wind Zone, Wind Speed, Typhoon Factor)를 즉시 확인할 수 있다.

## 지원 버전

- `MIDAS GEN NX 2026 (v1.1) US`
- 적용 기준: Thailand DPT (Department of Public Works and Town & Country Planning)

## 주요 기능

- **시간 절약:** 설계 코드 문서를 수동으로 검색하고 여러 표를 교차 참조하던 시간을 클릭
  한 번으로 없앤다.
- **정확한 위치 매칭:** 지도 기반 선택으로 도·군을 정확히 매칭해 위치 오류를 방지한다.
- **시각적 검증:** 선택한 지역이 지도에 시각적으로 표시되어 위치 확인이 직관적이다.
- **이중 언어 지원:** 태국어·영어를 자유롭게 전환할 수 있어 현지·해외 사용자 모두 편리하게
  사용 가능.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | 페이지 좌측 상단에서 태국어·영어 즉시 전환 |
| 2 | 좌측 드롭다운에서 건물이 위치한 도(Province) 선택 |
| 3 | 우측 드롭다운에서 건물이 위치한 군(District) 선택 |
| 4 | 군을 선택하면 지도가 해당 군으로 확대되고, 군 영역이 주황색으로 강조 표시됨 |
| 5 | 지도 옆 **Detailed Information** 섹션에서 DPT 설계 파라미터 확인 |

## 참고/제약사항

- **언어 선택:** 화면 상단 "Select Language / เลือกภาษา" 드롭다운에서 TH(태국어) 또는
  EN(영어) 선택.
- **도(Province) 선택:** 태국 77개 도 중 선택 가능. 선택 시 지도가 해당 도를 중심으로
  이동하고 도 경계 전체가 파란색으로 표시됨.
- **군(District) 선택:** 선택한 도에 속한 군만 목록에 표시되며(도 선택에 따라 자동
  필터링), 선택 시 지도가 해당 군으로 확대되고 주황색으로 강조 표시됨.
- **지도 표시:** 정확한 위치 확인을 위해 선택한 군을 중심으로 자동 확대.
- **DPT 설계 파라미터** — 지진하중: Seismic Zone(지진구역 분류), Ss(단주기 스펙트럼 응답
  가속도계수), S1(1초 주기 스펙트럼 응답 가속도계수). 풍하중: Wind Zone(풍속구역 분류, 예:
  4B, 1 등), Wind Speed(설계풍속, m/s), Typhoon Factor(태풍강도 배율, TF).

## 결론 (원문)

이 애플리케이션은 지리적 위치를 기준으로 태국 DPT 설계 코드를 조회하는 포괄적이고 사용하기
쉬운 환경을 제공한다. 직관적인 지도 기반 인터페이스와 이중 언어 지원, 즉시 파라미터 조회를
결합해 구조 설계 과정의 투명성과 정확성을 보장한다. 엔지니어는 태국 어느 위치든 정확한
지진·풍하중 파라미터를 빠르게 식별할 수 있어 수동 조회 오류 위험을 없애고 여러 코드 문서를
교차 참조하는 시간을 크게 줄인다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/52715682940313-Thailand-DPT-Code-Auto-Searching](https://support.midasuser.com/hc/en-us/articles/52715682940313-Thailand-DPT-Code-Auto-Searching)
