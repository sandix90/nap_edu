from typing import Dict

from marshmallow import Schema, ValidationError, EXCLUDE
from sanic.exceptions import SanicException


class APIValidateException(SanicException):

    status_code = 400

    def __init__(self, errs: Dict):

        super().__init__(errs)


class RequestDto:
    __schema__: Schema = None

    def __init__(self, data: dict):
        try:

            errors = self.__schema__(unknown=EXCLUDE).validate(data=data)
            if len(errors) > 0:
                raise APIValidateException(errors)

            self._import(data)
        except ValidationError as err:
            raise APIValidateException(errors)

    def _import(self, data: dict):
        for name, field in data.items():
            self.set(name, data[name])

    def set(self, key, value):
        return setattr(self, key, value)


class ResponseDto:
    __schema__ = Schema

    def __init__(self, obj: object):
        properties = [pr for pr in dir(obj) if not pr.startswith('_')]

        for property in properties:
            if property[:1] == '_':
                continue

            self._import_field(obj, property)

    def _import_field(self, source_obj: object, name: str):
        value = source_obj.__getattribute__(name)

        if not callable(value):
            setattr(self, name, value)

    def dump(self) -> dict:
        return self.__schema__().dump(self)
