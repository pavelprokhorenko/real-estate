"""add permission fields

Revision ID: 0032edcbf3b0
Revises: 5be4c279d28d
Create Date: 2022-05-16 09:39:16.247520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0032edcbf3b0'
down_revision = '5be4c279d28d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('is_superuser', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_superuser')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###
