# EQ1 Core

EQ1 검사 시스템의 핵심 라이브러리로, 카메라 제어, 통신, I/O 처리, 딥러닝 추론 등의 검사 시스템 핵심 기능을 제공합니다.

## 📦 패키지 설치

### 🚨 중요: TestPyPI 의존성 문제로 인해 로컬 설치만 가능합니다

TestPyPI의 의존성 충돌 문제로 인해 온라인 설치가 불가능합니다. 반드시 로컬 설치 파일을 사용해주세요.

### 로컬 설치 방법

```bash
# 1. eq1-core 프로젝트에서 빌드
cd /path/to/eq1-core
uv run python -m build

# 2. 다른 프로젝트에서 로컬 설치
cd /path/to/your-project
uv pip install /path/to/eq1-core/dist/eq1_core-0.1.8-py3-none-any.whl
```

### 상대 경로 설치 (권장)

```bash
# eq1-core와 같은 레벨의 다른 프로젝트에서
uv pip install ../eq1-core/dist/eq1_core-0.1.8-py3-none-any.whl
```

### 설치 확인

```bash
# 설치 확인
python -c "import eq1core; print('EQ1 Core 설치 성공!')"
```

## 🚀 빠른 시작

### 환경 설정

```python
import os

# 데이터베이스 및 로그 경로 설정
os.environ["DB_URL"] = "mysql+pymysql://crefle:passwd@localhost:3307/eq1"
os.environ["LOG_PATH"] = "./public/logs"
```

### 기본 사용법

```python
from eq1core.core import Core
from eq1core.logger import AppLogger
from eq1core.signal import CustomEvent, InspectionEvents
from eq1core.engines.sample import SampleEngine
from eq1core.infrastructure.factory import DataServiceFactory
from eq1core.data import InspectionMode, InspectionPartResultData

# Core 인스턴스 생성
core = Core(
    uuid="unique_id", 
    group_name="inspection_group", 
    data_service=DataServiceFactory.get_service('db'), 
    mode=InspectionMode.MULTI_SHOT
)

# 검사 엔진 등록
core.register_engine(SampleEngine)

# 검사 시작
core.start()
```

## 📋 주요 기능

- **카메라 제어**: 다양한 카메라 제조사의 SDK 지원
- **통신 시스템**: TCP/UDP, 시리얼 통신 프로토콜
- **I/O 처리**: EZI I/O 보드 제어 및 신호 처리
- **딥러닝 추론**: ONNX, PyTorch 모델 지원
- **이벤트 시스템**: 비동기 이벤트 처리 및 관리
- **데이터 관리**: 검사 결과 및 로그 관리

## 🔧 개발 환경 설정

### 필수 요구사항

- Python 3.12 이상
- UV Package Manager (권장)

### 로컬 개발 설치

```bash
# 저장소 클론
git clone https://github.com/crefle/eq1-core.git
cd eq1-core

# UV를 사용한 개발 환경 설정
uv sync --dev

# 개발 모드로 패키지 설치
uv pip install -e .
```

### 의존성 관리

```bash
# 새로운 의존성 추가
uv add package-name

# 개발 의존성 추가
uv add --dev package-name

# 의존성 제거
uv remove package-name
```

## 🏗️ 프로젝트 구조

```
src/eq1core/
├── __init__.py          # 패키지 초기화
├── core.py              # 핵심 시스템 클래스
├── signal.py            # 시그널 시스템
├── data.py              # 데이터 모델
├── dto.py               # 데이터 전송 객체
├── utils.py             # 유틸리티 함수
├── logger.py            # 로깅 시스템
├── configure.py         # 설정 관리
├── lib/                 # 하위 라이브러리
│   ├── camera/          # 카메라 제어
│   ├── communication/   # 통신 시스템
│   ├── ezi_io/          # I/O 처리
│   └── disk/            # 디스크 유틸리티
├── domain/              # 도메인 로직
│   ├── entities/        # 엔티티
│   ├── ports/           # 포트 인터페이스
│   └── services/        # 도메인 서비스
├── infrastructure/      # 인프라스트럭처
│   ├── db/              # 데이터베이스
│   └── api/             # API 서비스
├── engines/             # 검사 엔진
├── predictors/          # 예측 모델
├── inspection/          # 검사 워커
├── dl/                  # 딥러닝 모델
└── mock/                # 목업 객체
```

## 📚 사용법

### 이벤트 시스템 사용법

```python
from eq1core.signal import CustomEvent, InspectionEvents

# 커스텀 이벤트 정의
class MyCustomEvent(CustomEvent):
    def __init__(self):
        super().__init__(
            name="my_custom_event",
            description="사용자 정의 이벤트",
            hook=lambda: print("이벤트 훅 실행")
        )

# 이벤트 훅 등록
def on_inspection_finished(*args, **kwargs):
    data = args[0] if args else kwargs.get("inspection_part_result_data")
    print(f"검사 완료: 카메라 {data.camera_number}, 결과 {data.result}")

core.register_hook(
    event_name=InspectionEvents.InspectionPartFinished().name,
    hook=on_inspection_finished
)

# 이벤트 발생
core.emit(InspectionEvents.NewGroup().name, "PRODUCT-SERIAL-001")
```

### CLI 명령어 사용법

```python
from eq1core.decorators import cli_command

@cli_command("trigger")
def trigger_inspection(core: Core) -> bool:
    """검사 트리거 명령어"""
    # 카메라 트리거 로직
    return True

@cli_command("next")
def next_product(core) -> bool:
    """다음 제품 처리 명령어"""
    serial = f"PRODUCT-{int(time.time())}"
    core.emit("next_signal", serial)
    return True
```

### 카메라 제어

```python
from eq1core.lib.camera.frame_grabber.worker import ImageGrabber

# 카메라 워커에서 소프트웨어 트리거 실행
camera_serial = "DUMMY-CAM-SERIAL"
for worker in core._workers:
    if isinstance(worker, ImageGrabber):
        if worker.camera_serial == camera_serial:
            worker.execute_stream_software_trigger()
            break
```

### 로깅 시스템

```python
from eq1core.logger import AppLogger

# 정보 로그
AppLogger.write_info(self, "검사 시스템 시작", print_to_terminal=True)

# 디버그 로그
AppLogger.write_debug(self, f"카메라 {camera_number} 프레임 {frame_number}", print_to_terminal=True)

# 에러 로그
AppLogger.write_error(self, f"오류 발생: {error_message}", print_to_terminal=True)
```

### Signal 시스템 사용법

EQ1 Core는 PySide6와 완전히 호환되는 Signal/Slot 시스템을 제공합니다.

#### 1. 기본 Signal 사용법

```python
from eq1core.signal import Signal

# 타입이 지정된 Signal 생성
data_signal = Signal(str)
status_signal = Signal(str, int)
complex_signal = Signal(dict, list)

# 핸들러 연결
def on_data_received(data):
    print(f"Data received: {data}")

def on_status_changed(status, code):
    print(f"Status: {status}, Code: {code}")

def on_complex_event(data_dict, data_list):
    print(f"Complex event: {data_dict}, {data_list}")

data_signal.connect(on_data_received)
status_signal.connect(on_status_changed)
complex_signal.connect(on_complex_event)

# Signal 발생
data_signal.emit("Hello World")
status_signal.emit("Processing", 200)
complex_signal.emit({"key": "value"}, [1, 2, 3])
```

#### 2. Custom Signal 사용법 (Core 통합)

```python
from eq1core.core import Core

# Custom signal 생성 (PySide6 스타일 - 데이터 타입만 지정)
core.create_custom_signal("my_signal", str)
core.create_custom_signal("status_update", str, str)
core.create_custom_signal("data_update", dict)

# 핸들러 연결
def on_custom_event(data):
    print(f"Custom event received: {data}")

def on_status_update(status, timestamp):
    print(f"Status update: {status} at {timestamp}")

def on_data_update(data):
    print(f"Data update: {data}")

core.my_signal.connect(on_custom_event)
core.status_update.connect(on_status_update)
core.data_update.connect(on_data_update)

# ✅ core.my_signal.emit 형태로 사용
core.my_signal.emit("Hello from custom signal!")
core.status_update.emit("Processing", "2024-01-01 12:00:00")
core.data_update.emit({"message": "Complex data", "count": 42})

# 동적 signal 생성 및 사용
core.create_custom_signal("new_signal", str)
core.new_signal.connect(lambda x: print(f"New signal: {x}"))
core.new_signal.emit("Dynamic signal works!")

# Signal 존재 여부 확인
print(f"my_signal exists: {hasattr(core, 'my_signal')}")

# 모든 custom signal 조회
all_signals = core.get_all_custom_signals()
for name, signal in all_signals.items():
    print(f"{name}: {signal}")
```

### 타입 검증 기능

Signal은 PySide6와 유사하게 타입 검증을 제공합니다:

```python
# 타입 검증 활성화 (기본값)
signal = Signal(str, int)
signal.emit("hello", 42)  # ✅ 정상
signal.emit("hello", "world")  # ⚠️ 경고: int 대신 str 전달

# 타입 검증 비활성화 (성능 최적화)
signal.disable_type_checking()
signal.emit("hello", "world")  # ✅ 경고 없음

# 타입 검증 다시 활성화
signal.enable_type_checking()
```

### SignalEmitter 사용법

SignalEmitter를 사용하여 동적으로 Signal을 관리할 수 있습니다:

```python
from eq1core.signal import SignalEmitter, create_signal, connect_signal, emit_signal

# SignalEmitter 인스턴스 생성
emitter = SignalEmitter()

# 타입이 지정된 Signal 생성
user_signal = emitter.create_signal("user_signal", str)
status_signal = emitter.create_signal("status_signal", str, int)

# 핸들러 연결
user_signal.connect(lambda data: print(f"User: {data}"))
status_signal.connect(lambda status, code: print(f"Status: {status} ({code})"))

# Signal 발생
emitter.emit("user_signal", "User logged in")
emitter.emit("status_signal", "processing", 200)

# 전역 편의 함수 사용
global_signal = create_signal("global_signal", str)
connect_signal("global_signal", lambda msg: print(f"Global: {msg}"))
emit_signal("global_signal", "Hello from global")
```

### 비동기 Signal 처리

Signal은 동기 및 비동기 슬롯을 모두 지원합니다:

```python
import asyncio
from eq1core.signal import Signal

# 비동기 슬롯을 가진 Signal 생성
async def async_handler(data):
    await asyncio.sleep(0.1)  # 비동기 작업 시뮬레이션
    print(f"Async processed: {data}")

def sync_handler(data):
    print(f"Sync processed: {data}")

# Signal 생성 및 슬롯 연결
signal = Signal(str)
signal.connect(sync_handler)           # 동기 슬롯
signal.connect(async_handler, is_async=True)  # 비동기 슬롯

# 동기 실행
signal.emit("Hello")

# 비동기 실행 (모든 슬롯 포함)
await signal.emit_async("Hello Async")
```

### 전역 Signal 관리

전역 함수들을 사용하여 애플리케이션 전체에서 Signal을 관리할 수 있습니다:

```python
from eq1core.signal import create_signal, connect_signal, emit_signal, emit_signal_async

# 전역 Signal 생성
create_signal("app_status", str)
create_signal("data_update", dict)

# 핸들러 연결
def on_status_change(status):
    print(f"App status: {status}")

def on_data_change(data):
    print(f"Data changed: {data}")

connect_signal("app_status", on_status_change)
connect_signal("data_update", on_data_change)

# Signal 발생
emit_signal("app_status", "Running")
emit_signal("data_update", {"key": "value"})

# 비동기 Signal 발생
await emit_signal_async("app_status", "Processing")
```

### Signal과 SignalEmitter의 차이점

**Signal 클래스**: 개별 Signal 인스턴스를 생성하고 관리
- 타입이 지정된 Signal 생성
- 슬롯 연결/해제
- 동기/비동기 emit 지원
- 타입 검증 기능

**SignalEmitter 클래스**: 여러 Signal을 그룹으로 관리
- 동적 Signal 생성 및 관리
- 이름 기반 Signal 접근
- 일괄 Signal 관리
- 전역 Signal 네임스페이스

### PySide6와의 완전한 호환성

EQ1 Core의 Signal/Slot 시스템은 PySide6와 완전히 동일한 API를 제공합니다:

```python
# PySide6 Signal
from PySide6.QtCore import Signal

class MyClass:
    data_changed = Signal(str)
    status_updated = Signal(str, int)

# EQ1 Core Signal (완전히 동일!)
from eq1core.signal import Signal

class MyClass:
    data_changed = Signal(str)
    status_updated = Signal(str, int)
```

**추가 기능**:
- 타입 검증 및 힌트 제공
- 비동기 Signal/Slot 지원
- 동적 Signal 생성 및 관리
- 성능 최적화를 위한 타입 검증 제어
- 전역 Signal 관리 시스템

### 완전한 애플리케이션 예제

```python
class InspectionApp:
    def __init__(self, uuid: str, group_name: str):
        self._core = Core(
            uuid=uuid, 
            group_name=group_name, 
            data_service=DataServiceFactory.get_service('db'), 
            mode=InspectionMode.MULTI_SHOT
        )
        
        # 이벤트 훅 등록
        self._core.register_hook(
            event_name=InspectionEvents.InspectionPartFinished().name,
            hook=self.on_finished_inspection_part
        )
        
        # 검사 엔진 등록
        self._core.register_engine(SampleEngine)
        
        # Custom Signal 생성 및 연결
        self._core.create_custom_signal("inspection_status", str)
        self._core.create_custom_signal("data_processed", dict)
        
        # Signal 핸들러 연결
        self._core.inspection_status.connect(self.on_inspection_status_change)
        self._core.data_processed.connect(self.on_data_processed)
    
    def on_finished_inspection_part(self, *args, **kwargs):
        data = args[0] if args else kwargs.get("inspection_part_result_data")
        if data:
            AppLogger.write_info(self, f"검사 완료: {data.part_name} - {data.result}")
            
            # Custom Signal 발생
            self._core.inspection_status.emit(f"검사 완료: {data.result}")
            self._core.data_processed.emit({
                "part_name": data.part_name,
                "result": data.result,
                "timestamp": data.timestamp
            })
    
    def on_inspection_status_change(self, status):
        print(f"검사 상태 변경: {status}")
    
    def on_data_processed(self, data):
        print(f"데이터 처리 완료: {data}")
    
    def run(self):
        AppLogger.write_info(self, "검사 시스템 시작...", print_to_terminal=True)
        self._core.start()

# 애플리케이션 실행
if __name__ == "__main__":
    app = InspectionApp(uuid="-", group_name="PRODUCT-SAMPLE")
    app.run()
```

### Signal 시스템 활용 예제

```python
from eq1core.signal import Signal, SignalEmitter

class DataProcessor:
    def __init__(self):
        # 개별 Signal 생성
        self.data_received = Signal(dict)
        self.processing_complete = Signal(dict, bool)
        
        # SignalEmitter를 사용한 동적 Signal 관리
        self.emitter = SignalEmitter()
        self.emitter.create_signal("status_update", str)
        self.emitter.create_signal("error_occurred", str, str)
    
    def process_data(self, data):
        # 상태 업데이트 Signal 발생
        self.emitter.emit("status_update", "Processing started")
        
        try:
            # 데이터 수신 Signal 발생
            self.data_received.emit(data)
            
            # 데이터 처리 로직...
            result = {"processed": True, "data": data}
            
            # 처리 완료 Signal 발생
            self.processing_complete.emit(result, True)
            self.emitter.emit("status_update", "Processing completed")
            
        except Exception as e:
            # 오류 발생 Signal 발생
            self.emitter.emit("error_occurred", "Processing failed", str(e))
            self.processing_complete.emit({}, False)

# 사용 예제
processor = DataProcessor()

# Signal 핸들러 연결
processor.data_received.connect(lambda data: print(f"데이터 수신: {data}"))
processor.processing_complete.connect(lambda result, success: print(f"처리 완료: {result}, 성공: {success}"))

# SignalEmitter Signal 핸들러 연결
processor.emitter.get_signal("status_update").connect(lambda status: print(f"상태: {status}"))
processor.emitter.get_signal("error_occurred").connect(lambda error, details: print(f"오류: {error} - {details}"))

# 데이터 처리 실행
processor.process_data({"id": 1, "value": "test"})
```

## 🧪 테스트

```bash
# 테스트 실행
uv run pytest

# 커버리지와 함께 테스트 실행
uv run pytest --cov=src/eq1core

# 특정 테스트 파일 실행
uv run pytest tests/test_core.py
```

## 📦 패키지 배포

### 로컬 빌드

```bash
# 패키지 빌드
uv run python -m build

# 빌드된 파일 확인
ls dist/
```

### PyPI 배포

```bash
# TestPyPI에 배포 (테스트용)
uv run python -m twine upload --repository testpypi dist/*

# PyPI에 배포 (실제 배포)
uv run python -m twine upload dist/*
```

## 🤝 기여 가이드라인

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 코드 스타일

- Black 포매터 사용
- Flake8 린터 준수
- Type hints 사용
- Docstring 작성

```bash
# 코드 포맷팅
uv run black src/eq1core/

# 린팅
uv run flake8 src/eq1core/

# 타입 체크
uv run mypy src/eq1core/
```

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 📞 지원

- 이슈 리포트: [GitHub Issues](https://github.com/crefle/eq1-core/issues)
- 문서: [GitHub Wiki](https://github.com/crefle/eq1-core/wiki)
- 이메일: dev@crefle.com

## 🔄 버전 히스토리

- **0.1.8**: 경로 구조 개선 및 의존성 문제 해결
  - src 경로 완전 제거 및 상대경로로 변경
  - numpy 의존성 제거로 의존성 충돌 해결
  - example 디렉토리 import 경로 수정
  - multishot mode 동작 확인 완료

- **0.1.7**: 의존성 최적화
  - numpy 의존성 제거
  - TestPyPI 호환성 개선

- **0.1.6**: numpy 버전 호환성 개선
  - numpy>=1.9.3으로 버전 요구사항 완화

- **0.1.5**: numpy 버전 업데이트
  - numpy>=1.26.0으로 현대적 버전 사용

- **0.1.4**: numpy 의존성 완화
  - numpy>=1.24.0으로 설정

- **0.1.3**: numpy 버전 조정
  - numpy>=1.21.0으로 설정

- **0.1.2**: numpy 의존성 제거
  - numpy 완전 제거로 의존성 충돌 해결

- **0.1.1**: 초기 TestPyPI 배포
  - numpy>=2.3.1 (의존성 충돌 발생)

- **0.1.0**: 초기 PyPI 배포 버전
  - 핵심 검사 시스템 기능
  - 카메라 제어 및 통신 시스템
  - 딥러닝 추론 엔진
  - 이벤트 시스템

