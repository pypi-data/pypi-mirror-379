import cv2
import time
import threading
import numpy as np
from typing import Optional, Callable
from datetime import datetime
from eq1core.dto import CameraDTO
from eq1core.data import ImageData
from eq1core.logger import AppLogger
from eq1core.lib.camera.frame_grabber.interface import CommonLineScanCameraInterface


class ImageGrabber(threading.Thread):
    def __init__(self, camera_dto: CameraDTO, callback_fn: Optional[callable]  = None):
        super().__init__()
        self.daemon = True
        self._stop_event = threading.Event()
        self._lock = threading.Lock()
        self.connection_retry = False
        self.connection_retry_interval_sec = 3
        self.connection_retry_started_at = time.time()

        self._camera_number = camera_dto.number
        self._camera_serial = camera_dto.serial
        self._grabber_serial = camera_dto.fg_serial

        self._camera_type = camera_dto.settings.get('camera_type','mock').lower()
        self._md_pixel_resolution_mm = camera_dto.settings.get('md_pixel_resolution_mm', None)
        self._cd_pixel_resolution_mm = camera_dto.settings.get('cd_pixel_resolution_mm', None)
        self._md_pixel = camera_dto.settings.get('md_pixel', None)

        self._camera: CommonLineScanCameraInterface = None
        self._timeout: int = None

        # self._display_info = MV_FG_DISPLAY_FRAME_INFO()
        # self._image_info = MV_FG_INPUT_IMAGE_INFO()

        self._save_image_buffer = None
        self._save_image_buffer_size = None

        self._window_id = None

        self._on_grabbed_frame: Optional[Callable[[ImageData], None]] = None
        if callable(callback_fn):
            self._on_grabbed_frame = callback_fn

        res = self.connect()
        if not res:
            print('Failed to connect camera')

    @property
    def camera_number(self) -> int:
        return self._camera_number

    @property
    def camera_serial(self) -> str:
        return self._camera_serial

    @property
    def md_pixel_resolution_mm(self):
        return self._md_pixel_resolution_mm

    @property
    def cd_pixel_resolution_mm(self):
        return self._cd_pixel_resolution_mm

    @property
    def md_pixel(self):
        return self._md_pixel

    def execute_stream_software_trigger(self, path: str = None) -> bool:
        self._camera.execute_stream_software_trigger(path)

    def connect(self):
        self._camera = None
        if self._camera_type == 'mock':
            from eq1core.mock.mock_linescan_camera import MockCamera as Camera
            print('>> mock camera')
        else:
            from eq1core.lib.camera.frame_grabber.camera import MvLineScanCamera as Camera

        camera = Camera.create(
            camera_serial_number=self._camera_serial,
            frame_grabber_serial_number=self._grabber_serial,
            lock=self._lock
        )
        if not isinstance(camera, CommonLineScanCameraInterface):
            AppLogger.write_error(self, 'Camera is not instance of CommonLineScanCameraInterface. Failed to create camera instance.')
            return False

        res = camera.start_acquisition()
        if not res:
            AppLogger.write_error(self, 'Failed to start acquisition. close camera.', print_to_terminal=True)
            camera.close()
            return False

        self._camera = camera

        return True

    def set_window_id(self, window_id):
        self._window_id = window_id

    def set_grab_callback_fn(self, callback_fn: callable):
        self._on_grabbed_frame = callback_fn

    def run(self):
        self._stop_event.clear()

        while not self._stop_event.is_set():
            if self.connection_retry and (time.time() - self.connection_retry_started_at > self.connection_retry_interval_sec):
                AppLogger.write_debug(self, 'Start to reconnect camera', print_to_terminal=True)
                self.connection_retry_started_at = time.time()
                res = self.connect()
                if not res:
                    AppLogger.write_error(self, 'Failed to reconnect camera', print_to_terminal=True)
                    continue

                self.connection_retry = False
                continue

            if not self.check_status():
                self.connection_retry = True
                continue

            image = self._camera.get_frame()
            if image is None:
                continue

            print(f"FrameNumber:[{self._camera.frame_number}],    Width[{np.shape(image)[1]}],    Height[{np.shape(image)[0]}]")

            if callable(self._on_grabbed_frame):
                self._on_grabbed_frame(
                    ImageData(
                        camera_number=self._camera_number,
                        image=image,
                        captured_at=datetime.now(),
                        md_pixel_resolution_mm=self._md_pixel_resolution_mm if self._md_pixel_resolution_mm is not None else None,
                        cd_pixel_resolution_mm=self._cd_pixel_resolution_mm if self._cd_pixel_resolution_mm is not None else None,
                    )
                )

        if self._camera is not None:
            self._camera.stop_acquisition()
            self._camera.close()

    def stop(self):
        self._stop_event.set()

    def check_status(self) -> bool:
        # TODO : 카메라 연결 되었다가 끊어지는 경우, 상태 체크도 필요하고, 재연결 로직도 구현해야함..!
        if self._camera is None:
            return False
        # TODO : bugfix. 카메라 연결 상태 체크 로직이 이미지에 경계선을 만드는 문제가 있음..
        # if not self._camera.is_connected():
        #     self._camera.close()
        #     self._camera = None
        #     return False
        return True

    def clear_frame_buffer(self):
        if self._camera is None:
            return
        if not self._camera.on_acquisition:
            return
        self._camera.stop_acquisition()
        self._camera.start_acquisition()


if __name__ == "__main__":
    camera_dto = CameraDTO(
        name='x',
        camera_serial='DA2682636',
        grabber_serial='DA4991652',
    )

    _stop_flag = False

    def cv_show(image):
        cv2.imshow('image', image)
        cv2.waitKey(1)

    worker = ImageGrabber(camera_dto)
    worker.set_grab_callback_fn(cv_show)

    res = worker.connect()
    print('connection', res)

    worker.start()

    while not _stop_flag:
        pass

    worker.stop()
