from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES

from model import db, db_conn_str
from utils.ma import ma


class CustomApi(Api):
    def handle_error(self, err: Exception):
        if isinstance(err, HTTPException):
            return jsonify({
                'message': getattr(
                    err, 'description', HTTP_STATUS_CODES.get(err.code, '')
                )
            }), err.code
        print("handle_error: ", err)
        return str(err), 500


class Server:
    app = Flask(__name__)
    __api = CustomApi(app, errors={
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
        self.app.run(port=port, debug=True)


server = Server()
