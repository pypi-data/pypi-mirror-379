import cv2
import numpy as np
import time
import queue
import threading
import traceback
from typing import List, Callable
from datetime import datetime
from eq1core.engines.interface import BaseEngine
from eq1core.data import InspectionImageData, EngineResult, InspectionPartResultData
from eq1core.dto import InspectionPartDTO
from eq1core.utils import crop_image
from eq1core.logger import AppLogger


class InspectionWorker(threading.Thread):
    def __init__(self, inspection_parts: List[InspectionPartDTO],
                 engine: BaseEngine,
                 wait_queue: queue.Queue[InspectionImageData],
                 on_finished_fn: Callable[[InspectionPartResultData], None],
                 on_save_image_fn: Callable):
        """
        :param components: Inspection Worker 가 사용하는 Vision Engine 에 속한 검사항목 리스트
        :param engine: Inspection Worker 가 사용하는 핵심 검사 로직을 담은 객체
        :param wait_queue: ImageData 를 기다리는 Queue
        :param on_finished_fn: 검사 결과가 나왔을 때 호출되는 콜백 함수
        """
        super().__init__()

        self._inspection_parts = inspection_parts
        self._engine = engine
        self._queue = wait_queue
        self._on_finished_fn = on_finished_fn
        self._on_save_image_fn = on_save_image_fn
        self._stop_flag = threading.Event()

        self._inspection_parts_dict = self.set_inspection_parts_as_dict()
        
    def set_inspection_parts_as_dict(self) -> dict[int, dict[int, List[InspectionPartDTO]]]:
        self._inspection_parts_dict = {}
        for inspection_part in self._inspection_parts:
            if inspection_part.camera_number not in self._inspection_parts_dict:
                self._inspection_parts_dict[inspection_part.camera_number] = {}
            if inspection_part.frame_number not in self._inspection_parts_dict[inspection_part.camera_number]:
                self._inspection_parts_dict[inspection_part.camera_number][inspection_part.frame_number] = []
            self._inspection_parts_dict[inspection_part.camera_number][inspection_part.frame_number].append(inspection_part)
        return self._inspection_parts_dict

    def get_inspection_parts_by_camera_number_and_frame_number(self, camera_number: int, frame_number: int) -> List[InspectionPartDTO]:
            try:
                return self._inspection_parts_dict[camera_number][frame_number]
            except Exception as e:
                """
                검사엔진 기준으로 생성된 inspection parts 에는 해당 카메라 번호와 프레임 번호가 없을 수 있기 때문에 빈 값을 반환함.
                """ 
                return []

    def stop(self):
        self._stop_flag.set()

    def run(self):
        if len(self._inspection_parts) == 0:
            AppLogger.write_info(self, f'{self._engine} 의 _inspection_parts 가 비어있습니다. DB 설정을 확인해주세요.', print_to_terminal=True)

        self._stop_flag.clear()
        while not self._stop_flag.is_set():
            try:
                time.sleep(0.001)
                if self._queue.empty():
                    continue

                data = self._queue.get()
                if not isinstance(data, InspectionImageData):
                    raise TypeError('ImageData 타입이 아닙니다.')

                selected_inspection_parts = self.get_inspection_parts_by_camera_number_and_frame_number(data.camera_number, data.frame_number)
                if len(selected_inspection_parts) == 0:
                    continue

                for inspection_part in selected_inspection_parts:
                    inspection_part: InspectionPartDTO
                    started_at = datetime.now()
                    try:
                        roi_image = crop_image(
                            image=data.image,
                            roi_xywh=inspection_part.roi_xywh)
                        is_ok, result = self._engine.get_results(roi_image)  # TODO : 추후 성능 개선을 위하여 배치 처리로 변경될 수 있음.

                        """ 2025.01.08, hyeseong
                        pixel resolution 정보가 engine config 에서 camera config 로 이전 됨에 따라 
                        bboxes with mm unit 을 엔진 내에서 만들지 않고 한 단계 상위로 이동 시킴. 
                        """
                        # bboxes_with_mm_unit = []
                        # for bbox in result.bboxes_with_pixel_unit:
                        #     _x, _y, _w, _h = bbox
                        #     bboxes_with_mm_unit.append((round(_x * data.cd_pixel_resolution_mm, 2),
                        #                                 round(_y * data.md_pixel_resolution_mm, 2),
                        #                                 round(_w * data.cd_pixel_resolution_mm, 2),
                        #                                 round(_h * data.md_pixel_resolution_mm, 2)))

                        # result.bboxes_with_mm_unit = bboxes_with_mm_unit
                    except Exception as e:
                        AppLogger.write_error(self, traceback.format_exc(), print_to_terminal=True)
                        result = EngineResult(
                            is_ok=False,
                            is_failed=True,
                            base_engine_name=inspection_part.name
                        )

                        is_ok = False

                    finally:
                        finished_at = datetime.now()

                    origin_image_path, result_image_path = None, None
                    if callable(self._on_save_image_fn):
                        origin_image_path, result_image_path = self._on_save_image_fn(inspection_image=data,
                                                                                      inspection_part=inspection_part,
                                                                                      inspection_result=result)

                    if callable(self._on_finished_fn):
                        self._on_finished_fn(
                            InspectionPartResultData(
                                group_name=inspection_part.group.name,
                                group_serial=data.group_serial,
                                part_name=inspection_part.name,
                                engine_name=inspection_part.engine_name,
                                roi_xywh=inspection_part.roi_xywh,
                                camera_number=data.camera_number,
                                frame_number=data.frame_number,
                                started_at=started_at,
                                finished_at=finished_at,
                                captured_at=data.captured_at,
                                elapsed_time_ms=int((finished_at-started_at).total_seconds() * 1000),
                                result='ok' if is_ok else 'ng',
                                detail=result,
                                origin_image_path=origin_image_path,
                                result_image_path=result_image_path
                            )
                        )
                    AppLogger.write_debug(self, f"Finished Inspection. engine {self._engine}, is_ok {is_ok}")

            except Exception as e:
                AppLogger.write_error(self, f"InspectionWorker Error: {e}, {traceback.format_exc()}", print_to_terminal=True)
