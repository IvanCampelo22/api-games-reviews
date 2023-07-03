from sqlalchemy.orm import Session

from app.models.released_last_month_models import ReleasedGamesLastMonthModels

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ReleasedGamesLastMonthModels).offset(skip).limit(limit).all()