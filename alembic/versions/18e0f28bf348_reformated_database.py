"""reformated database

Revision ID: 18e0f28bf348
Revises: fb3335d7f6ac
Create Date: 2023-07-04 17:18:36.920592

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy import Column, INTEGER, VARCHAR


# revision identifiers, used by Alembic.
revision = '18e0f28bf348'
down_revision = 'fb3335d7f6ac'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ReleasedGamesLastMonth',
        Column('id', INTEGER, primary_key=True, autoincrement=True),
        Column('plataform_id', INTEGER, nullable=True),
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
