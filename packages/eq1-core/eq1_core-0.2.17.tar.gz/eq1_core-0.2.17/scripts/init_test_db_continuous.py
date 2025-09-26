"""
* 검사 프로그램 동작 확인을 위한 시나리오 테스트 코드입니다.
* 지정된 DB URL 로 접속하여 DB 테이블을 초기화하고 새로 세팅합니다.
* 린트포/박리지 검사 프로그램은 서로 다른 PC 에서 실행되지만 동일한 DB 를 공유 사용합니다.
* 카메라 stage 속성은 system.ini 에서 설정된 stage 이름과 동일해야 카메라가 활성화됩니다.
* 검사엔진, 검사항목, 딥러닝모델은 카메라가 활성화 된 stage 에서만 인스턴스로 생성 됩니다.
"""

import os
import json
import numpy as np
from typing import Any, Tuple
from enum import Enum

os.environ["DB_URL"] = "mysql+pymysql://crefle:passwd@localhost:3307/eq1"
os.environ["LOG_PATH"] = "./public/logs"

from src.infrastructure.db import create_all_table, drop_all_table
from src.infrastructure.db.models.predictor import DLCategory, PredictorType
from src.infrastructure.db.repositories import ProductRepo, ComponentRepo, CameraRepo, EngineRepo, PredictorRepo, UserRepo, DBRepositorySet
from src.engines.sample import SampleRollSurfaceEngine
from src.core import Core

CAM_SERIAL = "DA5002684"
FG_SERIAL = "DA4991651"
PRODUCT_CODE = "SAMPLE-PRODUCT-CODE"


if __name__ == "__main__":
    try:
        drop_all_table()
        create_all_table()

        """
        STEP 1. 카메라 등록
        """
        camera_model = CameraRepo.create(
            number=1,
            camera_serial=CAM_SERIAL,
            grabber_serial=FG_SERIAL,
            stage='-',  # system.ini 에서 설정된 stage 이름과 동일한 경우 카메라 활성화
            name=CAM_SERIAL.lower(),
            config=json.dumps(
                {
                    "camera_type": "mock",
                    "capture_roi": [0, 0, 50, 500],  # ui 에서 사용
                    "length": 50,                   # ui 에서 사용
                    "width": 500,                   # ui 에서 사용

                    "md_pixel_resolution_mm": 0.1,
                    "cd_pixel_resolution_mm": 0.1,
                    "md_pixel": 1000,
                }
            ),
            number_of_frames=999999
        )

        """
        STEP 2. 제품 등록
        """
        product_model = ProductRepo.create(
            name='plaster',
            code=PRODUCT_CODE
        )

        """
        STEP 3. 딥러닝 모델 등록
        """
        
        pass

        """
        STEP 4. 검사 엔진 등록
        """
        engine_model = EngineRepo.create(
            name='SampleEngine',
            base_engine=SampleRollSurfaceEngine.name.lower(),
            config=json.dumps(
                {
                    "ng_threshold": 0.3,
                    "cd_start_offset_mm": 0,
                    "patch_size": 1000,
                    "left_border_line": 150,
                    "right_border_line": 4520,
                    "patch_overlay": (100, 0),
                    "defect_ignore_ranges": [],
                    "force_ok_box_size": 0,  # pixel (w x h)
                    "force_ok_box_color": 120,  # 0~255;
                    # "predictor_name": 'lint_ad_predictor'
                }
            )
        )

        """
        STEP 5. 검사 항목 등록
        """
        component_infos = [
            {
                "product_id": product_model.id,
                "camera_id": camera_model.id,
                "engine_id": engine_model.id,
                "frame_number": -1,
                "name": "lint",
                "roi": "0,0,5000,1000"
            },
        ]
        for info in component_infos:
            ComponentRepo.create(**info)

        """
        STEP 6. USER 등록
        """
        UserRepo.create(
            name='crefle',
            position='개발자',
            login_id='crefle',
            password='crefle2025',
            permission='developer',
        )
        UserRepo.create(
            name='admin',
            position='직원',
            login_id='admin',
            password='admin2025',
            permission='admin',
        )

        core = Core(
            stage_name='-',
            product_code=PRODUCT_CODE,
            repos=DBRepositorySet
        )
        core.start()

    except Exception as e:
        import traceback
        print('Failed to Run Scenario Test : ', e)
        traceback.print_exc()
    finally:
        pass
