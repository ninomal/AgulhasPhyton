from models.conection.conection import DBconection
from models.repository.myConection import MyConection
from enums.enumsFinuras import EnumsFinuras
from typing import Dict
import collections, functools, operator

class Api():
    def __init__(self):
       self.mongoDB = DBconection()                           
       self.mongodbConection = MyConection(self.mongoDB,self.mongoDB.getColection())
       self.enumsFinuras = EnumsFinuras()
       self.listNeedlesBrokenDay = []        
  
    def addDayMongodb(self, day , dictData ):
        dictDay = {day : dictData}
        return dictDay
        
    def addFinurasAgulhasMongodb(self, finuras, agulhas ) :
        finurasDict = {finuras: agulhas}
        return finurasDict
        
    def addAgulhasinDictList(self,finuras, agulhasData ):
        finurasStr = str(self.enumsFinuras.finurasEnumsSelect(finuras))
        self.listNeedlesBrokenDay.append[{finurasStr : agulhasData}]
        return self.listNeedlesBrokenDay
    
    def clearList(self):
        self.listNeedlesBrokenDay = []
        
    def sumOfDay(self, data : Dict) -> Dict:
        result = dict(functools.reduce(operator.add,
                        map(collections.Counter, data)))
        return result

    def addTotalOfDayMongodb(self, totalOfDay : Dict ) -> Dict:
        self.mongodbConection.insert_document(totalOfDay)
        
    def getFinuras(self):
        pass
    
    def getTotalofDay(self):
        return self.listNeedlesBrokenDay
             
    def getMountId(self):
        pass
      
    def teste(self):
        teste = {"teste": 14141416789}
        self.mongodbConection.insert_document(teste)
        #dbt_colect = self.mongodbConection.getColection()
        #print(dbt_colect)
    
  