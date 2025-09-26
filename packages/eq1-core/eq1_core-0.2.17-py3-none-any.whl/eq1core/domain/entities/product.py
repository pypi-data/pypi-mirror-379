from dataclasses import dataclass, field
from typing import List, Optional
from .component import Component


@dataclass
class Product:
    id: int
    name: str
    code: str
    thumbnail_path: Optional[str] = None
    components: List[Component] = field(default_factory=list)  # 관련 컴포넌트 리스트
