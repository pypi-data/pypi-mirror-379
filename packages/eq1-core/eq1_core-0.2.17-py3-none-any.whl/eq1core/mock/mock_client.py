import socket
import threading
import time
import configparser
from eq1core.configure import Params
from eq1core.utils import Numeric
from eq1core.lib.communication.protocol.ethernet.tcp_client import TCPClient
from eq1core.lib.communication.network import NetworkHandler, NetworkEvent
from eq1core.lib.communication.data import SendData


class MockClient(threading.Thread):
    def __init__(self):
        super().__init__()
        self._client = TCPClient(
            address="0.0.0.0",
            port=2002,
            timeout=1
        )
        self._stop_flag = threading.Event()
        self._connection_flag = False

    @property
    def client(self):
        return self._client

    def stop(self):
        self._stop_flag.set()

    def send_data(self, data: bytes):
        print(f'\nclient send data: {[hex(v) for v in data]}')
        self._connection_flag = self._client.send(data)

    def run(self):
        self._stop_flag.clear()

        while not self._stop_flag.is_set():
            if not self._connection_flag:
                self._connection_flag = self._client.connect()

            self._connection_flag, data = self._client.read()
            if data is not None:
                print(f'\nclient received data: {[hex(v) for v in data]}')


if __name__ == "__main__":
    client = MockClient()
    client.start()

    print('>> client', client)

    time.sleep(1)
    while True:
        key = input('\n press key : ')
        match key:
            case 'q':
                client.stop()
                break

            case 'h':
                print(
                    "\n========== key list =========="
                    "\n1. q"
                    "\n2. tray"
                    "\n3. macro"
                    "\n4. wide"
                    "\n5. ultra"
                    "\n6. product"
                    "\n=============================="
                )
            case 'tray':
                client.send_data(
                    Numeric.convert_int_to_bytes(0xAA, length=1)
                    + Numeric.convert_int_to_bytes(0x71, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=2)
                )
            case 'macro':
                client.send_data(
                    Numeric.convert_int_to_bytes(0xAA, length=1)
                    + Numeric.convert_int_to_bytes(0x81, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=2)
                )
            case 'wide':
                client.send_data(
                    Numeric.convert_int_to_bytes(0xAA, length=1)
                    + Numeric.convert_int_to_bytes(0x83, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=2)
                )
            case 'ultra':
                client.send_data(
                    Numeric.convert_int_to_bytes(0xAA, length=1)
                    + Numeric.convert_int_to_bytes(0x85, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=2)
                )
            case 'product':
                client.send_data(
                    Numeric.convert_int_to_bytes(0xAA, length=1)
                    + Numeric.convert_int_to_bytes(0x75, length=1)
                    + Numeric.convert_int_to_bytes(0x09, length=2)
                    + Numeric.convert_int_to_bytes(0x10, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=1)
                    + Numeric.convert_int_to_bytes(0x00, length=1)
                )
