# smeller/gui/control_panel.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame
from PyQt6.QtCore import Qt, QTime
from smeller.gui.control_panel.timeline_player import TimelinePlayer
from smeller.gui.control_panel.seconds_time_edit import SecondsTimeEdit # Предполагается, что SecondsTimeEdit выделен в отдельный файл, если нет - нужно будет его тоже выделить

class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.timeline_player = None  # Инициализация timeline_player
        self.total_duration_timeedit = None # Инициализация total_duration_timeedit
        self._init_ui()

    def _init_ui(self):
        """Initializes the control panel UI (below the plot)."""
        layout = QVBoxLayout(self)
        # Здесь вместо мультимедийного плеера используем наш TimelinePlayer
        self.timeline_player = TimelinePlayer()

        layout.addWidget(self.timeline_player, stretch=0, alignment=Qt.AlignmentFlag.AlignBottom)
        self.total_duration_timeedit = SecondsTimeEdit()
        self.total_duration_timeedit.setDisplayFormat("hh:mm:ss")
        self.timeline_player.layout.addWidget(self.total_duration_timeedit)
        self.setLayout(layout)

    def connect_signals(self, main_window): #  Теперь принимаем MainWindow для подключения сигналов
        """Подключение сигналов к слотам MainWindow."""
        self.timeline_player.play_pressed.connect(main_window.start_control) # Play signal -> start_control
        self.timeline_player.pause_pressed.connect(main_window.pause_control) # Pause signal -> pause_control (новый метод)
        self.timeline_player.stop_pressed.connect(main_window.stop_control) # Stop signal -> stop_control
        
        self.timeline_player.set_volume.connect(main_window.set_volume) # Step signal -> set_volume

        self.timeline_player.current_time_changed.connect(main_window.on_current_time_changed)
        self.timeline_player.manual_seeked.connect(main_window.on_manual_seeked)
        self.timeline_player.manual_aroma_seeked.connect(main_window.on_manual_aroma)
        self.timeline_player.manual_aroma_start.connect(main_window.start_control)

        # Предполагается, что SecondsTimeEdit определен где-то или будет перемещен сюда
        self.total_duration_timeedit.timeChanged.connect(main_window.update_total_duration) # Изменили
        
