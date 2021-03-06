"""empty message

Revision ID: bf990e3c36aa
Revises: 9001a97376c0
Create Date: 2020-03-29 17:45:30.439306

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bf990e3c36aa'
down_revision = '9001a97376c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('permission', sa.Integer(), nullable=True))
    op.drop_column('user', 'role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('user', 'permission')
    # ### end Alembic commands ###
