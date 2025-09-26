"""
Core에 통신 플러그인을 추가하려면 다음과 같은 샘플 코드를 사용할 수 있습니다.
Signal 기반으로 네트워크 이벤트를 처리합니다.

1. core default signal을 사용할 수 있음.
2. ui custom signal을 생성하고 외부로 전달할 수 있음.
"""

import enum
from eq1core import EqPlugin, SendData, ReceivedData, NetworkHandler, Signal


class ReceivedCommand(enum.Enum):
    NEXT = 'NEXT'
    NEW = 'NEW'
    

class SendCommand(enum.Enum):
    SAMPLE = 'SAMPLE'


class UICommunicator(EqPlugin, NetworkHandler):
    def __init__(self, net_config, net_id=None):
        EqPlugin.__init__(self)
        NetworkHandler.__init__(self, net_config, event_callback=self, net_id=net_id)

        self.ui_custom_signal = Signal(ReceivedData)
        
    def on_received(self, data: ReceivedData):
        """네트워크로부터 데이터 수신 시 호출되는 메서드"""
        command = data.cmd
        if command == ReceivedCommand.NEXT.value:
            self.on_received_next()
        elif command == ReceivedCommand.NEW.value:
            self.ui_custom_signal.emit(data)  # -> ui custom signal을 생성하고 외부로 전달할 수도 있음.

    def on_received_next(self) -> bool:
        import time
        serial = time.strftime("%Y%m%d%H%M%S")
        self._core.new_group_created.emit(serial)  # -> core default signal을 바로 emit 할 수도 있음.
