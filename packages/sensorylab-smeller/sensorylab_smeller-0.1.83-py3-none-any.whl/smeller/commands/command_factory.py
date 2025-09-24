# smeller/commands/command_factory.py
from typing import Optional, Dict, Any
from .base import Command
import inspect
from smeller.commands import (
    SetChannelParametersCommand, GetHelpCommand, RestartDeviceCommand,
    SetAromaParametersCommand, AromaOnCommand, AromaOffCommand,
    AromaEnableCommand, AromaDisableCommand, SetGeneratorPowerCommand,
    SetGeneratorLogicCommand, ChannelOnCommand, ChannelOffCommand,
    ChannelEnableCommand, ChannelDisableCommand, ResetChannelsCommand,
    TestChannelsCommand, SetWatchdogCommand, SetBluetoothNameCommand,
    RebootLogCommand, SetModCommand, GetModCommand, I2CListCommand,
    SetWifiCommand, HtopCommand, SetMqttSubCommand, CrGetInfoCommand,
    ResetChannelParametersCommand, ResetParametersForModCommand,
    ReinitStatusCommand, SetFanCommand, SetFanConfigCommand, DebugCommand
)
from smeller.utils.exceptions import CommandError


class CommandFactory:


    def __init__(self):
        self._commands: Dict[str, type[Command]] = {  # type[Command] - это тип класса, а не экземпляр
            "p": SetChannelParametersCommand,
            "h": GetHelpCommand,
            "restart": RestartDeviceCommand,
            "cp": SetAromaParametersCommand,
            "ce": AromaOnCommand,
            "cd": AromaOffCommand,
            "cS": AromaEnableCommand,
            "cs": AromaDisableCommand,
            "g": SetGeneratorPowerCommand,
            "G": SetGeneratorLogicCommand,
            "e": ChannelOnCommand,
            "d": ChannelOffCommand,
            "S": ChannelEnableCommand,
            "s": ChannelDisableCommand,
            "r": ResetChannelsCommand,
            "test": TestChannelsCommand,
            "W": SetWatchdogCommand,
            "btn": SetBluetoothNameCommand,
            "reboot_log": RebootLogCommand,
            "set_mod": SetModCommand,
            "get_mod": GetModCommand,
            "i2c_list": I2CListCommand,
            "set_wifi": SetWifiCommand,
            "htop": HtopCommand,
            "setMqttSub": SetMqttSubCommand,
            "crGetI": CrGetInfoCommand,
            "R": ResetChannelParametersCommand,
            "Rs": ResetParametersForModCommand,
            "Rg": ReinitStatusCommand,
            "f": SetFanCommand,
            "x": SetFanConfigCommand,
            "debug": DebugCommand,
        }

    def create_command(self, command_str: str) -> Optional[Command]:
        """
        Creates a command object based on the input string.

        Args:
            command_str: The string representation of the command.

        Returns:
            The command object, or None if the command is not recognized.
        """
        parts = command_str.split()
        if not parts:
            return None

        command_key = parts[0]
        args = parts[1:]

        command_class = self._commands.get(command_key)
        if command_class is None:
            raise CommandError(f"Unknown command: {command_key}")

        try:
            #  ВСЕГДА вызываем _convert_args
            typed_args = self._convert_args(command_class, args)
            return command_class(*typed_args)

        except (ValueError, TypeError) as e:
            raise CommandError(f"Invalid arguments for command {command_key}: {e}")
        
    def _convert_args(self, command_class: type[Command], args: list[str]) -> list[Any]:
        """Конвертирует строковые аргументы в типы, указанные в аннотациях."""
        converted_args = []

        # Получаем аннотации типов из конструктора
        signature = inspect.signature(command_class.__init__)
        params = list(signature.parameters.values())

        #  Убираем 'self'
        params = params[1:]

        for i, arg_str in enumerate(args):
            if i < len(params):
                param = params[i]
                #  Если есть аннотация типа, конвертируем
                if param.annotation != inspect.Parameter.empty:
                    try:
                        converted = param.annotation(arg_str)
                    except (ValueError, TypeError) as e:
                        raise ValueError(
                            f"Cannot convert argument '{arg_str}' to {param.annotation} for parameter "
                            f"'{param.name}' of command {command_class.__name__}: {e}") from e
                    converted_args.append(converted)
                else:
                    converted_args.append(arg_str)
            else:
                # Обрабатываем случай когда передано больше аргументов чем нужно.
                break
        return converted_args