from fastapi.routing import APIRouter
from form.api.endpoints.v1 import forms_endpoints

api_router = APIRouter()

api_router.include_router(forms_endpoints.router, prefix='/teste', tags=['testes'])
