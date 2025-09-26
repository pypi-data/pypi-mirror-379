import os

os.environ["DB_URL"] = "mysql+pymysql://crefle:passwd@localhost:3307/eq1"
os.environ["LOG_PATH"] = "./public/logs"

from typing import Callable
from eq1core import (
    Core, AppLogger, InspectionResultData, ComponentResultData, 
    RollSurfaceEngineResult, CameraPixelInfo, InspectionMode,
    EventRegistry, CustomEvent, InspectionEvents, SampleRollSurfaceEngine,
    cli_command, RepositorySet, DBRepositorySet
)


class ContinuousModeEvents:
    """연속 모드에서 발생하는 이벤트들을 정의합니다."""
    
    class LotChangeRequested(CustomEvent):
        def __init__(self):
            super().__init__(
                name="lot_change_requested",
                description="Lot 변경 요청 이벤트",
                hook=lambda: print("Lot 변경 요청 이벤트가 발생했습니다.")
            )


@cli_command("shot")
def trigger_inspection(core: Core) -> bool:
    from eq1core.lib.camera.frame_grabber.worker import ImageGrabber
    camera_serial = "DA5002684"
    for worker in core._workers:
        if not isinstance(worker, ImageGrabber):
            continue
        if worker.camera_serial != camera_serial:
            continue

        worker.execute_stream_software_trigger()
    

@cli_command("next")
def next_lot(core) -> bool:
    core.emit(ContinuousModeEvents.LotChangeRequested().name)


class ContinuousModeApp:
    def __init__(self, stage_name: str, product_code: str):
        self._core = Core(stage_name=stage_name, product_code=product_code, repos=DBRepositorySet, mode=InspectionMode.CONTINUOUS)
        
        self._core.register_hook(
            event_name=InspectionEvents.ComponentFinished().name,
            hook=self.on_finished_component_inspection
        )

        self._core.register_hook(
            event_name=ContinuousModeEvents.LotChangeRequested().name,
            hook=self.on_received_next_lot            
        )

        self._core.register_engine(SampleRollSurfaceEngine)

    def on_received_next_lot(self, **kwargs) -> bool:
        try:
            AppLogger.write_debug(self, "Received next lot request.", print_to_terminal=True)
            res = self._core.emit(InspectionEvents.LotChange().name)
            if res:
                self.send_new_lot_number_to_control_pc()
            return res
        except Exception as e:
            import traceback
            AppLogger.write_error(self, f"Failed to change lot number: {e} {traceback.format_exc()}", print_to_terminal=True)

    def on_finished_component_inspection(self, **kwargs):
        try:
            required_keys = ["inspection_result_data", "component_result_data"]
            for required_key in required_keys:
                if required_key not in kwargs:
                    AppLogger.write_error(
                        self, f"Missing required key '{required_key}'.", print_to_terminal=True)
                    return

            inspection_result_data = kwargs.get("inspection_result_data", None)
            if not isinstance(inspection_result_data, InspectionResultData):
                AppLogger.write_error(self,
                                      f"Invalid inspection_result_data. expected {InspectionResultData} but {type(inspection_result_data)}",
                                      print_to_terminal=True)
                return

            component_result_data = kwargs.get("component_result_data", None)
            if not isinstance(component_result_data, ComponentResultData):
                AppLogger.write_error(self,
                                      f"Invalid component_result_data. expected {ComponentResultData} but {type(component_result_data)}",
                                      print_to_terminal=True)
                return

            if not isinstance(inspection_result_data.detail, RollSurfaceEngineResult):
                AppLogger.write_error(self,
                                      f"Invalid inspection_result_data.detail. expected {RollSurfaceEngineResult} but {type(inspection_result_data.detail)}",
                                      print_to_terminal=True)
                return

            AppLogger.write_debug(self,
                                  f'\n>>>> on_finished_component_inspection. cam #: {inspection_result_data.camera_number} _ frame #: {inspection_result_data.frame_number} _ "{component_result_data.component_name}" _ "{inspection_result_data.result}"',
                                  print_to_terminal=True)

            res: bool = self._core.emit(InspectionEvents.ComponentResultEnqueueRequested().name, component_result_data)

            camera_number = int(inspection_result_data.camera_number)
            camera_pixel_info: CameraPixelInfo = self._core.emit(InspectionEvents.CameraPixelInfoRequested().name, camera_number=camera_number)
            if not camera_pixel_info:
                AppLogger.write_error(self, f"Failed to get pixel info for camera {camera_number}", print_to_terminal=True)
                return

            frame_number = int(inspection_result_data.frame_number)
            cd_start_offset_mm = float(inspection_result_data.detail.engine_params.cd_start_offset_mm)
            bboxes_with_mm_unit = inspection_result_data.detail.bboxes_with_mm_unit

            AppLogger.write_debug(self, f'frame_number: {frame_number}', print_to_terminal=True)
            AppLogger.write_debug(self, f'frame_md_pixel_size: {camera_pixel_info.frame_md_pixel_size}', print_to_terminal=True)
            AppLogger.write_debug(self, f'md_pixel_resolution: {camera_pixel_info.md_pixel_resolution_mm}', print_to_terminal=True)
            AppLogger.write_debug(self, f'cd_pixel_resolution: {camera_pixel_info.cd_pixel_resolution_mm}', print_to_terminal=True)
            AppLogger.write_debug(self, f'bboxes_with_mm_unit: {bboxes_with_mm_unit}', print_to_terminal=True)

            sum_of_distances_of_passed_frames = camera_pixel_info.calculate_frame_distance(frame_number-1)
            
            locations = []
            for bbox in bboxes_with_mm_unit:
                x, y, w, h = bbox
                # 이전 프레임들의 길이 누적 값을 현재 프레임에 더해줌으로써 Roll 기준 위치로 변환.
                y += sum_of_distances_of_passed_frames
                x += cd_start_offset_mm  # 프레임 기반 위치를 Roll 기준 위치로 변환.
                locations.append(
                    f"{round(y, 3)},{round(y + h, 3)},{round(x, 3)},{round(x + w, 3)}")  # md_start, md_end, cd_start, cd_end

            self.send_defect_locations_to_control_pc(locations=locations)
            AppLogger.write_debug(self, f'<<<< on_finished_component_inspection\n', print_to_terminal=True)
            
        except Exception as e:
            import traceback
            AppLogger.write_error(
                self, f'failed to on_finished_component_inspection as {e} {traceback.format_exc()}', print_to_terminal=True)

    def send_defect_locations_to_control_pc(self, locations):
        pass

    def send_new_lot_number_to_control_pc(self):
        pass

    def run(self):
        AppLogger.write_info(self, "Starting Continuous Mode Application...", print_to_terminal=True)
        self._core.start()
        AppLogger.write_info(self, "Continuous Mode Application has started.", print_to_terminal=True)


if __name__ == "__main__":
    app = ContinuousModeApp(stage_name="-", product_code="SAMPLE-PRODUCT-CODE")
    app.run()