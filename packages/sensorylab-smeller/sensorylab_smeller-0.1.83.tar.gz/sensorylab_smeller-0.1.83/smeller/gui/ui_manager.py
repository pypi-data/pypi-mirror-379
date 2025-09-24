# main_window/ui_manager.py
import os, asyncio
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QAbstractButton, QDialog, QColorDialog, QGraphicsDropShadowEffect, QMessageBox
from PyQt6.QtCore import Qt, QTime
from PyQt6.QtGui import QColor
from smeller.gui.channels.channel_manager import ChannelManager
from smeller.gui.mediacenter.media_view import MediaView
from smeller.gui.waypoints.waypoint_plot_widget import WaypointPlotWidget
from smeller.gui.control_panel.control_panel import ControlPanel
from smeller.gui.aromablocks.aroma_block_list import AromablockList
from smeller.gui.menu_bar.menu_bar_manager import MenuBarManager

from smeller.models.aroma_block import AromaBlock
from smeller.gui.channels.channel_button import ChannelButton # Import ViewModel
from smeller.gui.cartridges.cartridge_info_dialog import CartridgeInfoDialog #  Импорт CartridgeInfoDialog
from smeller.gui.aromablocks.aroma_block_dialog import AromaBlockSaveDialog
from smeller.gui.theme_manager import ThemeManager #  Импорт CartridgeInfoDialog
from smeller.gui.devices.devices_connector_dialog import DeviceConnectionDialog #  Импорт DeviceConnectionDialog

from smeller.config.constants import *
import logging
logger = logging.getLogger(__name__)

class UIManager:
    """
    UIManager отвечает за сборку центрального виджета главного окна и организацию расположения основных компонентов приложения.
    """

    def __init__(self, parent, view_model):
        self.parent = parent
        self.view_model = view_model
        # Создаем центральный виджет и базовую вертикальную раскладку
        self.central_widget = QWidget(parent)
        self.global_layout = QVBoxLayout(self.central_widget)
        self.global_layout.setSpacing(0)
        self.global_layout.setContentsMargins(0, 0, 0, 0)
        
        self.media_layout = QHBoxLayout()
        self.media_layout.setSpacing(0)
        self.media_layout.setContentsMargins(25, 25, 25, 25)

        # Создаем заголовок для приложения
        self.title_label = QLabel("NeuroAir Control Panel", self.central_widget)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)  # AlignHCenter
        self.title_label.setStyleSheet("font-size: 20pt; font-weight: bold;")

        self.menu_bar_manager = MenuBarManager(parent)
        # Создаем компонент MediaView для отображения медиа-контента (например, видео)
        self.media_view = MediaView(parent)
        self.aromablocks_list = AromablockList(view_model=view_model, parent=parent)

        # Горизонтальная раскладка для основных частей интерфейса
        self.controllers_layout = QVBoxLayout()
        self.controllers_layout.setContentsMargins(25, 0, 25, 0)

        # Создаем компоненты интерфейса через соответствующие классы
        self.device_connection_dialog = None
        self.plot_widget_component = WaypointPlotWidget(view_model=view_model, parent=parent)
        self.channel_manager = ChannelManager(parent)
        
        self.control_panel = ControlPanel(parent)

        self.theme_manager = ThemeManager(self.parent, self.plot_widget_component.plot_widget)
        
        
    def get_central_widget(self):
        """
        Возвращает центральный виджет, который будет установлен в QMainWindow.
        """
        return self.central_widget

    def build_ui(self):
        """
        Собирает все компоненты интерфейса и располагает их в центральном виджете.
        """
        # Добавляем MediaView (например, область для видео или другого медиа-контента)
        self.media_layout.addWidget(self.media_view)
        self.media_layout.setSpacing(25)
        self.media_layout.addWidget(self.aromablocks_list, stretch=0) 
        self.aromablocks_list.setFixedWidth(250)
        self.channel_manager.setFixedWidth(250)


        # Размещаем панель управления под графиком (PlotWidgetComponent должен поддерживать такой метод)
        self.plot_widget_component.add_channel_manager(self.channel_manager)
        self.plot_widget_component.setFixedHeight(200)
        
        self.controllers_layout.addWidget(self.plot_widget_component, stretch=0, alignment=Qt.AlignmentFlag.AlignBottom) 
        self.controllers_layout.addWidget(self.control_panel) 

        # Устанавливаем меню через менеджер меню
        self.parent.setMenuBar(self.menu_bar_manager.get_menu_bar())
        self.global_layout.addWidget(self.title_label)
        self.global_layout.addLayout(self.media_layout)
        self.global_layout.addLayout(self.controllers_layout, stretch=0)
        self.theme_manager.apply_theme('dark')

    def set_initial_values(self):
        """
        Устанавливает начальные значения для компонентов интерфейса,
        например, выбирает интерполяцию по умолчанию и обновляет длительность таймлайна.
        """
        self.plot_widget_component.set_default_interpolation()
        #self.control_panel.update_total_duration(self.view_model.total_duration)
 
# ---------------------------------------
    def start_control(self):
        asyncio.create_task(self.view_model.start_control())
        self.media_view.play()

    def pause_control(self): # Новый метод для обработки сигнала паузы
        self.view_model.pause_control()
        self.media_view.pause()
        
    def stop_control(self):
        self.view_model.stop_control()
        self.media_view.stop()
    
    def set_volume(self, step):
        self.media_view.set_volume(step)
        
# -----------------------------------------------------
    def on_manual_seeked(self, seek_time: float):
        """
        Обработчик сигнала manual_seeked от TimelinePlayer.
        Передает информацию о перемотке в ViewModel.
        """
        self.media_view.set_position(int(seek_time * 1000))
        
    def on_manual_aroma(self, seek_time: float):
        """
        Обработчик сигнала manual_arome_seeked от TimelinePlayer.
        Передает информацию о перемотке в ViewModel.
        """
        self.view_model.handle_manual_seeked(seek_time)
        
    def on_manual_aroma_start(self):
        """
        Обработчик сигнала manual_seeked от TimelinePlayer.
        Передает информацию о перемотке в ViewModel.
        """
        self.view_model.handle_manual_seeked()
         
    def on_current_time_changed(self, current_time: float):
        """
        Слот для обновления маркера текущего времени на графике.
        """
        self.plot_widget_component.plot_widget.update_time_marker(current_time)
# ----------------------------------------------------------

    def update_total_duration(self, qtime: QTime | float):
        """Updates the total duration in the ViewModel.
        Handles both QTime and float inputs for duration.
        """
        if isinstance(qtime, QTime):
            duration_seconds = QTime(0, 0, 0).secsTo(qtime)
        elif isinstance(qtime, float):
            duration_seconds = int(qtime)  # Или можно оставить float, если ViewModel ожидает float
        else:
            logger.warning(f"Unexpected type for total duration: {type(qtime)}. Expected QTime or float.")
            return  # Прерываем выполнение, если тип неожиданный

        self.view_model.set_total_duration(duration_seconds)
        
# ---------------------------------------------------------------

    def switch_channel_from_button(self, button: QAbstractButton): #  Новый метод для обработки buttonClicked
        """Обработчик сигнала buttonClicked для QButtonGroup."""
        if isinstance(button, ChannelButton):
            self.switch_channel(button) #  Вызываем старый обработчик, передавая ChannelButton
        else:
            logger.warning("Clicked button is not a ChannelButton instance.")
            
    def switch_channel(self, button: ChannelButton): # Method now in MainWindow
        new_index = self.channel_manager.channel_buttons.id(button) # Access channel_buttons through ChannelManager
        self.view_model.switch_channel(new_index)
        for i, button_ in enumerate(self.channel_manager.channel_buttons.buttons()): # Access channel_buttons through ChannelManager
            if button_ == button:
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(5)
                shadow.setColor(self.channel_manager.neon_border_color) # Access neon_border_color through ChannelManager
                shadow.setOffset(0)
                button_.setGraphicsEffect(shadow)
            else:
                button_.setGraphicsEffect(None)   # Вот ключевое изменение!
                        
    def _set_cartridge_info(self, channel_index):
        """Opens dialog to set cartridge ID and name."""
        dialog = CartridgeInfoDialog(channel_index, self.view_model, self.parent) #  Передаем ViewModel
        result = dialog.exec() #  Запускаем диалог как модальный
        if result == QDialog.DialogCode.Accepted: #  Если нажата кнопка OK
            cartridge_id, cartridge_name = dialog.get_cartridge_info()
            self.view_model.set_channel_cartridge_info(channel_index, cartridge_id, cartridge_name)
            self.load_channel_config_from_viewmodel(channel_index) #  Обновление информации на кнопке
                            
    def _set_channel_color(self, channel_index):
        """Opens color dialog to set channel color."""
        current_config = self.view_model.channel_configs.get(channel_index)
        initial_color = current_config.color if current_config else QColor(Qt.GlobalColor.blue) # Default blue
        if isinstance(initial_color, dict):
                initial_color = QColor(initial_color['r'], initial_color['g'], initial_color['b'], initial_color['a'])
        color = QColorDialog.getColor(initial_color, self.parent, "Select Channel Color")
        if color.isValid():
            self.view_model.set_channel_color(channel_index, color)
            self.channel_manager.update_channel_button_color(channel_index, color) # <--- Добавляем вызов для обновления цвета кнопки
    
    def load_channel_config_from_viewmodel(self, channel_index: int):
            """
            Загружает конфигурацию управления для выбранного канала из модели представления (ViewModel).
            Обновляет текст кнопки (с информацией о картридже), устанавливает активный канал в WaypointPlotWidget,
            обновляет цвет линии, продолжительность и вейпоинты.
            
            Аргументы:
                channel_index (int): индекс канала (0-based).
            """
            if channel_index == -1:
                return
            config = self.view_model.channel_configs.get(channel_index)
            cartridge_text = f"{channel_index}"  # Текст по умолчанию
            # Если конфигурация существует – показать название/идентификатор картриджа
            if config:
                if config.cartridge_name:
                    cartridge_text = f"{channel_index}: {config.cartridge_name} ({config.cartridge_id})"
                elif config.cartridge_id:
                    cartridge_text = f"{channel_index}: ID {config.cartridge_id}"
                channel_color = config.color
            else:
                channel_color = self.plot_widget_component.plot_widget.default_colors[channel_index % len(self.plot_widget_component.plot_widget.default_colors)]
            if channel_index == -2:
                cartridge_text = "Вентилятор"
            elif 0 <= channel_index <= MAX_CHANNELS:
                cartridge_text = f"{channel_index + 1}"
            elif MAX_CHANNELS < channel_index:
                cartridge_text = str(channel_index)
                
            self.channel_manager.channel_button_widgets[channel_index].setText(cartridge_text)  # Обновляем текст кнопки
            self.channel_manager.current_channel_index = channel_index
            # В новом формате устанавливаем активный канал через метод set_active_channel
            
            if isinstance(channel_color, dict):
                    channel_color = QColor(channel_color['r'], channel_color['g'], channel_color['b'], channel_color['a'])
            self.plot_widget_component.plot_widget.set_active_channel(channel_index)
            self.plot_widget_component.plot_widget.set_channel_color(channel_index, channel_color) # Устанавливаем цвет линии графика
            self.plot_widget_component.plot_widget.set_total_duration(self.view_model.total_duration)
            # Передаём вейпоинты для конкретного канала; предполагается, что ViewModel обновлён для работы с мультиканальностью

            waypoints = self.view_model.get_waypoints(channel_index) if hasattr(self.view_model, "get_waypoints") else []

            self.plot_widget_component.plot_widget.set_waypoints(channel_index, waypoints)
            self.plot_widget_component.plot_widget.set_interpolation_type(config.interpolation_type)
            self.highlight_current_channel_button(channel_index)

    def highlight_current_channel_button(self, channel_index: int): # Method now in MainWindow
        """Вызывает метод ChannelManager для выделения кнопки текущего канала."""
        self.channel_manager.highlight_current_channel_button(channel_index)
        
# ---------------------------------------------------------------

    def on_waypoint_moved(self, channel_idx: int, waypoint_idx: int, new_time_percent: float, new_intensity: float):
        self.view_model.update_waypoint(channel_idx, waypoint_idx, new_time_percent, new_intensity)

    def on_waypoint_added(self, channel_idx: int, time_percent: float, intensity: float):
        self.view_model.add_waypoint(channel_idx, time_percent, intensity)

    def on_waypoint_deleted(self, channel_idx: int, waypoint_idx: int):
        self.view_model.delete_waypoint(channel_idx, waypoint_idx)
        
# ---------------------------------------------------------------
    def set_interpolation_button_from_viewmodel(self, interp_type: str): # Method now in MainWindow, calls component method
        """Sets the interpolation button in the WaypointPlotWidget from ViewModel."""
        self.plot_widget_component.set_interpolation_button_from_viewmodel(interp_type)

    def set_total_duration_from_viewmodel(self, duration: float):
        time = QTime(0, 0, 0).addSecs(int(duration))
        self.control_panel.total_duration_timeedit.setTime(time)
        self.plot_widget_component.plot_widget.set_total_duration(duration)
        self.control_panel.timeline_player.set_total_duration(duration)
        
    def update_plot_widget_from_viewmodel(self, channel_index: int):
        if channel_index == self.channel_manager.current_channel_index:
            waypoints = self.view_model.get_waypoints(channel_index)
            self.plot_widget_component.plot_widget.set_waypoints(channel_index, waypoints)
            self.plot_widget_component.plot_widget.update_plot()

            channel_color = self.plot_widget_component.plot_widget.channel_colors.get(channel_index)
            if waypoints: # Если есть вейпоинты, устанавливаем цвет кнопки в цвет графика
                self.channel_manager.update_channel_button_color(channel_index, channel_color)
            else:      # Иначе, сбрасываем цвет кнопки (None - для сброса)
                self.channel_manager.update_channel_button_color(channel_index, None) 
                                   
    def on_control_started_viewmodel(self):
        self.update_button_states(True)

    def on_control_stopped_viewmodel(self):
        self.update_button_states(False)
        
    def update_button_states(self, is_running: bool):
        for btn in self.channel_manager.channel_buttons.buttons():
            btn.setEnabled(not is_running)
        self.control_panel.total_duration_timeedit.setEnabled(not is_running)
        
    def show_error_message(self, message: str):
        QMessageBox.critical(self, "Error", message)

    def update_device_connection_status(self, is_connected: bool):
        status_message = "Device Connected" if is_connected else "Device Disconnected"
        logger.info(status_message) if is_connected else logger.warning(status_message)
        self.title_label.setWindowTitle(f"NeuroAir Control Panel - {status_message}")
        
    def update_aromablocks_table_view(self, aromablocks_list: list):
        current_id = self.view_model._current_aromablock_id
        self.aromablocks_list.update_table_view(aromablocks_list, current_id) 
           
    def on_aromablock_saved_viewmodel(self, block_id: int):
        """Обработчик сигнала aromablock_saved от ViewModel."""
        if block_id:
            logger.info(f"AromaBlock saved successfully with ID: {block_id}. Updating aromablocks list.")
            self.view_model.get_all_aromablocks_from_db() #  Обновляем список в GUI
        else:
            error_msg = "Не удалось сохранить AromaBlock. Проверьте логи для деталей." #  Изменен текст сообщения
            logger.error(error_msg)
            QMessageBox.critical(self, "Ошибка сохранения аромаблока", error_msg) #  Изменен текст сообщения
        self.update_menu_actions_state()
        
    def on_aromablock_loaded_viewmodel(self, loaded_aromablock: AromaBlock):
        """
        Обработчик сигнала aromablock_loaded от ViewModel.
        Применяет конфигурацию загруженного аромаблока и обновляет UI.
        """
        logger.info(f"AromaBlock '{loaded_aromablock.name}' loaded in MainWindow, applying configuration...")
        self.title_label.setText(loaded_aromablock.name)
        self.update_menu_actions_state()   
         
    def update_menu_actions_state(self):
        """Обновляет состояние пунктов меню в зависимости от состояния приложения."""
        is_aromablock_loaded = self.view_model.aromablock_loaded_instance is not None
        self.menu_bar_manager.save_action.setEnabled(is_aromablock_loaded) #  "Сохранить" активно только при загруженном аромаблоке
        self.menu_bar_manager.save_aromablock_action.setEnabled(is_aromablock_loaded) #  "Сохранить" активно только при загруженном аромаблоке
    
    def open_device_connection_dialog(self):
        """Открывает диалог настроек подключения устройства."""
        if not self.device_connection_dialog: #  Создаем только если не существует
            self.device_connection_dialog = DeviceConnectionDialog(self.parent, view_model=self.view_model)
        self.device_connection_dialog.show() #  Используем show, чтобы можно было несколько раз открывать и закрывать диалог

# ---------------------------------------------------------------
    def refresh_aromablocks_list(self):
        """Обновляет список аромаблоков, запрашивая данные из ViewModel."""
        self.view_model.get_all_aromablocks_from_db()

    def save_selected_aromablock(self):
        """
        Сохраняет изменения в текущем загруженном аромаблоке.
        Если аромаблок не загружен, предлагает использовать "Сохранить как...".
        """
        loaded_aromablock = self.view_model.aromablock_loaded_instance #  Получаем экземпляр загруженного аромаблока из ViewModel

        if loaded_aromablock and loaded_aromablock.id is not None: #  Проверяем, загружен ли аромаблок и есть ли у него ID (существует ли в БД)
            logger.info(f"Saving changes to existing AromaBlock '{loaded_aromablock.name}' (ID: {loaded_aromablock.id})...")

            #  Получаем текущие конфигурации каналов из ViewModel
            current_channel_configs = self.view_model.channel_configs

            #  Обновляем loaded_aromablock новыми конфигурациями.
            loaded_aromablock.channel_configurations = current_channel_configs
            loaded_aromablock.start_time = self.view_model.start_time
            loaded_aromablock.stop_time = self.view_model.total_duration
            #  Сохраняем обновленный аромаблок через AromaBlockModelController, используя новый метод update_aromablock_in_db
            success = self.view_model.aromablock_controller.update_aromablock_in_db(loaded_aromablock) #  <-- Вызываем update_aromablock_in_db
            if success:
                logger.info(f"AromaBlock '{loaded_aromablock.name}' (ID: {loaded_aromablock.id}) updated successfully.")
                QMessageBox.information(self, "Аромаблок сохранен", f"Изменения в аромаблоке '{loaded_aromablock.name}' успешно сохранены.")
                
            else:
                error_msg = f"Не удалось обновить AromaBlock '{loaded_aromablock.name}'. Проверьте логи для деталей."
                logger.error(error_msg)
                QMessageBox.critical(self, "Ошибка сохранения аромаблока", error_msg)
        else:
            logger.warning("No AromaBlock loaded to save. Prompting user to 'Save AromaBlock As...'")
            QMessageBox.information(
                self,
                "Сохранение аромаблока",
                "Нет загруженного аромаблока для сохранения изменений.\nИспользуйте 'Файл' -> 'Сохранить Аромаблок как...' для сохранения текущей конфигурации как нового аромаблока."
            )
                        
    def load_selected_aromablock_from_table(self, index):
        """Загружает выбранный аромаблок из QTableView."""
        if index.isValid():
            row = index.row()
            aromablock_id = self.aromablocks_list.table_model.get_aromablock_id(row) #  Получаем ID из модели
            if aromablock_id is not None:
                logger.debug(f"Loading aromablock ID: {aromablock_id} from table.")
                self.view_model.load_aromablock_from_db(aromablock_id)
                self.aromablocks_list.table_model.set_active_aromablock_id(aromablock_id) # <----  ДОБАВЬ ЭТУ СТРОКУ: Установка активного ID
            else:
                logger.warning("Aromablock ID is None, cannot load.")
            self.channel_manager.fan_button.click()
            

# ---------------------------------------------------------------

    def open_create_aromablock_dialog(self):
        """Открывает диалоговое окно для создания нового аромаблока."""
        self.view_model.reset_channel_configurations()
        dialog = AromaBlockSaveDialog(theme_name=self.plot_widget_component.plot_widget.theme) #  Создаем диалог сохранения
        if dialog.exec() == QDialog.DialogCode.Accepted: #  Если нажата кнопка "Сохранить" в диалоге
            aromablock_info = dialog.get_aromablock_info() # Получаем результат get_aromablock_info
            if aromablock_info: # Проверяем, что aromablock_info не None (имя введено)
                name, description, data_type, content_link, media_path = aromablock_info 
                if media_path:  # Если путь к видео есть
                    if os.path.isfile(media_path): # Проверяем, существует ли файл по указанному пути
                        self.media_view.load_media(media_path)  # Загружаем видео в MediaView
                        # Автоматическая установка длительности таймлайна:
                        duration = self.media_view.get_media_duration()
                        if duration > 0:
                            self.control_panel.timeline_player.set_total_duration(duration / 1000.0)
                            self.plot_widget_component.plot_widget.set_total_duration(duration / 1000.0)
                    else:
                        QMessageBox.warning(self, "Предупреждение", f"Видеофайл не найден по пути: {media_path}")
                        duration = 0
                        
                    result_id = self.view_model.save_current_config_as_aromablock(
                        name, description, data_type, content_link, start_time=0.0, stop_time=duration / 1000.0
                    )
                    if result_id:
                        self.aromablocks_list.table_model.set_active_aromablock_id(result_id)
                        self.update_menu_actions_state()
                        self.title_label.setText(name)
                        QMessageBox.information(
                            self,
                            "Аромаблок создан",
                            f"Новый аромаблок '{name}' успешно создан с ID: {result_id}."
                        )
                                
                result_id = self.view_model.save_current_config_as_aromablock(
                    name, description, data_type, content_link, start_time=0.0, stop_time=10.0
                )
                if result_id:
                    self.aromablocks_list.table_model.set_active_aromablock_id(result_id) # <----  ДОБАВЬ ЭТУ СТРОКУ: Установка активного ID
                    self.update_menu_actions_state()
                    self.title_label.setText(name)
                    # QMessageBox.information(
                    #     self,
                    #     "Аромаблок создан",
                    #     f"Новый аромаблок '{name}' успешно создан с ID: {result_id}."
                    # )
                    self.channel_manager.fan_button.click()
                    

    def undo_last_action(self): # <-- Undo slot in MainWindow
        """Undo the last action."""
        self.view_model.undo_last_action()

    def set_theme_dark(self): 
        self.theme_manager.apply_theme("Dark")
    def set_theme_white(self):
        self.theme_manager.apply_theme("Light")
         
# ---------------------------------------------------------------
         
    def update_total_duration(self, qtime: QTime | float):
        """Updates the total duration in the ViewModel.
        Handles both QTime and float inputs for duration.
        """
        self.view_model.set_total_duration(qtime)