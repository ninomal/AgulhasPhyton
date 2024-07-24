from models.conection.conection import DBconection
from models.repository.myConection import MyConection


class Api():
    def __init__(self):
       self.mongoDB = DBconection()                           
       self.mongodbConection = MyConection(self.mongoDB,self.mongoDB.getColection())
       
    def getDay(self, month , setor, day):
        daySlect = {{"2024":month}, {setor:day}}
        self.mongodbConection.getDay(daySlect)
    
    def getDocumentFind(self, name):
        documentionFind = self.mongodbConection.findINcolection(name)
        return documentionFind
                
    def addDayAgulhaMongoDB(self, data):    
        self.mongodbConection.insert_document(data)
        
    def deleteDay(self, day):
        self.mongodbConection.deleteDay(day)
        
  