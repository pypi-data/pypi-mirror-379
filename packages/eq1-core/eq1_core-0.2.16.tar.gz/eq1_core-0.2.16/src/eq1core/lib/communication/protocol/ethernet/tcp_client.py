import socket
from typing import Optional, Tuple
from eq1core.lib.communication.protocol.interface import Protocol


class TCPClient(Protocol):
    def __init__(self, address: str, port: int, timeout: int = 0.1):
        self._address = address
        self._port = port
        self._timeout = timeout
        self._socket = None

    def connect(self) -> bool:
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.settimeout(self._timeout)
            self._socket.connect((self._address, self._port))
            return True
        except (ConnectionRefusedError, OSError) as e:
            self._socket.close()
            self._socket = None
            return False

    def disconnect(self):
        try:
            self._socket.close()
            print('client disconnected')
        except Exception as e:
            pass

    def send(self, data: bytes) -> bool:
        try:
            self._socket.send(data)
            return True
        except BrokenPipeError as be:
            print(f'failed to send data. {be}')
            return False
        except AttributeError as ae:
            print(f'failed to send data. {ae}')
            return False

    def read(self) -> Tuple[bool, Optional[bytes]]:
        try:
            data = self._socket.recv(1024)
            if not data:
                raise ConnectionResetError

            return True, data
        except socket.timeout as te:
            return True, None
        except ConnectionResetError as ce:
            # print(f'failed to read data. {ce}')
            return False, None
        except AttributeError as ae:
            # print(f'failed to read data. {ae}')
            return False, None
