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
@router.get("/developers_with_id/", status_code=status.HTTP_200_OK)
async def get_developers_with_id(session: AsyncSession = Depends(conn.get_async_session), start_date: str = '', end_date: str = '', developer_id: str = ''):
    try:
        response = api.get_developers_with_id(start_date=start_date, end_date=end_date, developer_id=developer_id).json()
        if response and 'results' in response:
            logger.info(f'Response from API: {response}')

            for developer in response['results'] if 'results' in response else None:
                logger.info(f'Developer data: {developer}')

                developer_with_id_data = {
                    'slug_game': developer['slug'] if 'slug' in developer else None,
                    'name_game': developer['name'] if 'name' in developer else None,
                    'released_game': developer['released'] if 'released' in developer else None,
                    'tba_game': developer['tba'] if 'tba' in developer else None,
                    'background_image_game': developer['background_image'] if 'background_image' in developer else None,
                    'rating_game': developer['rating'] if 'rating' in developer else None,
                    'rating_top_game': developer['rating_top'] if 'rating_top' in developer else None,
                    'ratings_counts': developer['ratings_count'] if 'ratings_count' in developer else None,
                    'reviews_text_count': developer['reviews_text_count'] if 'reviews_text_count' in developer else None,
                    'added': developer['added'] if 'added' in developer else None,
                    'yet_add_by_status': developer['added_by_status']['yet'] if 'yet' in developer['added_by_status'] else None,
                    'owned_add_by_status': developer['added_by_status']['owned'] if 'owned' in developer['added_by_status'] else None,
                    'beaten_add_by_status': developer['added_by_status']['beaten'] if 'beaten' in developer['added_by_status'] else None,
                    'toplay_add_by_status': developer['added_by_status']['toplay'] if 'toplay' in developer['added_by_status'] else None,
                    'dropped_add_by_status': developer['added_by_status']['dropped'] if 'dropped' in developer['added_by_status'] else None,
                    'playing_add_by_status': developer['added_by_status']['playing'] if 'playing' in developer['added_by_status'] else None,
                    'metacritic': developer['metacritic'] if 'metacritic' in developer else None,
                    'suggestions_count': developer['suggestions_count'] if 'suggestions_count' in developer else None,
                    'updated': developer['updated'] if 'updated' in developer else None,
                    'metacritic_id': developer['id'] if 'id' in developer else None,
                    'metacritic_score': developer['score'] if 'score' in developer else None,
                    'clip': developer['clip'] if 'clip' in developer else None,
                    'esrb_rating_id': developer['esrb_rating']['id'] if 'id' in developer['esrb_rating'] else None,
                    'esrb_rating_name': developer['esrb_rating']['name'] if 'name' in developer['esrb_rating'] else None,
                    'esrb_rating_slug': developer['esrb_rating']['slug'] if 'slug' in developer['esrb_rating'] else None,
                    'esrb_rating_name_en': developer['esrb_rating']['name_en'] if 'name_en' in developer['esrb_rating'] else None,
                    'esrb_rating_name_ru': developer['esrb_rating']['name_ru'] if 'name_ru' in developer['esrb_rating'] else None,
                    'user_game': developer['user_game'] if 'user_game' in developer else None,
                    'reviews_count': developer['reviews_count'] if 'reviews_count' in developer else None,
                    'saturated_color': developer['saturated_color'] if 'saturated_color' in developer else None,
                    'dominant_color': developer['dominant_color'] if 'dominant_color' in developer else None

                }

                for plataforms in developer['platforms'] if plataforms in developer else None:
                    plataform_data = {
                        'plataform_id': plataforms['platform']['id'] if 'id' in plataforms['platform'] else None,
                        'plataform_name': plataforms['platform']['name'] if 'name' in plataforms['platform'] else None,
                        'plataform_slug': plataforms['platform']['slug'] if 'slug' in plataforms['platform'] else None
                    }

                    developer_with_id_data.update(**plataform_data)
                
                for stores in developer['stores'] if stores in developer else None:
                    stores_data = {
                        'store_id': stores['store']['id'] if 'id' in stores['store'] else None,
                        'store_name': stores['store']['name']if 'name' in stores['store'] else None,
                        'store_slug': stores['store']['slug'] if 'slug' in stores['store'] else None
                    }

                    developer_with_id_data.update(**stores_data)

                for ratings in developer['ratings'] if ratings in developer else None:
                    ratings_data = {
                        'ratings_id': ratings['id'] if 'id' in ratings else None,
                        'ratings_title': ratings['title'] if 'title' in ratings else None,
                        'ratings_count': ratings['count'] if 'count' in ratings else None,
                        'ratings_percent': ratings['percent'] if 'percent' in ratings else None,
                    }

                    developer_with_id_data.update(**ratings_data)

                for tags in developer['tags'] if tags in developer else None:
                    tags_data = {
                        'tags_metacritic_id': tags['id'] if 'id' in tags else None,
                        'tags_metacritic_name': tags['name'] if 'name' in tags else None,
                        'tags_metacritic_slug': tags['slug'] if 'slug' in tags else None,
                        'tags_metacritic_language': tags['language'] if 'language' in tags else None,
                        'tags_games_count': tags['games_count'] if 'games_count' in tags else None,
                        'tags_image_background': tags['image_background'] if 'image_background' in tags else None 
                        
                    }

                    developer_with_id_data.update(**tags_data)

                for short_screenshots in developer['short_screenshots'] if 'short_screenshots' in developer else None:
                    short_screenshots_data = {
                        'short_screenshots_id': short_screenshots['id'] if 'id' in short_screenshots else None,
                        'short_screenshots_image': short_screenshots['image'] if 'image' in short_screenshots else None
                    }

                    developer_with_id_data.update(**short_screenshots_data)

                for parent_plataforms in developer['parent_platforms'] if parent_plataforms in developer else None:
                    parent_plataform_data = {
                        'parent_plataforms_id': parent_plataforms['platform']['id'] if 'id' in parent_plataforms['platform'] else None,
                        'parent_plataforms_name': parent_plataforms['platform']['name'] if 'name' in parent_plataforms['platform'] else None,
                        'parent_plataforms_slug': parent_plataforms['platform']['slug'] if 'platform' in parent_plataforms and 'slug' in parent_plataforms['platform'] else None
                    }

                    developer_with_id_data.update(**parent_plataform_data)

                for genres in developer['genres'] if genres in developer else None:
                    genres_data = {
                        'genres_id': genres['id'] if 'id' in genres else None,
                        'genres_name': genres['name'] if 'name' in genres else None,
                        'genres_slug': genres['slug'] if 'slug' in genres else None
                    }

                    developer_with_id_data.update(**genres_data)
                
                with_id = DevelopersWithId(**developer_with_id_data)
                session.add(with_id)

            await session.commit()
            logger.info('Dados inseridos com sucesso')
            return {'message': 'dados inseridos com sucesso'}
    
        else:
            logger.error('Resposta inválida da API')
            return {'message': 'Resposta inválida da API'}

    except Exception as e:
        await session.rollback()
        logger.error(f'Erro ao inserir dados: {e}')
        return {'message': 'Erro ao inserir dados'}

