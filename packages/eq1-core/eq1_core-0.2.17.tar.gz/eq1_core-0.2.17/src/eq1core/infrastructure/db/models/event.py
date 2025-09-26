from enum import Enum
from typing import Dict
from sqlalchemy import Column, Integer, String, Text
from eq1core.infrastructure.db import Base
from eq1core.infrastructure.db.models.common import CommonModel


class EventUserType(Enum):
    INSPECTION = 'inspection'
    CLIENT = 'client'


class EventStatusType(Enum):
    WAIT = 'WAIT'
    DONE = 'DONE'
    FAIL = 'FAIL'
    CANCEL = 'CANCEL'


class EventModel(CommonModel, Base):
    __tablename__ = 'events'

    command = Column(String(20), nullable=False, unique=False, comment='이벤트 종류')
    data = Column(Text, nullable=False, unique=False, comment='이벤트 처리를 위한 세부정보 (json)')
    publisher = Column(String(20), nullable=False, unique=False, comment='이벤트 발생자')
    subscriber = Column(String(20), nullable=False, unique=False, comment='이벤트 구독자')
    status = Column(String(20), nullable=True, unique=False, comment='이벤트 처리 상태 (WAIT, DONE, FAIL, CANCEL)')

    def as_dict(self) -> Dict:
        return {
            'id': self.id,
            'command': self.command,
            'data': self.data,
            'publisher': self.publisher,
            'subscriber': self.subscriber,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
