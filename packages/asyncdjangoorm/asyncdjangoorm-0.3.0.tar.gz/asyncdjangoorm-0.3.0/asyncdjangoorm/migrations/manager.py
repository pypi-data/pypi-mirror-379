import os
from pathlib import Path
from alembic import command
from alembic.config import  Config
from alembic.script import ScriptDirectory
from alembic.runtime.environment import EnvironmentContext
from sqlalchemy.engine.url import make_url
from asyncdjangoorm.config.base import Base
from asyncdjangoorm.utils.settings_loader import load_settings_module
from asyncdjangoorm.migrations.ensure import ensure_migrations_setup
from asyncdjangoorm.migrations.env import get_sync_url_and_metadata

Base_DIR = Path(__file__).resolve().parent.parent
MIGRATIONS_DIR = Base_DIR / "migrations"

def _to_sync_url(async_url: str) -> str:
    url = make_url(async_url)
    ds = url.drivername or ""
    # map async drivers -> sync drivers
    if ds.startswith("sqlite+aiosqlite"):
        url = url.set(drivername="sqlite")
    elif ds.startswith("postgresql+asyncpg"):
        url = url.set(drivername="postgresql+psycopg2")
    elif ds.startswith("mysql+aiomysql"):
        url = url.set(drivername="mysql+pymysql")
    return str(url)




def _get_alembic_config() -> Config:
    # Ensure everything is ready before returning config
    migrations_dir = ensure_migrations_setup()
    _, sync_url, _ = get_sync_url_and_metadata()

    cfg = Config()
    cfg.set_main_option("script_location", str(migrations_dir))
    cfg.set_main_option("sqlalchemy.url", sync_url)
    cfg.attributes["project_dir"] = str(migrations_dir.parent)
    return cfg


def makemigrations(message="auto migration"):
    cfg = _get_alembic_config()
    # autogeneration will be driven by the env.py inside project migrations/
    command.revision(cfg, message=message, autogenerate=True)

def migrate(target="head"):
    cfg = _get_alembic_config()
    command.upgrade(cfg, target)

def rollback(target="-1"):
    cfg = _get_alembic_config()
    command.downgrade(cfg, target)