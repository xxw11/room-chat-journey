"""empty message

Revision ID: a3c9f6feb0ff
Revises: 7ccc6b7c340e
Create Date: 2020-04-01 21:30:48.896637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3c9f6feb0ff'
down_revision = '7ccc6b7c340e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('u_r',
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('r_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['r_id'], ['room.id'], ),
    sa.ForeignKeyConstraint(['u_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('u_id', 'r_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('u_r')
    # ### end Alembic commands ###