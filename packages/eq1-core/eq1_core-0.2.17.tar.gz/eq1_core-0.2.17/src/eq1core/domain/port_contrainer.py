
from dataclasses import dataclass
from .ports import (
    CameraPort, 
    ComponentPort, 
    EnginePort,
    ComponentResultPort, 
    PredictorPort,
    ProductPort, 
    ProductResultPort, 
    UserPort,
    AuditLogPort,
    EventPort,
    VisionPresetPort
)


@dataclass
class RepositorySet:
    camera: CameraPort
    component: ComponentPort
    engine: EnginePort
    component_result: ComponentResultPort
    predictor: PredictorPort
    product: ProductPort
    product_result: ProductResultPort
    user: UserPort
    audit_log: AuditLogPort
    event: EventPort
    vision_preset: VisionPresetPort
