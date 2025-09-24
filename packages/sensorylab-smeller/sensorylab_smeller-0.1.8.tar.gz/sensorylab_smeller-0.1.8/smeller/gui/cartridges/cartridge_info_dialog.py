# Содержимое файла: smeller/gui/cartridge_info_dialog.py
import asyncio
import logging
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableView, QAbstractItemView, QHeaderView
from PyQt6.QtCore import Qt, QAbstractTableModel, pyqtSlot
from PyQt6.QtGui import QColor
from smeller.dynamic_control.view_model import MainWindowViewModel #  Импорт ViewModel

logger = logging.getLogger(__name__)

class CartridgeTableModel(QAbstractTableModel):
    """
    Модель таблицы для отображения списка картриджей.
    """
    def __init__(self, data: list):
        super().__init__()
        self._data = data
        self._headers = ["ID", "Name", "Code", "Class"] #  Заголовки столбцов

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            row = self._data[index.row()]
            if index.column() == 0:
                return str(row.ID)
            elif index.column() == 1:
                return row.NAME or ""
            elif index.column() == 2:
                return row.CODE or ""
            elif index.column() == 3:
                return row.CLASS or ""
        return None

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._headers)

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self._headers[section]
        return None

    def update_data(self, new_data):
        """
        Обновляет данные модели и вызывает оповещение об изменении данных.
        """
        self.beginResetModel()
        self._data = new_data
        self.endResetModel()

class CartridgeInfoDialog(QDialog):
    """
    Диалоговое окно для установки информации о картридже.
    """
    def __init__(self, channel_index: int, view_model: MainWindowViewModel, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Set Cartridge Info - Channel {channel_index + 1}")
        self.channel_index = channel_index
        self.view_model = view_model #  Сохраняем ссылку на ViewModel

        self.cartridge_id_edit = QLineEdit()
        self.cartridge_name_edit = QLineEdit()
        self.fetch_from_device_button = QPushButton("Fetch from Device")
        self.search_field = QLineEdit() #  Поле поиска
        self.cartridge_table_view = QTableView()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")

        self._init_ui()
        self._init_data() #  Загрузка данных о картриджах
        self._init_connections()

    def _init_ui(self):
        """
        Инициализирует пользовательский интерфейс диалогового окна.
        """
        layout = QVBoxLayout()

        # --- Форма ручного ввода ---
        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Manual Input:"))

        id_layout = QHBoxLayout()
        id_layout.addWidget(QLabel("Cartridge ID:"))
        id_layout.addWidget(self.cartridge_id_edit)
        form_layout.addLayout(id_layout)

        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("Cartridge Name (optional):"))
        name_layout.addWidget(self.cartridge_name_edit)
        form_layout.addLayout(name_layout)
        layout.addLayout(form_layout)

        # --- Кнопка "Fetch from Device" ---
        layout.addWidget(self.fetch_from_device_button)

        # --- Поле поиска ---
        layout.addWidget(QLabel("Search Cartridge:"))
        layout.addWidget(self.search_field)
        # --- Таблица картриджей ---
        layout.addWidget(QLabel("Available Cartridges:"))
        self.cartridge_table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows) # Выделение целой строки
        self.cartridge_table_view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection) # Одиночное выделение
        self.cartridge_table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) # Запрет редактирования
        self.cartridge_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # Растягивание колонок
        layout.addWidget(self.cartridge_table_view)

        # --- Кнопки OK/Cancel ---
        button_layout = QHBoxLayout()
        button_layout.addStretch(1) #  Растяжка для прижатия к правому краю
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)


    def _init_data(self):
        """
        Загружает данные о картриджах из базы данных и отображает в таблице.
        """
        cartridges = self.view_model.get_all_cartridges_from_db()
        if cartridges:
            self._all_cartridges_data = cartridges #  Сохраняем все данные
            model = CartridgeTableModel(self._all_cartridges_data)
            self.cartridge_table_view.setModel(model)
        else:
            #  Если нет данных из БД, можно показать пустую таблицу или сообщение
            model = CartridgeTableModel([])
            self.cartridge_table_view.setModel(model)
            logger.warning("No cartridges data loaded from database for CartridgeInfoDialog.")


    def _init_connections(self):
        """
        Инициализирует соединения сигналов и слотов.
        """
        self.ok_button.clicked.connect(self.accept) #  Принятие диалога и закрытие
        self.cancel_button.clicked.connect(self.reject) #  Отклонение диалога и закрытие
        self.fetch_from_device_button.clicked.connect(self._on_fetch_from_device_clicked)
        self.cartridge_table_view.doubleClicked.connect(self._on_table_double_clicked) #  Двойной клик по таблице
        self.search_field.textChanged.connect(self._filter_cartridge_table) #  Подключаем поиск
    
    def _on_fetch_from_device_clicked(self):
        """
        Синхронная обёртка для запуска асинхронной задачи.
        """
        asyncio.create_task(self._on_fetch_button_clicked_sync())
        
    @pyqtSlot()
    async def _on_fetch_button_clicked_sync(self):
        """
        Асинхронно запрашивает информацию о картридже и обновляет UI.
        """
        logger.info(f"_on_fetch_button_clicked_sync for channel {self.channel_index + 1} started") # <--- Лог старта
        try:
            logger.debug(f"Calling view_model.fetch_cartridge_info_from_device for channel {self.channel_index + 1}") # <--- Лог перед вызовом асинхронной функции
            cartridge_info = await self.view_model.fetch_cartridge_info_from_device(self.channel_index)
            logger.debug(f"Returned from view_model.fetch_cartridge_info_from_device for channel {self.channel_index + 1}") # <--- Лог после возврата
            if cartridge_info:
                cartridge_id = cartridge_info.get('cartridge_id')
                cartridge_name = cartridge_info.get('cartridge_name')
                print(f"Информация с устройства (канал {self.channel_index + 1}): ID={cartridge_id}, Name='{cartridge_name}'")
                # --- Обновление полей ввода ID и имени на основе полученных данных ---
                if cartridge_id:
                    self.cartridge_id_edit.setText(str(cartridge_id))
                if cartridge_name:
                    self.cartridge_name_edit.setText(cartridge_name)
            else:
                print(f"Не удалось получить информацию с устройства для канала {self.channel_index + 1}")
        except Exception as e:
            logger.error(f"Exception in _on_fetch_button_clicked_sync for channel {self.channel_index + 1}: {e}", exc_info=True) # <--- Лог ошибки
        finally:
            logger.info(f"_on_fetch_button_clicked_sync for channel {self.channel_index + 1} finished") # <--- Лог завершения
    def _on_table_double_clicked(self, index):
        """
        Обработчик двойного клика на строке таблицы.
        Заполняет поля ввода ID и Name значениями из выбранной строки.
        """
        model = self.cartridge_table_view.model()
        if model:
            cartridge_id = model.data(model.index(index.row(), 0), Qt.ItemDataRole.DisplayRole)
            cartridge_name = model.data(model.index(index.row(), 1), Qt.ItemDataRole.DisplayRole)
            self.cartridge_id_edit.setText(str(cartridge_id) if cartridge_id else "")
            self.cartridge_name_edit.setText(cartridge_name if cartridge_name else "")

    def get_cartridge_info(self):
        """
        Возвращает информацию о картридже, введенную пользователем или выбранную из таблицы.
        """
        cartridge_id = self.cartridge_id_edit.text()
        cartridge_name = self.cartridge_name_edit.text()
        return cartridge_id, cartridge_name
    def _filter_cartridge_table(self, text):
        """
        Фильтрует таблицу картриджей на основе введенного текста поиска.
        """
        filtered_cartridges = []
        if text:
            text_lower = text.lower()
            for cartridge in self._all_cartridges_data:
                # Явное преобразование cartridge.CODE и cartridge.CLASS в строку перед использованием lower()
                code_str = str(cartridge.CODE) if cartridge.CODE is not None else ""
                class_str = str(cartridge.CLASS) if cartridge.CLASS is not None else "" #  Преобразование CLASS в str
                if (str(cartridge.ID).lower().__contains__(text_lower) or
                        (cartridge.NAME and cartridge.NAME.lower().__contains__(text_lower)) or
                        (code_str.lower().__contains__(text_lower)) or # Используем code_str.lower()
                        (class_str.lower().__contains__(text_lower))): # Используем class_str.lower()
                    filtered_cartridges.append(cartridge)
        else:
            filtered_cartridges = self._all_cartridges_data

        model = CartridgeTableModel(filtered_cartridges)
        self.cartridge_table_view.setModel(model)