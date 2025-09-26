from typing import Protocol, Optional, List
from abc import ABC, abstractmethod
from eq1core.domain.entities.component import Component
from eq1core.domain.ports.common import CommonPort


class ComponentPort(CommonPort[Component], Protocol):

    def get_components_by_product_id(self, product_id: int) -> List[Component]:
        ...

    def get_components_by_product_id_and_camera_id_and_frame_number(self, product_id: int,
                                                                    camera_id: int,
                                                                    frame_number: int,
                                                                    only_activated: bool = True) -> List[Component]:
        ...

    def get_components_by_engine_id(self, engine_id: int) -> List[Component]:
        ...

    def get_components_by_camera_id(self, camera_id: int) -> List[Component]:
        ...

    def get_frameless_components_by_product_id_and_camera_id(self, product_id: int, camera_id: int) -> List[Component]:
        ...

    def get_components_by_camera_id_and_frame_number(self, camera_id: int, frame_number: int) -> List[Component]:
        ...