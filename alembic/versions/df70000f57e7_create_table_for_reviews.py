"""create table for reviews

Revision ID: df70000f57e7
Revises: 6d1b92402d38
Create Date: 2024-05-27 10:02:15.798109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df70000f57e7'
down_revision = '6d1b92402d38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game', sa.String(length=320), nullable=False),
    sa.Column('rate', sa.Enum('Péssimo', 'Ruim', 'Regular', 'Bom', 'Muito Bom', name="rate_enum"), nullable=False),
    sa.Column('text_review', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Review')
    # ### end Alembic commands ###