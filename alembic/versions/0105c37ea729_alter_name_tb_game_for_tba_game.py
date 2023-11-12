"""alter name tb_game for tba_game

Revision ID: 0105c37ea729
Revises: 35e7f3d46dd4
Create Date: 2023-11-09 08:46:07.441773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0105c37ea729'
down_revision = '35e7f3d46dd4'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('DevelopersWithId', 'tb_game', nullable=True, new_column_name='tba_game')



def downgrade():
    pass
