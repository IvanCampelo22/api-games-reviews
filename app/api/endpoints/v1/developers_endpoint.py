from fastapi import Depends, APIRouter, status

from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from database.conn import async_session
from database import conn
from app.auth.auth_bearer import JWTBearer
from app.models.developers_models import Developers
from core.connection_api import ApiGames

router = APIRouter()
api = ApiGames()

@async_session
@router.get("/developers/", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
async def get_developers(session: AsyncSession = Depends(conn.get_async_session), developer_name: str = ''):
    try:       
        response = api.get_developers(developer_name).json()
        logger.info('Dados buscados na API')

        for developer in response['results']:
    
            return developer
    
    except Exception as e:
        await session.rollback()
        logger.error(f'Erro ao inserir dados: {e}')
        return {'message': 'Erro ao inserir dados'}