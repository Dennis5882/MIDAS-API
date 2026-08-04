# Nastran Importer

> **원문:** [Nastran Importer](https://support.midasuser.com/hc/en-us/articles/45548001795865-Nastran-Importer)
> **원문 작성:** 2025-04-09 · **원문 최종 편집:** 2025-08-01

---

## 개요

**Nastran BDF(Bulk Data Format)** 파일을 MIDAS CIVIL NX로 매끄럽게 가져오는 Plug-in이다.
메시 기반 모델을 다루는 엔지니어를 위해 설계되었으며, 노드/요소 데이터 변환을 자동화하면서
형상 무결성을 유지해 정확한 시뮬레이션을 보장한다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

- **효율적인 워크플로:** 수동 데이터 변환 없이 Nastran BDF 파일을 직접 가져온다.
- **데이터 무결성:** 가져오는 동안 원본 메시 구조(노드/요소)를 유지한다.
- **시간 절약:** Nastran 모델을 Civil NX로 옮기는 과정의 불필요한 단계를 없앤다.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | Import 버튼을 클릭해 로컬 폴더 접근 |
| 2 | 변환할 BDF 파일 선택 |
| 3 | 변환된 형상 모델 확인 |

## 참고/제약사항

- 지원 데이터는 **노드(nodes)**와 **요소(elements)**이며, 지원하지 않는 데이터(예: 솔버
  전용 명령어)는 무시된다.
- 복잡한 모델은 임포트 후 메시 연속성을 반드시 검증해야 한다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/45548001795865-Nastran-Importer](https://support.midasuser.com/hc/en-us/articles/45548001795865-Nastran-Importer)
