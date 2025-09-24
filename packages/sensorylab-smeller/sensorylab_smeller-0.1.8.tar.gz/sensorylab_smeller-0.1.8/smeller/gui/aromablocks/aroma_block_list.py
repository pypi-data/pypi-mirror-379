# gui/aromablock_list.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableView, QFrame, QPushButton,
    QAbstractItemView, QHeaderView, QMenu
)
from PyQt6.QtCore import Qt
from smeller.dynamic_control.aroma_table_model import AromaBlockTableModel
from smeller.gui.aromablocks.aroma_block_delegate import AromaBlockDelegate
import logging

logger = logging.getLogger(__name__)


class AromablockList(QWidget):
    def __init__(self, view_model, parent=None):
        super().__init__(parent)
        
        self.view_model = view_model
        self._init_ui()

    def _init_ui(self):
        # Фрейм для таблицы и кнопок
        self.list_frame = QFrame()
        self.list_layout = QVBoxLayout(self.list_frame)
        self.list_layout.setContentsMargins(0, 0, 0, 0)

        # Подпись списка аромаблоков
        self.label = QLabel("Список аромаблоков")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.list_layout.addWidget(self.label)

        # Таблица для отображения аромаблоков
        self.table_view = QTableView()
        self.table_view.setContentsMargins(0, 0, 0, 0)
        self.table_view.setMinimumWidth(140)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_view.verticalHeader().setHidden(True)
        self.table_view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        # Создаём модель таблицы
        self.table_model = AromaBlockTableModel(self.view_model)  # ViewModel будет установлена позже
        self.table_view.setModel(self.table_model)
        self.table_view.setItemDelegate(AromaBlockDelegate(self))


        self.list_layout.addWidget(self.table_view, stretch=1)

        # Layout для кнопок под таблицей
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.refresh_button = QPushButton("Обновить")
        self.save_button = QPushButton("Сохранить")
        self.buttons_layout.addWidget(self.refresh_button)
        self.buttons_layout.addWidget(self.save_button)
        self.list_layout.addLayout(self.buttons_layout)

        # Основной layout для всего списка
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.list_frame)
        self.setLayout(main_layout)

    def connect_signals(self, main_window):
        """
        Подключаем сигналы:
         – кнопки обновления и сохранения
         – двойной клик по таблице
         – контекстное меню (открывает окно с опциями)
         Все события будут делегироваться методам MainWindow.
        """
        self.refresh_button.clicked.connect(main_window.refresh_aromablocks_list)
        self.save_button.clicked.connect(main_window.save_selected_aromablock)
        self.table_view.doubleClicked.connect(main_window.load_selected_aromablock_from_table)
        self.table_view.customContextMenuRequested.connect(
            lambda pos: self._open_context_menu(pos, main_window)
        )
        # Если у модели появится сигнал dataChanged, можно сделать:
        self.table_model.dataChanged.connect(self.table_view.viewport().update)

    def _open_context_menu(self, position, main_window):
        index = self.table_view.indexAt(position)
        if not index.isValid():
            return

        menu = QMenu(self)
        open_action = menu.addAction("Открыть")
        delete_action = menu.addAction("Удалить")
        copy_action = menu.addAction("Копировать")

        action = menu.exec(self.table_view.viewport().mapToGlobal(position))
        if action == open_action:
            main_window.load_selected_aromablock_from_table(index)
        elif action == delete_action:
            main_window.delete_selected_aromablock_from_table(index)
        elif action == copy_action:
            main_window.copy_selected_aromablock_from_table(index)

    def update_table_view(self, aromablocks_list: list, current_aromablock_id=None):
        """
        Обновляет модель таблицы данными из списка аромаблоков и, если нужно, выделяет активную строку.
        """
        self.table_model.set_aromablocks(aromablocks_list)
        # Если список пуст – можно установить placeholder
        if not aromablocks_list and not self.table_model.placeholder_set:
            self.table_model.set_placeholder_message("Нет созданных аромаблоков")
        # Если требуется, выделяем активный аромаблок
        if current_aromablock_id is not None:
            for row in range(len(aromablocks_list)):
                block_id = self.table_model.get_aromablock_id(row)
                if block_id == current_aromablock_id:
                    selection_model = self.table_view.selectionModel()
                    model_index = self.table_model.index(row, 0)
                    if model_index.isValid():
                        selection_model.clearSelection()
                        selection_model.select(model_index, 
                                                selection_model.SelectionFlag.Select | selection_model.SelectionFlag.Rows
                        )
                    break