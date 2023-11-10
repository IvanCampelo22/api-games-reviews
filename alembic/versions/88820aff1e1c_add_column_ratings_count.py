"""add column ratings_count

Revision ID: 88820aff1e1c
Revises: 36a0be6c9d7a
Create Date: 2023-11-09 09:14:07.695406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88820aff1e1c'
down_revision = '36a0be6c9d7a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('DevelopersWithId', sa.Column('ratings_counts', sa.String))


def downgrade():
    pass
