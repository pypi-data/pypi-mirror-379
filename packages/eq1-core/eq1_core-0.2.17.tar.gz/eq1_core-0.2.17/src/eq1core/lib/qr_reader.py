import time
import threading
from typing import Any, Optional
from eq1core.logger import AppLogger
from eq1core.configure import Params
from eq1core.lib.communication.protocol.ethernet import TCPClient
from eq1core.lib.communication.protocol.factory import create_protocol


class QrEvent:
    def on_received_qr_info(self, data: Any):
        pass

    def timeout_qr_info(self):
        pass


class QrReader(threading.Thread):
    def __init__(self, network_config: Params, event_callback: QrEvent, timeout: Optional[int] = 3, singleshot: bool = True):
        super().__init__()

        self.network_config = network_config
        self.event_callback = event_callback
        self._protocol = create_protocol(
            params=self.network_config
        )
        if not isinstance(self._protocol, TCPClient):
            raise ValueError(f"Invalid qr protocol. expected {TCPClient} but {self._protocol}")

        self._timeout = timeout  # sec
        self._stop_flag = threading.Event()
        self._is_connected = False
        self._singleshot = singleshot

    def stop(self):
        AppLogger.write_info(self, f"QR Reader Stop !!", print_to_terminal=True)
        self._stop_flag.set()

    def timeout_check(self, started_at):
        if self._timeout is None:
            return
        if time.time() - started_at > self._timeout:
            AppLogger.write_debug(self, f"current time ({time.time()}) - started_at ({started_at}) > timeout sec ({time.time()-started_at})", print_to_terminal=True)
            self.event_callback.timeout_qr_info()
            self.stop()

    def connect_to_qr_reader(self):
        if self._protocol.connect():
            AppLogger.write_info(self, f'Connected to QR Reader. {self._protocol._address}:{self._protocol._port}', print_to_terminal=True)
            self._is_connected = True

    def read_from_qr_reader(self):
        try:
            res, data = self._protocol.read()
            if not res:
                self._is_connected = False

            if data is not None:
                self.event_callback.on_received_qr_info(data.decode('utf-8'))
                if self._singleshot:
                    self.stop()
                AppLogger.write_debug(self, f"Received QR Data: {data.decode('utf-8')}", print_to_terminal=True)
        except Exception as e:
            self._is_connected = False

    def run(self):
        AppLogger.write_info(self, f"QR Reader Start !!", print_to_terminal=True)
        self._stop_flag.clear()

        started_at = time.time()
        while not self._stop_flag.is_set():
            self.timeout_check(started_at)
            if not self._is_connected:
                self.connect_to_qr_reader()
            else:
                self.read_from_qr_reader()

