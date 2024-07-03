from models.conection.conection import DBconection
from models.repository.myConection import MyConection


class Api():
    def __init__(self):
       self.mongoDB = DBconection()                           
       self.mongodbConection = MyConection(self.mongoDB,self.mongoDB.getColection())
       
            
    def addDayMongoDB(self, ):
        pass
       
    def getFinuras(self):
        pass
    
    def getTotalofDay(self, name):
        totalDay = self.mongodbConection.findINcolection(name)
        return totalDay
             
    def getMountId(self):
        pass
      
    def addDayAgulhaMongoDB(self, data):    
        self.mongodbConection.insert_document(data)
    
    def sumTotalDay(self):
       self.mongodbConection.sumTotalDay()
    
  