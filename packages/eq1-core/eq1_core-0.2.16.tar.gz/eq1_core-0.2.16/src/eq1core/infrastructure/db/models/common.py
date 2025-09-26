from sqlalchemy import Column, Integer, DateTime
from datetime import datetime


class CommonModel:
    __tablename__ = None

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_deleted = Column(Integer, nullable=False, default=0, comment='삭제 여부')
    created_at = Column(DateTime, nullable=False, default=datetime.now(), comment='생성일')
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), comment='수정일')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class AnotherCommonModel:
    __tablename__ = None

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now(), comment='생성일')
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), comment='수정일')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
