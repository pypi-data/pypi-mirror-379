from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

from eq1core.data import ProductResultCode, InspectionPartResultData
from eq1core.dto import InspectionPartDTO, InspectionGroupDTO, VisionEngineDTO, CameraDTO, InspectionGroupResultDTO, InspectionPartResultDTO


class CoreDataService(ABC):
    @abstractmethod
    def is_group_result_empty(self, name: str) -> bool:
        pass
 
    @abstractmethod
    def get_active_cameras(self, uuid: str) -> List[CameraDTO]:
        pass

    @abstractmethod
    def get_last_group_serial(self, group_name: str) -> Optional[str]:
        pass

    @abstractmethod
    def get_last_group_result_by_name(self, name: str) -> Optional[InspectionGroupResultDTO]:
        pass

    @abstractmethod
    def get_group_result_by_serial(self, serial: str) -> Optional[InspectionGroupResultDTO]:
        pass

    @abstractmethod
    def get_active_engines(self, uuid: str) -> List[VisionEngineDTO]:
        """
        프로그램에서 활성화시킬 엔진 목록을 조회하는 메서드.
        """
        pass

    @abstractmethod
    def get_active_inspection_parts(self, uuid: str) -> List[InspectionPartDTO]:
        pass

    @abstractmethod
    def get_active_inspection_parts_by_engine_name(self, name: str) -> List[InspectionPartDTO]:
        pass

    @abstractmethod
    def set_unlocked_group_results_as_failed(self, group_name: str, serial: str) -> bool:
        pass
    
    @abstractmethod
    def set_group_result_as_finished(self,
                                       serial: str,
                                       result_code: ProductResultCode,
                                       finished_at: datetime,
                                       is_locked: bool = True,
                                       elapsed_time_ms: int = 0
                                       ) -> InspectionGroupResultDTO:
        pass

    @abstractmethod
    def create_new_group_result(self, name: str, serial: str, started_at: datetime = datetime.now(), elapsed_time_ms: int = 0) -> InspectionGroupResultDTO:
        pass

    @abstractmethod
    def save_inspection_part_results(self, results: List[InspectionPartResultData]) -> List[InspectionPartResultDTO]:
        pass
