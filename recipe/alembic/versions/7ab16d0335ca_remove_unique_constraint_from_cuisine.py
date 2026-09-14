"""remove unique constraint from cuisine

Revision ID: 7ab16d0335ca
Revises: cdcdb24c4657
Create Date: 2026-09-12 18:37:14.163112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ab16d0335ca'
down_revision: Union[str, Sequence[str], None] = 'cdcdb24c4657'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
