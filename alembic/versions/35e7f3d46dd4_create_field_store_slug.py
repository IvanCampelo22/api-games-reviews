"""create field store_slug

Revision ID: 35e7f3d46dd4
Revises: 487fda1294e0
Create Date: 2023-11-08 21:05:10.168745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35e7f3d46dd4'
down_revision = '487fda1294e0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('DevelopersWithId', sa.Column('store_slug', sa.String))



def downgrade():
    pass
