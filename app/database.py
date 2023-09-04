
from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import get_settings

from sqlalchemy.orm import object_mapper, class_mapper

from typing import Generator, Any


engine = create_engine(str(get_settings().db_url), pool_pre_ping=True)


@lru_cache
def create_session():
    session = scoped_session(
        sessionmaker(autoflush=False, autocommit=False, bind=engine)
    )
    return session

def get_session() -> Generator[scoped_session, None, None]:
    Session = create_session()
    try:
        yield Session
    except:
        Session.remove()

Base: Any = declarative_base()


def sqlalchemy_to_dict(obj):
    if hasattr(obj, '__table__'):
        mapper = class_mapper(obj.__class__)
    else:
        mapper = object_mapper(obj)
    columns = [column.key for column in mapper.columns]
    return {column: getattr(obj, column) for column in columns}