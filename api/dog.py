import uuid

from flask_injector import FlaskInjector

from injector import inject

from services.dog_provider import DogProvider
import json
import pickle
class Dog(object):

    
    def __init__(self):
        self._search = ""

    def search(self) -> list:
        # Do something if you want
        return []

    @inject
    def post(self,data_provider:DogProvider,dog: dict) -> dict:
        
        dogg = data_provider.create(self.cleanInput(dog))
        return dogg, 201
        
    @inject
    def get(self, data_provider:DogProvider,name="")-> dict:
        dog = data_provider.get_one_by_name({"name":name})
        return dog,200

    @inject
    def list(self,data_provider:DogProvider,sort:str)->list:
        items = data_provider.get()
        sorted_lst = sorted(items,key=lambda x: x[sort])
        return sorted_lst,200
    
    @inject
    def update(self,data_provider:DogProvider,name,dog: dict)->dict:
        dog.update({"name":name})   
        dogg = data_provider.update(self.cleanInput(dog))
        return dogg,200

    @inject
    def summarized_data(self,data_provider:DogProvider)->dict:
        age_avg = data_provider.average_age()
        weight_avg = data_provider.average_weight()
        return {"age average":age_avg, "weight average":weight_avg },200
    
    def cleanInput(self,dog:dict)->dict:
        name = dog["name"] # this is mandatory
        age = dog["age"] if "age" in dog else 0
        weight = dog["weight"] if "weight" in dog else 0
        breeder = dog["breeder"] if "breeder" in dog else {}
        return  {
            "name":name,
            "age":age,
            "weight":weight,
            "breeder":breeder
        }
    

class_instance = Dog()
