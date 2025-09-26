import asyncio
import json
import queue
import datetime
import time
from threading import Lock
from typing import List, Any, Callable, Optional
from eq1core.logger import AppLogger, log_duration

from eq1core.data import InspectionRequestData, ImageData, ProductResultCode, InspectionImageData, FrameInfo, InspectionMode, InspectionGroupResultData, InspectionPartResultData
from eq1core.frame_number import FrameNumberTrackerProducer
from eq1core.domain.services.core_data_service import CoreDataService
from eq1core.dto import InspectionPartDTO, InspectionGroupResultDTO, CameraDTO


class InspectionRequestEventListener:
    def __init__(
            self,
            uuid: str,
            wait_queue_list: List[queue.Queue],
            data_service: CoreDataService,
            on_changed_lot_number_callback_fn: Callable[[], bool] = None,
            on_changed_frame_number_callback_fn: Callable[[InspectionImageData], None] = None,
    ):
        self.uuid = uuid
        self.service = data_service
        self._wait_queue_list = wait_queue_list
        self._frame_number_tracker_producer = None
        self._on_changed_lot_number = None
        self._on_changed_frame_number = None

        self._current_group_serial: str = None

        self.cameras: List[CameraDTO] = self.service.get_active_cameras(uuid=self.uuid)

        if callable(on_changed_lot_number_callback_fn):
            self._on_changed_lot_number = on_changed_lot_number_callback_fn

        if callable(on_changed_frame_number_callback_fn):
            self._on_changed_frame_number = on_changed_frame_number_callback_fn

        if not self._init_frame_number_tracker_producer():
            raise RuntimeError('FrameNumberTrackerProducer 초기화 실패')

    def _init_frame_number_tracker_producer(self):
        try:
            if len(self.cameras) == 0:
                raise ValueError('등록된 카메라 정보가 없습니다.')

            frame_infos = []
            for camera in self.cameras:
                camera: CameraDTO
                frame_infos.append(
                    FrameInfo(
                        camera_number=camera.number,
                        number_of_frames=camera.number_of_frames
                    )
                )

            self._frame_number_tracker_producer = FrameNumberTrackerProducer(
                frame_infos=frame_infos
            )
            return True
        except Exception as e:
            import traceback
            AppLogger.write_error(self, f"FrameNumberTrackerProducer 초기화 실패 : {e}, {traceback.format_exc()}")
            return False

    @log_duration
    def on_ready(self, data: InspectionRequestData) -> InspectionGroupResultDTO:
        # TODO : skip positions 정보를 Workers 에게 전달하는 로직 추가 필요.
        try:
            if not isinstance(data, InspectionRequestData):
                raise TypeError(f'InspectionRequestEventListener > on_ready > 입력 데이터 타입이 잘못 됐습니다. expected : {InspectionRequestData} got : {type(data)}')
            AppLogger.write_debug(self, f"InspectionRequestEventListener > on_ready > input : {data}")
            for camera in self.cameras:
                self._frame_number_tracker_producer.reset_frame_number_by_camera_number(camera.number)

            last_group_result: InspectionGroupResultDTO = self.service.get_last_group_result_by_name(name=data.group_name)
            if last_group_result is None or last_group_result.is_locked == 1 or last_group_result.serial != data.group_serial:
                new_group_result = self.service.create_new_group_result(
                    name=data.group_name,
                    serial=data.group_serial,
                    started_at=datetime.datetime.now(),
                    elapsed_time_ms=int(time.time() * 1000)
                )

            self._current_group_serial = new_group_result.serial
            return new_group_result
        except Exception as e:
            import traceback
            self._current_group_serial = None
            AppLogger.write_error(self, f"inspection listener on ready error : {e}, {traceback.format_exc()}", print_to_terminal=True)

    @log_duration
    def on_request(self, data: ImageData):
        try:
            if not isinstance(data, ImageData):
                raise TypeError(f'InspectionRequestEventListener > on_request > 입력 데이터 타입이 잘못 됐습니다. expected : {ImageData} got : {type(data)}')
            AppLogger.write_debug(self, f"inspection listener on request input : {type(data)} {data.camera_number} {data.image.shape} {data.captured_at}", print_to_terminal=True)
            
            if callable(self._on_changed_lot_number) and self._on_changed_lot_number():
                AppLogger.write_debug(self, f"LOT 변경이 감지 되었습니다. frame_number 를 초기화 합니다.", print_to_terminal=True)
                for camera in self.cameras:
                    # TODO : 중복 초기화 방지를 위한 로직 보완 필요.
                    self._frame_number_tracker_producer.reset_frame_number_by_camera_number(camera.number)
            frame_number = self._frame_number_tracker_producer.increase_frame_number_by_camera_number(
                camera_number=data.camera_number
            )
            inspection_image_data = InspectionImageData(
                group_serial=self._current_group_serial,
                camera_number=data.camera_number,
                frame_number=frame_number,
                image=data.image.copy(),
                captured_at=data.captured_at,
                md_pixel_resolution_mm=data.md_pixel_resolution_mm,
                cd_pixel_resolution_mm=data.cd_pixel_resolution_mm
            )
            if callable(self._on_changed_frame_number):
                self._on_changed_frame_number(inspection_image_data)
            for wait_queue in self._wait_queue_list:
                wait_queue.put(inspection_image_data)
        except Exception as e:
            import traceback
            AppLogger.write_error(self, f"inspection listener on request error : {e}, {traceback.format_exc()}", print_to_terminal=True)

    def on_failed(self, camera_number: int):
        try:
            self._frame_number_tracker_producer.reset_frame_number_by_camera_number(camera_number)
        except Exception as e:
            import traceback
            AppLogger.write_error(self, f"inspection listener on failed error : {e}, {traceback.format_exc()}")


class InspectionResultEventListener:
    """
    검사 완료 이벤트 처리 객체
    
    현재 컨셉상 Group Result 는 동시에 두 개 이상 존재할 수 없습니다.

    여러 Group 동시 처리가 필요한 경우, 코드 수정이 필요합니다.
    """
    def __init__(self,
                 uuid: str,
                 data_service: CoreDataService,
                 inspection_group_finished_callback_fn: Callable[[InspectionGroupResultData], None] = None,
                 inspection_part_finished_callback_fn: Callable[[InspectionPartResultData], None] = None,
                 one_frame_finished_callback_fn: callable = None,
                 inspection_mode: InspectionMode = None,
                 async_lock: Lock = None):
        self.uuid = uuid
        self._inspection_group_finished_callback_fn = inspection_group_finished_callback_fn
        self._inspection_part_finished_callback_fn = inspection_part_finished_callback_fn
        self._one_frame_finished_callback_fn = one_frame_finished_callback_fn
        self._inspection_mode = inspection_mode
        self._async_lock = async_lock

        self.service = data_service

        if self._inspection_mode is None:
            raise ValueError("InspectionMode is required for InspectionResultEventListener")
        
        self._inspection_parts: List[InspectionPartDTO] = self.service.get_active_inspection_parts(uuid=self.uuid)
        self._inspection_part_results: List[InspectionPartResultData] = []

        self._is_infinite_mode = self._inspection_mode in [InspectionMode.CONTINUOUS]

    def clear(self):
        self._inspection_part_results.clear()

    def is_frame_finished(self,
                          camera_number: int,
                          frame_number: int) -> bool:

        frame_inspection_parts = []
        for inspection_part in self._inspection_parts:
            if inspection_part.camera_number == camera_number:
                if inspection_part.frame_number == frame_number or inspection_part.frame_number == -1:
                    frame_inspection_parts.append(inspection_part)
        
        frame_inspection_parts_results = []
        for inspection_part_result in self._inspection_part_results:
            if inspection_part_result.camera_number == camera_number:
                if inspection_part_result.frame_number == frame_number or inspection_part_result.frame_number == -1:
                    frame_inspection_parts_results.append(inspection_part_result)

        number_of_frame_inspection_parts = len(frame_inspection_parts)
        number_of_frame_inspection_parts_results = len(frame_inspection_parts_results)
        
        print('>> number_of_frame_inspection_parts', number_of_frame_inspection_parts, 'number_of_frame_inspection_parts_results', number_of_frame_inspection_parts_results)
        return number_of_frame_inspection_parts == number_of_frame_inspection_parts_results

    def on_frame_finished(self, camera_number: int, frame_number: int):
        if callable(self._one_frame_finished_callback_fn):
            inspection_part_results: List[InspectionPartResultData] = []
            for inspection_part_result in self._inspection_part_results:
                if inspection_part_result.camera_number == camera_number:
                    if inspection_part_result.frame_number == frame_number or inspection_part_result.frame_number == -1:
                        inspection_part_results.append(inspection_part_result)

            self._one_frame_finished_callback_fn(inspection_part_results)
                
    def determine_group_result_code(self, results: List[InspectionPartResultData]) -> ProductResultCode:
        for result in results:
            if result.result.lower() != 'ok':
                return ProductResultCode.NG

        return ProductResultCode.OK
    
    def is_group_finished(self) -> bool:
        return len(self._inspection_parts) == len(self._inspection_part_results)

    def on_group_finished(self, serial: str):  # TODO : 해당 함수도 바깥 콜백으로 옮기는게 맞을지 고민.
        group_result: Optional[InspectionGroupResultDTO] = self.service.get_group_result_by_serial(serial=serial)
        AppLogger.write_debug(self, f"Inspection Group Completed. group_name: {group_result.name}, group_serial: {group_result.serial}", print_to_terminal=True)
        
        is_updated = False
        if self._async_lock is not None:
            self._async_lock.acquire()
        try:
            if group_result.elapsed_time_ms is None:
                AppLogger.write_debug(self, f"elapsed_time_ms의 시작이 기록되지 않았습니다. elapsed_time_ms를 0으로 처리합니다.", print_to_terminal=True)
                elapsed_time_ms = 0
            else:
                """
                group_result.elapsed_time_ms == def on_ready 에서 생선될 시점의 int(time.time()*1000) 값
                """
                elapsed_time_ms = int(time.time() * 1000) - group_result.elapsed_time_ms
    
            if group_result.is_locked == 0:
                group_result_dto: InspectionGroupResultDTO = self.service.set_group_result_as_finished(
                    serial=group_result.serial,
                    result_code=self.determine_group_result_code(self._inspection_part_results),
                    finished_at=datetime.datetime.now(),
                    is_locked=1,
                    elapsed_time_ms=elapsed_time_ms
                )
                is_updated = True
        except Exception as e:
            import traceback
            AppLogger.write_error("failed to update product result", traceback.format_exc(), print_to_terminal=True)
        finally:
            if self._async_lock is not None:
                self._async_lock.release()
    
        if is_updated and callable(self._inspection_group_finished_callback_fn):
            self._inspection_group_finished_callback_fn(
                InspectionGroupResultData(
                    name=group_result_dto.name,
                    serial=group_result_dto.serial,
                    result_code=group_result_dto.result,
                    started_at=group_result_dto.started_at,
                    finished_at=group_result_dto.finished_at,
                    elapsed_time_ms=group_result_dto.elapsed_time_ms,
                    is_locked=group_result_dto.is_locked,
                    number_of_inspection_parts=len(self._inspection_parts),
                    number_of_completed_parts=len(self._inspection_part_results),
                    completed_parts=self._inspection_part_results
                )
            )
        self.clear()

    def on_finished(self, data: InspectionPartResultData):
        try:
            if not isinstance(data, InspectionPartResultData):
                raise TypeError(f'InspectionResultEventListener > on_finished > 입력 데이터 타입이 잘못 됐습니다. expected : {InspectionPartResultData} got : {type(data)}')

            AppLogger.write_debug(self, f"inspection listener on finished input : inspection_part {data.part_name}, camera_number: {data.camera_number}, frame_number: {data.frame_number}, started_at: {data.started_at}, finished_at: {data.finished_at}, result: {data.result}, elapsed_time_ms: {data.elapsed_time_ms}, origin_image_path: {data.origin_image_path}, result_image_path: {data.result_image_path}")

            # TODO : Product Result 가 잠겨있는 경우, 자동발급 옵션 적용.
            group_result: Optional[InspectionGroupResultDTO] = self.service.get_group_result_by_serial(serial=data.group_serial)
            if group_result is None or group_result.is_locked == 1 or group_result.started_at > data.captured_at:
                AppLogger.write_error(self, f'group name {data.group_name} 와 일치하는 그룹 결과 정보가 없거나 이미 잠겨있습니다. 그룹 결과가 제대로 생성되지 않았거나 잘못된 그룹 이름 일 수 있습니다.', print_to_terminal=True)
                self._inspection_part_results.clear()
                return
            
            if group_result.serial != data.group_serial:
                AppLogger.write_error(self, f'마지막 group result의 serial 값이 현재 part result 의 group_serial 값과 다릅니다. group_serial: {group_result.serial}, group_result.serial: {data.group_serial}', print_to_terminal=True)
                self._inspection_part_results.clear()
                return
            
            if data.frame_number == -1:
                data.part_name += f'_f#{data.frame_number}'
            
            if not self._is_infinite_mode:
                if data.part_name not in [inspection_part_result.part_name for inspection_part_result in self._inspection_part_results]:
                    self._inspection_part_results.append(data)
                else:
                    AppLogger.write_error(self, f'inspection part {data.part_name} 이 이미 존재합니다. 중복 검사 결과가 생성되었습니다.', print_to_terminal=True)
            else:
                # 무한 모드에서는 중복 체크 없이 추가하고, 최근 100개만 유지
                self._inspection_part_results.append(data)
                if len(self._inspection_part_results) > 100:
                    # 오래된 결과부터 제거 (FIFO 방식)
                    self._inspection_part_results.pop(0)

            if callable(self._inspection_part_finished_callback_fn):
                self._inspection_part_finished_callback_fn(data)

            if not self._is_infinite_mode:
                """
                아래 로직은 한독 프로젝트와 같이 라인스캔 검사방식의 무한 프레임에서는 의미 없는 로직입니다.
                """
                if self.is_frame_finished(camera_number=data.camera_number, frame_number=data.frame_number):
                    self.on_frame_finished(camera_number=data.camera_number, frame_number=data.frame_number)
                
                AppLogger.write_debug(self, f"검사 진행율 ... {len(self._inspection_part_results)} / {len(self._inspection_parts)}", print_to_terminal=True)
                if self.is_group_finished():
                    self.on_group_finished(serial=group_result.serial)

        except Exception as e:
            import traceback
            AppLogger.write_error(self, f"inspection listener on finished error : {e}, {traceback.format_exc()}", print_to_terminal=True)
