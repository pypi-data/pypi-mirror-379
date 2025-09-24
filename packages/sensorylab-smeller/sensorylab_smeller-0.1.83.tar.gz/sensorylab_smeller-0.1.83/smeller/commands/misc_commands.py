# smeller/commands/misc_commands.py
from typing import List, Any, Optional
from .base import Command
class TestChannelsCommand(Command):


    def __init__(self, delay: int = 5000, onTick: int = 500, offTick: int = 2000):
        self.delay = delay
        self.onTick = onTick
        self.offTick = offTick
    def serialize(self) -> str:
        return f"test {self.delay} {self.onTick} {self.offTick}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]  # Простой пример
        return None

class SetWatchdogCommand(Command):


    def __init__(self, n_channel: int, watchdog: int):
        self.n_channel = n_channel
        self.watchdog = watchdog
    def serialize(self) -> str:
        return f"W {self.n_channel} {self.watchdog}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class SetBluetoothNameCommand(Command):

    def __init__(self, bluetoothName: str):
        if len(bluetoothName) > 16:
            raise ValueError("Bluetooth name cannot exceed 16 characters")
        self.bluetoothName = bluetoothName

    def serialize(self) -> str:
        return f"btn {self.bluetoothName}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class RebootLogCommand(Command):
    def __init__(self, n: int):
        self.n = n

    def serialize(self) -> str:
        return f"reboot_log {self.n}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines
        return None

class SetModCommand(Command):

    def __init__(self, mod: int, n_channel: Optional[int] = None):
        self.mod = mod
        self.n_channel = n_channel
    def serialize(self) -> str:
        if self.n_channel is None:
            return f"set_mod {self.mod}"
        else:
            return f"set_mod {self.n_channel} {self.mod}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class GetModCommand(Command):


    def __init__(self, n_channel: Optional[int] = None):
        self.n_channel = n_channel
    def serialize(self) -> str:
        if self.n_channel is None:
            return "get_mod"
        else:
            return f"get_mod {self.n_channel}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]  # Возвращаем первую строку
        return None
class I2CListCommand(Command):
    def serialize(self) -> str:
        return "i2c_list"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines  # Возвращаем все строки
        return None

class SetWifiCommand(Command):


    def __init__(self, SSID: str, password: str):
        if len(SSID) > 32:
            raise ValueError("SSID cannot exceed 32 characters")
        if len(password) > 63:
            raise ValueError("Password cannot exceed 63 characters")
        self.SSID = SSID
        self.password = password

    def serialize(self) -> str:
        return f"set_wifi {self.SSID} {self.password}"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]  # Простой пример
        return None

class HtopCommand(Command):
    def serialize(self) -> str:
        return "htop"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines
        return None
class SetMqttSubCommand(Command):
    def __init__(self, MQTT_SUB: str):
        self.MQTT_SUB = MQTT_SUB
    def serialize(self) -> str:
        return f"setMqttSub {self.MQTT_SUB}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class CrGetInfoCommand(Command):
    def serialize(self) -> str:
        return "crGetI"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines
        return None

class ResetChannelParametersCommand(Command):
    def serialize(self) -> str:
        return "R"

    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]  # Простой пример
        return None
class ResetParametersForModCommand(Command):
    def __init__(self, flag: int, mod: Optional[int] = None):
        if flag not in [0, 1]:
            raise ValueError("Flag must be 0 or 1")
        self.flag = flag
        self.mod = mod

    def serialize(self) -> str:
        if self.mod is None:
            return f"Rs {self.flag}"
        else:
            return f"Rs {self.flag} {self.mod}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class ReinitStatusCommand(Command):
    def __init__(self, mod: Optional[int] = None):
        self.mod = mod

    def serialize(self) -> str:
        if self.mod is None:
            return "Rg"
        else:
            return f"Rg {self.mod}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class SetFanCommand(Command):
    def __init__(self, pwmMax: int):
        self.pwmMax = pwmMax

    def serialize(self) -> str:
        return f"f {self.pwmMax}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class SetFanConfigCommand(Command):

    def __init__(self, pwmMax: int, pwmMin: int, pwmMode: int, period: int):
        self.pwmMax = pwmMax
        self.pwmMin = pwmMin
        self.pwmMode = pwmMode
        self.period = period
    def serialize(self) -> str:
        return f"x {self.pwmMax} {self.pwmMin} {self.pwmMode} {self.period}"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None

class DebugCommand(Command):
    def serialize(self) -> str:
        return "debug"
    def parse_response(self, response_lines: List[str]) -> Any:
        if response_lines:
            return response_lines[0]
        return None