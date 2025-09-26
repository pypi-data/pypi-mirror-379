from src.eq1core.dto import StorageConfigDTO


class TestStorageDTOs:
    def test_storage_dtos(self, path_config_factory, disk_config_factory, valid_storage_config, partial_storage_config):
        
        config = path_config_factory()
        assert config.root == "/data/storage" and config.period == "daily"
        config = path_config_factory(root="/custom/path", period="weekly")
        assert config.root == "/custom/path" and config.period == "weekly"
        config = path_config_factory(root=None, period=None)
        assert config.root is None and config.period is None

        config = disk_config_factory()
        assert config.limit == 80 and config.auto_clean is True
        config = disk_config_factory(limit=90, auto_clean=False)
        assert config.limit == 90 and config.auto_clean is False
        config = disk_config_factory(audit_log_keep_days=None, limit=None)
        assert config.audit_log_keep_days is None and config.limit is None

        assert all([valid_storage_config.origin, valid_storage_config.result, valid_storage_config.disk])
        assert valid_storage_config.origin.root == "/data/origin" and valid_storage_config.disk.limit == 80
        
        config = StorageConfigDTO(origin=None, result=None, disk=None)
        assert all(v is None for v in [config.origin, config.result, config.disk])
        
        assert partial_storage_config.origin and not partial_storage_config.result
        assert partial_storage_config.origin.root == "/data/origin"