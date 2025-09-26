import os
import time
import socket
import threading

# 데이터베이스 환경변수 설정 (eq1core 모듈 초기화 전에 설정)
os.environ["DB_URL"] = "mysql+pymysql://crefle:passwd@localhost:3307/eq1"
os.environ["LOG_PATH"] = "./public/logs"

from eq1core import EqPlugin, Signal
from eq1_network.data import SendData, ReceivedData
from eq1_network.examples.data.dataset import MessageType, CommandType


class UISendData(SendData):
    def __init__(self, cmd: str = "", data: list = None):
        self.cmd = cmd
        self.data = data or []
    
    def to_bytes(self) -> bytes:
        return f"{self.cmd} {' '.join(self.data)}".encode('utf-8')


class UIReceivedData(ReceivedData):
    def __init__(self, cmd: str = "", data: list = None):
        self.cmd = cmd
        self.data = data or []
    
    @classmethod
    def from_bytes(cls, data: bytes):
        try:
            parts = data.decode('utf-8').split(' ')
            return cls(cmd=parts[0] if parts else "", data=parts[1:] if len(parts) > 1 else [])
        except:
            return cls()


class UICommunicator(EqPlugin):
    def __init__(self, net_config, net_id=None):
        EqPlugin.__init__(self)
        
        self._address = net_config.get('address', 'localhost')
        self._port = net_config.get('port', 8888)
        self._net_id = net_id
        
        self._socket = None
        self._conn = None
        self._server_thread = None
        self._stop_flag = threading.Event()
        
        self.ui_custom_signal = Signal(UIReceivedData)

    def start(self):
        return self._start_server()
    
    def stop(self):
        self._stop_server()
    
    def disconnect(self):
        self.stop()

    def is_connected(self):
        return self._conn is not None

    def _start_server(self):
        if self.is_connected():
            print(f"⚠️ [TCP서버] 이미 실행 중 (ID: {self._net_id})")
            return True
            
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self._socket.bind((self._address, self._port))
            self._socket.settimeout(1)
            self._socket.listen(1)
            
            print(f"🚀 [TCP서버] 시작: {self._address}:{self._port}")
            
            self._stop_flag.clear()
            self._server_thread = threading.Thread(target=self._server_loop, daemon=True)
            self._server_thread.start()
            
            return True
            
        except Exception as e:
            print(f"❌ [TCP서버] 시작 실패: {e}")
            self._cleanup()
            return False

    def _stop_server(self):
        self._stop_flag.set()
        
        if self._conn:
            try:
                self._conn.close()
            except:
                pass
            self._conn = None
        
        self._cleanup()
        
        if self._server_thread and self._server_thread.is_alive():
            self._server_thread.join(timeout=2)
        
        print("📝 [TCP서버] 중지 완료")

    def _cleanup(self):
        if self._socket:
            try:
                self._socket.close()
            except:
                pass
            self._socket = None

    def _server_loop(self):
        while not self._stop_flag.is_set():
            try:
                if not self._conn:
                    self._conn, addr = self._socket.accept()
                    self._conn.settimeout(1)
                    print(f"📱 [연결] 클라이언트 접속: {addr[0]}:{addr[1]}")
                
                data = self._conn.recv(1024)
                if not data:
                    print("📝 [연결] 클라이언트 연결 해제")
                    self._conn.close()
                    self._conn = None
                    continue
                
                received_data = UIReceivedData.from_bytes(data)
                print(f"📨 [수신] {data.decode('utf-8', errors='ignore')}")
                
                self.ui_custom_signal.emit(received_data)
                self._process_command(received_data)
                
            except socket.timeout:
                continue
            except Exception as e:
                if not self._stop_flag.is_set():
                    print(f"❌ [오류] 서버 루프: {e}")
                break
        
        if self._conn:
            try:
                self._conn.close()
            except:
                pass
            self._conn = None

    def _process_command(self, data: UIReceivedData):
        if not data.cmd:
            self._send_response("data_received", [])
            return

        # 명령어별 처리
        if data.cmd == CommandType.NEXT.value:
            self._send_response("next_processed", [time.strftime("%Y%m%d%H%M%S")])
        elif data.cmd == CommandType.NEW.value:
            self._send_response("new_processed", ["signal_emitted"])
        elif data.cmd == CommandType.STATUS.value:
            self._send_response("status_processed", [f"server_ready_port_{self._port}"])
        elif data.cmd.startswith(MessageType.DATA.value):
            # DATA#1 2 3 -> [1, 2, 3]
            values = (data.cmd[5:] + " " + " ".join(data.data)).split() if data.cmd.startswith("DATA#") else (data.data or [])
            self._send_response("data_processed", [str(values)])
        elif data.cmd.startswith(CommandType.INT.value):
            # INT#1 2 3 -> [1, 2, 3]
            values = (data.cmd[4:] + " " + " ".join(data.data)).split() if data.cmd.startswith("INT#") else (data.data or [])
            self._send_response("int_processed", [str(values)])
        else:
            # 커스텀: cmd + data (데이터가 없으면 cmd만)
            if data.data:
                self._send_response("custom_processed", [data.cmd, str(data.data)])
            else:
                self._send_response("custom_processed", [data.cmd])

    def _send_response(self, cmd: str, data: list = None):
        if not self._conn:
            return False
            
        try:
            response = UISendData(cmd=cmd, data=data or [])
            self._conn.send(response.to_bytes())
            print(f"✅ [송신] {response.to_bytes().decode('utf-8')}")
            return True
        except Exception as e:
            print(f"❌ [송신실패] {e}")
            return False

    def get_server_info(self):
        return {
            "is_running": self.is_connected(),
            "address": self._address,
            "port": self._port,
            "net_id": self._net_id
        }