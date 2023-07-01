from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.conn import Base


class ReleasedGameLastMonth(Base):
    __tablename__ = "users"

    id_plataform = Column(Integer, primary_key=True, index=True)
    name_plataform = Column(String, nullable=True)
    slug_plataform = Column(String, nullable=True)
    games_count = Column(Integer, nullable=True)
    image_background = Column(String, nullable=True)
    image = Column(String, nullable=True)
    year_start = Column(Integer, nullable=True)