"""add content column to posts table

Revision ID: b5abc4e4ee35
Revises: 6590728759f5
Create Date: 2023-12-20 12:09:59.087804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5abc4e4ee35'
down_revision: Union[str, None] = '6590728759f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(length=255), nullable=False),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
