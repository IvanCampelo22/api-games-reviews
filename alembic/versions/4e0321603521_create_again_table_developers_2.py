"""create again table Developers 2

Revision ID: 4e0321603521
Revises: e762029401ee
Create Date: 2023-07-16 09:50:35.276857

"""
from alembic import op
from sqlalchemy import Column, INTEGER, VARCHAR, JSON



# revision identifiers, used by Alembic.
revision = '4e0321603521'
down_revision = 'e762029401ee'
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
