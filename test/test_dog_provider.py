import os
import unittest

DATABASE = "./database.db"
database_file = "sqlite:///{}".format(DATABASE)

class DogProviderTest(unittest.TestCase):
    
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):

    # executed after each test
    def tearDown(self):
        pass
        

    def test_get(self):
        pass

    def test_get_one_by_name(self):
        pass
    def test_create(self):
        pass
    def test_update(self):
        pass
    def test_average_age(self):
        pass
    def test_average_weight(self):
        pass

 

