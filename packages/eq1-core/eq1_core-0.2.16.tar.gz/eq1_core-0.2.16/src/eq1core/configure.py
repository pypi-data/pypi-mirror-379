import abc
import configparser
from pathlib import Path
from typing import Dict, Any, List


class Params:
    def __init__(self, configure):
        self._configure = configure

    def cast_data_type(self, v: str):
        if isinstance(v, int):
            return v
        try:
            return int(v)
        except ValueError as e:
            pass

        try:
            return float(v)
        except ValueError as e:
            pass

        if v.upper() == "TRUE":
            return True

        if v.upper() == "FALSE":
            return False

        if ',' in v:
            return [self.cast_data_type(_v) for _v in v.split(",")]

        return v

    def __getattr__(self, item):
        if not self.include(item):
            return None

        return self.cast_data_type(self._configure[item.lower()])

    def __getitem__(self, item):
        if not self.include(item):
            return None

        return self.cast_data_type(self._configure[item.lower()])

    def __contains__(self, item):
        return self.include(item)

    def include(self, key):
        if self._configure is None:
            return False

        return key.lower() in self._configure

    def get_default(self, key, default):
        if self.include(key):
            return self[key]
        return default


class BaseConfigure(abc.ABC):
    def __init__(self, file_path: str, auto_init: bool = True):
        self._file_path = file_path
        self._auto_init = auto_init

        self._configure = self._init_configure()

    def reload(self):
        auto_init = self._auto_init
        self._configure = self._init_configure()
        self._auto_init = auto_init

    def default_dict(self) -> Dict:
        return {}

    def _init_configure(self) -> configparser.ConfigParser:
        configure = configparser.ConfigParser()
        configure.read_dict(self.default_dict())
        if Path(self._file_path).exists():
            configure.read(self._file_path)
        elif self._auto_init:
            self.write_configure_file(configure, self._file_path)

        return configure

    def keys(self, section: str):
        return self._configure[section.upper()].keys()

    @property
    def file_path(self) -> str:
        return self._file_path

    @classmethod
    def write_configure_file(cls, configure: configparser.ConfigParser, file_path: str):
        if not Path(file_path).parent.exists():
            Path(file_path).parent.mkdir(parents=True)

        with open(file_path, "w", encoding="utf-8") as f:
            configure.write(f)

    def sections(self):
        return [s.upper() for s in self._configure.sections()]

    def get_value(self, section: str, value: str):
        if section.upper() not in self.sections():
            return None

        try:
            return self._configure[section.upper()][value]
        except KeyError as e:
            return None

    def set_value(self, section: str, key: str, value: Any):
        self._configure[section.upper()][key] = value

    def save_configure(self):
        self.write_configure_file(self._configure, self._file_path)

    def params(self, section: str = "system") -> Params:
        return Params(self._configure[section.upper()])


class NetworkConfigure(BaseConfigure):
    def __init__(self, file_path="./public/network.ini"):
        super().__init__(file_path)

    def default_dict(self) -> Dict:
        return {
            'ROBOT1': {
                'method': 'ethernet',
                'protocol': 'tcp',
                'address': '127.0.0.1',
                'port': 9000,
                'timeout': 1,
                'mode': 'server'
            },
            'ROBOT2': {
                'method': 'ethernet',
                'protocol': 'tcp',
                'address': '127.0.0.1',
                'port': 9001,
                'timeout': 1,
                'mode': 'server'
            },
            'IR': {
                'method': 'ethernet',
                'protocol': 'tcp',
                'address': '127.0.0.1',
                'port': 2002,
                'timeout': 10,
                'mode': 'server'
            },
            'QR': {
                'method': 'ethernet',
                'protocol': 'tcp',
                'address': '127.0.0.1',
                'port': 9003,
                'timeout': 1,
                'mode': 'client'
            },
            'IO': {
                'input_ip': '127.0.0.99',
                'output_ip': '127.0.0.99'
            },
            'CENTRIC_MONITOR': {
                'server_ip': '127.0.0.1'
            },
            'LASER': {
                'method': 'serial',
                'port_name': '/dev/ttyUSB0',
                'baud_rate': 9600,
                'timeout': 1000
            },
            'COUNTER': {
                'type': 'rtu',
                'port_name': '/dev/ttyUSB0',
            }
        }

    def params(self, section: str = 'ROBOT1') -> Params:
        return Params(self._configure[section.upper()])

    def centric_monitor_ip(self) -> str:
        # SERVER IP must be set
        return self.get_value("CENTRIC_MONITOR", "server_ip")

    def io_input_ip(self) -> str:
        return self.get_value("IO", "input_ip")

    def io_output_ip(self) -> str:
        return self.get_value("IO", "output_ip")

    def counter_port_name(self) -> str:
        return self.get_value("COUNTER", "port_name")

    def counter_type(self) -> str:
        return self.get_value("COUNTER", "type")

    def set_robot1_method(self, method: str):
        self.set_value("ROBOT1", "method", method)

    def set_robot1_protocol(self, protocol: str):
        self.set_value("ROBOT1", "protocol", protocol)

    def set_robot1_address(self, address: str):
        self.set_value("ROBOT1", "address", address)

    def set_robot1_port(self, port: int):
        self.set_value("ROBOT1", "port", port)

    def set_robot1_timeout(self, timeout: int):
        self.set_value("ROBOT1", "timeout", timeout)

    def set_ir_method(self, method: str):
        self.set_value("IR", "method", method)

    def set_ir_protocol(self, protocol: str):
        self.set_value("IR", "protocol", protocol)

    def set_ir_address(self, address: str):
        self.set_value("IR", "address", address)

    def set_ir_port(self, port: int):
        self.set_value("IR", "port", port)

    def set_ir_timeout(self, timeout: int):
        self.set_value("IR", "timeout", timeout)

    def set_laser_port_name(self, port_name: str):
        self.set_value("LASER", "port_name", port_name)

    def set_laser_baud_rate(self, baud_rate: int):
        self.set_value("LASER", "baud_rate", baud_rate)

    def set_laser_timeout(self, timeout: int):
        self.set_value("LASER", "timeout", timeout)

    def set_counter_port_name(self, port_name: str):
        self.set_value("COUNTER", "port_name", port_name)

    def set_counter_type(self, counter_type: str):
        self.set_value("COUNTER", "type", counter_type)


class SystemConfigure(BaseConfigure):
    def __init__(self, file_path: str = "./public/system.ini"):
        super().__init__(file_path)

    def default_dict(self) -> Dict:
        return {
            'SYSTEM': {
                'version': "1.0",
                'network_configure': "./public/network.ini",
                'trigger_configure': "./public/trigger.ini",
                'storage_configure': "./public/storage.ini",
                'stage': 'vision',
                'use_mock_qr_server': "no",
                'save_origin': "no",
                'save_only_ng': "yes",
            }
        }

    def get_stage_name(self) -> str:
        return self.get_value("system", "stage")

    def version(self) -> str:
        return self.get_value("system", "version")

    def network_configure_path(self) -> str:
        return self.get_value("system", "network_configure")

    def trigger_configure_path(self) -> str:
        return self.get_value("system", "trigger_configure")

    def storage_configure_path(self) -> str:
        return self.get_value("system", "storage_configure")

    def use_mock_qr_server(self) -> bool:
        return self.get_value("system", "use_mock_qr_server").lower() == "yes"

    def save_origin(self) -> bool:
        return self.get_value("system", "save_origin").lower() == "yes"

    def save_only_ng(self) -> bool:
        return self.get_value("system", "save_only_ng").lower() == "yes"

    def set_version(self, version: str):
        self.set_value("system", "version", version)

    def set_stage_name(self, name: str):
        self.set_value("system", "stage", name)

    def set_network_configure_path(self, path: str):
        self.set_value("system", "network_configure", path)

    def set_trigger_configure_path(self, path: str):
        self.set_value("system", "trigger_configure", path)

    def set_storage_configure_path(self, path: str):
        self.set_value("system", "storage_configure", path)

    def set_use_mock_qr_server(self, answer: str):
        self.set_value("system", "use_mock_qr_server", answer.lower())

    def set_save_origin(self, answer: str):
        self.set_value("system", "save_origin", answer.lower())

    def set_save_only_ng(self, answer: str):
        self.set_value("system", "save_only_ng", answer.lower())


class TriggerConfigure(BaseConfigure):
    def __init__(self, file_path: str = "./public/trigger.ini"):
        super().__init__(file_path)

    def default_dict(self) -> Dict:
        return {
            'CAMERA1': {
                'positions': "1050, 1650, 2250, 2850, 3450, 4050, 4650, 5250, 5850, 6450, 7050, 7650, 8250, 8880, 9480"
            },
            'CAMERA2': {
                'positions': "700, 1050, 1650, 2250, 2850, 3450, 4050, 4650, 5250, 5850, 6450, 7050, 7650, 8250, 8880, 9480, 9780"
            },
            'CAMERA3': {
                'positions': "1050, 1650, 2250, 2850, 3450, 4050, 4650, 5250, 5850, 6450, 7050, 7650, 8250, 8880, 9480"
            }
        }

    def get_positions(self) -> Dict[str, List[int]]:
        return {
            'camera1': self.get_cam1_positions(),
            'camera2': self.get_cam2_positions(),
            'camera3': self.get_cam3_positions()
        }

    def get_cam1_positions(self) -> List[int]:
        return list(map(int, self.get_value('camera1', "positions").split(",")))

    def get_cam2_positions(self) -> List[int]:
        return list(map(int, self.get_value('camera2', "positions").split(",")))

    def get_cam3_positions(self) -> List[int]:
        return list(map(int, self.get_value('camera3', "positions").split(",")))

    def set_cam1_positions(self, positions: List[int]):
        self.set_value('camera1', 'positions', ", ".join(map(str, positions)))

    def set_cam2_positions(self, positions: List[int]):
        self.set_value('camera2', 'positions', ", ".join(map(str, positions)))

    def set_cam3_positions(self, positions: List[int]):
        self.set_value('camera3', 'positions', ", ".join(map(str, positions)))


class StorageConfigure(BaseConfigure):
    def __init__(self, file_path: str = "./public/storage.ini"):
        super().__init__(file_path)

    def default_dict(self) -> Dict:
        return {
            'ORIGIN': {
                'root': "./public/output/origin",
                'period': "30d",
                'interval': "1h",
            },
            'RESULT': {
                'root': "./public/output/result",
                'period': "30d",
                'interval': "1h",
            },
            'DISK': {
                'audit_log_keep_days': 365,
                'keep_days': 180,
                'limit': 80,
                'auto_clean': 'yes',
            }
        }

    def get_origin_image_root(self) -> str:
        return self.get_value("origin", "root")

    def get_result_image_root(self) -> str:
        return self.get_value("result", "root")

    def get_origin_image_period(self) -> str:
        return self.get_value("origin", "period")

    def get_result_image_period(self) -> str:
        return self.get_value("result", "period")

    def get_origin_image_interval(self) -> str:
        return self.get_value("origin", "interval")

    def get_result_image_interval(self) -> str:
        return self.get_value("result", "interval")

    def get_audit_log_keep_days(self) -> str:
        return self.get_value("disk", "audit_log_keep_days")

    def get_keep_days(self) -> str:
        return self.get_value("disk", "keep_days")

    def get_limit(self) -> str:
        return self.get_value("disk", "limit")

    def get_auto_clean(self) -> str:
        return self.get_value("disk", "auto_clean")

    def set_origin_image_root(self, path: str):
        self.set_value("origin", "path", path)

    def set_result_image_root(self, path: str):
        self.set_value("result", "path", path)

    def set_origin_image_period(self, period: str):
        self.set_value("origin", "period", period)

    def set_result_image_period(self, period: str):
        self.set_value("result", "period", period)

    def set_origin_image_interval(self, interval: str):
        self.set_value("origin", "interval", interval)

    def set_result_image_interval(self, interval: str):
        self.set_value("result", "interval", interval)

    def set_audit_log_keep_days(self, days: int):
        self.set_value("disk", "audit_log_keep_days", days)

    def set_keep_days(self, days: int):
        self.set_value("disk", "keep_days", days)

    def set_limit(self, limit: int):
        self.set_value("disk", "limit", limit)

    def set_auto_clean(self, auto_clean: str):
        self.set_value("disk", "auto_clean", auto_clean)

