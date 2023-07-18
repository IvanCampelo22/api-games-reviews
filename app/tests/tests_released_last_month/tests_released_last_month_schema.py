import pytest
from pydantic import ValidationError

from app.schemas.released_last_month_schemas import ReleasedGamesLastMonthSchema

def test_valid_released_games_last_month_schema():
    data = {
        "id": 1,
        "plataform_id": 1,
        "name_plataform": "PC",
        "slug_plataform": "Pc",
        "games_count": 10,
        "image_backgroud": "image_background",
        "image": "image_test",
        "year_start": 1,
        "year_end": 1,
        "game_id": 1,
        "game_slug": "Resident Evil",
        "game_name": "resident evil"



    }

    assert ReleasedGamesLastMonthSchema(**data)
