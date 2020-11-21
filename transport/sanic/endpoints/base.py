from sanic.exceptions import SanicException
from sanic.request import Request
from structlog import getLogger

from api.base import APIValidateException
from db.database import DataBase, DBSession, DBNoResultException
from transport.sanic.base import SanicEndpoint

log = getLogger('BaseSanicEndpoint')


class BaseSanicEndpoint(SanicEndpoint):

    async def _method(self, request: Request, body: dict, *args, **kwargs):
        try:
            database: DataBase = self.context.database
            session: DBSession = database.make_session()

            return await super()._method(request, body, session=session)

        except APIValidateException as e:
            return await self.make_response_json(code=e.status_code, message=str(e))

        except DBNoResultException as e:
            log.error(e)
            return await self.make_response_json(code=400)

        except SanicException as e:
            log.error(e)
            if hasattr(e, 'error_code'):
                return await self.make_response_json(code=e.status_code, error_code=e.error_code, message=str(e))
            else:
                return await self.make_response_json(code=e.status_code, message=str(e))

        except Exception as e:
            return await self.make_response_json(code=500, message=str(e))
