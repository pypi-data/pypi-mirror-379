import socket
import threading
import json
import time
import unittest
import configparser
from eq1core.configure import Params
from eq1core.lib.communication.protocol.ethernet.tcp_server import TCPServer
from eq1core.lib.communication.network import NetworkHandler, NetworkEvent
from eq1core.lib.communication.data import SendData
from eq1core.lib.communication.command import SendCommand, StatusCode


if __name__ == "__main__":
    config = {
        "SERVER": {
            "method": "ethernet",
            "protocol": "tcp",
            "address": "0.0.0.0",
            "port": 2002,
            "timeout": 1,
            "mode": "server"
        },
    }

    configure = configparser.ConfigParser()
    configure.read_dict(
        config
    )

    server = NetworkHandler(
        network_config=Params(configure["SERVER"]),
        event_callback=NetworkEvent()
    )

    server.start()

    while True:
        key = input('\n press key : ')
        match key:
            case 'q':
                server.stop()
                break
            case 'h':
                print(
                    "\n========== key list =========="
                    "\n1. q"
                    "\n2. tray"
                    # "\n3. sticker"
                    "\n4. product"
                    "\n5. macro"
                    "\n6. ultra"
                    "\n7. wide"
                    "\n=============================="
                )

            case 'distance':
                sub_key = input('    value :')
                server.send_data(
                    SendData(
                        cmd='DISTANCE',
                        data=[str(sub_key)]
                    )
                )
