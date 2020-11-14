from sqlalchemy import Column

from db.models.base import BaseModel
from sqlalchemy import VARCHAR


class DBEmployee(BaseModel):
    __tablename__ = 'employees'

    first_name = Column(VARCHAR(50))
    last_name = Column(VARCHAR(50))
