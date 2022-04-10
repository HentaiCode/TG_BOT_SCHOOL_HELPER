from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import current_app as app
import os

engine = create_engine('sqlite:///blogs.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
SqlAlchemyBase = declarative_base()
SqlAlchemyBase.query = db_session.query_property()


def init_db():
    from database import models
    SqlAlchemyBase.metadata.create_all(engine)