import time
import socket
import threading
import dataclasses


@dataclasses.dataclass
class PacketStructure:
    header: int
    length: int
    sync_no: int
    reserved: int
    frame_type: int
    data: bytes

    @classmethod
    def from_bytes(cls, data: bytes):
        return cls(
            header=int(data[0]),
            length=int(data[1]),
            sync_no=int(data[2]),
            reserved=int(data[3]),
            frame_type=int(data[4]),
            data=data[5:]
        )

    def to_bytes(self):

        return (int(self.header).to_bytes(1, 'big')
                + int(self.length).to_bytes(1, 'big')
                + int(self.sync_no).to_bytes(1, 'big')
                + int(self.reserved).to_bytes(1, 'big')
                + int(self.frame_type).to_bytes(1, 'big')
                + int(0).to_bytes(1, 'big')
                + self.data)


class FrameType:
    GET_SLAVE_INFO = 0x01
    GET_INPUT = 0xC0
    GET_OUTPUT = 0xC5
    GET_IO_LEVEL = 0xCA

    SET_OUTPUT = 0xC6
    SET_IO_LEVEL = 0xCB


class MockIoBoard(threading.Thread):
    def __init__(self):
        super().__init__()
        self.ip = '127.0.0.1'
        self.port = 3001
        self.is_stop = False

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip, self.port))

        self.input_state = b'\x00\x00\x00\x00\x00\x00\x00\x00'

        print('MockIoBoard is initialized.')

    def stop(self):
        self.socket.close()
        self.is_stop = True

    def run(self):
        while not self.is_stop:
            try:
                time.sleep(0.001)
                data, addr = self.socket.recvfrom(1024)
                data = PacketStructure.from_bytes(data)
                if data.frame_type == FrameType.GET_SLAVE_INFO:
                    self.socket.sendto(
                        int(0).to_bytes(1, 'big') + int(156).to_bytes(1, 'big') + b'abcdefg',
                        addr
                    )
                if data.frame_type == FrameType.GET_INPUT:
                    send_data = PacketStructure(
                        header=0xAA,
                        length=12,
                        sync_no=data.sync_no,
                        reserved=0x00,
                        frame_type=FrameType.GET_INPUT,
                        data=self.input_state
                    ).to_bytes()
                    self.socket.sendto(
                        send_data,
                        addr
                    )
            except Exception as e:
                print('err', e)


class Main(threading.Thread):
    def __init__(self):
        super().__init__()
        self.mock_io_board = MockIoBoard()
        self.mock_io_board.start()

    def run(self):
        while True:
            time.sleep(0.001)
            print('press "q" to exit.\n')
            x = input('select number [0 ~ 7]. \n')
            if len(x) == 0:
                continue

            if x == 'q':
                break

            y = input('select [1 (on) / 0 (off)]\n')
            if y not in ['1', '0']:
                print('잘못 입력하셨습니다. 1 또는 0 중에 선택해주세요.')
                continue

            try:
                port_number = int(x)
                print('port_number', port_number)
                data = bytearray(b'\x00\x00\x00\x00')

                # >> 입력 8포트 이상인 경우 아래 코드로 테스트할 것.
                # data[port_number//8] = 1 << (port_number % 8)

                # >> 입력 8포트 경우 아래 코드로 테스트 가능.
                data[0] = self.mock_io_board.input_state[0]
                if y == '1':
                    data[0] = data[0] | int(1) << (port_number % 8)
                else:
                    data[0] = data[0] & ~(int(1) << (port_number % 8))
                # <<

                data += b'\x00\x00\x00\x00'
                self.mock_io_board.input_state = data
                print('self.mock_io_board.input_state', self.mock_io_board.input_state)

            except Exception as e:
                print('>> error!! ', e)

        self.mock_io_board.stop()
        self.mock_io_board.join()


if __name__ == "__main__":
    app = Main()
    app.start()
