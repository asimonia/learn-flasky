"""migration2

Revision ID: 663c3bd7082
Revises: eaafd1a9588
Create Date: 2016-06-07 01:25:36.844876

"""

# revision identifiers, used by Alembic.
revision = '663c3bd7082'
down_revision = 'eaafd1a9588'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###
