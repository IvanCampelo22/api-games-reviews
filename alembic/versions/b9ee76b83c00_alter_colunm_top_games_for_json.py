"""alter colunm top_games for json

Revision ID: b9ee76b83c00
Revises: 647f5736e201
Create Date: 2023-07-16 09:38:04.401170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9ee76b83c00'
down_revision = '647f5736e201'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('Developers', 'top_games', existing_type=sa.INTEGER(), type_=sa.JSON(), nullable=True, postgresql_using='top_games::json')



def downgrade():
    pass
