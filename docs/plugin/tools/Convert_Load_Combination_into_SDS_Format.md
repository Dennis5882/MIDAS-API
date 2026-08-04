# Convert Load Combination into SDS Format

> **원문:** [Convert Load Combination into SDS Format](https://support.midasuser.com/hc/en-us/articles/45496104876313-Convert-Load-Combinations-into-SDS-Format)
> **원문 작성:** 2025-04-08 · **원문 최종 편집:** 2025-08-01

---

## 개요

하중조합을 기본 하중케이스만으로 구성된 조합으로 변환해, **MIDAS SDS**에서 사용할 수 있게
해주는 Plug-in이다.

## 지원 버전

`MIDAS GEN NX 2026 (v1.1) KR`

## 주요 기능

구조물을 설계하려면 하중조합을 만들어야 하는데, 이 조합은 구조물에 작용하는 하중 상태에
따라 달라지고 하중에 적용되는 계수는 설계기준에 따라 달라진다. 그래서 모든 조건을 만족하는
하중조합을 자동으로 만들기는 어렵다.

프로그램이 제공하지 않는 하중조합을 사용자가 직접 만들어 쓰고 싶은데, 그 하중조합이 연동되는
프로그램에서는 동작하지 않는다면 얼마나 불편할까? 이를 위해 이 Plug-in은 기존 프로그램에서
생성된 하중조합을 분해해 MIDAS SDS 같은 프로그램에서 쓸 수 있는 기본 하중의 조합으로
변환한다.

- 프로그램 간 전환 시 불필요한 작업이 줄어 설계 시간이 단축된다.
- 반복적인 수정 작업에서 발생하는 사람 실수를 줄인다.
- 불필요한 하중이 자동 생성되는 것을 막아 더 경제적인 설계가 가능하다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | Plug-in 실행 후 **Select lcb Type**에서 가져올 Design Type 선택 |
| 2 | Design Type 선택 시 **Select Active Type** 창이 활성화되어, 현재 하중조합이 존재하는 Type만 표시됨. SDS LCB Type으로 변환할 Type을 선택하고 **Create** 클릭 시 SDS 형식으로 변환 |
| 3 | 결과를 SDS에 전달하는 두 가지 방법: ① 클립보드에 저장해 SDS에 바로 붙여넣기, ② Excel 파일로 다운로드(OS 다운로드 폴더에 자동 저장)해 원하는 대로 수정 |
| 4 | 복사한 하중조합을 SDS의 Load Combinations 스프레드시트 폼 1행 활성 셀에 붙여넣으면 완료 |

## 참고/제약사항

- **SDS는 아직 활성화된 API가 없어**, 하중조합은 복사-붙여넣기 방식으로만 전달할 수 있다
  (원문 명시). 이 Plug-in은 SDS 쪽으로는 JSON API가 아니라 클립보드/Excel 파일 경유로
  데이터를 넘긴다.

## 결론 (원문)

이 가이드를 통해 Plug-in을 활용해 CIVIL 또는 GEN 한쪽 프로그램만을 위한 하중조합을 만들 수
있어, 설계 시간을 줄이고 정확도를 높일 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/45496104876313-Convert-Load-Combinations-into-SDS-Format](https://support.midasuser.com/hc/en-us/articles/45496104876313-Convert-Load-Combinations-into-SDS-Format)
