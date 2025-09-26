"""
Network Setting DTO 테스트 코드

NetworkSettingDTO의 동작 검증 테스트
"""

import pytest
from src.eq1core.dto import NetworkSettingDTO


class TestNetworkSettingDTO:
    """NetworkSettingDTO 테스트"""
    
    def test_valid_network_setting_creation(self, robot1_section, robot2_section):
        """정상적인 네트워크 설정 생성 테스트"""
        setting = NetworkSettingDTO(
            sections={
                "ROBOT1": robot1_section,
                "ROBOT2": robot2_section
            }
        )
        
        assert len(setting.sections) == 2
        assert "ROBOT1" in setting.sections
        assert "ROBOT2" in setting.sections
        assert setting.sections["ROBOT1"].port == 9000
        assert setting.sections["ROBOT2"].port == 9001
    
    def test_network_setting_with_empty_sections(self):
        """빈 섹션으로 네트워크 설정 생성 테스트"""
        setting = NetworkSettingDTO(sections={})
        
        assert len(setting.sections) == 0
    
    def test_network_setting_with_single_section(self, robot1_section):
        """단일 섹션으로 네트워크 설정 생성 테스트"""
        setting = NetworkSettingDTO(sections={"ROBOT1": robot1_section})
        
        assert len(setting.sections) == 1
        assert "ROBOT1" in setting.sections
        assert setting.sections["ROBOT1"].port == 9000
    
    def test_network_setting_with_multiple_sections(self, network_section_factory):
        """다중 섹션으로 네트워크 설정 생성 테스트"""
        robot1 = network_section_factory(port=9000)
        robot2 = network_section_factory(port=9001)
        robot3 = network_section_factory(port=9002)
        
        setting = NetworkSettingDTO(
            sections={
                "ROBOT1": robot1,
                "ROBOT2": robot2,
                "ROBOT3": robot3
            }
        )
        
        assert len(setting.sections) == 3
        assert setting.sections["ROBOT1"].port == 9000
        assert setting.sections["ROBOT2"].port == 9001
        assert setting.sections["ROBOT3"].port == 9002

