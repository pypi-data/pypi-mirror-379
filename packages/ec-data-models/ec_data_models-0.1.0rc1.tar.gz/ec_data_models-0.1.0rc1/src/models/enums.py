from enum import Enum

from sqlalchemy.dialects import postgresql


class DepartmentType(str, Enum):
    committee = "committee"
    initiative = "initiative"
    advisor = "advisor"


class EventType(str, Enum):
    internal = "internal"
    acm = "ACM"
    talk = "talk"
    hackathon = "hackathon"
    both = "both"
    sdd = "SDD"
    launch = "launch"
    other = "other"


# Helpers for Alembic migrations: a pre-configured postgresql.ENUM instance
# Use create_type=True only when creating the DB enum (initial migration).
def pg_department_enum(create_type: bool = False) -> postgresql.ENUM:
    return postgresql.ENUM(
        *(e.value for e in DepartmentType),
        name="departmenttype",
        create_type=create_type,
    )


def pg_event_enum(create_type: bool = False) -> postgresql.ENUM:
    return postgresql.ENUM(
        *(e.value for e in EventType), name="eventtype", create_type=create_type
    )
    return postgresql.ENUM(
        *(e.value for e in EventType), name="eventtype", create_type=create_type
    )
