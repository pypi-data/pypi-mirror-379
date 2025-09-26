from ctypes import c_bool, c_uint, byref, sizeof, memset
import threading
from typing import Optional
from MVFGControl_class import *
from eq1core.lib.camera.frame_grabber.constants import nInterfaceNum
from eq1core.lib.camera.frame_grabber.data import InterfaceInfo, DeviceInfo, HexStr


class MvfgCommonLibrary:
    """
    *  hikvision sample code 를 참고하여 작성된 코드입니다.
    * 용어 설명
        * MVFG : Machine Vision Frame Grabber
        * interface : 장착된 프레임그래버; 데이터 통신 방식에 따라 분류됨; (CXP, GEV, CAMERALINK, XoF)
        * device : 연결된 카메라;
    """

    def get_interface_list(self) -> list[InterfaceInfo]:
        """
        * hikvision sample code 를 참고하여 작성된 코드입니다.
        * 장착된 프레임그래버 목록을 조회합니다.
        """
        _interface_list = []

        bChanged = c_bool(False)
        ret = FGSystem.UpdateInterfaceList(
            MV_FG_CXP_INTERFACE | MV_FG_GEV_INTERFACE | MV_FG_CAMERALINK_INTERFACE | MV_FG_XoF_INTERFACE, bChanged
        )
        if MV_FG_SUCCESS != ret:
            error_message = "Enum Interfaces Failed! ret:" + HexStr.from_int(ret)
            print(error_message)
            return []

        ret = FGSystem.GetNumInterfaces(nInterfaceNum)
        if MV_FG_SUCCESS != ret:
            error_message = "Get Num Interfaces Failed! ret:" + HexStr.from_int(ret)
            print(error_message)
            return []

        if 0 == nInterfaceNum.value:
            error_message = "No Interface!"
            print(error_message)
            return []

        # if bChanged.value:
        for i in range(0, nInterfaceNum.value):
            stInterfaceInfo = MV_FG_INTERFACE_INFO()
            memset(byref(stInterfaceInfo), 0, sizeof(stInterfaceInfo))
            ret = FGSystem.GetInterfaceInfo(i, stInterfaceInfo)
            if MV_FG_SUCCESS != ret:
                error_message = "Get Interface Info Failed! ret:" + HexStr.from_int(ret)
                print(error_message)
                return []

            info = InterfaceInfo(
                mvfg_interface_info=stInterfaceInfo
            )
            print(f"[{i}] {info}")
            _interface_list.append(info)

        return _interface_list

    def open_interface_by_index(self, index: int) -> Optional[FGInterface]:
        _interface_list = self.get_interface_list()
        if index < 0 or index >= len(_interface_list):
            error_message = "Please select valid index!"
            print(error_message)
            return None

        _fg_interface = FGInterface()
        ret = _fg_interface.OpenInterface(index)
        if MV_FG_SUCCESS != ret:
            error_message = "Open Interface Failed! ret:" + HexStr.from_int(ret)
            print(error_message)
            return None

        print(f"Open Interface Success! index:{index}")
        return _fg_interface

    def open_interface_by_serial(self, serial_number: str) -> Optional[FGInterface]:
        _fg_info = None
        _interface_list = self.get_interface_list()
        print('>! interface_list', _interface_list)

        for i, info in enumerate(_interface_list):
            if info.serial_number != serial_number:
                continue

            _fg_interface = FGInterface()
            ret = _fg_interface.OpenInterface(i)
            if MV_FG_SUCCESS != ret:
                error_message = "Open Interface Failed! ret:" + HexStr.from_int(ret)
                print(error_message)
                return None

            print(f"Open Interface Success! info:{info}")
            return _fg_interface

    def close_interface(self, interface: FGInterface) -> bool:
        ret = interface.CloseInterface()
        if MV_FG_SUCCESS != ret:
            error_message = "Close Interface Failed! ret:" + HexStr.from_int(ret)
            print(error_message)
            return False

        # InterfaceRepository().delete(interface.interface_id)
        print("Close Interface Success!")
        return True

    def get_device_list(self, fg_interface: FGInterface) -> list:
        _device_list = []

        bChanged = c_bool(False)
        nDeviceNum = c_uint(0)

        ret = fg_interface.UpdateDeviceList(bChanged)
        if MV_FG_SUCCESS != ret:
            error_message = "Enum Devices Failed! ret:" + HexStr.from_int(ret)
            print(error_message)
            return []

        ret = fg_interface.GetNumDevices(nDeviceNum)
        if MV_FG_SUCCESS != ret:
            error_message = "Get Num Devices Failed! ret:" + HexStr.from_int(ret)
            print(error_message)
            return []

        if 0 == nDeviceNum.value:
            error_message = "No Device!"
            print(error_message)
            return []

        if bChanged.value:
            for i in range(0, nDeviceNum.value):
                stDeviceInfo = MV_FG_DEVICE_INFO()
                memset(byref(stDeviceInfo), 0, sizeof(stDeviceInfo))
                ret = fg_interface.GetDeviceInfo(i, stDeviceInfo)
                if MV_FG_SUCCESS != ret:
                    error_message = "Get Device Info Failed! ret:" + HexStr.from_int(ret)
                    print(error_message)
                    return []

                device_info = DeviceInfo(
                    mv_device_info=stDeviceInfo
                )
                _device_list.append(device_info)

            return _device_list

    def open_device(self, interface: FGInterface, device_index: int) -> FGDevice:
        # TODO : 이미 열린 장치인지 확인하는 로직 추가하기.

        _fg_device = FGDevice()
        ret = _fg_device.OpenDevice(interface, device_index)
        if MV_FG_SUCCESS != ret:
            error_message = "Open Device Failed! ret:" + HexStr.from_int(ret)
            print(error_message)
            return

        # TODO : 트리거 모드 등 설정 필요.
        print(f"Open Device Success! index:{device_index}")
        return _fg_device

    def close_device(self, fg_device: FGDevice) -> bool:
        ret = fg_device.CloseDevice()
        if MV_FG_SUCCESS != ret:
            error_message = "Close Device Failed! ret:" + HexStr.from_int(ret)
            print(error_message)
            return False
        return True

    def save_bmp(self,
                 image_info: MV_FG_INPUT_IMAGE_INFO,
                 image_processor: FGImageProcess,
                 thread_lock: Optional[threading.Lock],
                 filename: str = "image",
                 ) -> Optional[str]:

        if isinstance(thread_lock, threading.Lock):
            thread_lock.acquire()

        file_path = filename + ".bmp"
        stBmpInfo = MV_FG_SAVE_BITMAP_INFO()
        memset(byref(stBmpInfo), 0, sizeof(MV_FG_SAVE_BITMAP_INFO))
        BmpBuffer = (c_ubyte * (image_info.nWidth * image_info.nHeight * 3 + 2048))()
        BmpBufferSize = image_info.nWidth * image_info.nHeight * 3 + 2048

        stBmpInfo.stInputImageInfo = image_info
        stBmpInfo.pBmpBuf = BmpBuffer
        stBmpInfo.nBmpBufSize = BmpBufferSize
        stBmpInfo.enCfaMethod = MV_FG_CFA_METHOD_OPTIMAL

        ret = image_processor.SaveBitmap(stBmpInfo)
        if MV_FG_SUCCESS != ret:
            return None

        file = open(file_path.encode('ascii'), 'wb+')
        img_data = (c_ubyte * stBmpInfo.nBmpBufLen)()
        cdll.msvcrt.memcpy(byref(img_data), stBmpInfo.pBmpBuf, stBmpInfo.nBmpBufLen)
        file.write(img_data)
        file.close()

        if isinstance(thread_lock, threading.Lock):
            thread_lock.release()

        if MV_FG_SUCCESS != ret:
            print("Save Bmp Failed! ret:" + HexStr.from_int(ret))
            return None

        return file_path
