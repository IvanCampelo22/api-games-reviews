from fastapi.routing import APIRouter
from app.api.endpoints.v1 import released_last_month_endpoints, released_last_month_plataform_endpoints
api_router = APIRouter()

api_router.include_router(released_last_month_endpoints.router, prefix='/games', tags=['released_last_month'])
api_router.include_router(released_last_month_plataform_endpoints.router, prefix='/games', tags=['released_last_month_plataform'])