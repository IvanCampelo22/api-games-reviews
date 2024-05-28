from sqlalchemy import Column, Integer, String, DateTime,Boolean
from sqlalchemy.sql.schema import ForeignKey
from database.conn import Base
import datetime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(50),  nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    review = relationship('Reviews', back_populates='user')

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

class TokenTable(Base):
    __tablename__ = "TokenTable"
    user_id = Column(Integer)
    access_toke = Column(String(450), primary_key=True)
    refresh_toke = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now)