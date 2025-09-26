import datetime
from sqlalchemy import and_
from typing import List, Optional
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.models import AuditLogModel
from eq1core.infrastructure.db.mapper import to_domain
from eq1core.infrastructure.db.repositories.common import CommonRepo


class AuditLogRepo(CommonRepo):
    db_session = SessionLocal
    model = AuditLogModel

    @classmethod
    @to_domain
    def get_expired_audit_logs(cls, expired_date: datetime) -> List[AuditLogModel]:
        with cls.db_session() as session:
            return session.query(cls.model).filter(and_(cls.model.created_at < expired_date)).all()
