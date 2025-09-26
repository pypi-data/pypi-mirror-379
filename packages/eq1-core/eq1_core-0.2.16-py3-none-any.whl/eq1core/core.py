"""
MEMO : 설정에서 줄 수 있는 것들 정리..

- 검사 모드 : 
    - Single : 단일 제품 단일 촬영
    - Multi : 단일 제품 다중 촬영
    - Continuous : 제품 구분 없이 연속 촬영
- 검사 결과 중복 허용 : Product Result 를 중복 생성을 허용할 건지? 아니면 단일 생성만 허용할지?
- DB Async Writer 사용 여부 : 고속/연속 프레임 검사에서 쓰기 작업 과부하로 프로그램 속도 저하 문제가 발생함에 따라 bulk 쓰기 작업을 별도의 쓰레드로 분리할 것인지 여부.

"""

import os
import sys
import time
import queue
import traceback
import threading
import numpy as np
from typing import Tuple, List, Optional, Dict, Any, Callable, Type
from .logger import AppLogger
from .engines.factory import EngineFactory
from .engines.interface import BaseEngine
from .predictors.factory import PredictorFactory
from .predictors.interface import BasePredictor
from .dto import CameraDTO, VisionEngineDTO, PredictorDTO, InspectionPartDTO, InspectionGroupResultDTO
from .data import CameraPixelInfo, LotInfo, InspectionRequestData, InspectionMode, InspectionPartResultData, InspectionGroupResultData, InspectionImageData, EngineResult
from .utils import DBAsyncWriter
from .inspection.worker import InspectionWorker
from .inspection.event_listener import InspectionRequestEventListener, InspectionResultEventListener
from .lib.camera.worker import CameraHandler
from .lib.camera.frame_grabber.worker import ImageGrabber
from .signal import Signal, global_signal_emitter
from .decorators import REGISTRY
from .domain.services.core_data_service import CoreDataService


class Core:

    # TODO : 추후 SettingDataService 추가 시 설정 값을 사용할 것..
    ORIGIN_IMAGE_ROOT = './public/output/origin'
    RESULT_IMAGE_ROOT = './public/output/result'
    
    # TODO : 추후 불필요한 시그널은 삭제할 것.
    inspection_part_finished = Signal(InspectionPartResultData)
    inspection_group_finished = Signal(InspectionGroupResultData)
    one_frame_finished = Signal(list)
    lot_changed = Signal()
    new_group_created = Signal()
    camera_error = Signal(str)
    system_error = Signal(str)
    status_changed = Signal(str)
    inspection_part_result_enqueue_requested = Signal(InspectionPartResultData)
    custom_image_save_logic = Signal(str, str, np.ndarray, list, object)
    
    def __init__(self, uuid: str, group_name: str, data_service: CoreDataService, mode: InspectionMode = InspectionMode.MULTI_SHOT):
        if mode == InspectionMode.CONTINUOUS:  # TODO : 카메라 라이브러리 정리 필요. 에어리어와 라인스캔 호환.
            from .lib.camera.frame_grabber.worker import ImageGrabber as CameraWorker
        else:
            from .lib.camera.worker import CameraHandler as CameraWorker
        
        self._camera_worker_class = CameraWorker
            
        self.service = data_service
        
        self.stop_flag: bool = False
        self._current_lot_number: Optional[int] = None
        self.uuid: str = uuid
        self._group_name: str = group_name
        self._mode: InspectionMode = mode

        self._engine_factory = EngineFactory()
        self._predictor_factory = PredictorFactory()

        self.inspection_request_event_listener: Optional[InspectionRequestEventListener] = None
        self.inspection_result_event_listener: Optional[InspectionResultEventListener] = None

        self._workers: List[Any] = []
        self._plugins: List[Any] = []
        
        # 사용자 정의 Signal은 global_signal_emitter를 통해 관리
        self._cli_command_handlers: Dict[str, Callable] = {}
        
        # 기본 Signal 핸들러들 등록
        self._connect_default_signal_handlers()

    @property
    def group_name(self) -> str:
        return self._group_name
    
    @property
    def uuid(self) -> str:
        return self._uuid
    
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value

    @group_name.setter
    def group_name(self, value: str):
        self._group_name = value
    
    def _connect_default_signal_handlers(self):
        """기본 Signal 핸들러들 연결"""
        # 검사 완료 시그널들
        self.inspection_part_finished.connect(self._default_on_inspection_part_finished)
        self.inspection_group_finished.connect(self._default_on_inspection_group_finished)
        self.one_frame_finished.connect(self._default_on_one_frame_finished)
        
        # 시스템 시그널들
        self.lot_changed.connect(self.change_lot_number)
        self.new_group_created.connect(self.create_group_result)
        self.camera_error.connect(self._default_on_camera_error)
        self.system_error.connect(self._default_on_system_error)
        self.status_changed.connect(self._default_on_status_changed)
        
        AppLogger.write_debug(self, "Default signal handlers connected", print_to_terminal=True)

    def get_all_custom_signals(self) -> Dict[str, Signal]:
        """모든 사용자 정의 Signal 조회"""
        return global_signal_emitter.get_all_signals()

    def __setattr__(self, name: str, value):
        """속성 설정 시 Signal 타입인 경우 특별 처리"""
        if isinstance(value, Signal):
            # Signal을 core 인스턴스에 직접 추가
            self.__dict__[name] = value
        else:
            # 일반 속성은 기본 방식으로 설정
            super().__setattr__(name, value)

    def __getattr__(self, name: str):
        """동적 속성 접근을 통해 custom signal에 접근할 수 있도록 함"""
        # core 인스턴스에 직접 추가된 signal인지 확인
        if name in self.__dict__ and isinstance(self.__dict__[name], Signal):
            return self.__dict__[name]
        
        # global_signal_emitter의 custom signal인지 확인
        custom_signal = global_signal_emitter.get_signal(name)
        if custom_signal:
            return custom_signal
        
        # 기본 속성 접근으로 위임
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __hasattr__(self, name: str) -> bool:
        """속성 존재 여부 확인 (custom signal 포함)"""
        # 기본 속성 확인
        if hasattr(self.__class__, name) or name in self.__dict__:
            return True
        
        # core 인스턴스에 직접 추가된 signal 확인
        if name in self.__dict__ and isinstance(self.__dict__[name], Signal):
            return True
        
        # global_signal_emitter의 custom signal 확인
        return global_signal_emitter.get_signal(name) is not None

    def register_engine(self, engine_class: Type[BaseEngine]) -> None:
        self._engine_factory.register_engine(engine_class)

    def get_registered_engines(self) -> list[str]:
        return self._engine_factory.get_registered_engines()

    def create_engine(self, data: VisionEngineDTO) -> BaseEngine:
        return self._engine_factory.create_engine(data)

    def register_predictor(self, name: str, predictor_class: Type[BasePredictor]) -> None:
        self._predictor_factory.register_predictor(name, predictor_class)

    def get_registered_predictors(self) -> list[str]:
        return self._predictor_factory.get_registered_predictors()

    def create_predictor(self, data: PredictorDTO) -> BasePredictor:
        return self._predictor_factory.create_predictor(data)

    def _default_on_inspection_part_finished(self, data: Optional[InspectionPartResultData]):
        try:
            if data is None:
                AppLogger.write_error(self, "inspection_part_result_data is None. check your hook function.", print_to_terminal=True)
                return

            AppLogger.write_debug(self, 
                                  f'\n>>>> on_finished_inspection_part. cam #: {data.camera_number} _ frame #: {data.frame_number} _ "{data.part_name}" _ "{data.result}"',
                                  print_to_terminal=True)

            data.roi_xywh = ",".join(map(str, data.roi_xywh))  # TODO : roi xywh 를 str 로 저장해야하기 때문에 임시로 추가함.
            self.inspection_part_result_enqueue_requested.emit(data)
            AppLogger.write_info(self, "inspection part result enqueue requested successfully.", print_to_terminal=True)            
        except Exception as e:
            import traceback
            AppLogger.write_error(
                self, f'failed to on_finished_inspection_part as {e} {traceback.format_exc()}', print_to_terminal=True)
        
    def _default_on_inspection_group_finished(self, data: InspectionGroupResultData):
        AppLogger.write_debug(self, f'Inspection Group finished: {data.name} - {data.result_code}', print_to_terminal=True)

    def _default_on_one_frame_finished(self, data: List[InspectionPartResultData]):
        AppLogger.write_debug(self, f'Frame finished: {len(data)} components', print_to_terminal=True)

    def _default_on_camera_error(self, error_msg: str):
        AppLogger.write_error(self, f'Camera error: {error_msg}', print_to_terminal=True)

    def _default_on_system_error(self, error_msg: str):
        AppLogger.write_error(self, f'System error: {error_msg}', print_to_terminal=True)

    def _default_on_status_changed(self, status: str):
        AppLogger.write_info(self, f'Status changed: {status}', print_to_terminal=True)

    # InspectionResultEventListener에 전달할 콜백들 (기본 Signal 사용)
    def on_finished_inspection_part(self, *args, **kwargs):
        self.inspection_part_finished.emit(*args, **kwargs)

    def on_finished_inspection_group(self, *args, **kwargs):
        self.inspection_group_finished.emit(*args, **kwargs)

    def on_finished_one_frame_inspection(self, *args, **kwargs):
        self.one_frame_finished.emit(*args, **kwargs)

    def init_workers(self):
        self.init_inspection_workers()
        self.init_async_db_writer()
        # InspectionRequestEventListener가 생성된 후에 카메라 초기화
        if hasattr(self, 'inspection_request_event_listener'):
            self.init_cameras(
                on_captured_fn=self.inspection_request_event_listener.on_request
            )
        else:
            AppLogger.write_error(self, "InspectionRequestEventListener가 생성되지 않았습니다.", print_to_terminal=True)

    def start_workers(self):
        for worker in self._workers:
            worker.start()

    def stop_workers(self):
        for worker in self._workers:
            try:
                worker.stop()
            except Exception as e:
                print(f"Failed to stop worker. {e}")

        for worker in self._workers:
            try:
                worker.join()
            except Exception as e:
                print(f"Failed to join worker. {e}")

        self._workers = []

    def start_plugins(self):
        for plugin in self._plugins:
            plugin.start()

    def stop_plugins(self):
        for plugin in self._plugins:
            plugin.stop()

    def init_async_db_writer(self):
        part_result_async_writer = DBAsyncWriter(self.service.save_inspection_part_results)
        self._workers.append(part_result_async_writer)
        
        # inspection_part_result_enqueue_requested 시그널을 DBAsyncWriter에 연결
        # bulk save 를 위한 시그널 연결
        self.inspection_part_result_enqueue_requested.connect(part_result_async_writer.put)
        AppLogger.write_debug(self, "inspection_part_result_enqueue_requested 시그널이 DBAsyncWriter에 연결되었습니다.", print_to_terminal=True)

    def init_inspection_workers(self):
        wait_queues = []

        try:
            self.inspection_result_event_listener = InspectionResultEventListener(
                uuid=self.uuid,
                data_service=self.service,
                inspection_group_finished_callback_fn=self.on_finished_inspection_group,
                inspection_part_finished_callback_fn=self.on_finished_inspection_part,
                one_frame_finished_callback_fn=self.on_finished_one_frame_inspection,
                inspection_mode=self._mode,
                async_lock=threading.Lock()
            )

            active_engines = self.service.get_active_engines(uuid=self.uuid)
            for engine_dto in active_engines:
                engine_dto: VisionEngineDTO

                if engine_dto.predictor is not None:
                    self.create_predictor(data=engine_dto.predictor) # <<< 

                inspection_parts: List[InspectionPartDTO] = self.service.get_active_inspection_parts_by_engine_name(name=engine_dto.name)
                
                wait_queue = queue.Queue()
                engine: BaseEngine = self.create_engine(data=engine_dto)
                worker = InspectionWorker(
                    inspection_parts=inspection_parts,
                    engine=engine,
                    wait_queue=wait_queue,
                    on_finished_fn=self.inspection_result_event_listener.on_finished,
                    on_save_image_fn=self.on_requested_save_image
                )
                self._workers.append(worker)
                AppLogger.write_debug(self, f"inspection worker created : {engine_dto.name} {len(inspection_parts)}", print_to_terminal=True)
                wait_queues.append(wait_queue)

        except Exception as e:
            AppLogger.write_error(self, f"Failed to initialize inspection workers. {e} {traceback.format_exc()}", print_to_terminal=True)

        finally:
            self.inspection_request_event_listener = InspectionRequestEventListener(
                uuid=self.uuid,
                wait_queue_list=wait_queues,
                # on_changed_lot_number_callback_fn=self.on_changed_lot_number,  # 이벤트 리스너에 직접 콜백 던지던 부분이 있는데.. 어떻게 처리할지 고민 중...
                # on_changed_frame_number_callback_fn=self.on_changed_frame_number,
                data_service=self.service,
            )

    def init_cameras(self, on_captured_fn: callable):
        try:
            cameras = self.service.get_active_cameras(uuid=self.uuid)
            if len(cameras) == 0:
                raise Exception("There is no camera to initialize. Please check the camera configuration.")

            for camera in cameras:
                camera: CameraDTO
                camera_worker = self._camera_worker_class(  # TODO : Area 카메라와 LineScan 카메라의 Worker가 분리되어 있음.. 하나로 합치거나 인터페이스를 통일할 필요가 있음..
                    camera_dto=camera,
                    callback_fn=on_captured_fn
                )
                self._workers.append(camera_worker)
        except Exception as e:
            AppLogger.write_error(self, f"Failed to initialize cameras. {e} {traceback.format_exc()}", print_to_terminal=True)

    def log_current_camera_status(self):
        for worker in self._workers:
            if not isinstance(worker, self._camera_worker_class):
                continue
            worker.check_status()

    def register_plugin(self, plugin):
        """
        EqPlugin 을 상속받은 객체를 등록하고 초기화합니다.
        """
        if hasattr(plugin, 'register'):
            plugin.register(self)
            self._plugins.append(plugin)
        else:
            raise TypeError(f"{plugin} 은 register 메서드를 가진 유효한 Plugin이 아닙니다.")

    def unregister_all_plugins(self):
        """
        종료 시 모든 플러그인을 해제
        """
        for plugin in self._plugins:
            if hasattr(plugin, 'unregister'):
                plugin.unregister()
        self._plugins.clear()

    def show_description(self):
        default_commands = [
            "exit",
            "help",
            "h",
            "q",
            "cli"
        ]
        description = "[EQ1Core] Available commands:\n"
        for cmd in default_commands:
            description += f"- {cmd}\n"
        description += "\nRegistered CLI commands:\n"
        for name in REGISTRY["cli_commands"].keys():
            description += f"- {name}\n"
        AppLogger.write_info(self, description, print_to_terminal=True) 
        
    def _load_cli_commands(self):
        for name, handler in REGISTRY["cli_commands"].items():
            self._cli_command_handlers[name] = handler

    def _run_cli_loop(self):
        while True:
            time.sleep(0.001)
            if not sys.stdin.isatty():
                return
            try:
                cmd = input("> ").strip()  # TODO : EOF 처리 필요.
                if cmd in ["exit", "q"]:
                    print("[EQ1Core] Exiting...")
                    self.stop()
                    break
                elif cmd in ["help", "h"]:
                    self.show_description()
                elif cmd in self._cli_command_handlers:
                    self._cli_command_handlers[cmd](self)
                else:
                    print(f"[EQ1Core] Unknown command: {cmd}")
            except KeyboardInterrupt:
                print("\n[EQ1Core] Exiting...")
                self.stop()
                break
            except Exception as e:
                print(f"[EQ1Core] Error: {e}")
                traceback.print_exc()

    def start(self):
        AppLogger.write_info(self, f'Main Process was successfully started. ({os.path.abspath(__file__)})\n', print_to_terminal=True)
        self.stop_flag = False
        self.init_workers()
        self.start_workers()
        self.start_plugins()

        self.show_description()
        self._load_cli_commands()
        self._run_cli_loop()

    def stop(self):
        self.stop_flag = True
        
        self.stop_workers()
        self.stop_plugins()
        self.unregister_all_plugins()

    def on_requested_save_image(self, inspection_image: InspectionImageData,
                                inspection_part: InspectionPartDTO,
                                inspection_result: EngineResult) -> Tuple[str, str]:

        result_suffix = "_ok.png" if inspection_result.is_ok else "_ng.png"

        def get_save_dir(root_dir: str) -> str:
            from datetime import datetime
            root_dir = os.path.abspath(root_dir)
            save_dir = os.path.join(root_dir,
                                    datetime.now().strftime('%Y%m%d'),
                                    f"{inspection_image.group_serial.replace('/', '-')}")
            if not os.path.exists(save_dir):
                os.makedirs(save_dir, exist_ok=True)

            return save_dir
        
        try:
            origin_dir: str = get_save_dir(self.ORIGIN_IMAGE_ROOT)
            result_dir: str = get_save_dir(self.RESULT_IMAGE_ROOT)

            origin_path =  os.path.join(origin_dir, inspection_image.get_filename()+".bmp")
            result_path =  os.path.join(result_dir, inspection_image.get_filename().split('.')[0] + "_" + inspection_part.name + result_suffix)

            image: np.ndarray = inspection_image.image
            roi_xywh: List[int] = inspection_part.roi_xywh
            engine_result: EngineResult = inspection_result

            self.custom_image_save_logic.emit(origin_path, result_path, image, roi_xywh, engine_result)
            
            return origin_path, result_path
        except Exception as e:
            AppLogger.write_error(
                self, f"Failed to save images. {e} {traceback.format_exc()}", print_to_terminal=True)
            return "", ""

    def get_camera_pixel_info(self, camera_number: int) -> Optional[CameraPixelInfo]:
        """특정 카메라의 픽셀 해상도 정보 반환"""
        try:
            for worker in self._workers:
                if not isinstance(worker, self._camera_worker_class):
                    continue
                if worker.camera_number != camera_number:
                    continue
                
                return CameraPixelInfo(
                    md_pixel_resolution_mm=worker.md_pixel_resolution_mm,
                    cd_pixel_resolution_mm=worker.cd_pixel_resolution_mm,
                    frame_md_pixel_size=worker.md_pixel
                )
            
            AppLogger.write_warning(self, f"Camera {camera_number} not found", print_to_terminal=True)
            return None
            
        except Exception as e:
            AppLogger.write_error(self, f"Failed to get camera pixel info for camera {camera_number}: {e}", print_to_terminal=True)
            return None

    def change_lot_number(self) -> bool:
        try:
            new_lot_number = self.create_group_result()
            for worker in self._workers:
                if not isinstance(worker, self._camera_worker_class):
                    continue
                worker.clear_frame_buffer()
            self._current_lot_number = new_lot_number
            return True
        except Exception as e:
            AppLogger.write_error(self, f"Failed to change lot number: {e} {traceback.format_exc()}", print_to_terminal=True)
            return False

    def auto_generate_serial(self, group_name: str) -> str:
        """
        serial 을 자동으로 생성하는 함수입니다.
        일반적으로 product serial 을 외부에서 입력받아야하지만, 제품별 시리얼을 구분하지 않는 경우에 사용합니다.
        serial 을 자동으로 생성하여 제품결과가 고유한 시리얼을 가지도록 합니다.
        단, 해당 제품결과가 비어있는 경우에는 serial을 새로 생성하지 않습니다.
        """
        group_serial: str = self.service.get_last_group_serial(group_name=group_name)
        if LotInfo.is_valid_serial_format(group_serial):
            lot_info = LotInfo.from_serial(group_serial)
            if not self.service.is_group_result_empty(group_name):
                lot_info = lot_info.next()
        else:
            lot_info = LotInfo.new()

        return lot_info.to_serial()
        
    def create_group_result(self, serial: str = None) -> str:
        AppLogger.write_debug(self, f"Creating group result >  name : {self._group_name} > serial: {serial}", print_to_terminal=True)
        
        # TODO : mode 별로 다르게 처리할 것. lot 자동 증가 모드에서는 serial 을 자동생성한 Lot 로 처리. 이외에는 Serial을 입력받아서 사용해야함.
        if serial is None:
            serial = self.auto_generate_serial(self._group_name)
        
        res: bool = self.service.set_unlocked_group_results_as_failed(
            group_name=self._group_name,
            serial=serial
        )
        if not res:
            raise Exception("Failed to 'set unlocked group results as failed'")

        if not isinstance(self.inspection_result_event_listener, InspectionResultEventListener):
            raise Exception("event_listener is not instance of InspectionResultEventListener")

        self.inspection_result_event_listener.clear()

        if not isinstance(self.inspection_request_event_listener, InspectionRequestEventListener):
            raise Exception("event_listener is not instance of InspectionRequestEventListener")

        inspection_group_result_dto: InspectionGroupResultDTO = self.inspection_request_event_listener.on_ready(
            data=InspectionRequestData(
                group_name=self._group_name,
                group_serial=serial,
            )
        )

        return serial
        