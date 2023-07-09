from pydantic import BaseModel

class ReleasedGamesLastMonthSchemaMonth(BaseModel):
    id: int
    slug_game: str 
    name_game: str 
    playtime: int 
    plataform_id: int
    plataform_name: str
    plataform_slug: str
