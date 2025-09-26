import enum
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Optional
from eq1core.data import ProductResultCode


@dataclass
class ProductResult:
    id: Optional[int] = None
    product_code: str = field(default_factory=str)
    product_serial: Optional[str] = None
    result_code: Optional[ProductResultCode] = None
    started_at: datetime = field(default_factory=datetime.now)
    finished_at: Optional[datetime] = None
    elapsed_time_ms: Optional[int] = None
    is_locked: int = 0  # 0: unlocked, 1: locked

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
