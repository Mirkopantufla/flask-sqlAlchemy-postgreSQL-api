"""empty message

Revision ID: 4ec534c9dc19
Revises: 0d277e4e1ef5
Create Date: 2023-12-28 01:27:49.244599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ec534c9dc19'
down_revision = '0d277e4e1ef5'
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
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'products', ['product_id'], ['product_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    op.drop_table('products')
    # ### end Alembic commands ###