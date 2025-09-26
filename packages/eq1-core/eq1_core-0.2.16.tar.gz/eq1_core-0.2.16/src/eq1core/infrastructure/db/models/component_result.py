from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from eq1core.infrastructure.db import Base
from .common import CommonModel


class ComponentResultModel(CommonModel, Base):
    __tablename__ = 'component_results'

    product_result_id = Column(Integer, ForeignKey('product_results.id'), nullable=False, comment='제품 결과 ID')

    component_name = Column(String(50), nullable=False, comment='검사 항목 이름')
    camera_number = Column(Integer, nullable=False, comment='카메라 번호')
    frame_number = Column(Integer, nullable=False, comment='프레임 번호')
    roi = Column(String(50), nullable=True, comment='프레임 내 검사 영역 좌표 (x y w h)')
    started_at = Column(DateTime, nullable=False, comment='검사 시작 시간')
    finished_at = Column(DateTime, nullable=True, comment='검사 완료 시간')
    result = Column(String(20), nullable=True, comment='검사 결과')
    elapsed_time_ms = Column(Integer, nullable=True, comment='검사 소요 시간 (초)')
    detail = Column(Text, nullable=True, comment='검사 결과 상세 정보 (json)')
    origin_image_path = Column(Text, nullable=True, comment='원본 이미지 경로')
    result_image_path = Column(Text, nullable=True, comment='결과 이미지 경로')

    product_result = relationship('ProductResultModel', back_populates='component_results')

