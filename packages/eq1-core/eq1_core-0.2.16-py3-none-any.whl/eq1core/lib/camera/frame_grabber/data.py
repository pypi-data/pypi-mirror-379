import dataclasses
from MVFGControl_class import *


class InterfaceInfo:
    """
    * hikvision sample code 를 참고하여 작성된 코드입니다.
    * 프레임그래버 인터페이스 정보를 담는 데이터 클래스입니다.
    """
    DISPLAY_NAME = "chDisplayName"
    INTERFACE_ID = "chInterfaceID"
    SERIAL_NUMBER = "chSerialNumber"

    def __init__(self, mvfg_interface_info: MV_FG_INTERFACE_INFO):
        interface_type = mvfg_interface_info.nTLayerType
        if interface_type == MV_FG_CXP_INTERFACE:
            self.title = "CXP"
            self.interface_info = mvfg_interface_info.IfaceInfo.stCXPIfaceInfo
        elif interface_type == MV_FG_GEV_INTERFACE:
            self.title = "GEV"
            self.interface_info = mvfg_interface_info.IfaceInfo.stGEVIfaceInfo
        elif interface_type == MV_FG_CAMERALINK_INTERFACE:
            self.title = "CML"
            self.interface_info = mvfg_interface_info.IfaceInfo.stCMLIfaceInfo
        elif interface_type == MV_FG_XoF_INTERFACE:
            self.title = "XoF"
            self.interface_info = mvfg_interface_info.IfaceInfo.stXoFIfaceInfo
        else:
            self.title = "Unknown"
            self.interface_info = None

        self.display_name: str = self.get_field_info(self.DISPLAY_NAME)
        self.interface_id: str = self.get_field_info(self.INTERFACE_ID)
        self.serial_number: str = self.get_field_info(self.SERIAL_NUMBER)

    def get_field_info(self, field_name: str) -> str:
        self.field_value = ""
        for per in getattr(self.interface_info, field_name):
            if per == 0:
                break
            self.field_value += chr(per)

        return self.field_value

    def __repr__(self):
        return f"{self.title} {self.display_name}|{self.interface_id}|{self.serial_number}"

    def __str__(self):
        return self.__repr__()


class DeviceInfo:
    """
    * hikvision sample code 를 참고하여 작성된 코드입니다.
    * 프레임그래버 디바이스 정보를 담는 데이터 클래스입니다.
    """

    def __init__(self, mv_device_info: MV_FG_DEVICE_INFO):
        self._interface_type: str = None
        self._user_defined_name: str = None
        self._model_name: str = None
        self._serial_number: str = None

        device_type = mv_device_info.nDevType
        if MV_FG_CXP_DEVICE == device_type:
            _info = mv_device_info.DevInfo.stCXPDevInfo
            self._interface_type = "CXP"
        elif MV_FG_GEV_DEVICE == device_type:
            _info = mv_device_info.DevInfo.stGEVDevInfo
            self._interface_type = "GEV"
        elif MV_FG_CAMERALINK_DEVICE == device_type:
            _info = mv_device_info.DevInfo.stCMLDevInfo
            self._interface_type = "CML"
        elif MV_FG_XoF_DEVICE == device_type:
            _info = mv_device_info.DevInfo.stXoFDevInfo
            self._interface_type = "XoF"
        else:
            raise ValueError("Unknown device type")

        self._user_defined_name = self._decode(_info.chUserDefinedName)
        self._model_name = self._decode(_info.chModelName)
        self._serial_number = self._decode(_info.chSerialNumber)

    @staticmethod
    def _decode(char_array):
        device_string = ""
        for per in char_array:
            if per == 0:
                break
            device_string += chr(per)
        return device_string

    def __repr__(self):
        return f"{self._interface_type} {self._user_defined_name}|{self._model_name}|{self._serial_number}"

    def __str__(self):
        return self.__repr__()

    @property
    def serial_number(self):
        return self._serial_number


class HexStr:
    """
    * hikvision sample code 를 참고하여 작성된 코드입니다.
    * 반환된 오류 코드를 16 진수로 표시합니다.
    """
    @classmethod
    def from_int(cls, num: int) -> str:
        char_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        hex_string = ""
        if num < 0:
            num = num + 2 ** 32
        while num >= 16:
            digit = num % 16
            hex_string = char_dict.get(digit, str(digit)) + hex_string
            num //= 16
        hex_string = char_dict.get(num, str(num)) + hex_string

        return hex_string
