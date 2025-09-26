import socket
import threading
import time
import json
import traceback
import logging
from typing import Optional, Tuple
from eq1core.lib.communication.protocol.interface import Protocol


class TCPServer(Protocol):
    def __init__(self, address: str, port: int, timeout: int = 1):
        self._address = address
        self._port = port
        self._timeout = timeout
        self._socket = None
        self._conn = None
        
        # 자체 로거 설정
        self._logger = logging.getLogger(f"TCPServer_{address}:{port}")
        self._logger.setLevel(logging.INFO)
        
        # 핸들러가 없으면 추가
        if not self._logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self._logger.addHandler(handler)

    def is_connected(self) -> bool:
        return self._conn is not None

    def connect(self) -> bool:
        if self._conn is not None:
            return True

        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Address already in use Error 방지.
            self._socket.bind((self._address, self._port))
            self._socket.settimeout(self._timeout)
            self._socket.listen(1)  # Client 동시 연결 수 1:1 로 제한 설정.
            self._conn, _ = self._socket.accept()
            self._conn.settimeout(self._timeout)
            
            self._logger.info(f"TCP 서버 연결 성공: {self._address}:{self._port}")

            return True
        except socket.timeout as te:
            self._logger.warning(f"연결 타임아웃: {self._address}:{self._port}")
            self.disconnect()

            return False
        except socket.error as se:
            self._logger.error(f"socket error 발생. {se}. {self._address}:{self._port}. retry after {self._timeout}sec.")
            self.disconnect()
            time.sleep(self._timeout)
            return False
        except Exception as e:
            self._logger.error(f"failed to connect {self._address}:{self._port}... {traceback.format_exc()}. retry after {self._timeout}sec.")
            self.disconnect()
            time.sleep(self._timeout)
            return False

    def disconnect(self):
        try:
            if self._conn is not None:
                self._conn.close()
            if self._socket is not None:
                self._socket.close()
            self._conn = None
            self._socket = None
            self._logger.info(f"TCP 서버 연결 해제: {self._address}:{self._port}")
        except Exception as e:
            self._logger.warning(f"연결 해제 중 오류 발생: {e}")

    def send(self, data: bytes) -> bool:
        try:
            self._conn.send(data)
            self._logger.debug(f"데이터 전송 성공: {len(data)} bytes")
            return True
        except socket.timeout as te:
            self._logger.warning("데이터 전송 타임아웃")
            return True
        except BrokenPipeError as be:
            self._logger.error(f'데이터 전송 실패 (BrokenPipeError): {be}')
            return False
        except AttributeError as ae:
            self._logger.error(f'데이터 전송 실패 (AttributeError): {ae}')
            return False

    def read(self) -> Tuple[bool, Optional[bytes]]:
        try:
            data = self._conn.recv(1024)
            if not data:
                raise ConnectionResetError

            self._logger.debug(f"데이터 수신 성공: {len(data)} bytes")
            return True, data
        except socket.timeout as te:
            return True, None
        except ConnectionResetError as ce:
            self._logger.error(f'데이터 수신 실패 (ConnectionResetError): {ce}')
            return False, None
        except AttributeError as ae:
            self._logger.error(f'데이터 수신 실패 (AttributeError): {ae}')
            return False, None
