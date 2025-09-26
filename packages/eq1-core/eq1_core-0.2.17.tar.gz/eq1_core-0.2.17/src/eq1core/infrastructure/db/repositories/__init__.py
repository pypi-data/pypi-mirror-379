from .common import CommonRepo
from .product import ProductRepo
from .camera import CameraRepo
from .component import ComponentRepo
from .engine import EngineRepo
from .predictor import PredictorRepo
from .product_result import ProductResultRepo
from .component_result import ComponentResultRepo
from .audit_logs import AuditLogRepo
from .vision_presets import VisionPresetRepo
from .users import UserRepo
from .event import EventRepo


from eq1core.domain.port_contrainer import RepositorySet

DBRepositorySet = RepositorySet(
    camera=CameraRepo,
    component=ComponentRepo,
    engine=EngineRepo,
    component_result=ComponentResultRepo,
    predictor=PredictorRepo,
    product=ProductRepo,
    product_result=ProductResultRepo,
    user=UserRepo,
    audit_log=AuditLogRepo,
    vision_preset=VisionPresetRepo,
    event=EventRepo
)
