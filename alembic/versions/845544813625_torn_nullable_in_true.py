"""torn nullable in True

Revision ID: 845544813625
Revises: 33cc22b3fafb
Create Date: 2023-07-04 16:22:23.308436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '845544813625'
down_revision = '33cc22b3fafb'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('ReleasedGamesLastMonth', 'plataform_id', type_=sa.Integer(), nullable=True)


def downgrade():
    op.alter_column('ReleasedGamesLastMonth', 'plataform_id', type_=sa.Integer(), nullable=True)

