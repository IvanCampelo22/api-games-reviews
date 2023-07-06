from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.conn import Base

class ReleasedLastMonthPlataform(Base):
    __tablename__ = "ReleasedLastMonthPlataform"

    id = Column(Integer, primary_key=True, index=True)
    slug_game = Column(String, nullable=True)
    name_game = Column(String, nullable=True)
    playtime = Column(Integer, nullable=True)
    plataform_id = Column(Integer, nullable=True)
    plataform_name = Column(String, nullable=True)
    plataform_slug = Column(String, nullable=True)
