from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from core.connection_api import ApiGames
from app.models.upcoming_games_models import UpcomingGames
from database import conn
from database.conn import async_session

router = APIRouter()
api = ApiGames()

@async_session
@router.get("/upcoming-games/", status_code=status.HTTP_200_OK)
async def upcoming_games(session: AsyncSession = Depends(conn.get_async_session), start_date: str = '', end_date: str = ''):
    try:
        
        response = api.get_upcoming_games(start_date=start_date, end_date=end_date).json()
        logger.info('Buscando dados na API')

        for game in response['results']:
            logger.success('Sucesso')
            return game

    except Exception as e:
        await session.rollback()
        logger.error(f'Erro ao inserir dados: {e}')
        return {'message': 'Erro ao inserir dados'}