from sqlalchemy import Integer, Float, Column, String, Date, Boolean
from database.conn import Base 

class DevelopersWithId(Base):
    __tablename__ = "DevelopersWithId"

    id = Column(Integer, primary_key=True, index=True)
    slug_game = Column(String, nullable=True)
    name_game = Column(String, nullable=True)
    playtime = Column(Integer, nullable=True)
    plataform_id = Column(Integer, nullable=True)
    plataform_name = Column(String, nullable=True)
    plataform_slug = Column(String, nullable=True)
    store_id = Column(Integer, nullable=True)
    store_name = Column(String, nullable=True)
    store_slug = Column(String, nullable=True)
    released_game = Column(String, nullable=True)
    tba_game = Column(Boolean, nullable=True)
    background_image_game = Column(String, nullable=True)
    rating_game = Column(Float, nullable=True)
    rating_top_game = Column(Integer, nullable=True)
    ratings_id = Column(Integer, nullable=True)
    ratings_title = Column(String, nullable=True)
    ratings_counts = Column(Integer, nullable=True)
    ratings_percent = Column(Float, nullable=True)
    ratings_count = Column(Integer, nullable=True)
    reviews_text_count = Column(Integer, nullable=True)
    added = Column(Integer, nullable=True)
    yet_add_by_status = Column(Integer, nullable=True)
    owned_add_by_status = Column(Integer, nullable=True)
    beaten_add_by_status = Column(Integer, nullable=True)
    toplay_add_by_status = Column(Integer, nullable=True)
    dropped_add_by_status = Column(Integer, nullable=True)
    playing_add_by_status = Column(Integer, nullable=True)
    metacritic = Column(Integer, nullable=True)
    suggestions_count = Column(Integer, nullable=True)
    updated = Column(String, nullable=True)
    metacritic_id = Column(Integer, nullable=True)
    metacritic_score = Column(Integer, nullable=True)
    clip = Column(Boolean, nullable=True)
    tags_metacritic_id = Column(Integer, nullable=True)
    tags_metacritic_name = Column(String, nullable=True)
    tags_metacritic_slug = Column(String, nullable=True)
    tags_metacritic_language = Column(String, nullable=True)
    tags_games_count = Column(Integer, nullable=True)
    tags_image_background = Column(String, nullable=True)
    esrb_rating_id = Column(Integer, nullable=True)
    esrb_rating_name = Column(String, nullable=True)
    esrb_rating_slug = Column(String, nullable=True)
    esrb_rating_name_en = Column(String, nullable=True)
    esrb_rating_name_ru = Column(String, nullable=True)
    user_game = Column(String, nullable=True)
    reviews_count = Column(Integer, nullable=True)
    saturated_color = Column(String, nullable=True)
    dominant_color = Column(String, nullable=True)
    short_screenshots_id = Column(Integer, nullable=True)
    short_screenshots_image = Column(String, nullable=True)
    parent_plataforms_id = Column(Integer, nullable=True)
    parent_plataforms_name = Column(String, nullable=True)
    parent_plataforms_slug = Column(String, nullable=True)
    genres_id = Column(Integer, nullable=True)
    genres_name = Column(String, nullable=True)
    genres_slug = Column(String, nullable=True)