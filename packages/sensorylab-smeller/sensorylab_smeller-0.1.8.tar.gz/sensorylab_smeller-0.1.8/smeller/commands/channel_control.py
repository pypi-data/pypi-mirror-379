# smeller/commands/channel_control.py
from typing import List, Any, Optional
from .base import Command

class ChannelOnCommand(Command):
    def __init__(self, n_channel: int, mod: Optional[int] = None):
        self.n_channel = n_channel
        self.mod = mod

    def serialize(self) -> str:
        return f"e {self.n_channel}" if self.mod is None else f"e {self.n_channel} {self.mod}"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None
class ChannelOffCommand(Command):
    def __init__(self, n_channel: int, mod: Optional[int] = None):
        self.n_channel = n_channel
        self.mod = mod

    def serialize(self) -> str:
        return f"d {self.n_channel}" if self.mod is None else f"d {self.n_channel} {self.mod}"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class ChannelEnableCommand(Command):
    def __init__(self, n_channel: int, mod: Optional[int] = None):
        self.n_channel = n_channel
        self.mod = mod

    def serialize(self) -> str:
        return f"S {self.n_channel}" if self.mod is None else f"S {self.n_channel} {self.mod}"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class ChannelDisableCommand(Command):
    def __init__(self, n_channel: int, mod: Optional[int] = None):
        self.n_channel = n_channel
        self.mod = mod

    def serialize(self) -> str:
        return f"s {self.n_channel}" if self.mod is None else f"s {self.n_channel} {self.mod}"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None
class ResetChannelsCommand(Command):
    def serialize(self) -> str:
        return "r"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None