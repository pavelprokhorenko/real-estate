"""add developer table

Revision ID: fee66562cbef
Revises: 0032edcbf3b0
Create Date: 2022-05-18 12:35:20.582195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fee66562cbef'
down_revision = '0032edcbf3b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('developer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('international_name', sa.String(), nullable=False),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_developer_id'), 'developer', ['id'], unique=False)
    op.create_index(op.f('ix_developer_international_name'), 'developer', ['international_name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_developer_international_name'), table_name='developer')
    op.drop_index(op.f('ix_developer_id'), table_name='developer')
    op.drop_table('developer')
    # ### end Alembic commands ###
