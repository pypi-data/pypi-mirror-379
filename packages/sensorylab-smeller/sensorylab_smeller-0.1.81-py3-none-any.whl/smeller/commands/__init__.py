# commands/__init__.py
from .base import Command
from .set_channel_params import SetChannelParametersCommand
from .get_help import GetHelpCommand
from .restart_device import RestartDeviceCommand
from .set_aroma_params import SetAromaParametersCommand, AromaOnCommand, AromaOffCommand, AromaEnableCommand, AromaDisableCommand  # Добавляем новые команды
from .set_generator import SetGeneratorPowerCommand, SetGeneratorLogicCommand
from .channel_control import ChannelOnCommand, ChannelOffCommand, ChannelEnableCommand, ChannelDisableCommand, ResetChannelsCommand
from .misc_commands import (TestChannelsCommand, SetWatchdogCommand, SetBluetoothNameCommand,
                            RebootLogCommand, SetModCommand, GetModCommand, I2CListCommand,
                            SetWifiCommand, HtopCommand, SetMqttSubCommand, CrGetInfoCommand,
                            ResetChannelParametersCommand, ResetParametersForModCommand,
                            ReinitStatusCommand, SetFanCommand, SetFanConfigCommand, DebugCommand)

__all__ = [
    "Command",
    "SetChannelParametersCommand",
    "GetHelpCommand",
    'RestartDeviceCommand',
    "SetAromaParametersCommand",
    "AromaOnCommand",
    "AromaOffCommand",
    "AromaEnableCommand",
    "AromaDisableCommand",
    "SetGeneratorPowerCommand",
    "SetGeneratorLogicCommand",
    "ChannelOnCommand",
    "ChannelOffCommand",
    "ChannelEnableCommand",
    "ChannelDisableCommand",
    'ResetChannelsCommand',
    "TestChannelsCommand",
    "SetWatchdogCommand",
    "SetBluetoothNameCommand",
    "RebootLogCommand",
    "SetModCommand",
    "GetModCommand",
    "I2CListCommand",
    "SetWifiCommand",
    "HtopCommand",
    "SetMqttSubCommand",
    "CrGetInfoCommand",
    "ResetChannelParametersCommand",
    "ResetParametersForModCommand",
    "ReinitStatusCommand",
    "SetFanCommand",
    "SetFanConfigCommand",
    "DebugCommand"
]