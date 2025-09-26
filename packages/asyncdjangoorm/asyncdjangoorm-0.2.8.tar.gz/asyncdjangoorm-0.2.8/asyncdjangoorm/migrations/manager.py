import os
from pathlib import Path
from alembic import command
from alembic.config import  Config
from alembic.script import ScriptDirectory
from alembic.runtime.environment import EnvironmentContext
from sqlalchemy.engine.url import make_url
from asyncdjangoorm.config.base import Base
from asyncdjangoorm.utils.settings_loader import load_settings_module


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
    """
    Build an alembic Config for the *current project* (settings discovered by load_settings_module).
    It also returns migration_dir so callers know where the project's migrations folder is.
    """
    try:
        settings = load_settings_module()
        project_dir = Path(settings.__file__).resolve().parent
    except Exception:
        # fallback to cwd
        project_dir = Path.cwd()

    migrations_dir = project_dir / "migrations"
    if not migrations_dir.exists():
        # fallback: create minimal migrations dir (versions subfolder) to avoid Alembic errors
        versions_dir = migrations_dir / "versions"
        versions_dir.mkdir(parents=True, exist_ok=True)

    # find DB URL (prefer settings attr)
    db_url = None
    try:
        settings = load_settings_module()
        db_url = getattr(settings, "DATABASE_URL", None)
    except Exception:
        db_url = os.getenv("DATABASE_URL")

    if not db_url:
        db_url = "sqlite+aiosqlite:///./db.sqlite3"

    sync_url = _to_sync_url(db_url)
    cfg = Config()
    cfg.set_main_option("script_location", str(migrations_dir))
    cfg.set_main_option("sqlalchemy.url", sync_url)
    # also keep settings module reference in cfg.attrs if needed
    cfg.attributes["project_dir"] = str(project_dir)
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