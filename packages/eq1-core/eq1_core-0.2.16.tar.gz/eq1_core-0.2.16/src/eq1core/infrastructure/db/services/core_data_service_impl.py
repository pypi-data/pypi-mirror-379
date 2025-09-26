import json
from typing import List, Optional
from datetime import datetime
from eq1core.data import ProductResultCode, InspectionPartResultData, ComponentResultData, EngineResult
from eq1core.domain.services.core_data_service import CoreDataService
from eq1core.infrastructure.db.repositories import DBRepositorySet
from eq1core.domain.entities import Engine, Product, Component, Camera, ProductResult
from eq1core.infrastructure.db.models import ComponentResultModel
from eq1core.dto import InspectionPartDTO, InspectionGroupDTO, VisionEngineDTO, CameraDTO, InspectionGroupResultDTO, InspectionPartResultDTO


class CoreDBService(CoreDataService):
    def __init__(self):
        self.repos = DBRepositorySet

    def is_group_result_empty(self, name: str) -> bool:
        product_result: ProductResult = self.repos.product_result.get_last_result_by_product_code(product_code=name)
        if not product_result:
            return True
        return len(self.repos.component_result.get_finished_components_by_product_result_id(product_result.id)) == 0

    def get_active_cameras(self, uuid: str) -> List[CameraDTO]:
        cameras: List[Camera] = self.repos.camera.get_all_by_stage(stage=uuid)
        res = []
        for camera in cameras:
            try:
                config = json.loads(camera.config) if camera.config else {}
            except (json.JSONDecodeError, TypeError):
                config = {}
                
            res.append(
                CameraDTO(
                    name=camera.name,
                    number=camera.number,
                    serial=camera.camera_serial,
                    fg_serial=camera.grabber_serial,
                    number_of_frames=camera.number_of_frames,
                    settings=config
                )
            )
        return res
    
    def get_last_group_serial(self, group_name: str) -> Optional[str]:
        product_result = self.repos.product_result.get_last_result_by_product_code(product_code=group_name)
        if product_result:
            return product_result.product_serial
        return None
    
    def get_last_group_result_by_name(self, name: str) -> Optional[InspectionGroupResultDTO]:
        product_result: ProductResult = self.repos.product_result.get_last_result_by_product_code(product_code=name)
        if product_result is None:
            return
        
        return InspectionGroupResultDTO(
            name=product_result.product_code,
            serial=product_result.product_serial,
            result=product_result.result_code.value,
            started_at=product_result.started_at,
            finished_at=product_result.finished_at,
            elapsed_time_ms=product_result.elapsed_time_ms,
            is_locked=product_result.is_locked
        )
    
    def get_group_result_by_serial(self, serial: str) -> Optional[InspectionGroupResultDTO]:
        product_results: List[ProductResult] = self.repos.product_result.get_results_by_product_serial(product_serial=serial)
        if not product_results:
            return None
        result = product_results[0]
        return InspectionGroupResultDTO(
            name=result.product_code,
            serial=result.product_serial,
            result=result.result_code.value if result.result_code else None,
            started_at=result.started_at,
            finished_at=result.finished_at,
            elapsed_time_ms=result.elapsed_time_ms,
            is_locked=result.is_locked
        )
    
    def get_active_engines(self, uuid: str) -> List[VisionEngineDTO]:
        """
        활성화 엔진의 조건 : 해당 엔진을 사용하는 활성화된 검사 항목이 존재해야함.
        """
        filtered_cameras = self.repos.camera.get_all_by_stage(stage=uuid)
        filtered_components = []
        for camera in filtered_cameras:
            filtered_components += self.repos.component.get_components_by_camera_id(camera.id)
        engine_dict = {}
        for component in filtered_components:
            component: Component
            engine: Engine = self.repos.engine.get_by_id(id=component.engine_id)
            # predictors: List[Predictor] = self.repos.predictor.get_predictors_by_engine_id(engine_id=engine.id)
            
            if engine and engine.name not in engine_dict:
                engine_dict[engine.name] = VisionEngineDTO(
                    name=engine.name, 
                    code=engine.name,
                    predictor=None,
                    settings=json.loads(engine.config)
                    )
                        
        return engine_dict.values()

    def get_active_inspection_parts(self, uuid: str) -> List[InspectionPartDTO]:
        filtered_cameras = self.repos.camera.get_all_by_stage(stage=uuid)
        filtered_components = []
        for camera in filtered_cameras:
            filtered_components += self.repos.component.get_components_by_camera_id(camera.id)

        inspection_parts = []
        for component in filtered_components:
            component: Component
            product: Product = self.repos.product.get_by_id(id=component.product_id)
            engine: Engine = self.repos.engine.get_by_id(id=component.engine_id)
            camera: Camera = self.repos.camera.get_by_id(id=component.camera_id)
            inspection_parts.append(
                InspectionPartDTO(
                    name=component.name,
                    group=InspectionGroupDTO(
                        name=product.name
                    ),
                    engine_name=engine.name,
                    camera_number=camera.number,
                    frame_number=component.frame_number,
                    uuid=camera.stage,
                    roi_xywh=list(map(int, component.roi.split(',')))
                )
            )
        return inspection_parts

    def get_active_inspection_parts_by_engine_name(self, name: str) -> List[InspectionPartDTO]:
        engine: Engine = self.repos.engine.get_by_name(name=name)
        components: List[Component] = self.repos.component.get_components_by_engine_id(engine_id=engine.id)
        inspection_parts = []
        for component in components:
            component: Component
            product: Product = self.repos.product.get_by_id(id=component.product_id)
            camera: Camera = self.repos.camera.get_by_id(id=component.camera_id)
            inspection_parts.append(
                InspectionPartDTO(
                    name=component.name,
                    group=InspectionGroupDTO(
                        name=product.name
                    ),
                    engine_name=engine.name,
                    camera_number=camera.number,
                    frame_number=component.frame_number,
                    uuid=camera.stage,
                    roi_xywh=list(map(int, component.roi.split(',')))
                )
            )
        return inspection_parts
    
    def set_unlocked_group_results_as_failed(self, group_name: str, serial: str) -> bool:
        unlocked_results = self.repos.product_result.get_unlocked_results_before_certain_time_by_product_code(  # >>REPO
            product_code=group_name,
            certain_time=datetime.now()
        )
        try:
            for unlocked_result in unlocked_results:
                if unlocked_result.product_serial == serial:
                    continue

                self.repos.product_result.update(
                    unlocked_result.id, 
                    result_code=ProductResultCode.FAIL,
                    is_locked=True
                )
            return True
        except Exception as e:
            import traceback
            print('product result lock error', traceback.format_exc())
            return False

    def set_group_result_as_finished(self,
                                     serial: str,
                                     result_code: ProductResultCode,
                                     finished_at: datetime,
                                     is_locked: bool = True,
                                     elapsed_time_ms: int = 0
                                     ) -> InspectionGroupResultDTO:
        product_results: List[ProductResult] = self.repos.product_result.get_results_by_product_serial(product_serial=serial)
        if not product_results:
            return None
        product_result = product_results[0]
        product_result = self.repos.product_result.update(
            id=product_result.id,
            result_code=result_code,
            finished_at=finished_at,
            is_locked=is_locked,
            elapsed_time_ms=elapsed_time_ms
        )
        return InspectionGroupResultDTO(
            name=product_result.product_code,
            serial=product_result.product_serial,
            result=product_result.result_code.value if product_result.result_code else None,
            started_at=product_result.started_at,
            finished_at=product_result.finished_at,
            elapsed_time_ms=product_result.elapsed_time_ms,
            is_locked=product_result.is_locked
        )
    
    def create_new_group_result(self,
                                name: str,
                                serial: str,
                                started_at: datetime = datetime.now(),
                                elapsed_time_ms: int = 0) -> InspectionGroupResultDTO:
        
        product_result: ProductResult =  self.repos.product_result.create(
            product_code=name,
            product_serial=serial,
            started_at=started_at,
            elapsed_time_ms=elapsed_time_ms
        )

        return InspectionGroupResultDTO(
            name=product_result.product_code,
            serial=product_result.product_serial,
            started_at=product_result.started_at,
        )

    def save_inspection_part_results(self, results: List[InspectionPartResultData]) -> List[InspectionPartResultDTO]:
        component_results: List[ComponentResultData] = []
        for result in results:
            result: InspectionPartResultData
            product_results = self.repos.product_result.get_results_by_product_serial(product_serial=result.group_serial)
            if not product_results:
                continue
            product_result = product_results[0]
            
            detail_value = result.detail
            if hasattr(detail_value, 'to_dict'):
                detail_value = json.dumps(detail_value.to_dict())
            elif detail_value is not None:
                try:
                    detail_value = json.dumps(detail_value)
                except (TypeError, ValueError):
                    detail_value = str(detail_value)
            
            component_results.append(
                ComponentResultData(
                    product_result_id=product_result.id,
                    component_name=result.part_name,
                    camera_number=result.camera_number,
                    frame_number=result.frame_number,
                    roi=result.roi_xywh,
                    started_at=result.started_at,
                    finished_at=result.finished_at,
                    result=result.result,
                    elapsed_time_ms=result.elapsed_time_ms,
                    detail=detail_value,
                    origin_image_path=result.origin_image_path,
                    result_image_path=result.result_image_path
                )
            )
        component_result_models: List[ComponentResultModel] = self.repos.component_result.create_bulk(data=component_results)
        res = []
        for result in component_result_models:
            res.append(
                InspectionPartResultDTO(
                    id=result.id,
                    group_result_id=result.product_result_id,
                    part_name=result.component_name,
                    camera_number=result.camera_number,
                    frame_number=result.frame_number,
                    roi=result.roi,
                    started_at=result.started_at,
                    finished_at=result.finished_at,
                    result=result.result,
                    elapsed_time_ms=result.elapsed_time_ms,
                    detail=result.detail,
                    origin_image_path=result.origin_image_path,
                    result_image_path=result.result_image_path
                )
            )
            
        return res