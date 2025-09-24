# smeller/models/aroma_track.py

from dataclasses import dataclass, field
from typing import List, Optional
from .aroma_block import AromaBlock
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
@dataclass
class AromaTrack:
    """
    Data class representing an Aroma Track, which is a sequence of AromaBlock instances.
    
    Attributes:
        name (str): The name of the aroma track.
        description (Optional[str]): An optional text description of the track.
        aromablocks (List[AromaBlock]): A list of AromaBlock objects forming the track.
                                     Defaults to an empty list.
    """
    name: str = ""
    description: Optional[str] = None
    aromablocks: List[AromaBlock] = field(default_factory=list)

    def __repr__(self) -> str:
        return (f"AromaTrack(name='{self.name}', description='{self.description}', "
                f"aromablocks={self.aromablocks})")
        
class AromaTrackModel(Base):
    """
    SQLAlchemy model for the 'aroma_tracks' database table, storing AromaTrack information.
    """
    __tablename__ = 'aroma_tracks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text) #  Используем Text вместо String для длинных описаний

    aromablocks = relationship("AromaBlockModel", back_populates="aroma_track") #  One-to-many relationship

    def __repr__(self):
        return f"<AromaTrackModel(id={self.id}, name='{self.name}')>"
    
if __name__ == '__main__':
    # Пример быстрого теста класса AromaTrack
    track = AromaTrack(name="Sample Track", description="A simple test track")
    print("AromaTrack:", track)