"""create table DevelopersWithId

Revision ID: d77d2c4312b6
Revises: da28ce378b7e
Create Date: 2023-07-17 22:17:48.483366

"""
from alembic import op
from sqlalchemy import Column, INTEGER, VARCHAR, DATE, FLOAT, BOOLEAN


# revision identifiers, used by Alembic.
revision = 'd77d2c4312b6'
down_revision = 'da28ce378b7e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "DevelopersWithId",
        Column("id", INTEGER, primary_key=True, index=True),
        Column("slug_game", VARCHAR, nullable=True),
        Column("name_game", VARCHAR, nullable=True),
        Column("plataform_id",INTEGER, nullable=True),
        Column("plataform_name",VARCHAR, nullable=True),
        Column("plataform_slug",VARCHAR, nullable=True),
        Column("store_id",INTEGER, nullable=True),
        Column("store_name",VARCHAR, nullable=True),
        Column("released_game",DATE, nullable=True),
        Column("tb_game",BOOLEAN, nullable=True),
        Column("background_image_game",VARCHAR, nullable=True),
        Column("rating_game",FLOAT, nullable=True),
        Column("rating_top_game",INTEGER, nullable=True),
        Column("ratings_id",INTEGER, nullable=True),
        Column("ratings_title", VARCHAR, nullable=True),
        Column("ratings_counts", VARCHAR, nullable=True),
        Column("ratings_percent", FLOAT, nullable=True),
        Column("ratings_count",INTEGER, nullable=True),
        Column("reviews_text_count",INTEGER, nullable=True),
        Column("added",INTEGER, nullable=True),
        Column("yet_add_by_status",INTEGER, nullable=True),
        Column("owned_add_by_status",INTEGER, nullable=True),
        Column("beaten_add_by_status", INTEGER, nullable=True),
        Column("toplay_add_by_status", INTEGER, nullable=True),
        Column("dropped_add_by_status",INTEGER, nullable=True),
        Column("playing_add_by_status", INTEGER, nullable=True),
        Column("metacritic",INTEGER, nullable=True),
        Column("suggestions_count", INTEGER, nullable=True),
        Column("updated", DATE, nullable=True),
        Column("metacritic_id", INTEGER, nullable=True),
        Column("metacritic_score", INTEGER, nullable=True),
        Column("clip", BOOLEAN, nullable=True),
        Column("tags_metacritic_id", INTEGER, nullable=True),
        Column("tags_metacritic_name", VARCHAR, nullable=True),
        Column("tags_metacritic_slug", VARCHAR, nullable=True),
        Column("tags_metacritic_language",VARCHAR, nullable=True),
        Column("tags_games_count",INTEGER, nullable=True),
        Column("tags_image_background", VARCHAR, nullable=True),
        Column("esrb_rating_id", INTEGER, nullable=True),
        Column("esrb_rating_name", VARCHAR, nullable=True),
        Column("esrb_rating_slug",VARCHAR, nullable=True),
        Column("esrb_rating_name_en", VARCHAR, nullable=True),
        Column("esrb_rating_name_ru", VARCHAR, nullable=True),
        Column("user_game", VARCHAR, nullable=True),
        Column("reviews_count", INTEGER, nullable=True),
        Column("saturated_color",VARCHAR, nullable=True),
        Column("dominant_color",VARCHAR, nullable=True),
        Column("short_screenshots_id",INTEGER, nullable=True),
        Column("short_screenshots_image",VARCHAR, nullable=True),
        Column("parent_plataforms_id", INTEGER, nullable=True),
        Column("parent_plataforms_name",VARCHAR, nullable=True),
        Column("parent_plataforms_slug",VARCHAR, nullable=True),
        Column("genres_id",INTEGER, nullable=True),
        Column("genres_name",VARCHAR, nullable=True),
        Column("genres_slug",VARCHAR, nullable=True),

    )


def downgrade():
    pass
