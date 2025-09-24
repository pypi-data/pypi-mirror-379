# Содержимое файла: smeller/controllers/cartridge_manager.py
from smeller.database.db_manager import DatabaseManager
import logging

logger = logging.getLogger(__name__)

class CartridgeManager:
    """
    Класс для управления информацией о картриджах, включая взаимодействие с базой данных.
    """
    def __init__(self, db_manager: DatabaseManager):
        """
        Инициализирует CartridgeManager, принимая DatabaseManager в качестве зависимости.

        Args:
            db_manager (DatabaseManager): Экземпляр DatabaseManager для доступа к БД.
        """
        self.db_manager = db_manager
        if self.db_manager:
            logger.info("CartridgeManager initialized with DatabaseManager.")
        else:
            logger.warning("CartridgeManager initialized without DatabaseManager.")

    def get_cartridge_name_from_db(self, cartridge_id: int) -> str:
        """
        Получает имя картриджа из базы данных по его ID.

        Args:
            cartridge_id (int): ID картриджа.

        Returns:
            str: Имя картриджа или None, если картридж не найден.
        """
        if not self.db_manager:
            logger.warning("DatabaseManager is not initialized. Cannot fetch cartridge name from DB.")
            return None

        cartridge = self.db_manager.get_cartridge_by_id(cartridge_id)
        if cartridge:
            return cartridge.NAME
        else:
            return None

    def get_all_cartridges_from_db(self):
        """
        Получает все картриджи из базы данных.

        Returns:
            List[CartridgeModel]: Список объектов CartridgeModel.
        """
        if not self.db_manager:
            logger.warning("DatabaseManager is not initialized. Cannot fetch all cartridges from DB.")
            return []
        return self.db_manager.get_all_cartridges()

    async def discover_cartridge_info_from_device(self, channel_index, device_controller): #  <--- Добавлен device_controller
        """
        Получает ID картриджа с устройства используя 'crGetI' команду и ищет имя в БД.

        Args:
            channel_index (int): Индекс канала, для которого нужно получить информацию о картридже.
            device_controller (DeviceController): Экземпляр DeviceController для отправки команд.

        Returns:
            dict: Словарь с информацией о картридже (cartridge_id, cartridge_name).
        """
        try:
            response_lines = await device_controller.cr_get_info() #  <--- Используем cr_get_info команду
            if response_lines:
                # Парсим ответ. Ожидаем формат: '0| id=..., s=..., cnt=...', ...
                for line in response_lines:
                    parts = line.split('|')
                    if len(parts) > 1 and parts[0].strip() == str(channel_index): #  Ищем строку для нужного channel_index
                        params_str = parts[1]
                        param_pairs = params_str.split(', ')
                        cartridge_id_str = None
                        for pair in param_pairs:
                            if pair.startswith('id='):
                                cartridge_id_str = pair[3:] #  Извлекаем значение после 'id='
                                break
                        if cartridge_id_str:
                            try:
                                cartridge_id = int(cartridge_id_str) #  Преобразуем ID в int
                                cartridge_name = self.get_cartridge_name_from_db(cartridge_id) #  Ищем имя в БД
                                logger.info(f"Channel {channel_index+1}: Device reported cartridge ID {cartridge_id}, name from DB: '{cartridge_name}'")
                                return {'cartridge_id': str(cartridge_id), 'cartridge_name': cartridge_name}
                            except ValueError:
                                logger.warning(f"Channel {channel_index+1}: Invalid cartridge ID format in response: '{cartridge_id_str}'")
                                return {'cartridge_id': None, 'cartridge_name': None} #  Неверный формат ID
                        else:
                            logger.warning(f"Channel {channel_index+1}: Cartridge ID not found in response.")
                            return {'cartridge_id': None, 'cartridge_name': None} #  ID не найден в ответе
                logger.warning(f"Channel {channel_index+1}: No info in crGetI response for this channel.")
                return {'cartridge_id': None, 'cartridge_name': None} #  Нет информации для этого канала
            else:
                logger.warning(f"Channel {channel_index+1}: Empty response from crGetI command.")
                return {'cartridge_id': None, 'cartridge_name': None} #  Пустой ответ от устройства

        except Exception as e:
            logger.error(f"Error fetching cartridge info from device for channel {channel_index+1}: {e}", exc_info=True)
            return {'cartridge_id': None, 'cartridge_name': None} #  Ошибка при запросе/парсинге