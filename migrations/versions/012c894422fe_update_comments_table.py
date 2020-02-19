"""update-comments-table

Revision ID: 012c894422fe
Revises: 8b198f9fcc34
Create Date: 2020-02-19 19:23:41.441387

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '012c894422fe'
down_revision = '8b198f9fcc34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'created_on',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'created_on',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###
