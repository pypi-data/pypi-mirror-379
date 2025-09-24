# smeller/commands/base.py
from abc import ABC, abstractmethod
from typing import List, Any

class Command(ABC):
    """
    Abstract base class for device commands.
    """
    @abstractmethod
    def serialize(self) -> str:
        """Serializes the command to a string for sending to the device."""
        raise NotImplementedError

    @abstractmethod
    def parse_response(self, response_lines: List[str]) -> Any:
        """Parses the response from the device."""
        raise NotImplementedError
    
