# smeller/utils/comport_manager.py

import asyncio
import re, time
import logging
from typing import List, Optional, Tuple, NamedTuple, Any
import serial
import bluetooth as bt
import serial.tools.list_ports

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
        self._read_task = None
        self._stop_event = asyncio.Event()
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
        """
        Фоновый цикл для непрерывного чтения из COM-порта.
        """
        loop = asyncio.get_running_loop()
        last_byte_time = loop.time()
        partial_data = ""
        try:
            while not self._stop_event.is_set():
                try:
                    # Читаем доступные байты (или один, если ничего не доступно)
                    bytes_to_read = self.connection.in_waiting or 1
                    data = await loop.run_in_executor(None, self.connection.read, bytes_to_read)
                except (serial.SerialException, PermissionError) as e:
                    logger.error("PermissionError reading from COM port: %s", e, exc_info=True)
                    await self._handle_disconnection()
                    return  # завершаем цикл чтения
                except Exception as e:
                    logger.error("Error reading from COM port: %s", e, exc_info=True)
                    await asyncio.sleep(0.1)
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
                        # Если накоплен символ перевода строки, обрабатываем накопленный ответ
                        if "\n" in partial_data:
                            lines = partial_data.splitlines()
                            for line in lines:
                                if line.strip():
                                    await self._buffer.put(line.strip())
                            partial_data = ""
                    elif self.response_mode == "ack":
                        # Если режим "ack", как только получили хоть что-то – сразу фиксируем факт получения
                        if partial_data.strip():
                            await self._buffer.put("ack")
                            partial_data = ""
                else:
                    # Если данных нет, проверяем, не истёк ли inter_byte_timeout для уже накопленных данных
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
            logger.error(f"Exception in COMPortHandler _read_loop: {e}")
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
        try:
            self.connection.reset_input_buffer()
            self.connection.reset_output_buffer()
        except Exception as e:
            logger.error(f"Error resetting COM port buffers: {e}")

        # Здесь можно добавить terminator, если он не включён в команду
        full_command = f"{command}"
        try:
            self.connection.write(full_command.encode())
            self.connection.flush()
            logger.debug(f"Sent command: {full_command.strip()}")
        except Exception as e:
            logger.error(f"Error writing to COM port: {e}")

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