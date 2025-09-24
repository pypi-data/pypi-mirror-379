# smeller/models/aroma_event.py

from dataclasses import dataclass, field
from typing import Dict, Union, Optional

@dataclass
class AromaEvent:
    """
    Data class representing a single aroma event within an AromaBlock.

    Attributes:
        timestamp (Optional[float]): The time (in seconds) at which the aroma event occurs,
            relative to the start of the AromaBlock. Defaults to None if not specified.
        command (str): A string identifier for the command to be executed (e.g., "cp", "ce", "f").
        parameters (Dict[str, Union[str, int, float]]): A dictionary containing any parameters
            required for the command. Defaults to an empty dictionary.
    """
    timestamp: Optional[float] = None
    command: str = ""
    parameters: Dict[str, Union[str, int, float]] = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"AromaEvent(timestamp={self.timestamp}, command='{self.command}', parameters={self.parameters})"


if __name__ == '__main__':
    # Простой тест для проверки корректности работы AromaEvent
    event1 = AromaEvent(timestamp=0.5, command="cp", parameters={"channel": 1, "intensity": 50})
    event2 = AromaEvent(command="ce", parameters={"channel": 2})
    
    print("Event 1:", event1)
    print("Event 2:", event2)
    
    print("Event 1 command:", event1.command)
    print("Event 2 timestamp:", event2.timestamp)