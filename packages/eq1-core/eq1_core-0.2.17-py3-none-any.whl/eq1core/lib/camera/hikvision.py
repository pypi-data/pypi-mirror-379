import cv2
import traceback
import numpy as np
from typing import Optional
from MvImport.MvCameraControl_class import *
from eq1core.lib.camera.interface import CameraInterface
from eq1core.logger import AppLogger


class CameraRepo:
    _instance = None

    @classmethod
    def _get_instance(cls):
        return cls._instance

    @classmethod
    def instance(cls):
        cls._instance = cls()
        cls.instance = cls._get_instance

        return cls._instance

    def __init__(self):
        self._cams = {}

    def find_cam(self, serial: str):
        if serial in self._cams:
            return self._cams[serial]

        return None

    def put(self, cam: CameraInterface, serial: str):
        self._cams[serial] = cam

    def remove(self, serial: str):
        if serial in self._cams:
            del self._cams[serial]


class HikvisionColorFormat:
    MONO8 = 0x01000000 | 8 << 16 | 0x0001
    MONO10 = 0x01000000 | 16 << 16 | 0x0003
    BayerGR8 = 0x01000000 | 8 << 16 | 0x0008
    RGB8 = 0x01000000 | 24 << 16 | 0x0014


class HikVision(CameraInterface):
    def __init__(self, serial: str = None, interface: str = ""):
        self._cam = MvCamera()
        self._cam_serial = serial
        self._interface = interface
        self._nPayloadSize = None
        self._data_buf = None
        self._exposure_time = None
        self._trigger_mode = None
        self._trigger_source = None
        self._trigger_delay_us = None
        self._pixel_format = None
        self._timeout = None

        self._valid_devices = self.get_device_infos()
        print('self._valid_devices', self._valid_devices)

    @property
    def cam_serial(self) -> str:
        return self._cam_serial

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
        repo = CameraRepo.instance()
        used_cam = repo.find_cam(serial)
        if used_cam is not None:
            print('already used camera')
            return used_cam

        cam = cls(serial, interface_type)
        cam._timeout = timeout
        cam.open(serial)
        cam.set_exposure_time(exposure_time)
        cam.set_trigger_delay_us(trigger_delay_us)
        cam.set_gain_db(gain_db)

        if trigger_mode.lower() == "on":
            cam.set_trigger_mode_on()
        else:
            cam.set_trigger_mode_off()

        if trigger_source.lower() == "hw":
            cam.set_trigger_source_hardware(0)
        elif trigger_source.lower() == "line0":
            cam.set_trigger_source_hardware(0)
        elif trigger_source.lower() == "line2":
            cam.set_trigger_source_hardware(2)
        else:
            cam.set_trigger_source_software()

        # TODO : pixel format 설정이 동작하지 않음. 일단 주석 처리 해놓았으며 추후 확인 필요.
        # if pixel_format.lower() == "mono":
        #     cam.set_pixel_format_mono()
        # else:
        #     cam.set_pixel_format_rgb()

        repo.put(cam, serial)

        return cam

    def set_trigger_mode(self, mode: int):
        ret = self._cam.MV_CC_SetEnumValue("TriggerMode", mode)
        if ret != 0:
            print(f"set trigger mode to ({mode}) on fail! ", ret)
            return False

        self._trigger_mode = mode

    def set_trigger_source(self, source: int):
        if source == MV_TRIGGER_SOURCE_SOFTWARE:
            return self.set_trigger_source_software()
        elif source == MV_TRIGGER_SOURCE_LINE0:
            return self.set_trigger_source_hardware(MV_TRIGGER_SOURCE_LINE0)
        elif source == MV_TRIGGER_SOURCE_LINE2:
            return self.set_trigger_source_hardware(MV_TRIGGER_SOURCE_LINE2)

    def is_open(self):
        self._cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_ON)
        self._cam.MV_CC_SetEnumValue("TriggerSource", MV_TRIGGER_SOURCE_SOFTWARE)
        self._cam.MV_CC_SetCommandValue("TriggerSoftware")

        res = self.get_frame()

        self._cam.MV_CC_SetEnumValue("TriggerMode", self._trigger_mode)
        self._cam.MV_CC_SetEnumValue("TriggerSource", self._trigger_source)

        return res is not None

    def close(self, serial):
        self._cam.MV_CC_StopGrabbing()
        self._cam.MV_CC_CloseDevice()
        self._cam.MV_CC_DestroyHandle()

        repo = CameraRepo.instance()
        repo.remove(serial)

    def open(self, serial: str):
        try:
            deviceList = MV_CC_DEVICE_INFO_LIST()
            if self._interface.lower() == "gige":
                tlayerType = MV_GIGE_DEVICE
            elif self._interface.lower() == "usb":
                tlayerType = MV_USB_DEVICE
            else:
                tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE

            ret = MvCamera.MV_CC_EnumDevices(tlayerType, deviceList)
            if ret != 0:
                print(f"Enum devices failed! ret[0x{ret:x}]")
                return

            if deviceList.nDeviceNum == 0:
                print("No devices found!")
                return

            device_info = None
            for i in range(deviceList.nDeviceNum):
                stDeviceList = cast(deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
                if stDeviceList.nTLayerType == MV_GIGE_DEVICE:
                    device_serial = bytes(stDeviceList.SpecialInfo.stGigEInfo.chSerialNumber).decode('utf-8').strip('\x00')
                elif stDeviceList.nTLayerType == MV_USB_DEVICE:
                    device_serial = bytes(stDeviceList.SpecialInfo.stUsb3VInfo.chSerialNumber).decode('utf-8').strip('\x00')
                else:
                    continue

                if device_serial == serial:
                    device_info = stDeviceList
                    break

            if device_info is None:
                print(f"Device with serial number {serial} not found!")
                return

            ret = self._cam.MV_CC_CreateHandle(device_info)
            if ret != 0:
                print(f"Failed to create handle for device with serial {serial}")
                return

            ret = self._cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
            if ret != 0:
                print(f"Failed to open device with serial {serial}")
                return

            if device_info.nTLayerType == MV_GIGE_DEVICE:
                nPacketSize = self._cam.MV_CC_GetOptimalPacketSize()

            stParam = MVCC_INTVALUE()
            memset(byref(stParam), 0, sizeof(MVCC_INTVALUE))
            ret = self._cam.MV_CC_GetIntValue("PayloadSize", stParam)
            self._nPayloadSize = stParam.nCurValue

            ret = self._cam.MV_CC_StartGrabbing()
            if ret != 0:
                print(f"Failed to start grabbing from device with serial {serial}")
                return

            self._stDeviceList = MV_FRAME_OUT_INFO_EX()
            memset(byref(self._stDeviceList), 0, sizeof(self._stDeviceList))
            self._data_buf = (c_ubyte * self._nPayloadSize)()
        except Exception as e:
            AppLogger.write_debug(self, f"Failed to open camera by serial {serial}: {e} {traceback.format_exc()}", print_to_terminal=True)

    def get_trigger_mode(self) -> int:
        return self._trigger_mode

    def get_trigger_source(self) -> int:
        return self._trigger_source

    def set_trigger_mode_on(self):
        ret = self._cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_ON)
        if ret != 0:
            print("set trigger mode on fail! ", ret)
            return False

        self._trigger_mode = MV_TRIGGER_MODE_ON
        return True

    def set_trigger_mode_off(self):
        ret = self._cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_OFF)
        if ret != 0:
            print("set trigger mode off fail! ", ret)
            return False

        self._trigger_mode = MV_TRIGGER_MODE_OFF
        return True

    def set_trigger_source_software(self):
        ret = self._cam.MV_CC_SetEnumValue("TriggerSource", MV_TRIGGER_SOURCE_SOFTWARE)
        if ret != 0:
            print("set trigger source software fail! ", ret)
            return False

        self._trigger_source = MV_TRIGGER_SOURCE_SOFTWARE
        return True

    def set_trigger_source_hardware(self, line_number: int = MV_TRIGGER_SOURCE_LINE0):
        ret = self._cam.MV_CC_SetEnumValue("TriggerSource", line_number)
        if ret != 0:
            print("set trigger source line0 fail! ", ret)
            return False

        self._trigger_source = line_number
        return True

    def set_trigger_delay_us(self, delay_us: float):
        ret = self._cam.MV_CC_SetFloatValue("TriggerDelay", delay_us)
        if ret != 0:
            print("set trigger delay fail! ", ret)
            return False

        return True

    def set_exposure_time(self,  time_us: float):
        ret = self._cam.MV_CC_SetFloatValue("ExposureTime", time_us)
        if ret != 0:
            print("set exposure time fail! ", ret)
            return False

        self._exposure_time = time_us
        return True

    def set_gain_db(self, gain_db: float):
        ret = self._cam.MV_CC_SetFloatValue("Gain", gain_db)
        if ret != 0:
            print("set gain db fail! ", ret)
            return False

        return True

    def set_pixel_format_mono(self):
        # TODO : 동작하지 않음.. 시간이 너무 오래 걸려서 일단 보류. 추후 확인 필요.
        ret = self._cam.MV_CC_SetEnumValue("PixelFormat", HikvisionColorFormat.MONO8)
        if ret != 0:
            print("set pixel format mono fail! ", ret)
            return False

        self._pixel_format = HikvisionColorFormat.MONO8
        return True

    def set_pixel_format_rgb(self):
        ret = self._cam.MV_CC_SetEnumValue("PixelFormat", HikvisionColorFormat.RGB8)
        if ret != 0:
            print("set pixel format rgb fail! ", ret)
            return False

        self._pixel_format = HikvisionColorFormat.RGB8
        return True

    def execute_software_trigger(self, *args) -> bool:
        try:
            ret = self._cam.MV_CC_SetCommandValue("TriggerSoftware")
            if ret != 0:
                error_message = f"Failed to execute software trigger. ret must be 0. but {ret} returned."
                AppLogger.write_debug(self, error_message, print_to_terminal=True)
                AppLogger.write_error(self, error_message)
                return False
            return True
        except Exception as e:
            AppLogger.write_error(self, f"Failed to execute software trigger: {e} {traceback.format_exc()}")

    @classmethod
    def get_device_infos(cls):
        res = []

        try:
            device_list = MV_CC_DEVICE_INFO_LIST()
            connection_type = MV_GIGE_DEVICE | MV_USB_DEVICE
            ret = MvCamera.MV_CC_EnumDevices(connection_type, device_list)
            if ret != 0:
                return RuntimeError("Not found camera devices")

            for i in range(device_list.nDeviceNum):
                stDeviceList = cast(device_list.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
                if stDeviceList.nTLayerType == MV_GIGE_DEVICE:
                    device_serial = bytes(stDeviceList.SpecialInfo.stGigEInfo.chSerialNumber).decode('utf-8').strip('\x00')
                    res.append(('gige', device_serial))
                elif stDeviceList.nTLayerType == MV_USB_DEVICE:
                    device_serial = bytes(stDeviceList.SpecialInfo.stUsb3VInfo.chSerialNumber).decode('utf-8').strip('\x00')
                    res.append(('usb', device_serial))
                else:
                    print('Unknown device type')

        except Exception as e:
            AppLogger.write_error(cls, f"Failed to get device infos: {e} {traceback.format_exc()}")

        return res

    def get_frame(self) -> Optional[np.ndarray]:
        try:
            ret = self._cam.MV_CC_GetOneFrameTimeout(byref(self._data_buf), self._nPayloadSize, self._stDeviceList, self._timeout)
            if ret == 2147483651 or ret == 2147483655:
                # get frame timeout
                return None

            if ret != 0:
                error_message = f"Failed to get frame. ret value error. expected 0 but hikrobot library 'self._cam.MV_CC_GetOneFrameTimeout(byref(self._data_buf), self._nPayloadSize, self._stDeviceList, self._timeout)' return {ret}"
                AppLogger.write_debug(self, error_message, print_to_terminal=True)
                AppLogger.write_error(self, error_message)
                return None

            nRGBSize = self._stDeviceList.nWidth * self._stDeviceList.nHeight * 3
            stConvertParam = MV_CC_PIXEL_CONVERT_PARAM()
            memset(byref(stConvertParam), 0, sizeof(stConvertParam))
            stConvertParam.nWidth = self._stDeviceList.nWidth
            stConvertParam.nHeight = self._stDeviceList.nHeight
            stConvertParam.pSrcData = self._data_buf
            stConvertParam.nSrcDataLen = self._stDeviceList.nFrameLen
            stConvertParam.enSrcPixelType = self._stDeviceList.enPixelType
            stConvertParam.enDstPixelType = PixelType_Gvsp_RGB8_Packed
            stConvertParam.pDstBuffer = (c_ubyte * nRGBSize)()
            stConvertParam.nDstBufferSize = nRGBSize

            self._cam.MV_CC_ConvertPixelType(stConvertParam)

            img_buff = (c_ubyte * stConvertParam.nDstLen)()
            memmove(byref(img_buff), stConvertParam.pDstBuffer, stConvertParam.nDstLen)
            image = np.array(img_buff).reshape(stConvertParam.nHeight, stConvertParam.nWidth, 3)

            return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        except Exception as e:
            AppLogger.write_error(self, f"Failed to get frame: {e} {traceback.format_exc()}")


if __name__ == "__main__":
    import time
    serial = '02E16700978'
    cam = HikVision.create(serial=serial,
                           exposure_time=30000,
                           timeout=1000,
                           trigger_mode="on",
                           trigger_source="sw",
                           pixel_format="mono",
                           interface_type="gige")
    print(cam.is_open())
    cam.close(serial)
