from api.api import Api


class ProductsService:
    def __init__(self):
        self.api = Api()
     
    def adduserIdMonthId(self, monthIdData):
        self.api.getMountId(monthIdData)      
        
    def addDayAgulhaBrokeMongoDB(self, algulhas):
        self.api.addDayAgulhaMongoDB(algulhas)
        
    def getMountId(self):
        self.api.getMountId()   
        
    def getFinuras(self):
        self.api.getFinuras()
    
    def getTotalofDay(self, name):
        totalDay = self.api.getTotalofDay(name)
        return totalDay
   
        