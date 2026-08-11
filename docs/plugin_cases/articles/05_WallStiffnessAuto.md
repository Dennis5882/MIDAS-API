# WallStiffnessAuto

- 원문: https://support.midasuser.com/hc/ko/articles/60729084287897-WallStiffnessAuto
- 영상: [05_WallStiffnessAuto.mp4](../videos/05_WallStiffnessAuto.mp4) (원본: https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/WallStiffnessAuto_%EB%AF%BC%EC%84%B1.mp4)

---

MIDAS Support
기술자료
API 적용사례
API 적용 사례
WallStiffnessAuto
생성
2026.08.03
편집
2026.08.05
33
373
WallStiffnessAuto
━  GEN NX API CHALLENGE 2026
WallStiffnessAuto
WallStiffnessAuto는 GEN NX API로 RC 벽체 설계(KDS-41-20-2022) 결과를 직접
          조회해, 기준을 초과한 벽체의 강성 증감계수(WSSF)를 NG가 모두 해소될 때까지 스스로 낮춰가는 프로그램입니다.
FEATURES
주요 기능
01
NG 부재 자동 탐색
구조해석과 벽체 설계를 실행한 뒤, 기준을 초과한 벽체를 층/Wall ID
                    단위로 자동 추출하고 지배 응력비를 함께 표시합니다.
02
저감 조건 설정
회당 감소량, 계수 하한, 최대 반복 횟수를 설정하면 그 범위 안에서 자동 반복이 진행됩니다.
03
자동 반복 저감
반복마다 강성 적용 → 해석 → 설계 재확인 순으로 진행하며, NG가 모두
                    해소되거나 계수가 하한에 도달하면 자동으로 중단됩니다.
04
계수 복원
반복 중 저감된 계수는 언제든 버튼 한 번으로 저감 이전 값(1.0)으로 복원할 수 있습니다.
예
33
컨텐츠가 도움이 되셨나요?
