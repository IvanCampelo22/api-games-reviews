"""remove review_id and add user_id in table review

Revision ID: cc2ffbac0d43
Revises: d1d21f4dd48e
Create Date: 2024-05-28 07:21:01.196139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc2ffbac0d43'
down_revision = 'd1d21f4dd48e'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('User', 'review_id')
    op.add_column('Reviews', sa.Column('user_id', sa.Integer, sa.ForeignKey('User.id'), nullable=False))


def downgrade():
    pass
