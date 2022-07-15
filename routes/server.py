from flask import Flask
from flask_restful import Api

from model import db, db_conn_str
from utils.ma import ma


class Server:
    __app = Flask(__name__)
    __api = Api(__app)

    def add_resource(self, path, resource):
        self.__api.add_resource(resource, path)

    def run(self, port=5000):
        self.__app.config["SQLALCHEMY_DATABASE_URI"] = db_conn_str
        self.__app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(self.__app)
        ma.init_app(self.__app)
        self.__app.run(port=port)
