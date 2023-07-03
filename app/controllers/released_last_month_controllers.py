from sqlalchemy.orm import Session
from app.models.released_last_month_models import ReleasedGamesLastMonth

class ReleasedGamesLastMonthControllers():

    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    async def released_last_month(db: Session):
        return db.query(ReleasedGamesLastMonth).all()