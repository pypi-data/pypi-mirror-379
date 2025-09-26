"""
Network Section DTO 테스트 코드

NetworkSectionDTO의 동작 검증 테스트
"""


class TestNetworkSectionDTO:
    """NetworkSectionDTO 테스트"""
    
    def test_network_section_creation(self, network_section_factory):
        """네트워크 섹션 생성 테스트"""
        section = network_section_factory()
        assert section.method == "ethernet"
        assert section.port == 9000
        
        section = network_section_factory(method="wifi", port=8080)
        assert section.method == "wifi"
        assert section.port == 8080
        
        section = network_section_factory(protocol=None, port=None)
        assert section.protocol is None
        assert section.port is None
