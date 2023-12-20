"""add user table

Revision ID: b5d7e4139c37
Revises: b5abc4e4ee35
Create Date: 2023-12-20 12:18:45.272312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5d7e4139c37'
down_revision: Union[str, None] = 'b5abc4e4ee35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), 
                     nullable=False),
                     sa.Column('email', sa.String(length=255), nullable=False),
                     sa.Column('password', sa.String(length=255), nullable=False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),  nullable=False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email'),
                     )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
