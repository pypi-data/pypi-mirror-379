import enum


class ReceivedCommand(enum.Enum):
    SAMPLE_TRG = 0x98


class SendCommand(enum.Enum):
    SAMPLE_ACK = 0x99


class StatusCode(enum.Enum):
    OK = 0x00
    NG = 0x01
