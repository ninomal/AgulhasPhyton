from api.api import Api


class ProductsService:
    def __init__(self):
        self.api = Api()
     
    def addDayAgulhaBrokeMongoDB(self, algulhas):
        self.api.addDayAgulhaMongoDB(algulhas)
              
    def getDay(self, month , setor, day):
        self.api.getDay(month , setor, day)
    
    def getDocumentFind(self, name):
        document = self.api.getDocumentFind(name)
        return document
    
    def deleteTurn(self, turn):
        self.api.deleteTurn(turn) 
        
    def deleteDay(self, day):
        self.api.deleteDay(day)
   
        