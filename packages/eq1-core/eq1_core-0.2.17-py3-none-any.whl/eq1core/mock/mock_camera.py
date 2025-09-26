import os
import cv2
import numpy as np
import traceback
from eq1core.lib.camera.interface import CameraInterface


class MockCamera(CameraInterface):
    BUFFER_PATH = '/tmp/mock_camera_buffer'

    def __init__(self, serial: str = None, interface_type: str = None):
        self._serial = serial
        self._interface_type = interface_type
        print("\nCamera was initialized with mock camera"
              "\nIf you want to test get frame, "
              f"\nput the image file in {self.BUFFER_PATH}/{serial}.bmp"
              "\nthe serial is the camera serial number.\n")

    @classmethod
    def create(cls, 
               serial: str,
               interface_type: str = "usb",
               exposure_time: float = 30000,
               gain_db: float = 0.0,
               timeout: float = 1000,
               trigger_mode: str = "on",
               trigger_source: str = "sw",
               trigger_delay_us: int = 0,
               pixel_format: str = "mono"):
        # 실제 카메라와 동일한 인터페이스 제공
        return cls(serial=serial, interface_type=interface_type)

    def open(self):
        pass

    def is_open(self) -> bool:
        return True

    def close(self):
        pass

    def get_trigger_mode(self):
        pass

    def get_trigger_source(self):
        pass

    def execute_software_trigger(self, path: str = None) -> bool:
        try:
            print('Execute software trigger for mock camera')
            import shutil

            if not os.path.exists(self.BUFFER_PATH):
                os.makedirs(self.BUFFER_PATH)

            if path is None or not os.path.exists(path):
                image = np.random.randint(0, 256, size=(2048, 2448, 3), dtype=np.uint8)
                cv2.imwrite(f'{self.BUFFER_PATH}/{self._serial}.bmp', image)
            else:
                shutil.copy2(path,
                             f'{self.BUFFER_PATH}/{self._serial}.bmp')
            return True
        except Exception as e:
            print('failed to execute software trigger in mock camera')
            traceback.print_exc()
            return False

    def set_trigger_mode(self, mode: int):
        pass

    def set_trigger_source(self, source: int):
        pass

    def set_trigger_mode_on(self):
        pass

    def set_trigger_mode_off(self):
        pass

    def set_trigger_source_hardware(self, value):
        pass

    def set_trigger_source_software(self):
        pass

    def set_exposure_time(self, exposure_time: float):
        pass

    def set_pixel_format_mono(self):
        pass

    def set_pixel_format_rgb(self):
        pass

    def get_frame(self):
        try:
            path = f'{self.BUFFER_PATH}/{self._serial}.bmp'
            if os.path.exists(path) and cv2.imread(path) is not None:
                image = cv2.imread(path)
                os.remove(path)

                return np.array(image)
        except Exception as e:
            print('failed to get frame in mock camera')
            traceback.print_exc()

    @property
    def cam_serial(self) -> str:
        return self._serial
