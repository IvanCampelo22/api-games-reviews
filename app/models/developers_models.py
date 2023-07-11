from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database.conn import Base

class Developers(Base):
    __tablename__ = "Developers"

    id = Column(Integer, primary_key=True, index=True)
    developer_id = Column(Integer, nullable=True)
    text = Column(String, nullable=True)
    developer_name = Column(String, nullable=True)
    exact_name = Column(String, nullable=True)
    search_name = Column(String, nullable=True)
    developer_slug = Column(String, nullable=True)
    top_games = Column(String, nullable=True)
    games_count = Column(Integer, nullable=True)
    image_background = Column(String, nullable=True)
    score = Column(String, nullable=True)

