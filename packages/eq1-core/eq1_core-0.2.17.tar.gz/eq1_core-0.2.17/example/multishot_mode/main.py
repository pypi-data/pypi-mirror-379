
import os


os.environ["DB_URL"] = "mysql+pymysql://crefle:passwd@localhost:3307/eq1"
os.environ["LOG_PATH"] = "./public/logs"

import cv2
import numpy as np
from typing import Optional, List
from pprint import pprint
from eq1core import (
    Core,
    AppLogger,
    SampleEngine,
    cli_command,
    InspectionMode,
    InspectionPartResultData,
    InspectionGroupResultData,
    Signal,
    DataServiceFactory
)

@cli_command("shot")
def trigger_inspection(core: Core) -> bool:
    from eq1core.lib.camera.worker import CameraHandler
    
    print("Available workers:", [type(w).__name__ for w in core._workers])
    
    for worker in core._workers:
        if isinstance(worker, CameraHandler):
            print(f"Found CameraHandler worker with camera_serial: {worker._camera_serial}")
            # CameraHandler는 request_capture 메서드 사용
            image_data = worker.request_capture()
            if image_data:
                print(f"Captured image from camera {worker.camera_number}: {image_data.image.shape if image_data.image is not None else 'None'}")
                return True
            else:
                print(f"Failed to capture image from camera {worker.camera_number}")
                return False

    print(f"NotFound CameraHandler worker")
    return False

@cli_command("next")
def next_product(core) -> bool:
    import time
    dummy_serial = f"DUMMY-SERIAL-{int(time.time()*10000)}"
    core.next_signal.emit(dummy_serial)


class MultiShotModeApp:
    # TODO : 아직 설정 로딩부 구현이 안되어있음.
    SAVE_ORIGIN_IMAGE_FLAG = True

    def __init__(self, uuid: str, group_name: str):
        self._core = Core(uuid=uuid, group_name=group_name, data_service=DataServiceFactory.get_service('db'), mode=InspectionMode.MULTI_SHOT)
        
        # 기존 register_hook 방식 대신 Signal에 핸들러 연결
        self._core.inspection_part_finished.connect(self.on_finished_inspection_part)
        self._core.inspection_group_finished.connect(self.on_finished_inspection_group)
        self._core.custom_image_save_logic.connect(self.save_image)
        
        self._core.next_signal = Signal(str)
        self._core.next_signal.connect(self.on_received_next)

        self._core.register_engine(SampleEngine)
        
        # 등록된 Signal 정보 출력
        print("=== 등록된 Signal 정보 ===")
        core_signals = []
        for attr_name in dir(self._core):
            attr_value = getattr(self._core, attr_name)
            if isinstance(attr_value, Signal):
                core_signals.append((attr_name, attr_value))
        
        for signal_name, signal in core_signals:
            print(f"  - {signal_name}: {signal}")
        print()

    def on_received_next(self, serial: str) -> bool:
        try:
            # 기존 emit 방식 대신 Signal 발생
            self._core.new_group_created.emit(serial)
            AppLogger.write_info(self, "new group event emitted successfully.", print_to_terminal=True)
            return True
        except Exception as e:
            import traceback
            AppLogger.write_error(self, f"Failed to change lot number: {e} {traceback.format_exc()}", print_to_terminal=True)
            return False

    def on_finished_inspection_part(self, *args, **kwargs):
        print("core 내부에서 inspection part 결과를 DB에 저장합니다.\n만약 추가 작업이 필요한 경우, 이곳에 정의하세요.")

    def on_finished_inspection_group(self, data: Optional[InspectionGroupResultData]):
        if data is None:
            AppLogger.write_error(self, "inspection_group_result_data is None. check your hook function.", print_to_terminal=True)
            return
        
        AppLogger.write_debug(self, f'<<<< on_finished_inspection_group\n', print_to_terminal=True)
        pprint(data)

    def save_image(self, origin_path: str, result_path: str, image: np.ndarray, roi_xywh: List[int], engine_result: object):
        AppLogger.write_info(self, f"custom image save logic: {origin_path}, {result_path}, {image}, {roi_xywh}, {engine_result.is_ok}", print_to_terminal=True)
        try:            
            origin_image = np.copy(image)
            if self.SAVE_ORIGIN_IMAGE_FLAG and not os.path.exists(origin_path):
                cv2.imwrite(origin_path, origin_image)

            x, y, w, h = roi_xywh
            result_image = np.copy(origin_image[y:y + h, x:x + w, ...])
            cv2.putText(result_image, f"{"OK" if engine_result.is_ok else "NG"}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            result_image = cv2.resize(result_image, (w // 3, h // 3))
            if not os.path.exists(result_path):
                cv2.imwrite(result_path, result_image)

            return origin_path, result_path
        except Exception as e:
            import traceback
            AppLogger.write_error(self, f"Failed to save image. {e} {traceback.format_exc()}", print_to_terminal=True)
            return "", ""
        
    def run(self):
        AppLogger.write_info(self, "Starting Multi-Shot Mode Application...", print_to_terminal=True)
        self._core.start()
        AppLogger.write_info(self, "Multi-Shot Mode Application has started.", print_to_terminal=True)


if __name__ == "__main__":
    app = MultiShotModeApp(uuid="-", group_name="MULTISHOT-PRODUCT-SAMPLE")
    app.run()