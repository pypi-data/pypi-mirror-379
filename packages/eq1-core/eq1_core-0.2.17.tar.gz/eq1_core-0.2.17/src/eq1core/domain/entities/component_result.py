from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class ComponentResult:
    id: int
    product_result_id: int
    component_name: str
    camera_number: int
    frame_number: int
    roi: Optional[str]
    started_at: datetime
    finished_at: Optional[datetime]
    result: Optional[str]
    elapsed_time_ms: Optional[int]
    detail: Optional[str]
    origin_image_path: Optional[str]
    result_image_path: Optional[str]
