# smeller/gui/aroma_block_dialog.py
from PyQt6.QtWidgets import (
    QComboBox, QLineEdit,
    QDialog, QDialogButtonBox, QFormLayout, QTextEdit,
    QDialogButtonBox, QPushButton,
    QFileDialog, QHBoxLayout, QLabel
    
    )
from PyQt6.QtCore import Qt
import logging

logger = logging.getLogger(__name__)

class AromaBlockSaveDialog(QDialog):
    """
    Кастомный диалог для сохранения AromaBlock с объединенными полями ввода.
    """
    def __init__(self, parent=None, theme_name="dark"):
        
        logger.debug("AromaBlockSaveDialog.__init__ вызван") # Или используй logger
        super().__init__(parent)
        self.setWindowTitle("Сохранить AromaBlock")
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint) # Убираем кнопки "закрыть", "свернуть", "развернуть"
        self.setObjectName("aromaBlockSaveDialog") #  Для стилизации

        self.theme_name = theme_name

        self.form_layout = QFormLayout(self)

        self.name_edit = QLineEdit()
        self.form_layout.addRow("Имя аромаблока:", self.name_edit)

        self.description_edit = QTextEdit() #  QTextEdit для многострочного описания
        self.form_layout.addRow("Описание (опционально):", self.description_edit)

        self.data_type_combobox = QComboBox()
        self.data_type_combobox.addItems([
            "video", "audio track", "exhibition aromatization setup",
            "theatrical performance setup", "aroma marketing setup", "aroma testing setup"
        ]) #  Примеры типов контента
        self.form_layout.addRow("Тип контента:", self.data_type_combobox)

        self.content_link_edit = QLineEdit()
        self.form_layout.addRow("Ссылка на контент (опционально):", self.content_link_edit)
        # --- Добавляем кнопку "Загрузить видео" ---
        self.load_video_button = QPushButton("Загрузить видео", self)
        self.load_video_button.clicked.connect(self.load_video_file)
        self.video_file_label = QLabel("Файл не выбран", self) #  Добавляем QLabel
        self.video_file_label.setWordWrap(True)  #  Разрешаем перенос слов

        video_layout = QHBoxLayout()  #  Используем QHBoxLayout для размещения кнопки и QLabel рядом
        video_layout.addWidget(self.load_video_button)
        video_layout.addWidget(self.video_file_label)
        self.form_layout.addRow("Видео файл (опционально):", video_layout)  #  Используем layout

        self.video_path = None  # Для хранения пути к видеофайлу

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel) #  Кнопки "Сохранить" и "Отмена"
        self.button_box.accepted.connect(self.accept) #  При нажатии "Сохранить" - accept()
        self.button_box.rejected.connect(self.reject) #  При нажатии "Отмена" - reject()
        self.form_layout.addRow(self.button_box)

        self.setStyleSheet("""
            QDialog#aromaBlockSaveDialog {
                border-radius: 15px; /* Закругленные углы для всего диалога */
                /* Дополнительные стили, если необходимо */
            }
        """)
        self.apply_theme(self.theme_name) # Применяем тему к диалогу

    def load_video_file(self):
        """Открывает диалог выбора видеофайла и сохраняет путь."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выбрать видео файл", "", "Video Files (*.mp4 *.avi *.mkv *.mov);;All Files (*)"
        )
        if file_path:
            self.video_path = file_path
            self.video_file_label.setText(file_path) #  Устанавливаем текст QLabel
            print(f"Выбран видео файл: {self.video_path}")

    def get_aromablock_info(self):
        """Возвращает введенные данные аромаблока."""
        return (
            self.name_edit.text(),
            self.description_edit.toPlainText(), #  Используем toPlainText() для QTextEdit
            self.data_type_combobox.currentText(),
            self.content_link_edit.text(),
            self.video_path  # Возвращаем путь к видео
        )

    def apply_theme(self, theme_name: str):
        """Применяет тему к диалогу."""
        if theme_name.lower() == 'dark':
            self.setStyleSheet("""
                QDialog#aromaBlockSaveDialog {
                    background-color: #353535;
                    color: white;
                    border-radius: 15px;
                    padding: 20px;
                }
                QLabel { color: white; }
                QLineEdit, QTextEdit, QComboBox {
                    background-color: #555555;
                    color: white;
                    border: 1px solid #777777;
                    border-radius: 5px;
                    padding: 5px;
                }
                QDialogButtonBox QPushButton {
                    background-color: #555555;
                    color: white;
                    border: 1px solid #777777;
                    border-radius: 5px;
                    padding: 5px;
                    min-width: 80px;
                }
                QDialogButtonBox QPushButton:hover {
                    background-color: #777777;
                }
            """)
        elif theme_name.lower() == 'light':
            self.setStyleSheet("""
                QDialog#aromaBlockSaveDialog {
                    background-color: #f0f0f0;
                    color: black;
                    border-radius: 15px;
                    padding: 20px;
                }
                QLabel { color: black; }
                QLineEdit, QTextEdit, QComboBox {
                    background-color: #e0e0e0;
                    color: black;
                    border: 1px solid #c0c0c0;
                    border-radius: 5px;
                    padding: 5px;
                }
                QDialogButtonBox QPushButton {
                    background-color: #e0e0e0;
                    color: black;
                    border: 1px solid #c0c0c0;
                    border-radius: 5px;
                    padding: 5px;
                    min-width: 80px;
                }
                QDialogButtonBox QPushButton:hover {
                    background-color: #d0d0d0;
                }
            """)    
    def reject(self):
        """Сбрасывает video_path при отмене и закрывает диалог."""
        self.video_path = None  # Сбрасываем путь
        super().reject() # Вызываем родительский reject
        
if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dialog = AromaBlockSaveDialog()
    if dialog.exec() == AromaBlockSaveDialog.DialogCode.Accepted:
        name, description, data_type, content_link = dialog.get_aromablock_info()
        print("Данные аромаблока:", name, description, data_type, content_link)
    else:
        print("Диалог отменен")
    sys.exit(app.exec())