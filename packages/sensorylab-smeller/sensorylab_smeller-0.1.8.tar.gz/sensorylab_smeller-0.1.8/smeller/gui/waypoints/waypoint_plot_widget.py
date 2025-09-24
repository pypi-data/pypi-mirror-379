# smeller/gui/waypoint_plot_widget.py
import pyqtgraph as pg
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGraphicsDropShadowEffect, QFrame, QSizePolicy, QGroupBox, QPushButton, QButtonGroup, QRadioButton
from PyQt6.QtGui import QColor, QPalette, QAction
from PyQt6.QtCore import Qt, QTimer
from smeller.gui.waypoints.waypoint import PlotWidget  # Ensure correct import of your WaypointPlotWidget class
from smeller.config.constants import LINEAR, EXPONENTIAL, SINUSOIDAL, STEP
import logging

logger = logging.getLogger(__name__)

class WaypointPlotWidget(QWidget):
    def __init__(self, parent=None, view_model=None, channel_index=0, channel_color=QColor(128,128,128,128)):
        super().__init__(parent)
        self.plot_widget = None
        self.plot_frame = None
        self.plot_layout = None
        self.interpolation_group = None
        self.interpolation_buttons = None
        self.interp_type_names = [LINEAR, EXPONENTIAL, SINUSOIDAL, STEP]
        self.neon_border_color = QColor(80, 165, 225)
        self.view_model = view_model #  Сохраняем ViewModel
        self.channel_index = channel_index
        self.channel_color = channel_color
        self._init_ui()

    def _init_ui(self):
        """Initializes the WaypointPlotWidget."""
        self.plot_widget = PlotWidget(channel_index=self.channel_index, channel_color=self.channel_color, view_model=self.view_model, parent=self) # Pass initial color
        self.plot_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        #self.plot_widget.setMinimumHeight(260)
        self.plot_widget.setContentsMargins(0, 0, 0, 0)
        self.plot_frame = QFrame()
        self.plot_frame.setObjectName("PlotFrame")
        self.plot_layout = QVBoxLayout(self.plot_frame)
        self.plot_layout.setSpacing(4)
        self.plot_layout.setContentsMargins(0, 0, 0, 0)
        
        self.plot_and_buttons = QHBoxLayout()
        self.plot_and_buttons.setContentsMargins(0, 0, 0, 0)
        self.plot_and_buttons.setSpacing(0)

        # --- Interpolation Type Group ---
        self.interpolation_group = QGroupBox()
        self.interpolation_group.setFixedHeight(32)
        # --- Применяем стили к interpolation_group ---
        interpolation_layout = QHBoxLayout(self.interpolation_group)

        self.interpolation_buttons = QButtonGroup(self)
        self.interpolation_buttons.setExclusive(True)

        for i, interp_type_str in enumerate(
                self.interp_type_names):
            btn = QRadioButton(interp_type_str)
            interpolation_layout.addWidget(btn)
            self.interpolation_buttons.addButton(btn, i)

            if interp_type_str == LINEAR:
                btn.setChecked(True)
                
        self.plot_layout.addWidget(self.interpolation_group, 0, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)  # 0 - stretch factor, Qt.AlignHCenter - выравнивание
        self.plot_and_buttons.addWidget(self.plot_widget, stretch=1)
        self.plot_layout.addLayout(self.plot_and_buttons)
        self.setLayout(self.plot_layout)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(self.neon_border_color)
        shadow.setXOffset(0)
        shadow.setYOffset(3)
        self.setGraphicsEffect(shadow)

    def connect_signals(self, main_window):
        """Подключаем сигналы к MainWindow."""
        self.interpolation_buttons.buttonClicked.connect(self.update_interpolation_type)

        self.plot_widget.waypoint_moved.connect(main_window.on_waypoint_moved)
        self.plot_widget.waypoint_added.connect(main_window.on_waypoint_added)
        self.plot_widget.waypoint_deleted.connect(main_window.on_waypoint_deleted)
        
    def set_interpolation_button_from_viewmodel(self, interp_type: str):
        for btn in self.interpolation_buttons.buttons():
            button_id = self.interpolation_buttons.id(btn)
            button_interp_type_name = self.interp_type_names[button_id]
            if button_interp_type_name == interp_type:
                btn.setChecked(True)
                break
        self.plot_widget.set_interpolation_type(interp_type)
        QTimer.singleShot(0, self.plot_widget.update_plot)

    def update_interpolation_type(self, button: QRadioButton):
        interp_type_index = self.interpolation_buttons.id(button)
        interp_type_str = self.interp_type_names[interp_type_index]
        
        self.view_model.update_interpolation_type(interp_type_str) #  Вызываем метод ViewModel из MainWindow

    def set_plot_interpolation_type(self, interp_type: str):
        self.plot_widget.set_interpolation_type(interp_type)

    def add_channel_manager(self, channel_manager):
        """
        Добавляет панель управления под графиком.
        
        Аргументы:
            channel_manager (QWidget): Виджет, представляющий панель управления.
        """
        self.plot_and_buttons.addWidget(channel_manager, stretch=0)

    def set_default_interpolation(self):
        """
        Устанавливает интерполяцию по умолчанию (линейную) и обновляет график.
        """
        self.plot_widget.set_interpolation_type(LINEAR)
        self.plot_widget.update_plot()