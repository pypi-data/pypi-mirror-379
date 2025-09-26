#!/usr/bin/env python3
"""
EventEmitter 데모

이 예시는 EventEmitter의 새로운 API를 테스트합니다.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.eq1core.signal import SignalEmitter, create_signal, connect_signal, emit_signal


def on_user_event(data: str):
    """사용자 이벤트 핸들러"""
    print(f"👤 User event: {data}")


def on_system_event(event_type: str, details: dict):
    """시스템 이벤트 핸들러"""
    print(f"🖥️ System event: {event_type} - {details}")


def on_status_event(status: str, code: int):
    """상태 이벤트 핸들러"""
    print(f"📊 Status event: {status} (code: {code})")


def main():
    print("🚀 EventEmitter 데모 시작")
    print("=" * 50)
    
    # 1. SignalEmitter 인스턴스 생성
    print("1. SignalEmitter 인스턴스 생성...")
    emitter = SignalEmitter()
    
    # 2. 타입이 지정된 Signal 생성
    print("\n2. 타입이 지정된 Signal 생성...")
    user_signal = emitter.create_signal("user_event", str)
    system_signal = emitter.create_signal("system_event", str, dict)
    status_signal = emitter.create_signal("status_event", str, int)
    
    print(f"  - {user_signal}")
    print(f"  - {system_signal}")
    print(f"  - {status_signal}")
    
    # 3. 핸들러 연결
    print("\n3. 핸들러 연결...")
    user_signal.connect(on_user_event)
    system_signal.connect(on_system_event)
    status_signal.connect(on_status_event)
    
    # 4. Signal 발생
    print("\n4. Signal 발생...")
    emitter.emit("user_event", "User logged in")
    emitter.emit("system_event", "error", {"code": 500, "message": "Internal server error"})
    emitter.emit("status_event", "processing", 200)
    
    # 5. 전역 편의 함수 사용
    print("\n5. 전역 편의 함수 사용...")
    
    # 전역 Signal 생성
    global_signal = create_signal("global_event", str, int)
    global_signal.connect(lambda msg, num: print(f"🌍 Global event: {msg} - {num}"))
    
    # 전역 Signal 발생
    emit_signal("global_event", "Hello from global", 42)
    
    # 6. 동적 Signal 생성 및 사용
    print("\n6. 동적 Signal 생성 및 사용...")
    
    # connect_signal로 자동 생성
    connect_signal("dynamic_event", lambda x: print(f"⚡ Dynamic event: {x}"))
    emit_signal("dynamic_event", "Auto-created signal works!")
    
    # 7. 모든 Signal 조회
    print("\n7. 모든 Signal 조회...")
    all_signals = emitter.get_all_signals()
    for name, signal in all_signals.items():
        print(f"  - {name}: {signal}")
    
    # 8. Signal 제거
    print("\n8. Signal 제거...")
    emitter.remove_signal("user_event")
    print(f"  - user_event 제거됨")
    
    # 제거된 Signal 발생 시도
    emitter.emit("user_event", "This won't work")
    
    print("\n✅ EventEmitter 데모 완료!")


if __name__ == "__main__":
    main()
