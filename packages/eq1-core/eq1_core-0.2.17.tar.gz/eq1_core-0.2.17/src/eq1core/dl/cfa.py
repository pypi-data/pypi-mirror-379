import os
import cv2
import numpy as np
import torch
import random
import dataclasses
import onnxruntime

from typing import Dict, Optional
from .onnx import load_onnx_model


@dataclasses.dataclass
class CfaModelParams:
    wrn50_path: str
    cfa_path: str
    min_score: float
    max_score: float
    threshold: float

    @classmethod
    def from_dict(cls, data: Dict) -> Optional['CfaModelParams']:
        try:
            return cls(
                wrn50_path=data['wrn50_path'],
                cfa_path=data['cfa_path'],
                min_score=data['min_score'],
                max_score=data['max_score'],
                threshold=data['threshold']
            )
        except KeyError as e:
            raise ValueError(f'Missing required key: {e}')

    def to_dict(self):
        return {
            'wrn50_path': self.wrn50_path,
            'cfa_path': self.cfa_path,
            'min_score': self.min_score,
            'max_score': self.max_score,
            'threshold': self.threshold
        }


@dataclasses.dataclass
class CfaResultData:
    is_ok: bool = False
    max_score: float = 0
    scores: np.ndarray = None


class CfaModel:
    def __init__(self, params: CfaModelParams):
        self.params = params

        self.wrn_50_onnx = load_onnx_model(self.params.wrn50_path)
        self.cfa_onnx = load_onnx_model(self.params.cfa_path)

        seed = 1024
        random.seed(seed)
        # torch.manual_seed(seed)
        #
        # is_cuda_available = torch.cuda.is_available()
        # if is_cuda_available:
        #     torch.cuda.manual_seed_all(seed)
        # print(f'cfa model loaded on: {torch.device("cuda" if is_cuda_available else "cpu")}')
        print(f'cfa model loaded on : ', onnxruntime.get_device())

    def transform(self, image):
        image = np.repeat(image[..., np.newaxis], repeats=3, axis=2)
        image = np.array(image).astype(np.float32)
        image = image / 255.0
        image -= np.array([0.485, 0.456, 0.406])
        image /= np.array([0.229, 0.224, 0.225])
        image = np.transpose(image, (2, 0, 1))

        return image

    def process_image_to_inputs(self, image: np.ndarray) -> np.ndarray:
        image = cv2.resize(image, (256, 256), interpolation=cv2.INTER_AREA)

        if image.shape[-1] == 1:
            image = np.squeeze(image, axis=-1)

        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        image = self.transform(image)
        image = image[np.newaxis]

        return image

    def process_outputs_to_result(self, outputs: np.ndarray) -> CfaResultData:
        heatmaps = np.transpose(outputs[1][0], (1, 2, 0))
        heatmaps = cv2.resize(heatmaps, (256, 256))[:, :, np.newaxis]
        heatmaps = self.gaussian_smooth(heatmaps, sigma=4)

        scores = self.rescale(heatmaps, self.params.min_score, self.params.max_score)
        max_score = float(np.max(scores))

        is_ok = False
        if max_score < self.params.threshold:
            is_ok = True

        return CfaResultData(
            is_ok=is_ok,
            max_score=max_score,
            scores=scores
        )

    def gaussian_smooth(self, data: np.ndarray, sigma: int = 4) -> np.ndarray:
        from scipy.ndimage import gaussian_filter
        bs = data.shape[2]
        for i in range(0, bs):
            data[i] = gaussian_filter(data[i], sigma=sigma)
        return data

    def rescale(self, data: np.ndarray, min_scale: float, max_scale: float) -> np.ndarray:
        return (data - min_scale) / (max_scale - min_scale)

    def inference(self, image: np.ndarray) -> CfaResultData:
        inputs = self.process_image_to_inputs(image)
        outputs = self.cfa_onnx.inference(
            self.wrn_50_onnx.inference(inputs)[0]
        )
        return self.process_outputs_to_result(outputs)
