# smeller/models/channel_control_config.py
from dataclasses import dataclass, field
from typing import List, Tuple, Union
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

@dataclass
class ChannelControlConfig:
    channel_id: int
    cycle_time: int
    waypoints: List[Tuple[float, float]]
    interpolation_type: str
    cartridge_id: str = ""
    cartridge_name: str = ""
    color: dict = field(default_factory=lambda: {'r': 128, 'g': 128, 'b': 128, 'a': 255})

    def __post_init__(self):
        if isinstance(self.color, QColor):
            self.color = {
                'r': self.color.red(),
                'g': self.color.green(),
                'b': self.color.blue(),
                'a': self.color.alpha()
            }
        elif self.color is None: # Handle None case just in case
             self.color = {'r': 128, 'g': 128, 'b': 128, 'a': 255}