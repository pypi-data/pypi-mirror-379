# Содержимое файла: multi_device_manager.py
import asyncio
import logging
from typing import Dict, List, Optional, Tuple, Any, NamedTuple, Literal # Добавлены NamedTuple, Literal
import serial.tools.list_ports # Для ListPortInfo

# --- Импорты ваших модулей ---
from smeller.communication.base import CommunicationInterface
from smeller.communication.factory import create_communication
# Используем DeviceInfo из bluetooth_com, если BtDeviceInfo не нужен для других целей
from smeller.communication.bluetooth_com import DeviceInfo as BtDeviceInfo # Переименовываем импорт, если нужен отдельный тип
# Если DeviceInfo из bluetooth_com подходит, используйте его напрямую:
# from smeller.communication.bluetooth_com import DeviceInfo
from smeller.config.config import AppConfig, MqttConfig, BaseDeviceDefinition
from smeller.utils.comport_manager import COMPortManager, ListPortInfo # Импортируем ListPortInfo
from smeller.services.mqtt_client import MqttClient # Для обнаружения MQTT устройств

from smeller.utils.events import Event, EventHandler

# --- Добавляем необходимые импорты для новой логики ---
from smeller.controllers.device_controller import DeviceController # Важно!
from smeller.commands.base import Command # Важно!
from smeller.commands.command_factory import CommandFactory # Важно!
from smeller.utils.exceptions import DeviceError, CommandError #

logger = logging.getLogger(__name__)

DeviceId = str  # Уникальный идентификатор устройства (e.g., COM_port, MAC_address, chip_id)

# --- Добавлено определение DeviceStatus ---
DeviceStatus = Literal["pending", "connecting", "connected", "disconnecting", "disconnected", "error"]

# --- Добавлено определение ConnectionInfo ---
class ConnectionInfo(NamedTuple):
    """Структура для хранения информации о соединении."""
    identifier: DeviceId
    connection_type: str
    status: DeviceStatus = "pending" # Статус по умолчанию
    config: Dict[str, Any] = {} # Конфигурация для конкретного устройства
    communication: Optional[CommunicationInterface] = None # Интерфейс связи после подключения
    last_error: Optional[str] = None # Последняя ошибка
    controller: Optional[DeviceController] = None
# --- Определение BtDeviceInfo теперь берется из bluetooth_com.py или остается, если нужно ---
# Если DeviceInfo из bluetooth_com подходит, эту строку можно удалить:
# class BtDeviceInfo(NamedTuple):
#    """Структура для информации об обнаруженном Bluetooth устройстве."""
#    address: str
#    name: Optional[str] = None


class MultiDeviceManager:
    """
    Manages multiple device connections and acts as a facade,
    routing commands to the currently selected active device.
    Mimics the public API of DeviceController.
    """

    def __init__(self, config: AppConfig, event_handler: EventHandler, port_manager: Optional[COMPortManager] = None):
        """
        Инициализирует менеджер устройств.

        Args:
        config: Конфигурация приложения.
        event_handler: Обработчик событий для DeviceController'ов.
        port_manager: Экземпляр COMPortManager (если не передан, создается новый).
        """
        self.config = config
        self.event_handler = event_handler # Сохраняем обработчик событий
        self.command_factory = CommandFactory() # Создаем фабрику команд
        
        # Используем переданный или создаем новый COMPortManager для обнаружения COM-портов
        # Используем getattr для безопасного доступа к discovery_cache_timeout
        cache_timeout = getattr(config, 'discovery_cache_timeout', 5.0)
        self.port_manager: COMPortManager = port_manager if port_manager else COMPortManager(
            cache_timeout=cache_timeout
        )
        # Хранилище информации о целевых и активных соединениях
        # Ключ - DeviceId (COM-порт, MAC-адрес, chip_id)
        # Значение - ConnectionInfo
        self.connections: Dict[DeviceId, ConnectionInfo] = {}

        # --- Новое: Хранилище для внутренних DeviceController'ов ---
        self._internal_controllers: Dict[DeviceId, DeviceController] = {}

        # --- Новое: ID активного устройства ---
        self._active_device_id: Optional[DeviceId] = None

        # MQTT клиент для обнаружения устройств и потенциального обмена командами
        # Он будет использоваться для всех MQTT-соединений (мультиплексирование)
        self.mqtt_config: MqttConfig = config.mqtt
        self.mqtt_client: Optional[MqttClient] = None
        self._mqtt_client_running: bool = False # Флаг состояния клиента
        if self.mqtt_config and self.mqtt_config.host: # Проверяем, что host задан
             try:
                 self.mqtt_client = MqttClient(
                     host=self.mqtt_config.host,
                     port=self.mqtt_config.port,
                     username=self.mqtt_config.username,
                     password=self.mqtt_config.password,
                    # client_id_suffix="-manager" # Добавляем суффикс, чтобы избежать конфликтов ID
                 )
                 # Запуск клиента MQTT лучше выполнять извне, например, в главном цикле приложения
                 #asyncio.create_task(self.mqtt_client.run()) # Не запускаем здесь
                 logger.info("MQTT client initialized for MultiDeviceManager.")
             except Exception as e:
                 logger.error(f"Failed to initialize MQTT client in MultiDeviceManager: {e}", exc_info=True)
                 self.mqtt_client = None # Явно указываем, что клиент не создан
        else:
             logger.warning("MQTT host not configured. MQTT discovery and connections will be unavailable.")

    def is_mqtt_client_running(self) -> bool:
        """Возвращает текущее состояние MQTT клиента."""
        # Дополнительно проверяем, жив ли поток, если start вызывался
        if self.mqtt_client and self._mqtt_client_running:
             return self.mqtt_client.isRunning()
        return False
    
    async def start_mqtt_client(self) -> bool:
        """Запускает MQTT клиент, если он создан и не запущен."""
        if self.mqtt_client and not self.is_mqtt_client_running():
            try:
                logger.info("Starting MQTT client thread...")
                self.mqtt_client.start() # Запускаем QThread
                # Добавим небольшую паузу, чтобы дать потоку запуститься и подключиться
                await asyncio.sleep(1) # Пауза для попытки подключения
                self._mqtt_client_running = self.mqtt_client.isRunning() # Обновляем флаг по факту
                if self._mqtt_client_running:
                     logger.info("MQTT client thread started.")
                     # Оповещаем об изменении статуса (опционально)
                     # await self.event_handler.publish(Event("mqtt_status_changed", data={'running': True}))
                     return True
                else:
                     logger.error("Failed to start MQTT client thread.")
                     return False
            except Exception as e:
                logger.error(f"Error starting MQTT client: {e}", exc_info=True)
                self._mqtt_client_running = False
                return False
        elif self.is_mqtt_client_running():
            logger.warning("MQTT client is already running.")
            return True # Уже запущен - считаем успехом
        else:
            logger.error("Cannot start MQTT client: client not initialized.")
            return False
    
    async def start_mqtt_client(self) -> bool:
        """Запускает MQTT клиент, если он создан и не запущен."""
        if self.mqtt_client and not self.is_mqtt_client_running():
            try:
                logger.info("Starting MQTT client thread...")
                self.mqtt_client.start() # Запускаем QThread
                # Добавим небольшую паузу, чтобы дать потоку запуститься и подключиться
                await asyncio.sleep(1) # Пауза для попытки подключения
                self._mqtt_client_running = self.mqtt_client.isRunning() # Обновляем флаг по факту
                if self._mqtt_client_running:
                     logger.info("MQTT client thread started.")
                     # Оповещаем об изменении статуса (опционально)
                     await self.event_handler.publish(Event("mqtt_status_changed", data={'running': True}))
                     return True
                else:
                     logger.error("Failed to start MQTT client thread.")
                     return False
            except Exception as e:
                logger.error(f"Error starting MQTT client: {e}", exc_info=True)
                self._mqtt_client_running = False
                return False
        elif self.is_mqtt_client_running():
            logger.warning("MQTT client is already running.")
            return True # Уже запущен - считаем успехом
        else:
            logger.error("Cannot start MQTT client: client not initialized.")
            return False
        
        
    async def stop_mqtt_client(self) -> bool:
        """Останавливает MQTT клиент, если он запущен."""
        if self.mqtt_client and self.is_mqtt_client_running():
            try:
                logger.info("Stopping MQTT client...")
                self.mqtt_client.stop() # Вызываем метод stop у MqttClient (QThread)
                # MqttClient.stop должен сам корректно завершать поток
                # Можно добавить ожидание, если stop не блокирующий:
                # self.mqtt_client.wait(5000) # Ждем до 5 секунд
                self._mqtt_client_running = False
                logger.info("MQTT client stopped.")
                # await self.event_handler.publish(Event("mqtt_status_changed", data={'running': False}))
                return True
            except Exception as e:
                logger.error(f"Error stopping MQTT client: {e}", exc_info=True)
                # Флаг может остаться true, если остановка не удалась
                self._mqtt_client_running = self.mqtt_client.isRunning()
                return False
        elif not self.is_mqtt_client_running():
            logger.warning("MQTT client is not running.")
            self._mqtt_client_running = False # Убедимся, что флаг сброшен
            return True # Уже остановлен - считаем успехом
        else:
            logger.error("Cannot stop MQTT client: client not initialized.")
            return False

    def discover_serial_ports(self, refresh: bool = False) -> List[ListPortInfo]:
        """
        Возвращает список доступных COM портов, используя COMPortManager.

        Args:
            refresh: Принудительно обновить кэш портов.

        Returns:
            Список объектов ListPortInfo.
        """
        logger.debug(f"Discovering serial ports (refresh={refresh})...")
        try:
            ports = self.port_manager.get_com_ports(refresh=refresh)
            logger.info(f"Discovered {len(ports)} serial ports.")
            return ports
        except Exception as e:
            logger.error(f"Error discovering serial ports: {e}", exc_info=True)
            return []

    # --- Скорректирован метод discover_bluetooth_devices ---
    async def discover_bluetooth_devices(self, scan_duration: Optional[int] = None) -> List[BtDeviceInfo]:
        """
        Асинхронно обнаруживает Bluetooth устройства поблизости.
        Использует временный контроллер Bluetooth для сканирования и получения списка DeviceInfo.

        Args:
            scan_duration: Время сканирования в секундах (если None, используется значение из конфига).

        Returns:
            Список объектов BtDeviceInfo (или DeviceInfo из bluetooth_com).
        """
        duration = scan_duration if scan_duration is not None else self.config.bluetooth.discovery_duration
        logger.debug(f"Discovering Bluetooth devices (duration={duration}s)...")
        # Локальный импорт, чтобы избежать циклической зависимости, если BT не используется
        try:
            from smeller.communication.bluetooth_com import BluetoothDeviceController
        except ImportError:
            logger.error("Bluetooth communication module not found. Cannot discover BT devices.")
            return []

        # Создаем временный контроллер только для обнаружения
        # Передаем ему конфиг, чтобы он знал длительность сканирования по умолчанию и т.д.
        temp_bt_controller = BluetoothDeviceController(self.config)
        # Устанавливаем кастомную длительность, если она передана
        if scan_duration is not None:
             temp_bt_controller.discovery_duration = scan_duration

        discovered_devices: List[BtDeviceInfo] = []
        try:
            # Метод discover_devices из BluetoothDeviceController уже возвращает List[DeviceInfo]
            # DeviceInfo(mac, name, com_port, is_paired)
            # Нам для простого обнаружения достаточно mac и name
            devices_info = await temp_bt_controller.discover_devices() # Используем duration из контроллера

            # Преобразуем результат в BtDeviceInfo, если мы используем отдельный тип
            # Если BtDeviceInfo = DeviceInfo, то просто возвращаем devices_info
            # В данном случае BtDeviceInfo = DeviceInfo, поэтому преобразование не нужно
            discovered_devices = devices_info # Прямое присваивание

            # Если бы BtDeviceInfo был другим типом (например, только mac и name):
            # discovered_devices = [
            #     BtDeviceInfo(address=dev.mac, name=dev.name) for dev in devices_info
            # ]

            logger.info(f"Discovered {len(discovered_devices)} Bluetooth devices.")

        except Exception as e:
            logger.error(f"Bluetooth discovery failed: {e}", exc_info=True)
        # finally:
            # Здесь можно добавить очистку ресурсов temp_bt_controller, если она нужна

        return discovered_devices

    def get_discovered_mqtt_devices(self) -> List[DeviceId]:
        """
        Возвращает список Chip ID устройств, которые отправляли сообщения
        (обнаружены через MQTT).

        **Требует реализации метода `get_discovered_chip_ids()` в вашем `MqttClient`.**

        Returns:
            Список строк (Chip ID).
        """
        if self.mqtt_client:
            try:
                # Предполагаем, что у MqttClient есть метод get_discovered_chip_ids()
                # !!! ВАЖНО: Убедитесь, что этот метод реализован в smeller.services.mqtt_client.MqttClient !!!
                discovered_ids = self.mqtt_client.get_discovered_chip_ids() # Пример вызова
                logger.info(f"Found {len(discovered_ids)} devices via MQTT discovery.")
                return discovered_ids
            except AttributeError:
                 logger.error("Method 'get_discovered_chip_ids' not found in MqttClient. MQTT discovery unavailable.", exc_info=True)
                 return []
            except Exception as e:
                logger.error(f"Failed to get discovered MQTT devices from client: {e}", exc_info=True)
                return []
        else:
            logger.warning("MQTT client not initialized. Cannot get discovered MQTT devices.")
            return []


    # --- Новое: Управление активным устройством ---
    def select_active_device(self, device_id: Optional[DeviceId]):
        """Выбирает активное устройство для отправки команд."""
        if device_id is None:
            self._active_device_id = None
            logger.info("No device selected as active.")
        elif device_id in self._internal_controllers:
            self._active_device_id = device_id
            logger.info(f"Device '{device_id}' selected as active.")
        # Можно добавить сигнал для GUI об изменении активного устройства
        # self.event_handler.publish(Event("active_device_changed", data=device_id))
        elif device_id in self.connections:
            logger.warning(f"Cannot select device '{device_id}' as active: not connected (no internal controller).")
        else:
            logger.warning(f"Cannot select device '{device_id}' as active: device not registered.")

    def get_active_device_id(self) -> Optional[DeviceId]:
        """Возвращает ID активного устройства."""
        return self._active_device_id

    def get_active_controller(self) -> Optional[DeviceController]:
        """Возвращает экземпляр DeviceController для активного устройства."""
        if self._active_device_id:
            return self._internal_controllers.get(self._active_device_id)
        return None
    
    def get_active_controller(self) -> Optional[DeviceController]:
        """Возвращает контроллер для текущего активного и подключенного устройства."""
        if self._active_device_id:
            conn_info = self.connections.get(self._active_device_id)
            if conn_info and conn_info.status == "connected":
                return conn_info.controller
            # Если активное устройство больше не подключено, логируем это
            elif conn_info:
                logger.warning(f"Active device '{self._active_device_id}' is not connected (status: {conn_info.status}).")
            else:
                # Этого не должно произойти, если select_active_device работает правильно
                logger.error(f"Active device ID '{self._active_device_id}' set, but device not found in connections.")
                self._active_device_id = None # Сбрасываем некорректный ID
        return None
    # --- Управление целевыми устройствами ---
    def add_target_device(self, identifier: DeviceId, connection_type: str, config: Optional[Dict[str, Any]] = None):
        """
        Регистрирует устройство в менеджере для последующего подключения.

        Args:
            identifier: Уникальный идентификатор устройства (COM-порт, MAC, chip_id).
            connection_type: Тип соединения ('serial', 'bluetooth', 'mqtt').
            config: Словарь с дополнительными параметрами для метода connect соответствующего CommunicationInterface.
        """
        if not identifier:
            logger.error("Cannot add target device: identifier is empty.")
            return

        if identifier in self.connections:
            logger.warning(f"Device {identifier} already registered. Updating config.")
            # Обновляем только конфиг и тип, если они переданы, статус не трогаем
            current_info = self.connections[identifier]
            new_config = config if config is not None else current_info.config
            self.connections[identifier] = current_info._replace(
                connection_type=connection_type,
                config=new_config
            )
        else:
            logger.info(f"Registering new target device: {identifier} (type: {connection_type})")
            # Создаем новую запись ConnectionInfo
            conn_info = ConnectionInfo(
                identifier=identifier,
                connection_type=connection_type,
                config=config if config is not None else {}, # Пустой словарь, если конфиг не передан
                status="pending", # Начальный статус - ожидание
                communication=None,
                last_error=None,
                controller=None
            )
            self.connections[identifier] = conn_info

        # Оповещаем об изменении списка целевых устройств (если нужно для GUI)
        #asyncio.create_task(self.event_handler.publish(Event("target_device_list_updated")))


    def remove_target_device(self, identifier: DeviceId):
        """
        Удаляет устройство из списка целевых. Если устройство было подключено, оно отключается.
        """
        if identifier in self.connections:
            logger.info(f"Removing target device: {identifier}")
            conn_info = self.connections[identifier]
            # Если устройство подключено, сначала отключаем его
            if conn_info.status in ["connected", "connecting"]:
                asyncio.create_task(self.disconnect_device(identifier)) # Запускаем отключение в фоне

            # Удаляем запись из словаря
            del self.connections[identifier]
            # Оповещаем об изменении списка целевых устройств (если нужно для GUI)
            # asyncio.create_task(self.event_handler.publish(Event("target_device_list_updated")))
        else:
            logger.warning(f"Cannot remove device {identifier}: not found in target list.")


    async def connect_device(self, identifier: DeviceId) -> bool:
        """
        Подключает конкретное устройство из списка целевых.

        Args:
            identifier: Идентификатор устройства для подключения.

        Returns:
            True в случае успеха, False в случае ошибки.
        """
        if identifier not in self.connections:
            logger.error(f"Device {identifier} not found in target list. Cannot connect.")
            await self.event_handler.publish(Event("device_connection_failed", data={'identifier': identifier, 'error': "Device not registered."}))
            return False

        conn_info = self.connections[identifier]
        logger.info(f"Device {identifier} {conn_info}")
        # Проверяем текущий статус
        # Добавлена проверка на существование communication и вызов is_connected (если он есть)

        if conn_info.status == "connected" and conn_info.communication and conn_info.controller:
            logger.info(f"Device {identifier} is already connected.")
            return True

        if conn_info.status == "connecting":
            logger.warning(f"Device {identifier} is already connecting. Please wait.")
            # Возвращаем True, т.к. процесс уже идет (можно вернуть False, если нужно блокировать повторный вызов)
            return True # Или False

        logger.info(f"Attempting to connect device: {identifier} ({conn_info.connection_type})")
        self._update_connection_status(identifier, "connecting", error_message=None)

        try:
            # --- Создание или получение интерфейса связи ---
            comm: Optional[CommunicationInterface] = None
            comm = create_communication(self.config, conn_info.connection_type, port_manager=self.port_manager)

            if not comm:
                raise ConnectionError(f"Failed to create communication interface for type {conn_info.connection_type}")
            connect_kwargs = conn_info.config.copy()
            # Валидация: Проверим, что необходимые ключи есть в connect_kwargs
            required_key = None
            if conn_info.connection_type == "serial":
                required_key = 'port'
            elif conn_info.connection_type == "bluetooth":
                required_key = 'mac_address'
            elif conn_info.connection_type == "mqtt":
                required_key = 'chip_id'

            if required_key and required_key not in connect_kwargs:
                 raise ValueError(f"Missing required connection parameter '{required_key}' in config for device {identifier}")
            if required_key and not connect_kwargs[required_key]:
                 raise ValueError(f"Required connection parameter '{required_key}' is empty in config for device {identifier}")


            logger.debug(f"Calling {conn_info.connection_type} connect with args: {connect_kwargs}")
            # Теперь connect_kwargs будет содержать {'port': 'COM3', 'baudrate': 115200, ...}
            connected = await comm.connect(**connect_kwargs)

            if connected:
                logger.info(f"Successfully established communication for {identifier}")
                device_controller = DeviceController(comm, self.config, self.event_handler) # config тут общий, но можно передать device_specific_config, если нужно

                # Обновляем статус и сохраняем communication И controller
                self._update_connection_status(identifier, "connected", communication=comm, controller=device_controller, error_message=None)
                await self.event_handler.publish(Event("device_connected", data={'identifier': identifier}))
                return True
            else:
                # Важно: Если comm.connect вернул False, сам comm должен залогировать причину
                logger.error(f"Failed to connect to {identifier} ({conn_info.connection_type} connect method returned False). Check communication logs.")
                self._update_connection_status(identifier, "error", error_message="Connection attempt failed (returned False).", communication=None, controller=None)
                await self.event_handler.publish(Event("device_connection_failed", data={'identifier': identifier, 'error': "Connection attempt failed (returned False)."}))
                return False

        except Exception as e:
            logger.error(f"Error connecting to {identifier}: {e}", exc_info=True)
            self._update_connection_status(identifier, "error", error_message=str(e), communication=None, controller=None)
            await self.event_handler.publish(Event("device_connection_failed", data={'identifier': identifier, 'error': str(e)}))
            return False
        finally:
            if identifier in self.connections and self.connections[identifier].status != "connected":
                self._update_connection_status(identifier, self.connections[identifier].status, controller=None)



    async def connect_all_pending(self):
        """Пытается подключить все устройства со статусом 'pending'."""
        pending_devices = [id for id, info in self.connections.items() if info.status == "pending"]
        if not pending_devices:
            logger.info("No pending devices to connect.")
            return

        logger.info(f"Attempting to connect pending devices: {pending_devices}")
        tasks = [self.connect_device(dev_id) for dev_id in pending_devices]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for dev_id, result in zip(pending_devices, results):
            if isinstance(result, Exception):
                logger.error(f"Error connecting pending device {dev_id}: {result}")
            elif not result:
                logger.warning(f"Failed to connect pending device {dev_id} (connect returned False).")
            # Успешное подключение уже залогировано в connect_device
               
    async def disconnect_all_connected(self):
        """Отключает все устройства со статусом 'connected'."""
        connected_devices = [id for id, info in self.connections.items() if info.status == "connected"]
        if not connected_devices:
            logger.info("No connected devices to disconnect.")
            return

        logger.info(f"Attempting to disconnect connected devices: {connected_devices}")
        tasks = [self.disconnect_device(dev_id) for dev_id in connected_devices]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for dev_id, result in zip(connected_devices, results):
            if isinstance(result, Exception):
                logger.error(f"Error disconnecting device {dev_id}: {result}")
            # Успешное отключение уже залогировано в disconnect_device

    # ------>>> НОВЫЙ МЕТОД для получения контроллера <<<------
    def get_device_controller(self, identifier: DeviceId) -> Optional[DeviceController]:
        """Возвращает экземпляр DeviceController для указанного устройства."""
        conn_info = self.connections.get(identifier)
        if conn_info and conn_info.status == "connected":
            return conn_info.controller
        logger.warning(f"Device controller not available for {identifier} (status: {conn_info.status if conn_info else 'not found'}).")
        return None
    
    

    async def send_command_to_all(self, command_str: str, timeout: float = 5.0) -> Dict[DeviceId, Optional[Any]]:
        """
        Отправляет команду всем подключенным устройствам.

        Returns:
            Словарь {device_id: response}, где response - ответ от устройства или None/Exception при ошибке.
        """
        connected_devices = {id: info for id, info in self.connections.items() if info.status == "connected"}
        if not connected_devices:
            logger.warning("No connected devices to send command to.")
            return {}

        logger.info(f"Sending command '{command_str}' to all connected devices: {list(connected_devices.keys())}")
        tasks = {dev_id: self.send_command(dev_id, command_str, timeout) for dev_id in connected_devices}

        # Используем asyncio.gather для параллельного выполнения
        results = await asyncio.gather(*tasks.values(), return_exceptions=True)

        # Собираем результаты в словарь
        responses = {}
        for dev_id, result in zip(tasks.keys(), results):
            if isinstance(result, Exception):
                logger.error(f"Error sending command to {dev_id}: {result}")
                responses[dev_id] = result # Сохраняем исключение как результат
            else:
                responses[dev_id] = result

        return responses
    
    # Этот метод больше не нужен для DynamicBlockController, но может быть полезен для ручного управления
    async def send_command(self, identifier: DeviceId, command_str: str, timeout: float = 5.0) -> Optional[Any]:
        """
        Отправляет команду конкретному подключенному устройству через его DeviceController.

        Args:
        identifier: Идентификатор целевого устройства.
        command_str: Строка команды для отправки.
        timeout: Таймаут ожидания ответа (используется внутри DeviceController/Communication).

        Returns:
        Распарсенный ответ от команды или None в случае ошибки.
        """
        controller = self.get_device_controller(identifier)
        if not controller:
            logger.error(f"Device {identifier} not connected or controller not available. Cannot send command '{command_str}'.")
            return None

        logger.debug(f"Sending command '{command_str}' via DeviceController for {identifier}...")
        try:
            # Используем метод send_raw_command контроллера устройства
            # timeout используется внутри send_raw_command -> send_command -> communication.send_command
            response = await controller.send_raw_command(command_str) # send_raw_command возвращает распарсенный ответ
            logger.debug(f"Parsed response from {identifier} for '{command_str}': {response}")
            return response
        except DeviceError as e: # Ловим специфичные ошибки контроллера/команды
            logger.error(f"Device error sending command '{command_str}' to {identifier}: {e}")
            # Статус 'error' должен устанавливаться внутри обработчика событий контроллера
            await self.event_handler.publish(Event("command_failed", data={'identifier': identifier, 'command': command_str, 'error': str(e)}))
            return None
        except Exception as e:
            logger.error(f"Unexpected error sending command '{command_str}' to {identifier}: {e}", exc_info=True)
            self._update_connection_status(identifier, "error", error_message=f"Communication error: {e}")
            await self.event_handler.publish(Event("command_failed", data={'identifier': identifier, 'command': command_str, 'error': f"Unexpected error: {e}"}))
            return None
        

    async def reset_channels(self) -> Dict[DeviceId, Optional[Any]]:
        """
        Отправляет команду 'r' (сброс всех каналов) всем подключенным устройствам.

        Returns:
            Словарь {device_id: response}, где response - ответ от устройства или None/Exception при ошибке.
        """
        connected_controllers: Dict[DeviceId, DeviceController] = {
            dev_id: info.controller
            for dev_id, info in self.connections.items()
            if info.status == "connected" and info.controller is not None
        }

        if not connected_controllers:
            logger.warning("Cannot reset channels: no connected devices found.")
            return {}

        logger.info(f"Sending reset_channels to devices: {list(connected_controllers.keys())}")

        tasks = {
            dev_id: controller.reset_channels()
            for dev_id, controller in connected_controllers.items()
        }

        results = await asyncio.gather(*tasks.values(), return_exceptions=True)

        responses = {}
        for dev_id, result in zip(tasks.keys(), results):
            if isinstance(result, Exception):
                logger.error(f"Error resetting channels for {dev_id}: {result}")
                responses[dev_id] = result
            else:
                logger.debug(f"Reset channels response from {dev_id}: {result}")
                responses[dev_id] = result

        return responses

    async def set_fan_config(self, pwmMax: int, pwmMin: int, pwmMode: int, period: int) -> Dict[DeviceId, Optional[Any]]:
        """
        Отправляет команду 'x' (конфигурация вентилятора) всем подключенным устройствам.

        Args:
            pwmMax: Максимальный PWM.
            pwmMin: Минимальный PWM.
            pwmMode: Режим PWM.
            period: Период.

        Returns:
            Словарь {device_id: response}, где response - ответ от устройства или None/Exception при ошибке.
        """
        connected_controllers: Dict[DeviceId, DeviceController] = {
            dev_id: info.controller
            for dev_id, info in self.connections.items()
            if info.status == "connected" and info.controller is not None
        }

        if not connected_controllers:
            logger.warning("Cannot set fan config: no connected devices found.")
            return {}

        logger.info(f"Sending set_fan_config(max={pwmMax}, min={pwmMin}, mode={pwmMode}, period={period}) to devices: {list(connected_controllers.keys())}")

        tasks = {
            dev_id: controller.set_fan_config(pwmMax, pwmMin, pwmMode, period)
            for dev_id, controller in connected_controllers.items()
        }

        results = await asyncio.gather(*tasks.values(), return_exceptions=True)

        responses = {}
        for dev_id, result in zip(tasks.keys(), results):
            if isinstance(result, Exception):
                logger.error(f"Error setting fan config for {dev_id}: {result}")
                responses[dev_id] = result
            else:
                logger.debug(f"Set fan config response from {dev_id}: {result}")
                responses[dev_id] = result

        return responses

    
    # --- Методы-прослойки для DynamicBlockController ---
    async def set_channel_parameters(self, channel: int, on_tick: int, off_tick: int, **kwargs) -> Dict[DeviceId, Optional[Any]]:
        """
        Отправляет команду 'p' (установка параметров канала) всем подключенным устройствам.

        Args:
            channel: Номер канала.
            on_tick: Время включения (в тиках).
            off_tick: Время выключения (в тиках).
            **kwargs: Дополнительные параметры команды (если есть).

        Returns:
            Словарь {device_id: response}, где response - ответ от устройства или None/Exception при ошибке.
        """
        connected_controllers: Dict[DeviceId, DeviceController] = {
            dev_id: info.controller
            for dev_id, info in self.connections.items()
            if info.status == "connected" and info.controller is not None
        }

        #if not connected_controllers:
        #    logger.warning("Cannot set channel parameters: no connected devices found.")
        #    return {}

        logger.info(f"Sending set_channel_parameters(ch={channel}, on={on_tick}, off={off_tick}) to devices: {list(connected_controllers.keys())}")

        # Создаем задачи для параллельной отправки
        tasks = {
            dev_id: controller.set_channel_parameters(dev_id, channel, on_tick, off_tick, **kwargs)
            for dev_id, controller in connected_controllers.items()
        }

        # Запускаем задачи и собираем результаты (включая исключения)
        results = await asyncio.gather(*tasks.values(), return_exceptions=True)

        # Формируем словарь результатов
        responses = {}
        for dev_id, result in zip(tasks.keys(), results):
            if isinstance(result, Exception):
                logger.error(f"Error setting channel parameters for {dev_id}: {result}")
                responses[dev_id] = result # Сохраняем исключение
                # Опционально: обновить статус устройства на 'error'
                # self._update_connection_status(dev_id, "error", error_message=f"Command failed: {result}")
            else:
                logger.debug(f"Set channel parameters response from {dev_id}: {result}")
                responses[dev_id] = result

        return responses
    
    async def channel_off(self, channel: int, mod: Optional[int] = None) -> Dict[DeviceId, Optional[Any]]:
        """
        Отправляет команду 'd' (выключить канал) всем подключенным устройствам.

        Args:
            channel: Номер канала.
            mod: Модификатор (если используется).

        Returns:
            Словарь {device_id: response}, где response - ответ от устройства или None/Exception при ошибке.
        """
        connected_controllers: Dict[DeviceId, DeviceController] = {
            dev_id: info.controller
            for dev_id, info in self.connections.items()
            if info.status == "connected" and info.controller is not None
        }

        if not connected_controllers:
            logger.warning("Cannot turn off channel: no connected devices found.")
            return {}

        logger.info(f"Sending channel_off(ch={channel}, mod={mod}) to devices: {list(connected_controllers.keys())}")

        tasks = {
            dev_id: controller.channel_off(channel, mod)
            for dev_id, controller in connected_controllers.items()
        }

        results = await asyncio.gather(*tasks.values(), return_exceptions=True)

        responses = {}
        for dev_id, result in zip(tasks.keys(), results):
            if isinstance(result, Exception):
                logger.error(f"Error turning off channel for {dev_id}: {result}")
                responses[dev_id] = result
            else:
                logger.debug(f"Channel off response from {dev_id}: {result}")
                responses[dev_id] = result

        return responses
        
    # --- Метод disconnect (пример) ---
    async def disconnect_device(self, identifier: DeviceId):
        """Отключает устройство и очищает ресурсы."""
        logger.info(f"Disconnecting device: {identifier}")
        conn_info = self.connections.get(identifier)
        if not conn_info:
            logger.warning(f"Device {identifier} not found for disconnecting.")
            return

        # Если устройство уже отключается или отключено, выходим
        if conn_info.status in ["disconnecting", "disconnected"]:
            logger.debug(f"Device {identifier} is already {conn_info.status}.")
            return
        

       
        # Разрываем соединение через communication interface
        if conn_info.communication:
            try:
                if conn_info.connection_type == 'mqtt':
                    # Для MQTT может потребоваться специальный метод disconnect_chip
                    if hasattr(conn_info.communication, 'disconnect_chip'):
                        await conn_info.communication.disconnect_chip(identifier)
                    else:
                        # Если общего disconnect нет или он не подходит, возможно, ничего делать не нужно
                        logger.debug(f"MQTT chip {identifier} deregistered implicitly or disconnect_chip not available.")
                else:
                    await conn_info.communication.disconnect()
                    logger.debug(f"Called disconnect for {conn_info.connection_type} device {identifier}.")
            except Exception as e:
                    logger.error(f"Error during communication disconnect for {identifier}: {e}", exc_info=True)
                    self._update_connection_status(identifier, "error", communication=None, controller=None, error_message=f"Disconnect error: {e}")
                    await self.event_handler.publish(Event("device_disconnected", data={'identifier': identifier, 'error': str(e)})) # Сообщаем об ошибке
                    return # Выходим, так как статус уже 'error'

        # Обновляем статус и очищаем ссылки
        self._update_connection_status(identifier, "disconnected", communication=None, controller=None, error_message=None)
        # Отправляем событие об отключении
        await self.event_handler.publish(Event("device_disconnected", data={'identifier': identifier}))
        logger.info(f"Device {identifier} disconnected successfully.")


    # --- Метод для получения списка устройств и статусов (пример) ---
    def get_connection_statuses(self) -> Dict[DeviceId, Tuple[DeviceStatus, Optional[str]]]:
        """Возвращает словарь статусов устройств {identifier: (status, last_error)}."""
        return {
                identifier: (conn_info.status, conn_info.last_error)
                for identifier, conn_info in self.connections.items()
                }
    # --- Очистка ресурсов при завершении работы ---
    async def cleanup(self):
        """Отключает все подключенные устройства перед завершением работы."""
        logger.info("MultiDeviceManager cleanup: Disconnecting all devices...")
        await self.disconnect_all_connected()
        if self.mqtt_client:
            await self.stop_mqtt_client()# Останавливаем MQTT клиент, если он был создан
        logger.info("MultiDeviceManager cleanup finished.")



    # --- Внутренний метод обновления статуса (Очищенный) ---
    def _update_connection_status(self,
                    identifier: DeviceId,
                    status: DeviceStatus,
                    communication: Optional[CommunicationInterface] = Ellipsis,
                    controller: Optional[DeviceController] = Ellipsis,
                    error_message: Optional[str] = None):
        """
        Внутренний метод для обновления статуса соединения, интерфейса связи и контроллера.
        """
        if identifier not in self.connections:
            logger.warning(f"Tried to update status for non-existent device {identifier}")
            return

        conn_info = self.connections[identifier]

        # Определяем новые значения, используя Ellipsis как маркер "не изменять"
        new_comm = conn_info.communication if communication is Ellipsis else communication
        new_controller = conn_info.controller if controller is Ellipsis else controller
        # Обновляем ошибку: устанавливаем новую, если статус 'error', очищаем, если статус не 'error', иначе оставляем как есть
        new_error = error_message if status == "error" else (None if status != "error" else conn_info.last_error)
        # --- КЛЮЧЕВОЕ ИЗМЕНЕНИЕ: Управление флагом _is_connected контроллера ---
        if new_controller is not None: # Если контроллер существует (или только что создан)
            if status == "connected":
                new_controller._is_connected = True # Устанавливаем флаг вручную
                logger.debug(f"Set internal _is_connected=True for controller {identifier}")
            else:
                # Если статус НЕ connected, сбрасываем флаг контроллера
                if new_controller._is_connected: # Сбрасываем только если был True
                     new_controller._is_connected = False
                     logger.debug(f"Set internal _is_connected=False for controller {identifier}")
        # --- КОНЕЦ ИЗМЕНЕНИЯ ---
        # Если статус меняется на НЕ 'connected', автоматически очищаем controller и communication,
        # если только они не переданы явно (например, при переходе в 'error' из 'connecting')
        if status != "connected":
            if communication is Ellipsis: # Если явно не передали, очищаем
                    new_comm = None
            if controller is Ellipsis: # Если явно не передали, очищаем
                    new_controller = None

        # Создаем новый экземпляр ConnectionInfo с обновленными данными
        self.connections[identifier] = conn_info._replace(
        status=status,
        communication=new_comm,
        controller=new_controller,
        last_error=new_error
        )
        logger.debug(f"Status updated for {identifier}: {status}" + (f" (Error: {new_error})" if new_error else ""))

        # Отправляем событие об изменении статуса через ГЛАВНЫЙ EventHandler
        asyncio.create_task(self.event_handler.publish(Event("device_status_changed", data={"identifier": identifier, "status": status, "error": new_error})))



# >>> НОВЫЙ МЕТОД для авто-подключения <<<
    async def connect_defined_devices(self):
        """
        Читает `defined_devices` из AppConfig, регистрирует их
        и пытается подключить все устройства, помеченные как enabled.
        """
        if not hasattr(self.config, 'defined_devices') or not isinstance(self.config.defined_devices, list):
                logger.warning("No 'defined_devices' list found in AppConfig or it's not a list. Skipping auto-connect.")
                return

        logger.info(f"Starting auto-connection process for {len(self.config.defined_devices)} defined devices...")
        connect_tasks = []

        for device_def in self.config.defined_devices:
            # Проверяем, что это объект нужного типа (BaseDeviceDefinition или словарь)
            if isinstance(device_def, BaseDeviceDefinition):
                # Если это датакласс (рекомендуемый подход)
                if not getattr(device_def, 'enabled', True): # По умолчанию enabled=True, если атрибута нет
                        logger.info(f"Skipping device '{getattr(device_def, 'id', 'N/A')}': disabled in config.")
                        continue

                identifier = getattr(device_def, 'id', None)
                connection_type = getattr(device_def, 'connection_type', None)

                if not identifier or not connection_type:
                        logger.warning(f"Skipping device definition due to missing 'id' or 'connection_type': {device_def}")
                        continue

                # Формируем словарь config для add_target_device и connect_device
                connect_config = {}
                # 1. Добавляем общие параметры из device_config датакласса
                if hasattr(device_def, 'device_config') and device_def.device_config:
                    # Преобразуем DeviceConfig в словарь, если нужно
                        if hasattr(device_def.device_config, '__dict__'):
                            # Простой способ для простых датаклассов
                            connect_config.update(vars(device_def.device_config))
                    # elif dataclasses.is_dataclass(device_def.device_config):
                    #      connect_config.update(dataclasses.asdict(device_def.device_config))

                # 2. Добавляем специфичные параметры (port, baudrate, mac_address, chip_id)
                # Они могут быть как в корне device_def, так и внутри device_config
                if connection_type == 'serial':
                        connect_config['port'] = getattr(device_def, 'port', identifier) # Используем порт из определения или сам identifier
                        connect_config['baudrate'] = getattr(device_def, 'baudrate', self.config.serial.baudrate)
                elif connection_type == 'bluetooth':
                        # MAC адрес должен быть в определении устройства
                        connect_config['mac_address'] = getattr(device_def, 'mac_address', identifier) # Используем mac или identifier
                        connect_config['baudrate'] = getattr(device_def, 'baudrate', self.config.bluetooth.baudrate) # Baudrate для BT
                elif connection_type == 'mqtt':
                        connect_config['chip_id'] = getattr(device_def, 'chip_id', identifier) # Используем chip_id или identifier

                # 3. Добавляем остальные атрибуты из device_def (если они есть и нужны для connect)
                # Например, 'timeout', 'response_mode' могут быть напрямую в device_def
                for key, value in vars(device_def).items():
                        if key not in ['id', 'name', 'enabled', 'connection_type', 'device_config', 'port', 'baudrate', 'mac_address', 'chip_id'] and key not in connect_config:
                            connect_config[key] = value

                # Регистрируем устройство
                self.add_target_device(identifier, connection_type, connect_config)
                # Добавляем задачу на подключение
                connect_tasks.append(self.connect_device(identifier))

            elif isinstance(device_def, dict):
            # Если используется старый формат словарей (менее предпочтительно)
                if not device_def.get('enabled', True):
                    logger.info(f"Skipping device '{device_def.get('id', 'N/A')}': disabled in config.")
                    continue

                identifier = device_def.get('id')
                connection_type = device_def.get('connection_type')

                if not identifier or not connection_type:
                    logger.warning(f"Skipping dictionary device definition due to missing 'id' or 'connection_type': {device_def}")
                    continue

            # Формируем config из словаря
                connect_config = device_def.get('device_config', {})
                if not isinstance(connect_config, dict): # Проверка типа
                    connect_config = {}

                if connection_type == 'serial':
                    connect_config['port'] = device_def.get('port', identifier)
                    connect_config['baudrate'] = device_def.get('baudrate', self.config.serial.baudrate)
                elif connection_type == 'bluetooth':
                    connect_config['mac_address'] = device_def.get('mac_address', identifier)
                    connect_config['baudrate'] = device_def.get('baudrate', self.config.bluetooth.baudrate)
                elif connection_type == 'mqtt':
                    connect_config['chip_id'] = device_def.get('chip_id', identifier)

            # Добавляем остальные ключи из device_def, которых нет в connect_config
                for key, value in device_def.items():
                    if key not in ['id', 'name', 'enabled', 'connection_type', 'device_config', 'port', 'baudrate', 'mac_address', 'chip_id'] and key not in connect_config:
                        connect_config[key] = value

                self.add_target_device(identifier, connection_type, connect_config)
                connect_tasks.append(self.connect_device(identifier))
            else:
                logger.warning(f"Skipping invalid device definition (not a dict or BaseDeviceDefinition): {device_def}")


        if connect_tasks:
            logger.info(f"Attempting to connect {len(connect_tasks)} enabled devices...")
            # Запускаем все задачи подключения параллельно
            results = await asyncio.gather(*connect_tasks, return_exceptions=True)

            # Логируем результаты
            success_count = 0
            for i, result in enumerate(results):
            # Получаем identifier из задачи (не самый надежный способ, лучше хранить связку задача-identifier)
            # Пока просто используем индекс для логирования
                if isinstance(result, Exception):
                    logger.error(f"Auto-connect task #{i+1} failed: {result}")
                elif result: # connect_device вернул True
                    success_count += 1
            # Если вернул False, ошибка уже залогирована в connect_device
            logger.info(f"Auto-connection process finished. Successfully connected {success_count} out of {len(connect_tasks)} devices attempted.")
        else:
            logger.info("No enabled devices found to auto-connect.")
        # >>> КОНЕЦ НОВОГО МЕТОДА <<<