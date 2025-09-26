from typing import Dict, Any, Type
from eq1core.dto import VisionEngineDTO
from eq1core.engines.interface import BaseEngine


class EngineFactory:
    def __init__(self):
        self._engine_classes: Dict[str, Type[BaseEngine]] = {}

    def register_engine(self, engine_class: Type[BaseEngine]) -> None:
        self._engine_classes[engine_class.name.lower()] = engine_class

    def create_engine(self, data: VisionEngineDTO) -> BaseEngine:
        engine_name = data.name.lower()
        if engine_name in self._engine_classes:
            engine_class = self._engine_classes[engine_name]
            return engine_class.create_from_config(data.settings)
        else:
            raise ValueError(f'\n{data.name}엔진의 base로 설정된 {engine_name}는 지원되지 않는 엔진 이름입니다.'
                             f'\n지원되는 엔진 목록을 참고해주세요. {list(self._engine_classes.keys())}')

    def get_registered_engines(self) -> list[str]:
        """등록된 엔진 목록을 반환합니다."""
        return list(self._engine_classes.keys())
