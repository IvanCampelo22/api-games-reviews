from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

import pytest

from database.conn import Base
from app.models.released_last_month_models import ReleasedGamesLastMonth
from app.tests.conftest import async_session


@pytest.mark.asyncio
async def test_released_games_last_month(async_session):
    async with get_async_session(async_session) as session:
        game = ReleasedGamesLastMonth(
            plataform_id=1,
            name_plataform="Plataform 1",
            slug_plataform="plataform-1",
            games_count=10,
            image_background="background.jpg",
            image="game.jpg",
            year_start=2022,
            year_end=2023,
            game_id=1,
            game_slug="game-1",
            game_name="Game 1"
        )

        session.add(game)
        await session.commit()

        assert game.id is not None
        assert game.plataform_id == 1
        assert game.name_plataform == "Plataform 1"
        assert game.slug_plataform == "plataform-1"
        assert game.games_count == 10
        assert game.image_background == "background.jpg"
        assert game.image == "game.jpg"
        assert game.year_start == 2022
        assert game.year_end == 2023
        assert game.game_id == 1
        assert game.game_slug == "game-1"
        assert game.game_name == "Game 1"

async def get_async_session(async_session):
    async with async_session() as session:
        yield session
        await session.rollback()
        await session.close()