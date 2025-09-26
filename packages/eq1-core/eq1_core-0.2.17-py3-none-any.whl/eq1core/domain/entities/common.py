from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CommonModel:
    id: int = field(default=None)
    is_deleted: int = field(default=0, metadata={"comment": "삭제 여부"})
    created_at: datetime = field(default_factory=datetime.now, metadata={"comment": "생성일"})
    updated_at: datetime = field(default_factory=datetime.now, metadata={"comment": "수정일"})


@dataclass
class AnotherCommonModel:
    id: int = field(default=None)
    created_at: datetime = field(default_factory=datetime.now, metadata={"comment": "생성일"})
    updated_at: datetime = field(default_factory=datetime.now, metadata={"comment": "수정일"})
