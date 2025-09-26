from eq1core.domain.services.core_data_service import CoreDataService


class CoreEQ1DBService(CoreDataService):
    def __init__(self):
        pass

    def is_group_result_empty(self, name: str) -> bool:
        # TODO: 구현 필요
        pass
    
    def get_active_cameras(self, uuid: str):
        # TODO: 구현 필요
        pass

    def get_last_group_serial(self, group_name: str):
        # TODO: 구현 필요
        pass

    def get_last_group_result_by_name(self, name: str):
        # TODO: 구현 필요
        pass

    def get_group_result_by_serial(self, serial: str):
        # TODO: 구현 필요
        pass

    def get_active_engines(self, uuid: str):
        # TODO: 구현 필요
        pass

    def get_active_inspection_parts(self, uuid: str):
        # TODO: 구현 필요
        pass

    def get_active_inspection_parts_by_engine_name(self, name: str):
        # TODO: 구현 필요
        pass

    def set_unlocked_group_results_as_failed(self, group_name: str, serial: str) -> bool:
        # TODO: 구현 필요
        pass
    
    def set_group_result_as_finished(self, serial: str, result_code, finished_at, is_locked: bool = True, elapsed_time_ms: int = 0):
        # TODO: 구현 필요
        pass

    def create_new_group_result(self, name: str, serial: str, started_at=None, elapsed_time_ms: int = 0):
        # TODO: 구현 필요
        pass

    def save_inspection_part_results(self, results):
        # TODO: 구현 필요
        pass