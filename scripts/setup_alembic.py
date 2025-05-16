"""
Script to initialize and setup Alembic migrations.
"""

import os
import sys
from pathlib import Path
import subprocess

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import models to ensure they're available to Alembic
from app.models.models import User, Conversation, Message


def setup_alembic():
    """Initialize Alembic and create initial migration."""
    # Create migrations directory
    migrations_dir = project_root / "migrations"
    migrations_dir.mkdir(exist_ok=True)
    
    # Create alembic.ini file
    alembic_ini = """
[alembic]
script_location = migrations
prepend_sys_path = .
version_path_separator = os

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
    """
    
    with open(project_root / "alembic.ini", "w") as f:
        f.write(alembic_ini.strip())
    
    # Create migrations directory structure
    env_py = """
import os
import sys
from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import models module
from app.models.models import Base
from app.database.connection import DATABASE_URL

# Alembic Config object
config = context.config

# Set the DB URL in the alembic config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for autogenerate support
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
    """
    
    # Create migrations directory and env.py
    migrations_path = migrations_dir
    migrations_path.mkdir(exist_ok=True)
    
    versions_path = migrations_path / "versions"
    versions_path.mkdir(exist_ok=True)
    
    with open(migrations_path / "env.py", "w") as f:
        f.write(env_py.strip())
    
    # Create __init__.py
    with open(migrations_path / "__init__.py", "w") as f:
        f.write('"""Alembic migrations package."""\n')
    
    # Create script.py.mako template
    script_py_mako = """\"\"\"${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

\"\"\"
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade() -> None:
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    ${downgrades if downgrades else "pass"}
"""
    
    with open(migrations_path / "script.py.mako", "w") as f:
        f.write(script_py_mako)
    
    print("Alembic setup complete. Migration files created.")


if __name__ == "__main__":
    setup_alembic()
