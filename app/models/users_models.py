from sqlalchemy import Integer, Boolean, Date, String, Column
from database.conn import Base 
from datetime import datetime


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(length=340), nullable=False)
    username = Column(String(length=120), unique=True, nullable=False)
    email = Column(String(240), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)
    created_at = Column(Date, default=datetime.now())