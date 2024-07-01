from typing import Dict

class MyConection:
    def __init__(self, dbconection,  colection):
        self.__dbConection = dbconection
        #self.__nameOfBank = nameOfBank
        self.__colection = colection
        
    def insert_document(self, document: Dict) -> Dict:
        self.__colection.insert_one(document)
        
    def getColection(self):
        self.getColection()
        
    def findINcolection(self, name):
        findColection = self.__colection.find(name)
        return findColection