# smeller/config/config.py

from dataclasses import dataclass, field
from typing import Optional, List, Union, Dict, Any

@dataclass
class DeviceConfig:
    """
    Configuration for the NeuroAir device.
    """
    num_ports: int = 12 
    response_mode: Optional[str] = None
    command_timeout: Optional[float] = None
    
@dataclass
class BaseDeviceDefinition:
    """Базовое определение устройства для конфигурации."""
    id: str  # Уникальный идентификатор устройства внутри приложения (например, "smeller_com3", "bt_sensor_lab", "mqtt_device_1")
    name: Optional[str] = None  # Удобное для пользователя имя (опционально)
    enabled: bool = True  # Флаг, позволяющий временно отключить устройство в конфиге
    # Общие параметры устройства (можно оставить пустым, если используются глобальные)
    device_config: DeviceConfig = field(default_factory=DeviceConfig)

@dataclass
class SerialDeviceDefinition(BaseDeviceDefinition):
    """Определение устройства с серийным подключением."""
    connection_type: str = "serial"  # Явно указываем тип для парсинга
    port: Optional[str] = None
    baudrate: int = 115200  # Можно задать дефолтные значения
    timeout: float = 3.0
    command_terminator: str = "\n"
    # Можно добавить специфичные для Serial параметры из SerialConfig, если они не дублируются в DeviceConfig
    # Например, response_mode можно взять из device_config
    # response_mode: str = "full" # Пример, если нужно переопределить

@dataclass
class BluetoothDeviceDefinition(BaseDeviceDefinition):
    """Определение устройства с Bluetooth подключением."""
    connection_type: str = "bluetooth"
    mac_address: Optional[str] = None
    # Параметры для COM-порта, который создается для Bluetooth SPP
    # Могут наследоваться или дублироваться из SerialConfig/SerialDeviceDefinition
    baudrate: int = 115200
    timeout: float = 5.0 # BT может требовать большего таймаута
    ping_interval: float = 10.0 # Пример специфичного BT параметра
    discovery_duration: int = 8 # Пример

@dataclass
class MqttDeviceDefinition(BaseDeviceDefinition):
    """Определение устройства с MQTT подключением."""
    connection_type: str = "mqtt"
    chip_id: Optional[str] = None
    # Параметры брокера (host, port, user, pass) берутся из глобальной AppConfig.mqtt
    command_terminator: str = "\n" # Пример специфичного MQTT параметра
               
@dataclass
class SerialConfig:
    port: str = "COM22" # Значение по умолчанию
    baudrate: int = 115200
    timeout: float = 2.0
    response_mode: str = "full" # или "ack" – настройка в DeviceConfig
    command_terminator: str = "\n"

@dataclass
class BluetoothConfig(SerialConfig): # Наследуем общие параметры от SerialConfig
    mac_address: Optional[str] = None
    discovery_duration: int = 10
    ping_interval: int = 5
    
@dataclass
class MqttConfig: #  Новая конфигурация MQTT
    host: str = "mstuca1.ru"
    port: int = 1883
    username: Optional[str] = None
    password: Optional[str] = None
    subscribe_topic: str = "air/+/status"
    publish_topic: str = "air/{chip_id}/in"
    command_terminator: str = "\n" #  или "\r\n" в зависимости от устройства

@dataclass
class DatabaseConfig:
    dbname: str = "SL_aroma"
    user: str = "sl_adder"
    password: str = "95719574"
    host: str = "10.10.0.129"
    port: str = "5432"
    options: str = "-c client_encoding=utf-8"

@dataclass
class DynamicControlConfig:
    update_interval: float = 0.1
    default_cycle_time: int = 100

@dataclass
class GuiConfig:
    theme: str = "dark"
    # TODO: Добавить настройку цветов и размеров

@dataclass
class LoggingConfig:
    level: str = "DEBUG"
    file_path: str = "smeller.log"

@dataclass
class AppConfig: # Общая конфигурация приложения
    connection_type: str = "serial" # 'serial' или 'bluetooth'
    device: DeviceConfig = field(default_factory=DeviceConfig)
    serial: SerialConfig = field(default_factory=SerialConfig)
    bluetooth: BluetoothConfig = field(default_factory=BluetoothConfig)
    
    defined_devices: List[Union[SerialDeviceDefinition, BluetoothDeviceDefinition, MqttDeviceDefinition]] = field(default_factory=list)

    mqtt: MqttConfig = field(default_factory=MqttConfig) 
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    dynamic_control: DynamicControlConfig = field(default_factory=DynamicControlConfig)
    gui: GuiConfig = field(default_factory=GuiConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    comport_cache_timeout: float = 5.0
    interpolation_points: int = 100
    
    
    