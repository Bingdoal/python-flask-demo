from config import env
from middleware.request_aop import init_request_aop
from migrations.migration import up_migrate
from routes.auth.login import Login
from routes.server import server
from routes.user.user import User
from routes.user.users import Users

if __name__ == '__main__':
    if env.get("db.migration.enabled") is True:
        up_migrate(env.get_str("db.migrations.target"))

    print(f'Server {env.get("server.name")} version:{env.get("server.version")} start on {env.get("server.port")}...')

    init_request_aop()
    server.add_resource("/v1/user/<string:name>", User)
    server.add_resource("/v1/users", Users)
    server.add_resource("/v1/auth/login", Login)
    server.run(env.get("server.port"))
