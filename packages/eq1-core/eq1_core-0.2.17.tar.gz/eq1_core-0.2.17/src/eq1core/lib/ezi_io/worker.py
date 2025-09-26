import abc
import time
import threading
import traceback
from eq1core.lib.ezi_io.data import EziIoSendData
from eq1core.lib.ezi_io.protocol import EthernetProtocol
from eq1core.lib.ezi_io.data import EziIoReceivedData, FrameType


class InputPinListenerEvent(abc.ABC):
    @abc.abstractmethod
    def on_received(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def on_failed_recv(self, *args, **kwargs):
        pass


class InputPinInfoRequester(threading.Thread):
    """
    Request Timeout 대기 시간 동안 발생할 수 있는 Input Port Read Delay 을 방지하기 위하여
    Requester Thread 를 굳이 Listener Thread 와 분리함.
    """
    def __init__(self, protocol: EthernetProtocol):
        super().__init__()
        self._stop_flag = threading.Event()
        self._protocol = protocol

    def stop(self):
        self._stop_flag.set()

    def run(self):
        self._stop_flag.clear()
        while not self._stop_flag.is_set():
            try:
                time.sleep(0.01)
                self._protocol.send(EziIoSendData.get_input())
            except Exception as e:
                print(e)


class InputPinInfoListener(threading.Thread):
    def __init__(self, protocol: EthernetProtocol, event_callback: InputPinListenerEvent):
        super().__init__()
        self._stop_flag = threading.Event()
        self._protocol = protocol
        self._event_callback = event_callback

    def stop(self):
        self._stop_flag.set()

    def run(self):
        if not isinstance(self._protocol, EthernetProtocol):
            raise ValueError(f"protocol must be instance of EthernetProtocol. but {self._protocol}")

        if not isinstance(self._event_callback, InputPinListenerEvent):
            raise ValueError(f"event_callback must be instance of InputPinListenerEvent. but {self._event_callback}")

        self._stop_flag.clear()
        while not self._stop_flag.is_set():
            try:
                time.sleep(0.001)
                recv_data = self._protocol.receive()
                if recv_data is None:
                    self._event_callback.on_failed_recv()
                    continue
                frame_type, inputs = EziIoReceivedData.from_bytes(recv_data[0])
                if frame_type != FrameType.GET_INPUT:
                    continue

                self._event_callback.on_received(inputs)
            except Exception as e:
                traceback.print_exc()
