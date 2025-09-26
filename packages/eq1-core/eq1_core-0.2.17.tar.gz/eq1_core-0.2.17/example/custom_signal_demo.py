#!/usr/bin/env python3
"""
Custom Signal 사용 데모

이 예시는 Core에서 custom signal을 생성하고 
core.my_signal.emit 형태로 사용하는 방법을 보여줍니다.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.eq1core.core import Core
from src.eq1core.data import InspectionMode


class MockDataService:
    """데모용 Mock 데이터 서비스"""
    
    def get_active_cameras(self, uuid):
        return []
    
    def get_active_engines(self, uuid):
        return []
    
    def get_active_inspection_parts_by_engine_name(self, name):
        return []
    
    def get_last_group_serial(self, group_name):
        return "DEMO-001"
    
    def is_group_result_empty(self, group_name):
        return True
    
    def set_unlocked_group_results_as_failed(self, group_name, serial):
        return True
    
    def save_inspection_part_results(self, results):
        return True


def on_custom_event(data):
    """Custom signal 핸들러"""
    print(f"🎉 Custom event received: {data}")


def on_status_update(status, timestamp):
    """Status update signal 핸들러"""
    print(f"📊 Status update: {status} at {timestamp}")

def on_data_update(data):
    """Data update signal 핸들러"""
    print(f"📈 Data update: {data}")


def main():
    # Core 인스턴스 생성 (Mock 데이터 서비스 사용)
    uuid = "demo-uuid"
    group_name = "demo-group"
    data_service = MockDataService()
    core = Core(uuid, group_name, data_service, InspectionMode.MULTI_SHOT)
    
    print("🚀 Custom Signal Demo 시작")
    print("=" * 50)
    
    # 1. Custom signal 생성 (PySide6 스타일)
    print("1. Custom signal 생성 (PySide6 스타일)...")
    my_signal = core.create_custom_signal("my_signal", str)
    status_signal = core.create_custom_signal("status_update", str, str)
    data_signal = core.create_custom_signal("data_update", dict)
    
    # 2. 핸들러 연결
    print("2. 핸들러 연결...")
    my_signal.connect(on_custom_event)
    status_signal.connect(on_status_update)
    data_signal.connect(on_data_update)
    
    # 3. core.my_signal.emit 형태로 사용
    print("3. core.my_signal.emit 형태로 signal 발생...")
    
    # ✅ 이제 이렇게 사용할 수 있습니다!
    core.my_signal.emit("Hello from custom signal!")
    core.status_update.emit("Processing", "2024-01-01 12:00:00")
    
    print("\n4. 추가 데이터와 함께 signal 발생...")
    core.my_signal.emit("Simple string data")
    core.status_update.emit("Completed", "2024-01-01 12:01:00")
    core.data_update.emit({"message": "Complex data", "count": 42, "timestamp": "2024-01-01 12:01:00"})
    
    print("\n5. 동적으로 새로운 signal 생성 및 사용...")
    # 동적으로 새로운 signal 생성 (PySide6 스타일)
    core.create_custom_signal("new_signal", str)
    core.new_signal.connect(lambda x: print(f"🆕 New signal: {x}"))
    
    # 즉시 사용 가능
    core.new_signal.emit("Dynamic signal works!")
    
    print("\n6. Signal 존재 여부 확인...")
    print(f"my_signal exists: {hasattr(core, 'my_signal')}")
    print(f"status_update exists: {hasattr(core, 'status_update')}")
    print(f"data_update exists: {hasattr(core, 'data_update')}")
    print(f"non_existent exists: {hasattr(core, 'non_existent')}")
    
    print("\n7. 모든 custom signal 조회...")
    all_signals = core.get_all_custom_signals()
    for name, signal in all_signals.items():
        print(f"  - {name}: {signal}")
    
    print("\n✅ Demo 완료!")


if __name__ == "__main__":
    main()
