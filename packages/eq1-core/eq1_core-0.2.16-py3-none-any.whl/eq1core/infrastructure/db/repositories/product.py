import traceback
from typing import List, Optional
from sqlalchemy import and_
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.repositories.common import CommonRepo
from eq1core.infrastructure.db.models import ProductModel
from eq1core.infrastructure.db.mapper import to_domain


class ProductRepo(CommonRepo):
    db_session = SessionLocal
    model = ProductModel

    @classmethod
    @to_domain
    def get_by_code(cls, code: str, hide_deleted: bool = True) -> Optional[ProductModel]:
        with cls.db_session() as session:
            query_filters = [cls.model.code == code]

            if hide_deleted:
                query_filters.append(cls.model.is_deleted == 0)

            return session.query(cls.model).filter(and_(*query_filters)).first()

    @classmethod
    @to_domain
    def delete(cls, instance: ProductModel) -> Optional[ProductModel]:
        with cls.db_session() as session:
            try:
                instance.is_deleted = 1
                session.merge(instance)

                instance = session.query(ProductModel).filter_by(id=instance.id).first()
                for child in instance.components:
                    child.is_deleted = 1
                    session.merge(child)

                session.commit()
                session.refresh(instance)

                return instance
            except Exception as e:
                traceback.print_exc()
                session.rollback()
                raise e
