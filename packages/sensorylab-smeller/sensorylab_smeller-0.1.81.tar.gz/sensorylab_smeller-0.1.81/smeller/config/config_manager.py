# Содержимое файла: smeller/config/config_manager.py
import json
import logging
from pathlib import Path
from typing import Optional, List, Union
from dataclasses import asdict 
from smeller.config.config import (
                                    AppConfig, 
                                    DeviceConfig, 
                                    SerialConfig, 
                                    BluetoothConfig, 
                                    MqttConfig, # Добавляем MqttConfig
                                    
                                    DatabaseConfig, 
                                    GuiConfig, 
                                    LoggingConfig, 
                                    DynamicControlConfig, # Убедись, что путь к AppConfig правильный
                                    BaseDeviceDefinition,
                                    SerialDeviceDefinition,
                                    BluetoothDeviceDefinition,
                                    MqttDeviceDefinition
)
from smeller.database.db_manager import DatabaseManager #
from smeller.dynamic_control.dynamic_block_controller import DynamicBlockController
from smeller.controllers.device_controller import DeviceController
from smeller.communication.bluetooth_com import BluetoothCommunication
from smeller.communication.serial_com import SerialCommunication

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, # <--- Устанавливаем уровень DEBUG
                        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

DEFAULT_CONFIG_FILE = "config.json"  # Имя файла конфигурации по умолчанию

class ConfigManager:


    def __init__(self, config_dir: str = "smeller/config"):
        self.config_dir = Path(config_dir)
        self.config_file_path = self.config_dir / DEFAULT_CONFIG_FILE
        self._config: AppConfig = self.reset_to_defaults() # Инициализация конфигурацией по умолчанию

        self.db_manager: Optional[DatabaseManager] = None  # Явное объявление и инициализация None
        self.dynamic_block_controller: Optional[DynamicBlockController] = None # Явное объявление и инициализация None

    def load_config(self) -> AppConfig:
        """
        Loads configuration from JSON file.
        """
        try:
            with open(self.config_file_path, "r") as f:
                config_dict = json.load(f)
        except FileNotFoundError:
            logger.warning(f"Config file not found at {self.config_file_path}. Loading default settings.")
            return self.reset_to_defaults()  # Используем дефолтные настройки
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON from {self.config_file_path}. Loading default settings.")
            return self.reset_to_defaults()
        except Exception as e:
            logger.error(f"Unexpected error loading config: {e}. Loading default settings.", exc_info=True)
            return self.reset_to_defaults()

        try:
            mqtt_config_data = config_dict.get("mqtt") # Может быть None
            #  Десериализация JSON в dataclass объекты:
            device_config_data = config_dict.get("device", {})
            serial_config_data = config_dict.get("serial", {})
            bluetooth_config_data = config_dict.get("bluetooth", {})
            database_config_data = config_dict.get("database", {})
            gui_config_data = config_dict.get("gui", {})
            logging_config_data = config_dict.get("logging", {})
            dynamic_control_config_data = config_dict.get("dynamic_control", {})

            mqtt_config = MqttConfig(**mqtt_config_data) if mqtt_config_data else None
            device_config = DeviceConfig(**device_config_data) #  Создаем DeviceConfig
            serial_config = SerialConfig(**serial_config_data) #  Создаем SerialConfig
            # BluetoothConfig наследуется от SerialConfig, поэтому инициализируем так:
            bluetooth_config = BluetoothConfig(**bluetooth_config_data) #  Создаем BluetoothConfig
            database_config = DatabaseConfig(**database_config_data) #  Создаем DatabaseConfig
            gui_config = GuiConfig(**gui_config_data) #  Создаем GuiConfig
            logging_config = LoggingConfig(**logging_config_data) #  Создаем LoggingConfig
            dynamic_control_config = DynamicControlConfig(**dynamic_control_config_data)
            
            # --- Десериализация списка defined_devices ---
            defined_devices_list: List[Union[SerialDeviceDefinition, BluetoothDeviceDefinition, MqttDeviceDefinition]] = []
            raw_devices_list = config_dict.get("defined_devices", [])

            if not isinstance(raw_devices_list, list):
                 logger.warning(f"'defined_devices' in config is not a list. Skipping device definitions.")
                 raw_devices_list = [] # Используем пустой список, если формат неверный

            for i, device_data in enumerate(raw_devices_list):
                if not isinstance(device_data, dict):
                    logger.warning(f"Device definition at index {i} is not a dictionary. Skipping.")
                    continue

                connection_type = device_data.get("connection_type")
                device_id = device_data.get("id") # Получаем id

                if not connection_type:
                    logger.warning(f"Device definition at index {i} (id: {device_id or 'N/A'}) missing 'connection_type'. Skipping.")
                    continue
                if not device_id:
                    logger.warning(f"Device definition at index {i} missing 'id'. Skipping.")
                    continue

                # Десериализуем вложенный device_config
                device_config_data = device_data.get("device_config", {})
                try:
                    # Если device_config_data пустой, создастся дефолтный DeviceConfig
                    specific_device_config = DeviceConfig(**device_config_data)
                except TypeError as e:
                     logger.error(f"Error creating DeviceConfig for device '{device_id}': {e}. Using default DeviceConfig.", exc_info=True)
                     specific_device_config = DeviceConfig() # Используем дефолтный при ошибке

                # Удаляем уже обработанные ключи перед передачей в **kwargs
                device_args = device_data.copy()
                device_args.pop("connection_type", None) # Удаляем, т.к. не нужен в конструкторе DeviceDefinition
                device_args.pop("device_config", None) # Удаляем, т.к. передаем объект specific_device_config

                try:
                    device_definition: Optional[BaseDeviceDefinition] = None
                    if connection_type == "serial":
                        device_definition = SerialDeviceDefinition(
                            device_config=specific_device_config,
                            **device_args
                        )
                    elif connection_type == "bluetooth":
                        device_definition = BluetoothDeviceDefinition(
                            device_config=specific_device_config,
                            **device_args
                        )
                    elif connection_type == "mqtt":
                        device_definition = MqttDeviceDefinition(
                            device_config=specific_device_config,
                            **device_args
                        )
                    else:
                        logger.warning(f"Unknown connection_type '{connection_type}' for device '{device_id}'. Skipping.")
                        continue # Пропускаем неизвестный тип

                    defined_devices_list.append(device_definition)
                    logger.debug(f"Successfully parsed device definition for id: {device_id}, type: {connection_type}")

                except TypeError as e:
                     logger.error(f"TypeError creating device definition for device '{device_id}' (type: {connection_type}): {e}. Check config fields.", exc_info=True)
                except Exception as e:
                     logger.error(f"Unexpected error creating device definition for device '{device_id}': {e}", exc_info=True)


            app_config = AppConfig( #  Создаем AppConfig, передавая созданные dataclass-объекты
                defined_devices=defined_devices_list,
                connection_type=config_dict.get("connection_type", "serial"), #  Значение по умолчанию, если отсутствует в JSON
                device = device_config,
                serial=serial_config,
                bluetooth=bluetooth_config,
                database=database_config,
                gui=gui_config,
                logging=logging_config,
                dynamic_control=dynamic_control_config,
                comport_cache_timeout=config_dict.get("comport_cache_timeout", 5.0), #  Значение по умолчанию, если отсутствует
                interpolation_points=config_dict.get("interpolation_points", 100) #  Значение по умолчанию
            )
            logger.info("Configuration loaded successfully from JSON file.")
            return app_config

        except TypeError as e: #  Ловим ошибки TypeError при инициализации dataclass
            logger.error(f"TypeError during config deserialization: {e}. Check config file structure and types.", exc_info=True)
            return self.reset_to_defaults() #  Возврат к дефолтным настройкам при ошибке десериализации
        except Exception as e: #  Ловим любые другие ошибки
            logger.error(f"Unexpected error during config loading: {e}. Loading default settings.", exc_info=True)
            return self.reset_to_defaults() 
                
    def save_config(self, config: AppConfig, filepath: Optional[str] = None) -> None:
        """Сохраняет конфигурацию в JSON файл, используя dataclasses.asdict."""
        config_path = Path(filepath) if filepath else self.config_file_path
        try:
            self.config_dir.mkdir(parents=True, exist_ok=True) # Ensure directory exists
            # Используем asdict для рекурсивного преобразования dataclass в словарь
            config_dict = asdict(config)
            # Убираем None значения из словаря перед сохранением (опционально, для чистоты JSON)
            config_dict_cleaned = {k: v for k, v in config_dict.items() if v is not None}

            with open(config_path, 'w', encoding="utf-8") as f: # Добавил encoding
                json.dump(config_dict_cleaned, f, indent=4, ensure_ascii=False) # ensure_ascii=False для кириллицы
                logger.info(f"Configuration saved to: {config_path}")
        except TypeError as e:
             logger.error(f"TypeError saving configuration (possibly non-serializable data): {e}", exc_info=True)
        except Exception as e:
            logger.error(f"Failed to save configuration to {config_path}: {e}", exc_info=True)


    def get_config(self) -> AppConfig:
        """Возвращает текущую конфигурацию."""
        return self._config

    def apply_config(self, config: AppConfig) -> None:
        """Применяет переданную конфигурацию к глобальным компонентам приложения."""
        logger.info("Applying configuration to global components...")
        self._config = config # Обновляем текущую конфигурацию

        # --- Применяем параметры к глобальным компонентам ---

        # Применяем параметры DynamicBlockController
        if self.dynamic_block_controller: # Проверяем, существует ли атрибут
            try: # Добавляем try-except на случай, если атрибут не установлен
                 self.dynamic_block_controller.update_interval = config.dynamic_control.update_interval
                 logger.debug("DynamicBlockController configuration applied.")
            except AttributeError as e:
                 logger.warning(f"Could not apply config to DynamicBlockController: {e}")

        # Применяем параметры DatabaseManager
        if self.db_manager:
            logger.info("Re-initializing DatabaseManager with new configuration...")
            try:
                self.db_manager.db_params = { # Обновляем параметры подключения
                    'dbname': config.database.dbname,
                    'user': config.database.user,
                    'password': config.database.password,
                    'host': config.database.host,
                    'port': config.database.port,
                    'options': config.database.options
                }
                self.db_manager.engine = None # Сбрасываем старый engine
                self.db_manager.create_engine() # Пересоздаем engine с новыми параметрами
                logger.info("DatabaseManager re-initialized with new configuration.")
            except Exception as e:
                logger.error(f"Error re-initializing DatabaseManager: {e}", exc_info=True)
        else:
            logger.warning("DatabaseManager not yet initialized, cannot apply database config.")

        logger.info("Global component configuration applied.")

    def reset_to_defaults(self) -> AppConfig:
        """Возвращает конфигурацию по умолчанию с пустым списком устройств."""
        default_config = AppConfig(defined_devices=[]) # Создаем с пустым списком
        logger.info("Configuration reset to defaults (no defined devices).")
        return default_config