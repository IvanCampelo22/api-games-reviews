"""add column playtime in DevelopersWithId

Revision ID: 455f1be47b29
Revises: d77d2c4312b6
Create Date: 2023-07-18 07:27:59.398894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '455f1be47b29'
down_revision = 'd77d2c4312b6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('DevelopersWithId', sa.Column('playtime', sa.Integer, nullable=True))


def downgrade():
    pass
