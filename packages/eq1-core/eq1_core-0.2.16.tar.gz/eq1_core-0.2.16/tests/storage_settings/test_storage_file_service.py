import pytest
from src.eq1core.dto import StorageConfigDTO
from src.eq1core.infrastructure.setting_file_service import SettingFileService


class TestStorageSettingFileService:
    def _create_service_with_storage(self, tmp_path, storage_content):
        system_file = tmp_path / "system.ini"
        system_file.write_text("[SYSTEM]\nversion = 1.0")
        service = SettingFileService(str(system_file))
        storage_file = tmp_path / "storage.ini"
        storage_file.write_text(storage_content)
        service.storage_config_path = str(storage_file)
        return service

    def test_storage_file_service(self, tmp_path, valid_storage_config_content, partial_storage_config_content, invalid_storage_config_content, valid_storage_config):
        service = self._create_service_with_storage(tmp_path, valid_storage_config_content)
        result = service.get_storage_setting()
        assert isinstance(result, StorageConfigDTO) and all([result.origin, result.result, result.disk])
        assert result.origin.root == "/data/origin" and result.disk.limit == 80

        service = self._create_service_with_storage(tmp_path, partial_storage_config_content)
        result = service.get_storage_setting()
        assert isinstance(result, StorageConfigDTO) and result.origin
        assert result.origin.root == "/data/origin"

        service = self._create_service_with_storage(tmp_path, invalid_storage_config_content)
        with pytest.raises(ValueError, match="Invalid storage configuration data"):
            service.get_storage_setting()

        system_file = tmp_path / "system.ini"
        system_file.write_text("[SYSTEM]\nversion = 1.0")
        service = SettingFileService(str(system_file))
        assert service.validate_setting("storage", valid_storage_config) is True
        assert service.validate_setting("storage", StorageConfigDTO(origin=None, result=None, disk=None)) is False
