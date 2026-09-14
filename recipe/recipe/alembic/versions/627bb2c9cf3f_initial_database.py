"""initial database

Revision ID: 627bb2c9cf3f
Revises: 
Create Date: 2026-09-12 14:38:48.880033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '627bb2c9cf3f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'users',
        sa.Column(
            'mfa_enabled',
            sa.Boolean(),
            nullable=False,
            server_default=sa.false()
        )
    )
    op.drop_index(op.f('ix_users_user_id'), table_name='users')


def downgrade() -> None:
    """Downgrade schema."""
    op.create_index(
        op.f('ix_users_user_id'),
        'users',
        ['user_id'],
        unique=False
    )
    op.drop_column('users', 'mfa_enabled')