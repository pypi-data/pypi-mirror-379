import cv2
import numpy as np
from typing import Dict, Any, Tuple
from eq1core.data import EngineResult, RollSurfaceEngineResult, RollSurfaceEngineParams
from eq1core.engines.interface import BaseEngine


class SampleRollSurfaceEngine(BaseEngine):
    @classmethod
    @property
    def name(cls) -> str:
        return "SampleEngine"

    def get_results(self, image: np.ndarray) -> Tuple[bool, RollSurfaceEngineResult]:
        # Mock implementation for testing purposes
        result = RollSurfaceEngineResult(
            is_ok=True,
            is_failed=False,
            base_engine_name='SampleEngine',
            engine_params=RollSurfaceEngineParams(),
            image=None,
            patch_results=[],
            bboxes_with_pixel_unit=[],
            bboxes_with_mm_unit=[],
            bbox_scores=[],
        )
        return False, result

    @classmethod
    def create_from_config(cls, config: dict):
        # Mock implementation for testing purposes
        return cls()


class SampleEngine(BaseEngine):
    @classmethod
    @property  # TODO : deprecated
    def name(cls) -> str:  
        return "Sample-Engine"

    def get_results(self, image: np.ndarray) -> Tuple[bool, EngineResult]:
        # Mock implementation for testing purposes
        result = EngineResult(
           
        )
        return False, result

    @classmethod
    def create_from_config(cls, config: dict):
        # Mock implementation for testing purposes
        return cls()