from typing import List, Optional, Protocol
from abc import ABC, abstractmethod
from eq1core.domain.entities.vision_presets import VisionPreset
from eq1core.domain.ports.common import CommonPort


class VisionPresetPort(CommonPort[VisionPreset], Protocol):
    def get_all(self) -> List[VisionPreset]:
        ...

    def get_by_id(self, preset_id: int) -> Optional[VisionPreset]:
        ...

    def create(self, data: dict) -> VisionPreset:
        ...

    def update(self, preset_id: int, data: dict) -> Optional[VisionPreset]:
        ...

    def delete(self, preset_id: int) -> bool:
        ...
