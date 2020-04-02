"""empty message

Revision ID: 527c713724c4
Revises: 554a7c756b2c
Create Date: 2020-04-01 23:54:38.898375

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '527c713724c4'
down_revision = '554a7c756b2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('message_author', sa.Integer(), nullable=True))
    op.add_column('message', sa.Column('message_room', sa.Integer(), nullable=True))
    op.drop_constraint('message_ibfk_1', 'message', type_='foreignkey')
    op.drop_constraint('message_ibfk_2', 'message', type_='foreignkey')
    op.create_foreign_key(None, 'message', 'user', ['message_room'], ['id'])
    op.create_foreign_key(None, 'message', 'user', ['message_author'], ['id'])
    op.drop_column('message', 'room_id')
    op.drop_column('message', 'author_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('author_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('message', sa.Column('room_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'message', type_='foreignkey')
    op.drop_constraint(None, 'message', type_='foreignkey')
    op.create_foreign_key('message_ibfk_2', 'message', 'room', ['room_id'], ['id'])
    op.create_foreign_key('message_ibfk_1', 'message', 'user', ['author_id'], ['id'])
    op.drop_column('message', 'message_room')
    op.drop_column('message', 'message_author')
    # ### end Alembic commands ###
