from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:12345678@localhost/gamesreviews"


engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, future=True, echo=True)
AnsyncSessionLocal = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession, future=True)

Base = declarative_base()

async def get_async_session():
    async with AnsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

def async_session(func):
    async def wrapper(*args, **kwargs):
        async with get_async_session() as session:
            return await func(session, *args, **kwargs)
    return wrapper



