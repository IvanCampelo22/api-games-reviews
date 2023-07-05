from pydantic import BaseModel

class ReleasedGamesLastMonthSchema(BaseModel):
    id: int
    plataform_id: int
    name_plataform: str 
    slug_plataform: str
    games_count: int
    image_backgroud: str
    image: str
    year_start: int
    year_end: int
    game_id: int
    game_slug: str
    game_name: str

    class Config:
        orm_mode = True