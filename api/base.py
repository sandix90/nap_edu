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
            if errors is not None:
                raise APIValidateException(errors)

            self._import(data)
        except ValidationError as err:
            raise APIValidateException(errors)

    def _import(self, data: dict):
        for name, field in self.__schema__.declared_fields.items():
            self.set(name, data[name])

    def set(self, key, value):
        return setattr(self, key, value)


class ResponseDto:
    __schema__: Schema = None
    data: object = None

    def __init__(self, data: object):
        self.__schema__.load(data)

    def dump(self) -> dict:
        return self.__schema__.dump(self).data
