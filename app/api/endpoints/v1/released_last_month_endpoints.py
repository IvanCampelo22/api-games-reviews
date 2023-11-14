from fastapi import Depends, APIRouter, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from core.connection_api import ApiGames
from database import conn
from database.conn import async_session

router = APIRouter()
api = ApiGames()

@async_session
@router.get("/released-last-month/", status_code=status.HTTP_200_OK)
async def get_released_last_month(session: AsyncSession = Depends(conn.get_async_session)):
    try:
        response = api.get_released_last_month().json()
        logger.info('Buscando dados na API')

        for platform in response['results']:
            logger.success('Sucesso')
            return platform

    except Exception as e:
        await session.rollback()
        logger.error(f'Erro ao inserir dados: {e}')
        return {'message': 'Erro ao inserir dados'}
    