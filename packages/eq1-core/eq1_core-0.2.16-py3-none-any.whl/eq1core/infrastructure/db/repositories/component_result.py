import datetime
from sqlalchemy import and_
from typing import List
from eq1core.data import ComponentResultData
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.repositories.common import CommonRepo
from eq1core.infrastructure.db.models import ComponentResultModel, ProductResultModel
from eq1core.infrastructure.db.mapper import to_domain


class ComponentResultRepo(CommonRepo):
    db_session = SessionLocal
    model = ComponentResultModel

    @classmethod
    @to_domain
    def get_finished_components_by_product_result_id(cls, product_result_id: int) -> List[ComponentResultModel]:
        with cls.db_session() as session:
            query_filters = [
                ProductResultModel.is_deleted == 0,
                ComponentResultModel.is_deleted == 0,
                ProductResultModel.id == product_result_id,
                ]

            query = session.query(ComponentResultModel)
            query = query.join(ProductResultModel, ComponentResultModel.product_result_id == ProductResultModel.id)

            return query.filter(and_(*query_filters)).all()

    @classmethod
    def count_finished_components_by_product_result_id(cls, product_result_id: int) -> int:
        with cls.db_session() as session:
            query_filters = [
                ProductResultModel.is_deleted == 0,
                ComponentResultModel.is_deleted == 0,
                ProductResultModel.id == product_result_id,
            ]

            query = session.query(ComponentResultModel)
            query = query.join(ProductResultModel, ComponentResultModel.product_result_id == ProductResultModel.id)

            return query.filter(and_(*query_filters)).count()

    @classmethod
    def count_finished_components_by_product_result_id_and_camera_number(cls, product_result_id: int, camera_number: int) -> int:
        with cls.db_session() as session:
            query_filters = [
                ProductResultModel.is_deleted == 0,
                ComponentResultModel.is_deleted == 0,
                ProductResultModel.id == product_result_id,
                ComponentResultModel.camera_number == camera_number,
            ]

            query = session.query(ComponentResultModel)
            query = query.join(ProductResultModel, ComponentResultModel.product_result_id == ProductResultModel.id)

            return query.filter(and_(*query_filters)).count()

    @classmethod
    @to_domain
    def get_finished_components_by_product_result_id_and_camera_number_and_frame_number(cls,
                                                                                        product_result_id: int,
                                                                                        camera_number: int,
                                                                                        frame_number: int) -> List[ComponentResultModel]:
        with cls.db_session() as session:
            query_filters = [
                ProductResultModel.is_deleted == 0,
                ComponentResultModel.is_deleted == 0,
                ProductResultModel.id == product_result_id,
                ComponentResultModel.camera_number == camera_number,
                ComponentResultModel.frame_number == frame_number,
            ]

            query = session.query(ComponentResultModel)
            query = query.join(ProductResultModel, ComponentResultModel.product_result_id == ProductResultModel.id)

            return query.filter(and_(*query_filters)).all()

    @classmethod
    def get_component_names_by_product_result_id(cls, product_result_id: int) -> List[str]:
        with cls.db_session() as session:
            query_filters = [
                ProductResultModel.is_deleted == 0,
                ComponentResultModel.is_deleted == 0,
                ProductResultModel.id == product_result_id,
            ]

            query = session.query(ComponentResultModel.component_name)
            query = query.join(ProductResultModel, ComponentResultModel.product_result_id == ProductResultModel.id)
            items = query.filter(and_(*query_filters)).all()

            return [item[0] for item in items]

    @classmethod
    def create_bulk(cls, data: List[ComponentResultData]) -> List[ComponentResultModel]:
        with cls.db_session() as session:
            try:
                models = []
                for component_result in data:
                    instance = cls.model(
                        **component_result.__dict__
                    )
                    models.append(instance)
                    session.add(instance)
                session.commit()
                # 세션이 닫히기 전에 필요한 속성들을 미리 로드
                for model in models:
                    session.refresh(model)
                return models
            except Exception as e:
                import traceback
                traceback.print_exc()
                session.rollback()
                raise e