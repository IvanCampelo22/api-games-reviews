from fastapi import Depends, APIRouter, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from app.models.released_last_month_models import ReleasedGamesLastMonth
from app.auth.auth_bearer import JWTBearer
from core.connection_api import ApiGames
from database import conn
from database.conn import async_session

router = APIRouter()
api = ApiGames()

@async_session
@router.get("/released-last-month/", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
async def get_released_last_month(session: AsyncSession = Depends(conn.get_async_session)):
    try:
        response = api.get_released_last_month().json()
        logger.info('Dados buscados na API')

        for platform in response['results']:
            logger.info('Inserindo dados no banco de dados')

            platform_data = {
                'plataform_id': platform['id'],
                'name_plataform': platform['name'],
                'slug_plataform': platform['slug'],
                'games_count': platform['games_count'],
                'image_background': platform['image_background'],
                'image': platform['image'],
                'year_start': platform['year_start'],
                'year_end': platform['year_end'],
            }

            for game in platform['games']:
                game_data = {
                    'game_id': game['id'],
                    'game_slug': game['slug'],
                    'game_name': game['name'],
                }
                platform_data.update(game_data)
                
                new_platform = ReleasedGamesLastMonth(**platform_data)
                session.add(new_platform)


        await session.commit()
        logger.info('Dados inseridos com sucesso')
        return {'message': 'Dados inseridos com sucesso'}

    except Exception as e:
        print(e)
        await session.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor", )
    