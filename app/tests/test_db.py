import pytest
from sqlalchemy.orm import sessionmaker
from database.conn import Base
import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

USER = os.getenv('USER_GAMES')
PASSWORD = os.getenv('PASSWORD_GAMES')
HOST = os.getenv('HOST_GAMES')
NAME = os.getenv('NAME_GAMES')

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}/{NAME}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession)

@pytest.fixture(scope="function")
async def test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with SessionLocal() as session:
        transaction = await session.begin()
        yield
        await transaction.rollback()