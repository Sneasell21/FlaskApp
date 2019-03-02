import uuid

from flask_injector import FlaskInjector

from injector import inject

from services.breeder_provider import BreederProvider


class Breeder(object):

    
    def __init__(self):
        self._search = ""


   
    def search(self) -> list:
        # Do something if you want
        return []

    @inject
    def post(self,data_provider_breeder:BreederProvider, breeder: dict) -> dict:
        breeder = data_provider_breeder.create(breeder)

        return breeder,201
        
    @inject
    def get(self,data_provider_breeder:BreederProvider,name="")->dict:
        return data_provider_breeder.get(name),200
    
    @inject
    def list(self,data_provider_breeder:BreederProvider)->list:
        return data_provider_breeder.breederList(),200

class_instance = Breeder()
