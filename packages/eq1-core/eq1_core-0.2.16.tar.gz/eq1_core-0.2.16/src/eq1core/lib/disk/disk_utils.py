import os
import shutil
import json
import time
from pathlib import Path
from eq1core.logger import AppLogger  # TODO : src 의존성 제거하기
from datetime import datetime, timedelta


class DiskManager(threading.Thread):
    """
    "지정 폴더"를 "일정 주기" 마다 체크 하며 "정해진 기간"이 넘은 "폴더"를 "삭제"하는 클래스
    """
    def __init__(self, folder_path: str, retention_days: int = 30, interval: int = 3600):
        super().__init__()
        AppLogger.write_info(self, f"DiskManager is created for {folder_path}. Retention(days): {retention_days}, Interval(sec): {interval}", print_to_terminal=True)
        self.daemon = True
        self._stop_flag = threading.Event()
        self.folder_path = folder_path
        self.retention_days = retention_days
        self.interval = interval

    def get_folder_age(self, folder: str) -> timedelta:
        folder_creation_time = os.path.getctime(folder)
        return datetime.now() - datetime.fromtimestamp(folder_creation_time)

    def is_expired_folder(self, folder: str) -> bool:
        folder_age = self.get_folder_age(folder)
        return folder_age > timedelta(days=self.retention_days)

    def delete_expired_folder(self) -> bool:
        try:
            if not os.path.exists(self.folder_path):
                AppLogger.write_debug(self, f"{self.folder_path} does not exist.")
                return False

            for folder_name in os.listdir(self.folder_path):
                folder_full_path = os.path.join(self.folder_path, folder_name)
                if os.path.isdir(folder_full_path) and self.is_expired_folder(folder_full_path):
                    shutil.rmtree(folder_full_path)
                    AppLogger.write_debug(self, f"'{folder_full_path}' folder is successfully deleted.")
            return True
        except Exception as e:
            AppLogger.write_error(self, f"Failed to deleted !! {e} {traceback.format_exc()}")

            return False

    def stop(self):
        self._stop_flag.set()

    def run(self):
        self._stop_flag.clear()
        while not self._stop_flag.is_set():
            AppLogger.write_debug(self, f"Checking expired folders... {self.folder_path}")
            res = self.delete_expired_folder()
            AppLogger.write_debug(self, f"Checking expired folders... done.")
            AppLogger.write_debug(self, f"Next Check will run After {self.interval} seconds...")

            """
            2024.11.12 - time.sleep 동안 stop 명령을 날려도 바로 종료 되지 않는 문제가 있어서 로직을 수정함.
            """
            _st_time = time.time()
            while time.time() - _st_time < self.interval and not self._stop_flag.is_set():
                time.sleep(0.1)


class Eq1DiskManager(threading.Thread):
    """
    크레플 Eq1 비전 검사 프로그램 전용 디스크 관리 매니저
    Database 구조와 밀접하게 연관되어 있음
    """

    ROOT = "/"  # windows 에서는 "C:\\" 사용하도록 변경 필요. (현재는 리눅스 기준)

    def __init__(self,
                 audit_log_keep_days: int = 365,
                 keep_days: int = 30,
                 limit: int = 80,
                 auto_clean: bool = False,
                 execution_hour: int = 12, # 24시간제(0~23) 기준 매일 점심에 진행
                 execution_minute: int = 0,
                 execution_second: int = 0):
        """
        :param audit_log_keep_days: audit log 보관 기간
        :param keep_days: product results, component results 보관 기간
        :param limit: 저장 공간 사용 제한 (%)
        :param auto_clean: 저장 공간 사용 제한 초과 시 자동 삭제 여부
        """
        super().__init__()

        self.daemon = True
        self._stop_flag = threading.Event()
        self.audit_log_keep_days = audit_log_keep_days
        self.keep_days = keep_days
        self.limit = limit
        self.auto_clean = auto_clean
        self.execution_hour = execution_hour
        self.execution_minute = execution_minute
        self.execution_second = execution_second

        self.on_process = False
        AppLogger.write_info(self, f"Eq1DiskManager is created. Audit Log Keep Days: {audit_log_keep_days}, Keep Days: {keep_days}, Limit(%): {limit}, Auto Clean: {auto_clean}, Execution Time: {self.execution_hour}h {self.execution_minute}m {self.execution_second}s", print_to_terminal=True)

    def stop(self):
        self._stop_flag.set()

    def is_execution_time(self) -> bool:
        now = datetime.now()
        return now.hour == self.execution_hour and now.minute == self.execution_minute and now.second == self.execution_second

    def is_limit_exceeded(self) -> bool:
        total, used, free = shutil.disk_usage(self.ROOT)
        return (used / total) * 100 > self.limit

    @staticmethod
    def get_expired_date(keep_days: int) -> datetime:
        target_date = datetime.now() + timedelta(days=1) - timedelta(days=keep_days)  # keep days 가 0 이라면 실행 시점의 오늘 데이터도 삭제 대상이 됨.
        target_date = target_date.replace(hour=0, minute=0, second=0, microsecond=0)

        return target_date

    def clear_expired_audit_logs(self, expired_date: datetime) -> bool:
        try:
            AppLogger.write_debug(self, f"clear expired audit logs... {expired_date}", print_to_terminal=True)
            from app.db.repositories.audict_logs import AuditLogRepo
            expired_audit_logs = AuditLogRepo.get_expired_audit_logs(expired_date)
            AuditLogRepo.delete_pure_bulk(expired_audit_logs)
            AppLogger.write_debug(self, f"clear expired audit logs... done. ({len(expired_audit_logs)})", print_to_terminal=True)
            return True
        except Exception as e:
            AppLogger.write_error(self, f"Failed to clear expired audit logs !! {e} {traceback.format_exc()}", print_to_terminal=True)
            return False

    def clear_expired_inspection_results(self, expired_date: datetime) -> bool:
        """
        제품결과, 항목결과 항목이 만 개 단위로 발생할 것이기 때문에 DB 트랜젝션에 대한 주의가 필요함
        개별 삭제가 아닌 bulk 로 삭제하도록 해놓은 이유임
        """
        try:
            AppLogger.write_debug(self, f"clear expired inspection results... {expired_date}", print_to_terminal=True)
            from app.db.repositories.product_result import ProductResultRepo
            from app.db.repositories.component_result import ComponentResultRepo
            expired_product_results = ProductResultRepo.get_expired_results(expired_date)
            bulk_delete_target_product_results = []  # DB 트랜젝션을 줄이기 위해 bulk 로 삭제.
            number_of_deleted_product_results = 0
            number_of_deleted_component_results = 0
            for expired_product_result in expired_product_results:
                expired_component_results = ComponentResultRepo.get_finished_components_by_product_result_id(expired_product_result.id)
                bulk_delete_target_component_results = []  # DB 트랜젝션을 줄이기 위해 bulk 로 삭제.
                for expired_component_result in expired_component_results:
                    """
                    DB를 사용하는 검사 PC 가 여러개이다 보니 이미지 파일이 존재하지 않을 수도 있음..
                    따라서 파일이 존재하는 경우에만 component result 를 삭제하도록 하였으나
                    추후 개선 방안에 대한 고민이 필요함
                    """
                    if os.path.exists(expired_component_result.result_image_path):
                        os.remove(expired_component_result.result_image_path)
                        bulk_delete_target_component_results.append(expired_component_result)
                ComponentResultRepo.delete_pure_bulk(bulk_delete_target_component_results)
                number_of_deleted_component_results += len(bulk_delete_target_component_results)
                if ComponentResultRepo.count_finished_components_by_product_result_id(expired_product_result.id) == 0:
                    bulk_delete_target_product_results.append(expired_product_result)
            ProductResultRepo.delete_pure_bulk(bulk_delete_target_product_results)
            number_of_deleted_product_results += len(bulk_delete_target_product_results)
            AppLogger.write_debug(self, f"clear expired inspection results... done. ({number_of_deleted_product_results}, {number_of_deleted_component_results})", print_to_terminal=True)
            return True
        except Exception as e:
            AppLogger.write_error(self, f"Failed to clear expired inspection results !! {e} {traceback.format_exc()}", print_to_terminal=True)
            return False

    def clear_limit_exceeded_data(self):
        AppLogger.write_debug(self, "clear limit exceeded data...", print_to_terminal=True)
        _days = 0
        while not self._stop_flag.is_set() and self.is_limit_exceeded():
            time.sleep(0.5)
            self.clear_expired_audit_logs(
                self.get_expired_date(
                    max(self.keep_days - _days, 0)  # 이부분은 일부로 audit log keep days 가 아닌 keep days 를 적용하였음. 용량 부족 상태이기 때문에 동일 기간을 적용. audit log 는 검사 결과보다는 용량이 적을 것이라 가정함.
                )
            )
            self.clear_expired_inspection_results(
                self.get_expired_date(
                    max(self.keep_days - _days, 0)
                )
            )
            _days += 1
            if _days > self.keep_days:
                break

    def _on_wait(self):
        time.sleep(60)
        self.on_process = False
        AppLogger.write_debug(self, "eq1 disk manager ... on wait... .", print_to_terminal=True)

    def run(self):
        self._stop_flag.clear()
        while not self._stop_flag.is_set():
            try:
                time.sleep(0.1)
                if self.on_process:
                    continue

                if self.is_limit_exceeded() and self.auto_clean:
                    self.on_process = True
                    self.clear_limit_exceeded_data()
                    threading.Thread(target=self._on_wait, args=(), daemon=True).start()

                if self.is_execution_time():
                    self.on_process = True
                    self.clear_expired_audit_logs(
                        expired_date=self.get_expired_date(
                            keep_days=self.audit_log_keep_days
                        )
                    )
                    self.clear_expired_inspection_results(
                        expired_date=self.get_expired_date(
                            keep_days=self.keep_days
                        )
                    )
                    threading.Thread(target=self._on_wait, args=(), daemon=True).start()
            except Exception as e:
                AppLogger.write_error(self, f"Eq1DiskManager Something went wrong !! {e} {traceback.format_exc()}", print_to_terminal=True)
