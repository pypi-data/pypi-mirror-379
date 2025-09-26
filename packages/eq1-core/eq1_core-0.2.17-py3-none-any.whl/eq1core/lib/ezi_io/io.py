import time
import traceback
import threading
from typing import Optional
from eq1core.lib.ezi_io.protocol import UdpClient
from eq1core.lib.ezi_io.data import EziIoSendData, EziIoReceivedData
from eq1core.lib.ezi_io.worker import InputPinListenerEvent, InputPinInfoRequester, InputPinInfoListener


class EziIoHandler(InputPinListenerEvent):
    def on_received(self, data: bytes):
        self._input_pin_info = data

    def on_failed_recv(self, *args, **kwargs):
        pass

    def __init__(self, input_ip: Optional[str] = None, output_ip: Optional[str] = None):
        super().__init__()
        try:
            self._input_pin_info = None
            self._input_pin_info_requester = None
            self._input_pin_info_listener = None
            self._input_port_network = None
            self._output_port_network = None

            if input_ip is not None:
                self._input_port_network = UdpClient(input_ip)
                self._input_port_network.send(EziIoSendData.get_slave_info())
                time.sleep(0.1)
                recv_data = self._input_port_network.receive()
                recv_data, addr = recv_data
                frame_type, slave_type = EziIoReceivedData.from_bytes(recv_data)
                print(f"input port network init\n"  # TODO : logging.  
                      f"addr: {addr}\n"
                      f"slave_info: {slave_type}")

            if output_ip is not None:
                self._output_port_network = UdpClient(output_ip)
                self._output_port_network.send(EziIoSendData.get_slave_info())
                time.sleep(0.1)
                recv_data, addr = self._output_port_network.receive()
                frame_type, slave_type = EziIoReceivedData.from_bytes(recv_data)
                print(f"output port network init\n" # TODO : logging.
                      f"addr: {addr}\n"
                      f"slave_info: {slave_type}")

            self.reset_all_port()

            self.start_all_workers()
        except Exception as e:
            print(f"failed to init EziIO: {traceback.format_exc()}")

    def start_all_workers(self):
        if self._input_port_network is not None:
            self._input_pin_info_requester = InputPinInfoRequester(protocol=self._input_port_network)
            self._input_pin_info_listener = InputPinInfoListener(protocol=self._input_port_network, event_callback=self)

            self._input_pin_info_requester.start()
            self._input_pin_info_listener.start()

    def stop_all_workers(self):
        if self._input_pin_info_requester is not None and self._input_pin_info_requester.is_alive():
            self._input_pin_info_requester.stop()
            self._input_pin_info_requester.join()

        if self._input_pin_info_listener is not None and self._input_pin_info_listener.is_alive():
            self._input_pin_info_listener.stop()
            self._input_pin_info_listener.join()

    def reset_all_port(self):
        if self._input_port_network is not None:
            self._input_port_network.send(EziIoSendData.set_io_level(0))

        if self._output_port_network is not None:
            self._output_port_network.send(EziIoSendData.set_io_level(0))
            for i in range(0, 32):
                self.turn_off_port(i)

    def is_port_on(self, port_num: int) -> Optional[bool]:
        """
        아래는 32개 input port 기준으로 설명되었으나 8개 단위로 동일하게 동작함.

        self._input_pin_info : 4 bytes (ex. b'\x00\x00\x00\x00')
                                              ~~~  ~~~  ~~~  ~~~
                                              0~7 8~15 16~23 24~31
                                         8개 포트 씩 묶어서 앞에서 부터 할당됨
                                         반대로 8개 비트 안에서는 내림차순으로 할당됨

        이진수로 변환해서 보면
            --> b'\b00000000\b00000000\b00000000\b00000000'
            --> input signal on 이 되면 1 로 변함
            -->  3번 포트 활성화 예시 =  b'\b00001000\b00000000\b00000000\b00000000'
            --> 22번 포트 활성화 예시 =  b'\b00000000\b00000000\b01000000\b00000000'

        self._input_pin_info[port_num//8] & (1 << (port_num % 8))
            --> 따라서 port_num//8 로 인덱싱하고
                port_num % 8 만큼 비트를 왼쪽으로 밀고
                두 값을 비트 연산 and 하면 둘 다 1인 경우 1 이상의 값이 나옴.

        """
        try:
            assert port_num >= 0, f"input port_num must be greater than -1 , but {port_num}"
            assert port_num <= 31, f"input port_num must be less than 32, but {port_num}"

            if self._input_pin_info is None:
                raise Exception("failed to read input pin info.")

            if (self._input_pin_info[port_num//8] & (1 << (port_num % 8))) != 0:
                return True
            return False
        except Exception as e:
            print(f"failed to read input port {port_num}: {traceback.format_exc()}")

    def turn_on_port(self, port_num: int, duration: Optional[float] = None) -> bool:
        """
        :param port_num:
        :param duration:  float, seconds
        :return:
        """
        try:
            assert port_num >= 0, f"output port_num must be greater than -1, but {port_num}"
            assert port_num <= 31, f"output port_num must be less than 32, but {port_num}"

            self._output_port_network.send(EziIoSendData.set_output(port_num))
            if duration is not None:
                timer = threading.Timer(duration, self.turn_off_port, args=[port_num])
                timer.start()
            return True
        except Exception as e:
            print(f"failed to turn on output port {port_num}: {traceback.format_exc()}")
            return False

    def turn_off_port(self, port_num: int) -> bool:
        try:
            assert port_num >= 0, f"output port_num must be greater than -1, but {port_num}"
            assert port_num <= 31, f"output port_num must be less than 32, but {port_num}"

            self._output_port_network.send(EziIoSendData.reset_output(port_num))
            return True
        except Exception as e:
            print(f"failed to turn off output port {port_num}: {traceback.format_exc()}")
            return False
