import time
import threading
import traceback
from datetime import datetime
from enum import Enum

from eq1core.dto import CameraDTO
from eq1core.data import ImageData
from eq1core.logger import AppLogger


class CameraHandler(threading.Thread):
    def __init__(self, camera_dto: CameraDTO, callback_fn: callable = None):
        super().__init__()
        if not isinstance(camera_dto, CameraDTO):
            raise ValueError('camera_dto must be instance of CameraDTO')

        self._camera = None
        self._stop_flag = threading.Event()
        self._check_flag = threading.Event()
        self._callback_fn = callback_fn
        self._pause_flag = threading.Event()
        self._capturing_flag = threading.Event()
        self._camera_serial = camera_dto.serial
        self._camera_number = camera_dto.number
        self._last_captured_at = time.time()

        # settings에서 카메라 설정 정보 가져오기
        settings = camera_dto.settings or {}
        self._is_mock = settings.get('camera_type', 'mock').lower() == 'mock'
        self._interface_type = settings.get('interface_type', '').lower()
        self._exposure_time = float(settings.get('exposure_time', 30000))
        self._gain_db = float(settings.get('gain_db', 0))
        self._trigger_mode = settings.get('trigger_mode', 'off').lower()
        self._trigger_source = settings.get('trigger_source', 'sw').lower()
        self._trigger_delay_us = int(settings.get('trigger_delay_us', 0))

        # 픽셀 해상도 정보 (ImageGrabber와 호환성을 위해 추가)
        self._md_pixel_resolution_mm = settings.get('md_pixel_resolution_mm', None)
        self._cd_pixel_resolution_mm = settings.get('cd_pixel_resolution_mm', None)
        self._md_pixel = settings.get('md_pixel', None)

        self.connect()
        self.last_captured_at = time.time()

    def connect(self):
        try:
            if self._is_mock:
                from eq1core.mock.mock_camera import MockCamera as Camera
            else:
                from eq1core.lib.camera.hikvision import HikVision as Camera

            print('camera serial', self._camera_serial)
            self._camera = Camera.create(
                serial=self._camera_serial,
                interface_type=self._interface_type,
                exposure_time=self._exposure_time,
                gain_db=self._gain_db,
                trigger_mode=self._trigger_mode,
                trigger_source=self._trigger_source,
                trigger_delay_us=self._trigger_delay_us
            )
            return True
        except Exception as e:
            AppLogger.write_error(self, f'Camera no.{self._camera_number} connect failed. {e}', print_to_terminal=True)
            self._camera = None  # 예외 발생 시 명시적으로 None으로 설정
            return False

    def check_status(self):
        self._check_flag.set()

    def stop(self):
        self._stop_flag.set()

    @property
    def camera_number(self):
        return self._camera_number

    def is_mock(self):
        return self._is_mock

    @property
    def md_pixel_resolution_mm(self):
        return self._md_pixel_resolution_mm
    
    @property
    def cd_pixel_resolution_mm(self):
        return self._cd_pixel_resolution_mm
    
    @property
    def md_pixel(self):
        return self._md_pixel

    # TODO : 외부에서 camera 인스턴스에 직접 접근하는 것들은 해당 함수로 대체하기.
    def execute_software_trigger(self, path: str = None):
        try:
            if self._camera is None:
                AppLogger.write_error(self, f'Camera no.{self._camera_number} is not connected.', print_to_terminal=True)
                return False
                
            if self._camera.execute_software_trigger(path):
                AppLogger.write_debug(self, f'Camera no.{self._camera_number} execute software trigger success.', print_to_terminal=True)
                return True
            else:
                AppLogger.write_debug(self, f'Camera no.{self._camera_number} execute software trigger failed.', print_to_terminal=True)
                return False
        except Exception as e:
            AppLogger.write_error(self, f'Camera no.{self._camera_number} execute software trigger failed. {e}', print_to_terminal=True)
            self.check_status()
            return False

    def keep_alive_check(self):
        try:
            if self._camera is None:
                return False
            is_ok = self._camera.is_open()
            # UIEventLogger는 현재 프로젝트에 없으므로 주석 처리
            # UIEventLogger.log_camera_worker_status(
            #     is_ok=is_ok,
            #     message='Camera is OK' if is_ok else 'Camera is not OK',
            #     camera_number=self._camera_number
            # )
            if not is_ok:
                AppLogger.write_error(self, f'Camera no.{self._camera_number} is disconnected .. retry after 5 seconds.', print_to_terminal=True)
                return False
            return True
        except Exception as e:
            AppLogger.write_error(self,
                                  f'Camera no.{self._camera_number}. {e}. {traceback.format_exc()}')
            return False

    def run(self):
        AppLogger.write_info(self, f'Camera no.{self._camera_number} Thread Started.')
        self._stop_flag.clear()
        # worker is up and logging camera status.
        self._check_flag.set()
        self._pause_flag.clear()

        while not self._stop_flag.is_set():
            time.sleep(0.001)
            if time.time() - self._last_captured_at > 600:  # 카메라 사용 되지 않고 대기하는 동안 10분 간격으로 상태 체크
                self._last_captured_at = time.time()
                self._check_flag.set()

            if self._check_flag.is_set():
                if self.keep_alive_check():
                    self._check_flag.clear()
                else:
                    if self._camera is not None:
                        try:
                            self._camera.close(self._camera_serial)
                        except Exception as e:
                            AppLogger.write_error(self, f'Camera no.{self._camera_number} close failed: {e}')
                    time.sleep(5)
                    self.connect()

            while self._pause_flag.is_set():
                self._capturing_flag.set()
                time.sleep(0.001)

            self._capturing_flag.clear()
            try:
                if self._camera is None:
                    time.sleep(0.1)  # 카메라가 연결되지 않은 경우 잠시 대기
                    continue
                image = self._camera.get_frame()
                if image is None:
                    continue
                self._last_captured_at = time.time()
                AppLogger.write_debug(self, f'Camera no.{self._camera_number} Captured.')
                data = ImageData(
                    camera_number=self._camera_number,
                    image=image,
                    captured_at=datetime.now()
                )
                if callable(self._callback_fn):
                    self._callback_fn(data)

            except Exception as e:
                AppLogger.write_error(self, f'Camera no.{self._camera_number} Error. {e} {traceback.format_exc()}\n')

    def clear_frame_buffer(self):
        """프레임 버퍼 클리어 (ImageGrabber와 호환성을 위해 추가)"""
        # CameraHandler는 실시간 스트리밍 방식이므로 버퍼 클리어가 필요 없음
        # 하지만 호환성을 위해 빈 메서드로 구현
        pass

    def request_capture(self):
        """소프트웨어 트리거로 이미지 캡처 요청"""
        # 현재 트리거 설정 저장
        original_trigger_mode = None
        original_trigger_source = None
        
        try:
            if self._camera is None:
                AppLogger.write_error(self, f'Camera no.{self._camera_number} is not connected.', print_to_terminal=True)
                return None
            
            # 현재 트리거 설정 저장
            try:
                original_trigger_mode = self._camera.get_trigger_mode()
                original_trigger_source = self._camera.get_trigger_source()
            except:
                # 일부 카메라는 이 메서드가 없을 수 있음
                pass
                
            # 트리거 모드를 소프트웨어로 변경
            try:
                self._camera.set_trigger_mode_on()
                self._camera.set_trigger_source_software()
            except:
                # 이미 설정되어 있거나 설정 변경이 불가능한 경우
                pass
                
            # 소프트웨어 트리거 실행
            if self.execute_software_trigger():
                # 이미지 캡처
                image = self._camera.get_frame()
                if image is not None:
                    self._last_captured_at = time.time()
                    AppLogger.write_debug(self, f'Camera no.{self._camera_number} Captured.')
                    
                    # ImageData 생성
                    data = ImageData(
                        camera_number=self._camera_number,
                        image=image,
                        captured_at=datetime.now(),
                        md_pixel_resolution_mm=self._md_pixel_resolution_mm,
                        cd_pixel_resolution_mm=self._cd_pixel_resolution_mm
                    )
                    
                    # callback_fn 호출 (InspectionRequestEventListener.on_request)
                    if callable(self._callback_fn):
                        self._callback_fn(data)
                        return data
                    else:
                        AppLogger.write_warning(self, f'Camera no.{self._camera_number} callback_fn is not set.', print_to_terminal=True)
                        return data
                else:
                    AppLogger.write_error(self, f'Camera no.{self._camera_number} failed to get frame.', print_to_terminal=True)
                    return None
            else:
                AppLogger.write_error(self, f'Camera no.{self._camera_number} software trigger failed.', print_to_terminal=True)
                return None
                
        except Exception as e:
            AppLogger.write_error(self, f'Camera no.{self._camera_number} request_capture failed: {e}', print_to_terminal=True)
            return None
            
        finally:
            # 원래 트리거 설정으로 복원
            try:
                if original_trigger_mode is not None:
                    self._camera.set_trigger_mode(original_trigger_mode)
                if original_trigger_source is not None:
                    self._camera.set_trigger_source(original_trigger_source)
            except:
                # 복원 실패 시 로그만 남김
                AppLogger.write_warning(self, f'Camera no.{self._camera_number} failed to restore original trigger settings.', print_to_terminal=True)
