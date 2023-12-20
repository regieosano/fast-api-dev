"""Create again posts table with corrections

Revision ID: 6590728759f5
Revises: 4a5314588e14
Create Date: 2023-12-20 11:53:36.104997

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6590728759f5'
down_revision: Union[str, None] = '4a5314588e14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True,), sa.Column('title', sa.String(length=255), nullable=False),)
   

def downgrade() -> None:
    op.drop_table('posts')
