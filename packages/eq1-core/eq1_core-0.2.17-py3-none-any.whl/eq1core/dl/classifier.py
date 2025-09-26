from typing import List
from .onnx import load_onnx_model


class Resnet50Classifier:
    def __init__(self, model_path: str):
        self.model = load_onnx_model(model_path)

    def inference(self, image) -> List[int]:
        return self.model.inference(image)[0]
