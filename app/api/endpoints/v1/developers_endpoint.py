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
            logger.info('Inserindo dados no banco de dados')

            developer_data = {
                'developer_id': developer['id'],
                'text': developer['text'],
                'developer_name': developer['name'],
                'exact_name': developer['exact_name'],
                'search_name': developer['search_name'],
                'developer_slug': developer['slug'],
                'top_games': developer['top_games'],
                'games_count': developer['games_count'],
                'image_background': developer['image_background'],
                'score': developer['score']
            }

            new_developer = Developers(**developer_data)
            session.add(new_developer)

        await session.commit()
        logger.info('Dados inseridos com sucesso')
        return new_developer
    
    except Exception as e:
        await session.rollback()
        logger.error(f'Erro ao inserir dados: {e}')
        return {'message': 'Erro ao inserir dados'}