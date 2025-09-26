import threading
import time
from eq1core.lib.communication.protocol.ethernet.tcp_server import TCPServer


class MockQrServer(threading.Thread):
    def __init__(self, address='127.0.0.1', port=9002):
        super().__init__()
        self.server = TCPServer(
            address=address,
            port=port
        )

    def run(self):
        print('mock qr server started')
        while True:
            try:
                time.sleep(1)
                res = self.server.connect()
                if not res:
                    continue

                res = self.server.send(b'hello')
                if not res:
                    self.server.disconnect()

            except Exception as e:
                pass


if __name__ == "__main__":
    app = MockQrServer()
    app.run()
