from database.conn import async_session
from sqlalchemy.future import select
from app.models.released_last_month_models import ReleasedGamesLastMonthModels

@async_session
async def fetch_categories(session):
    stat = select(ReleasedGamesLastMonthModels)
    print(stat)
    result = async_session.execute(stat)
    return result.scalars().all()