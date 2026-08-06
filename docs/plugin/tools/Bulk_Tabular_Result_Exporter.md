# Bulk Tabular Result Exporter

> **원문:** [Bulk Tabular Result Exporter](https://support.midasuser.com/hc/ko/articles/60848073556633-Bulk-Tabular-Result-Exporter)
> **원문 작성:** 2026-08-06 · **원문 최종 편집:** 2026-08-06

---

## 개요

교량 모델에서 전처리 데이터(절점·요소·단면)와 후처리 해석 결과(반력, 부재력, 변위, 응력 등)를
여러 하중조합·시공단계에 걸쳐 추출하려면, 통상 테이블마다 선택·설정·수동 export한 뒤 하나의
워크북으로 재조립해야 한다. 이 Plug-in은 그 과정을 단일 작업으로 만든다. 필요한 모든 테이블을
Job으로 한 번씩 정의하고 실제 모델에 대해 미리보기한 뒤, 구조화된 Excel 파일의 개별 워크시트로
한 번에 기록한다. 전체 선택 구성은 다음 모델·다음 리비전에서 재사용할 프리셋으로 저장할 수 있다.

## 지원 버전

`MIDAS CIVIL NX 2026 (v1.1.0)`

## 주요 기능

- **One workbook, every table** — 전처리 모델 데이터와 후처리 결과를 함께 export. 각 Job은
  이름이 명확한 개별 워크시트에 기록되며, **Contents & Export Log** 시트에 요청·반환 내역이
  기록된다.
- **Complete table coverage** — 안내형(guided) 모델 데이터 엔드포인트 100개 이상과 모든 내장
  결과 테이블에 접근 가능. **Any DB Table**·**Any Result Table** 모드로 안내 목록에 없는
  테이블도 접근할 수 있다.
- **Model-aware selection** — Structure Group, 시공단계, 해석 스텝 라벨을 연결된 모델에서
  직접 읽어와 필터로 제공한다(수기 입력이 아님).
- **Report-ready output** — 컬럼 헤더에 단위 포함, 헤더 스타일링, 열 너비 자동 조정, AutoFilter
  적용, 숫자값은 숫자형 유지, ID는 텍스트로 보존.
- **Repeatable workflow** — 전체 테이블 선택 구성을 프리셋으로 저장하고, 이후 세션·수정된
  모델·다음 프로젝트에서 한 번에 복원.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | 테이블 소스 선택 — **Pre-processing**(모델 데이터) / **Post-processing**(해석 결과) 전환 |
| 2 | Table Job 추가 — 카탈로그에서 검색·선택해 추가. 각 Job이 워크시트 1개가 되며, 필요한 만큼 추가 가능 |
| 3 | Job 설정 — 필요한 결과 성분만 선택, 절점/요소 ID·숫자 범위·Structure Group으로 필터, MIDAS 접미사로 하중케이스·하중조합 입력 |
| 4 | (필요 시) 시공단계 설정 — 모델에 저장된 시공단계를 읽어와 export할 정확한 스텝 선택 |
| 5 | 단위·정밀도 설정 — Job별 힘 단위, 길이 단위, 숫자 형식, 소수 자릿수 지정 |
| 6 | Preview — 워크북 생성 전 실제 모델과 대조해 반환될 컬럼·데이터 확인 |
| 7 | Export all to Excel — 활성화된 모든 Job을 추출해 하나의 워크북에 기록. 실패한 Job이 있어도 나머지 성공한 Job은 유지되며, 실패 메시지는 Export Log에 기록됨 |
| 8 | 프리셋 저장 — 전체 선택 구성을 `.mrxpreset.json` 파일로 저장해 이후 재사용 |

## 참고/제약사항

이 Plug-in은 원문에 스스로 밝히듯 특정 엔드포인트 하나를 감싼 도구가 아니라, "100개 이상의
안내형 모델 데이터 엔드포인트 + 모든 내장 결과 테이블"에 접근하는 **범용 일괄 export 도구**다.

## 관련 JSON API 엔드포인트

특정 엔드포인트로 좁혀 링크하지 않는다 — 원문이 스스로 "전처리(`/db/*`) + 후처리(`/post/*`)
전반을 포괄하는 범용 도구"라고 명시하고 있어, 개별 엔드포인트 하나만 링크하면 오히려 범위를
오해하게 만들 수 있다. 실제 대응 대상은 `docs/manual/` 전체다.

## 결론 (원문)

이 Plug-in은 모델이 개정될 때마다 반복되는 리포팅의 번거롭고 오류가 나기 쉬운 부분 — 같은
테이블 선택, 같은 필터 입력, 같은 스프레드시트 병합 — 을 제거한다. 워크북을 한 번 정의하고
모델에 대해 미리보기한 뒤, 해석이 바뀔 때마다 몇 초 만에 재생성할 수 있다. 엔지니어는 결과를
수집하는 대신 해석하는 데 시간을 쓸 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/ko/articles/60848073556633-Bulk-Tabular-Result-Exporter](https://support.midasuser.com/hc/ko/articles/60848073556633-Bulk-Tabular-Result-Exporter)
