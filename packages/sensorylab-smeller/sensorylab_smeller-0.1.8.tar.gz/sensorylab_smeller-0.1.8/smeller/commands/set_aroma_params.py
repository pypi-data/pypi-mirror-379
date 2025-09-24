# smeller/commands/set_aroma_params.py
from typing import List, Any, Optional, Dict
from .base import Command

class SetAromaParametersCommand(Command):
    def __init__(self, idAroma: int, onTick: int, offTick: int, phase: Optional[int] = None,
                 delayed_start: Optional[int] = None, watchdog: Optional[int] = None, mod: Optional[int] = None):
        self.idAroma = idAroma
        self.onTick = onTick
        self.offTick = offTick
        self.phase = phase
        self.delayed_start = delayed_start
        self.watchdog = watchdog
        self.mod = mod

    def serialize(self) -> str:
        parts = ["cp", str(self.idAroma), str(self.onTick), str(self.offTick)]
        if self.phase is not None:
            parts.append(str(self.phase))
        if self.delayed_start is not None:
            parts.append(str(self.delayed_start))
        if self.watchdog is not None:
            parts.append(str(self.watchdog))
        if self.mod is not None:
            parts.append(str(self.mod))
        return " ".join(parts)

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]  #  Пример: возвращаем первую строку ответа
        return None


class AromaOnCommand(Command):
    def __init__(self, idAroma: int, mod: Optional[int] = None):
        self.idAroma = idAroma
        self.mod = mod

    def serialize(self) -> str:
        return f"ce {self.idAroma}" if self.mod is None else f"ce {self.idAroma} {self.mod}"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

# ... (аналогично для AromaOffCommand, AromaEnableCommand, AromaDisableCommand) ...

class AromaOffCommand(Command):
    def __init__(self, idAroma: int, mod: Optional[int] = None):
        self.idAroma = idAroma
        self.mod = mod

    def serialize(self) -> str:
        return f"cd {self.idAroma}" if self.mod is None else f"cd {self.idAroma} {self.mod}"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None
class AromaEnableCommand(Command):
    def __init__(self, idAroma: int, mod: Optional[int] = None):
        self.idAroma = idAroma
        self.mod = mod

    def serialize(self) -> str:
        return f"cS {self.idAroma}" if self.mod is None else f"cS {self.idAroma} {self.mod}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None
class AromaDisableCommand(Command):
    def __init__(self, idAroma: int, mod: Optional[int] = None):
        self.idAroma = idAroma
        self.mod = mod

    def serialize(self) -> str:
        return f"cs {self.idAroma}" if self.mod is None else f"cs {self.idAroma} {self.mod}"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None