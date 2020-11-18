from sqlalchemy import create_engine

from configs.config import ApplicationConfig
from context import Context
from db.database import DataBase


def init_sqlite_db(context: Context, config: ApplicationConfig):
    """
    :param context: Mutable
    """

    engine = create_engine(
        f'sqlite:///db.sqlite',
        pool_pre_ping=True
    )
    engine.execute('pragma foreign_keys=on')
    database = DataBase(engine)
    # database.check_connection()
    context.set("database", database)
