# SPACE GASS Converter

> **원문:** [SPACE GASS Converter](https://support.midasuser.com/hc/en-us/articles/35824220762521-SPACE-GASS-Converter)
> **원문 작성:** 2024-08-02 · **원문 최종 편집:** 2025-08-01

---

## 개요

SPACE GASS `.txt` 파일의 모델 데이터를 Civil NX로 효율적으로 가져오는 Plug-in이다. SPACE
GASS 파일을 Civil NX 모델링으로 직접 임포트할 수 있다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

SPACE GASS 모델 파일을 이용해 Civil NX로 모델 데이터를 효율적으로 가져온다. 재료·단면 관련
데이터, 요소·노드 같은 형상 데이터, 경계조건·하중 데이터를 자동 변환하면서 원본 데이터의
무결성을 유지해 신뢰성 있고 정확한 시뮬레이션을 가능하게 한다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | **Import** 버튼 클릭 |
| 2 | SPACE GASS `.txt` 파일 임포트(텍스트(txt) SPACE GASS 파일만 임포트 가능) |
| 3 | 임포트한 SPACE GASS 텍스트 파일 확인 |
| 4 | SPACE GASS 모델링 정보 확인(읽기 전용 에디터) |
| 5 | **Send** 버튼 클릭 |
| 6 | Civil 모델 생성 |

## 참고/제약사항 — SPACE GASS → midas Civil 변환 매핑

### 변환 가능한 데이터 범주

`MATERIAL`, `SECTION`, `NODE`, `ELEMENT`, `BOUNDARY CONDITION`, `LOAD`

### MATERIAL / SECTION

재료·단면 정보는 User Defined 방식과 호환된다.

### NODE (좌표계 변환)

SPACEGASS와 midas Civil의 전역좌표계가 서로 달라 다음과 같이 변환된다.

| | SPACE GASS | MIDAS CIVIL NX |
| --- | --- | --- |
| X-DIR | X | X |
| Y-DIR | Y | Z |
| Z-DIR | Z | -Y |

### ELEMENT

| SPACE GASS | MIDAS CIVIL NX |
| --- | --- |
| Normal | General Beam |
| Plate | Plate |
| Tension Only | Tension Only |
| Compression Only | Compression Only |

### BOUNDARY CONDITION

다음 데이터가 변환 가능하다: `SUPPORT`, `POINT SPRING`, `RIGID LINK / ELASTIC LINK`,
`BEAM END RELEASE`

### LOADCASE

| SPACE GASS | MIDAS CIVIL NX |
| --- | --- |
| SELF LOAD | SELF WEIGHT |
| PRESCRIBED DISPLACEMENT | SPECIFIED DISPLACEMENT OF SUPPORT |
| MEMBER CONCENTRATED LOAD | NODAL LOAD |
| MEMBER DISTRIBUTED FORCE | UNIFORM LOAD |
| MEMBER DISTRIBUTED MOMENT | UNIFORM MOMENT |
| PLATE PRESSURE LOAD | PRESSURE LOAD |

## 결론 (원문)

SPACE GASS Converter로 MIDAS CIVIL NX에 모델 정보를 빠르게 가져올 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35824220762521-SPACE-GASS-Converter](https://support.midasuser.com/hc/en-us/articles/35824220762521-SPACE-GASS-Converter)
