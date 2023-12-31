"""create user model

Revision ID: 86fc246258e9
Revises: 62c5a1aab719
Create Date: 2023-11-12 17:19:05.421158

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '86fc246258e9'
down_revision = '62c5a1aab719'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users', 
                    sa.Column('id', sa.Integer, primary_key=True, index=True),
                    sa.Column('full_name', sa.String(length=340), nullable=False),
                    sa.Column('username', sa.String(length=120), nullable=False),
                    sa.Column('email', sa.String(length=240), nullable=False),
                    sa.Column('hashed_password', sa.String, nullable=False),
                    sa.Column('is_active', sa.Boolean, default=True),
                    sa.Column('created_at', sa.Date, default=datetime.now()))
    
                    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
