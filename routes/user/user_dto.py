from marshmallow import validate

from utils.ma import ma


class UserDto(ma.Schema):
    name = ma.Str(required=True, validate=[validate.Length(min=1)])
    email = ma.Email(required=True)
    password = ma.Str(required=True, validate=[validate.Length(min=1)])
