"""
EQ1 Core - 검사 시스템 핵심 라이브러리

이 패키지는 카메라 제어, 통신, I/O 처리, 딥러닝 추론 등의
검사 시스템 핵심 기능을 제공합니다.
"""

__version__ = "0.2.1"
__author__ = "CREFLE INC."
__description__ = "EQ1 검사 시스템 핵심 라이브러리"

# 핵심 모듈들
from . import core
from . import signal
from . import data
from . import dto
from . import utils
from . import logger
from . import image_utils
from . import configure
from . import coord_utils
from . import frame_number
from . import decorators
from . import plugin

# 하위 패키지들
from . import lib
from . import domain
from . import infrastructure
from . import engines
from . import predictors
from . import inspection
from . import dl
from . import mock

# 주요 클래스들 export
from .core import Core as EQ1Core
from .core import Core  # 원래 이름으로도 사용 가능
from .signal import Signal, SignalEmitter
from .data import InspectionMode, ProductResultCode, InspectionPartResultData, InspectionGroupResultData
from .dto import CameraDTO, VisionEngineDTO, PredictorDTO
from .logger import AppLogger
from .configure import Params
from .engines.sample import SampleEngine
from .decorators import cli_command
from .infrastructure.factory import DataServiceFactory
from .plugin import EqPlugin
from .lib.communication.data import SendData, ReceivedData
from .lib.communication.network import NetworkHandler, NetworkEvent
from .infrastructure.db.repositories import DBRepositorySet

__all__ = [
    # 버전 정보
    "__version__",
    "__author__",
    "__description__",
    
    # 핵심 모듈들
    "core",
    "signal", 
    "data",
    "dto",
    "utils",
    "logger",
    "image_utils",
    "configure",
    "coord_utils",
    "frame_number",
    "decorators",
    "plugin",
    
    # 하위 패키지들
    "lib",
    "domain",
    "infrastructure",
    "engines",
    "predictors",
    "inspection",
    "dl",
    "mock",
    
    # 주요 클래스들
    "EQ1Core",
    "Core",
    "Signal",
    "SignalEmitter",
    "InspectionMode",
    "ProductResultCode",
    "InspectionPartResultData",
    "InspectionGroupResultData",
    "CameraDTO",
    "VisionEngineDTO", 
    "PredictorDTO",
    "AppLogger",
    "Params",
    "SampleEngine",
    "cli_command",
    "DataServiceFactory",
    "EqPlugin",
    "SendData",
    "ReceivedData",
    "NetworkHandler",
    "NetworkEvent",
    "DBRepositorySet",
]
