"""
SystemSettingDTO 테스트 코드

SystemSettingDTO의 정상/비정상 데이터 처리 테스트
"""

import pytest
from src.eq1core.dto import SystemSettingDTO


class TestSystemSettingDTO:
    """SystemSettingDTO 테스트"""
    
    def test_valid_system_setting_creation(self):
        """정상적인 시스템 설정 생성 테스트"""
        setting = SystemSettingDTO(
            version="1.0",
            save_origin=True,
            save_only_ng=False
        )
        
        assert setting.version == "1.0"
        assert setting.save_origin is True
        assert setting.save_only_ng is False


if __name__ == "__main__":
    pytest.main([__file__])
