import dataclasses
import datetime
from typing import List, Optional, Dict
# 지연 임포트로 변경하여 순환 참조 문제 해결
# from .infrastructure.db.models.camera import CameraModel


# @dataclasses.dataclass
# class CameraDTO:  # TODO : area 와 line 겸용으로 사용하기 위하여 일시적으로 초기값을 할당해놓았으나 추후 작업이 끝나면 다시 수정해야함.
#     name: str
#     number_of_frames: int = -1
#     number: int = -1
#     connection_index: int = -1
#     camera_serial: str = ""
#     grabber_serial: str = ""
#     stage: str = ""
#     config: dict = None  # json

#     @classmethod
#     def from_model(cls, model: CameraModel):
#         try:
#             config = json.loads(model.config)
#         except TypeError:
#             config = {}

#         return cls(
#             number=model.number,
#             connection_index=model.connection_index,
#             camera_serial=model.camera_serial,
#             grabber_serial=model.grabber_serial,
#             stage=model.stage,
#             name=model.name,
#             number_of_frames=model.number_of_frames,
#             config=config
#         )


@dataclasses.dataclass
class PredictorDTO:
    name: str
    settings: Optional[dict] = None


@dataclasses.dataclass
class CameraDTO:
    name: str
    number: int
    serial: str
    fg_serial: str = None
    number_of_frames: int = 0
    settings: Optional[dict] = None


@dataclasses.dataclass
class InspectionGroupDTO:
    name: str


@dataclasses.dataclass
class InspectionPartDTO:
    name: str
    group: InspectionGroupDTO
    engine_name: str
    camera_number: int
    frame_number: int
    uuid: str
    roi_xywh: List[int]


@dataclasses.dataclass
class VisionEngineDTO:
    name: str
    code: str
    predictor: Optional[PredictorDTO] = None
    settings: Optional[dict] = None
    

@dataclasses.dataclass
class InspectionGroupResultDTO:
    name: str
    serial: str
    result: str = None
    started_at: datetime.datetime = None
    finished_at: datetime.datetime = None
    elapsed_time_ms: int = None
    is_locked: bool = False


@dataclasses.dataclass
class InspectionPartResultDTO:
    id: int
    group_result_id: int
    part_name: str
    camera_number: int
    frame_number: int
    roi: Optional[str]
    started_at: datetime
    finished_at: Optional[datetime.datetime]
    result: Optional[str]
    elapsed_time_ms: Optional[int]
    detail: Optional[str]
    origin_image_path: Optional[str]
    result_image_path: Optional[str]


@dataclasses.dataclass
class SystemSettingDTO:
    """시스템 설정 데이터 전송 객체"""
    version: str
    save_origin: bool
    save_only_ng: bool


@dataclasses.dataclass
class NetworkSectionDTO:
    """네트워크 섹션 설정 데이터 전송 객체"""
    method: Optional[str] = None
    protocol: Optional[str] = None
    address: Optional[str] = None
    port: Optional[int] = None
    timeout: Optional[float] = None
    mode: Optional[str] = None


@dataclasses.dataclass
class NetworkSettingDTO:
    """네트워크 설정 데이터 전송 객체"""
    sections: Dict[str, NetworkSectionDTO]


@dataclasses.dataclass
class PathConfigDTO:
    """경로 설정 데이터 전송 객체"""
    root: Optional[str] = None
    period: Optional[str] = None
    interval: Optional[str] = None


@dataclasses.dataclass
class DiskConfigDTO:
    """디스크 관리 설정 데이터 전송 객체"""
    audit_log_keep_days: Optional[int] = None
    keep_days: Optional[int] = None
    limit: Optional[int] = None
    auto_clean: Optional[bool] = None


@dataclasses.dataclass
class StorageConfigDTO:
    """스토리지 설정 데이터 전송 객체"""
    origin: Optional[PathConfigDTO] = None
    result: Optional[PathConfigDTO] = None
    disk: Optional[DiskConfigDTO] = None
