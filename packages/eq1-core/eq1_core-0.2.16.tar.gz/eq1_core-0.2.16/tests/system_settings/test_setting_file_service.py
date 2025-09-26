"""
SettingFileService 테스트 코드

파일 기반 설정 서비스의 동작 검증 테스트
"""

import pytest
import os
from src.eq1core.dto import SystemSettingDTO
from src.eq1core.infrastructure.setting_file_service import SettingFileService


@pytest.fixture
def valid_config_content():
    """유효한 설정 파일 내용"""
    return """[SYSTEM]
version = 1.0
save_origin = yes
save_only_ng = no
"""


@pytest.fixture
def invalid_config_content():
    """잘못된 설정 파일 내용 (빈 버전)"""
    return """[SYSTEM]
version = 
save_origin = yes
save_only_ng = no
"""


@pytest.fixture
def invalid_boolean_config_content():
    """잘못된 불린 값이 포함된 설정 파일 내용"""
    return """[SYSTEM]
version = 1.0
save_origin = yes
save_only_ng = no
"""


@pytest.fixture
def valid_setting():
    """유효한 설정 객체"""
    return SystemSettingDTO(
        version="1.0",
        save_origin=True,
        save_only_ng=False
    )


class TestSettingFileService:
    """SettingFileService 테스트"""
    
    def _create_config_file(self, tmp_path, content):
        """설정 파일 생성 헬퍼"""
        system_config_path = tmp_path / "system.ini"
        system_config_path.write_text(content)
        return system_config_path
    
    def _create_service(self, config_path):
        """서비스 생성 헬퍼"""
        return SettingFileService(str(config_path))
    
    def _create_service_with_config(self, tmp_path, content):
        """설정 파일과 서비스를 함께 생성하는 헬퍼"""
        config_path = self._create_config_file(tmp_path, content)
        return self._create_service(config_path)
    
    def test_get_system_setting_from_valid_file(self, tmp_path, valid_config_content):
        """유효한 설정 파일에서 시스템 설정 조회 테스트"""
        service = self._create_service_with_config(tmp_path, valid_config_content)
        result = service.get_system_setting()
        
        assert result.version == "1.0"
        assert result.save_origin is True
        assert result.save_only_ng is False
    
    def test_get_system_setting_from_invalid_file(self, tmp_path, invalid_config_content):
        """잘못된 설정 파일에서 시스템 설정 조회 테스트"""
        service = self._create_service_with_config(tmp_path, invalid_config_content)
        
        with pytest.raises(ValueError, match="Failed to parse system configuration"):
            service.get_system_setting()
    
    def test_get_system_setting_from_file_with_invalid_boolean(self, tmp_path, invalid_boolean_config_content):
        """잘못된 불린 값이 포함된 설정 파일에서 시스템 설정 조회 테스트"""
        service = self._create_service_with_config(tmp_path, invalid_boolean_config_content)
        setting = service.get_system_setting()
        
        assert setting.version == "1.0"
        assert setting.save_origin is True
        assert setting.save_only_ng is False
    
    def test_get_system_setting_from_missing_file(self, tmp_path):
        """존재하지 않는 설정 파일에서 시스템 설정 조회 테스트"""
        non_existent_file = tmp_path / "non_existent.ini"
        
        service = self._create_service(non_existent_file)
        setting = service.get_system_setting()
        
        assert setting.version == "1.0"
        assert setting.save_origin is False
        assert setting.save_only_ng is True
    
    def test_get_system_setting_from_empty_file(self, tmp_path):
        """빈 설정 파일에서 시스템 설정 조회 테스트"""
        service = self._create_service_with_config(tmp_path, "")
        setting = service.get_system_setting()
        
        assert setting.version == "1.0"
        assert setting.save_origin is False
        assert setting.save_only_ng is True
    
    def test_validate_setting_valid_data(self, tmp_path, valid_config_content, valid_setting):
        """유효한 설정 데이터 검증 테스트"""
        service = self._create_service_with_config(tmp_path, valid_config_content)
        result = service.validate_setting("system", valid_setting)
        assert result is True
    
    def test_validate_setting_invalid_data(self, tmp_path, valid_config_content):
        """잘못된 설정 데이터 검증 테스트"""
        service = self._create_service_with_config(tmp_path, valid_config_content)
        
        invalid_setting = SystemSettingDTO(
            version="",
            save_origin=True,
            save_only_ng=False
        )
        
        result = service.validate_setting("system", invalid_setting)
        assert result is False
    
    def test_validate_setting_wrong_type(self, tmp_path, valid_config_content, valid_setting):
        """잘못된 설정 타입 검증 테스트"""
        service = self._create_service_with_config(tmp_path, valid_config_content)
        result = service.validate_setting("invalid_type", valid_setting)
        assert result is False
    
    def test_validate_setting_with_none_setting(self, tmp_path, valid_config_content):
        """None 설정 객체 검증 테스트"""
        service = self._create_service_with_config(tmp_path, valid_config_content)
        result = service.validate_setting("system", None)
        assert result is False
    
    def test_file_permission_error(self, tmp_path, valid_config_content):
        """파일 권한 오류 테스트"""
        system_config_path = self._create_config_file(tmp_path, valid_config_content)
        
        # 파일을 읽기 전용으로 설정 (Unix/Linux/macOS)
        os.chmod(str(system_config_path), 0o444)
        
        try:
            service = self._create_service(system_config_path)
            result = service.get_system_setting()
            assert result is not None
            
            import stat
            file_stat = os.stat(str(system_config_path))
            assert not (file_stat.st_mode & stat.S_IWRITE)
            
        finally:
            # 권한 복원
            os.chmod(str(system_config_path), 0o644)
    
    def test_concurrent_file_access(self, tmp_path, valid_config_content):
        """동시 파일 접근 테스트"""
        system_config_path = self._create_config_file(tmp_path, valid_config_content)
        
        import threading
        
        def read_config():
            service = self._create_service(system_config_path)
            return service.get_system_setting()
        
        threads = []
        results = []
        
        for _ in range(5):
            thread = threading.Thread(target=lambda: results.append(read_config()))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        assert len(results) == 5
        for result in results:
            assert result.version == "1.0"
            assert result.save_origin is True
            assert result.save_only_ng is False


if __name__ == "__main__":
    pytest.main([__file__])
