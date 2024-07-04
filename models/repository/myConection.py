from typing import Dict

class MyConection:
    def __init__(self, dbconection,  colection):
        self.__dbConection = dbconection
        #self.__nameOfBank = nameOfBank
        self.__collection = colection
    
    def getDay(self, day: Dict):
        dayResult = self.__collection.find(day)  
        return dayResult
        
    def insert_document(self, document: Dict) -> Dict:
        self.__collection.insert_one(document)
               
    def findINcolection(self, name):
        findColection = self.__collection.find(name)
        return findColection
    
    def deleteTurn(self, turn : Dict):
        self.__collection.deleteOne(turn) 
        
    def deleteDay(self, day : Dict):
        self.__collection.deleteOne(day)