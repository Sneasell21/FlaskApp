from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase


DATABASE = "./database.db"
database_file = "sqlite:///{}".format(DATABASE)
engine = create_engine(database_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base(cls=(JsonSerializableBase,))
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import model.models
    Base.metadata.create_all(bind=engine)