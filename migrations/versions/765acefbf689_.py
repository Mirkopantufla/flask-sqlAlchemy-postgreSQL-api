"""empty message

Revision ID: 765acefbf689
Revises: 4ec534c9dc19
Create Date: 2024-01-05 13:31:48.290209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '765acefbf689'
down_revision = '4ec534c9dc19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.alter_column('src_imagen',
               existing_type=sa.VARCHAR(length=400),
               type_=sa.String(length=3000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.alter_column('src_imagen',
               existing_type=sa.String(length=3000),
               type_=sa.VARCHAR(length=400),
               existing_nullable=True)

    # ### end Alembic commands ###