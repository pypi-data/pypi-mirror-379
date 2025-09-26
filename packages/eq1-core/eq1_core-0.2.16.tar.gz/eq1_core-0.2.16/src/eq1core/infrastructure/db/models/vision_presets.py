# models/vision_presets.py
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from eq1core.infrastructure.db import Base
from .common import CommonModel
from sqlalchemy import func


class VisionPresetModel(CommonModel, Base):
    __tablename__ = 'vision_presets'

    is_used = Column(Boolean, nullable=False, default=False, comment='선택 여부')
    name = Column(String(50), nullable=False, comment='프리셋 이름')
    engine_id = Column(Integer, nullable=False, comment='엔진 ID')
    config = Column(Text, nullable=True, comment='프리셋 데이터 (json)')
    created_at = Column(DateTime, nullable=False, server_default=func.now(), comment='생성일')
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), comment='수정일')

    def __repr__(self):
        return f"<VisionPreset(name={self.name}, engine_id={self.engine_id})>"
