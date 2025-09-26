from .logger import AppLogger
import traceback
import threading
import time
import struct
import numpy as np
from typing import List


def crop_image(image: np.ndarray, roi_xywh: List[int]) -> np.ndarray:
    x, y, w, h = roi_xywh
    return image[y:y+h, x:x+w]


class Numeric:
    @classmethod
    def convert_int_to_bytes(cls, value: int, length: int, byteorder: str = "big"):
        assert isinstance(value, int), f"Value must be int type, but : {value}[{type(value)}"
        return value.to_bytes(length, byteorder)

    @classmethod
    def convert_bytes_to_int(cls, value: bytes, byteorder: str = "big"):
        assert isinstance(value, bytes), f"Value must be bytes type, but : {value}[{type(value)}"
        return int.from_bytes(value, byteorder)

    @classmethod
    def convert_float_to_bytes(cls, value: float):
        assert isinstance(value, float), f"Value must be float type, but : {value}[{type(value)}]"
        # return struct.pack('!f', value)
        # float 연산 시 부동소수점 문제로 좌표값이 정확하지 않아 100배하여 int로 전달하기로 협의하였음. 음수값이 포함되어 있어 !i로 변경.
        return struct.pack('!i', int(value*100))

    @classmethod
    def convert_bytes_to_float(cls, value: bytes):
        assert isinstance(
            value, bytes), f"Value must be bytes type, but : {value}[{type(value)}]"
        return struct.unpack('!f', value)[0]
    

class DBAsyncWriter(threading.Thread):
    """
    한독 프로젝트와 같이 실시간 고속 검사 환경에서 프레임 단위로 DB에 트랜젝션을 날리니까
    시간이 지나면서 프로그램이 비정상 동작을 하는 문제가 발생함
    이를 해결하기 위해 트랜젝션이 많이 발생하는 부분을 비동기로 처리하는 클래스를 생성함
    """

    def __init__(self, create_bulk: callable):
        super().__init__()
        self.stop_flag = threading.Event()
        self.wait_list: List = []
        self.time_interval_msec: int = 1000  # TODO : config.
        self.last_executed_time = time.time()

        self.create_bulk = create_bulk

        AppLogger.write_debug(self, 'DBAsyncWriter created')

    def put(self, data):
        self.wait_list.append(data)

    def stop(self):
        self.stop_flag.set()

    def run(self):
        self.stop_flag.clear()

        while not self.stop_flag.is_set():
            time.sleep(0.01)
            if len(self.wait_list) == 0:
                continue

            if time.time() - self.last_executed_time < self.time_interval_msec / 1000:
                continue

            try:
                AppLogger.write_debug(
                    self, f'DBAsyncWriter write {len(self.wait_list)} data to db', print_to_terminal=True)
                self.create_bulk(self.wait_list)
                AppLogger.write_info(
                    self, f'DBAsyncWriter: {len(self.wait_list)}개의 검사 결과를 DB에 성공적으로 저장했습니다.', print_to_terminal=True)
            except Exception as e:
                AppLogger.write_error(
                    self, f'DBAsyncWriter failed to write data to db: {e} {traceback.format_exc()}', print_to_terminal=True)

            self.wait_list = []
            self.last_executed_time = time.time()
