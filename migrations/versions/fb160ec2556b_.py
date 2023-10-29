"""empty message

Revision ID: fb160ec2556b
Revises: 4f848a006b38
Create Date: 2023-10-25 16:04:22.133602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb160ec2556b'
down_revision = '4f848a006b38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('product_id',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('product_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=300),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###
