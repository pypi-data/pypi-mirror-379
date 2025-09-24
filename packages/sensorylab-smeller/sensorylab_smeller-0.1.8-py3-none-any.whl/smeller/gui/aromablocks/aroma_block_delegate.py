# Содержимое файла: smeller/gui/aroma_block_delegate.py
from PyQt6.QtWidgets import QStyledItemDelegate
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

class AromaBlockDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        """Переопределяем метод paint для отрисовки."""
        model = index.model()
        if model and hasattr(model, 'get_active_aromablock_id') and hasattr(model, 'get_aromablock_id'): # Проверяем наличие необходимых методов
            aromablock_id = model.get_aromablock_id(index.row())
            active_id = model.get_active_aromablock_id()

            if aromablock_id == active_id and active_id is not None and aromablock_id is not None:
                # Рисуем активный элемент с другим фоном
                option.backgroundBrush = QColor("#FFFFCC")  # Светло-желтый фон, например
                option.font.setBold(True) # Жирный шрифт
                option.palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.darkBlue) # Темно-синий текст

        # Вызываем стандартный метод отрисовки, чтобы нарисовать текст и т.д.
        super().paint(painter, option, index)