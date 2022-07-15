from alembic import command
from alembic.config import Config

from config import env
from model import db_conn_str


def up_migrate(version="heads"):
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', env.get_str("db.migration.path"))
    alembic_cfg.set_main_option('sqlalchemy.url', db_conn_str)
    command.upgrade(alembic_cfg, version)


def down_migrate(version="0000_base_line"):
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', env.get_str("db.migration.path"))
    alembic_cfg.set_main_option('sqlalchemy.url', db_conn_str)
    command.downgrade(alembic_cfg, version)
