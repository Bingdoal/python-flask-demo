from flask import jsonify
from flask_restful import Resource
from marshmallow import ValidationError

from model.user.user_model import UserModel
from routes.user.user_dto import UserDto
from utils import request_utils


class Users(Resource):
    def get(self):
        users = UserModel()
        return jsonify(users.find_all())

    def post(self):
        body = request_utils.get_body()
        user_dto = UserDto()
        try:
            result = user_dto.load(body)
        except ValidationError as error:
            return {
                       "msg": error.messages
                   }, 433

        user = UserModel()
        user.name = result["name"]
        user.password = result["password"]
        user.email = result["email"]
        user.create()

        return {}, 204
