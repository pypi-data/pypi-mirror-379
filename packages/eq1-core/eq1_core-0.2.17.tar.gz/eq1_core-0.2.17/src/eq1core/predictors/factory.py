from typing import Dict, Any, Type
# from eq1core.data import PredictorData
from eq1core.dto import PredictorDTO
from .interface import BasePredictor


class PredictorRepository:
    _instance = None

    @classmethod
    def _get_instance(cls):
        return cls._instance

    @classmethod
    def instance(cls):
        cls._instance = cls()
        cls.instance = cls._get_instance

        return cls._instance

    def __init__(self):
        self._predictors = {}

    def get(self, name: str, config: dict = None):
        if name in self._predictors:
            return self._predictors[name]

        return None

    def put(self, predictor, name: str):
        self._predictors[name] = predictor

    def remove(self, name: str):
        if name in self._predictors:
            del self._predictors[name]


class PredictorFactory:
    def __init__(self):
        self._registered_predictors: Dict[str, Type[BasePredictor]] = {}

    def register_predictor(self, name: str, predictor_class: Type[BasePredictor]) -> None:
        self._registered_predictors[name.lower()] = predictor_class

    def create_predictor(self, data: PredictorDTO) -> Type[BasePredictor]:
        predictor_name = data.name.lower()
        if predictor_name in self._registered_predictors:
            predictor_class = self._registered_predictors[predictor_name]
            return predictor_class.create_from_config(data.settings)
        else:
            raise ValueError(f'\n{data.name}는 등록되지 않은 Predictor 입니다.'
                             f'\n등록된 Predictor 목록을 참고해주세요. {list(self._registered_predictors.keys())}')

    def get_registered_predictors(self) -> list[str]:
        """등록된 엔진 목록을 반환합니다."""
        return list(self._registered_predictors.keys())
