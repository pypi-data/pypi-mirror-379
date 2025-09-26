# migrations/env.py (place into your project template migrations/)
from logging.config import fileConfig
import os
import importlib
from pathlib import Path
from alembic import context
from sqlalchemy import create_engine
from sqlalchemy.engine.url import make_url
from asyncdjangoorm.utils.settings_loader import load_settings_module
from asyncdjangoorm.migrations.manager import _get_alembic_config
from asyncdjangoorm.migrations.ensure import ensure_migrations_setup

settings = load_settings_module()
project_dir = Path(settings.__file__).resolve().parent
migrations_dir = project_dir / "migrations"
migrations_dir.mkdir(parents=True, exist_ok=True)

def get_sync_url_and_metadata():
    migrations_dir = ensure_migrations_setup()

    settings = load_settings_module()
    async_url = getattr(settings, "DATABASE_URL", None)
    if async_url is None:
        raise RuntimeError("DATABASE_URL is not set in settings.py")
    
    url = make_url(async_url)
    drv = url.drivername or ""
    if drv.startswith("sqlite+aiosqlite"):
        sync_url = str(url.set(drivername="sqlite"))
    elif drv.startswith("postgresql+asyncpg"):
        sync_url = str(url.set(drivername="postgresql+psycopg2"))
    elif drv.startswith("mysql+aiomysql"):
        sync_url = str(url.set(drivername="mysql+pymysql"))
    else:
        sync_url = str(url)

    # target metadata for autogenerate
    target_metadata = None
    meta_spec = getattr(settings, "ASYNCDJANGO_TARGET_METADATA", None)
    if isinstance(meta_spec, str):
        if ":" in meta_spec:
            mod_name, attr = meta_spec.split(":", 1)
        else:
            mod_name, attr = meta_spec, "metadata"
        mod = importlib.import_module(mod_name)
        target_metadata = getattr(mod, attr, None)    
    else:
        from asyncdjangoorm.config.base import Base
        target_metadata = Base.metadata

    # create env.py if missing
    env_py = migrations_dir / "env.py"
    if not env_py.exists():
        env_py.write_text(
            "from asyncdjangoorm.migrations.manager import run_migrations\n"
            "run_migrations()\n",
            encoding="utf-8"
        )

    return sync_url, target_metadata




def run_migrations_offline():
    sync_url, target_metadata = get_sync_url_and_metadata()
    context.configure(
        url=sync_url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        compare_server_default=True,
    )
    with context.begin_transaction():
        context.run_migrations()



def run_migrations_online():
    sync_url, target_metadata = get_sync_url_and_metadata()
    engine = create_engine(sync_url)
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )
        with context.begin_transaction():
            context.run_migrations()


def run_migrations():
    """Entry point for Alembic."""
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()


