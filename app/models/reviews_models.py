from sqlalchemy import Column, Integer, String, DateTime,Boolean, Enum
from sqlalchemy.schema import ForeignKey
from database.conn import Base
import datetime
from sqlalchemy.orm import relationship
from app.models.users_models import User

class Reviews(Base):
    __tablename__ = 'Reviews'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    game = Column(String(320), nullable=False)
    rate = Column(Enum("Péssimo", "Ruim", "Regular", "Bom", "Muito Bom", name="rate_enum"), nullable=False)
    text_review = Column(String, nullable=True)
    updated_at = Column(DateTime, default=datetime.datetime.now())
    created_at = Column(DateTime, default=datetime.datetime.now())

    user = relationship('User', back_populates='review')