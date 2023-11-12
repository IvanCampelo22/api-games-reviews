import pytest
import os
from fastapi.testclient import TestClient
import os

from main import app

client = TestClient(app)

API_KEY = os.getenv("API_KEY_RAWG")

def test_released_last_month_message():

    response = client.get(f"games/released-last-month-pataform?key={API_KEY}")

    assert response.status_code == 200
    assert response.json() == {"message": "Dados inseridos com sucesso"}