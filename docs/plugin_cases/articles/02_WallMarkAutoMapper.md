# WallMarkAutoMapper

- 원문: https://support.midasuser.com/hc/ko/articles/60809496186521-WallMarkAutoMapper
- 영상: [02_WallMarkAutoMapper.mp4](../videos/02_WallMarkAutoMapper.mp4) (원본: https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/Wall%20Mark%20Auto%20Mapper_%EB%82%98%EB%8A%94%EA%B0%90%EC%9E%90.mp4)

---

MIDAS Support
기술자료
API 적용사례
API 적용 사례
WallMarkAutoMapper
생성
2026.08.05
편집
2026.08.05
11
217
WallMark Auto Mapper
━  GEN NX API CHALLENGE 2026
WallMark Auto Mapper
WallMark Auto Mapper는 DXF 구조평면도에서 벽체명과 위치정보를 추출하고, MIDAS GEN
          NX 해석모델에 기존에 부여된 Wall ID별 벽체 위치와 자동 매칭하여 도면의 벽체명을 해당 Wall ID의
          Wall Mark로 부여·관리하는 Plug-in입니다. 자동 매칭 결과는 Preview와 결과표에서 검토·수정한
          뒤 선택적으로 모델에 적용할 수 있습니다.
FEATURES
주요 기능
01
DXF 도면 벽체명 및 위치 정보 추출
선택한 DXF 구조평면도의 지정 레이어에서 벽체명과 위치 정보를 추출하여,
                    GEN NX 모델과 매칭할 도면측 데이터를 자동으로 구성합니다.
02
GEN NX Wall ID별 벽체 중심 좌표 계산
선택한 층과 Wall Type(Membrane 또는 Plate)에 해당하는
                    벽요소를 선별하고, 해당 벽요소의 Node 및 Element 정보를 이용해
                    기존에 부여된 Wall ID별 벽체 중심 좌표를 계산합니다.
03
도면 벽체 정보-Wall ID 자동 매칭
DXF 형식의 구조평면도에서 추출한 벽체명과 위치 정보를 GEN NX 해석모델의
                    Wall ID별 벽체 중심 좌표와 허용 거리를 기준으로 비교하여 가장 가까운
                    후보를 연결합니다. 매칭 결과는 매칭 성공·검토 필요·매칭 실패로 분류하여
                    Preview와 결과표에 표시합니다.
04
Wall Mark 검토·적용 및 관리
Preview와 결과표에서 도면 벽체명과 Wall ID의 매칭 결과를 확인·수정한
                    뒤, 선택한 도면 벽체명을 해당하는 하나 이상의 Wall ID에 Wall
                    Mark로 부여합니다. 기존 Wall Mark의 추가·수정·삭제와 Excel
                    가져오기·내보내기, PDF 결과표 출력을 지원합니다.
예
11
컨텐츠가 도움이 되셨나요?
