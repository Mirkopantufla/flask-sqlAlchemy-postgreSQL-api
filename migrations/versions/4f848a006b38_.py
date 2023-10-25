"""empty message

Revision ID: 4f848a006b38
Revises: 0f497d4b2f91
Create Date: 2023-10-23 20:45:24.133403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f848a006b38'
down_revision = '0f497d4b2f91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=300),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=300),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###