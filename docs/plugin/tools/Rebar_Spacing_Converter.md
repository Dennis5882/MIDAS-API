# Rebar Spacing Converter

> **원문:** [Rebar Spacing Converter](https://support.midasuser.com/hc/en-us/articles/35649267067545-Rebar-Spacing-Converter)
> **원문 작성:** 2024-07-29 · **원문 최종 편집:** 2025-08-01

---

## 개요

철근 단면적을 기준으로 다양한 지름의 철근 간격을 확인할 수 있게 해주는 Plug-in이다.

## 지원 버전

`MIDAS CIVIL NX 2024 (v1.1) US`

## 주요 기능

설계 실무에서는 철근 지름을 다른 크기로 바꿔야 하는 경우가 흔하다. 이때 기존 철근 지름이
지시하던 간격도 새 지름에 맞춰 바뀌어야 하는데, 철근 단면적을 기준으로 재계산하면 재설계
과정이 단순해진다.

- 기준에 따른 철근 간격을 빠르게 검증해 설계·시공 효율 향상.
- 기준에 따라 간격을 확인할 수 있는 철근 데이터베이스 지원.

## 사용 방법

| 단계 | 설명 |
| --- | --- |
| 1 | 국가별 철근 기준(national rebar standard) 선택 |
| 2 | 라디오 목록에서 입력 방법 선택(4가지 방식) |
| 3 | 철근 크기와 간격 선택 |
| 4 | **ADD TO BELOW LIST** 클릭 시 선택한 철근 크기·간격이 목록에 추가됨 |

**예시:** `#4@100`으로 배치된 철근을 `#3`과 `#4`를 함께 쓰는 배치로 바꾸려면 — 철근 코드를
"ASTM"으로 설정하고 입력 방법을 "1=>2"로 선택(단일 철근 `#4`를 두 철근 `#3+#4`로 바꾸는
것이므로). Before rebar size를 "#4", before spacing을 "100"으로, after rebar size를 "#3",
"#4"로 설정하면 "After Rebar Spacing"이 자동 계산되어 `#3+#4@77.5`로 표시된다. **ADD TO
BELOW LIST**를 클릭하면 결과를 목록 형태로 확인할 수 있다.

**Rebar Spacing Verification:** 입력한 크기·간격에 따라 철근이 배치되며, 동일한 단면적을
유지하면서 다양한 지름의 철근 간격을 검증할 수 있다.

## 참고/제약사항

### 지원 철근 기준

| 코드 | 기준 |
| --- | --- |
| ASTM | American Society for Testing Materials |
| KS | Korean Industrial Standards |
| EN | European Code |
| GB | Chinese National Standard |
| IS | Indian Standards |
| JIS | Japanese Industrial Standards |
| UNI | Italian National Standards |
| AS/NZS | Australian/New Zealand |

### 입력 방법

| 방법 | 설명 | 예시 |
| --- | --- | --- |
| Input Method 1 | 단일 철근 크기 입력 | 철근 크기 `#4`, 간격 `100` → `#4` 철근이 100 간격으로 배치 |
| Input Method 2 | 두 철근 크기 입력 | 철근 크기 `#4`, `#6`, 간격 `100` → `#4`, `#6` 철근이 100 간격으로 교대 배치 |

## 결론 (원문)

Rebar Spacing Converter Plug-in으로 다양한 지름의 철근을 변환하고, 동일 단면적 기준으로
철근 간격을 검증할 수 있다.

## 원문 링크

[https://support.midasuser.com/hc/en-us/articles/35649267067545-Rebar-Spacing-Converter](https://support.midasuser.com/hc/en-us/articles/35649267067545-Rebar-Spacing-Converter)
