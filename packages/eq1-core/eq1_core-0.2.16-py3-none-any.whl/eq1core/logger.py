import os
import time
import inspect
import logging
import datetime
import threading
from enum import Enum
from typing import Any


def _make_save_time():
    yesterday = datetime.date.today() - datetime.timedelta(1)
    save_time = str(yesterday.strftime('%Y%m%d'))
    return save_time


class LogLevel(Enum):
    ERROR = 40
    INFO = 20
    DEBUG = 10
    TIME = 10

    @classmethod
    def get_by_value(cls, value):
        for c in cls:
            if c.value == value:
                return c

    @classmethod
    def get_by_name(cls, name: str):
        for c in cls:
            if c.name.lower() == name.lower():
                return c


class AppLogger:
    _TEST_MODE = False
    GLOBAL_LOG_LEVEL = LogLevel.DEBUG
    MSG_FORMAT = "{} - {} : {}"
    LOG_PATH = os.getenv('LOG_PATH', './public/logs')
    LOGGER_INSTANCES = {}
    _lock = threading.Lock()

    def __init__(self, set_level: LogLevel):
        self.output_path = os.path.join(AppLogger.LOG_PATH, set_level.name)

        self.file_handler = None
        self.logger = None
        self.prefix = None
        self.level = set_level
        self.output_file_prefix = 'vision'
        self._init_set_level(set_level)
        # self.backup_log()

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        with AppLogger._lock:
            if self.level.name in AppLogger.LOGGER_INSTANCES:
                self.logger = AppLogger.LOGGER_INSTANCES[self.level.name]
            else:
                self.logger = logging.getLogger(self.output_file_prefix + "_" + self.level.name)
                self.logger.setLevel(self.level.value)
                self._create_file_handler(self.output_path)
                AppLogger.LOGGER_INSTANCES[self.level.name] = self.logger

    @classmethod
    def write_time_tack(cls, parent: Any, message: str):
        p_name = str(type(parent))
        f_name = inspect.stack()[1].function
        cls(LogLevel.TIME).write(cls.MSG_FORMAT.format(
            p_name, f_name, message
        ))

    @classmethod
    def write_error(cls, parent: Any, message: str, print_to_terminal: bool = False):
        p_name = str(type(parent))
        f_name = inspect.stack()[1].function
        cls(LogLevel.ERROR).write(cls.MSG_FORMAT.format(
            p_name, f_name, message
        ))
        if print_to_terminal:
            print(message)

    @classmethod
    def write_debug(cls, parent: Any, message: str, print_to_terminal: bool = False):
        if cls.GLOBAL_LOG_LEVEL.value <= LogLevel.DEBUG.value:
            p_name = str(type(parent))
            f_name = inspect.stack()[1].function
            cls(LogLevel.DEBUG).write(cls.MSG_FORMAT.format(
                p_name, f_name, message
            ))
            if print_to_terminal:
                print(message)

    @classmethod
    def write_info(cls, parent: Any, message: str, print_to_terminal: bool = False):
        if cls.GLOBAL_LOG_LEVEL.value <= LogLevel.INFO.value:
            p_name = str(type(parent))
            f_name = inspect.stack()[1].function
            cls(LogLevel.INFO).write(cls.MSG_FORMAT.format(
                p_name, f_name, message
            ))
            if print_to_terminal:
                print(message)

    @classmethod
    def set_test_mode(cls, is_test_mode):
        cls._TEST_MODE = is_test_mode

    @classmethod
    def is_test_mode(cls):
        return cls._TEST_MODE

    def _init_set_level(self, set_level):
        try:
            self.output_file_prefix = set_level.name
            self.level = set_level
        except ValueError as ve:
            print('Log level 이 잘못됐습니다.\n\n')

    def _create_file_handler(self, log_dir_path):
        if AppLogger.is_test_mode():
            return

        if self.logger is None:
            raise Exception("Not found {} Logger instance".format(self.level.name))

        prefix = self.output_file_prefix
        log_filename = "{}.{}.log".format(prefix, datetime.datetime.now().strftime('%Y%m%d'))
        filename = os.path.join(log_dir_path, log_filename)

        if not self.logger.handlers:
            file_handler = logging.FileHandler(filename)
            formatter = logging.Formatter("[{}]".format(self.logger.name) + "%(asctime)s.%(msecs)03d" + ' -> ' + "%(message)s", "%Y.%m.%dT%H:%M:%S")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            self.file_handler = file_handler

    def remove_handler(self):
        if AppLogger.is_test_mode():
            return
        if self.file_handler is not None:
            self.logger.removeHandler(self.file_handler)
            self.file_handler = None

    def create_new_handler(self):
        if AppLogger.is_test_mode():
            return

        self.remove_handler()
        self._create_file_handler(self.output_path)

    def backup_log(self):
        import datetime
        from pathlib import Path
        log_file_path = Path(self.output_path).joinpath('{}.log'.format(self.output_file_prefix))
        if not log_file_path.exists():
            return False
        created_datetime = datetime.datetime.fromtimestamp(log_file_path.stat().st_ctime)  # TODO : st_ctime 이 Unix 계열에서 파일 생성 시간이 아닌 파일의 메타 정보가 변경된 시간으로 업데이트 되었음. 파일 생성 시간으로 변경 필요. 다만 우분투에서 st_birthtime 이 없어서 파일명 자체를 당일 날짜로 변경 처리함.
        today = datetime.datetime.now()
        if created_datetime.day != today.day or created_datetime.month != today.month or created_datetime.year != today.year:
            backup_file_path = os.path.join(self.output_path, '{}.log.{}'.format(self.output_file_prefix, _make_save_time()))
            os.renames(str(log_file_path), backup_file_path)

    def write(self, message: str):
        if AppLogger.is_test_mode():
            return
        with AppLogger._lock:
            self.logger.critical(message)


def log_duration(func):
    def call(*args, **kwargs):
        s_time = time.time()
        result = func(*args, **kwargs)
        AppLogger.write_debug(log_duration, f"LogCallDuration({func} : duration ({time.time() - s_time})")
        return result
    return call
