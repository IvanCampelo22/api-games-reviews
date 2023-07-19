import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os

USER = os.getenv('USER_GAMES')
PASSWORD = os.getenv('PASSWORD_GAMES')
HOST = os.getenv('HOST_GAMES')
NAME = os.getenv('NAME_GAMES')

@pytest.fixture
async def async_session():

    SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}/{NAME}"

    engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)
    async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, future=True)

    async with async_session() as session:
        yield session
        await session.rollback()
        await session.close()