from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv


load_dotenv()
DB_PATH = os.getenv('DB_PATH')

engine = create_engine(f'sqlite:///{DB_PATH}')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
SqlAlchemyBase = declarative_base()
SqlAlchemyBase.query = db_session.query_property()


def init_db():
    from database import models
    SqlAlchemyBase.metadata.create_all(engine)
