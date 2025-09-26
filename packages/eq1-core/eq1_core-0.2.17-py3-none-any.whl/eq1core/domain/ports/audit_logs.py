import datetime
from typing import Protocol, List
from abc import ABC, abstractmethod
from eq1core.domain.entities.audit_logs import AuditLog


class AuditLogPort(Protocol):
    def get_expired_audit_logs(self, expired_date: datetime.datetime) -> List[AuditLog]:
        ...
