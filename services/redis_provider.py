import redis
import os


class RedisProvider(object):
    def __init__(self):
        self._redis = redis.Redis(host=os.environ['REDIS_URL'],port=int(os.environ['REDIS_PORT']))
        self._ttl = 31104000 #one year
        
    def add_data(self,key,data:dict):
        self._redis.hmset(key, data)

    def remove_data(self,key=""):
        self._redis.delete(key) #remove old keys

    def expire_data(self, key,ttl):
        self._redis.expire(key, ttl)
    
    def checkIfExist(self,key)-> bool:
        return self._redis.exists(key)

    def get_data(self,key="")-> list:
        return self._redis.hgetall(key)
