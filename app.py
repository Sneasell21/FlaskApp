import connexion
import sqlite3
from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from flask_sqlalchemy import SQLAlchemy
from persistence.database import db_session
from persistence.database import init_db
from persistence.database import Base





from services.dog_provider import DogProvider
from services.breeder_provider import BreederProvider
from services.redis_provider import RedisProvider

init_db()

def configure(binder: Binder) -> Binder:
    binder.bind(
        DogProvider,
        DogProvider,
    )
    binder.bind(
        BreederProvider,
        BreederProvider
    )
    binder.bind(
        RedisProvider,
        RedisProvider
    )
    
if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('dog_running_app.yaml', resolver=RestyResolver('api'))
    application = app.app
    FlaskInjector(app=application, modules=[configure])
    app.run(host='0.0.0.0', port=8098)
