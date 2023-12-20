"""add foreign key to posts table

Revision ID: 26225d8ccb4a
Revises: b5d7e4139c37
Create Date: 2023-12-20 14:45:21.500649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26225d8ccb4a'
down_revision: Union[str, None] = 'b5d7e4139c37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('fk_posts_owner_id', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('fk_posts_owner_id', 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    pass
