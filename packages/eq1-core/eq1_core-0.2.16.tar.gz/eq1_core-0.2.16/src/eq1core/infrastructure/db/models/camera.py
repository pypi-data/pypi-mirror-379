from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from eq1core.infrastructure.db import Base
from eq1core.infrastructure.db.models.common import CommonModel


class CameraModel(CommonModel, Base):
    __tablename__ = 'cameras'

    number = Column(Integer, nullable=False, unique=True, comment='설비 내 카메라 위치 번호')
    connection_index = Column(Integer, nullable=True, unique=True, comment='HikVision에서 연결된 카메라 순서 번호; 없으면 number 사용; serial 로 연결 되도록 기능 변경 완료 되면 삭제 예정;')
    camera_serial = Column(String(20), nullable=True, unique=True, comment='카메라 시리얼 번호')
    grabber_serial = Column(String(20), nullable=True, unique=True, comment='프레임 그래버 시리얼 번호')
    name = Column(String(50), nullable=False, comment='카메라 이름')
    stage = Column(String(20), nullable=True, comment='카메라를 사용할 프로그램 이름')
    config = Column(Text, nullable=True, comment='카메라 설정 (json)')
    number_of_frames = Column(Integer, nullable=False, comment='시퀀스에 속한 프레임 개수')

    components = relationship('ComponentModel', back_populates='camera')
