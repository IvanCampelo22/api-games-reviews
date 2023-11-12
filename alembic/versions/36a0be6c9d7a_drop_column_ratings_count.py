"""drop column ratings_count

Revision ID: 36a0be6c9d7a
Revises: 933997105939
Create Date: 2023-11-09 09:11:46.323390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36a0be6c9d7a'
down_revision = '933997105939'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('DevelopersWithId', 'ratings_counts')


def downgrade():
    pass
