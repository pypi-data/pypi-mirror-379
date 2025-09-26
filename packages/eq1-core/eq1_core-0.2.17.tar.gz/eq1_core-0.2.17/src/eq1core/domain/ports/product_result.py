from abc import ABC, abstractmethod
from typing import Protocol, List, Optional
from datetime import datetime
from .common import CommonPort
from eq1core.domain.entities.product_result import ProductResult


class ProductResultPort(CommonPort[ProductResult], Protocol):
    def get_last_result_by_product_code(self, product_code: str):
        ...

    def get_results_by_product_serial(self, product_serial: str) -> List[ProductResult]:
        ...

    def get_results_by_product_code_and_period(self,
                                               product_code: str,
                                               start_date: datetime = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0),
                                               end_date: datetime = datetime.now(),
                                               exclude_retry: bool = False,
                                               only_ok: bool = False,
                                               only_serial_exists: bool = False) -> List[ProductResult]:
        ...

    def get_unlocked_results_before_certain_time_by_product_code(self,
                                                                 product_code: str,
                                                                 certain_time: datetime) -> List[ProductResult]:
        ...

    def get_expired_results(self, expired_date: datetime) -> List[ProductResult]:
        ...
