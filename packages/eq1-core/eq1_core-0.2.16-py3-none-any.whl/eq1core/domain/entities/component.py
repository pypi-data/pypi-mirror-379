from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Component:
    id: int
    product_id: int  # 제품 ID
    camera_id: Optional[int] = None  # 카메라 ID
    engine_id: Optional[int] = None  # 비전 엔진 ID

    name: str = ''  # 검사 항목 이름
    frame_number: int = 0  # 카메라 시퀀스 내 프레임 번호
    position_index: int = 0  # 결과맵 NG BOX 좌표 매핑 번호
    roi: Optional[str] = None  # 프레임 내 검사 영역 좌표 (x y w h)
    is_activated: int = 1  # 검사 활성/비활성 플래그 (0: 비활성, 1: 활성)
