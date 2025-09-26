import time
import threading
import dataclasses
from typing import List
import socket
from typing import Optional, Tuple


@dataclasses.dataclass(frozen=True)
class SendData:
    cmd: str
    data: List[str] = dataclasses.field(default_factory=list)

    def to_bytes(self) -> bytes:
        result = self.cmd
        for datum in self.data:
            result += f"#{datum}"

        return result.encode('utf-8')


class TCPClient:
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


class MockClient(threading.Thread):
    def __init__(self):
        super().__init__()
        self._client = TCPClient(
            address="0.0.0.0",
            port=1234,
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
                    "\n2. next"
                    "\n3. new"
                    "\n=============================="
                )

            case 'next':
                client.send_data(
                    SendData(
                        cmd='NEXT',
                        data=[]
                    ).to_bytes()
                )

            case 'new':
                client.send_data(
                    SendData(
                        cmd='NEW',
                        data=[]
                    ).to_bytes()
                )
            