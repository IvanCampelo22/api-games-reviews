"""Initial migration

Revision ID: 4ba25f5f1379
Revises: 25686094c26e
Create Date: 2023-07-03 15:57:47.816760

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, INTEGER, VARCHAR



# revision identifiers, used by Alembic.
revision = '4ba25f5f1379'
down_revision = '25686094c26e'
branch_labels = None
depends_on = None


def upgrade() -> None: 
    op.create_table(
        'ReleasedGamesLastMonth',
        Column('plataform_id', INTEGER, primary_key=True, autoincrement=True),
        Column('name_plataform', VARCHAR, nullable=False),
        Column('slug_plataform', VARCHAR,  nullable=True),
        Column('games_count', INTEGER, nullable=True),
        Column('image_background', VARCHAR, nullable=True),
        Column('image', VARCHAR, nullable=True),
        Column('year_start', INTEGER, nullable=True),
        Column('year_end', INTEGER, nullable=True),
        Column('game_id', INTEGER, nullable=True),
        Column('game_slug', VARCHAR, nullable=True),
        Column('game_name', VARCHAR, nullable=True),

    )


def downgrade():
    pass
