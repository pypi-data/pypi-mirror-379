from pathlib import Path
from asyncdjangoorm.utils.settings_loader import load_settings_module



def ensure_migrations_setup():
    settings = load_settings_module()
    project_dir = Path(settings.__file__).resolve().parent
    migrations_dir = project_dir / "migrations"
    versions_dir = migrations_dir / "versions"

    # create folders if missing
    versions_dir.mkdir(parents=True, exist_ok=True)

    # create env.py if missing
    env_py = migrations_dir / "env.py"
    if not env_py.exists():
        env_py.write_text(
            "from asyncdjangoorm.migrations.manager import run_migrations\n"
            "run_migrations()\n",
            encoding="utf-8"
        )

    # create script.py.mako if missing
    mako_template = migrations_dir / "script.py.mako"
    if not mako_template.exists():
        mako_template.write_text(
            '''"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

def upgrade():
    ${upgrades if upgrades else "pass"}

def downgrade():
    ${downgrades if downgrades else "pass"}
''',
            encoding="utf-8"
        )

    return migrations_dir

