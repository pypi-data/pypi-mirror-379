"""
파일 기반 설정 데이터 서비스 구현체

이 모듈은 기존 configure.py의 클래스들을 활용하여 설정 데이터를 관리하는 서비스 구현체입니다.
"""

from typing import Optional, Union
from src.eq1core.dto import SystemSettingDTO, NetworkSettingDTO, NetworkSectionDTO, StorageConfigDTO, PathConfigDTO, DiskConfigDTO
from src.eq1core.domain.services.setting_data_service import SettingDataService
from src.eq1core.configure import SystemConfigure, NetworkConfigure, StorageConfigure


class SettingFileService(SettingDataService):
    """
    파일 기반 설정 데이터 서비스 구현체
    
    기존 configure.py의 클래스들을 활용하여 설정 데이터를 읽고 검증하는 서비스입니다.
    """
    
    def __init__(self, system_config_path: str):
        """
        SettingFileService 초기화
        
        Args:
            system_config_path: 시스템 설정 파일 경로
        """
        self.system_config_path = system_config_path
        self.network_config_path: Optional[str] = None
        self.storage_config_path: Optional[str] = None
        
        self._system_configure = SystemConfigure(system_config_path)
        
        self._initialize_config_paths()
    
    def _initialize_config_paths(self) -> None:
        """
        시스템 설정을 읽어서 다른 설정 파일 경로들을 초기화합니다.
        """
        self.network_config_path = self._system_configure.network_configure_path()
        self.storage_config_path = self._system_configure.storage_configure_path()
        
        if not self.network_config_path:
            self.network_config_path = "./public/network.ini"
        if not self.storage_config_path:
            self.storage_config_path = "./public/storage.ini"
    
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
        try:
            version = self._system_configure.version()
            save_origin = self._system_configure.save_origin()
            save_only_ng = self._system_configure.save_only_ng()
            
            setting = SystemSettingDTO(
                version=version,
                save_origin=save_origin,
                save_only_ng=save_only_ng
            )
            
            if not self._validate_system_setting(setting):
                raise ValueError("Invalid system configuration data")
            
            return setting
            
        except Exception as e:
            raise ValueError(f"Failed to parse system configuration: {str(e)}") from e
    
    def get_network_setting(self) -> NetworkSettingDTO:
        """
        네트워크 설정을 조회합니다.
        
        Returns:
            NetworkSettingDTO: 네트워크 설정 데이터
            
        Raises:
            ValueError: 설정 데이터가 유효하지 않은 경우
        """
        try:
            network_configure = NetworkConfigure(self.network_config_path)
            sections = {}
            
            for section_name in network_configure.sections():
                section_data = self._parse_network_section(network_configure, section_name)
                if section_data:
                    sections[section_name] = section_data
            
            setting = NetworkSettingDTO(sections=sections)
            
            if not self._validate_network_setting(setting):
                raise ValueError("Invalid network configuration data")
            
            return setting
            
        except Exception as e:
            raise ValueError(f"Failed to parse network configuration: {str(e)}") from e
    
    def _parse_network_section(self, network_configure: NetworkConfigure, section_name: str) -> Optional[NetworkSectionDTO]:
        """
        네트워크 섹션을 파싱하여 NetworkSectionDTO로 변환
        
        Args:
            network_configure: NetworkConfigure 인스턴스
            section_name: 섹션 이름
            
        Returns:
            NetworkSectionDTO: 파싱된 섹션 데이터, 파싱 실패 시 None
        """
        try:
            method = network_configure.get_value(section_name, "method")
            protocol = network_configure.get_value(section_name, "protocol")
            address = network_configure.get_value(section_name, "address")
            port = network_configure.get_value(section_name, "port")
            timeout = network_configure.get_value(section_name, "timeout")
            mode = network_configure.get_value(section_name, "mode")
            
            port_int = None
            if port is not None:
                try:
                    port_int = int(port)
                except (ValueError, TypeError):
                    port_int = None
            
            timeout_float = None
            if timeout is not None:
                try:
                    timeout_float = float(timeout)
                except (ValueError, TypeError):
                    timeout_float = None
            
            return NetworkSectionDTO(
                method=method,
                protocol=protocol,
                address=address,
                port=port_int,
                timeout=timeout_float,
                mode=mode
            )
            
        except (ValueError, TypeError, KeyError):
            return None
    
    def get_storage_setting(self) -> StorageConfigDTO:
        """
        스토리지 설정을 조회합니다.
        
        Returns:
            StorageConfigDTO: 스토리지 설정 데이터
            
        Raises:
            ValueError: 설정 데이터가 유효하지 않은 경우
        """
        try:
            storage_configure = StorageConfigure(self.storage_config_path)
            
            origin = self._parse_path_config(storage_configure, "ORIGIN")
            result = self._parse_path_config(storage_configure, "RESULT")
            disk = self._parse_disk_config(storage_configure, "DISK")
            
            setting = StorageConfigDTO(
                origin=origin,
                result=result,
                disk=disk
            )
            
            if not self._validate_storage_setting(setting):
                raise ValueError("Invalid storage configuration data")
            
            return setting
            
        except Exception as e:
            raise ValueError(f"Failed to parse storage configuration: {str(e)}") from e
    
    def _parse_path_config(self, storage_configure: StorageConfigure, section_name: str) -> Optional[PathConfigDTO]:
        """
        경로 설정 섹션을 파싱하여 PathConfigDTO로 변환
        
        Args:
            storage_configure: StorageConfigure 인스턴스
            section_name: 섹션 이름 ("ORIGIN" 또는 "RESULT")
            
        Returns:
            PathConfigDTO: 파싱된 경로 설정 데이터, 파싱 실패 시 None
        """
        try:
            if section_name == "ORIGIN":
                root = storage_configure.get_origin_image_root()
                period = storage_configure.get_origin_image_period()
                interval = storage_configure.get_origin_image_interval()
            elif section_name == "RESULT":
                root = storage_configure.get_result_image_root()
                period = storage_configure.get_result_image_period()
                interval = storage_configure.get_result_image_interval()
            else:
                return None
            
            return PathConfigDTO(
                root=root,
                period=period,
                interval=interval
            )
            
        except (ValueError, TypeError, KeyError):
            return None
    
    def _parse_disk_config(self, storage_configure: StorageConfigure, section_name: str) -> Optional[DiskConfigDTO]:
        """
        디스크 설정 섹션을 파싱하여 DiskConfigDTO로 변환
        
        Args:
            storage_configure: StorageConfigure 인스턴스
            section_name: 섹션 이름 ("DISK")
            
        Returns:
            DiskConfigDTO: 파싱된 디스크 설정 데이터, 파싱 실패 시 None
        """
        try:
            if section_name != "DISK":
                return None
            
            audit_log_keep_days = storage_configure.get_audit_log_keep_days()
            keep_days = storage_configure.get_keep_days()
            limit = storage_configure.get_limit()
            auto_clean = storage_configure.get_auto_clean()
            
            audit_log_keep_days_int = None
            if audit_log_keep_days is not None:
                try:
                    audit_log_keep_days_int = int(audit_log_keep_days)
                except (ValueError, TypeError):
                    audit_log_keep_days_int = None
            
            keep_days_int = None
            if keep_days is not None:
                try:
                    keep_days_int = int(keep_days)
                except (ValueError, TypeError):
                    keep_days_int = None
            
            limit_int = None
            if limit is not None:
                try:
                    limit_int = int(limit)
                except (ValueError, TypeError):
                    limit_int = None
            
            auto_clean_bool = None
            if auto_clean is not None:
                try:
                    auto_clean_bool = auto_clean.lower() == "yes" or auto_clean.lower() == "true"
                except (ValueError, TypeError, AttributeError):
                    auto_clean_bool = None
            
            return DiskConfigDTO(
                audit_log_keep_days=audit_log_keep_days_int,
                keep_days=keep_days_int,
                limit=limit_int,
                auto_clean=auto_clean_bool
            )
            
        except (ValueError, TypeError, KeyError):
            return None
    
    def validate_setting(self, setting_type: str, setting_data: Union[SystemSettingDTO, NetworkSettingDTO, StorageConfigDTO]) -> bool:
        """
        설정 데이터의 유효성을 검증합니다.
        
        Args:
            setting_type: 설정 타입 (예: "system", "network")
            setting_data: 검증할 설정 데이터
            
        Returns:
            bool: 설정 데이터가 유효한 경우 True, 그렇지 않으면 False
        """
        if setting_type == "system":
            if not isinstance(setting_data, SystemSettingDTO):
                return False
            return self._validate_system_setting(setting_data)
        elif setting_type == "network":
            if not isinstance(setting_data, NetworkSettingDTO):
                return False
            return self._validate_network_setting(setting_data)
        elif setting_type == "storage":
            if not isinstance(setting_data, StorageConfigDTO):
                return False
            return self._validate_storage_setting(setting_data)
        else:
            return False
    
