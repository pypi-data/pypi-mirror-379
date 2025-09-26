import os

# 데이터베이스 환경변수 설정 (eq1core 모듈 초기화 전에 설정)
os.environ["DB_URL"] = "mysql+pymysql://crefle:passwd@localhost:3307/eq1"
os.environ["LOG_PATH"] = "./public/logs"

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui import UICommunicator
from eq1core import DataServiceFactory, Core
from eq1core.engines.sample import SampleEngine


def main(stage_name: str, product_code: str):
    """메인 실행 함수 - UICommunicator를 통한 Core 네트워크 송수신"""
    if not stage_name or not product_code:
        raise ValueError("stage_name과 product_code는 필수입니다.")

    try:
        # Core 초기화
        print(f"🚀 [Core] Core 초기화: {stage_name}, {product_code}")
        core = Core(
            uuid=stage_name, 
            group_name=product_code, 
            data_service=DataServiceFactory.get_service('db')
            )
        
        # 엔진 등록
        core.register_engine(SampleEngine)
        print(f"🔧 [Core] SampleEngine 등록 완료")
        
        # UICommunicator 플러그인 생성
        ui_communicator = UICommunicator({
            "method": "ethernet",
            "protocol": "tcp", 
            "address": "0.0.0.0",  # 모든 인터페이스에서 수신
            "port": 1235,
            "timeout": 1.0,
            "mode": "server"
        }, net_id="TCP_SERVER")

        # 유연한 메시지 처리 함수 정의
        def handle_network_message(received_data):
            """네트워크 메시지 처리 - 다양한 형태의 데이터 지원"""
            print(f"📨 [Core] UICommunicator 메시지 수신: {received_data}")
            
            # 다양한 형태의 데이터 처리
            if hasattr(received_data, 'cmd'):
                command = received_data.cmd
                print(f"🔧 [Core] UICommunicator 명령 처리: {command}")
                
                if command == "NEXT":
                    print(f"🔄 [Core] NEXT 명령 처리 완료")
                elif command == "NEW":
                    print(f"🆕 [Core] NEW 명령 처리 완료")
                elif command == "STATUS":
                    print(f"📊 [Core] STATUS 명령 처리 완료")
                elif command == "DATA":
                    print(f"📊 [Core] DATA 명령 처리 완료")
                elif command == "SHOT":
                    print(f"📷 [Core] 카메라 촬영 명령 수신 - 카메라가 잘 구동되었습니다!")
                elif command == "INT":
                    if hasattr(received_data, 'data') and received_data.data and len(received_data.data) > 0:
                        int_values = received_data.data
                        print(f"🔢 [Core] 정수 명령 처리 완료: {int_values}")
                    else:
                        print(f"⚠️ [Core] 정수 명령이지만 데이터가 없습니다")
                else:
                    print(f"📝 [Core] 사용자 정의 데이터 처리: {command}")
        # UICommunicator 시그널 연결
        ui_communicator.ui_custom_signal.connect(handle_network_message)
        # 플러그인 등록 (서버 시작은 Core에서 자동으로 처리됨)
        core.register_plugin(ui_communicator)
        # Core 시작
        core.start()
        
        print("🎉 [Core] Network plugin 설정 완료!")
        # 서버 정보 출력 (서버가 실행 중일 때만)
        server_info = ui_communicator.get_server_info()
        if server_info["is_running"]:
            print(f"📡 [Core] 포트 {server_info['port']} (UICommunicator)에서 대기 중")
        
    except Exception as e:
        print(f"❌ [Core] 플러그인 등록 실패: {e}")
        try:
            if 'ui_communicator' in locals():
                ui_communicator.disconnect()
        except Exception as cleanup_error:
            print(f"⚠️ [Core] 리소스 정리 중 오류: {cleanup_error}")
        raise Exception(f"플러그인 등록 실패: {e}")


if __name__ == "__main__":
    main(stage_name='-', product_code='MULTISHOT-PRODUCT-SAMPLE')
