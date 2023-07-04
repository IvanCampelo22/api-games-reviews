"""create id primary_key and plataform_id just integer and nullable true

Revision ID: fb3335d7f6ac
Revises: 8b182bb84545
Create Date: 2023-07-04 17:00:32.155264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb3335d7f6ac'
down_revision = '8b182bb84545'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    op.drop_column('ReleasedGamesLasMonth', 'plataform_id')

