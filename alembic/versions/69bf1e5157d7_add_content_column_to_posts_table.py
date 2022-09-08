"""add content column to posts table

Revision ID: 69bf1e5157d7
Revises: d8bdb87af8a8
Create Date: 2022-09-07 14:11:07.842408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69bf1e5157d7'
down_revision = 'd8bdb87af8a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
