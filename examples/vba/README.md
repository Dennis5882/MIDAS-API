# Excel VBA 예제

## 사전 준비

1. **MIDAS Civil NX 또는 Gen NX 실행**
2. Open API 메뉴에서 **MAPI-Key** 발급
3. Excel에서 `ALT+F11` (VBA 편집기) 또는 "개발 도구" 탭 활성화
   (파일 → 옵션 → 리본 사용자 지정 → "개발 도구" 체크)

## JSON 처리를 위한 라이브러리 설치

VBA는 JSON을 다루는 내장 기능이 없어서 외부 라이브러리가 필요합니다.

1. [VBA-JSON](https://github.com/VBA-tools/VBA-JSON)의 `JsonConverter.bas`를 다운로드
2. VBA 편집기 → 모듈 우클릭 → "파일 가져오기" → `JsonConverter.bas` 선택
3. 도구 → 참조에서 **"Microsoft Scripting Runtime"** 체크 (Dictionary의 Early binding에 필요)

## 예제 파일

- [`SimpleBeamLoadCombination.bas`](./SimpleBeamLoadCombination.bas) — `WebRequest()` 헬퍼(`WinHttp.WinHttpRequest.5.1` 기반) +
  단순보를 20등분해 절점/요소를 반복 생성하고, 자중(`/db/bodf`) + 등분포 보하중(`/db/bmld`) + 하중조합(`/db/lcom-gen`)까지 엮는 예제.
  Excel 시트 셀에서 입력값을 읽어오는 구조이므로, 실행 전 아래 "시트 입력 레이아웃"에 맞춰 값을 채워야 합니다.
  [MIDAS Support "Example: Excel VBA"](https://support.midasuser.com/hc/en-us/articles/30506684736665-Example-Excel-VBA) 튜토리얼 기사를 재구성.

### 시트 입력 레이아웃 (원본 기사 기준)

| 셀 | 값 | 설명 |
|---|---|---|
| `E5` | 거리 단위 (예: `M`) | |
| `E6` | 힘 단위 (예: `KN`) | |
| `E8` | 보 길이 | |
| `E9` | 단면 높이 | |
| `E10` | 단면 폭 | |
| `E12:E15` | 재료/단면/시작절점/시작요소 ID | 순서대로 |
| `I9` / `J9` | 보하중 방향(예: `GZ`) / 크기 | |
| `I12:J13` | 하중조합 계수·하중케이스명 2행 | (팩터, LC 이름) |
| `J5` / `J6` | 재료 표준 / 재료 등급 (예: `AS17(RC)` / `C32`) | |
| `H15` / `H16` | Base URL / MAPI-Key | |

## 실행

1. `JsonConverter.bas`와 `SimpleBeamLoadCombination.bas`를 모두 프로젝트에 임포트
2. 시트에 입력값 채우기 (위 표 참고)
3. 개발 도구 → 삽입 → 버튼(양식 컨트롤) → `CreateSimpleBeam` 매크로 연결
4. MIDAS Civil NX를 실행한 상태에서 버튼 클릭

## 핵심 패턴

```vb
Function WebRequest(Method As String, Command As String, body As String) As String
    Dim req As Object
    Set req = CreateObject("WinHttp.WinHttpRequest.5.1")
    req.Open Method, baseURL & Command, False
    req.SetRequestHeader "Content-type", "application/json"
    req.SetRequestHeader "MAPI-Key", MAPI_Key
    req.Send body
    WebRequest = req.ResponseText
End Function

' 모든 /db/* 요청은 Assign 래퍼 사용 (Dictionary → JsonConverter.ConvertToJson)
Dim dicMain As Scripting.Dictionary: Set dicMain = New Dictionary
' ...
dicMain.Add "Assign", dicSub1
body = JsonConverter.ConvertToJson(dicMain)
WebRequest "POST", "/db/node", body
```
