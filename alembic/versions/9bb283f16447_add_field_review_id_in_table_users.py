"""add field review_id in table users

Revision ID: 9bb283f16447
Revises: df70000f57e7
Create Date: 2024-05-27 12:06:28.652862

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9bb283f16447'
down_revision = 'df70000f57e7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('User', sa.Column('review_id', sa.Integer, sa.ForeignKey('Review.id'), nullable=False))


def downgrade():
    pass
    
