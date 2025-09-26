from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from eq1core.infrastructure.db import Base
from .common import CommonModel


class ComponentModel(CommonModel, Base):
    __tablename__ = 'components'

    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False, comment='제품 ID')
    camera_id = Column(Integer, ForeignKey('cameras.id', ondelete='RESTRICT'), nullable=True, comment='카메라 ID')
    engine_id = Column(Integer, ForeignKey('engines.id', ondelete='RESTRICT'), nullable=True, comment='비전 엔진 ID')

    name = Column(String(50), nullable=False, comment='검사 항목 이름')
    frame_number = Column(Integer, nullable=False, comment='카메라 시퀀스 내 프레임 번호')
    position_index = Column(Integer, nullable=False, comment='결과맵 NG BOX 좌표 매핑 번호', default=0)
    roi = Column(String(50), nullable=True, comment='프레임 내 검사 영역 좌표 (x y w h)')
    is_activated = Column(Integer, nullable=False, default=1, comment='검사 활성/비활성 플래그 (0: 비활성, 1: 활성)')

    product = relationship('ProductModel', back_populates='components')
    camera = relationship('CameraModel', back_populates='components')
    engine = relationship('EngineModel', back_populates='components')
    __table_args__ = (
        UniqueConstraint('product_id', 'name', name='uq_product_component_name', comment='동일 제품 내 검사 항목명 중복 불가'),
    )

