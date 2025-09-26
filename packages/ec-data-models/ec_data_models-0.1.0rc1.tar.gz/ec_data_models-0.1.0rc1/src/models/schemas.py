from datetime import datetime

from sqlmodel import SQLModel


class PersonRead(SQLModel):
    id: int
    email: str
    username: str | None
    first_name: str | None
    last_name: str | None
    created_at: datetime


class PersonCreate(SQLModel):
    email: str
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class PersonUpdate(SQLModel):
    email: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class OrganisationRead(SQLModel):
    id: int
    name: str | None


class OrganisationCreate(SQLModel):
    name: str | None = None
