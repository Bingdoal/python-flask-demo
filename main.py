from config import env
from migrations.migration import up_migrate, down_migrate
from routes.server import Server
from routes.user.user import User
from routes.user.users import Users

if __name__ == '__main__':
    if env.get("db.migrations.enabled") is True:
        up_migrate(env.get_str("db.migrations.target"))

    print(f'Server {env.get("server.name")} version:{env.get("server.version")} start on {env.get("server.port")}...')

    server = Server()
    server.add_resource("/v1/user/<string:name>", User)
    server.add_resource("/v1/users", Users)
    server.run(env.get("server.port"))
