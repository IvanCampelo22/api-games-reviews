from app.schemas.user_schema import UserCreate, TokenSchema, requestdetails
from app.models.users_models import User, TokenTable
from database.conn import Base, engine, AnsyncSessionLocal
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth.auth_handler import get_hashed_password, create_access_token,create_refresh_token,verify_password
from fastapi import FastAPI, Depends, HTTPException,status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from database import conn
from sqlalchemy.future import select


ACCESS_TOKEN_EXPIRE_MINUTES = 30 
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 
ALGORITHM = "HS256"
JWT_SECRET_KEY = "narscbjim@$@&^@&%^&RFghgjvbdsha"
JWT_REFRESH_SECRET_KEY = "13ugfdfgh@#$%^@&jkl45678902"

router=APIRouter()

@router.post("/register")
async def register_user(user: UserCreate, session: AsyncSession = Depends(conn.get_async_session)):
    result = await session.execute(select(User).where(User.email == user.email))
    existing_user = result.scalar()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    encrypted_password = get_hashed_password(user.password)

    new_user = User(username=user.username, email=user.email, password=encrypted_password )

    session.add(new_user)
    await session.commit()

    return {"message":"user created successfully"}

@router.post('/login' ,response_model=TokenSchema)
async def login(request: requestdetails, session: AsyncSession = Depends(conn.get_async_session)):
    result = await session.execute(select(User).where(User.email == request.email))
    user = result.scalar()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
    hashed_pass = user.password
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    
    access=create_access_token(user.id)
    refresh = create_refresh_token(user.id)

    token_db = TokenTable(user_id=user.id,  access_toke=access,  refresh_toke=refresh, status=True)
    session.add(token_db)
    await session.commit()

    return {
        "access_token": access,
        "refresh_token": refresh,
    }

from typing import List

@router.get('/getusers', response_model=List[UserCreate])
async def getusers(db: AsyncSession = Depends(conn.get_async_session)):
    async with db as session:
        query = select(User)
        result = await session.execute(query)
        user: List[UserCreate] = result.scalars().unique().all()

        return user
