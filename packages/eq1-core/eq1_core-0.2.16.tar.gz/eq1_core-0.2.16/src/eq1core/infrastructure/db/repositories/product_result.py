from typing import List
from sqlalchemy import and_, func
from datetime import datetime
from eq1core.data import ProductResultCode
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.repositories.common import CommonRepo
from eq1core.infrastructure.db.models import ProductResultModel
from eq1core.infrastructure.db.mapper import to_domain


class ProductResultRepo(CommonRepo):
    db_session = SessionLocal
    model = ProductResultModel

    @classmethod
    @to_domain
    def get_last_result_by_product_code(cls, product_code: str) -> ProductResultModel:
        with cls.db_session() as session:
            query_filters = [ProductResultModel.is_deleted == 0,
                             ProductResultModel.product_code == product_code]

            return session.query(cls.model).filter(and_(*query_filters)).order_by(ProductResultModel.id.desc()).first()

    @classmethod
    @to_domain
    def get_results_by_product_serial(cls, product_serial: str) -> List[ProductResultModel]:
        with cls.db_session() as session:
            query_filters = [ProductResultModel.is_deleted == 0,
                             ProductResultModel.product_serial == product_serial]

            return session.query(cls.model).filter(and_(*query_filters)).all()

    @classmethod
    @to_domain
    def get_results_by_product_code_and_period(cls, product_code: str,
                                               start_date: datetime = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0),
                                               end_date: datetime = datetime.now(),
                                               exclude_retry: bool = False,
                                               only_ok: bool = False,
                                               only_serial_exists: bool = False) -> List[ProductResultModel]:
        """

        :param product_code:
        :param start_date:
        :param end_date:
        :param exclude_retry: serial 번호가 중복된 경우 가장 최근 시간의 결과만 가져올 지 여부
        :return:
        """
        with cls.db_session() as session:
            if start_date > end_date:
                raise ValueError('start_date must be less than end_date')

            query_filters = [ProductResultModel.is_deleted == 0,
                             ProductResultModel.product_code == product_code,
                             ProductResultModel.started_at >= start_date,
                             ProductResultModel.started_at <= end_date]

            if only_ok:
                query_filters.append(ProductResultModel.result_code == ProductResultCode.OK)

            if only_serial_exists:
                query_filters.append(ProductResultModel.product_serial.isnot(None))

            query = session.query(ProductResultModel)

            if exclude_retry:
                subquery = (
                    session.query(
                        ProductResultModel.product_serial,
                        func.max(ProductResultModel.started_at).label('latest_started_at_in_serial_group')
                    )
                    .filter(ProductResultModel.is_deleted == 0)
                    .group_by(ProductResultModel.product_serial)
                    .subquery()
                )

                query = query.join(
                    subquery,
                    and_(
                        ProductResultModel.product_serial == subquery.c.product_serial,
                        ProductResultModel.started_at == subquery.c.latest_started_at_in_serial_group
                    )
                )

            return query.filter(and_(*query_filters)).all()

    @classmethod
    @to_domain
    def get_unlocked_results_before_certain_time_by_product_code(cls,
                                                                 product_code: str,
                                                                 certain_time: datetime) -> List[ProductResultModel]:
        with cls.db_session() as session:
            query_filters = [ProductResultModel.is_deleted == 0,
                             ProductResultModel.product_code == product_code,
                             ProductResultModel.is_locked == 0,
                             ProductResultModel.started_at < certain_time]

            query = session.query(ProductResultModel)
            query = query.filter(and_(*query_filters))
            query = query.order_by(ProductResultModel.started_at)

            return query.all()

    @classmethod
    @to_domain
    def get_expired_results(cls, expired_date: datetime) -> List[ProductResultModel]:
        with cls.db_session() as session:
            query_filters = [ProductResultModel.is_deleted == 0,
                             ProductResultModel.started_at < expired_date]

            return session.query(cls.model).filter(and_(*query_filters)).all()