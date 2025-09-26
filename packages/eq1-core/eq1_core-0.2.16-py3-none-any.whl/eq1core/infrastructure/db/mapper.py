from typing import Optional, Any
from . import Base
from .models import AuditLogModel, CameraModel, ComponentModel, ComponentResultModel, EngineModel, EventModel, PredictorModel, ProductModel, ProductResultModel, UserModel, VisionPresetModel
from eq1core.domain.entities import AuditLog, Camera, Component, ComponentResult, Engine, Event, Predictor, Product, ProductResult, User, VisionPreset
from functools import wraps
from typing import Union, List

"""
예시 : 
@to_domain
def get_by_id(id: int) -> Optional[ComponentModel]:
    with cls.db_session() as session:
        model = session.query(ComponentModel).filter(ComponentModel.id == id).first()
        return model    

@to_domain
def get_all() -> List[ComponentModel]:
    with cls.db_session() as session:
        models = session.query(ComponentModel).all()
        return models

"""


def to_domain(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            return [convert_model_to_entity(model) for model in result]
        elif isinstance(result, Base):
            return convert_model_to_entity(result)
        return result
    return wrapper


def from_domain(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        entity = func(*args, **kwargs)
        if isinstance(entity, Base):
            return entity
        raise ValueError("Expected a Base model instance")
    return wrapper


def convert_model_to_entity(model: Base) -> Optional[Any]:
    if isinstance(model, AuditLogModel):
        return AuditLog(
            id=model.id,
            user_id=model.user_id,
            worker_name=model.worker_name,
            action=model.action,
            target=model.target,
            description=model.description
        )

    if isinstance(model, CameraModel):
        return Camera(
            id=model.id,
            number=model.number,
            connection_index=model.connection_index,
            camera_serial=model.camera_serial,
            grabber_serial=model.grabber_serial,
            name=model.name,
            stage=model.stage,
            config=model.config,
            number_of_frames=model.number_of_frames,
        )

    if isinstance(model, ComponentModel):
        return Component(
            id=model.id,
            product_id=model.product_id,
            camera_id=model.camera_id,
            engine_id=model.engine_id,
            name=model.name,
            frame_number=model.frame_number,
            position_index=model.position_index,
            roi=model.roi,
            is_activated=model.is_activated      
        )

    if isinstance(model, ComponentResultModel):
        return ComponentResult(
            id=model.id,
            product_result_id=model.product_result_id,
            component_name=model.component_name,
            camera_number=model.camera_number,
            frame_number=model.frame_number,
            roi=model.roi,
            started_at=model.started_at,
            finished_at=model.finished_at,
            result=model.result,
            elapsed_time_ms=model.elapsed_time_ms,
            detail=model.detail,
            origin_image_path=model.origin_image_path,
            result_image_path=model.result_image_path
        )

    if isinstance(model, EngineModel):
        return Engine(
            id=model.id,
            name=model.name,
            base_engine=model.base_engine,
            alias=model.alias,
            config=model.config,
            is_activated=model.is_activated        
        )

    if isinstance(model, EventModel):
        return Event(
            id=model.id,
            command=model.command,
            data=model.data,
            publisher=model.publisher,
            subscriber=model.subscriber,
            status=model.status        
        )

    if isinstance(model, PredictorModel):
        return Predictor(
            id=model.id,
            name=model.name,
            type=model.type.value,
            category=model.category.value if model.category else None,
            config=model.config,
            version=model.version        
        )

    if isinstance(model, ProductModel):
        return Product(
            id=model.id,
            name=model.name,
            code=model.code,
            thumbnail_path=model.thumbnail_path,
        )

    if isinstance(model, ProductResultModel):
        return ProductResult(
            id=model.id,
            product_code=model.product_code,
            product_serial=model.product_serial,
            result_code=model.result_code,
            started_at=model.started_at,
            finished_at=model.finished_at if model.finished_at else None,
            elapsed_time_ms=model.elapsed_time_ms,
            is_locked=model.is_locked        
        )

    if isinstance(model, UserModel):
        return User(
            id=model.id,
            created_at=model.created_at,
            last_login_at=model.last_login_at,
            login_id=model.login_id,
            position=model.position,
            name=model.name,
            password=model.password,
            is_active=model.is_active,
            permission=model.permission,
            password_valid_by=model.password_valid_by,
            password_reuse_count=model.password_reuse_count,
            is_temporary=model.is_temporary        
        )

    if isinstance(model, VisionPresetModel):
        return VisionPreset(
            id=model.id,
            is_used=model.is_used,
            name=model.name,
            engine_id=model.engine_id,
            config=model.config,
            created_at=model.created_at,
            updated_at=model.updated_at
        )


def convert_entity_to_model(entity: Any) -> Optional[Base]:
    if isinstance(entity, AuditLog):
        return AuditLogModel(
            id=entity.id,
            user_id=entity.user_id,
            worker_name=entity.worker_name,
            action=entity.action,
            target=entity.target,
            description=entity.description
        )

    if isinstance(entity, Camera):
        return CameraModel(
            id=entity.id,
            number=entity.number,
            connection_index=entity.connection_index,
            camera_serial=entity.camera_serial,
            grabber_serial=entity.grabber_serial,
            name=entity.name,
            stage=entity.stage,
            config=entity.config,
            number_of_frames=entity.number_of_frames
        )

    if isinstance(entity, Component):
        return ComponentModel(
            id=entity.id,
            product_id=entity.product_id,
            camera_id=entity.camera_id,
            engine_id=entity.engine_id,
            name=entity.name,
            frame_number=entity.frame_number,
            position_index=entity.position_index,
            roi=entity.roi,
            is_activated=entity.is_activated
        )

    if isinstance(entity, ComponentResult):
        return ComponentResultModel(
            id=entity.id,
            product_result_id=entity.product_result_id,
            component_name=entity.component_name,
            camera_number=entity.camera_number,
            frame_number=entity.frame_number,
            roi=entity.roi,
            started_at=entity.started_at,
            finished_at=entity.finished_at if entity.finished_at else None,
            result=entity.result,
            elapsed_time_ms=entity.elapsed_time_ms,
            detail=entity.detail,
            origin_image_path=entity.origin_image_path,
            result_image_path=entity.result_image_path
        )

    if isinstance(entity, Engine):
        import json
        
        try:
            config = json.loads(entity.config)
        except json.JSONDecodeError:
            config = entity.config

        return EngineModel(
            id=entity.id,
            name=entity.name,
            base_engine=entity.base_engine,
            alias=entity.alias,
            config=entity.config,
            is_activated=entity.is_activated
        )

    if isinstance(entity, Event):
        return EventModel(
            id=entity.id,
            command=entity.command.value if entity.command else None,
            data=str(entity.data) if entity.data else None,  # Assuming data can be serialized to string
            publisher=str(entity.publisher) if entity.publisher else None,  # Assuming publisher can be serialized to string
            subscriber=str(entity.subscriber) if entity.subscriber else None,  # Assuming subscriber can be serialized to string
            status=entity.status.value if entity.status else None,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )