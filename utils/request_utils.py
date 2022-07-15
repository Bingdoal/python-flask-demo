from flask import request


def get_query():
    return request.args.to_dict()


def get_body():
    data = request.json
    if data is None:
        data = request.form
    return data
