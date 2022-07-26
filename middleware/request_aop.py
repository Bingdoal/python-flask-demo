from flask import request
from flask.typing import ResponseClass

from routes.server import server


@server.app.before_request
def before_request():
    print("before request.", request.url)


@server.app.after_request
def after_request(response: ResponseClass):
    status_as_string = response.status
    status_as_integer = response.status_code
    print("after request.", status_as_string, status_as_integer, response.json)
    return response


def init_request_aop():
    return
