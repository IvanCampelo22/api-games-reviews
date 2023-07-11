from sqlalchemy import Column, Integer, String

from database.conn import Base

class ReleasedGamesLastMonthPlataform(Base):
    __tablename__ = "ReleasedGamesLastMonthPlataform"

    id = Column(Integer, primary_key=True, index=True)
    slug_game = Column(String, nullable=True)
    name_game = Column(String, nullable=True)
    playtime = Column(Integer, nullable=True)
    plataform_id = Column(Integer, nullable=True)
    plataform_name = Column(String, nullable=True)
    plataform_slug = Column(String, nullable=True)
