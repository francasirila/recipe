"""merge migration heads

Revision ID: ecdaffeb00eb
Revises: 8a9f34d21abc, 846569882a74
Create Date: 2026-09-12 19:06:31.252867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecdaffeb00eb'
down_revision: Union[str, Sequence[str], None] = ('8a9f34d21abc', '846569882a74')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


down_revision = (
    "7ab16d0335ca",
    "846569882a74"
)