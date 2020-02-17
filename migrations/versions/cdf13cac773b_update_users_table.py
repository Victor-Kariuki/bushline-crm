"""update-users-table

Revision ID: cdf13cac773b
Revises: cae41e68b82e
Create Date: 2020-02-14 15:45:50.208420

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cdf13cac773b'
down_revision = 'cae41e68b82e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('leads', 'location')
    op.alter_column('tasks', 'title',
               existing_type=mysql.VARCHAR(length=60),
               nullable='False')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'title',
               existing_type=mysql.VARCHAR(length=60),
               nullable=True)
    op.add_column('leads', sa.Column('location', mysql.VARCHAR(length=60), nullable=False))
    # ### end Alembic commands ###
