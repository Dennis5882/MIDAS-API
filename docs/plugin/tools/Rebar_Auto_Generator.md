# Rebar Auto Generator

> **원문:** [Rebar Auto Generator](https://support.midasuser.com/hc/en-us/articles/60470400396953-Rebar-Auto-Generator)
> **원문 작성:** 2026-07-27 · **원문 최종 편집:** 2026-10-12

---

## 개요

호주 RMS 기준에 따라 단면의 종방향·전단 철근 생성을 자동화하는 Plug-in이다. 미리 정의된
표준 위치에 빠르고 정확하게 철근을 생성할 수 있다.

## 지원 버전

`MIDAS CIVIL NX 2026 (v1.1)`

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | **Connect** 클릭 → Marketplace를 열고 Rebar Auto Generator Plug-in 실행 |
| 2 | Section ID, Type, Name, vBar size, Pitch를 선택하고 **Generate Rebar** 클릭 |

## 참고/제약사항

1. Plug-in은 PSC-Composite 단면을 자동 감지해 철근 생성에 사용한다.
2. Plug-in을 실행하면 선택한 단면의 기존 철근 데이터를 덮어쓴다.
3. 현재 `AS-Super-T_RMS_2019` 단면만 지원한다.
4. **'Ref .dwg file'**로 도면 형식의 철근 상세를 검토할 수 있다.

## 관련 JSON API 엔드포인트

Plug-in이 생성하는 단면 철근 정보는 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/RPSC` — Section Manager (Reinforcements)](../../manual/04_DB_Properties.md)

## 결론 (원문)

Rebar Auto Generator Plug-in은 MIDAS CIVIL NX, 특히 RMS 표준 단면에서 철근 모델링을
단순화한다. 철근 배치를 자동화하고 사전 정의된 기준 준수를 보장해 수작업 부담을 줄이고
오류를 최소화한다.

> ✅ **2026-10-18 정기 점검 — 원문 정정 확인.** 이전에는 원문에 "Benefits of this plugin" 문단이
> 있었으나, 이 아티클의 실제 기능(단면 철근 자동 생성)과 무관한 다른 Plug-in(시간이력 하중케이스·
> EN1991-2:2003 감쇠·운행속도-가속도 그래프 관련, "Dynamic Analysis of Rail Bridge"와 동일 문구)이
> 그대로 복사된 것이어서 이 문서에는 옮기지 않았다. 2026-10-12 원문 편집으로 en-us 본문에서 해당
> 문단이 삭제되어 자기모순이 해소됐다(ko 페이지에는 아직 남아 있음 — 기준 로케일은 en-us).
> 그 외 본문(개요·지원 버전·사용 방법·참고·결론)은 변경 없음.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/60470400396953-Rebar-Auto-Generator](https://support.midasuser.com/hc/en-us/articles/60470400396953-Rebar-Auto-Generator)
