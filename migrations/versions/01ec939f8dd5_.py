"""empty message

Revision ID: 01ec939f8dd5
Revises: 3f5fd312c67d
Create Date: 2023-10-26 20:17:40.896779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01ec939f8dd5'
down_revision = '3f5fd312c67d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=False),
    sa.Column('price', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=3000), nullable=False),
    sa.Column('category', sa.String(length=300), nullable=True),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###