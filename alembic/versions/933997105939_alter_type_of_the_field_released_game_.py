"""alter type of the field released_game for string

Revision ID: 933997105939
Revises: 0105c37ea729
Create Date: 2023-11-09 09:00:49.142903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '933997105939'
down_revision = '0105c37ea729'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('DevelopersWithId','released_game', nullable=True, type_=sa.String)


def downgrade():
    pass
