import pytest
import os
from fastapi.testclient import TestClient
import os

from main import app

client = TestClient(app)

API_KEY = os.getenv("API_KEY_RAWG")

def test_released_last_month_plataform_endpoint():

    response = client.get(f"games/released-last-month-pataform/?start_date=2019-01-01&end_date=2019-01-30&plataform_id=7&key={API_KEY}")

    assert response.status_code == 200
    assert response.json() == {"message": "Dados inseridos com sucesso"}
