# gui/channel_manager.py

import sys, os
import asyncio
import pyqtgraph as pg
import math

from pathlib import Path
project_root = Path(__file__).resolve().parents[2]  # Поднимаемся на два уровня вверх
sys.path.append(str(project_root))

import logging
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QAbstractButton, QLabel, QDialog, QGridLayout, QGroupBox, QPushButton, QButtonGroup, QMenu, QColorDialog, QMessageBox
from PyQt6.QtGui import QColor, QPalette, QAction
from PyQt6.QtCore import Qt, pyqtSignal
from smeller.gui.channels.channel_button import ChannelButton
from smeller.config.constants import MAX_CHANNELS
import logging

logger = logging.getLogger(__name__)

class ChannelManager(QWidget):
    
    index_cartridge_info = pyqtSignal(int)
    index_channel_color = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.channel_buttons = None
        self.channel_button_widgets = {}
        self.current_channel_index = -2
        self.fan_button = None
        self.neon_border_color = QColor(80, 165, 225) #  Перенесли цвет неона
        self._init_ui()

    def _init_ui(self):
        """Initializes the channel selection buttons."""
        
        
        channel_button_layout = QVBoxLayout(self)
        channel_button_layout.setContentsMargins(0,0,0,0)
        channel_button_layout.setSpacing(4)

        channel_button_layout.addStretch(0)
        
        buttons_group = QGroupBox()
        buttons_group.setObjectName("BtnGBox")
        grid_layout = QGridLayout(buttons_group)
        grid_layout.setSpacing(4)
        self.channel_buttons = QButtonGroup(self)
        self.channel_buttons.setExclusive(True)
        self.channel_button_widgets = {} # Словарь для хранения виджетов кнопок

        for i in range(MAX_CHANNELS):
            btn = ChannelButton(i)
            btn.setObjectName("channelButton")
            btn.setText(f"{i + 1}")

            btn.setCheckable(True)
            self.channel_buttons.addButton(btn, i)
            row = i // 4  # Целочисленное деление для определения строки
            col = i % 4   # Остаток от деления для определения столбца
            grid_layout.addWidget(btn, row, col)
            btn.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
            btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
            btn.customContextMenuRequested.connect(self.open_channel_context_menu)  # Connect context menu
            # Подключаем новые сигналы ChannelButton к обработчикам-заглушкам
            btn.long_press_activated.connect(self.on_channel_button_long_press)
            #btn.double_click_activated.connect(self.on_channel_button_double_click)
            #btn.hold_activated.connect(self.on_channel_button_hold)
            btn.setFixedWidth(55)
            self.channel_button_widgets[i] = btn  # Сохраняем виджет кнопки
              # Enable context menu
        self.fan_button = ChannelButton(-2)
        self.channel_buttons.addButton(self.fan_button, -2)
        self.channel_button_widgets[-2] = self.fan_button  # Сохраняем виджет кнопки
        self.fan_button.setObjectName("fanButton") #  Устанавливаем objectName "fanButton" для стилизации
        self.fan_button.setText("Вентилятор") #  Устанавливаем objectName "fanButton" для стилизации
        self.fan_button.setCheckable(True) # Сделаем кнопку переключаемой
        self.fan_button.setFixedHeight(30)
         # Сохраняем ссылку на кнопку вентилятора
        #self.fan_button.clicked.connect(self.on_fan_button_clicked) # Подключаем обработчик
        grid_layout.addWidget(self.fan_button, 3, 0, 1, 4)
        # Добавляем сетку с кнопками в основной лейаут
        channel_button_layout.addWidget(buttons_group, stretch=1)
        self.setLayout(channel_button_layout)


    def connect_signals(self, main_window):
        """Подключаем сигналы к MainWindow."""
        self.channel_buttons.buttonClicked[QAbstractButton].connect(main_window.switch_channel_from_button)
        self.index_cartridge_info.connect(main_window._set_cartridge_info)
        self.index_channel_color.connect(main_window._set_channel_color)
        
        #self.fan_button.clicked.connect(main_window.on_fan_button_clicked) # Подключаем обработчик

    def open_channel_context_menu(self, position):
        """Opens context menu for channel buttons."""
        channel_index = None
        for index, btn in self.channel_button_widgets.items():
            if btn == self.sender(): # Determine which button was clicked
                channel_index = index
                break
        if channel_index is None:
            return

        menu = QMenu(self)
        set_cartridge_action = menu.addAction("Set Cartridge Info")
        set_color_action = menu.addAction("Set Color")

        action = menu.exec(self.channel_button_widgets[channel_index].mapToGlobal(position))
        if action == set_cartridge_action:
            self.index_cartridge_info.emit(channel_index) # Вызываем метод MainWindow
        elif action == set_color_action:
            self.index_channel_color.emit(channel_index) # Вызываем метод MainWindow


   
    def on_channel_button_long_press(self, channel_index: int):
        """Заглушка для обработки долгого нажатия кнопки канала."""
        logger.info(f"Долгое нажатие на кнопке канала {channel_index }")

    def on_channel_button_double_click(self, channel_index: int):
        """Заглушка для обработки двойного клика кнопки канала."""
        logger.info(f"Двойной клик на кнопке канала {channel_index }")

    def on_channel_button_hold(self, channel_index: int):
        """Заглушка для обработки удержания кнопки канала."""
        logger.info(f"Удержание кнопки канала {channel_index }")

    def on_fan_button_clicked(self, checked: bool): # Placeholder, logic moved to MainWindow
        pass


    def update_channel_button_color(self, channel_index: int, color: QColor = None):
        """
        Обновляет цвет кнопки канала и устанавливает контрастный цвет текста.

        Args:
            channel_index (int): Индекс канала (0-based).
            color (QColor, optional): Цвет фона для установки. Если None, цвет кнопки сбрасывается.
        """
        if channel_index not in self.channel_button_widgets:
            logger.warning(f"No button widget found for channel index: {channel_index}")
            return
        button = self.channel_button_widgets[channel_index]
        if color is not None:
            #  Определяем контрастный цвет текста
            text_color = self._get_contrasting_text_color(color)
            #  Устанавливаем цвет фона кнопки и контрастный цвет текста.
            button.setStyleSheet(f"background-color: {color.name()}; color: {text_color.name()}; border: none;")
        else:
            #  Сбрасываем цвет кнопки к стандартному стилю и цвет текста к стандартному (тема определит)
            button.setStyleSheet("")

    def _get_contrasting_text_color(self, background_color: QColor) -> QColor:
        """
        Определяет контрастный цвет текста (белый или черный) для заданного цвета фона.

        Args:
            background_color (QColor): Цвет фона.

        Returns:
            QColor: Контрастный цвет текста (QColor.GlobalColor.white или QColor.GlobalColor.black).
        """
        #  Формула для расчета perceived luminance (пример, упрощенная версия)
        luminance = (0.299 * background_color.redF() +
                     0.587 * background_color.greenF() +
                     0.114 * background_color.blueF())

        #  Порог, определяющий, какой фон считать "светлым"
        #  Порог можно настроить, значения от 0.5 до 0.7 могут быть подходящими
        if luminance > 0.5:
            return QColor(Qt.GlobalColor.black) #  Возвращаем черный цвет для светлого фона
        else:
            return QColor(Qt.GlobalColor.white) #  Возвращаем белый цвет для темного фона

    def highlight_current_channel_button(self, channel_index: int):
        if not self.channel_buttons:
            return
        for btn in self.channel_buttons.buttons():
            btn.setChecked(self.channel_buttons.id(btn) == channel_index)

    def get_channel_button(self, channel_index):
        """Возвращает виджет кнопки канала по индексу."""
        return self.channel_button_widgets.get(channel_index)
    
    
    
