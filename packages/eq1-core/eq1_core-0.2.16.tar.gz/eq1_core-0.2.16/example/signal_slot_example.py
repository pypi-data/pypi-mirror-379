#!/usr/bin/env python3
"""
Signal/Slot 패턴 사용 예제

이 예시는 EQ1 Core의 Signal/Slot 시스템을 PySide6 스타일로 사용하는 방법을 보여줍니다.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.eq1core.signal import (
    Signal, SignalEmitter, InspectionSignals,
    connect_signal, emit_signal
)
from typing import Any


def example_1_basic_signal_slot():
    """기본 Signal/Slot 사용법"""
    print("=== 예제 1: 기본 Signal/Slot 사용법 ===")
    
    def on_frame_ready(frame_data):
        print(f"📹 프레임 준비: {len(frame_data)} bytes")
    
    def on_frame_processed(result):
        print(f"🔍 프레임 처리 완료: {result}")
    
    # Signal 생성
    camera_signal = Signal(bytes)
    
    # 슬롯 연결
    camera_signal.connect(on_frame_ready)
    camera_signal.connect(on_frame_processed)
    
    # Signal 발생
    frame_data = b"fake_frame_data_12345"
    camera_signal.emit(frame_data)
    
    print(f"연결된 슬롯 수: {camera_signal.slot_count}")
    print()


def example_2_async_signal_slot():
    """비동기 Signal/Slot 사용법"""
    print("=== 예제 2: 비동기 Signal/Slot 사용법 ===")
    
    import asyncio
    
    def sync_frame_logger(frame_data):
        print(f"📝 동기 로깅: {len(frame_data)} bytes")
    
    async def async_frame_processor(frame_data):
        print(f"⚡ 비동기 처리 시작: {len(frame_data)} bytes")
        await asyncio.sleep(0.1)  # 가상의 비동기 작업
        print(f"✅ 비동기 처리 완료: {len(frame_data)} bytes")
    
    async def async_result_saver(result):
        print(f"💾 비동기 저장 시작: {result}")
        await asyncio.sleep(0.05)  # 가상의 저장 작업
        print(f"💾 비동기 저장 완료: {result}")
    
    # Signal 생성
    workflow_signal = Signal(bytes)
    
    # 동기/비동기 슬롯 연결
    workflow_signal.connect(sync_frame_logger, is_async=False)
    workflow_signal.connect(async_frame_processor, is_async=True)
    workflow_signal.connect(async_result_saver, is_async=True)
    
    # 비동기 Signal 발생
    async def main():
        image_data = b"large_image_data_67890"
        await workflow_signal.emit_async(image_data)
    
    asyncio.run(main())
    print()


def example_3_signal_emitter():
    """SignalEmitter 사용법"""
    print("=== 예제 3: SignalEmitter 사용법 ===")
    
    def on_camera_signal(signal_type: str, data: Any):
        print(f"📹 카메라 시그널: {signal_type} - {data}")
    
    # SignalEmitter 인스턴스 생성
    emitter = SignalEmitter()
    
    # Signal 생성
    camera_signal = emitter.create_signal("camera_signal", str, dict)
    camera_signal.connect(on_camera_signal)
    
    # Signal 발생
    camera_signal.emit("frame_captured", {"width": 1920, "height": 1080})
    camera_signal.emit("exposure_changed", {"exposure_time": 1000})
    print()


def example_4_global_signal_emitter():
    """전역 시그널 에미터 사용법"""
    print("=== 예제 4: 전역 시그널 에미터 사용법 ===")
    
    def on_lot_change(lot_id: str):
        print(f"📦 Lot 변경: {lot_id}")
    
    def on_new_group(group_id: str):
        print(f"🏭 새 그룹 시작: {group_id}")
    
    # 전역 시그널에 슬롯 연결
    connect_signal("lot_change", on_lot_change)
    connect_signal("new_group", on_new_group)
    
    # 전역 시그널 발생
    emit_signal("lot_change", "LOT2024001")
    emit_signal("new_group", "GROUP_A")
    print()


def example_5_inspection_signals():
    """검사 시그널 사용법"""
    print("=== 예제 5: 검사 시그널 사용법 ===")
    
    def on_part_finished(part_id: str, result: dict):
        print(f"✅ 항목 검사 완료: {part_id} - {result['status']}")
    
    def on_group_finished(group_id: str, summary: dict):
        print(f"🏁 그룹 검사 완료: {group_id}")
        print(f"   총 항목: {summary['total_parts']}")
        print(f"   통과: {summary['passed']}")
        print(f"   실패: {summary['failed']}")
    
    # 미리 정의된 검사 시그널 사용
    InspectionSignals.inspection_part_finished.connect(on_part_finished)
    InspectionSignals.inspection_group_finished.connect(on_group_finished)
    
    # 검사 시그널 발생
    InspectionSignals.inspection_part_finished.emit("PART_001", {"status": "PASS", "score": 0.98})
    InspectionSignals.inspection_group_finished.emit("GROUP_B", {
        "total_parts": 10,
        "passed": 9,
        "failed": 1
    })
    print()


def example_6_signal_management():
    """시그널 관리 기능 사용법"""
    print("=== 예제 6: 시그널 관리 기능 사용법 ===")
    
    def temp_handler(data):
        print(f"임시 핸들러: {data}")
    
    # 시그널 생성 및 관리
    emitter = SignalEmitter()
    test_signal = emitter.create_signal("test_signal", str)
    
    # 슬롯 연결
    test_signal.connect(temp_handler)
    print(f"연결된 슬롯 수: {test_signal.slot_count}")
    
    # 시그널 발생
    test_signal.emit("테스트 데이터")
    
    # 슬롯 연결 해제
    test_signal.disconnect(temp_handler)
    print(f"연결 해제 후 슬롯 수: {test_signal.slot_count}")
    
    # 시그널 비활성화
    test_signal.disable()
    test_signal.emit("비활성화된 시그널")  # 실행되지 않음
    
    # 시그널 다시 활성화
    test_signal.enable()
    test_signal.emit("다시 활성화된 시그널")
    
    # 시그널 제거
    emitter.remove_signal("test_signal")
    print()


def example_7_type_validation():
    """타입 검증 기능 사용법"""
    print("=== 예제 7: 타입 검증 기능 사용법 ===")
    
    def on_status_update(status: str, code: int):
        print(f"📊 상태 업데이트: {status} (코드: {code})")
    
    # 타입이 지정된 Signal 생성
    status_signal = Signal(str, int)
    status_signal.connect(on_status_update)
    
    # 올바른 타입으로 emit
    status_signal.emit("processing", 200)
    
    # 잘못된 타입으로 emit (경고 발생)
    status_signal.emit("error", "500")  # int 대신 str 전달
    
    # 타입 검증 비활성화
    status_signal.disable_type_checking()
    status_signal.emit("success", "200")  # 경고 없음
    
    # 타입 검증 다시 활성화
    status_signal.enable_type_checking()
    status_signal.emit("timeout", 408)  # 정상
    print()


def main():
    """모든 예제 실행"""
    print("🚀 Signal/Slot 패턴 예제 시작")
    print("=" * 60)
    
    example_1_basic_signal_slot()
    example_2_async_signal_slot()
    example_3_signal_emitter()
    example_4_global_signal_emitter()
    example_5_inspection_signals()
    example_6_signal_management()
    example_7_type_validation()
    
    print("✅ 모든 예제 완료!")


if __name__ == "__main__":
    main()
