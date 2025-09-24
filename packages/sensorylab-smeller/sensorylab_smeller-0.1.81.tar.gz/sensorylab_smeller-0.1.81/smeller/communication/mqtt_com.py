# Содержимое файла: mqtt_com.py
# Содержимое файла: mqtt_com.py
import asyncio
import logging
from typing import List, Optional, Dict # Добавлен Dict

from smeller.communication.base import CommunicationInterface
from smeller.config.config import AppConfig, MqttConfig
from smeller.services.mqtt_client import MqttClient

logger = logging.getLogger(__name__)

class MqttCommunication(CommunicationInterface):
    """
    Реализация интерфейса связи через MQTT.
    Предназначена для работы в режиме Singleton, управляя одним MQTT клиентом
    для взаимодействия с несколькими устройствами (по chip_id).
    """

    def __init__(self, config: AppConfig):
        """
        Инициализирует MQTT Communication. Вызывается фабрикой один раз.
        """
        self.config: AppConfig = config
        # Проверяем наличие MQTT конфигурации при инициализации
        if not config.mqtt or not config.mqtt.host:
            # Эта проверка дублируется в фабрике, но лучше перестраховаться
            raise ValueError("MqttConfig with host is required for MqttCommunication.")
        self.mqtt_config: MqttConfig = config.mqtt
        self.mqtt_client: Optional[MqttClient] = None
        self._client_started: bool = False # Флаг, что клиент был запущен

        # --- Начало изменений: Управление очередями для разных chip_id ---
        # Словарь для хранения очередей ответов для каждого chip_id
        # Ключ: chip_id (str), Значение: asyncio.Queue
        self._response_queues: Dict[str, asyncio.Queue] = {}
        # Блокировка для синхронизации доступа к словарю очередей
        self._queues_lock = asyncio.Lock()
        # --- Конец изменений ---

        # Убран _current_chip_id, так как он теперь передается в методы

    async def _ensure_client_started(self):
        """Внутренний метод для создания и запуска MQTT клиента (если еще не сделано)."""
        if not self.mqtt_client:
            logger.info("Initializing MQTT client...")
            self.mqtt_client = MqttClient(
                host=self.mqtt_config.host,
                port=self.mqtt_config.port,
                username=self.mqtt_config.username,
                password=self.mqtt_config.password
                # client_id можно настроить, если нужно
            )
            # Подключаем обработчик сообщений *один раз* при создании клиента
            self.mqtt_client.message_received.connect(self._on_mqtt_message)

        if not self._client_started:
             logger.info("Starting MQTT client thread...")
             try:
                 self.mqtt_client.start() # Запускаем MQTT client в отдельном потоке
                 self._client_started = True
                 # Можно добавить небольшую задержку или проверку статуса подключения,
                 # но MqttClient сам должен управлять переподключениями.
                 await asyncio.sleep(0.1) # Небольшая пауза, чтобы дать клиенту запуститься
             except Exception as e:
                 logger.error(f"Failed to start MQTT client: {e}", exc_info=True)
                 self.mqtt_client = None # Сбрасываем клиент при ошибке старта
                 self._client_started = False
                 return False
        return True

    async def connect(self, chip_id: Optional[str] = None, **kwargs) -> bool:
        """
        Регистрирует chip_id для получения ответов и проверяет/запускает MQTT клиент.

        Args:
            chip_id: Уникальный идентификатор устройства (обязателен).
            **kwargs: Дополнительные аргументы (игнорируются).

        Returns:
            True, если клиент запущен и chip_id зарегистрирован, иначе False.
        """
        if not chip_id:
            logger.error("Chip ID is required for MQTT connection registration.")
            return False

        logger.info(f"Registering MQTT connection for chip_id: {chip_id}")

        # Убеждаемся, что MQTT клиент создан и запущен
        client_ready = await self._ensure_client_started()
        if not client_ready or not self.mqtt_client:
            logger.error(f"MQTT client is not available. Cannot register chip_id {chip_id}.")
            return False

        # Создаем очередь для этого chip_id, если ее еще нет
        async with self._queues_lock:
            if chip_id not in self._response_queues:
                logger.debug(f"Creating response queue for chip_id: {chip_id}")
                self._response_queues[chip_id] = asyncio.Queue()
            else:
                logger.debug(f"Response queue for chip_id {chip_id} already exists.")

        # В реальной реализации MQTT, здесь могла бы быть подписка на топик вида /devices/{chip_id}/out
        # Но текущий MqttClient, похоже, обрабатывает это иначе (подписывается шире и фильтрует).
        # Оставляем как есть, полагаясь на MqttClient и _on_mqtt_message.

        logger.info(f"MQTT Communication ready for chip_id: {chip_id}")
        # Возвращаем статус подключения самого клиента MQTT
        return self.mqtt_client.is_connected # Возвращаем реальный статус подключения к брокеру

    async def disconnect(self) -> None:
        """
        Останавливает MQTT клиент и очищает все ресурсы.
        Влияет на все устройства, использующие этот Singleton.
        """
        logger.warning("Disconnecting MQTT client (affects all registered devices)...")
        if self.mqtt_client:
            try:
                self.mqtt_client.stop()
                # MqttClient.stop() должен сам ожидать завершения потока,
                # но добавим ожидание на всякий случай, если stop не блокирующий
                # self.mqtt_client.wait() # Если есть такой метод
            except Exception as e:
                logger.error(f"Error stopping MQTT client: {e}", exc_info=True)
            finally:
                self.mqtt_client = None
                self._client_started = False
                async with self._queues_lock:
                    self._response_queues.clear()
                logger.info("MQTT client stopped and resources cleared.")
        else:
            logger.warning("MQTT client is not initialized or already stopped.")

    async def disconnect_chip(self, chip_id: str) -> None:
        """
        Дерегистрирует chip_id, удаляя его очередь ответов.
        Не останавливает MQTT клиент.

        Args:
            chip_id: Идентификатор устройства для дерегистрации.
        """
        if not chip_id:
            logger.warning("No chip_id provided for deregistration.")
            return

        logger.info(f"Deregistering MQTT chip_id: {chip_id}")
        async with self._queues_lock:
            if chip_id in self._response_queues:
                # Очищаем очередь перед удалением, чтобы разбудить ожидающие задачи
                queue = self._response_queues[chip_id]
                while not queue.empty():
                    try:
                        queue.get_nowait()
                    except asyncio.QueueEmpty:
                        break
                    queue.task_done() # Отмечаем задачу как выполненную

                del self._response_queues[chip_id]
                logger.debug(f"Removed response queue for chip_id: {chip_id}")
            else:
                logger.warning(f"No response queue found for chip_id: {chip_id} to deregister.")
        # Здесь можно было бы отписаться от топика устройства, если бы MqttClient это поддерживал

    # --- Изменение сигнатуры: добавлен chip_id ---
    async def send_command(self, command_str: str, chip_id: str) -> Optional[List[str]]:
        """
        Отправка команды конкретному устройству через MQTT.

        Args:
            command_str: Строка команды.
            chip_id: Идентификатор целевого устройства.

        Returns:
            ["Command sent to MQTT Broker"] если отправка инициирована, None в случае ошибки.
            Примечание: Успешная отправка брокеру не гарантирует доставку устройству.
        """
        if not chip_id:
            logger.error("Chip ID is required to send MQTT command.")
            return None

        if self.mqtt_client and self.mqtt_client.is_connected:
            # Формируем команду с терминатором
            full_command = f"{command_str.strip()}{self.mqtt_config.command_terminator}"
            try:
                # MqttClient.send_message ожидает chip_id и сообщение
                await self.mqtt_client.send_message(chip_id, full_command)
                logger.debug(f"MQTT Command '{command_str.strip()}' queued for chip_id {chip_id}")
                # Возвращаем фиктивный ответ, подтверждающий отправку в брокер
                return ["Command sent to MQTT Broker"]
            except Exception as e:
                 logger.error(f"Failed to send MQTT command to chip_id {chip_id}: {e}", exc_info=True)
                 return None
        else:
            logger.warning(f"MQTT client is not connected. Cannot send command to chip_id {chip_id}.")
            return None

    # --- Изменение сигнатуры: добавлен chip_id ---
    async def read_response(
        self,
        chip_id: str,
        timeout: float = 5.0,
        inter_byte_timeout: float = 0.5 # Этот параметр здесь не используется
    ) -> List[str]:
        """
        Чтение ответа из очереди для конкретного chip_id.

        Args:
            chip_id: Идентификатор устройства, от которого ожидается ответ.
            timeout: Максимальное время ожидания ответа в секундах.
            inter_byte_timeout: Не используется в MQTT.

        Returns:
            Список строк ответа (обычно одна строка). Пустой список при таймауте.
        """
        if not chip_id:
            logger.error("Chip ID is required to read MQTT response.")
            return []

        responses = []
        queue: Optional[asyncio.Queue] = None

        async with self._queues_lock:
            queue = self._response_queues.get(chip_id)

        if queue is None:
            logger.warning(f"No response queue found for chip_id: {chip_id}. Cannot read response.")
            # Возможно, стоит подождать немного, если connect был вызван только что?
            # await asyncio.sleep(0.1) # Или вернуть пустой список сразу
            return []

        try:
            logger.debug(f"Waiting for response from chip_id {chip_id} (timeout: {timeout}s)")
            # Ожидаем ответ из *специфичной* для chip_id очереди
            response = await asyncio.wait_for(queue.get(), timeout=timeout)
            responses.append(response)
            queue.task_done() # Сообщаем очереди, что элемент обработан
            logger.debug(f"MQTT Response received for chip_id {chip_id}: {response}")
        except asyncio.TimeoutError:
            logger.debug(f"No MQTT response received for chip_id {chip_id} within timeout.")
        except asyncio.CancelledError:
             logger.warning(f"Response reading cancelled for chip_id {chip_id}")
             # Важно пробросить исключение, чтобы внешняя задача могла его обработать
             raise
        except Exception as e:
             logger.error(f"Error reading response queue for chip_id {chip_id}: {e}", exc_info=True)

        return responses

    def _on_mqtt_message(self, chip_id: str, topic_suffix: str, message: str):
        """
        Обработчик входящих MQTT сообщений.
        Вызывается из MqttClient при получении любого сообщения.
        Маршрутизирует сообщение в очередь соответствующего chip_id.
        """
        logger.debug(f"MQTT message received: chip_id={chip_id}, suffix='{topic_suffix}', msg='{message[:50]}...'") # Логируем начало сообщения

        # --- Начало изменений: Маршрутизация в нужную очередь ---
        queue: Optional[asyncio.Queue] = None
        # Не блокируем здесь надолго, используем get без async with
        # Доступ к словарю для чтения обычно потокобезопасен в CPython из-за GIL,
        # но использование get безопасно в любом случае.
        queue = self._response_queues.get(chip_id)

        if queue:
            # Мы заинтересованы только в ответах на команды (предполагаем, что они приходят с суффиксом 'out')
            if topic_suffix == 'out':
                try:
                    queue.put_nowait(message)
                    logger.debug(f"MQTT message for chip_id {chip_id} (suffix: {topic_suffix}) placed in queue.")
                except asyncio.QueueFull:
                    logger.error(f"Response queue for chip_id {chip_id} is full! Message lost: {message[:50]}...")
            else:
                # Можно обрабатывать другие суффиксы (например, 'status', 'telemetry') иначе, если нужно
                logger.debug(f"MQTT message for chip_id {chip_id} with suffix '{topic_suffix}' ignored (not 'out').")
        else:
            # Сообщение пришло для chip_id, для которого нет активной очереди (connect не вызывался или был disconnect_chip)
             # Не считаем это ошибкой, просто игнорируем или логируем с уровнем INFO/DEBUG
            logger.debug(f"Received MQTT message for unregistered chip_id {chip_id}. Ignoring.")
        # --- Конец изменений ---

    async def is_connected(self, chip_id: Optional[str] = None) -> bool:
        """
        Проверяет, подключен ли MQTT клиент к брокеру.
        Опционально проверяет, зарегистрирован ли chip_id.

        Args:
            chip_id: Если указан, проверяется также наличие очереди для него.

        Returns:
            True, если MQTT клиент подключен (и chip_id зарегистрирован, если указан).
        """
        if not self.mqtt_client or not self.mqtt_client.is_connected:
            return False

        if chip_id:
            # Проверяем наличие очереди под блокировкой
            async with self._queues_lock:
                return chip_id in self._response_queues
        else:
            # Если chip_id не указан, просто возвращаем статус клиента
            return True