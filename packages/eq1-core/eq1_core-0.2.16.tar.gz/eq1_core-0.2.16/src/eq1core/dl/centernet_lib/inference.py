from torchvision import transforms
from centernet.models import cnet
import centernet.utils as utils
from typing import List, Any
import numpy as np
import torch
import cv2


def load_model(options: Any, device: torch.device) -> torch.nn.Module:
    model = cnet(nb_res=options.resnet_num, num_classes=options.num_classes)
    model.load_state_dict(torch.load(options.model_path, map_location="cpu"))
    model = model.to(device)
    return model


def inference(
    option: Any, device: torch.device, test_img: np.ndarray
) -> List[np.ndarray]:
    model = load_model(option, device)
    test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

    transform_x = transforms.Compose(
        [
            transforms.ToPILImage(),
            transforms.Resize((option.input_size, option.input_size)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )

    img = transform_x(test_img)
    img = torch.unsqueeze(img, 0).to(device)

    out_hm, out_wh, out_reg = model(img)

    bbox, cls, scores = utils.heatmap_bbox(out_hm, out_wh, out_reg, option.topk)

    real_w, real_h = test_img.shape[1], test_img.shape[0]
    w_ratio = real_w * option.down_ratio / option.input_size
    h_ratio = real_h * option.down_ratio / option.input_size

    cls = cls.unsqueeze(-1).float()
    scores = scores.unsqueeze(-1)

    bbox_cls_score = torch.cat([bbox, cls, scores], dim=-1).squeeze()
    bbox_cls_score = bbox_cls_score.detach().numpy()
    bbox_list = []

    for bcs in bbox_cls_score:
        box, cls, score = bcs[:4], int(bcs[4]), bcs[-1]
        if score >= 0.6:
            box = np.array(
                [box[0] * w_ratio, box[1] * h_ratio, box[2] * w_ratio, box[3] * h_ratio]
            ).astype(int)
            bbox_list.append(box)

    return bbox_list
