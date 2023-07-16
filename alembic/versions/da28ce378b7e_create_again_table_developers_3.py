"""create again table Developers 3

Revision ID: da28ce378b7e
Revises: 4e0321603521
Create Date: 2023-07-16 09:56:06.155899

"""
from alembic import op
from sqlalchemy import Column, INTEGER, VARCHAR, JSON


# revision identifiers, used by Alembic.
revision = 'da28ce378b7e'
down_revision = '4e0321603521'
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
        Column('top_games', JSON, nullable=True),
        Column('games_count', INTEGER, nullable=True),
        Column('image_background', VARCHAR, nullable=True),
        Column('score', VARCHAR, nullable=True),
    )



def downgrade():
    pass
