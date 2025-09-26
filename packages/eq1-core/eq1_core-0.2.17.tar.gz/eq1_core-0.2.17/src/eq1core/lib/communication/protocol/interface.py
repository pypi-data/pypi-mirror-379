import abc
from typing import Tuple, Optional, List


class Protocol(abc.ABC):

    @abc.abstractmethod
    def connect(self) -> bool:
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

    @abc.abstractmethod
    def send(self, data: bytes) -> bool:
        pass

    @abc.abstractmethod
    def read(self) -> Tuple[bool, Optional[bytes]]:
        pass
