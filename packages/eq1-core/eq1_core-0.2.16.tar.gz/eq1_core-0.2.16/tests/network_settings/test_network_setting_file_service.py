"""
Network Setting File Service 테스트 코드

SettingFileService의 네트워크 관련 메서드 동작 검증 테스트
"""

import pytest
from src.eq1core.dto import NetworkSettingDTO
from src.eq1core.infrastructure.setting_file_service import SettingFileService


class TestNetworkSettingFileService:
    """Network Setting File Service 테스트"""
    
    def _create_config_file(self, tmp_path, content, filename="system.ini"):
        """설정 파일 생성 헬퍼 메서드"""
        config_file = tmp_path / filename
        config_file.write_text(content)
        return str(config_file)
    
    def _create_service(self, tmp_path):
        """서비스 생성 헬퍼 메서드"""
        system_config_path = self._create_config_file(tmp_path, "[SYSTEM]\nversion = 1.0")
        return SettingFileService(system_config_path)
    
    def _create_service_with_network_config(self, tmp_path, network_content):
        """네트워크 설정이 포함된 서비스 생성 헬퍼 메서드"""
        system_config_path = self._create_config_file(tmp_path, "[SYSTEM]\nversion = 1.0")
        service = SettingFileService(system_config_path)
        
        network_config_path = self._create_config_file(tmp_path, network_content, "network.ini")
        service.network_config_path = network_config_path
        
        return service
    
    def test_get_network_setting_from_valid_file(self, tmp_path, valid_network_config_content):
        """유효한 네트워크 설정 파일에서 설정 조회 테스트"""
        service = self._create_service_with_network_config(tmp_path, valid_network_config_content)
        
        result = service.get_network_setting()
        
        assert isinstance(result, NetworkSettingDTO)
        assert len(result.sections) >= 3
        assert "ROBOT1" in result.sections
        assert "ROBOT2" in result.sections
        assert "IO" in result.sections
        
        robot1 = result.sections["ROBOT1"]
        assert robot1.method == "ethernet"
        assert robot1.protocol == "tcp"
        assert robot1.address == "127.0.0.1"
        assert robot1.port == 9000
        assert robot1.timeout == 1.0
        assert robot1.mode == "server"
        
        robot2 = result.sections["ROBOT2"]
        assert robot2.method == "ethernet"
        assert robot2.protocol == "tcp"
        assert robot2.address == "127.0.0.1"
        assert robot2.port == 9001
        assert robot2.timeout == 1.0
        assert robot2.mode == "server"
        
        io = result.sections["IO"]
        assert io.method == "ethernet"
        assert io.protocol == "tcp"
        assert io.address == "127.0.0.1"
        assert io.port == 9002
        assert io.timeout == 0.5
        assert io.mode == "client"
    
    def test_get_network_setting_from_partial_file(self, tmp_path, partial_network_config_content):
        """부분적인 네트워크 설정 파일에서 설정 조회 테스트"""
        service = self._create_service_with_network_config(tmp_path, partial_network_config_content)
        
        result = service.get_network_setting()
        
        assert isinstance(result, NetworkSettingDTO)
        assert len(result.sections) >= 2
        
        robot1 = result.sections["ROBOT1"]
        assert robot1.method == "ethernet"
        assert robot1.protocol == "tcp"
        assert robot1.address == "127.0.0.1"
        assert robot1.port == 9000
        assert robot1.timeout == 1.0
        assert robot1.mode == "server"
        
        robot2 = result.sections["ROBOT2"]
        assert robot2.method == "ethernet"
        assert robot2.protocol == "tcp"
        assert robot2.address == "127.0.0.1"
        assert robot2.port == 9001
        assert robot2.timeout == 1.0
        assert robot2.mode == "server"
    
    def test_get_network_setting_from_invalid_file(self, tmp_path, invalid_network_config_content):
        """유효하지 않은 네트워크 설정 파일에서 설정 조회 테스트"""
        service = self._create_service_with_network_config(tmp_path, invalid_network_config_content)
        
        with pytest.raises(ValueError, match="Failed to parse network configuration"):
            service.get_network_setting()
    
    def test_get_network_setting_from_missing_file(self, tmp_path):
        """존재하지 않는 네트워크 설정 파일에서 설정 조회 테스트"""
        service = self._create_service(tmp_path)
        result = service.get_network_setting()
        
        assert isinstance(result, NetworkSettingDTO)
        assert len(result.sections) >= 0
    
    def test_validate_network_setting_valid_data(self, tmp_path, valid_network_setting):
        """유효한 네트워크 설정 데이터 검증 테스트"""
        service = self._create_service(tmp_path)
        result = service.validate_setting("network", valid_network_setting)
        
        assert result is True
    
    def test_validate_network_setting_invalid_data(self, tmp_path):
        """유효하지 않은 네트워크 설정 데이터 검증 테스트"""
        service = self._create_service(tmp_path)
        invalid_setting = NetworkSettingDTO(sections=None)
        result = service.validate_setting("network", invalid_setting)
        
        assert result is False
    
    def test_validate_network_setting_wrong_type(self, tmp_path, valid_network_setting):
        """잘못된 설정 타입으로 검증 테스트"""
        service = self._create_service(tmp_path)
        result = service.validate_setting("system", valid_network_setting)
        
        assert result is False
    
    def test_validate_network_setting_with_none_setting(self, tmp_path):
        """None 설정으로 검증 테스트"""
        service = self._create_service(tmp_path)
        result = service.validate_setting("network", None)
        
        assert result is False


if __name__ == "__main__":
    pytest.main([__file__])
