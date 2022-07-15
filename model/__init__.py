from flask_sqlalchemy import SQLAlchemy

from config import env

db = SQLAlchemy()


db_conn_str = f'mysql+pymysql://' \
              f'{env.get("db.mysql.user")}:{env.get("db.mysql.pwd")}@' \
              f'{env.get("db.mysql.host")}:{env.get("db.mysql.port")}/{env.get("db.mysql.database")}'
