from models.configs import configs_mongodb_conect
from pymongo import MongoClient

class DBconection:
    def __init__(self):
        self.conectionString = configs_mongodb_conect.get("conectionIP")
        self.conectOn = MongoClient(self.conectionString)
        self.bankConected = self.conectOn[configs_mongodb_conect.get("nameOfBank")]
        self.colection = self.bankConected.get_collection(configs_mongodb_conect.get("nameOfColection"))
        
    def getColection(self):
        return self.colection
        