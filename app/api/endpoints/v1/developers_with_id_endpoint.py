from fastapi import Depends, APIRouter, HTTPException, status

from database.conn import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.developers_with_id_models import DevelopersWithId
from core.connection_api import ApiGames
from loguru import logger

from database import conn

router = APIRouter()

api = ApiGames()

@async_session
@router.get("/developers-with-id/", status_code=status.HTTP_200_OK)
async def developers_with_id(session: AsyncSession = Depends(conn.get_async_session), start_date: str ='', end_date: str = '', developer_id: str = ''):
    try:
        query = select(DevelopersWithId)
        results = await session.execute(query)
        devs_with_id =  results.scalars().all()
        response = api.get_developers_with_id(start_date=start_date, end_date=end_date, developer_id=developer_id)
        response_json = response.json()
        logger.info("Dados buscados na api")

        for games in response_json['results']:
            logger.info("Inserindo no banco de dados")

            games_data = {
                'slug_game': games['slug'],
                'name_game': games['name'],
                'playtime': games['playtime']

            }

            new_developer_with_id = DevelopersWithId(**games_data)
            session.add(new_developer_with_id)

        await session.commit()
        logger.info('Dados inseridos com sucesso')
        return {'message': f'Dados inseridos com sucesso'}
        
    except Exception as e:
        await session.rollback()
        logger.error(f'Erro ao inserir dados: {e}')
        return {'message': f'Erro ao inserir dados {e}'}