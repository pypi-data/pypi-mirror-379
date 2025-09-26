from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from eq1core.infrastructure.db import Base
from .common import AnotherCommonModel


class AuditLogModel(AnotherCommonModel, Base):
    __tablename__ = 'audit_logs'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, comment='사용자 ID')

    worker_name = Column(String(50), nullable=True, comment='이벤트 생성자 이름')
    action = Column(String(50), nullable=False, comment='수행 액션')
    target = Column(String(50), nullable=True, comment='수행 대상 (tracing -> LOT 번호)')
    description = Column(Text, nullable=True, comment='설명')

    user = relationship('UserModel', back_populates='audit_logs')

    def __repr__(self):
        return f"<AuditLog(action={self.action}, user_id={self.user_id})>"
