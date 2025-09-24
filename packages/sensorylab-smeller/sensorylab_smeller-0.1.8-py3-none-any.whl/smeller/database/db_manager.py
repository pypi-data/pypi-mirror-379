# Содержимое файла: smeller/database/db_manager.py
from dataclasses import asdict
from typing import List, Optional
    
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
import logging
from smeller.models.aroma_block import AromaBlockModel, AromaBlock
from smeller.models.channel_control_config import ChannelControlConfig # Убедись, что этот импорт тоже есть, если нет - добавь
from smeller.models.cartridge import CartridgeModel 
from smeller.config.config import DatabaseConfig 
from smeller.models.aroma_track import AromaTrackModel #  <-- Импорт AromaTrackModel
from smeller.models.base import Base #  Импорт Base

logger = logging.getLogger(__name__)


class DatabaseManager:
    """
    Класс для управления подключением к базе данных и выполнения запросов.
    """
    def __init__(self, db_config: DatabaseConfig):
        self.db_params = {
            'dbname': db_config.dbname,
            'user': db_config.user,
            'password': db_config.password,
            'host': db_config.host,
            'port': db_config.port,
            'options': db_config.options
        }
        self.engine = None
        self.Session = sessionmaker() #  Создаем Session factory, но не привязываем к engine пока

    def create_engine(self):
        """
        Создает SQLAlchemy engine. Использует параметры подключения из __init__.
        """
        if self.engine is None:
            db_url = f"postgresql://{self.db_params['user']}:{self.db_params['password']}@{self.db_params['host']}:{self.db_params['port']}/{self.db_params['dbname']}"
            try:
                self.engine = create_engine(db_url)
                #Base.metadata.drop_all(self.engine)
                Base.metadata.create_all(self.engine) #  Создаем таблицы, если их нет
                self.Session.configure(bind=self.engine) # Привязываем Session factory к созданному engine
                self.create_aromablock_table_if_not_exists()
                self.create_aroma_track_table_if_not_exists() 
                logger.info(f"Database engine created successfully for host: {self.db_params['host']}")
            except SQLAlchemyError as e:
                logger.error(f"Database engine creation error: {e}")
                self.engine = None
                raise
        return self.engine

    def get_session(self):
        """
        Возвращает новую сессию SQLAlchemy. Гарантирует, что engine создан.
        """
        if self.engine is None:
            self.create_engine() #  Создаем engine, если он еще не создан
        return self.Session()

    def get_cartridge_by_id(self, cartridge_id: int):
        """
        Получает картридж из базы данных по ID.

        Args:
            cartridge_id (int): ID картриджа для поиска.

        Returns:
            CartridgeModel: Объект CartridgeModel или None, если не найден.
        """
        session = self.get_session()
        try:
            cartridge = session.query(CartridgeModel).filter(CartridgeModel.ID == cartridge_id).first()
            if cartridge:
                logger.debug(f"Cartridge found in DB: {cartridge}")
            else:
                logger.debug(f"Cartridge ID {cartridge_id} not found in DB.")
            return cartridge
        except SQLAlchemyError as e:
            logger.error(f"Database query error (get_cartridge_by_id): {e}")
            return None
        finally:
            session.close()

    def get_all_cartridges(self):
        """
        Получает все картриджи из базы данных.

        Returns:
            List[CartridgeModel]: Список объектов CartridgeModel.
        """
        session = self.get_session()
        try:
            cartridges = session.query(CartridgeModel).all()
            logger.debug(f"Fetched {len(cartridges)} cartridges from DB.")
            return cartridges
        except SQLAlchemyError as e:
            logger.error(f"Database query error (get_all_cartridges): {e}")
            return []
        finally:
            session.close()
            
    def create_aromablock_table_if_not_exists(self):
        """Создает таблицу sl_aromablocks в БД, если она не существует."""
        if self.engine is None:
            self.create_engine() #  Убедимся, что engine создан
        try:
            #Base.metadata.drop_all(self.engine, tables=[AromaBlockModel.__table__], checkfirst=True)
            Base.metadata.create_all(self.engine, tables=[AromaBlockModel.__table__], checkfirst=True)
            logger.info("AromaBlock table created or already exists.")
        except SQLAlchemyError as e:
            logger.error(f"Error creating AromaBlock table: {e}")
            raise

    def create_aroma_track_table_if_not_exists(self):
        """Создает таблицу aroma_tracks в БД, если она не существует."""
        if self.engine is None:
            self.create_engine() #  Убедимся, что engine создан
        try:
            #Base.metadata.drop_all(self.engine, tables=[AromaTrackModel.__table__], checkfirst=True) #  ОСТОРОЖНО: УДАЛЕНИЕ ТАБЛИЦЫ!
            Base.metadata.create_all(self.engine, tables=[AromaTrackModel.__table__], checkfirst=True)
            logger.info("AromaTrack table created or already exists.")
        except SQLAlchemyError as e:
            logger.error(f"Error creating AromaTrack table: {e}")
            raise
        
    def get_aromablock_session(self):
        """Возвращает новую сессию SQLAlchemy, связанную с engine для AromaBlockModel."""
        if self.engine is None:
            self.create_engine() #  Убедимся, что engine создан
        return self.Session() #
    
    def save_aromablock(self, aromablock: 'AromaBlock'): #  Важно: используем type hint в виде строки 'AromaBlock'
        """Сохраняет или обновляет AromaBlock в базе данных."""
        session = self.get_aromablock_session() #  Используем сессию для аромаблоков
        try:
            #  Сериализуем channel_configurations в JSON
            channel_configs_json = {}
            for channel_id, config in aromablock.channel_configurations.items():
                channel_configs_json[channel_id] = asdict(config) #  Преобразуем в dict

            if aromablock.id is not None:
                #  Обновление существующей записи
                db_aromablock = session.query(AromaBlockModel).filter(AromaBlockModel.id == aromablock.id).first()
                if db_aromablock:
                    db_aromablock.name = aromablock.name
                    db_aromablock.description = aromablock.description
                    db_aromablock.data_type = aromablock.data_type
                    db_aromablock.content_link = aromablock.content_link
                    db_aromablock.channel_configurations = channel_configs_json
                    db_aromablock.start_time = aromablock.start_time
                    db_aromablock.stop_time = aromablock.stop_time
                else:
                    logger.warning(f"AromaBlock with ID {aromablock.id} not found for update.")
                    return None #  Или raise exception
            else:
                #  Создание новой записи
                db_aromablock = AromaBlockModel(
                    name=aromablock.name,
                    description=aromablock.description,
                    data_type=aromablock.data_type,
                    content_link=aromablock.content_link,
                    channel_configurations=channel_configs_json,
                    start_time = aromablock.start_time,
                    stop_time = aromablock.stop_time,
                )
                session.add(db_aromablock)
            session.commit()
            logger.info(f"AromaBlock '{aromablock.name}' with ID {db_aromablock.id} saved/updated in DB.")
            return db_aromablock.id #  Возвращаем ID сохраненной записи
        except SQLAlchemyError as e:
            session.rollback()
            logger.error(f"Database error saving AromaBlock: {e}", exc_info=True)
            return None
        finally:
            session.close()

    def load_aromablock(self, aromablock_id: int) -> Optional['AromaBlock']: #  Важно: используем type hint в виде строки 'AromaBlock'
        """Загружает AromaBlock из базы данных по ID."""
        session = self.get_aromablock_session() #  Используем сессию для аромаблоков
        try:
            db_aromablock = session.query(AromaBlockModel).filter(AromaBlockModel.id == aromablock_id).first()
            if db_aromablock:
                #  Десериализуем JSON обратно в Dict[int, ChannelControlConfig]
                channel_configs_data = db_aromablock.channel_configurations or {}
                channel_configurations = {}
                for channel_id, config_data in channel_configs_data.items():
                    channel_configurations[int(channel_id)] = ChannelControlConfig(**config_data) #  Создаем ChannelControlConfig из dict

                return AromaBlock(
                    id=db_aromablock.id,
                    name=db_aromablock.name,
                    description=db_aromablock.description,
                    data_type=db_aromablock.data_type,
                    content_link=db_aromablock.content_link,
                    channel_configurations=channel_configurations,
                    start_time = db_aromablock.start_time,
                    stop_time = db_aromablock.stop_time
                )
            else:
                logger.debug(f"AromaBlock with ID {aromablock_id} not found in DB.")
                return None
        except SQLAlchemyError as e:
            logger.error(f"Database error loading AromaBlock: {e}", exc_info=True)
            return None
        finally:
            session.close()

    def get_all_aromablocks(self) -> List['AromaBlock']: #  Важно: используем type hint в виде строки 'AromaBlock'
        """Возвращает список всех AromaBlock из базы данных."""
        session = self.get_aromablock_session() #  Используем сессию для аромаблоков
        try:
            db_aromablocks = session.query(AromaBlockModel).all()
            aromablocks = []
            for db_block in db_aromablocks:
                #  Десериализуем JSON в ChannelControlConfig для каждого блока
                channel_configs_data = db_block.channel_configurations or {}
                channel_configurations = {}
                for channel_id, config_data in channel_configs_data.items():
                    channel_configurations[int(channel_id)] = ChannelControlConfig(**config_data)

                aromablocks.append(AromaBlock(
                    id=db_block.id,
                    name=db_block.name,
                    description=db_block.description,
                    data_type=db_block.data_type,
                    content_link=db_block.content_link,
                    channel_configurations=channel_configurations,
                    start_time = db_block.start_time,
                    stop_time = db_block.stop_time
                ))
            logger.debug(f"Fetched {len(aromablocks)} AromaBlocks from DB.")
            return aromablocks
        except SQLAlchemyError as e:
            logger.error(f"Database error fetching all AromaBlocks: {e}", exc_info=True)
            return []
        finally:
            session.close()

    def delete_aromablock(self, aromablock_id: int) -> bool:
        """Удаляет AromaBlock из базы данных по ID."""
        session = self.get_aromablock_session() #  Используем сессию для аромаблоков
        try:
            db_aromablock = session.query(AromaBlockModel).filter(AromaBlockModel.id == aromablock_id).first()
            if db_aromablock:
                session.delete(db_aromablock)
                session.commit()
                logger.info(f"AromaBlock with ID {aromablock_id} deleted from DB.")
                return True
            else:
                logger.warning(f"AromaBlock with ID {aromablock_id} not found for deletion.")
                return False
        except SQLAlchemyError as e:
            session.rollback()
            logger.error(f"Database error deleting AromaBlock: {e}", exc_info=True)
            return False
        finally:
            session.close()
