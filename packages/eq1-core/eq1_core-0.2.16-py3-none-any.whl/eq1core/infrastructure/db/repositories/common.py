import traceback
import datetime
from sqlalchemy import and_
from sqlalchemy.orm import scoped_session
from typing import Optional, List, Any, Union
from eq1core.infrastructure.db import Base
from eq1core.infrastructure.db.mapper import to_domain


class CommonRepo:
    db_session: scoped_session = None
    model: Base = None

    @classmethod
    @to_domain
    def get_by_id(cls, id: int, hide_deleted: bool = True) -> Optional[Any]:
        with cls.db_session() as session:
            query_filters = [cls.model.id == id]

            if hide_deleted:
                query_filters.append(cls.model.is_deleted == 0)

            return session.query(cls.model).filter(and_(*query_filters)).first()

    @classmethod
    @to_domain
    def get_all(cls, hide_deleted: bool = True) -> List[Any]:
        with cls.db_session() as session:
            query_filters = []

            if hide_deleted:
                query_filters = [cls.model.is_deleted == 0]

            return session.query(cls.model).filter(and_(True, *query_filters)).all()

    @classmethod
    @to_domain
    def create(cls, **kwargs) -> Optional[Any]:
        with cls.db_session() as session:
            try:
                instance = cls.model(**kwargs)
                instance.created_at = datetime.datetime.now()
                instance.updated_at = datetime.datetime.now()
                session.add(instance)
                session.commit()
                session.refresh(instance)
                return instance
            except Exception as e:
                traceback.print_exc()
                session.rollback()
                raise e

    @classmethod
    @to_domain
    def update(cls, id: int, **kwargs) -> Optional[Any]:
        print(f"Updating {cls.model.__name__} with id {id} and kwargs: {kwargs}")
        with cls.db_session() as session:
            query_filters = [cls.model.id == id]
            instance = session.query(cls.model).filter(and_(*query_filters)).first()
            for key, value in kwargs.items():
                if hasattr(cls.model, key):
                    setattr(instance, key, value)

        with cls.db_session() as session:
            try:
                instance.updated_at = datetime.datetime.now()
                session.merge(instance)
                session.commit()

                return instance
            except Exception as e:
                traceback.print_exc()
                session.rollback()
                raise e

    @classmethod
    @to_domain
    def delete(cls, id: int) -> Optional[Any]:
        with cls.db_session() as session:
            query_filters = [cls.model.id == id]
            instance = session.query(cls.model).filter(and_(*query_filters)).first()

        with cls.db_session() as session:
            try:
                instance.is_deleted = 1
                session.merge(instance)
                session.commit()
                return instance
            except Exception as e:
                traceback.print_exc()
                session.rollback()
                raise e

    @classmethod
    @to_domain
    def delete_pure(cls, id: int) -> Optional[Any]:
        with cls.db_session() as session:
            query_filters = [cls.model.id == id]
            instance = session.query(cls.model).filter(and_(*query_filters)).first()

        with cls.db_session() as session:
            try:
                session.delete(instance)
                session.commit()
                return instance
            except Exception as e:
                traceback.print_exc()
                session.rollback()
                raise e

    @classmethod
    @to_domain
    def delete_pure_bulk(cls, ids: List[id]) -> List[Any]:
        with cls.db_session() as session:
            query_filters = [cls.model.id.in_(ids)]
            instances = session.query(cls.model).filter(and_(*query_filters)).all()
            
        with cls.db_session() as session:
            try:
                for instance in instances:
                    session.delete(instance)
                session.commit()
                return instances
            except Exception as e:
                traceback.print_exc()
                session.rollback()
                raise e