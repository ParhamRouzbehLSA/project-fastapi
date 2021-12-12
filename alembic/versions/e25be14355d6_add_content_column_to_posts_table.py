"""add content column to posts table

Revision ID: e25be14355d6
Revises: a53a950af21a
Create Date: 2021-12-11 11:37:39.047461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e25be14355d6'
down_revision = 'a53a950af21a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
