"""create user and token

Revision ID: d2cc6150eb7e
Revises: d2ebf0b1f212
Create Date: 2023-11-14 11:14:37.881391

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'd2cc6150eb7e'
down_revision = 'd2ebf0b1f212'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('User', 
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), unique=True, nullable=False),
        sa.Column('password', sa.String(100), nullable=False))

    op.create_table('TokenTable', 
        sa.Column('user_id', sa.Integer),
        sa.Column('acess_token', sa.String(450), primary_key=True),
        sa.Column('refresh_toke', sa.String(450), nullable=False),
        sa.Column('status', sa.Boolean),
        sa.Column('created_date', sa.DateTime, default=datetime.now()))

def downgrade():
    pass
