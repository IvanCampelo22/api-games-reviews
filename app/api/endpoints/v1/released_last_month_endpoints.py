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
@router.get("/released-last-month/", status_code=status.HTTP_200_OK)
async def get_released_last_month(session: AsyncSession = Depends(conn.get_async_session)):
    try:
        query = select(ReleasedGamesLastMonth)
        results = await session.execute(query)
        released_last_month = results.scalars().all()
        response = api.get_released_last_month()
        response_json = response.json()
        logger.info('Dados buscados na API')

        for platform in response_json['results']:
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
    

@async_session
@router.get("/released-last-month-pataform/", status_code=status.HTTP_200_OK)
async def get_released_last_month(session: AsyncSession = Depends(conn.get_async_session), date: str = '', plataform_id: str = ''):
    try:
        query = select(ReleasedGamesLastMonthPlataform)
        results = await session.execute(query)
        released_last_month = results.scalars().all()
        response = api.get_released_last_month()
        response_json = response.json()
        logger.info('Dados buscados na API')

        for game in response_json['results']:
            logger.info('Inserindo dados no banco de dados')    

            game_data = {
                'slug_name': game['slug'],
                'name_game': game['name'],
                'playtime': game['playtime'],
            }

            for plataform in game['plataforms']:
                plataform_data_id = plataform['platform']

                plataform_data = {
                    'plataform_id': plataform_data_id['id'],
                    'plataform_name': plataform_data_id['name'],
                    'plataform_slug': plataform_data_id['slug'],
                }
                game_data.update(plataform_data)
                
                new_platform = ReleasedGamesLastMonth(**game_data)
                session.add(new_platform)
            
        await session.commit()
        logger.info('Dados inseridos com sucesso')
        return {'message': 'Dados inseridos com sucesso'}

    except Exception as e:
        print(e)
        await session.rollback()
        raise HTTPException(status_code=500, detail="Erro interno do servidor", )