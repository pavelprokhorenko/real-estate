"""fix name type in amenity table

Revision ID: 6052b45b448f
Revises: 3be034052cd6
Create Date: 2022-05-24 07:06:33.422755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6052b45b448f'
down_revision = '3be034052cd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('amenity', 'name',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('amenity', 'name',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###