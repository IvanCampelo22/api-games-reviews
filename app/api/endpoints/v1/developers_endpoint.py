from fastapi import Depends, APIRouter, status

from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from app.auth.auth_handler import token_required
from app.auth.auth_bearer import JWTBearer
from database.conn import async_session
from database import conn
from core.connection_api import ApiGames

router = APIRouter()
api = ApiGames()

@async_session
@token_required
@router.get("/developers/", status_code=status.HTTP_200_OK)
async def get_developers(dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(conn.get_async_session), developer_name: str = ''):
    try:       
        response = api.get_developers(developer_name).json()
        logger.info('Buscando dados na API')

        for developer in response['results']:
            logger.success('Sucesso')
            return developer
    
    except Exception as e:
        await session.rollback()
        logger.error(f'Erro ao resgatar dados: {e}')
        return {'message': 'Erro ao resgatar dados'}