from sqlalchemy import and_
from typing import List, Optional
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.repositories.common import CommonRepo
from eq1core.infrastructure.db.models import CameraModel
from eq1core.infrastructure.db.mapper import to_domain


class CameraRepo(CommonRepo):
    db_session = SessionLocal
    model = CameraModel

    @classmethod
    @to_domain
    def get_by_number(cls, number: int, hide_deleted: bool = True) -> Optional[CameraModel]:
        with cls.db_session() as session:
            query_filters = [cls.model.number == number]

            if hide_deleted:
                query_filters.append(cls.model.is_deleted == 0)

            return session.query(cls.model).filter(and_(*query_filters)).first()

    @classmethod
    @to_domain
    def get_all_by_stage(cls, stage: str, hide_deleted: bool = True) -> List[CameraModel]:
        with cls.db_session() as session:
            query_filters = [cls.model.stage == stage]

            if hide_deleted:
                query_filters.append(cls.model.is_deleted == 0)

            return session.query(cls.model).filter(and_(*query_filters)).all()
            