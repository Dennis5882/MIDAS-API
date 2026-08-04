# GEN NX to Staad Converter

> **원문:** [GEN NX to Staad Converter](https://support.midasuser.com/hc/en-us/articles/56728677543321-GEN-NX-to-Staad-Converter)
> **원문 작성:** 2026-04-07 · **원문 최종 편집:** 2026-07-27

---

## 개요

MIDAS GEN NX 모델을 STAAD.Pro의 `.std` 형식으로 변환하는 Plug-in이다. 형상·재료 물성·
하중 조건 전반에서 데이터 무결성을 유지하도록 만들어져 수작업 재모델링 시간을 크게 줄인다.

## 지원 버전

`MIDAS GEN NX 2026 (v1.1) US`

## 주요 기능

- **시간 절약:** STAAD에서 모델을 수동으로 재작성할 필요를 없애, 몇 시간 걸리던 재모델링
  작업을 몇 분으로 줄인다.
- **투명한 변환:** 내장 로그가 무엇이 변환됐고 어떤 항목이(있다면) 지원되지 않았는지 명확히
  나열해, 엔지니어가 변환 내용을 빠르게 검토할 수 있다.
- **사용 편의성:** 변환할 데이터를 선택하고 `.STD` 파일을 생성하는 간단한 인터페이스.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | 체크박스로 내보낼 데이터 선택: Geometry, Material Properties, Section Properties, Supports, Loads, Load Combinations |
| 2 | **Generate .STD File** 클릭 시 변환 시작(진행률 표시줄로 처리 상태 표시) |
| 3 | **Download .STD File** 클릭 시 생성된 `.std` 파일 저장 |
| 4 | **Logs** 섹션을 펼쳐 변환 메시지, 매핑 노트, 미지원/생략 항목 경고 확인 |
| 5 | **Reset**으로 현재 실행을 초기화하고 새 변환 시작 |

로그 패널은 API 연결 및 데이터 프리페치부터 최종 파일 생성까지 모든 단계를 상세히 기록하며,
변환 중 발견된 미지원 기능에 대한 명시적 경고도 포함한다.

## 참고/제약사항 — MIDAS GEN NX → STAAD.Pro 변환 매핑

### 변환 가능한 데이터 범주

`UNITS`, `MATERIAL PROPERTIES`, `SECTION PROPERTIES`, `BOUNDARY CONDITION`,
`MEMBER SPECIFICATION`, `RELEASE`, `LOAD`, `LOAD CASE & COMBINATION` (및 `GEOMETRY`)

### NODE (좌표계 변환)

전역좌표계가 서로 달라 다음과 같이 변환된다.

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| X | Z |
| Y | X |
| Z | Y |

### ELEMENT

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| Beam | Member |
| Truss | Member Truss |
| Plate | Shell Element |
| Wall | Shell Element |

> ⚠️ 인장전용(Tension-only)·압축전용(Compression-only) 부재는 현재 지원하지 않는다.

### MATERIAL

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| Isotropic | Isotropic (E, Poisson, Density, Alpha, Damping) |
| Orthotropic | 미지원 |
| SRC | 미지원 |

### SECTION

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| I (I Section) | ISECTION / TABLE ST |
| C (Channel) | GENERAL with Profile Points |
| L (Angle) | GENERAL with Profile Points |
| T (Tee) | TEE |
| B (Box) | TUBE |
| P (Pipe) | PIPE |
| 2L (Double Angle) | DOUBLE ANGLE |
| 2C, 2CB (Double Channel) | GENERAL with Profile Points |
| SB (Solid Rectangle) | PRIS YD ZD |
| SR (Solid Round) | PRIS YD |
| 그 외 | 원 단면 속성을 가진 GENERAL(0.1m × 0.1m Placeholder Profile Points) |

> ⚠️ `VALUE`, `SRC`, `COMBINED`, `TAPERED`, `COMPOSITE` 단면 타입은 현재 지원하지 않는다.

### BOUNDARY CONDITION

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| Support (Fixed / Pinned / Partial) | FIXED / PINNED / FIXED BUT |
| Point Spring (Linear) | KFX, KFY, KFZ, KMX, KMY, KMZ |
| Rigid Link | SLAVE RIGID MASTER |

> ⚠️ 비선형 Point Spring과 스프링 감쇠(damping)는 지원하지 않는다.

### RELEASE

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| 1D Member Release (Full DOF) | MEMBER RELEASE |
| 1D Member Release (Partial Moment) | MPX / MPY / MPZ |
| 1D Member Release (Spring) | Spring KFX–KMZ |
| 2D Plate Release (J1–J4) | PLATE RELEASE |

### LOAD

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| Self Weight | SELFWEIGHT |
| Nodal Load (Force / Moment) | JOINT LOAD |
| Beam Concentrated Force | MEMBER LOAD CON |
| Beam Concentrated Moment | MEMBER LOAD CMON |
| Beam Uniform / Trapezoidal Force | MEMBER LOAD TRAP |
| Beam Uniform Moment | MEMBER LOAD UMON (discretized) |
| Pressure Load (Uniform) | ELEMENT LOAD PRESSURE |
| Pressure Load (Trapezoidal) | ELEMENT LOAD TRAP JT |

> ⚠️ 보 하중의 편심(eccentricity)은 지원하지 않는다. 바닥하중(FBLA)은 Plug-in 실행 전
> MIDAS에서 보하중으로 사전 변환해야 한다. STAAD 자체 제약으로 투영(projection)이 있는
> 사다리꼴 압력하중은 지원하지 않는다.

### LOAD CASE

MIDAS 하중케이스 코드(`D`, `L`, `W`, `E`, `T`, `S` 등)가 STAAD `LOADTYPE` 키워드(`Dead`,
`Live`, `Wind`, `Seismic-H`, `Temperature`, `Snow` 등)로 매핑된다.

### LOAD COMBINATION

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| Algebraic | ADD |
| Absolute | ABS |
| SRSS | SRSS |

> ⚠️ Envelope 조합(중첩된 envelope 포함)은 지원하지 않는다.

### 기타 미지원 기능 (수동으로 STAAD.Pro에 정의 필요)

- Floor Diaphragms
- Beam end offsets
- Section Stiffness Scale Factors
- Load to Masses
- Static Seismic Loads
- Static Wind Loads

## 결론 (원문)

GEN NX to STAAD Converter는 MIDAS GEN NX에서 STAAD.Pro로 구조 모델을 빠르고 신뢰성 있게
옮기는 방법을 제공한다. 형상·물성·경계조건·하중·조합 전달을 자동화해, 엔지니어가 플랫폼 간
모델 재구축이 아니라 해석·설계에 더 많은 시간을 쓸 수 있게 돕는다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/56728677543321-GEN-NX-to-Staad-Converter](https://support.midasuser.com/hc/en-us/articles/56728677543321-GEN-NX-to-Staad-Converter)
