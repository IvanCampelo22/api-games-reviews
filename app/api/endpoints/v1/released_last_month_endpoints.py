from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import app.models
from app.schemas import released_last_month_schemas
from app.controllers import released_last_month_controllers
from database.conn import SessionLocal, engine

from database import conn

conn.Base.metadata.create_all(bind=engine)

router = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/", response_model=released_last_month_schemas.ReleasedGamesLastMonthSchema)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = released_last_month_controllers.get_users(db, skip=skip, limit=limit)
    return users




