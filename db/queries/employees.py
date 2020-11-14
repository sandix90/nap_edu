from structlog import getLogger

from db.database import DBSession, DBNoResultException
from db.models import DBEmployee

log = getLogger('Employees queries')


def GetEmployeeById(session: DBSession, user_id: int) -> DBEmployee:
    user = None
    try:
        user = session.query(DBEmployee).filter(DBEmployee.id == user_id).one()
    except DBNoResultException:
        log.error("User is not found")

    return user
