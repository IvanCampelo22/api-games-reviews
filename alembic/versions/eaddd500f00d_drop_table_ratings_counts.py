"""drop table ratings_counts

Revision ID: eaddd500f00d
Revises: 7f55eee5ee99
Create Date: 2023-11-09 09:20:53.033042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaddd500f00d'
down_revision = '7f55eee5ee99'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('DevelopersWithId', 'ratings_counts')


def downgrade():
    pass
