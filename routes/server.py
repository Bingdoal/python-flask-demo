import logging

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES
from waitress import serve

from config import env
from model import db, db_conn_str
from routes.api_error import ApiError
from utils.ma import ma

level = logging.getLevelName(env.get_str("logger.level").upper())
logging.basicConfig(level=level,
                    format='%(asctime)s: %(name)s:%(lineno)d |%(levelname)s| %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)


class CustomApi(Api):
    def handle_error(self, err: Exception):
        if isinstance(err, HTTPException):
            return jsonify({
                'message': getattr(
                    err, 'description', HTTP_STATUS_CODES.get(err.code, '')
                )
            }), err.code
        elif isinstance(err, ApiError):
            return jsonify({
                'message': err.message
            }), err.code

        logger.exception(err)
        return {
                   "message": str(err)
               }, 500


class __Server:
    app = Flask(__name__)
    __api = CustomApi(app, errors={
        'NoAuthorizationError': {
            'message': "jwt token is invalidate",
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
        serve(self.app, host="0.0.0.0", port=port)


api_server = __Server()
