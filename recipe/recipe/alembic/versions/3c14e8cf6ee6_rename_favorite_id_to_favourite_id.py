from typing import Sequence, Union

from alembic import op


revision: str = "846569882a74"

down_revision: Union[str, Sequence[str], None] = "7ab16d0335ca"

branch_labels = None

depends_on = None


def upgrade() -> None:
    op.alter_column(
        "favourites",
        "favorite_id",
        new_column_name="favourite_id"
    )


def downgrade() -> None:
    op.alter_column(
        "favourites",
        "favourite_id",
        new_column_name="favorite_id"
    )