from models.conection.configs import configs_mongodb_conect
from pymongo import MongoClient

class DBconection:
    def __init__(self):
        self.__conectionString = configs_mongodb_conect.get("conectionIP")
        self.__conectOn = MongoClient(self.__conectionString)
        self.__bankConected = self.__conectOn[configs_mongodb_conect.get("nameOfBank")]
        self.__collection = self.__bankConected.get_collection(configs_mongodb_conect.get("nameOfColection"))
        
    def getColection(self):
        return self.__collection
        
    def findINColection(self, name):
        findVar = self.__collection.find(name)   
        return findVar
    
    