"""remove unique constraint from cuisine

Revision ID: cdcdb24c4657
Revises: 0970bc8743e4
Create Date: 2026-09-12 18:37:03.382669

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdcdb24c4657'
down_revision: Union[str, Sequence[str], None] = '0970bc8743e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_index(
        "ix_recipes_cuisine",
        table_name="recipes"
    )



def downgrade() -> None:
    op.create_index(
        "ix_recipes_cuisine",
        "recipes",
        ["cuisine"],
        unique=True
    )