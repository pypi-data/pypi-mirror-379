class TestStorageSettingDataService:
    def test_storage_setting_interface(self, mock_service, valid_storage_config):
        
        mock_service.get_storage_setting.return_value = valid_storage_config
        assert mock_service.get_storage_setting() == valid_storage_config
        mock_service.get_storage_setting.assert_called_once()

        mock_service.validate_setting.return_value = True
        assert mock_service.validate_setting("storage", valid_storage_config) is True
        mock_service.validate_setting.assert_called_with("storage", valid_storage_config)

        mock_service.validate_setting.return_value = False
        assert mock_service.validate_setting("invalid_type", valid_storage_config) is False