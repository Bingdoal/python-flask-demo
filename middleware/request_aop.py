import logging

from flask import request
from flask.typing import ResponseClass

from routes.server import api_server

logger = logging.getLogger(__name__)


@api_server.app.before_request
def before_request():
    logger.info(f"[Request]: {request.method} {request.path}")


@api_server.app.after_request
def after_request(response: ResponseClass):
    status_as_string = response.status
    logger.info(f"[Response]: {request.method} {request.path}: {status_as_string}")
    return response


def init_request_aop():
    return
