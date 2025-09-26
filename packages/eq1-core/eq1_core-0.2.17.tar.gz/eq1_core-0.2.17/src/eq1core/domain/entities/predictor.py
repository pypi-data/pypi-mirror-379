import enum
from dataclasses import dataclass, field
from typing import Optional


class DLCategory(enum.Enum):
    ANOMALY = 'ANOMALY'
    CLASSIFICATION = 'CLASSIFICATION'
    DETECTION = 'DETECTION'
    SEGMENTATION = 'SEGMENTATION'


class PredictorType(enum.Enum):
    CV = 'CV'
    DL = 'DL'


@dataclass
class Predictor:
    id: int
    name: str  # 예측 모듈 이름
    type: PredictorType = PredictorType.CV  # 예측 모듈 타입 (CV: 컴퓨터 비전, DL: 딥러닝)
    category: Optional[DLCategory] = None  # 딥러닝 카테고리
    config: Optional[str] = None  # 예측 모듈 세부 설정 (json)
    version: Optional[str] = None  # 버전
