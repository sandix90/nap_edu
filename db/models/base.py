import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, TIMESTAMP, func

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.utcnow, server_default=func.datetime('now'))
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.utcnow, server_default=func.datetime('now'), onupdate=func.datetime('now'))

    def __repr__(self):
        return f'{self.__name__}'
