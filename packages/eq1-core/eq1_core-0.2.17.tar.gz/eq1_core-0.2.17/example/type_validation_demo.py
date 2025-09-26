#!/usr/bin/env python3
"""
Signal 타입 검증 데모

이 예시는 Signal의 타입 검증 기능을 테스트합니다.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.eq1core.signal import Signal


def on_string_event(data: str):
    """문자열 이벤트 핸들러"""
    print(f"✅ String event: {data}")


def on_status_event(status: str, timestamp: str):
    """상태 이벤트 핸들러"""
    print(f"✅ Status event: {status} at {timestamp}")


def on_data_event(data: dict):
    """데이터 이벤트 핸들러"""
    print(f"✅ Data event: {data}")


def on_wrong_signature(data: str, extra: int):
    """잘못된 시그니처 핸들러"""
    print(f"❌ Wrong signature: {data}, {extra}")


def main():
    print("🚀 Signal 타입 검증 데모 시작")
    print("=" * 50)
    
    # 1. 타입이 지정된 Signal 생성
    print("1. 타입이 지정된 Signal 생성...")
    string_signal = Signal(str)
    status_signal = Signal(str, str)
    data_signal = Signal(dict)
    
    print(f"  - {string_signal}")
    print(f"  - {status_signal}")
    print(f"  - {data_signal}")
    
    # 2. 올바른 핸들러 연결
    print("\n2. 올바른 핸들러 연결...")
    string_signal.connect(on_string_event)
    status_signal.connect(on_status_event)
    data_signal.connect(on_data_event)
    
    # 3. 올바른 타입으로 emit
    print("\n3. 올바른 타입으로 emit...")
    string_signal.emit("Hello World!")
    status_signal.emit("Processing", "2024-01-01 12:00:00")
    data_signal.emit({"message": "Test data", "count": 42})
    
    # 4. 잘못된 타입으로 emit (경고 발생)
    print("\n4. 잘못된 타입으로 emit (경고 발생)...")
    string_signal.emit(123)  # int를 str 대신 전달
    status_signal.emit("Only one string")  # 인자 개수 부족
    status_signal.emit("Too", "many", "args")  # 인자 개수 초과
    data_signal.emit("Not a dict")  # str을 dict 대신 전달
    
    # 5. 잘못된 시그니처 핸들러 연결
    print("\n5. 잘못된 시그니처 핸들러 연결...")
    string_signal.connect(on_wrong_signature)
    string_signal.emit("Test with wrong handler")
    
    # 6. 타입 검증 비활성화
    print("\n6. 타입 검증 비활성화...")
    string_signal.disable_type_checking()
    print("  - 타입 검증 비활성화됨")
    string_signal.emit(123)  # 이제 경고 없이 실행됨
    
    # 7. 타입 검증 다시 활성화
    print("\n7. 타입 검증 다시 활성화...")
    string_signal.enable_type_checking()
    print("  - 타입 검증 활성화됨")
    string_signal.emit(456)  # 다시 경고 발생
    
    print("\n✅ 타입 검증 데모 완료!")


if __name__ == "__main__":
    main()
