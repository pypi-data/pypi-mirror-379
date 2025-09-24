# smeller/models/aromablock.py
from dataclasses import dataclass, field
from typing import Optional, Dict, List, Tuple
from sqlalchemy import Column, Integer, String, JSON, Float, ForeignKey
from sqlalchemy.orm import relationship
from .channel_control_config import ChannelControlConfig 
from .base import Base

@dataclass
class AromaBlock:
    """
    Data class representing an Aroma Block which defines a segment of an aroma track.

    Attributes:
        id (Optional[int]): Unique identifier if loaded from the database.
        name (str): The name of the aroma block.
        description (Optional[str]): A textual description of the aroma block.
        data_type (str): Type of content associated with the block (e.g. video, audio).
        content_link (Optional[str]): Link or path to the content.
        channel_configurations (Dict): Dictionary containing channel settings; typically stored as JSON.
        start_time (Optional[float]): The time (in seconds) when this aroma block begins in the track.
        stop_time (Optional[float]): The time (in seconds) when this aroma block ends in the track.
    """
    id: Optional[int] = None
    name: str = ""
    description: Optional[str] = None
    data_type: Optional[str] = None
    content_link: Optional[str] = None
    channel_configurations: Dict[int, ChannelControlConfig] = field(default_factory=dict)
    start_time: Optional[float] = None
    stop_time: Optional[float] = None

    def __repr__(self) -> str:
        return (f"AromaBlock(id={self.id}, name='{self.name}', "
                f"start_time={self.start_time}, stop_time={self.stop_time}, "
                f"channel_configurations={self.channel_configurations})")

class AromaBlockModel(Base):
    """
    SQLAlchemy model for the 'sl_aromablocks' database table, storing AromaBlock information.
    """
    __tablename__ = 'sl_aromablocks' # Имя таблицы для аромаблоков
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    data_type = Column(String)
    content_link = Column(String)
    channel_configurations = Column(JSON) # Храним как JSON
    start_time = Column(Float)  # Новое поле для хранения времени начала (в секундах)
    stop_time = Column(Float)   # Новое поле для хранения времени окончания (в секундах)

    aroma_track_id = Column(Integer, ForeignKey('aroma_tracks.id')) #  ForeignKey to aroma_tracks table
    aroma_track = relationship("AromaTrackModel", back_populates="aromablocks") #  Обратная связь

    def __repr__(self) -> str:
        return (f"<AromaBlockModel(id={self.id}, name='{self.name}', "
                f"start_time={self.start_time}, stop_time={self.stop_time})>")
        
if __name__ == '__main__':
    block = AromaBlock(name="Test Block", start_time=10.5, stop_time=20.0, channel_configurations={"1": {"on_tick": 100}})
    print("AromaBlock instance:", block)