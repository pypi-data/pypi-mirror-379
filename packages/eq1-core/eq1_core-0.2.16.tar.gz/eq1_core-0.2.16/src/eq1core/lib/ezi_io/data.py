from typing import Literal, Tuple, Optional
from dataclasses import dataclass
from eq1core.lib.ezi_io.protocol import UdpClient


class ErrorCode:
    FRAME_TYPE_ERROR = 0x80
    DATA_LENGTH_ERROR = 0x81
    FRAME_SPECIFICATION_ERROR = 0x82
    CRC_ERROR = 0xAA


class FrameType:
    GET_SLAVE_INFO = 0x01
    GET_INPUT = 0xC0
    GET_OUTPUT = 0xC5
    GET_IO_LEVEL = 0xCA

    SET_OUTPUT = 0xC6
    SET_IO_LEVEL = 0xCB


class PinMap:
    # TODO : change pin number according to the project
    # input 0~7
    NEXT = 1

    # output 8~15
    OK = 10
    NG = 11
    ERROR = 12

    LED = 8
    CYLINDER = 9


class Numeric:
    @classmethod
    def convert_int_to_bytes(cls, value: int, length: int, byteorder: Literal["little", "big"] = "big"):
        assert isinstance(value, int), f"Value must be int type, but : {value}[{type(value)}"
        return value.to_bytes(length, byteorder)

    @classmethod
    def convert_bytes_to_int(cls, value: bytes, byteorder: Literal["little", "big"] = "big"):
        assert isinstance(value, bytes), f"Value must be bytes type, but : {value}[{type(value)}"
        return int.from_bytes(value, byteorder)


@dataclass
class PacketStructure:
    sync_no: int
    frame_type: int
    data: bytes = b''

    def to_bytes(self):
        header = Numeric.convert_int_to_bytes(value=0xAA, length=1)
        sync_no = Numeric.convert_int_to_bytes(value=self.sync_no, length=1)
        reserved = Numeric.convert_int_to_bytes(value=0x00, length=1)
        frame_type = Numeric.convert_int_to_bytes(value=self.frame_type, length=1)
        data = self.data
        length = Numeric.convert_int_to_bytes(value=len(sync_no + reserved + frame_type + data), length=1)

        return header + length + sync_no + reserved + frame_type + data


class EziIoSendData:
    sync_no = 0

    @classmethod
    def get_next_sync_no(cls):
        cls.sync_no += 1
        if cls.sync_no > 250:
            cls.sync_no = 0
        return cls.sync_no

    @classmethod
    def get_slave_info(cls):
        return PacketStructure(sync_no=cls.get_next_sync_no(),
                               frame_type=FrameType.GET_SLAVE_INFO).to_bytes()

    @classmethod
    def get_input(cls):
        return PacketStructure(sync_no=cls.get_next_sync_no(),
                               frame_type=FrameType.GET_INPUT).to_bytes()

    @classmethod
    def get_output(cls):
        return PacketStructure(sync_no=cls.get_next_sync_no(),
                               frame_type=FrameType.GET_OUTPUT).to_bytes()

    @classmethod
    def get_io_level(cls):
        return PacketStructure(sync_no=cls.get_next_sync_no(),
                               frame_type=FrameType.GET_IO_LEVEL).to_bytes()

    @classmethod
    def set_io_level(cls, level: Optional[int] = 0):
        """
        0: Low Active Level (Latch: Falling edge)
        1: High Active Level (Latch: Rising edge)

        만약 포트 개별 설정이 필요한 경우 코드 수정 필요
        """
        if level == 0:
            data = b'\x00\x00\x00\x00'
        else:
            data = b'\xff\xff\xff\xff'

        return PacketStructure(sync_no=cls.get_next_sync_no(),
                               frame_type=FrameType.SET_IO_LEVEL,
                               data=data).to_bytes()

    @classmethod
    def set_output(cls, port_number: int):
        """
        :param port_number: 0 ~ 31

        ezi-io 보드의 SetOutput 요청 데이터 구조는 0~63 까지의 비트맵으로 구성되어 있음.

        포트를 on/off 하는 포트가 분리되어 있으며 동시 신호 시 off 가 우선권을 갖음.

        b'\x00\x00\x00\x00\x00\x00\x00\x00'
           ~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~
         bit=1 위치 on(set)  bit=1 위치 off(reset)
        """
        data = bytearray(b'\x00\x00\x00\x00')
        data[port_number//8] = 1 << (port_number % 8)
        data += b'\x00\x00\x00\x00'

        return PacketStructure(sync_no=cls.get_next_sync_no(),
                               frame_type=FrameType.SET_OUTPUT,
                               data=data).to_bytes()

    @classmethod
    def reset_output(cls, port_number: int):
        """
        :param port_number: 0 ~ 31

        ezi-io 보드의 SetOutput 요청 데이터 구조는 0~63 까지의 비트맵으로 구성되어 있음.

        포트를 on/off 하는 포트가 분리되어 있으며 동시 신호 시 off 가 우선권을 갖음.

        b'\x00\x00\x00\x00\x00\x00\x00\x00'
           ~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~
         bit=1 위치 on(set)  bit=1 위치 off(reset)
        """
        data = bytearray(b'\x00\x00\x00\x00')
        data[port_number//8] = 1 << (port_number % 8)
        data = b'\x00\x00\x00\x00' + data

        return PacketStructure(sync_no=cls.get_next_sync_no(),
                               frame_type=FrameType.SET_OUTPUT,
                               data=data).to_bytes()


class EziIoReceivedData:
    @classmethod
    def from_bytes(cls, data: bytes) -> Tuple[Optional[int], Optional[int]]:
        if data is None or len(data) < 6:
            return None, None

        header = data[0]
        length = data[1]
        sync_no = data[2]
        reserved = data[3]
        frame_type = data[4]
        err_code = data[5]

        if err_code != 0:
            # AppLogger.write_error(cls, f"ezi io request failed ! "
            #                             f"frame_type : {frame_type}, error code : {err_code}, sync_no: {sync_no}")
            return None, None

        if frame_type == FrameType.GET_SLAVE_INFO:
            slave_type = data[6]
            message = data[7:]

            return frame_type, slave_type

        elif frame_type == FrameType.GET_INPUT:
            inputs = data[6:10]  # pin 0~31

            return frame_type, inputs

        elif frame_type == FrameType.GET_OUTPUT:
            outputs = data[6:10]  # pin 0~31

            return frame_type, outputs

        elif frame_type == FrameType.SET_OUTPUT:
            pass

        elif frame_type == FrameType.GET_IO_LEVEL:
            pass

        elif frame_type == FrameType.SET_IO_LEVEL:
            pass


if __name__ == "__main__":
    inputs_sock = UdpClient("192.168.0.4", 3001)
    outputs_sock = UdpClient("192.168.0.2", 3001)

    inputs_sock.send(EziIoSendData.get_slave_info())
    print(inputs_sock.receive())
    print(EziIoReceivedData.from_bytes(data=inputs_sock.receive()[0]))

    outputs_sock.send(EziIoSendData.get_slave_info())
    print(outputs_sock.receive())
    print(EziIoReceivedData.from_bytes(data=outputs_sock.receive()[0]))
