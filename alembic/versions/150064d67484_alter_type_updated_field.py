"""alter type updated field

Revision ID: 150064d67484
Revises: e9efe3a075a1
Create Date: 2023-11-09 21:23:36.819679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '150064d67484'
down_revision = 'e9efe3a075a1'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('DevelopersWithId', 'updated', nullable=True, type_=sa.String)


def downgrade():
    pass
