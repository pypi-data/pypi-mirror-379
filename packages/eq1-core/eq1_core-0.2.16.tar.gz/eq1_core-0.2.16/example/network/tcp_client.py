import os
import time

# 데이터베이스 환경변수 설정 (eq1core 모듈 초기화 전에 설정)
os.environ["DB_URL"] = "mysql+pymysql://crefle:passwd@localhost:3307/eq1"
os.environ["LOG_PATH"] = "./public/logs"

from eq1_network.protocols.ethernet.tcp_client import TCPClient


class MockClient(TCPClient):
    def __init__(self, address: str = "localhost", port: int = 1235):
        super().__init__(address, port, timeout=1.0)
        self._last_response = None
    
    def send_data(self, data: bytes):
        """서버로 데이터 전송"""
        try:
            if self.send(data):
                print(f'✅ 클라이언트 데이터 전송: {data.decode("utf-8")}')
                return True
            else:
                print("❌ 서버에 연결되지 않음")
                return False
        except Exception as e:
            print(f"❌ 데이터 전송 오류: {e}")
            return False
    
    def wait_for_response(self, timeout=5):
        """응답 수신 대기"""
        try:
            success, data = self.read()
            if success and data:
                self._last_response = data.decode('utf-8')
                return self._last_response
            elif success and data is None:
                return None      # 타임아웃 발생
            else:
                return None      # 연결 오류
        except Exception as e:
            print(f"❌ 응답 수신 오류: {e}")
            return None
    

    def stop(self):
        """클라이언트 중지"""
        self.disconnect()


if __name__ == "__main__":
    client = MockClient(address="localhost", port=1235)
    print("🌐 UICommunicator와 통신 모드")
    
    if client.connect():
        print("✅ 서버 연결 완료! 메뉴를 시작합니다.")
    else:
        print("❌ 서버 연결 실패")
        exit(1)
    
    while True:
        print(
            "\n========== TCP Client Menu =========="
            "\n명령어를 입력하세요:"
            "\n"
            "\n📤 기본 명령어:"
            "\n  next     - NEXT 명령 전송"
            "\n  new      - NEW 명령 전송"
            "\n  status   - STATUS 명령 전송"
            "\n  shot     - 카메라 촬영 테스트"
            "\n  data     - DATA 메시지 전송"
            "\n  int      - 정수 메시지 전송"
            "\n  custom   - 사용자 정의 데이터 전송"
            "\n  exit     - 클라이언트 종료"
            "\n====================================="
        )
        command = input('\n명령어 입력: ').strip().lower()
        match command:
            case 'exit':
                print("👋 클라이언트를 종료합니다...")
                client.stop()
                break
            
            case 'next':
                print("📤 NEXT 명령 전송 중...")
                client.send_data("NEXT".encode('utf-8'))
                response = client.wait_for_response()
                if response:
                    print(f"📨 응답 수신: {response}")

            case 'new':
                print("📤 NEW 명령 전송 중...")
                client.send_data("NEW".encode('utf-8'))
                response = client.wait_for_response()
                if response:
                    print(f"📨 응답 수신: {response}")
            
            case 'status':
                print("📤 STATUS 명령 전송 중...")
                client.send_data("STATUS".encode('utf-8'))
                response = client.wait_for_response()
                if response:
                    print(f"📨 응답 수신: {response}")
                    
            case 'shot':
                print("📤 SHOT 명령 전송 중...")
                client.send_data("SHOT".encode('utf-8'))
                response = client.wait_for_response()
                if response:
                    print(f"📨 응답 수신: {response}")
            
            case 'data':
                data_input = input("📝 전송할 데이터를 입력하세요 (여러 개는 공백으로 구분): ")
                if data_input:
                    data_parts = data_input.split()
                    print(f"📤 DATA 메시지 전송 중... (데이터: {data_parts})")
                    data_content = " ".join(data_parts)
                    client.send_data(f"DATA#{data_content}".encode('utf-8'))
                    response = client.wait_for_response()
                    if response:
                        print(f"📨 응답 수신: {response}")
                else:
                    print("❌ 데이터를 입력해주세요.")
            
            case 'int':
                try:
                    int_input = input("📝 전송할 정수 값을 입력하세요 (여러 개는 공백으로 구분): ")
                    int_values = [int(x.strip()) for x in int_input.split()]
                    print(f"📤 정수 메시지 전송 중... (값들: {int_values})")
                    # 여러 정수를 공백으로 구분하여 전송
                    int_data = " ".join(map(str, int_values))
                    client.send_data(f"INT#{int_data}".encode('utf-8'))
                    response = client.wait_for_response()
                    if response:
                        print(f"📨 응답 수신: {response}")
                except ValueError:
                    print("❌ 올바른 정수를 입력해주세요. (예: 123 또는 123 456 789)")
            
            case 'custom':
                custom_input = input("📝 전송할 데이터를 입력하세요 (여러 개는 공백으로 구분): ")
                if custom_input:
                    custom_parts = custom_input.split()
                    print(f"📤 커스텀 데이터 전송 중... (데이터: {custom_parts})")
                    # 첫 번째 부분을 명령어로, 나머지를 데이터로 구성
                    if len(custom_parts) == 1:
                        # 명령어만 있는 경우
                        custom_data = custom_parts[0]
                    else:
                        # 명령어와 데이터가 있는 경우 공백으로 구분하여 전송
                        custom_data = " ".join(custom_parts)
                    
                    client.send_data(custom_data.encode('utf-8'))
                    response = client.wait_for_response()
                    if response:
                        print(f"📨 응답 수신: {response}")
                else:
                    print("❌ 빈 데이터는 전송할 수 없습니다.")
            
            case _:
                print(f"❌ 알 수 없는 명령어: '{command}'")
                print("💡 'exit'를 입력하여 종료하거나, 위의 명령어 중 하나를 입력하세요.")
