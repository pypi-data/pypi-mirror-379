import onnxruntime
import numpy as np
from typing import List, Any


class OnnxModel:
    def __init__(
            self,
            session: onnxruntime.InferenceSession,
            input_name: str,
            output_names: List[str],
    ):
        self.session = session
        self.input_name = input_name
        self.output_names = output_names

    def inference(self, inputs: np.ndarray) -> Any:
        return self.session.run(
            output_names=self.output_names,
            input_feed={self.input_name: inputs}
        )


def load_onnx_model(path: str) -> OnnxModel:
    providers = [
        ('CUDAExecutionProvider', {
            'device_id': 0,
            'arena_extend_strategy': 'kNextPowerOfTwo',
            'gpu_mem_limit': 10 * 1024 * 1024 * 1024,
            'cudnn_conv_algo_search': 'EXHAUSTIVE',
            'do_copy_in_default_stream': True,
        }),
        'CPUExecutionProvider',
    ]
    session = onnxruntime.InferenceSession(path, providers=providers)
    input_name = session.get_inputs()[0].name
    output_names = [output.name for output in session.get_outputs()]

    return OnnxModel(
        session=session,
        input_name=input_name,
        output_names=output_names
    )
