from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from model import db, db_conn_str
from utils.ma import ma


class Server:
    app = Flask(__name__)
    __api = Api(app, errors={
        'NoAuthorizationError': {
            'message': "access_token is invalidate",
            'status': 409,
        }
    })
    jwt = JWTManager()

    def add_resource(self, path, resource):
        self.__api.add_resource(resource, path)

    def run(self, port=5000):
        self.app.config["SQLALCHEMY_DATABASE_URI"] = db_conn_str
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['JWT_SECRET_KEY'] = 'MY_SECRET'

        self.jwt.init_app(self.app)
        db.init_app(self.app)
        ma.init_app(self.app)
        self.app.run(port=port)


server = Server()
