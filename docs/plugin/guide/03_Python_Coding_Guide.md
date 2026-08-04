# Guiding for writing Python Code (Planning/Development Collaboration)

> **원문:** [Guiding for writing Python Code (Planning/Development Collaboration)](https://support.midasuser.com/hc/ko/articles/44321576105497-Guiding-for-writing-Python-Code-Planning-Development-Collaboration)
> **원문 작성/편집:** 2025-03-10

---

## 목적

Plug-in 기획자가 개발자에게 의도를 장문으로 설명하지 않아도, **의도를 담은 Python 코드**를
먼저 작성해두면 개발 착수 시간을 단축할 수 있다. 파일을 3가지 카테고리로 단순하게 구조화하고,
`main`과 `components`만 잘 정의해두면 별도 설계 문서 없이 설계 + Python 코드만으로 바로 개발을
시작할 수 있다는 것이 원문의 제안이다.

## 기본 규칙

- 이 사용 시점 기준 웹페이지에서 사용 가능한 Python 버전은 **3.11.2**.
- 모든 Python 코드는 **함수로 캡슐화**한다.
- 코드를 직접 실행하는 대신 `def do():`를 정의하고 `do()`를 호출해 테스트한다.

```python
# 일반적인 main.py
a = 1
b = 1
value = a + b
print(value)
```

```python
# 함수화한 main.py
def summation(a, b):
    return a + b

# 아래 세 줄을 주석 처리하면 Python 코드가 즉시 실행되지 않는다.
a = 1
b = 1
summation(a, b)
```

UI에 채울 데이터도 Python 코드로 작성한다. 예를 들어 `NODE` 데이터의 `X` 값만 Drop List에
채우고 싶다면 다음과 같이 작성한다.

```python
# components.py
def getNodeX4CompDropList():
    civil = MidasAPI(Product.CIVIL, "KR")
    nodeEntries = civil.dbRead("NODE")
    nodeXs = []
    for entry_id, entry_values in nodeEntries.items():
        x_value = entry_values.get("X")
        if x_value is not None:
            nodeXs.append(x_value)
    return nodeXs  # [1, 2, 3, ...] NODE의 X 값
```

> `MidasAPI(...).dbRead("NODE")`는 이 Python 래퍼를 통해 JSON Manual의
> [`GET /db/NODE`](../../manual/03_DB_Node_Element.md) 엔드포인트를 호출하는 것으로 보인다.
> Plug-in 개발 시 `dbRead`/`dbWrite` 등에 넘기는 테이블 코드(`"NODE"`, `"ELEM"` 등)는
> `docs/manual/`에 정리된 `/db/*` 엔드포인트의 URI 코드와 대응되므로, Plug-in 코드를 읽을 때
> 해당 엔드포인트 문서를 함께 참고하면 스키마를 빠르게 파악할 수 있다.

`main.py`에 들어갈 함수는 파라미터를 받는 형태로 작성한다. 예를 들어 Drop List에서 선택한
특정 Node의 X 값을 2배로 만드는 메인 로직이 있다면, 선택된 Node X 값을 파라미터로 넘기는
방식으로 작성한다.

```python
# main.py
def main(selectedNodeX):
    result = selectedNodeX * 2
    print(result)

# 테스트용 코드
selectedNodeX = 1  # Drop List(Node X)에서 1을 선택했다고 가정
main(selectedNodeX)  # 출력: 2
```

## Python 파일 3가지 카테고리

| 파일 | 역할 |
| --- | --- |
| `main.py` | UI에서 값을 받아 최종적으로 실행되는 로직을 정의 |
| `components.py` | UI 컴포넌트에 채울 값을 정의. 실제 데이터를 반환하므로 설계 문서 설명 없이도 UI에 바로 채울 수 있음 |
| (자유 명명, 예: `sub_logics.py`) | `main` 함수를 보조하는 로직을 정의. 모든 코드를 `main`에 몰아넣으면 가독성이 떨어지므로 하나 또는 여러 파일로 분리 |

```python
# main.py
from multiple import calc2x

def main(selectedNodeX):
    result = calc2x(selectedNodeX)
    print(result)

selectedNodeX = 1
main(selectedNodeX)
```

```python
# multiple.py (보조 로직 파일 — 이름은 자유)
def calc2x(value):
    return value * 2
```

## Python 코드 테스트 가이드

Plug-in Item 개발 환경에서 Python 코드를 직접 실행해보면 바로 적용 가능한 코드를 만들 수 있다.

1. VS Code에 **Live Server** 확장을 설치한다 — 저장만으로 즉시 실행 가능한 로컬 서버를 띄워
   웹페이지를 연다.
2. `engineers-api-python` 저장소를 받아 `pyscript_tester` 디렉터리를 추가한다.
3. 새 프로젝트를 시작하려면 `pyscript_tester`를 복사해 새 폴더를 만든다.
4. 복사한 폴더를 VS Code에서 프로젝트로 연다.
5. 좌측 트리에서 `index.html`을 클릭한 뒤 우측 하단 **Go Live**를 클릭한다. Live Server가
   정상 설치돼 있으면 우측 하단에 "Go Live"가 보인다.
6. 브라우저가 열리고 테스트 화면이 뜨면 테스트 환경 구성이 완료된 것이다.

기본 구조는 `pyscript_main.py`를 실행하는 방식이다. 보조 Python 파일을 만들어 쓰려면, 보조
파일을 만든 뒤 파일명을 `pyscript_config.json`에 추가하면 된다.

> ⚠️ 원문에는 `engineers-api-python` 저장소·스크린샷이 언급되나, 실제 저장소 URL은 원문
> 텍스트에 노출되어 있지 않아(이미지로만 안내) 이 문서에는 추측해 넣지 않았다. 필요 시 원문
> 아티클을 직접 열어 이미지 속 링크를 확인할 것.
