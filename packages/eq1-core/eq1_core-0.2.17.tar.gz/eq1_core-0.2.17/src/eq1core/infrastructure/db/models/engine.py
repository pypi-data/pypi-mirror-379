from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from eq1core.infrastructure.db import Base
from eq1core.infrastructure.db.models.common import CommonModel


class EngineModel(CommonModel, Base):
    __tablename__ = 'engines'

    name = Column(String(50), nullable=False, unique=True, comment='비전 엔진 이름')
    base_engine = Column(String(50), nullable=False, unique=False, comment='실제 구현부 엔진 이름')
    alias = Column(String(50), nullable=True, unique=True, comment='비전 엔진 별칭')
    config = Column(Text, nullable=True, comment='비전 엔진 설정 (json)')
    is_activated = Column(Integer, nullable=False, default=1, comment='비전 엔진 활성 여부 (0: 비활성, 1: 활성)')

    components = relationship('ComponentModel', back_populates='engine')
    # predictors = relationship('PredictorModel', back_populates='engine')
