
from enum import Enum


REGISTRY = {
    # "hooks": {},
    "cli_commands": {},
    # "network_events": {},
    # "custom_events": {}
}


def cli_command(name):
    def decorator(func):
        REGISTRY["cli_commands"][name] = func
        return func
    return decorator
