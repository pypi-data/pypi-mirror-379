# smeller/commands/restart_device.py

from typing import List, Any
from .base import Command
class RestartDeviceCommand(Command):


    def serialize(self) -> str:
        return "restart"
    def parse_response(self, response_lines: List[str]) -> Any:
        return response_lines