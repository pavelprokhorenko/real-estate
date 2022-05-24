"""add amenity and building tables

Revision ID: 3be034052cd6
Revises: 610434539289
Create Date: 2022-05-21 14:47:29.378700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3be034052cd6'
down_revision = '610434539289'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('amenity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_amenity_id'), 'amenity', ['id'], unique=False)
    op.create_index(op.f('ix_amenity_name'), 'amenity', ['name'], unique=True)
    op.create_table('building',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('latitude', sa.Numeric(), nullable=False),
    sa.Column('longitude', sa.Numeric(), nullable=False),
    sa.Column('building_class', sa.String(), nullable=False),
    sa.Column('postcode', sa.String(), nullable=False),
    sa.Column('number_of_units', sa.Integer(), nullable=False),
    sa.Column('number_of_floors', sa.Integer(), nullable=False),
    sa.Column('year_built', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_building_id'), 'building', ['id'], unique=False)
    op.create_table('building_amenities',
    sa.Column('amenity_id', sa.Integer(), nullable=False),
    sa.Column('building_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amenity_id'], ['amenity.id'], ),
    sa.ForeignKeyConstraint(['building_id'], ['building.id'], ),
    sa.PrimaryKeyConstraint('amenity_id', 'building_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('building_amenities')
    op.drop_index(op.f('ix_building_id'), table_name='building')
    op.drop_table('building')
    op.drop_index(op.f('ix_amenity_name'), table_name='amenity')
    op.drop_index(op.f('ix_amenity_id'), table_name='amenity')
    op.drop_table('amenity')
    # ### end Alembic commands ###
