from api.api import Api


class ProductsService:
    def __init__(self):
        self.api = Api()
     
    def addDayAgulhaBrokeMongoDB(self, algulhas):
        self.api.addDayAgulhaMongoDB(algulhas)
              
    def getDay(self, day):
        self.api.getDay(day)
    
    def getTotalofDay(self, name):
        totalDay = self.api.getTotalofDay(name)
        return totalDay
    
    def deleteTurn(self, turn):
        self.api.deleteTurn(turn) 
        
    def deleteDay(self, day):
        self.api.deleteDay(day)
   
        