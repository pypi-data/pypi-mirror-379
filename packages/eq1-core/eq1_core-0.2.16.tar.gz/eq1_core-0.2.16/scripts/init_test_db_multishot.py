import os
import sys


# 실행 경로 : python scripts/init_test_db_multishot.py

# 현재 스크립트의 디렉토리를 Python 경로에 추가 (로컬 개발용)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
sys.path.insert(0, project_root)

os.environ["DB_URL"] = "mysql+pymysql://crefle:passwd@localhost:3307/eq1"
os.environ["LOG_PATH"] = "./public/logs"

# 로컬 개발 환경용 import
from src.eq1core.infrastructure.db.repositories import ProductRepo, ComponentRepo, CameraRepo, EngineRepo
from src.eq1core.infrastructure.db import create_all_table, drop_all_table, SessionLocal
from src.eq1core.core import Core
from src.eq1core.engines.sample import SampleEngine
from src.eq1core.infrastructure.factory import DataServiceFactory
from sqlalchemy import text

import json
import traceback


PRODUCT_CODE = "MULTISHOT-PRODUCT-SAMPLE"


if __name__ == "__main__":
    try:
        print("데이터베이스 테이블 삭제 중...")
        drop_all_table()
        print("데이터베이스 테이블 생성 중...")
        create_all_table()
        print("테이블 생성 완료")

        # SQL을 직접 실행하여 기존 데이터 정리
        print("기존 데이터 정리 중...")
        with SessionLocal() as session:
            try:
                # 외래 키 제약 조건을 일시적으로 비활성화
                session.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
                
                # 외래 키 제약 조건을 고려하여 올바른 순서로 삭제
                # 1. 먼저 컴포넌트 데이터 삭제 (카메라와 엔진을 참조)
                session.execute(text("DELETE FROM components WHERE name LIKE 'sample-component-%'"))
                print("기존 컴포넌트 데이터 삭제됨")
                
                # 2. 카메라 데이터 삭제 (컴포넌트가 먼저 삭제된 후)
                session.execute(text("DELETE FROM cameras WHERE number IN (1, 2)"))
                print("기존 카메라 데이터 삭제됨")
                
                # 3. 엔진 데이터 삭제
                session.execute(text("DELETE FROM engines WHERE name = 'sample-engine'"))
                print("기존 엔진 데이터 삭제됨")
                
                # 4. 제품 데이터 삭제
                session.execute(text("DELETE FROM products WHERE code = :code"), {"code": PRODUCT_CODE})
                print("기존 제품 데이터 삭제됨")
                
                # 외래 키 제약 조건을 다시 활성화
                session.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
                
                session.commit()
            except Exception as e:
                print(f"기존 데이터 정리 중 에러 (무시됨): {e}")
                session.rollback()
                # 롤백 후에도 외래 키 제약 조건을 다시 활성화
                try:
                    session.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
                    session.commit()
                except:
                    pass

        # 카메라 등록
        print("카메라 등록 중...")
        
        # 여러 카메라 등록 (실제 환경 시뮬레이션)
        cameras = []
        
        # 카메라 1: 메인 검사 카메라 (2프레임 처리)
        camera1 = CameraRepo.create(
            number=1,
            camera_serial="MOCK-CAM-001",
            stage='-',  # system.ini 에서 설정된 stage 이름과 동일한 경우 카메라 활성화
            name="main-inspection-camera",
            config=json.dumps(
                {
                    "camera_type": "mock",
                    "format": "mono",
                    "exposure_time": 50000,
                    "gain_db": 20,
                    "trigger_mode": "on",
                    "trigger_source": "sw",
                }
            ),
            number_of_frames=3  # 2프레임을 순차적으로 처리
        )
        cameras.append(camera1)
        print(f"카메라 1 등록 완료: ID={camera1.id}, Serial={camera1.camera_serial} (2프레임 처리)")
        
        # 카메라 2는 비활성화 (카메라 1개로 2프레임 처리)
        print("카메라 2는 비활성화됨 - 카메라 1개로 2프레임 처리")
        
        print(f"총 {len(cameras)}개 카메라 등록 완료")
        
        # 제품 등록
        print("제품 등록 중...")
        product = ProductRepo.create(
            name=PRODUCT_CODE,
            code=PRODUCT_CODE
        )
        print(f"제품 등록 완료: ID={product.id}")

        # 검사 엔진 등록
        print("검사 엔진 등록 중...")
        engine = EngineRepo.create(
            name='sample-engine',
            base_engine=SampleEngine.name.lower(),
            config=json.dumps(
                {
                    "threshold": 100,
                }
            )
        )
        print(f"검사 엔진 등록 완료: ID={engine.id}")

        # 검사 항목 등록
        print("검사 항목 등록 중...")
        ComponentRepo.create(
            product_id=product.id,
            camera_id=camera1.id, # 첫 번째 카메라
            engine_id=engine.id,
            frame_number=1,
            name="sample-component-1",
            roi="0, 0, 2448, 2048",
        )
        ComponentRepo.create(
            product_id=product.id,
            camera_id=camera1.id, # 첫 번째 카메라
            engine_id=engine.id,
            frame_number=2,
            name="sample-component-2",
            roi="0, 0, 2448, 2048",
        )
        ComponentRepo.create(
            product_id=product.id,
            camera_id=camera1.id, # 첫 번째 카메라
            engine_id=engine.id,
            frame_number=3,
            name="sample-component-3",
            roi="0, 0, 2448, 2048",
        )
        print("검사 항목 등록 완료")

        print("Core 초기화 중...")
        core = Core(
            uuid='-',
            group_name=PRODUCT_CODE,
            data_service=DataServiceFactory.get_service('db')
        )
        core.register_engine(SampleEngine)
        core.start()
        print("Core 시작 완료")

        print("✅ 테스트 데이터베이스 초기화가 성공적으로 완료되었습니다!")
        
    except Exception as e:
        print(f"❌ 테스트 데이터베이스 초기화 중 에러가 발생했습니다: {e}")
        print("상세 에러 정보:")
        traceback.print_exc()
        
    finally:
        print("스크립트 실행 완료")
