"""alter name refresh_token

Revision ID: 303a231d6f3d
Revises: d2cc6150eb7e
Create Date: 2023-11-14 11:38:55.704642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '303a231d6f3d'
down_revision = 'd2cc6150eb7e'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('TokenTable', 'acess_token', primary_key=True, new_column_name='access_toke')


def downgrade():
    pass
