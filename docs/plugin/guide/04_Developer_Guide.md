# A Guide to Creating Plug-in for Developers

> **원문:** [A Guide to Creating Plug-in for Developers](https://support.midasuser.com/hc/ko/articles/44321750649369-A-Guide-to-Creating-Plug-in-for-Developers)
> **원문 작성:** 2025-03-10 · **원문 최종 편집:** 2025-05-19 (2026-08-04 재확인, 내용 변경 없음 — 타임스탬프만 갱신된 cosmetic bump)

---

이 문서는 **개발자용 Plug-in 개발 가이드**다.

## 사전 요구사항

- CLI (Command-Line Interface)
- npm (node package manager)
- npx (node package execute)
- TypeScript 기반 React
- Python (사용하는 라이브러리에 따라)

### 권장 IDE/프레임워크

- Visual Studio Code
- Node.js

## MIDAS IT 제공 라이브러리

Plug-in 개발을 간소화하기 위해 MIDAS IT이 제공하는 라이브러리들:

| 라이브러리 (npm) | 설명 |
| --- | --- |
| `@midasit-dev/cra-template-moaui` | React + TypeScript + moaui + Pyscript로 구성된 Plug-in 개발 템플릿 |
| `@midasit-dev/cra-template-moaui-light` | Pyscript를 제외한 React + TypeScript + moaui 템플릿 |
| `@midasit-dev/moaui-components-v1` | Material UI 기반, MIDAS IT 디자인이 적용된 UI 컴포넌트 |
| `@midasit-dev/moaui-lab` | 위 컴포넌트의 StoryBook |

> **왜 Pyscript인가?** Plug-in은 엔지니어링 도구이므로 본질적으로 수치 계산이 필요하고,
> 이런 계산에는 Python이 가장 적합한 도구로 판단되어 템플릿에 포함되었다.

## Plug-in 업로드

개발한 Plug-in은 제품 내에 등록해 사용할 수 있다. 절차는 다음과 같다.

1. 빌드해서 하나의 ZIP 파일로 패키징한다.
2. Plug-in 플랫폼의 **MyWork** 탭으로 이동한다.
3. 업로드를 진행한다.

업로드한 Plug-in을 실행하면(사전에 API 연결을 확인할 것) 의도한 대로 개발된 인터페이스가
표시된다.

## FAQ

**Q. 아이콘은 어떻게 등록하나?**
A. 빌드 폴더 최상위에 있는 `icon.svg` 파일을 Plug-in 아이콘으로 인식한다(다른 포맷은 지원하지
않음). SVG 파일을 만들어 `icon.svg`로 저장하고, 빌드를 ZIP으로 패키징할 때 반드시 포함시킨다.

**Q. 설명(Description)은 어떻게 수정하나?**
A. 빌드 폴더의 `readme.md` 내용이 Plug-in 설명으로 표시된다. `readme.md`에 설명을 작성하고
빌드 시 포함되도록 한다.

**Q. 다른 사용자와 Plug-in을 공유하려면?**
A. 원문 작성 시점 기준, 개별 개발한 Plug-in을 Marketplace에서 공유할 수 있는 시스템을 준비
중이라고 안내한다.

> ⚠️ Marketplace 공유 기능은 [How to use MIDAS Plug-ins](02_How_to_Use.md)에서도 동일하게
> "준비 중"으로 언급된다. 실제 제공 여부는 정기 점검 시 재확인이 필요하다.
