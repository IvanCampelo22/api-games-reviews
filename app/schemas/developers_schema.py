from pydantic import BaseModel

class DevelopersSchema(BaseModel):
    id: int
    developer_id: int
    text: str
    developer_name: str
    exact_name: str
    search_name: str
    developer_slug: str
    top_games: list
    games_count: int
    image_background: str
    score: str
