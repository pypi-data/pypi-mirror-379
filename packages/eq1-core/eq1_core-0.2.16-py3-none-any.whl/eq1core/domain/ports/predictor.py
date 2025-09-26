from typing import List, Protocol
from abc import ABC, abstractmethod
from eq1core.domain.entities.predictor import Predictor
from eq1core.domain.ports.common import CommonPort


class PredictorPort(CommonPort[Predictor], Protocol):
    def get_predictor_by_name(self, name: str) -> dict:
        ...

    def get_predictors_by_engine_id(self, engine_id: int) -> List[Predictor]:
        ...

    def get_predictors_by_product_id(self, product_id: int) -> List[Predictor]:
        ...
