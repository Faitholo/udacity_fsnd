"""empty message

Revision ID: c960d8557305
Revises: 
Create Date: 2022-05-18 10:22:40.607338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c960d8557305'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('item', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='todos1_pkey')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    ()
    # ### end Alembic commands ###
