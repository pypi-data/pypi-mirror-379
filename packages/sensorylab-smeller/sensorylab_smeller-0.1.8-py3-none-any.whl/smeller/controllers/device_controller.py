# smeller/controllers/device_controller.py
import logging
from typing import Optional, List

from smeller.communication.base import CommunicationInterface
from smeller.config.config import DeviceConfig
from smeller.commands.base import Command
from smeller.commands.command_factory import CommandFactory  
from smeller.utils.exceptions import CommandError
from smeller.utils.events import Event, EventHandler
from smeller.config.config import AppConfig # Убедись, что путь к AppConfig правильный

logger = logging.getLogger(__name__)

class DeviceController:
    """
    Main controller for the NeuroAir device.
    """

    def __init__(self, communication: CommunicationInterface, config: AppConfig, event_handler: EventHandler):
        """
        Initializes the DeviceController.

        Args:
            communication: The communication interface to use.
            config: The device configuration.
            event_handler:
        """
        self.communication = communication
        self.config = config
        self.event_handler = event_handler
        self._is_connected = False
        self.command_factory = CommandFactory()  # Создаем экземпляр фабрики


    async def connect(self, *args, **kwargs) -> bool:
        """
        Connects to the device.  Passes arguments to the underlying communication interface.
        """
        logger.debug(f"DeviceController.connect() called with args: {args}, kwargs: {kwargs}")
        self._is_connected = await self.communication.connect(*args, **kwargs)
        if self._is_connected:
            await self.event_handler.publish(Event("device_connected"))
        else:
            await self.event_handler.publish(Event("device_connection_failed")) # Добавлено событие при неудаче
        return self._is_connected

    async def disconnect(self) -> None:
        """Disconnects from the device."""
        logger.debug("DeviceController.disconnect() called")
        await self.communication.disconnect()
        self._is_connected = False
        await self.event_handler.publish(Event("device_disconnected"))

    @property
    def is_connected(self) -> bool:
        """Returns True if the device is connected, False otherwise."""
        return self._is_connected

    async def send_command(self, command: Command) -> Optional[List[str]]:
        """
        Sends a command to the device and handles the response.

        Args:
            command: The command to send.

        Returns:
            The parsed response from the device, or None if an error occurred.
        """
        if not self.is_connected:
            logger.warning("Cannot send command: device not connected.")
            await self.event_handler.publish(Event("error", data="Device not connected"))
            return None
        try:
            command_str = command.serialize()
            logger.debug(f"Sending command: {command_str}")
            response_lines = await self.communication.send_command(command_str)

            if response_lines is None: # Обрабатываем None (ошибка отправки)
                logger.error("Command failed (no response).")
                await self.event_handler.publish(Event("error", data="Command failed (no response)."))
                return None

            logger.debug(f"Received response: {response_lines}")
            parsed_response = command.parse_response(response_lines)
            await self.event_handler.publish(Event("command_response", data=parsed_response))
            return parsed_response  # Возвращаем разобранный ответ

        except Exception as e:
            logger.error(f"Error sending command: {e}", exc_info=True)
            await self.event_handler.publish(Event("error", data=str(e)))
            return None


    async def send_raw_command(self, command_str: str) -> Optional[List[str]]:
        """Отправляет "сырую" команду (строку) и возвращает ответ."""
        if not self.is_connected:
            logger.warning("Cannot send command: device not connected.")
            await self.event_handler.publish(Event("error", data="Device not connected"))
            return None

        try:
            command = self.command_factory.create_command(command_str)
            if command:
                return await self.send_command(command)
            else:
                logger.warning(f"Invalid command string: {command_str}")
                return None

        except CommandError as e:
            logger.error(f"Command error: {e}")
            await self.event_handler.publish(Event("error", data=str(e)))
            return None
        
    async def set_channel_parameters(self, dev_id, channel: int, on_tick: int, off_tick: int, **kwargs) -> Optional[List[str]]:
        """
        Sets channel parameters.
        """
        # Вместо создания команды напрямую используем фабрику:
        # command = commands.set_channel_params.SetChannelParametersCommand(channel, on_tick, off_tick, **kwargs)
        print('to dev_id', dev_id)
        # return await self.send_command(command)
        command_str = f"p {channel} {on_tick} {off_tick}"
        # Добавляем дополнительные параметры
        for key, value in kwargs.items():
            command_str += f" {key} {value}"
        return await self.send_raw_command(command_str)

    async def get_help(self) -> Optional[List[str]]:
        """
        Gets help.
        """
        return await self.send_raw_command("h")
    async def restart(self) -> Optional[List[str]]:
        """
        Restarts the device.
        """
        return await self.send_raw_command("restart")
    async def set_aroma_parameters(self, idAroma: int, onTick: int, offTick: int, **kwargs) -> Optional[List[str]]:
        command_str = f"cp {idAroma} {onTick} {offTick}"
        for key, value in kwargs.items():
            command_str += f" {key} {value}"
        return await self.send_raw_command(command_str)
    async def aroma_on(self, idAroma: int, mod: Optional[int] = None) -> Optional[List[str]]:
        mod_str = f" {mod}" if mod is not None else ""
        return await self.send_raw_command(f"ce {idAroma}{mod_str}")
    async def aroma_off(self, idAroma: int, mod: Optional[int] = None) -> Optional[List[str]]:
        mod_str = f" {mod}" if mod is not None else ""
        return await self.send_raw_command(f"cd {idAroma}{mod_str}")
    async def aroma_enable(self, idAroma: int, mod: Optional[int] = None) -> Optional[List[str]]:
        mod_str = f" {mod}" if mod is not None else ""
        return await self.send_raw_command(f"cS {idAroma}{mod_str}")
    async def aroma_disable(self, idAroma: int, mod: Optional[int] = None) -> Optional[List[str]]:
        mod_str = f" {mod}" if mod is not None else ""
        return await self.send_raw_command(f"cs {idAroma}{mod_str}")
    async def set_generator_power(self, state: int) -> Optional[List[str]]:
        return await self.send_raw_command(f"g {state}")
    async def set_generator_logic(self, state: int) -> Optional[List[str]]:
        return await self.send_raw_command(f"G {state}")
    async def channel_on(self, n_channel: int, mod: Optional[int] = None) -> Optional[List[str]]:
        mod_str = f" {mod}" if mod is not None else ""
        return await self.send_raw_command(f"e {n_channel}{mod_str}")
    async def channel_off(self, n_channel: int, mod: Optional[int] = None) -> Optional[List[str]]:
        mod_str = f" {mod}" if mod is not None else ""
        return await self.send_raw_command(f"d {n_channel}{mod_str}")
    async def channel_enable(self, n_channel: int, mod: Optional[int] = None) -> Optional[List[str]]:
        mod_str = f" {mod}" if mod is not None else ""
        return await self.send_raw_command(f"S {n_channel}{mod_str}")
    async def channel_disable(self, n_channel: int, mod: Optional[int] = None) -> Optional[List[str]]:
        mod_str = f" {mod}" if mod is not None else ""
        return await self.send_raw_command(f"s {n_channel}{mod_str}")
    async def reset_channels(self) -> Optional[List[str]]:
        return await self.send_raw_command("r")
    async def test_channels(self, delay: int = 100, onTick: int = 100, offTick: int = 50) -> Optional[List[str]]:
        return await self.send_raw_command(f"test {delay} {onTick} {offTick}")
    async def set_watchdog(self, n_channel: int, watchdog: int) -> Optional[List[str]]:
        return await self.send_raw_command(f"W {n_channel} {watchdog}")
    async def set_bluetooth_name(self, bluetoothName: str) -> Optional[List[str]]:
        return await self.send_raw_command(f"btn {bluetoothName}")
    async def reboot_log(self, n: int) -> Optional[List[str]]:
        return await self.send_raw_command(f"reboot_log {n}")
    async def set_mod(self, mod: int, n_channel: Optional[int] = None) -> Optional[List[str]]:
        n_channel_str = f" {n_channel}" if n_channel is not None else ""
        return await self.send_raw_command(f"set_mod{n_channel_str} {mod}")
    async def get_mod(self, n_channel: Optional[int] = None) -> Optional[List[str]]:
        n_channel_str = f" {n_channel}" if n_channel is not None else ""
        return await self.send_raw_command(f"get_mod{n_channel_str}")
    async def i2c_list(self) -> Optional[List[str]]:
        return await self.send_raw_command("i2c_list")
    async def set_wifi(self, SSID: str, password: str) -> Optional[List[str]]:
        return await self.send_raw_command(f"set_wifi {SSID} {password}")
    async def htop(self) -> Optional[List[str]]:
        return await self.send_raw_command("htop")
    async def set_mqtt_sub(self, MQTT_SUB: str) -> Optional[List[str]]:
        return await self.send_raw_command(f"setMqttSub {MQTT_SUB}")
    async def cr_get_info(self) -> Optional[List[str]]: 
        """
        Gets cartridge info from device using 'crGetI' command.
        """
        return await self.send_raw_command("crGetI")
    async def reset_channel_parameters(self) -> Optional[List[str]]:
        return await self.send_raw_command("R")
    async def reset_parameters_for_mod(self, flag: int, mod: Optional[int] = None) -> Optional[List[str]]:
        mod_str = f" {mod}" if mod is not None else ""
        return await self.send_raw_command(f"Rs {flag}{mod_str}")
    async def reinit_status(self, mod: Optional[int] = None) -> Optional[List[str]]:
        mod_str = f" {mod}" if mod is not None else ""
        return await self.send_raw_command(f"Rg{mod_str}")
    async def set_fan(self, pwmMax: int) -> Optional[List[str]]:
        return await self.send_raw_command(f"f {pwmMax}")
    async def set_fan_config(self, pwmMax: int, pwmMin: int, pwmMode: int, period: int) -> Optional[List[str]]:
        return await self.send_raw_command(f"x {pwmMax} {pwmMin} {pwmMode} {period}")
    async def debug(self) -> Optional[List[str]]:
        return await self.send_raw_command("debug")