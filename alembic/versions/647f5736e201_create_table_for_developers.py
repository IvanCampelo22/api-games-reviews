"""create table for Developers

Revision ID: 647f5736e201
Revises: 74b1c52a3995
Create Date: 2023-07-11 08:27:26.629130

"""
from alembic import op
from sqlalchemy import Column, INTEGER, VARCHAR


# revision identifiers, used by Alembic.
revision = '647f5736e201'
down_revision = '74b1c52a3995'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Developers',
        Column('id', INTEGER, primary_key=True, autoincrement=True),
        Column('developer_id', INTEGER, nullable=True),
        Column('text', VARCHAR, nullable=True),
        Column('developer_name', VARCHAR, nullable=True),
        Column('exact_name', VARCHAR, nullable=True),
        Column('search_name', VARCHAR, nullable=True),
        Column('developer_slug', VARCHAR, nullable=True),
        Column('top_games', INTEGER, nullable=True),
        Column('games_count', INTEGER, nullable=True),
        Column('image_background', VARCHAR, nullable=True),
        Column('score', VARCHAR, nullable=True),
    )


def downgrade():
    pass
