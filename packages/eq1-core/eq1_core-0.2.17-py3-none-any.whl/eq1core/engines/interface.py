import abc
import numpy as np
from typing import Any, Tuple


class BaseEngine(abc.ABC):
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @abc.abstractmethod
    def get_results(self, image: np.ndarray) -> Tuple[bool, Any]:
        pass

    @classmethod
    @abc.abstractmethod
    def create_from_config(cls, config: dict):
        pass
