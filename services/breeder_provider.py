from model.models import Breeder
from flask_injector import FlaskInjector

from injector import inject
from persistence.database import db_session
from services.redis_provider import RedisProvider
import json

REDIS_KEY = 'breeder_data'
class BreederProvider(object):
    @inject
    def __init__(self,redis_provider:RedisProvider, list=[]):
        self._redis = redis_provider
        self.updateRedisCache()

        
    def breederList(self) -> list:
        if not self._items:
            self.updateRedisCache()
    
        data = self._redis.get_data(REDIS_KEY)
        ll = dict(data)
        return json.loads(ll["data".encode('utf-8')])     


    def create(self,breeder:dict) -> dict:
        newBreeder = Breeder(fname=breeder["name"])
        db_session.add(newBreeder)
        db_session.commit()
        updateRedisCache()
        return newBreeder.__json__()

    def get(self, name) -> dict:
        breeder = Breeder.query.filter(Breeder.fname == name).first()
        return breeder.__json__()
    
    def updateRedisCache(self):
        self._items = Breeder.query.all()
        self._redis.remove_data(REDIS_KEY)
        self._redis.add_data(REDIS_KEY,{"data": json.dumps(list(map(lambda x: x.__json__(),self._items)))})
  
