from typing import List, Optional
from sqlalchemy import and_
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.repositories.common import CommonRepo
from eq1core.infrastructure.db.models import PredictorModel, ProductModel, ComponentModel, EngineModel
from eq1core.infrastructure.db.mapper import to_domain


class PredictorRepo(CommonRepo):
    db_session = SessionLocal
    model = PredictorModel

    @classmethod
    @to_domain
    def get_predictor_by_name(cls, name: str) -> PredictorModel:
        with cls.db_session() as session:
            return session.query(PredictorModel).filter(PredictorModel.name == name).first()

    @classmethod
    @to_domain
    def get_predictors_by_engine_id(cls, engine_id: int) -> List[PredictorModel]:
        with cls.db_session() as session:
            query_filters = [EngineModel.is_deleted == 0,
                             PredictorModel.is_deleted == 0,
                             EngineModel.id == engine_id]

            query = session.query(PredictorModel)
            query = query.join(EngineModel, PredictorModel.engine_id == EngineModel.id)

            return query.filter(and_(*query_filters)).all()

    @classmethod
    @to_domain
    def get_predictors_by_product_id(cls, product_id: int) -> List[PredictorModel]:
        with cls.db_session() as session:
            query_filters = [ProductModel.is_deleted == 0,
                             ComponentModel.is_deleted == 0,
                             EngineModel.is_deleted == 0,
                             PredictorModel.is_deleted == 0,
                             ProductModel.id == product_id]

            query = session.query(PredictorModel)
            query = query.join(EngineModel, PredictorModel.engine_id == EngineModel.id)
            query = query.join(ComponentModel, EngineModel.id == ComponentModel.engine_id)
            query = query.join(ProductModel, ComponentModel.product_id == ProductModel.id)

            return query.filter(and_(*query_filters)).all()
