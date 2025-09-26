"""
Core에 통신 플러그인을 추가하는 샘플 코드입니다.
Signal 기반으로 네트워크 이벤트를 처리합니다.
"""

import os
os.environ["DB_URL"] = "mysql+pymysql://crefle:passwd@localhost:3307/eq1"
os.environ["LOG_PATH"] = "./public/logs"

from eq1core import DataServiceFactory, Core, Signal
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from network_plugin.ui import UICommunicator


def main(stage_name: str, product_code: str):
    """메인 실행 함수"""
    if not stage_name or not product_code:
        raise ValueError("stage_name과 product_code는 필수입니다.")

    try:
        # Core 초기화
        print(f"🚀 [Core] Core 초기화: {stage_name}, {product_code}")
        core = Core(uuid=stage_name, group_name=product_code, 
                   data_service=DataServiceFactory.get_service('db'))
        
        # UICommunicator 플러그인 생성
        ui_communicator = UICommunicator({
            "method": "ethernet",
            "protocol": "tcp", 
            "address": "localhost",
            "port": 1234,
            "timeout": 1,
            "mode": "server"
        })

        ui_communicator.ui_custom_signal.connect(lambda x: print(f"여기서 데이터를 받아서 직접 core {core} 랑 연결할 수 있음 : {x}"))
        
        # 플러그인 등록 및 시작
        core.register_plugin(ui_communicator)
        core.start()
        
        print("🎉 [Core] Network plugin 설정 완료!")
        
    except Exception as e:
        raise Exception(f"플러그인 등록 실패: {e}")

    
if __name__ == "__main__":
    main(stage_name='-', product_code='MULTISHOT-PRODUCT-SAMPLE')

