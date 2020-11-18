from http import HTTPStatus

from sanic.request import Request
from sanic.response import BaseHTTPResponse, json as JsonResponse

from configs.config import ApplicationConfig
from context import Context


def import_body_json(request: Request) -> dict:
    if 'application/json' in request.content_type and request.json is not None:
        return dict(request.json)

    return {}


def import_body_headers(request: Request) -> dict:
    headers = {}

    for header in request.headers:
        if header[:2].lower() == 'x-':
            headers[header] = request.headers[header]

    return headers


class SanicEndpoint:

    async def __call__(self, *args, **kwargs):
        return await self.handle(*args, **kwargs)

    def __init__(self, config: ApplicationConfig, context: Context, uri, methods, *args, **kwargs):
        self.config = config
        self.uri = uri
        self.methods = methods
        self.context = context
        self.__name__ = self.__class__.__name__

    async def handle(self, request: Request, *args, **kwargs):
        body = {}

        body.update(import_body_json(request))
        # body['auth'] = auth

        return await self._method(request, body, *args, **kwargs)

    async def _method(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        method = request.method.lower()
        func_name = f'method_{method}'

        if hasattr(self, func_name):
            func = getattr(self, func_name)

            return await func(request, body, *args, **kwargs)
        else:
            return await self.make_response_json(code=405, message='Method Not Allowed')

    async def method_get(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.make_response_json(code=500, message=f'{request.method} Not Impl')

    async def method_head(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.make_response_json(code=500, message=f'{request.method} Not Impl')

    async def method_post(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.make_response_json(code=500, message=f'{request.method} Not Impl')

    async def method_put(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.make_response_json(code=500, message=f'{request.method} Not Impl')

    async def method_delete(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.make_response_json(code=500, message=f'{request.method} Not Impl')

    async def method_connect(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.make_response_json(code=500, message=f'{request.method} Not Impl')

    async def method_options(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.make_response_json(code=500, message=f'{request.method} Not Impl')

    async def method_trace(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.make_response_json(code=500, message=f'{request.method} Not Impl')

    async def method_patch(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:
        return await self.make_response_json(code=500, message=f'{request.method} Not Impl')

    @staticmethod
    async def make_response_json(code: int = 200, message: str = None, data: dict = None, error_code: int = None) -> BaseHTTPResponse:
        if data is not None:
            return JsonResponse(data)

        if message is None:
            message = HTTPStatus(code).phrase

        if error_code is None:
            error_code = code

        data = {
            'code': error_code,
            'message': message
        }

        return JsonResponse(data, status=code)
