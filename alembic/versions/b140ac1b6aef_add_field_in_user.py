"""add field in user

Revision ID: b140ac1b6aef
Revises: 86fc246258e9
Create Date: 2023-11-12 21:34:09.799680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b140ac1b6aef'
down_revision = '86fc246258e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_Users_id', table_name='Users')
    op.drop_table('Users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Users_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=340), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=240), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Users_pkey')
    )
    op.create_index('ix_Users_id', 'Users', ['id'], unique=False)
    # ### end Alembic commands ###
