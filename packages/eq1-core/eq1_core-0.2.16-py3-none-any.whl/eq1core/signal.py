import asyncio
import threading
from typing import Dict, Optional, Callable, List


class Signal:
    """PySide6 Signal과 유사한 이벤트 시그널 클래스"""
    
    def __init__(self, *types):
        """
        Signal 생성 (PySide6 스타일)
        
        Args:
            *types: 데이터 타입들
        """
        self.types = types
        self._slots: List[Callable] = []
        self._async_slots: List[Callable] = []
        self._lock = threading.RLock()
        self._enabled = True
        self._type_checking = True  # 타입 검증 활성화 여부
    
    def _validate_types(self, *args) -> bool:
        """타입 검증 수행"""
        if not self._type_checking or not self.types:
            return True
        
        # 위치 인자 타입 검증
        if len(args) != len(self.types):
            print(f"Warning: Signal expects {len(self.types)} arguments, got {len(args)}")
            return False
        
        for i, (arg, expected_type) in enumerate(zip(args, self.types)):
            if not isinstance(arg, expected_type):
                print(f"Warning: Signal argument {i} expects {expected_type.__name__}, got {type(arg).__name__}")
                return False
        
        return True
    
    def connect(self, slot: Callable, is_async: bool = False):
        """시그널에 슬롯 연결"""
        # 타입 힌트 제공
        if self.types and self._type_checking:
            expected_params = [f"arg{i}: {t.__name__}" for i, t in enumerate(self.types)]
            hint = f"Expected signature: ({', '.join(expected_params)})"
            print(f"Signal {hint}")
        
        with self._lock:
            if is_async:
                self._async_slots.append(slot)
            else:
                self._slots.append(slot)
    
    def disconnect(self, slot: Callable):
        """시그널에서 슬롯 연결 해제"""
        with self._lock:
            if slot in self._slots:
                self._slots.remove(slot)
            if slot in self._async_slots:
                self._async_slots.remove(slot)
    
    def disconnect_all(self):
        """모든 슬롯 연결 해제"""
        with self._lock:
            self._slots.clear()
            self._async_slots.clear()
    
    def enable_type_checking(self):
        """타입 검증 활성화"""
        self._type_checking = True
    
    def disable_type_checking(self):
        """타입 검증 비활성화"""
        self._type_checking = False
    
    def __str__(self) -> str:
        """Signal 정보 문자열 표현"""
        type_info = f"[{', '.join(t.__name__ for t in self.types)}]" if self.types else "[any]"
        return f"Signal{type_info}(slots={self.slot_count})"
    
    def __repr__(self) -> str:
        """Signal 정보 문자열 표현 (디버깅용)"""
        return self.__str__()
    
    def emit(self, *args, **kwargs):
        """시그널 발생 (동기 슬롯만)"""
        if not self._enabled:
            return
        
        # 타입 검증 수행
        if not self._validate_types(*args, **kwargs):
            return
        
        with self._lock:
            slots = self._slots.copy()
        
        for slot in slots:
            try:
                slot(*args, **kwargs)
            except Exception as e:
                # 로깅 추가 필요
                print(f"Error in signal slot {slot.__name__}: {e}")
    
    async def emit_async(self, *args, **kwargs):
        """시그널 발생 (비동기 슬롯 포함)"""
        if not self._enabled:
            return
        
        # 타입 검증 수행
        if not self._validate_types(*args, **kwargs):
            return
        
        with self._lock:
            slots = self._slots.copy()
            async_slots = self._async_slots.copy()
        
        # 동기 슬롯 실행
        for slot in slots:
            try:
                slot(*args, **kwargs)
            except Exception as e:
                print(f"Error in signal slot {slot.__name__}: {e}")
        
        # 비동기 슬롯 실행
        if async_slots:
            tasks = []
            for slot in async_slots:
                try:
                    if asyncio.iscoroutinefunction(slot):
                        task = asyncio.create_task(slot(*args, **kwargs))
                        tasks.append(task)
                    else:
                        # 동기 함수를 비동기로 실행
                        loop = asyncio.get_event_loop()
                        task = loop.run_in_executor(None, slot, *args, **kwargs)
                        tasks.append(task)
                except Exception as e:
                    print(f"Error in async signal slot {slot.__name__}: {e}")
            
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)
    
    def enable(self):
        """시그널 활성화"""
        self._enabled = True
    
    def disable(self):
        """시그널 비활성화"""
        self._enabled = False
    
    @property
    def slot_count(self) -> int:
        """연결된 슬롯 개수"""
        with self._lock:
            return len(self._slots) + len(self._async_slots)


class SignalEmitter:
    """시그널 발생 및 관리 클래스"""
    
    def __init__(self):
        self._signals: Dict[str, Signal] = {}
        self._lock = threading.RLock()
    
    def create_signal(self, name: str, *types) -> Signal:
        """새로운 시그널 생성"""
        with self._lock:
            if name in self._signals:
                raise ValueError(f"Signal '{name}' already exists")
            
            signal = Signal(*types)
            self._signals[name] = signal
            return signal
    
    def get_signal(self, name: str) -> Optional[Signal]:
        """시그널 조회"""
        return self._signals.get(name)
    
    def remove_signal(self, name: str):
        """시그널 제거"""
        with self._lock:
            if name in self._signals:
                signal = self._signals[name]
                signal.disconnect_all()
                del self._signals[name]
    
    def emit(self, signal_name: str, *args, **kwargs):
        """시그널 발생"""
        signal = self.get_signal(signal_name)
        if signal:
            signal.emit(*args, **kwargs)
    
    async def emit_async(self, signal_name: str, *args, **kwargs):
        """비동기 시그널 발생"""
        signal = self.get_signal(signal_name)
        if signal:
            await signal.emit_async(*args, **kwargs)
    
    def get_all_signals(self) -> Dict[str, Signal]:
        """모든 시그널 조회"""
        return self._signals.copy()
    
    def clear_all_signals(self):
        """모든 시그널 제거"""
        with self._lock:
            for signal in self._signals.values():
                signal.disconnect_all()
            self._signals.clear()


# 전역 시그널 에미터 인스턴스
global_signal_emitter = SignalEmitter()

# 편의 함수들
def create_signal(signal_name: str, *types) -> Signal:
    """전역 시그널 생성"""
    return global_signal_emitter.create_signal(signal_name, *types)

def connect_signal(signal_name: str, slot: Callable, is_async: bool = False):
    """전역 시그널에 슬롯 연결"""
    signal = global_signal_emitter.get_signal(signal_name)
    if signal:
        signal.connect(slot, is_async)
    else:
        # 시그널이 없으면 생성 (타입 정보 없이)
        signal = global_signal_emitter.create_signal(signal_name)
        signal.connect(slot, is_async)

def disconnect_signal(signal_name: str, slot: Callable):
    """전역 시그널에서 슬롯 연결 해제"""
    signal = global_signal_emitter.get_signal(signal_name)
    if signal:
        signal.disconnect(slot)

def emit_signal(signal_name: str, *args, **kwargs):
    """전역 시그널 발생"""
    global_signal_emitter.emit(signal_name, *args, **kwargs)

async def emit_signal_async(signal_name: str, *args, **kwargs):
    """전역 비동기 시그널 발생"""
    await global_signal_emitter.emit_async(signal_name, *args, **kwargs)


