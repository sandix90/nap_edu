from sanic.request import Request
from sanic.response import BaseHTTPResponse
from structlog import getLogger

from api.request import RequestCreateEmployeeDto
from api.response import ResponseEmployee
from db.database import DBSession
from db.queries import employees as employees_queries
from transport.sanic.endpoints.base import BaseSanicEndpoint

log = getLogger('CreateEmployeeEndpoint')


class CreateEmployeeEndpoint(BaseSanicEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        request_model = RequestCreateEmployeeDto(body)

        dbEmployee = employees_queries.create_employee(session, request_model)

        session.commit_session()

        response_model = ResponseEmployee(dbEmployee)
        return await self.make_response_json(code=200, data=response_model.dump())
