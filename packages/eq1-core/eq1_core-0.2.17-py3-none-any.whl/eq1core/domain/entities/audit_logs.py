from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AuditLog:
    id: int  # Unique identifier for the audit log
    user_id: Optional[int] = field(default=None, metadata={"comment": "사용자 ID"})
    worker_name: Optional[str] = field(default=None, metadata={"comment": "이벤트 생성자 이름"})
    action: str = field(default="", metadata={"comment": "수행 액션"})
    target: Optional[str] = field(default=None, metadata={"comment": "수행 대상 (tracing -> LOT 번호)"})
    description: Optional[str] = field(default=None, metadata={"comment": "설명"})

    def __repr__(self):
        return f"<AuditLog(action={self.action}, user_id={self.user_id})>"
