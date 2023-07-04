"""remove primary_key for plataform_id

Revision ID: 33cc22b3fafb
Revises: 491b7e843f52
Create Date: 2023-07-04 16:12:18.364736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33cc22b3fafb'
down_revision = '491b7e843f52'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    op.alter_column('ReleasedGamesLastMonth', 'plataform_id', type_=sa.Integer(), nullable=False)

