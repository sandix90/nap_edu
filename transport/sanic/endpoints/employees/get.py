from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request.get_employee import RequestGetEmployeeDto
from db.database import DBSession
from db.queries import employees as employees_queries
from transport.sanic.endpoints.base import BaseSanicEndpoint


class GetEmployeeEndpoint(BaseSanicEndpoint):

    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        request_model = RequestGetEmployeeDto(body)
        dbEmployee = employees_queries.GetEmployeeById(session=session, user_id=request_model.eid)

        return await self.make_response_json(code=200)