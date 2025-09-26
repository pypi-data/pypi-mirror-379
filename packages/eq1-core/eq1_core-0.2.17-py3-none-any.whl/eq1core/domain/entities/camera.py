from dataclasses import dataclass, field
from typing import List, Optional
from eq1core.domain.entities.component import Component


@dataclass
class Camera:
    id: int
    number: int  # 설비 내 카메라 위치 번호
    connection_index: Optional[int] = None  # HikVision에서 연결된 카메라 순서 번호
    camera_serial: Optional[str] = None  # 카메라 시리얼 번호
    grabber_serial: Optional[str] = None  # 프레임 그래버 시리얼 번호
    name: str = ''  # 카메라 이름
    stage: Optional[str] = None  # 카메라를 사용할 프로그램 이름
    config: Optional[str] = None  # 카메라 설정 (json)
    number_of_frames: int = 0  # 시퀀스에 속한 프레임 개수
    components: List[Component] = field(default_factory=list)  # 관련 컴포넌트 리스트
