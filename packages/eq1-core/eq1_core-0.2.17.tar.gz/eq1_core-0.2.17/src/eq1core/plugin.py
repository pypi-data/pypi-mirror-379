
from .logger import AppLogger


class EqPlugin:
    def __init__(self):
        self._core = None

    @property
    def core(self):
        """Core 인스턴스에 안전하게 접근하기 위한 property"""
        return self._core

    def register(self, core):
        self._core = core
        AppLogger.write_info(self, f"플러그인 '{self.__class__.__name__}'이(가) Core에 등록되었습니다.")

    def unregister(self):
        """옵션: 종료 시 정리할 작업"""
        if self._core is not None:
            AppLogger.write_info(self, f"플러그인 '{self.__class__.__name__}'이(가) Core에서 해제되었습니다.")
            self._core = None

    def emit(self, name: str, *args, **kwargs):
        if self.core is None:
            raise ValueError("Core is not registered")
        if not hasattr(self.core, 'emit'):
            raise ValueError("Core does not have emit method")
        
        self.core.emit(name, *args, **kwargs)
