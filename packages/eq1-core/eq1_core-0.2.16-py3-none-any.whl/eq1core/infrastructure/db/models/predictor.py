import enum
from sqlalchemy import Column, Integer, String, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship
from eq1core.infrastructure.db import Base
from eq1core.infrastructure.db.models.common import CommonModel


class DLCategory(enum.Enum):
    ANOMALY = 'ANOMALY'
    CLASSIFICATION = 'CLASSIFICATION'
    DETECTION = 'DETECTION'
    SEGMENTATION = 'SEGMENTATION'


class PredictorType(enum.Enum):
    CV = 'CV'
    DL = 'DL'


class PredictorModel(CommonModel, Base):
    __tablename__ = 'predictors'

    # engine_id = Column(Integer, ForeignKey('engines.id'), nullable=False, comment='비전 엔진 ID')

    name = Column(String(50), nullable=False, unique=True, comment='예측 모듈 이름')
    type = Column(Enum(PredictorType), nullable=False, default=PredictorType.CV, comment='예측 모듈 타입 (CV: 컴퓨터 비전, DL: 딥러닝)')
    category = Column(Enum(DLCategory), nullable=True, comment='딥러닝 카테고리')
    config = Column(Text, nullable=True, comment='예측 모듈 세부 설정 (json)')
    version = Column(String(50), nullable=True, comment='버전')

    # engine = relationship('EngineModel', back_populates='predictors')
 