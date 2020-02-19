"""update-appointments-table

Revision ID: 6c7b52d82c26
Revises: 6953c580dceb
Create Date: 2020-02-19 13:01:31.216705

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6c7b52d82c26'
down_revision = '6953c580dceb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('appointments', 'time',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('appointments', 'time',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###