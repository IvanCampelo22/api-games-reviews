"""add column ratings_counts

Revision ID: e9efe3a075a1
Revises: eaddd500f00d
Create Date: 2023-11-09 09:21:22.009102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9efe3a075a1'
down_revision = 'eaddd500f00d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('DevelopersWithId', sa.Column('ratings_counts', sa.Integer))


def downgrade():
    pass
