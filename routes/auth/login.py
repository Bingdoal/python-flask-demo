import datetime

from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from flask_restful import Resource

from utils.request_utils import get_body


class Login(Resource):
    @jwt_required()
    def get(self):
        return get_jwt()

    def post(self):
        body = get_body()
        username = body.get("username")
        pwd = body.get("password")

        token = create_access_token(identity=username, additional_claims={
            "test": "ttt"
        }, expires_delta=datetime.timedelta(days=20))

        return {
                   "token": token
               }, 200
