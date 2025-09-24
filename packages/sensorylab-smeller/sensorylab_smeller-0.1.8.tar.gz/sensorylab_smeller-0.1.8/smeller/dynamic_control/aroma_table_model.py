# smeller/dynamic_control/aroma_table_model.py
from PyQt6.QtCore import  Qt, QAbstractTableModel, QModelIndex, QVariant
from typing import List, Optional
from smeller.models.aroma_block import AromaBlock
from smeller.dynamic_control.view_model import MainWindowViewModel

import logging

logger = logging.getLogger(__name__)


# --- AromaBlockTableModel ---
class AromaBlockTableModel(QAbstractTableModel):
    """
    Модель для отображения списка AromaBlock в QTableView.
    """
    def __init__(self, view_model: MainWindowViewModel, parent=None):
        super().__init__(parent)
        self.aromablocks: List[AromaBlock] = []
        self.headers = ["ID", "Имя", "Start", "Stop"]#  Заголовки столбцов
        self.view_model = view_model
        self.placeholder_message = None #  Сообщение-заглушка
        self.placeholder_set = False #  Флаг, что заглушка установлена
        self._active_aromablock_id = None 
        
    def set_active_aromablock_id(self, aromablock_id): # <----  Убедись, что есть этот метод
        """Устанавливает ID активного аромаблока."""
        if self._active_aromablock_id != aromablock_id:
            # Сбрасываем старый индекс
            if self._active_aromablock_id is not None:
                old_index = self.index_by_id(self._active_aromablock_id)
                if old_index.isValid():
                    self.dataChanged.emit(old_index, old_index)  # Уведомляем о смене

            self._active_aromablock_id = aromablock_id

            # Устанавливаем новый
            new_index = self.index_by_id(self._active_aromablock_id)
            if new_index.isValid():
                self.dataChanged.emit(new_index, new_index) # Уведомляем о смене

    def get_active_aromablock_id(self): # <----  Убедись, что есть этот метод
        """Возвращает ID активного аромаблока."""
        return self._active_aromablock_id
       
    def set_aromablocks(self, blocks: List[AromaBlock]):
        self.beginResetModel() #  Сигнал для QTableView о полном обновлении данных
        self.aromablocks = blocks
        self.placeholder_set = False # Сбрасываем флаг заглушки при обновлении данных
        self.endResetModel()

    def set_placeholder_message(self, message: str):
        self.beginResetModel()
        self.placeholder_message = message
        self.placeholder_set = True
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        if self.placeholder_set:
            return 1 #  Одна строка для заглушки
        return len(self.aromablocks)

    def columnCount(self, parent=QModelIndex()):
        if self.placeholder_set:
            return 1 #  Один столбец для заглушки
        return len(self.headers)

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return QVariant()

        if self.placeholder_set: # Если установлен placeholder
            if role == Qt.ItemDataRole.DisplayRole and index.row() == 0 and index.column() == 0:
                return self.placeholder_message #  Возвращаем сообщение-заглушку
            return QVariant() #  Для остальных ролей и ячеек возвращаем пустой Variant

        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            block = self.aromablocks[row]

            if col == 0:
                return str(block.id)
            elif col == 1:
                return block.name
            elif col == 2:
                return block.start_time
            elif col == 3:
                return block.stop_time
        return QVariant()

    def headerData(self, section: int, orientation: Qt.Orientation, role=Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            if not self.placeholder_set: # Заголовки столбцов не показываем, если установлен placeholder
                return self.headers[section]
            else:
                return "" #  Пустые заголовки, если placeholder
        return QVariant()

    def get_aromablock_id(self, row: int) -> Optional[int]:
        """Возвращает ID аромаблока по индексу строки."""
        if 0 <= row < len(self.aromablocks):
            return self.aromablocks[row].id
        return None
    def index_by_id(self, block_id: int) -> QModelIndex:
        """Возвращает QModelIndex для строки с заданным ID аромаблока."""
        for row, block in enumerate(self.aromablocks):
            if block.id == block_id:
                return self.index(row, 0) # Возвращаем индекс для первой колонки
        return QModelIndex() # Возвращает невалидный индекс, если ID не найден
