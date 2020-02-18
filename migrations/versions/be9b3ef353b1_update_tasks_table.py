"""update-tasks-table

Revision ID: be9b3ef353b1
Revises: 2ca74acaa96c
Create Date: 2020-02-18 12:52:50.621748

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'be9b3ef353b1'
down_revision = '2ca74acaa96c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'title',
               existing_type=mysql.VARCHAR(length=60),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'title',
               existing_type=mysql.VARCHAR(length=60),
               nullable=True)
    # ### end Alembic commands ###