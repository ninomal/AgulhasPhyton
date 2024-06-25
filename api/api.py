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
    
    def getTotalofDay(self):
        pass
             
    def getMountId(self):
        pass
      
    def teste(self, data):      
        print(data)
        self.mongodbConection.insert_document(data)
        #dbt_colect = self.mongodbConection.getColection()
        #print(dbt_colect)
    
  