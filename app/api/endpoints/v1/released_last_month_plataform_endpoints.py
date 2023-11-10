from fastapi import Depends, APIRouter, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from app.auth.auth_bearer import JWTBearer
from app.models.released_last_month_plataform_models import ReleasedGamesLastMonthPlataform
from core.connection_api import ApiGames
from database import conn
from database.conn import async_session

router = APIRouter()
api = ApiGames()

@async_session
@router.get("/released-last-month-pataform/", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_200_OK)
async def get_released_last_month(session: AsyncSession = Depends(conn.get_async_session), start_date: str = '', end_date: str = '', plataform_id: str = ''):
    try:
        response = api.get_released_last_month_plataform(start_date=start_date, end_date=end_date, plataform_id=plataform_id).json()
        logger.info('Dados buscados na API ReleasedLastMonthPlataform')

        for game in response['results']:
            logger.info('Inserindo dados no banco de dados ReleasedLastMonthPlataform')    

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

            
            new_platform = ReleasedGamesLastMonthPlataform(**game_data)
            session.add(new_platform)
            
        await session.commit()
        logger.info('Dados inseridos com sucesso')
        return {'message': 'dados inseridos com sucesso'}

    except Exception as e:
        print(e)
        await session.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor")