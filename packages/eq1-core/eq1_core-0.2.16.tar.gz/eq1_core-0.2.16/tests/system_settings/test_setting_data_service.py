"""
SettingDataService 인터페이스 테스트 코드

SettingDataService 인터페이스의 동작 검증 테스트
"""

import pytest
from unittest.mock import Mock
from src.eq1core.dto import SystemSettingDTO
from src.eq1core.domain.services.setting_data_service import SettingDataService


@pytest.fixture
def valid_setting():
    """유효한 설정 객체"""
    return SystemSettingDTO(
        version="1.0",
        save_origin=True,
        save_only_ng=False
    )


@pytest.fixture
def mock_service():
    """Mock 서비스 객체"""
    return Mock(spec=SettingDataService)


class TestSettingDataService:
    """SettingDataService 인터페이스 테스트"""
    
    def test_get_system_setting_interface(self, mock_service, valid_setting):
        """시스템 설정 조회 인터페이스 테스트"""
        mock_service.get_system_setting.return_value = valid_setting
        
        result = mock_service.get_system_setting()
        
        assert result == valid_setting
        mock_service.get_system_setting.assert_called_once()
    
    def test_validate_setting_interface(self, mock_service, valid_setting):
        """설정 검증 인터페이스 테스트"""
        mock_service.validate_setting.return_value = True
        
        result = mock_service.validate_setting("system", valid_setting)
        
        assert result is True
        mock_service.validate_setting.assert_called_once_with("system", valid_setting)
    
    def test_validate_setting_invalid_type(self, mock_service, valid_setting):
        """잘못된 설정 타입 검증 테스트"""
        mock_service.validate_setting.return_value = False
        
        result = mock_service.validate_setting("invalid_type", valid_setting)
        
        assert result is False
        mock_service.validate_setting.assert_called_once_with("invalid_type", valid_setting)


if __name__ == "__main__":
    pytest.main([__file__])
