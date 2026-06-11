#!/usr/bin/env python3
"""
MIDAS NX Open API - Python 기본 예제

MIDAS Gen NX에 사각 기둥 1개를 생성하는 최소 예제입니다.

사전 준비:
  1) MIDAS Gen NX 실행
  2) Open API 메뉴에서 MAPI-Key 발급
  3) 아래 MAPI_KEY / BASE_URL 설정 (또는 환경변수 사용)

실행:
  pip install requests
  python basic_example.py
"""

import os
import json
import requests

# ── 설정 ────────────────────────────────────────────────────────────────
# Gen NX: .../gen   |   Civil NX: .../civil
BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

HEADERS = {
    "MAPI-Key": MAPI_KEY,          # ⚠️ Authorization Bearer 아님
    "Content-Type": "application/json",
}


def MidasAPI(method: str, command: str, body: dict | None = None) -> dict:
    """MIDAS NX Open API 호출 헬퍼.

    method  : "POST" | "PUT" | "GET" | "DELETE"
    command : "/doc/new", "/db/node" 등
    body    : {"Assign": {...}} 형식의 요청 바디
    """
    url = BASE_URL + command
    fn = getattr(requests, method.lower())
    res = fn(url, headers=HEADERS, json=body, timeout=10)
    print(f"{method:6} {command:14} -> {res.status_code}")
    try:
        return res.json()
    except json.JSONDecodeError:
        return {"raw": res.text}


def main() -> None:
    print("🚀 MIDAS NX Open API - Python 예제")
    print(f"📍 Base URL: {BASE_URL}\n")

    # 1) 새 문서
    MidasAPI("POST", "/doc/new", {})

    # 2) 단위 (대만 RC 관행: m, tonf)
    MidasAPI("PUT", "/db/unit", {"Assign": {"1": {"DIST": "M", "FORCE": "TONF"}}})

    # 3) 재료 (RC C32)
    MidasAPI("POST", "/db/matl", {"Assign": {1: {
        "TYPE": "CONC", "NAME": "C32",
        "PARAM": [{"P_TYPE": 1, "STANDARD": "AS17(RC)", "DB": "C32"}],
    }}})

    # 4) 단면 (600x600 사각)
    MidasAPI("POST", "/db/sect", {"Assign": {1: {
        "SECTTYPE": "DBUSER", "SECT_NAME": "C600",
        "SECT_BEFORE": {"SHAPE": "SB", "DATATYPE": 2,
                        "SECT_I": {"vSIZE": [0.6, 0.6]}},
    }}})

    # 5) 노드 (3.2m 기둥)
    MidasAPI("POST", "/db/node", {"Assign": {
        1: {"X": 0, "Y": 0, "Z": 0},
        2: {"X": 0, "Y": 0, "Z": 3.2},
    }})

    # 6) 기둥 요소 (BEAM)
    MidasAPI("POST", "/db/elem", {"Assign": {1: {
        "TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0,
    }}})

    # 7) 하단 고정 지지
    MidasAPI("POST", "/db/cons", {"Assign": {1: {
        "ITEMS": [{"ID": 1, "CONSTRAINT": "1111111"}],
    }}})

    # 8) 저장
    MidasAPI("POST", "/doc/save")

    print("\n✅ 완료! MIDAS Gen NX 화면에서 기둥을 확인하세요.")


if __name__ == "__main__":
    main()
