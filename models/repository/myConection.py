from typing import Dict

class MyConection:
    def __init__(self, dbconection,  colection):
        self.__dbConection = dbconection
        #self.__nameOfBank = nameOfBank
        self.__collection = colection
        
    def insert_document(self, document: Dict) -> Dict:
        self.__collection.insert_one(document)
        
    def getColection(self):
        self.getColection()
        
    def findINcolection(self, name):
        findColection = self.__collection.find(name)
        return findColection
    
    def sumTotalDay(self):
        query = {"0207.RASCH.total": {"$elemMatch": {"3975": 20}}}
        projection = {"_id": "6684956ed595b0a13d0913", "0207.RASCH.total.$": 1}
        result = list(self.__collection.find(query, projection))
        return result