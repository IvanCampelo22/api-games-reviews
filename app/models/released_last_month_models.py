from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.conn import Base



class ReleasedGamesLastMonthModels(Base):
    __tablename__ = "ReleasedGamesLastMonth"

    plataform_id = Column(Integer, primary_key=True, index=True)
    name_plataform = Column(String, nullable=True)
    slug_plataform = Column(String, nullable=True)
    games_count = Column(Integer, nullable=True)
    image_background = Column(String, nullable=True)
    image = Column(String, nullable=True)
    year_start = Column(Integer, nullable=True)
    year_end = Column(Integer, nullable=True)
    game_id = Column(Integer, nullable=True)
    game_slug = Column(String, nullable=True)
    game_name = Column(String, nullable=True)


