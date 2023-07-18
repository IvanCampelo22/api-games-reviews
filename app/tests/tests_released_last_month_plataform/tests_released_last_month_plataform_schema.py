import pytest
from pydantic import ValidationError

from app.schemas.released_last_month_plataform_schemas import ReleasedGamesLastMonthSchemaMonthSchema

def test_valid_released_last_month_plataform():
    data = {
        "id": 1,
        "slug_game": "Diablo",
        "name_game": "diablo",
        "playtime": 10,
        "plataform_id": 12,
        "plataform_name": "PC",
        "plataform_slug": "Pc"
    
    }

    ReleasedGamesLastMonthSchemaMonthSchema(**data)


def test_invalid_released_last_month_plataform():
    invalid_data = {
        "slug_game": "Diablo",
        "name_game": "diablo",
        "playtime": 10,
        "plataform_id": 12,
        "plataform_name": "PC",
        "plataform_slug": "Pc"
    }

    with pytest.raises(ValidationError):
        ReleasedGamesLastMonthSchemaMonthSchema(**invalid_data)