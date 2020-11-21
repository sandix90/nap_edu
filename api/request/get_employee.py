from marshmallow import fields, Schema

from api.base import RequestDto


class RequestGetEmployeeDtoSchema(Schema):
    eid = fields.Int(required=True, allow_none=False)


class RequestGetEmployeeDto(RequestDto, RequestGetEmployeeDtoSchema):
    __schema__ = RequestGetEmployeeDtoSchema
