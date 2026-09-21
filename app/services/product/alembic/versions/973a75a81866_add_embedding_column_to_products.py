"""Add embedding column to products

Revision ID: 973a75a81866
Revises: 65f2446cd424
Create Date: 2026-09-20 07:57:27.386033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '973a75a81866'
down_revision: Union[str, Sequence[str], None] = '65f2446cd424'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")
    op.execute(
        "ALTER TABLE products "
        "ADD COLUMN IF NOT EXISTS embedding vector(1536)"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("ALTER TABLE products DROP COLUMN IF EXISTS embedding")
