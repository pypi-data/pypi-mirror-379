import pytest
from src.eq1core.dto import PathConfigDTO, DiskConfigDTO, StorageConfigDTO


@pytest.fixture
def path_config_factory():
    def _create_path_config(
        root="/data/storage",
        period="daily",
        interval="1h"
    ):
        return PathConfigDTO(
            root=root,
            period=period,
            interval=interval
        )
    return _create_path_config


@pytest.fixture
def disk_config_factory():
    def _create_disk_config(
        audit_log_keep_days=30,
        keep_days=7,
        limit=80,
        auto_clean=True
    ):
        return DiskConfigDTO(
            audit_log_keep_days=audit_log_keep_days,
            keep_days=keep_days,
            limit=limit,
            auto_clean=auto_clean
        )
    return _create_disk_config


@pytest.fixture
def valid_storage_config(path_config_factory, disk_config_factory):
    return StorageConfigDTO(
        origin=path_config_factory(root="/data/origin", period="daily"),
        result=path_config_factory(root="/data/result", period="weekly"),
        disk=disk_config_factory()
    )

@pytest.fixture
def partial_storage_config(path_config_factory):
    return StorageConfigDTO(
        origin=path_config_factory(root="/data/origin", period="daily"),
        result=None,
        disk=None
    )


@pytest.fixture
def mock_service():
    from unittest.mock import Mock
    from src.eq1core.domain.services.setting_data_service import SettingDataService
    return Mock(spec=SettingDataService)


@pytest.fixture
def valid_storage_config_content():
    return """
[ORIGIN]
root = /data/origin
period = daily
interval = 1h

[RESULT]
root = /data/result
period = weekly
interval = 2h

[DISK]
audit_log_keep_days = 30
keep_days = 7
limit = 80
auto_clean = yes
"""


@pytest.fixture
def invalid_storage_config_content():
    return """
[ORIGIN]
root = 
period = daily
interval = 1h

[DISK]
audit_log_keep_days = -1
keep_days = 7
limit = 150
auto_clean = invalid
"""


@pytest.fixture
def partial_storage_config_content():
    return """
[ORIGIN]
root = /data/origin
period = daily
"""