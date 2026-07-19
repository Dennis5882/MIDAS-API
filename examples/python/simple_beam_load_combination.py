#!/usr/bin/env python3
"""
MIDAS NX Open API - Python 예제: 단순보 하중조합

10m 단순보(양단 핀/롤러 지지)를 20등분해서 절점/요소를 생성하고,
자중(DL) + 등분포 보하중(SIDL)을 적용한 뒤 하중조합까지 구성하는 예제입니다.
basic_example.py(기둥 1개짜리 최소 예제)보다 한 단계 더 실전에 가까운 흐름을 보여줍니다.

출처: MIDAS Support - Example: Python
https://support.midasuser.com/hc/en-us/articles/30230181806361-Example-Python
(공식 튜토리얼 기사를 이 저장소 스타일/네이밍에 맞춰 재구성한 버전입니다)

사전 준비:
  1) MIDAS Civil NX 또는 Gen NX 실행
  2) Open API 메뉴에서 MAPI-Key 발급
  3) 아래 MAPI_KEY / BASE_URL 설정 (또는 환경변수 사용)

실행:
  pip install requests
  python simple_beam_load_combination.py
"""

import os
import json
import requests

# ── 설정 ────────────────────────────────────────────────────────────────
BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/civil")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

HEADERS = {
    "MAPI-Key": MAPI_KEY,
    "Content-Type": "application/json",
}


def MidasAPI(method: str, command: str, body: dict | None = None) -> dict:
    """MIDAS NX Open API 호출 헬퍼."""
    url = BASE_URL + command
    fn = getattr(requests, method.lower())
    res = fn(url, headers=HEADERS, json=body, timeout=10)
    print(f"{method:6} {command:14} -> {res.status_code}")
    try:
        return res.json()
    except json.JSONDecodeError:
        return {"raw": res.text}


def main() -> None:
    print("🚀 MIDAS NX Open API - 단순보 하중조합 예제")
    print(f"📍 Base URL: {BASE_URL}\n")

    # ── 입력값 ──────────────────────────────────────────────────────────
    unit_dist, unit_force = "M", "KN"

    length, height, width = 10.0, 1.0, 0.8   # 보 길이/단면 높이/폭 (m)
    beam_load = -30.0                        # 추가 등분포 하중 (kN/m, SIDL)

    mat_standard, mat_grade = "AS17(RC)", "C32"

    material_id, section_id = 1, 1
    num_divisions = 20                       # 보를 20등분

    # 1) 새 문서
    MidasAPI("POST", "/doc/new", {})

    # 2) 단위
    MidasAPI("PUT", "/db/unit", {"Assign": {"1": {"DIST": unit_dist, "FORCE": unit_force}}})

    # 3) 재료 (RC C32)
    MidasAPI("POST", "/db/matl", {"Assign": {material_id: {
        "TYPE": "CONC", "NAME": mat_grade,
        "PARAM": [{"P_TYPE": 1, "STANDARD": mat_standard, "DB": mat_grade}],
    }}})

    # 4) 단면 (직사각형 값입력 단면)
    MidasAPI("POST", "/db/sect", {"Assign": {section_id: {
        "SECTTYPE": "DBUSER", "SECT_NAME": "Rectangular",
        "SECT_BEFORE": {
            "USE_SHEAR_DEFORM": True, "SHAPE": "SB", "DATATYPE": 2,
            "SECT_I": {"vSIZE": [height, width]},
        },
    }}})

    # 5) 절점 (0 ~ length를 num_divisions등분)
    interval = length / num_divisions
    node_assign = {
        i + 1: {"X": round(i * interval, 6), "Y": 0.0, "Z": 0.0}
        for i in range(num_divisions + 1)
    }
    MidasAPI("POST", "/db/node", {"Assign": node_assign})

    # 6) 요소 (인접 절점을 순서대로 BEAM으로 연결)
    elem_assign = {
        i + 1: {"TYPE": "BEAM", "MATL": material_id, "SECT": section_id, "NODE": [i + 1, i + 2]}
        for i in range(num_divisions)
    }
    MidasAPI("POST", "/db/elem", {"Assign": elem_assign})

    # 7) 지지조건 (시작단 핀, 끝단 롤러)
    last_node_id = num_divisions + 1
    MidasAPI("POST", "/db/cons", {"Assign": {
        1: {"ITEMS": [{"ID": 1, "CONSTRAINT": "1111000"}]},
        last_node_id: {"ITEMS": [{"ID": 1, "CONSTRAINT": "0111000"}]},
    }})

    # 8) 하중 케이스 (자중용 DL, 추가하중용 SIDL)
    MidasAPI("POST", "/db/stld", {"Assign": {
        1: {"NAME": "DL", "TYPE": "USER", "DESC": "Dead Load"},
        2: {"NAME": "SIDL", "TYPE": "USER", "DESC": "Super Imposed Dead Load"},
    }})

    # 9) 자중 (DL 하중 케이스에 -Z 방향 1배)
    MidasAPI("POST", "/db/bodf", {"Assign": {"1": {"LCNAME": "DL", "FV": [0, 0, -1]}}})

    # 10) 등분포 보하중 (모든 요소에 SIDL 적용)
    bmld_assign = {
        i + 1: {"ITEMS": [{
            "ID": 1, "LCNAME": "SIDL", "CMD": "BEAM", "TYPE": "UNILOAD",
            "DIRECTION": "GZ", "D": [0, 1], "P": [beam_load, beam_load],
        }]}
        for i in range(num_divisions)
    }
    MidasAPI("POST", "/db/bmld", {"Assign": bmld_assign})

    # 11) 하중조합 (DL*1.2 + SIDL*1.5)
    MidasAPI("POST", "/db/lcom-gen", {"Assign": {1: {
        "NAME": "Comb1", "ACTIVE": "ACTIVE", "iTYPE": 0,
        "vCOMB": [
            {"ANAL": "ST", "LCNAME": "DL", "FACTOR": 1.2},
            {"ANAL": "ST", "LCNAME": "SIDL", "FACTOR": 1.5},
        ],
    }}})

    # 12) 저장
    MidasAPI("POST", "/doc/save")

    print("\n✅ 완료! MIDAS NX 화면에서 단순보와 하중조합을 확인하세요.")


if __name__ == "__main__":
    main()
