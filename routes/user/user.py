from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from routes.user.user_dto import UserDto
from utils import request_utils


class User(Resource):
    def get(self, name=''):
        query = request_utils.get_query()
        print(query)
        user_dto = UserDto()
        try:
            result = user_dto.load(query)
            return result, 200
        except ValidationError as error:
            return {
                       "msg": error.messages
                   }, 433

    def put(self, name):
        pass

    def delete(self, name):
        pass
