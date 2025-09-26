from dataclasses import dataclass, field
from typing import Dict, Optional
from enum import Enum
from datetime import datetime


class EventUserType(Enum):
    INSPECTION = 'inspection'
    CLIENT = 'client'


class EventStatusType(Enum):
    WAIT = 'WAIT'
    DONE = 'DONE'
    FAIL = 'FAIL'
    CANCEL = 'CANCEL'


@dataclass
class Event:
    id: Optional[int] = None
    command: str = field(default="")
    data: str = field(default="")
    publisher: str = field(default="")
    subscriber: str = field(default="")
    status: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

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
