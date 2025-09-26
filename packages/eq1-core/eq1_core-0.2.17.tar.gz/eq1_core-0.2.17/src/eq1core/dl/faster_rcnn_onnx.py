import cv2
import random
import torch
import numpy as np
from typing import List, Any, Tuple
from .onnx import load_onnx_model, OnnxModel


class FasterRCNNOnnx:
    def __init__(self,
                 model_path: str,
                 input_size: List[int]):
        """

        :param model_path: path of onnx model file
        :param input_size: [width, height]
        """
        self._model: OnnxModel = load_onnx_model(model_path)
        self._input_size = input_size

        seed = 1024
        random.seed(seed)
        torch.manual_seed(seed)

        use_cuda = torch.cuda.is_available()
        if use_cuda:
            torch.cuda.manual_seed_all(seed)
        print(f'cfa model loaded on: {torch.device("cuda" if use_cuda else "cpu")}')

    def __call__(self, image: np.ndarray) -> Any:
        return self.inference(image)

    def preprocess(self, image: np.ndarray) -> np.ndarray:
        image = cv2.resize(image, self._input_size)
        image = image.transpose(2, 0, 1)
        image = image.astype(np.float32)
        return image

    def inference(self, image: np.ndarray) -> Tuple[List, List, List]:
        """

        :param image: rgb image
        :return: [boxes, scores, classes]
        """
        preprocessed_image = self.preprocess(image)
        results = self._model.inference(preprocessed_image)
        # example : [array([[587.65375, 448.26187, 708.6529 , 502.04562]], dtype=float32), array([0], dtype=int64), array([0.99707043], dtype=float32), array([800, 956], dtype=int64)]
        bboxes = results[0]
        classes = results[1]
        scores = results[2]

        bboxes = [list(map(int, box)) for box in bboxes]
        scores = [float(score) for score in scores]
        classes = [int(cls) for cls in classes]

        return bboxes, scores, classes
