# ui_components/menu_bar_manager.py

from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction

class MenuBarManager:
    """
    MenuBarManager отвечает за создание и настройку строки меню.
    Он создает меню "Файл", "Правка" и "Стиль" с необходимыми действиями.
    """

    def __init__(self, parent):
        self.parent = parent
        self.menu_bar = QMenuBar(parent)
        self._create_menus()

    def _create_menus(self):
        # Меню "Файл"
        self.file_menu = self.menu_bar.addMenu("Файл")
        self.create_aromablock_action = QAction("Создать Аромаблок...", self.parent)
        self.save_action = QAction("Сохранить", self.parent)
        self.save_aromablock_action = QAction("Сохранить Аромаблок как...", self.parent)
        self.file_menu.addAction(self.create_aromablock_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_aromablock_action)

        # Меню "Правка"
        self.edit_menu = self.menu_bar.addMenu("Правка")
        self.undo_action = QAction("Назад (интенсивность)", self.parent)
        self.edit_menu.addAction(self.undo_action)
        # === Settings Menu ===
        self.settings_menu = self.menu_bar.addMenu("Настройки")
        self.device_connection_settings_action = QAction("Подключение устройства", self.parent) #  Новый пункт меню
        self.settings_menu.addAction(self.device_connection_settings_action)
        # Меню "Стиль"
        self.style_menu = self.menu_bar.addMenu("Стиль")
        self.set_dark_action = QAction("Темная тема", self.parent)
        self.set_white_action = QAction("Светлая тема", self.parent)
        self.style_menu.addAction(self.set_dark_action)
        self.style_menu.addAction(self.set_white_action)

    def get_menu_bar(self):
        """
        Возвращает экземпляр QMenuBar, который можно установить в MainWindow.
        """
        return self.menu_bar
    
    def connect_signals(self, main_window):
        self.create_aromablock_action.triggered.connect(main_window.open_create_aromablock_dialog)
        self.save_action.triggered.connect(main_window.save_selected_aromablock) #  Подключаем к функции save_selected_aromablock
        self.save_aromablock_action.triggered.connect(main_window.open_create_aromablock_dialog) #  Connect "Save AromaBlock"
        self.undo_action.triggered.connect(main_window.undo_last_action) 
        self.set_dark_action.triggered.connect(main_window.set_theme_dark)
        self.set_white_action.triggered.connect(main_window.set_theme_white)
        self.device_connection_settings_action.triggered.connect(main_window.open_device_connection_dialog)