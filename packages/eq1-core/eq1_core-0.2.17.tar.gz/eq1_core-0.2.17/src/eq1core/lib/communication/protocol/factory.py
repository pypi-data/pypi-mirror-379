from typing import List, Dict
from eq1core.configure import Params  # TODO : src 의존성 제거하기
from eq1core.lib.communication.protocol.interface import Protocol


def create_serial_protocol(port_name: str, baud_rate: int, timeout: int = 1):
    from eq1core.lib.communication.protocol.serial_protocol import SerialProtocol

    return SerialProtocol(port_name, baud_rate, timeout)


def create_ethernet_protocol(protocol: str, address: str, port: int, timeout: int = 1, mode: str = "client"):
    from eq1core.lib.communication.protocol.ethernet import TCPServer, TCPClient

    if protocol.lower() == "tcp" and mode.lower() == "server":
        return TCPServer(address, port, timeout)
    elif protocol.lower() == "tcp" and mode.lower() == "client":
        return TCPClient(address, port, timeout)
    elif protocol.lower() == "udp" and mode.lower() == "server":
        raise ValueError(f"Not Implemented yet for {protocol} / {mode}")
    elif protocol.lower() == "udp" and mode.lower() == "client":
        raise ValueError(f"Not Implemented yet for {protocol} / {mode}")
    else:
        raise ValueError(f"Not found protocol for {protocol}")


def valid_params(params: Dict, need_params: List[str]):
    for k in need_params:
        if k not in params:
            raise ValueError(f"Not found [{k}] in Network Params")

    return True


def create_protocol(params: Dict) -> Protocol:
    if "method" not in params:
        raise ValueError("Not found [method] value in Network Params")

    method = params['method']
    if method == "ethernet":
        need_params = ["protocol", "timeout", "address", "port", "mode"]
        valid_params(params, need_params)
        return create_ethernet_protocol(
            params['protocol'], params['address'], params['port'], params['timeout'], params['mode']
        )

    elif method == "serial":
        need_params = ["port_name", "baud_rate", "timeout"]
        valid_params(params, need_params)
        return create_serial_protocol(
            params['port_name'], params['baud_rate'], params['timeout']
        )
