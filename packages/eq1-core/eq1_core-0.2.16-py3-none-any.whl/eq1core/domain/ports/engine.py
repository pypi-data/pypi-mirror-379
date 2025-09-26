from typing import List, Protocol
from abc import ABC, abstractmethod
from eq1core.domain.entities.engine import Engine
from eq1core.domain.ports.common import CommonPort


class EnginePort(CommonPort[Engine], Protocol):
    def get_all(self, only_activated: bool = False, hide_deleted: bool = True) -> List[Engine]:
        ...

    def get_by_component_id(self, component_id: int) -> List[Engine]:
        ...

    def get_by_name(self, name: str) -> Engine:
        ...