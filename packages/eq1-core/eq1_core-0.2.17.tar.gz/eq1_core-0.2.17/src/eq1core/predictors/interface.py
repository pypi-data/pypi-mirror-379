import abc
import numpy as np
from typing import Any, Tuple


class BasePredictor(abc.ABC):
   @abc.abstractmethod
   def create_from_config(cls, config: dict) -> 'BasePredictor':
        """Create a predictor instance from the given configuration."""
        pass
