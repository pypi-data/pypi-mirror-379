import enum
import json
import datetime
import numpy as np
from typing import Any, List, Union, Tuple
from dataclasses import dataclass, field


@dataclass(frozen=True)
class FrameInfo:
    camera_number: int
    number_of_frames: int


@dataclass(frozen=True)
class InspectionRequestData:
    group_name: str
    group_serial: Union[int, str] = None
    skip_positions: List[int] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'InspectionRequestData':
        return cls(
            group_name=data.get('group_name'),
            group_serial=data.get('group_serial'),
            skip_positions=data.get('skip_positions')
        )

    def create_sample(self):
        # create data to take sample image
        pass


@dataclass(frozen=True)
class PatchData:
    roi: Tuple[int, int, int, int]
    image: np.ndarray


@dataclass(frozen=True)
class PatchResult:
    is_ok: bool = False
    roi: Tuple[int, int, int, int] = None  # (x, y, w, h)
    image: np.ndarray = None
    bboxes: List[Tuple[int, int, int, int]] = field(
        default_factory=list)  # (x, y, w, h)
    scores: List[float] = field(
        default_factory=list)  # 각 bbox의 max 스코어 정보
    

@dataclass
class RollSurfaceEngineParams:
    ng_threshold: float = 0.5  # 결과 값이 설정 값 이상인 경우 NG 로 판정
    cd_start_offset_mm: float = 0  # 실제 원단 너비 방향 시작 위치 보정 값; patch 내 bbox 위치 보정을 위한 값;
    left_border_line: int = 0  # 왼쪽 경계선; 패치 생성 시 제외; unit = pixel;
    right_border_line: int = -1  # 오른쪽 경계선; 패치 생성 시 제외; unit = pixel;
    defect_ignore_ranges: List[Tuple[int, int]] = field(
        default_factory=lambda: [(),])  # 검사 후 불량 무시 영역; [(start_x, end_x),]
    force_ok_box_size: int = 0  # 가로 x 세로 크기가 force_ok_box_size 이하인 bbox 는 무조건 OK 로 판정
    # 박스 내 pixel 값이 모두 force_ok_box_color 이상인 bbox 는 무조건 OK 로 판정
    force_ok_box_color: int = 255
    patch_size: int = 500  # 패치 크기; 정사각형; pixel 단위;
    # 패치 생성시 이미지 overlay 크기; unit = pixel;
    patch_overlay: Tuple[int, int] = (0, 0)
    # 이미지가 패치 사이즈로 정확히 나누어 떨어지지 않을 경우 나머지 부분을 버릴지, 마지막 패치를 조금 겹쳐서라도 하나 더 생성할 지 결정
    drop_remainder: bool = False
    predictor_name: str = 'surface_ad_predictor'  # dl predictor 이름


@dataclass
class RollSurfaceEngineResult:
    """
    * 현재 bboxes 는 패치 이미지를 기준으로 계산되었습니다.
    * 실제 이미지에 표시할 때는 left_border_line 을 더해주어야 합니다.
    * left_border_line, right_border_line 은 원단보다 조금 안쪽에 그려집니다.
    * 이로 인해 발생하는 폭 오차는 일단 무시하기로 결정했습니다...
    """

    is_ok: bool = False
    is_failed: bool = False
    base_engine_name: str = 'noname'
    engine_params: RollSurfaceEngineParams = None
    image: np.ndarray = None
    patch_results: List[PatchResult] = field(default_factory=list)
    bboxes_with_pixel_unit: List[Tuple[int, int, int, int]] = field(
        default_factory=list)
    bboxes_with_mm_unit: List[Tuple[float, float, float,
                                    float]] = field(default_factory=list)
    bbox_scores: List[float] = field(default_factory=list)

    def to_dict(self):
        return {
            "is_ok": self.is_ok,
            "is_failed": self.is_failed,
            "base_engine_name": self.base_engine_name,
            "bboxes_with_mm_unit": self.bboxes_with_mm_unit
        }


@dataclass(frozen=True)
class ImageData:
    camera_number: int
    image: np.ndarray
    captured_at: datetime.datetime
    md_pixel_resolution_mm: float = None
    cd_pixel_resolution_mm: float = None


@dataclass(frozen=True)
class InspectionImageData:
    group_serial: str
    camera_number: int
    frame_number: int
    image: np.ndarray
    captured_at: datetime.datetime
    md_pixel_resolution_mm: float = None
    cd_pixel_resolution_mm: float = None

    def get_filename(self):
        return f'{self.captured_at.strftime("%Y-%m-%dT%H%M%S")}_cam{self.camera_number:02}_frame{self.frame_number:02}'


@dataclass(frozen=True)
class ComponentData:  # TODO : -> DTO
    component_id: int
    component_name: str
    camera_number: int
    frame_number: int
    roi: List[int]  # x, y, w, h


    # TODO : from db or api. 아래와 같은 직접 참조는 제거해야함.
    @classmethod
    def from_model(cls, model):
        # 지연 임포트로 변경하여 순환 참조 문제 해결
        # from .infrastructure.db.repositories import CameraRepo
        camera_number = CameraRepo.get_by_id(model.camera_id).number
        roi = [int(x) for x in model.roi.split(',')]
        return cls(
            component_id=model.id,
            component_name=model.name,
            camera_number=camera_number,
            frame_number=model.frame_number,
            roi=roi
        )


@dataclass
class ComponentResultData:
    product_result_id: int
    component_name: str
    camera_number: int
    frame_number: int
    roi: List[int]
    started_at: datetime.datetime
    finished_at: datetime.datetime
    result: str
    elapsed_time_ms: int
    detail: Any
    origin_image_path: str
    result_image_path: str


@dataclass
class InspectionPartResultData:
    group_name: str
    group_serial: str
    part_name: str
    engine_name: str
    camera_number: int
    frame_number: int
    roi_xywh: List[int]
    started_at: datetime.datetime
    finished_at: datetime.datetime
    captured_at: datetime.datetime
    result: str
    elapsed_time_ms: int
    detail: Any
    origin_image_path: str
    result_image_path: str


@dataclass
class InspectionGroupResultData:
    name: str
    serial: str
    result_code: str
    started_at: datetime.datetime
    finished_at: datetime.datetime
    elapsed_time_ms: int
    is_locked: int

    number_of_inspection_parts: int
    number_of_completed_parts: int = 0
    completed_parts: List[InspectionPartResultData] = field(default_factory=list)


class ProductResultCode(enum.Enum):
    OK = 'OK'
    NG = 'NG'
    FAIL = 'FAIL'
    PASS = 'PASS'
    SAMPLE = 'SAMPLE'
    DEMO = 'DEMO'
    REPAIRED = 'REPAIRED'

    def get_by_value(value: str) -> 'ProductResultCode':
        for code in ProductResultCode:
            if code.value == value:
                return code
        raise ValueError(f"Unknown ProductResultCode value: {value}")


@dataclass(frozen=True)
class EngineResult:
    is_ok: bool
    is_failed: bool = False
    base_engine_name: str = 'None'

    def to_dict(self):
        return {
            "is_ok": self.is_ok,
            "fail": self.is_failed,
            "base_engine_name": self.base_engine_name,
        }


@dataclass
class CameraPixelInfo:
    """카메라 픽셀 해상도 정보"""
    md_pixel_resolution_mm: float
    cd_pixel_resolution_mm: float
    frame_md_pixel_size: int
    
    @property
    def frame_md_mm_size(self) -> float:
        """프레임의 MD 방향 실제 크기 (mm)"""
        return self.frame_md_pixel_size * self.md_pixel_resolution_mm
    
    def calculate_frame_distance(self, frame_number: int) -> float:
        """특정 프레임까지의 누적 거리 계산 (mm)"""
        return self.frame_md_mm_size * (frame_number)
    
    def pixel_to_mm_md(self, pixel_value: float) -> float:
        """MD 방향 픽셀 값을 mm로 변환"""
        return pixel_value * self.md_pixel_resolution_mm
    
    def pixel_to_mm_cd(self, pixel_value: float) -> float:
        """CD 방향 픽셀 값을 mm로 변환"""
        return pixel_value * self.cd_pixel_resolution_mm
    
    def mm_to_pixel_md(self, mm_value: float) -> float:
        """MD 방향 mm 값을 픽셀로 변환"""
        return mm_value / self.md_pixel_resolution_mm
    
    def mm_to_pixel_cd(self, mm_value: float) -> float:
        """CD 방향 mm 값을 픽셀로 변환"""
        return mm_value / self.cd_pixel_resolution_mm
    

@dataclass
class LotInfo:  # TODO : Lot -> AutoGeneratedSerial
    date: datetime.datetime
    number: int

    def as_dict(self):
        return {
            "date": self.date,
            "number": self.number
        }
    
    @classmethod
    def new(self):
        return LotInfo(date=datetime.datetime.now(), number=1)

    @classmethod
    def from_serial(cls, serial: str):
        date_str, number_str = serial.split('@')
        date = datetime.datetime.strptime(date_str, '%Y%m%d')
        number = int(number_str)

        return cls(date, number)
    
    @classmethod
    def is_valid_serial_format(cls, serial: str) -> bool:
        try:
            cls.from_serial(serial)
            return True
        except Exception:
            return False

    def to_serial(self):
        return f"{self.date.strftime('%Y%m%d')}@{self.number:05d}"

    def is_today(self):
        return self.date.date() == datetime.datetime.now().date()

    def increment(self):
        self.number += 1

        return self

    def next(self):
        if self.is_today():
            return self.increment()
        else:
            self.date = datetime.datetime.now()
            self.number = 1
            return self


class InspectionMode(enum.Enum):
    SINGLE_SHOT = enum.auto()
    MULTI_SHOT = enum.auto()
    CONTINUOUS = enum.auto()
