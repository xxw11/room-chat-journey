"""empty message

Revision ID: 8e73b6fa72fb
Revises: 92b53413a92d
Create Date: 2020-04-02 09:27:22.067582

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8e73b6fa72fb'
down_revision = '92b53413a92d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('message', 'message_author',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('message', 'message_room',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('message', 'message_room',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('message', 'message_author',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###