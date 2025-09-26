from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func
from passlib.hash import sha256_crypt
from datetime import datetime
from eq1core.infrastructure.db import Base
from .common import AnotherCommonModel


class UserModel(AnotherCommonModel, Base):
    __tablename__ = 'users'

    created_at = Column(DateTime, nullable=False, server_default=func.now(), comment='생성 일시')
    last_login_at = Column(DateTime, nullable=False, server_default=func.now(), comment='수정 일시')
    login_id = Column(String(50), nullable=False, unique=True, comment='사용자 이름')
    position = Column(String(50), nullable=False, default='직원', comment='사용자 직책')
    name = Column(String(50), nullable=False, unique=True, comment='사용자 이름')
    password = Column(String(256), nullable=False, comment='비밀번호')
    is_active = Column(Integer, nullable=False, default=1, comment='활성 여부 (0: 비활성, 1: 활성)')
    permission = Column(String(10), nullable=False, default="worker", comment='사용자 권한 등급 (worker, manager, admin, developer)')
    password_valid_by = Column(DateTime, nullable=True, comment='비밀번호 유효기간')
    password_reuse_count = Column(Integer, nullable=False, default=0, comment='비밀번호 재사용 횟수')
    is_temporary = Column(Integer, nullable=False, default=0, comment='임시 비밀번호 여부 (0: 일반, 1: 임시)')

    # Password encryption function
    @property
    def hashed_password(self):
        return sha256_crypt.encrypt(self.password)

    @hashed_password.setter
    def hashed_password(self, raw_password):
        self.password = sha256_crypt.encrypt(raw_password)

    # Password verification
    def verify_password(self, password):
        return sha256_crypt.verify(password, self.password)

    # Relationship with audit logs
    audit_logs = relationship('AuditLogModel', back_populates='user')

    def __repr__(self):
        return f"<User(name={self.name}, login_id={self.login_id})>"
