"""alter nullable of the review_id in table users

Revision ID: d1d21f4dd48e
Revises: 9bb283f16447
Create Date: 2024-05-27 16:11:41.569993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1d21f4dd48e'
down_revision = '9bb283f16447'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('User', sa.Column('review_id', sa.Integer, sa.ForeignKey('Review.id'), nullable=True))


def downgrade():
    pass
