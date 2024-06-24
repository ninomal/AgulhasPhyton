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
       
    def addDayMongoDB(self, day, finuras, agulhas, turno, setor):
        finurasFunc = self.addFinuras(finuras, agulhas)
        agulhasDict = self.addAgulhasinDictList()
        dayMongo = self.addDay(day,setor, turno,  finurasFunc)
  
    def addDay(self, day , setor, turno, finuras : Dict, agulhasDictList : Dict) -> Dict:
        dayStr = str(day)
        dictDay = {dayStr : {setor :{turno: {finuras : agulhasDictList}}}}
        return dictDay
             
    def addFinuras(self, finuras, agulhas):
        finurasDict = {finuras: agulhas}
        return finurasDict
        
    def addAgulhasinDictList(self,finuras, agulhasData ):
        self.listNeedlesBrokenDay.append[{finuras : agulhasData}]
        return self.listNeedlesBrokenDay
    
    def clearList(self):
        self.listNeedlesBrokenDay = []
        
    def sumOfDay(self, data : Dict) -> Dict:
        result = dict(functools.reduce(operator.add,
                        map(collections.Counter, data)))
        return result

    def addTotalOfDay(self ):
        listOfDay = self.listNeedlesBrokenDay
        #name
        #add value
        
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
    
  