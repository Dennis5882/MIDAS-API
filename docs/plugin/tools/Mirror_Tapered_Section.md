# Mirror Tapered Section

> **원문:** [Mirror Tapered Section](https://support.midasuser.com/hc/en-us/articles/35651585867801-Mirror-Tapered-Section)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

기존 변단면(Tapered Section)의 I단과 J단을 서로 바꿔 새로운 변단면을 생성한다. 동일한
로컬축을 갖는 대칭 미러 변단면을 만든다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

코핑(coping)의 로컬축을 대칭으로 맞추려면 I단과 J단을 서로 바꾼 변단면을 만들어야 한다
(예: coping 1-1 / coping 1-2 — I·J단이 바뀐 변단면). 이 Plug-in은 대칭 형상 한쪽에 변단면을
만든 뒤 I·J단을 바꿔 새 변단면을 형성함으로써 빠르게 단면을 생성할 수 있게 해준다.

## 사용 방법

| 필드 | 설명 |
| --- | --- |
| Tapered Section List | 현재 입력된 변단면 목록을 가져옴(Refresh 버튼으로 갱신 가능). 미러링할 단면 선택 |
| New Section Name Tag | 새로 생성할 단면 이름에 붙일 태그 입력. 예: A 단면을 선택하면 "A_Mirror"라는 이름으로 새 변단면이 생성됨 |
| Generate | 새 변단면 생성 |

## 참고/제약사항

Mirror 기능은 변단면(Tapered Section)에만 적용 가능하다. Tapered Value·User·DB 단면 모두
가능하다.

## 관련 JSON API 엔드포인트

Plug-in이 생성하는 변단면은 `docs/manual`의 다음 엔드포인트와 대응된다.

- [`/db/SECT` — Section Properties (Tapered 포함)](../../manual/04_DB_Properties.md)

## 결론 (원문)

대칭 형상을 가진 변단면이라면 Mirror Section Plug-in으로 손쉽게 단면을 만들 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35651585867801-Mirror-Tapered-Section](https://support.midasuser.com/hc/en-us/articles/35651585867801-Mirror-Tapered-Section)
