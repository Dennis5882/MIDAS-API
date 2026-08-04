# 6x6 General Spring for Pile Foundation (KR)

> **원문:** [Pile Spring](https://support.midasuser.com/hc/en-us/articles/35651992652441-Pile-Spring)
> ("Plug-in Item" 목록에는 "6x6 General Spring for Pile Foundation (KR)"로 표기되나, 아티클
> 자체 제목은 "Pile Spring"이다.)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

말뚝 기초를 모델링하는 방법 중 하나는 **6x6 General Spring**으로 말뚝 기초 강성을 고려하는
것이다. 이 Plug-in은 한국 도로교설계기준(2010) 변위법을 이용해 말뚝 기초 강성을 계산하는 것을
지원한다.

말뚝 제원(말뚝 종류, 상부·하부 말뚝, 보강)을 입력하고 말뚝을 배치한 뒤 지반 정보를 입력하면,
각 말뚝의 특성값과 축 스프링 상수(Kv), 축직각 강성(K1~K4)을 확인하고 방향별(Global X, Y)
연성 스프링 매트릭스 값을 Excel 계산서로 확인할 수 있다. 최종적으로 방향별 매트릭스를 결합한
6x6 General Spring이 계산되어 midas Civil에 General Spring으로 임포트된다.

- 말뚝 제원·지반 정보 입력을 바탕으로 변위법을 이용한 6x6 강성 매트릭스 계산
- 상시·지진 시·고유주기 산정용 매트릭스 지원
- 지원 말뚝 종류: 현장타설말뚝(Cast-in-place), PHC말뚝, SC말뚝, 강관말뚝(Steel Pipe),
  소일시멘트말뚝(Soil Cement)
- 복합말뚝(상부·하부 말뚝), 군말뚝, 단독말뚝 지원

## 지원 버전

- `MIDAS CIVIL NX 2024 (v1.1) KR`
- 적용 기준: 한국 도로교설계기준(2010)

## 주요 기능

말뚝 기초 모델링 방법에는 고정점 모델, 가상 고정점(β) 모델, p-y 곡선 모델, 6x6 general
spring 모델 등이 있다. 이 Plug-in은 6x6 general spring 방식의 강성 매트릭스를 계산해 Midas
Civil에 general spring을 자동 생성한다. 전통적으로 Excel로 하던 말뚝 특성값·축/횡 스프링
강성 산정·최종 매트릭스 결합 과정을 자동화하며, 계산된 값은 Excel 계산서로도 검증 가능하다.

## 사용 방법

매트릭스를 계산하려면 **Pile Information** 탭에 말뚝 제원을, **Ground Information** 탭에
지반 정수를 입력한다.

| 단계 | 탭 | 설명 |
| --- | --- | --- |
| 1 | Pile Information | 말뚝 제원 입력 및 배치. 단독말뚝·군말뚝·보강 단면·복합말뚝(상부/하부) 지원. 말뚝 종류(현장타설·PHC·SC·강관·소일시멘트)와 시공 방법(항타·진동해머·현장타설·대구경천공·선굴착·강관소일시멘트·회전) 선택. 말뚝 배치 좌표계는 한국 도로교설계기준(2010) 좌표계를 따르며, Midas Civil로 임포트 시 Civil 좌표계로 변환됨 |
| 2 | Ground Information | 지반 정수 및 수평 지반반력계수 저감계수 선택. 층(점토·사질토·자갈) 선택과 도로설계편람 기준 전단파속도 자동 계산 지원. 액상화층·경사면 영향·군말뚝 영향에 의한 수평 지반반력계수(KH) 저감 옵션 제공 |
| 3 | Import Data | 강성 매트릭스 결과 확인 후 6x6 general spring을 Midas Civil에 입력. Type1/Type2는 Plug-in의 하중 좌표계를 Midas Civil 좌표계에 맞추는 설정 |

## 참고/제약사항

- 6x6 General Spring 대신 가상 고정점 모델을 적용하는 경우, Excel 계산서에 출력되는 말뚝
  특성값(β)으로 가상 고정점 위치를 정할 수 있다.
- 복합말뚝의 특성값은 Excel 계산서로 산정할 때 보통 상부 말뚝의 단면 특성(EI)과 단일
  지반반력계수(KH)로 결정하지만, 이 Plug-in은 상부·하부 말뚝 제원뿐 아니라 보강 단면(피복·충전
  구간)까지 고려하고 다층 지반의 지반반력계수를 반영해 말뚝 특성값을 계산한다.
- 축 스프링 상수(Kv)는 한국 도로교설계기준(2010) 공식으로 계산되며, 노출 말뚝은 보정계수를
  적용하지 않는다. 실무에서 흔한 복합말뚝(SC+PHC)은 일반적으로 PHC 말뚝의 단면 특성만 고려해
  계산한다. 혼합 말뚝은 직렬 스프링 강성 공식으로 축 스프링 상수를 계산한다.
- 축직각 스프링 상수(K1~K4)는 단일 지반(수평 지반반력계수 일정)·말뚝 단면 특성(EI) 일정 조건의
  일반식이 도로교설계기준 공식이지만, 이 Plug-in은 다층 지반·복합말뚝에 대해 프레임 해석법으로
  계산한다. 단층 지반·단독 말뚝의 경우 도로교설계기준 일반식과 동일한 결과를 얻을 수 있다.
- 원문에 샘플 첨부파일(`pile sample.zip`)이 제공된다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35651992652441-Pile-Spring](https://support.midasuser.com/hc/en-us/articles/35651992652441-Pile-Spring)
