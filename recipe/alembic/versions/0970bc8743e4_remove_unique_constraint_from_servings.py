"""remove unique constraint from servings

Revision ID: 0970bc8743e4
Revises: cb7cd9430554
Create Date: 2026-09-12 17:34:53.497049

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0970bc8743e4'
down_revision: Union[str, Sequence[str], None] = 'cb7cd9430554'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_index(
        "ix_recipes_servings",
        table_name="recipes"
    )


def downgrade() -> None:
    op.create_index(
        "ix_recipes_servings",
        "recipes",
        ["servings"],
        unique=True
    )