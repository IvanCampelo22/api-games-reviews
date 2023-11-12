from httpx import AsyncClient
import pytest
from fastapi.testclient import TestClient
from main import app
from app.models.released_last_month_plataform_models import ReleasedGamesLastMonthPlataform
import os

bearer = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiaXZhbmNhbXBlbG8xOTczQGdtYWlsLmNvbSIsImV4cGlyZXMiOjE2OTk2MTc0MTkuMTU1NjAzNH0.TfxGkDPJPZzxwFwsrCg8_c2frsRYPLVpDvZBHExbdtY'
 
headers = {"Authorization": f"Bearer {bearer}"}

client = TestClient(app)

API_KEY = os.getenv("API_KEY_RAWG")

@pytest.mark.asyncio
async def test_status_code_200_released_last_month_plataform():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/") as ac:
        response = await ac.get(f"games/released-last-month-pataform/?start_date=2019-01-01&end_date=2019-12-31&plataform_id=1", headers=headers)
    assert response.status_code == 200
    assert response.json() == {'message': 'dados inseridos com sucesso'}