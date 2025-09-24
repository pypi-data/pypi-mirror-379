# smeller/communication/serial_com.py
import asyncio
import logging
from typing import List, Optional
import sys
from pathlib import Path

# Добавляем директорию, содержащую neuroairAPI, в sys.path
project_root = Path(__file__).resolve().parents[1]  # Поднимаемся на два уровня вверх
sys.path.append(str(project_root))
project_root = Path(__file__).resolve().parents[3]  # Поднимаемся на два уровня вверх
sys.path.append(str(project_root))

import serial
import serial.tools.list_ports

from smeller.communication.base import CommunicationInterface
from smeller.config.config import AppConfig  # Исправленный импорт
from smeller.utils.comport_manager import COMPortManager, COMPortHandler  # Убедись, что путь правильный

logger = logging.getLogger(__name__)

class SerialCommunication(CommunicationInterface):
    
    def __init__(self, config: AppConfig, port_manager=None):

        self.config = config
        self.connection: Optional[serial.Serial] = None
        self._running = False
        self.port_handler: Optional[COMPortHandler] = None
        self.port_manager = port_manager if port_manager is not None else COMPortManager()
        
    async def connect(self, com_port: Optional[str] = None, **kwargs) -> bool:
        """
        Establishes a serial connection.
                :param com_port:
        """
        com_port = kwargs.get('port')
        baudrate = kwargs.get('baudrate')
        # Получаем таймаут из kwargs или из дефолтного config.serial
        timeout = kwargs.get('timeout', self.config.serial.timeout)
        # Получаем режим ответа из kwargs или из дефолтного config.serial
        response_mode = kwargs.get('response_mode', self.config.serial.response_mode)
        # Получаем inter_byte_timeout из kwargs или рассчитываем из timeout
        inter_byte_timeout = kwargs.get('inter_byte_timeout', timeout / 2)

        if not com_port:
            logger.error("Connection error: 'port' not specified in connection arguments.")
            return False
        if not baudrate:
            logger.error(f"Connection error for port {com_port}: 'baudrate' not specified.")
            return False

        try:
            self.connection = serial.Serial(
                port=com_port,
                baudrate=self.config.serial.baudrate,
                timeout=self.config.serial.timeout
            )
            self._running = True
            
            self.port_handler = COMPortHandler(
                connection=self.connection,
                response_mode=self.config.serial.response_mode,  # или "ack" – настройка в DeviceConfig
                inter_byte_timeout=self.config.serial.timeout / 2  # примерное значение
            )
            await self.port_handler.start()
            logger.info(f"Connected to {com_port}")
            return True

        except serial.SerialException as e:
            logger.error(f"Connection error: {e}")
            return False
    async def disconnect(self) -> None:
        """Closes the serial connection."""
        self._running = False
        if self.port_handler:
            await self.port_handler.stop()
        if self.connection and self.connection.is_open:
            self.connection.close()
            logger.info("Connection closed")

    async def send_command(self, command_str: str) -> Optional[List[str]]:
        if not self.connection or not self.connection.is_open or not self.port_handler:
            logger.warning("No active connection")
            return None

        try:
            # Формируем и отправляем команду через COMPortHandler
            full_command = f"{command_str.strip()}{self.config.serial.command_terminator}"
            await self.port_handler.send_command(full_command)
            # Здесь мы всё равно запрашиваем ответ, но благодаря фоновой задаче
            # мы не блокируем остальную работу, а просто забираем уже накопленные данные
            if self.config.serial.response_mode == "full":
                return await self.port_handler.get_response(timeout=self.config.serial.timeout)
            else:
                return await self.port_handler.get_response(timeout=0.2)
        except Exception as e:
            logger.error(f"Command failed: {e}")
            return None
        
    async def read_response(self, timeout: float = 3.0, inter_byte_timeout: float = 0.5) -> List[str]:
        # Тут можно просто делегировать через COMPortHandler, если понадобится
        if self.port_handler:
            return await self.port_handler.get_response(timeout=timeout)
        return []