# PySide6 Signal/Slot 패턴 기반 이벤트 시스템 가이드

## 개요

이 문서는 EQ-1 Core 프로젝트에서 PySide6의 Signal/Slot 패턴을 참고하여 구현한 이벤트 시스템의 사용법을 설명합니다.

## 주요 특징

- **PySide6 호환성**: PySide6의 Signal/Slot 패턴과 유사한 API
- **비동기 지원**: 동기/비동기 슬롯 모두 지원
- **스레드 안전**: 멀티스레드 환경에서 안전한 사용
- **컨텍스트 관리**: 이벤트 컨텍스트와 우선순위 지원
- **기존 호환성**: 기존 Event 클래스와의 호환성 유지

## 핵심 클래스

### Signal
PySide6의 Signal과 유사한 이벤트 시그널 클래스입니다.

```python
from eq1core.signal import Signal

# 시그널 생성
camera_signal = Signal("camera_frame_ready", "카메라 프레임 준비 완료")

# 슬롯 함수 정의
def on_frame_ready(frame_data):
    print(f"프레임 수신: {len(frame_data)} bytes")

# 슬롯 연결
camera_signal.connect(on_frame_ready)

# 시그널 발생
frame_data = b"fake_frame_data" * 1000
camera_signal.emit(frame_data)
```

### EventEmitter
이벤트 발생 및 관리 클래스입니다.

```python
from eq1core.signal import EventEmitter

# 이벤트 에미터 생성
emitter = EventEmitter()

# 시그널 생성
camera_signal = emitter.create_signal("camera_frame", "카메라 프레임")

# 슬롯 연결
def on_frame(frame_data):
    print(f"프레임 수신: {len(frame_data)} bytes")

camera_signal.connect(on_frame)

# 시그널 발생
frame_data = b"fake_frame" * 100
emitter.emit("camera_frame", frame_data)
```

### EventContext
이벤트 컨텍스트 정보를 담는 클래스입니다.

```python
from eq1core.signal import EventContext, EventPriority
import time

# 컨텍스트 생성
context = EventContext(
    source="camera_1",
    timestamp=time.time(),
    priority=EventPriority.HIGH,
    metadata={"lot_id": "LOT001", "product_type": "PCB"}
)

# 컨텍스트와 함께 시그널 발생
def on_inspection_complete(context, result):
    print(f"검사 완료 - 소스: {context.source}")
    print(f"우선순위: {context.priority.name}")
    print(f"결과: {result}")

inspection_signal = Signal("inspection_complete", "검사 완료")
inspection_signal.connect(on_inspection_complete)

result = {"status": "PASS", "defects": 0}
inspection_signal.emit_with_context(context, result)
```

## 사용법

### 1. 기본 Signal/Slot 사용법

```python
from eq1core.signal import Signal

# 시그널 생성
camera_signal = Signal("camera_frame_ready", "카메라 프레임 준비 완료")

# 여러 슬롯 연결
def on_frame_ready(frame_data):
    print(f"📸 프레임 수신: {len(frame_data)} bytes")

def on_frame_processed(frame_data):
    print(f"🔍 프레임 처리 완료: {len(frame_data)} bytes")

camera_signal.connect(on_frame_ready)
camera_signal.connect(on_frame_processed)

# 시그널 발생
frame_data = b"fake_frame_data" * 1000
camera_signal.emit(frame_data)

print(f"연결된 슬롯 수: {camera_signal.slot_count}")
```

### 2. 비동기 Signal/Slot 사용법

```python
import asyncio
from eq1core.signal import Signal

async def async_frame_processor(frame_data):
    await asyncio.sleep(0.1)  # 비동기 처리 시뮬레이션
    print(f"🔄 비동기 프레임 처리: {len(frame_data)} bytes")

def sync_frame_logger(frame_data):
    print(f"📝 동기 프레임 로깅: {len(frame_data)} bytes")

# 비동기 슬롯 연결
camera_signal = Signal("camera_frame_ready", "카메라 프레임 준비 완료")
camera_signal.connect(sync_frame_logger, is_async=False)
camera_signal.connect(async_frame_processor, is_async=True)

# 비동기 시그널 발생
frame_data = b"async_frame_data" * 500
await camera_signal.emit_async(frame_data)
```

### 3. 전역 이벤트 에미터 사용법

```python
from eq1core.signal import connect_signal, emit_signal

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
```

### 4. 이벤트 컨텍스트 매니저 사용법

```python
from eq1core.signal import EventEmitter, EventPriority

def on_camera_event(context, event_type: str, data):
    print(f"📹 카메라 이벤트: {event_type}")
    print(f"   소스: {context.source}")
    print(f"   우선순위: {context.priority.name}")
    print(f"   데이터: {data}")

# EventEmitter 인스턴스 생성
emitter = EventEmitter()
camera_signal = emitter.create_signal("camera_event", "카메라 이벤트")
camera_signal.connect(on_camera_event)

# 컨텍스트 매니저 사용
with emitter.context("camera_2", EventPriority.CRITICAL, {"camera_id": "CAM002"}) as ctx:
    camera_signal.emit_with_context(ctx, "frame_captured", {"width": 1920, "height": 1080})
    camera_signal.emit_with_context(ctx, "exposure_changed", {"exposure_time": 1000})
```

### 5. 시그널 관리 기능

```python
from eq1core.signal import EventEmitter

def temp_handler(data):
    print(f"임시 핸들러: {data}")

# 시그널 생성 및 관리
emitter = EventEmitter()
test_signal = emitter.create_signal("test_signal", "테스트 시그널")

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
```

### 6. 비동기 이벤트 워크플로우

```python
import asyncio
from eq1core.signal import Signal

async def async_image_processor(image_data):
    await asyncio.sleep(0.05)
    print(f"🖼️ 이미지 처리 완료: {len(image_data)} bytes")
    return {"processed": True, "size": len(image_data)}

async def async_result_saver(result):
    await asyncio.sleep(0.02)
    print(f"💾 결과 저장 완료: {result}")

def sync_logger(message):
    print(f"📝 로그: {message}")

# 비동기 워크플로우 시그널
workflow_signal = Signal("image_workflow", "이미지 처리 워크플로우")
workflow_signal.connect(sync_logger, is_async=False)
workflow_signal.connect(async_image_processor, is_async=True)
workflow_signal.connect(async_result_saver, is_async=True)

# 비동기 워크플로우 실행
image_data = b"large_image_data" * 2000
await workflow_signal.emit_async(image_data)
```

## 기존 검사 이벤트 사용법

미리 정의된 검사 이벤트 시그널들을 사용할 수 있습니다.

```python
from eq1core.signal import InspectionEvents

def on_part_finished(part_id: str, result: dict):
    print(f"✅ 항목 검사 완료: {part_id} - {result['status']}")

def on_group_finished(group_id: str, summary: dict):
    print(f"🏁 그룹 검사 완료: {group_id}")
    print(f"   총 항목: {summary['total_parts']}")
    print(f"   통과: {summary['passed']}")
    print(f"   실패: {summary['failed']}")

# 미리 정의된 검사 이벤트 시그널 사용
InspectionEvents.inspection_part_finished.connect(on_part_finished)
InspectionEvents.inspection_group_finished.connect(on_group_finished)

# 검사 이벤트 발생
InspectionEvents.inspection_part_finished.emit("PART_001", {"status": "PASS", "score": 0.98})
InspectionEvents.inspection_group_finished.emit("GROUP_B", {
    "total_parts": 10,
    "passed": 9,
    "failed": 1
})
```

## 이벤트 우선순위

이벤트 우선순위는 `EventPriority` 열거형으로 정의됩니다.

```python
from eq1core.signal import EventPriority

# 우선순위 레벨
EventPriority.LOW      # 0 - 낮음
EventPriority.NORMAL   # 1 - 보통
EventPriority.HIGH     # 2 - 높음
EventPriority.CRITICAL # 3 - 긴급
```

## 스레드 안전성

모든 Signal과 EventEmitter 클래스는 스레드 안전하게 설계되었습니다.

```python
import threading
from eq1core.signal import Signal

signal = Signal("thread_safe", "스레드 안전 테스트")

def worker():
    def slot(data):
        print(f"스레드 {threading.current_thread().name}: {data}")
    
    signal.connect(slot)
    signal.emit("테스트 데이터")

# 여러 스레드에서 동시 사용
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

## 성능 최적화 팁

1. **슬롯 함수 최적화**: 슬롯 함수는 가능한 한 빠르게 실행되도록 설계
2. **비동기 활용**: 시간이 오래 걸리는 작업은 비동기 슬롯으로 처리
3. **불필요한 연결 해제**: 사용하지 않는 슬롯은 반드시 연결 해제
4. **시그널 비활성화**: 일시적으로 사용하지 않는 시그널은 비활성화

## 디버깅 및 로깅

시그널 디버깅을 위한 유용한 속성들:

```python
signal = Signal("debug_test", "디버깅 테스트")

# 연결된 슬롯 개수 확인
print(f"슬롯 개수: {signal.slot_count}")

# 시그널 정보 출력
print(f"시그널 정보: {signal}")

# 시그널 활성화 상태 확인
print(f"활성화 상태: {signal._enabled}")
```

## 기존 코드와의 호환성

기존 Event 클래스와의 호환성을 위해 EventRegistry 클래스가 제공됩니다.

```python
from eq1core.signal import EventRegistry

# 기존 방식으로 이벤트 등록
registry = EventRegistry()
event = CustomEvent("custom_event", "사용자 정의 이벤트")
registry.register_event(event)

# 새로운 방식으로 시그널 사용
emitter = registry.emitter
signal = emitter.create_signal("new_signal", "새로운 시그널")
```

## 결론

PySide6 Signal/Slot 패턴을 참고한 이벤트 시스템은 다음과 같은 장점을 제공합니다:

- **직관적인 API**: PySide6 개발자들에게 친숙한 인터페이스
- **강력한 기능**: 비동기 처리, 컨텍스트 관리, 우선순위 지원
- **안정성**: 스레드 안전성과 오류 처리
- **확장성**: 새로운 시그널과 슬롯을 쉽게 추가 가능
- **호환성**: 기존 코드와의 호환성 유지

이 시스템을 활용하여 EQ-1 Core 프로젝트의 이벤트 처리를 더욱 효율적이고 유지보수하기 쉽게 만들 수 있습니다.
