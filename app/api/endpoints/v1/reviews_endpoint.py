from app.schemas.reviews_schema import ReviewCreate
from app.models.reviews_models import Reviews
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import token_required, format_jwt
from fastapi import Depends, HTTPException,status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from database import conn
from sqlalchemy.future import select
from jose import jwt
from datetime import datetime
from typing import List
from sqlalchemy.orm import joinedload
from database.conn import async_session
from loguru import logger


router=APIRouter()

@token_required
@async_session
@router.post("/create-review", responses={
    201: {
        "description": "Review criada com sucesso!",
        "content": {
            "application/json": {
                "example": [
                    {   
                        "game": "World Of Warcraft",
                        "rate": "Muito Bom",
                        "text_review": "É um jogo com um mundo aberto incrível!",
                    }
                ]
            }
        },
        400: {"description": "Insira dados válidos"}
}},  status_code=status.HTTP_201_CREATED)
async def create_reviews(review: ReviewCreate, dependencies=Depends(JWTBearer()), session: AsyncSession = Depends(conn.get_async_session)):
    try:
        decoded_payload = format_jwt(dependencies)
        user = decoded_payload.get('sub') 

        result = await session.execute(select(Reviews).where(Reviews.user_id == int(user), Reviews.game == review.game, Reviews.rate == review.rate, Reviews.text_review == review.text_review))
        existing_review = result.scalar()
        
        if existing_review:
            await session.rollback() 
            return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Você já escreveu uma avaliação igual para esse jogo")                 

        new_review = Reviews(user_id=int(user), game=review.game, rate=review.rate, text_review=review.text_review)
        
        if not new_review.game or not new_review.rate: 
            await session.rollback()
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Insira informações válidas")
        
        session.add(new_review)
        await session.commit()

        return new_review

    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}')
    


@async_session
@router.get("/list-reviews", status_code=status.HTTP_200_OK)
async def list_reviews( session: AsyncSession = Depends(conn.get_async_session)):
    try: 
        query = select(Reviews)
        result = await session.execute(query)
        result = result.unique()
        reviews: List[ReviewCreate] = result.scalars().all()

        return reviews
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e}')