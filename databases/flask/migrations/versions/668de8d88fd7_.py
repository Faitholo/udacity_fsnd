"""empty message

Revision ID: 668de8d88fd7
Revises: c960d8557305
Create Date: 2022-05-18 10:57:02.601770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '668de8d88fd7'
down_revision = 'c960d8557305'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    
    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')
    
    op.alter_column('todos','completed', nullable =False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
