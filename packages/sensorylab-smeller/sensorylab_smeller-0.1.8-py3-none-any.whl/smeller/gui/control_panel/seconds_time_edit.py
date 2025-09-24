# smeller/gui/seconds_time_edit.py
import sys
from PyQt6.QtWidgets import QTimeEdit, QDateTimeEdit
from pathlib import Path
project_root = Path(__file__).resolve().parents[2]  # Поднимаемся на два уровня вверх
sys.path.append(str(project_root))
import logging

from PyQt6.QtCore import Qt, QTime, QEvent

from smeller.config.constants import *


logger = logging.getLogger(__name__)

class SecondsTimeEdit(QTimeEdit):
    """
    Custom QTimeEdit that only allows modification of seconds,
    and always focuses on the seconds section when stepping.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setDisplayFormat("hh:mm:ss")
        self.setTime(QTime(0, 0, 0))  # Initialize to 00:00:00

    def stepBy(self, steps):
        """
        Overrides stepBy to change seconds, handling wrap-around and
        propagating changes to minutes and hours.
        """
        current_time = self.time()
        new_time = current_time.addSecs(steps)  # Use addSecs for proper handling
        self.setTime(new_time)

    def eventFilter(self, obj, event):
        """
        Filters events to handle arrow key presses even when focus is not on seconds.
        """
        if event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Up:
                self.setCurrentSection(QDateTimeEdit.Section.SecondSection)
                self.stepBy(1)
                return True  # Event handled
            elif event.key() == Qt.Key.Key_Down:
                self.setCurrentSection(QDateTimeEdit.Section.SecondSection)
                self.stepBy(-1)
                return True  # Event handled
        return super().eventFilter(obj, event)
    def focusInEvent(self, event):
        """
        Sets focus in secconds when gets focus
        """
        super().focusInEvent(event)
        self.setCurrentSection(QDateTimeEdit.Section.SecondSection)
                        