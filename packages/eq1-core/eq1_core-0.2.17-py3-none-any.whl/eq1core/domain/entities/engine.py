from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any


@dataclass
class Engine:
    id: int
    name: str  # 비전 엔진 이름
    base_engine: str  # 실제 구현부 엔진 이름
    alias: Optional[str] = None  # 비전 엔진 별칭
    config: Optional[Dict] = None  # 비전 엔진 설정
    is_activated: int = 1  # 비전 엔진 활성 여부 (0: 비활성, 1: 활성)
    components: List[Any] = field(default_factory=list)
    # predictors: List['PredictorModel'] = field(default_factory=list)
