"""alter type field ratings_count

Revision ID: 7f55eee5ee99
Revises: 88820aff1e1c
Create Date: 2023-11-09 09:15:53.559196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f55eee5ee99'
down_revision = '88820aff1e1c'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('DevelopersWithId','ratings_counts', nullable=True, type_=sa.String)



def downgrade():
    pass
