# Содержимое файла: smeller/controllers/aromablock_model_controller.py

from PyQt6.QtCore import pyqtSignal, QObject
from smeller.database.db_manager import DatabaseManager  #  Импорт DatabaseManager
from smeller.models.aroma_block import AromaBlock #  Импорт AromaBlock
from smeller.models.channel_control_config import ChannelControlConfig
import logging
logger = logging.getLogger(__name__)

class AromaBlockModelController(QObject):
    """
    Контроллер для управления операциями, связанными с AromaBlock.
    Отделяет логику управления аромаблоками от MainWindowViewModel.
    """
    aromablocks_list_updated = pyqtSignal(list)
    aromablock_loaded = pyqtSignal(AromaBlock)
    aromablock_saved = pyqtSignal(int)
    control_error = pyqtSignal(str)

    def __init__(self, db_manager: DatabaseManager, parent=None):
        super().__init__(parent)
        self.db_manager = db_manager
        if not self.db_manager or not self.db_manager.engine:
            logger.error("AromaBlockModelController initialized without a valid DatabaseManager.")
            #  Можно решить, что делать в этом случае, например, выбросить исключение

    def get_all_aromablocks_from_db(self):
        """
        Получает все AromaBlock из базы данных через DatabaseManager и
        эмитирует сигнал aromablocks_list_updated с полученным списком.
        """
        logger.info("Fetching all AromaBlocks from the database...")
        try:
            if not self.db_manager or not self.db_manager.engine:
                logger.error("DatabaseManager is not initialized.")
                self.control_error.emit("Database error: не удалось подключиться к базе данных.")
                return

            aromablocks = self.db_manager.get_all_aromablocks() 

            if aromablocks:
                logger.info(f"Successfully fetched {len(aromablocks)} AromaBlocks from DB.")
                #  Эмитируем сигнал с обновленным списком аромаблоков
                self.aromablocks_list_updated.emit(aromablocks)
            else:
                logger.info("No AromaBlocks found in database or database error.")
                self.aromablocks_list_updated.emit([]) #  Эмитируем пустой список, если блоков нет или ошибка
                if not self.db_manager.engine: #  Если ошибка подключения к БД
                    self.control_error.emit("Database error: не удалось получить список аромаблоков.")
        except Exception as e:
            error_message = f"Error fetching AromaBlocks: {e}"
            logger.error(error_message, exc_info=True)
            self.control_error.emit(error_message)

    def load_aromablock_from_db(self, aromablock_id: int):
        """
        Загружает AromaBlock из базы данных и применяет конфигурацию к ViewModel.
        """
        logger.info(f"Loading AromaBlock with ID: {aromablock_id} from database.")
        try:
            if not self.db_manager or not self.db_manager.engine:
                logger.error("DatabaseManager is not initialized.")
                self.control_error.emit("Database error: не удалось подключиться к базе данных.")
                return

            db_aromablock = self.db_manager.load_aromablock(aromablock_id)
            if db_aromablock:
                loaded_aromablock = db_aromablock
                logger.info(f"AromaBlock '{loaded_aromablock.name}' loaded successfully.")
                #  Эмитируем сигнал о загрузке аромаблока
                self.aromablock_loaded.emit(loaded_aromablock)
                return loaded_aromablock
            else:
                error_message = f"AromaBlock with ID {aromablock_id} not found in database."
                logger.warning(error_message)
                self.control_error.emit(error_message)
                return None
            
        except Exception as e:
            error_message = f"Error loading AromaBlock with ID {aromablock_id}: {e}"
            logger.error(error_message, exc_info=True)
            self.control_error.emit(error_message)
            return None

    def save_current_config_as_aromablock(self, aromablock_name: str, 
                                          aromablock_description: str, 
                                          aromablock_data_type: str, 
                                          aromablock_content_link: str,
                                          start_time: float, stop_time: float, channel_configs) -> AromaBlock:
        """
        Сохраняет текущую конфигурацию каналов как новый AromaBlock в базе данных.

        Args:
            aromablock_name (str): Имя для нового блока.
            aromablock_description (str): Описание блока.
            aromablock_data_type (str): Тип данных (например, видео, аудио).
            aromablock_content_link (str): Ссылка на контент, если имеется.
            start_time (float): Время начала блока в секундах.
            stop_time (float): Время окончания блока в секундах.
            channel_configs: Конфигурации каналов.
        """
        logger.info(f"Saving current configuration as AromaBlock '{aromablock_name}'...")
        if not self.db_manager or not self.db_manager.engine:
            logger.error("DatabaseManager is not initialized.")
            self.control_error.emit("Database error: не удалось подключиться к базе данных.")
            return None

        #  1. Собираем текущие конфигурации каналов из ViewModel (теперь передаются аргументом)
        current_channel_configurations = channel_configs.copy() #  Копируем, чтобы избежать неожиданных изменений

        #  2. Создаем объект AromaBlock
        new_aromablock = AromaBlock(
            name=aromablock_name,
            description=aromablock_description,
            data_type=aromablock_data_type,
            content_link=aromablock_content_link,
            channel_configurations=current_channel_configurations,
            start_time=start_time,
            stop_time=stop_time
        )

        #  3. Сохраняем AromaBlock в базу данных через db_manager
        block_id = self.db_manager.save_aromablock(new_aromablock)
        if block_id:
            logger.info(f"AromaBlock '{aromablock_name}' saved successfully with ID: {block_id}")
            new_aromablock.id = block_id
            #  Эмитируем сигнал об успешном сохранении, передавая ID
            self.aromablock_saved.emit(block_id)
            #  Опционально: можно сразу обновить список аромаблоков в GUI
            self.get_all_aromablocks_from_db()
            return new_aromablock
        else:
            error_message = f"Failed to save AromaBlock '{aromablock_name}' to database."
            logger.error(error_message, exc_info=True)
            self.control_error.emit(error_message)
            return None

    def apply_aromablock_config(self, loaded_aromablock: AromaBlock):
        """
        Применяет конфигурацию загруженного AromaBlock.
        Возвращает channel_configurations для применения в ViewModel.

        Args:
            loaded_aromablock (AromaBlock): Загруженный объект AromaBlock.

        Returns:
            Dict: channel_configurations из AromaBlock.
        """
        logger.info(f"Applying configuration from AromaBlock '{loaded_aromablock.name}'...")
        # Возвращаем конфигурации каналов для установки в ViewModel
        return loaded_aromablock.channel_configurations.copy()

    def delete_aromablock_from_db(self, aromablock_id: int):
        """Удаляет AromaBlock из базы данных по ID и обновляет список."""
        logger.info(f"Deleting AromaBlock with ID: {aromablock_id} from database.")
        if not self.db_manager or not self.db_manager.engine:
            logger.error("DatabaseManager is not initialized.")
            self.control_error.emit("Database error: не удалось подключиться к базе данных.")
            return

        deleted = self.db_manager.delete_aromablock(aromablock_id) #  Вызываем метод DatabaseManager для удаления
        if deleted:
            logger.info(f"AromaBlock with ID {aromablock_id} deleted successfully.")
            self.get_all_aromablocks_from_db() #  Обновляем список аромаблоков после удаления
        else:
            error_message = f"Failed to delete AromaBlock with ID {aromablock_id} from database."
            logger.error(error_message)
            self.control_error.emit(error_message) #  Сигнал об ошибке, если не удалось удалить

    def copy_aromablock_in_db(self, aromablock_id: int):
        """Копирует AromaBlock из базы данных по ID и сохраняет как новый."""
        logger.info(f"Copying AromaBlock with ID: {aromablock_id} from database.")
        if not self.db_manager or not self.db_manager.engine:
            logger.error("DatabaseManager is not initialized.")
            self.control_error.emit("Database error: не удалось подключиться к базе данных.")
            return None

        original_aromablock = self.db_manager.load_aromablock(aromablock_id) #  Загружаем оригинальный аромаблок
        if original_aromablock:
            copied_aromablock = AromaBlock( #  Создаем новый объект AromaBlock на основе оригинала
                name=f"{original_aromablock.name} (Copy)", #  Добавляем "(Copy)" к имени
                description=original_aromablock.description,
                data_type=original_aromablock.data_type,
                content_link=original_aromablock.content_link,
                channel_configurations=original_aromablock.channel_configurations.copy(), #  Копируем конфигурации каналов
                start_time=original_aromablock.start_time, #  Копируем start_value
                stop_time=original_aromablock.stop_time     #  Копируем stop_value
            )
            new_block_id = self.db_manager.save_aromablock(copied_aromablock) #  Сохраняем как новый, ID будет сгенерирован заново
            if new_block_id:
                logger.info(f"AromaBlock '{copied_aromablock.name}' (ID: {new_block_id}) copied successfully.")
                self.aromablock_saved.emit(new_block_id) #  Эмитируем сигнал о сохранении копии
                self.get_all_aromablocks_from_db() #  Обновляем список аромаблоков
                return new_block_id
            else:
                error_message = f"Failed to save copied AromaBlock '{copied_aromablock.name}' to database."
                logger.error(error_message)
                self.control_error.emit(error_message)
                return None
        else:
            error_message = f"AromaBlock with ID {aromablock_id} not found for copying."
            logger.warning(error_message)
            self.control_error.emit(error_message)
            return None  
        
    def update_aromablock_in_db(self, aromablock: 'AromaBlock'):
        """Обновляет существующий AromaBlock в базе данных."""
        logger.info(f"Updating AromaBlock '{aromablock.name}' with ID: {aromablock.id} in database.")
        if not self.db_manager or not self.db_manager.engine:
            logger.error("DatabaseManager is not initialized.")
            self.control_error.emit("Database error: не удалось подключиться к базе данных.")
            return False

        updated_block_id = self.db_manager.save_aromablock(aromablock) #  Используем существующий save_aromablock из db_manager
        if updated_block_id:
            logger.info(f"AromaBlock '{aromablock.name}' (ID: {updated_block_id}) updated successfully.")
            self.aromablock_saved.emit(updated_block_id) #  Эмитируем сигнал об успешном сохранении, передавая ID
            self.get_all_aromablocks_from_db() #  Обновляем список аромаблоков
            return True
        else:
            error_message = f"Failed to update AromaBlock '{aromablock.name}' (ID: {aromablock.id}) in database."
            logger.error(error_message)
            self.control_error.emit(error_message)
            return False