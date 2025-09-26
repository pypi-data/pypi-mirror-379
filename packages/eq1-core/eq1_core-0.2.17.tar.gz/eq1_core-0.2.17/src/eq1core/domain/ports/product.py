from typing import Optional, Protocol
from abc import ABC, abstractmethod
from eq1core.domain.entities.product import Product
from .common import CommonPort


class ProductPort(CommonPort[Product], Protocol):
    def get_by_code(self, code: str, hide_deleted: bool = True) -> Optional[Product]:
        ...

    def delete(self, instance: Product) -> Optional[Product]:
        ...
