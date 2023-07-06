"""create table for ReleasedGamesLastMonthPlataform

Revision ID: a2609b93a975
Revises: 18e0f28bf348
Create Date: 2023-07-06 18:29:23.026966

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, INTEGER, VARCHAR



# revision identifiers, used by Alembic.
revision = 'a2609b93a975'
down_revision = '18e0f28bf348'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ReleasedGamesLastMonthPlataform',
        Column('id', INTEGER, primary_key=True, autoincrement=True),
        Column('slug_game', VARCHAR, nullable=True),
        Column('name_game', VARCHAR, nullable=True),
        Column('playtime', INTEGER, nullable=True),
        Column('plataform_id', INTEGER, nullable=True),
        Column('plataform_name', VARCHAR, nullable=True),
        Column('plataform_slug', VARCHAR, nullable=True),
    )


def downgrade():
    pass
