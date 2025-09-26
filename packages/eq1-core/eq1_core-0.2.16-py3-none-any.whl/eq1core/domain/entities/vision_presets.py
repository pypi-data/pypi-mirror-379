from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class VisionPreset:
    id: int
    is_used: bool = field(default=False, metadata={"comment": "선택 여부"})
    name: str = field(default="", metadata={"comment": "프리셋 이름"})
    engine_id: int = field(default=0, metadata={"comment": "엔진 ID"})
    config: Optional[str] = field(default=None, metadata={"comment": "프리셋 데이터 (json)"})
    created_at: datetime = field(default_factory=datetime.now, metadata={"comment": "생성일"})
    updated_at: datetime = field(default_factory=datetime.now, metadata={"comment": "수정일"})

    def __repr__(self):
        return f"<VisionPreset(name={self.name}, engine_id={self.engine_id})>"
