#!/usr/bin/env python3
"""
MIDAS API - Python 예제
첫 번째 API 호출을 위한 기본 예제입니다.
"""

import requests
import json
import os
from typing import Dict, Any

# 설정
API_KEY = os.getenv("MIDAS_API_KEY", "your-api-key-here")
BASE_URL = os.getenv("MIDAS_BASE_URL", "https://your-midas-server.com/api/v1")

# 헤더 준비
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def print_response(title: str, response: requests.Response) -> None:
    """응답을 보기 좋게 출력합니다."""
    print("\n" + "=" * 60)
    print(f"📌 {title}")
    print("=" * 60)
    print(f"상태 코드: {response.status_code}")
    try:
        data = response.json()
        print(f"응답:\n{json.dumps(data, indent=2, ensure_ascii=False)}")
    except json.JSONDecodeError:
        print(f"응답: {response.text}")


def get_project_info() -> None:
    """프로젝트 정보를 조회합니다."""
    try:
        response = requests.get(
            f"{BASE_URL}/db/PJCF",
            headers=headers,
            timeout=10
        )
        print_response("프로젝트 정보 조회 (GET)", response)
    except requests.exceptions.RequestException as e:
        print(f"❌ 오류: {e}")


def create_new_project() -> None:
    """새 프로젝트를 생성합니다."""
    try:
        payload = {
            "project_name": "My API Project",
            "unit": "m",
            "description": "Created via Python API"
        }
        response = requests.post(
            f"{BASE_URL}/doc/NEW",
            headers=headers,
            json=payload,
            timeout=10
        )
        print_response("새 프로젝트 생성 (POST)", response)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ 오류: {e}")
        return None


def get_unit_info() -> None:
    """단위 정보를 조회합니다."""
    try:
        response = requests.get(
            f"{BASE_URL}/db/UNIT",
            headers=headers,
            timeout=10
        )
        print_response("단위 정보 조회 (GET)", response)
    except requests.exceptions.RequestException as e:
        print(f"❌ 오류: {e}")


def get_materials() -> None:
    """재료 목록을 조회합니다."""
    try:
        response = requests.get(
            f"{BASE_URL}/db/MATL",
            headers=headers,
            timeout=10
        )
        print_response("재료 목록 조회 (GET)", response)
    except requests.exceptions.RequestException as e:
        print(f"❌ 오류: {e}")


def get_nodes() -> None:
    """노드 목록을 조회합니다."""
    try:
        response = requests.get(
            f"{BASE_URL}/db/NODE",
            headers=headers,
            timeout=10
        )
        print_response("노드 목록 조회 (GET)", response)
    except requests.exceptions.RequestException as e:
        print(f"❌ 오류: {e}")


def get_elements() -> None:
    """요소 목록을 조회합니다."""
    try:
        response = requests.get(
            f"{BASE_URL}/db/ELEM",
            headers=headers,
            timeout=10
        )
        print_response("요소 목록 조회 (GET)", response)
    except requests.exceptions.RequestException as e:
        print(f"❌ 오류: {e}")


def main() -> None:
    """메인 함수: 모든 예제를 실행합니다."""
    print("\n" + "🚀 MIDAS API Python 예제" + "\n")
    print(f"📍 Base URL: {BASE_URL}")
    print(f"🔑 API Key: {API_KEY[:10]}..." if len(API_KEY) > 10 else f"🔑 API Key: {API_KEY}")

    # 예제 1: 프로젝트 정보 조회
    get_project_info()

    # 예제 2: 새 프로젝트 생성
    result = create_new_project()

    # 예제 3: 단위 정보 조회
    get_unit_info()

    # 예제 4: 재료 목록 조회
    get_materials()

    # 예제 5: 노드 목록 조회
    get_nodes()

    # 예제 6: 요소 목록 조회
    get_elements()

    print("\n" + "=" * 60)
    print("✅ 모든 예제 완료!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
