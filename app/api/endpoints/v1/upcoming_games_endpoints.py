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
        logger.info('Dados buscados na API')

        for game in response['results']:
            logger.info('Inserindo dados no banco de dados')    

            game_data = {
                'slug_game': game['slug'],
                'name_game': game['name'],
                'playtime': game['playtime'],
            }

            for plataform in game['platforms']:
                plataform_data = {
                    'plataform_id': plataform['platform']['id'],
                    'plataform_name': plataform['platform']['name'],
                    'plataform_slug': plataform['platform']['slug'],
                }
                game_data.update(plataform_data)

            
            new_platform = UpcomingGames(**game_data)
            session.add(new_platform)
            
        await session.commit()
        logger.info('Dados inseridos com sucesso')
        return {'message': 'dados inseridos com sucesso'}

    except Exception as e:
        print(e)
        await session.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor", )