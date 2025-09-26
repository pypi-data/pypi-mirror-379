import os
import cv2
import numpy as np
import traceback
import threading
from typing import Optional
from eq1core.lib.camera.frame_grabber.interface import CommonLineScanCameraInterface


class MockCamera(CommonLineScanCameraInterface):
    BUFFER_PATH = '/tmp/mock_camera_buffer'

    def __init__(self, camera_serial_number: str, frame_grabber_serial_number: str, timeout: int, lock: threading.Lock = None):
        super().__init__()
        self._camera_serial_number = camera_serial_number
        self._frame_grabber_serial_number = frame_grabber_serial_number
        self._frame_number = 0
        self._is_connected = True
        print("\nCamera was initialized with mock camera"
              "\nIf you want to test get frame, "
              f"\nput the image file in {self.BUFFER_PATH}/{self._camera_serial_number}.bmp\n")

    @classmethod
    def create(cls, camera_serial_number, frame_grabber_serial_number, *args, **kwargs):

        return cls(camera_serial_number=camera_serial_number, frame_grabber_serial_number=frame_grabber_serial_number, timeout=1000)

    def delete(self):
        pass

    def is_connected(self):
        return self._is_connected

    @property
    def camera_serial_number(self):
        return self._camera_serial_number

    @property
    def frame_number(self):
        return self._frame_number

    def open(self):
        pass

    def close(self):
        pass

    def start_acquisition(self) -> bool:
        return True

    def stop_acquisition(self) -> bool:
        import time
        time.sleep(1)
        return True

    def on_acquisition(self) -> bool:
        return True

    def set_interface_camera_type(self, camera_type: int = 0) -> bool:
        pass

    def get_interface_camera_type(self):
        pass

    def set_device_image_width(self, width: int) -> bool:
        pass

    def set_device_image_height(self, height: int) -> bool:
        pass

    def execute_stream_software_trigger(self, path: str = None) -> bool:
        try:
            print('Execute software trigger for mock camera')
            import shutil

            if not os.path.exists(self.BUFFER_PATH):
                os.makedirs(self.BUFFER_PATH)

            if path is None or not os.path.exists(path):
                image = np.random.randint(0, 256, size=(500, 500, 3), dtype=np.uint8)
                cv2.imwrite(f'{self.BUFFER_PATH}/{self._camera_serial_number}.bmp', image)
            else:
                shutil.copy2(path,
                             f'{self.BUFFER_PATH}/{self._camera_serial_number}.bmp')
            return True
        except Exception as e:
            print('failed to execute software trigger in mock camera')
            traceback.print_exc()
            return False

    def get_frame(self) -> Optional[np.ndarray]:
        try:
            path = f'{self.BUFFER_PATH}/{self._camera_serial_number}.bmp'
            if os.path.exists(path) and cv2.imread(path) is not None:
                image = cv2.imread(path)
                os.remove(path)
                self._frame_number += 1
                return np.array(image)
        except Exception as e:
            print('failed to get frame in mock camera')
            traceback.print_exc()
