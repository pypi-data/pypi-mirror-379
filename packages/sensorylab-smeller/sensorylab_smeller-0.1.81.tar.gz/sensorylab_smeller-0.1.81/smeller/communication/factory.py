# smeller/communication/factory.py
# Содержимое файла: factory.py
import logging
from typing import Optional, Dict, Any # Добавлен Dict, Any
from smeller.communication.base import CommunicationInterface
from smeller.communication.serial_com import SerialCommunication
from smeller.communication.bluetooth_com import BluetoothCommunication
from smeller.communication.mqtt_com import MqttCommunication
from smeller.config.config import AppConfig
from smeller.utils.comport_manager import COMPortManager

logger = logging.getLogger(__name__)

# Словарь для хранения созданных экземпляров (для синглтонов)
# Ключ - тип соединения ("mqtt"), Значение - экземпляр CommunicationInterface
_communication_instances: Dict[str, CommunicationInterface] = {}


def create_communication(
    config: AppConfig,
    connection_type: str,
    port_manager: Optional[COMPortManager] = None,
    # Добавляем **kwargs для гибкости, если понадобится передать доп. параметры
    **kwargs: Any
) -> CommunicationInterface:
    """
    Фабрика для создания экземпляров интерфейса связи.

    Реализует паттерн Singleton для MQTT соединения.

    Args:
        config: Конфигурация приложения.
        connection_type: Тип соединения ('serial', 'bluetooth', 'mqtt').
        port_manager: Менеджер COM-портов (необходим для serial и bluetooth).
        **kwargs: Дополнительные аргументы (пока не используются).

    Returns:
        Экземпляр, реализующий CommunicationInterface.

    Raises:
        ValueError: Если указан неверный тип соединения.
        TypeError: Если port_manager не передан для serial или bluetooth.
    """
    logger.debug(f"Creating communication interface for type: {connection_type}")

    if connection_type == "serial":
        #if port_manager is None:
        #    raise TypeError("COMPortManager is required for serial connection type")
        # Для serial создаем новый экземпляр каждый раз
        return SerialCommunication(config, port_manager)
    elif connection_type == "bluetooth":
        #if port_manager is None:
        #    raise TypeError("COMPortManager is required for bluetooth connection type")
        # Для bluetooth создаем новый экземпляр каждый раз
        return BluetoothCommunication(config, port_manager)
    elif connection_type == "mqtt":
        # --- Начало изменений для Singleton ---
        instance = _communication_instances.get(connection_type)
        if instance is None:
            logger.info("Creating new MQTT Communication singleton instance.")
            # Проверяем наличие MQTT конфигурации
            #if not config.mqtt or not config.mqtt.host:
            #     raise ValueError("MQTT configuration (host) is missing in AppConfig for MQTT connection.")
            instance = MqttCommunication(config)
            _communication_instances[connection_type] = instance
        else:
            logger.debug("Returning existing MQTT Communication singleton instance.")
        # Проверяем, что возвращаемый экземпляр соответствует интерфейсу
        #if not isinstance(instance, MqttCommunication):
             # Эта ситуация не должна возникать при правильной логике, но добавим проверку
             #raise TypeError(f"Cached instance for 'mqtt' is not MqttCommunication: {type(instance)}")
        return instance
        # --- Конец изменений для Singleton ---
    else:
        raise ValueError(f"Invalid connection type specified: {connection_type}")

# Дополнительно: функция для сброса синглтонов (может понадобиться при перезагрузке)
def reset_communication_singletons():
    """Сбрасывает кэш синглтон экземпляров (полезно для тестов или перезагрузки)."""
    logger.info("Resetting communication singletons cache.")
    _communication_instances.clear()