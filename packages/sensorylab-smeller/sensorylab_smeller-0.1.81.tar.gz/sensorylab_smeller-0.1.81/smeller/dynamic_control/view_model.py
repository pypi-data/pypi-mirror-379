# smeller/dynamic_control/view_model.py
import asyncio
from PyQt6.QtCore import pyqtSignal, QObject, pyqtProperty, Qt, QTime
from PyQt6.QtGui import QColor
from typing import Dict, List, Tuple, Optional, Any
from smeller.communication.factory import create_communication
from smeller.dynamic_control.dynamic_block_controller import DynamicBlockController
from smeller.controllers.device_controller import DeviceController, Event
from smeller.models.aroma_block import AromaBlock
from smeller.models.channel_control_config import ChannelControlConfig
from smeller.database.db_manager import DatabaseManager  #  Импорт DatabaseManager
from smeller.controllers.cartridge_manager import CartridgeManager #  Импорт CartridgeManager
from smeller.controllers.aromablock_model_controller import AromaBlockModelController
from smeller.config.config import AppConfig 

from smeller.communication.bluetooth_com import DeviceInfo as BtDeviceInfo
from smeller.utils.comport_manager import ListPortInfo
from smeller.communication.multi_device_manager import MultiDeviceManager, DeviceId, DeviceStatus # Добавляем импорты
from smeller.config.constants import *
import logging

logger = logging.getLogger(__name__)

class MainWindowViewModel(QObject):
    """
    ViewModel for the MainWindow, managing the overall application state,
    interaction with the backend (Model), and providing data for the View.
    """
    control_started = pyqtSignal()
    """Signal emitted when dynamic control is started."""
    control_stopped = pyqtSignal()
    """Signal emitted when dynamic control is stopped."""
    manual_seeked_signal = pyqtSignal(float)
    
    channel_switched = pyqtSignal(int)
    """Signal emitted when the selected channel is switched.
    Args:
        channel_index (int): The index of the newly selected channel (0-based).
    """
    interpolation_type_changed = pyqtSignal(str) # Changed to str to match InterpolationType
    """Signal emitted when the interpolation type is changed.
    Args:
        interp_type (str): The new interpolation type (from InterpolationType enum).
    """
    total_duration_changed = pyqtSignal(float)
    """Signal emitted when the total duration is changed.
    Args:
        duration (float): The new total duration in seconds.
    """
    start_time_changed = pyqtSignal(float)
    """Signal emitted when the start_time is changed.
    Args:
        start_time_changed (float): The new start time in seconds.
    """
    waypoint_updated = pyqtSignal(int)
    """Signal emitted when waypoints for a channel are updated.
    Args:
        channel_index (int): The index of the channel (0-based).
    """
    control_error = pyqtSignal(str)
    """Signal emitted when an error occurs during control operations.
    Args:
        message (str): The error message to display.
    """
    device_connected_changed = pyqtSignal(bool)
    """Signal emitted when the device connection status changes."""

    aromablocks_list_updated = pyqtSignal(list)
    aromablock_loaded = pyqtSignal(AromaBlock)
    aromablock_saved = pyqtSignal(int)

    device_status_updated = pyqtSignal(str, str, str) # Добавляем сигнал: device_id, status, error_message (None если нет ошибки)
    device_list_changed = pyqtSignal(dict) # Сигнал об изменении списка устройств и их статусов


    def __init__(self, devices_manager: MultiDeviceManager, dynamic_controller: DynamicBlockController, config: AppConfig):
        """
        Initializes the MainWindowViewModel.

        Args:
            device_controller (DeviceController): The DeviceController instance (Model).
            dynamic_controller (DynamicBlockController): The DynamicBlockController instance (Model).
        """
        super().__init__()
        self.devices_manager: MultiDeviceManager = devices_manager
        """Reference to the DeviceController (Model)."""
        self.dynamic_controller: DynamicBlockController = dynamic_controller
        """Reference to the DynamicBlockController (Model)."""
        self.config: AppConfig = config
        logger.debug(f"MainWindowViewModel.__init__: self.dynamic_controller after assignment = {self.dynamic_controller}") # <--- PRINT STATEMENT

        self.db_manager = DatabaseManager(config.database) #  Создаем DatabaseManager
        try:
            self.db_manager.create_engine() #  Пытаемся создать engine и проверить подключение сразу
        except Exception as e:
            logger.error(f"Failed to initialize database connection: {e}")
            self.db_manager = None #  Отключаем, если не удалось подключиться
        
        self.aromablock_controller = AromaBlockModelController(self.db_manager)
        self.cartridge_manager = CartridgeManager(self.db_manager) #  Создаем CartridgeManager
        
        self._seek_time_offset: float = 0.0 # Добавляем переменную для хранения времени перемотки, инициализируем нулем
        self._start_time: float = 0.0
        self._total_duration: float = 0.0
        """Current total duration for dynamic control in seconds."""
        self._current_channel_index: int = 0
        """Currently selected channel index (0-based)."""
        self._is_control_running: bool = False
        """Flag indicating if dynamic control is currently running."""
        self._current_interpolation_type: str = LINEAR # Default to Linear
        """Currently selected interpolation type."""
        self.channel_configs: Dict[int, ChannelControlConfig] = {}
        """Dictionary to store ChannelControlConfig for each channel (key is channel index)."""
        self._is_device_connected: bool = False
        """Flag indicating if the device is currently connected."""
        self.aromablock_loaded_instance: Optional[AromaBlock] = None
        self._current_aromablock_id: Optional[int] = None
        
        self._undo_history: List[Dict[str, Any]] = []

        # --- НОВОЕ: Состояние для выбранного устройства ---
        self._selected_device_id: Optional[DeviceId] = None
        # <<<------

        # --- НОВОЕ: Хранение конфигураций каналов для КАЖДОГО устройства ---
        # Ключ - DeviceId, Значение - Dict[int, ChannelControlConfig]
        self.device_channel_configs: Dict[DeviceId, Dict[int, ChannelControlConfig]] = {}
        # Текущая конфигурация (ссылка на конфиг выбранного устройства)
        self.channel_configs: Dict[int, ChannelControlConfig] = {}
        
        self.load_channel_config(self._current_channel_index) # Load initial channel config

        # Connect to device connection events from DeviceController to update status in ViewModel
        self.devices_manager.event_handler.subscribe("device_connected", self._on_device_connected)
        self.devices_manager.event_handler.subscribe("device_disconnected", self._on_device_disconnected)
        self.devices_manager.event_handler.subscribe("device_connection_failed", self._on_device_connection_failed)
        self.devices_manager.event_handler.subscribe("device_status_changed", self._on_device_status_changed) # Общее событие статуса
        # <<<------
        
        self.aromablock_controller.aromablocks_list_updated.connect(self.aromablocks_list_updated)
        self.aromablock_controller.aromablock_loaded.connect(self.aromablock_loaded)
        self.aromablock_controller.aromablock_saved.connect(self.aromablock_saved)
        self.aromablock_controller.control_error.connect(self.control_error)
    
    async def _on_device_status_changed(self, event: Event):
        """Обрабатывает события изменения статуса от MultiDeviceManager."""
        data = event.data
        identifier = data.get("identifier")
        status = data.get("status")
        error = data.get("error")

        if identifier:
            logger.info(f"Device status changed event received: {identifier} -> {status} (Error: {error})")
            # Обновляем внутреннее состояние (если нужно)
            # ...

            # Эмитируем сигнал для GUI
            self.device_status_updated.emit(identifier, status, error or "")
            # Обновляем общий список статусов
            self._emit_device_list_update()
        # <<<------

    # --- Вспомогательный метод для обновления списка устройств в GUI ---
    def _emit_device_list_update(self):
        """Отправляет сигнал с текущим списком устройств и их статусами."""
        statuses = self.devices_manager.get_connection_statuses()
        self.device_list_changed.emit(statuses)
        
    
    '''async def connection_to_device(self, com_port=None, mac_address=None, connection_type='serial', chip_id=None, mqtt_config=None): #  Добавили chip_id и mqtt_config
        """
        Асинхронно устанавливает соединение с устройством и ждет завершения.
        """
        logger.info(f"Starting connection to device on port: {com_port}, mac_address: {mac_address}, type: {connection_type}, chip_id: {chip_id}")

        #  Динамическое создание communication object на основе типа соединения
        conn = create_communication(self.config, connection_type)
        self.device_controller.communication = conn #  Обновляем communication в device_controller

        connected = False #  Изначально устанавливаем в False

        if connection_type == "serial":
            connected = await self.device_controller.connect(com_port=com_port)
        elif connection_type == "bluetooth":
            connected = await self.device_controller.connect(mac_address=mac_address)
        elif connection_type == "mqtt": #  Обработка MQTT соединения
            if chip_id and mqtt_config: #  Проверяем наличие chip_id и mqtt_config
                connected = await self.device_controller.connect(chip_id=chip_id, mqtt_config=mqtt_config) #  Передаем chip_id и mqtt_config
            else:
                logger.error("Chip ID and MQTT config are required for MQTT connection.")
                self.control_error.emit("Chip ID and MQTT config are required for MQTT connection.")
                return False
        else:
            logger.error(f"Unknown connection type: {connection_type}")
            self.control_error.emit(f"Unknown connection type: {connection_type}")
            return False

        if connected:
            logger.info(f"Successfully connected to device via {connection_type}") #  Общее сообщение об успехе
        else:
            logger.error(f"Failed to connect to device via {connection_type}")
            self.control_error.emit(f"Failed to connect to device via {connection_type}.")
        return connected'''
            
    # --- Device Connection Status Property ---
    @pyqtProperty(bool, notify=device_connected_changed)
    def is_device_connected(self) -> bool:
        """
        Returns the device connection status.
        Returns:
            bool: True if device is connected, False otherwise.
        """
        return self._is_device_connected

    def _set_device_connected(self, connected: bool):
        """Internal method to update device connection status and emit signal."""
        if self._is_device_connected != connected:
            self._is_device_connected = connected
            self.device_connected_changed.emit(connected)

    async def _on_device_connected(self, event):  # <--- Changed to async def
        """Handler for 'device_connected' event."""
        logger.info("Device connected event received in ViewModel.")
        self._set_device_connected(True)

    async def _on_device_disconnected(self, event): # <--- Changed to async def
        """Handler for 'device_disconnected' event."""
        logger.info("Device disconnected event received in ViewModel.")
        self._set_device_connected(False)

    async def _on_device_connection_failed(self, event): # <--- Changed to async def
        """Handler for 'device_connection_failed' event."""
        logger.error("Device connection failed event received in ViewModel.")
        self._set_device_connected(False)
        self.control_error.emit("Failed to connect to device.")


    # --- Total Duration Property ---
    @pyqtProperty(float, notify=start_time_changed)
    def start_time(self) -> float:
        """
        Returns the total duration for dynamic control.
        Returns:
            float: Total duration in seconds.
        """
        return self._start_time
    
    # --- Total Duration Property ---
    @pyqtProperty(float, notify=total_duration_changed)
    def total_duration(self) -> float:
        """
        Returns the total duration for dynamic control.
        Returns:
            float: Total duration in seconds.
        """
        return self._total_duration

    def set_total_duration(self, duration: float | QTime):
        """
        Sets the total duration for dynamic control and emits the total_duration_changed signal.
        Args:
            duration (float): The new total duration in seconds.
        """
        
        if isinstance(duration, QTime):
            duration_seconds = QTime(0, 0, 0).secsTo(duration)
        elif isinstance(duration, float):
            duration_seconds = int(duration)  # Или можно оставить float, если ViewModel ожидает float
        else:
            logger.warning(f"Unexpected type for total duration: {type(duration)}. Expected QTime or float.")
            return  # Прерываем выполнение, если тип неожиданный

        if duration_seconds > 0:
            self._total_duration = duration_seconds
            self.total_duration_changed.emit(duration_seconds)
            self.save_channel_config(self._current_channel_index) # Save config when duration changes
        else:
            logger.warning("Total duration must be greater than zero.")
            self.control_error.emit("Total duration must be greater than zero.")

    # --- Current Channel Index Property ---
    @pyqtProperty(int, notify=channel_switched)
    def current_channel_index(self) -> int:
        """
        Returns the currently selected channel index.
        Returns:
            int: Current channel index (0-based).
        """
        return self._current_channel_index

    # --- Is Control Running Property ---
    @pyqtProperty(bool, notify=control_started, fset=None) # fset=None to make it read-only from outside
    def is_control_running(self) -> bool:
        """
        Returns the control running status.
        Returns:
            bool: True if control is running, False otherwise.
        """
        return self._is_control_running


    # --- Current Interpolation Type Property ---
    @pyqtProperty(str, notify=interpolation_type_changed) # Changed to str
    def current_interpolation_type(self) -> str: # Changed return type to str
        """
        Returns the current interpolation type.
        Returns:
            str: Current interpolation type (from InterpolationType enum).
        """
        return self._current_interpolation_type

    def set_current_interpolation_type(self, interp_type: str): # Changed param type to str
        """
        Sets the current interpolation type and emits the interpolation_type_changed signal.
        Args:
            interp_type (str): The new interpolation type (from InterpolationType enum).
        """
        
        if interp_type in [LINEAR, EXPONENTIAL, SINUSOIDAL, STEP]:
            self._current_interpolation_type = interp_type
            self.interpolation_type_changed.emit(interp_type)
            self.save_channel_config(self._current_channel_index) # Save config when interpolation type changes
        else:
            logger.warning(f"Invalid interpolation type: {interp_type}")
            self.control_error.emit(f"Invalid interpolation type: {interp_type}")


    # --- Waypoints Management ---
    def get_waypoints(self, channel_index: int = None) -> List[Tuple[float, float]]:
            if channel_index is None:
                channel_index = self._current_channel_index
            if channel_index in self.channel_configs:
                return self.channel_configs[channel_index].waypoints
            return []

    def set_waypoints(self, waypoints: List[Tuple[float, float]]):
        """
        Sets the waypoints for the currently selected channel, updates the config, and emits waypoint_updated signal.
        Args:
            waypoints (List[Tuple[float, float]]): List of waypoints as (time_percent, intensity_percent) tuples.
        """
        config = self.channel_configs.get(self._current_channel_index)
        if config:
            config.waypoints = waypoints
        else:
            config = ChannelControlConfig(
                channel_id=self._current_channel_index , # Channel ID is 1-based
                cycle_time=self.config.dynamic_control.default_cycle_time, # Default cycle time
                waypoints=waypoints,
                interpolation_type=self._current_interpolation_type
            )
            self.channel_configs[self._current_channel_index] = config
        self.waypoint_updated.emit(self._current_channel_index)
        self.save_channel_config(self._current_channel_index) # Save config when waypoints are set


    # --- Control Commands ---
    async def start_control(self):
        """
        Starts the dynamic control process.
        Validates configurations, then starts the DynamicBlockController,
        and emits the control_started signal upon successful start.
        Handles potential ValueErrors from configuration validation.
        """
        logger.debug(f"MainWindowViewModel.start_control: self.dynamic_controller = {self.dynamic_controller}") # <--- ADD THIS PRINT STATEMENT
        if self._is_control_running:
            logger.warning("Control is already running.")
            return

        configs_for_start: Dict[str, List[ChannelControlConfig]] = {}
        for index in range(-2, MAX_CHANNELS): # MAX_CHANNELS
            if index in self.channel_configs:
                # Use cartridge_id as string key, based on channel index (assuming 1-to-1 mapping for now)
                cartridge_id = index # Or define cartridge IDs more explicitly if needed
                configs_for_start[cartridge_id] = [self.channel_configs[index]] # List of configs for each cartridge

        try:
            total_duration = self._total_duration
            if self.dynamic_controller is None: # Проверка на NoneType
                logger.error("dynamic_controller is None! Cannot start control.")
                self.control_error.emit("Dynamic controller is not initialized.")
                return  # Выходим из метода, чтобы предотвратить ошибку
            logger.debug(self.dynamic_controller)
            
            start_time_offset = self._seek_time_offset
            self.dynamic_controller.start(configs_for_start, total_duration, start_time_offset)
            self._seek_time_offset = 0.0
            self._is_control_running = True
            self.control_started.emit()
            logger.info("Dynamic control started successfully.")
        except ValueError as e:
            logger.error(f"Error starting control: {e}")
            self.control_error.emit(str(e))
        except Exception as e:
            logger.exception("Unexpected error during start_control:")
            self.control_error.emit(f"Unexpected error during start: {e}")

    def pause_control(self):
        """
        Pauses the dynamic control process.
        Pauses the DynamicBlockController and updates the control status.
        """
        if not self._is_control_running:
            logger.warning("Control is not running, cannot pause.")
            return
        
        self.dynamic_controller.pause() # Call pause method in DynamicBlockController
        self._is_control_running = False # Set control status to paused (or adjust as needed)
        logger.info("Dynamic control paused by user.")
        self.control_stopped.emit() # Можно использовать сигнал 'control_stopped' для паузы тоже, или добавить 'control_paused' сигнал, если нужно различать состояния

    def stop_control(self):
        """
        Stops the dynamic control process.
        Stops the DynamicBlockController and emits the control_stopped signal.
        """
        if not self._is_control_running:
            logger.warning("Control is not running.")
            return
        self.dynamic_controller.stop()
        self._is_control_running = False
        self.control_stopped.emit()
        logger.info("Dynamic control stopped by user.")
        
    def handle_manual_seeked(self, seek_time: float):
        """
        Обрабатывает событие ручной перемотки таймлайна.
        Останавливает текущее управление и сохраняет время перемотки.
        """
        logger.info(f"Manual seeked to time: {seek_time} seconds.")
        self._seek_time_offset = seek_time # Сохраняем время перемотки
        if self._is_control_running:
            self.stop_control() # Останавливаем текущее управление при перемотке
        #self.manual_seeked_signal.emit(seek_time) # Опционально, можно испустить сигнал для GUI
        logger.debug(f"Seek time offset stored: {self._seek_time_offset}")
        if self._seek_time_offset < 0:
            self._seek_time_offset = 0 # Ensure seek time is not negative

    
    def switch_channel(self, channel_index: int):
        """
        Switches the currently selected channel.
        Saves the configuration of the current channel, loads the configuration for the new channel,
        and emits the channel_switched signal.
        Args:
            channel_index (int): The index of the channel to switch to (0-based).
        """
        if -2 <= channel_index < MAX_CHANNELS: # MAX_CHANNELS
            self.save_channel_config(self._current_channel_index) # Save current channel config
            self._current_channel_index = channel_index
            self.load_channel_config(self._current_channel_index) # Load new channel config
            self.channel_switched.emit(channel_index)
            logger.debug(f"Switched to channel index: {channel_index}") # Log 1-based channel number
        else:
            logger.warning(f"Invalid channel index: {channel_index}")
            self.control_error.emit(f"Invalid channel index: {channel_index}")

    def reset_channel_configurations(self):
        """
        Сбрасывает конфигурации каналов к значениям по умолчанию (пустые вейпоинты, линейная интерполяция).
        Используется при создании нового аромаблока.
        """
        self.channel_configs = {} # Очищаем словарь конфигураций
        for channel_index in range(-2, MAX_CHANNELS): # MAX_CHANNELS
            default_color = QColor(Qt.GlobalColor.blue)
            config = ChannelControlConfig(channel_id=channel_index, 
                                          cycle_time=self.config.dynamic_control.default_cycle_time, 
                                          waypoints=[], 
                                          interpolation_type=LINEAR, 
                                          cartridge_id="", 
                                          cartridge_name="", 
                                          color=default_color)
            self.channel_configs[channel_index] = config
            self.load_channel_config(channel_index) # Загружаем дефолтную конфигурацию для обновления UI
        logger.info("Channel configurations reset to default empty state.")


    def update_interpolation_type(self, interp_type_str: str): # Changed param type to str
        """
        Updates the interpolation type for the current channel.

        Args:
            interp_type_str (str): The new interpolation type (from InterpolationType enum).
        """
        self.set_current_interpolation_type(interp_type_str)
        logger.debug(f"Interpolation type updated to: {interp_type_str} for channel {self._current_channel_index }")


    # --- Configuration Management ---
    def load_channel_config(self, channel_index: int):
        """
        Loads the channel configuration for the given channel index.
        If a configuration exists, it loads waypoints and interpolation type.
        If not, it initializes with default values (Linear interpolation, no waypoints).
        Args:
            channel_index (int): The index of the channel to load configuration for (0-based).
        """
        if channel_index in self.channel_configs:
            config = self.channel_configs[channel_index]
            self._current_interpolation_type = config.interpolation_type # Restore interpolation type
            self.interpolation_type_changed.emit(config.interpolation_type) # Notify View about interpolation type
            logger.debug(f"Loaded config for channel index: {channel_index}")
        else:
            # Если конфигурации нет, создаем новую с пустыми вейпоинтами и линейной интерполяцией
            default_color = QColor(Qt.GlobalColor.blue)  # Или другой цвет по умолчанию
            config = ChannelControlConfig(
                channel_id=channel_index ,
                cycle_time=self.config.dynamic_control.default_cycle_time,
                waypoints=[],  # Пустой список вейпоинтов
                interpolation_type=LINEAR, # Линейная интерполяция
                cartridge_id="",
                cartridge_name="",
                color=default_color
            )
            self.channel_configs[channel_index] = config
            self._current_interpolation_type = LINEAR
            logger.debug(f"Initialized default config for channel index: {channel_index}")

        # ВАЖНО: Сообщаем виджету обновить вейпоинты *после* загрузки или инициализации конфига
        self.waypoint_updated.emit(channel_index)
        
    def save_channel_config(self, channel_index: int):
        """
        Saves the current channel configuration.
        """
        waypoints = self.get_waypoints() # Get current waypoints from ViewModel state
        config = self.channel_configs.get(channel_index)
        if config:
            config.waypoints = waypoints
            config.interpolation_type = self._current_interpolation_type
        else:
            config = ChannelControlConfig(
                channel_id=channel_index , # Channel ID is 1-based
                cycle_time=self.config.dynamic_control.default_cycle_time, # Default cycle time
                waypoints=waypoints,
                interpolation_type=self._current_interpolation_type,
                cartridge_id="", # Дефолтное значение, если нет конфига
                cartridge_name="", # Дефолтное значение, если нет конфига
                color=QColor(Qt.GlobalColor.blue) # Дефолтный цвет, если нет конфига
            )
            self.channel_configs[channel_index] = config
        logger.debug(f"Saved config for channel index: {channel_index }")

    def update_waypoint(self, channel_index: int, waypoint_index: int, new_time_percent: float, new_intensity: float):
        
        config = self.channel_configs.get(channel_index)
        logger.debug(f'Конфиги: {self.channel_configs}, {channel_index}, {waypoint_index}, {len(config.waypoints)}')
        if config and 0 <= waypoint_index < len(config.waypoints):
            old_waypoint = config.waypoints[waypoint_index] # <-- Get the old waypoint

            # Create undo action
            undo_action = {
                'action': 'update_waypoint',
                'channel_index': channel_index,
                'waypoint_index': waypoint_index,
                'old_time_percent': old_waypoint[0], # Save old time and intensity
                'old_intensity': old_waypoint[1]
            }
            self._undo_history.append(undo_action) # Add to undo history
            
            # Округляем время до ближайшего целого, деленного на 100 (т.е. до ближайших "сотен" процентов)
            rounded_time_percent = round(new_time_percent)

            # Проверяем, есть ли уже точка с таким временем
            existing_waypoint_index = None
            for i, (time_percent, _) in enumerate(config.waypoints):
                if round(time_percent) == rounded_time_percent and i != waypoint_index:
                    existing_waypoint_index = i
                    break

            if existing_waypoint_index is not None:
                # Обновляем существующую точку
                config.waypoints[existing_waypoint_index] = (rounded_time_percent, new_intensity)
                # Удаляем текущую точку, которую мы должны были обновить
                del config.waypoints[waypoint_index]
            else:
                # Обновляем точку как обычно
                config.waypoints[waypoint_index] = (rounded_time_percent, new_intensity)

            config.waypoints.sort(key=lambda wp: wp[0]) # Keep waypoints sorted by time
            self.waypoint_updated.emit(channel_index) # Notify plot to redraw
            self.save_channel_config(channel_index)
            logger.debug(f"Updated waypoint {waypoint_index} for channel {channel_index }")
        else:
            logger.warning(f"Invalid waypoint index or channel config not found for channel {channel_index }")
            self.control_error.emit(f"Invalid waypoint update request for channel {channel_index }")
            
    def add_waypoint(self, channel_idx: int, time_percent: float, intensity: float):
        """
        Adds a waypoint to the specified channel's configuration.
        Args:
            channel_idx (int): Channel index (0-based).
            time_percent (float): Time percentage for the waypoint.
            intensity (float): Intensity percentage for the waypoint.
        """
        logger.debug(f"Добавляем новую точку: {channel_idx}, {time_percent}, {intensity}")
        if channel_idx == self._current_channel_index: # Добавлена проверка текущего канала
            config = self.channel_configs.get(channel_idx)
            time_val = round(time_percent / 100 * self._total_duration) # Округляем

            if config:
                # Проверяем, есть ли уже вейпоинт с таким временем
                existing_waypoint_index = None
                for i, (existing_time_percent, _) in enumerate(config.waypoints):
                    if round(existing_time_percent / 100 * self._total_duration) == time_val:
                        existing_waypoint_index = i
                        break

                if existing_waypoint_index is not None:
                    # Обновляем существующий вейпоинт
                    config.waypoints[existing_waypoint_index] = (time_percent, intensity)
                else:
                    # Добавляем новый вейпоинт
                    config.waypoints.append((time_percent, intensity))

                config.waypoints.sort(key=lambda wp: wp[0])  # Сортируем
                self.waypoint_updated.emit(channel_idx)
                self.save_channel_config(channel_idx)  # Сохраняем
                logger.debug(f"Added waypoint at ({time_percent:.2f}%, {intensity:.2f}%) to channel {channel_idx }")
            else:
                # Создание нового конфига, если его нет
                logger.warning("Trying to add waypoint to a channel with no config.")
                self.control_error.emit(f"Cannot add waypoint to channel {channel_idx } (no config)")


    def delete_waypoint(self, channel_index: int, waypoint_index: int):
        """
        Deletes a waypoint from a channel's configuration.
        Args:
            channel_index (int): Channel index (0-based).
            waypoint_index (int): Index of the waypoint to delete.
        """
        config = self.channel_configs.get(channel_index)
        if config and 0 <= waypoint_index < len(config.waypoints):
            del config.waypoints[waypoint_index]
            self.waypoint_updated.emit(channel_index)
            self.save_channel_config(channel_index)
            logger.debug(f"Deleted waypoint {waypoint_index} for channel {channel_index }")
        else:
            logger.warning(f"DELETE: Invalid waypoint index or channel config not found for channel {channel_index }")
            self.control_error.emit(f"Invalid waypoint deletion request for channel {channel_index }")
            
    def set_channel_cartridge_info(self, channel_index: int, cartridge_id: str, cartridge_name: str):
        """
        Sets cartridge ID and name for a channel.
        Args:
            channel_index (int): Channel index (0-based).
            cartridge_id (str): Cartridge ID.
            cartridge_name (str): Cartridge name.
        """
        config = self.channel_configs.get(channel_index)
        if config:
            config.cartridge_id = cartridge_id
            config.cartridge_name = cartridge_name
        else:
            config = ChannelControlConfig(
                channel_id=channel_index ,
                cycle_time=self.config.dynamic_control.default_cycle_time,
                waypoints=[],
                interpolation_type=self._current_interpolation_type,
                cartridge_id=cartridge_id,
                cartridge_name=cartridge_name
            )
            self.channel_configs[channel_index] = config
        self.save_channel_config(channel_index) # Save immediately
        self.channel_switched.emit(channel_index) # Refresh channel button text

    def set_channel_color(self, channel_index: int, color: QColor):
        """
        Sets the color for a channel.
        Args:
            channel_index (int): Channel index (0-based).
            color (QColor): Color to set.
        """
        config = self.channel_configs.get(channel_index)
        if config:
            config.color = color
        else: # in case config is somehow not initialized yet
             config = ChannelControlConfig(
                channel_id=channel_index ,
                cycle_time=self.config.dynamic_control.default_cycle_time,
                waypoints=[],
                interpolation_type=self._current_interpolation_type,
                color=color # Set color even for new config
            )
             self.channel_configs[channel_index] = config
        self.save_channel_config(channel_index)
        self.channel_switched.emit(channel_index) # Refresh plot color
        logger.debug(f"Цвет для канала {channel_index } установлен в: {color.getRgb()}") # <--- ДОБАВЛЕН ЛОГ
        
        
    #база картриджей
    def get_all_cartridges_from_db(self):
        """
        Получает все картриджи через CartridgeManager.
        """
        return self.cartridge_manager.get_all_cartridges_from_db()

    async def fetch_cartridge_info_from_device(self, channel_index): #  <--- Функция стала асинхронной
        """
        Запрашивает информацию о картридже с устройства через CartridgeManager,
        передавая DeviceController.
        """
        return await self.cartridge_manager.discover_cartridge_info_from_device(channel_index, self.device_controller) #  <--- Передаем device_controller
    

    def get_all_aromablocks_from_db(self): #  Метод-прокси для вызова из GUI
        """Запрашивает список аромаблоков через AromaBlockModelController."""
        self.aromablock_controller.get_all_aromablocks_from_db()

    def load_aromablock_from_db(self, aromablock_id: int): #  Метод-прокси для вызова из GUI
        """Загружает AromaBlock по ID через AromaBlockModelController."""
        loaded_aromablock = self.aromablock_controller.load_aromablock_from_db(aromablock_id)
        if loaded_aromablock:
            self._current_aromablock_id = loaded_aromablock.id
            self.apply_aromablock_config(loaded_aromablock)
            
            return loaded_aromablock
        return None
    
    def save_current_config_as_aromablock(self, aromablock_name: str, 
                                          aromablock_description: str, 
                                          aromablock_data_type: str, 
                                          aromablock_content_link: str,
                                          start_time: float, stop_time: float,
                                          ): # Метод-прокси
        """Сохраняет текущую конфигурацию как AromaBlock через AromaBlockModelController."""
        return_value = self.aromablock_controller.save_current_config_as_aromablock(
            aromablock_name, aromablock_description, 
            aromablock_data_type, aromablock_content_link, 
            start_time, stop_time,
            self.channel_configs
        )
        if return_value:
            self.apply_aromablock_config(return_value)  # Apply config of the new AromaBlock
            return return_value.id  # Return ID for signal processing
        return None

    def delete_aromablock_from_db(self, aromablock_id: int): # Метод-прокси
        """Удаляет AromaBlock по ID через AromaBlockModelController."""
        self.aromablock_controller.delete_aromablock_from_db(aromablock_id)

    def copy_aromablock_from_db(self, aromablock_id: int): # Метод-прокси для вызова из GUI
        """Копирует AromaBlock по ID через AromaBlockModelController."""
        self.aromablock_controller.copy_aromablock_in_db(aromablock_id)
        
    def apply_aromablock_config(self, loaded_aromablock: AromaBlock): # Метод-прокси (возможно, стоит перенести логику применения конфига в AromaBlockModelController или оставить здесь, в зависимости от сложности)
        """Применяет конфигурацию загруженного AromaBlock, используя AromaBlockModelController."""
        logger.info(f"Applying configuration from AromaBlock '{loaded_aromablock.name}' to ViewModel...")
        
        #  Получаем конфигурации каналов от AromaBlockModelController
        self.total_duration_changed.emit(loaded_aromablock.stop_time)
        channel_configurations = self.aromablock_controller.apply_aromablock_config(loaded_aromablock)

        #  1. Применяем конфигурации каналов
        self.channel_configs = channel_configurations #  Заменяем текущие конфигурации на загруженные
        self._current_aromablock_id = loaded_aromablock.id
        #  2. Обновляем GUI, эмитируя сигналы (остается без изменений)
        for channel_index in range(-2, MAX_CHANNELS): # MAX_CHANNELS
            self.load_channel_config(channel_index) #  Перезагружаем конфигурацию для каждого канала, чтобы обновить UI
            self.channel_switched.emit(channel_index) #  Обновляем кнопки каналов (текст, цвет)
            self.waypoint_updated.emit(channel_index) #  Обновляем графики вейпоинтов
        logger.info(f"Configuration from AromaBlock '{loaded_aromablock.name}' applied successfully.")
        self.aromablock_loaded_instance = loaded_aromablock
        
    def undo_last_action(self): # <-- Add Undo method
        if self._undo_history:
            last_action = self._undo_history.pop()
            action_type = last_action['action']

            if action_type == 'update_waypoint':
                channel_index = last_action['channel_index']
                waypoint_index = last_action['waypoint_index']
                old_time_percent = last_action['old_time_percent']
                old_intensity = last_action['old_intensity']

                config = self.channel_configs.get(channel_index)
                if config and 0 <= waypoint_index < len(config.waypoints):
                    config.waypoints[waypoint_index] = (old_time_percent, old_intensity) # Restore old waypoint
                    config.waypoints.sort(key=lambda wp: wp[0]) # Keep sorted
                    self.waypoint_updated.emit(channel_index) # Update plot
                    self.save_channel_config(channel_index) # Save config
                    logger.debug(f"Undo: Waypoint {waypoint_index} for channel {channel_index } reverted.")
        else:
            logger.info("Undo history is empty.")
    
    def connect_signals(self, main_window):
        self.channel_switched.connect(main_window.load_channel_config_from_viewmodel)
        self.interpolation_type_changed.connect(main_window.set_interpolation_button_from_viewmodel)
        self.total_duration_changed.connect(main_window.set_total_duration_from_viewmodel)
        self.waypoint_updated.connect(main_window.update_plot_widget_from_viewmodel)
        self.control_started.connect(main_window.on_control_started_viewmodel)
        self.control_stopped.connect(main_window.on_control_stopped_viewmodel)
        self.control_error.connect(main_window.show_error_message)
        self.device_connected_changed.connect(main_window.update_device_connection_status)

        self.aromablocks_list_updated.connect(main_window.update_aromablocks_table_view) #  Сигнал для обновления таблицы
        self.aromablock_saved.connect(main_window.on_aromablock_saved_viewmodel)
        self.aromablock_loaded.connect(main_window.on_aromablock_loaded_viewmodel) #  Обработка загрузкиsignals(self, main_
        
        #self.device_status_updated.connect(main_window.update_device_status_display) # Подключаем к новому слоту в MainWindow
        #self.device_list_changed.connect(main_window.update_device_list_display) # Подключаем к новому слоту в MainWindow
        
        
    async def vm_connect_device(self, identifier: DeviceId):
        # Может добавить доп. логику ViewModel перед вызовом менеджера
        return await self.devices_manager.connect_device(identifier)

    async def vm_disconnect_device(self, identifier: DeviceId):
        await self.devices_manager.disconnect_device(identifier) # Или через request_disconnection

    async def vm_remove_device(self, identifier: DeviceId):
        await self.devices_manager.remove_target_device(identifier) # Или через request_remove_device

    def vm_get_connection_statuses(self) -> Dict[DeviceId, Tuple[DeviceStatus, Optional[str]]]:
        return self.devices_manager.get_connection_statuses()

    def vm_discover_serial_ports(self, refresh: bool = True) -> List[ListPortInfo]:
        return self.devices_manager.discover_serial_ports(refresh=refresh)

    async def vm_discover_bluetooth_devices(self, scan_duration: Optional[int] = None) -> List[BtDeviceInfo]:
        return await self.devices_manager.discover_bluetooth_devices(scan_duration=scan_duration)

    def vm_get_discovered_mqtt_devices(self) -> List[DeviceId]:
        return self.devices_manager.get_discovered_mqtt_devices()
    # --- Управление соединениями ---
    async def vm_connect_device(self, identifier: DeviceId):
        """Запрашивает подключение через MultiDeviceManager."""
        # Здесь можно добавить логику ViewModel, если нужно
        logger.debug(f"ViewModel: Proxying connect request for {identifier}")
        # Важно: connect_device менеджера сам обрабатывает регистрацию, если add_target_device был вызван ранее
        # Если connect_device вызывается для УЖЕ известного устройства (из таблицы)
        await self.devices_manager.connect_device(identifier)
        # Статус обновится через сигнал

    async def vm_disconnect_device(self, identifier: DeviceId):
        """Запрашивает отключение через MultiDeviceManager."""
        logger.debug(f"ViewModel: Proxying disconnect request for {identifier}")
        await self.devices_manager.disconnect_device(identifier)
        # Статус обновится через сигнал
        if self._selected_device_id == identifier:
             self.select_device(None) # Сбрасываем выбор, если отключили выбранное

    async def vm_remove_device(self, identifier: DeviceId):
        """Запрашивает удаление через MultiDeviceManager."""
        logger.debug(f"ViewModel: Proxying remove request for {identifier}")
        self.devices_manager.remove_target_device(identifier) # Этот метод сам вызывает disconnect
        if self._selected_device_id == identifier:
             self.select_device(None) # Сбрасываем выбор, если удалили выбранное
        # Список обновится через сигнал device_list_changed (нужно убедиться, что он эмитится из remove_target_device или обновить здесь)
        self._emit_device_list_update() # Принудительно обновляем список

    async def vm_add_and_connect_device(self, identifier: DeviceId, connection_type: str, config: Optional[Dict[str, Any]] = None):
        """Регистрирует и запрашивает подключение нового устройства."""
        logger.debug(f"ViewModel: Proxying add and connect request for {identifier}")
        # 1. Регистрируем (или обновляем конфиг)
        self.devices_manager.add_target_device(identifier, connection_type, config)
        # 2. Запускаем подключение
        await self.devices_manager.connect_device(identifier)
        # Статус и список обновятся через сигналы

    async def vm_disconnect_all_devices(self):
        """Запрашивает отключение всех устройств."""
        logger.debug("ViewModel: Proxying disconnect all request")
        await self.devices_manager.disconnect_all_connected()

    # --- Получение информации ---
    def vm_get_connection_statuses(self) -> Dict[DeviceId, Tuple[DeviceStatus, Optional[str]]]:
        """Возвращает статусы всех зарегистрированных устройств."""
        return self.devices_manager.get_connection_statuses()

    def vm_get_connection_info(self, identifier: DeviceId) -> Optional[Any]: # Возвращаемый тип зависит от ConnectionInfo
        """Возвращает информацию о конкретном устройстве."""
        return self.devices_manager.connections.get(identifier)

    # --- Обнаружение устройств ---
    def vm_discover_serial_ports(self, refresh: bool = True) -> List[ListPortInfo]:
        """Запускает обнаружение COM-портов."""
        return self.devices_manager.discover_serial_ports(refresh=refresh)

    async def vm_discover_bluetooth_devices(self, scan_duration: Optional[int] = None) -> List[BtDeviceInfo]:
        """Запускает обнаружение Bluetooth-устройств."""
        return await self.devices_manager.discover_bluetooth_devices(scan_duration=scan_duration)

    def vm_get_discovered_mqtt_devices(self) -> List[DeviceId]:
        """Запрашивает список обнаруженных MQTT Chip ID."""
        return self.devices_manager.get_discovered_mqtt_devices()

    # <<<------ КОНЕЦ ПРОКСИ-МЕТОДОВ <<<------

    # ------>>> ПРОКСИ-МЕТОДЫ для УПРАВЛЕНИЯ MQTT <<<------
    def vm_is_mqtt_client_running(self) -> bool:
        """Проверяет, запущен ли MQTT клиент."""
        return self.devices_manager.is_mqtt_client_running()

    async def vm_start_mqtt_client(self) -> bool:
        """Запрашивает запуск MQTT клиента."""
        logger.debug("ViewModel: Proxying start MQTT client request")
        result = await self.devices_manager.start_mqtt_client()
        # if self.mqtt_client_status_changed: # Если сигнал добавлен
        #     self.mqtt_client_status_changed.emit(result)
        return result

    async def vm_stop_mqtt_client(self) -> bool:
        """Запрашивает остановку MQTT клиента."""
        logger.debug("ViewModel: Proxying stop MQTT client request")
        result = await self.devices_manager.stop_mqtt_client()
        # if self.mqtt_client_status_changed: # Если сигнал добавлен
        #     self.mqtt_client_status_changed.emit(not result) # Статус false если остановка успешна
        return result
    # <<<------ КОНЕЦ ПРОКСИ-МЕТОДОВ MQTT <<<------












    # ... (остальные методы ViewModel: select_device, управление каналами, аромаблоками и т.д.) ...

    # Метод _emit_device_list_update должен вызываться после добавления/удаления
    def _emit_device_list_update(self):
        """Отправляет сигнал с текущим списком устройств и их статусами."""
        # Используем прокси-метод
        statuses = self.vm_get_connection_statuses()
        self.device_list_changed.emit(statuses)

    # Метод _on_device_status_changed остается без изменений, он уже вызывается из MultiDeviceManager
    async def _on_device_status_changed(self, event: Event):
        # ... (код без изменений) ...
        data = event.data
        identifier = data.get("identifier")
        status = data.get("status")
        error = data.get("error")
        if identifier:
            # logger.info(f"ViewModel received status update: {identifier} -> {status}") # Логирование уже есть ниже
            self.device_status_updated.emit(identifier, status, error or "")
            # Обновление общего списка может быть избыточным здесь, если обновляется только статус
            # self._emit_device_list_update() # Можно убрать, если device_list_changed вызывается только при добавлении/удалении
            
    # ------>>> МЕТОД ВЫБОРА АКТИВНОГО УСТРОЙСТВА <<<------
    def select_device(self, device_id: Optional[DeviceId]):
        """
        Выбирает активное устройство для управления конфигурацией каналов и запуска.

        Args:
            device_id: Идентификатор устройства или None для снятия выбора.
        """
        # Проверяем, действительно ли изменился выбор
        if self._selected_device_id == device_id:
            logger.debug(f"Device {device_id} is already selected.")
            return # Ничего не делаем, если устройство уже выбрано

        # --- Сохраняем конфигурацию предыдущего устройства ---
        # Проверяем, было ли выбрано предыдущее устройство
        if self._selected_device_id is not None:
            logger.debug(f"Saving configuration for previously selected device: {self._selected_device_id}")
            # Вызываем save_channel_config для текущего активного канала перед сменой устройства
            self.save_channel_config(self._current_channel_index)
            # Копируем весь текущий словарь self.channel_configs в хранилище для старого device_id
            if self._selected_device_id in self.device_channel_configs:
                 self.device_channel_configs[self._selected_device_id] = self.channel_configs.copy()
            else:
                 # Если конфига для старого ID еще не было, создаем его
                 logger.warning(f"Config dictionary for device {self._selected_device_id} not found during save. Creating.")
                 self.device_channel_configs[self._selected_device_id] = self.channel_configs.copy()


        # --- Обновляем выбранное устройство ---
        old_device_id = self._selected_device_id
        self._selected_device_id = device_id
        logger.info(f"Selected device changed from '{old_device_id}' to: '{device_id}'")

        # --- Загружаем конфигурацию нового устройства ---
        # load_device_config обновит self.channel_configs
        #self.load_device_config(device_id)

        # --- Оповещаем GUI (если нужно) ---
        # Можно добавить специальный сигнал, если другие части GUI должны реагировать
        # self.selected_device_changed.emit(device_id)

        # --- Обновляем UI каналов и графика для нового устройства ---
        # Сбрасываем активный канал на дефолтный (например, вентилятор)
        # и вызываем switch_channel, чтобы он загрузил конфиг этого канала
        # из нового self.channel_configs и обновил UI (кнопки, график)
        self._current_channel_index = -2 # Или любой другой дефолтный индекс
        self.switch_channel(self._current_channel_index)

        # Очищаем историю отмен при смене устройства, т.к. она относится к предыдущему
        self._undo_history.clear()
        logger.debug("Undo history cleared due to device change.")

    # <<<------ КОНЕЦ МЕТОДА select_device <<<------

    def get_selected_device_id(self) -> Optional[DeviceId]:
         """Возвращает ID выбранного устройства."""
         return self._selected_device_id