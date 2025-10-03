from logging.config import fileConfig
from sqlalchemy import pool, create_engine
from alembic import context
from sqlmodel import SQLModel
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Import semua model agar metadata kebaca
from app.models import *

# Ambil config Alembic
config = context.config

# Ambil DATABASE_URL dari .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Set URL ke Alembic config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata
target_metadata = SQLModel.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
