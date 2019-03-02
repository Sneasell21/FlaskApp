from model.models import Dog
from model.models import Breeder
from flask_injector import FlaskInjector

from injector import inject
from persistence.database import db_session
from services.redis_provider import RedisProvider
import json

REDIS_KEY = 'dog_data_list'

class DogProvider(object):

    @inject
    def __init__(self,redis_provider:RedisProvider, dogs: list=[]):
        self._redis = redis_provider
        self.updateRedisCache()
        
    
    @inject
    def get(self) -> list:
        data = self._redis.get_data(REDIS_KEY)
        ll = dict(data)
        return json.loads(ll["data".encode('utf-8')])
    
    def get_one_by_name(self, dog: dict) -> dict:
        dogo = Dog.query.filter(Dog.fname == dog["name"]).first()
        return dogo.__json__()

    def create(self, dog:dict)-> dict:
        newDog = Dog(fname=dog["name"],age=dog["age"],weight=dog["weight"])
        db_session.add(newDog)
        db_session.commit()
        updateRedisCache()
        return newDog.__json__()

    def update(self,dog:dict)-> dict:
        doggo = Dog.query.filter(Dog.fname == dog["name"]).first()
        doggo.age = dog["age"] if "age" in dog else doggo.age
        doggo.weight = dog["weight"] if "weight" in dog else doggo.weight
        breeder = dog["breeder"] if "breeder" in dog else doggo.breeder
        if (breeder):
            breeder = Breeder.query.filter(Breeder.fname == dog["breeder" ]["name"]).first()
            if breeder :
                doggo.breeder = breeder
            else:
                if ("name" in dog):
                    newBreeder = Breeder(fname=dog["breeder" ]["name"])
                    db_session.add(newBreeder)
                    db_session.commit()
                    doggo.breeder = newBreeder

        db_session.merge(doggo)
        db_session.commit()
        updateRedisCache()
        return doggo.__json__()
    
    def average_age(self):
         data_list = self.get()
         total = sum( map(lambda x:x['age'],data_list))
         return total/len(data_list)

    def average_weight(self):
         data_list =  self.get()
         total = sum( map(lambda x:x['weight'],data_list))
         return total/len(data_list)    
    


    def updateRedisCache(self):
        self._items = Dog.query.all()
        self._redis.remove_data(REDIS_KEY)
        self._redis.add_data(REDIS_KEY,{"data": json.dumps(list(map(lambda x: x.__json__(),self._items)))})


