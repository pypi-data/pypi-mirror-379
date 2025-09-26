"""
Network Settings 테스트 공통 픽스처

NetworkSectionDTO와 NetworkSettingDTO 테스트에서 재사용할 수 있는 팩토리 픽스처들을 정의합니다.
"""

import pytest
from src.eq1core.dto import NetworkSectionDTO, NetworkSettingDTO


@pytest.fixture
def network_section_factory():
    """NetworkSectionDTO 팩토리 픽스처"""
    def _create_section(
        method="ethernet",
        protocol="tcp", 
        address="127.0.0.1",
        port=9000,
        timeout=1.0,
        mode="server"
    ):
        return NetworkSectionDTO(
            method=method,
            protocol=protocol,
            address=address,
            port=port,
            timeout=timeout,
            mode=mode
        )
    return _create_section


@pytest.fixture
def robot1_section(network_section_factory):
    """ROBOT1 섹션 픽스처"""
    return network_section_factory(port=9000)


@pytest.fixture
def robot2_section(network_section_factory):
    """ROBOT2 섹션 픽스처"""
    return network_section_factory(port=9001)


@pytest.fixture
def valid_network_setting(robot1_section, robot2_section):
    """유효한 네트워크 설정 픽스처"""
    return NetworkSettingDTO(
        sections={
            "ROBOT1": robot1_section,
            "ROBOT2": robot2_section
        }
    )


@pytest.fixture
def mock_service():
    """Mock 서비스 객체"""
    from unittest.mock import Mock
    from src.eq1core.domain.services.setting_data_service import SettingDataService
    return Mock(spec=SettingDataService)


@pytest.fixture
def valid_network_config_content():
    """유효한 네트워크 설정 파일 내용"""
    return """
[ROBOT1]
method = ethernet
protocol = tcp
address = 127.0.0.1
port = 9000
timeout = 1.0
mode = server

[ROBOT2]
method = ethernet
protocol = tcp
address = 127.0.0.1
port = 9001
timeout = 1.0
mode = server

[IO]
method = ethernet
protocol = tcp
address = 127.0.0.1
port = 9002
timeout = 0.5
mode = client
"""


@pytest.fixture
def invalid_network_config_content():
    """유효하지 않은 네트워크 설정 파일 내용"""
    return """
[ROBOT1]
method = 
protocol = tcp
address = 
port = -1
timeout = -0.5
mode = server
"""


@pytest.fixture
def partial_network_config_content():
    """부분적인 네트워크 설정 파일 내용"""
    return """
[ROBOT1]
method = ethernet
port = 9000
"""
