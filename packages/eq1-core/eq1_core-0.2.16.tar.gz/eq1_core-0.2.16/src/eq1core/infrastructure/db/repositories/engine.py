from sqlalchemy import and_
from typing import List, Optional
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.repositories.common import CommonRepo
from eq1core.infrastructure.db.models import EngineModel, ComponentModel
from eq1core.infrastructure.db.mapper import to_domain


class EngineRepo(CommonRepo):
    db_session = SessionLocal
    model = EngineModel

    @classmethod
    @to_domain
    def get_all(cls, only_activated: bool = False, hide_deleted: bool = True) -> List[EngineModel]:
        with cls.db_session() as session:
            query_filters = []

            if hide_deleted:
                query_filters.append(EngineModel.is_deleted == 0)

            if only_activated:
                query_filters.append(EngineModel.is_activated == 1)

            return session.query(EngineModel).filter(and_(True, *query_filters)).all()

    @classmethod
    @to_domain
    def get_by_component_id(cls, component_id: int) -> List[EngineModel]:
        with cls.db_session() as session:
            query_filters = [
                EngineModel.is_deleted == 0,
                EngineModel.components.any(
                    and_(
                        ComponentModel.is_deleted == 0,
                        ComponentModel.id == component_id
                    )
                )
            ]

            return session.query(EngineModel).filter(and_(*query_filters)).all()
        
    @classmethod
    @to_domain
    def get_by_name(cls, name: str) -> EngineModel:
        with cls.db_session() as session:
            return session.query(EngineModel).filter(EngineModel.name == name).first()