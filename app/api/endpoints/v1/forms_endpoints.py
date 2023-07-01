from fastapi import APIRouter
from loguru import logger


router = APIRouter()

@router.get("/")
async def root():
    logger.success('Hello World')
    return {"message": "Hello World"}