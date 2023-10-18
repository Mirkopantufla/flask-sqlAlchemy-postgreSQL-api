"""empty message

Revision ID: 0f497d4b2f91
Revises: 4eeb584c135c
Create Date: 2023-10-17 21:25:57.141428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f497d4b2f91'
down_revision = '4eeb584c135c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('communes',
    sa.Column('commune_id', sa.String(length=100), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('commune_id')
    )
    op.create_table('images',
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.Column('src_imagen', sa.String(length=400), nullable=True),
    sa.Column('id_publico', sa.String(length=200), nullable=True),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('image_id')
    )
    op.create_table('products',
    sa.Column('product_id', sa.String(length=300), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=3000), nullable=False),
    sa.Column('category', sa.String(length=300), nullable=True),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('regions',
    sa.Column('region_id', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('roman_number', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('region_id')
    )
    op.create_table('roles',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('role_id')
    )
    op.create_table('ship_details',
    sa.Column('shipDetail_id', sa.Integer(), nullable=False),
    sa.Column('address_name', sa.String(length=300), nullable=False),
    sa.Column('address', sa.String(length=300), nullable=False),
    sa.Column('address_number', sa.Integer(), nullable=False),
    sa.Column('aditional_info', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('commune_id', sa.Integer(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('shipDetail_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('rut_numbers', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=300), nullable=False),
    sa.Column('last_name', sa.String(length=300), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=300), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.Column('terms_conditions', sa.Boolean(), nullable=False),
    sa.Column('register_date', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], ),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('rut_numbers')
    )
    op.create_table('carts',
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('product_ids', sa.ARRAY(sa.Integer()), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('cart_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carts')
    op.drop_table('users')
    op.drop_table('ship_details')
    op.drop_table('roles')
    op.drop_table('regions')
    op.drop_table('products')
    op.drop_table('images')
    op.drop_table('communes')
    # ### end Alembic commands ###
