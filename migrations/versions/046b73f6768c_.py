"""empty message

Revision ID: 046b73f6768c
Revises: e038987e172d
Create Date: 2023-11-27 12:29:58.298317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '046b73f6768c'
down_revision = 'e038987e172d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('rut_numbers', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=300), nullable=False),
    sa.Column('last_name', sa.String(length=300), nullable=False),
    sa.Column('phone_number', sa.BigInteger(), nullable=False),
    sa.Column('email', sa.String(length=300), nullable=False),
    sa.Column('password', sa.String(length=300), nullable=False),
    sa.Column('terms_conditions', sa.Boolean(), nullable=False),
    sa.Column('register_date', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], ),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('rut_numbers')
    )
    with op.batch_alter_table('carts', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['user_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('carts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    op.drop_table('users')
    # ### end Alembic commands ###
