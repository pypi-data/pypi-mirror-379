# main_window/main_window.py

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QTime
from smeller.gui.ui_manager import UIManager
from smeller.gui.connectors import SetupConnector
import asyncio

import logging
logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self, view_model, *args, **kwargs):
        """
        Основное окно приложения, которое делегирует сборку интерфейса UIManager'у
        и настройку сигналов и слотов классу SetupConnector.
        """
        super().__init__(*args, **kwargs)
        self.view_model = view_model

        # Создаем менеджер интерфейса, который отвечает за сборку центрального виджета и всех компонентов
        self.ui_manager = UIManager(parent=self, view_model=self.view_model)
        self.setCentralWidget(self.ui_manager.get_central_widget())
        self.ui_manager.build_ui()

        # Создаем и инициализируем соединители (connectors) для установки сигналов/слотов между компонентами и ViewModel
        self.connector = SetupConnector(view_model=self.view_model, ui_manager=self.ui_manager)
        self.connector.setup_connections()

        # Устанавливаем начальные значения и состояние интерфейса
        self.ui_manager.set_initial_values()
     