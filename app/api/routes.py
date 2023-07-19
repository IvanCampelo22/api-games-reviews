from fastapi.routing import APIRouter
from app.api.endpoints.v1 import released_last_month_endpoints, released_last_month_plataform_endpoints, upcoming_games_endpoints, developers_endpoint, developers_with_id_endpoint
api_router = APIRouter()

api_router.include_router(released_last_month_endpoints.router, prefix='/games', tags=['released_last_month'])
api_router.include_router(released_last_month_plataform_endpoints.router, prefix='/games', tags=['released_last_month_plataform'])
api_router.include_router(upcoming_games_endpoints.router, prefix='/games', tags=['upcoming_games'])
api_router.include_router(developers_endpoint.router, prefix='/games', tags=['developers'])
api_router.include_router(developers_with_id_endpoint.router, prefix='/games', tags=['developers_with_id'])