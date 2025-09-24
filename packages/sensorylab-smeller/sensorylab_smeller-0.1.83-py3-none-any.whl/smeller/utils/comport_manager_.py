# smeller/utils/comport_manager.py
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parents[2]  # Поднимаемся на два уровня вверх
sys.path.append(str(project_root))

import asyncio
import re, time
import logging
from typing import List, Optional, Tuple, NamedTuple, Any
import serial
import bluetooth as bt
import serial.tools.list_ports
from smeller.config.config import AppConfig
from smeller.communication.bluetooth_com import BluetoothDeviceController, DeviceInfo

logging.basicConfig(
    level=logging.DEBUG,  # Понижаем уровень до DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("device_debug.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Типовые константы
DEFAULT_CACHE_TIMEOUT = 5 # Уменьшил таймаут кеширования

class ListPortInfo(NamedTuple):
    device: str
    name: Optional[str]
    description: Optional[str]
    hwid: Optional[str]
    vid: Optional[int]
    pid: Optional[int]
    serial_number: Optional[str]
    location: Optional[str]
    manufacturer: Optional[str]
    product: Optional[str]
    interface: Optional[str]
    # Добавляем метод для удобного представления, если нужно
    def __str__(self) -> str:
        return f"{self.device}: {self.description} ({self.hwid})"



class COMPortManager:
    """
    Менеджер для обнаружения и управления информацией о COM-портах и
    Bluetooth-устройствах, представленных как COM-порты.
    Выполняет роль PortDiscoveryService.
    """
    def __init__(self, config: AppConfig, cache_timeout: float = DEFAULT_CACHE_TIMEOUT):
        """
        Инициализация менеджера портов.

        Args:
            config: Конфигурация приложения (AppConfig).
            cache_timeout: Время жизни кэша для результатов сканирования (в секундах).
        """
        self.config = config # Сохраняем конфигурацию
        self._ports_cache: Optional[List[ListPortInfo]] = None
        self._last_ports_update: float = 0
        # Добавляем кэш для Bluetooth устройств
        self._bt_devices_cache: Optional[List[DeviceInfo]] = None
        self._last_bt_update: float = 0
        self.cache_timeout: float = cache_timeout
        # Экземпляр BluetoothDeviceController будет создаваться по требованию
        self._bt_controller: Optional[BluetoothDeviceController] = None

        # Регулярное выражение для MAC-адреса в HWID (можно оставить как есть)
        self._mac_pattern = re.compile(r"&([0-9A-F]{12})", re.IGNORECASE)


    # --- Методы для обнаружения COM-портов (синхронные) ---

    def get_com_ports(self, refresh: bool = False) -> List[ListPortInfo]:
        """
        Возвращает список доступных COM-портов. Использует кэширование.

        Args:
            refresh: Принудительно обновить список портов, игнорируя кэш.

        Returns:
            Список объектов ListPortInfo.
        """
        logger.debug(f"Getting COM ports (refresh={refresh})...")
        now = time.monotonic() # Используем monotonic для измерения времени
        if (
            not refresh
            and self._ports_cache is not None # Проверяем, что кэш не None
            and (now - self._last_ports_update) < self.cache_timeout
        ):
            logger.debug(f"Returning cached COM ports (age: {now - self._last_ports_update:.2f}s)")
            return self._ports_cache

        logger.debug(f"Refreshing COM ports list (cache timeout: {self.cache_timeout}s)")
        try:
            # Используем list comprehension для преобразования в ListPortInfo
            # serial.tools.list_ports.ListPortInfo уже является NamedTuple-подобным
            raw_ports = serial.tools.list_ports.comports()
            # Явно преобразуем в наш NamedTuple ListPortInfo для единообразия
            # и обработки возможных отсутствующих полей
            self._ports_cache = [
                ListPortInfo(
                    device=p.device,
                    name=p.name,
                    description=p.description,
                    hwid=p.hwid,
                    vid=p.vid,
                    pid=p.pid,
                    serial_number=p.serial_number,
                    location=p.location,
                    manufacturer=p.manufacturer,
                    product=p.product,
                    interface=p.interface,
                ) for p in raw_ports
            ]
            self._last_ports_update = now
            logger.info(f"Found {len(self._ports_cache)} COM ports: {[p.device for p in self._ports_cache]}")
            return self._ports_cache
        except Exception as e: # Более общая обработка ошибок
            logger.error(f"Error getting COM port list: {e}", exc_info=True)
            self._ports_cache = [] # Сбрасываем кэш при ошибке
            self._last_ports_update = 0
            return []

    # --- Методы для обнаружения Bluetooth устройств (асинхронные) ---

    def _get_bt_controller(self) -> BluetoothDeviceController:
        """Создает или возвращает существующий экземпляр BluetoothDeviceController."""
        if self._bt_controller is None:
            logger.debug("Creating BluetoothDeviceController instance.")
            self._bt_controller = BluetoothDeviceController(self.config)
        return self._bt_controller

    async def discover_bluetooth_devices(self, refresh: bool = False) -> List[DeviceInfo]:
        """
        Асинхронно обнаруживает Bluetooth-устройства, используя BluetoothDeviceController.
        Использует кэширование.

        Args:
            refresh: Принудительно обновить список устройств, игнорируя кэш.

        Returns:
            Список объектов DeviceInfo.
        """
        logger.debug(f"Discovering Bluetooth devices (refresh={refresh})...")
        now = time.monotonic()
        if (
            not refresh
            and self._bt_devices_cache is not None
            and (now - self._last_bt_update) < self.cache_timeout
        ):
            logger.debug(f"Returning cached Bluetooth devices (age: {now - self._last_bt_update:.2f}s)")
            return self._bt_devices_cache

        logger.debug(f"Refreshing Bluetooth devices list (cache timeout: {self.cache_timeout}s)")
        try:
            bt_controller = self._get_bt_controller()
            # Используем метод из BluetoothDeviceController для обнаружения
            # Этот метод уже включает сопоставление с COM-портами
            devices = await bt_controller.discover_devices()

            self._bt_devices_cache = devices
            self._last_bt_update = now
            logger.info(f"Found {len(self._bt_devices_cache)} valid Bluetooth devices.")
            return self._bt_devices_cache
        except Exception as e:
            logger.error(f"Error discovering Bluetooth devices: {e}", exc_info=True)
            self._bt_devices_cache = [] # Сбрасываем кэш при ошибке
            self._last_bt_update = 0
            return []

    # --- Вспомогательные методы (остаются или дорабатываются) ---

    def filter_bluetooth_ports(self, ports: List[ListPortInfo]) -> List[ListPortInfo]:
        """
        Фильтрует список COM-портов, оставляя только те, которые,
        вероятно, связаны с Bluetooth.
        (Этот метод может быть менее надежным, чем discover_bluetooth_devices)
        """
        logger.debug("Filtering COM ports for potential Bluetooth devices...")
        # Проверяем наличие описания перед доступом к нему
        bt_ports = [
            port for port in ports
            if port.description and any(
                keyword in port.description.upper()
                for keyword in {"BLUETOOTH", "BTHENUM", "BLUETOOTH LINK"} # Добавлены возможные ключевые слова
            )
        ]
        logger.debug(f"Found {len(bt_ports)} potential Bluetooth COM ports.")
        return bt_ports

    def extract_mac_from_port(self, port: ListPortInfo) -> Optional[str]:
        """
        Извлекает MAC-адрес из HWID COM-порта, если он там присутствует.
        Формат MAC: XX:XX:XX:XX:XX:XX
        """
        if not port or not port.hwid:
            # logger.debug(f"Cannot extract MAC: No port or hwid provided.")
            return None

        # logger.debug(f"Attempting to extract MAC from hwid: {port.hwid}")
        # Ищем MAC вида &XXXXXXXXXXXX или _XXXXXXXXXXXX
        # Паттерн стал более общим, ищет 12 HEX символов после & или _
        match = re.search(r"[&_]([0-9A-F]{12})", port.hwid.upper())
        if match:
            mac_raw = match.group(1)
            # Форматируем MAC в стандартный вид XX:XX:XX:XX:XX:XX
            formatted_mac = ":".join(mac_raw[i:i+2] for i in range(0, 12, 2))
            logger.debug(f"Extracted MAC {formatted_mac} from {port.device}")
            return formatted_mac
        # else:
            # logger.debug(f"No standard MAC pattern found in hwid for {port.device}")

        # Дополнительная проверка для некоторых форматов, например, BTHENUM\{...}\XXXXXXXXXXXX_...
        match_bthenum = re.search(r"\\([0-9A-F]{12})_", port.hwid.upper())
        if match_bthenum:
            mac_raw = match_bthenum.group(1)
            formatted_mac = ":".join(mac_raw[i:i+2] for i in range(0, 12, 2))
            logger.debug(f"Extracted MAC {formatted_mac} from BTHENUM format in {port.device}")
            return formatted_mac

        return None

    # --- Опционально: Метод для объединения информации ---
    async def discover_all_devices(self, refresh_com: bool = False, refresh_bt: bool = False) -> Dict[str, Any]:
        """
        Обнаруживает все устройства: COM-порты и Bluetooth.
        Возвращает словарь с ключами 'serial' и 'bluetooth'.

        Args:
            refresh_com: Принудительно обновить список COM-портов.
            refresh_bt: Принудительно обновить список Bluetooth-устройств.

        Returns:
            Словарь {'serial': List[ListPortInfo], 'bluetooth': List[DeviceInfo]}
        """
        logger.info(f"Discovering all devices (refresh_com={refresh_com}, refresh_bt={refresh_bt})...")
        # Запускаем обе задачи параллельно
        com_task = asyncio.to_thread(self.get_com_ports, refresh=refresh_com)
        bt_task = self.discover_bluetooth_devices(refresh=refresh_bt)

        com_ports, bt_devices = await asyncio.gather(com_task, bt_task, return_exceptions=True)

        results = {}
        if isinstance(com_ports, Exception):
            logger.error(f"Failed to get COM ports during combined discovery: {com_ports}")
            results['serial'] = []
        else:
            results['serial'] = com_ports

        if isinstance(bt_devices, Exception):
            logger.error(f"Failed to discover Bluetooth devices during combined discovery: {bt_devices}")
            results['bluetooth'] = []
        else:
            results['bluetooth'] = bt_devices

        logger.info(f"Combined discovery finished. Found {len(results['serial'])} COM ports and {len(results['bluetooth'])} Bluetooth devices.")
        return results

    def clear_cache(self):
        """Очищает кэш COM-портов и Bluetooth-устройств."""
        logger.info("Clearing device discovery cache.")
        self._ports_cache = None
        self._last_ports_update = 0
        self._bt_devices_cache = None
        self._last_bt_update = 0



class COMPortManager:
    
    def __init__(self, cache_timeout: float = DEFAULT_CACHE_TIMEOUT):
        self._ports_cache = None
        self._last_update = 0
        self.cache_timeout = cache_timeout  # seconds

    def get_com_ports(self, refresh=False):
        logger.debug(f"Getting COM ports (refresh={refresh})...")
        if (not refresh) and self._ports_cache and ((time.time() - self._last_update) < self.cache_timeout):
            logger.debug("Returning cached COM ports")
            return self._ports_cache

        logger.debug("Refreshing COM ports list")
        try:
            self._ports_cache: List[ListPortInfo] = list(serial.tools.list_ports.comports())
            self._last_update = time.time()
            
            logger.debug(f"Found {len(self._ports_cache)} ports: {[p.device for p in self._ports_cache]}")
            return self._ports_cache
        except serial.SerialException as e: # Улучшение: обрабатываем исключения
            logger.error(f"Error getting COM port list: {e}", exc_info=True)
            self._ports_cache = [] # Сбрасываем кэш при ошибке
            self._last_update = 0
            return []
        
    def filter_bluetooth_ports(self, ports: List[ListPortInfo]) -> List[ListPortInfo]:
        logger.warning("Filtering Bluetooth ports based on description keywords. This method might not be reliable on all systems.")
        return [
        port for port in ports
            if port.description and any( # Добавлена проверка на None
                    keyword in port.description.upper()
                    for keyword in {"BLUETOOTH", "BTHENUM"}
            )
        ]
    def extract_mac_from_port(self, port: Any) -> Optional[str]:
        logger.debug(f"Extracting MAC from port: {port}")
        
        if not port.hwid:
            logger.debug("No hwid available")
            return None
            
        logger.debug(f"Processing hwid: {port.hwid}")
        match = re.search(r"&([0-9A-F]{12})", port.hwid.upper())
        if match:
            mac_str = match.group(1)
            formatted_mac = ":".join(mac_str[i:i+2] for i in range(0, 12, 2))
            logger.debug(f"Formatted MAC: {formatted_mac}")
            return formatted_mac
            
        logger.debug("No MAC found in hwid")
        return None

class COMPortHandler:
    def __init__(self, connection: serial.Serial, response_mode: str = "full", inter_byte_timeout: float = 0.5):
        """
        Унифицированный обработчик COM-порта для Serial и Bluetooth соединений.

        Args:
            connection (serial.Serial): Открытое соединение с COM-портом.
            response_mode (str): Режим получения обратной связи:
                "full" – вернуть полный текст ответа,
                "ack" – не сохранять текст, а просто фиксировать факт получения.
            inter_byte_timeout (float): Время простоя между байтами, после которого считается, что ответ закончился.
        """
        self.connection = connection
        self.desired_port = connection.port
        self.response_mode = response_mode  # "full" или "ack"
        self.inter_byte_timeout = inter_byte_timeout
        self._buffer = asyncio.Queue()  # Очередь для накопленных ответов
        self._read_task: Optional[asyncio.Task] = None
        self._stop_event = asyncio.Event()
        self._write_lock = asyncio.Lock()
        self.com_port_manager = COMPortManager()

    async def start(self):
        """
        Запускает фоновый task для чтения из COM-порта.
        """
        if self._read_task is None:
            self._stop_event.clear()
            self._read_task = asyncio.create_task(self._read_loop())
            logger.debug("COMPortHandler reader started.")
        else:
            logger.debug("COMPortHandler reader already running.")

    async def stop(self):
        """
        Останавливает фоновый task чтения из COM-порта.
        """
        self._stop_event.set()
        if self._read_task:
            self._read_task.cancel()
            try:
                await self._read_task
            except asyncio.CancelledError:
                logger.debug("COMPortHandler reader cancelled.")
            self._read_task = None
            logger.debug("COMPortHandler reader stopped.")

    async def _read_loop(self):
        """Фоновое чтение порта с буферизацией строк."""
        loop = asyncio.get_running_loop()
        last_byte_time = loop.time()
        partial_data = ""
        try:
            while not self._stop_event.is_set():
                try:
                    bytes_to_read = self.connection.in_waiting or 1
                    data = await loop.run_in_executor(None, self.connection.read, bytes_to_read)
                except (serial.SerialException, PermissionError) as e:
                    logger.error("Error reading from COM port: %s", e, exc_info=True)
                    await self._handle_disconnection()
                    return
                except Exception as e:
                    logger.error("Error reading from COM port: %s", e, exc_info=True)
                    await asyncio.sleep(0.05)
                    continue

                if data:
                    try:
                        decoded = data.decode(errors="replace")
                    except Exception as err:
                        decoded = ""
                        logger.error("Error decoding data: %s", err, exc_info=True)
                    partial_data += decoded
                    last_byte_time = loop.time()

                    if self.response_mode == "full":
                        if "\n" in partial_data:
                            lines = partial_data.splitlines()
                            for line in lines:
                                if line.strip():
                                    await self._buffer.put(line.strip())
                            partial_data = ""
                    elif self.response_mode == "ack":
                        if partial_data.strip():
                            await self._buffer.put("ack")
                            partial_data = ""
                else:
                    if partial_data and (loop.time() - last_byte_time) >= self.inter_byte_timeout:
                        if self.response_mode == "full":
                            await self._buffer.put(partial_data.strip())
                        elif self.response_mode == "ack":
                            await self._buffer.put("ack")
                        partial_data = ""
                    await asyncio.sleep(0.01)
        except asyncio.CancelledError:
            logger.debug("COMPortHandler _read_loop cancelled.")
        except Exception as e:
            logger.error(f"Exception in COMPortHandler _read_loop: {e}", exc_info=True)
        finally:
            logger.debug("COMPortHandler _read_loop exiting.")
            self._read_task = None

    async def _handle_disconnection(self):
        """
        Обрабатывает ситуацию потери соединения:
        – закрывает текущий порт
        – запускает монитор для переподключения
        """
        logger.info("Handling disconnection for port %s...", self.desired_port)
        try:
            self.connection.close()
        except Exception as e:
            logger.error("Error closing connection: %s", e, exc_info=True)
        await asyncio.sleep(1)  # небольшая задержка перед повторной проверкой
        asyncio.create_task(self.monitor_connection(self.desired_port))

    async def monitor_connection(self, desired_port: str):
        """
        Фоновый монитор, который периодически проверяет доступность desired_port
        и переподключается при его наличии.
        """
        logger.info("Starting monitor for port %s", desired_port)
        while not self._stop_event.is_set():
            ports = self.com_port_manager.get_com_ports(refresh=True)
            available_ports = [port.device for port in ports]
            if desired_port in available_ports:
                try:
                    # Здесь можно подстроить параметры baudrate и timeout, используя старое соединение
                    new_connection = serial.Serial(
                        desired_port,
                        baudrate=self.connection.baudrate if hasattr(self.connection, "baudrate") else 115200,
                        timeout=self.connection.timeout if hasattr(self.connection, "timeout") else 0
                    )
                    logger.info("Successfully reconnected to port %s", desired_port)
                    self.connection = new_connection
                    await self.start()  # перезапускаем фоновый цикл чтения
                    return
                except Exception as e:
                    logger.error("Error reconnecting: %s", e, exc_info=True)
            await asyncio.sleep(2)  # ждём 2 секунды перед повторной попыткой

    async def send_command(self, command: str):
        """
        Отправляет команду через COM-порт, предварительно очищая входной/выходной буферы.
        """
        # try:
        #     self.connection.reset_input_buffer()
        #     self.connection.reset_output_buffer()
        # except Exception as e:
        #     logger.error(f"Error resetting COM port buffers: {e}")
        async with self._write_lock:
            # Дренируем ответный программный буфер (по желанию)
            while not self._buffer.empty():
                try:
                    self._buffer.get_nowait()
                except asyncio.QueueEmpty:
                    break

            full_command = f"{command}"
            try:
                self.connection.write(full_command.encode("utf-8", "ignore"))
                self.connection.flush()
                logger.debug(f"Sent command: {full_command.strip()}")
            except Exception as e:
                logger.error(f"Error writing to COM port: {e}", exc_info=True)


    async def get_response(self, timeout: float = 3.0) -> List[str]:
        """
        Извлекает накопленные ответы из очереди.

        Args:
            timeout (float): Максимальное время ожидания первого элемента ответа.

        Returns:
            List[str]: Список полученных ответов (линий или ack-токенов).
        """
        responses = []
        try:
            # Получаем первый ответ с заданным timeout
            first = await asyncio.wait_for(self._buffer.get(), timeout=timeout)
            responses.append(first)
            # Пробуем слить оставшиеся элементы, если они уже накоплены
            while True:
                try:
                    item = self._buffer.get_nowait()
                    responses.append(item)
                except asyncio.QueueEmpty:
                    break
        except asyncio.TimeoutError:
            logger.debug("No response received within timeout.")
        return responses
    

# Пример использования (если нужно запустить для проверки)
async def main_test(app_config):
    print("Initializing COMPortManager...")
    manager = COMPortManager(config=app_config, cache_timeout=10)

    print("\n--- Discovering COM Ports ---")
    com_ports = manager.get_com_ports()
    if com_ports:
        for port in com_ports:
            mac = manager.extract_mac_from_port(port)
            print(f"  {port.device}: {port.description} (MAC: {mac or 'N/A'})")
    else:
        print("  No COM ports found.")

    print("\n--- Discovering Bluetooth Devices (Async) ---")
    try:
        bt_devices = await manager.discover_bluetooth_devices()
        if bt_devices:
            for device in bt_devices:
                print(f"  {device.name} ({device.mac}) - COM: {device.com_port}, Paired: {device.is_paired}")
        else:
            print("  No Bluetooth devices found or discovery failed.")

        # Повторный вызов для проверки кэша
        print("\n--- Discovering Bluetooth Devices (Async - Cached) ---")
        start_time = time.monotonic()
        bt_devices_cached = await manager.discover_bluetooth_devices()
        end_time = time.monotonic()
        print(f"  Discovery from cache took {end_time - start_time:.4f} seconds.")
        if bt_devices_cached:
             for device in bt_devices_cached:
                print(f"  {device.name} ({device.mac}) - COM: {device.com_port}, Paired: {device.is_paired}")
        else:
            print("  No Bluetooth devices found.")


        print("\n--- Discovering All Devices (Combined - Async) ---")
        all_devices = await manager.discover_all_devices(refresh_com=True, refresh_bt=True)
        print("  Serial Ports:")
        if all_devices['serial']:
            for port in all_devices['serial']:
                print(f"    {port.device}: {port.description}")
        else:
            print("    None")
        print("  Bluetooth Devices:")
        if all_devices['bluetooth']:
            for device in all_devices['bluetooth']:
                 print(f"    {device.name} ({device.mac}) - COM: {device.com_port}, Paired: {device.is_paired}")
        else:
            print("    None")

    except Exception as e:
        print(f"\nAn error occurred during async operations: {e}")
        logging.exception("Error during main_test")
if __name__ == "__main__":
#     # Нужна заглушка для AppConfig
    from smeller.config.config import load_config, BluetoothConfig, SerialConfig
    logging.basicConfig(level=logging.DEBUG)

#     # Создаем минимальную конфигурацию для теста
#     # В реальном приложении она будет загружаться из файла
    test_config = AppConfig(
        serial=SerialConfig(port=None, baudrate=115200, timeout=2, response_mode="full"),
        bluetooth=BluetoothConfig(ping_interval=5, discovery_duration=8), # Увеличим время поиска для теста
        # ... другие секции конфига
    )
    print("Running COMPortManager test...")
    asyncio.run(main_test(test_config))
    print("\nTest finished.")
    