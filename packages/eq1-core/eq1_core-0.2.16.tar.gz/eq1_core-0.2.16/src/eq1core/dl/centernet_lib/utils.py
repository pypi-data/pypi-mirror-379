import torch
from torch.nn import functional as F
from typing import Tuple


def hm_topk(
    hm: torch.Tensor, k: int
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    batch, cls, h, w = hm.size()
    out = F.max_pool2d(hm, 3, 1, 1)
    keep_max = (out == hm).float()
    hm = keep_max * hm

    topk_scores, topk_indexs = hm.view(batch, cls, -1).topk(k)  # (batch,cls,k)

    topk_scores, topk_ind = topk_scores.view(batch, -1).topk(k)  # (batch,k)

    topk_cls = topk_ind // k

    topk_indexs = topk_indexs.view(batch, -1).gather(1, topk_ind)

    topk_ys, topk_xs = topk_indexs // w, topk_indexs % w
    return topk_scores, topk_indexs, topk_cls, topk_xs, topk_ys


def heatmap_bbox(
    hm: torch.Tensor, wh: torch.Tensor, reg: torch.Tensor, k: int = 100
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    scores, indexs, cls, xs, ys = hm_topk(hm.sigmoid_(), k)
    batch = reg.size(0)

    reg = reg.view(batch, 2, -1).transpose(2, 1).contiguous()  # (batch,w*h,2)
    reg_indexs = indexs.unsqueeze(2).expand(batch, -1, 2)  # (batch,k,2)
    reg = reg.gather(1, reg_indexs)  # (batch,k,2)
    xs = xs.float() + reg[:, :, 0]
    ys = ys.float() + reg[:, :, 1]
    # wh via reg_indexs
    wh = (
        wh.view(batch, 2, -1).transpose(2, 1).contiguous().gather(1, reg_indexs)
    )  # ((batch,k,2)
    # bbox via xs and wh
    bbox = (
        xs - wh[:, :, 0] / 2,
        ys - wh[:, :, 1] / 2,
        xs + wh[:, :, 0] / 2,
        ys + wh[:, :, 1] / 2,
    )
    bbox = torch.stack(bbox, -1)  # (batch,k,4)
    return bbox, cls, scores
