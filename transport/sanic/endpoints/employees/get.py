from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestGetEmployeeDto
from api.response import ResponseEmployee
from db.database import DBSession, DBNoResultException
from db.queries import employees as employees_queries
from .. import exceptions
from ..base import BaseSanicEndpoint


class GetEmployeeEndpoint(BaseSanicEndpoint):

    async def method_get(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:
        request_model = RequestGetEmployeeDto(body)
        try:

            dbEmployee = employees_queries.get_employee_by_id(session=session, user_id=request_model.eid)
        except DBNoResultException:
            raise exceptions.UserNotFoundException

        responseModel = ResponseEmployee(dbEmployee)
        return await self.make_response_json(code=200, data=responseModel.dump())
