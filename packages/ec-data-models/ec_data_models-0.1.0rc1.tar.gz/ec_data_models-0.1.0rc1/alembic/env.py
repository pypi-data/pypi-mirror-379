import os
from logging.config import fileConfig
from typing import TYPE_CHECKING

import alembic.context as context  # type: ignore[attr-defined]
from sqlalchemy import create_engine, engine_from_config, pool

from src.models import models

if TYPE_CHECKING:
    # For static typing only; alembic provides 'context' at runtime.
    from alembic import context as _context  # noqa: F401

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging if present; otherwise set a basic config.
if config.config_file_name:
    fileConfig(config.config_file_name)
else:
    import logging

    logging.basicConfig()

target_metadata = models.SQLModel.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    # Allow overriding the SQLAlchemy URL via -x (CLI), ini, or DATABASE_URL env var
    x_args = context.get_x_argument(as_dictionary=True)
    section = config.get_section(config.config_ini_section) or {}
    url = (
        x_args.get("sqlalchemy.url")
        or config.get_main_option("sqlalchemy.url")
        or section.get("sqlalchemy.url")
        or os.environ.get("DATABASE_URL")
        or os.environ.get("SQLALCHEMY_DATABASE_URI")
    )

    if url:
        connectable = create_engine(url)
    else:
        connectable = engine_from_config(
            section, prefix="sqlalchemy.", poolclass=pool.NullPool
        )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
