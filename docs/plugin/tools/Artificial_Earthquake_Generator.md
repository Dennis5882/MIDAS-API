# Artificial Earthquake Generator

> **원문:** [Artificial Earthquake Generator](https://support.midasuser.com/hc/en-us/articles/35656036758937-Artificial-Earthquake-Generator)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

기준에 따라 시간이력해석용 **응답스펙트럼**과 **인공지진파**를 생성하고 그래프를 만드는
Plug-in이다. 설계 스펙트럼을 이용해 인공 지진파를 생성하고 스펙트럼 하중 그래프로 변환할 수
있다. ASCE7 스펙트럼 시리즈 기준을 포함하며, 데이터는 USGS Seismic Design Geodatabase에서
가져온다.

## 지원 버전

- `MIDAS CIVIL NX 2024 (v1.1) US`
- 적용 기준: American Standard (ASCE7-22)

## 주요 기능

USGS Seismic Design Geodatabase를 기반으로 ASCE7-22 기준 응답스펙트럼 데이터를 제공한다.
지정 지역의 위도/경도 데이터를 조회하고 4가지 RS 데이터 유형을 제공한다.

- Two-Period Design Spectrum
- Two-Period MCEr Spectrum
- Multi-Period Design Spectrum
- Multi-Period MCEr Spectrum

생성된 RS 데이터를 바탕으로 목표 스펙트럼에 맞춰 RS 매칭(spectral matching)을 통해 정합된
인공 지반운동 데이터도 생성한다.

- 기준에 따른 정확한 응답스펙트럼·인공 지진파 생성
- USGS 데이터를 이용한 신뢰성 있는 결과
- 생성 데이터를 그래프로 시각화해 분석 용이
- 설계 기준 선택·데이터 입력을 위한 사용하기 쉬운 인터페이스

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1. Spectrum Standard 선택 | Plug-in을 실행하고 설계 스펙트럼 기준(ASCE7-22)을 선택 |
| 2. Target Address 입력 | 대상 주소를 입력하고 **Search** 클릭. 주소(By Address) 또는 위도/경도(By Latitude/Longitude)로 입력 가능 |
| 3. Seismic Data 입력 | Risk Category, Soil Site Class, Design Spectrum Option 설정 |
| 4. Calc. Design Spectrum | 클릭하면 응답스펙트럼 계산 |
| 5. Artificial Earthquake Data 설정 | 인공지진 데이터 계산을 위해 Rise·Level·Total time·Damping Ratio 등 지진 규모에 맞는 값 입력 |
| 6. Calc. Artificial Earthquake | 클릭하면 시간이력함수 데이터 생성 |
| 7. 결과 분석 | 결과 그래프를 시각화해 분석 |
| 8. Update RS Function / Update TimeHistory Function | 클릭하면 결과 데이터를 프로그램으로 가져옴(import) |

### 응답스펙트럼 데이터 생성 방법

대상 지역을 검색하고 Seismic Data에 지진위험계수·지진구역계수를 입력한 뒤 **Calc. Design
Spectrum**을 클릭하면, USGS Seismic Design Geodatabase 기반 응답스펙트럼 데이터가 출력된다.
시각화·텍스트 결과를 검토한 뒤 **Update RS Function**을 클릭하면 Civil NX의 **RS
Functions**로 데이터를 가져온다.

### 시간이력해석용 인공지진파 생성 방법

설계 스펙트럼에서 설계 기준을 선택하고 Envelope Function 데이터·최대 가속도·감쇠비 등 평가
대상 지진 강도에 맞는 함수 입력값을 입력한다. **Calc. Artificial Earthquake**를 클릭하면
인공지진파를 생성하고 스펙트럼 또는 가속도 그래프로 변환한다. 결과 검토 후 **Update
TimeHistory Functions**를 클릭하면 Civil NX의 **TimeHistory Functions**로 데이터를 가져온다.

생성된 인공 지진파는 **Graph Type**으로 스펙트럼·가속도 그래프 형태로 전환해 볼 수 있다.

## 관련 JSON API 엔드포인트

원문에서 결과를 가져오는 대상으로 명시한 Civil NX의 "RS Functions"·"TimeHistory Functions"는
`docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/SPFC` — Response Spectrum Functions](../../manual/09_DB_Dynamic_Loads.md)
- [`/db/THFC` — Time History Functions](../../manual/09_DB_Dynamic_Loads.md)

## 결론 (원문)

이 가이드로 새 기준(ASCE7-22) 기반 RS 및 인공지진파 생성 Plug-in을 이용해 시간이력해석용
응답스펙트럼·인공지진파를 효과적으로 생성·분석할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35656036758937-Artificial-Earthquake-Generator](https://support.midasuser.com/hc/en-us/articles/35656036758937-Artificial-Earthquake-Generator)
