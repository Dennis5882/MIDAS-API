Attribute VB_Name = "SimpleBeamLoadCombination"
Option Explicit

' MIDAS NX Open API - Excel VBA 예제: 단순보 하중조합
'
' 10m 단순보(양단 핀/롤러 지지)를 20등분해서 절점/요소를 생성하고,
' 자중(DL) + 등분포 보하중(SIDL)을 적용한 뒤 하중조합까지 구성하는 예제입니다.
' examples/python/simple_beam_load_combination.py와 동일한 흐름의 VBA 버전입니다.
'
' 출처: MIDAS Support - Example: Excel VBA
' https://support.midasuser.com/hc/en-us/articles/30506684736665-Example-Excel-VBA
' (공식 튜토리얼 기사를 이 저장소 스타일에 맞춰 재구성한 버전입니다.
'  요소 생성 루프의 상한이 원본 기사에서 "0 To num_division"으로 되어 있어
'  존재하지 않는 (num_division+2)번째 절점을 참조하는 off-by-one 버그가 있었습니다.
'  아래 코드는 "0 To num_division - 1"로 수정했습니다 — 이는 같은 기사군의
'  Python 버전(examples/python/simple_beam_load_combination.py)의 루프 범위와도 일치합니다.)
'
' 사전 준비:
'   1) JsonConverter.bas (VBA-JSON, https://github.com/VBA-tools/VBA-JSON) 임포트
'   2) 도구 → 참조 → "Microsoft Scripting Runtime" 체크
'   3) 시트에 입력값 채우기 (README.md의 "시트 입력 레이아웃" 참고)

' REST API 호출 헬퍼
Function WebRequest(Method As String, Command As String, body As String) As String

    Dim TCRequestItem As Object
    Dim baseURL As String
    Dim URL As String
    Dim MAPI_Key As Variant

    Set TCRequestItem = CreateObject("WinHttp.WinHttpRequest.5.1")

    'SetTimeouts(resolveTimeout, ConnectTimeout, SendTimeout, ReceiveTimeout)
    TCRequestItem.SetTimeouts 200000, 200000, 200000, 200000

    baseURL = Cells(15, "H").Value
    MAPI_Key = Cells(16, "H").Value

    URL = baseURL & Command
    TCRequestItem.Open Method, URL, False
    TCRequestItem.SetRequestHeader "Content-type", "application/json"
    TCRequestItem.SetRequestHeader "MAPI-Key", MAPI_Key
    TCRequestItem.Send body
    WebRequest = TCRequestItem.ResponseText

    Debug.Print Command & " : " & TCRequestItem.Status & " - " & TCRequestItem.StatusText

End Function

Sub CreateSimpleBeam()

    Dim i As Long

    ' 시트에서 입력값 읽기
    Dim dist As String
    Dim force As String
    Dim length As Double
    Dim height As Double
    Dim width As Double
    Dim direction As String
    Dim loadValue As Double
    Dim modelID As Range
    Dim loadCase As Range
    Dim matSt As String
    Dim matDB As String

    dist = UCase(Cells(5, "E").Value)
    force = UCase(Cells(6, "E").Value)

    length = Cells(8, "E").Value
    height = Cells(9, "E").Value
    width = Cells(10, "E").Value

    direction = Cells(9, "I").Value
    loadValue = Cells(9, "J").Value

    matSt = Cells(5, "J").Value
    matDB = Cells(6, "J").Value

    Set loadCase = Range(Cells(12, "I"), Cells(13, "J"))
    Set modelID = Range(Cells(12, "E"), Cells(15, "E"))

    Dim dicMain As Scripting.Dictionary
    Dim dicSub1 As Scripting.Dictionary
    Dim dicSub2 As Scripting.Dictionary
    Dim dicSub3 As Scripting.Dictionary
    Dim dicSub4 As Scripting.Dictionary
    Dim response As String
    Dim body As String

    Dim num_division As Long
    Dim interval As Double
    num_division = 20
    interval = length / num_division

    ' 1) 새 문서
    response = WebRequest("POST", "/doc/new", "{}")
    Debug.Print response

    ' 2) 단위
    Set dicMain = New Dictionary
    Set dicSub1 = New Dictionary: Set dicSub2 = New Dictionary

    dicSub2.Add "DIST", dist
    dicSub2.Add "FORCE", force
    dicSub1.Add "1", dicSub2
    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("PUT", "/db/unit", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing: Set dicSub2 = Nothing

    ' 3) 재료 (RC)
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary
    Set dicSub2 = New Dictionary: Set dicSub3 = New Dictionary

    dicSub3.Add "P_TYPE", 1
    dicSub3.Add "STANDARD", matSt
    dicSub3.Add "DB", matDB

    dicSub2.Add "TYPE", "CONC"
    dicSub2.Add "NAME", matDB
    dicSub2.Add "PARAM", Array(dicSub3)

    dicSub1.Add modelID(1, 1), dicSub2
    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/matl", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing
    Set dicSub2 = Nothing: Set dicSub3 = Nothing

    ' 4) 단면 (직사각형 값입력 단면)
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary
    Set dicSub2 = New Dictionary: Set dicSub3 = New Dictionary: Set dicSub4 = New Dictionary

    dicSub4.Add "vSIZE", Array(height, width)

    dicSub3.Add "USE_SHEAR_DEFORM", True
    dicSub3.Add "SHAPE", "SB"
    dicSub3.Add "DATATYPE", 2
    dicSub3.Add "SECT_I", dicSub4

    dicSub2.Add "SECTTYPE", "DBUSER"
    dicSub2.Add "SECT_NAME", "Rectangular"
    dicSub2.Add "SECT_BEFORE", dicSub3

    dicSub1.Add modelID(2, 1), dicSub2
    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/sect", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing
    Set dicSub2 = Nothing: Set dicSub3 = Nothing: Set dicSub4 = Nothing

    ' 5) 절점 (0 ~ length를 num_division등분 → num_division+1개)
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary

    For i = 0 To num_division
        Set dicSub2 = New Dictionary

        dicSub2.Add "X", i * interval
        dicSub2.Add "Y", 0
        dicSub2.Add "Z", 0

        dicSub1.Add modelID(3, 1) + i, dicSub2

        Set dicSub2 = Nothing
    Next i

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/node", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing

    ' 6) 요소 (인접 절점을 순서대로 BEAM으로 연결 → num_division개)
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary

    For i = 0 To num_division - 1
        Set dicSub2 = New Dictionary

        dicSub2.Add "TYPE", "BEAM"
        dicSub2.Add "MATL", modelID(1, 1)
        dicSub2.Add "SECT", modelID(2, 1)
        dicSub2.Add "NODE", Array(modelID(3, 1) + i, modelID(3, 1) + i + 1)

        dicSub1.Add modelID(4, 1) + i, dicSub2

        Set dicSub2 = Nothing
    Next i

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/elem", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing

    ' 7) 지지조건 (시작단 핀, 끝단 롤러)
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary
    Set dicSub2 = New Dictionary: Set dicSub3 = New Dictionary

    dicSub3.Add "ID", 1
    dicSub3.Add "CONSTRAINT", "1111000"
    dicSub2.Add "ITEMS", Array(dicSub3)
    dicSub1.Add modelID(3, 1), dicSub2

    Set dicSub2 = Nothing: Set dicSub3 = Nothing
    Set dicSub2 = New Dictionary: Set dicSub3 = New Dictionary

    dicSub3.Add "ID", 1
    dicSub3.Add "CONSTRAINT", "0111000"
    dicSub2.Add "ITEMS", Array(dicSub3)
    dicSub1.Add modelID(3, 1) + num_division, dicSub2

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/cons", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing
    Set dicSub2 = Nothing: Set dicSub3 = Nothing

    ' 8) 하중 케이스 (자중용 DL, 추가하중용 SIDL — loadCase 시트범위 2행)
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary

    For i = 0 To loadCase.Rows.Count - 1
        Set dicSub2 = New Dictionary

        dicSub2.Add "NAME", loadCase(i + 1, 2)
        dicSub2.Add "TYPE", "USER"

        dicSub1.Add i + 1, dicSub2

        Set dicSub2 = Nothing
    Next i

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/stld", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing

    ' 9) 자중 (1행 하중케이스에 -Z 방향 1배)
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary
    Set dicSub2 = New Dictionary

    dicSub2.Add "LCNAME", loadCase(1, 2)
    dicSub2.Add "FV", Array(0, 0, -1)
    dicSub1.Add "1", dicSub2

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/bodf", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing
    Set dicSub2 = Nothing

    ' 10) 등분포 보하중 (2행 하중케이스, 모든 요소에 적용)
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary

    For i = 0 To num_division - 1
        Set dicSub2 = New Dictionary: Set dicSub3 = New Dictionary

        dicSub3.Add "ID", 1
        dicSub3.Add "LCNAME", loadCase(2, 2)
        dicSub3.Add "CMD", "BEAM"
        dicSub3.Add "TYPE", "UNILOAD"
        dicSub3.Add "DIRECTION", direction
        dicSub3.Add "D", Array(0, 1)
        dicSub3.Add "P", Array(loadValue, loadValue)

        dicSub2.Add "ITEMS", Array(dicSub3)
        dicSub1.Add modelID(4, 1) + i, dicSub2

        Set dicSub2 = Nothing: Set dicSub3 = Nothing
    Next i

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/bmld", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing

    ' 11) 하중조합 (loadCase 시트범위의 팩터·LC이름 그대로 사용)
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary
    Set dicSub2 = New Dictionary

    Dim vCOMB() As Object
    ReDim vCOMB(loadCase.Rows.Count - 1)

    For i = 0 To loadCase.Rows.Count - 1
        Set dicSub3 = New Dictionary

        dicSub3.Add "ANAL", "ST"
        dicSub3.Add "LCNAME", loadCase(i + 1, 2)
        dicSub3.Add "FACTOR", loadCase(i + 1, 1)

        Set vCOMB(i) = dicSub3

        Set dicSub3 = Nothing
    Next i

    dicSub2.Add "NAME", "Comb1"
    dicSub2.Add "ACTIVE", "ACTIVE"
    dicSub2.Add "iTYPE", 0
    dicSub2.Add "vCOMB", vCOMB

    dicSub1.Add "1", dicSub2
    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/lcom-gen", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing
    Set dicSub2 = Nothing

    ' 12) 저장
    response = WebRequest("POST", "/doc/save", "{}")
    Debug.Print response

    MsgBox "완료! MIDAS NX 화면에서 단순보와 하중조합을 확인하세요."

End Sub
