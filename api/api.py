from models.conection.conection import DBconection
from models.repository.myConection import MyConection


class Api():
    def __init__(self):
       self.mongoDB = DBconection()                           
       self.mongodbConection = MyConection(self.mongoDB,self.mongoDB.getColection())
       
    def getDay(self, day):
        self.mongodbConection.getDay(day)
    
    def getTotalofDay(self, name):
        totalDay = self.mongodbConection.findINcolection(name)
        return totalDay
                
    def addDayAgulhaMongoDB(self, data):    
        self.mongodbConection.insert_document(data)
    
    def deleteTurn(self, turn):
        self.mongodbConection.deleteTurn(turn)
    
    def deleteDay(self, day):
        self.mongodbConection.deleteDay(day)
        
  