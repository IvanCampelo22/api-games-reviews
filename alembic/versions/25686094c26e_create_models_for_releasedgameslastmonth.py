"""create models for ReleasedGamesLastMonth

Revision ID: 25686094c26e
Revises: 
Create Date: 2023-07-02 15:08:53.186177

"""
from alembic import op
from sqlalchemy import Column, INTEGER, VARCHAR


# revision identifiers, used by Alembic.
revision = '25686094c26e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(): 
    op.create_table(
        'ReleasedGamesLastMonth',
        Column('plataform_id', INTEGER, primary_key=True, autoincrement=True),
        Column('name_plataform', VARCHAR, nullable=True),
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
