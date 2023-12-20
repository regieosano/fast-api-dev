"""Create posts table

Revision ID: 4a5314588e14
Revises: 
Create Date: 2023-12-20 11:00:24.453098

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a5314588e14'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True,), sa.Column('title', sa.String(length=255), nullable=False),)
   

def downgrade() -> None:
    op.drop_table('posts')
