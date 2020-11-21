from sqlalchemy.orm.exc import NoResultFound
from structlog import getLogger

from api.request import RequestCreateEmployeeDto
from db.database import DBSession, DBNoResultException
from db.models import DBEmployee

log = getLogger('Employees queries')


def get_employee_by_id(session: DBSession, user_id: int) -> DBEmployee:
    try:
        user = session.query(DBEmployee).filter(DBEmployee.id == user_id).one()
    except NoResultFound:
        log.error("User is not found")
        raise DBNoResultException

    return user


def create_employee(session: DBSession, user: RequestCreateEmployeeDto) -> DBEmployee:
    user = DBEmployee(
        first_name=user.first_name,
        last_name=user.last_name
    )
    session.add_model(user, need_flush=True)

    return user
