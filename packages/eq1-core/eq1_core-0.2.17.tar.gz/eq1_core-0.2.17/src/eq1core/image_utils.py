import cv2
import numpy as np
from typing import List, Tuple, Optional
from matplotlib import colors
from PIL import Image, ImageEnhance


def adjust_cv_image_brightness(image: np.ndarray, brightness_enhancement_factor: float) -> np.ndarray:
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    enhancer = ImageEnhance.Brightness(pil_image)
    enhanced_image = np.array(enhancer.enhance(brightness_enhancement_factor))
    return cv2.cvtColor(enhanced_image, cv2.COLOR_RGB2BGR)


def get_binary_image(img: np.ndarray, threshold: int = 125, mode: int = cv2.THRESH_BINARY) -> np.ndarray:
    """이미지를 전처리하여 이진화된 이미지를 반환"""
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(img, threshold, 255, mode)
    return binary_image


def filter_white_noise(img: np.ndarray, kernel_size: int = 5, iter_num: int = 2) -> np.ndarray:
    """이미지에 모폴로지 연산을 적용"""
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    img = cv2.erode(img, kernel, iterations=iter_num)
    img = cv2.dilate(img, kernel, iterations=iter_num)
    return img


def filter_black_noise(img: np.ndarray, kernel_size: int = 5, iter_num: int = 2) -> np.ndarray:
    """이미지에 모폴로지 연산을 적용"""
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    img = cv2.dilate(img, kernel, iterations=iter_num)
    img = cv2.erode(img, kernel, iterations=iter_num)
    return img


def find_contours(img: np.ndarray, threshold: int = 125) -> Tuple[np.ndarray]:
    """이미지에서 윤곽선을 찾아 반환"""
    preprocessed = get_binary_image(img, threshold)
    contours, _ = cv2.findContours(preprocessed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def find_contours_with_trim(img: np.ndarray, threshold: int = 125) -> Tuple[np.ndarray]:
    """이미지에서 윤곽선을 찾아 반환"""
    preprocessed = get_binary_image(img, threshold)
    preprocessed = trim_contour_line(preprocessed)
    contours, _ = cv2.findContours(preprocessed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def filter_contours_by_area(contours: Tuple[np.ndarray], area_threshold: int, range_ratio: float = 0.2) -> List[np.ndarray]:
    """주어진 면적 범위에 따라 윤곽선을 필터링"""
    return [cnt for cnt in contours if area_threshold * (1 - range_ratio) < cv2.contourArea(cnt) < area_threshold * (1 + range_ratio)]


def contour2bbox(contours: List[np.ndarray]) -> List[List[int]]:
    """윤곽선으로부터 바운딩 박스를 계산"""
    bboxs = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        bboxs.append([x, y, x+w, y+h])
    return bboxs


def crop_roi(image: np.ndarray, roi: Tuple[int, int, int, int]) -> np.ndarray:
    """이미지에서 바운딩 박스에 해당하는 영역을 잘라내어 반환"""
    x1, y1, x2, y2 = roi

    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(image.shape[1], x2)
    y2 = min(image.shape[0], y2)

    return image[y1:y2, x1:x2]


def filter_contours_by_size(contours, filtering_w, filtering_h, ratio=0.12):
    filtered_contours = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if filtering_w * (1 - ratio) <= w <= filtering_w * (1 + ratio) and filtering_h * (1 - ratio) <= h <= filtering_h * (1 + ratio):
            filtered_contours.append(contour)
    return filtered_contours


def trim_contour_line(binary_image):
    if binary_image.dtype != np.uint8:
        binary_image = cv2.convertScaleAbs(binary_image)
    kernel = np.ones((5, 5), np.uint8)
    eroded_img = cv2.erode(binary_image, kernel, iterations=1)
    dilated_img = cv2.dilate(eroded_img, kernel, iterations=1)
    clean_img = cv2.morphologyEx(dilated_img, cv2.MORPH_OPEN, kernel)

    return clean_img


def get_hsv_channel(hsv_image: np.ndarray, channel: str = 's') -> np.ndarray:
    h, s, v = cv2.split(hsv_image)
    channel = channel.lower()
    if channel == 'h':
        return h
    elif channel == 's':
        return s
    elif channel == 'v':
        return v
    else:
        raise ValueError(f"Invalid channel: {channel}. Choose 'h', 's', or 'v'.")


def adjust_channel_brightness(s_channel_image: np.ndarray, brightness_factor: float = 1.0) -> np.ndarray:
    if s_channel_image.dtype != np.uint8:
        s_channel_image = cv2.convertScaleAbs(s_channel_image)
    adjusted_image = cv2.convertScaleAbs(s_channel_image, alpha=brightness_factor)

    return adjusted_image


def apply_gamma_correction(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** invGamma * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)


def find_circle_in_mask(mask_image, dp=1.2, minDist=50, param1=100, param2=30, minRadius=10, maxRadius=100):
    blurred_mask = cv2.GaussianBlur(mask_image, (9, 9), 2)
    circles = cv2.HoughCircles(blurred_mask, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist,
                               param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    if circles is None:
        return None

    circles = np.round(circles[0, :]).astype("int")  # 원 좌표 및 반지름을 정수로 변환
    largest_circle = max(circles, key=lambda c: c[2])  # 반지름(r) 값이 가장 큰 원 선택
    x, y, r = largest_circle
    return x, y, r


def find_black_circle_in_image(image, gamma=0.5, circle_ratio=0.6, min_circle_area=150) -> Optional[Tuple[int, int, int]]:
    enhanced_image = apply_gamma_correction(image, gamma=gamma)
    blurred_image = cv2.medianBlur(enhanced_image, 5)
    _, thresh = cv2.threshold(blurred_image, 100, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        radius = int(radius)
        x, y = int(x), int(y)

        if radius == 0:
            continue

        if cv2.contourArea(contour) / (np.pi * radius ** 2) > circle_ratio:
            mask = np.zeros(image.shape, dtype=np.uint8)
            cv2.circle(mask, (x, y), radius, 255, -1)
            mean_val = cv2.mean(image, mask=mask)[0]
            if mean_val < min_circle_area:
                return int(x), int(y), int(radius)

    return None


def exclude_circle_from_mask(mask, center_x, center_y, radius):
    cv2.circle(mask, (center_x, center_y), radius, 0, -1)
    return mask


def exclude_ellipse_from_mask(mask, center_x, center_y, axis_length_x, axis_length_y, angle=0):
    cv2.ellipse(mask, (center_x, center_y), (axis_length_x, axis_length_y), angle, 0, 360, 0, -1)
    return mask


def enhance_and_find_blue_region(hsv_image, lower_blue, upper_blue):
    h, s, v = cv2.split(hsv_image)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    v_enhanced = clahe.apply(v)
    hsv_enhanced = cv2.merge([h, s, v_enhanced])
    peeling_film_mask = cv2.inRange(hsv_enhanced, lower_blue, upper_blue)
    peeling_film_mask = cv2.GaussianBlur(peeling_film_mask, (5, 5), 0)

    return peeling_film_mask


def display_bboxes_on_image(img: np.ndarray, bbox_list: list):
    img_with_bboxes = img.copy()
    for bbox in bbox_list:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(img_with_bboxes, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('bbox', img_with_bboxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def display_contour(base_img, contour, title='dis_contour'):
    cp_base_img = base_img.copy()

    if isinstance(contour, list):
        if len(contour) > 0 and isinstance(contour[0], np.ndarray):
            cv2.drawContours(cp_base_img, contour, -1, (0, 255, 0), 2)
        else:
            print("Invalid contour list format.")
    elif isinstance(contour, np.ndarray):
        cv2.drawContours(cp_base_img, [contour], -1, (0, 255, 0), 2)
    else:
        print("Invalid contour data type.")
        return
    display_image_with_safe_exit(cp_base_img, window_name=title)


def display_image_with_safe_exit(image, window_name='Image'):
    cv2.imshow(window_name, image)
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # 'q' or ESC
            break
    cv2.destroyAllWindows()


def find_contours_with_binary_inv(img: np.ndarray, threshold: int = 125) -> Tuple[np.ndarray]:
    preprocessed = get_binary_image(img, threshold, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(preprocessed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def find_contours_with_black_noise_filter(img: np.ndarray, threshold: int = 125, kernel_size: int = 5, iter_num: int = 2) -> Tuple[np.ndarray]:
    """이미지에서 윤곽선을 찾아 반환"""
    preprocessed = get_binary_image(img, threshold)
    preprocessed = filter_black_noise(preprocessed, kernel_size, iter_num)
    contours, _ = cv2.findContours(preprocessed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def filter_contours_by_wh(contours: Tuple[np.ndarray], width: int, height: int, ratio: float = 0.12):
    filtered_contours = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if width * (1 - ratio) <= w <= width * (1 + ratio) and height * (1 - ratio) <= h <= height * (1 + ratio):
            filtered_contours.append(contour)
    return filtered_contours


def calculate_contour_center(contour: np.ndarray) -> Tuple[int, int]:
    """윤곽선의 중심점을 계산"""

    M = cv2.moments(contour)
    if M["m00"] != 0:
        return (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    return None


def move_contours(contours, dx, dy):
    moved_contours = []
    for contour in contours:
        moved_contour = contour + np.array([dx, dy], dtype=np.int32)
        moved_contours.append(moved_contour)
    return moved_contours


def overlay_image(background, overlay, position):
    overlay_height, overlay_width = overlay.shape[:2]

    x, y = position
    roi = background[y:y+overlay_height, x:x+overlay_width]

    overlay_gray = cv2.cvtColor(overlay, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(overlay_gray, 1, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    background_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    overlay_fg = cv2.bitwise_and(overlay, overlay, mask=mask)

    dst = cv2.add(background_bg, overlay_fg)
    background[y:y+overlay_height, x:x+overlay_width] = dst

    return background


def calculate_rotated_angle(contour: np.ndarray) -> int:
    _, _, angle = cv2.minAreaRect(contour)
    if angle < -45:
        return int(angle + 90)
    if angle > 45:
        return int(angle - 90)
    return int(angle)


def rotate_image(image: np.ndarray, center: Tuple[int, int], angle: int, scale: float = 1.0) -> np.ndarray:
    return cv2.warpAffine(
        src=image,
        M=cv2.getRotationMatrix2D(
            center=center,
            angle=angle,
            scale=scale
        ),
        dsize=(0, 0)
    )


def shift_image(image: np.ndarray, offset_x: int, offset_y: int) -> np.ndarray:
    return cv2.warpAffine(
        src=image,
        M=np.float32([[1, 0, offset_x], [0, 1, offset_y]]),
        dsize=(0, 0)
    )


def pad_to_square(image: np.ndarray) -> np.ndarray:
    if image.shape[0] == image.shape[1]:
        return image

    h, w = image.shape[:2]
    max_length = max(h, w)
    zero_pad = np.zeros_like(image, dtype=np.uint8)
    zero_pad = cv2.resize(zero_pad, (max_length, max_length))

    x_offset = (max_length - w) // 2
    y_offset = (max_length - h) // 2

    zero_pad[y_offset:y_offset+h, x_offset:x_offset+w] = image

    return zero_pad


def calibrate_image(image: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    h, w = image.shape[:2]

    return cv2.warpPerspective(image, matrix, (w, h))


def draw_diagonal_stripes(image: np.ndarray,
                          roi: list[int],  # [x, y, w, h]
                          line_spacing: int = 10,
                          color: Tuple[int, int, int] = (255, 0, 0),
                          thickness: int = 1) -> np.ndarray:
    x, y, w, h = roi
    for i in range(0, w + h, line_spacing):
        # 우상단 -> 좌하단 방향
        start_point = (x + i, y) if i <= w else (x + w, y + (i - w))
        end_point = (x, y + i) if i <= h else (x + (i - h), y + h)
        cv2.line(image, start_point, end_point, color, thickness)

        # 좌상단 -> 우하단 방향
        # start_point = (x + w - i, y) if i <= w else (x, y + (i - w))
        # end_point = (x + w, y + i) if i <= h else (x + w - (i - h), y + h)
        # cv2.line(image, start_point, end_point, color, thickness)

    cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)

    return image.copy()


class HeatMap:
    color_degree = 255.
    vmin = 1.
    vmax = 255. * 0.4 + vmin * 0.6
    norm = colors.Normalize(vmin=vmin, vmax=vmax)
    alpha = 0.2
    isSave = False

    @classmethod
    def draw(cls, image, score_map, threshold=0.5):  # 추가: threshold 값을 설정하여 임계값 이상의 영역을 찾습니다.
        """
        * image 는 반드시 3차원 Color 이미지여야 합니다.
        """
        if len(image.shape) == 3 and image.shape[2] == 3: image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        resized_score_map = cv2.resize(score_map,
                                       dsize=(image.shape[1], image.shape[0]),
                                       interpolation=cv2.INTER_LINEAR)
        resized_score_map = resized_score_map * cls.color_degree
        norm_score_map = cv2.normalize(resized_score_map, None, alpha=0, beta=cls.color_degree, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        color_map = cv2.applyColorMap(norm_score_map, cv2.COLORMAP_JET)
        composed_img = cv2.addWeighted(image, 1 - cls.alpha, color_map, cls.alpha, 0)

        return composed_img
