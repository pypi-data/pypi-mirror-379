from typing import List, Optional, Protocol
from abc import ABC, abstractmethod
from eq1core.domain.entities.camera import Camera
from eq1core.domain.ports.common import CommonPort


class CameraPort(CommonPort[Camera], Protocol):
    def get_by_number(self, number: int,
                      hide_deleted: bool = True) -> Optional[Camera]: ...

    def get_all_by_stage(
        self, stage: str, hide_deleted: bool = True) -> List[Camera]: ...
