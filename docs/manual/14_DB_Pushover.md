# 14. DB – Pushover

> **대상 제품:** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **인증 헤더:** `MAPI-Key: <발급된 키>`  
> **출처:** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

---

## Endpoint 목록

| No. | Endpoint | 기능 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/db/POGD`](#1-dbpogd--pushover-analysis-control-data) | 푸시오버 해석 제어 데이터 | POST, GET, PUT, DELETE |
| 2 | [`/db/POGD-M1`](#2-dbpogd-m1--pushover-global-control-hyper-s) | 푸시오버 전역 제어 (Hyper-S) | GET, PUT, DELETE |
| 3 | [`/db/IEPI`](#3-dbiepi--ignore-elements-for-pushover-initial-load) | 푸시오버 초기하중 무시 요소 | POST, GET, PUT, DELETE |
| 4 | [`/db/PHGE`](#4-dbphge--assign-pushover-hinge-properties) | 푸시오버 힌지 속성 배정 | POST, GET, PUT, DELETE |
| 5 | [`/db/POLC`](#5-dbpolc--pushover-load-cases) | 푸시오버 하중케이스 | POST, GET, PUT, DELETE |
| 6 | [`/db/POLC-M1`](#6-dbpolc-m1--pushover-load-case-hyper-s) | 푸시오버 하중케이스 (Hyper-S) | GET, PUT, DELETE |

> **참고:** Hyper-S 솔버 전용 엔드포인트(`-M1`)는 **POST를 지원하지 않습니다.** 데이터 생성·수정은 `PUT`으로, 조회는 `GET`으로, 삭제는 `DELETE`로 수행합니다.

---

## 1. `/db/POGD` — Pushover Analysis Control Data

> **기능:** 푸시오버(정적 비선형) 해석의 전역 제어 데이터를 정의합니다. 기하비선형 옵션, 초기하중 방법, 비선형 해석 옵션(수렴 조건·해석 정지 조건), 파이버 모델 옵션, 힌지 데이터 옵션을 포함합니다.

### Input URI

```
{base url}/db/POGD
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "POGD": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "GEOMNONLINEAR_TYPE": { "description": "GeometricNonlinearityType", "type": "string" },
      "INITLOADMETHOD": { "description": "InitialLoadAnalysisMethod", "type": "string" },
      "INITLOAD": {
        "description": "InitialLoadCaseList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "LC_NAME": { "description": "LoadCaseName", "type": "string" },
            "LC_TYPE": { "description": "LoadCaseType", "type": "string" },
            "SF": { "description": "ScaleFactor", "type": "number" }
          }
        }
      },
      "bCONSIGNOREELEM": { "description": "ConsiderIgnoreElementsforNL.AnalysisInitialLoad", "type": "boolean" },
      "NONL_OPT": {
        "description": "NonlinearAnalysisOption",
        "type": "object",
        "properties": {
          "bPERMITFAIL": { "description": "NonlinearAnalysisPermitConvergenceFailure", "type": "boolean" },
          "SUBSTEP": { "description": "NonlinearAnalysisMaxNum.ofSubsteps", "type": "integer" },
          "MAXITER": { "description": "MaximumIteration", "type": "integer" },
          "bDISPLNORM": { "description": "UseConvergenceCriteriaDisplacementNorm", "type": "boolean" },
          "bFORCENORM": { "description": "UseConvergenceCriteriaForceNorm", "type": "boolean" },
          "bENERGYNORM": { "description": "UseConvergenceCriteriaEnergyNorm", "type": "boolean" },
          "DISPLNORM": { "description": "DisplacementNorm", "type": "number" },
          "FORCENORM": { "description": "ForceNorm", "type": "number" },
          "ENERGYNORM": { "description": "EnergyNorm", "type": "number" },
          "bSHEARYIELDSTOP": { "description": "UseAnalysisStop-ShearComp.Yield", "type": "boolean" },
          "BSHEARYIELDSTOPBEAM": { "description": "UseAnalysisStop-ShearComp.Yield-Beam/Column", "type": "boolean" },
          "bSHEARYIELDSTOPWALL": { "description": "UseAnalysisStop-ShearComp.Yield-Wall", "type": "boolean" },
          "bAXIALYIELDSTOP": { "description": "UseAnalysisStop-AxialComp.Collapse/Buckling", "type": "boolean" },
          "bAXIALYIELDSTOPBEAM": { "description": "UseAnalysisStop-AxialComp.Collapse/Buckling-Beam/Column", "type": "boolean" },
          "bAXIALYIELDSTOPWALL": { "description": "UseAnalysisStop-AxialComp.Collapse/Buckling-Wall", "type": "boolean" },
          "bAXIALYIELDSTOPTRUSS": { "description": "UseAnalysisStop-AxialComp.Collapse/Buckling-Truss", "type": "boolean" },
          "bSUPPORTDZDIRSTOP": { "description": "UseAnalysisStop-SupportUplifting/Collapse:Dz-Direction", "type": "boolean" },
          "bSUPPORTSTOPUPLIFTING": { "description": "UseAnalysisStop-Uplifting:Dz-Direction", "type": "boolean" },
          "bSUPPORTSTOPCOLLAPSE": { "description": "UseAnalysisStop-Collapse:Dz-Direction", "type": "boolean" }
        }
      },
      "PHOP_OPT": {
        "description": "NonlinearAnalysisOption",
        "type": "object",
        "properties": {
          "bCONSREBARAREA1D": { "description": "FiberModelOption-ConsiderBeam/ColumnReinforcementArea", "type": "boolean" },
          "BEAM_CORE_SIZE": { "description": "FiberModelOption-Beam-ColumnCoreAreasSizeType", "type": "string" },
          "BEAM_CORE_DIV_Y": { "description": "FiberModelOption-Beam-ColumnCoreDivision(y-dir)", "type": "integer" },
          "BEAM_CORE_DIV_Z": { "description": "FiberModelOption-Beam-ColumnCoreDivision(z-dir)", "type": "integer" },
          "BEAM_COVER_SIZE": { "description": "FiberModelOption-Beam-ColumnCoverAreasSizeType", "type": "string" },
          "BEAM_COVER_DIV_Y": { "description": "FiberModelOption-Beam-ColumnCoverDivision(y-dir)", "type": "integer" },
          "BEAM_COVER_DIV_Z": { "description": "FiberModelOption-Beam-ColumnCoverDivision(z-dir)", "type": "integer" },
          "bCONSREBARAREAWALL": { "description": "FiberModelOption-ConsiderWallReinforcementArea", "type": "boolean" },
          "bWALLCONSOUT": { "description": "FiberModelOption-WallConsiderOut-of-planeNonlinearityofPlateType", "type": "boolean" },
          "WALL_CORE_SIZE": { "description": "FiberModelOption-WallCoreFiberAreasSizeType", "type": "string" },
          "WALL_CORE_DIV_Z": { "description": "FiberModelOption-WallCoreDivision(z-dir)", "type": "integer" },
          "WALL_CORE_DIV_Y": { "description": "FiberModelOption-WallCoreDivision(y-dir)", "type": "integer" },
          "WALL_COVER_SIZE": { "description": "FiberModelOption-WallCoverAreasSizeType", "type": "string" },
          "WALL_COVER_DIV_Z": { "description": "FiberModelOption-WallCoverDivision(z-dir)", "type": "integer" },
          "WALL_COVER_DIV_Y": { "description": "FiberModelOption-WallCoverDivision(y-dir)", "type": "integer" },
          "SHEAR_R": { "description": "FiberModelOption-SpringShear", "type": "number" },
          "bASSIGNBYMEMBER": { "description": "AssignHingePropertiestoMemberonlyforMoment-RotationBeam/Column", "type": "boolean" },
          "bTRI_SYM": { "description": "UseTrilinearDefaultStiffnessReductionSymmetrical", "type": "boolean" },
          "TRI_TENS_A1": { "description": "TrilinearDefaultStiffnessReduction-Tens.a1", "type": "number" },
          "TRI_TENS_A2": { "description": "TrilinearDefaultStiffnessReduction-Tens.a2", "type": "number" },
          "TRI_COMP_A1": { "description": "TrilinearDefaultStiffnessReduction-Comp.a1", "type": "number" },
          "TRI_COMP_A2": { "description": "TrilinearDefaultStiffnessReduction-Comp.a2", "type": "number" },
          "bBI_SYM": { "description": "UseBilinearDefaultStiffnessReductionSymmetrical", "type": "boolean" },
          "BI_TENS_A1": { "description": "BilinearDefaultStiffnessReduction-Tens.a1", "type": "number" },
          "BI_COMP_A1": { "description": "BilinearDefaultStiffnessReduction-Comp.a1", "type": "number" },
          "PSPR_APPLY_TYPE": { "description": "PointSpringSupportApplyType", "type": "string" },
          "ELNK_APPLY_TYPE": { "description": "ElasticLinkApplyType", "type": "string" },
          "bUSEAUTOCALCREFERENCE": { "description": "ReferenceCode/ManualforAuto-Calculation", "type": "boolean" },
          "RCDGNCODE": { "description": "RCReferenceDesignCode", "type": "string" },
          "LOC_BEAM": { "description": "ReferenceLocationofBeam/DistributedHinges", "type": "string" },
          "LOC_COLUMN": { "description": "ReferenceLocationofColumn", "type": "string" },
          "SF_WALL": { "description": "ScaleFactorforUltimateRotation-WallScaleFactor", "type": "number" },
          "bSF_BRITTLE": { "description": "ScaleFactorforUltimateRotation-UseBrittleScaleFactor", "type": "boolean" },
          "SF_BRITTLE": { "description": "ScaleFactorforUltimateRotation-BrittleScaleFactor", "type": "number" },
          "bSF_EARTHQUAKE": { "description": "ScaleFactorforUltimateRotation-UseEarthquakeScaleFactor", "type": "boolean" },
          "SF_EARTHQUAKE": { "description": "ScaleFactorforUltimateRotation-EarthquakeScaleFactor", "type": "number" },
          "bSF_SMOOTH_BAR": { "description": "ScaleFactorforUltimateRotation-UseSmoothbarScaleFactor", "type": "boolean" },
          "SF_SMOOTH_BAR": { "description": "ScaleFactorforUltimateRotation-SmoothbarScaleFactor", "type": "number" },
          "SND_SEIS_GRUP": { "description": "SecondarySeismicElementsGroupName", "type": "string" },
          "CONFIDENCE": { "description": "ConfidenceFactor", "type": "number" },
          "bBUCKLING": { "description": "CalcYieldSurfaceofBeamconsideringBuckling", "type": "boolean" },
          "bCALCAXIALFORCE": { "description": "CalcMcConsideringAxialForce(AIJ)", "type": "boolean" }
        }
      },
      "NODECONNECTIVITY": { "description": "WallNodeConnectivity", "type": "string" },
      "bSHOWGRAPHAFTER": { "description": "Misc...-ShowPushoverCurveResultAfterAnalysis", "type": "boolean" },
      "bSHOWGRAPGHDURING": { "description": "Misc...-ShowPushoverCurveduringAnalysis", "type": "boolean" }
    }
  }
}
```

### Parameters

**최상위 항목**

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 기하비선형 타입 · None: `"NONE"` / Large Displacements: `"LARGE_DISP"` | `"GEOMNONLINEAR_TYPE"` | String | `"NONE"` | Optional |
| 2 | 초기하중 방법 · 비선형 정적해석 수행: `"PERFORM_ANAL"` / 정적·시공단계 해석결과 가져오기: `"IMPORT_RESULT"` | `"INITLOADMETHOD"` | String | `"PERFORM_ANAL"` | Optional |
| 3 | 초기하중 케이스 목록 | `"INITLOAD"` | Array [Object] | — | Optional |
| — | (INITLOAD) 하중케이스명 | `"LC_NAME"` | String | — | Required |
| — | (INITLOAD) 하중케이스 타입 | `"LC_TYPE"` | String | — | Required |
| — | (INITLOAD) 축척계수 | `"SF"` | Number | — | Required |
| 4 | 초기하중이 비선형 정적해석일 때, 무시 요소(IEPI) 고려 여부 | `"bCONSIGNOREELEM"` | Boolean | `false` | Optional |
| 5 | 비선형 해석 옵션 | `"NONL_OPT"` | Object | — | **Required** |
| 6 | 푸시오버 힌지 데이터 옵션 | `"PHOP_OPT"` | Object | — | Optional |
| 7 | 벽체 노드 연결성 · 핀: `"PINNED"` / 고정: `"FIXED"` | `"NODECONNECTIVITY"` | String | — | Required |
| 8 | 해석 후 푸시오버 곡선 결과 표시 | `"bSHOWGRAPHAFTER"` | Boolean | — | Required |
| 9 | 해석 중 푸시오버 곡선 표시 | `"bSHOWGRAPGHDURING"` | Boolean | — | Required |

**`NONL_OPT` (비선형 해석 옵션) 상세**

| 그룹 | Key | 설명 | 타입 | 기본값 |
|------|-----|------|------|--------|
| 일반 | `bPERMITFAIL` | 수렴 실패 허용 | Boolean | `false` |
| 일반 | `SUBSTEP` | 서브스텝 최대 수 | Integer | — |
| 일반 | `MAXITER` | 최대 반복 횟수 | Integer | — |
| 수렴조건 | `bDISPLNORM` / `DISPLNORM` | 변위 노름 사용 여부/값 | Boolean/Number | `false` / `0` |
| 수렴조건 | `bFORCENORM` / `FORCENORM` | 하중 노름 사용 여부/값 | Boolean/Number | `false` / `0` |
| 수렴조건 | `bENERGYNORM` / `ENERGYNORM` | 에너지 노름 사용 여부/값 | Boolean/Number | `false` / `0` |
| 해석정지 | `bSHEARYIELDSTOP` | 전단 성분 항복 시 정지 | Boolean | `false` |
| 해석정지 | `BSHEARYIELDSTOPBEAM` | 〃 – 보/기둥 | Boolean | `false` |
| 해석정지 | `bSHEARYIELDSTOPWALL` | 〃 – 벽체 | Boolean | `false` |
| 해석정지 | `bAXIALYIELDSTOP` | 축력 성분 붕괴/좌굴 시 정지 | Boolean | `false` |
| 해석정지 | `bAXIALYIELDSTOPBEAM` | 〃 – 보/기둥 | Boolean | `false` |
| 해석정지 | `bAXIALYIELDSTOPWALL` | 〃 – 벽체 | Boolean | `false` |
| 해석정지 | `bAXIALYIELDSTOPTRUSS` | 〃 – 트러스 | Boolean | `false` |
| 해석정지 | `bSUPPORTDZDIRSTOP` | 지점 부상/붕괴(Dz방향) 시 정지 | Boolean | `false` |
| 해석정지 | `bSUPPORTSTOPUPLIFTING` | 〃 – 부상(Uplifting) | Boolean | `false` |
| 해석정지 | `bSUPPORTSTOPCOLLAPSE` | 〃 – 붕괴(Collapse) | Boolean | `false` |

**`PHOP_OPT` (푸시오버 힌지 데이터 옵션) 상세**

| 그룹 | Key | 설명 | 타입 |
|------|-----|------|------|
| 파이버(보-기둥) | `bCONSREBARAREA1D` | 철근량 고려 | Boolean |
| 파이버(보-기둥) | `BEAM_CORE_SIZE` | 코어 영역 크기 타입 · Auto: `"AUTO"` / Equal: `"EQUAL"` | String |
| 파이버(보-기둥) | `BEAM_CORE_DIV_Y` / `BEAM_CORE_DIV_Z` | 코어 분할 수 (y/z) | Integer |
| 파이버(보-기둥) | `BEAM_COVER_SIZE` | 커버 영역 크기 타입 | String |
| 파이버(보-기둥) | `BEAM_COVER_DIV_Y` / `BEAM_COVER_DIV_Z` | 커버 분할 수 (y/z) | Integer |
| 파이버(벽체) | `bCONSREBARAREAWALL` | 철근량 고려 | Boolean |
| 파이버(벽체) | `bWALLCONSOUT` | 판 타입 면외 비선형성 고려 | Boolean |
| 파이버(벽체) | `WALL_CORE_SIZE` / `WALL_COVER_SIZE` | 코어/커버 크기 타입 | String |
| 파이버(벽체) | `WALL_CORE_DIV_Z` / `WALL_CORE_DIV_Y` | 코어 분할 수 (z/y) | Integer |
| 파이버(벽체) | `WALL_COVER_DIV_Z` / `WALL_COVER_DIV_Y` | 커버 분할 수 (z/y) | Integer |
| 파이버(벽체) | `SHEAR_R` | 스프링 전단 계수 | Number |
| 힌지옵션 | `bASSIGNBYMEMBER` | 모멘트-회전 보/기둥 힌지속성을 부재단위로만 배정 | Boolean |
| 강성저감(3선형) | `bTRI_SYM` | 대칭 여부 | Boolean |
| 강성저감(3선형) | `TRI_TENS_A1` / `TRI_TENS_A2` | 인장 α1/α2 | Number |
| 강성저감(3선형) | `TRI_COMP_A1` / `TRI_COMP_A2` | 압축 α1/α2 | Number |
| 강성저감(2선형) | `bBI_SYM` | 대칭 여부 | Boolean |
| 강성저감(2선형) | `BI_TENS_A1` / `BI_COMP_A1` | 인장/압축 α1 | Number |
| 스프링/링크 비선형 | `PSPR_APPLY_TYPE` · `"APPLY"` / `"ASSUME"` | 점 스프링 지지 적용 타입 | String |
| 스프링/링크 비선형 | `ELNK_APPLY_TYPE` · `"APPLY"` / `"ASSUME"` | 탄성링크 적용 타입 | String |
| 강도 자동계산 | `bUSEAUTOCALCREFERENCE` | 참조 코드/매뉴얼 사용 | Boolean |
| 강도 자동계산 | `RCDGNCODE` · `"KISTEC2019"` / `"KISTEC2013"` / `"MOE2019"` / `"MOE2018"` / `"AIK-G-001-2021"` | RC 참조 설계기준 | String |
| 강도 자동계산 | `LOC_BEAM` · I단: `"I"` / J단: `"J"` / 중앙: `"M"` | 보/분포힌지 기준 위치 | String |
| 강도 자동계산 | `LOC_COLUMN` | 기둥 기준 위치 | String |
| 극한회전 축척계수 | `SF_WALL` | 벽체 축척계수 | Number |
| 극한회전 축척계수 | `bSF_BRITTLE` / `SF_BRITTLE` | 취성 축척계수 사용/값 | Boolean/Number |
| 극한회전 축척계수 | `bSF_EARTHQUAKE` / `SF_EARTHQUAKE` | 지진 축척계수 사용/값 | Boolean/Number |
| 극한회전 축척계수 | `bSF_SMOOTH_BAR` / `SF_SMOOTH_BAR` | 원형철근 축척계수 사용/값 | Boolean/Number |
| 기타 | `SND_SEIS_GRUP` | 2차 내진요소 그룹명 | String |
| 기타 | `CONFIDENCE` | 신뢰도 계수 | Number |
| 기타 | `bBUCKLING` | 좌굴 고려 항복면 계산 | Boolean |
| 기타 | `bCALCAXIALFORCE` | 축력 고려 Mc 계산(AIJ) | Boolean |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "GEOMNONLINEAR_TYPE": "NONE",
      "INITLOADMETHOD": "PERFORM_ANAL",
      "INITLOAD": [],
      "bCONSIGNOREELEM": true,
      "NONL_OPT": {
        "bPERMITFAIL": true,
        "SUBSTEP": 10,
        "MAXITER": 10,
        "bDISPLNORM": true,
        "bFORCENORM": false,
        "bENERGYNORM": false,
        "DISPLNORM": 0.001,
        "FORCENORM": 0.001,
        "ENERGYNORM": 0.001,
        "bSHEARYIELDSTOP": false,
        "BSHEARYIELDSTOPBEAM": true,
        "bSHEARYIELDSTOPWALL": false,
        "bAXIALYIELDSTOP": false,
        "bAXIALYIELDSTOPBEAM": true,
        "bAXIALYIELDSTOPWALL": false,
        "bAXIALYIELDSTOPTRUSS": false,
        "bSUPPORTDZDIRSTOP": false,
        "bSUPPORTSTOPUPLIFTING": false,
        "bSUPPORTSTOPCOLLAPSE": false
      },
      "PHOP_OPT": {
        "bCONSREBARAREA1D": false,
        "BEAM_CORE_SIZE": "AUTO",
        "BEAM_CORE_DIV_Y": 15,
        "BEAM_CORE_DIV_Z": 15,
        "BEAM_COVER_SIZE": "EQUAL",
        "BEAM_COVER_DIV_Y": 15,
        "BEAM_COVER_DIV_Z": 15,
        "bCONSREBARAREAWALL": false,
        "bWALLCONSOUT": true,
        "WALL_CORE_SIZE": "AUTO",
        "WALL_CORE_DIV_Z": 8,
        "WALL_CORE_DIV_Y": 8,
        "WALL_COVER_SIZE": "AUTO",
        "WALL_COVER_DIV_Z": 8,
        "WALL_COVER_DIV_Y": 1,
        "SHEAR_R": 0.4,
        "bASSIGNBYMEMBER": true,
        "bTRI_SYM": true,
        "TRI_TENS_A1": 0.1,
        "TRI_TENS_A2": 0.05,
        "TRI_COMP_A1": 0.1,
        "TRI_COMP_A2": 0.05,
        "bBI_SYM": true,
        "BI_TENS_A1": 0.05,
        "BI_COMP_A1": 0.05,
        "PSPR_APPLY_TYPE": "ASSUME",
        "ELNK_APPLY_TYPE": "APPLY",
        "bUSEAUTOCALCREFERENCE": true,
        "RCDGNCODE": "KISTEC2019",
        "LOC_BEAM": "M",
        "LOC_COLUMN": "I",
        "SF_WALL": 1.6,
        "bSF_BRITTLE": false,
        "SF_BRITTLE": 1.6,
        "bSF_EARTHQUAKE": false,
        "SF_EARTHQUAKE": 0.85,
        "bSF_SMOOTH_BAR": false,
        "SF_SMOOTH_BAR": 0.575,
        "CONFIDENCE": 1,
        "bBUCKLING": true,
        "bCALCAXIALFORCE": true
      },
      "NODECONNECTIVITY": "PINNED",
      "bSHOWGRAPHAFTER": true,
      "bSHOWGRAPGHDURING": false
    }
  }
}
```

**GET Response Body**

```json
{
  "POGD": {
    "1": {
      "GEOMNONLINEAR_TYPE": "NONE",
      "INITLOADMETHOD": "PERFORM_ANAL",
      "INITLOAD": [],
      "bCONSIGNOREELEM": true,
      "NONL_OPT": { "SUBSTEP": 10, "MAXITER": 10 },
      "PHOP_OPT": { "BEAM_CORE_SIZE": "AUTO" },
      "NODECONNECTIVITY": "PINNED",
      "bSHOWGRAPHAFTER": true,
      "bSHOWGRAPGHDURING": false
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 푸시오버 해석 제어 데이터 생성 ──────────────────────────
payload = {
    "Assign": {
        "1": {
            "GEOMNONLINEAR_TYPE": "NONE",
            "INITLOADMETHOD": "PERFORM_ANAL",
            "INITLOAD": [],
            "bCONSIGNOREELEM": True,
            "NONL_OPT": {
                "bPERMITFAIL": True,
                "SUBSTEP": 10,
                "MAXITER": 10,
                "bDISPLNORM": True,
                "bFORCENORM": False,
                "bENERGYNORM": False,
                "DISPLNORM": 0.001,
                "FORCENORM": 0.001,
                "ENERGYNORM": 0.001,
                "bSHEARYIELDSTOP": False,
                "BSHEARYIELDSTOPBEAM": True,
                "bSHEARYIELDSTOPWALL": False,
                "bAXIALYIELDSTOP": False,
                "bAXIALYIELDSTOPBEAM": True,
                "bAXIALYIELDSTOPWALL": False,
                "bAXIALYIELDSTOPTRUSS": False,
                "bSUPPORTDZDIRSTOP": False,
                "bSUPPORTSTOPUPLIFTING": False,
                "bSUPPORTSTOPCOLLAPSE": False
            },
            "PHOP_OPT": {
                "bCONSREBARAREA1D": False,
                "BEAM_CORE_SIZE": "AUTO",
                "BEAM_CORE_DIV_Y": 15,
                "BEAM_CORE_DIV_Z": 15,
                "BEAM_COVER_SIZE": "EQUAL",
                "BEAM_COVER_DIV_Y": 15,
                "BEAM_COVER_DIV_Z": 15,
                "bCONSREBARAREAWALL": False,
                "bWALLCONSOUT": True,
                "WALL_CORE_SIZE": "AUTO",
                "WALL_CORE_DIV_Z": 8,
                "WALL_CORE_DIV_Y": 8,
                "WALL_COVER_SIZE": "AUTO",
                "WALL_COVER_DIV_Z": 8,
                "WALL_COVER_DIV_Y": 1,
                "SHEAR_R": 0.4,
                "bASSIGNBYMEMBER": True,
                "bTRI_SYM": True,
                "TRI_TENS_A1": 0.1,
                "TRI_TENS_A2": 0.05,
                "TRI_COMP_A1": 0.1,
                "TRI_COMP_A2": 0.05,
                "bBI_SYM": True,
                "BI_TENS_A1": 0.05,
                "BI_COMP_A1": 0.05,
                "PSPR_APPLY_TYPE": "ASSUME",
                "ELNK_APPLY_TYPE": "APPLY",
                "bUSEAUTOCALCREFERENCE": True,
                "RCDGNCODE": "KISTEC2019",
                "LOC_BEAM": "M",
                "LOC_COLUMN": "I",
                "SF_WALL": 1.6,
                "bSF_BRITTLE": False,
                "SF_BRITTLE": 1.6,
                "bSF_EARTHQUAKE": False,
                "SF_EARTHQUAKE": 0.85,
                "bSF_SMOOTH_BAR": False,
                "SF_SMOOTH_BAR": 0.575,
                "CONFIDENCE": 1,
                "bBUCKLING": True,
                "bCALCAXIALFORCE": True
            },
            "NODECONNECTIVITY": "PINNED",
            "bSHOWGRAPHAFTER": True,
            "bSHOWGRAPGHDURING": False
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/POGD", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 푸시오버 제어 데이터 조회 ────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/POGD", headers=HEADERS)
print("GET:", resp.json())
```

---

## 2. `/db/POGD-M1` — Pushover Global Control (Hyper-S)

> **기능:** Hyper-S(MEC) 솔버 전용 Pushover(정적 비선형 내진성능평가) 해석의 전역 제어 옵션을 정의합니다. 기하비선형 유형, 초기하중 처리, 해석 중단 조건, 반복(Iteration) 제어, 힌지(Hinge) 옵션, 그래프 표시 옵션 등을 설정합니다.

### Input URI

```
{base url}/db/POGD-M1
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "Assign"
  ],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keys are string indices (e.g. \"1\"); each value is a Pushover Global Control settings object.",
      "minProperties": 1,
      "additionalProperties": {
        "type": "object",
        "unevaluatedProperties": false,
        "required": [
          "GEO_NONL_TYPE",
          "INIT_LOAD_TYPE",
          "ITER_CTRL"
        ],
        "allOf": [
          {
            "type": "object",
            "properties": {
              "GEO_NONL_TYPE": {
                "type": "integer",
                "enum": [0, 1, 2],
                "description": "None / P-Delta / Large Displacements"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "INIT_LOAD_TYPE": {
                "type": "integer",
                "enum": [0, 1],
                "description": "Perform Nonlinear Static Analysis for Initial Load / Import Static Analysis / Construction Stage Analysis Results"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "INIT_LOAD_LIST": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "required": ["LC_NAME", "LC_TYPE", "SF"],
                  "properties": {
                    "LC_NAME": {
                      "type": "string",
                      "minLength": 1,
                      "description": "Load Case / Scale Factor / 목록"
                    },
                    "LC_TYPE": {
                      "type": "string",
                      "enum": ["STATIC", "STAGE"],
                      "description": "Load Case / Scale Factor / 목록"
                    },
                    "SF": {
                      "type": "number",
                      "not": { "const": 0 },
                      "description": "Load Case / Scale Factor / 목록"
                    }
                  }
                },
                "description": "Load Case / Scale Factor / 목록 (각 엔트리 {LC_NAME, LC_TYPE, SF}. LC_TYPE='STATIC' 또는 'STAGE')"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "IGNORE_ELEM": {
                "type": "boolean",
                "description": "Consider 'Ignore Elements for Initial Load'"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "ANALYSIS_STOP": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "SHEAR_YIELD": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["OPT_USE"],
                    "properties": {
                      "OPT_USE": {
                        "type": "boolean",
                        "description": "Shear Component Yield / Axial Component Collapse / Support Uplifting-Collapse"
                      },
                      "BEAM_COLUMN": { "type": "boolean", "description": "Beam/Column" },
                      "WALL": { "type": "boolean", "description": "Wall" }
                    },
                    "allOf": [
                      {
                        "description": "If OPT_USE is true, at least one of BEAM_COLUMN or WALL must be true.",
                        "if": {
                          "properties": { "OPT_USE": { "const": true } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "anyOf": [
                            { "properties": { "BEAM_COLUMN": { "const": true } }, "required": ["BEAM_COLUMN"] },
                            { "properties": { "WALL": { "const": true } }, "required": ["WALL"] }
                          ]
                        }
                      },
                      {
                        "description": "If OPT_USE is false, BEAM_COLUMN and WALL must not be provided.",
                        "if": {
                          "properties": { "OPT_USE": { "const": false } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "not": {
                            "anyOf": [
                              { "required": ["BEAM_COLUMN"] },
                              { "required": ["WALL"] }
                            ]
                          }
                        }
                      }
                    ]
                  },
                  "AXIAL_YIELD": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["OPT_USE"],
                    "properties": {
                      "OPT_USE": {
                        "type": "boolean",
                        "description": "Shear Component Yield / Axial Component Collapse / Support Uplifting-Collapse"
                      },
                      "BEAM": { "type": "boolean", "description": "Beam" },
                      "WALL": { "type": "boolean", "description": "Wall" },
                      "TRUSS": { "type": "boolean", "description": "Truss" }
                    },
                    "allOf": [
                      {
                        "description": "If OPT_USE is true, at least one of BEAM, WALL, or TRUSS must be true.",
                        "if": {
                          "properties": { "OPT_USE": { "const": true } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "anyOf": [
                            { "properties": { "BEAM": { "const": true } }, "required": ["BEAM"] },
                            { "properties": { "WALL": { "const": true } }, "required": ["WALL"] },
                            { "properties": { "TRUSS": { "const": true } }, "required": ["TRUSS"] }
                          ]
                        }
                      },
                      {
                        "description": "If OPT_USE is false, BEAM, WALL, and TRUSS must not be provided.",
                        "if": {
                          "properties": { "OPT_USE": { "const": false } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "not": {
                            "anyOf": [
                              { "required": ["BEAM"] },
                              { "required": ["WALL"] },
                              { "required": ["TRUSS"] }
                            ]
                          }
                        }
                      }
                    ]
                  },
                  "SUPPORT_DZ_DIR": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["OPT_USE"],
                    "properties": {
                      "OPT_USE": {
                        "type": "boolean",
                        "description": "Shear Component Yield / Axial Component Collapse / Support Uplifting-Collapse"
                      },
                      "UPLIFT": { "type": "boolean", "description": "Uplift" },
                      "COLLAPSE": { "type": "boolean", "description": "Collapse" }
                    },
                    "allOf": [
                      {
                        "description": "If OPT_USE is true, at least one of UPLIFT or COLLAPSE must be true.",
                        "if": {
                          "properties": { "OPT_USE": { "const": true } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "anyOf": [
                            { "properties": { "UPLIFT": { "const": true } }, "required": ["UPLIFT"] },
                            { "properties": { "COLLAPSE": { "const": true } }, "required": ["COLLAPSE"] }
                          ]
                        }
                      },
                      {
                        "description": "If OPT_USE is false, UPLIFT and COLLAPSE must not be provided.",
                        "if": {
                          "properties": { "OPT_USE": { "const": false } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "not": {
                            "anyOf": [
                              { "required": ["UPLIFT"] },
                              { "required": ["COLLAPSE"] }
                            ]
                          }
                        }
                      }
                    ]
                  }
                },
                "description": "Shear Component Yield / Axial Component Collapse / Support Uplifting-Collapse"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "ITER_CTRL": {
                "type": "object",
                "additionalProperties": false,
                "required": ["MAX_ITER", "NORM_CTRL", "STIFF_UPD_SCHEME"],
                "properties": {
                  "PERMIT_FAIL": {
                    "type": "boolean",
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "MAX_ITER": {
                    "type": "integer",
                    "minimum": 1,
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "NORM_CTRL": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["DISP", "FORCE", "ENERGY"],
                    "properties": {
                      "DISP": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": ["OPT_USE"],
                        "properties": {
                          "OPT_USE": { "type": "boolean", "description": "Norm option on/off" },
                          "VALUE": { "type": "number", "exclusiveMinimum": 0, "description": "Norm tolerance value" }
                        },
                        "allOf": [
                          {
                            "description": "If OPT_USE is true, VALUE is required.",
                            "if": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] },
                            "then": { "required": ["VALUE"] }
                          },
                          {
                            "description": "If OPT_USE is false, VALUE must not be provided.",
                            "if": { "properties": { "OPT_USE": { "const": false } }, "required": ["OPT_USE"] },
                            "then": { "not": { "required": ["VALUE"] } }
                          }
                        ],
                        "description": "Displacement norm"
                      },
                      "FORCE": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": ["OPT_USE"],
                        "properties": {
                          "OPT_USE": { "type": "boolean", "description": "Norm option on/off" },
                          "VALUE": { "type": "number", "exclusiveMinimum": 0, "description": "Norm tolerance value" }
                        },
                        "allOf": [
                          {
                            "description": "If OPT_USE is true, VALUE is required.",
                            "if": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] },
                            "then": { "required": ["VALUE"] }
                          },
                          {
                            "description": "If OPT_USE is false, VALUE must not be provided.",
                            "if": { "properties": { "OPT_USE": { "const": false } }, "required": ["OPT_USE"] },
                            "then": { "not": { "required": ["VALUE"] } }
                          }
                        ],
                        "description": "Force norm"
                      },
                      "ENERGY": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": ["OPT_USE"],
                        "properties": {
                          "OPT_USE": { "type": "boolean", "description": "Norm option on/off" },
                          "VALUE": { "type": "number", "exclusiveMinimum": 0, "description": "Norm tolerance value" }
                        },
                        "allOf": [
                          {
                            "description": "If OPT_USE is true, VALUE is required.",
                            "if": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] },
                            "then": { "required": ["VALUE"] }
                          },
                          {
                            "description": "If OPT_USE is false, VALUE must not be provided.",
                            "if": { "properties": { "OPT_USE": { "const": false } }, "required": ["OPT_USE"] },
                            "then": { "not": { "required": ["VALUE"] } }
                          }
                        ],
                        "description": "Energy norm"
                      }
                    },
                    "anyOf": [
                      { "properties": { "DISP": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] } } },
                      { "properties": { "FORCE": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] } } },
                      { "properties": { "ENERGY": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] } } }
                    ],
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "STIFF_UPD_SCHEME": {
                    "type": "integer",
                    "enum": [0, 1, 2],
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "ITER_BEF_UPDATE": {
                    "type": "integer",
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "MAX_BISECT_LEVEL": {
                    "type": "integer",
                    "default": 5,
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "SMART_BISECT": {
                    "type": "boolean",
                    "default": false,
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "DIVERGENCE_THRESHOLD": {
                    "type": "number",
                    "default": 3,
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "LINE_SEARCH": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["OPT_USE"],
                    "properties": {
                      "OPT_USE": {
                        "type": "boolean",
                        "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                      },
                      "LINE_SEARCH_OPT": {
                        "type": "string",
                        "enum": ["AUTO", "USER"],
                        "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                      },
                      "START_ITER_NO": {
                        "type": "integer",
                        "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                      },
                      "MAX_LINE_SEARCH_ITER": {
                        "type": "integer",
                        "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                      },
                      "LINE_SEARCH_TOL": {
                        "type": "number",
                        "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                      }
                    },
                    "allOf": [
                      {
                        "description": "If OPT_USE is false, LINE_SEARCH detail fields must not be provided.",
                        "if": { "properties": { "OPT_USE": { "const": false } }, "required": ["OPT_USE"] },
                        "then": {
                          "not": {
                            "anyOf": [
                              { "required": ["LINE_SEARCH_OPT"] },
                              { "required": ["START_ITER_NO"] },
                              { "required": ["MAX_LINE_SEARCH_ITER"] },
                              { "required": ["LINE_SEARCH_TOL"] }
                            ]
                          }
                        }
                      },
                      {
                        "description": "If OPT_USE is true, LINE_SEARCH_OPT is required.",
                        "if": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] },
                        "then": { "required": ["LINE_SEARCH_OPT"] }
                      },
                      {
                        "description": "If LINE_SEARCH_OPT is AUTO, START_ITER_NO, MAX_LINE_SEARCH_ITER, and LINE_SEARCH_TOL must not be provided.",
                        "if": { "properties": { "LINE_SEARCH_OPT": { "const": "AUTO" } }, "required": ["LINE_SEARCH_OPT"] },
                        "then": {
                          "not": {
                            "anyOf": [
                              { "required": ["START_ITER_NO"] },
                              { "required": ["MAX_LINE_SEARCH_ITER"] },
                              { "required": ["LINE_SEARCH_TOL"] }
                            ]
                          }
                        }
                      },
                      {
                        "description": "If LINE_SEARCH_OPT is USER, START_ITER_NO, MAX_LINE_SEARCH_ITER, and LINE_SEARCH_TOL are required.",
                        "if": { "properties": { "LINE_SEARCH_OPT": { "const": "USER" } }, "required": ["LINE_SEARCH_OPT"] },
                        "then": { "required": ["START_ITER_NO", "MAX_LINE_SEARCH_ITER", "LINE_SEARCH_TOL"] }
                      }
                    ],
                    "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                  }
                },
                "allOf": [
                  {
                    "description": "If STIFF_UPD_SCHEME is 0, ITER_BEF_UPDATE is required.",
                    "if": { "properties": { "STIFF_UPD_SCHEME": { "const": 0 } }, "required": ["STIFF_UPD_SCHEME"] },
                    "then": { "required": ["ITER_BEF_UPDATE"] }
                  },
                  {
                    "description": "If STIFF_UPD_SCHEME is 1 or 2, ITER_BEF_UPDATE must not be provided.",
                    "if": { "properties": { "STIFF_UPD_SCHEME": { "enum": [1, 2] } }, "required": ["STIFF_UPD_SCHEME"] },
                    "then": { "not": { "required": ["ITER_BEF_UPDATE"] } }
                  }
                ],
                "description": "(복합) (세부 필드는 서브 §4 Iteration Control 과 중복 — 메인 대화상자에서 접근 가능)"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "PO_HINGE_OPT": {
                "type": "object",
                "additionalProperties": false,
                "required": ["ASSIGN_BY_MEMBER", "NONL_TYPE", "TRILINEAR", "BILINEAR", "LOC_BEAM", "CALC_YIELDS"],
                "properties": {
                  "ASSIGN_BY_MEMBER": {
                    "type": "boolean",
                    "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
                  },
                  "NONL_TYPE": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["PSPRING_SUP", "EL"],
                    "properties": {
                      "PSPRING_SUP": { "type": "integer", "enum": [0, 1], "description": "Apply nonlinear / Linear" },
                      "EL": { "type": "integer", "enum": [0, 1], "description": "Apply nonlinear / Linear" }
                    },
                    "description": "Apply nonlinear / Linear"
                  },
                  "TRILINEAR": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["TENS_A1", "TENS_A2", "COMP_A1", "COMP_A2", "SYMMETRIC"],
                    "properties": {
                      "TENS_A1": { "type": "number", "description": "Trilinear default stiffness reduction" },
                      "TENS_A2": { "type": "number", "description": "Trilinear default stiffness reduction" },
                      "COMP_A1": { "type": "number", "description": "Trilinear default stiffness reduction" },
                      "COMP_A2": { "type": "number", "description": "Trilinear default stiffness reduction" },
                      "SYMMETRIC": { "type": "boolean", "description": "Trilinear default stiffness reduction" }
                    },
                    "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
                  },
                  "BILINEAR": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["TENS_A1", "COMP_A1", "SYMMETRIC"],
                    "properties": {
                      "TENS_A1": { "type": "number", "description": "Bilinear default stiffness reduction" },
                      "COMP_A1": { "type": "number", "description": "Bilinear default stiffness reduction" },
                      "SYMMETRIC": { "type": "boolean", "description": "Bilinear default stiffness reduction" }
                    },
                    "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
                  },
                  "LOC_BEAM": {
                    "type": "integer",
                    "enum": [0, 1, 2],
                    "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
                  },
                  "CALC_YIELDS": {
                    "type": "boolean",
                    "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
                  }
                },
                "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "MISC": {
                "type": "object",
                "additionalProperties": false,
                "required": ["SHOW_GRAPH_AFTER", "SHOW_GRAPH_DURING"],
                "properties": {
                  "SHOW_GRAPH_AFTER": { "type": "boolean", "description": "Show Pushover Curve Result After Analysis" },
                  "SHOW_GRAPH_DURING": { "type": "boolean", "description": "Show Pushover Curve during Analyzing" }
                },
                "description": "Pushover Misc Options"
              }
            }
          },
          {
            "description": "If GEO_NONL_TYPE is Large Displacements or P-Delta, INIT_LOAD_TYPE must be 0.",
            "if": {
              "properties": { "GEO_NONL_TYPE": { "enum": [1, 2] } },
              "required": ["GEO_NONL_TYPE"]
            },
            "then": { "properties": { "INIT_LOAD_TYPE": { "const": 0 } } }
          },
          {
            "description": "If INIT_LOAD_TYPE is 1, IGNORE_ELEM must not be provided.",
            "if": {
              "properties": { "INIT_LOAD_TYPE": { "const": 1 } },
              "required": ["INIT_LOAD_TYPE"]
            },
            "then": { "not": { "required": ["IGNORE_ELEM"] } }
          }
        ]
      }
    }
  }
}
```

### Parameters

`Assign` 객체 하위에 `"1"`, `"2"` 등 문자열 인덱스를 키로 하여 각 항목의 Pushover Global Control 설정을 정의합니다.

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 1 | 기하비선형 유형 (None: 0 / Large Displacements: 1 / P-Delta: 2). GEO_NONL_TYPE이 1 또는 2이면 INIT_LOAD_TYPE은 반드시 0이어야 함 | `GEO_NONL_TYPE` | integer (enum) | - | 필수 |
| 2 | 초기하중 유형 (비선형 정적해석 수행: 0 / 정적·시공단계 해석 결과 가져오기: 1) | `INIT_LOAD_TYPE` | integer (enum) | - | 필수 |
| 3 | 초기하중 하중케이스 목록 (INIT_LOAD_TYPE=1일 때 IGNORE_ELEM 지정 불가) | `INIT_LOAD_LIST` | array [object] | - | 선택 |
| 3-1 | └ 하중케이스 이름 (길이 ≥1) | `INIT_LOAD_LIST[].LC_NAME` | string | - | 필수 (배열 사용 시) |
| 3-2 | └ 하중케이스 타입 (Static: STATIC / Stage: STAGE) | `INIT_LOAD_LIST[].LC_TYPE` | string (enum) | - | 필수 (배열 사용 시) |
| 3-3 | └ 배율(Scale Factor), 0 불가 | `INIT_LOAD_LIST[].SF` | number | - | 필수 (배열 사용 시) |
| 4 | 초기하중 산정 시 요소 무시 옵션 (Ignore Elements for Initial Load). INIT_LOAD_TYPE=1이면 제공 불가 | `IGNORE_ELEM` | boolean | - | 선택 |
| 5 | 해석 중단(Analysis Stop) 조건 그룹 | `ANALYSIS_STOP` | object | - | 선택 |
| 5-1 | └ 전단 성분 항복(Shear Component Yield) | `ANALYSIS_STOP.SHEAR_YIELD` | object | - | 선택 |
| 5-1-a | 　　└ 사용 여부 | `ANALYSIS_STOP.SHEAR_YIELD.OPT_USE` | boolean | - | 필수. true이면 BEAM_COLUMN/WALL 중 최소 1개는 true, false이면 둘 다 미기재 |
| 5-1-b | 　　└ Beam/Column | `ANALYSIS_STOP.SHEAR_YIELD.BEAM_COLUMN` | boolean | - | 선택 |
| 5-1-c | 　　└ Wall | `ANALYSIS_STOP.SHEAR_YIELD.WALL` | boolean | - | 선택 |
| 5-2 | └ 축방향 성분 붕괴/좌굴(Axial Component Collapse) | `ANALYSIS_STOP.AXIAL_YIELD` | object | - | 선택 |
| 5-2-a | 　　└ 사용 여부 | `ANALYSIS_STOP.AXIAL_YIELD.OPT_USE` | boolean | - | 필수. true이면 BEAM/WALL/TRUSS 중 최소 1개는 true, false이면 모두 미기재 |
| 5-2-b | 　　└ Beam | `ANALYSIS_STOP.AXIAL_YIELD.BEAM` | boolean | - | 선택 |
| 5-2-c | 　　└ Wall | `ANALYSIS_STOP.AXIAL_YIELD.WALL` | boolean | - | 선택 |
| 5-2-d | 　　└ Truss | `ANALYSIS_STOP.AXIAL_YIELD.TRUSS` | boolean | - | 선택 |
| 5-3 | └ 지점 들뜸/붕괴 : Dz 방향(Support Uplifting/Collapse) | `ANALYSIS_STOP.SUPPORT_DZ_DIR` | object | - | 선택 |
| 5-3-a | 　　└ 사용 여부 | `ANALYSIS_STOP.SUPPORT_DZ_DIR.OPT_USE` | boolean | - | 필수. true이면 UPLIFT/COLLAPSE 중 최소 1개는 true, false이면 둘 다 미기재 |
| 5-3-b | 　　└ Uplift | `ANALYSIS_STOP.SUPPORT_DZ_DIR.UPLIFT` | boolean | - | 선택 |
| 5-3-c | 　　└ Collapse | `ANALYSIS_STOP.SUPPORT_DZ_DIR.COLLAPSE` | boolean | - | 선택 |
| 6 | 반복 제어(Iteration Controls) | `ITER_CTRL` | object | - | 필수 |
| 6-1 | └ 수렴 실패 허용(Permit Convergence Failure) | `ITER_CTRL.PERMIT_FAIL` | boolean | - | 선택 |
| 6-2 | └ 최대 반복횟수(Maximum Iteration), ≥1 | `ITER_CTRL.MAX_ITER` | integer | - | 필수 |
| 6-3 | └ 수렴 기준(Convergence Criteria) | `ITER_CTRL.NORM_CTRL` | object | - | 필수. DISP/FORCE/ENERGY 중 최소 1개는 OPT_USE=true |
| 6-3-a | 　　└ 변위 노름(Displacement norm) | `ITER_CTRL.NORM_CTRL.DISP` | object | - | 필수 |
| 6-3-a-i | 　　　　└ 사용 여부 | `ITER_CTRL.NORM_CTRL.DISP.OPT_USE` | boolean | - | 필수 |
| 6-3-a-ii | 　　　　└ 허용오차 값 (>0). DISP.OPT_USE=true일 때 필수, false이면 제공 불가 | `ITER_CTRL.NORM_CTRL.DISP.VALUE` | number | - | 조건부 필수 |
| 6-3-b | 　　└ 하중 노름(Force norm) | `ITER_CTRL.NORM_CTRL.FORCE` | object | - | 필수 |
| 6-3-b-i | 　　　　└ 사용 여부 | `ITER_CTRL.NORM_CTRL.FORCE.OPT_USE` | boolean | - | 필수 |
| 6-3-b-ii | 　　　　└ 허용오차 값 (>0). FORCE.OPT_USE=true일 때 필수, false이면 제공 불가 | `ITER_CTRL.NORM_CTRL.FORCE.VALUE` | number | - | 조건부 필수 |
| 6-3-c | 　　└ 에너지 노름(Energy norm) | `ITER_CTRL.NORM_CTRL.ENERGY` | object | - | 필수 |
| 6-3-c-i | 　　　　└ 사용 여부 | `ITER_CTRL.NORM_CTRL.ENERGY.OPT_USE` | boolean | - | 필수 |
| 6-3-c-ii | 　　　　└ 허용오차 값 (>0). ENERGY.OPT_USE=true일 때 필수, false이면 제공 불가 | `ITER_CTRL.NORM_CTRL.ENERGY.VALUE` | number | - | 조건부 필수 |
| 6-4 | └ 강성 갱신 방식 (Custom: 0 / Full Newton-Raphson: 1 / Initial Stiffness: 2) | `ITER_CTRL.STIFF_UPD_SCHEME` | integer (enum) | - | 필수 |
| 6-5 | └ 강성 갱신 전 반복횟수. STIFF_UPD_SCHEME=0일 때 필수, 1·2이면 제공 불가 | `ITER_CTRL.ITER_BEF_UPDATE` | integer | - | 조건부 필수 |
| 6-6 | └ 최대 이분(Bisection) 레벨 | `ITER_CTRL.MAX_BISECT_LEVEL` | integer | 5 | 선택 |
| 6-7 | └ Smart Bisection 사용 | `ITER_CTRL.SMART_BISECT` | boolean | false | 선택 |
| 6-8 | └ 발산 임계값(Divergence Threshold) | `ITER_CTRL.DIVERGENCE_THRESHOLD` | number | 3 | 선택 |
| 6-9 | └ Line Search 사용 | `ITER_CTRL.LINE_SEARCH` | object | - | 선택 |
| 6-9-a | 　　└ 사용 여부. false이면 세부 필드 모두 제공 불가, true이면 LINE_SEARCH_OPT 필수 | `ITER_CTRL.LINE_SEARCH.OPT_USE` | boolean | - | 필수 |
| 6-9-b | 　　└ Line Search 옵션 (Auto: AUTO / User: USER). AUTO이면 세부값 제공 불가, USER이면 세부값 모두 필수 | `ITER_CTRL.LINE_SEARCH.LINE_SEARCH_OPT` | string (enum) | - | 조건부 필수 |
| 6-9-c | 　　└ Line Search 시작 반복 횟수 (USER일 때 필수) | `ITER_CTRL.LINE_SEARCH.START_ITER_NO` | integer | - | 조건부 필수 |
| 6-9-d | 　　└ 반복당 최대 Line Search 횟수 (USER일 때 필수) | `ITER_CTRL.LINE_SEARCH.MAX_LINE_SEARCH_ITER` | integer | - | 조건부 필수 |
| 6-9-e | 　　└ Line Search 허용오차 (USER일 때 필수) | `ITER_CTRL.LINE_SEARCH.LINE_SEARCH_TOL` | number | - | 조건부 필수 |
| 7 | Pushover 힌지 데이터 옵션 | `PO_HINGE_OPT` | object | - | 선택 |
| 7-1 | └ 부재에만 힌지 속성 지정 | `PO_HINGE_OPT.ASSIGN_BY_MEMBER` | boolean | - | 필수 |
| 7-2 | └ Skeleton Curve 기본 강성 저감비 (Trilinear) | `PO_HINGE_OPT.TRILINEAR` | object | - | 필수 |
| 7-2-a | 　　└ α1 (+) | `PO_HINGE_OPT.TRILINEAR.TENS_A1` | number | - | 필수 |
| 7-2-b | 　　└ α2 (+) | `PO_HINGE_OPT.TRILINEAR.TENS_A2` | number | - | 필수 |
| 7-2-c | 　　└ α1 (-) | `PO_HINGE_OPT.TRILINEAR.COMP_A1` | number | - | 필수 |
| 7-2-d | 　　└ α2 (-) | `PO_HINGE_OPT.TRILINEAR.COMP_A2` | number | - | 필수 |
| 7-2-e | 　　└ 대칭 여부(SYMMETRIC) | `PO_HINGE_OPT.TRILINEAR.SYMMETRIC` | boolean | - | 필수 |
| 7-3 | └ 힌지 속성 기본 강성 저감비 (Bilinear) | `PO_HINGE_OPT.BILINEAR` | object | - | 필수 |
| 7-3-a | 　　└ α1 (+) | `PO_HINGE_OPT.BILINEAR.TENS_A1` | number | - | 필수 |
| 7-3-b | 　　└ α1 (-) | `PO_HINGE_OPT.BILINEAR.COMP_A1` | number | - | 필수 |
| 7-3-c | 　　└ 대칭 여부(SYMMETRIC) | `PO_HINGE_OPT.BILINEAR.SYMMETRIC` | boolean | - | 필수 |
| 7-4 | └ 점 스프링 지점 & 탄성링크 비선형 유형 | `PO_HINGE_OPT.NONL_TYPE` | object | - | 필수 |
| 7-4-a | 　　└ 점 스프링 지점 적용 방식 (Apply Nonlinear: 0 / Linear: 1) | `PO_HINGE_OPT.NONL_TYPE.PSPRING_SUP` | integer (enum) | - | 필수 |
| 7-4-b | 　　└ 탄성링크 적용 방식 (Apply Nonlinear: 0 / Linear: 1) | `PO_HINGE_OPT.NONL_TYPE.EL` | integer (enum) | - | 필수 |
| 7-5 | └ 분포힌지 기준 위치 (I-End: 0 / Mid-span: 1 / J-End: 2) | `PO_HINGE_OPT.LOC_BEAM` | integer (enum) | - | 필수 |
| 7-6 | └ 좌굴 고려 Beam 항복면 계산 | `PO_HINGE_OPT.CALC_YIELDS` | boolean | - | 필수 |
| 8 | Pushover 기타(Misc) 옵션 | `MISC` | object | - | 선택 |
| 8-1 | └ 해석 후 Pushover 곡선 결과 표시 | `MISC.SHOW_GRAPH_AFTER` | boolean | - | 필수 |
| 8-2 | └ 해석 중 Pushover 곡선 표시 | `MISC.SHOW_GRAPH_DURING` | boolean | - | 필수 |

> ⚠️ **2026-08-26 확인:** `GEO_NONL_TYPE`의 enum 순서를 이전엔 None:0/P-Delta:1/Large
> Displacements:2로 잘못 기재했다. 원문 JSON Schema의 description은 단어 나열 순서가
> "None / P-Delta / Large Displacements"라 이를 그대로 따른 것이 원인으로 보이나, 원문
> Specifications 표는 명시적으로 None:0/**Large Displacements:1**/**P-Delta:2**로 번호를
> 매겨 놓았다(스키마 설명 문구와 표가 서로 모순 — 표가 우선). 09장 `/db/THGC-M1`의 동명 필드
> `GEO_NONL_TYPE`도 0=None/1=Large Disp/2=P-Delta로 동일 순서라 교차 확인됨(아티클 id
> `56511008007705`).

### Request / Response JSON

**PUT Request Body**
```json
{
  "Assign": {
    "1": {
      "GEO_NONL_TYPE": 0,
      "INIT_LOAD_TYPE": 0,
      "INIT_LOAD_LIST": [
        { "LC_NAME": "DL", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "LL", "LC_TYPE": "STATIC", "SF": 0.25 },
        { "LC_NAME": "EQX", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "EQY", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "STAGE_FINAL", "LC_TYPE": "STAGE", "SF": 1 }
      ],
      "IGNORE_ELEM": true,
      "ANALYSIS_STOP": {
        "SHEAR_YIELD": { "OPT_USE": true, "BEAM_COLUMN": true, "WALL": true },
        "AXIAL_YIELD": { "OPT_USE": true, "BEAM": true, "WALL": true, "TRUSS": true },
        "SUPPORT_DZ_DIR": { "OPT_USE": true, "UPLIFT": true, "COLLAPSE": true }
      },
      "ITER_CTRL": {
        "PERMIT_FAIL": false,
        "MAX_ITER": 30,
        "NORM_CTRL": {
          "DISP": { "OPT_USE": true, "VALUE": 0.001 },
          "FORCE": { "OPT_USE": true, "VALUE": 0.001 },
          "ENERGY": { "OPT_USE": true, "VALUE": 0.0001 }
        },
        "STIFF_UPD_SCHEME": 0,
        "ITER_BEF_UPDATE": 5,
        "MAX_BISECT_LEVEL": 8,
        "SMART_BISECT": true,
        "DIVERGENCE_THRESHOLD": 3,
        "LINE_SEARCH": {
          "OPT_USE": true,
          "LINE_SEARCH_OPT": "USER",
          "START_ITER_NO": 3,
          "MAX_LINE_SEARCH_ITER": 10,
          "LINE_SEARCH_TOL": 0.8
        }
      },
      "PO_HINGE_OPT": {
        "ASSIGN_BY_MEMBER": true,
        "NONL_TYPE": { "PSPRING_SUP": 1, "EL": 1 },
        "TRILINEAR": { "TENS_A1": 0.1, "TENS_A2": 0.05, "COMP_A1": 0.1, "COMP_A2": 0.05, "SYMMETRIC": true },
        "BILINEAR": { "TENS_A1": 0.1, "COMP_A1": 0.1, "SYMMETRIC": true },
        "LOC_BEAM": 0,
        "CALC_YIELDS": true
      },
      "MISC": {
        "SHOW_GRAPH_AFTER": true,
        "SHOW_GRAPH_DURING": true
      }
    }
  }
}
```

**GET Response Body**
```json
{
  "POGD-M1": {
    "1": {
      "GEO_NONL_TYPE": 0,
      "INIT_LOAD_TYPE": 0,
      "INIT_LOAD_LIST": [
        { "LC_NAME": "DL", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "LL", "LC_TYPE": "STATIC", "SF": 0.25 },
        { "LC_NAME": "EQX", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "EQY", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "STAGE_FINAL", "LC_TYPE": "STAGE", "SF": 1 }
      ],
      "IGNORE_ELEM": true,
      "ANALYSIS_STOP": {
        "SHEAR_YIELD": { "OPT_USE": true, "BEAM_COLUMN": true, "WALL": true },
        "AXIAL_YIELD": { "OPT_USE": true, "BEAM": true, "WALL": true, "TRUSS": true },
        "SUPPORT_DZ_DIR": { "OPT_USE": true, "UPLIFT": true, "COLLAPSE": true }
      },
      "ITER_CTRL": {
        "PERMIT_FAIL": false,
        "MAX_ITER": 30,
        "NORM_CTRL": {
          "DISP": { "OPT_USE": true, "VALUE": 0.001 },
          "FORCE": { "OPT_USE": true, "VALUE": 0.001 },
          "ENERGY": { "OPT_USE": true, "VALUE": 0.0001 }
        },
        "STIFF_UPD_SCHEME": 0,
        "ITER_BEF_UPDATE": 5,
        "MAX_BISECT_LEVEL": 8,
        "SMART_BISECT": true,
        "DIVERGENCE_THRESHOLD": 3,
        "LINE_SEARCH": {
          "OPT_USE": true,
          "LINE_SEARCH_OPT": "USER",
          "START_ITER_NO": 3,
          "MAX_LINE_SEARCH_ITER": 10,
          "LINE_SEARCH_TOL": 0.8
        }
      },
      "PO_HINGE_OPT": {
        "ASSIGN_BY_MEMBER": true,
        "NONL_TYPE": { "PSPRING_SUP": 1, "EL": 1 },
        "TRILINEAR": { "TENS_A1": 0.1, "TENS_A2": 0.05, "COMP_A1": 0.1, "COMP_A2": 0.05, "SYMMETRIC": true },
        "BILINEAR": { "TENS_A1": 0.1, "COMP_A1": 0.1, "SYMMETRIC": true },
        "LOC_BEAM": 0,
        "CALC_YIELDS": true
      },
      "MISC": {
        "SHOW_GRAPH_AFTER": true,
        "SHOW_GRAPH_DURING": true
      }
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── PUT: Pushover Global Control(Hyper-S) 등록/수정 ───────────────
def put_pushover_global_control():
    payload = {
        "Assign": {
            "1": {
                "GEO_NONL_TYPE": 0,       # None
                "INIT_LOAD_TYPE": 0,      # 비선형 정적해석으로 초기하중 산정
                "INIT_LOAD_LIST": [
                    {"LC_NAME": "DL", "LC_TYPE": "STATIC", "SF": 1},
                    {"LC_NAME": "LL", "LC_TYPE": "STATIC", "SF": 0.25},
                    {"LC_NAME": "EQX", "LC_TYPE": "STATIC", "SF": 1},
                    {"LC_NAME": "EQY", "LC_TYPE": "STATIC", "SF": 1},
                    {"LC_NAME": "STAGE_FINAL", "LC_TYPE": "STAGE", "SF": 1}
                ],
                "IGNORE_ELEM": True,
                "ANALYSIS_STOP": {
                    "SHEAR_YIELD": {"OPT_USE": True, "BEAM_COLUMN": True, "WALL": True},
                    "AXIAL_YIELD": {"OPT_USE": True, "BEAM": True, "WALL": True, "TRUSS": True},
                    "SUPPORT_DZ_DIR": {"OPT_USE": True, "UPLIFT": True, "COLLAPSE": True}
                },
                "ITER_CTRL": {
                    "PERMIT_FAIL": False,
                    "MAX_ITER": 30,
                    "NORM_CTRL": {
                        "DISP": {"OPT_USE": True, "VALUE": 0.001},
                        "FORCE": {"OPT_USE": True, "VALUE": 0.001},
                        "ENERGY": {"OPT_USE": True, "VALUE": 0.0001}
                    },
                    "STIFF_UPD_SCHEME": 0,       # Custom -> ITER_BEF_UPDATE 필수
                    "ITER_BEF_UPDATE": 5,
                    "MAX_BISECT_LEVEL": 8,
                    "SMART_BISECT": True,
                    "DIVERGENCE_THRESHOLD": 3,
                    "LINE_SEARCH": {
                        "OPT_USE": True,
                        "LINE_SEARCH_OPT": "USER",   # USER -> 세부값 필수
                        "START_ITER_NO": 3,
                        "MAX_LINE_SEARCH_ITER": 10,
                        "LINE_SEARCH_TOL": 0.8
                    }
                },
                "PO_HINGE_OPT": {
                    "ASSIGN_BY_MEMBER": True,
                    "NONL_TYPE": {"PSPRING_SUP": 1, "EL": 1},
                    "TRILINEAR": {"TENS_A1": 0.1, "TENS_A2": 0.05, "COMP_A1": 0.1, "COMP_A2": 0.05, "SYMMETRIC": True},
                    "BILINEAR": {"TENS_A1": 0.1, "COMP_A1": 0.1, "SYMMETRIC": True},
                    "LOC_BEAM": 0,
                    "CALC_YIELDS": True
                },
                "MISC": {
                    "SHOW_GRAPH_AFTER": True,
                    "SHOW_GRAPH_DURING": True
                }
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/POGD-M1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("PUT:", resp.status_code, resp.json())

# ── GET: Pushover Global Control(Hyper-S) 조회 ────────────────────
def get_pushover_global_control():
    resp = requests.get(f"{BASE_URL}/db/POGD-M1", headers=HEADERS)
    resp.raise_for_status()
    print("GET:", resp.json())

put_pushover_global_control()
get_pushover_global_control()
```

---

## 3. `/db/IEPI` — Ignore Elements for Pushover Initial Load

> **기능:** 비선형(푸시오버) 해석의 초기하중 계산 시 무시할 요소를 지정합니다. Assign Key는 요소 ID입니다.

### Input URI

```
{base url}/db/IEPI
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "IEPI": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "B_IGNORE": { "description": "IgnoreElementsforNL.AnalysisInitialLoad", "type": "boolean" }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 비선형 해석 초기하중용 요소 무시 여부 | `"B_IGNORE"` | Boolean | `false` | Optional |

> **참고:** Assign Key는 **요소 ID**입니다 (일련번호 아님).

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "59": { "B_IGNORE": true },
    "60": { "B_IGNORE": true },
    "61": { "B_IGNORE": true },
    "62": { "B_IGNORE": true },
    "63": { "B_IGNORE": true },
    "64": { "B_IGNORE": true },
    "65": { "B_IGNORE": true },
    "66": { "B_IGNORE": true },
    "67": { "B_IGNORE": true },
    "68": { "B_IGNORE": true },
    "69": { "B_IGNORE": true },
    "70": { "B_IGNORE": true }
  }
}
```

**GET Response Body**

```json
{
  "IEPI": {
    "59": { "B_IGNORE": true },
    "60": { "B_IGNORE": true }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 초기하중 계산에서 특정 요소들 무시 지정 ─────────────────
ignore_elements = [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
payload = {
    "Assign": {
        str(elem_id): {"B_IGNORE": True} for elem_id in ignore_elements
    }
}
resp = requests.post(f"{BASE_URL}/db/IEPI", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 무시 요소 목록 조회 ───────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/IEPI", headers=HEADERS)
ignored = resp.json().get("IEPI", {})
print(f"무시된 요소 수: {len(ignored)}")
print(f"요소 ID 목록: {list(ignored.keys())}")

# ── DELETE: 특정 요소를 무시 목록에서 제거 ─────────────────────────
resp = requests.delete(f"{BASE_URL}/db/IEPI/59", headers=HEADERS)
print("DELETE:", resp.status_code)
```

---

## 4. `/db/PHGE` — Assign Pushover Hinge Properties

> **기능:** 요소에 푸시오버 힌지 속성을 배정합니다. Assign Key는 배정 순번이며, 요소 ID(`ID`)와 요소 타입(`TYPE`)을 별도 필드로 지정합니다.

### Input URI

```
{base url}/db/PHGE
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "PHGE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "ID": { "description": "ID", "type": "integer" },
      "TYPE": { "description": "ElementType", "type": "string" },
      "HINGE_TYPE": { "description": "PushoverHingeType", "type": "string" },
      "FIBER_KEY": { "description": "FiberKey", "type": "integer" }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 요소 ID | `"ID"` | Integer | — | **Required** |
| 2 | 요소 타입 · Beam/Column: `"BEAM"` / Wall(⚠️ Gen NX 전용): `"WALL"` / Truss: `"TRUSS"` / General Link: `"G-LINK"` | `"TYPE"` | String | — | **Required** |
| 3 | 푸시오버 힌지 타입 (예: `"Myz_15"`) | `"HINGE_TYPE"` | String | — | **Required** |
| 4 | 파이버 키 | `"FIBER_KEY"` | Integer | — | **Required** |

> ⚠️ **2026-08-26 확인:** `TYPE`은 원문에서 `"BEAM"`/`"WALL"`/`"TRUSS"`/`"G-LINK"` 4개 값으로
> 한정된 enum이며, `"WALL"`에는 원문상 "MIDAS GEN NX only" 아이콘이 붙어 있다 — 이전 문서는
> "예:" 표기로 비한정 나열하며 `"G-LINK"`를 누락하고 있었다(아티클 id `35992838417049`).

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "15": {
      "ID": 1,
      "TYPE": "BEAM",
      "HINGE_TYPE": "Myz_15",
      "FIBER_KEY": 0
    }
  }
}
```

**GET Response Body**

```json
{
  "PHGE": {
    "15": {
      "ID": 1,
      "TYPE": "BEAM",
      "HINGE_TYPE": "Myz_15",
      "FIBER_KEY": 0
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 요소에 푸시오버 힌지 속성 배정 ──────────────────────────
payload = {
    "Assign": {
        "15": {
            "ID": 1,
            "TYPE": "BEAM",
            "HINGE_TYPE": "Myz_15",
            "FIBER_KEY": 0
        },
        "16": {
            "ID": 2,
            "TYPE": "BEAM",
            "HINGE_TYPE": "Myz_15",
            "FIBER_KEY": 0
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/PHGE", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 배정된 힌지 속성 조회 ─────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/PHGE", headers=HEADERS)
hinges = resp.json().get("PHGE", {})
for key, val in hinges.items():
    print(f"  [{key}] Element ID={val['ID']} ({val['TYPE']}) → {val['HINGE_TYPE']}")
```

---

## 5. `/db/POLC` — Pushover Load Cases

> **기능:** 푸시오버(정적 비선형) 하중케이스를 정의합니다. 증분 방법(하중 제어/변위 제어), 해석 정지 조건, 하중 패턴(정적 하중/균등 가속도/모드 형상/정규화 모드 형상)을 설정합니다.

### Input URI

```
{base url}/db/POLC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "POLC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "LCNAME": { "description": "LoadCaseName", "type": "string" },
      "DESC": { "description": "Description", "type": "string" },
      "INCRE_STEP": { "description": "IncrementSteps", "type": "integer" },
      "bCONS_PDELTA": { "description": "ConsiderP-DeltaEffect", "type": "boolean" },
      "bUSEINITIAL": { "description": "UseInitialLoad", "type": "boolean" },
      "bREACOUTPUT": { "description": "CumulativeReaction/StoryShearbyInitialLoad", "type": "boolean" },
      "INCRE_METHOD": { "description": "IncrementMethod", "type": "string" },
      "STEPCTRLOPTION": { "description": "SteppingControlOption", "type": "string" },
      "INCFUNC_KEY": { "description": "IncrementalControlFunctionKey", "type": "integer" },
      "STIFF_RATIO": { "description": "AnalysisStoppingConditionCurrentStiffnessRatio", "type": "number" },
      "bLIMITDEFORMANGLE": { "description": "UseLimitInter-StoryDeformationAngle", "type": "boolean" },
      "LIMITDEFORMANGLE": { "description": "LimitInter-StoryDeformationAngle(1/[rad])", "type": "number" },
      "bDRIFTMAX": { "description": "MaximumDriftofAllVerticalElements", "type": "boolean" },
      "bDRIFTCENTER": { "description": "DriftattheCenterofFloorDiaphragm(StoryCenter)", "type": "boolean" },
      "bDRIFTAVER": { "description": "DriftcalculatedbyAverageDisplacementofStory", "type": "boolean" },
      "DISPCTRLOPTION": { "description": "DisplacementControlOption", "type": "string" },
      "GLOBAL_MAX_DISP": { "description": "GlobalMaxTranslationalDisplacement", "type": "number" },
      "MASTERNODE": { "description": "MasterNodeKey", "type": "integer" },
      "MASTERDIRECTION": { "description": "MasterNodeDirection", "type": "string" },
      "MASTERMAXDISP": { "description": "MasterNodeDisplacement", "type": "number" },
      "LOADPATTERNTYPE": { "description": "LoadPatternType", "type": "string" },
      "LOADPATTERN": {
        "description": "LoadPatternDataList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "LCNAME": { "description": "LoadCaseName(ifUsedLoadPattern=LOAD)", "type": "string" },
            "DIR": { "description": "Direction(ifUsedLoadPattern=ACC)", "type": "string" },
            "MODE": { "description": "ModeNumber(ifUsedLoadPattern=MODE,NOR_MODE)", "type": "integer" },
            "SF": { "description": "ScaleFactor", "type": "number" }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 설명 | Key | Value 타입 | 기본값 | 필수 |
|-----|------|-----|-----------|--------|------|
| 1 | 하중케이스 이름 | `"LCNAME"` | String | — | **Required** |
| 2 | 설명 | `"DESC"` | String | `""` | Optional |
| 3 | 증분 스텝 수 | `"INCRE_STEP"` | Integer | — | **Required** |
| 4 | P-Delta 효과 고려 | `"bCONS_PDELTA"` | Boolean | `false` | **Required** |
| 5 | 초기하중 사용 여부 | `"bUSEINITIAL"` | Boolean | `false` | Optional |
| 6 | 초기하중에 의한 누적 반력/층전단력 출력 | `"bREACOUTPUT"` | Boolean | `false` | Optional |
| 7 | 증분 방법 · 하중제어: `"LOAD"` / 변위제어: `"DISP"` | `"INCRE_METHOD"` | String | — | **Required** |
| 8 | 스테핑 제어 옵션(`INCRE_METHOD="LOAD"`일 때) · 자동: `"AUTO"` / 등분할(1/nstep): `"EQUAL"` / 증분제어함수: `"INC_FUNC"` | `"STEPCTRLOPTION"` | String | — | **Required** |
| 9 | 증분제어함수 키 (`STEPCTRLOPTION="INC_FUNC"`일 때) | `"INCFUNC_KEY"` | Integer | — | **Required** |
| 10 | 현재 강성비(Cs) (`INCRE_METHOD="LOAD"`일 때) | `"STIFF_RATIO"` | Number | — | **Required** |
| 11 | 변위 제어 옵션(`INCRE_METHOD="DISP"`일 때) · 전체: `"GLOBAL"` / 마스터 노드: `"NODE"` | `"DISPCTRLOPTION"` | String | — | **Required** |
| 12 | 최대 병진 변위(`DISPCTRLOPTION="GLOBAL"`) | `"GLOBAL_MAX_DISP"` | Number | — | **Required** |
| 13 | 마스터 노드 ID(`DISPCTRLOPTION="NODE"`) | `"MASTERNODE"` | Integer | — | **Required** |
| 14 | 마스터 노드 방향 · `"DX"` / `"DY"` / `"DZ"` | `"MASTERDIRECTION"` | String | — | **Required** |
| 15 | 마스터 노드 최대 변위 | `"MASTERMAXDISP"` | Number | — | **Required** |
| 16 | 층간변형각 제한 사용 | `"bLIMITDEFORMANGLE"` | Boolean | `false` | Optional |
| 17 | 층간변형각 제한값 (1/[rad]) | `"LIMITDEFORMANGLE"` | Number | — | **Required** |
| 18 | 모든 수직요소의 최대 층간변위 | `"bDRIFTMAX"` | Boolean | `false` | Optional |
| 19 | 바닥 다이아프램 중심 층간변위 | `"bDRIFTCENTER"` | Boolean | `false` | Optional |
| 20 | 층 평균변위로 계산된 층간변위 | `"bDRIFTAVER"` | Boolean | `false` | Optional |
| 21 | 하중 패턴 타입 · 정적하중: `"LOAD"` / 균등가속도: `"ACC"` / 모드형상: `"MODE"` / 정규화모드형상×질량: `"NOR_MODE"` | `"LOADPATTERNTYPE"` | String | — | **Required** |
| 22 | 하중 패턴 목록 | `"LOADPATTERN"` | Array [Object] | — | **Required** |

**`LOADPATTERN` 배열 항목 – `LOADPATTERNTYPE` 별 필드**

| `LOADPATTERNTYPE` | 필드 | 설명 | 타입 |
|--------------------|------|------|------|
| `"LOAD"` (정적 하중케이스) | `LCNAME` | 하중케이스명 | String |
| `"LOAD"` | `SF` | 축척계수 | Number |
| `"ACC"` (균등 가속도) | `DIR` · `"DX"`/`"DY"`/`"DZ"` | 방향 | String |
| `"ACC"` | `SF` | 축척계수 | Number |
| `"MODE"` / `"NOR_MODE"` (모드형상) | `MODE` | 모드 번호 | Integer |
| `"MODE"` / `"NOR_MODE"` | `SF` | 축척계수 | Number |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "LCNAME": "Mode_X",
      "DESC": "",
      "INCRE_STEP": 10,
      "bCONS_PDELTA": true,
      "bUSEINITIAL": false,
      "bREACOUTPUT": false,
      "INCRE_METHOD": "DISP",
      "STEPCTRLOPTION": "AUTO",
      "INCFUNC_KEY": 0,
      "STIFF_RATIO": 0,
      "bLIMITDEFORMANGLE": true,
      "LIMITDEFORMANGLE": 10,
      "bDRIFTMAX": true,
      "bDRIFTCENTER": false,
      "bDRIFTAVER": false,
      "DISPCTRLOPTION": "NODE",
      "GLOBAL_MAX_DISP": 0,
      "MASTERNODE": 134,
      "MASTERDIRECTION": "DX",
      "MASTERMAXDISP": 1,
      "LOADPATTERNTYPE": "MODE",
      "LOADPATTERN": [
        { "MODE": 1, "SF": 1 }
      ]
    },
    "2": {
      "LCNAME": "Uni_X",
      "DESC": "",
      "INCRE_STEP": 10,
      "bCONS_PDELTA": false,
      "bUSEINITIAL": false,
      "bREACOUTPUT": false,
      "INCRE_METHOD": "LOAD",
      "STEPCTRLOPTION": "EQUAL",
      "INCFUNC_KEY": 0,
      "STIFF_RATIO": 0,
      "bLIMITDEFORMANGLE": true,
      "LIMITDEFORMANGLE": 10,
      "bDRIFTMAX": true,
      "bDRIFTCENTER": false,
      "bDRIFTAVER": false,
      "DISPCTRLOPTION": "GLOBAL",
      "GLOBAL_MAX_DISP": 0,
      "MASTERNODE": 0,
      "MASTERDIRECTION": "",
      "MASTERMAXDISP": 0,
      "LOADPATTERNTYPE": "ACC",
      "LOADPATTERN": [
        { "DIR": "DX", "SF": 1 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "POLC": {
    "1": {
      "LCNAME": "Mode_X",
      "INCRE_STEP": 10,
      "INCRE_METHOD": "DISP",
      "DISPCTRLOPTION": "NODE",
      "MASTERNODE": 134,
      "MASTERDIRECTION": "DX",
      "MASTERMAXDISP": 1,
      "LOADPATTERNTYPE": "MODE",
      "LOADPATTERN": [ { "MODE": 1, "SF": 1 } ]
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 푸시오버 하중케이스 4종 생성 (모드형상 X/Y, 균등하중 X/Y) ──
payload = {
    "Assign": {
        "1": {
            "LCNAME": "Mode_X", "DESC": "", "INCRE_STEP": 10,
            "bCONS_PDELTA": True, "bUSEINITIAL": False, "bREACOUTPUT": False,
            "INCRE_METHOD": "DISP", "STEPCTRLOPTION": "AUTO", "INCFUNC_KEY": 0,
            "STIFF_RATIO": 0,
            "bLIMITDEFORMANGLE": True, "LIMITDEFORMANGLE": 10,
            "bDRIFTMAX": True, "bDRIFTCENTER": False, "bDRIFTAVER": False,
            "DISPCTRLOPTION": "NODE", "GLOBAL_MAX_DISP": 0,
            "MASTERNODE": 134, "MASTERDIRECTION": "DX", "MASTERMAXDISP": 1,
            "LOADPATTERNTYPE": "MODE",
            "LOADPATTERN": [{"MODE": 1, "SF": 1}]
        },
        "2": {
            "LCNAME": "Mode_Y", "DESC": "", "INCRE_STEP": 10,
            "bCONS_PDELTA": True, "bUSEINITIAL": False, "bREACOUTPUT": False,
            "INCRE_METHOD": "DISP", "STEPCTRLOPTION": "AUTO", "INCFUNC_KEY": 0,
            "STIFF_RATIO": 0,
            "bLIMITDEFORMANGLE": True, "LIMITDEFORMANGLE": 10,
            "bDRIFTMAX": True, "bDRIFTCENTER": False, "bDRIFTAVER": False,
            "DISPCTRLOPTION": "NODE", "GLOBAL_MAX_DISP": 0,
            "MASTERNODE": 134, "MASTERDIRECTION": "DY", "MASTERMAXDISP": 1,
            "LOADPATTERNTYPE": "MODE",
            "LOADPATTERN": [{"MODE": 2, "SF": 1}]
        },
        "3": {
            "LCNAME": "Uni_X", "DESC": "", "INCRE_STEP": 10,
            "bCONS_PDELTA": False, "bUSEINITIAL": False, "bREACOUTPUT": False,
            "INCRE_METHOD": "LOAD", "STEPCTRLOPTION": "EQUAL", "INCFUNC_KEY": 0,
            "STIFF_RATIO": 0,
            "bLIMITDEFORMANGLE": True, "LIMITDEFORMANGLE": 10,
            "bDRIFTMAX": True, "bDRIFTCENTER": False, "bDRIFTAVER": False,
            "DISPCTRLOPTION": "GLOBAL", "GLOBAL_MAX_DISP": 0,
            "MASTERNODE": 0, "MASTERDIRECTION": "", "MASTERMAXDISP": 0,
            "LOADPATTERNTYPE": "ACC",
            "LOADPATTERN": [{"DIR": "DX", "SF": 1}]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/POLC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 하중케이스 조회 ──────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/POLC", headers=HEADERS)
cases = resp.json().get("POLC", {})
for key, val in cases.items():
    print(f"  [{key}] {val['LCNAME']} | {val['INCRE_METHOD']} 제어 | 패턴={val['LOADPATTERNTYPE']}")
```

---

## 6. `/db/POLC-M1` — Pushover Load Case (Hyper-S)

> **기능:** Hyper-S(MEC) 솔버 전용 Pushover(정적 비선형) 해석에 사용되는 하중케이스(제어 방식, 증분 단계, 하중 패턴 등)를 정의합니다.

### Input URI

```
{base url}/db/POLC-M1
```

### Active Methods

`GET` · `PUT` · `DELETE`

> ⚠️ **2026-08-26 확인:** 원문 아티클의 Active Methods 표는 `POST, GET, PUT, DELETE`로
> 표기돼 있으나(아티클 id `56506753403673`), 이 챕터의 다른 모든 Hyper-S(`-M1`) 엔드포인트와
> 챕터 서두의 안내("Hyper-S 솔버 전용 엔드포인트는 POST를 지원하지 않습니다")가 일관되게
> POST 미지원을 전제한다. 원문이 다른 엔드포인트용 템플릿을 복사하며 트리밍하지 않은 것인지,
> 실제로 이 엔드포인트만 POST를 지원하는지 원문만으로는 판단할 수 없어 실기 확인 전까지
> `GET`/`PUT`/`DELETE`로 유지한다.

### JSON Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "Assign"
  ],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keys are string indices; each value is a Pushover Load Case (Add/Modify) request item.",
      "minProperties": 1,
      "additionalProperties": {
        "type": "object",
        "unevaluatedProperties": false,
        "allOf": [
          {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "LCNAME",
              "INCRE_STEP",
              "NLTYPE",
              "bUSEINITIAL",
              "INCRE_METHOD",
              "CTRL_OPT",
              "LOADPATTERNTYPE",
              "LOADPATTERN"
            ],
            "properties": {
              "LCNAME": {
                "type": "string",
                "description": "Name (길이 1~20, 중복 불가)"
              },
              "DESC": {
                "type": "string",
                "default": "",
                "description": "Description (길이 ≤80)"
              },
              "INCRE_STEP": {
                "type": "integer",
                "minimum": 1,
                "description": "Increment Steps (nstep) (값 > 0. UI 기본 20)"
              },
              "NLTYPE": {
                "type": "string",
                "enum": ["NONE", "PDELTA", "LARGE"],
                "description": "None / P-Delta / Large Displacements (UI 3개 라디오가 단일 enum으로 병합)"
              },
              "bUSEINITIAL": {
                "type": "boolean",
                "description": "Use Initial Load (true일 때 bREACOUTPUT 필수)"
              },
              "bREACOUTPUT": {
                "type": "boolean",
                "description": "Cumulative Reaction / Story Shear (bUSEINITIAL == false 일 때 제공 시 오류)"
              },
              "INCRE_METHOD": {
                "type": "string",
                "enum": ["LOAD", "DISP"],
                "description": "Load Control / Displacement Control (UI 2개 라디오가 단일 enum으로 병합)"
              },
              "CTRL_OPT": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "STEPCTRLOPTION": {
                    "type": "string",
                    "enum": ["AUTO", "EQUAL", "INC_FUNC"],
                    "description": "Auto-Stepping Control (LOAD 분기)"
                  },
                  "INCFUNC_NAME": {
                    "type": "string",
                    "description": "Increment Function Name (POFC 이름 참조)"
                  },
                  "DISPCTRLOPTION": {
                    "type": "string",
                    "enum": ["GLOBAL", "NODE"],
                    "description": "Global / Master Node (DISP 분기)"
                  },
                  "GLOBAL_MAX_DISP": {
                    "type": "number",
                    "exclusiveMinimum": 0,
                    "description": "Max. Translational Displacement (값 > 0 필수)"
                  },
                  "MASTERNODE": {
                    "type": "integer",
                    "minimum": 1,
                    "description": "Node (ExistNode 통과 필요)"
                  },
                  "MASTERDIRECTION": {
                    "type": "string",
                    "enum": ["DX", "DY", "DZ"],
                    "description": "Direction"
                  },
                  "MASTERMAXDISP": {
                    "type": "number",
                    "not": { "const": 0 },
                    "description": "Max. Displacement (값 != 0.0 필수)"
                  },
                  "STIFF_RATIO": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 100,
                    "description": "Current Stiffness Ratio (Cs) ([0, 100] 범위)"
                  }
                },
                "allOf": [
                  {
                    "description": "When STEPCTRLOPTION = INC_FUNC, INCFUNC_NAME is required",
                    "if": { "properties": { "STEPCTRLOPTION": { "const": "INC_FUNC" } }, "required": ["STEPCTRLOPTION"] },
                    "then": { "required": ["INCFUNC_NAME"] }
                  },
                  {
                    "description": "When STEPCTRLOPTION = AUTO or EQUAL, INCFUNC_NAME must not be provided",
                    "if": { "properties": { "STEPCTRLOPTION": { "enum": ["AUTO", "EQUAL"] } }, "required": ["STEPCTRLOPTION"] },
                    "then": { "not": { "required": ["INCFUNC_NAME"] } }
                  },
                  {
                    "description": "When DISPCTRLOPTION = GLOBAL, GLOBAL_MAX_DISP is required and node-control fields must not be provided",
                    "if": { "properties": { "DISPCTRLOPTION": { "const": "GLOBAL" } }, "required": ["DISPCTRLOPTION"] },
                    "then": {
                      "required": ["GLOBAL_MAX_DISP"],
                      "not": {
                        "anyOf": [
                          { "required": ["MASTERNODE"] },
                          { "required": ["MASTERDIRECTION"] },
                          { "required": ["MASTERMAXDISP"] }
                        ]
                      }
                    }
                  },
                  {
                    "description": "When DISPCTRLOPTION = NODE, MASTERNODE, MASTERDIRECTION, and MASTERMAXDISP are required and GLOBAL_MAX_DISP must not be provided",
                    "if": { "properties": { "DISPCTRLOPTION": { "const": "NODE" } }, "required": ["DISPCTRLOPTION"] },
                    "then": {
                      "required": ["MASTERNODE", "MASTERDIRECTION", "MASTERMAXDISP"],
                      "not": { "required": ["GLOBAL_MAX_DISP"] }
                    }
                  }
                ],
                "description": "Control Option (INCRE_METHOD 분기 컨테이너)"
              },
              "LOADPATTERNTYPE": {
                "type": "string",
                "enum": ["LOAD", "ACC", "MODE", "NOR_MODE"],
                "description": "Load Type (배열 크기 제약: ACC/MODE/NOR_MODE는 배열 원소 1개만 허용)"
              },
              "LOADPATTERN": {
                "type": "array",
                "minItems": 1,
                "description": "Load Pattern 배열 (크기 ≥ 1)",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "LCNAME": {
                      "type": "string",
                      "description": "Load Case (ExistStld 통과 필요, Static Load Case 이름)"
                    },
                    "DIR": {
                      "type": "string",
                      "enum": ["DX", "DY", "DZ"],
                      "description": "Direction (Uniform Acceleration용)"
                    },
                    "MODE": {
                      "type": "integer",
                      "minimum": 1,
                      "description": "Mode (값 > 0. 1개 항목만 허용)"
                    },
                    "SF": {
                      "type": "number",
                      "not": { "const": 0 },
                      "description": "Scale Factor (값 != 0.0. UI 기본 1.0)"
                    }
                  }
                }
              }
            },
            "allOf": [
              {
                "description": "When bUSEINITIAL = true, bREACOUTPUT is required",
                "if": { "properties": { "bUSEINITIAL": { "const": true } }, "required": ["bUSEINITIAL"] },
                "then": { "required": ["bREACOUTPUT"] }
              },
              {
                "description": "When bUSEINITIAL = false, bREACOUTPUT must not be provided",
                "if": { "properties": { "bUSEINITIAL": { "const": false } }, "required": ["bUSEINITIAL"] },
                "then": { "not": { "required": ["bREACOUTPUT"] } }
              },
              {
                "description": "When INCRE_METHOD = LOAD, CTRL_OPT requires STEPCTRLOPTION and STIFF_RATIO and must not contain displacement-control fields",
                "if": { "properties": { "INCRE_METHOD": { "const": "LOAD" } }, "required": ["INCRE_METHOD"] },
                "then": {
                  "properties": {
                    "CTRL_OPT": {
                      "required": ["STEPCTRLOPTION", "STIFF_RATIO"],
                      "not": {
                        "anyOf": [
                          { "required": ["DISPCTRLOPTION"] },
                          { "required": ["GLOBAL_MAX_DISP"] },
                          { "required": ["MASTERNODE"] },
                          { "required": ["MASTERDIRECTION"] },
                          { "required": ["MASTERMAXDISP"] }
                        ]
                      }
                    }
                  }
                }
              },
              {
                "description": "When INCRE_METHOD = DISP, CTRL_OPT requires DISPCTRLOPTION and must not contain load-control fields",
                "if": { "properties": { "INCRE_METHOD": { "const": "DISP" } }, "required": ["INCRE_METHOD"] },
                "then": {
                  "properties": {
                    "CTRL_OPT": {
                      "required": ["DISPCTRLOPTION"],
                      "not": {
                        "anyOf": [
                          { "required": ["STEPCTRLOPTION"] },
                          { "required": ["INCFUNC_NAME"] },
                          { "required": ["STIFF_RATIO"] }
                        ]
                      }
                    }
                  }
                }
              },
              {
                "description": "When LOADPATTERNTYPE = LOAD, LOADPATTERN items must be load-case items (LCNAME + SF required; DIR, MODE forbidden)",
                "if": { "properties": { "LOADPATTERNTYPE": { "const": "LOAD" } }, "required": ["LOADPATTERNTYPE"] },
                "then": {
                  "properties": {
                    "LOADPATTERN": {
                      "items": {
                        "required": ["LCNAME", "SF"],
                        "not": { "anyOf": [ { "required": ["DIR"] }, { "required": ["MODE"] } ] }
                      }
                    }
                  }
                }
              },
              {
                "description": "When LOADPATTERNTYPE = ACC, LOADPATTERN must contain exactly one acceleration item (DIR + SF required; LCNAME, MODE forbidden)",
                "if": { "properties": { "LOADPATTERNTYPE": { "const": "ACC" } }, "required": ["LOADPATTERNTYPE"] },
                "then": {
                  "properties": {
                    "LOADPATTERN": {
                      "maxItems": 1,
                      "items": {
                        "required": ["DIR", "SF"],
                        "not": { "anyOf": [ { "required": ["LCNAME"] }, { "required": ["MODE"] } ] }
                      }
                    }
                  }
                }
              },
              {
                "description": "When LOADPATTERNTYPE = MODE or NOR_MODE, LOADPATTERN must contain exactly one mode item (MODE + SF required; LCNAME, DIR forbidden)",
                "if": { "properties": { "LOADPATTERNTYPE": { "enum": ["MODE", "NOR_MODE"] } }, "required": ["LOADPATTERNTYPE"] },
                "then": {
                  "properties": {
                    "LOADPATTERN": {
                      "maxItems": 1,
                      "items": {
                        "required": ["MODE", "SF"],
                        "not": { "anyOf": [ { "required": ["LCNAME"] }, { "required": ["DIR"] } ] }
                      }
                    }
                  }
                }
              }
            ]
          }
        ]
      }
    }
  }
}
```

> 참고: 원본 스키마는 `CTRL_OPT`/`LOADPATTERN`의 조건부(`if`/`then`) 규칙을 `allOf` 하위에서 `unevaluatedProperties: false`와 함께 각 분기(LOAD/DISP, LOAD/ACC/MODE/NOR_MODE)별로 필드 전체를 재선언하는 방식으로 표현합니다. 위 스키마는 필드 정의 중복을 생략하고 조건부 `required`/`not` 규칙만 표시했으며, 실제 필드 목록·타입·enum은 상단 `CTRL_OPT`/`LOADPATTERN.items` 정의와 동일합니다.
>
> ⚠️ **2026-08-26 확인:** 원문 JSON Schema는 `LOADPATTERN.items`의 `DIR`·`MODE` 필드
> description을 둘 다 `"Load Case (...)"`로 잘못 표기하고 있다(`LCNAME`의 설명을 복붙한 것으로
> 추정). 위 스키마에는 실제 의미(`DIR`="Direction (Uniform Acceleration용)",
> `MODE`="Mode (값 > 0. 1개 항목만 허용)")로 정정해 실었으니, 다음 동기화 때 원문과 다르다고
> 되돌리지 말 것(아티클 id `56506753403673`). 같은 이유로 `NLTYPE`/`INCRE_METHOD`/
> `DISPCTRLOPTION`의 schema description도 원문은 잘려 있으나(예: `NLTYPE`은 "None"만 남고
> "/ P-Delta / Large Displacements"가 누락) 아래 표는 Specifications 표 기준 전체 enum으로
> 보강해 실었다.

### Parameters

`Assign` 객체 하위에 `"1"`, `"2"` 등 문자열 인덱스를 키로 하여 각 항목의 Pushover Load Case를 정의합니다.

| No. | 설명 | Key | Value 타입 | 기본값/enum | 필수 |
|-----|------|-----|-----------|-------------|------|
| 1 | 이름 (길이 1~20, 중복 불가) | `LCNAME` | string | - | 필수 |
| 2 | 설명 (길이 ≤80) | `DESC` | string | `""` | 선택 |
| 3 | 증분 스텝 수(nstep), 값 > 0 (UI 기본 20) | `INCRE_STEP` | integer | - | 필수 |
| 4 | 기하비선형 유형 (None: NONE / P-Delta: PDELTA / Large Displacements: LARGE) | `NLTYPE` | string (enum) | - | 필수 |
| 5 | 초기하중 사용 여부. true이면 bREACOUTPUT 필수, false이면 제공 불가 | `bUSEINITIAL` | boolean | - | 필수 |
| 6 | 초기하중에 의한 누적 반력/층전단력 (bUSEINITIAL=true일 때 필수) | `bREACOUTPUT` | boolean | - | 조건부 필수 |
| 7 | 증분 방법 (Load Control: LOAD / Displacement Control: DISP) | `INCRE_METHOD` | string (enum) | - | 필수 |
| 8 | 제어 옵션 컨테이너 | `CTRL_OPT` | object | - | 필수 |
| **INCRE_METHOD = "LOAD"인 경우** (CTRL_OPT 내 DISP 계열 필드 제공 불가) |
| 8-1 | └ 자동 증분 제어 (Auto-Stepping: AUTO / Equal Step: EQUAL / Incremental Control Function: INC_FUNC) | `CTRL_OPT.STEPCTRLOPTION` | string (enum) | - | 필수 |
| 8-2 | └ 증분 함수 이름 (STEPCTRLOPTION="INC_FUNC"일 때 필수, 그 외 제공 불가) | `CTRL_OPT.INCFUNC_NAME` | string | - | 조건부 필수 |
| 8-3 | └ 현재 강성비(Cs), [0, 100] 범위 | `CTRL_OPT.STIFF_RATIO` | number | - | 필수 |
| **INCRE_METHOD = "DISP"인 경우** (CTRL_OPT 내 LOAD 계열 필드 제공 불가) |
| 9-1 | └ 변위 제어 옵션 (Global: GLOBAL / Master Node: NODE) | `CTRL_OPT.DISPCTRLOPTION` | string (enum) | - | 필수 |
| 9-2 | └ 최대 병진 변위(GLOBAL일 때 필수, 값 > 0) | `CTRL_OPT.GLOBAL_MAX_DISP` | number | - | 조건부 필수 |
| 9-3 | └ 절점 번호(NODE일 때 필수, ExistNode 통과 필요) | `CTRL_OPT.MASTERNODE` | integer | - | 조건부 필수 |
| 9-4 | └ 방향 (DX: DX / DY: DY / DZ: DZ) (NODE일 때 필수) | `CTRL_OPT.MASTERDIRECTION` | string (enum) | - | 조건부 필수 |
| 9-5 | └ 최대 변위(NODE일 때 필수, 값 != 0.0) | `CTRL_OPT.MASTERMAXDISP` | number | - | 조건부 필수 |
| 10 | 하중 패턴 유형 (정적 하중케이스: LOAD / 균일 가속도: ACC / 모드형상: MODE / 정규화 모드형상: NOR_MODE) | `LOADPATTERNTYPE` | string (enum) | - | 필수 |
| 11 | 하중 패턴 배열 (크기 ≥ 1; ACC/MODE/NOR_MODE는 원소 1개로 제한) | `LOADPATTERN` | array [object] | - | 필수 |
| **LOADPATTERNTYPE = "LOAD"인 경우** (DIR, MODE 제공 불가) |
| 11-1 | └ 하중케이스 이름 (ExistStld 통과 필요, Static Load Case 이름) | `LOADPATTERN[].LCNAME` | string | - | 필수 |
| 11-2 | └ 배율(Scale Factor), 값 != 0.0 (UI 기본 1.0) | `LOADPATTERN[].SF` | number | - | 필수 |
| **LOADPATTERNTYPE = "ACC"인 경우** (배열 원소 정확히 1개; LCNAME, MODE 제공 불가) |
| 12-1 | └ 방향 (DX: DX / DY: DY / DZ: DZ) | `LOADPATTERN[].DIR` | string (enum) | - | 필수 |
| 12-2 | └ 배율(Scale Factor), 값 != 0.0 | `LOADPATTERN[].SF` | number | - | 필수 |
| **LOADPATTERNTYPE = "MODE" 또는 "NOR_MODE"인 경우** (배열 원소 정확히 1개; LCNAME, DIR 제공 불가) |
| 13-1 | └ 모드 번호, 값 > 0 | `LOADPATTERN[].MODE` | integer | - | 필수 |
| 13-2 | └ 배율(Scale Factor), 값 != 0.0 | `LOADPATTERN[].SF` | number | - | 필수 |

### Request / Response JSON

**PUT Request Body — Increment Method: Load Control**
```json
{
  "Assign": {
    "1": {
      "LCNAME": "PUSH_LOAD_X",
      "DESC": "Pushover load control case in X direction",
      "INCRE_STEP": 20,
      "NLTYPE": "PDELTA",
      "bUSEINITIAL": true,
      "bREACOUTPUT": true,
      "INCRE_METHOD": "LOAD",
      "CTRL_OPT": {
        "STEPCTRLOPTION": "INC_FUNC",
        "INCFUNC_NAME": "POFC_01",
        "STIFF_RATIO": 80
      },
      "LOADPATTERNTYPE": "LOAD",
      "LOADPATTERN": [
        { "LCNAME": "DEAD", "SF": 1 },
        { "LCNAME": "LIVE", "SF": 0.5 }
      ]
    }
  }
}
```

**PUT Request Body — Increment Method: Displacement Control**
```json
{
  "Assign": {
    "1": {
      "LCNAME": "PUSH_DISP_X",
      "DESC": "Pushover displacement control case using master node",
      "INCRE_STEP": 20,
      "NLTYPE": "PDELTA",
      "bUSEINITIAL": true,
      "bREACOUTPUT": true,
      "INCRE_METHOD": "DISP",
      "CTRL_OPT": {
        "DISPCTRLOPTION": "NODE",
        "MASTERNODE": 1001,
        "MASTERDIRECTION": "DX",
        "MASTERMAXDISP": 0.25
      },
      "LOADPATTERNTYPE": "LOAD",
      "LOADPATTERN": [
        { "LCNAME": "DEAD", "SF": 1 },
        { "LCNAME": "LIVE", "SF": 0.5 }
      ]
    }
  }
}
```

**GET Response Body**
```json
{
  "POLC-M1": {
    "1": {
      "LCNAME": "PUSH_LOAD_X",
      "DESC": "Pushover load control case in X direction",
      "INCRE_STEP": 20,
      "NLTYPE": "PDELTA",
      "bUSEINITIAL": true,
      "bREACOUTPUT": true,
      "INCRE_METHOD": "LOAD",
      "CTRL_OPT": {
        "STEPCTRLOPTION": "INC_FUNC",
        "INCFUNC_NAME": "POFC_01",
        "STIFF_RATIO": 80
      },
      "LOADPATTERNTYPE": "LOAD",
      "LOADPATTERN": [
        { "LCNAME": "DEAD", "SF": 1 },
        { "LCNAME": "LIVE", "SF": 0.5 }
      ]
    },
    "2": {
      "LCNAME": "PUSH_DISP_X",
      "DESC": "Pushover displacement control case using master node",
      "INCRE_STEP": 20,
      "NLTYPE": "PDELTA",
      "bUSEINITIAL": true,
      "bREACOUTPUT": true,
      "INCRE_METHOD": "DISP",
      "CTRL_OPT": {
        "DISPCTRLOPTION": "NODE",
        "MASTERNODE": 1001,
        "MASTERDIRECTION": "DX",
        "MASTERMAXDISP": 0.25
      },
      "LOADPATTERNTYPE": "LOAD",
      "LOADPATTERN": [
        { "LCNAME": "DEAD", "SF": 1 },
        { "LCNAME": "LIVE", "SF": 0.5 }
      ]
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── PUT: Pushover Load Case(Hyper-S) - Load Control 방식 ─────────
def put_pushover_load_case_load_control():
    payload = {
        "Assign": {
            "1": {
                "LCNAME": "PUSH_LOAD_X",
                "DESC": "Pushover load control case in X direction",
                "INCRE_STEP": 20,
                "NLTYPE": "PDELTA",
                "bUSEINITIAL": True,
                "bREACOUTPUT": True,          # bUSEINITIAL=True이므로 필수
                "INCRE_METHOD": "LOAD",
                "CTRL_OPT": {
                    "STEPCTRLOPTION": "INC_FUNC",   # INC_FUNC -> INCFUNC_NAME 필수
                    "INCFUNC_NAME": "POFC_01",
                    "STIFF_RATIO": 80
                },
                "LOADPATTERNTYPE": "LOAD",
                "LOADPATTERN": [
                    {"LCNAME": "DEAD", "SF": 1},
                    {"LCNAME": "LIVE", "SF": 0.5}
                ]
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/POLC-M1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("PUT (Load Control):", resp.status_code, resp.json())

# ── PUT: Pushover Load Case(Hyper-S) - Displacement Control 방식 ─
def put_pushover_load_case_disp_control():
    payload = {
        "Assign": {
            "2": {
                "LCNAME": "PUSH_DISP_X",
                "DESC": "Pushover displacement control case using master node",
                "INCRE_STEP": 20,
                "NLTYPE": "PDELTA",
                "bUSEINITIAL": True,
                "bREACOUTPUT": True,
                "INCRE_METHOD": "DISP",
                "CTRL_OPT": {
                    "DISPCTRLOPTION": "NODE",     # NODE -> MASTERNODE/DIRECTION/MAXDISP 필수
                    "MASTERNODE": 1001,
                    "MASTERDIRECTION": "DX",
                    "MASTERMAXDISP": 0.25
                },
                "LOADPATTERNTYPE": "LOAD",
                "LOADPATTERN": [
                    {"LCNAME": "DEAD", "SF": 1},
                    {"LCNAME": "LIVE", "SF": 0.5}
                ]
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/POLC-M1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("PUT (Displacement Control):", resp.status_code, resp.json())

# ── GET: Pushover Load Case(Hyper-S) 전체 조회 ────────────────────
def get_pushover_load_case():
    resp = requests.get(f"{BASE_URL}/db/POLC-M1", headers=HEADERS)
    resp.raise_for_status()
    print("GET:", resp.json())

put_pushover_load_case_load_control()
put_pushover_load_case_disp_control()
get_pushover_load_case()
```

---

## End-to-End Workflow

다음은 내진성능평가를 위한 푸시오버 해석 전체 설정 워크플로우입니다.

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── STEP 1: 초기하중 무시 요소 설정 (IEPI) ────────────────────────
# 시공단계 임시 부재 등 초기하중 계산에서 제외할 요소 지정
iepi_payload = {
    "Assign": {
        str(eid): {"B_IGNORE": True} for eid in [101, 102, 103]
    }
}
r1 = requests.post(f"{BASE_URL}/db/IEPI", json=iepi_payload, headers=HEADERS)
print(f"STEP1 IEPI: {r1.status_code}")

# ── STEP 2: 푸시오버 힌지 속성 배정 (PHGE) ────────────────────────
phge_payload = {
    "Assign": {
        "1": {"ID": 1, "TYPE": "BEAM", "HINGE_TYPE": "Myz_15", "FIBER_KEY": 0},
        "2": {"ID": 2, "TYPE": "BEAM", "HINGE_TYPE": "Myz_15", "FIBER_KEY": 0}
    }
}
r2 = requests.post(f"{BASE_URL}/db/PHGE", json=phge_payload, headers=HEADERS)
print(f"STEP2 PHGE: {r2.status_code}")

# ── STEP 3: 푸시오버 해석 제어 데이터 설정 (POGD) ─────────────────
pogd_payload = {
    "Assign": {
        "1": {
            "GEOMNONLINEAR_TYPE": "NONE",
            "INITLOADMETHOD": "PERFORM_ANAL",
            "INITLOAD": [],
            "bCONSIGNOREELEM": True,
            "NONL_OPT": {
                "bPERMITFAIL": True, "SUBSTEP": 10, "MAXITER": 30,
                "bDISPLNORM": True, "bFORCENORM": False, "bENERGYNORM": False,
                "DISPLNORM": 0.001, "FORCENORM": 0.001, "ENERGYNORM": 0.001,
                "bSHEARYIELDSTOP": False, "BSHEARYIELDSTOPBEAM": True,
                "bSHEARYIELDSTOPWALL": False, "bAXIALYIELDSTOP": False,
                "bAXIALYIELDSTOPBEAM": True, "bAXIALYIELDSTOPWALL": False,
                "bAXIALYIELDSTOPTRUSS": False, "bSUPPORTDZDIRSTOP": False,
                "bSUPPORTSTOPUPLIFTING": False, "bSUPPORTSTOPCOLLAPSE": False
            },
            "PHOP_OPT": {
                "bCONSREBARAREA1D": True, "BEAM_CORE_SIZE": "AUTO",
                "BEAM_CORE_DIV_Y": 15, "BEAM_CORE_DIV_Z": 15,
                "BEAM_COVER_SIZE": "EQUAL", "BEAM_COVER_DIV_Y": 15, "BEAM_COVER_DIV_Z": 15,
                "bCONSREBARAREAWALL": True, "bWALLCONSOUT": True,
                "WALL_CORE_SIZE": "AUTO", "WALL_CORE_DIV_Z": 8, "WALL_CORE_DIV_Y": 8,
                "WALL_COVER_SIZE": "AUTO", "WALL_COVER_DIV_Z": 8, "WALL_COVER_DIV_Y": 1,
                "SHEAR_R": 0.4, "bASSIGNBYMEMBER": True,
                "bTRI_SYM": True, "TRI_TENS_A1": 0.1, "TRI_TENS_A2": 0.05,
                "TRI_COMP_A1": 0.1, "TRI_COMP_A2": 0.05,
                "bBI_SYM": True, "BI_TENS_A1": 0.05, "BI_COMP_A1": 0.05,
                "PSPR_APPLY_TYPE": "ASSUME", "ELNK_APPLY_TYPE": "APPLY",
                "bUSEAUTOCALCREFERENCE": True, "RCDGNCODE": "KISTEC2019",
                "LOC_BEAM": "M", "LOC_COLUMN": "I",
                "SF_WALL": 1.6, "bSF_BRITTLE": False, "SF_BRITTLE": 1.6,
                "bSF_EARTHQUAKE": False, "SF_EARTHQUAKE": 0.85,
                "bSF_SMOOTH_BAR": False, "SF_SMOOTH_BAR": 0.575,
                "CONFIDENCE": 1, "bBUCKLING": True, "bCALCAXIALFORCE": True
            },
            "NODECONNECTIVITY": "PINNED",
            "bSHOWGRAPHAFTER": True,
            "bSHOWGRAPGHDURING": False
        }
    }
}
r3 = requests.post(f"{BASE_URL}/db/POGD", json=pogd_payload, headers=HEADERS)
print(f"STEP3 POGD: {r3.status_code}")

# ── STEP 4: 푸시오버 하중케이스 정의 (POLC) ───────────────────────
polc_payload = {
    "Assign": {
        "1": {
            "LCNAME": "PUSH_MODE_X", "DESC": "1차 모드 X방향 가력",
            "INCRE_STEP": 20, "bCONS_PDELTA": True, "bUSEINITIAL": True,
            "bREACOUTPUT": True, "INCRE_METHOD": "DISP", "STEPCTRLOPTION": "AUTO",
            "INCFUNC_KEY": 0, "STIFF_RATIO": 0,
            "bLIMITDEFORMANGLE": True, "LIMITDEFORMANGLE": 25,
            "bDRIFTMAX": True, "bDRIFTCENTER": False, "bDRIFTAVER": False,
            "DISPCTRLOPTION": "NODE", "GLOBAL_MAX_DISP": 0,
            "MASTERNODE": 134, "MASTERDIRECTION": "DX", "MASTERMAXDISP": 1.5,
            "LOADPATTERNTYPE": "MODE",
            "LOADPATTERN": [{"MODE": 1, "SF": 1}]
        }
    }
}
r4 = requests.post(f"{BASE_URL}/db/POLC", json=polc_payload, headers=HEADERS)
print(f"STEP4 POLC: {r4.status_code}")

# ── STEP 5: 절단선 정의 후 해석 실행 ──────────────────────────────
r5 = requests.post(f"{BASE_URL}/doc/ANAL", json={"Argument": {}}, headers=HEADERS)
print(f"STEP5 ANAL: {r5.status_code}")

# ── 전체 설정 확인 ─────────────────────────────────────────────────
print("\n=== 푸시오버 설정 확인 ===")
for ep in ["IEPI", "PHGE", "POGD", "POLC"]:
    r = requests.get(f"{BASE_URL}/db/{ep}", headers=HEADERS)
    data = r.json().get(ep, {})
    print(f"  {ep}: {len(data)}개")
```

---

## POGD vs POGD-M1 / POLC vs POLC-M1 비교 요약

| 항목 | 일반(General) | Hyper-S(-M1) |
|------|:--------------:|:------------:|
| Active Methods | POST, GET, PUT, DELETE | GET, PUT, DELETE (POST 미지원) |
| 필드 명명 규칙 | 약어형 Flat 구조 (`GEOMNONLINEAR_TYPE`) | 그룹화된 Enum/중첩 구조 (`GEO_NONL_TYPE`: 0/1/2) |
| JSON Schema 스타일 | 단순 `properties` 나열 | `allOf` / `if-then` 조건부 스키마 |
| 적용 대상 | Civil NX / Gen NX 공통 | Hyper-S 솔버 전용 모델 |
