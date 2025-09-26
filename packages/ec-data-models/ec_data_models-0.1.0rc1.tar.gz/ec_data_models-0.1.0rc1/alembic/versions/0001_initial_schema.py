"""initial schema

Revision ID: 0001_initial_schema
Revises:
Create Date: 2025-08-24
"""

from typing import TYPE_CHECKING

import alembic.op as op  # type: ignore[attr-defined]

from src.models.enums import pg_department_enum, pg_event_enum

if TYPE_CHECKING:
    # For static typing only; alembic provides 'op' dynamically at runtime.
    from alembic import op as _op  # noqa: F401

revision = "0001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create Postgres enums using centralized definitions
    pg_event_enum(create_type=True).create(op.get_bind(), checkfirst=True)
    pg_department_enum(create_type=True).create(op.get_bind(), checkfirst=True)


def downgrade():
    # drop enums
    op.execute("DROP TYPE IF EXISTS eventtype")
    op.execute("DROP TYPE IF EXISTS departmenttype")
