# Tendon Profile

> **원문:** [Tendon Profile](https://support.midasuser.com/hc/en-us/articles/45306728128921-Tendon-Profile)
> **원문 작성:** 2025-04-03 · **원문 최종 편집:** 2025-08-01

---

## 개요

교량 구조물의 텐던 프로파일(tendon profile)을 상대좌표에서 절대좌표로 효율적으로 변환하는
Plug-in이다. Element 텐던 프로파일을 Straight 텐던 프로파일로 변환해, 2D·3D 모델을 다루는
엔지니어의 작업을 단순화한다.

- **지원 조건:** 2D/3D, Splice, Element 입력 타입에서 동작.
- **제약:** 2D·3D 입력 타입 모두에서 Straight Length·Transfer Length는 지원하지 않는다.
  2D 입력 타입에서는 Fix·BOT 기능도 제외된다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

- **시간 절약:** 수동 DXF 내보내기, Excel 처리, 수동 입력을 없애 몇 시간 걸리던 작업을 몇
  분으로 줄인다.
- **오류 감소:** 번거로운 과정을 자동화해 좌표 변환 중 사람 실수를 최소화한다.
- **커스터마이즈 가능한 파라미터:** X축 방향, 회전각, Y/Z 오프셋을 특정 설계 요구사항에
  맞게 조정할 수 있다.
- **사용 편의성:** 변환 가능한 텐던 프로파일을 선택하고 변환을 적용하는 간단한 인터페이스.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | **"Import Tendon Profile List"** 클릭 |
| 2 | 변환할 텐던 프로파일 선택 |
| 3 | **"NEW"** 또는 **"Modify"** 버튼을 눌러 변환 자동 적용 |

**NEW** 버튼을 클릭하면, 원래 텐던 이름 + `"_str"`로 새 텐던 프로파일이 생성된다.

## 참고/제약사항

- Straight Length, Transfer Length, Fix, BOT 기능은 특정 조건에서 지원하지 않는다.
- 2D 모델의 경우 지원하지 않는 기능은 3D 입력을 이용한 대체 워크플로가 필요할 수 있다.

## 관련 JSON API 엔드포인트

Plug-in이 변환하는 텐던 프로파일은 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/TDNA` — Tendon Profile](../../manual/07_DB_Temperature_Prestress.md)

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/45306728128921-Tendon-Profile](https://support.midasuser.com/hc/en-us/articles/45306728128921-Tendon-Profile)
