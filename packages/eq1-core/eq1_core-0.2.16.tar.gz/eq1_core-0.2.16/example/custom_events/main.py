# Core에 이벤트 등록 예제
import os
import asyncio

os.environ["DB_URL"] = "mysql+pymysql://crefle:passwd@localhost:3307/eq1"
os.environ["LOG_PATH"] = "./public/logs"

from eq1core.signal import (
    create_signal, connect_signal, emit_signal, emit_signal_async, global_signal_emitter, Signal
)
from eq1core import Core, InspectionMode, DataServiceFactory, AppLogger


def maintenance_handler(equipment_id: str, issue: str):
    """장비 정비 필요 이벤트 핸들러"""
    print(f"🔧 Maintenance needed for {equipment_id}: {issue}")


def notification_handler(title: str, message: str):
    """알림 이벤트 핸들러"""
    print(f"📢 {title}: {message}")


async def async_maintenance_handler(equipment_id: str, issue: str):
    """비동기 장비 정비 필요 이벤트 핸들러"""
    print(f"🔄 Async maintenance check for {equipment_id}: {issue}")
    await asyncio.sleep(0.1)  # 비동기 작업 시뮬레이션
    print(f"✅ Maintenance task completed for {equipment_id}")


def core_camera_error_handler(error_message: str):
    """Core의 카메라 에러 핸들러"""
    print(f"📷 Camera Error: {error_message}")


def core_system_error_handler(error_message: str):
    """Core의 시스템 에러 핸들러"""
    print(f"⚠️ System Error: {error_message}")


def core_status_changed_handler(status: str):
    """Core의 상태 변경 핸들러"""
    print(f"🔄 Status Changed: {status}")


def custom_alert_handler(level: str, message: str, timestamp: str):
    """커스텀 알림 핸들러"""
    print(f"🚨 [{level}] {message} at {timestamp}")


def quality_check_handler(product_id: str, result: str, confidence: float):
    """품질 검사 핸들러"""
    print(f"🔍 Quality check for {product_id}: {result} (confidence: {confidence:.2f})")


def production_line_handler(line_id: str, status: str, speed: int):
    """생산라인 상태 핸들러"""
    print(f"🏭 Production line {line_id}: {status} at {speed} units/min")


def main():
    print("=== Core에 이벤트 등록 예제 ===\n")
    
    # Core 인스턴스 생성 (DataServiceFactory 사용)
    data_service = DataServiceFactory.get_service('db')
    core = Core(
        uuid="test_uuid",
        group_name="test_group", 
        data_service=data_service,
        mode=InspectionMode.MULTI_SHOT
    )
    
    # 방법 1: Core의 기본 Signal에 핸들러 연결
    print("## 방법 1: Core의 기본 Signal에 핸들러 연결")
    
    # Core의 기본 Signal들에 핸들러 연결
    core.camera_error.connect(core_camera_error_handler)
    core.system_error.connect(core_system_error_handler)
    core.status_changed.connect(core_status_changed_handler)
    
    # Core의 Signal 발생 테스트
    core.camera_error.emit("Camera connection lost")
    core.system_error.emit("Memory allocation failed")
    core.status_changed.emit("Initializing cameras")
    print()
    
    # 방법 2: Core 인스턴스에 새로운 Signal 동적 추가
    print("## 방법 2: Core 인스턴스에 새로운 Signal 동적 추가")
    
    # Core에 새로운 Signal들 추가
    core.custom_alert = Signal(str, str, str)  # level, message, timestamp
    core.quality_check = Signal(str, str, float)  # product_id, result, confidence
    core.production_line_status = Signal(str, str, int)  # line_id, status, speed
    
    # 새로 추가된 Signal들에 핸들러 연결
    core.custom_alert.connect(custom_alert_handler)
    core.quality_check.connect(quality_check_handler)
    core.production_line_status.connect(production_line_handler)
    
    # 새로운 Signal들 발생 테스트
    core.custom_alert.emit("WARNING", "Temperature threshold exceeded", "2024-01-15 14:30:25")
    core.quality_check.emit("PROD_001", "PASS", 0.95)
    core.production_line_status.emit("LINE_A", "RUNNING", 120)
    print()
    
    # 방법 3: 여러 핸들러를 하나의 Signal에 연결
    print("## 방법 3: 여러 핸들러를 하나의 Signal에 연결")
    
    # 추가 핸들러 함수들
    def alert_logger(level: str, message: str, timestamp: str):
        print(f"📝 Logging alert: [{level}] {message}")
    
    def alert_notifier(level: str, message: str, timestamp: str):
        print(f"📧 Sending notification for: {message}")
    
    # 하나의 Signal에 여러 핸들러 연결
    core.custom_alert.connect(alert_logger)
    core.custom_alert.connect(alert_notifier)
    
    # 여러 핸들러가 연결된 Signal 발생
    core.custom_alert.emit("ERROR", "Critical system failure", "2024-01-15 14:35:10")
    print()
    
    # 방법 4: 사용자 정의 Signal 생성 및 Core에서 사용
    print("## 방법 4: 사용자 정의 Signal 생성 및 Core에서 사용")
    
    # 전역 Signal 생성
    create_signal("maintenance_required", str, str)
    create_signal("custom_notification", str, str)
    
    # 핸들러 연결
    connect_signal("maintenance_required", maintenance_handler)
    connect_signal("custom_notification", notification_handler)
    
    # Core에서 사용자 정의 Signal 발생
    emit_signal("maintenance_required", "MACHINE_001", "Filter replacement needed")
    emit_signal("custom_notification", "System Alert", "All systems operational")
    print()
    
    # 방법 5: 여러 핸들러 연결
    print("## 방법 5: 여러 핸들러 연결")
    
    create_signal("global_maintenance", str, str)
    connect_signal("global_maintenance", maintenance_handler)
    connect_signal("global_maintenance", notification_handler)
    
    emit_signal("global_maintenance", "MACHINE_002", "Calibration required")
    print()
    
    # 방법 6: 비동기 핸들러 연결
    print("## 방법 6: 비동기 핸들러 연결")
    
    create_signal("async_maintenance", str, str)
    connect_signal("async_maintenance", maintenance_handler)
    connect_signal("async_maintenance", async_maintenance_handler, is_async=True)
    
    # 비동기 시그널 발생
    async def run_async_example():
        await emit_signal_async("async_maintenance", "MACHINE_003", "Software update needed")
    
    asyncio.run(run_async_example())
    print()
    
    # 방법 7: Core의 검사 완료 Signal에 핸들러 연결
    print("## 방법 7: Core의 검사 완료 Signal에 핸들러 연결")
    
    def on_inspection_part_finished(result_data):
        """검사 파트 완료 핸들러"""
        print(f"✅ Inspection part finished: {result_data}")
    
    def on_inspection_group_finished(result_data):
        """검사 그룹 완료 핸들러"""
        print(f"🎯 Inspection group finished: {result_data}")
    
    def on_one_frame_finished(frame_data_list):
        """단일 프레임 완료 핸들러"""
        print(f"📸 One frame finished: {len(frame_data_list)} frames processed")
    
    # Core의 검사 관련 Signal에 핸들러 연결
    core.inspection_part_finished.connect(on_inspection_part_finished)
    core.inspection_group_finished.connect(on_inspection_group_finished)
    core.one_frame_finished.connect(on_one_frame_finished)
    
    # 방법 8: 타입 검증 없이 사용
    print("## 방법 8: 타입 검증 없이 사용")
    
    create_signal("flexible_event")
    connect_signal("flexible_event", lambda x, y: print(f"Flexible handler: {x}, {y}"))
    emit_signal("flexible_event", "test", 123)  # 타입 검증 없이 실행
    print()
    
    # 방법 9: Core에 추가된 Signal 정보 확인
    print("## 방법 9: Core에 추가된 Signal 정보 확인")
    
    # Core 인스턴스의 모든 Signal 속성 확인
    core_signals = []
    for attr_name in dir(core):
        attr_value = getattr(core, attr_name)
        if isinstance(attr_value, Signal):
            core_signals.append((attr_name, attr_value))
    
    print(f"Core 인스턴스의 Signal 개수: {len(core_signals)}")
    for signal_name, signal in core_signals:
        print(f"  - {signal_name}: {signal}")
    
    print()
    
    # 방법 10: Signal 정보 조회
    print("## 방법 10: Signal 정보 조회")
    
    # 등록된 모든 Signal 조회
    all_signals = global_signal_emitter.get_all_signals()
    print(f"전역 등록된 Signal 개수: {len(all_signals)}")
    for signal_name, signal in all_signals.items():
        print(f"  - {signal_name}: {signal}")
    
    print()
    print("=== 예제 완료 ===")


if __name__ == "__main__":
    main()
