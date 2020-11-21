from marshmallow import fields, Schema

from api.base import ResponseDto


class ResponseEmployeeSchema(Schema):
    id = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    first_name = fields.Str()
    last_name = fields.Str()


class ResponseEmployee(ResponseDto):
    __schema__ = ResponseEmployeeSchema
