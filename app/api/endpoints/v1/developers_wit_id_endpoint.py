from fastapi import Depends, APIRouter, status

from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from app.auth.auth_handler import token_required
from app.auth.auth_bearer import JWTBearer
from core.connection_api import ApiGames
from database.conn import async_session
from database import conn

router = APIRouter()
api = ApiGames()

@async_session
@token_required
@router.get("/developers_with_id/", status_code=status.HTTP_200_OK)
async def get_developers_with_id(dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(conn.get_async_session), start_date: str = '', end_date: str = '', developer_id: str = ''):
    try:
        response = api.get_developers_with_id(start_date=start_date, end_date=end_date, developer_id=developer_id).json()
        logger.info('Buscando dados na API')

        for developer in response['results']:
            logger.success('Sucesso')
            return developer

    except Exception as e:
        await session.rollback()
        logger.error(f'Erro ao inserir dados: {e}')
        return {'message': 'Erro ao inserir dados'}

