"""Create full schema.

Revision ID: 0002_full_schema
Revises: 0001_initial_schema
Create Date: 2025-08-24
"""

from typing import TYPE_CHECKING

import alembic.op as op  # type: ignore[attr-defined]
import sqlalchemy as sa

from src.models.enums import pg_department_enum, pg_event_enum

if TYPE_CHECKING:
    # For static typing only; alembic provides 'op' dynamically at runtime.
    from alembic import op as _op  # noqa: F401

revision = "0002_full_schema"
down_revision = "0001_initial_schema"
branch_labels = None
depends_on = None


def upgrade():
    # person
    op.create_table(
        "person",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("username", sa.String, nullable=True),
        sa.Column("first_name", sa.String, nullable=True),
        sa.Column("last_name", sa.String, nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_person_email", "person", ["email"])
    op.create_unique_constraint("uq_person_email", "person", ["email"])

    # student_info (one-to-one, PK is person.id)
    op.create_table(
        "student_info",
        sa.Column(
            "id",
            sa.Integer,
            sa.ForeignKey("person.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("gpa", sa.Integer, nullable=True),
    )

    # job_info (one-to-one, PK is person.id)
    op.create_table(
        "job_info",
        sa.Column(
            "id",
            sa.Integer,
            sa.ForeignKey("person.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("title", sa.String, nullable=True),
        sa.Column("department", sa.String, nullable=True),
    )

    # member (one-to-one, PK is person.id)
    op.create_table(
        "member",
        sa.Column(
            "id",
            sa.Integer,
            sa.ForeignKey("person.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("ec_email", sa.String, nullable=False),
    )

    # alumni (PK is member.id)
    op.create_table(
        "alumni",
        sa.Column(
            "id",
            sa.Integer,
            sa.ForeignKey("member.id", ondelete="CASCADE"),
            primary_key=True,
        ),
    )

    # department (uses ENUM 'departmenttype' created in 0001)
    op.create_table(
        "department",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column(
            "type",
            pg_department_enum(create_type=False),
            nullable=False,
        ),
    )

    # member_semester_info
    op.create_table(
        "member_semester_info",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "member_id",
            sa.Integer,
            sa.ForeignKey("member.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("role", sa.String, nullable=True),
        sa.Column("semester", sa.String, nullable=True),
        sa.Column(
            "department_id",
            sa.Integer,
            sa.ForeignKey("department.id", ondelete="SET NULL"),
            nullable=True,
        ),
    )

    # event (uses ENUM 'eventtype' created in 0001)
    op.create_table(
        "event",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "type",
            pg_event_enum(create_type=False),
            nullable=False,
        ),
        sa.Column("start", sa.DateTime(timezone=True), nullable=True),
        sa.Column("end", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "parent_event",
            sa.Integer,
            sa.ForeignKey("event.id", ondelete="SET NULL"),
            nullable=True,
        ),
    )

    # organisation
    op.create_table(
        "organisation",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=True),
    )

    # person_organisation_association (link person <-> organisation, optional job)
    op.create_table(
        "person_organisation_association",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "oid",
            sa.Integer,
            sa.ForeignKey("organisation.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "pid",
            sa.Integer,
            sa.ForeignKey("person.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "jid",
            sa.Integer,
            sa.ForeignKey("job_info.id", ondelete="SET NULL"),
            nullable=True,
        ),
    )
    op.create_unique_constraint(
        "uq_person_org_oid_pid", "person_organisation_association", ["oid", "pid"]
    )
    op.create_index(
        "ix_person_org_oid_pid", "person_organisation_association", ["oid", "pid"]
    )

    # person_event (join table)
    op.create_table(
        "person_event",
        sa.Column(
            "pid",
            sa.Integer,
            sa.ForeignKey("person.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column(
            "eid",
            sa.Integer,
            sa.ForeignKey("event.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("role", sa.String, nullable=True),
        sa.Column("description", sa.String, nullable=True),
        sa.Column(
            "person_organisation_association_id",
            sa.Integer,
            sa.ForeignKey("person_organisation_association.id", ondelete="SET NULL"),
            nullable=True,
        ),
    )
    op.create_index("ix_person_event_pid_eid", "person_event", ["pid", "eid"])

    # helper_shift
    op.create_table(
        "helper_shift",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "pid",
            sa.Integer,
            sa.ForeignKey("person.id", ondelete="CASCADE"),
            nullable=True,
        ),
        sa.Column(
            "eid",
            sa.Integer,
            sa.ForeignKey("event.id", ondelete="CASCADE"),
            nullable=True,
        ),
        sa.Column("role", sa.String, nullable=True),
        sa.Column("start", sa.DateTime(timezone=True), nullable=True),
        sa.Column("end", sa.DateTime(timezone=True), nullable=True),
    )

    # organisation_event (join)
    op.create_table(
        "organisation_event",
        sa.Column(
            "oid",
            sa.Integer,
            sa.ForeignKey("organisation.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column(
            "eid",
            sa.Integer,
            sa.ForeignKey("event.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("role", sa.String, nullable=True),
    )
    op.create_index(
        "ix_organisation_event_oid_eid", "organisation_event", ["oid", "eid"]
    )

    # sponsorship
    op.create_table(
        "sponsorship",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("type", sa.String, nullable=True),
        sa.Column(
            "eid",
            sa.Integer,
            sa.ForeignKey("event.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column(
            "organisation_id",
            sa.Integer,
            sa.ForeignKey("organisation.id", ondelete="SET NULL"),
            nullable=True,
        ),
    )


def downgrade():
    # Drop in reverse order of creation to respect FKs
    op.drop_table("sponsorship")
    op.drop_index("ix_organisation_event_oid_eid", table_name="organisation_event")
    op.drop_table("organisation_event")
    op.drop_table("helper_shift")
    op.drop_index("ix_person_event_pid_eid", table_name="person_event")
    op.drop_table("person_event")
    op.drop_index("ix_person_org_oid_pid", table_name="person_organisation_association")
    op.drop_constraint(
        "uq_person_org_oid_pid", "person_organisation_association", type_="unique"
    )
    op.drop_table("person_organisation_association")
    op.drop_table("organisation")
    op.drop_table("event")
    op.drop_table("member_semester_info")
    op.drop_table("department")
    op.drop_table("alumni")
    op.drop_table("member")
    op.drop_table("job_info")
    op.drop_table("student_info")
    op.drop_index("ix_person_email", table_name="person")
    op.drop_constraint("uq_person_email", "person", type_="unique")
    op.drop_table("person")
