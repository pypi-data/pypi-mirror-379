# gui/theme_manager.py

import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
import logging

logger = logging.getLogger(__name__)


class ThemeManager:
    def __init__(self, parent=None, plot_widget=None):
        """
        ThemeManager применяет выбранную тему ко всему приложению.

        Аргументы:
            parent (QWidget): Родительский виджет (обычно MainWindow), которому будет установлен общий стиль.
            plot_widget (QWidget): Виджет графика, которому будут заданы дополнительные стили (если необходимо).
        """
        self.parent = parent
        self.plot_widget = plot_widget

    def apply_theme(self, theme_name: str):
        app = QApplication.instance()
        if theme_name.lower() == 'dark':
            app.setStyle("Fusion")
            palette = QPalette()
            palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
            palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
            palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
            app.setPalette(palette)

            pg.setConfigOption('background', 'k')
            pg.setConfigOption('foreground', 'w')

            # Применяем стили для виджета графика, если он указан
            if self.plot_widget is not None:
                self.plot_widget.setStyleSheet("""
                    border-top-left-radius: 15px;
                    border-top-right-radius: 0px;
                    border-bottom-left-radius: 15px;
                    border-bottom-right-radius: 0px;
                    background-color: qlineargradient(
                        x1: 0, y1: 0, x2: 0, y2: 1,
                        stop: 0 rgb(30, 30, 30),
                        stop: 1 rgb(50, 50, 50)
                    );
                    border-top: 2px solid rgb(0, 195, 255);
                    border-right: 0px solid rgb(0, 195, 255);
                    border-bottom: 2px solid rgb(0, 195, 255);
                    border-left: 2px solid rgb(0, 195, 255);
                    padding: 5px;
                """)

            # Устанавливаем стиль для основного окна (и дочерних виджетов)
            if self.parent is not None:
                self.parent.setStyleSheet("""
                    QMainWindow {
                        background-color: #353535;
                        color: white;
                    }
                    QPushButton {
                        background-color: #555555;
                        color: white;
                        border: 1px solid #777777;
                        border-radius: 10px;
                        padding: 5px;
                    }
                    QPushButton:hover {
                        background-color: #777777;
                    }
                    QPushButton:checked {
                        background-color: #acacac;
                    }
                    QLabel {
                        color: white;
                    }
                    QComboBox {
                        background-color: #555555;
                        color: white;
                        border: 1px solid #777777;
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QMenuBar {
                        background-color: #444444;
                        color: white;
                    }
                    QMenuBar::item {
                        background-color: transparent;
                    }
                    QMenuBar::item:selected {
                        background-color: #777777;
                    }
                    QMenu {
                        background-color: #444444;
                        color: white;
                        border: 1px solid #777777;
                    }
                    QMenu::item:selected {
                        background-color: #777777;
                    }
                    QTableView {
                        background-color: #444444;
                        color: white;
                        border: 1px solid #777777;
                        gridline-color: #666666;
                        border-radius: 10px;
                        padding: 4px;
                    }
                    QTableView::item:selected {
                        background-color: rgba(0, 195, 255, 150);
                        color: white;
                    }
                    QHeaderView::section {
                        background-color: #555555;
                        color: white;
                        border: none;
                        border-bottom: 2px solid rgb(0, 195, 255);
                        padding: 4px;
                    }
                    QGroupBox#BtnGBox {
                        border: 2px solid rgb(0, 195, 255);
                        border-left: 1px solid rgb(0, 195, 255);
                        background-color: qlineargradient(
                            x1: 0, y1: 0, x2: 0, y2: 1,
                            stop: 0 rgb(15, 15, 45),
                            stop: 1 rgb(30, 30, 50)
                        );
                        border-top-left-radius: 0px;
                        border-top-right-radius: 15px;
                        border-bottom-left-radius: 0px;
                        border-bottom-right-radius: 15px;
                    }
                    QGroupBox {
                        border: 2px solid rgb(0, 195, 255);
                        background-color: qlineargradient(
                            x1: 0, y1: 0, x2: 0, y2: 1,
                            stop: 0 rgb(15, 15, 45),
                            stop: 1 rgb(30, 30, 50)
                        );
                        border-top-left-radius: 15px;
                        border-top-right-radius: 15px;
                        border-bottom-left-radius: 15px;
                        border-bottom-right-radius: 15px;
                    }
                    QGroupBox::title {
                        subcontrol-origin: margin;
                        subcontrol-position: top center;
                        padding: 0 0px;
                        background-color: qlineargradient(
                            x1: 0, y1: 0, x2: 0, y2: 1,
                            stop: 0 rgb(30, 30, 30),
                            stop: 1 rgb(50, 50, 50)
                        );
                        color: white;
                    }
                    QRadioButton {
                        color: white;
                    }
                """)

        elif theme_name.lower() == 'light':
            app.setPalette(app.style().standardPalette())

            pg.setConfigOption('background', 'w')
            pg.setConfigOption('foreground', 'k')

            if self.plot_widget is not None:
                self.plot_widget.setStyleSheet("""
                    border-top-left-radius: 15px;
                    border-top-right-radius: 0px;
                    border-bottom-left-radius: 15px;
                    border-bottom-right-radius: 0px;
                    background-color: qlineargradient(
                        x1: 0, y1: 0, x2: 0, y2: 1,
                        stop: 0 rgb(240, 240, 240),
                        stop: 1 rgb(255, 255, 255)
                    );
                    border-top: 2px solid rgb(150, 150, 150);
                    border-right: 0px solid rgb(150, 150, 150);
                    border-bottom: 2px solid rgb(150, 150, 150);
                    border-left: 2px solid rgb(150, 150, 150);
                    padding: 5px;
                """)

            if self.parent is not None:
                self.parent.setStyleSheet("""
                    QMainWindow {
                        background-color: #f0f0f0;
                        color: black;
                    }
                    QPushButton {
                        background-color: #e0e0e0;
                        color: black;
                        border: 1px solid #c0c0c0;
                        border-radius: 10px;
                        padding: 5px;
                    }
                    QPushButton:hover {
                        background-color: #d0d0d0;
                    }
                    QPushButton:checked {
                        background-color: #acacac;
                    }
                    QLabel {
                        color: black;
                    }
                    QComboBox {
                        background-color: #e0e0e0;
                        color: black;
                        border: 1px solid #c0c0c0;
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QMenuBar {
                        background-color: #f0f0f0;
                        color: black;
                        border-bottom: 1px solid #c0c0c0;
                    }
                    QMenuBar::item {
                        background-color: transparent;
                    }
                    QMenuBar::item:selected {
                        background-color: #d0d0d0;
                    }
                    QMenu {
                        background-color: #f0f0f0;
                        color: black;
                        border: 1px solid #c0c0c0;
                    }
                    QMenu::item:selected {
                        background-color: #d0d0d0;
                    }
                    QTableView {
                        background-color: #ffffff;
                        color: black;
                        border: 1px solid #c0c0c0;
                        gridline-color: #e0e0e0;
                        border-radius: 10px;
                        padding: 4px;
                    }
                    QTableView::item:selected {
                        background-color: rgba(200, 230, 255, 150);
                        color: black;
                    }
                    QHeaderView::section {
                        background-color: #e0e0e0;
                        color: black;
                        border: none;
                        border-bottom: 2px solid #c0c0c0;
                        padding: 4px;
                    }
                    QGroupBox#BtnGBox {
                        color: black;
                        border: 2px solid rgb(150, 150, 150);
                        border-left: 1px solid rgb(150, 150, 150);
                        background-color: qlineargradient(
                            x1: 0, y1: 0, x2: 0, y2: 1,
                            stop: 0 rgb(240, 240, 240),
                            stop: 1 rgb(255, 255, 255)
                        );
                        border-top-left-radius: 0px;
                        border-top-right-radius: 15px;
                        border-bottom-left-radius: 0px;
                        border-bottom-right-radius: 15px;
                    }
                    QGroupBox {
                        color: black;
                        border: 2px solid rgb(150, 150, 150);
                        background-color: qlineargradient(
                            x1: 0, y1: 0, x2: 0, y2: 1,
                            stop: 0 rgb(240, 240, 240),
                            stop: 1 rgb(255, 255, 255)
                        );
                        border-top-left-radius: 15px;
                        border-top-right-radius: 15px;
                        border-bottom-left-radius: 15px;
                        border-bottom-right-radius: 15px;
                    }
                    QRadioButton {
                        color: black;
                    }
                """)
        else:
            logger.warning(f"Unknown theme: {theme_name}")

        # Если у виджета графика есть метод set_theme, применяем его
        if self.plot_widget is not None and hasattr(self.plot_widget, "set_theme"):
            self.plot_widget.set_theme(theme_name)