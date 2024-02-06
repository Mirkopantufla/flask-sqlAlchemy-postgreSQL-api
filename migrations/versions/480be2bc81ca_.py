"""empty message

Revision ID: 480be2bc81ca
Revises: 22fb9020125f
Create Date: 2024-02-01 12:34:10.785078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '480be2bc81ca'
down_revision = '22fb9020125f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=False),
    sa.Column('price', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.Column('description', sa.String(length=3000), nullable=False),
    sa.Column('category', sa.String(length=300), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('images',
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.Column('src_imagen', sa.String(length=3000), nullable=True),
    sa.Column('id_publico', sa.String(length=200), nullable=True),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('image_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.drop_table('products')
    # ### end Alembic commands ###
