"""add id in database ReleasedGamesLastMonth

Revision ID: 491b7e843f52
Revises: 4ba25f5f1379
Create Date: 2023-07-04 16:03:37.278878

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy import Column, INTEGER, VARCHAR



# revision identifiers, used by Alembic.
revision = '491b7e843f52'
down_revision = '4ba25f5f1379'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('ReleasedGamesLastMonth', sa.Column('id', sa.Integer(), primary_key=True, nullable=False))



def downgrade():
    pass
