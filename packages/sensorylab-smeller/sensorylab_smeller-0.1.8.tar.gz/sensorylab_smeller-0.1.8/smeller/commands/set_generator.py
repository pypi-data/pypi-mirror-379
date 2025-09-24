# smeller/commands/set_generator.py
from typing import List, Any
from .base import Command

class SetGeneratorPowerCommand(Command):
    def __init__(self, state: int):
        if state not in [0, 1]:
            raise ValueError("State must be 0 or 1")
        self.state = state

    def serialize(self) -> str:
        return f"g {self.state}"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class SetGeneratorLogicCommand(Command):
    def __init__(self, state: int):
        if state not in [0, 1]:
            raise ValueError("State must be 0 or 1")
        self.state = state

    def serialize(self) -> str:
        return f"G {self.state}"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None