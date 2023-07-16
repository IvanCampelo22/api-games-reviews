from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.released_last_month_schemas import ReleasedGamesLastMonthSchema
from database.conn import async_session, engine, Base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.models.released_last_month_models import ReleasedGamesLastMonth
from app.models.released_last_month_plataform_models import ReleasedGamesLastMonthPlataform
from core.connection_api import ApiGames
from database.conn import AnsyncSessionLocal
from loguru import logger

from database import conn

router = APIRouter()

api = ApiGames()


@async_session
@router.get("/released-last-month-pataform/", status_code=status.HTTP_200_OK)
async def get_released_last_month(session: AsyncSession = Depends(conn.get_async_session), start_date: str = '', end_date: str = '', plataform_id: str = ''):
    try:
        query = select(ReleasedGamesLastMonthPlataform)
        results = await session.execute(query)
        released_last_month_plataform = results.scalars().all()
        response = api.get_released_last_month_plataform(start_date=start_date, end_date=end_date, plataform_id=plataform_id)
        response_json = response.json()
        logger.info('Dados buscados na API ReleasedLastMonthPlataform')

        for game in response_json['results']:
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
        return released_last_month_plataform

    except Exception as e:
        print(e)
        await session.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor")