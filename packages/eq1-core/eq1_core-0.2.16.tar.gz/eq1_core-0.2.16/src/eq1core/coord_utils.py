from typing import List, Tuple, Optional
import cv2
import math
import numpy as np


def calculate_angle(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """
    각도 계산 수행

    (1, 0) -> 0 도
    (0, 1) -> 90 도
    (-1, 0) -> 180 도
    (0, -1) -> 270 도
    """
    x1, y1 = point1
    x2, y2 = point2
    dx, dy = x2 - x1, y1 - y2

    angle_radians = math.atan2(dy, dx)
    angle_degrees = math.degrees(angle_radians)

    if dy < 0:  # point2 가 point1 기준 3, 4 사분면에 위치하는 경우, atan2 계산 값이 0 ~ -180 도 값을 갖기 때문에 360을 더해줌
        angle_degrees += 360

    return angle_degrees


def convert_degree_to_unit_vector(degree: float) -> Tuple[float, float]:
    """degree 각도를 갖는 단위 벡터 반환"""
    if degree > 180:
        _degree = degree - 360
    else:
        _degree = degree

    return math.cos(math.radians(_degree)), -math.sin(math.radians(_degree))


def get_intersection_point(points: List[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
    """두 개의 선분의 교차점 반환"""
    point1, point2, point3, point4 = points[0], points[2], points[1], points[3]

    if points[0][1] > points[1][1]:
        point1, point3 = points[1], points[0]
    if points[2][1] < points[3][1]:
        point2, point4 = points[3], points[2]

    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    x4, y4 = point4

    # 분모가 0이 되는 경우를 방지
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None  # 평행하거나 일치하는 경우

    # 교차점 찾기
    px = int(((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom)
    py = int(((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom)

    # 교차점이 두 선분에 속하는지 확인
    if (min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2) and
            min(x3, x4) <= px <= max(x3, x4) and min(y3, y4) <= py <= max(y3, y4)):
        return px, py
    else:
        return None


def get_transform_matrix(src_points: List[List[int]], dst_points: List[List[int]]) -> np.ndarray:
    """변환 행렬 계산"""
    if len(src_points) != 4 or len(dst_points) != 4:
        raise ValueError("The number of points must be 4.")
    src_points = np.array(src_points, dtype=np.float32)
    dst_points = np.array(dst_points, dtype=np.float32)

    return cv2.getPerspectiveTransform(src_points, dst_points)


def transform_point(point: Tuple[float, float], matrix: np.ndarray) -> Tuple[float, float]:
    """점 변환"""
    point = np.array([[[point[0], point[1]]]], dtype=np.float32)
    transformed_point = cv2.perspectiveTransform(point, matrix)

    return float(transformed_point[0][0][0]), float(transformed_point[0][0][1])


def transform_angle(point: Tuple[float, float], degree: float, matrix: np.ndarray) -> float:
    """각도 변환"""
    x, y = point
    dx, dy = convert_degree_to_unit_vector(degree)
    dst_point = x + dx, y + dy

    transformed_src = transform_point(point, matrix)
    transformed_dst = transform_point(dst_point, matrix)

    transformed_angle = calculate_angle(transformed_src, transformed_dst)

    return transformed_angle


def transform_coord(coord: Tuple[float, float, float], matrix: np.ndarray) -> Tuple[float, float, float]:
    """좌표와 각도 변환"""
    x1, y1, r1 = coord
    dx, dy = convert_degree_to_unit_vector(r1)
    x2, y2 = x1 + dx, y1 + dy

    transformed_x1, transformed_y1 = transform_point((x1, y1), matrix)
    transformed_x2, transformed_y2 = transform_point((x2, y2), matrix)

    transformed_r1 = calculate_angle(
        (transformed_x1, transformed_y1),
        (transformed_x2, transformed_y2)
    )

    return transformed_x1, transformed_y1, transformed_r1


def iou(bbox1, bbox2):
    x1, y1, w1, h1 = bbox1
    x2, y2, w2, h2 = bbox2

    x1_max, y1_max = x1 + w1, y1 + h1
    x2_max, y2_max = x2 + w2, y2 + h2

    inter_x1 = max(x1, x2)
    inter_y1 = max(y1, y2)
    inter_x2 = min(x1_max, x2_max)
    inter_y2 = min(y1_max, y2_max)

    inter_width = max(0, inter_x2 - inter_x1)
    inter_height = max(0, inter_y2 - inter_y1)
    inter_area = inter_width * inter_height

    bbox1_area = w1 * h1
    bbox2_area = w2 * h2

    union_area = bbox1_area + bbox2_area - inter_area

    return inter_area / union_area if union_area != 0 else 0


def merge_boxes(bbox1, bbox2):
    """
    bbox 형식: (x, y, w, h)
    """
    x1, y1, w1, h1 = bbox1
    x2, y2, w2, h2 = bbox2

    new_x1 = min(x1, x2)
    new_y1 = min(y1, y2)
    new_x2 = max(x1 + w1, x2 + w2)
    new_y2 = max(y1 + h1, y2 + h2)

    new_w = new_x2 - new_x1
    new_h = new_y2 - new_y1

    return new_x1, new_y1, new_w, new_h


def merge_overlap_boxes(boxes: List[Tuple[int, int, int, int]], scores: List[float], iou_threshold: float = 0.0001) -> Tuple[List[Tuple[int, int, int, int]], List[float]]:
    """
    겹치는 박스들을 병합하고 max score 를 취합니다.
    
    Args:
        boxes: 박스 좌표 리스트 [(x, y, w, h), ...]
        scores: 각 박스의 점수 리스트
        iou_threshold: 겹침 판단을 위한 IoU 임계값
        
    Returns:
        병합된 박스 좌표 리스트와 점수 리스트
    """
    if not boxes:
        return [], []
        
    boxes_and_scores = list(zip(boxes, scores))
    boxes_and_scores.sort(key=lambda x: x[1], reverse=True)
    
    merged_results = []
    remaining = boxes_and_scores.copy()
    
    while remaining:
        target_box, target_score = remaining.pop(0)
        overlap_indexes = []
        
        for i, (other_box, other_score) in enumerate(remaining):
            if iou(target_box, other_box) >= iou_threshold:
                overlap_indexes.append(i)
                target_box = merge_boxes(target_box, other_box)
                target_score = max(target_score, other_score)
        
        for i in reversed(overlap_indexes):
            remaining.pop(i)
            
        merged_results.append((target_box, target_score))
        
    merged_boxes = [box for box, _ in merged_results]
    merged_scores = [score for _, score in merged_results]
    
    return merged_boxes, merged_scores


def nms_merge(bboxes, threshold=0.5):
    while True:
        bboxes = sorted(bboxes, key=lambda bbox: bbox[2] * bbox[3], reverse=True)
        merged = False
        new_bboxes = []
        i = 0
        while i < len(bboxes):
            bbox1 = bboxes[i]
            j = i + 1
            merged_bbox = bbox1

            while j < len(bboxes):
                bbox2 = bboxes[j]
                if iou(merged_bbox, bbox2) >= threshold:
                    merged_bbox = merge_boxes(merged_bbox, bbox2)
                    bboxes.pop(j)
                    merged = True
                else:
                    j += 1

            new_bboxes.append(merged_bbox)
            bboxes.pop(i)

        bboxes = new_bboxes

        if not merged:
            break

    return bboxes


# if __name__ == '__main__':
#     bbox1 = (50, 50, 100, 100)
#     bbox2 = (80, 80, 100, 100)
#     bbox3 = (120, 120, 20, 20)
#
#     image = np.zeros((500, 500, 3), dtype=np.uint8)
#     cv2.rectangle(image, (bbox1[0], bbox1[1]), (bbox1[0] + bbox1[2], bbox1[1] + bbox1[3]), (255, 0, 0), 2)
#     cv2.rectangle(image, (bbox2[0], bbox2[1]), (bbox2[0] + bbox2[2], bbox2[1] + bbox2[3]), (0, 255, 0), 2)
#     cv2.rectangle(image, (bbox3[0], bbox3[1]), (bbox3[0] + bbox3[2], bbox3[1] + bbox3[3]), (255, 255, 0), 2)
#
#     bboxes = nms_merge([bbox1, bbox2, bbox3], threshold=0.01)
#     for bbox in bboxes:
#         cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 0, 255), 2)
#
#     cv2.imshow('image', image)
#     cv2.waitKey(0)