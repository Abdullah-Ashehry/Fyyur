"""empty message

Revision ID: 2118bd4cec5c
Revises: b0c5bd47552b
Create Date: 2020-04-16 17:13:47.586060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2118bd4cec5c'
down_revision = 'b0c5bd47552b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
