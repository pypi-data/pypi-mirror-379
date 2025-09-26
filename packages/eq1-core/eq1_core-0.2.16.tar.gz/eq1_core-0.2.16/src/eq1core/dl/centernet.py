import dataclasses
import torch
import cv2
import numpy as np
from typing import List
from torchvision import transforms
from .centernet_lib.architecture import cnet
from .centernet_lib.utils import heatmap_bbox


@dataclasses.dataclass
class CenterNetModelParams:
    model_path: str
    resnet_number: int = 18
    number_of_classes: int = 6
    input_size: int = 512
    top_k: int = 50
    down_ratio: int = 4


@dataclasses.dataclass
class DetectionBox:
    x: int
    y: int
    w: int
    h: int
    score: float


@dataclasses.dataclass
class CenterNetModelResult:
    boxes: List[DetectionBox]


class CenterNetModel:
    def __init__(self, params: CenterNetModelParams):
        torch.manual_seed(41)

        self.params = params
        self.use_cuda = torch.cuda.is_available()
        self.device = torch.device('cuda' if self.use_cuda else 'cpu')
        self.model = self.load_model()
        self.model.to(self.device)
        print('CenterNet model loaded on:', self.device)

    def load_model(self) -> torch.nn.Module:
        model = cnet(nb_res=self.params.resnet_number, num_classes=self.params.number_of_classes)
        model.load_state_dict(torch.load(self.params.model_path, map_location="cpu"))

        return model

    def inference(self, image: np.ndarray) -> CenterNetModelResult:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        transform_x = transforms.Compose(
            [
                transforms.ToPILImage(),
                transforms.Resize((self.params.input_size, self.params.input_size)),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
            ]
        )

        img = transform_x(rgb_image)
        img = torch.unsqueeze(img, 0).to(self.device)

        out_hm, out_wh, out_reg = self.model(img)

        bbox, cls, scores = heatmap_bbox(out_hm, out_wh, out_reg, self.params.top_k)

        real_w, real_h = image.shape[1], image.shape[0]
        w_ratio = real_w * self.params.down_ratio / self.params.input_size
        h_ratio = real_h * self.params.down_ratio / self.params.input_size

        cls = cls.unsqueeze(-1).float()
        scores = scores.unsqueeze(-1)

        bbox_cls_score = torch.cat([bbox, cls, scores], dim=-1).squeeze()
        if self.use_cuda:
            bbox_cls_score = bbox_cls_score.cpu()

        bbox_cls_score = bbox_cls_score.detach().numpy()
        bbox_list = []

        for bcs in bbox_cls_score:
            box, cls, score = bcs[:4], int(bcs[4]), bcs[-1]
            if score >= 0.4:
                x1, y1, x2, y2 = np.array(
                    [box[0] * w_ratio, box[1] * h_ratio, box[2] * w_ratio, box[3] * h_ratio]
                ).astype(int)
                bbox_list.append(DetectionBox(x=x1, y=y1, w=x2-x1, h=y2-y1, score=score))
        return CenterNetModelResult(
            boxes=bbox_list
        )
