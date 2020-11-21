from sanic.exceptions import SanicException

_codes_messages = {
    10000: '',
    10001: 'User not found',
}


class UsersException(SanicException):

    error_code: int

    def __init__(self):
        message = None
        try:
            message = _codes_messages[self.error_code]
        except Exception as e:
            pass
        finally:
            super().__init__(message=message)


class UserNotFoundException(UsersException):
    error_code = 10001
    status_code = 404

