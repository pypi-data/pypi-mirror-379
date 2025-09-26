"""
설정 데이터 서비스 인터페이스

이 모듈은 설정 데이터를 관리하는 서비스의 인터페이스를 정의합니다.
파일 기반, DB 기반 등 다양한 구현체가 이 인터페이스를 구현할 수 있습니다.
"""

from abc import ABC, abstractmethod
from typing import Union
from eq1core.dto import SystemSettingDTO, NetworkSettingDTO, StorageConfigDTO


class SettingDataService(ABC):
    """
    설정 데이터 서비스 추상 기본 클래스
    
    이 클래스는 설정 데이터의 조회와 검증 기능을 제공합니다.
    다양한 구현체(파일 기반, DB 기반 등)가 이 클래스를 상속받아 구현할 수 있습니다.
    """
    
    @abstractmethod
    def get_system_setting(self) -> SystemSettingDTO:
        """
        시스템 설정을 조회합니다.
        
        Returns:
            SystemSettingDTO: 시스템 설정 데이터
            
        Raises:
            FileNotFoundError: 설정 파일이 존재하지 않는 경우
            ValueError: 설정 데이터가 유효하지 않은 경우
            PermissionError: 설정 파일에 접근 권한이 없는 경우
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_network_setting(self) -> NetworkSettingDTO:
        """
        네트워크 설정을 조회합니다.
        
        Returns:
            NetworkSettingDTO: 네트워크 설정 데이터
            
        Raises:
            FileNotFoundError: 설정 파일이 존재하지 않는 경우
            ValueError: 설정 데이터가 유효하지 않은 경우
            PermissionError: 설정 파일에 접근 권한이 없는 경우
        """
        raise NotImplementedError
    
    @abstractmethod
    def get_storage_setting(self) -> StorageConfigDTO:
        """
        스토리지 설정을 조회합니다.
        
        Returns:
            StorageConfigDTO: 스토리지 설정 데이터
            
        Raises:
            FileNotFoundError: 설정 파일이 존재하지 않는 경우
            ValueError: 설정 데이터가 유효하지 않은 경우
            PermissionError: 설정 파일에 접근 권한이 없는 경우
        """
        raise NotImplementedError
    
    @abstractmethod
    def validate_setting(self, setting_type: str, setting_data: Union[SystemSettingDTO, NetworkSettingDTO, StorageConfigDTO]) -> bool:
        """
        설정 데이터의 유효성을 검증합니다.
        
        Args:
            setting_type: 설정 타입 (예: "system", "network")
            setting_data: 검증할 설정 데이터
            
        Returns:
            bool: 설정 데이터가 유효한 경우 True, 그렇지 않으면 False
        """
        raise NotImplementedError
    
    def _validate_system_setting(self, setting_data: SystemSettingDTO) -> bool:
        """
        시스템 설정 데이터의 유효성을 검증하는 공통 메서드
        
        Args:
            setting_data: 검증할 시스템 설정 데이터
            
        Returns:
            bool: 설정 데이터가 유효한 경우 True, 그렇지 않으면 False
        """
        if not setting_data.version or not setting_data.version.strip():
            return False
        
        if not isinstance(setting_data.save_origin, bool):
            return False
        
        if not isinstance(setting_data.save_only_ng, bool):
            return False
        
        return True
    
    def _validate_network_setting(self, setting_data: NetworkSettingDTO) -> bool:
        """
        네트워크 설정 데이터의 유효성을 검증하는 공통 메서드
        
        Args:
            setting_data: 검증할 네트워크 설정 데이터
            
        Returns:
            bool: 설정 데이터가 유효한 경우 True, 그렇지 않으면 False
        """
        if setting_data.sections is None:
            return False
        
        for _, section_data in setting_data.sections.items():
            if not self._validate_network_section(section_data):
                return False
        
        return True
    
    def _validate_network_section(self, section_data) -> bool:
        """
        네트워크 섹션 데이터의 유효성을 검증하는 공통 메서드
        
        Args:
            section_data: 검증할 네트워크 섹션 데이터
            
        Returns:
            bool: 섹션 데이터가 유효한 경우 True, 그렇지 않으면 False
        """
        if section_data.method is not None:
            if not isinstance(section_data.method, str):
                return False

        if section_data.protocol is not None:
            if not isinstance(section_data.protocol, str):
                return False
        
        if section_data.address is not None:
            if not isinstance(section_data.address, str):
                return False
        
        if section_data.port is not None:
            if not isinstance(section_data.port, int) or section_data.port <= 0:
                return False
        
        if section_data.timeout is not None:
            if not isinstance(section_data.timeout, (int, float)) or section_data.timeout <= 0:
                return False
        
        if section_data.mode is not None:
            if not isinstance(section_data.mode, str):
                return False
        
        return True
    
    def _validate_storage_setting(self, setting_data: StorageConfigDTO) -> bool:
        """
        스토리지 설정 데이터의 유효성을 검증하는 공통 메서드
        
        Args:
            setting_data: 검증할 스토리지 설정 데이터
            
        Returns:
            bool: 설정 데이터가 유효한 경우 True, 그렇지 않으면 False
        """
        if setting_data.origin is None and setting_data.result is None and setting_data.disk is None:
            return False
        
        if setting_data.origin is not None:
            if not self._validate_path_config(setting_data.origin):
                return False
        
        if setting_data.result is not None:
            if not self._validate_path_config(setting_data.result):
                return False
        
        if setting_data.disk is not None:
            if not self._validate_disk_config(setting_data.disk):
                return False
        
        return True
    
    def _validate_path_config(self, path_data) -> bool:
        """
        경로 설정 데이터의 유효성을 검증하는 공통 메서드
        
        Args:
            path_data: 검증할 경로 설정 데이터
            
        Returns:
            bool: 경로 데이터가 유효한 경우 True, 그렇지 않으면 False
        """
        if path_data.root is not None:
            if not isinstance(path_data.root, str):
                return False
        
        if path_data.period is not None:
            if not isinstance(path_data.period, str):
                return False
        
        if path_data.interval is not None:
            if not isinstance(path_data.interval, str):
                return False
        
        return True
    
    def _validate_disk_config(self, disk_data) -> bool:
        """
        디스크 설정 데이터의 유효성을 검증하는 공통 메서드
        
        Args:
            disk_data: 검증할 디스크 설정 데이터
            
        Returns:
            bool: 디스크 데이터가 유효한 경우 True, 그렇지 않으면 False
        """
        if disk_data.audit_log_keep_days is not None:
            if not isinstance(disk_data.audit_log_keep_days, int) or disk_data.audit_log_keep_days < 0:
                return False
        
        if disk_data.keep_days is not None:
            if not isinstance(disk_data.keep_days, int) or disk_data.keep_days < 0:
                return False
        
        if disk_data.limit is not None:
            if not isinstance(disk_data.limit, int) or disk_data.limit <= 0 or disk_data.limit > 100:
                return False
        
        if disk_data.auto_clean is not None:
            if not isinstance(disk_data.auto_clean, bool):
                return False
        
        return True
