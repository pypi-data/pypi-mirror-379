from datetime import UTC, datetime
from typing import ClassVar

from sqlalchemy import Index, UniqueConstraint
from sqlmodel import Column, DateTime, Field, Integer, Relationship, SQLModel, String
from sqlmodel import Enum as SQLEnum

from .enums import DepartmentType, EventType


class Person(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(sa_column=Column(String, nullable=False))
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column=Column(DateTime(timezone=True)),
    )

    # relationships
    member: "Member | None" = Relationship(
        back_populates="person", sa_relationship_kwargs={"uselist": False}
    )
    student_info: "list[StudentInfo]" = Relationship(back_populates="person")
    job_info: "list[JobInfo]" = Relationship(back_populates="person")
    person_events: "list[PersonEvent]" = Relationship(back_populates="person")
    helper_shifts: "list[HelperShift]" = Relationship(back_populates="person")
    org_associations: "list[PersonOrganisationAssociation]" = Relationship(
        back_populates="person"
    )

    __table_args__ = (
        UniqueConstraint("email", name="uq_person_email"),
        Index("ix_person_email", "email"),
    )


class StudentInfo(SQLModel, table=True):
    __tablename__: ClassVar[str] = "student_info"
    id: int | None = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.id", nullable=False)
    gpa: int | None = None

    # relationship back to person
    person: "Person | None" = Relationship(back_populates="student_info")


class JobInfo(SQLModel, table=True):
    __tablename__: ClassVar[str] = "job_info"
    id: int | None = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.id", nullable=False)
    title: str | None = None
    department: str | None = None

    # relationship back to person
    person: "Person | None" = Relationship(back_populates="job_info")


class Member(SQLModel, table=True):
    __tablename__: ClassVar[str] = "member"
    # one-to-one: Member.id references Person.id (same PK)
    id: int = Field(foreign_key="person.id", primary_key=True)
    ec_email: str = Field(sa_column=Column(String, nullable=False))

    person: "Person | None" = Relationship(back_populates="member")
    semesters: "list[MemberSemesterInfo]" = Relationship(back_populates="member")


class Alumni(SQLModel, table=True):
    __tablename__: ClassVar[str] = "alumni"
    # Alumni.id references Member.id (same PK)
    id: int = Field(foreign_key="member.id", primary_key=True)


class MemberSemesterInfo(SQLModel, table=True):
    __tablename__: ClassVar[str] = "member_semester_info"
    id: int | None = Field(default=None, primary_key=True)
    member_id: int = Field(foreign_key="member.id")
    role: str | None = None
    semester: str | None = None

    member: "Member | None" = Relationship(back_populates="semesters")
    # The DBML had Ref: member_semester_info.id > department.id which is odd;
    # provide optional department_id
    department_id: int | None = Field(default=None, foreign_key="department.id")
    # relationship back to department
    department: "Department | None" = Relationship(back_populates="semesters")


class Department(SQLModel, table=True):
    __tablename__: ClassVar[str] = "department"
    id: int = Field(sa_column=Column(Integer, primary_key=True))
    name: str = Field(sa_column=Column(String, nullable=False))
    type: DepartmentType = Field(
        sa_column=Column(SQLEnum(DepartmentType), nullable=False)
    )

    semesters: "list[MemberSemesterInfo]" = Relationship(back_populates="department")


class Event(SQLModel, table=True):
    __tablename__: ClassVar[str] = "event"
    id: int = Field(sa_column=Column(Integer, primary_key=True))
    type: EventType = Field(sa_column=Column(SQLEnum(EventType), nullable=False))
    start: datetime | None = None
    end: datetime | None = None
    parent_event: int | None = Field(default=None, foreign_key="event.id")

    parent: "Event | None" = Relationship(
        sa_relationship_kwargs={"remote_side": "Event.id"}
    )
    person_events: "list[PersonEvent]" = Relationship(back_populates="event")
    helper_shifts: "list[HelperShift]" = Relationship(back_populates="event")
    organisation_events: "list[OrganisationEvent]" = Relationship(
        back_populates="event"
    )
    sponsorships: "list[Sponsorship]" = Relationship(back_populates="event")


class PersonOrganisationAssociation(SQLModel, table=True):
    __tablename__: ClassVar[str] = "person_organisation_association"
    id: int | None = Field(default=None, primary_key=True)
    oid: int = Field(foreign_key="organisation.id")
    pid: int = Field(foreign_key="person.id")
    jid: int | None = Field(default=None, foreign_key="job_info.id")

    organisation: "Organisation | None" = Relationship(
        back_populates="person_associations"
    )
    person: "Person | None" = Relationship(back_populates="org_associations")
    job_info: "JobInfo | None" = Relationship()
    person_events: "list[PersonEvent]" = Relationship(
        back_populates="person_organisation_association"
    )

    __table_args__ = (
        UniqueConstraint("oid", "pid", name="uq_person_org_oid_pid"),
        Index("ix_person_org_oid_pid", "oid", "pid"),
    )


class PersonEvent(SQLModel, table=True):
    __tablename__: ClassVar[str] = "person_event"
    pid: int = Field(foreign_key="person.id", primary_key=True)
    eid: int = Field(foreign_key="event.id", primary_key=True)
    role: str | None = None
    description: str | None = None
    person_organisation_association_id: int | None = Field(
        default=None, foreign_key="person_organisation_association.id"
    )

    person: "Person | None" = Relationship(back_populates="person_events")
    event: "Event | None" = Relationship(back_populates="person_events")
    person_organisation_association: "PersonOrganisationAssociation | None" = (
        Relationship(back_populates="person_events")
    )

    __table_args__ = (Index("ix_person_event_pid_eid", "pid", "eid"),)


class HelperShift(SQLModel, table=True):
    __tablename__: ClassVar[str] = "helper_shift"
    id: int = Field(sa_column=Column(Integer, primary_key=True))
    pid: int = Field(foreign_key="person.id")
    eid: int = Field(foreign_key="event.id")
    role: str | None = None
    start: datetime | None = None
    end: datetime | None = None

    person: "Person | None" = Relationship(back_populates="helper_shifts")
    event: "Event | None" = Relationship(back_populates="helper_shifts")


class Organisation(SQLModel, table=True):
    __tablename__: ClassVar[str] = "organisation"
    id: int = Field(sa_column=Column(Integer, primary_key=True))
    name: str | None = None

    org_events: "list[OrganisationEvent]" = Relationship(back_populates="organisation")
    person_associations: "list[PersonOrganisationAssociation]" = Relationship(
        back_populates="organisation"
    )


class OrganisationEvent(SQLModel, table=True):
    __tablename__: ClassVar[str] = "organisation_event"
    oid: int = Field(foreign_key="organisation.id", primary_key=True)
    eid: int = Field(foreign_key="event.id", primary_key=True)
    role: str | None = None

    organisation: "Organisation | None" = Relationship(back_populates="org_events")
    event: "Event | None" = Relationship(back_populates="organisation_events")

    __table_args__ = (Index("ix_organisation_event_oid_eid", "oid", "eid"),)


class Sponsorship(SQLModel, table=True):
    __tablename__: ClassVar[str] = "sponsorship"
    id: int = Field(sa_column=Column(Integer, primary_key=True))
    type: str | None = None
    eid: int | None = Field(default=None, foreign_key="event.id")
    organisation_id: int | None = Field(default=None, foreign_key="organisation.id")

    event: "Event | None" = Relationship(back_populates="sponsorships")
    organisation: "Organisation | None" = Relationship()

    # ... existing file continues ...
