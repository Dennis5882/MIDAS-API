# 09. DB – Dynamic Loads

동적 하중 관련 데이터베이스 API입니다.  
응답 스펙트럼(Response Spectrum) 함수 및 하중 케이스, 시간이력(Time History) 전역 제어, 함수, 하중 케이스를 포함합니다.

> **Base URL**
> - MIDAS CIVIL NX : `https://moa-engineers.midasit.com:443/civil`
> - MIDAS GEN NX   : `https://moa-engineers.midasit.com:443/gen`
>
> **인증** : 모든 요청 헤더에 `MAPI-Key: <your-api-key>` 포함

---

## 목차

| # | Endpoint | 설명 |
|---|----------|------|
| 1 | [/db/SPFC](#1-dbspfc--response-spectrum-functions) | 응답 스펙트럼 함수 |
| 2 | [/db/SPLC](#2-dbsplc--response-spectrum-load-cases) | 응답 스펙트럼 하중 케이스 |
| 3 | [/db/THGC](#3-dbthgc--time-history-global-control) | 시간이력 전역 제어 |
| 4 | [/db/THGC-M1](#4-dbthgc-m1--time-history-global-control-hyper-s) | 시간이력 전역 제어 (Hyper-S) |
| 5 | [/db/THOO-M1](#5-dbthoo-m1--time-history-output-option-hyper-s) | 시간이력 출력 옵션 (Hyper-S) |
| 6 | [/db/THIS](#6-dbthis--time-history-load-cases) | 시간이력 하중 케이스 |
| 7 | [/db/THIS-M1](#7-dbthis-m1--time-history-load-cases-hyper-s) | 시간이력 하중 케이스 (Hyper-S) |
| 8 | [/db/THFC](#8-dbthfc--time-history-functions) | 시간이력 함수 |
| 9 | [/db/THGA](#9-dbthga--ground-acceleration) | 지반 가속도 |
| 10 | [/db/THNL](#10-dbthnl--dynamic-nodal-loads) | 동적 절점 하중 |
| 11 | [/db/THSL](#11-dbthsl--time-varying-static-loads) | 시변 정적 하중 |
| 12 | [/db/THMS](#12-dbthms--multiple-support-excitation) | 다중 지점 가진 |

---

## 1. /db/SPFC – Response Spectrum Functions

응답 스펙트럼 함수를 정의합니다.  
`STR.SPEC_CODE` 값으로 User 정의, 한국 코드, 미국 코드, Eurocode, 중국, 인도, 대만 등 다양한 설계 기준을 지원합니다.

### 1-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/SPFC` | 전체 응답 스펙트럼 함수 조회 |
| `GET` | `{base_url}/db/SPFC/{id}` | 특정 ID 응답 스펙트럼 함수 조회 |
| `POST` | `{base_url}/db/SPFC` | 응답 스펙트럼 함수 생성 |
| `PUT` | `{base_url}/db/SPFC` | 응답 스펙트럼 함수 전체 수정 |
| `PUT` | `{base_url}/db/SPFC/{id}` | 특정 ID 응답 스펙트럼 함수 수정 |
| `DELETE` | `{base_url}/db/SPFC` | 전체 응답 스펙트럼 함수 삭제 |
| `DELETE` | `{base_url}/db/SPFC/{id}` | 특정 ID 응답 스펙트럼 함수 삭제 |

### 1-2. 공통 파라미터 (모든 코드 타입)

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | RS 함수명 | `NAME` | String | - | Required |
| 2 | 스펙트럼 데이터 타입 (1=정규화가속도, 2=가속도, 3=속도, 4=변위) | `iTYPE` | Integer | - | Required |
| 3 | 스케일 방법 (0=Scale Factor, 1=Max Value) | `iMETHOD` | Integer | 0 | Optional |
| 4 | 스케일 값 | `SCALE` | Number | - | Required |
| 5 | 중력 가속도 (정규화 가속도 타입에만 해당) | `GRAV` | Number | - | Required |
| 6 | 감쇠비 | `DRATIO` | Number | 0.05 | Optional |
| 7 | 설명 | `DESC` | String | Blank | Optional |

---

#### 1-2-A. User Type

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 8 | 함수 데이터 배열 | `aFUNC` | Array[Object] | - | Required |
| (1) | 주기 (sec) | `PERIOD` | Number | - | Required |
| (2) | 값 (데이터 타입에 따라 다름) | `VALUE` | Number | - | Required |

**Request Body 예시 (User Type)**

```json
{
  "Assign": {
    "1": {
      "NAME": "RS_func",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "DESC": "",
      "aFUNC": [
        { "PERIOD": 0,    "VALUE": 0.11  },
        { "PERIOD": 0.06, "VALUE": 0.308 },
        { "PERIOD": 0.12, "VALUE": 0.308 },
        { "PERIOD": 0.3,  "VALUE": 0.308 },
        { "PERIOD": 0.36, "VALUE": 0.2567},
        { "PERIOD": 0.6,  "VALUE": 0.154 },
        { "PERIOD": 1.2,  "VALUE": 0.077 }
      ]
    }
  }
}
```

---

#### 1-2-B. Korea Type

`STR` 오브젝트의 `SPEC_CODE` 값으로 한국 설계 기준을 선택합니다.

| SPEC_CODE 값 | 설명 |
|---|---|
| `"KDS(41-17-00:2019)"` | KDS 41 17 00 : 2019 내진설계기준 |
| `"KDS(17-10-00:2018)"` | KDS 17 10 00 : 2018 도로교 내진설계기준 |
| `"KS_BRG"` | 한국 교량 기준 |
| `"KBC2016"` | KBC 2016 |
| `"KBC2009"` | KBC 2009 |
| `"KBC2005"` | KBC 2005 |
| `"KS2000"` | KS 2000 |

**KDS(41-17-00:2019) 추가 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 8 | 코드 데이터 (STR 오브젝트) | `STR` | Object | - | Required |
| (1) | 설계 스펙트럼 코드 | `SPEC_CODE` | `"KDS(41-17-00:2019)"` | - | Required |
| 9 | 옵션 데이터 (OPT 오브젝트) | `OPT` | Object | - | Optional |
| (1) | 지반 분류 (0=S1, 1=S2, 2=S3, 3=S4, 4=S5, 5=S6) | `SC_` | Integer | 0 | Optional |
| (2) | 지진 구역 (0=구역1, 1=구역2) | `iSEISZONE` | Integer | 0 | Optional |
| 10 | 계수 데이터 (VAL 오브젝트) | `VAL` | Object | - | Required |
| (1) | 스펙트럼 응답 가속도 [Sds, Sd1] | `aSRA` | Array[Number, 2] | - | Required |
| (2) | 지반 증폭 계수 [Fa, Fv] | `aSCP` | Array[Number, 2] | - | Required |
| (3) | 최대 주기 | `PERIOD` | Number | - | Required |
| (4) | 중요도 계수 (Ie) | `IE` | Number | - | Required |
| (5) | 반응 수정 계수 (R) | `R_` | Number | - | Required |
| (6) | EPA (구역 계수) | `ZONEFACTOR` | Number | - | Required |
| 11 | 계산 옵션 | `CALC_OPT` | Boolean | false | Create Only |

**KDS(17-10-00:2018) 추가 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| (1) | 지반 분류 (0=S1 ~ 5=S6) | `SC_` | Integer | 0 | Optional |
| (2) | 지진 구역 (0=구역1, 1=구역2) | `iSEISZONE` | Integer | 0 | Optional |
| VAL.(1) | 지반 증폭 계수 [Fa, Fv] | `aSCP` | Array[Number, 2] | - | Required |
| VAL.(2) | 최대 주기 | `PERIOD` | Number | - | Required |
| VAL.(3) | 지진 위험도 계수 (I) | `IE` | Number | - | Required |

**KS_BRG (한국 교량) 추가 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| VAL.(1) | 지진 구역 계수 (Ar): Area I=0.11, Area II=0.07 | `EPA` | Number | - | Required |
| VAL.(2) | 최대 주기 | `PERIOD` | Number | - | Required |
| VAL.(3) | 지반 프로파일 타입 (S1=1.0, S2=1.2, S3=1.5, S4=2.0) | `SPTYPE` | Number | - | Required |
| VAL.(4) | 중요도 계수 (I) | `IE` | Number | - | Required |
| VAL.(5) | 반응 수정 계수 (R) | `R_` | Number | - | Required |

**Request Body 예시 (KDS 41-17-00:2019)**

```json
{
  "Assign": {
    "2": {
      "NAME": "KDS_2019_func",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "KDS(41-17-00:2019)" },
      "OPT": { "SC_": 2, "iSEISZONE": 0 },
      "VAL": {
        "aSRA": [0.22, 0.154],
        "aSCP": [1.0, 1.5],
        "PERIOD": 4.0,
        "IE": 1.2,
        "R_": 5.0,
        "ZONEFACTOR": 0.22
      }
    }
  }
}
```

---

#### 1-2-C. US Type

| SPEC_CODE 값 | 설명 |
|---|---|
| `"AASHTO-LRFD12"` | AASHTO LRFD 2012 |
| `"IBC2012"` | IBC 2012 |
| `"IBC2009"` | IBC 2009 |
| `"IBC2000"` | IBC 2000 |
| `"UBC97"` | UBC 1997 |
| `"UBC88"` | UBC 1988 |

**Request Body 예시 (IBC 2012)**

```json
{
  "Assign": {
    "3": {
      "NAME": "IBC2012_func",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "IBC2012" },
      "OPT": { "SC_": 2 },
      "VAL": {
        "aSRA": [0.5, 0.2],
        "aSCP": [1.0, 1.5],
        "PERIOD": 4.0,
        "IE": 1.0,
        "R_": 5.0
      }
    }
  }
}
```

---

#### 1-2-D. Eurocode Type

| SPEC_CODE 값 | 설명 |
|---|---|
| `"EURO2004"` | Eurocode 8 (2004) |
| `"EURO1996"` | Eurocode 8 (1996) |
| `"EURO1996_ELA"` | Eurocode 8 (1996) Elastic |

**EURO2004 주요 추가 파라미터**

| 설명 | Key | 비고 |
|------|-----|------|
| 스펙트럼 타입 (1=Elastic, 2=Design) | `SPECTYPE` | OPT 오브젝트 |
| 지반 타입 (0=A, 1=B, 2=C, 3=D, 4=E) | `GROUTYPE` | OPT 오브젝트 |
| 국가 부속서 코드 | `NATIONALANNEX` | OPT 오브젝트 |

**Request Body 예시 (EURO2004)**

```json
{
  "Assign": {
    "4": {
      "NAME": "EURO2004_func",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "EURO2004" },
      "OPT": {
        "SPECTYPE": 1,
        "GROUTYPE": 1,
        "NATIONALANNEX": "EN"
      },
      "VAL": {
        "ag": 0.25,
        "PERIOD": 4.0,
        "IE": 1.0
      }
    }
  }
}
```

---

#### 1-2-E. China Type

> ⚠️ 2026-08-25 확인: 이전 문서에는 China/Japan/Taiwan/India/Other Countries Type이 전혀
> 문서화되어 있지 않았음(MVHL과 동일한 유형의 누락). 원문
> [Response Spectrum Functions - China](https://support.midasuser.com/hc/en-us/articles/39473334759065)
> 기준, 9개 코드 중 가장 최신·대표적인 GB50011-2010만 전체 필드를 문서화하고 나머지 8개는
> SPEC_CODE 매핑표로 정리(SECT/TDMT 원칙).

| SPEC_CODE 값 | 설명 |
| --- | --- |
| `"CH2010"` | China (GB50011-2010) — 아래 대표 예시 |
| `"GB50111_2006"` | China (GB50111-2006) |
| `"CH2001"` | China (GB50011-2001) |
| `"CHSH2003"` | China Shanghai (DGJ08-9-2003) |
| `"CH_BRG89"` | China (JTJ004-89) |
| `"JTG/T 2231-01-2020"` | China (JTG/T 2231-01-2020) |
| `"JTG/T B02-01-2008"` | China (JTG/T B02-01-2008) |
| `"CH_GBJ111_87"` | China (GBJ11-87) |
| `"CJJ 166-2011"` | China (CJJ 166-2011) |

**GB50011-2010 추가 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 8-(2) | 설계 지진 등급(Seismic Fortification Intensity) | `SFI`(STR) | String | `"0.05g"` | Optional |
| 8-(3) | 지반 종류(I0/I1/II/III/IV) | `SC_`(STR) | String | `"I0"` | Optional |
| 8-(4) | 지진 영향(Frequent/Middle/Scarce) | `EQ_`(STR) | String | – | Required |
| 9-(1) | 근원 유형(0/1/2) | `NSC`(OPT) | Integer | 0 | Optional |
| 9-(2) | 공칭 횡력(0=전단력차, 1=관성력) | `nLForce`(OPT) | Integer | 0 | Optional |
| 10-(1) | 설계 특성 주기 [Tg, Tg1, Tg2] (GB50011-2010은 Tg만 사용) | `aTG`(VAL) | Array[Number,3] | – | Required |
| 10-(2) | 감쇠비 | `DP`(VAL) | Number | – | Required |
| 10-(3) | 최대 지진영향계수 | `MaxEQ`(VAL) | Number | – | Required |
| 10-(4) | 최대 주기 | `PERIOD`(VAL) | Number | – | Required |

**Request Body 예시 (GB50011-2010)**

```json
{
  "Assign": {
    "5": {
      "NAME": "China(GB50011-10)",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "CH2010", "SFI": "0.10g", "SC_": "II", "EQ_": "MIDDLE" },
      "OPT": { "NSC": 1, "nLForce": 0 },
      "VAL": { "aTG": [0.4, 0, 0], "DP": 0.05, "MaxEQ": 0.23, "PERIOD": 6 },
      "CALC_OPT": true
    }
  }
}
```

---

#### 1-2-F. Japan Type

| SPEC_CODE 값 | 설명 |
| --- | --- |
| `"JPN2000"` | Japan (Arch. 2000) |
| `"JP_BRG2017"` | Japan (Bridge 2017, MIDAS CIVIL NX JP 버전 전용) |
| `"JP_BRG2012"` | Japan (Bridge 2012, MIDAS CIVIL NX JP 버전 전용) |
| `"JP_BRG2002"` | Japan (Bridge 2002) |

**JPN2000(Arch.2000) 추가 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 9-(1) | 지진 지역 계수(Z) 0=1.0/1=0.9/2=0.8/3=0.7 | `iSEISZONEFACTOR`(OPT) | Integer | 0 | Optional |
| 9-(2) | 지반 종류(I/II/III) | `SOILCLASS`(OPT) | Integer | 0 | Optional |
| 10-(1) | 최대 주기 | `PERIOD`(VAL) | Number | – | Required |
| 10-(2) | 밑면 전단력 계수(Co) | `CO`(VAL) | Number | – | Required |

**Bridge2017/2012/2002 공통 추가 파라미터** (SPEC_CODE만 다름)

| No. | 설명 | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 9-(1) | 지반 종류(I/II/III) | `SOILCLASS`(OPT) | Integer | 0 | Optional |
| 9-(2) | 지진 지역(Bridge2017/2012: A1/A2/B1/B2/C, Bridge2002: A/B/C) | `iSEISZONE`(OPT) | Integer | 0 | Optional |
| 9-(3) | 지진 입력 방법(Level1/Level2 Type I/Level2 Type II) | `iEQMETHOD`(OPT) | Integer | 0 | Optional |
| 10-(1) | 최대 주기 | `PERIOD`(VAL) | Number | – | Required |
| 10-(2) | 수정 계수(Cz) — ⚠️ MIDAS가 다른 값으로 자동 계산해 입력값이 무시됨 | `CZ`(VAL) | Number | – | Required |

**Request Body 예시 (JPN2000)**

```json
{
  "Assign": {
    "6": {
      "NAME": "JP2000",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "JPN2000" },
      "OPT": { "iSEISZONEFACTOR": 2, "SOILCLASS": 1 },
      "VAL": { "PERIOD": 6, "CO": 0.2 },
      "CALC_OPT": true
    }
  }
}
```

---

#### 1-2-G. Taiwan Type

> ⚠️ 원문 [Response Spectrum Functions - Taiwan](https://support.midasuser.com/hc/en-us/articles/39473471043737)
> 자체가 7개 코드를 다루는 대형 아티클이라, 가장 최신인 Taiwan(2022)만 전체 필드를 문서화한다.

| SPEC_CODE 값 | 설명 |
| --- | --- |
| `"TAIWAN(2022)"` | Taiwan 2022 — 아래 대표 예시 |
| `"TAIWAN06"` | Taiwan 2006 |
| `"TAIWAN99H"` | Taiwan 1999 Horizontal |
| `"TAIWAN99V"` | Taiwan 1999 Vertical |
| `"TAIWAN(2011)"` | Taiwan Bridge 98 |
| `"TAIWAN89H_BRG"` | Taiwan Bridge 89 Horizontal |
| `"TAIWAN89V_BRG"` | Taiwan Bridge 89 Vertical |

**Taiwan(2022) 추가 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 9-(1) | 지반 종류(Type1/2/3/User Input) | `SOILCLASS`(OPT) | Integer | 0 | Optional |
| 9-(2) | 지진 구역(General/Near Fault/Taipei Basin) | `iSEISZONE`(OPT) | Integer | 0 | Optional |
| 9-(3) | 스펙트럼 방향(0=수평/1=수직) | `iSPECTYPE`(OPT) | Integer | 0 | Optional |
| 9-(4) | 스펙트럼 용도(0=Design/1=Small-Medium/2=Maximum) | `iSPECUSE`(OPT) | Integer | 0 | Optional |
| 9-(5) | 세부 구역(Taipei Basin I~IV/User Input, 구역이 Taipei Basin일 때) | `iSUBZONE`(OPT) | Integer | 0 | Optional |
| 10-(1) | 수평 스펙트럼 가속도 [Sds,Sd1,Sms,Sm1] (General/Near Fault 구역) | `aSRA`(VAL) | Array[Number,4] | – | Required |
| 10-(2) | 대만분지 스펙트럼 가속도 [Sds_t,Sd1_t,Sms_t,Sm1_t] (Taipei Basin 구역) | `aSRA_T`(VAL) | Array[Number,4] | – | Required |
| 10-(3) | 근단층 지진 영향 [Nda,Ndv,Nma,Nmv] (Near Fault 구역) | `aNSF`(VAL) | Array[Number,4] | – | Required |
| 10-(4) | 지반 증폭 계수 [Fda,Fdv,Fma,Fmv] (General/Near Fault 구역) | `aSMF`(VAL) | Array[Number,4] | – | Required |
| 10-(5) | 감쇠비(%) | `DP`(VAL) | Number | – | Required |
| 10-(6) | 최대 주기 | `PERIOD`(VAL) | Number | – | Required |
| 10-(7) | 중요도 계수(I) | `IF`(VAL) | Number | – | Required |
| 10-(8) | 지진 증폭 계수(ay) | `SMFACTOR`(VAL) | Number | – | Required |
| 10-(9) | 반응 수정 계수(R) | `RMFACTOR`(VAL) | Number | – | Required |
| 10-(10) | 기본 주기(T1) | `FUNDAMENTAL_PERIOD`(VAL) | Number | – | Required |

**Request Body 예시 (Taiwan 2022, Near Fault Zone)**

```json
{
  "Assign": {
    "7": {
      "NAME": "Taiwan(2022)",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "TAIWAN(2022)" },
      "OPT": {"SOILCLASS": 0, "iSEISZONE": 1, "iSPECTYPE": 0, "iSPECUSE": 1, "iSUBZONE": 0},
      "VAL": {
        "aSRA": [0.5, 0.3, 0.7, 0.4],
        "aSRA_T": [0.6, 0.8, 1.6, 1.6],
        "aNSF": [0.8, 0.45, 1, 0.6],
        "aSMF": [1, 1, 1, 1],
        "DP": 5, "PERIOD": 6, "IF": 1, "SMFACTOR": 1, "RMFACTOR": 1.6,
        "FUNDAMENTAL_PERIOD": 0.09
      },
      "CALC_OPT": true
    }
  }
}
```

---

#### 1-2-H. India Type

| SPEC_CODE 값 | 설명 |
| --- | --- |
| `"IS1893(2016)"` | India (IS1893:2016) |
| `"IS2002"` | India (IS1893:2002) |
| `"IRC:SP:114-2018"` | India (IRC:SP:114-2018) |

**공통 추가 파라미터 (3개 코드 공통)**

| No. | 설명 | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 9-(1) | 지반 종류(I=Rock/Hard·II=Medium·III=Soft) | `SOILCLASS`(OPT) | Integer | 0 | Optional |
| 9-(2) | 지진 구역(II 0.10/III 0.16/IV 0.24/V 0.36, IRC:SP:114-2018은 User Defined=4도 지원) | `iSEISZONE`(OPT) | Integer | 0 | Optional |
| 10-(1) | 감쇠비(%) | `DP`(VAL) | Number | – | Required |
| 10-(2) | 최대 주기 | `PERIOD`(VAL) | Number | – | Required |
| 10-(3) | 중요도 계수(I) | `IE`(VAL) | Number | – | Required |
| 10-(4) | 반응 저감 계수(R) | `R_`(VAL) | Number | – | Required |
| 10-(5) | 감쇠 배율 계수(값 1 고정) | `DPFAC`(VAL) | Integer | – | Required |
| 10-(6) | 사용자 정의 지진구역 값 (IRC:SP:114-2018, `iSEISZONE`=4일 때만) | `USERDEFSEISZONE`(VAL) | Number | – | Required |

**Request Body 예시 (IS1893:2016)**

```json
{
  "Assign": {
    "8": {
      "NAME": "IS1893(2016)",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "IS1893(2016)" },
      "OPT": { "SOILCLASS": 0, "iSEISZONE": 0 },
      "VAL": { "DP": 5, "PERIOD": 6, "IE": 1, "R_": 3, "DPFAC": 1 },
      "CALC_OPT": true
    }
  }
}
```

---

#### 1-2-I. Other Countries Type

> ⚠️ 원문 [Response Spectrum Functions - Other Countries](https://support.midasuser.com/hc/en-us/articles/39508838720153)
> 가 8개 국가 코드를 다루는 대형 아티클이라, 가장 필드가 단순한 Canada(NBC95)만 전체 문서화하고
> 나머지는 SPEC_CODE 매핑만 남긴다.

| SPEC_CODE 값 | 설명 |
| --- | --- |
| `"NBC95"` | Canada (NBC 1995) — 아래 대표 예시 |
| `"NTC2018"` | Italy (NTC 2018) |
| `"DPWH-LRFD BSDS(2013)"` | Philippines (DPWH-LRFD BSDS 2013) |
| `"AS 5100.2(2017)"` | Australia (AS 5100.2:2017) |
| `"NSR-10"` | Colombia (NSR-10) |
| `"P100-1(2013)"` | Romania (P100-1:2013) |
| `"SP 268.1325800.2016"` | Russia (SP 268.1325800.2016) |
| `"DPT.1301/1302-61:2018"` | Thailand (DPT.1301/1302-61:2018) |

**Canada NBC95 추가 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 9-(1) | 가속도 구역(Za, 0~6) | `ZA`(OPT) | Integer | 0 | Optional |
| 9-(2) | 속도 구역(Zv, 0~6) | `ZV`(OPT) | Integer | 0 | Optional |
| 10-(1) | 최대 주기 | `PERIOD`(VAL) | Number | – | Required |
| 10-(2) | 구역 속도비(v) | `V`(VAL) | Number | – | Required |

**Request Body 예시 (Canada NBC95)**

```json
{
  "Assign": {
    "9": {
      "NAME": "NBC1995",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "NBC95" },
      "OPT": { "ZA": 2, "ZV": 3 },
      "VAL": { "PERIOD": 6, "V": 0.15 },
      "CALC_OPT": true
    }
  }
}
```

---

### 1-3. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 1) User Type 응답 스펙트럼 함수 생성 ────────────────────────────────────
payload_user = {
    "Assign": {
        "1": {
            "NAME": "RS_UserDefined",
            "iTYPE": 1,       # Normalized Acceleration
            "iMETHOD": 0,     # Scale Factor
            "SCALE": 1.0,
            "GRAV": 9.806,
            "DRATIO": 0.05,
            "aFUNC": [
                {"PERIOD": 0.0,  "VALUE": 0.110},
                {"PERIOD": 0.06, "VALUE": 0.308},
                {"PERIOD": 0.12, "VALUE": 0.308},
                {"PERIOD": 0.30, "VALUE": 0.308},
                {"PERIOD": 0.60, "VALUE": 0.154},
                {"PERIOD": 1.20, "VALUE": 0.077},
                {"PERIOD": 4.00, "VALUE": 0.023}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/SPFC", json=payload_user, headers=HEADERS)
print("User SPFC POST:", resp.status_code)

# ── 2) KDS 41-17-00:2019 응답 스펙트럼 함수 생성 ────────────────────────────
payload_kds = {
    "Assign": {
        "2": {
            "NAME": "RS_KDS2019",
            "iTYPE": 1,
            "iMETHOD": 0,
            "SCALE": 1.0,
            "GRAV": 9.806,
            "DRATIO": 0.05,
            "STR": {"SPEC_CODE": "KDS(41-17-00:2019)"},
            "OPT": {"SC_": 2, "iSEISZONE": 0},
            "VAL": {
                "aSRA": [0.22, 0.154],
                "aSCP": [1.0, 1.5],
                "PERIOD": 4.0,
                "IE": 1.2,
                "R_": 5.0,
                "ZONEFACTOR": 0.22
            }
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/SPFC", json=payload_kds, headers=HEADERS)
print("KDS SPFC POST:", resp.status_code)

# ── 3) 전체 조회 ─────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/SPFC", headers=HEADERS)
print("SPFC GET:", resp.status_code, resp.json())

# ── 4) 특정 ID 삭제 ──────────────────────────────────────────────────────────
resp = requests.delete(f"{BASE_URL}/db/SPFC/1", headers=HEADERS)
print("SPFC DELETE/1:", resp.status_code)
```

---

## 2. /db/SPLC – Response Spectrum Load Cases

응답 스펙트럼 하중 케이스를 정의합니다.

### 2-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/SPLC` | 전체 조회 |
| `GET` | `{base_url}/db/SPLC/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/SPLC` | 생성 |
| `PUT` | `{base_url}/db/SPLC` | 전체 수정 |
| `PUT` | `{base_url}/db/SPLC/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/SPLC` | 전체 삭제 |
| `DELETE` | `{base_url}/db/SPLC/{id}` | 특정 ID 삭제 |

### 2-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 하중 케이스명 | `NAME` | String | - | Required |
| 2 | 설명 | `DESC` | String | Blank | Optional |
| 3 | 방향 (`"XY"` 또는 `"Z"`) | `DIR` | String | `"XY"` | Optional |
| 4 | 가진 각도 | `ANGLE` | Number | 0 | Optional |
| 5 | 스케일 계수 | `SCALE` | Number | - | Required |
| 6 | 주기 수정 계수 | `PMFT` | Number | - | Required |
| 7 | 스펙트럼 함수명 목록 | `aFUNCNAME` | Array[String] | - | Required |
| 8 | 스펙트럼 데이터 보간 방법 (`"LINEAR"` / `"LOG"`) | `INTERP` | String | `"LINEAR"` | Optional |
| 9 | 모드 조합 방법 (`"SRSS"` / `"CQC"` / `"ABS"` / `"Linear"`) | `COMTYPE` | String | `"CQC"` | Optional |
| 10 | 결과에 부호 추가 | `bADDSIGN` | Boolean | false | Optional |
| 11 | 부호 추가 방법 (0=주모드방향, 1=절대최대값방향) | `iSIGNTYPE` | Integer | 1 | Optional |
| 12 | 모드 형상 선택 | `bMODE` | Boolean | - | Optional |
| 13 | 사용 모드 목록 | `aUSEMODE` | Array[Object] | - | Optional |
| (1) | 모드 사용 여부 | `bUSE` | Boolean | - | Optional |
| (2) | 모드 형상 계수 | `MSFACTOR` | Number | - | Optional |
| 14 | 감쇠 방법 적용 여부 | `bDAMP` | Boolean | false | Optional |
| 15 | 감쇠비 보정 여부 | `bCDAMP` | Boolean | false | Optional |
| 16 | 감쇠 방법 (1=Modal, 2=Mass&Stiff, 3=StrainEnergy) | `iMDTYPE` | Integer | - | Required (bDAMP=true 시) |

**Modal 감쇠 추가 파라미터**

| 설명 | Key | Value Type |
|------|-----|------------|
| 전체 모드 감쇠비 | `DALL` | Number |
| 모드별 감쇠비 목록 | `aDAMPING` | Array[Object] |
| - 모드 번호 | `iMODE` | Integer |
| - 감쇠비 | `DAMPING` | Number |

**Mass & Stiffness Proportional 감쇠 추가 파라미터**

| 설명 | Key | Value Type | 비고 |
|------|-----|------------|------|
| 감쇠 유형 (1=직접 지정, 2=모달 감쇠로부터 계산) | `iCOEF` | Integer | Required |
| 질량 비례 여부 | `bMASSP` | Boolean | - |
| 강성 비례 여부 | `bSTIFFP` | Boolean | - |
| 질량 비례 계수 (iCOEF=1) | `MASSC` | Number | - |
| 강성 비례 계수 (iCOEF=1) | `STIFFC` | Number | - |
| 계산 방법 (1=주파수, 2=주기) | `iCALC` | Integer | iCOEF=2 시 |
| 모드1 주파수/주기 | `FP1` | Number | iCOEF=2 시 |
| 모드2 주파수/주기 | `FP2` | Number | iCOEF=2 시 |
| 모드1 감쇠비 | `DR1` | Number | iCOEF=2 시 |
| 모드2 감쇠비 | `DR2` | Number | iCOEF=2 시 |

**우발 편심(Accidental Eccentricity) 파라미터** *(GEN NX only)*

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 24 | 우발 편심 적용 | `bACCECC` | Boolean | false | Optional |
| 25 | 편심 데이터 (true=자동, false=사용자 정의) | `bACCECC_AUTO` | Boolean | - | Required |
| 26 | 편심 비율 | `ACCECC_PERCENT` | Number | - | Required |
| 27 | GL 이하 편심 고려 여부 | `bACCECC_CONSIDER_GL` | Boolean | - | Required |
| 28 | 최소 우발 비틀림 모멘트 제한 | `bACCECC_MINIMUM_TORSION` | Boolean | - | Required |
| 29 | 편심 목록 | `aACCECC_ECCEN_LIST` | Array[Object] | - | Required |
| (1) | 층 이름 | `STORY` | String | - | Required |
| (2) | Cross 방향 위치 | `CROSS` | Number | - | Required |
| (3) | Along 방향 위치 | `ALONG` | Number | - | Required |

> ⚠️ 2026-08-25 확인: 원문 Specifications 표는 `ACCECC_PERTCENT`(오타, 스키마는 `ACCECC_PERCENT`)와
> 28번 Key를 27번과 동일한 `bACCECC_CONSIDER_GL`로 중복 오기(스키마는 `bACCECC_MINIMUM_TORSION`)
> 하고 있음. 이 4개 필드는 원문 Request 예제에 등장하지 않아 표와 대조할 예제가 없으므로,
> CLAUDE.md 원칙에 따라 JSON Schema를 근거로 정정(원문
> [Response Spectrum Load Cases](https://support.midasuser.com/hc/en-us/articles/35963719599641)).

**비소산 요소 설계 파라미터** *(GEN NX only)*

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 30 | 비소산 요소 설계 | `bNDP` | Boolean | false | Optional |
| (1) | 비소산 계수 | `NDP` | Number | - | Required |

### 2-3. Request Body 예시

**기본 (감쇠 없음)**

```json
{
  "Assign": {
    "1": {
      "NAME": "LC_RS_XY",
      "DIR": "XY",
      "ANGLE": 0,
      "SCALE": 1,
      "PMFT": 1,
      "bDAMP": false,
      "INTERP": "LOG",
      "COMTYPE": "CQC",
      "bADDSIGN": true,
      "iSIGNTYPE": 0,
      "bMODE": true,
      "aFUNCNAME": ["RS_func"],
      "aUSEMODE": [
        {"bUSE": true, "MSFACTOR": 1},
        {"bUSE": true, "MSFACTOR": 1},
        {"bUSE": true, "MSFACTOR": 1}
      ]
    }
  }
}
```

**Modal 감쇠 적용**

```json
{
  "Assign": {
    "2": {
      "NAME": "LC_RS_Modal_Damp",
      "DIR": "XY",
      "ANGLE": 0,
      "SCALE": 1,
      "PMFT": 1,
      "bDAMP": true,
      "INTERP": "LOG",
      "COMTYPE": "CQC",
      "bADDSIGN": true,
      "iSIGNTYPE": 0,
      "bMODE": true,
      "aFUNCNAME": ["RS_func"],
      "aUSEMODE": [
        {"bUSE": true, "MSFACTOR": 1},
        {"bUSE": true, "MSFACTOR": 1}
      ],
      "bCDAMP": true,
      "iMDTYPE": 1,
      "DALL": 0.05,
      "aDAMPING": [
        {"iMODE": 1, "DAMPING": 0.06},
        {"iMODE": 2, "DAMPING": 0.07}
      ]
    }
  }
}
```

**Mass & Stiffness Proportional 감쇠 (직접 지정)**

```json
{
  "Assign": {
    "3": {
      "NAME": "LC_RS_M_S_Direct",
      "DIR": "XY",
      "ANGLE": 0,
      "SCALE": 1,
      "PMFT": 1,
      "bDAMP": true,
      "INTERP": "LOG",
      "COMTYPE": "CQC",
      "bADDSIGN": true,
      "iSIGNTYPE": 0,
      "bMODE": true,
      "aFUNCNAME": ["RS_func"],
      "aUSEMODE": [{"bUSE": true, "MSFACTOR": 1}],
      "bCDAMP": false,
      "iMDTYPE": 2,
      "iCOEF": 1,
      "bMASSP": true,
      "MASSC": 1.1,
      "bSTIFFP": true,
      "STIFFC": 1.2
    }
  }
}
```

**Mass & Stiffness Proportional 감쇠 (모달 감쇠로부터 계산)**

```json
{
  "Assign": {
    "4": {
      "NAME": "LC_RS_M_S_Calc",
      "DIR": "Z",
      "ANGLE": 0,
      "SCALE": 1,
      "PMFT": 1,
      "bDAMP": true,
      "INTERP": "LOG",
      "COMTYPE": "CQC",
      "bADDSIGN": true,
      "iSIGNTYPE": 0,
      "bMODE": true,
      "aFUNCNAME": ["RS_func"],
      "aUSEMODE": [{"bUSE": true, "MSFACTOR": 1}],
      "bCDAMP": false,
      "iMDTYPE": 2,
      "iCOEF": 2,
      "bMASSP": true,
      "bSTIFFP": true,
      "iCALC": 1,
      "FP1": 0.6,
      "FP2": 0.7,
      "DR1": 0.05,
      "DR2": 0.06
    }
  }
}
```

### 2-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 응답 스펙트럼 하중 케이스 생성 ──────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "RS_EQ_X",
            "DIR": "XY",
            "ANGLE": 0.0,
            "SCALE": 1.0,
            "PMFT": 1.0,
            "bDAMP": True,
            "INTERP": "LOG",
            "COMTYPE": "CQC",
            "bADDSIGN": True,
            "iSIGNTYPE": 0,
            "bMODE": True,
            "aFUNCNAME": ["RS_KDS2019"],
            "aUSEMODE": [
                {"bUSE": True, "MSFACTOR": 1},
                {"bUSE": True, "MSFACTOR": 1},
                {"bUSE": True, "MSFACTOR": 1}
            ],
            "bCDAMP": True,
            "iMDTYPE": 1,      # Modal 감쇠
            "DALL": 0.05,
            "aDAMPING": []
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/SPLC", json=payload, headers=HEADERS)
print("SPLC POST:", resp.status_code)

# ── 전체 조회 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/SPLC", headers=HEADERS)
print("SPLC GET:", resp.json())

# ── 특정 ID 수정 ─────────────────────────────────────────────────────────────
payload["Assign"]["1"]["SCALE"] = 1.2
resp = requests.put(f"{BASE_URL}/db/SPLC/1", json=payload, headers=HEADERS)
print("SPLC PUT/1:", resp.status_code)
```

---

## 3. /db/THGC – Time History Global Control

시간이력 해석 전역 제어 파라미터를 정의합니다.

> **CIVIL NX 전용** (GEN NX에서는 사용 불가)

### 3-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/THGC` | 전역 제어 조회 |
| `POST` | `{base_url}/db/THGC` | 전역 제어 생성 |
| `PUT` | `{base_url}/db/THGC` | 전역 제어 수정 |
| `DELETE` | `{base_url}/db/THGC` | 전역 제어 삭제 |

### 3-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 기하 비선형 타입 (0=None, 1=Large Disp, 2=P-Delta) | `GNT` | Integer | - | Required |
| 2 | 초기 하중 유형 (0=비선형 정적 해석, 1=정적/시공단계 결과 가져오기) | `ILT` | Integer | 0 | Required |
| 3 | 초기 하중 목록 | `aILL` | Array[Object] | [] | Optional |
| (1) | 정적 하중 케이스명 | `SLC` | String | - | Required |
| (2) | 스케일 계수 | `SF` | Real | - | Required |
| (3) | 하중 케이스 타입 (1=Static, 18=Construction) | `LCT` | Integer | - | Required |
| 4 | NL 초기 하중 무시 요소 옵션 | `IEPI` | Boolean | true | Optional |
| 5 | 증분 스텝 수 | `NSTEP` | Integer | 1 | Optional |
| 6 | 결과 출력 방법 (false=최종 스텝만, true=스텝 증분) | `bROT` | Boolean | false | Optional |
| 7 | 출력 스텝 증분 수 | `SNIO` | Integer | 1 | Optional |
| 8 | 수렴 실패 허용 | `bPCF` | Boolean | true | Required |
| 9 | 최대 부분 스텝 수 | `MAXNS` | Integer | 10 | Required |
| 10 | 최대 반복 횟수 | `MAXIT` | Integer | 10 | Required |
| 11 | 변위 노름 사용 | `bDN` | Boolean | true | Optional |
| 12 | 하중 노름 사용 | `bFN` | Boolean | false | Optional |
| 13 | 에너지 노름 사용 | `bEN` | Boolean | false | Optional |
| 14 | 변위 노름 값 | `DN` | Real | 0.001 | Optional |
| 15 | 하중 노름 값 | `FN` | Real | 0 | Optional |
| 16 | 에너지 노름 값 | `EN` | Real | 0 | Optional |
| 17 | 선형 탐색 방법 사용 | `bULSM` | Boolean | false | Optional |
| 18 | 선형 탐색 시작 반복 수 | `ULSM` | Integer | 5 | Optional |
| 19 | 시간이력 에너지 결과 출력 | `ENERGYRESULT` | Boolean | true | Optional |
| 20 | 점성 감쇠기 / 오일 감쇠기 결과 | `SDVI` | Boolean | true | Optional |
| 21 | 점탄성 감쇠기 결과 | `SDVE` | Boolean | true | Optional |
| 22 | 강재 감쇠기 결과 | `SDST` | Boolean | true | Optional |
| 23 | 이력 절연 장치 결과 | `SDHY` | Boolean | true | Optional |
| 24 | 절연 장치 결과 | `SDIS` | Boolean | true | Optional |
| 25 | 모델 항복 상태 | `bMSSSTATUS` | Boolean | true | Optional |

### 3-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "GNT": 0,
      "ILT": 0,
      "aILL": [
        {"SLC": "Pretension",   "SF": 1.0, "LCT": 1},
        {"SLC": "EarthPressure","SF": 1.2, "LCT": 1}
      ],
      "IEPI": true,
      "NSTEP": 1,
      "bROT": false,
      "SNIO": 1,
      "bPCF": true,
      "MAXNS": 10,
      "MAXIT": 10,
      "bDN": true,
      "bFN": false,
      "bEN": false,
      "DN": 0.001,
      "FN": 0.001,
      "EN": 0.001,
      "bULSM": false,
      "ULSM": 5,
      "ENERGYRESULT": false,
      "SDVI": false,
      "SDVE": false,
      "SDST": false,
      "SDHY": false,
      "SDIS": false,
      "bMSSSTATUS": false
    }
  }
}
```

### 3-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 시간이력 전역 제어 생성 ──────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "GNT": 0,           # 기하 비선형 없음
            "ILT": 0,           # 비선형 정적 해석으로 초기 하중 처리
            "aILL": [
                {"SLC": "DL", "SF": 1.0, "LCT": 1}
            ],
            "IEPI": True,
            "NSTEP": 1,
            "bROT": False,
            "SNIO": 1,
            "bPCF": True,
            "MAXNS": 10,
            "MAXIT": 30,
            "bDN": True,
            "bFN": True,
            "bEN": False,
            "DN": 0.001,
            "FN": 0.001,
            "EN": 0.001,
            "bULSM": True,
            "ULSM": 5,
            "ENERGYRESULT": True,
            "SDVI": True,
            "SDVE": True,
            "SDST": True,
            "SDHY": True,
            "SDIS": True,
            "bMSSSTATUS": True
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THGC", json=payload, headers=HEADERS)
print("THGC POST:", resp.status_code)
```

---

## 4. /db/THGC-M1 – Time History Global Control (Hyper-S)

Hyper-S 비선형 시간이력 전역 제어를 정의합니다.

> **CIVIL NX 전용** (GEN NX에서는 사용 불가)

### 4-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/THGC-M1` | 조회 |
| `PUT` | `{base_url}/db/THGC-M1` | 수정 |
| `DELETE` | `{base_url}/db/THGC-M1` | 삭제 |

### 4-2. 파라미터

**메인 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 기하 비선형 타입 (0=None, 1=Large Disp, 2=P-Delta) | `GEO_NONL_TYPE` | Integer(enum) | - | Required |
| 2 | 초기 하중 유형 (0=비선형 정적 해석, 0=정적/시공단계 결과 가져오기) | `INIT_LOAD_TYPE` | Integer(enum) | - | Required |
| 3 | 초기 하중 목록 | `INIT_LOAD_LIST` | Array[Object] | - | Optional |
| (1) | 하중 케이스명 | `LC_NAME` | String | - | Required |
| (2) | 스케일 계수 | `SF` | Number | - | Required |
| (3) | 하중 케이스 타입 | `LC_TYPE` | String | - | Required |
| 4 | 초기 하중 케이스 증분 스텝 | `INCREMENT_STEP` | Object | - | Optional |
| 5 | 반복 파라미터 | `ITER_PARAM` | Object | - | Required |
| 6 | NL 해석 초기 하중 요소 무시 여부 | `IGNORE_ELEM` | Boolean | false | Optional |
| 7 | 적용 변위 기준 (0=미변형, 1=변형) | `SEQ_LOAD_TYPE` | Integer(enum) | 1 | Optional |
| 8 | 비탄성 힌지 데이터 옵션 | `HINGE_OPT` | Object | - | Optional |

**INCREMENT_STEP 서브 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 증분 스텝 수 | `NSTEP` | Integer | 1 | Optional |
| 결과 출력 타입 (0=최종 스텝만, 1=스텝 증분) | `OUT_TYPE` | Integer(enum) | 0 | Optional |
| 스텝 증분 수 (OUT_TYPE=1 시) | `STEP_INC` | Integer | 1 | Required |

**ITER_PARAM 서브 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| 수렴 실패 허용 | `PERMIT_FAIL` | Boolean | true | Optional |
| 최대 반복 횟수 | `MAX_ITER` | Integer | - | Required |
| 수렴 판정 기준 (NORM_CTRL) | `NORM_CTRL` | Object | - | Optional |
| - 변위 노름 | `DISP` → `{OPT_USE, VALUE}` | Object | - | Optional |
| - 하중 노름 | `FORCE` → `{OPT_USE, VALUE}` | Object | - | Optional |
| - 에너지 노름 | `ENERGY` → `{OPT_USE, VALUE}` | Object | - | Optional |
| 강성 업데이트 방식 (0=Custom, 1=FullNR, 2=InitStiff) | `STIFF_UPD_SCHEME` | Integer(enum) | 1 | Optional |
| 강성 업데이트 전 반복 횟수 (STIFF_UPD_SCHEME=0 시) | `ITER_BEF_UPDATE` | Integer | 5 | Required |
| 최대 이분법 수준 | `MAX_BISECT_LEVEL` | Integer | 5 | Optional |
| 스마트 이분법 | `SMART_BISECT` | Boolean | false | Optional |
| 발산 임계값 | `DIVERGENCE_THRESHOLD` | Number | 3 | Optional |
| 선형 탐색 옵션 (LINE_SEARCH) | `LINE_SEARCH` | Object | - | Optional |
| - 선형 탐색 사용 여부 | `OPT_USE` | Boolean | true | Required |
| - 선형 탐색 옵션 (0=자동, 1=사용자 정의) | `LINE_SEARCH_OPT` | Integer(enum) | 0 | Required |
| - 선형 탐색 시작 반복 번호 | `START_ITER_NO` | Integer | - | Required |
| - 최대 선형 탐색 반복 횟수 | `MAX_LINE_SEARCH_ITER` | Integer | - | Required |
| - 선형 탐색 허용오차 | `LINE_SEARCH_TOL` | Number | - | Required |

**HINGE_OPT 서브 파라미터**

| 설명 | Key | Value Type | Default | Required |
|------|-----|------------|---------|----------|
| Point Spring Support (0=비선형 특성 적용, 1=선형으로 간주) | `PSPRING_SUP` | Integer(enum) | 0 | Optional |
| Elastic Link (0=비선형 특성 적용, 1=선형으로 간주) | `EL` | Integer(enum) | 1 | Optional |

> ⚠️ 2026-08-25 확인: 이전 문서는 `PSPRING_SUP`을 "P-스프링 지점 처리", `EL`을 "요소 데이터"로만
> 표기해 실제 의미(둘 다 0/1 enum — 비선형 특성 적용 여부)와 기본값이 누락돼 있었음. 원문
> [Time History Global Control (THGC-M1)](https://support.midasuser.com/hc/en-us/articles/56510942223513)
> 기준으로 정정.

### 4-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "GEO_NONL_TYPE": 1,
      "INIT_LOAD_TYPE": 0,
      "INIT_LOAD_LIST": [
        {"LC_NAME": "DL", "SF": 0.75, "LC_TYPE": "ST"}
      ],
      "INCREMENT_STEP": {
        "NSTEP": 10,
        "OUT_TYPE": 1,
        "STEP_INC": 1
      },
      "ITER_PARAM": {
        "PERMIT_FAIL": true,
        "MAX_ITER": 30,
        "NORM_CTRL": {
          "DISP":   {"OPT_USE": true, "VALUE": 0.001},
          "FORCE":  {"OPT_USE": true, "VALUE": 0.001},
          "ENERGY": {"OPT_USE": true, "VALUE": 0.001}
        },
        "STIFF_UPD_SCHEME": 0,
        "ITER_BEF_UPDATE": 5,
        "MAX_BISECT_LEVEL": 5,
        "SMART_BISECT": false,
        "DIVERGENCE_THRESHOLD": 3,
        "LINE_SEARCH": {
          "OPT_USE": true,
          "LINE_SEARCH_OPT": 1,
          "START_ITER_NO": 3,
          "MAX_LINE_SEARCH_ITER": 4,
          "LINE_SEARCH_TOL": 0.5
        }
      },
      "IGNORE_ELEM": false,
      "SEQ_LOAD_TYPE": 1,
      "HINGE_OPT": {
        "PSPRING_SUP": 0,
        "EL": 1
      }
    }
  }
}
```

### 4-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── Hyper-S 시간이력 전역 제어 수정 ─────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "GEO_NONL_TYPE": 1,
            "INIT_LOAD_TYPE": 0,
            "INIT_LOAD_LIST": [
                {"LC_NAME": "DL", "SF": 1.0, "LC_TYPE": "ST"}
            ],
            "INCREMENT_STEP": {
                "NSTEP": 10,
                "OUT_TYPE": 1,
                "STEP_INC": 1
            },
            "ITER_PARAM": {
                "PERMIT_FAIL": True,
                "MAX_ITER": 30,
                "NORM_CTRL": {
                    "DISP": {"OPT_USE": True, "VALUE": 0.001}
                },
                "STIFF_UPD_SCHEME": 1,
                "MAX_BISECT_LEVEL": 5,
                "SMART_BISECT": False,
                "DIVERGENCE_THRESHOLD": 3,
                "LINE_SEARCH": {
                    "OPT_USE": False
                }
            },
            "IGNORE_ELEM": False,
            "SEQ_LOAD_TYPE": 1
        }
    }
}

resp = requests.put(f"{BASE_URL}/db/THGC-M1", json=payload, headers=HEADERS)
print("THGC-M1 PUT:", resp.status_code)
```

---

## 5. /db/THOO-M1 – Time History Output Option (Hyper-S)

Hyper-S 비선형 시간이력 출력 옵션을 정의합니다.

> **CIVIL NX 전용** (GEN NX에서는 사용 불가)

### 5-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/THOO-M1` | 조회 |
| `PUT` | `{base_url}/db/THOO-M1` | 수정 |
| `DELETE` | `{base_url}/db/THOO-M1` | 삭제 |

### 5-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 비선형 해석 결과 출력 옵션 | `OUT_OPT` | Object | - | Required |
| (1) | 비탄성 힌지 스텝별 출력 옵션 (0=전체 요소, 1=선택 요소, 2=미출력) | `HINGE_OUT` | Integer(enum) | - | Required |
| (2) | 공통 설정 여부 (true=FIBER_OUT이 HINGE_OUT과 동일) | `COMMON_OPT` | Boolean | - | Required |
| (3) | 섬유 단면 스텝별 출력 옵션 (0=전체 요소, 1=선택 요소, 2=미출력) | `FIBER_OUT` | Integer(enum) | - | Required (COMMON_OPT=false 시) |
| 2 | 시간이력 결과 옵션 | `RESULT_SELECTION` | Object | - | Required |
| (1) | 에너지 결과 출력 | `ENERGY_RESULT` | Boolean | true | Optional |
| (2) | 점성 감쇠기 / 오일 감쇠기 결과 | `SDVI` | Boolean | true | Optional |
| (3) | 점탄성 감쇠기 결과 | `SDVE` | Boolean | true | Optional |
| (4) | 강재 감쇠기 결과 | `SDST` | Boolean | true | Optional |
| (5) | 이력 절연 장치 결과 | `SDHY` | Boolean | true | Optional |
| (6) | 절연 장치 결과 | `SDIS` | Boolean | true | Optional |

### 5-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "OUT_OPT": {
        "HINGE_OUT": 1,
        "COMMON_OPT": false,
        "FIBER_OUT": 1
      },
      "RESULT_SELECTION": {
        "ENERGY_RESULT": true,
        "SDVI": true,
        "SDVE": true,
        "SDST": true,
        "SDHY": true,
        "SDIS": true
      }
    }
  }
}
```

### 5-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── Hyper-S 출력 옵션 수정 ───────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "OUT_OPT": {
                "HINGE_OUT": 0,    # 전체 비탄성 요소 출력
                "COMMON_OPT": True  # FIBER_OUT = HINGE_OUT 동일
            },
            "RESULT_SELECTION": {
                "ENERGY_RESULT": True,
                "SDVI": True,
                "SDVE": False,
                "SDST": False,
                "SDHY": True,
                "SDIS": True
            }
        }
    }
}

resp = requests.put(f"{BASE_URL}/db/THOO-M1", json=payload, headers=HEADERS)
print("THOO-M1 PUT:", resp.status_code)
```

---

## 6. /db/THIS – Time History Load Cases

시간이력 하중 케이스를 정의합니다.  
`COMMON.iATYPE` (Linear/Nonlinear) × `COMMON.iAMETHOD` (Modal/Direct/Static) 조합에 따라 서로 다른 추가 파라미터가 필요합니다.

### 6-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/THIS` | 전체 조회 |
| `GET` | `{base_url}/db/THIS/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/THIS` | 생성 |
| `PUT` | `{base_url}/db/THIS` | 전체 수정 |
| `PUT` | `{base_url}/db/THIS/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/THIS` | 전체 삭제 |
| `DELETE` | `{base_url}/db/THIS/{id}` | 특정 ID 삭제 |

### 6-2. COMMON 공통 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 공통 설정 오브젝트 | `COMMON` | Object | - | Required |
| (1) | 하중 케이스명 | `NAME` | String | - | Required |
| (2) | 설명 | `DESC` | String | Blank | Optional |
| (3) | 해석 타입 (1=Linear, 2=Nonlinear) | `iATYPE` | Integer | - | Required |
| (4) | 해석 방법 (1=Modal, 2=Direct Integration, 3=Static) | `iAMETHOD` | Integer | - | Required |
| (5) | 시간이력 타입 (1=Transient, 2=Periodic) | `iTHTYPE` | Integer | - | Required |

### 6-3. Linear + Modal (Transient / Periodic)

COMMON 추가 파라미터:

| 설명 | Key | Value Type | Required |
|------|-----|------------|----------|
| 종료 시간 | `ENDTIME` | Number | Required |
| 시간 증분 | `INC` | Number | Required |
| 출력 스텝 증분 수 | `iOUT` | Integer | Required |
| 하중 적용 방법 (`"ORDER"`) | `INITMETHOD` | String | Required |
| 감쇠 방법 (1=Modal, 2=M&S, 3=StrainEnergy) | `iMDTYPE` | Integer | Required |

**ORDER 방법 사용 시 순차 하중 파라미터**

| 설명 | Key | Value Type | Required |
|------|-----|------------|----------|
| 후속 하중 옵션 사용 여부 | `bSUBSEQ` | Boolean | Optional |
| 후속 하중 타입 (0=하중케이스, 1=초기요소력) | `SUBSEQ` | Integer | Optional |
| 하중 케이스 타입 (`"ST"` / `"CS"` / `"TH"`) | `LCTYPE` | String | Optional |
| 하중 케이스명 | `CASE` | String | Optional |

**INIT 방법 사용 시 파라미터**

| 설명 | Key | Value Type | Required |
|------|-----|------------|----------|
| 초기 하중 사용 여부 (0=사용, 1=미사용) | `INITLOAD` | Integer | Optional |
| D/V/A 결과 누적 | `bDVA` | Boolean | Optional |
| 최종 스텝 하중 유지 | `bKEEP` | Boolean | Optional |

### 6-4. Linear + Direct Integration (Transient)

COMMON 추가 파라미터: `ENDTIME`, `INC`, `iOUT`, `INITMETHOD`, `iMDTYPE`

추가 파라미터:

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 2 | Newmark 방법 타입 (1=Constant Accel, 2=Linear Accel, 3=User Input) | `iNMM` | Integer | - | Required |
| 3 | Gamma 값 (User Input 시) | `GAMMA` | Number | 0.5 | Optional |
| 4 | Beta 값 (User Input 시) | `BETA` | Number | 0.25 | Optional |

### 6-5. Nonlinear + Modal (Transient)

COMMON 추가 파라미터: `ENDTIME`, `INC`, `iOUT`, `INITMETHOD`, `iMDTYPE`

추가 파라미터: 아래 [6-8. 반복 제어 파라미터](#6-8-반복-제어-파라미터-nonlinear-공통) 공통 필드 +

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 2 | 최소 스텝 크기 | `MINSSS` | Number | - | Required |

### 6-6. Nonlinear + Direct Integration (Transient)

COMMON 추가 파라미터: `ENDTIME`, `INC`, `iOUT`, `iGEOM`, `INITMETHOD`, `iMDTYPE`(1=Modal,
2=Mass & Stiffness Proportional, 3=Strain Energy Proportional, **4=Element Mass & Stiffness
Proportional** — ⚠️ 4번째 값이 이전 문서에 누락돼 있었음)

추가 파라미터:

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 2 | Newmark 방법 타입 (1=Constant Accel, 2=Linear Accel, 3=User Input) | `iNMM` | Integer | - | Required |
| 3 | Gamma 값 | `GAMMA` | Number | 0.5 | Optional |
| 4 | Beta 값 | `BETA` | Number | 0.25 | Optional |
| 5 | 반복 수행 여부 | `bITER` | Boolean | true | Optional |
| 6 | 감쇠 매트릭스 업데이트 여부 (Modal·Strain Energy: 미사용 / M&S·Element M&S: 사용) | `DMUPDATE` | Boolean | false | Optional |

추가 파라미터(아래 [6-8. 반복 제어 파라미터](#6-8-반복-제어-파라미터-nonlinear-공통) 공통 필드 +):

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| A | 수렴 실패 허용 | `bCONV` | Boolean | true | Optional |
| B | 최소 스텝 크기 | `MINSSS` | Number | - | Required |
| C | 에너지 노름 사용 | `bEN` | Boolean | false | Optional |
| D | 에너지 노름 값(bEN=true 시) | `EN` | Number | 0.001 | Optional |

### 6-7. Nonlinear + Static

COMMON 추가 파라미터: `ENDTIME`, `iISTEP` (증분 스텝), `iOUT`, `iGEOM`, `INITMETHOD`

추가 파라미터:

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 2 | 누적 하중 증분 이력 출력 | `bCUMULATE` | Boolean | false | Optional |
| 3 | 반복 수행 여부 | `bITER` | Boolean | true | Optional |
| 4 | 증분 방법 (0=하중 제어, 1=변위 제어) | `iINCCTRL` | Integer | 0 | Optional |

**증분 방법(iINCCTRL) 세부 파라미터**

> ⚠️ 2026-08-25 확인: 이전 문서는 `iINCCTRL` 옵션만 소개하고 각 방식(하중 제어/변위 제어)의
> 실제 하위 필드가 전혀 문서화돼 있지 않았음.

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| Load Control (iINCCTRL=0) | | | | | |
| (1) | Scale Factor | `SCALE` | Number | 1 | Required |
| Displacement Control (iINCCTRL=1) | | | | | |
| (1) | Displacement Control Option (0=Global Control, 1=Master Node Control) | `iCTRL` | Integer | - | Required |
| (2) | Displacement (Global: 최대 병진 변위 / Master Node: 최대 변위) | `TINC` | Number | - | Required |
| (3) | Master Node No. (iCTRL=1일 때) | `MNODE` | Integer | - | Required |
| (4) | Master Direction (1=DX, 2=DY, 3=DZ, iCTRL=1일 때) | `MDIR` | Integer | - | Required |

추가 파라미터(아래 [6-8. 반복 제어 파라미터](#6-8-반복-제어-파라미터-nonlinear-공통) 공통 필드 +):

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| A | 수렴 실패 허용 | `bCONV` | Boolean | true | Optional |
| B | 최대 부분 스텝 수 | `iMSTEP` | Integer | - | Required |
| C | 에너지 노름 사용 | `bEN` | Boolean | false | Optional |
| D | 에너지 노름 값(bEN=true 시) | `EN` | Number | 0.001 | Optional |

### 6-8. 반복 제어 파라미터 (Nonlinear 공통)

> ⚠️ 2026-08-25 확인: Nonlinear + Modal/Direct Integration/Static 3개 모드 모두에 적용되는
> 공통 반복 제어 필드(`iMAXITER`~`dTOL`)가 이전 문서에 전혀 없었음. 원문
> [Time History Load Cases](https://support.midasuser.com/hc/en-us/articles/35963903917593)의
> "Iteration Control for Nonlinear Type" 각주 기준으로 보강.

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 최대 반복 횟수 | `iMAXITER` | Integer | - | Required |
| 2 | 변위 노름 사용 | `bDN` | Boolean | true | Optional |
| 3 | 변위 노름 값(bDN=true 시) | `DN` | Number | 0.001 | Optional |
| 4 | 하중 노름 사용 | `bFN` | Boolean | false | Optional |
| 5 | 하중 노름 값(bFN=true 시) | `FN` | Number | 0.001 | Optional |
| 6 | 선형 탐색 방법 사용 | `bULSM` | Boolean | false | Optional |
| 7 | 선형 탐색 시작 반복 수(bULSM=true 시) | `ULSM` | Integer | 5 | Optional |
| 8 | Runge-Kutta 방법 (0=Fehlberg, 1=Cash-Karp) | `iRKM` | Integer | 0 | Optional |
| 9 | 허용 오차 | `dTOL` | Number | 1e-08 | Optional |

이 표에 더해 Modal(6-5)은 `MINSSS`, Direct Integration(6-6)은 `bCONV`/`MINSSS`/`bEN`/`EN`,
Static(6-7)은 `bCONV`/`iMSTEP`/`bEN`/`EN`이 각각 모드별로 추가된다.

### 6-9. 감쇠 파라미터

**Modal 감쇠 (iMDTYPE=1)**

| 설명 | Key | Value Type |
|------|-----|------------|
| 전체 모드 감쇠비 | `DALL` | Number |
| 모드별 감쇠비 오버라이드 목록 | `aDAMP` | Array[Object] |
| - 모드 번호 | `iMODE` | Integer |
| - 감쇠비 | `DAMPING` | Number |

> ⚠️ 2026-08-25 확인: 이전 문서는 Key를 `aMDAMPING`으로 잘못 기재하고 있었음(원문 스키마·모든
> Request 예제 모두 `aDAMP`). 실제 API 호출 시 필드가 무시될 수 있는 오류였음.

**Mass & Stiffness Proportional 감쇠 (iMDTYPE=2)**

> ⚠️ 2026-08-25 확인: 이 감쇠 방식의 하위 필드가 이전 문서(§6 THIS)에 전혀 문서화돼 있지
> 않았음(§2 SPLC의 동일 항목만 문서화돼 있었음).

| No. | 설명 | Key | Value Type | Required |
|-----|------|-----|------------|----------|
| 1 | 계수 산정 방식 (1=직접 지정, 2=모달 감쇠로부터 계산) | `iCOEF` | Integer | Required |
| iCOEF=1(직접 지정) | | | | |
| 2 | 질량 비례 사용 여부 | `bMASSP` | Boolean | Required |
| 3 | 질량 비례 계수(bMASSP=true 시) | `MASSC` | Number | Required |
| 4 | 강성 비례 사용 여부 | `bSTIFFP` | Boolean | Required |
| 5 | 강성 비례 계수(bSTIFFP=true 시) | `STIFFC` | Number | Required |
| iCOEF=2(모달 감쇠로부터 계산) | | | | |
| 2 | 계산 방법 (1=주파수, 2=주기) | `iCALC` | Integer | Required |
| 3 | 모드1 주파수/주기 | `FP1` | Number | Required |
| 4 | 모드1 감쇠비 | `DR1` | Number | Required |
| 5 | 모드2 주파수/주기 | `FP2` | Number | Required |
| 6 | 모드2 감쇠비 | `DR2` | Number | Required |

### 6-10. Request Body 예시

**Linear + Modal + Transient**

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "TH_Linear_Modal",
        "DESC": "선형 모달 시간이력",
        "iATYPE": 1,
        "iAMETHOD": 1,
        "iTHTYPE": 1,
        "ENDTIME": 30.0,
        "INC": 0.01,
        "iOUT": 1,
        "INITMETHOD": "INIT",
        "INITLOAD": 0,
        "bDVA": false,
        "bKEEP": false,
        "iMDTYPE": 1
      },
      "DALL": 0.05
    }
  }
}
```

**Nonlinear + Direct Integration + Transient**

```json
{
  "Assign": {
    "2": {
      "COMMON": {
        "NAME": "TH_NL_Direct",
        "DESC": "비선형 직접적분 시간이력",
        "iATYPE": 2,
        "iAMETHOD": 2,
        "iTHTYPE": 1,
        "ENDTIME": 20.0,
        "INC": 0.005,
        "iOUT": 2,
        "iGEOM": 0,
        "INITMETHOD": "INIT",
        "INITLOAD": 0,
        "bDVA": false,
        "bKEEP": false,
        "iMDTYPE": 2
      },
      "iNMM": 1,
      "bITER": true,
      "DMUPDATE": false
    }
  }
}
```

**Nonlinear + Static (Load Control)**

```json
{
  "Assign": {
    "3": {
      "COMMON": {
        "NAME": "TH_NL_Static",
        "DESC": "비선형 정적 시간이력",
        "iATYPE": 2,
        "iAMETHOD": 3,
        "ENDTIME": 10.0,
        "iISTEP": 100,
        "iOUT": 1,
        "iGEOM": 0,
        "INITMETHOD": "INIT"
      },
      "bCUMULATE": true,
      "iINCCTRL": 0,
      "SCALE": 1,
      "bITER": true,
      "bCONV": true,
      "iMSTEP": 10,
      "iMAXITER": 10,
      "bDN": true,
      "DN": 0.001,
      "bFN": true,
      "FN": 0.001,
      "bEN": true,
      "EN": 0.001,
      "iRKM": 0,
      "dTOL": 1e-08,
      "bULSM": true,
      "ULSM": 5
    }
  }
}
```

**Nonlinear + Static (Displacement Control – Master Node)**

```json
{
  "Assign": {
    "4": {
      "COMMON": {
        "NAME": "TH_NL_Static_Disp",
        "DESC": "",
        "iATYPE": 2,
        "iAMETHOD": 3,
        "iISTEP": 1,
        "iOUT": 1,
        "iGEOM": 0,
        "INITLOAD": 0,
        "INITMETHOD": "ORDER",
        "bSUBSEQ": true,
        "SUBSEQ": 1
      },
      "bCUMULATE": false,
      "iINCCTRL": 1,
      "iCTRL": 1,
      "TINC": 0.02,
      "MNODE": 1,
      "MDIR": 2,
      "bITER": true,
      "bCONV": true,
      "iMSTEP": 10,
      "iMAXITER": 10,
      "bDN": true,
      "DN": 0.001,
      "iRKM": 0,
      "dTOL": 1e-08,
      "bULSM": false,
      "ULSM": 5
    }
  }
}
```

### 6-11. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 1) Linear Modal Transient 생성 ────────────────────────────────────────────
payload_linear_modal = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "TH01_Linear_Modal",
                "iATYPE": 1,       # Linear
                "iAMETHOD": 1,     # Modal
                "iTHTYPE": 1,      # Transient
                "ENDTIME": 30.0,
                "INC": 0.01,
                "iOUT": 1,
                "INITMETHOD": "INIT",
                "INITLOAD": 0,
                "bDVA": False,
                "bKEEP": False,
                "iMDTYPE": 1       # Modal 감쇠
            },
            "DALL": 0.05
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THIS", json=payload_linear_modal, headers=HEADERS)
print("THIS POST (Linear Modal):", resp.status_code)

# ── 2) Nonlinear Direct Integration Transient 생성 ───────────────────────────
payload_nl_di = {
    "Assign": {
        "2": {
            "COMMON": {
                "NAME": "TH02_NL_DI",
                "iATYPE": 2,       # Nonlinear
                "iAMETHOD": 2,     # Direct Integration
                "iTHTYPE": 1,      # Transient
                "ENDTIME": 20.0,
                "INC": 0.005,
                "iOUT": 2,
                "iGEOM": 0,
                "INITMETHOD": "INIT",
                "INITLOAD": 0,
                "bDVA": False,
                "bKEEP": False,
                "iMDTYPE": 2       # Mass & Stiffness Proportional
            },
            "iNMM": 1,             # Constant Acceleration
            "bITER": True,
            "DMUPDATE": False
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THIS", json=payload_nl_di, headers=HEADERS)
print("THIS POST (NL DI):", resp.status_code)

# ── 3) 전체 조회 ─────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THIS", headers=HEADERS)
print("THIS GET:", resp.status_code)
```

---

## 7. /db/THIS-M1 – Time History Load Cases (Hyper-S)

Hyper-S 비선형 시간이력 하중 케이스를 정의합니다.  
기존 THIS와 달리 중첩 오브젝트 구조(ANAL_CASE, DAMPING, NONL_CTRL_PARAM)를 사용합니다.

> **CIVIL NX 전용** (GEN NX에서는 사용 불가)

### 7-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/THIS-M1` | 전체 조회 |
| `GET` | `{base_url}/db/THIS-M1/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/THIS-M1` | 생성 |
| `PUT` | `{base_url}/db/THIS-M1` | 전체 수정 |
| `PUT` | `{base_url}/db/THIS-M1/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/THIS-M1` | 전체 삭제 |
| `DELETE` | `{base_url}/db/THIS-M1/{id}` | 특정 ID 삭제 |

### 7-2. 파라미터

**공통 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 하중 케이스명 | `NAME` | String | - | Required |
| 2 | 설명 | `DESC` | String | - | Optional |
| 3 | 해석 케이스 옵션 | `ANAL_CASE` | Object | - | Required |
| (1) | 해석 타입 (0=Linear, 1=Nonlinear) | `ANAL_TYPE` | Integer(enum) | - | Required |
| (2) | 해석 방법 (0=Modal, 1=Direct Integration, **2=Static**) | `ANAL_METHOD` | Integer(enum) | - | Required |
| (3) | 시간이력 타입 (0=Transient, 1=Periodic) — Nonlinear+Direct Integration/Static은 Periodic 거부 | `TH_TYPE` | Integer(enum) | - | Optional |
| 3-a | 기하 비선형 타입 (0=None, 1=P-Delta, 2=Large Displacements, ANAL_TYPE=Nonlinear 시) | `GEOM_NL_TYPE` | Integer(enum) | 0 | Optional |
| 4 | 종료 시간 | `ENDTIME` | Number | - | Required |
| 5 | 시간 증분 | `TIME_INC` | Number | - | Required |
| 6 | 출력 스텝 증분 수 | `OUTPUT_STEP` | Integer | 1 | Required |
| 6-a | 증분 스텝 수 (Nonlinear+Static일 때 사실상 필수) | `INC_STEP` | Integer | 1 | Optional |
| 7 | 초기 하중 방법 (`"INIT"` / `"ORDER"`) | `INIT_METHOD` | String(enum) | - | Required |
| 8 | 초기 하중 사용 (INIT_METHOD=INIT 시) | `USE_INIT_LOAD` | Boolean | - | Required |
| 9 | D/V/A 결과 누적 (USE_INIT_LOAD=true 시) | `CUM_DVA` | Boolean | false | Required |
| 10 | 최종 스텝 하중 유지 | `KEEP_LOAD` | Boolean | false | Required |
| 11 | 후속 하중 옵션 (INIT_METHOD=ORDER 시) | `SUBSEQ` | Object | - | Required |
| (1) | 후속 하중 사용 | `OPT_USE` | Boolean | false | Optional |
| (2) | 후속 하중 타입 (0=하중케이스, 1=초기요소력, 2=기하강성초기력) | `SUBSEQ_LOAD` | Integer(enum) | - | Required |
| (3) | 하중 케이스 타입 (`"ST"` / `"CS"` / `"TH"`) | `LCTYPE` | String(enum) | - | Required |
| (4) | 하중 케이스명 | `CASE` | String | - | Required |
| 12 | 최종 스텝 가속도 유지 | `KEEP_ACC` | Boolean | false | Optional |
| 13 | 감쇠 설정 | `DAMPING` | Object | - | Required |
| (1) | 감쇠 방법 (0=Direct Modal, 1=M&S Proportional, 2=Strain Energy, 3=Element M&S — Modal+Element(3) 조합은 거부됨) | `DAMPING_METHOD` | Integer(enum) | - | Required |
| (2) | 전체 모드 감쇠비 (DAMPING_METHOD=0 시) | `ALL_DAMPING_RATIO` | Number | - | Required |
| (3) | 모드별 감쇠비 오버라이드 목록 | `MODAL_DAMPING_RATIO` | Array[Object] | - | Optional |
| - 모드 번호 | `MODE_NO` | Integer | - | Required |
| - 감쇠비 | `DAMPING` | Number | - | Required |
| 14 | 비선형 제어 파라미터 (ANAL_TYPE=1 시) | `NONL_CTRL_PARAM` | Object | - | Optional |
| (1) | 반복 수행 여부 | `PERFORM_ITER` | Boolean | - | Required |
| (2) | 반복 제어 파라미터 | `ITER_CTRL` | Object | - | Required |
| - 수렴 실패 허용 | `PERMIT_FAIL` | Boolean | - | - |
| - 최대 반복 횟수 | `MAX_ITER` | Integer | - | - |
| - 수렴 판정 기준 (NORM_CTRL) | `NORM_CTRL` | Object | - | - |
| - 강성 업데이트 방식 | `STIFF_UPD_SCHEME` | Integer | - | - |
| - 강성 업데이트 전 반복 횟수 (STIFF_UPD_SCHEME=0일 때만 지정 가능) | `ITER_BEF_UPDATE` | Integer | - | - |
| - 최대 이분법 수준 | `MAX_BISECT_LEVEL` | Integer | - | - |
| - 스마트 이분법 | `SMART_BISECT` | Boolean | - | - |
| - 발산 임계값 | `DIVERGENCE_THRESHOLD` | Number | - | - |
| - 선형 탐색 옵션 (LINE_SEARCH) | `LINE_SEARCH` | Object | - | - |
| (3) | 감쇠 매트릭스 업데이트 (0/1/2, DAMPING_METHOD가 M&S(1)/Element M&S(3)일 때만) | `DAMP_UPDATE` | Integer(enum) | - | Optional |

> ⚠️ 2026-08-25 확인: 이전 문서는 다음 3개를 완전히 누락하고 있었음(원문
> [Time History Load Cases (THIS-M1)](https://support.midasuser.com/hc/en-us/articles/56538335819673)
> 기준). ANAL_METHOD의 세 번째 값(Static=2, 단 Linear+Static 조합은 서버가 거부)이 스펙에서
> 통째로 빠져 있었고, `GEOM_NL_TYPE`은 스키마 설명 자체가 "Schema 값 1↔DB 값 2, Schema 값
> 2↔DB 값 1"로 저장 시 뒤바뀐다고 명시하고 있어 원문 그대로 옮겨 적었으니 실제 연동 전 재확인
> 권장. `DAMPING_METHOD=1`(M&S Proportional)의 세부 계수 입력 구조도 전혀 없었다.

**M&S Proportional 감쇠 세부 필드 (DAMPING_METHOD=1)**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 계수 산정 방식 (0=Direct Specification, 1=Calculate from Modal Damping) | `COEF_INPUT` | Integer(enum) | - | Required |
| COEF_INPUT=0 | | | | | |
| 2 | 질량 비례 사용 (USE_MASS/USE_STIFF 중 최소 1개는 true) | `USE_MASS` | Boolean | - | Optional |
| 3 | 질량 계수(Rm) | `MASS_VALUE` | Number | - | Optional |
| 4 | 강성 비례 사용 | `USE_STIFF` | Boolean | - | Optional |
| 5 | 강성 계수(Rk) | `STIFF_VALUE` | Number | - | Optional |
| COEF_INPUT=1 | | | | | |
| 2 | 계산 기준 (0=Frequency, 1=Period) | `COEF_CALC` | Integer(enum) | - | Required |
| 3 | 모드1 주파수(COEF_CALC=0) / 주기(COEF_CALC=1) | `FREQ1`/`PERIOD1` | Number | - | Required |
| 4 | 모드1 감쇠비 | `DR1` | Number | - | Required |
| 5 | 모드2 주파수(FREQ1≠FREQ2)/주기(PERIOD1≠PERIOD2) | `FREQ2`/`PERIOD2` | Number | - | Required |
| 6 | 모드2 감쇠비 | `DR2` | Number | - | Required |

**증분 제어 (ANAL_METHOD=2 Static 전용, `INC_CTRL`)**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 증분 방법 (0=Load Control, 1=Displacement Control) | `INC_METHOD` | Integer(enum) | - | Required |
| INC_METHOD=0 | | | | | |
| 2 | Scale Factor | `SF` | Number | 1 | Optional |
| INC_METHOD=1(`DISP_CTRL` 오브젝트) | | | | | |
| 2 | 제어 옵션 (0=Global, 1=Master Node Control) | `CTRL_OPT` | Integer(enum) | - | Required |
| 3 | 최대 병진 변위(Global 전용) | `MAX_TRANS_DISP` | Number | - | Optional |
| 4 | Master Node No.(Master Node Control 전용) | `MASTER_NODE` | Integer | - | Optional |
| 5 | Master Direction(0/1/2, Master Node Control 전용) | `MASTER_DIR` | Integer(enum) | - | Optional |
| 6 | 최대 변위(Master Node Control 전용) | `MAX_DISP` | Number | - | Optional |

**시간 적분 방법 (ANAL_METHOD=1 Direct Integration 전용, `TIME_PARAM`)**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 적분 방법 (0=Newmark, 1=HHT) | `METHOD` | Integer(enum) | - | Required |
| 2 | Newmark 방법 타입(METHOD=0) 0=Constant/1=Linear Accel./2=User Input | `NEWMARK_METHOD` | Integer(enum) | - | Optional |
| 3 | Gamma(NEWMARK_METHOD=2 시) | `GAMMA` | Number | 0.5 | Optional |
| 4 | Beta(NEWMARK_METHOD=2 시) | `BETA` | Number | 0.25 | Optional |

**비선형 경계요소 해석 (`BOUNDARY_NL_ANAL`)**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 적분법 (0=Fehlberg, 1=Cash-Karp, 2=Dormand-Prince) | `METHOD` | Integer(enum) | 0 | Optional |
| 2 | 허용 오차 | `TOL` | Number | 1e-08 | Optional |

### 7-3. Request Body 예시

**Linear + Modal + Transient**

```json
{
  "Assign": {
    "1": {
      "NAME": "LC_LINEAR_MODAL_TRANS",
      "DESC": "Linear Modal Transient case",
      "ANAL_CASE": {
        "ANAL_TYPE": 0,
        "ANAL_METHOD": 0,
        "TH_TYPE": 0
      },
      "ENDTIME": 10,
      "TIME_INC": 0.01,
      "OUTPUT_STEP": 1,
      "INIT_METHOD": "INIT",
      "USE_INIT_LOAD": true,
      "CUM_DVA": true,
      "KEEP_LOAD": true,
      "DAMPING": {
        "DAMPING_METHOD": 0,
        "ALL_DAMPING_RATIO": 0.05,
        "MODAL_DAMPING_RATIO": [
          {"MODE_NO": 1, "DAMPING": 0.05},
          {"MODE_NO": 2, "DAMPING": 0.04}
        ]
      }
    }
  }
}
```

**Nonlinear + Modal + Transient**

```json
{
  "Assign": {
    "2": {
      "NAME": "LC_NONLINEAR_MODAL_TRANS",
      "ANAL_CASE": {
        "ANAL_TYPE": 1,
        "ANAL_METHOD": 0,
        "TH_TYPE": 0
      },
      "ENDTIME": 10,
      "TIME_INC": 0.01,
      "OUTPUT_STEP": 1,
      "INIT_METHOD": "INIT",
      "USE_INIT_LOAD": true,
      "CUM_DVA": true,
      "KEEP_LOAD": true,
      "DAMPING": {
        "DAMPING_METHOD": 0,
        "ALL_DAMPING_RATIO": 0.05,
        "MODAL_DAMPING_RATIO": [
          {"MODE_NO": 1, "DAMPING": 0.05}
        ]
      },
      "NONL_CTRL_PARAM": {
        "PERFORM_ITER": true,
        "ITER_CTRL": {
          "PERMIT_FAIL": true,
          "MAX_ITER": 30,
          "NORM_CTRL": {
            "DISP": {"OPT_USE": true, "VALUE": 0.001}
          },
          "STIFF_UPD_SCHEME": 0,
          "ITER_BEF_UPDATE": 5,
          "MAX_BISECT_LEVEL": 5,
          "SMART_BISECT": false,
          "DIVERGENCE_THRESHOLD": 3,
          "LINE_SEARCH": {
            "OPT_USE": true,
            "LINE_SEARCH_OPT": 1,
            "START_ITER_NO": 3,
            "MAX_LINE_SEARCH_ITER": 4,
            "LINE_SEARCH_TOL": 0.5
          }
        }
      }
    }
  }
}
```

### 7-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── Hyper-S Linear Modal Transient 생성 ─────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "HyperS_Linear_Modal",
            "ANAL_CASE": {
                "ANAL_TYPE": 0,     # Linear
                "ANAL_METHOD": 0,   # Modal
                "TH_TYPE": 0        # Transient
            },
            "ENDTIME": 30.0,
            "TIME_INC": 0.01,
            "OUTPUT_STEP": 1,
            "INIT_METHOD": "INIT",
            "USE_INIT_LOAD": True,
            "CUM_DVA": False,
            "KEEP_LOAD": False,
            "DAMPING": {
                "DAMPING_METHOD": 0,
                "ALL_DAMPING_RATIO": 0.05
            }
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THIS-M1", json=payload, headers=HEADERS)
print("THIS-M1 POST:", resp.status_code)

# ── 조회 ─────────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THIS-M1", headers=HEADERS)
print("THIS-M1 GET:", resp.status_code)
```

---

## 8. /db/THFC – Time History Functions

시간이력 함수(시간-값 쌍 또는 사인파 함수)를 정의합니다.

### 8-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/THFC` | 전체 조회 |
| `GET` | `{base_url}/db/THFC/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/THFC` | 생성 |
| `PUT` | `{base_url}/db/THFC` | 전체 수정 |
| `PUT` | `{base_url}/db/THFC/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/THFC` | 전체 삭제 |
| `DELETE` | `{base_url}/db/THFC/{id}` | 특정 ID 삭제 |

### 8-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 함수명 | `NAME` | String | - | Required |
| 2 | 설명 | `DESC` | String | Blank | Optional |
| 3 | 데이터 타입 (1=정규화가속도, 2=가속도, 3=힘, 4=모멘트, 5=Normal) | `iTYPE` | Integer | - | Required |
| 4 | 중력 가속도 | `GRAV` | Number | - | Required |
| 5 | 함수 타입 (1=Time Function, 2=Sinusoidal) | `FUNCTYPE` | Integer | - | Required |

**Time Function (FUNCTYPE=1) 추가 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 6 | 스케일 방법 (0=Scale Factor, 1=Max Value) | `iMETHOD` | Integer | - | Required |
| 7a | 스케일 계수 (iMETHOD=0 시) | `SCALE` | Number | - | Required |
| 7b | 최대 값 (iMETHOD=1 시) | `MAXVALUE` | Number | 0 | Optional |
| 8 | 시간-값 데이터 목록 | `aFUNCDATA` | Array[Object] | - | Required |
| (1) | 시간 | `TIME` | Number | - | Required |
| (2) | 값 | `VALUE` | Number | - | Required |

**Sinusoidal (FUNCTYPE=2) 추가 파라미터**

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 6 | 상수 A | `CONS_A` | Number | - | Required |
| 7 | 상수 C | `CONS_C` | Number | - | Required |
| 8 | 주파수 | `FREQUENCY` | Number | - | Required |
| 9 | 감쇠 계수 | `DAMP_FACTOR` | Number | - | Required |
| 10 | 위상각 | `PHASE_ANGLE` | Number | - | Required |

### 8-3. Request Body 예시

**Time Function (Scale Factor)**

```json
{
  "Assign": {
    "1": {
      "NAME": "ElCentro_Scale",
      "FUNCTYPE": 1,
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1.0,
      "GRAV": 9.806,
      "aFUNCDATA": [
        {"TIME": 0.02, "VALUE":  0.00517},
        {"TIME": 0.04, "VALUE":  0.00421},
        {"TIME": 0.06, "VALUE":  0.00324},
        {"TIME": 0.08, "VALUE": -0.00102}
      ],
      "DESC": "1940 El Centro EW"
    }
  }
}
```

**Time Function (Max Value)**

```json
{
  "Assign": {
    "2": {
      "NAME": "ElCentro_MaxVal",
      "FUNCTYPE": 1,
      "iTYPE": 1,
      "iMETHOD": 1,
      "MAXVALUE": 0.2,
      "GRAV": 9.806,
      "aFUNCDATA": [
        {"TIME": 0.02, "VALUE":  0.00517},
        {"TIME": 0.04, "VALUE":  0.00421}
      ]
    }
  }
}
```

**Sinusoidal**

```json
{
  "Assign": {
    "3": {
      "NAME": "Sinusoidal_1Hz",
      "FUNCTYPE": 2,
      "iTYPE": 1,
      "GRAV": 9.806,
      "CONS_A": 0.05,
      "CONS_C": 0.01,
      "FREQUENCY": 1.0,
      "DAMP_FACTOR": 0.1,
      "PHASE_ANGLE": 0.0,
      "DESC": "1Hz Sinusoidal"
    }
  }
}
```

### 8-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 1) Time Function 생성 (Scale Factor) ─────────────────────────────────────
payload_tf = {
    "Assign": {
        "1": {
            "NAME": "EQ_EW",
            "FUNCTYPE": 1,
            "iTYPE": 1,        # Normalized Acceleration
            "iMETHOD": 0,      # Scale Factor
            "SCALE": 1.0,
            "GRAV": 9.806,
            "aFUNCDATA": [
                {"TIME": 0.02, "VALUE":  0.00517},
                {"TIME": 0.04, "VALUE":  0.00421},
                {"TIME": 0.06, "VALUE":  0.00324},
            ],
            "DESC": "El Centro EW Component"
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THFC", json=payload_tf, headers=HEADERS)
print("THFC POST (Time Function):", resp.status_code)

# ── 2) Sinusoidal 함수 생성 ──────────────────────────────────────────────────
payload_sin = {
    "Assign": {
        "2": {
            "NAME": "SIN_1Hz",
            "FUNCTYPE": 2,
            "iTYPE": 3,        # Force
            "GRAV": 9.806,
            "CONS_A": 100.0,   # 진폭 100 kN
            "CONS_C": 0.0,
            "FREQUENCY": 1.0,
            "DAMP_FACTOR": 0.0,
            "PHASE_ANGLE": 0.0
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THFC", json=payload_sin, headers=HEADERS)
print("THFC POST (Sinusoidal):", resp.status_code)

# ── 3) 특정 함수 조회 ────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THFC/1", headers=HEADERS)
print("THFC GET/1:", resp.json())
```

---

## 9. /db/THGA – Ground Acceleration

시간이력 하중 케이스에 적용되는 지반 가속도를 정의합니다.

### 9-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/THGA` | 전체 조회 |
| `GET` | `{base_url}/db/THGA/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/THGA` | 생성 |
| `PUT` | `{base_url}/db/THGA` | 전체 수정 |
| `PUT` | `{base_url}/db/THGA/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/THGA` | 전체 삭제 |
| `DELETE` | `{base_url}/db/THGA/{id}` | 특정 ID 삭제 |

### 9-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 시간이력 하중 케이스명 | `NAME` | String | - | Required |
| 2 | 수평 지반 가속도 각도 | `ANGLE` | Number | 0 | Optional |
| 3 | X방향 함수명 | `FUNCX` | String | - | Required |
| 4 | X방향 스케일 계수 | `SCALEX` | Number | - | Required |
| 5 | X방향 도달 시간 | `ATIMEX` | Number | 0 | Optional |
| 6 | Y방향 함수명 | `FUNCY` | String | - | Required |
| 7 | Y방향 스케일 계수 | `SCALEY` | Number | - | Required |
| 8 | Y방향 도달 시간 | `ATIMEY` | Number | 0 | Optional |
| 9 | Z방향 함수명 | `FUNCZ` | String | - | Required |
| 10 | Z방향 스케일 계수 | `SCALEZ` | Number | - | Required |
| 11 | Z방향 도달 시간 | `ATIMEZ` | Number | 0 | Optional |

### 9-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "NAME": "GA_ElCentro",
      "ANGLE": 0,
      "FUNCX": "ElCentro_EW",
      "SCALEX": 1.0,
      "ATIMEX": 0,
      "FUNCY": "ElCentro_NS",
      "SCALEY": 0.85,
      "ATIMEY": 0,
      "FUNCZ": "ElCentro_UD",
      "SCALEZ": 0.65,
      "ATIMEZ": 0
    }
  }
}
```

### 9-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 지반 가속도 하중 생성 ────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "GA_3Dir",
            "ANGLE": 0.0,
            "FUNCX": "EQ_EW",    # X방향 : 수평(EW)
            "SCALEX": 1.0,
            "ATIMEX": 0.0,
            "FUNCY": "EQ_NS",    # Y방향 : 수평(NS)
            "SCALEY": 1.0,
            "ATIMEY": 0.0,
            "FUNCZ": "EQ_UD",    # Z방향 : 수직(UD)
            "SCALEZ": 0.667,
            "ATIMEZ": 0.0
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THGA", json=payload, headers=HEADERS)
print("THGA POST:", resp.status_code)

# ── 전체 조회 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THGA", headers=HEADERS)
print("THGA GET:", resp.json())
```

---

## 10. /db/THNL – Dynamic Nodal Loads

시간이력 하중 케이스에 적용되는 동적 절점 하중을 정의합니다.

> **주의**: `FUNC_NAME`에는 Force 또는 Moment 타입의 시간이력 함수만 사용 가능합니다.

### 10-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/THNL` | 전체 조회 |
| `GET` | `{base_url}/db/THNL/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/THNL` | 생성 |
| `PUT` | `{base_url}/db/THNL` | 전체 수정 |
| `PUT` | `{base_url}/db/THNL/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/THNL` | 전체 삭제 |
| `DELETE` | `{base_url}/db/THNL/{id}` | 특정 ID 삭제 |

### 10-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 동적 절점 하중 목록 | `ITEMS` | Array[Object] | - | Required |
| (1) | 일련번호 | `ID` | Integer | 0 | Optional |
| (2) | 시간이력 하중 케이스명 | `THLCNAME` | String | - | Required |
| (3) | 시간이력 함수명 (Force/Moment 타입만 사용 가능) | `FUNC_NAME` | String | - | Required |
| (4) | 방향 (`"X"` / `"Y"` / `"Z"`) | `DIR` | String | - | Required |
| (5) | 도달 시간 | `ARRIVAL_TIME` | Number | - | Required |
| (6) | 스케일 계수 | `SCALE_FACTOR` | Number | - | Required |

### 10-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "THLCNAME": "TH01_Linear_Modal",
          "FUNC_NAME": "SIN_1Hz",
          "DIR": "Y",
          "ARRIVAL_TIME": 0.0,
          "SCALE_FACTOR": 1.0
        },
        {
          "ID": 2,
          "THLCNAME": "TH01_Linear_Modal",
          "FUNC_NAME": "SIN_1Hz",
          "DIR": "Z",
          "ARRIVAL_TIME": 5.0,
          "SCALE_FACTOR": 0.5
        }
      ]
    }
  }
}
```

### 10-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 동적 절점 하중 생성 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "ID": 1,
                    "THLCNAME": "TH01_Linear_Modal",
                    "FUNC_NAME": "SIN_1Hz",     # Force/Moment 타입 함수
                    "DIR": "Y",
                    "ARRIVAL_TIME": 0.0,
                    "SCALE_FACTOR": 1.0
                }
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THNL", json=payload, headers=HEADERS)
print("THNL POST:", resp.status_code)

# ── 전체 조회 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THNL", headers=HEADERS)
print("THNL GET:", resp.json())
```

---

## 11. /db/THSL – Time Varying Static Loads

시간이력 하중 케이스에 적용되는 시변 정적 하중을 정의합니다.

> **주의**: `THIS_FUNCNAME`에는 Normal 타입의 시간이력 함수만 사용 가능합니다.

### 11-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/THSL` | 전체 조회 |
| `GET` | `{base_url}/db/THSL/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/THSL` | 생성 |
| `PUT` | `{base_url}/db/THSL` | 전체 수정 |
| `PUT` | `{base_url}/db/THSL/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/THSL` | 전체 삭제 |
| `DELETE` | `{base_url}/db/THSL/{id}` | 특정 ID 삭제 |

### 11-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 시간이력 하중 케이스명 | `THIS_LCNAME` | String | - | Required |
| 2 | 정적 하중 케이스명 | `SLOAD` | String | - | Required |
| 3 | 시간이력 함수명 (Normal 타입만 사용 가능) | `THIS_FUNCNAME` | String | - | Required |
| 4 | 도달 시간 | `ATIME` | Number | 0 | Optional |
| 5 | 스케일 계수 | `SCALE` | Number | - | Required |

### 11-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "THIS_LCNAME": "TH01_Linear_Modal",
      "SLOAD": "SW",
      "THIS_FUNCNAME": "NormFunc_SW",
      "ATIME": 0.0,
      "SCALE": 1.0
    },
    "2": {
      "THIS_LCNAME": "TH01_Linear_Modal",
      "SLOAD": "Pretension",
      "THIS_FUNCNAME": "NormFunc_PT",
      "ATIME": 3.0,
      "SCALE": 1.0
    }
  }
}
```

### 11-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 시변 정적 하중 생성 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "THIS_LCNAME": "TH01_Linear_Modal",
            "SLOAD": "SW",               # 정적 하중 케이스명
            "THIS_FUNCNAME": "NormFunc",  # Normal 타입 시간이력 함수
            "ATIME": 0.0,
            "SCALE": 1.0
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THSL", json=payload, headers=HEADERS)
print("THSL POST:", resp.status_code)

# ── 특정 케이스 삭제 ─────────────────────────────────────────────────────────
resp = requests.delete(f"{BASE_URL}/db/THSL/1", headers=HEADERS)
print("THSL DELETE/1:", resp.status_code)
```

---

## 12. /db/THMS – Multiple Support Excitation

다중 지점 가진을 정의합니다.

> **주의**: `FUNCX` / `FUNCY` / `FUNCZ`에는 Normalized Acceleration 또는 Acceleration 타입의 시간이력 함수만 사용 가능합니다.

### 12-1. HTTP 메서드 및 URL

| 메서드 | URL | 설명 |
|--------|-----|------|
| `GET` | `{base_url}/db/THMS` | 전체 조회 |
| `GET` | `{base_url}/db/THMS/{id}` | 특정 ID 조회 |
| `POST` | `{base_url}/db/THMS` | 생성 |
| `PUT` | `{base_url}/db/THMS` | 전체 수정 |
| `PUT` | `{base_url}/db/THMS/{id}` | 특정 ID 수정 |
| `DELETE` | `{base_url}/db/THMS` | 전체 삭제 |
| `DELETE` | `{base_url}/db/THMS/{id}` | 특정 ID 삭제 |

### 12-2. 파라미터

| No. | 설명 | Key | Value Type | Default | Required |
|-----|------|-----|------------|---------|----------|
| 1 | 다중 지점 가진 목록 | `ITEMS` | Array[Object] | - | Required |
| (1) | 일련번호 | `ID` | Integer | 0 | Optional |
| (2) | 시간이력 하중 케이스명 | `LCNAME` | String | - | Required |
| (3) | 수평 지반 가속도 각도 | `ANGLE` | Number | 0 | Optional |
| (4) | X방향 함수명 (NormAccel/Acceleration 타입만) | `FUNCX` | String | - | Required |
| (5) | X방향 스케일 계수 | `SCALEX` | Number | - | Required |
| (6) | X방향 도달 시간 | `ATIMEX` | Number | 0 | Optional |
| (7) | Y방향 함수명 | `FUNCY` | String | - | Optional |
| (8) | Y방향 스케일 계수 | `SCALEY` | Number | - | Optional |
| (9) | Y방향 도달 시간 | `ATIMEY` | Number | 0 | Optional |
| (10) | Z방향 함수명 | `FUNCZ` | String | - | Optional |
| (11) | Z방향 스케일 계수 | `SCALEZ` | Number | - | Optional |
| (12) | Z방향 도달 시간 | `ATIMEZ` | Number | 0 | Optional |

### 12-3. Request Body 예시

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "TH01_Linear_Modal",
          "ANGLE": 0,
          "FUNCX": "ElCentro_EW",
          "SCALEX": 1.0,
          "ATIMEX": 0,
          "FUNCY": "ElCentro_NS",
          "SCALEY": 1.0,
          "ATIMEY": 0,
          "FUNCZ": "ElCentro_UD",
          "SCALEZ": 0.667,
          "ATIMEZ": 0
        }
      ]
    }
  }
}
```

### 12-4. Python 예제 코드

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 다중 지점 가진 생성 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "TH01_Linear_Modal",
                    "ANGLE": 0.0,
                    "FUNCX": "ElCentro_EW",
                    "SCALEX": 1.0,
                    "ATIMEX": 0.0,
                    "FUNCY": "ElCentro_NS",
                    "SCALEY": 1.0,
                    "ATIMEY": 0.0,
                    "FUNCZ": "ElCentro_UD",
                    "SCALEZ": 0.667,
                    "ATIMEZ": 0.0
                }
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THMS", json=payload, headers=HEADERS)
print("THMS POST:", resp.status_code)

# ── 전체 조회 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THMS", headers=HEADERS)
print("THMS GET:", resp.json())
```

---

## End-to-End 워크플로우 예제

응답 스펙트럼 해석 및 시간이력 해석의 전형적인 설정 순서를 보여주는 예제입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── STEP 1: 응답 스펙트럼 함수 생성 (KDS 41-17-00:2019) ─────────────────────
spfc = {
    "Assign": {
        "1": {
            "NAME": "RS_KDS2019",
            "iTYPE": 1,
            "iMETHOD": 0,
            "SCALE": 1.0,
            "GRAV": 9.806,
            "DRATIO": 0.05,
            "STR": {"SPEC_CODE": "KDS(41-17-00:2019)"},
            "OPT": {"SC_": 2, "iSEISZONE": 0},
            "VAL": {
                "aSRA": [0.22, 0.154],
                "aSCP": [1.0, 1.5],
                "PERIOD": 4.0,
                "IE": 1.2,
                "R_": 5.0,
                "ZONEFACTOR": 0.22
            }
        }
    }
}
r = requests.post(f"{BASE_URL}/db/SPFC", json=spfc, headers=HEADERS)
print("STEP 1 - SPFC:", r.status_code)

# ── STEP 2: 응답 스펙트럼 하중 케이스 생성 ──────────────────────────────────
splc = {
    "Assign": {
        "1": {
            "NAME": "RS_EQ_XY",
            "DIR": "XY",
            "ANGLE": 0.0,
            "SCALE": 1.0,
            "PMFT": 1.0,
            "bDAMP": True,
            "INTERP": "LOG",
            "COMTYPE": "CQC",
            "bADDSIGN": True,
            "iSIGNTYPE": 0,
            "bMODE": True,
            "aFUNCNAME": ["RS_KDS2019"],
            "aUSEMODE": [
                {"bUSE": True, "MSFACTOR": 1},
                {"bUSE": True, "MSFACTOR": 1},
                {"bUSE": True, "MSFACTOR": 1}
            ],
            "bCDAMP": True,
            "iMDTYPE": 1,
            "DALL": 0.05
        }
    }
}
r = requests.post(f"{BASE_URL}/db/SPLC", json=splc, headers=HEADERS)
print("STEP 2 - SPLC:", r.status_code)

# ── STEP 3: 시간이력 함수 생성 (El Centro 지진파) ────────────────────────────
thfc = {
    "Assign": {
        "1": {
            "NAME": "ElCentro_EW",
            "FUNCTYPE": 1,
            "iTYPE": 1,
            "iMETHOD": 1,
            "MAXVALUE": 0.348,
            "GRAV": 9.806,
            "aFUNCDATA": [
                {"TIME": 0.02, "VALUE":  0.00517},
                {"TIME": 0.04, "VALUE":  0.00421},
                # ... 실제 데이터 추가 ...
            ]
        }
    }
}
r = requests.post(f"{BASE_URL}/db/THFC", json=thfc, headers=HEADERS)
print("STEP 3 - THFC:", r.status_code)

# ── STEP 4: 시간이력 전역 제어 설정 ─────────────────────────────────────────
thgc = {
    "Assign": {
        "1": {
            "GNT": 0,
            "ILT": 0,
            "aILL": [{"SLC": "DL", "SF": 1.0, "LCT": 1}],
            "IEPI": True,
            "NSTEP": 1,
            "bROT": False,
            "SNIO": 1,
            "bPCF": True,
            "MAXNS": 10,
            "MAXIT": 30,
            "bDN": True,
            "bFN": False,
            "bEN": False,
            "DN": 0.001,
            "FN": 0.001,
            "EN": 0.001,
            "bULSM": False,
            "ULSM": 5,
            "ENERGYRESULT": True,
            "SDVI": True,
            "SDVE": True,
            "SDST": True,
            "SDHY": True,
            "SDIS": True,
            "bMSSSTATUS": True
        }
    }
}
r = requests.post(f"{BASE_URL}/db/THGC", json=thgc, headers=HEADERS)
print("STEP 4 - THGC:", r.status_code)

# ── STEP 5: 시간이력 하중 케이스 생성 (Linear Modal Transient) ───────────────
this = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "TH_EQ_Linear",
                "iATYPE": 1,        # Linear
                "iAMETHOD": 1,      # Modal
                "iTHTYPE": 1,       # Transient
                "ENDTIME": 40.0,
                "INC": 0.01,
                "iOUT": 1,
                "INITMETHOD": "INIT",
                "INITLOAD": 0,
                "bDVA": False,
                "bKEEP": False,
                "iMDTYPE": 1        # Modal 감쇠
            },
            "DALL": 0.05
        }
    }
}
r = requests.post(f"{BASE_URL}/db/THIS", json=this, headers=HEADERS)
print("STEP 5 - THIS:", r.status_code)

# ── STEP 6: 지반 가속도 적용 ────────────────────────────────────────────────
thga = {
    "Assign": {
        "1": {
            "NAME": "TH_EQ_Linear",
            "ANGLE": 0.0,
            "FUNCX": "ElCentro_EW",
            "SCALEX": 1.0,
            "ATIMEX": 0.0,
            "FUNCY": "ElCentro_EW",
            "SCALEY": 0.85,
            "ATIMEY": 0.0,
            "FUNCZ": "ElCentro_EW",
            "SCALEZ": 0.667,
            "ATIMEZ": 0.0
        }
    }
}
r = requests.post(f"{BASE_URL}/db/THGA", json=thga, headers=HEADERS)
print("STEP 6 - THGA:", r.status_code)

print("\n=== 동적 하중 설정 완료 ===")
```

---

*다음 파트: [10_DB_Construction_Stage.md](10_DB_Construction_Stage.md)*
