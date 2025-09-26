import threading
import numpy as np
from typing import Optional
from ctypes import cast, POINTER, c_ubyte, c_uint, byref, sizeof, memset
from eq1core.lib.camera.MvImport.MVFGControl_class import FGGeneral, FGStream, FGImageProcess
from eq1core.lib.camera.MvImport.MVFGDefines_header import MV_FG_BUFFER_INFO
from eq1core.lib.camera.MvImport.MVFGErrorDefine_const import MV_FG_SUCCESS
from eq1core.lib.camera.frame_grabber.interface import CommonLineScanCameraInterface
from eq1core.lib.camera.frame_grabber.constants import TRIGGER_MODE_OFF, MONO8, MONO10, MONO12
from eq1core.lib.camera.frame_grabber.data import HexStr
from eq1core.lib.camera.frame_grabber.mvfg import MvfgCommonLibrary
from eq1core.logger import AppLogger  # TODO : src 의존성 제거하기


class LineScanCameraRepository:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LineScanCameraRepository, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not hasattr(self, '_repo'):
            self._repo = {}

    def put(self, camera: CommonLineScanCameraInterface):
        self._repo[camera.camera_serial_number] = camera

    def get_by_serial(self, serial_number: str) -> Optional[CommonLineScanCameraInterface]:
        return self._repo.get(serial_number, None)

    def get_all(self):
        return list(self._repo.values())

    def delete(self, serial_number: str):
        self._repo.pop(serial_number)


class MvLineScanCamera(CommonLineScanCameraInterface):
    def __init__(self, camera_serial_number: str, frame_grabber_serial_number: str, timeout: int, lock: threading.Lock = None):
        super().__init__()
        self._mvfg_lib = MvfgCommonLibrary()  # TODO : 추후 유틸리티성 모듈로 분리하여 사용할 수 있도록 할 예정.
        self._camera_serial_number = camera_serial_number
        self._frame_grabber_serial_number = frame_grabber_serial_number
        self._fg_interface = None
        self._fg_device = None
        self._fg_stream = FGStream()
        self._interface_setting = None
        self._device_setting = None
        # self._fg_image_process = None
        self._frame_info = None
        self._trigger_mode = c_uint(0)
        self._timeout = timeout
        self._lock: threading.Lock = lock
        self._on_acquisition = False

    @classmethod
    def create(cls,
               camera_serial_number: str,
               frame_grabber_serial_number: str,
               timeout: int = 1000,
               lock: threading.Lock = None
               ) -> Optional[CommonLineScanCameraInterface]:
        camera = LineScanCameraRepository().get_by_serial(camera_serial_number)
        if camera is not None:
            print(f"Camera already exists. {camera_serial_number}")
            return camera

        camera = cls(
            camera_serial_number=camera_serial_number,
            frame_grabber_serial_number=frame_grabber_serial_number,
            timeout=timeout,
            lock=lock
        )
        res = camera.open()
        if not res:
            print(f"Failed to open camera. {camera_serial_number}")
            return None

        LineScanCameraRepository().put(camera)
        return camera

    @property
    def camera_serial_number(self):
        return self._camera_serial_number

    @property
    def frame_number(self):
        return self._frame_info.nFrameID

    @property
    def on_acquisition(self):
        return self._on_acquisition

    def open(self):
        self._fg_interface = self._mvfg_lib.open_interface_by_serial(self._frame_grabber_serial_number)
        if self._fg_interface is None:
            print("Failed to open interface")
            return False

        device_list = self._mvfg_lib.get_device_list(self._fg_interface)
        print('device_list', device_list)
        for i, device_info in enumerate(device_list):
            if device_info.serial_number == self._camera_serial_number:
                self._fg_device = self._mvfg_lib.open_device(self._fg_interface, i)
                break
        if self._fg_device is None:
            print("Failed to open device")
            return False

        ret = self._fg_device.GetNumStreams(c_uint(0))
        if MV_FG_SUCCESS != ret:
            print("Get Num Streams Failed! ret:" + HexStr.from_int(ret))
            return False

        ret = self._fg_stream.OpenStream(self._fg_device, c_uint(0))
        if MV_FG_SUCCESS != ret:
            print("Open Stream Failed! ret:" + HexStr.from_int(ret))
            return False

        # self._fg_image_process = FGImageProcess(self._fg_stream)

        ret = self._fg_stream.SetBufferNum(c_uint(3))
        if MV_FG_SUCCESS != ret:
            print("Set Buffer Num Failed! ret:" + HexStr.from_int(ret))
            return False

        print(f"Success to open device.")
        self._interface_setting = FGGeneral(self._fg_interface)
        self._device_setting = FGGeneral(self._fg_device)

        return True

    def close(self):
        res = self._mvfg_lib.close_device(self._fg_device)
        if not res:
            print("Failed to close device")

        res = self._mvfg_lib.close_interface(self._fg_interface)
        if not res:
            print("Failed to close interface")

        self.delete()
        print(f"Success to close device. {self._camera_serial_number}")

    def clear_buffer_memory(self):
        self._frame_info = MV_FG_BUFFER_INFO()
        memset(byref(self._frame_info), 0, sizeof(self._frame_info))

    def start_acquisition(self) -> bool:
        self.clear_buffer_memory()
        ret = self._fg_stream.StartAcquisition()
        if MV_FG_SUCCESS != ret:
            print("Start Acquisition Failed! ret:" + HexStr.from_int(ret))
            return False
        self._on_acquisition = True
        return True

    def stop_acquisition(self) -> bool:
        ret = self._fg_stream.StopAcquisition()
        if MV_FG_SUCCESS != ret:
            print("Stop Acquisition Failed! ret:" + HexStr.from_int(ret))
            return False
        self._on_acquisition = False
        return True

    def get_frame(self) -> Optional[np.ndarray]:
        try:
            ret = self._fg_stream.GetFrameBuffer(self._frame_info, self._timeout)
            if MV_FG_SUCCESS != ret:
                if self._trigger_mode is TRIGGER_MODE_OFF:
                    print("Get Frame Buffer Failed! ret:" + HexStr.from_int(ret))
                return None

            if self._lock is not None:
                self._lock.acquire()

            image_array = np.ctypeslib.as_array(cast(self._frame_info.pBuffer, POINTER(c_ubyte)),
                                                shape=(self._frame_info.nFilledSize,))

            if self._frame_info.enPixelType in [MONO8, MONO10, MONO12]:
                image = image_array[:self._frame_info.nHeight * self._frame_info.nWidth].reshape(
                    (self._frame_info.nHeight, self._frame_info.nWidth, 1)
                )
            else:
                AppLogger.write_error(self, f"Unsupported pixel type: {self._frame_info.enPixelType}", print_to_terminal=True)
                return None

            if self._lock is not None:
                self._lock.release()

            ret = self._fg_stream.ReleaseFrameBuffer(self._frame_info)
            if MV_FG_SUCCESS != ret:
                AppLogger.write_error(self, f"Release Frame Buffer Failed! ret:{ret}", print_to_terminal=True)
                return None

            return image
        except Exception as e:
            import traceback
            AppLogger.write_error(self, f"failed to get frame. {traceback.format_exc()}", print_to_terminal=True)
            return None

    def set_interface_camera_type(self, camera_type: int = 0) -> bool:
        """
        camera_type:
            0: FrameScan
            1: LineScan
        """
        ret = self._interface_setting.SetEnumValue("CameraType", camera_type)
        print('ret', ret)
        if MV_FG_SUCCESS != ret:
            print("Set Camera Type Failed! ret:" + HexStr.from_int(ret))
            return False
        return True

    def get_interface_camera_type(self):
        camera_type = c_uint(0)
        ret = self._interface_setting.GetEnumValue("CameraType", camera_type)
        print('ret', ret)
        print('camera_type', camera_type)

    def get_device_scan_type(self):
        # 동작 검증 필요
        scan_type = c_uint(0)
        ret = self._device_setting.GetEnumValue("DeviceScanType", scan_type)
        print('ret', ret)
        print('scan_type', scan_type)

    def get_camera_serial_number(self):
        # 동작 검증 필요
        pc_node_value = c_uint(0)
        ret = self._device_setting.GetStringValue("DeviceSerialNumber", pc_node_value)
        print('ret', ret)

    def set_device_image_width(self, width: int) -> bool:
        ret = self._device_setting.SetIntValue("Width", width)
        if MV_FG_SUCCESS != ret:
            print("Set Device Width Failed! ret:" + HexStr.from_int(ret))
            return False
        return True

    def set_device_image_height(self, height: int) -> bool:
        ret = self._device_setting.SetIntValue("Height", height)
        if MV_FG_SUCCESS != ret:
            print("Set Device Height Failed! ret:" + HexStr.from_int(ret))
            return False
        return True

    def execute_stream_software_trigger(self, *args, **kwargs) -> bool:
        # TODO : to be implemented
        pass

    def is_connected(self) -> bool:
        # TODO : 만약 또 카메라 재연결 로직 문제가 생긴다면 일단 이부분을 강제 True 로 설정할 것..
        device_list = self._mvfg_lib.get_device_list(self._fg_interface)

        """
        이미 모든 장치가 연결 상태라면 device_list 가 None 으로 리턴됩니다.
        정상 상태로 간주합니다. 
        """
        if device_list is None:
            return True

        """
        미사용 장치가 존재하면 리스트가 반환됩니다.
        리스트가 반환되었는데 목록이 비어있다면 사용가능한 장치가 없다고 판단합니다.
        """
        if len(device_list) == 0:
            return False

        detected_device_serial_number_list = []
        for device in device_list:
            detected_device_serial_number_list.append(device.serial_number)

        """
        device list 에서 검색된다면 현재 연결이 끊어진 상태라는 의미입니다.
        """
        if self._camera_serial_number in detected_device_serial_number_list:
            return False

        return True

    def delete(self):
        LineScanCameraRepository().delete(self._camera_serial_number)
        self._fg_interface = None
        self._fg_device = None
        self._interface_setting = None
        self._device_setting = None
        self._frame_info = None
        self._on_acquisition = False


if __name__ == "__main__":
    import time

    cam_1 = MvLineScanCamera.create(
        camera_serial_number='DA5002684',  # lint
        frame_grabber_serial_number='DA4991651',
    )

    print('cam1', LineScanCameraRepository().get_by_serial('DA5002684'))

    # cam_1.set_interface_camera_type(0)
    # cam_1.set_device_image_width(1000)


    cam_1.is_connected()

    started_at = time.time()
    while True:
        time.sleep(1)
        print(cam_1.is_connected())
        if time.time() - started_at > 1000:
            break
    cam_1.close()
