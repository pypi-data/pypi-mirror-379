import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Enum, DateTime, BigInteger
from sqlalchemy.orm import relationship
from eq1core.infrastructure.db import Base
from eq1core.infrastructure.db.models.common import CommonModel
from eq1core.data import ProductResultCode


class ProductResultModel(CommonModel, Base):
    __tablename__ = 'product_results'

    product_code = Column(String(50), nullable=False, comment='제품 코드')
    product_serial = Column(String(50), nullable=True, comment='제품 시리얼 번호')
    result_code = Column(Enum(ProductResultCode), nullable=True, comment='검사 결과 코드')
    started_at = Column(DateTime, nullable=False, default=datetime.now(), comment='검사 시작 시간')
    finished_at = Column(DateTime, nullable=True, comment='검사 완료 시간')
    elapsed_time_ms = Column(BigInteger, nullable=True, comment='검사 소요 시간 (초)')
    is_locked = Column(Integer, nullable=False, default=0, comment='검사 결과 잠금 여부 (0: 잠금 해제, 1: 잠금)')  # TODO : finished_at 존재 유/무와 동일한 정보를 담고 있기 때문에 추후 코드 개발 중 불필요하다고 판단될 경우 제거할 것.

    component_results = relationship('ComponentResultModel', back_populates='product_result')

    def to_dict(self):
        return {
            'id': self.id,
            'product_code': self.product_code,
            'product_serial': self.product_serial,
            'result_code': self.result_code.value if self.result_code is not None else None,
            'started_at': self.started_at.strftime('%Y-%m-%d %H:%M:%S'),
            'finished_at': self.finished_at.strftime('%Y-%m-%d %H:%M:%S') if self.finished_at is not None else None,
            'elapsed_time_ms': self.elapsed_time_ms,
            'is_locked': self.is_locked
        }
