"""create table for UpcomingGames

Revision ID: 74b1c52a3995
Revises: a2609b93a975
Create Date: 2023-07-10 21:45:45.592767

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, INTEGER, VARCHAR


# revision identifiers, used by Alembic.
revision = '74b1c52a3995'
down_revision = 'a2609b93a975'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'UpcomingGames',
        Column('id', sa.Integer, primary_key=True, autoincrement=True),
        Column('slug_game', sa.String, nullable=True),
        Column('name_game', sa.String, nullable=True),
        Column('playtime', sa.Integer, nullable=True),
        Column('plataform_id', sa.Integer, nullable=True),
        Column('plataform_name', sa.String, nullable=True),
        Column('plataform_slug', sa.String, nullable=True),
    )


def downgrade():
    pass
