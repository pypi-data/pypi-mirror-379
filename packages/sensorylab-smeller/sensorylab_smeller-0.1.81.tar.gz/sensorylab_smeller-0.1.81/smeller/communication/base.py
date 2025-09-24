# smeller/communication/base.py
from abc import ABC, abstractmethod
from typing import List, Optional
#from events import Event


class CommunicationInterface(ABC):
    """
    Abstract base class for communication interfaces.
    """

    @abstractmethod
    async def connect(self, *args, **kwargs) -> bool:
        """
        Connects to the device.

        Returns:
            True if connection was successful, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    async def disconnect(self) -> None:
        """Disconnects from the device."""
        raise NotImplementedError

    @abstractmethod
    async def send_command(self, command_str: str) -> Optional[List[str]]:
        """
        Sends a command to the device.
        :param command_str:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    async def read_response(self, timeout: float = 3.0, inter_byte_timeout: float = 0.5) -> list[str]:
        """
        Чтение ответа
        :param timeout:
        :param inter_byte_timeout:
        :return:
        """
        raise NotImplementedError