from sanic.request import Request

from api.base import APIValidateException
from db.database import DataBase, DBSession
from transport.sanic.base import SanicEndpoint


class BaseSanicEndpoint(SanicEndpoint):

    async def _method(self, request: Request, body: dict, *args, **kwargs):
        try:
            database: DataBase = self.context.database
            session: DBSession = database.make_session()

            return await super()._method(request, body, session=session)

        except APIValidateException as e:
            return await self.make_response_json(code=e.status_code, message=str(e))

        except Exception as e:
            return await self.make_response_json(code=500, message=str(e))
