"""empty message

Revision ID: 3f06016d40db
Revises: 92c4ea9a487e
Create Date: 2020-04-01 22:07:08.692473

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3f06016d40db'
down_revision = '92c4ea9a487e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('u_rooms', sa.Integer(), nullable=True))
    op.drop_constraint('user_ibfk_1', 'user', type_='foreignkey')
    op.create_foreign_key(None, 'user', 'room', ['u_rooms'], ['id'])
    op.drop_column('user', 'rooms')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('rooms', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.create_foreign_key('user_ibfk_1', 'user', 'room', ['rooms'], ['id'])
    op.drop_column('user', 'u_rooms')
    # ### end Alembic commands ###
