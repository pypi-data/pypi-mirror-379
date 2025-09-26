from typing import List, Protocol
from abc import ABC, abstractmethod
from eq1core.domain.entities.component_result import ComponentResult
from eq1core.data import InspectionPartResultData
from eq1core.domain.ports.common import CommonPort


class ComponentResultPort(CommonPort[ComponentResult], Protocol):
    def get_finished_components_by_product_result_id(self, product_result_id: int) -> List[ComponentResult]:
        ...

    def count_finished_components_by_product_result_id(self, product_result_id: int) -> int:
        ...

    def count_finished_components_by_product_result_id_and_camera_number(self, product_result_id: int, camera_number: int) -> int:
        ...

    def get_finished_components_by_product_result_id_and_camera_number_and_frame_number(self,
                                                                                        product_result_id: int,
                                                                                        camera_number: int,
                                                                                        frame_number: int) -> List[ComponentResult]:
        ...

    def get_component_names_by_product_result_id(self, product_result_id: int) -> List[str]:
        ...

    def create_bulk(self, data: List[InspectionPartResultData]) -> List[ComponentResult]:
        ...
