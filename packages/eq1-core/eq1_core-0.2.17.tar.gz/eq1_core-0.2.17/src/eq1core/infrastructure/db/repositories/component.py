from sqlalchemy import and_
from typing import Optional, List
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.models import ProductModel, ComponentModel, CameraModel, EngineModel
from eq1core.infrastructure.db.mapper import to_domain
from eq1core.infrastructure.db.repositories.common import CommonRepo


class ComponentRepo(CommonRepo):
    db_session = SessionLocal
    model = ComponentModel

    @classmethod
    @to_domain
    def get_components_by_product_id(cls, product_id: int) -> List[ComponentModel]:
        with cls.db_session() as session:
            query_filters = [ProductModel.is_deleted == 0,
                             ComponentModel.is_deleted == 0,
                             ComponentModel.product_id == product_id]

            query = session.query(ComponentModel)
            query = query.join(ProductModel, ComponentModel.product_id == ProductModel.id)

            return query.filter(and_(*query_filters)).all()

    @classmethod
    @to_domain
    def get_components_by_product_id_and_camera_id_and_frame_number(cls, product_id: int,
                                                                    camera_id: int,
                                                                    frame_number: int,
                                                                    only_activated: bool = True) -> List[ComponentModel]:
        with cls.db_session() as session:
            query_filters = [ProductModel.is_deleted == 0,
                             CameraModel.is_deleted == 0,
                             ComponentModel.is_deleted == 0,
                             ComponentModel.product_id == product_id,
                             ComponentModel.camera_id == camera_id,
                             ComponentModel.frame_number == frame_number]

            if only_activated:
                query_filters.append(ComponentModel.is_activated == 1)

            query = session.query(ComponentModel)
            query = query.join(CameraModel, ComponentModel.camera_id == CameraModel.id)
            query = query.join(ProductModel, ComponentModel.product_id == ProductModel.id)

            return query.filter(and_(*query_filters)).all()

    @classmethod
    @to_domain
    def get_components_by_engine_id(cls, engine_id: int) -> List[ComponentModel]:
        with cls.db_session() as session:
            query_filters = [EngineModel.is_deleted == 0,
                             ComponentModel.is_deleted == 0,
                             ComponentModel.engine_id == engine_id]

            query = session.query(ComponentModel)
            query = query.join(EngineModel, ComponentModel.engine_id == EngineModel.id)

            return query.filter(and_(*query_filters)).all()

    @classmethod
    @to_domain
    def get_components_by_camera_id(cls, camera_id: int) -> List[ComponentModel]:
        with cls.db_session() as session:
            query_filters = [CameraModel.is_deleted == 0,
                             ComponentModel.is_deleted == 0,
                             ComponentModel.camera_id == camera_id]

            query = session.query(ComponentModel)
            query = query.join(CameraModel, ComponentModel.camera_id == CameraModel.id)

            return query.filter(and_(*query_filters)).all()

    @classmethod
    @to_domain
    def get_frameless_components_by_product_id_and_camera_id(cls, product_id: int, camera_id: int) -> List[ComponentModel]:
        with cls.db_session() as session:
            query_filters = [ProductModel.is_deleted == 0,
                             ComponentModel.is_deleted == 0,
                             ComponentModel.is_activated == 1,
                             ComponentModel.frame_number == -1,
                             ComponentModel.product_id == product_id,
                             ComponentModel.camera_id == camera_id]

            query = session.query(ComponentModel)
            query = query.join(ProductModel, ComponentModel.product_id == ProductModel.id)

            return query.filter(and_(*query_filters)).all()
        
    @classmethod
    @to_domain
    def get_components_by_camera_id_and_frame_number(cls, camera_id: int, frame_number: int) -> List[ComponentModel]:
        with cls.db_session() as session:
            query_filters = [CameraModel.is_deleted == 0,
                             ComponentModel.is_deleted == 0,
                             ComponentModel.camera_id == camera_id,
                             ComponentModel.frame_number == frame_number]

            query = session.query(ComponentModel)
            query = query.join(CameraModel, ComponentModel.camera_id == CameraModel.id)

            return query.filter(and_(*query_filters)).all()