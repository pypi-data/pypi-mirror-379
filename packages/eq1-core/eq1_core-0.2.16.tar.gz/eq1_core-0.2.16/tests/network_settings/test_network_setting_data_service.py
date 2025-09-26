"""
Network Setting Data Service 인터페이스 테스트 코드

SettingDataService의 네트워크 관련 메서드 동작 검증 테스트
"""


class TestNetworkSettingDataService:
    """Network Setting Data Service 인터페이스 테스트"""
    
    def test_get_network_setting_interface(self, mock_service, valid_network_setting):
        """네트워크 설정 조회 인터페이스 테스트"""
        mock_service.get_network_setting.return_value = valid_network_setting
        result = mock_service.get_network_setting()
        
        assert result == valid_network_setting
        mock_service.get_network_setting.assert_called_once()
    
    def test_validate_network_setting_interface(self, mock_service, valid_network_setting):
        """네트워크 설정 검증 인터페이스 테스트"""
        mock_service.validate_setting.return_value = True
        result = mock_service.validate_setting("network", valid_network_setting)
        
        assert result is True
        mock_service.validate_setting.assert_called_once_with("network", valid_network_setting)
    
    def test_validate_network_setting_invalid_type(self, mock_service, valid_network_setting):
        """잘못된 네트워크 설정 타입 검증 테스트"""
        mock_service.validate_setting.return_value = False
        result = mock_service.validate_setting("invalid_type", valid_network_setting)
        
        assert result is False
        mock_service.validate_setting.assert_called_once_with("invalid_type", valid_network_setting)
