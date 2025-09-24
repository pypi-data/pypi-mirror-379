# smeller/communication/bluetooth_com.py
import asyncio, re, time, subprocess
import logging
from typing import List, Optional, NamedTuple, Tuple, Any
import serial
from smeller.communication.base import CommunicationInterface
from smeller.config.config import AppConfig
from smeller.utils.comport_manager import COMPortManager, COMPortHandler  # Убедись, что путь правильный
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
COMMAND_TERMINATOR = "\n"
DEVICE_NAME_PATTERN = re.compile(r"^[0-9A-Za-z]{3}_[0-9A-F]{12}$")
MAC_ADDRESS_PATTERN = re.compile(r"([0-9A-F]{2}[:]){5}([0-9A-F]{2})")

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

class DeviceInfo(NamedTuple):
    mac: str
    name: str
    com_port: Optional[str]
    is_paired: bool
    
class BluetoothDeviceController:
    def __init__(self, config: AppConfig):
        self.config = config
        self.baudrate = config.serial.baudrate
        self.ping_interval = config.bluetooth.ping_interval
        self.discovery_duration = config.bluetooth.discovery_duration
        self.connection: Optional[serial.Serial] = None
        self.port_handler: Optional[COMPortHandler] = None
        self._running = False
        self.port_manager = COMPortManager()
        self._ping_task: Optional[asyncio.Task] = None

    # Модифицируем метод discover_devices
    async def discover_devices(self) -> List[DeviceInfo]:
        """Обнаруживает и возвращает список доступных Bluetooth устройств."""
        try:
            logger.debug("Starting Bluetooth discovery...")
            logger.debug(f"Calling bt.discover_devices() with parameters: "
                        f"duration={self.discovery_duration}, lookup_names=True, flush_cache=True, lookup_class=True")
            
            start_time = time.time()
            nearby_devices = bt.discover_devices(
                duration=self.discovery_duration,
                lookup_names=True,
                flush_cache=True,
                lookup_class=True
            )
            elapsed = time.time() - start_time
            
            logger.debug(f"Discovery completed in {elapsed:.2f} seconds")
            logger.debug(f"Raw discovered devices: {nearby_devices}")
            
            return await self._process_discovered_devices(nearby_devices)
        except Exception as e:
            logger.error(f"Bluetooth discovery failed: {str(e)}", exc_info=True)
            return []


    # Обновим _process_discovered_devices
    async def _process_discovered_devices(self, devices: List[Tuple[str, str, int]]) -> List[DeviceInfo]:
        """Обрабатывает обнаруженные устройства и сопоставляет с COM-портами."""
        logger.debug("Starting processing of discovered devices")
        
        com_ports = self.port_manager.get_com_ports()
        logger.debug(f"All COM ports: {[p.device for p in com_ports]}")
        
        bt_ports = self.port_manager.filter_bluetooth_ports(com_ports)
        logger.debug(f"Filtered Bluetooth COM ports: {[p.device for p in bt_ports]}")
        
        paired_macs = self._get_paired_devices()
        logger.debug(f"Paired MAC addresses: {paired_macs}")
        
        valid_devices = []
        for index, (mac, name, _) in enumerate(devices):
            logger.debug(f"Processing device #{index + 1}: MAC={mac}, Name={name}")
            
            if not name:
                logger.debug("Skipping device without name")
                continue
                
            if not self._validate_device_name(name):
                logger.debug(f"Invalid device name format: {name}")
                continue

            com_port = self._find_matching_com_port(mac, bt_ports)
            port_info = com_port.device if com_port else "None"
            logger.debug(f"COM port match: {port_info}")
            
            is_paired = mac in paired_macs
            logger.debug(f"Paired status: {is_paired}")
            
            valid_devices.append(
                DeviceInfo(mac, name, port_info, is_paired)
            )
        
        logger.debug(f"Total valid devices found: {len(valid_devices)}")
        return valid_devices

    def _validate_device_name(self, name: str) -> bool:
        """Проверяет валидность имени устройства."""
        return bool(DEVICE_NAME_PATTERN.match(name)) if name else False

    def _find_matching_com_port(self, mac: str, ports: List[Any]):
        """Находит COM-порт, соответствующий MAC-адресу."""
        for port in ports:
            port_mac = self.port_manager.extract_mac_from_port(port)
            if port_mac and port_mac == mac:
                return port
        return None


    # Добавим логирование в _get_paired_devices
    def _get_paired_devices(self) -> set:
        """Возвращает MAC-адреса сопряженных устройств."""
        logger.warning("Getting paired devices via PowerShell. This method is Windows-specific.")
        
        try:
            result = subprocess.check_output(
                ["powershell", "Get-PnpDevice -Class Bluetooth | Select-Object DeviceID"],
                stderr=subprocess.PIPE,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            logger.debug(f"PowerShell output:\n{result}")
            
            macs = set()
            for match in MAC_ADDRESS_PATTERN.finditer(result):
                mac = match.group(0).upper()
                logger.debug(f"Found MAC in output: {mac}")
                macs.add(mac)
                
            logger.debug(f"Total paired MACs found: {len(macs)}")
            return macs
            
        except subprocess.CalledProcessError as e:
            logger.error(f"PowerShell command failed! Exit code: {e.returncode}")
            logger.error(f"Error output: {e.stderr}")
        except Exception as e:
            logger.error(f"Error getting paired devices: {str(e)}", exc_info=True)
            
        return set()

    async def connect(self, device_info: Optional[DeviceInfo] = None, com_port_name: Optional[str] = None) -> bool:
        """
        Устанавливает соединение с выбранным устройством.
        Добавлена возможность подключения напрямую по COM-порту.

        Args:
        device_info: Информация об устройстве (если подключаемся через Bluetooth).
        com_port_name: Имя COM-порта (если подключаемся напрямую).

        Returns:
        True, если соединение установлено успешно, иначе False.
        """
        if not device_info.com_port:
            logger.warning("Both device_info and com_port_name provided. Using com_port_name for direct connection.")
            device_info = None # Если указаны оба параметра - подключаемся напрямую
        port_to_connect = com_port_name or (device_info.com_port if device_info else None)
        if not port_to_connect:
            logger.error("No COM port available for this device")
            return False
        
        try:
            self.connection = serial.Serial(
                port=device_info.com_port,
                baudrate=self.baudrate,
                timeout=2
            )
            self._running = True
            
            self.port_handler = COMPortHandler(
                connection=self.connection,
                response_mode=self.config.serial.response_mode,  # или "ack" – настройка в DeviceConfig
                inter_byte_timeout=self.config.serial.timeout / 2  # примерное значение
            )
            await self.port_handler.start()
            # Запуск фонового пинга
            self._ping_task = asyncio.create_task(self._start_ping())
            logger.info(f"Connected to {port_to_connect} ({device_info.name if device_info else 'direct connection'})")
            return True

        except serial.SerialException as e:
            logger.error(f"Connection error: {e}")
            return False

    async def disconnect(self):
        """Разрывает соединение с устройством."""
        self._running = False
        if self._ping_task:
            self._ping_task.cancel()
            try: # Добавлено ожидание завершения задачи
                await self._ping_task
            except asyncio.CancelledError:
                pass
        if self.connection and self.connection.is_open:
            self.connection.close()
            logger.info("Connection closed")

    async def _start_ping(self):
        """Запускает периодическую отправку ping-команд."""
        while self._running:
            try:
                response = await self.send_command("h")
                logger.debug(f"Ping response: {response}")
                await asyncio.sleep(self.ping_interval)
            except asyncio.CancelledError: # Обрабатываем отмену задачи
                logger.debug("Ping task cancelled")
                break
            except Exception as e:
                logger.error(f"Ping failed: {e}", exc_info=True)
                break

    async def send_command(self, command: str) -> Optional[List[str]]:
        """
        Отправляет команду через COM-порт и возвращает накопленный ответ.
        Логика делегирована COMPortHandler, который читает данные в фоне.
        """
        if not self.connection or not self.connection.is_open or not self.port_handler:
            logger.warning("No active connection")
            return None
        try:
            full_command = f"{command.strip()}{COMMAND_TERMINATOR}"
            await self.port_handler.send_command(full_command)
            response = await self.port_handler.get_response(timeout=self.config.timeout)
            return response
        except Exception as e:
            logger.error(f"Command failed: {e}")
            return None


class BluetoothCommunication(CommunicationInterface):


    def __init__(self, config: AppConfig, port_manager: Optional[COMPortManager] = None):
        self.config = config
        self.bt_controller = BluetoothDeviceController(config)
        self.connection: Optional[serial.Serial] = None
        self._running = False #Добавить
        if port_manager is None:
            self.port_manager = COMPortManager()
        else:
            self.port_manager = port_manager
    async def connect(self, mac_address: Optional[str] = None, **kwargs) -> bool:
        """
        Connects to the device via Bluetooth.

        :param mac_address: Optional MAC address. If not provided, discovery will be performed.
        :param kwargs:
        :return: True if connection was successful, False otherwise.
        """
        try:
            if mac_address:
                # Попытка подключиться напрямую по MAC-адресу
                logger.debug(f"Attempting direct connection to {mac_address}")
                devices = await self.bt_controller.discover_devices()
                device_info = next((d for d in devices if d.mac == mac_address), None)

                if not device_info:
                    logger.error(f"Device with MAC address {mac_address} not found.")
                    return False
                if not device_info.com_port:
                    logger.error(f'No COM Port {device_info}')
                    return False
                if await self.bt_controller.connect(device_info):
                    self.connection = self.bt_controller.connection
                    return True
                else:
                    return False
            else:
                # Обнаружение устройств
                logger.debug("Performing Bluetooth device discovery...")
                devices = await self.bt_controller.discover_devices()
                if not devices:
                    logger.error("No Bluetooth devices found.")
                    return False

                # Попытка подключиться к первому найденному устройству с COM-портом
                for device in devices:
                    if device.com_port:
                        if await self.bt_controller.connect(device):
                            self.connection = self.bt_controller.connection #Сохраняем
                            return True #Подключение в контроллере
                        else:
                            logger.warning(f"Failed to connect to {device.name} ({device.mac})")
                    else:
                        logger.warning(f"No COM port for {device.com_port}")
                logger.error("No devices with COM ports found during discovery.")
                return False

        except Exception as e:
            logger.error(f"Bluetooth connection error: {e}")
            return False
        
    async def disconnect(self) -> None:
        """Disconnects from the device."""
        await self.bt_controller.disconnect()
        self.connection = None #Очищаем
        self._running = False

    async def send_command(self, command_str: str) -> Optional[List[str]]:
        """
        Отправляет команду через Bluetooth.
        Делегирует отправку команде контроллеру.
        """
        if not self.connection or not self.connection.is_open:
            logger.warning("No active Bluetooth connection (or serial connection via Bluetooth).")
            return None
        try:
            return await self.bt_controller.send_command(command_str)
        except Exception as e:
            logger.error(f"Command failed (Bluetooth): {e}")
            return None

    async def read_response(self, timeout: float = 3.0, inter_byte_timeout: float = 0.5) -> List[str]:
        """
        Читает ответ, делегируя операцию COMPortHandler’у.
        """
        if not self.connection or not self.connection.is_open or not self.bt_controller.port_handler:
            logger.warning("No active Bluetooth connection (or serial connection via Bluetooth).")
            return []
        return await self.bt_controller.port_handler.get_response(timeout=timeout)